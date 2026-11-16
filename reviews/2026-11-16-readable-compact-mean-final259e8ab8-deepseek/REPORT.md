# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

Verdict is unforced. All seven assigned proofs were read in full in both revisions, including unchanged statement blocks. The new revision is a faithful reorganization of the same deductions into labeled Steps, with interleaved explanatory sentences. No logical step is deleted, no hypothesis or qualifier is dropped, and every newly inserted mathematical claim is verifiably correct under the same hypotheses (checked below with public working). The statements and definitions of all seven items are byte-identical in mathematical content between revisions; only local line offsets differ.

---

## P:compact-ground-family

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** (OLD 56–112; NEW 56–135)
1. Form-domain identification: $A_\sigma=H_\sigma+c$, $c=1+M\ge1$, and the form identity $\|A_\sigma^{1/2}u\|_2^2=q_\sigma(u)+c\|u\|_2^2$; equivalence to the $H^1$ norm; identification of completions $D(A_\sigma^{1/2})=H^1$.
2. Application of imported Theorem 10.2 to $-V_\sigma$ (self-adjoint $H^2$ operator, essential threshold $0$); max–min gives $-M\le E_1\le-\varepsilon$; bottom below threshold ⇒ isolated finite-multiplicity eigenvalue; then Theorem 10.13 (simple positive ground state); real representative via conjugation.
3. $E_1<E_2\le0$; level continuity from $|q_\sigma-q_\tau|\le\|V_\sigma-V_\tau\|_\infty$; compactness of $I$ gives $\Delta_*=\min_I(E_2-E_1)>0$; rate gap via $\lambda_\sigma-\mu_\sigma=(E_2-E_1)/(\lambda_\sigma+\mu_\sigma)\ge\Delta_*/(2\sqrt M)$.
4. $L^2$ continuity of $p_\sigma$ by two-sided variational bound; bootstrap to $H^2$ via $(1-\Delta)p_\sigma=(1-\lambda_\sigma^2+V_\sigma)p_\sigma$.

**Working.**
- Form identity: $\|A^{1/2}u\|^2=\|\nabla u\|^2-\int V|u|^2+c\|u\|^2=\|\nabla u\|^2+\int(c-V)|u|^2$. Since $0\le V\le M$, $1\le c-V\le c$, hence $\|u\|_{H^1}^2\le\|A^{1/2}u\|^2\le c\|u\|_{H^1}^2$ on $H^2$. The NEW added sentence (“the shifted potential term $c-V_\sigma$ lies between one and $c$”) is exactly this computation and is correct.
- Trial gives $q(w)\le-\varepsilon$ with $\|w\|_2=1$; form lower bound $q(u)\ge-\int V|u|^2\ge-M$ gives $-M\le E_1\le-\varepsilon$, so $M\ge\varepsilon>0$.
- Ground-state distance: with $p_\tau=ap_\sigma+r$, $r\perp p_\sigma$, $a=\langle p_\tau,p_\sigma\rangle>0$ (NEW clarifies positivity from two positive-a.e. states; OLD asserted $0<a\le1$). Orthogonality gives $a^2+\|r\|^2=1$. Upper bound: $q_\sigma(p_\tau)\le q_\tau(p_\tau)+d_V\le E_1(\tau)+d_V\le E_1(\sigma)+2d_V$. Lower bound uses $q_\sigma(p_\tau)=a^2E_1(\sigma)+q_\sigma(r)$ (cross term vanishes since $r\perp$ eigenvector) and $q_\sigma(r)\ge E_2(\sigma)\|r\|^2$, so $q_\sigma(p_\tau)\ge E_1(\sigma)+\Delta_*\|r\|^2$. Hence $\|r\|^2\le2d_V/\Delta_*$; $\|p_\tau-p_\sigma\|^2=2(1-a)\le2(1-a^2)=2\|r\|^2\le4d_V/\Delta_*$ — equation \eqref{E:compact-ground-continuity}.
- $H^2$ bootstrap: RHS norm $\le (1+M+M)\cdot1=1+2M$; $(1-\Delta)^{-1}$ is the Bessel isometry $L^2\to H^2$.

