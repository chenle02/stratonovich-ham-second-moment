#!/usr/bin/env python3
"""Preserve held-v2 source-association and honest-unread regression witnesses."""
from pathlib import Path
import hashlib
import json
import sys
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
P = ROOT.parent / "stratonovich-prebound-B21-prototype-v2-20261104"
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha((P / "manifest.json").read_bytes()) == "f245719df1a127bb5e537a9dea1ee51951916dd1ca789cf0a5e8624d0e59f783"
manifest = json.loads((P / "manifest.json").read_bytes())
for row in manifest["files"]:
  b = (P / row["path"]).read_bytes()
  assert len(b) == row["bytes"] and sha(b) == row["sha256"]
before = {q.name: sha(q.read_bytes()) for q in P.iterdir() if q.is_file()}
sys.path.insert(0, str(P))
from pure_controls import fixture, M
from validate_report import Checker
report = fixture()
assert not Checker(M, report).run()["record_issues"]
report["proofs"]["PROOF024"].update(
  status="NOT_READ", actual_hypotheses="", actual_consumer_check="", actual_working={},
  remaining_obligation="PROOF024 has not been read; its proof and source application remain open.")
formal = report["formal_statements"]["S016"]
formal.update(status="NOT_READ", actual_hypotheses="", actual_consumer_check="",
              actual_clause_and_scope_check="",
              remaining_obligation="The attached static coefficient statement and full parent proof remain unread.")
formal.pop("certificate")
result = Checker(M, report).run()
assert result["record_issues"] == ["native proof hypothesis/consumer check",
                                   "native formal application/scope check",
                                   "native attached-own certificate to actual parent"]
obligations = json.loads((P / "global-obligations.json").read_bytes())
wrong = {k: obligations["finite_controls"][k]["obligation"] for k in ["F12_WHITE_27", "F13_WHITE_45"]}
assert all("210-213" in text for text in wrong.values())
index = json.loads((ROOT / "reviews/2026-11-02-main-deepseek/proof-index-v7-neutral.json").read_bytes())
ids = {"PROOF011", "PROOF012", "PROOF210", "PROOF211", "PROOF212", "PROOF213"}
actual = [{k: row[k] for k in ["id", "claim_label", "path", "line", "end_line", "raw_body_sha256"]}
          for row in index["proofs"] if row["id"] in ids]
after = {q.name: sha(q.read_bytes()) for q in P.iterdir() if q.is_file()}
assert before == after
print(json.dumps({"role": "ROOT V2 REGRESSION WITNESSES, NOT SCIENTIFIC REVIEW",
                  "held_v2_manifest_sha256": sha((P / "manifest.json").read_bytes()),
                  "unconsumed_unread_case": {"verdict": report["verdict"], "actual_record_issues": result["record_issues"],
                                             "scientific_acceptance": False},
                  "wrong_operational_captions": wrong,
                  "actual_source_associations": actual,
                  "synthetic_report_saved_or_sent": False,
                  "all_held_files_unchanged": True}, indent=2) + "\n", end="")
