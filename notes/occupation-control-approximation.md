# Positive occupation controls and exact smooth-test approximation

ACCEPTED at the scoped scientific analytic/type/application gate: actual
Opus5.5/HIGH,8PASS/PASS_WITH_NOTES groups,272.897seconds,no requiredrepairs;
scientific source80e47d6. Exact evidence and seven optional clarifications
in reviews/2026-10-30-occupation-approximation/scientific-adjudication-v1.md.
Positive rough-control approximation, original-point lower and equality
of raw variational suprema hold in the stated X class, which includes
finite-energy occupation densities. Original sharp/source/dimensional
goal and intended normalization remain open.

## 1. Actual model, functional class and accepted inputs

Fix original real d1 Gamma with its positive amplitude: Riesz
Gamma(dx)=c_Gamma|x|^-alpha dx for0<alpha<1, or white
Gamma=c_Gamma delta_0 atalpha=1. Fix0<a<1,alpha+a<2. In particular
|x|^-1 dx is NOTthe white endpoint. All norms/spaces below are real.
Let B=L1(R) intersect L2(R), with norm ||f||B=||f||1+||f||2, and
X=L2((0,1);B), using Bochner strong measurability. B is a separable
Banach space: a Cauchy sequence converges in L1 and L2, the limits agree
locally in measure, and the diagonal image in the separable product
L1 x L2 is closed. Thus the sum norm is complete and separable.
Let X_pos consist of nonnegative nonzero equivalence classes in X.

Choose jointly measurable representatives for psi in X: approximate its
Bochner representative by simple B-valued functions in X, and choose a
subsequence converging almost everywhere on each finite spacetime box
using the local spacetimeL1 bound and a diagonal summable sequence.
The resulting joint limit represents psi(t) in L1loc, hence its B class,
for almost every t. For X_pos take its nonnegative version. Integrals
below are on these representatives; Fubini and the norm estimates proved
below show independence of null-set changes, up to null sigma. No
pointwise Gaussian noise or rough stochastic evolution is constructed.

Scoped accepted inputs, not re-proved here:
- notes/general-positive-consumer.md(24),(31)-(32), with scientific
  adjudication: EACH fixed psi in C_pos (nonnegative nonzero real
  C_c^infinity((0,1)xR)) satisfies Q2>=2I_psi-v_psi/2 for the SAME
  original canonical Stratonovich point solution, where
  Q2=liminf_(t->infinity)t^-kappa log E|u(t,0)|^2,
  kappa=(4-alpha-a)/(3-alpha). Q2 is finite; the real smooth-score
  values V_c^pos are positive finite for every auxiliary c>0.
- notes/nonseparable-profile-family.md(3)-(4) and its common-H1-form
  T4.12 Rayleigh input: on C_pos, H_sigma=-d2-h_sigma has bottom
  E1<0, real positive normalized p_sigma in H2, and the bottom equals
  the infimum of its H1 Rayleigh form. Actual lambda=sqrt(-E1).

Only the first bullet is the stochastic input. The second identifies
smooth Rayleigh rates, without assuming any rough spectral theorem.
The exact canonical model/finite-upper capsule and source-normalization
adjudication in the packet retain their previous scopes. No firstmean
source value is imported. All new class/form/density arguments follow.

## 2. Time convolution, spatial split and exact raw cost

Write K(s,t)=|s-t|^-a and K0=2^a/(1-a). Direct integration gives
int_0^1 K(s,t)dt=[s^(1-a)+(1-s)^(1-a)]/(1-a)<=K0,
by concavity and symmetry about1/2. For a nonnegative scalar F,
Cauchy-Schwarz against K(s,t)dt and then Fubini give

 int_0^1 (int_0^1 K(s,t)F(t)dt)^2 ds
 <=K0 int int K(s,t)F(t)^2 dt ds<=K0^2||F||2^2.            (1)

For psi in X define q_sigma=int_0^1 K(sigma,t)psi(t)dt as a Bochner
B integral for almost every sigma. Existence follows from (1) applied
to F(t)=||psi(t)||B; the norm bound and strong measurability follow by
simple-function approximation and this estimate. Thus

 ||q||X<=K0||psi||X.                                      (2)

