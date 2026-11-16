# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

Scope note. I read both supplied scientific views in full, statement-by-statement and proof-by-proof. Byte-exactness against the pinned original revisions is asserted by the supplied manifest and is not independently re-verifiable from the two extracted views; what I verified is content (sentence- and formula-level) equality of the two views’ statement/proof environments and the accuracy of the newly inserted explanatory prose. The eight statements are textually identical across views at the listed LF offsets. Four proofs (P:nogo-22, P:nogo-24, P:nogo-26, P:nogo-30) are textually identical apart from the LF shift; four (P:nogo-21, P:nogo-25, P:nogo-27, P:nogo-32) received only roadmap sentences plus `\medskip\noindent\textit{Step k.~}` headings, with every retained mathematical sentence identical. I found no lost steps, no qualifier changes, no constant/normalization changes, and no new defect.

---

## P:nogo-21
Old reading: COMPLETE. New reading: COMPLETE.
Argument preservation: PRESERVED. New explanations: JUSTIFIED.

The new opening (“We first construct a deterministic coefficient response that is not Hilbert–Schmidt, even after the stated observation cutoff. We then realize that coefficient as an actual covariance mean. Compatibility with a mean-square Hilbert–Schmidt driver would make this response Hilbert–Schmidt…”) and the five Step headings correctly partition the old argument: Steps 1–2 build and refute a non-HS response, Step 3 retains the failure under compact observation, Step 4 realizes the coefficient as a covariance mean, Step 5 derives the contradiction. All retained sentences match the old proof.

Public reconstruction: COMPLETE. Original-step coverage:

1. *Deterministic response.* With $B(b)(v,w)=(0,bv)$ and $S(u)$ the wave Fourier matrix, $A_h=\int_0^T S(-u)B(h(u))S(u)\,du$ is a strong operator integral on $E_s$: on compact time intervals $S(u)$ is strongly continuous and uniformly bounded, and multiplication by $H$ is bounded on $H^s$ because its weighted Fourier kernel is bounded by a constant times $\langle\xi-\eta\rangle^{|s|}|\widehat H(\xi-\eta)|$, an $L^1$ (hence $L^2$-bounded) convolution kernel.

2. *Lower-left kernel.* The $(2,1)$ block passes through $S(u)_{1,1}=\cos(u|\xi|)$, the multiplier $k(u)H$, and $S(-u)_{2,2}=\cos(u|\eta|)$. Conjugating by $\operatorname{diag}(\langle\xi\rangle^s,\langle\xi\rangle^{s-1})$ (output weight on the velocity coordinate) gives exactly
$$K_s(\xi,\eta)=(2\pi)^{-d/2}\langle\xi\rangle^{s-1}\langle\eta\rangle^{-s}\widehat H(\xi-\eta)\int_0^T k(u)\cos(u|\xi|)\cos(u|\eta|)\,du,$$
consistent with the displayed full product matrix whose lower-left entry is $\cos(ru)\cos(\rho u)$.

