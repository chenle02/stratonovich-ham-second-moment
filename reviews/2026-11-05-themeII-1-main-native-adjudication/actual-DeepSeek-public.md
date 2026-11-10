## 0. Scope and method of this review

**Reviewed science.** The complete current af97 manuscript (28 modules) is supplied. This review assesses **only** the three canonical Theme II joins

1. `JOIN-CONSTRUCTOR`,
2. `JOIN-DRIVER-SOURCE`,
3. `JOIN-F-YOUNG-OBSERVABLE`,

with their actually consumed applications at `E124/125` and `G189`, and the cross-owner clauses those joins consume (`004/005/006/007/008/009/214`, `061–111`, `S064`). Everything else (Theme I owners, the other ten joins, `H` positive-matching, white evaluation, whole-project completion) is **not** checked here and is not cleared by this report.

**Method.** This is a literal mathematical reconstruction, not a hash check and not a reading of prior grades. Historical author capsules, native reports and annotations are used only as evidence to *challenge*, never as premises; procedural assignments inside them are nonoperative. Where a historical public report contained a wrong formula or an overbroad caption, I check the **current source** rather than inherit the error.

**Notation/conventions.** \(a=\alpha_0\in(0,1)\), \(d\in\{1,2,3\}\), \(0<\alpha<d\) or \(\alpha=d=1\), \(\alpha+a<2\); \(\Gamma\) nonnegative even positive-definite temperate homogeneous Radon, spectral convention \(\Gamma=\int e^{i\xi\cdot x}\mu(d\xi)\) distributionally; data \((1,0)\); unitary spatial Fourier \(c_d=(2\pi)^{-d/2}\). No spectral/angular density, finite total \(\mu\), \(H^3\), Hilbert-valued white vector, or rough point trace is assumed. \(\Gamma=0\) is the direct zero branch.

---

## 1. `JOIN-CONSTRUCTOR`: original source to canonical mixed solution

### 1.1 Damped norms (PROOF004) — *sound*

Recall \((N_0,N_1,N_2)\) from `E:damped-norm-definitions`. Three normalizations are verified exactly.

* **Mass.** \(G_s(\mathbb R^d)=s\) (also \(d=3\) surface measure), so
  \[
  N_0(\theta)=\int_0^\infty e^{-\theta s}s\,ds=\theta^{-2}.
  \]
* **First norm.** \(\lambda=\theta u\), \(\xi=\theta\eta\), spectral homogeneity \(\mu(\theta A)=\theta^{\alpha}\mu(A)\):
  \[
  N_1(\theta)
  =\theta^{\alpha+a-2}
  \Gamma_E(a)^{-1}\int_0^\infty u^{a-1}
  \int\frac{\mu(d\eta)}{((1+u)^2+|\eta|^2)}\,du.
  \]
  Finiteness: near \(u=0\) needs \(a>0\); at infinity \((1+u)^{\alpha-2}u^{a-1}\sim u^{\alpha+a-3}\), integrable iff \(\alpha+a<2\). Correct.
* **Second norm.** \(s=u/\theta\), \(t=v/\theta\), \(\xi=\theta\eta\), \(\widehat G_{u/\theta}(\theta\eta)=\theta^{-1}\widehat G_u(\eta)\):
  \[
  N_2(\theta)^2=\theta^{a-2-2+\alpha}N_2(1)^2
  =\theta^{-(4-\alpha-a)}N_2(1)^2=\theta^{-\beta}N_2(1)^2,
  \quad \beta=4-\alpha-a.
  \]
  Nonnegativity holds because for each \(\xi\) the temporal form is a positive Laplace mixture of \(e^{-\lambda|s-t|}\).
* **Absolute majorant/tails.** On \(|\xi|\le 1\) use \(|\widehat G_s\widehat G_t|\le st\), on \(|\xi|>1\) use \(|\xi|^{-2}\) and \(\int_{|\xi|>1}|\xi|^{-2}\mu=\alpha V/(2-\alpha)\); the only time singularity is \(v^{-a}\). The marked-tail kernels \(K_M\le|\cdot|^{-a}\), \(K_M\to0\) off the diagonal, so both tails vanish by dominated convergence.
* **Smoothing/truncation do not increase the bounds.** The \(N_1\) integrand is nonnegative after the Laplace transform; for \(N_2\) the time quadratic form is first integrated at each \(\xi\), and a multiplier in \([0,1]\) is removed in the upper bound. This is correct and is *not* pointwise covariance monotonicity.

No computation error found. The source \((3.4)\) inner absolute value is immaterial here because the damped Green–heat transform is nonnegative; the source \((3.5)\) independent \(x,y\) second variable is the convention actually used. Both are recorded correctly in the manuscript.

### 1.2 Independent-origin Cauchy–Schwarz (PROOF214) — *sound*

