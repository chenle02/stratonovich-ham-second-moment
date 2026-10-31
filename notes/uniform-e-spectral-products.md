# Uniform E signed spectral rates, mean products and arbitrary small residuals

UNREVIEWED COMPLETE PROOF CANDIDATE. US1-US4 statement/source/type gate
43ff384/adoptionda79a8d passed actualOpus5.5/HIGH,19checks,607.619s,
no requiredrepairs. All10notes adjudicated before this proof,including
correction of the reviewer's balanced-mode observation. This note requires
its OWN FULL independent proof/source/type/application gate before use.
Original all-Gamma/d1/2/3 sharp/source goal ACTIVE. No sharp-score Rayleigh
application,signed-positive comparison,source constant or exactlimit here.

## 1. Exact objects and imported inputs

Keep the model,mask and raw space of the frozen target: ALL original
H:homog Gamma/amplitudes,d=1,2,3,0<a<1,0<alpha<d or alpha=d=1,alpha+a<2,
including Gamma=0. Unitary Fourier,Lambda=(1-Delta)^(1/2),
 E=Hhalf x Hminus-half, F=E directsum R2,
with real Hilbert norms and closed isometric inclusion i:E->F. For each
finite R>=1 use m_R=eta_root(x/R)^2 ONCE,after source smoothing,where the
accepted real even compact smooth root profile is fixed. All velocities
are retained. H_I=H_t tensor H_sp is the supported slow raw completion,
not a raw time-indicator multiplier. Choose once
 1/2<theta<min(1-a/2,(3-a-alpha)/2), nu=1/theta,
 1/(1-theta)<r<2/a, nu<=p<2<r.
In particular 1<nu<2<r and 1-1/r>theta. The strict gaps are nonempty.

Direct OWN accepted imports,checked below for the new applications:
- C3 (upper-cameron-compactness.md Sections3-7): actual compact masked
  multipliers on F/E,completed supported means,time tensor identification,
  compact-conjugation primitives and true block clocks.
- U (uniform-e-cameron-regulator.md Sections2,5,6): bounded spatial E map
  J_R:H_sp->K(E),||J_R||<=M_0 independentR; compact scalar C_t:H_t->Lr(I),
  I=(0,1),and actual completed E field
    mathcalT_R=J_R(C_t tensor Id), ||mathcalT_R||<=C_mean=M_0||C_t||. (1)
  U (15) gives ||A tensor Id_G||H_t tensor G->Lr(I;G)<=||A|| for r>=2,
  any bounded scalar A:H_t->Lr and any real Hilbert G. This is a norm
  assertion,NOT a compactness assertion.
- S (upper-signed-static.md Sections2-5): the actual fixed-R F-class
  reconstruction/form/spectral/Young identification. Its quantitative
  F norm bound is NOT imported as an E-only bound. We rederive that bound.
- E1 (upper-young-perturbation.md Sections1-3): for ANY nonzero Banach
  phase,zero-started theta paths H,x with ||H||theta<=K,any bounded left
  multiplier A and t<=B,
    ||A U_(H+x)(t)||<=||A U_H(t)||exp(C(theta,B,K)(v+v^nu)), v=||x||theta. (2)
  Constants are dimension-free; no Hamiltonian condition on x,A and no
  penalty at v=0. Young invertibility/local Lipschitz continuity and the
  refined piececount proof are also imported there.
- SP (e-phase-symplectic-baseline.md Sections6-7): actual completed E
  PURE MEAN physical block endpoints preserve J_E and have norm>=1 at
  each true clock,including partial/empty blocks. We verify mean/mask fit.
- B (upper-mean-block-product.md Sections2-6) is an accepted comparator
  for the decomposition and schedules,not an already uniform-R E theorem.

