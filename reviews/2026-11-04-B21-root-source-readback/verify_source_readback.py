#!/usr/bin/env python3
"""Recompute B21 statement/proof identities from the unchanged sealed source."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEAL = "af97ae4db921a660b0a4ed1ffbe9b6f53a487e2b"
INDEX = "reviews/2026-11-02-main-deepseek/proof-index-v7-neutral.json"
IDS = set(range(24, 36)) | set(range(52, 61))
READ_RANGES = [(2985, 4605), (6850, 7785)]
sha = lambda b: hashlib.sha256(b).hexdigest()
index = json.loads((ROOT / INDEX).read_bytes())
rows = []
for proof in index["proofs"]:
  if int(proof["id"][5:]) not in IDS:
    continue
  rel = proof["path"]
  current = (ROOT / rel).read_bytes()
  sealed = subprocess.check_output(["git", "show", SEAL + ":" + rel], cwd=ROOT)
  assert current == sealed
  assert sha(current) == proof["source_sha256"]
  lines = current.splitlines(keepends=True)
  excerpt = b"".join(lines[proof["line"] - 1:proof["end_line"]])
  start = excerpt.index(b"\\begin{proof}") + len(b"\\begin{proof}")
  end = excerpt.rindex(b"\\end{proof}")
  proof_sha = sha(excerpt[start:end])
  assert proof_sha == proof["raw_body_sha256"]
  statement = proof["statement"]
  excerpt = b"".join(lines[statement["start_line"] - 1:statement["end_line"]])
  opening = ("\\begin{" + statement["environment"] + "}").encode()
  closing = ("\\end{" + statement["environment"] + "}").encode()
  start = excerpt.index(opening) + len(opening)
  end = excerpt.rindex(closing)
  statement_sha = sha(excerpt[start:end])
  assert statement_sha == statement["raw_statement_body_sha256"]
  assert any(a <= statement["start_line"] <= proof["end_line"] <= b
             for a, b in READ_RANGES)
  rows.append({"id": proof["id"], "claim_label": proof["claim_label"],
               "path": rel, "statement_lines": [statement["start_line"], statement["end_line"]],
               "proof_lines": [proof["line"], proof["end_line"]],
               "proof_body_sha256": proof_sha,
               "statement_body_sha256": statement_sha})
assert len(rows) == 21
result = {"schema": "root-b21-source-readback-v1", "sealed_science_commit": SEAL,
          "neutral_index": INDEX, "neutral_index_sha256": sha((ROOT / INDEX).read_bytes()),
          "root_personal_read_ranges": READ_RANGES,
          "machine_check_scope": "21 exact statements and proof bodies, current bytes equal sealed bytes",
          "not_established_by_machine_check": ["mathematical truth", "independent review", "whole-project completion"],
          "rows": rows}
print(json.dumps(result, indent=2) + "\n", end="")
