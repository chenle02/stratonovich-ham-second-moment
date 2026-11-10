# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. No proof gap, false identity, hidden hypothesis, sign error, or incorrect constant was found in the seven assigned proofs after by-hand reconstruction. The final coefficients of PROOF142–148 reproduce exactly, and every claimed asymptotic/compactness/trace-class distinction is correctly drawn.

## Noncritical findings

1. **Interface-depth limitation (not a gap).** PROOF142 leans on `P:spatial-four-linear` and `L:spatial-physical-pair` from `integrated_spatial_occupation.tex` for the absolute full-`H^1` four-linear bound, `N(f)=‖f‖_2^{1−α/4}‖f‖_2^{α/4}` and the Lebesgue-null transfer. I read that module's full proof (including `P:spatial-smooth-ratio`), but its ultimate finiteness of `R_sp` flows through `S_1^pos` boundedness → `T:full-upper`. This is *interface-read*, not exhaustively re-derived. I traced the ordering and found **no circularity**: `T:full-upper` is independent of the Cameron section, so the Cameron → occupation → full-upper chain is acyclic.

2. **Existential (non-sharp) constants.** `C_s`, `C_{a,r}`, `C_B`, `M_0`, `C_mean` are existence constants; the manuscript does not claim numerical sharpness, and I do not flag their (unclaimed) sharpness.

3. **Long constructions read, not line-by-line re-derived.** `P:actual-operator-driver` (the `C^θ` compact-operator path with `√p` Gaussian norm bounds) and `P:source-gaussian-transfer` are read fully at the lemma level (both variance directions via `P:wave-two-variances`; the n=16 coordinate-row counterexample `R:gaussian-one-variance-test` is correct and shows both variances are mandatory), but I did not reproduce every dyadic-chaining bound line. No defect was detected in the parts I re-derived.

4. **External source carriers.** The seven proofs themselves import little external analysis; the heavy imported theorems (Teschl form representation, Crouzeix–Palencia, Chen–Hu static coefficient rate) appear in *other* modules on the `R_sp`-finiteness chain. Their text carriers are present and internally consistent, but the PNG/rendered images are unavailable in this snapshot, so primary-source OCR fidelity for those imports is recorded as a limitation, not checked page-by-page.

## Checked derivations

**PROOF142 (`L:cameron-fractional-products`) — CHECKED.**
- Band derivative bound: on `2^{j−1}≤|ξ|<2^j`, `‖∇f_j‖_2≤2^j‖f_j‖_2`, hence `N(f_j)≤2^{jα/4}‖f_j‖_2` (low band factor 1 since `|ξ|<1`).
- Weighted Cauchy–Schwarz: `Σ_j 2^{jα/4}‖f_j‖_2 ≤ (Σ_j 2^{2js}‖f_j‖_2^2)^{1/2}(Σ_j 2^{−2j(s−α/4)})^{1/2}`; the series converges iff `s>α/4`, and `Σ_j 2^{2js}‖f_j‖_2^2 ≤ 2^{2s}‖f‖_{H^s}^2`.
- Polarization `fg=((f+g)²−(f−g)²)/4` gives a well-defined PSD bilinear extension; double series `Σ_{j,k}f_jg_k` converges absolutely in `H_sp` with `‖fg‖≤√R_sp(ΣN(f_j))(ΣN(g_k))`.
- No `L^p` multiplier theorem, no endpoint `s=α/4`. Correct.

**PROOF143 (`P:cameron-spatial-map`) — CHECKED.**
- Row identity reconstructed: `⟨T_sp qz,w⟩_F = ⟨m_R(Γ*q)(z_1+c_1), w_2⟩`, and the physical `H^{−1/2}` pairing in `E` is against `w'=Λ^{−1}w_2`, so with `m_R=η_R²` the row equals `B_Γ(q, (η_Rz_1+c_1η_R)(η_Rw'))` after evenness of Γ. Velocity weight `Λ^{−1}` is exactly where CAM02 demands; exactly one mask coefficient (no squared-mask double count).
- Compactness gain: `η_R : H^{1/2}→H^s` is, in `L²` coordinates, `Λ^s η_R Λ^{−1/2} = K_{η_R,s,1/2−s}` with σ=s, γ=1/2−s>0, giving `s_j ≲ j^{−(1/2−s)/d}`. Gain is `1/2−s`, not `s−1/2`.
- `c_1η_R` family is 1-dimensional compact; `c_2` (instantaneous velocity) column zero; product set `L` compact in `H_sp` via the fractional-product bound; map compactness via `T_sp(I−Q_n)→0` is genuinely *compactness of the operator*, separate from compact values.