The feature map
\[
h_\lambda(t,r)=\sqrt{2\lambda}e^{-\lambda(t-r)}\mathbf 1_{r\le t},
\qquad
\int_{\mathbb R}h_\lambda(t,r)h_\lambda(s,r)\,dr=e^{-\lambda|t-s|}
\]
reproduces the stationary kernel; the Bochner representation gives \(Q_L(f,g)=\langle F_L(f),F_L(g)\rangle\), and simultaneous translation of both variables plus Cauchy–Schwarz gives, for all predecessor origins,
\[
0\le Q(T_{A,a}G_1^0,T_{B,b}G_2^0)\le N_C(G_1)N_C(G_2),
\qquad
Q(T_{A,a}G_i^0,T_{A,a}G_i^0)=N_C(G_i)^2.
\]
The coefficient is **exactly one**, independent of origins, dimension, cap and masses; zero norms are handled without division. The **predecessor time offset \(A-B\) and spatial origin \(a-b\) remain** when variables are relativized. Consequently the source Case-2 printed offset-free equality is not used, and the hypotheses of the imported Theorem 3.1 are met with finite heat-weighted edge measures \(e^{-(\epsilon_j+\epsilon_h)|\xi|^2/2}\mu\), not the original infinite \(\mu\).

### 1.3 Spatial Wick measures and joint fixed orders (005/006) — *sound (named import)*

The positive-Laplace representation
\[
L_{\epsilon,D}(\lambda)
=\int e^{-\frac12\sum_e(\epsilon_j+\epsilon_h)|\xi_e|^2}
\prod_{l=1}^{2k}\frac1{(1+\lambda_l)^2+|\eta_l(\xi)|^2}
\prod_e\mu(d\xi_e)
\]
has nonnegative integrand; the wave–Brownian identity
\[
\int_0^\infty e^{-qt}G_t(dx)\,dt=\frac12\int_0^\infty e^{-q^2u/2}p_u(x)\,du\,dx
\]
holds by equal Fourier transforms \((q^2+|\xi|^2)^{-1}\). The Brownian occupation bound is derived by ordering the \(2j\) times, conditioning on the current largest remaining vertex, removing the paired vertices, and integrating the selected adjacent gaps with Dirichlet parameters; the resulting uniform total-mass bound contains the explicit \(2^{-2k-2}\) factor. Compactification \(y_l=e^{-r_l}\), Bernstein/Choquet polynomial uniqueness, continuity at zero, \(r_l=0\) face mass zero via \(\lambda_l\to\infty\), and positive-horizon-face nullity via disjoint dilation/local finiteness are all correct. The **undamped** measure is homogeneous of degree \((4-\alpha)k\); the damped measure is not claimed homogeneous. Empty-chain \(\ell=0\) faces are correctly not declared null.

The marked-tail estimate used by 006 is exactly
\[
0\le F_{\epsilon,0,D}-F_{\epsilon,\eta,D}
\le k\,e^{T_1+T_2}H^{k-1}\bigl(2A_{1/\eta}+B_{1/\eta}^2\bigr)\to0,
\qquad
H=\max(1,2N_1(1),N_2(1)^2).
\]
Each marked edge appears **once** in a first norm (source factor \(2\)) or **twice** in the paired second norm. The fixed-\(\eta\) spatial limit, Cauchy in \(\eta\), and the positivity squeeze for arbitrary vertex temporal widths \(\delta<\eta\) give the joint arbitrary-rate limit. The \(L^2\)-Cauchy argument uses the **common Gaussian family** with square **and cross** moments:
\[
\|Y_n^a-Y_n^b\|_2^2\to Q_n+Q_n-2Q_n=0,
\]
which is the joint-width conclusion, not marginal matching. Independent copies at different widths would not give this.

The only non-owned item here is the **interior induction of Chen author Theorem 3.1**, whose edgewise hypotheses and Case-2 bridge are owned (004/214). That is a legitimate named import, not a reason to reject 006.

### 1.4 Uniform vertex norms and mild identification (007/008/009) — *sound*

From 004 the norms obey \(N_0=\theta^{-2}\), \(N_1\le C_0\), \(N_2\le C_0\theta^{-1}\) for \(\theta\ge\theta_0\). Applying Theorem 3.1 to \(e^{-\theta r}G_r\) gives, for all vertexwise widths,
\[
\|Y_n^a(t,x)\|_2^2\le P_n e^{2\theta t}C_1^{n}\theta^{-2n},
\qquad P_n=\frac{(2n)!}{2^nn!}.
\]
Then \(\theta=\theta_0+n/t\) and \(P_n n^{-2n}\le 2^n/n!\) give
\[
q_n(t)=e^{\theta_0 t}\frac{C^{n/2}t^n}{\sqrt{n!}},\qquad
\sum_{n\ge0}\sqrt{n+1}\,q_n(T)<\infty
\]
by the ratio test. This is the width-uniform summability needed downstream; the extra \(e^{\theta_0 t}\) is legitimate and non-sharp, and it is **not** presented as an amplitude-homogeneous sharp estimate.

