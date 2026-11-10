# Growing-cone transfer from the original point moment to the actual E flow

ACCEPTED at the scoped FULL analytic/source/type/actual-application gate:
scientific4c6d63e,actualOpus5.5/HIGH,13checksPASS,377.833seconds,no required
repairs. All22input bindings and complete native archive verified before
six optional clarifications,adjudicated in
reviews/2026-10-31-growing-cone-point-transfer/scientific-adjudication-v1.md.
Frozen proof/report preserved unchanged there. Exact transfer reduction only;
the growingR stochastic upper/sharpconstant/source goal remains OPEN.

## 1. Original model, geometry and exact new claim

Keep every original nonzero H:homog covariance Gamma and amplitude:
d in{1,2,3},0<a=alpha_0<1,0<alpha<d or alpha=d=1,alpha+a<2.
Gamma is even,nonnegative,positive definite,homogeneous and tempered Radon.
Choose auxiliary exponents
 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<beta<min(1-a/2,(3-a-alpha)/2),
which exist because alpha<2 and alpha+a<2,a<1. They are the accepted
actual-driver/source/Young ranges, not a new model restriction.
The original canonical Stratonovich solution u_Gamma has data(1,0), with
all mixed/unequal/empty chains and self-pairings in its moment construction.
The zero covariance case is included separately in Section8.

Use UNITARY Fourier transform and the inhomogeneous Bessel convention
 Lambda=(1-Delta)^(1/2), ||f||Hsigma=||<xi>^sigma fhat||2,
 E=H^(1/2) x H^(-1/2), F=E directsum R2,
with real Hilbert direct-sum norms. The canonical inclusion i:E->F is
isometric with closed range, not dense range. S_E and S_F are the FULL
massless wave groups. For a smooth physical coefficient b,
 B(b)(v,w)=(0,bv) on E. Both displacement and physical velocity are retained.

Set
 kappa=(4-alpha-a)/(3-alpha)>1,0<delta<1,
 L=1/delta,T_delta=delta^(-1/kappa),g=delta^((1-a)/2),
 Gamma_delta=g^2 Gamma.
Fix real even eta in C_c^infinity,0<=eta<=1,eta=1 onB1,suppeta subsetB2.
Put
 R=L+2, eta_R(x)=eta(x/R),m=eta_R^2,psi=eta_R,z=(psi,0),
 D=B1(0),v_d=Lebesgue volume(D)>0,
 K={(t,x):0<=t<=L, |x|<=1+L-t}.                              (1)
The physical NOISE mask is m ONCE, after source smoothing. psi is its
root used as initial displacement, not a second noise mask. The cone K
is compact and causally closed: if (t,x) is in K,0<=s<=t and |y-x|<=t-s,
then |y|<=1+L-s. Its entire spatial projection lies inside B_(R-1), so
both psi and m equal1 on a neighbourhood of all needed cone points.

Let W be the GIVEN slow raw isonormal noise, W_fast(f)=W(T_(delta,0)f),
where the accepted raw pullback is an isometry. Let M_E be the actual
masked E FIRST interaction driver M_R(W_fast) on[0,L], and D_E=g M_E.
The actual E Young evolution is U_E, with physical flow
 P_E(t,s)=S_E(t)U_E(t,s)S_E(-s),P_delta=P_E(L,0).             (2)
This is a B(E)-driver construction. The F-to-E column extension in the fixed-mask note uses an auxiliary
L_(tildepsi),where tildepsi=1 near its larger localization chi; it is NOT
the datum psi=eta_R. Our E Young driver is D_E=g M_E. With amplitude g
the actual F driver satisfies i^-1 A_F i=D_E. No new spectral flow or
raw point trace defines P_delta.

We prove the EXACT point-moment identity and upper reduction
 E|u_Gamma(T_delta,0)|^2
   =v_d^-1 E||pr1 P_delta z||L2(D)^2
   <=v_d^-1||psi||H1/2^2 E||P_delta||B(E)^2,                 (3)
and
 limsup_(T->infinity)T^-kappa log E|u_Gamma(T,0)|^2
   <=limsup_(delta->0)delta log E||P_delta||B(E)^2.           (4)
All source limits are taken FIRST at fixed delta,R,L. The right side of
(4) still needs a growing-mask stochastic operator upper bound with the
correct constant. Neither accepted fixed-R GL nor a linear Cameron estimate
supplies that rate. Equation(4) is a reduction, not the sharp theorem.

Direct OWN accepted inputs, exact scope:

