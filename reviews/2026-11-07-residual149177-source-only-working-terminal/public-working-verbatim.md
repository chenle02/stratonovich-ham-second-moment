## PROOF149 — L:young-upper-growth (`L:young-upper-growth`)

**Statement.** Let \(\mathcal X\) be a nonzero real Banach space, \(B\ge 1\),
\(\tfrac12<\theta<1\), \(\nu=1/\theta<2\). All driver paths start at zero,
\[\|D\|_\theta=\sup_{t\le B}\|D(t)\|+[D]_\theta,\quad [D]_\theta=\sup_{s<t}\frac{\|D(t)-D(s)\|}{|t-s|^\theta},\]
and \(U_D=I+\int \mathrm dD\,U_D\) is the **left** Young evolution. With
\[c_\theta=2\max(1,C_\theta),\qquad c_{0}=C_\theta\text{ the Young bilinear constant from }|t-s|^{2\theta}\]
there is a dimension-free constant \(c_{\theta,B}\) such that, for \(d=\|D\|_\theta\),
\[\sup_{t\le B}\|U_D(t,0)\|\le\exp\!\bigl(c_{\theta,B}(d+d^{\nu})\bigr),\qquad
\|U_H\|_{C^\theta}+\|U_H^{-1}\|_{C^\theta}\le L_{\theta,B,K}<\infty\]
whenever \(\|H\|_\theta\le K\), \(K\ge1\).

**Proof ingredients.** Completeness of \(\mathcal B(\mathcal X)\) and operator multiplication of norm \(1\); the scaled norm
\(N_\ell(V)=\sup\|V\|+\ell^\theta[V]_\theta\) with
\(N_\ell(\int_a^{\scriptscriptstyle\cdot}\mathrm dD\,V)\le c_\theta[D]_\theta\ell^\theta N_\ell(V)\);
whole-interval contraction when \(c_\theta dB^\theta\le1/4\); equal-piece splitting otherwise; at \(d=0\), \(U_D=I\); inverse via the Neumann series on each local piece and
\(U_H^{-1}(t)-U_H^{-1}(s)=-U_H^{-1}(t)(U_H(t)-U_H(s))U_H^{-1}(s)\).

**Remaining condition / falsified item.** No fixed prefactor; endpoint identity \(d=0\Rightarrow U_D=I\); uniform inverse control holds only on the fixed driver ball \(\|H\|_\theta\le K\), not on all paths. The estimate is for left Young \(\theta>1/2\) only; no unbounded-operator path is admitted.

---

## PROOF150 — P:young-upper-multiplicative (`P:young-upper-multiplicative`)

**Statement.** If \(K\ge1\), \(\|H\|_\theta\le K\), \(x=\|X\|_\theta\), and \(A\in\mathcal B(\mathcal X)\), then
\[\|A\,U_{H+X}(t,0)\|\le\|A\,U_H(t,0)\|\exp\!\bigl(C_{\theta,B,K}(x+x^{\nu})\bigr),\qquad 0\le t\le B.\]
This holds with arbitrary \(A\), including noninvertible \(A\) and \(A=0\), with no extra factor when \(x=0\).

