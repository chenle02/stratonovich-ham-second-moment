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
