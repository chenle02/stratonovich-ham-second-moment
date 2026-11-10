# US1-US4: exact uniform-E spectral and product target, BEFORE tests

UNREVIEWED STATEMENTS. No proof/adoption is claimed. Original all-model
sharp/source goal unchanged; current component BT is accepted separately.

## Model and spaces

All original H:homog Gamma/amplitudes,d=1,2,3,0<a<1,0<alpha<d or
alpha=d=1,alpha+a<2; include the zero covariance trivially. Unitary Fourier,
Lambda=(1-Delta)^(1/2),E=Hhalf x Hminus-half, F=E plus R2. Physical mask
m_R=eta_root(x/R)^2 ONCE,R>=1. Both displacement and physical/fast velocity
retained. H_I=H_t tensor H_sp is the accepted supported slow raw Hilbert
space,not multiplication by a raw time indicator.

For real compact smooth q let V_q=m_R(Gamma*q),M_q:Hhalf->Hminus-half
its actual multiplier, B_E(V_q)(u,v)=(0,M_q u). Define Vclass_E,R to be
the OPERATOR-NORM closure of these E interactions. Norm k=||B_E(V)||
equals ||M_V||Hhalf->Hminus-half. No F constant-column norm enters any
uniform estimate. At fixed R a lift to F may identify the actual rough
potential/flow,with a possibly R-dependent reconstruction constant.

Use the actual E completed mean mathcalT_R=J_R(C_t tensor Id_Hsp)
on H_I,from accepted U,with ||J_R||<=M_0 and C_mean=M_0||C_t||. Fix
 1/2<theta<min(1-a/2,(3-a-alpha)/2),nu=1/theta,
 1/(1-theta)<r<2/a, nu<=p<2<r.
Thus 1<nu<2<r. Additional SA exponents/fixed even Q are needed only when
choosing its actual b_delta,not for deterministic US statements.

## US1: E-norm signed static form, spectral rate and actual flow

Each element of Vclass_E,R determines one real V in Hminus-half supported
in supp m_R,with actual symmetric multiplier action. On complexified L2
let q_V(u)=||grad u||2^2-<Vu,u>,form domain H1,and H_V the corresponding
self-adjoint operator. For ANY K>=max(1,k),c=2+K^2,A=H_V+c,
 A>=1,D(A^.5)=H1,D(A^.25)=Hhalf,negative dual completion Hminus-half,
 .5||u||H1^2<=q_V(u)+c||u||2^2<=3(1+K^2)||u||H1^2.
No rough H2 domain is asserted. The actual E physical Young flow P_V(t)
equals the spectral wave of this H_V. With
 beta(V)=inf_(u in H1,||u||2=1)q_V(u)=inf spectrum H_V,
 -K^2<=beta(V)<=0, lambda(V)=sqrt(-beta(V))<=K,
 ||P_V(t)||B(E)<=8(1+K)^2(1+t)exp(lambda(V)t),t>=0.       (US1a)
The larger 16(1+K)^4(1+t)^3 bound may be used later. Constants independent
R/Gamma/d,apart from the explicit E norm K. No gap,ground state,positivity
or positive rate needed. For V,W with E norms<=K,K>=1,
 |beta(V)-beta(W)|<=(K+2)||B_E(V)-B_E(W)||,
 |lambda(V)-lambda(W)|<=sqrt((K+2)||B_E(V)-B_E(W)||).       (US1b)
Potential reconstruction and actual-flow identification need fixed-R
application proofs; none of their nonuniform constants may enter US1a/b.

## US2: uniform time averaging without spatial compactness

For integer B>=1,0<delta<min(1,1/B),N=floor(1/(delta B)),n=N+1,
s_m=m delta B,ell_m=B for m<N,ell_N=delta^-1-NB in[0,B).
True slow cells I_m=[s_m,s_m+delta ell_m],last possibly empty. Let A_delta
be Bochner averaging over each NONEMPTY true cell,not point sampling or
averaging the short last cell over a full cell. It acts on scalar Lr too.
Set omega_delta=||(A_delta-I)C_t||H_t->Lr. Then omega_delta->0 at fixed B.
For W_R,Phi=mathcalT_R Phi and barW=A_delta W_R,Phi,
 sup_(R>=1,||Phi||<=M)||barW-W||Lr<=M_0 M omega_delta->0,
 sup_(R>=1,||Phi||<=M)int|lambda(barW)-lambda(W)|
 <=sqrt(3+2C_mean M)*sqrt(M_0 M omega_delta)->0.           (US2)
All means/averages lie in Vclass_E,R. Rate_R(Phi)=int_I lambda(W_R,Phi)
is finite,nonnegative,continuous. No uniform compactness of the spatial
tensor or any finite Gaussian head is asserted.

## US3: uniform E deterministic block products on growing balls

H_m(Phi)(u)=int_0^min(u,ell_m)
 S_E(-v)W_R,Phi(s_m+delta v)S_E(v)dv,stopped/constextended to[0,B].