**Proof ingredients.** Put \(U=U_H\), \(R=U^{-1}\), \(G(s)Z=R(s)ZU(s)\). \(G\) is a \(C^\theta\) path of bounded maps on \(\mathcal B(\mathcal X)\), uniformly bounded on the fixed ball, so the Banach Young integral
\[Z(t)=\int_0^t R(s)\,\mathrm dX(s)\,U(s)\]
exists with \(\|Z\|_\theta\le L'_{\theta,B,K}x\) and \(Z_{s,t}=R(s)X_{s,t}U(s)+O(|t-s|^{2\theta})\). Writing \(V=U_Z\), the left Young remainders combine as
\[U_{H+X}=U_H\,U_Z\]
without smooth density in the full Hölder norm; the cross term is of order \(2\theta\). Then PROOF149 is applied to \(Z\), and \(A\) is left-multiplied.

**Remaining condition / falsified item.** The ordered product \(U_{H+X}=U_HU_Z\) must not be replaced by the reverse order \(U_ZU_H\) for a general noncommuting left-Young integrand; the endpoint factor \(\|AU_H(t)\|\) is retained exactly at \(X=0\). Noninvertibility/zero \(A\) is allowed because the proof only uses submultiplicativity, never invertibility of \(A\).

---

## PROOF151 — L:uniform-mean-cutoff (`L:uniform-mean-cutoff`)

**Statement.** For real Schwartz cutoff \(\eta\) with \(\eta=1\) on \(B_1\), \(0\le\eta\le1\), \(\operatorname{supp}\eta\subset\overline B_2\), set \(\eta_R(x)=\eta(x/R)\), \(m_R=\eta_R^2\), \(R\ge1\), \(E=H^{1/2}\times H^{-1/2}\), \(\alpha/4<s<1/2\), \(\beta=1/2-s>0\), \(A_s=C_s^2\sqrt{R_{\mathrm{sp}}}\). The physical row is
\[k_R(z,w)=(\eta_R z_1)(\eta_R\Lambda^{-1}w_2),\qquad \langle T_Rq,z,w\rangle_E=\langle q,k_R(z,w)\rangle_{H_{\mathrm{sp}}}.\]
For every real \(\sigma\), multiplication by \(\eta_R\) on \(H^\sigma\) has norm at most
\[M_\sigma=2^{|\sigma|/2}(2\pi)^{-d/2}\int_{\mathbb R^d}|\widehat\eta(p)|\langle p\rangle^{|\sigma|}\mathrm dp,\]
independently of \(R\ge1\). With \(M=M_{1/2}\), \(M_0=A_sM^2\),
\[\|k_R(z,w)\|_{H_{\mathrm{sp}}}\le M_0\|z\|_E\|w\|_E,\qquad
\|T_R\|_{H_{\mathrm{sp}}\to\mathcal L(E)}\le M_0.\]
The physical mask occurs **once**, after the covariance convolution; the mean domain is \(E\).

**Remaining condition / falsified item.** Uniform-radius claims are on \(E\) only; the constant-data columns of \(F=E\oplus\mathbb R^2\) are outside \(E\) and are not covered here. No uniform \(F\)-column or path-norm claim is made.

---

## PROOF152 — L:uniform-mean-spatial-tails (`L:uniform-mean-spatial-tails`)

**Statement.** Let \(C_\varepsilon\) be the covariance-Hilbert heat contraction with Fourier multiplier
\(e^{-\varepsilon|\xi|^2/2}\), and let \(P_K\) be the real orthogonal projection on \(H_{\mathrm{sp}}\) for the closed frequency ball \(\{|\xi|\le K\}\). \(P_K\) commutes with heat. For \(K\ge1\), \(\varepsilon>0\), \(R\ge1\), with \(\beta=1/2-s\),
\[\|T_R(I-C_\varepsilon)\|_{\mathcal B(H_{\mathrm{sp}},\mathcal L(E))}\le M_h\varepsilon^{\beta/2},\qquad
M_h=4A_sM^2\mathbb E|G_d|^\beta,\]
\[\|T_R(I-P_K)\|_{\mathcal B(H_{\mathrm{sp}},\mathcal L(E))}\le M_fK^{-\beta},\qquad
M_f=\frac{M_h}{1-e^{-1/2}},\]
where \(G_d\) is a standard \(d\)-dimensional Gaussian.

**Proof ingredients.** Translation covariance bound
\(\|\tau_hk_R(z,w)-k_R(z,w)\|_{H_{\mathrm{sp}}}\le4A_sM^2\min(1,|h|^\beta)\|z\|_E\|w\|_E\);
Bochner Gaussian integral \(\int p_\varepsilon(h)\tau_hk\,\mathrm dh=C_\varepsilon k\); indicator multiplication on the **closed image** of the covariance Fourier isometry gives \(P_K\); \(1-e^{-|\xi|^2/(2K^2)}\ge1-e^{-1/2}\) on \(|\xi|>K\).

**Remaining condition / falsified item.** \(P_K\) is allowed to have infinite rank; no surjectivity onto \(L^2(\mu)\), no spectral density, and no finite-rank restriction is claimed. Heat filtering alone is not an orthogonal projection in \(H_{\mathrm{sp}}\); \(P_K\) is constructed on the actual closed Fourier image.

---

## PROOF153 — L:uniform-mean-tensor (`L:uniform-mean-tensor`)

**Statement.** If \(H_0,G\) are real Hilbert spaces, \(2\le r<\infty\), and \(A:H_0\to L^r(I)\) is bounded, then
\[\|A\otimes I_G\|_{H_0\otimes G\to L^r(I;G)}\le\|A\|.\]
The tensor extension need not be compact when \(A\) is compact: for \(Af\ne0\) and an infinite orthonormal \((e_j)\subset G\), the images \(Af\otimes e_j\) have pairwise distance \(\sqrt2\|Af\|_{L^r}\), so no convergent subsequence exists.

**Proof ingredients.** Finite tensors \(v=\sum_{j=1}^n f_j\otimes e_j\), independent standard normals \(\gamma_j\), \(m_r=\mathbb E|\gamma_1|^r\ge1\); convexity of \(s\mapsto s^{r/2}\) on the covariance eigenvalues gives
\(\mathbb E\|\sum_j\gamma_jf_j\|_{H_0}^r\le m_r(\sum_j\|f_j\|^2)^{r/2}\); Tonelli; density.

**Remaining condition / falsified item.** Compact scalar time-tail tensored with an infinite identity is **not** compact. This corrects the possible pitfall that a scalar compact \(C_t\) kills the spatial head: it does not; spatial tail uses the actual frequency projection \(P_K\).

---

## PROOF154 — P:uniform-mean-regulator (`P:uniform-mean-regulator`)

**Statement.** With the actual supported tensor \(H_I=H_t\otimes H_{\mathrm{sp}}\), the compact scalar covariance map
\(C_t:H_t\to L^r(I)\), \(2<r<2/a\), and \(U=C_t\otimes I_{H_{\mathrm{sp}}}\), let \(\pi_J\) be the first-\(J\) time-basis projection, \(\varepsilon_J=\|C_t(I-\pi_J)\|_{H_t\to L^r(I)}\), and \(\mathcal T_R=T_RU\). Then
\[P_{\mathrm{ret}}=\pi_J\otimes P_K,\qquad Q_{J,K}=I-P_{\mathrm{ret}}\]
are real orthogonal projections and \(\varepsilon_J\to0\). Uniformly for \(R\ge1\), with \(c_t=\|C_t\|\),
\[\|\mathcal T_R\|_{H_I\to L^r(I;\mathcal L(E))}\le M_0c_t,\qquad
\|\mathcal T_RQ_{J,K}\|_{H_I\to L^r(I;\mathcal L(E))}\le M_0\varepsilon_J+M_fc_tK^{-\beta}.\]
The decomposition is the typed time head (scalar compact \(C_t\)) plus the spatial frequency tail (\(P_K\)), and it is not a modulus/maximum bound.

**Remaining condition / falsified item.** There is no \(R\)-uniform compactness of \(\mathcal T_R\). Infinite spatial rank is allowed; this proposition bounds the completed mean but does not compact it uniformly in \(R\), and does not bound the expected residual path norm.

---

## PROOF155 — P:uniform-actual-cameron (`P:uniform-actual-cameron`)

**Statement.** Use \(B,\delta,N,s_m,\ell_m,I_m,\theta,r,p\) with the exact admissible package
\[\frac12<\theta<\min\!\Bigl(1-\frac a2,\frac{3-a-\alpha}{2}\Bigr),\qquad
\frac1{1-\theta}<r<\frac2a,\qquad
\frac1\theta\le p<2<r.\]
Let \(i_I:H_I\to H_W\) be the isometric closed inclusion, \(P_{\mathrm{full}}=i_IP_{\mathrm{ret}}i_I^*\),
\(Q_{\mathrm{full}}=I-P_{\mathrm{full}}\), \(T_{\delta,m}\) the raw isometry (147/148),
\[Y_m(f)=W(Q_{\mathrm{full}}T_{\delta,m}f),\qquad
X_m(u)=g_\delta A_{m_R}(Y_m)(\min(u,\ell_m)),\qquad g_\delta=\delta^{(1-a)/2}.\]
Then \(X=(X_m)\) is a centered Gaussian tuple in the separable little Hölder compact-operator space on \(E\), its actual Bochner covariance is
\[(Lh)_m(u)=\sqrt\delta\int_0^{\min(u,\ell_m)}S_E(-v)\mathcal T_R(Q_{J,K}i_I^*h)(s_m+\delta v)S_E(v)\mathrm dv,\]
and in the norm \(\|x\|_{\delta,p}=(\delta\sum_m\|x_m\|_{C^\theta}^p)^{1/p}\),
\[\|Lh\|_{\delta,p}\le\sqrt\delta\,C_{B,E}(2/B)^{1/p-1/r}[M_0\varepsilon_J+M_fc_tK^{-\beta}]\|h\|_{H_W},\qquad
C_{B,E}\le18B^{3-1/r}.\]
The Cameron norm is the minimum raw \(H_W\)-preimage norm on the actual first chaos.

**Remaining condition / falsified item.** \(P_{\mathrm{full}},\,Q_{\mathrm{full}}\) fields are independent; residual time blocks may remain correlated; the retained spatial head may have infinite rank. Heat filtering alone does not give the orthogonal decomposition. This is a **linear Cameron-metric bound**, not an expected-path-norm bound uniform in \(R\), not an \(F\)-column bound, and not a covariance order; all spatial constants are independent of \(R\ge1\) but \(Y_m\) is real Gaussian obtained by orthogonal residual projection.

---

## PROOF156 — L:radius-outer-maps (`L:radius-outer-maps`)

**Statement.** Fix \(\chi_0,\psi_0\in C_c^\infty\), \(\chi_0=\eta^2\)-type plateau on \(B_1\), \(\psi_0=1\) on a neighborhood of \(\operatorname{supp}\chi_0\), \(\operatorname{supp}\psi_0\subset B_3\). For \(\rho\ge1\), \(\chi_\rho=\chi_0(\cdot/\rho)\), \(\psi_\rho=\psi_0(\cdot/\rho)\), \(L=2\pi\rho\), auxiliary torus \(H^r(\mathbb T_L;\mathrm dx)\) with modes \(L^{-d/2}e^{ik\cdot x/\rho}\). The periodization and recovery maps satisfy, for every real \(r\),
\[\|\mathcal P_{\psi_\rho}:H^r(\mathbb R^d)\to H^r(\mathbb T_L)\|\le C_{\psi_0,r},\qquad
\|\mathcal E_{\chi_\rho}:H^r(\mathbb T_L)\to H^r(\mathbb R^d)\|\le C_{\chi_0,r},\]
independently of \(\rho\ge1\).

**Proof ingredients.** Exact weighted Fourier kernels; no extra \((2\pi)^{-d/2}\); Peetre inequality for positive and negative \(r\); the factor
\(\rho^{d/2}\) from the lattice side cancels \(\rho^{-d/2}\) from the continuum side in the mixed Schur bound; the lattice sum at spacing one has no remaining \(\rho\) dependence.

**Remaining condition / falsified item.** All real Sobolev indices are covered by exact whole-space recovery; no rough-point Fourier sampling is used. This is a factor of the envelope operator, not a rough-path or Gaussian statement.

---

## PROOF157 — P:radius-compact-envelopes (`P:radius-compact-envelopes`)

**Statement.** For real \(\sigma\), \(\gamma>0\), \(q\ge1\) with \(q\gamma>d\),
\[\|\Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma}\|_{S_q}\le
C_{\sigma,\gamma,q,d,\chi_0,\psi_0}\,\rho^{d/q}.\]
In the balanced coordinates of the compact cutoff, for the fixed even index \(Q\ge2\),
\[\|K_{\mathrm{in}}\|_{S_Q}=\|K_{\mathrm{out}}\|_{S_Q}\le C_Q\rho^{d/Q}.\]
\(K_{\mathrm{out}}=P_{\chi_\rho}D_\gamma\) and \(K_{\mathrm{in}}=P_{\chi_\rho}^*D_\gamma\); \(K_{\mathrm{in}}=VK_{\mathrm{out}}V\) for the unitary coordinate swap \(V(z_1,z_2)=(z_2,z_1)\).

