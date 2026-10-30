# Temporal equilibrium controls and a damped lower-endpoint comparison

CANDIDATE PROOF, not adopted. Preproof92f2e16 passed8groups/HIGH,
269.588seconds,15texts+2sourceimages,no requiredrepairs. Fullscientific
analytic/source/type/application review REQUIRED. Generalcomparisonbelow
has an explicit factor; globalfactor>=1 remainsOPEN. Oneactualwhitepoint
is closed. Original all-range/sharpupper/dimensional goal remainsACTIVE.

## 1. Actual model and scoped inputs

Fix originalreal d1 Gamma=c_Gamma|x|^-alpha dx for0<alpha<1,orwhite
Gamma=c_Gamma delta_0 atalpha=1,c_Gamma>0. Fix0<a<1,alpha+a<2.
Put q=4-alpha,k=3-alpha,m=q/k,d=q-2a>0. Allspaces/forms areREAL.

Use these accepted inputs at their exact scopes:
- occupation-control-approximation.md Sections1-6: B=L1 intersect L2,
  sum norm; X=L2((0,1);B); positive nonzero X_pos; actualpositive
  covariance/potential/form construction and rate I_psi; continuous raw
  covariance bilinear form B_Gamma. Positive smooth approximation gives
  the SAME real score values over C_pos and X_pos (SUP). No rough
  stochastic evolution is inferred. Its normalized real strong-H1,
  finite-integrated-energy occupation class is denoted O below.
- general-positive-consumer.md(24),(31)-(32): for the SAME original
  canonical Stratonovich point solution,
  Q2=liminf_(t->infinity)t^-kappa log E|u(t,0)|^2>=V2=2^m V1,
  kappa=(4-alpha-a)/k,where Vc=sup_Xpos(cI_psi-v_psi/2),c>0.
  Vc are positivefiniteREAL. V1 is an AUXILIARYscore value, not a
  firstmean theorem. Each rough score is consumed through fixed smooth
  approximants, not a new rough-flow construction or psi(delta).
- raw-positive-value-ceiling.md Sections2-3: spatialhomogeneity, actual
  covariance CS on X_pos and the scalar/spatial-dilation arguments.
  In particular normalizedrealH1g has b(g)=||g'||2^2>0 and
  A_sp(g)=int g^2(Gamma*g^2)<=C b(g)^(alpha/2),with C independent ofg.
  The covariance CS is for the actual Gaussian law, not kernelpositivity.

For z>0 use the source-SHAPED algebraicmap already checked there:

 F_b(z)=k[(q-2b)^((q-2b)/2)/(8(q-b)^(q-b))
                       *(2z/(2-alpha))^((2-alpha)/2)]^(1/k),
 Delta=[qlogq+(q-2a)log(q-2a)]/2-(q-a)log(q-a)>0,
 F_a(z)=exp(Delta/k)F_0(z).                                (1)

F0 changes the DISPLAYparameter only. The energies below are explicitly
defined, with no printed static M or disputed numerical value imported.
The point-second-moment label2 is ours; author(1.10) is a FIRSTmean map.

## 2. Self-contained temporal potential identity

For x>0 write Gamma(x)=int_0^infinity u^(x-1)e^-u du, and for x,y>0
Beta(x,y)=int_0^1 t^(x-1)(1-t)^(y-1)dt. These converge. Integration by
parts gives Gamma(x+1)=x Gamma(x). Tonelli and the change of variables
(u,v)=(R t,R(1-t)),Jacobian R, in the positive product Gamma integral
give Beta(x,y)=Gamma(x)Gamma(y)/Gamma(x+y).

We will use the positive binomial series
(1-z)^-p=sum_(n>=0)(p)_n z^n/n!,p>0,0<=z<1,
where (p)_0=1 and (p)_n=p(p+1)...(p+n-1). To justify it directly, the
series converges uniformly on every [0,z0],z0<1,by its coefficient ratio.
Termwise differentiation shows (1-z)y'=p y,y(0)=1. Multiplying by
(1-z)^p shows the product has derivative0, giving the claimed formula.
All series terms below are nonnegative, so Tonelli applies.