3. *Time-integral lower bound.* Write $r=|\xi|,\rho=|\eta|$; product-to-sum gives $\int k\cos(ru)\cos(\rho u)\,du=\tfrac12[\int k\cos((r-\rho)u)+\int k\cos((r+\rho)u)]$. For $|\xi-\eta|\le\varepsilon$ one has $|r-\rho|\le\varepsilon$ and $\varepsilon T\le1$, so $\cos((r-\rho)u)\ge\cos 1$ and the first integral $\ge J_0/2$. Integration by parts in the absolutely continuous $k$ gives $|\int_0^T k\cos((r+\rho)u)du|\le(\|k\|_\infty+T\|k'\|_\infty)/(r+\rho)=B_0/(r+\rho)$ (only the upper boundary survives since $\sin((r+\rho)\cdot 0)=0$). With $r\ge R_0=\max(1,2\varepsilon,4B_0/J_0)$, one has $B_0/(r+\rho)\le J_0/4$, so the time integral $\ge J_0/8$.

4. *Weight bound.* For $|\xi-\eta|\le\varepsilon\le 1\le r$, $|\langle\xi\rangle-\langle\eta\rangle|\le|\xi-\eta|\le1$, so $\langle\xi\rangle^{s-1}\langle\eta\rangle^{-s}=\langle\xi\rangle^{-1}(\langle\xi\rangle/\langle\eta\rangle)^s\ge c_s'\langle\xi\rangle^{-1}\ge c_s/|\xi|$ with positive constants absorbed into $c_s$ (the ratio bound is valid up to absolute constants; this matches the stated lower bound).

5. *Divergence.* Combining Step 4 with $\widehat H(z)\ge\widehat H(0)/2>0$ and the time bound, $|K_s|\ge c_s/|\xi|$ on $\{|\xi-\eta|\le\varepsilon,\ |\xi|\ge R_0\}$. The truncated kernel $P_NK_sP_N$ is $L^2$; the $\eta$-ball of radius $\varepsilon$ about each $\xi\in B_{N-\varepsilon}\setminus B_{R_0}$ lies in $B_N$, so
$$\|P_NK_sP_N\|_{\mathrm{HS}}^2\ge c_s^2|B_\varepsilon|\,|\mathbb S^{d-1}|\int_{R_0}^{N-\varepsilon}r^{d-3}\,dr\to\infty$$
($\log$ growth for $d=2$, linear for $d=3$). Since every block compression of a Hilbert–Schmidt operator has bounded HS norm, $A_h$ is not HS; complexification preserves HS norm.

6. *Cutoff retention.* With $\operatorname{supp}H\subset B_A$ and $\chi=1$ on $B_{A+T+1}$, finite propagation speed $1$ (from the energy-flux inequality $v_t\partial_n v-(v_t^2+|\nabla v|^2)/2\le0$, combined with time reversal) gives $D_\chi A_h=A_h=A_hD_\chi$.

7. *Covariance mean.* Since $\Gamma$ is nonzero Radon, choose $L_0$ with $0<\Gamma(B_{L_0})<\infty$; with $q\ge1$ on $B_{2L_0+1}$, $U=\Gamma*q$ is smooth even nonnegative with $U(0)>0$, and $Q=\int qU\ge|B_{L_0+1}|\Gamma(B_{L_0})>0$. With $H=\zeta U$ ($\zeta$ even, nonnegative, smooth compact, $=1$ near $0$), $f\in C_c^\infty(0,1)$ nonzero nonnegative and $k(u)=\int_0^1|u-v|^{-a}f(v)dv$, we get $k\ge\int f>0$ on $[0,1]$, $k\in C^1$ (by moving $\partial_u=-\partial_v$ onto $f$), $\mathbb E Z^2=Q\int_0^1fk\,du\in(0,\infty)$ for $Z=W(f\otimes q)$.

8. *Compatible adjoint/form (the sensitive step, unchanged and correct).* Since $S(-u)^*=S(u)$ holds only in the homogeneous $|D|$-weighted pairing, the proof correctly transposes in the $\Lambda$-weighted $E_s$ product, $W_s=\operatorname{diag}(\Lambda^{2s},\Lambda^{2s-2})$. Then $S(-u)^{*_{E_s}}=W_s^{-1}S(-u)^TW_s$, whose second row is $[\Lambda^{2-2s}(-\sin(u|D|)/|D|)\Lambda^{2s},\ \Lambda^{2-2s}\cos(u|D|)\Lambda^{2s-2}]$; hence $\Lambda^{2s-2}(S(-u)^{*_{E_s}}w)_2=-\frac{\sin(u|D|)}{|D|}\Lambda^{2s}w_1+\cos(u|D|)\Lambda^{2s-2}w_2$. Inserting $D_\chi^{*_{E_s}}=\operatorname{diag}(\Lambda^{-2s}\chi\Lambda^{2s},\Lambda^{2-2s}\chi\Lambda^{2s-2})$ produces exactly the stated $G_w(u)=\Lambda^{2s-2}((D_\chi S(-u))^{*_{E_s}}w)_2=-\frac{\sin(u|D|)}{|D|}(\chi\Lambda^{2s}w_1)+\cos(u|D|)(\chi\Lambda^{2s-2}w_2)$. This is precisely where “multiplication by $\chi$ has not been treated as self-adjoint” matters.

9. *Fubini and contradiction.* The raw covariance pairing yields $\mathbb E[Z\ell_\chi(z,w)]=\int_0^T\int k(u)H(x)v_u(x)G_w(u,x)\,dx\,du=\langle D_\chi A_h z,w\rangle_{E_s}=\langle A_h z,w\rangle$. If a realization $X\in L^2(\Omega;\mathrm{HS}(E_s,E_s))$ satisfied $\langle Xz,w\rangle=\ell_\chi(z,w)$ a.s. for each fixed Schwartz pair, then $\mathbb E[ZX]$ is a Hilbert–Schmidt Bochner integral $Y$ ($\mathbb E\|ZX\|_{\mathrm{HS}}\le(\mathbb E Z^2)^{1/2}(\mathbb E\|X\|^2)^{1/2}<\infty$), and $\langle Yz,w\rangle=\langle A_hz,w\rangle$ for all such pairs; Schwatz density forces $Y=A_h$, contradicting non-HS-ness.

Lost steps/qualifiers: none. The “for every fixed Schwartz pair” a.s. quantifier and the density/exceptional-set handling are unchanged. Pre-existing vs new concerns: no new concerns. The terseness of the ratio bound in Step 4 is pre-existing and is valid as reconstructed.

---

## P:nogo-22
Old reading: COMPLETE. New reading: COMPLETE.
Argument preservation: PRESERVED. New explanations: none added (proof text identical).

Public reconstruction: COMPLETE. Steps:

1. $\Gamma=\delta_0(dx_1)dx_2$ on $\mathbb R^2$ is nonnegative, even, positive definite and tempered with $\Gamma(cA)=c\Gamma(A)$, matching $d=2,\alpha=1$ in Hypothesis H:homog.
2. Spatial covariance seminorm: $B_\Gamma(g,g)=\int\Gamma(dy)\int g(x)g(x-y)dx=\int_\mathbb R(\int_\mathbb R g(x_1,x_2)dx_2)^2dx_1=:V(g)$ (the $\delta_0$ in $x_1$ collapses the shift, the $dx_2$ integral squares the marginal).
3. With $\chi=\psi^2$ ($\psi$ nonnegative nonconstant compact plateau), $g(x)=\chi(x_1)\chi''(x_2)$ and $\zeta(x)=\chi(x_1)\chi(x_2)=(\psi(x_1)\psi(x_2))^2$, a nonnegative smooth square mask. Then $\int\chi''=0$ gives $V(g)=0$; integration by parts gives $\int\zeta(x)g(x)dx_2=\chi(x_1)^2\int\chi\chi''=-\chi(x_1)^2\int(\chi')^2$, so $V(\zeta g)=\int\chi^4\,(\int(\chi')^2)^2>0$.
4. Tensoring with nonzero nonnegative $\tau\in C_c^\infty(0,T)$ gives $\mathbb E W(F)^2=\|\tau\|_a^2V(g)=0$ and $\mathbb E W(\zeta F)^2=\|\tau\|_a^2V(\zeta g)>0$ ($\|\tau\|_a^2>0$ by positivity of the time kernel).
5. Hence the family $F$ and $\zeta F$ are representatives whose mask separates the null class; no finite uniform covariance-norm multiplier bound can hold.