**Proof ingredients.** Recovery identity
\(\Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma}=\Lambda^\sigma\mathcal E_{\chi_\rho}\mathcal I_\gamma\mathcal P_{\psi_\rho}\Lambda^{-\sigma-\gamma}\);
diagonal torus singular values \(\langle k/\rho\rangle^{-\gamma}\); lattice volume
\(\sum_k\langle k/\rho\rangle^{-u}\le C\rho^d\) for \(u=q\gamma>d\); finite-rank approximation and ordered singular values.

**Remaining condition / falsified item.** This is **one** \(S_Q\)-envelope of size \(\rho^{d/Q}\), equal for input and output by the balanced adjoint/swap; it is not two separate \(L^2\)-radius losses and not a Hilbert–Schmidt \(\rho^{d/2}\) factor. The index \(Q>d/\gamma\) is fixed and even; no endpoint \(q\gamma=d\) claim.

---

## PROOF158 — P:radius-actual-moments (`P:radius-actual-moments`)

**Statement.** Under
\[0<\gamma<\min\!\Bigl(\tfrac12,\frac{2-\alpha}{2}\Bigr),\qquad
\tfrac12<\theta<\eta_t<\beta_t<\min\!\Bigl(1-\tfrac a2,\frac{3-a-\alpha}{2}\Bigr),\]
and one fixed even \(Q\ge2\) with
\[Q\gamma>d,\qquad \beta_t-\eta_t-\frac1Q>0,\qquad Q>\frac{2d}{1-a},\]
the actual zero-start \(E\) interaction driver \(M_R(W)=A_{m_R}(W)\) satisfies, for every finite \(v\ge1\),
\[\|M_R(W)\|_{L^v(C^\theta([0,B];\mathcal L(E)))}\le C_{Q,B}\sqrt v\,R^{d/Q},\qquad R\ge1.\]
The constant is independent of \(v\) and \(R\).

**Proof ingredients.** Both actual finite weighted variances \(V_{\mathrm{out},N},V_{\mathrm{in},N}\le b_I D_\gamma^2\) and both localizations \(P_{\chi_\rho}\); finite Gaussian matrix bound with \(p=Q\); \(S_Q\) dominance \(\|K_{\mathrm{out}}\|_{S_q}\le\|K_{\mathrm{out}}\|_{S_Q}\) for \(q\ge Q\); increment \(L^q\) bounds with exponent \(\beta_t\); dyadic chaining with \(\eta_t\) and grid factor \(2^{n/q}\); Lyapunov to arbitrary \(v\).

**Remaining condition / falsified item.** This is an \(E\) first-driver path moment only. The two constant columns on \(F\) require separate estimates, and any projection inserted into a Cameron comparison must itself satisfy the actual orthogonality/covariance hypotheses. The bound is fixed-\(R\); no uniform-radius convergence in the chaining is asserted. The \(Q\) margin condition is strict and \(Q,B\) are fixed before any \(\delta\to0\).

---

## PROOF159 — C:radius-covariance-residuals (`C:radius-covariance-residuals`)

**Statement.** Let \(Y\) be a centered Gaussian linear noise on the actual coupled space with
\(\mathrm{Var}\,Y(f)\le C\|f\|_{H_W}^2\), \(C\ge0\). Its transferred driver obeys
\[\|M_R(Y)\|_{L^v(C^\theta)}\le\sqrt C\,C_{Q,B}\sqrt v\,R^{d/Q}.\]
In particular \(C=1\) is valid for
\[Y_m(f)=W((I-\Pi)T_{\delta,m}f),\]
where \(\Pi\) is any deterministic orthogonal projection on the slow \(H_W\); \(\Pi\) may have infinite rank and may depend on \(\delta,R\).

**Proof ingredients.** This is the pure linear Gaussian covariance contraction (source transfer); raw pullback isometry \(\|T_{\delta,m}f\|=\|f\|\); \(\|I-\Pi\|\le1\).

**Remaining condition / falsified item.** The projection must be **deterministic**; never noise-dependent. This is a linear covariance comparison only; it does not transfer any nonlinear product or F-column moment.

---

## PROOF160 — P:radius-mean-anchor (`P:radius-mean-anchor`)

**Statement.** Fix \(B\ge1\), the true partition \(B,\delta,N,\ell_m\), \(0<\delta<\min(1,1/B)\),
\(N=\lfloor1/(\delta B)\rfloor\), \(g_\delta=\delta^{(1-a)/2}\), fixed \(p\ge1\). For \(Y_m\) as in PROOF159,
\[X_m(u)=g_\delta M_R(Y_m)(\min(u,\ell_m)),\qquad
Z_\delta=\Bigl(\delta\sum_{m=0}^N\|X_m\|_{C^\theta}^p\Bigr)^{1/p|_p},\]
then
\[\mathbb E Z_\delta\le(2/B)^{1/p}C_{Q,B}\sqrt p\,g_\delta R^{d/Q}.\]
For \(R_\delta=\delta^{-1}+2\le3/\delta\),
\[2\mathbb E Z_\delta\le2(2/B)^{1/p}C_{Q,B}\sqrt p\,3^{d/Q}\delta^{e_{\mathrm{anchor}}}\to0,\qquad
e_{\mathrm{anchor}}=\frac{1-a}{2}-\frac dQ>0.\]
Uniform in the deterministic residual projection.

**Proof ingredients.** Stopping does not increase \(\sup\) or Hölder semi-norm; linearity of expectation for a finite sum; \(N+1\le2/(\delta B)\); Lyapunov; the third fixed-\(Q\) guard \(Q(1-a)>2d\) makes \(e_{\mathrm{anchor}}>0\).

**Remaining condition / falsified item.** This is an expected first-driver mean anchor on \(E\); it is finite weighted block sum, not a maximum and not an independence/block-product estimate. \(B,p,Q\) are fixed first, then \(\delta\to0\); no \(F\)-column, cone-coverage, source-to-point, or nonlinear upper follows.

---

## PROOF161 — L:signed-limiting-multiplier (`L:signed-limiting-multiplier`)

**Statement.** For a fixed finite mask \(m_R=\eta_R^2\), \(V_q=m_R(\Gamma*q)\) for real \(q\in C_c^\infty\), and
\(L_q(u,v,c_1,c_2)=(0,V_q(u+c_1),0,0)\) on \(F=E\oplus\mathbb R^2\), let \(\mathcal V_R\) be the operator-norm closure in \(\mathcal K(F)\). Every \(L\in\mathcal V_R\) determines a unique real \(V\in H^{-1/2}\), \(\operatorname{supp}V\subset\operatorname{supp}m_R\), with
\[L(u,v,c_1,c_2)=(0,Vu+c_1V,0,0),\qquad
|v_V(u,w)|\le\|L\|\,\|u\|_{H^{1/2}}\|w\|_{H^{1/2}},\]
where the multiplication \(H^{1/2}\to H^{-1/2}\) extends from compact smooth tests, and \(v_V(u,w)=\langle V,uw\rangle\).

**Proof ingredients.** The constant-displacement column has norm \(1\), so \(\|V_{q_n}-V_{q_j}\|_{H^{-1/2}}\le\|L_{q_n}-L_{q_j}\|\); smooth multiplication bound on \(H^{-1/2}\); test-pairing identification; complexification.

**Remaining condition / falsified item.** This is a signed distributional multiplier in \(H^{-1/2}\); no \(H^1\)-algebra, no point trace, and no pointwise representative of the unsigned potential are assumed. The recovered \(V\) can be oscillatory and need not be a function.

---

## PROOF162 — P:signed-closed-form (`P:signed-closed-form`)

**Statement.** Let \(K\ge\max(1,\|L\|)\), \(c=2+K^2\), and on complexified \(L^2\) define the Hermitian closed form
\(q_V(u)=\|\nabla u\|_2^2-v_V(u,u)\), \(Q(q_V)=H^1\). This represents a unique self-adjoint \(H_V\). With \(A=H_V+c\ge1\), \(L_K=3(1+K^2)\),
\[D(A^{1/2})=H^1,\qquad
\tfrac12\|u\|_{H^1}^2\le q_V(u)+c\|u\|_2^2\le L_K\|u\|_{H^1}^2,\]
\[D(A^{1/4})=H^{1/2},\qquad
2^{-1/4}\|u\|_{H^{1/2}}\le\|A^{1/4}u\|_2\le L_K^{1/4}\|u\|_{H^{1/2}},\]
and the negative dual completion is \(H^{-1/2}\). **No \(H^2\) operator domain is asserted.**

