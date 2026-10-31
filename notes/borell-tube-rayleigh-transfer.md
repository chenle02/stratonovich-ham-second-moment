# Gaussian control tubes and Rayleigh transfer for the actual E wave input

ACCEPTED at the scoped FULL analytic/source/type/actual-E-law application
gate: scientifica1c90c7,actualOpus5.5/HIGH,20checksPASS,508.072seconds,
no requiredrepairs. All43five-way bindings and58native archive members
verified before optional clarity edits. Four minor findings adjudicated in
reviews/2026-10-31-borell-tube-transfer/scientific-adjudication-v1.md.
Frozen proof/report unchanged. Statement15f8a97/adoption6937719 passed
separately. Gaussian-input transfer/coarse bound only; no sharp spectral/
product envelope,source constant or exact limit. Original goal ACTIVE.

## 1. Abstract objects and the PRIMARY input

Fix 0<delta<1. Let Hraw be real separable Hilbert,W its GIVEN isonormal
process,and X a strongly measurable centered Gaussian variable in a real
separable Banach space mathcalB,with E||X||^2<infinity. Each continuous linear
coordinate has the form ell(X)=W(k_ell). Define its Bochner covariance and
normalized deterministic mean map by
 Cov_delta h=E[X W(h)]=sqrt(delta)Mean_delta h.                (1)
Assume Mean_delta is compact. Let
 Hseen=closed span{k_ell}, E0=closure Cov_delta(Hraw).
For the abstract claim assume X lies in E0 almost surely with its
Gaussian law there,and the genuine first-chaos Wiener realization on E0: its Cameron space is Cov_delta(Hseen),with norm
 ||Cov_delta h||CM=||P_seen h||Hraw,
where P_seen is the Hilbert projection onto Hseen. Section5 verifies this
realization for the ACTUAL E tuple,not merely a formal covariance bound.
In particular ker Cov_delta=ker Mean_delta=Hseen^perp.

The ONLY imported Gaussian isoperimetric result here is PRIMARY
Friz-Hairer2020,Theorem11.6,printed190,with its printed measurability
footnote (retained page renders190-191 and exact excerpt in the packet):
for an abstract Wiener space,a Borel set A of positive Gaussian mass and
the Cameron unit ball Ball_CM,
 mu((A+t Ball_CM)^c)<=barPhi(hat_a+t),t>=0,
 hat_a=Phi_normal^-1(mu(A)).                                (2)
The same printed page gives barPhi(y)<=exp(-y^2/2) for y>=0.
This theorem is NOT proved here. It is a SET enlargement theorem,not an
assertion that the nonlinear wave solution is Gaussian. We explicitly
verify Borel enlarged sets below,so no unproved outer-measure convention
is hidden. Primary custody distinguishes this new use from D1's old
norm/generalized-Fernique11.7 application.

Put b_delta=2E||X|| and A_delta={x inE0:||x||<=b_delta}. In the nonzero-law
case b_delta>0 and Markov gives mu(A_delta)>=1/2. For r>=0 let
 Tube_r=A_delta+Mean_delta(Ball_Hraw(r)),
 D_delta(x)=inf{r>=0:x inTube_r},infempty=infinity.           (3)
All raw balls in this note are CLOSED. Here Mean_delta is an operator;
Ball_CM is a set. Later L_delta is a wave horizon,C_pr a primitive
constant,c_Y a Young constant,and C_env an envelope constant. No one
symbol is used for all of those roles.

## 2. Compact ball images, closed tubes and least-radius membership

For each r,Mean_delta(Ball_Hraw(r)) is compact,including closedness. Here
is the needed Hilbert argument. From any bounded sequence h_j choose a
weakly convergent subsequence with weak limit h and ||h||<=r (diagonal
ONbasis coordinates and Fatou suffice in a separable Hilbert space).
Compactness of Mean_delta gives norm-convergent subsubsequences of its
images; bounded linear testing identifies every such limit as Mean_delta h.
Thus the images converge in norm along that subsequence. This proves
sequential compactness,and hence compactness in the Banach metric.

