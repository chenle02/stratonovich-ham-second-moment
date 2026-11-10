# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I found no proof-breaking gap, no false identity, no silently assumed raw-overlap theorem, and no invalid constant or sign in the audited successor (proof.md lines 1–324) or in the seven production responses. All seven v1 requests are materially addressed, and the O1/O2/O3 deductions remain sound when the named construction modules are taken as the declared bounded inputs.

## Noncritical findings

1. **Imported construction results remain un-re-verified.** The deductions lean on named inputs: P:actual-operator-driver, P:source-gaussian-transfer, P:source-ordinary-response, P:constant-young-linear, P:constant-gaussian-flow, L:constant-phase-free, L:driver-gain-localization, and L:source-retaining-isometry. I audited their exact interfaces and usage, not their full source-paper proofs, exactly as the scope directs. No mismatch detectable from the supplied excerpts.

2. **PaperDev-Tailored-Workflow.md excerpt is still missing** in this snapshot. Recorded as a limitation; it does not change the verdict because statement.json, scope.txt, the four construction TeX excerpts, and the adjudication give a complete interface to audit the new bytes.

3. **Proposition C measurability is correct but compressed.** The equality `D = sup_{(s,t)∈Δ_T^Q} sup_l ‖A(t,s)e_l‖` is justified by (i) density of {e_l} giving the operator norm at each fixed time pair and (ii) joint strong continuity plus a dense rational triangle for each fixed e_l. Equivalently this uses lower semicontinuity of the operator norm under strong convergence; that one word is not stated, though the two-step argument in lines 248–257 is valid.

4. **Expectation transfer glosses a null set.** The triangle inequality `D ≤ (two errors)` holds everywhere; the middle source difference is zero on Ω_A, whose complement is null, so `E_ext D ≤ E_ext(err1)+E_ext(err2)` is valid. This is implicit at lines 267–278 but not spelled out; no defect.

5. **Minor typography:** line 151 “satisfies(A1)” is missing a space; purely cosmetic.

6. **Repair checklist location.** The seven-item repair resolution is enumerated in production-adjudication.md rather than inside proof.md itself; proof.md’s “Remaining gates” records the scope limitations but not a per-item checklist. Not a correctness issue given the adjudication is in-scope context.

## Checked derivations

- **E-restriction (Lemma A).** `A i = i M_E`, `π_C A = 0`, `S_F(t)i = i S(t)` preserve iE; the induced-norm inequality `‖Q|_E − Q′|_E‖ ≤ ‖Q − Q′‖_{B(F)}` holds for invariant operators, so restriction is bounded linear and transfers strong measurability/moments/convergence. No density of E in F is used. Correct.
- **Coefficient bound.** `‖B(v)‖` computation: `B(u,v)=(0,bu)`, `‖bu‖_{H^{−1/2}} ≤ ‖bu‖_{L²} ≤ ‖b‖_∞‖u‖_{L²} ≤ ‖b‖_∞‖(u,v)‖_E`, since `‖u‖_{L²} ≤ ‖u‖_{H^{1/2}}` under the Bessel potential convention. `K = sup_r‖b‖_∞` is finite from input-3 smoothness; no derivative norm or uniformity in (j,N,R) is asserted. Correct.
- **Young-to-ordinary exchange.** Line 128–129 error `T·sup‖C‖·ω_V(mesh)` is right: `Σ∫‖C(r)(V(r_k)−V(r))‖dr ≤ sup‖C‖·ω_V(mesh)·(t−s)`. The integrator is the Hölder/Lipschitz primitive `M_R^n`, not C; the rejection of requiring C itself to be C^θ is sound (bounded strongly continuous C + uniformly continuous V is enough). Correct.
- **Picard bound and uniqueness.** `‖Q_k‖ ≤ C_T^{k+1}K^k(t−s)^k/k!` checked by induction; homogeneous-difference iteration to `(C_T K T)^k/k! → 0` yields uniqueness among continuous E-valued solutions; no operator-norm derivative of the free group assumed. Correct.
- **Cone supports (Lemma B).** `K_r = B(2j+1+t−r)`; backward cone `K_r ⊕ B(v−r) = K_v`; guard `R,N ≥ 2j+T+3` forces masks/cutoffs equal one on neighborhoods of every closure, with strict margin (`2j+1+T ≤ R−2`, `N−2`). Correct radii and directions.
- **Forcing decomposition.** `B_1q_1 − B_2q_2 = B_1(q_1−q_2) + (B_1−B_2)q_2`; first term killed by smooth-multiplier distributional vanishing (pairing with `bφ`), second by `(m_{R1}−m_{R2})Y_n = 0` on `K_r`; both phase components retained. Correct.
- **Horizon restriction (Lemma B).** Same retaining time field on both horizons; longer solution restricted to shorter triangle solves (A1) and ordinary uniqueness identifies it with the shorter flow; no raw-version gluing assumed. Correct.
- **Measurability and expectation transfer (Proposition C).** Joint strong continuity of `S(t)U(t,s)S(−s)` follows from norm continuity of U plus strong continuity/boundedness of S; the triple-sequence argument at lines 240–246 is valid. Countable rational-triangle/dense-sphere supremum makes D W-measurable; `E_original D = E_extension D` because D is a W-measurable pullback; a.s. triangle inequality plus `lim_n(err)=0` (input 4, L¹ triangle norm) force `D=0`. Countable integer-tuple intersection only. Correct.
- **A.s. universality.** `D=0` equals zero operator-norm over the whole (continuous) triangle and all states, so a single event covers all states and real times for each tuple; no uncountable intersection over states/time/source widths. Correct.
- **O3 local consequence.** `e = D_{ψ_M}z ∈ E` by the explicit local-Sobolev definition; `M > 2max(N1,N2)` makes `ψ_M = 1` on neighborhoods of both data-cutoff supports so `D_{ψ_Ni}e = D_{ψ_Ni}z`; Proposition C applied to the global e proves the tested identity without a point trace or an unmasked global operator, and without claiming a local Fréchet composition law. Correct.
- **Zero covariance.** Γ = 0 reduces to free propagation and horizon uniqueness; no nondegenerate Gaussian/Cameron assumption used at line 292–294. Correct.