**Proof ingredients.** Fourier-Cauchy-Schwarz and the signed form bound give
\(|v_V(u,u)|\le K\|u\|_{H^1}\|u\|_2\); closed semibounded form \((\|u\|_{H^1}-\)weighted equivalent norm with shift \(c\)); Teschl Theorem 2.14 (2.63) representation; resolvent/square-root order
\(\tfrac12(1-\Delta)\le A\le L_K(1-\Delta)\) obtained via completing the square
\(\langle f,(T_0+t)^{-1}f\rangle=\sup_u\{2\operatorname{Re}\langle f,u\rangle-q_{T_0}(u)-t\|u\|^2\}\)
and
\(\sqrt x=\pi^{-1}\int_0^\infty t^{-1/2}x/(x+t)\mathrm dt\), giving \(T_0^{1/2}\le S_0^{1/2}\) as forms; duality.

**Remaining condition / falsified item.** Teschl's closed-form theorem is used on the dense closed form domain \(H^1\); the quarter-power domain follows from flat resolvent order, **not** from arbitrary operator-power monotonicity. \(K\) is not an arbitrary larger shift; it is tied to \((1+K^2)\) by the choice \(c=2+K^2\).

---

## PROOF163 — L:signed-spectral-wave (`L:signed-spectral-wave`)

**Statement.** Let
\[\beta(V)=\inf_{\substack{u\in H^1\\ \|u\|_2=1}}q_V(u),\qquad \lambda(V)=\sqrt{-\beta(V)}.\]
Then \(\beta(V)=\inf\operatorname{spec}H_V\), \(-K^2\le\beta(V)\le0\), and the spectral wave on \(E\) obeys
\[\|P_V^E(t)\|\le8(1+K)^2(1+t)\,e^{\lambda(V)t},\qquad t\ge0.\]
The spectral wave matrix in the \(A=q_V+c\)-weighted phase is
\[\begin{pmatrix}C_t(h)&\sqrt{h+c}\,S_t(h)\\ -hS_t(h)/\sqrt{h+c}&C_t(h)\end{pmatrix},\]
with \(C_t,S_t\) the cosine/sine or hyperbolic cosine/sine functions, including the value \((1,t)\) at \(h=0\).

**Proof ingredients.** \(-K^2\le q_V(u)\) for unit \(u\); translated compact bumps with support outside \(\operatorname{supp}m_R\) give \(\beta\le0\); Teschl (3.52)–(3.53) identifies the form infimum with the spectral bottom; the lower bound \(\beta=-K^2\)-control comes from a unit \(u\) with \(\|u\|_2=1,\|u\|_{H^1}\ge1\); the wave entries are bounded using \(|S_t(h)|\le t e^{\lambda t}\) for \(h<0\) and \(\min(t,h^{-1/2})\) for \(h>0\); condition-number cost \(M_K^2\le2(1+K)\).

**Remaining condition / falsified item.** Zero top energy is reached by outside-support translated trials with \(\lambda\to0\); no division by \(\lambda\), and no positive ground state or gap is assumed. PVM support/domain and condition numbers are tracked, not replaced by point-operator power rules.

---

## PROOF164 — P:signed-physical-wave (`P:signed-physical-wave`)

**Statement.** The spectral wave of PROOF163 equals the actual bounded-perturbation/Young physical wave on \(E\); its \(F\)-extension satisfies
\[\|P_V(t)\|_{\mathcal L(F)}\le16(1+K)^4(1+t)^3\,e^{\lambda(V)t},\qquad t\ge0,\]
including both constant response columns, with full forcing
\[P_V(t)(e,c)=\Bigl(P_V^E(t)e+\int_0^t P_V^E(t-s)(0,V(c_1+sc_2))\mathrm ds,\ C(t)c\Bigr).\]
**No \(D(A^{3/4})=H^{3/2}\) assertion is used.**

**Proof ingredients.** From the form representation, \(H_V=\Delta+V\) distributionally on \(D(H_V)\), giving \(D(H_V)\hookrightarrow H^{3/2}\) through \((1-\Delta)u=(H_V+V+1)u\); the free generator is \((v,\Delta u)\) on \(H^{3/2}\times H^{1/2}\); spectral graph trajectories and Duhamel in \(E\); density of graph data; Volterra uniqueness; \(F\)-variation of constants; forcing norm \(\le K(1+s)\), and
\(\int_0^t(1+t-s)(1+s)\mathrm ds\le(1+t)^3\).

**Remaining condition / falsified item.** No \(D(A^{3/4})=H^{3/2}\) shorthand is relied on; the chain \(D(H_V)\to H^{3/2}\) comes from the first-order distributional equation, not a fractional-power interpolation. The \(F\)-bound retains both constants and has \((1+t)^3\); there is no positive ground assertion. If later sharpening uses \(K\le1+\|L\|\), it uses \(K=\max(1,\|L\|)\), not an arbitrary larger \(K\).

---

## PROOF165 — L:symplectic-free (`L:symplectic-free`)

**Statement.** On \(E=H^{1/2}\times H^{-1/2}\), with \(\Lambda=(1-\Delta)^{1/2}\) and the balanced isometry
\(C_{\mathrm{bal}}(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)\),
\[J_E=C_{\mathrm{bal}}^{-1}J_{\mathrm{symp}}C_{\mathrm{bal}},\qquad
J_{\mathrm{symp}}(q,p)=(p,-q),\qquad J_E^2=-I,\]
\[\omega(z,w)=\langle z,J_Ew\rangle_E=\langle u,g\rangle_{H^{1/2},H^{-1/2}}-\langle f,v\rangle_{H^{1/2},H^{-1/2}},\qquad z=(u,v),\,w=(f,g).\]
The free group preserves \(\omega\); \(B(b)(u,v)=(0,bu)\) is \(\omega\)-skew. For zero-start \(X\in C^\theta([0,T];\mathcal K(E))\),
\[U_X(t,s)-I\in\mathcal K(E),\qquad
\|S_E(t)U_X(t,s)S_E(-s)\|\ge\|S_E(t-s)\|\ge1,\qquad 0\le s\le t\le T.\]
For finitely many such paths,
\[P_N\cdots P_0-S_E\Bigl(\sum_j\ell_j\Bigr)\in\mathcal K(E),\qquad
\|P_N\cdots P_0\|\ge\|S_E(\sum_j\ell_j)\|\ge1.\]

**Proof ingredients.** Compact left-Young sums; translations \(\tau_y\) on both entries are isometries commuting with \(S_E(h)\), the translated pairing is Fourier of an \(L^1\) function, so \(\tau_y z\rightharpoonup0\), hence compact perturbations do not lower the free norm; free invertibility
\(S_E(-h)=\mathcal R S_E(h)\mathcal R\), \(\mathcal R(u,v)=(u,-v)\), gives \(1\le\|S_E(h)\|^2\); telescoping finite products.

**Remaining condition / falsified item.** **Compactness alone does not imply symplecticity**: the above is a lower-bound baseline valid for all compact-driver tuples, not only Hamiltonian/Gaussian ones. \(\operatorname{im}(P_N\cdots P_0-S_E(\sum\ell_j))\) is compact, but conservation must be proved separately (PROOF168).

---

## PROOF166 — L:symplectic-source-mean (`L:symplectic-source-mean`)

**Statement.** For fixed \(R,T>0\), mask \(m_R\), \(c\in\mathbb R\), \(\Phi\in H_W\),
\[Z=W(\Phi),\qquad D_\Phi=\mathbb E[ZM],\qquad D_\Phi^\rho=\mathbb E[ZM^\rho],\qquad
D=cM+D_\Phi,\qquad D^\rho=cM^\rho+D_\Phi^\rho,\]
all in \(\mathcal B(E)\) paths. Then the expectations are Bochner-defined and
\[\|D_\Phi^\rho-D_\Phi\|_{C^\theta}\le\|\Phi\|_{H_W}\|M^\rho-M\|_{L^2C^\theta}\to0.\]
For each positive \(\rho=(\varepsilon,\eta)\), there is a deterministic real time-continuous, spatially smooth
\(h_\Phi^\rho\) such that
\[D_\Phi^\rho(t)=\int_0^t S_E(-r)B(m_Rh_\Phi^\rho(r))S_E(r)\mathrm dr,\]
a Lipschitz operator path, and the combined source coefficient is
\[b^\rho=m_R(cY^\rho+h_\Phi^\rho).\]

