# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

## L:gaussian-scalar-powers

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The old proof (OLD 30–46) and new proof (NEW 30–74) establish `E:gaussian-weighted-power` by reducing to `t = u/v` and analyzing the derivative `θ(1−t^{θ−1})`; the new Step 1 spells out that `θ−1 < 0`, making the derivative negative below `1` and positive above, which is exactly the old monotonicity claim. Applying this with `u=|x|^L`, `v=|y|^L`, `θ=q/L` still gives `E:gaussian-integer-power`. The new text explicitly recovers the two coefficients `q/L` and `(L−q)/L`. The endpoint cases `q=0,L` remain identities, with the `a^0=1` convention retained. The finite Hölder step is unchanged, with the new explanation that the normalized `u`-sums and `v`-sums are both `1`, so the right side sums to `1/m+(1−1/m)=1`; this is correct. The expectation step is strengthened, not weakened: the new Step 3 justifies integrability of `(Z/F)^r` from `rZ/F+1−r` being integrable, since `EZ=F<∞`, and then multiplies by `F^r`. The `F=0` case is retained.

  Arithmetic check: for `θ=1/m`, `1−θ=(m−1)/m`, so the normalized product is `u^{1/m}v^{(m−1)/m}`, reproducing the normalized Hölder product; the constant `1/m+(1−1/m)=1` is exact.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## L:gaussian-trace-bounds

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The new proof (NEW 92–151) keeps the eigenbasis computation of the trace word exactly: `∑_{i,j}|b_{ij}|² λ_j^q λ_i^{L−q}`, using `b_{ji}=conj(b_{ij})`. The added explanation of the intermediate index `j` in `BY^qBY^{L−q}` is correct; the diagonal entry of the product is indeed summed over `j`, contributing `λ_j^q` and `λ_i^{L−q}`. Applying `E:gaussian-integer-power` gives the two weights `q/L` and `(L−q)/L`; interchanging `i,j` is justified by `|b_{ij}|=|b_{ji}|`, and both sums equal `∑|b_{ij}|²|λ_i|^L = Tr(B²|Y|^L)`, because the `i`th diagonal entry of `B²` in the `Y`-eigenbasis is `∑_j|b_{ij}|²`. No commutation of `B` and `Y` is used.

  For `D`: the new Step 2 explains that `d_i=∑_j|U_{ij}|²θ_j`, that the row sums supply convex weights, and that for fixed `i` the linear term `∑_j|U_{ij}|²(θ_j−d_i)` vanishes because the weights sum to one and `d_i` is the weighted mean. The convexity inequality `t^m ≥ s^m + ms^{m−1}(t−s)` averaged with `s=d_i` yields `d_i^m ≤ ∑_j|U_{ij}|²θ_j^m`, and summing over `i` gives `TrD^m`. The Hölder exponent check is exact: `(2m−2)m/(m−1)=2m`, so the second factor is `(Tr|Y|^{2m})^{(m−1)/m}`.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## P:finite-gaussian-matrix

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The new proof (NEW 182–281) preserves the Gaussian integration-by-parts identity `E[g_kP(g)] = E[∂_kP(g)]`. The added sign explanation is correct: the density derivative is `−g_kρ`, and moving the derivative to `P` changes the sign back to positive; the boundary term vanishes because a polynomial times a Gaussian density decays at infinity. The product-rule bookkeeping is correct: with `L=2m−2`, differentiating `Tr(B_kY^{2m−1})` gives `∑_{q=0}^{L}Tr(B_kY^qB_kY^{L−q})`, where `q` counts `Y` factors before the differentiated factor. The traces are real in the `Y`-eigenbasis, so `Re` can be dropped before applying `E:gaussian-trace-word`.

  The chain
  `F ≤ (2m−1) E Tr(D|Y|^{2m−2}) ≤ (2m−1)(TrD^m)^{1/m} E(Tr|Y|^{2m})^{(m−1)/m} ≤ (2m−1)(TrD^m)^{1/m}F^{(m−1)/m}`
  is unchanged. The new explanation that `r=(m−1)/m∈(0,1)` licenses the scalar expectation bound is correct. The `m=1` equality is unchanged and correct. The dilation block computation is preserved: `TrY^{2m}=Tr(XX^*)^m+Tr(X^*X)^m=2Tr((X^*X)^m)` via the rectangular cyclic identity `Tr((XX^*)^m)=Tr((X^*X)^m)`, so dividing by two is correct and no extra factor two enters the average. The `p=2` equality `ETr(X^*X)=TrV_in=TrV_out` is correct.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## L:cutoff-factorization

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The new proof (NEW 339–499) retains all three elementary facts (`E:cutoff-peetre`, compact-smooth Fourier decay, and `E:cutoff-lattice-sum`). The positive/negative-r Peetre treatment is correct: for `r≥0` one raises `⟨x⟩ ≤ √2⟨y⟩⟨x−y⟩` to `r`; for `r<0` one interchanges `x,y` and raises to `|r|`. The lattice-sum refinement `⟨y−ak⟩ ≥ ⟨ak/2⟩ ≥ min(1,a/2)⟨k⟩` is valid for `|k|≥1`, giving the stated `max(1,2/a)^N` constant; the dyadic bound `∑ C_d2^{j(d−N)}` converges because `N>d`.

  The weighted kernels are unchanged:
  `P_ψ`: `L^{-d/2}(⟨κ_k⟩/⟨ξ⟩)^r ψ̂(κ_k−ξ)`,
  `E_χ`: `L^{-d/2}(⟨ξ⟩/⟨κ_k⟩)^r χ̂(ξ−κ_k)`.
  The `c_d` cancellation is consistent with the stated unitary convention: `c_d²∫e^{iξ(y−x)}dξ=1` under the unitary inverse pair, so the second equality in the coefficient formula has no residual constant factor. The mixed Schur bound is correctly summarized: one side is an `L¹` integral in `ξ`, the other a translated lattice sum over `k`, bounded uniformly by `E:cutoff-lattice-sum`. The new Step 4 makes the extension-by-density explicit and state the distributional meaning of the periods; this addresses C1 fully. The new Step 5 proves `E:cutoff-whole-space-recovery` by first treating Schwartz `u` and then applying density, preserving both the strict-support alias elimination and all real orders; this addresses C2 fully. The detailed disposition is recorded below under AUDIT dispositions.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## P:cutoff-singular-values

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The proof (NEW 513–604) retains the factorization `K=Λ^σE_χI_γP_ψΛ^{−σ−γ}` and the diagonal inclusion tail bound `⟨κ_k⟩^{−γ}` with tail norm `[1+(2π/L)^2(n+1)^2]^{−γ/2}`. The rank `(2n+1)^d` is unchanged. The new arithmetic is correct: for `j≥3^d`, `n=⌊j^{1/d}/4⌋` gives `2n+1≤j^{1/d}/2+1<j^{1/d}`, hence `(2n+1)^d<j`; and `n+1>j^{1/d}/4` gives error at most `M(2L/π)^γj^{−γ/d}`. The rank-`<j` approximation argument for `s_j(K)≤||K−F||` is correctly explained by finding a unit vector in `kerF∩span(first j right singular vectors)`. The small-index case is correct: for `j<3^d`, `3^γj^{−γ/d}>1`, so `C=Mmax(3^γ,(2L/π)^γ)` covers `s_j(K)≤M≤Cj^{−γ/d}`. The `S_p` summation criterion `pγ>d` is unchanged.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## P:compact-two-envelopes

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The new proof (NEW 648–716) preserves the adjoint computation `A_σ^*=A_{−σ}` and the block formula `P_χ=diag(A_{1/2},A_{−1/2})`, `P_χ^*=diag(A_{−1/2},A_{1/2})=UP_χU`. The added explanation that moving Bessel powers through an inner product reverses the order of the three factors, while real multiplication by `χ` is self-adjoint, is correct and does not require evenness of `χ`. The factor identity `K_in=UK_outU` uses commutativity of the unitary swap with `D_γ`, correctly justified. The singular-value multiset union for a block diagonal operator is correct. The positive-eigenvalue multiplicity argument for `KK^*` and `K^*K` is correctly expanded: `K/√λ` carries the `λ`-eigenspace of `K^*K` into that of `KK^*` with preserved norm, and `K^*/√λ` is the inverse on the image. The trace identity `TrB_out^{p/2}=TrB_in^{p/2}=||K_out||_p^p` follows by summing squared singular values.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## L:compact-positive-order

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The key compactness step is unchanged:
  `||(1−Q_n)A^{1/2}||² = ||(1−Q_n)A(1−Q_n)|| ≤ ||(1−Q_n)B(1−Q_n)||→0`.
  The new Step 1 correctly identifies this as the `C^*C` norm identity, noting that no commutation of `Q_n` with `A` is needed because the two expressions are the norms of `T^*T` and `TT^*` for `T=A^{1/2}(1−Q_n)`. The finite-rank approximants `Q_nA^{1/2}` are correct. The new Step 2 gives the max-min formula including zero padding: if fewer than `j` positive eigenvalues exist, every `j`-dimensional subspace meets the orthogonal complement and the infimum is zero. The scalar monotonicity `λ_j(A)^t≤λ_j(B)^t` for `t≥1` is the correct substitute for the unavailable operator inequality `A^t≤B^t`, and the final sentence retains the explicit no-`A^t≤B^t` qualifier.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## P:localized-finite-variance

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The new proof (NEW 799–845) correctly derives the two localization congruences. From `P_χZ_ℓ=Z_ℓ` one gets `P_χZ_ℓZ_ℓ^*P_χ^*=Z_ℓZ_ℓ^*`; summing gives `V_out=P_χV_outP_χ^*`. From `Z_ℓ=Z_ℓP_χ` and its adjoint one gets `P_χ^*Z_ℓ^*Z_ℓP_χ=Z_ℓ^*Z_ℓ`, giving `V_in=P_χ^*V_inP_χ`. Positive congruence preserving order is correctly explained by testing on `P^*v`. The bounds `V_out≤CB_out`, `V_in≤CB_in` then follow from the compact envelopes, and `L:compact-positive-order` with `t=p/2` gives the two trace bounds. The new explanation that `p≥2` is exactly the condition `t=p/2≥1` is correct. The `C=0` case and the individual `Z_ℓ` compactness via `Z_ℓZ_ℓ^*≤V_out` and `Q_n`-approximation are unchanged.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## C:finite-gaussian-operators

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The new proof (NEW 862–955) preserves the compression `Z_{ℓ,n}=Π_nZ_ℓΠ_n`, the positive difference `∑Π_nZ_ℓ(1−Π_n)Z_ℓ^*Π_n`, and the input analogue. The new explanation of the max-min comparison is correct: on vectors in `ranΠ_n`, the quadratic forms of `Π_nVΠ_n` and `V` agree, and Rayleigh subspaces inside `ranΠ_n` form a subset of all subspaces, so `λ_j(Π_nVΠ_n)≤λ_j(V)`. The finite matrix bound then gives `E||X_n||_p^p≤(p−1)^{p/2}C^{p/2}||K_out||_p^p`.

  The two-passage argument is correctly separated. First, for each fixed Gaussian coordinate, `s_j(X_n)→s_j(X)` by the inf-sup singular-value formula and its Lipschitz property; counting-measure Fatou then gives `||X||_p^p≤liminf_n||X_n||_p^p`, allowing extended infinity. The norm convergence `Π_nXΠ_n→X` is correctly justified by the finite-rank approximation `X≈F` and uniform strong convergence on the ranges of `F` and `F^*`. Measurability is also correct: `g↦X(g)` is norm-continuous, each singular value is continuous by the Lipschitz bound, and the partial sums of `s_j^p` have a measurable increasing limit. Probability Fatou then yields `E||X||_p^p≤liminf_nE||X_n||_p^p`, and the uniform finite bound gives almost-sure finiteness. No `S_p`-Bochner convergence or factor two is added.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## P:cutoff-boundary-tests

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The new proof (NEW 971–1024) preserves the witness construction. For `v,f∈C_c^∞` inside the `χ=1` plateau, `P_χṽ=ṽ` and `P_χ^*w̃=w̃` follow because `χv=v` and `χf=f` under the appropriate Bessel factors; this correctly handles the nonlocal character of `Λ^{±1/2}v` and `Λ^{±1/2}f`. The rank-one variances are unchanged. The new explanation of the bound
  `|⟨x,a⟩| = |⟨D_γx,D_γ^{-1}a⟩| ≤ ||D_γx|| ||D_γ^{-1}a||`
  is correct: `D_γ` is self-adjoint, and `D_γ^{-1}a` belongs to `H` because `a` is Schwartz. This gives the finite common `C`.

  The noncompactness argument is preserved and clarified: `Λ^{−γ}` commutes with translations, so translates of `f` map to translates of `g=Λ^{−γ}f`. Plancherel gives `⟨T_hg,g⟩ = c_d^{-1}(|ĝ|²)^(h)`, which tends to zero because `|ĝ|²` is Schwartz. Choosing a large spacing makes the pairwise image distances at least `||g||`, so the images have no Cauchy subsequence.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern: none identified within this read.

