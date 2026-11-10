## PROOF001

**Source record.** Path `notes/notes_stratonovich_ham_second_moment.tex`; module SHA-256 `516d6a650bdac7d3da68672f37836afd084b651c39553b43d5135d0512e39d14`; statement_LF `[367,378]`, proof_LF `[380,393]`; raw proof body SHA-256 `adc019e1d6e0a1941c8ab725c147843ef332c0979c75a9d238fa4fdf31d7d2db`; full proof environment SHA-256 `e3b8a760af6e040053144927eea9367ec84635901d4ea683ebe06038d2153dbd`.

### Statement

Under Hypothesis H:homog,

\[
\mathbb E u(t,x)\ge 1,\qquad
\mathbb E u^2(t,x)\ge \bigl(\mathbb E u(t,x)\bigr)^2.
\]

Consequently, for every real \(\ell\),

\[
\liminf_{t\to\infty}t^{-\kappa}\log \mathbb E u(t,x)\ge \ell
\quad\Longrightarrow\quad
\liminf_{t\to\infty}t^{-\kappa}\log \mathbb E u^2(t,x)\ge 2\ell.
\]

The specialization \(\ell=L_*\) is explicitly conditional on the intended first-moment lower bound with that constant, not an unconditional adoption of the printed normalization.

### Derivation

For each fixed \((t,x)\) the proof first appeals to Lemma L:vertex-crude (PROOF008) to get
\[
\sum_{n\ge0}\|X_n(t,x)\|_2<\infty,
\]
the proof of which does not use the present proposition. Hence \(\sum_n\mathbb E|X_n(t,x)|<\infty\), so the mean of the canonical series is the sum of its means.

By the expansion \(\eqref{E:expansion}\) and the even-Wick formulas (2.20)–(2.21),
\[
\mathbb E u(t,x)=\sum_{n\ge0}\mathbb E S_{2n}(g_{2n}(\cdot,t,x))\ge 1,
\]
since
- every term is a pairing integral of a nonnegative integrand (positivity of the covariance and Green factors),
- \(S_0=1\).

By Cauchy–Schwarz,
\[
\mathbb E u^2(t,x)\ge \bigl(\mathbb E u(t,x)\bigr)^2,
\]
so
\[
t^{-\kappa}\log\mathbb E u^2(t,x)\ge 2\,t^{-\kappa}\log\mathbb E u(t,x).
\]
Taking lower limits gives the implication for every valid \(\ell\).

**Simplest cases.** At zero covariance one gets \(u=1\), both sides are \(0\), and the implication is vacuous but valid. At any fixed order the nonnegativity reduces to \(\mathbb E S_{2n}^2\ge(\mathbb E S_{2n})^2\).

**Consumed hypotheses.** H:homog; the existence of the series \(\sum X_n\) with absolute \(L^2\) summability from PROOF008; the nonnegative pairing-integral identification of \(\mathbb E S_{2n}\) (from PROOF002’s mixed identity at \(m=n\), and PROOF006 for the fixed-order construction).

**Unproved conditions.** The unconditional numeric constant \(2L_*\) requires the separate first-moment lower bound \(L_*\). The Jensen implication itself is unconditional once the series identification is granted; it does not itself prove any positive growth rate.

## PROOF002

**Source record.** Same module; statement_LF `[437,452]`, proof_LF `[454,510]`; raw proof body SHA-256 `0927bc947ce1a000eba63bdd55320c069a906b5734d08652253679940735d228`; full proof environment SHA-256 `e9234e8d7e8d80b5d8a7ecb13336d3fce9f0f3af60e7bc59de6fead3b1d99c6f`.

### Statement (complete ordered-chain Wick products)

Put \(X_n(t,x)=S_n(g_n(\cdot,t,x))\), \(X_0=1\). For \(m+n=2k\), the two chains are \(I_1=\{1,\dots,m\}\), \(I_2=\{m+1,\dots,m+n\}\). For \(D\in\Pi_k\),

\[
J_{m,n,D}(t)
=\int_{[0,t]^m_<\times[0,t]^n_<}\mathrm d\boldsymbol s
\int_{(\R^d)^{m+n}}\mathrm d\boldsymbol y
\prod_{\rho=1}^2\prod_{l\in I_\rho}
G(s_l-s_{p(l)},y_l-y_{p(l)})
\prod_{(j,h)\in D}|s_j-s_h|^{-\alpha_0}\gamma(y_j-y_h),
\]

where \(p(l)\) is the preceding label in its own chain and at the first vertex of either chain the common root is used: \((s_{p(l)},y_{p(l)})=(0,0)\). An empty chain contributes factor one.

Then under H:homog,

\[
\mathbb E[X_m(t,x)X_n(t,x)]
=
\begin{cases}
\sum_{D\in\Pi_k}J_{m,n,D}(t), & m+n=2k,\\
0, & m+n\ \text{odd}.
\end{cases}
\]

In particular

\[
\mathbb E u^2(t,x)=\sum_{k=0}^{\infty}\sum_{m=0}^{2k}\sum_{D\in\Pi_k}
J_{m,2k-m,D}(t),
\]

a convergent series of nonnegative terms. The case \(m=n=0\) equals one. Self-pairings within one chain and cross-pairings between the chains are both included in \(\Pi_k\); the second chain has its own root and does not continue the first chain.

### Derivation

The proof proceeds in this order.

1. **Fixed-order inputs.** Lemma L:joint-fixed-order (PROOF006) constructs each \(X_n\) and each individual two-chain diagram at arbitrary vertexwise widths, including unequal and empty chains. It uses the positive spatial-measure limit (PROOF005) and Lemma L:pairing-product-envelope (EXTERNAL_CANDIDATE_OWN215); it uses neither the present proposition nor any infinite solution series.

2. **Wick at positive widths.** At positive noise widths, Wick’s formula gives \(0\) at odd total order and the finite pairing sum at even total order. The Green-width limit is taken first.

3. **Product \(L^1\) convergence.** For fixed \(m,n\), joint \(L^2\) convergence of the two factors gives
\[
\|Y_mY_n-X_mX_n\|_1
\le \|Y_m-X_m\|_2\,\|Y_n\|_2
+\|X_m\|_2\,\|Y_n-X_n\|_2\to 0.
\]
A zero-order factor remains equal to one.

4. **Initial-chain identification.** For terminal variables in the first chain set
\[
s'_j=t-s_{m+1-j},\qquad y'_j=x-y_{m+1-j},\qquad 1\le j\le m,
\]
and the length-\(n\) analog on the second chain. Each transformed chain has initial root \((0,0)\). For example \(G(t-s_m,x-y_m)\mapsto G(s'_1,y'_1)\); differences change sign and are absorbed by evenness. The vertex involution
\[
\rho(j)=m+1-j,\ 1\le j\le m;\qquad
\rho(m+j)=m+n+1-j,\ 1\le j\le n,
\]
induces the pairing bijection \(D\mapsto\{\{\rho(a),\rho(b)\}:\{a,b\}\in D\}\). Passing through the finitely many diagram limits proves \(\mathbb E[X_mX_n]\) is exactly the sum of \(\eqref{E:mixed-diagram}\).

5. **Summability.** Lemmas L:crude-corrected (PROOF007) and L:vertex-crude (PROOF008) independently prove fixed-\(t\) norm summability of the \(X_n\). Proposition P:mild-construction (PROOF009) identifies the series as a Stratonovich mild solution. None of those proofs uses the present mixed identity, so there is no circularity.

6. **Full series.** \(U_N=\sum_{n=0}^N X_n\to u\) in \(L^2\), and
\[
|\mathbb E U_N^2-\mathbb E u^2|
\le \|U_N-u\|_2(\|U_N\|_2+\|u\|_2)\to 0.
\]
The finite expansions \(\mathbb E U_N^2\) increase since every mixed expectation is nonnegative. Their limit is the full double sum independent of enumeration; regrouping by total order gives \(\eqref{E:full-second}\).

**Convergence order.** The stated convergence is qualitative \(L^2\)/\(L^1\) at fixed \(t,x\); no rate in \(t\) is claimed. Summability is at each fixed \(t\).

**Consumed hypotheses.** H:homog; PROOF005, PROOF006, PROOF007, PROOF008, PROOF009, and EXTERNAL_CANDIDATE_OWN215.

**Unproved conditions.** The mixed identity inherits the status of PROOF006’s joint fixed-order construction, which in turn uses the reconstructed pairing envelope. The printed first-moment normalization conventions are not relied upon here.

## PROOF003

**Source record.** Same module; statement_LF `[514,523]`, proof_LF `[525,539]`; raw proof body SHA-256 `fc567c9cdd5ddc0f982cb936a6582ae2ebb5f5db16b62973ec35b2981d39b6f8`; full proof environment SHA-256 `3731d1b72e3c46a114c8f0780a0fb70cd808ac1a91b372df81b5eeecc054ea26`.

### Statement