Put r=(1-a)/2 in(0,1/2) and w(t)=[t(1-t)]^-r. For0<s<1, split
J(s)=int_0^1 |s-t|^(2r-1)w(t)dt into its left and right parts.
Substituting t=su in the left part gives

 L(s)=s^r int_0^1 (1-u)^(2r-1)u^-r(1-su)^-r du
 =Beta(1-r,2r)s^r sum_(n>=0)
       (r)_n(1-r)_n s^n/[(1+r)_n n!].

The second equality follows from the binomial series and
Beta(n+1-r,2r)/Beta(1-r,2r)=(1-r)_n/(1+r)_n, using Gamma recurrence.
Since (r)_n/(1+r)_n=r/(r+n), a second positive binomial expansion gives

 L(s)=r Beta(1-r,2r) B_s(r,r),
 B_s(r,r)=int_0^s u^(r-1)(1-u)^(r-1)du.                  (2)

Indeed expansion of (1-u)^-(1-r) in B_s gives precisely the terms
s^(r+n)(1-r)_n/[(r+n)n!]. Reflection t->1-t makes the right part L(1-s).
Symmetry of the incomplete-Beta integrand gives
B_s(r,r)+B_(1-s)(r,r)=Beta(r,r). Consequently

 J(s)=r Beta(1-r,2r)Beta(r,r)=Gamma(r)Gamma(1-r).

All split integrals are finite: their local exponents are -r>-1 at
endpoints and2r-1>-1 at t=s. At s=0, the integral is directly
Beta(r,1-r)=Gamma(r)Gamma(1-r); s=1 follows by reflection. Thus, defining

 f_a(t)=[t(1-t)]^-r/[Gamma(r)Gamma(1-r)],0<t<1,

we have the EXACT identity for EVERYs in[0,1]

 int_0^1 |s-t|^-a f_a(t)dt=1.                            (3)

No higher-dimensional Riesz theorem was imported. The endpoint integrals
were evaluated separately, not inferred from an unjustified uniform limit.
f_a is nonnegative, nonzero and lies in L1 and L2: its squared endpoint
exponent is -2r=a-1>-1. Its mass is

 M_a=int_0^1 f_a(t)dt
 =Beta(1-r,1-r)/[Gamma(r)Gamma(1-r)]
 =Gamma((1+a)/2)/[Gamma(1+a)Gamma((1-a)/2)]>0.              (4)

For any positive nonzero phi in spatial B, the control psi(t,x)=f_a(t)phi(x)
lies in X_pos, since ||psi||X=||f_a||2||phi||B. Identity(3) gives the
actual q_psi,sigma=phi and h_psi,sigma=Gamma*phi, independent ofsigma,
up to their spatial representatives. The accepted raw-cost construction
and Tonelli give exactly

 v_psi=M_a int phi(Gamma*phi),
 I_psi=lambda(phi),                                      (5)

where lambda(phi) is the WHOLE-H1 Rayleigh rate of potential Gamma*phi.
It is the accepted variational rate; no H2 operator, eigenfunction or
Young flow for this rough control is being assumed. The mean need not
be pointwise bounded, and the actual X-form construction covers it.
No time-mass renormalization was made.

## 3. Spatial energy and an actual static-control lower bound

Let Fsp={realg inH1(R):||g||2=1}. For g inFsp set
b(g)=||g'||2^2,A_sp(g)=int g^2(Gamma*g^2). By the accepted spatial bound,
0<b,A_sp<infinity and A_sp<=C b^(alpha/2). Define the positivefiniteREAL
supremum R_sp=sup_Fsp A_sp/b^(alpha/2). Its set is nonempty (a normalized
compact smooth bump suffices), positive and bounded above.

Occupation dilation S_ell g(x)=sqrt(ell)g(ellx),ell>0,is an H1 isomorphism
and L2 unitary with inverse S_(1/ell). The ACTUAL Radon covariance scaling
gives A_sp(S_ellg)=ell^alpha A_sp(g),b(S_ellg)=ell^2b(g),includingwhite.
This is distinct from the Gaussian-test dilation D_s of the older note.
The same elementary one-variable maximum proved in rawvalue Section2,
with kinetic coefficient1/2, gives

 E_sp:=sup_Fsp[A_sp-b/2]
    =(2-alpha)/2*alpha^(alpha/(2-alpha))*R_sp^(2/(2-alpha)),
 R_sp=(2E_sp/(2-alpha))^((2-alpha)/2)*alpha^(-alpha/2).       (6)

