# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro (deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

The NEW revision of `notes/integrated_gaussian_tubes.tex` adds a one-sentence roadmap and `Step 1/2/3/4` headings inside five of the eight proofs, and inserts two roadmap sentences into one more proof. The remaining two proofs (`L:tube-rayleigh-tail`, `L:tube-half-action`) are byte-for-byte unchanged. I compared every substantive sentence of all eight OLD and NEW proofs and their statements/definitions. No mathematical step, hypothesis, qualifier, or normalization was removed or altered. The added headings accurately summarize the deductions they introduce. I reconstruct the public working of all eight target proofs below; upstream/baseline results are used only under their stated hypotheses.

---

## P:tube-wiener-realization
Old reading: COMPLETE (L37–110). New reading: COMPLETE (L37–129). Public reconstruction: COMPLETE. Original-step coverage: no omissions, no lost qualifiers.

**Difference.** NEW inserts a roadmap ("We reconstruct the Gaussian variable from its finite original-noise coordinates... verify the measurable-norm condition") and Step 1–4 headings; the text inside each step matches OLD paragraph-for-paragraph. One new sentence at Step 4, "We verify the finite-dimensional tail criterion for the measurable norm," is an accurate descriptor.

**Reconstructed working.**
- *Step 1 (finite regression).* Countable norming family `(ℓ_j)` in `B*` with `‖x‖=sup_j|ℓ_j(x)|` generates the Borel sets, so `X` is measurable in the completion of `σ(W(H))`. With ONB `(e_j)` and `G_j=σ(W(e_1),…,W(e_j))`, scalar conditional expectations extended by `L²` contraction give the Gaussian regression
  `X_j=E[X|G_j]=Σ_{l≤j}W(e_l)Ce_l` (`E:tube-finite-regression`), since `E[X W(e_l)]=Ce_l` by the definition `Ch=E[XW(h)]`. Convergence `X_j→X` in `L²(B)` follows by the monotone class argument stated. This is correct: the regression formula is the standard finite first-chaos projection, and `E‖X‖²<∞` gives Bochner `L²`.
- *Step 2 (Cameron image).* `ℓ(Ch)=E[ℓ(X)W(h)]=E[W(k_ℓ)W(h)]=⟨k_ℓ,h⟩`. Hence `ker C={h:⟨k_ℓ,h⟩=0 ∀ℓ}=H_seen^⊥` (with `H_seen=span{k_ℓ}^-`), so `C` is injective on `H_seen` and `‖Ch‖_CM=‖P_seen h‖_H`. This is the first-Wiener-chaos Cameron norm in `E:tube-cameron-space`; no inverse covariance or RN derivative is used.
- *Step 3 (support, Radon, full support).* `X_j∈E_0`, `X_j→X` in `L²`, a.s. subsequence ⇒ `X∈E_0` a.s. Tightness: cover by finite unions of radius-`2^{-j}` balls with mass `>1-ε2^{-j-1}`; intersection is closed, totally bounded, complete ⇒ compact; this, plus metric regularity, gives a Radon law. Full support: tail `X-X_j` has labels `(I-P_j)k_ℓ ⊥ e_1,…,e_j`, so it is independent of the finite sum; given `h,ε`, choose `j` with `‖CP_jh-Ch‖<ε/3` and `P(‖X-X_j‖<ε/3)>0`; the finite centered Gaussian sum has positive mass in every ball about `CP_jh` (preimage under the finite linear map contains an open ball about `P_jh`); independence makes every ball about `Ch` positive. This is valid.
- *Step 4 (measurable norm).* For `V_j=span{P_seen e_l:l≤j}` and any finite orthonormal `(h_k)⊂V_j^⊥`, `h_k⊥e_1,…,e_j`, so regression gives `E[X-X_j|W(h_k)]=Σ_kW(h_k)Ch_k` and Jensen gives `E‖Σ_k W(h_k)Ch_k‖²≤E‖X-X_j‖²`. Choose `j` with the right side `<ε³`; Markov ⇒ `P(‖Σ_kW(h_k)Ch_k‖>ε)≤ε` uniformly in the orthonormal family. Since `C:H_seen→H_CM` is isometric, `C(V_j)` is the excluded finite-dimensional Cameron subspace; this is exactly the standard measurable-norm tail condition on the dense Hilbert image with Banach completion `E_0`. Characteristic functional `E e^{iℓ(X)}=exp(-‖k_ℓ‖²/2)` finishes the abstract Wiener identification. Zero law is handled.

