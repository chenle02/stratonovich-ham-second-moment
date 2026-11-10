# Whole-current review: Stratonovich second-moment argument (af97)

## 0. Scope of this judgment

This is a text-level mathematical review of the supplied current manuscript
`notes/notes_stratonovich_ham_second_moment.tex` (SHA
`364753242f9d02e57036af586ab8e777b184d897862750d3170d79f028067914`) together with
its 28 supporting modules, maps, supplements and primary texts. It is **not** a
certification of source pixels, of the rendered paper, or of the author PDF
images. Source availability has never been treated by me as proof of a
statement. The Kimi/source/visual audit, the independent fresh cold
paper-and-bibliography-only read, and the whole `HIGH` gate remain open and are
not discharged by this review.

I have read the supplied mathematics as evidence and reconstructed the main
chains below from the actual formulas, quantifiers and consumers. For items I
did not independently re-derive end-to-end I mark them explicitly `LIMITED` or
`NOT_READ`; I do not fill unread load-bearing steps with invented proofs.

**Unforced judgment at the end:** the main constructions are coherent and the
signature formulas are faithful to the source, but a number of large
`LIMITED`/`NOT_READ` remainders prevent a complete scientific acceptance of all
214/240/13 items in one pass. My verdict is **INCONCLUSIVE**, confidence
**medium** for the core chains and **low** for complete whole-program closure.

---

## 1. Original model and constant audit

The standing model `H:homog` (formal `S064`) is the given assumption, not an
OWN theorem:

- $d\in\{1,2,3\}$;
- $0<\alpha_0<1$, write $a=\alpha_0$;
- $0<\alpha<d$ or $\alpha=d=1$ (spatial white);
- $\alpha+\alpha_0<2$;
- $\Gamma$ is a nonnegative, even, positive-definite tempered Radon measure with
  $\Gamma(cA)=c^{d-\alpha}\Gamma(A)$;
- spectral convention $\Gamma=\int e^{i\xi\cdot x}\mu(d\xi)$ distributionally;
- data $(1,0)$;
- zero covariance handled directly ($u=1$, $C_2=0$).

Constants and exponents actually used:

$$
\nu=3-\alpha,\qquad q=4-\alpha,\qquad
\beta=4-\alpha-\alpha_0,\qquad
\kappa=\frac{\beta}{\nu}=\frac{4-\alpha-\alpha_0}{3-\alpha}\in(1,2),
$$

and the intrinsic second-moment homogeneity

$$
m=\frac{q}{\nu}=\frac{4-\alpha}{3-\alpha}.
$$

The covariance enters the independent upper bound only through

$$
R_\alpha = \frac{\alpha\,\pi\,\mu(B_1)}{2\sin(\pi\alpha/2)} ,
\qquad
\E[u(T,x)^2] \le e(T+2)^d
\exp\!\Big\{ C(\alpha,\alpha_0)\, R_\alpha^{1/\nu} T^{\kappa}\Big\}.
$$

The amplitude dependence of the intrinsic constant obtained from the
positive-control formula is

$$
C_2(b\Gamma,a)=b^{1/(3-\alpha)}C_2(\Gamma,a),
$$

obtained via the Radon pushforward factor $r^{\alpha-d}$ and the separate
Lebesgue factor $r^{-d}$; the two must not be conflated (white $d=\alpha=1$
keeps the Radon factor $1$ but retains the Lebesgue $r^{-1}$).

The kinetic coefficient in the intrinsic formula is $1$ and the Gaussian raw
action is exactly $v_\Psi/2$, **not** $v_\Psi$.

---

## 2. Owner-unit and declaration coverage

The canonical owner units (from `maps/canonical-owner-units.tsv`) are:

| Owner unit | OWN proofs | Main function |
|---|---|---|
| A | PROOF001–023, PROOF214 | fixed-order construction, mild/mixed/crude/envelope, White/Riesz/d1/low-$\alpha$/higher-$\alpha$ calibration, independent-origin covariance bridge |
| B | PROOF024–060 | endpoint/planar/three-transfer alternatives, static phase variance, interval upper, static continuation and clock obstruction |
| C | PROOF061–093 | masked covariance, wave variance, compact Gaussian, operator driver, source convergence, masked moments, constant-phase Young |
| D | PROOF094–110 | compact mean family, exact scaling, raw lower, unmasked variational, temporal/spatial occupation, Cameron mean |
| E | PROOF111–139 | compact ground family, raw block lower, full unmasked variational |
| F | PROOF140–169 | Cameron/Young/uniform mean/radius anchor, signed static, symplectic phase |
| G | PROOF170–193 | Gaussian tubes, uniform products, point transfer, signed upper |
| H | PROOF194–213 | positive Gram optimiser, intrinsic constant, occupation bounds, white evaluation |