Lost steps/qualifiers: none. Pre-existing vs new: none.

---

## P:nogo-24
Old reading: COMPLETE. New reading: COMPLETE.
Argument preservation: PRESERVED. New explanations: none added.

Public reconstruction: COMPLETE. Steps:

1. Take nonzero $f$ Schwartz with Gaussian $\widehat f$; then $g=\Lambda^{-\gamma}f$ has $\widehat g=\langle\xi\rangle^{-\gamma}\widehat f$ nonzero Schwartz.
2. Plancherel and the sign convention give $\langle T_hg,g\rangle=\int e^{-i\xi\cdot h}|\widehat g(\xi)|^2d\xi$; since $|\widehat g|^2$ is Schwartz, its Fourier transform decays, so the inner product $\to0$ as $|h|\to\infty$.
3. Choose spacing $b$ and $h_n=nb e_1$ with $|\langle T_{h_n-h_m}g,g\rangle|\le\tfrac12\|g\|^2$ for $n\ne m$; then $\|T_{h_n}g-T_{h_m}g\|^2=2\|g\|^2-2\langle T_{h_n-h_m}g,g\rangle\ge\|g\|^2$, so the images have pairwise distance $\ge\|g\|$ and no Cauchy subsequence.
4. Inputs $T_{h_n}f$ have constant norm and their images under $\Lambda^{-\gamma}$ are $T_{h_n}g$ (translation commutes with the multiplier). Hence noncompact.

