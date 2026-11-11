# Adjudication: wave-L5 correspondence review, VariationalMean (whole result)

- **Object:** the ledger section "VariationalMean (whole result)", its index rows, its
  coverage rows and cross-references at companion `210cc3f` (manuscript
  `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only,
  `CODEX_HOME` workaround; frozen packet with every library module (the
  section's own modules read completely), claims.yaml, coverage.yaml (and
  docs/coverage-scope-tex.yaml where the contract names it), all 78 TeX
  inputs at `975feb3`; contract-check, dry run and contract-check on the
  dispatched prompt clean.
- **Result:** valid, **FAIL**, confidence high; 46 checks: 45 PASS, 1 FAIL; 1 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| W1 | major | **ACCEPTED** | index did not reproduce the table labels (heatSpec, heat_identity under E:variational-heat-envelope; mean_le, mean_lip under E:variational-global-mean; gauss_conv) and lacked the 23 auxiliaries | `f2f233f` |

Every finding was verified against the Lean source and the TeX at `975feb3`
before repair (companion branch `l5-repair`, merged into main). A narrow
confirmation review of the repairs follows; the gate is Le's decision.
