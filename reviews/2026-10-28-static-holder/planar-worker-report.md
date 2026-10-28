# General planar interpolation worker report

Status: **DONE_WITH_CONCERNS — written candidate complete, independent review
pending**. Date:2026-10-28 UTC. No git action, sibling/source/registry edit,
external communication or cluster work.

## Delivered result and exact boundary

Inserted one461-line section `S:planar-holder` after the existing Riesz
interpolation section and before Targets. The final canonical PDF has42pages.
Compiled labels are recorded in planar-worker-checks.json:

- Lemma8.1, p34: complete planar endpoint construction, both positivity proofs,
  direct line convolution and Gaussian Hölder on the original weighted measure.
- Lemma8.2, p36: GENERAL planar static coefficient input, independently sourced
  from the published static theorem and explicit variational finiteness input.
- Proposition8.3, p37: complete higher-alpha general planar transfer, not a
  reference to the unaccepted Riesz Proposition7.2 as a premise.
- Corollary8.4, p40: combines the new candidate with the accepted low-alpha
  result to state the full admissible planar parameter range.
- Remark8.5, p40: static/first-moment/Jensen calibration and remaining scope.

The section has a candidate banner. Earlier abstract/global accepted-scope
prose, the entire Section7 Riesz candidate and historical review statuses are
unchanged. No d3 counterexample or weighted-wave lemma was inserted. The full
G:upper is NOT claimed complete: general d3 higher-alpha covariance remains
outside this planar argument, and sharp constants, novelty and Lean are open.

## Covariance proof details

The input is explicitly a nonnegative even positive-definite tempered Radon
measure Gamma with physical scaling exponent2-alpha. A function covariance
means Gamma(dx)=gamma(x)dx. Zero covariance is separately trivial. Scaling
removes the origin atom; polar rectangle masses extend by measure uniqueness
on finite annuli and Tonelli to every nonnegative Borel integrand, including G.
No angular density or isotropy is introduced.

The weighted endpoint measures are locally finite and tempered by their
radial powers. Their positive measure scaling exponents are1 and2-beta;
these are not called density degrees. The low endpoint is a HALF-mixture of
full line Lebesgue measures over the full even sphere. Its Schwartz
quadratic form is the integral of a squared line average. The direct planar
line integral is1/2, giving convolution constant S/4, where S is the original
PHYSICAL angular mass. Covariance and Green Gaussian averaging preserve this
bound; no equality with a general spectral ball mass is assumed.

The static endpoint is handled by Gaussian multiplication of the ORIGINAL
positive spectral covariance, then a radial Gaussian mixture. Absolute Fubini
is checked using the locally finite weighted measure against Schwartz decay.
There is no fractional power of a distribution. Gaussian Hölder is on the
finite UNNORMALIZED measure p_epsilon(z-x)Gamma(dx); the radial exponents
cancel exactly and the origin atom is absent.

## Static source and full transfer

The general static lemma verifies Dalang by spectral ball homogeneity and a
convergent dyadic sum. The printed Chen–Hu(5.1),(5.15), pp2173/2180, supply
coefficient homogeneity and a finite upper rate at p2. Finiteness of their
variational M is explicitly connected via Chen–Hu p2147/p2175 to Chen2023,
DOI10.1214/23-EJP985, Theorem1.1 p2. The cited key chen:23:exponential was
found in read-only All.bib before use. No Riesz-only lemma is used for the
static endpoint. Absorbing finitely many low orders into C_st is proved locally.
These source theorems remain imported inputs, not re-proved here.

The target proof defines one finite disjoint measure over ALL splits,
pairings, ordered times and unsmoothed planar product-Green increments.
Spatial Gaussian Hölder uses the same edge width2epsilon. Temporal cutoff
is only bounded by the raw power. The low endpoint is a deterministic raw-time
integral, not an asserted stochastic identity. Closing constant S/4 and the
opening AM–GM yield(S/2)^k t^k/k^k; full temporal symmetry and split counting
give2^k Z_b0^k t^((2-b0)k)/k!, hence C_low=Z_b0*S.

The static endpoint is the ACTUAL regularized static coefficient. Source
fixed-order L2 convergence and finite mixed L1 convergence pass noise limits
before applying the static coefficient bound. No epsilon monotonicity or
uniform smoothed static asymptotic is assumed. The affine powers give exactly
(k!)^(3-alpha) and t^((4-alpha-alpha0)k). Empty chains, k0, the complete
nonnegative coefficient series and final scalar summation are explicit.

## Exact normalization diagnostics

planar-normalization-checks.py and JSON check the affine/radial exponents at
alpha=3/2,alpha0=1/4,theta=3/8,b0=2/3,beta=9/5 using exact fractions.
They also record these normalization controls:

- Riesz gamma=c|x|^-alpha: S=2*pi*c, closing constant pi*c/2.
- Atomic angular covariance |x1|^-1/2 dx1 delta_0(dx2): unit-ball mass4,
  alpha3/2, S=2, Gamma_low=line Lebesgue measure, closing constant1/2.
- Product exponents a1=9/10,a2=3/5: four-quadrant beta substitution gives
  S=2B(1/20,1/5), approximately49.3070799043. The60-digit beta evaluation
  is a floating display value, not a certified enclosure or moment test.

These finite algebra/normalization controls are not all-order proof or Lean
certificates. No singular Monte Carlo or discarded covariance factor is used.

## Preservation and build evidence

Baseline commit9ac62d2fa9036516d0aa49c041684acce92b60d2, source
c21b9e691a8a81b5414b65a53b0411b3894bd002d6a058686f7bb9e1e15dff3a.
Deleting the new section recovers that source BYTE-FOR-BYTE. All20preexisting
proofs and25preexisting non-remark/non-goal statement environments are preserved;
remarks and all other outside content are covered by the stronger whole-byte check.
All four new proofs have the required linked closing sentences.

Final TeX SHA256:
`326e1508002dd5ecbadc83fc1c5975926370ae468aa46f29bf2315a30ac39a32`.
Final PDF SHA256:
`1ea056afa44b65dc35a54d3864afe25be45108d02d2977fc90412db35ba1312a`.

Build used ONLY the canonical root command:

  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex

Final build is terminal exit0:0errors,0undefined references/citations,
0overfull boxes,0tabs. Existing hyperref PDF-string and counter warnings remain
outside this gate. Scoped new-section le-style checker passes after a plain-
English wording adjustment. Rendered pages34and38 were visually inspected for
statement, constants and common-measure display layout. No whole-manuscript
Le-Typing or whole-PDF visual-inspection claim is made. No global formatter
was allowed to change the required byte-preserved earlier source.

## Honest remaining concerns

No missing mathematical premise was found by this worker. The generalized
covariance interpretation is explicit and tied to the source Gaussian
framework; its source/application audit is still a separate evidence layer,
not an independent whole-source proof verification. The new full planar
candidate requires its own cross-family review. The source constant is finite
but nonsharp and not numerically evaluated. This construction is genuinely
dimension-specific; no radial-lowering claim in d3 is made. An earlier medium
review of endpoint material is neither upgraded nor used to avoid reviewing
this complete broader candidate. No scientific status promotion is performed.

Pre-freeze clarifications: the general static lemma now treats Xi=0
explicitly(U_n=0 for n>=1,B_k=0 for k>=1,C_st=1), before invoking source
coefficient logarithms. The comparison remark is explicitly restricted to
the stated Riesz subclasses. These are the only two requested edits; earlier
draft hashes are preserved in planar-worker-checks.json/pre_freeze_history.
The canonical rebuild is terminal exit0 and baseline preservation is rechecked.
