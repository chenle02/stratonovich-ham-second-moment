# Actual masked wave forms and both mean-square variance directions

ACCEPTED internal actual-variance result: native Opus5.5/high full review,
PASS_WITH_NOTES/HIGH, scientific revision227d4bc; see the
2026-10-30-actual-two-variance proof packet and adjudication.
The forms below use the SAME original W. No random bounded operator,
Schatten path, source limit, Young flow or new moment asymptotic is claimed.

## 1. Objects, phases and precise assertions

Use canonical H:homog: d in {1,2,3}, a=alpha_0 in (0,1), alpha+a<2,
0<alpha<d or alpha=d=1. Gamma is nonzero, nonnegative, even,
positive-definite tempered Radon with Gamma(cA)=c^(d-alpha)Gamma(A), and
Gamma=int exp(i xi.x)mu(dxi) in tempered distributions. W is its original
real Gaussian test completion with raw temporal kernel |t-u|^-a.
Complexify by W_C(F)=W(Re F)+i W(Im F).

Set Lambda=(1-Delta)^(1/2), <xi>=sqrt(1+|xi|^2), c_d=(2pi)^(-d/2),
and use unitary spatial Fourier transform. On complex phases let

 E_s=H^s x H^(s-1), s=1/2,
 Jz(xi)=(<xi>^(1/2)hat z1(xi),<xi>^(-1/2)hat z2(xi)).

J is unitary from E_s to L2(R^d;C^2). Inner products are linear in the
first slot. Let S(t) have the full massless wave matrix

 [[cos(t|xi|),sin(t|xi|)/|xi|],
  [-|xi|sin(t|xi|),cos(t|xi|)]],

with sine quotient t at xi=0. B(b)(u,v)=(0,bu). Fix a real even compact
smooth mask zeta>=0, equal1 on B1 and zero off B2; zeta_R(x)=zeta(x/R)
for every R>0. Fix T>0 and I=[s0,s0+h] subset[0,T], 0<h<=1.
No observation cutoff is part of the next definition.

For Schwartz phases z,w put

 v_z(t)=[S(t)z]_1,
 G_w(t)=-sin(t|D|)/|D| [Lambda w1]+cos(t|D|)[Lambda^-1 w2],
 F_z,w(t,x)=1_I(t) v_z(t,x)conj(G_w(t,x)),
 ell_R(I;z,w)=W_C(zeta_R F_z,w).                                   (1)

Admission in the actual completion is proved below. The admitted form is
linear in z and conjugate linear in w: v_z and G_w are linear, and the
conjugate in (1) gives the second assertion since W_C(iF)=iW_C(F) directly
from its definition. Define

 0<gamma<min(1/2,(2-alpha)/2),
 B_alpha(h)=1 if alpha<1; 1+log(1/h) if alpha=1; h^(1-alpha) if alpha>1.

**Proposition 1.** There is finite C_T, depending on the fixed model,
mask,a,alpha,gamma,T but not R,I,the family or its size, such that every
finite complex E_s-orthonormal Schwartz phase family {e_k} and every
Schwartz phase z satisfy

 sum_k E|ell_R(I;e_k,z)|^2
       <=C_T h^(2-a)B_alpha(h)||z||_(E_(s-gamma))^2,                 (2)
 sum_k E|ell_R(I;z,e_k)|^2
       <=C_T h^(2-a)B_alpha(h)||z||_(E_(s-gamma))^2.                 (3)

For every 1/2<beta<min(1-a/2,(3-a-alpha)/2), either right side can be
replaced by C_T,beta h^(2beta)||z||_(E_(s-gamma))^2, uniformly as above.
Here ||z||_(E_(s-gamma))=||<xi>^-gamma Jz||L2.

**Proposition 2.** On the SAME probability space there are deterministic
bounded real linear maps

 m_R,I,n_R,I:E_(s-gamma)(R) -> L2(Omega;E_s(R)),

with squared bounds (2)-(3), for which, for each fixed real Schwartz pair,

 <m_R,I z,w>_E =ell_R(I;z,w)=<z,n_R,I w>_E in L2(Omega).             (4)

Their fixed-vector values and finite families of such values are centered
Gaussian. No common uncountable almost-sure version or random bounded
operator on E_s is asserted.

Named OWN accepted inputs: spectral-mask-covariance-foundation.md,
Propositions1-2 and Section4 (raw variance, auxiliary norm, its uniform
translated growth); scalar-frequency-row-bound.md Proposition1 and
Corollary2; temporal-phase-bound.md Propositions1-3 and Section1. All new
complex/indicator applications, phase matching and Bessel arguments are
proved here, not attributed to their old reviews. The old HS obstruction
supplies the phase conventions and a scoped comparison, not a driver norm.

