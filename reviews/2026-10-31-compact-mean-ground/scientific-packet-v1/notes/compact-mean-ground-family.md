# Compact mean families: ground state and complementary full wave

COMPLETE CANDIDATE, not adopted before independent full proof review.
This proves the deterministic compact-family consumer proposed in target-v2,
not a random event, moment asymptotic or independently new spectral method.
The original all-dimensional sharp second-moment goal remains ACTIVE.

## 1. Exact objects and named inputs

Let d=1,2,3, I=[0,1], K_x compact, and sigma->V_sigma a continuous map
I->C_c^infinity(K_x), real and nonnegative. Assume one real w in H1 with
||w||2=1 and epsilon>0 satisfies

 int|grad w|²-int V_sigma w²<=-epsilon for ALL sigma in I.        (1)

Set M=sup_I||V_sigma||infinity. Use EXACT accepted phase
E=H1/2 x H-1/2, F=E directsum R², embedded as e+(c1,c2), and i:E->F.
Its free group S_F and ordinary compact-potential physical flow are inputs
from OWN fixed-mask-young-constant-phase.md Y1-Y4/compact base,
scientific8ad5094/adoption5969da5. In particular

 B(V)(e,c)=(0,V(e1+c1)) in E,
 ||B(V)||B(F,E)<=||V||infinity+||V||2.                           (2)

P_sigma(t) is that ACTUAL physical flow for the frozen coefficient V_sigma;
sigma is an index, not physical propagation time t or a coupling parameter.
Its E restriction is denoted P_sigma^E. The nonlinear/random consumer is
not an input or conclusion here. The scalar special case V_sigma=b(sigma)U
requires continuous b in[b0,b1] and the v1 trial; it does not replace this
full family target. Define H_sigma=-Delta-V_sigma on H2.

Imported source statements, not proved here, are Teschl2014 SECOND edition:
Theorem10.2,p258: real bounded compact potentials in R^d here give
self-adjoint H2 operator, bounded below, essential spectrum[0,infinity),
and compact smooth core; Theorem10.13,p273: IF the spectral bottom is an
eigenvalue it is simple with strictly positive eigenfunction; Theorem4.12
and Corollary4.13,pp140-141: max-min/form monotonicity, with form domain
allowed and the essential threshold used after discrete eigenvalues end.
The source kinetic operator is -Delta. Positivity is read a.e., sufficient
for the integrals below; no d1 ODE is imported into d3.

All uniformity, continuity, fractional/global-E and full-F applications,
and the actual original-profile common trial, are derived below. The old
d1 spectral-complement-transfer.md Sections2-3 is a method comparator only.
No p in L1, weighted tail, arbitrary-phase covariance ordering or printed
author energy normalization is assumed.

## 2. Ground existence, uniform gap and H2 continuity

The source10.2 applies since each -V_sigma is real smooth compact, hence
L2 in the dimensions here. Its quadratic form on H1 is
q_sigma(u)=||grad u||2²-int V_sigma|u|². To check the common form domain,
shift by c=1+M. On H1 its positive form is bounded above/below by c and1
times the usual H1 norm squared. It is therefore closed. Hilbert Riesz
representation in this coercive form norm gives the associated weak
equation (-Delta+c-V_sigma)u=f; for f in L2 it implies
-Delta u=f-(c-V_sigma)u in L2, so Fourier elliptic regularity gives u in H2.
Conversely H2 integration by parts gives that equation. Thus this is the
form of H_sigma+c, and the common form domain is indeed H1.

For unit u, q_sigma(u)>=-M. The trial(1) and the form max-min principle give

                 -M<=E1(sigma):=inf spec(H_sigma)<=-epsilon.    (3)

In particular M>=epsilon>0. The bottom belongs to the spectrum of this
lower-bounded self-adjoint operator. Since it lies below essential threshold0,
it is an isolated eigenvalue of finite multiplicity. ONLY NOW apply10.13:
it is simple and has a unique real positive-a.e. L2-normalized ground p_sigma.
Real potentials preserve complex conjugation; the normalized positive choice
fixes the real representative without a sign ambiguity.

