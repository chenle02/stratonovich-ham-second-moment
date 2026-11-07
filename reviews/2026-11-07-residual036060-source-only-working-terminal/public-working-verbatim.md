## PROOF036

**Statement (Lemma `L:physical-spectral-energy`).** Let \(\Xi\) be a nonnegative, even, positive-definite tempered Radon covariance on \(\mathbb R^3\) with
\[
\Xi(rA)=r^{3-\chi}\Xi(A),\qquad 0<\chi<2,
\]
and let \(\mu_\Xi\) be its positive even spectral measure in the convention
\[
\Xi=\int_{\mathbb R^3}e^{i\xi\cdot x}\mu_\Xi(d\xi),\qquad
\widehat h(\xi)=\int_{\mathbb R^3}e^{-i\xi\cdot x}h(x)dx .
\]
For every real \(g\in W^{1,2}(\mathbb R^3)\),
\[
\mathcal Q_\Xi(g):=\int_{\mathbb R^3}\int_{\mathbb R^3}g(y+z)^2g(y)^2\,dy\,\Xi(dz)
=\int_{\mathbb R^3}|\widehat{g^2}(\xi)|^2\mu_\Xi(d\xi)<\infty ,
\tag{E:physical-spectral-energy}
\]
independently of the Borel representative of \(g\), and there is a finite \(C_0=C_0(\Xi)\ge0\) with
\[
\mathcal Q_\Xi(g)\le \tfrac12\|g\|_2^2\|\nabla g\|_2^2+C_0\|g\|_2^4 .
\tag{E:energy-quartic-bound}
\]

**Supplied deductions.**
1. Fourier uniqueness gives \(\mu_\Xi(rA)=r^\chi\mu_\Xi(A)\); the finite unit-ball mass and
\[
\int_{\mathbb R^3}\frac{\mu_\Xi(d\xi)}{1+|\xi|^2}
\le \mu_\Xi(B_1)+2^\chi\mu_\Xi(B_1)\sum_{j\ge0}2^{j(\chi-2)}<\infty
\]
verify Dalang’s condition.
2. For real Schwartz \(f\) set \(Q(f)=\mathcal E(f^2)\), \(\mathcal E(h)=\int|\widehat h|^2\mu_\Xi(d\xi)\).
3. **Imported premise** (quartic, not square-root): the closing finiteness assertion of Chen2023 Theorem 1.1 restricted to real unit-\(L^2\) Schwartz profiles gives a finite \(C_0\ge0\) with
\[
Q(g)\le \tfrac12\|\nabla g\|_2^2+C_0,\qquad \|g\|_2=1 .
\]
This imports the variation finiteness for the quartic functional in the closed \(H^1\) test class, not the square-root \(\mathcal M\) in Chen–Hu (1.11).
4. Quartic homogeneity
\[
Q(f)=\|f\|_2^4\,Q\!\left(f/\|f\|_2\right)
\le \tfrac12\|f\|_2^2\|\nabla f\|_2^2+C_0\|f\|_2^4 .
\]
5. **Two different Cauchy–Schwarz inequalities** are used:
   - spectral CS on the pairing
\[
P(f,h)=\int_{\mathbb R^3}\Xi(dz)\int_{\mathbb R^3}f(y+z)^2h(y)^2dy
=\int \widehat{f^2}(\xi)\overline{\widehat{h^2}(\xi)}\mu_\Xi(d\xi)
\le Q(f)^{1/2}Q(h)^{1/2},
\]
with evenness removing the sign of the Fourier convention;
   - CS on the positive \(\sigma\)-finite measure \(dy\,\Xi(dz)\) applied to \(A_f(y,z)=f(y+z)f(y)\), giving
\[
\mathcal E(fh)=\int\Xi(dz)\int f(y+z)f(y)h(y+z)h(y)dy
\le Q(f)^{1/2}Q(h)^{1/2}.
\]
6. With \(N(f)^2=\|f\|_2^2+\|\nabla f\|_2^2\), both estimates give
\[
\|A_f-A_h\|_{L^2(dy\,\Xi)}\le D\,(N(f)+N(h))\,N(f-h),
\]
\[
\|B_f-B_h\|_{L^2(\mu_\Xi)}\le D\,(N(f)+N(h))\,N(f-h),\qquad
B_f=\widehat{f^2}.
\]
7. Choose real Schwartz \(f_n\to g\) in \(W^{1,2}\). Both sequences are Cauchy in their \(L^2\) spaces. Along an a.e. subsequence,
\[
f_n(y+z)f_n(y)\to g(y+z)g(y)\quad (dy\,\Xi(dz))\text{-a.e.}
\]
by translation-invariance and \(\sigma\)-finite Fubini. **Representative independence** follows because changing \(g\) on a Lebesgue-null set changes the product only on a \(dy\,\Xi(dz)\)-null set.
8. For the Fourier side, \(\|f_n^2-g^2\|_1\to0\) gives \(\widehat{f_n^2}\to\widehat{g^2}\) uniformly, so the strong \(L^2(\mu_\Xi)\) limit equals \(B_g\). Passing \(\|A_{f_n}\|^2=Q(f_n)=\|B_{f_n}\|^2\) and the Schwartz quartic bound proves the statement.

**Falsification check (singular plane \(\Xi\), representative change).** The measure \(dy\,\Xi(dz)\) is \(\sigma\)-finite also when \(\Xi\) is a plane-supported measure, so the a.e. convergence and representative-independence argument do not require a density for \(\Xi\); the only imported nontrivial content is the Schwartz quartic finiteness.

**Remaining premise of 036:** the quartic Schwartz bound \(Q(g)\le\tfrac12\|\nabla g\|_2^2+C_0\) is imported from Chen2023 Theorem 1.1; 036 itself supplies only the Cauchy/Fubini/limit machinery and the \(H^1\) identification.

## PROOF037

**Statement (Lemma `L:phase-contractions`).** Let \(0<\alpha<2\), \(\Gamma\) nonnegative, even, positive-definite tempered Radon on \(\mathbb R^3\), \(\Gamma(rA)=r^{3-\alpha}\Gamma(A)\), and
\[
V=\mu(B_1),\quad M=\Gamma(B_1),\quad
R_\alpha=\frac{\alpha\pi V}{2\sin(\pi\alpha/2)},\quad
c_\Gamma=\frac{(3-\alpha)M}{4\pi},\quad
b_\alpha=2^\alpha+\frac{3^{2-\alpha}}{2-\alpha},\quad
D_\Gamma=c_\Gamma b_\alpha .
\]
For \(\lambda>0\), \(q\in\mathbb R^3\), \(a>0\), \(\epsilon>0\),
\[
\int_{\mathbb R^3}\frac{\mu(d\xi)}{\lambda^2+|q+\xi|^2}
\le R_\alpha\lambda^{\alpha-2},
\tag{E:phase-resolvent}
\]
and, with \(\Gamma_\epsilon=p_{2\epsilon}*\Gamma\),
\[
|T_\epsilon(a,q)|\le D_\Gamma a^{1-\alpha},
\qquad
T_\epsilon(a,q)=\int_{\mathbb R^3}e^{iq\cdot x}\Gamma_\epsilon(x)G_a(dx)
=\int_{\mathbb R^3}\widehat G_a(q+\xi)e^{-\epsilon|\xi|^2}\mu(d\xi).
\tag{E:phase-trace}
\]

**Supplied deductions.**
1. Homogeneity/Fourier uniqueness give \(\mu(B_r)=Vr^\alpha\), no origin atom.
2. Gaussian comparison:
\[
\int e^{-s|q+\xi|^2}\mu(d\xi)
=\int p_{2s}(x)e^{iq\cdot x}\Gamma(dx)
\le\int p_{2s}(x)\Gamma(dx)
=\int e^{-s|\xi|^2}\mu(d\xi).
\]
Multiplying by \(e^{-\lambda^2s}\), integrating in \(s\), and using nonnegative Tonelli gives the resolvent comparison; at \(q=0\),
\[
\alpha V\int_0^\infty\frac{r^{\alpha-1}}{\lambda^2+r^2}dr=R_\alpha\lambda^{\alpha-2}.
\]
3. Fourier Fubini gives the \(T_\epsilon\) identity; \(|T_\epsilon(a,q)|\le T_\epsilon(a,0)\).
4. Radial distributional law \(\Gamma(B_r)=M r^{3-\alpha}\) gives, for nonnegative radial Schwartz \(F\),
\[
\int F(x)\Gamma(dx)=c_\Gamma\int_{\mathbb R^3}F(x)|x|^{-\alpha}dx.
\]
Applying to \(F=G_a*p_{2\epsilon}\), \(T_\epsilon(a,0)\le c_\Gamma\sup_z(G_a*|\cdot|^{-\alpha})(z)\), with the three-region sphere-wave bounds producing \(b_\alpha\).

**Remaining premise of 037:** the elementary spectral integral identity
\[
\int_0^\infty r^{\alpha-1}(1+r^2)^{-1}dr=\pi/(2\sin(\pi\alpha/2))
\]
is an imported calculus identity.

## PROOF038

**Statement (Proposition `P:static-phase-variance`).** Let \(A_\lambda=\lambda^2-\Delta\),
\[
\|(f,g)\|_\lambda^2=\|f\|_2^2+\|A_\lambda^{-1/2}g\|_2^2,
\qquad C_t=\cos(t\sqrt{-\Delta}),
\]
and \(W_\epsilon(x)=W(p_\epsilon(x-\cdot))\) with covariance \(\Gamma_\epsilon\). For real Schwartz \(f,g\), \(w_0(t)=C_t f+G_t*g\), \(Z_0(t)=(w_0(t),\dot w_0(t))\), and
\[
Z_{j+1}(t)=\int_0^t\binom{G_{t-s}*(W_\epsilon Z_{j,u}(s))}{C_{t-s}(W_\epsilon Z_{j,u}(s))}ds,\qquad j=0,1,
\]
as Gaussian-polynomial Bochner integrals at fixed \(\epsilon>0\). Let \(N=\|(f,g)\|_\lambda\). Uniformly in \(\epsilon>0\),
\[
\mathbb E\|Z_1(h)\|_\lambda^2
\le R_\alpha h^2\lambda^{\alpha-2}(1+\lambda^2h^2)^2N^2,
\tag{E:phase-born}
\]
\[
\|\mathbb E Z_2(h)\|_\lambda
\le \frac{D_\Gamma(1+\lambda^2h^2)h^{3-\alpha}}{\lambda(2-\alpha)(3-\alpha)}N .
\tag{E:phase-mean}
\]
With \(\lambda=h^{-1}\) and \(K_\epsilon\) the coefficient of \(\sigma^2\) in the finite polynomial
\[
\mathbb E\|Z_0(h)+\sigma Z_1(h)+\sigma^2 Z_2(h)\|_\lambda^2,
\]
there holds
\[
|K_\epsilon|\le\left(4R_\alpha+\frac{4\sqrt e\,D_\Gamma}{(2-\alpha)(3-\alpha)}\right)
h^{4-\alpha}\|(f,g)\|_{1/h}^2 .
\tag{E:phase-variance}
\]

**Supplied deductions.**
1. In unnormalized Fourier variables with Plancherel measure \((2\pi)^{-3}d\eta\),
\[
a_s(\eta)=\widehat{w_0}(s,\eta),\qquad
e_\lambda(\eta)=|\widehat f|^2+\frac{|\widehat g|^2}{\lambda^2+|\eta|^2},
\]
and Cauchy–Schwarz on the two initial coordinates gives
\[
|a_s(\eta)|^2\le(1+\lambda^2s^2)e_\lambda(\eta).
\]
For \(k_\tau(r)=(\sin(\tau r)/r,\cos(\tau r)/\sqrt{\lambda^2+r^2})\),
\[
|k_\tau(r)|^2\le\frac{1+\lambda^2h^2}{\lambda^2+r^2},\qquad 0\le\tau\le h .
\]
2. Covariance expansion + spatial Plancherel:
\[
\mathbb E\|Z_1(h)\|_\lambda^2
=\frac1{(2\pi)^3}\int d\eta\int\mu_\epsilon(d\xi)
\left|\int_0^h k_{h-s}(|\eta+\xi|)a_s(\eta)ds\right|^2 .
\]
Time Cauchy and 037 yield E:phase-born. **Both displacement and velocity are retained through the two-component \(k_\tau\).**
3. The second-order mean uses whether the contraction kernel is exactly \(G_{s-r}(dx)\Gamma_\epsilon\) with Fourier multiplier \(T_\epsilon(s-r,\eta)\); its operator norm is at most \(D_\Gamma(s-r)^{1-\alpha}\). Under \((u,v)\mapsto(u,A_\lambda^{-1/2}v)\),
\[
\|k_\tau(|D|)\|\le\sqrt{1+\lambda^2h^2}/\lambda,\qquad
\|w_0(r)\|_2\le\sqrt{1+\lambda^2h^2}N,
\]
and
\[
\int_0^h ds\int_0^s(s-r)^{1-\alpha}dr
=\frac{h^{3-\alpha}}{(2-\alpha)(3-\alpha)}
\]
give E:phase-mean.
4. Free phase \(\|Z_0(h)\|_\lambda\le e^{\lambda h/2}N\) via differentiated energy and Gronwall.
5. The full variance coefficient is
\[
K_\epsilon=\mathbb E\|Z_1(h)\|_\lambda^2+2\operatorname{Re}\langle Z_0(h),\mathbb E Z_2(h)\rangle_\lambda .
\]
**Both the squared first-order term and the second-order mean are retained**; the second is not dropped and no sign/monotonicity argument is used. Substituting \(\lambda=h^{-1}\) gives E:phase-variance.

