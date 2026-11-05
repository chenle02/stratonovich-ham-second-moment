# Current Unit A — Scientific Review: 24 OWN proofs (001–023, 214) and 38 declared roles

I assess only the assigned A deductions at their stated scope. All formulas below are reconstructed from the supplied current source; prior dossiers/annotations are treated as evidence to challenge, not as acceptance. No tools were used.

---

## 1. Compact coverage index (24 proofs / 38 roles / constructor)

| PROOF | Decl | Claim (scope) | Assessment |
|---|---|---|---|
| 001 | S037 | Jensen: $\mathbb E u\ge1$, $\mathbb Eu^2\ge(\mathbb Eu)^2$, liminf transfer $2\ell$ | **Reconstructed** (cond. on 008) |
| 002 | S038 | Mixed terms: $\mathbb E[X_mX_n]=\sum_{D\in\Pi_k}J_{m,n,D}$ (even), $0$ (odd); full second series | **Reconstructed** (cond. on 005/006/007/008/009) |
| 003 | S004 | White/$\delta_0$ order-two $=2c_0t^{3-\alpha_0}$, $c_0=[(1-\alpha_0)(2-\alpha_0)(3-\alpha_0)]^{-1}$ | **Exact** |
| 004 | S005 | Damped norms $N_0=\theta^{-2}$, $N_1=\theta^{\alpha+\alpha_0-2}N_1(1)$, $N_2^2=\theta^{-\beta}N_2(1)^2$; tails $\to0$ | **Exact** |
| 214 | S006 | Translated-covariance CS, coefficient $1$, independent origins | **Exact** |
| 005 | S007 | Spatial Wick measures: weak limit $\nu_D$, homogeneity $\rho_D(cA)=c^{(4-\alpha)k}\rho_D(A)$, face masses $0$ | **Reconstructed** |
| 006 | S008 | Joint fixed-order diagram/term limits, arbitrary relative rates, Green-first | **Reconstructed** (named Thm 3.1 import) |
| 007 | S009 | Crude: $\mathbb EX_n^2\le e^{2\theta_0t}\frac{C^nt^{2n}}{n!}$; $\mathbb Eu^2\le 2e^{2\theta_0t+2Ct^2}$ | **Exact** |
| 008 | S010 | Vertexwise $q_n=e^{\theta_0t}\frac{C^{n/2}t^n}{\sqrt{n!}}$; $\sum\sqrt{n+1}\,q_n(T)<\infty$ | **Exact** |
| 009 | S039 | Mild equation, occupied multiplication $2\sqrt{n+1}$, fixed-factor Green limit | **Reconstructed** |
| 010 | S040 | Homogeneous envelope $\rho=\beta/(\beta-1)>\kappa$; majorant two-sided growth | **Exact** (numerical majorant; $\mathbb Eu^2\le B_K$ cond. on 002) |
| 011 | S041 | White order-four: 9 base rows, $t^{6-2\alpha_0}$ scaling | **Exact** |
| 012 | S011 | Static order-four: $11t^6/540$, order-two $t^3/3$, 27/45 sectors | **Exact** |
| 013 | S042 | Riesz order-two closed forms; order-four explicit integral $t^{2\beta}$ | **Exact** |
| 014 | S012 | d1 spatial bound $K_{\rm sp}^kt^{bk}/k^{bk}$ | **Exact** |
| 015 | S043 | d1 upper $C_2=q(2ZK_{\rm sp})^{1/q}$ | **Exact** |
| 016 | S013 | Low-$\alpha$ convolution $V h^{1-\alpha}/(1-\alpha)$ | **Exact** |
| 017 | S014 | $\alpha=1$ oscillatory/Abel bound $\pi V/2$ | **Exact** |
| 018 | S044 | $0<\alpha\le1$ all $d$, $K_{\rm sp}^{\rm gen}$, $C_2^{\rm gen}$ | **Exact** (spatial subclause) |
| 019 | S057 | $C_{1,\*}=C_{2,\*}/2^{(4-\alpha)/(3-\alpha)}$ | **Exact** |
| 020 | S045 | Conditional transfer under $H$:spatial-maximum | **Conditional** |
| 021 | S015 | Riesz maxima $M_3=c2^{1-\alpha}/(2-\alpha)$, $M_2$ (d2, $\alpha<3/2$) | **Reconstructed** |
| 022 | S058 | Riesz application, stated ranges | **Conditional application** |
| 023 | S046 | Obstructions to spatial-maximum | **Reconstructed** |