For \(d=\alpha=1\) and \(\gamma=\delta_0\), put
\[
c_0=\frac1{(1-\alpha_0)(2-\alpha_0)(3-\alpha_0)}.
\]
Then
\[
\mathbb E X_1(t,x)^2=c_0\,t^{3-\alpha_0},\qquad
\mathbb E X_2(t,x)=\tfrac12 c_0\,t^{3-\alpha_0}.
\]
The total-order-two contribution to \(\eqref{E:full-second}\) is \(2c_0 t^{3-\alpha_0}\) (self-pairing \(X_1^2\), plus the two split terms \(2\mathbb E X_2\)).

### Derivation

Here \(G(s,y)=\frac12\mathbf1_{\{|y|<s\}}\), so
\[
\int_\R G(s,y)G(r,y)\,\mathrm dy=\frac{\min(s,r)}2.
\]

- **The (1,1) integral.** 
\[
\int_0^t\mathrm ds\int_0^s r(s-r)^{-\alpha_0}\mathrm dr
=\frac{t^{3-\alpha_0}}{(1-\alpha_0)(2-\alpha_0)(3-\alpha_0)}.
\]
Derivation: \(\int_0^s r(s-r)^{-\alpha_0}dr=s^{2-\alpha_0}B(2,1-\alpha_0)=s^{2-\alpha_0}/((1-\alpha_0)(2-\alpha_0))\), then \(\int_0^t s^{2-\alpha_0}ds=t^{3-\alpha_0}/(3-\alpha_0)\).

- **The (0,2) term.** The delta covariance forces the two spatial vertices equal. Writing \(0<r<s<t\) for the ordered time variables, the first Green factor \(G_r\) has spatial mass \(r\), while \(G_{s-r}(0)=1/2\). Its time integral is half the preceding display. The (2,0) term is identical.

The claim is an exact small-order computation on its precise ordered domain; no other fusion diagram is involved.

**Test of simplest cases.** For \(\alpha_0=0\), \(c_0=1/6\), giving \(\mathbb E X_1^2=t^3/6\), \(\mathbb E X_2=t^3/12\), and the total order-two coefficient \(t^3/3\), which is the static value recorded elsewhere in the source. All three factors \((1-\alpha_0),(2-\alpha_0),(3-\alpha_0)\) are positive for \(0<\alpha_0<1\), so \(c_0>0\) and finite.

**Consumed hypotheses.** \(d=\alpha=1\), \(\gamma=\delta_0\), \(0<\alpha_0<1\).

**Unproved conditions.** None beyond the explicit one-dimensional white specialization; the lemma is a calibration, not an asymptotic premise.

## PROOF004

**Source record.** Same module; statement_LF `[587,613]`, proof_LF `[615,675]`; raw proof body SHA-256 `54a170eba3afe5c50ec8095d92b1c7c89024b904e81cde882cd15bb5c86e24f8`; full proof environment SHA-256 `18d0d6f9fe61aa9ea5effd44c3b1c0e43ba483a2cc3181b25a633b29bc382917`.

### Statement (exact N1/N2 Laplace/spectral scalings and tails)

For the damped wave kernels, with \(\widehat G_s(\xi)=\sin(s|\xi|)/|\xi|\),

\[
\begin{aligned}
N_0(\theta)&=\int_0^\infty e^{-\theta s}G_s(\R^d)\,\mathrm ds,\\
N_1(\theta)&=\frac1{\Gamma_{\mathrm E}(\alpha_0)}
\int_0^\infty\lambda^{\alpha_0-1}\mathrm d\lambda
\int\frac{\mu(\mathrm d\xi)}{(\theta+\lambda)^2+|\xi|^2},\\
N_2(\theta)^2&=\int_0^\infty\int_0^\infty
e^{-\theta(s+t)}|s-t|^{-\alpha_0}
\int\widehat G_s(\xi)\overline{\widehat G_t(\xi)}\mu(\mathrm d\xi)
\,\mathrm ds\,\mathrm dt.
\end{aligned}
\]

Under H:homog each of these is finite for every \(\theta>0\), \(N_2(\theta)^2\ge0\), and

\[
N_0(\theta)=\theta^{-2},\qquad
N_1(\theta)=\theta^{\alpha+\alpha_0-2}N_1(1),\qquad
N_2(\theta)^2=\theta^{-\beta}N_2(1)^2,\qquad
\beta=4-\alpha-\alpha_0.
\]

With
\[
K_M(r)=\frac1{\Gamma_{\mathrm E}(\alpha_0)}\int_M^\infty
e^{-\lambda|r|}\lambda^{\alpha_0-1}\mathrm d\lambda
\]
and \(N_1^{(M)}(1),N_2^{(M)}(1)\) the corresponding tails,

\[
N_1^{(M)}(1)\to0,\qquad N_2^{(M)}(1)\to0\qquad(M\to\infty).
\]

Spatial Gaussian smoothing, Gaussian smoothing of the Green kernel, and restriction of a temporal Laplace domain do not increase these full or tail bounds.

### Derivation

1. **Spectral homogeneity.** Fourier uniqueness applied to \(\Gamma(cx)=c^{-\alpha}\Gamma(x)\) gives \(\mu(cA)=c^\alpha\mu(A)\). Radon finiteness, \(\alpha>0\), gives \(\mu(\{0\})=0\) and the ball law \(\mu(B_r)=r^\alpha V\), \(V=\mu(B_1)<\infty\).

2. **Resolvent finiteness.** For \(a>0\),
\[
\int\frac{\mu(\mathrm d\xi)}{a^2+|\xi|^2}
=\alpha V a^{\alpha-2}\int_0^\infty\frac{u^{\alpha-1}}{1+u^2}\mathrm du<\infty,
\]
finite because \(0<\alpha<2\). Substitution into \(N_1\) reduces finiteness to
\[
\int_0^\infty\lambda^{\alpha_0-1}(\theta+\lambda)^{\alpha-2}\mathrm d\lambda<\infty
\]
with conditions at zero and infinity \(\alpha_0>0\) and \(\alpha+\alpha_0<2\).

3. **\(N_2\) absolute integrability.** \(|\widehat G_s(\xi)|\le\min(s,|\xi|^{-1})\). On \(|\xi|\le1\),
\[
V\int_0^\infty\int_0^\infty e^{-\theta(s+t)}|s-t|^{-\alpha_0}st\,\mathrm ds\,\mathrm dt<\infty.
\]
On \(|\xi|>1\), \(\int_{|\xi|>1}|\xi|^{-2}\mu(\mathrm d\xi)=\alpha V/(2-\alpha)\) and the same time integral without \(st\) is finite by writing \(u=\min(s,t)\), \(v=|s-t|\) and using \(\alpha_0<1\). Non-negativity of the per-\(\xi\) time integral follows from the positive Laplace-mixture positive definiteness of \(e^{-\lambda|s-t|}\), hence \(N_2(\theta)^2\ge0\).

4. **Mass and scaling.** \(G_s(\R^d)=s\) gives \(N_0(\theta)=\theta^{-2}\). Substitutions \(N_1\): \(\lambda=\theta u\), \(\xi=\theta\eta\). \(N_2\): \(s=u/\theta\), \(t=v/\theta\), \(\xi=\theta\eta\) with \(\widehat G_{u/\theta}(\theta\eta)=\theta^{-1}\widehat G_u(\eta)\), which gives exactly \(\theta^{-\beta}\).

5. **Tails.** The first tail is the tail of the finite nonnegative \(N_1(1)\). For the second, \(0\le K_M(r)\le|r|^{-\alpha_0}\) and \(K_M(r)\to0\) for \(r\neq0\); the absolute majorant allows dominated convergence in \((s,t,\xi)\). The tail kernel is positive definite by the same Laplace-mixture argument.

6. **Smoothing/truncation monotonicity.** Gaussian multipliers lie in \([0,1]\); \(N_1\) integrand nonnegative; for \(N_2\) the per-\(\xi\) quadratic form is nonnegative so its multiplier can be dropped in an upper bound; Laplace-domain restriction decreases the first norm and its nonnegative covariance quadratic form.

**Endpoint restrictions.** \(0<\alpha_0<1\), \(0<\alpha<d\) or \(\alpha=d=1\), \(d\in\{1,2,3\}\), \(\alpha+\alpha_0<2\), and the Fourier uniqueness of the spectral scaling.

**Unproved conditions.** No additional premise beyond H:homog is required for this lemma. The positive-definiteness step uses the standard Laplace-mixture representation of \(e^{-\lambda|s-t|}\).

## PROOF005

**Source record.** Same module; statement_LF `[1176,1192]`, proof_LF `[1194,1336]`; raw proof body SHA-256 `d7820cfa105715b1b7fd5a3150d6fbb9b3297e6926f72d9a7edc66e3fbd6857c`; full proof environment SHA-256 `3f39b5960f9b336ee7048d55d518f65344eccbbe41bcb2d88dd1cf5db8ae7d37`.

### Statement (positive spatial Wick-measure limit and \(\alpha\)-homogeneity)

