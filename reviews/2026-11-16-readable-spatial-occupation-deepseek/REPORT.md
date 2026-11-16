# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

Scope: exactly the 8 assigned proof labels in
`notes/integrated_spatial_occupation.tex`, comparing OLD
`cdde711c…` (whole module) with NEW `bc531b02…` (whole module), using the
supplied baseline contexts as unchanged inputs. Imported results are accepted
at their stated hypotheses; I did not re-certify their external proofs. All 8
old and new proofs were read completely.

## L:spatial-physical-pair
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD and NEW proofs are byte-identical on LF 25–34, and the
  statements on LF 13–23 are unchanged. The sigma-finiteness argument
  (exhausting balls for $\Gamma$, sigma-finite Lebesgue), Tonelli first in
  $x$ killing $\nu\{x\in N\}$ and $\nu\{x-y\in N\}$ for Borel Lebesgue-null
  $N$ (a fixed translate of $N$ is null), and the Borel-null-superset step for
  arbitrary versions all remain. The stipulation that signed pairings are used
  only after absolute convergence is retained.
- Lost steps/qualifiers: none identified within this read.

## L:spatial-static-controls
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 58–98 expanded to NEW LF 58–125 by inserting Step 1–3
  headings and two justifications. (i) The square-root Lipschitz step is now
  spelled out: $|\sup F_c-\sup F_{c'}| \le |c-c'|\|U_z\|_\infty$, then
  $| \sqrt{\lambda_z(c)^2}-\sqrt{\lambda_z(c')^2}|
  = |\lambda_z(c)^2-\lambda_z(c')^2|/(\lambda_z(c)+\lambda_z(c'))$, with a
  positive denominator floor on a compact positive $c$ interval; this is valid
  because $U_z\ge0$ and $c\mapsto \lambda_z(c)^2$ is nondecreasing. (ii) The
  monotone-cutoff assertion is justified: $\chi$
  (from P:variational-remove-mask) is nonincreasing, $1/(nt)$ decreases in
  $n$, so both factors increase, and $\chi\to1$ at argument $0^+$; monotone
  convergence plus \eqref{E:temporal-equilibrium-potential} gives
  $k_n(s)\uparrow1$ for every $s\in[0,1]$, and $c_0=\int_0^1f_4>0$ keeps
  $k_n(s)\in[c_0,1]$. The cost identity
  $v_{\Psi_n}=B_\Gamma(z,z)\int_0^1f_n(s)k_n(s)\mathrm{d}s$ and the limit
  $M_aB_\Gamma(z,z)$ are unchanged. The final sentence the variational
  differences need not increase is retained.
- Lost steps/qualifiers: none identified within this read.

## L:spatial-fourier-bound
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 116–167 expanded to NEW LF 143–216. The added Step 2
  derivation is correct: for $|\xi|^2\le4b$,
  $8b/(4b+|\xi|^2)\ge1$ and the mass bound $|\mathcal{F}_0Q|\le1$ applies;
  for $|\xi|^2>4b$ the derivative bound gives
  $|\mathcal{F}_0Q|^2\le4b/|\xi|^2\le8b/(4b+|\xi|^2)$ because
  $4b\le|\xi|^2$. The resolvent step is unchanged, and the constant checks:
  $8b\,\mathcal{R}_\Gamma(2\sqrt b)=8b(2\sqrt b)^{\alpha-2}R_\alpha
  =2^{1+\alpha}R_\alpha b^{\alpha/2}$. The spectral identity uses the
  unnormalized $\mathcal{F}_0Q$, avoiding spurious $c_d$ factors; the
  $\Gamma=0$ clause ($\mu=0$, both sides vanish) is preserved.
- Lost steps/qualifiers: none identified within this read.

## P:spatial-smooth-ratio
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 188–226 expanded to NEW LF 237–296. The added Step 2
  verification is algebraic and correct: with $u=\alpha/q$,
  $\ell^2b=uL^2$ and $\theta\ell^\alpha A=(1+u)L^2$, so the radicand is
  $L^2$; then
  $\theta^2\ell^\alpha A=(1+u)^2L^4/(\ell^\alpha A)$ and, since
  $\ell^\alpha A=u^{\alpha/2}L^\alpha R(g)$, this is the claimed coefficient
  $C$ in $L-CL^q$ with $q=4-\alpha$. The added derivative computation is
  correct: $1-qCL^{q-1}$ changes sign once, at which point
  $CL^q=L/q$, giving the value $(k/q)(qC)^{-1/k}$. The algebra
  $1+u=4/q$ and $1/(q^qC)=R(g)\alpha^{\alpha/2}/(8M_aq^{q/2})$ matches
  \eqref{E:spatial-smooth-score}.
- Lost steps/qualifiers: none identified within this read.

## P:spatial-four-linear
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 253–312 expanded to NEW LF 323–407. The added Step 3
  telescoping explanation is justified: a single-coordinate difference of the
  four-linear form is bounded by
  $R_0N(f_j-g_j)N(f_{i_1})N(f_{i_2})N(f_{i_3})$; the three unchanged
  arguments stay bounded in $H^1$ and the difference factor tends to zero.
  This provides the continuity used to transfer positive semidefiniteness from
  smooth compact squares to finite linear combinations of $H^1$ squares
  (and hence \eqref{E:spatial-square-CS}). Step 4 keeps the strict positivity
  argument via the indicator correlation near zero, with the explicit note
  that no $H^1$ claim is made for $1_E$.
- Lost steps/qualifiers: one pre-existing proof-text imprecision (not
  rewrite-introduced): the sentence “The homogeneous bound gives
  $R_{\mathrm{sp}}\le R_0$” is not the direct mechanism, since for a general
  unit $H^1$ profile \eqref{E:spatial-homogeneous-bound} yields
  $A\le R_0b^{\alpha}$, i.e.\ ratio $\le R_0b^{\alpha/2}$, which may exceed
  $R_0$ for $b>1$. The conclusion $R_{\mathrm{sp}}\le R_0$ is nonetheless
  valid by the immediately following “normalized smooth approximations
  preserve the ratio by continuity” argument. Both the wording and the
  correcting continuity sentence are identical in OLD and NEW.

## P:spatial-energy-map
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 346–367 expanded to NEW LF 441–470. The added derivative
  checks are correct: $\mathrm{d}/\mathrm{d}\ell(\ell^\alpha A-\ell^2b/2)
  =\alpha A\ell^{\alpha-1}-b\ell$, whose positive zero is
  $\ell^{2-\alpha}=\alpha A/b$; there $b\ell^2=\alpha A\ell^\alpha$, giving
  the critical value $(1-\alpha/2)A\ell^\alpha$, and substituting the critical
  scale produces
  $\frac{2-\alpha}{2}\alpha^{\alpha/(2-\alpha)}R(g)^{2/(2-\alpha)}$.
  For $0<\alpha<2$ the derivative factor is positive at $0^+$ and negative at
  $\infty$, so this is the global maximum. The substitution leading to
  \eqref{E:spatial-static-energy-score} and the statement that no optimizer is
  assumed are unchanged.
- Lost steps/qualifiers: none identified within this read.

## L:occupation-kernel-row
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 393–401 and NEW LF 496–504 are identical. The damped
  comparison kernel \eqref{E:occupation-damped-kernel} is kept distinct from
  the original temporal kernel $|s-t|^{-a}$; dropping the quadratic damping
  gives $K_\star(u)\le|u|^{-a}$. Positivity, monotonicity, $a<1$ local
  integrability, and the concavity of $\Phi$ (because
  $\Phi'=K_\star$ is decreasing) remain. The row is
  $\Phi(s)+\Phi(1-s)\le2\Phi(1/2)$, so
  $R_\star=2\int_0^{1/2}K_\star(u)\,\mathrm{d}u$, with the diagonal value
  $K_\star(0)=0$ changing no time integral.
- Lost steps/qualifiers: none identified within this read.

## P:occupation-physical-class
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 429–465 expanded to NEW LF 532–584. Step 1 (measurability,
  separably valued representative, simple-$H^1$-valued Bochner approximation,
  representative independence via L:spatial-physical-pair) is unchanged.
  Step 2 retains $F(s)=b(g_s)^{\alpha/4}$, the concavity step
  ($0<\alpha/2<1$ gives $\int_0^1b(g_s)^{\alpha/2}\le T(g)^{\alpha/2}$), the
  bound $2F(s)F(t)\le F(s)^2+F(t)^2$, evenness of $K_\star$, and positive
  Tonelli before finiteness. Step 3 retains the scalar maximum
  $R_\star^{2/(2-\alpha)}\mathcal{E}_{\mathrm{sp}}$ and the positivity test:
  a constant-in-time unit compact profile with dilation $U_\ell$ has
  $J=J_0\ell^\alpha A_{\mathrm{sp}}(g)$ with
  $J_0=\iint_{[0,1]^2}K_\star(s-t)\,\mathrm{d}s\,\mathrm{d}t\in(0,\infty)$
  and $T=\ell^2b(g)$, so $J-T/2>0$ for small $\ell$ since $\alpha<2$. The
  full class (no time smoothness, no common compact support, no optimizer) is
  retained, as is the zero-covariance paragraph after the proof.
- Lost steps/qualifiers: one pre-existing proof-text imprecision (not
  rewrite-introduced): “Equations \eqref{E:spatial-homogeneous-bound} and
  \eqref{E:spatial-square-CS} give
  $B_\Gamma(g_s^2,g_t^2)\le R_{\mathrm{sp}}F(s)F(t)$” — those two equations
  alone give $B\le R_{\mathrm{sp}}F(s)^2F(t)^2$. The stated bound follows
  instead from the ratio-supremum definition (for unit $g_s$,
  $A_{\mathrm{sp}}(g_s)\le R_{\mathrm{sp}}b(g_s)^{\alpha/2}$) together with
  \eqref{E:spatial-square-CS}. The displayed bound and the subsequent
  $J$-estimate are correct; only the cited source is imprecise. Both OLD and
  NEW carry the identical sentence.

## AUDIT dispositions
No AUDIT-marked material remains in this module, and I found no
rewrite-introduced AUDIT-worthy defect. The two pre-existing proof-text
citation issues noted under P:spatial-four-linear and
P:occupation-physical-class are carried verbatim from OLD and are
readability/attribution issues rather than false conclusions; they do not
arise from the NEW revision.

## Findings and limits
All 8 assigned proofs were read completely in both revisions; no PARTIAL or
NOT_READ designation applies. Arguments and statements are preserved, the NEW
explanatory assertions are justified under the same hypotheses, and no step,
qualifier, exponent, endpoint case, zero-covariance case, or limit was lost.
The NEW revision only inserts step headings and local justifications; no
equation, hypothesis, class, or constant is changed. The occupation energy
continues to use the damped comparison kernel $K_\star$, not the original
temporal kernel, consistent with the surrounding definitions. Imported
finiteness results (P:variational-unmasked-rate, E:temporal-equilibrium,
L:damped-homogeneous-norms, E:intro-spectral-mass, E:masked-spectral-convention)
are consumed under their stated conditions; I did not independently certify
their primary-source proofs. The scope is internal argument-preservation and
readability, not whole-book truth or render fidelity.