**38 roles.** OWN (24): S004–S015, S037–S046, S057, S058 — all attached to their proofs above. EXTERNAL (2): S001, S002 — quoted/restated sources (checks §6). CONTEXT (12): S064, S065, S067, S070–S078 — role checks §6. No CONTEXT statement receives an invented proof; S064 is the active global given, S065 the additional conditional premise, S067 a never-forced source conjecture.

---

## 2. Constructor core

### WORK A — Homogeneous damped norms (004) and independent-origin CS (214)

**Hypotheses.** $0<\alpha_0<1$, $0<\alpha<d$ or $\alpha=d=1$, $\alpha+\alpha_0<2$; $\Gamma$ nonnegative even PD homogeneous tempered Radon measure, $\Gamma(cA)=c^{d-\alpha}\Gamma(A)$, spectral convention $\Gamma=\int e^{i\xi\cdot x}\mu(d\xi)$ with $\mu(cA)=c^\alpha\mu(A)$. $\beta=4-\alpha-\alpha_0$.

**PROOF004 (damped norms).** Definitions (E:damped-norm-definitions):
$$N_0(\theta)=\int_0^\infty e^{-\theta s}G_s(\mathbb R^d)ds,\quad N_1(\theta)=\tfrac1{\Gamma_E(\alpha_0)}\int_0^\infty\lambda^{\alpha_0-1}d\lambda\int\tfrac{\mu(d\xi)}{(\theta+\lambda)^2+|\xi|^2},$$
$$N_2(\theta)^2=\int_0^\infty\!\!\int_0^\infty e^{-\theta(s+t)}|s-t|^{-\alpha_0}\int\widehat G_s(\xi)\overline{\widehat G_t(\xi)}\mu(d\xi)\,ds\,dt.$$

- $N_0(\theta)=\int e^{-\theta s}s\,ds=\theta^{-2}$. ✓
- $N_1$: $\lambda=\theta u$, $\xi=\theta\eta$ gives $\theta^{\alpha+\alpha_0-2}$. Finiteness: radial mass $\mu(B_r)=Vr^\alpha$ gives $\int\frac{\mu(d\xi)}{a^2+|\xi|^2}=\alpha Va^{\alpha-2}\int_0^\infty\frac{u^{\alpha-1}}{1+u^2}du<\infty$ ($0<\alpha<2$); remaining $\lambda$-integral finite by $\alpha_0>0$ and $\alpha+\alpha_0<2$. ✓
- $N_2$: substitution $s=u/\theta$, $t=v/\theta$, $\xi=\theta\eta$, using $\widehat G_{u/\theta}(\theta\eta)=\theta^{-1}\widehat G_u(\eta)$: total power $\theta^{\alpha_0}\theta^{-2}\theta^{\alpha}\theta^{-2}=\theta^{-\beta}$. ✓ Nonnegativity: time form is positive Laplace mixture of $e^{-\lambda|s-t|}$. ✓
- Tails: $0\le K_M(r)\le|r|^{-\alpha_0}$, $K_M\to0$ off diagonal; the absolute majorant of $N_2$ (split by $s\le t$, $t\le s$, singly singular $v^{-\alpha_0}$, $\alpha_0<1$) justifies dominated convergence. ✓
- Smoothing/truncation do **not** increase bounds: $N_1$ integrand nonnegative after Laplace; $N_2$ time quadratic form nonnegative at each $\xi$, so $[0,1]$-multipliers removable. ✓

*No gap.* The constant set $(A,B)=(N_1(1),N_2(1))$ is finite for the fixed covariance.

