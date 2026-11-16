# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro (deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

All ten assigned proof pairs were read as complete modules in both revisions. For each pair the unchanged statements, the complete original (OLD) proofs, and the rewrites (NEW) were reconstructed from checkable public equations. The NEW proofs mostly add structuring ("Step k"), sign/derivative bookkeeping, and explicit expansions of previously compressed steps; I found no new mathematical defect. The pre-existing proof structure is preserved; the normalization and localization conventions are carried over unchanged.

---

## L:gaussian-scalar-powers

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Weighted inequality** `E:gaussian-weighted-power`. For `v>0`, set `t=u/v`; the claim becomes `t^θ ≤ θt+1−θ`. With `φ(t)=θt+1−θ−t^θ`, `φ(1)=0` and `φ'(t)=θ(1−t^{θ−1})`; since `θ−1<0`, `φ'<0` on `(0,1)` and `φ'>0` on `(1,∞)`, so `φ≥0`. Continuity gives `t=0`; `v=0` uses `u^θ 0^{1−θ}=0 ≤ θu` because `1−θ>0`. OLD said “decreases to zero at one and then increases”; NEW spells out the sign of `φ'` explicitly (new LF 34–39), which is correct.
  2. **Integer-power consequence** `E:gaussian-integer-power`. Substitute `u=|x|^L`, `v=|y|^L`, `θ=q/L` for `0<q<L`: `(|x|^L)^{q/L}(|y|^L)^{1−q/L}=|x|^q|y|^{L−q}` with weights `q/L,(L−q)/L`. Endpoints are identities under `a^0=1`.
  3. **Finite Hölder**. Normalize the sequences by their `ℓ^m` and `ℓ^{m/(m−1)}` norms; a zero norm is trivial. Apply the weighted inequality with `θ=1/m` and sum.
  4. **Expectation bound**. `F=0 ⇒ Z=0` a.s.; otherwise apply the weighted inequality to `(Z/F,1)` with `θ=r∈(0,1)` and integrate to get `E Z^r ≤ F^r`.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The added “Step 1/2/3” and the derivative-sign discussion are faithful.
- Evidence: `E:gaussian-weighted-power`, `E:gaussian-integer-power`; OLD LF 30–46 vs NEW LF 30–65. The derivative calculation `φ'(t)=θ(1−t^{θ−1})` is checkable directly.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## L:gaussian-trace-bounds

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Trace word expansion**. In a `Y`-eigenbasis with real `λ_i` and `b_{ji}=̄{b_{ij}}`, the diagonal entry trick gives
     `Tr(BY^qBY^{L−q}) = Σ_{i,j}|b_{ij}|^2 λ_j^q λ_i^{L−q}`,
     which is real because `λ_j^qλ_i^{L−q}∈R` and `|b_{ij}|^2≥0`. NEW adds the intermediate-index explanation (new LF 86–93), which is accurate.
  2. **Power bound**. `λ_j^qλ_i^{L−q} ≤ |λ_j|^q|λ_i|^{L−q} ≤ (q/L)|λ_j|^L + (L−q)/L|λ_i|^L`. Interchanging `i,j` (allowed since `|b_{ij}|=|b_{ji}|`) makes the `|λ_j|^L` part equal to the `|λ_i|^L` part; the weights sum to one, so the whole sum is `Σ_{i,j}|b_{ij}|^2|λ_i|^L = Tr(B^2|Y|^L)`. No commutation of `B,Y` is used.
  3. **Diagonal of B**. With `d_i=D_{ii}≥0` and eigenvalues `θ_j`, write `D=U diag(θ)U^*`, so `d_i=Σ_j|U_{ij}|^2 θ_j` and row/column sums of `|U_{ij}|^2` are one. Convexity `t^m≥s^m+m s^{m−1}(t−s)` (true since `h(t)=t^m−s^m−m s^{m−1}(t−s)` has `h(s)=0`, `h'(t)=m(t^{m−1}−s^{m−1})`, so `h≥0`) gives `Σ_i d_i^m ≤ Σ_{i,j}|U_{ij}|^2 θ_j^m = Tr D^m`. NEW’s “row sums provide the weights, column sums give the equality after summing” matches.
  4. **Hölder step**. `Σ_i d_i|λ_i|^{2m−2} ≤ (Σ_i d_i^m)^{1/m}(Σ_i|λ_i|^{2m})^{(m−1)/m}` with the exponent identity `(2m−2)m/(m−1)=2m`; combine with step 3 to get `E:gaussian-trace-holder`.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. All added glosses (index accounting, convexity averaging, Hölder factor matching) are correct.
