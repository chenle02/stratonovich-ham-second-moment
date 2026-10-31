# Canonical source convergence in the masked operator-driver norm

ACCEPTED after independent Opus5.5/HIGH full proof review: ten checks,
PASS_WITH_NOTES, no required repairs. See the scientific adjudication in
reviews/2026-10-30-source-operator-convergence/. The frozen scientific
candidate is retained at revision da9d464; the changes below clarify the
five minor findings without replacing an estimate or construction.
This concerns LINEAR Gaussian first drivers. It proves no nonlinear Young
flow, canonical-solution identity, pointwise Sobolev evaluation or new
solution-moment asymptotic.

## 1. Objects, inputs and statements

Use the original H:homog class in d=1,2,3, with a=alpha_0 in(0,1),
alpha+a<2, and 0<alpha<d or alpha=d=1. Gamma and its even positive
spectral measure mu have convention Gamma=int exp(i xi.x)mu(dxi).
Spatial Fourier transform is UNITARY, c_d=(2pi)^(-d/2).
Let H be the real positive-time test-noise null-quotient completion and
W its GIVEN isonormal Gaussian process. Zero covariance is trivial.

Fix R,T>0, E=H^(1/2)xH^(-1/2), and a real compact smooth physical mask
zeta_R as in the accepted actual-operator-driver.md. Fix

 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<beta<min(1-a/2,(3-a-alpha)/2).

Write Btheta=C^theta([0,T];B(E)). From that OWN accepted theorem choose
once a smooth compact-test RAW H-ONbasis {f_j}, and its RAW deterministic
operator paths A_j(t), so

 M_N(t)=sum_(j<=N)W(f_j)A_j(t) -> M_R in Lp(Omega;Btheta), p>=1.     (1)

The finite paths have compact values; all finite p convergence, strong
measurability in the countable closed path span, actual raw matrix forms,
and Gaussian sqrt(p)/exponential local norm estimates are named inputs.
No source field is presumed to have the same CM coefficients as W.

**Theorem 1 (Gaussian transfer).** Let Y be a centered Gaussian linear
noise on the raw smooth tests, on a common coupled probability space,
with Var Y(F)<=C||F||_H^2, C>=0. It extends to H. The paths

    M_Y,N(t)=sum_(j<=N)Y(f_j) A_j(t)                               (2)

converge in every finite Lp(Btheta), p>=1, to an actual Gaussian compact-
valued path M_Y, and

 ||M_Y-M_Y,N||_LpBtheta<=sqrt(C)||M_R-M_N||_LpBtheta,
 ||M_Y||_LpBtheta<=sqrt(C)||M_R||_LpBtheta.                          (3)

Y(f_j) need not be independent. For each fixed REAL Schwartz phase pair
and time t,

    <M_Y(t)z,w>_E=Y(h_R,t;z,w) in L2,                             (4)

where h_R is the literal raw noise test zeta_R times the wave product
with the actual E-adjoint, including the time indicator. The map is
linear on jointly Gaussian noise families, basis independent up to
indistinguishability, and complexifies with the usual sesquilinear pairing.
If (W,Y_n) are jointly centered Gaussian, with uniform bounds for Y_n and
D_n=W-Y_n relative to raw H, and Var D_n(F)->0 on smooth compact tests,
then M_Yn->M_R in every finite Lp(Btheta).

**Theorem 2 (canonical source).** On a possibly enlarged Gaussian space
retaining the actual GIVEN W, construct the author's epsilon,delta family
with the heat kernel (1.20) and Laplace prefix (2.9). For epsilon,delta>0,

 Cov(Y_(epsilon,delta)(t,x),Y_(epsilon',delta')(s,y))
    =K_(delta max delta')(t-s) Gamma_(epsilon+epsilon')(x-y),       (5)
 K_delta(v)=Gamma_E(a)^-1 int_0^(delta^-1)
                               exp(-lambda|v|)lambda^(a-1)dlambda,
 Gamma_epsilon=p_epsilon*Gamma,
 p_epsilon(x)=(2pi epsilon)^(-d/2)exp(-|x|^2/(2epsilon)).

There are corresponding masked first drivers M_R^(epsilon,delta), and

 M_R^(epsilon,delta)->M_R in every finite Lp(Btheta)                (6)

