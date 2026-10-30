# A ceiling for the positive Gaussian-control variational value

ACCEPTED at the scoped scientific analytic/source/type/application gate:
actualOpus5.5/HIGH,8PASSgroups,322.118seconds,26texts+4sourceimages,
no requiredrepairs; scientificsourcead6c188. Exact evidence and seven
optional clarifications in reviews/2026-10-30-raw-value-ceiling/
scientific-adjudication-v1.md. This bounds the positive-control LOWER-
MECHANISM VALUE V_c, not the point moment Q2. Original sharp/source/
dimensional goal and intended normalization remain open.

## 1. Fixed actual objects, scoped imports and new energy

Fix actual real d1 covariance Gamma with its positive amplitude: Riesz
c_Gamma|x|^-alpha dx for0<alpha<1, or white c_Gamma delta_0 atalpha=1.
Fix0<a<1,alpha+a<2. Write q=4-alpha,k=3-alpha,m=q/k. Thus3<=q<4,
2<=k<3,alpha<2. Symbols q,k here are scalars, not the imported spatial
profile q_sigma or far kernel. K(s,t)=|s-t|^-a on(0,1)^2.

Imported accepted inputs, not re-proved:
- occupation-control-approximation.md Sections1-6: B=L1 intersect L2 with
  sum norm,X=L2(time;B),actual covariance bilinear B_Gamma,raw v_psi,
  potential h_psi,sigma and whole-H1 variational rate lambda_psi,I_psi.
  Positive smooth C_pos tests approximate EACH X_pos test in X with
  continuous covariance cost. The positive finite REAL values V_c^pos
  over X_pos equal the smooth-test score suprema (SUP).
- The same note (OCC): real stronglyH1-measurable g with ||g(t)||2=1
  a.e. and finite integrated derivative energy has rho_g=g^2 in X_pos.
  For such normalized f, int f^4<=2||f'||2. The time Schur constant is
  K0=2^a/(1-a). All kernels, amplitudes and costs are the actual ones.
- nonseparable-profile-family.md(4),(7)-(8) and its adjudication: for
  each FIXED smooth psi in C_pos, actual normalized real positive
  ground p_sigma is continuous in H2 with a uniform H2 bound; its
  rate lambda_sigma>0 and H_sigma p_sigma=-lambda_sigma^2 p_sigma,
  H_sigma=-d2-h_sigma. Rates and H2 norms are bounded on[0,1].
- joint-gaussian-tilt.md Section1: the SAME raw-law Gaussian W has
  covariance |s-t|^-a Gamma for all real smooth compact tests and
  Z=W(psi),v=E Z^2. In particular for two such tests f,g,
  E[W(f)W(g)]=B_Gamma(f,g), by that covariance bilinear form (or its
  polarization). The profile is tilt(5) and raw variance is consumer(25).
- General-positive consumer(24),(31)-(32): for the SAME original point
  solution Q2=liminf t^-kappa log E|u(t,0)|^2, kappa=(4-alpha-a)/k,
  Q2>=V_2^pos. Other labels c>0 are auxiliary. This is a LOWER bound.

Let O denote exactly the occupation class in the second bullet. Define

 T_occ(g)=int_0^1||g'(t)||2^2dt,
 A_occ(g)=B_Gamma(rho_g,rho_g)=v_(rho_g),
 E_eta=sup_(g in O)[A_occ(g)-eta T_occ(g)],eta>0.           (1)

Eta is a kinetic coefficient, not the spectral decay margin in older
notes. E_eta retains the ACTUAL a and Gamma. It is a new raw energy over
an explicit meaningful domain, not an adopted source E,E_star or static M.
Finiteness/positivity and real supremum in (1) are established next.

## 2. Finite positive occupation energy and its exact interpolation ratio

For every normalized nonzero f in H1, ||f'||2>0. Indeed a zero weak
derivative makes its distribution constant: every compact smooth test
of zero integral is the derivative of a compact smooth primitive, so
pairing with f depends only on the test integral. L2 forces that constant
to be0, contradicting normalization. Consequently0<T_occ(g)<infinity
for g in O. Also rho_g in X_pos and accepted raw-cost positivity imply
0<A_occ(g)<infinity. O is nonempty by any constant-in-time normalized
nonzero real compact smooth f.

