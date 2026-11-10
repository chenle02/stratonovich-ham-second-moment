# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. Reconstructed every step of PROOF178–184 by hand from the embedded `notes/integrated_uniform_products.tex` excerpt; each identity `This proves Lemma/Proposition/Corollary \ref{...}` is present at the stated closing line and each declared constant rechecks. No false identity, hidden hypothesis, sign error, boundary-term loss, or invalid iterated-limit order was found. The single place where a naive entrywise estimate appears loose (the `|h S_t|/sqrt(h+c)| <= K e^{λt}` line in PROOF179's spectral matrix) is in fact correct: for `h=β = −μ² ∈ [−K²−,0)`, one recomputes `|h S_t|/sqrt(h+c) = μ sinh(tμ)/sqrt(2+K²−μ²) = [μ/sqrt(2+K²−μ²)]·sinh(tμ) ≤ K·e^{tμ} ≤ K e^{λt}`, exactly as claimed.

## Noncritical findings

- N1 (constant enlargement): PROOF182's spectral prefactor `L_{B,K} = log16 + 4log(1+K) + 3log(1+B)` is a rounding-up of the strict prefactor `8(1+K)²(1+B)`. Verified the round-up `8(1+K)²(1+B) ≤ 16(1+K)⁴(1+B)³` holds; harmless (explicitly described as "sufficient prefactor, by enlarging").
- N2 (the `C_B` round-up): `C_B ≤ 18B^{3−1/r} ≤ 32B^{3−1/r}` and `C_B B^{1/r} ≥ B`. Both verified from `C_B = G_B²[B^{1−1/r}+B^{1−1/r−θ}]`, `1≤G_B≤3B`, `θ<1<r`. The `32` is a convenience, not a load-bearing optimum.
- N3 (two primitive constants): the little-Hölder primitive constants `C_B`/`c_B` are structurally standard (I re-derived the `‖H_m‖_θ ≤ C_B δ^{-1/r}‖W‖_{L^r(I_m)}` bound from the S_E conjugate sandwich and the affine time pullback). They enter only as finite constants that vanish or stay finite in the stated iterated limits.
- N4 (cross-section reliance): PROOF178–184 consume conclusions of earlier embedded sections (signed-static wave identification, uniform-mean regulator/tensor bound, cameron compact time map `C_t`, symplectic block baseline, Young multiplicative bound). I checked each consumed statement against its embedded source text and its role in the target proofs; I did not re-derive those earlier sections in full, as they are outside the seven-proof assignment.
- N5 (notation): `T_R`, `T`, `M`, `K`, `C_B` are locally overloaded across files; no mathematical ambiguity materializes.

## Checked derivations

**PROOF178 — L:uniform-E-lift (lines 53–81) — CHECKED.**
- `L∈V_{E,R}` has form `(u,v) ↦ (0,Mu)` with `‖L‖ = ‖M‖_{H^{1/2}→H^{-1/2}} =: k`; closed block form makes the two norms coincide.
- Potential extraction: with `χ_R = 1` near `supp m_R`, `M_n χ_R = V_n`; `‖V_n−V_j‖_{H^{-1/2}} ≤ ‖χ_R‖_{H^{1/2}}‖M_n−M_j‖` gives Cauchy and a unique `V∈H^{-1/2}` with support in `supp m_R`; `M χ_R = V` forces uniqueness.
- Pairing bound `|v_V(u,w)| ≤ k‖u‖_{H^{1/2}}‖w‖_{H^{1/2}}` follows from `‖V‖_{H^{-1/2}}=‖M‖=k`; symmetry from `⟨Vu,w⟩` on real states, Hermitian extension by real/imaginary splitting.
- Lift `L_F(u,v,c₁,c₂)=(0, Mu+c₁V, 0,0)`; `L_F i = iL` verified termwise; difference bound `(1+‖χ_R‖_{H^{1/2}})‖M_n−M_j‖` explicitly R-dependent and marked "enters no uniform estimate". Complexification preserves the E-operators norm (real/imaginary norm splitting). `V=0` and `L=0` on zero covariance. Pass.

