# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. After complete hand verification of PROOF004 (L:damped-homogeneous-norms), PROOF005 (L:spatial-wick-measures), and PROOF006 (L:joint-fixed-order), I found no false identity, no wrong sign, no incorrect constant, no hidden hypothesis breach, and no invalid asymptotics in the exact target excerpt (lines 3–414 of review-material.txt). Every scaling law, resolvent integral, Laplace-limited heat identity, Brownian moment bound, mass bound, homogeneity exponent, horizon/zero-face argument, telescoping tail decomposition, and the Theorem 3.1 application were checked by hand and are correct.

## Noncritical findings

1. **(J08, source presentation) The printed source (3.5) uses `G(s,x)G(t,x)` for the second norm, duplicating `x`.** The second variable should be `y`. The target manuscript is alive to this: line 25–26 explicitly reads the second Green factor “with the independent variable `y`,” and lines 23–24 state the pairing of `G_θ(s,x)` with `G_θ(t,y)`. This is a disclosed source typo, handled correctly, not a target error.

2. **(J08, source presentation) Source Case 2 (held PDF p. 21, review-material lines 5067–5073) displays `γ⁰_(n1,2n)(s−r) γ_(n1,2n)(x−y)` and claims “Cauchy-Schwarz + shift-invariance,” but the substitution actually retains offsets `τ₀ = s_{2n−1} − s_{n1−1}` (time) and `z₀ = x_{2n−1} − x_{n1−1}` (space).** The offset-free displayed form drops these. The argument is nevertheless *salvageable without silently repairing it*: the offset kernel `γ⁰((s+τ₀)−r) · γ(y−(x−z₀))` is a Schur product of shifted PSD kernels (hence PSD), and its diagonal quadratic form is shift-invariant, so the stationary-covariance Cauchy–Schwarz still yields `≤ ‖G_{n1}‖⁽²⁾ ‖G_{2n}‖⁽²⁾`. This is a presentation gap in the *source's* proof of the imported theorem, not a flaw in the target's use of it (the target imports Theorem 3.1 wholesale, line 356–357).

3. **(J09, completeness) The explicit admissible constant `C_{k,T1,T2}` is asserted abstractly** (“Constants may depend on the fixed covariance and `k,T1,T2`,” lines 374–375), not displayed. I derived a valid explicit admissible value by hand (see Checked derivations, PROOF006): `C_{k,T1,T2} = 4k·e^{T1+T2}·max{1, 2N1(1), N2(1)}^{2k}` with `N0(1)=1`. This *verifies* the existence claim; the manuscript itself does not print it. No uniformity in `k`, `T`, or covariance is claimed, and none is used — correct.

4. **(J01/J02, exposition) The positivity `N2(θ)² ≥ 0` is asserted via “positive Laplace mixture” (lines 87–89) without spelling out that `e^{−θ(s+t)}` is PSD, `e^{−λ|s−t|}` is PSD, and their Schur product is PSD.** The conclusion is correct; the working is compressed.

5. **(J10, exposition) “Cap the temporal Laplace domains above” (line 358) is terse.** The bound is monotone in the caps, so cap removal by positivity is legitimate; the exact role of the cap is not expanded. Non-blocking.

6. **(Notation) The statement line 49 writes `N2^{(M)}(1) ⟶ 0`, while the proof (line 103) uses `N2^{(M)}(1)² ⟶ 0`.** Harmless: a nonnegative quantity tends to 0 iff its square does.

7. **(J07, exposition) Homogeneity is passed through vague limits (line 304) and then extended to Borel sets.** This is the correct compact-test route (J07 requires exactly this, not an unjustified arbitrary-Borel set limit), but the boundary-`ρ_D`-mass-zero step is only implicit. Standard.

None of these is blocking.

## Checked derivations

Wholly by hand, with every constant, limit, sign, and hypothesis checked.

