# Nonlinear block comparison with the deterministic physical growth retained

ACCEPTED at the scoped FULL analytic/source/type/application gate:
scientificcdf2056,24checks/HIGH388.122seconds, no required repairs.
Six optional clarity notes adjudicated in
reviews/2026-10-31-upper-young-perturbation/scientific-adjudication-v1.md.
Frozen proof/report unchanged. FixedR nonlinear operator control only,
not the original point-moment sharp upper. The full all-dimensional/source
completion contract remains ACTIVE.

## 1. Exact statements and direct inputs

Local notation distinguishes the raw Hilbert space H from a path H by
its domain, the radius R from the inverse path R in Section3 and the
scalar R_delta,J by context. G_B is the free-group norm; C_B the accepted
primitive constant; c_B the new crude bad-block cost. These are distinct.
Write ||D||theta=sup_t||D(t)||+[D]_theta for operator paths. All spaces
and noises are real. First let F be any nonzero Banach space and use its
induced norm on B(F). Fix B>=1,1/2<theta<1,nu=1/theta. For a path D starting
at0 let U_D be the LEFT Young evolution
 U_D(t)=I+int_0^t dD(s)U_D(s).

**E1.** For every K>=1 there is C(theta,B,K)<infinity, independent of the
Banach dimension, such that for ||H||theta<=K, X(0)=H(0)=0, x=||X||theta,

 ||A U_(H+X)(t)||<=||A U_H(t)|| exp(C(theta,B,K)(x+x^nu))       (1)

for all bounded A:F->F and0<=t<=B, including noninvertible A and A=0.
There is no extra factor at x0.

For E2-E4 use EXACTLY accepted upper-cameron-compactness.md C3 (12)-(15)
and upper-residual-exponential.md PropositionD1. Original nonzero H:homog
Gamma and amplitude, dimensions d=1,2,3, a=alpha_0 in(0,1), admissible
alpha+a<2, fixed spatial mask m_R=eta_R² ONCE, F=E directsum R² with
E=H^(1/2)xH^(-1/2). Use the same supported raw H=H_I, GIVEN W, compact
mean T:H->Lr(I;K(F)), basis e1,e2,... and P_J onto its FIRST J vectors
(empty if J0), Q_J=I-P_J. The ranges are exactly
 1/2<theta<min(1-a/2,(3-a-alpha)/2),
 1/(1-theta)<r<2/a, nu=1/theta<=p<2<r.
Fix integer B>=1,0<delta<min(1,1/B), N=floor(1/(delta B)),n=N+1,
s_m=m delta B, true last lengths ell_m, intervals I_m as in C3.

OWN direct accepted inputs, not recertified here:
- fixed-mask-young-constant-phase.md Sections2-4: exact free S_F, constants,
  actual F extension, Banach Young local estimates/invertibility/stability.
- C3: actual raw restricted Gaussian tuple/covariance, supported coefficients,
  compact mean T, B0=h0theta([0,B];K(F)), stopped constant extensions.
- D1: actual residual X_delta,J=(X_m), exact norm
  Y=(delta sum_m||X_m||theta^p)^(1/p), b=2EY<=C g_delta,
  g_delta=delta^((1-a)/2), and finite-delta/exponential bounds (3)-(5).
- source-operator-convergence.md Theorem1: linear Gaussian transfer and
  same-noise limits. D1(8) provides the finite-head regression identity too.

Imported integration input: PRIMARY Friz-Hairer2020 Section4.1(4.1)-(4.3),
printed61-62, and Section1.5,printed13. Required images and selected text
are in reviews/2026-10-31-upper-young-perturbation/. It gives Banach Young
existence/continuity and the local remainder with exponent2theta>1.
The exact nonlinear consumers below are derived here, not attributed to
the book. No analytic-semigroup or bounded nonlinear-vector-field theorem
is used for the wave phase.