**Falsification check.** A scalar static oscillator with a nonzero second-order mean tests exactly the term \(2\operatorname{Re}\langle Z_0,\mathbb E Z_2\rangle\); the proof retains it, so no arbitrary-phase covariance monotonicity is assumed.

## PROOF039

**Statement (Lemma `L:complex-phase`).** Let \(H\) be complex Hilbert, \(A_0\) bounded nonnegative selfadjoint, \(B\) bounded selfadjoint, \(A_\rho=\rho^2+A_0\), and suppose for \(0<a<1\), \(d>0\),
\[
\|A_\rho^{-1/2}BA_\rho^{-1/2}\|\le d\rho^{a-2},\qquad \rho>0 .
\tag{E:abstract-sandwich}
\]
Define
\[
I_a=\int_0^\infty s^{-1/2}(1+s)^{(a-3)/2}ds,
\qquad
\delta_a=\min\{1/4,\ \pi/(8I_a)\}.
\]
For \(\lambda>0\), \(|z|\le\delta_a\lambda^{2-a}/d\), \(L=A_0-zB\), the phase propagator of \(u''+Lu=0\) satisfies
\[
\|\mathcal M_z(h)\|_{X_\lambda\to X_\lambda}\le 100\,e^{2\lambda h},
\qquad
\|(f,g)\|_{X_\lambda}^2=\|f\|^2+\|A_\lambda^{-1/2}g\|^2,\quad h\ge0.
\tag{E:complex-phase-bound}
\]
The constant is independent of \(H,\|A_0\|,\|B\|\).

**Supplied deductions.**
1. Set \(\delta=\delta_a\), \(L_\lambda=L+\lambda^2\), \(\kappa=(\lambda^2+t)^{1/2}\),
\[
L_\lambda+t=A_\kappa^{1/2}(1-zK_\kappa)A_\kappa^{1/2},\qquad K_\kappa=A_\kappa^{-1/2}BA_\kappa^{-1/2}.
\]
Since \(a-2<0\), \(\|zK_\kappa\|\le\delta\), so invertibility holds and
\[
\|A_\kappa^{1/2}(L_\lambda+t)^{-1}\|\le\frac1{(1-\delta)\kappa},
\qquad
\operatorname{Re}\langle L_\lambda u,u\rangle\ge(1-\delta)\langle A_\lambda u,u\rangle.
\]
2. Principal inverse square roots on the right half-plane and the scalar identity
\[
w^{-1/2}=\frac1\pi\int_0^\infty t^{-1/2}(w+t)^{-1}dt
\]
give for \(Q_z=A_\lambda^{1/2}L_\lambda^{-1/2}\) the exact ordered factorization
\[
A_\lambda^{1/2}\big[(L_\lambda+t)^{-1}-A_\kappa^{-1}\big]
=A_\lambda^{1/2}A_\kappa^{-1/2}(1-zK_\kappa)^{-1}zK_\kappa A_\kappa^{-1/2}.
\]
The four factor norms are \(1,(1-\delta)^{-1},|z|d\kappa^{a-2},\kappa^{-1}\), hence
\[
\|Q_z-1\|\le\frac{|z|d\lambda^{a-2}I_a}{\pi(1-\delta)}\le\frac16,
\qquad
\|Q_z\|\le2,\ \|Q_z^{-1}\|\le2.
\]
Applying to \(L^*=A_0-\overline zB\) and taking adjoints gives all four ordered comparisons
\[
A_\lambda^{1/2}L_\lambda^{-1/2},\ \ L_\lambda^{-1/2}A_\lambda^{1/2},\ \ L_\lambda^{1/2}A_\lambda^{-1/2},\ \ A_\lambda^{-1/2}L_\lambda^{1/2}
\]
of norm at most \(2\). **No commutation of \(A_\lambda\) with \(L\) is used**, only functions of \(L\) commute with each other.
3. Numerical-range parabola: for \(\|u\|=1\), \(s=\|A_0^{1/2}u\|\), optimizing the sandwich at \(\rho=s\) and \(\rho=\lambda\) gives
\[
x+\lambda^2\ge(1-\delta)(s^2+\lambda^2),\qquad
|y|\le2\delta\lambda^{2-a}s^{a},
\qquad
y^2\le \frac{4\delta^2}{1-\delta}\lambda^2(x+\lambda^2)\le\frac13\lambda^2(x+\lambda^2).
\]
Then \(x\ge-\lambda^2/4\), \(|w|\le x+2\lambda^2\), \(|\operatorname{Im}\sqrt w|\le\lambda\).
4. The scalar functions
\[
C_h(w)=\cos(h\sqrt w),\quad
F_h(w)=\sqrt{w+\lambda^2}\,\frac{\sin(h\sqrt w)}{\sqrt w},\quad
H_h(w)=\frac{w}{\sqrt{w+\lambda^2}}\,\frac{\sin(h\sqrt w)}{\sqrt w}
\]
are holomorphic near \(\overline{W(L)}\) with bounds \(e^{\lambda h}\), \(2(1+\lambda h)e^{\lambda h}\), \(2e^{\lambda h}\).
5. The imported bounded-operator Crouzeix–Palencia theorem
\[
\|F(T)\|\le(1+\sqrt2)\sup_{w\in W(T)}|F(w)|
\]
is applied **only to bounded operators** \(L\) at finite cutoffs; no unbounded square-root domain theorem is imported. This yields the four block norms \(3e^{\lambda h}\), \(12(1+\lambda h)e^{\lambda h}\), \(12e^{\lambda h}\), \(12e^{\lambda h}\), whose sum is at most \(100e^{2\lambda h}\).

**Falsification check.** A noncommuting \(2\times 2\) complex example cannot be handled by commuting \(A_\lambda\) with \(L\); the proof's ordered products place functions of \(L\) between root-comparison factors, matching the noncommutative block structure.

**Remaining premise of 039:** the Crouzeix–Palencia theorem itself is imported from the selected 8-page primary packet; \(\delta_a<1\) requires \(I_a<\infty\), which holds for \(0<a<1\).

## PROOF040

**Statement (Lemma `L:fock-form`).** For the covariance and \(R_\alpha\) of 037, fixed \(\epsilon>0\), representation \(W_\epsilon(x)=\sum_{i\ge1}g_i e_i(x)\), Gaussian Hermite-degree projection \(P_N\), and spatial Fourier-band projection \(S_b\),
\[
B_{N,m,b}=P_NS_b\Big(\sum_{i=1}^m g_iM_{e_i}\Big)S_bP_N,\qquad A_\rho=\rho^2-\Delta.
\]
These are bounded selfadjoint operators, and uniformly in \(\epsilon,m,b\),
\[
\|A_\rho^{-1/2}B_{N,m,b}A_\rho^{-1/2}\|
\le d_N\rho^{\alpha/2-2},\qquad
d_N=2\sqrt{N+1}\,\sqrt{R_\alpha}.
\tag{E:fock-sandwich}
\]

**Supplied deductions.**
1. \(e_i(x)=\mathbb E[W_\epsilon(x)g_i]\), \(\sum_i e_i(x)^2=\Gamma_\epsilon(0)=v_\epsilon\), \(|e_i(x)|\le\sqrt{v_\epsilon}\), so each \(M_{e_i}\) is bounded selfadjoint.
2. With \(H_i=A_\rho^{-1/2}M_{e_i}A_\rho^{-1/2}\), Gaussian isometry + spatial Plancherel give
\[
\sum_i\|H_if\|_2^2
=\frac1{(2\pi)^3}\int\frac{|\widehat f(\eta)|^2}{\rho^2+|\eta|^2}
\left(\int\frac{e^{-\epsilon|\xi|^2}\mu(d\xi)}{\rho^2+|\eta+\xi|^2}\right)d\eta.
\]
By 037 the spectral bracket is at most \(R_\alpha\rho^{\alpha-2}\), so
\[
\sum_i H_i^2\le R_\alpha\rho^{\alpha-4}I.
\]
3. Finite sums share the bound; \(S_b\) compression preserves it through \((S_bH_iS_b)^2\le S_bH_i^2S_b\) on the band because \(H_i\) is selfadjoint.
4. Normalized Hermite creation/annihilation identities:
\[
g_i h_{\mathbf a}=\sqrt{a_i+1}\,h_{\mathbf a+e_i}+\sqrt{a_i}\,h_{\mathbf a-e_i}
\]
gives the creation row norm \(\sqrt{k+1}\) on degree \(k\) via \(\sum_i a_i^*a_i=(k+1)I\), and annihilation is its adjoint. Composition with the spatial column \(S_bH_iS_b\), summing over degrees at most \(N\), gives E:fock-sandwich. \(-\Delta\) is bounded on \(S_b\).

## PROOF041

**Statement (Lemma `L:finite-word-cutoff`).** Let \(g_{ij}\) be independent standard Gaussians grouped by color \(i\), let \(J_i=\sum_{j=1}^{m_i}M_{g_{ij}}\otimes K_{ij}\) with bounded \(K_{ij}\), and let \(F_0,\ldots,F_n\) be bounded operators on \(\mathscr X\). For a fixed word \(i_1,\ldots,i_n\), with \(r_i\) the number of occurrences of color \(i\), if \(N_i\ge r_i\) and \(P\) projects each color onto total Hermite degree at most \(N_i\), then for all \(v\in\mathscr X\),
\[
(I\otimes F_n)(PJ_{i_n}P)\cdots(PJ_{i_1}P)(I\otimes F_0)(1\otimes v)
=(I\otimes F_n)J_{i_n}\cdots J_{i_1}(I\otimes F_0)(1\otimes v).
\tag{E:finite-word-cutoff}
\]
The equality holds for finite sums and for Bochner integrals of such words whenever the displayed vector integrals exist.

**Supplied deductions.**
1. Multiplication by \(g_{ij}\) changes only the total degree of color \(i\) by one and leaves other color degrees unchanged; \(F_l\) leaves all degrees unchanged.
2. After the first \(l\) insertions, the color-\(i\) degree of the uncompressed word is \(r_i(l)\le r_i\le N_i\). Induction shows \(P\) is the identity before and after every insertion.
3. **Create-then-annihilate and all self-contractions are retained** because the lowering term \(\sqrt{a_i}h_{\mathbf a-e_i}\) is present in the Hermite multiplication.

This is an equality of selected finite words, not an identity between the full cutoff and uncompressed propagators.

## PROOF042

**Statement (Proposition `P:static-phase-all-orders`).** Under the covariance class of 037, with \(A_\alpha=400\sqrt2\,e^2/\delta_{\alpha/2}\), for \(n\ge1\), uniformly in \(\epsilon>0\),
\[
\|Z_n^\epsilon(h)\|_{L^2(\Omega;X_{1/h})}
\le
\frac{(A_\alpha\sqrt{R_\alpha})^n h^{(4-\alpha)n/2}}{(n!)^{(3-\alpha)/2}}
\|(f,g)\|_{1/h}.
\tag{E:all-static-phase-orders}
\]
For every fixed positive smoothing and real \(\sigma\), \(\sum_{n\ge0}\sigma^nZ_n^\epsilon(h)\) converges in \(L^2\) phase with
\[
\sum_{n\ge0}\sigma^nZ_n^\epsilon(h)
\le
(\sqrt e+2)^2
\exp\left\{6A_\alpha^{2/(3-\alpha)}(|\sigma|^2R_\alpha)^{1/(3-\alpha)}
h^{(4-\alpha)/(3-\alpha)}\right\}\|(f,g)\|_{1/h}^2.
\tag{E:all-static-phase-sum}
\]