For completeness the supremum argument uses only actual classes: all
S_ellg belong toFsp and ell1 includes allFsp, so E_sp equals the supremum
of the maxima of ell^alpha A-ell^2b/2. Each maximum is the first coefficient
in(6) times [A/b^(alpha/2)]^(2/(2-alpha)). Ratios bounded by R_sp give one
inequality; ratios approaching R_sp and continuity give the other. Thus
E_sp is finitepositiveREAL, with no optimizer or static SPDE theorem.
It has NOtemporal kernel and is not a source's disputed numerical M.

Fix g inFsp,write A=A_sp(g),b=b(g),R=A/b^(alpha/2)>0. For theta,ell>0
choose phi=theta(S_ellg)^2 inB, and psi=f_a tensorphi as inSection2.
Testing its wholeH1 Rayleigh form with S_ellg gives
lambda(phi)^2>=theta ell^alpha A-ell^2b whenever this is positive.
Its raw cost from(5) is M_a theta^2 ell^alpha A.

To exhibit ACTUALfeasible controls, put u=alpha/q>0. For any L>0 choose
ell=(uL^2/b)^(1/2),theta=(1+u)L^2/(ell^alpha A). Then
ell^2b=uL^2,theta ell^alpha A=(1+u)L^2, so the radicand is L^2>0.
Consequently the accepted variational score bound gives

 V1>=L-M_a/(2R)*(1+u)^2/u^(alpha/2)*L^q.                 (7)

All choices are fixed before the original time limit. The displayed u
also minimizes (1+u)^2/u^(alpha/2): its logarithmic derivative is
2/(1+u)-alpha/(2u), changing sign at alpha/q. No minimax assertion is used.
Maximizing the right side of(7) over L>0 is elementary: derivative1-qCL^k
with C=M_a(1+u)^2/(2Ru^(alpha/2)) changes sign once; its maximum is
(k/q)(1/(qC))^(1/k). Substituting u=alpha/q and q-1=k simplifies this to

 V1>=k[(R/M_a)*alpha^(alpha/2)/(8q^(q/2))]^(1/k).

Approximate the positivefiniteR_sp by ratios of g (no attainment) and
use(6). We obtain the actual lower value

 V1>=M_a^(-1/k) F_0(E_sp).                               (8)

Every rough test used is in X_pos and its score is the accepted smooth-
approximation value. No rough stochastic variable or static asymptotic
formula was introduced, and no supremum/time-limit interchange occurred.

## 4. The actual damped occupation energy and its upper comparison

Define, with the ORIGINALa,alpha and d=q-2a>0,

 K_star(u)=Gamma(a)^(-1)int_0^infinity
      exp[-(lambda+lambda^2/(2d))|u|]lambda^(a-1)dlambda.

It is positive/even/decreasing in |u|,finite for u!=0 and infinite at0.
Dropping only the quadratic damping and substituting |u|lambda gives
K_star(u)<=|u|^-a off0. Hence it is locally integrable for a<1; the time
diagonal has zero Lebesgue measure and no atom. Put
R_star=2int_0^(1/2)K_star(u)du in(0,infinity). Since Phi(s)=int_0^s K_star
is concave, the row at s in[0,1] is Phi(s)+Phi(1-s)<=2Phi(1/2)=R_star.
Equality holds at1/2, so R_star is the EXACT time-row maximum.

Let O be real stronglyH1-measurable g:(0,1)->H1 with ||g_s||2=1 a.e.
and T(g)=int_0^1 b(g_s)ds<infinity. Define our EXPLICIT own energy

 E_star^O=sup_(g inO){int_(0,1)^2 K_star(s-t)
             int_R g_s^2(Gamma*g_t^2) dx dsdt-T(g)/2}.      (9)

