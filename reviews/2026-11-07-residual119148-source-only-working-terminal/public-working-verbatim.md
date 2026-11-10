## PROOF119
**Current statement** (the entire `L:exact-canonical-scaling` lemma). Under Hypothesis H:homog with $a=\alpha_0\in(0,1)$, define
$$\kappa=\frac{4-\alpha-a}{3-\alpha},\qquad \delta=T^{-\kappa},\qquad r_T=T\delta=T^{\beta/2\kappa},\quad \beta=4-\alpha-a,$$
so that $r_T=T^{(a-1)/(3-\alpha)}$. Then for every $T>0$ the law of $u(Tt,r_T x)$ equals the law of the canonical expansion solution $V_\delta(t,x)$ with data $(1,0)$ of
$$\delta^2\partial_t^2 V_\delta=\Delta V_\delta+\sqrt\delta\,\dot W\,V_\delta,$$
where $\dot W$ has the original raw covariance. Consequently
$$T^{-\kappa}\log\mathbb E|u(T,0)|^2=\delta\log\mathbb E|V_\delta(1,0)|^2.$$
The assertion is equality in law only; no pathwise uniqueness for a full rough solution is assumed.

**Constants/domains/hypotheses.** Admissible $d\in\{1,2,3\}$, $\Gamma$ homogeneous of degree $-\alpha$ in the tempered-Radon sense (including white noise $d=\alpha=1$), $\alpha+\alpha_0<2$; positivity of $\kappa\in(1,2)$ holds since $\beta>2$.

**Derivation as supplied.** At positive widths, time--space dilation of the Gaussian source gives covariance amplitude $T^{-a}r_T^{-\alpha}$, obtained distributionally from $\Gamma(cA)=c^{d-\alpha}\Gamma(A)$; white noise is included. Source cutoffs transform by $K_\eta(Ts)=T^{-a}K_{\eta/T}(s)$ and $\epsilon\mapsto\epsilon/r_T^2$, preserving the joint maximum-time/summed-space width laws at every vertex. The Green measure scales as
$$G_d(T\tau,r_T\ud z)=r_T\,G_d(\tau/\delta,\ud z),$$
from the degree $1-d$ distributional scaling, including the sphere measure in $d=3$. Each terminal Duhamel vertex contributes $T r_T T^{-a/2} r_T^{-\alpha/2}$. The two exact algebraic identities are
$$T^{-a/2}r_T^{1-\alpha/2}=\delta^{-1/2},\qquad T^{1-a/2}r_T^{1-\alpha/2}=\sqrt\delta,$$
the first being used after substitution (the displayed two exponents are exactly equivalent). The Green kernel of the fast equation is $\delta^{-1}G_d((t-s)/\delta)$; multiplied by $\sqrt\delta$ it gives precisely the vertex factor. Hence every finite list of fixed-order coefficients (all self-pairings, unequal and empty chains) has the same joint law under dilation. Green smoothing in $d=3$ is removed first, with its width divided by $r_T^2$ on the scaled side. Lemma `L:joint-fixed-order` and the absolute $L^2$ summability in Lemma `L:vertex-crude` pass the identities to the canonical series and its second moment. No large-time/source limit interchange occurs.

**Consumed/unproved conditions.** Consumes `L:joint-fixed-order` (fixed-order joint diagram limits) and `L:vertex-crude` (vertexwise $L^2$ summability) from the main file. The Green-before-noise order in $d=3$ is part of the dilation statement. No samplewise identity for all $T$ at once is asserted; it is equality in law at each fixed $T$.

## PROOF120
**Current statement** (`L:raw-block-inputs`). For integer $B\ge1$, $0<\delta<\min(1,1/B)$, define $N=\lfloor1/(\delta B)\rfloor$, $s_m=m\delta B$, $\tau=\delta^{-1}-NB\in[0,B)$, $g_\delta=\delta^{(1-a)/2}$, and for a smooth compact positive-fast-time test $f$ extended by zero,
$$T_{\delta,m}f(s,x)=\delta^{a/2-1}f((s-s_m)/\delta,x),\qquad W_{\delta,m}(f)=W(T_{\delta,m}f).$$
With $\mathscr B_0=h_0^\theta([0,B];\mathcal K(F))$ (the $C^\theta$ closure of zero-initial polygonal compact-operator paths, $F=E\oplus\mathbb R^2$), $\mathscr B_\delta=\mathscr B_0^{N+1}$ with maximum norm, and $X_m:=g_\delta A_R(W_{\delta,m})$, the vector $(X,Z)$, $X=(X_m)_{m=0}^N$, is jointly centered Banach Gaussian, and the Bochner covariance is
$$b:=\mathbb E[XZ]=\sqrt\delta\,H,\qquad H=(H_m)_{m=0}^N,\qquad H_m(u)=\int_0^u S_F(-r)iB_F(V_{s_m+\delta r})S_F(r)\ud r,$$
where $V_s=m_R h_s$ is the masked mean of the original control $\Psi$, and the convolution formula for $h_s$ is extended smoothly to $s\in[0,2]$. Moreover, for $p\ge1$,
$$\|X_m\|_{L^p(\mathscr B_0)}\le C_{R,B}\sqrt p\,g_\delta.$$

**Derivation as supplied.** Pullback of the raw covariance gives the factor $\delta^{a-2}\delta^2\delta^{-a}=1$, so each $T_{\delta,m}$ extends isometrically through the null quotient; the literal identity $W_{\delta,m}(f)=W_{\mathrm{fast}}(f(\cdot-mB,\cdot))$ holds. $\mathscr B_0$ is separable: finite-rank rational matrices in a countable Hilbert basis are dense in $\mathcal K(F)$, and polygonal approximation with breakpoint bounds uses $[f]_\theta\le(2\|f\|_\infty)^{1-\theta}\mathrm{Lip}(f)^\theta$, so every zero-initial Lipschitz compact-valued path lies in $\mathscr B_0$. The finite raw coefficient paths $iA_jL_\psi$ converge in $L^pC^\theta$, giving the moment bound. Gaussianity is inherited by scalar continuous functionals through $L^2$ limits. The key covariance calculation is
$$\mathbb E[W_{\delta,m}(f)Z]=\delta^{a/2}\int f(u,x)h_{s_m+\delta u}(x)\ud x\ud u,$$
justified by absolute Fubini (compact supports, local Radon mass, $a<1$), then passed to indicator time tests through raw-norm approximation and to the constant columns of $F$ via finite propagation and boundedness, giving $b=\sqrt\delta H$. The span of $E$ and both constant coordinates is dense in $F$; $E$ alone is not.

**Consumed/unproved conditions.** Consumes the actual $F$-driver $A_R$ of the constant-phase Young section (F009) and the compact-mean $V_s$. Only covariance (not independence) of the blocks is claimed.

## PROOF121
**Current statement** (`P:raw-block-gaussian-law`). On all of the separable Banach space $\mathscr B_\delta$, for every nonnegative norm-Borel $j$,
$$\mathbb E\, j(X)=\mathbb E\left[e^{-Z/\sqrt\delta-v/(2\delta)}\,j(X+H)\right],$$
valid also as an extended nonnegative integral. Here $v=v_\Psi=\mathbb E Z^2$ and $Z=W(\Psi)$ is the single original raw variable.

**Derivation as supplied.** For real $s$, $e^{-sZ-s^2v/2}$ is a completed-square Radon–Nikodym factor making a probability $\mathbb Q_s$. For every finite list $\ell$ of continuous real coordinates, $(\ell(X),Z)$ is equal in law to $(TG,z\cdot G)$ with $Tz=\ell(b)$, $|z|^2=v$ via a (possibly singular) positive square root; no covariance inverse is used. Substituting $G'=G+sz$ gives $\mathbb E_{Q_s}f(\ell(X+sb))=\mathbb E f(\ell(X))$ for all bounded Borel $f$. One then takes $s=\delta^{-1/2}$, using $sb=H$. The norm-Borel sigma-field is generated by matrix entries at rational times plus $0,B$, because $\|T\|=\sup_{u,w\in\mathcal D}|\langle Tu,w\rangle|$ over a countable dense set $\mathcal D$ and the Hölder and supremum norms are suprema over rational times/pairs. Separability makes open sets countable unions of balls from dense centers, and the cylinders form a generating $\pi$-system; uniqueness of measures extends the identity. The map and its deterministic translate are defined on the entire input space, so no exceptional translated domain arises.

**Consumed/unproved conditions.** Finite Gaussian law on one fixed finite tuple in one norm-Borel Banach space; no quasi-invariance or Borell statement for infinite-dimensional Gaussian measure is made, and no covariance inverse or independent block actions are introduced.

## PROOF122
**Current statement** (`L:raw-block-uniform-error`). Let $M_\delta=\max_{m\le N}\|X_m\|_{\mathscr B_0}$ (including the factor $g_\delta$). Then $M_\delta\to0$ in every finite $L^q$ and for some $c>0$, $\sup_\delta\mathbb E e^{cM_\delta^2}<\infty$. With $D_x(u)=S_F(u)U_x(u,0)$ (everywhere-defined linear Young map), $D_m^0=D_{X_m}$, $D_m^+=D_{X_m+H_m}$, and $P_s$ the actual deterministic compact-mean physical flow, one has
$$E_{\mathrm{op},\delta}:=\max_{m\le N}\sup_{0\le u\le B}\|D_m^+(u)-P_{s_m}(u)\|_{\mathcal B(F)}\longrightarrow0$$
in every finite $L^q$.

**Derivation.** Maximum plus moment bound and $N+1\le2/\delta$ give
$$\|M_\delta\|_p\le C'\sqrt p\,\delta^{(1-a)/2-1/p},$$
so choosing $p>2/(1-a)$ proves the limit. The square-exponential bound follows by splitting moments into a fixed finite head and a geometric tail using $n!\ge(n/e)^n$. Let $H_m^{\mathrm{stat}}$ be the primitive for constant potential $V_{s_m}$; compact-mean smoothness on $[0,2]$ gives $\sup_m\max(\|H_m\|_{C^\theta},\|H_m^{\mathrm{stat}}\|_{C^\theta})\le H_0$ and $\sup_m\|H_m-H_m^{\mathrm{stat}}\|_{C^\theta}\le C\delta$. On $\{M_\delta\le1\}$ the local Young stability gives $E_{\mathrm{op},\delta}\le C(M_\delta+\delta)$, hence convergence in probability; uniform integrability comes from the global Young bound and the exponential moment with $1/\theta<2$.