- fixed-mask-moment-transfer.md Sections1,4,5,scientific604c60f: ordinary
  full-source locally continuous/jointly measurable solution; absolute L2
  Picard-series control uniform in space/cutoffs; spatial stationarity;
  and FULL unmasked source POINT second-moment limit(11). These depend on
  the source law and continuous version, not a particular realization of
  a whole auxiliary source family. Its lower-direction F3(12) is NOT used.
- fixed-mask-young-constant-phase.md Sections2-5,scientific8ad5094: full
  distributional free phase on E plus constants, including d3 derivative
  Green entries and finite propagation of TOTAL data; actual F driver
  restriction A_F i=i M_E; Young uniqueness/inverse; all-finite-Lp source
  flow differences; ordinary source Duhamel identity ON STATES. Its scalar
  identification for e0 alone is not presumed to cover psi: Section4 here
  proves the compact-data identification.
- source-operator-convergence.md Theorems1-2,Sections6-7,scientificda9d464:
  retaining sources,Gaussian contraction/test transfer,spatial smooth/time
  continuous source versions,actual source FIRST response identity on E.
- raw-block-event-lower.md Sections7-8,scientificd4d876e: actual fast-source
  pullback,testwise convergence and exact unmasked law scaling preceding(26).
  No positive-control lower bound or comparison(25) is reversed.
- direct-event-calibration.md Section1(S)-(M),scientific9d77f90: exact
  original canonical scaling,Green MEASURES/all mixed and self-pairings,
  source limits before large time,d3 Green-before-noise convention. Four
  old scalar Lean types are reused only within their explicit scope.
- upper-gaussian-operator.md GL,scientific180bf1a: actual full-F moment
  FINITENESS for each fixed delta,R; no fixed-R RATE on a growing diagonal.

## 2. Actual E/F restriction, measurability and fixed-parameter moments

Fix delta throughout Sections2-6. The accepted actual F extension obeys
 A_F(t)i=i D_E(t), S_F(t)i=i S_E(t), simultaneously in t on a path set.
These also hold for every fixed positive source parameter pair. They are
literal driver/free identities, not a density argument on F.

For each initial e in E, i U_E(t,s)e solves the F state Young equation
with initial i e: apply i to its Young sums and use A_F increments times
i=i times D_E increments. The bounded linear inclusion commutes with the
Young limit. State uniqueness on each local contraction interval and then
patching give U_F(t,s)i=i U_E(t,s). Equality extends to all states and
all time pairs by boundedness and the constructed evolution; no event for
all uncountably many delta or cutoffs is needed. The free identities imply
 P_F(t,s)i=i P_E(t,s), ||P_E(t,s)||B(E)<=||P_F(t,s)||B(F),    (5)
and the same isometric restriction bound for differences of source/raw
physical flows. This is a DEFINITE input to this proof, not optional.

The accepted F source convergence in the uniform time-triangle operator-
difference norm therefore yields the E convergence in every finite Lp
whenever the actual retaining source first drivers converge. Section3
checks that convergence for our fast pullback, not a newly selected source.
Actual E Young evolution is invertible: on a small interval its interaction
operator is within1/3 of I by the accepted contraction estimate, hence has
a Neumann inverse; products and free-group inverses give the global inverse.
This does not assume symplectic conservation or surjectivity from a form.

At the endpoint, the Young map is continuous on the separable closed span
of the actual first-driver paths. Its bounded physical conjugation and
restriction preserve strong measurability into their separable image, even
though all B(E) need not be separable and S_E is not norm continuous.
The operator norm and the E/L2(D) evaluations used below are measurable.
We instantiate GL with this SAME admissible theta. If two admissible
exponents are compared,the actual driver versions agree on literal rows
and rational times,then as paths; both Young solutions belong to a common
lower admissible Holder class,where uniqueness identifies them.

GL's supported-noise hypothesis is also exact. A fast row up to L has
slow pullback supported in[0,delta L]=[0,1]. Smooth interior approximations
to endpoint indicators converge in the raw covariance norm,because a<1
and the masked spatial support is compact with finite Radon covariance
mass. Thus its completion belongs to the closed H_I. The same holds for
the genuine F constant columns. Countable dense state/rational-time Gaussian
coordinates identify the first paths with the construction from W restricted
to H_I,and the Young map adds no noise. The present endpoint is therefore
GL's actual given-noise flow,not merely an equal-law substitute.
GL FINITENESS applies to the single finite pair (delta,R=L+2), and (5) gives
            0<E||P_delta||B(E)^2<infinity.                  (6)
