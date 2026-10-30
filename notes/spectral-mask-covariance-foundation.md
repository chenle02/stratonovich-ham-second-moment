# Spectral growth and a physical-mask linear covariance bound

ACCEPTED internal covariance foundation: independent Opus5.5/high full
review, PASS_WITH_NOTES/HIGH, scientific revision af9b1ad; see the
2026-10-30-spectral-mask-foundation review packet and adjudication.
This is a raw covariance foundation. It constructs no operator path or
wave flow and proves no new moment asymptotic. Canonical H:homog and the
original all-dimensional sharp goal are retained.

## 1. Objects and conventions

Fix d in {1,2,3}, a in (0,1), alpha+a<2, with 0<alpha<d or alpha=d=1.
Gamma is a NONZERO nonnegative even positive-definite tempered Radon
measure, Gamma(cA)=c^(d-alpha)Gamma(A). Its positive even tempered spectral
measure mu is in the convention

    Gamma = int exp(i xi.x) mu(dxi), distributionally.

Thus for every complex Schwartz test phi,

    int phi(x) Gamma(dx) = int [int exp(i xi.x)phi(x)dx] mu(dxi).       (1)

This is a distribution pairing identity. It does not assert absolute
integrability of the joint oscillatory integral. Write c_d=(2pi)^(-d/2)
and hat f(xi)=c_d int exp(-i xi.x)f(x)dx. For real Hilbert spaces Fourier
transforms take values in the complexification, with its usual norm.

Tempered positive Radon measures integrate every Schwartz function
absolutely. One direct justification of the needed polynomial bound is to
choose a nonnegative compact smooth phi>=1 on the unit ball. Continuity of
the distribution gives a finite Schwartz seminorm bound on its pairing
with phi(x/R); that seminorm grows at most polynomially for R>=1.
Consequently the mass of the ball of radius R grows polynomially. Dyadic
shells then show integrability of (1+|x|)^(-N) for some N, and of every
Schwartz function. This applies separately to Gamma and mu. Cutoffs
converge in Schwartz topology, so dominated convergence identifies the
tempered pairing with the ordinary integral for these measures.

## 2. Uniform translated spectral growth

**Proposition 1.** Let

    M_Gamma = int exp(-|x|^2/4) Gamma(dx),
    C_Gamma = e M_Gamma/(2sqrt(pi))^d.

Then 0<M_Gamma<infinity, and for every y in R^d and r>0,

    G_r(y) := int exp(-|xi-y|^2/r^2) mu(dxi)
      = (r/(2sqrt(pi)))^d
           int exp(-r^2|x|^2/4)exp(-i y.x) Gamma(dx),                 (2)
    0 <= G_r(y) <= r^alpha M_Gamma/(2sqrt(pi))^d,
    mu(B(y,r)) <= C_Gamma r^alpha.                                  (3)

Balls may be open or closed. No spectral density is assumed.

*Proof.* Gaussian integrability follows from Section 1; positivity of M
follows from Gamma nonzero and the strictly positive integrand. For the
Fourier constant, the one-dimensional integral J(b)=int exp(-A x^2)
exp(i b x)dx, A>0, has J(0)=sqrt(pi/A), as follows by squaring the real
Gaussian integral and using polar coordinates. Differentiation under the
integral and integration by parts give J'(b)=-b J(b)/(2A). Hence
J(b)=sqrt(pi/A)exp(-b^2/(4A)). Taking products in d coordinates gives

 int exp(-r^2|x|^2/4)exp(i(xi-y).x)dx
       =(2sqrt(pi)/r)^d exp(-|xi-y|^2/r^2).

Apply (1) to the SINGLE Schwartz test
exp(-r^2|x|^2/4)exp(-i y.x), then multiply by (r/(2sqrt(pi)))^d.
This proves (2) without interchanging two infinite measures. Its left side
is nonnegative and finite. The absolute value of its right side is bounded
by the same expression with exp(-i y.x) removed, since Gamma>=0.

The pushforward of Gamma under x->r x assigns to A the mass
Gamma(A/r)=r^(alpha-d)Gamma(A). Initially for indicators, then nonnegative
simple functions and monotone convergence, this gives

 int exp(-r^2|x|^2/4)Gamma(dx)=r^(alpha-d) M_Gamma.

