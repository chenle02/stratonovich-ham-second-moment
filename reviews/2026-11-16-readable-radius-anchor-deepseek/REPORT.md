# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

The rewrite of `notes/integrated_radius_anchor.tex` is purely additive and explanatory. All five statements, the section preamble, and the closing remarks are byte-identical between revisions (line shifts are consistent with purely additive growth: +10 in proof 1, +19 in proof 2, +24 in proof 3, +0 in proof 4, +4 in proof 5). Every new explanatory assertion is mathematically correct and matches the guiding requirements (radius-power bookkeeping, Schatten-index freezing, no invented lattice density, no radius-uniform convergence inference, no independence/maximum replacement). All five target deductions, including unchanged proof 4, are publicly reconstructed below.

## L:radius-outer-maps
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Exact kernels. With $L=2\pi\rho$ and $\kappa_k=2\pi k/L=k/\rho$, the periodization kernel is $L^{-d/2}(\langle k/\rho\rangle/\langle\xi\rangle)^r\widehat{\psi_\rho}(k/\rho-\xi)$ and the recovery kernel is $L^{-d/2}(\langle\xi\rangle/\langle k/\rho\rangle)^r\widehat{\chi_\rho}(\xi-k/\rho)$. This matches the upstream Lemma `L:cutoff-factorization` with $\kappa_k=k/\rho$ and its explicit statement "there is no additional $c_d$": for periodization, the $c_d=(2\pi)^{-d/2}$ of Fourier inversion cancels its $c_d^{-1}$ in the ordinary Fourier integral, so the kernel is exactly $L^{-d/2}\widehat\psi(\kappa_k-\xi)$ with no surviving $(2\pi)^{-d/2}$; the torus mode normalization $L^{-d/2}$ supplies the recovery kernel factor directly.
  2. Scaling: $\widehat{\phi_\rho}(t)=\int\phi_0(x/\rho)e^{-itx}dx=\rho^d\widehat{\phi_0}(\rho t)$.
  3. Kernel magnitude: $L^{-d/2}=(2\pi)^{-d/2}\rho^{-d/2}$; inserting $\widehat{\psi_\rho}(k/\rho-\xi)=\rho^d\widehat{\psi_0}(k-\rho\xi)$ and applying Peetre `E:cutoff-peetre` (valid for negative r by interchanging $x,y$) plus $\langle(k-\rho\xi)/\rho\rangle\le\langle k-\rho\xi\rangle$ for $\rho\ge1$, the absolute kernel is bounded by $C_r\rho^{d/2}F_r(k-\rho\xi)$ with $F_r(t)=|\widehat{\phi_0}(\pm t)|\langle t\rangle^{|r|}$. The $\pm$ handles the two maps' sign $\rho\xi-k$ vs $k-\rho\xi$.
  4. Column/row Schur quantities. Fixed $k$, $\int C_r\rho^{d/2}F_r(k-\rho\xi)d\xi$ with $t=\rho\xi-k$, $d\xi=\rho^{-d}dt$, gives $C_r\rho^{d/2}\rho^{-d}\|F_r\|_1=C\rho^{-d/2}$. Fixed $\xi$, $\sum_k C_r\rho^{d/2}F_r(k-\rho\xi)=C\rho^{d/2}\sup_y\sum_k F_r(k-y)\le C\rho^{d/2}$ by `E:cutoff-lattice-sum` (integer lattice, unit spacing, no $\rho$).
  5. Mixed Schur: operator norm $\le\sqrt{M_1M_2}=\sqrt{(C\rho^{-d/2})(C\rho^{d/2})}=C$, radius-independent.
  6. Recovery is the transpose with roles reversed; then density (Schwartz on $\R^d$, torus polynomials on $\T_L$) extends to all $H^r$, negative $r$ included, distributionally without point-sampling rough Fourier data.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The added paragraph states: substitution $\rho\xi-k$ contributes $\rho^{-d}$; times kernel's $\rho^{d/2}$ gives $\rho^{-d/2}$; the sum variable has unit lattice spacing so no $\rho$-dependent lattice density; product radius-independent before the square root. This is exactly the correct bookkeeping (no invented Riemann-sum $\rho^d$ on the lattice side).
