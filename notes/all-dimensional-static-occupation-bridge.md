# Static controls and full occupation energy in every original dimension

ACCEPTED at the scoped FULL analytic/source/type/application gate:
Opus5.5/HIGH,18checks PASS/PASS_WITH_NOTES,366.614seconds, no required
repairs, scientific source249e2c4. Nine optional clarifications are recorded
in reviews/2026-10-31-all-dimensional-static-occupation/scientific-adjudication-v1.md.
Frozen proof/report unchanged. Original full sharp/source goal stays ACTIVE.

## 1. Exact model, physical pairings and named inputs

Fix the ORIGINAL nonzero nonnegative even positive-definite tempered Radon
Gamma on R^d, d=1,2,3, with Gamma(rA)=r^(d-alpha)Gamma(A),
0<alpha<d or alpha=d=1, 0<a<1, alpha+a<2. Its actual amplitude is kept. Write Gamma=int exp(i xi.x)mu(dxi) in
tempered distributions, with even positive tempered spectral measure mu,
in the same H:homog convention as input I. Then alpha<2-a<2, 2-alpha>0, k=3-alpha>1, q=4-alpha=k+1>2,
m=q/k>1 and D=q-2a>2-a>0. D is a SCALAR, not physical dimension.
All Sobolev spaces and tests are REAL; spectral operators may be complexified
as in the accepted input. Positive compact tests mean NONNEGATIVE NONZERO.

Define the positive sigma-finite two-point measure
 dnu(x,y)=dx Gamma(dy). For measurable spatial functions set

 B(f,h)=int_Rd int_Rd f(x)h(x-y)Gamma(dy)dx.                    (1)

Initially (1) is an extended nonnegative integral when f,h>=0. For signed
inputs it is used ONLY after absolute convergence is proved. It is NOT
multiplication by a possibly infinite a.e. convolution. Choose finite BOREL representatives of Lebesgue classes. For an arbitrary
Lebesgue version, use a Borel null superset for the following argument;
its shifted version is then measurable in the nu-completion. If N is Lebesgue null, the sets x in N and
x-y in N have nu-measure zero: integrate their indicators first in x
for each y, then against sigma-finite Gamma. Thus (1), when defined,
does not depend on the chosen representatives. The same observation
passes Lebesgue-a.e. convergence to nu-a.e. convergence at both positions.

Put A_sp(g)=B(g²,g²), b(g)=||grad g||2², initially for smooth compact g.
For a smooth compact z, U_z=Gamma*z has its usual pointwise meaning.
For rough H1 fields every pairing will retain definition(1).

OWN accepted inputs, exact scopes:
I. unmasked-variational-lower.md, scientific61ac2a3/adoption94d85ca,
   Sections1-6: ALL original Gamma/dimensions and all nonnegative nonzero
   smooth compact spacetime tests Psi. Actual bounded smooth mean h_s,
   negative unmasked Rayleigh bottom with positive rate lambda_s,
   I_Psi=int_0^1 lambda_s ds, raw cost v_Psi, positive finite real S_1,
   and original canonical point rate

 Q2=liminf_(T->infinity)T^-kappa log E|u(T,0)|²
    >=2^m S_1,  kappa=(4-alpha-a)/k,
 S_1=sup_(smooth positive Psi)(I_Psi-v_Psi/2).                 (2)

   Its same-model upper finiteness is an INDEPENDENT accepted result;
   the spatial estimates proved below are not its premises. No d1 X or
   printed firstmean/static-energy theorem is imported into this proof.
II. damped-lower-endpoint-bridge.md Section2, scientific8883160: ONLY the
   exact scalar equilibrium identity and Gamma/Beta mass computation

 f_a(t)=[t(1-t)]^(-(1-a)/2)/[Gamma_E((1-a)/2)Gamma_E((1+a)/2)],
 int_0^1 |s-t|^-a f_a(t)dt=1 for EVERY s in[0,1],
 M_a=int_0^1 f_a(t)dt
    =Gamma_E((1+a)/2)/[Gamma_E(1+a)Gamma_E((1-a)/2)]>0.          (3)

   Here f_a belongs to L1 and L2. This scalar identity has only 0<a<1
   as its parameter range. The old d1 rough-X/spatial/point consumer is
   NOT imported. Kernel-row/calculus facts below are re-derived.