PRIMARY imports,NOT proved here: Teschl2014 SECOND edition,Theorem2.14
printed81/(2.63),closed forms definition printed80; Theorems3.1/3.2,
printed102-104/(3.18)-(3.33),Borel calculus/domains/strong limits;
Theorem3.6,printed109/(3.51)-(3.53),spectral/form representation.
Friz-Hairer2020 Section1.5 printed13 and4.1 printed61-62/(4.1)-(4.3)
supply Banach Young remainder/existence/continuity. The nonlinear (2) is
OWN E1,not a book theorem. Exact selected texts and10images supplied;
original PDF identity/DOI metadata inherited,not freshly verified here.

## 2. The actual E closure,unique potential and fixed-R lift

For q real compact smooth let V_q=m_R(Gamma*q),M_q:Hhalf->Hminus-half,
 L_q=B_E(V_q):(u,v)->(0,M_q u).
From C3 these are actual compact operators. Let mathcalV_E,R be their
operator-norm closure,which is a closed real linear subspace of K(E).
Let L_n=L_(q_n)->L. Each first/output-displacement column and each
input-velocity column is zero,so L=(0,M u) with M_n->M and
                 ||L||B(E)=||M||Hhalf->Hminus-half=:k.       (3)

Choose chi_R real compact smooth,equal1 on a neighborhood of supp m_R.
This uses ONLY fixed finite R. Since M_n chi_R=V_n,
 ||V_n-V_j||Hminus-half<=||chi_R||Hhalf ||M_n-M_j||.
Thus V_n converges to a real V in Hminus-half. Pairing with tests outside
supp m_R gives the same support. For any compact smooth u,multiplication
by u is bounded on Hminus-half (accepted C3 smooth-cutoff multiplier),so
V_n u->Vu. Hence M u=Vu on tests,and density extends this uniquely to
Hhalf. This also proves V independent of the approximating sequence:
M chi_R=V,then action on all tests determines M. Symmetry of the smooth
pairing passes to the limit:
             |v_V(u,w)|<=k||u||Hhalf||w||Hhalf.             (4)

The old F operators are L_n,F(u,v,c1,c2)=(0,M_n u+c1 V_n,0,0).
Their differences have norm at most
 (1+||chi_R||Hhalf)||M_n-M_j||,
so they converge in the SAME old class mathcalV_R to a lift L_F,with
L_F i=iL. This bound is allowed to grow with R: it proves identification
only. We will use neither ||chi_R|| nor ||L_F|| in any uniform estimate.
All averages/completed spatial means lie in mathcalV_E,R by dense smooth
raw tests and bounded completion of J_R; Bochner averages preserve closed
linearity. This is the actual mean class,not arbitrary point potentials.

Complexify the Hilbert spaces. The complex norm of M equals its real
norm: sum the squared real/imaginary input and output norms. The symmetric
real pairing becomes Hermitian,whose diagonal splits into its real and
imaginary diagonal values. Thus (4) and all following constants hold in
the complexification. Real restrictions commute with conjugation by
uniqueness of forms/resolvents/calculus. No additional complex norm cost.

## 3. E-only form,quarter phase and exact spectral rate

Fix K>=max(1,k),b=||u||2,z=||u||H1. Fourier Cauchy-Schwarz gives
 ||u||Hhalf^2<=b z,so |v_V(u,u)|<=K b z<=z^2/2+K^2 b^2/2. (5)
The last finite inequality uses the supplied complete Mathlib weighted
AMGM type at weights1/2,1/2 and bases z^2,(Kb)^2; weights/bases nonnegative,
weights sum1,positive powers handle zeros. Fourier interpolation is
analytic,not kernel-certified. For q_V=z^2-b^2-v_V and c=2+K^2,
 q_V+c b^2>=z^2/2+(1+K^2/2)b^2,
 q_V+c b^2<=3z^2/2+(1+3K^2/2)b^2<=3(1+K^2)z^2.           (6)