## 2. Actual tests, complex covariance and the auxiliary bound

For Schwartz phases all v_z,G_w are Schwartz uniformly for t in[0,T].
The free multiplier is smooth at zero by the continuous sine quotient;
its derivatives have polynomial growth uniformly on compact time intervals.
The Bessel multipliers preserve Schwartz space. These facts also show
continuous dependence on t in every Schwartz seminorm.

For tests supported in a fixed compact spatial K, the absolute spatial
covariance is at most

 |K| Gamma(K-K) ||F(t)||infinity ||H(u)||infinity.

Indeed in int Gamma(dy)int F(t,x)conj(H(u,x-y))dx, only y in K-K can
contribute and the x integral is bounded by |K| times the product of
suprema. Local finiteness of Gamma and the temporal Schur bound
2T^(1-a)/(1-a) thus give a finite covariance bound by a constant times
the L2 temporal supnorms. Approximate the indicator and time dependence
in (1) by smooth interior temporal tests, retaining the common spatial
support supp zeta_R. This proves zeta_R F_z,w belongs to the raw completion
for EVERY allowed d and finite T. This is a new application of the direct
argument, not an invocation of the d2/3,T<=1 scope of the old HS note.
The membership constant can depend on R; the estimate proved later does not.

Here are also consistent auxiliary approximants. For any spatially Schwartz
F(t,x) continuous in Schwartz seminorms on I and zero off I, time partitions
with frozen spatial values approximate F in L2 time in every Schwartz
seminorm. Replace the finitely many cell indicators by compact smooth
temporal functions. A diagonal sequence F_n then consists of finite smooth
temporal tensors and converges in these L2 seminorms. Spatial Fourier
integration by parts shows, for every fixed sufficiently large integer N,

 ||hat(F_n-F)(xi)||_L2(0,T) <=epsilon_n <xi>^-N, epsilon_n ->0.

For example integrate spatial derivatives by parts and bound the resulting
L1 spatial norms by a higher weighted Schwartz supremum. Minkowski in time
makes the same estimate with L2 temporal seminorms. Since mu and nu_R are
tempered, choose N so their integrals of <xi>^(-2N) are finite. The Schur
bound for the temporal Hilbert H_a then gives convergence in both spectral
H_a norms. After masking, the fixed-K estimate above gives convergence in
the raw noise completion. Multiplication by the fixed Schwartz mask
zeta_R also preserves the L2 Schwartz-seminorm convergence, with constants
allowed to depend on R here. The same Fourier decay argument therefore
gives convergence of the MASKED difference in the mu spectral norm too,
as required for the equality in (5). Thus the auxiliary extension and actual W limit
agree for (1); no original-noise-quotient multiplier theorem is used.

The complex extension needs a normalization check. For real tensor tests
f,g, their spatial transforms obey hat f(-xi)=conj(hat f(xi)). The temporal
H_a is a complexification of a real Hilbert space, so
A(xi)=<hat f(xi),hat g(xi)>_H_a satisfies A(-xi)=conj(A(xi)). Integrating
against either even mu or even nu_R makes the imaginary part zero. Thus
expanding the squared norm of hat f+i hat g and integrating gives exactly
the sum of the two individual squared norms: the mixed imaginary term is
odd and cancels. All integrals are finite by Schwartz decay. Approximation
as above extends this to the indicator tests.

Consequently the real variance formula and mask inequality extend to these
complex tests with the SAME constants:

 E|W_C(zeta_R F)|^2
  =(2pi)^d int ||hat(zeta_R F)(xi)||_H_a^2 mu(dxi)
  <=(2pi)^d int ||hat F(lambda)||_H_a^2 nu_R(dlambda).               (5)

The auxiliary measure is the actual one from the accepted foundation,

 nu_R(deta)=c_d^2 L_zeta [int |hat zeta_R(xi-eta)|mu(dxi)]deta,
 L_zeta=||hat zeta||1=||hat zeta_R||1,
 nu_R(B(y,r))<= C_nu r^alpha,
 C_nu=c_d^2 L_zeta^2 C_Gamma,                                      (6)

where C_Gamma is the constant of its Proposition1. It is positive, even,
Radon and tempered. The ball bound is uniform in R. Equation(5) concerns
the ACTUAL masked W on its original space. Its right side is a positive
bounding norm, not the declaration that masked W is stationary, and no
auxiliary stochastic field or nonlinear PDE comparison is needed.

## 3. Sobolev adjoint and the full normalized interaction