III. RawValueCeiling.strict_log_gap with its COMPLETE public type: the
   OLD finite fact takes q,a with a>0 and q-2a>0 and gives Delta(q,a)>0.
   Its actual B5 application is in Section6. No new kernel run.

The old d1 spatial optimization proof is a method comparator only.
We prove the actual smooth controls, full physical H1 extension, occupation
measurability and energy bound in this original measure class.

## 2. Actual smooth time controls for every compact spatial z

Fix nonnegative nonzero z in C_c^infinity(R^d). Define

 lambda_z(c)²=sup_(real unit H1 g){c int U_z g²-b(g)}, c>0.    (4)

This is positive finite. To obtain exactly the accepted bounded-potential
input, take one nonnegative nonzero f in C_c^infinity((0,1)), fix s0=1/2,
and put k_f(s0)=int |s0-t|^-a f(t)dt, positive finite. The ACTUAL smooth
test Psi(t,x)=c f(t)z(x)/k_f(s0) has h_(s0)=c U_z. Input I therefore
gives a bounded smooth potential, the Rayleigh formula(4), and a positive
rate for every c>0. For c in[c0,1], c0>0, its square is Lipschitz with
constant ||U_z||infinity by taking the same unit suprema in(4).
Monotonicity gives lambda_z(c)>=lambda_z(c0)>0, so the square root is
also Lipschitz on this interval. Only a Rayleigh bottom is used.

Use a fixed smooth decreasing chi equal1 on[0,1],0 on[2,infinity),
with values in[0,1], as constructed in input I Section4. For integers n>=4,

 f_n(t)=f_a(t)chi(1/(nt))chi(1/(n(1-t))), 0<t<1,
 k_n(s)=int_0^1 |s-t|^-a f_n(t)dt.                            (5)

Extend f_n by0 outside(0,1). It vanishes near both endpoints, is smooth
compact and nonzero, and increases to f_a. Thus Psi_n=f_n tensor z is
an ACTUAL member of the smooth positive class in(2). In particular no
zero test at n1 or rough Gaussian test has been used. Positive monotone
convergence and(3) give k_n(s) increasing to1 at EVERY s in[0,1]. Also
0< c0:=int f_4 <=k_n(s)<=1, since |s-t|^-a>=1 on the unit square off its
null diagonal. Thus lambda_z(k_n(s))->lambda_z(1), uniformly bounded by
lambda_z(1). The actual mean of Psi_n is k_n(s)U_z, so its accepted rate
is exactly lambda_z(k_n(s)). Dominated convergence gives

 I_(Psi_n)->lambda_z(1).

Its raw cost is the physical nonnegative Tonelli pairing
v_(Psi_n)=B(z,z)int_0^1 f_n(s)k_n(s)ds. Since f_n k_n increases to f_a,
it converges to M_a B(z,z). Here B(z,z) is finite and positive: the spatial
smooth autocorrelation is compact, continuous and strictly positive near0,
and Gamma charges every ball centered at0. The latter follows by scaling
one ORIGIN-CENTERED ball B(0,n) of positive mass (these exhaust R^d),
then its Radon homogeneity.
Taking the limit of the EACH-FIXED-n real score inequalities in(2) yields

                    S_1>=lambda_z(1)-M_a B(z,z)/2.           (6)

The score differences themselves need not increase. No test depends on
original T or a weak-noise parameter, and no rough evolution/time limit
exchange has occurred. This proves B1.

## 3. Actual static controls and a uniform smooth spatial ratio

