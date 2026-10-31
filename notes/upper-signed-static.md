# Signed rough static potentials: exact spectral rate and actual wave phase

ACCEPTED at the scoped FULL analytic/source/type/application gate:
scientific404354a,25checks/HIGH327.286seconds,no required repairs.
Seven optional clarity notes adjudicated in
reviews/2026-10-31-upper-signed-static/scientific-adjudication-v1.md.
Frozen proof/report unchanged. V1 temporal-range FAIL remains preserved;
actual range2<r<2/a. FixedR static/rate interface only, not the original
point sharp upper; full sharp/source goal ACTIVE.

## 1. Objects, statements and named inputs

Use exactly accepted upper-cameron-compactness.md Sections1,3,5-6 (C1-C3),
original H:homog Gamma and amplitude in d=1,2,3,0<a=alpha_0<1 and original
admissible alpha. R fixed, m_R=eta_R² used ONCE. The real phase is
 E=H^(1/2)(R^d)xH^(-1/2)(R^d), F=E directsum R²,
with its orthogonal Hilbert norm, unitary Fourier convention and
Lambda=(1-Delta)^1/2. The SAME free wave S_F, constant-coordinate matrix
 tau(t)=[[1,t],[0,1]], and Young local calculus are accepted inputs from
fixed-mask-young-constant-phase.md Sections2-4. C3 Section7 supplies strong
continuity of the group and its adjoint and norm-continuous conjugation
of a compact operator. No source first-moment normalization is imported.

For q real compact smooth, V_q=m_R(Gamma*q) is real smooth compact and
 L_q=B(V_q):(u,v,c1,c2)->(0,V_q(u+c1),0,0).
C3 Section3 proves this is the actual compact multiplier on F and its
norm-continuous extension T_sp:H_sp->K(F). Define mathcalV_R to be the
OPERATOR-NORM closure of {L_q}. It is a closed real linear subspace of
K(F). For L in this class put k=||L|| and choose K>=max(1,k).

**S1.** L determines a unique real V in H^(-1/2) supported in supp m_R,
with its actual multiplier action and symmetric pairing. On H1 define
 q_V(u)=||grad u||2²-<Vu,u>.
There is a unique self-adjoint H_V on complexified L2 with this form.
For c=2+K² and A=H_V+c,

 A>=1, D(A^(1/2))=H1,
 (1/2)||u||H1²<=q_V(u)+c||u||2²<=3(1+K²)||u||H1²,           (1)
 D(A^(1/4))=H1/2, with negative dual completion H-1/2.       (2)

No H2 domain is asserted for rough H_V.

**S2.** Put beta(V)=inf_(u in H1,||u||2=1)q_V(u). Then
 beta(V)=inf spectrum(H_V), -K²<=beta(V)<=0,
 lambda(V)=sqrt(-beta(V))<=K,

 ||P_V(t)||B(F)<=16(1+K)^4(1+t)^3 exp(lambda(V)t), t>=0.     (3)

P_V is the ACTUAL physical Young/bounded-perturbation wave flow, with both
constant response columns, not a separate spectral model. No positive V,
eigenstate, ground-state gap or positive lambda is assumed. The polynomial
powers are sufficient, not optimal; the exponential rate is exactly lambda.

**S3.** If L_V,L_W have norms<=K,K>=1, then

 |beta(V)-beta(W)|<=(K+2)||L_V-L_W||,
 |lambda(V)-lambda(W)|<=sqrt((K+2)||L_V-L_W||).               (4)

**S4.** Use the ACTUAL accepted tensor mean T=T_sp U:H_I->Lr(I;K(F)),
I=(0,1), EXPLICIT2<r<2/a. Its fields belong to mathcalV_R a.e.;
 Rate(Phi)=int_I lambda(T Phi(s))ds
is finite/continuous. For the C3 block partitions I_m, mesh<=delta B,
let barT_delta Phi be the Bochner average on every positive-length I_m.
Empty last intervals contribute nothing. For each fixed M,

 sup_(||Phi||<=M)||barT_delta Phi-T Phi||Lr ->0,
 sup_(||Phi||<=M)int_I|lambda(barT_delta Phi)-lambda(T Phi)| ->0           (5)

