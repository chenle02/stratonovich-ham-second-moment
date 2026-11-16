# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

The rewrite preserves every statement, hypothesis qualifier, exponent, endpoint case and limit
seen in the old module. Added material is explanatory structuring, differentiation detail,
resolvent scalar-integral detail, cost-substitution detail, and one explicit citation of an
upstream ball-charge fact. I checked the added explanations algebraically; all are justified
under the same hypotheses. No step or qualifier was lost. No AUDIT-worthy issue was found in
the assigned scope.

## L:spatial-physical-pair
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Sigma-finiteness: `\nu(dx,dy)=dx \Gamma(dy)`; `\Gamma` is locally finite (Radon), so
     exhausting balls have finite `\Gamma`-mass; Lebesgue measure is sigma-finite; the product
     is sigma-finite.
  2. Null transfer at the `x` coordinate: for Borel `N` with `Leb(N)=0`,
     `\nu\{x\in N\}=\int \Gamma(dy) Leb(N)=0`, because integrating first in `x` makes the
     inner Lebesgue mass vanish.
  3. Null transfer at the `x-y` coordinate: for each fixed `y`, `\{x: x-y\in N\}=N+y` has
     Lebesgue measure zero, so `\nu\{x-y\in N\}=\int \Gamma(dy)Leb(N)=0`.
  4. Every Lebesgue-null set has a Borel null superset, so arbitrary representatives differ on
     a `\nu`-null set and are measurable in the `\nu`-completion with the same
     `\eqref{E:spatial-physical-pair}` value.
  5. The same argument applies to the exception set of an a.e. convergent sequence, so
     Lebesgue-a.e. convergence transfers to `\nu`-a.e. convergence at both `x` and `x-y`.
  6. Signed integrands are admitted only after absolute convergence.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (none added; the proof is byte-for-byte the same aside from
  formatting at the same local LFs).
- Evidence: old statement 13–23 = new statement 13–23; old proof 25–34 = new proof 25–34.
  The Tonelli checks in steps 2–3 are exactly the ones stated in the proof; no normalization
  constant appears because this is a measure identity, not a Fourier inversion.
- Lost steps/qualifiers: none identified within this read.

## L:spatial-static-controls
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Static rate: take `f\in C_c^\infty(0,1)` nonnegative nonzero and `s_0=1/2`; the test
     `\Psi(t,x)=c f(t)z(x)/k_f(s_0)` has mean `cU_z` at `s_0`. Input
     `P:variational-unmasked-rate` applies since `\Psi` is a nonnegative compact smooth
     control; it gives boundedness of the potential, the displayed real Rayleigh formula
     `\eqref{E:variational-real-rayleigh}`, and positivity of the rate for each `c>0`.
  2. Lipschitz bound: for unit `g`, `q_c(g)-q_d(g)=(c-d)\int U_z g^2`, so comparing the
     same unit tests gives `|\lambda_z(c)^2-\lambda_z(d)^2|\le |c-d|\,\|U_z\|_\infty`.
     Positivity on a compact `c`-interval gives a positive floor, hence
     `|\lambda_z(c)-\lambda_z(d)|\le |c-d|\|U_z\|_\infty/(2\inf_{I}\lambda_z)`.
  3. Equilibrium approximation: `f_n=f_a\chi(1/(nt))\chi(1/(n(1-t)))` is smooth compact,
     nonzero, vanishes near both endpoints, and increases to `f_a`; hence
     `k_n(s)\uparrow 1` by `\eqref{E:temporal-equilibrium-potential}`. Since
     `|s-t|^{-a}\ge 1` off the diagonal, `0<c_0=\int_0^1 f_4\le k_n(s)\le 1`.
  4. Rate convergence: `I_{\Psi_n}=\int_0^1\lambda_z(k_n(s))ds\to\lambda_z(1)` by continuity
     of `\lambda_z` and dominated convergence with the constant bound `\lambda_z(1)`.
  5. Cost: the nonnegative Tonelli pairing is
     `v_{\Psi_n}=B_\Gamma(z,z)\int_0^1 f_n(s)k_n(s)ds`; `f_nk_n\uparrow f_a`, so the cost
     tends to `M_aB_\Gamma(z,z)`. The spatial factor is positive and finite via the positive
     autocorrelation of `z` near zero and homogeneity, which transfers positive mass of some
     origin-centered ball to every positive radius.
  6. Passing to the limit in `S_1^{\mathrm{pos}}\ge I_{\Psi_n}-v_{\Psi_n}/2` gives
     `\eqref{E:spatial-static-score}`. The two limiting quantities exist separately; the
     proof correctly notes the differences need not be monotone.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The added introductory paragraph and Steps 1–3 only reorganize
  the same arguments; the explicit phrase “pass their rewards and costs to the limit
  separately” matches the old limit step and is valid because both limits exist.
