# White spatial energy and explicit bounds for the derived moment constant

AUTHOR PROOF, UNREVIEWED. WS FIT passed26checks/HIGH at sourcead9fe4d,
276.215seconds; this new full analytic proof has NOT passed its own gate.
The two finite conditional algebra steps are kernel checked, not the H1,
CDF or model assertions below. Le's goal is the actual computed constant,
without forcing Chen's prediction. The all-model PB/OC theorems are retained;
this section evaluates a concrete example, not a reduced target.

## 1. Exact model, imports and statements

Take d=1,alpha=1,0<a<1 and physical spatial covariance Gamma=c delta_0,
c>=0. The temporal covariance is |s-t|^-a, with no H(2H-1) multiplier.
The wave equation has kinetic coefficient1, initial data(1,0) and the
Stratonovich product. Thus sqrt(c) would be the coefficient of unit noise;
c itself is covariance MASS, not an auxiliary moment label.

OWN accepted inputs, exact roles:
- PB=physical-signed-positive-score-comparison.md, scientific40ec9a9,
  PB5: for the SAME original canonical point solution and every fixed x,
  C2(c,a)=lim_(T->infinity)T^(-(3-a)/2)log E|u(T,x)|² exists and has
  the intrinsic positive raw-control variational formula. It is0 atc0.
- OC=all-model-occupation-ceiling.md,scientific25cc688,Section6(18):
  for this same C2 atalpha1,k2,m3/2,
  2^m M_a^(-1/k)F0(E_sp)<=C2<=2^m K0(a)^(1/k)F0(E_sp),
  M_a=Gamma_E((1+a)/2)/[Gamma_E(1+a)Gamma_E((1-a)/2)],
  K0(a)=2^a/(1-a).
  Here Gamma_E is Euler's Gamma, not the spatial covariance. Both factors
  are positive finite for0<a<1. The static energy and F0 are defined below.