Under H:homog, for two ordered chains with \(m+n=2k\ge2\), pairing \(D\in\Pi_k\), gap vector \(\boldsymbol r\in(0,\infty)^{2k}\), positive spatial widths \(\boldsymbol\epsilon\), the finite measures

\[
\nu_{\boldsymbol\epsilon,D}=e^{-\sum_l r_l}
J_{\boldsymbol\epsilon,D}(\boldsymbol r)\,\mathrm d\boldsymbol r,\qquad
J_{\boldsymbol\epsilon,D}(\boldsymbol r)
=\int\prod_{l=1}^{2k}G_{r_l}(\mathrm dz_l)
\prod_{\{j,h\}\in D}\gamma_{\epsilon_j+\epsilon_h}(x_j-x_h)
\]

converge weakly, as all spatial widths tend to zero at arbitrary relative rates, to a finite measure \(\nu_D\). The locally finite measure \(\rho_D=e^{\sum_l r_l}\nu_D\) satisfies

\[
\rho_D(cA)=c^{(4-\alpha)k}\rho_D(A),\qquad c>0,
\]

and assigns zero mass to every face \(r_l=0\) and every face \(\ell_i=T>0\) (with \(\ell_i\) the sum of gaps in chain \(i\)). Consequently

\[
\int_{\ell_1<T_1,\ell_2<T_2}\varphi\,\mathrm d\rho_{\boldsymbol\epsilon,D}
\longrightarrow
\int_{\ell_1<T_1,\ell_2<T_2}\varphi\,\mathrm d\rho_D
\]

for bounded continuous \(\varphi\) and \(T_1,T_2>0\).

### Derivation

1. **Laplace transform.** Orient \(e=\{j,h\}\) as \(j<h\), and let \(\eta_l(\boldsymbol\xi)\) be the coefficient of \(z_l\) in \(\sum_e\xi_e\cdot(x_j-x_h)\). Then for \(\lambda_l\ge0\),

\[
L_{\boldsymbol\epsilon,D}(\boldsymbol\lambda)
=\int e^{-\sum_l\lambda_l r_l}\mathrm d\nu_{\boldsymbol\epsilon,D}
=\int\exp\!\Big\{-\frac12\sum_{e=\{j,h\}}(\epsilon_j+\epsilon_h)|\xi_e|^2\Big\}
\prod_{l=1}^{2k}\frac1{(1+\lambda_l)^2+|\eta_l(\boldsymbol\xi)|^2}
\prod_{e\in D}\mu(\mathrm d\xi_e).
\]

The integrand is nonnegative, so the transforms increase when any spatial width decreases (transform monotonicity, not pointwise monotonicity of covariances).

2. **Heat bound.** With \(V=\mu(B_1)\),

\[
0\le(p_t*\gamma_b)(x)\le A t^{-\alpha/2},\qquad
A=\alpha V\int_0^\infty u^{\alpha-1}e^{-u^2/2}\mathrm du<\infty.
\]

3. **Brownian occupation moments.** For a Brownian motion \(B\),

\[
S_b(T)=\int_0^T\int_0^T\gamma_b(B_s-B_t)\mathrm ds\,\mathrm dt,
\]

and for integer \(j\ge1\),

\[
\mathbb E_B S_b(T)^j
\le\frac{(2j)!\,[A\,\Gamma_{\mathrm E}(1-\alpha/2)]^j}
{\Gamma_{\mathrm E}((2-\alpha/2)j+1)}\,T^{(2-\alpha/2)j}.
\]

This is the ordered-variable elimination procedure: order the \(2j\) times, condition on all but the last remaining Brownian vertex, bound its pair factor by \(A\) times the last remaining gap to power \(-\alpha/2\), remove that vertex and partner, and observe that the remaining factors have again the Brownian marginal law at the remaining times. The \(j\) selected right endpoints are distinct, each selected gap dominates the original adjacent gap. On each ordered simplex the bound is \(A^j\) times a product of \(j\) distinct adjacent gaps to power \(-\alpha/2\); Dirichlet integration gives
\[
\Gamma_{\mathrm E}(1-\alpha/2)^j T^{(2-\alpha/2)j}/\Gamma_{\mathrm E}((2-\alpha/2)j+1),
\]
and there are \((2j)!\) orders.

4. **Uniform total-mass bound.** With \(\epsilon_*=\min_l\epsilon_l\), the positive transform \(L_{\boldsymbol\epsilon,D}(0)\) is bounded by the transform with all widths equal to \(\epsilon_*\). The wave-to-heat identity
\[
\int_0^\infty e^{-at}G_t(\mathrm dx)\mathrm dt
=\frac12\int_0^\infty e^{-a^2u/2}p_u(x)\mathrm du\,\mathrm dx
\]
(equal Fourier transforms \((a^2+|\xi|^2)^{-1}\)) writes the common-width transform as \(2^{-2k}\) times a two-Brownian-chain integral with gap weights \(e^{-\sum_l u_l/2}\) and covariance \(\gamma_{2\epsilon_*}\) on every pair. If \(\tau_i\) is the last Brownian time in chain \(i\), insert

\[
1=\frac14\int_{\tau_1}^\infty\int_{\tau_2}^\infty
e^{-((a-\tau_1)+(b-\tau_2))/2}\mathrm da\,\mathrm db.
\]

By positivity the ordered Brownian domains are extended to full cubes, and at fixed paths the time integrations factor into one occupation integral per pair. For independent paths,

\[
0\le A_{12}:=\int_0^a\int_0^b
\gamma_{2\epsilon_*}\bigl(B_1(s)-B_2(t)\bigr)\mathrm ds\,\mathrm dt
\le\sqrt{S^{(1)}_{2\epsilon_*}(a)\,S^{(2)}_{2\epsilon_*}(b)}.
\]

If the pairing has \(v_1,v_2\) self-pairs and \(w\) cross-pairs, \(v_1+v_2+w=k\), the occupation product is at most
\[
S_1^{v_1+w/2}S_2^{v_2+w/2}\le(1+S_1)^k(1+S_2)^k.
\]
The moment bound makes each expected factor bounded by a fixed finite \(M_k\) of nonnegative horizon powers, and independence gives

\[
\sup_{\boldsymbol\epsilon>0}L_{\boldsymbol\epsilon,D}(0)
\le2^{-2k-2}\Big(\int_0^\infty e^{-a/2}M_k(a)\mathrm da\Big)^2<\infty.
\]

5. **Weak limit.** Monotone convergence gives finite limits \(L_D(\boldsymbol\lambda)\) for all \(\boldsymbol\lambda\ge0\); the limiting integrand at zero is integrable, so continuity at zero follows by dominated convergence. Push to \([0,1]^{2k}\) via \(y_l=e^{-r_l}\). Uniformly bounded masses on the compact cube have weak cluster limits; the integer monomial moments are the prescribed \(L_D\) values, so polynomial density determines a unique cluster limit. For \(c>0\), \(\int\prod_l y_l^c\) is \(L_D(c,\dots,c)\); as \(c\downarrow0\) continuity at zero plus monotone convergence shows the cluster limit has no mass where any \(y_l=0\). Closed neighborhoods of these faces have limiting mass zero; the portmanteau inequality bounds the approximating tail masses, giving weak convergence on \([0,\infty)^{2k}\) and independence of the relative width rates.

6. **Face nullity and homogeneity.** Sending only \(\lambda_l\to\infty\) in the limiting positive integral gives zero, and this limit equals \(\nu_D\{r_l=0\}\), so coordinate-zero faces have zero mass. Scaling
\[
G_{cr}(c\,\mathrm dz)=c\,G_r(\mathrm dz),\qquad
\gamma_b(cx)=c^{-\alpha}\gamma_{b/c^2}(x)
\]
plus \(2k\) time Jacobians gives \(\rho_{\boldsymbol\epsilon,D}(cA)=c^{(4-\alpha)k}\rho_{\boldsymbol\epsilon/c^2,D}(A)\). Vague limits give the same homogeneity for \(\rho_D\). A compact part of the face \(\{\ell_i=T\}\) with positive mass would have disjoint dilates \(cA\), \(c\in[1,2]\), with a common positive lower mass bound inside one compact set, contradicting local finiteness; exhausting the face gives zero mass. The finite-horizon region is bounded with boundary contained in the horizon and coordinate-zero faces; weak convergence with a compact cutoff and the bounded continuous multiplier \(e^{\sum r_l}\varphi\) proves the asserted limit equality.

**Consumed hypotheses.** H:homog; standard Fourier/Laplace uniqueness and the wave-to-heat identity; independence of the auxiliary Brownian chains and horizons is part of the estimate, not the model.

**Unproved conditions.** The derivation establishes the measure limits but does not by itself identify them with random Wick diagrams; that identification is separate (PROOF006, and the source-convergence records). The Brownian last-vertex elimination is stated as a verification to be checked, not an assumed known theorem; all displayed formulas above are its actual derivation.

