# A global one-dimensional damped lower-endpoint bound

CANDIDATE PROOF, not adopted. Preproof6aa03b9 passed17groups/HIGH,
472.565seconds,15texts+2sourceimages,no requiredrepairs. Fullscientific
analytic/source/type/application review REQUIRED. This targets every
admissible d1 parameter, while originald2/d3,sharpupper,conditionalexact
limit and intendedsource/domain/label interpretation remainOPEN.

## 1. Actual statement and scoped imports

Fix originalreal d1 spatial covariance Gamma_sp=c_Gamma|x|^-alpha dx for
0<alpha<1,orwhite Gamma_sp=c_Gamma delta0 atalpha=1,c_Gamma>0.
Fix0<a<1,alpha+a<2. Put q=4-alpha in[3,4),k=3-alpha,m=q/k,
d=q-2a>0,x=a/2 in(0,1/2). In the scalar argument Gamma(s) denotes
Euler's Gamma function, NEVER the spatial covariance measure.

From the accepted damped-lower-endpoint-bridge.md(1),(4),(9),(11), use
EXACTLYthe same definitions:

 M_a=Gamma((1+a)/2)/[Gamma(1+a)Gamma((1-a)/2)],
 K_star(u)=Gamma(a)^(-1)int_0^infinity
       exp[-(lambda+lambda^2/(2d))|u|]lambda^(a-1)dlambda,
 R_star=2int_0^(1/2)K_star(u)du>0,
 Delta(q,a)=[qlogq+(q-2a)log(q-2a)]/2-(q-a)log(q-a),
 Omega=[M_a^-1/(R_star expDelta(q,a))]^(1/k)>0.

E_star^O is its own explicitly defined damped energy with gradient penalty
1/2 on the strong-H1-measurable,finite-integrated-energy,a.e.normalized
occupation class O. F_a is its algebraic source-shaped map(1).
That accepted theorem gives for the SAME original canonical point solution

 Q2:=liminf_(t->infinity)t^-kappa log E|u(t,0)|^2
    >=2^m Omega F_a(E_star^O),kappa=(4-alpha-a)/k.           (1)

Every value on the right is finitepositive. This is not an actualfirst-
mean premise. The factor2^m is our auxiliary c2 score consumer, not a
printed second-moment theorem in source(1.10). The source's intended
normalization/domain/label dictionary remains separate.

We prove Omega>1 on the ENTIREstated d1 range. More explicitly, the
rational V defined in Section5 satisfies0<V(a/2)<1 and

 Q2>=2^m V(a/2)^(-1/k)F_a(E_star^O)>2^m F_a(E_star^O).      (2)

Only (1) is a stochastic input. All new arguments below are deterministic
scalar estimates and exact rational positivity. Basic positive Gamma/Beta
integrals, recurrence, Beta-Gamma product and Gamma(1/2)=sqrt(pi) were
proved in the accepted bridge Sections2,5; we also explain the new Gamma
identities used here. No numerical Gamma table or reflection formula is used.

## 2. A positive Taylor kernel majorant

For z>=0 define P4(z)=1-z+z^2/2-z^3/6+z^4/24. Taylor's integral remainder
is exp(-z)=P4(z)-(1/24)int_0^z exp(-t)(z-t)^4dt. Thus
P4(z)>=exp(-z)>0. At any d>0, multiply this upper bound at z=u lambda
by exp(-u lambda^2/(2d))lambda^(a-1)/Gamma(a) and integrate over
lambda>0,0<u<1/2. The integral is positive and bounds R_star above.
Each of the five monomial integrals is absolutely finite: Gaussian
substitution gives

 int_0^infinity lambda^(a+j-1)exp(-u lambda^2/(2d))dlambda
   =(1/2)Gamma((a+j)/2)(2d/u)^((a+j)/2),

and its remaining u exponent is (j-a)/2>-1. Finite summation and
integration can therefore be interchanged, despite the alternating signs.
The resulting exact expression for the majorant is

 B4(a,d)=sum_(j=0..4) (-1)^j Gamma((a+j)/2)/Gamma(a)
                *2^a d^((a+j)/2)/[j!(j+2-a)]>0,
 R_star(a,d)<=B4(a,d).                                   (3)

Monotonicity in d comes from its POSITIVEdouble integral, not from its
alternating coefficients: P4(u lambda)>0 and exp(-u lambda^2/(2d))
increases in d. Hence B4(a,d)<=B4(a,4-2a).

For q>=3, direct differentiation gives
partial_q Delta(q,a)=(1/2)log[q(q-2a)/(q-a)^2]<0,
since q(q-2a)=(q-a)^2-a^2>0. Therefore

 R_star expDelta(q,a)<=B4(a,4-2a)expDelta(3,a).             (4)

