# Residual Gaussian driver norms at the inverse-delta exponential speed

ACCEPTED at the scoped FULL analytic/source/type/application gate:
scientific8b16bb7,20checks/HIGH324.742seconds, no required repairs.
Five optional clarity notes adjudicated in
reviews/2026-10-31-upper-residual-exponential/scientific-adjudication-v1.md.
Frozen proof/report unchanged. This is a fixed-spatial-mask driver estimate,
not the sharp upper for the original point moment. All original model
classes and the full completion contract remain unchanged.

## 1. Objects, accepted inputs and precise claim

Use exactly notes/upper-cameron-compactness.md Sections1,4,7-8 (C1-C3,
scientifice0a6f3e/adoptionda1e1f7). All spaces and noises are real. The
original H:homog covariance Gamma, its amplitude, dimension d=1,2,3,
0<a=alpha_0<1 and admissible alpha are fixed. The physical mask is
m_R=eta_R squared ONCE, with R fixed. F=H^(1/2) x H^(-1/2) directsum R²
includes both constant columns. Let H=H_I be the supported raw noise
Hilbert subspace of the GIVEN H_W on I=(0,1), with isonormal W. No raw
Gaussian random variable with values in H or L2 is used.

Fix an integer B>=1 and

 1/2<theta<min(1-a/2,(3-a-alpha)/2),
 1/(1-theta)<r<2/a,  1/theta<=p<2,  nu=1/theta in(1,2).

The intervals are nonempty: both upper theta endpoints exceed1/2, and
theta<1-a/2 implies1/(1-theta)<2/a. Thus nu<=p<2<r. Fix0<delta<min(1,1/B), J>=0, set Q_J=I-P_J, and use the
actual stopped residual paths X_m=X_(m,J) of C3 on [0,B]. There are
n=N+1 paths, N=floor(1/(delta B)); an empty last block gives a zero path.
In the separable little-Holder Banach space

 B0=h0theta([0,B];K(F)),  E_delta=(B0)^n,
 ||x||_delta=(delta sum_(m=0..N)||x_m||Ctheta^p)^(1/p),

put X=(X_m), Y=||X||_delta, b=2EY. The norm is equivalent to the product
norm because n is finite and delta>0. K(F) has the operator norm. We use
the actual given-W joint tuple, not independent block copies.

The accepted compact mean T:H->Lr(I;K(F)) gives

 epsilon_J=||T Q_J|| ->0 as J->infinity,
 C0=C_B(2/B)^(1/p-1/r),  s=C0 epsilon_J,
 L Phi=E[X W(Phi)],  ||L Phi||_delta<=sqrt(delta)s||Phi||H.      (1)

The Bochner covariance in (1), its actual noise identification and both
constant columns are precisely C3 (12)-(15). T and epsilon_J depend on R.
C_B is the fixed primitive bound in C3 (13). The covariance map L is
compact: C3 (12) is a bounded linear primitive/conjugation map applied to
compact T Q_J, for this fixed delta. All these are accepted inputs, not
new proofs here.

Other direct accepted inputs: actual-operator-driver.md gives Gaussian
Lp first-driver bounds; source-operator-convergence.md Theorem1 transfers
those bounds under marginal variance contraction; fixed-mask-young-constant-
phase.md Section3 extends those actual drivers to F. C3 Section7 identifies
every continuous linear statistic ell(X)=W(k_ell), k_ell in H, with

 ell(L Phi)=<k_ell,Phi>H.                                    (2)

We do not recertify those upstream analytic results.

**Proposition D1.** For every eta>0 all these actual expectations are finite,
and, with

 A_nu=(2-nu)/2 (2nu)^(nu/(2-nu)) 2^(2(nu-1)/(2-nu)),

 0<=delta log E exp(eta Y^nu/delta)
 <=2^(nu-1)eta b^nu
   +A_nu eta^(2/(2-nu))s^(2nu/(2-nu))+delta log2.              (3)

Moreover EY<=C g_delta uniformly in J and delta, where
 g_delta=delta^((1-a)/2),
