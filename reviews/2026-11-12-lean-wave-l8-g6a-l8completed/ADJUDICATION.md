# Wave L8 correspondence review: adjudication of every finding

Companion branch `wave-l8/repair`, based on the reviewed commit 3518233. Repairs are in commits
aeaccf6 (docs) and 7af916a (comments only in two refutation files). The file:line references
point to the files at 7af916a. "Ledger" means docs/statement-ledger.md.

## Damped-norm smoothing scope (one defect reported by six reviews)

| Group | Id | Sev | Verdict | Change |
|---|---|---|---|---|
| g1 | W1 | fatal | ACCEPTED | coverage.yaml:165, docs/coverage-scope-tex.yaml:14-15 (ASCII and TeX): new scope sentence of 388 characters. Covariance smoothing is represented only by membership of the Gaussian factor in the multiplier class, and its spectral identification is not formalized. Green smoothing is identified with the smoothed norm only in d = 1. The N_0 identity holds in every d. Class stays same-assumptions/weaker. |
| g1 | W2 | major | ACCEPTED | Ledger Scope 195-204, Index 642, DampedMultiplier intro 1336-1345, full_wave row 1495, DampedNormsHomog 1554-1561 and 1619-1621, WaveGreen 7076-7080. Each "full lemma", "whole result", "every assertion" or "smoothing remarks proved" claim now names both gaps and points to fourier_one for the d = 1 identification. README.md:84-92 is narrowed the same way. |
| g6 | W1, W2 | major | ACCEPTED | These duplicate g1 W1 and W2. Same changes. |
| g6a | W1 | major | ACCEPTED | Duplicate of g1 W1 and W2. Same changes. |
| g6b | W1 | major | ACCEPTED | Duplicate of g1 W1. Same change. |
| g6c | W1 | major | ACCEPTED | Duplicate of g1 W1 and W2, including ledger 1535-1540, 1597-1599 and 6986-6988 at 3518233. Same changes. |

## R_0 at alpha = 0

| Group | Id | Sev | Verdict | Change |
|---|---|---|---|---|
| g1 | W3 | major | ACCEPTED | Ledger 5544-5554: the two files are now described as controls of Lean's totalized division outside the manuscript's domain. At alpha = 0, R_0 is 0/0. The continuous extension gives R_0 = 1, so the identity and the bound both hold at the witness. The comment blocks in refutations/spectral-mass-identity/AlphaPositive.lean:9-17 and FourierBoundAlphaZero.lean:15-20 were rewritten to say the same. This change touches comments only: strip_compare.py against 3518233 finds the code identical for both files. Both files compile on <MACHINE> (`env lean`, exit 0, no output). The probe directories were removed. |

## TerminalWick and FiniteWick

| Group | Id | Sev | Verdict | Change |
|---|---|---|---|---|
| g4 | W1 | fatal | ACCEPTED (docs only; Lean unchanged per decision) | (1) Ledger TerminalWick prose 5919 and 5938-5951 add a new item (3): hK is an added restriction that is not in the manuscript. It gives the non-Borel cut-time example and names the declarations that take hK and those that do not. hK was removed from "implicit hypotheses" at 5963-5964. (2) The terminal_wick_paper row 6043 no longer says "exact-hypothesis"; its inputs cell states the added restriction. (3) The mixed_moment_eq_sum_pairings row 6025 inputs add hK. (4) Scope 280-282 and 293-295 carve hK out of "side conditions the TeX leaves implicit". (5) In coverage.yaml for L:terminal-wick, a third input "an added measurability restriction not in the manuscript, hK: ..." is added. The note no longer calls the hypothesis "explicit", and the scope (ASCII and TeX, 345 characters) adds "the Wick formula adds a hypothesis the lemma lacks: joint measurability of the covariance". (6) README.md:206-211 has the same disclosure. Class: the row was already inputs-supplied/weaker, so nothing changes. The uniform-series-tail row was checked: L8Completed.uniform_series_tail_terminal_wick_paper (L8Completed.lean:312-357) and terminalWickInput_of_nonneg take no hK. That row stays inputs-supplied/full. Its coverage note now says it holds without hK. |
| g4 | W2 | major | ACCEPTED | Ledger 1924-1931 and 1942-1952: the integrability guarantee now covers Gaussian monomials only. The bridge integral_multivariateGaussian_eq for an arbitrary continuous F is described as a totalized identity, with exp(x_0^4) as the example. Integrability transfers only through integrable_multivariateGaussian_iff. |
| g4 | W3 | major | ACCEPTED | Ledger Scope 280-281: the comparison is stated per mixed moment, not for second moments of finite partial sums. This was already true in the coverage scope. |
| g4 | W4 | minor | ACCEPTED | Ledger 1945-1952 lists the finite-wick refutations, marking which are combinatorial and which is an actual Gaussian law. NonnegDropped is marked as using arbitrary weights. Ledger 5997-6002 lists the terminal-wick refutations, which are scalar controls. |
| g6 | W4 | minor | ACCEPTED | Ledger 2850: "the covariance formula hK" is now "the measurability of the covariance K (hK, the added restriction of terminal_wick_paper)". |
| g6a | W3 | minor | ACCEPTED | Duplicate of g6 W4. Same change. |

