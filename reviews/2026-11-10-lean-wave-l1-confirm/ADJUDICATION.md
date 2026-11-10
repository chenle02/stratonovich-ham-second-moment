# Adjudication: confirmation review of the repaired wave L1 rows

- **Object:** the five whole-result ledger sections (21 rows incl. the
  exact-hypothesis wrappers), paragraphs, index, totals (109/61/48), scope prose
  and coverage rows at companion `f510681`, manuscript `ba01d98`. Codex
  GPT-6.1-Sol, effort high, read-only, `CODEX_HOME` workaround; contract-check
  and dry run clean; required reading reported complete.
- **Result:** valid, **FAIL**, confidence high; 30 checks: 29 PASS, 1 FAIL
  (COVERAGE-ROWS); 2 fatal findings, no other issue. All 21 rows, paragraphs,
  index, totals and scope prose confirmed.

| ID | Disposition | Verified | Repair |
|---|---|---|---|
| W1 (E:driver-parameters) | **ACCEPTED** | coverage class same-assumptions while the cited theorem assumes only the numerical part of H:homog; a `note` does not cure a false class | Le chose (2026-11-10) to model H:homog in Lean: `HomogHypothesis.HomogCovariance` (companion `f81115b`), wrapper `parameters_nonempty_paper`; coverage cites it (`b876362`) |
| W2 (E:kappa) | **ACCEPTED** | same, for `kappa_mem_Ioo` | wrapper `kappa_mem_Ioo_paper`; coverage cites it (`b876362`) |

lean-pkg receipt and gate verified-private at `b876362`; claims synced at
`d7abbd4` (117 claims). The H:homog model itself is under a separate
correspondence review (launched the same day). Tooling gap (no coverage class
for "weaker hypotheses") reported to lean-ops; triaged as a schema proposal.