**Lost steps/qualifiers / pre-existing concerns.** None introduced. A pre-existing terseness (identical in both): continuity of the second level $E_2$ “including passage of $E_2$ to the threshold” is asserted from the max–min infimum/supremum manipulation rather than expanded; this is standard and is not a rewrite change.

---

## L:compact-fractional-phase

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** (OLD 135–164; NEW 158–205)
1. Resolvent order $(T+t)^{-1}\ge(S+t)^{-1}$ for positive self-adjoint $T\le S$ with common form domain, via the variational supremum identity.
2. Consequent $I-t(T+t)^{-1}=T(T+t)^{-1}\le S(S+t)^{-1}$; scalar square-root integral; spectral integration gives $T^{1/2}\le S^{1/2}$ including domain inclusions.
3. Application to $B\le A_\sigma\le cB$ (form order on $H^1$) giving \eqref{E:compact-quarter-power} and domain equality with $H^{1/2}$.
4. Duality for the negative entry and completion to $H^{-1/2}$.

**Working.**
- Variational identity: the maximizer of $2\operatorname{Re}\langle f,u\rangle-q_T(u)-t\|u\|_2^2$ is $u=(T+t)^{-1}f$, value $\langle f,(T+t)^{-1}f\rangle$. Increasing the form decreases each term in the supremum (NEW’s opening sentence), so $T\le S$ forces $\langle f,(T+t)^{-1}f\rangle\ge\langle f,(S+t)^{-1}f\rangle$: resolvent order reverses. This holds for arbitrary noncommuting $T,S$ because only the scalar variational identity is compared — no operator-power rule for noncommuting operators is invoked, satisfying the required check.
- Scalar identity: $\int_0^\infty t^{-1/2}\frac{x}{x+t}dt=\pi\sqrt x$ by $t=xr^2$, $\int_0^\infty(1+r^2)^{-1}dr=\pi/2$. So $T^{1/2}=\pi^{-1}\int t^{-1/2}T(T+t)^{-1}dt$; the scalar order $T(T+t)^{-1}\le S(S+t)^{-1}$ plus positive weight and Tonelli(monotone) yields the half-power form inequality.
- Since $(cB)^{1/2}=c^{1/2}B^{1/2}$, one application gives $\|B^{1/4}u\|\le\|A_\sigma^{1/4}u\|\le c^{1/4}\|B^{1/4}u\|$ (the half-power comparison with the pair $(A_\sigma,cB)$), i.e. \eqref{E:compact-quarter-power}; equivalence of norms gives $D(A_\sigma^{1/4})=D(B^{1/4})=H^{1/2}$, matching NEW’s closing remark in Step 1.
- Duality: $\sup_{\|A^{1/4}u\|\le1}|\langle u,z\rangle|=\|A^{-1/4}z\|$; attained at $u=A^{-1/2}z/\|A^{-1/4}z\|$ (NEW retains). Reversal under duality and $c$-dependence of the constants (NEW Step 2) are correct; completion identifies the negative space with $H^{-1/2}$ uniformly.

**Lost steps/qualifiers / pre-existing concerns.** None. The “common form domain” assumption is satisfied since $D(A_\sigma^{1/2})=H^1=D(B^{1/2})$ was established in P:compact-ground-family.

---

## P:compact-E-wave

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** (OLD 189–252; NEW 230–318)
1. Definition of spectral functions $C_t,S_t$ for $h>0$, $h=0$, $h<0$; spectral wave matrix \eqref{E:compact-spectral-wave}; reality preservation.
2. Complementary spatial projection $Q_\sigma^{\mathrm{sp}}$; phase-isometry scalar entries; scalar bounds on $h\ge0$ and on $-\mu_\sigma^2\le h<0$; operator bound $C(1+t)e^{\mu_\sigma t}$ including $\mu_\sigma=0$.
3. Both ground branches $(p_\sigma,\pm\lambda_\sigma p_\sigma)$; decaying branch retained in $I-\Pi_\sigma^E$; uniform projection bounds.
4. Identification with the physical flow via graph levels, spectral cutoffs, free Fourier group, Duhamel/Picard, density within $E$.