**PROOF004 — Lemma L:damped-homogeneous-norms (lines 28–116).**
- `Γ(cA)=c^{d−α}Γ(A)` ⇒ `μ(cA)=c^α μ(A)` (Fourier scaling + uniqueness) ✓.
- `μ({0})=0` (Radon + `α>0`) ✓; `μ(B_r)=r^α V`, `V=μ(B_1)` ✓ (pure scaling, no isotropy).
- Resolvent integral (line 64): by layer cake on `a²+|ξ|²` I get exactly `∫μ(dξ)/(a²+|ξ|²) = αV a^{α−2} ∫₀^∞ u^{α−1}/(1+u²)du`, finite iff `0<α<2` ✓ (no density/isotropy assumed; only radial ball masses from scaling enter).
- `N1` finiteness reduces to `∫λ^{α0−1}(θ+λ)^{α−2}dλ`; conditions `α0>0` at 0 and `α+α0<2` at ∞ ✓ (line 70–71).
- `N2` absolute integrability: `|Ĝ_s(ξ)| ≤ min(s,|ξ|⁻¹)` ✓; low-frequency `st` bound ✓; high-frequency `∫_{|ξ|>1}|ξ|⁻² μ = αV/(2−α)` (layer cake) ✓; time singularity `v^{−α0}` integrable since `α0<1` ✓.
- `N2(θ)²≥0`: per-`ξ` time integral is a PSD quadratic form (Schur product of `e^{−θ(s+t)}` and the Laplace mixture of `e^{−λ|s−t|}`) ✓.
- `N0=θ⁻²` ✓ (`G_s(ℝ^d)=s`, `∫e^{−θs}s ds`).
- `N1(θ)=θ^{α+α0−2}N1(1)` ✓ (powers: `θ^{α0−1}·θ·θ^α·θ^{−2}`).
- `N2(θ)²=θ^{−β}N2(1)²`, `β=4−α−α0` ✓ (powers: `θ^{−2}·θ^{α0}·θ^{−2}·θ^α`).
- Tails `→0` ✓ (dominated by finite full-norm majorants; `K_M ≤ |r|^{−α0}` pointwise, `K_M→0` for `r≠0`).
- Smoothing/truncation non-increase: `N1` integrand nonnegative; `N2` Gaussian multiplier removable only after the (signed) time product is integrated to a nonnegative quantity per `ξ`; Laplace-domain restriction lowers the form ✓.