The 240 declarations split as:

[held back until the source author has been told]

I do **not** reclassify any CONTEXT declaration as an OWN deduction. In
particular `H:three-endpoints` (`S066`) and `H:spatial-maximum` (`S065`) are
conditional/property-scope declarations, never part of `H:homog`.

The 13 canonical joins are:

1. `JOIN-CONSTRUCTOR`
2. `JOIN-INDEPENDENT-UPPER`
3. `JOIN-DRIVER-SOURCE`
4. `JOIN-F-YOUNG-OBSERVABLE`
5. `JOIN-RAW-SCALING-LOWER`
6. `JOIN-UNMASK-FINITENESS`
7. `JOIN-OCCUPATION-SPATIAL`
8. `JOIN-UNIFORM-E-SIGNED`
9. `JOIN-SYMPLECTIC-TUBE`
10. `JOIN-POINT-UPPER`
11. `JOIN-POSITIVE-INTRINSIC`
12. `JOIN-CALIBRATION-ALTERNATIVES`
13. `JOIN-DERIVED-BOUNDS-WHITE`

Each is assessed with its exact same-solution/order obligation below.

---

## 3. Reconstructed derivation chains (shared `WORK` sections)

### WORK-1. Fixed-order construction and bridge (A: PROOF001–010, 214)

The constructive spine is `WORK-1`:

1. `PROOF004` establishes the damped norms
   $$
   N_0(\theta)=\theta^{-2},\qquad
   N_1(\theta)=\theta^{\alpha+\alpha_0-2}N_1(1),\qquad
   N_2(\theta)^2=\theta^{-\beta}N_2(1)^2,
   $$
   with vanishing tails $N_1^{(M)}(1),N_2^{(M)}(1)\to 0$.

2. `PROOF214` proves the independent-origin covariance Cauchy–Schwarz
   $$
   0\le Q(T_{A,a}G_1^0,T_{B,b}G_2^0)\le N_C(G_1)N_C(G_2),
   $$
   with coefficient exactly $1$, retaining the $A-B$ predecessor offset. This
   is the bridge for the source Case 2 and does **not** use the source offset-free
   printed equality.

3. `PROOF005+006` construct the fixed-order spatial Wick measures and the joint
   diagram limits with arbitrary relative width rates and Green-before-noise in
   $d=3$, including unequal/empty chains.

4. `PROOF007+008` obtain corrected vertexwise and crude bounds with fixed-t
   summability
   $$
   \sum_{n\ge0}\sqrt{n+1}\,q_n(T)<\infty.
   $$

5. `PROOF009` confirms the canonical series is a mild solution with no
   uniqueness claim; `PROOF002` gives the nonnegative mixed expansion; `PROOF010`
   gives the numerical-majorant envelope with exponent
   $$
   \rho=\frac{\beta}{\beta-1}>\kappa.
   $$

`WORK-1` status: **reconstructed from source** for the fixed-order/Summability
clauses; `PROOF002`/`PROOF009` full parent derivations are **LIMITED** where
their boundary `INPUT_APPLICATION` declarations are consumed downstream.

---

### WORK-2. Independent full upper (B: PROOF036–051)

`WORK-2` is the actual all-scale upper, separate from the variational
identification.

**Phase/variance input (036–043).** `PROOF036` imports only the **quartic**
C23 finite variation (1.5) as seed and then proves the physical/spectral
energy identification by its own Schwartz/H¹ approximation. `PROOF037` keeps
the spectral mass $V=\mu(B_1)$ and physical mass $M=\Gamma(B_1)$ distinct, and
derives the resolvent constant $R_\alpha$ and the physical trace constant
$D_\Gamma$. `PROOF038` gives both the `Born` term
$$
\E\|Z_1(h)\|_\lambda^2\le R_\alpha h^2\lambda^{\alpha-2}
(1+\lambda^2h^2)^2N^2
$$
and the `mean` term
$$
\|\E Z_2(h)\|_\lambda\le
\frac{D_\Gamma(1+\lambda^2h^2)h^{3-\alpha}}{\lambda(2-\alpha)(3-\alpha)}N,
$$
so that first-variance bounds do **not** discard the velocity entry.

