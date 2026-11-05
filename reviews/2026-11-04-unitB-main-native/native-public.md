# Unit-B reconstruction: PROOF024–PROOF060 (37), 48 declaration roles, and the two joined obligations

**Scientific target:** af97ae4db921a660b0a4ed1ffbe9b6f53a487e2b (manuscript hash `36475324…`). All historical payloads are treated as nonoperative data; verdicts and statuses are my own from the current source only. No tools used.

**Overall verdict (unforced).** All **37/37 B-OWN deductions (024–060) are reconstructed and internally verified** as written, under (a) their explicitly stated hypotheses, (b) the exactly-named external imports, and (c) narrowed applications of outside-owner OWN parents. **48/48 declaration roles covered** (37 OWN + 11 CONTEXT, including the global-given role of S064 and the source-qualification role of S071). **JOIN-INDEPENDENT-UPPER closes acyclically** from 044–048 → 049 → prelimit → 050+006 → canonical 051. The **B contribution to JOIN-CALIBRATION-ALTERNATIVES is assessed complete with explicit A/H boundary checks**; the full calibration join itself is *not* closed here because it consumes outside-B parents as named conditions.

**Confidence: HIGH** that the B-OWN mathematics stands as internally valid under its stated inputs. **MEDIUM** for unconditional acceptance of the whole B block, because the named external theorems (Chen–Hu static fixed-order/coefficient rate/(1.9); Chen-2023 (1.4)&(1.5); Crouzeix–Palencia Theorem 6/(3); author Theorem 3.1/(6.3)) have their proofs held external, and the narrowed A-owner clauses (002, 004, 005, 006, 008, 017, 018) are assumed valid rather than re-derived here. These are stated explicitly as remaining conditions, not hidden premises.

---

## 1. Notation and import ledger (checked)

Permanent conventions: $a=\alpha_0\in(0,1)$, $0<\alpha<d$ or $\alpha=d=1$, $\alpha+a<2$, $d\in\{1,2,3\}$; $\Gamma$ nonnegative even positive-definite homogeneous tempered Radon measure with spectral measure $\mu$ in the **unnormalized** convention $\Gamma=\int e^{i\xi\cdot x}\mu(d\xi)$; data $(1,0)$; original amplitude retained; zero covariance ⇒ $u=1$. Throughout, $\nu=3-\alpha$, $\beta=4-\alpha-a$, $\kappa=\beta/\nu$, and in the static block $q_{st}=4-\alpha=\nu+1$ (distinct from $q=3-\alpha$).

**External imports, each preserved as an import (no reproof claimed):**

| Import | Exact use | Hypothesis check |
|---|---|---|
| CH (published AOP 53(6)) Thm 3.8(i)/(3.23), p.2165 | fixed static order $L^2$ limits | static Dalang ($\chi<2$) verified by dyadic spectral annuli in **024/027/033** |
| CH (2.17)/(2.19)/(2.18)/(2.20)–(2.22) | full split/pairing coefficient $B_k$; generalized-covariance heat convention | matched to full $2k{+}1$-split, all-pairing, self/empty-unions |
| CH (5.1), p.2173, and (5.15), p.2180 | homogeneity $B_k(t)=t^{(4-\chi)k}B_k(1)$; coefficient rate at $p=2$ | $p=2$ gives $B_k$ exactly; rate is *coefficient* rate, not a log-moment/time assertion |
| CH Thm 1.2 / (1.9) (published static) | **054/058** static raw rate $L_0$, $p^{\kappa_{st}}$ | **raw** $\mathbb E U^p$, not $\|U\|_p$; Jensen/054 enforces raw reading |
| C23 Thm 1.1 **quartic (1.5)** | **036** seed at real unit-$\!L^2$ Schwartz | $\chi<2$ Dalang; quartic energy minus $\tfrac12$gradient |
| C23 Thm 1.1 **square-root (1.4)** | **027/033** via CH p.2175 identification $E_{1/2}=2^{\chi/(4-\chi)}\mathcal M$ | finite under Dalang; separate from (1.5) |
| CP author-preprint v1, (3) p.1, Thm 6 pp.5–6 | **039/045** bounded numerical-range spectral set, constant $1+\sqrt2$ | bounded operators; holomorphic $C_h,F_h,H_h$ near closed $W(T)$ |
| author Thm 3.1/(3.6); (2.23)–(2.24); (6.3) | pairing inequality (in external fixed-order 006 chain); source law; complex Laplace | edgewise finite Gaussian/Laplace hypotheses checked; (3.4) absolute-bars and (3.5) independent-variable/offset qualifications retained |
| Balan–Conus | **comparison only** | **no B proof imports it as a premise** |