## AUDIT dispositions

C1 (dense cores and extension/identification in the mixed counting/Lebesgue Schur argument): RESOLVED. The new proof of `L:cutoff-factorization` makes the two-stage argument explicit. Step 2 states the mixed Schur bound for a kernel with one counting side and one Lebesgue side, and says the proof is first carried out on finitely supported sequences and smooth compactly supported functions, then extended by density. Step 3 writes both `P_ψ` and `E_χ` as exact weighted kernels on those dense cores. Step 4 asserts Schwartz density in `H^r(R^d)` and finite-polynomial density in `H^r(T_L)` for every real `r`, so the bounded extensions are unique and agree with the kernel operators on the cores. The step also gives the distributional identification of the periodization coefficients for rough inputs. This closes the previously flagged gap; no unresolved audit-worthy issue remains.

C2 (recovery from periodic Fourier partial sums through the extended cutoff map for every real Sobolev order): RESOLVED. Step 5 of `L:cutoff-factorization` now does the series-limit passage explicitly: for Schwartz `u`, the periodic Fourier partial sums are finite torus polynomials; rapid decay of the coefficients gives convergence in `H^{σ+γ}(T_L)`, hence in `H^σ(T_L)`; boundedness of `E_χ` then gives convergence of the images to `E_χI_γP_ψu` in `H^σ(R^d)`. Simultaneously, smooth convergence on the support of `χ` shows the products with `χ` converge to `χψu=χu` as distributions, and Sobolev convergence implies distributional convergence for every real `σ`, so the two limits agree. Density of Schwartz functions in `H^{σ+γ}(R^d)` then proves the identity on the full domain for every real `σ` and `γ>0`. This resolves the previously flagged passage; no unresolved audit-worthy issue remains.