**Working.**
- Let $U=A^{1/4}u$, $Z=A^{-1/4}z$ (the spectral phase norm is $\|(U,Z)\|_{L^2}^2$). Then the displacement entry is $A^{1/4}(C_t u+S_t z)=C_t(h)U+S_t(h)(h+c)^{1/2}Z=C_tU+\sqrt{h+c}\,S_t Z$, and the velocity entry is $A^{-1/4}(-HS_t u+C_tz)=-hS_t(h)(h+c)^{-1/2}U+C_tZ=-hS_t/\sqrt{h+c}\,U+C_tZ$. This verifies NEW Step 1 (“multiplies the displacement by $(h+c)^{1/4}$, velocity by $(h+c)^{-1/4}$”, giving $\sqrt{h+c}$ and its reciprocal on the off-diagonals).
- $h\ge0$: $|S_t|\le\min(t,h^{-1/2})$; $\sqrt{h+c}\,|S_t|\le\sqrt{1+c}(1+t)$ for $h\le1$ and $\le\sqrt{1+c/h}\le\sqrt{1+c}$ for $h\ge1$; $|hS_t|/\sqrt{h+c}\le\sqrt h/\sqrt{h+c}\le1$; $|C_t|\le1$. So $C(1+t)$.
- $-\mu^2\le h<0$: $|C_t|=\cosh(t\sqrt{|h|})\le e^{\mu t}$; $|S_t|\le t e^{\mu t}$ (as $\sinh x/x\le e^x$); $|h|\le M$, $1\le h+c\le c$; hence $C(1+t)e^{\mu t}$; $\mu_\sigma=0$ is covered by the bound on $h\ge0$.
- Ground branches: $\|e_\sigma^E\|_{E_\sigma}^2=(c-\lambda^2)^{1/2}+\lambda^2(c-\lambda^2)^{-1/2}=c/\sqrt{c-\lambda^2}$, uniformly bounded because $1\le c-\lambda^2\le c$ and $\sqrt\varepsilon\le\lambda\le\sqrt M$; the dual norm is bounded likewise. The decaying branch $(p_\sigma,-\lambda_\sigma p_\sigma)$ carries $e^{-\lambda t}$ and lies in $I-\Pi_\sigma^E$.
- Identification: graph norm $(A_\sigma u,A_\sigma^{1/2}z)$ is equivalent to $H^2\times H^1$ since $A_\sigma-B=M-V_\sigma$ is bounded by $M$ while $A_\sigma,B\ge1$; the free Fourier group on $H^1\times L^2$ is strongly continuous (dominated Fourier convergence), generator $(z,\Delta u)$; the interaction-picture derivative is justified at graph levels on smooth data — NEW correctly notes this is not an operator-norm derivative on the whole phase. $V_\sigma:H^{1/2}\to L^2\to H^{-1/2}$ with $\|V_\sigma u\|_{H^{-1/2}}\le\|V_\sigma u\|_2\le M\|u\|_2\le M\|u\|_{H^{1/2}}$; Picard uniqueness and density within $E$ (not density of $E$ in $F$) complete the identification.

**Lost steps/qualifiers / pre-existing concerns.** None. Both ground copies, the $\mu=0$ case, and the strong-vs-operator-norm distinction are preserved.

---

## P:compact-F-projection

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** (OLD 296–342; NEW 362–429)
1. Block formula \eqref{E:compact-F-block} by variation of constants with an $E$-valued Fubini exchange.
2. Positivity and continuity of $f_\sigma$; constant-coordinate dual via two exponential integrals and the shifted tail; dual eigenproperty $\ell_\sigma P_\sigma(t)=e^{\lambda t}\ell_\sigma$; projection properties \eqref{E:compact-F-eigen}.
3. Positive margins \eqref{E:compact-positive-margins} by compactness, without $L^1$ ground states or point traces.