The envelope q4 is an auxiliary bound on the positive kernel parameter;
we have not introduced an alpha0 noise model. It remains to show the
right side of(4) is smaller than Ceff:=M_a^-1.

## 3. Elementary Gamma estimates with exact constants

Gamma(s)=int_0^infinity t^(s-1)e^-t dt for s>0 is differentiable twice
on every compact positive-parameter interval, by domination with powers
of t times |logt|^j near0 and exponential decay at infinity. In particular
Gamma'(1)=int_0^infinity logt e^-t dt. This justifies all differentiations
below; no Eulerconstant value is imported.

First derive duplication from the positive Beta integral. Symmetry about
1/2, the substitution t=(1+v)/2 and then v^2=u give
Beta(s,s)=2^(1-2s)Beta(1/2,s),s>0. Using the Beta-Gamma product yields

 Gamma(2s)=2^(2s-1)Gamma(s)Gamma(s+1/2)/sqrt(pi).           (5)

We will need only these elementary numerical bounds:

 e<11/4, sqrt(pi)>177/100, log4<7/5.                      (6)

For e, the exponential-series tail from n4 is strictly less than
(1/24)/(1-1/5)=5/96, while the n0..3 sum is8/3. Thus e<87/32<11/4.
For pi use the exact bound pi>157/50 from Mathlib.Analysis.Real.Pi.Bounds,
Real.pi_gt_d2, pinned v4.35.0/Mathlib56a0058, already used and kernel-
checked in the accepted bridge Section5. Since (177/100)^2=31329/10000
<157/50, the square-root claim follows. Finally the positive exponential
series gives exp(7/5)>=sum_(j=0..5)(7/5)^j/j!=189479/46875>4,
so strict monotonicity gives log4<7/5.

Set g(x)=1-3x/5 and L(x)=(177/100)(1-7x/5). Both are positive for
0<x<1/2. We prove three Gamma bounds:

 Gamma(1+x)>=g(x),
 Gamma(1/2+x)/Gamma(1+x)>=L(x),
 Gamma(1/2-x)Gamma(1/2+x)>=pi/(1-4x^2).                   (7)

For the first, we explicitly bound Gamma'(1). Taylor P4 and
int_0^1(-logt)t^jdt=1/(j+1)^2 give

 int_0^1(-logt)e^-t dt<=1-1/4+1/18-1/96+1/600=5737/7200.

For the positive part, integration by parts gives
int_1^infinity logt e^-t dt=E1(1):=int_1^infinity e^-t/t dt.
Here is a purely integral lower bound. Under the unit-mass measure
mu(dy)=e^-y dy on y>=0, int y dmu=1 and int|y-1|dmu=2/e, by splitting
at1 and integrating (y e^-y)'. For X=1+y,

 1/X=1/2-(X-2)/4+(X-2)^2/(4X).

Cauchy-Schwarz gives int (y-1)^2/(1+y)dmu>=(int|y-1|dmu)^2/int(1+y)dmu
=2/e^2. Integrating the reciprocal identity and substituting t=1+y yields

 E1(1)=e^-1 int 1/(1+y)dmu>=1/(2e)+1/(2e^3)
       >274/1331>1/5,                                   (8)

where (6) and monotonicity of the expression in e were used. Thus
Gamma'(1)>1/5-5737/7200=-4297/7200>-3/5. The tangent inequality
t^x=exp(xlogt)>=1+xlogt, integrated against e^-t dt, proves
Gamma(1+x)>=1+xGamma'(1)>=g(x).

For the ratio put T(x)=Gamma(1/2+x)/Gamma(1+x). The Beta product gives
T(x)=pi^(-1/2)int_0^1 t^(x-1/2)(1-t)^(-1/2)dt.
It is convex in x on x>-1/2, either by the exponential tangent or by
its nonnegative second derivative under the integral. Differentiation
near0 is justified by t^(-3/4)|logt|^j domination near0, j<=2.
T(0)=sqrt(pi). Differentiating the logarithm of (5), in the form
Gamma(1+2x)=2^(2x)Gamma(1/2+x)Gamma(1+x)/sqrt(pi),at0 gives
T'(0)=-2sqrt(pi)log2; the terms Gamma'(1) cancel. Hence

 T(x)>=sqrt(pi)(1-xlog4)>=L(x),

using (6) and positivity of 1-7x/5. This is convexity of T itself,
not an unsupported convexity assertion about a ratio of arbitrary functions.

For the product, Cauchy-Schwarz in the positive Gamma integrals gives
Gamma(3/2-x)Gamma(3/2+x)>=Gamma(3/2)^2=pi/4.
Recurrence and 1/4-x^2>0 give the last inequality in(7).