**PROOF214 (translated covariance CS).** Feature space $\mathcal H_L=L^2((0,L]\times\mathbb R^d\times\mathbb R;\,\nu(d\lambda)\mu(d\xi)dr)$, $h_\lambda(t,r)=\sqrt{2\lambda}e^{-\lambda(t-r)}\mathbf 1_{r\le t}$. Verified identities:
$$\int_{\mathbb R}h_\lambda(t,r)h_\lambda(s,r)dr=2\lambda e^{-\lambda(t+s)}\int_{-\infty}^{\min(t,s)}e^{2\lambda r}dr=e^{-\lambda|t-s|},\qquad \|\Phi_L(t,x)\|^2=\nu((0,L])\mu(\mathbb R^d).$$
So $\langle\Phi_L(t,x),\Phi_L(s,y)\rangle=\kappa_L(t-s)\gamma(x-y)=C_L((t,x),(s,y))$; Bochner Fubini gives $Q_L(f,g)=\langle F_L(f),F_L(g)\rangle$; Cauchy–Schwarz gives $|Q_L(f,h)|\le Q_L(f,f)^{1/2}Q_L(h,h)^{1/2}$. Two-variable translation gives $Q_L(T_{A,a}f,T_{A,a}h)=Q_L(f,h)$. With $h=T_{A-B,a-b}h$ applied through CS and translation invariance,
$$0\le Q(T_{A,a}G_1^0,T_{B,b}G_2^0)\le N_C(G_1)N_C(G_2),\qquad Q(T_{A,a}G_i^0,T_{A,a}G_i^0)=N_C(G_i)^2.$$
Independent origin $A-B$ and spatial origin $a-b$ **remain** when variables are relativized ($\kappa(u-v+A-B)\gamma(X-Y+a-b)$); coefficient exactly $1$, no division, zero norms covered. ✓

*No gap.* It is an inequality, not a quotation of the printed (3.5).

### WORK B — Fixed-order construction (005, 006)

**PROOF005 (spatial Wick measures).** Finite edge measures $\mu_e=e^{-(\epsilon_j+\epsilon_h)|\xi|^2/2}\mu$ with $\mu_e(\mathbb R^d)=V\Gamma_E(1+\alpha/2)(2/b_e)^{\alpha/2}<\infty$; $\gamma_e=p_{b_e}\ast\Gamma\ge0$. The Laplace transform
$$L_{\epsilon,D}(\lambda)=\int e^{-\frac12\sum_e(\epsilon_j+\epsilon_h)|\xi_e|^2}\prod_{l=1}^{2k}\frac1{(1+\lambda_l)^2+|\eta_l(\xi)|^2}\prod_e\mu(d\xi_e)$$
has nonnegative after-Laplace integrand (transform monotonicity). Heat bound $(p_t\ast\gamma_b)(x)\le A t^{-\alpha/2}$, $A=\alpha V\int_0^\infty u^{\alpha-1}e^{-u^2/2}du=2^{\alpha/2}V\Gamma_E(1+\alpha/2)$. Brownian occupation moment
$$\mathbb E_B S_b(T)^j\le\frac{(2j)!\,[A\Gamma_E(1-\alpha/2)]^j}{\Gamma_E((2-\alpha/2)j+1)}T^{(2-\alpha/2)j}$$
by ordering the $2j$ times, conditioning on the largest remaining vertex, removing the pair, integrating $j$ distinct selected adjacent gaps (Dirichlet $1-\alpha/2$). The wave-to-Brownian identity
$$\int_0^\infty e^{-qt}G_t(dx)dt=\frac12\int_0^\infty e^{-q^2u/2}p_u(x)\,du\,dx$$
holds by equal Fourier transforms $(q^2+|\xi|^2)^{-1}$. Horizon insertion $\frac14\int_{\tau_1}^\infty\int_{\tau_2}^\infty e^{-[(a-\tau_1)+(b-\tau_2)]/2}$ (also for empty chains, $\tau_i=0$) gives the uniform mass $U_k<\infty$; the $2^{-2k-2}$ factor is explicit. Spectral CS gives cross-pair $C_{12}\le\sqrt{S_1S_2}$; occupation product $\le(1+S_1)^k(1+S_2)^k$. Compactification $y_l=e^{-r_l}$, Bernstein polynomial density for uniqueness, continuity at zero excluding escape to infinity, $\lambda_l\to\infty$ giving $\nu_D\{r_l=0\}=0$; homogeneity $\rho_D(cA)=c^{(4-\alpha)k}\rho_D(A)$ (undamped only); positive-horizon faces $\ell_i=T>0$ null by disjoint-dilate/local-finiteness; empty-chain $\ell=0$ face has full mass and is *not* declared null. ✓