Let g be a real unit C_c^infinity profile. Then b=b(g)>0: a unit L2
function with zero weak gradient would have Fourier support only at0
and hence would be zero. Also 0<A=A_sp(g)<infinity by the compact
square-test autocorrelation argument just used. Set R(g)=A/b^(alpha/2).
For ell>0 let U_ell g(x)=ell^(d/2)g(ell x). It is an L2-unitary H1
bijection with inverse U_(1/ell), preserving smooth compact profiles.
The actual change of variables in(1), with Radon pushforward
int F(ell y)Gamma(dy)=ell^(alpha-d)int F(z)Gamma(dz), gives

 A_sp(U_ell g)=ell^alpha A_sp(g), b(U_ell g)=ell² b(g).        (7)

The factors in the first equality are ell^(2d) from the two densities,
ell^(-d) from dx, and ell^(alpha-d) from Gamma. No angular density
assumption or unitary Fourier normalization is hidden here.

For theta,ell>0 choose the ACTUAL nonnegative nonzero compact smooth
z=theta (U_ell g)². Testing(4) at U_ell g gives
lambda_z(1)²>=theta ell^alpha A-ell²b. Its raw spatial cost is
B(z,z)=theta²ell^alpha A. Write u=alpha/q>0. For any L>0 choose

 ell²=uL²/b, theta=(1+u)L²/(ell^alpha A).                     (8)

Both are positive and the radicand is L². By(6),

 S_1>=L-C L^q, C=M_a(1+u)²/[2R(g)u^(alpha/2)]>0.             (9)

Every choice is a fixed actual smooth control. Derivative1-qC L^(q-1)
changes sign once; the maximum over L>0 occurs at L^k=1/(qC) and equals
(k/q)(qC)^(-1/k). Since 1+u=4/q and q-1=k, direct substitution gives
1/(q^q C)=R(g)alpha^(alpha/2)/[8M_a q^(q/2)]. Hence

 S_1>=k[(R(g)/M_a)alpha^(alpha/2)/(8q^(q/2))]^(1/k).          (10)

This re-verifies the coefficients in every original dimension, rather
than importing the d1 consumer. Finiteness of S_1 from input I bounds
ALL these smooth ratios by the same finite positive number
8 M_a q^(q/2)(S_1/k)^k/alpha^(alpha/2). A normalized compact bump gives
one positive ratio. Therefore their supremum R0 is a positive finite
REAL number. This is the first spatial uniform estimate, obtained without
assuming a spatial GN inequality or the H1 extension that follows.
This proves B2.

## 4. Physical H1 extension, absolute four-linear bound and density

For smooth compact real f, normalization in the definition of R0 gives

 A_sp(f)<=R0 N(f)^4,
 N(f)=||f||2^(1-alpha/4)||grad f||2^(alpha/4)<=||f||H1.         (11)

For f=0 both sides are0; otherwise divide by ||f||2. All exponents in
N are positive. Smooth SIGNED spatial test covariance is positive:
with Qhat(xi)=int exp(i xi.x)Q(x)dx, convention H:homog gives

 B(Q,Q)=int |Qhat(xi)|² mu(dxi)>=0, Q in C_c^infinity real.   (12)

Indeed pair Gamma with the smooth compact correlation int Q(x)Q(x-y)dx;
its Fourier integral in the stated convention is |Qhat|². The spectral
integral is finite by rapid decay and tempered mu. Formula(12), or the
quadratic polynomial for Q+tP, gives covariance Cauchy-Schwarz for all
smooth signed Q,P. Here B(Q,P)=B(P,Q): change (x,y) to(x-y,-y)
and use evenness of Gamma. In particular

 0<=B(f²,h²)<=sqrt(A_sp(f)A_sp(h))<=R0 N(f)²N(h)²             (13)

for smooth compact real f,h. Their SQUARES are already nonnegative smooth
tests even when f,h change sign; no unsmoothed modulus is assumed smooth.

Smooth compact functions are dense in H1 in every dimension here. To see
this, multiply f by a cutoff zeta_R equal1 on B_R,0 outside B_(2R),
with ||grad zeta_R||infinity<=C/R. The f/grad f tails and the bound
||(grad zeta_R)f||2<=C||f||2/R give H1 convergence. Mollification then
converges in H1 by L2 translation continuity of the function and its weak
gradients, and preserves compact support. H1 is separable, for example
through its closed isometric image f->(f,grad f) in separable L2^(d+1).

