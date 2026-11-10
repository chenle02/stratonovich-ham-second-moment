# Finite signed occupation scores and entrywise Gram comparison

ACCEPTED at the scoped FULL analytic/source/type/finite-application gate:
scientific4e2219d,actualOpus5.5/HIGH,26checksPASS,305.393seconds,no required
repairs. All48five-way input bindings and63nativearchive members verified
BEFORE optional clarity edits; all7minor findings adjudicated in
reviews/2026-10-31-positive-gram-variational/scientific-adjudication-v1.md.
Frozen packet proof/report unchanged. Four public finite algebraic facts
and a private integrated active-branch consumer passed local source/type/
axiom/replay/control and exact PG-application fidelity; evidence in
lean-progress/local-checks/positive-gram-v1/. Whole PG1-PG2 optimization
remains reviewed INFORMAL analysis,not a kernel theorem or a physical
application. Original all-model sharp/source goal remains ACTIVE.

## 1. Exact statement and conventions

Let H be ANY real Hilbert space,I a finite index set,k_i in H,
ell_i>0,b_i>=0. Put C_ij=<k_i,k_j> and assume C_ij>=0 for EVERY i,j.
This is weak entrywise nonnegativity,not strict positivity,independence,
componentwise positivity of label coordinates,or invertibility. A Gram
matrix is symmetric and PSD because
 sum_ij a_i C_ij a_j=||sum_i a_i k_i||^2>=0.
Define t_+=max(t,0),and
 F(Phi)=2sum_i ell_i sqrt((<Phi,k_i>-b_i)_+)-||Phi||^2/2,
 S= sup_(Phi inH)F(Phi).
Let J={i:k_i!=0}={i:C_ii>0}. Zero labels contribute0 because b_i>=0,
so they may be discarded. I=empty,J=empty and H={0} are permitted.

For each nonempty A subsetJ and positive weights w=(w_i)_(i inA),put
 D_A(w)=sum_(i inA)ell_i^2/w_i-sum_(i inA)b_i w_i
                  +(1/2)sum_(i,j inA)w_i C_ij w_j,
 d_A=inf_(w_i>0)D_A(w).
Set d_empty=0. We prove
                 S=max_(A subsetJ,includingempty)d_A.       (PG1)
Each nonempty eligible branch has a unique positive dual minimizer.
If A is a MAXIMIZING nonempty subset and w its minimizer,a global primal
maximizer is Phi_A=sum_(i inA)w_i k_i. If empty is maximizing,Phi=0 is a
maximizer. No uniqueness of the global primal or maximizing subset is claimed.

It follows that S depends only on C,ell,b,not the Hilbert realization.
For any two real symmetric PSD matrices C,D with nonnegative entries,
C_ij<=D_ij,same ell,b,we prove
                              S(C)<=S(D).                  (PG2)
The difference D-C need NOT be PSD. Gram realizability is proved in Section6.
No statement concerns arbitrary-phase Gaussian or wave covariance ordering.

## 2. Scalar square-root inequality and exact Hilbert algebra

For w>0,t>=0 and real ell,
                   2ell sqrt(t)<=ell^2/w+w t.              (1)
Indeed sqrt(w)>0,sqrt(wt)=sqrt(w)sqrt(t),and
 0<=(ell/sqrt(w)-sqrt(wt))^2=ell^2/w+w t-2ell sqrt(t).
The square-root identities hold also at t=0. For ell>0,t>0,equality holds
when w=ell/sqrt(t),equivalently t=ell^2/w^2.
For comparison only,the older Mathlib weightedAMGM type atweights1/2 and
bases ell^2/w,w*t gives |ell|sqrt(t) below their arithmetic mean: use
sqrt(ell^2)=|ell| and x^(1/2)=sqrt(x) for nonnegative x. Since
ell sqrt(t)<=|ell|sqrt(t),this also implies(1). This alternative is UNUSED;
the recorded older nu-weights remain provenance only. The actual local
scalar_sqrt_dual proves(1) directly using
(w sqrt(t))^2=w^2 t and positive cancellation. Its complete printed type
allows any real ell,with w>0 and t>=0 (including t=0); PG's ell>0 is stronger.
No certificate is inferred merely from the older AMGM printout.