and C may depend on all fixed model/driver parameters, R,B,theta,p and
auxiliary Holder exponents. Consequently for each fixed J,

 limsup_(delta->0)delta log E exp(eta Y^nu/delta)
 <=A_nu eta^(2/(2-nu))(C0 epsilon_J)^(2nu/(2-nu)),             (4)
 lim_(J->infinity)limsup_(delta->0)
                  delta log E exp(eta Y^nu/delta)=0.          (5)

Local symbols a,b in the source theorem, the sublevel set A, the scalar
coefficient A in Section5 and the theorem null set are confined to their
respective paragraphs; a=alpha_0 and block count N otherwise stay as above.
A_nu is a sufficient finite constant, not claimed sharp. No joint J,delta
limit, uniform-R assertion, nonlinear product bound or point upper appears.

## 2. Actual mean bound and Gaussian law

For each fast block, C3 constructs X_m=g_delta times the transferred
masked F driver, stopped at its true remainder length. Its fast noise is
Y_(m,J)(f)=W(Q_J T_(delta,m)f). The pullback is an isometry and Q_J a
contraction, so Var Y_(m,J)(f)<=||f||H_W². Accepted Gaussian transfer,
F extension and stopping therefore give

 (E||X_m||Ctheta^q)^(1/q)<=C_q g_delta,  q>=1,                (6)

uniformly in m,J,delta, with fixed B and mask. Constant extension of a
stopped interaction primitive does not increase its Holder norm. In
particular, Jensen and linearity of expectation, not block independence,
give

 EY <=(EY^p)^(1/p)
     =(delta sum_m E||X_m||Ctheta^p)^(1/p)
     <=(delta n)^(1/p) C_p g_delta
     <=(2/B)^(1/p) C_p g_delta.                              (7)

The same computation at exponent2 (using the finite-sum triangle
inequality in L^(2/p), since p<2) gives E Y²<infinity. Each X_m is an
actual centered Gaussian Banach path by C3's finite transfer and limits;
for the finite tuple, any finite collection of scalar statistics is the
L2 limit of jointly Gaussian first-chaos variables in the SAME W. Thus X
is strongly measurable, centered Gaussian, with a Radon law on separable
E_delta. For completeness, a probability on a separable complete metric
space is tight here: for each radius2^-k choose a finite union of balls
carrying mass>1-epsilon2^-k; the intersection of their closed unions is
closed and totally bounded, hence compact, of mass>=1-epsilon. Taking a
summable allocation proves tightness. No uncountable coordinate assembly
or Gaussian field at a fixed time is being asserted.

## 3. The genuine Cameron space and the ambient Wiener realization

We give the realization details rather than infer an abstract Wiener
space from a formal raw covariance bound. Fix delta,J in this section.
A separable Banach space has a countable norming family of continuous
linear functionals: choose a dense sequence of unit vectors and apply
Hahn-Banach to each. These functionals norm every vector by approximation;
their inverse images generate the Borel sets, since they determine norms
of differences from a countable dense set. We may therefore use countable
scalar identities below to identify Banach variables and laws.

Choose the complete supported raw ONbasis e_i from C3. Let P_n denote the
orthogonal projection onto span{e_i:i<=n}, and P_seen the orthogonal
projection onto H_seen defined below. Write G_n for the
sigma field generated by W(e_1),...,W(e_n). The tuple X is measurable
with respect to the completion of sigma(W(e_i):i>=1), by (2) and countable
Borel coordinates. Its Bochner conditional expectation exists with no
Radon-Nikodym property assumption on E_delta: for a simple Banach variable
sum v_j 1_(A_j) use sum v_j E[1_(A_j)|G_n]; the conditional norm inequality
and scalar Jensen give an L2 contraction. Approximate X in Bochner L2 by
simple variables to obtain the conditional expectation and its scalar
identities. Scalar Gaussian regression and (2) now imply, first for a
countable norming family and then as Banach variables,

 X_n=E[X|G_n]=sum_(i<=n)W(e_i)L e_i.                          (8)

