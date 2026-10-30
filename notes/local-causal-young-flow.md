# Physical masks, a local phase, and causal Young evolution

Status: CANDIDATE. The new analytic/source/type/application gate is pending.
This is an internal bridge for the original sharp-moment problem, not a new
claim of the operator-Young method. Standard Young machinery is imported
from Friz--Hairer; Chapouto--Li--Oh already use interaction drivers for waves.
No sharp moment constant, spectral growth event or higher-dimensional flow
is asserted. The original full target stays ACTIVE.

## 1. Contract and named inputs

Work in d1 with raw covariance |t-s|^-a Gamma(x-y),0<a<1,0<alpha<=1,
Gamma nonzero and in the ORIGINAL homogeneous Radon class. Set
E=H^(1/2)(R)xH^(-1/2)(R), H=1-a/2. Fix a real compact smooth zeta with
0<=zeta<=1, zeta=1on[-1,1], supp zeta contained in[-2,2], and set
zeta_R(x)=zeta(x/R),R>=1. Multiplication by a scalar acts diagonally on
phase vectors. Let S(t) be the massless free wave phase group.

Named accepted inputs, not re-proved:
- notes/interaction-driver-path.md, scientific b398b77/adoption77fd1fe:
  localized Gaussian HS first-driver increments, compatible versions,
  SOURCE-compatible common cutoffs with filtered ANDDEFECT covariance
  contraction and testwise convergence, and Lp Holder path convergence.
- notes/phase-response-test.md, source0ae116c: exact first-response HS trace,
  Gaussian Hilbert moments, stationary canonical regularization limits,
  Bochner spatial averages and averaged-to-original-point moment transfer.
- Canonical notes L:joint-fixed-order and L:vertex-crude/E:vertex-crude:
  arbitrary joint fixed-order L2 limits and summable norm bounds q_n(t),
  uniform in ALLvertex widths. Their scoped prior quantitative/construction
  gates are retained; the full regularized-solution consumer is derived here.
- notes/direct-event-calibration.md, source9d77f90: exact semiclassical
  scaling and the unit-block amplitude delta^((1-a)/2).

We prove the missing physical-mask and local-to-operator steps, then APPLY
standard Banach Young theory. All regularization limits below are at fixed
R and fixed finite horizon unless explicitly stated otherwise. A family of
uniform upper bounds is not an interchange with a large-time limit.

The proposed conclusions are:
1. The actual masked interaction driver is a Holder path in bounded
   operators on one separable local phase space F containing (1,0).
   Its operator path norm is bounded by a finite MAXIMUM of local HS
   driver norms, with constants independent of R.
2. It defines a linear nonexplosive evolution, compatible with the source
   cutoffs in all finiteLp operator differences. Physical evolution is
   strongly continuous; norm continuity of the FREEwave group is not claimed.
3. It is causal and recovers the actual canonical Stratonovich smooth
   spatial averages inside a cone on which zeta_R=1.
4. On the growing set of semiclassical unit blocks, the actual masked
   evolutions approach their deterministic-profile evolutions uniformly in
   block index in probability, and in every finiteLp operator difference.
   This is a block stability statement, not exponential solution growth.

## 2. The physical mask is bounded on the noise Hilbert space

For alpha<1 put b=(1-alpha)/2 in(0,1/2). The spatial Gaussian test norm,
up to its fixed covariance amplitude/Fourier constant, is

    ||f||_noise^2=integral_R |q|^(-2b)|fhat(q)|^2dq.         (2.1)

For alpha1 this is L2, and multiplication by zeta_R is a contraction.
For alpha<1 we prove, with C independent of R,

    ||zeta_R f||_noise <= C ||f||_noise.                    (2.2)

It suffices first to use the unit mask. In ordinary unweighted Fourier L2,
write g(k)=|k|^-b fhat(k). The absolute kernel of the mask conjugated by
this weight, apart from the fixed1/sqrt(2pi), is

    K(q,k)=|zetahat(q-k)| |q|^-b |k|^b.                    (2.3)

