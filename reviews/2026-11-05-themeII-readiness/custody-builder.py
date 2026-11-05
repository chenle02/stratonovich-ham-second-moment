#!/usr/bin/env python3
"""Freeze already held author preparation; no model/source operation."""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import shutil
import tarfile

DIRECTORIES = [
  "whole-current-scope-capacity-plan-20261105",
  "whole-B-support-counterpart-reconciliation-20261105",
  "whole-calibration-primary-counterpart-reconciliation-20261105",
  "whole-B-core-selected-counterpart-reconciliation-20261105",
  "whole-B-static-selected-counterpart-reconciliation-20261105",
  "whole-A-C-E-selected-counterpart-reconciliation-20261105",
  "whole-H-historical-counterpart-reconciliation-20261105",
  "themeII-current-join-readiness-plan-20261105",
  "themeII-4-root-finiteness-application-20261105",
  "themeII-4-root-finiteness-independent-author-check-20261105",
  "themeII-root-preparation-selection-20261105",
]


def sha(raw):
  return hashlib.sha256(raw).hexdigest()


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--state-root", type=Path, required=True)
  args = parser.parse_args()
  destination = Path(__file__).resolve().parent
  archive = destination / "held-preparation.tar.gz"
  if archive.exists():
    raise SystemExit("Refusing to overwrite an existing frozen archive")
  payloads = {}
  trees = []
  for name in DIRECTORIES:
    root = args.state_root / name
    manifest_raw = (root / "manifest.json").read_bytes()
    manifest = json.loads(manifest_raw)
    held_raw = (root / "HELD.json").read_bytes()
    held = json.loads(held_raw)
    assert sha(manifest_raw) == held["manifest_sha256"], name
    members = manifest.get("members", manifest.get("files"))
    assert isinstance(members, list), name
    for member in members:
      member_name = member.get("path", member.get("file"))
      relative = Path(member_name)
      assert not relative.is_absolute() and ".." not in relative.parts
      source = root / relative
      assert source.is_file() and not source.is_symlink(), source
      raw = source.read_bytes()
      assert len(raw) == member["bytes"] and sha(raw) == member["sha256"], source
      target = str(Path(name) / relative)
      assert target not in payloads
      payloads[target] = raw
    payloads[name + "/manifest.json"] = manifest_raw
    payloads[name + "/HELD.json"] = held_raw
    trees.append({"directory": name, "manifest_sha256": sha(manifest_raw),
                  "verified_manifest_members": len(members)})
  rows = []
  with archive.open("xb") as output:
    with gzip.GzipFile(fileobj=output, mode="wb", filename="", mtime=0) as compressed:
      with tarfile.open(fileobj=compressed, mode="w|") as tar:
        for name, raw in sorted(payloads.items()):
          info = tarfile.TarInfo(name)
          info.size = len(raw)
          info.mode = 0o644
          info.mtime = 0
          tar.addfile(info, io.BytesIO(raw))
          rows.append({"path": name, "bytes": len(raw), "sha256": sha(raw)})
  with tarfile.open(archive, "r:gz") as tar:
    actual = tar.getmembers()
    assert len(actual) == len(rows)
    for member, expected in zip(actual, rows):
      assert member.isfile() and member.name == expected["path"]
      raw = tar.extractfile(member).read()
      assert len(raw) == expected["bytes"] and sha(raw) == expected["sha256"]
  copies = {
    "Root-selection.md": ("themeII-root-preparation-selection-20261105", "Root-selection.md"),
    "finiteness-application.md": ("themeII-4-root-finiteness-application-20261105", "worked-application.md"),
    "finiteness-author-check.md": ("themeII-4-root-finiteness-independent-author-check-20261105", "report.md"),
  }
  for target, (directory, source_name) in copies.items():
    source = args.state_root / directory / source_name
    shutil.copyfile(source, destination / target)
    assert (destination / target).read_bytes() == payloads[directory + "/" + source_name]
  inventory = {"kind": "HELD_AUTHOR_PREPARATION_CUSTODY_NOT_MODEL_INPUT_OR_REVIEW_ACCEPTANCE",
               "archive": archive.name, "archive_bytes": archive.stat().st_size,
               "archive_sha256": sha(archive.read_bytes()), "members": rows,
               "member_count": len(rows), "uncompressed_bytes": sum(r["bytes"] for r in rows),
               "source_trees": trees, "all_members_read_back": True,
               "scientific_omission_or_model_dispatch_or_accepted_grade_change": False}
  (destination / "held-preparation.inventory.json").write_text(json.dumps(inventory, indent=2) + "\n")
  print(json.dumps({k: inventory[k] for k in ("archive_bytes", "archive_sha256", "member_count", "uncompressed_bytes")}))


if __name__ == "__main__":
  main()
