"""Check schedule integrity before creating native project cycles and tasks."""
import argparse
from collections import defaultdict, deque
from datetime import date
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def validate(plan):
    errors = []
    if not isinstance(plan, dict):
        return ["plan must be an object"]
    if not isinstance(plan.get("planId"), str) or not plan["planId"].strip():
        errors.append("planId is required")
    try:
        ZoneInfo(plan.get("timezone", ""))
    except (ZoneInfoNotFoundError, ValueError, TypeError):
        errors.append("invalid timezone: use an IANA name")

    def day(value, label):
        if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            errors.append(f"{label}: invalid date; use YYYY-MM-DD")
            return None
        try:
            return date.fromisoformat(value)
        except ValueError:
            errors.append(f"{label}: invalid date")
            return None

    def index(field):
        rows = plan.get(field)
        if not isinstance(rows, list):
            errors.append(f"{field} must be an array")
            return {}
        result = {}
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"].strip():
                errors.append(f"{field}: each record needs a nonempty string id")
                continue
            ident = row["id"]
            if ident in result:
                errors.append(f"{field}: duplicate id {ident}")
                continue
            result[ident] = row
        return result

    initiatives = index("initiatives")
    cycles = index("cycles")
    tasks = index("tasks")
    all_ids = [*initiatives, *cycles, *tasks]
    if len(all_ids) != len(set(all_ids)):
        errors.append("duplicate id across object types")
    if not cycles:
        errors.append("at least one cycle is required for a ready calendar")
    initiative_dates = {}
    for ident, row in initiatives.items():
        a, b = row.get("startDate"), row.get("targetDate")
        if a is None and b is None:
            initiative_dates[ident] = (None, None)
            continue
        start, end = day(a, f"{ident}.startDate"), day(b, f"{ident}.targetDate")
        initiative_dates[ident] = (start, end)
        if start and end and start > end:
            errors.append(f"{ident}: initiative dates reversed")

    cycle_dates = {}
    capacities = {}
    for ident, row in cycles.items():
        start = day(row.get("startDate"), f"{ident}.startDate")
        end = day(row.get("endDate"), f"{ident}.endDate")
        cycle_dates[ident] = (start, end)
        if start and end and start > end:
            errors.append(f"{ident}: cycle dates reversed")
        budget = row.get("capacityMinutes")
        if not isinstance(budget, dict):
            errors.append(f"{ident}: capacityMinutes must map resources to net minutes")
            budget = {}
        for resource, minutes in budget.items():
            if not isinstance(resource, str) or not resource.strip() or type(minutes) is not int or minutes < 0:
                errors.append(f"{ident}: invalid resource capacity")
        capacities[ident] = budget

    ordered = sorted((a, b, ident) for ident, (a, b) in cycle_dates.items() if a and b and a <= b)
    latest_end = None
    for start, end, ident in ordered:
        if latest_end is not None and start <= latest_end:
            errors.append(f"{ident}: cycles overlap (inclusive dates)")
        latest_end = max(latest_end, end) if latest_end else end

    usage = defaultdict(int)
    task_dates = {}
    graph = {}
    scheduled_count = 0
    for ident, row in tasks.items():
        initiative = row.get("initiativeId")
        if not isinstance(initiative, str) or initiative not in initiatives:
            errors.append(f"{ident}: unknown initiative")
            initiative = None
        readiness = row.get("readiness")
        if not isinstance(readiness, str) or readiness not in {"ready", "blocked", "later"}:
            errors.append(f"{ident}: readiness must be ready, blocked or later")
            readiness = None
        dependencies = row.get("dependsOn")
        if not isinstance(dependencies, list) or any(not isinstance(x, str) for x in dependencies):
            errors.append(f"{ident}: dependsOn must be an array of task ids")
            dependencies = []
        if len(dependencies) != len(set(dependencies)):
            errors.append(f"{ident}: duplicate dependency")
        graph[ident] = set(dependencies)
        for dependency in dependencies:
            if dependency not in tasks:
                errors.append(f"{ident}: unknown dependency {dependency}")
        cycle = row.get("cycleId")
        if cycle is not None and not isinstance(cycle, str):
            errors.append(f"{ident}: invalid cycle reference")
            task_dates[ident] = (None, None)
            continue
        if cycle is None:
            task_dates[ident] = (None, None)
            if row.get("startDate") is not None or row.get("dueDate") is not None:
                errors.append(f"{ident}: unscheduled task must have no dates")
            continue
        scheduled_count += 1
        if readiness in {"blocked", "later"}:
            errors.append(f"{ident}: blocked/later task is scheduled")
        if cycle not in cycles:
            errors.append(f"{ident}: unknown cycle")
        start = day(row.get("startDate"), f"{ident}.startDate")
        end = day(row.get("dueDate"), f"{ident}.dueDate")
        task_dates[ident] = (start, end)
        if start and end:
            if start > end:
                errors.append(f"{ident}: task dates reversed")
            a, b = cycle_dates.get(cycle, (None, None))
            if a and b and not (a <= start <= end <= b):
                errors.append(f"{ident}: task dates outside cycle")
            a, b = initiative_dates.get(initiative, (None, None))
            if initiative in initiatives and (not a or not b):
                errors.append(f"{ident}: scheduled task needs dated initiative")
            elif a and b and not (a <= start <= end <= b):
                errors.append(f"{ident}: task dates outside initiative")
        minutes, resource = row.get("estimateMinutes"), row.get("resource")
        if type(minutes) is not int or minutes <= 0:
            errors.append(f"{ident}: scheduled estimateMinutes must be a positive integer")
        elif not isinstance(resource, str) or resource not in capacities.get(cycle, {}):
            errors.append(f"{ident}: resource has no cycle capacity")
        else:
            usage[(cycle, resource)] += minutes

    if not scheduled_count:
        errors.append("at least one scheduled task is required for a ready calendar")
    for (cycle, resource), minutes in usage.items():
        capacity = capacities[cycle][resource]
        if type(capacity) is int and minutes > capacity:
            errors.append(f"{cycle}/{resource}: capacity exceeded ({minutes} > {capacity} minutes)")
    for ident, dependencies in graph.items():
        start, _ = task_dates.get(ident, (None, None))
        if tasks[ident].get("cycleId") is None:
            continue
        for dependency in dependencies:
            if dependency not in tasks:
                continue
            _, end = task_dates.get(dependency, (None, None))
            if tasks[dependency].get("cycleId") is None:
                errors.append(f"{ident}: dependency is unscheduled ({dependency})")
            elif start and end and end > start:
                errors.append(f"{ident}: dependency finishes after task starts ({dependency})")

    incoming = {ident: len([x for x in deps if x in tasks]) for ident, deps in graph.items()}
    outgoing = defaultdict(list)
    for ident, deps in graph.items():
        for dependency in deps:
            if dependency in tasks:
                outgoing[dependency].append(ident)
    ready = deque(ident for ident, n in incoming.items() if n == 0)
    seen = 0
    while ready:
        ident = ready.popleft()
        seen += 1
        for target in outgoing[ident]:
            incoming[target] -= 1
            if incoming[target] == 0:
                ready.append(target)
    if seen != len(tasks):
        errors.append("dependency cycle: resolve circular task prerequisites")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schedule", type=Path)
    args = parser.parse_args()
    try:
        plan = json.loads(args.schedule.read_text())
        errors = validate(plan)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        parser.exit(2, f"Cannot read schedule: {type(error).__name__}\n")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Schedule references, dates, dependency order and cycle capacity verified.")
    print("User agreement, estimate quality, workday sequencing and launch readiness need separate review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