### Scope determinations (F01–F10)

- **F01 — Countable common source events:** PASS. Ω_A is the countable intersection of Ω_A(n,R,T); Lemma B fixes a sample in it covering both masks and both horizons; all-state/all-initial-time identification included.
- **F02 — Distributional forcing/propagation, B1(q1−q2)+(B1−B2)q2, both components:** PASS. Explicit and correct.
- **F03 — Young objects M and V, θ>1/2, rejection of C-Hölder, bounded strongly continuous C, exchange estimate:** PASS. Rejection is independently justified.
- **F04 — Joint strong continuity, countable dense-unit/rational-triangle supremum, measurability/versions:** PASS. Valid; see Noncritical 3.
- **F05 — Explicit finite constants, exact Sobolev embeddings, no derivative/uniform-cutoff overclaim:** PASS. K is explicit and finite; uniformity explicitly disclaimed.
- **F06 — Local Sobolev definition, global cutoff input, O3, no point trace/unmasked global operator:** PASS.
- **F07 — Imported-source and missing-workflow-excerpt boundaries:** PASS. Limitations recorded; no image/novelty/full-source claim.
- **F08 — Full Lemma A/B/Proposition C + O1/O2/O3 no-regression, realization-vs-law, Γ=0, tuple guards, expectation transfer:** PASS. All guards and the same-realization (not merely equal-law) route are respected (lines 40–44, 277–278).
- **F09 — Seven prior requests adjudicated; rejection judged on proof:** PASS. All seven addressed; the two author refusals (C-Hölder, derivative-norm) are sound and do not weaken the argument.
- **F10 — Scoped production disposition, repairs/unresolved/limitations, no full acceptance:** PASS (with note). proof.md's “Remaining gates” correctly avoids full-project acceptance; the explicit repair resolution sits in the adjudication rather than in proof.md itself.

## Required fixes before production gate

No correctness-blocking fixes are required. Optional, non-blocking improvements:

1. In Proposition C, add one clause that the operator norm is lower-semicontinuous under strong convergence (or cite the joint-continuity/dense-triangle two-step) to make the rational-triangle reduction instantaneous.
2. Spell out that the a.s. triangle inequality only needs the middle source term to vanish on Ω_A, whose complement is null.
3. Optionally move the seven-item repair-disposition checklist from production-adjudication.md into proof.md’s “Remaining gates” for self-containedness.

## One-line summary

The successor is mathematically sound given its named construction inputs: signs, boundary supports, constants, Young/ordinary exchange, measurability, countable event bookkeeping, expectation transfer, and the O3 local-cutoff consequence all check out, with only the residual record of the missing workflow excerpt, imported un-re-verified source results, and two compressed-but-valid continuity/null-set sentences.