We justify its sharp comparison rather than use an arbitrary GN constant.
For any two positive spatial B inputs h1,h2, choose one nonzero positive
smooth time function chi in(0,1). The accepted covariance CS on X_pos,
applied to chi tensorh1 and chi tensorh2, cancels the same positive
factor int int K(s,t)chi(s)chi(t)dsdt and gives spatialcovarianceCS:

 int h1(Gamma*h2)<=sqrt[int h1(Gamma*h1) int h2(Gamma*h2)].

All integrals are finite by the accepted B near/far estimates. Applying
this deterministic inequality to each pair g_s^2,g_t^2, then(6), gives
interaction<=R_sp b(g_s)^(alpha/4)b(g_t)^(alpha/4).
SymmetricSchur with row R_star and time concavity on the unit interval
therefore bounds the positive interaction in(9) by
R_star R_sp T(g)^(alpha/2). In particular it is finite; it is also <=
the accepted finite raw interaction since K_star<=K.

Scalar maximization in T>=0 and(6) yield

 E_star^O<=sup_T[R_star R_sp T^(alpha/2)-T/2]
          =R_star^(2/(2-alpha)) E_sp.                    (10)

No dilation of a time-dependent g is needed here: dilation already gave
the exact spatial ratio relation(6). The new energy is positive: take a
constant-in-time normalized bump; its damped interaction is a positive
finite scalar times A_sp, and a small spatial dilation makes its alpha-
degree interaction dominate the quadratic kinetic term. Thus (9) is a
nonempty bounded-above REALsupremum with0<E_star^O<infinity before F is used.

Since F0(z) is proportional to z^((2-alpha)/(2k)), (10) gives
F0(E_star^O)<=R_star^(1/k)F0(E_sp). Combining(8),(1) and the accepted
Q2>=V2=2^mV1 proves for ALLactuald1parameters

 Q2>=2^m Omega(alpha,a) F_a(E_star^O),
 Omega=[M_a^(-1)/(R_star expDelta)]^(1/k)>0.               (11)

This is the actual original-point lower comparison. Amplitudes remain
in E_star^O; Omega is independent of c_Gamma. We have NOTproved Omega>=1
on the full range. Nor is E_star^O silently every possible reading of a
source variational constant. All three controls/energy/point links above
are needed; a raw-value ceiling cannot replace this lower argument.

## 5. A rigorous white point, with an exact gain

Now fix alpha=1,a=1/2. Then q=3,k=2,m=3/2,d=2,kappa=5/4.
For u>0, dropping ONLYexp(-u lambda) in the damped kernel gives

 K_star(u)<=Gamma(a/2)/(2Gamma(a))*(2d/u)^(a/2).

Indeed substitution v=u lambda^2/(2d) computes the remaining positive
Gaussian-Laplace integral exactly. Integrating over0<u<1/2 yields

 R_star<=B_star=(4/3)2^(-1/4)Gamma(1/4)/sqrt(pi).           (12)

Here Gamma(1/2)=sqrt(pi),Gamma(3/2)=sqrt(pi)/2. These follow by substituting
v=x^2 in Gamma(1/2) and the Gaussian integral: squaring int_R e^-x²dx and
using positive polarcoordinates gives2pi int_0^infinity r e^-r²dr=pi;
Gamma recurrence gives3/2. Therefore(4),(12) give

 M_a^-1/B_star=3pi 2^(1/4)/(8Gamma(3/4)).

Cauchy-Schwarz in the Gamma integral gives
Gamma(3/4)=int_0^infinity [t^(-1/2)e^-t]^(1/2)[e^-t]^(1/2)dt
<=Gamma(1/2)^(1/2)Gamma(1)^(1/2)=pi^(1/4).
Every factor is positive, so

 M_a^-1/R_star>=M_a^-1/B_star>=W:=3pi^(3/4)2^(1/4)/8.      (13)

At this point expDelta=2*3^(3/2)/(5/2)^(5/2). Positive real-power algebra
simplifies the exact ratio to

 [W/expDelta]^4=pi^3*5^10/(9*2^25).                       (14)

We use the classical explicitbound pi>157/50. Its exact imported finite
proof is Mathlib.Analysis.Real.Pi.Bounds,Real.pi_gt_d2 (3.14<pi), pinned
Lean/Mathlib4.35.0/Mathlib56a0058. Our local pi_cube_certificate and
rational_pi_gain compile it into the exact ratios needed here, with
complete public types retained. No Gamma or SPDE assertion is imported
from those scalar lemmas.