Two more estimates are elementary:

 sqrt(1-x)>=g(x), (1-x)^x<=P(x):=1-x^2+x^4/2.             (9)

The first follows by squaring, since
1-x-g(x)^2=x(5-9x)/25>=0 and g>0. For the second use
log(1-x)<=-x and exp(-x^2)<=1-x^2+x^4/2, the latter being the signed
second-order Taylor upper bound. All bases and factors in(7)-(9) are positive.

## 4. Exact Gamma identity and an actual rational envelope

For x=a/2 define

 E(x)=1/[2(1-x)]+x(1-x)/(2-x)+x(x+1)(1-x)^2/[3(3-x)],
 C(x)=1/(3-2x)+(2x+1)(1-x)/[3(5-2x)].

Both are positive. Grouping the even j0,2,4 and odd j1,3 terms of(3),
using Gamma recurrence and d0=4-2a=4(1-x), gives

 B4(a,d0)=2^a d0^x/Gamma(2x)
   *[Gamma(x)E(x)-2sqrt(1-x)C(x)Gamma(1/2+x)].

Apply duplication(5) both at x and x+1/2, and use Gamma(1+x)=xGamma(x).
Since Ceff=Gamma(1+2x)Gamma(1/2-x)/Gamma(1/2+x), this is the EXACT identity

 B4(a,d0)/Ceff
 =2pi(1-x)^x/[Gamma(1/2-x)Gamma(1/2+x)Gamma(1+x)]
    *[E(x)-2sqrt(1-x)C(x)x T(x)].                         (10)

No reflection formula or numerical Gamma estimate occurs. B4>0 by its
positive integral and the prefactor is positive, so the ORIGINALbracket
in(10) is positive. Replacing sqrt(1-x) by g and T(x) by L only increases
that bracket. Consequently

 H(x):=E(x)-2g(x)C(x)xL(x)>0.

We can now bound positive prefactors using(7)-(9), obtaining

 0<B4(a,d0)/Ceff<=2P(x)(1-4x^2)H(x)/g(x).                (11)

Positivity was proved BEFORE multiplication of upper bounds.

For completeness bound the remaining map factor. For f(u)=u logu,
f''(u)=1/u. The symmetric second-order Taylor integral between3-4x
and3 gives

 0<Delta(3,2x)<=2x^2/(3-4x)=:z<1.

Indeed the midpoint radius is2x and the second derivative is at most
1/(3-4x). Also 3-4x-2x^2>=1/2 on [0,1/2]; for example x^2<=x/2
makes it at least3-5x>=1/2. Since exp(-y)>=1-y for 0<=y<1,

 expDelta(3,2x)<=(3-4x)/(3-4x-2x^2).                     (12)

Define the ACTUALrational function

 V(x)=2P(x)(1-4x^2)/g(x)*H(x)*(3-4x)/(3-4x-2x^2).         (13)

All its factors are positive on0<x<1/2. Equations(11)-(12) therefore prove

 0<B4(a,4-2a)expDelta(3,a)/Ceff<=V(a/2).                  (14)

It remains a finite rational task, with no Gamma content hidden in V.

## 5. Exact positivity certificates on two rational intervals

Let

 D(x)=750(3-x)(2-x)(1-x)(5-2x)(3-2x)(5-3x)(3-4x-2x^2),
 Q(x)=-237888x^15+2567920x^14-10605344x^13+17964536x^12
 +3700636x^11-59045877x^10+66291248x^9+36266494x^8
 -125535292x^7+58424029x^6+68792033x^5-94022217x^4
 +42981706x^3-8102234x^2+516600x+9900.

Clearing the explicit nonzero denominators in(13) and expanding gives

 D(x)(1-V(x))=xQ(x).                                     (15)

D(x)>0 on[0,1/2],factor by factor, including the last factor just bounded
below by1/2. To prove Q positive without a root approximation, the following
EXACTinteger certificates hold for every real t:

 4^15 Q(t/4)-1=sum_(i=0..15) A_i t^i(1-t)^(15-i),
 4^15 Q((1+t)/4)-1=sum_(i=0..15) B_i t^i(1-t)^(15-i).      (16)

All coefficients are given explicitly here:

| i | A_i | B_i |
|---:|---:|---:|
| 0 | 10630044057599 | 12356981993087 |
| 1 | 298124417433585 | 224060765099313 |
| 2 | 2513855498420119 | 1894937289568407 |
| 3 | 11108582904823353 | 9799655243171641 |
| 4 | 30835186027461291 | 34453566936433323 |
| 5 | 58554861260633157 | 87031904519822405 |
| 6 | 79751967489125491 | 163125524987087987 |
| 7 | 80316614660581085 | 231150225523443421 |
| 8 | 61414936532707037 | 249909141873911517 |
| 9 | 36921141989698675 | 206372784329731187 |
| 10 | 18353430194004037 | 129237504527758405 |
| 11 | 7893814205477547 | 60326501022497451 |
| 12 | 2890010244293689 | 20332988225551929 |
| 13 | 811168303884183 | 4674097187389335 |
| 14 | 146648694693297 | 655486353407985 |
| 15 | 12356981993087 | 42278584319999 |

Each identity is checked by expansion; all listed coefficients are strictly
positive integers. For0<=t<=1 every monomial is nonnegative, so each left
side in(16) is nonnegative. The substitutions cover respectively[0,1/4]
and[1/4,1/2], yielding Q(x)>=4^-15>0 on the whole closed interval.
Combining with(15), x>0 and D>0 proves

 V(x)<1 for0<x<=1/2.                                    (17)

The actual Gamma application has x<1/2 and already has V>0 from Section4.
The purely rational statement can include x1/2; it asserts no Gamma or
noise model at a1.

There is an independent kernel check of the ENTIRErational core:
StratonovichHAMAudit.GlobalOmega defines exactly Q,D,V above. Its public
left_certificate/right_certificate prove(16)'s scaled inequalities,
polynomial_pos proves Q>0, and rational_lt_one proves(17) with the actual
rational definition and all denominator conditions. Complete definitions,
public types, source and compile/replay receipts are retained in
lean-progress/local-checks/global-omega-v1/. This is finite arithmetic
verification, not an axiom of desired positivity or a Gamma/SPDE theorem.
The explicit table also makes the mathematical certificate self-contained.

## 6. The original point lower bound on the full d1 range

Equations(4),(14),(17) give the strict GLOBALcomparison

 0<R_star expDelta(q,a)/M_a^-1<=V(a/2)<1.

By the accepted definition of Omega and k>0,
Omega>=(1/V(a/2))^(1/k)>1. Substituting into the actual point consumer(1)
proves(2) for every admissible d1 temporal exponent and spatial covariance,
with its actual amplitude retained in E_star^O. In particular

 liminf_(t->infinity)t^-((4-alpha-a)/(3-alpha)) log E|u(t,0)|^2
 >=2^((4-alpha)/(3-alpha)) V(a/2)^(-1/(3-alpha)) F_a(E_star^O)
 >2^((4-alpha)/(3-alpha)) F_a(E_star^O).                   (18)

No numerical value of a spatial energy, no optimizer, minimax exchange,
rough-flow construction or moving parameter/test was used. Each noise
parameter and each approximating test is fixed before its own time limit,
as in the accepted bridge. The gain depends on parameters; V(0)=1 as a
rational endpoint identity, so no uniform gain at a0 is claimed and no
excluded endpoint noise model or parameter/time-limit interchange is inferred.

E_star^O remains the EXPLICITown energy over O with the actual source
(1.13) damped kernel and (1.12) half gradient. Interpreting it as a particular
source lower input requires BOTH the domain dictionary and the first-to-
second-label convention, as already recorded in the bridge adjudication.
Source(1.10) is a first-mean map only. We do not use its first-mean theorem,
repair its printed normalization, identify actual mean growth or claim an
improvement over actual Jensen. The source interpretation remains conditional;
the actual canonical point inequality(18) with our defined energy is direct.

This closes the d1 lower comparison for all its stated parameters, not the
original whole goal. The sharp upper constant, original d2/d3 lower
construction, intended source normalization/domain/label map, variational
gap and conditional exact limit remain open. Retained full G:upper is
unchanged. No Skorohod development, source-author contact, public release,
novelty, whole-paper cold-read or circulation clearance is claimed.

The eight scalar samples are only controls; (3)-(17) are the proof. The
weaker envelope omitting P failed four exact tests and its refusal is
retained. A single whole-interval Bernstein attempt had one negative
coefficient and was refused as a certificate, not a false-polynomial claim.
Subdivision then supplied(16), with every coefficient checked independently
by Lean. The initial local Lean denominator-normalization failure is also
retained; only canonical nonzero facts were added, with public definitions
and theorem statements unchanged. Four local lemmas have complete public
objects/types, standard axioms, five fresh replay hash matches and two
False controls. Analytic Gamma/kernel/energy/SPDE assembly is NOTformalized
by those lemmas. No companion/package/lease/registry/HPC transaction.

Full scientific proof/source/type/application review is REQUIRED before
adoption. Canonical TeX/PDF is unchanged; this is an internal candidate,
not full G:sharp or whole-paper completion. Original full goal remainsACTIVE.
