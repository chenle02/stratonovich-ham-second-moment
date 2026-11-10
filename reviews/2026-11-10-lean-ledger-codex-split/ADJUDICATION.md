# Adjudication: split Codex GPT-6.1-Sol review of the Lean ledger (M + S)

Object: `docs/statement-ledger.md` at companion `0eb9403`, manuscript `669ccc9`.
Components, coverage and the join: `JOIN.md`, `join-facts.json`. Contracts,
schemas, dry runs, `contract-check` results, packets and full attempt evidence
under `M-main/` and `S-modules/`. Same read-only sandbox and `CODEX_HOME`
workaround as the earlier Codex runs; no auth tokens in the evidence.
Adjudicator: Claude Opus 5.5 (#22).

| ID | Sev | Disposition | Evidence checked at 669ccc9 / Lean | Change (companion 435fdb0) |
|---|---|---|---|---|
| S1 | FATAL | **ACCEPTED** | `integrated_exact_scaling.tex` l.1–56: `L:exact-canonical-scaling` defines `δ=T^{-κ}`, `r_T` and the exponent identities but never uses κ>1. Main TeX l.141–143: `E:kappa` asserts `κ ∈ (1,2)`. `integrated_point_transfer.tex` l.307–308, proof of `P:original-point-transfer`: "Since α<2<3, a<1, we have κ>1", exactly the Lean hypotheses `a<1`, `alpha<3` (`DirectEvent.lean:16-17`). | Row and index → `E:kappa (lower inequality)`; DirectEvent paragraph rewritten (also resolves the LEDGER-SCOPE PARTIAL); `kappa_gt_one` removed from the `L:exact-canonical-scaling` coverage row; new coverage row `E:kappa` (`conclusion: weaker`). Its coverage title "The growth exponent kappa" is descriptive: the equation has no title. |
| M1 | FATAL | **ACCEPTED** | `integrated_temporal_equilibrium.tex` l.32–35: `L:temporal-equilibrium`, "For 0<a<1 put r=(1−a)/2"; l.80–81: "square integrability follow from −r>−1 and −2r=a−1>−1". `LocalFlow.lean:9,12-14`: `noiseOrder α = (1−α)/2`, `0 ≤ r ∧ r < 1/2 ∧ α−1 = −2r` for `0<α≤1`. With α := a this is the range and identity used. Difference recorded: Lean gives `r ≥ 0`; the manuscript's `a<1` gives `r>0`, which the Γ factors need. | Row and index → `L:temporal-equilibrium (with alpha = a)`; LocalFlow paragraph names the exception and the r>0 difference; new coverage row (`conclusion: special-case`) |
| S LEDGER-SCOPE | PARTIAL | **ACCEPTED** (same defect as S1) | DirectEvent paragraph attributed κ>1 to `L:exact-canonical-scaling` | Fixed with S1 |

No finding rejected; no Lean or manuscript defect. Counts after repair:
**40 labelled, 48 unlabelled** (script: index equals per-module tables; all 56
cited labels exist at 669ccc9). coverage.yaml: 28 rows (24 inputs-supplied,
4 outside). Companion `435fdb0` is a docs-only descendant of `38d16163ab89`.

Gate status: see `JOIN.md`, not closed. Downstream: the work-package board
needs Group B rows for `E:kappa` and `L:temporal-equilibrium` (levels are the
owner's decision); unlabelled 49 → 48.
