## PROOF094

**Owner: F007 `L:source-finite-comparison`. Linear finite Gaussian image comparison.**

**Setting.** Let \(V\) be a real Banach space, \(v_1,\dots,v_N\in V\) fixed vectors, and \(\xi=(\xi_1,\dots,\xi_N)\) a centered Gaussian vector with covariance matrix bounded by \(CI\) in the positive-semidefinite order, \(C\ge0\). Let \(g=(g_1,\dots,g_N)\) be independent standard real Gaussians. Fix \(p\ge1\).

**Statement.**
\[
\left(\mathbb E\Big\|\sum_{j=1}^N \xi_j v_j\Big\|_V^p\right)^{1/p}
\ \le\ \sqrt C\,
\left(\mathbb E\Big\|\sum_{j=1}^N g_j v_j\Big\|_V^p\right)^{1/p}.
\tag{094.i}
\]

**Derivation.** Define \(\varphi(x)=\|\sum_{j=1}^N x_j v_j\|_V^p\). This is continuous and convex (convex because a norm is convex and \(p\ge1\)); the finite bound \(\mathbb E\varphi(g)<\infty\) follows from Gaussian moments of the finite linear image. On an auxiliary product space take \(Z\) Gaussian, independent of \(\xi\), with covariance \(CI-\operatorname{Cov}(\xi)\) (nonnegative by hypothesis; \(Z=0\) if \(C=0\)). Conditional Jensen w.r.t. \(\xi\) gives
\[
\mathbb E\,\varphi(\xi)\le\mathbb E\,\varphi(\xi+Z),
\]
and \(\xi+Z\) has the law of \(\sqrt C\,g\). The \(C=0\) case gives \(0\le0\).

**Pinpoint.** This is a *linear* Gaussian covariance comparison only. It carries no statement about nonlinear functions of a wave solution, about source-filter commutation, or about any coupled nonlinear solution. It is applied below only to the deterministic coefficient paths \(A_j(\cdot)\) in the Banach path space \(\mathscr B_\theta=C^\theta([0,T];\mathcal B(E))\). Independence of the \(\xi_j\) is **not** assumed. The auxiliary vector \(Z\) is a comparison device and changes neither the actual coupling of \(\xi\) nor any nonlinear wave evolution.

---

## PROOF095

**Owner: F007 `P:source-gaussian-transfer`. Gaussian transfer and stability in the path norm.**

**Setting.** Fixed \(R,T,\zeta_R,E\) and the parameters in `E:driver-parameters`; \(\mathscr B_\theta=C^\theta([0,T];\mathcal B(E))\). Fixed raw basis \(f_j\) with actual raw coefficient paths \(A_j(\cdot)\), and \(M_N=\sum_{j\le N}W(f_j)A_j\to M_R\) in every finite \(L^p(\mathscr B_\theta)\) (the raw head from 091/092). Let \(Y\) be a centered Gaussian linear noise on smooth compact positive-time tests, on a common coupled space, with
\[
\operatorname{Var}Y(F)\le C\|F\|_{H_W}^2 .
\tag{095.i}
\]
\(Y\) is **not** assumed independent in its coordinates.

**Statement.**
1. \(Y\) extends to \(H_W\) as a bounded linear map into \(L^2\).
2. \(M_{Y,N}=\sum_{j\le N}Y(f_j)A_j\) converges in every finite \(L^p(\mathscr B_\theta)\) to a centered Gaussian path \(M_Y\) with compact values at all times on one path event, and
\[
\|M_Y-M_{Y,N}\|_{L^p\mathscr B_\theta}\le\sqrt C\,\|M_R-M_N\|_{L^p\mathscr B_\theta},
\tag{095.ii}
\]
\[
\|M_Y\|_{L^p\mathscr B_\theta}\le\sqrt C\,\|M_R\|_{L^p\mathscr B_\theta}.
\tag{095.iii}
\]
3. For real Schwartz \(z,w\), \(t\in[0,T]\),
\[
\langle M_Y(t)z,w\rangle_E=Y(h_{R,t;z,w})\quad\text{in }L^2,
\tag{095.iv}
\]
with \(h_{R,t;z,w}\) the literal raw test class \(\zeta_R1_{(0,t)}v_zG_w\) with the adjoint in `E:variance-dual-wave`.
4. The path is basis-independent up to indistinguishability, linear in jointly Gaussian noise families, and complexifies sesquilinearly.
5. **Stability.** If \((W,Y_n)\) are jointly centered Gaussian, \(Y_n\) and \(D_n=W-Y_n\) satisfy uniform bounds of the form (095.i), and \(\operatorname{Var}D_n(F)\to0\) on every smooth compact test \(F\), then \(M_{Y_n}\to M_R\) in every finite \(L^p(\mathscr B_\theta)\), at arbitrary relative rates.

**Derivation.** (095.i) annihilates raw-null tests and extends \(Y\). For each finite orthonormal family the covariance of \((Y(f_j))\) is \(\le CI\) by testing real linear combinations; independence is not used. Apply PROOF094 with \(v_j=A_j\in\mathscr B_\theta\) and to finite tails \(v_j=A_j\), \(N<j\le M\). The raw convergence makes \(M_{Y,N}\) Cauchy. The limit lies in the separable closed span of the countably many \(A_j\); a subsequence/tail construction gives a strongly measurable limit on the actual space of \(Y\). Passing to limits gives (095.ii),(095.iii). (095.iv) uses \(\langle A_j(t)z,w\rangle_E=\langle h_{R,t;z,w},f_j\rangle_{H_W}\) and \(Y(P_Nh)\to Y(h)\). For stability, the finite head covariance matrix satisfies \(s_N(n)=\sum_{j\le N}\operatorname{Var}D_n(f_j)\to0\), so PROOF094 gives \(\|M_{D_n,N}\|_{L^p}\le\sqrt{s_N(n)}\|M_N\|_{L^p}\); send \(N\) large then \(n\) large.

**Pinpoint.** The transfer **depends on the actual raw coefficient paths \(A_j\)** and the already-proved raw path tail \(M_N\to M_R\) (uniform-in-head raw PATHTAIL from 091/092). It is not a "nonlinear wave comparison"; no commutation of a filter with a mask or wave group is used; joint Gaussianity is a hypothesis only in the stability clause. Mere equality in law is not used — the raw-row identity is an actual \(L^2\) equality on the coupled space.

---

## PROOF096

**Owner: F007 `L:source-spatial-heat`. Spatial Hilbert space and heat contraction.**

**Setting.** \(H_\Gamma\) is the real test-null completion for
\[
B_\Gamma(f,g)=\int_{\R^d}\Gamma(\ud y)\int_{\R^d}f(x)g(x-y)\ud x
=(2\pi)^d\int_{\R^d}\widehat f(\xi)\overline{\widehat g(\xi)}\,\mu(\ud\xi),
\tag{096.i}
\]
with the unitary Fourier convention \(c_d=(2\pi)^{-d/2}\). Define
\[
p_\varepsilon(x)=(2\pi\varepsilon)^{-d/2}e^{-|x|^2/(2\varepsilon)},\quad
C_\varepsilon f=p_\varepsilon*f.
\tag{096.ii}
\]

**Statement.** \(H_\Gamma\) is separable and contains every Schwartz test. On \(H_\Gamma\), \(C_\varepsilon\) is a positive self-adjoint contraction, \(I-C_\varepsilon\) is a contraction, and \(C_\varepsilon\to I\) strongly as \(\varepsilon\downarrow0\).

**Derivation.** The spectral normalization is the spatial computation in `P:masked-noise-completion`; reality of \(B_\Gamma(f,g)\) for real tests uses evenness of \(\mu\). Compact-support bound
\[
|B_\Gamma(f,g)|\le|K|\,\Gamma(K-K)\,\|f\|_\infty\|g\|_\infty
\tag{096.iii}
\]
gives separability by countable smooth approximation. Schwartz cutoffs converge in Schwartz seminorms and against tempered \(\Gamma\), so Schwartz tests enter the same completion. The Fourier multiplier of \(C_\varepsilon\) is \(m_\varepsilon(\xi)=e^{-\varepsilon|\xi|^2/2}\). On dense Schwartz tests the displayed norm gives positivity, self-adjointness, and both contractions \(0\le m_\varepsilon\le1\), \(0\le 1-m_\varepsilon\le1\). Dominated convergence gives strong convergence on the dense set; uniform boundedness extends to the completion.

**Pinpoint.** This is a spatial realization statement; it defines no physical mask on a noise quotient. The unitary Fourier constants \(c_d=(2\pi)^{-d/2}\) are carried exactly through (096.i). No interchange of two infinite measures is made in the oscillatory expression: (096.i) is obtained by applying the spectral convention `E:masked-spectral-convention` to a single Schwartz test \(h(z)=\int f(y+z)g(y)\ud y\), then reflecting using evenness of \(\mu\).

---

## PROOF097

**Owner: F007 `L:source-retaining-isometry`. Feature isometry and the retaining extension.**

**Setting.** \(\nu_a(\ud\lambda)=\lambda^{a-1}\ud\lambda/\Gamma_E(a)\) (\(a=\alpha_0\)), and
\[
\mathcal G=L^2\big((0,\infty)_\lambda\times\R_r,\ \nu_a(\ud\lambda)\ud r;\ H_\Gamma\big),
\tag{097.i}
\]
a real separable Hilbert space.

**Statement.** On finite smooth temporal-spatial tensors define
\[
\Phi F(\lambda,r)=\sqrt{2\lambda}
\int_{\substack{t>0\\ t\ge r}}e^{-\lambda(t-r)}F(t,\cdot)\ud t .
\tag{097.ii}
\]
Then \(\Phi\) extends to an isometry \(\Phi:H_W\to\mathcal G\) with **closed range**; (097.ii) represents smooth compact tests a.e. On a product extension retaining the original \(W\), with \(P\) the orthogonal projection onto \(\Phi H_W\) and \(J\) an independent isonormal on \((\Phi H_W)^\perp\), define
\[
\mathcal I(g)=W(\Phi^{-1}Pg)+J((I-P)g).
\tag{097.iii}
\]
Then \(\mathcal I\) is isonormal on \(\mathcal G\), and
\[
\mathcal I(\Phi h)=W(h)\quad\text{in }L^2\quad(h\in H_W).
\tag{097.iv}
\]

**Derivation.** The identity
\[
\int_{-\infty}^{\min(t,u)}2\lambda e^{-\lambda(t+u-2r)}\ud r=e^{-\lambda|t-u|}
\tag{097.v}
\]
and the raw Laplace formula of `L:masked-time-completion` give \(\|\Phi F\|_\mathcal G^2=\|F\|_{H_W}^2\) for finite tensors. All signed exchanges are absolutely integrable: compact temporal factors give integrals of \(|\tau(t)\sigma(u)||t-u|^{-a}\) (finite since \(a<1\)) times finite spatial inner products; **no oscillatory infinite-measure Fubini** is used. Smooth time partitions on one compact support approximate general spacetime tests uniformly by finite tensors; the local covariance bound `E:driver-test-continuity` proves density in \(H_W\). Hence the isometry extends with closed range. For a general smooth compact \(F\), the approximants converge uniformly in spatial \(H_\Gamma\) norm in time, so their pointwise integrals converge while the isometry gives \(\mathcal G\)-convergence; the a.e. subsequence identifies the two limits. The auxiliary coordinate \(r<0\) is used only in the feature integral — it does **not** assign raw negative-time noise. Orthogonality of \(J\) to \(\Phi H_W\), plus independence, makes (097.iii) isonormal and proves (097.iv).