## PROOF006

**Source record.** Same module; statement_LF `[1338,1347]`, proof_LF `[1349,1432]`; raw proof body SHA-256 `ca55075ab99eaf6cb70cf0ed498e9401929b8be3d30e997d90d369bb02656423`; full proof environment SHA-256 `ead3ade5e8fb83e4228c078414cd0c90a95631cbcfab91dd920d8df4806c9561`.

### Statement

Under H:homog, every two-chain diagram with \(m+n=2k\ge2\) has a finite joint limit as all its positive vertexwise spatial and temporal widths tend to zero, at arbitrary relative rates. This includes unequal and empty chains. For every \(n\ge1,t>0,x\), \(Y_n^{\boldsymbol a}(t,x)\) has a unique joint \(L^2\) limit, denoted \(X_n(t,x)\); it is the multiple Stratonovich integral of \(g_n\). In dimension three the Green-width limit is removed before the noise-width limit.

### Derivation

1. **Spatial-first limit.** Use the gap variables and spatial measures of PROOF005. With \(s_j=s_j(\boldsymbol r)\), on \(\ell_1<T_1,\ell_2<T_2\),

\[
F_{\boldsymbol\epsilon,\boldsymbol\delta,D}
=\int\prod_{\{j,h\}\in D}
\gamma^0_{\delta_j\vee\delta_h}(s_j-s_h)\,\mathrm d\rho_{\boldsymbol\epsilon,D}.
\]

At a common temporal width \(\eta>0\) the multiplier is bounded and continuous, so the spatial limit exists at every \(T_1,T_2>0\) by PROOF005’s weak-limit equality.

2. **Temporal-cutoff removal.** \(F_{\boldsymbol\epsilon,0,D}\) (full factors \(|s_j-s_h|^{-\alpha_0}\)) is finite at positive spatial widths: covariances are bounded by their finite suprema, Green masses by horizon bounds, and the disjoint-pair time factors are integrable because \(\alpha_0<1\). A difference-of-products inequality bounds \(F_{\boldsymbol\epsilon,0,D}-F_{\boldsymbol\epsilon,\eta,D}\) by a sum of \(k\) nonnegative integrals, each with one marked time covariance \(K_{1/\eta}\) and the rest full.

3. **Marked edge envelope.** Apply EXTERNAL_CANDIDATE_OWN215 to \(e^{-s}G_s\). First smooth the Green kernel in \(d=3\) and cap the temporal Laplace domains. Each spatial edge has finite Gaussian-weighted spectral measure with nonnegative physical covariance; each temporal domain is a Laplace interval or restriction. The finite-horizon exponential loss is at most \(e^{T_1+T_2}\). PROOF004 bounds all unmarked norms independently of the smoothing parameters, and the marked edge appears once in the first-norm product or twice in the second-norm product in every admissible assignment. Therefore

\[
0\le F_{\boldsymbol\epsilon,0,D}-F_{\boldsymbol\epsilon,\eta,D}
\le C_{k,T_1,T_2}\Bigl(N_1^{(1/\eta)}(1)+N_2^{(1/\eta)}(1)^2\Bigr),
\]

uniformly in all spatial widths. Here the tail norms vanish by PROOF004; the convergence of the remainder is at the rate \(N_1^{(1/\eta)}(1)+N_2^{(1/\eta)}(1)^2\).

4. **Passages.** Let the upper temporal caps go to infinity by positivity, then remove Green smoothing at fixed spatial widths using bounded spatial covariance products, weak Green-measure convergence, and the same integrable time-cube majorant. The bound survives both passages and its right side tends to zero as \(\eta\downarrow0\).

5. **Joint limit.** The fixed-\(\eta\) spatial limit \(b_D(\eta)\) is increasing as \(\eta\) decreases and is Cauchy, with finite limit \(b_D\). If every \(\delta_j<\eta\), positivity gives
\[
F_{\boldsymbol\epsilon,\eta,D}\le F_{\boldsymbol\epsilon,\boldsymbol\delta,D}\le F_{\boldsymbol\epsilon,0,D}.
\]
Fixing \(\eta\), passing to the spatial limit in the lower term, using the uniform remainder, and letting \(\eta\downarrow0\) gives the joint limit \(b_D\) with arbitrary spatial/temporal rates. Empty chains contribute no horizon variables and are covered.

6. **\(L^2\) fixed-order limit.** At positive widths, Wick’s formula expresses the mixed second moments of two copies of \(Y_n\) as the finite diagram sum after reversing both terminal chains at horizon \(t\); evenness absorbs sign changes. Every mixed moment, including diagonals, tends to the same finite \(Q_n=\sum_{D\in\Pi_n}b_D\). Hence

\[
\|Y_n^{\boldsymbol a}-Y_n^{\boldsymbol b}\|_2^2
\longrightarrow Q_n+Q_n-2Q_n=0,
\]

so completeness of \(L^2\) gives a unique limit independent of all width ratios. Restriction to common noise widths gives the multiple Stratonovich definition of \(g_n\).

**Convergence order.** The temporal remainder is \(o(1)\) in \(\eta\) uniformly in spatial widths, driven by the vanishing tail norms \(N_1^{(1/\eta)}(1)+N_2^{(1/\eta)}(1)^2\); the final width limit is a qualitative \(L^2\) limit.

**Consumed hypotheses.** H:homog; PROOF004, PROOF005, EXTERNAL_CANDIDATE_OWN215; the source’s Wick/regularization conventions.

**Unproved conditions.** The marked-edge envelope is exactly the reconstructed per-family pairing bound; the uniformity of the marked-edge factor across admissible partitions (as argued in the ledger F103) is needed and is not an unconditional published theorem. The identification with the source’s Definition 2.2 convention additionally requires the source’s regularization scheme.

## PROOF007

**Source record.** Same module; statement_LF `[1442,1450]`, proof_LF `[1452,1504]`; raw proof body SHA-256 `2b3db904292c37eb43d3927695340068ef32329abfde0dcf72900d3bb57e86da`; full proof environment SHA-256 `d165dd24f5dc3328cb205ba8af86e121c1c7d754f7d7417666ba876307e305a5`.

### Statement (corrected crude estimate)

Under H:homog, there are \(C<\infty,\theta_0>0\) such that for \(n\ge1,t>0\),

\[
\mathbb E X_n(t,x)^2\le e^{2\theta_0t}\,\frac{C^n t^{2n}}{n!},
\qquad
\mathbb E u^2(t,x)\le 2e^{2\theta_0t+2Ct^2}.
\]

### Derivation

1. **Telescoping weights.** On the two finite chains the product of exponential weights telescopes to \(e^{-\theta(s_n+s_{2n})}\ge e^{-2\theta t}\). Extend the nonnegative integral to the two infinite time simplices and apply EXTERNAL_CANDIDATE_OWN215.