For positive psi this agrees with the positive joint integral, by
Tonelli for its L1 and L2 representatives. Put q_avg=int_0^1 psi(t)dt
in B. It is nonnegative nonzero and has positive finite L1 mass.
K>=1 almost everywhere gives q_sigma>=q_avg almost everywhere in x
for almost every sigma.

For Riesz fix ONCE Gamma_near=Gamma 1_{|y|<=1}, whose L1 mass is
C_near=2c_Gamma/(1-alpha), and k_far(y)=c_Gamma|y|^-alpha 1_{|y|>1},
with bound C_far=c_Gamma. For f in B,

 ||Gamma_near*f||2<=C_near||f||2,
 ||k_far*f||infinity<=C_far||f||1.                        (3)

The first follows by Minkowski and translation invariance of L2;
the second by the absolute integral. The far convolution tends to0
as |x| tends to infinity: approximate f in L1 by bounded-support
functions, use the uniform error bound in (3), and use decay of k_far
for the bounded-support part. No compact support of Riesz means is
inferred. For white simply use h=c_Gamma q in L2, with C_near=c_Gamma
and no far term. Therefore actual h_sigma=Gamma*q_sigma belongs to
L2+L-infinity for almost every sigma. It is nonnegative for X_pos.

For f,g in B, the same split and Cauchy-Schwarz give absolute convergence
and

 |int f(x)(Gamma*g)(x)dx|
 <=C_near||f||2||g||2+C_far||f||1||g||1,                  (4)

where C_far=0 for white. Schur bound (1), followed by time Cauchy-Schwarz,
therefore defines a continuous bilinear form on ALL X:

 B_Gamma(psi,chi)=int int K(s,t)int psi(s,x)(Gamma*chi(t))(x)dx dsdt,
 |B_Gamma(psi,chi)|<=(C_near+C_far)K0||psi||X||chi||X.       (5)

This estimate on signed differences is a norm estimate, not a signed
stochastic-control theorem. For X_pos define the actual raw quadratic
cost v_psi=B_Gamma(psi,psi). Tonelli and (2)-(5) give

 v_psi=int_0^1 int_R psi(sigma,x)h_sigma(x)dx dsigma<infinity. (6)

It is positive. Indeed K>=1 gives v_psi>=int q_avg(Gamma*q_avg).
For white this is c_Gamma||q_avg||2^2>0. For Riesz (4) makes it finite;
q_avg is positive on a set of positive measure, and the kernel is
strictly positive off its measure-zero diagonal, so the double integral
is strictly positive. No continuity of rough q_avg is used. Bilinear
continuity also gives

 |v_psi-v_chi|<=C||psi-chi||X(||psi||X+||chi||X).            (7)

These are raw physical covariance integrals, with no Fourier factor or
change of amplitude. No additional random variable W(psi) is needed.

## 3. The whole H1 form, its core and measurable positive finite rate

For almost every sigma write h_sigma=h_near,sigma+h_far,sigma as above.
Let A_sigma=||h_near,sigma||2 and choose the MEASURABLE bound
b_sigma=C_far||q_sigma||1 for its far part, or b_sigma=0 in white.
Both A and b belong to L2(0,1), by (2)-(3). A measurable joint version
of h comes from the preceding integral construction; all pairings below
also have the bounded-linear/Bochner descriptions in Section4.

We first recall the needed elementary H1 facts explicitly. Compact
cutoffs converge in H1 by L2 tail estimates on f,f' and the cutoff
derivative bound; mollifying the cutoff converges together with its weak
derivative by L2 translation continuity. This proves C_c^infinity density
in H1. For such a real compact smooth f, integrating (f^2)' from minus
infinity gives ||f||infinity^2<=2||f||2||f'||2. An H1 approximating
sequence is uniformly Cauchy by this inequality applied to differences,
so it supplies the continuous representative and the same inequality
for all H1. Write D=||f'||2,N=||f||2. In particular

 ||f||infinity<=D+N, ||f||4^2<=||f||infinity N<=DN+N^2.