Pmean_m=S_E(ell_m)U_Hm(ell_m), actual LEFT Young evolution.
C_B=G_B^2[B^(1-1/r)+B^(1-1/r-theta)],G_B=sup_|v|<=B||S_E(v)||.
Use G_B<=3B,C_B<=18B^(3-1/r)<=32B^(3-1/r),C_B B^(1/r)>=B.
The generic polynomial Young estimate has Ctheta independent B,R,delta:
 log||S_E(ell)U_D(ell)||<=Ctheta B(1+||D||theta^nu),ell<=B.
For all actual means ||Pmean_m||>=1 by SP,including partial/empty cells.
For ANY fixed B,M>0,K>=1,Z=C_mean M,L_BK=log16+4log(1+K)+3log(1+B),
 limsup_(delta->0) sup_(R>=1,||Phi||<=M)
 [delta sum_m log||Pmean_m||-Rate_R(Phi)]
 <=L_BK/B+Ctheta32^r Z^r B^(3r)(K^-r+K^(nu-r)).           (US3a)
For M_B=M0 B^m,ANY M0>0,m>=0,choose s>r(3+m)/(r-nu),K_B=B^s:
 limsup_(integer B->infinity) limsup_(delta->0)
 sup_(R>=1,||Phi||<=M_B)
 [delta sum_m log||Pmean_m||-Rate_R(Phi)]<=0.              (US3b)
The product here is a SCALAR product of block norms. No equality with
norm of ordered operator product. No diagonal B_delta or uniform small
error before the fixed-B inner limit is asserted.

## US4: EVERY arbitrary small residual, E mean denominator only

For arbitrary zero-start little-Holder compact-operator tuples x_m on
[0,B],put Y=(delta sum||x_m||theta^p)^(1/p),
Ppert_m=S_E(ell_m)U_(H_m+x_m)(ell_m),
z=product_m ||Ppert_m||/||Pmean_m||. Generic Young evolution is invertible,
so these norms are positive. For every Kres>=1 there are finite C_Kres
and c_B depending only theta,B,Kres (c_B independent Kres),uniform R,delta,
Phi,M,x,with D_M=C_B^r(C_mean M)^r and
 delta log max(1,z)
 <=C_Kres[(2/B)^(1-1/p)Y+(2/B)^(1-nu/p)Y^nu]
   +c_B D_M(Kres^-r+Kres^(nu-r)).                        (US4a)
The residual x is NOT required Hamiltonian/Gaussian,or a Cameron mean.
For ANY deterministic b_delta>=0 with b_delta->0 at each fixed B,define
 F_(delta,R)(x+H(Phi))=2delta log max(1,||Ppert_N...Ppert_0||).
Then uniformly R>=1 and ||Phi||<=M,the excess over
2delta sum log||Pmean_m|| tends to <=0 on Y<=b_delta,as delta->0,
by taking delta first,then Kres->infinity. Consequently US3b yields
 limsup_B limsup_delta sup_(R>=1,||Phi||<=M_B,Y<=b_delta)
 [F_(delta,R)(x+H(Phi))-2Rate_R(Phi)]<=0.                (US4b)
At EACH B,M_B fixed before delta. Constants C_Kres may grow arbitrarily
with B/Kres. Mean baseline>=1 permits max1/product step; no residual
symplectic identity or independence is assumed. Actual SA b_delta on
R_delta is one possible later choice,not a uniform-R stochastic bound.

## Required tests and evidence boundaries

Freeze these statements BEFORE running diagnostics. Static 2x2 balanced
wave matrices: compare independent expm/closed spectral formula at40/80
digits,zero/near-zero frequencies,stable/unstable/critical potentials and
large time. Evaluate sufficient norm bounds. Wrong omission of polynomial
prefactor and wrong rate must fail on suitable cases. Noncommuting stable
switch (quarter-period oscillators) gives exact diagonal product with norm2;
its individual rates0 do not license a global exp(integrated rate) bound.
Test scalar displacement-only multiplication and ordered/scalar norm
product equality as negative controls,not assumptions. Truepartial/empty
cell and weighted Young/Holder budgets must handle zeros and positive powers.

Finite matrices are mechanism checks/comparators,NOT actual masked spatial
PDE simulations or proof/enclosures. Higher-precision consistency and CAS
are not Lean. Count raw rows separately from distinct informative cases;
positive tautological bounds are evaluator calibration,not falsification.
Accepted U3 orthonormal spatial sequence already refutes tensor compactness;
no finite spatial grid is a substitute for that infinite-dimensional guard.

Primary sources already held: Teschl2014 SECOND edition form/spectral pages
used in accepted signed-static S1-S4; Friz-Hairer2020 Young pages used in
accepted generic E1. Old proofs/types/axioms supplied for EXACT NEW E-norm/
uniformR/trueclock applications,not recertification or waiver. No new Lean
count/package/compiler,sourcefix,p1identity,Skorohod,contact,HPC,TeX/PDF/wiki/
bib/publication. BT/Rayleigh sharp-score integration,signed-positive score,
source dictionary/conditional exact limit remain separate and OPEN.
