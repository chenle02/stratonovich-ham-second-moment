## PROOF178
`L:uniform-E-lift` (F023, Lemma `L:uniform-E-lift`)

**Actual statement.** Let \(E=H^{1/2}(\mathbb R^d)\times H^{-1/2}(\mathbb R^d)\),
\(F=E\oplus\mathbb R^2\), \(i:E\to F\) the inclusion. Fix the root profile
\(\eta\in C_c^\infty(\mathbb R^d)\), \(0\le\eta\le1\), \(\eta=1\)
on \(B_1\), \(\operatorname{supp}\eta\subset\overline B_2\), and
\(m_R=\eta(\cdot/R)^2\) for \(R\ge1\). For real smooth compact \(q\) put
\(V_q=m_R(\Gamma*q)\), \(M_q:H^{1/2}\to H^{-1/2}\) its multiplier, and
\(L_q^E(u,v)=(0,M_qu)\). Let \(\mathcal V_{E,R}\subset\mathcal K(E)\)
be the operator-norm closure of these operators.

Then every \(L\in\mathcal V_{E,R}\) has the form \(L(u,v)=(0,Mu)\) with
\(\|L\|=\|M\|=:k\), and it determines a unique real \(V\in H^{-1/2}\)
supported in \(\operatorname{supp}m_R\) such that \(Mu=Vu\) on
\(H^{1/2}\). The actual symmetric pairing
\[
v_V(u,w)=\langle Vu,w\rangle_{H^{-1/2},H^{1/2}}
\]
satisfies
\[
|v_V(u,w)|\le k\|u\|_{H^{1/2}}\|w\|_{H^{1/2}}.
\]
It possesses a lift \(L_F\) in the exact class of Section `signed-static-wave`
(the closure in \(\mathcal K(F)\) of \((u,v,c_1,c_2)\mapsto(0,V_qu+c_1V_q,0,0)\)),
with \(L_F\,i=i\,L\). Lift constants may depend on \(R\) and are used
**only for identification**, not as uniform budgets.

**Actual unproved/failed step.** The extension to \(L_F\) is proved only by
the fixed-\(R\) smooth-\(q\) closure bound involving
\(\|\chi_R\|_{H^{1/2}}\); this is allowed to grow with \(R\), and it does
not give a quantitative \(F\)-norm. Consequently no uniform-in-\(R\) lift
bound is obtained. The raw potential \(V\) is only in \(H^{-1/2}\), so
pointwise or \(H^2\) operator facts about the signed potential are not
asserted here.

## PROOF179
`P:uniform-E-spectral` (F023, Proposition `P:uniform-E-spectral`)

**Actual statement.** With \(E\), \(\mathcal V_{E,R}\), \(v_V\) from
PROOF178, define the lower form
\[
\beta(V)=\inf_{\substack{u\in H^1(\mathbb R^d)\\ \|u\|_2=1}}
\{\|\nabla u\|_2^2-v_V(u,u)\},\qquad
\lambda(L)=\sqrt{-\beta(V)}.
\]
For \(K\ge\max(1,k)\), the actual physical wave \(P_V^E(t)\) satisfies,
for all \(t\ge0\),
\[
-K^2\le\beta(V)=\inf\operatorname{spec}H_V\le0,
\qquad
\|P_V^E(t)\|_{\mathcal B(E)}
\le 8(1+K)^2(1+t)e^{\lambda(L)t}.
\]
If two such operators \(L_V,L_W\) have norms at most \(K\), then
\[
|\beta(V)-\beta(W)|\le(K+2)\|L_V-L_W\|,
\qquad
|\lambda(L_V)-\lambda(L_W)|
\le\sqrt{(K+2)\|L_V-L_W\|}.
\]
The quantitative constants use the \(E\) norm alone. The proof shifts by
\(c=2+K^2\), \(A=H_V+c\), \(L_K=3(1+K^2)\), and establishes the
quarter-power domain \(D(A^{1/4})=H^{1/2}\) and the negative dual
\(H^{-1/2}\) by the sandwich
\(\frac12(1-\Delta)\le A\le L_K(1-\Delta)\), using only the form
representation of Teschl (physical pages 92–93, 112–117, 121). The
\(H_V\) is the unique self-adjoint operator of the closed form
\(q_V=\|\nabla u\|_2^2-v_V(u,u)\) on \(H^1\). No \(H^2\) operator domain
is asserted for the rough signed \(V\).

**Actual unproved/failed step.** The form is closed and semibounded only
because \(|v_V(u,u)|\le K\|u\|_{H^{1/2}}^2\le K\|u\|_2\|u\|_{H^1}\);
without the half-weight AM-GM bound the negative completion could fail
to be both closed and nondegenerate. The continuity rate
\(|\lambda(V)-\lambda(W)|\le\sqrt{(K+2)\|L_V-L_W\|}\) depends on an
\(\varepsilon\)-minimizer of the quadratic form and the fact that such a
minimizer has \(H^1\)-budget \(z\le K+2\). No optimizer or self-adjoint
\(H^2\) eigenfunction at the bottom is assumed; the spectral bottom is
identified through form/complement arguments, not a ground state.

## PROOF180
`P:uniform-rate-averaging` (F023, Proposition `P:uniform-rate-averaging`)

**Actual statement.** The scalar-temporal mean is
\(C_t=K^{1/2}\iota:H_t\to L^r(I)\) with kernel \(|s-t|^{-a}\), and
\(C_t\) is compact into \(L^r(I)\) for \(2<r<2/a\). \(T_R\) is the actual
completed spatial mean, \(W_R=\mathcal T_R\Phi=C_t\Phi\) transported;
\(\|\mathcal T_R\|\le C_{\rm mean}=M_0\|C_t\|\) uniformly in \(R\ge1\).
Use the true partition \(I_m\) with mesh at most \(\delta B\); the averaging
\(\mathcal A_\delta\) averages over each positive-length cell and ignores the
empty last cell. Put
\(\omega_\delta=\|(\mathcal A_\delta-I)C_t\|_{H_t\to L^r(I)}\). Then
\(\omega_\delta\to0\) as \(\delta\to0\) at fixed \(B\).

