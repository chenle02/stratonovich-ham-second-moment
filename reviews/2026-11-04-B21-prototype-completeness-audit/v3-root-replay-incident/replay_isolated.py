#!/usr/bin/env python3
"""Replay held v3 programs only in an owned disposable copy, never in custody."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
ROOT = Path(__file__).resolve().parents[3]
STATE = ROOT.parent
P = STATE / "stratonovich-prebound-B21-prototype-v3-20261104"
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha((P / "manifest.json").read_bytes()) == "063b261eb4f294d138fb6b434d5b85dd63bab48c14dc4cabbf494f24f817dfc0"
manifest = json.loads((P / "manifest.json").read_bytes())
for row in manifest["files"]:
  raw = (P / row["path"]).read_bytes()
  assert len(raw) == row["bytes"] and sha(raw) == row["sha256"]
before = {q.name: sha(q.read_bytes()) for q in P.iterdir() if q.is_file()}
programs = {
  "generate_source_map.py": ["source-map.json", "model-view.json", "source-reconstruction-receipt.json"],
  "build_protocol_schema.py": ["report-schema.json", "operative-grammar.md"],
  "pure_controls.py": ["control-results.json"],
  "minimum.py": ["minimum-result.json"],
}
results = []
with tempfile.TemporaryDirectory(prefix=".root-B21-v3-replay-", dir=STATE) as raw:
  copy = Path(raw)
  for file in P.iterdir():
    assert file.is_file() and not file.is_symlink()
    shutil.copyfile(file, copy / file.name)
  for program, outputs in programs.items():
    cp = subprocess.run(["python3", str(copy / program)], cwd=copy,
                        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    for output in outputs:
      assert (copy / output).read_bytes() == (P / output).read_bytes(), (program, output)
    results.append({"program": program, "exit_code": cp.returncode,
                    "stdout": cp.stdout.decode().strip(), "stderr_bytes": len(cp.stderr),
                    "exact_outputs": outputs})
assert before == {q.name: sha(q.read_bytes()) for q in P.iterdir() if q.is_file()}
print(json.dumps({"method": "fresh disposable sibling copy; all program outputs confined to copy; no incomplete writer monkeypatch",
                  "held_manifest_sha256": sha((P / "manifest.json").read_bytes()),
                  "programs": results, "all_held_files_unchanged": True,
                  "source_or_native_writes": False, "scientific_acceptance": False}, indent=2) + "\n", end="")