as epsilon,delta->0 at arbitrary relative rates. Raw W and M_R are
retained by pullback, not replaced by equal-law variables. The source
and full residual drivers have uniform Gaussian sqrt(p) and exponential
local pathnorm bounds, for fixed R,T and admissible exponents.

For each FIXED positive epsilon,delta, the pointfield has a version
continuous in time and smooth in space, all spatial derivatives jointly
continuous on compact cones. Its ordinary masked first response

 int_0^t S(-u)B(zeta_R Y_(epsilon,delta)(u,.))S(u)du                 (7)

exists as a statewise integral and an operator-norm Lipschitz path on E;
it agrees indistinguishably with M_R^(epsilon,delta). S is the massless
wave phase and B(b)(v,w)=(0,bv). No operator-norm continuity of S is used.
Versions and (7) are per fixed source parameters; no common null set for
all uncountably many parameter pairs is asserted.

The exact source inputs are the pinned AUTHOR pages5,6,8,9: (1.20),
(1.21), (2.9) and (2.11). The paper's law-redefinition does not prove
given-W retention; our extension and the Radon implementation are new
proofs below. We do not import its page8 increment display, whose spatial
index differs from (2.9), or any first-mean/energy/conjectured-limit claim.

## 2. Finite Gaussian comparison for a Banach linear image

Let v_1,...,v_N lie in any real Banach space, and let xi be a centered
Gaussian vector with covariance C_N<=C I. On an auxiliary space take an
independent centered Gaussian vector Z with covariance C I-C_N. For
p>=1 the scalar function

    phi(x)=||sum_j x_j v_j||^p

is continuous and convex; it may be a SEMINORM power, not a norm on
R^N. Its finite Gaussian expectations are finite by the finite sum bound.
Conditional Jensen on R^N gives E phi(xi)<=E phi(xi+Z). The latter
Gaussian vector has covariance C I, hence the law of sqrt(C) times a
standard independent vector. Thus

 (E||sum xi_j v_j||^p)^(1/p)
        <=sqrt(C)(E||sum g_j v_j||^p)^(1/p).                       (8)

C=0 is immediate. This proves the finite-image extension of the OWN
foundation Section4 comparison. It assumes no independence among xi_j
and no infinite-dimensional comparison or Banach conditional expectation.
The auxiliary Z is only for this inequality; it does not change the
coupling where the actual xi live. No nonlinear PDE solution is compared.

## 3. Actual Gaussian transfer and stability in the FULL path norm

The variance hypothesis extends Y continuously from tests to H, as an
actual linear map into L2 on its given probability space. Raw-null tests
are also Y-null. Completion preserves Gaussian finite-dimensional laws.
For any finite subset of the raw basis, its evaluation covariance obeys
Cov(Y(f_i),Y(f_j))<=C I: apply the variance bound to a real linear
combination of orthonormal f_j.

Apply (8) with v_j=A_j(.) in Btheta, including any finite tail j=N+1,...,M.
The raw standard Gaussian comparison vector has the law of W(f_j), even
when those actual raw variables are correlated with Y on the common space.
Equation(1) makes (2) Lp(Btheta) Cauchy. The finite paths lie in the same
separable closed span of the countable A_j(.) as (1). Its Banach Lp
completion gives a strongly measurable limit on the ACTUAL space of Y.
For example choose an Lp-Cauchy subsequence with summable successive Lp
differences; its L1 differences sum almost surely, yielding a Banach norm
limit, and Fatou gives convergence of the full sequence. Different p
limits coincide by convergence in probability. Letting M->infinity in
the finite tail inequalities proves (3). An almost surely uniformly
convergent subsequence proves compact values at all times on one path set.
Every continuous linear functional is an L2 limit of finite Gaussian
linear combinations, so the path is Gaussian.

For real Schwartz z,w let h=h_R,t;z,w in H. Its membership and the exact
Sobolev-adjoint wave product are the accepted actual-variance/operator
inputs. For t>1 split its indicator into finitely many short intervals;
endpoints are null in the noise norm, so linearity gives the same h.
The raw coefficient identity is

 <A_j(t)z,w>_E=E[W(h)W(f_j)]=<h,f_j>_H.                            (9)