The lower bound dominates z^2/2 and b^2. It also dominates2b^2 since
z>=b,K>=1. The shifted norm is equivalent to the complete H1 norm;
H1 is dense in L2. Thus q_V is densely defined,Hermitian,semibounded and
CLOSED in the PRIMARY printed80 definition. Theorem2.14 applies and gives
unique self-adjoint H_V; its shift A=H_V+c has A>=1 (in fact>=2).
Theorem3.6/(3.53) gives D(A^.5)=H1. No rough H2 domain is claimed.

For completeness repeat the quarter-order step with these E constants.
Put B0=1-Delta,L_K=3(1+K^2). Equation(6) says .5B0<=A<=L_K B0 as
forms with common H1 domain. For positive self-adjoint T,S>=1 with
q_T<=q_S,the resolvent quadratic-form variational identity gives
 (T+t)^-1 >=(S+t)^-1,t>0:
its value on f is sup_u[2Re<f,u>-q(u)-t||u||^2],by completion of the
square in the form Hilbert norm. Use
 sqrt(x)=(1/pi)int_0^infinity t^-1/2 x/(x+t)dt,x>0,
which follows by t=xv^2. Positive spectral integration/Tonelli and
I-t(T+t)^-1<=I-t(S+t)^-1 yield T^.5<=S^.5 including form domains.
Apply to (B0,2A) and (A,L_K B0),each pair>=1. Consequently
 2^-1/4||u||Hhalf<=||A^.25u||2<=L_K^.25||u||Hhalf,
                         D(A^.25)=Hhalf.                  (7)
For v in L2,the dual norm under the L2 pairing is ||A^-.25v||2:
Cauchy-Schwarz proves <=; testing u=A^-.5v and normalizing proves equality
when v!=0. Completion gives exactly Hminus-half. Hence,with
 ||(u,v)||E_A^2=||A^.25u||2^2+||A^-.25v||2^2,M_K=L_K^.25,
 M_K^-1||z||E<=||z||E_A<=M_K||z||E,
 M_K^2=sqrt(3(1+K^2))<=2(1+K).                            (8)
The inverse lower constants are dominated by M_K because K>=1.

For unit L2 u, (5) gives q_V(u)>=z^2-1-Kz>=-K^2. Conversely take a
unit compact smooth bump,dilate it by a large scale and translate its
ENTIRE support outside supp m_R. Potential pairing0,kinetic energy->0.
Thus beta(V)=inf_unit_H1 q_V satisfies -K^2<=beta<=0,uniformly in value
although the test translations depend R. From PRIMARY(3.52)-(3.53),beta
is the spectral bottom: the spectral form integral is bounded below by
the spectral infimum; any nonzero bounded spectral slice below beta would
supply a unit form test below beta. Conversely a support point of the
projection-valued measure has nonzero arbitrarily small bounded spectral
slices,which give approximate eigenvectors and form tests approaching it.
Such support is nonempty since scalar spectral measures of unit vectors
have mass1. This verifies inf spectrum H_V=beta. Put lambda=sqrt(-beta)
<=K; every spectral h has h+c>=2. No eigenstate,gap or positive lambda.

Define C_t(h),S_t(h) by cos(t sqrt h),sin(t sqrt h)/sqrt h for h>0;
by1,t at h=0; by cosh(t sqrt(-h)),sinh(t sqrt(-h))/sqrt(-h) for h<0.
Under the E_A isometry the spectral wave matrix is
 [C_t(h), sqrt(h+c)S_t(h);
  -hS_t(h)/sqrt(h+c), C_t(h)].                            (9)
For h>=0,|C_t|<=1,|S_t|<=min(t,h^-1/2),upper offdiagonal<=1+sqrt(c)t,
lower<=1,with continuous value sqrt(c)t,0 at h=0. For beta<=h<0,
|C_t|<=exp(lambda t),|S_t|<=t exp(lambda t),upper<=sqrt(c)t exp(lambda t),
lower=sqrt(|h|)sinh(t sqrt(|h|))/sqrt(h+c)<=K exp(lambda t).
Since sqrt(c)<=2K,each entry is <=2(1+K)(1+t)exp(lambda t). PRIMARY3.1
bounds each operator entry; a2x2 block matrix has norm<=twice that bound.
Combining(8),
       ||P_V^E(t)||B(E)<=8(1+K)^2(1+t)exp(lambda(V)t).       (10)