**PROOF144 (`L:cameron-supported-tensor`) — CHECKED.**
- Raw spacetime covariance is `|s−t|^{−a}Γ(x−y)`, so the completion of separated tensors is the Hilbert tensor `H_t⊗H_sp` after null quotients.
- Density error: `‖E‖²_{H_W} ≤ ε²|A|Γ(A−A)∫_I∫_I|s−t|^{−a}dsdt <∞` (using `A−x⊆A−A` and positive-measure monotonicity).
- Gram–Schmidt preserves compact support; `P_J` remains an orthogonal projection in `H_W`. Explicitly not indicator multiplication, no disjoint-time independence. Correct.

**PROOF145 (`P:cameron-temporal-map`) — CHECKED.**
- Fourier: `∫_R e^{−λ|v|}e^{−iξv}dv = 2λ/(λ²+ξ²)` — strict positivity and injectivity.
- Truncation: `‖K−K_ε‖_{Schur} ≤ 2ε^{1−a}/(1−a)` (row/column integral `2∫_0^ε u^{−a}du`).
- `ι:f↦K^{1/2}f` isometric (`⟨Kf,f⟩=‖K^{1/2}f‖²`), dense range (ker K=0) ⇒ onto.
- Young exponents: `u=r/2, v=r'` give `1/u+1/v = 2/r+(r−1)/r = 1+1/r`; `K_a∈L^{r/2}` iff `ar/2<1` iff `r<2/a`; covariance C-S + `L^r` duality give `‖Kf‖_r≤√‖K_a‖_{r/2}‖f‖_{H_t}`.
- Trace: for `N^{1/2}1_{[j/N,(j+1)/N)}`, `⟨Ke,e⟩=2N^{a−1}/((1−a)(2−a))` per cell, sum `2N^a/((1−a)(2−a))→∞`, so K is not trace class and `C_t` is not Hilbert–Schmidt. Correct; compact ⇏ trace class is nailed down.

**PROOF146 (`P:cameron-full-mean`) — CHECKED.**
- `‖g‖²_{H_t⊗H_sp} ≤ ∫∫|s−t|^{−a}‖g_s‖‖g_t‖dsdt ≤ C_{a,r}²‖g‖²_{L^{r'}(H_sp)}` (PROOF145 Young bound applied to the scalar field `‖g_·‖`).
- Spatial covariance applied exactly once, by `T_sp`; compactness via `T_n=T_spQ_nU` with finite spatial rank and precompact scalar `C_t` image, `T_n→T` in operator norm. Scalar time compactness ⊗ infinite identity correctly identified as insufficient.
- `ε_J=‖T(I−P_J)‖→0` via `(I−P_J)v_J⇀0` and compactness. Correct.

**PROOF147 (`L:cameron-actual-residual`) — CHECKED.**
- `Var Y_{m,J}(f)=‖Q_JT_{δ,m}f‖²≤‖f‖²` (pullback isometry + orthogonality of `Q_J`), enabling `P:source-gaussian-transfer`.
- `Q_J` preserves `H_I` because `P_J⊂H_I`; projected transfer `P_HQ_JT_{δ,m}` reproduces original rows (slow residual already supported in `[0,1]`, endpoints admitted by indicator approximation against `|s−t|^{−a}Γ`).
- Every continuous linear statistic `ℓ(X)=W(k_ℓ)` with `k_ℓ∈H_I` via the closed isonormal image; joint Gaussian finite tuple; empty last interval zero. No independence of blocks, no `H`-valued W. Correct.

**PROOF148 (`P:cameron-actual-embedding`) — CHECKED.**
- `E[Y_{m,J}(f)W(Φ)] = δ^{a/2}∫f(v,x)h_{Q_JΦ}(s_m+δv,x)dxdv` (raw pullback Jacobian); `g_δδ^{a/2} = δ^{(1−a)/2}δ^{a/2} = √δ`.
- Conjugation `S_F(−v)T(Q_JΦ)(s_m+δv)S_F(v)`: interaction picture with both constant columns (constant velocity picks up displacement `v`; constant displacement stays 1). Strong continuity of `S_F` *and its adjoint*, compact-image conjugation norm continuity, joint measurability — no free operator-norm continuity of the group, no pathwise noise substitution.
- Primitive estimate: increment over `[u₁,u₂]` `≤ G_B²δ^{−1/r}‖M‖_{L^r|u₂−u₁|^{1−1/r}}`, so `‖(LΦ)_m‖_{C^θ} ≤ √δ·C_B·δ^{−1/r}‖M‖_{L^r(I_m)}` with `C_B=G_B²[B^{1−1/r}+B^{1−1/r−θ}]`, `1−1/r>θ`.
- Power mean: `(Σt_m^p)^{1/p} ≤ n^{1/p−1/r}(Σt_m^r)^{1/r}`, `n=N+1≥2`, `δn≤2/B`, `Σt_m^r=‖M‖^r`, `‖M‖≤ε_J‖Φ‖`. Since `p<r`, `1/p−1/r>0`, giving exactly `√δ·C_B(2/B)^{1/p−1/r}ε_J‖Φ‖_H`. No missed `δ/B`; `B` factor explicit.
- Cameron-space identification: `ker L_{δ,J}=H_seen^⊥` with first-chaos norm `‖P_seen h‖_H`, minimum raw preimage norm, **not** inverse covariance. Correct.