Substitution proves the Gaussian bound in (3). On either ball B(y,r),
exp(-|xi-y|^2/r^2)>=e^-1; integrating gives the ball bound. This proves
Proposition 1.

## 3. An auxiliary spectral measure for physical masks

Fix a real nonzero Schwartz function zeta and R>0. Set zeta_R(x)=zeta(x/R),
k_R=hat zeta_R, and L=||hat zeta||_1. Changing variables in the Fourier
integral gives k_R(u)=R^d hat zeta(Ru), so ||k_R||_1=L in (0,infinity).
Define the positive measure

    nu_R(deta)=rho_R(eta)deta,
    rho_R(eta)=c_d^2 L int |k_R(xi-eta)| mu(dxi).                     (4)

This auxiliary measure is a bounding norm; the original Gaussian noise
has not been replaced.

**Proposition 2.** nu_R is an even tempered Radon measure. For all y,r>0,

    nu_R(B(y,r)) <= c_d^2 L^2 C_Gamma r^alpha,                        (5)

uniformly over R>0. If H is a separable complex Hilbert space and F is an
H-valued Schwartz function (all derivatives rapidly decreasing in H norm),
then

 int ||hat(zeta_R F)(xi)||_H^2 mu(dxi)
       <= int ||hat F(eta)||_H^2 nu_R(deta).                         (6)

The assertion also holds for real H after complexification.

*Proof.* A Schwartz decay bound for |k_R| and the polynomial mass growth
of mu show rho_R(eta)<infinity for every eta. On each compact eta set the
same bound dominates the integrand uniformly; dominated convergence shows
rho_R is continuous. Thus nu_R is locally finite and Radon. Since zeta is
real, k_R(-u)=conj(k_R(u)), even if zeta itself is not even. Evenness of mu
then makes rho_R even.

Tonelli, with u=xi-eta, gives exactly

 nu_R(B(y,r))=c_d^2 L int |k_R(u)| mu(B(y+u,r))du.

Apply (3), then int |k_R|=L, to obtain (5). In particular nu_R has
polynomial growth on centered balls and is tempered by the dyadic-shell
argument of Section 1. The constant in (5) depends on zeta through L but
not on R. Local density bounds need not be uniform in R.

Bochner Fourier integration, multiplication and convolution give

    hat(zeta_R F)(xi)=c_d int k_R(xi-eta)hat F(eta)deta.

For clarity, this identity follows first for scalar Schwartz functions
by inserting Fourier inversion (absolute integrability holds), then for
finite-rank H-valued functions. For general H-valued Schwartz F, let P_n
be orthogonal projections onto an increasing finite-dimensional span of
an orthonormal basis. The Schwartz bounds on F dominate all needed
integrals; P_n F and their Fourier integrals converge pointwise in norm,
so dominated convergence proves the same identity. In finite-dimensional H
use the full identity projection, and in the zero space the assertion is
trivial.

The Bochner triangle inequality followed by weighted Cauchy-Schwarz yields

 ||hat(zeta_R F)(xi)||^2
   <=c_d^2 L int |k_R(xi-eta)| ||hat F(eta)||^2 deta.

Integrate against mu and use Tonelli. The right side is exactly the right
side of (6). It is finite since hat F is Schwartz in norm and nu_R is
tempered; the same argument also establishes integrability on the left.
This proves Proposition 2.

## 4. Actual temporal covariance and completion on the same noise

Fix T>0. On C_c^infinity(0,T;R) put

 <tau,sigma>_a=int_0^T int_0^T tau(t)sigma(s)|t-s|^-a dt ds.

This positive semidefinite form defines the real Hilbert completion H_a
of its null quotient. To verify positivity directly, use

 |t-s|^-a = Gamma_E(a)^-1 int_0^infinity lambda^(a-1)
                                      exp(-lambda|t-s|)dlambda

away from the null diagonal, and

 exp(-lambda|t-s|)=int_{-infinity}^{min(t,s)}
          2lambda exp(-lambda(t-u))exp(-lambda(s-u))du.