- Evidence: `E:gaussian-trace-word`, `E:gaussian-trace-holder`, `E:gaussian-integer-power`; OLD LF 64–92 vs NEW LF 83–129.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## P:finite-gaussian-matrix

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Integration by parts (IPB)**. For Hermitian `B_k`, `Y=Σg_kB_k`, `D=ΣB_k^2`. Density `e^{−g_k²/2}` has derivative `−g_k` times itself, so moving the derivative onto the polynomial gives `E[g_kP(g)]=E[∂_kP(g)]` with no boundary term; Gaussian decay dominates every polynomial moment. NEW (new LF 168–176) correctly explains the sign and boundary vanishing.
  2. **Hermitian moment**. `Tr Y^{2m}=Σ_k g_k Tr(B_kY^{2m−1})`; the product rule for `Y^{2m−1}` puts `B_k` at one of `2m−1` positions, giving `F=E Tr Y^{2m}=Σ_kΣ_{q=0}^{L}E Tr(B_kY^qB_kY^{L−q})`, `L=2m−2`. Each trace is real (eigenbasis of L:gaussian-trace-bounds).
  3. **Two bounds**. `F ≤ (2m−1)E Tr(D|Y|^{2m−2}) ≤ (2m−1)(Tr D^m)^{1/m} E(Tr|Y|^{2m})^{(m−1)/m} ≤ (2m−1)(Tr D^m)^{1/m}F^{(m−1)/m}`, using `Tr|Y|^{2m}=Tr Y^{2m}` (Hermitian) and the scalar expectation bound with `r=(m−1)/m∈(0,1)`. Dividing the positive fractional power and raising to `m` gives `E:finite-hermitian-gaussian`, `E Tr Y^{2m}≤(2m−1)^mTr D^m`. NEW’s statements that `D≥0`, `Tr|Y|^{2m}≥0`, and `0<r<1` are all checkable.
  4. **m=1 equality**. Independence gives `E Tr Y²=Σ_kTr B_k²=Tr D`, exactly.
  5. **Hermitian dilation**. `B_k=[[0,A_k],[A_k^*,0]]`, `Y=[[0,X],[X^*,0]]`, `D=diag(V_out,V_in)`. Squaring gives diagonal blocks, so `TrY^{2m}=Tr(XX^*)^m+Tr(X^*X)^m`. Cyclicity for compatible rectangles and `(XX^*)^m=X(X^*X)^{m−1}X^*` give `Tr(XX^*)^m=Tr(X^*X)^m=Tr((X^*X)^m)`. Hence `TrY^{2m}=2Tr(X^*X)^m` and `TrD^m=TrV_out^m+TrV_in^m`. Substituting and dividing by two produces `E:finite-gaussian-average` with `√(p−1)` (since `(2m−1)^{m/p}=√(p−1)` for `p=2m`; NEW’s factor-two tracking `TrY^{2m}=2Tr(X^*X)^m` is exact).
  6. **Maximum form**. For positive `V`, `‖V^{1/2}‖_{S_p}^p=Tr V^m`; the average is bounded by the maximum.
  7. **p=2 equality**. `E Tr X^*X=Tr V_in=Tr V_out`.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The added explanations of the differentiated-factor count, `D≥0`, `r∈(0,1)`, and the dilation block structure are all correct.
- Evidence: `E:finite-gaussian-average`, `E:finite-gaussian-maximum`, `E:finite-hermitian-gaussian`; OLD LF 123–180 vs NEW LF 160–249.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified; the external Tropp attribution is historical and not needed for the reconstruction.

---

