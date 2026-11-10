# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

None. The NEW worked supplement expands, rather than alters, the mathematics already present in the tracked source, and its expanded calculations are correct within the stated guards. No false identity, sign error, boundary-term error, incorrect constant, or invalid asymptotic was found in PROOF087, PROOF092, or the PROOF093 assembly.

Specific spot-checks that passed:

- The shrinking-cone/energy identity in supplement §A is exact:
  e = (v² + |∇u|²)/2, ∂_t e = div(v ∇u), and
  dE_ρ/dt = ∫_{∂B(ρ−t)} (v∂_n u − e)dS ≤ 0,
  with 2v∂_n u ≤ v² + (∂_n u)² ≤ v² + |∇u|². Both initial entries are required, and displacement recovery u(t,x) = u(0,x) + ∫_0^t v(τ,x)dτ needs the zero initial displacement; the supplement states these two indispensability conditions correctly.
- Time reversal S(−t) = J S(t) J with J(u,v) = (u,−v) is verified against the explicit Fourier matrix in `E:variance-free-matrix` (including the sine quotient value t at zero frequency).
- Gain and adjoint dual indices: B(b)(u,v)=(0,bu) maps E_r → E_{r+1} because the second slot index rises r−1 → r under multiplication by a smooth bounded-derivative coefficient; dualizing gives E_{2s−r−1} → E_{2s−r} = E_{−r} → E_{1−r}, and γ < 1/2 makes both A_j and its adjoint map E_{s−γ} → E.
- The covariance row identity E[g_j ℓ_R(I;z,w)] = ⟨A_j(I)z,w⟩_E chains `E:driver-literal-covariance` through `E:variance-physical-adjoint`; the mask positioning (mask after convolution, not inside Γ∗f_j) is correctly flagged.
- The deterministic dyadic C^η control constant 2^{1+η}(1+T^{−η}) is re-derived and the F(0)=0 / nonzero-constant failure mode is correct and non-circular (Lipschitz paths give finite Z_η for η < 1).
- The p-dependent even-q selection q = 2 ceil(max(p,q0)/2) satisfies q ≥ p, q even, q ≤ p+q0+2 ≤ (q0+3)p (the last via (q0+2)(p−1) ≥ 0), so Lyapunov carries L^q → L^p; the supplement correctly records that a fixed-q L^q bound gives only p ≤ q.
- The exponential-moment series uses even moments Y^{2m}, m! ≥ (m/e)^m, giving a (2e c C1²)^m majorant and c < 1/(2e C1²); the C1 = 0 case is handled.

## Noncritical findings

1. The supplement’s opening references to a prior “PASS_WITH_NOTES/MEDIUM” report, its nine raw FULL rows, eleven PASS checks, and an adjudicated fixed-q/Lp wording cannot be verified from this intentionally blind snapshot (no Progress.md / Review.md / reviews/ read). Per scope, this is historical commentary, not a proof premise, and it was not used.
2. Upstream numeric constants are consumed as premises rather than re-derived here: e.g. C0(a)=16/(1−a) in `L:masked-temporal-modulation`, C_T in `P:wave-two-variances`, C_ν, and the constants in `P:frequency-row`. Their derivations were read and found consistent, but the constants were not independently recomputed.
3. The exponential moment is established through even moments only. This is sufficient for E exp(cY²) and the source states it, so it is not a defect, but it should not be read as control of arbitrary odd Schatten/moment indices.
4. The concrete allowed tuple (d=1 white, α=1, a=1/2, γ=1/4, θ=9/16, η=5/8, β=11/16, q0=32) checks out exactly; the general-d requirement q0 > d/γ is covered elsewhere by the source but is not exercised by that single tuple.
5. The supplement correctly disclaims any uniform-in-R path norm, any C^θ Schatten-valued path, and any source/global/cold/full-goal credit; no overclaim was found.

## Checked derivations

Primary targets (complete actual bodies + supplement bridges):

- PROOF087 `L:driver-gain-localization` (source LF169–237; supplement §A and LF2615–2651).
- PROOF092 `L:driver-holder-limit` (source LF463–553; supplement §B and LF2653–2724).
- PROOF093 `P:actual-operator-driver` assembly (statement LF27–55, proof LF555–591; supplement LF2714–2724).

Per-proof ledger (each 085–093, explicit status and residual):

