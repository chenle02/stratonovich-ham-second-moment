# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro (deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

This is an independent reconstruction-based review of the five assigned
proof pairs in `notes/integrated_uniform_mean.tex` (old
`cdde711c…`, new `08575eb…`). I read every complete proof in both revisions,
reconstructed each deduction from checkable public estimates, and compared all
new explanatory assertions under the unchanged hypotheses. Upstream named
results (fractional products, compact spatial map, block pullback, Gaussian
transfer, the completed `J=0` Cameron covariance, etc.) are used only after
checking their application hypotheses, and are not counted as additional
reviewed proofs. No tools, files, or network were used.

---

## L:uniform-mean-cutoff

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (statement and proof text are byte-identical
  at lines 29–42 and 44–62 respectively)
- New explanations: JUSTIFIED (no new text introduced in this pair)
- Evidence: The proof is unchanged, so I reconstruct both.

**Step 1 (Peetre multiplier bound).** With unitary Fourier transform `c_d =
(2π)^{-d/2}`, multiplication by `η_R` has symbol convolution
`(η_R u)^ = c_d (η̂_R * û)`. Peetre gives `⟨ξ⟩^σ ≤ 2^{|σ|/2}⟨ξ-q⟩^{|σ|}⟨q⟩^{|σ|}`,
hence `⟨ξ⟩^σ|(η_R u)^(ξ)| ≤ c_d 2^{|σ|/2}∫|η̂_R(q)|⟨q⟩^{|σ|}⟨ξ-q⟩^σ|û(ξ-q)|dq`,
i.e. convolution of `⟨ξ⟩^σ û` against the kernel
`2^{|σ|/2}(2π)^{-d/2}|η̂_R(q)|⟨q⟩^{|σ|}`.

**Step 2 (`R`-independence).** `η̂_R(q) = R^d η̂(Rq)`. Substituting `p=Rq`
(`dq = R^{-d}dp`) yields `∫|η̂_R(q)|⟨q⟩^{|σ|}dq = ∫|η̂(p)|⟨p/R⟩^{|σ|}dp`.
Since `R≥1`, `⟨p/R⟩ ≤ ⟨p⟩`, so the `L^1` norm is bounded by
`M_σ = 2^{|σ|/2}(2π)^{-d/2}∫|η̂(p)|⟨p⟩^{|σ|}dp`, finite for Schwartz `η`. This is
exactly the asserted normalization and constant, valid for every real `σ`.

**Step 3.** `L^1 * L^2` (Young) proves boundedness on Schwartz functions; density
extends to `H^σ`.

**Step 4 (velocity isometry).** `‖Λ^{-1}w_2‖_{H^{1/2}} = ‖Λ^{1/2}Λ^{-1}w_2‖_{L^2}
= ‖Λ^{-1/2}w_2‖_{L^2} = ‖w_2‖_{H^{-1/2}}`, so it is an isometry. `H^{1/2}↪H^s`
has norm one since `s<1/2`.

**Step 5 (row bound).** `k_R(z,w) = (η_R z_1)(η_R Λ^{-1}w_2)` has two `H^{1/2}`
factors, each norm `≤ M_{1/2}` times the corresponding `E`-component norm.
Lemma `L:cameron-fractional-products` (hypotheses met: `α/4<s<1/2`, real `H^s`
factors) gives `‖fg‖_{H_sp} ≤ C_s²√R_sp‖f‖_{H^s}‖g‖_{H^s}`; writing
`A_s = C_s²√R_sp`, `M = M_{1/2}` and using `‖f‖_{H^s} ≤ ‖f‖_{H^{1/2}}`, one gets
`‖k_R(z,w)‖_{H_sp} ≤ A_s M²‖z_1‖_{H^{1/2}}‖w_2‖_{H^{-1/2}} ≤ M_0‖z‖_E‖w‖_E`.
This is the fractional row bound `M_0 = A_s M²`, constant in `R`.