For Phi in H, define deterministic paths, stopped at ell_m and constantly
extended, by
 H_m(Phi)(u)=int_0^min(u,ell_m)
       S_F(-v)T Phi(s_m+delta v)S_F(v)dv,
 a_m=C_B delta^(-1/r)||T Phi||Lr(I_m),
 D_M=C_B^r||T||^r M^r,  M>0 fixed.                           (2)

For zero-started paths x_m in B0 with pi_C x_m=0 put
 P_m(Phi,x_m)=S_F(ell_m)U_(H_m(Phi)+x_m)(ell_m),
 P_m^0(Phi)=S_F(ell_m)U_(H_m(Phi))(ell_m),
 z(Phi,x)=product_m ||P_m(Phi,x_m)||/||P_m^0(Phi)||.          (3)

**E2.** If ||Phi||H<=M, then ||H_m(Phi)||theta<=a_m,
delta sum a_m^r<=D_M, and ||P_m^0(Phi)||>=1. For K>=1 there are constants
c_B depending on theta,B (and the fixed free group), INDEPENDENT OF K,
and C_K depending on theta,B,K and the same fixed free group, all independent of
J,delta,Phi,M, such that

 log max(1,z(Phi,x))
 <=C_K sum_m(v_m+v_m^nu)+c_B sum_(a_m>K)(1+a_m^nu),
 v_m=||x_m||theta,
 delta sum_(a_m>K)(1+a_m^nu)<=D_M(K^-r+K^(nu-r)).             (4)

Define A_m(W) to be the FULL fast driver transferred from f->W(T_(delta,m)f),
with mask m_R, genuine F extension, stopped at ell_m and constantly
extended, BEFORE multiplication by g_delta. The actual head identity is

 g_delta A_m(W)=H_m(Phi_delta,J)+X_m,
 Phi_delta,J=sqrt(delta)sum_(j=1..J)W(e_j)e_j.                (5)

**E3.** For every fixed q>0 let
 R_delta,J=sup_(||Phi||H<=M) E[max(1,z(Phi,X_delta,J))^q].
Then R_delta,J is finite and
 lim_(J->infinity)limsup_(delta->0)delta log R_delta,J=0.     (6)
The integrand is jointly Borel in Phi and the tuple; expectation is a
Borel function of Phi. Sup is OUTSIDE expectation.

**E4.** With G=(W(e_1),...,W(e_J)), the actual tuple is independent of G,
and, on ||Phi_delta,J||<=M,
 E[max(1,z(Phi_delta,J,X_delta,J))^q | G]<=R_delta,J           (7)
almost surely. No time-block independence or uncountable-head common null
set is assumed. Statements (5) and (7) have different roles: (5) identifies
the actual blocks; (7) is the conditional error bound.

## 2. Refined Young growth and uniform inverse bounds

Let c_theta=2max(1,C_theta), where C_theta is the PRIMARY Young remainder
constant. On a piece of length ell, the complete norm
 N_ell(V)=sup||V||+ell^theta[V]_theta satisfies, as derived in the accepted
fixed-mask Section4(6a),
 N_ell(int_a^. dD V)<=c_theta[D]_theta ell^theta N_ell(V).     (8)
All constants arise from bounded multiplication with norm1, so they are
dimension free. Put d=||D||theta. If c_theta d B^theta<=1/4, contraction
on the whole interval, including arbitrary initial data, gives
 sup||U_D||<=1/(1-c_theta d B^theta).
Hence log sup||U_D||<=2c_theta B^theta d, since -log(1-u)<=2u for u<=1/4.
If c_theta d B^theta>1/4, choose
 n_D=ceil(B(4c_theta d)^nu), ell=B/n_D.
Then n_D>=1 and each piece has contraction ratio<=1/4; its evolution
norm is at most4/3. Also B(4c_theta d)^nu>1, so
 n_D<=2B(4c_theta d)^nu.
Patching by uniqueness therefore gives log sup||U_D||<=C(theta,B)d^nu.
For d0 the solution is I. Combining the cases proves the refined bound

 sup_(t<=B)||U_D(t)||<=exp(c(theta,B)(d+d^nu)).               (9)