`PROOF039` is the bounded nonselfadjoint complex-phase bound
$\|\mathcal M_z(h)\|_{X_\lambda}\le100e^{2\lambda h}$ obtained from the
Crouzeix–Palencia numerical-range bound (introduced as a named import, not an
OWN theorem). The four ordered root comparisons follow from the resolvent
integral
$$
w^{-1/2}=\frac1\pi\int_0^\infty t^{-1/2}\frac{1}{w+t}\,dt.
$$
`PROOF040` gives the Fock sandwich with $d_N=2\sqrt{N+1}\sqrt{R_\alpha}$, both
creation and annihilation retained. `PROOF041` proves selected finite-word
exactness under per-colour degree cutoffs.

**Interval coefficients (044–048).** The dimension-independent resolvent
bound gives the column contraction
$$
\int\frac{\mu(d\xi)}{\rho^2+|\eta+\xi|^2}\le R_\alpha\rho^{\alpha-2}.
$$
The fixed total-order coefficient satisfies (`PROOF047+048`)
$$
\left|[s^{2k}]\E\|\mathcal U_{\mathcal F}^\epsilon(T;s)v\|_{1/T}^2\right|
\le \frac{C^k R_\alpha^k T^{\beta k}}{(k!)^\nu}\|v\|_{1/T}^2
$$
after the positive inventory product `PROOF046`. The final phase bound is
$$
\E\|\mathcal U_{\mathcal F}^\epsilon(T;1)v\|_{1/T}^2
\le e\exp\{C R_\alpha^{1/\nu}T^{\beta/\nu}\}\|v\|_{1/T}^2.
$$

**Terminal Wick and closure (049–051).** `PROOF049` gives the coefficient-one
terminal pairing formula with mass $T^{2n}/(2n)!$ and no spurious $n!$ or
$m!n!$ factor. `PROOF050` is a conditional tail lemma: given an independent
prelimit enlarged-amplitude bound
$$
B(T;r)=e(T+2)^d\exp\{C(r^2R_\alpha)^{1/\nu}T^{\kappa}\},\qquad r>1,
$$
and 006 fixed-order limits, geometric tails close the canonical series. The
prelimit $B_r$ is constructed **inside** `PROOF051` from $048+049$ and
localization, *before* the canonical closure. Then $006+050$ close the
amplitude $-1$ bound
$$
\E u^2(T,x)\le e(T+2)^d\exp\{C R_\alpha^{1/(3-\alpha)}T^{\kappa}\}.
$$

**Cycle check.** $051 \to 132$ finishes before $132$ obtains finiteness. The
shorthand $051\to050\to051$ is not a cycle once the intermediate prelimit
antecedent $B(T;r)$ is distinguished from the full canonical theorem.
`WORK-2` status: **reconstructed** for the displayed order; `PROOF051` full
parent remains **LIMITED** where its own inner named imports are only matched,
not reproved.

---

### WORK-3. Calibration alternatives and endpoint transfers (B: PROOF024–035, 052–060)

**Endpoint alternates (024–035).** `PROOF024+027` provide the static
coefficient input from the published Chen–Hu fixed-order/coefficient-rate
statements: for a homogeneous static covariance of degree $\chi$, the full
split-sum $B_k$ satisfies, after finite-order enlargement,

$$
0\le B_k(t)\le \frac{C_{\rm st}^k t^{(4-\chi)k}}{(k!)^{3-\chi}}.
$$

`PROOF026` constructs the planar low/static endpoints
$\Gamma_{\rm low}=|x|^{\alpha-1}\Gamma$ and
$\Gamma_{\rm st}=|x|^{\alpha-\chi}\Gamma$, proves PD of each, and the closing
bound
$$
(G_h*\Gamma_{\rm low})(z)\le S/4.
$$
`PROOF028` interpolates between the low temporal endpoint and the static
endpoint on one common diagram measure; the factorial and time powers combine
exactly as
$$
2\vartheta+(1-\vartheta)(3-\chi)=3-\alpha=:q,
\qquad
\vartheta(3-b_0)+(1-\vartheta)(4-\chi)=4-\alpha-\alpha_0=\beta.
$$
The resulting bound is
$$
\E u^2(t,x)\le\exp\{q C^{1/q}t^{\kappa}\}.
$$

