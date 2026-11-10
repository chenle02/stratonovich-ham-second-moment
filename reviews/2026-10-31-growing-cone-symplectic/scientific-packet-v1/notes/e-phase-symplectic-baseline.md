# Actual E symplectic evolution and deterministic block-mean norm baseline

UNREVIEWED COMPLETE PROOF CANDIDATE. SP1-SP4 statement/source/old-scalar-
application gate passed Opus5.5/HIGH at frozen240f907 (20checks,413.721s),
with all11optional findings adjudicated at179e629. This note supplies the
full proofs and exact block application. It needs its own FULL independent
gate before adoption. Norm>=1 is not a growingR upper or sharp constant.
The original all-model sharp-point/source goal remains ACTIVE.

## 1. Model, distinct objects and exact new claims

Keep ALL original nonzero H:homog Gamma/amplitudes,d=1,2,3,0<a<1,
0<alpha<d or alpha=d=1,alpha+a<2. All spaces are REAL,with unitary Fourier
and Lambda=(1-Delta)^(1/2). Set E=H^(1/2) x H^(-1/2),F=E directsum R2,
i:E->F the closed isometric inclusion,i^*:F->E its Hilbert adjoint.
Fix finite R,T>0,real scalar c,physical mask m_R=eta(x/R)^2 ONCE,where
eta is real even smooth compact,0<=eta<=1,eta1 onB1,suppB2. Sources are
smoothed before this physical mask,not inside the raw covariance quotient.
Choose accepted auxiliary gamma and Holder exponents
 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<beta<min(1-a/2,(3-a-alpha)/2).
The ranges are nonempty by the original strict subcritical assumptions.

Let H_raw be the full positive-time raw noise Hilbert completion and W
its GIVEN isonormal process. Let M=M_R(W) be the actual E B(E)-valued first
interaction path on[0,T],and M_rho the actual retaining-source paths from
source-operator-convergence.md. They have compact values,separable closed
Ctheta path spans and all finite Gaussian moments. Here rho denotes ONLY
the positive heat/Laplace source pair. For ANY FIXED Phi in H_raw define
 Z=W(Phi), D_Phi=E[Z M], D_Phi,rho=E[Z M_rho],
 D=c M+D_Phi, D_rho=c M_rho+D_Phi,rho.                       (1)
These are E operator paths. D_Phi is a deterministic completed covariance
mean,not an asserted pointwise raw potential. Let U_D be the actual LEFT
Young evolution and P_D(t,s)=S_E(t)U_D(t,s)S_E(-s) its physical flow.
Use J_symp below for a symplectic operator,never a noise projection rank.
The balanced isometry C_bal below is the driver note's J0. In Section7
mathcalT_E denotes a mean-field map,T_m a raw time pullback,and B a horizon.

We prove for all0<=s<=t<=T,on one path set for these FIXED c,Phi,R,T,
       P_D(t,s)^* J_E P_D(t,s)=J_E, ||P_D(t,s)||B(E)>=1.     (2)
P_D is also invertible by actual Young/free evolution,not by inferring
surjectivity from the form identity. The statement includes c=0 pure means,
Phi=0 rawnoise,and the free case. We then identify the EXACT actual block
mean in Section7 with a covariance mean of the form(1),and obtain its
norm>=1 at the true endpoint. No uniform mean budget or upper follows.

Direct OWN accepted inputs,checked for new uses,not recertified:
- actual-operator-driver.md Theorem/Sections1,3,9,scientific93d71e4:
  balanced real E,full massless group,same-W first-driver construction,
  literal completed rows,separable Gaussian Ctheta paths,sqrt(p) moments.
- source-operator-convergence.md Theorems1-2/Sections4-7,scientificda9d464:
  actual retaining source/G-vector representation,all finite Lp Ctheta
  convergence,covariance contractions,source smoothness and actual ordinary
  FIRST source primitive on E,including indicator rows and fixed parameters.
- fixed-mask-young-constant-phase.md Sections2-5,scientific8ad5094:
  actual F extension/free identities A_F i=i M_E,source ordinary Duhamel
  equation on states,Young uniqueness/inverse/local Lipschitz dependence,
  all finite moments/source differences and physical conjugation.
- upper-cameron-compactness.md Sections4,6,7(12),scientifice0a6f3e:
  supported slow H_I,actual completed mean mathcalT_F in Lr(I;K(F)),range
  in iE,full source/raw covariance identity,partial/empty block conventions.
- raw-block-event-lower.md Section2,scientificd4d876e: actual raw test
  isometry and same-W fast noises. No independence of temporal blocks.
