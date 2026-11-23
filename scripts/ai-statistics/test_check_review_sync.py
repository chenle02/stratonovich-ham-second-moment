"""Focused failure controls for the final review-sync gate; no real release actions."""
import copy
import datetime as dt
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
spec = importlib.util.spec_from_file_location("review_sync_gate", HERE / "check_review_sync.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class ReviewSyncGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        historical = (REPO / gate.HISTORICAL).read_bytes()
        current = json.loads((REPO / gate.LEDGER).read_text())
        current["snapshot_utc"] = "2026-11-15T00:00:00+00:00"
        self.write(gate.HISTORICAL, historical)
        self.write(gate.LEDGER, json.dumps(current))
        self.write(str(Path(gate.LEDGER).with_suffix(".schema.json")), "{}")
        self.write(gate.CHECKER, (HERE / "check_review_sync.py").read_bytes())
        self.write(gate.GENERATOR, "import sys\nassert '--check' in sys.argv\n")
        self.write("AGENTS.md", "Release review sync is a final gate.\n")
        self.write("AI-USE-STATEMENT.md", "Known grades retained; whole-run totals unknown.\n")
        self.write("notes/ai-statistics.tex", "Two scoped acceptances; historical status retained.\n")
        self.write("notes/ai-statistics-data.tex", "Generated fixture data\n")
        self.write("notes/shared-input.tex", "Exact source fixture\n")
        for name in gate.BOOKS:
            self.write(name + ".tex", "\\input{notes/shared-input}\n")
            self.write(name + ".pdf", b"%PDF-1.7 fixture artifact\n")
            self.write(name + ".bbl", "Bibliography fixture\n")
        self.selected_evidence = "experiment/ledger-updates/2026-11-15-evidence-update/observations.json"
        self.selected_inventory = "experiment/ledger-updates/2026-11-15-evidence-update/review-attempts.json"
        self.selected_tokens = "scripts/ai-statistics/tokens/fixture.json"
        self.write(self.selected_evidence, '{"observations": []}\n')
        self.write(self.selected_inventory, '{"attempts": []}\n')
        self.write(self.selected_tokens, '{"snapshot": "fixture"}\n')
        self.selection = {
            "note": "Selected fixture inputs; no provider/lifetime claim.",
            "review_evidence": {"path": "../../" + self.selected_evidence,
                                "sha256": gate.digest((self.root / self.selected_evidence).read_bytes())},
            "review_inventory": {"path": "../../" + self.selected_inventory,
                                 "sha256": gate.digest((self.root / self.selected_inventory).read_bytes())},
            "tokens": {"path": "tokens/fixture.json",
                       "sha256": gate.digest((self.root / self.selected_tokens).read_bytes())},
        }
        self.write(gate.SELECTION, json.dumps(self.selection))
        self.decision_name = "experiment/ledger-updates/2026-11-15-cold-closeout/PU-DISPOSITION.json"
        self.write(self.decision_name, (REPO / self.decision_name).read_bytes())
        for row in current["rows"]:
            self.write(gate.summary_path(self.root, gate.LEDGER, row), "Author process summary " + row["id"])
        self.manifest = {
            "schema": "appendix-review-sync/1", "ledger": gate.LEDGER,
            "historical_ledger": gate.HISTORICAL,
            "recent_ids": [r["id"] for r in current["rows"][29:]],
            "expected_recent_rows": copy.deepcopy(current["rows"][29:]),
            "reconciliation_scope": "Captured closeout only, no lifetime/whole-book claim.",
            "decision_evidence": {"C016": {
                "authority": "Le direct conversation", "date": "2026-11-15",
                "bounded_exception": True, "aggregate_cap_verified": False,
                "receipt": self.decision_name, "receipt_sha256": gate.PU_DECISION_SHA256}},
            "required_text_fragments": {
                "AI-USE-STATEMENT.md": ["whole-run totals unknown"],
                "notes/ai-statistics.tex": ["historical status retained"]},
        }
        self.seal()

    def write(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data.encode() if isinstance(data, str) else data)

    def seal(self):
        self.manifest["artifacts_sha256"] = {
            p.relative_to(self.root).as_posix(): gate.digest(p.read_bytes())
            for p in self.root.rglob("*") if p.is_file() and ".git" not in p.parts
            and p != self.root / gate.MANIFEST}
        self.write(gate.MANIFEST, json.dumps(self.manifest))

    def rewrite_ledger(self, mutate, update_expected=False):
        data = json.loads((self.root / gate.LEDGER).read_text())
        mutate(data)
        self.write(gate.LEDGER, json.dumps(data))
        if update_expected:
            self.manifest["expected_recent_rows"] = copy.deepcopy(data["rows"][29:])
        self.seal()

    def check(self, **kwargs):
        return gate.validate(self.root, **kwargs)

    def test_valid_snapshot_runs_generator_without_writes(self):
        before = {p.relative_to(self.root): gate.digest(p.read_bytes())
                  for p in self.root.rglob("*") if p.is_file()}
        result = self.check()
        self.assertEqual(result["historical_rows_unchanged"], 29)
        self.assertEqual(result["named_summaries"], 35)
        self.assertEqual(result["mode"], "snapshot")
        self.assertEqual(before, {p.relative_to(self.root): gate.digest(p.read_bytes())
                                 for p in self.root.rglob("*") if p.is_file()})

    def test_redacted_file_is_accepted_only_on_the_public_tree_with_markers(self):
        self.manifest["redacted_on_export"] = ["AGENTS.md"]
        self.seal()
        self.write("AGENTS.md", "Release review sync is a final gate.\n[held back: private planning]\n")
        result = gate.validate(self.root, run_generator=False)
        self.assertEqual(result["redacted_on_export_unverified"], ["AGENTS.md"])
        self.assertEqual(result["artifacts_verified"], len(self.manifest["artifacts_sha256"]) - 1)

    def test_redacted_file_without_markers_still_fails(self):
        self.manifest["redacted_on_export"] = ["AGENTS.md"]
        self.seal()
        self.write("AGENTS.md", "Release review sync is a final gate, edited.\n")
        with self.assertRaisesRegex(gate.SyncError, "changed after review-sync sealing: AGENTS.md"):
            gate.validate(self.root, run_generator=False)

    def test_unlisted_file_with_markers_still_fails(self):
        self.seal()
        self.write("AGENTS.md", "Release review sync is a final gate.\n<HOME>/x\n")
        with self.assertRaisesRegex(gate.SyncError, "changed after review-sync sealing: AGENTS.md"):
            gate.validate(self.root, run_generator=False)

    def test_private_tree_verifies_listed_files_by_hash(self):
        self.manifest["redacted_on_export"] = ["AGENTS.md"]
        self.seal()
        (self.root / "private").mkdir()
        self.write("AGENTS.md", "Release review sync is a final gate.\n[held back: private planning]\n")
        with self.assertRaisesRegex(gate.SyncError, "changed after review-sync sealing: AGENTS.md"):
            gate.validate(self.root, run_generator=False)

    def test_redacted_list_must_name_sealed_artifacts(self):
        self.manifest["redacted_on_export"] = ["not-sealed.md"]
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "redacted_on_export must list sealed artifact paths"):
            gate.validate(self.root, run_generator=False)

    def test_historical_row_cannot_be_rewritten(self):
        self.rewrite_ledger(lambda d: d["rows"][0].update(reported_confidence="high"))
        with self.assertRaisesRegex(gate.SyncError, "Historical 29"):
            self.check()

    def test_raw_tokens_cannot_change_even_with_resealed_expected_rows(self):
        def mutate(d):
            d["rows"][-6]["token_usage_reported"]["input"] += 1
        self.rewrite_ledger(mutate, update_expected=True)
        with self.assertRaisesRegex(gate.SyncError, "Frozen reported"):
            self.check()

    def test_scoped_disposition_cannot_be_upgraded(self):
        self.rewrite_ledger(lambda d: d["rows"][-5].update(accepted_at_stated_scope=True), True)
        with self.assertRaisesRegex(gate.SyncError, "Scientific disposition"):
            self.check()

    def test_whole_book_acceptance_cannot_be_inferred_from_local_pass(self):
        self.rewrite_ledger(lambda d: d["rows"][-4].update(WHOLE_BOOK_ACCEPTED=True), True)
        with self.assertRaisesRegex(gate.SyncError, "Whole-book acceptance"):
            self.check()

    def test_pdf_source_pair_is_hash_bound(self):
        self.write(gate.BOOKS[0] + ".pdf", b"Changed PDF after sealing")
        with self.assertRaisesRegex(gate.SyncError, "Artifact changed"):
            self.check()

    def test_missing_combined_pdf_cannot_be_omitted_from_the_seal(self):
        (self.root / "notes/combined.pdf").unlink()
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "hashes absent.*notes/combined.pdf"):
            self.check()

    def test_combined_pdf_and_bibliography_remain_hash_bound(self):
        for name in ("notes/combined.pdf", "notes/combined.bbl"):
            with self.subTest(name=name):
                original = (self.root / name).read_bytes()
                self.write(name, b"Changed after sealing")
                with self.assertRaisesRegex(gate.SyncError, "Artifact changed.*" + name):
                    self.check()
                self.write(name, original)

    def test_missing_selection_or_review_selection_is_fatal(self):
        original = (self.root / gate.SELECTION).read_bytes()
        (self.root / gate.SELECTION).unlink()
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "Required file missing.*selection.json"):
            self.check()
        self.write(gate.SELECTION, original)
        del self.selection["review_inventory"]
        self.write(gate.SELECTION, json.dumps(self.selection))
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "review_evidence and review_inventory"):
            self.check()

    def test_selected_input_missing_or_changed_is_fatal_even_when_resealed(self):
        original = (self.root / self.selected_evidence).read_bytes()
        (self.root / self.selected_evidence).unlink()
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "Required file missing.*observations.json"):
            self.check()
        self.write(self.selected_evidence, original + b" ")
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "differs from selection.json.*review_evidence"):
            self.check()

    def test_every_selection_and_selection_file_requires_manifest_hash(self):
        for name in (gate.SELECTION, self.selected_inventory, self.selected_tokens):
            with self.subTest(name=name):
                saved = self.manifest["artifacts_sha256"].pop(name)
                self.write(gate.MANIFEST, json.dumps(self.manifest))
                with self.assertRaisesRegex(gate.SyncError, "hashes absent"):
                    self.check()
                self.manifest["artifacts_sha256"][name] = saved
        self.write(gate.MANIFEST, json.dumps(self.manifest))

    def test_selected_parent_paths_are_allowed_only_inside_the_repo(self):
        self.assertEqual(self.check()["status"], "PASS")  # ../../experiment works
        self.selection["review_evidence"]["path"] = "../../../outside.json"
        self.write(gate.SELECTION, json.dumps(self.selection))
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "Selected input escapes"):
            self.check()

    def test_omitted_input_source_cannot_hide_in_sparse_manifest(self):
        del self.manifest["artifacts_sha256"]["notes/shared-input.tex"]
        self.write(gate.MANIFEST, json.dumps(self.manifest))
        with self.assertRaisesRegex(gate.SyncError, "hashes absent"):
            self.check()

    def test_named_historical_summary_is_required(self):
        data = json.loads((self.root / gate.LEDGER).read_text())
        name = gate.summary_path(self.root, gate.LEDGER, data["rows"][0])
        (self.root / name).unlink()
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "hashes absent"):
            self.check()

    def test_pu_needs_direct_exception_and_keeps_unknown_cap(self):
        self.manifest["decision_evidence"]["C016"]["aggregate_cap_verified"] = True
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "bounded exception"):
            self.check()

    def test_partial_pu_usage_cannot_be_relabelled_full(self):
        self.rewrite_ledger(lambda d: d["rows"][-2].update(accounting_scope="Whole invocation"), True)
        with self.assertRaisesRegex(gate.SyncError, "final-step usage"):
            self.check()

    def test_missing_approved_disclosure_fragment_fails(self):
        self.write("AI-USE-STATEMENT.md", "No caveat here")
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "disclosure fragment missing"):
            self.check()

    def test_public_sync_manifest_cannot_publish_private_draft_locator(self):
        self.manifest["decision_evidence"]["private_draft"] = "private/drafts/held-review.json"
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "must not contain private"):
            self.check()

    def test_generator_staleness_is_fatal(self):
        self.write(gate.GENERATOR, "raise SystemExit('fixture stale')\n")
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "generated data are stale"):
            self.check()

    def test_duplicate_inventory_and_path_escape_fail(self):
        self.manifest["recent_ids"].append("C017")
        self.seal()
        with self.assertRaisesRegex(gate.SyncError, "inventory"):
            self.check()
        self.manifest["recent_ids"].pop()
        self.manifest["artifacts_sha256"]["../outside"] = "a" * 64
        self.write(gate.MANIFEST, json.dumps(self.manifest))
        with self.assertRaisesRegex(gate.SyncError, "repository-relative"):
            self.check()

    def init_release(self):
        env = {**os.environ, "GIT_AUTHOR_NAME": "Fixture", "GIT_COMMITTER_NAME": "Fixture",
               "GIT_AUTHOR_EMAIL": "fixture", "GIT_COMMITTER_EMAIL": "fixture",
               "GIT_AUTHOR_DATE": "2026-11-15T01:00:00+00:00", "GIT_COMMITTER_DATE": "2026-11-15T01:00:00+00:00"}
        for args in [("init", "-q"), ("add", "."), ("-c", "core.hooksPath=/dev/null", "commit", "-q", "-m", "fixture")]:
            subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True, env=env)
        return gate.git(self.root, "rev-parse", "HEAD")

    def attestation(self, release):
        # External to the clean release checkout, so no receipt self-reference.
        fd, name = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        path = Path(name)
        self.addCleanup(path.unlink)
        value = {"release_sha": release,
                 "review_sync_sha256": gate.digest((self.root / gate.MANIFEST).read_bytes()),
                 "authority": "Le or designated release owner", "attested_by": "Fixture owner",
                 "recorded_utc": "2026-11-15T23:00:00+00:00",
                 "all_reviews_reconciled": True, "scientific_acceptance_separate": True}
        path.write_text(json.dumps(value))
        return path

    def test_final_requires_exact_clean_sha_and_external_attestation(self):
        release = self.init_release()
        with self.assertRaisesRegex(gate.SyncError, "external release-owner"):
            self.check(release_sha=release)
        receipt = self.attestation(release)
        self.assertEqual(self.check(release_sha=release, attestation=receipt)["mode"], "exact-release")
        changed = json.loads(receipt.read_text())
        changed["release_sha"] = "0" * 40
        receipt.write_text(json.dumps(changed))
        with self.assertRaisesRegex(gate.SyncError, "stale or bound"):
            self.check(release_sha=release, attestation=receipt)

    def test_final_stale_receipt_and_dirty_tree_fail(self):
        release = self.init_release()
        receipt = self.attestation(release)
        value = json.loads(receipt.read_text())
        value["recorded_utc"] = "2020-01-01T00:00:00+00:00"
        receipt.write_text(json.dumps(value))
        with self.assertRaisesRegex(gate.SyncError, "predates"):
            self.check(release_sha=release, attestation=receipt)

    def test_final_receipt_must_bind_manifest_and_attest_inventory(self):
        release = self.init_release()
        receipt = self.attestation(release)
        original = json.loads(receipt.read_text())
        for field, value, error in [
            ("review_sync_sha256", "0" * 64, "stale or bound"),
            ("all_reviews_reconciled", False, "explicitly attest"),
            ("scientific_acceptance_separate", False, "explicitly attest"),
        ]:
            with self.subTest(field=field):
                changed = {**original, field: value}
                receipt.write_text(json.dumps(changed))
                with self.assertRaisesRegex(gate.SyncError, error):
                    self.check(release_sha=release, attestation=receipt)
        self.write("untracked-work", "Must not be silently exported")
        with self.assertRaisesRegex(gate.SyncError, "clean exact-SHA"):
            self.check(release_sha=release, attestation=receipt)


class AccountingScopeNoteTests(unittest.TestCase):
    def test_final_step_note_names_scopes_not_shared_formats(self):
        spec = importlib.util.spec_from_file_location("appendix_scope_note", HERE / "make_appendix.py")
        appendix = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(appendix)
        panel = "Panel header/final-step usage only; not verified full-session totals"
        partial = "header/final-step usage only; previous abandoned stream usage unknown; not full invocation totals."
        full = "One native assistant response; reported token object. No broader session accounting inferred."
        rows = ([{"accounting_scope": panel, "token_format_signature": "D"}] * 4 +
                [{"accounting_scope": partial, "token_format_signature": "A"}] +
                [{"accounting_scope": full, "token_format_signature": "A"}] * 10)
        note = appendix.header_note(rows, {panel: "S2", partial: "S4", full: "S3"})
        self.assertIn("5 records with scopes~S2 and~S4", note)
        self.assertNotIn("format", note)
        self.assertNotIn("S3", note)
        self.assertEqual(appendix.header_note(rows[-10:], {full: "S3"}), "")


if __name__ == "__main__":
    unittest.main()