We need a HOMOGENEOUS bound, not the old fixed-radius split. Write
b(t)=||g'(t)||2^2>0 a.e. In the Riesz case set r_t=g(t)^2, of mass1,
with L_t=||r_t||infinity<=2sqrt(b(t)), by the accepted d1 Sobolev bound.
For ANYradius R>0, direct integration near0 and unit mass away give

 (Gamma*r_t)(x)
 <=c_Gamma[2L_t R^(1-alpha)/(1-alpha)+R^-alpha].

Choose R=1/L_t (positivefinite). This proves
||Gamma*r_t||infinity<=c_Gamma[2/(1-alpha)+1]2^alpha b(t)^(alpha/2).
Denote that finite constant by C_Gamma. Spatial symmetry and mass1 then
give, for almost all s,t,

 int r_s(Gamma*r_t)
 <=C_Gamma min(b(s)^(alpha/2),b(t)^(alpha/2))
 <=C_Gamma b(s)^(alpha/4)b(t)^(alpha/4).                   (2)

All integrals are nonnegative and Tonelli applies. For white alpha=1,
spatial Cauchy-Schwarz and int g(t)^4<=2sqrt(b(t)) give (2) with
C_Gamma=2c_Gamma and exponent alpha/4=1/4. Thus that endpoint uses its
actual Dirac covariance, never a |x|^-1 density.

Apply the symmetric time Schur estimate to F(t)=b(t)^(alpha/4): its
L2 norm is finite since alpha/2<1 and b is integrable. Concavity on the
unit time interval gives int b^(alpha/2)<=T_occ(g)^(alpha/2). Therefore

 A_occ(g)<=K0 C_Gamma T_occ(g)^(alpha/2).                  (3)

In particular A_occ-eta T_occ is bounded above: the function
C x^(alpha/2)-eta x on x>=0 is bounded above, since alpha/2<1.
We will prove positivity by dilation. Its real score set is nonempty.

For ell>0 define OCCUPATION dilation
(S_ell g)(t,x)=sqrt(ell)g(t,ell x). It is an H1 isomorphism, L2 unitary,
with inverse S_(1/ell), preserving strong time measurability and O.
Its density is ell rho_g(t,ell x). Gamma's actual Radon pushforward under
y->ell y is ell^(alpha-1)Gamma, so convolution of that density is
ell^alpha(Gamma*rho_g(t))(ell x). This holds also for white, where
alpha=1 and the pushforward factor is1. A usual dx change then yields

 A_occ(S_ell g)=ell^alpha A_occ(g),
 T_occ(S_ell g)=ell^2 T_occ(g).                            (4)

This is distinct from D_ell psi=ell^(3-alpha)psi(t,ell x), which dilates
Gaussian tests. No F-phase isometry or across-test noise bound is used.
Since alpha<2 and A_occ(g)>0, a sufficiently small fixed ell makes
ell^alpha A_occ(g)-eta ell^2 T_occ(g)>0. Thus0<E_eta<infinity and the
REAL supremum in (1) is legitimate.

Define the positive finite REAL ratio supremum

 C_occ=sup_(g in O) A_occ(g)/T_occ(g)^(alpha/2).             (5)

Nonemptiness, positivity and boundedness above follow from (3) and T>0.
For fixed A=A_occ(g)>0,T=T_occ(g)>0, the scalar function
A ell^alpha-eta T ell^2 has unique global maximum at
ell_*=(alpha A/(2eta T))^(1/(2-alpha)). This follows by factoring its
derivative as ell^(alpha-1)[alpha A-2eta T ell^(2-alpha)]; the bracket
changes from positive to negative once. Endpoint limits are0 and minus
infinity. Its maximum is

 D_eta [A/T^(alpha/2)]^(2/(2-alpha)),
 D_eta=(2-alpha)/2*(alpha/(2eta))^(alpha/(2-alpha)).         (6)

