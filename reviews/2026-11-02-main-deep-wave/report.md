# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. No proof gap, false identity, sign error, hidden hypothesis, or invalid constant was found in the nine assigned proofs PROOF066–074. I did not read `packet.md`, any `Progress.md`/`Review.md`/reviews directory, and no external theorem or source outside the embedded excerpts was used; all checks below are direct hand calculations on the supplied text.

## Noncritical findings

1. **PROOF067 is loose by a factor of 2.** Expanding `P_r Q_ρ` into four modes with coefficients of magnitude `1/4` and applying `(Σ|c_j|)Σ|c_j|‖v_j‖²` gives exactly one half of the asserted right side, as the text itself notes ("This gives one half of the asserted right side, and hence the bound."). The stated bound is valid, just non-sharp.

2. **PROOF066 low-frequency constant sufficiency is compressed.** The step `2/(1−a) ≤ 16/(1−a)⟨ωh⟩^{a−1}` relies on `⟨ωh⟩^{a−1} ≥ 2^{(a−1)/2} ≥ 2^{−1/2} > 1/8` for `|ωh| ≤ 1`. It is correct but should be spelled out.

3. **`L:masked-time-completion` Schur constant is loose.** The row integral `∫_0^T |t−s|^{−a} ds` is actually `≤ 2^a T^{1−a}/(1−a)`; the manuscript uses `2T^{1−a}/(1−a)`, which is valid since `2^a < 2` but not sharp. No correctness impact.

4. **PROOF069 near-region inequality is correct but terse.** `⟨ξ⟩^{−ε} ≤ q^{−ε}` (line 853) holds because `q = max(1,|ξ|)` satisfies `⟨ξ⟩² = 1+|ξ|² ≥ q²`. This is a two-line check not stated.

5. **PROOF069 far-region wording is inverted.** "Each oscillatory bracket is at least `⟨hr⟩/2`" gives a lower bound on the argument; raising to `a−1 < 0` then yields the needed upper bound `⟨h(·)⟩^{a−1} ≤ 2^{1−a}⟨hr⟩^{a−1}` and `Q_h ≤ 2^{2−a}⟨hr⟩^{a−1}`. The conclusion is right; the phrasing could mislead a reader.

## Checked derivations

All WAVE01–WAVE09 below were reconstructed by hand; each is **PASS** with **CHECKED** coverage. Falsification probes attempted and their conclusions: ω=0 (reduces to the `|ωh|≤1` branch); resonant r=ρ (gives `Q_h = 1 + ⟨2hr⟩^{a−1}`); h=1 (all `B_α(1)=1`); h→0 (α=1 log absorbed via `e^{−εu}(1+u) ≤ 1+1/(eε)`); d1 white noise (α=d=1, `B_α = 1+log(1/h)`); zero covariance (all bounds trivial via `C=0 ⇒ ν=0` in PROOF069 and line 973–974/1327–1329); anisotropic hyperplane measure (used only in the quotient-obstruction proposition, not in the nine; the nine retain only evenness, never a density). None of these falsify any bound.

- **WAVE01 — PROOF066 — PASS / CHECKED.** Moving-endpoint `c(v)` and `c'(v) = −A(s+h)Ā(s+h−v) + ∫A'(u+v)Ā(u)du`; `c(h)=0`, `|c|≤hM²`, `|c'|≤M²+hMD`; square split into two conjugate triangles giving `2 Re ∫_0^h v^{−a}e^{iωv}c(v)dv`; rescaling `y=v/h`, `f=c(hy)/h`, giving `2h^{2−a}Re∫_0^1 y^{−a}e^{iωhy}f(y)dy`; `|f|,|f'| ≤ K²`, `f(1)=0`; low-frequency bound `K²/(1−a)`; high-frequency IBP with endpoint `K²k^{a−1}` and derivative integral `≤ K²k^{a−1}(1+1/(1−a))`, summed to `4K²k^{a−1}/(1−a)`; `k^{a−1} ≤ √2⟨ωh⟩^{a−1}` checked via `a−1∈(−1,0)`; `8√2 ≤ 16` gives `16/(1−a)`. Signs and `a∈(0,1)` window are correct.