No Teschl statement is cited in any of the 37 B bodies (the later $C/H$ blocks use it; outside this unit).

---

## 2. Reconstruction of the 37 OWN deductions

### 2.1 Static-rate and interpolation finite inputs (024, 027)

**WORK024 — L:static-holder-input (CHECKED).** Hypotheses: static $\gamma_\chi=c|x|^{-\chi}$, $d\in\{2,3\}$, $1{<}\chi{<}2$, data $(1,0)$. Dalang: $\mu(B_r)=Vr^\chi$ (Fourier uniqueness of covariance homogeneity), hence $\int(1{+}|\xi|^2)^{-1}d\mu \le V[1{+}2^\chi\sum_j2^{j(\chi-2)}]<\infty$. CH 3.8(i) gives $U_n$; (2.17)/(2.19) identify $B_k=\sum_{m=0}^{2k}\mathbb E[U_mU_{2k-m}]$ with all pairings/splits; (5.1) homogeneity; (5.15) at $p{=}2$ gives finite upper root rate; finite-order enlargement yields one finite $C_{st}$ with $B_k(t)\le C_{st}^k t^{(4-\chi)k}/(k!)^{3-\chi}$, $B_0=1$. Zero $\Xi$: $C_{st}=1$. *Remaining condition:* CH statements external; $\mathcal M$ finiteness carried by CH/C23.

**WORK027 — L:planar-static-input (CHECKED).** Same route for *general* planar Radon $\Xi$, degree $\chi\in(1,2)$, via the generalized convention (2.18); Dalang by annuli; CH 3.8(i), (5.1)/(5.15); C23 (1.4) for $\mathcal M$ finiteness **not** the quartic. *Distinct role from 036:* 036 uses quartic (1.5); 027 uses square-root (1.4).

### 2.2 Interpolation transfers and planar branches (025, 028, 029)

**WORK025 — P:static-holder-upper (CHECKED, conditional inputs).** Riesz $\gamma_\alpha=c|x|^{-\alpha}$, $d{=}2,3$, $1{<}\alpha{<}2{-}a$. Common positive disjoint-union measure over all splits/pairings/ordered time/Green increments; $\gamma_\alpha=\gamma_1^\vartheta\gamma_\chi^{1-\vartheta}$ (same $c$), Gaussian Hölder on $p_\epsilon$; temporal $Q_\delta\le T_{b_0}^\vartheta$; Hölder on the whole measure gives $A_k^{reg}\le L_k^{\vartheta}B_k^{1-\vartheta}$. Low half: closing bound $\pi V_1/2$ (**017**), descending integration gives spatial $(2M)^k t^k/k^k$; temporal pairing-sum symmetry gives exactly $\tfrac{2^k}{k!}$; so $L_k\le C_{low}^k t^{(3-b_0)k}/(k!)^2$, $C_{low}=2Z_{b_0}\pi V_1$. Exponent identities close to $A_k\le C^k t^{\beta k}/(k!)^\nu$. *Consumes narrowed:* 024 (static $C_{st}$), 017 ($\alpha{=}1$ closing), 002 ($\mathbb E u^2{=}\sum A_k$ nonnegative), 006 (width limits). All exponents verified.

**WORK028 — P:planar-upper (CHECKED, conditional inputs).** Identical algebra with **026** endpoints; $C_{low}=Z_{b_0}S$ from the planar $S/4$ closing. No 017 import (026 is self-contained). Consumes narrowed 027, 002, 006.

**WORK029 — C:planar-range (CHECKED).** Union: $\alpha\le1$→018 (all-$d$ low bound), $1{<}\alpha{<}2{-}a$→028, $\Gamma{=}0$→$u{=}1$. Only $d{=}2$; no generalized $d{=}3$ factorization asserted.

### 2.3 Endpoint geometry and conditional three-dimensional route (026, 030, 031, 032)

