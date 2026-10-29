# Full upper bound: proof map and review limits

The current result is the ORIGINAL full G:upper:for every covariance in
H:homog and d=1,2,3,the canonical Stratonovich mild solution satisfies

E u²(T,x) <= e(T+2)^d exp[C R_alpha^(1/nu) T^(beta/nu)], T>=1,
nu=3-alpha, beta=4-alpha-alpha0, kappa=beta/nu.

R_alpha=alpha*pi*mu(B1)/(2*sin(pi*alpha/2));C depends only on alpha,alpha0.
This covers the original nonnegative even PD homogeneous tempered Radon
covariance/spectral class,including d=alpha=1 white space. G:sharp remains
open. No first-moment asymptotic constant enters this bound.

## Construction branch

1. L:damped-homogeneous-norms directly proves norm finiteness,scaling and
   vanishing high temporal-Laplace tails from radial spectral ball growth.
2. L:spatial-wick-measures proves positive gap-Laplace transforms,uniform
   mass via Brownian heat conditioning,weak convergence and null boundaries.
3. L:joint-fixed-order uses marked temporal-tail edges in the explicitly
   imported Chen Theorem3.1 to obtain arbitrary joint width limits and
   Gaussian L2 Cauchy construction. Green smoothing precedes noise removal.
4. L:vertex-crude and P:mild-construction independently identify this series
   with the actual onefold Stratonovich mild equation. Fixed-covariance
   constants used here do not enter the quantitative moment constant.

These three new lemmas and their consumers passed their OWN8check primary/
HIGH gate atf9303ed. The final adopted statements and46of51proofs match
that review;five optional minor clarifications are separately bound.

## Quantitative branch

1. L:interval-contractions controls fresh Gaussian colors by R_alpha using
   radial spectral masses,without density/isotropy assumptions.
2. The complex-phase/Fock estimates bound occupied background colors.
   The bounded-operator Crouzeix--Palencia theorem is explicitly imported.
   L:finite-word-cutoff retains both creation and annihilation at each prefix.
3. L:fixed-split assembles background segments,metric changes and fresh-color
   insertions at fixed inventory. Singleton types and higher degrees are
   counted once;the conversion keeps the factorial power3-alpha.
4. P:interval-coefficients sums the inventory uniformly. The auxiliary
   entire-series majorant depends on finite-family variance only for
   identification;the coefficient bound is independent of that variance.
5. Three shifted dyadic grids dominate the source time covariance at finite
   Wick order,with c=6^alpha0 and decreasing lengths h_i<=78T/i.
6. Positive terminal-chain comparisons and finite propagation identify the
   finite-depth interval models with the constant-data solution on B1.
7. At fixed smoothing/order,J->infinity is MCT of positive integrals,not
   construction of an infinite-variance Gaussian field. All finite J models
   have finite variance. Time diagonals are null at this stage.
8. The scaled amplitude2bound gives uniform geometric order tails;the final
   amplitude1bound gives the displayed constant. The fixed-order input from
   the construction branch is used here,without a convergence-rate constant.

The actual19check primary/HIGH sourcea7e725e audits the quantitative branch.
The current L:fixed-split,L:terminal-wick and L:uniform-series-tail proofs
match its bytes. P:interval-coefficients matches final adoptiondf1648b;its
previously recorded singleton split-count explanation is the explicit minor
textual delta from that primary. critical-path-review-binding.json preserves
both exact matches and this qualification.

## Current limits

The seventh free-form cold read found clean spot-checks but did not clear
journal presentation or independently rederive the whole critical path.
It is retained as NOT CLEAR;primary acceptance is not whole-paper clearance.
The research notebook also contains alternative conditional/historical routes,
which are outside this upper proof. A focused exposition can follow this map
while preserving the notebook. Novelty,paper promotion,sharp constants,Lean,
canonical wiki publication and circulation remain separate gates.