Define E2 by the second max-min level, equal0 if a second negative eigenvalue
does not exist. Simplicity/isolation and essential threshold0 imply
E1<E2<=0. If dV=||V_sigma-V_tau||infinity, every common unit form test obeys
|q_sigma(u)-q_tau(u)|<=dV. Taking the same infima on orthogonal complements
and the same suprema in4.12 preserves this bound. Consequently

          |Ej(sigma)-Ej(tau)|<=dV, j=1,2.                      (4)

This also covers an E2 crossing to threshold0. Both levels are continuous;
their strictly positive difference on compact I has minimum Delta>0.
Put lambda_sigma=sqrt(-E1), mu_sigma=sqrt(-E2)>=0. Then

 sqrt(epsilon)<=lambda_sigma<=sqrt(M),
 lambda_sigma-mu_sigma
   =(E2-E1)/(lambda_sigma+mu_sigma)>=Delta/(2sqrt(M))>0.        (5)

There is no division by mu and no assumption of a second bound state.
Write l=sqrt(epsilon), Lambda=sqrt(M), d0=inf_I(lambda-mu)>0.

We give the ground-state continuity argument. For the positive unit p_tau,
q_sigma(p_tau)<=E1(tau)+dV<=E1(sigma)+2dV. Decompose
p_tau=a p_sigma+r, r orthogonal to p_sigma. Positivity gives a>0; a<=1.
The spectral lower bound on that orthogonal complement gives
q_sigma(p_tau)>=E1(sigma)+(E2(sigma)-E1(sigma))||r||2².
Hence ||r||2²<=2dV/Delta and

 ||p_tau-p_sigma||2²=2(1-a)<=2(1-a²)<=4dV/Delta.               (6)

For H2 use the actual eigenfunction equation

 (1-Delta)p_sigma=(1-lambda_sigma²+V_sigma)p_sigma.             (7)

Its right side is continuous in L2 by(4),(6), and bounded by1+2M in L2.
Since (1-Delta)^(-1):L2->H2 is an isometry in the Bessel convention,
p_sigma is continuous in H2 with a uniform bound. This proves all ground,
level, gap and parameter-continuity assertions of F2 before its wave bound.

## 3. Uniform fractional identification of the global phase

Let A_sigma=H_sigma+c with c=1+M and B=1-Delta. On their common form
domain H1,

                         B<=A_sigma<=cB, both >=1.             (8)

Here is the needed fractional comparison, not an assumption that an L2
bound holds in E. For positive self-adjoint T,S>=1 on a common form domain,
T<=S implies (T+t)^(-1)>=(S+t)^(-1) for t>0. Indeed the quadratic resolvent
form at f is the supremum over that form domain of
2Re<f,u>-q_T(u)-t||u||². Completing the square in the closed form norm
gives the resolvent value, and smaller q makes the supremum larger.
It follows that I-t(T+t)^(-1)<=I-t(S+t)^(-1). The scalar identity

 sqrt(x)=(1/pi)int_0^infinity t^(-1/2) x/(x+t)dt

follows by t=xr² and int_0^infinity(1+r²)^(-1)dr=pi/2. Spectral integration
and positive Tonelli, first over finite intervals then by monotone convergence,
give T^(1/2)<=S^(1/2) in forms, including the domain inclusions. Applying
this to both comparisons in(8) yields

 ||B^(1/4)u||2<=||A_sigma^(1/4)u||2
                         <=c^(1/4)||B^(1/4)u||2.              (9)

The quarter-power domain is exactly H1/2. Under L2 pairing, the dual norm
is ||A_sigma^(-1/4)z||2 for z in L2: write the pairing with A^(+/-1/4)
and use Cauchy--Schwarz, with equality obtained by a scalar multiple of
A^(-1/2)z. Completion identifies the negative entry with H-1/2. Thus

 ||(u,z)||E_sigma²=||A_sigma^(1/4)u||2²+||A_sigma^(-1/4)z||2²  (10)

is uniformly equivalent to the ACTUAL fixed global E norm. This argument
works on R^d as stated; it does not use a d1 tail estimate or a noninteger
operator-power monotonicity outside the proved square-root comparison.

## 4. Complementary wave calculus and its physical identity

