# U1-U5: uniform-radius E Cameron mean and infinite-spatial-rank regulator

FROZEN UNREVIEWED v2 statement refinement after diagnostic calibration,
before proof. V1 preserved; exact block-weight factor now explicit.
Full original allGamma/d1/2/3 upper/sharp goal remains target, no narrower
completion claim. This is growing-cone route steps3-5, not an actual
stochastic residual exponential theorem. GC/SP gates remain pending.

## Original class, exact spaces and fixed parameters

ALL original nonzero homogeneous even nonnegative positive-definite
Radon Gamma, original amplitude,d=1,2,3,0<a<1,alpha+a<2,
0<alpha<d or alpha=d=1. Unit Fourier convention of accepted notes.
H_sp real spatial covariance test-null completion, H_t real time covariance
completion onI=(0,1),H=H_t tensor H_sp as accepted C2. E=H1/2 x H-1/2.
Fix alpha/4<s<1/2 and beta=1/2-s in(0,1/2). Fix real even base
eta in C_c^infinity,0<=eta<=1,eta1 onB1,suppB2. R>=1,eta_R(x)=eta(x/R),
physical noise mask m_R=eta_R^2 ONCE. No constant data columns in E.
All constants may depend on Gamma/amplitude,d,a,s,r,eta, never R>=1.

Use OWN accepted upper-cameron-compactness.md Section2(3)-(4): actual
physical fractional product ||fg||H_sp<=A_s||f||Hs||g||Hs with absolute
physical pairings and all-model covariance normalization. From its
Section3(5), restrict the ACTUAL T_sp,R on F to E; call it T_sp,R,E.
Its row is
 <T_sp,R,E q z,w>_E=<q,(eta_R z1)(eta_R Lambda^-1 w2)>H_sp.
For smooth q this is actual B(m_R Gamma*q) on E, then completion. No raw
noise-quotient multiplication by m_R. R-dependent compactness is accepted
pointwise in R; new uniform bounds below require explicit proof.

## U1 uniform physical state cutoffs and mean multiplier norm

Propose constants M_sigma independentR>=1 such that
 ||eta_R f||Hsigma<=M_sigma||f||Hsigma for sigma=s,1/2,
 ||T_sp,R,E||H_sp->B(E)<=A_s M_(1/2)^2.
Here H1/2 embedsHs with norm1; Lambda^-1:H-1/2->H1/2 is isometric.
Fourier weighted-L1 multiplier proof must track the exact dilation,
R^d etahat(Rxi), rather than use an unspecified fixed-cutoff constant.
Do NOT claim a uniform F constant-column bound or a raw noise-mask map.

## U2 uniform spatial heat and true frequency-projection tails

For h inR^d let tau_h f(x)=f(x-h), acting isometrically on H_sp.
Let C_epsilon be the accepted spatial heat contraction with Fourier
multiplier exp(-epsilon|xi|^2/2). Propose for0<epsilon<=1,
 ||T_sp,R,E(I-C_epsilon)||H_sp->B(E)<=C epsilon^(beta/2).
The planned product estimate is on the ACTUAL row
k=(eta_R z1)(eta_R Lambda^-1 w2), using
 ||tau_h k-k||H_sp<=C min(1,|h|^beta)||z||E||w||E.
Heat as a Bochner average of translations on H_sp and its covariance
Fourier normalization must be checked. No pointwise covariance density.

For K>=1, define P_K on H_sp by the TRUE spectral multiplier
1_(|xi|<=K) under the covariance Fourier isometry. Propose it is a real
orthogonal projection, preserves the completed test image and
 ||T_sp,R,E(I-P_K)||H_sp->B(E)<=C K^(-beta).
Do not assume the test image equals all L2(mu). Instead bounded smooth
even radial approximants to the closed-ball indicator acting on Schwartz
functions should preserve the image and converge by dominated integration;
boundary sphere mass must be included, not assumed zero. Selfadjointness/
idempotence extend from the Fourier image. Frequency is an operation on
the NOISE Hilbert space, not a periodic state replacement or physical mask.
Heat tail at epsilon=K^-2 compares to the projector tail using
1-exp(-|xi|²/(2K²))>=1-exp(-1/2) on |xi|>K.

## U3 scalar time tails tensor an infinite Hilbert identity

Fix2<r<2/a. Accepted C_t:H_t->Lr(I) is compact (C2Section5).
For FIRSTJ smooth-test time ONbasis directions let pi_J be their raw
orthogonal projection,epsilon_J=||C_t(I-pi_J)||H_t->Lr ->0.
Propose for every real Hilbert G and bounded A:H_t->Lr(I),
 ||A tensor I_G||H_t tensor G->Lr(I;G)<=||A||,