For definiteness take a deterministic b smooth on[0,T]xR^d with common
compact spatial support and uniformly bounded spatial derivatives on this
interval. Multiplication and S(t) are bounded on E_s on compact times;
this follows from Schwartz convolution with Bessel weights and the full
wave matrix. The strong integral int_I S(-t)B(b(t))S(t)z dt is therefore
well-defined for each E_s input.

Direct Fourier duality with both E_s weights gives, for Schwartz phases,

 <S(-t)B(b(t))S(t)z,w>_E
       =int b(t,x)v_z(t,x)conj(G_w(t,x))dx.                         (7)

Indeed S(-t)(0,f)=(-sin(t|D|)f/|D|,cos(t|D|)f); move the selfadjoint
real Fourier multipliers and the weights Lambda^(2s),Lambda^(2s-2)
onto w. At s=1/2 these are precisely Lambda and Lambda^-1 in (1).
Thus the formula keeps both phase entries and the actual E_s adjoint.
For a classical smooth source use b=zeta_R dot W^rho and integrate(7):
the pairing is W_C^rho(zeta_R F_z,w), NOT raw ell_R. No source convergence
is inferred from this fixed-width identity.

For a real compact smooth chi let Dchi multiply both phase entries. Its
E_s adjoint on Schwartz phases is

 Dchi^*E w=(Lambda^(-2s)chi Lambda^(2s)w1,
           Lambda^(2-2s)chi Lambda^(2s-2)w2).

It is generally not Dchi. Formula(7) applied with Dchi^*E w yields the
localized test with chi INSIDE the two Bessel-weighted arguments of G.
Thus ell_R(I;z,Dchi^*E w) is the correctly observed form. In the OLD
accepted HS note's literal scope d2/3,real phases,R>=1,I=(0,T),T<=1,
s=1/2 and chi=1 on B_(2R+T+1), this equals its named ell_chi (endpoints do not affect the noise
norm). Outside that scope the displayed identity is derived here, not
imported by putting chi=1 in a compact-chi theorem.

Write r=|xi|,rho=|eta|, c_r=cos(rt), b_r=<r>sin(rt)/r with b_0=t. If
U=Jz,V=Jw then

 hat v_z(t,eta)=<eta>^-1/2 [c_rho U1(eta)+b_rho U2(eta)],
 hat G_w(t,xi)=<xi>^-1/2 [-b_r V1(xi)+c_r V2(xi)].                  (8)

Therefore the normalized phase kernel, with spatial multiplication's
convolution constant and Fourier coefficient removed, is EXACTLY

 K(t;xi,eta)=(<xi><eta>)^-1/2
       [[-b_r c_rho,-b_r b_rho],[c_r c_rho,c_r b_rho]].              (9)

For r,rho>0 this is also direct multiplication of J_xi S(-t,xi), the
lower-left coupling and S(t,eta)J_eta^-1. The unchanged local Lean theorem
DimensionalMatrix.full_interaction verifies that divided-frequency matrix
identity with cp=cos(rt),sp=sin(rt),p=r,H the scalar Fourier coefficient,
cq=cos(rho t),sq=sin(rho t),q=rho. The weighted application is the algebra
in (8)-(9), not a new theorem from that finite proof. At either zero radius
use the continuous sinc in the physical S, not Lean's field division at0;
(8)-(9) then follow by direct substitution/continuity, including the matrix
[[-t,-t^2],[1,t]] when both radii vanish.

The scalar Schwartz product Fourier formula, with the conjugate in (1), is

 hat F_z,w(t,-lambda)
  =c_d 1_I(t) int sum_(i,j=1,2) K_ij(t;eta+lambda,eta)
                          U_j(eta)conj(V_i(eta+lambda))deta.       (10)

It is simply hat(v conjG)(-lambda)=c_d int hat v(eta)
conj(hat G(eta+lambda))deta, followed by (8). Schwartz decay licenses the
spatial integral for each time, uniformly on the finite interval; the
same formula holds as a Bochner H_a integral by the temporal Schur bound.
Evenness of nu_R lets us use -lambda instead of lambda in(5). Since
(2pi)^d c_d^2=1, equations(5),(10) give

 E|ell_R(I;z,w)|^2 <=int ||int sum_ij 1_I K_ij(t;eta+lambda,eta)
                  U_j(eta)conj(V_i(eta+lambda))deta||_H_a^2 nu_R(dlambda).
                                                                    (11)

This is the normalization cancellation for the actual LINEAR form; no
stationarity of its masked law has entered.

## 4. A Hilbert-valued finite Bessel step