Consequently the actual potential form P_sigma(f)=int h_sigma f^2 is
finite and nonnegative, and for EVERY eps>0,

 P_sigma(f)<=A_sigma DN+(A_sigma+b_sigma)N^2
 <=eps D^2+[A_sigma+A_sigma^2/(4eps)+b_sigma]N^2.           (8)

The second inequality follows from the nonnegative square
(2eps D-A_sigma N)^2/(4eps). This is precisely the finite local
potential_budget with A=A_sigma,D,N as above and heps=eps>0, followed
by adding b_sigma N^2. Its analytic Sobolev and integral premises were
proved here, not by Lean. The sharper exponents in the preproof honesty
note are also valid but unnecessary; (8) suffices for all integrability.

Define on WHOLE real H1 the symmetric form

 a_sigma(f,g)=int f'g'-int h_sigma f g.                    (9)

It is continuous on H1: the near term is bounded by
A_sigma||f||infinity||g||2, and the far by b_sigma||f||2||g||2,
with the H1 supremum bound just proved. It is lower bounded by (8).
Take eps=1/2, C_sigma=A_sigma+A_sigma^2/2+b_sigma>=0. Then

 (D^2+N^2)/2<=a_sigma(f,f)+(C_sigma+1)N^2
             <=(C_sigma+1)(D^2+N^2).                     (10)

The lower inequality is exactly shifted_coercivity with
P=P_sigma(f),C=C_sigma, using (8). For the upper use P_sigma>=0 and
C_sigma+1>=1. Thus the shifted-form norm is equivalent to the complete
H1 norm, proving closedness on that domain. Its L2 domain is dense by
compact smooth density. We make NO H2 operator-domain, rough eigenvector,
self-adjoint representation or stochastic wave assertion.

