# Next bounded test: time regularity of the interaction-picture driver

UNPROVED planning, not part of the review packet or accepted mathematics.
The first-response proof now passed8HIGH at0ae116c. Every further
estimate/flow/event step below is still UNPROVED. No sharp theorem,
new source constant, all-order flow or Gaussian event is asserted here.

Immediate proposed object on the balanced E=H^(1/2)xH^(-1/2):
M(t)=integral_0^t S(-r) [0,0;W(dr),0] S(r).
Start on Schwartz data and with spatial/noise cutoffs. Use localized output
chi; do not assume a global stationary-noise HS operator exists.

Candidate estimate to test and prove, with h=|t-s|<=1:
E||chi(M(t)-M(s))||_HS(E)^2 <= C h^(2-a)(1+|log h|)^2.
For nonwhite d1Riesz alpha<1, a bound without the logarithm may hold. It is
UNPROVED here. Check uniformity in all source regularization widths.

Suggested calculations to audit:
(1) Derive exact J_(a,h)(r)=h^(2-a) J_(a,1)(hr), and the balanced spatial
convolution bound integral dk/(<k+q><k>) <= C log(2+|q|)/<q>.
(2) For white spectral measure the two high/high terms may be exchanged by
k->-k in (r,k)variables. Check the exact transformation before using it.
For alpha<1 the spatial trace with the raw bound J<=C h^(2-a) may already
be finite. Low modes still need the rescaled modulation estimate.
(3) M(t)-M(s) is a free conjugation of the short-block first response with
shifted stationary noise. Use finite propagation and a larger output cutoff;
do not commute chi past the free group. Verify the HS ideal bounds.
(4) If this holds, Gaussian higher moments/Kolmogorov could give local
HS-valued Holder exponent theta>1/2 because a<1. Source-cutoff convergence
in that norm, not just fixed-time L2, is required before any Young flow.

Before a broader flow theorem, run the primary-source implication/value gate
for existing Gaussian operator-valued Young wave constructions. A gap in the
held CDST statements is not evidence of novelty or permission to duplicate
a known complete construction.

Only after this estimate is verified: assess an interaction-picture Young
operator construction, avoiding the undefined primitive square. A spatially
compact noise cutoff has a global HS norm growing with volume. It cannot be
silently declared uniformly small on the expanding cone. Test uniformly
local phase norms and local operator estimates instead. There are order
1/delta temporal blocks and order1/delta spatial cells in d1; high-p Gaussian
bounds might control their maximum without temporal/spatial independence.
The rescaled unit-block noise amplitude is delta^((1-a)/2). No such maximum
or full-flow estimate is currently proved.

Further gates, NOTopened by this plan:
- A cutoff-independent operator path and all-order Young evolution, with
source-compatible smooth approximants and actual canonical Stratonovich
identification. Data1 requires finite propagation/uniform-local handling.
- Constant/smooth positive profile spectral dominance on the chosen phase,
with initial projection and averaged terminal observable controlled. Do not
infer it from wellposedness or the scalar2x2positive-matrix proof.
- A Cameron--Martin good-noise event retaining the actual residual, with
probability cost once and actual averaged-square growth. The reviewed spatial
average transfer would then address the original point second moment.
- Exact source-variational comparison and the desired p2factor; do not adopt
an intended correction of the printed normalization or guess constants.

Loewner control of a LINEARGaussian response variance is legitimate; it does
not license the already refuted nonlinear mean residual-discard comparison.
Higher dimensions need a different operator-ideal/norm test; the d1HS result
must not be promoted to them. Original full sharp target remains intact.
