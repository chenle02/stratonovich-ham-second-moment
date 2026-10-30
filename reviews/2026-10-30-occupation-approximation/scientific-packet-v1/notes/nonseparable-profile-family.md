# Uniform spectral and physical-wave bridge for an actual positive profile

ACCEPTED at the scoped scientific analytic/source/application gate: actual
Opus5.5/HIGH,27PASSgroups,379.661seconds,no required repairs; scientific
sourcec0a0093. Exact evidence and eight optional clarifications are in
reviews/2026-10-30-nonseparable-family/scientific-adjudication-v1.md.
Uniform estimates hold for each FIXED general nonnegative nonzero compact
psi, not only a separable test. General-test stochastic lower/variational
consumers and original sharp/source/dimensional goals remain open.

## 1. Exact objects and imported inputs

Fix original d1 positive nonzero Riesz/white Gamma with its amplitude,
0<a<1,0<alpha<=1,alpha+a<2. Fix ONE nonzero nonnegative real
psi in C_c^infinity((0,1) x R), not assumed separable. For sigma in[0,1],

 q_sigma(x)=integral_0^1 |sigma-u|^-a psi(u,x)du,
 q_avg(x)=integral_0^1 psi(u,x)du,
 h_sigma=Gamma*q_sigma, U_avg=Gamma*q_avg.                  (1)

The covariance notation h_sigma=Cov(W(sigma,.),W(psi)) is distributional
shorthand. Formula (1) defines the smooth deterministic function; it is
not evaluation of the Gaussian noise at a point. Sigma is a profile INDEX,
not a multiplicative coupling, and sigma=0 does not mean zero potential.

Imported scoped analytic inputs, not proved again:
- From notes/joint-gaussian-tilt.md Section3,(5)-(6), at its GENERAL psi
  scope: h_sigma is real smooth in space, uniformly bounded with bounded
  spatial derivatives, Lipschitz into C_b^1, and has uniform spatial C1
  tails tending to0. Covariance amplitude is retained.
- From notes/local-causal-young-flow.md Sections4-5: the fixed real Banach
  phase F is the closure of compact smooth phase vectors PLUS(1,0),(0,1)
  in uniformly local E=H1/2 x H-1/2, norm sup_j||chi_j z||E. Global E
  embeds continuously in F; compact phases alone and global E are NOT
  asserted dense in F. The free group S and bounded admissible potentials
  give the named physical wave evolution on F.
- From Teschl2014SECONDedition, with exact held source images/custody in
  reviews/2026-10-30-spectral-phase/: T10.2,p258 and vanishing-potential
  class p200-201 give self-adjointness on H2, lower boundedness, essential
  spectrum[0,infinity) and compact smooth core for real bounded potentials
  vanishing at infinity. T10.13,p273 supplies a simple positive ground
  state IF the bottom is an eigenvalue. T4.12,p141, with definition p140,
  gives MAX-MIN levels capped at the essential threshold and the common
  form-domain version. These are external inputs, not newly proved here.

For frozen sigma let H_sigma=-d2-h_sigma on H2 (complexified for spectral
statements). Let P_sigma(tau) be the PHYSICAL autonomous wave evolution
on actual F, with generator (v,w)->(w,v_xx+h_sigma v), tau>=0. Each frozen
h_sigma is admissible by the uniform C1 tails, with zero constant part
in local-flow(5.6). The accepted construction gives its strongly continuous
F flow and boundedness on each finite time horizon, uniformly in sigma
when that horizon is fixed, since the W1infinity bounds are common.
Shifting the deterministic Duhamel equation and using uniqueness gives
P_sigma(tau+s)=P_sigma(tau)P_sigma(s) for nonnegative times.
No operator-norm continuity of S in tau is assumed.

The candidate claims are exactly S1-S3 of target-v2: uniformly negative
simple ground, uniform energy/rate gap, weighted eigenfunction/derivative
bounds and actual F projection/duality/continuity, positive constant and
smooth-average entrance, and a uniform complementary physical-wave bound.
All constants may depend on THIS fixed psi,a,Gamma and the fixed partition,
not on sigma or fast propagation tau. No uniformity across tests is claimed.

## 2. A common attractive profile and uniform ground/gap

Spatial differentiation under the time integral in(1) is justified by
integrability of |sigma-u|^-a and the common compact support/derivative
bounds of psi. Thus each q_sigma is smooth compact with one spatial
support and uniform spatial derivative bounds. A nonnegative continuous
time integrand has zero integral exactly when it is identically zero,
and the kernel is strictly positive. Thus the positivity sets of q_sigma
and q_avg agree, so their spatial supports are in fact the same.
Since |sigma-u|<=1,

 q_sigma>=q_avg>=0, h_sigma>=U_avg>=0.                     (2)