## L:cutoff-factorization

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Peetre inequality** `E:cutoff-peetre`. From `⟨x⟩≤√2⟨y⟩⟨x−y⟩`, raising to `r≥0` gives the bound; for `r<0` interchange `x,y` and raise to `|r|`, using `⟨y−x⟩=⟨x−y⟩`. NEW (new LF 336–341) states this correctly.
  2. **Cutoff Fourier decay and lattice sum**. Compact smooth cutoffs have Schwartz Fourier transforms by integration by parts. For the lattice sum `E:cutoff-lattice-sum`, translate `y` into one cell (`|y|≤a√d/2`); for `|k|≥√d`, `|y−ak|≥a|k|−|y|≥a|k|/2`, then `⟨y−ak⟩≥⟨ak/2⟩≥min(1,a/2)⟨k⟩`, so the sum is controlled by `max(1,2/a)^N Σ⟨k⟩^{−N}`; dyadic shells contribute `C_d2^{j(d−N)}`, summable since `N>d`. NEW’s explicit geometric tail `Σ_{j≥0}C_d2^{j(d−N)}` is correct.
  3. **Mixed Schur bound**. For kernel `K(k,ξ)` with row/column integrals bounded by `M_1,M_2`, Cauchy–Schwarz plus Tonelli gives `‖K‖²≤M_1M_2`, valid with counting measure on one side and Lebesgue on the other.
  4. **P_ψ kernel**. `(P_ψu)_k=L^{−d/2}∫ψu e^{−iκ_k·x}dx`. By Parseval with `f=ψ`, `g=ūe^{iκ_k·x}`, this equals `L^{−d/2}∫̂ψ(κ_k−ξ)û(ξ)dξ` with no residual `c_d`; weighting by `⟨κ_k⟩^r/⟨ξ⟩^r` yields exactly the displayed kernel. NEW’s remark about the cancellation of the Fourier constants is consistent (the `c_d`-normalized Fourier transform is unitary).
  5. **E_χ kernel**. For a finite torus polynomial, `̂(E_χv)(ξ)=Σ_k v_kL^{−d/2}̂χ(ξ−κ_k)`, giving the normalized kernel `L^{−d/2}(⟨ξ⟩/⟨κ_k⟩)^r̂χ(ξ−κ_k)` with no additional `c_d`.
  6. **Schur bounds**. Peetre bounds each kernel by `L^{−d/2}2^{|r|/2}⟨·⟩^{|r|}|̂ψ|` or the `̂χ` analogue, rapidly decreasing; one Schur quantity is the finite `L^1` integral, the other a translated lattice sum bounded by `E:cutoff-lattice-sum` with `a=2π/L`. This proves both directions of `E:cutoff-periodic-maps` for every real `r`.
  7. **Density and distributional identification**. Weighted Fourier truncation gives Schwartz density in `H^r(R^d)` and polynomial density on the torus; the extensions agree with the distributional pairings because each periodic coefficient pairs with a compact smooth test. NEW’s full-Lebesgue Schur remark covers whole-space multiplication by `χ`.
  8. **Recovery identity** `E:cutoff-whole-space-recovery`. For Schwartz `u`, the partial sums of the periodic Fourier series of `ψu` converge smoothly on the cube; applying `E_χ` gives `χ` times the partial sums. Rapid coefficient decay gives convergence in `H^{σ+γ}(T_L)`, hence in `H^σ(T_L)`; boundedness of `E_χ` gives convergence of images to `E_χI_γP_ψu`. Smooth convergence on `supp χ` gives distributional convergence to `χψu=χu`; Sobolev convergence implies distributional convergence, so the two limits coincide. Schwartz density extends to `H^{σ+γ}(R^d)`.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The expanded five-step organization and the coefficient/alias bookkeeping are correct.
- Evidence: `E:cutoff-peetre`, `E:cutoff-lattice-sum`, `E:cutoff-periodic-maps`, `E:cutoff-whole-space-recovery`; OLD LF 238–311 vs NEW LF 307–467.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read. Note: this reconstruction does not certify the unassigned upstream wave operator modules; the cutoff map boundedness was verified directly here.

---