The union of all S_ell g is exactly O: each image belongs to O, and
ell=1 includes every g. Hence E_eta equals the supremum over g of
(6). Every ratio is <=C_occ, proving E_eta<=D_eta C_occ^(2/(2-alpha)).
Conversely, approximate C_occ from below by its ratios and use continuity
of the positive power; this proves the reverse inequality without an
optimizer. Solving that equality and comparing its eta dependence gives

 C_occ=(2E_eta/(2-alpha))^((2-alpha)/2)*(2eta/alpha)^(alpha/2),
 E_eta=eta^(-alpha/(2-alpha))E_1.                          (7)

No minimax interchange has occurred, only the explicitly identified union
of spatial dilates and both real-supremum inequalities.

## 3. Actual smooth ground curve and covariance/time inequalities

Fix psi in C_pos, before all time limits. Its ACTUAL positive normalized
p_sigma from the accepted family is continuous in H2, so strongly
H1-measurable with bounded derivative norm. Thus g(sigma)=p_sigma belongs
to O. Put T=T_occ(g)>0,A=A_occ(g)>0,rho=p^2 in X_pos.
The actual H2 eigen-equation and integration by parts give

 lambda_sigma^2+||p_sigma'||2^2=int h_psi,sigma p_sigma^2.

The integration by parts is valid on H2, by compact-smooth approximation
and L2 convergence of both derivatives; h is bounded for this fixed smooth
family. Uniform H2 and rate bounds make every integrated term finite.
Tonelli, evenness of Gamma and symmetry of K identify the right integral:

 int_0^1 lambda_sigma^2 dsigma+T=B_Gamma(psi,rho).          (8)

Here lambda is exactly the accepted whole-form rate on smooth tests.
There is no rough ground-state claim.

For clarity prove covariance Cauchy-Schwarz at the ACTUAL X pairings.
For f,h in X_pos choose their positive smooth X approximants supplied
by the accepted occupation approximation. At each fixed n, W(f_n) and
W(h_n) are on the SAME raw Gaussian space. Ordinary random-variable CS
and the imported raw covariance law give
B_Gamma(f_n,h_n)^2<=v_(f_n)v_(h_n). Bilinear continuity in X and cost
convergence pass to

 |B_Gamma(f,h)|<=sqrt(v_f v_h).                            (9)

This is not deduced from pointwise kernel positivity or an independent
noise. No construction of W(f) at rough input was needed. Apply (9)
to psi,rho. Time CS on a unit interval is only an UPPER inequality,
I_psi^2<=(int lambda_sigma^2). Combining (8),(9) and (5) therefore gives

 I_psi^2+T<=sqrt(v_psi A)
              <=sqrt(v_psi C_occ)T^(alpha/4).              (10)

The factor T^(alpha/4) comes from the square root of A, not T^(alpha/2).
No equality replacing the time integral of square roots has been assumed.

## 4. Eliminate the scalar energy and raw cost with exact coefficients

Write beta=alpha/4 in(0,1),v=v_psi>0 and H=sqrt(v C_occ)>0.
The function H T^beta-T has derivative beta H T^(beta-1)-1, strictly
decreasing from positive infinity to -1. Its unique global maximum
is at T_*=(beta H)^(1/(1-beta)). Substituting gives

 I_psi^2<=q/4*(alpha/4)^(alpha/q)*(v C_occ)^(2/q),
 I_psi<=D v^(1/q),
 D=sqrt(q/4)*(alpha/4)^(alpha/(2q))*C_occ^(1/q)>0.          (11)

The first inequality uses (10) then this global maximum, not a choice of
the actual T. Positive square roots give the second.
For auxiliary c>0, the score cI_psi-v/2 is <=cD v^(1/q)-v/2.
Since q>1, the latter derivative cD/q*v^(1/q-1)-1/2 decreases from
positive infinity to -1/2. Its global maximum occurs at
v_*=(2cD/q)^(q/k), with value k v_*/2. Thus EVERY smooth score obeys

 cI_psi-v_psi/2<=k/2*(2cD/q)^(q/k).                       (12)

