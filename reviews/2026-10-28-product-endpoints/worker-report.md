# Three-dimensional covariance-endpoint worker report

Status: **DONE_WITH_CONCERNS — complete candidate, independent review pending**.
Date:2026-10-28 UTC. No git, sibling/source/registry edit, external contact or
cluster work. All builds are terminal.

## Three authorized subaims delivered

Inserted one556-line Section9 before Targets, leaving all earlier content and
review status unchanged.

1. Lemma9.1,p40(L:product-endpoints): complete strict product-exponent
   construction and covariance admissibility. It proves both strict interval
   sum bounds, active-coordinate bounds, zero-coordinate preservation, exact
   endpoint sums and reconstruction. Gaussian mixtures run only over active
   coordinates; no Gamma(0) or coordinate-white-noise convention is introduced.
2. Hypothesis9.2,p42 and Proposition9.3,p43: an EXPLICIT deterministic
   common-Gaussian covariance comparison, followed by a complete conditional
   d3 transfer with precise source identification and an explicit nonsharp
   asymptotic variational constant. No moment estimate is assumed.
3. Corollary9.4,p47: ordinary product covariances0<=a_j<1 and isotropic Riesz
   covariances, with the canonical midpoint theta=(alpha0+2-alpha)/2.
   Endpoint choices/constants therefore depend only on the original data.
   The Riesz admissibility argument is given afresh, not taken from an
   unaccepted earlier candidate.

Remark9.5,p48 records calibrations and boundaries. Earlier Section7/8 candidates,
the accepted abstract/global scope, and historical confidence are unchanged.
General d3 factorization, sharpness, novelty and formal verification remain open.

## Static input and Green-limit identification

The proof directly imports the GENERAL static coefficient facts from Chen–Hu
(5.1),(5.15),Theorem3.8(i), with Dalang verified by spectral homogeneity and a
dyadic sum. The zero static covariance is explicitly trivial. Finiteness of the
actual static variational input is bound to Chen2023Theorem1.1 as identified
by Chen–Hu p2175. The new proof does not invoke P7.2,P8.3 or their static
specializations as accepted premises.

At fixed spatial noise width the static field has bounded continuous covariance.
The Gaussian-product integrand is mean-square continuous and uniformly L2
bounded by P_n times the nth power of its variance. Its integral against the
source's finite positive eta=0 Green-chain measure therefore exists in L2.
This defines the ACTUAL source approximant at(2.22), not merely an unspecified
Cauchy limit. Weak convergence of Green products, including mixed products with
one width already zero, and bounded Gaussian moment factors give BOTH
E U_eta^2 -> E U_0^2 and E U_eta U_0 -> E U_0^2. Their difference proves L2
convergence to that named source approximant. The target uses its prescribed
inner Green limit. Only after this fixed-noise Green limit are noise widths
removed via the respective source fixed-order L2 theorems. Finite mixed
products converge in L1; empty chains and k0 are explicit.

Hölder is on the entire finite disjoint measure of splits, pairings, ordered
times and product-Green increments. The low endpoint uses raw temporal power
only as a deterministic integral. Its uniform closing constant pi*V_low/2,
opening AM–GM and complete temporal count give C_low=2Z_b0*pi*V_low.
The static endpoint is the actual regularized static coefficient; its raw
coefficient majorant is applied only AFTER limits. No smoothing monotonicity,
uniform smoothed static asymptotic or target raw-integral equality is assumed.

## Explicit variational limsup constant

The authorized strengthening defines M_st as the actual source functional(1.11)
for Gamma_st with unit gradient penalty, using a positive-measure energy
definition when Gamma_st is singular. It retains the actual endpoint amplitude.
With Q=3-beta and Nu=4-beta, source(5.15) at p2 gives

  Lambda_st = 2*(2 sqrt(M_st)/(4-beta))^(4-beta).