**Supplied deductions.**
1. \(R_\alpha=0\) makes the positive-order terms zero; otherwise finite Gaussian-mode \(m\), degree \(N\), band \(b\) are used.
2. 040 and 039 with \(a=\alpha/2\) give the bound \(100e^{2\lambda h}\) on the complex coupling circle of radius \(\delta_{\alpha/2}\lambda^{2-\alpha/2}/d_N\).
3. The four phase entries are entire in the coupling via the power series for \(\cos(h\sqrt L)\), \(\sin(h\sqrt L)/\sqrt L\); Cauchy’s operator-valued formula bounds the \(n\)-th coefficient (the \(n\)-th Duhamel phase) by
\[
100e^{2\lambda h}\left(\frac{d_N}{\delta_{\alpha/2}\lambda^{2-\alpha/2}}\right)^n\|S_b(f,g)\|_\lambda.
\]
4. 041 with one color, \(N=n\), identifies the cutoff word with the uncompressed word, including self-contractions.
5. Choosing \(\lambda=n/h\), using \(\|z\|_{1/h}\le n\|z\|_{n/h}\), \(d_n\le2\sqrt{2n}\sqrt{R_\alpha}\), \(100n\le200^n\), \(n!\le n^n\), gives
\[
\le 100n\left(\frac{2\sqrt2 e^2}{\delta_{\alpha/2}}\right)^n
R_\alpha^{n/2}h^{(4-\alpha)n/2}n^{-(3-\alpha)n/2}\|(f,g)\|_{1/h},
\]
which is E:all-static-phase-orders with \(A_\alpha=400\sqrt2e^2/\delta_{\alpha/2}\).
6. Removal of \(b,m\) is done **at fixed \(\epsilon,n\)** using the unweighted multiplication bound \(2\sqrt{N+1}\sqrt{v_\epsilon}\), the block insertion bound divided by \(\lambda\), free bound \(e^{\lambda h/2}\), strong convergence, and dominated time integration; no zero-smoothing phase limit is asserted.
7. Put \(\beta=(3-\alpha)/2\in(1/2,3/2)\), \(x=A_\alpha|\sigma|\sqrt{R_\alpha}h^{(4-\alpha)/2}\). The elementary bound
\[
\sum_{n\ge0}\frac{x^n}{(n!)^\beta}\le2e^{3x^{1/\beta}}
\]
uses the \(\ell^\beta\) inequality for \(\beta\ge1\) and Hölder with the geometric sequence for \(\beta<1\). Combined with \(\|Z_0(h)\|_{1/h}\le\sqrt e\|(f,g)\|_{1/h}\), this gives E:all-static-phase-sum.

## PROOF043

**Statement (Corollary `C:static-interaction`).** Let \(S_0(t)\) be free phase evolution and for \(\lambda h\le1\),
\[
\mathcal I^\epsilon_\sigma(h)(f,g)=S_0(-h)\sum_{n\ge0}\sigma^nZ_n^\epsilon(h).
\]
Set \(\gamma=3-\alpha\), \(B_\alpha=3eA_\alpha^2\),
\[
L_\alpha(h,\lambda)=4eR_\alpha h^2\lambda^{\alpha-2}
+\frac{4\sqrt eD_\Gamma}{(2-\alpha)(3-\alpha)}\frac{h^{3-\alpha}}{\lambda},
\qquad
x=B_\alpha\sigma^2R_\alpha h^{4-\alpha},
\]
\[
\mathcal E(h,\sigma,\lambda)
=\sigma^2L_\alpha(h,\lambda)+(\lambda h)^{-2}x^2e^{\gamma x^{1/\gamma}}.
\]
Uniformly in \(\epsilon>0\),
\[
\mathbb E\|\mathcal I^\epsilon_\sigma(h)(f,g)\|_\lambda^2
\le[1+\mathcal E(h,\sigma,\lambda)]\|(f,g)\|_\lambda^2.
\tag{E:static-interaction}
\]
If \(0<\alpha_0<1\), \(\alpha+\alpha_0<2\), \(h_j=2^{-j}/\lambda\), \(\sigma_j^2=h_j^{-\alpha_0}\), \(T>0\), then
\[
\sum_{j\ge0}\frac{T}{h_j}\mathcal E(h_j,\sigma_j,\lambda)<\infty.
\tag{E:static-block-series}
\]
For a finite single partition with mutually independent smoothed fields, real \(\sigma_j\), \(\lambda h_j\le1\),
\[
\mathbb E\|\mathcal M_K(h_K)\cdots\mathcal M_1(h_1)(f,g)\|_\lambda^2
\le
\exp\left\{\lambda\sum_{j=1}^K h_j+\sum_{j=1}^K\mathcal E(h_j,\sigma_j,\lambda)\right\}
\|(f,g)\|_\lambda^2.
\tag{E:independent-static-blocks}
\]

**Supplied deductions.**
1. \(Y_n=S_0(-h)Z_n^\epsilon(h)\); the free bound holds in both time directions, and Proposition 038 bounds the complete first variance coefficient of \(\mathbb E\|\sum\sigma^nY_n\|_\lambda^2\) in absolute value by \(L_\alpha(h,\lambda)N^2\), using exactly
\[
\|S_0(-h)\|_\lambda^{-2}\mathbb E\|Z_1\|_\lambda^2
\quad\text{and}\quad
2\operatorname{Re}\langle Z_0,\mathbb E Z_2\rangle . 
\]
2. For \(n\ge1\), \(\lambda h\le1\), E:all-static-phase-orders gives
\[
\|Y_n\|_{L^2(\Omega;X_\lambda)}
\le\frac{\sqrt e}{\lambda h}
\frac{(A_\alpha\sqrt{R_\alpha})^n h^{(4-\alpha)n/2}}{(n!)^{\gamma/2}}N.
\]
3. Gaussian symmetry makes all \(r+s\) odd inner products vanish. For \(r+s=2k\), \(r!s!\ge(k!)^2\), giving the higher-order double-index bound
\[
\le
\frac{e(2k+1)}{(\lambda h)^2}
\frac{(A_\alpha^2R_\alpha)^k h^{(4-\alpha)k}}{(k!)^\gamma}N^2,
\qquad
e(2k+1)\le(3e)^k .
\]
The \(k\ge2\) part is at most
\[
\frac{x^2e^{\gamma x^{1/\gamma}}}{(\lambda h)^2}N^2,
\]
which, with the sharper first-coefficient \(L_\alpha\), proves E:static-interaction.
4. With \(\beta=4-\alpha-\alpha_0>2\), after multiplication by \(T/h_j\), the first-coefficient terms are constant multiples of
\[
T\lambda^{\alpha-2}h_j^{1-\alpha_0},\qquad
\frac T\lambda h_j^{2-\alpha-\alpha_0},
\]
and the higher-order term is
\[
\frac{T(B_\alpha R_\alpha)^2}{\lambda^2}h_j^{2\beta-3}
\exp\{\gamma(B_\alpha R_\alpha)^{1/\gamma}h_j^{\beta/\gamma}\},
\]
with the exponential bounded by its value at \(h_0\). All geometric series converge.
5. Independent blocks: \(\mathcal M_j=S_0(h_j)\mathcal I_j\), with free norm-squared \(e^{\lambda h_j}\), extends to random independent initial phases by tensoring with the past probability space; product and \(1+y\le e^y\) give E:independent-static-blocks.

**Boundary stated explicitly.** The block-series is only the sum of individual upper bounds on one dyadic partition; it does **not** identify an evolution driven by overlapping or repeated fields, and independent blocks are asserted only on one partition.

## PROOF044

**Statement (Lemma `L:interval-contractions`).** In \(d\in\{1,2,3\}\), with homogeneous nonnegative even positive-definite tempered Radon \(\Gamma\), spectral \(\mu\), and
\[
R_\alpha=\frac{\alpha\pi\mu(B_1)}{2\sin(\pi\alpha/2)},
\qquad A_\rho=\rho^2-\Delta,
\qquad
\|(f,g)\|_\rho^2=\|f\|_2^2+\|A_\rho^{-1/2}g\|_2^2 ,
\]
uniformly in positive spatial smoothing and finite mode/band cutoffs,
\[
\sum_m\|A_\rho^{-1/2}M_{e_m}f\|_2^2
\le R_\alpha\rho^{\alpha-2}\|f\|_2^2 .
\tag{E:interval-column}
\]
Consequently, on a color initially in vacuum,
\[
\|(u,v)\mapsto(0,W_\epsilon u)\|\le\sqrt{R_\alpha}\,\rho^{(\alpha-2)/2},
\]
and with Hermite degree \(N\),
\[
\|A_\rho^{-1/2}B_{N,m,b}A_\rho^{-1/2}\|
\le 2\sqrt{N+1}\,\sqrt{R_\alpha}\,\rho^{\alpha/2-2}.
\tag{E:interval-fock}
\]

**Supplied deductions.**
1. Gaussian comparison is dimension-independent:
\[
\int e^{-s|\eta+\xi|^2}\mu(d\xi)
=\int p_{2s}^{(d)}(x)e^{i\eta\cdot x}\Gamma(dx)
\le\int e^{-s|\xi|^2}\mu(d\xi),
\]
using evenness and physical nonnegativity. Integrating against \(e^{-\rho^2s}ds\) gives
\[
\sup_\eta\int\frac{\mu(d\xi)}{\rho^2+|\eta+\xi|^2}\le R_\alpha\rho^{\alpha-2}.
\]
2. Gaussian isometry and unnormalized Plancherel give E:interval-column at each \(\epsilon\); finite mode sums are subsums, and \(S_bA_\rho^{-1}S_b\le A_\rho^{-1}\) extends it to band truncations.
3. The phase insertion bound follows because \(\sum_mg_m(0,M_{e_m}u)\) has squared norm exactly the left side of E:interval-column.
4. Substituting \(A_\rho^{-1/2}f\) gives the selfadjoint sandwiches \(\sum_m(A_\rho^{-1/2}M_{e_m}A_\rho^{-1/2})^2\le R_\alpha\rho^{\alpha-4}I\); adding creation \(\sqrt{j+1}\) and its adjoint over degrees at most \(N\) gives E:interval-fock. All statements tensor with any other Hilbert factor.

## PROOF045

**Statement (Lemma `L:interval-complex`).** Let \(A_0\) be bounded nonnegative selfadjoint, \(V\) bounded, \(A_\rho=\rho^2+A_0\). The conclusion of 039 holds for \(L=A_0-V\) with \(V\) not necessarily selfadjoint whenever
\[
\|A_\rho^{-1/2}VA_\rho^{-1/2}\|\le D\rho^{a-2},\qquad\rho>0,\quad0<a<1,\quad
D\le\delta_a\Lambda^{2-a},
\]
with bound \(100e^{2\Lambda h}\) in \(X_\Lambda\). If the piecewise-constant potential is a sum of connected-interval fields with positive weights \(\omega_i\) and
\[
\Lambda(t)=\lambda+\sum_i\omega_i\mathbf1_{I_i}(t),
\]
then the total loss in changing phase norms, starting and ending in \(X_\lambda\), is at most
\[
\prod_i(1+\omega_i/\lambda).
\tag{E:interval-metric}
\]