2. **Admissible product degrees.** For every admissible product, with \(q_i=\#Q_i\),

\[
q_0=q_1,\qquad q_0+\frac{q_2}{2}=n.
\]

With \(\theta\ge\theta_0\) and the damped-norm bounds
\[
N_0(\theta)=\theta^{-2},\qquad N_1(\theta)\le C_0,\qquad N_2(\theta)\le C_0\theta^{-1},
\]
each pairing is bounded by \(e^{2\theta t}C^n\theta^{-2n}\). Summing the \(P_n=(2n)!/(2^n n!)\) pairings,

\[
\mathbb E X_n(t,x)^2\le P_n e^{2\theta t}C^n\theta^{-2n},\qquad \theta\ge\theta_0.
\]

3. **Finite-spectral-measure regularization.** The smoothing leaves the zero norm unchanged and the \(N_1,N_2\) bounds are controlled by PROOF004’s multiplier bounds, uniform in regularization. In \(d=3\), use \(G_\eta=p_\eta*G\) first; its Fourier multiplier is \(\le1\) and its mass equals the Green mass, so the bounds are uniform in \(\eta\). For fixed \((\epsilon,\delta)\), first take \(\eta\downarrow0\), then \((\epsilon,\delta)\to0\) using PROOF006; squared moments converge, so the uniform inequality survives each limit.

4. **Choose \(\theta\).** Take \(\theta=\theta_0+n/t\). Since \((2n)!\le(2n)^{2n}\),
\[
P_n n^{-2n}\le \frac{2^n}{n!}.
\]
Absorbing \(2^n e^{2n}\) into \(C^n\) gives the first bound. The square roots are summable for each \(t\) by the ratio test, so the norm series converges independently of Proposition P:mixed.

5. **Full moment.** By Minkowski and Cauchy–Schwarz,

\[
\|u(t,x)\|_2\le e^{\theta_0t}\sum_{n\ge0}\frac{(\sqrt C\,t)^n}{\sqrt{n!}},
\]
and
\[
\Bigl(\sum_{n\ge0}\frac{z^n}{\sqrt{n!}}\Bigr)^2
\le\Bigl(\sum_{n\ge0}2^{-n}\Bigr)
\Bigl(\sum_{n\ge0}\frac{(2z^2)^n}{n!}\Bigr)
=2e^{2z^2}.
\]
This gives \(\mathbb E u^2\le 2e^{2\theta_0t+2Ct^2}\).

**Convergence order.** The order-\(n\) bound has denominator \(n!\); the series is summable at fixed \(t\) by the ratio test. No uniformity in \(t\) beyond the stated exponential form is claimed.

**Consumed hypotheses.** H:homog; PROOF004, PROOF006, EXTERNAL_CANDIDATE_OWN215; the smoothed-spectral-measure finiteness using (1.5).

**Unproved conditions.** The inequality transfer through regularization limits uses fixed-order \(L^2\) convergence (PROOF006); the actual bound is conditional on the reconstructed envelope.

## PROOF008

**Source record.** Same module; statement_LF `[1508,1520]`, proof_LF `[1522,1581]`; raw proof body SHA-256 `13e01462f76698eaebad7e5f564b92638fb05fb80a6d2b910c48fb5c22980549`; full proof environment SHA-256 `4fe5c21adb5ca85c7ce547e65ccd25153359c5e22257194bff595f7545ea0280`.

### Statement (uniform vertexwise regularization bound)

Under H:homog there are \(C<\infty,\theta_0>0\) such that, for all positive vertexwise widths and \(n\ge1\),

\[
\|Y_n^{\boldsymbol a}(t,x)\|_2\le q_n(t),\qquad
q_n(t):=e^{\theta_0t}\frac{C^{n/2}t^n}{\sqrt{n!}}.
\]

The same bound holds for \(X_n(t,x)\), with \(q_0(t)=e^{\theta_0t}\ge1\). For each \(T<\infty\),

\[
\sum_{n\ge0}\sqrt{n+1}\,q_n(T)<\infty.
\]

### Derivation

1. **Vertexwise Wick square.** Wick’s formula (2.19) with the joint covariance (2.11) gives

\[
\|Y_n^{\boldsymbol a}(t,x)\|_2^2
=\sum_{D\in\Pi_n}J^{\boldsymbol a,\boldsymbol a}_{n,n,D},
\]

where the edge covariances are
\[
\gamma^0_{\delta_j\vee\delta_l}(s_j-s_l)
\,\gamma_{\epsilon_j+\epsilon_l}(y_j-y_l).
\]
Reversing terminal chains via \(s'_j=t-s_{n+1-j}\), \(y'_j=x-y_{n+1-j}\) only permutes vertex widths and flips differences, which evenness absorbs.

2. **Edge hypotheses.** For each pairing apply EXTERNAL_CANDIDATE_OWN215 to \(e^{-\theta r}G_r\) (with Green smoothing first in \(d=3\)). Each edge may carry its own finite spectral measure and temporal truncation:

\[
e^{-(\epsilon_j+\epsilon_l)|\xi|^2/2}\mu(\mathrm d\xi),
\qquad
[0,(\delta_j\vee\delta_l)^{-1}],
\]

both finite by (1.5). All edge norms obey the crude norm bounds uniformly in widths.

3. **Unmarked-norm independence.** For the first norm the Laplace–Fourier transform is positive and smoothing/truncation decrease the nonnegative spectral integral. For the second norm, enlarge the temporal covariance to \(|s-r|^{-\alpha_0}\), use the spectral expression of the squared absolute transform, and remove the spatial Gaussian multiplier to get an upper bound; Green smoothing has multiplier \(\le1\) and unchanged mass. These are applications of PROOF004, not an imported large-parameter formula.

4. **Degree accounting.** \(\#Q_0=\#Q_1\) and \(\#Q_0+\#Q_2/2=n\) give

\[
\|Y_n^{\boldsymbol a}(t,x)\|_2^2
\le P_n\,e^{2\theta t}C_1^{\,n}\theta^{-2n},\qquad\theta\ge\theta_0,
\]
with \(C_1=D^2\), \(D=\max\{1,2C_0\}\).

5. **Limits and ratio test.** Green width \(\to0\) at fixed positive noise widths, then \(\theta=\theta_0+n/t\). With \(P_n n^{-2n}\le2^n/n!\),

\[
\|Y_n^{\boldsymbol a}(t,x)\|_2\le e^{\theta_0t}\frac{C^{n/2}t^n}{\sqrt{n!}}.
\]

The same bound passes to \(X_n\) through PROOF006. Finally

\[
\frac{\sqrt{n+2}\,q_{n+1}(T)}
{\sqrt{n+1}\,q_n(T)}
=\sqrt C\,T\,\frac{\sqrt{n+2}}{n+1}\longrightarrow0,
\]

so \(\sum_n\sqrt{n+1}\,q_n(T)<\infty\).

**Consumed hypotheses.** H:homog; PROOF004, PROOF006, EXTERNAL_CANDIDATE_OWN215; the joint covariance law (2.11).

**Unproved conditions.** The rate is conditional on the per-family pairing envelope; the vertexwise-width uniformity is the whole point of the lemma and is derived, not assumed.

## PROOF009

**Source record.** Same module; statement_LF `[1583,1598]`, proof_LF `[1604,1751]`; raw proof body SHA-256 `64049ea1f0cc33d8a5fffce8250b2bf1b3c2d6ec81782f881774670454b96b32`; full proof environment SHA-256 `d56d08b5811d0d9a16154ac939cafe754d68c5be89806a74048935196c084025`.

### Statement (mild construction from the fixed-order limits)

Under H:homog, \(u(t,x)=\sum_{n\ge0}X_n(t,x)\) is a mild solution in Definition 2.1 / (2.12). For each \(t>0,x\in\R^d\),

\[
\lim_{\epsilon,\delta\downarrow0}
\int_0^t\int_{\R^d}G(t-s,x-\mathrm dy)
u(s,y)\,W_{\epsilon,\delta}(s,y)\,\mathrm ds
=u(t,x)-1\quad\text{in }L^2(\Omega).
\]

The limit allows arbitrary relative widths; in \(d=3\) the Green-width limit precedes the noise-width limit. No uniqueness assertion is made.

### Derivation

1. **Degree-closed Gaussian polynomial spaces.** Let \(\mathscr P_{\le n}\) be the closed Gaussian polynomial space of total degree \(\le n\) generated by all coupled source fields. Fixed-width terminal integrals belong to it; their \(L^2\) limits \(X_n\) do too.

2. **Occupied multiplication bound.** For centered linear Gaussian \(H\) and \(F\in\mathscr P_{\le n}\),

\[
\|HF\|_2\le2\sqrt{n+1}\,\|H\|_2\|F\|_2.
\]
Proof: scale \(H/\|H\|_2\) as the first coordinate of an orthonormal Gaussian basis; on normalized Hermite polynomials the creation and annihilation operators have norms \(\le\sqrt{n+1}\) and \(\le\sqrt n\) on degrees \(\le n\), since the squared coefficient weights are \(a_1+1\le n+1\) and \(a_1\le n\). This also proves closedness of multiplication and allows \(F\) to depend on \(H\).

3. **Measurability and spatial continuity.** PROOF008 gives absolute \(L^2\) convergence of the series locally uniformly in time. At positive widths rescale to unit-time domains; bounded Gaussian moments and finite Green masses give Bochner domination, hence joint measurability. Countable-width limits give this for \(X_n\) and the series. Positive-width terminal terms are \(L^2\)-continuous in space; joint spatial stationarity gives

\[
\|Y_n^{\boldsymbol b}(s,y)-X_n(s,y)\|_2
=\|Y_n^{\boldsymbol b}(s,0)-X_n(s,0)\|_2
\]

uniformly in \(y\) for fixed \(s\), so \(X_n(s,\cdot)\) and \(u(s,\cdot)\) have continuous \(L^2\) representatives.

4. **Fixed external width.** Fix \(a=(\epsilon,\delta)>0\), \(W_a=W_{\epsilon,\delta}\), variance \(V_a=\gamma^0_\delta(0)\gamma_{2\epsilon}(0)<\infty\). For \(n\ge1\) the Bochner integral

\[
I_{n,a}(t,x)=\int_0^t\int_{\R^d}G(t-s,x-\mathrm dy)
W_a(s,y)\,X_{n-1}(s,y)\,\mathrm ds
\]

exists because

\[
\|W_a(s,y)X_{n-1}(s,y)\|_2
\le2\sqrt n\sqrt{V_a}\,q_{n-1}(T),\qquad 0\le s\le T,
\]

and the Green mass is \(t-s\). At fixed \(a\), multiplication by \(W_a\) preserves \(L^2\) convergence, so

\[
I_{n,a}(t,x)=\lim_{\boldsymbol b\downarrow0}Y_n^{(\boldsymbol b,a)}(t,x)
\quad\text{in }L^2,
\]

and \(\sup_a\|I_{n,a}\|_2\le q_n(t)\).

5. **Dimension three Green limit at fixed external widths.** The product \(W_a(s,y)X_{n-1}(s,y)\) is \(L^2\)-continuous in \(y\). Convolution with \(p_\eta*G_{t-s}\) converges in \(L^2\) to \(G_{t-s}\) through finite partitions of unity, scalar weak Green convergence, and tightness; the mass \(t-s\) and the uniform bound permit dominated time integration. This is Green-first, and the inner noise limit is not interchanged with the Green limit.

6. **External width limit.** For fixed \(n\), joint fixed-order convergence (PROOF006) gives
\[
\lim_{a\downarrow0}I_{n,a}(t,x)=X_n(t,x)\quad\text{in }L^2,
\]
with arbitrary relative rates, without assuming a separate partial-limit theorem.

7. **Full product.** At fixed \(a\),

\[
\sum_{n\ge1}\|W_a(s,y)X_{n-1}(s,y)\|_2
\le2\sqrt{V_a}\sum_{n\ge1}\sqrt n\,q_{n-1}(T)<\infty.
\]

Multiplication is closed, so partial sums of \(u\) and their products converge and the product is \(W_a u\). Dominated Green integration gives

\[
I_a(t,x):=\int_0^t\int_{\R^d}G(t-s,x-\mathrm dy)
W_a(s,y)\,u(s,y)\,\mathrm ds
=\sum_{n\ge1}I_{n,a}(t,x)
\]

in \(L^2\).

8. **Final comparison.** For every \(N\),

\[
\|I_a(t,x)-(u(t,x)-1)\|_2
\le\sum_{n=1}^N\|I_{n,a}(t,x)-X_n(t,x)\|_2
+2\sum_{n>N}q_n(t).
\]

First \(a\downarrow0\) using the external-width limit, then \(N\to\infty\) using PROOF008’s summability. This proves the mild equation in the stated definition.

**Convergence order.** The two-side estimate has head term \(\sum_{n\le N}\|I_{n,a}-X_n\|_2\to0\) with \(a\), and tail \(2\sum_{n>N}q_n(t)\to0\) with \(N\) at geometric rate from PROOF008.

**Consumed hypotheses.** H:homog; PROOF006, PROOF008; the coupled Gaussian polynomial spaces over all source fields; pointfield regularity for fixed cutoffs.

**Unproved conditions.** The proof constructs the onefold Stratonovich mild identity for the product \(u\,W_{\epsilon,\delta}\) on the fixed \(W+J\) extension; it does not claim W-only measurability of the cutoff fields or uniqueness. The closedness of multiplication and the Bochner/Green limits are used, not imported operator theorems.

## PROOF010

**Source record.** Same module; statement_LF `[1761,1782]`, proof_LF `[1784,1836]`; raw proof body SHA-256 `c0b13b1e2d2cd27e3a5ab3d784d605a9fbc1e4cb50658dbffc097d283e4960ea`; full proof environment SHA-256 `91882e66cb71a47440d13cf3ba1bbe3a65a43ba124b3961c01ba3ea8735b6776`.

### Statement (uniform homogeneous pairing estimate and majorant growth)

Under H:homog there is \(K>0\) such that

\[
\mathbb E[X_m(t,x)X_n(t,x)]
\le P_k\,K^k\,e^{2\theta t}\,\theta^{-\beta k},
\qquad m+n=2k\ge2,\ \theta>0,
\]
with \(P_k=\#\Pi_k=(2k)!/(2^k k!)\) and \(\beta=4-\alpha-\alpha_0\).

Define the numerical majorant

\[
B_K(t)=1+\sum_{k\ge1}(2k+1)P_k K^k
\inf_{\theta>0}\{e^{2\theta t}\theta^{-\beta k}\}.
\]

Then \(\mathbb E u^2(t,x)\le B_K(t)\) and, for some \(c,C>0\) and all large \(t\),

\[
c\,t^\rho\le\log B_K(t)\le C\,t^\rho,\qquad
\rho=\frac{\beta}{\beta-1}
=\frac{4-\alpha-\alpha_0}{3-\alpha-\alpha_0}>\kappa.
\]

The lower bound concerns only the numerical majorant \(B_K\), not the second moment.

### Derivation

1. **Homogeneous norm scaling.** The wave kernel scales \(G(cs,c\,\mathrm dy)=c\,G(s,\mathrm dy)\) and the covariance has degree \(-\alpha\). Changing all variables by \(\theta^{-1}\) gives

\[
N_0(\theta)=\theta^{-2},\quad
N_1(\theta)=N_1(1)\,\theta^{\alpha+\alpha_0-2},\quad
N_2(\theta)^2=N_2(1)^2\,\theta^{-\beta},
\]
directly from PROOF004. Both products \(2N_0N_1\) and \(N_2^2\) have degree \(-\beta\).

2. **Common constant.** Choose \(K\ge\max\{2N_1(1),N_2(1)^2\}\). For every admissible product, \(q_0+q_2/2=k\), so its degree is \(-\beta k\) and its constant is at most \(K^k\). The finite horizons contribute at most \(e^{2\theta t}\). Regularized moments obey the same uniform bounds via PROOF004 multiplier removals, the Green limit in \(d=3\), and PROOF006’s joint fixed-order limit. Proposition P:mixed then gives the majorant.

3. **Infimum.** The infimum in \(B_K\) is attained at \(\theta=\beta k/(2t)\) with value
\[
e^{\beta k}\Bigl(\frac{2t}{\beta k}\Bigr)^{\beta k}.
\]

4. **Factorial envelope.** Put \(q=\beta-1>1\). Using
\[
k!\le P_k\le2^k k!,\qquad(k/e)^k\le k!\le k^k,\qquad 2k+1\le3^k,
\]
there are positive \(a,b\) depending only on \(K,\beta\) with

\[
\sum_{k\ge0}\frac{(a t^\beta)^k}{(k!)^q}
\le B_K(t)\le
\sum_{k\ge0}\frac{(b t^\beta)^k}{(k!)^q}.
\]

Indeed the extra factorial factor \(k!^\beta/k^{\beta k}\) lies between \(e^{-\beta k}\) and \(1\). The right side is at most
\[
\Bigl(\sum_{k\ge0}z^{k/q}/k!\Bigr)^q=e^{qz^{1/q}}
\]
by the elementary \(\ell^q\)-versus-\(\ell^1\) inequality. For the lower bound choose \(k=\lfloor z^{1/q}/2\rfloor\) and use \(k!\le k^k\), giving a single summand at least \(2^{qk}\). These estimates give the two-sided growth at \(\rho=\beta/(\beta-1)\). Since \(\beta-1=3-\alpha-\alpha_0<3-\alpha\), \(\rho>\kappa\).

**Consumed hypotheses.** H:homog; PROOF002, PROOF004, PROOF006, EXTERNAL_CANDIDATE_OWN215.

**Unproved conditions.** The displayed majorant has exponent \(\rho>\kappa\), so it cannot by itself settle the target upper scale; this is explicitly stated in the source. Its validity is conditional on the reconstructed pairing envelope. The lower bound is a statement about \(B_K\), not about \(\mathbb E u^2\).

## PROOF214

**Source record.** Same module; statement_LF `[709,720]`, proof_LF `[722,803]`; raw proof body SHA-256 `8a187e589582d0c618d281bc1a3ce974a4d0a715a0e2a750692288d465dc2434`; full proof environment SHA-256 `b1f5e1d722d3f12173a93295ec7284fa714143e53125068ea0d2992cf069a3c6`.

### Statement (translated covariance Cauchy–Schwarz, coefficient one)

Fix \(d\in\{1,2,3\}\), a finite positive Borel measure \(\mu\) on \(\R^d\) with \(\gamma(z)=\int e^{i\xi\cdot z}\mu(\mathrm d\xi)\) real and nonnegative for every \(z\), and a positive Borel measure \(\nu\) on \((0,\infty)\) with \(\nu((0,L])<\infty\) for every \(L>0\). Put

\[
\kappa_L(t)=\int_{(0,L]}e^{-\lambda|t|}\nu(\mathrm d\lambda),\qquad
C_L((t,x),(s,y))=\kappa_L(t-s)\gamma(x-y),
\]

and for complex \(L^1\) functions \(f,h\),

\[
Q_L(f,h)=\int_{\R^2}\int_{\R^{2d}}
f(t,x)\overline{h(s,y)}\,\kappa_L(t-s)\gamma(x-y)
\,\mathrm dx\,\mathrm dy\,\mathrm dt\,\mathrm ds.
\]

For nonnegative \(G_i\) let \(G_i^0\) be the zero extension to nonpositive times, \(N_0(G)=\int_0^\infty\int G\), \(N_C(G)^2=Q(G^0,G^0)\), and \(T_{A,a}f(t,x)=f(t-A,x-a)\). Then for arbitrary origins \((A,a),(B,b)\),

\[
0\le Q\bigl(T_{A,a}G_1^0,T_{B,b}G_2^0\bigr)\le N_C(G_1)N_C(G_2),
\]

and \(Q(T_{A,a}G_i^0,T_{A,a}G_i^0)=N_C(G_i)^2\). The coefficient one is independent of the origins, dimension, cap, and covariance masses; zero norms and zero measures are included.

### Derivation

1. **Feature space.** For \(\lambda>0\),

\[
h_\lambda(t,r)=\sqrt{2\lambda}\,e^{-\lambda(t-r)}\mathbf1_{\{r\le t\}},
\]
with
\[
\int_\R h_\lambda(t,r)h_\lambda(s,r)\,\mathrm dr
=e^{-\lambda|t-s|},\qquad\int_\R h_\lambda(t,r)^2\mathrm dr=1.
\]

On \(\mathcal H_L=L^2\bigl((0,L]\times\R^d\times\R,\nu(\mathrm d\lambda)\mu(\mathrm d\xi)\mathrm dr\bigr)\), set \(\Phi_L(t,x)(\lambda,\xi,r)=h_\lambda(t,r)e^{i\xi\cdot x}\). Then

\[
\|\Phi_L(t,x)\|^2=m_L=\nu((0,L])\mu(\R^d),
\qquad
\langle\Phi_L(t,x),\Phi_L(s,y)\rangle=C_L((t,x),(s,y)).
\]

2. **Bochner identity.** The map \((t,x)\mapsto\Phi_L(t,x)\) is norm-continuous, strongly measurable with separable range, and bounded. For \(f\in L^1\), \(F_L(f)=\int f(t,x)\Phi_L(t,x)\,\mathrm dt\,\mathrm dx\) exists as a Bochner integral and

\[
Q_L(f,h)=\langle F_L(f),F_L(h)\rangle
\]

by Bochner Fubini, justified by \(m_L\|f\|_1\|h\|_1\). Therefore

\[
|Q_L(f,h)|\le Q_L(f,f)^{1/2}Q_L(h,h)^{1/2}.
\]

This uses the original stationary covariance \(C_L\), not positivity of an independently shifted cross kernel; no new Gaussian field is introduced.

3. **Common-translation invariance.** Changing both variables by the same translation gives
\[
Q_L(T_{A,a}f,T_{A,a}h)=Q_L(f,h)
\]
by Lebesgue translation invariance on the full time line. Cauchy–Schwarz applied to the two distinct translates, together with the self-pairing identity, proves the capped form with coefficient one, keeping the predecessor offsets \(A-B\) in the time argument.

4. **Passage to unbounded nonnegative kernels.** Set

\[
G_{i,M}(t,x)=\min(G_i(t,x),M)\mathbf1_{\{0<t\le M,\ |x|\le M\}}.
\]
These increase to \(G_i\). Since \(C_L\ge0\), monotone convergence passes the capped inequality and common-translation identity from \(G_{i,M}\) to \(G_i\). Equivalently, the finite-cap passage follows from \(L^1\) convergence and the absolute bound.

5. **Cap removal.** Positivity of \(\nu\) and nonnegativity of \(\gamma\) give
\[
Q_L(G_i^0,G_i^0)\uparrow N_C(G_i)^2,\qquad
Q_L(T_{A,a}G_1^0,T_{B,b}G_2^0)\uparrow Q(T_{A,a}G_1^0,T_{B,b}G_2^0).
\]
The finite self-norms bound the limit. No division by a norm occurs, so zero norms cause no exception. No spatial Gaussian mollifier is removed in this argument.

**Consumed hypotheses.** \(\mu\) finite with nonnegative real \(\gamma\); \(\nu\) finite on caps; \(G_i\) nonnegative Borel with \(N_0,N_C<\infty\). The source’s Case-2 application uses the predecessor offsets retained explicitly.

**Unproved conditions.** None specific to the lemma; it is the exact coefficient-one bridge used in the envelope proof’s Case 2, replacing the source’s offset-free equality, which is not an identity for \(A\neq B\).

## EXTERNAL_CANDIDATE_OWN215

**Source record.** Same module; statement_LF `[1005,1017]`, proof_LF `[1019,1135]`; raw proof body SHA-256 `94df56ba684fc7c8d7ffff64eac7ad085d0a583ada35d2b0fb2fad65547c64c4`; full proof environment SHA-256 `8d8a29d05d05e032e461bbf93ce2407403c71cc04c19cd8a97dd4f7c966c2ad7`.

### Statement (finite pairing product envelope)

Fix \(d\ge1\), \(0<a<1\), and a matching \(D\) on \(2n\) labels. For each edge \(e\in D\), \(\mu_e\) is finite positive with \(\gamma_e(x)=\int e^{i\xi\cdot x}\mu_e(\mathrm d\xi)\ge0\). For measurable \(A_e\subset(0,\infty)\),

\[
\nu_e(\mathrm d\lambda)=\Gamma_{\mathrm E}(a)^{-1}\mathbf1_{A_e}(\lambda)\lambda^{a-1}\mathrm d\lambda,
\qquad
\kappa_e(t)=\int e^{-\lambda|t|}\nu_e(\mathrm d\lambda).
\]

For nonnegative \(G\in L^1((0,\infty)\times\R^d)\),

\[
\begin{aligned}
N_0(G)&=\int G(t,x)\mathrm dt\mathrm dx,\\
N_{1,e}(G)&=\int\Bigl|\int e^{-\lambda t+i\xi\cdot x}G(t,x)\mathrm dt\mathrm dx\Bigr|
\nu_e(\mathrm d\lambda)\mu_e(\mathrm d\xi),\\
N_{2,e}(G)^2&=\int G(s,x)G(t,y)\kappa_e(s-t)\gamma_e(x-y)
\mathrm ds\mathrm dx\mathrm dt\mathrm dy.
\end{aligned}
\]

For the two ordered chains \(I_1=\{1,\dots,n_1\}\), \(I_2=\{n_1+1,\dots,2n\}\), \(n_1+n_2=2n\), with separate roots \((0,0)\) at the first vertex of each chain,

\[
I_D(\boldsymbol G)=\int
\prod_{\rho=1}^2\prod_{l\in I_\rho}G_l(s_l-s_{p(l)},x_l-x_{p(l)})
\prod_{e=\{j,k\}\in D}\kappa_e(s_j-s_k)\gamma_e(x_j-x_k)
\mathrm d\boldsymbol s\,\mathrm d\boldsymbol x.
\]

Call \((Q,\iota)\) admissible if \(Q_0,Q_1,Q_2\) partition the kernel labels, \(|Q_0|=|Q_1|\), and \(\iota:Q_1\cup Q_2\to D\) uses each edge once on \(Q_1\) or twice on \(Q_2\), never both; no incidence requirement between \(l\) and \(\iota(l)\). Then

\[
I_D(\boldsymbol G)\le\max_{(Q,\iota)\in\mathcal A_D}\mathcal P_{Q,\iota}(\boldsymbol G),
\]

with

\[
\mathcal P_{Q,\iota}(\boldsymbol G)=
\prod_{l\in Q_0}N_0(G_l)
\prod_{l\in Q_1}2N_{1,\iota(l)}(G_l)
\prod_{l\in Q_2}N_{2,\iota(l)}(G_l).
\]

A maximizing assignment may depend on the kernels and edge data; no single assignment valid for all kernel families is asserted. For \(n=0\) both sides are one; zero kernels, measures, and norms are allowed.

### Derivation (original complete generic induction as rewritten in the source)

1. **Finite caps.** Cap every temporal domain at \(L<\infty\); its measure is finite since \(a>0\). The stationary covariance pairing of PROOF214 has norm \(N_{2,e}\), and its feature \(h_\lambda(t,r)e^{i\xi\cdot x}\) works in any finite dimension, so the coefficient-one Cauchy–Schwarz and translation invariance apply at the cap. All Fourier and Bochner interchanges at the cap are justified by the finite covariance masses times the relevant \(L^1\) masses.

2. **Convolution estimates.** For one-sided spacetime convolution \(F=G*H\),

\[
\begin{aligned}
N_0(F)&=N_0(G)N_0(H),\\
N_{1,e}(F)&\le N_0(G)N_{1,e}(H),\\
N_{2,e}(F)&\le N_0(G)N_{2,e}(H),
\end{aligned}
\]

where for the first-norm estimate \(|\mathcal L G(\lambda,\xi)|\le N_0(G)\) for \(\lambda\ge0\), and for the second one zero-extends \(H\), represents \(F\) as a Bochner integral of translates of \(H\) against \(G\), and applies Minkowski. Thus every fused kernel satisfies all remaining edge hypotheses; no division by a norm occurs.

3. **Base cases.** \(n=0\): empty product/partition \(1\). \(n=1\): two vertices on one chain give at most \(N_0(G_{\rm first})N_{1,e}(G_{\rm last})\); one vertex on each chain gives at most two second norms by covariance Cauchy–Schwarz. Both nonempty-chain orientations are checked.

4. **Regional half-bound.** For an endpoint \(v\) with predecessor \(p\) and partner \(a\) satisfying \(s_a\le s_p\) on a region whose indicator is independent of \((s_v,x_v)\), put \(e_0=\{a,v\}\). Since \(\kappa_{e_0}\) is decreasing on positive arguments,

\[
\kappa_{e_0}(s_v-s_a)\le\kappa_{e_0}(s_v-s_p).
\]

Integrating the endpoint and taking the modulus of its spatial Fourier phase gives

\[
\int|\mathcal L G_v(\lambda,\xi)|\nu_{e_0}(\mathrm d\lambda)\mu_{e_0}(\mathrm d\xi)
=N_{1,e_0}(G_v).
\]

Drop the region indicator by positivity. Remove \(v\) and \(e_0\). If the partner \(a\) is terminal, integrate \(N_0(G_a)\) and apply induction. If not, integrate the successive pair \(G_a*G_b\) at \(b\), with \(b\) the successor of \(a\) on its own chain.

5. **All three fusion slots with the retained factor two.** Let \(F=G_a*G_b\), and apply the full \(n-1\) induction to the reduced diagram, marking the slot \(i=0,1,2\) occupied by \(F\). With \(R_0,R_1,R_2\) the remaining slots and \(B_{\rm rest}\) their product retaining every first-slot factor two, the new slots and the resulting half-products are exactly:

- \(i=0\): \(Q_0=R_0\cup\{a,b\}\), \(Q_1=R_1\cup\{v\}\), \(Q_2=R_2\). Mass multiplicativity gives one half of the new product.
- \(i=1\): \(Q_0=R_0\cup\{a\}\), \(Q_1=R_1\cup\{b,v\}\), \(Q_2=R_2\). If \(e_1\) is the inherited edge, the actual term and its bound are
\[
N_{1,e_0}(G_v)\,[2N_{1,e_1}(F)]B_{\rm rest}
\le\tfrac12N_0(G_a)\,[2N_{1,e_1}(G_b)]\,[2N_{1,e_0}(G_v)]B_{\rm rest}.
\]
The inherited edge stays first exactly once; \(e_0\) is first exactly once; no incidence condition is needed. This retained-first-slot-\(2\) estimate is the item identified in the ledger F102 (the printed source omits the second factor \(2\)).
- \(i=2\): \(Q_0=R_0\cup\{a\}\), \(Q_1=R_1\cup\{v\}\), \(Q_2=R_2\cup\{b\}\). The last convolution estimate puts the other second norm on \(G_b\), a mass on \(G_a\), and \(2N_{1,e_0}(G_v)\) on \(v\), again with a factor one half.

Every old edge retains its type and multiplicity; the counting gives \(|Q_0|=|Q_1|\) and even \(|Q_2|\) in all three cases. This proves the regional half-bound using only the full induction hypothesis.

6. **Domestic endpoints and empty chains.** A domestic endpoint has its partner at or before its predecessor, so the half-bound applies on the entire domain; this also handles empty chains.

7. **Endpoints paired to each other (Case 2).** If \(u=n_1\) and \(v=2n\) are paired to each other, condition on their separate predecessors \((A,z),(B,w)\). The endpoint integral keeps the temporal argument \(r-q+A-B\); original stationary covariance Cauchy–Schwarz bounds it by \(N_{2,e}(G_u)N_{2,e}(G_v)\), translating each self-pairing separately. Induction and adding \(u,v\) to \(Q_2\) prove the full bound. There is no origin factor and no discarded predecessor-time offset.

8. **Both endpoint pairs cross and distinct (Case 3).** Let \(a\) be the partner of \(v\), \(b\) the partner of \(u\), \(p=u-1\), \(q=v-1\); then \(a<u\), \(b<v\). On \(\{s_a\le s_q\}\) remove \(v\) by the regional half-bound; the indicator is independent of \(s_v,x_v\). On the complementary region the chain orders give \(s_p\ge s_a>s_q\ge s_b\), so remove \(u\) instead. The removed partner has a successor on its own chain in both cases. The two bounds are \(P/2\) and \(P'/2\) for possibly different admissible products, so

\[
I_D=I_D(R_A)+I_D(R_B)\le\frac{P+P'}2\le\max(P,P').
\]

9. **Cap removal.** Increase \(L\) to infinity. Diagram integrands and all norm factors increase by positivity and monotone convergence; the maximum over the finitely many admissible products converges to the maximum of their limits. No kernel-independent or measurable maximizing choice is needed. Zero norms and measures require no exception because the positive cap convention avoids undefined products on the singular time diagonal.

**Cross-check with F101/F102/F103.** The F101 independent reconstruction matches this induction in the operative steps: the first-slot fusion is \(N_{1,e}(G*H)\le N_0(G)N_{1,e}(H)\) (not the unmultiplied \(N_2N_2\) conversion, which is obstructed by the exact finite-model ratio \(2N_1(G*H)/(N_2(G)N_2(H))=1+2/\pi>1\)); the empty-first-chain chronological base uses mass on the first kernel, first norm on the second; Case 2 keeps \(A-B\); Case 3 produces possibly different half-products and takes their maximum. F102 records the printed-source discrepancies (missing factor two, label swap, Case-2 offset omission). F103 states that current consumers need only the per-family existential bound and that the marked-edge/unmarked-norm envelopes are valid for every admissible partition.

**Consumed hypotheses.** \(G_l\ge0\) integrable with \(N_{1,e},N_{2,e}<\infty\) for all \(l,e\in D\); finite positive \(\mu_e\); Laplace domain \(A_e\subset(0,\infty)\); caps and positive-cap limits.

**Unproved conditions.** This is a reconstructed/corrected theorem, not an unconditionally accepted published statement: the printed source contains the discrepancies itemized in F101/F102, and the reconstruction has not been given an acceptance verdict here. Also, only the per-family existential form is derived; no single partition valid for all kernel families is asserted. Zero/uncapped diagonal handling rests on the positive cap convention.

## GLOBAL-UNPROVED-CONDITIONS

1. **Pairing-envelope dependency.** PROOF005, PROOF006, PROOF007, PROOF008, and PROOF010 consume Lemma L:pairing-product-envelope (EXTERNAL_CANDIDATE_OWN215), which is a reconstructed/corrected deterministic theorem. The printed source’s omitted first-slot factor two, the empty-chain base label swap, the Case-2 predecessor-offset omission, and the \(p18\) fused-\(N_2\) conversion are source-internal discrepancies (F101/F102). The current manuscript embeds the corrected derivation, but the corrected theorem remains a mathematical condition for every downstream application; no adoption label or source availability replaces its proof at the needed clause.

2. **No W-only measurability.** The positive-cutoff source fields are not in the closed range \(\Phi(H_W)\) whenever \(\Gamma\neq0\) and the cutoffs are positive and finite (the explicit \(q\perp\Phi(H_W)\) with \(\langle v,q\rangle>0\) counterexample in F194). Consequently the fixed extension must retain an auxiliary isonormal \(J\), and the positive-width fields are not \(\sigma(W)\)-measurable. This does not refute the isometry or the fixed-\(W+J\) construction, but it falsifies the stronger W-only/point-source-measurability assertion. Whether particular nonlinear/canonical limits are \(\sigma(W)\)-measurable by another argument is not settled by that counterexample alone.

3. **First-moment normalization.** \(L_*\) enters only conditionally through the intended first-moment lower bound. The printed normalization of Theorem T:first is not adopted; PROOF001’s numerical \(2L_*\) consequence is conditional.

4. **Source/lattice identification clauses.** The identifications with the actual Stratonovich/mild definitions (PROOF002, PROOF006, PROOF009) rely on the source’s common-prefix regularization, the Green-first convention in \(d=3\), and the joint covariance law (2.11)/(2.24). These are retained as mathematical inputs; the convergence records (F007) supply the fixed-\(W+J\) extension and source-law facts but do not by themselves prove the fixed-order/mild limits.

5. **Per-family versus universal partition.** Only the per-family existential pairing bound is claimed. The F103 consumer qualification establishes that the actual consumers need no common kernel-independent partition, but it does not promote the reconstruction to the stronger universal quantifier.

6. **No uniqueness and no full-goal closure.** PROOF009 proves the onefold Stratonovich mild identity but asserts no uniqueness; PROOF010’s majorant has exponent \(\rho>\kappa\) and does not settle the sharp-scale goal; PROOF007/PROOF008 provide fixed-\(t\) summability and mild-series convergence, not the intrinsic second-moment constant. No operator-Gaussian parent theorem, source-cutoff independence, point trace, grade conjunction, or full-goal closure is imported.

7. **Residual open items.** The joint fixed-order construction’s identification of \(X_n\) as the multiple Stratonovich integral of \(g_n\) depends on arbitrary-relative-rate limit arguments that are derived conditionally on the corrected envelope. The Brownian moment elimination, Laplace weak-limit identification by polynomial density, and Radon homogeneity-separation of horizon faces in PROOF005 are the actual derivations above and are not to be treated as favorable premises; their correctness is to be verified from those formulas.