Lost steps/qualifiers: none. Pre-existing vs new: none.

---

## P:nogo-25
Old reading: COMPLETE. New reading: COMPLETE.
Argument preservation: PRESERVED. New explanations: JUSTIFIED.

The new roadmap (“translate unit controls beyond the supports of a fixed projection while enlarging the physical mask to contain them; a unit constant-displacement input then gives a nonvanishing operator lower bound”) and the two Step headings correctly describe the old two blocks: Step 1 builds unit controls killed by $P_J$; Step 2 retains a positive response inside the growing mask. All retained sentences identical.

Public reconstruction: COMPLETE. Steps:

1. By Lemma L:temporal-equilibrium (unassigned, used under its stated hypotheses), $f_a$ satisfies $\int_0^1|s-t|^{-a}f_a(t)dt=1$ and $\|f_a\|_{H_a}^2=M_a>0$.
2. With $\|q\|_2=1$ and $q_n=q(\cdot-x_n)$, $\Psi_n=(f_a\otimes q_n)/\sqrt{M_a}$ has raw norm one. Its covariance mean is constant in time: $h_{\Psi_n}(s)=(\int_0^1|s-t|^{-a}f_a(t)dt)\,q_n/\sqrt{M_a}=q_n/\sqrt{M_a}$.
3. The finitely many tests spanning $\operatorname{ran}P_J$ share a compact spatial support; by one-dimensional white-noise orthogonality ($\Gamma=\delta_0$ makes spatially disjoint controls orthogonal), $P_J\Psi_n=0$ exactly for all large $n$. Choose $R_n$ so $\operatorname{supp}q_n$ lies in the plateau of $m_{R_n}$.
4. $e=(0,0,1,0)$ has norm one. For $w_n=(0,\Lambda q_n/\|q\|_{H^{1/2}},0,0)$, the velocity norm is $\|\Lambda q_n\|_{H^{-1/2}}/\|q\|_{H^{1/2}}=\|q_n\|_{H^{1/2}}/\|q\|_{H^{1/2}}=1$ (translation invariance), so $w_n$ has norm one.
5. $T_{R_n}\Psi_n(s)e=(0,m_{R_n}h(s),0,0)=(0,q_n/\sqrt{M_a},0,0)$, and $\langle q_n,\Lambda q_n\rangle_{H^{-1/2}}=\langle \Lambda^{-1/2}q_n,\Lambda^{-1/2}\Lambda q_n\rangle_{L^2}=\|q_n\|_2^2$. Hence $\langle T_{R_n}\Psi_n(s)e,w_n\rangle_F=\|q_n\|_2^2/(\sqrt{M_a}\|q\|_{H^{1/2}})=:c_a>0$, constant in $s$.
6. Since $\Psi_n$ is unit and $(I-P_J)\Psi_n=\Psi_n$ for large $n$, $\|T_{R_n}(I-P_J)\|\ge(\int_0^1c_a^rds)^{1/r}=c_a$, giving $\sup_R\|T_R(I-P_J)\|\ge c_a$ with $c_a$ independent of $J$ and of $r$ (so valid for every $2<r<2/a$ as stated).

