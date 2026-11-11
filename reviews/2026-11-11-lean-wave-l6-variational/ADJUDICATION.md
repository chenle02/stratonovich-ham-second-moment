# Adjudication: wave-L6 correspondence review, item d-Variational

- **Object:** the wave-L6 ledger section(s) of this item, their index rows,
  coverage rows and cross-references at companion `250cf39` (manuscript
  `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only,
  `CODEX_HOME` workaround; frozen packet with every library module (the
  item's own modules read completely), claims.yaml, coverage.yaml,
  docs/coverage-scope-tex.yaml and all 78 TeX inputs at `975feb3`;
  contract-check, dry run and contract-check on the dispatched prompt clean.
- **Result:** valid, **PASS_WITH_NOTES**, confidence high; 82 checks: 80 PASS, 2 PASS_WITH_NOTES; 3 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion branch `l6-repair`) |
|---|---|---|---|---|
| W1 | minor | **ACCEPTED** | verified against the Lean source and the TeX at `975feb3`: PARA-VariationalRate, diagonal convention: candidate/statement-ledger.md:4341-4343 says '/s-u/^(-alpha0) >= 1 on [0,1]^2' | `6057c14` |
| W2 | minor | **ACCEPTED** | verified against the Lean source and the TeX at `975feb3`: SCOPE-PROSE, umbrella wording: candidate/statement-ledger.md:48-50 says the conclusions of thirty-eight labelled results are formalized 'in full', although its subsequent qualifications and coverage.yaml explicitly ident | `9fa681b` |
| W3 | minor | **ACCEPTED** | verified against the Lean source and the TeX at `975feb3`: SCOPE-PROSE, status terminology: candidate/statement-ledger.md:223-237 can be read as equating all proof-route helpers with status 'internal' | `5eeedb2` |

Every finding was verified before repair; none was declined. Lean files
were changed in doc comments only (comment-stripped sources identical,
recompiled). The repairs are on companion branch `l6-repair`
(`250cf39`..`5373db5`), merged into main; a confirmation review follows;
the gate is Le's decision.