For \(M\ge0\), \(\|\Phi\|_{H_I}\le M\), \(W_R=\mathcal T_R\Phi\),
\(\overline W_R=\mathcal A_\delta W_R\), \(Z=C_{\rm mean}M\),
\[
\|W_R\|_{L^r},\|\overline W_R\|_{L^r}\le Z,
\quad
\|\overline W_R-W_R\|_{L^r}\le M_0M\omega_\delta
=:\Omega_\delta(M).
\]
The own rate is
\[
\operatorname{Rate}_R(\Phi)=\int_0^1\lambda(\mathcal T_R\Phi(s))\ud s,
\]
and the averaged-rate error is
\[
\int_I|\lambda(\overline W_R)-\lambda(W_R)|\ud s
\le\sqrt{3+2Z}\,\sqrt{\Omega_\delta(M)}
=:\Lambda_\delta(M)\longrightarrow0.
\]
Both errors are uniform in \(R\ge1\). The rate is finite, nonnegative and
continuous on \(H_I\), with
\(\operatorname{Rate}_R(\Phi)\le1+C_{\rm mean}\|\Phi\|\). The comparison
\(|\lambda(W_1)-\lambda(W_2)|\) is applied with the locally defined
\(K(s)=\max(1,\|W_1(s)\|,\|W_2(s)\|)\), not an a priori universal
\(K\le1+k\).

**Actual unproved/failed step.** The passage to \(\omega_\delta\to0\) is a
**scalar-time** compactness statement for the compact image of \(C_t\);
it does not compactify the spatial tensor \(C_t\otimes I_{H_{\rm sp}}\).
Only after the typed identity
\(\mathcal A_\delta^{\mathcal K(E)}\mathcal T_R
=\mathcal T_R((\mathcal A_\delta C_t)\otimes I)\) is the uniform-in-\(R\)
bound obtained through \(\|T_R\|\le M_0\). The full mean is not asserted
compact for any \(R\), and the rate error is only an \(H^1\)-form-based
\(L^1(I)\) comparison, not a uniform-in-\(B\) statement.

## PROOF181
`L:uniform-product-budgets` (F023, Lemma `L:uniform-product-budgets`)

**Actual statement.** For the scalar free-wave bound
\(G_B=\sup_{|v|\le B}\|S_E(v)\|\) with \(E=H^{1/2}\times H^{-1/2}\),
and
\[
C_B=G_B^2\bigl(B^{1-1/r}+B^{1-1/r-\theta}\bigr),
\]
the estimates
\[
1\le G_B\le3B,\qquad
C_B\le18B^{3-1/r}\le32B^{3-1/r},\qquad
C_BB^{1/r}\ge B
\]
hold. For \(\Phi\in H_I\), \(W_R=\mathcal T_R\Phi\) and the true blocks
\(H_m=\int_0^{\min(u,\ell_m)}S_E(-v)W_R(s_m+\delta v)S_E(v)\ud v\),
the stopped primitives lie in the zero-start little Hölder space and
\[
\|H_m\|_\theta\le a_m:=C_B\delta^{-1/r}\|W_R\|_{L^r(I_m)},
\qquad
\delta\sum_m a_m^r\le C_B^r\|W_R\|_{L^r(I)}^r.
\]
There is a fixed \(C_{\rm gr}=C_{\rm gr}(\theta)>0\) such that for every
zero-start \(C^\theta([0,B];\mathcal L(E))\) path \(D\),
\[
\log\|S_E(\ell)U_D(\ell,0)\|
\le C_{\rm gr}B(1+\|D\|_\theta^\nu),
\qquad 0\le\ell\le B,
\]
with \(\nu=1/\theta<2\), where \(U_D\) is the left Young evolution. No
Gaussian, Hamiltonian or positivity hypothesis is used for this bound.
The actual mean endpoints satisfy \(\|P_m^{\rm mean}\|\ge1\), where
\(P_m^{\rm mean}=S_E(\ell_m)U_{H_m}(\ell_m,0)\).

**Actual unproved/failed step.** The first line uses \(C_B\le32B^{3-1/r}\),
a sufficient replacement for the earlier finer \(\le18B^{3-1/r}\); this is
exact for \(r\ge1\). The baseline \(\|P_m^{\rm mean}\|\ge1\) is imported
from the symmetric/symplectic compact-free lower bound and holds only for
the **mean** endpoint, not for arbitrary perturbed paths. The individual
primitive bound \(a_m\) is \(r\)-norm based and loses no additional factor;
there is no uniform-in-\(R\) control of \(W_R\) beyond \(C_{\rm mean}\), so
no \(R\)-uniform equivalence of \(H_m\) to \(a_m\) is claimed.

## PROOF182
`P:uniform-mean-product` (F023, Proposition `P:uniform-mean-product`)

**Actual statement.** Fix integer \(B\ge1\), \(M\ge0\), \(K\ge1\),
\(Z=C_{\rm mean}M\). Then uniformly in \(R\ge1\), \(\|\Phi\|_{H_I}\le M\),
\[
\begin{aligned}
&\delta\sum_{m=0}^N\log\|P_m^{\rm mean}\|
-\operatorname{Rate}_R(\Phi)\\
&\quad\le\frac{L_{B,K}}B
+C_{\rm gr}32^rZ^rB^{3r}(K^{-r}+K^{\nu-r})
+\Lambda_\delta(M)+C(\theta,B,K)E_\delta
+\operatorname{Last}_\delta,
\end{aligned}
\]
where
\[
L_{B,K}=\log16+4\log(1+K)+3\log(1+B),
\]
\[
\begin{aligned}
E_\delta&=(2/B)^{1-1/r}C_B\Omega_\delta(M)
+(2/B)^{1-\nu/r}C_B^\nu\Omega_\delta(M)^\nu,\\
\operatorname{Last}_\delta
&=C_{\rm gr}B\bigl[\delta+C_B^\nu Z^\nu\delta^{1-\nu/r}\bigr].
\end{aligned}
\]
The last three terms tend to zero as \(\delta\to0\) at fixed \(B,K,M\).
Here \(P_m^{\rm mean}\) is the physical mean endpoint of the frozen/block
mean path \(H_m\); on full cells with \(a_m\le K\), the static spectral
bound of PROOF179 gives the exact \(e^{B\lambda(\bar M_m)}\) plus the
\(O(L_{B,K}/B)\) prefactor, and the perturbative bound uses the
**left** multiplicative Young estimate with actual left multiplier
\(S_E(B)\). Bad cells use PROOF181 growth with
\(1+a_m^\nu\le(K^{-r}+K^{\nu-r})a_m^r\) for \(a_m>K\ge1\). The
terminal \(\tau\)-cell uses the **stopped** path; its error is
\(\operatorname{Last}_\delta\), with \(\nu<r\), so no division by the
terminal cell length occurs.