This is the RAW HALF-variance cost; replacing v/2 by v changes the bound.
All real powers below have positive bases. Squaring D and multiplying
powers yields the useful coefficient identity

 (2D/q)^q=q^(-q/2)*(alpha/4)^(alpha/2)*C_occ.               (13)

Substitute (7) into (13). The two alpha factors multiply as
(alpha/4)^(alpha/2)*(2eta/alpha)^(alpha/2)=(eta/2)^(alpha/2).
Converting the outside1/2 in (12) to2^(-k) inside the1/k power uses
k=3-alpha, and gives2^(-k)(eta/2)^(alpha/2)=(2eta)^(alpha/2)/8.
Consequently the right side of (12) equals

 U_c(eta)=c^m(2eta)^(alpha/(2k)) F_0(E_eta),
 F_b(z)=k[ (q-2b)^((q-2b)/2)/(8(q-b)^(q-b))
                          *(2z/(2-alpha))^((2-alpha)/2)]^(1/k),
 z>0,0<=b<q/2.                                          (14)

Taking the REAL supremum of smooth scores, then the accepted exact
smooth/X value identity (SUP), proves the actual VALUE ceiling

 V_c^pos<=U_c(eta) for every c>0,eta>0.                    (15)

The bound is independent of psi because T and v were eliminated and
C_occ is universal for the fixed model. No rough eigenfunction, flow,
optimizer or uniform across-test event was used. By (7), substituting
E_eta into (14) cancels eta^(alpha/(2k)) against the energy power, so
U_c(eta) is independent of eta. All E_eta STILLuse the actual a.
F_0 means the algebraic DISPLAYparameter b is0, not a static covariance
replacement, a new noise law or an a->0 limit.

## 5. Strict map gap and an exact admissible parameter certificate

For any z>0 and actual0<a<1, all bases in F_a are positive because
q>=3 and q-2a>1. Define

 Delta_map(q,a)=[q log q+(q-2a)log(q-2a)]/2-(q-a)log(q-a).

It is positive. Indeed f(x)=x log x has strictly increasing derivative
log x+1 on x>0. With midpoint x=q-a and radius a>0,
f(x+a)+f(x-a)-2f(x)=int_0^a[f'(x+t)-f'(x-t)]dt>0.
This is twice Delta_map. It is also exactly the local scalar lemma
strict_log_gap with arguments q,a, ha=a>0,hpos=q-2a>0.
The analytic domain conditions have just been verified, not assumed
from the printed-source notation.

Taking logs in (14), all z factors and positive k factors cancel:

 F_a(z)/F_0(z)=exp(Delta_map(q,a)/k)>1.                    (16)

At kinetic eta=1/2, (15)-(16) therefore imply

 V_c^pos<=c^m F_0(E_(1/2))<c^m F_a(E_(1/2)).              (17)

At general eta, the EXACT ratio of c^m F_a(E_eta) to U_c(eta) is
exp([Delta_map-(alpha/2)log(2eta)]/k). Hence strict separation from
the ceiling is equivalent to

 Delta_map(q,a)>(alpha/2)log(2eta).                        (18)

It holds automatically for eta<=1/2. No actual source input has been
identified with E_(1/2).

There is also a concrete eta1 example, with no numerical energy value:
alpha=1/10,a=9/10 satisfies alpha+a=1<2,0<a<1 and0<alpha<1.
Then q=39/10,q-2a=21/10,q-a=3, and exact logarithmic algebra gives

 20Delta_map=39log(39/10)+21log(21/10)-60log3
             =log[(39^39*21^21)/30^60].

The positive integers satisfy
39^39*21^21>2*30^60. This is the exact local Lean theorem exact_gap;
its full integer values/difference are also recorded by the diagnostic
script. Strict monotonicity of log on positive arguments therefore
proves20Delta_map>log2, or (18) at eta=1. Combining with (15) proves

 V_c^pos<=U_c(1)<c^m F_a(E_1)
       at alpha=1/10,a=9/10,for all amplitudes and c>0.    (19)

