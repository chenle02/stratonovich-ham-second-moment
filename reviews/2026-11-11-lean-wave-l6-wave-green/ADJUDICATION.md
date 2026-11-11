# Adjudication: wave-L6 correspondence review, item a-WaveGreen

- **Object:** the wave-L6 ledger section(s) of this item, their index rows,
  coverage rows and cross-references at companion `250cf39` (manuscript
  `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only,
  `CODEX_HOME` workaround; frozen packet with every library module (the
  item's own modules read completely), claims.yaml, coverage.yaml,
  docs/coverage-scope-tex.yaml and all 78 TeX inputs at `975feb3`;
  contract-check, dry run and contract-check on the dispatched prompt clean.
- **Result:** valid, **PASS_WITH_NOTES**, confidence high; 35 checks: 34 PASS, 1 PASS_WITH_NOTES; 3 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion branch `l6-repair`) |
|---|---|---|---|---|
| W1 | minor | **ACCEPTED** | verified against the Lean source and the TeX at `975feb3`: PARA-WaveGreen, exponential-integral explanation | `e4f7b27` |
| W2 | minor | **ACCEPTED** | verified against the Lean source and the TeX at `975feb3`: PARA-WaveGreen, used-field bookkeeping | `9c81373` |
| W3 | minor | **ACCEPTED** | verified against the Lean source and the TeX at `975feb3`: Stale supporting metadata. claims.yaml:6200 says 'the package defines no wave Green measure', and DampedNormsHomog.lean:48-52 says the WaveGreen discharge 'was not attempted' | `89cea2f, 5373db5` |

Every finding was verified before repair; none was declined. Lean files
were changed in doc comments only (comment-stripped sources identical,
recompiled). The repairs are on companion branch `l6-repair`
(`250cf39`..`5373db5`), merged into main; a confirmation review follows;
the gate is Le's decision.