Argument preservation: PRESERVED. New explanations: JUSTIFIED (roadmap and headings match the deductions). Evidence: `E:tube-finite-regression`, `E:tube-cameron-space`; the Markov constant `ε³/ε²=ε` is the correct measurable-norm normalization; the characteristic functional is the standard isonormal one (no Fourier inversion factor is introduced). Pre-existing concern: reliance on the countable-norming-family Borel-generation fact and on a.s.-subsequence for the support, both standard and stated as such; none flagged as a defect.

---

## L:tube-closed-geometry
Old reading: COMPLETE (L148–184). New reading: COMPLETE (L167–215). Public reconstruction: COMPLETE. Original-step coverage: no omissions, including the `r=0` and `μ(A_δ)=1` (`â=+∞`) cases.

**Difference.** NEW inserts a roadmap ("compact control images... attains every finite infimal radius... exact covariance scale") and Step 1/Step 2 headings; content is the same.

**Reconstructed working.**
- *Step 1 (closedness, attainment).* `M_δ` compact ⇒ `M_δ(B_H(r))` is compact (closed ball weakly sequentially compact in separable Hilbert; image norm-convergent along a subsequence; scalar testing identifies the limit). `A_δ` closed + compact image ⇒ `T_r=A_δ+M_δ(B_H(r))` closed: extract the compact component, pass the residual into closed `A_δ`. Membership `x∈T_r ⇒ d_δ(x)≤r` is trivial; conversely `d_δ(x)≤r` gives `h_j`, `‖h_j‖≤r+1/j`, with `x-M_δh_j∈A_δ`; weak subsequence `h_j⇀h`, `‖h‖≤liminf‖h_j‖≤r`; compactness forces `M_δh_j→M_δh`; closedness of `A_δ` gives `x∈T_r`. This also covers `r=0`, proving least finite-radius attainment, and closed sublevels give lower semicontinuity (hence Borel measurability). This is correct.
- *Step 2 (exact Cameron scale + isoperimetry).* Nonzero law ⇒ `b_δ=2E‖X‖>0`; Markov gives `μ(A_δ)≥1/2`. Since `C=√δ M_δ` and `C` kills `H_seen^⊥`, the Cameron unit ball is `K=C(B_H(1))=√δ M_δ(B_H(1))`, and `M_δ(B_H(r))=rM_δ(B_H(1))`, so `T_r=A_δ+(r/√δ)K`. These are Borel enlargements (closed). The imported Friz–Hairer theorem applies to the realization of `P:tube-wiener-realization`, giving `μ((A+tK)^c)≤Φ̄_N(â+t)`. With `t=r/√δ≥0`, `â=Φ_N^{-1}(μ(A_δ))≥0` (since `μ(A_δ)≥1/2`), and `Φ̄_N(y)≤e^{-y²/2}` for `y≥0`, one gets `P(d_δ(X)>r)≤e^{-(â+r/√δ)²/2}≤e^{-r²/(2δ)}`. Tail →0 gives finiteness a.s.

Argument preservation: PRESERVED. New explanations: JUSTIFIED. Evidence: the key identity `K=√δ M_δ(B_H(1))` is checked; the enlargement parameter `t=r/√δ` is exactly what converts `e^{-t²/2}` into the `δ`-scale tail `e^{-r²/(2δ)}`. Pre-existing concern: none identified within this read; the imported isoperimetric theorem itself is external and is not re-certified, but its application hypotheses (Borel `A`, `μ(A)>0`, abstract Wiener realization, `t≥0`) are all verified in the target proof.

---

## P:tube-rayleigh-transfer
Old reading: COMPLETE (L208–235). New reading: COMPLETE (L239–271). Public reconstruction: COMPLETE. Original-step coverage: no omissions; open/closed/zero endpoints and the `{d_δ=∞}` null event are retained.

**Difference.** NEW adds one roadmap sentence ("We compare upper-level probabilities... treating both open and closed endpoints") before the body; the body is identical.