Dominated spectral convergence and scalar addition formulas give a
strongly continuous group with these finite-horizon bounds.

Identify THIS spectral group with the actual physical Young flow at
FIXED R. The lift in Section2 belongs to old S's exact mathcalV_R.
From OWN S2 Section5,the E part of that fixed-R physical flow equals the
spectral wave of its represented form q_V. Its hypotheses are met: the
same real compact multiplier L,its F lift,common form domain H1 and
bounded conjugation primitive. Indeed S_E and its adjoint are strongly
continuous,so compact L has norm-continuous conjugates S_E(-v)L S_E(v);
their integral is Lipschitz. Thus the generic Young equation equals the
ordinary bounded-interaction equation,as required by that imported
Duhamel/core identification. Its generator's form is EXACTLY q_V above,
so PRIMARY2.14 uniqueness identifies H_V,independently of the old shift
chosen using ||L_F||. The spectral scalar functions C_t,S_t depend H_V,
not the auxiliary shift; on dense spectral-cutoff data the old/new groups
coincide,and boundedness extends equality to E. No old quantitative F
bound is transferred. All constants in (5)-(10) use k_E alone; chi_R and
||L_F|| occurred ONLY in this fixed-R identification.

Finally let V,W in this class have E norms<=K and let d0=||M_V-M_W||.
An eta-minimizer for W,0<eta<=1,has unit L2 norm and q_W<=1 because
beta(W)<=0. Equation(5) gives z^2-1-Kz<=1,hence z<=K+2. Therefore
 |q_V(u)-q_W(u)|<=d0||u||Hhalf^2<=d0(K+2).
Take infima,eta->0 and reverse V,W:
 |beta(V)-beta(W)|<=(K+2)d0,
 |lambda(V)-lambda(W)|<=sqrt((K+2)d0).                    (11)
The second inequality uses nonnegative -beta and the scalar square-root
inequality. This proves US1 with E norms only.

## 4. Uniform scalar-time averaging and integrated rates

Fix integer B>=1,0<delta<min(1,1/B),N=floor(1/(delta B)),n=N+1,
s_m=m delta B,ell_m=B for m<N,ell_N=delta^-1-NB in[0,B).
I_m=[s_m,s_m+delta ell_m] covers I up to endpoints. All Lr spaces for
operator fields below are Bochner Lr(I;K(E)) with the operator norm.
K(E) is separable; actual fields (1) are strongly measurable and remain
in the closed subspace mathcalV_E,R almost everywhere. No pointwise
representatives simultaneously for all controls are required.

Let A_delta^Z be averaging on each positive-length I_m for any Banach Z;
it is defined up to null sets,so endpoint values and an empty last cell
may be set0. Jensen gives ||A_delta^Z||Lr->Lr<=1. For continuous fields
on[0,1],the error is bounded by their uniform modulus at mesh<=delta B.
Such fields are dense in Bochner Lr,by simple-function approximation and
continuous approximation of scalar indicator functions. Contraction gives
strong convergence A_delta^Z f->f. In the scalar case and on the compact
closure of C_t's unit-ball image,this convergence is UNIFORM: take a
finite epsilon net,then use ||A_delta-I||<=2. Thus
           omega_delta=||(A_delta-I)C_t||H_t->Lr ->0.       (12)
This compactness is scalar time only.

On each finite tensor,Phi=sum f_j tensor h_j,Bochner integration commutes
with the fixed bounded spatial J_R,and
 A_delta^K(E) J_R(C_t tensor Id)Phi
                     =J_R((A_delta C_t)tensor Id)Phi.      (13)