**WORK026 — L:planar-endpoints (CHECKED).** $\Gamma(\{0\})=0$ by homogeneity ($2{-}\alpha>0$); $S$ finite positive; polar disintegration $r^{1-\alpha}dr\,\sigma(d\omega)$ by annulus-rectangle measure uniqueness. $\Gamma_{low}$ PD by full-sphere line representation with factor $\tfrac12$ and line-perpendicular squares; $\Gamma_{st}$ PD by convergent Gaussian mixture $e^{-s|x|^2}\Gamma$, exponent $\chi{-}\alpha>0$. Line section of disk Green $= \tfrac12$ ⇒ closing $S/4$; heat averaging preserves. Gaussian Hölder on the **unnormalized** measure $p_\epsilon(z-x)\Gamma(dx)$, exponent identity $\vartheta(\alpha-1)+(1-\vartheta)(\alpha-\chi)=0$.

**WORK030 — L:product-endpoints (CHECKED).** $L_j,U_j,\Lambda,b_j,v_j$ construction: verify $\sum_jL_j<1<\sum_jU_j$ (the $r\ge2$ case uses $\alpha<2-\vartheta\le r-(r-1)\vartheta$ with strictness), $\Lambda\in(0,1)$, active coordinates in $(0,1)$, zeros preserved. PD by coordinatewise Gaussian mixtures; zero powers are constants. Hölder on Gaussian probability; same amplitude $c$.

**WORK031 — L:plane-endpoints (CHECKED).** $m=dy\,\delta_0(dz)$; $v_j=a_j/(1-\vartheta)<1$; PD includes normal Dirac by slicing; Hölder on unnormalized $p_\epsilon$. Spectral check: $\mu_{low}=\frac{c}{2\pi}\delta_0(d\xi_1)\delta_0(d\xi_2)d\xi_3$ ⇒ $V_{low}=c/\pi$ (verified against the $(2\pi)^{-d}\widehat\gamma$ normalization).

**WORK032 — L:endpoint-closure (CHECKED).** General Gaussian via $q_\Sigma=p_b*q_{\Sigma-bI}$; pushforward $p_\epsilon*T_\#J(x)=d_T^{-1}(q_\Sigma*J)(T^{-1}x)$, $\Sigma=\epsilon T^{-1}T^{-\top}$ (determinant verified); finite sums by discrete Hölder; exotic PD via $\psi=\varphi\circ T$.

### 2.4 Conditional d3 transfer, corollaries, spectral energy (033, 034, 035, 036)

**WORK033 — P:three-transfer (CHECKED, conditional; narrowed 017/036/002/006 + CH/C23).** Hthree is an explicit extra assumption. Common-measure Hölder; low closing $\pi V_{low}/2$ (**017**); $C_{st}$ in $d{=}3$ via the 027 route; **036** supplies measure-form correctness + finiteness of $\mathcal M_{st}$; C23 (1.4)/CH p.2175 supply the rate. Green-first source identification is the genuinely delicate part and is present in full: continuous field versions (Kolmogorov, Gaussian moments), Bochner integrals, $L^2$–pathwise Fubini duality, square and mixed $\eta/0$ moments. All-time constant $C_{st}$ and asymptotic $\Lambda_{st}$ kept distinct; finite low orders retained as a power sum before sending $r\downarrow0$. *Remaining:* Hthree conditional to 030/031/Riesz + 032 closures; imported CH 3.8(i)/(2.18)/(5.1)/(5.15), C23 (1.4).

**WORK034 — C:three-product-riesz (CHECKED, conditional).** Products: 030. Riesz: $\gamma_1=c|x|^{-1}$, $\gamma_\chi=c|x|^{-\chi}$, Gaussian-mixture PD, Hölder. Exponent-1 coordinate excluded.

**WORK035 — C:three-finite-images (CHECKED, conditional).** Common midpoint; 030/031/034 endpoints; 032 composition; no stochastic solution addition, no infinite-mixture limit.

