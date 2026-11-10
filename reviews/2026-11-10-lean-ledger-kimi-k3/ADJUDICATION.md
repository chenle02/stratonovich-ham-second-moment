# Adjudication: Kimi-K3 correspondence review of the Lean statement ledger

- **Object:** `docs/statement-ledger.md` of `stratonovich-ham-second-moment-lean`
  at companion commit `4bdffba181a76bec2da9d79b2e0097afc721e385` (the
  post-DeepSeek ledger of `a78c5d0` plus the 669ccc9 re-anchor note; docs-only
  descendant of the verified `38d16163ab89`), against manuscript revision
  `669ccc9b07241ae94f365f4a2e17c04da66870ca` (41 TeX inputs).
- **Reviewer:** `subscription-review-cli run kimi --model kimi-code/k3`, native
  kimi 2.5.2, OAuth `managed:kimi-code`; receipt: `model_actual` k3,
  `effort_actual` max (configured, not overridden). Second model family after
  DeepSeek V4 Pro (2026-11-09 review). DeepSeek's report was NOT in the packet.
- **Read-only, tool-assisted:** reviewer profile tools `[Read, Grep, Glob]` in an
  isolated copy of the packet; no edit, network or delegation.
- **Kimi hold:** launched 07:11 before the 2026-11-09 hold was noticed; Le then
  lifted it for this run and, later, in general (Progress.md, f2425c8 and
  67b141a). Never stopped; no retry or resume.
- **Frozen packet:** `packet.tar.gz` (69 files: ledger, claims.yaml,
  coverage.yaml, 24 Lean sources at 4bdffba; 41 TeX at 669ccc9;
  `PROVENANCE.json`, each file written from its git blob and byte-compared).
  Receipt: `candidate_hashes_unchanged` true.
- **Contract:** `contract.txt`; prompt as dispatched `attempt-01/prompt.txt`.

## Transport, report validity and acceptance (kept separate)

| Layer | Result |
|---|---|
| Transport | completed normally, exit 0, 1,670 s |
| Report validity | **invalid-report** (driver exit 3; `scientific_verdict` null, `accepted` false) |
| Cause | the supervisor's contract asked for per-check verdicts `OK`/`WEAK`/`WRONG`/`ABSENT-CONFIRMED`/`LABEL-FOUND`; `subscription-review-report/1` accepts only PASS, PASS_WITH_NOTES, FAIL, INCONCLUSIVE, PARTIAL (`review_report_contract.py` `CHECK_VERDICTS`). The reviewer also put one prose line before the fenced JSON. `contract-check` was not run before dispatch; it should have been. |
| Recovery | `recover-report` refused (`body-invalid`, unsupported verdict value): `recover-report-refusal.json`. Fence extraction alone cannot fix the check vocabulary, and the report must not be hand-edited. |
| Acceptance | **NOT ACCEPTED** as a gate receipt. The receipt is retained unchanged. |

The report's scientific content is complete and readable
(`report-extracted-for-reading.json`, extracted by fence only, for reading):
verdict PASS_WITH_NOTES, confidence **high**, 88/88 checks (33 mappings
correct, 55 absences confirmed with search terms recorded per row), findings
0 fatal / 0 major / 4 minor, `required_repairs` empty, complete source
coverage claimed for every packet file. The adjudication below uses that
content on its merits; it does not convert the invalid receipt into an
accepted one.

## Findings

Adjudicator: Claude Opus 5.5 (#22). Each finding checked against the Lean
sources at 4bdffba and the TeX at 669ccc9.

| ID | Sev | Disposition | Evidence checked | Change (companion 01e2480) |
|---|---|---|---|---|
| K1 | MINOR | **ACCEPTED** | `DirectEvent.lean`: `physical_scale`, `noise_scale`, `vertex_scale` each take `(halpha : alpha < 3)`; ledger cells said only "For `T > 0`" | Cells now "For `T > 0` and `alpha < 3`" |
| K2 | MINOR | **ACCEPTED (wording)**; the substantive part is a packet-scope limit | The reviewer read cf979d6 as *later* than 669ccc9; it is earlier, so the preamble was ambiguous. The cross-revision claim itself was verified by the supervisor's script (40 cited statements/proofs, math identical up to whitespace/braces; companion 4bdffba commit) and is outside this packet by design | Preamble states cf979d6 is the earlier revision and what the check covered; stray "(for example …)" placement fixed |
| K3 | MINOR | **ACCEPTED (clarifying note)** | Paraphrases are correct but shortened, e.g. `ClockFilter.resolvent_partial_fraction`, `DimensionalMatrix.full_interaction` | Scope bullet: the column paraphrases; the Lean type is exact; `Audit/` prints it |
| K4 | MINOR | **ACCEPTED (wording)** | `RawValueCeiling.exact_gap : 2*30^60 < 39^39*21^21` ⇔ 2Δ > log 2 at q=39, a=9 (2Δ ≈ 2.742 > 0.693) | Module text states the inequality and its meaning |

No finding rejected. No Lean or manuscript defect. No mapping or count change:
33 labelled, 55 unlabelled; coverage.yaml unchanged. Companion `01e2480` is a
docs-only descendant of `38d16163ab89` (lean-pkg gate check confirms).

## Agreement with the first review

DeepSeek V4 Pro (2026-11-09, MEDIUM) and Kimi-K3 (this run, high) found no
fidelity error and no wrong mapping in the post-repair rows. Kimi confirmed
all 55 absences by recorded search, closing DeepSeek's stated limitation.

## Status

- Accepted repairs applied (01e2480). Edited rows not re-reviewed (wording only).
- **Correspondence gate: NOT closed by receipt.** The only high-confidence
  report is in an invalid-report attempt caused by the supervisor's contract.
  To obtain an accepted receipt: a new immutable Kimi-K3 attempt on a fresh
  packet at 01e2480 with a schema-conforming contract (check verdicts
  PASS/FAIL/PARTIAL; row status in `reason`), run through `contract-check`
  first. Not a confidence-only retry: the contract and candidate change.
  Needs Le's go-ahead for the Kimi quota.