For real spectral h define C_t(h)=cos(t sqrt(h)), S_t(h)=sin(t sqrt(h))/sqrt(h)
when h>0; C_t(0)=1,S_t(0)=t; and C_t(h)=cosh(t sqrt(-h)),
S_t(h)=sinh(t sqrt(-h))/sqrt(-h) when h<0. The spectral wave matrix is

            [[C_t(H_sigma),S_t(H_sigma)],
             [-H_sigma S_t(H_sigma),C_t(H_sigma)]].           (11)

Let Q_sigma^sp=I-|p_sigma><p_sigma| on L2. It commutes with H_sigma,A_sigma
and extends contractively on both entries of(10). On its spectral support
h>=E2=-mu_sigma², the isometry in(10) turns(11) into scalar matrix entries
C_t(h), sqrt(h+c)S_t(h), -hS_t(h)/sqrt(h+c), C_t(h).
They are uniformly bounded by C(1+t)exp(mu_sigma t), t>=0. For h>=0,
use |S_t(h)|<=min(t,h^(-1/2)), splitting h<=1/h>=1 for the upper off-diagonal;
the lower one is bounded by1. For -mu²<=h<0, |C_t(h)|<=exp(mu t) and
|S_t(h)|<=t exp(mu t), from its cosh integral, while |h|<=M and1<=h+c<=c.
This proves the bound also at mu=0 without dividing by mu.

On the remaining two-dimensional spatial ground phase, the growing and
decaying vectors are (p_sigma,+/-lambda_sigma p_sigma). The growing
projection is

 ell_sigma^E(u,z)=(<p_sigma,u>+<p_sigma,z>/lambda_sigma)/2,
 e_sigma^E=(p_sigma,lambda_sigma p_sigma), Pi_sigma^E=e_sigma^E ell_sigma^E.

The complementary ground branch decays as exp(-lambda_sigma t). Its two
branch projection norms in(10) are uniformly bounded because l<=lambda<=Lambda
and1<=c-lambda²<=c. Combining it with the Q^sp phase gives

 ||P_sigma^E(t)(I-Pi_sigma^E)||B(E)<=C(1+t)exp(mu_sigma t).     (12)

We justify the notation P_sigma^E in this spectral calculation. The same
matrix bounds at graph levels (A_sigma u,A_sigma^(1/2)z) give continuous
solutions in H2 x H1. These graph norms are equivalent to those Sobolev
norms: the H1 equivalence is(8), and ||A u||2 and||(1-Delta)u||2 are uniformly
equivalent since their difference is bounded by M||u||2 and A>=1.
Spectral cutoffs give u_t=z in H1 and z_t=-H_sigma u in L2, with continuous
derivatives at those levels. For compact smooth initial data, differentiating
S_E(-t)(u(t),z(t)) in H1 x L2 gives the free Duhamel formula with force
(0,V_sigma u); all terms exist in the strong generator domain H2 x H1.
It also holds in E. Uniqueness there follows by Picard/Gronwall because
u->V_sigma u maps H1/2 into L2 and then H-1/2 with bound M.
Therefore the spectral solution equals the named ordinary physical flow
on those data. Density of compact smooth data in GLOBAL E and fixed-horizon
boundedness extend equality to all E. No claim of E dense in F is used.

The same calculation gives, on all E,

 P_sigma^E(t)e_sigma^E=exp(lambda_sigma t)e_sigma^E,
 ell_sigma^E P_sigma^E(t)=exp(lambda_sigma t)ell_sigma^E.        (13)

All Sobolev pairings above are continuous: p_sigma in H2 supplies both
needed dual entries. No low-Sobolev point evaluation is involved.

## 5. The actual full-F constant-forcing projection

Physical constant coordinates evolve by C(t)(c1,c2)=(c1+t c2,c2), since
potential forces have range in iE. Put D_sigma(c1,c2)=(0,V_sigma c1) in E.
Using the E physical flow for the inhomogeneous global component gives

 P_sigma(t)(e,c)=(P_sigma^E(t)e+K_sigma(t)c,C(t)c),
 K_sigma(t)c=int_0^t P_sigma^E(t-r)D_sigma C(r)c dr.             (14)