Consequently the finite matrix coefficient in (2) is Y(P_N h), where
P_N is RAW H orthogonal projection onto f_1,...,f_N. Since P_N h->h,
Y(P_Nh)->Y(h) in L2. The operator-path L2 limit gives (4) on the SAME
space. No filter was commuted through the physical mask or a wave group.
For complex pairs, extend the real noise linearly and the real operators
complex linearly; four real pair identities give conjugate linearity in w.
No point evaluation of an E displacement is used, in any dimension here.

Two choices of raw smooth ONbasis give the same actual Y matrix forms.
Compare a countable dense Schwartz phase set at rational times, then use
phase density and path continuity. This proves indistinguishability. For
jointly Gaussian Y,Z, any real linear combination has a raw variance
bound by the L2 triangle inequality. The finite sums are linear in the
noise, hence so are their Lp path limits.

For stability put D_n=W-Y_n. Joint Gaussianity makes this a centered
Gaussian noise. Fix p. The uniform variance bound and (3) give

 ||M_Dn-M_Dn,N||_LpBtheta
         <=sqrt(C_D)||M_R-M_N||_LpBtheta,                          (10)

uniformly n. For fixed N, the covariance matrix of (D_n(f_j))_(j<=N) is
positive and bounded by its trace times I, with trace
s_N(n)=sum_(j<=N)Var D_n(f_j)->0. Applying (8) again gives
||M_Dn,N||_LpBtheta<=sqrt(s_N(n))||M_N||_LpBtheta. First choose N to
make (10) small, then n large to control the finite part. Linearity
identifies M_Dn=M_R-M_Yn, proving Theorem1. The same splitting proves a
multiparameter limit directly when each fixed test error tends to0;
there is no rate relation or uncountable-version step hidden in it.

## 4. Spatial Hilbert space and a given-W-retaining source coupling

Let H_Gamma be the real spatial test null-quotient Hilbert space with

 B_Gamma(f,g)=int Gamma(dy)int f(x)g(x-y)dx
            =(2pi)^d int hat f(xi)conj(hat g(xi))mu(dxi).           (11)

The last integral is real for real tests by even mu. This is the OWN
foundation's spatial normalization. Local Radon mass gives continuity
on compact test supports, proving separability as in the raw test-space
argument. Schwartz functions are included by expanding smooth cutoffs:
convergence in Schwartz seminorms makes the covariance correlation pairing
converge against tempered Gamma.

Heat C_epsilon f=p_epsilon*f has Fourier multiplier
m_epsilon(xi)=exp(-epsilon|xi|^2/2). By (11) it is a positive selfadjoint
contraction, I-C_epsilon is a contraction, and C_epsilon->I strongly.
These statements first follow by dominated integration on dense Schwartz
tests and then on the completion. Heat maps those tests into Schwartz
functions in the same completion. No bounded PHYSICAL mask multiplier
on the raw noise quotient is being asserted.

Set nu_a(dlambda)=lambda^(a-1)dlambda/Gamma_E(a) and

 G=L2((0,infinity)_lambda xR_r, nu_a(dlambda)dr;H_Gamma),
 Phi F(lambda,r)=sqrt(2lambda)int_(t>0,t>=r)
                         exp[-lambda(t-r)]F(t,.)dt.               (12)

This real Hilbert space is separable by countable simple functions on
rational rectangles and spatial separability. For finite temporal-spatial
tensors, the elementary identity

 int_(-infinity)^min(t,u)2lambda exp[-lambda(t+u-2r)]dr
                         =exp(-lambda|t-u|)

and the Laplace formula in source(1.21) give ||Phi F||_G^2=||F||_H^2.
All signed interchanges are legitimate: finite sums of compact temporal
factors reduce them to integrals of |tau(t)sigma(u)||t-u|^-a, finite
because a<1, times fixed finite spatial inner products. No Fubini over
infinite spectral total mass is used. Such tensors are dense in raw H
by smooth time partitions on a compact test support, so Phi extends as
an isometry with CLOSED range. The coordinate r is an auxiliary integral
variable, not a newly assigned value of raw negative-time noise.

For a general smooth compact F, (12) also represents this extension almost
everywhere. Indeed choose finite smooth tensor approximants F_n on one
fixed support, converging uniformly there. The physical covariance form
against the tempered Radon Gamma bounds their spatial H_Gamma errors
uniformly in time by a constant times their uniform errors. For fixed
lambda,r, the time integral in (12) therefore converges in H_Gamma.
Meanwhile Phi F_n converges in G by the isometry; a subsequence converges
almost everywhere as H_Gamma-valued functions. Its two limits coincide.

