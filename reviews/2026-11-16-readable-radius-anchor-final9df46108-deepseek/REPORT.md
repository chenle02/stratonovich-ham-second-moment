# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro (deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

All five assigned proof pairs were read in full in both revisions, including every unchanged portion. The revisions are a readability rewrite: three proofs gain step headings and short orienting/derivation sentences; two proofs are byte-identical in their proof bodies. The new explanatory sentences were each checked against the same hypotheses, normalizations and conventions and were found accurate. No step, qualifier, exponent, normalization or constant-dependence statement was silently repaired or invented in the new text, and no new unsupported claim was introduced.

Reconstruction convention: the module uses the unnormalized torus $L^2(Q_L,\mathrm dx)$ with $L=2\pi\rho$, modes $L^{-d/2}e^{ik\cdot x/\rho}$ (so $\kappa_k=2\pi k/L=k/\rho$), weights $\langle k/\rho\rangle^r$, and whole-space $H^r$ norms $\|\langle\xi\rangle^r\hat u\|_2$. Named upstream inputs were used only after checking their application hypotheses; their own proofs are unassigned and were not counted. Below, "OLD/NEW LF" refer to module-local line numbers per the inventory.

---

## L:radius-outer-maps

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage (both revisions).**

(1) *Kernel derivation.* The kth periodization coefficient is
$$(\mathcal P_{\psi_\rho}u)_k=L^{-d/2}\int_{Q_L}\psi_\rho(x)u(x)e^{-ik\cdot x/\rho}\,\mathrm dx,$$
with the integral on $\R^d$ equal to the torus integral because $\operatorname{supp}\psi_\rho\subset B_{3\rho}$ and $3<\pi$ places it strictly inside $Q_L$. The weighted kernel is
$$L^{-d/2}\big(\langle k/\rho\rangle/\langle\xi\rangle\big)^r\widehat{\psi_\rho}(k/\rho-\xi),$$
and for recovery
$$L^{-d/2}\big(\langle\xi\rangle/\langle k/\rho\rangle\big)^r\widehat{\chi_\rho}(\xi-k/\rho).$$
These coincide with the kernels in unassigned Lemma L:cutoff-factorization with $\kappa_k=k/\rho$; the claim "no additional $(2\pi)^{-d/2}$" matches that lemma's own $c_d$ cancellation statement. I verified directly that the modes $L^{-d/2}e^{ik\cdot x/\rho}$ are orthonormal in $L^2(Q_L,\mathrm dx)$ (integral $\int_{(-\pi\rho,\pi\rho)^d}e^{i(k-\ell)\cdot x/\rho}\mathrm dx=L^d\delta_{k\ell}$), confirming the normalization convention.

(2) *Scaling.* $\widehat{\phi_\rho}(t)=\rho^d\widehat{\phi_0}(\rho t)$ is the standard dilation formula, applied to $\phi_0\in\{\psi_0,\chi_0\}$. Substituting in the first kernel:
$$(2\pi\rho)^{-d/2}\rho^d(\langle k/\rho\rangle/\langle\xi\rangle)^r\widehat{\psi_0}(k-\rho\xi)=(2\pi)^{-d/2}\rho^{d/2}(\cdot).$$

(3) *Peetre reduction.* Peetre $\left(\frac{\langle x\rangle}{\langle y\rangle}\right)^r\le2^{|r|/2}\langle x-y\rangle^{|r|}$ (valid for negative $r$ after interchange) with $x=k/\rho$, $y=\xi$, plus $\langle(k-\rho\xi)/\rho\rangle\le\langle k-\rho\xi\rangle$, which holds only because $\rho\ge1$, gives
$$|\text{kernel}|\le C_r\rho^{d/2}F_r(k-\rho\xi),\quad F_r(t)=|\widehat{\phi_0}(\pm t)|\langle t\rangle^{|r|}.$$
The factor $(2\pi)^{-d/2}2^{|r|/2}$ is absorbed into $C_r$. This is the required $\rho^{d/2}$ kernel bound.

