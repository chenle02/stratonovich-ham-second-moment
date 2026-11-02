# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I found no proof gap, false identity, hidden hypothesis, incorrect constant, sign error, boundary-term loss, or invalid asymptotics inside the five assigned proof bodies (PROOF151–155). The R-independent constants are exact where claimed.

## Noncritical findings

1. **PROOF151, terseness only.** The step "Hilbert Cauchy–Schwarz then gives the operator bound" names Riesz duality for the sesquilinear kernel `k_R(z,w)` rather than an actual trace-class/HS argument. The claim is correct: the bilinear form realizes `z ↦ (w ↦ ⟨q,k_R(z,w)⟩)` as an element of `E* ≅ E`, with norm ≤ sup‖k_R(z,w)‖ ≤ M₀. Optional clarity, no defect.

2. **PROOF154, notation.** In the decomposition `Q_{J,K} = (I−π_J)⊗I + π_J⊗(I−P_K)` the symbol `I` is overloaded (`I_{H_t}` vs `I_{H_sp}`); context disambiguates. Also the typed intertwining `U(π_J⊗(I−P_K)) = (I_{L^r}⊗(I−P_K))(C_t π_J⊗I)` requires identifying `L^r(I)⊗H_sp ≅ L^r(I;H_sp)`, which is standard Bochner identification. Both verified correct.

3. **Interface dependency (in-scope).** PROOF155 imports, as supplied premises: (i) the completed `J=0` covariance identity of `P:cameron-actual-embedding`, (ii) Gaussian transfer `P:source-gaussian-transfer`, (iii) the residual-path lemma `L:cameron-actual-residual`, (iv) the raw pullback isometry `L:raw-block-inputs`. I verified their *consistent use* and the E-restriction/amplitude/constants are re-derived in the five own bodies, but I did not re-derive those prerequisite bodies themselves (they are outside the assigned five). No inconsistency found in the interfaces.

4. **External source depth limitation.** The five proofs do **not** directly import Teschl/Friz–Hairer/Crouzeix/Chen; those enter only through reference bodies (Young evolution, compact-mean family). Their carriers here are OCR text only; image/edition verification was not performed and is recorded as a limitation, not a defect of PROOF151–155.

5. **Zero covariance.** The section is stated for nonzero covariance. The zero-noise case is trivial (`u=1`, all means/drivers vanish) and is handled in the downstream sections, not expanded in these five bodies. Not a gap under the stated nonzero scope.

## Checked derivations

**PROOF151 — `L:uniform-mean-cutoff` (uniform multiplier + physical mean).** Status: CHECKED.
- *Hypothesis:* real σ, `R≥1`, `η_R(x)=η(x/R)` even smooth compact, `α/4<s<1/2`.
- *Verified:* unitary convention `ĉ(ξ)=c_d∫e^{−iξ·x}f dx`, `c_d=(2π)^{−d/2}`; Peetre `⟨ξ⟩^σ⟨η⟩^{−σ} ≤ 2^{|σ|/2}⟨ξ−η⟩^{|σ|}`; convolution kernel `c_d 2^{|σ|/2}|η̂_R(q)|⟨q⟩^{|σ|}`; `η̂_R(q)=R^dη̂(Rq)`; substitution `p=Rq` and `⟨p/R⟩≤⟨p⟩` for `R≥1` give exactly `M_σ = 2^{|σ|/2}(2π)^{−d/2}∫|η̂(p)|⟨p⟩^{|σ|}dp`, R-independent, valid for all real σ including negative. Young `L^1*L^2` gives the multiplier norm.
- *Row:* `k_R(z,w)=(η_R z_1)(η_R Λ^{-1}w_2)` — both phase slots, one mask (η_R·η_R=m_R). `Λ^{-1}:H^{-1/2}→H^{1/2}` isometry (`‖Λ^{-1}f‖_{H^{1/2}}=⟨ξ⟩^{-1/2}f̂`); `H^{1/2}↪H^s` norm exactly 1 (`⟨ξ⟩^{2s−1}≤1` for `s<1/2`). Fractional product `‖fg‖_{H_sp}≤A_s‖f‖_{H^s}‖g‖_{H^s}`, `A_s=C_s²√R_sp` ⇒ `‖k_R‖ ≤ A_sM²‖z‖_E‖w‖_E = M₀‖z‖_E‖w‖_E`; operator bound `‖T_R‖≤M₀`. Consistent with the completed map of `P:cameron-spatial-map` (F-column hidden behind E-restriction; none appears in the uniform bound).