**Consumed/unproved conditions.** Consumes local Young stability (F009) and compact-mean smoothness (F010). Quantifier order: $B$ is fixed (later chosen by the cone lemma), then $\delta\downarrow0$.

## PROOF123
**Current statement** (`L:raw-block-indexed-cone`). Fix $0<\varrho<1/2$. There exist an integer $B\ge1$ and positive $\omega,\epsilon_{\mathrm{op}},c_*$ such that for every $N\ge1$: if $\sigma_0,\dots,\sigma_N\in I=[0,1]$ have adjacent distances at most $\omega$ and $D_m(u)$ ($0\le u\le B$) satisfy $\max_{m\le N}\sup_u\|D_m(u)-P_{\sigma_m}(u)\|\le\epsilon_{\mathrm{op}}$, then for $0\le u\le B$,
$$O_\phi D_N(u)D_{N-1}(B)\cdots D_0(B)e_0\ \ge\ c_*(1-\varrho)^{N-1}\exp\left(B\sum_{m<N}\lambda_{\sigma_m}+u\lambda_{\sigma_N}\right)>0.$$
No positivity, composition, or independence assumption on the $D_m$ is required.

**Derivation.** From the normalized complement bound $\|e^{-\lambda_s t}P_s(t)Q_s\|\le C_{\mathrm{gap}}e^{-\eta_{\mathrm{gap}}t}$ fix $C_{\mathrm{gap}},\eta_{\mathrm{gap}}$, then define positive margins $a_*=\inf_I\ell_s(e_0)$, $j_*=\inf_I O_\phi(e_s)$, $M_e,M_\ell,M_P,M_Q,M_z,E_0,H_{\mathrm{obs}}$. Choose aperture first $\vartheta=\min(1,j_*/(16H_{\mathrm{obs}}C_{\mathrm{gap}}))$, then $B$ with $q_B=C_{\mathrm{gap}}e^{-\eta_{\mathrm{gap}}B}\le\min(1/8,\vartheta a_*/(8M_QE_0))$, then $\nu$ with $\nu M_z\le\min(\varrho/2,\vartheta,1/4)$, then $\omega$ for adjacent-index continuity, and finally $\epsilon_{\mathrm{op}}$ satisfying the five explicit budgets $M_\ell\epsilon M_z\le\varrho/2$, $M_Q\epsilon M_z\le\vartheta/4$, $M_\ell\epsilon E_0\le a_*/2$, $M_Q\epsilon E_0\le\vartheta a_*/8$, $H_{\mathrm{obs}}\epsilon M_z\le j_*/8$. The cone is $z=Ae_s+r$ with $A=\ell_s(z)>0$, $\ell_s(r)=0$, $\|r\|\le\vartheta A$. Entrance gives amplitude $\ge e^{\lambda_b B}a_*/2$ and residual ratio $\le\vartheta/2$. For adjacent-index continuation, rebase using $\ell_c(z)\ge(1-\nu M_z)A$ and $\|Q_cz\|\le(\vartheta+\nu M_z)A$; the perturbation bounds give $y\le\vartheta x$ and the amplitude factor $e^{\lambda_cB}(1-\varrho)$. The terminal partial block gives at least $j_*/2$ times the rebased amplitude. The final constant is $c_*=a_*j_*/4$, and the order of choices uses the normalized complement rather than any growing terminal norm.

**Consumed/unproved conditions.** The aperture is chosen before $B$; all five budgets are explicit. This is a deterministic cone statement, not a probabilistic estimate; it is the content of `L:raw-block-indexed-cone`.

## PROOF124
**Current statement** (`L:raw-block-restart`). Fix $\delta,B,N$, let $L=\delta^{-1}$, $L_{\mathrm{ext}}=(N+1)B\ge L$. On the global fast horizon define $A_{\mathrm{glob}}=g_\delta A_R(W_{\mathrm{fast}})$. Its actual physical flow satisfies
$$P_{\mathrm{glob}}(mB+u,mB)=D_m^0(u),\qquad 0\le u\le B,$$
and the analogous identity with the deterministic mean $V_{\delta t}$ added globally and local drivers $X_m+H_m$. The finite block products, including the last remainder $\tau$, are actual source limits in $L^2$ at fixed $(\delta,N)$.

**Derivation.** Take one retaining slow source $Y_{\epsilon,\eta}$ on the extension of $W$ (F007). Define $Y_{\mathrm{fast}}(f)=Y_{\epsilon,\eta}(T_{\delta,0}f)$ and $Y_m(f)=Y_{\epsilon,\eta}(T_{\delta,m}f)$. The pullback isometry and the two raw variance dominations give source/residual bounds by $\|f\|_{H_W}^2$; Gaussian transfer gives $L^pC^\theta$ first-driver limits including both constant columns. The pointfield identities $Y_{\mathrm{fast}}(u,x)=\delta^{a/2}Y_{\epsilon,\eta}(\delta u,x)$ and $Y_m(u,x)=Y_{\mathrm{fast}}(mB+u,x)$ follow by test change of variables; temporal law $K_{\eta/\delta}$ uses $\delta^aK_\eta(\delta r)=K_{\eta/\delta}(r)$. The ordinary primitives equal the Gaussian-transfer drivers via the indicator approximation. The exact conjugation identity
$$S_F(mB)[A_{\mathrm{glob}}^{\mathrm{src}}(mB+u)-A_{\mathrm{glob}}^{\mathrm{src}}(mB)]S_F(-mB)=X_m^{\mathrm{src}}(u)$$
holds without commuting any mask through a wave group. Conjugating the global interaction Young equation by $S_F(mB)$ and using uniqueness gives the cocycle identity for the raw sum as well. For the finite product source convergence: with $C\ge1$ the maximum factor norm and $e_{\mathrm{src}}$ the maximum factor difference, the recurrence $d(n+1)\le C d(n)+C^n e_{\mathrm{src}}$ gives $d(N+1)\le(N+1)C^{N+1}e_{\mathrm{src}}$; Hölder with $C\in L^{4(N+1)}$ and $e_{\mathrm{src}}\in L^4$ yields the $L^2$ convergence. This is only a fixed-$\delta$ source limit; no finite-source Cameron mean is substituted.

**Consumed/unproved conditions.** Consumes `P:source-gaussian-transfer` (F007) and `P:constant-gaussian-flow` (F009). The finite-product $L^2$ telescoping estimate requires the $L^{4n}$ norm control; it does not give any uniform estimate as $N$ grows.

## PROOF125
**Current statement** (`P:raw-block-point-comparison`). Define
$$U_{\delta,B}=O_\phi D_N^0(\tau)D_{N-1}^0(B)\cdots D_0^0(B)e_0,\qquad Y_{\delta,B}=O_\phi D_N^+(\tau)D_{N-1}^+(B)\cdots D_0^+(B)e_0.$$
Both have all finite unweighted moments, and
$$\mathbb E U_{\delta,B}^2=\mathbb E\left[e^{-Z/\sqrt\delta-v/(2\delta)}Y_{\delta,B}^2\right],\qquad \mathbb E U_{\delta,B}^2\le\mathbb E|V_\delta(1,0)|^2=\mathbb E|u(T,0)|^2,\quad\delta=T^{-\kappa}.$$

**Derivation.** On all of $\mathscr B_\delta$ set $j_\delta(x)=|O_\phi D_{x_N}(\tau)\cdots D_{x_0}(B)e_0|^2$; it is everywhere defined and continuous, so PROOF121 applies directly to obtain the exact square identity with the original $Z,v$; no prior integrability of $j_\delta$ is needed, and no tilted-source convergence is used. For the comparison: put $\Gamma_\delta=g_\delta^2\Gamma$ and $W'=g_\delta W_{\mathrm{fast}}$; since the raw matrix forms are linear in noise and Gaussian transfer retains the constant columns, its first driver is $g_\delta$ times the original one, and the $n$-th source chain is multiplied by $g_\delta^n$. The source-limit premise of the masked comparison is discharged at fixed $\delta,N$ using the retaining source; the telescoped product error with $n=N+1$ and Hölder with exponents $4n$ and $4$ gives $L^2$ convergence; no uniform-in-$N$ source estimate is needed. The physical source identification (`L:constant-source-solution`) identifies the source product with the tested ordinary masked solution at fast time $L=1/\delta$, and `P:masked-source-moments` gives tested comparison. Since $0\le m_R\le1$ multiplies each nonnegative Wick integrand by a product of vertex masks, the vertex-wise comparison includes unequal/self/empty chains; `P:masked-canonical-transfer` at $\Gamma_\delta$ then gives $\mathbb EU_{\delta,B}^2\le\mathbb E|u_{\Gamma_\delta}(L,0)|^2$. The change from fast to slow time maps the unmasked source equation into the regularized version of $\delta^2V_{\delta,tt}=\Delta V_\delta+\sqrt\delta\,\dot WV_\delta$ with slow terminal time one, matching `L:exact-canonical-scaling`. The mask radius $R$ is fixed and need not contain the growing backward cone: the comparison is a moment inequality, not equality of fields.

**Consumed/unproved conditions.** Consumes PROOF121, the masked comparison (F008), the constant-source-flow identification (F009), the source restarts (PROOF124), and the exact scaling (PROOF119). Only noise-only products are used in the masked passage; the shifted product is already the everywhere-defined $j_\delta(X+H)$.

## PROOF126
**Current statement** (`P:raw-block-original-lower`). For every original positive $\Psi\in C_c^\infty((0,1)\times\mathbb R^d)$ and each eligible fixed mask $R$, and every fixed $x\in\mathbb R^d$,
$$\liminf_{T\to\infty}T^{-\kappa}\log\mathbb E|u(T,x)|^2\ \ge\ 2\int_0^1\lambda_s\ud s-\frac{v_\Psi}{2}.$$