**Proof ingredients.** Gaussian \(L^2\) path moments; retaining isometry \(j_{\mathrm{src}}:H_W\to\mathcal G\), isonormal \(\mathcal I\) with \(\mathcal I(j_{\mathrm{src}}h)=W(h)\); pointfield
\(Y^\rho(t,x)=\mathcal I(v_{\rho;t,x})\); \(h_\Phi^\rho(t,x)=\langle j_{\mathrm{src}}\Phi,v_{\rho;t,x}\rangle_{\mathcal G}\); row identification by Fubini.

**Remaining condition / falsified item.** The source uses the fixed \(W+\) one auxiliary \(J\) extension; the countercheck (F194) shows **positive-cutoff point features are not in the closed image of the raw feature map**, so \(Y^\rho\) is not \(W\)-measurable in general. This does not falsify the fixed-extension retention or the mean and covariance identities; no Cameron-shift identity is asserted here. Any \(W\)-only measurability claim must not be imported from this proposition.

---

## PROOF167 — P:symplectic-source (`P:symplectic-source`)

**Statement.** At each fixed positive \(\rho\), on one probability-one set for the fixed \(c,\Phi,R,T\),
\[P_{D^\rho}(t,s)^*J_EP_{D^\rho}(t,s)=J_E,\qquad 0\le s\le t\le T,\]
where \(P_{D^\rho}(t,s)=S_E(t)U_{D^\rho}(t,s)S_E(-s)\).

**Proof ingredients.** Intersect the regularity event and the ordinary-primitive identification; \(b^\rho\) has one compact support and is continuous in \(\sup\)-norm, uniformly bounded; \(C_b(r)=S_E(-r)B(b^\rho(r))S_E(r)\) is skew for \(\omega\); the Young equation equals the statewise C^1 equation
\(U(t,s)e=e+\int_s^t C_b(r)U(r,s)e\,\mathrm dr\); differentiation of the bounded bilinear \(\omega\) kills the time derivative.

**Remaining condition / falsified item.** Conservation is proved at fixed \(\rho\) by the ordinary C^1 source equation, not by a source limit or an unproved raw conservation; no uncountable intersection of source parameters is used. The combined source \(b^\rho\) is generally noncentered.

---

## PROOF168 — P:symplectic-raw (`P:symplectic-raw`)

**Statement.** For the fixed \(c,\Phi,R,T\) in closed form,
\[P_D(t,s)^*J_EP_D(t,s)=J_E,\qquad
\|P_D(t,s)\|\ge1,\qquad 0\le s\le t\le T,\]
the flow is invertible, and for \(c=0\) the assertion is deterministic for each fixed \(\Phi\).

**Proof ingredients.** The closed real linear constraint
\(\mathfrak g_J=\{A:A^*J_E+J_EA=0\}\) is satisfied by each deterministic coefficient
\(A_j(0,t)\) because \(H_{j,R}\) is real and the free group preserves \(\omega\); finite sums and their \(L^2C^\theta\) limit obey the same constraint; the Bochner mean \(D_\Phi\) also lies in \(\mathfrak g_J\); Young remainders give
\(V(v)-V(u)=D_{u,v}V(u)+R_{u,v}\), \(\|R_{u,v}\|\le C|v-u|^{2\theta}\); the first-order term
\(V(u)^*(D_{u,v}^*J_E+J_ED_{u,v})V(u)\) vanishes, and the remaining \(2\theta\)-terms sum to zero as the mesh vanishes. Invertibility comes from local Young Neumann pieces and finite products, followed by the free inverse.

**Remaining condition / falsified item.** Raw conservation is derived directly from the real \(J\)-skew coefficient constraint and Young remainder \(2\theta>1\), **not** from the unproved source conservation or infinite-dimensional conservation. Invertibility is from Young Neumann pieces, **not** from conservation alone.

---

## PROOF169 — P:symplectic-block-mean (`P:symplectic-block-mean`)

**Statement.** With \(B,\delta,N,s_m,\ell_m\) fixed, \(i_I:H_I\to H_W\), \(T_m=T_{\delta,m}\) the raw isometry, \(W_m(f)=W(T_mf)\), for \(\Phi\in H_I\),
\[\phi_m=\delta^{-a/2}T_m^*i_I\Phi,\qquad \mathcal T_E\Phi=i^*T\Phi\,i,\]
where \(T\) is the actual full \(F\) mean. Define
\[H_{m,E}(\Phi)(u)=\int_0^{\min(u,\ell_m)}S_E(-v)\mathcal T_E\Phi(s_m+\delta v)S_E(v)\mathrm dv,\]
\[M_m=M_R(W_m),\qquad D_{\phi_m}(u)=\mathbb E[M_m(u)W_m(\phi_m)].\]
Then
\[D_{\phi_m}(\min(u,\ell_m))=H_{m,E}(\Phi)(u),\qquad 0\le u\le B,\]
and consequently
\[\|S_E(\ell_m)U_{H_{m,E}(\Phi)}(\ell_m,0)\|\ge1,\qquad (\ell_m=0\text{ gives the identity, norm }1).\]

**Proof ingredients.** Pullback covariance factor \(\delta^{a-2}\delta^2\delta^{-a}=1\); \(T_mT_m^*\) is the projection on the raw image; the unscaled covariance is
\[\mathbb E[M_m(u)W(i_I\Phi)]=\delta^{a/2}H_{m,E}(\Phi)(u),\quad u\le\ell_m,\]
so dividing by \(g_\delta\delta^{a/2}=\delta^{a/2}\) gives the direction \(\phi_m\); compact Bochner primitive and \(1-1/r>\theta\).

**Remaining condition / falsified item.** The unscaled covariance factor is \(\delta^{a/2}\), **not** \(\sqrt\delta\); \(\sqrt\delta\) appears only after the global \(g_\delta\). The full \(F\) constant columns are kept until the \(E\)-compression and velocity column are used; fast directions for the symplectic baseline are **not** separate action costs or uniform budgets. This is a fixed-parameter identity; no uniform \(R\)-budget or source-to-point transfer is claimed.

---

## PROOF170 — P:tube-wiener-realization (`P:tube-wiener-realization`)

**Statement.** \(H\) real separable Hilbert; \(W\) its isonormal process; \(X\) strongly measurable centered Gaussian in a real separable Banach \(\mathscr B\), \(\mathbb E\|X\|^2<\infty\); every continuous linear coordinate \(\ell(X)=W(k_\ell)\); \(0<\delta<1\);
\[Ch=\mathbb E[XW(h)]=\sqrt\delta\,\mathcal M_\delta h,\qquad
H_{\mathrm{seen}}=\overline{\operatorname{span}\{k_\ell\}},\qquad
E_0=\overline{C(H)},\]
with \(\mathcal M_\delta:H\to\mathscr B\) compact. Then \(X\in E_0\) a.s., with a centered Radon Gaussian law of full support on \(E_0\), and
\[H_{\mathrm{CM}}=C(H_{\mathrm{seen}}),\qquad
\|Ch\|_{\mathrm{CM}}=\|P_{\mathrm{seen}}h\|_H,\qquad
\ker C=H_{\mathrm{seen}}^\perp.\]
This support triple is an abstract Wiener realization including the measurable-norm condition.

**Proof ingredients.** Countable norming family and Borel generation; finite Gaussian regression
\(X_j=\mathbb E[X\mid\mathcal G_j]=\sum_{l\le j}W(e_l)Ce_l\to X\) in \(L^2(\mathscr B)\); minimum raw preimage norm from \(\ker C=H_{\mathrm{seen}}^\perp\); tightness via finite unions of balls and metric compactness; full support via independence of the finite Gaussian head and the orthogonal tail and positivity of finite Gaussian preimage balls despite possible singularity; measurable-norm tail via regression, Bochner Jensen, and Markov uniformly over finite orthonormal families in \(V_j^\perp\).