- Complete old JointTilt.shifted_amplitude source/type fixture: scalar
  amplitude relation only,with actual delta>0 and positive denominators.
No GC/U/SA estimate or old d1 Hilbert-Schmidt assembly is a premise.

## 2. The bounded symplectic form and the full free-wave identity

C_bal:E->L2(R^d;R2), C_bal(u,v)=(Lambda^(1/2)u,Lambda^(-1/2)v)
is an onto real isometry by the Bessel definitions. On L2xL2 define
 J_symp(q,p)=(p,-q), J_E=C_bal^-1 J_symp C_bal.
Thus J_E is bounded,isometric,skew-adjoint,J_E^2=-I and ||J_E||=1.
For z=(u,v),w=(f,g),
 omega(z,w)=<z,J_E w>_E=dual(u,g)-dual(f,v),                 (3)
where dual is the real H1/2,H-1/2 pairing. Indeed C_bal places the two
terms in the L2 pairing. Explicitly J_E(f,g)=(Lambda^-1g,-Lambda f).
There is no L2 pairing of a general distributional velocity.

In balanced Fourier coordinates the free wave matrix is
 W_t(xi)=[cos(tk),<xi>sin(tk)/k;
          -k sin(tk)/<xi>,cos(tk)], k=|xi|.                 (4)
The sine quotient has its continuous value t at k=0,so at zero the
matrix is [1,t;0,1]. Every entry is real and even in xi,and the matrix
is bounded on finite time horizons; this is the actual massless free
group,not a Bessel-mass replacement. Direct 2x2 multiplication gives
 W_t(xi)^tr J_symp W_t(xi)=J_symp,
since its determinant is cos(tk)^2+sin(tk)^2=1 (also at zero).
For real physical phases the Fourier vectors have Hermitian symmetry;
the real E pairing is the real part of the complex Fourier L2 pairing.
The pointwise matrix identity therefore integrates to
               omega(S_E(t)z,S_E(t)w)=omega(z,w).           (5)
All products are integrable by L2 Cauchy-Schwarz and the finite-horizon
matrix bound. Equivalently start on Schwartz phases,then use density and
boundedness to extend(5) to ALL E. No differentiation of the unbounded
wave generator,no frequency-zero trace,and no pointwise Sobolev evaluation
is used. Strong time continuity is all that will be needed below.

For any bounded real smooth spatial b, B(b)(u,v)=(0,bu) is bounded on E:
 ||bu||H-1/2<=||bu||2<=||b||infinity||u||H1/2.
Since u,f in H1/2 are L2,and bu,bf are L2 subsetH-1/2,the actual duality
gives the absolutely integrable cancellation
 omega(B(b)z,w)+omega(z,B(b)w)
          =-int f b u+int u b f=0.                         (6)
This is omega-skew,not skew-adjoint for the E Hilbert inner product.

## 3. Completed covariance means and their actual source coefficients

The separable Gaussian path moments imply Bochner existence in(1):
 E||Z M||Ctheta<=||Phi||H_raw ||M||L2(Ctheta)<infinity,
and similarly for M_rho. Bounded linear testing commutes with these
Bochner expectations. Cauchy-Schwarz gives
 ||D_Phi,rho-D_Phi||Ctheta
       <=||Phi||H_raw ||M_rho-M||L2(Ctheta)->0,             (7)
and the source contraction bounds give uniformly rho
       ||D_Phi,rho||Ctheta<=||Phi||H_raw ||M||L2(Ctheta).    (8)
These are fixed-R,T deterministic budgets,not uniform in Phi or delta.
There is no H_raw-valued standard Gaussian variable.

On the retaining extension,the source note gives a real isometry
j_src:H_raw->G and an isonormal I on G with I(j_src h)=W(h).
The actual source pointfield is Y_rho(t,x)=I(v_rho;t,x),with G-valued
spatial derivatives and joint G-norm continuity at each positive rho.
Consequently
 h_Phi,rho(t,x)=E[W(Phi)Y_rho(t,x)]
                   =<j_src Phi,v_rho;t,x>G                (9)
is a deterministic real function,time continuous and spatially smooth,
with all spatial derivatives jointly continuous on compact sets. Bounded
linearity of the G inner product commutes with those derivatives. This
uses no expected source supremum or pointwise raw potential for Phi.
After multiplying by m_R it has one compact spatial support and bounded
derivatives on[0,T].

The actual source primitive identity is
 D_Phi,rho(t)=int_0^t S_E(-r)B(m_R h_Phi,rho(r))S_E(r)dr,     (10)