New flagged issues: none identified in this read.

## Findings and limits

- New defects introduced by the rewrite: none identified. The rewrite is a reorganization and expansion into numbered steps with explanatory sentences; no hypothesis, equation, quantifier, endpoint case, or sign was lost.
- Changed argument: none material. All ten proofs preserve the same mathematical strategy. The additions are justifications and bookkeeping details, and each addition checks out against the original hypotheses.
- Pre-existing concerns: none rising to audit level. Some wording remains terse, especially the `c_d` cancellation in `L:cutoff-factorization` and the initial statement of the mixed Schur bound, but in both cases the surrounding computation is correct and now sufficiently explicit.
- Harmless wording: the new “Step 1/Step 2” scaffolding and some repeated sentences are purely presentational; they do not alter mathematics. The extra detail on `P_{gs}` integration-by-parts sign, the factor-two trace, the dyadic lattice counting, and the two Fatou passages is correct and useful.
- Endpoints and zero cases: consistently retained across `L:gaussian-scalar-powers` (`q=0,L`, `v=0`, `F=0`), `P:cutoff-singular-values` (zero cutoff, `j<3^d`, `s_j=0`), `L:compact-positive-order` (zero padding), `P:localized-finite-variance` (`C=0`), and `C:finite-gaussian-operators` (extended infinity).
- Limits of this review: only the ten assigned proofs and the unchanged statements and module definitions supplied were read; the unproved remark, comments, and surrounding sections were not treated as additional assigned proofs. This is not a whole-book, Lean-correspondence, render/image, publication-acceptance, or human-verification review. Both revisions were read in raw source form. No PARTIAL/NOT_READ was necessary.