**Supplied deductions.**
1. Adjoint sandwich identity gives the same bound for \(V^*\). The form estimate at \(\rho=\Lambda\) gives \(\operatorname{Re}\langle(L+\Lambda^2)u,u\rangle\ge(1-\delta_a)\langle A_\Lambda u,u\rangle\), so shifted operator and adjoint have right-half-plane spectra.
2. With \(K_\kappa=A_\kappa^{-1/2}VA_\kappa^{-1/2}\), \(\kappa=(\Lambda^2+t)^{1/2}\),
\[
(L+\Lambda^2+t)^{-1}-A_\kappa^{-1}
=A_\kappa^{-1/2}(1-K_\kappa)^{-1}K_\kappa A_\kappa^{-1/2},
\]
giving the same inverse-root \(1/6\) bound; adjoints are taken under the norm-convergent resolvent integral, and the four ordered comparisons are bounded by \(2\).
3. For \(\|u\|=1\), \(s=\|A_0^{1/2}u\|\), the form estimates at \(\rho=\Lambda\) and \(\rho=s\) give
\[
|\langle Vu,u\rangle|\le D\Lambda^{a-2}(s^2+\Lambda^2),\qquad
|\langle Vu,u\rangle|\le2Ds^a,
\]
hence the same numerical-range parabola. Crouzeix–Palencia and the scalar bounds apply **without selfadjointness of \(V\) and without commuting \(A_\Lambda\) with \(L\)**. The four block norms sum to \(100e^{2\Lambda h}\).
4. Metric identity: \(\|z\|_{\rho_{new}}\le\max\{1,\rho_{old}/\rho_{new}\}\|z\|_{\rho_{old}}\). At a jump, the ratio is at most
\[
\frac{\lambda+\sum_R\omega_i+\sum_E\omega_i}
{\lambda+\sum_R\omega_i+\sum_S\omega_i}
\le1+\sum_E\omega_i/\lambda
\le\prod_E(1+\omega_i/\lambda).
\]
An initial increase has no loss; the final return to \(X_\lambda\) is charged as an ending jump at \(T\), and each connected interval ends once.

**Falsification check.** For a noncommuting \(2\times 2\) complex potential, the four ordered products in 039 remain valid because \(L_\lambda^{-1/2}A_\lambda^{1/2}\) and \(A_\lambda^{-1/2}L_\lambda^{1/2}\) are estimated by adjoints, not by commuting \(A_\lambda\) with \(L\).

## PROOF046

**Statement (Lemma `L:inventory-product`).** For \(k\ge1\), with \(\beta=4-\alpha-\alpha_0,\ \nu=3-\alpha,\ p=2-\alpha_0\),
\[
v_i=i^{-\beta}+k^{-1}i^{-(\beta-1)}+k^{\alpha-2}i^{-p},
\qquad
b_{i,l}=\frac{i^{-\beta l}(1+li/k)^2}{(l!)^\nu},\quad l\ge2,
\]
there is a finite \(C=C(\alpha,\alpha_0)\), independent of \(M,k\), with
\[
[z^k]\prod_{i=1}^M\left(1+v_iz+\sum_{l\ge2}b_{i,l}z^l\right)
\le\frac{C^k}{(k!)^\nu}.
\tag{E:inventory-product}
\]

**Supplied deductions.** Evaluate at \(z=\theta k^\nu\), \(\theta=1/4\):
1. \(P_i=\theta k^\nu i^{-\beta}\), \(Q_i=\theta k i^{-p}\), the third singleton term being \(Q_i\) because \(\nu+\alpha-2=1\).
2. \(1+A+B\le(1+A)(1+B)\) separates \(1+Q_i\); for \(p>1\),
\[
\sum_{i\ge1}\log(1+Ai^{-p})\le A^{1/p}\int_0^\infty\log(1+x^{-p})dx\le Ck.
\]
3. For \(i\le k\), \(S_\nu(4P_i)\) with \(\nu>1\) gives
\[
\sum_{i\le k}\log S_\nu(4P_i)
\le\nu(4\theta)^{1/\nu}k\sum_{i\ge1}i^{-\beta/\nu}\le Ck.
\]
4. For \(i>k\), the singleton tail and the uniform bound
\[
\sum_{l\ge2}P^l(1+ly)^2/(l!)^\nu\le CP^2(1+y^2)
\]
give logarithmic contributions \(Ck^{\alpha_0}\) and \(Ck^{2\alpha_0-1}\), both at most \(Ck\). The product is at most \(e^{Ck}\), so positivity of coefficients gives
\[
[z^k]\le\theta^{-k}k^{-\nu k}e^{Ck}\le C^k/(k!)^\nu .
\]
No multinomial is required.

## PROOF047

**Statement (Lemma `L:fixed-split`).** Given finite connected intervals \(I_i\subset[0,T]\), lengths \(h_i\) decreasing, independent copies \(W_i^\epsilon\), and
\[
h_i\le L T/i,\qquad \sigma_i^2\le c\,h_i^{-\alpha_0},
\]
let
\[
\mathcal U^\epsilon_{\mathcal F}(T;s)
\]
be the phase evolution with potential \(s\sum_i\sigma_i\mathbf1_{I_i}(t)W_i^\epsilon(x)\). With \(R_\alpha>0,\sigma_i>0\), integers \(r_i,q_i,k_i\ge0\), \(r_i+q_i=2k_i\), \(k=\sum k_i\ge1\), \(\lambda=k/T\), modal/band/Hermite cutoffs \(m_i,S_b,N_i=2k_i\) and \(P=\bigotimes_iP_{N_i}\),
\[
B_i=P S_b\Big(\sum_{j=1}^{m_i}g_{ij}M_{e_{ij}}\Big)S_bP,
\qquad
V_{\mathbf z}(t)=\sum_i z_i\sigma_i\mathbf1_{I_i}(t)B_i ,
\]
\[
\mathcal I=\{i:k_i>0\},\quad
\mathcal C=\{i:k_i=1,r_i=q_i=1\},\quad
\mathcal B=\mathcal I\setminus\mathcal C,\quad
\ell_i=\mathbf1_{r_i>0}+\mathbf1_{q_i>0}.
\]
With \(U_{\mathbf r}v=[\mathbf z^{\mathbf r}]\mathcal M^{cut}_{\mathbf z}(T)v\), there is a finite \(C_{\rm split}=C_{\rm split}(\alpha)\) uniform in all cutoffs and the inventory such that
\[
\begin{split}
|\langle U_{\mathbf r}v,U_{\mathbf q}v\rangle_{L^2(\Omega;X_{1/T})}|
\le k^2 C_{\rm split}^k R_\alpha^k\|v\|^2_{1/T}
&\prod_{i\in\mathcal C}(\sigma_i^2h_i^2\lambda^{\alpha-2})
\\&\times
\prod_{i\in\mathcal B}\frac{(\sigma_i^2h_i^{4-\alpha})^{k_i}}{(k_i!)^\nu}
(1+k_i/(\lambda h_i))^{\ell_i}.
\end{split}
\tag{E:fixed-split-bound}
\]

**Supplied deductions.**
1. Active intervals have positive-length intersections \(I_i^T\) with \((0,T)\); zero-length intersections give zero coefficients. With \(a=\alpha/2\), \(\omega_i=k_i/h_i\), \(d_i=2\sqrt{2k_i+1}\sqrt{R_\alpha}\), \(\varrho_i=\delta_a\omega_i^{2-a}/(\sigma_id_i)\) for \(i\in\mathcal B\).
2. **Background segments.** For \(\Lambda(t)=\lambda+\sum_{i\in\mathcal A}\omega_i\mathbf1_{I_i^T}\), 044 gives
\[
\|A_\rho^{-1/2}V_z(t)A_\rho^{-1/2}\|\le D(t)\rho^{a-2},\qquad
D(t)\le\delta_a\Lambda(t)^{2-a}.
\]
A common partition from cross insertion times and background endpoints has at most \(3k+1\) segments; 045 gives the product bound
\[
M_k=100^{3k+1}e^{4k}.
\]
3. **Phase-weight identity.** At each ending cut,
\[
\prod_j q_j\le D_{\mathcal A}=\prod_{i\in\mathcal A}(1+k_i/(\lambda h_i)),
\]
charging each connected interval exactly once; insertion-only cuts and interval starts add no new copy.
4. **Cross-sector subspaces.** For \(i\in\mathcal C\), the fresh color has \((r_i,q_i)=(1,1)\); the vacuum/first-degree subspace \(\mathscr Z_S\) carries the input, giving
\[
\|J_i\|\le\sigma_i\sqrt{R_\alpha}\Lambda(t_i)^{(\alpha-2)/2}
\le\sigma_i\sqrt{R_\alpha}\lambda^{(\alpha-2)/2}.
\]
This allows arbitrary background/earlier-color dependence while using only fresh-color vacuum.
5. **Insertion cube without \(m!\).** Variation of constants gives
\[
\Phi_{\mathcal A}(z)=\sum_\pi\int_{D_\pi}\mathcal W_{\mathcal A}(z,t)v\,dt,
\qquad
\sum_\pi|D_\pi|=\prod_{i\in\mathcal C}|I_i^T|\le\prod_{i\in\mathcal C}h_i.
\]
Minkowski and the single-word product give
\[
\|\Phi_{\mathcal A}(z)\|_\lambda\le M_kD_{\mathcal A}\|v\|_\lambda
\prod_{i\in\mathcal C}\sigma_i\sqrt{R_\alpha}h_i\lambda^{(\alpha-2)/2}.
\]
Vector Cauchy on the background polytorus extracts \(U_{\mathbf r}v\) **before** any inner product.
6. **Radii and factorial bookkeeping.** Cauchy–Schwarz between the two copies gives the prefactor \(k^2M_k^2D_{\mathcal A_r}D_{\mathcal A_q}\), the radius exponents \(r_i+q_i=2k_i\), and, for \(i\in\mathcal B\),
\[
\varrho_i^{-2k_i}\le(12\delta_a^{-2})^{k_i}
\frac{(R_\alpha\sigma_i^2h_i^{4-\alpha})^{k_i}}{(k_i!)^{3-\alpha}}.
\]
The metric product is exactly \(D_{\mathcal A_r}D_{\mathcal A_q}=\prod_{i\in\mathcal B}(1+k_i/(\lambda h_i))^{\ell_i}\), with \(\ell_i=1\) for a singleton on one copy and at most \(2\) for higher colors. Finally
\[
M_k^2=100^{6k+2}e^{8k}\le(100^8e^8)^k,\qquad
|\mathcal C|+\sum_{i\in\mathcal B}k_i=k,
\]
and
\[
C_{\rm split}=100^8e^8\max\{1,12\delta_{\alpha/2}^{-2}\}.
\]

**Falsification check.** Cross colors use only \((1,1)\) insertions on two separate copies; occupied singletons are background colors with Hermite cutoff \(N_i=2\), not fresh vacuums. Simultaneous endpoints are assigned to one partition choice and form a null set.

## PROOF048

**Statement (Proposition `P:interval-coefficients`).** There is \(C=C(\alpha,\alpha_0,L,c)\) such that for every real Schwartz phase \(v\), \(k\ge1\),
\[
\left|[s^{2k}]\mathbb E\|\mathcal U^\epsilon_{\mathcal F}(T;s)v\|_{1/T}^2\right|
\le\frac{C^kR_\alpha^k T^{\beta k}}{(k!)^\nu}\|v\|_{1/T}^2,
\tag{E:interval-coefficient-bound}
\]
uniformly in \(\epsilon>0\) and the finite family, and hence
\[
\mathbb E\|\mathcal U^\epsilon_{\mathcal F}(T;1)v\|_{1/T}^2
\le e\exp\{C R_\alpha^{1/\nu}T^{\beta/\nu}\}\|v\|_{1/T}^2.
\tag{E:interval-phase-bound}
\]

**Supplied deductions.**
1. Enlarge \(L\) to \(\max(1,L)\); replace \((\sigma_i,W_i^\epsilon)\) by \((|\sigma_i|,\operatorname{sgn}(\sigma_i)W_i^\epsilon)\).
2. **Entire-majorant identification** at fixed finite family/\(\epsilon\) with \(v_{\max}<\infty\):
\[
\|U_n\|\le e^{\lambda T/2}\frac{(2z_*\sqrt{n+1}\sqrt{v_{\max}}T/\lambda)^n}{n!}\|v\|_\lambda .
\]
The coefficientwise absolute convergence is bounded by \(4^{|\mathcal F|}K_{2z_*}^2\); \(v_{\max}\) is used **only for this finite-smoothed identification, not as a uniform constant**.
3. Reflection parity \(U_{\mathbf r}\mapsto(-1)^{r_i}U_{\mathbf r}\) gives \(Q_{\mathbf r,\mathbf q}=0\) unless \(r_i+q_i=2k_i\), \(\sum k_i=k\), with \(\prod_i(2k_i+1)\le3^k\) splits.
4. Hermite cutoffs \(N_i=2k_i\) preserve both selected coefficients exactly by 041; creation-then-annihilation is retained.
5. Applying 047 with \(\lambda=k/T\) and absorbing \(k^2C_{\rm split}^k3^kc^k\) (using \(k^2\le4^k\)) gives local energy weights:
\[
\begin{array}{c|c}
\text{case}&\text{weight}\\ \hline
(2,0),(0,2)&R_\alpha h_i^\beta(1+1/(\lambda h_i))\\
(1,1)&R_\alpha\lambda^{\alpha-2}h_i^{2-\alpha_0}\\
k_i=l\ge2&R_\alpha^l h_i^{\beta l}(1+l/(\lambda h_i))^2/(l!)^\nu .
\end{array}
\]
Here the first metric factor occurs on one copy only and the last on at most one per copy; **whole increasing length weights are used, never an inverse \(h_i\)-factor alone**.
6. Substituting \(h_i\le LT/i\), \(\lambda=k/T\) leaves exactly \(v_i\) at singleton orders and \(b_{i,l}\) at \(l\ge2\), with no multinomial factor:
\[
\sum_{\sum k_i=k}\prod_i w_{i,k_i}
=[z^k]\prod_i\Big(\sum_{l\ge0}w_{i,l}z^l\Big).
\]
046 gives E:interval-coefficient-bound.
7. Summation uses \(x=CR_\alpha T^\beta\), \(Y=e^{\nu x^{1/\nu}}\), and \(\sum_{k\ge0}x^k/(k!)^\nu\le Y\).