as a statewise integral giving a Lipschitz B(E) path. Here is its exact
identification,not a formal expectation of an operator derivative. On
Schwartz states its row is the scalar integral of h_Phi,rho against the
literal masked wave product of source note(19). Ordinary Fubini interchanges
E[Z Y_rho] with that integral: on this fixed compact time/spatial row,
|E[Z Y_rho(t,x)]|<=||Phi||sqrt(EY_rho(t,x)^2),with finite bounded point
variance at fixed rho,and the deterministic row is absolutely integrable.
The source note's test/indicator approximation extends this equality to
its actual completed row,also by Gaussian Cauchy-Schwarz and covariance
contraction. Thus it equals E[Z<M_rho(t)z,w>],the row of D_Phi,rho.
Countable dense states and rational times,then boundedness/continuity,
identify the operator paths. No pointwise evaluation of raw noise or
unjustified B(E)-valued Radon-Nikodym derivative is required.

The actual combined source driver D_rho is therefore the ordinary first
primitive with coefficient
       b_rho(t,x)=m_R(x)[c Y_rho(t,x)+h_Phi,rho(t,x)].         (11)
Its random component is centered Gaussian,but the combined source is
NONCENTERED. The physical mask appears ONCE in both terms.

## 4. Ordinary source conservation by the bounded interaction equation

Fix positive rho and its probability-one Ct spatially smooth source event.
b=b_rho has a common compact support and is continuous in sup norm,with
finite uniform sample bound on[0,T]. The interaction coefficient
             C_b(r)=S_E(-r)B(b(r))S_E(r)
is uniformly bounded and strongly continuous ON STATES. This follows
from strong continuity/free bounds and norm continuity of B(b(r)); it
does not assert norm differentiability of S_E. By(5),(6),
       omega(C_b(r)z,w)+omega(z,C_b(r)w)=0                  (12)
for every r,z,w.

The accepted source first-response identity and(10) identify the Young
state equation with the ordinary interaction equation
 U_rho(t,s)e=e+int_s^t C_b(r)U_rho(r,s)e dr.                 (13)
Indeed Young Riemann sums replace each driver increment by its statewise
integral; their difference from(13) is bounded by the uniform coefficient
bound times the uniform continuity error of U_rho on the partition.
Thus the integrand in(13) is strongly continuous in E. The elementary
strong-integral difference quotient converges to its integrand,so each
state U_rho(t,s)e is C^1 in t and has derivative C_b(t)U_rho(t,s)e.
The original free generator was never differentiated on a rough E state.

Since omega is a bounded bilinear form,differentiate
omega(U_rho(t,s)e,U_rho(t,s)f). Equation(12) gives derivativezero,hence
 omega(U_rho(t,s)e,U_rho(t,s)f)=omega(e,f).
The argument is pathwise on the same coefficient-regularity event for ALL
states and time pairs: bounded ordinary evolution is defined there on all
E; it is not an uncountable intersection of exceptional state events.
Free conjugation using(5) now gives
                  P_rho(t,s)^*J_E P_rho(t,s)=J_E           (14)
for every0<=s<=t<=T on this event. This proves SP1 for the actual ordinary
source,including signed sample potentials and deterministic source means.

## 5. Noncentered actual Young convergence and raw conservation

All actual Gaussian first-source paths have uniform sqrt(p) norm moments
at fixed R,T by the source contraction and accepted driver theorem. The
deterministic means satisfy(7)-(8). Therefore
 ||cM_rho+D_Phi,rho||Lp(Ctheta)<=C_(c,Phi,R,T)sqrt(p),p>=1,
and the combined drivers converge to D in every finite Lp Ctheta.
The elementary Gaussian moment-series estimate gives uniform square-
exponential moments for those shifted path norms. These are bounds on
Gaussian plus bounded deterministic shifts,not a claim the sources(11)
are centered.

The accepted Young local-Lipschitz estimate gives evolution convergence
in probability on each driver ball. Uniform Gaussian tails make the
complement small. The Young global growth is bounded by
 C_T exp(C_T(1+||D_rho||Ctheta)^(1/theta)),1/theta<2.
Square-exponential driver tails imply all finite evolution moments uniformly
rho,so uniform integrability upgrades to all finite Lp convergence of the
interaction evolutions in the UNIFORM time-triangle operator-difference
norm. Multiplication by the bounded free groups gives the same physical
difference convergence. No operator-norm continuity of the physical free
group itself is being asserted.

