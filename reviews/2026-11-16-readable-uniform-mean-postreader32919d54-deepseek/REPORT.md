# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

Both complete modules were read. The NEW revision is a step-structured rewrite of the OLD proofs: it inserts numbered step headings and a handful of explanatory sentences, but the statements, hypotheses, constants, limits and deductions are unchanged. Reconstructed working below confirms every new explanatory assertion under the same hypotheses.

**Global checks.** Throughout, the row normalization is unitary Fourier with `c_d = (2π)^{-d/2}`; heat has Fourier multiplier `e^{-ε|ξ|^2/2}` (variance `ε`, no extra factor); `β = 1/2 - s > 0`; `r` is the single fixed block exponent with `2 < r < 2/a` and `1 - 1/r > θ`; `p < 2 < r`, so `r/p > 1`. The masks appear as `η_R` on each factor of the row `k_R(z,w) = (η_R z_1)(η_R Λ^{-1}w_2)`, i.e. the physical mask `η_R^2` occurs once after covariance convolution; all uniform-radius operator bounds concern the E-restricted map `T_R : H_sp → K(E)`, not the `F` constant columns.

---

## L:uniform-mean-cutoff

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

OLD LF 44–62 and NEW LF 44–62 are byte-identical; the statement LF 29–42 is likewise unchanged. Reconstructed steps:

1. **Peetre multiplier bound.** Writing `⟨ξ⟩ = √(1+|ξ|²)`, Peetre gives `⟨ξ⟩^σ ⟨η⟩^{-σ} ≤ 2^{|σ|/2} ⟨ξ-η⟩^{|σ|}`. Since `(η_R f)^∧(ξ) = c_d ∫ η̂_R(ξ-η) f̂(η)dη`, splitting `⟨ξ⟩^σ` with Peetre and applying Young `L^1*L^2` gives
   ```
   ‖η_R f‖_{H^σ} ≤ c_d 2^{|σ|/2} (∫|η̂_R(q)|⟨q⟩^{|σ|}dq) ‖f‖_{H^σ}.
   ```
2. **R-uniformity.** `η̂_R(q) = R^d η̂(Rq)`. Substituting `p = Rq`,
   ```
   ∫ R^d |η̂(Rq)|⟨q⟩^{|σ|}dq = ∫ |η̂(p)|⟨p/R⟩^{|σ|}dp ≤ ∫|η̂(p)|⟨p⟩^{|σ|}dp
   ```
   since `R ≥ 1` gives `⟨p/R⟩ ≤ ⟨p⟩`. This is exactly `M_σ`, with `c_d = (2π)^{-d/2}`.
3. **Row bound.** `Λ^{-1}: H^{-1/2} → H^{1/2}` is an isometry and `H^{1/2} ↪ H^s` has norm one (`s < 1/2`). With `M = M_{1/2}`,
   ```
   ‖η_R z_1‖_{H^{1/2}} ≤ M‖z_1‖_{H^{1/2}},  ‖η_R Λ^{-1}w_2‖_{H^{1/2}} ≤ M‖w_2‖_{H^{-1/2}}.
   ```
   Lemma `L:cameron-fractional-products` (checked hypotheses `α/4 < s < 1/2`) gives
   ```
   ‖k_R(z,w)‖_{H_sp} ≤ A_s (M‖z‖_E)(M‖w‖_E) = M_0‖z‖_E‖w‖_E,  M_0 = A_s M².
   ```
4. **Operator bound.** From `E:uniform-mean-row`, for unit `q`,
   `|⟨T_R q z,w⟩_E| ≤ ‖q‖_{H_sp}‖k_R(z,w)‖_{H_sp}`, so `‖T_R‖ ≤ M_0`.

Evidence: `E:uniform-spatial-mean`; the constant `M_σ` matches the displayed `2^{|σ|/2}(2π)^{-d/2}∫|η̂(p)|⟨p⟩^{|σ|}dp`.

Pre-existing note: fixed-R compact values are imported from `P:cameron-spatial-map` (unassigned upstream) and only *retained*, not re-derived. The uniform-in-R norm bound itself is fully reconstructed.

---

## L:uniform-mean-spatial-tails

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