**Working.**
- Coupling: $C(t)(c_1,c_2)=(c_1+tc_2,c_2)$; $D_\sigma(c_1,c_2)=(0,V_\sigma c_1)\in E$; force range in $iE$ gives the constant block. For a continuous $E$ force $g$, $Y(t)=P^E(t)e+\int_0^t P^E(t-r)g(r)dr$, substituting $P^E(t-r)=S(t-r)+\int_0^{t-r}S(t-r-s)B^EP^E(s)ds$ and exchanging the triangle $0\le r\le s\le t$ (verbatim the displayed NEW/OLD exchange) gives $Y(t)=S(t)e+\int_0^t S(t-s)[B^EY(s)+g(s)]ds$; uniqueness identifies \eqref{E:compact-F-block}. NEW’s triangle/region explanation matches the exchange exactly.
- $f_\sigma=\frac{\int V_\sigma p_\sigma}{2\lambda_\sigma}>0$: finite by $L^2$ Cauchy–Schwarz; positivity since $V_\sigma\not\equiv0$ (else the common trial would force $\|\nabla w\|^2\le-\varepsilon$) and $p_\sigma>0$ a.e.
- $\ell_\sigma^ED_\sigma C(r)c=\frac{\langle p_\sigma,V_\sigma(c_1+rc_2)\rangle}{2\lambda_\sigma}=f_\sigma(c_1+rc_2)$. Then $\ell_\sigma^C(c)=\int_0^\infty e^{-\lambda r}f(c_1+rc_2)dr=f(c_1/\lambda+c_2/\lambda^2)$ using $\int e^{-\lambda r}=1/\lambda$, $\int re^{-\lambda r}=1/\lambda^2$ (NEW spells these out); the tail $\ell_\sigma^C(C(t)c)=\int_t^\infty e^{\lambda(t-r)}f(c_1+rc_2)dr$ follows by $s=r-t$. Applying $\ell_\sigma$ to \eqref{E:compact-F-block}: $e^{\lambda t}\ell^E(e)+\int_0^t e^{\lambda(t-r)}f(c_1+rc_2)dr+\int_t^\infty e^{\lambda(t-r)}f(c_1+rc_2)dr=e^{\lambda t}\ell(e,c)$. With $P(t)e_\sigma=e^{\lambda t}e_\sigma$ and $\ell_\sigma(e_\sigma)=\ell^E(e^E)+0=1$, both $P\Pi=e^{\lambda t}\Pi$ and $\Pi P=e^{\lambda t}\Pi$ follow.
- Margins: $\ell_\sigma(e_0)=f_\sigma/\lambda_\sigma>0$; $O_\phi(e_\sigma)=\int\phi p_\sigma>0$ because $\phi\ge0$, $\int\phi=1$ so $\phi>0$ on a positive-measure set, and $p_\sigma>0$ a.e. (NEW states this); continuity on compact $I$ gives $\inf_I>0$. Everything is integrals; no point trace, no $p_\sigma\in L^1$.

**Lost steps/qualifiers / pre-existing concerns.** None. Both constant-data columns and their coupling into $E$ are handled.

---

## P:compact-F-complement

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** (OLD 369–406; NEW 456–521)
1. Exact complement decomposition, including the growing-forcing cancellation and the tail subtraction term \eqref{E:compact-complement-forcing}; cubic polynomial bound \eqref{E:compact-F-complement}.
2. Normalized decay \eqref{E:compact-normalized-complement} for $\eta<d_0$.
3. Finite-horizon parameter dependence \eqref{E:compact-parameter-flow} by statewise Duhamel subtraction and scalar Gronwall; measurability of the operator norm.