- Evidence: \(L^{-d/2}\widehat{\phi_\rho}(k/\rho-\xi)=(2\pi\rho)^{-d/2}\rho^d\widehat{\phi_0}(k-\rho\xi)\propto\rho^{d/2}\widehat{\phi_0}(k-\rho\xi)\); \(\int F_r(k-\rho\xi)d\xi=\rho^{-d}\|F_r\|_1\); \(\sup_\xi\sum_k F_r(k-\rho\xi)<\infty\) uniform by `E:cutoff-lattice-sum`.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read. The only cosmetic point is writing $\rho\xi-k$ where the free kernel uses $k-\rho\xi$; the $\pm$ in $F_r$ absorbs the reflection.

## P:radius-compact-envelopes
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Full-domain factorization: $\chi_\rho\psi_\rho=\chi_\rho$ (since $\psi_0=1$ near $\operatorname{supp}\chi_0$) gives $\Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma}=\Lambda^\sigma\mathcal{E}_{\chi_\rho}\mathcal{I}_\gamma\mathcal{P}_{\psi_\rho}\Lambda^{-\sigma-\gamma}$ on all of $L^2(\R^d)$, negative $\sigma$ included, by `L:cutoff-factorization` and density.
  2. Inclusion: $\mathcal{I}_\gamma:H^{\sigma+\gamma}(\T_L)\to H^\sigma(\T_L)$ has normalized diagonal values $\langle k/\rho\rangle^{-\gamma}$; the two Bessel powers $\Lambda^{-\sigma-\gamma}:L^2\to H^{\sigma+\gamma}$ and $\Lambda^\sigma:H^\sigma\to L^2$ are unitary (isometric), so they do not alter singular values.
  3. Cube/volume comparison with $u=q\gamma>d$: for $x\in k+[-1/2,1/2]^d$, $\langle x/\rho\rangle\le\sqrt2\langle k/\rho\rangle\langle(x-k)/\rho\rangle\le\sqrt{2(1+d/4)}\langle k/\rho\rangle=c_d'\langle k/\rho\rangle$ (using $|x-k|\le\sqrt d/2$ and $\rho\ge1$). Hence $\langle k/\rho\rangle^{-u}\le(c_d')^u\langle x/\rho\rangle^{-u}$; summing unit-cube integrals and substituting $y=x/\rho$ gives $\sum_k\langle k/\rho\rangle^{-u}\le(c_d')^u\rho^d\int_{\R^d}\langle y\rangle^{-u}dy\le C_{d,u}\rho^d$ (`E:radius-lattice-volume`), finiteness from dyadic terms $C_d2^{j(d-u)}$, $d-u<0$.
  4. Rank transfer: sort diagonal values decreasing $(\lambda_j)$; retaining $j-1$ coordinates has rank $<j$ and norm error $\lambda_j$; composing with bounded outer maps gives $s_j\le C_{\chi_0,\sigma}C_{\psi_0,\sigma+\gamma}\lambda_j$ by the min-max argument of `P:cutoff-singular-values`; finite-rank approximation gives compactness.
  5. Sum powers then root: $\sum_j s_j^q\le C^q\sum_k\langle k/\rho\rangle^{-q\gamma}=C^q\sum_k\langle k/\rho\rangle^{-u}\le C^qC_{d,u}\rho^d$, so $\|K\|_{S_q}\le C\rho^{d/q}$ (`E:radius-cutoff-Schatten`). Correct exponent: $(\rho^d)^{1/q}=\rho^{d/q}$, not $\rho^d$.
  6. Balanced envelopes: $K_{\rm out}=P_{\chi_\rho}D_\gamma$ has blocks $\Lambda^{1/2}\chi_\rho\Lambda^{-1/2-\gamma}$ and $\Lambda^{-1/2}\chi_\rho\Lambda^{1/2-\gamma}$ (i.e. $\sigma=\pm1/2$); their $q$th powers add as a multiset union, giving $\|K_{\rm out}\|_{S_q}^q\le2C^q\rho^d$; `P:compact-two-envelopes` gives $K_{\rm in}=VK_{\rm out}V$ for unitary swap $V(z_1,z_2)=(z_2,z_1)$, so equal norms (`E:radius-two-envelopes`).
  7. Endpoint remark: $\gamma<1/2$ and $q\gamma>d$ force $q>2d\ge2$; no Hilbert–Schmidt ($q=2$) conclusion; $P_{\chi_\rho}$ and its adjoint are not assumed selfadjoint/idempotent.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The added Step 2 sentence "the unit cubes partition Euclidean space and each has volume one... substituting $y=x/\rho$ gives the factor $\rho^d$; taking a $q$th root later gives $\rho^{d/q}$" is precisely correct and guards against an unpowered sum or doubled exponent.
- Evidence: \(c_d'=\sqrt{2(1+d/4)}\); \(\int_{\R^d}\langle y\rangle^{-u}dy<\infty\) for $u=q\gamma>d$; \(\rho^{d/q}=((c_d')^u\rho^d\int\langle y\rangle^{-u}dy)^{1/q}\).
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read. Constant dependence: $C_{\sigma,\gamma,q,d,\chi_0,\psi_0}$ and $C_q$ depend on the cutoff profiles, Sobolev/Schatten indices and dimension; independent of $\rho$.