`PROOF030` constructs strict ordinary-product endpoints; `PROOF031` constructs
plane-supported endpoints with $V_{\rm low}=c/\pi$; `PROOF032` closes under
invertible linear images and finite weighted sums; `PROOF033` gives the
conditional d3 transfer and the separate nonsharp asymptotic constant, keeping
$C_{\rm st}$ and the asymptotic rate distinct; `PROOF034+035` discharge
`H:three-endpoints` only for the stated families (ordinary products, Riesz,
plane families, finite sums of invertible images).

**Static continuation and clock (052–060).** `PROOF052` interpolates the raw
fractional mean coefficients,
$$
m_k(a)\le m_k(0)^{1-a/b}m_k(b)^{a/b},
$$
after the static endpoint is built independently. `PROOF053` is the internal
positive-series type identity
$$
\tau=\nu K^{1/\nu},\qquad
K=\limsup_k\big((k!)^\nu c_k\big)^{1/k}.
$$
`PROOF054` gives the exact static amplitude clock
$$
\E[U_\sigma(T)^p]=\E[U(\sigma^{2/(4-\alpha)}T)^p],\qquad p=1,2,
$$
which produces `static-minorant` rates
$$
\liminf_T T^{-\kappa(a)}\log\E[u^{(a)}(T)^p]\ge p^{\kappa_{\rm st}}L_0,
$$
where $\kappa_{\rm st}=(4-\alpha)/(3-\alpha)$. `PROOF055` gives the strict gap
in the window $(0,a_*)$; `PROOF056` extends the interpolation to the full
second moment coefficients; `PROOF057` proves log-convexity of the raw upper
growth types; `PROOF058` recovers the static constant iteratively only,
with no fixed-$a$ all-$p$ law and no $a\to0$ interchange.

`PROOF059` computes the white gap transforms
$$
K_\times(\theta_1,\theta_2)=\frac{\Gamma_{\rm E}(1-a)}
{2(\theta_1+\theta_2)^2}(\theta_1^{a-1}+\theta_2^{a-1}),
$$
and `PROOF060` proves the clock-copy obstruction
$$
J_{\Gamma,\rho}(\theta)\le J_{\Gamma,1}(\theta)
=\int_0^\infty \frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)\,d\lambda
<K_\Gamma(\theta),
$$
with degree-one loss $J_{\Gamma,1}/K_\Gamma=2-2^a$. This is a **narrow**
no-go for the literal unweighted constant-$\rho$ rectangular copy; it does not
rule out other clock couplings.

`WORK-3` status: **reconstructed** for the endpoint disjoint branches and the
clock calculus; `PROOF025/028/033/052/054/056/058` are **LIMITED** on stated
upstream consumers (006/002/017/018/036/049/051 and the published imports).

---

### WORK-4. Driver, source and Young construction (C, D, F)

The operator driver is constructed on the **given** noise $W$:

1. `PROOF063/064` complete temporal and noise completions. `PROOF065` shows a
   physical mask need not preserve raw null tests, so course masking cannot be
   asserted on the original quotient.

2. `PROOF069/071/073/074` give the normalized Fourier row and both variance
   directions:
   $$
   \sum_k\E|\ell_R(I;e_k,z)|^2\le C_T h^{2-a}B_\alpha(h)
   \|z\|_{E_{s-\gamma}}^2
   $$
   and the reflected output-family bound. The two directions are **not**
   interchangeable; the second uses evenness of $\nu_R$ to reflect.

3. `PROOF085–093` build the same-noise compact operator path
   $M_R\in L^p(C^\theta)$ with $\sqrt p$ Gaussian norms, all-time compactness
   on one path event, and its square-exponential norm bound.