Indeed the conditional mean of W(k_ell) given these coordinates is the
sum of W(e_i)<k_ell,e_i>. The finite-coordinate approximation converges
X_n->X in Bochner L2: finite-coordinate scalar simple variables are dense
among simple variables measurable in the increasing union sigma field
(by the scalar monotone-class approximation of events), and conditional
expectation is an L2 contraction. This also proves (8)'s convergence
without assuming an H-valued standard Gaussian or a trace-class raw field.

Set H_seen=closed span{k_ell:ell in E_delta*}. From (2), ker L=H_seen
perpendicular. The closed first chaos generated by X is exactly W(H_seen).
Thus its Cameron directions, with their genuine first-chaos norm, are

 H_CM=L(H_seen),  ||L Phi||CM=||Phi||H for Phi in H_seen.      (9)

The norm is unambiguous because L is injective on H_seen. The Bochner
covariance definition proves (9): E[X W(Phi)]=L Phi, while all first-chaos
variables of X are obtained by closing its scalar statistics in L2.
Projection onto H_seen accounts for every unused raw direction. In
particular (1) bounds the TRUE embedding H_CM into E_delta by sqrt(delta)s.

Let E0=closure L(H)=closure L(H_seen) in E_delta. Equation(8) gives X in
E0 almost surely. Its support is exactly E0. To see the reverse inclusion,
X-X_n is independent of the finite Gaussian head: every scalar tail
statistic has coefficient (I-P_n)k_ell, orthogonal to e_1,...,e_n; joint
Gaussianity and countable coordinates give independence of the Banach tail.
For any Phi in H, L P_n Phi->L Phi. Given rho>0 choose n large enough that
||L P_n Phi-L Phi||<rho/3 and P(||X-X_n||<rho/3)>0, the latter by L2
convergence. The finite centered Gaussian head has positive probability
in every ball about L P_n Phi: the preimage of that ball under its finite
linear map contains a ball about the coefficient vector of P_n Phi, of
positive standard Gaussian probability. Independence yields
P(||X-L Phi||<rho)>0. Closure then gives every point of E0 in the support.
This argument includes Phi=0. H_CM is dense in E0 by definition; restricting
the law to E0 loses no mass and preserves the norms and covariance.

One can also verify directly the measurable-norm condition for this Wiener
realization, to avoid an implicit infinite-dimensional Gaussian assumption.
Put F_n=span{P_seen e_i:i<=n} in H_seen. For every finite orthonormal family
h_j in F_n perpendicular, each h_j is orthogonal to e_1,...,e_n. For the
Banach Gaussian variable Z_G=sum_j W(h_j)L h_j, regression as in (8) gives

 E[X-X_n | W(h_j), all j]=Z_G,
 E||Z_G||_delta²<=E||X-X_n||_delta².                         (10)

For arbitrary epsilon>0 choose n with the right side<epsilon³. Markov
then gives P(||sum g_j Lh_j||_delta>epsilon)<epsilon for EVERY such finite
orthonormal family. This is precisely the measurable-norm tail condition
on H_seen, with norm ||L Phi||_delta. Its completion is E0; the centered
Radon Gaussian law just constructed has characteristic functional

 int exp(i ell(x))mu(dx)=exp(-||k_ell||H²/2).

Thus (E0,H_CM,mu) is the abstract Wiener realization used below, including
density and the measurable norm, not just an unnamed Banach Gaussian law.
If E0={0} the law is zero and we use the elementary zero case instead.

The Cameron unit ball K is compact as a subset of E0. In fact it is the
image under compact L of the closed unit ball of H_seen. To justify
closedness of that image as well, from any bounded sequence Phi_j choose
a weakly convergent subsequence in the separable Hilbert space (diagonal
ONbasis coordinates and Fatou), with limit of norm<=1. Compactness of L
then forces convergence to L Phi in norm, since every norm-convergent
subsequence has that weak limit. This proves compactness of the image.
For A={x in E0:||x||_delta<=b}, A is closed; A+tK is closed for t>=0,
because a converging sum admits a convergent compact component. Hence all
enlargements used for this norm application are Borel. No outer-measure
ambiguity in the PRIMARY Borell footnote remains.