Closed A_delta plus that compact image is closed: if a_j+Mean_delta h_j
converges,choose a convergent compact component,then the residual converges
inside the closed A_delta. Therefore every Tube_r is closed and Borel.
Moreover
                       {D_delta<=r}=Tube_r.                (4)
One inclusion follows from the infimum. For the converse,if D_delta(x)<=r,
choose h_j with ||h_j||<=r+1/j and x-Mean_delta h_j in A_delta.
A weakly convergent subsequence has a limit h with ||h||<=r. Compactness
gives Mean_delta h_j->Mean_delta h,and closedness gives the required
residual in A_delta. This also proves ATTainment at the least finite
radius,not just membership in slightly larger open tubes. It works at r=0.
Equation(4) makes D_delta lower semicontinuous as an extended nonnegative
function,and hence Borel.

Unused raw directions cause no enlargement of the image ball: Mean_delta
kills Hseen^perp and P_seen is a contraction onto Hseen. Hence
 Ball_CM=Cov_delta(Ball_Hraw(1))
        =sqrt(delta)Mean_delta(Ball_Hraw(1)),
 Tube_r=A_delta+(r/sqrt(delta))Ball_CM.                     (5)
This is the EXACT Cameron geometry,not an embedding upper bound. In
particular no free-group or covariance-norm constant enters the half action.

Apply PRIMARY(2),using the Borel sets just proved and hat_a>=0. It gives
 P(D_delta(X)>r)<=barPhi(hat_a+r/sqrt(delta))
                         <=exp(-r^2/(2delta)),r>=0.         (6)
The convention hat_a=+infinity when mu(A_delta)=1 is allowed by the source.
The tail tends to0,so D_delta(X)<infinity almost surely. No uniform-R or
uniform-delta compactness,entropy estimate or dimension is required in this
fixed-parameter argument. This proves the geometric part of BT1.

## 3. Rayleigh comparison for all monotone envelopes,including jumps

Let R_aux have the AUXILIARY Rayleigh density
       rho_delta(r)=(r/delta)exp(-r^2/(2delta)),r>0.          (7)
Its mass is1 and survival function exp(-r^2/(2delta)),by direct integration.
It is a stochastic dominator of D_delta(X),not a proposed norm of an
infinite-dimensional white Gaussian vector.

Let G:[0,infinity)->R be Borel and nondecreasing. For any t>=0,the upper
level set of exp(G(r)/delta) is an upper interval,possibly empty or the
entire halfline,with either an open or a closed finite endpoint c.
Open endpoints are controlled by(6). For c>0 closed endpoints are controlled
by taking s upwards to c in
 P(D_delta(X)>=c)=lim_(s up c)P(D_delta(X)>s)
                         <=exp(-c^2/(2delta)).
Rayleigh has no atom,so the last quantity is also P(R_aux>=c). At c=0 the
closed-endpoint probability bound is1 on both sides. Thus upper level
probabilities are ordered even when G jumps. Layer cake/Tonelli gives
             E exp(G(D_delta(X))/delta)
                         <=E exp(G(R_aux)/delta).           (8)
The almost surely infinite-distance exception may be assigned any value;
it has zero mass. Infinite expectations on either side cause no subtraction.

If a Borel F:E0->R obeys F(x)<=G(r) for EVERY r and EVERY x in Tube_r,
then least-radius membership(4) gives F(X)<=G(D_delta(X)) almost surely.
No measurable choice of h(X) or of a residual is needed. Combining(7)-(8),
 E exp(F(X)/delta)
       <=int_0^infinity (r/delta)
                      exp((G(r)-r^2/2)/delta)dr.            (9)
This proves BT1b for all such G,not just differentiable profiles.

