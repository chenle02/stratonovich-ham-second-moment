"""Pre-dispatch byte/commit guard only; does not certify scientific completeness."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def main():
    if sys.flags.optimize:
        raise ValueError("Run the guard without Python optimization")
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ["packet", "manifest", "required", "contract"]:
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()

    def check_blob(path):
        assert not path.is_symlink(), f"symlink: {path}"
        rel = path.resolve().relative_to(ROOT).as_posix()
        got = subprocess.run(["git", "show", commit + ":" + rel], cwd=ROOT,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        assert got.returncode == 0, f"not committed at {commit}: {rel}"
        assert got.stdout == path.read_bytes(), f"working/committed bytes differ: {rel}"

    for path in [args.manifest, args.required, args.contract]:
        check_blob(path)
    assert not args.packet.is_symlink()
    mapping = json.loads(args.manifest.read_text())
    actual = set()
    for path in args.packet.rglob("*"):
        assert not path.is_symlink(), f"packet symlink: {path}"
        if path.is_file():
            actual.add(path.relative_to(args.packet).as_posix())
    assert set(mapping) == actual, "packet/manifest membership mismatch"
    for name, digest in mapping.items():
        assert not PurePosixPath(name).is_absolute() and ".." not in PurePosixPath(name).parts
        assert re.fullmatch("[0-9a-f]{64}", digest), f"bad digest: {name}"
        path = args.packet / name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"manifest drift: {name}"
        check_blob(path)
    required = json.loads(args.required.read_text())
    assert required, "empty reading plan"
    for row in required:
        assert row["path"] in mapping, f"required member absent: {row['path']}"
        if row.get("kind") == "image":
            assert row["sha256"] == mapping[row["path"]], "required image hash differs"
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == commit
    result = {"status": "PASS", "commit": commit, "packet_members": len(mapping),
              "all_working_manifest_committed_blobs_equal": True,
              "required_paths_present": True,
              "does_not_prove": "Semantic dependency completeness, native delivery, mathematics or acceptance"}
    if args.out:
        args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print("REFUSED: " + str(exc), file=sys.stderr)
        sys.exit(1)