For each lambda the quadratic form is an integral of a square. The
Laplace identity is the change of variables v=lambda|t-s| in the defining
Euler Gamma integral. All exchanges for smooth compact tests are valid:
absolute integrability follows from
sup_t int_0^T |t-s|^-a ds <= 2T^(1-a)/(1-a), followed by Cauchy-Schwarz
(or the elementary 2|xy|<=|x|^2+|y|^2 bound). The same estimate gives
||tau||_a^2 <= 2T^(1-a)/(1-a) ||tau||_2^2. A countable L2-dense family of
smooth compact tests is therefore H_a-dense, so H_a is separable.

Let D consist of finite sums F(t,x)=sum_j tau_j(t)f_j(x), with tau_j as
above and f_j real Schwartz. These are a subclass of H_a-valued Schwartz
functions of x, not all such functions. For the original real isonormal
noise W and its canonical test completion, define W(F) by the physical
covariance form in the model. It is finite on D. If W is initially
given on compact spatial tests, multiply f_j by expanding smooth cutoffs:
the products converge in Schwartz topology, and the spectral form below
is continuous in that topology, so D lies in the same noise completion.
In this convention,

 E W(F)^2 = (2pi)^d int ||hat F(xi)||_(H_a complexified)^2 mu(dxi).   (7)

Here is the normalization derivation, rather than a convention change.
For real spatial f,g, let h(z)=int f(y+z)g(y)dy, a Schwartz function.
Fourier inversion and Parseval give
h(z)=int exp(i xi.z)hat f(xi)conj(hat g(xi))dxi. Thus
int exp(i xi.z)h(z)dz=(2pi)^d hat f(-xi)conj(hat g(-xi)). Apply (1) to
h, then reflect xi using evenness of mu. Consequently the spatial
covariance form int h(z)Gamma(dz) is (2pi)^d int hat f(xi)conj(hat g(xi))
mu(dxi). Sum over the finite temporal factors to obtain (7). Absolute
integrability follows from Schwartz decay and temperedness; the temporal
kernel is integrable on the finite interval. No joint infinite-measure
oscillatory Fubini is used.

Apply (6) with H equal to the complexification of H_a. It gives

    E W(zeta_R F)^2 <= N_R(F)^2,
    N_R(F)^2 := (2pi)^d int ||hat F(eta)||_H_a^2 nu_R(deta).          (8)

Define A_R to be the Hilbert completion of D/{F:N_R(F)=0}, with this
auxiliary norm (and the associated real inner product). For F in D the map
F->W(zeta_R F) is linear into the actual L2(Omega) of the SAME original W.
Equation (8) annihilates auxiliary-null tests and makes this map a
contraction, so it extends uniquely to A_R. Specifically an auxiliary
Cauchy sequence produces an L2(Omega) Cauchy sequence of actual masked
noise evaluations; equal auxiliary classes give equal L2 limits. The
limits remain centered jointly Gaussian, since their finite linear
combinations are L2 limits of centered Gaussians, with convergent
variances and hence convergent Gaussian characteristic functions.
This proves the stated completion assertion. It depends on zeta and R;
it does not claim multiplication descends to the original mu quotient.
No concrete spatial distribution representative for every A_R element is
required or asserted.

For finite F_1,...,F_m in D, let A_ij=E[W(zeta_R F_i)W(zeta_R F_j)] and
let B_ij be the real auxiliary inner product associated with N_R. Both
carry the SAME (2pi)^d normalization. Applying (8) to sum b_i F_i for
arbitrary real b gives b^T A b<=b^T B b, so B-A is positive semidefinite.
Diagonalize this finite real symmetric matrix to construct a centered
Gaussian Z of covariance B-A independent of the vector X of actual masked
noise values, on a product probability space. Then X+Z has covariance B.
For any norm on R^m and p>=1, convexity and conditional Jensen give
E||X||^p<=E||X+Z||^p. Finite Gaussian moments make these expectations finite.
This comparison concerns ONLY finite linear Gaussian images. It is not a
covariance comparison for nonlinear wave solutions. Also (4) does not
assert that the inverse Fourier covariance of nu_R is nonnegative as a
physical measure; later estimates may use (5), not such an assumption.