If the Gaussian law is zero,then X=0 almost surely,Cov_delta=Mean_delta=0
and E0={0}. We do not apply Borell with a positive-radius assumption.
Instead F(0)<=G(0)<=G(r),so normalization of(7) proves(9) directly. The
observable F(0) is NOT assumed zero. This includes a free wave endpoint,
whose operator norm may exceed1 despite zero noise.

## 4. Original wave input,compatible parameters and exact covariance

Now keep ALL original H:homog Gamma/amplitudes,d=1,2,3,0<a<1,
0<alpha<d or alpha=d=1,alpha+a<2. W is the GIVEN positive-time slow noise.
Use unitary Fourier,inhomogeneous Bessel Lambda=(1-Delta)^(1/2),real
 E=H^(1/2) x H^(-1/2), F=E directsum R2,
with closed isometric inclusion i:E->F. Fix integer block horizon B>=1,
 0<delta<min(1,1/B),L_delta=1/delta,R_delta=L_delta+2,
 g_delta=delta^((1-a)/2),m_R=eta_root(x/R)^2 ONCE,
where eta_root is the accepted real even smooth compact root profile. Let
N=floor(1/(delta B)),n=N+1,s_m=m delta B,ell_m=B for m<N,
ell_N=L_delta-NB in[0,B). Slow intervals I_m partition I=(0,1) up to
endpoints; the last may be empty. Both displacement and FAST velocity
remain in every physical block. Hraw=H_I is the closed supported raw
Hilbert space inside H_W,not a raw time-indicator multiplier construction.

Choose once
 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<eta_time<beta_time<min(1-a/2,(3-a-alpha)/2),
 nu=1/theta, 1/(1-theta)<r_t<2/a, nu<=p<2<r_t.
Then 1<nu<2 and r_t>nu. Choose a fixed EVEN Q satisfying
 Qgamma>d, beta_time-eta_time-1/Q>0, Q>2d/(1-a).             (10)
All ranges are nonempty; choose the exponents in their strict gaps,then
an even integer above the finite maximum of the three thresholds. This
is the SAMEtheta used in the SA mean anchor,chosen before delta. Constants
need not be uniform as a approaches1 or alpha+a approaches2.

Use full actual noise,not a finite head or projected residual:
 W_m(f)=W(T_(delta,m)f), X_m=g_delta M_R(W_m),               (11)
stopping each interaction primitive at ell_m and extending it constantly
to[0,B]. Take R=R_delta in applications; all preliminary bounds allow any
R>=1. Every component starts at0 and has compact operator values. Let
mathcalB_delta be the finite product of zero-start little-Holder spaces
h0theta([0,B];K(E)),with norm
        ||x||_(delta,p)=(delta sum_m||x_m||Ctheta^p)^(1/p).  (12)
K(E) is separable in operator norm; rational piecewise-linear paths on
rational grids are dense in the little-Holder closure. Thus this is a
separable Banach space. The actual construction/transfer is the Ctheta
limit of Lipschitz finite coefficient paths,so X_delta=(X_m) belongs to
this space and is strongly measurable and jointly centered Gaussian.
SA gives all finite moments at fixed parameters,in particular Bochner L2.
None of this asserts separability of the entire B(E) or full Ctheta space.

Let mathcalT_(R,E):H_I->Lr_t(I;K(E)) be the ACTUAL completed E mean field.
From accepted C2 by compression it is COMPACT at each fixed R. Accepted U
(17) bounds its norm by a constant C_mean INDEPENDENT R>=1. Define
 (Mean_delta Phi)_m(u)=int_0^min(u,ell_m)
  S_E(-v)mathcalT_(R,E)Phi(s_m+delta v)S_E(v)dv.             (13)
This is a bounded linear map from the mean-field Lr_t space into(12) at
fixed delta,B. Norm continuity of free conjugation on compact operators,
affine time pullback and the exponent 1-1/r_t>theta give Bochner fields
and little-Holder paths,including constant stopping. Composition with
the fixed-R compact mean field proves Mean_delta is COMPACT. There is
no assertion of uniform compactness as R_delta grows.

