# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. All five target proofs (PROOF156–160) contain valid, load-bearing steps. I found no false identities, no sign errors in the cancellations that matter, no wrong constants, and no invalid asymptotics in the stated scopes. The three claimed strengths (uniform outer maps; polynomial Schatten/radius growth at fixed Q; fixed-parameter expected-norm decay) are correctly separated from the explicitly disclaimed F-column/concentration/nonlinear/point-transfer conclusions.

## Noncritical findings

1. **PROOF156 (constant bookkeeping, terse).** The "no additional $(2\pi)^{-d/2}$" claim depends on the unitary Fourier convention $c_d=(2\pi)^{-d/2}$ with $\widehat{fg}=c_d\,\hat f*\hat g$. Reconstructed by hand it is correct for both the periodization kernel and the recovery kernel; it is stated tersely but validly.
2. **PROOF158 (monotonicity needs "unnormalized").** The step $\|K_{\rm out}\|_{S_q}\le\|K_{\rm out}\|_{S_Q}$ for $q\ge Q$ is correct only because the Schatten norms are unnormalized (the proof says so explicitly). This is the key "fixed-Q before varying q" step and is sound; worth flagging only because it silently fails under normalization conventions.
3. **PROOF158 (arbitrary v).** Line 274–275, "choose an even $q\ge\max(v,Q)$ with $q\le v+Q+2\le(Q+3)v$": valid because the gap to the next even integer is at most 2 and $(Q+3)v-(v+Q+2)=(Q+2)(v-1)\ge0$ for $v\ge1$. Correct but could be spelled out.
4. **PROOF160 (redundant factor 2).** The displayed "$2E Z_\delta\le2(2/B)^{1/p}\dots$" carries a redundant factor 2 on both sides; harmless and derived correctly.
5. **Notation collision (cosmetic).** The root profile $\eta$ (a function) and the Hölder exponent $\eta_t$ (a number) coexist; they are consistently distinguished by the subscript, and no step conflates them.
6. **Dependence on cited modules.** PROOF158's $R$-uniform variance budget rests on the $R$-uniformity of the auxiliary-measure growth (covariance.tex) and the scalar row bound (wave-consumer.tex); both were verified in the embedded context, not re-derived in the target excerpts. This is normal lemma usage, not a gap, but it is the single load-point where an error elsewhere would propagate.

## Checked derivations

### PROOF156 — `L:radius-outer-maps` (uniform rescaled outer maps) — CHECKED

**Hypotheses.** Real $r$; $\chi_0\in C_c^\infty$, $=1$ on $B_1$, supported in $\overline B_2$; $\psi_0\in C_c^\infty$, $=1$ on a neighborhood of $\mathrm{supp}\,\chi_0$, supported inside $B_3$; $\rho\ge1$, $L=2\pi\rho$, torus $L^2(Q_L)$ with modes $L^{-d/2}e^{ik\cdot x/\rho}$ and weights $\langle k/\rho\rangle^r$.

**Reconstruction.** Periodization kernel is $L^{-d/2}(\langle k/\rho\rangle/\langle\xi\rangle)^r\widehat{\psi_\rho}(k/\rho-\xi)$; recovery kernel is $L^{-d/2}(\langle\xi\rangle/\langle k/\rho\rangle)^r\widehat{\chi_\rho}(\xi-k/\rho)$. Verified the $c_d$ cancellation: $(\mathcal P_\psi u)_k = L^{-d/2}c_d^{-1}\widehat{\psi u}(k/\rho) = L^{-d/2}\int\widehat\psi(k/\rho-\xi)\hat u(\xi)\,d\xi$, so no residual $c_d$; the recovery kernel is $L^{-d/2}\widehat\chi(\xi-k/\rho)$ by the same argument. Profile scaling $\widehat{\phi_\rho}(t)=\rho^d\widehat{\phi_0}(\rho t)$. Peetre with $\langle(k-\rho\xi)/\rho\rangle\le\langle k-\rho\xi\rangle$ (valid for $\rho\ge1$) and both signs of $r$ give the bound $C_r\rho^{d/2}F_r(k-\rho\xi)$.

**I verified the two Schur quantities.** At fixed $k$: $\int\rho^{d/2}F_r(k-\rho\xi)\,d\xi = \rho^{-d/2}\|F_r\|_1$ (substitute $u=k-\rho\xi$, $du=\rho^d d\xi$). At fixed $\xi$: $\sum_k\rho^{d/2}F_r(k-\rho\xi)=\rho^{d/2}\cdot O(1)$ on the unit lattice (lattice-spacing-one tail of order $>d$). Operator norm $\le\sqrt{\rho^{-d/2}\cdot\rho^{d/2}}=O(1)$; powers cancel. Roles reversed for recovery. Density (Schwartz / torus polynomials) and the no-pointwise-sampling claim (lines 91–95) are valid.

