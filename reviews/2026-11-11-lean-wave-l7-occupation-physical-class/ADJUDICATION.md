# Adjudication: wave-L7 correspondence review, OccupationPhysicalClass

- **Object:** the wave-L7 ledger section(s) OccupationPhysicalClass, their index rows, claims.yaml summaries, coverage rows and cross-references at companion `a8fb495` (manuscript `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only, `CODEX_HOME` workaround; frozen packet with every library module (the item's own modules read completely), claims.yaml, coverage.yaml, docs/coverage-scope-tex.yaml and all TeX inputs at `975feb3`; contract-check, dry run and contract-check on the dispatched prompt clean.
- **Result:** valid, **PASS_WITH_NOTES**, confidence high, receipt accepted: True; 39 checks: 38 PASS, 1 PASS_WITH_NOTES; 1 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion branch `l7-repair`, merged at d2d29df) |
|---|---|---|---|---|
| W1 | minor | **ACCEPTED** | verified: the Scope section now names both StratonovichHAMAudit/ (step modules) and StratonovichHAMSecondMoment/ (whole-result modules) | `26e30aa` |

Every finding was verified against the Lean source and the TeX at `975feb3` before repair; none was declined. Lean files were changed in doc comments only (stripped sources identical to a8fb495, rebuilt; CheckFidelity 1430/1430, 0 problems after regeneration). Companion main after the merge: `d19c71a`. A confirmation review follows; the gate is Le's decision.