For arbitrary real H1 f,h choose smooth compact f_n,h_n converging in H1
and, along a common subsequence, Lebesgue-a.e. Because of the null-set
observation after(1), their squares converge at both two-point positions
nu-a.e. Fatou in the NONNEGATIVE physical integral and(13) give

 0<=B(f²,h²)<=R0 N(f)²N(h)²<infinity.                        (14)

N is continuous in H1, so its smooth-approximation norms have the stated
limit. In particular this proves the diagonal bound(11) on all real H1.
No continuity or equality of pairings has been inferred from Fatou alone.

For arbitrary real H1 f1,...,f4, apply ordinary Cauchy-Schwarz to the
POSITIVE two-point measure nu, grouping f1(x)f3(x-y) and f2(x)f4(x-y).
The two squared integrals are finite by(14). Thus

 int |f1(x)f2(x)f3(x-y)f4(x-y)|dnu
   <=sqrt(B(f1²,f3²)B(f2²,f4²))<=R0 product_(j=1..4)N(fj).    (15)

This proves ABSOLUTE convergence of the actual signed four-linear form
C4(f1,f2,f3,f4)=B(f1 f2,f3 f4), with |C4| bounded by R0 times the product
of H1 norms. It is consequently jointly continuous: expand a difference
by changing one argument at a time, and apply this bound to each of the
four terms. Representative independence was already checked in(1).
This is a physical-integral proof, not an abstract completion assertion.

In particular A_sp and (f,h)->B(f²,h²) are continuous in H1. Smooth signed
covariance PSD passes to finite linear combinations of H1 square tests
by this actual continuity. Applying it to f²+t h², or passing the smooth
Cauchy-Schwarz inequality to limits, yields the EXACT physical bound

              0<=B(f²,h²)<=sqrt(A_sp(f)A_sp(h))              (16)

on the full H1 class. This closes the pairing/density issue beyond the
one-sided Fatou step. It uses neither a global H1 supremum embedding nor
a d1 density split. Absolute-value approximations are unnecessary here:
the nonnegative approximants needed for Fatou were the squared signed
smooth approximants in(13), and signs enter only after(15).

Let R_sp be the ratio supremum over ALL real unit H1 profiles. Their
gradient energies are positive as before. The diagonal estimate(14) gives
R_sp<=R0, while smooth inclusion gives the reverse; hence R_sp=R0>0
finite. Also for every real H1 f, including zero, (11) is the promised
homogeneous inequality with constant R_sp. Continuity proves more: any
normalized smooth compact approximation to a unit H1 profile has the same
limiting ratio, since its positive denominator b(f) is approached in H1.

For completeness A_sp(f)>0 for any nonzero H1 f. Choose a bounded finite
positive-measure set E on which |f|>=c>0. The correlation of 1_E is
continuous and positive near0 by L2 translation continuity. Gamma charges
that ball, so B(f²,f²)>=c^4 B(1_E,1_E)>0. This is a nonnegative-integral
lower bound and does not need 1_E in H1. Its finiteness follows from(14).

Define the real spatial energy E_sp=sup_(real unit H1)(A_sp-b/2).
For a fixed unit profile with A,b>0, (7) extends either by actual positive
changes of variables or by H1 continuity. The maximum over ell>0 of
ell^alpha A-ell² b/2 occurs at ell^(2-alpha)=alpha A/b and equals
(2-alpha)alpha^(alpha/(2-alpha))R(g)^(2/(2-alpha))/2. Taking the two
suprema (ell1 already includes every profile) and approximating R_sp gives

 E_sp=(2-alpha)/2*alpha^(alpha/(2-alpha))*R_sp^(2/(2-alpha)),
                   0<E_sp<infinity.                         (17)

