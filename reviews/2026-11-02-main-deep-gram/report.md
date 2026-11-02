# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. I found no false statements, sign errors, wrong constants, hidden hypotheses, misapplied identities, or invalid duality/attainment steps in PROOF194–198 (the five finite-Gram proofs in `integrated_positive_gram.tex`, AUDIT194–198 equivalent). Every identity, factor of two, boundary term, and constant was reconstructed by hand and checks out.

The only substantive unverifiable content is *upstream* of these five proofs: the intrinsic second-moment module cross-references lemmas/propositions (`L:uniform-E-lift`, `P:uniform-rate-averaging`, `P:variational-positive-scores`, `P:raw-block-original-lower`, `P:original-signed-point-upper`, `L:cameron-supported-tensor`, `L:uniform-mean-tensor`, `E:variational-positive-class`, etc.) that are absent from this snapshot. Per scope, that module is application context, not a proof target, so this does not lower the verdict on PROOF194–198, but it is an unresolved obligation I record explicitly.

## Noncritical findings

1. **PROOF194 (scalar equality case)** — the text asserts "If $\ell,t>0$, equality holds for $w=\ell/\sqrt t$." This is a correct *sufficient* condition but not a necessity statement; for $\ell<0$ no positive $w$ gives equality, and for $\ell=0,t>0$ the square is $wt>0$. Not an error — optional completeness only.

2. **Remark `R:gram-controls` "doubling the cost"** — the claim "maximum $3\,2^{-4/3}$ at $\phi=2^{-2/3}$" is correct for doubling the quadratic coefficient (score $2\sqrt\phi-\phi^2$), but the phrase "doubling the cost" is slightly ambiguous about which term is doubled. This is an auxiliary numerical control, not a proof step, and the arithmetic is right ($4\cdot2^{-4/3}-2^{-4/3}=3\cdot2^{-4/3}$).

3. **Lean coverage boundary** — the four Lean certificates (`scalar_sqrt_dual`, `gram_norm_square`, `active_upper_bound`, `half_weighted_entrywise_mono`) cover only the scalar/Hilbert identities, the active upper bound, and the entrywise quadratic monotonicity. The dual coercivity, Hessian calculus, infimum attainment, realization induction, and inf/max duality arguments remain unformalized analytic steps. The manuscript states this honestly in `R:gram-controls`; I verified these analytic steps independently and they are sound.

4. **Zero-label / empty-subset excluded from dual** — the proposition maximizes only over $A\subset\mathcal J$, correctly excluding subsets containing zero labels (for which $d_A=-\infty$). This is stated and used correctly; I flag it only because it is the kind of "hidden hypothesis" one must notice.

## Checked derivations

**PROOF194 — scalar/Hilbert identities (all verified):**
- $({\ell}/{\sqrt w}-\sqrt{wt})^2=\ell^2/w+wt-2\ell\sqrt t$ using $\sqrt{wt}=\sqrt w\sqrt t$ for $w>0,t\ge0$; valid for arbitrary real $\ell$; nonnegativity gives $2\ell\sqrt t\le\ell^2/w+wt$. Factor of two exact.
- Equality condition $\ell/\sqrt w=\sqrt{wt}\iff w=\ell/\sqrt t$ for $\ell,t>0$. Correct.
- $\|\Phi-z\|^2=\|\Phi\|^2-2\langle\Phi,z\rangle+\|z\|^2$ gives $\langle\Phi,z\rangle-\|\Phi\|^2/2=\|z\|^2/2-\|\Phi-z\|^2/2\le\|z\|^2/2$. Correct.
- $\|\sum_iw_ik_i\|^2=\sum_{i,j}w_iw_j\langle k_i,k_j\rangle=\sum_{i,j}w_iC_{ij}w_j$ by real bilinearity, any finite real $w_i$. Correct.