4. `PROOF094–098` give the retaining source isometry and the exact joint source
   covariance
   $$
   \mathrm{Cov}(Y_{\epsilon,\eta}(t,x),Y_{\epsilon',\eta'}(s,y))
   =K_{\max(\eta,\eta')}(t-s)\Gamma_{\epsilon+\epsilon'}(x-y).
   $$
   `PROOF099/100` provide the positive-width pointfield regularity and the
   ordinary first response on $E$.

5. `PROOF104–109` extend the driver to $F=E\oplus\mathbb R^2$ with both
   constant-response columns, prove the linear Young evolution (local
   contraction, composition, inverse, subquadratic growth
   $\mathcal O((1+d)^\nu)$ with $\nu=1/\theta<2$), and identify the ordinary
   source solution with the constant data. The physical flow is **strongly**
   continuous, not norm-continuous; $iE$ is closed and proper, so density of
   $E$ in $F$ is not used.

`WORK-4` status: **reconstructed** for the structural driver/Young clauses;
several compactness/UI statements are **LIMITED** at their own fixed-parameter
sources.

---

### WORK-5. Raw lower, Cameron space and Gaussian tubes (D, E, F, G)

**Cameron/rayleigh space.** `PROOF170` proves the genuine abstract-Wiener
realization on the actual first chaos, with Cameron norm
$\|Ch\|_{\rm CM}=\|P_{\rm seen}h\|$. `PROOF171` proves closed Borel tubes and
least-radius attainment. `PROOF172` is the Rayleigh transfer
$$
\E[e^{F(X)/\delta}]\le\int_0^\infty\frac{r}{\delta}
\exp\!\Big\{\frac{G(r)-r^2/2}{\delta}\Big\}\,dr.
$$
The half-action `$r^2/2$` is the **single global raw action**; no separate
independent-block costs are added.

**Actual block mean.** The completed $E$ mean is
$\mathcal T_R=T_R(C_t\otimes I)$ with bound $C_{\rm mean}$ uniform in $R$.
`PROOF169` keeps the exact fast mean covariance scale
$\sqrt\delta H_m$; compactness alone does not prove the scale.

**Uniform radius bounds.** `PROOF156–160` give the radius-explicit Schatten
envelope $\|K_{\rm out}\|_{S_Q}\le C_Q\rho^{d/Q}$; `PROOF158` gives the radius
path moment norm $C\sqrt p\,R^{d/Q}$; `PROOF160` gives the decay at
$R_\delta=\delta^{-1}+2$ with exponent $(1-a)/2-d/Q>0$.

**Compact free/Young floor.** `PROOF165` proves the translation-commuting
compact perturbation norm floor
$$
\|S_E(t)+K\|\ge\|S_E(t)\|,\qquad \|S_E(t)\|\ge1,
$$
using whole-space translations, weak-null vectors and the isometric velocity
reversal. `PROOF168` is the real J-skew raw conservation; invertibility is
from `PROOF107`'s Neumann pieces, not from conservation in infinite dimension.

`WORK-5` status: **reconstructed** for the displayed norms; the full stochastic
convergence chains remain **LIMITED** as marked.

---

### WORK-6. Symplectic, point transfer and signed upper (G: PROOF170–193)

**Symplectic and tube (165–177).** The real isometric skew $J_E$ is preserved
by the free group and by the physical force pairing. Source ordinary flows
conserve $J_E$ at positive widths (`PROOF167`). The raw path closure and
Young remainder give the raw conservation at fixed parameters (`PROOF168`).
`PROOF173–177` assemble the actual tube law, global endpoint identity, coarse
envelope, exact Rayleigh tail, and half-action supremum.

**Point transfer (185–189).** The operative facts are:

1. At fixed $\delta$, the actual $E$ endpoint $P_\delta$ is the closed
   isometric restriction of its $F$ extension, with
   $1\le \E\|P_\delta\|^2<\infty$.

2. The fast source has covariance
   $\delta^aK_\tau(\delta v)=K_{\tau/\delta}(v)$ against
   $\Gamma_\delta=g^2\Gamma$, with $g=\delta^{(1-a)/2}$; no second $g$ or mask.

3. The TOTAL initial difference $(\psi-1,0)$ cancels on the pure cone
   $\mathcal C=\{(t,x):|x|\le1+L-t\}$ by full finite propagation; separately
   testing the $E$ and constant parts would miss the cancellation.

4. On the cone the compact-data displacement equals the unmasked flat-data
   solution with the same realized coefficient (factorial Green recursion
   $HM^nt^{2n}/(2n)!$).

5. This gives an **integral of squares** identity
   $$
   \E\|\mathrm{pr}_1P_\delta(L,0)z\|_{L^2(D)}^2
   =v_d\,\E|u_{\Gamma_\delta}(L,0)|^2,
   $$
   not a squared average and not a masked-stationarity substitution.

6. The two fixed-$\delta$ moment limits (flow displacement on the left,
   canonical point moment on the right) are taken **before** canonical-law
   scaling. Only then
   $$
   \E|u_\Gamma(T_\delta,0)|^2=\E|u_{\Gamma_\delta}(L,0)|^2.
   $$
   The data cost is polynomial $C_\eta R^d$ with
   $\delta\log\mathrm{DataPref}_\delta\to0$.

**Signed upper (190–193).** The raw signed score
$$
\mathcal S_R=\sup_{\Phi\in H_I}\{2\mathrm{Rate}_R(\Phi)-\|\Phi\|_{H_I}^2/2\}
$$
has the finite ceiling $2+2C_{\rm mean}^2$. The radial half-action bulk/tail
split gives
$$
M_\delta\le\frac{M^2}{2\delta}e^{(\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M})/\delta}
+4e^{(A_0+\eta_B b_{\delta,B}^\nu-M^2/4)/\delta},
$$
with the exact tail constant $4$ and exponent $-M^2/4$. The two-limit order
is: $\delta\to0$ at fixed $B$, then $B\to\infty$ on the **same** endpoint
$P_\delta$. This uses only the limsup $V_{\rm up}$, **not** the $203$
all-$R$ score convergence.

