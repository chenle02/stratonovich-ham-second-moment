# Actual-event finite arithmetic only

Two actual paper consumers, no new nontrivial library definitions.
Pinned Mathlib search found Analysis.ODE.DiscreteGronwall (general
product/sum form) and SpecificLimits.ArithmeticGeometric, and exact
Real.rpow_add/sub and sqrt_eq_rpow. Existing direct-event/joint-tilt
modules inspected. We use native induction/order arithmetic and those
Mathlib real-power APIs for a paper-specific closed-form budget, not
a competing recurrence framework or spectral/probability foundation.
Latest stable4.35.0/fullMathlibpin from the recent official source queries
remains the read-only donor pin; no new package/lease/registry/HPC.

finite_error_accumulation: C>=1,e>=0,d0<=0 and the per-step bound
d(n+1)<=C*d(n)+C^n*e imply d(n)<=n*C^n*e for every n. Actual operator
norm differences satisfy the recurrence by submultiplicativity and
previous-prefix norm bound; THOSE operator hypotheses are analytic.
For an actual finite factor list, extend BOTH sequences by identities
past their ends before instantiating the all-n recurrence; the used
finite products do not change. This quantifier extension is analytic,
not hidden in the theorem. This is the looser finite bound used in actual-shifted-event(13), not
a formal proof of the stronger ordered identity(12) or norm estimates.

moderate_penalty: delta>0 implies
delta*(delta^(-1/4)/sqrt(delta))=delta^(1/4). It checks the normalized
SAME-Z density penalty in the proof of(20)-(21). It does NOT prove
Chebyshev, probability limits, Gaussian tilting or the event.

WrongAccumulation uses C1,e1,d(n)=n (which satisfies the recurrence)
but incorrectly drops accumulated error and claims d1<=0. WrongPenalty incorrectly keeps a unit
normalized penalty at delta1/16, rootquarter1/2 and sqrt1/4, whereas
it equals1/2. Both numerical altered endpoints must reach actual False.
Fresh owned source/replay, full types/live axioms and independent
application review required; no formal SPDE/flow/event/companion claim.

The application fence was clarified after the local run; Lean/Audit/control
sources and complete printed types are unchanged.
