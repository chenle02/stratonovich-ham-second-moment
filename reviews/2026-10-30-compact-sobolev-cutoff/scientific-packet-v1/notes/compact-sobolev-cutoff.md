# Whole-space compact Sobolev cutoffs and finite Gaussian operator sums

COMPLETE CANDIDATE, not adopted before independent full proof review.
The spatial state stays on R^d. A periodic box is used only to factor a
compactly supported multiplication operator, with exact recovery below.
This note constructs no actual source family, infinite Gaussian series,
time path, Young flow or new moment asymptotic.

## 1. Conventions and statements

Let d in {1,2,3}, Lambda=(1-Delta)^(1/2), and <xi>=sqrt(1+|xi|^2).
Use unitary Fourier transform hat f=c_d int exp(-i xi.x)f(x)dx,
c_d=(2pi)^(-d/2). H^r(R^d) has norm ||<xi>^r hat f||2, for every real r.
Lambda is the Bessel norm multiplier; the underlying wave remains massless.

Let chi be a REAL compact smooth function, sigma real, gamma>0. Initially
on Schwartz inputs put

    K_(sigma,gamma)=Lambda^sigma chi Lambda^(-sigma-gamma).          (1)

Singular values are indexed j>=1 in decreasing order, with multiplicity
and zeros, with UNNORMALIZED Schatten norm ||K||_Sp^p=sum_j s_j(K)^p.
We use elementary compact Hilbert spectral theory for singular values;
the approximation and order facts required below are proved explicitly.

**Proposition 1.** (1) extends uniquely to a compact L2(R^d) operator and

    s_j(K_(sigma,gamma)) <= C_(chi,sigma,gamma,d) j^(-gamma/d).       (2)

Consequently K belongs to S_p for every p>=1 with p gamma>d. No uniform
support-radius or endpoint Schatten assertion is made. Zero chi is trivial.

For the physical phase E=H^(1/2)xH^(-1/2), use unitary physical coordinates
J0(u,v)=(Lambda^(1/2)u,Lambda^(-1/2)v) in H=L2(R^d;C^2).
The frequency J of the accepted actual-variance note is (F directsum F)J0,
so this is a unitary change of coordinates. Let Dchi multiply both phase
entries, and set

 Pchi=J0 Dchi J0^-1,
 D_gamma=diag(Lambda^-gamma,Lambda^-gamma),
 Kout=Pchi D_gamma,        Kin=Pchi* D_gamma.                        (3)

**Proposition 2.** Pchi is bounded. If U(v,w)=(w,v), then Pchi*=U Pchi U,
Kin=U Kout U, and Kout,Kin are compact. For p>=1,p gamma>d they have equal
S_p norms. For p>=2 define

 B_out=Pchi D_gamma^2 Pchi*=Kout Kout*,
 B_in =Pchi* D_gamma^2 Pchi=Kin Kin*.

Then both are positive compact and

 Tr B_out^(p/2)=Tr B_in^(p/2)=||Kout||_Sp^p.                         (4)

Pchi is not assumed selfadjoint or a projection.

**Proposition 3.** Suppose a finite family of bounded operators Z_l on H
satisfies

 Pchi Z_l=Z_l=Z_l Pchi,
 Vout=sum_l Z_l Z_l* <= C D_gamma^2,
 Vin =sum_l Z_l* Z_l <= C D_gamma^2, C>=0.                           (5)

For p>=2,p gamma>d, every Z_l is compact in S_p, Vout,Vin are positive
compact in S_(p/2), and

 Vout<=C B_out, Vin<=C B_in,
 Tr Vout^(p/2), Tr Vin^(p/2) <=C^(p/2)||Kout||_Sp^p.                 (6)

These are explicit operator hypotheses; no actual source family is
postulated to satisfy them. Section7 gives a nonzero whole-space witness
when chi has a plateau, as the physical observation cutoffs do.

**Corollary 4.** For even p=2m>=2 with p gamma>d and real independent
standard Gaussians g_l, the FINITE sum X=sum_l g_l Z_l in (5) satisfies

    (E||X||_Sp^p)^(1/p) <=sqrt(p-1) sqrt(C)||Kout||_Sp.             (7)