## Counts

| Group | Id | Sev | Verdict | Change |
|---|---|---|---|---|
| g6 | W3 | major | ACCEPTED | coverage.yaml:10 "fourteen" is now "fifteen". |
| g6a | W2 | major | ACCEPTED | Same change. A recount from coverage.yaml gives 28 same/full, 15 same/weaker, 5 inputs/full, 20 inputs/weaker and 3 outside, for 71 rows. COMPLETION.md already showed 15, and no class changed. |

## Other minor findings

| Group | Id | Sev | Verdict | Change |
|---|---|---|---|---|
| g1 | W4 | minor | ACCEPTED | Ledger Scope 190-193: the identity R_Gamma(1) = R_alpha is now attributed to resolvent_eq_ralpha_paper, and the bound to spatial_fourier_bound_ralpha_paper. |
| g2 | W1 | minor | ACCEPTED | Ledger 4419-4433 restricts "every field" and "integrability of every integrand" to the principal statements. It names the general auxiliary bounds (abs_cross_le, conv_stronglyMeasurable) and the totalized exceptions. |
| g2 | W2 | minor | ACCEPTED | Ledger 2789-2790: "(no manuscript label)" is now "(route lemmas of the proof of T:intrinsic-occupation-ceiling, not separately labelled manuscript results)". |
| g2 | W3 | minor | ACCEPTED (docs only) | New refutation paragraphs at ledger 3613-3621 (OccupationCeilingFinite) and 4461-4468 (SpaceTimePositivity). WrongRowConstant (p = 0, i.e. a = 1), ZeroScoreMax (alpha = 0), CSConstant and VarianceFactor (Lebesgue Gamma) are named as controls for the generalized statements outside the manuscript's model. The refutation files were not changed, because their headers make no claim of manuscript admissibility. |
| g3 | W1 | minor | ACCEPTED | Ledger 5662-5663: the Cauchy rows now repeat rho > 0, the entire map into a complete complex normed space, c > 0 and d >= 0. |
| g5b | W1 | minor | ACCEPTED | Ledger 5725-5731, 5738-5739 and the row at 5816 replace "partitions" with "finite node lists". They state that ordering, endpoints and mesh are not required and that the condition does not characterize the Young evolution. The coverage.yaml L:symplectic-free input adds the weaker supplied form. The coverage scope already said "given only by convergence of its left Young sums", so it is unchanged. |
| g5b | W2 | minor | ACCEPTED | Ledger Not-in-Lean 7438-7442: "supplied as FreeWaveData" now applies to the group, reversal and translation data only. J_E and the preservation of omega are "neither proved nor assumed". |
| g5b | W3 | minor | ACCEPTED | Ledger 5740-5744: T > 0 is unused only in the single-path wrapper. The product wrapper has B and no positivity hypothesis. Verified at SymplecticFree.lean:661 and 681-689. |
| g5b | W4 | minor | ACCEPTED | Ledger 5779: the value at k = 0 is [[1, br t],[0,1]], which is the TeX's matrix after setting br = <0> = 1. |
| g5 | W1-W3 | minor | ACCEPTED | These duplicate g5b W1, W3 and W2. Same changes. |
| g5 | required repair (supply DimensionalMatrix.forward) | packet | REJECTED as a companion repair | This is a gap in the review packet, not a defect in the companion. It was resolved by the g5b rerun, whose packet includes the StratonovichHAMAudit step modules (PASS_WITH_NOTES, requirement A complete). |
| g6 | INCONCLUSIVE checks (incomplete reading) | — | no action | These are reviewer coverage limits, not findings. The rows they touch were covered by g6a, g6b and g6c, which completed reading requirement A. |