as delta B->0, in particular delta->0 at fixedB. No original point upper
or deterministic product estimate is asserted by this rate interface.

PRIMARY imports, NOT proved here: Teschl2014 SECOND edition, Theorem2.14,
printed81,(2.63), the representation of a densely defined closed semibounded
Hermitian form by a unique self-adjoint operator; closedness definitions
on printed80; Theorem3.6,printed109,(3.51)-(3.53), spectral representation
and form domain; Theorem3.1,printed102,(3.18)-(3.21), bounded Borel calculus/
strong convergence; Theorem3.2,printed104,(3.29)-(3.33), unbounded functions,
domains and products. Selected page103 supplies D_f and spectral cutoffs.
All selected text and7images (5math+title/copyright) are retained in
reviews/2026-10-31-upper-signed-static/. This is not a full-book audit.
The positive compact-mean-ground-family.md Sections3-4 are a METHOD
comparator; their positivity, ground/gap and H2 assertions are not inputs
to the rough signed claim. No KLMN theorem is imported.

## 2. The limiting multiplier and its closed form

Choose L_n=L_(q_n)->L in operator norm. The constant-displacement input
 e_disp=(0,0,1,0)
has norm1, so ||V_n-V_m||H-1/2<=||L_n-L_m||. Thus V_n converges to a real
V in H-1/2. Pairing with compact smooth tests outside supp m_R shows V
keeps that support. Every first/constant output, the velocity-input column
and the instant constant-velocity column of L_n is zero, hence stays zero
in the norm limit. On the displacement column, multiplication M_n by V_n
converges in B(H1/2,H-1/2) to M with norm<=k.

For compact smooth u, multiplication by u is bounded on H-1/2 (the accepted
whole-space smooth-cutoff result used in C3). Hence V_n u->Vu there and
M u=Vu. Density extends M uniquely to H1/2. The constant column recovers V
and the zero columns are fixed, so V determines L uniquely. For compact
smooth u,w the pairing is <V,u w>; symmetry follows, and density gives

 |v_V(u,w)|<=k||u||H1/2||w||H1/2.                           (6)

The complexified multiplier has the same norm: split inputs into real and
imaginary parts in the Hilbert norms. The real symmetric pairing extends
sesquilinearly to a Hermitian one; its diagonal is the sum of the real and
imaginary diagonal pairings. All subsequent operators commute with real
conjugation by uniqueness of the form/resolvent and spectral calculus, so
their real restrictions are the physical phases of the statement.

Cauchy-Schwarz in Fourier gives
 ||u||H1/2²=int<xi>|hat u|²<=||u||2||u||H1.
Write b=||u||2,z=||u||H1. With K>=k,
 |v_V(u,u)|<=Kbz<=z²/2+K²b²/2.                             (7)
For the exact finite reuse, existing Mathlib
Real.geom_mean_le_arith_mean2_weighted requires nonnegative weights/bases,
weights summing to1. Take weights1/2,1/2 and bases z²,(Kb)². Their weighted
product is z(Kb), including zero norms since all powers are positive, and
their weighted sum is the last expression in(7). K,b,z>=0, so every guard
fits the previously audited complete public type; no new Lean theorem.
Its custody scope describes an older nu-weight plan; the GENERAL printed
type, rather than that older substitution, is what is reused here.
Fourier interpolation and all analytic form claims remain outside Lean.

Now q_V=z²-b²-v_V(u,u). With c=2+K², (7) yields

 q_V+c b²>=z²/2+(1+K²/2)b²,
 q_V+c b²<=3z²/2+(1+3K²/2)b²<=3(1+K²)z².                  (8)