**Working.**
- $P(t)\Pi=e^{\lambda t}\Pi$ has constant part $(0,0)$. Decomposing $e=Q^Ee+\Pi^Ee$ gives $P^E(t)e=P^E(t)Q^Ee+e^{\lambda t}e^E\ell^E(e)$. The forcing integral splits as $e^E\int_0^t e^{\lambda(t-r)}f(c_1+rc_2)dr+\int_0^t P^E(t-r)Q^EDC(r)c\,dr$. The growing part satisfies $e^E\int_0^t e^{\lambda(t-r)}f(c_1+rc_2)dr=e^E(e^{\lambda t}\ell^C(c)-\ell^C(C(t)c))$; subtracting $e^{\lambda t}e^E\ell^C(c)$ leaves $-e^E\ell^C(C(t)c)$, yielding \eqref{E:compact-complement-forcing}. NEW Step 1 reproduces this identity correctly.
- $\|Q^EDC(r)\|\le C(1+r)$: $\|(0,V(c_1+rc_2))\|_E=\|V(c_1+rc_2)\|_{H^{-1/2}}\le M|c_1+rc_2|\|1_K\|_2\le C(1+r)|c|$, with $\|Q^E\|$ uniform. $\|P^E(t-r)Q^E\|\le C(1+t-r)e^{\mu(t-r)}\le C(1+t-r)e^{\mu t}$ since $\mu\ge0$. Integral $\le Ce^{\mu t}|c|\int_0^t(1+t-r)(1+r)dr$, and $\int_0^t(1+t-r)(1+r)dr=(1+t)t+t\cdot t^2/2-t^3/3=t+t^2+t^3/6$ (NEW’s factorization and cubic polynomial are correct). First term $C(1+t)e^{\mu t}\|e\|_E$; final and constant terms $C(1+t)|c|$; $\mu\ge0$ gives \eqref{E:compact-F-complement}.
- Normalized: $\lambda-\mu\ge d_0$ gives $e^{-\lambda t}P(t)Q\le C(1+t)^3e^{-d_0 t}$; for $\eta<d_0$, $(1+t)^3e^{-(d_0-\eta)t}$ is bounded, giving \eqref{E:compact-normalized-complement}.
- Dependence: subtracting the two free-Duhamel equations, $P_\sigma-P_\tau=\int S_F(t-r)B_\sigma(P_\sigma(r)-P_\tau(r))dr+\int S_F(t-r)(B_\sigma-B_\tau)P_\tau(r)dr$; $\|B_\sigma-B_\tau\|\le d_{\sigma,\tau}$; bounded free-group and uniform finite-horizon flow bounds reduce to scalar Gronwall (NEW Step 2 correct). Measurability via separability/countable dense set; no operator-norm derivative of the free group is used.

**Lost steps/qualifiers / pre-existing concerns.** None. The “constant-velocity polynomial is included” qualifier is retained; the subtracted/tail term is present.

---

## L:compact-raw-profile

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** (OLD 442–474; NEW 557–604)
1. Identification of the covariance mean and \eqref{E:compact-raw-cost}; finiteness.
2. Strict positivity of $Q(\overline q)$ via Radon pairings and homogeneity; the time-uniform mean floor \eqref{E:compact-positive-mean-floor}.
3. Smoothness of $h$ by differentiating the compact test; fixed-mask Lipschitz bounds.