**Falsification check.** Extremely short intervals are bounded through the increasing \(h_i\)-powers and the inventory tail, not through an isolated \(1/h_i\); the only place \(v_{\max}\) enters is the fixed-\(\epsilon,\mathcal F\) identification of the actual Duhamel series.

## PROOF049

**Statement (Lemma `L:terminal-wick`).** For \(n\ge1\), define the positive terminal-chain measure
\[
\mathbf g_n^{T,x}(d\mathbf s,d\mathbf y)
=\mathbf1_{[0,T]^n_<}(\mathbf s)d\mathbf s
\prod_{j=1}^n G_{s_{j+1}-s_j}(y_{j+1}-dy_j),\qquad
(s_{n+1},y_{n+1})=(T,x),
\]
read backwards from \(x\), with \(\mathbf g_0^{T,x}\) the empty-tuple mass one. Let \(\mathcal W\) be centered Gaussian with covariance \(\mathcal K\), \(V=\sup_{s,y}\mathbb E|\mathcal W(s,y)|^2<\infty\), and mean-square continuity on each cell of a finite partition of \([0,T]\times\mathbb R^d\). Then
\[
Y_n(T,x)=\int\prod_{j=1}^n\mathcal W(s_j,y_j)\,\mathbf g_n^{T,x}(d\mathbf s,d\mathbf y)
\]
are Bochner\(L^2\) integrals with
\[
\|Y_n(T,x)\|_2
\le\sqrt{(2n-1)!!}\,V^{n/2}\frac{T^{2n}}{(2n)!},
\tag{E:terminal-term-majorant}
\]
and for \(m+n=2k\),
\[
\mathbb E[Y_m(T,x)Y_n(T,x)]
=\sum_{D\in\Pi_k}\mathcal T^{\mathcal K}_{m,n,D}(T,x),
\tag{E:terminal-wick-formula}
\]
where
\[
\begin{split}
\mathcal T_{m,n,D}^{\mathcal K}=&
\int_{[0,T]^m_<\times[0,T]^n_<}d\mathbf s\,d\mathbf r
\int_{(\mathbb R^d)^m\times(\mathbb R^d)^n}
\prod_{j=1}^m G_{s_{j+1}-s_j}(y_{j+1}-dy_j)
\prod_{j=1}^n G_{r_{j+1}-r_j}(z_{j+1}-dz_j)\\
&\times\prod_{\{a,b\}\in D}\mathcal K(\tau_a,\eta_a;\tau_b,\eta_b),
\end{split}
\tag{E:terminal-pairing-integral}
\]
each pairing with coefficient one, odd total order zero, empty chains and \((m,n)=(0,0)\) with the usual empty products. If \(\mathcal K\ge0\), every integral is nonnegative and entrywise comparison \(0\le\mathcal K_1\le\mathcal K_2\) orders finite partial-order second moments; \(\sum_{n\ge0}r^nY_n\) converges absolutely in \(L^2\) for every real/complex \(r\).

**Supplied deductions.**
1. \(G_h(\mathbb R^d)=h\), so the total mass \(M_n(T)\) obeys \(M_n(T)=\int_0^T(T-s)M_{n-1}(s)ds\), hence \(M_n(T)=T^{2n}/(2n)!\).
2. Gaussian moments and Hölder give the Wick-moment bound \(\sqrt{(2n-1)!!}V^{n/2}\); mean-square Gaussian continuity yields strong measurability on partition cells.
3. Fubini and differentiating the joint characteristic function at degree \(m+n\) gives E:terminal-wick-formula: the orientation/orderings cancel the \(2^kk!\) denominator, giving coefficient one per unordered pair partition.
4. Symmetrizing a chain does not change the stochastic integral, so the \(1/n!\) average of the \(n!\) pushforwards represents the ordered integral; no extra \(n!\) or \(m!n!\) enters.
5. In \(d=3\), replace \(G\) by \(p_\eta*G\); equal masses, weak convergence, bounded continuous Wick factors, and dominated convergence give the fixed-noise Green convention.
6. Positivity and comparison are immediate from nonnegative Green measures and \(\mathcal K\ge0\). The series ratio is \(|r|\sqrt{V}T^2/((2n+2)\sqrt{2n+1})\to0\).

No stationary time reversal of \(K_J\) is asserted.

## PROOF050

**Statement (Lemma `L:uniform-series-tail`).** Fix \((T,x)\). Let \(Y_n^{\epsilon,\delta}\) be the regularized terms of 049 for a field with nonnegative covariance, \(u^{\epsilon,\delta}(r)=\sum_{n\ge0}r^nY_n^{\epsilon,\delta}\). Suppose for some \(r>1\), finite \(B_r\),
\[
\sup_{\epsilon,\delta>0}\mathbb E|u^{\epsilon,\delta}(r)|^2\le B_r,\qquad
Y_n^{\epsilon,\delta}\to X_n\text{ in }L^2\text{ for each }n.
\]
Then \(u=\sum_{n\ge0}X_n\) converges absolutely in \(L^2\), \(u^{\epsilon,\delta}(1)\to u\) in \(L^2\), and
\[
\|Y_n^{\epsilon,\delta}\|_2,\|X_n\|_2\le B_r^{1/2}r^{-n},
\qquad
\|\sum_{n>N}Y_n^{\epsilon,\delta}\|_2,\|\sum_{n>N}X_n\|_2
\le\frac{B_r^{1/2}r^{-(N+1)}}{1-r^{-1}} .
\tag{E:uniform-series-tail}
\]
If also \(\mathbb E|u^{\epsilon,\delta}(1)|^2\le B_1\) uniformly, then \(\mathbb E|u|^2\le B_1\).

**Supplied deductions.**
1. 049 gives absolute \(L^2\) convergence of each regularized series and nonnegative mixed moments; the scaled second moment contains the nonnegative term \(r^{2n}\mathbb E|Y_n^{\epsilon,\delta}|^2\le B_r\).
2. The fixed-order limit passes the same bound to \(X_n\); geometric sums give all tail bounds.
3. For the full-series limit, the distance is at most
\[
\frac{2B_r^{1/2}r^{-(N+1)}}{1-r^{-1}}
+\left\|\sum_{n=0}^N(Y_n^{\epsilon,\delta}-X_n)\right\|_2 ,
\]
giving convergence by first taking \(\epsilon,\delta\downarrow0\) at fixed \(N\), then \(N\to\infty\). Norm continuity passes \(B_1\).

## PROOF051

**Statement (Theorem `T:full-upper`).** Under Hypothesis `H:homog`, for \(u\) the canonical expansion solution,
\[
R_\alpha=\frac{\alpha\pi\mu(B_1)}{2\sin(\pi\alpha/2)},
\]
there is a finite \(C=C(\alpha,\alpha_0)\) such that
\[
\mathbb E u^2(T,x)
\le e(T+2)^d
\exp\left\{C R_\alpha^{1/(3-\alpha)}
T^{(4-\alpha-\alpha_0)/(3-\alpha)}\right\},\qquad T\ge1.
\tag{E:full-upper-bound}
\]

**Supplied deduction chain.**
1. **Dyadic majorant.** Choose \(H_0\) with \(6T\le H_0<12T\), \(h_j=H_02^{-j}\), three shifted nested grids with shifts \(h_j(n+(-1)^jt)\), \(t=0,1/3,2/3\). For \(s\ne r\),
\[
|s-r|^{-\alpha_0}
\le6^{\alpha_0}\sum_{\text{three grids},|I|\le H_0}
|I|^{-\alpha_0}\mathbf1_I(s)\mathbf1_I(r)
=:K_\infty(s,r).
\tag{E:dyadic-time-majorant}
\]
2. **Finite inventory.** Depth-\(J\) intervals with independent \(\sigma_I^2=6^{\alpha_0}|I|^{-\alpha_0}\) fields have decreasing lengths \(h_i\le78T/i\), so \(L=78\), \(c=6^{\alpha_0}\) in 048, uniformly in \(J,\epsilon\).
3. **Constant data comparison.** Cutoff \(f_T\in C_c^\infty(B_{T+2})\), equal to \(1\) on \(B_{T+1}\); for a chain ending at \(x\in B_1\), the free initial-data factor equals one, and Duhamel induction over modes identifies the phase position with the constant-data model, giving
\[
|B_1|\,\mathbb E|u_{J,\epsilon}(T,0)|^2
\le e\,|B_{T+2}|\exp\{CR_\alpha^{1/\nu}T^{\beta/\nu}\}.
\]
4. **Wick identification.** The interval model has covariance \(K_J(s,r)\Gamma_\epsilon(y-z)\); 049 applies term by term with each edge factor \(K_J\Gamma_\epsilon\), coefficient one, including self-pairs and unequal/empty chains; no stationarity in time is required.
5. **Source comparison.** The source covariance obeys
\[
0\le\gamma_\delta^0(s-r)\Gamma_\epsilon(y-z)\le|s-r|^{-\alpha_0}\Gamma_\epsilon(y-z),
\qquad
\gamma_\delta^0(t)=\Gamma(\alpha_0)^{-1}\int_0^{\delta^{-1}}e^{-q|t|}q^{\alpha_0-1}dq.
\]
For fixed partial order \(N\), nonnegative Tonelli with \(K_J\uparrow K_\infty\) gives
\[
\mathbb E|U_N^{\epsilon,\delta}(T,x)|^2
\le\lim_{J\to\infty}\mathbb E|V_{N,J}^\epsilon(T,x)|^2
\le\sup_J\mathbb E|u_{J,\epsilon}(T,x)|^2
\le B(T).
\tag{E:interval-source-comparison}
\]
No infinite-depth Gaussian field of covariance \(K_\infty\Gamma_\epsilon\) is constructed; \(K_\infty\) is used only inside positive integral limits.
6. **Scaled noise and series.** Noise amplitude \(a\) replaces \(\Gamma\to a^2\Gamma\), \(R_\alpha\to a^2R_\alpha\), so
\[
\mathbb E|u^{\epsilon,\delta}(a;T,x)|^2
\le e(T+2)^d\exp\{C(a^2R_\alpha)^{1/\nu}T^\kappa\}.
\tag{E:regularized-scaled-moment}
\]
7. **Tail passage.** 006 supplies fixed-order \(L^2\) convergence \(Y_n^{\epsilon,\delta}\to X_n\); 050 with \(r=2,B_r=B(T;2)\) completes absolute convergence and full regularized convergence, then the limit at \(a=1\) uses \(B(T;1)\), not \(B(T;2)\).
8. **Order of limits** is enumerated: fixed-order uniformity; finite-family identification before positivity; finite-depth positivity before \(J\to\infty\); 050 before summing orders; no uniformity in \(T\) or covariance shapes is claimed.

**Falsification check.** Spatial white \(d=\alpha=1\) is included since \(\Gamma=\delta_0\) satisfies the measure hypotheses; zero noise is trivial; nonstationary \(K_J\) is handled because the 049 comparison precedes any time reversal.

**Boundary.** 051 does not use Proposition `P:mixed`, `L:crude-corrected`, or the source Section 5 convergence; Proposition `P:mild-construction` is a separate identification and does not supply the sharp-scale moment estimate.

## PROOF052