The time diagonal is an integrable singularity, not an atom. Psi is
positive on an open rectangle, so q_avg is nonzero. Hence U_avg is a
nonzero nonnegative bounded continuous profile in both white and Riesz
cases. This is deterministic positive-profile order, not covariance
monotonicity on arbitrary wave phases.

Put M=sup_sigma||h_sigma||infinity>0 and
D_(sigma,s)=||h_sigma-h_s||infinity<=C_h|sigma-s|.
Every -h_sigma is in T10.2's bounded vanishing class, with common domain
H2 and essential threshold0. Choose D>=1 with
m=integral_[-D,D] U_avg(x)dx>0. Choose compact smooth chi,0<=chi<=1,
chi=1 on[-1,1], and A=integral|chi'|^2, B=integral chi^2>0.
Fix ONE R>=max(1,D,2A/m), and w_R(x)=chi(x/R). Then

 ||w_R||2^2=R B,
 <w_R,H_sigma w_R><=A/R-m<=-m/2,
 E1(sigma)=inf spectrum H_sigma<=-eps,
 eps=m/(2RB)>0, and E1(sigma)>=-M.                         (3)

The Rayleigh characterization is the n=1 case of T4.12. By the spectral
theorem the bottom belongs to the spectrum, and being below essential0
it is an isolated eigenvalue of finite multiplicity. ONLY NOW apply
conditional T10.13: it is simple with positive real normalized p_sigma,

 ||p_sigma||L2=1, lambda_sigma=sqrt(-E1(sigma)),
 l=sqrt(eps)<=lambda_sigma<=L_rate=sqrt(M).                 (4)

Reality follows by restricting the real-potential conjugation symmetry.
The H2 representative is C1 in d1 and satisfies
p_sigma''=(lambda_sigma^2-h_sigma)p_sigma, hence is C2. A zero of a
nonnegative solution would have derivative0 and uniqueness for this
continuous-coefficient ODE would force it to vanish identically. Thus
p_sigma is pointwise strictly positive, not just almost everywhere.

Define E2(sigma) by T4.12's second MAX-MIN level. It is the second negative
eigenvalue when present, and0 otherwise. Infinitely many Riesz bound states
are allowed. Simplicity and isolation give E1(sigma)<E2(sigma)<=0.
For any common unit test in H2 or the common H1 form domain, potential
comparison gives an absolute quadratic-form difference <=D_(sigma,s).
Take infima over the SAME normalized orthogonal-complement test classes,
then suprema over the SAME finite orthogonality lists as in T4.12. Thus

 |Ej(sigma)-Ej(s)|<=D_(sigma,s), j=1,2.                     (5)

No continuity of selected eigenvectors was used to obtain (5), and it
also applies when E2 hits essential0. The positive continuous difference
E2-E1 on compact[0,1] has minimum Delta>0. With
mu_sigma=sqrt(-E2(sigma))>=0,

 lambda_sigma-mu_sigma
  =(E2(sigma)-E1(sigma))/(lambda_sigma+mu_sigma)
  >=Delta/(2L_rate)=:d_rate>0.                             (6)

Denominators are positive by(4); both rates are at most L_rate. This
proves S1, including its genuinely uniform spectral data, not an assumed
gap or a per-member-to-uniform semigroup inference.

## 3. Uniform tails and continuous positive eigenfunction selection

The eigenfunction energy and ODE give

 ||p_sigma'||2^2=integral h_sigma p_sigma^2-lambda_sigma^2<=M,
 ||p_sigma''||2<=2M.

Hence H2 norms are uniform. The elementary d1 inequality
||g||infinity^2<=2||g||2||g'||2 bounds p_sigma and p_sigma' uniformly.
H1 functions have continuous representatives vanishing at infinity: use
compact smooth approximation in H1 and that same sup inequality. This
applies to p_sigma and p_sigma'.