`WORK-6` status: **reconstructed** for the reduction structure; `PROOF186/188/189`
boundary consumers (095/102/103) are **LIMITED** as input applications.

---

### WORK-7. Positive Gram, intrinsic constant, occupation, white (H: PROOF194–213)

**Finite Gram (194–198).** The finite objective
$$
\mathfrak F_C(\Phi)=2\!\sum_i\ell_i\sqrt{(\langle\Phi,k_i\rangle-b_i)_+}
-\|\Phi\|^2/2
$$
is solved exactly via the active-subset dual:
$$
\mathcal S(C)=\max_{A\subset\mathcal J}d_A^C,\qquad
d_\emptyset^C=0,
$$
with a positive-conic optimizer or zero. `PROOF195` uses the diagonal gradient
term to obtain strict Hessian positivity even for singular Grams; `PROOF198` is
the **entrywise optimized-value** comparison, with no PSD order on $D-C$.

**Intrinsic constant (199–204).** `PROOF199` embeds positive controls in the
original raw space with
$$
\|\Psi\|_{H_I}^2=v_\Psi,\qquad
\mathcal T_R\Psi(s)=B_E(m_R h_{\Psi,s}),
$$
one physical mask after covariance convolution. `PROOF200` gives the label row
with $h_i=1_{I_i}/\ell_i$. `PROOF201` proves the uniform optimizer budget
$$
M=4C_{\rm mean}+4
$$
before time averaging. `PROOF202` proves the signed ceiling
$$
\mathcal S_R\le S_2^{\rm pos},
$$
with error $4e_n+2\varepsilon$, using only optimized Gram values. `PROOF203`
proves the cutoff removal
$$
\lim_{R\to\infty}\mathcal S_R=S_2^{\rm pos}
$$
with a fixed near-optimal positive test and a **possibly nonmonotone** mask
family. `PROOF204` matches upper and lower for the same canonical solution,
giving

$$
C_2(\Gamma,a)
=\sup_{\Psi\in C_{\rm pos}}
\Big\{2\int_I\sqrt{
\sup_{\substack{f\in H^1(\mathbb R^d;\mathbb R)\\\|f\|_2=1}}
\Big(\int h_{\Psi,s}f^2-\|\nabla f\|_2^2\Big)}\,ds
-\frac{v_\Psi}{2}\Big\},
$$

with
$$
h_{\Psi,s}(x)=\int_I|s-t|^{-a}(\Gamma*\Psi_t)(x)\,dt,\qquad
v_\Psi=\int \Psi\,h_{\Psi}.
$$

The positive scores satisfy
$$
S_c^{\rm pos}=c^{(4-\alpha)/(3-\alpha)}S_1^{\rm pos},\qquad
Q_2\ge S_2^{\rm pos},
$$
and the final identification is
$$
C_2=S_2^{\rm pos}=2^{(4-\alpha)/(3-\alpha)}S_1^{\rm pos}.
$$
$S_1^{\rm pos}$ remains auxiliary: it is **not** an actual first-moment constant
or a Chen printed constant.

**Occupation and white (205–213).** The common spatial energy
$\mathcal E_{\rm sp}$ bounds the occupation ceiling, and the white evaluation
$\mathcal E_{\rm sp}=c^2/6$ for $\Gamma=c\delta_0$ gives the explicit bracket
$$
\frac23\sqrt{\frac{c}{M_a}}\le C_2(c,a)\le\frac23\sqrt{cK_0(a)}.
$$