The lower bound dominates both z²/2 and b², since z>=b and K>=1. Thus
the Hermitian form on H1 is semibounded and its shifted norm is equivalent
to the complete H1 norm. H1 is dense in L2, so the form is CLOSED in the
primary p80 definition. Import Theorem2.14 with these verified hypotheses:
it gives H_V, independently of which admissible K/shift was used. Theorem3.6
and(3.53), applied after the shift A>=1, give D(A^.5)=H1 and (1).
Here A>=1 is its form lower bound; the spectral-support argument in
Section3 also explains its equivalent operator/spectrum interpretation.

## 3. Quarter-power phase and the actual spectral bottom

Let B0=1-Delta on L2 (not the path space B0 used in earlier notes), and
L_K=3(1+K²). On common form domain H1, .5B0<=A<=L_K B0.
Here is the needed square-root comparison with its valid >=1 pairs.
For self-adjoint T0,S0>=1, q_T0<=q_S0 implies
 (T0+t)^-1 >=(S0+t)^-1, t>0,
as forms on L2: for f, the resolvent quadratic form is the supremum on the
common form domain of 2Re<f,u>-q(u)-t||u||², by completing the square in
the form Hilbert norm. Smaller q makes that supremum larger.
The scalar identity
 sqrt(x)=(1/pi)int_0^infinity t^-1/2 x/(x+t)dt, x>0,
follows by t=xv². Positive spectral integration/Tonelli gives
T0^.5<=S0^.5 as forms, including domains, since
I-t(T0+t)^-1<=I-t(S0+t)^-1. Apply this to (B0,2A) and (A,L_K B0), BOTH
operators in each pair>=1. It follows that

 2^-1/4||u||H1/2<=||A^1/4u||2<=L_K^1/4||u||H1/2.           (9)

These inequalities and their domain inclusions identify D(A^.25)=H1/2.
The L2-pairing dual norm is ||A^-.25 v||2 for v in L2: Cauchy-Schwarz
with A^(.25) and A^(-.25) proves the upper bound, and u=A^(-.5)v gives
equality after normalization when v is nonzero. Completion therefore
identifies the negative entry with H-1/2. This proves S1.

Use the spectral phase norm
 ||(u,v)||E_A²=||A^.25u||2²+||A^-.25v||2².
For M_K=L_K^.25, (9) and the dual inequalities give
 M_K^-1||z||E<=||z||E_A<=M_K||z||E, since K>=1.              (10)
Indeed M_K>=2^.25 dominates both inverse lower constants. Consequently
the condition-number cost is M_K²=sqrt(3(1+K²))<=2(1+K).

For unit u, z>=1, (7) gives
 q_V(u)>=z²-1-Kz>=z²/2-1-K²/2>=-(1+K²)/2>=-K².
Conversely choose a unit compact smooth bump, dilate it by a scale L and
translate its entire support outside supp m_R. Its potential pairing is0
and its kinetic energy tends to0 as L->infinity. Hence -K²<=beta<=0.
Real/complex form infima agree because the complex diagonal splits into
real/imaginary diagonals. The spectral formula(3.52)-(3.53) identifies beta
with the spectral bottom: spectral support lies above the form lower bound,
otherwise a bounded spectral slice below it gives a unit form test violating
that bound. Conversely the form integral is bounded below by the spectral
infimum. The spectrum is nonempty directly from its projection-valued measure:
a unit vector has scalar measure of total mass1 and hence a support point;
normalized projections onto arbitrarily small bounded neighborhoods give
approximate eigenvectors there, excluding a bounded inverse. The bounded
below spectrum and the two form bounds therefore give equality. No eigenstate or essential-spectrum theorem is used.
Thus lambda=sqrt(-beta)<=K, and every spectral h obeys h>=beta and h+c>=2.

## 4. Full spectral wave and an explicit polynomial budget

Define real functions C_t(h),S_t(h) by cos(t sqrt h),sin(t sqrt h)/sqrt h
for h>0; by1,t for h0; by cosh(t sqrt(-h)),sinh(t sqrt(-h))/sqrt(-h) for
h<0. On E_A the spectral wave matrix becomes, under its L2xL2 isometry,

 [[C_t(h),sqrt(h+c)S_t(h)],
  [-h S_t(h)/sqrt(h+c),C_t(h)]].                            (11)