**Actual unproved/failed step.** The frozen-block comparison is carried out
only on **full** cells. It requires the frozen spatial operator
\(\bar M_m\in\mathcal V_{E,R}\) with \(\|\bar M_m\|\le K/B\le K\) to have
the exact \(E\)-static bound of PROOF179; for blocks whose averages
satisfy \(a_m>K\), the estimate is the cruder
\(C_{\rm gr}B(1+a_m^\nu)\). No \(R\)-uniform bound on the size of
\(\bar M_m\) is available, and no uniform validity of the **good/bad**
partition as \(R\) varies is established beyond the fixed
\(a_m\le C_B Z\) budgets.

## PROOF183
`C:uniform-polynomial-balls` (F023, Corollary `C:uniform-polynomial-balls`)

**Actual statement.** For \(c_{\rm ball}>0\), \(\kappa_{\rm ball}\ge0\),
put \(M_B=c_{\rm ball}B^{\kappa_{\rm ball}}\). Then
\[
\limsup_{\substack{B\to\infty\\B\in\mathbb N}}
\limsup_{\delta\downarrow0}
\sup_{\substack{R\ge1\\\|\Phi\|_{H_I}\le M_B}}
\left\{\delta\sum_m\log\|P_m^{\rm mean}\|
-\operatorname{Rate}_R(\Phi)\right\}\le0.
\]
The proof fixes
\(s>r(3+\kappa_{\rm ball})/(r-\nu)\) and \(K_B=B^s\). At fixed \(B\),
the inner \(\delta\) limit is taken **first**, at fixed \(B,M_B,K_B\),
with fixed radius \(R\) and threshold \(K_B\). The bad-block exponents
after substituting \(M_B=c_{\rm ball}B^{\kappa_{\rm ball}}\) are
\[
C_{\rm gr}32^rC_{\rm mean}^rc_{\rm ball}^r
\left\{B^{r(3+\kappa_{\rm ball})-sr}
+B^{r(3+\kappa_{\rm ball})+s(\nu-r)}\right\}
\]
and both powers are strictly negative. Also
\(L_{B,K_B}/B\to0\). The outer limit is taken only as integer
\(B\to\infty\). No diagonal choice \(B=B_\delta\) or \(M_\delta\) is made.

**Actual unproved/failed step.** The assertion is only an outer
integer-\(B\) limsup after an inner fixed-\(B\) \(\delta\)-limit. It does
not give a uniform bound for a \(B(\delta)\)-dependent threshold, and no
uniform-in-\(R\) compactness of the **ball** family is used. The rate
logarithmic excess is only for the mean product; the perturbed residual
excess is handled separately in PROOF184. Nothing here proves a uniform
polynomial-radius estimate for the stochastic endpoint or for the full
raw flow.

## PROOF184
`P:uniform-arbitrary-residual` (F023, Proposition `P:uniform-arbitrary-residual`)

**Actual statement.** Let \(x_m\) be arbitrary zero-start little
\(C^\theta\) compact-operator paths on \([0,B]\), \(v_m=\|x_m\|_\theta\),
\[
Y=\left(\delta\sum_{m=0}^Nv_m^p\right)^{1/p}.
\]
Define
\[
P_m^{\rm pert}=S_E(\ell_m)U_{H_m+x_m}(\ell_m,0),\qquad
z_{\rm rat}=\prod_m\frac{\|P_m^{\rm pert}\|}{\|P_m^{\rm mean}\|}.
\]
For every fixed integer \(B\ge1\), \(M\ge0\), \(K_{\rm res}\ge1\),
\[
\begin{aligned}
\delta\log\max(1,z_{\rm rat})
&\le C_{K_{\rm res}}\bigl[(2/B)^{1-1/p}Y+(2/B)^{1-\nu/p}Y^\nu\bigr]\\
&\quad+c_BD_M(K_{\rm res}^{-r}+K_{\rm res}^{\nu-r}),
\end{aligned}
\]
uniformly in \(R\ge1\) and \(\|\Phi\|_{H_I}\le M\). Here
\(C_{K_{\rm res}}=C(\theta,B,K_{\rm res})\), \(c_B=2^{\nu-1}C_{\rm gr}B\),
\(D_M=C_B^r(C_{\rm mean}M)^r\). The bad-cell treatment uses the actual
mean denominator \(\|P_m^{\rm mean}\|\geq1\), so the ratio is bounded by
the positive denominator one; the weighted
power-mean step uses \(p\ge\nu\), \(r>\nu\), and is valid for
\(p=\nu\), zero entries and the true empty final cell. Product
submultiplicativity does not commute the noisy factors.

If \(b_\delta\ge0\) is deterministic with \(b_\delta\to0\) at each fixed
\(B\), \(M_B\) is as in PROOF183, and
\[
\mathcal F=2\delta\log\max\bigl(1,\|P_N^{\rm pert}\cdots P_0^{\rm pert}\|\bigr),
\]
then
\[
\limsup_{\substack{B\to\infty\\B\in\mathbb N}}
\limsup_{\delta\downarrow0}
\sup_{\substack{R\ge1,\ \|\Phi\|\le M_B\\Y\le b_\delta}}
\{\mathcal F-2\operatorname{Rate}_R(\Phi)\}\le0.
\]
The limit order is \(\delta\downarrow0\) at fixed \(B,M_B,K_{\rm res}\),
then \(K_{\rm res}\to\infty\), then \(B\to\infty\). The factor
\(\mathcal F\) already carries \(2\delta\log\|\cdot\|\).

**Actual unproved/failed step.** No Gaussian, Cameron, positivity or
Hamiltonian condition is imposed on the residuals, so the bound is purely
deterministic and cannot itself control the actual stochastic residual
size \(Y\). Its application requires the separate actual Gaussian law
(PROOF170) and the matching \(Y\le b_\delta\) constraint from the
tube section. The integrated 2-rate comparison is obtained only after
product submultiplicativity and the mean-product \(\le0\) limsup of
PROOF183; nothing here gives the **actual** endpoint moment bound.

## PROOF185
`L:point-actual-finiteness` (F024, Lemma `L:point-actual-finiteness`)