**Constants/limits.** Uniform in $\rho\ge1$; the only quantitative input beyond Peetre is rapid decay of the compact-smooth Fourier transform; $3<\pi$ guarantees strict containment in the cube. **RAD01 all controls PASS.**

### PROOF157 — `P:radius-compact-envelopes` — CHECKED

**Hypotheses.** Real $\sigma$, $\gamma>0$, $q\ge1$, $q\gamma>d$.

**Reconstruction.** Factorization $\Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma}=\Lambda^\sigma\mathcal E_{\chi_\rho}\mathcal I_\gamma\mathcal P_{\psi_\rho}\Lambda^{-\sigma-\gamma}$ is an equality on $L^2$ by the recovery identity, with negative $\sigma$ included. $\mathcal I_\gamma:H^{\sigma+\gamma}(\mathbb T_L)\to H^\sigma(\mathbb T_L)$ has singular values exactly $\langle k/\rho\rangle^{-\gamma}$ (ratio of the two Sobolev weights). I verified:
- the unit-cube bound $\langle x/\rho\rangle\le\sqrt2\langle k/\rho\rangle\langle(x-k)/\rho\rangle\le\sqrt{2(1+d/4)}\langle k/\rho\rangle$, i.e. $c_d'=\sqrt{2(1+d/4)}$;
- the volume estimate $\sum_k\langle k/\rho\rangle^{-u}\le(c_d')^u\rho^d\int\langle y\rangle^{-u}\,dy$, finite for $u=q\gamma>d$ by dyadic shells $2^{j(d-u)}$;
- $s_j(\Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma})\le C_{\chi_0,\sigma}C_{\psi_0,\sigma+\gamma}\lambda_j$ via the min–max singular-value bound for a composition, with the Bessel maps $\Lambda^\sigma,\Lambda^{-(\sigma+\gamma)}$ unitary, hence $S_q\le C\rho^{d/q}$; compactness from $\lambda_j\to0$ and finite-rank approximation.
- The two blocks are exactly the $\sigma=1/2$ and $\sigma=-1/2$ whole-space operators; $K_{\rm in}=UK_{\rm out}U$ under the swap $U(z_1,z_2)=(z_2,z_1)$, so the norms agree.
- Lines 164–167 are correct: $\gamma<1/2$ and $q\gamma>d$ force $q>2d\ge2$, so no Hilbert–Schmidt claim; and neither $P_{\chi_\rho}$ nor its adjoint is asserted self-adjoint or idempotent.

**RAD02 all controls PASS:** factorization with negative $\sigma$, singular values, $c_d'$, $u=q\gamma>d$, lattice volume $\rho^d$, rank approximation, two balanced blocks with equal norms, no endpoint/HS/self-adjoint overclaim.

### PROOF158 — `P:radius-actual-moments` — CHECKED

**Hypotheses.** Parameters (E:radius-anchor-parameters)–(E:radius-anchor-Q): $0<\gamma<\min(\tfrac12,\tfrac{2-\alpha}2)$, $\tfrac12<\theta<\eta_t<\beta_t<\min(1-\tfrac a2,\tfrac{3-a-\alpha}2)$; $Q$ even, $Q\gamma>d$, $\beta_t-\eta_t-\tfrac1Q>0$, $Q>\tfrac{2d}{1-a}$; horizon $B\ge1$; finite $v\ge1$.