**PROOF179 — P:uniform-E-spectral (lines 104–243) — CHECKED.**
- Form budget: `‖u‖²_{H^{1/2}} ≤ bz` (Fourier CS); `|v_V(u,u)| ≤ Kbz ≤ z²/2+K²b²/2` (AM-GM with weights ½,½). Then `½z²+(1+K²/2)b² ≤ q_V+cb² ≤ 3(1+K²)z²` with `c=2+K²`; lower dominates `2b²`, hence `A=H_V+c ≥ 2`; closed semibounded form on full `H¹` with equivalent shifted norm.
- Teschl imports at the exact embedded pinpoints: Theorem 2.14 (p.81, (2.63)) for the unique self-adjoint representative; Theorem 3.6 (p.109, (3.51)–(3.53)) for form domain/spectral representation; Theorems 3.1–3.2 (pp.102–104, (3.18)–(3.33)) for the C\*-calculus and strong (dominated) continuity used in the wave.
- Quarter-power domains: `½B₀ ≤ A ≤ L_K B₀` (`L_K=3(1+K²)`) by resolvent/completion-of-squares order `T≤S ⇒ (T+t)^{-1} ≥ (S+t)^{-1}` plus `x^{1/2}= (1/π)∫t^{-1/2}x/(x+t)dt`, giving `D(A^{1/2})=H¹`, `D(A^{1/4})=H^{1/2}`, `2^{-1/4}‖u‖_{H^{1/2}} ≤ ‖A^{1/4}u‖ ≤ L_K^{1/4}‖u‖_{H^{1/2}}`, and `H^{-1/2}` dual completion. Condition cost `M_K² = L_K^{1/2} = sqrt(3(1+K²)) ≤ 2(1+K)`.
- Bottom: `−K² ≤ β ≤ 0` (unit data + off-support dilated compact bump), `β = inf spec H_V` via bounded spectral slices and the closed-PVM support `Σ` being exactly the spectrum; `λ ≤ K`.
- E_A wave matrix with `Cos/Sin` (hyperbolic for `h<0`); each entry `≤ 2(1+K)(1+t)e^{λt}` (upper-right `sqrt(c)|Sin| ≤ √c·t e^{λt} ≤ 2K t e^{λt}`; lower-left `|h Sin|/sqrt(h+c) ≤ K e^{λt}` as re-derived above), matrix norm `≤ 2×` entry bound, `×` condition cost gives exactly `8(1+K)²(1+t)e^{λt}`.
- Identification with the actual physical wave through the fixed-R lift (PROOF178) and P:signed-physical-wave; the lift's (R-dependent) F-bound is used for identification only and no lift constant enters the budgets — the required "no lift-budget transfer".
- Rate continuity: ε-minimizer `u` with `q_W ≤ 1` forces `z ≤ K+2`; `|v_V−v_W|(u,u) ≤ ‖L_V−L_W‖‖u‖²_{H^{1/2}} ≤ (K+2)‖L_V−L_W‖`; square-root inequality on `−β ≥ 0`.
- Zero covariance: `{0}`, `H_V=−Δ`, `β=λ=0`, free wave. Pass.