**WORK036 — L:physical-spectral-energy (CHECKED).** $\Xi$ on $\mathbb R^3$, $0{<}\chi{<}2$. Duplicated: Dalang by annuli; **C23 (1.5) quartic** seed at unit-$L^2$ real Schwartz gives $Q(f)\le\tfrac12\|\nabla f\|^2+C_0$; two *distinct* Cauchy bounds — spectral $P(f,h)\le\sqrt{Q(f)Q(h)}$ and product-energy $\mathscr E(fh)\le\sqrt{Q(f)Q(h)}$. Full $H^1$ extension via $A_f(y,z){=}f(y{+}z)f(y)$, $B_f{=}\widehat{f^2}$, strong $L^2$ closeness, Lebesgue-$y$-first sigma-finite Fubini (no Lebesgue-null $\Rightarrow$ $\Xi$-null), uniform Fourier convergence from $L^1$ convergence of squares. Representative independence and quartic bound pass.

### 2.5 Static phase block (037, 038, 039, 040, 041, 042, 043)

**WORK037 — L:phase-contractions (CHECKED).** Spectral and **physical** masses kept distinct ($V=\mu(B_1)$, $M=\Gamma(B_1)$). Resolvent: translated-heat domination by physical nonnegativity + evenness; $R_\alpha=\frac{\alpha\pi V}{2\sin(\pi\alpha/2)}$. Physical trace: radial test against $G_a*p_{2\epsilon}$; $c_\Gamma=\frac{(3-\alpha)M}{4\pi}$; the sphere convolution equals $\frac{(a+r)^{2-\alpha}-|a-r|^{2-\alpha}}{2r(2-\alpha)}$ (verified, including the $1/(4\pi a)$ density cancellation); region bounds $2^\alpha$, $1$, $3^{2-\alpha}/(2-\alpha)$; $D_\Gamma=c_\Gamma b_\alpha$. Plain d3 scope.

**WORK038 — P:static-phase-variance (CHECKED).** Both phase entries; general-$\lambda$ Born and mean. Free coefficient $|a_s|^2\le(1+\lambda^2s^2)e_\lambda$; output $|k_\tau|^2\le\frac{1+\lambda^2h^2}{\lambda^2+r^2}$; same-field Born via 037. Mean: multiplier $T_\epsilon(s-r,\eta)$, norm $\le D_\Gamma(s-r)^{1-\alpha}$. Free growth both directions via the absolute differentiated energy bound; $K_\epsilon=\mathbb E\|Z_1\|^2+2\operatorname{Re}\langle Z_0,\mathbb E Z_2\rangle$; no sign on the mean term. First-variance only, not all-order.

**WORK039 — L:complex-phase (CHECKED).** $I_a=\mathrm{Beta}(\tfrac12,1-\tfrac a2)$; at $a=\alpha/2$ the second argument is $1-\alpha/4$. Ordered relative inverse-root integral; $Q=A_\lambda^{1/2}L_\lambda^{-1/2}$; four ordered root comparisons $\le2$; numerical-range parabola; scalar bounds; CP import; block sum $\le100e^{2\lambda h}$. Bounded operators only.

**WORK040 — L:fock-form (CHECKED).** The current source correctly uses the **double half-weight** identity $\sum_i\|H_if\|^2=(2\pi)^{-d}\int\frac{|\hat f|^2}{\rho^2+|\eta|^2}J_{\rho\epsilon}d\eta$, $H_i=A_\rho^{-1/2}M_{e_i}A_\rho^{-1/2}$, yielding $\sum H_i^2\le R_\alpha\rho^{\alpha-4}I$; row=column by self-adjointness; creation $\sqrt{j+1}$, annihilation adjoint; $d_N=2\sqrt{N+1}\sqrt{R_\alpha}$. The unweighted column (needed in 044/047) is the separate identity without the input weight. (The historical "missing half-weight" caption was a report-level error; the source is correct.)

**WORK041 — L:finite-word-cutoff (CHECKED).** Exact selected-prefix degree induction; retention of lowering/self-contractions; equality for finite sums and existing Bochner word integrals; not a full truncated-flow identity.

**WORK042 — P:static-phase-all-orders (CHECKED).** 039+040+041 at $a=\alpha/2$; complex vector Cauchy; $\lambda=n/h$; $A_\alpha=400\sqrt2e^2/\delta_{\alpha/2}$; factorial exponent $(3-\alpha)/2$; band then mode removal at fixed $\epsilon,n$ with no zero-smoothing limit; scalar series with correct Hölder powers $(\cdot)^\beta(\cdot)^{1-\beta}$ for $\beta<1$ and $\ell^\beta/\ell^1$ for $\beta\ge1$.