*No gap; input to 006.*

**PROOF006 (joint fixed-order).** Marked-temporal-tail bound: at unit damping, unmarked first norm $2A\le H$, second $B^2\le H$, $H=\max(1,2A,B^2)$; one marked edge costs $2A_M$ (first type, factor 2 from source) or $B_M^2$ (second type, edge twice). So
$$0\le F_{\epsilon,0,D}-F_{\epsilon,\eta,D}\le k e^{T_1+T_2}H^{k-1}\bigl(2A_{1/\eta}+B_{1/\eta}^2\bigr)\to0,$$
uniform in all positive vertex spatial widths, auxiliary temporal caps, Green widths. The imported Theorem 3.1 is applied only to damped kernels $e^{-s}G_s$ with finite edge measures and finite Laplace domains — its hypotheses verified edgewise, with 214 supplying the Case-2 step (keeping $A-B$; the printed offset-free equality is not used). Caps $\to\infty$ by positivity; Green removal at fixed positive spatial widths by bounded continuous covariance products + integrable full time-cube majorant. Fixed-$\eta$ spatial limits $b_D(\eta)$ Cauchy; squeeze $F_{\epsilon,\eta}\le F_{\epsilon,\delta}\le F_{\epsilon,\eta}+E(\eta)$ for all $\delta<\eta$ gives the joint arbitrary-rate limit. $L^2$-Cauchy via the **common Gaussian family** (max-time/summed-space covariance) with square+CROSS moments: $\|Y_n^a-Y_n^b\|_2^2\to Q_n+Q_n-2Q_n=0$. Unequal/empty chains retained; Green-first in $d=3$. ✓

*Named import:* only the source Theorem 3.1 induction beyond its hypotheses and the 214 Case-2 bridge; no source Theorem 4.1/Lemma 4.4/Section 5.

### WORK C — Summability, mild identity, mixed series (007, 008, 009, 002)

**PROOF007 (crude).** $\theta=\theta_0+n/t$; $P_n n^{-2n}\le2^n/n!$ (since $(2n)!\le(2n)^{2n}$); $(\sum z^n/\sqrt{n!})^2\le2e^{2z^2}$. Gives $\mathbb Eu^2\le2e^{2\theta_0t+2Ct^2}$. The author's asserted *uniform-in-$t$* (5.4) is not imported (S070); the uniform-in-$\theta\downarrow0$ loss is the repair. ✓

**PROOF008 (vertexwise).** Reversal to own roots per chain; Theorem 3.1 on $e^{-\theta r}G_r$ with finite edge measures; $D=\max(1,2C_0)$, $C_1=D^2$:
$$\|Y_n^a\|_2^2\le P_ne^{2\theta t}C_1^n\theta^{-2n}\ (\theta\ge\theta_0),\quad \theta=\theta_0+n/t\Rightarrow q_n=e^{\theta_0t}\frac{C^{n/2}t^n}{\sqrt{n!}}.$$
Ratio $z\sqrt{n+2}/(n+1)\to0$ gives $\sum\sqrt{n+1}q_n(T)<\infty$ with explicit tail $\sqrt{N+2}\,q_{N+1}/(1-\rho)$ after thresholds $N+1\ge2z^2/\rho^2$. ✓ Large-$\theta$ restriction is retained (no false small-$\theta$ uniformity).