**PROOF180 — P:uniform-rate-averaging (lines 269–314) — CHECKED.**
- `ω_δ = ‖(A_δ−I)C_t‖_{H_t→L^r} → 0`: `C_t` compact into `L^r` (`2<r<2/a`), hence unit-ball image compact; `‖A_δ−I‖≤2` pointwise + uniform convergence on compact subsets = uniform convergence on the closure. Bochner cell averaging is an `L^r` contraction (Jensen).
- Typed commutation `A_δ^{K(E)} T_R(C_t⊗I)Φ = T_R((A_δ C_t)⊗I)Φ` on finite tensors, extended via the dimension-free Hilbert tensor bound (L:uniform-mean-tensor) and `‖T_R‖ ≤ M_0`, giving `‖W̄−W‖_{L^r} ≤ M_0 ω_δ ‖Φ‖_{H_I} ≤ Ω_δ(M)`.
- Integrated rate error: `|λ(φ)−λ(ψ)| ≤ sqrt{(K(s)+2)‖φ−ψ‖}` pointwise; Cauchy–Schwarz gives `∫|Δλ| ≤ sqrt{3+‖φ‖_{L¹}+‖ψ‖_{L¹}} sqrt{‖φ−ψ‖_{L¹}} ≤ sqrt{3+2Z} sqrt{Ω_δ(M)}` (using `K(s) ≤ 1+‖φ‖+‖ψ‖`, `L¹ ≤ L^r` on `|I|=1`, and `‖W_R‖_{L^r},‖W̄‖_{L^r} ≤ Z=C_mean M`).
- Rate finite, nonnegative, continuous; `λ(L) ≤ max(1,‖L‖)` gives `Rate ≤ 1+C_mean‖Φ‖`. No tensor compactness or global spatial compact-family shortcut invoked. Pass.

**PROOF181 — L:uniform-product-budgets (lines 346–388) — CHECKED.**
- `G_B`: balanced Fourier matrix upper entry `≤√2 B`, lower and diagonals `≤1`; Frobenius `≤ sqrt{3+2B²} ≤ 3B`; `G_B≥1` from `S_E(0)=I`. `C_B = G_B²[B^{1−1/r}+B^{1−1/r−θ}]`; `C_B B^{1/r} ≥ B` and `C_B ≤ 18B^{3−1/r} ≤ 32B^{3−1/r}` follow directly.
- Primitive `‖H_m‖_θ ≤ a_m = C_B δ^{-1/r}‖W_R‖_{L^r(I_m)}` (conjugate sandwich, affine pullback `dv=dw/δ`, Hölder exponent `1−1/r>θ`, constant stopping preserves the seminorm); `δΣa_m^r ≤ C_B^r‖W_R‖^r_{L^r}` by the true partition.
- Young growth `log‖S_E(ℓ)U_D(ℓ,0)‖ ≤ C_gr B(1+‖D‖_θ^ν)` with explicit `C_gr`; generic algebra on `L(E)` with multiplication of norm one.
- `‖P_m^mean‖ ≥ 1` from P:symplectic-block-mean (the block direction `δ^{-a/2}T^*_{δ,m}i_IΦ` is finite at fixed `δ`, no fast-direction cost). Empty endpoint = identity. Pass.

**PROOF182 — P:uniform-mean-product (lines 414–475) — CHECKED.**
- `e_m = C_Bδ^{-1/r}‖W−W̄‖_{L^r(I_m)}`; Jensen/primitive give `‖H̄_m‖_θ ≤ a_m`, `‖H_m−H̄_m‖_θ ≤ e_m`; `δΣe_m^r ≤ C_B^rΩ_δ(M)^r`; finite power means give `δΣ(e_m+e_m^ν) ≤ E_δ = (2/B)^{1−1/r}C_BΩ_δ + (2/B)^{1−ν/r}C_B^νΩ_δ^ν` (checked both exponents, `δn≤2/B`, and `p/ν≥1`, `r/ν>1`).
- Full cell: `‖M̄_m‖ ≤ (δB)^{-1/r}‖W‖_{L^r(I_m)} = a_m/(C_BB^{1/r}) ≤ a_m/B` (uses `C_BB^{1/r}≥B`).
- Good blocks (`a_m≤K`): multiplicative Young with base `H̄_m`, perturbation `H_m−H̄_m`, left factor `S_E(B)`; base static wave of `M̄_m` (PROOF179) with norm `≤ K/B ≤ K`; `log‖P_m^mean‖ ≤ L_{B,K} + Bλ(M̄_m) + C(θ,B,K)(e_m+e_m^ν)`.
- Good-cell λ sum: `δΣ_good Bλ(M̄) ≤ ∫λ(W̄) ≤ Rate + Λ_δ` (nonnegativity of λ; dropped rate cells can only lower the left side). Prefactors sum to `≤ L_{B,K}/B` (`δN ≤ 1/B`).
- Bad cells: `1+a_m^ν ≤ (K^{-r}+K^{ν-r})a_m^r`, `δΣa_m^r ≤ C_B^rZ^r`; `C_B ≤ 32B^{3−1/r}` yields `C_gr 32^r Z^r B^{3r}(K^{-r}+K^{ν-r})`.
- Last cell: stopped path, `a_N ≤ C_Bδ^{-1/r}Z`, `C_gr B[δ + C_B^νZ^νδ^{1−ν/r}]` (no division by `ℓ_N`; `ν<r`). All three error terms vanish at fixed `B,K,M`. Pass.

