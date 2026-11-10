# Adjudication: schema-conforming Kimi-K3 review of the Lean statement ledger (v2)

- **Object:** `docs/statement-ledger.md`, companion commit
  `01e2480bd207a64d4492617eba055d828ef4cd03` (after the v1 Kimi fixes), against
  manuscript `669ccc9b07241ae94f365f4a2e17c04da66870ca` (41 TeX inputs).
- **Reviewer:** `subscription-review-cli run kimi --model kimi-code/k3`; receipt
  `model_actual` k3, `effort_actual` max. Tools `[Read, Grep, Glob]`, isolated
  packet copy, read-only. No earlier report in the packet. Kimi hold lifted by
  Le (Progress.md, 2026-11-10).
- **Frozen packet:** `packet.tar.gz` (68 files + `PROVENANCE.json`, each written
  from its git blob and byte-compared). `candidate_hashes_unchanged` true.
- **Preflight (new for v2):** `report.schema.json` mirrors
  `review_report_contract.py`; `contract-check` observable on the contract and
  on the exact dispatched `attempt-01/prompt.txt` (`contract-check.json`); dry
  run clean (`dryrun/`); a sample report built from the contract passed the
  lab validator before launch.

## Transport, validity, acceptance (kept separate)

| Layer | Result |
|---|---|
| Transport | completed, exit 0, 1,786 s |
| Report validity | **invalid-report** (driver exit 3, `scientific_verdict` null, `accepted` false). Diagnostic: JSON fails at char 0 |
| Cause | Kimi wrote one 329-byte prose sentence ("All evidence is gathered. … Here is the report.") before the JSON object, despite the contract's explicit "Return ONLY the JSON object". The v1 attempt did the same. The check-verdict defect of v1 is fixed: every check uses PASS/PASS_WITH_NOTES. |
| Recovery | `recover-report` refused (`not-recoverable`): it supports only fence extraction or one missing closer, not a prose prefix (`recover-report-refusal.json`). |
| Acceptance | **NOT ACCEPTED** as a receipt. Receipt retained unchanged. |
| Body (reading only) | Stripping only the prefix, the lab validator and passing-report gate accept the body: PASS_WITH_NOTES, high, 88 checks (86 PASS, 2 PASS_WITH_NOTES), 0 fatal, 0 major, 2 minor, no required repair (`body-reading-check.json`). This is a reading aid, not an acceptance record. |

## Findings (adjudicator: Claude Opus 5.5, #22)

| ID | Sev | Disposition | Evidence checked | Change (companion 5e0d122) |
|---|---|---|---|---|
| K1 | MINOR | **ACCEPTED** | `ClockFilter.lean:29` `(hθ : 0 < θ)`; row omitted θ>0 and the factor 2θ/(2θ+ℓ) | Row states θ>0 and the filtered integrand |
| K2 | MINOR | **ACCEPTED** | `PhaseResponse.lean:25-26` checks exactly `2*(1/2)+α+a<3 ∧ α+a-3<-1` | Row names the two margins |
| LF1/LF2 (checks, PASS with reason LABEL-FOUND) | — | **ACCEPTED as a note; rows keep no label** | `forward` = `(C,G;-LG,C)` with q=√L, main TeX 669ccc9 l.5174 in the proof of `L:complex-phase` (l.5019), and balanced `W_t` in `L:symplectic-free` (`integrated_symplectic_phase.tex` l.31, 72–78). `backward` is the inverse (time-reversed) matrix, not displayed; the reviewer's "same matrix" holds for `forward` only. The checked product `full_interaction` appears nowhere. Definitions make no claim; the manuscript owner ruled against labels for coverage. The contract defined LABEL-FOUND as FAIL; the reviewer gave PASS with reasons, which this adjudication accepts on the merits and records as a deviation from the contract | Module paragraph locates `forward`, describes `backward`, keeps no label |

No finding rejected; no Lean or manuscript defect; counts unchanged (33 labelled,
55 unlabelled; coverage.yaml unchanged). Companion `5e0d122` is a docs-only
descendant of `38d16163ab89` (gate check confirms).

## Status

- Three independent reports now agree that the ledger has no fidelity error,
  no wrong mapping and no required repair: DeepSeek V4 Pro (MEDIUM, valid),
  Kimi-K3 v1 (high, invalid-report: check vocabulary), Kimi-K3 v2 (high,
  invalid-report: prose prefix). Their minor findings are all applied.
- **Correspondence gate: NOT closed by an accepted receipt.** Both high
  reports fail format validation for reasons outside their content. Options
  for Le: (a) a lab tool change so `recover-report` can strip a leading prose
  line, a byte-reversible operation like fence extraction, then recover v2
  unchanged; (b) a Codex or Claude route, which may follow JSON-only output; (c)
  a human statement read. A third Kimi attempt is not recommended: K3 wrote a
  prefix in both runs despite explicit instructions.
