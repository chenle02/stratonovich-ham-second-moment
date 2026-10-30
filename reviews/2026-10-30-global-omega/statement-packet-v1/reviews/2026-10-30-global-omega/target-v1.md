# Global d1 damped lower comparison: proposed theorem and actual envelope

PROPOSED,unproved/unreviewed. Aim at ALLoriginald1a/alpha parameters,
not another isolatedpoint. Originald2/d3/sharpUPPER/conditionalexactlimit/
source-normalization/wholepaper goal remainsOPEN. No sourcefix/p1premise.

## Objects and claimed consequence

Originalreal d1Gamma Riesz c_Gamma|x|^-alpha dx for0<alpha<1 orwhite
c_Gamma delta0 atalpha1,c_Gamma>0;0<a<1,alpha+a<2,q=4-alpha in[3,4),
k=3-alpha,m=q/k,d=q-2a>0. Use EXACT M_a,R_star,K_star,Delta(q,a),
F_a,E_star^O,actualcanonicalQ2 andOmega of accepted damped-lower-endpoint-
bridge.md Sections1-6, with all explicitO-domain/source/label qualifications.
In particular Q2>=2^mOmega F_a(E_star^O),
Omega=[M_a^-1/(R_star expDelta(q,a))]^(1/k)>0.

Prove GLOBAL Omega>1 forALLthoseparameters, giving the actualpointlower
 Q2>=2^mOmega F_a(E_star^O)>2^m F_a(E_star^O).              (END)
This uses OWN explicit dampedenergy on meaningfulstrongH1measfiniteenergy
O; no allprintedAd/intendedsourceL/first-to-second-label identity adopted.

## T1: original kernel reduced to one Gamma inequality

P4(z)=1-z+z²/2-z³/6+z⁴/24>=exp(-z)>0,z>=0,by signedTaylorremainder.
Inside ACTUALK_star, integrate each term after GaussianLaplacesubstitution
and overu in(0,1/2) to derive
 R_star(a,d)<=B4(a,d),
 B4(a,d)=sum_(j=0..4) (-1)^j Gamma((a+j)/2)/Gamma(a)
                   *2^a*d^((a+j)/2)/[j!(j+2-a)].
Check absoluteintegrability of EACHterm before finitealternatingsum.
Because P4positive, its integral bound is increasingind; hence d<=4-2a.
Delta(q,a) is decreasinginq onq>=3 by derivative
(1/2)log[q(q-2a)/(q-a)²]<0. Thus suffice to prove
 B4(a,4-2a)expDelta(3,a)<M_a^-1,0<a<1.                  (G4)
The envelopeq4 doesNOTassert an alpha0SPDEmodel.

## T2: exact Gamma identity and elementary bounds

Put x=a/2 in(0,1/2),g(x)=1-3x/5,L(x)=(177/100)(1-7x/5),
 P(x)=1-x²+x⁴/2,
 E(x)=1/[2(1-x)]+x(1-x)/(2-x)+x(x+1)(1-x)²/[3(3-x)],
 C(x)=1/(3-2x)+(2x+1)(1-x)/[3(5-2x)].
With Ceff=M_a^-1, derive the EXACTidentity using Gamma recurrence/duplication:
 B4(a,4-2a)/Ceff
 =2pi(1-x)^x/[Gamma(1/2+x)Gamma(1/2-x)Gamma(1+x)]
       *[E(x)-2sqrt(1-x)C(x)x Gamma(1/2+x)/Gamma(1+x)].   (ID)
Derive duplication from the positive Beta integral if not importing it;
no Gamma reflection theorem needed. Gamma derivatives justified by domination.
Prove for0<x<1/2
 Gamma(1+x)>=g(x)>0,
 Gamma(1/2+x)/Gamma(1+x)>=L(x)>0,
 Gamma(1/2-x)Gamma(1/2+x)>=pi/(1-4x²),
 sqrt(1-x)>=g(x), (1-x)^x<=P(x),
 expDelta(3,2x)<=[3-4x]/[3-4x-2x²].                    (AUX)
Allsigns and denominator domains explicit; no numericGamma bound assumed.