Let P be orthogonal projection in G onto Phi H. On a product extension
of the original probability space, take an independent isonormal J on
(Phi H)perp, built from a finite/countable ONbasis and independent standard
Gaussians. Define

    I(g)=W(Phi^-1 P g)+J((1-P)g).                                 (13)

It is isonormal on G by orthogonality and independence. For each fixed
h in H, I(Phi h)=W(h) in L2, with the actual original variable retained
by pullback. Thus this is stronger than the author's page9 law-only
redefinition, and is proved here rather than attributed to that paragraph.
It need not put every cutoff into the minimal raw-W Gaussian span.
In particular this is existence of a retaining coupling: the cutoff
family can depend on the auxiliary J and is not asserted to be determined
by W alone.
For the countable fixed basis f_j, the equalities hold on one common
probability-one set. The raw finite operator paths in (1), and hence their
Lp limits, are exactly the pullbacks of the already constructed raw paths.

Let P_delta multiply G by 1_(lambda<=delta^-1), and let C_epsilon act
fiberwise on H_Gamma. They commute. Define

 Q_rho=C_epsilon P_delta, rho=(epsilon,delta),
 Y_rho(F)=I(Q_rho Phi F), D_rho(F)=I((1-Q_rho)Phi F).                (14)

These fields are jointly Gaussian with the fixed raw W, and D_rho=W-Y_rho.
The source construction is not temporal convolution.

## 5. Exact source law, domination and strong deterministic-test limit

The spatial heat covariance function is

 Gamma_epsilon(x)=int p_epsilon(x-y)Gamma(dy)
                 =int exp(i xi.x)m_epsilon(xi)mu(dxi).             (15)