The strict positivity follows from invertibility on nonzero E. GL's fixed-R
asymptotic score is never used here along R=L+2.

## 3. Same retaining source and exact fast law

On the accepted extension retaining W, take ONE slow source
Y_(epsilon,tau),epsilon,tau>0,with its continuous-time/smooth-space version.
Define its actual fast pullback
 Y_fast(t,x)=delta^(a/2)Y_(epsilon,tau)(delta t,x).            (7)
For a fast test f, this is Y_(epsilon,tau)(T_(delta,0)f).
The raw pullback is an isometry; hence the accepted slow-source covariance
contraction and vanishing test-error variance imply, at this fixed delta,
 Var Y_fast(f), Var((Y_fast-W_fast)(f))<=||f||H_fast^2,
 Var((Y_fast-W_fast)(f))->0.                               (8)
The jointly Gaussian families retain W_fast as an actual variable, not an
equal-law replacement. Generic Gaussian transfer on[0,L] gives
 M_R(Y_fast)->M_R(W_fast) in every finite Lp Ctheta(B(E)),    (9)
for admissible theta>1/2. Multiplication by the fixed g and the bounded F
extension transfer(9) to the drivers used in Section2. More explicitly,
Gaussian transfer with covariance bound1 and the accepted raw-driver
sqrt(p) moments give uniform-in-rho sqrt(p) first-path moments at this
FIXED delta,R,L,also after g and the bounded F extension. The elementary
moment-series argument gives uniform square-exponential path norms.
The accepted Young bound has growth exp(C(1+||A||)^(1/theta)),with
1/theta<2. Local-Lipschitz convergence on bounded driver balls first gives
probability convergence; those exponential tails give all finite moments
and uniform integrability,exactly as in fixed-mask Y3. Thus its upgrade
applies to this actual fast pullback family as well. The source Young/
physical E flows, denoted P_E^rho, therefore satisfy
 E sup_(s<=t<=L)||P_E^rho(t,s)-P_E(t,s)||B(E)^2 ->0.          (10)
Here rho=(epsilon,tau); arbitrary joint rates are allowed. Radius/horizon,
free conjugation constants,g and z may depend on delta but are fixed while
rho tends to0. There is no uniform-in-delta source estimate or limit swap.

For clarity, the ordinary source identity also applies to this ACTUAL
pullback. On Schwartz E states its ordinary first primitive with coefficient
b_rho(t,x)=m(x)g Y_fast(t,x) has row g Y_fast(h_R,t;z,w), exactly the row
of g M_R(Y_fast). The source regularity and indicator-test approximation
in source-operator-convergence.md Section7 identify this with the statewise
integral int S_E(-r)B(b_rho(r))S_E(r)dr. Countably many dense states and
rational times, then boundedness/continuity, identify the operator paths.
Thus P_E^rho is the ACTUAL ordinary Duhamel flow for b_rho and all E data.

The fast source has the canonical law at a different cutoff. With
 K_tau(v)=Gamma_E(a)^-1 int_0^(tau^-1)exp(-lambda|v|)lambda^(a-1)dlambda,
substitution lambda'=delta lambda gives
             delta^a K_tau(delta v)=K_(tau/delta)(v).
Consequently the field g Y_fast has covariance
 K_(tau/delta)(t-s) Gamma_delta,2epsilon(x-y),               (11)
where Gamma_delta,2epsilon=p_(2epsilon)*Gamma_delta and
Gamma_delta=g^2Gamma. The two-source shared-width max/heat-sum convention
is preserved as well. Positive multiplication by g^2 keeps Gamma_delta in
EVERY original admissible covariance class, including the d1 white endpoint.
At fixed delta,(epsilon,tau/delta)->(0,0). The full source theorem F(11)
therefore applies to the single-source law in (11) and its continuous
version. It need not be the literal independently constructed Theorem2
source family for Gamma_delta on a different Gaussian space.

## 4. Compact-data ordinary source displacement is a scalar mild solution

Fix delta,rho and a probability-one regularity event for the pointfield.
b=b_rho is compactly supported in B_(2R), spatially smooth, and continuous
in time in every bounded spatial derivative norm on[0,L]. Its derivative
bounds are finite SAMPLE constants. No expectation of a global unmasked
noise supremum, and no raw higher regularity, is asserted.

Choose an integer k>d/2+1 and E_k=H^k x H^(k-1). In Bessel-unitary
coordinates the free matrix is the same bounded Fourier matrix as on E:
 [cos(t|xi|),<xi>sin(t|xi|)/|xi|;
  -|xi|sin(t|xi|)/<xi>,cos(t|xi|)],