**Reconstructed working.**
- Rayleigh density `(r/δ)e^{-r²/(2δ)}` has survival `e^{-r²/(2δ)}`: substitution `u=r²/(2δ)` gives mass 1 and tail `e^{-c²/(2δ)}`. (Explicit check.)
- Since `G` is nondecreasing, `{r:e^{G(r)/δ}>t}` is an upper interval (empty, `[c,∞)`, or `(c,∞)`, including the whole halfline). Open endpoints are bounded directly by `E:tube-attained-radius`; at a positive closed endpoint `c`, `P(d_δ(X)≥c)=lim_{s↑c}P(d_δ(X)>s)≤e^{-c²/(2δ)}=P(R_δ≥c)`, using `{d≥c}=∩_{s<c}{d>s}` and Rayleigh having no atoms; at `c=0` both probabilities are 1. The null event `{d_δ=∞}` is handled by setting `e^{G(d_δ)/δ}=1`. Layer cake / Tonelli therefore orders `E e^{G(d_δ(X))/δ}≤E e^{G(R_δ)/δ}=∫(r/δ)e^{(G(r)-r²/2)/δ}dr`, even with jumps or infinite expectations.
- Least-radius attainment gives `X∈T_{d_δ(X)}`, so `F(X)≤G(d_δ(X))` by hypothesis ⇒ `E e^{F(X)/δ}≤∫…`. Zero law: `F(0)≤G(0)≤G(r)` (monotone), so `e^{F(0)/δ}≤e^{G(0)/δ}≤E e^{G(R)/δ}`; `F(0)` need not be zero. Correct.

Argument preservation: PRESERVED. New explanations: JUSTIFIED. Evidence: the closed-endpoint passage `P(d≥c)=lim_{s↑c}P(d>s)` is the correct monotone-continuity identity; the layer cake integrand for the Rayleigh side recovers the exact density `(r/δ)e^{-r²/(2δ)}`. Pre-existing concern: none identified; the non-selection of a measurable control/residual is explicitly stated and is legitimate because of least-radius attainment.

---

## P:tube-actual-law
Old reading: COMPLETE (L283–327). New reading: COMPLETE (L319–379). Public reconstruction: COMPLETE. Original-step coverage: no omissions; the Gaussian hypotheses, compactness, covariance scale, and radius decay are all reconstructed.

**Difference.** NEW inserts a roadmap and Step 1–3 headings; content unchanged.

**Reconstructed working.**
- *Step 1 (state space).* Compact operators on separable Hilbert form a separable operator-norm space; polygonal approximation gives separability of the little Hölder closure of zero-initial Lipschitz compact paths; constant stopping preserves it. `X_δ` is the `C^θ` limit of finite coefficient paths on the given single `W`; finite linear collections are `L²` limits of first-chaos Gaussians, hence jointly centered Gaussian; `E‖X_δ‖_{δ,p}²<∞` by `C:radius-covariance-residuals`; `H_I` is separable by `L:cameron-supported-tensor`. This gives a centered strongly measurable Gaussian tuple with finite second moment.
- *Step 2 (compact mean).* `T_R` is the `E`-compression of `P:cameron-full-mean` (compact into `L^{r_t}(I;K(E))` at fixed `R`), and `P:uniform-mean-regulator` gives `‖T_R‖≤C_mean=M_0‖C_t‖` uniformly in `R≥1`. Compact conjugation + affine time pullback + `1-1/r_t>θ` bound the primitive in `E:tube-actual-mean` from that field space into `B_δ`; constant stopping is bounded; composition with compact `T_R` makes `M_δ` compact. No uniform-radius compactness is asserted.
- *Step 3 (covariance and radius).* The rank-zero identity `E:cameron-actual-covariance` compressed to `E` via `P:symplectic-block-mean` gives `E:tube-actual-covariance`; the covariance scale is exactly `g_δ δ^{a/2}=δ^{1/2}=√δ`. Supported rows lie in `H_I` by the inside-`I` approximation of `L:cameron-actual-residual`; countable matrix coordinates and rational times identify the tuple in the closed first chaos `W(H_I)` on the same `W`; no block independence or time-indicator multiplier is used. Thus `P:tube-wiener-realization` applies. Finally `P:radius-mean-anchor` with zero residual projection gives `b_δ=2E‖X_δ‖_{δ,p}≤C_{Q,B,p}δ^{(1-a)/2-d/Q}→0` (`E:tube-typical-radius`), since the third condition `Q>2d/(1-a)` makes the exponent positive. Zero covariance gives zero paths/means directly.

Argument preservation: PRESERVED. New explanations: JUSTIFIED. Evidence: `g_δδ^{a/2}=√δ` is computed correctly; the radius substitution `R_δ=δ^{-1}+2≤3/δ` turns `g_δR^{d/Q}` into `δ^{(1-a)/2-d/Q}`; the compactness chain is compact∘bounded, so no uniform-radius compactness is used. Pre-existing concern: none identified; the compact values of the noise path are inherited from the Schatten-valued finite sums in the required upstream moments and are consistent with `L:symplectic-free` (which needs compact-valued paths).