- PROOF085 `L:driver-noise-basis` — RECONSTRUCTED (basic). Checked: separability via countable dense tests on rational boxes with the continuity estimate `E:driver-test-continuity`; infinite-dimensionality via the tensor witness q and positivity of ‖τ‖_a through the ODE v′ = λv − τ; Gram–Schmidt basis and independence via Gaussian characteristic functions. Residual: Laplace factorization from `L:masked-time-completion` and Γ(B_L) > 0 positivity used as premises.
- PROOF086 `L:driver-covariance-coefficients` — RECONSTRUCTED. Checked: smoothness/support B_{2R} of H_{j,R} by dominated convergence (mask applied after convolution); covariance identity via physical covariance + Fubini; representative-class independence by distribution testing and continuity at t=0. Residual: physical covariance formula of the masked-covariance section as premise.
- PROOF087 — RECONSTRUCTED (primary). Checked: gain-one E_r → E_{r+1}; adjoint dual gain E_{2s−r−1} → E_{2s−r} and both operators E_{s−γ} → E; two-entry finite propagation (flux identity, cone vanishing, arbitrary centers, time reversal, d=1 boundary = two endpoints); cutoff margins B(2R+T+1) and B(2R+T); both localization identities; raw row covariance. Residual: bounded/strong continuity of S(t) on E_r and boundedness of smooth multiplication on H^r used as upstream facts.
- PROOF088 `L:driver-actual-variances` — RECONSTRUCTED. Checked: orthogonal-projection inequality E|⟨X_N e_k,w⟩|² ≤ E|ℓ_R(e_k,w)|²; both variance directions obtain b_I = C_T h^{2−a}B_α(h); V_out,V_in ≤ b_I D_γ²; first-chaos expansions; tail strong-to-zero and limit localization; complexification. Residual: `P:wave-two-variances`, `P:wave-square-columns`, `P:compact-two-envelopes` consumed as premises.
- PROOF089 `L:driver-dominated-tails` — RECONSTRUCTED. Checked: finite spectral projection Q, weak→norm via 2‖QT_NQ‖ + 2ε; λ_j(T_N) ≤ λ_j(B) and dominated summation → trace-to-zero. Residual: `L:compact-positive-order` as premise.
- PROOF090 `L:driver-gaussian-tail-average` — RECONSTRUCTED. Checked: compression variance inequalities; average form of `P:finite-gaussian-matrix`; operator-norm convergence of compressed sums; singular-value norm-Lipschitz + Fatou. Residual: `P:finite-gaussian-matrix` as premise.
- PROOF091 `L:driver-interval-limit` — RECONSTRUCTED. Checked: hypotheses of `P:localized-finite-variance`/`C:finite-gaussian-operators` are satisfied by 087/088; tail Cauchy; strong measurability; compact centered Gaussian limit; fixed row identity; long-interval additivity with null endpoints and no false long-h Schatten formula. Residual: `P:localized-finite-variance`, `C:finite-gaussian-operators` as premises.
- PROOF092 — RECONSTRUCTED (primary). Checked: increment L^q(operator-norm) ≤ C√q |t−u|^β via finite Gaussian bound + strict β refinement + ‖K_χ‖_{S_q} ≤ ‖K_χ‖_{S_q0}; dyadic D_n moment bound without independence; coarse/fine geometric sums with δ0 = β−η−1/q0 > 0; C^η control with exact constant; finite-grid N,M-then-mesh Cauchy (no pointwise⇒uniform shortcut); interpolation with supremum term; scalar probability Hölder at the same q; C^θ Cauchy and separable path span; single path event for compact values. Residual: the h^{2β} version of `P:wave-two-variances` is consumed as premise.
- PROOF093 — RECONSTRUCTED (primary assembly). Checked: assembly of 085–092 on the original probability space; raw row identity and long-interval reading; centered Gaussian path and complexified sesquilinear identity via the four real pair identities; indistinguishability through a countable dense Schwartz phase set and rational times (no uncountable common-event assumption); all-time compact values on one path set; per-p even q with q ≤ (q0+3)p, Lyapunov ⇒ C√p; exponential moment with c < 1/(2e C1²). Residual: consumes 085–092; operator-norm Hölder path only, as correctly stated.

Upstream proof inventory (all in-scope bodies were read in the embedded packet; none genuinely unread):

- REDERIVED in this review (supplement-supported): two-entry free-wave finite propagation (flux/cone/time reversal); Sobolev-distribution support extension and mollified-output backward support; deterministic dyadic C^η control, coarse/fine sums, finite-grid/interpolation Cauchy, p-dependent even-q and exponential moment.
- STATEMENT_VERIFIED / USED_AS_PREMISE (not re-derived from first principles here): `L:masked-time-completion`, `P:masked-spectral-growth`, `P:masked-auxiliary-norm`, `P:masked-noise-completion`, `L:masked-temporal-modulation`, `L:masked-trig-products`, `L:masked-continuous-wave`, `P:frequency-row`, `C:frequency-time`, `P:actual-wave-form`, `L:phase-bessel`, `P:wave-two-variances`, `P:wave-square-columns`, `P:finite-gaussian-matrix`, `L:cutoff-factorization`, `P:cutoff-singular-values`, `P:compact-two-envelopes`, `L:compact-positive-order`, `P:localized-finite-variance`, `C:finite-gaussian-operators`, `P:cutoff-boundary-tests`.
- UNREAD: none.

