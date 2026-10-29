# Terminal-cross scalar consumers: local statement fence

Le's authorization for local Lean verification persists. No companion repo,
new package, lease, registration, donor write or cluster job is involved.
Reuse the pinned Lean4.35.0/Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679
read-only dependency cache, with owned source/output and capped local runs.

This checks the ACTUAL final scalar comparison for the white (1,3)03|12
gap transform. Put c=1+lambda>1, b=1+nu>=1, P=c²+c+1 and
N=bP+c³+c+1. The target is STRICT:

    P/[16 c³(c+1) sqrt(b²+(c²-1)/(c²+1))]
      < N/[32 c³(b+c-1)(b+1)].

No desired comparison is a hypothesis. A shifted positive polynomial
certificate proves it after positive denominators and square roots are
handled. Certificate identity/positivity are checked as separate facts.

Also check two consumers of the kernel-envelope proof:

- A>0,s>=1/2 imply A/[2(A+1)] <= sA/(A+2s).
- 0<=D<C and (C-D)k=Cr-DR imply, for every real w,
  C exp(-rw)-D exp(-Rw) <= (C-D)exp(-kw).
  This is convexity, not a bound assumed as an input.

The paper must separately establish the exact wave/clock reductions, their
finite integrals, the positive Laplace mixture of the heat kernel, and the
component coefficients' correspondence. No Brownian/SPDE/white-to-general
extension or all-order/sharp theorem is formalized by these scalar lemmas.

Acceptance: source elaboration, full public types and live standard-three
axiom audit, semantic false controls, fresh OWNED source replay using the
unchanged pinned dependency cache. Not a canonical lean-pkg/Comparator gate.
Independent source/type/application correspondence remains a separate check.