We use a simple precise version. If {u_k} is a finite orthonormal family
in L2(R^d;C^2), and g=(g1,g2) belongs to L2(R^d;H_a^2), then

 sum_k ||int sum_j u_k,j(eta)g_j(eta)deta||_H_a^2
           <=int sum_j ||g_j(eta)||_H_a^2 deta.                     (12)

The version with conj(u_k,j) is valid as well. To prove(12), expand g in
a countable orthonormal basis of the separable H_a. For each coefficient
function apply ordinary scalar Bessel to the orthonormal family conj(u_k)
(or u_k for the conjugated version). Sum over the H_a basis and use
nonnegative Tonelli and Parseval. Scalar finite Bessel itself is the norm
identity for subtracting an orthogonal finite projection. The Bochner
integrals exist by L2 Cauchy-Schwarz. No independence of Gaussian forms
or phase components occurs here.

For each fixed lambda the kernels used in this argument lie in this L2
class. Indeed |c_r|<=1 and |b_r|<=sqrt(2)max(1,T) for all r>=0 and t in[0,T], by the
high/low sine bounds. Thus the H_a norms of 1_I K_ij are uniformly bounded
on fixed T, with t in[0,T]. These kernels are jointly continuous into
L2(0,T), hence into H_a by Schur, in their frequency parameters. Together
with continuous U,V and separability this gives the strong measurability
needed for the integrals. Multiplication by the shifted Schwartz U or V yields an L2
function in eta or xi. Subsequent integrations in lambda are of
nonnegative quantities; they may initially be extended values, whose
finiteness is proved next.

## 5. Both actual variance directions

Define the symmetric nonnegative scalar function

 Phi_h(xi,eta)=
  [<h(|xi|-|eta|)>^(a-1)+<h(|xi|+|eta|)>^(a-1)]/(<xi><eta>).

From the accepted temporal estimate, Proposition3,

 ||1_I K_ij(.;xi,eta)||_H_a^2
       <= A_T h^(2-a) Phi_h(xi,eta),
 A_T=C1(a)(1+T)^4, C1(a)=4*3^(1-a)*16/(1-a).                       (13)

All four entries satisfy this with continuous zero modes. From the accepted
scalar estimate, Proposition1, and the ACTUAL (6),

 int Phi_h(xi,xi-lambda)nu_R(dlambda)
       <=K_scalar C_nu B_alpha(h)<xi>^(-2gamma).                   (14)

All its hypotheses are met: actual nu_R is positive Radon with uniform
translated growth, the original alpha+a<2 and the stipulated strict gamma.
No physical positivity of its inverse covariance is required.

First fix w=z and V=Jz, and let U_k=Je_k be the INPUT orthonormal family.
In (11) put

 g_j^lambda(eta)=sum_i 1_I K_ij(.;eta+lambda,eta)
                                      conj(V_i(eta+lambda)).

Apply(12) and integrate lambda. Cauchy-Schwarz over the two output phase
components gives

 sum_j ||g_j^lambda(eta)||_H_a^2
 <=2 sum_ij |V_i(eta+lambda)|^2 ||1_I K_ij(.;eta+lambda,eta)||_H_a^2
 <=4 A_T h^(2-a) Phi_h(eta+lambda,eta) sum_i |V_i(eta+lambda)|^2.

Change variables xi=eta+lambda in the Lebesgue integral for each lambda,
then use nonnegative Tonelli and(14). This proves (2) with

    C_T=4 A_T K_scalar C_nu.                                      (15)

Next fix input z and U=Jz, and let V_k=Je_k be the OUTPUT family.
Change variables eta=xi-lambda in(11), and put

 f_i^lambda(xi)=sum_j 1_I K_ij(.;xi,xi-lambda) U_j(xi-lambda).

Use the conjugated version of(12). Cauchy-Schwarz over the two input
phase components now bounds its right side by

 4 A_T h^(2-a) int Phi_h(xi,xi-lambda)sum_j|U_j(xi-lambda)|^2 dxi.

After eta=xi-lambda and Tonelli, the remaining row at fixed eta is
int Phi_h(eta+lambda,eta)nu_R(dlambda). Reflect lambda using the ACTUAL
evenness of nu_R, then use symmetry of Phi_h. It becomes exactly
int Phi_h(eta,eta-lambda)nu_R(dlambda), bounded by(14) with xi=eta.
This proves (3) with the SAME (15). The two directions were derived
separately, not inferred from a scalar variance or a claim of independence.

