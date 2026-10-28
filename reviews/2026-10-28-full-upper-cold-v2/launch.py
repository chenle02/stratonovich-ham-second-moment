"""Launch one source-bound, isolated, prior-blind native cold-reader attempt."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
REVIEW = Path(__file__).resolve().parent
PACKET = REVIEW / "packet-v1"
NATIVE = REVIEW / "native-v1"
if NATIVE.exists():
    raise SystemExit("Refusing to overwrite or restart an existing attempt")

subprocess.run([
    sys.executable,
    str(ROOT / "reviews/2026-10-28-product-endpoints/check-frozen-packet.py"),
    "--packet", str(PACKET),
    "--manifest", str(REVIEW / "manifest-v1.json"),
    "--required", str(REVIEW / "required-inputs-v1.json"),
    "--contract", str(REVIEW / "prompt-v1.txt"),
    "--out", str(REVIEW / "committed-preflight-v1.json"),
], cwd=ROOT, check=True)
revision = subprocess.check_output(
    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
).strip()
binding = json.loads((REVIEW / "change-binding.json").read_text())
for name, key in [
    ("notes/notes_stratonovich_ham_second_moment.tex", "canonical_tex_sha256"),
    ("notes/notes_stratonovich_ham_second_moment.pdf", "canonical_pdf_sha256"),
]:
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == binding[key]

workspace = Path(tempfile.mkdtemp(
    prefix="stratonovich-whole-cold-", dir=Path.home() / ".local/state/tmp"
))
subprocess.run(["git", "init", "--quiet", str(workspace)], check=True)
manifest = json.loads((REVIEW / "manifest-v1.json").read_text())
for name, digest in manifest.items():
    shutil.copyfile(PACKET / name, workspace / name)
    assert hashlib.sha256((workspace / name).read_bytes()).hexdigest() == digest

overrides = {
    "OPENCODE_CONFIG": str(REVIEW / "launch-config.json"),
    "OPENCODE_DISABLE_CLAUDE_CODE": "true",
    "OPENCODE_DISABLE_CLAUDE_CODE_PROMPT": "true",
    "OPENCODE_DISABLE_CLAUDE_CODE_SKILLS": "true",
    "OPENCODE_DISABLE_EXTERNAL_SKILLS": "true",
    "OPENCODE_DISABLE_PROJECT_CONFIG": "true",
    "OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX": "131072",
}
env = os.environ.copy()
env.update(overrides)
argv = [
    "opencode", "run", "--pure", "--format", "json", "--agent", "cold-referee",
    "--dir", str(workspace), "-m", "deepseek/deepseek-v4-pro",
]
NATIVE.mkdir()
started = time.time()
record = {
    "source_revision": revision,
    "category": "paper-review-deepseek",
    "model_requested": "deepseek/deepseek-v4-pro",
    "argv": argv,
    "cwd": str(workspace),
    "environment_overrides": overrides,
    "input_hashes": manifest,
    "prompt_sha256": hashlib.sha256((REVIEW / "prompt-v1.txt").read_bytes()).hexdigest(),
    "started_unix": started,
    "timeout_seconds": 2400,
    "fresh_session": True,
    "automatic_retry": False,
}
with (NATIVE / "events.jsonl").open("w") as output, (NATIVE / "stderr.txt").open("w") as error:
    process = subprocess.Popen(
        argv, cwd=workspace, env=env, stdin=subprocess.PIPE,
        stdout=output, stderr=error, text=True,
    )
    record["pid"] = process.pid
    (NATIVE / "execution.json").write_text(json.dumps(record, indent=2) + "\n")
    try:
        process.communicate((REVIEW / "prompt-v1.txt").read_text(), timeout=2400)
        record["exit_code"] = process.returncode
        record["status"] = "terminal"
    except subprocess.TimeoutExpired:
        process.kill()
        process.communicate()
        record["exit_code"] = process.returncode
        record["status"] = "terminal-timeout"
record["elapsed_seconds"] = time.time() - started
record["ended_unix"] = time.time()
record["head_held"] = subprocess.check_output(
    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
).strip() == revision
record["workspace_bytes_unchanged"] = all(
    hashlib.sha256((workspace / name).read_bytes()).hexdigest() == digest
    for name, digest in manifest.items()
)
(NATIVE / "execution.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({key: record[key] for key in [
    "status", "exit_code", "elapsed_seconds", "head_held", "workspace_bytes_unchanged"
]}))
