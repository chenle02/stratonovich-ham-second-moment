# Adjudication: wave-L6 correspondence review, item f-StaticControls

- **Object:** the wave-L6 ledger section(s) of this item, their index rows,
  coverage rows and cross-references at companion `250cf39` (manuscript
  `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only,
  `CODEX_HOME` workaround; frozen packet with every library module (the
  item's own modules read completely), claims.yaml, coverage.yaml,
  docs/coverage-scope-tex.yaml and all 78 TeX inputs at `975feb3`;
  contract-check, dry run and contract-check on the dispatched prompt clean.
- **Result:** valid, **FAIL**, confidence high; 84 checks: 81 PASS, 3 FAIL; 2 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion branch `l6-repair`) |
|---|---|---|---|---|
| W1 | fatal | **ACCEPTED** | verified against the Lean source and the TeX at `975feb3`: rayleighFloor_volume / PARA-SpatialStaticControls: candidate/statement-ledger | `7022b14` |
| W2 | major | **ACCEPTED** | verified against the Lean source and the TeX at `975feb3`: CROSS-REFERENCES: candidate/statement-ledger | `4574ba7` |

Every finding was verified before repair; none was declined. Lean files
were changed in doc comments only (comment-stripped sources identical,
recompiled). The repairs are on companion branch `l6-repair`
(`250cf39`..`5373db5`), merged into main; a confirmation review follows;
the gate is Le's decision.