- **WAVE02 — PROOF067 — PASS / CHECKED.** Four complex modes with frequencies `σr+τρ` (σ,τ∈{±1}), coefficients of magnitude `1/4`; two modes have `|r−ρ|`, two have `r+ρ`; weighted Cauchy–Schwarz `‖Σc_jv_j‖² ≤ (Σ|c_j|)Σ|c_j|‖v_j‖²` with `Σ|c_j|=1`; no orthogonality or independence used; repeated/zero frequencies permitted.

- **WAVE03 — PROOF068 — PASS / CHECKED.** For `r≥1`, `b_r = (⟨r⟩/r)sin(rt)` with coefficient `≤√2`; for `0≤r≤1`, `b_r = t⟨r⟩∫_0^1 cos(vrt)dv`, containing `r=0`; product is a coefficient `≤2` times a (0/1/2-copy) normalized average of `t^j P_{r'}Q_{ρ'}`; continuity in `L²(0,T)` and `H_a` makes the averages genuine Bochner integrals; Hilbert Jensen bounds the squared norm; `A=t^j` gives `M+hD ≤ 1, T+1, T²+2T`, each `≤(1+T)²`, so `(M+hD)² ≤ (1+T)^4`; frequency-shift comparison `⟨x+e⟩ ≥ ⟨x⟩/(1+|e|)` with `|e|≤2` gives `3^{1−a}` per bracket; scalar-square `4` yields `C_1 = 4·3^{1−a}C_0`.

- **WAVE04 — PROOF069 — PASS / CHECKED.** `C=0 ⇒ ν=0` via countable ball covering; pushforward `ν_ξ` with `ν_ξ(B(0,R)) ≤ CR^α`; dyadic `A_ξ(q) ≤ C(1+2^αΣ2^{j(α−1)})` and the three regimes `1, 1+log q, q^{α−1}`; near region `|λ|≤4q ⇒ |η|≤5q`, `Q_h ≤ 2`, `2⟨ξ⟩^{−ε}A_ξ(q) ≤ 2q^{−ε}A_ξ(q)`; α>1 exponent `α+2γ−2 < 0` by `γ<(2−α)/2`; far region lower bounds `|η|≥3r/4`, `||η|−|ξ||≥r/2`, `|η|+|ξ|≥r/2`; dyadic split at `L=⌊log₂(1/h)⌋`; tail `h^{1−α}/(1−2^{α+a−2})` using `α+a−2<0`; finite sums match `B_α(h)` in all regimes; constants dimension-free.

- **WAVE05 — PROOF070 — PASS / CHECKED.** Both upper endpoints `1−a/2` and `(3−a−α)/2` exceed `1/2` (by `a<1` and `α+a<2`); α<1 uses `2−a>2β`; α>1 uses `3−a−α>2β`; α=1 absorbs the logarithm with `δ=2−a−2β>0`; the minimum correctly selects the right regime; no endpoint β used.

- **WAVE06 — PROOF071 — PASS / CHECKED.** Wave multipliers smooth at zero via the continuous sine quotient; compact-support raw admission `|K|Γ(K−K)‖F‖_∞‖H‖_∞`; Fourier decay `ε_n⟨ξ⟩^{−N}` chosen so the square weight is integrable against both tempered μ and ν_R; actual-vs-auxiliary limit identity for masked products; Hermitian symmetry `A(−ξ)=Ā(ξ)` cancels the imaginary mixed term, extending `P:masked-noise-completion` to `W_ℂ`; `S(−t)(0,f) = (−sin(t|D|)f/|D|, cos(t|D|)f)`; physical adjoint `⟨S(−t)B(b)S(t)z,w⟩_E = ∫b v_z Ḡ_w dx` checked with `G_w = −sin(t|D|)/|D| Λw₁ + cos(t|D|)Λ^{−1}w₂`; `D_χ^{∗,E} = (Λ^{−1}χΛ, ΛχΛ^{−1})` checked in each Sobolev slot; normalized `2×2` kernel reproduced from `v̂_z` and `Ĝ_w`; zero-frequency matrix `[[−t,−t²],[1,t]]` correct; conjugate-product Fourier sign and `(2π)^d c_d² = 1` leave no residual Fourier factor. The R-dependent admission is correctly kept separate from uniform variance bounds.

- **WAVE07 — PROOF072 — PASS / CHECKED.** Scalar finite Bessel on each H-coefficient; conjugated family handled by replacing `{u_k}` with `{conj u_k}` (still orthonormal); Parseval in H plus nonnegative Tonelli; Bochner integrability by `L²` Cauchy–Schwarz; finite/zero dimensional H immediate; no independence.