with finite-tensor definition followed by completion. This is only r>=2.
A Gaussian-randomization proof must track m_r=E|N(0,1)|^r and show the
Hilbert Gaussian r-moment bound by m_r times trace^(r/2), so constants do
not grow with spatial dimension. Scalar compactness tensor infinite I is
NOT compactness; only the norm of the time tail tends to0.

## U4 exact uniformR retained projection and mean tail

Let U:H->Lr(I;H_sp) be accepted temporal covariance map C_t tensor I.
Define T_R,E Phi(t)=T_sp,R,E(U Phi(t)), the actual E restriction of the
completed physical mean. Set Q_JK=I-pi_J tensor P_K on H, J>=0,K>=1.
Propose pi_J tensor P_K is a TRUE raw orthogonal projection, generally
INFINITE spatial rank, and
 ||T_R,E||H->Lr(B(E))<=C,
 ||T_R,E Q_JK||H->Lr(B(E))<=C(epsilon_J+K^-beta).
No finite Gaussian head density or finite-rank compactness is asserted.
Spatial heat is only a proof/comparison regulator; the retained head is
the TRUE frequency projection, so actual head/residual Gaussian fields
can be orthogonal/independent on the given isonormal space. Heat-filter
head and I-heat residual would NOT be independent and are not used.

## U5 exact actual raw block Cameron norm application

Keep C3 accepted theta,p,r ranges:
 1/2<theta<min(1-a/2,(3-a-alpha)/2),
 1/(1-theta)<r<2/a, 1/theta<=p<2<r.
Integer B>=1,0<delta<min(1,1/B),true block ell_m/slowintervalI_m as C3.
Extend retained projection pi_J tensor P_K from closed H_I to full H_W
by its isometric inclusion/adjoint, not time-indicator multiplication.
Q_full=I-P_ret, actual fast residual noise Y_m(f)=W(Q_full T_(delta,m)f).
Take ACTUAL E Gaussian transfer A_R(Y_m) from accepted Theorem1, stop its
interaction path atell_m and extend constantly to[0,B]. X_m=g_delta A_R(Y_m),
g_delta=delta^((1-a)/2). Tuple norm
 Y_delta=(delta sum_m||X_m||Ctheta^p)^(1/p).
Propose its ACTUAL Cameron covariance map from rawH_W into this Banach
tuple has norm <=sqrt(delta) C_B (2/B)^(1/p-1/r) C(epsilon_J+K^-beta),
UNIFORMR>=1, where C_B=G_B^2[B^(1-1/r)+B^(1-1/r-theta)],
G_B=sup_(|v|<=B)||S_E(v)||. Propose G_B<=3B and
C_B<=18B^(3-1/r) directly in E, B>=1. No imported F constant-column
normalization or hidden delta-weight/rank factor.
All actual rows supported in H_I, completed means/covariance formulas,
last empty block, discrete Holder factors and noise-only amplitude must
be matched, not merely abstract mean norm substituted. Infinite spatial
rank is allowed for this LINEAR Gaussian Cameron statement.

This does NOT bound E Y_delta uniformlyR, supply a Gaussian residual
exponential rate or a finite retained-head Laplace argument. Quantitative
stochastic anchors, infinite-head/localization/entropy, original point
transfer, signed-positive score, source-normalization/sharpconstants and
conditional exactlimit remain OPEN. No instantaneous raw Gaussian H/L2
field, arbitrary-phase covariance monotonicity, Skorohod/contact/HPC/
companion/sourcefix/TeX/PDF/wiki/bib/publication action.74facts20seams/L0
unchanged. Independent source/statement and FULL proof/actual-application
gates before adopting or building a substantial successor on this claim.

## Pre-proof falsification plan

Evaluate the ACTUAL d1 WHITE spatial covariance row k=m_R f_b^2 for real
Gaussian states f_b normalized in whole-space H1/2, using the physical
compact eta_R^2 mask. Vary R>=1,translations b and noise heat/frequency
cutoffs. Compare two quadrature/Fourier resolutions and an unmasked exact
Gaussian Parseval/tail calibration; explicitly record discretization and
threshold errors, no certified enclosure. This tests a family of row
values, not the operator supremum or allGamma theorem. Test U3 on finite
scalar time operators with multiple Hilbert coordinate directions and a
wrong dimension-dependent/compactness inference; existing trace/noncompact
boundary remains. No claim numerical absence of a counterexample proves U.