Both sides are bounded on H_I by (1),contraction and U(15),so finite-tensor
density proves(13) on the COMPLETED supported raw space. With
W=mathcalT_R Phi,barW=A_delta^K(E)W,||Phi||<=M,Z=C_mean M,
 ||W||Lr,||barW||Lr<=Z,
 ||barW-W||Lr<=M_0 M omega_delta=:Omega_delta(M)->0         (14)
uniform R>=1. Averages stay in the same closed E class. There is no claim
that (C_t tensor Id) or the spatial family is compact; the accepted U
orthonormal spatial sequence refutes precisely that stronger claim.

Equation(11),pointwise with K(s)=max(1,||W1(s)||,||W2(s)||),and scalar
Cauchy-Schwarz yield
 int|lambda(W1)-lambda(W2)|
 <=sqrt(3+||W1||L1+||W2||L1)*sqrt(||W1-W2||L1).             (15)
All quantities are measurable by continuity of lambda on the E class.
Since I has length1,(14)-(15) give uniformlyR,
 Lambda_delta(M):=sup_ball int|lambda(barW)-lambda(W)|
 <=sqrt(3+2Z)*sqrt(M_0 M omega_delta)->0.                  (16)
Rate_R(Phi)=int lambda(mathcalT_R Phi) is nonnegative,finite and continuous
on H_I; lambda(L)<=max(1,||L||) gives Rate<=1+C_mean||Phi||. This proves US2.

## 5. E-only primitive,Young and mean-baseline budgets

Write ||D||theta=sup||D||+[D]_theta. Let
 G_B=sup_(|v|<=B)||S_E(v)||,
 C_B=G_B^2[B^(1-1/r)+B^(1-1/r-theta)].
The Bessel-unitary Fourier free matrix has diagonal cos(vk),upper
sqrt(1+k^2)sin(vk)/k and lower -k sin(vk)/sqrt(1+k^2),with valuev,0 at k=0.
Split k<=1 and k>=1 to bound the upper by sqrt(2)B; other entries<=1.
Frobenius gives G_B<=sqrt(3+2B^2)<=3B. Also G_B>=1 from v=0,hence
 C_B<=18B^(3-1/r)<=32B^(3-1/r), C_B B^(1/r)>=B.            (17)
For any W in Lr,its actual stopped primitive
 H_m(u)=int_0^min(u,ell_m) S_E(-v)W(s_m+delta v)S_E(v)dv
is a zero-start little-theta-Holder compact-operator path on[0,B]. Holder
in time with exponent1-1/r>theta gives
 ||H_m||theta<=a_m:=C_B delta^-1/r||W||Lr(I_m),
                delta sum a_m^r<=C_B^r||W||Lr^r.          (18)
Constant stopping and conjugation preserve this estimate,including ell=0.
These are the C3/U primitive estimates with the E constants just checked.

The generic Young piececount from OWN E1 Section2 applies to B(E),whose
multiplication has norm1. With c_theta=2max(1,C_Young),d=||D||theta:
if c_theta d B^theta<=1/4,the whole-interval contraction gives log sup||U_D||
<=1/2. Otherwise at most2B(4c_theta d)^nu pieces each of norm<=4/3 give
log sup||U_D||<=2B(4c_theta)^nu log(4/3)d^nu. Combining logG_B<=log(4B),
we can take the SAME sufficient model-independent positive constant
 Ctheta=4+log4+2(4c_theta)^nu,
 log||S_E(ell)U_D(ell)||<=Ctheta B(1+d^nu),0<=ell<=B.       (19)
This verifies the new E application of B1,not an unspecified C(B).
Equation(2) likewise applies with the nonzero Hilbert phase E and ANY
bounded left multiplier S_E(ell); its constant depends only theta,B,K.