## 5. A genuine compact-mask obstruction in the original quotient

**Proposition 3.** In the actual admissible d=2 case

    Gamma=delta_0(dx1) dx2, alpha=1, 0<a<1,
    mu=(2pi)^-1 dxi1 delta_0(dxi2),

there is a real compact smooth physical mask for which no finite bound
E W(zeta F)^2<=C E W(F)^2 holds for all compact smooth space-time tests F.
In particular this mask does not descend to the original noise quotient.

*Proof.* The distributional spectral identity follows from
int exp(i xi1 x1)dxi1=2pi delta_0(x1) and the constant function 1 in x2.
Equivalently apply Fourier inversion to a Schwartz test, avoiding a
pointwise interpretation of that identity. Gamma is nonnegative, even,
positive definite and tempered, with Gamma(cA)=c Gamma(A); thus alpha=1
and alpha+a<2. This is not white noise in d=2.

For any real spatial test g, its covariance is exactly

 V(g)=int_R [int_R g(x1,x2)dx2]^2 dx1.                              (9)

Indeed integrate the displacement covariance delta_0(dz1)dz2 against
int g(y+z)g(y)dy; compact support licenses the ordinary Fubini here.

Choose real even chi in C_c^infinity(R), 1 on [-1,1], 0 outside [-2,2].
Such a nonconstant plateau can be constructed by chi=1 for r=|x|<=1,
chi=0 for r>=2, and, for 1<r<2,

 chi(x)=exp(-1/(2-r))/[exp(-1/(2-r))+exp(-1/(r-1))].

The exponentials vanish to every order at their respective endpoints,
so the pasted function is smooth. Put I=int chi'^2 and J=int chi^4.
Both are finite and positive: J>=2, and I=0 would force chi constant.
Let g(x)=chi(x1)chi''(x2) and zeta(x)=chi(x1)chi(x2), both compact smooth.
The unmasked marginal vanishes exactly since int chi''=0. The masked
marginal equals chi(x1)^2 int chi chi''=-I chi(x1)^2 by integration by
parts with zero boundary terms. Equation (9) gives

    V(g)=0,           V(zeta g)=J I^2>0.

Finally take any nonzero nonnegative tau in C_c^infinity(0,T) and
F(t,x)=tau(t)g(x). Its time variance factor ||tau||_a^2 is finite and
strictly positive, since the integrand tau(t)tau(s)|t-s|^-a is positive
on a set of positive two-dimensional measure. Thus the full unmasked
noise variance is zero and the masked variance is ||tau||_a^2 JI^2>0.
No finite C can bound the latter by the former. This proves Proposition 3.

The Gaussian SCHWARTZ diagnostic uses zeta_R(x)=exp(-|x|^2/(2R^2)),
not this compact mask. Exact zero unmasked variances in diagnostic JSON
are analytic labels from marginal differentiation, not numerical zero
integrals. The numerical compact check verifies integration by parts at
60-digit working precision with relative tolerance 1e-45; its assertions
were executed without Python optimization. These controls are not proofs
of Propositions 1-3.

## 6. Consequences and remaining obligations

These results apply to every original covariance in H:homog; no density,
strict spectral positivity or effective dimension assumption was added.
The zero covariance is trivial and excluded only to make M_Gamma>0.
Proposition 3 supplies an actual d2 counterexample to a bound claimed
uniformly over the full d2/3 class; no separate d3 counterexample was
proved here. Proposition 2 instead REPLACES the norm of INPUT TESTS and
bounds the actual masked linear noise on its original probability space.
The auxiliary and original test norms need not dominate one another.
It neither changes the nonlinear PDE nor establishes an operator norm.

Still needed: actual four-component phase covariance in both operator
variance directions, localized Schatten moments and cutoff tails, time
regularity and a fixed-space causal Young flow, actual canonical constant
data compatibility and growing cones, all-dimensional lower bounds and
sharp upper constants. The separate scalar row plan is unreviewed, outside
this proof packet. Source normalization/domain/label decisions remain open;
no identification of source variational energies or exact limit is made.
No new Lean claim, Skorohod result, correspondence, HPC, private companion,
public release or whole-paper/cold-reader clearance follows here.
