# Adjudication: wave-L7 correspondence review, InventoryProduct

- **Object:** the wave-L7 ledger section(s) InventoryProduct, their index rows, claims.yaml summaries, coverage rows and cross-references at companion `a8fb495` (manuscript `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only, `CODEX_HOME` workaround; frozen packet with every library module (the item's own modules read completely), claims.yaml, coverage.yaml, docs/coverage-scope-tex.yaml and all TeX inputs at `975feb3`; contract-check, dry run and contract-check on the dispatched prompt clean.
- **Result:** valid, **PASS_WITH_NOTES**, confidence high, receipt accepted: True; 35 checks: 32 PASS, 3 PASS_WITH_NOTES; 2 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion branch `l7-repair`, merged at d2d29df) |
|---|---|---|---|---|
| W1 | minor | **ACCEPTED** | verified against InventoryProduct.lean:275-276, 597-598 and the TeX at 975feb3 lines 2933-2949: the TeX treats p through the integral of log(1+A x^(-p)) and uses the power sum only for beta/nu; the ledger row for sum_rpow_pos_le now says so | `26e30aa` |
| W2 | minor | **ACCEPTED** | verified: factorCoeff_nonneg takes k, i, l without hypotheses; "every theorem has k >= 1" now reads "every evaluation and coefficient bound", zero indices noted | `319cc2e, 26e30aa` |

Every finding was verified against the Lean source and the TeX at `975feb3` before repair; none was declined. Lean files were changed in doc comments only (stripped sources identical to a8fb495, rebuilt; CheckFidelity 1430/1430, 0 problems after regeneration). Companion main after the merge: `d19c71a`. A confirmation review follows; the gate is Le's decision.