For completeness the E/F restriction also holds for these mean shifts.
The accepted F driver extension has A_F i=i M,and its source counterpart
A_F,rho i=i M_rho. Bounded Bochner expectation with Z gives the same
intertwining for D_Phi and D_Phi,rho. Thus the combined F driver restricts
to D or D_rho. Applying i to E Young sums and using state uniqueness gives
U_F i=i U_E; free conjugation gives P_F i=i P_E. Closed isometric inclusion,
not E denseF,is used. This checks the actual source/mean evolution object,
rather than inventing a second spectral group.

Choose a countable source sequence rho_n->0 and then a subsequence whose
expected squared uniform physical difference is at most2^(-4n). Markov
bounds make the probabilities of difference>2^-n summable; the probability
of any such event after indexN is bounded by the corresponding tail sum,
which tends to0. Hence the differences converge uniformly in operator
norm over ALL time pairs almost surely on a further path set. Intersect
with the countably many source conservation events. Uniform convergence
also bounds all involved operator norms,and
 ||P_n^*J_E P_n-P^*J_E P||
    <=||P_n-P|| ||J_E|| (||P_n||+||P||)
then passes(14) to P_D simultaneously for all time pairs. No common event
over uncountably many Phi,c,R,delta or cutoffs has been claimed.
This proves SP2. If c=0,all raw/source mean paths and their evolutions
are deterministic,so this result holds deterministically for each Phi;
there is no probabilistic parameter exception for a deterministic mean-
ball supremum. The same argument covers Phi=0,c=0 and the zero source.

## 6. Norm baseline and actual inverse

The real Hilbert adjoint has ||P^*||=||P||. Since ||J_E||=1,SP2 implies
           1=||P_D^*J_E P_D||<=||P_D||^2,
hence ||P_D(t,s)||>=1. This uses only bounded-operator norm submultiplicity.
Surjectivity does NOT follow from that symplectic identity alone in an
infinite-dimensional Hilbert space. It follows instead from the actual
Young evolution: on short contraction pieces ||U-I||<=1/3,the Neumann
series gives an inverse; finite products and S_E inverses give P_D inverse.
This proves SP3,with no eigenstate,determinant of the full phase,positivity,
spatial point trace or uniform growingR moment assertion.

## 7. Exact slow/fast completed block-mean application

Now specify every SP4 parameter. Fix integer B>=1,0<delta<min(1,1/B),
N=floor(1/(delta B)),s_m=m delta B,ell_m=B for m<N and
ell_N=1/delta-NB in[0,B). R>0 is fixed for each identity instance; it may
be chosen R=1/delta+2 AFTER delta is fixed. Use SP2 horizon T=B>0,and
handle ell_m=0 separately below. Let H_slow=H_W be the full positive-time
slow raw space and H_I its closed supported subspace on I=(0,1),with
j_I:H_I->H_slow the isometric inclusion. Let H_fast be the positive-time
raw completion with the same covariance. The actual isometry is
 T_m f(s,x)=delta^(a/2-1)f((s-s_m)/delta,x),                  (15)
where f is extended by zero so the expression vanishes for s<=s_m.
Its covariance factors are delta^(a-2)delta^2delta^-a=1,so it respects nulls
and extends as an isometry H_fast->H_slow. Its Hilbert adjoint T_m^* is a
contraction. No physical time-indicator action on the raw quotient is used.
The ACTUAL fast noise is W_m(f)=W(T_m f); all m remain on the same W.

Fix any Phi in H_I,write Z_slow=W(j_I Phi),and set
                phi_m=delta^(-a/2)T_m^*j_I Phi.             (16)
This has norm at most delta^(-a/2)||Phi||,finite perdelta,NOT a uniform
control-radius bound. Let M_m=M_R(W_m) on[0,B] be the unscaled actual E
first driver. Its completed covariance direction is
       D_(phi_m)(u)=E[M_m(u)W_m(phi_m)].                    (17)
For its source approximation in SP2,we choose sourceTheorem2 with W_m as
the actual given isonormal process,extending the original probability space
by an independent auxiliary source. This retains all base variables. A
slow-source pullback would also be admissible,but is not presumed here.
The raw deterministic object(17) is independent of the source realization.

The slow mean field mathcalT_F Phi belongs to Lr(I;K(F)) and has range
in closed iE,as in accepted C3. Define its ACTUAL E compression
 mathcalT_E Phi(t)=i^* mathcalT_F Phi(t)i in K(E).           (18)
The compression is bounded linear,so strong measurability and Lr bounds
pass to E. Choose accepted C3 exponents
 1/(1-theta)<r<2/a,1/theta<=p<2<r,