OLD proof LF 90–150; NEW proof LF 90–179 adds Step 1–4 headings plus three explanatory sentences (row identity/selfadjointness, factor count, averaging). Statement LF 70–88 unchanged.

Reconstructed steps:

1. **Translation estimate.** On the covariance Fourier image, `τ_h` multiplies by `e^{-iξ·h}`; dominated convergence on tests plus isometry/density gives strong continuity on `H_sp`. Using `|e^{-it}-1| ≤ 2 min(1,|t|^β)` and `|ξ|^β⟨ξ⟩^s ≤ ⟨ξ⟩^{1/2}` (valid because `β = 1/2-s`):
   ```
   ‖τ_h f - f‖_{H^s} ≤ 2 min(1,|h|^β) ‖f‖_{H^{1/2}}.
   ```
2. **Product difference.** With `f = η_R z_1`, `g = η_R Λ^{-1}w_2`,
   ```
   τ_h(fg)-fg = (τ_h f - f) τ_h g + f(τ_h g - g).
   ```
   The fractional product bound applies at `H^s × H^s`. Each term contributes `A_s · [2 min(1,|h|^β) M‖z‖_E] · [M‖w‖_E]`; two terms give the fourfold constant:
   ```
   ‖τ_h k_R(z,w) - k_R(z,w)‖_{H_sp} ≤ 4 A_s M² min(1,|h|^β)‖z‖_E‖w‖_E
   ```
   (`E:uniform-mean-row-translation`). NEW's sentence that the product bound contributes `2 A_s M²` twice is exactly this.
3. **Heat averaging.** `C_ε f = ∫ p_ε(h) τ_h f dh` is a Bochner integral; its Fourier image is `e^{-ε|ξ|^2/2} f̂`. With `h = √ε G_d`,
   ```
   ∫ p_ε(h) min(1,|h|^β) dh ≤ ∫ p_ε(h)|h|^β dh = ε^{β/2} E|G_d|^β.
   ```
   Hence `‖(I-C_ε)k_R‖ ≤ M_h ε^{β/2}‖z‖_E‖w‖_E` with `M_h = 4A_s M² E|G_d|^β`. The inserted identity
   ```
   ⟨T_R(I-C_ε)q z,w⟩_E = ⟨q,(I-C_ε)k_R(z,w)⟩_{H_sp}
   ```
   is correct because `C_ε` is selfadjoint (real Fourier multiplier); it yields `E:uniform-mean-heat`.
4. **Frequency projection `P_K`.** `V` is the closed image of `f ↦ (2π)^{d/2} f̂` in `L²(μ)`; no surjectivity is assumed. The smooth even radial `χ_n` (1 on `{|ξ|≤K}`, 0 off `{|ξ|>K+1/n}`) satisfies `χ_n f̂ ∈ V` for real Schwartz `f`, and `χ_n → 1_{|ξ|≤K}` pointwise, including the boundary sphere. Dominated convergence against `|f̂|²μ` closes in `V`; contractive extension over all of `V` defines the orthogonal idempotent `P_K`. Infinite rank is allowed.
5. **Heat residual comparison.** On `|ξ| > K`, `1 - e^{-|ξ|²/(2K²)} ≥ 1 - e^{-1/2}`, so
   ```
   ‖(I-P_K)k‖_{H_sp} ≤ (1-e^{-1/2})^{-1}‖(I-C_{K^{-2}})k‖_{H_sp}.
   ```
   With `ε = K^{-2}` the heat bound gives `M_h K^{-β}`; selfadjointness of `P_K` in the row identity gives `E:uniform-mean-frequency` with `M_f = M_h/(1-e^{-1/2})`.

The NEW explanatory assertions (selfadjoint transfer, the `2A_sM²` factors, the `min ≤ |h|^β` averaging) were all verified. Denominator `1-e^{-1/2} > 0` checked.

---

## L:uniform-mean-tensor

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

OLD proof LF 168–198; NEW proof LF 197–244 adds Step 1–2 headings and one explanatory sentence about the common `m_r` factor. Statement OLD LF 158–166 = NEW LF 187–195.

Reconstructed steps:

1. **Gaussian moment bound.** For `v = Σ_{j≤n} f_j ⊗ e_j` with orthonormal `(e_j)`, `‖v‖² = Σ‖f_j‖² =: L`. With independent standard normals `γ_j`, `X = Σγ_j f_j` has covariance `Σ f_j ⊗ f_j`; diagonalizing gives `‖X‖² = Σ_l λ_l ζ_l²`, `Σλ_l = L`. For `L > 0`, Jensen at the convex exponent `r/2 ≥ 1` with weights `λ_l/L`:
   ```
   E(Σ_l λ_l ζ_l²)^{r/2} = L^{r/2} E(Σ_l (λ_l/L)ζ_l²)^{r/2} ≤ L^{r/2} m_r Σ_l(λ_l/L) = m_r L^{r/2}.
   ```
   (`m_r = E|γ_1|^r`; `L = 0` trivial.)
2. **Scalar side and cancellation.** For each fixed `t`, `Σ_j γ_j Af_j(t)` is `N(0, Σ_j|Af_j(t)|²)`, so its `r`-th absolute moment is `m_r (Σ|Af_j(t)|²)^{r/2}`. Tonelli (finite `Σ|Af_j|² ∈ L^{r/2}`) gives
   ```
   m_r ∫(Σ|Af_j(t)|²)^{r/2}dt = E‖AΣ γ_j f_j‖_{L^r}^r ≤ ‖A‖^r m_r (Σ‖f_j‖²)^{r/2}.
   ```
   NEW's sentence "same factor `m_r` on both sides, no dimension-dependent factor remains" is exact. Cancel `m_r > 0`, take the `r`-th root, extend by density/Bochner completeness. Zero space trivial.
3. **Noncompactness.** For `Af ≠ 0` and infinite orthonormal `(e_j)`, the images `Af ⊗ e_j = (Af)e_j` have pairwise distance `√2 ‖Af‖_{L^r} > 0`, so no convergent subsequence; compactness of `A` does not transfer.

The rewrite adds no new mathematics; the variance explanation is correct.

---

## P:uniform-mean-regulator

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

OLD proof LF 233–262; NEW proof LF 279–323 adds Step 1–2 headings and, in Step 2, an explicit derivation of the first bound `‖ℳ_R‖ ≤ M_0 c_t` via `E:uniform-spatial-mean` applied pointwise. Statement OLD LF 215–231 = NEW LF 261–277.

Reconstructed steps:

1. **Projections.** `π_J`, `P_K` are selfadjoint idempotent contractions; so are `P_ret = π_J ⊗ P_K` and `Q_{J,K} = I - P_ret`.
2. **Temporal tail.** If `ε_J ↛ 0`, choose unit `v_J` with `‖C_t(I-π_J)v_J‖_{L^r}` bounded below. Since `⟨(I-π_J)v_J, h⟩ ≤ ‖(I-π_J)h‖ → 0`, `(I-π_J)v_J → 0` weakly; compactness of `C_t : H_t → L^r(I)` (from `P:cameron-temporal-map`, `2 < r < 2/a` checked) gives a norm-convergent subsequence whose weak limit is 0, a contradiction. Hence `ε_J → 0`.
3. **First bound.** By `L:uniform-mean-tensor` with `A = C_t`, `‖UΦ‖_{L^r(I;H_sp)} ≤ c_t‖Φ‖_{H_I}`; pointwise `E:uniform-spatial-mean` gives `‖T_R UΦ‖_{L^r(I;L(E))} ≤ M_0 c_t‖Φ‖`. This is the NEW inserted computation.
4. **Decomposition.**
   ```
   Q_{J,K} = (I-π_J)⊗I + π_J⊗(I-P_K).
   ```
   The first term: `U((I-π_J)⊗I) = (C_t(I-π_J))⊗I`, and the tensor lemma bounds it by `ε_J`; applying `T_R` pointwise gives `M_0 ε_J`. The second term uses the intertwining
   ```
   U(π_J⊗(I-P_K)) = (I_{L^r}⊗(I-P_K))(C_tπ_J⊗I),
   ```
   so `E:uniform-mean-frequency` pointwise plus the tensor lemma for `C_tπ_J` (`‖C_tπ_J‖ ≤ c_t`) gives `M_f c_t K^{-β}`. Triangle inequality yields `E:uniform-completed-mean`.

