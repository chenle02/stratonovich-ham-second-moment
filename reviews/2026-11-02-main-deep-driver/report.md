# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

None requiring rejection. Across PROOF085–093 I reconstructed the chain of estimates and found no false identity, wrong sign, incorrect final coefficient, or invalid limit passage. The two genuinely load-bearing steps that are sketched rather than fully expanded in the text are:

1. DRV03/DRV087 (finite propagation with both phase entries) relies on the classical energy-boundary-flux argument for the free wave equation; the manuscript states the key inequality $v\partial_n u - (v^2+|\nabla u|^2)/2 \le 0$ but does not reprove the support theorem in detail.
2. DRV08/DRV092 uses the dyadic-to-Hölder norm equivalence for $C^\eta$ (weighted dyadic increments control the Hölder norm) without a full $\varepsilon$-proof. I reconstructed it and it is correct.

Both are standard, in-project admissible, and do not falsify the proofs; they are noncritical residuals rather than gaps. The review is bounded to the embedded excerpt of `driver-consumer.tex` plus its stated upstream interfaces (`P:wave-two-variances`, `P:wave-square-columns`, `P:localized-finite-variance`, `C:finite-gaussian-operators`, `P:compact-two-envelopes`, `L:compact-positive-order`); those upstream interfaces were checked for consistent use but not fully re-derived here.

## Noncritical findings

1. **DRV01/085 spatial positivity constant** uses $q\ge 1$ on $B_{2L+1}$; the lower bound $Q_{\mathrm{sp}}\ge |B_{L+1}|\Gamma(B_L)$ is correct, but the text implicitly invokes that a nonzero positive Radon measure has positive mass on some ball. Standard and fine.
2. **DRV02/086 class-independence** proves the null-class statement only for $t>0$ from testing and then extends to $t=0$ by continuity of $H_{j,R}$ in $t$; the continuity near $t=0$ is valid because $|u|^{-a}$ is locally integrable and $f_j$ is time-compact. Correct, but worth an explicit sentence in the manuscript.
3. **DRV03/087 adjoint index bookkeeping** ($E_{2s-r-1}\to E_{2s-r}$, $s=1/2$) is correct; I verified the duals: $H^r$ dual w.r.t. $H^{1/2}$ is $H^{1-r}$, $H^{r-1}$ dual w.r.t. $H^{-1/2}$ is $H^{-r}$, so $(E_r)^*=E_{1-r}$.
4. **DRV04/088 and DRV07/091** depend on the $\beta$-versions of `P:wave-two-variances`; the statement that $C_T$ is independent of $R$ is used (via $C_\nu=c_d^2L_\zeta^2C_\Gamma$), and it is consistent with the wave section.
5. **DRV08/092** the coarse-level handling "finitely many coarse levels controlled by unit partitions" is asserted without detail; it is valid because only $L^p$-norm growth matters there, and the fine-level geometric ratio $2^{-(\beta-\eta-1/q_0)}<1$ is what closes the sum.
6. **DRV09/093** the "long interval Schatten" sentence in the proposition is mildly compressed: the displayed formula is for short intervals $h\le1$, and long intervals are obtained by additivity with endpoint nullity, not by plugging long $h$ into the formula. No false long-$h$ bound is asserted.
7. No counterexample survived the manual tests in DRV10 (zero covariance, scaling limits, $p/q$ powers, the $\alpha=1$ critical logarithm, Schatten-monotonicity for large $q$). See DRV10 below.

## Checked derivations

All line references are the original `integrated_actual_operator_driver.tex` LF numbers (carried verbatim in the packet).