**Step 6 (operator bound).** From the row identity,
`‖T_R q‖_{L(E)} = sup_{‖z‖,‖w‖≤1}|⟨q,k_R(z,w)⟩| ≤ M_0‖q‖_{H_sp}`, i.e.
`‖T_R‖ ≤ M_0`. Compact values at fixed `R` are retained as the `E`-restriction
of Proposition `P:cameron-spatial-map` (a stated upstream fact, not re-derived
here). This is exactly the unchanged proof as asserted.

---

## L:uniform-mean-spatial-tails

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (new proof adds only six paragraph/step
  headings and two explanatory sentences; all mathematical content matches)
- New explanations: JUSTIFIED
- Evidence: reconstructed below.

**Step 1 (translations).** In the covariance Fourier isometry, `τ_h` multiplies
by `e^{-iξ·h}`; dominated convergence on tests plus density/isometry gives strong
continuity of the isometries on `H_sp`, preserving the real subspace.

**Step 2 (translation error).** Using `|e^{-it}-1| ≤ |t|` and `≤2`, one has
`|e^{-it}-1| ≤ 2 min(1,|t|^β)` for `0<β<1` (here `β = 1/2-s < 1/2`). Combining
with `|ξ|^β⟨ξ⟩^s ≤ ⟨ξ⟩^β⟨ξ⟩^s = ⟨ξ⟩^{1/2}`, the pointwise check
`min(1,|ξh|^β)⟨ξ⟩^s ≤ min(1,|h|^β)⟨ξ⟩^{1/2}` holds in both regimes
(`|ξh|≤1` uses the second inequality; `|ξh|≥1` uses `⟨ξ⟩^{-β}≤|h|^β`), giving
`‖τ_hf-f‖_{H^s} ≤ 2 min(1,|h|^β)‖f‖_{H^{1/2}}`.

**Step 3 (row translation).** With `f=η_Rz_1`, `g=η_RΛ^{-1}w_2`, the identity
`τ_h(fg)-fg = (τ_hf-f)τ_hg + f(τ_hg-g)` holds in `H_sp` (smooth factors first,
then the fractional product extension of Lemma `L:cameron-fractional-products`).
Each term is `≤ A_s·2min(1,|h|^β)M‖z_1‖·M‖w‖_E = 2A_sM²min(1,|h|^β)‖z_1‖‖w_2‖`;
summing two terms gives
`‖τ_h k_R-w-k_R‖ ≤ 4A_sM²min(1,|h|^β)‖z‖_E‖w‖_E`
`(E:uniform-mean-row-translation)`. Constant is fourfold, as asserted. This
checks the new sentence: “the fractional product bound therefore contributes
`2A_sM^2` twice.”

**Step 4 (heat averaging).** `∫p_ε(h)τ_hk dh` is a valid Bochner integral
(strongly continuous, bounded orbit in a separable Hilbert space). Gaussian
integration gives Fourier image `e^{-ε|ξ|²/2}k̂`, the stated `C_ε`. Integrating
`(E:uniform-mean-row-translation)` against `p_ε`:
`‖(I-C_ε)k‖ ≤ ∫p_ε(h)‖k-τ_hk‖dh ≤ 4A_sM²‖z‖‖w‖∫p_ε(h)min(1,|h|^β)dh`
`≤ 4A_sM² E|√εG_d|^β ‖z‖‖w‖ = M_h ε^{β/2}‖z‖_E‖w‖_E`, with
`M_h = 4A_sM²E|G_d|^β`. The variance of `p_ε` is exactly `ε`; no extra Fourier
normalization factor appears. Self-adjointness of `C_ε` in the row pairing gives
`‖T_R(I-C_ε)‖ ≤ M_h ε^{β/2}` `(E:uniform-mean-heat)`. This verifies the new
explanatory text on averaging `min(1,|h|^β) ≤ |h|^β` and the
self-adjoint transfer.

