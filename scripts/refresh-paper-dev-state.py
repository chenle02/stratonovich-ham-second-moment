#!/usr/bin/env python3
"""Refresh ignored dashboard state from Progress.md without review promotion."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess


def section(text, name):
    match = re.search(r"^## " + re.escape(name) + r"\s*$", text, re.M)
    if match is None:
        raise ValueError("Missing authoritative Progress.md section: " + name)
    rest = text[match.end():]
    end = re.search(r"^## ", rest, re.M)
    return rest[:end.start() if end else len(rest)].strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--authority", type=Path,
                        help="Research checkout; use with a separate launcher --repo")
    args = parser.parse_args()
    repo = args.repo.resolve()
    authority = (args.authority or repo).resolve()
    text = (authority / "Progress.md").read_text()
    goal = " ".join(section(text, "Goal").split())
    status = section(text, "Status")
    round_text = section(text, "Round")
    if not round_text.isdecimal() or int(round_text) < 1:
        raise ValueError("Round must be the recorded positive integer")
    if status not in {"IN_PROGRESS", "NEEDS_FEEDBACK", "PAUSED", "DONE"}:
        raise ValueError("Unrecognized authoritative status")
    if not goal:
        raise ValueError("Empty authoritative goal")
    subaim = " ".join(section(text, "Current Subaim").split())
    subaim = re.sub(r"^- \[[ xX]\] ", "", subaim)
    launcher = repo != authority
    if launcher:
        subaim = ("LAUNCHER: local review list is an older snapshot. Research: "
                  + os.path.relpath(authority, repo) + ". " + subaim)
    helper = shutil.which("paper-dev-state.py")
    if helper is None:
        raise RuntimeError("Canonical paper-dev-state.py is required on PATH")
    state = repo / ".paper-dev-state.json"
    base = [helper, "--file", str(state)]
    if not state.exists():
        subprocess.run(base + ["init", "--round", round_text,
                              "--goal", goal, "--status", status], check=True)
    values = {
        "current_round": int(round_text), "status": status, "goal": goal,
        "current_subaim": subaim,
        "wave": "whole-goal verification; round accounting under audit",
        "authority_progress": os.path.relpath(authority / "Progress.md", repo),
        "launcher_snapshot": launcher, "dashboard_metadata_only": True,
    }
    # The canonical helper locks and merges named keys. It preserves unrelated
    # session/role/review keys; this adapter neither invents nor upgrades them.
    subprocess.run(base + ["set", "--json"] +
                   [key + "=" + json.dumps(value) for key, value in values.items()],
                   check=True)
    print("Dashboard metadata refreshed; no review or round-close gate changed.")


if __name__ == "__main__":
    main()