For actual W=mathcalT_R Phi,the mean endpoints Pmean_m=S_E(ell_m)U_Hm(ell_m)
have norm>=1 by OWN SP4. Here is the exact fit: U Sections2/6 constructs
J_R and (1) as the E restriction i^*mathcalT_F i of C3's completed field.
SP Section7 (19)-(23) uses that SAME compression and the SAME physical mask
eta_root(x/R)^2 after smoothing. At each fixed delta its fast direction
phi_m=delta^-a/2 T_m^*Phi is a finite raw vector,identifying this primitive
up to ell_m and then constant stopping. Its norm is NOT a uniform cost.
SP's c=0 pure-mean symplectic identity therefore gives
             ||Pmean_m||>=1, every R,Phi,delta,m.          (20)
For pure means this identity is deterministic; no uncountable random
exceptional-set intersection is needed. Empty endpoint isI. Both velocity
components and all actual clocks are unchanged. No F constant coordinate
or residual symplecticity is used in(20).

## 6. Full good/bad blocks and true last cell

For nonempty I_m let barM_m be its OWN Bochner average; set barM_N=0 if
empty. Define Hbar_m from this constant and let
 e_m=C_B delta^-1/r||W-barW||Lr(I_m).
Jensen and(18) give
 ||Hbar_m||theta<=a_m, ||H_m-Hbar_m||theta<=e_m,
 delta sum e_m^r<=C_B^r Omega_delta(M)^r,
 delta sum a_m^r<=D_M:=C_B^r Z^r.                          (21)
On FULL cells only, ||barM_m||<=(delta B)^-1/r||W||Lr(I_m)
=a_m/(C_B B^(1/r))<=a_m/B. No such full-length formula for the short last.

We will use the exact finite Holder bounds
 delta sum e_m<=(delta n)^(1-1/r)(delta sum e_m^r)^(1/r),
 delta sum e_m^nu<=(delta n)^(1-nu/r)(delta sum e_m^r)^(nu/r). (22)
These follow from supplied complete Mathlib powermean at exponents r>=1,
r/nu>1 and values e_m>=0,e_m^nu>=0,respectively,then positive powers and
multiplication by delta. n=N+1>=2,delta>0; no negative/zero-cardinality
powers occur. This is an analytic application of an old finite type,not
new numeric zero-case tests or a new kernel statement. Because delta n<=2/B,
 delta sum(e_m+e_m^nu)<=
 (2/B)^(1-1/r)C_B Omega_delta(M)
 +(2/B)^(1-nu/r)C_B^nu Omega_delta(M)^nu=:Efree_delta ->0,  (23)
uniformR at each fixed B,M.

Fix K>=1; split FULL indices m<N into good a_m<=K and bad a_m>K.
On a good block apply(2) with base Hbar_m,perturbation H_m-Hbar_m,left
multiplier S_E(B). The baseline endpoint is EXACTLY the actual static
physical flow of barM_m by US1's fixed-R identification. Its E norm budget
<=K/B<=K and K>=1 allow the larger sufficient static bound. Thus
 log||Pmean_m||<=L_BK+B lambda(barM_m)
                         +C(theta,B,K)(e_m+e_m^nu),
 L_BK=log16+4log(1+K)+3log(1+B).                           (24)
No noncommuting flows have been equated. Good prefactors sum to at most
L_BK/B because delta N<=1/B. Rates satisfy
 delta sum_good B lambda(barM_m)<=int_I lambda(barW)
                         <=Rate_R(Phi)+Lambda_delta(M).   (25)
Dropping bad,last/empty rate cells is valid since lambda>=0.

On bad full cells (19) gives Ctheta B(1+a_m^nu). Since a_m>K>=1,
 1+a_m^nu<=(K^-r+K^(nu-r))a_m^r.
Using(17),(21),their delta-weighted sum is at most
 Ctheta32^r Z^r B^(3r)(K^-r+K^(nu-r)).                     (26)
