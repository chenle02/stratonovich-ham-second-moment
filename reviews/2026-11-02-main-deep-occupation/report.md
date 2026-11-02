# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I re-derived the internal logic, signs, boundary terms, scaling factors, and all final coefficients of PROOF135–141, and found no false identity, wrong exponent, sign error, or invalid asymptotics inside the seven audited proofs. In particular the fine coefficients that are easy to get wrong are correct:

- PROOF137: maximizing `L → L − C·L^q` with `q=4−α`, `k=q−1` gives the point `L^k = 1/(qC)` and value `(k/q)(qC)^{−1/k} = k(q^q C)^{−1/k}`; with `u=α/q`, `1+u=4/q`, this reduces exactly to `k[ R(g)α^{α/2}/(8 M_a q^{q/2}) ]^{1/k}` (the `q^q` versus `q^{q/2}` bookkeeping is correct via `k+α/2−1 = 2−α/2 = q/2`).
- PROOF139: the energy identity constant `((2−α)/2)α^{α/(2−α)}R_sp^{2/(2−α)}` is correct, and the substitution `R_sp α^{α/2} = (2E_sp/(2−α))^{(2−α)/2}` is correct.
- PROOF141: the scalar comparison constant `R_star^{2/(2−α)}·E_sp` is correct (same maximizer calculation, `T=(αR_starR_sp)^{2/(2−α)}`).
- Cross-checked the downstream white consumer (`E_sp = c²/6`, `F0 = √c/(3√2)`, bracket `(2/3)√(c/M_a) ≤ C₂ ≤ (2/3)√(cK₀)`) against PROOF139/140/137 formulas; it is consistent.

The honesty posture is also correct: the proofs explicitly refuse optimizers/attainment (`No optimizer is assumed`, `no attaining profile or equality... asserted`), keep Fatou as an inequality until continuity is re-established separately, and never claim `1_E ∈ H¹` (PROOF138 positivity uses only the nonnegative physical integral).

## Noncritical findings

1. **Large external dependency surface (not rederived here).** PROOF136–137–139 rest on lemmas outside the seven-proof set: the exact equilibrium potential `∫₀¹|s−t|^{−a}f_a(t)dt = 1` for every `s∈[0,1]`, the exact mass `M_a = Γ_E((1+a)/2)/(Γ_E(1+a)Γ_E((1−a)/2))`, the unmasked Rayleigh-rate proposition (boundedness/positivity of the mean and the real Rayleigh identity), the smooth nonincreasing cutoff `χ` from `P:variational-remove-mask`, and the finiteness/positivity of `S1^pos`. These are cited consistently and the packet contains their sources, but they are not part of the seven rederived proofs. Likewise the finiteness of `S1^pos` feeds on the independent `T:full-upper`; the non-circularity claim in OCC04 is genuine (finiteness of `R₀` is bootstrapped from the already-finite score, not from the rough spatial extension), but that bootstrap is off-scope here.

2. **PROOF135 relies implicitly on the extended-integral convention `0·∞ = 0`** in Tonelli (`ν{x∈N} = |N|·Γ(ℝ^d)` with possibly infinite total mass). Standard, but not spelled out; the same applies to the "every origin-centered ball has positive Γ-mass" step. In the degenerate white case `α=d=1` the homogeneity exponent is `0` (trivially positive mass on every ball containing 0); the proof's phrasing covers it but only via the nondegenerate scaling picture.

3. **`K_star(0)` convention.** The natural pointwise value of `K_star(u)` at `u=0` is `+∞` (the `λ^{a−1}` integral diverges); the definition sets `K_star(0)=0` for time integration. Harmless (diagonal is null), but it is a redefinition rather than the limiting value, and the row-max computation silently uses it only off the diagonal.

4. **Compressed positivity/Lipschitz step in PROOF136.** "a positive rate for every c>0" and the positive floor on compact `c`-intervals are delegated to `P:variational-unmasked-rate`, and the square-root Lipschitz transfer is stated in one sentence. Correct, but the positivity-for-every-`c>0` argument (dilate a bump where `U_z>0`) is not written out.

5. **Compressed PSD extension in PROOF138.** Positivity `0 ≤ B_Γ(f²,h²)` for full `H¹` is obtained by polarizing through the continuity of `(f,h)↦B_Γ(f²,h²)` on the span of finite combinations of `H¹` squares. Correct, but terse; a reader must supply the approximation `Σcᵢg_{i,n}² → Σcᵢgᵢ²` and the positivity limit.

6. **Compactified Bochner-measurability argument in PROOF141.** "Joint measurable spatial representatives exist" via separable-valued representative, simple `H¹`-valued approximation with summable `L²(0,1;H¹)` errors, a.e. subsequence limit, and reconciliation with PROOF135. Standard and correct, but the most delicate step is stated in two sentences.

