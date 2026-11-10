## PROOF194
Label `L:gram-scalar-algebra` (module `notes/integrated_positive_gram.tex`, statement_LF 28–40, proof_LF 42–55).

**Statement (exact).** Let $H$ be any real Hilbert space. For real $\ell$, $w>0$, $t\ge 0$:
$$2\ell\sqrt t\ \le\ \frac{\ell^2}{w}+wt . \tag{E:gram-sqrt-dual}$$
For $\Phi,z\in H$:
$$\langle\Phi,z\rangle-\frac{\|\Phi\|^2}{2}=\frac{\|z\|^2}{2}-\frac{\|\Phi-z\|^2}{2}\le\frac{\|z\|^2}{2}. \tag{E:gram-hilbert-square}$$
For finite real $w_i$: $\|\sum_i w_i k_i\|^2=\sum_{i,j}w_iC_{ij}w_j$.

**Deduction.** (i) $0\le(\ell/\sqrt w-\sqrt{wt})^2=\ell^2/w+wt-2\ell\sqrt t$ by completing the square; covers $t=0$; equality at $w=\ell/\sqrt t$ when $\ell,t>0$. (ii) Expand $\|\Phi-z\|^2$. (iii) Bilinearity of the real inner product. No compactness of a Hilbert ball, no inverse Gram, no covariance matrix inverse is used.

**Condition/risk.** None internal. This is exact finite algebra. The only mathematical obligation is that the dual weights are strictly positive ($w>0$): the identity (E:gram-sqrt-dual) is one-sided for $w>0$ and this positivity is what later forces the positive-orthant dual in PROOF195.

---

## PROOF195
Label `L:gram-dual-minimum` (statement_LF 57–64, proof_LF 66–107).

**Statement (exact).** Setting: finite index set $\mathcal I$, $k_i\in H$, $\ell_i>0$, $b_i\ge0$, Gram $C_{ij}=\langle k_i,k_j\rangle\ge0$ entrywise (hence symmetric PSD); $\mathcal J=\{i:C_{ii}>0\}$. For nonempty $A\subset\mathcal J$, $w_i>0$,
$$D_A^C(w)=\sum_{i\in A}\frac{\ell_i^2}{w_i}-\sum_{i\in A}b_iw_i+\frac12\sum_{i,j\in A}w_iC_{ij}w_j,\qquad d_A^C=\inf_{w_i>0}D_A^C(w),\qquad d_\varnothing^C=0.$$
**Claim.** Each nonempty $A\subset\mathcal J$ has a *unique positive minimizer* $w^A\in(0,\infty)^A$ of $D_A^C$, and at that minimizer
$$\sum_{j\in A}C_{ij}w_j^A-b_i=\frac{\ell_i^2}{(w_i^A)^2}>0,\qquad i\in A. \tag{E:gram-dual-stationarity}$$

**Deduction.** (i) Coercivity: with $c_i=C_{ii}>0$, $K_A=\sum_i b_i^2/c_i$,
$$D_A^C(w)\ge\sum_i\left(\ell_i^2/w_i-b_iw_i+\tfrac12c_iw_i^2\right)\ge\sum_i\ell_i^2/w_i+\tfrac14\sum_i c_iw_i^2-K_A.$$
So bounded sublevels live in the box $[\ell_i^2/L_A,\sqrt{4L_A/c_i}]$ with $L_A=d_0+K_A$, $d_0=D_A^C(1,\dots,1)>0+L_A>0$; the minimum is attained in the open positive orthant. (ii) Hessian at a point: $\sum_i 2\ell_i^2w_i^{-3}\xi_i^2+\sum_{i,j}\xi_iC_{ij}\xi_j>0$ (first term strict, second a squared Hilbert norm), so $D_A^C$ is strictly convex on $(0,\infty)^A$; uniqueness. (iii) Interior stationarity: $-\ell_i^2/(w_i^A)^2-b_i+\sum_jC_{ij}w_j^A=0$, i.e. (E:gram-dual-stationarity); the RHS $\ell_i^2/(w_i^A)^2>0$.

**Condition/risk.** None internal. The positive-orthant minimization is complete because $c_i=C_{ii}>0$ on $\mathcal J$. The dual is *not* extended to nonnegative weights (no zero-weight coordinate); no inverse-Gram or nondegeneracy assumption is made anywhere. Note the omitted term $-b_iw_i$ is what makes the sign of $D_A^C$ possibly negative — this is the empty-subset phenomenon used in PROOF196.

---

## PROOF196
Label `P:gram-positive-optimizer` (statement_LF 109–118, proof_LF 120–157).

**Statement (exact).** With $\mathfrak F_C(\Phi)=2\sum_{i}\ell_i\sqrt{(\langle\Phi,k_i\rangle-b_i)_+}-\frac12\|\Phi\|^2$ and $\mathscr S(C)=\sup_\Phi\mathfrak F_C(\Phi)$, with $\ell_i>0$, $b_i\ge0$, entrywise nonnegative PSD Gram $C$:
$$\mathscr S(C)=\max_{A\subset\mathcal J}d_A^C.$$
Attainment: if a maximizing subset is **empty**, $\Phi=0$ attains; if a maximizing nonempty $A$ is chosen, $\Phi_A=\sum_{i\in A}w_i^A k_i$ attains with strictly positive coefficients $w_i^A>0$. *No uniqueness of the primal maximizer or of the maximizing subset is asserted.*

**Deduction.** Upper bound: for arbitrary $\Phi$, put $A=A(\Phi)=\{i:\langle\Phi,k_i\rangle>b_i\}\subset\mathcal J$; all remaining score terms vanish (thresholds give zero). If empty, $\mathfrak F_C(\Phi)=-\frac12\|\Phi\|^2\le0=d_\varnothing$. Otherwise with $t_i=\langle\Phi,k_i\rangle-b_i>0$ and arbitrary positive $w$ on $A$, $z=\sum_{i\in A}w_ik_i$, PROOF194 gives
$$\mathfrak F_C(\Phi)\le\sum_i\frac{\ell_i^2}{w_i}-\sum_ib_iw_i+\langle\Phi,z\rangle-\frac12\|\Phi\|^2\le D_A^C(w),$$
so $\mathfrak F_C(\Phi)\le d_{A(\Phi)}^C$; the supremum is bounded by $\max_{A\subset\mathcal J}d_A^C$. Lower bound: $\mathfrak F_C(0)=0=d_\varnothing$; for nonempty $A$ take $w^A$; (E:gram-dual-stationarity) makes each label $i\in A$ strictly active at $\Phi_A$ with $\sqrt{\langle\Phi_A,k_i\rangle-b_i}=\ell_i/w_i^A$, so the two PROOF194 inequalities become equalities on $A$ with $z=\Phi_A$; omitted labels add nonnegative terms; hence $\mathfrak F_C(\Phi_A)\ge d_A^C$. Maximize over all subsets, including the empty one.

**Condition/risk.** The exact conditions retained are: (a) the empty value $d_\varnothing=0$ is essential and must be included in the max — e.g. one label $C=1$, $\ell=1/10$, $b=4$ gives nonempty dual $D(4)=-3199/400<0$ whereas the score at $\Phi=0$ is $0$; (b) **no outside-inactivity assumption**: the maximizer $\Phi_A$ may activate labels outside $A$ and that only increases the score; (c) **no global concavity**: $k=\ell=b=1$ has score $2\sqrt{(\phi-1)_+}-\phi^2/2$, decreasing on $[0,1]$ with infinite positive right-slope at $1$; (d) **no primal uniqueness**. These are the exact conditions to retain; the deduction itself is closed.

---

## PROOF197
Label `L:gram-realization` (statement_LF 159–164, proof_LF 166–188).

**Statement (exact).** Every finite real symmetric PSD matrix is the Gram matrix of vectors in a finite-dimensional real Hilbert space. When its entries are nonnegative, the value $\mathscr S(C)$ of PROOF196 is **independent of the realization**; positive semidefiniteness of the round realization does not force nonnegative entries in the interior.