For every Phi,z in H,expanding ||Phi-z||^2 gives EXACTLY
 <Phi,z>-||Phi||^2/2=||z||^2/2-||Phi-z||^2/2<=||z||^2/2.     (2)
For finite w,k and z=sum_i w_i k_i,bilinearity gives
                       ||z||^2=sum_ij w_i w_j C_ij.         (3)
The local gram_norm_square certifies(3) at any finite index and real inner
product space; completeH is not needed by that algebra. These are valid
in infinite-dimensional H; no compactness of its unit ball
or inverse covariance matrix is used. The factors1/2 are essential.

## 3. Positive-weight dual: coercivity,barrier and attained minimum

Fix nonempty A subsetJ. Each c_i=C_ii is strictly positive. For w_i>0,
entrywise C_ij>=0 and positive w_i give
 D_A(w)>=sum_i[ell_i^2/w_i-b_i w_i+(c_i/2)w_i^2].
Completion of the square gives
 (c_i/4)w_i^2-b_i w_i>=-b_i^2/c_i,
so with K_A=sum_i b_i^2/c_i,
 D_A(w)>=sum_i ell_i^2/w_i+(1/4)sum_i c_i w_i^2-K_A.       (4)
This bound handles JOINT approaches to the orthant boundary and infinity;
no negative term from another coordinate can hide the reciprocal barrier.

Take w0=(1,...,1),d0=D_A(w0),L_A=d0+K_A. Applying(4) to w0 shows L_A>0.
Every w with D_A(w)<=d0 satisfies,coordinate by coordinate,
                ell_i^2/L_A<=w_i<=sqrt(4L_A/c_i).          (5)
The box is compact and entirely inside the open positive orthant. The
sublevel set is nonempty (it contains w0) and closed in that box because
D_A is continuous there. A minimizing sequence taken INSIDE this sublevel set has a
convergent subsequence in the box; its limit stays positive and continuity
attains the infimum. Points outside the sublevel have value>d0,so this
is a GLOBAL minimum on all positive w. In particular d_A is finite.

D_A is smooth on the open positive orthant. At its minimum w*,each
coordinate has a two-sided local minimum under small positive/negative
perturbations,hence its derivative is0. Its Hessian has quadratic form
 sum_i (2ell_i^2/w_i^3)xi_i^2+sum_ij xi_i C_ij xi_j>0
for xi!=0: the first term is strictly positive and the Gram term is a
squared Hilbert norm by(3). On each nonconstant line segment within the
orthant,the second derivative is strictly positive; thus D_A is strictly
convex and its minimizer is unique. No positive definiteness of C needed.

Differentiating the symmetric quadratic gives
 derivative_i[(1/2)sum_jh w_j C_jh w_h]=sum_j C_ij w_j.
Stationarity is therefore the EXACT identity
                sum_j C_ij w*_j-b_i=ell_i^2/(w*_i)^2>0.    (6)
Let Phi_A=sum_i w*_i k_i. Equation(6) says every i in A is strictly
active at Phi_A,with sqrt(<Phi_A,k_i>-b_i)=ell_i/w*_i.
This constructs a positive conic combination; it asserts no coordinatewise
order on H and does not yet assert that an ARBITRARY A is globally optimal.

## 4. Full positive-part score: active upper bound and matching lower

For arbitrary Phi,let A(Phi)={i:<Phi,k_i> > b_i}. This is a subset of J:
if k_i=0,then 0>b_i is impossible because b_i>=0. Terms outside A(Phi)
are0,including equality at the threshold. If A(Phi)=empty,
F(Phi)=-||Phi||^2/2<=0=d_empty.

Otherwise take ANY w_i>0 on A=A(Phi) and set t_i=<Phi,k_i>-b_i>0.
Apply(1),sum,and then(2)-(3) with z=sum_i w_i k_i:
 F(Phi)<=sum_i ell_i^2/w_i-sum_i b_i w_i
                      +<Phi,z>-||Phi||^2/2
         <=sum_i ell_i^2/w_i-sum_i b_i w_i+||z||^2/2=D_A(w).