Lost steps/qualifiers: none; the finite-rank projection, the “for all sufficiently large n,” the exactness of $P_J\Psi_n=0$, and the phantom $\sup_R$ are all preserved. Pre-existing vs new: none.

---

## P:nogo-26
Old reading: COMPLETE. New reading: COMPLETE.
Argument preservation: PRESERVED. New explanations: none added.

Public reconstruction: COMPLETE. Steps:

1. For $D(t)=xt$, $U(t)=e^{xt}$, $\log U(1)=x$, $\|D\|_\infty=x$, and $[D]_{C^{2/3}}=\sup_{s\ne t}x|t-s|^{1/3}=x$, so $\|D\|_{C^{2/3}}=2x$.
2. Any universal bound $x\le C(2x)^{3/2}$ fails for $x=1/(16C^2)$: $C(2x)^{3/2}=C\cdot 2^{3/2}x^{3/2}=x/\sqrt2<x$. So no finite $C$ works (with $\nu=3/2=1/\theta$).
3. Second assertion: $b_1=N^{1/r}$, $b_j=0$ ($j>1$) gives $N^{-1}\sum b_j^r=1$ but $\max_j b_j=N^{1/r}\to\infty$; no $N$-independent bound holds.

Lost steps/qualifiers: none. Pre-existing vs new: none.

---

## P:nogo-27
Old reading: COMPLETE. New reading: COMPLETE.
Argument preservation: PRESERVED. New explanations: JUSTIFIED.

The added roadmap (“normalize a concentrating temporal test in the covariance norm; its local lower bound disproves boundedness above the threshold; pointwise decay away from its center separately disproves compactness at the endpoint”) and the two Step headings correctly describe the two old blocks. All retained sentences identical.

Public reconstruction: COMPLETE. Steps:

1. For $\phi\in C_c^\infty(-1,1)$ nonzero nonnegative and $v_\phi=\iint\phi(u)\phi(v)|u-v|^{-a}dudv>0$, set $f_\epsilon=\epsilon^{a/2-1}\phi((\cdot-t_0)/\epsilon)/\sqrt{v_\phi}$. The change of variables $t=t_0+\epsilon u$, $s=t_0+\epsilon v$ gives $\|f_\epsilon\|_{H_a}^2=v_\phi^{-1}\epsilon^{a-2}\cdot\epsilon^2\epsilon^{-a}v_\phi=1$.
2. At $t=t_0+\epsilon y$, $C_af_\epsilon(t_0+\epsilon y)=\epsilon^{-a/2}v_\phi^{-1/2}\int|y-v|^{-a}\phi(v)dv$. For $|y|\le1$ and $v\in(-1,1)$, $|y-v|\le2$, so the integral $\ge2^{-a}\int\phi>0$.
3. Hence $\|C_af_\epsilon\|_{L^r}^r\ge c_r'\epsilon^{1-ar/2}$, so $\|C_af_\epsilon\|_{L^r}\ge c_r\epsilon^{1/r-a/2}$, and $\sup|C_af_\epsilon|\ge c\epsilon^{-a/2}$. The exponent $1/r-a/2<0$ exactly when $r>2/a$, giving unboundedness; the supremum bound covers $r=\infty$.
4. For fixed $t\ne t_0$, $|t-s|$ is bounded below on $\operatorname{supp}f_\epsilon$ for small $\epsilon$, and the scaling gives $C_af_\epsilon(t)=O_t(\epsilon^{a/2})\to0$.
5. At $r=2/a$ the exponent $1/r-a/2$ vanishes, so $\|C_af_\epsilon\|_{L^{2/a}}\ge c>0$ while $C_af_\epsilon\to0$ pointwise off $t_0$. A strongly convergent subsequence would pass to an a.e.-convergent subsequence whose limit must be $0$, contradicting the uniform positive norm; hence noncompactness at the endpoint.