`WORK-7` status: **reconstructed** for the analytic identity; `PROOF200–202`
consumer clauses are **LIMITED** at their stated source inputs.

---

## 4. Join-by-join coupled judgments

| Join | Status | Core check and open remainder |
|---|---|---|
| `CONSTRUCTOR` | reconstructed | Fixed-order norm/measure chain is acyclic; empty/unequal chains and independent roots retained. `002/009` parents LIMITED. |
| `INDEPENDENT-UPPER` | reconstructed | Prelimit $B_r$ precedes canonical $050$; no intrinsic/002/007/008 premise in the tail. $051$ parent LIMITED. |
| `DRIVER-SOURCE` | reconstructed | Same-W interval/operator limit, correlated retaining sources, arbitary relative widths at fixed $R,T$. $091–098$ parents LIMITED. |
| `F-YOUNG-OBSERVABLE` | reconstructed | Both constant columns; $iE$ closed proper; physical flow strongly continuous; no H¹ᐟ² point trace. |
| `RAW-SCALING-LOWER` | reconstructed | Same-$W$ blocks, exact Gaussian law change, half-action $v/2$; source limits precede $\delta$. |
| `UNMASK-FINITENESS` | reconstructed | Independent 051 upper supplies score finiteness; 202/204 are not finiteness antecedents. |
| `OCCUPATION-SPATIAL` | reconstructed | Lebesgue $x$ first handles singular $\Gamma$; rough H¹ extension after smooth ratio. |
| `UNIFORM-E-SIGNED` | reconstructed | Lift/$\chi_R$ constants identify only; uniform budgets use $E$ norms. |
| `SYMPLECTIC-TUBE` | reconstructed | Real J-skew closure and compact Young floor; compactness does not give conservation/scales. |
| `POINT-UPPER` | reconstructed | Two fixed-$\delta$ moment limits before canonical scaling; signed upper via radial half-action. |
| `POSITIVE-INTRINSIC` | reconstructed | Entrywise Gram comparison, uniform budget before averaging, fixed-test cutoff; same-canonical upper/lower. |
| `CALIBRATION-ALTERNATIVES` | LIMITED | 27-domain/45-sector/Riesz/endpoint routes coherent; unresolved 002/006/017/018/036/049–051 parents concentrated in transfers. |
| `DERIVED-BOUNDS-WHITE` | reconstructed | Derived bounds are bounds on $C_2$, not evaluations; zero cases direct. |

---

## 5. Primary applications and model/constant/cycle audits

### 5.1 Primary applications

- **AUTHOR** (`BOOK.chen-author-full`): hypothesis/regularization conventions and (6.3) matched; the printed first-moment normalization is quoted, not adopted; Section 5(ii), (5.3)–(5.4), 4.1/L4.4 are not imported.
- **CHEN-HU**: Theorem 3.8(i), (5.1)/(5.15) used for static fixed-order and coefficient-rate; Theorem 1.2/(1.9) raw-$p$ normalization retained.
- **CHEN2023**: the **quartic** (1.5) seed is imported in `PROOF036`; the square-root (1.4) is *not* silently substituted. Both finiteness statements exist; the quantitative values differ and are not identified.
- **BALAN–CONUS**: `COMPARISON_ONLY`; no Skorohod solution/constant imported.
- **CROUZEIX–PALENCIA**: bounded numerical-range spectral set, $1+\sqrt2$, matched; unbounded extension not used.
- **TESCHL**: closed forms, spectral calculus, max-min, ground-state simplicity, matched for compact smooth potentials and imports only; the $H^2$-domain item is **not** invoked for rough multipliers.
- **FRIZ–HAIRER**: bounded-bilinear Young estimate and Théorème 11.6 set enlargement matched after OWN AWS/Borel checks.

### 5.2 Model/constant audit

- **Original model** preserved in every block. No new model or data assumption is introduced.
- **Endpoint hypotheses** `H:three-endpoints`/`H:spatial-maximum` remain conditional/property-scope, never all-Gamma.
- **Static normalization** is raw-$p$ moments; no L²-norm/raw misread is adopted.
- **Clock and constant scope** is the literal two-clock copy family; `S1pos` is auxiliary.

### 5.3 Cycles

- **$051\to132\to202$**: $051$'s prelimit $B_r$ precedes $006+050$ and the canonical bound; $132$ finiteness is upstream of $202$. No cycle.
- **$193\to203\to204$**: $193$ supplies only a limsup; $203$ proves the all-$R$ limit afterwards; $204$ composes them. No diagonal $R(\delta)$ selection is assumed.