(4) *Schur quantities.* $F_r$ is integrable and decays faster than every inverse power. At fixed $k$, $\int\rho^{d/2}F_r(k-\rho\xi)\,\mathrm d\xi$ needs the substitution $y=\rho\xi-k$ (Jacobian $\rho^{-d}$): value $C\rho^{-d/2}$. At fixed $\xi$, $\sum_k\rho^{d/2}F_r(k-\rho\xi)=\rho^{d/2}\sum_kF_r(k-\rho\xi)$; the sum is over the integer lattice with shift $\rho\xi$ and is bounded by E:cutoff-lattice-sum (tail order $>d$), value $C\rho^{d/2}$. Lattice spacing is $1$ ($k\in\mathbb Z^d$) — I confirm there is no lattice-density factor. The two quantities multiply to a radius-independent constant, and the mixed Schur inequality gives $\|T\|\le\sqrt{M_1M_2}$ with the radius powers cancelling before the square root. For recovery the row/column roles reverse with the same cancellation.

(5) *Extension.* Bounded-kernel extension from Schwartz functions and torus polynomials plus the distributional identification from L:cutoff-factorization (no point sampling of rough Fourier data) covers all real $r$, including negative $r$.

**New explanations.** Three insertions. (a) Opening summary "rescale the exact Fourier kernels and bound their integral and lattice-sum norms separately… radius powers cancel in the mixed Schur estimate" — accurate and consistent with steps (3)–(4). (b) "The bracket comparison uses $\rho\ge1$; consequently, the constants multiplying the explicit radius powers in the two Schur bounds depend only on the fixed $\phi_0,r,d$" — correct: the only $\rho$-assumption used is $\rho\ge1$ in $\langle\cdot/\rho\rangle\le\langle\cdot\rangle$; $C_r$ absorbs only $(2\pi)^{-d/2}2^{|r|/2}$ and $\|F_r\|_1$/lattice-sum constants, which depend on $\phi_0,r,d$. (c) "In the integral bound, the substitution $\rho\xi-k$ contributes $\rho^{-d}$. Multiplying by the kernel's factor $\rho^{d/2}$ gives $\rho^{-d/2}$" — exactly the computation in step (4).

**Constants.** $C_{\psi_0,r},C_{\chi_0,r}$ depend on the fixed base profile, $r$, and $d$; they are independent of $\rho\ge1$, hence of $R$, basis truncation, moment index, and any residual projection. No defeat identified.

---

## P:radius-compact-envelopes

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.**

(1) *Full-domain factorization.* The recovery identity (unassigned E:cutoff-whole-space-recovery) $\chi_\rho u=\mathcal E_{\chi_\rho}\mathcal I_\gamma\mathcal P_{\psi_\rho}u$ on $H^{\sigma+\gamma}$, valid on the whole domain by density including negative $\sigma$, gives
$$\Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma}=\Lambda^\sigma\mathcal E_{\chi_\rho}\mathcal I_\gamma\mathcal P_{\psi_\rho}\Lambda^{-\sigma-\gamma}.$$
Here $\Lambda^{-\sigma-\gamma}:L^2\to H^{\sigma+\gamma}$ and $\Lambda^\sigma:H^\sigma\to L^2$ are isometries (unitary Bessel maps), $\mathcal I_\gamma$ is diagonal on the torus with singular values $\langle k/\rho\rangle^{-\gamma}$, and the two non-Bessel outer maps are bounded uniformly in $\rho$ by L:radius-outer-maps.

