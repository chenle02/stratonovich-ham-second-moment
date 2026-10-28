# Plane-supported endpoints and finite-sum closure: scoped acceptance

[held back: AI account details]

## Exact accepted scope

Pure deterministic verification of Hypothesis9.2 for rotated plane-supported
covariances c|y1|^-a1|y2|^-a2 dy delta0(dz),with s=a1+a2 in(0,1-alpha0),
normal-delta-preserving endpoints,and finite nonnegative-sum closure of the
condition for covariances sharing alpha/theta/beta. Low endpoint normalization
V=c/pi and wave closing boundc/2 also passed. No powers of distributions.

This does NOT accept the stochastic consumer of Hypothesis9.2: its complete
Section9 review remains all14PASS/medium below HIGH. It does not establish a
representation/density theorem for all d3 covariances,novelty,Lean verification,
sharpness or circulation clearance. Statements about mixing ordinary-product
and Riesz components remain conditional on their actual endpoint constructions;
this auxiliary report did not fully review that product lemma.

## All five minor findings

1. The sentence applying closure to Section9 product/Riesz families references
   constructions not included in the auxiliary packet. Core plane and abstract
   finite-sum results are independent of them. Retain that exact scope; do not
   transfer this HIGH verdict to the whole product/moment argument.
2. The control script displayed the fixed example without computing/asserting
   it; a1=1/2 is not on its grid. Reviewer recomputed it independently by hand.
   Root will separately add an executed exact example assertion to the live
   control script. Frozen packet/script/JSON remain immutable.
3. The256half-theta cases are a tautological AMGM reduction,not evidence for
   general theta or zero weights. Analytic discrete Holder proves the actual
   statement. Do not expand diagnostic counts into proof/Lean claims.
4. Absolute Fubini can be made explicit with A(u)=integral |phi(y+u,z)phi(y,z)|
   dydz. Rapid decay gives A(u)<=C_N product_j(1+|u_j|)^(-N). Then integral
   f_e(u)A(u)du is bounded by a product of finite one-dimensional weighted
   integrals for0<=e_j<1,N>1. No false assertion that product singularities
   are uniformly bounded off a cube is needed. This explains the existing
   rapidly-decaying-autocorrelation justification without changing the proof.
5. Source condition(1.5)follows from the positive spectral MEASURE mass scaling
   mu(rA)=r^alpha mu(A) and the dyadic tail alpha+alpha0<2. Zero tangential
   exponents give spectral atoms; full-dimensional density is not assumed.

## Limitations and failure lineage

This is AI/read-only auxiliary review,not human or novelty verification.
Reviewer did not run code/hash checks; root separately executed exact controls
and verified committed bytes,actual native ledger and archive. Source images
were read visually. Ordinary-product endpoint feasibility was only sketched
in this scope; the radial-lowering counterexample was not supplied.

Auxiliary v1 was supervisor-interrupted because its commit had failed on a
trailing blank line while root improperly proceeded to a later tool call. It
has no scientific verdict and is not a second review vote. Its logs,old packet,
receipt and explicit supervisor cause are preserved. Generic blocked-provider
status is not a provider outage/quota finding. New v2 removes only a boundary
blank line and is correctly committed before launch; no old receipt/threshold
was edited. The new guard has an actual uncommitted refusal and committed
positive control; it certifies identity only,not scientific completeness.