which exist because theta<1-a/2. Constant columns are inactive on iE inputs;
they were NOT discarded in forming the original F driver or mean.
Define the stopped E primitive on[0,B]
 H_(m,E)(Phi)(u)=int_0^min(u,ell_m)
     S_E(-v)mathcalT_E Phi(s_m+delta v)S_E(v)dv.             (19)
The actual free conjugation is norm-continuous on compact operators,by
strong continuity of S_E and its adjoint and compact approximation. Thus
(19) is Bochner defined and Ctheta by the accepted r-budget/primitive bound;
affine time pullback preserves null sets. No point potential is presumed.

Accepted C3(12) at RAW PROJECTION RANK ZERO (not J_symp=0) gives on F
 E[g_delta A_(F,m)(u)Z_slow]=sqrt(delta)H_(m,F)(Phi)(u),
             g_delta=delta^((1-a)/2),0<=u<=ell_m.           (20)
Compress through i,using A_(F,m)i=i M_m,S_F i=i S_E and(18). Bochner
covariance commutes with this bounded compression. The complete old scalar
JointTilt.shifted_amplitude,delta>0,g_delta>0,sqrt(delta)>0,gives
 g_delta delta^(a/2)=sqrt(delta).
Dividing(20) by the positive g_delta therefore gives
 E[M_m(u)Z_slow]=delta^(a/2)H_(m,E)(Phi)(u),0<=u<=ell_m.      (21)
This is the UNSCALED covariance; assigning it sqrt(delta) would be wrong.
The completed C3 identity applies to ALL Phi in H_I by its bounded raw-
Hilbert/dense-test extension,not only positive or smooth directions.

To match(17),observe that T_m T_m^* is the orthogonal projection onto its
closed range. The Gaussian difference
 Z_slow-W_m(T_m^*j_I Phi)=W((I-T_m T_m^*)j_I Phi)
is orthogonal to the entire fast first chaos. Each continuous linear
coordinate of M_m is an L2 limit of finite W_m-basis sums,so its covariance
with that difference is zero. Bochner covariance exists by L2 path moments;
bounded linear tests separate its values. Hence
 E[M_m(u)Z_slow]=E[M_m(u)W_m(T_m^*j_I Phi)]
as an operator path. Multiply by delta^(-a/2),then(16),(17),(21) give
       D_(phi_m)(u)=H_(m,E)(Phi)(u),0<=u<=ell_m.             (22)
For u>ell_m no unstopped equality is asserted. Equivalently define
D_(phi_m)^stop(u)=D_(phi_m)(min(u,ell_m));then it equals(19) on ALL[0,B].
This is the precise partial-block covariance/source application.

Apply SP2-SP3 with c=0,horizon B,reference W_m and deterministic direction
phi_m. Equality of drivers on[0,ell_m] and Young uniqueness give the same
endpoint. Therefore the ACTUAL pure-mean E block satisfies
 ||S_E(ell_m)U_(H_(m,E)(Phi))(ell_m,0)||B(E)>=1.              (23)
If ell_m=0 it is I and the norm is1,without needing a zero positive horizon.
All identities are fixed-delta/R instances; deterministic Phi arbitrary.
This proves SP4 and supplies the actual E mean-block denominator,not a
uniform control budget or a replacement for the F constant-column argument.

## 8. Finite evidence, zero covariance and remaining goal

If Gamma=0,the raw Hilbert mean/noise drivers vanish and the result is
free-wave(5). All original nonzero covariances,including d1white,were
retained; no spectral density or angular regularity was needed.

The old complete JointTilt source/type fixture is unchanged. Its scalar
amplitude identity is used exactly at delta>0 with positive sqrt/g,as in
Section7. It does not certify Sobolev duality,free Fourier integration,
source G-vector/primitive,Gaussian/Bochner limits,Young convergence,
Cameron means or raw adjoint projection. The finite symplectic evaluator
has one free and three nonzero signed-potential cases; v1 wrong Bessel
force weight remains preserved and v2 corrects the physical similarity.
The block-direction tests check finite adjoint/scalar bookkeeping only;
their mean identity by definition is not used to prove(21)-(22).
No new Lean theorem/compiler/count:74facts20seams/L0 PROPOSED unchanged.

This is a COMPLETE UNREVIEWED proof of the norm baseline and exact block
mean application only. It makes no stochastic growingR/operator upper,
nonlinear-product ratio,pointsharp/source-energy/normalization/exactlimit,
novelty,human or whole-paper claim. No contact,Skorohod development,HPC,
companion,TeX/PDF/wiki/bib/sourcePDF/sibling/publication action.