**Step 5 (projection).** `V` is the closed image of the covariance Fourier
isometry into `L²(μ)` with the fixed `(2π)^{d/2}` factor; no surjectivity or
spectral density is assumed. For real Schwartz `f` and real even smooth `χ_n`
(`=1` on `B̅_K`, `=0` outside `B_{K+1/n}`), `χ_nf̂` is the transform of a real
Schwartz function, hence in `V`. Dominated convergence against `|f̂|²μ` gives
`1_{|ξ|≤K}f̂ ∈ V`, including the charged boundary sphere. Density/contraction
extends to all of `V`; indicator multiplication is self-adjoint and idempotent,
pulling back to a real orthogonal `P_K` which may have infinite rank. All Fourier
multipliers commute.

**Step 6 (frequency tail).** On `|ξ|>K`,
`1-e^{-|ξ|²/(2K²)} ≥ 1-e^{-1/2}`, so
`‖(I-P_K)u‖² ≤ (1-e^{-1/2})^{-2}‖(I-C_{K^{-2}})u‖²` and hence
`‖(I-P_K)u‖ ≤ (1-e^{-1/2})^{-1}‖(I-C_{K^{-2}})u‖`. Applying the row heat bound at
`ε=K^{-2}` gives `‖(I-P_K)k_R(z,w)‖ ≤ M_f K^{-β}‖z‖‖w‖` with
`M_f = M_h/(1-e^{-1/2})`; self-adjointness of `P_K` yields
`(E:uniform-mean-frequency)`. The `(1-e^{-1/2})` denominator is exactly as
required. No density of `μ`, periodic state space, or finite rank is used.

---

## L:uniform-mean-tensor

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (new proof adds step headings and one
  explanatory sentence)
- New explanations: JUSTIFIED
- Evidence below.

**Step 1 (Gaussian moment).** For `v = Σ_j f_j⊗e_j`, `(e_j)` orthonormal, the
`H_0⊗G` norm squared is `Σ_j‖f_j‖²`; the covariance of `Σ_jγ_jf_j` is the
finite-rank operator with eigenvalues `λ_l`, whose squared norm has law
`Σ_lλ_lζ_l²`, independent standard `ζ_l`. For `L=Σ‖f_j‖²=Σλ_l>0`, Jensen on the
convex map `x↦x^{r/2}` (`r/2≥1`) with weights `λ_l/L` gives
`E‖Σγ_jf_j‖^r ≤ m_r(Σ‖f_j‖²)^{r/2}`; `L=0` is trivial.

**Step 2 (transfer and cancellation).** For fixed `t`, `Σ_jγ_jAf_j(t)` is a
scalar centered Gaussian with variance `Σ_j|Af_j(t)|²`; its `r`-th absolute
moment is `m_r(Σ|Af_j(t)|²)^{r/2}`. Tonelli gives
`m_r∫(Σ|Af_j(t)|²)^{r/2}dt = E‖AΣγ_jf_j‖^r_{L^r} ≤ ‖A‖^r m_r(Σ‖f_j‖²)^{r/2}`.
Canceling the positive `m_r` and taking `r`-th roots gives
`‖(A⊗I_G)v‖ ≤ ‖A‖‖v‖`; the new sentence correctly states that the common factor
`m_r` cancels and no dimension-dependent factor remains. Density of finite
tensors and Bochner completeness extend the map; the zero spaces are trivial.

**Step 3 (noncompactness).** For `Af≠0` and infinite orthonormal `(e_j)` in `G`,
`‖(A⊗I_G)(f⊗e_j)-(A⊗I_G)(f⊗e_k)‖ = ‖e_j-e_k‖_G‖Af‖_{L^r} = √2‖Af‖_{L^r}`
(`j≠k`), so the bounded sequence `f⊗e_j` has no norm-convergent subsequence.
Compact scalar `A` therefore does not force compactness of the tensor extension.
(Finite auxiliary Gaussians only were used.)