- **WAVE08 — PROOF073 — PASS / CHECKED.** Kernel time bound `‖1_I K_ij‖² ≤ A_T h^{2−a}Φ_h(ξ,η)` with `A_T = C_1(1+T)^4`; actual `ν_R` growth bound makes `P:frequency-row` apply, giving `∫Φ_h(ξ,ξ−λ)ν_R ≤ K C_ν B_α(h)⟨ξ⟩^{−2γ}`; **input direction**: `g_j^λ = Σ_i 1_I K_ij V̄_i`, Bessel (unconjugated), Cauchy–Schwarz over two components gives factor `4A_T h^{2−a}Φ_hΣ|V_i|²`, change `ξ=η+λ`, Tonelli, row bound; **output direction**: `η=ξ−λ`, `f_i^λ = Σ_j 1_I K_ij U_j`, conjugated Bessel, `4A_T h^{2−a}∫Φ_h(ξ,ξ−λ)Σ|U_j(ξ−λ)|²`, change `η=ξ−λ`, reflect λ by evenness of ν_R, symmetry of `Φ_h` recovers the same row; `‖z‖_{E_{s−γ}} = ‖⟨ξ⟩^{−γ}Jz‖₂` verified slot-by-slot; constant `4A_T K C_ν` for both directions; strict β replacement via `C:frequency-time`; uniform in R, I, family size.

- **WAVE09 — PROOF074 — PASS / CHECKED.** Countable real Schwartz ONB via Fourier cutoff + symmetrization `(g(ξ)+ḡ(−ξ))/2` and Gram–Schmidt; finite Gaussian sums; orthogonal expected-square tails sum to the variance sums; `L²(Ω;E_s)` limits without coefficient independence; singleton forms of both variance directions identify the two dual pairings; basis independence by Parseval; finite-family Gaussianity by characteristic-function convergence.

- **WAVE10 — PASS (applications; context read, not re-derived in full).** `driver` preserves `γ∈(0,min(1/2,(2−α)/2))` and `1/2<θ<β<min(1−a/2,(3−a−α)/2)`, matching PROOF069/070/073; `L:driver-actual-variances` uses **both** variance directions (`V_out`, `V_in ≤ b_I D_γ²`) with `b_I = C_T h^{2−a}B_α(h)`; `source-consumer` uses the same fixed `R,T,ζ_R,E` and parameters and only compares through the bounded variance `VarY(F) ≤ C‖F‖_{H_W}²`; no filter is commuted through the mask ζ_R or the wave group. A few downstream lemmas (fixed Schatten envelopes, source pointfield regularity) lie outside the nine assigned proofs and are reported as not re-derived here; I found no contradiction with the parameter windows or mask/phases/norms used.

- **WAVE11 — PASS.** The nine proofs are internally non-circular (066→067→068→069→070→073→074, with 071/072 independent); zero covariance is handled explicitly; no density/isotropy or covariance-monotonicity substitution occurs (only evenness of μ and ν_R is used, consistently with PROOF069 needing it only in one reflect step); no whole-213-proof/image/cold/goal acceptance is asserted anywhere in the excerpt.

## Required fixes before production gate

None blocking. Optional clarity improvements only: (i) state the `⟨ωh⟩^{a−1} ≥ 2^{(a−1)/2}` lower bound explicitly in PROOF066; (ii) rephrase PROOF069 "at least `⟨hr⟩/2`" as a bound on the argument before inversion; (iii) note the factor-of-2 slack in PROOF067; (iv) make the `q^{−ε}` vs `⟨ξ⟩^{−ε}` step explicit in PROOF069.

## One-line summary

The nine canonical temporal-wave/frequency/two-variance/actual-column proofs PROOF066–074 are reconstructed soundly by direct calculation — signs, boundary terms, constants `16/(1−a)`, `4·3^{1−a}C_0(1+T)^4`, `4A_T K C_ν`, `h^{2−a}B_α(h)`/`h^{2β}`, the exact `2×2` kernel, zero-frequency handling, `(2π)^d c_d²=1`, and all `α<1/=1/>1` regimes check out — with only non-sharp constants and terseness issues, and no overclaim of the whole project beyond these scoped components.