**Deduction.** Order the index set; empty matrix realized in $\{0\}$. If all entries vanish, testing $e_i+t e_j$ in the quadratic form gives $C=0$; realize by zero vectors. Else place a positive diagonal $c$ first and write $C=\begin{pmatrix}c&v^{\mathsf T}\\ v&A\end{pmatrix}$. The Schur complement $B=A-vv^{\mathsf T}/c$ is PSD because $(y,-v^{\mathsf T}y/c)$ gives the PSD test. Realize $B$ by vectors $u_i$; then $k_1=(\sqrt c,0)$, $k_i=(v_i/\sqrt c,u_i)$ realize $C$; undo the permutation. **The entries of $B$ may be negative.** Realization independence: $C_{ii}=0$ means $k_i=0$, its row/column vanish, and (E:gram-active-duality) depends only on $(C,\ell,b)$ and the eligible indices $\mathcal J=\{C_{ii}>0\}$.

**Condition/risk.** The only flagged strengthening is **complete positivity / nonnegative coordinates** — the realization via Schur complement does *not* preserve entrywise nonnegativity, and PROOF196's proof does not need it. The proof correctly avoids the Loewner machinery. No failure; retention condition: only entrywise data $(C_{ij})$ and $\mathcal J$ are legitimate inputs.

---

## PROOF198
Label `P:gram-entrywise-comparison` (statement_LF 190–198, proof_LF 200–214).

**Statement (exact).** Let $C,D$ be real symmetric PSD matrices on the *same* finite index set with $0\le C_{ij}\le D_{ij}$ entrywise, and the same $\ell_i>0$, $b_i\ge0$. Then $\mathscr S(C)\le\mathscr S(D)$. **No positive-semidefinite (Loewner) order on $D-C$ is required.**

**Deduction.** $\mathcal J_C\subset\mathcal J_D$. For nonempty $A\subset\mathcal J_C$ and positive weights $w$,
$$D_A^D(w)-D_A^C(w)=\frac12\sum_{i,j\in A}w_i(D_{ij}-C_{ij})w_j\ge0,$$
so $d_A^C\le d_A^D$ after infima; the empty values are both zero. PROOF196 converts these to $S(C)\le S(D)$, including the appearance of labels that were null in $C$ (zero-Gram → empty subset handled by the inclusion of eligible families).

**Condition/risk.** The falsified strengthening: Loewner order. The explicit witness is $C=I_2$, $D=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}$, both nonnegative PSD Grams, with $D-C=\begin{pmatrix}0&1/2\\1/2&0\end{pmatrix}$ having eigenvalues $\pm1/2$ (indefinite). Hence the dual difference $D_A^D-D_A^C$ is nonnegative only through entrywise data — which is exactly the hypothesis. This is the intended entrywise content carried into the physical labels of PROOF200.

---

## PROOF199
Label `L:positive-raw-embedding` (module `notes/integrated_intrinsic_constant.tex`, statement_LF 26–43, proof_LF 45–123).

**Statement (exact).** With $a=\alpha_0$, $I=(0,1)$, $K(s,t)=|s-t|^{-a}$, and the original raw covariance Hilbert space $H_I=H_t\otimes H_{\mathrm{sp}}$:
1. For every real Hilbert space $G$ there is a bounded map $J_G:L^2(I;G)\to H_t\widehat\otimes G$ with
$$\|J_GF\|^2=\int_{I^2}K(s,t)\langle F(s),F(t)\rangle_G\,\mathrm ds\mathrm dt\le K_0\|F\|_{L^2(I;G)}^2,\qquad K_0=\frac{2^a}{1-a}.$$
2. The natural inclusion puts every positive compact smooth test $\Psi\in\mathcal C_{\mathrm{pos}}$ (all nonzero nonnegative $C_c^\infty(I\times\R^d)$) into $H_I$, and
$$\|\Psi\|_{H_I}^2=v_\Psi,\qquad \mathcal T_R\Psi(s)=B_E(m_R\,h_{\Psi,s})\ \text{a.e. }s,$$
where $h_{\Psi,s}(x)=\int_0^1|s-t|^{-a}(\Gamma*\Psi_t)(x)\,\mathrm dt$ (with $\Gamma*\Psi_t$ the continuous mean) and $v_\Psi=\int_{I\times\R^d}\Psi(s,x)h_{\Psi,s}(x)\,\mathrm dx\mathrm ds$. For each fixed smooth $\Psi$ the RHS gives a canonical version for every $R\ge1$ and every $s\in I$.

**Deduction.** Row bound: $\int_IK(s,t)\mathrm dt=(s^{1-a}+(1-s)^{1-a})/(1-a)\le K_0$; bilinear Schur/completing-square extends $J_G$. The Bochner integral $\int_I K(s,t)F(t)\mathrm dt$ exists a.e.; agrees with $(C_t\otimes I)J_G$ on tensors; equal limits. The local physical bound $\|q\|_{H_{\mathrm{sp}}}^2\le|B|\Gamma(B-B)\|q\|_\infty^2$ on a common compact support admits $\Psi$; then $v_\Psi$ and the Fubini identity for $\|\Psi\|_{H_I}^2$ follow. The mean-row identity is obtained by testing the completed mean against displacement/velocity pairs, giving $\mathcal T_R\Psi(s)=B_E(m_R h_{\Psi,s})$ a.e., with the stated canonical version for fixed $\Psi$.

**Condition/risk.** This imports, with precise statements retained:
(i) the compact temporal covariance map $C_t:H_t\to L^r(I)$, $2<r<2/a$, and the completed mean $\mathcal T_R=T_R(C_t\otimes I)$ taking values in $\mathcal K(E)$ (Section `S:actual-cameron-mean`, Propositions `P:cameron-full-mean`, `P:uniform-mean-regulator`), with the uniform bound $C_{\mathrm{mean}}=M_0\|C_t\|<\infty$;
(ii) the mean-row identity `E:uniform-mean-row` giving $\langle T_R q\,z,w\rangle_E=\langle q,(\eta_R z_1)(\eta_R\Lambda^{-1}w_2)\rangle_{H_{\mathrm{sp}}}$.
No new deduction about the covariance being injective is used: the null-quotient completions handle it. The direct sums (both sums, no surviving zero-divisor) are legitimate at $a<1$.

---

## PROOF200
Label `L:positive-physical-gram` (statement_LF 125–145, proof_LF 147–175).

**Statement (exact).** Take a finite partition of $I$ into nonempty cells $I_i$ of lengths $\ell_i>0$, $\sum_i\ell_i=1$, and real $f_i\in C_c^\infty(\R^d;\R)$ with $\|f_i\|_2=1$. Define
$$h_i=\frac{\mathbf 1_{I_i}}{\ell_i},\quad b_i=\|\nabla f_i\|_2^2,\quad
k_i^R=h_i\otimes(m_R f_i^2),\quad k_i^\infty=h_i\otimes f_i^2\ \in H_I.$$
If $v_L(u,w)=\langle Vu,w\rangle_{H^{-1/2},H^{1/2}}$ is the symmetric multiplier form of the operator $L=B_E(V)\in\mathcal V_{E,R}$, then for every $\Phi\in H_I$:
$$\langle\Phi,k_i^R\rangle_{H_I}=\frac1{\ell_i}\int_{I_i}v_{\mathcal T_R\Phi(s)}(f_i,f_i)\,\mathrm ds.$$
The Grams $C^R_{ij}=\langle k_i^R,k_j^R\rangle$, $D_{ij}=\langle k_i^\infty,k_j^\infty\rangle$ satisfy
$$0\le C^R_{ij}\le D_{ij}\ \text{entrywise.}$$

**Deduction.** $h_i\in H_t$ by PROOF199; $f_i^2$ lies in $H_{\mathrm{sp}}$ with finite pairing. The row identity comes from `E:uniform-mean-row` with $z=(f_i,0)$, $w=(0,\Lambda f_i)$, giving row product $(\eta_R f_i)^2=m_R f_i^2$, integrated over the cell against $h_i$. Each Gram factors into the nonnegative temporal pairing of $h_i,h_j$ and the physical spatial pairing; since $0\le m_R\le1$ and $\Gamma$, $f_i^2,f_j^2$ are nonnegative, the masked factor is pointwise dominated by the unmasked one; Tonelli gives $0\le C_{ij}^R\le D_{ij}$. No additional Gamma/Fourier factor enters; the physical pairing already contains $\Gamma$; no Loewner claim on $D-C^R$.