**PROOF152 — `L:uniform-mean-spatial-tails` (heat tail + frequency tail).** Status: CHECKED.
- *Heat tail:* translations unitary on `H_sp` (multiplier `e^{−iξ·h}`), strong continuity by DC; real subspace preserved. Pointwise `⟨ξ⟩^s|e^{−iξh}−1|≤2min(1,|h|^β)⟨ξ⟩^{1/2}` verified (split `|h|≥1` / `|h|≤1`, using `|ξ|^β⟨ξ⟩^s≤⟨ξ⟩^{1/2}`, `β=1/2−s`). Product identity valid in `H_sp` by fractional-product continuity. Two-term constant `4A_sM²` (both cross terms `A_s·2min·M‖z₁‖·M‖w₂‖`). Gaussian average `h=√εG_d`: variance ε, Fourier multiplier `e^{−ε|ξ|²/2}` (no extra normalization), `ε^{β/2}`, giving `M_h=4A_sM²E|G_d|^β`. Row self-adjointness of `C_ε` transfers to `‖T_R(I−C_ε)‖≤M_hε^{β/2}`. No mask/heat commutation.
- *Frequency tail:* `P_K` built on closed image `V⊂L²(μ)` (no onto-`L²(μ)` assumed, keeps `(2π)^{d/2}` factor); `χ_n=1` on the closed ball, 0 off `K+1/n`; dominated convergence includes the boundary sphere (even μ-charged); extension from dense image by contraction. Indicator multiplication self-adjoint/idempotent/real, commutes with heat. On `|ξ|>K`, multiplier `1−e^{−|ξ|²/(2K²)}≥1−e^{−1/2}`, so `n(ξ)²≥(1−e^{−1/2})²1_{|ξ|>K}` — I confirmed the correct comparison is `‖(I−P_K)k‖ ≤ (1−e^{−1/2})^{-1}‖(I−C_{K^{-2}})k‖` (not the square root; the squared-norm factor `n(ξ)²` yields the inverse of `1−e^{−1/2}` exactly). With `ε=K^{-2}` and the heat tail: `‖(I−P_K)k‖≤M_f K^{−β}`, `M_f=M_h/(1−e^{−1/2})`. Infinite rank OK; no abs-continuity/periodicity assumption.

**PROOF153 — `L:uniform-mean-tensor` (dimension-free tensor extension).** Status: CHECKED.
- Finite tensor norm `Σ‖f_j‖²`; independent normals γ_j, `m_r=E|γ|^r`; diagonalization trace `L=Σλ_l=Σ_j‖f_j‖²`; convexity at `r/2≥1` gives `E‖Σγ_jf_j‖^r ≤ m_rL^{r/2}`. Scalar moment `E|Σγ_j(Af_j)(t)|^r = m_r(Σ|Af_j(t)|²)^{r/2}` by Tonelli; `E‖AΣγf_j‖^r_{L^r}≤‖A‖^r m_r L^{r/2}`; cancelling finite positive `m_r` and taking the r-th root gives `‖(A⊗I_G)v‖_{L^r(I;G)}≤‖A‖‖v‖`. Density+Bochner completeness extend. `r=2` and zero spaces handled. Noncompactness witness: `‖Af⊗(e_j−e_k)‖_{L^r(G)}=√2‖Af‖_{L^r}>0` for infinite ON `(e_j)`, so the bounded sequence `f⊗e_j` has no convergent image subsequence even when A is compact. No infinite Gaussian vector; bounded-tensor ≠ compact-tensor is correctly asserted.

**PROOF154 — `P:uniform-mean-regulator` (uniform completed mean regulation).** Status: CHECKED.
- `P_ret=π_J⊗P_K`, `Q_{J,K}=I−P_ret` orthogonal (tensor of orthogonal projections). `ε_J→0` by weak-null-plus-compact (`(I−π_J)v_J⇀0`, `C_t` compact, norm-convergent subsequence →0). Lemma 153 transfers the scalar tail without dimension factor.
- First bound `‖T_R‖≤M₀c_t`: pointwise `‖T_Rq‖≤M₀‖q‖` composed with `‖U‖=‖C_t⊗I‖≤c_t`.
- Exact decomposition sums to `I−π_J⊗P_K` (verified algebraically). Typed intertwining verified on finite tensors coefficient-by-coefficient (order preserved: `C_tπ_J` acts before `I−P_K` in the spatial slot). Second term `T_R(I_{L^r}⊗(I−P_K))(C_tπ_J⊗I)` bound by pointwise `‖T_R(I−P_K)‖·‖(C_tπ_J⊗I)Φ‖ ≤ M_fK^{−β}·c_t‖Φ‖`. Total `M₀ε_J+M_f c_t K^{−β}`, uniform in `R≥1`. `ε_J,c_t` are R-independent (temporal only). Fixed-R compact values/strong measurability in `K(E)` correct; no uniform compactness, no finite-rank head.