**PROOF009 (mild).** Occupied multiplication $\|HF\|_2\le2\sqrt{n+1}\|H\|_2\|F\|_2$ via Hermite creation $(\le\sqrt{n+1})$ + annihilation $(\le\sqrt n)$ on degree-$\le n$ closed space; correlated $H,F$ allowed; never applied directly to infinite $u$ (product-series closure with an a.s. subsequence instead). Fixed external width $V_a=\gamma_\delta^0(0)\gamma_{2\epsilon}(0)$; uniform domination $2\sqrt n\sqrt{V_a}q_{n-1}(T)$. Fixed-random-factor Green averaging: for $F_s(z)=W_a(s,x-z)R(s,x-z)$ with $R$ $L^2$-continuous in $z$ and globally bounded in $L^2$, Bochner Fubini and compact modulus $\omega(r)\to0$ plus Gaussian tail $\min(1,d\eta/r^2)$ give the Green-width limit before noise removal. Partial/external/order limits: $\sup_{a>0}\|I_{n,a}\|_2\le q_n(t)$ (from 008 through the partial limit), 006 jointness removes $a$ at fixed $n$ first, tail $2\sum_{n>N}q_n(t)$. ✓ No uniqueness, no source Section 5(ii)/(5.3)–(5.4).

**PROOF002 (mixed).** Finite identity by Wick on one fixed family ($P_k=(2k)!/(2^kk!)$ partitions, coefficient 1, self/cross/empty included); Green-first at fixed noise widths. Product $L^1$ from $L^2$:
$$\|Y_mY_n-X_mX_n\|_1\le\|Y_m-X_m\|_2\|Y_n\|_2+\|X_m\|_2\|Y_n-X_n\|_2\to0.$$
Same-horizon reversal $s'_j=t-s_{m+1-j}$ with involution $\rho$, pairing bijection; independent roots retained. Series convergence from 007/008; mild identification from 009; $|\mathbb EU_N^2-\mathbb Eu^2|\le\|U_N-u\|_2(\|U_N\|_2+\|u\|_2)\to0$; nonnegative expected terms ⇒ monotone regrouping by total order. ✓

*Nonempty-imbalance finite check:* white/$\delta_0$ model, $D=\{(1,4),(2,3)\}$, first chain order 1, second order 3, the boxed domain gives $J_{(1,3),D}(t)\ge c^2 2^{-26}(32/9)^{\alpha_0}t^{6-2\alpha_0}>0$, so unequal orders survive (no pure-Wick orthogonality). ✓

---

## 3. Calibration core

### 001 (Jensen, cond. 008). $\mathbb Eu\ge1$ from nonnegative even pairing terms and 008-summability; CS transfer; $L_\*$-specialization conditional. ✓

### 003 (white test). Verified in §WORK-A header: $\int_0^s r(s-r)^{-\alpha_0}dr=\frac{s^{2-\alpha_0}}{(1-\alpha_0)(2-\alpha_0)}$, total $2c_0t^{3-\alpha_0}$. ✓

### 010 (envelope). Exact numerical-majorant algebra (§4 below): factorial denominator $(k!)^{3-\alpha-\alpha_0}$, exponent $\rho=\beta/(\beta-1)>\kappa$. **The lower bound is on $B_K$, never the moment.** $\mathbb Eu^2\le B_K$ is conditional on 002 (accepted). The historical false display omitting $2^{-\beta}$ and $(2/9)^\beta$ is corrected; those factors are present in the current source.

### 011/012 (white/static four). 011: 9 base rows with Green prefactor $1/16$, $F(a,b,c)=4ab-(a+b-c)_+^2+(|a-b|-c)_+^2$ exact area, $t^{6-2\alpha_0}$ scaling; disjoint-pair integrability is elementary (no 012-cycle). 012: time-first simplex reduction $1/(16m!n!)$, 27 chambers + reflections; **all 15 diagram coefficients recomputed exactly** (from the 46-row sector table): $(0,4)$: $11/17280$; $(1,3)$: $143/34560$; $(2,2)$: $31/17280$ interior, $31/2160=995/69984+47/349920$ two-piece; total $(22+143+187)/17280=11/540$; order-two $1/3$. Self/unequal/empty retained. ✓

### 013 (Riesz). Order-two: $\int G(s,y)G(r,z)c_\alpha|y-z|^{-\alpha}dy\,dz=\frac{c_\alpha[(s+r)^{2-\alpha}-|s-r|^{2-\alpha}]}{2(1-\alpha)(2-\alpha)}$; single-chain $c_\alpha rv^{1-\alpha}/(1-\alpha)$; $\mathbb EX_2=\frac{c_\alpha t^\beta}{(1-\alpha)\lambda(\lambda+1)(\lambda+2)}$, $\lambda=2-\alpha-\alpha_0$ (verified by $\int_0^t v^{\lambda-1}(t-v)^2dv=2t^{\lambda+2}/[\lambda(\lambda+1)(\lambda+2)]$). Order-four: $1/16$ inside four uniform laws, determinant-one triangular map, $t^{2\beta}$. ✓