**Derivation.** Fix $\epsilon_{\mathrm{rate}}>0$, choose $\varrho<1/2$ with $\log(1-\varrho)>-\epsilon_{\mathrm{rate}}/3$, and fix $B$ and the cone constants from PROOF123. With $p>2/(1-a)$ and $\gamma_p=p(1-a)/2-1>0$, Markov plus the union over blocks gives $\mathbb P(M_\delta>\eta)\le A_p\eta^{-p}\delta^{\gamma_p}$. The deterministic tolerance $E_{\mathrm{op},\delta}\le L_B(M_\delta+\delta)$ gives the event
$$E_\delta=\{E_{\mathrm{op},\delta}\le\epsilon_{\mathrm{op}}\}\cap\{|Z|\le\delta^{-1/4}\},$$
with $p_\delta=\mathbb P(E_\delta)\ge1-A_p\eta^{-p}\delta^{\gamma_p}-v\delta^{1/2}\to1$. This is one union bound; no block independence and no product of probabilities. The smallness conditions include $\delta B\le\omega$, $C_\lambda\delta B\le\epsilon_{\mathrm{rate}}/3$, $\delta|\log c_*|\le\epsilon_{\mathrm{rate}}/3$. On $E_\delta$ the cone lemma gives
$$\delta\log Y_{\delta,B}\ge\delta\log c_*+\delta(N-1)\log(1-\varrho)+\delta B\sum_{m<N}\lambda_{s_m}+\delta\tau\lambda_{s_N}\ge(I_R-\epsilon_{\mathrm{rate}})/\delta,$$
because the last two terms form the left Riemann sum for $I_R$ over $[0,1]$ with the terminal remainder interval included. Then PROOF125 and the nonnegativity of the density give
$$\mathbb E|u(T,0)|^2\ge p_\delta\exp\left((2I_R-2\epsilon_{\mathrm{rate}}-v/2)/\delta-\delta^{-3/4}\right),$$
hence $\delta\log\mathbb E|u(T,0)|^2\ge2I_R-2\epsilon_{\mathrm{rate}}-v/2-\delta^{1/4}+\delta\log p_\delta$. The linear penalty $\delta^{1/4}\to0$ and $\delta\log p_\delta\to0$; the quadratic cost is exactly $v/2$. Since $\delta=T^{-\kappa}$ bijects small $\delta$ and large $T$, this gives the continuous-time liminf $Q_2\ge2I_R-2\epsilon_{\mathrm{rate}}-v/2$; only then let $\epsilon_{\mathrm{rate}}\downarrow0$. No $B=B(\delta)$ is chosen. Spatial translation of all vertices preserves the law and Green kernels, so $0$ can be replaced by any fixed $x$.

**Consumed/unproved conditions.** Consumes PROOF123 and PROOF125. Order of quantifiers: fix $\Psi$, mask $R$, cone $B$, source limits at fixed $\delta$; then $\delta\downarrow0$; then rate tolerance $\downarrow0$.

## PROOF127
**Current statement** (`L:variational-heat-envelope`). With $p_\epsilon=(2\pi\epsilon)^{-d/2}e^{-|x|^2/(2\epsilon)}$,
$$(\Gamma*p_\epsilon)(x)=\int e^{i\xi\cdot x}e^{-\epsilon|\xi|^2/2}\mu(\ud\xi),\qquad 0\le(\Gamma*p_\epsilon)(x)\le(\Gamma*p_\epsilon)(0)<\infty,$$
and the value at zero is strictly positive.

**Derivation.** Positive tempered Radon measures have polynomial ball growth by evaluating the tempered bound on dilated cutoffs; dyadic summation makes $(1+|x|)^{-L}$ integrable for large $L$. Thus Gaussian weights are integrable against both $\Gamma$ and $\mu$. Pairing the (finite) convolution with a Schwartz test and using the spectral convention of H:homog plus $\int p_\epsilon(y)e^{-i\xi\cdot y}\ud y=e^{-\epsilon|\xi|^2/2}$ yields equality of the two continuous distributions at every $x$, without extra normalization. Nonnegativity and the domination by the real, even-mass value at zero follow; $\Gamma\ne0$ and $p_\epsilon>0$ give strict positivity at zero.

**Consumed/unproved conditions.** None beyond H:homog and positive-tempered-Radon structure. This records the spectral pairing, not a directional decay.

## PROOF128
**Current statement** (`L:variational-global-mean`). Every mixed time–space derivative of $h_s$ is globally bounded in space, uniformly on compact time intervals; in particular there exist finite $M,C_\Psi$ with
$$0\le h_s(x)\le M,\qquad \|h_s-h_t\|_\infty\le C_\Psi|s-t|,\qquad s,t\in I=[0,1].$$

**Derivation.** Extending $\Psi$ by zero and using compactness of its spatial support, each derivative satisfies $|D\Psi(t,x)|\le C_D p_\epsilon(x)$ on the support for a fixed $\epsilon>0$; PROOF127 bounds $\Gamma*|D\Psi|$ uniformly. Differentiation under the Radon integral is justified; with $r=s-t$,
$$h_s(x)=\int_{\mathbb R}|r|^{-a}(\Gamma*\Psi(s-r,\cdot))(x)\ud r,$$
and on compact $s$-intervals the $r$-domain is bounded, so the uniform bound times $|r|^{-a}$ is integrable ($a<1$). This gives global spatial bounds and the Lipschitz estimate; nonnegativity is from positive kernels. No directional decay of the mean is inferred.

## PROOF129
**Current statement** (`P:variational-unmasked-rate`). On complex $L^2(\mathbb R^d)$, $H_s=-\Delta-h_s$ is self-adjoint on $H^2$, with form domain $H^1$ and form $q_s(f)=\|\nabla f\|_2^2-\int h_s|f|^2$. Its bottom $E_s<0$ uniformly on $I$, and $\lambda_{\Psi,s}=\sqrt{-E_s}$ satisfies the real Rayleigh formula
$$\lambda_{\Psi,s}^2=\sup_{f\in H^1(\mathbb R^d;\mathbb R),\,\|f\|_2=1}\left(\int h_sf^2-\|\nabla f\|_2^2\right).$$
The rate is Lipschitz on $I$ and $I_\Psi=\int_0^1\lambda_{\Psi,s}\ud s$ is positive and finite. No eigenstate at the unmasked bottom is asserted.

**Derivation.** $A=-\Delta$ is self-adjoint on $H^2$; $B_s=-h_s$ is bounded self-adjoint with norm at most $M$. Closedness and self-adjointness follow from $(H_s-ib)$ having a Neumann inverse for $b>M$ and the kernel argument $u-v\in\ker(H_s^*-ib)=\operatorname{Ran}(H_s+ib)^\perp=\{0\}$. With $c_{\mathrm{shift}}=1+M$ and $J_s=H_s+c_{\mathrm{shift}}\ge1$, integration by parts gives $\|J_s^{1/2}f\|_2^2=q_s(f)+c_{\mathrm{shift}}\|f\|_2^2$ and $H^1$-equivalence, identifying $D(J_s^{1/2})=H^1$. The Rayleigh identity in both directions follows from nonzero spectral projections and the real/complex quotient splitting $q_s(u+iv)=q_s(u)+q_s(v)$. The negative floor uses `P:compact-original-common-trial` (from F010) giving a unit compactly supported $w$ and finite plateau mask with common negative margin $\epsilon_0$; the unmasked form is no larger, so $-M\le E_s\le-\epsilon_0<0$ and $\sqrt{\epsilon_0}\le\lambda_{\Psi,s}\le\sqrt M$. The Lipschitz bound
$$|\lambda_{s}-\lambda_t|\le\frac{C_\Psi}{2\sqrt{\epsilon_0}}|s-t|$$
comes from comparing unit form tests.

**Consumed/unproved conditions.** Consumes `P:compact-original-common-trial` (F010) for the strict negative bound, and `L:variational-global-mean` (PROOF128). No unmasked ground eigenstate and no compact-potential spectral theorem for $H_s$ are asserted.

## PROOF130
**Current statement** (`P:variational-remove-mask`). There is an increasing family of admissible radial masks $m_R\to1$ such that $\lambda_{R,s}\uparrow\lambda_{\Psi,s}$ uniformly on $I$ for $R\ge R_0(\Psi)$, and for the original canonical solution and any fixed $x$,
$$\liminf_{T\to\infty}T^{-\kappa}\log\mathbb E|u(T,x)|^2\ \ge\ 2I_\Psi-\frac{v_\Psi}{2}.$$

**Derivation.** Use $\chi(r)=F(2-r)/(F(2-r)+F(r-1))$, $F(t)=e^{-1/t}\mathbf1_{t>0}$, and $m_R(x)=\chi(|x|/R)$; smoothness at zero holds since $\chi$ is locally constant. Choose $R_0$ containing the common trial, so every $R\ge R_0$ has the same negative margin. For fixed $R$, the compact-family theorem applies to $m_Rh_s$; its real Rayleigh formula holds as in PROOF129. Monotone convergence of $m_Rh_s$ gives, by interchanging only the two numerical suprema,
$$\sup_{R\ge R_0}\lambda_{R,s}^2=\sup_{\|f\|_2=1,\ f\in H^1(\mathbb R^d;\mathbb R)}\sup_{R\ge R_0}\left(\int m_Rh_sf^2-\|\nabla f\|_2^2\right)=\lambda_{\Psi,s}^2.$$
Uniform convergence on compact $I$ follows from increasing open covers; thus $\int_I\lambda_{R,s}\ud s\uparrow I_\Psi$. For each fixed $R$ the same mask is used in PROOF126, giving a lower bound with $2\int\lambda_{R,s}\ud s-v/2$; taking the supremum over $R$ proves the statement.

**Consumed/unproved conditions.** Consumes PROOF126 for each fixed $R$. There is no $R(T)$, no unmasked noisy wave, and no uniform-in-mask Gaussian estimate; only numeric suprema of individually proved lower bounds are taken.

## PROOF131
**Current statement** (`L:variational-control-dilation`). For $r>0$, $(D_r\Psi)(s,x)=r^{d+2-\alpha}\Psi(s,rx)$ is a bijection of the full positive class $\mathcal C_{\mathrm{pos}}$ with inverse $D_{1/r}$, and with the same covariance,
$$h_{D_r\Psi,s}(x)=r^2h_{\Psi,s}(rx),\qquad v_{D_r\Psi}=r^{4-\alpha}v_\Psi,\qquad \lambda_{D_r\Psi,s}=r\lambda_{\Psi,s},\qquad I_{D_r\Psi}=rI_\Psi.$$