The local active_upper_bound and private Audit.active_consumer certify
this EXACT pointwise conditional inequality,including the HALF Gram
quadratic. Instantiate the finite index by A,labels/weights restricted to A,
hw frompositivew,ht fromstrictactiveness. The positive-part/active-set
selection and the following infimum/supremum steps remain analytic.
Since this holds for EVERY positive w,F(Phi)<=d_A. Taking suprema gives
                        S<=max_(A subsetJ)d_A.            (7)
There are finitely many A; Section3 made all branch values finite.

Conversely,F(0)=0 supplies S>=d_empty. For nonempty A,choose its attained
minimizer w*,and Phi_A from Section3. On A,inequality(1) is equality by(6),
and(2) is equality because Phi_A=z. Therefore
 2sum_(i inA)ell_i sqrt(<Phi_A,k_i>-b_i)-||Phi_A||^2/2=d_A.
Every omitted label contributes a NONNEGATIVE term to F(Phi_A),so
                           F(Phi_A)>=d_A.                (8)
This remains valid if d_A is negative. It does NOT claim all outside labels
are inactive for an arbitrary branch. Taking the largest of finitely many
values and using(7) proves PG1.

Choose a maximizing subset. If it is empty,Phi=0 achieves S=0. If it is
nonempty,(7)-(8) force F(Phi_A)=S=d_A,so the constructed positive conic
combination is a global maximizer. There can then be no strictly positive
outside contribution,but this is a CONSEQUENCE,not a premise. Ties between
branches or with0 are allowed; no global primal uniqueness is inferred.
All-zero labels give F(Phi)=-||Phi||^2/2 and S=0 directly. This proves the
attainment and degenerate cases in PG1,for arbitrary real Hilbert H.

The proof did not use global concavity of F,which is false. For example
k=ell=b=1 gives F(phi)=2sqrt((phi-1)_+)-phi^2/2: it decreases to-1/2 on
[0,1] and has an infinite positive right slope at1. The active-branch dual
argument,not a nonexistent global-concavity argument,handles this kink.

## 5. Analytic global-radius justification and exact small controls

For completeness justify the search-radius convention independently of the
numerical optimizer. Put a_sum=sum_i ell_i sqrt(||k_i||). If q=||Phi||,
Cauchy-Schwarz and b_i>=0 give
 (<Phi,k_i>-b_i)_+<=q||k_i||,
                     F(Phi)<=2a_sum sqrt(q)-q^2/2.         (9)
For q>0,F(Phi)>=0 forces q^(3/2)<=4a_sum. Since S>=0,all global maximizers
are inside radius (4a_sum)^(2/3),and the numerical radius plus1 is strictly
larger. If a_sum=0 all labels are0,already treated. No numerical
radius-variation experiment or certified global search is claimed.

The empty subset is indispensable. For one label with C=1,ell=1/10,b=4,
D(4)=1/400-16+8=-3199/400<0. Thus the infimum of the only nonempty branch
is negative,whereas F(0)=0; omitting the empty value gives a false formula.
This is an exact arithmetic counterexample,not a solver conclusion.

For k=ell=1,b=0,the scalar objective for phi>=0 is2sqrt(phi)-phi^2/2,
whose derivative1/sqrt(phi)-phi changes frompositive to negative atphi1.
For phi<=0 the value is nonpositive,and at infinity it tends to-infinity;
so the maximum is3/2. If the raw cost is wrongly doubled to phi^2,the
critical point is2^(-2/3) and the maximum is3*2^(-4/3). This proves the
hardcoded scalar comparison analytically; it is not an extra numerical run.

## 6. Every PSD matrix has a real Gram realization

For clarity supply a finite construction,requiring only PSD,not entrywise
positivity. Induct on the matrix size. Empty matrices are realized in{0}.
For symmetric PSD C,each diagonal is>=0. If all are0,testing the quadratic
form on e_i+t e_j gives2t C_ij>=0 for every real t,so every C_ij=0; take
all labels0. Otherwise permute a strictly positive diagonal c to position1
and write C=[c,v^tr;v,A]. The Schur complement B=A-vv^tr/c is PSD: for
any y,use x1=-v^tr y/c to get (x1,y)^tr C(x1,y)=y^tr B y>=0.
By induction B is the Gram matrix of vectors u_i in a finite Euclidean
space. Set k1=(sqrt(c),0),k_i=(v_i/sqrt(c),u_i) for i>1. Their pairings
are exactly C. Undo the permutation. This proves realization for arbitrary
real PSD C; B may have negative entries,and no nonnegative-coordinate
realization or completely-positive matrix assumption was introduced.

