# Moving blocks, positive amplitude and the terminal spatial average

CANDIDATE, not independently accepted. The unchanged mathematical target is
reviews/2026-10-30-moving-block-cone/target-v1.md. Its independent preproof
audit found no mathematical defect but required reproducible proxy controls;
that repair is implemented, with independent recheck still required in the
full scientific gate. No stochastic event or sharp moment theorem is claimed.

## 1. Actual inputs, observable and theorem

Use the fixed actual real d1 family and F of the three accepted notes
spectral-ground-family.md, spectral-weighted-projection.md and
spectral-complement-transfer.md. In particular U=Gamma*q, with actual nonzero
positive Riesz/white covariance amplitude, nonzero q>=0 compact smooth,
b in ONE fixed K=[b0,b1] subset(0,infinity), H_b=-d2-bU and physical wave P_b.
F is the closure of compact smooth phases PLUS both constants in uniformly
local E=H1/2 x H-1/2, as in local-causal-young-flow.md Sections4-5.

From these scoped accepted inputs, not proved again here:

 e_b=(p_b,lambda_b p_b), ell_b(v,w)=(<p_b,v>+<p_b,w>/lambda_b)/2,
 Pi_b=e_b ell_b, ell_b(e_b)=1, Q_b=I-Pi_b;
 P_b(t)Pi_b=Pi_b P_b(t)=exp(lambda_b t)Pi_b, t>=0;
 lambda_b>=l>0;
 ||exp(-lambda_b t)P_b(t)Q_b||B(F)<=C_R exp(-eta t), t>=0.   (1)

Here C_R>=1 and eta>0 are uniform in b. e_b,ell_b,Pi_b are bounded
uniformly and continuous in their respective F,F*,B(F) norms. Compact K
makes that continuity uniform. Also e0=(1,0) belongs to F and

 a_*=inf_b ell_b(e0)>0.                                    (2)

Fix nonnegative real phi in C_c^infinity with integral1. Define J(z) as
the distributional displacement pairing with phi. Choose compact smooth
kappa=1 near supp phi. The accepted finite localization bound (4.2) of
the local-flow note gives ||kappa z||E<=C_phi||z||F. Pairing its first
entry in H1/2 with phi in H-1/2 proves |J(z)|<=C_phi'||z||F. This defines
a bounded real functional, without point evaluation. For the eigenphase,

 J(e_b)=integral phi(x)p_b(x)dx>0.

Indeed p_b is continuous and strictly positive everywhere by the accepted
ground result, and a continuous nonnegative phi of integral1 is positive
on a nonempty open set. b->e_b is continuous in F, so b->J(e_b) is
continuous on compact K. Consequently

 j_*=inf_b J(e_b)>0.                                      (3)

For theta>0 define the two-entry cone

 C_b(theta)={z=a e_b+r: a=ell_b(z)>0, ell_b(r)=0,
                         ||r||F<=theta a}.                (4)

Theorem (candidate). For every 0<rho<1/2 there are theta>0, an INTEGER
T>=1, omega>0, epsilon>0 and c_*>0, depending only on this fixed family,
phi and rho, with the following property for all N>=1. Take b_0,...,b_N
in K with consecutive differences <=omega and real bounded operators
D_m(t):F->F,0<=m<=N,0<=t<=T, such that

 sup_(m,t)||D_m(t)-P_(b_m)(t)||B(F)<=epsilon.                (5)

Set z_0=e0 and z_(m+1)=D_m(T)z_m for0<=m<N. Then z_1 belongs to
C_(b_0)(theta) and ell_(b_0)(z_1)>=(a_*/2)exp(lambda_(b_0)T).
For1<=m<N the next z_(m+1) belongs to C_(b_m)(theta), and

 ell_(b_m)(z_(m+1))
   >=exp(lambda_(b_m)T)(1-rho)ell_(b_(m-1))(z_m).           (6)

For every s in[0,T],

 J(D_N(s)z_N)>=c_* (1-rho)^(N-1)
   exp(T*(sum_(m=0,...,N-1)lambda_(b_m))+s*lambda_(b_N)).    (7)