---

## 6. Counterexamples and retained falsifications

1. **Numerical-majorant no-go.** For the envelope,
   $$
   T_2(t)=\frac{15}{2}D^2t^{2\beta}(2!)^{-\beta+1},\quad
   T_3(t)=\frac{35}{2}D^3t^{3\beta}(3!)^{-(\beta-1)},
   $$
   with exact exponent $\rho=\beta/(\beta-1)>\kappa$. The lower bound is for
   the **majorant**, not the moment.

2. **White order-two self-pairings.** For $d=\alpha=1$, white covariance,
   $\E X_1^2=c_0t^{3-\alpha_0}$ and $\E X_2=\tfrac12c_0t^{3-\alpha_0}$, total
   order-two $2c_0t^{3-\alpha_0}$. Dropping empty/self-pairs is false.

3. **Clock-copy obstruction.** Shared normalized clock gives
   $J_1/K=(2-2^a)$ at degree one, strictly between $0$ and $1$; at the static
   endpoint the kernel is defined directly as $1$, so static checks alone miss
   the obstruction.

4. **Ordered-temporal symmetry normalization.** The pairing/split temporal
   factor is $2^k/k!$, not the raw diagram count and not $1$:
   $$
   P_k\sum_{m=0}^{2k}\frac1{m!(2k-m)!}=\frac{2^k}{k!}
   \quad(2,\ 2,\ 4/3 \text{ at } k=1,2,3).
   $$

5. **$H^2$ vs $H^{3/2}$.** For the rough multiplier $V=\chi|x|^{-3/4}$ in d1
   white, $u=\psi[1-(16/5)|x|^{5/4}]$ lies in $D(H_V)$ but not $H^2$; the
   operator domain is only graph-continuously embedded in $H^{3/2}$. No source
   repair is needed, but any returned claim of graph norms equivalent to
   $H^2\times H^1$ is false.

6. **F-lift vs E multiplier norm.** The sufficient F bound
   $16(1+K_F)^4(1+t)^3e^{\lambda t}$ uses $K_F$; the E bound
   $8(1+K_E)^2(1+t)e^{\lambda t}$ uses the actual multiplier norm. There is no
   $R$-uniform F bound from $K_E$ alone.

---

## 7. Explicit remaining work and limitations

1. Full independent re-derivation of all
   `INPUT_APPLICATION` boundary parents (002/005/006/008/017/018/036/049/050/051,
   180–184, 210–213 where consumed) is not performed in this pass; each such
   consumer is marked `LIMITED` and the remaining-full-parent condition is
   explicitly retained.

2. Source/text provenance is not pixel certification. The rendered paper, PDF
   image layer, Kimi/source inventory, and full visual audit are not concluded
   here.

3. A separate fresh cold read of the paper with bibliography only is
   expressly required and not substituted by this report.

4. The intrinsic constant is identified as a fully specified variational value,
   but it is **not** numerically evaluated and **not** identified with Chen's
   guessed constants or with the actual first-moment constant.

5. The whole `HIGH` acceptance, image credit, and source-glyph credit are
   ungraded and remain open.

---

## Overall verdict and confidence

The signature mathematical objects — fixed-order construction, independent
upper, endpoint transfers, operator/source driver with Young conservation,
Gaussian Cameron tubes, point transfer, and positive-control intrinsic
matching — are internally coherent and faithful to the supplied source. The
main constants and exponents recompute correctly where I checked them, and the
acyclicity of the central finiteness chains holds once prelimit antecedents are
distinguished from conclusions.

However, many `LIMITED` consumers remain, several scalar controls in the prior
evidence contain arithmetic/attribution defects that require the exact
calculations rather than generic consistency captions, and the full whole-scope
reconstruction of every one of the 214 OWN proofs with every one of the 240
declarations at `CHECKED` has not been completed in this single response.
Accordingly the whole-program status must remain open rather than passed.

---

### Final assessment

- **Global verdict:** `INCONCLUSIVE`.
- **Confidence on the core chains (fixed-order, independent upper, intrinsic formula, clock no-go):** `medium`.
- **Confidence on complete whole-214/240/13 closure:** `low`.
- No pass label, no forced `HIGH`, and no mathematical claim is accepted on the basis of source availability, a hash, a label repetition, or a prior vote.