**PROOF155 — `P:uniform-actual-cameron` (uniform-radius actual Cameron bound).** Status: CHECKED.
- `Var Y_m(f)=‖Q_fullT_{δ,m}f‖²≤‖f‖²_{H_fast}` (isometric pullback + orthogonal projection).
- Supported-row pairing `⟨Q_fullT_{δ,m}k,h⟩=⟨T_{δ,m}k,i_I Q_{J,K}i_I^*h⟩` verified via projectors: the h-component perpendicular to `H_I` annihilates against `T_{δ,m}k∈H_I`.
- `J=0` completed identity applied to `Q_{J,K}i_I^*h`, then genuine F→E restriction (`S_F|_E=S_E`, full mean restricted to `T_R`); no formal smoothness substitution. Amplitude `g_δδ^{a/2}=δ^{(1−a)/2}δ^{a/2}=√δ` exact.
- Bessel-unitary matrix of `S_E`: diagonals ≤1, upper `≤√2B`, lower `≤1`, zero-frequency sine = v; Frobenius `≤√(3+2B²)≤3B`; `G_{B,E}≤3B`. Primitive constant `C_{B,E}=G_{B,E}²(B^{1−1/r}+B^{1−1/r−θ})≤18B^{3−1/r}` (using `G²≤9B²`, `B^{1−1/r}+B^{1−1/r−θ}≤2B^{1−1/r}`). `1−1/r>θ`, constant stopping to little C^θ, empty block zero. Bochner measurability via compact values + strong continuity of both `S_E` and its adjoint (no free-group norm continuity).
- Power-mean: `(Σt_m^p)^{1/p}≤n^{1/p−1/r}(Σt_m^r)^{1/r}`, nonnegative inputs, `p<r`; `δ^{1/p−1/r}` accounts exactly; `Σt_m^r=‖M_h‖^r_{L^r(I)}`, `δn≤2/B` (`N=⌊1/(δB)⌋`, `δ<1/B`); final `√δ C_{B,E}(2/B)^{1/p−1/r}[M₀ε_J+M_f c_t K^{−β}]‖h‖`. No missing δ/N/B factor.
- Cameron geometry: `ker L = H_seen^⊥`, first-chaos space `L(H_seen)`, `‖Lh‖_{CM}=‖P_seen h‖_{H_W}`; bound applied to the min-preimage representative; no inverse covariance/density. Independence (`P_full`⊥`Q_full`) vs residual-block correlation, infinite-rank head, and the "not a growing-R residual-norm/concentration/conditioning bound" statement are all correct and honest.

## Five-proof status/ledger (hypothesis → conclusion → application)

| ID | Status | Hypothesis | Conclusion / use |
|---|---|---|---|
| PROOF151 `L:uniform-mean-cutoff` | CHECKED | real σ, R≥1, η_R profile | multiplier norm ≤ M_σ (R-indep.); row bound `‖T_R‖≤M₀`; feeds all later R-uniform bounds |
| PROOF152 `L:uniform-mean-spatial-tails` | CHECKED | β=1/2−s>0, K≥1, ε>0, C_ε heat, P_K closed-ball projection | heat tail `M_h ε^{β/2}`, frequency tail `M_f K^{−β}`; feeds regulator second term |
| PROOF153 `L:uniform-mean-tensor` | CHECKED | 2≤r<∞, A:H₀→L^r(I) | `‖A⊗I_G‖≤‖A‖`, extension noncompact in general; transfers scalar tails dimension-free |
| PROOF154 `P:uniform-mean-regulator` | CHECKED | `H_I=H_t⊗H_sp`, `C_t` compact, `U=C_t⊗I`, `P_ret=π_J⊗P_K` | `‖T_R‖≤M₀c_t`, `‖T_RQ_{J,K}‖≤M₀ε_J+M_fc_tK^{−β}`, `ε_J→0`; supplies the two R-uniform tails in 155 |
| PROOF155 `P:uniform-actual-cameron` | CHECKED | actual residual `Y_m`, `P_full=i_IP_reti_I*`, `g_δ=δ^{(1−a)/2}`, B,δ,N,ℓ_m, θ,r,p | amplitude √δ, Cameron embedding bound `≤√δ C_{B,E}(2/B)^{1/p−1/r}[M₀ε_J+M_fc_tK^{−β}]`, `C_{B,E}≤18B^{3−1/r}` |

## UME01–UME10

