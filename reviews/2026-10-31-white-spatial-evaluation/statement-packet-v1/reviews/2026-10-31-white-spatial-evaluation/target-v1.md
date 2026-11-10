# White-space evaluation of the derived bounds: proposed target

UNREVIEWED. Freeze before new diagnostics or proof. This is an explicit
calculation for the actual model, not a fit to a guessed constant. Keep the
full-model PB theorem; this is one example, not a reduced completion scope.

Fix d=1, alpha=1, Gamma=c delta_0 with physical covariance mass c>0,
0<a<1, data(1,0), kinetic operator-Delta. PB gives the ACTUAL point limit
C2(c,a) at exponent kappa=(3-a)/2 by its intrinsic positive-control value.
No finite-time closed moment formula, actualp1 or Skorohod result is sought.

## WS1: derive the spatial extremum directly

For every real f inH1(R),||f||2=1, put A=int f^4,b=int(f')²,
F(x)=int_(-infinity)^x f(y)²dy. Prove the exact CDF square identity

 int [f'(x)-z f(x)(1-2F(x))]²dx=b-2zA+z²/3, EVERY real z.

All terms, endpoint limits, representatives, chain rule and integration by
parts must be justified for full H1, not only compact smooth profiles.
In particular int f'f(1-2F)=A and int f²(1-2F)²=1/3.
At z=3A this gives3A²<=b. Prove sharpness by
 f_l(x)=sqrt(l/2)sech(lx), l>0,
 ||f_l||2²=1, int f_l^4=l/3, int(f_l')²=l²/3.
Consequently the ACTUAL physical white spatial ratio and energy are
 R_sp=c/sqrt(3),
 E_sp=sup_(realunitH1)[c int f^4-b/2]=c²/6.
The upper bound must follow from the CDF identity; equality at l=c supplies
the lower. Do not take a published white constant or Fourier factor as input.

## WS2: actual colored-time coefficient bounds

Conditional until the OC common-spatial-energy bracket passes its FULL gate,
substitute this E_sp at alpha1 into OC(18), with
 M_a=Gamma_E((1+a)/2)/[Gamma_E(1+a)Gamma_E((1-a)/2)],
 K0(a)=2^a/(1-a).
Prove the simplified exact bounds

 (2/3)sqrt(c/M_a)<=C2(c,a)<=(2/3)sqrt(c K0(a)).

This is an INTERVAL for the constant, not an assertion of either endpoint
or a global numerical evaluation of the PB variational supremum. Coefficients
must reflect the physical covariance mass c, not a mislabeled noise amplitude.
At c0 the direct deterministic rate0 has the matching zero bounds; do not
use the degenerate l0 soliton as a unit profile.

## Optional WS3: relative width, no endpoint SPDE substitution

The ratio of these bounds is sqrt(K0 M_a). Using only correctly sourced
Gamma duplication/recurrence and integral Cauchy-Schwarz, test the exact
uniform upper bound
 sqrt(K0(a)M_a)<= [sqrt(pi)/(2Gamma_E(5/4)²)]^(1/2).
An approximate decimal for this bound is NOT a certified decimal enclosure.
Do not infer a=0 or a=1 SPDE limit by substituting boundary parameters;
any parameter limit of comparison coefficients is a separate statement.

## Pre-proof checks and formal boundary

Exercise actual integrals for normalized sech and Gaussian profiles,
including shifts/scales, CDF derivative, the square expansion and wrong
cross-sign/one-third coefficients. They are deterministic consistency
checks, not a proof of the H1 endpoint/chain-rule statements. Retain all
precision-specific residuals/ties and any roundoff-floor values. If evaluated,
Gamma-factor endpoints are evaluations of derived bounds, not PDE samples.

Highest-value feasible finite Lean seams: the scalar implication
 [forall z,0<=b-2zA+z²/3] implies3A²<=b,
 and [3A²<=b] implies cA-b/2<=c²/6.
These do not formalize H1/CDF/integrals or the point moment. Fence complete
types before proof, search/reuse Mathlib first, and use only authorized local
standalone checks. No companion/package/lease/HPC creation. No formal fact
is claimed by this plan. Independent source/FIT and FULL application gates.

Le's derived-constant objective controls. Chen's constants are comparisons
only; old source discrepancies and the unadopted1.24proposal are untouched.
No novelty/whole-paper/human/coldread/public/contact/Skorohod clearance.
