"""Check calibrated image cohort before a NEW review; never accepts science."""
from pathlib import Path
import argparse
import hashlib
import json

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--required", type=Path, required=True)
p.add_argument("--receipt", type=Path, required=True)
p.add_argument("--ledger", type=Path, required=True)
p.add_argument("--out", type=Path)
a = p.parse_args()
x = json.loads(a.receipt.read_text())
l = json.loads(a.ledger.read_text())
assert x["read_ledger_sha256"] == hashlib.sha256(a.ledger.read_bytes()).hexdigest()
assert x["coverage_verified"] is True and l["coverage_verified"] is True
assert x["transport_ok"] is True and x["actual_route_verified"] is True
assert x["candidate_hashes_unchanged"] is True
assert x["model_actual"] == "claude-opus-5-5"
assert x["auth"]["apiProvider"] == "firstParty"
assert l["events_sha256"] == x["transport_events_sha256"]
assert l["events_hash_bound_to_receipt"] is True and not l["diagnostics"]
expected = {
    r["path"]: (r["sha256"], r["media_type"])
    for r in json.loads(a.required.read_text()) if r.get("kind") == "image"
}
observed = {
    r["path"]: (r["sha256"], r["media_type"])
    for r in l["required_images"] if r["status"] == "delivered"
}
assert expected and expected == observed, "Final image cohort is not exactly the calibrated cohort"
for name, (digest, _) in expected.items():
    assert x["input_hashes"][name] == digest
result = {
    "status": "CARRIER-READY",
    "images": len(expected),
    "calibration_wrapper_status": x["status"],
    "calibration_wrapper_accepted": x["accepted"],
    "does_not_prove": "Scientific acceptance,report-format validity,proof or future delivery. A NEW full review with its own complete ledger and unchanged HIGH threshold is still mandatory.",
}
if a.out:
    a.out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