All functions can be set0 off spectral support. For h>=0,
 |C_t|<=1, |S_t|<=min(t,h^-1/2),
 sqrt(h+c)|S_t|<=1+sqrt(c)t, |h S_t|/sqrt(h+c)<=1.
The h0 upper entry is sqrt(c)t and the lower one0. For beta<=h<0,
 |C_t|<=exp(lambda t), |S_t|<=t exp(lambda t),
 sqrt(h+c)|S_t|<=sqrt(c)t exp(lambda t),
 |h S_t|/sqrt(h+c)
   =sqrt(|h|)sinh(t sqrt(|h|))/sqrt(h+c)<=K exp(lambda t).
No division by lambda occurs. Since sqrt(c)<=2K for K>=1, each entry of
(11) is bounded by2(1+K)(1+t)exp(lambda t). Primary3.1 bounds each entry's
operator norm; a2x2 block matrix with each entry norm<=b has norm<=2b.
Equations(10)-(11) therefore give

 ||P_V^E(t)||B(E)<=8(1+K)²(1+t)exp(lambda t).                 (12)

Pointwise continuity of the spectral functions and a common finite-horizon
bound prove strong continuity by spectral dominated convergence. The scalar
addition identities give composition. These are global-E spectral bounds,
not yet the physical identification. The same scalar matrix estimates hold
on the weighted levels D(A^.5)xL2 and D(A)xD(A^.5), since after their
isometries the offdiagonal entries are again sqrt(h+c)S and -hS/sqrt(h+c).
Spectral cutoffs justify their bounded extensions and strong continuity.

## 5. Identify the ROUGH spectral wave with the actual physical flow

Theorem2.14(2.63), tested against compact smooth functions, says for
u in D(H_V) that H_V u=-Delta u-Vu as distributions. Such u is in H1,
so Vu is in H-1/2 by(6). Therefore
 (1-Delta)u=H_Vu+Vu+u in H-1/2,
and u belongs to H3/2. This embedding is continuous in the operator graph
norm: from(1), ||u||H1²<=2<Au,u><=||Au||2²+||u||2², and the displayed
distribution equation bounds ||u||H3/2 by a constant times
||Au||2+||u||2. No roughH2 domain has been asserted.

For completeness the free E generator is
 A0(u,v)=(v,Delta u), D(A0)=H3/2 x H1/2.
Fourier difference quotients on this domain give the derivative of S_E(t)
in E: after a frequency cutoff differentiate the scalar free-wave matrix,
and dominate its derivative by the H3/2xH1/2 graph norm before removing
the cutoff. Conversely any strong generator derivative has these distributional
components; v must lie in H1/2 and Delta u in H-1/2, which together with
u in H1/2 implies u in H3/2. This proves the domain statement with no
operator-norm differentiability of S_E.

Start spectral data in D(A)xD(A^.5)=D(H_V)xH1. By the graph-level estimates
following(12) its trajectory is continuous at that graph level and C1 in
H1xL2, with derivatives u_t=v, v_t=-H_Vu. One verifies this first on bounded
spectral cutoffs, differentiating scalar functions, then passes to the graph
norms by spectral dominated convergence and primary3.2. The cutoffs
1_[1,n](A) approximate graph data uniformly on each finite time horizon,
using the same weighted entry bounds in(11)-(12) at those graph levels.
The embedding above
gives continuity in D(A0), and the distributional equation gives
 z_t=A0 z+L_E z in E, L_E=L restricted to E.
Thus the strong-group chain rule (difference quotients on D(A0)) yields

 S_E(-t)z(t)=z(0)+int_0^t S_E(-s)L_E z(s)ds.                 (13)

The graph data are dense in E: D(A) is dense in D(A^.5)=H1 by spectral
cutoffs, H1 dense in H1/2, and H1 dense in H-1/2. Equation(12) and boundedness
of L_E extend (13) to all E data. Its Volterra solution is unique on every
finite horizon by Picard/Gronwall. Therefore P_V^E is exactly the ordinary
bounded-perturbation physical wave on E. This identifies the flows on a
dense graph core and then all E; no D(A^.75)=H3/2 assertion is needed.