The NEW explicit line for `UΦ` is a valid addition; it duplicates the old argument. No uniform-radius compactness is claimed, correctly.

---

## P:uniform-actual-cameron

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

OLD proof LF 313–394; NEW proof LF 374–494 adds Step 1–5 headings plus (Step 2) the `P_0 = 0`/`Y_{m,0}` reduction and (Step 4) the explicit `L^r` bound of `ℳ_h`. Statement OLD LF 291–311 = NEW LF 352–372.

Reconstructed steps:

1. **Residual paths and first chaos.** `Y_m(f) = W(Q_full T_{δ,m}f)` with `Q_full` an orthogonal projection; the pullback `T_{δ,m}` is an isometry (checked against `L:raw-block-inputs`), so `Var Y_m(f) ≤ ‖f‖_{H_fast}²`. `P:source-gaussian-transfer` (variance hypothesis checked) produces the centered Gaussian `K(E)`-valued operator paths on the same `W`, with finite path moments at each fixed `R,B,δ,J,K`. Constant stopping puts them in the separable little `C^θ` closure.
2. **Covariance reduction.** For an explicit E-row `k` pulled back to slow time (supported-row approximation from `L:cameron-actual-residual`),
   ```
   ⟨Q_full T_{δ,m}k, h⟩_{H_W} = ⟨T_{δ,m}k, i_I Q_{J,K} i_I^* h⟩_{H_W},
   ```
   checked by expanding `Q_full = I - i_I P_ret i_I^*` and using `T_{δ,m}k ∈ H_I`. NEW's clarification is correct: in the earlier construction `P_0 = 0`, so `Y_{m,0}(f) = W(T_{δ,m}f)`; the present pairing is exactly the unprojected (`J = 0`) covariance with control `Φ = Q_{J,K} i_I^* h ∈ H_I`. Perpendicular directions `h ⊥ H_I` vanish. The completed `J = 0` identity `E:cameron-actual-covariance` applied to `Φ`, restricted to the `E` rows (`S_F|_E = S_E`, `T|_E = T_R`), and the amplitude `g_δ δ^{a/2} = √δ` give `E:uniform-actual-covariance`. Bochner measurability is via compact-operator conjugation and strong continuity of `S_E, S_E^*` on `K(E)`.
3. **Free-group bound.** The Bessel Fourier matrix (`E` coordinates) has upper off-diagonal `⟨k⟩ sin(vk)/k`, bounded by `√2 B` (`|sin(vk)| ≤ Bk` for `k ≤ 1`; `⟨k⟩/k ≤ √2` for `k ≥ 1`), lower off-diagonal ≤ 1, diagonals ≤ 1. Frobenius squared ≤ `1+1+2B²+1 = 3+2B²`, so `G_{B,E} ≤ 3B`. With `g(v) = S_E(-v)ℳ_h(s_m+δv)S_E(v)`, `‖g‖_{L^r([0,ℓ_m])} ≤ G_{B,E}² δ^{-1/r} t_m`, and the primitive Hölder bound:
   ```
   ‖(Lh)_m‖_{C^θ} ≤ √δ G_{B,E}² (B^{1-1/r} + B^{1-1/r-θ}) δ^{-1/r} t_m
   ```
   (`‖·‖_∞` gives the `B^{1-1/r}` term, the Hölder seminorm gives `B^{1-1/r-θ}`; both use `1 - 1/r > θ`). So `C_{B,E} ≤ 9B² · 2B^{1-1/r} = 18B^{3-1/r}`.
4. **Block weights.** With `n = N+1`, `r/p > 1` and inputs `t_m^p`:
   ```
   (Σ t_m^p)^{1/p} ≤ n^{1/p-1/r}(Σ t_m^r)^{1/r}.
   ```
   The true partition gives `Σ t_m^r = ‖ℳ_h‖_{L^r(I)}^r` (empty last block contributes 0) and `δn ≤ 2/B`. From `E:uniform-completed-mean` and `‖i_I^*‖ ≤ 1`,
   ```
   ‖ℳ_h‖_{L^r} ≤ [M_0 ε_J + M_f c_t K^{-β}]‖h‖_{H_W}
   ```
   (the NEW inserted bound). Combining `δ^{1/p} · δ^{-1/r} · n^{1/p-1/r} = (δn)^{1/p-1/r}` and `p < r` gives `E:uniform-actual-cameron-bound`.