**Working.**
- Mean: $\mathbb E[W(\Psi)W(F_0)]=\iint\Psi(u,y)F_0(s,x)|s-u|^{-a}\Gamma(d(x-y))\,du\,dy\,ds\,dx=\int F_0(s,x)h_s(x)dx\,ds$ with $h_s(x)=\int_0^1|s-u|^{-a}(\Gamma*\Psi(u,\cdot))(x)du$. Setting $F_0=\Psi$ gives \eqref{E:compact-raw-cost}.
- Finiteness: $|(\Gamma*\Psi(u,\cdot))(x)|\le\|\Psi\|_\infty\Gamma(\overline B_{2A})$ for $x\in B_A$; $\int_0^1\int_0^1|\sigma-u|^{-a}dud\sigma=2/((1-a)(2-a))$ ($a<1$); so $v_\Psi\le\|\Psi\|_\infty^2\Gamma(\overline B_{2A})|B_A|\cdot 2/((1-a)(2-a))<\infty$.
- Positivity: $\overline q\in C_c^\infty$ nonnegative nonzero; $r(z)=\int\overline q(x)\overline q(x-z)dx$ is continuous with $r(0)=\|\overline q\|_2^2>0$, so $r\ge\|\overline q\|_2^2/2>0$ on a ball $B_\delta$; homogeneity gives $\Gamma(B_r)=r^{\alpha-d}\Gamma(B_1)>0$ for all $r>0$; hence $0<Q(\overline q)=\int r\,d\Gamma<\infty$. The floor: since $|\sigma-u|\le1$ and $a>0$, $|\sigma-u|^{-a}\ge1$, so positive Tonelli gives $h_\sigma\ge\Gamma*\overline q$, and $v_\Psi\ge\int(\Gamma*\overline q)\overline q=Q(\overline q)>0$.
- Correctly, the lower profile $\Gamma*\overline q$ is only asserted nonnegative/nonzero ($\overline q\ne0$); the strict positivity claim is about the integral cost $Q(\overline q)$, not pointwise profile positivity. Both revisions match this distinction.
- Smoothness: with $\Psi$ zero-extended in time, $h_s(x)=\int_\mathbb R|r|^{-a}\int\Gamma(dz)\Psi(s-r,x-z)dr$; on compact $(s,x)$ sets, $r\in(s-1,s)$ and $z\in x-\operatorname{supp}\Psi$ range over compact sets, and $|r|^{-a}\in L^1_{\mathrm{loc}}$ since $a<1$; all derivatives land on the smooth test $\Psi$, and dominated convergence gives $C^\infty$ in both variables. Hence $V_\sigma=m_Rh_\sigma$ is smooth compact and Lipschitz in $\sigma$.

**Lost steps/qualifiers / pre-existing concerns.** None. No separability assumption on $\Psi$ is made; no singular-kernel differentiation.

---

## P:compact-original-common-trial

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** (OLD 491–532; NEW 621–682)
1. Dilated unit trial $\psi_L=L^{-d/2}\psi(x/L)$; mask plateau $R\ge2L$; potential lower bound $C_\Gamma L^{-\alpha}$ (\eqref{E:compact-trial-potential}).
2. Kinetic energy $D_\psi L^{-2}$; $\alpha<2$ gives $\varepsilon_R=C_\Gamma L^{-\alpha}-D_\psi L^{-2}>0$; common negative trial uniform in $\sigma$.
3. Fixed radius before invoking P:compact-ground-family; rate Lipschitz via $\sqrt{\varepsilon_R}$ denominator; positivity at $\sigma=0$; original $\Psi,Z,v_\Psi$ unchanged.