**PROOF005 — Lemma L:spatial-wick-measures (lines 157–317).**
- Laplace transform (E:spatial-positive-laplace): each Green chain factor `∏ₗ [(1+λₗ)²+|ηₗ(ξ)|²]⁻¹`, each edge factor `e^{−(ε_j+ε_h)|ξ_e|²/2} μ(dξ_e)`; `ηₗ` is the exact coefficient of `zₗ` in `Σ_e ξ_e·(x_j−x_h)`; integrand nonnegative; wave Laplace transform `∫e^{−as}Ĝ_s dξ=(a²+|ξ|²)⁻¹` ✓; Fubini justified by finite heat-weighted spectral mass and finite damped Green masses ✓. Transform monotonicity, not pointwise covariance monotonicity (line 193–194) ✓.
- Heat bound (E:construction-heat-bound): `(p_t*γ_b)(x) = ∫e^{iξ·x}e^{−(t+b)|ξ|²/2}μ(dξ)`, `≤ (p_t*γ_b)(0) = A(t+b)^{−α/2} ≤ At^{−α/2}`, `A=αV∫₀^∞u^{α−1}e^{−u²/2}du` ✓ (max-at-zero + layer cake). Uniform in `b` and in the arbitrary shift `x` ✓.
- Resolvent-to-Brownian identity `∫e^{−at}G_t(dx)dt = ½∫e^{−a²u/2}p_u(x)du dx`: both sides have Fourier transform `(a²+|ξ|²)⁻¹` ✓.
- Brownian moment bound (E:construction-brownian-moments, `j≥1`): independent check at `j=1` gives `ES_b(T) ≤ A∫∫|s−t|^{−α/2} = 2AT^{2−α/2}/((1−α/2)(2−α/2))`, which equals `(2!)[AΓ(1−α/2)]/Γ(3−α/2)·T^{2−α/2}` exactly ✓. General Dirichlet factor: the `2j` ordered times span `2j+1` nonnegative gaps summing to `T`; `j` distinct adjacent gaps carry exponent `−α/2`, giving `Γ(1−α/2)^j T^{(2−α/2)j}/Γ((2−α/2)j+1)`; `(2j)!` orderings ✓. Conditioning on the latest remaining vertex: partner mean `m` arbitrary, variance = last gap, `(p_h*γ_b)(m) ≤ Ah^{−α/2}` ✓; removing a pair preserves the Brownian marginal ✓; selected right endpoints distinct, selected gap ≥ adjacent gap, negative power direction handled correctly ✓.
- Mass bound: common-width transform bounds `L_{ε,D}(0)`; wave-heat gives `2^{−2k}`; horizon insertion `1 = ¼∬ e^{−((a−τ₁)+(b−τ₂))/2}` (empty chains give `τᵢ=0`, still 1) ✓; `e^{−Σu_l/2}` cancels against `e^{τ/2}` from the horizon weight; ordered→cube extension valid (nonnegative integrand, superset domain) and then factors per pair ✓.
- Per-pair occupation: spectral Cauchy–Schwarz gives `0 ≤ A₁₂ ≤ √(S₁S₂)` ✓; `v₁+v₂+w=k` gives `S₁^{v₁+w/2}S₂^{v₂+w/2} ≤ (1+S₁)^k(1+S₂)^k` ✓; independence gives `M_k(a)M_k(b)`; final `sup_ε L_{ε,D}(0) ≤ 2^{−2k−2}(∫e^{−a/2}M_k(a)da)² < ∞` ✓ (fixed `k`, polynomial `M_k`; no uniform-in-`k` claim).
- Weak limit: pushforward to `[0,1]^{2k}` by `yₗ=e^{−rₗ}`; bounded mass ⇒ tight; integer monomial moments = `L_D` values; polynomial density ⇒ unique cluster limit; `L_D(c,…,c)→L_D(0)` plus monotone convergence ⇒ zero mass on `y=0` faces (no mass escape to `r=∞`) ✓; Portmanteau tail control and pullback ✓; arbitrary relative width sequences ✓.
- Zero faces: `λₗ→∞` dominates by the integrable zero-parameter integrand and equals `ν_D{rₗ=0}` ✓.
- Homogeneity: `G_{cr}(c dz)=cG_r(dz)` (Fourier check) ✓ and `γ_b(cx)=c^{−α}γ_{b/c²}(x)` ✓; combined with the `2k` time Jacobians this gives `ρ_{ε,D}(cA)=c^{(4−α)k}ρ_{ε/c²,D}(A)` (exponent `2k+2k−αk`) ✓; passed to `ρ_D` via vague (compact-test) limits ✓.
- Horizon faces: positive compact `A⊂{ℓᵢ=T}` contradicts local finiteness via disjoint dilates over `c∈[1,2]` with common positive lower bound `ρ_D(A)>0` ✓; empty chain has no positive-level face ✓; boundary of the finite-horizon region lies in horizon + coordinate-zero faces; `e^{Σr}φ` is bounded on the bounded region and `ν_D`-a.e. continuous ⇒ (E:spatial-wick-limit) ✓.