**PROOF195 — interior dual minimum (all verified):**
- Dropping nonnegative cross terms: $\sum_{i,j}w_iC_{ij}w_j\ge\sum_ic_iw_i^2$; hence $D_A^C(w)\ge\sum_i(\ell_i^2/w_i-b_iw_i+c_iw_i^2/2)$. Correct.
- Completing the square: $c_iw_i^2/4-b_iw_i=\frac{c_i}{4}(w_i-2b_i/c_i)^2-b_i^2/c_i\ge-b_i^2/c_i$, giving $D\ge\sum_i\ell_i^2/w_i+\frac14\sum_ic_iw_i^2-K_A$, $K_A=\sum_ib_i^2/c_i$. Constants correct.
- $L_A=d_0+K_A\ge\sum_i\ell_i^2+\frac14\sum_ic_i>0$. Coordinate bounds $\ell_i^2/L_A\le w_i\le\sqrt{4L_A/c_i}$ both follow from the two nonnegative remaining terms. Correct; box compact, strictly inside the open orthant (lower bound $>0$); sublevel $\{D\le d_0\}$ is closed in the box and contains $w^0=(1,\dots,1)$, so minimum attained; outside the sublevel values exceed $d_0$, so the minimum is global.
- Hessian $=\sum_i(2\ell_i^2/w_i^3)\xi_i^2+\sum_{i,j}\xi_iC_{ij}\xi_j$: first term strictly positive for $\xi\neq0$, second PSD (this is where PSD is used, distinct from entrywise nonnegativity used in coercivity). Strict convexity ⇒ uniqueness. Correct; handles singular $C$ because the $\ell_i^2$ barrier makes the Hessian positive definite.
- $\partial D/\partial w_i=-\ell_i^2/w_i^2-b_i+\sum_jC_{ij}w_j=0$ ⇒ $\sum_jC_{ij}w_j^A-b_i=\ell_i^2/(w_i^A)^2>0$. Sign and constants exact.

**PROOF196 — positive conic maximizer (all verified):**
- Active set $A(\Phi)=\{i:\langle\Phi,k_i\rangle>b_i\}\subseteq\mathcal J$ because $b_i\ge0$ forces $k_i\neq0$; threshold and below contribute zero. Correct.
- Weak-duality chain for $z=\sum_{i\in A}w_ik_i$: $2\sum_{i\in A}\ell_i\sqrt{t_i}\le\sum_{i\in A}(\ell_i^2/w_i+w_it_i)=\sum_{i\in A}\ell_i^2/w_i-\sum_{i\in A}b_iw_i+\langle\Phi,z\rangle$, then $\langle\Phi,z\rangle-\|\Phi\|^2/2\le\|z\|^2/2=\frac12\sum_{i,j\in A}w_iC_{ij}w_j$. Both steps exact; matches the Lean `active_upper_bound` instantiated on the active subset $A$. Hence $\mathfrak F_C(\Phi)\le d_{A(\Phi)}^C\le\max_{A\subseteq\mathcal J}d_A^C$. Correct.
- Dual-to-primal: at $\Phi_A=\sum_{j\in A}w_j^Ak_j$, stationarity gives $\sqrt{\langle\Phi_A,k_i\rangle-b_i}=\ell_i/w_i^A$, so both inequalities are equalities on the $A$-restricted score, which equals $d_A^C$. Omitted labels add only nonnegative terms, so $\mathfrak F_C(\Phi_A)\ge d_A^C$ (valid even when $d_A^C<0$). Combined with the upper bound, $\mathscr S(C)=\max_Ad_A^C$. Correct.
- Attainment without outside inactivity: for a maximizing nonempty $A^*$, $\mathfrak F_C(\Phi_{A^*})\ge d_{A^*}^C=\mathscr S(C)\ge\mathfrak F_C(\Phi_{A^*})$ forces equality, so $\Phi_{A^*}$ attains; empty case is $\mathfrak F_C(0)=0=d_\varnothing^C$. No concavity, minimax, or assumed outside inactivity used. Correct. No two-label counterexample found; the structure is closed.

**PROOF197 — real Gram realization (all verified):**
- Base case $\{0\}$. All-zero diagonal: quadratic form on $e_i+te_j$ equals $2tC_{ij}$, so $C=0$. Correct.
- Schur complement $B=A-vv^{\mathsf T}/c$ is PSD by testing on $(-v^{\mathsf T}y/c,y)$; computation gives $y^{\mathsf T}(A-vv^{\mathsf T}/c)y$. Correct.
- Reconstruction $k_1=(\sqrt c,0)$, $k_i=(v_i/\sqrt c,u_i)$: $\langle k_1,k_i\rangle=v_i$, $\langle k_i,k_j\rangle=v_iv_j/c+B_{ij}=A_{ij}$. Correct. No nonnegative-coordinate/complete-positivity assumption; $B$ may have negative entries. Correct.
- Independence: $C_{ii}=0\Rightarrow k_i=0\Rightarrow$ row vanishes; $\mathscr S(C)$ depends only on $C,\ell,b$ and $\mathcal J=\{i:C_{ii}>0\}$, all realization-independent. Correct.