### 014–019 (d1/low-$\alpha$). 014: descending integration invariant; weighted AM–GM gives exactly $K_{\rm sp}=c_\alpha2^{2-\alpha}(1-\alpha)^{-\alpha}/(2-\alpha)^{2-\alpha}$ (expanded in WORK: (§2 G2)). 015: temporal symmetry, $P_k\cdot2^{2k}/(2k)!=2^k/k!$, $k!k^{bk}\ge(k!)^{3-\alpha}$. 016: layer-cake $Vh^{1-\alpha}/(1-\alpha)$. 017: polar disintegration $\mu=dr\,\sigma(d\theta)$, $(g_h\ast p_{2a})(v)=I_a/\pi$, $0\le I_a\le\pi/2$; d1-white $V=c_\delta/\pi\Rightarrow c_\delta/2$ matching 014. 018: transfer with $K_{\rm sp}^{\rm gen}=V2^{2-\alpha}(1-\alpha)^{-\alpha}/(2-\alpha)^{2-\alpha}$ ($\alpha<1$), $\pi V$ ($\alpha=1$); the current source denominator is $(k!)^q$, $q=3-\alpha$ (the historical "(k!)³" quote is erroneous, not the source). 019: $2^{b+1}=2^{3-\alpha}$; $C_{1,\*}=C_{2,\*}/2^{(4-\alpha)/(3-\alpha)}$; strict $2C_{1,\*}<C_{2,\*}$; $L_\*$-step conditional. ✓

### 020–023 (conditional higher route). 020 assumes $H$:spatial-maximum with $\delta=\alpha-1$, $r\in(1/(1-\alpha_0),1/\delta)$ (nonempty since $\delta+\alpha_0<1$), $\theta=\alpha_0r'<1$, $a=1-\delta r/2>1/2$, $K=12M[\Gamma(1-\delta r)D_a]^{1/r}Z_\theta^{1/r'}$. Conditional only; does **not** use 014's low-$\alpha$ conclusion. 021: $M_3=c2^{1-\alpha}/(2-\alpha)$ via convexity/chord argument; d2 $M_2$ with $\alpha<3/2$; optimality by Fatou/approximate identity at maximizing shift. 022: Riesz PD via Gaussian mixture; ranges $d3\ 1<\alpha<2-\alpha_0$, $d2\ 1<\alpha<\min(3/2,2-\alpha_0)$. 023: wedge divergence at $\alpha\ge3/2$ (logarithmic at $3/2$); anisotropic $a_1+a_2/2>1$ failure; no-go scoped to the spatial supremum only (not existence, moments, or target scale). ✓

---

## 4. Numerical-majorant 010: exact identity and the false-display correction

$q=\beta-1$, $D=Ke^\beta(2/\beta)^\beta$. Exact $k$-th summand:
$$T_k(t)=D^k\frac{t^{\beta k}}{(k!)^q}\cdot(2k+1)\frac{P_k}{k!}\Bigl(\frac{k!}{k^k}\Bigr)^{\beta}.$$
Finite controls ($P_2=3$, $P_3=15$):
$$T_2\frac{(2!)^q}{t^{2\beta}}=\frac{15}{2}D^2\,2^{-\beta},\qquad T_3\frac{(3!)^q}{t^{3\beta}}=\frac{35}{2}D^3\Bigl(\frac29\Bigr)^{\beta}.$$