## P:radius-actual-moments
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Coefficients: $g_j=W(f_j)$ from `L:driver-noise-basis`, finite paths $M_N=\sum_{j\le N}g_jA_j$, same original noise (not source approximations).
  2. Envelope choice: $\rho=2R+B+2\le(B+4)R$ (since $R\ge1$ forces $B+2\le BR+2R$), $\chi=\chi_0(\cdot/\rho)$; the plateau covers $B_{2R+B+1}$, so both localization identities `E:driver-actual-localization` hold; physical noise mask remains $m_R$; both envelopes use $\chi_\rho$.
  3. Increment estimate: for $I\subset[0,B]$, $0<h=|I|\le1$, `P:wave-two-variances` + `L:driver-actual-variances` give both weighted variances $\le V_{B,{\rm var}}h^{2-a}B_\alpha(h)$ uniformly in $R,N,I$, with base mask $\zeta=\eta^2$. `C:finite-gaussian-operators` in balanced coordinates gives, for even $q\ge Q$,
     \[
     \|M_N(I)\|_{L^q(S_q)}\le\sqrt{q-1}\sqrt{V_{B,{\rm var}}}\,h^{1-a/2}B_\alpha(h)^{1/2}\|K_{\rm out}\|_{S_q}.
     \]
  4. Freezing the radius exponent: for $q\ge Q$, $\|K_{\rm out}\|_{S_q}\le\|K_{\rm out}\|_{S_Q}$: normalize the singular-value sequence by its $\ell^Q$ norm, then every entry is $\le1$ so $s_i^q\le s_i^Q$ and $\sum s_i^q\le\sum s_i^Q$. Applying `E:radius-two-envelopes` only at fixed $Q$ and $\rho^{d/Q}\le(B+4)^{d/Q}R^{d/Q}$, together with $\|A\|\le\|A\|_{S_q}$, $\sqrt{q-1}\le\sqrt q$, yields `E:radius-finite-increment`:
     \[
     \|M_N(t)-M_N(u)\|_{L^q(\mathcal L(E))}\le C_{Q,B}\sqrt q\,R^{d/Q}|t-u|^{\beta_t},\quad |t-u|\le1.
     \]
     Branch check: $h^{1-a/2}B_\alpha(h)^{1/2}$ with $B_\alpha^{1/2}=1$, $\sqrt{1+\log(1/h)}$, $h^{(1-\alpha)/2}$ respectively; strict gaps $\beta_t<1-a/2$ (resp. $< (3-a-\alpha)/2$) give strict absorption: $\alpha=1$: $h^{1-a/2}\sqrt{1+\log(1/h)}=h^{\beta_t}h^{\delta}\sqrt{1+\log(1/h)}\le C h^{\beta_t}$ for $\delta=1-a/2-\beta_t>0$; $\alpha>1$: exponent $1-a/2+(1-\alpha)/2=(3-a-\alpha)/2>\beta_t$.
  5. Dyadic chaining: $D_n$ largest adjacent increment on grid $kB2^{-n}$; for $B2^{-n}\le1$,
     \[
     \|D_n(M_N)\|_{L^q}\le 2^{n/q}C_{Q,B}\sqrt q\,R^{d/Q}(B2^{-n})^{\beta_t}
     \]
     (finite maximum into $L^q$: $\|\max_k X_k\|_q\le2^{n/q}\|X_k\|_q$, no independence). The $\eta_t$-weighted sum has geometric ratio $\le2^{-(\beta_t-\eta_t-1/Q)}<1$ since $1/q\le1/Q$; coarse levels are finitely many. `L:driver-holder-limit` then bounds $\|M_R\|_{L^qC^{\eta_t}}\le C_{Q,B}\sqrt q R^{d/Q}$, and $C^{\eta_t}\hookrightarrow C^\theta$ since $\theta<\eta_t$.
  6. Limit: for fixed $R$, `L:driver-holder-limit` identifies $M_R(W)$ as the all-finite-moment $C^\theta$ limit of these $M_N$; pass the uniform-in-$N$ bound. Correctly avoids radius-uniform convergence: "Uniform convergence in $R$ is unnecessary."
  7. Arbitrary $v$: choose even $q\ge\max(v,Q)$ with $q\le v+Q+2\le(Q+3)v$; Lyapunov gives `E:radius-actual-path-moments`, absorbing $\sqrt{Q+3}$ into $C_{Q,B}$, so the constant is independent of $v$ and $R$.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The Step 3 addition ("Using the envelope estimate only at Q is what prevents its constant from varying with the moment index q... The only remaining moment dependence... is the explicit √q") is exactly the correct mechanism.