**DRV01 — PROOF085 `L:driver-noise-basis` (59–63 / 65–121).** Reconstructed fully.
- `E:driver-test-continuity`: spatial factor $|K|\Gamma(K-K)$ is correct (only differences in $K-K$ contribute), temporal Schur factor $2L^{1-a}/(1-a)$ matches `L:masked-time-completion`. Countable rational supported dense collection gives separability without injectivity.
- Positivity: for $x\in B_{L+1}$, $y\in B_L$ one has $|x-y|\le 2L+1$, so $Q_{\mathrm{sp}}\ge|B_{L+1}|\Gamma(B_L)>0$; finiteness from $\Gamma(B_{4L+2})<\infty$. Checked.
- Temporal strict positivity via Laplace factorization $|t-s|^{-a}=\Gamma_E(a)^{-1}\int_0^\infty\lambda^{a-1}e^{-\lambda|t-s|}\,d\lambda$ and $e^{-\lambda|t-s|}=\int_{-\infty}^{\min(t,s)}2\lambda e^{-\lambda(t-u)}e^{-\lambda(s-u)}\,du$. Then $E_\lambda(\tau)=\int 2\lambda|\int_r^\infty e^{-\lambda(t-r)}\tau(t)dt|^2dr\ge0$; $v'=\lambda v-\tau$ forces $\tau=0$; infinite dimension follows. Checked.
- Gram-Schmidt in the null quotient and isonormal independence via characteristic functions. Checked.

**DRV02 — PROOF086 `L:driver-covariance-coefficients` (123–138 / 140–165).** Reconstructed fully.
- Smoothness/compact support: local integrability of $|v|^{-a}$ and local Radon mass of $\Gamma$ justify all derivatives moving onto $f_j$; support in $B_{2R}$ from $\zeta_R$. Checked.
- `E:driver-literal-covariance` from absolute Fubini, correct signs, no extra Fourier factor. Representative-independence reduces to $\zeta_R(x)\psi(t,x)=0$ distributionally for $t>0$, extended to $t=0$ by continuity. Checked.

**DRV03 — PROOF087 `L:driver-gain-localization` (169–190 / 192–237).** Reconstructed fully.
- $B(H_{j,R}(t)):E_r\to E_{r+1}$ (second slot multiplies the $H^r$ displacement by a compact-smooth multiplier), so `E:driver-gain-one` holds with constant $\le C_{j,r,R,T}|I|$; statewise Bochner integral, no operator-norm continuity of $S(t)$. Checked.
- Dual gain $E_{2s-r-1}\to E_{2s-r}$; with $s=1/2$, $(E_r)^*=E_{1-r}$, so the adjoint maps $E_{-r}\to E_{1-r}$, matching the claimed indices. Both send $E_{s-\gamma}\to E$ since $\gamma<1$. Checked.
- Localization: $\chi=1$ on $B_{2R+T+1}$, input $(1-D_\chi)z$ vanishes on $B_{2R+T+1}$, finite propagation (boundary flux inequality) makes the displacement vanish on $B_{2R}$ during $[0,T]$; output supported in $B_{2R+T}$; both identities $D_\chi A_j=A_j=A_jD_\chi$ follow. Checked (classical support theorem taken as admitted PDE fact).
- `E:driver-covariance-row` equals the physical Sobolev identity from `E:variance-physical-adjoint`; mask-after-convolution note is correct.

**DRV04 — PROOF088 `L:driver-actual-variances` (255–274 / 276–340).** Reconstructed fully.
- Projection identity $\sum_j|\langle A_j z,w\rangle_E|^2\le\mathbb E|\ell_R(I;z,w)|^2$ is correct (orthogonal projection onto the span of $g_1,\dots,g_N$).
- Output direction uses `E:wave-input-variance` ($e_k$ as varying input, $w$ fixed), input direction uses `E:wave-output-variance` ($z$ fixed, $e_k$ varying); the two directions are genuinely distinct and give $\sum_j\|A_j^{*,E}w\|^2\le b_I\|w\|^2_{E_{s-\gamma}}$ and $\sum_j\|A_j z\|^2\le b_I\|z\|^2_{E_{s-\gamma}}$. Transport by $J_0$ yields exactly $V_{\mathrm{out}},V_{\mathrm{in}}\le b_I D_\gamma^2$. Checked.
- Localization $P_\chi a_j=a_j=a_jP_\chi$; limits by polarization/Riesz; tails converge strongly; envelopes $T_{\mathrm{out},N}\le b_IB_{\mathrm{out}}$, $T_{\mathrm{in},N}\le b_IB_{\mathrm{in}}$ via positive congruence on localized tails. Checked.
- Column expansions $m_{R,I}(z)=\sum_j g_jA_jz$, $n_{R,I}(z)=\sum_j g_jA_j^{*,E}z$ follow from literal first-chaos membership and Parseval; complexification constants/multiplicities preserved. Checked.