If ell_N=0,the last factor isI and lognorm0. Otherwise use (19) on the
ACTUAL stopped path,not the frozen average. From a_N<=C_B delta^-1/r Z,
 delta log||Pmean_N||
 <=Ctheta B[delta+C_B^nu Z^nu delta^(1-nu/r)]=:Last_delta->0 (27)
for fixed B,M since nu<r,uniformR even for arbitrarily short last cells.
No division by their tiny length and no velocity discarded.

Combining(23)-(27) gives a finite-delta deterministic bound,uniformR/Phi:
 delta sum log||Pmean_m||-Rate_R(Phi)
 <=L_BK/B+Ctheta32^r Z^r B^(3r)(K^-r+K^(nu-r))
   +Lambda_delta(M)+C(theta,B,K)Efree_delta+Last_delta.     (28)
The last three terms vanish at FIXED B,K,M. Taking suprema then limsup
delta proves US3a. No F norm or cutoff reconstruction constant appears.

## 7. Polynomial control balls and deterministic suprema

Rename the target's radius parameters to c_ball>0,kappa_ball>=0 to avoid
M_0 (spatial-map norm) and block index m. Put M_B=c_ball B^kappa_ball,
and choose s>r(3+kappa_ball)/(r-nu),K_B=B^s. At each B the inner delta
limit in(28) has fixed finite radius/threshold. The bad terms become
 Ctheta32^r C_mean^r c_ball^r
 [B^(r(3+kappa_ball)-sr)+B^(r(3+kappa_ball)+s(nu-r))].       (29)
Both exponents are strictly negative: the second by choice,and the first
because r/(r-nu)>1 implies s>3+kappa_ball. Meanwhile
 L_(B,K_B)/B<=[log16+7log2+(4s+3)logB]/B ->0.              (30)
This proves US3b with delta FIRST,then integer B->infinity. Even rapidly
growing freezing-error constants were removed in the inner limit. No
prescribed diagonal B_delta,M_delta follows.

At each fixed R,B,delta,the mean primitive is a bounded linear map of
Phi into a separable finite product of little-Holder K(E) spaces. Young
endpoints are locally Lipschitz; their norms are positive,so their logs
are continuous. Rate is continuous by(15). All deterministic suprema on
closed control balls are finite by (18)-(19) and are suprema of Borel
continuous functions of Phi. Separability gives a countable dense subset
of each closed ball with the same supremum. Uniform suprema over R are
ordinary deterministic real suprema,not random measurability assertions
or an assumed compact R-parametrized family. These observations likewise
apply to the residual/control product balls below.

## 8. Arbitrary residuals: good/bad comparison and max1 ordered product

Let x_m be ANY zero-start little-theta-Holder compact-operator paths on
[0,B],v_m=||x_m||theta,Y=(delta sum v_m^p)^(1/p). No Hamiltonian,Gaussian
or Cameron condition. Define Ppert_m=S_E(ell_m)U_(H_m+x_m)(ell_m).
Free/Young evolutions are invertible (OWN E1 Section2),so all endpoint
norms are positive. Put z=product_m ||Ppert_m||/||Pmean_m||.

For any fixed Kres>=1,on ALL cells with a_m<=Kres,(2) gives logratio
<=C(theta,B,Kres)(v_m+v_m^nu),with the actual physical left endpoint.
On bad cells a_m>Kres,use(19),convexity
(a+v)^nu<=2^(nu-1)(a^nu+v^nu),and the mean denominator>=1 in(20).
The logratio is then <=c_B(1+a_m^nu+v_m^nu),with c_B positive independent
Kres,R,delta,Phi,M. Increase C_Kres to dominate both c_B and the good
constant. Summation and(21) imply,with a NONNEGATIVE right side,
 log max(1,z)<=C_Kres sum(v_m+v_m^nu)
                +c_B sum_(a_m>Kres)(1+a_m^nu).
