# Adjudication: wave-L7 correspondence review, UniformSeriesTail

- **Object:** the wave-L7 ledger section(s) UniformSeriesTail, their index rows, claims.yaml summaries, coverage rows and cross-references at companion `a8fb495` (manuscript `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only, `CODEX_HOME` workaround; frozen packet with every library module (the item's own modules read completely), claims.yaml, coverage.yaml, docs/coverage-scope-tex.yaml and all TeX inputs at `975feb3`; contract-check, dry run and contract-check on the dispatched prompt clean.
- **Result:** valid, **FAIL**, confidence high, receipt accepted: False; 19 checks: 1 FAIL, 17 PASS, 1 PASS_WITH_NOTES; 2 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion branch `l7-repair`, merged at d2d29df) |
|---|---|---|---|---|
| W1 | fatal | **ACCEPTED** | verified: WeakSobolev.rayleighRate := Real.sqrt (sSup ...); TeX integrated_spatial_occupation.tex 43-45 and integrated_unmasked_variational.tex 103-107 define lambda^2 as the supremum. My plain-English rewording at companion d3d7f4c (for the book Appendix F) wrongly said lambda IS the supremum, in the L:spatial-static-controls and P:spatial-smooth-ratio scope sentences. Both now say lambda is the square root of the supremum; a repo-wide sweep made three further ambiguous phrasings precise. The same two-row fix was put on top of d3d7f4c as 3c158f5 (branch appendix-f-lambda) for the book, which #24 re-pinned (book c6dded6); nothing was public | `d0d0335, 1e481f7, 3c158f5` |
| W2 | minor | **ACCEPTED** | verified: "zero when m+n is odd" is at TeX line 3565; citation corrected in the ledger, the TerminalWickInput row and the Lean doc comment (comparator copy regenerated) | `319cc2e, ca2b428, 26e30aa` |

Every finding was verified against the Lean source and the TeX at `975feb3` before repair; none was declined. Lean files were changed in doc comments only (stripped sources identical to a8fb495, rebuilt; CheckFidelity 1430/1430, 0 problems after regeneration). Companion main after the merge: `d19c71a`. A confirmation review follows; the gate is Le's decision.