---

## L:tube-actual-endpoint
Old reading: COMPLETE (L350–385). New reading: COMPLETE (L402–450). Public reconstruction: COMPLETE. Original-step coverage: no omissions; both identities and the fixed-`(δ,R,B)` scope are retained.

**Difference.** NEW inserts a roadmap and Step 1/Step 2 headings; content unchanged.

**Reconstructed working.**
- *Step 1 (continuity, off-null-set definition, lower bound).* Generic (linear) Young evolution is globally defined and locally Lipschitz in the `C^θ` driver; finite products, fixed-time free factors, norm and `log max(1,·)` preserve continuity, so `F_δ` is a finite continuous functional on all tuples (`B_δ`), independent of any Gaussian full-measure set. For every tuple of compact-valued zero-initial `C^θ` paths, the finite-product assertion of `L:symplectic-free` (`E:symplectic-compact-product-baseline`) gives `‖P_δ(x)‖≥‖S_E(Σ_mℓ_m)‖≥1`. Hence `max(1,‖P_δ(x)‖)=‖P_δ(x)‖`.
- *Step 2 (global cocycle).* `L:raw-block-restart` in its no-deterministic-mean case applies to the same full input with base profile `η²`; the single regularized slow noise preserving `W` is pulled back by `T_{δ,0}` and `T_{δ,m}`; local restriction is a time shift by `mB`; sources are the limits at fixed `(N+1)B` and `B`. The cocycle gives the ordered physical `F`-product with the true remainder; `i:E→F` is a closed isometry, so restricting and using injectivity of `i` gives `P_δ(X_δ)=P_{δ,E}^R(L_δ,0)` (first identity in `E:tube-global-endpoint`). The lower bound then removes the maximum, and exponentiating gives `e^{F_δ(X_δ)/δ}=‖P_{δ,E}^R(L_δ,0)‖²`. No mask is commuted through a free group; blocks remain correlated. Zero covariance gives the free product `S_E(L_δ)`.

Argument preservation: PRESERVED. New explanations: JUSTIFIED. Evidence: the lower bound `‖P_δ(x)‖≥1` uses `L:symplectic-free` which is checked for compact zero-initial `C^θ` paths on `L(E)`; the second identity depends on `‖P_δ(X_δ)‖≥1`, which is established independently of Gaussian/hamiltonian assumptions. Pre-existing concern: the use of `L:raw-block-restart` with `i:E→F` relies on the `F`-flow restricting consistently to `E`; this is supplied by `P:constant-phase-driver` in the baseline and is used explicitly through the closed isometry `i`. Not a rewrite defect.

---

## P:tube-coarse-envelope
Old reading: COMPLETE (L414–473). New reading: COMPLETE (L479–550). Public reconstruction: COMPLETE. Original-step coverage: no omissions; every primitive/power-mean constant and the zero/empty-cell cases are reconstructed.

**Difference.** NEW inserts a roadmap and Step 1/Step 2 headings; content unchanged.

**Reconstructed working.**
- *Step 1 (primitive sum).* `G_B=sup_{|v|≤B}‖S_E(v)‖≥1`, `C_pr=G_B²[B^{1-1/r_t}+B^{1-1/r_t-θ}]`; `P:uniform-actual-cameron` gives `1≤G_B≤3B`, `C_pr≤18B^{3-1/r_t}`. The primitive estimate without `√δ` gives `h_m=‖(M_δΦ)_m‖_{C^θ}≤C_prδ^{-1/r_t}‖T_RΦ‖_{L^{r_t}(I_m)}`. Raising to `r_t` and summing over the true partition (including any empty last cell) gives
  `δΣ_mh_m^{r_t}≤C_pr^{r_t}Σ_m‖T_RΦ‖_{L^{r_t}(I_m)}^{r_t}=C_pr^{r_t}‖T_RΦ‖_{L^{r_t}(I)}^{r_t}≤(C_prC_mean)^{r_t}‖Φ‖_{H_I}^{r_t}` (`E:tube-primitive-sum`). Correct.
