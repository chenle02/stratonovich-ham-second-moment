# Fractional covariance products and averaged Cameron block bounds

COMPLETE PROOF CANDIDATE, not adopted before FULL independent review.
C1-C3 statement gate source0342ce4 passed22checks/HIGH569.515s;
its seven notes are proof obligations, not a proof/upper certificate.
Original sharp/source goal remains ACTIVE.

## 1. Exact objects, spaces and direct accepted inputs

Use ALL original nonzero H:homog Gamma in d=1,2,3: even nonnegative
positive-definite tempered Radon measure with degree alpha,0<alpha<d or
alpha=d=1,0<a<1,alpha+a<2. Actual amplitudes are fixed. All spaces are REAL.
Write Lambda=(1-Delta)^1/2, ||f||H^s=||<xi>^s hat f||2 with unitary Fourier
transform. Put E=H1/2 x H-1/2, F=E directsum R², with its real Hilbert norm;
z=(z1,z2,c1,c2) represents the distribution pair z+(c1,c2), and i:E->F
is the isometric inclusion. Constants are not placed in E; E is not dense F.

For spatial tests use the actual two-point form
 B(f,h)=int dx int Gamma(dy)f(x)h(x-y).
H_sp is the real covariance-null quotient completion of C_c^infinity(R^d)
with this inner product. H_t is the analogous completion of C_c^infinity(I),
I=(0,1), with K_a(s,t)=|s-t|^-a. H is the ACTUAL completion of tests supported
in I x R^d, with product covariance K_a Gamma. It embeds isometrically as
a CLOSED subspace of the given positive-time raw H_W; W below is the GIVEN
isonormal process restricted to H. This is not physical multiplication of
raw H_W elements by 1_I, and disjoint time supports are not independent.

Here and below B for rough products is a physical integral only after
absolute convergence is established. Choose Borel representatives. For
Lebesgue-null N, both x in N and x-y in N have dx Gamma(dy) measure zero
by integrating first in x for each y. Representative changes therefore
do not change the resulting integrals; the same fact transfers a.e. limits.

Direct OWN accepted inputs, not recertified here:
A. all-dimensional-static-occupation-bridge.md Section4(11)-(16),
   scientific249e2c4/adoptionaa4a016: positive finite R_sp and, for real H1,
   the actual absolutely convergent signed form with bound

 |B(f1 f2,f3 f4)|<=R_sp product_j N(fj),
 N(f)=||f||2^(1-alpha/4)||grad f||2^(alpha/4).                 (1)

   The absolute-integral version of(1), physical PSD/CS and smooth density
   hold too. No d1 density split or global H1 supremum embedding is imported.
B. compact-sobolev-cutoff.md Proposition1/Sections2-3: multiplication by
   smooth compact eta is bounded H^s->H^s for every real s, and compact
   H^(sigma+gamma)->H^sigma for gamma>0. This is the full R^d result,
   with no periodic STATE replacement. We use sigma=s,gamma=1/2-s and
   sigma=-1/2,gamma=1 below, with the exact stated domains.
C. actual-operator-driver.md and source-operator-convergence.md Theorem1:
   GIVEN-W linear Gaussian first drivers, literal completed noise matrix
   forms, Gaussian variance-contraction transfer/basis independence and
   compact-valued Holder paths. fixed-mask-young-constant-phase.md supplies
   the EXACT F extension, free group S_F and ordinary multiplier B(V).
   raw-block-event-lower.md Sections2-4 supplies the literal test pullback
   and its same-noise covariance calculation, not a uniform tail in delta.
   The upstream ground/moment/variance proofs are not re-audited here.

Fix a real even eta_R in C_c^infinity,0<=eta_R<=1, equal1 on B_R and
supported in the closed B_(2R). The PHYSICAL driver mask is m_R=eta_R².
Every call to an accepted theorem takes ITS mask argument equal to m_R;
the root eta_R is only a state-factorization device. It is never squared
again as a noise mask. R is fixed throughout the positive result.

The claims proved below are compact T_sp:H_sp->K(F), compact
T:H->L^r(I;K(F)) for2<r<2/a, and an averaged Cameron-operator bound for
actual residual block drivers. K(F) always has the OPERATOR norm. No
instantaneous Gaussian field or new SPDE upper is a claim.

## 2. Spatial fractional products and their physical meaning