**Condition/risk.** All hypotheses of PROOF198 are met **entrywise**, with eligible sets $\mathcal J_{C^R}\subset\mathcal J_D$. The flagged anti-conditions: no PSD order of $D-C^R$ assumed, zero labels permitted (a zero $f_i^2$ row handled by 198's eligible-set inclusion), and the comparison is of Gram entries only — it does not compare two Rayleigh forms with the *same* coordinate profile.

---

## PROOF201
Label `L:positive-uniform-optimizer` (statement_LF 177–187, proof_LF 189–247).

**Statement (exact).** Put
$$M=4\,C_{\mathrm{mean}}+4.$$
Then: (i) the supremum over $\Phi$ defining the raw signed score $\mathcal S_R=\sup_{\Phi}\{2\,\mathrm{Rate}_R(\Phi)-\frac12\|\Phi\|_{H_I}^2\}$ may be restricted to $\|\Phi\|_{H_I}\le M$, *uniformly in $R\ge1$*; (ii) for every finite trial family of PROOF200 the unmasked finite score $\mathfrak F_D$ has a maximizer $\Phi_D$ with $\|\Phi_D\|\le M$, which is either zero or a positive conic combination $\sum_i w_ik_i^\infty$, $w_i>0$; (iii) in the nonzero branch $\Phi_D$ is approximable in $H_I$ by tests in $\mathcal C_{\mathrm{pos}}$.

**Deduction.** With $C=C_{\mathrm{mean}}$, $q=\|\Phi\|$, the exported rate bound $\mathrm{Rate}_R(\Phi)\le1+Cq$ gives
$$2\,\mathrm{Rate}_R(\Phi)-\frac{q^2}2\le2+2Cq-\frac{q^2}2<2-2q<0\quad(q>M),$$
while $\Phi=0$ has score zero, proving (i). For the finite objective, PROOF196 gives an attained maximizer, and repeated use of the same exported bound shows $\|\Phi_D\|\le M$ uniformly. For the nonzero branch, $\Phi_D=\sum_{i\in A}w_ih_i\otimes f_i^2$; smoothing $h_i$ by nonnegative compact approximate identities and smooth cutoffs converging to one produces $h_{i,j}\in C_c^\infty(I)$, $\Psi_j=\sum_iw_ih_{i,j}f_i^2\in\mathcal C_{\mathrm{pos}}$ with $\Psi_j\to\Phi_D$ in $H_I$; the integrated-rate continuity
$|\mathrm{Rate}_{R'}(\Psi_j)-\mathrm{Rate}_{R'}(\Phi_D)|\le\sqrt{3+C\|\Psi_j\|+C\|\Phi_D\|}\,\sqrt{C\|\Psi_j-\Phi_D\|}\to0$
holds uniformly in $R'$. No uniform derivative budget on the approximants is asserted.

**Condition/risk.** This is the *uniform optimizer ball* that must be established **before** the second time-averaging in PROOF202: the bound $\|\Phi_D\|\le M$ qualifies $\Phi_D$ for the uniform averaging error $e_n$, which is only controlled on $\|\Phi\|\le M$. The imported inputs are exactly: $\mathrm{Rate}_R(\Phi)\le1+C_{\mathrm{mean}}\|\Phi\|$ and the rate continuity (both in `S:uniform-physical-products`). The positive smoothing is a conic-sum approximation, not a truncation of an eigenvector.

---

## PROOF202
Label `P:positive-signed-comparison` (statement_LF 249–255, proof_LF 257–332).

**Statement (exact).** For every $R\ge1$,
$$\mathcal S_R\le S_2^{\mathrm{pos}}.$$

**Deduction (exact order).** Use uniform partitions of $I$ into $n\ge2$ cells of length $1/n$; the uniform averaging error $e_n\to0$ is valid on $\|\Phi\|\le M$ uniformly in $R$. Fix $R,\Phi,n$ ($\|\Phi\|\le M$). Let $W_i=\ell_i^{-1}\int_{I_i}\mathcal T_R\Phi(s)\mathrm ds$; the real Rayleigh identity
$$\lambda(W_i)=\sup_{f\in C_c^\infty(\R^d;\R),\,\|f\|_2=1}\sqrt{(v_{W_i}(f,f)-\|\nabla f\|_2^2)_+}$$
gives, with near-maximizing trials $f_i$ (error $\varepsilon$),
$$2\,\mathrm{Rate}_R(\Phi)-\tfrac12\|\Phi\|^2\le \mathfrak F_{C^R}(\Phi)+2e_n+2\varepsilon.$$
Entrywise Gram comparison (198) then gives $\mathfrak F_{C^R}(\Phi)\le\mathscr S(C^R)\le\mathscr S(D)=\mathfrak F_D(\Phi_D)$ (**optimized values, not the same control**). PROOF201 gives $\|\Phi_D\|\le M$; choose $R'$ whose plateau covers $\operatorname{supp}f_i$, so $k_i^{R'}=k_i^\infty$; the label row plus the same uniform averaging gives
$$\mathfrak F_D(\Phi_D)\le2\,\mathrm{Rate}_{R'}(\Phi_D)-\tfrac12\|\Phi_D\|^2+2e_n.$$
If $\Phi_D=0$, the finite score is zero. Else approximate by positive smooth $\Psi_j$; PROOF199 identifies their actual mean with $B_E(m_{R'}h_{\Psi_j,s})$ and their cost with $v_{\Psi_j}$; since $h_{\Psi_j,s}\ge0$ and $0\le m_{R'}\le1$, real form order gives $\mathrm{Rate}_{R'}(\Psi_j)\le I_{\Psi_j}$, so
$$2\,\mathrm{Rate}_{R'}(\Psi_j)-\tfrac12\|\Psi_j\|^2\le S_2^{\mathrm{pos}}.$$
Convergence passes this to $\Phi_D$. Collecting all terms: $2\,\mathrm{Rate}_R(\Phi)-\frac12\|\Phi\|^2\le S_2^{\mathrm{pos}}+4e_n+2\varepsilon$. Let $\varepsilon\downarrow0$, take the supremum over the $M$-ball (legitimate by 201), then $n\to\infty$.

**Condition/risk.** (i) The error $e_n$ is used **twice** — first to produce the masked Gram, then on $\Phi_D$ — and is legitimate only because $\|\Phi_D\|\le M$ is proved (201) *before* the second use and $e_n$ is uniform in $R$; the tracked error is exactly $4e_n+2\varepsilon$. (ii) Zero branch uses only $S_2^{\mathrm{pos}}\ge0$. (iii) The finiteness $S_2^{\mathrm{pos}}<\infty$ is **not** derived here and is **not** circular: it comes from the independent upper bound (051→132 in `P:variational-positive-scores`), which precedes this step. (iv) The form-order step $m_R\le1\,\Rightarrow\,\mathrm{Rate}_{R'}(\Psi_j)\le I_{\Psi_j}$ uses real $H^1$ form monotonicity (Teschl Cor.~4.13) applied to *nonnegative* potentials only.

---

## PROOF203
Label `P:positive-score-cutoff` (statement_LF 334–340, proof_LF 342–371).

**Statement (exact).** The possibly nonmonotone mask family $(m_R)_{R\ge1}$ (even, $0\le m_R\le1$, $\uparrow 1$ pointwise, or in general eventually 1 on each fixed compact set) satisfies
$$\lim_{R\to\infty}\mathcal S_R=S_2^{\mathrm{pos}}.$$

**Deduction.** Fix **one** positive compact test $\Psi\in\mathcal C_{\mathrm{pos}}$ *before* any $R$ or moment limit. Its masked rate $\lambda_R(s)$ satisfies $0\le\lambda_R(s)\le\lambda_{\Psi,s}$ by real form order, and $m_R=1$ on the support of each fixed compact smooth trial $f$ for all large $R$; the real Rayleigh trial argument gives $\liminf_R\lambda_R(s)^2\ge\int h_{\Psi,s}f^2-\|\nabla f\|_2^2$, and trial density plus the unmasked Rayleigh identity gives $\lambda_R(s)\to\lambda_{\Psi,s}$. The global smooth bound $H_\Psi=\sup_{s,x}h_{\Psi,s}(x)<\infty$ gives $\lambda_R(s)\le\sqrt{H_\Psi}$, so dominated convergence gives $\mathrm{Rate}_R(\Psi)\to I_\Psi$. The cost $\|\Psi\|^2=v_\Psi$ is independent of $R$. Hence $\liminf_R\mathcal S_R\ge2I_\Psi-\frac12v_\Psi$ for each fixed test. Given $\varepsilon>0$, choose one test with score $>S_2^{\mathrm{pos}}-\varepsilon$ (the finite supremum admits one), take liminf, then $\varepsilon\downarrow0$. PROOF202 supplies the reverse limsup. Done.

**Condition/risk.** No unmasked ground eigenfunction is claimed: the argument uses only trial density, form monotonicity, and pointwise (eventually-1-on-each-fixed-trial) mask convergence. The optimizer is a *single fixed* control chosen before $R\to\infty$, not an $R$-dependent test; the only masking assumption used is that each fixed compact Rayleigh trial eventually sits in the plateau. No uniform-in-control claim over all of $\mathcal C_{\mathrm{pos}}$.

---

## PROOF204
Label `T:intrinsic-second-moment` (statement_LF 373–402, proof_LF 404–428).

**Statement (exact).** For every original admissible model — covariance $\Gamma$ (possibly $\delta_0$ at $d=\alpha=1$) homogeneous of degree $-\alpha$, temporal exponent $\alpha_0=a$, $0<\alpha_0<1$, $\alpha+\alpha_0<2$ — data $(1,0)$, and every fixed $x\in\R^d$:
$$\lim_{T\to\infty}T^{-\frac{4-\alpha-a}{3-\alpha}}\log\E|u_\Gamma(T,x)|^2=C_2(\Gamma,a)=S_2^{\mathrm{pos}}=2^{\frac{4-\alpha}{3-\alpha}}S_1^{\mathrm{pos}},$$
with the complete positive-control formula
$$C_2=\sup_{\Psi\in\mathcal C_{\mathrm{pos}}}\left\{2\int_0^1\sqrt{\sup_{\substack{f\in H^1(\R^d;\R)\\ \|f\|_2=1}}\left(\int h_{\Psi,s}f^2-\|\nabla f\|_2^2\right)}\mathrm ds-\frac{v_\Psi}{2}\right\},$$
$$h_{\Psi,s}(x)=\int_0^1|s-t|^{-a}(\Gamma*\Psi_t)(x)\,\mathrm dt,\quad
v_\Psi=\int_{(0,1)\times\R^d}\Psi(s,x)h_{\Psi,s}(x)\,\mathrm dx\mathrm ds,$$
with $\mathcal C_{\mathrm{pos}}$ = all nonzero nonnegative real $C_c^\infty((0,1)\times\R^d)$ tests (nonseparable allowed). Covariance amplitude original, kinetic coefficient one, Gaussian action $v_\Psi/2$. Nonzero $\Gamma$: $0<C_2<\infty$. $\Gamma=0$: constant and rate are zero.

**Deduction.** Assume $\Gamma\neq0$. **Upper:** `P:original-signed-point-upper` bounds the point limsup by $\limsup_{\delta\downarrow0}\mathcal S_{\delta^{-1}+2}$; PROOF203 converts this to $S_2^{\mathrm{pos}}$. **Lower:** `P:variational-positive-scores` gives $\liminf\ge S_2^{\mathrm{pos}}$. Both bounds use the **same** canonical Stratonovich $u$, same exponent $\kappa=\frac{4-\alpha-a}{3-\alpha}$, same covariance/amplitude, same variance-half action, same data $(1,0)$ with *both* entries (displacement and velocity), and the identical source-first identification of all mixed/unequal/self/empty pairing chains and Green-before-noise convention in $d=3$. Spatial stationarity (`P:raw-block-original-lower`) extends both bounds to every fixed $x$. Homogeneity $S_c^{\mathrm{pos}}=c^{\frac{4-\alpha}{3-\alpha}}S_1^{\mathrm{pos}}$, positivity, and finiteness are from `P:variational-positive-scores` (funded by 051, see GLOBAL-G1). The formula follows from `E:variational-real-rayleigh` and the raw variance definition. $\Gamma=0$: $H_I=\{0\}$, all means/variances/rates vanish, $u=1$.

**Condition/risk.** The consummation is a *coupling* of three imported terminal bounds — signed upper (`P:original-signed-point-upper`, i.e. the F025 chain 190–193), cutoff removal (203), and raw lower (`P:variational-positive-scores`, i.e. the F013 chain 127–132) — not an independent re-derivation inside 194–204. The three must be valid for the *same object*; the equality is exactly
$$\limsup_T\le S_2^{\mathrm{pos}}\le\liminf_T.$$
The label-one score $S_1^{\mathrm{pos}}$ is **auxiliary**: it is not an actual first-moment limit, not Chen's printed $L_*$ or $L^*$, it supplies no double-Jensen improvement, and no source normalization is corrected. Zero covariance is handled only by the direct zero identity (no strict-positivity claim there).

---

## PROOF205
Label `L:occupation-raw-square` (module `notes/integrated_occupation_ceiling.tex`, statement_LF 24–44, proof_LF 46–98).

**Statement (exact).** There is a continuous map $Q:H^1(\R^d;\R)\to H_{\mathrm{sp}}$ with
$$\langle Q(f),Q(h)\rangle_{H_{\mathrm{sp}}}=B_\Gamma(f^2,h^2),\qquad \|Q(f)\|_{H_{\mathrm{sp}}}^2=A_{\mathrm{sp}}(f).$$
For every full occupation profile $g\in\mathcal O$ (strongly $H^1$-measurable $s\mapsto g_s$, $\|g_s\|_2=1$ a.e., $T(g)=\int_0^1\|\nabla g_s\|_2^2\,\mathrm ds<\infty$), the element
$$\rho_g=J_{H_{\mathrm{sp}}}(s\mapsto Q(g_s))\in H_I$$
satisfies
$$\|\rho_g\|_{H_I}^2=A(g),\qquad
\langle\Psi,\rho_g\rangle_{H_I}=\int_0^1\int_{\R^d}h_{\Psi,s}(x)g_s(x)^2\,\mathrm dx\,\mathrm ds\quad(\Psi\in\mathcal C_{\mathrm{pos}}),$$
and consequently $\langle\Psi,\rho_g\rangle_{H_I}\le\sqrt{v_\Psi A(g)}$.

**Deduction.** Set $F_g(s)=Q(g_s)$; strong measurability uses separability of $H^1$ through $f\mapsto(f,\nabla f)$. With $b_s=\|\nabla g_s\|_2^2$, the four-linear control gives $\|Q(g_s)\|^2=A_{\mathrm{sp}}(g_s)\le R_{\mathrm{sp}}b_s^{\alpha/2}$, so
$$\int_0^1\|F_g(s)\|^2\mathrm ds\le R_{\mathrm{sp}}T(g)^{\alpha/2}.$$
$J_{H_{\mathrm{sp}}}$ (PROOF199) produces $\rho_g$ with norm $A(g)$. The pairing with $\Psi$ follows from the polarized inclusion and the physical identity $\langle\Psi_t,Q(g_s)\rangle=B_\Gamma(\Psi_t,g_s^2)$; evenness of $\Gamma$ and nonnegative Tonelli give the double integral; Hilbert Cauchy–Schwarz with $\|\Psi\|^2=v_\Psi$ gives the bound.

**Condition/risk.** This is the *full $H^1$ square map*; the earlier damped occupation object is `K_\star`-based energy and is **not** used here. Three imported facts are retained precisely: $Q$'s continuity and the four-linear absolute estimate (F015 `P:spatial-four-linear`), the spatial constant $R_{\mathrm{sp}}$, and the Bochner inclusion $J_{H_{\mathrm{sp}}}$ (199). The representative independence is from `L:spatial-physical-pair`. No time-smooth profile, no common compact support, and no optimizer restriction are imposed on $\mathcal O$. The rough occupation object $\rho_g$ is a raw-Hilbert element, not a stochastic flow insertion.

---

## PROOF206
Label `P:raw-occupation-energy` (statement_LF 100–120, proof_LF 122–164).

**Statement (exact).** With $K_0=\frac{2^a}{1-a}$ and raw occupation quantities
$$A(g)=\int_{I^2}K(s,t)B_\Gamma(g_s^2,g_t^2)\,\mathrm ds\mathrm dt,\quad
C_{\mathrm{occ}}=\sup_{g\in\mathcal O}\frac{A(g)}{T(g)^{\alpha/2}},\quad
\mathcal E_\zeta^{\mathcal O}=\sup_{g\in\mathcal O}\{A(g)-\zeta T(g)\}\ (\zeta>0),$$
one has
$$0<C_{\mathrm{occ}}\le K_0R_{\mathrm{sp}}<\infty,$$
$$\mathcal E_\zeta^{\mathcal O}=D_\zeta C_{\mathrm{occ}}^{2/(2-\alpha)},\qquad
D_\zeta=\frac{2-\alpha}{2}\left(\frac{\alpha}{2\zeta}\right)^{\alpha/(2-\alpha)},$$
$$C_{\mathrm{occ}}=\left(\frac{2\mathcal E_\zeta^{\mathcal O}}{2-\alpha}\right)^{(2-\alpha)/2}\left(\frac{2\zeta}{\alpha}\right)^{\alpha/2},$$
and $\mathcal E_\zeta^{\mathcal O}=\zeta^{-\alpha/(2-\alpha)}\mathcal E_1^{\mathcal O}$.

**Deduction.** Unit $H^1$ profiles have positive gradient energy; spatial covariance Cauchy–Schwarz gives $B_\Gamma(g_s^2,g_t^2)\le R_{\mathrm{sp}}b_s^{\alpha/4}b_t^{\alpha/4}$; Schur with row bound $K_0$ and concavity give $0\le A(g)\le K_0R_{\mathrm{sp}}T(g)^{\alpha/2}$; a fixed constant-in-time compact profile has positive $A$, so $0<C_{\mathrm{occ}}<\infty$. Full-class dilation $(U_\ell g)_s(x)=\ell^{d/2}g_s(\ell x)$ is a bijection of $\mathcal O$ with $A(U_\ell g)=\ell^\alpha A(g)$, $T(U_\ell g)=\ell^2T(g)$; scalar optimization in $\ell$ of $A\ell^\alpha-\zeta T\ell^2$ at $\ell^{2-\alpha}=\alpha A/(2\zeta T)$ attains $D_\zeta[A/T^{\alpha/2}]^{2/(2-\alpha)}$; ratios approaching $C_{\mathrm{occ}}$ give the equalities. No optimizer or minimax exchange is assumed, and $\zeta$ is a **scalar penalty**, not a spatial mask and not a noise parameter.

[held back: collaborators' unpublished work]

---

## PROOF207
Label `L:occupation-rayleigh-selection` (statement_LF 166–174, proof_LF 176–216).

**Statement (exact).** For fixed $\Psi\in\mathcal C_{\mathrm{pos}}$ and every $\varepsilon>0$ there exists $g_\varepsilon\in\mathcal O$ such that
$$I_\Psi^2+T(g_\varepsilon)\le\sqrt{v_\Psi A(g_\varepsilon)}+\varepsilon.$$

**Deduction.** Countable dense family $(f_j)$ of unit compact smooth $H^1$ trials; $b_j=\|\nabla f_j\|_2^2$, $R_j(s)=\int h_{\Psi,s}f_j^2-b_j$, $\lambda_{\Psi,s}^2=\sup_jR_j(s)$. First-index Borel selection: $A_1=U_1$, $A_j=U_j\setminus\bigcup_{i<j}U_i$ with $U_j=\{R_j(s)>\lambda_{\Psi,s}^2-\varepsilon\}$; $g_\varepsilon(s)=f_j$ on $A_j$, filled by $f_1$ off the cover. Finite-valued truncations of finite profiles give strong measurability. The near-Rayleigh choice gives $b(g_\varepsilon(s))<H_\Psi+\varepsilon$, so $g_\varepsilon\in\mathcal O$. Integrating and using PROOF205's pairing:
$$\int_0^1\lambda_{\Psi,s}^2\,\mathrm ds+T(g_\varepsilon)\le\langle\Psi,\rho_{g_\varepsilon}\rangle+\varepsilon\le\sqrt{v_\Psi A(g_\varepsilon)}+\varepsilon;$$
then $I_\Psi^2\le\int_0^1\lambda_{\Psi,s}^2$ (time Cauchy–Schwarz with unit interval). No eigenvector, no continuum-selector, and no limit occupation is required.

**Condition/risk.** The selection is **Borel first-index near-Rayleigh**, which is exactly what avoids an unmasked ground state or a measurable continuum optimizer. The kinetic bound uses the finite trial supremum only, not a ground profile.

---

## PROOF208 (derived, mandatory)
Label `T:intrinsic-occupation-ceiling` (statement_LF 228–242, proof_LF 244–280).

**Statement (exact).** For $0\le b<q/2$, define $F_b(0)=0$ and
$$F_b(z)=k\left[\frac{(q-2b)^{(q-2b)/2}}{8(q-b)^{q-b}}\left(\frac{2z}{2-\alpha}\right)^{(2-\alpha)/2}\right]^{1/k},\ z>0,\quad q=4-\alpha,\ k=3-\alpha.$$
For every positive score coefficient $\mathfrak c$,
$$S_{\mathfrak c}^{\mathrm{pos}}\le U_{\mathfrak c}:=\mathfrak c^{\frac{q}{k}}k\left[\frac{\alpha^{\alpha/2}C_{\mathrm{occ}}}{8q^{q/2}}\right]^{1/k}
=\mathfrak c^{\frac{q}{k}}(2\zeta)^{\alpha/(2k)}F_0(\mathcal E_\zeta^{\mathcal O}),\quad \zeta>0.$$
In particular $C_2= S_2^{\mathrm{pos}}\le U_2$. The ceiling is **not** asserted attained or equal to $C_2$.

**Deduction.** Fix $\Psi$; with $v=v_\Psi$, $C=C_{\mathrm{occ}}$, $\beta=\alpha/4$, PROOF207 gives $I_\Psi^2\le\sqrt{vC}\,T^\beta-T+\varepsilon$, optimizable in $T$ first. Uniqueness of the critical point gives
$$\sup_{T\ge0}\{\sqrt{vC}T^\beta-T\}=\frac q4\left(\frac\alpha4\right)^{\alpha/q}(vC)^{2/q},$$
so $I_\Psi\le Dv^{1/q}$ with $D=\sqrt{q/4}\,(\alpha/4)^{\alpha/(2q)}C^{1/q}$. Then optimize $v\ge0$ in $\mathfrak cDv^{1/q}-\frac v2$; the maximum is at $v_*=(2\mathfrak cD/q)^{q/k}$ equal to $kv_*/2$, and positivity of powers gives $(2D/q)^q=q^{-q/2}(\alpha/4)^{\alpha/2}C$; since $k+\alpha=3$, the maximum is exactly $U_{\mathfrak c}$ (denominator $8$). The second form uses PROOF206's rewrite of $C_{\mathrm{occ}}$ in terms of $\mathcal E_\zeta^{\mathcal O}$; the $(2\zeta)^{\alpha/(2k)}$ factor and the penalty cancellation are reproduced. $\varepsilon\downarrow0$ then the supremum over $\mathcal C_{\mathrm{pos}}$; 204 identifies $S_2^{\mathrm{pos}}=C_2$.

**Condition/risk.** The ceiling is the *combined* occupation bound: it upper-bounds the positive-control score through the raw ratio $C_{\mathrm{occ}}$. It is not an evaluation of the intrinsic supremum; attainment/equality is explicitly disclaimed. The 204 identification is applied **only after** this scalar ceiling is derived (no reversal).

---

## PROOF209 (derived, mandatory)
Label `C:intrinsic-spatial-bracket` (statement_LF 282–296, proof_LF 298–334).

**Statement (exact).** With $m=\frac{4-\alpha}{3-\alpha}$, the equilibrium mass $M_a=\frac{\Gamma_E((1+a)/2)}{\Gamma_E(1+a)\Gamma_E((1-a)/2)}$, and the spatial energy $\mathcal E_{\mathrm{sp}}$, the intrinsic constant obeys the two-sided spatial-energy bracket
$$2^m M_a^{-1/k}F_0(\mathcal E_{\mathrm{sp}})\le C_2(\Gamma,a)\le2^mK_0^{1/k}F_0(\mathcal E_{\mathrm{sp}}).$$
For $\Gamma\neq0$ there is, in addition, the own-energy comparison
$$C_2\le2^mF_0(\mathcal E_{1/2}^{\mathcal O})<2^mF_a(\mathcal E_{1/2}^{\mathcal O}).$$

**Deduction.** Upper: insert $C_{\mathrm{occ}}\le K_0R_{\mathrm{sp}}$ into PROOF208's first form and convert $\mathcal E_{\mathrm{sp}}$ to $R_{\mathrm{sp}}$ via `E:spatial-energy-map`. Lower: `E:spatial-static-energy-score` multiplied by $2^m$ together with 204. The strict gap: define
$$\Delta=\frac12[q\log q+(q-2a)\log(q-2a)]-(q-a)\log(q-a)>0,$$
positive because $a>0$, $q-2a>2-a>1$, and $x\mapsto x\log x$ is strictly midpoint-convex (second derivative $1/x>0$). Subtracting logarithms: $\log(F_a(z)/F_0(z))=\Delta/k$, and
$$\frac{\mathfrak c^mF_a(\mathcal E_\zeta^{\mathcal O})}{U_{\mathfrak c}}=\exp\left(\frac{\Delta-\frac{\alpha}{2}\log(2\zeta)}{k}\right).$$
At $\zeta=1/2$, $\log(2\zeta)=0$, giving $2^mF_a(\mathcal E_{1/2}^{\mathcal O})>U_2$, hence the strict statement. At $\zeta=1$ the comparison is **not universally favorable**: with $\alpha=5/4$, $a=1/2$, $d=2$,
$$8\left[\Delta-\frac\alpha2\log2\right]=\log\frac{11^{11}7^7}{2^5\,9^{18}}<0$$
($11^{11}7^7=234966429149994773$, $2^5 9^{18}=4803028329503971872$).

[held back: collaborators' unpublished work]

---

## PROOF210
Label `L:white-cdf-square` (module `notes/integrated_white_evaluation.tex`, statement_LF 13–20, proof_LF 22–59).

**Statement (exact).** $d=\alpha=1$, $\Gamma=c\delta_0$, $c\ge0$. For every real unit $f\in H^1(\R)$, with $A=\int_\R f^4$, $b=\int_\R(f')^2$, $\mathsf F(x)=\int_{-\infty}^xf(y)^2\mathrm dy$, for every real $z$:
$$0\le\int_\R\left[f'-zf(1-2\mathsf F)\right]^2=b-2zA+\frac{z^2}{3},$$
and $A<\infty$.

**Deduction.** On bounded intervals $f'$ is $L^1$ (Cauchy–Schwarz); its integral primitive has weak derivative $f'$; the difference has zero weak derivative hence is constant; so $f$ has a locally absolutely continuous representative. $\rho=f^2$ is locally AC with $\rho'=2ff'\in L^1$, $\rho\ge0$, $\int\rho=1$; $\rho$ has vanishing end limits, hence is bounded, so $A<\infty$. $\mathsf F'=\rho$, $0\le\mathsf F\le1$, end limits $0,1$. Integration by parts with vanishing tails gives $\int f'f(1-2\mathsf F)=A$ and, via $P(y)=y-2y^2+\frac43y^3$ with $P'=(1-2y)^2$, $\int f^2(1-2\mathsf F)^2=P(1)-P(0)=1/3$. Expansion of the square gives the exact identity.

**Condition/risk.** Only the *weak* derivative is required: $f'$ exists in $L^2$ (in $L^1_{\mathrm{loc}}$ on bounded intervals), and **no** absolute continuity claim is made for $f'$; the CDF $\mathsf F$ is absolutely continuous but need not be strictly increasing, and $f$ need not be positive or compactly supported. This is the exact fragile point (weak-AC vs strong-AC) and it is handled correctly.

---

## PROOF211 (derived, mandatory)
Label `P:white-spatial-energy` (statement_LF 61–68, proof_LF 70–108).

**Statement (exact).** For $c>0$:
$$R_{\mathrm{sp}}=\frac c{\sqrt3},\qquad \mathcal E_{\mathrm{sp}}=\frac{c^2}{6}.$$
Both are zero at $c=0$.

**Deduction.** PROOF210 at $z=3A$ gives $3A^2\le b$. Nonzero unit profiles have $A,b>0$, so $A/\sqrt b\le1/\sqrt3$. The noncompact full-$H^1$ family
$$f_\ell(x)=\sqrt{\frac\ell2}\,\operatorname{sech}(\ell x),\quad f'_\ell=-\ell\tanh(\ell x)f_\ell$$
has unit mass, $A=\ell/3$, $b=\ell^2/3$ (via $t=\tanh(\ell x)$, $\mathrm dt=\ell\operatorname{sech}^2(\ell x)\mathrm dx$), attaining $A/\sqrt b=1/\sqrt3$; hence $R_{\mathrm{sp}}=c/\sqrt3$ since $A_{\mathrm{sp}}=cA$. Then `E:spatial-energy-map`: $\mathcal E_{\mathrm{sp}}=\frac{2-\alpha}{2}\alpha^{\alpha/(2-\alpha)}R_{\mathrm{sp}}^{2/(2-\alpha)}=\frac12\cdot\frac{c^2}{3}=\frac{c^2}{6}$, attained at $\ell=c$ by the bound $cA-b/2\le\frac32A(c/3-A)+\frac{c^2}{6}$. No Fourier constant and no ill-defined kernel $|x|^{-1}$ enters (the covariance is $\delta_0$ directly). $c=0$: the energy is $\sup(-\frac b2)=0$, approached along $f_\ell$ as $\ell\downarrow0$ with no zero-scale unit vector.

**Condition/risk.** The witnessing profile is a **full-$H^1$ energy optimizer, not a compact stochastic control**: the bridging to compact controls is the earlier compact-approximation statement (`P:spatial-four-linear`, compact truncation/mollification in $H^1$), which is the "actual 138-approximation" condition — it is *not* reproved here. At $c=0$ the optimizer degenerates as $\ell\to0$; this is the zero-limit identity, never a zero-scale profile.

---

## PROOF212 (derived, mandatory)
Label `T:white-moment-bounds` (statement_LF 110–121, proof_LF 123–138).

**Statement (exact).** For $\Gamma=c\delta_0$, $0<a<1$, the intrinsic constant satisfies
$$\frac23\sqrt{\frac{c}{M_a}}\le C_2(c,a)\le\frac23\sqrt{c\,K_0(a)},$$
where
$$K_0(a)=\frac{2^a}{1-a},\qquad M_a=\frac{\Gamma_E((1+a)/2)}{\Gamma_E(1+a)\Gamma_E((1-a)/2)}.$$
The time exponent is $\frac{3-a}{2}$. These are **bounds**, not a numerical evaluation of the intrinsic supremum. Here $c$ is covariance mass; the unit-noise coefficient would be $\sqrt c$; kinetic coefficient is one.

**Deduction.** $q=3,k=2,m=\frac qk=\frac32$. `E:spatial-static-energy-score` gives $F_0(z)=2[(2z)^{1/2}/(8\cdot3^{3/2})]^{1/2}$. With $\sqrt{2\mathcal E_{\mathrm{sp}}}=c/\sqrt3$, one gets $F_0(\mathcal E_{\mathrm{sp}})=\frac{\sqrt c}{3\sqrt2}$, hence $2^mF_0(\mathcal E_{\mathrm{sp}})=\frac23\sqrt c$. PROOF209 then yields the two bounds with $M_a^{-1/2}$ and $K_0^{1/2}$. All Gamma/Beta factors are positive and finite for $0<a<1$. At $c=0$, $u=1$, $C_2=0$; both bounds vanish.

**Condition/risk.** Substitution of $q=3,k=2,m=3/2$ is exact; no endpoint value is taken; the output is a bracketing of $C_2$, not an evaluation. The white spacetime noise amplitude convention is $\sqrt c$ (variance mass $c$); no extra temporal normalization is inserted.

---

## PROOF213 (derived, mandatory)
Label `C:white-relative-width` (statement_LF 140–148, proof_LF 150–173).

**Statement (exact).** For $c>0$, the ratio of the upper and lower bound *formulas* satisfies
$$\sqrt{K_0(a)M_a}\le\left[\frac{\sqrt\pi}{2\,\Gamma_E(5/4)^2}\right]^{1/2},$$
with equality at $a=1/2$.

**Deduction.** Gamma duplication/recurrence:
$$\Gamma_E(1+a)=\frac{2^a\Gamma_E((1+a)/2)\Gamma_E(1+a/2)}{\sqrt\pi},\qquad
(1-a)\Gamma_E\left(\frac{1-a}{2}\right)=2\Gamma_E\left(\frac{3-a}{2}\right),$$
hence
$$K_0(a)M_a=\frac{\sqrt\pi}{2\Gamma_E(1+a/2)\Gamma_E((3-a)/2)}.$$
Put $x=1+a/2$, $y=(3-a)/2$, $x+y=5/2$. In Euler's integral the functions $t^{(x-1)/2}e^{-t/2}$ and $t^{(y-1)/2}e^{-t/2}$ have squared norms $\Gamma_E(x),\Gamma_E(y)$ and inner product $\Gamma_E(5/4)$; Cauchy–Schwarz gives $\Gamma_E(x)\Gamma_E(y)\ge\Gamma_E(5/4)^2$, with equality iff $x=y=5/4$, i.e. $a=1/2$. Swapping $a\leftrightarrow1-a$ exchanges $x,y$.

**Condition/risk.** Only the *ratio of the two computed bound formulas* is symmetric under $a\mapsto1-a$; the moment constant and the exponent $\frac{3-a}{2}$ are **not** symmetric, and no time-endpoint statement is made. No arXiv-v1 exact-p1 limit, no white-time boundary ($a=1$), and no strict Riesz $|x|^{-1}$ substitution is invoked.

---

## APPLICATION-POSITIVE-INTRINSIC-DERIVED-WHITE

**One coupled argument (exact transfer chain).**

**(0) Model facts maintained throughout.** Original canonical Stratonovich $u$ with data $(1,0)$; covariance amplitude original; kinetic coefficient one; Gaussian action $v_\Psi/2$; exponent $\kappa=\frac{4-\alpha-a}{3-\alpha}$ unchanged; all mixed/unequal/self/empty Stratonovich pairings retained; Green-width before noise-width in $d=3$; zero covariance handled by the direct zero identity; full nonseparable positive class $\mathcal C_{\mathrm{pos}}$ is the variational domain. The isonormal realization used in the upper is the **fixed-$W$ + one $J$ extension** (see GLOBAL-G8): no false W-only measurability of positive-cutoff point features is used.

**(1) PROOF194 → PROOF198.** A finite convex(max)-of-coercive-min dual identity on *entrywise* nonnegative PSD Grams, with the empty-subset value $0$ mandatory and no Loewner order, no global concavity, and no primal uniqueness. Componentwise the pass-through data are $\ell,c_D,D$ dual differences $D_A^D-D_A^C=\frac12 w^\top(D-C)w\ge0$ requiring only $D_{ij}\ge C_{ij}\ge0$.

**(2) PROOF199 → PROOF200.** The Bochner inclusion $J_G:L^2(I;G)\to H_t\widehat\otimes G$ with row constant $K_0=\frac{2^a}{1-a}$ promotes finite-cell indicator labels $h_i=\mathbf1_{I_i}/\ell_i$ tensored with (masked) squares $m_Rf_i^2$ into the raw $H_I$; the completed mean $\mathcal T_R$ turns $\Psi$ into the operator $B_E(m_Rh_{\Psi,s})$, and the label row is the multiplier form $v_{\mathcal T_R\Phi(s)}(f_i,f_i)$. The physical Gram matrices satisfy the exact entrywise order $0\le C^R_{ij}\le D_{ij}$ of PROOF198, because $0\le m_R\le1$ and $\Gamma$ is nonnegative.

**(3) PROOF201 before PROOF202.** The uniform optimizer radius $M=4C_{\mathrm{mean}}+4$ is proved from the exported rate bound $\mathrm{Rate}_R(\Phi)\le1+C_{\mathrm{mean}}\|\Phi\|$ *before* any averaging error is reused. This qualifies the unmasked finite optimizer $\Phi_D$ (positive conic combination, or zero) for the quantitative averaging error $e_n$, which is uniform in $R$ and valid on $\|\Phi\|\le M$.

**(4) PROOF202.** The signed score $\mathcal S_R$ is bounded by $S_2^{\mathrm{pos}}$ by: (a) cell-averaging $\mathrm{Rate}_R$ into Rayleigh sums of finite Gram entries within error $e_n$; (b) near-maximizing finite Rayleigh trials; (c) entrywise Gram comparison $C^R\le D$ (PROOF198); (d) PROOF201's bound on $\Phi_D$, then choice of a plateau $R'$, positive smooth approximation into $\mathcal C_{\mathrm{pos}}$, and the form-order bound (mask $\le$ unmasked). All limits are taken at the correct order; the errors are exactly $4e_n+2\varepsilon$, with the zero-optimizer branch closed by $S_2^{\mathrm{pos}}\ge0$.

**(5) PROOF203.** Fixing one positive test $\Psi$ before any mask/moment limit, masked rates converge to the unmasked Rayleigh rate (each fixed compact trial eventually in the plateau), dominated by $\sqrt{H_\Psi}$; hence $\liminf_R\mathcal S_R\ge S_2^{\mathrm{pos}}$, and PROOF202 gives the reverse; so $\mathcal S_R\to S_{2}^{\mathrm{pos}}$.

**(6) PROOF204.** The same canonical solution carries: upper = `P:original-signed-point-upper` (the F025 chain culminating at $\limsup_T\le\limsup_\delta\mathcal S_{\delta^{-1}+2}$) followed by PROOF203's cutoff limit; lower = `P:variational-positive-scores` (the F013 chain $\liminf_T\ge S_2^{\mathrm{pos}}$, finiteness/positivity funded by the independent 051 upper). Equality identifies the limit as
$$C_2=S_2^{\mathrm{pos}}=2^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}},$$
with $S_1^{\mathrm{pos}}$ auxiliary (not an actual $p=1$ moment, not a Chen constant).

**(7) PROOF205 → PROOF209.** The full-$H^1$ square map $Q$ realizes the raw occupation $\rho_g\in H_I$ with norm $A(g)$, pairing with $\Psi$ through the physical mean; the raw ratio $C_{\mathrm{occ}}=\sup_\mathcal O A/T^{\alpha/2}$ and dilation $A\to\ell^\alpha A$, $T\to\ell^2T$ give the penalty energy $\mathcal E_\zeta^{\mathcal O}=\zeta^{-\alpha/(2-\alpha)}\mathcal E_1^{\mathcal O}$; the near-Rayleigh Borel selection (207) optimizes $T$ then $v$, producing the scalar ceiling $U_c = c^{\frac{q}{k}}k[\alpha^{\alpha/2}C_{\mathrm{occ}}/(8q^{q/2})]^{1/k}$; inserting $C_{\mathrm{occ}}\le K_0R_{\mathrm{sp}}$ and $R_{\mathrm{sp}}\leftrightarrow\mathcal E_{\mathrm{sp}}$ gives the two-sided spatial-energy bracket; the strict $F_a>F_0$ gap is scalar convexity, with the legal negative comparison at penalty $\zeta=1$.

**(8) PROOF210 → PROOF213.** The square-map identity $b-2zA+z^2/3\ge0$ forces $3A^2\le b$, attained by noncompact $\operatorname{sech}$ profiles, giving the exact white energy $\mathcal E_{\mathrm{sp}}=c^2/6$ and the computed two-sided bounds $\frac23\sqrt{c/M_a}\le C_2\le\frac23\sqrt{cK_0(a)}$, whose ratio is Cauchy–Schwarz-maximized at $a=\frac12$. These are bounds on $C_2$, not evaluations; zero mass is direct zero.

The chain is the single coupled positive-intrinsic→derived-white deduction; it is not a conjunction of label checks.

---

## GLOBAL-UNPROVED-CONDITIONS

**G1. Independent upper finiteness (051 → 132), order fixed.** The finiteness of $S_2^{\mathrm{pos}}$ in PROOF202/204 is inherited from `P:variational-positive-scores` through the independently established Theorem `T:full-upper` (the CP-funded interval upper, funded by 001–051): $\E u^2(T,x)\le e(T+2)^d\exp\{C_{\mathrm{up}}T^\kappa\}$. The direction is **051 → 132 → 194–204**, not 204 → 202 or 132 → 051. Retained condition: `T:full-upper` is accepted as upstream; its derivation is not part of the B-batch.

**G2. Raw lower chain (120–132) and its half-action.** The lower bound consumed in 204 is `P:variational-positive-scores` with the raw-block lower `P:raw-block-original-lower` behind it: $\liminf_T\ge2I_\Psi-\frac12v_\Psi$ for each eligible positive control/mask, then mask removal and the score homogenization $S_c^{\mathrm{pos}}=c^{\frac{4-\alpha}{3-\alpha}}S_1^{\mathrm{pos}}$. Only the *raw half variance* $v_\Psi/2$ enters the action; the Gauss–Cameron change of law uses the whole given $W$ and a deterministic block mean. Retained conditions: the Cameron change-of-law on the norm-Borel space, the finite block cone (indexed ground/cone constants, order of choices $B,\omega,\varepsilon_{\mathrm{op}},c_*$), and the actual reset/restart on one retained source — all upstream of the B-batch.

**G3. Signed upper chain (156/170–193).** The upper consumed in 204 is `P:original-signed-point-upper`: with $R_\delta=\delta^{-1}+2$ and $\delta=T^{-\kappa}$,
$$\limsup_{T\to\infty}T^{-\kappa}\log\E|u(T,x)|^2\le\limsup_{\delta\downarrow0}\mathcal S_{R_\delta},\qquad \mathcal S_R\le2+2C_{\mathrm{mean}}^2.$$
Retained conditions: the compact-tube/Young/Rayleigh machinery (AWS realization, Borell 11.6 enlargement, mean and residual product envelopes, point transfer from the source-first cone identity). **The operative Gaussian law is fixed-$W$ plus one independent isonormal $J$ on the orthogonal complement**; the strengthening that positive-cutoff point features lie in $\Phi(H_W)$ (hence are $\sigma(W)$-measurable) is false (F194 explicit counterexample with $\langle v,q\rangle_{\mathcal G}\neq0$ for $q\perp\Phi(H_W)$), and no deduction in the chain may depend on W-only measurability.

**G4. Mean/spectral inputs to 199–203.** Retained exactly, with RHS statements: the compact map $C_t:H_t\to L^r(I)$, $2<r<2/a$; the completed mean $\mathcal T_R:H_I\to L^r(I;\mathcal K(E))$ with $\|\mathcal T_R\|\le C_{\mathrm{mean}}$ uniformly in $R\ge1$; the mean-row identity; $\mathrm{Rate}_R$ continuity and $\mathrm{Rate}_R(\Phi)\le1+C_{\mathrm{mean}}\|\Phi\|$; the uniform averaging error $e_n\to0$ on $\|\Phi\|\le M$. These are imported (F016, F018, F023), not re-derived inside 194–204.

**G5. CP import.** Only the bounded-operator Crouzeix–Palencia statement is used — arXiv-v1 Theorem 6, $\|F(T)\|\le(1+\sqrt2)\sup_{w\in W(T)}|F(w)|$ for bounded $T$ — funding the complex-phase propagator and hence 039→051→132. No "042" parent/book/journal equivalence and no invented generalization may be substituted.

**G6. Teschl imports (2nd ed., selected hypotheses only).** Closed semibounded form → unique self-adjoint operator (Thm 2.14, (2.63)); PVM/spectral calculus (Thms 3.1, 3.2, 3.6, (3.51)–(3.53)); max-min and form monotonicity (Thm 4.12, Cor 4.13); one-particle self-adjointness/essential spectrum (Thm 10.2); ground-state simplicity/positivity (Thms 10.12–10.13). These are used **only for compact/masked potentials and signed compact waves**; the unmasked $H_s=-\Delta-h_s$ is treated as a bounded ($L^\infty$) perturbation of $-\Delta$ with Rayleigh rate via trial density, and **no unmasked ground eigenfunction** is claimed anywhere in 199–213.

**G7. FH imports (2nd ed., selected only).** Young integration in infinite dimensions (1.5, p.13–14), the Young bound (4.1)–(4.3), p.61–62, and the set-enlargement Theorem 11.6 (Borell) with footnote 3 (the "outer-measure" measurability read). **Not imported:** generalized Fernique 11.7, Gaussian-rough-path Fernique 11.9, or any stronger Gaussian-tail theorem. The tube/radial tail argument is derived directly from the reproduced half-action Rayleigh density.

**G8. Fixed-W + one-J only.** The source/operator realization is the isometric feature embedding plus an independent auxiliary isonormal on the complement, retaining exactly the original $W$ on its first chaos. Every positive-cutoff source the upper compares may use $J$; no claim that sources or canonical terms are functions of $W$ alone is used, and the F194 counterexample (a legal $\mathcal G$-vector $q$ with $\int p\,\mathrm d\nu_a=0$, $\int_{(\cdot\le\Lambda)}p\,\mathrm d\nu_a=1$, giving $\langle v,q\rangle\neq0$) is retained as the disqualifier of the W-only strengthening. Zero covariance is the separate direct case.

**G9. White specialization conditions.** $d=\alpha=1$, $\Gamma=c\delta_0$ only; $0<a<1$ strictly (no white-time endpoint); bounds, not evaluations; the square map is the exact weak-$H^1$ identity; the $\operatorname{sech}$ family is a full-$H^1$ energy witness whose compact approximation must go through the four-linear $H^1$ extension; $c=0$ is the zero identity. No strict Riesz $|x|^{-\alpha}$ limit and no “$a=1$” substitution.

**G10. Chen 2023 non-use.** The 2023 variational-finiteness theorem is cited only in the explicitly identified auxiliary places (static finiteness, energy-fidelity) with Theorem 1.1 only; it does **not** fund the B-batch 194–213 and does not recursively fund 051/132. No gratuitous Chen-2023 paper input.

[held back: collaborators' unpublished work]

**G12. All-13 joins and whole-survey still owed.** `JOIN-POSITIVE-INTRINSIC` (194–204) and `JOIN-DERIVED-BOUNDS-WHITE` (133–143, 204–213) have `no_prior_label_discharges_this_join = true` and `final_genuine_whole_coupled_MAIN_still_required = true`; the component-level deductions of 194–213 do not discharge them. The remaining joins (including `JOIN-INDEPENDENT-UPPER` for 051 and `JOIN-UNMASK-FINITENESS` for 127–132 feeding this batch) remain scope context; the genuine full integrated review/visual/cold/delivery of the main is not completed by this batch.

**G13. Indefinite outputs kept open.** No numerical evaluation of the intrinsic supremum is produced; the white bounds bracket $C_2$; no attainment of the occupation ceiling, the spatial energy, or the bracket endpoints is claimed; positivity is only for nonzero covariance.