## 4. Primary concentration theorem, all shifts and zero cases

Imported result, NOT proved here: Friz-Hairer (2020), printed190-191,
Theorem11.7, with Theorem11.6, and the norm specialization Example11.8.
The actual held primary page renders and exact excerpt are retained in
reviews/2026-10-31-upper-gaussian-projection-screen/. The source crosswalk
and primary-friz-hairer-custody-v2.json bind the edition and physical PDF
pages200-201. No finite-dimensional independent-component rough-path
result (including the visible Theorem11.9) is used.

Theorem11.7 assumes a,sigma>0, measurable f,g with mu(g<=a)>0, and a single
null set off which f(x)<=g(x-h)+sigma||h||CM for EVERY h. Its tail is
barPhi(hat_a-a/sigma+v/sigma), v>a, where
hat_a=Phi^-1(mu(g<=a)). The source allows hat_a=+infinity and bounds
barPhi(t)<=exp(-t²/2) for t>=0.

If EY=0, nonnegativity implies Y=0 almost surely, and (3) follows
directly at this delta; Section6 derives (4)-(5) from the all-delta bound.
No concentration theorem is applied. If s=0,
(1) gives L=0; (2) then gives ||k_ell||²=ell(L k_ell)=0 for every ell.
A countable norming family implies X=0 almost surely, so this is again
the zero case. In particular EY>0 implies s>0. It is harmless if s>0 but
the actual law is zero at some delta: the first case already covered it.

In the remaining case set sigma=sqrt(delta)s>0, a=b=2EY>0, and
f(x)=g(x)=||x||_delta on E0. Markov gives mu(A)>=1/2, hence hat_b>=0.
The norm triangle and the actual CM bound give for ALL x in E0 and ALL
h in H_CM

 ||x||_delta<=||x-h||_delta+sigma||h||CM.                     (11)

The null set is empty. Theorem11.7 applies directly with this upper
embedding bound sigma; we do not require that it equal the exact norm
named in Example11.8. At v=b+sigma t, t>0, its conclusion yields

 P(Y>b+sigma t)<=barPhi(hat_b+t)<=exp(-t²/2).                 (12)

At t=0 the bound1 is trivial. No negative-t assertion is made. This is a
norm shift on the actual Banach law, not a universal nonlinear solution
shift or an assertion of conditional independence of the driver blocks.

## 5. Integrating the tail with the full quadratic retained

Let R_2 be an auxiliary Rayleigh variable with tail exp(-t²/2), t>=0,
and density t exp(-t²/2). Equation(12), together with the trivial bound
below b, says Y is stochastically dominated by b+sigma R_2. This is a
comparison of scalar distributions only. For increasing nonnegative phi,
the expectation comparison follows first for tail indicators and finite
positive step combinations, then by monotone convergence; apply it to
phi(y)=exp(eta y^nu/delta). Integrability is NOT assumed in this step.
Convexity for1<nu<2 gives

 E exp(eta Y^nu/delta)
 <=exp(2^(nu-1)eta b^nu/delta)
   E exp(eta 2^(nu-1)sigma^nu R_2^nu/delta).                 (13)

Put A=eta 2^(nu-1)s^nu and change variable x=sqrt(delta)t in the Rayleigh
integral. The last expectation equals

 int_0^infinity (x/delta)exp((A x^nu-x²/2)/delta)dx.          (14)

For every A,x>=0 the following weighted AMGM bound holds:

 A x^nu<=x²/4+S,
 S=(2-nu)/2 (2nu)^(nu/(2-nu)) A^(2/(2-nu)).                  (15)