- Evidence: `E:radius-two-envelopes` at $Q$ gives $C_Q\rho^{d/Q}\le C_Q(B+4)^{d/Q}R^{d/Q}$; monotonicity $\|K_{\rm out}\|_{S_q}\le\|K_{\rm out}\|_{S_Q}$ freezes $R^{d/Q}$; the geometric-summation condition $\beta_t-\eta_t-1/Q>0$ comes from `E:radius-anchor-Q`.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: the proof is an $E$ operator-path estimate and explicitly excludes the $F$ constant columns (stated in the proposition). The variance-$N,I$-uniformity leans on `P:wave-two-variances` (uniform in $R$) and `L:driver-actual-variances` (uniform in $N$); these are unassigned upstream statements whose hypotheses (mask $m_R$, localization by $\chi_\rho$) are checked here. `V_{B,\rm var}` is introduced inline as the uniform variance budget (upstream $C_T$ at horizon $B$); cosmetic naming only.

## C:radius-covariance-residuals
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE (unchanged proof; still reconstructed)
- Original-step coverage:
  1. `P:source-gaussian-transfer` is a covariance-contraction theorem for this same physical mask and deterministic coefficient maps; its norm comparison `E:source-transfer-norm` gives $\|M_R(Y)\|_{L^v}\le\sqrt C\,\|M_R(W)\|_{L^v\mathscr B_\theta}$. This is a reference-*law* comparison on the same coupling; $Y$ is not replaced.
  2. Substituting `E:radius-actual-path-moments` gives $\|M_R(Y)\|_{L^v(C^\theta)}\le\sqrt C\,C_{Q,B}\sqrt v\,R^{d/Q}$; the zero case ($C=0$) is immediate.
  3. Second assertion: for $Y_m(f)=W((I-\Pi)T_{\delta,m}f)$, linearity of $W$ gives $\operatorname{Var}Y_m(f)=\|(I-\Pi)T_{\delta,m}f\|^2_{H_W}\le\|T_{\delta,m}f\|^2_{H_W}$ by $\|I-\Pi\|\le1$; the pullback `E:raw-block-pullback` is an isometry (`L:raw-block-inputs`), so this is $\le\|f\|^2_{H_W}$ in the original (fast) norm — i.e. $C=1$. Π is deterministic (orthogonal projection on slow $H_W$), possibly infinite-rank and $(\delta,R)$-dependent; no random projection is used.
  4. Qualifiers retained: joint residuals keep the given slow $W$ and may be correlated; they need not lie in the span of one fast noise, which is not a hypothesis of Gaussian transfer.
- Argument preservation: PRESERVED
- New explanations: none added (byte-identical proof).
- Evidence: $\|(I-\Pi)T_{\delta,m}f\|\le\|T_{\delta,m}f\|=\|f\|$ (isometry); `E:source-transfer-norm` with reference bound $C_{Q,B}\sqrt v R^{d/Q}$.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read. The clause "where the right side is the original norm in fast coordinates" is an interpretation note consistent with `L:raw-block-inputs`.