- *Step 2 (endpoint on each tube).* Young growth (`E:young-upper-refined-growth`) plus `d≤1+d^ν` and `(1+d)^ν≤2^{ν-1}(1+d^ν)` gives `log‖U_d(u,0)‖≤c_Y(1+‖d‖_{C^θ}^ν)` on `L(E)`. For `a∈A_δ`, `v_m=‖a_m‖`, `n=N+1`: `‖S_E(ℓ_m)U_m‖≤G_Bexp(c_Y(1+(v_m+h_m)^ν))`, and submultiplicativity + convexity give `F_δ(a+M_δΦ)≤2δn(logG_B+c_Y)+2^νc_YδΣ_m(v_m^ν+h_m^ν)`. (The bound is nonnegative, so the `max(1,·)` is dominated; equivalently the symplectic lower bound `‖P‖≥1` is available.)
- Weighted power means (valid for `p/ν≥1`, `r_t/ν>1`, nonnegative inputs, zero norms/empty cells, `δ>0`, `n≥2`, including `p=ν`):
  `δΣ_m v_m^ν≤(δn)^{1-ν/p}‖a‖_{δ,p}^ν`, `δΣ_m h_m^ν≤(δn)^{1-ν/r_t}(δΣ_m h_m^{r_t})^{ν/r_t}`.
  Using `δn≤2/B` and `E:tube-primitive-sum` yields `F_δ≤D_0+D_1b_δ^ν+D_2r^ν` with
  `D_0=2(2/B)(logG_B+c_Y)`, `D_1=2^νc_Y(2/B)^{1-ν/p}`, `D_2=2^νc_Y(2/B)^{1-ν/r_t}(C_prC_mean)^ν`.
  The `δ,r_t`-cancellation in `D_2` is verified (the `δ`-weight and the `δ^{-ν/r_t·r_t/ν}` powers cancel). `C_env=1+D_0+D_1+D_2` is independent of `δ,R`. The supremum sets are nonempty (`a=0,Φ=0`), so `G_δ(r)` is finite; monotone ⇒ Borel; `F_δ≤G_δ(r)` on each closed tube. Applying `P:tube-rayleigh-transfer` and `E:tube-global-endpoint` gives the operator moment bound. Zero law uses the transfer's direct case.

Argument preservation: PRESERVED. New explanations: JUSTIFIED. Evidence: all three `D_i` constants recomputed and match; the `(2/B)` powers arise from `δn≤2/B`; the `r_t` cancellation is exact; empty cells contribute zero and require no negative powers. Pre-existing concern: none identified; the measurability of the monotone supremum `G_δ` is by monotonicity (monotone functions are Borel), not by a measurable optimizer.

---

## L:tube-rayleigh-tail
Old reading: COMPLETE (L488–501). New reading: COMPLETE (L565–578). Public reconstruction: COMPLETE. Original-step coverage: no omissions.

**Difference.** None. NEW proof is identical to OLD (and NEW statement identical). No roadmap added.

**Reconstructed working.**
- For `r≥M`, the conditions `C≥0`, `1<ν<2`, `M>0`, `4C≤M^{2-ν}` give `r^{2-ν}≥M^{2-ν}≥4C`, hence `Cr^ν≤r²/4`; then `Cr^ν-r²/2≤-r²/4≤-M²/8-r²/8` (using `r≥M`). So `G(r)-r²/2≤A_0-M²/8-r²/8`.
- `-d/dr[4e^{-r²/(8δ)}]=(r/δ)e^{-r²/(8δ)}`, so `∫_M^∞(r/δ)e^{-r²/(8δ)}dr=4e^{-M²/(8δ)}`. Combining with `e^{(A_0-M²/8)/δ}` gives the prefactor/exponent `4e^{(A_0-M²/4)/δ}` (`E:tube-rayleigh-tail`).
- The cutoff exists because `2-ν>0`. On `[0,M]`, `G(r)≤A_0+Cr^ν≤A_0+CM^ν`, so that integral is finite. Applying with `A_0=C_env(1+b_δ^ν)`, `C=C_env` makes the operator-moment bound finite at fixed parameters (choose `M` with `4C_env≤M^{2-ν}`).

Argument preservation: PRESERVED. New explanations: JUSTIFIED (no new sentences). Evidence: the two `M²/8` contributions correctly combine into `M²/4`; the derivative identity is exact. Pre-existing concern: none identified.

---

## L:tube-half-action
Old reading: COMPLETE (L513–520). New reading: COMPLETE (L590–597). Public reconstruction: COMPLETE. Original-step coverage: no omissions.

**Difference.** None. NEW proof is identical to OLD.