The actual covariance identity is,from accepted U Section7(22) with
retained raw rank0 (Q_ret=I, the complement denoted Q in U),
    Cov_delta Phi=E[X_delta W(Phi)]
                         =sqrt(delta)Mean_delta Phi.      (14)
Every scalar stopped row pulls back to a slow label in H_I,as in accepted
C3 and U: endpoint indicators are approximated inside I in the raw norm.
Countable matrix/rational-time coordinates identify the actual Gaussian
tuple as measurable in W(H_I); its linear statistics are in that closed
first chaos. This is SAME-W covariance,not a norm bound or an independent-
block sum. Its scale is sqrt(delta) because g_delta delta^(a/2)=sqrt(delta).
Fast directions used in SP establish a norm baseline only; their possibly
large norms are NOT summed or substituted for the global H_I action.

## 5. The genuine E-law Wiener realization and the typical ball

We recheck the generic first-chaos construction in accepted OWN D1
(upper-residual-exponential.md Section3) on THIS E tuple. Its old F norm
or old expected-norm bound is not imported. If X_delta is the zero law,
(14) gives Cov_delta=Mean_delta=0,the support is{0},and Section3 applies
directly; no ONbasis construction is needed. This includes Gamma=0,
whose actual drivers and mean field are zero. In the remaining case use
the nonzero supported raw space and the construction below.

A countable norming family of continuous linear functionals on the separable
Banach span generates its Borel sets. Each ell(X_delta)=W(k_ell),with
k_ell in H_I by(14)'s supported-coordinate argument. Choose a complete raw
ONbasis e_j of H_I,and mathcalG_j=sigma(W(e_1),...,W(e_j)). Bochner conditional
expectation is constructed first on simple Banach variables by scalar
conditional expectations,then by the L2 norm contraction and simple
approximation; no Banach Radon-Nikodym property is assumed. Gaussian
regression on each scalar coordinate and the countable norming family give
 X_delta,j=E[X_delta|mathcalG_j]
                =sum_(l<=j)W(e_l)Cov_delta e_l.            (15)
Finite-coordinate scalar events approximate the sigma field generated by
W(H_I),so these conditional expectations converge to X_delta in Bochner L2,
as in the explicit D1 argument. This uses only supported first-chaos
measurability,not a Gaussian random variable with values in H_I.

Let Hseen be the closed span of k_ell. Bounded linear testing shows
ker Cov_delta=Hseen^perp; Cov_delta is injective on Hseen. The closed
first chaos generated by X_delta is W(Hseen),so its genuine Cameron image
and norm are
 H_CM=Cov_delta(Hseen), ||Cov_delta Phi||CM=||P_seen Phi||HI. (16)
This is the same first-chaos identification as accepted U and D1,now with
the actual E covariance(14). The image completion in the Banach norm is
E0_delta=closure Cov_delta(H_I). Equation(15) gives X_delta in E0_delta
almost surely. Its Gaussian law is Radon: the ambient span is separable
and complete,and the finite-ball/totally-bounded-intersection construction
in D1 Section2 proves tightness there without finite-dimensional state
replacement.

For completeness its support is ALL E0_delta. X_delta-X_delta,j is
independent of the finite Gaussian head: each tail scalar label is
(I-P_j)k_ell,orthogonal to e_1,...,e_j,and countable Borel coordinates
transfer joint Gaussian independence to the Banach tail. Given Phi and a
radius epsilon>0,choose j so Cov_delta P_j Phi approximates Cov_delta Phi
and the L2 tail has positive probability below epsilon/3. The finite
Gaussian head has positive probability in any ball about Cov_delta P_j Phi,
even if its covariance is singular (the finite preimage is an open set
about a coefficient vector). Independence gives positive probability in
every ball about Cov_delta Phi. Closure proves the full support statement.