Here are the exact real-exponent guards, matching the existing Mathlib
Real.geom_mean_le_arith_mean2_weighted (complete type in the packet):
weights w1=nu/2 and w2=(2-nu)/2 are strictly positive and sum to1; bases
u1=x²/(2nu) and u2=A^(2/(2-nu))(2nu)^(nu/(2-nu)) are nonnegative.
Their weighted geometric mean is A x^nu: for A,x>0 expand powers, cancel
(2nu)^(-nu/2) with (2nu)^(nu/2), and use (x²)^(nu/2)=x^nu.
If A=0 or x=0 the same identity follows from strictly positive powers
of0, with no 0^0. The weighted arithmetic mean is x²/4+S. Denominators
2nu and2-nu are positive. Thus every premise and base in the existing
real-power theorem is satisfied; the old natural-power lemma is not used.

Substituting (15) into (14) proves FINITENESS and bounds it by

 exp(S/delta) int_0^infinity (x/delta)exp(-x²/(4delta))dx
 =2 exp(S/delta).                                         (16)

The factor2 is essential. Finally, nonnegative-base real-power algebra
(and the zero case separately) gives

 S=A_nu eta^(2/(2-nu))s^(2nu/(2-nu)).                        (17)

Taking logarithms after finiteness is established in (13)-(16) proves
the upper bound(3). The lower bound follows because exp(eta Y^nu/delta)
is at least1. This proves Proposition D1's finite-delta assertion.

## 6. Limits, controls, proof scope and the next obstruction

Equation(7) gives b<=2C g_delta->0, uniformly in J, since a<1. For fixed
J, let delta decrease to0 in (3); b^nu and delta log2 vanish, giving (4).
Next epsilon_J->0 at FIXED R, and 2nu/(2-nu)>0. The nonnegative lower
bound in (3) sandwiches the iterated limit and proves (5). No coupling
between different delta laws, joint limit, or delta-dependent J is needed.
This proves Proposition D1.

Falsification was done before proof investment: the retained18 rank-one
Gaussian integrals at40/60 digits, nu1 exact-CDF calibration and finite
arithmetic bounds agree. Nu1 is only a scalar calibration outside the
actual nu in(1,2). No certified quadrature enclosure is claimed; all
controls fix eta1 and do not establish the general eta power. The nu1.8,
epsilon1 bound is very loose (about2.6million versus about20); it cannot
validate a fine constant. At nu2 the
scalar Gaussian exponent is (eta epsilon²-1/2)t², so its integral diverges
at equality as well as above; for nu>2 the positive power dominates the
quadratic and the scalar moment diverges for any positive coefficient.
These endpoint declarations were analytically checked, not computed as
quadrature. A wrong CM scale g_delta gives divergent inverse-delta rates
in the retained scalar countermodel even though its mean norm vanishes.
The corrected epsilon power6 at nu1.5 also defeats the proposed power7
control. These are guards, not operator or SPDE evidence.

The existing Mathlib weighted AMGM type/axioms were checked locally at
the retained pin. This proof audits its actual real-weight application;
no new Lean theorem, module, package or official companion is created.
The73 finite facts/19 local seams remain unchanged. The Gaussian,
functional-analytic and asymptotic assertions here remain informal proofs.

D1 alone supplies no nonlinear Young-product or signed deterministic-wave
upper estimate. Nu<=p permits the elementary pathwise inequality
 delta sum_m||X_m||Ctheta^nu
 <=(delta n)^(1-nu/p)Y^nu,
by finite Holder (equality if nu=p); this explains the proposed speed's
use, but supplies no solution estimate to which it may be applied.
The accepted white translated controls refute uniform-R compact tails for
fixed finite smooth projections. D1 retains FIXED R and does not bypass
that guard. Growing-cone localization/entropy, nonlinear stability,
source-to-original POINT upper, matching constants and the intended source
normalization are still open. No reversal of F3, point Sobolev trace,
heat-error independence, source normalization repair or Skorohod result
has entered the proof. No human correspondence, HPC, publication, canonical
TeX/PDF/wiki integration or whole-paper clearance is requested or claimed.