Let N=157^3*5^4=2418683125 and D=9*2^28=2415919104.
The local Natlemma exact_margin verifies N>D (difference2764021).
Since Omega^2=M_a^-1/(R_star expDelta), (13)-(14) give

 Omega^8>=pi^3*5^10/(9*2^25)>N/D>1.                      (15)

The strict middle inequality is exactly rational_pi_gain, whose type
retains both positive denominators, after casting the positive integers
into R. pi_cube_certificate separately confirms the weaker threshold
pi^3>9*2^25/5^10; it alone would not record the stronger rational gain.
Thus zeta=(N/D)^(1/8)>1 and Omega>zeta. Substituting into(11) proves
for the ORIGINALcanonical Stratonovich point solution with ANYwhite
covariance amplitude c_Gamma>0,

 liminf_(t->infinity)t^(-5/4)log E|u(t,0)|^2
      >=zeta*2^(3/2) F_(1/2)(E_star^O), zeta>1.            (16)

In fact the preceding strict Omega bound gives a strict comparison,
but(16) is the stated lower result. No spatial sharp optimizer or any
numerical value of E_sp/E_star^O was used. This is one genuine admissible
parameter point, not a claim that the global scalar condition is solved.

## 6. Source dictionary, calibrations and remaining goal

K_star in Section4 is exactly the kernel printed in authorversion
p4(1.13); (9) uses its p4(1.12) half gradient penalty. F_a is exactly the
algebraic map on p3(1.10). Both primary crops and sourceSHA5f7385ca...97b6c
are held in the review source context. The source(1.10) is a first-mean
statement; factor2^m here is from our accepted raw-score homogeneity and
point consumer, not an imported second-moment theorem.

E_star^O is EXPLICITLY defined over strong-H1-measurable finite-integrated-
energy/a.e.normalized O. Printed Ad gives every-sliceH1/unitmass and omits
time/integrated-energy details. Identifying (9) with a particular intended
source reading needs that domain dictionary; no silent renormalized meaning
or equality to all readings is asserted. The independent source-normalization
warning remains UNKNOWN. No raw E1/Ehalf is substituted for the damped
input, and neither sourcePDF nor canonical definitions are repaired.

This direct second-moment argument does not use an actualfirstmean lower
bound, signed observable restriction or source L. It proves no improvement
over the actual Jensen mean comparison. If a source lower constant is defined
using exactly(9), (16) gives its corresponding displayed p2lower endpoint
with a strictgain at the stated point; that is the precise conditional
source interpretation, not a normalization fix or full G:sharp theorem.

The full d1comparison(11) keeps Omega explicit. The nine old positive
numerical margins do not prove the global inequality M_a^-1>=R_star expDelta.
Original full a/alpha range, d2/d3 lower construction, sharp upper constant,
conditionalexact limit and source normalization remain open. Retained full
G:upper is untouched. Statica0 is excluded; f_a's L2 membership used a>0,
so no uniforma0 passage or disputedstaticM calibration is inferred. Noise
amplitude and kinetic/halfvariance factors stayed explicit. No Skorohod
asymptotic equality was assumed or developed.

The 15temporal quadratures remove the interior singularity but retain
integrable endpoint singularities. Attempt01rounded t to1 and returned
infinity; exactcode/writtenfailuremetadata preserved. Factorizedproduct/
expm1 successor retains precision/tolerance and is not a proof of(3).
All analytic steps are supplied above. Three local finite Nat/pi lemmas
have exactpublictypes/standardaxioms,5cleanfreshreplaymatches/2Falsecontrols;
their applications are Section5 ONLY. No formalBeta/Gamma/staticcontrol/
energy/point/SPDE certificate or officialpackage/companion/HPC gate.

Fullscientific analytic/source/type/application review is REQUIRED before
adoption. CanonicalTeX/PDF unchanged. This is an internal partialresult,
not wholepaper/coldread/novelty/circulation clearance or permission for
sourceauthorcontact/publicrelease. Full original goal remainsACTIVE.
