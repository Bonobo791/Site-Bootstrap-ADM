"""Exercise calendar failures that would create misleading project commitments."""
import copy
import unittest

from validate_schedule import validate


def fixture():
    return {
        "planId": "cleaning-launch-v1", "timezone": "America/New_York",
        "initiatives": [{"id": "I01", "startDate": "2026-10-12", "targetDate": "2026-10-25"}],
        "cycles": [
            {"id": "CY01", "startDate": "2026-10-12", "endDate": "2026-10-18", "capacityMinutes": {"builder": 480}},
            {"id": "CY02", "startDate": "2026-10-19", "endDate": "2026-10-25", "capacityMinutes": {"builder": 300}},
        ],
        "tasks": [
            {"id": "T001", "initiativeId": "I01", "cycleId": "CY01", "readiness": "ready", "resource": "builder", "estimateMinutes": 240, "startDate": "2026-10-12", "dueDate": "2026-10-14", "dependsOn": []},
            {"id": "T002", "initiativeId": "I01", "cycleId": "CY01", "readiness": "ready", "resource": "builder", "estimateMinutes": 180, "startDate": "2026-10-15", "dueDate": "2026-10-18", "dependsOn": ["T001"]},
            {"id": "T003", "initiativeId": "I01", "cycleId": "CY02", "readiness": "ready", "resource": "builder", "estimateMinutes": 300, "startDate": "2026-10-19", "dueDate": "2026-10-23", "dependsOn": ["T002"]},
        ],
    }


class ScheduleChecks(unittest.TestCase):
    def setUp(self):
        self.plan = copy.deepcopy(fixture())

    def rejects(self, fragment):
        self.assertTrue(any(fragment in error for error in validate(self.plan)), validate(self.plan))

    def test_valid_calendar_and_capacity(self):
        self.assertEqual(validate(self.plan), [])

    def test_inclusive_cycle_boundaries_cannot_overlap(self):
        self.plan["cycles"][1]["startDate"] = "2026-10-18"
        self.rejects("overlap")

    def test_resource_capacity_is_not_pooled_between_cycles(self):
        self.plan["tasks"][0]["estimateMinutes"] = 400
        self.rejects("capacity exceeded")

    def test_unknown_cycle_is_rejected(self):
        self.plan["tasks"][0]["cycleId"] = "CY99"
        self.rejects("unknown cycle")

    def test_tasks_must_fit_cycle_dates(self):
        self.plan["tasks"][2]["dueDate"] = "2026-10-26"
        self.rejects("outside cycle")

    def test_blocked_work_cannot_be_committed(self):
        self.plan["tasks"][0]["readiness"] = "blocked"
        self.rejects("blocked/later task is scheduled")

    def test_dependency_finishes_before_dependent_starts(self):
        self.plan["tasks"][1]["startDate"] = "2026-10-13"
        self.rejects("dependency finishes after task starts")

    def test_graph_cycle_is_rejected(self):
        self.plan["tasks"][0]["dependsOn"] = ["T003"]
        self.rejects("dependency cycle")

    def test_missing_dependency_is_rejected(self):
        self.plan["tasks"][2]["dependsOn"] = ["T999"]
        self.rejects("unknown dependency")

    def test_duplicate_ids_are_rejected(self):
        self.plan["tasks"].append(copy.deepcopy(self.plan["tasks"][0]))
        self.rejects("duplicate id")

    def test_unscheduled_prerequisite_blocks_committed_task(self):
        self.plan["tasks"][0].update(cycleId=None, startDate=None, dueDate=None)
        self.rejects("dependency is unscheduled")

    def test_later_work_can_remain_undated_backlog(self):
        self.plan["tasks"].append({"id": "T004", "initiativeId": "I01", "readiness": "later", "cycleId": None, "startDate": None, "dueDate": None, "dependsOn": ["T003"]})
        self.assertEqual(validate(self.plan), [])

    def test_invalid_date_and_timezone_are_rejected(self):
        self.plan["timezone"] = "Mars/Olympus"
        self.plan["cycles"][0]["startDate"] = "2026-02-30"
        self.rejects("invalid timezone")
        self.rejects("invalid date")

    def test_initiative_must_encompass_task_dates(self):
        self.plan["initiatives"][0]["targetDate"] = "2026-10-20"
        self.rejects("outside initiative")

    def test_malformed_references_report_errors_instead_of_crashing(self):
        self.plan["tasks"][0]["initiativeId"] = {"id": "I01"}
        self.plan["tasks"][0]["cycleId"] = ["CY01"]
        self.plan["tasks"][0]["readiness"] = {"state": "ready"}
        self.rejects("invalid cycle reference")

    def test_unresolved_template_is_not_a_ready_calendar(self):
        self.plan["cycles"] = []
        self.plan["tasks"] = []
        self.rejects("at least one cycle")
        self.rejects("at least one scheduled task")


if __name__ == "__main__":
    unittest.main()