**WORK043 — C:static-interaction (CHECKED, 038 general-$\lambda$/042).** Both Born and mean terms; $S_0(-h)$ cost $\sqrt e$; parity/factorial pairings; $B_\alpha=3eA_\alpha^2$; dyadic powers $h^{1-\alpha}$, $h^{2-\alpha-a}$, $h^{2\beta-3}$ all positive; only independent NEXT-field partitions.

### 2.6 Interval/upper chain (044–051)

**WORK044 — L:interval-contractions (CHECKED).** Dimension-free rederivation: translated heat/resolvent domination; $R_\alpha\rho^{\alpha-2}$; unweighted column; vacuum insertion $\sqrt{R_\alpha}\rho^{(\alpha-2)/2}$; occupied Fock $2\sqrt{N+1}\sqrt{R_\alpha}\rho^{\alpha/2-2}$. Physical origin atoms not excluded ($d{=}1$ white lives here); spectral origin atom zero. Tensors with other Hilbert factors.

**WORK045 — L:interval-complex (CHECKED).** Nonselfadjoint $V$, $V^*$ same sandwich; same four ordered roots; parabola; piecewise $\Lambda(t)=\lambda+\sum\omega_i1_{I_i}$; ending charge exactly once per connected interval including final return; start/insertion cost no extra factor.

**WORK046 — L:inventory-product (CHECKED).** $z=\theta k^\nu$, $\theta=1/4$; $Q_i=\theta ki^{-p}$ (by $\nu+\alpha-2=1$); fine/coarse splits; strict windows; $[z^k]\prod\le C^k/(k!)^\nu$, $C=C(\alpha,\alpha_0)$. No multinomial/inventory-size constant.

**WORK047 — L:fixed-split (CHECKED).** $N_i=2k_i$ exact; common partition $\le3k{+}1$; one-copy $M_k=100^{3k+1}e^{4k}$, two-copy square $e^{8k}$; cross colors fresh per copy, occupied backgrounds joint-Hilbert; cross cube volume $\le\prod h_i$ with no factorial; normalized vector Cauchy; singleton mean one metric factor; **$R_\alpha^k$ counted exactly once** ($|C|+\sum_Bk_i=k$).

**WORK048 — P:interval-coefficients (CHECKED).** Ordinary coefficients; strong cutoff identification via nonuniform $v_{max}$ entire majorant (never in the uniform constant); reflection parity $r_i+q_i=2k_i$; $\le3^k$ splits; whole positive-length substitution $h_i\le LT/i$; ordinary generating product = exactly one count per allocation; 046 closes; absolute-majorant summation (coefficients not claimed nonnegative); phase bound $e\exp(CR_\alpha^{1/\nu}T^{\beta/\nu})$.

**WORK049 — L:terminal-wick (CHECKED).** Terminal mass $T^{2n}/(2n)!$ by recursion; Gaussian product bound; MGF differentiation ⇒ every pairing coefficient exactly 1; symmetrization adds no factorial; nonnegativity comparison entrywise; absolute series at every $r$; d3 Green-first. Does **not** supply width-uniform $B_r$.

**WORK050 — L:uniform-series-tail (CHECKED, conditional).** Given width-uniform $B_r$ for $r>1$ and fixed-order L2 limits: diagonal extraction gives $\|Y_n\|\le B_r^{1/2}r^{-n}$; geometric tails; canonical convergence is the *conclusion*. $B_1$ passes separately.

**WORK051 — T:full-upper (CHECKED).** Nested three-shift grids: shifts differing by $\pm h_j/3$ give boundary mutual separation $h_j/3$; covering at $3d<h_j\le6d$; $H_0\in[6T,12T)$ ensures a scale exists. Inventory $h_i\le78T/i$, $\sigma_I^2=6^a|I|^{-a}$ (cumulative count through level $j$: $6T/h_j+6(j+1)\le78T/h_j$). Compact flap $f_T$ gives causal identity, volume ratio $(T+2)^d=|B_{T+2}|/|B_1|$ with no derivative norm. Entrywise positive Wick comparison $\gamma_\delta^0\Gamma_\epsilon\le K_J\Gamma_\epsilon\le K_\infty\Gamma_\epsilon$ at fixed widths/finite order; $K_\infty$ only a numeric majorant under positive integrals. Enlarged amplitude $B(T;b)$; Green-first at fixed widths; $N\to\infty$ via 049; canonical close via 006 + 050 with $B(T;2)$, final bound via $B(T;1)$. **Imports limited to** 048/049/050/006 + author (2.23)–(2.24); *no* 002/007/008/source-Section-5/variational finiteness. 009 is a parallel mild-designation premise of the theorem's wording, not a rate input.