On the full F the same bounded L and strongly continuous S_F define a unique
Duhamel flow on every finite horizon by Picard iteration: a local bound
C_T on S_F makes the nth iterated Volterra term at most
C_T^(n+1)k^n T^n/n! times the initial norm, so the series converges.
Uniqueness by the same estimate makes
overlapping horizons agree and gives all-time composition. Its interaction
primitive is
 D_V(t)=int_0^t S_F(-s)L S_F(s)ds.
Because L is compact, C3's strong-group/adjoint argument gives operator-norm
continuity of the integrand. Hence D_V is Lipschitz on each finite horizon,
and the ordinary operator equation equals the Young equation. This is the
actual phase construction used upstream, with no different noise/flow law.

The constant coordinates are tau(t)c. For initial (e,c) the E component is

 P_V^E(t)e+int_0^t P_V^E(t-s)(0,V(c1+s c2))ds.               (14)

The strong E-valued Fubini calculation in
compact-mean-ground-family.md Section5(14) applies here with bounded L_E:
substitute the E free-Duhamel formula under the forcing integral and
interchange the finite time triangle, whose E norms are absolutely bounded.
Thus (14) solves the full Duhamel system, and uniqueness identifies it.
No constants are placed
in L2, and no density of E in F is used. The forcing norm is at most
K(1+s)|c|. Apply(12), use lambda>=0 and
int_0^t(1+t-s)(1+s)ds<=t(1+t)²<=(1+t)^3. The constant block has norm<=1+t.
The full norm is therefore at most
 (1+t)^3 exp(lambda t)
 [8(1+K)²||e||+(8K(1+K)²+1)|c|]
 <=13(1+K)^3(1+t)^3 exp(lambda t)||(e,c)||F,
by scalar Cauchy-Schwarz and sqrt(8²+9²)<13. This implies(3) with16 and
power4 as stated. Both constant responses are included through c1+s c2.
This proves S2.

## 6. Bottom continuity and multiplier approximation

Let d0=||L_V-L_W|| and choose a unit eta-minimizer for W,0<eta<=1.
Since beta(W)<=0, q_W(u)<=1. Put z=||u||H1>=1. From(7),
 z²-1-Kz<=1, hence z<=K+2 (larger z makes z(z-K)>2).
The interpolation and multiplier difference bound give
 |q_V(u)-q_W(u)|<=d0||u||H1/2²<=d0 z<=d0(K+2).
Take the infimum for V, let eta->0, then reverse V,W to obtain the first
part of(4). For nonnegative x,y, |sqrt x-sqrt y|<=sqrt|x-y|; applying it
to -beta(V),-beta(W) gives the second part. This proves S3. It says nothing
about whether actual binding is Lipschitz in a particular model at zero.

The operator-norm approximations L_n->L used to define the class are also
consistent with the actual physical flows. On each finite horizon, compact
conjugation gives ||D_n-D||Ctheta<=C_T||L_n-L|| for any theta<1. Their
norms stay bounded, so accepted Young local Lipschitz stability gives
uniform operator-norm convergence of interactions, hence of physical flows.
S3 with one eventual common bound K+1 gives beta_n->beta and lambda_n->lambda.
Thus the rough identification and spectral rate also respect smooth masked
mean approximation. No smoothH2 assertion was passed to the rough limit.

## 7. Actual mean fields and uniform rate averaging

Fix EXPLICIT2<r<2/a. Accepted C3 gives compact
 T=T_sp U:H_I->Lr(I;K(F)), with U Phi(s) in H_sp a.e.
Smooth spatial tests are dense in H_sp, so T_sp(H_sp) lies in mathcalV_R.
Thus T Phi(s) is in this closed linear class a.e. The subspace
Lr(I;mathcalV_R) is closed: from an Lr-convergent sequence extract an a.e.
convergent subsequence and use the class's closedness. Therefore the compact
closure of T of any bounded ball stays in this subspace.