**Remaining condition / falsified item.** This first-chaos realization uses only \(\ell(X)=W(k_\ell)\) and compact \(C\); it is **proved here**, not imported as an abstract-Wiener assumption from PROOF148 or Banach-Gaussian existence. It does not assert that a positive-cutoff source pointfield belongs to the raw feature image; F194 shows that range inclusion is false. Zero law is explicit and correct.

---

## PROOF171 — L:tube-closed-geometry (`L:tube-closed-geometry`)

**Statement.** If the law of \(X\) is nonzero, put
\[b_\delta=2\mathbb E\|X\|,\qquad A_\delta=\{x\in E_0:\|x\|\le b_\delta\},\qquad
\mathcal T_r=A_\delta+\mathcal M_\delta(\overline B_H(r)).\]
Every \(\mathcal T_r\) is closed. The extended distance
\[d_\delta(x)=\inf\{r\ge0:x\in\mathcal T_r\}\]
obeys
\[\{d_\delta\le r\}=\mathcal T_r,\qquad
\mathbb P(d_\delta(X)>r)\le e^{-r^2/(2\delta)},\qquad r\ge0,\]
so \(d_\delta\) is lower semicontinuous and finite almost surely.

**Proof ingredients.** A compact operator from a separable Hilbert space sends closed balls to compact closed sets by weak subsequence convergence; closed base ball plus compact image is closed; least radius attained by weak limit plus compactness; Markov \(\mu(A_\delta)\ge1/2\); exact Cameron unit-ball identity
\(\mathcal K=C(\overline B_H(1))=\sqrt\delta\,\mathcal M_\delta(\overline B_H(1))\), applied after importing Borell/FH11.6; the half action is \(\exp(-r^2/(2\delta))\).

**Remaining condition / falsified item.** Noncompact \(M\) would break closedness of the enlargements. The outermost-measurability warning of FH footnote 3 is resolved by these **actual closed Borel enlargements**; it is not waived. No unverified measurable selection is used; least radius is attained in the closed compact-image geometry.

---

## PROOF172 — P:tube-rayleigh-transfer (`P:tube-rayleigh-transfer`)

**Statement.** Let \(F:E_0\to\mathbb R\) be Borel and \(G:[0,\infty)\to\mathbb R\) Borel nondecreasing. If
\[F(x)\le G(r)\quad\text{for all }x\in\mathcal T_r,\ r\ge0,\]
then
\[\mathbb E\,e^{F(X)/\delta}\le\int_0^\infty\frac r\delta\exp\!\Bigl(\frac{G(r)-r^2/2}{\delta}\Bigr)\mathrm dr.\]
For the zero law \(E_0=\{0\},C=\mathcal M_\delta=0\), the same conclusion holds when \(F(0)\le G(0)\).

**Proof ingredients.** Rayleigh dominator with density \((r/\delta)e^{-r^2/(2\delta)}\) and survival \(e^{-r^2/(2\delta)}\); upper-level comparison covers jumps, open/closed levels; the closed endpoint \(c>0\) is passed by \(s\uparrow c\); least-radius attainment gives \(F(x)\le G(d_\delta(X))\); the null event \(\{d_\delta(X)=\infty\}\) is defined with value one and does not change the expectation; zero law uses \(F(0)\le G(0)\le G(r)\).

**Remaining condition / falsified item.** This is a scalar Rayleigh stochastic dominator, not a raw-Hilbert Gaussian norm and not a density on the infinite-dimensional space. \(G(0)\)/zero law \(F(0)>0\) is allowed; jumps are included.

---

## PROOF173 — P:tube-actual-law (`P:tube-actual-law`)

**Statement.** With \(H=H_I\),
\[(\mathcal M_\delta\Phi)_m(u)=\int_0^{\min(u,\ell_m)}S_E(-v)\mathcal T_R\Phi(s_m+\delta v)S_E(v)\mathrm dv,\]
\[\mathbb E[X_\delta W(\Phi)]=\sqrt\delta\,\mathcal M_\delta\Phi,\qquad
C_\delta\Phi=\mathbb E[X_\delta W(\Phi)],\qquad E_{0,\delta}=\overline{C_\delta(H_I)}\subset\mathscr B_\delta,\]
\(X_\delta=(X_m)\) satisfies the Gaussian hypotheses; \(\mathcal M_\delta\) is compact at each fixed radius/parameter; and at \(R=R_\delta\)
\[b_\delta=2\mathbb E\|X_\delta\|_{\delta,p}\le C_{Q,B,p}\delta^{(1-a)/2-d/Q}\to0.\]

**Proof ingredients.** Actual \(E\) mean field \(\mathcal T_R\) compact into \(L^{r_t}(I;\mathcal K(E))\) at fixed \(R\) by F016; compact conjugation and affine pullback, \(1-1/r_t>\theta\); scale
\(g_\delta\delta^{a/2}=\sqrt\delta\); every stopped row's slow pullback lies in \(H_I\); PROOF170 applies to the exact law on its support; expected-norm anchor PROOF160 at \(R=R_\delta\).

**Remaining condition / falsified item.** \(\mathcal M_\delta\) is compact only at each fixed \(R,\delta\): **no \(R\)-uniform compactness**. The input law is the unprojected given \(W\) on \(H_I\); time blocks remain correlated, and the action is the single global \(H_I\) cost, not a per-fast-direction cost. The compactness/convergence holds for fixed \(B,Q,p\) before \(\delta\to0\).

---

## PROOF174 — L:tube-actual-endpoint (`L:tube-actual-endpoint`)

**Statement.** For every tuple \(x\in\mathscr B_\delta\),
\[P_m(x_m)=S_E(\ell_m)U_{x_m}(\ell_m,0),\qquad
\mathcal P_\delta(x)=P_N(x_N)\cdots P_0(x_0),\qquad
F_\delta(x)=2\delta\log\max(1,\|\mathcal P_\delta(x)\|).\]
\(F_\delta\) is finite and continuous on all tuples. For the actual input,
\[\mathcal P_\delta(X_\delta)=P_{\delta,E}^R(L_\delta,0),\qquad
e^{F_\delta(X_\delta)/\delta}=\|P_{\delta,E}^R(L_\delta,0)\|^2\]
almost surely, for each fixed admissible \(\delta,R,B\).

**Proof ingredients.** Generic Young evolution is globally defined and locally Lipschitz; finite products and free factors preserve continuity; the compact-product baseline PROOF165 gives
\(\|\mathcal P_\delta(x)\|\ge\|S_E(\sum_m\ell_m)\|\ge1\), so the log-max equals the norm on the actual input; PROOF124/raw-block restart applies on the fixed extended horizon \((N+1)B\), then source-to-raw at fixed \(\delta\), terminal remainder \(\tau\); full \(F\) drivers and groups intertwine through \(i:E\to F\), and restriction gives the \(E\) identity.

**Remaining condition / falsified item.** The restart is from **one actual source** at fixed \(\delta,N\) and extended horizon, then the source→raw limit; no mask/free-group commutation and no block-independence are asserted. The compact-product baseline removes the max; it is used at zero noise too. The identity is a fixed-parameter almost-sure statement, not a simultaneous event over all \(\delta,R\).

---

## PROOF175 — P:tube-coarse-envelope (`P:tube-coarse-envelope`)

**Statement.** On \(E_{0,\delta}\), let \(A_\delta\) be the closed ball of radius \(b_\delta\), and
\[G_\delta(r)=\sup_{\substack{a\in A_\delta\\ \|\Phi\|_{H_I}\le r}}F_\delta(a+\mathcal M_\delta\Phi).\]
Then \(G_\delta\) is finite, nondecreasing, and Borel; there is \(C_{\mathrm{env}}<\infty\), independent of \(\delta\) and \(R\ge1\), such that
\[G_\delta(r)\le C_{\mathrm{env}}(1+b_\delta^\nu+r^\nu),\qquad
\mathbb E\|P_{\delta,E}^R(L_\delta,0)\|^2\le\int_0^\infty\frac r\delta e^{(G_\delta(r)-r^2/2)/\delta}\mathrm dr.\]
Here \(\nu=1/\theta\), with primitive exponents \(r_t,p\) in the package \(r_t>2>\nu\), \(p\ge\nu\).