No optimizer is assumed. Taking smooth ratios approaching R_sp in(10),
then substituting(17), gives

 S_1>=M_a^(-1/k)F_0(E_sp),
 F_0(z)=k[(1/(8q^(q/2)))*(2z/(2-alpha))^((2-alpha)/2)]^(1/k), z>0. (18)

These prove B3 on the full real H1 class and its physical integrals.

## 5. Kernel row and full strongly measurable occupation class

With the SAME D=q-2a>0 define the positive even kernel

 K_star(u)=Gamma_E(a)^(-1)int_0^infinity
          exp[-(lambda+lambda²/(2D))|u|]lambda^(a-1)dlambda.    (19)

For u!=0 it is positive finite and <=|u|^-a by dropping only the
quadratic damping and using the positive Gamma integral. Its infinite
value at0 may be changed arbitrarily on that null set in time integrals.
It is decreasing on u>0 and locally integrable because a<1. With
Phi(t)=int_0^t K_star(u)du, Phi is concave. The time row at s in[0,1] is
Phi(s)+Phi(1-s)<=2Phi(1/2), with equality at s=1/2. Thus

 R_star=2int_0^(1/2)K_star(u)du in(0,infinity)                 (20)

is the EXACT row maximum. This fact is not a claim of energy-bound
attainment or optimality for a time-dependent occupation profile.

Let O be the FULL class of real strongly H1-measurable g:(0,1)->H1,
||g_s||2=1 a.e., T(g)=int_0^1 b(g_s)ds<infinity. Then
int ||g_s||H1² ds=1+T(g), so it is an L2-in-time H1 field. Choose a fixed
unit compact bump on exceptional null times, using a strongly measurable
separably valued representative. The map s->b(g_s) is measurable because
the squared gradient norm is continuous on H1. Joint measurable spatial
representatives exist: approximate the Bochner field by simple H1-valued
functions in L2(time;H1), choose measurable spatial representatives for
their finitely/countably many values, and a subsequence summable in the
L2(time;H1) errors. It has a measurable spacetime L2 limit and for a.e.
s the same L2 spatial representative as g_s. The two-point null-set argument
makes every physical pairing independent of these choices.

The map (f,h)->B(f²,h²) is jointly continuous on separable H1 x H1 by(15).
Consequently (s,t)->B(g_s²,g_t²) is measurable, agrees a.e. with its actual
nonnegative spatial double integral and is representative-independent.
With F(s)=b(g_s)^(alpha/4), equations(11),(16) give
B(g_s²,g_t²)<=R_sp F(s)F(t). Since alpha/2<1,
F in L2 and int F²=int b^(alpha/2)<=T(g)^(alpha/2) by concavity on
the unit time interval. The inequality 2F(s)F(t)<=F(s)²+F(t)² and(20)
therefore prove

 J(g):=int_(0,1)^2 K_star(s-t)B(g_s²,g_t²)dsdt
        <=R_star R_sp T(g)^(alpha/2)<infinity.               (21)

All integrands are nonnegative; Tonelli is legitimate before finiteness
is established. Changing null times affects a product-null set and cannot
change this Lebesgue time integral. No spatial point trace or rough SPDE
was introduced.

Define the OWN energy over exactly this O by

 E_star^O=sup_(g in O)(J(g)-T(g)/2).                          (22)

The scalar maximum of R_star R_sp T^(alpha/2)-T/2 over T>=0, found by
differentiation, is R_star^(2/(2-alpha))E_sp from(17). Thus(22) is bounded
above by that finite number. It is nonempty and positive: take a constant
in time unit compact bump and its occupation dilation U_ell. Its J is
J0 ell^alpha A, with J0=int_(0,1)^2 K_star(s-t)dsdt positive finite,
whereas T=ell²b. For sufficiently small ell>0, alpha<2 makes
J0 ell^alpha A-ell²b/2>0. Hence the supremum is a positive finite real and

                 0<E_star^O<=R_star^(2/(2-alpha))E_sp.       (23)

This is an EXPLICIT comparison, not a proven optimal/attained ratio. No
restriction of O to smooth time fields, compact profiles or optimizers was
made in the upper bound. This proves B4.