**Derivation.** Positive dilation preserves smoothness, nonnegativity, nonzero support, and compact support; amplitude powers give the inverse. For the Radon pushforward, homogeneity gives $\int G(ry)\Gamma(\ud y)=r^{\alpha-d}\int G(z)\Gamma(\ud z)$; inside the temporal convolution this yields the $r^2$ mean relation. The raw variance uses the Lebesgue substitution $z=rx$:
$$v_{D_r\Psi}=r^{d+2-\alpha}\cdot r^2\cdot r^{-d}v_\Psi=r^{4-\alpha}v_\Psi,$$
distinguishing Radon pushforward from the spatial volume factor; singular and white covariances are included. The unitary $U_rf(x)=r^{d/2}f(rx)$ gives $\|\nabla U_rf\|_2^2=r^2\|\nabla f\|_2^2$ and $\int h_{D_r\Psi,s}(U_rf)^2=r^2\int h_{\Psi,s}f^2$, so the real Rayleigh bijection gives the squared rate identity; positivity of rates gives the scalar rate and integral identities. Time is not rescaled; for compact masks the identity uses $m_R(rx)=m_{R/r}(x)$, so a fixed mask radius is not invariant.

## PROOF132
**Current statement** (`P:variational-positive-scores`). For $c>0$, the score set $\{cI_\Psi-v_\Psi/2\}$ is nonempty and bounded above; its finite real supremum $S_c^{\mathrm{pos}}>0$ satisfies
$$S_c^{\mathrm{pos}}=c^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}},\qquad Q_2\ge S_2^{\mathrm{pos}}.$$
The label-one value is only an auxiliary variational score; no first-moment or source-constant identification is asserted.

**Derivation.** With $k=3-\alpha>0$, $q=4-\alpha=k+1$, $m=q/k>1$, fix a positive test $\Psi_0$ with $I_0,v_0>0$; the choice $r_0=(I_0/v_0)^{1/k}$ (any positive value) gives $I_{D_{r_0}\Psi_0}-v_{D_{r_0}\Psi_0}/2=r_0I_0/2>0$, so the set is nonempty. For $c>0$, $r_c=c^{1/k}$, $K_c=c^m$, the exact real-power identity gives
$$cI_{D_{r_c}\Psi}-v_{D_{r_c}\Psi}/2=K_c(I_\Psi-v_\Psi/2),$$
and since $D_{r_c}$ is a bijection, the whole $c$-score set equals $K_c$ times the whole label-one score set. Boundedness is proved before finite-real suprema by invoking the independent upper Theorem `T:full-upper` for the same canonical solution: $\mathbb E|u(T,0)|^2\le e(T+2)^d e^{C_{\mathrm{up}}T^\kappa}$ with $C_{\mathrm{up}}<\infty$; the prefactor is negligible under $T^{-\kappa}$, so the point limsup is at most $C_{\mathrm{up}}$ and every label-two score is at most this same $Q_2\le C_{\mathrm{up}}$. The set equality at $c=2$ bounds every label-one score by $C_{\mathrm{up}}/K_2$. Hence $S_1^{\mathrm{pos}}$ is a positive finite real number, and for general $c$ the same set equality gives $S_c^{\mathrm{pos}}=K_cS_1^{\mathrm{pos}}$. Numerical supremum of the label-two lower bounds from PROOF130 gives $Q_2\ge S_2^{\mathrm{pos}}$. Although $2^m>2$, $S_2^{\mathrm{pos}}>2S_1^{\mathrm{pos}}$ is only an auxiliary-score comparison, not a Jensen improvement.

**Consumed/unproved conditions.** The key dependency is the independent upper Theorem `T:full-upper` (051). Its interval proof does not consume PROOF132, the intrinsic result (204), or the actual operator driver (085/093); it uses the interval-field coefficient estimate, the bounded-operator CP input, and the fixed-order construction. The statement records this independence. No fixed separable control class is invoked: the supremum is a finite-real supremum over the full positive class, and the set scaling is pointwise.

## PROOF133
**Current statement** (`L:equilibrium-gamma-beta`). For positive arguments,
$$\Gamma_E(x+1)=x\Gamma_E(x),\qquad \mathrm{Beta}(x,y)=\frac{\Gamma_E(x)\Gamma_E(y)}{\Gamma_E(x+y)},\qquad \Gamma_E(2x)=\frac{2^{2x-1}\Gamma_E(x)\Gamma_E(x+1/2)}{\sqrt\pi}.$$

**Derivation.** Integration by parts gives the recurrence. Setting $(u,v)=(Rt,R(1-t))$ in the product Gamma integral with Tonelli gives the Beta–Gamma identity. Symmetry and $t=(1+v)/2$, $v^2=w$ give $\mathrm{Beta}(x,x)=2^{1-2x}\mathrm{Beta}(1/2,x)$; $\Gamma_E(1/2)=\int_{\mathbb R}e^{-z^2}\ud z=\sqrt\pi$ by squaring and polar coordinates; substitution then proves duplication.

## PROOF134
**Current statement** (`L:temporal-equilibrium`). For $0<a<1$, $r=(1-a)/2$,
$$f_a(t)=\frac{[t(1-t)]^{-r}}{\Gamma_E(r)\Gamma_E(1-r)},\qquad 0<t<1,$$
is positive and belongs to $L^1(0,1)\cap L^2(0,1)$, with
$$\int_0^1|s-t|^{-a}f_a(t)\ud t=1\quad\text{for every }s\in[0,1],\qquad M_a:=\int_0^1f_a(t)\ud t=\frac{\Gamma_E((1+a)/2)}{\Gamma_E(1+a)\Gamma_E((1-a)/2)}>0.$$

**Derivation.** The positive binomial series $(1-z)^{-p}=\sum_{n\ge0}(p)_n z^n/n!$ for $0\le z<1$ is derived by termwise differentiation of $y=(1-z)^{-p}$; all terms nonnegative justifies Tonelli. Splitting the potential integral into left/right parts with $t=su$ gives
$$L(s)=\int_0^s(s-t)^{2r-1}[t(1-t)]^{-r}\ud t=r\,\mathrm{Beta}(1-r,2r)\,B_s(r,r),$$
and reflection makes the right part $L(1-s)$; the symmetry $B_s(r,r)+B_{1-s}(r,r)=\mathrm{Beta}(r,r)$ yields the full integral $r\,\mathrm{Beta}(1-r,2r)\mathrm{Beta}(r,r)=\Gamma_E(r)\Gamma_E(1-r)$ at all $s$, including the endpoints by direct Beta evaluation. Integrability uses $-r>-1$ and $-2r=a-1>-1$; the mass is
$$M_a=\frac{\mathrm{Beta}(1-r,1-r)}{\Gamma_E(r)\Gamma_E(1-r)}=\frac{\Gamma_E(1-r)}{\Gamma_E(2-2r)\Gamma_E(r)},$$
i.e. the displayed form. The time mass is explicitly not renormalized.

## PROOF135
**Current statement** (`L:spatial-physical-pair`). The positive measure $\nu(\ud x,\ud y)=\ud x\,\Gamma(\ud y)$ is sigma-finite. For nonnegative functions,
$$B_\Gamma(f,h)=\int f(x)h(x-y)\nu(\ud x,\ud y),$$
initially an extended nonnegative integral with finite Borel representatives; its value is representative independent, and Lebesgue-a.e. convergence transfers to $\nu$-a.e. convergence at both positions $x$ and $x-y$.

**Derivation.** Local finiteness of $\Gamma$ and sigma-finiteness of Lebesgue measure give sigma-finiteness on exhausting balls. If $N$ is Borel Lebesgue-null, Tonelli first in $x$ gives $\nu\{x\in N\}=0$ and $\nu\{x-y\in N\}=0$, since translations of null sets are null; arbitrary null sets have Borel null supersets. Signed pairings are used only after absolute convergence.

## PROOF136
**Current statement** (`L:spatial-static-controls`). For nonnegative nonzero $z\in C_c^\infty(\mathbb R^d)$, define
$$\lambda_z(c)^2=\sup_{g\in H^1(\mathbb R^d;\mathbb R),\|g\|_2=1}\left(c\int U_z g^2-b(g)\right),\qquad U_z=\Gamma*z,\ b(g)=\|\nabla g\|_2^2.$$
This is positive, finite, and Lipschitz on every compact positive $c$-interval. With the exact mass $M_a$,
$$S_1^{\mathrm{pos}}\ \ge\ \lambda_z(1)-\frac{M_a}{2}B_\Gamma(z,z).$$

**Derivation.** Choose nonnegative nonzero $f\in C_c^\infty(0,1)$ and $s_0=1/2$; the test $\Psi(t,x)=c f(t)z(x)/\int_0^1|s_0-t|^{-a}f(t)\ud t$ has mean $cU_z$ at $s_0$. PROOF129 supplies bounded potential, the displayed real Rayleigh formula, and positivity. Comparing identical unit tests makes $\lambda_z(c)^2$ Lipschitz with constant $\|U_z\|_\infty$; positivity on compact intervals gives the square-root Lipschitz bound. To approach the equilibrium, set $f_n(t)=f_a(t)\chi(1/(nt))\chi(1/(n(1-t)))$ with the smooth cutoff $\chi$ from PROOF130, extended by zero; then $k_n(s)=\int|s-t|^{-a}f_n(t)\ud t\uparrow1$ pointwise by monotone convergence and the potential normalization of PROOF134, with uniform bounds $0<c_0\le k_n(s)\le1$. The actual mean of $\Psi_n=f_n\otimes z$ is $k_n(s)U_z$, hence its actual rate is $\lambda_z(k_n(s))\to\lambda_z(1)$; dominated convergence gives $I_{\Psi_n}\to\lambda_z(1)$. The raw cost is
$$v_{\Psi_n}=B_\Gamma(z,z)\int_0^1 f_n(s)k_n(s)\ud s\to M_aB_\Gamma(z,z),$$
and finiteness/positivity of $B_\Gamma(z,z)$ uses the compact autocorrelation plus homogeneity scaling a positive-mass origin ball to every radius. Passing the individual inequalities $S_1^{\mathrm{pos}}\ge I_{\Psi_n}-v_{\Psi_n}/2$ to the limit proves the statement; the score differences need not be monotone.

