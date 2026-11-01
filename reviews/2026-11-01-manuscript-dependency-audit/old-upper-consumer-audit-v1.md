# Actual old-upper consumers and retained fixed-time prerequisites

AUTHOR semantic dependency audit, 2026-11-01. Source read at workflow
3c375e63d3253bd571a604dae7a82dfa9c49ef42; main scientific source remains
887fbfbe0fa4368d6b32a436615d73349b2445d8. This is an organization audit,
not a new proof, mathematical acceptance or authorization to remove a lemma.

## Correct-scale upper growth: actual uses

An all-own-TeX search for T:full-upper finds one nontrivial final-argument
consumer: P:variational-positive-scores, integrated_unmasked_variational.tex
lines345-365. The proof uses the original canonical point-moment bound to
bound its normalized limsup by C_up. A fixed-test lower bound then makes
Q2 finite, bounds every label-two score, and control dilation bounds every
label-one score BEFORE taking a finite-real supremum. Merely proving each
individual potential/rate finite cannot replace this uniform bound.

A second mathematical consumer is P:near-static-mean-gap in main TeX
around6963. Cauchy-Schwarz plus the full upper at temporal exponent b
makes the first-moment normalized type finite. It is an auxiliary result
outside the current theorem reference path, but must remain valid if kept.
A spatial-ratio bound alone does not prove that temporal mean statement.
Other direct hits are the full-upper statement/proof itself and explanatory
prose (main159,6621,7628). The search is not a semantic completeness proof.
The original full-upper result remains a required retained deliverable.

## Fixed-time source summability is a separate dependency

L:masked-chain-comparison uses L:vertex-crude, not T:full-upper. Its
q_n(t)=exp(theta0*t) C^(n/2)t^n/sqrt(n!) is uniform over positive vertex
widths. E:vertex-summability makes sum sqrt(n+1) q_n(T) finite at fixed T.
L:vertex-crude is proved around main1044-1116 using the imported Chen
Theorem3.1, own damped homogeneous norms and pairing-count bounds.
It precedes the correct-scale result and does not use that result.

P:masked-source-moments uses sum q_n(T) to identify actual continuous
ordinary solutions, pass mixed diagrams to sums, construct spatial Bochner
averages and compare masked and stationary unmasked second moments.
P:masked-canonical-transfer then passes the source point moments to the
canonical field by fixed-order convergence and these uniform tails.
These source estimates CANNOT be deleted just because a later variational
score bound proves the correct asymptotic scale. Conversely, retaining them
does not force retention of the entire Section13 argument as a premise of
the final constant theorem. Their own imported source applications still
require the assigned independent fidelity review.

## The actual point-flow finiteness interface

L:point-actual-finiteness in integrated_point_transfer.tex lines20-69
uses P:tube-actual-law, P:tube-coarse-envelope and L:tube-rayleigh-tail
with B=1 for the actual endpoint. It establishes fixed-parameter finite
second operator moment directly, with literal given-W/mask/phase matching.
It does not appeal to an asymptotic full-upper bound.

L:point-fast-sources, lines72 onward, obtains fixed-delta source convergence
and uniform integrability from Gaussian path moments, square-exponential
tails, Young dependence and exponent 1/theta<2, then actual restriction.
There is no asserted uniform-in-delta moment bound. This is different from
replacing the source-chain construction or identifying arbitrary source laws.

## What the independent spatial-ratio draft might replace

Current spatial module first assumes finite S1, then
P:spatial-smooth-ratio uses its explicit lower-score inequality to force
finite R0. Draftv2 instead supplies finite R0/R_sp from the imported
Chen2023 compact-test energy and physical Fatou extension. If reviewed and
adopted, it could remove this direction of the bootstrap. It does not
replace the separate lower-score inequality in that proposition.

There is an existing possible route back to a uniform score bound:
P:spatial-four-linear, the occupation-class estimates, L:occupation-raw-square
and L:occupation-rayleigh-selection lead to the pointwise bound
I_Psi <= D v_Psi^(1/q) in T:intrinsic-occupation-ceiling. The first part of
that proof optimizes individual scores before its last invocation of the
intrinsic moment theorem. Its use as an earlier finiteness input would
require a new ordered interface audit: no finite S1/C2 premise may enter
through any setup, imported lemma, occupation constant or selection step.
The moment identity in the last part cannot be used to prove its own
premise. This audit does NOT certify this extraction, score finiteness or a
shorter final proof. Do not start another mathematical cycle before the
pending bounded finiteness draft receives its required independent review.

## Evidence and unchanged boundaries

The eight pending finiteness-review inputs were rechecked byte-for-byte
against live files, frozen packet copies and committed3c375e6; all match
the manifest SHA256. Main PDF remains257pages, SHA256
10bfeae6eb576e23ba928b8ef9eca968d87f23ac7eff884c632bf50acb3294c9.
No TeX, source PDF, main proof, Lean fact, review verdict or composition
contract changed. No shortened manuscript is claimed. New Lean work is
not useful for this reference/consumer classification; the pending draft's
analytic import and measure correspondence remain the substantive checks.