Use the positive Schur weight p(q)=|q|^-b off q0 (a Lebesgue-null set).
The weighted row integral is ||zetahat||_1 p(q). The column integral is
bounded by C p(k), because

    sup_(k!=0) |k|^(2b) integral_R
         |zetahat(q-k)| |q|^(-2b)dq < infinity.             (2.4)

Here is a direct check. For |k|<=2, split |q|<=4 and its complement;
2b<1 handles the singular part and Schwartz decay handles the tail.
For |k|>2 split |q|>=|k|/2, where the power costs at most C|k|^-2b,
and |q|<|k|/2. On the latter |q-k|>=|k|/2, so two powers of Schwartz
decay give C|k|^-2 times an integral bounded by C_b|k|^(1-2b).
After multiplication by |k|^(2b) this is bounded. This proves(2.4).

For clarity the weighted Schur consequence itself follows from
Cauchy--Schwarz: square integral K(q,k)g(k)dk using the factors p(k)
and1/p(k), apply the row bound, integrate q, then apply the column bound.
The resulting squared L2 operator bound is the product of the two Schur
constants. Thus(2.2) holds for R1 and dense tests, then in the completion.

For a scaled mask, zetahat_R(q)=R zetahat(Rq). The change z=Rq,y=Rk in
(2.4) cancels all R factors, while the L1 Fourier norm is unchanged. The
row/column constants are therefore uniform in R. This uses the homogeneous
noise norm, not an inhomogeneous Sobolev weight silently substituted for it.
The finite Lean row/column/rescaling deductions check these exact powers.

The same bound holds on the FULLspace-time Gaussian test Hilbert space.
Indeed Fourier-transform in time: its positive spectral measure tensors
with |q|^-2b dq; apply the spatial bound for almost every temporal frequency,
then integrate. The raw time normalization stays unchanged.

