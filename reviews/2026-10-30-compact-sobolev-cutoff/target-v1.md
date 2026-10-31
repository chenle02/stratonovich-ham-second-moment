# Whole-space compact cutoff and finite-operator moment: frozen target

UNREVIEWED statements before long proof. All operators retain the actual
whole-space Sobolev phases; no torus/finite-grid state replaces them.
d in {1,2,3}, Lambda=(1-Delta)^(1/2), unitary Fourier c_d=(2pi)^(-d/2).
Lambda is a Bessel NORM multiplier, not a change of the massless wave PDE.

C1. For every real chi in C_c^infinity(Rd), sigma real and gamma>0, the
initial Schwartz operator
 K_(sigma,gamma)=Lambda^sigma chi Lambda^(-sigma-gamma):L2(Rd)->L2(Rd)
extends uniquely compactly, with s_j(K)<=C j^(-gamma/d),j>=1. Singular
values UNNORMALIZED. In particular K in S_p for p>=1 and p gamma>d.
Constants may depend on d,chi,sigma,gamma and the auxiliary box choices,
not j. Zerochi is trivial. No uniform support-radius/p/gamma bound claimed.

Candidate exact auxiliary factorization: choose Q_L=(-L/2,L/2)^d and
real psi smooth compact insideQ, psi=1 on a neighborhood of suppchi,
chi compactinsideQ. Torus uses L2(Q,dx), orthonormal basis
 e_k=L^(-d/2)exp(i kappa_k.x), kappa_k=2pi k/L,
 H^r(T_L) norm=sum <kappa_k>^(2r)|u_k|^2.
Ppsi u=periodization of psi u, Echi v=chi times the periodic distribution
on Rd. Prove BOTH bounded H^r(Rd)->H^r(T_L) and reverse for EVERY realr
needed (negative included). Normalized Fourier kernels should be
 P_r(k,xi)=L^(-d/2)(<kappa_k>/<xi>)^r psihat(kappa_k-xi),
 E_r(xi,k)=L^(-d/2)(<xi>/<kappa_k>)^r chihat(xi-kappa_k).
No extra c_d remains. Verify constants, distributional meanings and density.
Use Peetre plus mixed counting/Lebesgue Schur, including uniform lattice
sum. Prove Echi I_gamma Ppsi u=chi u EXACTLY on H^(sigma+gamma)(Rd),
where I_gamma is the torus identity inclusion intoH^sigma. Diagonal values
<kappa_k>^-gamma only estimate the AUXILIARY inclusion, never freewave
spectrum or a constant state. Lattice finite-rank approximants give decay.

C2. Physical normalized E_(1/2) coordinates J0(u,v)=(Lambda^1/2u,
Lambda^-1/2v) in L2_x^2. Prior frequency J=(F directsumF)J0, unitarychange
only. Define Pchi=J0 Dchi J0^-1=diag(A_1/2,A_-1/2),
A_sigma=Lambda^sigma chi Lambda^-sigma. Prove boundedness and adjoints
onSchwartz then extension: A_sigma*=A_-sigma for REALchi.
Thus with unitary swap U(v,w)=(w,v), Pchi*=U Pchi U, NOTPchi=Pchi*.
Let D_gamma=diag(Lambda^-gamma,Lambda^-gamma). Both
 Kout=Pchi D_gamma, Kin=Pchi* D_gamma
are compact,S_p for p gamma>d, with Kin=U Kout U and equal Spnorms.
Norm^p is sum of the two scalar block norms^p. The two positive envelopes
 B_out=Pchi D_gamma^2 Pchi*=Kout Kout*,
 B_in =Pchi* D_gamma^2 Pchi=Kin Kin*
have equal trace powers Tr B_out^(p/2)=Tr B_in^(p/2)=||Kout||_Sp^p forp>=2.
This is an adjoint identity, not a projection assumption for Pchi.

C3. Conditional deterministic reduction on H=L2(Rd;C^2): suppose finitely
many bounded Z_l satisfy BOTH Pchi Z_l=Z_l=Z_l Pchi and
 Vout=sum Z_l Z_l*<=C D_gamma^2, Vin=sum Z_l* Z_l<=C D_gamma^2,
C>=0. Then Vout<=C B_out, Vin<=C B_in; forp>=2,p gamma>d,
 Vout,Vin positivecompact inS_(p/2), everyZ_l compact inS_p, and
 Tr Vout^(p/2),Tr Vin^(p/2) <= C^(p/2)||Kout||_Sp^p.
Use positive congruence and eigenvalue/minmax domination, NEVER false
A<=B implies A^m<=B^m. These are explicit operator hypotheses; matching
the actual CM/source families is NOT proved or assumed from mean-square
columns. If desired take chi plateau on an open ball for nonzero witnesses.

C4. For evenp=2m>=2 satisfyingp gamma>d and real independent standardg_l,
X=sum_l g_l Z_l from C3 obeys
 (E||X||_Sp^p)^(1/p)<=sqrt(p-1) sqrt(C)||Kout||_Sp.
Initially the Spnorm may be extended infinity; finiteness proves membership
a.s. This is a FINITE Gaussian operator sum, not an infinite series/path.
Proposed route uses accepted finite MATRIX theorem only on Q_n Z_l Q_n
for finite-rank orthogonal Q_n->I. Its variance compressions <=Q_nVQ_n.
Trace powers controlled through eigenvalues. For each outcome, compactX
satisfies Q_nXQ_n->X inoperatornorm; singular values are norm-Lipschitz,
so scalar Fatou twice (j andOmega) transfers the moment bound. No assumed
Sp-Bochner convergence, Banach martingale theorem or Gaussian operator
realization is to be used to prove its own existence.

Regime witness for C3 (not actualsource identification): choose nonzero
real compact smooth v,f inside chi=1. In J0 coordinates let
vtilde=(Lambda^1/2v,0), wtilde=(Lambda^-1/2f,0), Z=vtilde tensorwtilde*.
Then Pchi vtilde=vtilde, Pchi* wtilde=wtilde, so PchiZ=Z=ZPchi. Schwartz
regularity gives Vout/Vin<=C D_gamma^2 by weighted Cauchy-Schwarz. This is
an actual WHOLE-SPACE nonzero operator, not a periodic/finite proxy. Prove
or refute the stated matching before using it as a satisfiability witness.

Missing-cutoff control: chi=1 is outside C_c. Lambda^-gamma itself onRd
is noncompact (translated Gaussian images keep norm and separate), so
compactness must not be inferred from just a decaying Fourier multiplier.
No necessity assertion at the Schatten endpoint p gamma=d for Kchi.

Original all-dimensional lower/sharpupper/source goal remains ACTIVE.
No actual CM/source family, infinite Gaussian series, timepath, Youngflow,
canonicaldata/newmoment/sourceconstant/exactlimit theorem. No newLeanmodule
or oldfinitefact upgrade, privatecompanion/contact/Skorohod/HPC/TeX/PDF/wiki/
publicrelease/wholepaper clearance. Full independent proof gate after this
statement gate is mandatory before adopting C1-C4.
