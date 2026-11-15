#!/usr/bin/env python3
"""Read-only ledger/Appendix E synchronization gate.

Snapshot: python3 scripts/ai-statistics/check_review_sync.py
Final: add --release-sha EXACT_SHA --attestation /external/owner-receipt.json

Final mode must run in a clean detached checkout of EXACT_SHA (a local shared
clone is sufficient). No export, fetch, build, ledger rewrite or provider call
is performed. make_appendix.py --check is always run by the command-line gate.

An external owner attests that *all* final public/private review decisions were
reconciled. This program verifies that assertion's exact SHA/manifest binding;
it cannot discover future private reviews, authenticate a human signature, or
turn recorded grades into scientific/whole-book/release acceptance. No arbitrary
receipt expiry is imposed: final attestation must postdate the bound snapshot,
decision dates and release commit. Later reviews require renewed reconciliation.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

LEDGER = "experiment/ledger-updates/2026-11-15-cold-closeout/run-ledger-v4.json"
MANIFEST = "experiment/ledger-updates/2026-11-15-cold-closeout/REVIEW-SYNC.json"
HISTORICAL = "experiment/ledger-updates/2026-11-14-c003-provenance/run-ledger-v4.json"
HISTORICAL_SHA256 = "92275c3f06be56f61b52bce965459eeefeb22a4b43a2da12b85df172fc388fb2"
PU_DECISION_SHA256 = "1740a135ae58a59d27f318d5d0be45e260745d3218a0fee029f33f0e9456f6b3"
RAW_FIELDS = ("reported_verdict", "reported_confidence", "actual_model", "source_snapshot",
              "original_public_final_sha256", "token_usage_reported", "cost_reported",
              "cost_currency", "provider_calls")
# Frozen reported facts, not judgments of mathematical correctness. In C016 the
# token object is explicitly final-step-only; unknown invocation totals stay unknown.
RAW_FINGERPRINTS = {
    "C012": "b4f35bfcd0b5c75e394f24e2b349afc120dd13fa354dbef7b6ec8a8fd661cb47",
    "C013": "b6490e085981a1293a3a3aa0a54f77bfa3eac1a9ad87524ce5b5aacaa6b8f6a9",
    "C014": "2eb6dff9a4bcd0d2612c7decc8eb392883425cd3e013441ad363957886ae4ea1",
    "C015": "3e804f3112b1f97747902d8eb14b2a895afe43f1b649de1a87f4c04a5cf411dd",
    "C016": "9eec285f580bcf925beea08e5ed5d687193aef9a3dd7e0f5945ffbe3cce2fbc4",
    "C017": "1bac4b8d0c2d4cc28f82fbb975958afab8f73209c81d76c26f2e76d4b5933abe",
}
ACCEPTED = {"C012": False, "C013": False, "C014": True,
            "C015": False, "C016": True, "C017": False}
BOOKS = ("notes/notes_stratonovich_ham_second_moment",
         "notes/notes_stratonovich_ham_second_moment_reader",
         "notes/combined")
LANGUAGE_FILES = ("AI-USE-STATEMENT.md", "notes/ai-statistics.tex")
CHECKER = "scripts/ai-statistics/check_review_sync.py"
GENERATOR = "scripts/ai-statistics/make_appendix.py"
SELECTION = "scripts/ai-statistics/selection.json"
REQUIRED_REVIEW_SELECTIONS = ("review_evidence", "review_inventory")


class SyncError(Exception):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_fingerprint(row: dict) -> str:
    try:
        values = {name: row[name] for name in RAW_FIELDS}
    except KeyError as error:
        raise SyncError(f"Missing reported field: {error}") from error
    return digest(json.dumps(values, sort_keys=True, separators=(",", ":")).encode())


def checked_path(root: Path, name: str) -> Path:
    posix = PurePosixPath(name)
    if not name or posix.is_absolute() or ".." in posix.parts or "\\" in name:
        raise SyncError(f"Expected repository-relative artifact path: {name!r}")
    path = root / posix
    if not path.resolve().is_relative_to(root.resolve()):
        raise SyncError(f"Artifact escapes the release tree: {name}")
    if not path.is_file():
        raise SyncError(f"Required file missing: {name}")
    return path


def read_json(path: Path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise SyncError(f"Duplicate JSON key {key!r} in {path.name}")
            result[key] = value
        return result
    try:
        return json.loads(path.read_text(), object_pairs_hook=unique)
    except (OSError, UnicodeError, ValueError) as error:
        raise SyncError(f"Cannot read JSON {path.name}: {error}") from error


def reject_private_manifest_paths(value):
    """Bounded public-receipt check, not a substitute for the release filter."""
    if isinstance(value, dict):
        for key, item in value.items():
            reject_private_manifest_paths(key)
            reject_private_manifest_paths(item)
    elif isinstance(value, list):
        for item in value:
            reject_private_manifest_paths(item)
    elif isinstance(value, str) and ("private/" in value or "/home/" in value):
        raise SyncError("Public REVIEW-SYNC manifest must not contain private/runtime paths")


def timestamp(value, label):
    try:
        result = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, TypeError, ValueError) as error:
        raise SyncError(f"Invalid {label} timestamp") from error
    if result.tzinfo is None:
        raise SyncError(f"{label} timestamp must include a timezone")
    return result


def source_closure(root):
    """Conservative literal-input inventory; no TeX macro/conditional execution."""
    required, queue = set(), [book + ".tex" for book in BOOKS]
    while queue:
        name = queue.pop()
        if name in required:
            continue
        path = checked_path(root, name)
        required.add(name)
        for target in re.findall(r"\\input\{([^}]+)\}", path.read_text()):
            child = target if target.endswith(".tex") else target + ".tex"
            queue.append(child)
    for book in BOOKS:
        required.add(book + ".pdf")
        required.add(book + ".bbl")
    return required


def selected_artifacts(root):
    """Bind explicit inputs, not provider activity or lifetime completeness.

    Selection paths are relative to scripts/ai-statistics, unlike the manifest's
    repository-relative paths. A parent component is permitted only if the
    canonical target remains inside the release tree.
    """
    selection_path = checked_path(root, SELECTION)
    selection = read_json(selection_path)
    if not isinstance(selection, dict):
        raise SyncError("Appendix E selection must be a JSON object")
    if any(not isinstance(selection.get(key), dict) for key in REQUIRED_REVIEW_SELECTIONS):
        raise SyncError("Selection must name review_evidence and review_inventory")
    required = {SELECTION}
    for key, entry in selection.items():
        if not isinstance(entry, dict):
            continue  # e.g. the explanatory note; not a selected input
        name, expected_hash = entry.get("path"), entry.get("sha256")
        if (not isinstance(name, str) or not name or "\\" in name or
                PurePosixPath(name).is_absolute()):
            raise SyncError(f"Invalid selected path for {key}")
        target = (selection_path.parent / name).resolve()
        if not target.is_relative_to(root):
            raise SyncError(f"Selected input escapes the release tree: {key}")
        relative = target.relative_to(root).as_posix()
        path = checked_path(root, relative)
        if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
            raise SyncError(f"Invalid selected SHA256 for {key}")
        if digest(path.read_bytes()) != expected_hash:
            raise SyncError(f"Selected input differs from selection.json: {key}")
        required.add(relative)
    return required


def summary_path(root, ledger_name, row):
    name = row.get("report_summary")
    if not isinstance(name, str) or not name:
        raise SyncError(f"Missing summary locator for {row.get('id')}")
    path = (root / Path(ledger_name).parent / name).resolve()
    summary_root = (root / "experiment/reports").resolve()
    if not path.is_relative_to(summary_root) or path.suffix != ".md":
        raise SyncError(f"Summary locator outside experiment/reports: {name}")
    return path.relative_to(root.resolve()).as_posix()


def git(root, *args):
    process = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if process.returncode:
        raise SyncError(f"Read-only Git check failed: {' '.join(args)}")
    return process.stdout.strip()


def validate(root: Path, ledger_name=LEDGER, manifest_name=MANIFEST,
             release_sha=None, attestation=None, run_generator=True):
    root = root.resolve()
    manifest_path = checked_path(root, manifest_name)
    manifest = read_json(manifest_path)
    reject_private_manifest_paths(manifest)
    if manifest.get("schema") != "appendix-review-sync/1":
        raise SyncError("Unsupported REVIEW-SYNC schema")
    if manifest.get("ledger") != ledger_name or manifest.get("historical_ledger") != HISTORICAL:
        raise SyncError("Manifest does not select the explicit ledger/historical baseline")
    historical_path = checked_path(root, HISTORICAL)
    if digest(historical_path.read_bytes()) != HISTORICAL_SHA256:
        raise SyncError("Historical v4 ledger bytes changed")
    historical = read_json(historical_path)
    ledger = read_json(checked_path(root, ledger_name))
    if ledger.get("schema") != "publication-experiment-runs/4":
        raise SyncError("Selected ledger must use the recorded v4 schema")
    old_rows, rows = historical.get("rows"), ledger.get("rows")
    if not isinstance(old_rows, list) or len(old_rows) != 29 or not isinstance(rows, list):
        raise SyncError("Historical 29-row baseline or selected rows missing")
    if rows[:29] != old_rows:
        raise SyncError("Historical 29 row values/order were changed")
    ids = [row.get("id") for row in rows]
    if any(not isinstance(item, str) or not item for item in ids) or len(set(ids)) != len(ids):
        raise SyncError("Missing or duplicate ledger row identifiers")
    recent = manifest.get("recent_ids")
    if recent != ids[29:] or not set(RAW_FINGERPRINTS).issubset(set(recent or [])):
        raise SyncError("Review inventory does not reconcile all appended IDs, including C012–C017")
    expected = manifest.get("expected_recent_rows")
    if isinstance(expected, dict):
        expected = [expected.get(identifier) for identifier in recent]
    if expected != rows[29:]:
        raise SyncError("Recent row values differ from the sealed decision/telemetry inventory")
    if ledger.get("tokens_costs_recomputed") is not False or ledger.get("originals_preserved") is not True:
        raise SyncError("Reported telemetry/original-preservation flags changed")
    by_id = dict(zip(ids, rows))
    for identifier, expected_hash in RAW_FINGERPRINTS.items():
        row = by_id[identifier]
        if canonical_fingerprint(row) != expected_hash:
            raise SyncError(f"Frozen reported grade/usage/source/cost fields changed: {identifier}")
        accepted = ACCEPTED[identifier]
        if row.get("accepted_at_stated_scope") is not accepted:
            raise SyncError(f"Scientific disposition changed without a separately revised gate: {identifier}")
        if row.get("outcome") != ("accepted-at-scope" if accepted else "not-accepted"):
            raise SyncError(f"Outcome disagrees with scoped disposition: {identifier}")
    if any(row.get("WHOLE_BOOK_ACCEPTED") is not False for row in rows):
        raise SyncError("Whole-book acceptance is forbidden in this bounded ledger")
    if not all("partial" in by_id[item].get("adjudication_status", "").lower()
               for item in ("C015", "C017")):
        raise SyncError("IC and CH must remain explicitly qualified PARTIAL reconstructions")
    if not any(word in by_id["C013"].get("adjudication_status", "").lower()
               for word in ("partial", "qualified")):
        raise SyncError("Focused-parent evidence must retain its partial/qualified disposition")
    if not isinstance(manifest.get("reconciliation_scope"), str) or not manifest["reconciliation_scope"].strip():
        raise SyncError("Missing bounded review-inventory reconciliation scope")
    evidence = manifest.get("decision_evidence", {}).get("C016", {})
    if (evidence.get("authority") != "Le direct conversation" or
            evidence.get("date") != "2026-11-15" or evidence.get("bounded_exception") is not True or
            evidence.get("aggregate_cap_verified") is not False):
        raise SyncError("PU needs the explicit direct-Le bounded exception, with aggregate cap unverified")
    pu = by_id["C016"]
    if pu.get("provider_calls") is not None or pu.get("cost_reported") is not None or pu.get("cost_currency") is not None:
        raise SyncError("PU unknown complete invocation count/cost/currency was promoted to a known value")
    scope = pu.get("accounting_scope", "").lower()
    if "header/final-step" not in scope or "unknown" not in scope or "not full" not in scope:
        raise SyncError("PU final-step usage is not explicitly separated from unknown whole-invocation usage")
    telemetry = pu.get("telemetry_note", "").lower()
    if not (re.search(r"(?:two|2).*stream", telemetry) and "unknown" in telemetry and "aggregate cap" in telemetry):
        raise SyncError("PU must disclose two native streams and unknown aggregate usage/cap")
    receipt_name = evidence.get("receipt")
    if not isinstance(receipt_name, str) or not re.fullmatch(r"[0-9a-f]{64}", evidence.get("receipt_sha256", "")):
        raise SyncError("PU exception needs a hash-bound committed decision receipt")
    receipt = checked_path(root, receipt_name)
    if (digest(receipt.read_bytes()) != evidence["receipt_sha256"] or
            evidence["receipt_sha256"] != PU_DECISION_SHA256):
        raise SyncError("PU decision receipt does not match its declared hash")
    decision = read_json(receipt)
    if (decision.get("record_id") != "C016" or
            decision.get("accepted_at_stated_scope") is not True or
            decision.get("report_sha256") != pu["original_public_final_sha256"] or
            decision.get("automatic_retry_exception_approved") is not True or
            decision.get("aggregate_run_usage") is not None or decision.get("aggregate_run_cost") is not None or
            decision.get("aggregate_run_cap_compliance_verified") is not False or
            decision.get("whole_book_assurance_approved") is not False or
            decision.get("public_release_authorized") is not False):
        raise SyncError("PU bounded decision receipt does not preserve its scope and unknowns")
    required = {ledger_name, HISTORICAL, receipt_name, CHECKER, GENERATOR,
                "AGENTS.md", "AI-USE-STATEMENT.md", "notes/ai-statistics.tex",
                "notes/ai-statistics-data.tex", str(Path(ledger_name).with_suffix(".schema.json"))}
    summaries = [summary_path(root, ledger_name, row) for row in rows]
    required.update(summaries)
    required.update(source_closure(root))
    required.update(selected_artifacts(root))
    artifacts = manifest.get("artifacts_sha256")
    if not isinstance(artifacts, dict) or not required.issubset(artifacts):
        raise SyncError("Required source/PDF/summary/ledger/decision/generator hashes absent: " +
                        ", ".join(sorted(required - set(artifacts or {}))))
    for name, expected_hash in artifacts.items():
        path = checked_path(root, name)
        if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
            raise SyncError(f"Invalid SHA256 for {name}")
        if digest(path.read_bytes()) != expected_hash:
            raise SyncError(f"Artifact changed after review-sync sealing: {name}")
    fragments = manifest.get("required_text_fragments")
    if not isinstance(fragments, dict) or not set(LANGUAGE_FILES).issubset(fragments):
        raise SyncError("Owner-approved AI-use and Appendix E language fragments are required")
    for name in LANGUAGE_FILES:
        parts = fragments[name]
        if not isinstance(parts, list) or not parts or any(not isinstance(x, str) or not x.strip() for x in parts):
            raise SyncError(f"Missing factual language fragments for {name}")
        text = checked_path(root, name).read_text()
        for part in parts:
            if part not in text:
                raise SyncError(f"Approved factual disclosure fragment missing from {name}: {part!r}")
    if attestation is not None and release_sha is None:
        raise SyncError("An attestation must name an explicit --release-sha")
    if release_sha is not None:
        if not re.fullmatch(r"[0-9a-f]{40}", release_sha):
            raise SyncError("Final release SHA must be a full immutable commit hash")
        if git(root, "rev-parse", "HEAD") != release_sha:
            raise SyncError("Checkout HEAD is not the exact requested release SHA")
        if git(root, "status", "--porcelain", "--untracked-files=normal"):
            raise SyncError("Final release review-sync gate requires a clean exact-SHA scratch checkout")
        if attestation is None:
            raise SyncError("Final export requires an external release-owner attestation")
        if Path(attestation).resolve().is_relative_to(root):
            raise SyncError("Release-owner attestation must be external to the exact release tree")
        receipt = read_json(Path(attestation))
        if (receipt.get("release_sha") != release_sha or
                receipt.get("review_sync_sha256") != digest(manifest_path.read_bytes())):
            raise SyncError("Release-owner attestation is stale or bound to another SHA/manifest")
        if (receipt.get("authority") != "Le or designated release owner" or
                not isinstance(receipt.get("attested_by"), str) or not receipt["attested_by"].strip() or
                receipt.get("all_reviews_reconciled") is not True or
                receipt.get("scientific_acceptance_separate") is not True):
            raise SyncError("Owner must explicitly attest final review-inventory reconciliation and separate scientific acceptance")
        recorded = timestamp(receipt.get("recorded_utc"), "owner attestation")
        snapshot = timestamp(ledger.get("snapshot_utc"), "ledger snapshot")
        committed = timestamp(git(root, "show", "-s", "--format=%cI", release_sha), "release commit")
        decision_date = dt.datetime.fromisoformat(evidence["date"]).replace(tzinfo=dt.timezone.utc)
        if recorded < max(snapshot, committed, decision_date):
            raise SyncError("Owner attestation predates its ledger, release commit or decision evidence")
    if run_generator:
        process = subprocess.run([sys.executable, str(root / GENERATOR), "--check", "--ledger", ledger_name],
                                 cwd=root, capture_output=True, text=True)
        if process.returncode:
            raise SyncError("Appendix E generated data are stale or provenance is uncommitted: " +
                            (process.stderr + process.stdout).strip())
    return {"status": "PASS", "mode": "exact-release" if release_sha else "snapshot",
            "release_sha": release_sha, "review_sync_sha256": digest(manifest_path.read_bytes()),
            "rows": len(rows), "historical_rows_unchanged": 29, "recent_ids": recent,
            "named_summaries": len(summaries), "artifacts_verified": len(artifacts),
            "generator_check": run_generator, "whole_book_accepted": False,
            "claim_boundary": "Hash/record/text-fragment consistency only; final inventory completeness is the named owner's attestation, not machine discovery of private/future reviews."}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--ledger", default=LEDGER)
    parser.add_argument("--manifest", default=MANIFEST)
    parser.add_argument("--release-sha")
    parser.add_argument("--attestation", type=Path)
    args = parser.parse_args()
    try:
        result = validate(args.root, args.ledger, args.manifest, args.release_sha, args.attestation)
    except (SyncError, OSError, KeyError, TypeError, ValueError) as error:
        print(json.dumps({"status": "FAIL", "reason": str(error)}), file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