- Evidence: old proof 58–98 vs new proof 58–115; statement 42–56 identical in both.
  The identity `v_{\Psi_n}=B_\Gamma(z,z)\int f_n k_n` follows from
  `\int z(x)z(x-y)dx = c_z(y)` and
  `\int\int f_n(s)f_n(t)|s-t|^{-a}dsdt=\int f_n(s)k_n(s)ds`.
- Lost steps/qualifiers: none. Upstream inputs (`P:variational-unmasked-rate`,
  `P:variational-remove-mask`, `L:temporal-equilibrium`) are used under their stated
  hypotheses (`z` compact nonnegative nonzero, `\Gamma` nonzero, `0<a<1`).

## L:spatial-fourier-bound
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. `b=0` forces `\nabla g=0`, so `g` is constant and, with compact support, `g=0`,
     contradicting `\|g\|_2=1`; hence `b>0`.
  2. Set `Q=g^2`; define unnormalized `\mathcal F_0Q(\xi)=\int e^{-i\xi\cdot x}Q(x)dx`,
     which is `c_d^{-1}\widehat Q` with `c_d=(2\pi)^{-d/2}` in the unitary convention.
  3. The autocorrelation `c_Q(y)=\int Q(x)Q(x-y)dx` is smooth compact. Apply
     `\eqref{E:masked-spectral-convention}`; for real `Q` the inner Fourier integral is
     `|\mathcal F_0Q(\xi)|^2`, so
     `A_{\mathrm{sp}}(g)=\int c_Q(y)\Gamma(dy)=\int|\mathcal F_0Q(\xi)|^2\mu(d\xi)`.
     Finiteness comes from `c_Q` compact/`\Gamma` Radon and `|\mathcal F_0Q|^2` Schwartz
     with `\mu` tempered.
  4. `\|Q\|_1=1` gives `|\mathcal F_0Q|\le 1`; integration by parts plus Cauchy–Schwarz gives
     `|\xi||\mathcal F_0Q(\xi)|\le\|\nabla Q\|_1\le 2\|g\|_2\|\nabla g\|_2=2\sqrt b`.
  5. Splitting `|\xi|^2\le 4b` vs `>4b` yields
     `|\mathcal F_0Q|^2\le 8b/(4b+|\xi|^2)`. On the low region the right side is `\ge 1`,
     so the mass bound applies; on the high region
     `(2\sqrt b/|\xi|)^2=4b/|\xi|^2\le 8b/(4b+|\xi|^2)` because `4b\le |\xi|^2`.
  6. Use the imported resolvent `\mathcal R_\Gamma(q)=\int\mu(d\xi)/(q^2+|\xi|^2)
     =q^{\alpha-2}R_\alpha<\infty`; apply it at `q=2\sqrt b`:
     `A\le 8b\mathcal R_\Gamma(2\sqrt b)=2^{1+\alpha}R_\alpha b^{\alpha/2}`.
     Nonnegativity is from the spectral identity; `\Gamma=0` makes `\mu=0` and both sides vanish.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The new Step-2 majorant sentence is correct. The new scalar
  identity in Step 3,
  `\int_0^\infty u^{\alpha-1}/(1+u^2)du=\tfrac12 B(\alpha/2,1-\alpha/2)
  =\pi/(2\sin(\pi\alpha/2))`,
  follows from `x=u^2` and `\Gamma(x)\Gamma(1-x)=\pi/\sin(\pi x)`; it is exactly the radial
  factor behind `R_\alpha`. The new warning that the resolvent parameter `q>0` is distinct
  from the fixed `q=4-\alpha` is a correct and useful clarification.