with value t for the sine quotient at zero. It is uniformly bounded on
finite horizons and strongly continuous by dominated Fourier convergence.
Thus S(t) is a strongly continuous group on E_k, with a bound C_L.

For integer k, Leibniz's formula and the equivalent derivative norm give
 ||b(t)f||H^(k-1)<=C_k max_(|j|<=k-1)||partial^j b(t)||infinity
                                      ||f||H^(k-1).
The derivative norm equivalence follows by expanding (1+|xi|^2)^(k-1)
and Plancherel. Therefore B(b(t)) is a bounded operator on E_k with a finite
uniform sample bound B_L, continuous in operator norm there by the same
estimate on b(t)-b(s). The initial z=(psi,0) belongs to every E_k.

Define phase Picard terms Z_0(t)=S(t)z,
 Z_(n+1)(t)=int_0^t S(t-r)B(b(r))Z_n(r)dr.
Their statewise Bochner integrands are continuous, and iteration gives
 sup_(t<=L)||Z_n(t)||E_k
       <=C_L^(n+1)B_L^n L^n/n! ||z||E_k.                   (12)
The series converges in C([0,L];E_k) to Z(t), and summing the bounded
Volterra map gives its Duhamel equation. The same factorial estimate on
a difference proves uniqueness (iterate the homogeneous Volterra equation
n times and let n tend to infinity). Since E_k embeds continuously into E,
this is also an E Duhamel solution; uniqueness in E and Section3 identify
        Z(t)=P_E^rho(t,0)z.                                (13)
The higher norm is used ONLY to identify the smooth-source solution.

Fourier Cauchy-Schwarz gives ||fhat||1<=||f||Hk
(int <xi>^(-2k)dxi)^(1/2)<infinity for k>d/2. Fourier inversion/dominated
convergence imply H^k embeds continuously into bounded continuous functions.
Thus v_rho(t,x)=pr1 Z(t)(x) has a jointly continuous version; k-1>d/2
also gives a continuous source velocity. Measurability follows directly
from the construction: on the fixed compact support the source derivatives
form a measurable C_t C_x^(k-1) random element (countable dense evaluations
and continuity); Picard iteration and local norm estimates make Z a measurable
C_t E_k element. Continuous Fourier embedding gives the stated jointly
measurable displacement. This is source regularity, not a raw point trace.

Taking the first component of the phase equation yields, as distributions,
 v_rho(t)=C(t)psi+int_0^t G_(t-r)*(b(r)v_rho(r))dr,
                         C(t)=cos(t|D|).                    (14)
This is also a pointwise scalar mild identity. Indeed b(r)v_rho(r) is
continuous and compactly supported, with finite uniform L1 and sup bounds
on this horizon. The positive displacement Green measure has mass t-r
and support in B_(t-r), in ALL d=1,2,3; d3 is a sphere measure. Against
a compact smooth test phi, absolute Fubini is bounded by
 int_0^t ||phi||infinity ||b(r)v_rho(r)||1(t-r)dr<infinity.
It therefore matches the distributional Duhamel term. Writing G_h as h
times a dilation of its unit-time probability measure and using continuity
proves that term continuous in(t,x), so the distributional identity agrees
everywhere with the continuous versions. The free C(t)psi is continuous
by the same Sobolev/Fourier argument. No Green density in d3 is introduced.

## 5. Exact equality throughout the cone and the squared spatial average

Let u_rho^full be the ordinary UNMASKED source solution with coefficient
g Y_fast and data(1,0). Accepted F Sections1,4 applied through (11) supply
its locally continuous,jointly measurable scalar mild version, agreeing
at every fixed point with its L2 Picard sum. We do not place this global
unmasked field in E or F. Spatial stationarity and a finite Q_L bound hold
by the same source law; fixed parameters may affect Q_L. Its pathwise
compact-cone Picard construction needs only continuity and boundedness
of the realized field there. Its L2 point identification and stationarity
use only the law (11),not a particular retaining-family representation.

The TOTAL free initial difference between v_rho and u_rho^full is
(psi-1,0). It belongs to E plus constants: (psi,0)+(-1,0). Although neither
constant is in E, the accepted full distributional matrix on F represents
this total phase. The top-left kernel is partial_t G_t, not G_t; all
four entries are compactly supported distributions in B_t. Since psi-1
vanishes on B_R and |x|+t<=1+L=R-1 throughout K, this entire translated
kernel support lies a positive distance inside the region of vanishing
data. Full-phase finite propagation gives
                      C(t)psi(x)=1, (t,x)in K.             (15)