In particular there is ZERO growth cost at d0; the crude prefactor in
fixed-mask(7) would not have this property and is not used on good blocks.

For ||H||theta<=K choose one uniform partition with local contraction
ratio<=1/4, depending only on theta,B,K. On each piece the local evolution
Q satisfies sup||Q-I||<=1/3 by (8) and N_ell(Q)<=4/3, so Q is invertible
by the norm-convergent Neumann series and sup||Q^-1||<=3/2. Products give
uniform bounds for U=U_H and U^-1 over the whole horizon. Equation(8)
also bounds the local Holder seminorm of U by a constant times K and its
initial norm. For pairs crossing a boundary at distance less than ell,
split into the at most two pieces and use
 h1^theta+h2^theta<=2^(1-theta)(h1+h2)^theta.
For larger distances use2sup||U||/ell^theta. Thus ||U||Ctheta is uniformly
bounded. The exact identity

 U^-1(t)-U^-1(s)=-U^-1(t)(U(t)-U(s))U^-1(s)

bounds its Holder seminorm too. Consequently

 ||U_H||Ctheta+||U_H^-1||Ctheta<=L(theta,B,K).                (10)

Neither a matrix dimension nor rank enters. This proves the asserted
inverse control rather than merely pointwise invertibility.

## 3. Young conjugation and the multiplicative estimate

We spell out the product argument with remainders, avoiding smooth density
in the full Holder norm. Set U=U_H, R=U^-1 and
 G(s)(Z)=R(s) Z U(s), a bounded linear map B(F)->B(F).
It is theta-Holder in this operator norm, with
 sup||G||<=sup||R||sup||U||,
 [G]_theta<=[R]_theta sup||U||+sup||R||[U]_theta.
Thus (10) and the PRIMARY Young estimate construct the zero-started path

 Z(t)=int_0^t R(s)dX(s)U(s),  ||Z||theta<=L'(theta,B,K)x.     (11)

Indeed Z_(s,t)=G(s)X_(s,t)+O(|t-s|^(2theta)); its sup and seminorm bounds
follow by dividing the remainder by |t-s|^theta, using |t-s|<=B.
Here (11) means the ordinary Banach Young integral of the linear-map
integrand G against X; no tensor product or scalar commutation is used.

Let V=U_Z. The Young remainders give, uniformly on the fixed horizon,
 U_(s,t)=H_(s,t)U(s)+O(|t-s|^(2theta)),
 V_(s,t)=Z_(s,t)V(s)+O(|t-s|^(2theta)).
For P=UV the exact finite-product increment has a cross term
U_(s,t)V_(s,t), of order2theta. Substituting (11) gives

 P_(s,t)=H_(s,t)P(s)+U(s)R(s)X_(s,t)U(s)V(s)
                         +O(|t-s|^(2theta))
         =(H+X)_(s,t)P(s)+O(|t-s|^(2theta)).                 (12)

Summing over an arbitrary partition of any interval, all remainders vanish:
sum |t_i-t_(i-1)|^(2theta)<=B mesh^(2theta-1)->0. The left-point sums
converge to the Young integral, so P solves the equation driven by H+X.
Uniqueness, already supplied by the local contraction, yields

 U_(H+X)(t)=U_H(t)V(t).                                     (13)

This proves the needed product/associativity step with the correct LEFT
order. More generally, replacing increments of a Young primitive by their
first-order Young models in an iterated integral has the same vanishing
sum of2theta remainders; this is the associativity used in (12). There is
no quadratic correction. If desired the inverse differential follows by
the same product expansion of R U=I, namely dR=-R dH, with multiplication
in the displayed order; only the inverse identity in (10) was needed here.

Apply (9) to Z and use (11):
 ||V(t)||<=exp(C(theta,B,K)(x+x^nu)).
Left multiplication of (13) by any A and submultiplicativity prove (1),
including A0 and noninvertible A. This proves E1.