**Statement (Lemma `L:mean-coefficient-holder`).** Fix a nonzero covariance satisfying `H:homog`; set
\[
\nu=3-\alpha,\quad a_{\max}=\min(1,2-\alpha),\quad
\beta(a)=4-\alpha-a,\quad\kappa(a)=\frac{\beta(a)}{\nu},\quad
\kappa_{\rm st}=\frac{4-\alpha}{\nu}.
\]
Let \(u^{(a)}\) be the canonical solution with temporal covariance \(|s-r|^{-a}\Gamma\), \(0<a<a_{\max}\), and let \(u^{(0)}=U\) be the static canonical solution (temporal covariance one). Then for every \(0\le a<a_{\max}\),
\[
m_k(a)=\mathbb E X_{2k}^{(a)}(1,0),\quad m_0(a)=1,
\qquad
\mathbb E u^{(a)}(t,x)=\sum_{k\ge0}m_k(a)t^{\beta(a)k},
\tag{E:mean-positive-series}
\]
with \(F_a(z)=\sum_{k\ge0}m_k(a)z^k\) finite for every \(z\ge0\), and for \(0<a<b<a_{\max}\),
\[
m_k(a)\le m_k(0)^{1-a/b}m_k(b)^{a/b},\qquad k\ge1.
\tag{E:mean-coefficient-holder}
\]

**Imported static premises.** From Chen–Hu Theorem 1.2/(1.9), p. 2147:
\[
0<L_0:=\lim_{t\to\infty}t^{-\kappa_{\rm st}}\log\mathbb E U(t,x)<\infty,
\qquad
\lim_{t\to\infty}t^{-\kappa_{\rm st}}\log\mathbb E U(t,x)^2=2^{\kappa_{\rm st}}L_0.
\tag{E:static-ratio-input}
\]
The proof imports **only** the common \(p^{\kappa_{\rm st}}\) factor and moment law, not a white-noise constant.

**Supplied deductions.**
1. Static endpoint terms are constructed via bounded-variance Gaussian Bochner integrals and the spatial-Wick diagram limits; the static norm series is supplied by comparing its finite Wick sums with the fractional-time regularized bound
\[
\mathbb E|U_N^\epsilon(r;1,x)|^2
\le\mathbb E|u^{\epsilon,\delta_0}_{b_0}(r/\sqrt c;1,x)|^2
\le B_{b_0}(1;r/\sqrt c)
\]
and applying 050. This consumes 051 **afterwards**, not as a premise back into 051.
2. Static homogeneity
\[
\|X_n^{(0)}(t,x)\|_2=t^{(4-\alpha)n/2}\|X_n^{(0)}(1,0)\|_2
\]
and \(r>t^{(4-\alpha)/2}\) give fixed-\(t\) norm summability.
3. For a single chain \(2k\),
\[
m_k^\epsilon(a)=\sum_{D\in\Pi_k}\int\prod_{\{j,h\}\in D}|s_j-s_h|^{-a}\,d\omega_{\epsilon,D},
\]
with \(\omega_{\epsilon,D}\) the finite positive spatial Green–Wick measure. The time multiplier at \(a\) is exactly the \((a/b)\)-power of the multiplier at \(b\), so Hölder on the pairing-measure union gives the raw-power interpolation
\[
m_k^\epsilon(a)\le m_k^\epsilon(0)^{1-a/b}m_k^\epsilon(b)^{a/b}.
\]
No exponent-dependent Laplace prefix or Euler-Gamma normalization is interpolated.
4. Spatial-width removal uses the two-sided estimate
\[
F_{\epsilon,\eta,D}\le F_{\epsilon,0,D}\le F_{\epsilon,\eta,D}+r_a(\eta),
\qquad r_a(\eta)\to0
\]
uniformly in \(\epsilon\); spatial limit at fixed \(\eta\), then \(\eta\downarrow0\), gives the joint diagram value; the zero-exponent value comes from spatial-Wick-measures and the static fixed-order limit.
5. Scaling gives
\[
\mathbb E X_{2k}^{(a)}(t,x)=t^{\beta(a)k}m_k(a),
\]
and mean-series interchange uses the norm sums in `L:vertex-crude`.

## PROOF053

**Statement (Lemma `L:positive-series-type`).** Let \(\nu\ge1\), \(c_k\ge0\), \(c_0=1\), \(F(z)=\sum_{k\ge0}c_kz^k<\infty\) for all \(z\ge0\). If
\[
\tau=\limsup_{z\to\infty}z^{-1/\nu}\log F(z)<\infty,
\]
then
\[
K:=\limsup_{k\to\infty}((k!)^\nu c_k)^{1/k}<\infty,\qquad
\tau=\nu K^{1/\nu}.
\tag{E:positive-series-type}
\]
Conversely, finite \(K\) gives the same finite \(\tau\) and equality.

**Supplied deductions.**
1. For \(L>\tau\), continuity on compacts gives \(F(z)\le C_Le^{Lz^{1/\nu}}\); at \(z=(\nu k/L)^\nu\),
\[
c_k\le C_Le^{\nu k}\left(\frac L{\nu k}\right)^{\nu k},
\]
and Stirling’s two-sided bound
\[
k\log k-k+1\le\log(k!)\le k\log k-k+1+\log k
\]
gives \(K\le(L/\nu)^\nu\); letting \(L\downarrow\tau\) gives \(K\le(\tau/\nu)^\nu\).
2. Conversely, for \(A>K\), eventually \(c_k\le A^k/(k!)^\nu\), hence
\[
F(z)\le P(z)+\exp\{\nu(Az)^{1/\nu}\},
\]
so \(\tau\le\nu A^{1/\nu}\) and \(A\downarrow K\) closes the equality.

**Falsification check.** Zero or sparse coefficients are admitted: only the eventual upper bounds enter the limsup, and no positivity of a radius or division by a coefficient is used.

## PROOF054

**Statement (Proposition `P:static-minorant-lower`).** For every \(0<a<a_{\max}\), \(T>0\), \(p\in\{1,2\}\),
\[
\mathbb E[u^{(a)}(T,x)^p]
\ge\mathbb E\left[U\left(T^{1-a/(4-\alpha)},x\right)^p\right],
\tag{E:static-minorant-moment}
\]
and hence
\[
\liminf_{T\to\infty}T^{-\kappa(a)}\log\mathbb E[u^{(a)}(T,x)^p]
\ge p^{\kappa_{\rm st}}L_0,\qquad p=1,2.
\tag{E:static-minorant-rate}
\]

**Supplied deductions.**
1. For common positive widths \(\epsilon,\delta\), on \([0,T]\),
\[
\gamma_{\delta,a}^0(s-r)\ge c_{\delta,T}:=\gamma_{\delta,a}^0(T)>0,
\qquad c_{\delta,T}\to T^{-a}\ (\delta\downarrow0).
\]
2. **Fixed partial order first.** The order-\(N\) partial series have the same terminal Green kernels and pairings; each time factor of \(u^{(a)}\) exceeds \(c_{\delta,T}\), so finite expected powers are ordered for \(p=1,2\). In \(d=3\), Green smoothing is removed first at fixed noise widths.
3. Joint \((\epsilon,\delta)\downarrow0\) at fixed \(N\) uses the fixed-order limits; dependence on \(c_{\delta,T}\) is a finite polynomial, so the limit is the static model with amplitude \(\sigma=T^{-a/2}\). No uniform-in-\(T\) or infinite-order approximation is used.
4. **Exact amplitude/time clock before infinite orders.** Static homogeneity gives
\[
\sigma^n\|X_n^{(0)}(T,x)\|_2
=\|X_n^{(0)}(\sigma^{2/(4-\alpha)}T,x)\|_2,
\]
and the norm-series summability from 052 passes to the amplitude-scaled effective time; letting \(N\to\infty\) preserves the finite-order inequality. For the convergent nonnegative moment series,
\[
\mathbb E[U_\sigma(T,x)^p]
=\mathbb E[U(\sigma^{2/(4-\alpha)}T,x)^p].
\]
No coupling of random fields is asserted.
5. With \(\sigma=T^{-a/2}\),
\[
\left(T^{1-a/(4-\alpha)}\right)^{\kappa_{\rm st}}=T^{\kappa(a)},
\]
and the imported static rates E:static-ratio-input give E:static-minorant-rate.

## PROOF055

**Statement (Proposition `P:near-static-mean-gap`).** Define
\[
M(a)=\limsup_{T\to\infty}T^{-\kappa(a)}\log\mathbb E u^{(a)}(T,x),
\qquad
K(a)=\limsup_{k\to\infty}((k!)^\nu m_k(a))^{1/k}.
\]
Then \(K(0)=(L_0/\nu)^\nu>0\), \(K(b)<\infty\) for each \(0<b<a_{\max}\). For a fixed \(b\) and finite \(B_b\ge\max(2K(0),K(b))\), for \(0<a<b\),
\[
M(a)\le L_0\left(\frac{B_b}{K(0)}\right)^{a/(b\nu)}.
\tag{E:near-static-mean-upper}
\]
With
\[
a_*:=\frac{b\log2}{\log(B_b/K(0))}\in(0,b],
\tag{E:near-static-window}
\]
every \(0<a<a_*\) satisfies
\[
\liminf_{T\to\infty}T^{-\kappa(a)}\log\mathbb E[u^{(a)}(T,x)^2]>2M(a).
\tag{E:near-static-mean-gap}
\]

**Supplied deductions.**
1. The substitution \(z=T^{\beta(a)}\) identifies the normalized logarithmic type of \(F_a\) with \(M(a)\); imported static law and 053 give \(K(0)=(L_0/\nu)^\nu\).
2. For \(b>0\), Cauchy–Schwarz and **Theorem `T:full-upper`** at temporal exponent \(b\) give \(M(b)<\infty\), hence \(K(b)<\infty\). This consumes 051, not a printed first-moment rate constant.
3. From 052, multiplying by \((k!)^\nu\), taking \(k\)-th roots and limsup, with the \(\eta\)-regularization valid even for zero coefficients, gives
\[
K(a)\le K(0)^{1-a/b}B_b^{a/b}.
\]
053 gives
\[
M(a)=\nu K(a)^{1/\nu}\le L_0(B_b/K(0))^{a/(b\nu)}.
\]
4. Since \(B_b/K(0)\ge2\), the window \(a_*\) is positive and at most \(b\). For \(0<a<a_*\),
\[
2M(a)<2L_0\,2^{1/\nu}=2^{\kappa_{\rm st}}L_0,
\]
using \(\kappa_{\rm st}=1+1/\nu\), and 054 at \(p=2\) gives the strict gap.

The gate uses the **actual** first-mean rate \(M(a)\) and the **explicit** window \(a_*\), not a printed constant.

## PROOF056

**Statement (Lemma `L:full-moment-coefficient-holder`).** For \(p=1,2\), define
\[
c_{1,k}(a)=m_k(a),\qquad
c_{2,k}(a)=\sum_{m=0}^{2k}\mathbb E[X_m^{(a)}(1,0)X_{2k-m}^{(a)}(1,0)],
\qquad c_{p,0}(a)=1.
\]
For \(0\le a<a_{\max}\), the coefficients are nonnegative and
\[
\mathbb E[u^{(a)}(t,x)^p]
=\sum_{k\ge0}c_{p,k}(a)t^{\beta(a)k}<\infty,\qquad t>0.
\tag{E:full-moment-positive-series}
\]
If \(0\le a_1<a<a_2<a_{\max}\) and \(\theta=(a-a_1)/(a_2-a_1)\), then
\[
c_{p,k}(a)\le c_{p,k}(a_1)^{1-\theta}c_{p,k}(a_2)^\theta,\qquad k\ge0.
\tag{E:full-moment-coefficient-holder}
\]

**Supplied deductions.**
1. At common spatial width \(\epsilon\), unit horizon, each split \(m+n=2k\) and pairing \(D\) has a finite positive spatial Green–Wick measure \(\omega_{\epsilon,m,n,D}\). For \(p=1\), the union is only the single split \((m,n)=(0,2k)\); for \(p=2\), it is **all** \(m=0,\dots,2k\), with the two empty-chain orientations distinct. Wick’s formula has coefficient one per pairing.
2. Define
\[
c_{p,k}^\epsilon(a)=\int\prod_{\{j,h\}\in D}|s_j-s_h|^{-a}\,d\omega_{\epsilon,p,k}.
\]
The raw time multiplier at \(a\) is the weighted product of the endpoint multipliers; Hölder on the disjoint union gives
\[
c_{p,k}^\epsilon(a)\le c_{p,k}^\epsilon(a_1)^{1-\theta}c_{p,k}^\epsilon(a_2)^\theta.
\]
3. The raw-time spatial limit is identified as in 052 for every unequal/empty split; at zero exponent the multiplier is one and `L:spatial-wick-measures` applies. Positive exponents use Proposition `P:mixed`; products converge in \(L^1\) by Cauchy–Schwarz. This proves nonnegativity and E:full-moment-coefficient-holder. No exponent-dependent Laplace-prefix/Euler-Gamma normalization is interpolated.
4. Every diagram has \(2k\) time Jacobians, \(2k\) Green scalings, \(k\) spatial and \(k\) temporal covariance factors, so the homogeneous time degree is
\[
4k-\alpha k-ak=\beta(a)k,
\]
including empty-chain cases. Positive-\(a\) series follow from `P:mixed` and E:mean-positive-series; at zero the static norm series gives convergence of partial means/squares and the monotone regrouping by total order.