**Consumed/unproved conditions.** Subset tests $\Psi_n$ do not restrict the full positive class: they only produce a lower bound for $S_1^{\mathrm{pos}}$ from a specific family. Positivity of $B_\Gamma(z,z)$ requires a positive-mass ball of $\Gamma$, which holds for every nonzero admissible $\Gamma$.

## PROOF137
**Current statement** (`P:spatial-smooth-ratio`). For real unit $g\in C_c^\infty(\mathbb R^d)$ let
$$R(g)=\frac{A_{\mathrm{sp}}(g)}{b(g)^{\alpha/2}},\qquad A_{\mathrm{sp}}(g)=B_\Gamma(g^2,g^2).$$
Its supremum $R_0$ over such profiles is a positive finite real number, and for every such $g$,
$$S_1^{\mathrm{pos}}\ \ge\ k\left[\frac{R(g)\alpha^{\alpha/2}}{8M_aq^{q/2}}\right]^{1/k},\qquad k=3-\alpha,\ q=4-\alpha.$$

**Derivation.** $b(g)>0$ by the Fourier argument (zero weak gradient forces concentration at $0$); $A>0$ by positivity of the autocorrelation of $g^2$ on an origin-centered ball of positive $\Gamma$-mass; finiteness is from local Radon mass. The dilation $U_\ell g=\ell^{d/2}g(\ell x)$ gives
$$A_{\mathrm{sp}}(U_\ell g)=\ell^\alpha A,\qquad b(U_\ell g)=\ell^2b(g),$$
with factors $\ell^{2d}\ell^{-d}\ell^{\alpha-d}$. Choose $z=\theta(U_\ell g)^2$; the Rayleigh test $U_\ell g$ gives $\lambda_z(1)^2\ge\theta\ell^\alpha A-\ell^2b$, and $B_\Gamma(z,z)=\theta^2\ell^\alpha A$. Put $u=\alpha/q$, $\ell^2=uL^2/b$, $\theta=(1+u)L^2/(\ell^\alpha A)$ for any $L>0$; PROOF136 gives $S_1^{\mathrm{pos}}\ge L-CL^q$ with $C=M_a(1+u)^2/(2R(g)u^{\alpha/2})$. The maximum over $L$ occurs at $L^k=1/(qC)$ and equals $(k/q)(qC)^{-1/k}$, which is the displayed formula after $1+u=4/q$. Finiteness of $R_0$ before rough extension uses the already finite $S_1^{\mathrm{pos}}$ to bound every smooth ratio; a normalized compact bump supplies positivity.

**Consumed/unproved conditions.** Uses the already-finite $S_1^{\mathrm{pos}}$ (PROOF132) inside the bound; this is legitimate because the bound is an upper bound on $R_0$, not a circular definition of $S_1^{\mathrm{pos}}$. Only smooth compact profiles (a subset of the full positive class) enter.

## PROOF138
**Current statement** (`P:spatial-four-linear`). For real $f\in H^1(\mathbb R^d)$, $N(f)=\|f\|_2^{1-\alpha/4}\|\nabla f\|_2^{\alpha/4}$; every physical square pairing is finite and
$$A_{\mathrm{sp}}(f)\le R_0N(f)^4,\qquad 0\le B_\Gamma(f^2,h^2)\le\sqrt{A_{\mathrm{sp}}(f)A_{\mathrm{sp}}(h)},$$
and the signed integral $C_4(f_1,f_2,f_3,f_4)=B_\Gamma(f_1f_2,f_3f_4)$ is absolutely convergent and jointly continuous on $(H^1)^4$ with
$$\int|f_1(x)f_2(x)f_3(x-y)f_4(x-y)|\ud\nu\le R_0\prod_{j=1}^4N(f_j).$$
The ratio supremum $R_{\mathrm{sp}}$ over all real unit $H^1$ profiles equals $R_0$, and every nonzero $H^1$ profile has $A_{\mathrm{sp}}(f)>0$.

**Derivation.** For smooth compact $f$ the homogeneous bound follows by normalization in $R_0$. Smooth signed covariance is nonnegative via the physical/spectral identity $B_\Gamma(Q,Q)=\int|\widehat Q_{\mathrm{ord}}(\xi)|^2\mu(\ud\xi)\ge0$; symmetry and the quadratic argument give covariance Cauchy–Schwarz. Cutoff and mollification give Schwartz density in $H^1$. For general $f,h$, take smooth approximants converging in $H^1$ and along a Lebesgue-a.e. subsequence; PROOF135 transfers convergence at both positions to $\nu$-a.e.; Fatou gives $B_\Gamma(f^2,h^2)\le R_0N(f)^2N(h)^2$. At this point Fatou supplies an inequality, not continuity. Continuity is then established by ordinary Cauchy–Schwarz under $\nu$ on $f_1(x)f_3(x-y)$ and $f_2(x)f_4(x-y)$, whose squared integrals are finite by the preceding bound; this gives the absolute four-linear bound and joint continuity, and PSD passes to the full class through continuity of the pairing. Positivity of $A_{\mathrm{sp}}(f)$ for nonzero $f$ uses $|f|\ge c>0$ on a bounded positive-measure set $E$ and the positivity of the autocorrelation of $1_E$ on an origin-centered ball of positive $\Gamma$-mass; no $H^1$-membership of $1_E$ is needed.

**Consumed/unproved conditions.** Fatou alone does not give continuity; the four-linear absolute bound and telescoping one argument at a time supply continuity. No Sobolev algebra, point trace, or Gamma-density is used.

## PROOF139
**Current statement** (`P:spatial-energy-map`). Define the own energy
$$\mathcal E_{\mathrm{sp}}=\sup_{\|g\|_2=1}\left(A_{\mathrm{sp}}(g)-\frac{b(g)}2\right).$$
Then
$$\mathcal E_{\mathrm{sp}}=\frac{2-\alpha}{2}\alpha^{\alpha/(2-\alpha)}R_{\mathrm{sp}}^{2/(2-\alpha)}\in(0,\infty),$$
and
$$S_1^{\mathrm{pos}}\ \ge\ M_a^{-1/k}F_0(\mathcal E_{\mathrm{sp}}),\qquad F_0(z)=k\left[\frac{(2z/(2-\alpha))^{(2-\alpha)/2}}{8q^{q/2}}\right]^{1/k},\quad z>0.$$

**Derivation.** PROOF138 extends the dilation law to all real $H^1$ profiles: $A_{\mathrm{sp}}(U_\ell g)=\ell^\alpha A$, $b(U_\ell g)=\ell^2b$. For fixed unit $g$ with $A,b>0$, maximizing $\ell^\alpha A-\ell^2b/2$ occurs at $\ell^{2-\alpha}=\alpha A/b$ with value $(2-\alpha)/2\,\alpha^{\alpha/(2-\alpha)}R(g)^{2/(2-\alpha)}$. Dilation preserves the unit class and includes $\ell=1$; interchanging the two numerical suprema and using profiles with ratio tending to $R_{\mathrm{sp}}$ proves the energy equality. Passing smooth ratios through PROOF137 and substituting $R_{\mathrm{sp}}\alpha^{\alpha/2}=(2\mathcal E_{\mathrm{sp}}/(2-\alpha))^{(2-\alpha)/2}$ gives the score bound. No optimizer is assumed. The kinetic coefficient is the half $b/2$; the label $F_0$ is only a scalar map name, and the covariance retains its original temporal exponent $a$.

## PROOF140
**Current statement** (`L:occupation-kernel-row`). For $u\ne0$,
$$K_\star(u)=\frac1{\Gamma_E(a)}\int_0^\infty e^{-(\lambda+\lambda^2/(2D))|u|}\lambda^{a-1}\ud\lambda,\qquad D=4-\alpha-2a>0,$$
and $K_\star(0)=0$ for time integration. The kernel is even, positive off zero, locally integrable, decreasing on $(0,\infty)$, $K_\star(u)\le|u|^{-a}$, and its exact row maximum on $[0,1]$ is
$$\max_{s\in[0,1]}\int_0^1K_\star(s-t)\ud t=R_\star:=2\int_0^{1/2}K_\star(u)\ud u\in(0,\infty).$$

**Derivation.** Dropping the positive quadratic damping bounds the mixture by the Gamma integral $|u|^{-a}$; positivity and monotonicity come from the integrand, and $a<1$ gives local integrability. With $\Phi(t)=\int_0^t K_\star(u)\ud u$ concave, the row is $\Phi(s)+\Phi(1-s)\le2\Phi(1/2)$ with equality at $s=1/2$; the diagonal value is irrelevant to time integrals. $D>0$ uses $\alpha+\alpha_0<2$ so $\alpha+2a<2$ holds with the definition $D=4-\alpha-2a=2(2-\alpha/2-a)>0$.

## PROOF141
**Current statement** (`P:occupation-physical-class`). Let $\mathcal O$ be the class of strongly $H^1$-measurable fields $s\mapsto g_s$ on $(0,1)$ with $\|g_s\|_2=1$ a.e. and finite integrated kinetic energy $T(g)=\int_0^1b(g_s)\ud s<\infty$. The pairings $(s,t)\mapsto B_\Gamma(g_s^2,g_t^2)$ are measurable, representative independent, and equal to the physical integrals. With
$$J(g)=\int_0^1\int_0^1K_\star(s-t)B_\Gamma(g_s^2,g_t^2)\ud s\ud t,$$
one has
$$0\le J(g)\le R_\star R_{\mathrm{sp}}T(g)^{\alpha/2}<\infty,$$
and the own energy satisfies
$$0<\mathcal E_\star^{\mathcal O}:=\sup_{g\in\mathcal O}(J(g)-T(g)/2)\le R_\star^{2/(2-\alpha)}\mathcal E_{\mathrm{sp}}<\infty.$$