Lost steps/qualifiers: none. Pre-existing vs new: none.

---

## P:nogo-30
Old reading: COMPLETE. New reading: COMPLETE.
Argument preservation: PRESERVED. New explanations: none added.

Public reconstruction: COMPLETE. Steps:

1. With $(e_n)$ the standard ON sequence, $J_n(h)=(1-2\|h-e_n\|)_+$ is continuous on $\ell^2$.
2. For fixed $h$, $\langle h,e_n\rangle\to0$, so $\|h-e_n\|^2=\|h\|^2+1-2\langle h,e_n\rangle\to\|h\|^2+1\ge1$, hence $1-2\|h-e_n\|\to1-2\sqrt{\|h\|^2+1}<0$ eventually, so $J_n(h)=0$ eventually; $J_n\to0$ pointwise.
3. $J_n(e_n)=1$, so $J_n(e_n)-\tfrac12\|e_n\|^2=1-\tfrac12=\tfrac12$, giving $\sup_h\{J_n(h)-\tfrac12\|h\|^2\}\ge\tfrac12$ with norm-one witnesses $e_n$.
4. $\sup_h\{0-\tfrac12\|h\|^2\}=0$ (attained at $h=0$); the pointwise limit’s supremum is strictly smaller than the pointwise supremum of the scores.

Lost steps/qualifiers: none. Pre-existing vs new: none.

---

## P:nogo-32
Old reading: COMPLETE. New reading: COMPLETE.
Argument preservation: PRESERVED. New explanations: JUSTIFIED.

The added roadmap (“construct a feature-space vector orthogonal to every raw-noise test but not to the cutoff point feature; this separates the point feature from the closed noise image and gives a positive conditional variance”) and the three Step headings correctly partition the old proof (witness norm; orthogonality to the image; separation and conditional variance). All retained sentences identical.

Public reconstruction: COMPLETE. Steps:

