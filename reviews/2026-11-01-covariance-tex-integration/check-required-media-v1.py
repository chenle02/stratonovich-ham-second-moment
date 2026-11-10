#!/usr/bin/env python3
"""Check required PNG typing before native paper review; no reviewer dispatch."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def check(spec_path, workspace):
    spec = json.loads(Path(spec_path).read_text())
    root = Path(workspace).resolve()
    sys.path.insert(0, str(Path.home() / ".claude/bin"))
    from review_read_ledger import Workspace, load_full_spec
    texts, images = load_full_spec(spec, Workspace(root, str(root), str(root)))
    typed = {path for path, _, _ in images}
    pngs = set()
    for item in spec:
        relative = item["path"]
        content = (root / relative).read_bytes()
        if content.startswith(b"\x89PNG\r\n\x1a\n"):
            pngs.add(relative)
            if relative not in typed:
                raise ValueError("PNG declared as text: " + relative)
    if pngs != typed:
        raise ValueError("Image declarations do not exactly match PNG sources")
    return {"status": "PASS", "text_sources": len(texts),
            "image_sources": len(images),
            "spec_sha256": hashlib.sha256(Path(spec_path).read_bytes()).hexdigest(),
            "scope": "required-media classification and canonical spec validation only"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("required")
    parser.add_argument("workspace")
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.required, args.workspace), indent=2))
    except Exception as exc:
        print(json.dumps({"status": "REFUSED", "reason": str(exc)}))
        sys.exit(1)