There is no positivity, independence, semigroup or continuity assumption
on D; the finite products and stated norm bound suffice. In the eventual
application these are actual block families, whose (5) is still a separate
obligation. This theorem does not assume the desired product conclusion.

## 2. Explicit compatible parameter budgets

Fix finite constants

 M_e=max(1,sup_b||e_b||F), M_l=max(1,sup_b||ell_b||F*),
 M_P=max(1,sup_b||Pi_b||), B_Q=1+M_P, B=M_e+1,
 E0=||e0||F>0, H=max(1,||J||F*).

E0>0 because e0 is a nonzero distribution and the local norm is a norm.
Choose FIRST

 theta=min(1,j_*/(16 H C_R))>0.                            (8)

In particular H C_R theta<=j_*/16. Choose an integer T>=1 so large that

 q_T=C_R exp(-eta T)<=min(1/8,theta a_*/(8 B_Q E0)).         (9)

This exists since eta>0; increasing T preserves (9). Next choose nu>0
with

 nu B<=min(rho/2,theta,1/4).                               (10)

Uniform continuity of ell and Pi on K supplies omega>0 such that for
b,c in K with |b-c|<=omega both

 ||ell_b-ell_c||<=nu, ||Pi_b-Pi_c||<=nu.                    (11)

If the usual modulus gives a strict distance bound, halve the selected
radius so (11) also holds at <=omega. Finally choose epsilon>0 satisfying

 M_l epsilon B<=rho/2,
 B_Q epsilon B<=theta/4,
 M_l epsilon E0<=a_*/2,
 B_Q epsilon E0<=theta a_*/8,
 H epsilon B<=j_*/8.                                      (12)

Every right side is positive and every coefficient finite and positive,
so the minimum of the five corresponding positive ratios, or any smaller
positive number, works. This establishes simultaneous feasibility, not
an assumption of it. These choices depend on neither N nor s nor the
parameter sequence. Crucially (8) contains no T. For any r in ker ell_b,
(1) gives uniformly for ALL s>=0

 |J(exp(-lambda_b s)P_b(s)r)|<=H C_R||r||F.                 (13)

Thus no exp(C T) terminal constant is used to choose the aperture.

## 3. Entrance from constant initial data

Fix b=b_0 and write E=(D_0(T)-P_b(T))e0, so ||E||<=epsilon E0. By
invariance of ell_b, or the accepted commutation identity,

 A1=exp(-lambda_b T)ell_b(D_0(T)e0)
   =ell_b(e0)+exp(-lambda_b T)ell_b(E)
   >=a_*-M_l epsilon E0>=a_*/2>0.                         (14)

We used lambda_b T>=0, hence exp(-lambda_b T)<=1. Similarly commutation
of Q_b with P_b gives

 exp(-lambda_b T)||Q_b D_0(T)e0||
  <=q_T||Q_b e0||+B_Q epsilon E0
  <=q_T B_Q E0+B_Q epsilon E0<=theta a_*/4.                (15)

Here (9) and (12) bound the two terms by theta a_*/8 each. Dividing
(15) by A1>=a_*/2 gives residual-to-amplitude ratio <=theta/2, hence
<=theta. Since Q_b is a projection onto ker ell_b, the decomposition
in (4) is valid. This proves the entrance and its stated amplitude bound.
Constants have never been put in global L2 or global E.

## 4. Rebase and preserve the cone on EVERY full block

Let z=a e_b+r in C_b(theta), with |b-c|<=omega, and let D be one full
block with ||D-P_c(T)||<=epsilon. Then ||z||<=B a. Rebase to c BEFORE
applying the complementary estimate. Equation (11) gives

 |ell_c(z)-a|<=nu B a,
 ||Q_c z||=||Q_b z+(Pi_b-Pi_c)z||<=(theta+nu B)a.            (16)

Put E=(D-P_c(T))z, ||E||<=epsilon B a. The new normalized amplitude is

 A'=exp(-lambda_c T)ell_c(Dz)
   =ell_c(z)+exp(-lambda_c T)ell_c(E)
   >=(1-nu B-M_l epsilon B)a>=(1-rho)a>a/2.                (17)