Define the ACTUAL variational ground rate by the whole-domain form:

 lambda_psi(sigma)=sqrt(max(0,sup_(f in H1,||f||2=1)
                                  [P_sigma(f)-||f'||2^2])). (11)

To justify this definition measurably, H1 is separable (its derivative
graph is a closed subspace of separable L2 x L2). Choose a countable
H1-dense subset of nonzero REAL compact smooth functions, and normalize
each by its L2 norm. The resulting fixed countable set {f_j} is H1-dense
in the L2-UNITSPHERE of H1: approximate any unit f by the original dense
set and use continuity of its positive L2 normalization. It is not dense
in whole H1. Continuity of (9) now proves the EXACT equality

 lambda_psi(sigma)^2=max(0,sup_j[P_sigma(f_j)-||f_j'||2^2]). (12)

Each pairing is measurable as an integral of the joint nonnegative
profile against fixed f_j^2, or by Section4's bounded functional. Thus
(12) proves measurability, rather than replacing (11) by a proxy. The
norm bounds in (8) give

 0<=lambda_psi(sigma)<=sqrt(C_sigma)
 <=sqrt(A_sigma)+A_sigma/sqrt(2)+sqrt(b_sigma).             (13)

This is integrable since A,b are in L2 on a unit interval. Therefore
I_psi=int_0^1 lambda_psi(sigma)dsigma is finite, independently of any
SPDE upper bound.

I_psi>0. Let U_avg=Gamma*q_avg. Section2 gives a nonzero nonnegative
locally integrable U_avg; choose D0>=1 with
m=int_[-D0,D0] U_avg>0 finite. Choose real compact smooth0<=chi<=1,
chi=1 on[-1,1], and set A_chi=int|chi'|^2,B_chi=int chi^2>0.
Fix R>=max(1,D0,2A_chi/m). The trial w_R(x)=chi(x/R) satisfies
||w_R||2^2=RB_chi and, since h_sigma>=U_avg,

 a_sigma(w_R,w_R)<=A_chi/R-m<=-m/2.

Thus (11) is at least sqrt(m/(2RB_chi))>0 for almost every sigma.
The argument needs only local mass, not bounded/continuous U_avg, and
proves strict positivity of I without selecting any rough eigenfunction.

For smooth psi in C_pos, (6) is accepted consumer(25). The scoped accepted
family Rayleigh statement identifies the H1 infimum with its spectral
bottom E1. The real positive normalized p_sigma in H2 attains that
bottom, so restricting the complex form to real H1 changes no infimum.
E1<0 makes max(0,.) in (11) inactive. Therefore (11) equals the ACTUAL
accepted smooth lambda_sigma and I equals its accepted integral.
This proves exact smooth score matching, not just a normalization analogy.

## 4. Positive approximation and one-sided integrated-rate control

Fix psi in X_pos. For n large truncate it by
psi^n(t,x)=min(psi(t,x),n)1_{|x|<=n}1_{1/n<t<1-1/n}.
For almost every t this converges in both L1 and L2 to psi(t), with B
error bounded by ||psi(t)||B. Dominated convergence in time gives
||psi^n-psi||X->0. It is nonzero for all large n. For each fixed such n,
mollify in space and time by a nonnegative smooth compact product kernel
of total mass1, with radius less than1/(2n). The result is nonnegative,
nonzero and smooth compact in (0,1)xR. For fixed n, mollification of
this bounded compactly supported joint function converges in spacetimeL2.
All its mollifications have support in one enlarged finite spatial
interval, so ||f(t)||1<=sqrt(length)||f(t)||2 there; both X components
converge. Choose the radius small enough that the X error is <1/n.
This constructs an initial sequence psi_n in C_pos with

 ||psi_n-psi||X->0, v_(psi_n)->v_psi.                      (14)

No time or spatial mass renormalization was made. Growing spatial
support is permitted. The kernel estimates (5) are independent of support.

For each fixed real compact smooth unit f_j, evenness of Gamma and
absolute integrability from (3)-(5) yield

 P_sigma(f_j)=int_0^1 K(sigma,t) L_j(psi(t))dt,
 L_j(z)=int_R z(x)(Gamma*f_j^2)(x)dx.                     (15)

L_j is a bounded REAL linear functional on B: its near coefficient is
in L2 by (3) applied to f_j^2, and its far coefficient is bounded by
C_far||f_j||2^2, with white handled by the near coefficient alone.
Hence (1),(14) imply
||P^(psi_n)_sigma(f_j)-P^psi_sigma(f_j)||L2(sigma)->0 for each j.
Choose a subsequence indexed n_k so these norms are <=2^-k for every
j<=k. For each fixed j, summing their squared L2 norms and using Tonelli
shows that the corresponding errors tend to0 for almost every sigma.
Intersect over the countable j and the countably many full-measure
sets where all forms are defined. On this SAME full-measure set, (12)
gives for every j

 liminf_k lambda_(psi_nk)(sigma)^2
       >=max(0,P^psi_sigma(f_j)-||f_j'||2^2).

Taking the countable supremum and using (12) gives liminf lambda_nk
>=lambda_psi. Nonnegative Fatou therefore proves

 I_psi<=liminf_k I_(psi_nk).                              (APPROX)

Relabel this selected subsequence as psi_n; (14) is preserved. These are
EXISTING fixed smooth tests, never psi(delta). No uniform stochastic
constants over n, rough physical evolution or interchange of an
uncountable supremum and integral is required. This proves the proposed
actual positive cost/rate approximation.

## 5. The original point lower and identical real variational values

By exact smooth matching and accepted consumer(24), the original Q2
satisfies Q2>=2I_(psi_n)-v_(psi_n)/2 for EACH fixed approximant before
its own time limit. It follows from (14),(APPROX) that

 Q2>=2I_psi-v_psi/2 for EACH fixed psi in X_pos.            (POINT)

For example Q2 bounds every sequence score above, hence its lower limit;
that lower limit is at least the right side. Q2 was already finite from
the accepted original upper/lower result, not a new rough-flow theorem.

For c>0 let S_c^X={cI_psi-v_psi/2:psi in X_pos}. All elements are real
by Sections2-3, and the set is nonempty because C_pos is a nonempty
subset. Applying (14),(APPROX) with this fixed c gives for every psi

 cI_psi-v_psi/2<=liminf_n(cI_(psi_n)-v_(psi_n)/2)<=V_c^pos.

The last value is the existing finite REAL smooth-test supremum, so
S_c^X is bounded ABOVE BEFORE taking its real supremum. Thus its
supremum is <=V_c^pos. Conversely C_pos subset X_pos and exact smooth
score matching imply its supremum is >=V_c^pos. Consequently

 sup S_c^X=V_c^pos for every c>0.                         (SUP)

Existing positivity, finiteness and label homogeneity of V_c^pos now
hold for this SAME value over the enlarged class. No optimizer attainment
or supremum/time exchange is used. This is a density identity, not just
another proof of spatial homogeneity.

## 6. Genuine finite-energy occupation densities belong to X

Let O consist of strongly measurable real H1-valued g on(0,1), with
||g(t)||2=1 almost everywhere and
T_g=int_0^1||g'(t)||2^2dt<infinity. This is an explicitly specified
meaningful occupation domain. Define rho_g(t,x)=g(t,x)^2.
The square map H1->B is continuous: for f,g in H1,

 ||f^2-g^2||1<=||f-g||2||f+g||2,
 ||f^2-g^2||2<=||f-g||infinity||f+g||2,

and the H1 supremum estimate in Section3 controls the latter. Strong
measurability therefore transfers to rho_g as a B-valued function.
For normalized g(t), ||rho_g(t)||1=1 and
||rho_g(t)||2^2=int g(t)^4<=2||g'(t)||2. Hence time Cauchy-Schwarz gives

 ||rho_g||X^2=int (1+||rho_g(t)||2)^2dt
 <=2+4 int||g'(t)||2dt<=2+4sqrt(T_g)<infinity.             (OCC)

It is nonnegative and nonzero, so belongs to X_pos. Each conclusion
(APPROX),(POINT),(SUP) applies to this ACTUAL noncompact occupation
density. If w is bounded measurable nonnegative and w rho_g is nonzero,
then it is strongly measurable with X norm at most ||w||infinity||rho_g||X;
it too lies in X_pos. Zeros in w cause no renormalization or division.
Every rate and cost concerns this actual product with the original Gamma.

This does not assert that every possible reading of the source's printed
Ad is O, nor equate this raw score with its occupation ENERGY. The source
has separate raw/damped temporal kernels and gradient penalties1 versus
1/2. Intended normalization remains UNKNOWN. No V1=actualfirstmean or
sourceL/E/E_star identification, Jensen improvement, signed-control or
source optimizer-attainment statement follows from this class inclusion.

## 7. Falsification, formal and original-goal boundaries

The spacetimeL2-only topology failed the actual spreading Riesz control:
a=alpha=1/2,psi_n=n^-5 1_(0,1)(t)1_(0,n^8)(x) gives L2 squared n^-2 but
raw v=(64/9)n^2. Its spatial mass n^3 is controlled by X and does not
converge there. This is a wrong-topology no-go, not an SPDE refutation.
The white time-cutoff control shows why finite-test cost changes under
mass renormalization; both limits agree. Exact finite diagnostics are
fully specified/executed, not substitutes for the proofs above.

Two local real scalar deductions potential_budget/shifted_coercivity
compile/replay cleanly with complete public types/standard-three axioms,
five matching outputs and two numericalFalse controls. Their actual
applications are (8) and (10); the analytic premises are explicit above.
Initial redundant-tactic/server-hash refusal and root universe-parser
failure are preserved separately; no linter/guard/confidence weakened.
No form, Sobolev, Bochner/core/density/probability/SPDE or supremum theorem
is formalized by those scalars. Independent exacttype/application review
is still REQUIRED. No official package/companion/lease/registry/HPC.

Full scientific proof review is required before adoption. Canonical
TeX/PDF unchanged. Source optimizer/value map, intended normalization,
original higher dimensions, sharp upper constant and whole-paper cold
read/novelty/circulation remain open. No Skorohod development, source
correction, source-author contact, wiki/sibling edit or public release.