DA ledger:

- DA01 — VERIFIED. Fixed R,T>0; d∈{1,2,3}; a=α0∈(0,1); α+a<2; s=1/2; E_r=H^r×H^{r−1}; strict guards 0<γ<min(1/2,(2−α)/2) and 1/2<θ<β<min(1−a/2,(3−a−α)/2); q0 even, q0γ>d, δ0>0; Γ=0 bypass; γ strictly positive; two-entry massless group with sine quotient t at zero; H_{j,R} smooth supported in B_{2R}; B(b)(u,v)=(0,bu); statewise integral; “norm continuity of S(t) is not needed”; gain/adjoint dual indices and raw row covariance checked (not only localization).
- DA02 — VERIFIED. Exact shrinking-ball Reynolds/divergence identity and nonpositive flux; zero v,∇u then displacement recovered from zero u0; both initial entries carried; cones for arbitrary centers; time reversal J(u,v)=(u,−v); d=1 boundary as two endpoints; wave speed 1.
- DA03 — VERIFIED. Extension for every real r; Schwartz input retaining (1−D_χ); margin B(2R+T+1); output force mollified to support B(2R+ε) and convergent in E_{r+1}; backward support B(2R+t); statewise integral support B(2R+T); both entries; D_χ^{*,E} ≠ D_χ correctly maintained (`E:variance-cutoff-adjoint`).
- DA04 — VERIFIED. Dyadic control for any continuous Banach F with F(0)=0; Δ_{n+1} < v−u ≤ Δ_n; floor projections; ≤ two adjacent increments plus finer binary tails; constant 2^{1+η}(1+T^{−η}); no converse norm equivalence; Lipschitz paths make Z_η finite; η<1 and nonzero-constant falsification checks present.
- DA05 — VERIFIED. C√q increment bound from the complete two-variance + finite Gaussian interfaces; all admissible even q ≥ q0; Schatten norm monotonicity ‖K_χ‖_{S_q} ≤ ‖K_χ‖_{S_q0}; constants independent of q/N/basis; finite maximum 2^{n/q} without independence; coarse levels partitioned into unit intervals; T<1 / T=1 / T>1 handled via n_f; fine geometric gap δ0 > 0.
- DA06 — VERIFIED. Finite-grid L^q C^0 Cauchy in the order N,M then mesh→0; no pointwise⇒uniform shortcut; deterministic interpolation including the supremum term with (1+2^{1−λ})A^{1−λ}B^λ; scalar probability Hölder at the same q; C^θ Cauchy and separable closed span; one all-time compact event.
- DA07 — VERIFIED. New even q per p via 2 ceil(max(p,q0)/2); q ≤ p+q0+2 ≤ (q0+3)p; Lyapunov only p ≤ q; 2m/m! and squared-norm exponential moments with C1=0 case; fixed-q bound does not give all p (the supplement correctly identifies the raw fixed-q wording as not the source argument); strict window/zero case and tuple d=1 white α=1, a=1/2, γ=1/4, θ=9/16, η=5/8, β=11/16, q0=32 with δ0=1/32 and p=1→q=32, p=33→q=34, p=100→q=100.
- DA08 — VERIFIED. Assembly uses the given W/first-chaos raw definitions; 091 is used only where its proved guards (localization, variances) hold; fixed Schwartz raw rows; path/interval uniqueness in probability; additive long intervals with null endpoints; no false long-h Schatten formula; centered Gaussian path.
- DA09 — VERIFIED. Complex four-pair identities; basis indistinguishability via countable dense phases + rational times; no uncountable common-event assumption; cutoff/basis dependence noted; compact values on one path set; operator-norm path scope only.
- DA10 — PROVIDED. Per-proof ledger (085–093), DA01–DA10 ledger, and upstream rederived/premise/unread inventory are all stated above; structural completeness is reported independently of any clean-exit/stop claim. No Skorohod/Lean/HPC/source-evolution/sharp-asymptotic/uniform-growing-R/C^θ-Schatten conclusion follows from this unit, and none is asserted.

## Required fixes before production gate

None (no mathematical defect found). Optional, non-blocking: the supplement could state explicitly that its leading historical-report references are unverifiable in a blind snapshot and that upstream constants (C0(a), C_T, C_ν, row-bound K) are source-verified premises rather than components of this supplement’s own re-derivation. No change to any proof is required.

## One-line summary

The NEW worked supplement correctly and completely expands PROOF087’s two-entry finite-propagation/localization/gain/adjoint/raw-row argument and PROOF092/093’s dyadic-to-Hölder, finite-grid/interpolation, and per-p even-q/exponential-moment bridge with no false identities, sign errors, constant errors, hidden hypotheses, or invalid asymptotics; no critical finding, and no source overclaim.