**PROOF183 — C:uniform-polynomial-balls (lines 490–516) — CHECKED.**
- `K_B = B^s` with `s > r(3+κ_ball)/(r−ν)`. Bad exponents `r(3+κ_ball)−sr < 0` (as `s>3+κ_ball`) and `r(3+κ_ball)+s(ν−r) < 0` (the chosen `s`), both strict. `L_{B,K_B}/B ≤ [log16+7log2+(4s+3)logB]/B → 0`.
- Iterated order explicit and correct: `δ↓0` first at fixed `B,K_B,M_B` (only the three vanishing errors move), then integer `B→∞`; no diagonal `B_δ, M_δ`; `M_B = c_ballB^{κ_ball}`.
- `sup` legitimacy: deterministic controls in a separable Hilbert ball; Young local dependence + positive endpoint norms give continuity; a countable dense subset carries the sup; `sup_{R≥1}` is an ordinary real supremum (no random compactness, no uncountable measurability claim). Pass.

**PROOF184 — P:uniform-arbitrary-residual (lines 556–607) — CHECKED.**
- Endpoint norms positive (Young and free inverses); `z_rat = ∏‖P_m^pert‖/‖P_m^mean‖`.
- Good cells (`a_m≤K_res`): multiplicative Young with base `H_m`, perturbation `x_m`, left multiplier `S_E(ℓ_m)` gives `log ratio ≤ C(θ,B,K_res)(v_m+v_m^ν)`.
- Bad cells (`a_m>K_res`): refined growth + `(a_m+v_m)^ν ≤ 2^{ν−1}(a_m^ν+v_m^ν)` + mean endpoint denominator `≥1` gives `log ratio ≤ c_B(1+a_m^ν+v_m^ν)` (`c_B=2^{ν−1}C_grB`, independent of `K_res,R,δ,Φ,M`).
- Summing, reusing `1,a_m^ν ≤ a_m^r(K_res^{-r},K_res^{ν-r})` and `δΣa_m^r ≤ D_M = C_B^r(C_meanM)^r`: `δlog max(1,z_rat) ≤ C_{K_res}[(2/B)^{1−1/p}Y+(2/B)^{1−ν/p}Y^ν] + c_BD_M(K_res^{-r}+K_res^{ν-r})` (power means checked, including `p=ν`, zero inputs, empty block; no singular powers).
- Ordered noncommuting product: submultiplicativity and `A_prod = ∏‖P_m^mean‖ ≥ 1` give `max(1,‖P_N^pert⋯P_0^pert‖) ≤ A_prod·max(1,z_rat)`, hence `F − 2δΣlog‖P_m^mean‖ ≤ 2δ log max(1,z_rat)`.
- Limit order: `δ↓0` at fixed `B,M_B,K_res` (residual term `→0` under `Y≤b_δ`), then `K_res→∞` at fixed `B,M_B` (`c_BD_{M_B}(K_res^{-r}+K_res^{ν-r})→0` since `r>ν`), then the mean term via PROOF183 and `B→∞`. Fully deterministic; no Gaussian/Cameron/Hamiltonian condition; no scalar-displacement-moment multiplication. Pass.

## Required fixes before production gate