First, products fg of H1 functions are genuine H_sp elements. Approximate
f,g by compact smooth functions in H1. By(1), polarization and covariance
PSD, their products are Cauchy in H_sp, independent of the approximation;
for example ||uv||H_sp<=sqrt(R_sp)N(u)N(v) and expand a product difference.
The physical H1 four-linear continuity in A identifies the limiting norm
and pairings with B(fg,hk). PSD for products follows from fg=((f+g)²-
(f-g)²)/4 and smooth signed covariance PSD, followed by these limits.

Fix alpha/4<s<1/2. Use REAL RADIAL orthogonal Fourier bands D0=1_(|xi|<1)
and Dj=1_(2^(j-1)<=|xi|<2^j),j>=1. Sharp bands suffice: only Parseval and
frequency support are used, not any Lp multiplier theorem. For f in H^s,
f_j=Dj f is real and belongs to H1. The low block is explicitly included.
Frequency support gives

 N(f_j)<=2^(j alpha/4)||f_j||2,
 sum_j N(f_j)<=C_s ||f||H^s,                                 (2)

where weighted Cauchy-Schwarz uses the summable series
sum_j 2^(-2j(s-alpha/4)). The weighted l2 sum is bounded by the H^s norm
up to a fixed low-band constant. Also sum_j||f_j||2<infinity because s>0.
Thus sum_j|f_j| belongs to L2 by Minkowski/monotone convergence and the
series is absolutely convergent Lebesgue-a.e., with sum f.

For four H^s inputs, apply the ABSOLUTE form(1) to each band quadruple.
The sum of all those absolute two-point integrals is bounded by
R_sp product_j(sum_k N((fj)_k)), finite by(2). Tonelli and the null-set
observation after(1) therefore identify the actual product expansion at
both spatial positions with its absolutely convergent integral. We get

 int |f1(x)f2(x)f3(x-y)f4(x-y)|dx Gamma(dy)
                 <=C_s^4 R_sp product_j||fj||H^s.            (3)

This proves absolute physical convergence, representative independence
and joint four-linear continuity on H^s, without a Fatou-only equality.
The double series sum_(j,k) f_j g_k also converges absolutely in H_sp by
(1)-(2). Its partial sums are products of H1 functions. Their physical
norm identity passes by the absolute quadruple calculation just made.
Consequently

 ||fg||H_sp<=C_s²sqrt(R_sp)||f||H^s||g||H^s,                  (4)

with all physical product pairings in(3) equal to H_sp inner products.
Density of compact smooth functions in H^s can be checked by Schwartz
Fourier approximation, then compact cutoff approximation of each Schwartz
function in H1 and hence H^s. It follows that (4) is the unique bilinear
extension of the smooth product. This proves the fractional part of C1.

## 3. Compact spatial deterministic mean map on the EXACT F

For q smooth compact, Gamma*q is smooth locally: on each compact x set,
all y in its convolution integral remain in one compact set, of finite
Gamma mass, and derivatives fall on q. Thus V_q=m_R(Gamma*q) is real
smooth compact. Define T_sp q=iB(V_q) on F, where
 B(V)(z1,z2,c1,c2)=(0,V(z1+c1)) in E.