**Derivation.** Continuity of the squared-gradient norm makes $s\mapsto b(g_s)$ measurable, and $\int_0^1\|g_s\|_{H^1}^2=1+T(g)$. A separably valued strong representative (with exceptional null times replaced by a fixed unit compact bump) and simple $H^1$-valued approximation give joint measurable spatial representatives; PROOF135 makes the pairings representative independent. The continuous pairing map on separable $H^1\times H^1$ (PROOF138) makes $(s,t)\mapsto B_\Gamma(g_s^2,g_t^2)$ measurable. With $F(s)=b(g_s)^{\alpha/4}$, PROOF138 gives $B_\Gamma(g_s^2,g_t^2)\le R_{\mathrm{sp}}F(s)F(t)$; concavity ($0<\alpha/2<1$) gives $\int_0^1F^2=\int_0^1b(g_s)^{\alpha/2}\ud s\le T(g)^{\alpha/2}$; with $2F(s)F(t)\le F(s)^2+F(t)^2$ and the exact row bound (and its even column counterpart) this yields the $J$ bound after positive Tonelli. The scalar maximum of $R_\star R_{\mathrm{sp}}T^{\alpha/2}-T/2$ is $R_\star^{2/(2-\alpha)}\mathcal E_{\mathrm{sp}}$, giving the upper bound. Positivity uses a constant-in-time unit compact profile and its dilation: $J=\ell^\alpha J_0A_{\mathrm{sp}}(g)$, $T=\ell^2b(g)$, and for small $\ell$, $\alpha<2$ makes $J-T/2>0$.

**Consumed/unproved conditions.** Full strongly-$H^1$ measurable unit-$L^2$ occupation fields; no time smoothness, common compact support, or optimizer is imposed, and no attaining profile or equality in the bound is asserted.

## PROOF142
**Current statement** (`L:cameron-fractional-products`). For $\alpha/4<s<1/2$, products of real $H^s$ functions define actual elements of $H_{\mathrm{sp}}$, the completion of $C_c^\infty(\mathbb R^d)$ under $B_\Gamma$, with
$$\|fg\|_{H_{\mathrm{sp}}}\le C_s^2\sqrt{R_{\mathrm{sp}}}\|f\|_{H^s}\|g\|_{H^s},$$
and the Hilbert pairings equal the physical integrals; in particular
$$\int|f_1(x)f_2(x)f_3(x-y)f_4(x-y)|\ud x\,\Gamma(\ud y)\le C_s^4R_{\mathrm{sp}}\prod_{j=1}^4\|f_j\|_{H^s},\qquad C_s=\sum_{j\ge0}2^{-j(s-\alpha/4)}.$$

**Derivation.** For real $H^1$ factors, approximate by compact smooth functions; PROOF138 makes their products Cauchy in $H_{\mathrm{sp}}$ with norm at most $\sqrt{R_{\mathrm{sp}}}N(f)N(g)$, and $fg=((f+g)^2-(f-g)^2)/4$ gives PSD for products. Radial dyadic bands $D_0=1_{\{|\xi|<1\}}$, $D_j=1_{\{2^{j-1}\le|\xi|<2^j\}}$ satisfy $N(f_j)\le2^{j\alpha/4}\|f_j\|_2$ on the support and $\sum_jN(f_j)\le C_s\|f\|_{H^s}$, where the first uses the frequency band in the $N$ norm and the second uses $s>\alpha/4$; no $L^p$ multiplier theorem is used. Also $\sum_j\|f_j\|_2<\infty$ since $s>0$, so $\sum_j|f_j|$ converges absolutely a.e. to $f$. Summing the absolute $H^1$ four-linear estimate over band quadruples and using Tonelli plus the null-set transfer at both positions proves the absolute quadruple bound and identifies the physical product series; the double series is absolutely convergent in $H_{\mathrm{sp}}$, and Schwartz density in $H^s$ proves uniqueness of the bilinear extension.

**Consumed/unproved conditions.** No $H^1$ trace or Sobolev algebra is invoked; the frequency bands are an $H^1$ decomposition. The interval $\alpha/4<s<1/2$ is nonempty because $H:homog$ forces $\alpha<2$.