Specific self-contained route for the first Gamma bound: exp tangent gives
Gamma(1+x)>=1+xint_0^infty logt e^-t dt. Bound negativepiece
int_0^1(-logt)e^-t dt<=5737/7200 byTaylorP4. Positivepiece equals E1(1)
=int_1^infty e^-t/t dt. UnderY~Exp1, reciprocalidentity andCS give
E1(1)>=1/(2e)+1/(2e³)>1/5 using e<11/4, so thelogmoment>-3/5.
No Eulerconstant numerical input. The exact e bound follows exponential
series tail. RatioGamma bound: positiveBeta integral makes
T(x)=Gamma(1/2+x)/Gamma(1+x) convex; duplication differentiatedat0 gives
T'(0)=-2sqrtpi log2, so T(x)>=sqrtpi(1-2xlog2)>=L(x).
Use sqrtpi>177/100 and log4<7/5 with elementary/verifiedfinite bounds.
Gamma product bound follows CS at1.5: Gamma(1.5-x)Gamma(1.5+x)>=pi/4,
then recurrence. LastDelta estimate uses secondderivative1/u foru logu,
Delta(3,2x)<=2x²/(3-4x)<1 and expy<=1/(1-y). No specialfunctiontable.

## T3: actual rational envelope and finite certificates

From ID/AUX and bracketpositivity (P4integralpositive; replacements only
increase thebracket), prove the ACTUALbound
 0<B4(a,4-2a)expDelta(3,a)/Ceff<=V(x),
 V(x)=2P(x)(1-4x²)/g(x)*[E(x)-2g(x)C(x)xL(x)]
                       *(3-4x)/(3-4x-2x²).             (V)
Allfactors positive before multiplying inequalities. Prove V(x)<1 on
0<x<1/2 by exactrationalidentity D(x)(1-V(x))=xQ(x), where
 D=750(3-x)(2-x)(1-x)(5-2x)(3-2x)(5-3x)(3-4x-2x²)>0,
 Q= -237888x^15+2567920x^14-10605344x^13+17964536x^12
 +3700636x^11-59045877x^10+66291248x^9+36266494x^8
 -125535292x^7+58424029x^6+68792033x^5-94022217x^4
 +42981706x^3-8102234x²+516600x+9900.

certificates-v1.json specifies TWO16-term POSITIVE rational certificates:
4^15 Q(t/4)-1=sum_i A_i t^i(1-t)^(15-i),
4^15 Q((1+t)/4)-1=sum_i B_i t^i(1-t)^(15-i),0<=t<=1.
All A_i,B_i are EXACTpositiveintegers in thatJSON; the whole-interval
Bernstein attempthad a negativecoefficient, explicitlyrefused (not a
polynomialcounterexample). Twointervals cover[0,1/2], so Q>0.
Independentproof/type/application check mustbind the ACTUALQ/V/D and
allcoefficients, not opaque assumedpositivity. Lean certifies onlyfinite
rationalcore, notGamma/Betakernel/SPDE conclusions. ExactCAS identities
and8scalarcontrols are not by themselves an analyticproof.

## T4: original point consequence and open goals

CombineT1-T3 to G4, henceOmega>1. SinceV(x)>0 also obtain theexplicitgain
 Omega>=(1/V(a/2))^(1/k)>1,
 Q2>=2^m V(a/2)^(-1/k)F_a(E_star^O)>2^m F_a(E_star^O).  (GAIN)
No uniformgain as a->0 is claimed, no parameter/time-limit interchange.
Originaldata/covariance/Gaussianhalf-cost/kinetic1/2/source(1.13) unchanged.
No actualfirstmean/Jensen/sourceupper/normalizationfix/completeGsharp,
optimizer/minimax/movingtest/Skorohod/companion/HPC/contact/novelty/circulation.
Retainalloriginaldimensions/sharpupper/exactlimit/source/domain/labelgates.
Independentstatement audit BEFORElongproof, fullscientific/type/sourcegate
afterwrittenproof. Failure ofaWEAKenvelope withoutP(x) retained, not hidden.