- Evidence: old statement 104–114/new 121–131; old proof 116–167/new 133–215. Exponent check:
  `8\cdot (2\sqrt b)^{\alpha-2}=2^3\cdot2^{\alpha-2}b^{(\alpha-2)/2}=2^{\alpha+1}b^{
  (\alpha-2)/2}`, multiplied by `b` gives `2^{\alpha+1}b^{\alpha/2}`.
- Lost steps/qualifiers: none. The resolvent computation itself is the unassigned input
  `L:damped-homogeneous-norms` + `E:intro-spectral-mass`; I verified only that it is invoked
  at `q>0` under `H:homog`, not re-proved it.

## P:spatial-smooth-ratio
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. `b(g)>0` via the Fourier-support argument; `g^2` nonnegative nonzero smooth compact gives
     `0<A:=A_{\mathrm{sp}}(g)<\infty` by the same autocorrelation/ball-charge argument as
     `L:spatial-static-controls`. `L:spatial-fourier-bound` gives
     `R(g)\le 2^{1+\alpha}R_\alpha`; a normalized compact bump gives a positive value; hence
     `0<R_0<\infty` independently of the finiteness of `S_1^{\mathrm{pos}}`.
  2. Dilation: for `U_\ell g(x)=\ell^{d/2}g(\ell x)`,
     `A_{\mathrm{sp}}(U_\ell g)=\ell^\alpha A` and `b(U_\ell g)=\ell^2 b(g)`. Factors:
     `\ell^{2d}` (two squares), `\ell^{-d}` (from `dx`), `\ell^{\alpha-d}` (Radon pushforward),
     product `\ell^\alpha`.
  3. Control `z=\theta(U_\ell g)^2`. The test `U_\ell g` gives
     `\lambda_z(1)^2\ge \theta\ell^\alpha A-\ell^2b` and
     `B_\Gamma(z,z)=\theta^2\ell^\alpha A`.
  4. Set `u=\alpha/q`, `\ell^2=uL^2/b`, `\theta=(1+u)L^2/(\ell^\alpha A)`. Then
     `\theta\ell^\alpha A-\ell^2b=(1+u)L^2-uL^2=L^2`, so `\lambda_z(1)\ge L`.
     Also `\theta^2\ell^\alpha A=(1+u)^2L^{4-\alpha}/(u^{\alpha/2}R(g))`, hence
     `S_1^{\mathrm{pos}}\ge L-CL^q` with
     `C=M_a(1+u)^2/(2R(g)u^{\alpha/2})`.
  5. Maximizing `L-CL^q`: derivative `1-qCL^{q-1}=0`, so `L^k=1/(qC)`,
     `k=q-1`, and the maximum is `(k/q)(qC)^{-1/k}`. Since `1+u=4/q`, algebraic
     substitution gives
     `1/(q^q C)=R(g)\alpha^{\alpha/2}/(8M_a q^{q/2})`, proving
     `\eqref{E:spatial-smooth-score}`.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The new explicit sentences
  “`\theta^2\ell^\alpha A=(1+u)^2L^4/(\ell^\alpha A)`; replacing `\ell^\alpha A` by
  `u^{\alpha/2}L^\alpha R(g)`” are correct: `\ell^\alpha A=(\ell^2)^{\alpha/2}A
  =u^{\alpha/2}L^\alpha A/b^{\alpha/2}=u^{\alpha/2}L^\alpha R(g)`.
- Evidence: old proof 188–226/new proof 236–290; statement 175–186/223–234. Constant check:
  `(k/q)(qC)^{-1/k}=k q^{-1}q^{-1/k}C^{-1/k}=k q^{-q/k}C^{-1/k}` since `1+1/k=q/k`;
  and `q^q C=8M_a q^{q/2}/(R(g)\alpha^{\alpha/2})`, so the displayed score equals the
  maximum.
- Lost steps/qualifiers: none. The proof retains the note that only the finiteness proof of
  `R_0` is independent of the finiteness of `S_1^{\mathrm{pos}}`.