Falsification of a stronger endpoint assertion: b1/2 is excluded. For a
nonconstant real compact smooth zeta, choose f=zeta''. Then fhat(q)=O(q^2)
at0, so its |q|^-1 norm is finite, whereas integral zeta f=-integral(zeta')^2
is nonzero. Hence zetaf has infinite |q|^-1 norm. No uniform multiplier
claim at alpha0 follows, and this is outside the positive-alpha target.

## 3. Masked local drivers and source limits

Define W_R(f)=W(zeta_R f), and W_R^rho(f)=W^rho(zeta_R f), using the
COMMONsource construction of the accepted driver note. In particular the
physical mask is applied AFTER the noise regularization. It is NOTcommuted
through its spatial Fourier filter or through a wave operator. The source's
continuous temporal-slice coupling is a named input.

Source covariance contraction plus(2.2) gives, for every deterministic test,

    Var W_R^rho(f), Var(W_R-W_R^rho)(f), Var W_R(f)
         <= C^2 Var W(f).                                  (3.1)

Every masked test error tends to0 by applying the source limit to zeta_R f.
For the noise-Hilbert closure use(2.2) and density. Consequently the GENERIC
common-Gaussian criterion proved in the accepted driver note applies to
these new linear integrals. It gives, for every translated observation
chi_j(x)=chi(x-j) of one fixed compact smooth chi, theta in(1/2,H),

    ||chi_j M_R||_(Lp Ctheta HS(E)) <= C_(p,T),              (3.2)
    chi_j M_R^rho -> chi_j M_R in Lp Ctheta HS(E),           (3.3)

where

    M_R(t)=integral_0^t S(-u)B(W_R(du))S(u).                (3.4)

Constants in(3.2) are uniform in j,R,rho on fixed[0,T]. The underlying
RAWdriver bound is translation invariant; (3.1) has a uniform constant.
The same increment estimates hold for masked differences. This is only
LINEARGaussian covariance domination, never nonlinear solution/mean order.

Choose countable compatible local versions as in the prior note. Ordinary
distributional transpose finite propagation shows that M_R(t)-M_R(s) has
input-to-output propagation radius at most2T for0<=s<t<=T. Its output is
supported in[-2R-T,2R+T], and it vanishes on inputs supported outside that
interval. These facts first hold for smooth source cutoffs: each integrand
has wave propagation on each side and injects noise only in supp zeta_R.
They also follow directly on the Gaussian test side. Pass to the raw local
HS limits on countable smooth inputs/tests/times and use bounded extension/
path continuity. Do not use the nonlocal E-adjoint to deduce support.

## 4. One separable phase and the actual operator estimate

Choose chi real compact smooth, chi=1on[-2,2], supp chi in[-3,3], and
write chi_j for its integer translates. For distributional phases define

    ||v||_uloc = sup_(j in Z) ||chi_j v||_E.                (4.1)

This defines a Banach space E_uloc of locally E phases. Here are the needed
assembly details. Fix a smooth partition rho_j with sum_j rho_j=1, supported
in[j-1,j+1], so chi_j=1there. A Cauchy sequence for(4.1) converges after
each chi_j localization in E. Its local distributional limits agree on
overlaps, since multiplication by test cutoffs is bounded on E. The locally
finite sum using rho_j assembles one distribution v with those local limits;
then sup_j||chi_j(v_n-v)||_E tends to0 by the Cauchy bound. Thus the space
is complete. Distributional testing on each compact set is continuous.

Let F be the closure in E_uloc of smooth compact phase vectors plus the
two constant phases (1,0),(0,1). It is a separable Banach space containing
our initial data. All global E phases embed continuously in F: multiply
by chi_j with a uniform E multiplier bound, then approximate in global E
by compact smooth phases. Compactly supported locally E phases are global
E, by the finite partition above. No claim is made that arbitrary uniformly
local data, or the full unmasked random field, belong to F.

For any fixed B, a smooth translate psi_j=1on[j-B,j+B], supported in a
slightly larger fixed interval, satisfies

    ||psi_j v||_E <= C_B ||v||_uloc.                        (4.2)

To prove it, expand psi_j v into the FINITELY many psi_j rho_l chi_l v
with |l-j| bounded by B+2. All multipliers have uniform E bounds; take the
triangle inequality. This is not a square-sum over the full line.

Finite propagation and the bounded free group on E give
chi_j S(t)v=chi_j S(t)psi_j v with B depending only on T for |t|<=T.
Equations(4.2) and the global E bound imply S(t) bounded on E_uloc uniformly
on that horizon. It preserves F: compact smooth data propagate compactly,
and constant phases evolve by (c1,c2)->(c1+t c2,c2). Strong continuity holds
on that dense set, hence on F by the uniform bound. This is STRONG, not
operator-norm continuity of the free group.

Now select psi_j=1on the2T-enlargement of supp chi_j. The support fact in
Section3 gives, on global E inputs and then local distributions,

    chi_j [M_R(t)-M_R(s)]v
       =chi_j [M_R(t)-M_R(s)]psi_j v.                       (4.3)

Using HS>=operator norm and(4.2), for any finite path seminorm,

    ||M_R||_(Ctheta B(F))
      <= C_T max_(|j|<=2R+T+4)
                  ||chi_j M_R||_(Ctheta HS(E)).             (4.4)

Here M_R(0)=0; including its supremum norm only changes C_T. Construction:
for each compact/global E input the local Gaussian forms agree, and their
output is compactly supported locally E, hence in F. Identity(4.3) extends
this to every F input with the bound(4.4). More explicitly, choose a compact
kappa_R equal to1near[-2R-T,2R+T] and define the value on v by the already
constructed global-E operator applied to kappa_R v. The input support fact
makes it independent of kappa_R. This includes constant inputs; global E
is NOTbeing assumed dense in F. Local distributional assembly is unique. The same argument applied to raw/cutoff differences proves
convergence in Ctheta B(F) for fixed R. The map from this finite collection
of compatible HS paths to B(F) is continuous, so strong measurability comes
from their separable path versions; it is not assumed for a stationary
operator path on the full line.

There are at most C_T R indices in(4.4). Hence for all finite p>=1,

    ||M_R||_(Lp Ctheta B(F)) <= C_(p,T) R^(1/p),             (4.5)
    M_R^rho -> M_R in Lp Ctheta B(F), fixed R,T.             (4.6)

The convergence follows from the finite maximum and(3.3). Uniformity of
(4.5) covers all source widths, not an exchange of limits. The R^(1/p)
comes from a maximum, not a global HS norm of order sqrt(R).

We also need moment growth for the later nonlinear map. For one local
HS path, the Gaussian Hilbert inequality has constant C sqrt(p) for p>=2:
apply Minkowski to the sum of squared Gaussian coordinates and the scalar
Gaussian moment bound. In the prior dyadic path proof fix theta<gamma<H
and take p sufficiently large that1/p<=(H-gamma)/2. Its weighted dyadic
series is then bounded uniformly in p. Thus

    ||chi_j M_R||_(Lp Ctheta HS) <= C_T sqrt(p), p>=p0.      (4.7)

It holds for all cutoffs and differences. In a finite maximum (4.4), the
factor is at most(C_T R)^(1/p), so for fixed R its operator path norm has
uniform cutoff moments <=C_(R,T)sqrt(p). Expanding the exponential series,
using (2n)! or the bound n!>=(n/e)^n, gives
E exp(c_(R,T)||M_R^rho||_Ctheta^2) uniformly finite for some c_(R,T)>0.
No independence between cells, increments or source slices is required.

## 5. Apply standard linear Banach Young theory

The imported integration input is the Banach-valued Young estimate from
Friz--Hairer, Sections1.4--1.5/4.1 and Lemma4.2 (sewing). For a path
A in Ctheta([0,T];B(F)),A(0)=0,theta>1/2, it gives

    ||integral_s^t dA(u)Y(u) - [A(t)-A(s)]Y(s)||
         <= C_theta [A]_theta [Y]_theta |t-s|^(2theta).     (5.1)

Order matters: the operator increment multiplies Y ONTHELEFT. This standard
estimate also holds in the Banach algebra B(F), with ordinary composition.
The linear Young equation U=I+integral dA U has a unique global solution.
We record the short deduction needed by this application rather than claim
a new Young theorem. On an interval length ell, use the scaled norm
sup||Y||+ell^theta[Y]_theta. Equation(5.1) makes the integral map a
contraction when C[A]_theta ell^theta<=1/4. Its local operator bound is
at most2times the initial norm. Concatenate at most C_T(1+K^(1/theta))
intervals when [A]_theta<=K. The same local inequality applied to the
difference of two solutions gives local Lipschitz dependence on A and the
initial datum on bounded driver sets. Finite concatenation proves

    sup_(s<=t<=T)||U_A(t,s)|| <= C_T exp(C_T K^(1/theta)),   (5.2)
    sup_(s<=t<=T)||U_A(t,s)-U_D(t,s)||
         <= C_(K,T)||A-D||_Ctheta, ||A||,||D||<=K.          (5.3)

Its Ctheta norm on the triangle is bounded on such driver sets as well.
No smooth bump on an arbitrary Banach space, unbounded-field truncation,
commutativity or independent-increment hypothesis is used. This is the
linear case of Friz--Hairer8.3/8.9/Proposition8.12; the local calculation
checks the required bounded-algebra consumer directly.

Apply this with A=M_R (or any fixed scalar multiple). It gives interaction
operators U_R(t,s) on F and physical evolution

    P_R(t,s)=S(t)U_R(t,s)S(-s).                            (5.4)

They obey the evolution composition law. P_R is strongly continuous in
(s,t); norm continuity of S is not inferred. Equations(4.6),(5.3) give
convergence of P_R^rho to P_R, uniformly over s<=t in OPERATORdifference,
in probability. This does not assert that each physical path belongs to
C([0,T];B(F)). It is a uniform norm of the differences of strongly
continuous operator families.

In fact convergence holds in every finiteLp at fixed R,T. Equations(4.7)
and(5.2), with1/theta<2, imply uniform all-finite-moment bounds for the
cutoff and raw physical evolution norms: exp(C x^(1/theta)) is bounded by
a constant times exp(c x^2), for any fixed c>0. Convergence in probability
plus the higher moment bound gives uniform integrability and Lp convergence.
Strong measurability follows from the continuous Young map and the driver
versions, and for physical operator differences from the bounded linear
map V(t,s)->S(t)V(t,s)S(-s) into the supremum-norm family space.

A bounded deterministic potential h(t,x), measurable in t with uniformly
bounded W^(1,infinity) spatial norm on[0,T], is allowed as a base. Its
interaction primitive

    A_h(t)v=integral_0^t S(-u)B(h(u))S(u)v du              (5.5)

is defined as a strong integral in F for each v and is Lipschitz in B(F),
with bound C_T sup_u||h(u)||_W1infinity. Use an explicitly admissible profile
class: t->h(t) is strongly measurable in C_b^1, uniformly bounded there,
and h(t,x)=c(t)+h0(t,x), with bounded c and

    lim_(L->infinity) sup_t ||h0(t)||_W1infinity(|x|>=L)=0.  (5.6)

Compactly supported smooth profiles (one common compact support on a fixed
horizon) and spatially constant profiles are special cases. To verify F
invariance, multiplication is bounded on the local Sobolev phases, uniformly
by ||h||_W1infinity. It sends compact data into global compact phases, and
constant inputs into a constant plus h0. Cut off h0 outside[-L,L]; (5.6)
makes the resulting multiplier operators converge in B(F), while every
cutoff maps F into F. Thus the actual multiplier preserves F. No assertion
is made for an arbitrary bounded coefficient lacking this property. Apply
the same argument to A_h+g M_R. Uniform local Lipschitz stability holds
for such h with a fixed norm bound K; the tail rate in(5.6) is needed for
membership, not the local stability constant. A future Cameron profile
must be checked against this class and its Gaussian shift separately.

## 6. Source compatibility, causality and the actual observable

For positive source widths the masked field zeta_R W^rho is spatially
smooth and time continuous on compact sets (finite temporal Laplace range
and spatial heat). The resulting ordinary wave potential is bounded with
bounded first spatial derivative. To justify the path property at positive
widths, the spatial heat gives every finite spectral moment, and the finite
Laplace range gives time increment variance O(|t-s|). The same estimates
for spatial derivatives and Gaussian moments yield joint continuity on
compact sets by Kolmogorov, including the first spatial derivative. Its
usual strong/mild solution on F is
exactly(5.4). One does not need operator-norm differentiability of the wave
group: for each v the interaction primitive is the strong integral in(5.5),
now with the continuous random potential. Its B(F) increments are bounded
by the time integral of the operator norm. Young Riemann sums with a
continuous solution agree with that strong integral by the bound on the
coefficient and uniform continuity of the solution. Thus both formulations
have the same integral equation and uniqueness.

Ordinary smooth-potential wave evolution has propagation speed1 and local
dependence on the coefficient inside its backward cone. For completeness,
this follows directly from its Duhamel iteration: the wave kernel has
support |x-y|<=t-s; every iterated term is supported in the same cone by
the triangle inequality, and the bounded-potential Picard series converges
on every fixed horizon. The phase derivative entry has the same support.
The argument holds first on compact smooth data, then on F using bounded
localization and the evolution bound.

Choose a source sequence with almost sure convergence of the operator
families along a subsequence, supplied by the preceding Lp convergence.
Support/equality of distributions on fixed compact tests is closed under
F convergence. Therefore the same finite propagation holds for the raw
masked evolution. For two masks identical on a backward cone, their
regularized evolutions agree there; take their common-source limits.
This proves local independence of the mask, not a global stationary
operator path. Countably many masks/data/tests/times may be made compatible;
strong continuity and bounded extension give the usual fixed-horizon
operator statements. No uncountable exceptional-set exchange is used.

Now take initial data(1,0), zero deterministic profile, a fixed scalar noise
amplitude g, and a real smooth compact spatial test phi. If zeta_R=1on the
backward cone of {t}xsupp phi, then

    integral phi(x)[P_R(t,0)(1,0)]_1(x)dx
        = integral phi(x)u_g(t,x)dx in L2.                 (6.1)

Here u_g is the ORIGINALcanonical stationary Stratonovich model with noise
gW; g=0 is deterministic, g!=0 rescales Gamma by g^2. To prove(6.1), first
use the ordinary regularized equation and the local mask independence just
proved. The left average converges in L2 by operator convergence and the
bounded compact-test functional on F. The right regularized average
converges to its canonical Bochner average by the following explicit
series argument. At positive source widths, the ordinary solution at a
fixed point is its ordered Picard series sum_n g^n Y_n^rho. On each
compact backward cone this series converges pathwise, since its nth term
is bounded by M^n t^(2n)/(2n)! for a bound M on the potential there.
The named prior vertex estimate ||Y_n^rho||_2<=q_n(t) makes the same series
absolutely convergent in L2, uniformly in rho; sum_n|g|^n q_n(t) is finite
by its factorial denominator. Thus the pathwise and L2 sums agree. The
prior joint fixed-order limits give convergence of every finite prefix to
sum_n g^n X_n, and the uniform summable tails give full solution convergence.
The common Gaussian family is spatially stationary, so its L2 error is the
same at every x. The L2triangle bound for the average is ||phi||_1 times
that error. At positive widths, joint measurability and these uniform L2
bounds justify ordinary/Bochner spatial Fubini; no simultaneous pointwise
version of the raw limit is required. This uses L:vertex-crude, not the
weaker assertion that only canonical tails are summable. Uniqueness of limits gives
(6.1). No bounded point evaluation on H1/2 is used or claimed.

Nonnegative unit-mass phi therefore remains a valid observable for the
original POINTsecond moment through the accepted average inequality. This
identification is at fixed parameters before time asymptotics. A deterministic
h-flow exists as above, but its identification with a Cameron--Martin shift
of the canonical random variable is a separate future obligation.

## 7. Actual block-flow stability on a growing cone

Fix theta in(1/2,H) and a fixed block length1. Let0<delta<=1,
R_delta=c/delta with fixed c>=1, m=0,...,ceil(1/delta). Use the jointly
defined source fields

    W_m^delta(u,x)=delta^(a/2)W(m delta+delta u,x),
    g_delta=delta^((1-a)/2).                                (7.1)

Each has the raw law, and its source temporal cutoff is eta/delta. Spatial
heat widths stay unchanged. Apply the same physical mask zeta_Rdelta.
The previous driver estimates are uniform over m,delta and source widths.
The union of relevant spatial cells and time blocks has at most C_c delta^-2
indices. Let Z_delta be the maximum of their local HS Ctheta driver norms.
For every finite q>=1,

    ||g_delta Z_delta||_Lq
         <=C_q delta^((1-a)/2-2/q).                        (7.2)

This is the already verified two-index maximum argument. It needs no
independence. Choosing q>4/(1-a) gives convergence in probability, and any
smaller requested Lp convergence follows by a larger q. Equations(4.4)
and(7.2) control the ACTUALmasked B(F) drivers on ALLblocks. The phase on
a unit block is(V,partial_u V)=(V,delta partial_t V), as in the accepted
semiclassical calibration.

For deterministic block profiles h_m with the explicit admissibility
hypothesis(5.6)of Section5 and a common W1infinity bound K, let P_delta,m be
the actual unit-block physical evolution driven by h_m+g_delta zeta_Rdelta
W_m^delta, and P_hm its deterministic evolution. Standard Young stability
(5.3) gives, on {g_delta Z_delta<=epsilon<=1},

    max_m sup_(0<=s<=t<=1)||P_delta,m(t,s)-P_hm(t,s)||_B(F)
         <= C_K epsilon.                                  (7.3)

Thus the maximum operator difference tends to0 in probability, uniformly
in source widths; it also holds for the raw masked evolutions. Uniformity
means a supremum of the individual probability/moment bounds, or any choice
rho=rho(delta), not a pathwise supremum over an uncountable set of widths.

It tends to0 in every fixed finiteLp as well. Choose p0 large enough that
p0>4/(1-a) and that(4.7) holds for p>=p0. For any q>=p0, the finite-maximum
bound and(4.7) give

    ||g_delta Z_delta||_Lq <= C sqrt(q), uniformly delta,rho. (7.4)

Indeed delta^((1-a)/2-2/q)<=1. Expanding the exponential series as in
Section4 gives one uniform small-square-exponential moment. Equation(5.2),
with1/theta<2, supplies uniform higher moments for the maximum physical
evolution norm, raw and cut off, with bounded deterministic base. Combine
(7.3), probability convergence and uniform integrability. This proves the
all-finiteLp assertion without asserting a uniform pathwise stationary
operator on the full line.

For each fixed delta, the finitely many blocks concatenate by their source
limits and the evolution composition law. Taking c large enough protects
a fixed terminal observation interval and its whole backward cone; Section6
identifies the noise-only smooth averaged observable with the original
semiclassical/canonical one. Constants for existence on the full horizon
can depend on delta; the SMALLBLOCKstability constants above do not.
Neither a cutoff/large-time limit interchange nor closeness of the ENTIRE
product of1/delta blocks to its deterministic product follows from(7.3).
The needed spectral cone/product growth estimate remains OPEN.

## 8. Source and completion boundary

CLO, arXiv2607.07618v1, equations(1.22)--(1.24),Theorem1.4,Proposition4.1
and Section6 are method prior art, not a direct theorem giving(6.1)/(7.3).
For periodic diagonal spectra with tail |phi_n|^2 comparable to |n|^(alpha-d),
HS(L2;Hsigma) needs2sigma+alpha<0, while same-phase source bounds demand
sigma>max(-s,s-1)>=-1/2. These can coexist only ifalpha<1. In d1white no s
satisfies them. This is a comparison of those sufficient stated hypotheses,
not an impossibility theorem for their methods or other results. Foralpha<1,
s1/2 and sigma=-(1+alpha)/4 pass the tail inequalities. Original whole-line
Riesz covariance is NOTsilently identified with a periodic covariance.
Standard dyadic annuli prove the stated tail summability test; at equality
every annulus has a positive constant contribution and the sum diverges.

The seven new finite Lean facts cover mask order, Schur powers and these
source budgets; the previous eight InteractionDriver deductions are reused
unchanged at their exact box/Holder consumers. No operator/integration/
Gaussian/Young/causality/canonical-identification theorem is formalized.
No package/companion/lease/registry/donor write/cluster/Comparator gate.
The detailed source gate and ordinary new-reference ticket are separate.

Still open: the nonzero-profile Cameron-shift identification, a deterministic
spectral cone and growing product growth, a sharp event/variational lower
bound and intended source constant map; original higher dimensions and full
sharp upper/lower constant. No source1.24repair, Skorohod moment/asymptotic,
novelty, whole-paper or circulation clearance. WHITE13/original9and canonical
110-page/60-proof TeX/PDF remain unchanged.