- B=all-dimensional-static-occupation-bridge.md,249e2c4,Sections3-4:
  R_sp and E_sp use the FULL real L2-unit H1 class, with equality to the
  compact-approximation values when needed. Physical pairings are actual
  Gamma measure integrals. In this example
   B_Gamma(f²,f²)=c int_R f(x)^4dx,
   R_sp=sup_(realunitH1) c int f^4/||f'||2,
   E_sp=sup_(realunitH1)[c int f^4-||f'||2²/2].           (1)
  The static penalty1/2 is a defined variational object; it does not change
  the wave generator, whose Rayleigh kinetic coefficient remains1.
- global-d1-damped-lower.md,scientificee188ab,Section3(5) and its named
  scalar Gamma inputs: duplication, recurrence and Gamma_E(1/2)=sqrt(pi).
  These identities are for positive real arguments, with no model change.
- WhiteCDF.cdf_square_bound and WhiteCDF.energy_upper, complete printed
  types in lean-progress/local-checks/white-cdf-v1/: the finite conditional
  deductions specified in Section3. Their analytic hypotheses are proved
  here. No new axiom or formal H1/CDF/integral theorem is imported.

We prove R_sp=c/sqrt3 and E_sp=c²/6 for c>0. Consequently

 (2/3)sqrt(c/M_a)<=C2(c,a)<=(2/3)sqrt(c K0(a)).           (2)

For c>0 the ratio of these BOUNDS satisfies
 U/L=sqrt(K0(a)M_a)
    <=rho_*=[sqrt(pi)/(2Gamma_E(5/4)²)]^(1/2),           (3)
with equality at a1/2. These are not claims that C2 equals either bound
or that its intrinsic supremum has been numerically optimized.

## 2. Full-H1 representatives and the CDF square identity

Let f be REAL H1(R) with ||f||2=1. Choose its locally absolutely continuous
representative: on any bounded interval subtract the primitive of the weak
derivative f'; the difference has weak derivative0, hence is a.e. constant.
The last fact follows by testing against derivatives of compact smooth
primitives of all zero-integral test functions. The local representatives
patch on overlapping intervals. In particular f is continuous, and
q=f² is locally absolutely continuous with q'=2ff' a.e. Cauchy-Schwarz
gives q' inL1(R), while q inL1 has integral1 and is nonnegative.

Because q' is integrable, q has finite limits at both infinities: for large
x,y on the same tail, |q(x)-q(y)|<=int_tail |q'|. Its L1 integrability
forces both limits0. Therefore q is bounded and
 A=int_R f^4=int q²<=||q||infinity int q<infinity.
Put b=int_R(f')²<infinity and F(x)=int_(-infinity)^x q(y)dy.
Then0<=F<=1, F is C1 with F'=q, and F(-infinity)=0,F(infinity)=1.
These statements require no positivity of f itself or strict increase of F.

The product q(1-2F) is locally absolutely continuous and has derivative
q'(1-2F)-2q² inL1. Its endpoint limits vanish because q->0 and |1-2F|<=1.
Integrate this derivative on[-R,R] and let R->infinity, using absolute
integrability. Since q'=2ff', this proves

                  int_R f'f(1-2F)=A.                   (4)

Next P(y)=y-2y²+(4/3)y³ has derivative(1-2y)². The chain rule gives
(P(F))'=q(1-2F)², which is integrable since it is bounded byq. Integration
on[-R,R] and the two limits of F give

 int_R f²(1-2F)²=P(1)-P(0)=1/3.                        (5)

For EVERY real z, f'-z f(1-2F) lies inL2: its two terms do because F
is bounded. The cross product is absolutely integrable by Cauchy-Schwarz.
Thus pointwise square expansion and(4)-(5) legitimately give the REAL identity

 int_R [f'-z f(1-2F)]²=b-2zA+z²/3>=0, EVERY real z.    (6)

No undefined subtraction of infinite integrals, endpoint term or positive-f
assumption is hidden. This proves Lemma WS:CDF.

## 3. Sharp spatial ratio and energy, including the kernel consumers

Equation(6) supplies exactly the hypothesis of the PUBLIC conditional
WhiteCDF.cdf_square_bound, with A=int f^4 and b=int(f')². Its conclusion is

                            3A²<=b.                    (7)

Its kernel proof is the finite substitution z=3A; all representative,
integrability and integration facts proving its premise are Section2's
analytic work, not Lean-certified here. A>0 for a unit profile. Also b>0:
if f'=0, its absolutely continuous representative is constant, and the
only L2 constant is0, contradicting unit norm. Hence(7) gives A/sqrt(b)<=1/sqrt3.

For ell>0 define f_ell(x)=sqrt(ell/2)sech(ell x), sech=1/cosh.
It is a real smooth H1 profile, with f_ell'=-ell tanh(ell x)f_ell.
Substituting t=tanh(ell x) and dt=ell sech²(ell x)dx yields

 int f_ell²=(1/2)int_(-1)^1 dt=1,
 int f_ell^4=(ell/4)int_(-1)^1(1-t²)dt=ell/3,
 int(f_ell')²=(ell²/2)int_(-1)^1 t²dt=ell²/3.            (8)

Thus every f_ell attains the ratio1/sqrt3, and the physical measure identity
in(1) gives R_sp=c/sqrt3 for c>0. There is no Fourier normalization factor
and no substitution of the nonintegrable kernel |x|^-1 for delta_0.

The PUBLIC conditional WhiteCDF.energy_upper applies to(7) and the actual
physical covariance mass c, giving cA-b/2<=c²/6. Explicitly its finite
completion is
 cA-b/2<=cA-(3/2)A²
        =c²/6-(3/2)(A-c/3)²<=c²/6.                     (9)
The private compiled actual_energy_consumer composes the two public
deductions, with exactly the same all-real-z premise(6). Neither finite
statement proves the CDF premise or the admissible attainment.

At ell=c>0, (8) gives cA-b/2=c²/3-c²/6=c²/6. This is an admissible FULLH1
profile in(1), proving the reverse supremum bound. Therefore

                    R_sp=c/sqrt3, E_sp=c²/6.            (10)

The parent B already proves compact/full-H1 equality through density and
physical covariance continuity. We evaluate that full-H1 energy; no
noncompact soliton is directly asserted to be a smooth compact stochastic
control. This proves Proposition WS:spatial.

## 4. Actual moment bounds and the zero case

At alpha1, q3,k2,m3/2, OC's map is
 F0(z)=2[(2z)^(1/2)/(8*3^(3/2))]^(1/2).
For c>0, (10) gives(2E_sp)^(1/2)=c/sqrt3, so
 F0(E_sp)=2 sqrt(c/72)=sqrt(c)/(3sqrt2),
                 2^m F0(E_sp)=(2/3)sqrt(c).            (11)
Substituting(11) in the accepted OC common-spatial-energy bracket proves
(2) for the SAME original point limit. This is a calculation in the
original units, not a fitted number or an actual first-moment identity.

For c0 the original solution is1 and C2=0 by PB. The physical ratio R_sp
is0. Its energy is sup(-b/2)=0: every b>0 gives a nonpositive value,
while the unit profiles(8) with ell->0 have b=ell²/3->0. No ell0 profile
is used as a unit vector. With F0(0)=0 both bounds are the zero identity.
This proves Theorem WS:bounds.

## 5. A sharp uniform relative-width bound for the two formulas

Assume c>0 so U/L is defined. Every Gamma argument below is positive
because0<a<1. Duplication at s=(1+a)/2 and recurrence at(1-a)/2 give
 Gamma_E(1+a)=2^a Gamma_E((1+a)/2)Gamma_E(1+a/2)/sqrt(pi),
 (1-a)Gamma_E((1-a)/2)=2Gamma_E((3-a)/2).
Insert these exact identities in M_a and K0(a):

 K0(a)M_a=sqrt(pi)/[2Gamma_E(1+a/2)Gamma_E((3-a)/2)].     (12)

Set x=1+a/2,y=(3-a)/2. Their sum is5/2. In Euler's positive Gamma
integral, take L2(0,infinity) functions
u(t)=t^((x-1)/2)e^(-t/2), v(t)=t^((y-1)/2)e^(-t/2).
Their squared norms are Gamma_E(x),Gamma_E(y), finite for x,y>0;
their inner product is Gamma_E((x+y)/2)=Gamma_E(5/4). Cauchy-Schwarz gives
Gamma_E(5/4)²<=Gamma_E(x)Gamma_E(y). By positivity, inversion in(12)
and then the increasing square root prove(3). At a1/2, x=y=5/4, so the
upper bound is attained. Under a->1-a the two arguments exchange, giving
symmetry of this RATIO OF BOUND FORMULAS, not of C2 or its exponent.
This proves Corollary WS:width.

No a0 or a1 SPDE is substituted into the colored theorem, and no exchange
with the original long-time limit is claimed. The exact expression rho_*
can be evaluated numerically; an approximate decimal is not a certified
decimal enclosure. The c1,a1/2 proposed endpoints approximately1.0795179077
and1.1211952203 follow from(2), not a numerical optimization of C2.

## 6. Proof, computation and formalization boundaries

The exact general-model constant is the reviewed PB variational value.
This example gives its evaluated spatial energy and explicit bounds; it
asserts neither endpoint equals C2. The profile quadratures are independent
consistency evidence, not proofs of full-H1, endpoints or the supremum.
Hard-coded negative-control labels in that JSON are descriptive; actual
negative Lean source/logs reject the wrong coefficient4 and ceiling1/12.

Two finite public proofs have source/types/std3/replay/control evidence.
They do not formalize H1, integrals, CDF, Gamma, attainment or a stochastic
moment. Their source/application fidelity and the complete new analytic
note need this OWN full independent gate before adoption. No theorem is
being fitted to Chen's guesses; no source correction, actualp1, Skorohod
bridge, novelty/human/wholepaper/coldread/public/contact/HPC/companion
clearance follows. After this bounded example, consolidate and verify the
main result instead of opening optional refinements.