**Reconstruction and constants verified.**
- Envelope choice $\rho=2R+B+2\le(B+4)R$; $\chi_\rho=\chi_0(\cdot/\rho)$ has plateau $B_{\rho}=B_{2R+B+2}\supseteq B_{2R+B+1}$, so both literal localizations $D_\chi A_j(I)=A_j(I)=A_j(I)D_\chi$ hold; the physical mask $m_R$ is left unmixed with the envelope $\chi_\rho$ (correct). Note the separation: variance uses base profile $\zeta=\eta^2$, envelope uses $\chi_0$ — exactly the RAD03 requirement.
- Variance budget: $P:wave-two-variances$ (with $\ell_R$ on mask $\zeta_R=m_R$) plus $L:driver-actual-variances$ give $V_{\rm out},V_{\rm in}\le b_I D_\gamma^2$, $b_I=C_T h^{2-a}B_\alpha(h)$, with $C_T$ independent of $R$ (the $R$-uniformity is genuine: $\|k_R\|_1=L$ independent of $R$, and $\nu_R(B(y,r))\le c_d^2L^2C_\Gamma r^\alpha$ uniformly in $R$). Both variance directions remain.
- $C:finite-gaussian-operators$ at even $q\ge Q$ gives $\|M_N(I)\|_{L^q(S_q)}\le\sqrt{q-1}\,\sqrt{C_T}\,h^{1-a/2}B_\alpha(h)^{1/2}\|K_{\rm out}\|_{S_q}$ (both localizations and both variances hold; $q\gamma\ge Q\gamma>d$).
- Fixed-$Q$-first step: $\|K_{\rm out}\|_{S_q}\le\|K_{\rm out}\|_{S_Q}$ (unnormalized; normalized singular-value-by-$\ell^Q$-norm argument is correct), then $E:radius-two-envelopes$ applied only at $Q$ gives $\|K_{\rm out}\|_{S_Q}\le C_Q\rho^{d/Q}\le C_Q(B+4)^{d/Q}R^{d/Q}$. So the $q$-dependence is frozen at $Q$ before varying the moment order — exactly the honesty requirement.
- Operator norm $\le S_q$ norm, $\sqrt{q-1}\le\sqrt q$; short-time power is $1-\tfrac a2$ ($\alpha<1$), or $\tfrac{3-a-\alpha}2$ ($\alpha>1$), with the critical log at $\alpha=1$ absorbed by the strict gap $1-\tfrac a2-\beta_t>0$; hence the increment bound $E:radius-finite-increment$ with exponent $\beta_t$ and constant $C_{Q,B}\sqrt q\,R^{d/Q}$.
- Dyadic chaining: fine-level max bound $\|D_n\|_{L^q}\le2^{n/q}C_{Q,B}\sqrt q\,R^{d/Q}(B2^{-n})^{\beta_t}$ uses only (finite-maximum) power-linearity, no independence; the weighted-sum ratio is $2^{-(\beta_t-\eta_t-1/q)}\le2^{-(\beta_t-\eta_t-1/Q)}<1$, uniformly in $q\ge Q$ (second $Q$ guard). Coarse levels by unit partition. Chaining (as in $L:driver-holder-limit$) yields $\|\cdot\|_{L^qC^{\eta_t}}\le C_{Q,B}\sqrt q\,R^{d/Q}$, then $C^{\eta_t}\hookrightarrow C^\theta$.
- Fixed-$R$ limit: $M_N\to M_R$ in all finite $L^p(C^\theta)$; the uniform-in-$N$ bound passes to the limit, with explicit $R$-dependence at each $R$ (no uniform-in-$R$ convergence claimed, correctly).
- Arbitrary $v$: even $q\ge\max(v,Q)$, $q\le v+Q+2\le(Q+3)v$; Lyapunov gives $\|M_R\|_{L^v}\le C_{Q,B}\sqrt v\,R^{d/Q}$ after absorbing $\sqrt{Q+3}$. The statement's "$F$-columns require their own estimates" and "projection must satisfy orthogonality/covariance hypotheses" disclaimers are honest.

**RAD03 all controls PASS:** same-noise coefficient paths, envelope covers localization, base mask $\eta^2$ both variances, compact Gaussian estimate, fixed-$Q$-first then $S_q\le S_Q$, strict log absorption and dyadic $q$-uniform ratio $\beta_t-\eta_t-1/Q>0$, even-$q$ choice for arbitrary $v$, no $C^\theta S_q$ or $F$-column estimate.

### PROOF159 — `C:radius-covariance-residuals` — CHECKED

**Hypotheses.** $Y$ centered Gaussian linear noise, $\mathrm{Var}\,Y(f)\le C\|f\|_{H_W}^2$, $C\ge0$; second part $Y_m(f)=W((I-\Pi)T_{\delta,m}f)$ with deterministic orthogonal $\Pi$ on the slow $H_W$.

**Reconstruction.**
- First assertion: $P:source-gaussian-transfer$ is a linear Gaussian covariance-contraction for this mask and these deterministic coefficient maps; its tail/norm transfer (E:source-transfer-norm) gives $\|M_R(Y)\|_{L^v(C^\theta)}\le\sqrt C\,C_{Q,B}\sqrt v\,R^{d/Q}$ after PROOF158; $C=0$ gives zero directly; the actual $Y$ is not replaced by the reference. Correct.
- Second assertion: the raw pullback $T_{\delta,m}$ is an isometry (factor $\delta^{a-2}\delta^2\delta^{-a}=1$ re-derived by hand from the raw covariance under $s=s_m+\delta u$, $t=s_m+\delta r$), and $\|I-\Pi\|\le1$ gives $\mathrm{Var}\,Y_m(f)\le\|f\|_{H_W}^2$; right side is the raw fast-coordinate norm. Arbitrary (even infinite) rank, $\delta,R$-dependent $\Pi$ allowed; correlated blocks retained; no independence and no random projection. Correct.