This handles both initial components and the derivative initial kernel,
including d3. Checking the E and constant summands separately would be wrong.

Inside K the physical mask m equals1. Causal closure of K in (1), (14),
(15), and the full scalar mild equation show that w=v_rho-u_rho^full obeys
 w(t,x)=int_0^t int G_(t-r,dy) gY_fast(r,x-y)w(r,x-y)dr
for all(t,x)in K. Let H=sup_K|w|<infinity and M=sup_K|gY_fast|<infinity,
finite sample bounds on this compact cone. Iterating the equation n times
with positive Green MEASURES of mass t-r gives
              |w(t,x)|<=H M^n t^(2n)/(2n)!, (t,x)in K.      (16)
For example the mass recursion is f_0=1,
f_(n+1)(t)=int_0^t(t-r)f_n(r)dr, giving t^(2n)/(2n)!.
The factorial ratio forces the right side of (16) to zero for every fixed
finite L,M. Therefore
                  v_rho(t,x)=u_rho^full(t,x) on K.          (17)
No positivity of the sample potential, global Gaussian supremum estimate
or multiplication of scalar solution moments across blocks is used.
Events are per fixed delta,rho; no common event over uncountable cutoffs.

At time L the cone contains D. Tonelli, joint measurability, source
stationarity and the finite source point moment imply
 E||v_rho(L)||L2(D)^2
   =int_D E|u_rho^full(L,x)|^2 dx
   =v_d E|u_rho^full(L,0)|^2<infinity.                      (18)
This is an average of SQUARES, not a squared average or a reversed masked
covariance inequality. It proves the proposed GC1.

## 6. Source limits, canonical point law and the E operator upper

By (10), for this fixed deterministic z and fixed delta,
 ||pr1(P_E^rho(L,0)-P_E(L,0))z||L2(Omega;L2(D))
 <=||z||E ||P_E^rho(L,0)-P_E(L,0)||L2(Omega;B(E))->0.        (19)
Here L2(D)<=L2(R^d)<=H1/2 under the stated Bessel convention. Consequently
the second moments of those L2(D)-valued displacements converge: the
absolute difference of their expected squared norms is at most the L2
norm of their difference times the sum of their L2 norms. These norms
are finite and converge by (19). This is a raw spatial-L2 statement only.

Separately, accepted FULL source point-moment limit F(11), with the exact
law (11), gives
 E|u_rho^full(L,0)|^2 -> E|u_(Gamma_delta)(L,0)|^2.            (20)
It uses arbitrary joint rates for (epsilon,tau/delta), which tend to zero
at this FIXEDdelta. Taking these two distinct limits in equal prelimit
moments (18) proves the exact identity
 E|u_(Gamma_delta)(L,0)|^2
                  =v_d^-1 E||pr1 P_delta z||L2(D)^2.         (21)
No canonical point value is identified with a raw E point trace.

We use the following IMPORTED consequence of the accepted canonical
calibration and raw-block Section8; the time-change paragraph recalls
that input's normalization rather than independently re-proving the
canonical-series scaling. We recall the exact original point-law normalization. By the accepted
calibration, with delta=T^-kappa and r_T=T delta, V_delta(t,x) has the
canonical law of u_Gamma(Tt,r_T x) and equation
 delta^2 V_tt=Delta V+sqrt(delta) W V,data(1,0).
At ordinary positive source widths set U(t,x)=V_delta(delta t,x). Its
coefficient is sqrt(delta)Y_slow(delta t,x)=g Y_fast(t,x), so its fast
source law has covariance Gamma_delta as in (11). At time L=1/delta,
U(L,0)=V_delta(1,0). The accepted source/canonical-series argument in
raw-block Section8 preceding(26) passes this time change to raw point
moments at fixed delta, retaining all mixed,self/empty chains and d3
Green-before-noise limits. Thus
 E|u_Gamma(T_delta,0)|^2=E|u_(Gamma_delta)(L,0)|^2.            (22)
This is a LAW/moment identity, not a claimed pathwise equality of two
canonical solutions driven by the same unscaled noise. The E source/raw
construction itself retains the given W_fast on its actual coupled space.
The shrinking radius r_T is not R. No spatial Jacobian appears at point0;
(18) was a fixed-ball average in the fast coordinates, not an unnormalized
change of spatial integration variable in the original model.