**Proof ingredients.** Primitive bound
\(\delta\sum_m h_m^{r_t}\le(C_{\mathrm{pr}}C_{\mathrm{mean}})^{r_t}\|\Phi\|_{H_I}^{r_t}\);
generic Banach Young bound
\(\log\|U_d(u,0)\|\le c_Y(1+\|d\|^\nu)\);
the two exact weighted power means at exponents \(p/\nu\ge1\), \(r_t/\nu>1\), using \(\delta n\le2/B\); the supremum is finite without attainment; \(F_\delta\) is already \(2\delta\log\|P\|\), so no factor-\(2\) loss enters.

**Remaining condition / falsified item.** The coarse envelope is by construction a controlled sub-Gaussian tube upper bound for the **operator endpoint norm**, and it is finite for every admissible \(\delta\), not only where \(b_\delta\) is small. The supremum \(G_\delta\) is not asserted to attain; \(F_\delta\) already contains the factor \(2\delta\log\|P\|\), so no extra factor-two loss is added.

---

## PROOF176 — L:tube-rayleigh-tail (`L:tube-rayleigh-tail`)

**Statement.** Suppose \(G\) is Borel and \(G(r)\le A_0+Cr^\nu\), \(C\ge0\), \(1<\nu<2\). If \(M>0\) and \(4C\le M^{2-\nu}\), then
\[\int_M^\infty\frac r\delta e^{(G(r)-r^2/2)/\delta}\mathrm dr\le4e^{(A_0-M^2/4)/\delta}.\]
In particular the operator-moment bound of PROOF175 is finite at fixed parameters.

**Proof ingredients.** For \(r\ge M\),
\(Cr^\nu-r^2/2\le-M^2/8-r^2/8\) from \(r^{2-\nu}\ge M^{2-\nu}\ge4C\); analytic derivative
\(-\frac{\mathrm d}{\mathrm dr}[4e^{-r^2/(8\delta)}]=(r/\delta)e^{-r^2/(8\delta)}\) gives front factor \(4e^{-M^2/(8\delta)}\); combine with \(A_0\). On \([0,M]\), \(G(r)\le A_0+CM^\nu\) makes the integral finite.

**Remaining condition / falsified item.** The front factor is \(4\), from the exact half-cut \(M^2/4\) in the exponential and the \(e^{-r^2/8}\) integration, not a factor-\(2\) loss. The guard \(C\le M^{2-\nu}/4\) is exact; finite at fixed parameters, not a sharp large-deviation rate.

---

## PROOF177 — L:tube-half-action (`L:tube-half-action`)

**Statement.** For a finite \(J:H\to\mathbb R\) bounded above on every raw ball, let
\[g_J(r)=\sup_{\|h\|\le r}J(h).\]
In the extended reals,
\[\sup_{r\ge0}\bigl(g_J(r)-r^2/2\bigr)=\sup_{h\in H}\bigl(J(h)-\|h\|_H^2/2\bigr).\]

**Proof ingredients.** Lower inequality by \(r=\|h\|\); upper inequality by
\(J(h)-r^2/2\le J(h)-\|h\|_H^2/2\le\sup_h[J(h)-\|h\|_H^2/2]\) for \(\|h\|\le r\); no subtraction of infinities because each ball has finite supremum.

**Remaining condition / falsified item.** The identity retains exactly **one** global \(\|h\|_H^2/2\), not a sum over fast block actions. The coarse envelope is explicitly **not** the sharp spectral/product envelope and **not** an original-point upper bound.

---

## APPLICATION-GAUSSIAN-TUBES-UPPER

**Typed chain (all inputs actual, on \(E\), fixed \(B,Q,p\)).**

(1) **Full raw variance / compact Cameron mean** (F016, F005, F012/F013). The actual compact time–space mean
\[T:H_I\to L^{r_t}(I;\mathcal K(F)),\qquad T\Phi(s)=T_{\mathrm{sp}}(\mathcal U\Phi(s)),\]
has compact \(F\)-values and, compressed to \(E\), gives the actual field
\[\mathcal T_R\Phi=i^*T\Phi\,i\in L^{r_t}(I;\mathcal K(E)).\]
The raw block isometry \(T_{\delta,m}\) and the mean \(h_\Phi\) are those of F016/F009.

(2) **Uniform \(E\) regulation** (PROOF151–155). On \(E\),
\[P_{\mathrm{ret}}=\pi_J\otimes P_K,\qquad Q_{J,K}=I-P_{\mathrm{ret}},\qquad
P_{\mathrm{full}}=i_IP_{\mathrm{ret}}i_I^*,\qquad
Q_{\mathrm{full}}=I-P_{\mathrm{full}},\]
give the orthogonal head/residual decomposition and the completed Cameron covariance
\[(Lh)_m(u)=\sqrt\delta\int_0^{\min(u,\ell_m)}S_E(-v)\mathcal T_R(Q_{J,K}i_I^*h)(s_m+\delta v)S_E(v)\mathrm dv,\]
with the weighted-norm bound
\[\|Lh\|_{\delta,p}\le\sqrt\delta\,C_{B,E}(2/B)^{1/p-1/r}[M_0\varepsilon_J+M_fc_tK^{-\beta}]\|h\|_{H_W}.\]
All spatial constants are uniform in \(R\ge1\); \(P_{\mathrm{full}}\) and \(Q_{\mathrm{full}}\) fields are independent, residual blocks may be correlated, the head may have infinite rank, and \(C_{B,E}\le18B^{3-1/r}\).

(3) **Radius-explicit first-driver bounds** (PROOF156–160). The actual \(E\) driver produced by \(Y_m\) obeys
\[\|M_R(W)(\cdot)\|_{L^v(C^\theta)}\le C_{Q,B}\sqrt v\,R^{d/Q},\qquad
b_\delta=2\mathbb E\|X_\delta\|_{\delta,p}\le C_{Q,B,p}\delta^{(1-a)/2-d/Q}\]
at fixed \(B,Q,p\), then \(\delta\to0\) with \(R=R_\delta=\delta^{-1}+2\). This is the expected-norm anchor, distinct from the fixed-\(R\) compactness of \(\mathcal M_\delta\).

(4) **Signed rough physical / symplectic baseline** (PROOF161–169). Signed controls have closed form on \(H^1\), \(D(H_V)\hookrightarrow H^{3/2}\), no \(H^2\) domain, and the full \(F\)-bound with both constant columns and \((1+t)^3\). The actual block-mean primitive is
\[H_{m,E}(\Phi)(u)=\int_0^{\min(u,\ell_m)}S_E(-v)\mathcal T_E\Phi(s_m+\delta v)S_E(v)\mathrm dv,\]
with **unscaled** covariance \(\delta^{a/2}H\) and the compact-product norm baseline
\[\|S_E(\ell_m)U_{H_{m,E}(\Phi)}(\ell_m,0)\|\ge1.\]
This supplies the exact mean input into the tube geometry without a per-fast-direction cost.

(5) **Actual Gaussian realization** (PROOF170, made concrete by PROOF173). For the actual law \(X_\delta\) on \(\mathscr B_\delta\),
\[C_\delta\Phi=\sqrt\delta\,\mathcal M_\delta\Phi,\qquad
E_{0,\delta}=\overline{C_\delta(H_I)},\qquad
H_{\mathrm{CM}}=C_\delta(H_{\mathrm{seen}})\ \text{with minimum raw preimage norm}.\]
PROOF170 proves, on the actual first-chaos coordinates, the Radon law, full support on \(E_{0,\delta}\), abstract-Wiener measurable-norm condition, and the zero law; this is not imported from PROOF148.