## Checked derivations

- **PROOF135 (physical pair):** σ-finiteness of `dx⊗Γ(dy)`; representative independence at the positions `x` and `x−y`; Lebesgue-a.e. convergence transferred to `ν`-a.e. convergence via Tonelli + translation invariance + Borel null supersets. Signs/sharpness OK; support-agnostic, so plane/white/singular covariances are covered.
- **PROOF136 (static controls):** `λ_z(c)²` finite (`≤‖U_z‖_∞`) and Lipschitz in `c` with constant `‖U_z‖_∞`; positive floor on compact positive intervals; `f_n ↑ f_a`, `k_n ↑ 1`; mean `= k_n(s)U_z`, rate `= λ_z(k_n(s))`; `I_{Ψ_n}→λ_z(1)` by dominated convergence; cost `v_{Ψ_n}=B_Γ(z,z)∫f_n k_n → M_a B_Γ(z,z)`; positivity/finiteness of the spatial factor via autocorrelation near zero; `S1^pos ≥ λ_z(1) − (M_a/2)B_Γ(z,z)`.
- **PROOF137 (smooth ratio):** `b(g)>0` (Fourier-supported-at-zero argument); dilation `A_sp(U_ℓ g)=ℓ^α A`, `b(U_ℓ g)=ℓ²b` (`ℓ^{2d}·ℓ^{−d}·ℓ^{α−d}`); test profile `z=θ(U_ℓg)²` giving radicand `L²`; constant `C=M_a(1+u)²/(2R(g)u^{α/2})`; final coefficient (see Critical findings). Correct.
- **PROOF138 (four-linear):** `N(f)^4=‖f‖₂^{4−α}‖∇f‖₂^α`; homogeneous bound `A_sp ≤ R₀N⁴`; smooth-sign `B_Γ(Q,Q)=∫|Q̂_ord|²μ` in the `e^{+iξx}` model convention (no stray `2π`); symmetry; smooth square-CS; Fatou extension with `N`-continuity; sharp two-profile CS; four-linear bound `≤R₀ΠN(f_j)`; telescoping joint continuity; PSD on finite combinations; `R_sp=R₀`; strict positivity with the `1_E` correlation, explicitly *not* an `H¹` claim.
- **PROOF139 (energy map):** dilation reduction; `ℓ^{2−α}=αA/b`; maximum `((2−α)/2)α^{α/(2−α)}R(g)^{2/(2−α)}`; two-sup equality without optimizer; substitution into PROOF137; coefficient `M_a^{−1/k}F₀(E_sp)` and the scalar map `F₀`.
- **PROOF140 (kernel row):** `K_star ≤ |u|^{−a}` by dropping the quadratic damping; evenness, positivity, monotonicity, local integrability (`a<1`); `Φ` concave (decreasing integrand); row `= Φ(s)+Φ(1−s) ≤ 2Φ(1/2)` with equality at `s=1/2`; finiteness/positivity of `R_star`.
- **PROOF141 (occupation class):** measurability of pairings and representative independence; `∫₀¹‖g_s‖²_{H¹} = 1+T(g)`; Schur-type bound `B_Γ(g_s²,g_t²) ≤ R_sp F(s)F(t)` with `F=b^{α/4}`; concavity `∫F² ≤ T^{α/2}`; row+column bound giving `J ≤ R_star R_sp T^{α/2}`; scalar maximum `R_star^{2/(2−α)}E_sp`; positive lower bound via constant-in-time `U_ℓ`-dilation exploiting `α<2`; zero-covariance case with dilation, not a zero-gradient unit state.

## Required fixes before production gate

No mathematical corrections are required. Recommended (non-blocking) precision edits:

1. In PROOF135, state the extended Tonelli convention `0·∞=0` and note the degenerate `α=d=1` (white) homogeneity exponent-0 case explicitly in the "every origin-centered ball has positive mass" step.
2. In PROOF136, write out the one-line dilation argument establishing `λ_z(c)>0` for every `c>0` (currently delegated to the unmasked-rate proposition).
3. At `E:occupation-damped-kernel`, note that `K_star(0):=0` is a convention differing from the divergent pointwise limit.
4. (Optional, honesty) record at the point of use that the equilibrium-potential identity, `M_a`, and the finiteness of `S1^pos`/`T:full-upper` are external inputs to this subsection rather than results of PROOF135–141.

## One-line summary

All seven physical-occupation proofs (PROOF135–141) are correct in logic, signs, scaling, and final coefficients, with no proof gap found; the only qualifications are the (properly cited but here-unrederived) external finiteness/equilibrium inputs and a few compressed standard arguments.