**Historical false display (not a premise):** the quoted $T_2=\frac{15}{2}D^2t^{2\beta}(2!)^{-\beta+1}$ and $T_3=\frac{35}{2}D^3t^{3\beta}(3!)^{-(\beta-1)}$ omit the factors $2^{-\beta}$ and $(2/9)^\beta$. The **current source** (S040/proof 1548–1600) correctly carries them, and the two-sided factorial bounds follow:
$$a=De^{-\beta},\ b=6D,\qquad \sum_k\frac{(at^\beta)^k}{(k!)^q}\le B_K(t)\le\sum_k\frac{(bt^\beta)^k}{(k!)^q},$$
using $1\le P_k/k!\le2^k$, $1\le2k+1\le3^k$, $e^{-\beta k}\le(k!/k^k)^\beta\le1$. Upper growth $\exp(qz^{1/q})$; lower by the single summand $k=\lfloor z^{1/q}/2\rfloor$, $z^k/(k!)^q\ge2^{qk}$. Since $q>1$, $\log B_K\sim t^{\beta/(\beta-1)}=t^\rho$, $\rho>\kappa$. The $25$ finite log-domain checks (five $\beta\in(2,4)$, five $k$) are consistent; they are finite falsification checks, not proofs.

---

## 5. JOIN-CONSTRUCTOR coupling

The chain closes as declared: **(004 + 214)** finite damped-norm/tail inputs and independent-origin Case-2 coefficient-1 → **(005/006)** positive spatial Wick-measure limit and arbitrary-relative-width/Green-first fixed-order construction → **(008/009/002)** occupied multiplication, weighted norm summability, mild identity, canonical mixed second-moment series. Verified properties:

- **Empty/unequal chains:** retained throughout (005 keeps $\ell_i$ per chain, empty chain $\tau_i=0$; 006/002 carry empty factors; 002 keeps $2k+1$ splits).
- **Independent roots:** the second chain has its own root $(0,0)$, never the first chain's last vertex; 214's independent origins feed Case 2.
- **Self-pairings:** ordinary (Wick) products retain them; the $(0,2)$ white term is half the cross term (003); unequal-order nonnegativity (002) is nonempty.
- **Same canonical solution:** 009's mild identification and 002's series both converge to the same $u=\sum_nX_n$; no uniqueness theorem invoked; no $\sigma(W)$-measurability stronger than the retained same-family construction.
- **A join, not a conjunction:** the marked-edge $2A_M+B_M^2$ (006), the width-uniform $\sup_a\|I_{n,a}\|\le q_n$ (009), and the coefficient-1 origin-free bridge (214) are each *specific* new results, not relabeling of prior labels.

---

## 6. CONTEXT / EXTERNAL role checks

- **S001 (T:first):** quoted two-sided $L_\*\le\liminf\le\limsup\le L^\*$ with printed normalization qualification; matches held author edition. Not an input to upper-bound proofs; numeric $L_\*$ uses remain conditional.
- **S002 (T:crude):** quoted $\mathbb Eu^2\le e^{Ct^2}$; the associated claim of uniform-in-$t$ in source (5.4) is recorded as internally inconsistent with 003 at $n=1$ (S070); own 007/008 repair it. The external remark is not used as a premise.
- **S064 (H:homog):** active global given; CONTEXT classification marks it as having no OWN proof body, not as optional. Matches every consumer.
- **S065 (H:spatial-maximum):** additional conditional premise, used only by 020–023; discharged for stated Riesz ranges (021/022), refuted elsewhere (023). Never promoted to all-model.
- **S067 (Conj:allp):** source conjecture, comparison context only; never forced to a constant.
- **S070–S072:** source-uniformity discrepancy and G0-verdict; the majorant loss is factorial $(\alpha_0)$-free?? No — correct: missing factorial power is $(k!)^{\alpha_0}$, exponent $\rho>\kappa$; scoped to the majorant. ✓
- **S073–S077:** calibration/scope remarks: $c_\alpha=(1-\alpha)/2$ normalization toward white; $V=0\Rightarrow u=1$; degree-one $d2/d3$ not spatial white; order-two ratio $2(3-\alpha_0)$, order-four $1/2$ vs $11/540$ as non-sharp checks; Skorohod comparison exponent-only with $H(2H-1)$ normalization and different solution concept.
- **S078:** conditional Jensen under spatial-maximum; $\alpha_0\to0$ exponent boundary only; BC comparison restricted to Riesz subclass; arbitrary homogeneous covariances remain outside the conditional argument. No sharp constant is identified there. ✓

---

## 7. Primary-source fidelity

[held back until the source author has been told]

---

## 8. Explicit finite checks recap