This proves the amplitude factor in (6), including its sign. For the
new residual, use Q_c P_c(T)=P_c(T)Q_c and apply (1) to Q_c z:

 exp(-lambda_c T)||Q_c Dz||
  <=q_T||Q_c z||+B_Q epsilon B a
  <=[q_T(theta+nu B)+B_Q epsilon B]a
  <=[ (1/8)*(2theta)+theta/4 ]a=theta a/2.                 (18)

Equations (17)-(18) imply ||Q_c Dz||<=theta ell_c(Dz), and the new
amplitude is positive. This proves Dz in C_c(theta). No assumption that
r lies in the NEW kernel ell_c has been made: the second estimate in
(16) is exactly the needed correction. Apply this argument successively
for b=b_(m-1),c=b_m,D=D_m(T), to obtain every assertion (6).

## 5. Terminal partial block and the actual displacement functional

Let z=a e_b+r in C_b(theta), c=b_N with |b-c|<=omega, and any s in[0,T].
The rebased decomposition is z=ell_c(z)e_c+Q_c z. By (10) and (16),

 ell_c(z)>=(3/4)a, ||Q_c z||<=2theta a.                    (19)

Using the eigenmode identity, (1), and exp(-eta s)<=1 gives

 exp(-lambda_c s)J(P_c(s)z)
   >=j_* (3/4)a-H C_R (2theta)a
   >=(5j_*/8)a.                                          (20)

The perturbed terminal error is at most H epsilon||z||<=H epsilon B a.
After normalization it is no larger because exp(-lambda_c s)<=1.
Consequently (12) and (20) show

 J(D_N(s)z)>=(j_*/2)exp(lambda_c s)a.                      (21)

This holds uniformly in s, including s=0. It does not require D_N(0)=I;
(5) controls its difference from P_c(0)=I. The terminal b_N is used here
only, and its closeness to b_(N-1) is essential. No norm-growth implication
is substituted for the positive observable calculation.

Finally entrance (14) and induction on the N-1 inequalities (6) give

 ell_(b_(N-1))(z_N)>=(a_*/2)(1-rho)^(N-1)
                           exp(T*sum_(m=0,...,N-1)lambda_(b_m)).

For N=1 the induction is empty and the same assertion is (14). Apply
(21) with z=z_N,b=b_(N-1),c=b_N. Equation (7) follows with
c_*=a_*j_*/4>0. This proves the candidate moving-block/terminal theorem.

## 6. Boundaries, controls and next consumer

The independent preproof report checked C1-C4 against the actual accepted
inputs but found C5nonreplayable. The old proxy-only booleans alone receive
no credit. Diagnostics-v2 and replay-diagnostics.py now specify and replay
all100rational cases and both false-general-implication witnesses. These
remain finite proxies, not actual HAM evidence. Full independent scientific
review must check this proof AND that reproducibility repair before adoption.

Three local standalone Lean deductions for the scalar budgets in
(17)-(18),(20)-(21) compile/replay cleanly at Lean/Mathlib4.35.0, with
complete public types/live standard-three axioms, five matching owned
outputs and three semantic False controls. Evidence/type/application
fences are in lean-progress/local-checks/moving-cone-v1/. Independent
type/application review remains required. Spectral/ODE/local Sobolev/actual flow inputs and this analytic
assembly are not formalized by a scalar check. No new spectral library,
companion/package or cluster job is authorized or created here.

After adoption, (5) must be DISCHARGED for actual shifted masked random
flows on all fixed-length blocks. Slow variation, finite composition of
accepted unit-block estimates, Riesz mask perturbation and final-horizon
handling remain necessary. See the unreviewed application-obligations.md
in the moving-block review directory. Only afterwards can an all-block
event, the retained-residual Gaussian identity and its exact cost yield a
moment lower rate. The full variational optimizer, original higher
dimensions, intended source normalization and original sharp constants
remain open. No novelty, whole-paper or circulation clearance is claimed.