Here logmax follows because logz is bounded by that nonnegative number.
The bad sum is <=D_M/delta*(Kres^-r+Kres^(nu-r)).
Apply the same complete finite powermean type at exponents p>=1,p/nu>=1
and values v_m,v_m^nu>=0. After positive powers,
 delta sum v_m<=(2/B)^(1-1/p)Y,
 delta sum v_m^nu<=(2/B)^(1-nu/p)Y^nu.
Equality p=nu and zero entries cause no singular powers. Consequently
 delta log max(1,z)
 <=C_Kres[(2/B)^(1-1/p)Y+(2/B)^(1-nu/p)Y^nu]
          +c_B D_M(Kres^-r+Kres^(nu-r)).                  (31)
All constants uniformR; this proves US4a with SP mean denominator only.

Let Aprod=product_m||Pmean_m||>=1. Submultiplicativity gives
 ||Ppert_N...Ppert_0||<=Aprod*z,
 max(1,||ordered product||)<=Aprod*max(1,z).
Thus,with F=2delta logmax(1,||ordered product||),
       F-2delta sum log||Pmean_m||<=2delta logmax(1,z).     (32)
This is an inequality,not operator commutation or scalar displacement
multiplication. F is defined continuously on ALL tuples by generic Young,
including nonphysical residuals; it is not an a.s.-only solution map.

Fix B,M and any deterministic b_delta>=0 with b_delta->0. On Y<=b_delta,
(31)-(32) give limsup_delta of the uniform excess <=
2c_B D_M(Kres^-r+Kres^(nu-r)) for EVERY Kres>=1. Let Kres->infinity AFTER
delta: r>nu gives0. At each B use M=M_B; combine with(28)-(30),taking
suprema of sums no larger than sums of suprema. This proves
 limsup_B limsup_delta sup_(R>=1,||Phi||<=M_B,Y<=b_delta)
                  [F-2Rate_R(Phi)]<=0.                   (33)
This is US4b. It assumes only fixed-B smallness of b_delta. The actual SA
anchor on R_delta may later supply such a sequence; no uniform-R random
noise bound or future Rayleigh-score application is inferred here.

## 9. Evidence and remaining original objective

All ten statement notes adjudicated: typed fields/distinct radius names,
U/SP exact one-mask means,fixed-R E reconstruction/actual identity without
uniform F constants,completed averaging identity and deterministic-sup/
last-block/zero-guard duties are explicit above. The review's Q2 note was
incorrect: balanced finite k=0,b=1,V=-4,h=4,t=pi/4 gives [0,1/2;-2,0].
It is a realizable finite Fourier comparator,not a compact masked spatial
PDE or uniformly bounded slow Cameron control. Exact product/displacement
negative controls remain valid. 150raw/145configs/30t0/116distinctnonzerotime,
7raw/6distinct wrong-prefactor,11/11wrong-rate,36exactcell checks are not
independent samples or infinite-dimensional proofs. No diagnostic rerun.
40digit formula maximum is aggregate only; no complete40digit row-residual
custody claimed. Numerical consistency is not a certified enclosure.

PRIMARY theorems imported at exact pinpoints; accepted own inputs used
only at their labeled scopes. All form/domain/spectral/averaging/Young/
operator/limit claims remain INFORMAL analysis,not Lean. Old full Mathlib
AMGM/powermean types reused with their actual guards; no new kernel/source/
compiler/factcount74facts20seams/L0. Historical upstream counts not rewritten.

This is a complete UNREVIEWED uniform E spectral/product proof,not a sharp
moment theorem. BT Rayleigh signed-score integration and its explicit
bulk/tail/normalizer limits,signed-positive variational/mask removal,
intended source normalization/constants and conditional exact limit remain
OPEN. No p1 auxiliary-label identity,Skorohod/contact/HPC/companion/source
repair/TeX/PDF/wiki/bib/sibling/public action. Original full goal ACTIVE.