## PROOF057

**Statement (Proposition `P:moment-growth-logconvex`).** Define
\[
\overline\Lambda_p(a)=\limsup_{T\to\infty}T^{-\kappa(a)}\log\mathbb E[u^{(a)}(T,x)^p],
\qquad
\underline\Lambda_p(a)=\liminf_{T\to\infty}T^{-\kappa(a)}\log\mathbb E[u^{(a)}(T,x)^p],
\]
for \(p=1,2\), with \(p=1\) meaning \(\mathbb E u\), not \(\mathbb E|u|\). Then \(\overline\Lambda_p(a)\) is positive and finite on \(0\le a<a_{\max}\), and for the endpoints and \(\theta\) of 056,
\[
\overline\Lambda_p(a)\le
\overline\Lambda_p(a_1)^{1-\theta}
\overline\Lambda_p(a_2)^\theta.
\tag{E:moment-growth-logconvex}
\]
In particular \(\log\overline\Lambda_p\) is convex and \(\overline\Lambda_p\) is continuous on \((0,a_{\max})\).

**Supplied deductions.**
1. \(C_p=p^{\kappa_{\rm st}}L_0>0\); E:static-ratio-input gives \(\overline\Lambda_p(0)=\underline\Lambda_p(0)=C_p\), 054 gives \(\underline\Lambda_p(a)\ge C_p\) for \(a>0\).
2. Finiteness for \(p=2\) is Theorem `T:full-upper`; for \(p=1\) it follows by Cauchy–Schwarz, and positivity from the pairing series.
3. \(F_{p,a}(z)=\sum_{k\ge0}c_{p,k}(a)z^k\) has normalized logarithmic type \(\overline\Lambda_p(a)\) because \(z=T^{\beta(a)}\), \(z^{1/\nu}=T^{\kappa(a)}\). 053 gives
\[
K_p(a):=\limsup_{k}((k!)^\nu c_{p,k}(a))^{1/k}
=\left(\frac{\overline\Lambda_p(a)}{\nu}\right)^\nu .
\]
4. Multiplying E:full-moment-coefficient-holder by \((k!)^\nu\), \(k\)-th roots and limsup gives
\[
K_p(a)\le K_p(a_1)^{1-\theta}K_p(a_2)^\theta,
\]
using the \(\eta\)-regularization that permits zero/oscillating subsequences.
5. Continuity follows from the secant-slope boundedness for the finite convex function \(\log\overline\Lambda_p\).

## PROOF058

**Statement (Corollary `C:static-moment-constant-continuity`).** Put \(C_p=p^{\kappa_{\rm st}}L_0\), \(p=1,2\). For every fixed \(0<b<a_{\max}\) and \(0<a<b\),
\[
C_p\le\underline\Lambda_p(a)\le\overline\Lambda_p(a)
\le C_p\left(\frac{\overline\Lambda_p(b)}{C_p}\right)^{a/b}.
\tag{E:static-constant-envelope}
\]
Consequently,
\[
\lim_{a\downarrow0}\underline\Lambda_p(a)
=\lim_{a\downarrow0}\overline\Lambda_p(a)=C_p,\qquad p=1,2,
\tag{E:static-constant-continuity}
\]
and
\[
\lim_{a\downarrow0}\frac{\underline\Lambda_2(a)}{\overline\Lambda_1(a)}
=2^{\kappa_{\rm st}}.
\tag{E:static-moment-ratio-continuity}
\]

**Supplied deductions.**
1. The lower inequality is 054; the upper applies 057 at endpoints \(0,b\) with \(\overline\Lambda_p(0)=C_p\).
2. The finite ratio \(\overline\Lambda_p(b)/C_p\ge1\) gives \(a/b\)-power convergence to one, hence the iterated limits.
3. The ratio limit uses \(L_0>0\); consequently the ratio is
\[
\frac{2^{\kappa_{\rm st}}L_0}{L_0}=2^{\kappa_{\rm st}}.
\]
**Order of limits.** First the time liminf/limsup at each fixed \(a\) with normalization \(T^{-\kappa(a)}\), then \(a\downarrow0\). No uniform-in-\(a\) time limit, no simultaneous limit, and no existence of a pointwise-in-\(t\) time limit at fixed positive \(a\) is asserted. For **zero noise** \(L_0=0\), the ratio in E:static-moment-ratio-continuity is undefined; that case is kept separate.

## PROOF059

**Statement (Lemma `L:white-clock-laplace`, falsification setting \(d=\alpha=1\), \(\Gamma=\delta_0\), \(0<a<1\)).** The \((1,1)\) cross-pair gap transform is
\[
K_\times(\theta_1,\theta_2)
=\int_0^\infty\int_0^\infty
e^{-\theta_1s-\theta_2t}|s-t|^{-a}\frac{\min(s,t)}2\,ds\,dt
=\frac{\Gamma_E(1-a)}{2(\theta_1+\theta_2)^2}
\left(\theta_1^{a-1}+\theta_2^{a-1}\right),
\tag{E:white-cross-clock-transform}
\]
and in particular \(K_\times(\theta,\theta)=\Gamma_E(1-a)/(4\theta^{3-a})\). The empty-plus-length-two self-pair transform is
\[
K_{\rm self}(\eta_1,\eta_2)
=\int_0^\infty\int_0^\infty
e^{-\eta_1r_1-\eta_2r_2}r_2^{-a}\frac{r_1}2\,dr_1dr_2
=\frac{\Gamma_E(1-a)}{2\eta_1^2\eta_2^{1-a}}.
\tag{E:white-self-clock-transform}
\]

**Supplied deductions.**
1. The spatial cross factor is
\[
\int G_s(y)G_t(z)\delta_0(y-z)dydz
=\frac14\int\mathbf1_{\{|y|<s\wedge t\}}dy=\frac{\min(s,t)}2.
\]
2. Splitting \(s=t+v\), \(t=s+v\), each part is
\[
\frac12\left(\int_0^\infty t e^{-(\theta_1+\theta_2)t}dt\right)
\left(\int_0^\infty e^{-\theta_i v}v^{-a}dv\right),
\]
which evaluates via
\[
\int_0^\infty t e^{-ct}dt=c^{-2},\qquad
\int_0^\infty e^{-cv}v^{-a}dv=\Gamma_E(1-a)c^{a-1}.
\]
3. For the self-pair, the delta covariance forces equal positions; the second Green factor is \(G_{r_2}(0)=1/2\) and the first has mass \(r_1\); the time difference is \(r_2\).

## PROOF060

**Statement (Proposition `P:clock-copy-obstruction`).** Let \(\gamma_a^{\rm an}(z)=(z\,\mathrm{sgn}\Re z)^{-a}\), \(\Re z\ne0\), and for \(r>0,v\ge0\),
\[
\Psi_a(r,v)=\frac{1}{\Gamma_E(a)}
\int_0^\infty\lambda^{a-1}e^{-r\lambda-v\lambda^2/2}d\lambda
=\mathbb E(r+iZ)^{-a},
\qquad Z\sim N(0,v).
\tag{E:averaged-clock-kernel}
\]
For an arbitrary nonzero covariance in `H:homog` with temporal exponent \(a\), define
\[
h_\Gamma(w)=\int e^{-w|\xi|^2/2}\mu(d\xi),
\qquad
\mathcal R_\Gamma(q)=\int\frac{\mu(d\xi)}{q^2+|\xi|^2},
\]
with \(h_\Gamma(w)=w^{-\alpha/2}h_\Gamma(1)\), \(\mathcal R_\Gamma(q)=q^{\alpha-2}\mathcal R_\Gamma(1)\), and \(K_\Gamma(\theta)=N_2(\theta)^2\) the actual cross-pair gap transform. For independent spatial Brownian motions \(B_1,B_2\) and Brownian clocks \(\beta_1,\beta_2\) with correlation \(\rho\), \(v_\rho(u,v)=u+v-2\rho\min(u,v)\),
\[
J_{\Gamma,\rho}(\theta):=\frac14\int_0^\infty\int_0^\infty
e^{-\theta^2(u+v)/2}h_\Gamma(u+v)
\Psi_a(\theta|u-v|,v_\rho(u,v))\,du\,dv .
\tag{E:naive-clock-candidate}
\]
Set
\[
w_\theta(\lambda)=\frac{\lambda^{a-2}}{2\theta\Gamma_E(a)}
\left(\mathcal R_\Gamma(\theta)-\mathcal R_\Gamma(\theta+\lambda)\right),\qquad\lambda>0.
\tag{E:cross-clock-lambda-weight}
\]
Then \(w_\theta\) is a positive integrable density and
\[
K_\Gamma(\theta)=\int_0^\infty w_\theta(\lambda)d\lambda,
\qquad
0<J_{\Gamma,\rho}(\theta)\le J_{\Gamma,1}(\theta)
=\int_0^\infty\frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)d\lambda
<K_\Gamma(\theta).
\tag{E:clock-copy-obstruction}
\]
For \(\alpha=1\),
\[
J_{\Gamma,1}(\theta)=(2-2^a)K_\Gamma(\theta).
\tag{E:degree-one-clock-loss}
\]

**Supplied deductions.**
1. **Actual cross transform.** For \(r=|\xi|\), direct cone integration gives
\[
\int_0^\infty\int_0^\infty
e^{-\theta(s+t)-\lambda|s-t|}\widehat G_s(\xi)\overline{\widehat G_t(\xi)}dsdt
=\frac{2\theta+\lambda}{2\theta(\theta^2+r^2)((\theta+\lambda)^2+r^2)}.
\]
The spectral integrand is nonnegative; removing the Gaussian multiplier and applying weight \(1/\Gamma_E(a)\lambda^{a-1}d\lambda\) gives
\[
K_\Gamma(\theta)=\int_0^\infty\lambda^{a-1}\frac{2\theta+\lambda}{2\theta}
\int\frac{\mu(d\xi)}{(\theta^2+|\xi|^2)((\theta+\lambda)^2+|\xi|^2)}\frac{d\lambda}{\Gamma_E(a)},
\]
and partial fractions yield \(K_\Gamma(\theta)=\int w_\theta d\lambda\). The density is positive since \(\mathcal R_\Gamma(\theta)>\mathcal R_\Gamma(\theta+\lambda)\).
2. **Candidate finiteness and ordering.** \(\Psi_a(\theta|u-v|,v_\rho)\le(\theta|u-v|)^{-a}\) and \(h_\Gamma(w)=h_\Gamma(1)w^{-\alpha/2}\) supply the absolute majorant; with \(w=u+v\), \(q=u-v\), Jacobian \(1/2\),
\[
\frac2{1-a}\int_0^\infty e^{-\theta^2w/2}w^{1-\alpha/2-a}dw<\infty
\]
because \(a<1\) and \(a+\alpha/2<2\). The heat-regularized average uses \(h(w+2\epsilon)\le h(w)\), a spectral bound, not pointwise covariance monotonicity.
3. Since \(v_\rho(u,v)\ge|u-v|=v_1(u,v)\), monotonicity of \(\Psi_a\) in \(v\) gives \(J_{\Gamma,\rho}\le J_{\Gamma,1}\).
4. **Computing \(J_{\Gamma,1}\).** With \(A=\theta\lambda+\lambda^2/2\), the \(q\)-integral is \(2(1-e^{-Aw})/A\); the resolvent identity
\[
\mathcal R_\Gamma(q)=\frac12\int_0^\infty e^{-q^2v/2}h_\Gamma(v)dv
\]
gives
\[
J_{\Gamma,1}(\theta)
=\int_0^\infty\frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)d\lambda ,
\]
after the factor-two cancellations. Since \(2\theta/(2\theta+\lambda)<1\) and \(w_\theta>0\), \(J_{\Gamma,1}<K_\Gamma\).
5. **Degree-one ratio.** For \(\alpha=1\), \(\mathcal R_\Gamma(q)=\mathcal R_\Gamma(1)/q\), so
\[
K_\Gamma(\theta)=\frac{\mathcal R_\Gamma(1)}{2\theta^2\Gamma_E(a)}
\int_0^\infty\frac{\lambda^{a-1}}{\theta+\lambda}d\lambda,
\]
\[
J_{\Gamma,1}(\theta)=\frac{\mathcal R_\Gamma(1)}{\theta^2\Gamma_E(a)}
\int_0^\infty\lambda^{a-1}\left(\frac1{\theta+\lambda}-\frac1{2\theta+\lambda}\right)d\lambda.
\]
The Beta identity
\[
\int_0^\infty\frac{x^{a-1}}{x+c}dx=c^{a-1}\Gamma_E(a)\Gamma_E(1-a),\qquad c>0,
\]
evaluates both, giving \(J_{\Gamma,1}/K_\Gamma=2-2^a\). At \(a=1/2\) this is \(2-\sqrt2\).