## P:radius-mean-anchor
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Stopping at $\ell_m$ and extending constantly to $B$ does not increase sup or Hölder seminorm; an empty last interval ($\ell_N=0$) gives the zero path.
  2. Each block: by `C:radius-covariance-residuals` with $C=1$ at moment index $p\ge1$, $\|X_m\|_{L^p(C^\theta)}=g_\delta\|M_R(Y_m)\|_{L^p(C^\theta)}\le g_\delta C_{Q,B}\sqrt p\,R^{d/Q}$, hence $\E\|X_m\|_{C^\theta}^p\le(g_\delta C_{Q,B}\sqrt p\,R^{d/Q})^p$.
  3. Lyapunov/Jensen and linearity of the finite-sum expectation (no independence, no maximum):
     \[
     \E Z_\delta\le(\E Z_\delta^p)^{1/p}=\Big(\delta\sum_{m=0}^N\E\|X_m\|_{C^\theta}^p\Big)^{1/p}\le[\delta(N+1)]^{1/p}g_\delta C_{Q,B}\sqrt p\,R^{d/Q}.
     \]
     The aggregate is exactly $Z_\delta=(\delta\sum_m\|X_m\|^p)^{1/p}$, so $Z_\delta^p=\delta\sum_m\|X_m\|^p$.
  4. Since $\delta B<1$: $N=\lfloor1/(\delta B)\rfloor\ge1$ and $N+1\le1/(\delta B)+1\le2/(\delta B)$, so $[\delta(N+1)]^{1/p}\le(2/B)^{1/p}$, proving `E:radius-mean-anchor`.
  5. Numerical decay: $R_\delta=\delta^{-1}+2\le3/\delta$ (since $\delta<1$); $g_\delta R_\delta^{d/Q}=\delta^{(1-a)/2}R_\delta^{d/Q}\le3^{d/Q}\delta^{(1-a)/2-d/Q}=3^{d/Q}\delta^{e_{\rm anchor}}$. The last condition of `E:radius-anchor-Q` is $Q>2d/(1-a)\iff Q(1-a)>2d\iff e_{\rm anchor}=(1-a)/2-d/Q>0$, giving `E:radius-mean-anchor-decay` with $B,p,Q$ fixed. Uniform in the deterministic residual projection.
  6. Closing qualifiers (unchanged): this is an $E$ estimate, not an $F$ estimate; the radius substitution is numerical; cone coverage and source-to-point transfer need separate arguments; no concentration, integration over infinite Gaussian coordinates, or nonlinear moment bound follows.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The added paragraph explains that $\delta(N+1)$ (from the finite expectation sum, not from a maximum) is reduced to $2/B$ before radius substitution, so no independence assumption offsets the growing block count. Correct: the prefactor is $[\delta(N+1)]^{1/p}\le(2/B)^{1/p}$, $\delta$-independent.
- Evidence: \(R_\delta^{d/Q}\le(3/\delta)^{d/Q}=3^{d/Q}\delta^{-d/Q}\); \(g_\delta\delta^{-d/Q}=\delta^{(1-a)/2-d/Q}=\delta^{e_{\rm anchor}}\); \(e_{\rm anchor}>0\iff Q(1-a)>2d\).
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: the statement's "2" prefactor is cosmetic (doubling both sides of a valid bound). The "zero covariance" case is covered by the module's closing sentence ("operator paths and stochastic bounds vanish directly") and the corollary's $C\ge0$ handling.

## AUDIT dispositions
- All five statements: byte-identical between OLD and NEW (line shifts from purely additive proof growth: +10/+19/+24/0/+4).
- Proof 1, 2, 3, 5: additive explanatory rewrites; all added text mathematically verified.
- Proof 4: unchanged; still fully reconstructed and checked.
- No new rewrite defects found; no silent repairs detected; no invented lattice density, unpowered sum, doubled exponent, independence assumption, maximum-over-blocks, radius-uniform convergence, or $F$-estimate conversion introduced.
- Pre-existing contextual facts (not defects of the rewrite): dependence on unassigned upstream results `L:cutoff-factorization`, `P:cutoff-singular-values`, `P:compact-two-envelopes`, `P:wave-two-variances`, `L:driver-actual-variances`, `C:finite-gaussian-operators`, `P:source-gaussian-transfer`, `L:raw-block-inputs`, `L:driver-holder-limit`; all application hypotheses were checked where visible (mask $m_R$, base profile $\eta^2$, localization by $\chi_\rho$, both variance directions, isonormal reference law).

## Findings and limits
This is independent rewrite-preservation review of five proof pairs in one module, not a certification of the whole book, the unassigned upstream modules, the source PDFs, Lean correspondence, or any release. Old was not treated as an oracle; all five deductions were reconstructed from checkable equations and estimates. Verdict PASS at high confidence: readability-equivalence holds, with all new explanations justified and every mandated derivation (kernel $(2\pi)$ factors, $\rho^{d/2}/\rho^{-d/2}/\rho^{d/2}$ bookkeeping, unit-cube $\rho^d$ volume with $q$th root, fixed-$Q$ Schatten freezing, dyadic ratio $\beta_t-\eta_t-1/Q$, deterministic ℓ^p anchor aggregation with exponent $(1-a)/2-d/Q$) publicly verified. Remaining limitations are the ordinary upstream dependencies and the self-declared scope of the section (no $F$ column, cone, source-to-point, or nonlinear moment claims), all of which are honestly flagged in the source text itself.
