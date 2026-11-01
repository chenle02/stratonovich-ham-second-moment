# Exact finite white-CDF consumers and exclusions

Two PUBLIC conditional REAL algebra statements, sourceSHA
4d3f8ee4350f96d5936a4b213c7aff5a312218743ee43b885e3c91a3b100cbcd.
Headers were frozen before proof and unchanged. Both compile with only
standard axioms; exact full elaborated types, private composition and
positive calls are in types-and-axioms.txt and Audit.lean. Initial analytic
type/application correspondence is PENDING; these are not accepted WS facts.

1. cdf_square_bound(A,b,h): h is FOR EVERY REALz the scalar nonnegativity
   0<=b-2zA+z²/3. In WS, A=int f^4 and b=int(f')² for a real unit-L2 H1
   profile. The ANALYTIC CDF square identity must supply h. The kernel
   checks only the substitution/completion leading to3A²<=b, not that identity,
   the1/3 integral, H1 representatives, endpoints, mass or integrability.
2. energy_upper(c,A,b,h3): h3 is3A²<=b. It proves cA-b/2<=c²/6 for ANY
   REALc; the actual model uses c>=0 as physical covariance mass Gamma=cδ0.
   c is not OC's auxiliary moment label. WS must identify the physical
   energy with cA-b/2 and prove a genuine admissible profile attains the
   upper bound. The kernel does not prove a variational supremum/attainment.

The PRIVATEactual_energy_consumer composes these two exact public APIs.
It is not a third public fact. Ground positive calls use A=b=1/3,c=1;
the all-z premise is proved by the square(z-1)². The two standalone false
controls reject4A²<=b and the wrong energy ceiling1/12 at the same values,
with one exact arithmetic False goal each, not an API/import failure.

Source-only fresh replay of owned files produced five identical object
pairs and identical audit output; eight official Mathlib-only library dirs
at nine clean selected source pins are read-only. Two private libraries
are excluded. This is not an independent foundation rebuild or package gate.
Latest official stable pair4.35.0 and Mathlib56a0058 checked at preflight;
per-unit2CPU/4GiBhigh/6GiBmax/64tasks,proof-j1,asyncfalse,max2concurrent.
Effective limits were verified inside every unit. Process RSS about1.8GiB;
do not confuse it with the much smaller cgroup-charged shared-cache memory.

No new repository/package/remote/lease/registry/cluster action. Official
L0/PROPOSED and companion decision4 unchanged. Accepted78facts21seams plus
these2PROVISIONALpublicfacts; no full GN/CDF/PDE formalization claim.

Evidence guard: the initial inline validation looked only for known axiom
names. Although the actual complete outputs were manually read and contain
only standard axioms, that predicate could miss an additional unknown name.
Before promotion it was replaced by verify-evidence-v1.py, which parses the
ENTIRE axiom list and exact sole False error block. Fourteen adversarial
text mutations (extra/sorry axioms, missing/duplicate inventories, compound
False goals and API/extra errors) are rejected. This applies an existing
verification rule, not a new mathematical theorem; no proof was rerun for
this text-guard repair. The initial receipt and native logs are preserved.