## 6. Original point lower in the explicitly defined energy

F_0 in(18) is positive and increasing, with degree (2-alpha)/(2k)>0.
Thus(23) gives F_0(E_star^O)<=R_star^(1/k)F_0(E_sp). Combine this with
(2),(18) to obtain the SAME original point lower

               Q2>=2^m(M_a R_star)^(-1/k)F_0(E_star^O).     (24)

Put
 Delta(q,a)=[qlogq+(q-2a)log(q-2a)]/2-(q-a)log(q-a),
 F_a(z)=exp(Delta/k)F_0(z),
 Omega=[M_a^(-1)/(R_star expDelta)]^(1/k)>0.                  (25)

The OLD RawValueCeiling.strict_log_gap applies with its EXACT guards
ha:a>0, hpos:q-2a=D>0, so Delta>0. This scalar conclusion does not prove
any new covariance/energy/control claim. Multiplying the two positive
factors in(25) cancels expDelta: Omega F_a=(M_a R_star)^(-1/k)F_0.
Consequently(24) is exactly

                   Q2>=2^m Omega F_a(E_star^O).             (26)

All energies/costs retain the ORIGINAL Gamma amplitude and literal kinetic
penalty1/2. Neither an actual firstmean nor an author energy/label convention
was used. We claim Omega>0 only; no wider Omega>1 theorem is imported from
historical d1 results or an unreviewed future target. This proves B5.

## 7. Calibration, finite evidence and remaining original goal

Every original dimension/covariance, including invariant-direction and
alpha>1 cases, was retained. All rough forms are physical two-point
integrals; no global H1 supremum embedding, d1 near/far split, unmasked
ground eigenvalue or growing-mask/noise limit interchange was used.
The stochastic inputs were already accepted EACH-smooth-test statements;
all subsequent limits are numerical control/variational limits after them.

The one OLD finite strict_log_gap has its complete public type/source and
exact prior-byte bindings in lean-reuse-v1.json. Its two new guards are
explicit in Section6. No new compiler/kernel/replay or fact count;71facts/
18local seams/L0 PROPOSED unchanged. Physical PSD, Fatou, four-linear
continuity, Sobolev density, Gamma/time integrals, measurable occupation,
scalar differentiation and actual point identification remain ANALYTIC.
No official package/companion or formal SPDE result follows.

The pre-proof controls in diagnostics-v1.json concern actual covariance
models and smooth temporal cutoffs, but do not prove general H1 continuity.
Gaussian spatial controls are H1 and not compact; compact bump models were
separate.50/80working digits test algebra, with double-precision bump
inputs, while GL256/512 differences are not certified error. Negative
controls were closed-form WRONG-normalization ratios, not propagated
through the evaluator. No off-diagonal four-linear, d3 continuity or
amplitude sweep, eigenvalue or actual SPDE moment was computed.
K_star,R_star,Omega and E_star^O were NOT numerically evaluated. The
7.50069e-7 two-degree temporal difference is not used in any proof bound.

The exponent kappa and p2 factor in(2),(26) retain the required static
scale as a tends to0. This concerns ONLY kappa and the factor2^m;
no limit of M_a,R_star,Omega or the energies is proved here. No optimized
static numeric constant is asserted.
Separate Jensen bounds, with any source-normalization premise they require,
remain available and may be combined with(26) by a maximum. We do not
replace a p1 theorem or equate Stratonovich and Skorohod constants.

E_star^O has the FULL strong-H1/a.e.-normalized/finite-integrated-energy
meaning in(22). Identifying it with a particular intended author-domain
reading, repairing a printed normalization or using an author firstmean
label is NOT done here. All-alpha Omega>1, intended source/domain map,
matching sharp upper, conditional exact limit, whole-paper/cold-reader/
novelty/circulation gates remain OPEN. No source repair/contacts/Skorohod/
HPC/TeX/PDF/wiki/privatecompanion/publication. Full original goal ACTIVE.