## P:cutoff-singular-values

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Factorization**. `K_{χ,σ,γ}=Λ^σE_χI_γP_ψΛ^{−σ−γ}` from `E:cutoff-whole-space-recovery`.
  2. **Finite-rank approximation**. On the torus `I_γ` is diagonal with entries `⟨κ_k⟩^{−γ}`; `Q_n` retaining `|k|_∞≤n` has rank `(2n+1)^d` and `‖(1−Q_n)I_γ‖≤[1+(2π/L)²(n+1)²]^{−γ/2}→0`, because outside the retained cube `|κ_k|≥(2π/L)(n+1)`. NEW’s explanation of the weight ratio `⟨κ_k⟩^σ/⟨κ_k⟩^{σ+γ}=⟨κ_k⟩^{−γ}` is correct. Setting `K_n=Λ^σE_χQ_nI_γP_ψΛ^{−σ−γ}` gives finite-rank operators with `‖K−K_n‖→0`, hence compactness.
  3. **Index–rank matching**. With `M=‖E_χ‖‖P_ψ‖` (the outer Bessel maps are unitary), for `j≥3^d`, `n=⌊j^{1/d}/4⌋` gives `(2n+1)^d≤(j^{1/d}/2+1)^d<j` and `‖K−K_n‖≤M(2L/π)^γj^{−γ/d}`. For rank-`<j` `F`, `s_j(K)≤‖K−F‖` via the first-`j` right singular subspace meeting `ker F`. For `j<3^d`, `s_j(K)≤‖K‖≤M`.
  4. **Constant and summation**. `C_{χ,σ,γ,d}=M max(3^γ,(2L/π)^γ)`; `Σ_j j^{−pγ/d}<∞` iff `pγ>d`.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The added strict-rank and weight-ratio details are correct.
