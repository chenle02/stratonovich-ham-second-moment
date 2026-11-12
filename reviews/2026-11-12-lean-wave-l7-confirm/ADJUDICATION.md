# Adjudication: wave-L7 confirmation review

- **Object:** the repairs of the six wave-L7 reviews (companion branch `l7-repair`, merged at `d2d29df`; main `d19c71a`), against manuscript `975feb3`. Reviewer: Codex GPT-6.1-Sol, effort high, read-only; packet with the six prior reports, every library module, claims.yaml, coverage.yaml, docs/coverage-scope-tex.yaml and all TeX inputs; preflight clean.
- **Result:** valid, **FAIL**, confidence high, receipt not accepted; 17 checks (9 prior findings, 6 rescans, totals, no-regression).

| ID | Sev | Disposition | Verified | Repair |
|---|---|---|---|---|
| C1 | major | **ACCEPTED** | verified: the IntervalScalar.static_block_series ledger row and claims.yaml summary still said both positivity binders were unused; `_ha0 : 0 < alpha0` is used (with alpha + alpha0 < 2 it gives alpha < 2), `_hα0 : 0 < alpha` is unused | `b0c995b` |
| C2 | minor | **ACCEPTED** | verified: one ledger row and its claims summary still said H^1 convergence of the gradients | `b0c995b` (and one introductory sentence, finding A4 below, at `1265681`) |

The repairs were made together with the re-anchor to manuscript `a284420` and confirmed by its narrow re-check (`reviews/2026-11-12-lean-reanchor-a284420`: CONFIRM-C1 PASS, CONFIRM-C2 PASS_WITH_NOTES, the note repaired as A4) and the re-anchor confirmation (PASS/high).