The norm can initially be extended infinity. The proof establishes a
measurable extended norm and its finite expectation. No Sp-Bochner limit
or infinite Gaussian series is assumed. The only imported research input
is the OWN accepted finite MATRIX result, finite-gaussian-schatten.md,
Theorem1, with exactly these real Gaussians, complex matrices and even p.

## 2. Weighted mixed Schur estimates and the auxiliary Fourier maps

For x,y in R^d,

 <x><=sqrt(2)<y><x-y>,
 (<x>/<y>)^r<=2^(|r|/2)<x-y>^|r| for every real r.                  (8)

The first follows from |x|^2<=2|y|^2+2|x-y|^2. For r>=0 raise it to r;
for r<0 use its reversed x,y version. Thus negative indices are included.
The Fourier transform of any compact smooth cutoff decays faster than
any power, by integration by parts. Therefore
<z>^|r| |hat phi(z)| is nonnegative, integrable and rapidly decreasing
for every real r. Smoothness of its absolute value at zeros is not needed.

For lattice aZ^d, a>0, and N>d,

    sup_y sum_(k in Z^d) <y-a k>^-N <infinity.                     (9)

Translate y modulo the lattice into a centered fundamental cell. Its norm
is at most a sqrt(d)/2. For |k|>=sqrt(d), |y-a k|>=a|k|/2, giving a
constant times <k>^-N; the remaining k are finite. The latter series
converges: dyadic lattice shells have at most C_d 2^(jd) points and their
terms are at most 2^(-jN). This proves (9), with constants allowed to
depend on a,d,N. It also bounds uniformly lattice sums of any rapidly
decreasing function translated by y.

The mixed Schur estimate used here is elementary. If an integral kernel
from L2(mu) to L2(nu) has absolute row integrals bounded by M1 and absolute
column integrals bounded by M2, weighted Cauchy-Schwarz at each output
point, followed by nonnegative Tonelli, gives operator norm at most
sqrt(M1 M2). This applies when one measure is counting and the other is
Lebesgue, and also when both are Lebesgue. It first defines the operator
on finitely supported or compact test inputs and then extends by density.

Choose a cube Q_L=(-L/2,L/2)^d containing supp chi in its interior, and
real psi compact smooth in Q_L, equal1 on a neighborhood of supp chi.
Such choices exist by the compactness of supp chi and ordinary smooth
cutoffs. On the auxiliary torus T_L use L2(Q_L,dx), with orthonormal basis

 e_k(x)=L^(-d/2)exp(i kappa_k.x), kappa_k=2pi k/L,
 ||v||_H^r(T_L)^2=sum_k <kappa_k>^(2r)|v_k|^2.                      (10)

Initially let Ppsi u be periodization of psi u for u Schwartz. Its k-th
coefficient is

 (Ppsi u)_k=L^(-d/2)int psi(x)u(x)exp(-i kappa_k.x)dx
           =L^(-d/2)int psihat(kappa_k-xi)hat u(xi)dxi.             (11)

Inserting unitary Fourier inversion for u gives this constant: c_d from
inversion cancels c_d^-1 from the ordinary Fourier integral of psi.
After the Bessel normalizations, the kernel is exactly

 L^(-d/2)(<kappa_k>/<xi>)^r psihat(kappa_k-xi).                     (12)

For a finite torus polynomial v, put Echi v=chi times its periodic
extension on R^d. Its normalized Fourier kernel is exactly

 L^(-d/2)(<xi>/<kappa_k>)^r chihat(xi-kappa_k).                     (13)

Indeed each e_k contributes L^(-d/2)chihat(xi-kappa_k); there is no extra
c_d. Equations(8)-(9) bound both row/column quantities of (12) and (13):
one is the L1 integral of a rapidly decreasing function, and the other
is its uniformly translated lattice sum. Mixed Schur therefore proves,
for EVERY real r,

 Ppsi:H^r(R^d)->H^r(T_L),       Echi:H^r(T_L)->H^r(R^d)             (14)

bounded. All constants can depend on the fixed cube and cutoffs.

Schwartz functions are dense in H^r(R^d), by smooth compact approximation
of the weighted Fourier L2 function; torus polynomials are dense by their
weighted sequence truncations. Thus (14) defines the unique extensions,
including negative r. Their distributional meaning agrees with the initial
formulas: each Fourier coefficient pairs the distribution with a compact
smooth function, and multiplication/periodic extension is checked against
compact test functions by density. No pointwise sampling of a rough
Fourier function is asserted; (11) samples the SMOOTH product psi u through
its bounded kernel extension. The same full-Lebesgue Schur estimate and
(8) prove multiplication by a compact smooth function bounded on every
H^r(R^d), a fact also used in the density argument.