In 009 the occupied multiplication is the finite-degree bound
\[
\|HF\|_2\le 2\sqrt{n+1}\,\|H\|_2\|F\|_2
\]
on the closed total-degree-\({}\le n\) Gaussian polynomial space (creation/annihilation norms \(\sqrt{n+1},\sqrt n\)), permitting correlation. The infinite product \(W_a u\) is obtained by weighted *series* closure, not by applying the finite-degree bound to \(u\) directly. The Green averaging at a fixed external noise width uses the fixed random factor \(F_s\), the global \(L^2\) majorant \(M\), the compact modulus \(\omega(r)\), and the Gaussian tail \(\mathbb P(|Z_\eta|>r)\le\min(1,d\,\eta/r^2)\):
\[
\left\|\int(p_\eta*G_\tau)F_s-\int G_\tau F_s\right\|_2
\le \tau\Big(\omega(r)+2M\min(1,d\eta/r^2)\Big),
\]
first \(\eta\to0\), then \(r\to0\), then time dominated convergence. Green is removed **first** at positive noise widths. Then 006 removes the external width at fixed \(n\), and the order tail \(2\sum_{n>N}q_n\) closes the mild equation.

The historical native "generic \(R\)" overstatement is **not** in the current source: the source states the finite-degree/weighted-series conditions. So 009 is sound as written.

### 1.5 Mixed series and physical identification (002) — *sound*

Reversal to initial chains, pairing involution, odd/even Wick structure, all self/unequal/empty terms with coefficient one; product \(L^1\) convergence from \(L^2\); absolute double summability \(\sum_{m,n}\|X_m\|_2\|X_n\|_2\le Q_t^2\) before Fubini; monotone (in expected nonnegative pairwise terms) regrouping by total order. The physical identification of the **same** series with the mild solution is 009, not a uniqueness theorem. Neither 051 nor 132/204 is a premise.

**Join-1 verdict.** The constructor chain closes conditionally on (i) the imported Theorem 3.1 induction interior, whose hypotheses and Case-2 step have been owned, and (ii) the full internal measure-theoretic details of 005, which I matched but did not re-derive from first principles beyond the Brownian/Laplace structural argument. The explicit marked-tail constant \(H^{k-1}(2A_M+B_M^2)\) and the Green-first/width-uniform order are correct. No hidden circular use of a final moment bound appears in 004–009/002.

---

## 2. `JOIN-DRIVER-SOURCE`: both variances to the given-\(W\) path and retaining source

### 2.1 Two variance orientations (061–074)

The actual massless free matrix and the Sobolev dual wave
\[
G_w(t)=-\frac{\sin(t|D|)}{|D|}\Lambda w_1+\cos(t|D|)\Lambda^{-1}w_2
\]
are retained, as is the balanced cutoff adjoint \(D_\chi^{*,E}\). The normalized kernel
\[
K(t;\xi,\eta)=\frac{1}{\sqrt{\langle\xi\rangle\langle\eta\rangle}}
\begin{pmatrix}-b_rc_\rho&-b_rb_\rho\\ c_rc_\rho&c_rb_\rho\end{pmatrix},
\qquad
K(t;0,0)=\begin{pmatrix}-t&-t^2\\1&t\end{pmatrix}
\]
is correct, including \(b_0=t\), so no phase entry or zero-frequency sine quotient is lost. Its squared temporal bound is
\[
\|1_IK_{ij}(\cdot;\xi,\eta)\|_{H_a}^2\le A_T\,h^{2-a}\Phi_h(\xi,\eta),
\qquad
A_T=C_1(a)(1+T)^4.
\]
The two scalar row bounds use the even auxiliary measure \(\nu_R\) with
\[
\int\Phi_h(\xi,\xi-\lambda)\,\nu_R(d\lambda)\le K\,C_\nu B_\alpha(h)\langle\xi\rangle^{-2\gamma}.
\]
The **two orientations are distinct and both are used**:

*input family varying, output fixed*: finite two-component Cauchy–Schwarz gives factor \(4A_T\), and change \(\xi=\eta+\lambda\);
*output family varying, input fixed*: the conjugated Bessel inequality plus actual evenness of \(\nu_R\) reflects
\[
\int\Phi_h(\eta+\lambda,\eta)\,\nu_R(d\lambda)
=\int\Phi_h(\eta,\eta-\lambda)\,\nu_R(d\lambda),
\]
so the same row bound applies. This is a reflection fact about the **actual** even auxiliary measure, not a dropped matrix adjoint, and the two orientations are not statistically independent noises.

Both finite variances therefore give the same common budget
\[
b_I=4A_TKC_\nu\,h^{2-a}B_\alpha(h),
\qquad
B_\alpha(h)\in\{1,\ 1+\log(1/h),\ h^{1-\alpha}\},
\]
with the \(\alpha=1\) logarithm absorbed only in the strict gap \(2-a-2\beta>0\), and no \(\gamma=0\) or “iff” endpoint upgrade is made. Fourier normalization is consistent: the raw \(W\)-norm carries \((2\pi)^d\), and \((2\pi)^d c_d^2=1\) with \(c_d^2\) already in \(C_\nu\). The historical native report errors (missing Peetre power, false “iff \(p\gamma>d\)” necessity, “all \(\sigma,\gamma\) real” for the cutoff lemma, blanket \(p\ge1\) for the even finite Gaussian moments, and the misplaced dependency caption) are all **in the public records, not in the current source**. The current source states sufficient membership \(p\gamma>d\), real \(\sigma\), \(\gamma>0\), even \(q\ge2\) for the path moments, and the correct Peetre inequality.

### 2.2 Compact envelopes, trace tails, operator path (075–093)