The measurable-norm condition can also be checked explicitly as in D1.
Cov_delta is an isometry from Hseen onto H_CM,so the vectors Cov_delta h_k
below are CM-orthonormal,and the excluded finite-dimensional CM subspace
is Cov_delta(V_j). This is Gross's Hilbert-image formulation.
In Hseen put V_j=span{P_seen e_l:l<=j}. For any finite orthonormal family
h_k in V_j^perp,these h_k are orthogonal to e_1,...,e_j. Regression gives
 E[X_delta-X_delta,j | W(h_k),all k]=sum_k W(h_k)Cov_delta h_k,
so Jensen bounds the squared expected Banach norm of this finite sum by
E||X_delta-X_delta,j||^2. For any epsilon>0 choose j making that quantity
less than epsilon^3. Markov then bounds its probability of norm>epsilon
by epsilon,uniformly over EVERY such finite orthonormal family. This is
the measurable-norm tail condition for the dense Hilbert image in(16).
Together with the Gaussian characteristic functional exp(-||k_ell||^2/2),
these are precisely the generic genuine Wiener-realization checks of
accepted D1 Section3. Thus the actual support triple,not a formal raw
covariance surrogate,satisfies PRIMARY(2)'s abstract Wiener hypotheses.

Compactness in Section4 and the seen projection identify its CM unit
ball with sqrt(delta)Mean_delta(Ball_HI(1)),including closedness. The
closed base ball therefore has Borel enlargements exactly as in Section2.
SA applied to(11) with zero projection and the compatible fixed Q in(10)
gives
 b_delta=2E||X_delta||_(delta,p)
              <=C_(Q,B,p)delta^((1-a)/2-d/Q)->0            (17)
when R=delta^-1+2. At each fixed delta all constants and maps are finite;
no fixed sqrt(delta)-scaled Banach law or uniform-R compactness is assumed.
If the law is zero,its support is{0} and Section3's elementary case applies.
This proves all abstract BT1 eligibility for the original E input.

## 6. The actual endpoint functional and a uniform coarse envelope

For ANY x in mathcalB_delta,define the globally defined Young product
 mathcalP_delta(x)=P_N(x_N)...P_0(x_0),
 P_m(x_m)=S_E(ell_m)U_(x_m)(ell_m,0),
 F_delta(x)=2delta log max(1,||mathcalP_delta(x)||B(E)).      (18)
The Young endpoint map is locally Lipschitz on all Ctheta paths. Finite
products,bounded fixed-time free groups,norm and log max(1,.) are continuous,
so F_delta is finite,continuous and Borel,not merely defined on a Gaussian
full-measure domain. This permits evaluation on every tube without a
measurable control selection or translated exceptional set.

The ACTUAL noise-only raw restart from accepted GL Section2(3),with its
same-source/Young proof,gives the F global endpoint as the ordered physical
block product at each fixed delta,B,R. No GL fixed-R rate is used. The
actual E/F intertwining from GC/SP holds for the global flow and each
local block. Applying it to the product and using injectivity of i gives
        mathcalP_delta(X_delta)=P_delta,E^R(L_delta,0).    (19)
The local clocks,true partial/empty last block and both velocity components
are unchanged. The source limits establishing restart are taken first
at finite horizons; temporal blocks remain correlated on the SAME W.
At R=R_delta,SP with reference W_fast,c=g_delta,Phi=0 gives norm>=1 for
this actual endpoint. Hence
        exp(F_delta(X_delta)/delta)=||P_delta||B(E)^2.      (20)
This is an operator identity/application. No raw Sobolev point trace or
pathwise representation of the canonical original u is introduced.

Define A_delta on E0_delta using(17),and let
 G_delta(r)=sup{F_delta(a+Mean_delta Phi):
              a inA_delta, ||Phi||HI<=r}.                 (21)
We prove finiteness and the promised explicit coarse bound. Put
 C_pr=G_B^2[B^(1-1/r_t)+B^(1-1/r_t-theta)],
 G_B=sup_(|v|<=B)||S_E(v)||<=3B,