## 4. Actual mean paths, retained head and physical baseline

The deterministic primitive in (2) is the SAME bounded map on Lr as C3
(12), without its sqrt(delta) factor. C3 (13) therefore gives
 ||H_m(Phi)||theta<=C_B delta^(-1/r)||T Phi||Lr(I_m)=a_m.
Constant extension preserves the norm, including an empty final interval.
Since the I_m partition I up to endpoints,

 delta sum_m a_m^r=C_B^r||T Phi||Lr(I)^r<=D_M.                (14)

This is an averaged budget for arbitrary Phi; individual a_m may diverge.
There is no J in (14). For the random head below, boundedness is imposed
only by the explicit cutoff ||Phi_delta,J||<=M, not by writing it as the
projection of an already bounded raw vector.

To prove (5), split every literal fast noise test on the GIVEN W as
 W(T_(delta,m)f)=W(P_J T_(delta,m)f)+W(Q_J T_(delta,m)f).
Accepted Gaussian transfer is linear for these jointly Gaussian noises;
its finite sums and their Lp path limits preserve this identity, including
the bounded F extension. The first term is a finite raw Gaussian head:
for every path statistic ell its value is W(P_J k_ell), a finite sum in
the W(e_j). Also E[X_m W(e_j)]=0 because every residual coefficient has
Q_J before its raw test. Thus the head coefficients equal the full
coefficients, and no residual-head covariance is left.
Its coefficient for W(e_j), after multiplication by g_delta, is the actual
Bochner covariance E[g_delta A_m(W) W(e_j)]. By C3 (12) at residual rank0
that coefficient is sqrt(delta)H_m(e_j). Hence the head is exactly
H_m(Phi_delta,J). This also agrees with D1(8)'s finite-head regression.
Countable norming path statistics (dense unit states and rational times)
identify the path identity, not just a scalar law. There are finitely many
m, so (5) holds for the whole tuple on one event for each fixed delta,J.
No event uniform over all uncountably many delta or source parameters is
claimed. No bound on the size of Phi_delta,J is used for the identity.

The multipliers T Phi(s) have range in closed iE, and S_F preserves iE.
Bochner integrals therefore give pi_C H_m(Phi)=0 as operator paths. Applying
pi_C to the Young Riemann sums of the mean equation gives
pi_C U_(H_m)=pi_C. Consequently

 pi_C P_m^0=tau(ell_m)pi_C,
 tau(t)=[[1,t],[0,1]].                                      (15)

The constant-displacement input e_disp=(0_E,1,0) has norm1 in F; its output
constant coordinate remains(1,0), of norm1. Orthogonality of the direct sum
gives ||P_m^0||>=1, even when ell_m0 and P_m^0=I. This lower bound uses the displacement column. Both actual constant
columns and their free evolution are retained in F and in H_m; no density
of E in F is assumed.
The actual residual X_m starts at0 and has pi_C X_m=0 by closedness of the
F extension's range. This latter property is compatible with the arbitrary
x_m class, although only the mean property was needed for the denominator.

## 5. Good/bad mean-block comparison and finite-type reuse

Fix K>=1. If a_m<=K, use E1 with A=S_F(ell_m), t=ell_m. The exact physical
endpoint is retained and gives

 log(||P_m(Phi,x_m)||/||P_m^0(Phi)||)
                       <=C(theta,B,K)(v_m+v_m^nu).          (16)

If a_m>K, use sup_(t<=B)||S_F(t)||=G_B and the crude consequence of (9)
for ||H_m+x_m||theta<=a_m+v_m. Since nu>1, y<=1+y^nu and
(a+v)^nu<=2^(nu-1)(a^nu+v^nu), we obtain
 log||P_m(Phi,x_m)||<=c_B(1+a_m^nu+v_m^nu),                 (17)