1. $\|g\|_{H_\Gamma}^2=\int p_{2\varepsilon}(y)\Gamma(dy)\in(0,\infty)$: finiteness from temperedness and Gaussian decay; strict positivity from nonzero nonnegative $\Gamma$ and $p_{2\varepsilon}>0$. Then $\|v\|_{\mathcal G}^2=\|g\|^2\int_{r\le t_0}2\lambda e^{-2\lambda(t_0-r)}dr\,\nu_a(d\lambda)=\|g\|^2\nu_a((0,L])<\infty$ (the $r$-integral equals $1$), so $v\in\mathcal G$.
2. With $p=u_A/\int u_A\,d\nu_a-u_B/\int u_B\,d\nu_a$ supported in disjoint compact intervals $A\subset(0,L)$, $B\subset(L,\infty)$, one has $\int p\,d\nu_a=0$ and $\int_{(0,L]}p\,d\nu_a=1$. For $q(\lambda,r)=p(\lambda)(2\lambda)^{-1/2}(\varphi'(r)+\lambda\varphi(r))g$ with $\varphi\in C_c^\infty(0,\infty)$, $\varphi(t_0)=1$: $\int(\varphi'+\lambda\varphi)^2dr=\|\varphi'\|_2^2+\lambda^2\|\varphi\|_2^2$ (the cross term vanishes since $\int\varphi'\varphi=\tfrac12\varphi^2|$ is zero for compact $\varphi$), giving the displayed $\|q\|_{\mathcal G}^2$ finite because $p^2/\lambda$ and $\lambda p^2$ stay bounded away from $0,\infty$.
3. Using the isometry $\Phi F(\lambda,r)=\sqrt{2\lambda}\int_{t>0,t\ge r}e^{-\lambda(t-r)}F_tdt$ (Lemma L:source-retaining-isometry, unassigned) and the derivative identity $\frac{d}{dr}[e^{-\lambda(t-r)}\varphi(r)]=e^{-\lambda(t-r)}(\varphi'(r)+\lambda\varphi(r))$ (so $\int_{r\le t}e^{-\lambda(t-r)}(\varphi'(r)+\lambda\varphi(r))dr=\varphi(t)$), the coupling $\langle\Phi F(\lambda,r),q(\lambda,r)\rangle_{H_\Gamma}=p(\lambda)(\varphi'(r)+\lambda\varphi(r))\int_{t\ge r}e^{-\lambda(t-r)}\langle F_t,g\rangle dt$ integrates over $r$ and then over $\lambda$ to $\left(\int_{t>0}\langle F_t,g\rangle_{H_\Gamma}\varphi(t)dt\right)\int p\,d\nu_a=0$.
4. Smooth compact raw tensors are dense in $H_W$ and $\Phi H_W=K$ is closed, so $\langle\cdot,q\rangle$ vanishes on a dense subset and hence on $K$: $q\perp K$.
5. For the point feature, the same computation with $v$ gives $\langle v,q\rangle_{\mathcal G}=\varphi(t_0)\|g\|^2\int_{(0,L]}p\,d\nu_a=\|g\|^2>0$. Since $q\perp K$, $\langle v,q\rangle=\langle (I-P)v,q\rangle$, so $(I-P)v\neq0$.
6. With $J$ independent of $W$, $\operatorname{Var}(\mathcal I(v)\mid\sigma(W))=\operatorname{Var}(J((I-P)v))=\|(I-P)v\|^2\ge|\langle v,q\rangle|^2/\|q\|^2>0$ (Cauchy–Schwarz in $K^\perp$).

Lost steps/qualifiers: none; the positive finite cutoff $L$, $t_0>0$, the extension $K=\Phi H_W$ closed, and the conditional-variance statement are preserved. Pre-existing vs new: none.

---

## Findings and limits

All eight assigned statements are textually identical between the OLD and NEW scientific views at the listed LF ranges. Four proofs are textually identical apart from LF shift (P:nogo-22, P:nogo-24, P:nogo-26, P:nogo-30). Four proofs (P:nogo-21, P:nogo-25, P:nogo-27, P:nogo-32) received only outside-proof administrative roadmap sentences plus `Step k.` headings; in each case the heading scopes exactly match the deduction blocks they label, and no retained sentence, constant, normalization, hypothesis, projection, test, extension, or exceptional-set quantifier changed. The newly inserted explanations accurately summarize the underlying deductions and introduce no new mathematical assertion; hence they are JUSTIFIED.

Reconstruction status is COMPLETE for all eight proofs as detailed above. The only external inputs invoked, each under its checked hypotheses and with its own proof left unassigned, are: Hypothesis H:homog (baseline), the temporal equilibrium density of Lemma L:temporal-equilibrium (integrated_temporal_equilibrium), and the retaining isometry $\Phi$ of Lemma L:source-retaining-isometry (integrated_source_convergence); all display exactly the statements used. One sensitive point was checked in detail and found correct in both views: the Sobolev-adjoint transposition in P:nogo-21, including the explicit non-self-adjointness of $\chi$ on $E_s$, which is necessary for the claimed $G_w$ identity.

Limitations: (i) byte-exactness against the pinned original revisions is asserted by the provided manifest and is not re-derivable from the two extracted views alone; I verified content equivalence, not raw bytes. (ii) A few pre-existing tersenesses were reconstructed and found valid (e.g., the ratio constants absorbed into $c_s$ in P:nogo-21, Step 4; the integration-by-parts constant $B_0/(r+\rho)$ in P:nogo-21, Step 3) and are not new concerns. (iii) No primary-source theorem/PDF normalization was re-verified beyond the supplied statements. No new defect, lost step, or changed qualifier was identified.