For the finite coefficient family the two weighted variances
\[
V_{\text{out},N}\le b_1D_\gamma^2,\qquad V_{\text{in},N}\le b_1D_\gamma^2
\]
together with the two-sided localizations give the two **distinct** compact envelopes \(B_{\text{out}},B_{\text{in}}\), whose fixed trace powers equal \(\|K_{\text{out}}\|_{S_q}^q\) but whose operators are not equal. The tail argument uses compact eigenvalue domination and the displayed trace-power convergence
\[
\sup_{M>N}\mathbb E\Big\|\sum_{N<j\le M}W(f_j)A_j(I)\Big\|_{S_q}^q
\le\frac{(q-1)^{q/2}}{2}\Big(\operatorname{Tr}T_{\text{out},N}^{q/2}
+\operatorname{Tr}T_{\text{in},N}^{q/2}\Big)\to0.
\]
This is genuine compact-domination, not operator-power Loewner order. The finite Gaussian matrix bound (even \(q\)) retains the **average** of the two trace powers; the corrected \(n=16\) countercontrol \((288\text{ actual}, 144\text{ one-variance}, 1224\text{ average})\) confirms that dropping one direction is false.

The fixed-interval limit is a genuine \(L^q(\Omega;\mathcal B(E))\) Cauchy limit on the **original** \(\Omega\); the two admissible even \(q\)'s agree by uniqueness in probability; for each requested \(p\) one even \(q\ge p\) is chosen. The dyadic path construction fixes \(q_0\) before any limit with \(q_0\gamma>d\) and \(\beta-\eta-1/q_0>0\), then uses finite grid first, mesh second, and the lower-Hölder interpolation third; one a.s. \(C^\theta\)-convergent subsequence gives compact values at **all times on one event**. The output (PROOF093) is a centered Gaussian \(C^\theta(\mathcal B(E))\) path with \(L^p\) bound \(K\sqrt p\) and square-exponential norm, on the given \(W\), with the literal completed row. Fixed-interval Schatten moments at admissible even \(q\) are **not** a \(C^\theta S_q\)-valued path. All this is sound and is the correct fixed \(R,T\) object.

### 2.3 Retaining source and actual correlation (094–100)

The correlated Gaussian convex comparison (094) is exact. The transfer (095) uses the **uniform** variance bounds for source and full residual—supplied later by (098)—and the finite-head/tail estimate
\[
\|M_{Y_\rho}-M_R\|_{L^pB_\theta}
\le\sqrt{C_D}\,t_{N,p}+\sqrt{s_N(\rho)}\,\|M_N\|_{L^pB_\theta},
\]
where \(s_N(\rho)=\sum_{j\le N}\operatorname{Var}D_\rho(f_j)\to0\). The order is: fix \(N\) for the uniform tail, then remove widths for the finite head. No independence of source and residual is assumed, and indeed the heat residual generally correlates with the source; only the \(\lambda\)-disjoint part factorizes.