For the stated beta range, the scalar proof's Corollary2 (or its explicit
power/log estimate) gives h^(2-a)B_alpha(h)<=C_alpha,a,beta h^(2beta).
The critical logarithm is absorbed only at STRICT beta<(2-a)/2; all
intervals above1/2 are nonempty by a<1 and alpha+a<2. Constants (15) and
this scalar factor are uniform in R, I and family size. The earlier
R-dependent fixed-compact bound was only a test-admission argument and
has not been used as the uniform estimate. This proves Proposition 1.

## 6. SAME-W mean-square columns, without a pathwise operator claim

Work on real phases. Choose a countable real Schwartz orthonormal basis
{e_k} of E_s: start with a countable dense Schwartz sequence, apply
Gram-Schmidt and discard zero residuals. Density follows, for example,
by smooth Fourier cutoffs and the usual Schwartz density in Sobolev spaces.
Schwartz phases are also dense in E_(s-gamma).

For fixed real Schwartz z define

 m_N(z)=sum_(k<=N) ell_R(I;z,e_k)e_k,
 n_N(z)=sum_(k<=N) ell_R(I;e_k,z)e_k.

Both are E_s-valued finite Gaussian sums on the SAME W. Equations(2)-(3)
and orthogonality imply that the sums of expected squares of their
coefficients are finite. Thus they converge in L2(Omega;E_s), by the
orthogonal norm identity for tails, to m(z),n(z). No independence is
needed. Their squared norms obey the bounds of Proposition1. Strong
measurability follows from the finite sums and L2 limits in separable E_s.
They are real linear maps on Schwartz phases, so by that bound they extend
uniquely and boundedly to E_(s-gamma), with values in L2(Omega;E_s).

For fixed Schwartz z,w let w_N be its E_s orthogonal projection onto the
first N basis vectors. Then <m_N(z),w>_E=ell_R(I;z,w_N). A singleton
instance of(3), after scaling w-w_N to E_s norm1 (the zero case trivial),
gives

 E|ell_R(I;z,w-w_N)|^2
      <=C_T h^(2-a)B_alpha(h)||z||_(E_(s-gamma))^2 ||w-w_N||_E^2.

This tends to zero. It proves the first equality in(4). For the second,
project z instead and use a singleton instance of(2) to control
ell_R(I;z-z_N,w). Thus both identities hold in L2 for every fixed real
Schwartz pair. They also show basis independence of the limits: the
difference of two constructions has zero pairing with a fixed countable
Schwartz orthonormal basis, hence zero L2 norm by Parseval.

Each fixed-vector limit is centered Gaussian: continuous linear
functionals and finite linear combinations are L2 limits of centered
Gaussians with convergent variances, hence their characteristic functions
converge to the Gaussian one. The same argument after the E_(s-gamma)
input extension proves the assertion for arbitrary fixed inputs and finite
families of values from m and n. This proves Proposition 2.

The scope of this construction is deterministic maps INTO L2(Omega;E_s).
It makes no assertion of an L2(Omega;B(E_s)) or HS(E_s) realization.
No common null set for every input, bounded
sample operator, norm continuity in time, Schatten sum or source-limit
statement is inferred. This is compatible with the accepted physically
masked SAME-W L2HS obstruction in d2/3.

## 7. Controls and the remaining original goal

The 120 full normalized matrix snapshots include zero frequencies and
compare with direct S(-t)B(1)S(t). Twelve generic complex Gaussian-carrier
Schwartz products compare a CLOSED-FORM Fourier value with convolution
quadrature; they are not actual wave evolution over a time interval.
Three actual singular d2 raw spatial covariance controls compare an
analytically computed marginal formula with spectral quadrature INCLUDING
(2pi)^2. The code does not numerically integrate that marginal. They test
normalizations, not (2)-(3).

Finite matrix controls use four correlated temporal cells and atomic
spatial weights that are NOT H:homog; no continuum conclusion is inferred.
v1 has only an input-basis missing-conjugate negative control; v2 adds
both directions, recorded PSD minima and Bessel residuals. Numerical
working precision50 is not certified accuracy. The only reused Lean
result is the unchanged finite full-matrix identity; new Fourier,
completion, Bessel/Gaussian/mean-square estimates are analytic, not
formalized by it. No new Lean declaration or official package is claimed.

Still open: physical localization with correctly adjointed Sobolev cutoffs,
finite Gaussian Schatten moments and compact Sobolev singular values,
actual Gaussian series and source-cutoff tails, time paths and a fixed-space
Young flow, canonical initialdata/source matching and growing cones, all-
dimensional lower bounds and sharp upper constants. Source normalization,
domain/label and conditional exact-limit questions remain open. Original
full goal ACTIVE; no correspondence, Skorohod/HPC/companion/TeX/PDF/wiki
or publication/whole-paper/cold-reader transaction is authorized by this note.