**Scope stated in the module.** The obstruction concerns only the direct unweighted constant-correlation analytic clock substitution in E:naive-clock-candidate with product heat-chain measure, unrestricted operational-time rectangle, and constant Brownian correlation. It does **not** refute ordering-corrected, diagonal-only, or asymptotic clock representations, and does not identify the source’s all-moment conjecture. No Skorohod development is made.

## APPLICATION-INDEPENDENT-UPPER

The explicit noncircular coupling of 039/044/045/046/047/048/049/050/006 to 051 is as follows.

**Incoming foundation inputs.**
- **214** (constant-one translated covariance Cauchy–Schwarz) supplies, for every edge norm \(N_{2,e}\), the coefficient-one bound
\[
Q(T_{A,a}G_1^0,T_{B,b}G_2^0)\le N_{2,e}(G_1)N_{2,e}(G_2),
\]
with the predecessor-time offset \(A-B\) retained.
- **215** (finite pairing product envelope) supplies, for each actual kernel family, the per-family product
\[
I_D(\mathbf G)\le\max_{(Q,\iota)\in\mathcal A_D}\mathcal P_{Q,\iota}(\mathbf G),
\]
with exactly \(2N_{1,e}\) per first slot and two \(N_{2,e}\) per second slot; used by 006.
- **004** supplies the homogeneous damped norms and tails
\[
N_0(\theta)=\theta^{-2},\qquad
N_1(\theta)=\theta^{\alpha+\alpha_0-2}N_1(1),\qquad
N_2(\theta)^2=\theta^{-\beta}N_2(1)^2,
\]
and the tail convergence \(N_1^{(M)}(1),N_2^{(M)}(1)\to0\).
- **005** supplies the spatial Wick-measure limits \(\nu_D\) with \(\rho_D(cA)=c^{(4-\alpha)k}\rho_D(A)\).
- **006** supplies the joint fixed-order construction and the temporal-tail bound
\[
0\le F_{\epsilon,0,D}-F_{\epsilon,\eta,D}
\le C_{k,T_1,T_2}\left(N_1^{(1/\eta)}(1)+N_2^{(1/\eta)}(1)^2\right),
\]
from which the fixed-order \(L^2\) limits \(Y_n^{\epsilon,\delta}\to X_n\) follow.

**Chain to 051.**
1. **044** converts the homogeneous spectral comparison into the spatial column bound
\[
\sum_m\|A_\rho^{-1/2}M_{e_m}f\|_2^2\le R_\alpha\rho^{\alpha-2}\|f\|_2^2
\]
and the Hermite Fock bound
\[
2\sqrt{N+1}\,\sqrt{R_\alpha}\,\rho^{\alpha/2-2}.
\]
2. **039/045** convert the Fock sandwich into the uniform complex phase bound
\[
\|\mathcal M_z(h)\|_{X_\Lambda\to X_\Lambda}\le100e^{2\Lambda h}
\]
under \(D\le\delta_a\Lambda^{2-a}\), and bound the phase-weight metric change by \(\prod_i(1+\omega_i/\lambda)\) on a single connected-interval partition.
3. **047** uses 044/045 to obtain the fixed split energy:
\[
\text{cross }(1,1):\ R_\alpha\lambda^{\alpha-2}h_i^{2-\alpha_0},
\qquad
\text{singleton mean }(2,0)/(0,2):\ R_\alpha h_i^\beta(1+1/(\lambda h_i)),
\]
\[
l\ge2:\ \frac{R_\alpha^lh_i^{\beta l}(1+l/(\lambda h_i))^2}{(l!)^\nu},
\]
with one ending metric for a singleton mean and at most two for higher colors, and with constant \(C_{\rm split}=100^8e^8\max(1,12\delta_{\alpha/2}^{-2})\).
4. **046** sums these coefficient extractions through \(v_i,b_{i,l}\) at \(z=\theta k^\nu\), producing \(C^k/(k!)^\nu\) with no multinomial.
5. **048** applies reflection parity \(r_i+q_i=2k_i\), exact Hermite cutoff \(N_i=2k_i\) via 041, and the no-multinomial inventory product to obtain
\[
\left|[s^{2k}]\mathbb E\|\mathcal U^\epsilon_{\mathcal F}(T;s)v\|_{1/T}^2\right|
\le\frac{C^kR_\alpha^k T^{\beta k}}{(k!)^\nu}\|v\|_{1/T}^2 .
\]
6. **049** identifies each interval-model and source partial-order second moment with nonnegative coefficient-one Wick terms on the finite terminal Green-chain measure of mass \(T^{2n}/(2n)!\), including self-pairs, unequal and empty chains, before any time reversal.
7. **050** supplies the uniform-head/tail passage: a scaled moment \(B_r=B(T;2)\) with \(r=2\) gives geometric tails \(r^{-n}\) and the full \(L^2\) convergence of the regularized series to \(u\).
8. **051** then uses \(L=78\), \(c=6^{\alpha_0}\) for the three shifted nested grids, the monotone \(K_J\uparrow K_\infty\) comparison, entrywise positive Wick comparison, the amplitude scaling \(a\mapsto a^2R_\alpha\), and 050 with \(B(T;2)\) to reach \(B(T;1)\). The final bound uses \(B(T;1)\), not the larger tail bound.

**Source clauses supplied by F007 (not by an operator-Gaussian parent).** The retaining isometry
\[
\Phi F(\lambda,r)=\sqrt{2\lambda}\int_{t\ge r}e^{-\lambda(t-r)}F(t,\cdot)dt,
\qquad
\mathcal I(g)=W(\Phi^{-1}Pg)+J((I-P)g),
\]
with **one fixed** independent \(J\); the point features
\[
v_{\rho;t,x}(\lambda,r)=\mathbf1_{\lambda\le\eta^{-1}}\sqrt{2\lambda}
e^{-\lambda(t-r)}\mathbf1_{r\le t}p_\epsilon(x-\cdot);
\]
the retained law
\[
\mathbf I(\Phi h)=W(h),\qquad
\operatorname{Cov}(Y_{\epsilon,\eta}(t,x),Y_{\epsilon',\eta'}(s,y))
=K_{\max(\eta,\eta')}(t-s)\Gamma_{\epsilon+\epsilon'}(x-y),
\]
with temporal max and spatial sum \((p_{\epsilon}*p_{\epsilon'}=p_{\epsilon+\epsilon'})\); the two dominations
\[
\operatorname{Var}Y_\rho(F),\operatorname{Var}D_\rho(F)\le\|F\|_{H_W}^2,\qquad
\operatorname{Var}D_\rho(F)\to0;
\]
and the \(L^p\) driver convergence. Only these retaining/max/sum/point/test clauses are consumed at the finite-cutoff point needed by 006/049.

**Exclusions.**
- **009** (actual same-series mild identification) is separate; the held integrand, Green-first, multiplication and head-tail steps in 009 must not borrow 051.
- **S2 finiteness, the 132 variational conclusion, and the 204 intrinsic closure do not fund 051**; instead 051 funds the later 132 application; 052–058 consume 051 only afterwards and never feed premises back into it.
- **F194** establishes that a positive-cutoff point feature can be non-orthogonal to \((\Phi H_W)^\perp\), so \(W\)-only measurability of cutoff fields is not a premise; 051 does not assert it. F194 is a constraint on an unnecessary \(W\)-only strengthening, not a rating axiom.

## GLOBAL-UNPROVED-CONDITIONS

Per-section and global remaining mathematical premises:

**036.** The Schwartz quartic finiteness
\[
Q(g)\le\tfrac12\|\nabla g\|_2^2+C_0,\quad \|g\|_2=1,
\]
is imported from Chen2023 Theorem 1.1 (quartic (1.5), not square-root (1.4)). The two Cauchy–Schwarz inequalities, sigma-finite Fubini, representative independence, uniform Fourier limit and \(H^1\) closure are supplied.

**037.** The gamma integral identity \(\int_0^\infty r^{\alpha-1}/(1+r^2)dr=\pi/(2\sin(\pi\alpha/2))\) and the explicit sphere-wave convolution regions are elementary, but the constants depend on \(V=\mu(B_1)\), \(M=\Gamma(B_1)\) being finite.

**038.** The expansions and Bochner integrability are asserted at fixed \(\epsilon>0\); there is no \(\epsilon\to0\) limit. The second-order mean term \(2\operatorname{Re}\langle Z_0,\mathbb E Z_2\rangle\) is retained without sign; the whole coefficient is bounded in absolute value only.

**039/045.** The Crouzeix–Palencia theorem (selected 8-page packet) is imported for bounded operators. The numerical-range parabola uses \(\delta_a<1\); no unbounded square-root domain theorem is imported. The remaining hypothesis is the abstract sandwich
\[
\|A_\rho^{-1/2}BA_\rho^{-1/2}\|\le d\rho^{a-2}.
\]

**040.** \(B_{N,m,b}\) boundedness requires the band projection \(S_b\), so \(-\Delta\) is bounded on the band; the bound is only for finite \(N,m,b\) cutoffs.

**041.** The exact-word identity holds only when \(N_i\ge r_i\) for the fixed selected word; it is not an equality of full cutoff and uncompressed propagators and not an occupied-color vacuum bound.

**042/043.** All-orders bounds and block composition are at fixed positive smoothing; the dyadic series is the sum of individual upper bounds on one partition and does not supply overlapping-noise or repeated-field evolution; no zero-smoothing limit or multi-partition identification is proved.

**044/047.** The partition has at most \(3k+1\) segments; the insertion cube has no \(m!\) loss; cross colors are fresh vacuums while occupied singletons use cutoff \(N_i=2\); simultaneous endpoints are excluded as null sets. The constant \(C_{\rm split}\) is explicit but not numerically optimized.

**048.** \(v_{\max}\) is finite only after positive smoothing and is used only for identification, not as a uniform constant; smoothness of the fixed-width field and the finite-family entire majorant are used, not a smoothed asymptotic.

**049.** The field hypotheses are \(V<\infty\) plus mean-square continuity on finite partition cells; nonnegative covariance is needed for positivity/monotonicity and hence for the partial-order comparison in 051.

**050.** The tail passage needs a scaled-moment bound \(B_r\) with **some** \(r>1\); the final moment uses \(B_1\) supplied separately.

**051.** Full upper bound assumes `H:homog`; it uses the Green-first regularization and the actual common-regularization law, not a constructed infinite-depth \(K_\infty\)-covariance Gaussian field. No convergence rate in \(T\) or over covariance shapes is supplied. The finite-depth positivity limit and source \(N\to\infty\) are sequential.

**052–058.** The static rates \(L_0\), \(2^{\kappa_{\rm st}}L_0\), and the static coefficient upper rates are imported from Chen–Hu; the dual sources require the generalized-covariance convention (2.18) and Dalang finiteness, which the module supplies. The static norm series is proved via 051 **afterwards**, so these sections cannot be used to prove 051. Zero-noise \(L_0=0\) is excluded from the ratio in 058.

**060.** The complex Laplace identity (F088 (6.3)) and Gaussian characteristic function are imported; the candidate is only the direct unweighted constant-correlation clock copy. No ordering correction, diagonal representation, asymptotic route, or Skorohod development is provided.

**Global.** The standing covariance hypothesis `H:homog`, the imported Crouzeix–Palencia theorem, the imported Chen2023 quartic finiteness, and the imported Chen–Hu static statements remain external primary hypotheses; all remaining coupling and coefficient deductions above are supplied by the named proof bodies, and none of the original all215/241/13 debts is changed by this focused reconstruction.