## P:spatial-four-linear
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Smooth square-pair bound: for `f=\lambda g` with unit `g`,
     `N(f)^4=\lambda^4\|\nabla g\|_2^{2\alpha/2}=\lambda^4 b(g)^{\alpha/2}` and
     `A_{\mathrm{sp}}(f)=\lambda^4A_{\mathrm{sp}}(g)\le\lambda^4R_0b(g)^{\alpha/2}`,
     so `\eqref{E:spatial-homogeneous-bound}` holds, including `f=0`. Also
     `N(f)\le\|f\|_{H^1}` by weighted AM–GM.
  2. Smooth signed covariance: `B_\Gamma(Q,Q)=\int|\widehat Q_{\mathrm{ord}}(\xi)|^2\mu(d\xi)
     \ge 0` by the spectral convention; symmetry from evenness of `\Gamma` and the change
     `(x,y)\mapsto(x-y,-y)`; the quadratic form `Q+tP` gives covariance Cauchy–Schwarz.
     Hence for smooth real `f,h`,
     `0\le B_\Gamma(f^2,h^2)\le\sqrt{A_{\mathrm{sp}}(f)A_{\mathrm{sp}}(h)}
     \le R_0N(f)^2N(h)^2`.
  3. Sobolev extension: `H^1` density via cutoff+mollification; separability via the closed
     isometric image `f\mapsto(f,\nabla f)` in `L^2(\R^d)^{d+1}`. Common a.e. subsequence of
     approximants; `L:spatial-physical-pair` transfers convergence at both positions to
     `\nu`-a.e.; Fatou and continuity of `N` give `B_\Gamma(f^2,h^2)\le R_0N(f)^2N(h)^2`.
     This supplies an inequality, not yet continuity.
  4. Four-linear bound: Cauchy–Schwarz under `\nu` with `f_1(x)f_3(x-y)` and
     `f_2(x)f_4(x-y)` gives
     `\int|f_1f_2f_3f_4|d\nu\le R_0\prod_{j=1}^4N(f_j)`, proving
     `\eqref{E:spatial-four-linear}` and absolute convergence. Multilinearity is direct;
     telescoping plus `N(f)\le\|f\|_{H^1}` gives joint continuity, so `A_{\mathrm{sp}}` and
     the square pairings are continuous.
  5. PSD passes to finite linear combinations of `H^1` squares by continuity; two-profile
     Cauchy–Schwarz gives `\eqref{E:spatial-square-CS}`.
  6. Ratio identity: `R_{\mathrm{sp}}\le R_0` from the homogeneous bound, and `\ge R_0`
     because smooth compact profiles are included; smooth approximations preserve ratios by
     continuity.
  7. Strict positivity: for nonzero `f`, choose bounded `E` with `|f|\ge c>0`; the
     correlation `c_E(y)` of `1_E` is continuous and positive near zero; some origin-centered
     ball has positive `\Gamma`-mass, so
     `A_{\mathrm{sp}}(f)\ge c^4B_\Gamma(1_E,1_E)>0`. This uses a nonnegative integral, not an
     `H^1` claim for `1_E`.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The added Step 4 sentence “As in `L:compact-raw-profile`,
  nonzero `\Gamma` gives positive mass to some origin-centred ball, and homogeneity rescales
  that ball to every positive radius” is exactly the content established in the upstream
  proof `L:compact-raw-profile` (under `\Gamma\neq0`, `H:homog`). Its hypotheses match the
  section-level nonzero-covariance assumption.
- Evidence: old proof 253–312/new proof 317–398; statement 233–251/297–315. The exponent
  bookkeeping `N(g)^4=\|\nabla g\|_2^\alpha=b^{\alpha/2}` is the key consistency check
  linking the homogeneous bound to the dilation exponents used later.
- Lost steps/qualifiers: none. The finite measure/`1_E` caution is retained verbatim.