---

## P:uniform-mean-regulator

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (new proof adds step headings and one
  explanatory sentence)
- New explanations: JUSTIFIED
- Evidence below.

**Step 1 (projections).** `π_J⊗P_K` is self-adjoint idempotent contractive on
finite tensors, hence on the completion; so is `Q_{J,K}=I-π_J⊗P_K`.

**Step 2 (temporal tail).** If `ε_J=‖C_t(I-π_J)‖` did not tend to zero, we get
unit `v_J` with `‖C_t(I-π_J)v_J‖` bounded below on a subsequence. Since
`(I-π_J)v_J ⇀ 0` (pairing with `h` is `≤‖(I-π_J)h‖→0`), compactness of `C_t`
(norm-convergent subsequence) plus weak continuity forces the limit to `0`, a
contradiction. So `ε_J→0`. Lemma `L:uniform-mean-tensor` transfers this scalar
tail to Hilbert-valued time maps at no dimension cost.

**Step 3 (decomposition).**
`Q_{J,K} = (I-π_J)⊗I + π_J⊗(I-P_K)` is exact:
`(I-π_J)⊗I+π_J⊗(I-P_K) = I⊗I - π_J⊗P_K`.

**Step 4 (first term).** `T_R(I-π_J)⊗I = T_R(C_t(I-π_J)⊗I)`, giving bound
`M_0‖C_t(I-π_J)⊗I‖ ≤ M_0ε_J` by `L:uniform-mean-tensor`.

**Step 5 (intertwining and second term).** On finite tensors
`U(π_J⊗(I-P_K))(f⊗g) = (C_tπ_Jf)⊗(I-P_K)g = (I_{L^r}⊗(I-P_K))(C_tπ_J⊗I)(f⊗g)`;
continuity extends the identity. Then
`T_RU(π_J⊗(I-P_K)) = T_R(I_{L^r}⊗(I-P_K))(C_tπ_J⊗I)`, where the pointwise
factor `T_R(I-P_K)` has norm `≤M_fK^{-β}` by `(E:uniform-mean-frequency)`, and
`‖C_tπ_J⊗I‖ ≤ c_t` by the tensor lemma. Total:
`‖T_RQ_{J,K}‖ ≤ M_0ε_J + M_fc_tK^{-β}`, retaining both terms, the fixed `r`,
strong Bochner measurability (composition of the Bochner field `UΦ` with the
bounded linear compact-valued `T_R`), and compact values without any
uniform-radius compactness. The new explanatory sentence describing the first
(identity-in-space, small-in-time) and second (bounded-in-time, spatial error)
terms is accurate.

---

## P:uniform-actual-cameron

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (new proof reorganizes into Steps 1–5 and
  appends several explanatory sentences)
- New explanations: JUSTIFIED
- Evidence below.

**Step 1 (paths).** `Q_full` is an orthogonal projection on `H_W`, `T_{δ,m}` is
the original pullback isometry (`L:raw-block-inputs`); hence
`Var Y_m(f) ≤ ‖f‖²_{H_fast}`. Gaussian transfer
(`P:source-gaussian-transfer`) constructs the operator paths on the given `W`,
with finite path moments at fixed `R,B,δ,J,K`. Admissible exponent above `θ`
and constant stopping put the paths in the separable little `C^θ` closure; `L^2`
limits put every continuous linear coordinate in the first chaos of `W`.