**RAD04 all controls PASS.**

### PROOF160 — `P:radius-mean-anchor` — CHECKED

**Hypotheses.** Fixed $B\ge1$, $0<\delta<\min(1,1/B)$, $N=\lfloor1/(\delta B)\rfloor$, true block partition with $\ell_m=B$ ($m<N$), $\ell_N=\delta^{-1}-NB\in[0,B)$; $Y_m$ as in the corollary; $X_m(u)=g_\delta M_R(Y_m)(\min(u,\ell_m))$, $g_\delta=\delta^{(1-a)/2}$; fixed $p\ge1$.

**Reconstruction verified.**
- Stopping at $\ell_m$ and constant extension to $B$ does not increase $\sup$ or the Hölder seminorm (increments straddling $\ell_m$ vanish); an empty last interval ($\ell_N=0$) gives the zero path (driver is zero-start, so $M_R(Y_m)(0)=0$).
- Lyapunov for $p\ge1$ and linearity of a finite sum (no independence, no max): $\mathbb E Z_\delta\le(\mathbb E Z_\delta^p)^{1/p}=(\delta\sum_m\mathbb E\|X_m\|^p)^{1/p}\le[\delta(N+1)]^{1/p}g_\delta C_{Q,B}\sqrt p\,R^{d/Q}$; each $\mathbb E\|X_m\|^p\le g_\delta^p(C_{Q,B}\sqrt p\,R^{d/Q})^p$ from the corollary at $v=p$ (with $C=1$).
- $\delta B<1$ gives $N\ge1$ and $N+1\le2/(\delta B)$ (since $1/(\delta B)>1$ forces $1+1/(\delta B)<2/(\delta B)$), giving $E:radius-mean-anchor$.
- $R_\delta=\delta^{-1}+2\le3/\delta$ for $\delta<1$. The third $Q$ guard $Q>\tfrac{2d}{1-a}$ is equivalent to $Q(1-a)>2d$, so $e_{\rm anchor}=\tfrac{1-a}2-\tfrac dQ=\tfrac{Q(1-a)-2d}{2Q}>0$ strictly. Substitution gives $g_\delta R_\delta^{d/Q}\le\delta^{(1-a)/2}3^{d/Q}\delta^{-d/Q}=3^{d/Q}\delta^{e_{\rm anchor}}$, matching $E:radius-mean-anchor-decay$ with constant $2(2/B)^{1/p}C_{Q,B}\sqrt p\,3^{d/Q}$ and decay $\delta^{e_{\rm anchor}}\to0$; uniform in deterministic projections since the corollary's $C=1$ bound is projection-independent. Fixed $B,p,Q$, model; no concentration/nonlinear/point conclusion claimed. **RAD05 all controls PASS.**

### RAD06–RAD08 (fidelity, adversarial controls, completeness) — PASS

- **RAD06.** Mask/envelope separation, fixed-$R$ driver reuse at its stated scope, raw-pullback and Gaussian-transfer hypotheses, and the three strengths (uniform outer factors / polynomial $\rho^{d/q}, R^{d/Q}$ growth / fixed-parameter expected-norm decay) are kept distinct; no F-column or concentration import is silently made.
- **RAD07.** Hand controls checked: $\rho=1$ and large $\rho$ scaling; negative Sobolev index ($\sigma=-\tfrac12$ block); $q=Q$ and $q>Q$ versus fixed-$Q$ constant; white $d=\alpha=1$ critical log absorption; zero covariance (drivers vanish directly); $\Pi=0$, $\Pi=I$, and infinite-rank $\Pi$; correlated blocks (no independence used); $\tau=0$/empty last interval; exponent near the $Q$-threshold (strict, $Q$ fixed, no endpoint uniformity claimed).
- **RAD08.** All five bodies reconstructed; dependencies form the linear chain 156→157→158→159→160 with no circularity; every original model amplitude/covariance retained; the closing paragraph (lines 376–384) honestly disclaims constant-column $F$, unmasked-wave construction, cone/point transfer, concentration, infinite-head Gaussian integration, nonlinear moment growth, and $Q,B\to\infty$/endpoint uniformity.

## Required fixes before production gate

None. All five target proofs are mathematically sound within their stated hypotheses and scopes; no blocking repair is required.

## One-line summary

PROOF156–160 are valid radius-explicit first-driver estimates: the uniform outer-map Schur cancellation, the $S_q\le C\rho^{d/q}$ envelope bound, the fixed-$Q$ $R^{d/Q}$ path-moment estimate, the covariance-residual contraction, and the expected-norm decay $e_{\rm anchor}=(1-a)/2-d/Q>0$ at $R_\delta=\delta^{-1}+2$ all hold with the stated constants, scopes, and no forbidden overclaims.