## P:spatial-energy-map
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. `\eqref{E:spatial-dilation}` extends to real `H^1` profiles by continuity
     (`P:spatial-four-linear`) or by the usual Lebesgue change of variables.
  2. For fixed unit `g` with `A,b>0`, maximize `f(\ell)=A\ell^\alpha-(b/2)\ell^2`.
     Differentiating gives `f'(\ell)=\alpha A\ell^{\alpha-1}-b\ell`, whose positive zero
     satisfies `\ell^{2-\alpha}=\alpha A/b`. At the critical point
     `b\ell^2=\alpha A\ell^\alpha`, so the value is `(1-\alpha/2)A\ell^\alpha`; substituting
     `\ell^\alpha=(\alpha A/b)^{\alpha/(2-\alpha)}` gives
     `((2-\alpha)/2)\alpha^{\alpha/(2-\alpha)}(A/b^{\alpha/2})^{2/(2-\alpha)}
     =((2-\alpha)/2)\alpha^{\alpha/(2-\alpha)}R(g)^{2/(2-\alpha)}`.
  3. Dilation preserves the unit class and includes `\ell=1`; taking suprema in `\ell` and
     then in profiles with ratio approaching `R_{\mathrm{sp}}` gives
     `\eqref{E:spatial-energy-map}`. No optimizer is assumed.
  4. Solving for `R_{\mathrm{sp}}\alpha^{\alpha/2}`:
     `R_{\mathrm{sp}}\alpha^{\alpha/2}=(2\mathcal E_{\mathrm{sp}}/(2-\alpha))^{(2-\alpha)/2}`.
     Substituting into `\eqref{E:spatial-smooth-score}` gives
     `\eqref{E:spatial-static-energy-score}` with the stated `F_0`.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The added derivative sentence and the intermediate value
  `(1-\alpha/2)A\ell^\alpha` are correct and match the old closed-form optimum.
- Evidence: old proof 346–367/new proof 432–461; statement 319–344/405–430. The substitution
  check is shown in step 4 above; the exponent relation
  `1+\alpha/(2-\alpha)=2/(2-\alpha)` is what converts `A^{2/(2-\alpha)}b^{-\alpha/(2-\alpha)}`
  into `R^{2/(2-\alpha)}`.
- Lost steps/qualifiers: none. The statement still labels `F_0` as a scalar map and keeps the
  original temporal exponent `a`.

## L:occupation-kernel-row
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Dropping `\lambda^2/(2D)` gives `e^{-(\lambda+\lambda^2/(2D))|u|}\le e^{-\lambda|u|}`,
     so `K_\star(u)\le |u|^{-a}` by the Gamma integral
     `\Gamma_E(a)=\int_0^\infty e^{-\lambda|u|}\lambda^{a-1}d\lambda\cdot |u|^a`.
  2. Positivity and monotonicity on `(0,\infty)` follow from the positive, monotone integrand;
     `a<1` (from `0<\alpha_0<1`) gives local integrability. Evenness is direct from `|u|`.
  3. `\Phi(t)=\int_0^tK_\star(u)du` is concave because `K_\star` decreases on positive
     arguments.
  4. For `s\in[0,1]`, `\int_0^1K_\star(s-t)dt=\Phi(s)+\Phi(1-s)\le 2\Phi(1/2)`, with
     equality at `s=1/2`; the diagonal value is irrelevant to the time integral. Hence
     `\eqref{E:occupation-kernel-row}` with `R_\star=2\int_0^{1/2}K_\star(u)du\in(0,\infty)`.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (none added; proof text is identical at old 393–401/new 487–495).
- Evidence: statement old 383–391 = new 477–485. Finiteness of `R_\star` uses
  `\int_0^{1/2}u^{-a}du<\infty` since `a<1`; positivity uses `K_\star>0` off zero.
- Lost steps/qualifiers: none, including the `K_\star(0)=0` convention retained above the lemma.