**DRV05 — PROOF089 `L:driver-dominated-tails` (342–348 / 350–367).** Reconstructed fully.
- Spectral projection split and positive quadratic Cauchy–Schwarz give $\langle T_Nx,x\rangle\le 2\|QT_NQ\|+2\varepsilon$; weak convergence kills the finite block; norm convergence follows. Eigenvalue domination $\lambda_j(T_N)\le\lambda_j(B)$ plus dominated summation gives $\operatorname{Tr}T_N^m\to0$. No false $T_N^m\le B^m$ used. Checked.

**DRV06 — PROOF090 `L:driver-gaussian-tail-average` (369–378 / 380–395).** Reconstructed fully.
- Compression variance deficit $\sum_\ell Q_kZ_\ell(1-Q_k)Z_\ell^*Q_k\ge0$; `P:finite-gaussian-matrix` applied on the finite range; singular-value Lipschitz + Fatou. Result exactly $(q-1)^{q/2}(\operatorname{Tr}V_{\mathrm{out}}^{q/2}+\operatorname{Tr}V_{\mathrm{in}}^{q/2})/2$, no factor $2$ error. Checked.

**DRV07 — PROOF091 `L:driver-interval-limit` (399–410 / 412–459).** Reconstructed fully.
- All hypotheses for `P:localized-finite-variance` and `C:finite-gaussian-operators` are proved in DRV03–04. Uniform finite bound $\sqrt{q-1}\sqrt{C_T}h^{1-a/2}B_\alpha(h)^{1/2}\|K_\chi\|_{S_q}$ is correct (from $C=b_I$ and $\sqrt{b_I}=\sqrt{C_T}h^{1-a/2}B^{1/2}$).
- Cauchy uses vanishing tail traces, not mere boundedness; $L^q$ Cauchy for one even $q$ gives all operator-norm $L^p$, $p\ge1$, by $L^q\ge L^p$. Separable closed span, a.s. subsequence, compactness, joint Gaussianity, raw row identity, and long-interval additivity via zero-norm endpoints all verified.

**DRV08 — PROOF092 `L:driver-holder-limit` (463–470 / 472–553).** Reconstructed fully.
- Schatten monotonicity $\|K_\chi\|_{S_q}\le\|K_\chi\|_{S_{q_0}}$ for $q\ge q_0$ by normalization. Increment moments $C\sqrt q|t-u|^{\beta}$ for $|t-u|\le1$ from the $\beta$-version of `P:wave-two-variances`. The dyadic maximum bound $2^{n/q}C\sqrt q(T2^{-n})^{\beta}$ needs no independence. Geometric sum ratio exactly $2^{-(\beta-\eta-1/q_0)}<1$, giving the $\sqrt q$ bound.
- Dyadic-to-$C^\eta$ control, sup-norm control from $F(0)=0$, interpolation `E:driver-holder-interpolation`, and scalar Hölder in probability all verify; limits land in the separable closed span of countably many Lipschitz paths; compact values at all times on one path set. Checked.

**DRV09 — PROOF093 `P:actual-operator-driver` (27–55 / 555–591).** Reconstructed fully.
- Path/interval equality by uniqueness in probability; raw row identity and long-interval interpretation; increment additivity gives the Schatten bound at admissible even indices. Joint Gaussianity of finite linear functionals. Basis indistinguishability through a countable dense Schwartz-phase set and rational times, extended by boundedness + path continuity; no uncountable common event assumed.
- Moment bound: for $p\ge1$ choose even $q\ge\max(p,q_0)$ with $q\le p+q_0+2\le(q_0+3)p$, so $(\mathbb E Y^p)^{1/p}\le C\sqrt q\le C\sqrt{(q_0+3)p}$; hence $C\sqrt p$.
- Exponential: $\mathbb E Y^{2m}\le(C_1\sqrt{2m})^{2m}$; $m!\ge(m/e)^m$ gives $m$-th term $\le(2ecC_1^2)^m$; $c<1/(2eC_1^2)$ makes the geometric series converge; the $C_1=0$ case is handled. All signs/counts correct. The $\sqrt p$ here is for $\mathcal B(E)$ only.

I also verified the DRV10 and DRV11 items listed below.