**Step 2 (supported rows and covariance).** Every observed row, pulled back to
slow time, lies in `H_I` (`L:cameron-actual-residual`). For such a row `k`, with
`H_I = range(i_I)`,
`⟨Q_fullT_{δ,m}k,h⟩ = ⟨T_{δ,m}k,h⟩ - ⟨P_ret i_I^*T_{δ,m}k,i_I^*h⟩
= ⟨T_{δ,m}k,i_IQ_{J,K}i_I^*h⟩` since `i_I^*i_I=I` and `T_{δ,m}k∈H_I`.
Directions orthogonal to `H_I` are annihilated by `i_I^*`. Applying the completed
`J=0` upstream covariance identity to `Q_{J,K}i_I^*h` and restricting to `E`
gives `(E:uniform-actual-covariance)`. The amplitude is exactly
`g_δδ^{a/2} = δ^{(1-a)/2+a/2} = √δ`. Conjugation by `S_E` is norm-continuous on
compact operators (strong continuity of `S_E`, `S_E^*`), so the integral is a
compact-operator Bochner integral on `E`, identified for all times by
fixed-parameter `L²` continuity, dense states and rational times.

**Step 3 (free group bound).** In Bessel-unitary coordinates the matrix has
entries `cos(v|ξ|)`, `⟨ξ⟩sin(v|ξ|)/|ξ|`, `-|ξ|sin(v|ξ|)/⟨ξ⟩`, `cos(v|ξ|)`. For
`|v|≤B`: the upper off-diagonal is `≤√2B` (using `|sin(vk)|≤Bk` for `k≤1`,
`⟨k⟩/k≤√2` for `k≥1`); the lower and both diagonals are `≤1`; so the Frobenius
squared bound is `≤3+2B²` and `‖S_E(v)‖ ≤ √(3+2B²) ≤ 3B` for `B≥1`. Hence
`G_{B,E} = sup_{|v|≤B}‖S_E(v)‖ ≤ 3B`.

**Step 4 (primitive bound).** For `f(v) = S_E(-v)M_h(s_m+δv)S_E(v)` with
`M_h = T_R(Q_{J,K}i_I^*h)`, the standard primitive estimate on an interval of
length `≤B` gives, for the Hölder seminorm and the sup-norm respectively,
`‖∫_0^u f‖_{C^θ} ≤ G_{B,E}²[B^{1-1/r}+B^{1-1/r-θ}]‖f‖_{L^r(0,ℓ_m)}`; the affine
change of variables gives `‖f‖_{L^r(0,ℓ_m)} = δ^{-1/r}t_m` with
`t_m=‖M_h‖_{L^r(I_m;L(E))}`. So
`‖(Lh)_m‖_{C^θ} ≤ √δ C_{B,E}δ^{-1/r}t_m`,
`C_{B,E}=G_{B,E}²[B^{1-1/r}+B^{1-1/r-θ}]`. The primitive exponent `1-1/r>θ`
(parameters imply `r>1/(1-θ)`), constant stopping preserves the bound, and the
empty last block contributes zero.

**Step 5 (power mean).** For `n=N+1≥2` and exponent `r/p>1`,
`(Σt_m^p)^{1/p} ≤ n^{1/p-1/r}(Σt_m^r)^{1/r}`. The true partition gives
`Σt_m^r=‖M_h‖^r_{L^r(I)}`, and `δn=δ(⌊1/(δB)⌋+1)<1/B+δ<2/B`. The exact
`δ`-weighted norm gives
`‖Lh‖_{δ,p} ≤ δ^{1/p}√δ C_{B,E}δ^{-1/r}n^{1/p-1/r}‖M_h‖_{L^r}
= √δ C_{B,E}(δn)^{1/p-1/r}‖M_h‖_{L^r}`; since `p<r`,
`(δn)^{1/p-1/r} ≤ (2/B)^{1/p-1/r}`. Finally `‖M_h‖_{L^r} ≤ [M_0ε_J+M_fc_tK^{-β}]
‖h‖_{H_W}` by `(E:uniform-completed-mean)`. This is
`(E:uniform-actual-cameron-bound)`. Bound on the constant: 
`C_{B,E} ≤ (3B)²·2B^{1-1/r} = 18B^{3-1/r}`, exactly as the new text explains.

