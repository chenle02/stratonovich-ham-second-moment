#!/usr/bin/env python3
"""Pure held-v1 regression witnesses. Never saves a synthetic native report."""
from pathlib import Path
import copy
import hashlib
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
PROTOTYPE = ROOT.parent / "stratonovich-prebound-B21-prototype-20261104"
EXPECTED_VALIDATOR = "e772bfa744d763cbec51e530c2d9b11f7080e4312ee4a143c2296f8b7ea23683"
EXPECTED_MANIFEST = "efbc2d8c0bfddade4330ec35b2e6991617b2003cac0651cecbd5f4269b25be2a"
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha((PROTOTYPE / "validate_report.py").read_bytes()) == EXPECTED_VALIDATOR
assert sha((PROTOTYPE / "manifest.json").read_bytes()) == EXPECTED_MANIFEST
before = {p.name: sha(p.read_bytes()) for p in PROTOTYPE.iterdir() if p.is_file()}
sys.path.insert(0, str(PROTOTYPE))
from pure_controls import fixture, dep, M, SYN
from validate_report import Checker

report = fixture()
report["verdict"] = "PASS_WITH_NOTES"
for field in ["proofs", "formal_statements", "joins", "boundary_questions"]:
  for record in report[field].values():
    record["status"] = "CHECKED"
    if field in ["joins", "boundary_questions"]:
      record["actual_working"]["W"]["inputs"] = [dep("PROOF005")]
baseline = Checker(M, report).run()
assert not baseline["record_issues"]
assert baseline["scientific_acceptance"] is False

cases = []
for name, modify in [
  ("completed_public_record_false", lambda q: q.update(completed_public_record=False)),
  ("LIMITED_model_audit", lambda q: q.update(model_and_constant_audit=[{
    "status": "LIMITED", "actual_deduction": SYN, "inputs": [],
    "remaining_obligation": "The original model-to-constant implication is not worked."}])),
  ("NOT_READ_semantic_cycle_audit", lambda q: q.update(semantic_cycles=[{
    "status": "NOT_READ", "actual_deduction": "", "inputs": [],
    "remaining_obligation": "The dependency cycle check is not read."}])),
  ("empty_required_global_arrays", lambda q: None),
]:
  candidate = copy.deepcopy(report)
  modify(candidate)
  result = Checker(M, candidate).run()
  assert result["scientific_acceptance"] is False
  assert not result["record_issues"], (name, result["record_issues"])
  cases.append({"case": name, "actual_record_issues": result["record_issues"],
                "scientific_acceptance": False,
                "interpretation": "v1 completeness defect; no acceptance or native status inferred"})
after = {p.name: sha(p.read_bytes()) for p in PROTOTYPE.iterdir() if p.is_file()}
assert before == after
print(json.dumps({"scope": "ROOT PURE IN-MEMORY SYNTHETIC V1 COMPLETENESS WITNESSES",
                  "validator_sha256": EXPECTED_VALIDATOR,
                  "prototype_manifest_sha256": EXPECTED_MANIFEST,
                  "synthetic_report_saved_or_sent": False,
                  "all_held_files_unchanged": True,
                  "cases": cases,
                  "packet_or_provider_authorization": False}, indent=2) + "\n", end="")
