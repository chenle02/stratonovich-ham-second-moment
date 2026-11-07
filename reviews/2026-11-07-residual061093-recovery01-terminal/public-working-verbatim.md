## PROOF061

**Source:** `notes/integrated_covariance_foundation.tex`, Proposition `P:masked-spectral-growth` (`\ref{P:masked-spectral-growth}`), statement `E:masked-gaussian-transform`, `E:masked-translated-ball`.

**Standing hypotheses:** Hypothesis `H:homog`: \(d\in\{1,2,3\}\), \(a=\alpha_0\in(0,1)\), \(\Gamma\) a nonzero nonnegative, even, positive-definite tempered Radon measure on \(\mathbb R^d\), with positive even tempered Radon spectral measure \(\mu\) in the convention
\[
\Gamma=\int_{\mathbb R^d}e^{i\xi\cdot x}\mu(\mathrm d\xi)\quad\text{(tempered pairings)},
\]
unitary Fourier constant \(c_d=(2\pi)^{-d/2}\). The single distribution pairing used is
\[
\int_{\mathbb R^d}\varphi(x)\Gamma(\mathrm dx)
=\int_{\mathbb R^d}\Big(\int_{\mathbb R^d}e^{i\xi\cdot x}\varphi(x)\mathrm dx\Big)\mu(\mathrm d\xi).
\]

**Statement.** Put
\[
M_\Gamma=\int_{\mathbb R^d}e^{-|x|^2/4}\Gamma(\mathrm dx),\qquad
C_\Gamma=\frac{e\,M_\Gamma}{(2\sqrt\pi)^d}.
\]
Then \(0<M_\Gamma<\infty\), and for every \(y\in\mathbb R^d\), \(r>0\):
\[
\int_{\mathbb R^d}e^{-|\xi-y|^2/r^2}\mu(\mathrm d\xi)
=\Big(\frac{r}{2\sqrt\pi}\Big)^d
\int_{\mathbb R^d}e^{-r^2|x|^2/4}e^{-iy\cdot x}\Gamma(\mathrm dx),
\]
and
\[
0\le\int_{\mathbb R^d}e^{-|\xi-y|^2/r^2}\mu(\mathrm d\xi)
\le\frac{r^{\alpha}M_\Gamma}{(2\sqrt\pi)^d},\qquad
\mu(B(y,r))\le C_\Gamma r^{\alpha},
\]
where \(B(y,r)\) is the open ball. The closed-ball estimate follows by the same bound at \(r+\varepsilon\) and \(\varepsilon\downarrow0\).

**Key deductions used:** physical nonnegativity of \(\Gamma\) removes the complex phase; pushforward scaling \(x\mapsto rx\) gives \(r^{\alpha-d}\Gamma(A)\). No failed deduction identified inside the stated domain. The statement deliberately asserts only pointwise nonnegativity, not a density for \(\mu\).

## PROOF062

**Source:** `P:masked-auxiliary-norm`, `E:masked-auxiliary-measure`, `E:masked-auxiliary-growth`, `E:masked-hilbert-fourier`.

**Setup.** Fix a real nonzero Schwartz \(\zeta\). For \(R>0\):
\[
\zeta_R(x)=\zeta(x/R),\quad k_R=\widehat{\zeta_R},\quad
L=\|\widehat\zeta\|_1>0,\quad k_R(u)=R^d\widehat\zeta(Ru),\quad
\|k_R\|_1=L.
\]
Define the auxiliary measure
\[
\nu_R(\mathrm d\eta)=\rho_R(\eta)\mathrm d\eta,\qquad
\rho_R(\eta)=c_d^2L\int_{\mathbb R^d}|k_R(\xi-\eta)|\mu(\mathrm d\xi).
\]

**Statement.** \(\nu_R\) is even, tempered, and Radon, with
\[
\nu_R(B(y,r))\le c_d^2 L^2 C_\Gamma r^{\alpha}
\qquad(y\in\mathbb R^d,\ r>0),
\]
uniformly in \(R>0\). If \(H\) is a separable complex Hilbert space and \(F\) an \(H\)-valued Schwartz function,
\[
\int_{\mathbb R^d}\|\widehat{\zeta_RF}(\xi)\|_H^2\mu(\mathrm d\xi)
\le\int_{\mathbb R^d}\|\widehat F(\eta)\|_H^2\nu_R(\mathrm d\eta).
\]
For real \(H\) the same holds after complexification.

**Deductions:** \(\zeta\) real gives \(k_R(-u)=\overline{k_R(u)}\); evenness of \(\mu\) gives evenness of \(\rho_R\); the Hilbert estimate uses Bochner Fourier inversion plus weighted Cauchy–Schwarz. No nonnegative physical inverse covariance for \(\nu_R\) is assumed; no stationarity of a masked field is asserted. No failed deduction identified.

## PROOF063

**Source:** Lemma `L:masked-time-completion`, `E:masked-time-schur`.

**Statement.** Let \(T>0\), \(a=\alpha_0\). The form
\[
\langle f,g\rangle_a=\int_0^T\!\int_0^T
f(t)g(s)|t-s|^{-a}\mathrm dt\,\mathrm ds
\]
is positive semidefinite on real compact smooth tests. Its null-quotient completion \(H_a\) is separable. The inclusion of tests extends continuously from \(L^2(0,T)\), with
\[
\|f\|_a^2\le\frac{2T^{1-a}}{1-a}\|f\|_2^2.
\]
In the complexification the norm is the same double integral with \(f(t)\overline{f(s)}\). In particular, bounded measurable amplitudes on a subinterval, extended by zero, belong to the completion.

**Deductions:** positive-definiteness uses \(|t-s|^{-a}=\Gamma_E(a)^{-1}\int_0^\infty\lambda^{a-1}e^{-\lambda|t-s|}\mathrm d\lambda\) plus \(e^{-\lambda|t-s|}=\int_{-\infty}^{\min(t,s)}2\lambda e^{-\lambda(t-u)}e^{-\lambda(s-u)}\mathrm du\); the Schur bound \(2T^{1-a}/(1-a)\) follows from the row integral. No failed deduction identified.

## PROOF064

**Source:** Proposition `P:masked-noise-completion`, `E:masked-actual-noise-norm`.

**Statement.** Let \(\mathcal D\) consist of finite sums \(F(t,x)=\sum_j\tau_j(t)f_j(x)\), real \(\tau_j\in C_c^\infty(0,T)\), real Schwartz \(f_j\); these are \(H_a\)-valued Schwartz functions. Let \(W\) be the original real isonormal noise of `E:cov`. Then \(\mathcal D\) lies in the original test-noise completion and
\[
\mathbb E\,W(F)^2=(2\pi)^d
\int_{\mathbb R^d}\|\widehat F(\xi)\|_{H_a^{\mathbb C}}^2\mu(\mathrm d\xi).
\]
Define \(N_R(F)^2=(2\pi)^d\int\|\widehat F(\eta)\|_{H_a^{\mathbb C}}^2\nu_R(\mathrm d\eta)\). Then \(F\mapsto W(\zeta_RF)\) extends as a contraction from the null-quotient completion for \(N_R\) into the original \(L^2(\Omega)\); the extension is centered and jointly Gaussian. For finitely many real \(F_1,\dots,F_m\in\mathcal D\), the actual masked covariance matrix is bounded in positive semidefinite order by the auxiliary Gram matrix, hence finite Gaussian image covariance comparison and comparison of every convex norm power \(\mathbb E\|X\|^p\), \(p\ge1\).