**PROOF006 — Lemma L:joint-fixed-order (lines 319–414).**
- `F_{ε,δ,D}=∫∏γ⁰_{δ_j∨δ_h}(s_j−s_h)dρ_{ε,D}`; at common temporal width `η` the multiplier is bounded continuous ⇒ spatial limit exists at every `T₁,T₂` ✓.
- Finite temporary cutoff removal at positive spatial widths: bounded spatial covariances + Green mass horizon bounds + `|s−r|^{−α0}` integrable (`α0<1`) ✓.
- Telescope: `∏|s_e|^{−α0} − ∏γ⁰_η(s_e) = Σ_{l} [∏_{i<l}γ⁰_η·(|s_l|^{−α0}−γ⁰_η(s_l))·∏_{i>l}|s_i|^{−α0}]`, each difference `=K_{1/η}` and each term nonnegative ✓ (`|s_e|^{−α0}−γ⁰_η(s_e)=Γ(α0)⁻¹∫_{1/η}^∞e^{−λ|s_e|}λ^{α0−1}dλ`).
- Theorem 3.1 application (imported, lines 356–357): hypotheses verified — finite Gaussian-weighted spectral measures `e^{−(ε_j+ε_h)|ξ|²/2}μ(dξ)`, nonnegative physical covariance, nonnegative damped Green kernels (after `d=3` smoothing), Laplace intervals `[0,1/η]`, `[1/η,∞)`, `[0,∞)` as temporal domains, finite norms via Lemma L:damped-homogeneous-norms, two chains each with own root ✓. Cardinalities `#Q0=#Q1`, `#Q2` even, `#Q0+#Q2/2=k`; each Q1-pair once with factor 2, each Q2-pair twice ✓. Marked edge appears once in the first-norm product (`N1^{(1/η)}`) or twice (squared, `N2^{(1/η)}(1)²`) ✓.
- Explicit admissible constant (J09, derived here): `C_{k,T1,T2} = 4k·e^{T1+T2}·max{1, 2N1(1), N2(1)}^{2k}` (with `N0(1)=1`), so `0 ≤ F_{ε,0,D} − F_{ε,η,D} ≤ C_{k,T1,T2}(N1^{(1/η)}(1) + N2^{(1/η)}(1)²)`, uniform in spatial widths ✓. Contains full `N0(1)`, `N1(1)`, `N2(1)`, the marked tail (`N1` tail or `N2` tail²), the 2-factors, the `k`-sum (telescope), and `e^{T1+T2}`; no spurious square-root tail and no uniform-`k`/`T`/covariance claim.
- Bound survives removal of Laplace caps (positivity) and `d=3` Green smoothing (bounded continuous spatial covariances + weak Green convergence + integrable time majorant) ✓; RHS `→0` as `η↓0` ✓.
- Increasing `b_D(η)` and bracketing `F_{ε,η,D} ≤ F_{ε,δ,D} ≤ F_{ε,0,D}` when all `δ_j<η`: gives `liminf ≥ b_D(η)` and `limsup ≤ b_D(η)+σ(η)`, passing to `η↓0` yields the joint limit `b_D` at arbitrary relative rates ✓; empty/unequal chains ✓.
- `L²` identification: mixed moments via Wick with joint Gaussian regularizations (`ε-sum` spatial, `δ∨δ′` temporal); both diagonal and cross moments → same `Q_n=Σ_D b_D`; hence `‖Y_n^a − Y_n^b‖₂² → Q_n+Q_n−2Q_n = 0` ✓; completeness gives unique `X_n` independent of width ratios ✓. Both terminal chains reversed at the same horizon `t` (common reversal cancels the `T₁−T₂` offset; evenness handles the sign) ✓; Green-before-noise order preserved ✓; restricting to common noise widths reproduces the multiple Stratonovich integral of `g_n` ✓.

## J01–J12 determination

**J01–J12: FULLY_CHECKED**, with the following declared residual items (none is a proof gap): J02 positivity is correct but compressed (Schur product not spelled out); J08 the source (3.5) variable typo and the source Case 2 offset presentation are flagged separately (see below); J09 the explicit constant is verified to exist by my derivation but is not displayed in the manuscript; J07 the vague-limit Borel extension is implicit. All twelve checks otherwise verified by hand exactly as scoped. No check is NOT_FULLY_CHECKED and none FAIL.