with c_B independent of K,J,delta,Phi,M. Increase it to a positive constant
if necessary. Dividing by the baseline>=1 cannot increase this upper bound.
Choose C_K at least c_B and the good-block constant. Summing (16)-(17),
then using the nonnegative right side, proves the first assertion of (4).
On bad blocks a_m>K>=1 and r>nu give
 1<=K^-r a_m^r,  a_m^nu<=K^(nu-r)a_m^r.
Their sum with (14) proves the second assertion of (4). This proves E2.

For E3 we will also use the precise finite Holder inequality

 delta sum_m v_m^nu<=(delta n)^(1-nu/p)Y^nu.                 (18)

The previously audited EXISTING Mathlib
Real.rpow_sum_le_const_mul_sum_rpow_of_nonneg has exponent kappa>=1,
nonnegative f_m, and cardinality n. Here kappa=p/nu>=1, f_m=v_m^nu>=0,
n=N+1>=1. It gives (sum v_m^nu)^(p/nu)<=n^(p/nu-1)sum v_m^p.
Raising to nu/p>0 and multiplying by delta yields (18); all zero bases
have strictly positive exponents and n>0. If nu=p it is equality. This
is the exact actual finite application, not an analytic theorem formalized
in Lean; no new kernel source, theorem or count is introduced.

## 6. Uniform residual exponential estimate on a bounded control ball

At fixed delta,J the maps Phi->H_m(Phi) are bounded linear into B0; the
primitive estimate gives continuity. The accepted Young solution map is
locally Lipschitz in the driver on bounded balls, hence continuous. The
endpoint multiplication and operator norm are continuous, and every
denominator in (3) is at least1. Thus
 (Phi,x)->max(1,z(Phi,x))^q
is jointly continuous on the SEPARABLE supported Hilbert space H times
the zero-started closed subspace of the SEPARABLE finite product B0^n
with pi_C x_m=0. Extending its definition to arbitrary zero-started B0
residuals uses exactly the same formulas (no residual range property is
needed for the denominator). Strong measurability of the actual tuple
then makes it a jointly Borel integrand. Nonnegative Tonelli makes its
expectation a Borel function of Phi. No random supremum is taken.

For tau>0 and v>=0 we have
 v<=tau+tau^(1-nu)v^nu: for v<=tau use the first term, and for v>tau
use v^(nu-1)>=tau^(nu-1). Equations(4),(18) and delta n<=2/B therefore give,
UNIFORMLY over ||Phi||<=M,

 delta log E[max(1,z(Phi,X_delta,J))^q]
 <=q c_B D_M(K^-r+K^(nu-r))+(2q C_K/B)tau
                  +delta log E exp(eta Y^nu/delta),
 eta=q C_K(1+tau^(1-nu))(2/B)^(1-nu/p).                     (19)

All factors are finite positive except potentially the last expectation;
D1(3) proves that expectation finite. Since the bound is independent of
Phi, the SAME bound holds for delta log R_delta,J. Taking the supremum
outside expectation preserves this bound; log is increasing. Also R>=1.
D1 gives the fully finite bound if desired by replacing the last term with
 2^(nu-1)eta b_delta,J^nu
 +A_nu eta^(2/(2-nu))(C0 epsilon_J)^(2nu/(2-nu))+delta log2,
where all symbols are EXACTLY D1's fixedR quantities. In particular eta is
independent of J and delta at fixed theta,B,q,K,tau, as required.

For each fixed K,tau take limsup as delta->0, using b_delta,J->0. Then
let J->infinity; epsilon_J->0 removes the residual term. This gives

 0<=limsup_(J->infinity)limsup_(delta->0)delta log R_delta,J
 <=q c_B D_M(K^-r+K^(nu-r))+(2q C_K/B)tau.                   (20)

Now tau->0 with K fixed removes the second term even if C_K grows rapidly
with K. Finally K->infinity removes both remaining powers because r>nu>0
and c_B is INDEPENDENT K. Nonnegativity shows both outer liminf and limsup
are0, proving the ordinary iterated limit (6). This proves E3.
No rate comparison C(J,M)epsilon_J^c, joint limit, or exchange of the order
has been used. M,B,R remain fixed.