5. **Cameron representative.** `H_seen` is the closed span of all coefficient tests `k_ℓ`. The first-chaos identification (`P:cameron-actual-embedding`) says `L` kills `H_seen^⊥` and the Cameron norm is the minimum `H_W` preimage norm, i.e. `‖Lh‖_CM = ‖P_seen h‖_{H_W}`. Applying the bound to the minimum-norm representative yields the embedding bound without inverse covariance or a finite-dimensional density.

All NEW added claims were verified against the same hypotheses. `G_{B,E} ≤ 3B`, `1-1/r > θ`, `δ^{-1/r}`, `C_{B,E} ≤ 18B^{3-1/r}`, the `√δ` amplitude and the `(2/B)^{1/p-1/r}` factor are unchanged and correct. Spatial constants are `R`-independent; path moments are only fixed-parameter.

---

## AUDIT dispositions

| Label | Old proof | New proof | Reconstruction | Argument | New explanations |
|---|---|---|---|---|---|
| `L:uniform-mean-cutoff` | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| `L:uniform-mean-spatial-tails` | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| `L:uniform-mean-tensor` | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| `P:uniform-mean-regulator` | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| `P:uniform-actual-cameron` | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |

---

## Findings and limits

**Preservation.** The NEW revision is a readability rewrite: identical statements and definitions, step-structured proofs, and a small number of new explanatory sentences, all of which are mathematically justified under the unchanged hypotheses. No target deduction was silently repaired, and no unsupported claim was introduced. Reading was COMPLETE for every assigned proof; public reconstruction was COMPLETE, with the constants `M_σ, M_0, M_h, M_f`, the `4A_sM²` factor, the `(1-e^{-1/2})^{-1}` conversion, the `m_r` cancellation, the intertwining decomposition, `G_{B,E} ≤ 3B`, `C_{B,E} ≤ 18B^{3-1/r}`, and the `√δ` amplitude all re-derived from public equations.

**New explanatory assertions checked:**
- `C_ε` selfadjointness → row transfer (`L:uniform-mean-spatial-tails`, Step 2).
- the two `2A_sM²` contributions and `min(1,|h|^β) ≤ |h|^β` averaging.
- the scalar-Gaussian-variance `m_r` identity (`L:uniform-mean-tensor`, Step 2).
- the explicit `‖UΦ‖ ≤ c_t‖Φ‖`, `‖T_RUΦ‖ ≤ M_0c_t‖Φ‖` (`P:uniform-mean-regulator`, Step 2).
- the `P_0 = 0`, `Y_{m,0}` reduction to the unprojected covariance with `Φ = Q_{J,K}i_I^*h`, and the `L^r` bound of `ℳ_h` from `E:uniform-completed-mean` (`P:uniform-actual-cameron`, Steps 2 and 4).

**Pre-existing concerns / upstream reliance (not rewrite defects).** Fixed-R compact values in the cutoff lemma, the temporal compactness `ε_J → 0`, the Gaussian-transfer path construction, the pullback isometry, and the completed `J = 0` covariance identity are imported from unassigned upstream modules (`P:cameron-spatial-map`, `P:cameron-temporal-map`, `P:source-gaussian-transfer`, `L:raw-block-inputs`, `P:cameron-actual-embedding`). Their application hypotheses were checked; their own proofs were not assigned and were not counted. The module's closing caveat is retained verbatim in both revisions: these linear bounds do **not** give growing-mask expected residual norms, concentration, conditioning over the infinite sum, or a moment upper theorem. The retained and residual Gaussian fields (`P_full`, `Q_full`) are independent, while residual time blocks may remain correlated; this is intact.

**Limits of this review.** This is rewrite-preservation review only. It does not certify source PDFs/images, Lean correspondence, rendered pages, human sign-offs, whole-book truth, or the unassigned upstream proofs. No failure or new defect was found; the verdict is PASS with high confidence.
