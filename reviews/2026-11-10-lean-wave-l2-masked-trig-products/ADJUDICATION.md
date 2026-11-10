# Adjudication: correspondence review of the MaskedTrigProducts rows (wave L2)

- **Object:** the "MaskedTrigProducts (whole result)" section (30 rows), its
  index rows, the coverage row for `L:masked-trig-products`, the
  cross-references, the totals line and the Scope prose. Reviewer: Codex GPT-6.1-Sol, effort high, read-only sandbox, `CODEX_HOME`
  workaround; frozen packet (one Lean module, ledger, claims, coverage, all
  manuscript inputs at `ba01d98`), contract-check (schema) and dry run clean,
  contract-check on the dispatched prompt clean. Object: companion `c4e0620`.
- **Required reading:** Lean module and `integrated_covariance_foundation.tex`
  (1-428) complete; ledger, claims and coverage complete for the required
  parts.
- **Result:** valid, **PASS_WITH_NOTES**, confidence high, accepted; 36
  checks: 33 PASS, 3 PASS_WITH_NOTES; 0 fatal, 0 major, 1 minor. The
  abstraction of the completion (`E`, `V`, linear `emb`) was judged
  sound, and `hmod` is exactly `L:masked-temporal-modulation`.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| W1 | minor | **ACCEPTED** | `trig_product_bound` and `trig_product_bound_half` (Lean l.284, 315) take a witness `hp` of membership, which `prodFn_mem` derives from `hmem`; the paragraph said membership is never assumed | paragraph, both rows and both claims summaries mention the redundant witness (`17f0490`) |