## PROOF143
**Current statement** (`P:cameron-spatial-map`). The smooth-test map $T_{\mathrm{sp}}q=iB_F(m_R(\Gamma*q))$ extends to a compact linear map $T_{\mathrm{sp}}:H_{\mathrm{sp}}\to\mathcal K(F)$ (operator norm), and with $z=(z_1,z_2,c_1,c_2)$, $w=(w_1,w_2,d_1,d_2)$, $w'=\Lambda^{-1}w_2$, $\Lambda=(1-\Delta)^{1/2}$,
$$\langle T_{\mathrm{sp}}qz,w\rangle_F=\langle q,k(z,w)\rangle_{H_{\mathrm{sp}}},\qquad k(z,w)=(\eta_Rz_1+c_1\eta_R)(\eta_Rw').$$
Here $m_R=\eta_R^2$, and the root factor $\eta_R$ factors state tests; it is not a raw noise-space multiplier.

**Derivation.** For smooth compact $q$, $\Gamma*q$ is locally smooth by differentiation under the compactly restricted Radon integral; the velocity pairing in $E$ has weight $\Lambda^{-1}$, so physical Fubini on smooth states plus evenness of $\Gamma$ gives the row identity with the $\eta_R^2$ mask splitting into one $\eta_R$ on each factor. $L^2$ state approximation passes the physical integral, and PROOF142 passes the $H_{\mathrm{sp}}$ pairing. For unit $z,w$, multiplication by $\eta_R$ maps bounded $H^{1/2}$ sets to precompact $H^s$ sets with gain $1/2-s>0$; the $c_1\eta_R$ family is finite-dimensional; closures of both factor families are compact, so their products have compact closure $\mathcal L\subset H_{\mathrm{sp}}$, giving $\|T_{\mathrm{sp}}q\|\le\sup_{k\in\mathcal L}\|k\|\|q\|$ and null-class annihilation. Smooth images lie in $\mathcal K(F)$ by compactness of $mA(H^{1/2}\to H^{-1/2})$; the bounded extension is operator-norm closed. For a complete smooth-test orthonormal basis and projections $Q_n$, the row identity gives $\|T_{\mathrm{sp}}(I-Q_n)\|\le\sup_{k\in\mathcal L}\|(I-Q_n)k\|\to0$ by a finite-net argument and $\|I-Q_n\|\le1$; each $T_{\mathrm{sp}}Q_n$ has finite rank, so the limit is compact. This proves compactness of the map itself, not only compact values.

**Consumed/unproved conditions.** The key factors are the compact cutoff of Proposition `P:cutoff-singular-values` (F005) and PROOF142; all compactness is at fixed $R$.

## PROOF144
**Current statement** (`L:cameron-supported-tensor`). Canonically $H=H_t\otimes H_{\mathrm{sp}}$ as real Hilbert spaces, where $H_t$ is the completion of $C_c^\infty(I)$ under the kernel $|s-t|^{-a}$ and $H_{\mathrm{sp}}$ the completion under $B_\Gamma$. $H$ is separable with a complete orthonormal basis of smooth test representatives supported inside $I\times\mathbb R^d$, and $H$ embeds isometrically as a closed subspace of the given $H_W$. The projection $P_J$ onto the first $J$ basis elements is also an orthogonal projection on $H_W$ by the same finite formula.

**Derivation.** On separated smooth tests, absolute Fubini makes the raw inner product exactly the tensor product after null quotients. Finite sums are dense: a smooth compact spacetime test is approximated uniformly by smooth time partitions times spatial slices on one compact support inside $I\times\mathbb R^d$, with squared raw-norm error at most $\epsilon^2|A|\Gamma(A-A)\int_I\int_I|s-t|^{-a}\ud s\ud t<\infty$; countable smooth-test density on exhausting compact sets follows. Gram–Schmidt skipping zeros preserves smooth compact support. The isometric image is closed by completeness, and its finite orthonormal projection formula remains orthogonal on $H_W$. This projection is not multiplication by a time indicator and gives no independence of disjoint time intervals.

## PROOF145
**Current statement** (`P:cameron-temporal-map`). The operator $K$ on $L^2(I)$ with kernel $|s-t|^{-a}$ is compact, self-adjoint, strictly positive and injective; $\iota:f\mapsto K^{1/2}f$ extends isometrically from $H_t$ onto $L^2(I)$, and $C_t=K^{1/2}\iota:H_t\to L^r(I)$ is bounded and compact for every $2<r<2/a$. The operator $K$ is not trace class, and $C_t:H_t\to L^2(I)$ is not Hilbert–Schmidt.

**Derivation.** Schur bounds give $K$ bounded. The Gamma representation of $|s-t|^{-a}$ and zero extension give strict positivity via the quadratic form
$$\int_{\mathbb R}\frac{2\lambda}{\lambda^2+\xi^2}|\widehat f(\xi)|^2\ud\xi>0\quad(f\ne0),$$
integrated with weight $\lambda^{a-1}/\Gamma_E(a)$, giving injectivity; symmetry gives self-adjointness. $K_\epsilon=K1_{\{|s-t|\ge\epsilon\}}$ is square integrable and hence compact; the Schur norm of $K-K_\epsilon$ is at most $2\epsilon^{1-a}/(1-a)$, giving compactness of $K$ (the truncations are not used as Gaussian covariances). On tests $\|K^{1/2}f\|_2=\|f\|_{H_t}$ and $\ker K=0$ makes the range dense, so the isometry extends onto $L^2(I)$; on tests $C_tf=Kf$. The Young estimate $\|g\|_{H_t}^2\le C_{a,r}^2\|g\|_{r'}^2$, $r'=r/(r-1)$, follows from the triple-Hölder proof of Young with $u=r/2$, giving $\|Kf\|_r\le C_{a,r}\|f\|_{H_t}$; duality is legitimate because $Kf$ is dominated by the integrable-kernel row. Interpolation $\|u\|_r\le\|u\|_2^\tau\|u\|_{r_2}^{1-\tau}$ with $r<r_2<2/a$ upgrades compactness from $L^2$ to $L^r$. Finally the orthonormal cell indicators $N^{1/2}1_{(j/N,(j+1)/N)}$ have quadratic forms summing to $2N^a/((1-a)(2-a))\to\infty$, so $K$ has infinite trace and $K^{1/2}\iota$ is not Hilbert–Schmidt into $L^2$.

**Consumed/unproved conditions.** No instantaneous $L^2$-valued Gaussian is introduced; the non-trace-class conclusion exactly matches the falsifier's requirement.

## PROOF146
**Current statement** (`P:cameron-full-mean`). Fix one $2<r<2/a$. For finite tensors, $\mathcal U(\sum_j f_j\otimes q_j)(s)=\sum_j(Kf_j)(s)q_j$ extends to a bounded map $H\to L^r(I;H_{\mathrm{sp}})$ with dimension-free bound. The map $T\Phi(s)=T_{\mathrm{sp}}(\mathcal U\Phi(s)):H\to L^r(I;\mathcal K(F))$ is compact; for smooth supported $\Phi$ it is the actual multiplier $iB_F(m_Rh_\Phi(s))$ with $h_\Phi=|\cdot|^{-a}*(\Gamma*\Phi)$, and for the supported projections $P_J$,
$$\epsilon_J:=\|T(I-P_J)\|_{H\to L^r(\mathcal K(F))}\longrightarrow0.$$

**Derivation.** For a finite-dimensional spatial field $g$, positivity of the time kernel and scalar Young give
$$\|g\|_{H_t\otimes H_{\mathrm{sp}}}^2\le C_{a,r}^2\|g\|^2_{L^{r'}(H_{\mathrm{sp}})};$$
via Hilbert Cauchy–Schwarz and finite-dimensional duality this gives $\|\mathcal U\Phi\|_{L^r(H_{\mathrm{sp}})}\le C_{a,r}\|\Phi\|_H$ with no dimension factor; tensor density and completeness extend it to a strongly measurable Bochner field. Spatial covariance enters once, through $T_{\mathrm{sp}}$. The physical mean identity on separated tests follows from PROOF143; separated compact-support approximations identify the $L^r$ mean. Let $Q_n$ be the spatial projections of the compact-map proof; $T_n=T_{\mathrm{sp}}Q_n\mathcal U$ lie within $n$ of $T$ by the dimension-free bound and $\|T_{\mathrm{sp}}(I-Q_n)\|\to0$; each coordinate extraction $H\to H_t$ has norm at most one and its image under $C_t$ is precompact in $L^r$, so each $T_n$ is compact and $T$ is compact. Scalar time compactness tensored with an infinite identity would not suffice, because the spatial covariance is applied only through the compact $T_{\mathrm{sp}}$. For the tail, if $\|T(I-P_J)v_J\|$ stayed bounded below for unit $v_J$, then $(I-P_J)v_J\to0$ weakly and compactness would force norm convergence of a subsequence to a weak zero limit, a contradiction; hence $\epsilon_J\to0$.

**Consumed/unproved conditions.** $\epsilon_J\to0$ is at fixed $R$; no uniform-in-$R$ projection-tail assertion is made.

## PROOF147
**Current statement** (`L:cameron-actual-residual`). With $Q_J=I-P_J$ on $H_W$, $Y_{m,J}(f)=W(Q_JT_{\delta,m}f)$, and $g_\delta=\delta^{(1-a)/2}$, Gaussian transfer with mask $m_R$ constructs centered Gaussian paths
$$X_{m,J}(u)=g_\delta A_{m_R}(Y_{m,J})(\min(u,\ell_m)),\qquad 0\le u\le B,$$
whose finite tuple lies in $\mathscr B_0^{N+1}$ (the little-Hölder closure). Every continuous linear statistic $\ell(X)$ of this tuple satisfies $\ell(X)=W(k_\ell)$ for some $k_\ell\in H_I$; an empty last interval gives zero.

**Derivation.** Isometry of the pullback and orthogonality of $Q_J$ give $\mathrm{Var}\,Y_{m,J}(f)\le\|f\|_{H_W}^2$, so `P:source-gaussian-transfer` applies and the true $F$ extension with both constant columns is retained. The parameter choice $\theta<\beta<\beta_2$ below the threshold shows the paths lie in the little $C^\theta$ closure by polygonal approximation; constant stopping preserves compact values and $C^\beta$ bounds. Every observed row's slow pullback belongs to $H_I$: its time support is in $[0,1]$ and indicator approximation inside $I$ converges in raw norm against the integrable time kernel and compact spatial support, including endpoints; both constant columns and Schwartz $E$ states supply the identities, and boundedness extends them to all of $F$. Let $P_H$ project onto closed $H_I\subset H_W$; transfer for the noise $f\mapsto W(P_HQ_JT_{\delta,m}f)$ leaves each observed row unchanged, because the residual slow test lies in $H_I$. This projected-transfer series has coefficient tests in $H_I$, and applying $\ell$ gives an $L^2$ limit in the closed isonormal image $W(H_I)$. Original global-basis tests need not be individually supported.

**Consumed/unproved conditions.** This uses the actual supported slow rows, including both constant columns and endpoint density, not merely Gaussianity or an assumed global-basis support.

## PROOF148
**Current statement** (`P:cameron-actual-embedding`). The actual covariance map
$$(L_{\delta,J}\Phi)_m(u)=\sqrt\delta\int_0^{\min(u,\ell_m)}S_F(-v)T(Q_J\Phi)(s_m+\delta v)S_F(v)\ud v,\qquad\Phi\in H,$$
is a compact-operator Bochner integral. With
$$\|x\|_{\delta,p}=\left(\delta\sum_{m=0}^N\|x_m\|_{C^\theta}^p\right)^{1/p},\qquad G_B=\sup_{|v|\le B}\|S_F(v)\|,\qquad C_B=G_B^2[B^{1-1/r}+B^{1-1/r-\theta}],$$
one has
$$\|L_{\delta,J}\Phi\|_{\delta,p}\ \le\ \sqrt\delta\,C_B(2/B)^{1/p-1/r}\epsilon_J\|\Phi\|_H .$$
The convergence $\epsilon_J\to0$ fixes $R$ and is independent of $\delta$, and the parameter constraints are $\tfrac1{1-\theta}<r<\tfrac2a$ and $\tfrac1\theta\le p<2<r$; the primitive exponent satisfies $1-1/r>\theta$.

**Derivation.** For smooth supported $\Phi$, $Q_J\Phi$ is another such test, and the literal pullback mean gives
$$\mathbb E[Y_{m,J}(f)W(\Phi)]=\delta^{a/2}\int f(v,x)h_{Q_J\Phi}(s_m+\delta v,x)\ud x\ud v,$$
with absolute Fubini for signed compact tests; multiplying by $g_\delta$ gives $\sqrt\delta$, and PROOF143's row identity gives the displayed conjugated form, including both constant columns. Strong continuity of $S_F$ and its adjoint follows from the bounded weighted Fourier matrix; the constant block is finite-dimensional, so conjugation of compact operators is jointly norm-continuous, giving Bochner measurability. With $M=TQ_J\Phi$, Hölder and the primitive increment estimate give
$$\|(L_{\delta,J}\Phi)_m\|_{C^\theta}\le\sqrt\delta\,C_B\,\delta^{-1/r}\|M\|_{L^r(I_m)},$$
and constant stopping does not increase the Hölder norm. Equality on smooth controls extends by density. For the exact norm bound, put $t_m=\|M\|_{L^r(I_m)}\ge0$ and $n=N+1\ge2$; the finite power mean at exponent $r/p>1$ gives
$$\left(\sum_m t_m^p\right)^{1/p}\le n^{1/p-1/r}\left(\sum_m t_m^r\right)^{1/r},$$
and the true partition yields $\sum_mt_m^r=\|M\|_{L^r(I)}^r$ including an empty last interval, with $n\le2/(\delta B)$; substituting gives
$$\|L_{\delta,J}\Phi\|_{\delta,p}\le\sqrt\delta\,C_B(\delta n)^{1/p-1/r}\epsilon_J\|\Phi\|_H\le\sqrt\delta\,C_B(2/B)^{1/p-1/r}\epsilon_J\|\Phi\|_H.$$
If $H_{\mathrm{seen}}$ is the closed span of the $k_\ell$ from PROOF147, then $\ell(L_{\delta,J}\Phi)=\langle k_\ell,\Phi\rangle_H$, so $\ker L_{\delta,J}=H_{\mathrm{seen}}^\perp$; the first-chaos Cameron space is $L_{\delta,J}(H_{\mathrm{seen}})$ with the minimum raw-$H$ preimage norm obtained by orthogonal projection, without any inverse covariance. A raw-$H$ operator bound is therefore the actual embedding bound. The factor $(2/B)^{1/p-1/r}$ remains explicit; no extra $B$, $\delta$, or covariance/mask factor appears.

**Consumed/unproved conditions.** $r>1/(1-\theta)$ makes $1-1/r>\theta$; $r<2/a$ keeps $L^r$ available; $1/\theta\le p<2<r$ maintains the power-mean interpolation and the compact time map. All conclusions fix $R$; no uniform-radius projection tail or concentration estimate is asserted.

## APPLICATION-RAW-LOWER-VARIATIONAL-CAMERON
The single coupled argument, in the exact quantifier order fixed by the focused text, is the following chain.

**(a) Original raw control with half Gaussian cost.** For any fixed nonzero admissible covariance and any positive $\Psi\in C_c^\infty((0,1)\times\mathbb R^d)$, the original raw variable $Z=W(\Psi)$ has variance $v_\Psi=\mathbb E Z^2$ (PROOF120/PROOF121 retains this single covariance; no W-only restriction). Its positive cutoff/mask family uses exactly the given $W$ plus at most one independent auxiliary $J$ (F194 shows positive-cutoff point features are not in the closed $\Phi(H_W)$; this only falsifies the unnecessary W-only strengthening, not the fixed-$W+J$ extension used here). The raw source restart and Gaussian shift produce the exact Cameron identity $\mathbb EU_{\delta,B}^2=\mathbb E[e^{-Z/\sqrt\delta-v/(2\delta)}Y_{\delta,B}^2]$ (PROOF124–PROOF125), from which the linear Gaussian penalty and the quadratic cost $v/2$ emerge.

**(b) One-half action in the lower bound.** The cone event with fixed aperture $B$, index set $s_m$, perturbation tolerance, and the terminal remainder $\tau$ (PROOF122–PROOF123) gives $Y_{\delta,B}$ an amplitude at least $e^{(I_R-o(1))/\delta}$ on a single union-good event of probability $\to1$; the normalized linear penalty is $\delta\,\delta^{-3/4}\to0$, the half-cost is exactly $v_\Psi/2$, and one obtains PROOF126: $\liminf_T T^{-\kappa}\log\mathbb E|u(T,x)|^2\ \ge\ 2I_R-v_\Psi/2$ for each eligible fixed mask $R$.

**(c) Unmasked Rayleigh and control dilation.** The unmasked Rayleigh bottom $\lambda_{\Psi,s}^2=\sup_{\|f\|_2=1,\ f\in H^1(\mathbb R^d;\mathbb R)}(\int h_{\Psi,s}f^2-\|\nabla f\|_2^2)$, strictly negative via the compact-mean trial floor (PROOF129 consuming F010), removes masks by increasing radial masks $\lambda_{R,s}\uparrow\lambda_{\Psi,s}$ uniformly (PROOF130). The full-class control dilation gives $h_{D_r\Psi,s}(x)=r^2h_{\Psi,s}(rx)$, $v_{D_r\Psi}=r^{4-\alpha}v_\Psi$, $I_{D_r\Psi}=rI_\Psi$ (PROOF131). The score set satisfies the exact scaling $cI_{D_{r_c}\Psi}-v_{D_{r_c}\Psi}/2=K_c(I_\Psi-v_\Psi/2)$, and finiteness is funded by the independent $051$ upper-bound theorem for the same canonical solution before taking suprema (PROOF132). This is the required order: $051$ (an interval-field/CP/flexible-order upper bound not consuming PROOF132, the intrinsic 204, nor the actual operator-driver 085/093) supplies finiteness first, then the smooth ratio and full-$H^1$ closure proceed.

**(d) Smooth ratio and full physical $H^1$ closure.** The finite smooth spatial ratio $R_0$ with dilation $A_{\mathrm{sp}}(U_\ell g)=\ell^\alpha A$, $b(U_\ell g)=\ell^2b$, produces the explicit score lower bound with $R(g)\alpha^{\alpha/2}$ (PROOF137), using the already-finite $S_1^{\mathrm{pos}}$. Fatou alone does not give continuity; the absolute four-linear estimate $C_4\le R_0\prod_jN(f_j)$ and telescoped argument differences on $(H^1)^4$ do (PROOF138). This extends $R_{\mathrm{sp}}=R_0$, the square Cauchy–Schwarz, and positivity of $A_{\mathrm{sp}}(f)$ to the full real $H^1$ class, giving the own energy $\mathcal E_{\mathrm{sp}}$ with half kinetic coefficient (PROOF139).

**(e) Fractional products and compact mean maps.** On $H^s$, $\alpha/4<s<1/2$, dyadic-band products give the fractional product bound in $H_{\mathrm{sp}}$ with no Sobolev algebra (PROOF142). The spatial mean $T_{\mathrm{sp}}$ is compact $H_{\mathrm{sp}}\to\mathcal K(F)$ through the root mask factorization and finite-net projection, not merely compact values (PROOF143); the supported tensor $H=H_t\otimes H_{\mathrm{sp}}$ embeds closed in $H_W$ (PROOF144); the temporal map $C_t=K^{1/2}\iota$ is compact into $L^r$, $2<r<2/a$, with $K$ non-trace-class and $C_t$ non-Hilbert–Schmidt into $L^2$ via the cell-trace $N^a$ (PROOF145); the time–space mean $T$ is compact $H\to L^r(\mathcal K(F))$ with tail $\epsilon_J\to0$ at fixed $R$, the compact time map being composed with the compact spatial map rather than tensored with an infinite identity (PROOF146).

**(f) Actual supported residual and minimum raw-$H$ quotient.** The supported residual paths have all linear statistics $W(k_\ell)$ with $k_\ell\in H_I$, using supported slow rows, both constant columns, endpoint density, and the empty last interval (PROOF147). The actual covariance map $L_{\delta,J}$ is the conjugated compact Bochner integral, and the exact averaged bound $\sqrt\delta\,C_B(2/B)^{1/p-1/r}\epsilon_J\|\Phi\|_H$ holds under $r>1/(1-\theta)$, $r<2/a$, $1/\theta\le p<2<r$; the first-chaos Cameron image is $L_{\delta,J}(H_{\mathrm{seen}})$ with minimum raw-$H$ preimage norm obtained by orthogonal projection onto $H_{\mathrm{seen}}$, i.e. $\ker L_{\delta,J}=H_{\mathrm{seen}}^\perp$, with no inverse covariance (PROOF148).

**Consumed parent modules and per-row conditions.** F003 (masked spectral growth, temporal completion, same-noise completion, quotient obstruction), F004 (frequency rows, both wave variance directions, same-noise mean-square columns), F005 (finite Gaussian matrix moments, cutoff factorization, compact envelopes, both variance powers), F006 (actual Gaussian operator driver, variance tails, Holder path), F007 (source cutoffs, retaining isometry, canonical convergence), F008 (masked source moments, canonical point transfer), F009 (constant-phase Young evolution, compact deterministic base), F010 (compact ground family, fractional phase norms, full growing projection, complementary flow, raw profile, oracle lower). Each is retained only through its explicitly consumed clauses; the specific hypotheses are: $\gamma\in(0,\min(1/2,(2-\alpha)/2))$; $\theta<\beta<\min(1-a/2,(3-a-\alpha)/2)$; the spatial-mask convention after convolution (never before); masked spatial AVERAGE not point trace in F008; Green-before-noise in $d=3$; the global given-$W$ plus one $J$ source family.

## GLOBAL-UNPROVED-CONDITIONS
1. **Given-noise retention is only $W+J$.** Every positive-cutoff point source is legal on the fixed extension retaining $W$ and one independent auxiliary $J$; the positive-cutoff point features are NOT in the closed $\Phi(H_W)$ whenever $\Gamma\ne0$ and both cutoffs are positive and finite (F194). Consequently any deduction requiring W-only measurability of positive-width fields or a single $W$-measurable source family fails. The retained structure is exactly the fixed-$W+J$ isonormal extension with $I(\Phi h)=W(h)$; no W-only strengthening may be used by PROOF125–PROOF148.

2. **No finite-dimensional quasi-invariance is claimed.** PROOF121 is a finite-tuple change of law on one norm-Borel Banach space using a (possibly singular) positive square root; it proves no Borell/quasi-invariance statement, no measure transport beyond the single shift $H$, and no infinite-dimensional conversion. The AWS/support/measurability (170) and closed-tube geometry (171) are future and not assigned; they are not to be inferred from the existence of the Banach Gaussian $(X,Z)$ or from PROOF148's covariance embedding.

3. **Finiteness funding order.** The upper bound $051$ (interval-field coefficients, inventory product, fixed-split, Crouzeix–Palencia bounded-operator input) must be consumed before the score finiteness in PROOF132. The focused text does not allow $051$ to depend on PROOF132, the intrinsic theorem 204, or the actual operator driver 085/093. Any reverse dependency is an actual missing deduction.

4. **Mask/cutoff not W-only and physical mask position.** The physical mask $m_R=\eta_R^2$ multiplies the physical source after regularization and after covariance convolution. The root $\eta_R$ factors state tests in PROOF143 but does not define a noise-space multiplier; replacing the post-convolution mask by a pre-convolution mask changes the covariance identity and is not available.

5. **Quantifier order throughout.** Lower bound: fix $\Psi$, mask $R$, control trial, aperture $B$, all budgets, source limits at fixed $\delta,N$; then $\delta\downarrow0$; then rate tolerance $\epsilon_{\mathrm{rate}}\downarrow0$; then (only after the per-$\Psi$ bound) take the full-class numerical supremum. No $B(\delta)$ and no $R(T)$. Upper-side finiteness: fix covariance; obtain $051$ at each fixed $T$; take the suprema in PROOF132 only after finiteness. PROOF148: fixed $R$; $\epsilon_J\to0$ independent of $\delta$; no uniform-in-$R$ tail.

6. **Endpoint claims explicitly withheld.** PROOF129 does not assert an unmasked ground eigenstate; PROOF130 does not construct a mask-free noisy wave or an $R(t)$; PROOF134 keeps the exact unnormalized mass $M_a$ with $0<a<1$ and does not renormalize; PROOF141 asserts a positive finite supremum but not attainment or equality; PROOF140 defines $K_\star(0)=0$ for time integration only and produces the exact midpoint row maximum; PROOF145 states non-trace-class/non-Hilbert–Schmidt exactly as the falsifier demands; PROOF129/PROOF132/PROOF139 never identify the auxiliary label-one score with an actual first-moment or source constant.

7. **Compactness is never "value compactness."** PROOF143 and PROOF146 prove compactness of the mapping itself: the compact spatial mean is composed with the compact time map; a compact time map tensored with an infinite identity is not compact and is not asserted. PROOF144 is a closed isometric tensor embedding and an orthogonal projection, not time-indicator multiplication, and it asserts no independence of disjoint time intervals.

8. **Physical vs. Lebesgue factors.** The Radon pushforward factors ($r^{\alpha-d}$ for covariance, $r^2$ for the mean, $r^{4-\alpha}$ for variance, $r^{-d}$ from Lebesgue substitution) must remain separate; all appear in PROOF131 and PROOF137–139. The spatial dimensions, white endpoint $d=\alpha=1$, and singular Radon covariances are unchanged.

9. **Full-class vs. subset.** Smooth compact controls in PROOF136–137 are a subset; they lower-bound $S_1^{\mathrm{pos}}$ and $R_0$ without restricting the full class. Full-$H^1$ closure is exactly PROOF138 (Fatou plus four-linear continuity), and the full occupation class in PROOF141 is strongly $H^1$-measurable unit-$L^2$ fields with finite integrated kinetic energy.

10. **No point traces and no spectral-inverse shortcuts.** Masks are averaged spatial tests (F008), not point traces; PROOF143 and PROOF148 compute minimum raw-$H$ preimage norms by orthogonal projection onto $H_{\mathrm{seen}}$, never by inverting a covariance. The covariance amplitude, zero-cost Gaussian action, dimensions, and constants of the original model remain unchanged outside this focused work.