- Evidence: `E:cutoff-singular-values`; OLD LF 325–368 vs NEW LF 481–557.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## P:compact-two-envelopes

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Block form**. With `J_0(u,v)=(Λ^{1/2}u,Λ^{−1/2}v)`, `P_χ=J_0D_χJ_0^{-1}=diag(A_{1/2},A_{−1/2})` where `A_σ=Λ^σχΛ^{−σ}`. `χ` real multiplication is self-adjoint and `Λ^σ` is self-adjoint, so `A_σ^*=A_{−σ}`, hence `P_χ^*=diag(A_{−1/2},A_{1/2})=UP_χU` for the swap.
  2. **Swap/factor identity**. `D_γ` commutes with the swap, so `K_in=P_χ^*D_γ=UP_χUD_γ=UK_outU`.
  3. **Compactness/Schatten membership**. `K_out=diag(K_{χ,1/2,γ},K_{χ,−1/2,γ})`; direct-sum singular values form the multiset union, giving the displayed sum of `S_p`-norms, finite when `pγ>d`. NEW’s block-diagonal adjoint-times-self explanation is correct.
  4. **Trace identity**. For compact `K`, nonzero eigenvalues of `KK^*` and `K^*K` correspond (on an eigenspace `K^*Kx=λx` with `λ>0`, `Kx` is a `KK^*`-eigenvector of eigenvalue `λ` and `K/√λ` is an isometry); zeros contribute nothing. Thus `Tr(B_out)^{p/2}=Tr(B_in)^{p/2}=‖K_out‖_{S_p}^p`. NEW’s expanded inverse-isometry explanation is correct.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: `E:compact-balanced-cutoff`, `E:compact-two-factors`, `E:compact-envelope-traces`; OLD LF 412–439 vs NEW LF 601–657.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## L:compact-positive-order

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Compactness of A^{1/2}**. For finite spectral projections `Q_n` of compact positive `B`, `‖(1−Q_n)A^{1/2}‖²=‖(1−Q_n)A(1−Q_n)‖` by the C² identity `‖T‖²=‖TT^*‖`; the congruence `(1−Q_n)A(1−Q_n)≤(1−Q_n)B(1−Q_n)` follows from `A≤B`, and positive-order implies norm-order. The tail tends to zero, so `A^{1/2}` is compact and `A=A^{1/2}A^{1/2}` is compact. NEW’s equality/inequality glosses are correct.
  2. **Eigenvalue comparison**. Courant–Fischer/min-max: `λ_j(A)=sup_{dim L=j}inf_{x∈L,‖x‖=1}⟨Ax,x⟩`; comparing pointwise Rayleigh quotients preserves the inequality, hence `λ_j(A)≤λ_j(B)` including zero padding. NEW’s zero-eigenvalue counting and infimum/supremum monotonicity are correct.
  3. **Trace powers**. For `t≥1`, scalar monotonicity `λ_j^t≤λ_j'`, summed and passed to the increasing limit, gives `E:compact-positive-trace`; no operator `A^t≤B^t` is asserted (explicitly retained in NEW).
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: `E:compact-positive-trace`; OLD LF 455–472 vs NEW LF 673–719.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## P:localized-finite-variance

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Output variance envelope**. From `P_χZ_l=Z_l` and `Z_l=Z_lP_χ`, `V_out=P_χV_outP_χ^*`; positive congruence applied to `V_out≤CD_γ²` gives `V_out≤CP_χD_γ²P_χ^*=CB_out`. Right localization gives `V_in=P_χ^*V_inP_χ≤CB_in`. NEW’s congruence explanation is correct.
  2. **Trace bounds**. `B_out,B_in` are compact with finite `Tr(B_{·})^{p/2}=‖K_out‖_{S_p}^p`. Applying L:compact-positive-order with `t=p/2` and scaling by `C` yields `TrV_out^{p/2},TrV_in^{p/2}≤C^{p/2}‖K_out‖_{S_p}^p`. `C=0` is immediate.
  3. **Individual summands**. `Z_lZ_l^*≤V_out` because subtracting one positive summand leaves a positive sum. Hence `Z_lZ_l^*` is compact; `‖(1−Q_n)Z_l‖²=‖(1−Q_n)Z_lZ_l^*(1−Q_n)‖→0` makes `Z_l` compact. `s_j(Z_l)²=λ_j(Z_lZ_l^*)≤λ_j(V_out)`, so raising to `p/2` and summing gives `Z_l∈S_p` with `‖Z_l‖_{S_p}^p≤TrV_out^{p/2}`. NEW’s expansions (positive summand subtraction, finite-rank approximants, `p/2` exponent conversion) are correct.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: `E:localized-finite-hypotheses`, `E:localized-two-envelopes`, `E:localized-trace-bounds`; OLD LF 493–511 vs NEW LF 740–779.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## C:finite-gaussian-operators

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Compressed variances**. `Z_{l,n}=Π_nZ_lΠ_n`, `X_n=Σg_lZ_{l,n}`. `Σ_lΠ_nZ_lΠ_nZ_l^*Π_n≤Π_nV_outΠ_n` because the difference `Σ_lΠ_nZ_l(1−Π_n)Z_l^*Π_n` has quadratic form `‖(1−Π_n)Z_l^*Π_nx‖²≥0` (NEW’s explanation is exact); the input inequality is the adjoint version. `λ_j(Π_nVΠ_n)≤λ_j(V)` for positive compact `V` follows because `j`-dimensional subspaces of `ranΠ_n` form a subset of all subspaces. Hence both compressed variance trace powers are bounded by `C^{p/2}‖K_out‖_{S_p}^p`.
  2. **Finite matrix bound**. Applying P:finite-gaussian-matrix with `p=2m`, the average inequality gives `E‖X_n‖_{S_p}^p≤(p−1)^{p/2}(TrV_{out,n}^{p/2}+TrV_{in,n}^{p/2})/2≤(p−1)^{p/2}C^{p/2}‖K_out‖_{S_p}^p`, since the average of two quantities already ≤ the target adds no factor two (NEW states this explicitly).
  3. **Norm convergence of compressions**. `Π_n→I` strongly and `X` compact give `Π_nXΠ_n→X` in operator norm, via a finite-rank intermediate and `‖Π_n‖≤1`.
  4. **Singular-value Lipschitz/fatou**. `s_j(A)=inf_{dim L<j}sup_{v∈L^⊥,‖v‖=1}‖Av‖`; NEW’s derivation (upper bound by the first `j−1` right singular subspace, lower bound by a unit vector in the first `j` right singular subspace orthogonal to any `L`) is correct. Triangle inequality inside the supremum and infimum gives `s_j(A)≤s_j(B)+‖A−B‖`, so `s_j(X_n)→s_j(X)`. Fatou on the nonnegative sum gives `‖X‖_{S_p}^p≤liminf_n‖X_n‖_{S_p}^p`; combining with the uniform bound and Fatou in probability proves `E:finite-gaussian-operator-bound` and almost-sure finiteness.
  5. **Measurability**. Finitely many Gaussian coordinates change `X` continuously in operator norm; the Lipschitz property makes each `s_j` continuous; partial sums of nonnegative `p`th powers are measurable and their increasing (possibly infinite) limit is measurable. No `S_p`-Bochner convergence is assumed.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. All added details (positive difference terms, singular-value min-max lower bound, continuity/measurability) are correct.
