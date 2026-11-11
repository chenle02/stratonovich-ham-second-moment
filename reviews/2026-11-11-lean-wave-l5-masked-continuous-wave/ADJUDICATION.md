# Adjudication: wave-L5 correspondence review, MaskedContinuousWave (whole result)

- **Object:** the ledger section "MaskedContinuousWave (whole result)", its index rows, its
  coverage rows and cross-references at companion `210cc3f` (manuscript
  `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only,
  `CODEX_HOME` workaround; frozen packet with every library module (the
  section's own modules read completely), claims.yaml, coverage.yaml (and
  docs/coverage-scope-tex.yaml where the contract names it), all 78 TeX
  inputs at `975feb3`; contract-check, dry run and contract-check on the
  dispatched prompt clean.
- **Result:** valid, **FAIL**, confidence high; 28 checks: 25 PASS, 3 FAIL; 2 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| W1 | major | **ACCEPTED** | bFn_contDiff (:223) and bFn_bounds (:242) are not stated or used in TeX 392-423 (b_r = t<r> int cos(vrt) dv; A = t^j); docstrings say auxiliary | `ab98d90` |
| W2 | major | **ACCEPTED** | index listed 13 of 24 declarations; every other whole-result section has an auxiliary index row | `ab98d90` |

Every finding was verified against the Lean source and the TeX at `975feb3`
before repair (companion branch `l5-repair`, merged into main). A narrow
confirmation review of the repairs follows; the gate is Le's decision.