Combining (21)-(22) with the Hilbert phase/operator inequality gives
 E|u_Gamma(T_delta,0)|^2
 <=v_d^-1||z||E^2 E||P_delta||B(E)^2
 = v_d^-1||psi||H1/2^2 E||P_delta||B(E)^2.                   (23)
This proves GC2. The canonical point moment is strictly positive: its
absolutely convergent nonnegative pairing expansion contains the empty
pair of chains with value1, as in accepted F Sections2-5. This also holds
by the source point-moment limit. Together with (6), all logarithms below
are well defined and finite at each fixed delta.

## 7. Polynomial data cost and limiting reduction

Unitary Parseval and the inhomogeneous Bessel weights give
 ||psi||H1/2^2<=||psi||H1^2=||psi||2^2+||grad psi||2^2
   =R^d||eta||2^2+R^(d-2)||grad eta||2^2
   <=C_eta R^d, C_eta=||eta||2^2+||grad eta||2^2>0,           (24)
since R>=1. This is valid in all three dimensions, including the negative
d-2 exponent for d1. Let A_delta=v_d^-1 C_eta(delta^-1+2)^d. Then
 delta log A_delta
   =delta log(C_eta/v_d)+d delta[log(1+2delta)-log delta]->0. (25)
For example put r=-log delta->infinity; r exp(-r)->0 by
exp(r)>=r^2/2, proving the only nontrivial elementary logarithmic limit.

The original class gives alpha<2<3,a<1, so kappa>1. For positive delta,
log T_delta=-(log delta)/kappa and therefore T_delta^-kappa=delta.
This inverse parametrization/bijection is an elementary ANALYTIC positive-
real-power step, not an additional Lean-certified declaration. The map
0<delta<1 to 1<T_delta<infinity is a decreasing bijection. Take delta log
of (23), use (24)-(25) and that bijection, and obtain exactly (4). The
prefactor has finite normalized logarithm tending to zero, so no difference
of infinite quantities is used, even if the right limsup is infinite.
This proves GC3 for nonzero Gamma.

## 8. Zero covariance, calibrations and finite-evidence boundary

If Gamma=0, canonical u=1, all source/raw first drivers vanish and
P_delta=S_E(L). The compact-data free wave still equals1 on K by (15),
so (18),(21),(22) and (23) hold without source randomness. The full Fourier
fiber matrix in Section4 has determinant1 at every frequency, including
the triangular zero-frequency value. For a real 2x2 matrix its determinant
has magnitude at most the product of its column lengths, hence at most its
operator norm squared. Thus each fiber norm is at least1; Fourier multiplier
norms (equivalently complexification of the real group) give ||S_E(L)||>=1.
The elementary Fourier upper bound is C(1+L). Therefore
 0<=delta log||S_E(1/delta)||^2<=2delta log[C(1+1/delta)]->0,
and (4) is the trivial zero<=zero. No unreviewed SP conservation theorem
is used. The original canonical spatial stationarity, proved by translating
all finite source chains and then taking the accepted limits, extends the
point-moment statement from0 to any fixed x without changing constants.

The formal a->0 value of kappa is (4-alpha)/(3-alpha), consistent with
the time-independent calibration; the theorem itself keeps0<a<1. We did
not alter the p1 theorem, Jensen lower bound, or any accepted original p2
lower estimate. Exact source equality and moment scaling do not discard
Stratonovich self-pairings; they give no Skorohod result. No sharp constant
or equality of own signed scores with author L^* is asserted.

Existing DirectEvent.kappa_gt_one,physical_scale,noise_scale,vertex_scale
are reused at T_delta>0,alpha<3,a<1 with complete source/public-type evidence
in the frozen packet. Their real-power statements remain unchanged; the
Gaussian/Green/canonical-series scaling is the accepted analytic input.
The inverse T_delta parametrization, H1 scaling, source PDE, Fubini, cone,
E/F restriction and raw limits in this note are ANALYTIC. There is no new
Lean theorem/compiler/count:74facts20seams/L0 PROPOSED, companion decision4
unchanged. Calibration scripts were retained, not rerun; their fragile
floating exact-equality guard supplies no proof premise or enclosure.

The missing growingR stochastic operator upper and intended author energy/
normalization dictionary remain open. This note proves the scoped independently reviewed transfer
REDUCTION only,not the original sharp upper or conditional exact limit. No TeX/PDF/wiki/bib/sourcePDF/sibling/
Skorohod/contact/HPC/companion or publication action is taken here.