## 7. Actual Gaussian head conditioning and scope of the product

For fixed delta,J, Gaussian transfer constructs each X_m as an Lp limit
of finite operator-path sums whose scalar coefficients are
 W(Q_J T_(delta,m)f_k).
Therefore the tuple is measurable for the completed sigma field generated
by W(Q_J H_W). A subsequence converging almost surely in the finite
separable product makes this measurability explicit. Every finite Gaussian
subfamily of this field is orthogonal to W(e_1),...,W(e_J), hence independent
of that vector. The countable separable coordinate construction and a
monotone-class argument extend independence to the tuple; completing sigma
fields changes no almost-sure probability identities. This is unrelated
to disjoint time support; all the block residuals can remain correlated.

Let mu_X be the law of the tuple. For g in R^J set
 Phi(g)=sqrt(delta)sum_(j<=J)g_j e_j,
 f(g,x)=max(1,z(Phi(g),x))^q,
 psi(g)=int f(g,x)mu_X(dx).
The joint Borel property from Section6 and nonnegative Tonelli show psi
is Borel. Independence gives the product law of (G,X). Testing against
bounded nonnegative Borel functions of g and applying Tonelli proves the
freezing identity

 E[f(G,X)|G]=psi(G)                                        (21)

in the extended nonnegative sense. On ||Phi(g)||<=M, psi(g)<=R_delta,J by
definition. Thus (21) proves (7), with a version chosen through this one
Borel psi; no intersection of uncountably many null sets is taken. J0 is
the empty head, with the same assertion unconditionally. This proves E4.
The actual-block identification (5) then tells which physical operators
are being compared, rather than supplying independence itself.

For any finite ordered product of the displayed physical blocks,
 ||P_N ... P_0||<=product_m||P_m||
              <=max(1,z(Phi,x)) product_m||P_m^0(Phi)||.     (22)
This is submultiplicativity, not equality of norms. This note does NOT
prove an additional global raw-noise restart identity, bound the final
deterministic product sharply, or handle the Gaussian action complement
{||Phi_delta,J||>M} and passage M->infinity. Those are separate obligations.

## 8. Evidence, boundaries and the original target

Falsification preceded proof:15 exact nilpotent smooth-matrix rows include
six nontrivial cases distinguishing the LEFT conjugation and product order
and nine zero cases only. Three distinct left multipliers over those rows
give45 submultiplicativity checks, not independent tests of the unknown C.
The induced linfinity norm is a full Banach operator norm, not maximum
entry; the ones matrix separates them. These generic smooth controls did
not test the actual S_F baseline, partial-block clock or general Holder
x+x^nu bound; those are derived in Sections2-5. Four inherited scalar ODE
checks refute pure-nu cost, and four rare-block budgets refute a uniform
maximum-block claim. No actual CM realizability or SPDE numerical evidence.

The primary selected images show printed13,61-62 and the actual Young
estimate(4.3). This is standard calculus applied here, no method novelty.
Upstream accepted input fit is explicit, not a new full-source audit.
The finite powermean application is scoped separately:73finitefacts19local
seams/L0 unchanged. Gaussian, Young, spectral and SPDE arguments are informal,
not formalized by a finite inequality. Official companion decision4 pending.

E1-E4 retain the actual full F phase, velocity column, fixedR given-W tuple
and original all-Gamma model. They leave OPEN the sharp signed deterministic
spectral/variational upper, growing cone/localization/entropy, original point
upper/source limits, intended author-energy normalization and exact limit.
The accepted white translated-control guard still forbids uniformR tails
for fixed finite smooth projections. No F3 reversal, point Sobolev trace,
raw traceclass/L2 Gaussian field, time-block/heat-error independence,
Skorohod proof, source repair, human correspondence, HPC, companion creation,
canonical TeX/PDF/wiki/bib integration or public release has occurred.