The retaining isometry (097) keeps the **given** \(W\) literally via \(I(\Phi h)=W(h)\) with the auxiliary \(J\) only on the orthogonal complement; \(r\) is an auxiliary coordinate, not negative-time noise. The joint source covariance
\[
\operatorname{Cov}(Y_{\epsilon,\eta}(t,x),Y_{\epsilon',\eta'}(s,y))
=K_{\max(\eta,\eta')}(t-s)\,\Gamma_{\epsilon+\epsilon'}(x-y)
\]
is the correct heat **sum**/time **max** rule, with temporal width handled as a Laplace prefix, not convolution. The residual splitting
\[
\|(I-Q_\rho)g\|^2=\|(I-P_\eta)g\|^2+\|P_\eta(I-C_\epsilon)g\|^2\le \|g\|^2
\]
uses orthogonal \(\lambda\)-ranges and gives source and residual domination by the raw norm with constants \(1\). This is the genuine second pair of variance obligations, and it is met.

**Join-2 verdict.** The given-\(W\) first-chaos interval/path operator and the correlated retaining source transfer are coherent at **fixed \(R,T\)**. The only substantive conditions are (i) the full current OWN frequency/cutoff/driver foundations being upstream lemmas, and (ii) the fact that the variance/trace/norm constants are fixed-\(R,T\), so this join neither implies nor requires the later \(F156\)–\(F158\) growing-radius estimates. No growing-radius source convergence, no \(C^\theta S_q\) path, and no spatial spectral density is asserted here.

---

## 3. `JOIN-F-YOUNG-OBSERVABLE`: full \(F\), Young UI, exact observables

### 3.1 Closed proper \(F\) and BOTH constant columns (104–106) — *sound*

\(F=E\oplus\mathbb R^2\) with total distributions \((e_1+c_1,e_2+c_2)\); constants are not Sobolev states because their Fourier transform is a nonzero multiple of \(\delta_0\), which is not locally \(L^2\). Hence \(iE\) is closed and **proper**, not dense. The cutoff \(L_\psi\) is bounded on \(H^{\pm1/2}\) by Peetre multipliers; the free group
\[
S_F(t)(e,c_1,c_2)=(S_E(t)e,c_1+tc_2,c_2)
\]
has the constant block \(\begin{pmatrix}1&t\\0&1\end{pmatrix}\). Both constant-response columns are built explicitly:
\[
A=iM_RL_\psi,\qquad A(0,1,0)=iM_R(\psi,0),\qquad A(0,0,1)=iM_R(0,\psi).
\]
The range \(iE\) does **not** annihilate the constant inputs; the physical mask is outside a \(\pi_C A=0\) shortcut. The ordinary response on all of \(F\)
\[
A_E^\rho(t)z=\int_0^t S_E(-r)B_F(b(r))S_F(r)z\,dr,\qquad
B_F(b)(e,c_1,c_2)=(0,b(e_1+c_1))
\]
uses total finite propagation to compare \(z\) with \(iL_\psi z\), not density of \(E\) in \(F\). Correct. The second free datum \((0,0,1)\) at constant coefficient would give displacement \(t\); dropping it would fail even the deterministic first response.

### 3.2 Linear Young construction (107) — *sound (import matched)*

The only direct external input is the published Banach bounded-bilinear Young remainder estimate (Friz–Hairer, θ>1/2), applied with the left order \(D(u,v)V(u)\). The local contraction and the zero-based difference recurrence
\[
E_1\le4a_K,\qquad E_2\le16a_K,\qquad E_3\le48a_K
\]
are correct; patching gives composition, local/global invertibility, and growth
\[
\|U_D\|_{\triangle}\le C_T\exp\big(C_T(1+\|D\|_{C^\theta})^{1/\theta}\big).
\]
The interaction \(U\) is norm-continuous in the triangle norm; the physical/free flow is only strongly continuous on states and is placed in the bounded-family topology. No nonlinear bounded-vector-field theorem, no FH11.6, and no operator-norm derivative of \(S\) is used. Sound.

### 3.3 Source/full-\(F\) UI on the original measure (108) — *sound*

The Gaussian driver has \(E X^{2n}\le K^{2n}(2n)^n\), so a small square-exponential moment exists. Together with the subquadratic exponent \(1/\theta<2\), one gets
\[
rC_T(1+x)^{1/\theta}\le c_0 x^2+C_r
\]
and therefore every finite flow moment and uniform integrability on the **original** probability measure; driver-ball convergence to probability convergence, then uniform moments to \(L^p\). This is *not* a square-exponential nonlinear-flow assertion and *not* a tilted-source limit. Correct.

### 3.4 Picard/Bochner observables (109/110) — *sound, with the required type distinction*

The phase Picard bound \(C_T^{n+1}B_T^nT^n/n!\) matches the scalar Green recursion \(t^{2n}/(2n)!\) by distributional testing/Fubini, including the \(d=3\) sphere measure. The bounded tested observable
\[
O_\phi(e,c_1,c_2)=\langle e_1,\phi\rangle+c_1,
\qquad
Z_m=O_\phi P_A(t,0)e_0
\]
is exactly the scalar tested displacement, and the pathwise/Bochner identity is obtained by the sign test using the uniform \(Q_t\) bound. Discharging 103 yields
\[
\mathbb E|Z_m(t,\phi)|^2\le \mathbb E|u(t,0)|^2.
\]
This is a **scalar** mean-square bound, not an \(H^{1/2}\) point trace, and **not** the spatial average-of-squares requested by G189.

### 3.5 `E124/125` noise-only ordered products — *sound with fixed-\(\delta\) stratification*

At fixed \(\delta,N,R\) and a fixed raw control \(\Psi\) (with original \(Z,v\)), the one retaining source pulled back by
\[
T_{\delta,m}f(s,x)=\delta^{a/2-1}f((s-m\delta B)/\delta,x)
\]
has raw covariance factor \(1\); the actual ordinary-source conjugation
\[
S_F(mB)\big[A_{\mathrm{glob}}(mB+u)-A_{\mathrm{glob}}(mB)\big]S_F(-mB)=X_m(u)
\]
follows by change of variables and is orientation-correct. Young uniqueness gives the restart \(P_{\mathrm{glob}}(mB+u,mB)=D_m^0(u)\). The ordered product uses the **true** terminal remainder \(\tau\) (including \(\tau=0\)); if stopped paths \(\min(u,\ell_m)\) are introduced, both sides are stopped consistently, not only one.

The explicit ordered-product limit holds at fixed \(n=N+1\):
\[
\|\prod F_{m,\rho}-\prod F_m\|_{L^2}
\le n\,\|C_\rho\|_{L^{4n}}^{n}\,\|e_\rho\|_{L^4}\to0,
\]
with \(C_\rho=\max(1,\dots)\ge1\) (the floor is essential; the \(\tau=0\) identity factor and the constant block give \(\|P_F\|\ge1\) for the actual factors). All moments are on the **original** measure, before any Gaussian law/density/tilt. Then the masked comparison at \(\Gamma_\delta=g_\delta^2\Gamma\) and the canonical moment/scale identities give
\[
\mathbb E\,U_{\delta,B}^2\le \mathbb E|u_{\Gamma_\delta}(L,0)|^2
=\mathbb E|u_{\Gamma}(T,0)|^2.
\]
Only the noise-only source product is passed to the masked comparison; the shifted raw product is already the everywhere-defined raw functional in the Gaussian shift
\[
\mathbb E\,U_{\delta,B}^2
=\mathbb E\Big[e^{-Z/\sqrt\delta-v/(2\delta)}Y_{\delta,B}^2\Big],
\qquad v/(2\delta) \text{ once}.
\]
No source limit under this density, no independent block actions, no scalar moment multiplication occurs.

### 3.6 `G189` physical square — *two separate fixed-\(\delta\) limits*

The prelimit identity is
\[
\mathbb E\|pr_1P_E^\rho(L,0)z\|_{L^2(D)}^2
=|D|\,\mathbb E|u_{\Gamma_\delta,\rho}(L,0)|^2.
\]
At fixed \(\delta,R_\delta=L+2\), two independent limit arguments are used:

1. \(D108\) fixed-parameter \(F\)-flow UI plus closed isometric restriction \(E\subset F\) gives \(L^2(\Omega;L^2(D))\) convergence of the displacement, hence
\[
\bigl|\mathbb E\|a_\rho\|^2-\mathbb E\|a\|^2\bigr|
\le\|a_\rho-a\|_{L^2}\bigl(\|a_\rho\|_{L^2}+\|a\|_{L^2}\bigr)\to0.
\]
2. Separately \(A006/A008\) plus the double-tail bound give the canonical unmasked point second-moment limit at \(\Gamma_\delta\):
\[
\mathbb E|u_{\Gamma_\delta,\rho}(L,0)|^2\to\mathbb E|u_{\Gamma_\delta}(L,0)|^2
\]
and spatial stationarity gives the prefactor \(|D|\). Only then is the canonical law/scaling applied.

This is an **average of squares**, distinct from the scalar 110 average, and no \(H^{1/2}\) point trace or masked-noise stationarity appears. The fixed-\(\delta\) order of both limits before \(\delta\downarrow0\) is preserved; no growing-cone diagonal follows.

**Join-3 verdict.** Coherent. The restrictions are: (i) the Young stability/UI is finite-parameter; (ii) the fixed-parameter \(E\|P_E\|^2<\infty\) here is obtained by the \(F\)-flow restriction clause of \(D108\), which is a stated same-clause alternative to importing the unrelated full \(G185\) tube proof; (iii) the strict \(h=0\) (noise-only) status of \(E125/G189\) is respected, with the general deterministic source perturbations \(D111/F166/F167\) handled separately as below.

---

## 4. `D111/F166/F167` boundary and the noise-only/general-mean split

* **\(D111\) deterministic base.** For a fixed smooth compact-in-space \(h\) on a fixed horizon the primitive budget
  \[
  \|A_h\|_{C^\theta}\le C_S^2(T+T^{1-\theta})M_h
  \]
  with \(M_h=\sup_r(\|h(r)\|_\infty+\|h(r)\|_2)\) is correct and permits bounded \(H/G\) families per horizon. For a width-varying \(h_\rho\), fixed-\(h\) 111 alone does **not** suffice: one must additionally have actual primitive convergence \(A_{h_\rho}\to A_h\) (or a uniform budget on the same \(h_\rho\) on both comparison sides). This is exactly what `F166` supplies for the covariance-duality mean,
  \[
  \|D_\Phi^\rho-D_\Phi\|_{C^\theta}\le\|\Phi\|_{H_W}\|M_R^\rho-M_R\|_{L^2C^\theta},
  \]
  which is a fixed-\(\Phi\) covariance bound directly from the retaining source \(L^2\) convergence and does **not** require the later \(132/R_{\mathrm{sp}}\) or the uniform physical/mean regulation. This fixed-\(F166\) subclause is therefore checked at the needed interface.
* **`F167` ordinary identification** and the later **uniform radius/rough signed mean/regulated physical class** (`F146`, `F154`, `F164`, general raw-ball/tubes/`132`,`R_{\mathrm{sp}}`) are **not** needed by and are **not** reconstructed in this theme-argument: they remain explicit conditional branches for the later general-mean stage.
* **Cycle audit.** The chain
  \[
  \text{noise-only }D\text{ source/UI}\to E125\to(\text{separate }E126)\to132
  \]
  precedes \(R_{\mathrm{sp}}\) and the physical-mean regulation; there is no \(132\to\) rough spaces \(\to\) noise-only \(126\to132\) feedback. The fixed-\(F166\) estimate is local and does not become an antecedent of the noise-only lower route. No same-law substitute for same-coupling convergence is used anywhere: \(E124/125\) and \(G189\) all use the **one retaining source** and the original measure.

---

## 5. Register: the 59+S064 roles

Legend: **OK** = deduction sound under its stated inputs, checked at source level; **IMP** = named external import acceptable (we verified hypotheses/application, proof interior remains named); **LIM** = explicitly limited/conditional, and the condition is stated.

| Proof | Formal | Status | Reason |
|---|---|---|---|
| 002 | S038 | OK | Self/unequal/empty pairs, coefficient one, absolute double sum, 009 identification; no uniqueness/final-bound premise. |
| 004 | S005 | OK | Exact \(\theta\)-scalings \(1,\alpha+a-2,-\beta\); nonnegative \(N_2\); tails; smoothing non-increase. |
| 005 | S007 | OK | Positive Laplace/Brownian mass, faces, homogeneity of undamped \(\rho_D\). |
| 006 | S008 | IMP-LIM | Joint rates and Green-first correct; interior induction of Chen Thm 3.1 named (edgewise hypotheses owned). |
| 007 | S009 | OK | Crude \(\theta=\theta_0+n/t\); corrected \(e^{2\theta_0t}\); non-sharp. |
| 008 | S010 | OK | Width-uniform \(q_n\), ratio-test summability. |
| 009 | S039 | OK | Occupied degree bound + weighted series + fixed-factor Green average; order first Green then noise widths. |
| 214 | S006 | OK | Coefficient-one independent-origin CS with finite heat-weighted edges. |
| 061 | S090 | OK | Single-Schwartz-test translated spectral growth; no oscillatory double Fubini. |
| 062 | S091 | OK | Auxiliary \(\nu_R\) growth \(C_\nu=c_d^2L^2C_\Gamma\), evenness, Hilbert contraction. |
| 063 | S086 | OK | Laplace factorization, Schur completion, separability. |
| 064 | S092 | OK | Raw norm \((2\pi)^d\), masked contraction into original \(L^2\). |
| 065 | S093 | OK | Physical mask need not descend to raw-null quotient. |
| 066 | S087 | OK | Moving endpoint and large-\(k\) IBP; squared norm \(C_0=16/(1-a)\). |
| 067 | S088 | OK | Difference/sum oscillatory modes; no independence. |
| 068 | S089 | OK | \(b_0=t\) via Bochner average; \(C_1=4\cdot3^{1-a}C_0\). |
| 069 | S095 | OK | Near/far shells, critical log only at \(\alpha=1\). |
| 070 | S099 | OK | Strict \(\beta\) window absorbs the logarithm. |
| 071 | S096 | OK | Actual dual wave, cutoff adjoint, normalized kernel, full admission. |
| 072 | S094 | OK | Both conjugated Hilbert-valued Bessel forms. |
| 073 | S097 | OK | Both orientation rows; reflection uses actual even \(\nu_R\). |
| 074 | S098 | OK | Both columns; no random bounded operator claim. |
| 075 | S100 | OK | Weighted AM–GM/Hölder/expectation. |
| 076 | S101 | OK | Trace word and Hölder bounds. |
| 077 | S104 | LIM | Finite Gaussian matrix, **even \(p=2m\)** and retained average; input to 083/090. |
| 078 | S102 | OK | Periodization/recovery, negative indices, Peetre correct. |
| 079 | S105 | LIM | Sufficient membership \(p\gamma>d\); no endpoint necessity or \(\gamma=0\). |
| 080 | S106 | OK | Nonselfadjoint balanced cutoff; equal singular budgets, distinct envelopes. |
| 081 | S103 | LIM | Eigenvalue/trace-power comparison only; **no** operator-power Loewner order. |
| 082 | S107 | OK | Localized finite variance under one-sided localizations. |
| 083 | S109 | LIM | Corollary valid only for even \(p\ge2\), \(p\gamma>d\). |
| 084 | S108 | OK | Plateau witness and \(\Lambda^{-\gamma}\) noncompactness; not Loewner power order. |
| 085 | S111 | OK | Separable infinite-dimensional ONB on nonzero quotient. |
| 086 | S112 | OK | Smooth masked coefficients after convolution; mask not commuted. |
| 087 | S113 | OK | Gain \(E_r\to E_{r+1}\), dual \(E_{2s-r-1}\to E_{2s-r}\); distinct choices \(\gamma-1/2\). |
| 088 | S114 | OK | Both noise-basis/phase-Parseval directions; positive strong tails. |
| 089 | S115 | OK | Compact domination plus finite spectral head gives trace-power decay. |
| 090 | S116 | OK | Retained average of two trace powers by compression/Fatou. |
| 091 | S117 | OK | Genuine Cauchy via \(\sup_{M>N}\) tail; compact limit on original \(\Omega\). |
| 092 | S118 | OK | \(q_0\) before limits; grid–mesh–interpolation; all-time compact event. |
| 093 | S119 | LIM | Centered Gaussian \(C^\theta\) path at fixed \(R,T\); no \(C^\theta S_q\) path or growing-\(R\) claim. |
| 094 | S120 | OK | Convex Gaussian comparison. |
| 095 | S124 | LIM | Needs uniform variance bounds (supplied in 098); finite head/tail order correct. |
| 096 | S121 | OK | Heat contractions on Radon \(\Gamma\), unitary factor \((2\pi)^d\). |
| 097 | S122 | OK | Retaining isometry; \(I(\Phi h)=W(h)\) literally. |
| 098 | S125 | OK | Max-time/heat-sum source law; correlated residual; both variance bounds. |
| 099 | S123 | LIM | Versions and increments at **each fixed positive width** only. |
| 100 | S126 | OK | Ordinary primitive equals transferred driver on coupling. |
| 101 | S127 | OK | Positive Green chain mass; Green square+\textbf{cross}; mask Wick comparison. |
| 102 | S128 | OK | Ordinary Picard/uniqueness at positive widths; Bochner average. |
| 103 | S129 | LIM | Canonical point moment limit; masked \(L^2\) convergence is a premise supplied by 110. |
| 104 | S130 | OK | \(F=E\oplus\mathbb R^2\), closed proper \(E\), free block \(\begin{pmatrix}1&t\\0&1\end{pmatrix}\). |
| 105 | S133 | OK | Both constant columns, range \(iE\) does not annihilate them. |
| 106 | S131 | OK | Ordinary response on all \(F\) via total finite propagation. |
| 107 | S134 | IMP-LIM | Banach Young remainder imported; own contraction/composition/inverse/growth derived. |
| 108 | S135 | LIM | All finite moments/UI on original measure, fixed parameters. |
| 109 | S132 | OK | Picard–Green phase/scalar identification. |
| 110 | S136 | OK | Scalar tested observable; completes 103; not G189 average. |
| 111 | S137 | OK | Deterministic base budget; varying \(h_\rho\) needs F166 convergence clause. |
| S064 | H:homog | GIVEN | Formal CONTEXT, logical global given; no proof body; never an unproved OWN theorem. |

No proof is declared whole-paper-HIGH by this table; `LIM` rows state exact residual conditions and remain literal.

---

## 6. Consumed application clauses (`E124/125`, `G189`, `F166/167`, `D111`)

* **`E124` restart (noise-only).** One retaining source, literal pullbacks \(T_{\delta,m}\), source conjugation orientation, physical restart by Young uniqueness, ordered product stopping at both cells and the true \(\tau\) (including \(\tau=0\)).
* **`E125` product comparison (noise-only).** \(C_\rho\ge1\) floor, ordered product \(L^2\) limit on the original measure at fixed \(n=N+1\), masked Wick comparison at \(\Gamma_\delta\), canonical point limit, law scaling, and the one original slow \(Z,v\) — no tilted source limit.
* **`G189` physical square (noise-only).** Two fixed-\(\delta\) limits (`L^2(\Omega;L^2(D))` displacement then expected squared norm; then unmasked canonical point moment), average **of squares**, spatial stationarity \(|D|\), plateau \(R=L+2\) not the \(E125\) mask.
* **`F166` fixed-\(\Phi\) covariance dual.** \(D_\Phi=\mathbb E[W(\Phi)M]\), source bound \(\|\Phi\|_{H_W}\|M^\rho-M\|_{L^2C^\theta}\); local, no \(132/R_{\mathrm{sp}}\).
* **`F167` ordinary identification.** Separate; **not** needed and **not** reconstructed here.
* **`D111` base perturbations.** Fixed \(H/G\) per horizon; width-varying \(h_\rho\) requires primitive convergence + uniform budget.

**Noise-only/general-mean boundary.** Everything funding \(126\)'s lower and the \(G189\) source limit is \(h=0\) (noise-only) on the original measure. The uniform-radius raw-ball/physical-mean regulation, rough signed wave `164`, completed/regulated means `146/154`, `132/R_{\mathrm{sp}}` and later Gaussian tubes are **explicit conditional branches** of the later general-mean stage and are not borrowed to finance this theme argument.

---

## 7. Unforced scoped verdict, confidence and remaining conditions

**Verdict.** Under the stated current OWN inputs, the three assigned joins are mathematically coherent, and I found no concrete wrong formula, limit-order reversal, or circularity in the specified deductions at the source level. The intermediate calculations that were load-bearing (norm scalings, marked-tail constant, both variance rows with reflection, retained trace-power average, head/tail source transfer, Young local contraction, fixed-\(\delta\) ordered product, and the average-of-squares transfer) all reproduce correctly.

**This is not whole-paper clearance.** The joins remain conditional on:

1. the **named imports** — the interior induction of Chen author Theorem 3.1 (edgewise hypotheses and Case-2 bridge owned) and the Friz–Hairer Banach Young remainder estimate; both may remain imports after the exact hypothesis/application checks performed above, and no full book reproof is being demanded;
2. the **full internal proofs of the upstream OWN foundation lemmas** (wave/compactness/dyadic driver chain, positive spatial Wick uniqueness, external point/radial foundations), which I matched at their application interfaces but did not re-derive from first principles in every measure-theoretic \(\varepsilon\)-step;
3. the explicit **`LIM` rows** in the register (fixed \(R,T\) path scope, even \(q\), sufficient \(p\gamma>d\), masked \(L^2\) premise, positive-width versions, finite-parameter UI).

**Confidence.** Medium (not high), scoped to “the three joins close conditionally and no new source defect was located in this pass.” A high confidence would require the independent re-derivation of the named imports and the complete internal finiteness/continuity steps that the manscript circumscribes but which this assignment does not request as full-book reproofs.

**Required repairs/limitations carried forward (literally).** The historical public-record errors — the C Peetre lost power, the false “iff \(p\gamma>d\)”/over-broad \(\sigma,\gamma\) and even-\(p\) captions, the D “tested average” conflation of \(G189\) with a scalar average, and the A generic-\(R\) Green-multiplication wording — are **report errors, not current-source errors**; the current source states the correct formulas. These remain attached to their records and do not become premises. The general-mean/branch applications remain uncompleted and are explicitly outside Theme II.1.

No final cold/source/visual/Kimi clearance and no completion of the whole 214/240/13 goal is claimed from this assignment.