so C_pr<=18B^(3-1/r_t),as in accepted U(23). Its exact primitive estimate
and uniform E mean norm C_mean give,with h_m=||(Mean_delta Phi)_m||Ctheta,
        delta sum_m h_m^r_t
                       <=(C_pr C_mean)^r_t ||Phi||HI^r_t. (22)
There is no F constant-column mean norm in this bound.

For zero-start d on[0,B],the generic Banach Young growth estimate,as
proved in accepted fixed-mask Section4/Young-perturbation Section2,allows
 c_Y=c_Y(B,theta)>0 with
                  log||U_d(u,0)||<=c_Y(1+||d||Ctheta^nu),u<=B.
Indeed d<=1+d^nu and (1+d)^nu<=2^(nu-1)(1+d^nu) convert either cited
Young bound to this form by increasing c_Y. It holds on B(E),whose
multiplication has norm1,and needs no Gaussian,
Hamiltonian or positivity assumption. For a residual a in A_delta write
v_m=||a_m||Ctheta. Convexity gives ||a_m+(Mean_delta Phi)_m||^nu
<=2^(nu-1)(v_m^nu+h_m^nu). Submultiplicativity of the endpoint product,
with nonnegative upper terms,therefore gives
 F_delta(a+Mean_delta Phi)
 <=2delta n(log G_B+c_Y)+2^nu c_Y delta sum_m(v_m^nu+h_m^nu). (23)

The exact finite weighted Holder inequalities are
 delta sum v_m^nu<=(delta n)^(1-nu/p)||a||_(delta,p)^nu,
 delta sum h_m^nu<=(delta n)^(1-nu/r_t)
                              (delta sum h_m^r_t)^(nu/r_t).
They follow from the supplied COMPLETE Mathlib finite powermean type at
exponents p/nu>=1 and r_t/nu>1,values norm_m^nu>=0,followed by positive
powers. delta>0,n=N+1>=2; zero norms and empty blocks occur only under
positive powers. Cardinality powers are well defined even when p=nu.
Since delta n<=2/B,(22)-(23) yield,for ||Phi||<=r,
 F_delta(a+Mean_delta Phi)<=D0+D1 b_delta^nu+D2 r^nu,
 D0=2(2/B)(log G_B+c_Y),
 D1=2^nu c_Y(2/B)^(1-nu/p),
 D2=2^nu c_Y(2/B)^(1-nu/r_t)(C_pr C_mean)^nu.
Thus C_env=1+D0+D1+D2 is finite,INDEPENDENT delta and R>=1,and
          G_delta(r)<=C_env[1+b_delta^nu+r^nu].             (24)
This holds for ALL0<delta<min(1,1/B),not only sufficiently small delta.
Only replacing b_delta by a uniformly small constant uses the limit(17).
No quantitative optimal B-growth or sharp rate is asserted by(24).

Equation(21) is a supremum over nonempty norm-bounded sets,and(24) makes
it finite. It is nondecreasing with r,so it is Borel regardless of whether
a maximizer exists. Its definition provides the bound on EVERY closed
tube. Applying(9) and(20) gives the exact transfer
 E||P_delta||B(E)^2
 <=int_0^infinity (r/delta)
                      exp((G_delta(r)-r^2/2)/delta)dr.     (25)
This proves BT2. Combined with separately accepted GC,it also bounds the
ORIGINAL point second moment by the right side times its polynomial data
prefactor. GC (21)-(23) retains all mixed,self and empty chains and the
source-first limits. That is an exact consumer composition,not a sharp constant;
the missing integrated spectral/product envelope for G_delta remains open.

## 7. Exact Rayleigh tail budget and the raw half-action supremum