## Residual for the orchestrator or Le

The Lean docstrings in StratonovichHAMSecondMoment/TerminalWick.lean still say the following:
- In the module doc near line 52, hK is listed under "Implicit hypotheses made explicit".
- terminal_wick_paper (line 594) is called an "exact-hypothesis wrapper".

These are the same statements that g4 W1 refuted. Per the decision, Lean was not changed. A comment-only change there would rebuild TerminalWick and the modules that depend on it, and would alter the olean and receipt inputs. It should be scheduled with the next Lean wave, or Le can accept the docstring residue, with the docs as the record that overrides it.

## Confirmation round, bd1c439

Reviews c1 (damped/spectral/counts), c2 (wick), c3 (minors); Codex gpt-6.1-sol, high confidence; each FAIL on NO-REGRESSION only, no fatal finding, Lean changes confirmed comment-only. Repairs on branch wave-l8/repair2 (from 2c7e099).

| Review | Finding | Severity | Decision | Action |
|---|---|---|---|---|
| c1, c3 | C1 Scope integrability guarantee (ledger 291-297) | major | ACCEPTED | The blanket "integrability is part of each real-valued integral conclusion" is replaced: integrability is proved where a statement says so (as a conjunct or in a companion theorem); totalized integral identities (the continuous-F Gaussian bridge of FiniteWick, the SymplecticFree cancellation for arbitrary functions) and auxiliary bounds do not by themselves guarantee integrability; extended nonnegative integrals need not be finite. A grep of the ledger, README.md, FORMALIZATION.md and COMPLETION.md for other blanket integrability or no-junk-value promises found none: the remaining statements are local to one declaration or module (e.g. "integral comparison once integrability is known", "integrability inputs are hypotheses"). |
| c2 | C1 TeX mirror completeness (docs/coverage-scope-tex.yaml) | major | ACCEPTED | Fourteen mirrors added (recomputed by script: the same 14 labels). ascii equals the coverage.yaml conclusion_scope byte for byte; tex uses the manuscript macros ($G_h(hA)=hG_1(A)$, $\int N^p\ud\mathcal{N}(0,A)\le\int N^p\ud\mathcal{N}(0,B)$, $\E|\ell_R|^2$, $\nu_R$, $h^{2\beta}$), checked against integrated_covariance_foundation.tex 188-206, integrated_wave_variance.tex 240-246 and 368-382, and main TeX 5187; the eleven generic "finite, algebraic or scalar steps" scopes typeset the path as \texttt{docs/statement-ledger.md}. Rows sorted by label; header now states one row per coverage.yaml conclusion_scope and no other rows. Script: 35 scopes, 35 mirrors, no missing/extra/duplicate, no ascii mismatch. |
| c1 C2, c2 C3, c3 C2 | TerminalWick module comment (lines 31-32) | minor | ACCEPTED | Comment now says both wrappers use the TeX's hypotheses and the supplied inputs; only terminal_wick_paper additionally requires hK, terminal_wick_mono_paper does not. strip_compare: ALL IDENTICAL (code after comment stripping unchanged); Office build of TerminalWick and L8Completed succeeded. |
| c2 | C2 FiniteWick "as a conjunct" (ledger 1924-1926) | minor | ACCEPTED | Now "either as a conjunct or in a separate theorem" (wick_stdPi equality with integrability at a separate theorem). |
| c1 | C3 WaveGreen closing attribution (ledger 7076-7080) | minor | ACCEPTED | The narrowed bundle (smoothing as multiplier membership only) is attributed to damped_homogeneous_norms_full_wave; the identification of the smoothed Green norm with N_{2,m,S} is attributed separately to damped_homogeneous_norms_fourier_one, d = 1 only. |
| all | Limitations (packet omissions, no build) | — | no action | Reviewer coverage limits, not findings. |

The earlier "Residual for the orchestrator or Le" (hK under "Implicit hypotheses made explicit", "exact-hypothesis wrapper") is no longer present at 2c7e099: the module doc now describes hK as an added restriction (line 56) and the phrase "exact-hypothesis wrapper" does not occur.