The integral is statewise strong in E. Formula(14) solves the same F
Duhamel equation as the accepted compact-potential flow: the constant
block is fixed, and variation of constants on the E component accounts
for its forcing. Uniqueness from(2) identifies the two. Uniform finite-
horizon bounds follow from the free-group bound and Gronwall; all V_sigma
have uniformly bounded infinity and L2 norms on common K_x.

Set

 f_sigma=int V_sigma p_sigma/(2lambda_sigma)>0,
 ell_sigma^C(c)=f_sigma(c1/lambda_sigma+c2/lambda_sigma²),
 ell_sigma(e,c)=ell_sigma^E(e)+ell_sigma^C(c),
 e_sigma=i e_sigma^E, Pi_sigma=e_sigma ell_sigma, Q_sigma=I-Pi_sigma. (15)

The integral is finite by L2 Cauchy--Schwarz and strictly positive because
V_sigma is nonzero/nonnegative and p_sigma>0 a.e. Nonzeroness follows from
(1). All coefficients are norm-continuous/uniformly bounded by the compact
family, H2 continuity of p and positive floor l; no p_sigma in L1 is needed.

By(13), ell_sigma^E D_sigma C(r)c=f_sigma(c1+r c2). Direct integration gives

 ell_sigma^C(c)=int_0^infinity exp(-lambda_sigma r)f_sigma(c1+r c2)dr,
 ell_sigma^C(C(t)c)=int_t^infinity exp(lambda_sigma(t-r))
                                      f_sigma(c1+r c2)dr.      (16)

Both integrals converge absolutely since lambda>=l>0 and the integrand is
linear in r. Apply ell_sigma to(14), use(13), and combine the finite integral
with the tail in(16). This proves
ell_sigma P_sigma(t)=exp(lambda_sigma t)ell_sigma.
Also P_sigma(t)e_sigma=exp(lambda_sigma t)e_sigma and ell_sigma(e_sigma)=1.
Thus Pi_sigma is a bounded rank-one projection and

 P_sigma(t)Pi_sigma=Pi_sigma P_sigma(t)=exp(lambda_sigma t)Pi_sigma. (17)

Its F/F*/operator-norm parameter continuity follows from(6)-(7), (15) and
bounded bilinear multiplication; hence the norms are uniformly bounded.
For the actual data e0=(0,1,0), ell_sigma(e0)=f_sigma/lambda_sigma>0.
For fixed smooth compact phi>=0, integral1, O_phi(e,c)=<e1,phi>+c1 is bounded
by Sobolev duality, and O_phi(e_sigma)=int phi p_sigma>0. Each is continuous
in sigma; compact I gives strictly positive uniform minima. Positivity here
is a.e. positivity in integrals, not a d1 ODE argument or a raw point trace.

## 6. Full-F complementary physical wave and parameter bounds

Write Q_sigma^E=I-Pi_sigma^E. In(14) apply Q_sigma to(e,c), split D_sigma
into Q_sigma^E D_sigma+e_sigma^E ell_sigma^E D_sigma, and use(16). The exact
global-E component of P_sigma(t)Q_sigma(e,c) is

 P_sigma^E(t)Q_sigma^E e
 +int_0^t P_sigma^E(t-r)Q_sigma^E D_sigma C(r)c dr
 -e_sigma^E ell_sigma^C(C(t)c),                               (18)

and its constant component is C(t)c. This retains the subtracted growing
response to constants; omitting it would leave the unwanted growing mode.
Uniformly ||Q_sigma^E D_sigma C(r)||<=C(1+r). Equation(12) bounds the
integral in(18) by

 C exp(mu_sigma t) int_0^t(1+t-r)(1+r)dr |c|
 =C exp(mu_sigma t)(t+t²+t³/6)|c|.

The first term is bounded by C(1+t)exp(mu t)||e||E. The last term and the
constant component are bounded by C(1+t)|c|. Since mu>=0 this proves

 ||P_sigma(t)Q_sigma||B(F)<=C(1+t)^3 exp(mu_sigma t).            (19)

