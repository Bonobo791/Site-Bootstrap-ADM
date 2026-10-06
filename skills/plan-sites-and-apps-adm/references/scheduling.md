# Cycles, capacity and dependencies

## Establish a calendar

Ask for exact start date, hard/flexible launch target, timezone, working days, each resource's available hours, absences and review response times. Default to the user's known timezone; verify it for a cross-timezone team. Interpret “next month” as a planning window, not an invented launch date. If delegated, propose an explicit date/cadence/capacity and label it provisional until accepted.

Use native cycles with real `YYYY-MM-DD` start/end dates. Treat dates as inclusive planning days. A seven-day cycle starting 2026-10-12 ends 2026-10-18; the next starts 2026-10-19. Require next start strictly after previous end so cycles do not overlap at a boundary. Review/contingency may occupy part of a cycle. A cycle is a timebox, not a phase label or an agent cron schedule.

## Calculate commitments

For each resource and cycle:

`committable minutes = available working minutes - known non-project commitments - review/admin allocation - contingency reserve`

Record the inputs and the net result. When available hours already exclude other work, do not subtract that work twice. Make reviews/contingency either reserved capacity or scheduled tasks, not both. Estimate hands-on effort separately from provider/reviewer wait time. Leave unselected/unavailable resource capacity at zero; model shared bottlenecks such as one operator configuring all services.

Sum chosen effort estimates for that resource's scheduled leaf tasks. Keep the sum at or below net cycle capacity. Use estimate ranges/confidence in the plan, not precision unsupported by experience. Reserve a named launch-fix window; zero contingency requires an explicit accepted reason. Avoid treating agents as unlimited free capacity or assigning parallel work to a single person beyond availability.

## Order work

1. Build a dependency graph from prerequisites and real external gates. Detect cycles and unresolved dependencies.
2. Schedule provider/account/decision/content approvals early enough to unblock downstream tasks.
3. Place ready work in the earliest cycle with capacity. Dependencies must finish before dependent work begins; same-day ordering requires a documented sequence.
4. Include time for end-to-end verification, real provider operation, recovery, release and observation before claiming the target date feasible.
5. Check longest dependency path, per-resource overload and calendar lead times against the launch target.
6. When the deadline does not fit, present the specific conflict and options to reduce scope, add capacity or change dates. Preserve must-have outcomes and obtain a scope/timeline decision.

Initiative start/target dates encompass their scheduled tasks. Task dates fit within their cycle and initiative. An initiative can span cycles; a cycle can deliver tasks from multiple initiatives. A task spanning cycles should be split into independently verifiable work or left unscheduled until decomposed.

## Unknowns and later work

Schedule a bounded decision/access task when the work to resolve a blocker is understood. Keep the blocked implementation task in backlog with no cycle/dates until there is an agreed reliable prerequisite date. A planned prerequisite task and dependent implementation may both be scheduled when the prerequisite's completion is expected and its contingency is explicit; keep the dependency link and gate visible.

Use `readiness: ready` for work with sufficiently defined inputs, `blocked` for unresolved external/decision blockers and `later` for deferred scope. “Ready” does not mean dependencies have already been performed. Deferred tasks keep their initiative/requirements and have no native cycle/due-date commitment. Never count backlog effort as a delivered cycle commitment.

## Validate and revise

The manifest uses the following fields. Copy the empty template for a real plan; its empty arrays intentionally fail a ready-calendar check. The bundled example is a three-task allocation demonstration, not a complete product launch.

| Object | Required schedule fields |
|---|---|
| Root | `planId`, IANA `timezone`, `initiatives`, `cycles`, `tasks` arrays |
| Initiative | Unique `id`, `startDate`, `targetDate`; both dates may be null for entirely unscheduled work |
| Cycle | Unique `id`, `startDate`, `endDate`, `capacityMinutes` mapping agreed resource names to net integer minutes |
| Task | Unique `id`, existing `initiativeId`, `readiness` (`ready/blocked/later`), `dependsOn` array of task IDs |
| Scheduled task | Existing `cycleId`, `resource` with cycle capacity, positive integer `estimateMinutes`, `startDate`, `dueDate` |
| Unscheduled task | `cycleId`, `startDate`, `dueDate` null or absent; other planning details live in the full task record |

Use resource names consistently; resolve these to actual assignable members at publication. Include only leaf execution effort in the manifest, keeping parent grouping estimates separate.

Run `python3 scripts/validate_schedule.py <schedule.json>` from the skill directory. Review dates, role/member mapping, estimate confidence, accepted assumptions and critical path manually. The validator checks allocation arithmetic, not whether a person's day-by-day workload is realistic; inspect workdays and resource sequencing separately.

After publication, read back actual cycle/task membership and dates. Re-estimate before moving incomplete work to the next cycle; recalculate capacity/dependencies and update initiative targets and the plan document. Do not finish/delete cycles, alter historical records or shift deadlines silently. Reuse existing cycles when resuming the same plan. If an existing project is explicitly chosen, reconcile its calendar before adding cycles.