**Actual statement.** Set \(a=\alpha_0\),
\(\kappa=(4-\alpha-a)/(3-\alpha)>1\), and for \(0<\delta<1\),
\[
L=\delta^{-1},\quad R=L+2,\quad T_\delta=\delta^{-1/\kappa},
\quad g=\delta^{(1-a)/2},\quad \Gamma_\delta=g^2\Gamma.
\]
Fix the real even root \(\eta\), \(\psi=\eta(\cdot/R)\), \(m=\psi^2\),
\(z=(\psi,0)\in E\), \(D=B_1(0)\), \(v_d=|D|>0\). Let
\(W_{\rm fast}=W\circ T_{\delta,0}\) be the fast raw noise on the same
probability space, and \(P_\delta\) the physical \(E\) endpoint at time
\(L\) driven by \(gM_R(W_{\rm fast})\), with mask \(m\) once.

For nonzero \(\Gamma\), the actual \(E\) flow and its source flows are the
closed isometric restrictions of their actual \(F\) extensions; the
operator norms are measurable and
\[
1\le\mathbb E\|P_\delta\|_{\mathcal L(E)}^2<\infty.
\]
The finiteness input is the actual Gaussian tube / radial expected-radius
bound at \(B=1\) (PROOF170–173) and the compact deterministic baseline
\(\|P_\delta\|\ge\|S_E(L)\|\ge1\). The construction matches the given
\(W_{\rm fast}\), mask \(\eta^2\), amplitude \(g\), horizon
\(L=\delta^{-1}\). No \(F\)-norm rate along growing radii is assumed, and
no uniform-in-\(R\) endpoint rate is asserted here.

**Actual unproved/failed step.** The finiteness proof uses the actual
Cameron-tube radius \(b_{\delta,B}\) and Rayleigh bound for the
fixed-\(B\) tuple, identified with the same \(P_\delta\). This requires
the genuine AWS support and measurable-norm structure from the separator
sections; without that identification, the endpoint law only has finite
moments at fixed parameters, not a bound for the global \(P_\delta\). In
particular, the statement is not derivable from a uniform-growing-\(R\)
\(F\)-norm rate; any such rate is not proved and is excluded.

## PROOF186
`L:point-fast-sources` (F024, Lemma `L:point-fast-sources`)

**Actual statement.** At fixed \(\delta\), take one retaining slow source
\(Y_{\epsilon,\tau}(\epsilon,\tau>0)\) and define
\[
Y_{\rm fast}(t,x)=\delta^{a/2}Y_{\epsilon,\tau}(\delta t,x).
\]
Its actual physical \(E\) flow \(P_E^{\epsilon,\tau}\) with coefficient
\(m gY_{\rm fast}\) satisfies
\[
\mathbb E\sup_{0\le s\le t\le L}
\|P_E^{\epsilon,\tau}(t,s)-P_E(t,s)\|^2
\longrightarrow0
\qquad(\epsilon,\tau)\to(0,0).
\]
The unmasked field \(gY_{\rm fast}\) has the canonical source law for
covariance \(\Gamma_\delta\), spatial width \(\epsilon\), temporal width
\(\tau/\delta\); the covariance is
\[
\operatorname{Cov}(gY_{\rm fast}(t,x),gY_{\rm fast}(s,y))
=K_{\tau/\delta}(t-s)(p_{2\epsilon}*\Gamma_\delta)(x-y).
\]
The source and raw residual test variances are both dominated by
\(\|f\|_{H_{\rm fast}}^2\), and the residual variance tends to zero at
fixed \(\delta\) on every smooth compact test. This yields actual
Gaussian the path convergence and finite-order uniform integrability via
the Young transfer, using the **single retaining extension** \(W+J\) only;
no uniform-in-\(\delta\) source bound and no call to an equal-law family is
used. Cutoffs are not \(W\)-only; ordinary source first-primitive/flow
identities hold on all \(E\).