**Step 6 (Cameron norm).** With `H_seen` the closed span of the coefficient
tests, the first-chaos identification (`P:cameron-actual-embedding`) gives
`ker L = H_seen^⊥` and `‖Lh‖_{CM} = ‖P_seen h‖_{H_W}`. Taking the minimum-norm
preimage `P_seen h` (norm `≤‖h‖`) gives the Cameron embedding bound without an
inverse covariance or any finite-dimensional density.

**Closing qualifiers (both revisions).** The orthogonal `P_full`/`Q_full` fields
are independent; residual time blocks may remain correlated; the retained
spatial head may have infinite rank. The linear bounds give neither
growing-mask expected residual norms, nor concentration, nor conditioning over
the infinite sum, nor a moment upper theorem. These scope limits are correctly
preserved.

---

## AUDIT dispositions

- All five statements are textually unchanged in both revisions (old/new LF
  29–42, 70–88, 158–166/183–191, 215–231/257–273, 291–311/349–369).
- `L:uniform-mean-cutoff`: proof unchanged; reconstructed in full.
- `L:uniform-mean-spatial-tails`: new text is re-heading plus two correct
  explanatory sentences (“`2A_sM^2` twice”; averaging `min(1,|h|^β)≤|h|^β`).
- `L:uniform-mean-tensor`: re-heading plus one correct explanatory sentence
  (variance `Σ|Af_j(t)|²`, common `m_r`, cancellation).
- `P:uniform-mean-regulator`: re-heading plus one correct explanatory sentence
  (first/second term structure).
- `P:uniform-actual-cameron`: re-heading plus correct explanations of
  `(δn)^{1/p-1/r}`, `p<r` monotonicity, and `18B^{3-1/r}` from `G_{B,E}≤3B`.

No lost steps or qualifiers were detected in the rewrite. All five arguments
verify under the stated hypotheses, constants, domains (`E=H^{1/2}×H^{-1/2}`
only, not the constant `F` columns), normalizations, and conventions.

---

## Findings and limits

**Preservation conclusion.** The rewritten proofs preserve every logical step of
the originals; the new material is purely presentational (step headings) plus
routine explanatory restatements that are mathematically correct and add no
unsubstantiated claims. Cutoff, heat/frequency tails, tensor extension,
regulator two-term bound, and the Cameron embedding bound all reconstruct
cleanly.

**Pre-existing/contextual limits (not rewrite defects).** The target module
relies on unassigned upstream results whose proofs I did not re-derive:
`L:cameron-fractional-products` (fractional product bound with `A_s`),
`P:cameron-spatial-map` (compact values at fixed `R`), `P:cameron-temporal-map`
(compact `C_t:H_t→L^r(I)` for `2<r<2/a`), `L:raw-block-inputs` (pullback
isometry and `δ^{a/2}` Jacobian), `P:source-gaussian-transfer`, and
`P:cameron-actual-embedding` (the completed `J=0` covariance and first-chaos
Cameron identification). I checked that each target invocation meets the stated
application hypotheses (`s∈(α/4,1/2)`, `β=1/2-s`, `R≥1`, `2<r<2/a`, `p<2<r`,
`1-1/r>θ`, `δ<1/B`, `B≥1`); their internal proofs remain outside this assigned
scope and would require separate review.

**Matter-of-scope statements.** The closing paragraph’s disclaimer (no
concentration, conditioning, infinite-sum conditioning, or moment upper
theorem from these linear bounds) is retained verbatim; it coincides with the
task’s own warning and is not an overclaim. The fixed-`R` compactness is
correctly distinguished from uniform-radius claims. The projection `P_K` is
constructed on the actual covariance Fourier image `V⊂L²(μ)`, consistent with
“no surjectivity or spectral density assumed,” and the closed ball’s boundary
sphere is included by taking the pointwise limit of `χ_n`.

No lost steps/qualifiers, unresolved issues, or new defects were identified
within this read.