## 3. Exact whole-space recovery and singular-value decay

Let I_gamma:H^(sigma+gamma)(T_L)->H^sigma(T_L) be the identity inclusion.
For a Schwartz u, Ppsi u is the smooth periodic function psi u on Q_L.
Since chi is interior to this cube and chi psi=chi,

    Echi I_gamma Ppsi u=chi u.                                    (15)

There is no alias contribution on supp chi. The periodic Fourier series
converges smoothly here because psi u is compact smooth. Both sides of
(15) are bounded from H^(sigma+gamma)(R^d) to H^sigma(R^d): use (14),
the inclusion, global H^(sigma+gamma)->H^sigma and smooth multiplication.
Density extends (15) to that FULL whole-space Sobolev domain, including
negative indices. Consequently

 K_(sigma,gamma)=Lambda^sigma Echi I_gamma Ppsi Lambda^(-sigma-gamma).
                                                                    (16)

In the weighted coefficient coordinates of (10), I_gamma is diagonal
with entries delta_k=<kappa_k>^-gamma. Let Q_n retain |k|infinity<=n;
its rank is (2n+1)^d, and

 ||(1-Q_n)I_gamma||<= [1+(2pi/L)^2(n+1)^2]^(-gamma/2)->0.            (17)

Replacing I_gamma by Q_n I_gamma in(16) gives finite-rank K_n converging
in operator norm. A norm limit of finite-rank operators is compact:
finite-rank images of the unit ball have finite epsilon nets, and a
uniform norm approximation transfers such a net to the limiting image.

Write M=||Echi:H^sigma(T_L)->H^sigma(R^d)||
       *||Ppsi:H^(sigma+gamma)(R^d)->H^(sigma+gamma)(T_L)||.
The outer Bessel maps in (16) are unitary. For j>=3^d choose
n=floor(j^(1/d)/4). Then

 (2n+1)^d <=(j^(1/d)/2+1)^d<j,
 ||K-K_n|| <=M (2L/pi)^gamma j^(-gamma/d).                          (18)

The first strict inequality uses j^(1/d)>=3. The second follows from
n+1>j^(1/d)/4 and(17). For a compact K, any rank<j approximation F gives
s_j(K)<=||K-F||: in the span of its first j right singular vectors there
is a unit vector in ker F, and K has norm at least s_j on that vector.
The zero-singular-value case is immediate. Applying this to (18), and
using ||K||<=M for j<3^d, proves(2), for example with

    C=M max(3^gamma,(2L/pi)^gamma).

Finally sum j^(-p gamma/d), finite by the integral test when p gamma>d.
This proves Proposition1. It establishes a whole-space cutoff estimate;
the torus diagonal was only a factor of (16).

## 4. The actual balanced adjoints and both compact envelopes

Put A_sigma=Lambda^sigma chi Lambda^-sigma on L2. Full-Lebesgue Schur
as in Section2 proves A_sigma bounded for every real sigma. On Schwartz
functions the Bessel powers are selfadjoint under L2 duality, and real
chi is selfadjoint multiplication. Hence A_sigma*=A_-sigma there.
Boundedness and density give the actual Hilbert adjoint on all L2.
No evenness of chi is needed; a non-even real chi has a complex Fourier
transform with the same conjugate-reflection identity.

The physical J0 coordinates give

 Pchi=diag(A_(1/2),A_(-1/2)),
 Pchi*=diag(A_(-1/2),A_(1/2))=U Pchi U.

Since U commutes with D_gamma, Kin=U Kout U. The two blocks of Kout are
K_(1/2,gamma) and K_(-1/2,gamma), so Proposition1 proves compactness and
S_p membership. The spectrum of the squared absolute value of a block
diagonal compact operator is the union of its block spectra, giving

 ||Kout||_Sp^p=||K_(1/2,gamma)||_Sp^p+||K_(-1/2,gamma)||_Sp^p.