The integer certificate proves that scalar sign, not any energy or
stochastic claim by itself. The chain (1)-(15) is the analytic consumer.

## 6. Exact source dictionary and consequence for the named mechanism

The algebraic map F_a(z) in (14) agrees EXACTLYwith the map printed in
X.Chen authorversion p3(1.10), upon alpha0=a and substituting its input
by z. Pinpoint/image hashes are in the current review source custody;
sourcePDF SHA remains5f7385ca...97b6c. This is a map identity only.

The inputs E_eta here are explicitly defined by (1) over O with the
actual RAWkernel. Authorp4(1.11) prints rawkernel and gradient penalty1;
(1.12) prints the DAMPEDkernel and gradient penalty1/2. Thus E_(1/2)
is not silently the printed E or E_star. Even identifying E1 with a
printed energy requires a precise meaningful-domain dictionary: O uses
strong H1 time measurability, finite integrated energy and a.e. mass
normalization; printed Ad gives every-sliceH1/mass but omits those time/
finite-energy details. No equality to all possible readings is adopted.
The independently audited source-internal discrepancy remains retained;
intended normalization UNKNOWN and no correction proposed or selected.

The accepted actual-point mechanism supplies Q2>=V_2^pos. Equations
(17) and (19) bound V_2 FROM ABOVE. Since each fixed positive-control
score is <=V_2, optimizing those scores cannot itself deliver a lower
rate as large as the larger displayed quantity in (17) or (19).
Only c=2 has that point-second-moment consumer; other c are auxiliary.
This is a limitation of the defined positive Gaussian-control raw-score
mechanism. Q2 could be strictly larger than its lower functional, so
nothing here bounds Q2 from above or refutes an actual moment formula.

No comparison of a source LOWERconstant F_a(E_star) with U_2 is proved;
its damped kernel matters. The original two-sided sharp target may need
less than the displayed upper endpoint. The source's intended exact-limit
conjecture, sharp upper constant, original higher-dimensional lower
construction and alternate (including signed/complex-clock) mechanisms
remain open. The ceiling neither disproves nor reopens the retained
full G:upper theorem or its Theorem3.1 route. No actualfirstmean/sourceL
identity, Jensen improvement, signed-control/optimizer/attainment/minimax
result is asserted. It is a named-route limitation, not a moment no-go.

## 7. Calibrations, verification and remaining goal

As the DISPLAYparameter a tends to0 at fixed q,z, Delta_map tends to0
by continuity and F_a(z)/F_0(z) tends to1. This is scalar calibration
only; E_eta(a) and the actual moment were not passed through a limit.
The factor c^m in (14) agrees with the accepted auxiliary homogeneity;
it is not a new arbitrary-moment theorem or an actual firstmean result.
Jensen for the original mean remains available separately. No disputed
static white M, published numerical corollary or Skorohod asymptotic was
used or developed; covariance amplitude and all kinetic costs remain.

Six80-digit scalar controls evaluate the stationary points and sampled
neighbors and detect wrong fullcost/omittedkinetic-factor formulas.
They are not a global numerical search or an occupation-energy/SPDE
evaluator. Global optimizations were proved in Sections2/4. The exact
integer/log-gap local Lean seams have complete publictypes/standardaxioms,
5matchingfreshreplay outputs and2Falsecontrols. Their actual applications
are Section5 only, with domain/log conversion proved analytically there.
Initial local projection-argument compilation failure is retained, not
called a passing run. No formalenergy/covariance/spectral/ceiling/SPDE
claim or companion/package/lease/registry/HPC transaction follows.

Full independent scientific proof/source/type/application review is
REQUIRED before adoption. CanonicalTeX/PDF unchanged. Original fullgoal
ACTIVE; no sourcefix/contact/Skorohod/publicrelease/novelty/whole-paper/
coldread/circulation clearance. A value ceiling is progress on the raw
comparison, not completion of the requested sharp/source/dimensional goal.