**Actual unproved/failed step.** The positive-cutoff point features are
**not** in the closed range \(\Phi(H_W)\) (the counterexample with
\(p(\lambda)=u_A/(\int_A)-u_B/(\int_B)\), \(\int p\,d\nu_a=0\),
\(\mathrm{sign}+\) in \(\phi'(r)+\lambda\phi(r)\)). Therefore the
source uses the independent \(J\) component and is not \(\sigma(W)\)-measurable:
\[
\operatorname{Var}(Y_\rho(t_0,x)\mid\sigma(W))
=\|(I-P_\Phi)v\|_{\mathcal G}^2\ge|\langle v,q\rangle|^2/\|q\|^2>0.
\]
No false \(W\)-only range inclusion or point-source measurability is
claimed; only the fixed-\(W+J\) extension and its limiting identities are
used. Measurability or independence of the **nonlinear canonical limit**
is left open.

## PROOF187
`L:point-compact-source` (F024, Lemma `L:point-compact-source`)

**Actual statement.** For fixed \(\delta,\epsilon,\tau>0\), the
displacement
\[
v_{\epsilon,\tau}(t,x)=\bigl(\operatorname{pr}_1P_E^{\epsilon,\tau}(t,0)z\bigr)(x)
\]
has a jointly measurable continuous version and satisfies the ordinary
scalar mild equation
\[
v(t)=\cos(t\sqrt{-\Delta})\psi+\int_0^t G_d(t-r)*[b(r)v(r)]\ud r,
\qquad b=mgY_{\rm fast},
\]
with initial data \((\psi,0)\). The construction uses the higher Sobolev
phase \(E_k=H^k\times H^{k-1}\) with integer \(k>d/2+1\), the Bessel
free matrix
\[
\begin{pmatrix}\cos(t|\xi|)&\langle\xi\rangle\sin(t|\xi|)/|\xi|\\
-|\xi|\sin(t|\xi|)/\langle\xi\rangle&\cos(t|\xi|)\end{pmatrix},
\]
and the multiplier bound
\[
\|b(t)f\|_{H^{k-1}}\le C_k\max_{|j|\le k-1}\|\partial^j b(t)\|_\infty
\|f\|_{H^{k-1}},
\]
together with Picard factorial
\(\sup\|Z_n\|_{E_k}\le C_L^{n+1}B_L^nL^n\|z\|_{E_k}/n!\). These high
norms identify the **smooth source** displacement; the raw \(E\) phase has
no point trace and no pointwise algebra is imposed.

**Actual unproved/failed step.** The mild-equation equality is distributional
and then lifted to continuous versions through Green measures and absolute
Fubini; without the positive finite Green measures and the compact smooth
source support, a pointwise displacement of a finite-width smoothed field
could not be identified with the ordinary scalar mild solution. No
pointwise equality or mild identity is asserted for the **raw** \(E\) phase,
and the raw phase is not identified with an unmasked field in \(E\).

## PROOF188
`P:point-source-cone` (F024, Proposition `P:point-source-cone`)

**Actual statement.** Let \(u_{\epsilon,\tau}^{\rm full}\) be the unmasked
source solution with coefficient \(gY_{\rm fast}\) and data \((1,0)\).
At the fixed parameters, almost surely,
\[
v_{\epsilon,\tau}=u_{\epsilon,\tau}^{\rm full}
\quad\text{on }
\mathcal C=\{(t,x):0\le t\le L,\ |x|\le1+L-t\}.
\]
Consequently
\[
\mathbb E\|\operatorname{pr}_1P_E^{\epsilon,\tau}(L,0)z\|_{L^2(D)}^2
=v_d\,\mathbb E|u_{\epsilon,\tau}^{\rm full}(L,0)|^2<\infty.
\]
The proof uses the total initial difference
\((\psi-1,0)=(\psi,0)+(-1,0)\) in \(E\) plus constants, the compact
support of every free-phase kernel in \(B_t\), and the causal-cone closure
with \(R=L+2\) so that \(\operatorname{supp}\psi\cap\) the cone expansion
lies in the plateau. Finiteness of the honest sample coefficient on the
compact cone gives the factorial difference
\(\le HM^nt^{2n}/(2n)!\), requiring no sample positivity and no global
supremum moment. Tonelli and unmasked source spatial stationarity give
the **average of the square**
\(\mathbb E\|v_{\epsilon,\tau}(L,\cdot)\|_{L^2(D)}^2
=v_d\mathbb E|u^{\rm full}_{\epsilon,\tau}(L,0)|^2\),
not the square of an average and not a masked covariance ordering. The
full unmasked field is not embedded in \(E\) or \(F\).

**Actual unproved/failed step.** The cone equality is a pathwise
comparison of two ordinary mild solutions at fixed widths. It does not
transfer automatically to the limiting raw \(E\) phase: passing the
average-of-squares to the source limit is the separate double-limit step
of PROOF189. Without that source limit at fixed \(\delta\), the equality
remains a preliminary \(v_d\)-scaled spatial-square identity with no claim
about the original point moment.

## PROOF189
`P:original-point-transfer` (F024, Proposition `P:original-point-transfer`)

**Actual statement.** For every original model, including \(\Gamma=0\),
\[
\mathbb E|u_\Gamma(T_\delta,0)|^2
=v_d^{-1}\mathbb E\|\operatorname{pr}_1P_\delta z\|_{L^2(D)}^2
\le v_d^{-1}\|\psi\|_{H^{1/2}}^2\mathbb E\|P_\delta\|^2,
\]
\[
\limsup_{T\to\infty}T^{-\kappa}\log\mathbb E|u_\Gamma(T,x)|^2
\le\limsup_{\delta\downarrow0}\delta\log\mathbb E\|P_\delta\|^2
\quad\text{for every fixed }x.
\]
The data cost satisfies
\[
\|\psi\|_{H^{1/2}}^2\le R^d\|\eta\|_2^2+R^{d-2}\|\nabla\eta\|_2^2
\le C_\eta R^d,
\qquad C_\eta=\|\eta\|_2^2+\|\nabla\eta\|_2^2>0,
\]
with the correct negative power \(R^{d-2}\) in \(d=1\), and
\[
\operatorname{DataPref}_\delta=v_d^{-1}C_\eta(\delta^{-1}+2)^d,
\qquad \delta\log\operatorname{DataPref}_\delta\to0.
\]
The proof performs **two separate fixed-\(\delta\) source limits of equal
prelimit moments**: the operator-flow \(L^2(\Omega;L^2(D))\) limit via
PROOF186 and the full canonical point second moment via the canonical
masked transfer and the exact scaling PROOF119/125, at
covariance \(\Gamma_\delta\) and source cutoffs
\((\epsilon,\tau/\delta)\). Both widths go to zero **first** at fixed
\(\delta,R,L\); only then is the law scaling applied at
\(T_\delta=\delta^{-1/\kappa}\). Same-space convergence is not confused
with moment/law scaling, and zero-point Jacobian is not used. Full
mixed/unequal/self/empty Stratonovich chains and the Green-first
convention in \(d=3\) are retained. Logs are of positive finite moments;
spatial stationarity is used only for the original canonical \(u\). Zero
covariance is handled directly by the free cone identity and the
polynomial \(\|S_E(\delta^{-1})\|\) bound; no nondegenerate-Gaussian
premise is required.

**Actual unproved/failed step.** The transfer depends on the equality, at
fixed \(\delta\), of the two **limits** of the equal prelimit squares; this
is a double-limit exchange and is not an optimization identity. It also
takes \(\delta\to0\) only after the fixed-\(\delta\) source, Green and
canonical-chain limits. No quantitative rate of source convergence
uniform in \(\delta\) is claimed; any such uniform rate is not proved and
is not used. The raw \(E\) phase is not replaced by a pointwise solution
of the original SPDE on a shared probability space for all \(T\).

## PROOF190
`L:signed-score-envelope` (F025, Lemma `L:signed-score-envelope`)

**Actual statement.** With the **original** covariance \(\Gamma\), the
space \(H_I\) is not reweighted by \(g\) and is not a sum of fast block
costs. Let \(R_\delta=\delta^{-1}+2\) and
\(M_\delta=\mathbb E\|P_\delta\|^2\). For \(R\ge1\), define
\[
\mathcal S_R=\sup_{\Phi\in H_I}
\{2\operatorname{Rate}_R(\Phi)-\tfrac12\|\Phi\|_{H_I}^2\},
\qquad
V_{\rm up}=\limsup_{\delta\downarrow0}\mathcal S_{R_\delta}.
\]
Then
\[
0\le\mathcal S_R,V_{\rm up}\le2+2C_{\rm mean}^2<\infty.
\]
The upper bound follows from
\(\operatorname{Rate}_R(\Phi)\le1+C_{\rm mean}\|\Phi\|\); no optimizer,
positive control, finite rank, or convergence of \(\mathcal S_{R_\delta}\)
is assumed. The actual tube envelope \(G_{\delta,B}\) satisfies,
uniformly in \(R\ge1\) (in particular \(R=R_\delta\)),
\[
G_{\delta,B}(\rho)\le A_0+A_1B^{3\nu}\rho^\nu+\eta_B b_{\delta,B}^\nu,\quad
0<\delta<\min(1,1/B),\ \rho\ge0,
\]
with
\[
A_0=4C_{\rm gr},\qquad
A_1=2^{\nu+1-\nu/r}C_{\rm gr}32^\nu C_{\rm mean}^\nu,\qquad
\eta_B=2^{\nu+1-\nu/p}C_{\rm gr}B^{\nu/p}.
\]
The actual covariance/Cameron scale is \(\sqrt\delta\), and the expected
radius anchor uses **one** \(R^{d/Q}\) with fixed \(Q\) guards before
\(\delta\to0\). The score is not identified with any author constant
\(E,E_*,\gamma_*^0\), nor with the positive-control score.

**Actual unproved/failed step.** The score \(\mathcal S_R\) is only finite
by the crude bound; its possible nonconvergence along the moving radius is
harmless because \(V_{\rm up}\) is a limsup. The polynomial
\(A_1B^{3\nu}\rho^\nu\) envelope is a **coarse** envelope of the coarse
\(G_{\delta,B}\), not the sharp half-action variational envelope. No
positive-control optimizer or continuity of \(R\mapsto\mathcal S_R\) is
proved.

## PROOF191
`P:signed-moment-bulk-tail` (F025, Proposition `P:signed-moment-bulk-tail`)

**Actual statement.** For fixed integer \(B\ge1\),
\(0<\delta<\min(1,1/B)\), \(M>0\), define the finite deterministic number
\[
\mathcal E_{\delta,B,M}=
\max\left(0,\sup_{\substack{R\ge1,\ \|\Phi\|\le M
\\\|x\|_{\delta,p}\le b_{\delta,B}}}
\bigl[\mathcal F_{\delta,B}(x+\mathcal M_{\delta,B,R}\Phi)
-2\operatorname{Rate}_R(\Phi)\bigr]\right).
\]
For every polynomial \(M_B=c_{\rm ball}B^{\kappa_{\rm ball}}\),
\(c_{\rm ball}>0,\kappa_{\rm ball}\ge0\),
\[
e_B:=\limsup_{\delta\downarrow0}\mathcal E_{\delta,B,M_B}
\quad\text{finite nonnegative},\qquad e_B\longrightarrow0.
\]
If \(4A_1B^{3\nu}\le M^{2-\nu}\), then
\[
M_\delta\le
\frac{M^2}{2\delta}e^{(\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M})/\delta}
+4e^{(A_0+\eta_Bb_{\delta,B}^\nu-M^2/4)/\delta}.
\]
The bulk \(0\le\rho\le M\) uses only
\(\rho^2\ge\|\Phi\|^2\) and the score \(\mathcal S_{R_\delta}\); it does
not require an optimizer, a finite-dimensional Gaussian density, or a
Laplace principle. The prefactor \(M^2/(2\delta)\) is retained even when
it is less than one. The tail comes from the exact Rayleigh/tube bound
with front factor 4 and exponent \(A_0+\eta_Bb_{\delta,B}^\nu-M^2/4\).

**Actual unproved/failed step.** The deterministic error
\(\mathcal E_{\delta,B,M_B}\) vanishes in the double limit only via the
**residual** product bound of PROOF184 with actual residual
\(b_\delta\to0\) at fixed \(B\). It is not a stochastic bound from the
Gaussian law alone; it requires the actual small-residual law and the
matching \(\|x\|_{\delta,p}\le b_{\delta,B}\) cutoff. The tail cutoff
condition \(4A_1B^{3\nu}\le M^{2-\nu}\) is a finite-\(M\) restriction and
is not optimal.

## PROOF192
`P:signed-operator-upper` (F025, Proposition `P:signed-operator-upper`)

**Actual statement.** The actual global operator moment obeys
\[
0\le\liminf_{\delta\downarrow0}\delta\log M_\delta
\le\limsup_{\delta\downarrow0}\delta\log M_\delta
\le V_{\rm up}\le2+2C_{\rm mean}^2.
\]
Choose \(c_{\rm ball}>0\),
\(\kappa_{\rm ball}>3\nu/(2-\nu)\), and
\(M_B=c_{\rm ball}B^{\kappa_{\rm ball}}\). The condition
\(4A_1B^{3\nu}\le M_B^{2-\nu}\) holds for all sufficiently large \(B\).
At fixed such \(B\), a positive sum is at most twice its larger term;
taking \(\delta\log\) of PROOF191 gives
\[
\delta\log M_\delta\le\delta\log2+
\max\left\{\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M_B}
+\delta\log(M_B^2/(2\delta)),\
A_0+\eta_Bb_{\delta,B}^\nu-M_B^2/4+\delta\log4\right\}.
\]
As \(\delta\to0\) at fixed \(B\), \(b_{\delta,B}\to0\) and all logarithmic
normalizers vanish, including
\(\delta\log(M_B^2/(2\delta))
=\delta\log(M_B^2/2)-\delta\log\delta\to0\). Therefore
\[
\limsup_{\delta\downarrow0}\delta\log M_\delta
\le\max\{V_{\rm up}+e_B,\ A_0-M_B^2/4\},
\]
and then \(B\to\infty\) gives the claim. The actual \(M_\delta\) endpoint
is the **same** for every \(B\) by the restart identity, so the left side
does not depend on \(B\). The order is fixed-\(B\) \(\delta\to0\) **first**
(vanishing \(\delta\log\) normalizers and \(b_{\delta,B}\to0\)), then
integer \(B\to\infty\) (error \(e_B\to0\), tail \(A_0-M_B^2/4\to-\infty\)).
No diagonal \(B(\delta)\) or assumption of a limiting score is used.