- Evidence: `E:finite-gaussian-compression-bound`, `E:finite-gaussian-operator-bound`; OLD LF 528–572 vs NEW LF 796–873.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## P:cutoff-boundary-tests

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Rank-one witness**. Choose nonzero real `v,f∈C_c^∞` supported in the plateau, `̃v=(Λ^{1/2}v,0)`, `̃w=(Λ^{−1/2}f,0)`. Then `P_χ̃v=̃v` (since `A_{1/2}Λ^{1/2}v=Λ^{1/2}χv=Λ^{1/2}v`) and `P_χ^*̃w=̃w`, so `Zx=⟨x,̃w⟩̃v` satisfies `P_χZ=Z=ZP_χ`. Its variances are `‖̃w‖²̃v⊗̃v^*` and `‖̃v‖²̃w⊗̃w^*`.
  2. **Finite localising constant**. `|⟨x,a⟩|=|⟨D_γx,D_γ^{-1}a⟩|≤‖D_γx‖‖D_γ^{-1}a‖` by self-adjointness of `D_γ` and Cauchy–Schwarz; applied to the two Schwartz vectors `a=̃v,̃w` gives the displayed finite `C`. NEW’s equality and Cauchy–Schwarz attributions are correct.
  3. **Non-compactness of `Λ^{−γ}`**. For `f` with nonzero Gaussian Fourier transform, `g=Λ^{−γ}f` is nonzero Schwartz; translations of inputs map to translations of `g`. Plancherel gives `⟨T_hg,g⟩=∫e^{−iξ·h}|ĝ(ξ)|²dξ=c_d^{-1}̂(|ĝ|²)(h)`, tending to zero by Riemann–Lebesgue/Schwartz decay (since `|ĝ|²` is Schwartz). Choosing a large spacing makes distinct translates `‖g‖`-separated while all inputs have equal norm, so no Cauchy subsequence exists and `Λ^{−γ}` is not compact. NEW’s remark that the multiplier commutes with translations is correct.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: OLD LF 588–628 vs NEW LF 889–942; the witness and translation estimates are reproduced above.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## AUDIT dispositions

| Label | Old | New | Reconstruction | Preservation | New explanations |
|---|---|---|---|---|---|
| L:gaussian-scalar-powers | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| L:gaussian-trace-bounds | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| P:finite-gaussian-matrix | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| L:cutoff-factorization | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| P:cutoff-singular-values | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| P:compact-two-envelopes | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| L:compact-positive-order | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| P:localized-finite-variance | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| C:finite-gaussian-operators | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |
| P:cutoff-boundary-tests | COMPLETE | COMPLETE | COMPLETE | PRESERVED | JUSTIFIED |

---

## Findings and limits

The NEW revision rewrites the ten proofs by adding step structure and spelling out previously implicit sign, index, convexity, Schur, and min-max arguments. I reconstructed every assigned step publicly, including all unchanged OLD steps: scalar weighted powers and integer-endpoint conventions; the eigenbasis trace-word expansion without noncommuting operator-power order; the Gaussian integration-by-parts recursion, finite matrix words, Hermitian dilation and its exact factor two; the whole-space cutoff factorization at every real Sobolev order with the Fourier kernel constants, the mixed counting/Lebesgue Schur extension, and the recovery of periodic Fourier partial sums through the extended map; the rank/error singular-value bound and both variance-trace sides; the finite-dimensional congruence envelopes; the compact positive order/trace lemma; the localized variance compressions and their no-extra-factor-two average; the norm convergence, singular-value Lipschitz and Fatou steps; and the rank-one plateau witness with the translated-function non-compactness obstruction.

Comparison outcome: no changed statements, no dropped hypotheses, no altered constants, normalizations, domains, or limiting conventions. No new rewrite defect was found; the additions are explanatory and mathematically correct on the same hypotheses. Pre-existing concerns are limited to the external Tropp attribution (historical, not needed for the proof) and the fact that the module explicitly does not construct infinite Gaussian series, time regularity, coefficient localization, or source/Young identification; those remain upstream results, and this review does not attempt to certify them. I did not use tools, renderer output, Lean correspondence, or any prior report; the verdict rests solely on the supplied OLD/NEW LaTeX.

The two explicitly required cutoff extension/identification passages were derived publicly in `L:cutoff-factorization` (kernel identification of `P_ψ` and `E_χ` in weighted Fourier variables) and `P:cutoff-singular-values` (factorization and recovery of `Λ^σχΛ^{−σ−γ}` through `E_χI_γP_ψ`), and were not treated as black boxes.