Let G(r)<=A0+C r^nu,with real intercept A0,C>=0,1<nu<2. Choose M>0 with
4C<=M^(2-nu). For every r>=M,the unchanged old scalar kernel
StratonovichHAMAudit.GaussianTail.cutoff_density_split applies at x=r:
       C r^nu-r^2/2<=-M^2/8-r^2/8.
Its complete public type/standard axioms are supplied. The application
guards are EXACTLY M>0,r>=M,C>=0,1<nu<2 and that cutoff condition;
no desired inequality is assumed as a hypothesis. Its only certified
content is this real scalar inequality,not the following integration.

Analytically,-d/dr[4exp(-r^2/(8delta))]
                         =(r/delta)exp(-r^2/(8delta)).
Therefore
 int_M^infinity (r/delta)exp((G(r)-r^2/2)/delta)dr
 <=exp((A0-M^2/8)/delta)*4exp(-M^2/(8delta))
                         =4exp((A0-M^2/4)/delta).          (26)
Both the front4 and the M^2/4 exponent are retained. Such a cutoff exists
because 2-nu>0; it may be chosen sufficiently large at each fixed C.
The compact-radius integral is finite since monotone G is bounded above
there. Applying(26) to(24) proves finiteness of(25),without an infinite-
dimensional Gaussian density. This does not identify its sharp asymptotic.

Finally,let J:Hraw->R be finite and bounded above on every raw ball,and
g_J(r)=sup_(||Phi||<=r)J(Phi). In the extended reals,
 sup_(r>=0)[g_J(r)-r^2/2]
                    =sup_Phi[J(Phi)-||Phi||Hraw^2/2].       (27)
For >= take r=||Phi||. For <=,each ||Phi||<=r satisfies
J(Phi)-r^2/2<=J(Phi)-||Phi||^2/2;take the two suprema. Balls are nonempty,
their suprema are finite and no infinity-minus-infinity is formed. There
is no compactness,rank or density assumption for(27). This proves BT3.
Setting J=2Rate_R in a successor requires a NEW radius-uniform deterministic
spectral/product envelope and its error/tail/limit proof; (25) does NOT
establish that envelope or a signed-positive score comparison.

## 8. Evidence and remaining original scope

This is an independently reviewed proof of the stated Gaussian-input transfer
and original E-law application. It preserves the HALF global raw action.
Cameron embedding norm bounds have not replaced the exact geometry; no
sum of fast SP-direction costs,independent temporal blocks or Gaussian
random variable with values in Hraw is used. A norm budget on E is not a
budget on F with constant data columns. Nonlinear output is not Gaussian.

Correct linear-MGF comparisons are positive evaluator calibrations only:
their gap is nonnegative by construction. The raw36/48rows are not independent
evidence:8nonzero moment configurations,16delta/r pairs and12correct
standardized tail radii remain after symmetries/zero signals. Wrong-scale/
double-action and direct-CDF checks are the negative controls. Cell examples
use u=sqrt(2delta log(2n)),not logn in their exact numerical bound; they
illustrate why a vanishing mean premise cannot be omitted. No numerical,
CAS,Lean or dependency rebuild was run for this proof. V1 rounding error,
v2 unrounded comparison,raw data and semantically identical delivery carrier
remain preserved. Floating consistency is not a certified enclosure.

Old GaussianTail and Mathlib finite Holder statements are reused with
complete actual guards. All Gaussian/AWS/support/geometry/order/Young/
restart/primitive steps are ANALYTIC. No new declaration/compiler/count:
74facts20seams/L0 PROPOSED unchanged,companion decision4 still pending.
PRIMARY(2) is imported with exact pinpoint,not proved here; accepted prior
inputs are labeled and used at their stated scopes,not recertified.

The uniform sharp E spectral/product envelope,signed-positive variational
comparison,intended author energy/domain/normalization and conditional
exact limit remain OPEN. No first-mean auxiliary-label identity,source
repair,Skorohod development,contact,HPC,companion,TeX/PDF/wiki/bib/sourcePDF/
sibling or public-release action. Full original all-model goal ACTIVE.