### 2.7 Static-moment/calibration chain (052–058)

**WORK052 — L:mean-coefficient-holder (CHECKED, narrowed 005/006/008/049/050/051-prelimit).** Static endpoint built directly: temporal covariance 1 (not $\Gamma_E(0)$); floor $c=\gamma^0_{\delta_0,b_0}(1)>0$; static amplitude $r$ dominated by fractional $r/\sqrt c$; enlarged-amplitude prelimit bound ⇒ geometric static tails (050); raw-time exponent Hölder on a common positive measure; width limits per fixed exponent; diagram scaling $\beta(a)k$. No interpolation of exponent-dependent Laplace or Gamma prefactors.

**WORK053 — L:positive-series-type (CHECKED).** $\tau=\nu K^{1/\nu}$; optimized coefficient test at $z=(\nu k/L)^\nu$; Stirling; exceptional-polynomial converse. Factorial power is $\nu$, not $q_{st}$.

**WORK054 — P:static-minorant-lower (CHECKED, narrowed 006 + CH (1.9)).** Temporal minimum $c_{\delta,T}\to T^{-a}$; finite nonnegative diagram ordering for $p=1,2$; Green first; fixed-order noise removal; static amplitude clock $\sigma=T^{-a/2}$ ⇒ $T_{\mathrm{eff}}=T^{1-a/(4-\alpha)}$; **raw** published static rates $p^{\kappa_{st}}L_0$. $T_{\mathrm{eff}}^{\kappa_{st}}=T^{\kappa(a)}$ verified.

**WORK055 — P:near-static-mean-gap (CHECKED, narrowed 051–054 + 052/053).** $K(0)=(L_0/\nu)^\nu>0$; anchor via 051/Cauchy; root-limsup Hölder; window $a_*$; $2M(a)<2^{\kappa_{st}}L_0$ since $\kappa_{st}=1+1/\nu$. $M(a)$ is the actual raw mean limsup, not $E|u|$, not $S_1^{pos}$.

**WORK056 — L:full-moment-coefficient-holder (CHECKED, narrowed 005/006/002/052).** Full raw coefficients with both empty orientations for $p{=}2$; disjoint-union Hölder; terminal-to-initial reversal identifies static endpoint.

**WORK057 — P:moment-growth-logconvex (CHECKED, narrowed 051/053/054/056).** Raw upper rates positive finite; factorial-root log-convexity (endpoint $\pm\epsilon$ handles zeros); interior continuity via finite secant slopes.

**WORK058 — C:static-moment-constant-continuity (CHECKED, 054/057; no 055 edge).** Fix $\Gamma$+anchor first; time liminf/sup per fixed $a$ with its own normalizer, then $a\downarrow0$; squeeze to $C_p$; ratio $\underline\Lambda_2/\overline\Lambda_1\to2^{\kappa_{st}}$ (needs $L_0>0$). No simultaneous limit, no fixed-$a$ time-limit from interpolation.

### 2.8 Clock block (059, 060)

**WORK059 — L:white-clock-laplace (CHECKED).** Cross spatial contraction $\min(s,t)/2$; splitting $s=t+v$, $t=s+v$; $K_\times=\frac{\Gamma_E(1-a)}{2(\theta_1+\theta_2)^2}(\theta_1^{a-1}+\theta_2^{a-1})$; $K_{self}=\frac{\Gamma_E(1-a)}{2\eta_1^2\eta_2^{1-a}}$. Gap damping distinct from physical unequal-horizon factor $|T_1-T_2-s+t|^{-a}$.