Fix beta=l/2>0. The UNIFORM tail of h_sigma supplies one R_ext such that
h_sigma(x)<=l^2/2 for all sigma and |x|>=R_ext. Positivity then gives
p_sigma''>=beta^2 p_sigma on either exterior half-line. For x>=R_ext,
compare with p_sigma(R_ext)exp(-beta(x-R_ext)). Their difference w has
w(R_ext)=0,w(infinity)=0,w''-beta^2w>=0, so a positive interior maximum
would be impossible. Reverse x for the left half-line. Uniform boundary
values give p_sigma<=C exp(-beta|x|). The ODE gives the same bound for
|p_sigma''|; integrating it from the appropriate infinity using p_sigma'->0
gives it for |p_sigma'|. Enlarging C on the common interior yields

 |p_sigma|+|p_sigma'|+|p_sigma''|<=C exp(-beta|x|),            (7)

with C independent of sigma. No individual Agmon/Simon constant is being
assumed uniform; (7) is a direct common exterior comparison.

Let Q_s^L2 be the orthogonal complement of p_s on L2, distinct from the
wave complement. On it H_s-E1(s) has spectral lower bound Delta, so

 ||Q_s^L2 p_sigma||2
  <=Delta^-1||(H_s-E1(s))p_sigma||2<=2D_(sigma,s)/Delta.

The exact residual is [E1(sigma)-E1(s)+h_sigma-h_s]p_sigma, with the
correct sign. Positivity and normalization give overlap b=<p_sigma,p_s>
in(0,1] and
||p_sigma-p_s||2^2=2(1-b)<=2(1-b^2)=2||Q_s^L2 p_sigma||2^2.
Subtract the two ODEs: the second derivative of their difference is a
uniformly bounded coefficient times that difference plus a coefficient
of sup norm <=2D_(sigma,s) times p_s. The L2 bound above therefore
also bounds its second derivative by C D_(sigma,s); its first derivative
follows by integration by parts or xi^2<=1+xi^4. Consequently

 ||p_sigma-p_s||H2<=C D_(sigma,s),
 |lambda_sigma-lambda_s|<=D_(sigma,s)/(2l).                 (8)

The positive normalization fixes the phase globally. This proves the
required continuous selection and more, with no changing Hilbert spaces.

## 4. Exact local duals, full wave projection and linear average

Use the FIXED chi_j and smooth partition rho_j of local-flow Section4,
supp rho_j in[j-1,j+1],chi_j=1 there. Uniform (7) gives
||rho_j p_sigma||H1<=C exp(-beta|j|). For z=(v,w) in F DEFINE

 <p_sigma,v>=sum_j <rho_j p_sigma,chi_j v>,
 <p_sigma,w>=sum_j <rho_j p_sigma,chi_j w>.                 (9)

The first uses H-1/2--H1/2 duality and the second H1/2--H-1/2 duality;
H1 bounds of the compact test control either required norm. Both series
converge absolutely and have absolute value <=C||z||F, uniformly in sigma.
They agree with global E pairings and ordinary integrals for constants.
Independence of the partition follows by agreement first on compact smooth
phases PLUS both constants, then their DEFINING density in F. Compact
phases alone and E are not assumed dense in F.

A centered cutoff kappa_D, equal1 on[-D,D],supported in[-D-1,D+1], with
uniform first derivatives, gives the uniform local-dual tail bound

 |<p_sigma,(1-kappa_D)v>|+|<p_sigma,(1-kappa_D)w>|
                  <=C exp(-beta D)||z||F.                 (10)

Only cells |j|>=D-1 contribute, and their geometric sum proves it.

Define the full two-entry objects

 e_sigma=(p_sigma,lambda_sigma p_sigma),
 ell_sigma(v,w)=(<p_sigma,v>+<p_sigma,w>/lambda_sigma)/2,
 Pi_sigma=e_sigma ell_sigma.                              (11)

Global E->F embedding, H2 bounds, (4),(9) give common bounds on e_sigma,
ell_sigma and Pi_sigma. Normalization gives ell_sigma(e_sigma)=1 and
ell_sigma(p_sigma,-lambda_sigma p_sigma)=0, hence Pi_sigma^2=Pi_sigma
and the DECAYING ground partner remains in the complement. Velocity and
the reciprocal lambda in (11) are essential and are retained. Also

 ell_sigma(e0)=(1/2)integral p_sigma
       >=1/(2 sup_s||p_s||infinity)>0.                     (12)

Indeed 1=integral p_sigma^2<=||p_sigma||infinity integral p_sigma,
and the integral is finite by(7). Equations (8),(10) show e_sigma is
continuous in F and ell_sigma in F* norm: for fixed D the finite local
core tends to0 with ||p_sigma-p_s||H2, while the tail is uniformly small
as D grows. Lambda and its reciprocal are uniformly continuous by(8).
Thus Pi_sigma is operator-norm continuous as well. Compactness gives
uniform continuity; no fast-time norm continuity of S is inferred.