The factor2 was checked independently:2^(-Q)*2^Nu=2 because Nu-Q=1.
The normalized source time constant also agrees since Nu/Q-1=1/Q. The proof
gives the explicit generally nonsharp bound

  limsup t^(-kappa)log E u(t,x)^2
    <= q[C_low^theta Lambda_st^(1-theta)]^(1/q).

For every rate slack r>0, the coefficient threshold N_r is independent of t,
by STATIC coefficient homogeneity. The finitely many lower target orders
remain in a finite power sum P_r(t); log P_r(t)/t^kappa tends to0. The tail
is summed by the scalar factorial-series bound, then r decreases to0.
This also handles a zero static rate without division. The precise limsup
constant is NOT substituted into the pure all-time exponential: that earlier
bound retains C_st enlarged to cover low orders. No sharp-constant claim or
optimization over theta is made.

## Diagnostics and scope

The original probe's2985grid+5boundary controls and root's579controls were read;
those artifacts were not rewritten. New author-checks.py/JSON exercise84exact
canonical-midpoint grid cases(27with a zero coordinate), plus3additional cases.
They check reconstruction, endpoint sums, strict coordinate bounds, fractional
time feasibility, affine coefficient exponents and the p2 factor-two algebra.
An excluded coordinate exponent1 is refused. Total-order2/4 full-disjoint
counts are3/15. These finite controls are not a continuous proof, stochastic
convergence test, Lean certificate or independent review.

The product construction changes coordinate exponents, unlike the failed
Euclidean radial lowering. It proves no generic d3 factorization. Gaussian
comparison is an additional hypothesis outside the two discharged families.
Skorohod comparisons are limited to the published Riesz and strict-positive-
product cases within their stated hypotheses; zero-exponent product cases
here do not expand that comparison. No Skorohod result was developed.

## Formatter, preservation and final build

Baseline commit41ee952cbf2fa2a223c406943ce798f645308a7f, TeX SHA256
76d2331bad7f13ce1410d9bb3bfb23a1f6f4850132e9982ca62133af078abc17.
The baseline passed format-tex --check before editing. The ACTUAL requested
formatter was run on the canonical TeX BEFORE the canonical latexmk command.
It changed only the insertion. A second ACTUAL formatter run was byte-idempotent.
Its executable hash is in worker-checks.json. Deleting the insertion recovers
the complete baseline source byte-for-byte: all24old proofs,29old non-remark
statement environments, remarks, abstract and historical candidate status.
All3new proofs have their required linked closing sentences.

Final TeX SHA256:
950add7de797a7c754e565efa4654013b85bca9ccda31bab5c42ba82770015dc.
Final PDF SHA256:
d0359c46bc7d855dc81051388608091e536e7df7e04ed30ee2854c0f54a33244.

The canonical49-page build is terminal exit0:
0errors,0undefined references/citations,0overfull boxes,0tabs.
Only the prescribed root command was used:

  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex

Final pages43and47 were rendered and visually checked for the expanded theorem,
limsup constant, tail argument and application layout. Earlier draft pages40/45
were also inspected before the asymptotic strengthening; that is separate
coverage. No whole-PDF or whole-manuscript strict-style inspection is claimed.
The scoped le-style checker has no hard finding; its one 'rather than' advisory
was retained because it marks the specifically required distinction between
identifying the source eta=0 approximant and merely proving a Cauchy property.

The earlier9c611379/cad50ff6draft hashes are preserved in pre_freeze_history.
An amendment insertion initially failed a context-match assertion before any
canonical source write; its safe refusal is recorded, not treated as a proof
failure. The corrected insertion was formatted, built and preserved normally.
No source/PDF writes remain live.

## Honest limitations

No missing premise was found in this bounded author task. The imported static
source results and generalized-covariance framework are used at their audited
scope, not re-proved in their entirety. The new written candidate still requires
the mandated native independent review. Mathematical proof text, exact controls,
formatter idempotence and a clean build do not supply that review or promote
earlier medium-confidence candidates. The original full general-covariance and
sharp-constant objectives have not been narrowed or declared complete.