## P:occupation-physical-class
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Measurability and representatives: `s\mapsto b(g_s)` is measurable; the field belongs to
     `L^2((0,1);H^1)` since `\int\|g_s\|_{H^1}^2ds=1+T(g)`. A separably valued strong
     representative with null times replaced by one fixed unit compact bump is available.
     Bochner approximation by simple `H^1`-valued functions with summable errors produces a
     measurable spacetime limit whose a.e. time slice represents `g_s`.
     `L:spatial-physical-pair` makes pairings version-independent, and the continuous pairing
     from `P:spatial-four-linear` gives a measurable function agreeing a.e. with the physical
     integral.
  2. Spatial-time bound: with `F(s)=b(g_s)^{\alpha/4}`,
     `B_\Gamma(g_s^2,g_t^2)\le\sqrt{A_{\mathrm{sp}}(g_s)A_{\mathrm{sp}}(g_t)}
     \le R_{\mathrm{sp}}F(s)F(t)`; the second inequality uses
     `\eqref{E:spatial-homogeneous-bound}` in the form
     `A_{\mathrm{sp}}(g_s)\le R_{\mathrm{sp}}N(g_s)^4=R_{\mathrm{sp}}b(g_s)^{\alpha/2}
     =R_{\mathrm{sp}}F(s)^2` (since `g_s` is unit).
  3. Concavity/row bound: `0<\alpha/2<1`, so
     `\int_0^1F(s)^2ds=\int_0^1b(g_s)^{\alpha/2}ds\le T(g)^{\alpha/2}`. Using
     `2F(s)F(t)\le F(s)^2+F(t)^2` and the row/column bound (same by evenness of `K_\star`)
     gives
     `J(g)\le R_{\mathrm{sp}}\int\int K_\star(s-t)F(s)F(t)dsdt
     \le R_\star R_{\mathrm{sp}}T(g)^{\alpha/2}`. Nonnegative Tonelli is valid before
     finiteness; null-time modifications alter a product-null set.
  4. Energy upper bound: maximizing `R_\star R_{\mathrm{sp}}T^{\alpha/2}-T/2` over `T\ge0`
     (same differentiation as `\eqref{E:spatial-energy-map}`) gives
     `R_\star^{2/(2-\alpha)}\mathcal E_{\mathrm{sp}}`, so
     `\mathcal E_\star^{\mathcal O}\le R_\star^{2/(2-\alpha)}\mathcal E_{\mathrm{sp}}`.
  5. Positivity: a constant-in-time unit compact profile with dilation `U_\ell` has
     `J=J_0\ell^\alpha A_{\mathrm{sp}}(g)` with
     `J_0=\int\int K_\star(s-t)dsdt\in(0,\infty)` and `T=\ell^2b(g)`; since `\alpha<2`,
     small `\ell` makes `J-T/2>0`. No attaining profile, trace, or rough-stochastic-evolution
     argument is used.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED. The new step headings and summary paragraphs only reorganize the
  old reasoning; no hypothesis is weakened and no new existence claim is made.
- Evidence: old proof 429–465/new proof 523–575; statement 409–427/503–521. The critical
  exponent consistency is `N(g_s)^4=b(g_s)^{\alpha/2}=F(s)^2`, which justifies the cited
  `B\le R_{\mathrm{sp}}F(s)F(t)` and then the row/Jensen route to `T^{\alpha/2}`.
- Lost steps/qualifiers: none. The full-class hypotheses (strong `H^1`-measurability, unit
  norm a.e., finite `T`, no time smoothness/common compact support/optimizer) are retained
  verbatim.

## AUDIT dispositions
No AUDIT comment appears in either revision of `notes/integrated_spatial_occupation.tex`
within the assigned module. I found no AUDIT-worthy issue introduced by the rewrite. The only
noteworthy pre-existing stylistic point is the symbol `q` being used both as the fixed
`q=4-\alpha` and as the resolvent argument inside `L:spatial-fourier-bound`; the new revision
explicitly disambiguates it, so this is not a defect and is now clarified.

## Findings and limits
Within the eight assigned proof pairs, all old and new readings and all public reconstructions
are complete. The new revision is a readability rewrite: it adds step structure, states the
operational outline before each proof, and inserts correct algebraic/differentiation detail,
without changing statements, hypotheses, exponents, endpoint cases (`K_\star(0)=0`,
`\Gamma=0`, zero-covariance paragraph), limits, or qualifiers. The dilation scaling
`A\mapsto\ell^\alpha A`, `b\mapsto\ell^2b`, the exact gradient penalties, the scalar
variational constant `M_a(1+u)^2/(2R u^{\alpha/2})`, the coefficient
`R(g)\alpha^{\alpha/2}/(8M_aq^{q/2})`, and the occupation constant
`R_\star^{2/(2-\alpha)}\mathcal E_{\mathrm{sp}}` all survive with correct algebra.

This review is scoped to argument preservation and internal justification of new explanatory
assertions. Imported finiteness/spectral results (`P:variational-unmasked-rate`,
`P:variational-remove-mask`, `L:temporal-equilibrium`,
`L:damped-homogeneous-norms`, `L:compact-raw-profile`,
`\eqref{E:masked-spectral-convention}`, `\eqref{E:intro-spectral-mass}`) were treated as
inputs and checked only for application under their stated hypotheses; their own proofs were
not re-certified. Likewise, fidelity of the module to primary sources, Lean quotations,
rendered pages, or whole-book correctness is outside the assignment and was not reviewed.