**J08 split verdict (as required):** (a) *Source (3.5) verdict*: printed second Green variable is an internal typo; target reads it correctly as `y` and discloses it. (b) *Source Case 2 time-coordinate verdict*: the printed formula suppresses the retained offsets `s_{2n−1}−s_{n1−1}` and `x_{2n−1}−x_{n1−1}`; the repair is stationary-covariance Cauchy–Schwarz with shifted test functions (offset kernel is PSD; diagonal is shift-invariant), which the source states only as “shift-invariance.” Not repaired silently; disclosed as a source-presentation gap. (c) *Application verdict*: the target's use of Theorem 3.1 satisfies every printed hypothesis (finite Gaussian-weighted edge measures, nonnegative physical covariance, nonnegative damped kernels after `d=3` smoothing, finite norms, Laplace-interval temporal domains, independent chain roots, `#Q0=#Q1`, `#Q2` even) and does not reprove or silently correct the theorem.

## PROOF004–006 ledger

| Proof | Status | Checked steps / limits / constants | Residual gaps |
|---|---|---|---|
| PROOF004 `L:damped-homogeneous-norms` (611–671) | **FULLY_CHECKED** | `μ(cA)=c^αμ(A)`; `μ({0})=0`; `μ(B_r)=r^αV`; resolvent `=αV a^{α−2}∫u^{α−1}/(1+u²)du` (layer cake); `N0=θ⁻²`; `N1(θ)=θ^{α+α0−2}N1(1)`; `N2(θ)²=θ^{−β}N2(1)²`, `β=4−α−α0`; `N2²≥0`; tail norms `→0`; smoothing non-increase | none mathematical; positivity proof compressed (Schur product unstated) |
| PROOF005 `L:spatial-wick-measures` (730–872) | **FULLY_CHECKED** | Laplace formula; heat bound `A=αV∫u^{α−1}e^{−u²/2}`; Brownian moments (independent `j=1` check `=2AT^{2−α/2}/((1−α/2)(2−α/2))`; Dirichlet `2j+1` gaps); wave-heat `½`; `2^{−2k}`; horizon `¼`; `(1+S₁)^k(1+S₂)^k`; `2^{−2k−2}(∫e^{−a/2}M_k da)²`; homogeneity `c^{(4−α)k}`; zero/horizon faces | none mathematical; homogeneity Borel extension implicit |
| PROOF006 `L:joint-fixed-order` (885–969) | **FULLY_CHECKED** | telescope `k` × `K_{1/η}`; Theorem 3.1 hypotheses; explicit `C_{k,T1,T2}=4k e^{T1+T2}max{1,2N1(1),N2(1)}^{2k}` (derived); marked tail `N1^{(1/η)}` or `N2^{(1/η)}(1)²`; Cauchy bracket `b_D(η)`; `Q+Q−2Q=0`; common-horizon reversal | none mathematical; explicit constant not displayed in manuscript; “temporal caps” step terse |

## Required fixes before production gate

None blocking. Optional editorial improvements: (1) display the explicit admissible constant `C_{k,T1,T2}` instead of the abstract “constants may depend on …”; (2) spell out the Schur-product positivity and the temporal-cap/Green-smoothing removals; (3) add an explicit source-fidelity remark pinning the source (3.5) second-variable typo and the Case 2 offset/“shift-invariance” justification. These are presentation items, not proof repairs.

## One-line summary

PROOF004–006 are mathematically sound: every scalar, scaling law, resolvent and Laplace-limited identity, Brownian moment bound, mass bound, homogeneity exponent, face-vanishing argument, telescoping tail, and the Theorem 3.1 application verify correctly by hand, with only compressed exposition, an abstractly (not explicitly) stated `C_{k,T1,T2}`, and two disclosed source-presentation items remaining — PASS_WITH_NOTES, HIGH confidence.

**Scope/limitation note (honest):** this is a text-only, scoped audit of the exact excerpt; it does not certify raster/source-image coverage, the whole-manuscript argument, the full-source proof of the imported Theorem 3.1, or the final cold/image/source gates. Theorem 3.1 is imported (states as a cited pinpoint, not claimed as proved here); I verified its printed statement/hypotheses against the held pages 14–21 and the application, not a from-scratch re-proof of its full induction. PDF text extraction may garble mathematics; the two flagged source display items ((3.5) duplicated variable, Case 2 offsets) are exactly where extraction ambiguity and genuine presentation abbreviation cannot be cleanly separated without raster confirmation.