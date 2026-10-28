# Lean roadmap (strategy, not state)

The companion verifies the **finite and algebraic** parts of the project's
proofs and states every analytic input (chaos convergence, Laplace
transforms of the wave kernel, large deviations) as an explicit hypothesis.
End-to-end formalization of the SPDE is not a goal; an honest, minimal
unverified boundary is.

1. **L1 — counting (finite).** Pair partitions of 2n points split across two
   ordered chains; #Π_n = (2n)!/(2^n n!); the partition {Q0,Q1,Q2} of
   Chen's Theorem 3.1 (#Q0 = #Q1, #Q2 even); the growth of the resulting
   sums in n that determines the time exponent. Acceptance: the exact
   counting statement used in the notes, no sorry, axioms ⊆
   {propext, Classical.choice, Quot.sound}.
2. **L2 — Laplace to time (analysis with named hypotheses).** If the Laplace
   transform of a nonnegative nondecreasing f satisfies a bound of
   Mittag-Leffler type, then log f(t) ≤ C t^κ. Reusable beyond this project
   (check Mathlib and the lean-pkg registry first).
3. **L3 — constants.** The exponent κ = (4−α−α0)/(3−α) ∈ (1,2), the
   conjectured constant 2^{(4−α)/(3−α)} L, and the Jensen comparison
   2^{(4−α)/(3−α)} > 2 for 0 < α < 2.

Before each wave: `lean-pkg search` for prior art, `search-before-building-lean`,
and the statement fence (`lean-dev` skill).

## Additional seams after the October 28 checkpoints

These are future statement candidates. They do not open a wave, replace the
initial G0 fence, authorize a companion, or formalize the surrounding SPDE.

1. **Product endpoint feasibility.** For three real exponents in [0,1),
   sum alpha in (1,2), and 0<theta<2-alpha, verify the actual max/min
   intervals, sum L<1<sum U, the explicit Lambda interpolation, strict
   active-coordinate bounds, zero coordinates, endpoint sums and
   reconstruction. Source: notes Lemma9.1. The formal type must use the
   actual vectors, not a weaker recurrence or a finite test grid. The
   Gaussian-mixture/positive-definiteness and stochastic consumer are outside
   this algebra seam; its current paper review is medium, not accepted HIGH.
2. **Plane endpoint parameters.** For s=a1+a2 in (0,1-alpha0),
   alpha0<theta<1-s, prove v_j=a_j/(1-theta) in [0,1),
   beta=1+s/(1-theta)=(alpha-theta)/(1-theta), alpha=1+s,
   1<alpha<beta<2 and the three measure-scaling exponents. The actual normal
   Dirac measure, distributional covariance validity and Gaussian Holder are
   analytic inputs outside a scalar verification. The deterministic proof
   passed its own HIGH review; it did not accept the moment consumer.
3. **Conditional finite-sum comparison.** For finitely many nonnegative
   entries and weights, make the common theta and zero-weight conventions
   explicit. Reuse Mathlib's appropriate finite Holder inequality. Any
   covariance/convolution linearity and component comparison must be named
   hypotheses of a scalar consumer. No countable/integral-mixture or
   arbitrary-covariance representation conclusion may appear in the type.
4. **Exact source-ordering certificate.** With R>0 and the two functional
   estimates as explicit hypotheses, deduce E_star>E from
   E<=((11/9)^2/4)R^2 and E_star>=((549/560)^2/2)R^2.
   The exact positive gap is5440681/50803200. A rational tactic pass would
   certify this conditional deduction only; Sobolev estimates, Gamma moments,
   all-profile variational bounds and the finite-energy interpretation stay
   outside. It identifies no intended correction to the source constants.
5. **Moment exponent/constant bookkeeping.** With beta=(alpha-theta)/(1-theta)
   and b0=alpha0/theta, verify
   2theta+(1-theta)(3-beta)=3-alpha and
   theta(3-b0)+(1-theta)(4-beta)=4-alpha-alpha0.
   For Q=3-beta, nu=4-beta, verify nu-Q=1 and the actual real-power factor
   2^(-Q)2^nu=2. The static source coefficient bound, homogeneity, finite
   low-order enlargement and limiting-series application are separate named
   analytic inputs, not consequences of this arithmetic.

Evidence: reviews/2026-10-28-product-endpoints/ in the manuscript repo
(relative to this directory: ../reviews/2026-10-28-product-endpoints/), and
../reviews/2026-10-28-source-normalization/. Search exact reusable declarations
locally at the selected pins before writing any proof. No Lean command was
run and no private package was created by this strategy update.