Unitary conjugation preserves singular values, so Kin has the same norm.
The nonzero eigenvalues of K K* and K* K coincide with multiplicity:
an eigenvector of K* K at positive lambda is carried by K/sqrt(lambda)
to one of K K*, and the inverse map is K*/sqrt(lambda). Zeros contribute
nothing. This proves positivity, compactness and(4), and Proposition2.

## 5. Compact positive order and localized variance envelopes

We spell out the positive-order fact without raising an operator
inequality to an unsupported power. Suppose 0<=A<=B and B is compact
positive on a Hilbert space. Let Q_n be the finite spectral projections
of B. Its spectral tails have norm tending to zero. With the usual bounded
positive square root of A,

 ||(1-Q_n)A^(1/2)||^2
   =||(1-Q_n)A(1-Q_n)||<=||(1-Q_n)B(1-Q_n)||->0.

Thus A^(1/2) is a norm limit of finite-rank Q_n A^(1/2), and A is compact.
The compact positive spectral minmax formula gives

    lambda_j(A)<=lambda_j(B), for every j.                         (19)

For clarity the formula is obtained in an eigenbasis: the span of the
first j eigenvectors gives the lower bound in the supremum over j-dimensional
subspaces of their minimum Rayleigh quotient; every such subspace meets
the orthogonal complement of the first j-1 eigenvectors, giving the upper
bound. Comparing Rayleigh quotients under A<=B proves (19). Therefore,
for any t>=1 with Tr B^t finite, Tr A^t<=Tr B^t by summing scalar powers
of the eigenvalues. This argument asserts no order A^t<=B^t.

Under(5), left localization gives Vout=Pchi Vout Pchi*. Positive
congruence applied to Vout<=C D_gamma^2 yields Vout<=C B_out.
Right localization similarly gives Vin=Pchi* Vin Pchi<=C B_in.
Use (19) and(4) with t=p/2 to obtain (6), including compactness and
S_(p/2) membership. If C=0 both variances and all Z_l vanish, so the
assertions are trivial.

For each l, Z_l Z_l*<=Vout. It is compact by the same order fact. If Q_n
are its spectral projections, ||(1-Q_n)Z_l||^2 equals the spectral tail
norm of Z_l Z_l*, so Z_l is a norm limit of finite-rank operators and
compact. Its singular values squared are the nonzero eigenvalues of
Z_l Z_l*. Applying (19) again and summing proves Z_l in S_p, with
||Z_l||_Sp^p<=Tr Vout^(p/2). This proves Proposition3.

## 6. Finite Gaussian sums on the actual Hilbert space

Choose finite-rank orthogonal projections Q_n converging STRONGLY to I
on H, from any fixed countable orthonormal basis. Set
Z_l,n=Q_n Z_l Q_n, acting on the finite-dimensional range of Q_n, and
X_n=sum g_l Z_l,n. Its output variance satisfies

 sum_l Q_n Z_l Q_n Z_l* Q_n <=Q_n Vout Q_n,                          (20)

because the difference is sum_l Q_n Z_l(1-Q_n)Z_l*Q_n>=0. The analogous
input inequality has V_in. Compact minmax also gives
lambda_j(Q_n V Q_n)<=lambda_j(V) for positive compact V: the Rayleigh
subspaces in range Q_n are a subset of all subspaces. Consequently the
trace powers of either variance in(20) are at most C^(p/2)||Kout||_Sp^p
by(6) and finite positive-order minmax.

Apply OWN accepted finite-gaussian-schatten.md Theorem1 to these finite
complex matrices, the SAME finite independent real Gaussians and even p.
Both variance trace powers have that common bound, so

    E||X_n||_Sp^p <= (p-1)^(p/2) C^(p/2)||Kout||_Sp^p.             (21)

The matrix theorem's average of the two trace powers does not add a
factor2; both were bounded before taking their average.

For every Gaussian coordinate vector, X=sum g_l Z_l is compact as a
finite sum of compact operators. Strong Q_n->I implies Q_n X Q_n->X
in OPERATOR norm for compact X: approximate X by a finite-rank F, use
uniform strong convergence on the finite-dimensional ranges of F and F*,
then the projection norm bound1 to control the remainder. Singular values
are norm-Lipschitz. Indeed the formula
s_j(A)=inf_(dimE<j) sup_(v in Eperp,||v||=1)||Av||, obtained from the
compact singular vectors, gives s_j(A)<=s_j(B)+||A-B||, and interchange
A,B for the reverse inequality. Thus s_j(X_n)->s_j(X) for every j.