The `√δ` scaling, `(2/B)^{1/p−1/r}`, the strict `ε_J→0` at fixed `R`, and the explicit (not implicit) `B`-dependence all match the scope ledger exactly.

## Required fixes before production gate

None. All seven proofs are mathematically sound as written; the honest noncritical notes above concern verification depth of *unassigned* downstream dependencies, not defects in the assigned proofs.

## Seven-proof statuses

| Proof | Claim | Status |
|---|---|---|
| PROOF142 | `L:cameron-fractional-products` | CHECKED |
| PROOF143 | `P:cameron-spatial-map` | CHECKED |
| PROOF144 | `L:cameron-supported-tensor` | CHECKED |
| PROOF145 | `P:cameron-temporal-map` | CHECKED |
| PROOF146 | `P:cameron-full-mean` | CHECKED |
| PROOF147 | `L:cameron-actual-residual` | CHECKED |
| PROOF148 | `P:cameron-actual-embedding` | CHECKED |

## CAM01–CAM12 checks

- **CAM01 (PROOF142 fractional products):** PASS.
- **CAM02 (PROOF143 spatial map):** PASS.
- **CAM03 (PROOF144 supported tensor):** PASS.
- **CAM04 (PROOF145 temporal map):** PASS.
- **CAM05 (PROOF146 full mean):** PASS.
- **CAM06 (PROOF147 actual residual):** PASS.
- **CAM07 (PROOF148 embedding covariance):** PASS.
- **CAM08 (PROOF148 averaged norm/RKHS):** PASS.
- **CAM09 (domain/parameter/application ledger):** PASS — parameter windows nonempty (`α/4<s<1/2` since `α<2`; nested `θ<β<β₂`; `1<1/(1−θ)<r<2/a`, `1/θ≤p<2<r`); fixed-R compactness only; no uniform-R borrow.
- **CAM10 (adversarial controls):** PASS — d1/white, anisotropic/singular, null sets, zero covariance, low frequency, strict `r` endpoints, formal `a→0`, finite/infinite tensor labels, `η_R` root vs `m_R=η_R²`, empty last cell and floor partition, constant velocity, `H_I`-supported vs outside directions, residual correlations (no false independence), trace growth falsifying instantaneous `L²`-Gaussian while compact mean remains valid.
- **CAM11 (primary/source/dependency fidelity):** PASS with recorded limitation — all named prerequisite bodies are available; `R_sp` finiteness chain is non-circular; some unassigned bodies read at chain level; primary-source PNG/image and OCR page-level verification unavailable in this snapshot.
- **CAM12 (full seven-proof coverage/honesty):** PASS — scope honored: deep seven-proof audit only, no 28-file/213-proof/global/source-image/cold clearance claimed.

## One-line summary

All seven Cameron/compact-mean proofs (142–148) are reconstructed and verified correct — signs, boundary terms, Young/Schur/dyadic/power-mean constants, the `√δ=δ^{a/2}g_δ` scale, the fixed-`R` compactness, and the trace-class/gaussian-instantaneous distinctions — with only honest interface-depth notes on unassigned downstream dependencies (`R_sp` finiteness via `T:full-upper`) and no required fixes.

## Final completion statement

This run directly audits only the seven assigned proofs PROOF142–148 (`integrated_cameron_mean.tex`) at deep mathematical depth, plus their active prerequisite clauses as embedded. It does **not** certify the other 28 TeX modules, the other 206 proofs, source-page image authenticity, or any global/whole-paper gate; those remain out of this snapshot's scope and are not relabeled as passed. Verdict **PASS_WITH_NOTES** at **HIGH** confidence, honestly recorded per the no-forced-HIGH, no-delegation, no-prior-verdict constraints.