Lambda on this operator class is continuous by S3 and satisfies
lambda(L)<=max(1,||L||). It is consequently measurable on strongly measurable
fields, and its integral is finite. More quantitatively, for two such
fields M1,M2 in L1, use(4) pointwise with
 K(s)=max(1,||M1(s)||,||M2(s)||).
Cauchy-Schwarz gives

 int|lambda(M1)-lambda(M2)|
 <=sqrt(3+||M1||L1+||M2||L1) sqrt(||M1-M2||L1).              (15)

All integrands are measurable; (15) in particular proves Rate(Phi)
continuous on H_I since T is bounded into Lr and I has length1. The scalar
functional Rate is distinct from the phase F and the compact operator class.

Let A_Pi be Bochner averaging on a finite interval partition Pi, skipping
empty intervals. Averages stay in mathcalV_R, by closed linearity and simple
Bochner approximation. Jensen gives ||A_Pi M||Lr<=||M||Lr. For continuous
K(F)-valued M on the CLOSED interval[0,1], its averaged error is at most its uniform modulus of
continuity at mesh(Pi), so tends to0. Such closed-interval continuous fields are dense in
Bochner Lr: approximate by finite-valued simple functions, then approximate
the scalar indicator sets by continuous functions in Lr on I. The contraction
then gives strong convergence A_Pi M->M for every Lr field as mesh->0.
On a compact set it is uniform, by a finite epsilon net and the bound
||A_Pi-I||<=2. Apply this to the compact closure of T(||Phi||<=M).
The actual partitions have mesh<=delta B, so the first part of(5) follows.
Their positive-length last cell is averaged over its OWN length; an empty
last cell is simply omitted. There is no pointwise sampling of an Lr class.
Jensen also bounds both field L1 norms uniformly on the ball. Equation(15)
then proves the second uniform limit in(5). This proves S4.

## 8. Falsification, source and formal boundaries

The statement-v1 temporal condition r>2 was FALSE outside the accepted
range. Its FAIL/HIGH report and the root time-bubble obstruction remain
unchanged. Unit raw time controls have local mean Lr scale e^(1/r-a/2):
above2/a it diverges, at2/a weak-zero controls do not have norm-zero means,
so compactness fails. No endpoint boundedness theorem is claimed. The
corrected target and this proof use only2<r<2/a, without removing any
original covariance/dimensional model.

The60finite spectral-matrix rows at40/70digits include12t0norm1 and10h0
Jordan norm calibrations; these check finite fibres/weights/norm evaluator,
not the fullF spectral/CM/SPDE model or a certified error enclosure. The
12exact scalar form rows and4sqrt rows are narrow guards. Time-range
exponent controls do not compute profile norms. The free-velocity and1_Q
representative guards are analytic only. No script was rerun for the same
unchanged question. The scalar sqrt diagnostic makes no claim of actual
non-Lipschitz binding in mathcalV_R.

Primary Teschl2.14/3.1/3.2/3.6 are labeled imports with checked hypotheses;
all uniform norm, rough physical identity and actual averaging applications
are derived here. Existing real weightedAMGM TYPE and actual1/2-weight
application are reused; no new Lean source/compiler/kernel/count.73finite
facts19local seams/L0 unchanged. Form/SA/spectral/Young/measure/SPDE claims
are INFORMAL analysis, not formalized by that scalar kernel.

All mean-action tails/M-infinity, actual global restart, deterministic
product/time-freezing/variational optimization, growing original cone/
localization/entropy, original POINT upper/source constants/normalization/
conditional exactlimit remain OPEN. FixedR S1-S4 does not bypass the accepted
white uniformR guard for fixed finite smooth projections. No F3reverse/
pointtrace/rawL2Gaussian/independent timeblocks or heaterrors/Skorohod/
contact/HPC/sourcefix/companion/TeX/PDF/wiki/bib/promotion/publication or
full-goal completion is claimed. Full original objective ACTIVE.