For a Gram with C_ii=0,the realized label has norm0 and hence is0. Thus its
entire row/column vanishes. These facts also follow directly for any other
Hilbert realization. PG1's expression uses only C,ell,b,so EVERY realization
has exactly the same score. Denote it S(C). No chosen square root/inverse
or dimension of the realization appears in that value.

## 7. Entrywise comparison,including changing zero-label eligibility

Let C,D be real symmetric PSD matrices,entrywise>=0,C_ij<=D_ij,sameell,b.
Let J_C={i:C_ii>0},J_D={i:D_ii>0}. Then J_C subsetJ_D,so every eligible
active set for C is eligible for D,including the empty set. For every
nonempty A subsetJ_C and EVERY w_i>0,
 D_A^D(w)-D_A^C(w)=(1/2)sum_ij w_i(D_ij-C_ij)w_j>=0.      (10)
The local half_weighted_entrywise_mono certifies this pointwise order
with w_i>=0; the positive dualweights satisfy that guard. No PSD-difference
hypothesis enters. Eligibility/infimum/max steps remain analytic.
Thus d_A^C<=d_A^D,by taking infima of these pointwise ordered functions.
PG1 and the larger eligible family for D give
 S(C)=max_(A subsetJ_C)d_A^C<=max_(A subsetJ_D)d_A^D=S(D).
This proves PG2 even when zero labels become nonzero. For example C=[0],
D=[1],ell=1,b=0 gives0 versus3/2; this is an analytic example,not an added
numeric comparison pair. If J_C is empty,its maximum is0 and S(D)>=0.

No Loewner order is needed in(10); positivity of w_i w_j is what matters.
For C=I2,D=[1,1/2;1/2,1],D-C has eigenvectors(1,1),(1,-1) with eigenvalues
1/2,-1/2. Both C,D are PSD/nonnegative. With ell_1=ell_2=1 and b_1=b_2=0,their scores are3
and3*(3/2)^(1/3),respectively. In the second case swapping the two coordinates preserves the dual;
uniqueness therefore forces its minimizer to be symmetric. Hence
w1=w2=w,w^3=2/3,and D_full(w)=2/w+(3/2)w^2=3/w; individual
branches have value3/2,so the full branch wins. This concerns optimized
finite scores only,not arbitrary covariance or physical wave comparisons.

## 8. Evidence,fidelity and remaining original objective

All9statement findings are addressed: C>=0 notstrict; maximizingA/minimizer
only; empty-value control; analytic radiuscontainment instead of unperformed
radiusvariation; analytic wronghalfaction; recordedreportedprecisionties;
zero-eligibility inclusion; realization/independence; no uniqueprimalclaim.
Rawtarget/script/output/report remain unchanged. The12case/10objective
Newton+DE/Powell screen is numerical consistency/heuristic evidence only,
not proof,enclosure or statistical confidence. No rerun. Candidate-gap
reportedprecisionties include parallel andthree_mixed,not a uniqueargmax.

The local finite algebra seam passed source/fulltype/liveaxiom/freshowned-
replay/4arithmeticFalse controls,with6actualtargetcalls and a private exact
PGbranchconsumer. Fiveartifactpairs are byteidentical; fourpublicheaders
neverchanged. Two early proof/API failures and an auditwarning run are
preserved,with no linterdisabled. Current74acceptedfacts20seams remain;
4newpublicfacts/newlocal seam passed this FULL applicationfidelity gate.
Privateintegrationcheck is not a fifthpublicfact. No newpackage,
officialcompanion,registry/lease/HPC gate. Analytic dualcoercivity/interiormin/
calculus/attainment/realization and wholePG1-PG2 remain unformalized.
The full analytic proof/application gate accepted exactly the stated scope.

This is not an actual H_I/timeoccupation/mask-removal/positiveLOWERclass
application. Those need new exactsource and proof gates,as the separate
physical-application-next-v0.md design states. No authorenergy/domain/
normalization/constants,p1identity,Skorohod/sourcefix/contact/HPC/companion/
TeX/PDF/wiki/bib/sibling/publicaction. Originalallmodelsharpgoal ACTIVE.
