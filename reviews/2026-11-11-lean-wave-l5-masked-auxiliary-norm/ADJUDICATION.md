# Adjudication: wave-L5 correspondence review, MaskedAuxiliaryNorm (whole result)

- **Object:** the ledger section "MaskedAuxiliaryNorm (whole result)", its index rows, its
  coverage rows and cross-references at companion `210cc3f` (manuscript
  `975feb3`). Reviewer: Codex GPT-6.1-Sol, effort high, read-only,
  `CODEX_HOME` workaround; frozen packet with every library module (the
  section's own modules read completely), claims.yaml, coverage.yaml (and
  docs/coverage-scope-tex.yaml where the contract names it), all 78 TeX
  inputs at `975feb3`; contract-check, dry run and contract-check on the
  dispatched prompt clean.
- **Result:** valid, **FAIL**, confidence high; 66 checks: 65 PASS, 1 FAIL; 1 finding(s), all documentation, none in a Lean statement or proof.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| W1 | major | **ACCEPTED** | 42 no-direct-label declarations absent from the index; added in three sub-classes (transform convention 8-12, setup 79-82, route auxiliaries) | `18965bb` |

Every finding was verified against the Lean source and the TeX at `975feb3`
before repair (companion branch `l5-repair`, merged into main). A narrow
confirmation review of the repairs follows; the gate is Le's decision.