The distribution identity gives the equality without illegal oscillatory
Fubini. Heat spectral moments of all orders are finite for tempered mu,
so this function is smooth with bounded derivatives. In particular
B_Gamma(p_epsilon(x-.),p_epsilon'(y-.))=
Gamma_(epsilon+epsilon')(x-y): in (11) the two c_d factors of the heat
Fourier transforms cancel (2pi)^d exactly.

For each positive epsilon,delta define the G vector

 v_rho;t,x(lambda,r)=1_(lambda<=delta^-1)sqrt(2lambda)
       exp[-lambda(t-r)]1_(r<=t) p_epsilon(x-.).                   (16)

Its squared norm is K_delta(0)Gamma_(2epsilon)(0)<infinity. Thus I(v)
defines the SOURCE pointfield, with no raw point-noise evaluation. Taking
the two-vector inner product in G gives exactly(5): the common lambda
range is up to min(delta^-1,delta'^-1)=(delta max delta')^-1; the r
integral gives exp(-lambda|t-s|), and the spatial factor is (15) at
width epsilon+epsilon'. This proves source(2.9),(2.11) in our Radon/white
convention as well as the function case. It also fixes the heat normalization
from source(1.20). No source energy or conjectured moment constant is used.

For a smooth compact spacetime test F, the Bochner G integral of F(t,x)v
exists, and equals Q_rho Phi F. Strong measurability of v follows from
its G-norm continuity, obtained directly from (5) by the increment
calculation (17) below with b=0; this calculation uses no test integration.
Its norm is bounded on each compact parameter set. Integrate the heat translates in x to
obtain C_epsilon F(t,.), then the time factor in(12). Applying the bounded
linear map I:G->L2(Omega) proves that mean-square pointfield test integration
is Y_rho(F) of(14). Matrix tests with indicators follow by raw completion
and fixed-support L1 approximation; (16) has uniformly bounded G norm on
that compact set, and (14) is a raw-H contraction. The equality is on the
common space, not merely equality of covariances.

For g in G, orthogonal lambda ranges give

 ||(1-Q_rho)g||^2
 =||(1-P_delta)g||^2+||P_delta(1-C_epsilon)g||^2<=||g||^2.

Also ||Q_rho g||<=||g||. These prove BOTH variance dominations in the
target with constant1. Only disjoint lambda ranges are independent. The
heat defect within P_delta generally correlates with the heat-smoothed
source, so independence of the FULL residual is not asserted.

P_delta->I strongly as delta->0 by the L2 tail integral in lambda.
Fiberwise C_epsilon->I strongly on G follows first on simple functions,
then by its uniform contraction bound. The estimate

 ||(1-Q_rho)g||<=||(1-C_epsilon)g||+||(1-P_delta)g|| ->0

holds for any relative rates of the two parameters. Hence Var D_rho(F)->0
for EVERY F in H. Source and residual are centered Gaussian maps on that
H with covariance bounds1. Theorem1 applies directly on literal masked
matrix tests, giving (6) and M_Drho=M_R-M_R^rho. This does not commute
heat or a wave operator through zeta_R.

The same comparison gives ||M_R^rho||_LpBtheta,||M_Drho||_LpBtheta
<=||M_R||_LpBtheta. The accepted raw sqrt(p) bound and its even-moment
exponential-series argument give uniform local Gaussian moments and
exponential norms for both families. R,T remain fixed. All statements
are in Lp equivalence classes on the common enlarged space; no simultaneous
version over uncountably many rho, or large-time/source limit interchange,
is needed. This proves the source-driver convergence part of Theorem2.

## 6. Actual regularized fields: continuity and all spatial derivatives

Fix rho=(epsilon,delta)>0. For each spatial multiindex b, differentiate
(16) in x as a G-valued vector. All such derivatives exist: their squared
spatial Hilbert norms are the finite heat moments

    int xi^(2b)exp(-epsilon|xi|^2)mu(dxi),

and the next moments dominate difference quotients. Define the real
Gaussian derivative field Z_b(t,x)=I(partial_x^b v_rho;t,x). The temporal
and spatial increment computations from(5), rather than the inconsistent
index in the author's page8 increment display, give

 E|Z_b(t,x)-Z_b(s,y)|^2<=C_(rho,b)(|t-s|+|x-y|^2).                 (17)

At fixed x, use 1-exp(-lambda h)<=lambda h in the finite lambda integral;
at fixed t use |exp(i xi.x)-exp(i xi.y)|<=|xi||x-y| and the next heat
moment. Combine these two bounds by the squared triangle inequality.
This proof also covers singular/invariant-direction mu and uses no density.

Here is an explicit continuity argument. On a compact rectangle in
(t,x), Gaussian q-th increment moments, with even q, have root at most
C sqrt(q) times the parameter distance^(1/2) at small distances, by(17).
In m=d+1 parameter dimensions, the dyadic grid has at most C_m 2^(nm)
adjacent edges at level n. The maximum-edge Lq bound is at most
C sqrt(q)2^(-n(1/2-m/q)). Choose q large and 0<h0<1/2-m/q. The weighted
sum of maxima with weights 2^(n h0) has finite Lq norm. Multidimensional
binary refinement, with at most a fixed number of adjacent edges per
coordinate at each scale, constructs a continuous extension from dyadic
points. Its value at any fixed parameter point agrees with the given
Gaussian field in L2, by(17). Thus it is a modification. Exhaust countably
many nested compact rectangles exhausting the parameter domain, and all
multiindices, to obtain jointly continuous
versions for all Z_b, for this fixed rho. On overlaps the versions agree
on countably many dense points, hence everywhere by continuity; thus they
patch consistently.

These versions are actual derivatives, not merely fields with derivative
covariance. The G-valued fundamental theorem gives, for each coordinate i,

 partial_x^b v(t,x+h e_i)-partial_x^b v(t,x)
           =int_0^h partial_x^(b+e_i)v(t,x+u e_i)du.

Apply bounded linear I and use L2 integration. The continuous field
versions give the same ordinary integral; first enforce this identity
on countably many rational t,x,h and multiindices, then use joint
continuity to extend it to all parameters in the compact rectangles.
The ordinary fundamental theorem now shows partial_i Z_b=Z_(b+e_i).
Consequently Y_rho has sample spatial derivatives of every order, jointly
continuous with t. In particular t->Y_rho(t,.) is continuous in every
compact C^k spatial norm. The estimates and versions in this section are
per FIXED rho; parameter-uniform sample smoothness is not asserted.

## 7. Ordinary first-response identification on the common space

On the probability-one set of the preceding regularity, put
b_rho(t,x)=zeta_R(x)Y_rho(t,x). This is compact smooth in space and
continuous in time in every spatial derivative norm. For each Sobolev
phase E_r, multiplication estimates and the strongly continuous free
group show that

    L_rho(t)z=int_0^t S(-u)B(b_rho(u))S(u)z du                     (18)

exists as a statewise Bochner integral. Its operator increments E_r->E_(r+1)
are bounded by a finite sample constant times |t-s|. Thus it is a
Lipschitz B(E) path. No operator-norm derivative or continuity of S is
assumed, and no Banach-valued Radon-Nikodym property is needed.

At each FIXED time u the spatial duality computation is valid for any
smooth compact spatial b, regardless of its time regularity. On real
Schwartz phases,

 <S(-u)B(b(u))S(u)z,w>_E
   =int b(u,x)[S(u)z]_1(x)G_w(u,x)dx,
 G_w=-sin(u|D|)/|D|[Lambda w1]+cos(u|D|)[Lambda^-1 w2].             (19)

This follows directly from S(-u)(0,f) and the two E Bessel weights.
We do not invoke a prior statement whose hypotheses required smoothness
in time; the present computation only uses spatial smoothness at u.
For complex pairs the second factor is conjugated as usual.

Integrate(19). For a fixed Schwartz pair/time, the resulting scalar is
the ordinary integral of Y_rho against the literal h_R,t;z,w. The G-vector
pointfield identity in Section5 applies first to smooth tests. For the
continuous versions, compact Riemann sums converge pathwise to the ordinary
integral and in L2 to the G-vector integral, so these integrals agree. Approximate
the indicator wave test in the raw noise completion, with common compact
spatial support and L2-time spatial supremum error tending to0. Its L1
error tends to0 too. The pointvector norms in(16) are bounded on that
set, so their Bochner integrals converge in G; the covariance domination
in(14) gives the same L2 limit from the test-noise side. Thus

    <L_rho(t)z,w>_E=Y_rho(h_R,t;z,w)
                  =<M_R^rho(t)z,w>_E in L2.                       (20)

The equality is on the actual coupled space, not a law-only assertion.
A countable dense Schwartz phase collection at rational times, followed
by boundedness and the path continuity of both sides, proves equality
of the operator paths for all times on one probability-one set. This
establishes (7) and the remaining assertion of Theorem2. The resulting
strongly measurable path version is the already constructed M_R^rho.
Again the set is for fixed rho; (6) concerns equivalence classes in Lp
and needs no simultaneous version for all uncountable cutoff parameters.

## 8. Source fidelity, controls and remaining original goal

The source identities used here are exactly the AUTHOR heat normalization
(1.20), Laplace identity(1.21), self covariance(2.9) and joint covariance
(2.11), on the pinned rendered pages5,6,8,9. Its common-slice construction
redefines raw W without changing law; given-W retention on an extension
was proved in(12)-(13). The Radon implementation and all operator-path
applications were also proved here. We derive(17) from the correct joint
covariance and do not silently copy or repair the source's page8 epsilon
index mismatch. No first-mean variational constant, arXivv1 exact limit,
or conjecture(1.22) was used.

The five-point source covariance and two wrong-parameter negative controls
use d1 white or the admissible d2 delta_x1 tensorLeb_x2 example, not d2
white noise. The 24 test profiles use raw-completion time indicators and
Schwartz spatial Gaussians, not the literal compact smooth raw basis.
The rotated two-test source covariance is non-diagonal; its finite S4
comparison checks correlated evaluations. Full heat-source/residual cross
covariances are positive in these controls, so their independence cannot
be assumed. The one-coordinate extra-Gaussian illustration proves nothing
about the FULL minimal raw-W span. Working precision is not certified
quadrature accuracy. None of these finite controls substitutes for the
Banach comparison/coupling/source-path proofs above.

No new Lean module, theorem count or71facts/18seams upgrade is claimed.
All source convergence is at fixed finite R,T and the admissible exponents.
The actual source nonlinear wave evolution, Young-flow continuity and
canonical initial datum(1,0) still require a separate proof and test-average
passage; that datum is not in global E. No point evaluation is obtained
from the balanced Sobolev phase, including in d1. Source/canonical solution
moment transfer, growing cones/ground-gap lower asymptotics in d2/3,
sharp upper constants and source normalization/domain/label/conditional
exact-limit questions remain open. Original full goal ACTIVE; no source
repair, correspondence, Skorohod/HPC/private companion, canonical TeX/PDF/
wiki edit or publication/whole-paper/cold-reader clearance follows here.