**WORK060 — P:clock-copy-obstruction (CHECKED, narrowed 004+author (6.3)).** $h_\Gamma(w)=w^{-\alpha/2}h_\Gamma(1)$, $\mathcal R_\Gamma(q)=q^{\alpha-2}\mathcal R_\Gamma(1)$ without density; positive density $w_\theta(\lambda)=\frac{\lambda^{a-2}}{2\theta\Gamma_E(a)}[\mathcal R(\theta)-\mathcal R(\theta+\lambda)]$; $K_\Gamma=\int w_\theta$; admission $0\le J_\rho\le J_1$; closed form $J_1=\int\frac{2\theta}{2\theta+\lambda}w_\theta\,d\lambda<K$ strictly; at $\alpha=1$ the Beta integral gives exactly $2-2^a$ (degree-one only). No Skorohod result; only the literal analytic-copy family is obstructed.

---

## 3. Compact declaration-role coverage (48)

**37 OWN declarations** — each matched to its proof and verified, grouped:

| Formal | Role | Status |
|---|---|---|
| S003 | T:full-upper | OWN, checked (051) |
| S016 | L:static-holder-input | checked (024) |
| S017 | L:planar-endpoints | checked (026) |
| S018 | L:planar-static-input | checked (027) |
| S019 | L:product-endpoints | checked (030) |
| S020 | L:plane-endpoints | checked (031) |
| S021 | L:endpoint-closure | checked (032) |
| S022 | L:physical-spectral-energy | checked (036) |
| S023 | L:phase-contractions | checked (037) |
| S024 | L:complex-phase | checked (039) |
| S025 | L:fock-form | checked (040) |
| S026 | L:finite-word-cutoff | checked (041) |
| S027 | L:interval-contractions | checked (044) |
| S028 | L:interval-complex | checked (045) |
| S029 | L:inventory-product | checked (046) |
| S030 | L:fixed-split | checked (047) |
| S031 | L:terminal-wick | checked (049) |
| S032 | L:uniform-series-tail | checked (050, conditional) |
| S033 | L:mean-coefficient-holder | checked (052) |
| S034 | L:positive-series-type | checked (053) |
| S035 | L:full-moment-coefficient-holder | checked (056) |
| S036 | L:white-clock-laplace | checked (059) |
| S047 | P:static-holder-upper | checked (025) |
| S048 | P:planar-upper | checked (028) |
| S049 | P:three-transfer | checked (033, conditional Hthree) |
| S050 | P:static-phase-variance | checked (038) |
| S051 | P:static-phase-all-orders | checked (042) |
| S052 | P:interval-coefficients | checked (048) |
| S053 | P:static-minorant-lower | checked (054) |
| S054 | P:near-static-mean-gap | checked (055) |
| S055 | P:moment-growth-logconvex | checked (057) |
| S056 | P:clock-copy-obstruction | checked (060) |
| S059 | C:planar-range | checked (029) |
| S060 | C:three-product-riesz | checked (034) |
| S061 | C:three-finite-images | checked (035) |
| S062 | C:static-interaction | checked (043) |
| S063 | C:static-moment-constant-continuity | checked (058) |

**11 CONTEXT declarations** — role coverage (no invented proof bodies):

| Formal | Role | Coverage |
|---|---|---|
| S066 | H:three-endpoints | **conditional** extra covariance datum; used only by 033–035 and discharged by 030/031/Riesz + 032; never an all-$\Gamma$ given (that is S064) |
| S068 | G:upper | goal context; discharged by S003/051 at the canonical scale |
| S079 | R:static-holder-scope | scope for 025: isotropic Riesz only, anisotropic excluded |
| S080 | R:planar-scope | scope for 026–029: planar-specific, no d3 extension |
| S081 | R:three-endpoint-scope | scope for 033–035: Hthree extra condition; printed-normalization qualification retained |
| S082 | R:full-upper-boundary | scope for 051: nonsharp, static exponent boundary, intrinsic value outside |
| S083 | R:near-static-scope | scope for 054/055: window depends on fixed covariance/anchor |
| S084 | R:temporal-type-scope | scope for 056–058: iterated time-then-$a$ only |
| S085 | R:clock-copy-scope | scope for 059/060: literal analytic-copy family only |
| S064 | H:homog | **global given premise** actually consumed by every B body (spectral ball law, PD, homogeneity, data); CONTEXT label means “no OWN proof body,” not vacuous |
| S071 | R:source-case2-time-shift | **source qualification**, not a deduction target; its Case-2 offset / independent-variable facts are reflected in 004/006 and match the author hypotheses |