For any fixed0<eta<d0, (1+t)^3 exp(-(d0-eta)t) is bounded, so(19) gives
||exp(-lambda_sigma t)P_sigma(t)Q_sigma||<=C_eta exp(-eta t).
In particular eta can be chosen below inf lambda; the constant velocity
polynomial causes no contradiction. No scalar solution moments multiply
in this argument; it is an actual full-phase operator bound.

For finite T0 let B_sigma=iB(V_sigma). Equation(2) gives
||B_sigma-B_tau||<=||V_sigma-V_tau||infinity+||V_sigma-V_tau||2=:d_st.
Subtract the two physical free-Duhamel equations. If D(t)=P_sigma(t)-P_tau(t),
then, on states, D is the integral of S_F(t-r)B_sigma D(r) plus the integral
of S_F(t-r)(B_sigma-B_tau)P_tau(r). Uniform finite-horizon bounds and
Gronwall give

       sup_(0<=t<=T0)||D(t)||B(F)<=C_T0 d_st.                 (20)

The norm estimate follows from the statewise integrals and uniform operator
bounds; no B(F)-valued derivative or norm continuity of the free group is
assumed. The operator-norm difference is measurable in time: F is separable,
so its norm is the supremum over a countable dense set of unit inputs,
each with continuous image. Scalar Gronwall is therefore applicable.
This completes all generic deterministic family assertions F1-F3.

## 7. The full original positive tilt: exact mean and variance

Now let Gamma be NONZERO original H:homog in d1/2/3, a in(0,1),
0<alpha<d or alpha=d=1, alpha+a<2. Fix ANY nonnegative nonzero real
Psi in C_c^infinity((0,1)xR^d), not assumed separable. Choose A>=1 so its
spatial support is in B_A. Define

 h_sigma(x)=int_0^1 |sigma-u|^-a int Gamma(dz)Psi(u,x-z)du,
 q_avg(x)=int_0^1 Psi(u,x)du, Z=W(Psi).                         (21)

These are the ORIGINAL raw test and its covariance/CM mean, not a masked
Gaussian test or Psi(sigma,.). Against any smooth compact raw test F,
the covariance definition and absolute Fubini give
E[W(Psi)W(F)]=int F(s,x)h_s(x)ds dx. All spatial differences stay in a
compact set for these two tests, Gamma is locally finite, and the time
singularity is locally integrable because a<1. This identifies the linear
mean without evaluating the raw noise at a point or asserting a nonlinear
shifted-flow identity.

The exact raw variance is

 v_Psi=E Z²=int_0^1 int Psi(sigma,x)h_sigma(x)dx dsigma.         (22)

It is finite: the spatial covariance product is at most
||Psi||infinity² |B_A| Gamma(closed B_(2A)), while
int_0^1 int_0^1|sigma-u|^-a du dsigma=2/((1-a)(2-a)). No global decay or
translation bound on Gamma*h is used; compactness of Psi suffices.

Nonzero Gamma charges some B_r. By homogeneity,
Gamma(B1)=r^(alpha-d)Gamma(B_r)>0, finite by local finiteness. Hence every
Gamma(B_rho)>0. The smooth compact nonnegative correlation
Q_z=int q_avg(x)q_avg(x-z)dx has Q_0=||q_avg||2²>0 and is bounded below by
a positive number on some ball. Thus

                 Q(q_avg)=int Gamma(dz)Q_z is finite/positive. (23)

Positive Tonelli and |sigma-u|^-a>=1 on the unit square give
h_sigma>=Gamma*q_avg for every sigma in I and, from(22),
v_Psi>=Q(q_avg)>0. Both Z and v_Psi are fixed before choosing any mask.

For smoothness, extend Psi by zero in time. On compact time/spatial sets,
rewrite h_s(x)=int_R |r|^-a int Gamma(dz)Psi(s-r,x-z)dr. Derivatives in s
fall on the smooth compact test, not on the singular kernel. For s in a
fixed neighborhood of I the relevant r lie in one fixed bounded interval;
|r|^-a is integrable there. For x in a fixed compact set, z also stays in
one fixed compact set. The derivatives of Psi are uniformly bounded there.
Dominated differentiation proves smoothness in s,x and continuity of every
such derivative on compacts. Multiplication by the fixed smooth mask m_R
therefore gives a smooth I-family

                     V_sigma=m_R h_sigma in C_c^infinity(closed B_(2R)). (24)