**PROOF198 — entrywise comparison (all verified):**
- $\mathcal J_C\subseteq\mathcal J_D$ since $0\le C_{ii}\le D_{ii}$. $D_A^D(w)-D_A^C(w)=\frac12\sum_{i,j\in A}w_i(D_{ij}-C_{ij})w_j\ge0$ pointwise (entrywise order + positive $w$; no PSD on $D-C$). Infima and then maxima give $\mathscr S(C)\le\mathscr S(D)$ including the enlargement to newly eligible labels. Correct. The remark's counterexample $C=I_2$, $D=\binom{1\,1/2}{1/2\,1}$ has $D-C$ eigenvalues $\pm1/2$ and satisfies $0\le C_{ij}\le D_{ij}$. Correct.

**Remark controls (GRAM07, all verified):**
- $\ell=1/10,b=4,C=1$: $D(4)=1/400-16+8=-3199/400<0=\mathfrak F_C(0)$, so the empty set is essential. Correct.
- Non-concavity: $2\sqrt{(\phi-1)_+}-\phi^2/2$ decreases on $[0,1]$ and has right slope $+\infty$ at $1$ (derivative of $2\sqrt{\phi-1}$ is $1/\sqrt{\phi-1}$). Correct; global concavity unavailable.
- $k=\ell=1,b=0$: critical point $\phi=1$ (from $1/\sqrt\phi-\phi=0$), max $2-1/2=3/2$; for $\phi\le0$ score is $-\phi^2/2\le0$. Correct.
- "Doubling cost": $2\sqrt\phi-\phi^2$ has critical $\phi=2^{-2/3}$, value $4\cdot2^{-4/3}-2^{-4/3}=3\cdot2^{-4/3}$. Correct.

**Proof ledger (GRAM10):**
- PROOF194: all steps CHECKED. PASS.
- PROOF195: coercivity constants, coordinate bounds, compactness/closedness/attainment, cross-term handling, Hessian, stationarity — all CHECKED. PASS.
- PROOF196: active-set containment, weak-duality chain, dual-to-primal equality, omitted-label nonnegativity, empty case, attainment via forced equality — all CHECKED. PASS.
- PROOF197: empty base, zero-diagonal collapse, Schur test, reconstruction inner products, independence — all CHECKED. PASS.
- PROOF198: eligible inclusion, pointwise difference, inf/max, enlargement, indefinite $D-C$ check — all CHECKED. PASS.

**GRAM checklist:**
- GRAM01 PASS (scalar sqrt and Hilbert identities, factors of two, zero threshold, real $\ell$, exact).
- GRAM02 PASS (cross terms handled by nonnegativity drop; compact positive sublevel; constants $K_A,L_A$; no coordinate escape; no hidden invertibility).
- GRAM03 PASS (strict convexity and interior stationarity for singular PSD Grams with positive diagonals; nonnegativity vs PSD distinguished and used separately).
- GRAM04 PASS (duality quantifiers; threshold/zero/empty handled; negative nonempty dual scores handled; primal attainment without concavity/minimax/outside inactivity; two-label structure endorsed).
- GRAM05 PASS (induction, Schur complement, zero diagonals, independence; no complete positivity/nonnegative-coordinate assumption).
- GRAM06 PASS (entrywise comparison via infima/maxima and eligible-set enlargement; no PSD order on $D-C$, with correct indefinite counterexample).
- GRAM07 PASS (all four printed controls numerically confirmed; no falsification found).
- GRAM08 PASS (Lean hypotheses match the exact printed use on the active subset; analytic coercivity/calculus/attainment/inf-max independently verified).
- GRAM09 PASS within the finite-module scope; unresolved obligations: all upstream intrinsic lemmas/propositions cited by `integrated_intrinsic_constant.tex` are outside this snapshot.
- GRAM10 PASS (ledger above; no false statement or missing proof identified; remaining items are optional exposition).

## Required fixes before production gate

None. I identified no false statement and no missing proof within PROOF194–198. The only items not independently closed are upstream of the finite module (the intrinsic second-moment lemmas and their convergence/spectral inputs), which are outside the assigned five-proof scope but must be verified separately before the full intrinsic theorem is promoted.

## One-line summary

All five finite-Gram proofs (scalar/Hilbert identities, interior dual minimum, positive conic maximizer, real Gram realization, entrywise comparison) are algebraically and logically sound with correct signs, constants, boundary/empty-set handling, and realization independence; no repair is required.