None mandatory. Optionally: (i) in PROOF179 spell out the `μ sinh(tμ)/√(c−μ²) ≤ K e^{tμ}` factorization for the lower-left entry, since the stated one-line bound is correct but non-obvious; (ii) in PROOF182 state once that `C(θ,B,K)` absorbs `c_B` and the good-cell multiplicative constant. Neither affects validity.

## One-line summary

All seven uniform E-phase spectral/averaging/product/residual proofs reconstruct cleanly with exact constants, correct fixed-R identification without lift-budget leakage, and correct `δ→0` first, `K_res/B` after, integer-`B` last iterated order — PASS, HIGH confidence.

---

## Uniform requirements checks (UPR01–UPR10)

**UPR01 — PASS.** PROOF178 (L:uniform-E-lift): closed E class and `‖L‖=‖M‖`; potential uniqueness/support via `Mχ_R=V`; actual `H^{1/2}→H^{-1/2}` pairing and symmetry; full-F lift `(0,Mu+c₁V,0,0)` with `L_F i = iL` and R-dependent difference bound used only for identification; completed mean fields a.e. closed class + Bochner-average closure; complexification preserves the E norm and the Hermitian pairing. Fully covered.

**UPR02 — PASS.** PROOF179 (P:uniform-E-spectral): exact budget `c=2+K²`, `A≥2`, full `H¹` domain; Teschl 2.14/3.6/3.1–3.2 at the embedded correct hypothsames/pages; resolvent/square-root form order and quarter domains/negative completion; `E_A` condition cost `sqrt{3(1+K²)}≤2(1+K)`; `β≥−K²`, `β≤0` via dilated off-support trial; real/complex infimum; closed-PVM spectrum; `8(1+K)²(1+t)e^{λt}`; physical-wave identification via fixed-R lift with no lift-budget transfer; compact-interaction primitive and Young identity; continuity via ε-minimizer `z≤K+2`; `|Δβ|≤(K+2)‖ΔL‖`, `|Δλ|≤sqrt{(K+2)‖ΔL‖}`; zero-covariance case.

**UPR03 — PASS.** PROOF180 (P:uniform-rate-averaging): true slow partition and empty-cell handling; Bochner averaging contraction/density; `ω_δ→0` uniform on the compact `C_t` image; typed tensor commutation via the dimension-free bound and `‖T_R‖≤M_0`; uniform-R field errors; `sqrt{3+2Z}sqrt{Ω_δ(M)}`; finite/continuous rate; explicitly no tensor compactness or global spatial compact-family shortcut.

**UPR04 — PASS.** PROOF181 (L:uniform-product-budgets): `G_B ≤ sqrt{3+2B²} ≤ 3B`, `C_B ≤ 18B^{3−1/r} ≤ 32B^{3−1/r}`, `C_BB^{1/r}≥B`; `L^r` primitive exponent `1−1/r>θ`; explicit `C_grB(1+d^ν)` Young growth; completed-mean endpoint `‖P_m^mean‖≥1` via the symplectic block direction `δ^{-a/2}` with no uniform-direction cost; empty/zero cells.

**UPR05 — PASS.** PROOF182 (P:uniform-mean-product): own Bochner cell average, `a_m/e_m` budgets; good full cells `a_m≤K` with base norm `K/B≤K`, left factor `S_E(B)`; prefactor `L_{B,K}`; `δN≤1/B` vs all-cells `δn≤2/B`; nonnegative dropped rate cells; bad-tail `K` powers and `B^{3r}` count; last stopped-path bound `C_grB[δ+C_B^νZ^νδ^{1−ν/r}]` without dividing the short cell; fixed-parameter errors vanish uniformly in R.

**UPR06 — PASS.** PROOF183 (C:uniform-polynomial-balls): `M_B=c_ballB^{κ_ball}`, `K_B=B^s` with `s>r(3+κ_ball)/(r−ν)`; both bad exponents strictly negative; `L_{B,K_B}/B→0`; `δ` first at fixed `B/K_B/M_B`, then integer `B`; no diagonal choice; deterministic control-ball finiteness/continuity/countable-dense realization and ordinary `sup_R` (no random compactness).