(6) **Closed attained Borel tubes** (PROOF171). For the actual compact \(\mathcal M_\delta/\sqrt\delta\sim\) compact \(C\)-image,
\[b_\delta=2\mathbb E\|X_\delta\|_{\delta,p},\qquad A_\delta=\overline B_{E_{0,\delta}}(b_\delta),\qquad
\mathcal T_r=A_\delta+\mathcal M_\delta(\overline B_{H_I}(r)),\]
is closed and Borel; the attained distance \(d_\delta\) has
\[\{d_\delta\le r\}=\mathcal T_r,\qquad
\mathbb P(d_\delta(X_\delta)>r)\le e^{-r^2/(2\delta)}.\]
The exact genuine Cameron unit-ball identity holds **before** Borell/FH11.6:
\(\mathcal K=\sqrt\delta\,\mathcal M_\delta(\overline B_{H_I}(1))\), so the Gaussian half action is \(e^{-r^2/(2\delta)}\).

(7) **Actual operator Rayleigh integral** (PROOF172–177). With
\(F_\delta(x)=2\delta\log\max(1,\|\mathcal P_\delta(x)\|)\) and the exact restart identity PROOF174, the operator endpoint satisfies
\[\mathbb E\|P_{\delta,E}^R(L_\delta,0)\|^2
=\mathbb E\,e^{F_\delta(X_\delta)/\delta}
\le\int_0^\infty\frac r\delta\exp\!\Bigl(\frac{G_\delta(r)-r^2/2}{\delta}\Bigr)\mathrm dr,\]
where
\[G_\delta(r)=\sup_{a\in A_\delta,\|\Phi\|_{H_I}\le r}F_\delta(a+\mathcal M_\delta\Phi)
\le C_{\mathrm{env}}(1+b_\delta^\nu+r^\nu),\]
\(\nu=1/\theta\), \(r_t>2>\nu\), \(p\ge\nu\), and the radial integral is finite by PROOF176 for every fixed admissible \(\delta\). PROOF177 retains the **one** global \(H_I\) half-action \(-\|h\|^2/2\) and explicitly flags that the coarse envelope is not sharp. The chain uses fixed finite \(R\)-compactness for \(M_\delta\) and the numerical \(R_\delta\) only for the expected-norm anchor; \(B,Q,p\) are fixed before \(\delta\).

**What the application does and does not state.** It proves a finite Gaussian-tube upper bound for the **operator-norm endpoint** \(\|P_{\delta,E}^R(L_\delta,0)\|^2\) of the actual symplectic \(E\) flow, with one global half-action, under the actual first-chaos law on the unprojected \(H_I\). It does **not** derive the canonical point second moment \(u^2(t,x)\), does **not** bound the two \(F\)-constant columns by the \(E\) tube, does **not** replace the coarse envelope by the sharp spectral/product envelope, and does **not** identify or accept \(C_2\), the cold/MAIN whole goal, or any hidden 051/S2/204 premise.

---

## GLOBAL-UNPROVED-CONDITIONS

1. **Cutoff source measurability (F194, binding).** Positive finite-cutoff point features are **not** in the closed raw feature image \(\overline{\Phi(H_W)}\), so the source pointfields \(Y_\rho(t,x)\) have a nontrivial auxiliary \(J\)-component: the claimed closed-range/\(W\)-only assertion in earlier records is false. Consequently PROOF166/169/173 must be read in the fixed \(W+\) one-augmenting-\(J\) extension. This does not refute the fixed extension, the isometry, the retention identity, the point/test identity, or the joint covariance; and it does by itself prove that every nonlinear/canonical limit retains a \(J\)-component. The \(W\)-measurability of any nonlinear source limit remains an **open separate condition**, to be discharged only by explicit raw-test residual convergence in the relevant limit, not by the false range inclusion.

2. **The Gaussian-tube upper is an operator-norm endpoint bound, not the original point second moment.** The chain PROOF170–177 terminates at
\(\mathbb E\|P_{\delta,E}^R(L_\delta,0)\|^2\le\int_0^\infty(r/\delta)\exp((G_\delta(r)-r^2/2)/\delta)\,\mathrm dr\), with the coarse envelope \(G_\delta\). Transfer of an \(E\)-norm/operator bound to the actual pointwise \(u(t,x)\) second moment, and matching it to a variational formula, is **not supplied** in F017–F022. No \(C_2\), point-moment, cold, or MAIN/whole-goal acceptance follows.

3. **Constant \(F\)-columns and mask/point transfer.** PROOF151–155 (uniform Cameron regulation) and PROOF156–160 (radius anchor) are \(E\)-only statements; the two constant data columns lie outside \(E\). The Gaussian-tube application on \(E\) does not bound these columns. Any use of the \(E\) tube to bound the canonical data \((1,0)\) requires a separate \(F\)-column/point-transfer argument not present in these sections. PROOF169 keeps the full \(F\) columns only up to the \(E\)-compression; PROOF164 provides the full \(F\)-bound for signed static controls, but the stochastic \(F\)-column uniform bound is not derived here.

4. **Input finiteness \(R_{\mathrm{sp}}\).** The constants \(A_s=C_s^2\sqrt{R_{\mathrm{sp}}}\), \(M_0\), and the spatial covariance-tail bounds use \(R_{\mathrm{sp}}<\infty\) from F015. The chain \(R_{\mathrm{sp}}\leftarrow\)(F015 four-linear extension)\(\leftarrow\)(existing own spectral bounds/independent 051) is an **incoming conditional input**, not derived in F017–F022. It must not be reversed: \(R_{\mathrm{sp}}\), the spatial-energy finiteness, and any independent upper bound cannot be circularly financed by the point bound being proved here.

5. **No \(R\)-uniform compactness.** The actual mean \(\mathcal T_R\) and \(\mathcal M_\delta\) are compact only at each fixed \(R\); the radius \(R_\delta=\delta^{-1}+2\) enters only the expected-norm anchor. No uniform-in-\(R\) compactness, no \(F\)-column uniform bound, and no uniform-radius spectral tail can be assumed.

6. **Orthogonal decomposition hypotheses.** Heat filtering alone is not an orthogonal projection; \(P_K\) must be the actual closed-frequency-ball projection on the covariance Fourier image. The retained head may have infinite rank; only the actual residual blocks are independent, while blocks remain correlated; the scalar compact time-tail tensored with infinite identity is not compact. Any later conditioning/integration over the head must preserve these actual hypotheses.

7. **Signed-control limitations.** The signed multiplier \(V\) is a supported \(H^{-1/2}\) distribution with a bounded Hermitian form, represented by a closed \(H^1\) form via Teschl. No \(H^2\) operator domain, no point trace, no positive ground/gap, and no \(D(A^{3/4})=H^{3/2}\) interpolation is available by default; \(D(H_V)\hookrightarrow H^{3/2}\) is obtained only from the distributional equation \(H_V=\Delta+V\). If a sharper \(K\le1+\|L\|\) is used later, it uses \(K=\max(1,\|L\|)\), not an arbitrary larger shift.

8. **Symplectic vs compact baseline.** Compactness of \(U_X-I\) does not imply symplecticity: the lower bound \(\|S+{\rm compact}\|\ge\|S\|\) holds for arbitrary compact-driver tuples; actual \(J_E\)-conservation (PROOF168) uses the closed real \(J\)-skew constraint, not comp compactness alone. Invertibility uses Young Neumann pieces, not conservation in infinite dimension. The raw block-mean factor is \(\delta^{a/2}\), not \(\sqrt\delta\); the \(\sqrt\delta\) appears only after multiplying by \(g_\delta\).

9. **Rayleigh/tube pitfalls.** The final half action is **one** global \(\|h\|_{H_I}^2/2\), not a sum over fast directions. The coarse envelope introduces no factor-\(2\) loss because \(F_\delta\) is already \(2\delta\log\|P\|\). The radial tail front factor \(4\) comes from the exact \(e^{-M^2/4}\) half-cut with \(M^{2-\nu}\ge4C\), \(1<\nu<2\), not from a factor-two normalization error. The Rayleigh dominator must handle jumps in \(G\), the attained zero radius, and the zero law \(F(0)>0\); the closed-tube attainement resolves the FH measurable-selection footnote without waiving it.

10. **No extra OWN IDs / no replacement-paper proof.** The focused work provides only the exact \(E\)-covariance, \(E\)-anchor, \(E\)-tube, signed static, and symplectic-chain results above. All remaining gaps become explicit **conditions**, not silently inferred facts: original point-moment transfer, \(F\)-column uniform control, sharp/variational envelope, and identification/finiteness of \(C_2\) remain outside the supplied packet and are not accepted.