**Actual unproved/failed step.** \(\mathcal S_{R_\delta}\) is not assumed to
converge; \(V_{\rm up}\) is only a limsup. The proof uses
\(\limsup_{\delta}(X_\delta+Y_\delta)\le V_{\rm up}+e_B\), which is valid
as an inequality after the fixed-\(B\) \(\delta\)-limit, but it does not
identify \(\delta\log M_\delta\) with the score itself. The end of the
proof relies on the actual same-endpoint identification, so any failure of
that restart identification would reintroduce a \(B\)-dependence.

## PROOF193
`P:original-signed-point-upper` (F025, Proposition `P:original-signed-point-upper`)

**Actual statement.** For every original admissible model and every fixed
\(x\),
\[
\limsup_{T\to\infty}T^{-\kappa}\log\mathbb E|u_\Gamma(T,x)|^2
\le\limsup_{\delta\downarrow0}\mathcal S_{\delta^{-1}+2}
\le2+2C_{\rm mean}^2.
\]
This is obtained from PROOF189
\(\mathbb E|u_\Gamma(T_\delta,x)|^2\le
\operatorname{DataPref}_\delta M_\delta\), the fact
\(\delta\log\operatorname{DataPref}_\delta\to0\), the decreasing bijection
\(T_\delta=\delta^{-1/\kappa}\) with inverse \(\delta=T^{-\kappa}\), and
PROOF192. This is a source-first, full-chain, canonical-law upper bound; no
raw \(E\) point trace is used. The original moment is at least one and
finite, so the logarithm of a positive finite moment is well defined. For
zero covariance, \(u=1\), \(H_I=\{0\}\),
\(\operatorname{Rate}_R=\mathcal S_R=V_{\rm up}=0\), and
\(0\le\limsup_{\delta}\delta\log M_\delta\le\lim
2\delta\log[C(1+\delta^{-1})]=0\); the free
cone identity gives the spatial-square equality directly.