(2) *Diagonal sum to volume integral.* For $u=q\gamma>d$ and $x\in k+[-1/2,1/2]^d$:
$$\langle x/\rho\rangle\le\sqrt2\langle k/\rho\rangle\langle(x-k)/\rho\rangle\le\sqrt2\langle k/\rho\rangle\sqrt{1+d/4}=c_d'\langle k/\rho\rangle,$$
using $|x-k|\le\sqrt d/2$ and $\rho\ge1$. This yields $\langle k/\rho\rangle^{-u}\le(c_d')^u\langle x/\rho\rangle^{-u}$, integrating over the unit cubes (each of volume one) and substituting $y=x/\rho$:
$$\sum_k\langle k/\rho\rangle^{-u}\le(c_d')^u\rho^d\int_{\R^d}\langle y\rangle^{-u}\mathrm dy\le C_{d,u}\rho^d.$$
Convergence for $u>d$ is by dyadic annuli (terms $\sim2^{j(d-u)}$, geometric). The $\rho^d$ comes solely from the change-of-variable Jacobian; the lattice spacing is one throughout. This is the volume factor.

(3) *Singular-value transfer.* Order the inclusion's diagonal values $(\lambda_j)\downarrow0$; retaining the first $j-1$ coordinates has rank $<j$ and error $\lambda_j$. Composing with the bounded outer factors and applying unassigned P:cutoff-singular-values gives $s_j\le C_{\chi_0,\sigma}C_{\psi_0,\sigma+\gamma}\lambda_j$, which also proves compactness by finite-rank approximation. Summing $q$th powers:
$$\sum_js_j^q\le C^q\sum_j\lambda_j^q=C^q\sum_k\langle k/\rho\rangle^{-q\gamma}\le C\rho^d,$$
so taking the $q$th root gives $C\rho^{d/q}$. This is a power summed then rooted, producing $\rho^{d/q}$, not an unpowered sum or a doubled exponent. No separate Schatten ideal theorem is invoked.

(4) *Balanced envelopes.* $K_{\rm out}=P_{\chi_\rho}D_\gamma$ has blocks $\sigma=1/2$ and $\sigma=-1/2$; direct-sum Schatten norms add ($\|K\|_{S_q}^q=\|K_{1/2}\|^q+\|K_{-1/2}\|^q$), giving $2^{1/q}C\rho^{d/q}\le C_q\rho^{d/q}$. Unassigned P:compact-two-envelopes gives $K_{\rm in}=VK_{\rm out}V$ for the unitary swap $V(z_1,z_2)=(z_2,z_1)$, which commutes with the scalar diagonal $D_\gamma$; unitary conjugation preserves singular values, so the norms agree.

(5) *Endpoint remark.* From the fixed parameters $\gamma<1/2$ and $q\gamma>d$: $q>d/\gamma>2d\ge2$; no $q=2$ Hilbert–Schmidt conclusion is drawn. The proof notes explicitly that neither $P_{\chi_\rho}$ nor its adjoint is assumed selfadjoint or idempotent.

**New explanations.** The step structure (factorization / volume comparison / singular-value transfer) is accurate and changes nothing. The added Step-2 paragraph, "unit cubes partition Euclidean space and each has volume one… bounds the constant cube value $\langle k/\rho\rangle^{-u}$ by $(c_d')^u\langle x/\rho\rangle^{-u}$… substituting $y=x/\rho$ gives the factor $\rho^d$… a $q$th root later gives $\rho^{d/q}$," states precisely the direction of inequality I verified in step (2). All justifications hold.

**Constants.** $C_{\sigma,\gamma,q,d,\chi_0,\psi_0}$ (and $C_q$) may depend on $\sigma,\gamma,q,d$ and the fixed auxiliary cutoffs; the only $\rho$-dependence is the explicit $\rho^{d/q}$, and there is no dependence on basis truncation, moment index or residual projection (none exists here). No defeat identified.

---

## P:radius-actual-moments

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.**

(1) *Localization envelope.* From the driver construction, coefficients $g_j=W(f_j)$ (original noise, unassigned L:driver-noise-basis) and $M_N=\sum_{j\le N}g_jA_j$. The proof chooses the envelope radius
$$\rho=2R+B+2\le(B+4)R,\qquad\chi=\chi_0(\cdot/\rho).$$
I check $(B+4)R-(2R+B+2)=(B+2)(R-1)\ge0$ for $R\ge1$. Since $\chi_0=1$ on $B_1$, $\chi_\rho=1$ on $B_{2R+B+2}\supset B_{2R+B+1}$, so both localization identities in unassigned E:driver-actual-localization hold (the older driver lemma uses $\chi=1$ on $B_{2R+T+1}$ with $T=B$). The physical mask remains $m_R$, and both envelopes $K_{\rm in},K_{\rm out}$ use this same $\chi_\rho$.

(2) *Increments from both variance directions.* For an interval $I\subset[0,B]$ with $0<h=|I|\le1$, unassigned P:wave-two-variances and L:driver-actual-variances give both finite weighted variances dominated by $V_{B,\mathrm{var}}h^{2-a}B_\alpha(h)\,D_\gamma^2$, uniformly in $R,N,I$ (the constant is the baseline $C_T$ at $T=B$; it does not depend on $I$, $R$, or the family size). The base mask is the fixed profile $\zeta=\eta^2$. Unassigned C:finite-gaussian-operators, applied in balanced coordinates with even $q\ge Q$ (so $q\gamma>d$), gives
$$\|M_N(I)\|_{L^q(S_q)}\le\sqrt{q-1}\sqrt{V_{B,\mathrm{var}}}\,h^{1-a/2}B_\alpha(h)^{1/2}\|K_{\rm out}\|_{S_q},$$
with $B_\alpha(h)=1$, $1+\log(1/h)$, or $h^{1-\alpha}$ for $\alpha<1$, $=1$, $>1$. Both variances and both localizations are required; basis-dependent coefficient bounds are not summed. All hypotheses of C:finite-gaussian-operators are discharged by L:driver-actual-variances.

(3) *Fixed Schatten index.* For $q\ge Q$, $\|K_{\rm out}\|_{S_q}\le\|K_{\rm out}\|_{S_Q}$ by $\ell^p$ monotonicity of the unnormalized singular-value sequence (normalize by the $\ell^Q$ norm; each entry $\le1$). E:radius-two-envelopes is used only at the fixed index $Q$: $\|K_{\rm out}\|_{S_Q}\le C_Q\rho^{d/Q}$. Then $\|A\|\le\|A\|_{S_q}$, $\sqrt{q-1}\le\sqrt q$, complexification preserves the operator norm, and $\rho^{d/Q}\le(B+4)^{d/Q}R^{d/Q}$ yield
$$\|M_N(t)-M_N(u)\|_{L^q(\mathcal L(E))}\le C_{Q,B}\sqrt q\,R^{d/Q}|t-u|^{\beta_t},\quad|t-u|\le1.$$
Exponent absorption: for $\alpha<1$, $h^{1-a/2}\le h^{\beta_t}$ since $\beta_t<1-a/2$; for $\alpha=1$, $(1+\log(1/h))^{1/2}$ is absorbed by the strict gap $1-a/2-\beta_t>0$; for $\alpha>1$, the power is $(3-a-\alpha)/2>\beta_t$ by the parameter constraint. Constants are independent of $R,N,q$; longer increments are finite sums of unit increments with $B$-dependent constants.

(4) *Dyadic chaining.* $D_n(F)$ is the largest adjacent increment on the grid $kB2^{-n}$; for $B2^{-n}\le1$ the finite-maximum bound
$$\|D_n(M_N)\|_{L^q}\le2^{n/q}C_{Q,B}\sqrt q\,R^{d/Q}(B2^{-n})^{\beta_t}$$
uses no independence. Multiplying by $2^{n\eta_t}$ and summing gives a geometric ratio $2^{-(\beta_t-\eta_t-1/Q)}<1$ (uniformly for even $q\ge Q$ since $1/q\le1/Q$); the finitely many coarse levels use unit partitions. Unassigned L:driver-holder-limit then bounds the $L^qC^{\eta_t}$ norm by $C_{Q,B}\sqrt qR^{d/Q}$, and $\theta<\eta_t$ embeds into $C^\theta$.

(5) *Limit and Lyapunov.* For fixed $R$, L:driver-holder-limit identifies $M_R(W)$ as the all-finite-moment $C^\theta$ limit of these $M_N$; the uniform-in-$N$ estimate passes to the limit. The proof explicitly says uniform convergence in $R$ is unnecessary — the bound is radius-explicit, not radius-uniform. For $v\ge1$ choose even $q\in[\max(v,Q),\,v+Q+2]\le(Q+3)v$; Lyapunov gives $\|M_R(W)\|_{L^v}\le\|M_R(W)\|_{L^q}\le C_{Q,B}\sqrt{Q+3}\sqrt vR^{d/Q}$, absorbing $\sqrt{Q+3}$.

**New explanations.** All four step headings and the two orienting sentences ("keep the physical noise mask fixed while choosing a larger localization envelope", "use only one fixed Schatten index to extract the radius factor, then apply the dyadic path estimate uniformly over all higher moment indices") are accurate restatements of the proof's content; no quantitative claim is added or altered.

**Constants and independence.** $C_{Q,B}$ depends on the model, $B$, $Q$, the exponents and the fixed cutoffs, but is independent of $v$ (only $\sqrt v$ appears), of $R$ (only $R^{d/Q}$ appears), of the truncation $N$, and of any residual projection (none is present). The proof correctly avoids inferring radius-uniform convergence. No defeat identified.

---

## C:radius-covariance-residuals

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: none added (proof body byte-identical)

**Original-step coverage.**

(1) *Transfer.* Unassigned P:source-gaussian-transfer is a linear Gaussian covariance-contraction theorem with the same physical mask $m_R$ and the same deterministic coefficient maps $A_j$. Its conclusion E:source-transfer-norm is $\|M_Y\|_{L^p}\le\sqrt C\|M_R\|_{L^p}$; combining with P:radius-actual-moments gives
$$\|M_R(Y)\|_{L^v(C^\theta)}\le\sqrt C\,C_{Q,B}\sqrt v\,R^{d/Q}.$$
The reference has the canonical operator-path law used in P:radius-actual-moments; the noise $Y$ is not replaced by the reference noise in this comparison (only its law dominates, which is the content of the finite comparison L:source-finite-comparison). The zero-covariance case gives zero directly. I confirmed the application hypothesis: Y is centered Gaussian linear with $\operatorname{Var}Y(F)\le C\|F\|_{H_W}^2$, which is exactly E:source-raw-variance-bound.

(2) *Residual isometry.* For $Y_m(f)=W((I-\Pi)T_{\delta,m}f)$, unassigned L:raw-block-inputs proves $T_{\delta,m}$ is an isometry of the original test completion (the substitution $s=s_m+\delta u$ gives the factor $\delta^{a-2}\delta^2\delta^{-a}=1$), and $\Pi$ is an orthogonal projection so $\|I-\Pi\|\le1$. Hence
$$\operatorname{Var}Y_m(f)=\|(I-\Pi)T_{\delta,m}f\|_{H_W}^2\le\|f\|_{H_W}^2,$$
so $C=1$. The projection is deterministic, may have infinite rank and depend on $\delta,R$; residuals retain the given slow $W$ and may be correlated; no random noise-dependent projection is used, and no requirement that residuals lie in the span of one fast noise exists (not a hypothesis of the transfer). All assertions preserved verbatim. No defeat identified.

---

## P:radius-mean-anchor

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: none added (proof body byte-identical)

**Original-step coverage.**

(1) *Stopping and empty block.* Stopping an interaction primitive at $s=\ell_m$ and extending it constantly to $B$ does not increase its supremum or Hölder seminorm; an empty last interval ($\ell_N=0$) gives the zero path because the primitive starts at zero. These are used to regard $X_m=g_\delta M_R(Y_m)(\min(\cdot,\ell_m))$ as a $C^\theta$ path on $[0,B]$.

(2) *Aggregate expectation.* For any fixed $p\ge1$:
$$\mathbb E Z_\delta\le(\mathbb E Z_\delta^p)^{1/p}=\left(\delta\sum_{m=0}^N\mathbb E\|X_m\|_{C^\theta}^p\right)^{1/p}\le[\delta(N+1)]^{1/p}g_\delta C_{Q,B}\sqrt p\,R^{d/Q}.$$
The first inequality is Lyapunov ($Z_\delta\ge0$); the equality is exact because $Z_\delta^p=\delta\sum_m\|X_m\|^p$ is a finite linear aggregate (a $p$-norm power), so expectation commutes with the $\delta$-weighted finite sum — no time-block independence and no maximum over blocks replaces the finite-sum expectation. The last inequality uses C:radius-covariance-residuals at moment order $v=p$ with $C=1$: $\mathbb E\|X_m\|^p=g_\delta^p\mathbb E\|M_R(Y_m)(\min(\cdot,\ell_m))\|^p\le g_\delta^p(C_{Q,B}\sqrt pR^{d/Q})^p$.

(3) *Block count.* $\delta B<1$ gives $N=\lfloor1/(\delta B)\rfloor\ge1$ and $N+1\le2/(\delta B)$ (since $N+1\le x+1\le2x$ for $x=(1/\delta B)>1$). Hence $[\delta(N+1)]^{1/p}\le(2/B)^{1/p}$, proving E:radius-mean-anchor.

(4) *Radius substitution.* For $R_\delta=\delta^{-1}+2$ and $\delta<1$, $R_\delta\le3/\delta$. The last condition of E:radius-anchor-Q reads $Q>2d/(1-a)$, equivalent to $Q(1-a)>2d$ (since $a<1$), and dividing by $2Q>0$ gives $e_{\mathrm{anchor}}=(1-a)/2-d/Q>0$. Substituting:
$$g_\delta R_\delta^{d/Q}=\delta^{(1-a)/2}(\delta^{-1}+2)^{d/Q}\le3^{d/Q}\delta^{(1-a)/2-d/Q}=3^{d/Q}\delta^{e_{\mathrm{anchor}}}\to0.$$
Multiplying by $2(2/B)^{1/p}C_{Q,B}\sqrt p$ gives E:radius-mean-anchor-decay. The estimate holds at each fixed $B,p,Q$ and model, uniformly in every deterministic residual projection; it is numerical, and is explicitly not an $F$ estimate, cone coverage, source-to-point transfer, or nonlinear moment bound (the following paragraph disclaims each). Zero covariance makes all operator paths and stochastic bounds vanish. No defeat identified.

---

## AUDIT dispositions

- L:radius-outer-maps — PRESERVED; three new explanatory sentences verified against the rescaled kernels, the $\rho\ge1$ bracket comparison, and the $\rho^{-d/2}$ substitution computation.
- P:radius-compact-envelopes — PRESERVED; step headings and the volume-comparison gloss verified against the unit-cube comparison and $q$th-root extraction.
- P:radius-actual-moments — PRESERVED; step headings and summaries verified; the fixed-index $S_Q$ extraction, exponent absorption, dyadic sum and Lyapunov step all reproducible.
- C:radius-covariance-residuals — PRESERVED; proof body unchanged; reconstruction confirms covariance domination, deterministic projection, slow/fast isometry, no random projection.
- P:radius-mean-anchor — PRESERVED; proof body unchanged; finite-sum expectation, block-count bound, and the last-$Q$-condition positivity of $e_{\mathrm{anchor}}$ all reproducible.

Required invariant checks all pass: (i) rescaled Fourier kernels carry exact $(2\pi)$-cancellation and no extra factor; (ii) the $\rho^{d/2}$ kernel bound splits into $\rho^{-d/2}$ integral and $\rho^{d/2}$ lattice-sum quantities with radius-independent product before the mixed-Schur square root, and no lattice-density factor appears; (iii) negative Sobolev indices and the distributional recovery identity are preserved without point sampling; (iv) the compact-envelope argument sums $q$th powers then roots, yielding $\rho^{d/q}$, with unitary Bessel maps, diagonal singular values, finite-rank transfer, direct-sum and unitary-swap norm identities, and no projection/selfadjointness assumption on the cutoff; (v) $q\gamma>d$ and the later $q>2d$ are preserved with no Hilbert–Schmidt conclusion; (vi) path moments use the original-noise coefficient sums, envelope $\rho=2R+B+2$, both localizations and both weighted variances with mask $m_R$, the finite-Gaussian bound at even $q\ge Q$, the fixed-$Q$ norm domination, correct power/log branches, strict absorption, dyadic maxima, $\eta_t/\theta$ gaps and the fixed-$R$ path limit, with arbitrary $v$ from a controlled larger even $q$ and no radius-uniform convergence claimed; (vii) residuals use full covariance domination, deterministic projection and original isometry; (viii) the mean anchor retains true block counts/lengths, constant stopping, $g_\delta$, the exact $\delta$-weighted $p$-aggregate for any fixed $p\ge1$, empty last interval and the zero-covariance case, the finite-sum expectation, and the numerical radius $R_\delta=\delta^{-1}+2$ with positive exponent under the last $Q$ condition.

## Findings and limits

- The rewrite is purely expository: three proofs acquired step structure and clarifying sentences; two proofs are unchanged. Byte deltas aside, the added sentences reproduce checkable derivations without introducing new constants, factors, or hypotheses.
- No new rewrite defect was found. Arguments, quantifiers, exponents, and constant-dependence statements are preserved identically between revisions.
- Pre-existing (not rewrite) context notes, flagged honestly: the proofs lean on named upstream results (cutoff factorization and singular values, compact two envelopes, finite Gaussian operators, wave variances, driver variances/Hölder limit, Gaussian transfer, block-input isometry); I verified their application hypotheses where the module cites them, but their own proofs are unassigned and were not reviewed here. The symbols $V_{B,\mathrm{var}}$ and $C_Q$ are module-local renamings of upstream constants ($C_T$, $C_{\sigma,\gamma,q,d,\chi_0,\psi_0}$); this is a benign labeling choice, not an estimate change. The module's final paragraph correctly disclaims $F$-column estimates, cone coverage, source-to-point transfer, concentration, and uniformity in $Q,B\to\infty$; these are scope limits, not defects.
- Reading is COMPLETE for all five proofs in both revisions; public reconstruction is COMPLETE for all five. No obstruction, uncertainty or failure was encountered within the assigned scope. This review does not certify the upstream proofs, Lean correspondence, rendered pages, or whole-book truth, none of which was assigned.