---

## 4. The two joined obligations

### 4.1 JOIN-INDEPENDENT-UPPER — **CLOSED acyclic within its own chain**

- $044+045+041\to047$ (bounded nonselfadjoint phases, occupied/fresh colors, exact finite-split).
- $046+047+041\to048$ (ordinary interval coefficients, parameter-only $C$).
- $048+049+\text{localization}+\text{numerical positivity}\to$ prelimit $B(T;r)=e(T+2)^d\exp\{C(r^2R_\alpha)^{1/\nu}T^\kappa\}$ for every $r>1$, built **before** the canonical limit.
- $B_r$ + 006 fixed-order joint limits → 050 → canonical upper by $B(T;1)$.

No member of this chain consumes 002/007/008, source Section-5 convergence, Theorem 4.1/Lemma 4.4, or variational/intrinsic finiteness. 009 remains a parallel physical-mild designation. The only external legs are (i) the author universal pairing inequality inside the outside-owner fixed-order 006 route, and (ii) the bounded CP theorem reached through 039/045. The join is assessed **in full at the stated applications, and it closes** under those two named inputs and the A-owner fixed-order clause.

### 4.2 B contribution to JOIN-CALIBRATION-ALTERNATIVES — **ASSESSED, boundary-explicit**

**B internal items verified:** all finite white 27-domain/45-sector calibrations (011/012 via 059/060 context), Riesz normalization and Abel/degree-one convolutions (016/017 narrowly), temporal pairing symmetry ($2^k/k!$, zero factorial loss), conditional higher/planar/static/d3 routes with correct parameter windows, and the clock no-go limited to the literal copy family.

**A/H boundary checks (remaining conditions, not assumed closed):**

| Outside-B item | Narrow clause consumed by | Status |
|---|---|---|
| 002 P:mixed | 025/028/033/056 ($\mathbb E u^2=\sum_k A_k$ nonnegative) | narrowed, unverified in this unit |
| 004 L:damped-homogeneous-norms | 060 ($N_2(\theta)^2=K_\Gamma(\theta)$, finiteness) | narrowed |
| 005 L:spatial-wick-measures | 052/056 (spatial diagram limits) | narrowed |
| 006 L:joint-fixed-order | 025/028/033/052/054/056 (width limits) and 051 tail | narrowed; its own Theorem-3.1 induction remains a named extern |
| 008 L:vertex-crude | 052 (mean-series interchange) | narrowed |
| 017 L:alpha-one-convolution | 025/033 ($\pi V/2$ closing) | narrowed |
| 018 P:low-alpha-upper | 029 ($\alpha\le1$ branch) | narrowed |

**Boundary principles honored:** a numerical-majorant lower bound is never an actual-moment lower bound; no conditional alternative is promoted to the general theorem input; S1pos stays auxiliary; no actual $p_1$, Skorohod result, or printed-constant correction is manufactured; zero covariance handled directly everywhere; full $214/240/13$ and the actual intrinsic $C_2$ remain whole goals outside this unit.

---

## 5. Explicit genuine remaining conditions (honest)

1. **External theorem proofs are held, not verified here:** CH 3.8(i)/(2.18)/(5.1)/(5.15)/(1.9); C23 (1.4) and (1.5); CP Theorem 6/(3); author Theorem 3.1 and (6.3). A falsity of any one would transfer to its B consumers (listed in §2).
2. **A-owner narrowed clauses** (002, 004, 005, 006, 008, 017, 018) are assumed valid at their stated statements; if any is false, the affected B transfers (column in §4.2) become conditional. Per the operative rule, a checked narrow subclause suffices and is what I verified — not full-parent clearance.
3. **033–035 remain conditional under Hthree** for general $d{=}3$ covariance; no universal $d{=}3$ factorization is asserted.
4. **The static phase block 036–043 is standalone $d{=}3$** (as written); dimension-free support enters through 044. This is a scope note, not a gap.
5. **055’s gap / 058’s recovery are iterated-order statements**; no fixed-$a$ time-limit existence follows from interpolation, and $S_1^{pos}$ is never identified with an actual first-moment rate.

No unfinished B reconstruction remains *within* the assigned 37; the remaining conditions are exactly the externally imported statements and narrowed outside-B parents, now enumerated rather than hidden.