For fixed real nonnegative smooth compact phi of integral1 DEFINE

 J_phi(v,w)=<v,phi>,                                      (13)

the UNSQUARED real LINEAR displacement-only functional. It ignores w;
this does not remove w from the phase/projection (11). A compact cutoff
chi=1 near supp phi has ||chi z||E<=C_phi||z||F by local-flow(4.2), so
H1/2--H-1/2 duality makes (13) bounded and independent of the cutoff.
It is distributional testing, never point evaluation. Since p_sigma is
pointwise positive, J_phi(e_sigma)=integral phi p_sigma>0. Its continuity
in sigma and compactness give inf_sigma J_phi(e_sigma)>0.

For forward invariance, each frozen h_sigma is smooth with bounded spatial
derivatives. Compact smooth AND constant initial phases have classical
solutions with bounded derivatives on every finite horizon, by d1Duhamel
iteration (kernel mass tau-u) and its differentiated equations. The same
Picard iterates agree with the named F integral equation; F convergence
and continuous distribution testing identify the classical solution with
P_sigma, including constants. For a(tau)=integral p_sigma u(tau), (7)
justifies differentiation and integration by parts, giving a''=lambda_sigma^2 a.
Thus (a+a'/lambda_sigma)/2 evolves by exp(lambda_sigma tau). Extend the
functional identity from that dense class to F by boundedness. The exact
eigenphase solution e^(lambda_sigma tau)e_sigma is identified by the same
F uniqueness. Therefore for all sigma in[0,1],tau>=0,

 P_sigma(tau)Pi_sigma=Pi_sigma P_sigma(tau)
                         =exp(lambda_sigma tau)Pi_sigma. (14)

This proves S2. It is a pointwise flow identity plus NEWuniform dual and
continuity estimates, not a uniformity claim borrowed from fixed-q gates.

## 5. Uniform fractional phase and global complementary bound

Let c=1+M,A_sigma=H_sigma+c and B0=1-d2. On the common H1 form domain,

 B0<=A_sigma<=cB0, A_sigma>=1.                            (15)

Use the GENERIC positive-operator comparison argument proved in accepted
notes/spectral-complement-transfer.md Section2: inverse variational forms
reverse order for (A+t)^-1, and integrating the positive quadratic forms
of I-t(A+t)^-1 against t^-1/2/pi yields the square-root order. Monotone
spectral integration includes domain finiteness, so (15) implies

 D(A_sigma^1/4)=H1/2,
 ||B0^1/4 v||2<=||A_sigma^1/4 v||2<=c^1/4||B0^1/4 v||2.

Its Hilbert dual identifies the completion in ||A_sigma^-1/4 w||2 with
H-1/2. Thus E_sigma with squared norm
||A_sigma^1/4 v||2^2+||A_sigma^-1/4 w||2^2 is uniformly equivalent to
GLOBAL E. These applications have common c independent of sigma; no
per-member equivalence constant is silently declared uniform.

On Q_sigma^L2, spectrum H_sigma lies in[-mu_sigma^2,infinity). Under the
isometry to two unweighted L2 coordinates, the spectral wave matrix has
entries C_tau(xi),sqrt(xi+c)S_tau(xi),-xi S_tau(xi)/sqrt(xi+c),C_tau(xi).
Here C=cos(tau sqrt(xi)),S=sin(tau sqrt(xi))/sqrt(xi) for xi>0, C=1,S=tau
at0, and cosh/sinh continuations for xi<0. For xi>=0 use
|S|<=min(tau,xi^-1/2), split xi<=1 and xi>=1 for the upper off-diagonal;
the lower is bounded by1. For xi<0 use |S|<=tau exp(mu_sigma tau),
|C|<=exp(mu_sigma tau),|xi|<=M and xi+c>=1. All four entries are therefore
<=C(1+tau)exp(mu_sigma tau), with common C. The threshold mu=0 causes
no inverse-mu division. The remaining ground branch after I-Pi_sigma is
the decaying (p,-lambda p) phase, with uniform projections because
l<=lambda<=L_rate and 1<=c-lambda^2<=c. Consequently

 ||P_sigma(tau)(I-Pi_sigma)||E->E
                   <=C(1+tau)exp(mu_sigma tau).            (16)

To identify this spectral flow with the ACTUAL physical F flow on E,
start with compact smooth data in H2 x H1. The same matrix bounds at
these higher A-scales give a strong solution and the free Duhamel equation.
It is continuous into E, hence F, where B(h_sigma) is bounded. Uniqueness
of that Duhamel equation is Picard/Gronwall in F. Extend equality to all
E using density in E, E->F embedding and finite-horizon F bounds. This
uses no assertion that the physical F flow is a priori E-valued and no
E density in F. The full spectrum is used for the identification on a
finite horizon (replace mu by lambda there); only the complement uses mu.

## 6. Actual F transfer with the growing projection tail retained

The physical frozen flow has speed1. Indeed free propagation expands
support by at most its time increment, multiplication by h_sigma is local,
and each Duhamel Picard term has that support property. The series converges
in F on each finite horizon. Continuous distribution testing passes support
to its limit, including for constant data after local cutoff comparison.
No support is inferred from an E-adjoint.

Choose kappa_(j,tau)=1 on[j-tau-4,j+tau+4], supported in the interval
with radius tau+5, with uniform derivative bounds. The fixed partition
expands kappa z into <=C(1+tau) compact localized E terms, so

 ||kappa_(j,tau)z||E<=C(1+tau)||z||F.

Finite propagation gives chi_j P_sigma(tau)z=chi_j P_sigma(tau)(kappa z).
Set R_sigma(tau)=P_sigma(tau)(I-Pi_sigma). With (14) this gives EXACTLY

 chi_j R_sigma(tau)z=chi_j R_sigma(tau)(kappa z)
      +exp(lambda_sigma tau)chi_j e_sigma ell_sigma((kappa-1)z). (17)

The second term cannot be discarded. The first term is bounded in E by
C(1+tau)^2 exp(mu_sigma tau)||z||F, by(16). From(7),
||chi_j e_sigma||E<=C exp(-beta|j|). For the missing-input coefficient,
a contributing partition cell k satisfies |k-j|>=tau+3, hence
|k|>=tau+3-|j|. The same geometric local-dual sum as(9)-(10) yields

 |ell_sigma((1-kappa_(j,tau))z)|
       <=C exp(-beta(tau-|j|)_+)||z||F.

This includes distant |j|>tau cells, where the full dual bound suffices.
Since |j|+(tau-|j|)_+>=tau, the second term of(17) is at most
C exp((lambda_sigma-beta)tau)||z||F. Take the supremum over j in the
ACTUAL F norm. Both P_sigma and Pi_sigma already preserve F, so membership
of the output is known, and the estimate is

 ||R_sigma(tau)||F->F<=C[(1+tau)^2 exp(mu_sigma tau)
                              +exp((lambda_sigma-beta)tau)]. (18)

All constants are common, from M,l,L_rate,Delta,beta, the uniform tails
and fixed partition; none is an unspecified per-q constant. Choose
eta=min(d_rate,beta,l)/2>0, so eta<inf_sigma lambda_sigma. By(6), both
exponents in(18) are <=lambda_sigma-2eta. Finally
(1+tau)^2 exp(-eta tau)<=2+4/eta^2, from the quadratic lower bound on
exp(eta tau). Enlarging the common constant to >=1 proves for all
sigma in[0,1],tau>=0,

 ||P_sigma(tau)(I-Pi_sigma)||B(F)
                       <=C exp((lambda_sigma-eta)tau).     (19)

This proves S3 and the candidate uniform actual-family bridge.

## 7. Falsification, formal boundary and later consumer

The independently verified short white witness in
reviews/2026-10-30-nonseparable-family/falsification-v1.md shows that this
family cannot generally be written b(sigma)U. It refutes that EXACT
representation only, not optimizer sufficiency or any moment conjecture.
The revised preproof audit explicitly checked the first-entry linear J_phi
repair; the original failed audit remains unaccepted and preserved.

New content here is analytic class/source/uniformity, ODE, Sobolev and
spectral reasoning, not a new finite combinatorial identity. Existing local
scalar kernels do not certify these conclusions. No spectral/Young
foundation, desired-bound axiomatic shell, private companion/package or
cluster job is created. Full scientific analytic/application review remains
REQUIRED before S1-S3 adoption or use in a general-positive-profile event.

After adoption one must CHECK the moving-cone hypotheses for this indexed
family and prove the actual masked zeta_r h(delta u) block approximation,
including slow-profile freezing, uniform Riesz C1mask error and the last
partial-block extension. Then re-establish the actual same-residual event
and raw-cost lower consumer for general positive psi; none is claimed here.
Optimizer/source correspondence, signed-profile issues, intended source
normalization, original higher dimensions, sharp upper constant and whole-
paper/novelty/circulation clearance remain open. Canonical TeX/PDF unchanged.