**Deductions:** the spectral normalization uses \((2\pi)^d\) together with \(c_d=(2\pi)^{-d/2}\); Gaussian comparison is by coupling \(X+Z\sim N(0,B)\) on a product space and conditional Jensen. The auxiliary completion depends on \(R,\zeta\), and does **not** define mask multiplication on the original noise quotient (this boundary is stated before 065). No failed deduction identified.

## PROOF065

**Source:** Proposition `P:masked-quotient-obstruction`.

**Statement.** In the admissible case \(d=2\), \(\alpha=1\), \(0<a<1\), \(\Gamma=\delta_0(\mathrm dx_1)\mathrm dx_2\), there is a real compact smooth mask \(\zeta\) for which no finite \(C\) satisfies
\[
\mathbb E\,W(\zeta F)^2\le C\,\mathbb E\,W(F)^2
\]
for every compact smooth test \(F\).

**Verification in the source:** \(\mu=(2\pi)^{-1}\mathrm d\xi_1\delta_0(\mathrm d\xi_2)\); the spatial null norm is
\[
V(g)=\int_\mathbb R\Big(\int_\mathbb R g(x_1,x_2)\mathrm dx_2\Big)^2\mathrm dx_1.
\]
Take real even \(\chi\in C_c^\infty(\mathbb R)\), \(\chi=1\) on \([-1,1]\), \(\chi=0\) off \([-2,2]\), with the explicit smooth paste on \(1<r<2\),
\[
\chi(x)=\frac{e^{-1/(2-r)}}{e^{-1/(2-r)}+e^{-1/(r-1)}}\quad (1<r=|x|<2).
\]
Set
\[
I_\chi=\int(\chi')^2>0,\quad J_\chi=\int\chi^4\ge2,
\]
and
\[
g(x)=\chi(x_1)\chi''(x_2),\qquad\zeta(x)=\chi(x_1)\chi(x_2).
\]
The unmasked marginal of \(g\) vanishes because \(\int\chi''=0\); integration by parts gives the marginal of \(\zeta g\) as \(-I_\chi\chi(x_1)^2\). Hence
\[
V(g)=0,\qquad V(\zeta g)=J_\chi I_\chi^2>0.
\]
For a nonzero nonnegative \(\tau\in C_c^\infty(0,T)\), \(F(t,x)=\tau(t)g(x)\) has zero unmasked variance and strictly positive masked variance.

**Deduction boundary:** this is a legal noise-null mask obstruction in \(d=2,\alpha=1\); it is **not** bypassed by defining masks on the original noise quotient, and the proof explicitly says auxiliary completion does not define multiplication by \(\zeta_R\) on the original quotient. No failed deduction identified.

## PROOF066

**Source:** Lemma `L:masked-temporal-modulation`, `E:masked-temporal-modulation`.

**Setup.** \(\langle x\rangle=\sqrt{1+x^2}\), \(I=[s,s+h]\subset[0,T]\), \(0<h\le1\); norms in complexified \(H_a\). \(A\in C^1(I;\mathbb C)\), \(M=\sup_I|A|\), \(D=\sup_I|A'|\), \(K=M+hD\), \(C_0(a)=16/(1-a)\).

**Statement.** For every real \(\omega\),
\[
\|1_IA(t)e^{i\omega t}\|_a^2
\le C_0(a)h^{2-a}(M+hD)^2\langle h\omega\rangle^{a-1}.
\]
Bound is uniform in \(T,s,h,A,\omega\).

**Deductions:** moving-endpoint derivative
\[
c'(v)=-A(s+h)\overline{A(s+h-v)}
+\int_s^{s+h-v}A'(u+v)\overline{A(u)}\mathrm du,\quad c(h)=0,
\]
splits into conjugate triangles and integrates \(y^{-a}e^{i\omega hy}f(y)\) with \(f(1)=0\), \(|f|,|f'|\le K^2\); the far-frequency regime is controlled by integration by parts. No mass-suppressing anisotropy is used in this temporal lemma. No failed deduction identified.

## PROOF067

**Source:** Lemma `L:masked-trig-products`, `E:masked-trig-products`, `E:masked-frequency-pair`.

**Setup.** \(r,\rho\ge0\); \(P_r\in\{\cos(rt),\sin(rt)\}\), \(Q_\rho\in\{\cos(\rho t),\sin(\rho t)\}\), and
\[
\mathcal Q_h(r,\rho):=\langle h(r-\rho)\rangle^{a-1}
+\langle h(r+\rho)\rangle^{a-1}.
\]

**Statement.**
\[
\|1_IAP_rQ_\rho\|_a^2
\le C_0(a)h^{2-a}(M+hD)^2\mathcal Q_h(r,\rho),
\qquad C_0(a)=\frac{16}{1-a}.
\]

**Deductions:** the two trig factors expand to four modes \(\sigma r+\tau\rho\), \(\sigma,\tau\in\{-1,1\}\), coefficients \(1/4\). Correlated modes are handled by Hilbert inequality
\[
\|\sum_j c_jv_j\|^2\le(\sum_j|c_j|)\sum_j|c_j|\|v_j\|^2,
\]
not orthogonality/independence. Repeated or zero frequencies allowed. No failed deduction identified.

## PROOF068

**Source:** Lemma `L:masked-continuous-wave`, `E:masked-continuous-wave`.

**Setup.** \(c_r(t)=\cos(rt)\), and
\[
b_r(t)=\langle r\rangle\frac{\sin(rt)}{r}\ (r>0),\qquad b_0(t)=t.
\]
For \(F_r\in\{c_r,b_r\}\), \(G_\rho\in\{c_\rho,b_\rho\}\),
\[
C_1(a)=4\cdot3^{1-a}C_0(a).
\]

**Statement.**
\[
\|1_IF_rG_\rho\|_a^2
\le C_1(a)(1+T)^4h^{2-a}\mathcal Q_h(r,\rho),\qquad0<h\le1.
\]

**Deductions:** for \(0\le r\le1\), \(b_r(t)=t\langle r\rangle\int_0^1\cos(vrt)\mathrm dv\); products are coefficient-bounded normalized integrals of \(t^jP_{r'}Q_{\rho'}\), \(j\in\{0,1,2\}\), then Hilbert Jensen plus the trig estimate; the frequency shift bracket is controlled by
\[
\frac{\langle x\rangle}{1+|e|}\le\langle x+e\rangle\le(1+|e|)\langle x\rangle,\quad
3^{1-a}\ \text{ for }a-1<0,\ h\le1.
\]
The zero-frequency sine quotient is continuous, never divided by zero. No failed deduction identified.

## PROOF069

**Source:** `integrated_wave_variance.tex`, Proposition `P:frequency-row`, `E:variance-gamma-range`, `E:variance-scale-profile`, `E:frequency-translated-growth`, `E:frequency-row-kernel`, `E:frequency-row-integral`, `E:frequency-row-bound`.

**Setup.** \(a=\alpha_0\),
\[
0<\gamma<\min\Big(\tfrac12,\tfrac{2-\alpha}{2}\Big),
\qquad
B_\alpha(h)=
\begin{cases}
1,&\alpha<1,\\
1+\log(1/h),&\alpha=1,\\
h^{1-\alpha},&\alpha>1,
\end{cases}\quad 0<h\le1.
\]
\(\nu\) is a positive Radon measure with
\[
\nu(B(y,r))\le C r^{\alpha}\quad(y\in\mathbb R^d,\ r>0).
\]
Using `E:masked-frequency-pair`,
\[
\Phi_h(\xi,\eta):=\frac{\mathcal Q_h(|\xi|,|\eta|)}
{\langle\xi\rangle\langle\eta\rangle},\qquad
J_h(\xi):=\langle\xi\rangle^{2\gamma}
\int_{\mathbb R^d}\Phi_h(\xi,\xi-\lambda)\nu(\mathrm d\lambda).
\]
The last expression is a pushforward, not a density integral.

**Statement.** There is finite \(K=K(\alpha,a,\gamma)\), independent of \(d,\nu,C,h,\xi\), such that
\[
\sup_{\xi\in\mathbb R^d}J_h(\xi)\le KCB_\alpha(h),\qquad0<h\le1.
\]

**Deductions:** near region \(|\lambda|\le4q\), \(q=\max(1,|\xi|)\), uses \(\alpha+2\gamma<2\); far region \(|\lambda|>4q\) uses \(|\eta|\ge3r/4\), the dyadic sum converging by \(\alpha+a<2\); the critical \(\alpha=1\) log is absorbed by the strict \(\gamma\) headroom. No density, evenness, or Fubini-against-density assumption. No failed deduction identified. The proof is \(\alpha\)-dependent but valid for the mandatory near/far legal windows.

## PROOF070

**Source:** Corollary `C:frequency-time`, `E:variance-beta-range`, `E:frequency-time-bound`.

**Statement.** For every
\[
\frac12<\beta<\min\Big(1-\frac a2,\frac{3-a-\alpha}{2}\Big),
\]
there is finite \(K_\beta=K_\beta(\alpha,a,\gamma,\beta)\) such that
\[
h^{2-a}\sup_{\xi\in\mathbb R^d}J_h(\xi)\le K_\beta C h^{2\beta},\qquad0<h\le1.
\]

**Deductions:** at \(\alpha=1\), \(h^\delta(1+\log(1/h))\le1+1/(e\delta)\) for \(\delta=2-a-2\beta>0\) absorbs the critical log strictly; no endpoint \(\beta\) value, no \(\alpha=1\) necessity, and no spurious \(a/\gamma\) loss. No failed deduction identified.

## PROOF071

**Source:** `P:actual-wave-form`, `E:variance-free-matrix`, `E:variance-displacement`, `E:variance-dual-wave`, `E:variance-actual-form`, `E:variance-physical-adjoint`, `E:variance-cutoff-adjoint`, `E:variance-normalized-kernel`, `E:variance-normalized-covariance`, `E:variance-complex-noise`.

**Setup.** \(T>0\), \(\Lambda=(1-\Delta)^{1/2}\), \(s=1/2\), \(E_r=H^r(\mathbb R^d)\times H^{r-1}(\mathbb R^d)\), \(E=E_s\). Unitary Fourier phase map
\[
Jz(\xi)=\big(\langle\xi\rangle^{1/2}\widehat z_1(\xi),
\langle\xi\rangle^{-1/2}\widehat z_2(\xi)\big)
:\ E\to L^2(\mathbb R^d;\mathbb C^2).
\]
Free massless wave Fourier matrix
\[
S(t,\xi)=
\begin{pmatrix}
\cos(t|\xi|)&\sin(t|\xi|)/|\xi|\\
-|\xi|\sin(t|\xi|)&\cos(t|\xi|)
\end{pmatrix},
\]
with sine quotient equal to \(t\) at \(0\). \(B(b)(u,v)=(0,bu)\). Fix real even nonnegative \(\zeta\in C_c^\infty\), \(\zeta=1\) on \(B_1\), \(0\) off \(B_2\), \(\zeta_R(x)=\zeta(x/R)\). For \(I=[t_0,t_0+h]\subset[0,T]\) and Schwartz \(z,w\),
\[
v_z(t)=[S(t)z]_1,\qquad
G_w(t)=-\frac{\sin(t|D|)}{|D|}\Lambda w_1
+\cos(t|D|)\Lambda^{-1}w_2,
\]
\[
F_{z,w}(t,x)=1_I(t)v_z(t,x)\overline{G_w(t,x)},\qquad
\ell_R(I;z,w)=W_{\mathbb C}(\zeta_RF_{z,w}),
\]
\(W_{\mathbb C}(F)=W(\operatorname{Re}F)+iW(\operatorname{Im}F)\). No observation cutoff.

**Statement.** The tests \(\zeta_RF_{z,w}\) belong to the original noise completion; \(\ell_R\) is linear in \(z\), conjugate-linear in \(w\), on the same \(W\). For smooth compactly supported \(b\),
\[
\langle S(-t)B(b(t))S(t)z,w\rangle_E
=\int_{\mathbb R^d}b(t,x)v_z(t,x)\overline{G_w(t,x)}\mathrm dx,
\]
and the phase-cutoff multiplier \(D_\chi\) has adjoint
\[
D_\chi^{*,E}w
=\big(\Lambda^{-1}\chi\Lambda w_1,\Lambda\chi\Lambda^{-1}w_2\big).
\]
With \(U=Jz,V=Jw,r=|\xi|,\rho=|\eta|\),
\[
\mathcal K(t;\xi,\eta)
=\frac1{\sqrt{\langle\xi\rangle\langle\eta\rangle}}
\begin{pmatrix}
-b_rc_\rho&-b_rb_\rho\\[2mm]
c_rc_\rho&c_rb_\rho
\end{pmatrix}(t),
\]
where \(c_r,b_r\) are the continuous factors of `L:masked-continuous-wave`, and
\[
\mathbb E|\ell_R(I;z,w)|^2
\le\int_{\mathbb R^d}
\Big\|\int\sum_{i,j=1}^2
1_I\mathcal K_{ij}(\cdot;\eta+\lambda,\eta)
U_j(\eta)\overline{V_i(\eta+\lambda)}\mathrm d\eta
\Big\|_{H_a^{\mathbb C}}^2\nu_R(\mathrm d\lambda).
\]

**Deductions:** the zero-frequency matrix is
\(\begin{pmatrix}-t&-t^2\\1&t\end{pmatrix}\) at \(\xi=\eta=0\); Fourier conjugation yields \(\widehat F_{z,w}(t,-\lambda)\), evenness of \(\nu_R\) removes the sign; the factor \((2\pi)^dc_d^2=1\) cancels all Fourier constants. Actual wave tests are admitted through Schwartz-seminorm time approximation, not rough Fourier point sampling. No failed deduction identified.

## PROOF072

**Source:** Lemma `L:phase-bessel`, `E:phase-bessel`.

**Statement.** Let \(H\) be a separable complex Hilbert space, \(\{u_k\}\) a finite orthonormal family in \(L^2(\mathbb R^d;\mathbb C^2)\), \(g=(g_1,g_2)\in L^2(\mathbb R^d;H^2)\). Then
\[
\sum_k\Big\|\int\sum_{j=1}^2u_{k,j}(\eta)g_j(\eta)\mathrm d\eta\Big\|_H^2
\le\int\sum_{j=1}^2\|g_j(\eta)\|_H^2\mathrm d\eta.
\]
The same bound holds with \(\overline{u_{k,j}}\) replacing \(u_{k,j}\).

**Deductions:** expansion in an \(H\)-basis, scalar Bessel, Parseval, nonnegative Tonelli; both conjugation conventions are proved. No independence. No failed deduction identified.

## PROOF073

**Source:** Proposition `P:wave-two-variances`, `E:wave-input-variance`, `E:wave-output-variance`.

**Statement.** There is a finite \(C_T\), depending on the fixed model, mask, \(a,\alpha,\gamma,T\) but **not** on \(R,I\) or the orthonormal family, such that for every finite complex \(E\)-orthonormal Schwartz family \(\{e_k\}\) and every Schwartz phase \(z\),
\[
\sum_k\mathbb E|\ell_R(I;e_k,z)|^2
\le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2,
\]
\[
\sum_k\mathbb E|\ell_R(I;z,e_k)|^2
\le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2.
\]
For every \(\beta\) in `E:variance-beta-range`, either right side may be replaced by \(C_{T,\beta}h^{2\beta}\|z\|_{E_{s-\gamma}}^2\).

**Deductions:** the two directions are derived **separately**: input direction from `P:frequency-row` with row variable \(\eta+\lambda\), output direction reflects \(\lambda\) via actual evenness of \(\nu_R\) and uses symmetry of \(\Phi_h\). Both use their respective Hilbert-Bessel bound from 072. No one-variance substitution. No failed deduction identified.

## PROOF074

**Source:** Proposition `P:wave-square-columns`, `E:variance-square-columns`.

**Statement.** On the same probability space there are deterministic bounded real linear maps
\[
m_{R,I},n_{R,I}:E_{s-\gamma}^{\mathrm{real}}\longrightarrow L^2(\Omega;E_s^{\mathrm{real}}),
\]
each with squared bound \(C_T h^{2-a}B_\alpha(h)\), such that for every fixed real Schwartz pair \(z,w\),
\[
\langle m_{R,I}z,w\rangle_E=\ell_R(I;z,w)
=\langle z,n_{R,I}w\rangle_E\quad\text{in }L^2(\Omega).
\]
Fixed-vector values and finite families of values are centered Gaussian.

**Deductions:** construction via a countable real Schwartz orthonormal basis \((e_k)\) of \(E_s\), phase Parseval in both directions, full Sobolev extension by gain-one coefficient maps. The columns are fixed-interval \(L^2(\Omega;E_s)\) maps; no uncountable a.s. version, random bounded operator, Hilbert–Schmidt realization, time path, or source convergence follows. No failed deduction identified; only the boundary restriction is explicit.

## PROOF075

**Source:** Lemma `L:gaussian-scalar-powers`, `E:gaussian-weighted-power`, `E:gaussian-integer-power`.

**Statement.** For \(0<\theta<1\), \(u,v\ge0\),
\[
u^\theta v^{1-\theta}\le\theta u+(1-\theta)v.
\]
If \(L>0\), \(0\le q\le L\) integer, then
\[
|x|^q|y|^{L-q}\le\frac qL|x|^L+\frac{L-q}L|y|^L.
\]
Finite Hölder holds with exponents \(m>1\), \(m/(m-1)\). If \(Z\ge0\), \(\mathbb E Z=F\), \(0<r<1\), then \(\mathbb E Z^r\le F^r\).

**Deductions:** derivative monotonicity of \(\theta t+1-\theta-t^\theta\); normalization and weighted AM-GM; subpower Jensen with the convexity argument. No failed deduction identified.

## PROOF076

**Source:** Lemma `L:gaussian-trace-bounds`, `E:gaussian-trace-word`, `E:gaussian-trace-holder`.

**Statement.** Let \(B,Y\) be finite Hermitian matrices, \(m\ge2\), \(L=2m-2\). For \(0\le q\le L\),
\[
\operatorname{Re}\operatorname{Tr}\big(BY^qBY^{L-q}\big)
\le\operatorname{Tr}\big(B^2|Y|^L\big).
\]
If \(D\ge0\) is Hermitian,
\[
\operatorname{Tr}\big(D|Y|^{2m-2}\big)
\le(\operatorname{Tr}D^m)^{1/m}
(\operatorname{Tr}|Y|^{2m})^{(m-1)/m}.
\]

**Deductions:** diagonalization of \(Y\), Hermitian symmetry \(b_{ji}=\overline{b_{ij}}\), \(|b_{ij}|=|b_{ji}|\), weighted AM-GM; no commutation \(BY=YB\) assumed. The second bound uses unitary-coupling diagonal convexity plus finite Hölder. No failed deduction identified.

## PROOF077

**Source:** Proposition `P:finite-gaussian-matrix`, `E:finite-gaussian-average`, `E:finite-gaussian-maximum`.

**Statement.** Let \(A_1,\dots,A_N\) be complex \(o\times n\) matrices and \(g_k\) independent real standard Gaussians. Put
\[
X=\sum_k g_kA_k,\qquad V_{\rm out}=\sum_k A_kA_k^*,\qquad
V_{\rm in}=\sum_k A_k^*A_k.
\]
For even \(p=2m\ge2\), with \(\|A\|_{S_p}^p=\operatorname{Tr}((A^*A)^m)\),
\[
(\mathbb E\|X\|_{S_p}^p)^{1/p}
\le\sqrt{p-1}\Big(
\frac{\operatorname{Tr}V_{\rm out}^m+\operatorname{Tr}V_{\rm in}^m}{2}\Big)^{1/p}
\le\sqrt{p-1}\max\big(
\|V_{\rm out}^{1/2}\|_{S_p},\|V_{\rm in}^{1/2}\|_{S_p}\big).
\]
Constants independent of \(o,n,N\); equality at \(p=2\); empty/zero families give zero.

**Deductions:** full Gaussian integration by parts over the noncommuting trace word, then Hermitian dilation
\[
B_k=\begin{pmatrix}0&A_k\\A_k^*&0\end{pmatrix}
\]
with \(D=\operatorname{diag}(V_{\rm out},V_{\rm in})\) and trace identities
\[
\operatorname{Tr}Y^{2m}=2\operatorname{Tr}((X^*X)^m),\quad
\operatorname{Tr}D^m=\operatorname{Tr}V_{\rm out}^m+\operatorname{Tr}V_{\rm in}^m.
\]
Both variance powers are retained; no matrix-entry independence assumed. The 16-coordinate counterexample in `R:gaussian-one-variance-test` gives \(\mathbb E\|X\|_{S_4}^4=288\), refuting the 144 one-variance bound and its transpose. No failed deduction identified.

## PROOF078

**Source:** Lemma `L:cutoff-factorization`, `E:cutoff-periodic-maps`, `E:cutoff-whole-space-recovery`.

**Setup.** Unitary Fourier \(c_d=(2\pi)^{-d/2}\), \(\Lambda=(1-\Delta)^{1/2}\), \(\|u\|_{H^r(\mathbb R^d)}=\|\langle\xi\rangle^r\widehat u\|_2\). Fix real \(\sigma\), real compact smooth \(\chi\), cube \(Q_L=(-L/2,L/2)^d\supset\operatorname{supp}\chi\), \(\psi\in C_c^\infty(Q_L)\) with \(\psi=1\) near \(\operatorname{supp}\chi\). Torus \(\mathbb T_L\) basis
\[
e_k=L^{-d/2}e^{i\kappa_k\cdot x},\quad \kappa_k=2\pi k/L,\quad
\|v\|^2_{H^r(\mathbb T_L)}=\sum_k\langle\kappa_k\rangle^{2r}|v_k|^2.
\]

**Statement.** Periodization of \(\psi u\) and multiplication of a periodic function by \(\chi\) extend to bounded maps
\[
\mathcal P_\psi:H^r(\mathbb R^d)\to H^r(\mathbb T_L),\qquad
\mathcal E_\chi:H^r(\mathbb T_L)\to H^r(\mathbb R^d)
\]
for every real \(r\). If \(\mathcal I_\gamma:H^{\sigma+\gamma}(\mathbb T_L)\to H^\sigma(\mathbb T_L)\) is the identity inclusion,
\[
\mathcal E_\chi\mathcal I_\gamma\mathcal P_\psi u=\chi u,\qquad
u\in H^{\sigma+\gamma}(\mathbb R^d).
\]

**Deductions:** Peetre inequality \((\langle x\rangle/\langle y\rangle)^r\le2^{|r|/2}\langle x-y\rangle^{|r|}\), periodic Fourier kernels \(L^{-d/2}(\langle\kappa_k\rangle/\langle\xi\rangle)^r\widehat\psi(\kappa_k-\xi)\) and \(L^{-d/2}(\langle\xi\rangle/\langle\kappa_k\rangle)^r\widehat\chi(\xi-\kappa_k)\), mixed Lebesgue/counting Schur plus uniform lattice sums. Whole-space recovery is exact through smooth periodic series with \(\chi\psi=\chi\); no rough Fourier point sampling. No failed deduction identified.

## PROOF079

**Source:** Proposition `P:cutoff-singular-values`, `E:cutoff-singular-values`.

**Statement.** For real \(\sigma\), \(\gamma>0\), the initially Schwartz-defined operator
\[
K_{\chi,\sigma,\gamma}=\Lambda^\sigma\chi\Lambda^{-\sigma-\gamma}
\]
extends uniquely to a compact operator on \(L^2(\mathbb R^d)\), and
\[
s_j(K_{\chi,\sigma,\gamma})
\le C_{\chi,\sigma,\gamma,d}\,j^{-\gamma/d},\qquad j\ge1.
\]
Consequently \(K_{\chi,\sigma,\gamma}\in S_p\) whenever \(p\ge1\) and \(p\gamma>d\).

**Deductions:** the factorization through \(\mathcal I_\gamma\) and finite-dimensional projections \(Q_n\mathcal I_\gamma\); rank \((2n+1)^d\); error \(M(2L/\pi)^\gamma j^{-\gamma/d}\); singular-value min-max. No endpoint necessity (\(p\gamma=d\)) and no growing-\(R\) uniform constant are asserted. No failed deduction identified.

## PROOF080

**Source:** Proposition `P:compact-two-envelopes`, `E:compact-balanced-cutoff`, `E:compact-two-factors`, `E:compact-envelope-traces`.

**Setup.** \(E=H^{1/2}\times H^{-1/2}\), \(J_0(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)\), \(H=L^2(\mathbb R^d;\mathbb C^2)\), \(D_\chi\) entrywise spatial multiplication,
\[
P_\chi=J_0D_\chi J_0^{-1},\quad
D_\gamma=\operatorname{diag}(\Lambda^{-\gamma},\Lambda^{-\gamma}),\quad
K_{\rm out}=P_\chi D_\gamma,\quad K_{\rm in}=P_\chi^*D_\gamma.
\]

**Statement.** \(P_\chi\) is bounded. For the unitary swap \(U(v,w)=(w,v)\),
\[
P_\chi^*=UP_\chi U,\qquad K_{\rm in}=UK_{\rm out}U.
\]
Both factors are compact with equal \(S_p\) norms for \(p\ge1\), \(p\gamma>d\). For \(p\ge2\), \(p\gamma>d\),
\[
B_{\rm out}=P_\chi D_\gamma^2P_\chi^*=K_{\rm out}K_{\rm out}^*,\quad
B_{\rm in}=P_\chi^*D_\gamma^2P_\chi=K_{\rm in}K_{\rm in}^*,
\]
satisfy
\[
\operatorname{Tr}B_{\rm out}^{p/2}
=\operatorname{Tr}B_{\rm in}^{p/2}=\|K_{\rm out}\|_{S_p}^p.
\]

**Deductions:** \(P_\chi=\operatorname{diag}(A_{1/2},A_{-1/2})\) with \(A_\sigma=\Lambda^\sigma\chi\Lambda^{-\sigma}\), \(A_\sigma^*=A_{-\sigma}\); one \(S_p\) envelope, not a product; unitary conjugation preserves singular values; positive \(KK^*\)/\(K^*K\) eigenvalues agree with multiplicity. No self-adjointness of \(P_\chi\) assumed. No failed deduction identified.

## PROOF081

**Source:** Lemma `L:compact-positive-order`, `E:compact-positive-trace`.

**Statement.** If \(A,B\) are bounded self-adjoint, \(0\le A\le B\), \(B\) compact positive, then \(A\) is compact and its ordered eigenvalues satisfy \(\lambda_j(A)\le\lambda_j(B)\) with zero padding. For \(t\ge1\) with finite \(\operatorname{Tr}B^t\),
\[
\operatorname{Tr}A^t\le\operatorname{Tr}B^t.
\]

**Deductions:** finite spectral tail projections of \(B\) make \(A^{1/2}\) a norm limit of finite ranks; eigenvalue max-min via Rayleigh quotients. The section expressly says **no** operator inequality \(A^t\le B^t\) for \(t>1\) and no unbounded square-root domain theorem. No failed deduction identified.

## PROOF082

**Source:** Proposition `P:localized-finite-variance`, `E:localized-finite-hypotheses`, `E:localized-two-envelopes`, `E:localized-trace-bounds`.

**Statement.** Suppose finitely many bounded operators \(Z_\ell\) on \(H\) satisfy
\[
P_\chi Z_\ell=Z_\ell=Z_\ell P_\chi,\qquad
V_{\rm out}:=\sum_\ell Z_\ell Z_\ell^*\le CD_\gamma^2,\qquad
V_{\rm in}:=\sum_\ell Z_\ell^*Z_\ell\le CD_\gamma^2.
\]
If \(p\ge2\), \(p\gamma>d\), every \(Z_\ell\in S_p\), the two variances are compact in \(S_{p/2}\), and
\[
V_{\rm out}\le CB_{\rm out},\qquad V_{\rm in}\le CB_{\rm in},
\]
\[
\operatorname{Tr}V_{\rm out}^{p/2},\ \operatorname{Tr}V_{\rm in}^{p/2}
\le C^{p/2}\|K_{\rm out}\|_{S_p}^p.
\]

**Deductions:** positive congruence \(V_{\rm out}=P_\chi V_{\rm out}P_\chi^*\) and \(V_{\rm in}=P_\chi^*V_{\rm in}P_\chi\); compact order from `L:compact-positive-order`. The section states the two localization identities are **hypotheses**, and \(P_\chi\) is **not** assumed self-adjoint or a projection; no actual noise coefficient family has yet been shown to satisfy them (that occurs in 088). No failed deduction identified.

## PROOF083

**Source:** Corollary `C:finite-gaussian-operators`, `E:finite-gaussian-operator-bound`.

**Statement.** Under `E:localized-finite-hypotheses`, let \(g_\ell\) be independent real standard Gaussians. For even \(p\ge2\), \(p\gamma>d\), the finite sum \(X=\sum_\ell g_\ell Z_\ell\) satisfies
\[
(\mathbb E\|X\|_{S_p}^p)^{1/p}
\le\sqrt{p-1}\sqrt C\,\|K_{\rm out}\|_{S_p}.
\]
Its extended norm is measurable with finite expectation.

**Deductions:** finite-rank compression \(\Pi_n\), compressed variance comparison, `P:finite-gaussian-matrix`, passage by operator-norm convergence of \(\Pi_nX\Pi_n\to X\) plus singular-value Fatou. This is a **finite** Gaussian operator bound; it does **not** produce an infinite Gaussian path, \(S_p\)-Bochner convergence, or a random bounded-operator path. No failed deduction identified.

## PROOF084

**Source:** Proposition `P:cutoff-boundary-tests`.

**Statement.** If \(\chi=1\) on a nonempty open set, there is a nonzero rank-one operator satisfying `E:localized-finite-hypotheses` with a finite common \(C\). On the other hand, \(\Lambda^{-\gamma}\) on \(L^2(\mathbb R^d)\) is not compact for any \(\gamma>0\).

**Deductions:** the rank-one witness uses \(P_\chi\widetilde v=\widetilde v\), \(P_\chi^*\widetilde w=\widetilde w\) on the plateau and the Schwartz duality bound
\[
|\langle x,a\rangle|=|\langle D_\gamma x,D_\gamma^{-1}a\rangle|
\le\|D_\gamma x\|\,\|D_\gamma^{-1}a\|.
\]
The noncompactness uses translates of \(g=\Lambda^{-\gamma}f\) and \(\langle T_hg,g\rangle\to0\) by Schwartz decay of \(|\widehat g|^2\). The unlocalized \(\Lambda^{-\gamma}\) no-go is retained; \(\chi\equiv1\) cannot be substituted. No failed deduction identified.

## PROOF085

**Source:** Lemma `L:driver-noise-basis`.

**Statement.** The nonzero space \(H_W\) is separable and infinite-dimensional. It has a real orthonormal basis with compact smooth representatives, whose evaluations \(g_j=W(f_j)\) are independent standard real Gaussians.

**Deductions:** compact-support physical covariance estimate
\[
|\langle F,G\rangle_{H_W}|
\le|K|\Gamma(K-K)\frac{2L^{1-a}}{1-a}
\|\|F(t)\|_\infty\|_{L^2(0,L)}
\|\|G(t)\|_\infty\|_{L^2(0,L)};
\]
strict positivity of \(Q_{\rm sp}\) and of the temporal block norm via the Laplace factorization
\[
\|\tau\|_a^2=\Gamma_E(a)^{-1}\int_0^\infty
\lambda^{a-1}E_\lambda(\tau)\mathrm d\lambda,\quad
E_\lambda(\tau)=\int_\mathbb R2\lambda
\Big|\int_r^\infty e^{-\lambda(t-r)}\tau(t)\mathrm dt\Big|^2\mathrm dr.
\]
The Gaussians arise directly as \(W(f_j)\); no \(H_W\)-valued white vector is introduced. No failed deduction identified.

## PROOF086

**Source:** Lemma `L:driver-covariance-coefficients`, `E:driver-covariance-coefficient`, `E:driver-literal-covariance`.

**Statement.** For each basis representative \(f_j\),
\[
H_{j,R}(t,x)=\zeta_R(x)\int_{u>0}|t-u|^{-a}
\int_{\mathbb R^d}\Gamma(\mathrm dy)f_j(u,x-y)\mathrm du.
\]
These functions are real smooth on finite time-space compact sets, spatially supported in \(B_{2R}\), with bounded derivatives there. For smooth compact real positive-time \(F\), and the admitted wave tests of `E:variance-actual-form`,
\[
\mathbb E\big[W_{\mathbb C}(\zeta_RF)g_j\big]
=\int_{\mathbb R^d\times\mathbb R_+}H_{j,R}(t,x)F(t,x)\mathrm dt\,\mathrm dx.
\]
On \(t\ge0\) the coefficient depends only on the \(H_W\) class of \(f_j\).

**Deductions:** convolution structure after \(v=t-u\); the physical mask \(\zeta_R\) is applied **after** the covariance convolution; representative independence by testing against every compact smooth \(F\). The section warns that moving the mask inside \(\Gamma*f_j\) would change the identity. No failed deduction identified.

## PROOF087

**Source:** Lemma `L:driver-gain-localization`, `E:driver-coefficient-operator`, `E:driver-gain-one`, `E:driver-actual-localization`, `E:driver-covariance-row`.

**Statement.** For \(I\subset[0,T]\),
\[
A_j(I)z=\int_I S(-t)B(H_{j,R}(t))S(t)z\,\mathrm dt.
\]
For every real \(r\),
\[
\|A_j(I)\|_{\mathcal B(E_r,E_{r+1})}\le C_{j,r,R,T}|I|.
\]
Its \(E_s\) adjoint has gain \(E_{2s-r-1}\to E_{2s-r}\), so both \(A_j,A_j^{*,E}\) act \(E_{s-\gamma}\to E\). Choose real compact smooth \(\chi=1\) on \(B_{2R+T+1}\) (this \(P_\chi\) is not self-adjoint/projection). On every \(E_r\),
\[
D_\chi A_j(I)=A_j(I)=A_j(I)D_\chi.
\]
For each fixed Schwartz pair,
\[
\mathbb E[g_j\ell_R(I;z,w)]=\langle A_j(I)z,w\rangle_E.
\]

**Deductions:** bounded wave group on every \(E_r\); multiplier \(H_{j,R}(t)\) bounded on every \(H^r\) continuously in \(t\); dual is \(E_{2s-r}^*\cong E_{2s-r}\); localization by finite propagation forward/backward and support \(B_{2R+T}\); row identity by `E:driver-literal-covariance` plus `E:variance-physical-adjoint`. No operator-norm continuity of the free group or mask-wave commutation is asserted. No failed deduction identified.

## PROOF088

**Source:** Lemma `L:driver-actual-variances`, `E:driver-short-variance-budget`, `E:driver-two-variances`, `E:driver-compact-tail-envelopes`, `E:driver-column-expansions`.

**Setup.** \(J_0(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)\), \(H_0=L^2(\mathbb R^d;\mathbb R^2)\), \(a_j=J_0A_j(I)J_0^{-1}\), \(P_\chi=J_0D_\chi J_0^{-1}\), \(D_\gamma\) as above; for \(I\subset[0,T]\), \(0<h=|I|\le1\),
\[
b_I=C_T h^{2-a}B_\alpha(h).
\]

**Statement.** For every \(N\),
\[
V_{{\rm out},N}:=\sum_{j\le N}a_ja_j^*\le b_ID_\gamma^2,\qquad
V_{{\rm in},N}:=\sum_{j\le N}a_j^*a_j\le b_ID_\gamma^2.
\]
The finite families satisfy both actual localizations by \(P_\chi\). There are bounded positive limits \(V_{{\rm out},\infty},V_{{\rm in},\infty}\) with positive tails \(T_{{\rm out},N},T_{{\rm in},N}\to0\) strongly, and
\[
T_{{\rm out},N}\le b_IB_{\rm out},\qquad T_{{\rm in},N}\le b_IB_{\rm in}.
\]
For each \(z\in E_{s-\gamma}\),
\[
m_{R,I}(z)=\sum_jg_jA_j(I)z,\qquad
n_{R,I}(z)=\sum_jg_jA_j(I)^{*,E}z\quad
\text{in }L^2(\Omega;E).
\]

**Deductions:** the finite families arise from actual projections \(\mathcal P_N\ell_R\) onto the **given** \(W\)-basis, so the raw form is projected **before** phase Parseval; the two variance budgets are derived from the corresponding 073 directions, not from one variance. Extension to \(E_{s-\gamma}\) uses individual gain-one coefficient maps, not summed \(j\)-constants. First chaos is identified from actual linear raw tests, not mere Gaussian law. Complexification is norm-splitting. No failed deduction identified.

## PROOF089

**Source:** Lemma `L:driver-dominated-tails`, `E:driver-trace-tails`.

**Statement.** If \(0\le T_N\le B\), \(B\) positive compact in \(S_m\), \(m\ge1\), and \(T_N\to0\) weakly, then
\[
\|T_N\|\longrightarrow0,\qquad
\operatorname{Tr}T_N^m\longrightarrow0.
\]

**Deductions:** finite spectral projection \(Q\) of \(B\) and positive quadratic Cauchy–Schwarz give norm decay; `L:compact-positive-order` gives \(\lambda_j(T_N)\le\lambda_j(B)\), each tends to zero, dominated \(\ell^m\)-summation. Explicitly no order comparison of operator powers. No failed deduction identified.

## PROOF090

**Source:** Lemma `L:driver-gaussian-tail-average`, `E:driver-retained-gaussian-average`.

**Statement.** Let \(Z_\ell\) be finitely many compact operators with \(V_{\rm out},V_{\rm in}\in S_{q/2}\), \(q\ge2\) even, and \(g_\ell\) independent standard real Gaussians. Then
\[
\mathbb E\Big\|\sum_\ell g_\ell Z_\ell\Big\|_{S_q}^q
\le(q-1)^{q/2}\frac{\operatorname{Tr}V_{\rm out}^{q/2}
+\operatorname{Tr}V_{\rm in}^{q/2}}{2}.
\]

**Deductions:** finite-rank compression preserves the two variance inequalities in the appropriate direction; `P:finite-gaussian-matrix` on the finite block with the average of both trace powers; operator-norm convergence plus singular-value Fatou. No infinite Gaussian series and no \(S_q\)-Bochner convergence are assumed. No failed deduction identified.

## PROOF091

**Source:** Lemma `L:driver-interval-limit`, `E:driver-fixed-schatten`.

**Statement.** For each fixed short interval \(I\), \(X_N(I)\) converges in every finite \(L^p(\Omega;\mathcal B(E))\) to a compact-valued centered Gaussian operator \(X_R(I)\) on the original probability space. For every admissible even \(q\ge2\), \(q\gamma>d\),
\[
(\mathbb E\|X_R(I)\|_{S_q}^q)^{1/q}
\le\sqrt{q-1}\sqrt{C_T}\,h^{1-a/2}B_\alpha(h)^{1/2}
\|K_\chi\|_{S_q},\qquad K_\chi=P_\chi D_\gamma.
\]
Its fixed Schwartz rows equal the actual raw forms in \(L^2\).

**Deductions:** actual finite \(a_j\) satisfy all hypotheses of `P:localized-finite-variance`/`C:finite-gaussian-operators`; by 089 the tail trace powers \(T_{{\rm out},N}^{q/2},T_{{\rm in},N}^{q/2}\to0\); 090 gives a uniform-in-\(M>N\) vanishing \(L^q\) Cauchy bound:
\[
\sup_{M>N}\mathbb E\|Y_{N,M}\|_{S_q}^q
\le(q-1)^{q/2}\frac{\operatorname{Tr}T_{{\rm out},N}^{q/2}
+\operatorname{Tr}T_{{\rm in},N}^{q/2}}{2}\to0.
\]
Since \(\|Y\|\le\|Y\|_{S_q}\), this is genuine \(L^q(\mathcal B(E))\) Cauchy convergence; a uniform moment bound alone is insufficient. The limit is constructed by summable \(L^1\) subsequences in the closed countable span \(\mathcal F_I\) on the original space, avoiding new noise. No failed deduction identified.

## PROOF092

**Source:** Lemma `L:driver-holder-limit`, `E:driver-increment-moments`, `E:driver-dyadic-moment-sum`, `E:driver-holder-interpolation`.

**Statement.** The finite paths \(X_N(t)=X_N((0,t))\) converge in
\[
L^p(\Omega;C^\theta([0,T];\mathcal B(E)))
\]
for every finite \(p\ge1\), in a separable closed path span on the same probability space. The limit starts at zero and has compact values for all times on one path event. For sufficiently large even \(q_0\), its \(C^\theta\) norm has \(L^q\) bound \(C\sqrt q\), uniformly over even \(q\ge q_0\) and the basis.

**Deductions:** choose \(\theta<\eta<\beta\), even \(q_0\ge2\) with \(q_0\gamma>d\) and \(\beta-\eta-1/q_0>0\). The finite increment estimate is
\[
\|X_N(t)-X_N(u)\|_{L^q(\mathcal B(E))}
\le C\sqrt q\,|t-u|^\beta,\qquad|t-u|\le1,
\]
dyadic maximum bound \(2^{n/q}\), fixed-grid \(L^q\) limit **before** mesh limit, then Hölder interpolation \(C^\theta\) between \(\|\cdot\|_\infty\) and \(\|\cdot\|_{C^\eta}\). The separable closed Lipschitz span is the countably generated deterministic span of \(A_j(0,\cdot)\); one probability-one set carries compact values at all times. No failed deduction identified.

## PROOF093

**Source:** Proposition `P:actual-operator-driver`, `E:driver-path-convergence`, `E:driver-raw-row`, `E:driver-gaussian-norm`, `E:driver-fixed-schatten`.

**Statement.** There is an orthonormal basis \(\{f_j\}\) of \(H_W\) with real smooth compact test representatives, independent standard real Gaussians \(g_j=W(f_j)\), and deterministic operators \(A_j(0,t)\) on \(E\) such that
\[
X_N(t):=\sum_{j\le N}g_jA_j(0,t)\ \longrightarrow\ M_R(t)
\quad\text{in }L^p(\Omega;C^\theta([0,T];\mathcal B(E)))
\]
for every finite \(p\ge1\). The limit is a centered Gaussian path on the original probability space, starts at zero, and has compact values at every time on one probability-one path set. For each fixed real Schwartz pair \(z,w\) and \(t\in[0,T]\),
\[
\langle M_R(t)z,w\rangle_E=\ell_R((0,t);z,w)\quad\text{in }L^2(\Omega).
\]
Long raw intervals are the completed test, equivalently the additive unit-interval construction. Different compact smooth test bases give indistinguishable paths on the same \(W\). For constants \(C,c>0\) depending on fixed data but not the basis or \(p\),
\[
(\mathbb E\|M_R\|_{C^\theta}^p)^{1/p}\le C\sqrt p,\qquad
\mathbb E\exp(c\|M_R\|_{C^\theta}^2)<\infty.
\]
The complexification has the sesquilinear raw identity. Fixed-interval Schatten moments hold at admissible even indices in `E:driver-fixed-schatten`; arbitrary \(p\) refers to \(\mathcal B(E)\), not arbitrary Schatten indices or a Schatten-valued path.

**Deductions:** assembled from 085–092 on the same probability space; fixed-time values agree with interval limits by uniqueness in probability; basis independence via a countable dense Schwartz phase collection and rational times plus one countable null-set union. No failed deduction identified; the explicit boundary is that all constants may depend on \(R,T\), with **no** uniform-in-\(R\) path-norm estimate and no \(C^\theta S_q\)-valued path.

## APPLICATION-GAUSSIAN-DRIVER

The analytic chain, with every needed hypothesis/domain and with the order of limits, is:

**(073 → 074)** For \(I\subset[0,T]\), \(0<h=|I|\le1\), the raw complex/fied form \(\ell_R\) admits actual wave tests and satisfies the two Hilbert-Bessel variance bounds:
\[
\sum_k\mathbb E|\ell_R(I;e_k,z)|^2,\quad
\sum_k\mathbb E|\ell_R(I;z,e_k)|^2
\le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2.
\]
Phase Parseval builds two deterministic linear maps
\[
m_{R,I},n_{R,I}:E_{s-\gamma}^{\mathrm{real}}\to L^2(\Omega;E_s^{\mathrm{real}})
\]
with the same squared bound. Boundary: these are fixed-interval \(L^2(\Omega;E)\) maps, not random bounded operators or time paths.

**(074 → 088)** Choose the \(W\)-basis \((f_j)\), \(g_j=W(f_j)\). Coefficient operators come through the physical covariance identity and adjoint/duality:
\[
A_j(I)z=\int_I S(-t)B(H_{j,R}(t))S(t)z\,\mathrm dt,\quad
\mathbb E[g_j\ell_R(I;z,w)]=\langle A_j(I)z,w\rangle_E.
\]
Projecting the actual raw form onto the finite basis gives
\[
X_N(I)=\sum_{j\le N}g_jA_j(I).
\]
Both variance directions of 073 give the operator budgets
\[
V_{{\rm out},N}=\sum_{j\le N}a_ja_j^*\le b_ID_\gamma^2,\qquad
V_{{\rm in},N}=\sum_{j\le N}a_j^*a_j\le b_ID_\gamma^2,\qquad
b_I=C_T h^{2-a}B_\alpha(h).
\]
Localization from deterministic finite propagation gives \(P_\chi a_j=a_j=a_jP_\chi\), with \(P_\chi=J_0D_\chi J_0^{-1}\) **not** self-adjoint/projection. The first chaos is the closed linear chaos of \(W\), identified from actual linear raw tests, not merely from Gaussian law.

**(077, 083 finite operators)** These finite column families satisfy `P:localized-finite-variance` (082). Hence \(X_N(I)\) obeys
\[
(\mathbb E\|X_N(I)\|_{S_q}^q)^{1/q}
\le\sqrt{q-1}\sqrt{C_T}h^{1-a/2}B_\alpha(h)^{1/2}\|K_\chi\|_{S_q}
\]
for even \(q\ge2\), \(q\gamma>d\), with 077 providing the rectangular Hermitian dilation and the average of both variance powers. This is finite-operator moment control only; no infinite Gaussian path follows from this step.

**(088 → 089, 090 trace-tail decay)** Positive tails satisfy
\[
T_{{\rm out},N}\le b_IB_{\rm out},\qquad T_{{\rm in},N}\le b_IB_{\rm in}
\]
with \(B_{\rm out},B_{\rm in}\) compact in \(S_{q/2}\). Since \(T_N\to0\) strongly, 089 gives norm and trace-power decay:
\[
\|T_N\|\to0,\qquad
\operatorname{Tr}T_{{\rm out},N}^{q/2},\ \operatorname{Tr}T_{{\rm in},N}^{q/2}\to0.
\]
090 retains the average of **both** trace powers, yielding the uniform vanishing tail used for genuine \(L^q\) Cauchy convergence.

**(091 operator Cauchy)** For \(M>N\),
\[
\sup_{M>N}\mathbb E\|Y_{N,M}\|_{S_q}^q
\le(q-1)^{q/2}\frac{\operatorname{Tr}T_{{\rm out},N}^{q/2}
+\operatorname{Tr}T_{{\rm in},N}^{q/2}}{2}\to0,
\]
and \(\|\cdot\|_{\mathcal B(E)}\le\|\cdot\|_{S_q}\). This produces an actual \(L^q(\mathcal B(E))\) Cauchy property; a uniform moment bound alone is explicitly insufficient. The limit \(X_R(I)\) is compact-valued, centered Gaussian, strongly measurable, and lies in the separable countable span \(\mathcal F_I\) on the **original** probability space; raw rows equal \(\ell_R(I;\cdot,\cdot)\) in \(L^2\).

**(092, 093 separable Banach path)** For the nested time path \(X_N(t)=X_N((0,t))\),
\[
\|X_N(t)-X_N(u)\|_{L^q(\mathcal B(E))}
\le C\sqrt q\,|t-u|^\beta,\qquad|t-u|\le1,
\]
\[
\|D_n(X_N)\|_{L^q}\le2^{n/q}C\sqrt q\,(T2^{-n})^\beta.
\]
The chain requires \(\theta<\eta<\beta\), an even \(q_0\) with \(q_0\gamma>d\) and \(\beta-\eta-1/q_0>0\) so the dyadic series ratio is \(<1\). The fixed-grid limit is taken **before** the mesh limit, then Hölder interpolation
\[
\|F\|_{C^\theta}\le C\|F\|_\infty^{1-\theta/\eta}\|F\|_{C^\eta}^{\theta/\eta}.
\]
The path limit \(M_R\) is strongly measurable in the separable closed Lipschitz span generated by the countably many deterministic \(A_j(0,\cdot)\) on the same \((\Omega,\mathcal A,P)\). One probability-one set gives compact operator values at **all** times; Gaussianity is through finite linear functionals; exponential integrability follows from \(L^{2m}\) control via \(m!\ge(m/e)^m\).

**Strong measurability / separable Polish support.** The finite paths \(X_N\) are finite Gaussian sums of deterministic continuous operator paths, hence strongly measurable with separable range. The limit is obtained by almost surely \(C^\theta\)-convergent subsequences inside a separable closed span, so \(M_R\) is strongly measurable and its law is concentrated on a separable Banach subspace of \(C^\theta([0,T];\mathcal B(E))\). The law of a Gaussian random element in a separable Banach space is Radon (standard Gaussian-in-separable-Banach-space fact); this is the only standard Radon-law fact used. It is **not** promoted to AWS/Cameron image, minimal quotient norm, tube concentration, Young flow, source-cutoff convergence, or moment theorems. No unbounded square-root operator domain claim is made; all square-root statements concern bounded positive operators and compact positive FORM order.

## GLOBAL-UNPROVED-CONDITIONS

1. **065 is not bypassed.** Multiplication by the physical mask \(\zeta_R\) does not descend to the original noise quotient; the auxiliary quotient norm is \(R,\zeta\)-dependent and the original and auxiliary test norms need not dominate one another. The \(d=2,\alpha=1\) null-mask obstruction stands.

2. **Localization is a genuine standing hypothesis.** `P:localized-finite-variance` assumes \(P_\chi Z_\ell=Z_\ell=Z_\ell P_\chi\). \(P_\chi\) is not self-adjoint and not a projection; the compact cutoff cannot be replaced by \(\chi\equiv1\), whose unlocalized operator is noncompact.

3. **Only finite Gaussian operators exist before 091.** `C:finite-gaussian-operators` is a finite matrix/compression result. There is no infinite Gaussian series, no \(S_p\)-valued path, and no random bounded-operator path produced by 077/083 alone.

4. **The Cauchy property is trace-tail driven, not a uniform moment bound.** 089+090 supply the required vanishing \(S_q\)-moment tails; a uniform moment bound by itself is declared insufficient for the operator-norm Cauchy passage.

5. **No uniform-in-\(R\) path norm.** All constants in 085–093 may depend on \(R,T\). There is no uniform-in-\(R\) \(C^\theta\)-norm estimate and no \(C^\theta S_q\)-valued path; only fixed-interval Schatten moments at admissible even indices are asserted.

6. **No Schatten-valued time path.** Arbitrary \(p\) in the path bound refers to \(\mathcal B(E)\), not to Schatten indices, growing uniform \(R\)-norms, or Schatten-valued path regularity.

7. **Fixed interval vs. countably-nested path.** The deterministic unit-interval additivity is proved only for fixed intervals and fixed partitions; no uncountable intersection of independently selected null sets and no long-interval short-\(h\) bound are claimed.

8. **Branch independence / no self-circularity.** The raw operator branch (061–093) is independent of the fixed-order Stratonovich source branch; it does **not** import 006/009/mild parents or use any later \(C_2\) closure. The 088 projection is onto the given \(W\)-basis before phase Parseval, and both variance tails are necessary; no hidden circular use of the final constant, no new noise, and no replacement source is introduced.

9. **Falsification items retained within scope:**
- legal zero/singular/axis/plane covariances are allowed in the mask/spectral lemmas;
- 065 strictly-positive masked variance for a legal null test;
- 071 continuous zero-frequency matrix \(\begin{pmatrix}-t&-t^2\\1&t\end{pmatrix}\) is used, never division by zero;
- 077 sixteen coordinate rows give \(\mathbb E\|X\|_{S_4}^4=288\), refuting the one-variance \(144\) and its transpose;
- the trace word is noncommuting (\(B,Y\) not assumed to commute);
- \(P_\chi\) is nonselfadjoint;
- 084 retains the unlocalized \(\Lambda^{-\gamma}\) noncompactness no-go;
- 088/091/092 retain projection-order, both variance-tail necessity, correlated dyadic increments, fixed-grid-before-mesh limit, and the \(q\)-margin condition \(q_0\gamma>d\), \(q_0(\beta-\eta)>1\).