**Actual unproved/failed step.** The result is only an upper inequality,
not an equality or a variational identification. The moving signed raw
score \(\mathcal S_{\delta^{-1}+2}\) is not compared with the
positive-control score; no positive-lower matching or identity with the
unmasked variational value is established here. That identification is
deferred to the next claims 194–213 and is **not** proved or assumed in
PROOF193. Zero-covariance is exact for the free case, but no nonzero
positive-score closure is attempted.

## APPLICATION-UNIFORM-E-SOURCE-POINT-UPPER

**Actual combined chain.** With all \(E=H^{1/2}\times H^{-1/2}\),
\(F=E\oplus\mathbb R^2\), \(m_R=\eta(\cdot/R)^2\), \(\nu=1/\theta<2\),
\((1-\theta)^{-1}<r<2/a\), \(\nu\le p<2<r\) fixed in strict gaps, the chain is:

1. **Left Young \(+\) uniform \(E\) means.** PROOF149/150 supply the
multiplicative left Young bound
\[
\|AU_{H+X}(t)\|\le\|AU_H(t)\|\exp\{C_{\theta,B,K}(x+x^\nu)\},\quad
x=\|X\|_\theta.
\]
PROOF151/155 give the uniform completed mean
\(\mathcal T_R=C_t\otimes I\) transported by \(T_R\), with
\(\|\mathcal T_R\|\le C_{\rm mean}=M_0\|C_t\|\), \(\|T_R\|\le M_0\),
the heat/frequency tails
\(\|T_R(I-C_\varepsilon)\|\le M_h\varepsilon^{\beta/2}\),
\(\|T_R(I-P_K)\|\le M_fK^{-\beta}\), and the constant
\(M_0=A_sM^2\), \(M=M_{1/2}\), \(\beta=1/2-s\), \(s\in(\alpha/4,1/2)\).

2. **One radius envelope \(+\) signed/symplectic phase.** PROOF156–160
give the radius-explicit Schatten envelopes
\[
\|\Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma}\|_{S_q}
\le C_{\sigma,\gamma,q,d}\rho^{d/q}.
\]
This is a **single** \(R^{d/Q}\) factor with fixed even \(Q\) satisfying
\(Q\gamma>d\), \(Q>2d/(1-a)\), fixed before \(\delta\to0\). PROOF161–164
build the closed signed static forms and the quarter-power phase norm,
and PROOF165–169 establish the compact symplectic baseline
\(\|P_D(t,s)\|\ge1\) and the exact completed block-mean direction.

3. **Uniform deterministic products.** PROOF178–184 then give
\(L:uniform-E-lift\), \(P:uniform-E-spectral\), averaged mean rates and
the polynomial control-ball limits
\[
\limsup_{B\to\infty}\limsup_{\delta\to0}
\sup_{R,\|\Phi\|\le M_B}
\{\delta\sum_m\log\|P_m^{\rm mean}\|-\operatorname{Rate}_R(\Phi)\}\le0,
\]
and the arbitrary-residual integrated 2-rate limit. These are internal
\(E\)-phase deterministic estimates with no Gaussian, Cameron or
Hamiltonian assumption on residuals.

4. **Actual Gaussian support and Borel enlargements.** PROOF170 supplies
the genuine abstract Wiener support/realization
\(X\in\overline{C(H)}\) a.s., \(H_{\rm CM}=C(H)\), measurable norm, and
the finite-regression identity; PROOF171 supplies closed Borel tubes
\(\mathcal T_r=A_\delta+\sqrt\delta\mathcal M_\delta(\bar B(r))\), attained
radii \(d_\delta\), and the Rayleigh transfer. The Borell enlargement
FH pages 190–191 is applied only **after** the actual AWS eligibility of
PROOF170; no Fernique 11.7 rough-path import is used. The Cameron scale
is exactly \(\sqrt\delta\).

5. **Exact source-first point transfer.** PROOF185–189 produce the
fixed-\(\delta\) finiteness, fast-source convergence, compact-data ordinary
mild solution, cone average-of-squares, and the original point transfer
\[
\mathbb E|u_\Gamma(T_\delta,0)|^2
=v_d^{-1}\mathbb E\|\operatorname{pr}_1P_\delta z\|_{L^2(D)}^2,
\qquad
\limsup_{T}T^{-\kappa}\log\mathbb E|u_\Gamma(T,x)|^2
\le\limsup_\delta\delta\log\mathbb E\|P_\delta\|^2.
\]

6. **Moving signed raw score upper.** PROOF190–193 give
\[
\limsup_T T^{-\kappa}\log\mathbb E|u_\Gamma(T,x)|^2
\le\limsup_\delta\mathcal S_{\delta^{-1}+2}\le2+2C_{\rm mean}^2.
\]

**Standing hypotheses/domains.** All \(E\)-norm estimates use \(\Gamma\)
nonzero through the closed \(H^1\)-form with \(|v_V(u,u)|\le
K\|u\|_{H^{1/2}}^2\) and half-weight AM-GM; the radial \(S_q\) bound uses
Picard source masks with common root \(\eta\). The full \(F\) model,
source cutoffs, mild/canonical equations and both constant columns remain
in the original sections 006/008/009 and are not imported into the
uniform \(E\)-norm claims. No growing-\(R\) compactness, no \(H^1\) point
trace, no unmasked \(L^2\) ground, and no arbitrary phase-covariance
ordering is used. The \(R_\delta\) anchor uses one
\(R_\delta^{d/Q}\) with fixed \(Q\) and \(B\) fixed before \(\delta\). The
actual raw/source/Young/compact mean inputs come from the actual proofs
listed, or remain conditions; no later claim 204 or \(S_2\)-finite source
premise of 051 is used. No earlier response, and in particular no
original-119 wrong-powers report, is a proof input.