**Reconstructed working.**
- Lower bound: `r=‖h‖` gives `g_J(‖h‖)≥J(h)`, so `g_J(‖h‖)-‖h‖²/2≥J(h)-‖h‖²/2`; sup over `h` bounds RHS by LHS (as extended reals).
- Upper bound: for `‖h‖≤r`, `J(h)-r²/2≤J(h)-‖h‖²/2`; taking the ball supremum then the radius supremum gives `sup_{r≥0}{g_J(r)-r²/2}≤sup_{h∈H}{J(h)-‖h‖²/2}`.
- Each ball is nonempty (`0` belongs) and has finite `J`-supremum (bounded above on every original ball), so no `∞-∞` subtraction occurs. No compactness/rank/density is used. Correct.

Argument preservation: PRESERVED. New explanations: JUSTIFIED. Evidence: the two inequalities are exact and match in the extended reals. Pre-existing concern: none identified.

---

## AUDIT dispositions

No `AUDIT` or `TODO` markers remain in either revision of this module; specifically, the `\LeanMarker` labels (`P:tube-rayleigh-transfer`, `L:tube-rayleigh-tail`, `L:tube-half-action`) are present in both OLD and NEW and are markers, not comments. No AUDIT-worthy issue requiring a disposition is found. The main cross-reference dependency, the imported Gaussian enlargement theorem (Friz–Hairer Theorem 11.6), is applied only through `L:tube-closed-geometry`, where its hypotheses are checked; that external theorem is not re-proven here and is not assigned for review.

## Findings and limits

- **Scope.** Exactly the eight assigned proof labels were reconstructed. Baseline modules (`integrated_cameron_mean`, `integrated_radius_anchor`, `integrated_uniform_mean`, `integrated_raw_block_lower`, `integrated_symplectic_phase`, `integrated_young_upper_foundation`, `integrated_constant_phase_young`, `integrated_exact_scaling`, model assumptions) were read as upstream context only and their proofs not counted or re-certified.
- **Rewrite defects.** None identified. The NEW revision is an explanatory split into numbered steps for `P:tube-wiener-realization`, `L:tube-closed-geometry`, `P:tube-rayleigh-transfer`, `P:tube-actual-law`, `L:tube-actual-endpoint`, `P:tube-coarse-envelope`, with no reordering, no deleted/edited mathematics, and no added sentence that conflicts with the deduction. `L:tube-rayleigh-tail` and `L:tube-half-action` are unchanged.
- **Statements/definitions.** All eight statements and the section-level hypotheses (compact `M_δ`, `√δ` covariance scale, closed Hilbert balls, `0<δ<1`, the tuple norm and parameter windows) are unchanged between revisions; the shifted statement LF ranges are due to inserted proof text only.
- **Pre-existing observations (not rewrite defects, not blocking).** (i) `L:tube-closed-geometry` imports the Gaussian enlargement theorem; the assignment correctly treats this as imported context, and the target proof verifies its application (Borel `A`, positive mass, abstract Wiener realization, `t=r/√δ≥0`, `â≥0`). (ii) The `‖P_δ(x)‖≥1` bound in `L:tube-actual-endpoint` and its reuse inside `P:tube-coarse-envelope` rely on compact-valued paths from the upstream Schatten-valued finite sums; the target module states `B_δ` as little `C^θ([0,B];K(E))`, so the hypothesis of `L:symplectic-free` is met. (iii) The monotone-envelope Borel measurability is by monotonicity, not by an optimizer; this is mathematically correct and explicitly claimed. None of these is introduced by the rewrite.
- **Verification points requested.** I checked the `√δ` scale (`g_δδ^{a/2}=√δ` in `P:tube-actual-law`; `K=√δM_δ(B_H(1))` in `L:tube-closed-geometry`), the compact closed-name control-ball images and least-radius attainment (`L:tube-closed-geometry`), Rayleigh domination for open/closed/zero endpoints and layer cake without `F(0)=0` (`P:tube-rayleigh-transfer`), the supported `H_I` labels on the same `W`, fixed-radius compact mean vs radius-dependent moment decay (`P:tube-actual-law`), the global cocycle with true remainder (`L:tube-actual-endpoint`), the coarse primitive/power-mean constants with zero/empty cases (`P:tube-coarse-envelope`), the exact Rayleigh tail prefactor/exponent (`L:tube-rayleigh-tail`), and the single-control half-quadratic supremum (`L:tube-half-action`). All are preserved and justified.
- **Not certified.** This review does not certify the imported Gaussian isoperimetric theorem, the baseline proofs' inner fidelity, Lean quotation correspondence, rendered pages, or whole-book truth.

No blocking issue and no partial reconstruction remain; the eight assigned proof pairs preserve their mathematics, and the new explanatory scaffolding is accurate.