For w=(w1,w2,d1,d2) let w'=Lambda^-1 w2 in H1/2. The E velocity inner
product has weight Lambda^-1, so direct Fubini on smooth states gives

 <T_sp q z,w>F=<q,k(z,w)>H_sp,
 k(z,w)=(eta_R z1+c1 eta_R)(eta_R w').                        (5)

Evenness of Gamma converts the physical B(k,q) into B(q,k) in(5).
The same identity holds for all z,w in F by density and bounded smooth
multiplication. Its physical integral is well defined: the localized state
products are L1, Gamma*q is bounded on this fixed compact set, and L2
state approximation gives convergence there. Equation(4) supplies the
H_sp convergence. This argument does not multiply q in the noise quotient.

The two factor families in(5), with ||z||F,||w||F<=1, are precompact in
H^s by B with sigma=s,gamma=1/2-s. The added c1 eta_R family is finite
dimensional and compact. Their closures are compact, so their product
family has compact closure L in H_sp by(4). It is bounded, and (5) gives
||T_sp q||op<=sup_(k in L)||k||H_sp ||q||H_sp. Hence T_sp extends to the
raw quotient completion; a zero covariance class has zero operator image.
Both constants were included in F. The second constant column is zero
for the INSTANT multiplier and becomes nonzero after S_F in Section7.

For smooth q the E multiplication H1/2->H-1/2 is compact by B with
sigma=-1/2,gamma=1, and its extra c1 column is finite rank. Therefore
T_sp q belongs to K(F). Its bounded extension takes values there since
compact operators are closed in operator norm.

To prove compactness of the MAP, choose finite projections Q_n onto a
complete smooth-test ONbasis in H_sp (zeros omitted in Gram-Schmidt).
Such a basis exists by countable smooth-test density on compact sets;
finite combinations remain smooth compact. Equation(5) and self-adjoint
Q_n give
 ||T_sp(I-Q_n)||<=sup_(k in L)||(I-Q_n)k||H_sp ->0.            (6)
The convergence is uniform on compact L: use a finite epsilon net and
||I-Q_n||<=1, then strong convergence at each net point. T_sp Q_n has
finite-dimensional range in K(F); its norm limit is compact. Thus T_sp
is compact as H_sp->K(F), not merely pointwise compact-valued. K(F) is
separable, using finite-rank rational matrices in a real Hilbert basis.
This proves the remaining assertions of C1.

## 4. Actual tensor identification and supported projections

On separated smooth tests the raw spacetime covariance is exactly the
product H_t/H_sp inner product, by absolute Fubini. Finite sums therefore
identify isometrically with the algebraic Hilbert tensor product, after
both null quotients. They are dense in H: approximate a compact spacetime
test uniformly by smooth time partitions of unity times its spatial slices,
with one common compact support inside I x R^d. Uniform errors e on a
fixed spatial compact A have raw squared norm at most
 e² |A| Gamma(A-A) int_I int_I |s-t|^-a dsdt.
This is finite; temporal/spatial smooth partitions keep all supports legal.
Thus H=H_t tensor H_sp canonically, without a noise-density representation.

The same compact-support bound and countable smooth approximation give
separability and a countable dense list of smooth tests in H. Gram-Schmidt,
skipping zero classes, produces a complete ONbasis e_j supported INSIDE
I x R^d. Define P_J as projection onto its first J vectors. On H_W use
the same finite formula sum_j<J <.,e_j>e_j; it is an orthogonal projection
there too. This is not a raw time-indicator multiplier or independence of
time intervals. The residual is Q_J=I-P_J. The original W is retained.

## 5. Scalar time covariance: compact mean map without trace class

Let K act on L2(I) by Kf(s)=int_I |s-t|^-a f(t)dt. Schur gives a finite
operator norm because the row/column integrals are <=2/(1-a). The operator
is real self-adjoint and positive. One direct positivity/injectivity check
is the Gamma representation, valid off the time diagonal,
 |v|^-a=Gamma_E(a)^(-1)int_0^infinity e^(-lambda|v|)lambda^(a-1)dlambda.
For f in L2(I), extend by0. Schur bounds int K|f(s)f(t)|, so absolute
Fubini applies. Plancherel and the elementary Fourier integral for
exp(-lambda|v|) show its quadratic form is
 int_R 2lambda/(lambda²+xi²)|hat f(xi)|² dxi>0
when f!=0 and lambda>0. Integrating in lambda proves strict positivity of
K. No trace-class Gaussian field or density is being introduced.

The deterministic kernel K_epsilon=K 1_(|s-t|>=epsilon) is square integrable
on I², hence its integral operator is compact (approximate its L2 kernel
by finite sums of separated functions). It need not be PSD and is NOT
used as a Gaussian covariance. The Schur bound on K-K_epsilon is
2epsilon^(1-a)/(1-a), tending to0. Thus K is compact positive, and its
positive square root is compact by the compact self-adjoint spectral theorem.

On smooth tests the map iota:f->K^1/2 f has L2 norm exactly ||f||H_t.
It extends isometrically to H_t, onto closure(Ran K^1/2)=L2(I), since
smooth tests are L2 dense and ker K=0. The actual mean map on tests Kf
therefore extends to

                  C_t=K^1/2 iota:H_t->L2(I),                 (7)

which is compact. This is a deterministic covariance-Hilbert construction,
not identification of a raw L2-valued Gaussian variable.

Fix2<r<2/a and r'=r/(r-1). Extend the kernel by0 outside[-1,1]. It lies
in L^(r/2)(R). Scalar Young convolution gives for smooth test g
 ||g||H_t²<=||K_a||L^(r/2)||g||L^r'².                        (8)
For completeness the Young inequality here needs no external result:
for exponents u,v<r with1/u+1/v=1+1/r, split f(y)h(x-y) into the factors
(f^u h^v)^(1/r), f^(1-u/r), h^(1-v/r). Holder exponents r,
1/(1/u-1/r),1/(1/v-1/r), followed by integration in x and Tonelli, give
||f*h||r<=||f||u||h||v. Apply this to absolute functions with u=r/2,v=r'.
All exponents are finite and positive because r>2.

Covariance CS, (8) and ordinary Lr duality yield, initially for smooth f,
 ||Kf||Lr=sup_(smooth g,||g||r'<=1)|<f,g>H_t|
                  <=C_(a,r)||f||H_t.                        (9)
The tests Kf are bounded by the L1 kernel bound, so their Lr norms and
the stated duality are legitimate before completion. Density extends(9),
and its L2 value coincides with(7). Pick r2 with r<r2<2/a. Boundedness
into L^r2 and compactness into L2 imply compactness into Lr: choose
0<t<1 with1/r=t/2+(1-t)/r2 and use
||u||r<=||u||2^t||u||r2^(1-t) on differences of a bounded image sequence.
Thus C_t:H_t->Lr is compact, for every claimed r.

This cannot be strengthened to a trace-class assertion. The normalized
indicators N^1/2 1_((j/N,(j+1)/N)) are orthonormal in L2. Their K quadratic
forms sum to C_a N^a, C_a=2/((1-a)(2-a)), by integrating on each cell.
Since this diverges, positive K has infinite trace. The map(7) is not
Hilbert-Schmidt. There is no raw instantaneous L2 Gaussian in this argument.

## 6. Hilbert-valued bound and the COMPACT time-space mean map

For a finite tensor Psi=sum_j f_j tensor q_j, with orthonormal q_j in H_sp
and smooth f_j, define the RAW spatial-label field
 U(Psi)(s)=sum_j (Kf_j)(s)q_j.
It is strongly measurable and finite-dimensional. For a test vector field
g(s)=sum_j g_j(s)q_j, scalar Young and positivity of the time kernel give
 ||g||_(H_t tensor H_sp)²
   <=int int K_a(s,t)||g(s)||H_sp||g(t)||H_sp dsdt
   <=C_(a,r)² ||g||L^r'(H_sp)².
Hilbert CS and finite-dimensional Lr duality therefore give

             ||U(Psi)||Lr(H_sp)<=C_(a,r)||Psi||H.             (10)

There is NO dimension-dependent factor. The duality can be checked directly
by choosing the pointwise direction ||U||^(r-2)U and normalizing; all fields
here lie in a finite-dimensional subspace. Approximate its coefficients by
smooth tests in Lr', using(8). Thus no infinite-dimensional Pettis or RNP
assumption has been slipped in. Finite tensors are H dense, so(10) extends
to a strongly measurable Bochner Lr(H_sp) field by completeness. The
spatial covariance has NOT yet been applied by this time-only map.

Define T Psi(s)=T_sp(U(Psi)(s)). It is a bounded map H->Lr(I;K(F)). For
separated smooth tests, (5) identifies it with the ACTUAL mean multiplier
 iB(m_R h_Psi(s)), h_Psi=K_a Gamma*Psi.
For a general smooth compact spacetime test, the separated approximants
of Section4 also identify this physical mean: their uniform errors on one
compact support give a uniformly small m_R h-error, because K_a has a
uniform finite row integral and Gamma has finite mass on the relevant
compact spatial differences. B(V)'s accepted bound by ||V||infinity+||V||2
therefore gives uniform-in-time operator convergence on this fixed mask.
It coincides with the Lr limit defining T. For arbitrary H controls the
notation means only the unique completed operator field, not a pointwise
potential function or instantaneous random field.

It is compact. Indeed, (6) gives ||T_sp(I-Q_n)||->0. The maps
T_n Psi=T_sp Q_n U(Psi) approximate T in operator norm by(10). For fixed n,
write the finite Q_n field in its orthonormal spatial coordinates. Each
coordinate extraction H->H_t has norm<=1, and C_t:H_t->Lr is compact.
The n coordinate images form a precompact product; their finite linear
combination with the fixed compact operators T_sp q_j is precompact in
Lr(K(F)). Thus T_n is compact, and so is its norm limit T. This step uses
SPATIAL compactness; scalar time compactness tensor an infinite identity
would not suffice. This proves C2.

For the supported raw projections P_J of Section4, put

                 epsilon_J=||T(I-P_J)||H->Lr(K(F)).          (11)

It tends to0. To verify this without assuming norm convergence of P_J,
suppose unit v_J have ||T(I-P_J)v_J|| bounded below. The vectors
u_J=(I-P_J)v_J tend weakly to0, since for every fixed h,
|<u_J,h>|<=||(I-P_J)h||->0. Compact T gives a norm-convergent subsequence
of T u_J; every continuous linear observable has weak limit0, so its norm
limit is0, a contradiction. This establishes the needed operator-norm tail.

## 7. Actual residual drivers and completed Cameron identity

Fix integer B>=1 and0<delta<min(1,1/B). Put N=floor(1/(delta B)),
s_m=m delta B, ell_m=B for m<N and ell_N=1/delta-NB in[0,B).
The intervals I_m=[s_m,s_m+delta ell_m] partition[0,1] up to endpoints.
The last interval may be empty. Define the literal test pullback
 T_(delta,m)f(s,x)=delta^(a/2-1)f((s-s_m)/delta,x)
with zero extension. It is an isometry on the full positive-time raw test
completion: the covariance factors are delta^(a-2)delta²delta^-a=1.
Use the extended P_J on H_W from Section4 and define the ACTUAL Gaussian
linear noise on fast tests by

 Y_(m,J)(f)=W((I-P_J)T_(delta,m)f), g_delta=delta^((1-a)/2).

It has covariance bounded by the original raw test norm. Apply accepted
Gaussian transfer C, with its mask argument m_R, then its genuine F
extension, to get X_(m,J)=g_delta A_(m_R)(Y_(m,J)). Observe it only on
[0,ell_m] and extend its INTERACTION primitive constantly to[0,B].
For ell_m=0 this is the zero path. Transfer and stopping preserve compact
values and Cbeta bounds. With theta<beta in the accepted driver range,
these are actual centered Gaussian paths in the separable little-Holder
space B0=h0theta([0,B];K(F)). The joint law is coupled on the GIVEN W,
not an independent noise replacement.

Every completed literal row test up to ell_m belongs to the closed H_I:
its slow time support is within[0,1], and endpoint indicators are approximated
inside I by smooth time cutoffs in the raw covariance norm. This follows
by dominated convergence against integrable K_a and locally finite Gamma
on the compact spatial kernel support, as in the accepted source note.
Schwartz E states plus BOTH true constant columns suffice, then density
in F. Consequently the row first chaos, and hence the separable Gaussian
path itself, uses W(H_I). Equivalently, Gaussian transfer after the
orthogonal projection onto H_I leaves every observed row unchanged;
countable dense states/times identify the same path built from W(H_I).
No time-support independence is asserted.

For Phi smooth supported in I x R^d, (I-P_J)Phi is another such smooth
test. Direct covariance and the pullback give
 E[Y_(m,J)(f)W(Phi)]
   =delta^(a/2)int f(v,x)h_((I-P_J)Phi)(s_m+delta v,x)dv dx.
This is the exact same-W formula of the accepted raw-block calculation;
absolute Fubini allows signed tests too (or decompose a compact signed
test into two nonnegative smooth tests). Multiplying by g_delta gives
sqrt(delta), not a fractional-Brownian normalization. The literal F matrix
forms and(5) therefore identify the path covariance with

 L_(delta,J)Phi_m(u)=sqrt(delta)int_0^min(u,ell_m)
       S_F(-v) T((I-P_J)Phi)(s_m+delta v) S_F(v)dv.            (12)

Both constant columns are present: S_F(v) changes the constant velocity
column's displacement to v, while the constant displacement remains1.
A compact mean is multiplied AFTER convolution; no raw noise quotient
mask multiplier or commutation of mask/free group is used.

We justify the operator integral, regularity and complete extension. On
the Hilbert F, both S_F and its adjoint are strongly continuous. For E
this follows in Bessel-unitary coordinates from the Fourier matrix
 [cos(v|xi|), <xi>sin(v|xi|)/|xi|;
  -|xi|sin(v|xi|)/<xi>, cos(v|xi|)],
with the continuous value at xi0. The matrix and its adjoint have common
bounds C(1+B) on[-B,B] and pointwise continuous entries, so dominated
convergence applies; the constant triangular2x2 block is
finite-dimensional. For compact A, v->S_F(-v)AS_F(v) is OPERATOR-norm
continuous: strong convergence is uniform on compact images, and the
right factor follows by taking adjoints. Joint norm continuity in(v,A)
and local uniform bounds give Bochner measurability for any strongly
measurable K(F)-valued field, with Lr bound after this conjugation.
No operator-norm time continuity of S_F itself is assumed.

Let G_B=sup_(|v|<=B)||S_F(v)||. For M=T(I-P_J)Phi in Lr(I;K(F)),
Holder in v and the primitive increment estimate give

 ||L_(delta,J)Phi_m||Ctheta
 <=sqrt(delta) C_B delta^(-1/r)||M||Lr(I_m),
 C_B=G_B²[B^(1-1/r)+B^(1-1/r-theta)].                        (13)

Here choose1/2<theta<min(1-a/2,(3-a-alpha)/2),
1/(1-theta)<r<2/a and1/theta<=p<2. These intervals are nonempty and p<r.
The primitive has Holder exponent1-1/r>theta. Simple K(F)-valued integrand
approximation in Lr shows its primitive lies in B0; constant extension of
a stopped path does not increase its Holder norm. The affine pullback
preserves null sets, so(12) is independent of the Lr field representative.

For fixed delta,J the covariance map Phi->E[(X_(m,J))_m W(Phi)] is bounded
H->the finite product of B0 spaces by Bochner CS and L2 path moments.
The right side(12) is also bounded by(13). Equality on smooth Phi extends
by density to all H. Initial equality of matrix forms extends from dense
F states and rational times to full operator paths by continuity; norm
Borel coordinates use dense UNIT combinations, not largest matrix entries.
Thus(12) is the ACTUAL completed Cameron covariance operator of the given
residual Gaussian tuple. More explicitly, every continuous linear
statistic l(X) is W(k_l) with k_l in H, by Gaussian transfer and the
H_I-supported matrix kernels. Let H_seen be the closed span of these k_l.
Then l(L Phi)=<k_l,Phi>, so ker L=H_seen^perp. The first-chaos definition
of Gaussian Cameron directions gives L(H_seen) with norm ||Phi||H;
extra raw directions are quotiented by orthogonal projection onto H_seen.
Thus the following raw-H operator norm bound is also the actual Cameron
embedding norm bound. No inverse covariance or new noise law is needed.

## 8. Exact averaged norm, finite kernel reuse and uniform delta bound

Define the norm EXACTLY by
 ||x||_(delta,p)=(delta sum_(m=0..N)||x_m||Ctheta^p)^(1/p).     (14)
It is delta-weighted, not delta B-weighted; B stays explicit in the constant.
For t_m=||M||Lr(I_m)>=0, the existing pinned Mathlib
Real.rpow_sum_le_const_mul_sum_rpow_of_nonneg applies on the n=N+1
indices (n cast to real in powers) with exponent kappa_f=r/p>1 and nonnegative values f_m=t_m^p.
Its COMPLETE public type is supplied, not a new local theorem. It yields
 (sum t_m^p)^(r/p)<=n^(r/p-1)sum t_m^r.
The real-power identity holds for t_m>=0 and positive exponents, including
zero terms. Raising to1/r>0 gives the precise finite Holder estimate
 (sum t_m^p)^(1/p)<=n^(1/p-1/r)(sum t_m^r)^(1/r).
There is no empty-set ambiguity because N>=1. From delta B<1,
n<=2/(delta B); the exponent1/p-1/r is positive. Therefore(13)-(14) give

 ||L_(delta,J)Phi||_(delta,p)
 <=sqrt(delta) C_B (delta n)^(1/p-1/r)||M||Lr(I)
 <=sqrt(delta) C_B (2/B)^(1/p-1/r)epsilon_J||Phi||H.           (15)

All intervals, including the true final remainder, are accounted for by
sum t_m^r=||M||Lr(I)^r. This proves C3, with epsilon_J->0 independent of
delta. R enters through T and epsilon_J; B/theta/r/p constants are stated.
The finite kernel fact verifies only its exact power-mean implication;
C1-C3's functional-analytic and stochastic identification steps are ANALYTIC.
No Gaussian concentration, nonlinear Young-product or moment upper follows
from(15) alone.

## 9. Fixed radius is essential; scope and verification boundary

Here is a precise negative guard against an automatic growing-mask upgrade.
Take the admissible d1 white Gamma=delta0,alpha1, any0<a<1. From the ACCEPTED
scalar equilibrium identity/mass in damped-lower-endpoint-bridge.md Section2,
f_a in L2(I), K_a*f_a=1 and ||f_a||H_t²=M_a>0. Its H_t membership follows
by smooth L2 approximation and the Schur norm bound. Let q be a nonnegative
unit-L2 compact smooth bump and q_n(x)=q(x-x_n), centers escaping to infinity.
The raw H unit direction Phi_n=f_a tensor q_n/sqrt(M_a) has actual mean
q_n/sqrt(M_a), constant in time. This follows either directly from the
scalar identity or from the L2/mean completion in Sections5-6.

Fix J. The finitely many smooth compact basis tests spanning P_J have a
common compact spatial support. Choose x_n outside that support by more
than the radius of q. White spatial covariance gives P_J Phi_n=0 exactly,
regardless of temporal correlation. Choose R_n large enough that m_(R_n)=1
on supp q_n. Use F input e_disp=(0,0,1,0) in this section's four-entry
notation, norm1, and output dual w_n=(0,Lambda q_n/||q||H1/2,0,0), norm1.
The completed multiplier has the constant-in-time coordinate

 <T_(R_n)Phi_n(s)e_disp,w_n>F=1/[sqrt(M_a)||q||H1/2]>0.       (16)

Indeed the E velocity inner product has weight Lambda^-1, and q_n is unit
L2 with translation-invariant H1/2 norm. Thus for every fixed J,
 sup_R ||T_R(I-P_J)||H->Lr(K(F))>=1/[sqrt(M_a)||q||H1/2].
There is NO projection-tail convergence uniform in R for this fixed family.
This refutes ONLY that proposed extension, not fixed-R C1-C3, not all
projection/localization strategies and not the original sharp-upper goal.
For fixed R, sufficiently far white-noise q_n misses its mask. The negative
guard uses a bounded phase functional, no Sobolev point trace. It is the
exact control proposed separately in globalization-guard-v0.md.

All C1-C3 and this negative guard remain ANALYTIC. The existing Mathlib
finite power-mean type and standard axioms were checked at the established
pin; actual substitution/guards above require full independent application
review. No new local theorem, module, count, package or companion follows.
73facts19seams/L0 PROPOSED unchanged, no new kernel or donor build.

Controls in operator-cm-controls-v1.json are root consistency evidence,
not a proof:24selected F-coordinate rows include8trivial zero horizons,
and the missing-fast-velocity and wrong-Jacobian cases share one delta
ratio for column1, not independent negative tests. Selected spatial
frequency entries are LOWER witnesses for an operator norm, not its upper
evaluation. Gaussian profiles are whole-space H1 controls; compact rows
are separately specified. Quadrature differences are not certified error.
No full operator/Ctheta norm, projection tail or solution moment was sampled.

Friz-Hairer primary Theorems11.6/11.7 and Example11.8 were recon-read for
FUTURE concentration on an existing Gaussian Banach law. They are not
premises for spatial/time compactness or a trace-class raw-field claim.
No concentration, exponential residual estimate, nonlinear Young-product
upper, growing-cone original POINT upper or source-constant identity has
been proved here. Fixed-mask F3 cannot be reversed. Self-pairings and
unequal/empty Stratonovich chains remain part of the original objective.

The reviewed full correct-scale upper and strong own-energy lower remain
unchanged. Matching sharp upper, intended source-domain/normalization and
conditional exact limit, manuscript/wiki integration, whole-paper/novelty/
cold-reader/circulation gates remain OPEN. No contact/Skorohod/source repair/
HPC/TeX/PDF/wiki/bib/privatecompanion/publication. Full original goal ACTIVE.