**Pinpoint — a false strengthening.** A later external check (F194) proved that **positive-cutoff point features \(v_{\rho;t,x}\) are generally NOT in \(\Phi H_W\)**: with nonzero \(\Gamma\), \(t_0>0\), finite \(\Lambda=\eta^{-1}\), \(\epsilon>0\), the vector
\[
q(\lambda,r)=p(\lambda)\frac{\phi'(r)+\lambda\phi(r)}{\sqrt{2\lambda}}\otimes g,\qquad
\int p\,\ud\nu_a=0,\quad \int_{\lambda\le\Lambda}p\,\ud\nu_a=1,\quad g=p_\epsilon(x-\cdot),
\]
is in \(\mathcal G\), satisfies \(\langle\Phi F,q\rangle_\mathcal G=0\) for all smooth compact \(F\) (hence \(q\in(\Phi H_W)^\perp\)), while \(\langle v_{\rho;t_0,x},q\rangle_\mathcal G=\phi(t_0)\|g\|^2>0\). Consequently \(\operatorname{Var}(Y_\rho(t_0,x)\mid\sigma(W))\ge\|(I-P)v\|^2>0\). Thus cutoff point fields may carry a nontrivial auxiliary \(J\)-component; **no "W-only" representation of cutoff sources is implied or available here**. PROOF097 itself needs only the isometry/closed range and exact retention (097.iii)-(097.iv), which remain valid.

---

## PROOF098

**Owner: F007 `P:source-canonical-convergence`. Exact joint source law and convergence.**

**Setting.** \(P_\eta\) multiplies \(\mathcal G\) by \(1_{\{\lambda\le\eta^{-1}\}}\); \(C_\varepsilon\) acts fiberwise on \(H_\Gamma\); they commute. For \(\rho=(\varepsilon,\eta)>0\),
\[
Q_\rho=C_\varepsilon P_\eta,\qquad
Y_\rho(F)=\mathcal I(Q_\rho\Phi F),\qquad
D_\rho(F)=W(F)-Y_\rho(F).
\tag{098.i}
\]
Set
\[
\Gamma_e(x)=(p_e*\Gamma)(x),\qquad
K_\eta(v)=\frac1{\Gamma_E(a)}
\int_0^{\eta^{-1}}e^{-\lambda|v|}\lambda^{a-1}\ud\lambda.
\tag{098.ii}
\]

**Statement.**
1. **Point-field realizations.** With
\[
v_{\rho;t,x}(\lambda,r)
=1_{\{\lambda\le\eta^{-1}\}}\sqrt{2\lambda}
\,e^{-\lambda(t-r)}\,1_{\{r\le t\}}\,p_\varepsilon(x-\cdot),
\tag{098.iii}
\]
\(Y_\rho(t,x)=\mathcal I(v_{\rho;t,x})\) has joint covariance
\[
\operatorname{Cov}(Y_{\varepsilon,\eta}(t,x),Y_{\varepsilon',\eta'}(s,y))
=K_{\max(\eta,\eta')}(t-s)\,\Gamma_{\varepsilon+\varepsilon'}(x-y).
\tag{098.iv}
\]
Mean-square pointfield integration satisfies \(Y_\rho(F)=\) the mean-square integral of \(Y_\rho(\cdot,\cdot)\) against \(F\).
2. **Both dominations.**
\[
\operatorname{Var}Y_\rho(F),\ \operatorname{Var}D_\rho(F)\le\|F\|_{H_W}^2,
\tag{098.v}
\]
and \(\operatorname{Var}D_\rho(F)\to0\) as \(\varepsilon,\eta\downarrow0\) **at arbitrary relative rates** for every \(F\in H_W\).
3. **Operator-path limit.** For every finite \(p\ge1\),
\[
M_R^\rho:=M_{Y_\rho}\to M_R\quad\text{in }L^p(\mathscr B_\theta),\qquad
M_{D_\rho}=M_R-M_R^\rho.
\tag{098.vi}
\]
The source and residual have uniform local Gaussian driver moments and square-exponential norms with constants for fixed \(R,T\) and exponents.

**Derivation of the point/test part (direct).** The heat inner product
\[
B_\Gamma(p_\varepsilon(x-\cdot),p_{\varepsilon'}(y-\cdot))
=\Gamma_{\varepsilon+\varepsilon'}(x-y)
\tag{098.vii}
\]
uses \(\widehat{p_\varepsilon(x-\cdot)}(\xi)=c_d e^{-i\xi\cdot x}e^{-\varepsilon|\xi|^2/2}\) (the two \(c_d\)-factors and \((2\pi)^d\) cancel). Integrating \(r\) over the common \(\lambda\)-range gives \(e^{-\lambda|t-s|}\), giving (098.iv) with the temporal MAX in \(\lambda\)-cutoffs and spatial SUM of heat widths. The point feature has finite \(\mathcal G\)-norm and is norm-continuous in \((t,x)\), so its Bochner integral against a smooth test equals \(Q_\rho\Phi F\), hence \(Y_\rho(F)\). For the residual norm,
\[
\|(I-Q_\rho)g\|^2=\|(I-P_\eta)g\|^2+\|P_\eta(I-C_\varepsilon)g\|^2,
\tag{098.viii}
\]
so \(I-Q_\rho\) is a contraction and (098.v) holds. Strong convergence of \(P_\eta\) and fiberwise \(C_\varepsilon\), plus the bound
\[
\|(I-Q_\rho)g\|\le\|(I-C_\varepsilon)g\|+\|(I-P_\eta)g\|\to0,
\tag{098.ix}
\]
gives the arbitrary-relative-rate residual variance decay. This point/test algebra needs no operator theorem.

**Pinpoint.** The **full operator-path claim (098.vi)** genuinely requires PROOF095 (Gaussian transfer) together with the raw path facts 091/092 (fixed-basis HEAD error after a uniform raw PATHTAIL). It cannot be obtained from the point/test covariance algebra alone. Conversely, the point/test covariance part is direct and does not need an invented operator theorem.

**Failure to flag — independence of the full heat residual.** The disjoint \(\lambda\)-ranges in (098.viii) make *parts* of the residual independent, but **this does NOT give independence of the full heat residual** \(D_\rho\) from the source \(Y_\rho\): the shared \(\lambda\le\eta^{-1}\) band still carries the \(I-C_\varepsilon\) part. No such independence is asserted.

**Failure to flag — cutoff W-only.** The cutoff point features \(v_{\rho;t,x}\) in (098.iii) do **not** necessarily lie in \(\Phi H_W\) (see PROOF097, F194 counterexample). The source fields may genuinely use the auxiliary \(J\). Any public claim that positive-cutoff sources or their operators are functions of \(W\) alone is **false** and must be rejected; the retained interpretation is fixed-\(W\) plus one auxiliary \(J\).

---

## PROOF099

**Owner: F007 `L:source-pointfield-regularity`. Regularity for each fixed cutoff.**

**Setting.** \(\rho>0\) fixed.

**Statement.** The pointfield has a version continuous in time and smooth in space, with every spatial derivative jointly continuous on compact time-space rectangles. Specifically, for each multiindex \(b\),
\[
Z_b(t,x)=\mathcal I(\partial_x^b v_{\rho;t,x}),\qquad
\E|Z_b(t,x)-Z_b(s,y)|^2
\le C_{\rho,b}\,(|t-s|+|x-y|^2),
\tag{099.i}
\]
and the dyadic patching plus Gaussian \(q\)th moments gives a jointly continuous modification.

**Derivation.** The spatial squared norms are the finite heat spectral moments \(\int \xi^{2b}e^{-\varepsilon|\xi|^2}\mu(\ud\xi)\); adjacent-in-\(b\) moments dominate difference quotients. For the increment use \(1-e^{-\lambda h}\le\lambda h\) (finite cut \(\lambda\le\eta^{-1}\)) in time and \(|e^{i\xi\cdot x}-e^{i\xi\cdot y}|\le|\xi||x-y|\) in space via (098.iv) in `E:source-joint-covariance`. On a compact rectangle in \(m=d+1\) dimensions, even Gaussian moment roots are \(\le C\sqrt q\cdot(\text{distance})^{1/2}\) at small distances; the dyadic grid has \(\le C_m2^{nm}\) adjacent edges, whose maximum has \(L^q\) norm \(\le C\sqrt q\,2^{-n(1/2-m/q)}\); choose \(q\) large, \(0<h_0<1/2-m/q\), and the weighted maximum sum converges. Binary refinement gives a continuous extension agreeing with the given variables in \(L^2\). Countably many rectangles and multiindices patch by continuity on countable dense overlaps. The \(\mathcal G\)-valued fundamental theorem along coordinate segments, pushed through bounded \(\mathcal I\), makes the \(Z_b\) actual derivatives; the identity is enforced on rational data first and extended by continuity.

**Pinpoint.** The versions and identities are for **this fixed \(\rho\)**. There is no common path event over uncountably many source parameters, and the proof does not create a uniform event for all cutoffs. The plain \(L^\infty\)/derivative path objects are continuous/smooth only after modification at fixed cutoff; no derivative of the raw noise is taken.

---

## PROOF100

**Owner: F007 `P:source-ordinary-response`. Actual ordinary source response.**

**Setting.** Fixed \(\rho>0\), on the regularity event; \(b_\rho(t,x)=\zeta_R(x)Y_\rho(t,x)\); define the statewise integral
\[
L_\rho(t)z=\int_0^t S(-u)B(b_\rho(u))S(u)z\,\ud u .
\tag{100.i}
\]

**Statement.** \(L_\rho\) is operator-norm Lipschitz in \(t\) on \(E\), and
\[
L_\rho=M_R^\rho\quad\text{for all }t\in[0,T]\text{ on one probability-one set}.
\tag{100.ii}
\]
In particular it has the strongly measurable path version of the Gaussian construction.

**Derivation.** \(b_\rho(u,\cdot)\) is compact smooth space with continuous time in every spatial derivative norm, so \(B(b_\rho(u)):E_r\to E_{r+1}\) bounded, giving statewise gain and Lipschitz operator increments exactly as in `L:driver-gain-localization`; **no norm continuity or operator-norm derivative of \(S(t)\)** is used, only strong continuity of the full free group on finite horizons. The instantaneous Sobolev adjoint identity (from \(S(-u)(0,f)\) and the two Bessel weights) gives, for real Schwartz phases,
\[
\langle S(-u)B(b_\rho(u))S(u)z,w\rangle_E
=\int b_\rho(u,x)[S(u)z]_1(x)G_w(u,x)\ud x .
\tag{100.iii}
\]
Integrating in \(u\) yields the ordinary source-field integral against the raw test \(h_{R,t;z,w}\), identified in `P:source-canonical-convergence` with \(Y_\rho(h_{R,t;z,w})\); the continuous version has the same pathwise \(L^2\) integral as the point-feature integral (Riemann sums converge both pathwise and in \(L^2\)). Approximate the indicator wave test in the raw completion with common compact spatial support and small \(L^2\)-time spatial-sup error. Hence
\[
\langle L_\rho(t)z,w\rangle_E
=Y_\rho(h_{R,t;z,w})
=\langle M_R^\rho(t)z,w\rangle_E\quad\text{in }L^2 .
\tag{100.iv}
\]
Countable dense Schwartz phases and rational times, boundedness, and path continuity extend to all states/times on one probability-one set.

**Pinpoint.** Only continuous time of the source coefficient is required at fixed \(\rho\); the instantaneous identity (100.iii) uses no prior time-smoothness. **No operator-norm continuity of the free group and no Banach-space operator derivative** is invoked. The equality (100.ii) is on the actual coupled space, not merely in law; the set is for fixed \(\rho\).

---

## PROOF101

**Owner: F008 `L:masked-chain-comparison`. Ordered chains and mixed-order comparison.**

**Setting.** Fixed \(\rho=(\epsilon,\eta)\), source \(Y_\rho\); \(m\in C_c^\infty(\R^d)\) real with \(0\le m\le1\). \(X_{\rho,n}^m(t,x)\) is the ordinary ordered displacement integral with coefficient \(mY_\rho\); \(X_{\rho,n}\) the unmasked version; order-zero equals \(1\). Green measures \(G_d(r,\ud w)\) have mass \(r\), support in \(\overline{B_r}\), including the \(d=3\) sphere measure. All pair partitions including self-pairings are kept.

**Statement.**
1. The finite ordered integrals are Bochner \(L^2\) integrals. For \(n,k\ge0\), fixed \(t,x,y\), \(\rho>0\),
\[
0\le \E[X_{\rho,n}^m(t,x)X_{\rho,k}^m(t,y)]
\le \E[X_{\rho,n}(t,x)X_{\rho,k}(t,y)].
\tag{101.i}
\]
Both vanish when \(n+k\) is odd. With \(q_n\) from `L:vertex-crude`,
\[
\|X_{\rho,n}^m(t,x)\|_2\le q_n(t),\qquad
\|X_{\rho,n}(t,x)\|_2\le q_n(t).
\tag{101.ii}
\]

**Derivation.** The time-space chain measure \(\nu_n^{t,x}\) has mass \(t^{2n}/(2n)!\), deduced from the recursion \(f_n(t)=\int_0^t(t-r)f_{n-1}(r)\ud r\). The actual covariance \(C_\rho(s,z;r,w)=K_\eta(s-r)\Gamma_{2\epsilon}(z-w)\) satisfies \(0\le C_\rho\le c_\rho=K_\eta(0)\Gamma_{2\epsilon}(0)<\infty\). Gaussian product moments bound the \(L^2\) norm of each \(n\)-fold product, giving Bochner integrability and stochastic Fubini between two chains. For \(n+k=2l\) the \(D\)-diagram is the nonnegative integral of \(\prod_{\{i,j\}\in D}C_\rho(s_i,z_i;s_j,z_j)\) against \(\nu_n^{t,x}\otimes\nu_k^{t,y}\); the masked integrand acquires the single factor \(\prod_{i=1}^{2l}m(z_i)\in[0,1]\) with **one factor per vertex, independent of chain/partner**, giving (101.i) for all unequal/self/empty/mixed cases. Setting \(k=n,y=x\) and using the unmasked bound gives (101.ii).

**Pinpoint.** This is a comparison of **expected displacement Wick integrals**, never a samplewise order of solutions nor an arbitrary phase-energy covariance order. The \(d=3\) Green-width identification takes Green smoothing to zero first at fixed positive noise widths via weak convergence of positive Green measures, checking square and cross moments to the same diagram sum; no samplewise bound on heat tails is used. Uniformity of \(q_n\) comes from the actual fixed-order foundation (Lemma `L:vertex-crude` and its sum `E:vertex-summability` in module 008), not from an upper 051/C2 finiteness claim.

---

## PROOF102

**Owner: F008 `P:masked-source-moments`. Ordinary solutions and tested moments.**

**Statement.** The sums \(u_\rho^m=\sum_{n\ge0}X_{\rho,n}^m\) and \(u_\rho=\sum_{n\ge0}X_{\rho,n}\) converge absolutely in \(L^2\) and have locally continuous versions that are the unique locally continuous ordinary mild solutions with coefficients \(mY_\rho\) and \(Y_\rho\), respectively, and data \((1,0)\). For every nonnegative \(\phi\in C_c^\infty(\R^d)\),
\[
0\le\E[u_\rho^m(t,x)u_\rho^m(t,y)]
\le\E[u_\rho(t,x)u_\rho(t,y)],
\tag{102.i}
\]
and
\[
\E\Big|\int\phi(x)u_\rho^m(t,x)\ud x\Big|^2
\le\|\phi\|_1^2\,\E|u_\rho(t,0)|^2 .
\tag{102.ii}
\]
The spatial integral is an actual Bochner \(L^2\) integral.

**Derivation.** \(Q_T=\sum_{n\ge0}q_n(T)<\infty\) gives absolute \(L^2\) convergence. Pathwise identification on a compact backward-cone enlargement: on the regularity event the coefficient is bounded by a finite sample \(M\), finite propagation and chain mass \(t^{2n}/(2n)!\) dominate each Picard term, giving uniform convergence and the mild equation with data \((1,0)\); the difference iteration with \(B M^n T^{2n}/(2n)!\) gives uniqueness among continuous solutions. Ordinary Fubini identifies Bochner and pathwise chains, countably many orders, then an a.s. subsequence identifies the limit with the continuous Picard version. Cauchy–Schwarz termwise gives
\[
\sum_{n,k}\E|X_{\rho,n}^{(m)}(t,x)X_{\rho,k}^{(m)}(t,y)|\le Q_t^2,
\tag{102.iii}
\]
so (101.i) passes termwise to (102.i). Stationarity of the **unmasked** source (finite Picard integrals commute with translations) gives \(\E[u_\rho(t,x)u_\rho(t,y)]\le\E|u_\rho(t,0)|^2\); stationarity is not used for the masked solution. \(L^2\)-continuity in \(x\) from source increment continuity and dominated Gaussian moments, plus \(Q_t\) tails, give the \(L^2\)-continuous full sum; absolute Fubini (justified by \(\|\phi\|_1^2 Q_t^2\)) gives the average and (102.ii).

**Pinpoint.** The ordering/moment comparison is for **expectations**, with the single mask factor transferred as in PROOF101. The Picard identification uses compact backward cones for the locally continuous source solution; no strong solution concept or arbitrary samplewise order is asserted. For (102.ii) only the unmasked stationary law is used; no stationary law of the masked solution is claimed.

---

## PROOF103

**Owner: F008 `P:masked-canonical-transfer`. Canonical point-moment limit and conditional transfer.**

**Statement.**
1. **Canonical point-moment limit.** At every fixed \(t\), at arbitrary relative rates of \((\epsilon,\eta)\),
\[
\lim_{\epsilon,\eta\downarrow0}\E|u_\rho(t,0)|^2
=\E|u(t,0)|^2,
\tag{103.i}
\]
where \(u\) is the original canonical Stratonovich solution.
2. **Conditional transfer.** If the masked averages in `E:masked-average-source` converge in \(L^2\) to \(Z_m(t,\phi)\) (arbitrary rates or a specified sequence with both widths tending to zero), then
\[
\E|Z_m(t,\phi)|^2\le\|\phi\|_1^2\,\E|u(t,0)|^2.
\tag{103.ii}
\]

**Derivation.** At fixed orders the common-width source law is the vertexwise law in `L:joint-fixed-order`. Reversing each terminal chain (\(s'_j=t-s_{n+1-j}\), \(z'_j=-z_{n+1-j}\), and the same for the other chain) with even covariances gives the exact initial-chain convention of `P:mixed`; Green smoothing is removed first, then `L:joint-fixed-order` gives the joint limit at arbitrary relative noise-width rates. Thus for fixed \(n,k\),
\[
\E[X_{\rho,n}X_{\rho,k}]\to\E[X_nX_k].
\tag{103.iii}
\]
The double majorant \(q_n(t)q_k(t)\) controls both tails; choose a finite square of orders with exterior double majorant \(<\delta\) and use the finitely many joint limits. `P:mixed` identifies the sum, proving (103.i). The masked transfer uses only the \(L^2\) convergence premise: \(|\, \E|B|^2-\E|A|^2\,|\le\|B-A\|_2(\|B\|_2+\|A\|_2)\).

**Pinpoint.** The masked-transfer (103.ii) has an **explicit and genuinely conditional \(L^2\)-convergence premise for the exact same Bochner average**; uniform \(L^2\) bounds, passage of the unmasked moment (103.i), and presence of the limit object are not sufficient to drop it. It must be **discharged** by PROOF108–PROOF110 (the Young/source flow limit of the tested average at the same mask, horizon, observable), not by law/presence arguments. The canonical point-moment limit (103.i) does **not** assume full source convergence as a premise: it is built from fixed pair–order single-width diagram laws, terminal-to-initial reversal, Green first, then arbitrary-relative noise limits, with a double \(q_nq_k\) tail. A bounded non-convergent average family would satisfy the uniform bounds while failing the premise; the conclusion must not be asserted for such a family.

---

## PROOF104

**Owner: F009 `L:constant-phase-free`. The distributional phase and its free evolution.**

**Setting.** \(F=E\oplus\R^2\), \(\|(e,c_1,c_2)\|_F^2=\|e\|_E^2+c_1^2+c_2^2\); interpretation \((e_1+c_1,e_2+c_2)\); \(e_0=(0,1,0)\); \(i:E\to F\), \(\pi_C:F\to\R^2\).

**Statement.**
1. The distributional interpretation of \(F\) is continuous and **injective**; \(E\) imbeds as the closed proper subspace \(iE\), and the constant coordinates are genuinely outside all Sobolev entries (a nonzero constant cannot be represented by a locally \(L^2\) Fourier function near zero because the test \(\varphi(\xi/\varepsilon)\) kills the \(L^2\)-part while detecting \(\delta_0\)).
2. For every real \(\psi\in C_c^\infty\),
\[
L_\psi(e,c_1,c_2)=\psi e+(c_1\psi,c_2\psi)
\tag{104.i}
\]
is bounded \(F\to E\).
3. The free group on \(F\) is
\[
S_F(t)(e,c_1,c_2)=(S(t)e,\,c_1+t c_2,\,c_2),
\tag{104.ii}
\]
strongly continuous, bounded on finite horizons, with finite propagation for the **total** distributional data — including the local cancellation between the Sobolev part \(e\) and the constants on regions where the total data vanish.

**Derivation.** Injectivity: a local \(L^2\) function \(f\) tested against \(\varphi(\xi/\varepsilon)\), \(\varphi(0)=1\), \(\operatorname{supp}\varphi\subset B_1\), gives \(\|f\|_{L^2(B_\varepsilon)}\varepsilon^{d/2}\|\varphi\|_2\to0\), while \(\delta_0\) gives \(1\). Continuity of the Sobolev part into distributions: local Sobolev duality and the two test integrals, uniformly on bounded families of compact tests. \(L_\psi\) boundedness: the Peetre inequality \(\langle\xi\rangle^\sigma\langle\eta\rangle^{-\sigma}\le2^{|\sigma|/2}\langle\xi-\eta\rangle^{|\sigma|}\) and \(L^1*L^2\) give boundedness at \(\sigma=\pm1/2\); the constant columns are in \(E\). The finite block of (104.ii) and the strong finite-horizon bound on \(S(t)\) give the group properties. The matrix of compactly supported distributions
\[
\begin{pmatrix}\partial_t G_d & G_d\\ \Delta G_d & \partial_t G_d\end{pmatrix}
\tag{104.iii}
\]
has convolution multipliers \((\cos(t|\xi|),\, \sin(t|\xi|)/|\xi|,\, -|\xi|\sin(t|\xi|),\,\cos(t|\xi|))\) agreeing with \(S(t)\) on Schwartz phases; convolution by a compact distribution is continuous on tempered distributions; masses \(1,t,0,1\) give the constant block. Each entry is supported in \(B_{|t|}\), so total-data vanishing on an enlarged region implies vanishing of the evolved total distribution on the smaller cone, **allowing cancellation between \(e\) and constants**.

**Pinpoint.** This derivation shows \(E\) embeds closed and proper; it is **not dense** in \(F\). No "E-density" argument is available or used to extend driver/flow properties from \(E\) to \(F\). The finite-propagation claim is for the total distributional data (both entries), which is strictly stronger than separate-entry propagation and is essential for killing the \(E\)-correction in PROOF106.

---

## PROOF105

**Owner: F009 `P:constant-phase-driver`. Actual extended driver.**

**Setting.** Real \(\chi\in C_c^\infty\), \(\chi=1\) on \(B_{2R+T+1}\), support in \(B_{2R+T+2}\); real compact smooth \(\psi=1\) on a neighborhood of \(\operatorname{supp}\chi\). \(M_E=M_R\), \(M_E^\rho=M_{Y_\rho}\), raw deterministic coefficients shared.

**Statement.** As identities of continuous operator paths,
\[
D_\chi M_E=M_E=M_ED_\chi,
\tag{105.i}
\]
and the same for each fixed \(\rho\). Define
\[
A_E=M_EL_\psi,\quad A=iA_E,\qquad
A_E^\rho=M_E^\rho L_\psi,\quad A^\rho=iA_E^\rho.
\tag{105.ii}
\]
These are **independent of \(\psi\)**, have compact values, and satisfy
\[
Ai=iM_E,\qquad \pi_CA=0,
\tag{105.iii}
\]
and the source counterparts. In every finite \(L^pC^\theta\), \(A^\rho\to A\) at arbitrary relative source-width rates. Their norms have uniform \(\sqrt p\) moment bounds and a common finite square-exponential moment. The raw \(A\) is \(W\)-measurable.

**Derivation.** `L:driver-gain-localization` gives both localizations for every deterministic \(A_j(0,t)\); raw finite sums retain them; source finite sums use the same coefficients with correlated \(Y_\rho(f_j)\) (PROOF095); the \(C^\theta\) limits preserve the identities via rational times/continuous paths (one event per \(\rho\)). Independence of \(\psi\): \((L_\psi-L_{\psi'})z\in E\) and \(D_\chi(L_\psi-L_{\psi'})z=0\), so right localization kills the difference. For \(z=ie\), \(D_\chi D_\psi e=D_\chi e\) gives \(Ai=iM_E\). The two constant columns \(iM_E(\psi,0)\) and \(iM_E(0,\psi)\) are retained. Composition preserves compactness and transfers `E:source-driver-limit` and the Gaussian bound: if \(\|X\|_{L^p}\le C\sqrt p\), then \(\E X^{2n}\le C^{2n}(2n)^n\le C^{2n}(2en)^n/(n!)\)-compatible, and \(n!\ge(n/e)^n\) makes \(\E e^{cX^2}<\infty\) for \(2ecC^2<1\). \(A\) is a deterministic bounded transform of the \(W\)-measurable raw driver.

**Pinpoint.** Boundedness of \(L_\psi\) and the large cutoff are both used; left and right localization are both derived; both constant-response columns appear. The independence-of-\(\psi\) argument is a genuine right/left-localization identity, not an E-density argument. Only the raw \(A\) is \(W\)-measurable; the source \(A^\rho\) may carry the auxiliary \(J\)-component of PROOF097/098.

---

## PROOF106

**Owner: F009 `L:constant-source-response`. Ordinary response on all of \(F\).**

**Setting.** Fixed \(\rho\), \(b(r)=mY_\rho(r)\), and
\[
B_F(b)(e,c_1,c_2)=(0,\,b(e_1+c_1))\in E.
\tag{106.i}
\]

**Statement.**
\[
A_E^\rho(t)z=\int_0^t S(-r)B_F(b(r))S_F(r)z\,\ud r
\tag{106.ii}
\]
as a statewise strong integral; its primitive is Lipschitz in \(\mathcal B(F,E)\), and the identity holds for all states and times on one probability-one event for this \(\rho\).

**Derivation.** On the horizon \(b\) has one compact spatial support, is \(L^\infty\)- and \(L^2\)-continuous in time, with bounded spatial derivatives. Since \(e_1\in L^2\) and \(\|\cdot\|_{H^{-1/2}}\le\|\cdot\|_{L^2}\),
\[
\|B_F(b)\|_{\mathcal B(F,E)}\le\|b\|_\infty+\|b\|_2.
\tag{106.iii}
\]
Strong continuity and finite-horizon bounds make the integrand strongly continuous per state and uniformly operator-bounded, so integration gives operator-norm Lipschitz increments **without a Banach-space operator derivative**. The total initial distributions of \(z\) and \(iL_\psi z\) agree on the ball where \(\psi=1\), so (104.ii) gives equality of the free displacements near \(\operatorname{supp}m\) for \(0\le r\le T\); multiplication by \(b(r)\) kills the difference, and (100.i) applies to \(L_\psi z\): hence (106.ii). Density of \(E\) in \(F\) is never used.

**Pinpoint.** The argument uses the **total-data** finite propagation of PROOF104: the \(E\)-correction \((z-iL_\psi z)\) is not annihilated by separate-entry support; it is annihilated because \(S_F\) is the total-distribution wave group. Proposition 100 handles the actual \(E\)-state response; (106.ii) transports it to all of \(F\). No density of \(E\) in \(F\), no point trace, and no commutation of \(b\) with a mask is used.

---

## PROOF107

**Owner: F009 `P:constant-young-linear`. Exact left-order linear Young equation.**

**Source input.** Banach Young estimate, FH20 Sections 1.4–1.5, 4.1, (4.3), pp. 13,61–62: for \(D,V\) \(C^\theta\), \(\theta>1/2\), bounded bilinear multiplication,
\[
\Big\|\int_s^t\ud D(r)V(r)-D(s,t)V(s)\Big\|
\le C_\theta[D]_\theta[V]_\theta\,|t-s|^{2\theta}
\tag{107.i}
\]
with **left composition**; the Banach space is \(\mathcal B(F)\) (bilinear constant one). No nonlinear bounded-vector-field theorem and no rough second-level tensor pairing is imported.

**Statement.** For every \(D\in C^\theta([0,T];\mathcal B(F))\), \(D(0)=0\), there is a unique \(C^\theta\) solution in the terminal variable of
\[
U_D(t,s)=I+\int_s^t \ud D(r)\,U_D(r,s).
\tag{107.ii}
\]
It has composition \(U_D(t,r)U_D(r,s)=U_D(t,s)\), invertible values, and joint operator-norm continuity on \(0\le s\le t\le T\). The map \(D\mapsto U_D\) is locally Lipschitz into the uniform time-triangle norm, and
\[
\sup_{s\le t\le T}\|U_D(t,s)\|
\le C_T\exp\big(C_T(1+\|D\|_{C^\theta})^{1/\theta}\big).
\tag{107.iii}
\]

**Derivation.** On \([a,a+\ell]\) the scaled norm \(N_\ell(V)=\sup\|V\|+\ell^\theta[V]_\theta\) and \(I_D(V)=\int_a^\cdot\ud D\,V\) satisfy, by (107.i) applied to subintervals,
\[
N_\ell(I_D(V))
\le c_\theta[D]_\theta\ell^\theta N_\ell(V),\qquad c_\theta=2\max(1,C_\theta).
\tag{107.iv}
\]
With \([D]_\theta\le K\) and \(c_\theta K\ell^\theta\le1/4\), \(V\mapsto V_a+I_D(V)\) is a contraction; so \(N_\ell(V)\le2\|V_a\|\). Difference estimate:
\[
N_\ell(W)\le2\|W_a\|+2c_\theta\ell^\theta\delta N_\ell(V'),
\qquad W=V-V',\ \delta=\|D-D'\|_{C^\theta}.
\tag{107.v}
\]
Pieces \(j\) satisfy \(E_{j+1}\le2E_j+2^{j+2}c_\theta\ell^\theta\delta B\) with \(B=\|V'\|\) endpoint bound one; induction gives \(E_j\le2^jE_0+j2^{j+1}c_\theta\ell^\theta\delta B\), with a uniform number of pieces in \(s,t\), proving local Lipschitz dependence. \(K=1+\|D\|_{C^\theta}\) uses \(\le C_T(1+\|D\|_{C^\theta}^{1/\theta})\) pieces, each at most doubling the norm, giving (107.iii). Composition follows by right multiplication of the preceding evolution; \(N_\ell(U-I)\le1/3\) gives a Neumann invertibility; \(U_D(t,s)=U_D(t,0)U_D(s,0)^{-1}\) gives joint continuity.

**Pinpoint.** **Left order is essential**: the increment \(D(s,t)\) multiplies \(V(s)\) on the left; the proof never commutes \(\mathcal B(F)\) operators and never reorders \(D(t)-D(s)\) past \(V\). \(\theta>1/2\) is used both for \(2\theta>1\) (remainder is \(o(|t-s|)\)) and for the locally convergent fixed point; the excluded boundary/composition cases (e.g. a non-converging Young remainder for an \(\alpha\)-Hölder integrator with \(2\alpha<1\)) are not covered. No RSS-second-level tensor, no rough-path renormalization, no nonlinear bounded-vector-field theorem is used.

---

## PROOF108

**Owner: F009 `P:constant-gaussian-flow`. Actual Gaussian Young and physical flows.**

**Statement.** Applied to \(A,A^\rho\), the flows \(U_A,U_{A^\rho}\) are strongly measurable in the uniform triangle norm, have every finite norm moment, satisfy
\[
U_{A^\rho}\to U_A\quad\text{in every finite }
L^p\Big(\sup_{0\le s\le t\le T}\|\cdot\|_{\mathcal B(F)}\Big),
\tag{108.i}
\]
preserve the interaction constant coordinates
\[
\pi_C U_A(t,s)=\pi_C,\qquad (U_A(t,s)-I)F\subset iE,
\tag{108.ii}
\]
and likewise for the source. The physical flow
\[
P_A(t,s)=S_F(t)U_A(t,s)S_F(-s)
\tag{108.iii}
\]
has composition and strong continuity on states, physical constant block \((c_1,c_2)\mapsto(c_1+(t-s)c_2,c_2)\), all finite moments, and the analogous uniform \(L^p\) source convergence; \(P_A(t,s)-S_F(t-s)\) has range in \(iE\).

**Derivation.** Continuity of the Young map and the separable driver path span give strong measurability into \(C(\Delta_T;\mathcal B(F))\). Applying \(\pi_C\) to Young Riemann sums gives \(\pi_CU=\pi_C\); each increment lands in \(iE\), which is closed, giving the second identity in (108.ii).

**Convergence (108.i) — localized driver ball first, then \(K\to\infty\).** Let \(X_\rho=\|A^\rho\|_{C^\theta}\), \(X_0=\|A\|_{C^\theta}\); PROOF105 supplies \(c_0>0,H_0<\infty\) with \(\sup_\rho\E e^{c_0X_\rho^2}\le H_0\), \(\E e^{c_0X_0^2}\le H_0\). On \(\{X_\rho\le K,\ X_0\le K\}\), Proposition 107 gives
\[
\|U_{A^\rho}-U_A\|_\infty\le L_K\|A^\rho-A\|_{C^\theta}.
\tag{108.iv}
\]
For \(\varepsilon>0\), finite \(q\ge1\),
\[
\P(\|U_{A^\rho}-U_A\|_\infty>\varepsilon)
\le 2H_0 e^{-c_0K^2}
+(L_K/\varepsilon)^q\,\E\|A^\rho-A\|_{C^\theta}^q.
\tag{108.v}
\]
At fixed \(K\) the second term tends to zero at arbitrary relative source rates; only then \(K\to\infty\). **No independence** of raw, source, and residual drivers is used.

**Moments.** With \(\nu=1/\theta<2\), for each finite \(r\ge1\), \(c>0\),
\[
r C_T(1+x)^\nu\le cx^2+C_{r,c},
\tag{108.vi}
\]
since \((1+x)^\nu/x^2\to0\). With \(c\le c_0\) and (107.iii), \(\sup_\rho\E\|U_{A^\rho}\|_\infty^r<\infty\), \(\E\|U_A\|_\infty^r<\infty\). For \(V_\rho=\|U_{A^\rho}-U_A\|_\infty\),
\[
\E V_\rho^p\le\varepsilon^p+(\E V_\rho^{2p})^{1/2}\P(V_\rho>\varepsilon)^{1/2},
\tag{108.vii}
\]
giving \(L^p\) convergence by uniform \(2p\)-moments of \(V_\rho\) (bounded by \(2^{2p}((\E\|U_{A^\rho}\|_\infty^{2p})^{1/2}+(\E\|U_A\|_\infty^{2p})^{1/2})\)). The free group is strongly continuous and bounded on the horizon; \(C_T\ge\sup_{|r|\le T}\|S_F(r)\|\), and the bounded linear map \(\mathcal L(V)(t,s)=S_F(t)V(t,s)S_F(-s)\) into \(\mathcal B_\infty(\Delta_T;\mathcal B(F))\) has norm \(\le C_T^2\), so
\[
\|P_{A^\rho}-P_A\|_\infty\le C_T^2\|U_{A^\rho}-U_A\|_\infty,
\tag{108.viii}
\]
transferring moments and convergence. Statewise joint continuity uses only norm-continuous \(U\) modulo strong free-group differences. Physical constant block from \(J_tJ_{-s}=J_{t-s}\).

**Pinpoint.** The proof uses a **square-exponential bound on the DRIVER** \(A,A^\rho\) (PROOF105) combined with \(1/\theta<2\) from (108.vi) to obtain **finite flow moments and uniform integrability**. It does **not** assert or need a square-exponential bound on the flow \(U_A\), and it does not place the physical flow in a norm-continuous triangle space or assert operator-norm continuity of the free group. The physical families are statewise strongly continuous/norm-bounded operator families, with strong measurability through the separable ranges; convergence is at fixed \(L^p\), uniformly in the triangle norm.

---

## PROOF109

**Owner: F009 `L:constant-source-solution`. Identification with the ordinary source equation.**

**Statement.** For fixed \(\rho\), the displacement distribution of \(P_{A^\rho}(t,0)e_0\) is the locally continuous ordinary source solution \(u_\rho^m(t,\cdot)\) from PROOF102.

**Derivation.** In (106.ii) write \(C(r)=S(-r)B_F(b(r))S_F(r)\), so \(A_E^\rho\) is its primitive. The Young sums
\[
\sum_j\int_{t_j}^{t_{j+1}}iC(r)U_{A^\rho}(r_j,s)v\,\ud r
\tag{109.i}
\]
converge to the strong integral with \(U(r,s)v\) by uniform continuity of \(U\) and the uniform \(C\)-bound; thus the Young equation is exactly the ordinary interaction integral on states. Multiplying by the free groups gives the full-phase Duhamel equation; its unique \(C([0,T];F)\) solution follows from the bounded-coefficient Picard argument.

**Picard and chain identification.** Put \(W_0=e_0\), \(W_n(t)=\int_0^tS_F(t-r)iB_F(b(r))W_{n-1}(r)\ud r\), with \(B_T=\sup_r\|B_F(b(r))\|\le\sup(\|b\|_\infty+\|b\|_2)\). Induction on the time simplex gives \(\sup_t\|W_n(t)\|_F\le C_T^{n+1}B_T^nT^n/n!\), so the series converges in \(C([0,T];F)\) and its sum solves the Duhamel equation with coefficient \(g=b\). Let \(X_0=1\), \(X_n(t)=\int_0^tG_d(t-r)*(b(r)X_{n-1}(r))\ud r\); for compact smooth test \(\varphi\),
\[
\langle[X_n(t)]_1,\varphi\rangle
=\int_0^t\int f_r(y)\int G_d(t-r,\ud z)\varphi(y+z)\ud y\ud r,
\tag{109.ii}
\]
with \(f_r=b(r)X_{n-1}(r)\) smooth and compactly supported; absolute Fubini uses \(\|\varphi\|_\infty\|f_r\|_1(t-r)\), covering sphere measures in \(d=3\). Iterating gives exactly \(X_{\rho,n}^m\) with chronological order and one physical mask factor per vertex. The scalar compact-cone factorial bound gives locally uniform convergence to \(u_\rho^m\); the phase series converges in \(F\), hence in distributions; both displacement limits agree.

**Pinpoint.** This identifies the **distributional displacement**, not a pointwise \(H^{1/2}\) trace. The chain identification relies on PROOF106 (identity on all of \(F\)) and PROOF104 (total-data propagation) and on continuous testing of the phase integral by \(\varphi\). All identities are at one fixed \(\rho\); no uncountable common source-version event is used.

---

## PROOF110

**Owner: F009 `P:constant-raw-average`. Actual raw average and original point moment.**

**Setting.** Real \(\phi\in C_c^\infty\), \(\phi\ge0\), \(\int\phi=1\). Define the bounded functional and raw observable
\[
O_\phi(e,c_1,c_2)=\langle e_1,\phi\rangle+c_1,\qquad
Z_m(t,\phi)=O_\phi P_A(t,0)e_0.
\tag{110.i}
\]

**Statement.** \(O_\phi\) is bounded (\(H^{-1/2}\)-duality; \(\|O_\phi\|\le(\|\phi\|_{H^{-1/2}}^2+1)^{1/2}\)). \(Z_m\) is \(W\)-measurable. At arbitrary relative source-width rates, for every finite \(p\),
\[
\int\phi(x)u_\rho^m(t,x)\ud x
\longrightarrow Z_m(t,\phi)\quad\text{in }L^p.
\tag{110.ii}
\]
In particular
\[
\E|Z_m(t,\phi)|^2\le\E|u(t,0)|^2.
\tag{110.iii}
\]

**Derivation.** \(Z_m\) is a continuous/bounded measurable transform of the \(W\)-measurable raw driver through Young/deterministic maps on separable ranges; it **does not depend on the auxiliary \(J\)**. At fixed \(\rho\), (109.i)–(109.ii) give the a.s. identity
\[
O_\phi P_{A^\rho}(t,0)e_0
=\int\phi(x)u_\rho^m(t,x)\ud x =:C_\phi ,
\tag{110.iv}
\]
using the displacement pairing and the constant displacement coordinate in (110.i) — no point trace of \(H^{1/2}\) is taken. The a.s. average \(C_\phi\) equals the Bochner \(L^2\) average \(B_\phi\) of PROOF102: scalar Fubini gives \(\E\int|\phi u_\rho^m|\le Q_t\|\phi\|_1<\infty\) and \(\E|C_\phi|^2\le\|\phi\|_1\int|\phi|\E|u_\rho^m|^2\le Q_t^2\|\phi\|_1^2\); for every bounded real \(\Xi\), Bochner duality commutes with the test functional, and \(\Xi=\operatorname{sign}(B_\phi-C_\phi)\) gives equality a.s. PROOF108 gives
\[
\|B_\phi-Z_m(t,\phi)\|_{L^p}
\le\|O_\phi\|\,\|e_0\|\,\|\|P_{A^\rho}-P_A\|_\infty\|_{L^p}\to0,
\tag{110.v}
\]
which is (110.ii) for the **actual masked Bochner average**. This is exactly the conditional convergence premise of PROOF103 for the same mask, horizon, covariance, and observable, before time asymptotics; PROOF103 then gives (110.iii). Zero covariance gives the free constant solution and equality.

**Pinpoint.** PROOF108–PROOF110 **discharge** the PROOF103 conditional premise; the inequality to \(\E|u(t,0)|^2\) is a point–masked-average comparison, not an identification of the unmasked nonlinear solution or a W-only representation of the raw solution. No \(H^{1/2}\) point trace and no automatic uniqueness/W-measurability of an unmasked nonlinear limit is claimed. \(Z_m\) is \(W\)-measurable because it is built from the \(W\)-measurable raw driver \(A\), unlike cutoff source fields which may use \(J\).

---

## PROOF111

**Owner: F009 `P:constant-compact-base`. Compact deterministic base.**

**Setting.** Real \(h\in C([0,T];C_c^\infty(K))\) for one compact \(K\), all spatial derivatives continuous on the support; primitive
\[
A_h(t)=\int_0^t iS(-r)B_F(h(r))S_F(r)\ud r .
\tag{111.i}
\]

**Statement.** \(A_h\) is Lipschitz in \(\mathcal B(F)\), takes values with range in \(iE\), and
\[
\|A_h\|_{C^\theta}\le C_T\sup_r(\|h(r)\|_\infty+\|h(r)\|_2).
\tag{111.ii}
\]
The flow conclusions of PROOF107–PROOF109, including moments, source convergence, and ordinary-source identification, hold for \(A_h+gA\) and \(A_h+gA^\rho\), uniformly on bounded displayed deterministic budgets \(H\ge\|A_h\|_{C^\theta}\) and bounded real \(|g|\le G\).

**Derivation.** \(B_F(h)\) estimate and strong free groups give (111.i)–(111.ii) as in PROOF106. Moment transfer: if \(\E e^{cX^2}<\infty\), \(X=\|A\|_{C^\theta}\),
\[
\|A_h+gA\|_{C^\theta}\le H+GX,
\]
so \(\E e^{c'\|A_h+gA\|^2}\le e^{2c'H^2}\E e^{2c'G^2X^2}<\infty\) for \(c'\le c/(2(1+G^2))\); alternatively \(pC(1+H+Gx)^{1/\theta}\le cx^2+C_{p,H,G,c}\) transfers finite moments through the Young growth bound. Source driver convergence, local Young stability (PROOF107), and uniform integrability give the flow convergence; the state-integral and Picard-to-chain arguments of PROOF106/109 apply to \(h+gmY_\rho\), whose support lies in one fixed compact union.

**Pinpoint.** These are individual estimates on uniform displayed budgets; they assert **no Cameron-shift (Girsanov) identity** and no uncountable common-parameter event. Only \(h=0\), \(g=1\) enters `E:constant-original-point-transfer`; the deterministic base \(h\neq0\) is a budget-extended perturbation, not a transport of the probability measure.

---

## PROOF112

**Owner: F010 `P:compact-ground-family`. Ground states and a uniform rate gap.**

**Setting.** \(I=[0,1]\), \(K_x\subset\R^d\) compact, \(\sigma\mapsto V_\sigma\) continuous \(I\to C_c^\infty(K_x)\), real and nonnegative; \(M=\sup_I\|V_\sigma\|_\infty\), \(H_\sigma=-\Delta-V_\sigma\). Common trial (112.CT): there is real \(w\in H^1\), \(\|w\|_2=1\), with
\[
\|\nabla w\|_2^2-\int V_\sigma w^2\le-\varepsilon\quad(\sigma\in I),\qquad\varepsilon>0.
\tag{112.a}
\]

**Imported sources (second edition, Teschl).** Theorem 10.2, p.258: for real \(V\), \(V\in L^\infty+L^2\) in \(d\le3\), \(H=H_0+V\), \(D(H)=H^2(\R^d)\) is self-adjoint, bounded below, \(\sigma_{\rm ess}(H)=[0,\infty)\), \(C_c^\infty\) a core. Theorem 10.13, p.273: if \(H=H_0+V\) is self-adjoint, bounded below, with \(C_c^\infty\) core and the bottom is an eigenvalue, it is simple with a strictly positive eigenfunction. Theorem 4.12/Cor 4.13, pp.140–141: max-min and form monotonicity with the essential threshold after discrete eigenvalues end; the quadratic-form domain may replace \(D(A)\). These hypotheses are checked for **compact smooth real** potentials (hence in \(L^\infty\cap L^2\), within the \(d\le3\) class).

**Statement.**
1. The common form domain of \(H_\sigma\) is \(H^1\), with
\[
q_\sigma(u)=\|\nabla u\|_2^2-\int V_\sigma|u|^2 .
\tag{112.b}
\]
2. The bottom \(E_1(\sigma)\) is a **simple eigenvalue** below the essential threshold, with a unique real, positive-a.e., normalized ground state \(p_\sigma\). Let \(E_2(\sigma)\) be the second max-min level, set \(0\) if no second negative eigenvalue. Then
\[
-M\le E_1(\sigma)\le-\varepsilon,\qquad
E_1(\sigma)<E_2(\sigma)\le0,
\tag{112.c}
\]
\[
|E_j(\sigma)-E_j(\tau)|\le\|V_\sigma-V_\tau\|_\infty,\qquad j=1,2.
\tag{112.d}
\]
3. \(\sigma\mapsto p_\sigma\) is continuous into \(H^2\) and bounded there. With \(\lambda_\sigma=\sqrt{-E_1}\), \(\mu_\sigma=\sqrt{-E_2}\),
\[
\sqrt\varepsilon\le\lambda_\sigma\le\sqrt M,\qquad
d_0:=\inf_I(\lambda_\sigma-\mu_\sigma)>0.
\tag{112.e}
\]
4. **Ground continuity.** For \(d_V=\|V_\sigma-V_\tau\|_\infty\),
\[
\|p_\tau-p_\sigma\|_2^2
=2(1-a)\le2(1-a^2)\le\frac{4d_V}{\Delta_*},\qquad
p_\tau=ap_\sigma+r,\ r\perp p_\sigma.
\tag{112.f}
\]

**Derivation.** For \(c=1+M\), \(A_\sigma=H_\sigma+c\ge1\); on \(H^2\),
\[
\|A_\sigma^{1/2}u\|_2^2=q_\sigma(u)+c\|u\|_2^2,\qquad
\|u\|_{H^1}^2\le\|A_\sigma^{1/2}u\|^2\le c\|u\|_{H^1}^2;
\tag{112.g}
\]
spectral and Fourier cutoffs give \(D(A_\sigma^{1/2})=H^1\), so the common form domain is \(H^1\). The trial (112.a) and form max-min give \(-M\le E_1\le-\varepsilon\); the bottom lies below the essential threshold \([0,\infty)\), hence is an isolated eigenvalue of finite multiplicity; **only then** Theorem 10.13 applies, giving simplicity and positivity. Simplicity/isolation/threshold give \(E_1<E_2\le0\); the common form test difference proves (112.d) including passage to \(E_2=0\). Compactness of \(I\) gives \(\Delta_*=\min_I(E_2-E_1)>0\); then
\[
\lambda_\sigma-\mu_\sigma
=\frac{E_2-E_1}{\lambda_\sigma+\mu_\sigma}
\ge\frac{\Delta_*}{2\sqrt M}>0,
\tag{112.h}
\]
with **no division by \(\mu_\sigma\)** (the \(\mu_\sigma=0\) threshold case is covered). Variational decomposition gives (112.f); the eigenfunction equation \((1-\Delta)p_\sigma=(1-\lambda_\sigma^2+V_\sigma)p_\sigma\) with RHS in \(L^2\) bounded by \(1+2M\) gives \(H^2\)-continuity and boundedness.

**Pinpoint.** The eigenvalue conclusion for the bottom is derived **before** invoking positivity/simplicity: the common negative trial forces the bottom strictly below the essential threshold, making it an eigenvalue; Theorem 10.13 is applied only thereafter. The bound \(E_2\le0\) and \(d_0>0\) include the threshold case \(E_2=0\) corresponding to exactly one bound state; no second negative eigenvalue is assumed. The FORM-domain claim (112.b) must be proved as above (it is not granted by Theorem 10.2, which gives \(D(H)=H^2\) and \(\sigma_{\rm ess}\)). Ground-state \(L^2\)- to \(H^2\)-continuity uses only \(H^2\)-norm equivalence and the resolvent bound; no \(L^1\) ground-state assumption is made here or imported into PROOF115.

---

## PROOF113

**Owner: F010 `L:compact-fractional-phase`. Uniform quarter-power norms.**

**Setting.** \(B=1-\Delta\), \(c=1+M\), \(A_\sigma=H_\sigma+c\).

**Statement.** The quarter-power domain is \(H^{1/2}\), and
\[
\|B^{1/4}u\|_2\le\|A_\sigma^{1/4}u\|_2
\le c^{1/4}\|B^{1/4}u\|_2 .
\tag{113.a}
\]
The norm
\[
\|(u,z)\|_{E_\sigma}^2
=\|A_\sigma^{1/4}u\|_2^2+\|A_\sigma^{-1/4}z\|_2^2
\tag{113.b}
\]
is uniformly equivalent to the fixed norm on \(E=H^{1/2}\times H^{-1/2}\), with the negative entry understood by completion.

**Derivation.** On the common form domain \(H^1\), \(B\le A_\sigma\le cB\), all \(\ge1\). For positive self-adjoint \(T,S\) with common form domain, \(T\le S\) implies \((T+t)^{-1}\ge(S+t)^{-1}\) by the closed-form variational identity
\[
\langle f,(T+t)^{-1}f\rangle
=\sup_u\{2\operatorname{Re}\langle f,u\rangle-q_T(u)-t\|u\|_2^2\};
\tag{113.c}
\]
hence \(I-t(T+t)^{-1}\le I-t(S+t)^{-1}\). With
\[
\sqrt x=\frac1\pi\int_0^\infty t^{-1/2}\frac{x}{x+t}\ud t
\quad(x\ge0),
\tag{113.d}
\]
spectral integration and positive monotone Tonelli (finite intervals first, then \(t\to\infty\)) give \(T^{1/2}\le S^{1/2}\) **as forms**, including domain inclusions. Applying this to \(B\le A_\sigma\le cB\) gives (113.a) and identifies all three quarter-power domains with \(H^{1/2}\). For \(z\in L^2\),
\[
\|A_\sigma^{-1/4}z\|_2
=\sup_{v\in D(A_\sigma^{1/4}),\,\|A_\sigma^{1/4}v\|_2=1}
|\langle z,v\rangle|
\tag{113.e}
\]
is the dual norm of \(\|A_\sigma^{1/4}u\|_2\); completion and (113.a) identify it with \(H^{-1/2}\) uniformly in \(\sigma\).

**Pinpoint.** The square-root monotonicity \(T^{1/2}\le S^{1/2}\) is **proved** through the resolvent form order (113.c) and the scalar integral (113.d) with positive spectral Tonelli; it is not an assumed "operator power monotonicity", and no equality of unbounded root domains is presupposed. The quarter-power domain identity \(D(A_\sigma^{1/4})=H^{1/2}\) is obtained from the equivalent form-domain \(D(A_\sigma^{1/2})=H^1\) and the two-sided comparison, not by fiat.

---

## PROOF114

**Owner: F010 `P:compact-E-wave`. The actual complementary wave on \(E\).**

**Setting.**
\[
e_\sigma^E=(p_\sigma,\lambda_\sigma p_\sigma),\qquad
\ell_\sigma^E(u,z)
=\frac{\langle p_\sigma,u\rangle+\langle p_\sigma,z\rangle/\lambda_\sigma}{2},
\qquad
\Pi_\sigma^E=e_\sigma^E\ell_\sigma^E .
\tag{114.a}
\]

**Statement.** These are bounded real objects, continuous in norm, with \(\ell_\sigma^E(e_\sigma^E)=1\), and
\[
P_\sigma^E(t)e_\sigma^E=e^{\lambda_\sigma t}e_\sigma^E,\qquad
\ell_\sigma^EP_\sigma^E(t)=e^{\lambda_\sigma t}\ell_\sigma^E,
\tag{114.b}
\]
\[
\|P_\sigma^E(t)(I-\Pi_\sigma^E)\|_{\mathcal B(E)}
\le C(1+t)e^{\mu_\sigma t},\qquad t\ge0,
\tag{114.c}
\]
with \(C\) uniform in \(\sigma\).

**Derivation.** Real spectral functions \(C_t(h),S_t(h)\) are \(\cos(t\sqrt h),\sin(t\sqrt h)/\sqrt h\) for \(h>0\), \(1,t\) at \(h=0\), and \(\cosh(t\sqrt{-h}),\sinh(t\sqrt{-h})/\sqrt{-h}\) for \(h<0\). The spectral wave matrix is
\[
\begin{pmatrix}
C_t(H_\sigma)&S_t(H_\sigma)\\
-H_\sigma S_t(H_\sigma)&C_t(H_\sigma)
\end{pmatrix}.
\tag{114.d}
\]
The spatial projection \(Q_\sigma^{\rm sp}=I-|p_\sigma\rangle\langle p_\sigma|\) commutes with \(H_\sigma,A_\sigma\) and contracts the (113.b) norm; on its support \(h\ge E_2=-\mu_\sigma^2\), the weighted phase blocks have scalar entries \(C_t(h),\,\sqrt{h+c}\,S_t(h),\,-hS_t(h)/\sqrt{h+c},\,C_t(h)\), each bounded by \(C(1+t)e^{\mu_\sigma t}\) (using \(|S_t(h)|\le\min(t,h^{-1/2})\) for \(h\ge0\) and \(h\)-uniform bounds for \(-\mu_\sigma^2\le h<0\)). The two ground branches \((p_\sigma,\pm\lambda_\sigma p_\sigma)\) have uniformly bounded projections by \(\sqrt\varepsilon\le\lambda_\sigma\le\sqrt M\); their sum is the spatial ground projection; the decaying branch \((p_\sigma,-\lambda_\sigma p_\sigma)\) with factor \(e^{-\lambda_\sigma t}\) lies in \(I-\Pi_\sigma^E\). The fractional norm equivalence converts bounds to \(E\), proving (114.c). The spectral matrix is identified with the actual ordinary \(E\)-flow at graph levels \((A_\sigma u,A_\sigma^{1/2}z)\) giving continuous solutions in \(H^2\times H^1\); free Fourier group and the generator checks \((z,\Delta u)\) on \(H^2\times H^1\), differentiation of the interaction picture for compact smooth data, and Picard uniqueness identify the spectral solution with the ordinary flow on these data; density within \(E\) extends equality to all of \(E\).

**Pinpoint.** Identification with the ordinary flow is **first at graph levels \(H^2\times H^1\)**, where the spectral solution is a strong solution and the free generator is explicit; it is then extended by \(E\)-density within \(E\). **No density of \(E\) in \(F\)** is used. Zero and negative energies are kept (the \(h<0\) branch and the decaying ground branch), which is needed for the complementary estimate at \(\mu_\sigma=0\).

---

## PROOF115

**Owner: F010 `P:compact-F-projection`. The full-phase growing projection.**

**Setting.** \(C(t)(c_1,c_2)=(c_1+tc_2,c_2)\), and \(D_\sigma(c_1,c_2)=(0,V_\sigma c_1)\in E\). Set
\[
f_\sigma=\frac{\int V_\sigma p_\sigma}{2\lambda_\sigma}>0,\qquad
\ell_\sigma^C(c)=f_\sigma\left(\frac{c_1}{\lambda_\sigma}+\frac{c_2}{\lambda_\sigma^2}\right),
\tag{115.a}
\]
\[
e_\sigma=ie_\sigma^E,\qquad
\ell_\sigma(e,c)=\ell_\sigma^E(e)+\ell_\sigma^C(c),\qquad
\Pi_\sigma=e_\sigma\ell_\sigma,\quad Q_\sigma=I-\Pi_\sigma .
\tag{115.b}
\]

**Statement.**
1. The physical flow has the block form
\[
P_\sigma(t)(e,c)
=\Big(P_\sigma^E(t)e+
\int_0^tP_\sigma^E(t-r)D_\sigma C(r)c\,\ud r,\ C(t)c\Big).
\tag{115.c}
\]
2. The vectors, duals, and rank-one projections are norm-continuous and uniformly bounded, and
\[
\ell_\sigma(e_\sigma)=1,\qquad
P_\sigma(t)\Pi_\sigma=\Pi_\sigma P_\sigma(t)=e^{\lambda_\sigma t}\Pi_\sigma .
\tag{115.d}
\]
3. **Positive margins.** For every fixed nonnegative smooth compact \(\phi\) of integral one,
\[
\inf_I\ell_\sigma(e_0)>0,\qquad\inf_I O_\phi(e_\sigma)>0 .
\tag{115.e}
\]

**Derivation.** (115.c) is the variation-of-constants on the \(E\) component: with \(B_\sigma^E(u,z)=(0,V_\sigma u)\), strong \(E\)-valued Fubini on the finite triangle gives
\[
\int_0^t\int_r^t S(t-s)B_\sigma^EP_\sigma^E(s-r)g(r)\ud s\ud r
=\int_0^tS(t-s)B_\sigma^E\left[\int_0^sP_\sigma^E(s-r)g(r)\ud r\right]\ud s,
\tag{115.f}
\]
so \(Y(t)=P_\sigma^E(t)e+\int_0^tP_\sigma^E(t-r)g(r)\ud r\) solves free Duhamel with force \(B_\sigma^EY+g\); taking \(g(r)=D_\sigma C(r)c\) and adjoining the constant block gives the same \(F\)-Duhamel equation as the actual flow; uniqueness gives (115.c). \(0<f_\sigma<\infty\) by \(L^2\) Cauchy–Schwarz and by positivity of \(V_\sigma\not\equiv0\), \(p_\sigma>0\) a.e.; boundedness/continuity of coefficients by \(H^2\)-continuity and the rate floor. Directly,
\[
\ell_\sigma^ED_\sigma C(r)c=f_\sigma(c_1+rc_2),
\tag{115.g}
\]
\[
\ell_\sigma^C(c)=\int_0^\infty e^{-\lambda_\sigma r}f_\sigma(c_1+rc_2)\ud r,\qquad
\ell_\sigma^C(C(t)c)=\int_t^\infty e^{\lambda_\sigma(t-r)}f_\sigma(c_1+rc_2)\ud r,
\tag{115.h}
\]
so applying \(\ell_\sigma\) to (115.c) pairs the finite response integral with the dual Laplace tail, giving (115.d). Finally \(\ell_\sigma(e_0)=f_\sigma/\lambda_\sigma>0\) and \(O_\phi(e_\sigma)=\int\phi p_\sigma>0\), continuous on compact \(I\), hence (115.e).

**Pinpoint.** Positivity is through **integrals** of \(p_\sigma\) against \(V_\sigma\) and against \(\phi\), not through a point trace or a one-dimensional ODE; **no \(L^1\) bound on the ground state** is imported. The constant dual is the **dual Laplace tail** at rate \(\lambda_\sigma\) with columns \((\lambda_\sigma^{-1},\lambda_\sigma^{-2})\), which is why the growing response to constants is retained within the projection. No density of \(E\) in \(F\) is used: (115.c) is variation-of-constants on the \(E\) component plus a separately propagated constant block.

---

## PROOF116

**Owner: F010 `P:compact-F-complement`. Full-phase complement and parameter control.**

**Statement.** Uniformly over \(\sigma\in I\), \(t\ge0\),
\[
\|P_\sigma(t)Q_\sigma\|_{\mathcal B(F)}
\le C(1+t)^3e^{\mu_\sigma t}.
\tag{116.a}
\]
For every fixed \(0<\eta<d_0\),
\[
\|e^{-\lambda_\sigma t}P_\sigma(t)Q_\sigma\|
\le C_\eta e^{-\eta t}.
\tag{116.b}
\]
For every finite \(T_0\),
\[
\sup_{0\le t\le T_0}\|P_\sigma(t)-P_\tau(t)\|_{\mathcal B(F)}
\le C_{T_0}\left(\|V_\sigma-V_\tau\|_\infty+\|V_\sigma-V_\tau\|_2\right).
\tag{116.c}
\]

**Derivation.** Write \(Q_\sigma^E=I-\Pi_\sigma^E\) and split \(D_\sigma\) into growing/complementary parts in (115.c) with the two tails (115.h). The exact \(E\)-component of \(P_\sigma(t)Q_\sigma(e,c)\) is
\[
P_\sigma^E(t)Q_\sigma^E e
+\int_0^tP_\sigma^E(t-r)Q_\sigma^ED_\sigma C(r)c\,\ud r
-e_\sigma^E\,\ell_\sigma^C(C(t)c),
\tag{116.d}
\]
with constant component \(C(t)c\). The final subtraction retains the growing response-to-constants inside the projection. Since \(\|Q_\sigma^ED_\sigma C(r)\|\le C(1+r)\), the integral has norm \(\le C e^{\mu_\sigma t}|c|\int_0^t(1+t-r)(1+r)\ud r\), which expands to \(C(t+t^2+t^3/6)e^{\mu_\sigma t}|c|\); the free-complement term is \(\le C(1+t)e^{\mu_\sigma t}\|e\|\), the subtracted term is \(O(1+t)|c|\). Since \(\mu_\sigma\ge0\) this gives (116.a), and \((1+t)^3e^{-(d_0-\eta)t}\le C_\eta\) gives (116.b). For (116.c), set \(\mathcal B_\sigma=iB_F(V_\sigma)\); \(\|\mathcal B_\sigma-\mathcal B_\tau\|\le d_{\sigma,\tau}\). The two Duhamel differences split the evolution into \((\mathcal B_\sigma-\mathcal B_\tau)P_\tau(r)\) plus \(\mathcal B_\sigma(P_\sigma(r)-P_\tau(r))\); scalar statewise Gronwall on the difference of \(F\)-valued paths (with \(\|S_F(t-r)\|\le C_T\)) gives (116.c). Uniqueness of the Duhamel solution makes finite-horizon constructions agree on overlaps; integer horizons and autonomy give the same semigroup for all \(t\ge0\).

**Pinpoint.** The \((1+t)^3\) retains the **constant-velocity polynomial** \((c_1+(t-s)c_2)\) in the complementary flow; it is not removed, only normalized out in (116.b) by the \(e^{-\lambda_\sigma t}\) factor. The subtraction in (116.d) is the projection of the growing response, not a claim that constants have no response. Parameter continuity uses only **statewise** Gronwall; the operator norm is measurable via a countable dense set of unit states, so no \(\mathcal B(F)\)-valued derivative or operator-norm continuity of the free group is needed.

---

## PROOF117

**Owner: F010 `L:compact-raw-profile`. The original mean and raw variance.**

**Setting.** \(\Gamma\neq0\) satisfies `H:homog`, \(a=\alpha_0\); real, nonnegative, nonzero
\[
\Psi\in C_c^\infty((0,1)\times\R^d)
\tag{117.a}
\]
is **arbitrary, without any separability assumption**; define
\[
h_\sigma(x)=\int_0^1|\sigma-u|^{-a}(\Gamma*\Psi(u,\cdot))(x)\ud u,\qquad
\overline q(x)=\int_0^1\Psi(u,x)\ud u,\qquad Z=W(\Psi).
\tag{117.b}
\]

**Statement.** \(h\) is smooth in \(\sigma\) and \(x\) on compact sets, and
\[
0<v_\Psi:=\E Z^2
=\int_0^1\int\Psi(\sigma,x)h_\sigma(x)\ud x\ud\sigma<\infty.
\tag{117.c}
\]
Against every smooth compact positive-time test \(F_0\),
\[
\E[W(\Psi)W(F_0)]=\int F_0(s,x)h_s(x)\ud x\ud s .
\tag{117.d}
\]
Moreover, on \(I=[0,1]\),
\[
h_\sigma\ge\Gamma*\overline q,\qquad
v_\Psi\ge Q(\overline q):=\int\Gamma(\ud z)\int\overline q(x)\overline q(x-z)\ud x>0.
\tag{117.e}
\]
For every fixed mask, \(V_\sigma=m_Rh_\sigma\) is a smooth compact family, Lipschitz in \(\sigma\) in \(L^\infty\) and \(L^2\).

**Derivation.** Choose \(A\ge1\) with spatial support of \(\Psi\subset B_A\). The raw covariance identity and absolute Fubini give (117.d): the two compact tests restrict spatial differences to a compact set of finite \(\Gamma\)-mass, and the time singularity is locally integrable since \(a<1\). The same gives (117.c); spatial finiteness by \(\|\Psi\|_\infty^2|B_A|\Gamma(\overline B_{2A})\) and time finiteness by \(\int_0^1\int_0^1|\sigma-u|^{-a}\ud u\ud\sigma=2/((1-a)(2-a))\). Since \(|\sigma-u|^{-a}\ge1\) on the unit square, positive Tonelli gives the inequalities in (117.e). The strict positivity \(Q(\overline q)>0\): \(\overline q\not\equiv0\), homogeneous nonzero \(\Gamma\) charges every origin-centered ball positively, and the continuous compact autocorrelation \(\int\overline q(x)\overline q(x-z)\ud x\) is positive at zero, hence bounded below on a small ball. Smoothness of \(h\): extend \(\Psi\) by zero in time and write \(h_s(x)=\int_\R|r|^{-a}(\Gamma*\Psi(s-r,\cdot))(x)\ud r\); on compact \((s,x)\), \((r,z)\) range over fixed compacts, \(|r|^{-a}\) is integrable, and derivatives fall on the smooth test. Multiplication by \(m_R\) gives the claimed Lipschitz family.

**Pinpoint.** The derivative is taken on the **test \(\Psi\)**, never on the singular kernel \(|r|^{-a}\). The **original** raw variable \(Z=W(\Psi)\) and variance \(v_\Psi\) are retained with the exact harmonic mean formula (117.c). Positivity of \(h_0\) holds even when \(\Psi\) vanishes near \(t=0\) (compactly supported in \((0,1)\), hence \(\Psi(0,\cdot)=0\)), because the lower floor is the positive-definite functional \(Q(\overline q)\) evaluated on the **time-integrated** profile \(\overline q\), not on \(\Psi(0,\cdot)\). This covers nonsmooth-invariant covariances, including \(d=1\) white noise, by the positive ball-mass and nonnegative autocorrelation argument.

---

## PROOF118

**Owner: F010 `P:compact-original-common-trial`. Binding with the original control and cost fixed.**

**Statement.** For every \(\Psi\) as in PROOF117, a sufficiently large finite mask \(m_R\) makes \(V_\sigma=m_Rh_\sigma\) satisfy the common negative trial (112.a). Consequently all of PROOF112–PROOF116 (ground, projection, positive margins, complementary wave) apply. The rate \(\sigma\mapsto\lambda_\sigma\) is Lipschitz on \(I\) with \(\lambda_0>0\). The original test \(\Psi\), raw variable \(Z\), and variance \(v_\Psi\) are **unchanged** by the mask choice; the mask can also cover any fixed compact variational test supports.

**Derivation (order: fix \(\Psi,Z,v_\Psi\) first, then \(L,R\)).** Choose real unit \(L^2\) \(\psi\in C_c^\infty(B_2)\) with \(\psi\ge c_0>0\) on \(B_1\); put \(\psi_L(x)=L^{-d/2}\psi(x/L)\), kinetic \(D_\psi=\|\nabla\psi\|_2^2\), with \(L\ge\max(1,2A)\). Choose \(R\ge2L\) so \(m_R\equiv1\) on \(\operatorname{supp}\psi_L\), i.e. \(V_\sigma=h_\sigma\) there. Positive Tonelli and (117.e) give
\[
\int V_\sigma\psi_L^2
\ge c_0^2L^{-d}\int_{B_L}(\Gamma*\overline q)(x)\ud x
=c_0^2L^{-d}\int\overline q(y)\Gamma(B_L-y)\ud y
\ge c_0^2L^{-d}\Gamma(B_{L/2})\int\overline q
=C_\Gamma L^{-\alpha},
\tag{118.a}
\]
with
\[
C_\Gamma=c_0^2 2^{\alpha-d}\Gamma(B_1)\int\overline q>0,
\tag{118.b}
\]
using \(B_{L/2}\subset B_L-y\) for \(|y|\le A\), \(L\ge2A\). The kinetic energy is \(D_\psi L^{-2}\). Since \(\alpha<2\), choose \(L\) large so
\[
\varepsilon_R:=C_\Gamma L^{-\alpha}-D_\psi L^{-2}>0,
\tag{118.c}
\]
giving \(\|\nabla\psi_L\|^2-\int V_\sigma\psi_L^2\le-\varepsilon_R\) for every \(\sigma\). Fix this \(R\) before invoking PROOF112. The level bound and the \(L^\infty\)-Lipschitz family give
\[
|\lambda_\sigma-\lambda_\tau|
\le\frac{\|V_\sigma-V_\tau\|_\infty}{2\sqrt{\varepsilon_R}}
\le C_R|\sigma-\tau| .
\tag{118.d}
\]
Positivity of the integrated time test gives \(\lambda_0>0\) even though \(\Psi(0,\cdot)=0\). The raw test \(\Psi\) and \(Z\) were fixed first; only trial and mask grew.

**Pinpoint.** This is **not** an all-strength binding assertion for one fixed compact potential: for each control \(\Psi\) a possibly different finite \(R\) is chosen after \(\Psi\) is fixed, and the mask is fixed **before** source/time asymptotics. There is **no unmasked-ground** hypothesis and **no uniform (in growing \(R\)) bound**: a later supremum over controls must follow the individual bounds, not one fixed mask with uniform \(R\). The comparison \(CL^{-\alpha}\) vs \(DL^{-2}\) with \(\alpha<2\) is the entire mechanism; it does not require \(\Psi\) to be nonvanishing near \(t=0\). Enlarging \(R\) to include additional fixed supports preserves the trial and gives masked/unmasked equality on those supports. Zero covariance is the separate trivial case.

---

## APPLICATION-SOURCE-YOUNG-MASKED-MEAN

One actual coupled derivation discharges the PROOF103 conditional premise and delivers the compact-deterministic mean branch.

**Chain A — raw Gaussian/source driver (linear Gaussian chain).**
\[
\text{raw 061,093}\ \to\ 095\ \to\ 098\ \to\ 100\ \to\ 105\ \to\ 106\ \to\ 107\ \to\ 108\ \to\ 109\ \to\ 110.
\]

- `raw 061/093` supplies the same-space compact operator path \(M_R\) with deterministic coefficient paths \(A_j\), the two actual variances, vanishing compact tails, the \(C^\theta\) path limit, and the raw-row identity on the given \(W\).
- PROOF094 gives the finite linear Gaussian image bound; PROOF095 transfers the whole coefficient-path family to any centered Gaussian linear noise \(Y\) with variance dominated by \(C\|\cdot\|_{H_W}^2\), yielding \(M_Y\) in every finite \(L^p\) of \(\mathscr B_\theta\) and the exact raw rows \(\langle M_Y(t)z,w\rangle=Y(h_{R,t;z,w})\) — no source-coordinate independence.
- PROOF098 constructs the canonical sources \(Y_\rho=\mathcal I(Q_\rho\Phi\,\cdot)\) and full residual \(D_\rho\) on the PROOF097 retaining space (closed-range isometry \(\Phi\), given \(W\) retained, one auxiliary \(J\) on the complement), with the joint covariance \(K_{\max(\eta,\eta')}(t-s)\Gamma_{\epsilon+\epsilon'}(x-y)\), both variance dominations \(\le\|\cdot\|_{H_W}^2\), and strong residual decay at arbitrary relative rates; the operator-path limit \(M_R^\rho\to M_R\) uses PROOF095 plus the raw path tails 091/092.
- PROOF100 identifies the ordinary source response \(L_\rho=\int_0^\cdot S(-u)B(b_\rho(u))S(u)\ud u\) with \(M_R^\rho\) by the Sobolev adjoint, raw-test identity, point-feature/ordinary integral equality, and countable phase/time closure (no free-group operator-norm continuity).
- PROOF104–PROOF105 extend to \(F=E\oplus\R^2\): distributional injection, \(E\) closed proper (not dense), total-data finite propagation with \(E\)-constant cancellation, both localizations, and \(A=iM_EL_\psi\), \(A^\rho=iM_E^\rho L_\psi\) with \(Ai=iM_E\), \(\pi_CA=0\), and both constant columns.
- PROOF106 proves the source response on **all of \(F\)** by total initial-data equality plus PROOF100; PROOF107 gives the exact left-order Young equation with \(\theta>1/2\), composition, invertibility, local difference iteration, and global growth.
- PROOF108 proves source flow convergence by first localizing the driver ball at \(K\), then \(K\to\infty\), using the **driver** square-exponential tails and \(\nu=1/\theta<2\); finite flow moments and UI follow; the physical flows \(P_A,P_{A^\rho}\) have only statewise continuity.
- PROOF109 identifies \(P_{A^\rho}(t,0)e_0\)'s displacement distribution with the ordinary masked chain solution \(u_\rho^m\) (Young sums to Duhamel/Picard to exact scalar ordered chains).
- PROOF110 defines \(Z_m(t,\phi)=O_\phi P_A(t,0)e_0\), proves \(Z_m\) is \(W\)-measurable, proves the \(L^p\) convergence of the Bochner masked averages \(\int\phi u_\rho^m\) to \(Z_m\), and thereby **discharges the explicit PROOF103 conditional \(L^2\) premise at the same mask/horizon/observable/source**, yielding
\[
\E|Z_m(t,\phi)|^2\le\|\phi\|_1^2\E|u(t,0)|^2 .
\tag{A1}
\]

**Chain B — fixed-order/masked-moment foundation.**
\[
\text{foundation 002,006,008}\ \to\ 101\ \to\ 102\ \to\ 103.
\]
`002/006/008` supply the positive ordered Green chain measures, \(L^2\) fixed-order construction with arbitrary relative Green-then-noise limits (including unequal/empty chains), the vertex bound \(q_n\) with \(\sum\sqrt{n+1}\,q_n(T)<\infty\), and the canonical mixed expansion. PROOF101 gives the expected masked/unmasked comparison with one mask factor per vertex and the \(q_n\)-bound; PROOF102 constructs the locally continuous ordinary solutions and the tested averages; PROOF103 uses fixed pair-orders, terminal-to-initial reversal, Green first, arbitrary-relative noise limits, and a double \(q_nq_k\) tail to prove the canonical point-moment limit \(\E|u_\rho(t,0)|^2\to\E|u(t,0)|^2\), then states the conditional transfer (103.ii), which Chain A discharges.

**Chain C — independent compact deterministic mean branch.**
\[
111\ \text{(budget)}\ \to\ 112\ \to\ 113\ \to\ 114\ \to\ 115\ \to\ 116\ \to\ 117\ \to\ 118.
\]
The ordinary full-\(F\) mean from `111` (deterministic compact base plus bounded real \(g\), no Cameron shift) enters the deterministic-spectral family: PROOF112 derives, from Teschl 10.2 and the common negative trial, the simple positive ground state and the level gap before applying 10.13; PROOF113 obtains the uniformly equivalent quarter-power phase norms on \(E=H^{1/2}\times H^{-1/2}\) via proved resolvent/order; PROOF114 gives the \(E\)-complementary wave at graph levels then \(E\)-density; PROOF115 builds the full-phase projection including the dual-Laplace constant columns \(1/\lambda_\sigma,1/\lambda_\sigma^2\) and the positive margins \(\ell_\sigma(e_0)>0\), \(O_\phi(e_\sigma)>0\); PROOF116 keeps the constant-velocity \((1+t)^3\) in the complement and normalizes the gap; PROOF117 fixes the **original nonseparable** control \(\Psi\), raw \(Z=W(\Psi)\), and strict variance/mean floors; PROOF118 fixes a finite \(L,R\) **after** \(\Psi,Z,v_\Psi\) and binds the potential by \(C_\Gamma L^{-\alpha}>D_\psi L^{-2}\) with \(\alpha<2\), giving \(\lambda_0>0\), all masks fixed before source/time asymptotics.

**Consumption of inputs.** The raw Gaussian/source chain consumes the actual coefficient paths from 061/093 and the full residual strong convergence from 098 (through 095 and 091/092); the masked chain consumes the fixed-order foundation 002/006/008 and the vertex \(q_n\); the compact branch consumes only the Teschl 10.2/4.12/10.13 and FH20 (4.1)–(4.3) inputs, each applied within its checked hypotheses. The original canonical mild series \(u\) is identified separately in module 009 (not through the operator/source Gaussian parent), so no hidden circular moment assumption enters Chain A or B. No AWS/CM/tube/upper051/S2-finiteness/132/204 import and no Cameron action identity is used.

---

## GLOBAL-UNPROVED-CONDITIONS

These are the conditions, false strengthenings, and genuinely open steps across the focused work. They are not "favorable examples" and no proof-status axiom is imposed.

**G1. Full heat residual independence (098).** The disjoint \(\lambda\)-tail identity
\[
\|(I-Q_\rho)g\|^2=\|(I-P_\eta)g\|^2+\|P_\eta(I-C_\varepsilon)g\|^2
\tag{G1.1}
\]
gives orthogonality of two residual *parts*, but the shared \(\lambda\le\eta^{-1}\) band still carries the \(I-C_\varepsilon\) remainder. Hence disjoint \(\lambda\)-tail independence does **not** imply independence of the full heat residual \(D_\rho\) from \(Y_\rho\), and such independence is not proved and must not be asserted.

**G2. Cutoff W-only representation is false (097/098).** For nonzero \(\Gamma\), finite \(\Lambda=\eta^{-1}>0\), \(\epsilon>0\), \(t_0>0\), the positive-cutoff point feature
\[
v_{\rho;t_0,x}(\lambda,r)
=1_{\{\lambda\le\Lambda\}}\sqrt{2\lambda}e^{-\lambda(t_0-r)}1_{\{r\le t_0\}}p_\epsilon(x-\cdot)
\tag{G2.1}
\]
does not lie in the closed range \(\Phi(H_W)\). The F194 counterexample: choose disjoint compact \(A\subset(0,\Lambda)\), \(B\subset(\Lambda,\infty)\), bumps \(u_A,u_B\),
\[
p(\lambda)=\frac{u_A}{\int u_A\ud\nu_a}-\frac{u_B}{\int u_B\ud\nu_a},\qquad
\int p\,\ud\nu_a=0,\quad \int_{\lambda\le\Lambda}p\,\ud\nu_a=1,
\tag{G2.2}
\]
and
\[
q(\lambda,r)=p(\lambda)\frac{\phi'(r)+\lambda\phi(r)}{\sqrt{2\lambda}}\otimes p_\epsilon(x-\cdot),
\qquad \phi\in C_c^\infty((0,\infty)),\ \phi(t_0)=1;
\tag{G2.3}
\]
then \(\langle\Phi F,q\rangle=0\) for all \(F\), hence \(q\in(\Phi H_W)^\perp\), while \(\langle v_{\rho;t_0,x},q\rangle=\|p_\epsilon(x-\cdot)\|^2>0\), so \((I-P)v\neq0\) and
\[
\operatorname{Var}(Y_\rho(t_0,x)\mid\sigma(W))\ge\|(I-P)v\|^2\ge\frac{|\langle v,q\rangle|^2}{\|q\|^2}>0.
\tag{G2.4}
\]
Thus positive-cutoff point fields genuinely use the auxiliary \(J\). Only fixed-\(W\) plus one auxiliary \(J\) is retained; the three public W-only/range-inclusion passages are errors.

**G3. Nonlinear/canonical-limit W-measurability.** G2 settles only the finite-cutoff field. Whether a particular **nonlinear/canonical limit** is \(\sigma(W)\)-measurable by another argument is **open**; PROOF110 gives W-measurability of the tested masked observable \(Z_m\) through the raw \(W\)-measurable driver \(A\), and the unmasked comparison to \(\E|u(t,0)|^2\) is an inequality via the canonical series (103.i), not an equality to a W-only pathwise object.

**G4. PROOF103 conditional premise is real.** Uniform \(L^2\) bounds, the unmasked point-moment limit, and presence of a limit object do not yield (103.ii). Bounded non-convergent average families satisfy the uniform bounds while failing the premise. Only Chain A (108–110) discharges it for the exact same Bochner average.

**G5. PROOF098 operator-path claim.** The full claim (098.vi) \(M_R^\rho\to M_R\) in \(L^p(\mathscr B_\theta)\) **requires** PROOF095 plus the raw path facts 091/092 (uniform head error after a uniform tail). It is not derivable from the point/test covariance algebra alone, while that algebra itself is direct and does not need an invented operator theorem.

**G6. First singular/zero-variance and one-sided variance tests.** Neither variance direction alone can support the Gaussian matrix/cluster estimates (F005 `R:gaussian-one-variance-test`); the actual construction retains **both** \(V_{\rm out}\) and \(V_{\rm in}\). If \(\Gamma=0\), everything is the zero driver, handled separately; no positive claim is transferred across the zero covariance.

**G7. PROOF104 E-density.** \(E\) is closed and proper in \(F\), **not dense**. Any argument from \(E\)-density to \(F\) is invalid; the correct mechanism is total-data finite propagation plus the two-sided localization and both constant response columns.

**G8. PROOF107 left order and \(\theta>1/2\).** The left Young increment \(D(s,t)V(s)\) cannot be commuted; a right-order or a smeared order bound is not the statement. \(\theta\le1/2\) is excluded; no rough second-level tensor nor nonlinear bounded-vector-field theorem is imported.

**G9. PROOF108 square-exponential bound.** The square-exponential bound is on the **driver** \(A,A^\rho\), not the flow; only \(\|A\|_{C^\theta}\) with \(1/\theta<2\) and the Young growth enter. No square-exponential **flow** bound and no operator-norm-continuous physical flow/free group is proved or used; flows are statewise strongly continuous bounded operator families with strong measurability.

**G10. PROOF112 bound states.** The common trial forces a bottom eigenvalue below the threshold before 10.13; if the threshold is reached (\(E_2=0\)), exactly one negative bound state occurs, and the uniform gap uses \(\Delta_*/(2\sqrt M)\) without division by \(\mu_\sigma\).

**G11. Form/operator non-commutation.** \(B=1-\Delta\) and \(A_\sigma=H_\sigma+c\) do not commute; PROOF113 proves the square-root order \(B^{1/4}\le A_\sigma^{1/4}\le c^{1/4}B^{1/4}\) from the proved resolvent form comparison and positive spectral Tonelli; no operator power identity of noncommuting roots is assumed.

**G12. PROOF115 no \(L^1\) ground assumption.** The positive margins \(\ell_\sigma(e_0)\), \(O_\phi(e_\sigma)\) are integrals of \(p_\sigma>0\); the constant dual Laplace tail uses \(f_\sigma=\int V_\sigma p_\sigma/(2\lambda_\sigma)>0\). No \(p_\sigma\in L^1\) bound is used or needed.

**G13. PROOF116 constant tail.** The complement retains the constant-speed \((1+t)^3\) response; (116.b) is the normalized gap after multiplying by \(e^{-\lambda_\sigma t}\), not a decay of the constant response itself.

**G14. PROOF118 binding scope.** For each fixed \(\Psi,Z,v_\Psi\) a separate finite \(L,R\) is chosen before source/time asymptotics; there is no unmasked ground, no uniform-in-\(R\) bound, and no single fixed compact potential binding all strengths. White/singular admissible \(\Gamma\) with \(\Psi\) compactly supported away from \(t=0\) still gives \(h_0\ge\Gamma*\overline q\) with \(Q(\overline q)>0\), so \(\lambda_0>0\). Zero covariance is separate.

**G15. Cameron/shift and source independence.** PROOF111 asserts no Cameron-shift identity; only budget-extended deterministic perturbation. Source coefficient independence is never assumed in PROOF095/098; joint Gaussianity appears only in the stability hypotheses.