- **UME01** — PASS. Peetre constant `2^{|σ|/2}(2π)^{−d/2}`, unitary Fourier, `p=Rq`, `R≥1`, all real σ, `Λ^{-1}` isometry, `H^{1/2}→H^s` norm 1, `A_s=C_s²√R_sp`, `M₀=A_sM²`, both slots one mask, row/compact-values correct, no F-column hidden.
- **UME02** — PASS. Translation isometry, product identity, `β=1/2−s>0`, two-term constant `4A_sM²`, Gaussian variance ε, `M_h=4A_sM²E|G_d|^β`, no mask/heat commute.
- **UME03** — PASS. `P_K` on closed image V (no surjectivity), χ_n=1 on closed ball, DC includes boundary sphere, self-adjoint/idempotent/real/heat-commuting, `1−e^{−1/2}` gap with `ε=K^{-2}`, `M_f=M_h/(1−e^{−1/2})`, infinite rank allowed, no μ-density/periodicity.
- **UME04** — PASS. Finite ON/Gaussians, trace `L=Σ‖f_j‖²`, convexity at r/2≥1, scalar Gaussian/Tonelli cancels `m_r`, norm ≤‖A‖, measurable reps, Bochner density, r=2 and zero cases, `√2‖Af‖` noncompactness witness, bounded-not-compact correctly stated.
- **UME05** — PASS. `H_I` tensor identity, `ε_J→0`, dimension-free tail transfer, typed intertwining preserves coefficient order, exact `M₀c_t` and `M₀ε_J+M_fc_tK^{−β}`, fixed-R compact values/strong measurability, no uniform compactness/finite-rank assertion.
- **UME06** — PASS. `i_I` closed isometry, `P_full=i_IP_reti_I*` orthogonal (infinite rank OK), same-W residual, variance contraction, β>θ constant stopping/empty block, supported rows incl endpoints, exact removal of `H_I`-perp directions, J=0 completed identity on arbitrary projected controls, genuine F→E restriction, amplitude `√δ` exact, compact values + strong group-and-adjoint (no free-group norm continuity).
- **UME07** — PASS. Bessel-unitary matrix entries (`≤√2B`, ≤1), Frobenius `√(3+2B²)≤3B`, `C_{B,E}=G²(B^{1−1/r}+B^{1−1/r−θ})≤18B^{3−1/r}`, `1−1/r>θ`, `p<r`, `n=N+1≥2`, `δn≤2/B`, exact `(2/B)^{1/p−1/r}` with no missing δ/N/B, cov amplitude `√δ`, R-independence tracked.
- **UME08** — PASS. Every linear statistic = `W(k_l)`, `H_seen` closure, `ker L=H_seen^⊥`, first-chaos `L(H_seen)` with min raw preimage norm; no inverse covariance/density/infinite-H-valued noise; `P_full`/`Q_full` independent vs residual-block correlation stated correctly; infinite spatial head; heat residual distinct/correlated.
- **UME09** — PASS. `α/4<s<1/2`, `β=1/2−s`; strict `θ∈(1/2,min(1−a/2,(3−a−α)/2))`, `r∈(1/(1−θ),2/a)`, `1/θ≤p<2<r`, tensor `r≥2`; original amplitude retained; general Γ (incl. d1 white/anisotropic/singular); σ<0 cutoff; all ε>0, K≥1, closed ball; low-frequency P_K; J=0 and π_0=0; empty last cell; raw directions outside `H_I`; pure velocity slot via `Λ^{-1}`; E vs F constant columns; finite/infinite G. False claims (uniform-R compact tail, instantaneous Gaussian, infinite-head conditioning/expected residual norm at growing R, nonlinear bound) are not claimed.
- **UME10** — PASS. All five proofs reconstructed independently; no unchecked step or falsification found; hypothesis/conclusion/use ledger complete; scalar row and coefficient order preserved; no nonlinear/moment/concentration/cold/source-image/213-proof/novelty/publication/companion claim; no prior votes or forced HIGH.

## Required fixes before production gate

None (blocking). Optional clarity items only:
- PROOF151, spell out the Riesz/bilinear form behind "Hilbert Cauchy–Schwarz".
- PROOF154, disambiguate the `I` identities in the `Q_{J,K}` decomposition (optional).

## One-line summary

All five assigned uniform-mean/Cameron proofs (PROOF151–155) independently reconstruct into correct and complete arguments with exact, genuinely R-independent constants (`M_σ`, `M_0=A_sM²`, `M_h=4A_sM²E|G_d|^β`, `M_f=M_h/(1−e^{−1/2})`, `C_{B,E}≤18B^{3−1/r}`, `(2/B)^{1/p−1/r}`, amplitude `√δ`), no hidden F-column, no false compactness/instantaneous/conditioning overclaims, and honest scope statements; UME01–UME10 all PASS; only non-blocking interface/notation notes and external source-carrier limitations remain.

**Explicit completion statement:** the five target proofs are independently checked from the supplied source text; no proof is left unfinished and no step is silently repaired — the cited prerequisites (`L:cameron-fractional-products`, `P:source-gaussian-transfer`, `L:cameron-actual-residual`, `P:cameron-actual-embedding`, `L:raw-block-inputs`) were audited as consistent interfaces rather than re-derived, which is within this unit's assigned scope and is recorded above.