In particular V_sigma is Lipschitz in sigma in infinity and L2 norms for
each fixed R. No lambda_sigma is asserted yet: a sufficiently large mask
and a negative trial must first be selected.

## 8. Common negative trial with the ORIGINAL Psi and cost fixed

Choose real unit psi in C_c^infinity(B2) with psi>=c0>0 on B1, for example
a smooth plateau cutoff divided by its L2 norm. Let Dpsi=||grad psi||2²,
psi_L(x)=L^(-d/2)psi(x/L), L>=max(1,2A). Its norm is1 and kinetic energy
Dpsi L^-2. Choose the actual even [0,1] mask m_R=1 on B_R with R>=2L
and R>=A. On the support of psi_L, V_sigma=h_sigma. Therefore positive
Tonelli and(21)-(23) give, uniformly sigma,

 int V_sigma psi_L²
 >=c0² L^-d int_(B_L) (Gamma*q_avg)(x)dx
 =c0² L^-d int q_avg(y) Gamma(B_L-y)dy
 >=c0² L^-d Gamma(B_(L/2)) int q_avg
 =C_G L^-alpha,
 C_G=c0²2^(alpha-d)Gamma(B1)int q_avg>0.                        (25)

Here B_(L/2) is contained in B_L-y for |y|<=A and L>=2A; all spatial
integrations involve finite compact Gamma mass. Since alpha<2, choose L
large enough that C_G L^(2-alpha)>Dpsi. Then for epsilon_R defined by
C_G L^-alpha-Dpsi L^-2>0,

 int|grad psi_L|²-int V_sigma psi_L²<=-epsilon_R for ALL sigma. (26)

This is a common trial with the SAME original Psi, q_avg, Z and v_Psi.
Only trial/mask grow. It is not all-strength binding of a single fixed
compact potential. It includes singular invariant-direction covariances
and the d1 white endpoint through the same Radon/homogeneity argument.

Fix that finite R NOW. The generic family theorem applies, so lambda_sigma
is defined with floor sqrt(epsilon_R). Only after this choice do(4),(24) give

 |lambda_sigma-lambda_tau|
 <=||V_sigma-V_tau||infinity/(2sqrt(epsilon_R))<=C_R|sigma-tau|. (27)

Thus the ACTUAL mean family has the Lipschitz rate required by the old
indexed-cone input; a merely continuous generic family in Sections1-6
was only claimed to have continuous rates. Also lambda_0>0 even though
Psi(0,.)=0: its mean in(21) integrates the whole time test.

The mask can also cover any additional fixed compact variational test
supports. On those supports int V_sigma g_sigma²=int h_sigma g_sigma²,
because m_R=1 there. Such enlargement retains(26). The raw Gaussian
variable/cost(22) is NEVER replaced by a masked covariance. For each fixed
Psi the finite mask/trial is chosen before source/time asymptotics. A later
supremum over tests must be taken after the per-test lower bound; no uniform
mask over all tests or unsupported exchange of limits is asserted.
This proves the actual-profile assertions F4.

## 9. Completion boundary of this candidate

The full positive time-dependent tilt class was retained, not replaced by
products. F1-F4 would provide the exact deterministic indexed-family cone
inputs on the ACCEPTED F=E plus constants, including positive original
entrance/tested displacement and both phase entries. The old d1 cone proof
is a method/application comparator, not a new all-dimensional random event.

Still required: actual growing-block operator errors and products, raw
Cameron shift/event/same-Z cost, all-alpha variational lower comparison,
sharp upper constant and intended source-energy dictionary. No asymptotic
lower rate, printed author constant or exact limit is proved here. Finite
matrix/quad controls are falsification aids, not these continuum proofs.
71finitefacts/18Lean seams/L0 unchanged; no new formal spectral/flow theorem,
package/companion/HPC/contact/Skorohod/source fix/TeX/PDF/wiki/publication or
independent novelty/whole-paper clearance. Full original goal remains ACTIVE.