For fixed outcome, scalar Fatou for the nonnegative j-sum gives
||X||_Sp^p<=liminf_n ||X_n||_Sp^p, with extended infinity allowed.
These quantities are measurable: the finite Gaussian coordinate map to
X is operator-norm continuous, each singular value is continuous, and
the norm power is their nonnegative measurable sum. A second scalar Fatou
in probability and(21) prove(7). In particular this extended norm is
finite almost surely. No assumed S_p-Bochner convergence or infinite-
series theorem entered this argument. Under C3, finite sums are also in
S_p by its usual vector-space property, but the proof did not need to
assume that membership in order to obtain the uniform moment estimate.
This proves Corollary4.

## 7. Whole-space nonzero witness and the missing-cutoff test

Nonzero witnesses to(5) are asserted only when chi has a plateau on an
open set. Choose nonzero real compact smooth v,f inside that plateau and
put vtilde=(Lambda^(1/2)v,0), wtilde=(Lambda^(-1/2)f,0), both Schwartz.
Then Pchi vtilde=vtilde and Pchi* wtilde=wtilde by the actual block
formulas. The rank-one Zx=<x,wtilde>vtilde therefore satisfies
Pchi Z=Z=ZPchi. Its two variances are
||wtilde||^2 vtilde tensor vtilde* and ||vtilde||^2 wtilde tensor wtilde*.
For any Schwartz a and arbitrary x in H,

 |<x,a>|=|<D_gamma x,D_gamma^-1 a>|
                 <=||D_gamma x|| ||D_gamma^-1 a||.

Since a is Schwartz, the inverse multiplier here lies in L2. Apply this
with a=vtilde,wtilde to obtain(5) with finite common constant
max(||wtilde||^2||D_gamma^-1 vtilde||^2,
    ||vtilde||^2||D_gamma^-1 wtilde||^2). This is a genuine nonzero
whole-space witness with the Sobolev adjoint covector. It does not identify
an actual Cameron-Martin/source family. Without a plateau such a witness
need not exist; C3 remains a conditional assertion, possibly trivial.

Conversely the uncut operator Lambda^-gamma on L2(R^d) is noncompact.
Take f with Gaussian Fourier transform and g=Lambda^-gamma f, nonzero
Schwartz. Translates of f have a common norm; their images are the same
translates of g. The autocorrelation of g tends to zero as separation
tends to infinity, since it is the Fourier transform of the Schwartz
function |hat g|^2 (or by direct integration by parts). Choose a large
spacing so every two distinct translates have image distance at least
||g||. There is no Cauchy subsequence, disproving compactness. Thus chi=1,
outside the compact-cutoff hypothesis, cannot be silently substituted.
There is no assertion of necessity at p gamma=d for K_chi here.

## 8. Controls and remaining project obligations

The diagnostic v1 uses psi=chi(x/2), equal1 ON supp chi but not its
neighborhood. It still has chi psi=chi, but does not literally instantiate
the stronger cutoff choice in Section2. v2 widens psi to chi(x/3), support
inside the larger L14 box, with a genuine plateau neighborhood. Both use
actual compact smooth cutoffs and nonzero whole-space Schwartz data.
Four of the sixteen recovery tests are trivial outside support; twelve
are nonzero. These finite Fourier truncations do not prove(15) or(2).

The 150 Peetre controls include negative indices; thirteen lattice-diagonal
checks concern ONLY the auxiliary inclusion. The five-node sampled
whole-space Fourier-kernel adjoint/swap tests are finite algebra (even chi
in the tests), not continuum singular-value evidence. The three uncut
translation controls are consistent with the separate analytic negative
argument. Working precision40 is not certified quadrature accuracy.
No new Lean module or extension of the prior71facts/18seams is claimed.

Still open: actual smooth test-noise basis/CM coefficients and their gain/
localization, matching the finite variance hypotheses to actual truncations,
compact variance-tail convergence, Gaussian series and time paths, source
limits/Young flow/canonicaldata and growing-cone lower bounds. Original
all-dimensional lower/sharpupper/source normalization/domain/label/exactlimit
goal remains ACTIVE. No source repair, correspondence, Skorohod/HPC/private
companion, canonical TeX/PDF/wiki edit or publication/whole-paper clearance.