## Required fixes before production gate

No blocking fixes are required. Recommended nonblocking clarifications:

1. In **DRV03/087**, add one sentence citing the classical finite-propagation/energy identity for the full (both-entry) wave group, so the localization is not left to the sketch.
2. In **DRV08/092**, state the dyadic–Hölder norm equivalence explicitly as a lemma or give the telescoping argument in the text.
3. In **DRV09/093**, make the long-interval Schatten statement explicit: the displayed bound holds for short $h\le1$ intervals and is extended to long intervals only by finite additive partition with zero-norm endpoints.
4. Optional: in **DRV02/086**, spell out the continuity of $H_{j,R}$ at $t=0$ that carries the null-class statement from $t>0$ to $t\ge0$.

These are clarity edits, not correctness amendments. No constant, sign, or limit in the nine proofs needs correction.

## One-line summary

All nine actual Gaussian-driver proofs (PROOF085–093, including the deferred PROOF093 at statements 27–55 and proof 555–591) reconstruct with correct signs, boundary terms, constants, both variance directions, and fixed-$R,T$ limit passages; no critical gap found, with two classical implicit premises (wave finite propagation and dyadic–Hölder equivalence) to make explicit.

## 11 required checks (DRV01–DRV11)

| Check | Target | Status | Proof-level coverage |
|---|---|---|---|
| DRV01 | PROOF085 `L:driver-noise-basis` | PASS | FULL: separability, positivity, infinite dimension, Gram-Schmidt, Gaussian independence all verified |
| DRV02 | PROOF086 `L:driver-covariance-coefficients` | PASS | FULL: smoothness, Fubini covariance, null-class independence, mask-after-convolution verified |
| DRV03 | PROOF087 `L:driver-gain-localization` | PASS | FULL: one-derivative gain, adjoint indices, both-cutoff localization verified; finite propagation taken as classical PDE input |
| DRV04 | PROOF088 `L:driver-actual-variances` | PASS | FULL: both variance sums, first-chaos expansions, limits, tails, envelopes, complexification verified |
| DRV05 | PROOF089 `L:driver-dominated-tails` | PASS | FULL: weak-to-norm and dominated scalar summation verified |
| DRV06 | PROOF090 `L:driver-gaussian-tail-average` | PASS | FULL: compression + finite matrix bound + Fatou; exact average, no factor-2 error |
| DRV07 | PROOF091 `L:driver-interval-limit` | PASS | FULL: hypotheses pre-verified, Cauchy via vanishing tail traces, Schatten constant, additivity verified |
| DRV08 | PROOF092 `L:driver-holder-limit` | PASS | FULL: Schatten monotonicity, dyadic maximum, interpolation, separability, $C\sqrt q$ verified; dyadic–Hölder equivalence reconstructed |
| DRV09 | PROOF093 `P:actual-operator-driver` | PASS | FULL: path/interval equality, row identity, two-basis indistinguishability, $C\sqrt p$ and square-exponential tail verified |
| DRV10 | Manual falsification and downstream fit | PASS | Tested manually: $\Gamma=0$ triviality; noise-amplitude scaling; $p=2$ root of $h^{2-a}B_\alpha(h)$; large-$q$ $\sqrt{q-1}$; $\alpha<1,=1,>1$ cases with the critical logarithm absorbed via strict $\beta$ windows; Schatten endpoint excluded only where $q\gamma>d$ is required; both variance directions exercised by the row/column constructions; no $C^\theta S_q$-path claim |
| DRV11 | Completeness/non-circularity/scope | PASS | All nine proofs are non-circular; needed noise-as-linear-functional and compact-positive-order inputs are explicit; no bare Gaussianity-to-first-chaos jump, no $H_W$-valued Gaussian vector, no operator-norm continuity of $S(t)$, no uniform-in-$R$ path norm, no nonlinear Young flow/source/asymptotic overclaim in this section. Classical wave finite propagation and the dyadic–Hölder characterization are the only implicit premises; they are standard and were reconstructed, not assumed silently |

Confidence is MEDIUM (not HIGH) because the upstream wave/covariance/compact interfaces were checked for consistent use but not re-derived from scratch in this bounded unit, and two classical analytic facts are invoked inside DRV03/DRV08.