**Global actual unproved condition of the application.** The combined
chain proves only the **upper** direction through a moving limsup of the
signed raw score. It does not identify \(\limsup_\delta\mathcal
S_{\delta^{-1}+2}\) with the positive-control variational value, does not
prove a matching lower bound by the same score, and does not prove an
exact limit at fixed nonzero \(\Gamma\). The point transfer (PROOF189) is
the source-first conjunction of the operator-flow limit and the canonical
point-moment limit; it does not construct one common probability space on
which the raw phase equals the original point solution for all \(T\).

## GLOBAL-UNPROVED-CONDITIONS

**Per-section actual unproved/failed steps.**

- PROOF178: only fixed-\(R\) \(H^{-1/2}\) identification; no uniform
\(F\)-norm or pointwise/\(H^2\) rough potential. The smooth-\(q\) closure
bound can grow with \(R\).
- PROOF179: no \(H^2\) domain, no ground state, no eigenstate; only the
spectral bottom and the \(E\)-wave bound under the closed
\(H^1\)-form with \(|v_V|\le K\|u\|_{H^{1/2}}^2\). The bottom
identification is form-based, not an \(H^2\) operator theorem for \(V\).
- PROOF180: uniform \(\omega_\delta\to0\) is only scalar-time compactness
of \(C_t\); the spatial tensor is not compact and the rate error is
\(L^1(I)\) via \(K(s)=\max(1,\|W_1\|,\|W_2\|)\).
- PROOF181: \(C_BB^{1/r}\ge B\) and
\(C_B\le32B^{3-1/r}\) are sufficient inequalities; \(\|P_m^{\rm
mean}\|\ge1\) is a compact-free baseline only for the mean path.
- PROOF182: full-cell frozen static bound uses \(a_m\le K\); bad cells and
the stopped last cell use growth bounds. No uniform-in-\(R\) bound of the
frozen multiplier beyond \(a_m\) is available.
- PROOF183: only the integer-\(B\) outer limit after a fixed-\(B\)
\(\delta\)-limit; no diagonal \(B(\delta)\) and no uniform stochastic
ball bound.
- PROOF184: purely deterministic residual product bound; the actual
residual smallness \(Y\le b_\delta\) and the mean-product limit must be
supplied separately from the Gaussian law.
- PROOF185: fixed-\(\delta\) endpoint finiteness is conditional on the
actual AWS/tube identification and the restart identity of the same
\(P_\delta\); no growing-\(R\) \(F\)-rate is proved.
- PROOF186: positive-width sources are not \(W\)-only; the fixed \(W+J\)
extension has \(\|(I-P_\Phi)v\|>0\) in general, so no
\(\sigma(W)\)-measurability of cutoff sources is asserted.
- PROOF187: the ordinary mild solution exists only at positive source
widths via \(E_k\), \(k>d/2+1\); the raw \(E\) phase has no point trace.
- PROOF188: the cone equality and average-of-squares are fixed-width
pathwise prelimits; passing to the limit is deferred to PROOF189.
- PROOF189: the original point transfer is the two fixed-\(\delta\) source
limits of equal prelimit moments, followed by law scaling; no uniform
\(\delta\) source rate and no common solution space across \(T\).
- PROOF190: \(\mathcal S_R\) finite and \(G_{\delta,B}\) coarse, with
\(R_\delta^{d/Q}\) a single \(Q\)-guard factor; no positive/optimizer or
author-constant identification.
- PROOF191: the finite-delta bound uses the deterministic
\(\mathcal E_{\delta,B,M}\) and the \(4A_1B^{3\nu}\le M^{2-\nu}\)
cutoff; \(M^2/(2\delta)\) is kept but no density is used.
- PROOF192: \(\delta\to0\) at fixed \(B\) first, then \(B\to\infty\);
\(\mathcal S_{R_\delta}\) need not converge and \(V_{\rm up}\) is only a
limsup.
- PROOF193: only the upper bound by the moving signed score; no equality,
no positive-lower identification, no nonzero exact limit.

**Global unproved conditions (state-only).**

1. **Exact limit.** No claim 178–193 proves
\(\lim_{\delta\to0}\delta\log M_\delta=\lim_{\delta\to0}\mathcal
S_{\delta^{-1}+2}\), nor that the score has a limit or equals the
positive-control value \(S_2^{\rm pos}\) or the full variational value.
2. **Positive/raw identification.** The signed raw score over \(H_I\)
and the positive-control score of the unmasked lower/upper sections are
not identified; this is explicitly reserved for the next 20 claims
194–213 and is not proved here.
3. **Actual Gaussian eligible law.** The Borell/Rayleigh step is
conditional on the genuine AWS realization and the seen/attained Borel
enlargement proved in PROOF170–171; these are not consequences of
PROOF148 or finite Gaussian labels, and Borell is imported only after
eligibility.
4. **Source measurability.** Positive cutoff point features are outside
\(\Phi(H_W)\) for nonzero \(\Gamma\), so positive-width fields use the
independent \(J\) component; no \(W\)-only measurability of the canonical
nonlinear limit is proved.
5. **Uniform-R sharpness.** All \(E\)-norm estimates are deterministic
with \(\|T_R\|\le M_0\); no growing-\(R\) compactness, no \(H^1\) point
trace, no unmasked \(L^2\) ground, and no arbitrary phase-covariance
ordering is asserted.
6. **Double limits.** The effective order is: source/Green/canonical
limits at fixed \(\delta,R,L\); then \(\delta\to0\) at fixed
\(B,M_B,K_{\rm res}\); then \(K_{\rm res}\to\infty\), then integer
\(B\to\infty\). No diagonal \(B(\delta)\) or \(M_\delta\) and no
uniform-in-\(R\) zero-delta rate is available.
7. **Full \(F\) model and canonicity.** The \(F\) constant columns,
mild/canonical equations and source/canonical second moments remain in
006/008/009/101–125 and are separate from the uniform \(E\)-norm and
moving-score statements. This application derives the upper bound only
from source-first point transfer plus uniform \(E\) products and the
single \(R^{d/Q}\) anchor; no \(S_2\)-finite premise imported from an
invented 042 parent is used for 051.
8. **Batch boundary.** All 20 claims 194–213 remain **next required**;
they are neither proved, dropped, nor accepted by the present application
and global conditions.