1. White order-two: $2c_0t^{3-\alpha_0}$, $c_0=[(1-\alpha_0)(2-\alpha_0)(3-\alpha_0)]^{-1}$.
2. Static order-four $11t^6/540$, order-two $t^3/3$, two-piece $31/2160$.
3. Envelope: $T_2(2!)^q/t^{2\beta}=(15/2)D^22^{-\beta}$, $T_3(3!)^q/t^{3\beta}=(35/2)D^3(2/9)^\beta$.
4. $M_3=c2^{1-\alpha}/(2-\alpha)$ ($F_3(1)=2^{1-\alpha}/(2-\alpha)$).
5. $C_{1,\*}=C_{2,\*}/2^{(4-\alpha)/(3-\alpha)}$.
6. Riesz static order-two unit coefficient $\to1/3$ under $c_\alpha=(1-\alpha)/2$.
7. Occupied multiplication constant $2\sqrt{n+1}$; Gaussian tail $\min(1,d\eta/r^2)$ for the fixed-factor Green limit.
8. d1 white $\alpha=1$ match: $V=c_\delta/\pi\Rightarrow$ closing $\pi V/2=c_\delta/2$.

---

## 9. Scoped verdict, confidence, limitations

**Verdict (scoped to A's actual contribution).** The 24 assigned OWN deductions are mathematically sound at their stated scopes. The finite/coefficient algebra (003, 010, 011, 012, 013, 014, 015, 016, 017, 019, 021) is exact and was checked symbolically; the structural/measure-theoretic constructions (004, 005, 006, 007, 008, 009, 002, 214) are internally consistent and acyclic along the dependency spine, and the JOIN-CONSTRUCTOR coupling closes without using any later infinite-moment bound as a premise. The historical false 010 displays are correctly distinguished from the current source, whose formulas are correct.

**Confidence.** High for the algebraic/finite calculations and for the logical acyclicity of the constructor subgraph. The main genuinely external dependency is the **named import of Theorem 3.1** beyond its edgewise-hypothesis verification + 214 bridge; this is the one place I have not (and cannot, within this scoped task) re-derived the source's induction. All other named imports (CH, BC) are comparison-only and correctly scoped.

**Genuine limitations / unresolved items.**

1. *Theorem 3.1 induction* (source external): only its hypotheses and the Case-2 step are owned; the induction interior remains a named import under the stated "named after exact source hypotheses" convention. A hidden defect in the source's non-Case-2 induction would propagate to 006/008/002/009/015/018/020 via this import.
2. *020–023 remain conditional/family-specific*: the spatial-maximum premise is discharged only for the explicit Riesz ranges; general homogeneous covariance with $1<\alpha<2-\alpha_0$ in $d=2,3$ is **not** covered by the A alternative route (the independent upper 051 is the general input, outside A's assessed set).
3. *010's $\mathbb Eu^2\le B_K$* is conditional on 002; I accepted 002, so the conditional is discharged within this review, but 010 remains a **numerical-majorant** result: its lower bound never bounds the actual moment, and it is a no-go for *that* uniform pairing majorant only.
4. *021 optimality and 023 anisotropic PD/Fatou*: heavier measure-theoretic arguments; I verified the endpoint values and the divergence structure, but did not re-do the full Fatou/approximate-identity argument from first principles at every maximizing-shift detail — these are accepted as correctly constructed rather than independently re-derived step-by-step.
5. *No whole-model coverage:* this A-set alone does not close the 214-OWN/240-declaration/13-join goal. In particular the **independent target-scale upper (051)** and the intrinsic/occupation/white-evaluation chain are outside the assigned A set and remain open here; the A alternative routes are retained with their explicit extra hypotheses/no-gos, not silently promoted to general inputs.
6. *Constants:* $C_0,D,C_1,C,q_n,A,B,K_{\rm sp},M_3,M_2$ depend on the fixed covariance/parameters and are nonsharp; no uniformity over model shapes or sharp-constant identification is inferred from the calibration gates.

No wholeHIGH, composition, image, or cold clearance follows from this scoped result. Required external gates (wholeMAIN/Kimi/source-pixels/full-visual/final-fresh-cold/private-delivery) remain open.