**UPR07 — PASS.** PROOF184 (P:uniform-arbitrary-residual): arbitrary little-Hölder zero-start paths; good-cell exact multiplicative ratio; bad-cell mean denominator `≥1` (no perturbed-Hamiltonian assertion); `c_B=2^{ν−1}C_grB`; finite power means including `p=ν`, zeros, empty cell; `max(1,z_rat)`; ordered noncommuting submultiplicativity with `A_prod≥1`; `δ→0`, then `K_res→∞` at fixed `B/M`, then `M_B` and `B→∞`; deterministic `b_δ→0`; no scalar-displacement-moment multiplication or Gaussian inference.

**UPR08 — PASS.** Input-use ledger (delivered/read/consumed): *consumed and re-checked* — `integrated_signed_static.tex` (limiting multiplier, closed form, spectral wave/matrix, physical-wave identification), `integrated_uniform_mean.tex` (uniform cutoff `M_0`, `T_R`, tensor lemma, `C_mean=M_0‖C_t‖`), `integrated_cameron_mean.tex` (compact `C_t`, full F-mean and rank-zero covariance identity), `integrated_symplectic_phase.tex` (block-mean endpoint `≥1`), `integrated_young_upper_foundation.tex` (refined growth, multiplicative perturbation), `teschl-2014.txt` (2.14/3.1/3.2/3.6 with `(2.63)`,`(3.18)–(3.33)`,`(3.51)–(3.53)`), `friz-hairer.txt` (Young `(4.1)–(4.3)`, Sections 1.4–1.5/4.1; Borell 11.6 read but used in `integrated_gaussian_tubes.tex`, not in the seven proofs). *delivered, referenced, not re-derived* — `integrated_wave_variance.tex`, `integrated_actual_operator_driver.tex`, `integrated_source_convergence.tex`, `integrated_compact_gaussian.tex`, `integrated_gaussian_tubes.tex`, `integrated_radius_anchor.tex` (their stated conclusions are the seven proofs' inputs; internal derivation is outside the assigned seven-proof unit). *delivered, not consumed* — `integrated_covariance_foundation.tex`, `integrated_masked_moments.tex`, `integrated_constant_phase_young.tex` (conclusions via the intervening sections), `integrated_compact_mean_family.tex`, `integrated_exact_scaling.tex`, `integrated_raw_block_lower.tex`, `integrated_unmasked_variational.tex`, `integrated_temporal_equilibrium.tex`, `integrated_spatial_occupation.tex`, `integrated_point_transfer.tex`, `integrated_signed_moment_upper.tex`, `integrated_positive_gram.tex`, `integrated_intrinsic_constant.tex`, `integrated_occupation_ceiling.tex`, `integrated_white_evaluation.tex`, `chen-author.txt`, `crouzeix-v1.txt`. No F-norm leakage, no prior-vote or identity row import, no source correction, no unverified probabilistic conclusion consumed.

**UPR09 — PASS.** All manual controls hold: signed (not just positive) potential in the form bound; `β≤0` bottom including `β=0` (no eigenvalue asserted); non-eigen bottom; `N=1`, empty/short last cell; `p=ν` and `Y=0`, `M=0`; noncommuting product and non-Hamiltonian residual (only submultiplicativity + generic Young); polynomial `M_B` with valid `s`; fixed-R lift constants never in uniform budgets; all limit orders verified. No control blocks its claim.

**UPR10 — PASS.** Seven proofs reconstructed with every hypothesis territory and unverified step made explicit; original models and E-only quantitative budgets preserved; source/phase/constant interfaces not overextended (identification vs. bound, no lift-norm or `χ_R`-constant transfer); no concentration/independence/point-transfer/moment-asymptotic credit inside the seven proofs; full-213/source-image/cold/whole-paper credit withheld; no new formalization or kernel evidence assumed.