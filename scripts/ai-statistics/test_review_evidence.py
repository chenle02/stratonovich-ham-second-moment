"""Failure controls for additive chronology; no provider or release actions."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location("appendix_evidence", HERE / "make_appendix.py")
appendix = importlib.util.module_from_spec(spec)
spec.loader.exec_module(appendix)
BASE = ROOT / "experiment/ledger-updates/2026-11-15-evidence-update"


class ReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.updates = json.loads((BASE / "observations.json").read_text())
        self.inventory = json.loads((BASE / "review-attempts.json").read_text())
        self.ledger = json.loads((ROOT / appendix.LEDGER_DEFAULT).read_text())
        self.later = json.loads((HERE / "reviews/later-attempts-2026-11-15.json").read_text())

    def check(self):
        return appendix.validate_review_evidence(
            self.updates, self.inventory, self.ledger, self.later)

    def test_valid_evidence_is_read_only(self):
        before = copy.deepcopy((self.updates, self.inventory, self.ledger, self.later))
        self.assertEqual(tuple(map(len, self.check())), (6, 3, 1))
        self.assertEqual(before, (self.updates, self.inventory, self.ledger, self.later))

    def test_unknown_inventory_schema_is_refused(self):
        self.inventory["schema"] = "unreviewed-schema"
        with self.assertRaisesRegex(ValueError, "inventory schema"):
            self.check()

    def test_conflicting_base_snapshot_is_refused(self):
        self.inventory["base_snapshot"]["row_count"] = 36
        with self.assertRaisesRegex(ValueError, "base snapshots"):
            self.check()

    def test_duplicate_attempt_is_refused(self):
        self.inventory["attempts"][1]["id"] = self.inventory["attempts"][0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.check()

    def test_unreconciled_day_totals_are_refused(self):
        self.inventory["attempts"][0]["date_utc"] = "2026-11-16"
        with self.assertRaisesRegex(ValueError, "day totals"):
            self.check()

    def test_base_row_cannot_be_counted_twice(self):
        rows = [r for r in self.inventory["attempts"] if r["base_record_id"]]
        rows[1]["base_record_id"] = rows[0]["base_record_id"]
        with self.assertRaisesRegex(ValueError, "exactly once"):
            self.check()

    def test_unknown_p2_model_cannot_be_promoted(self):
        row = next(r for r in self.inventory["attempts"]
                   if r["base_record_id"] == "P2-deepseek")
        row["actual_model"] = "deepseek/deepseek-v4-pro"
        with self.assertRaisesRegex(ValueError, "actual attribution"):
            self.check()

    def test_client_clock_cannot_be_promoted_to_launch(self):
        row = next(r for r in self.updates["observations"] if r["record_id"] == "P1-cold")
        row["recorded_start_utc"] = row["client_session_created_utc"]
        with self.assertRaisesRegex(ValueError, "promoted"):
            self.check()

    def test_bound_cannot_become_point_clock(self):
        row = next(r for r in self.inventory["attempts"]
                   if r["base_record_id"] == "P2-deepseek")
        row["time_evidence"]["started_utc"] = "2026-11-13T05:29:59.353149Z"
        with self.assertRaisesRegex(ValueError, "point clock"):
            self.check()

    def test_frozen_running_is_not_current_terminal(self):
        row = next(r for r in self.updates["observations"] if r["record_id"] == "C011")
        row["later_native_status_label"] = "running"
        with self.assertRaisesRegex(ValueError, "C011"):
            self.check()

    def test_timeline_cannot_gain_grade_projection(self):
        self.inventory["attempts"][0]["verdict"] = "PASS"
        with self.assertRaisesRegex(ValueError, "quality projection"):
            self.check()

    def test_policy_does_not_grant_scientific_acceptance(self):
        self.updates["policy_decision"]["new_whole_book_acceptance"] = True
        with self.assertRaisesRegex(ValueError, "acceptance"):
            self.check()


if __name__ == "__main__":
    unittest.main()