**Working.**
- On $B_L$, $x/L\in B_1$, so $\psi_L(x)^2\ge c_0^2L^{-d}$ (NEW states this); $\operatorname{supp}\psi_L\subset B_{2L}\subset B_R$, so $V_\sigma=h_\sigma$ there.
- $\int V_\sigma\psi_L^2\ge c_0^2L^{-d}\int_{B_L}h_\sigma\ge c_0^2L^{-d}\int_{B_L}(\Gamma*\overline q)=c_0^2L^{-d}\int\overline q(y)\Gamma(B_L-y)dy$. For $|y|\le A$, $L\ge2A$ gives $B_{L/2}\subset B_L-y$, so this $\ge c_0^2L^{-d}\Gamma(B_{L/2})\int\overline q$. Homogeneity: $\Gamma(B_{L/2})=(L/2)^{d-\alpha}\Gamma(B_1)$ (NEW states), giving $c_0^22^{\alpha-d}\Gamma(B_1)\int\overline q\,L^{-\alpha}=C_\Gamma L^{-\alpha}$. This is the exact Radon scaling vs the Lebesgue scaling $L^{-d/2}$, $L^d$ integration.
- Kinetic: $\|\nabla\psi_L\|^2=L^{-2}\int|\nabla\psi(y)|^2dy=D_\psi L^{-2}$. From $\alpha_0+\alpha<2$, $\alpha<2$, so $L^{-\alpha}\gg L^{-2}$ and large $L$ gives $\varepsilon_R>0$; then $\|\nabla\psi_L\|^2-\int V_\sigma\psi_L^2\le-\varepsilon_R$ for every $\sigma$ (uniform since $C_\Gamma$ is $\sigma$-independent).
- Rate Lipschitz: $E_1(\sigma)\le-\varepsilon_R$ for all $\sigma$ gives $\lambda_\sigma=\sqrt{-E_1}\ge\sqrt{\varepsilon_R}$; $|\lambda_\sigma-\lambda_\tau|=|E_1(\tau)-E_1(\sigma)|/(\lambda_\sigma+\lambda_\tau)\le\|V_\sigma-V_\tau\|_\infty/(2\sqrt{\varepsilon_R})\le C_R|\sigma-\tau|$ (NEW states the denominator fact). $\lambda_0>0$ holds because the common trial includes $\sigma=0$; the mean $h_0=\int|u|^{-a}(\Gamma*\Psi(u,\cdot))du$ is nonzero even though $\Psi(0,\cdot)=0$.
- $\Psi$, $Z=W(\Psi)$, $v_\Psi$ are defined on the original noise and are untouched by the deterministic mask $m_R$; enlarging $R$ keeps the trial and makes masked/unmasked potential energies agree on arbitrary fixed compact supports. The “not all-strength binding”/“masks fixed before asymptotics” scope remarks are retained.

**Lost steps/qualifiers / pre-existing concerns.** None.

---

## AUDIT dispositions

No AUDIT-worthy issues found. No rewrite-introduced defect was identified in any of the seven proof pairs. All new explanatory assertions were checked against the old argument and the supplied hypotheses and were found correct; no step or qualifier was lost. Pre-existing (not rewrite-attributable) terseness is limited to:

1. P:compact-ground-family, Step 3: continuity of the second max–min level $E_2$ across the essential threshold is compressed to “including passage of $E_2$ to the threshold” in both revisions.
2. L:compact-fractional-phase: the Loewner machinery (variational resolvent identity → half-power comparison) is stated concisely but correctly; it does not use an unsupported noncommuting-power rule.

Neither constitutes a defect introduced by the rewrite, and neither affects equivalence of the two revisions.

---

## Findings and limits

- All seven assigned proofs were read COMPLETE in both revisions, including all unchanged portions and unchanged statements/definitions; the seven statements are mathematically identical between revisions (line offsets differ because of inserted Step text).
- Public reconstruction is COMPLETE for all seven; the key public equations/estimates were re-derived above (form identity and $\Delta_*$ for the ground family; variational resolvent and square-root integral for fractional norms; phase-isometry conjugation $\sqrt{h+c}$, $h/\sqrt{h+c}$ for the wave matrix; exponential tail/dual computations for the projection; the cubic polynomial $t+t^2+t^3/6$ and Gronwall step for the complement; Radon/homogeneity scaling $C_\Gamma L^{-\alpha}$ vs $D_\psi L^{-2}$ for the trial).
- This review certifies only rewrite preservation for the seven assigned target proofs. It does not re-verify the imported primary sources (Teschl Theorems 10.2, 10.13, 4.12/4.13), the Young-source PDFs, the unassigned baseline modules (model assumptions, constant-young, covariance foundation, compact Gaussian), Lean correspondence, or rendered pages; those were used only as stated inputs under checked application hypotheses.
- No tools, shell, network, delegation, editing, or messaging were used; the analysis is entirely from the embedded text.
