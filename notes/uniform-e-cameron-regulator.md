# Uniform spatial-mask E means and infinite-spatial-rank Cameron regulation

ACCEPTED at the scoped FULL analytic/source/type/actual-application gate:
scientificf54e92b,actualOpus5.5/HIGH,21checksPASS,348.303seconds,no required
repairs. All21input bindings and complete native archive verified before
optional clarity edits. Six findings adjudicated in
reviews/2026-10-31-uniform-e-cameron/scientific-adjudication-v1.md.
Frozen proof/report unchanged there. Linear uniformR Cameron bounds only;
expected stochastic norm and original sharp-point/source goal remain OPEN.

## 1. Exact claim, original model and accepted inputs

Use all original nonzero H:homog Gamma, with its actual amplitude, d=1,2,3,
0<a<1, alpha+a<2, and 0<alpha<d or alpha=d=1. Gamma is even, nonnegative,
positive definite and tempered Radon, with spectral convention
Gamma=int exp(i xi.x)mu(dxi). Fourier transform is unitary, c_d=(2pi)^(-d/2).
All Hilbert spaces are real; Fourier images use the real subspace with
Hermitian symmetry. Let
 E=H^(1/2) x H^(-1/2), Lambda=(1-Delta)^(1/2),
 alpha/4<s<1/2, beta=1/2-s in(0,1/2).
Fix real even eta smooth compact, 0<=eta<=1, eta=1 on B1, supported in B2.
For R>=1 put eta_R(x)=eta(x/R), m_R=eta_R^2. Noise is physically masked
ONCE by m_R, after any regulation; there are no constant data columns in E.

Direct OWN accepted inputs, checked for exact use, not recertified here:

- upper-cameron-compactness.md Section2(3)-(4): for real f,g in H^s,
  the actual physical product lies in H_sp and
       ||fg||H_sp<=A_s||f||Hs||g||Hs,                         (1)
  including absolute physical four-linear pairings and the original
  covariance normalization. Section3(5) and completion construct the
  actual fixed-R multiplier T_sp,R on F=E directsum R2; its E restriction
  T_R has literal row
   <T_R q z,w>_E=<q,(eta_R z1)(eta_R Lambda^-1 w2)>H_sp.      (2)
  For smooth q it is B(m_R(Gamma*q)) on E. This is not a physical mask
  multiplier on the raw covariance quotient. Fixed-R values are compact.
- The same note Sections4-6: H_I=H_t tensor H_sp is the actual supported
  raw-H subspace, embedded isometrically and closed in H_W. C_t:H_t->Lr(I)
  is compact for 2<r<2/a, and U=C_t tensor I:H_I->Lr(I;H_sp) is the actual
  completed temporal covariance map. We prove a stronger tensor norm
  assertion below; no scalar compactness tensor identity is assumed compact.
- source-operator-convergence.md Section4(11): the covariance Fourier
  isometry for H_sp, Schwartz inclusion by cutoff approximation, and
  selfadjoint heat contraction C_epsilon with multiplier
  exp(-epsilon|xi|^2/2). Its Theorem1 transfers actual centered Gaussian
  noises of covariance bounded by raw H into the same masked E first-driver
  construction, including separable compact-valued Holder paths and moments
  at each FIXED finite R and horizon.
- upper-cameron-compactness.md Section7(12)-(13): the actual completed
  raw-row covariance identity and supported-row argument, including signed
  controls and true last blocks. We apply its J=0 identity, then an
  arbitrary orthogonal residual projection, and explicitly recheck the
  actual covariance, tuple norm and Cameron identification below.
- raw-block-event-lower.md Section2: the actual slow-to-fast raw test
  isometry T_(delta,m). This is not independence of time blocks.
- Existing complete finite Mathlib power-mean type in
  reviews/2026-10-31-upper-gaussian-projection-screen/mathlib-finite-holder-type-v1.txt.
  Its exact new application is specified in Section7. It is an old scalar
  kernel input, not verification of this note's functional analysis.

Here H_sp is the spatial covariance test-null completion, H_t the time
completion on I=(0,1). Define the actual completed mean
        mathcalT_R Phi(t)=T_R(U Phi(t)).
Use different fonts/names for T_R (spatial multiplier) and T_(delta,m)
(raw time pullback). The notation below always states their domains.

Our new claims are uniform-R spatial multiplier and regulator bounds,
a dimension-independent temporal tensor tail, and the actual residual
block Cameron bound in Section7. All constants may depend on the fixed
model, d,a,s,r,eta, but not R>=1. These are LINEAR mean/Cameron bounds,
not stochastic expected-norm, exponential, nonlinear or sharp-point bounds.

## 2. Uniform physical cutoff constants and multiplier norm

For sigma real, Peetre's inequality in the accepted cutoff proof gives
 <xi>^sigma<zeta>^(-sigma)<=2^(|sigma|/2)<xi-zeta>^|sigma|.
On Schwartz inputs the normalized Fourier kernel of eta_R multiplication
is therefore bounded by convolution with
 2^(|sigma|/2)c_d |etahat_R(q)|<q>^|sigma|.
Since etahat_R(q)=R^d etahat(Rq), its L1 norm is at most
 M_sigma=2^(|sigma|/2)c_d int |etahat(p)|<p>^|sigma| dp<infinity, (3)
independent R>=1: substitute p=Rq and use <p/R><=<p>. The L1*L2
inequality and Schwartz density give
        ||eta_R f||Hsigma<=M_sigma||f||Hsigma.               (4)
No support volume enters (3). The sigma=s constant is recorded for U1;
all later estimates use sigma=1/2 followed by H1/2 embedding into Hs.

Write M=M_(1/2). The map w2->Lambda^-1 w2 is isometric H-1/2->H1/2,
and H1/2 embeds Hs with norm1. Thus the row product k_R(z,w) in (2) obeys
 ||k_R(z,w)||H_sp<=A_s M^2||z||E||w||E.                     (5)
Covariance Hilbert Cauchy-Schwarz in (2) proves
        ||T_R||H_sp->B(E)<=M_0, M_0=A_s M^2.                (6)
For each R, (2) is the E restriction of the accepted completed physical
operator: the same bounded row identity agrees on smooth q, then on the
raw completion. In particular no new spectral or point-potential model
has been substituted. The actual fixed-R compact-valued property is
retained. Equations (4) and (6) prove U1.

## 3. Translation regularity and the uniform noise-heat tail

Translations tau_h f(x)=f(x-h) act isometrically on H_sp. For test functions
this follows either from the physical covariance integral or its Fourier
isometry, whose multiplier is exp(-i xi.h). They preserve real tests;
completion extends the isometries. Strong continuity follows on tests by
dominated integration of |exp(-i xi.h)-1|^2|fhat|^2 against mu and then
by density and the uniform isometry bound. No density of mu is needed.

For f in H1/2, elementary Fourier bounds give
 ||tau_h f-f||Hs<=2 min(1,|h|^beta)||f||H1/2.                (7)
Indeed |exp(-it)-1|<=2|t|^beta for beta in(0,1), while the uniform bound
is 2; |xi|^beta<xi>^s<=<xi>^(1/2). For |h|<=1 use the power bound and
for |h|>1 use the uniform bound. Fourier density extends (7) to all f.

Put f=eta_R z1 and g=eta_R Lambda^-1 w2. Physical translation commutes
with products. The H_sp identity
 tau_h(fg)-fg=(tau_h f-f)tau_h g+f(tau_h g-g)
follows first on smooth states and then by (1) and density. Applying (1),
(4), (7) and the H1/2-to-Hs embedding yields
 ||tau_h k_R(z,w)-k_R(z,w)||H_sp
 <=4A_s M^2 min(1,|h|^beta)||z||E||w||E.                    (8)
The constant is independent of the support radius and translations.

Heat on H_sp is the Bochner average of these translations:
       C_epsilon k=int p_epsilon(h)tau_h k dh.              (9)
The strongly continuous isometric translation orbit is bounded, so this
Bochner integral exists in the separable Hilbert space. Its covariance
Fourier image is exp(-epsilon|xi|^2/2)khat, first on tests by ordinary
Gaussian integration and Fubini, then on the completion by the integral
contraction. Thus (9) is the ACTUAL accepted heat operator, with variance
epsilon and no additional (2pi) factor. The covariance isometry itself
has factor (2pi)^d on both sides, which does not alter (9).

Let G_d be a standard d-dimensional real normal vector and
 m_(d,beta)=E|G_d|^beta<infinity. Integrating (8) with respect to heat,
using min(1,x)<=x and h=sqrt(epsilon)G_d, gives
 ||(I-C_epsilon)k_R(z,w)||H_sp
 <=M_h epsilon^(beta/2)||z||E||w||E,
        M_h=4A_s M^2 m_(d,beta).                            (10)
Selfadjointness of C_epsilon in (2) now proves
 ||T_R(I-C_epsilon)||H_sp->B(E)<=M_h epsilon^(beta/2).        (11)
This proves the heat part of U2. The estimate is deterministic; it does
not assert that a heat-filtered random head is independent of its residual.

## 4. True spatial frequency projections, including singular measures

Let F_sp denote the covariance Fourier isometry, scaled by (2pi)^(d/2)
if desired so it is literally unitary onto its CLOSED image V in L2(mu).
We do not identify V with all of L2(mu). The Fourier formula extends to
Schwartz functions: compact cutoffs converge in Schwartz seminorms, and
tempered mu bounds the corresponding weighted L2(mu) Fourier error, so
the accepted H_sp extension has that same Fourier image. For K>=1 choose smooth real even
radial functions chi_n equal1 on the closed ball B_K, zero outside B_(K+1/n),
with 0<=chi_n<=1. They converge everywhere to 1_(|xi|<=K), including on
its boundary. Such functions are smooth at zero because they are constant
there. For a Schwartz real f, chi_n fhat is the transform of a real
Schwartz function. Schwartz functions belong to H_sp by the accepted
cutoff approximation. Dominated integration against |fhat|^2 mu therefore
shows that 1_(|xi|<=K) F_sp f belongs to V. This does not discard any
possible boundary-sphere mass or singular angular support.

Since tests are dense in H_sp, boundedness of the L2(mu) indicator extends
this assertion to every element of V. Its action is a contraction and
preserves V; multiplication by the real indicator is selfadjoint and
idempotent there. Pulling back defines the REAL orthogonal projection
P_K on the ACTUAL H_sp. It commutes with heat. For Q_K=I-P_K and
epsilon=K^-2, the Fourier multiplier on |xi|>K satisfies
       1-exp(-|xi|^2/(2K^2))>=c_0=1-exp(-1/2)>0.
Consequently, for all k in H_sp,
 ||Q_K k||H_sp<=c_0^-1||(I-C_(K^-2))k||H_sp.                (12)
Use (10) on the actual row and selfadjointness of Q_K in (2) to obtain
 ||T_R Q_K||H_sp->B(E)<=M_f K^-beta, M_f=M_h/c_0.            (13)
This proves the frequency part of U2. The projector acts on the covariance
Hilbert space, not on periodic state functions or by a physical noise mask.
Its range may be infinite dimensional; finite spatial rank is never used.

## 5. Dimension-independent time tensor tails

We prove the precise norm assertion needed for U3. Let H_0,G be real
Hilbert spaces, 2<=r<infinity, and A:H_0->Lr(I) bounded. For a finite tensor
write v=sum_(j=1)^n f_j tensor e_j with e_j orthonormal in G. Its squared
Hilbert norm is sum_j||f_j||H_0^2. Let gamma_j be independent standard real
normal variables and m_r=E|gamma_1|^r. For any finite vectors f_j in H_0,
        E||sum_j gamma_j f_j||H_0^r
            <=m_r (sum_j||f_j||H_0^2)^(r/2).               (14)
To see this, diagonalize their finite-dimensional Gaussian covariance.
With eigenvalues lambda_l>=0 and L=sum lambda_l, the squared norm has law
sum lambda_l zeta_l^2 with independent standard zeta_l. If L=0 it vanishes.
If L>0, convexity of x^(r/2) gives pointwise
 (sum (lambda_l/L)zeta_l^2)^(r/2)
       <=sum (lambda_l/L)|zeta_l|^r.
Expectation and multiplication by L^(r/2) prove (14), since
L=sum_j||f_j||^2. No coordinate-count factor enters.

Choose measurable representatives of the finitely many A f_j. For almost
every t, their Gaussian linear combination has variance sum_j|Af_j(t)|^2.
Tonelli and (14) give
 m_r int (sum_j|Af_j(t)|^2)^(r/2)dt
   =E||A(sum_j gamma_j f_j)||Lr^r
   <=||A||^r E||sum_j gamma_j f_j||H_0^r
   <=||A||^r m_r(sum_j||f_j||H_0^2)^(r/2).
Divide by the positive finite scalar m_r and take the rth root. Finite
tensors therefore satisfy
 ||(A tensor I_G)v||Lr(I;G)<=||A||||v||H_0 tensor G.          (15)
Finite tensor density and completeness define the strongly measurable
Bochner extension with the same bound, including infinite-dimensional G.
The zero space is trivial. There is no compactness claim for this tensor
map. Indeed, for nonzero Af and an infinite orthonormal sequence e_j in G,
images Af tensor e_j have pairwise Lr distance sqrt(2)||Af||Lr; this
sequence has no convergent subsequence.

Choose any complete smooth-test ONbasis of H_t and its first-J projection
pi_J, with pi_0=0. Set
 epsilon_J=||C_t(I-pi_J)||H_t->Lr(I).
Compactness of the accepted scalar C_t gives epsilon_J->0. For precision,
if not, choose unit v_J whose tail images stay bounded below. The vectors
(I-pi_J)v_J are weakly zero because pi_J tends strongly to I. Compactness
gives a norm-convergent image subsequence; every bounded linear scalar
observable has weak limit zero, so that subsequence's norm limit is zero,
a contradiction. Applying (15) to A=C_t(I-pi_J) proves the uniform Hilbert-
valued time-tail bound epsilon_J, with G=H_sp. This proves U3.

## 6. Actual uniform-R completed mean regulator

Define P_ret=pi_J tensor P_K on H_I=H_t tensor H_sp, Q_JK=I-P_ret.
Both factors are real orthogonal projections, so the completed tensor
operator is selfadjoint, idempotent and contractive, first on dense finite
tensors and then on H_I. In general it has INFINITE spatial rank.
The algebraic identity
 Q_JK=(I-pi_J)tensor I+pi_J tensor Q_K                       (16)
is exact. Put c_t=||C_t||H_t->Lr(I), which is finite for 2<r<2/a.

For each fixed R, the accepted compact-valued T_R is bounded and linear,
so mathcalT_R=T_R U is strongly measurable as a K(E)-valued Lr field and
agrees with the actual E restriction of the completed physical mean.
From (6), (15) and the actual temporal tensor identification,
        ||mathcalT_R||H_I->Lr(B(E))<=M_0 c_t.                (17)
For the first term of (16), apply (15) to the scalar time tail and then
(6). For the second, the precise finite-tensor intertwining is
 U(pi_J tensor Q_K)=(I_Lr tensor Q_K)(C_t pi_J tensor I_H_sp).
Density gives the same identity on the completion. Apply (13) pointwise
in time, then (15) to C_t.
This yields the explicit uniform bound
 ||mathcalT_R Q_JK||H_I->Lr(B(E))
       <=M_0 epsilon_J+M_f c_t K^-beta.                     (18)
For example C_U=M_0+M_f c_t gives C_U(epsilon_J+K^-beta).
This proves U4, without asserting uniform-R compactness or finite retained
rank. A heat-filter head and I-heat residual are not used for independence:
P_ret and Q_JK are TRUE orthogonal raw-H projections.

## 7. Actual projected residual and block Cameron application

Keep 1/2<theta<min(1-a/2,(3-a-alpha)/2),
 1/(1-theta)<r<2/a, 1/theta<=p<2<r.
Take integer B>=1, 0<delta<min(1,1/B), N=floor(1/(delta B)), n=N+1,
s_m=m delta B, ell_m=B for m<N and ell_N=1/delta-NB in[0,B). Let
I_m=[s_m,s_m+delta ell_m]; these partition I up to endpoints. Empty final
intervals are retained with norm zero. Write i_I:H_I->H_W for the accepted
isometric closed inclusion, i_I^* its Hilbert adjoint, and extend
 P_full=i_I P_ret i_I^*, Q_full=I-P_full.
This is an orthogonal projection on H_W; no raw time-indicator multiplier
is introduced. Define the ACTUAL fast residual noise and E driver
 Y_m(f)=W(Q_full T_(delta,m)f),
 X_m=g_delta A_R(Y_m), g_delta=delta^((1-a)/2),               (19)
stopping the interaction primitive at ell_m and extending constantly to B.
T_(delta,m) is the accepted raw isometry. Thus Var Y_m(f)<=||f||H_fast^2,
and the accepted Gaussian-transfer theorem constructs (19) on the SAME
original W in the compact-valued E path norm. Its fixed-R,B moments are
finite; no uniform-R stochastic norm bound has been inserted here.
Choosing a Holder exponent strictly above theta within the allowed range
puts the paths in a separable little-Holder/closed path span, as in OWN C3.
The finite tuple is a centered Gaussian Banach variable with norm
       ||x||_(delta,p)=(delta sum_m||x_m||Ctheta^p)^(1/p).    (20)

For h in H_W let Lh=E[(X_m)_m W(h)] be its actual Bochner covariance.
It exists by the fixed-parameter L2 path moments. For a literal completed
row test k of a stopped fast first driver, its slow pullback
T_(delta,m)k belongs to H_I: this is the accepted supported-row argument
in C3 Section7, including boundary approximation inside I. Projection gives
 <Q_full T_(delta,m)k,h>
     =<T_(delta,m)k, i_I Q_JK i_I^*h>.                      (21)
The component of Q_full h orthogonal to H_I disappears because the row
belongs to H_I. This identity holds for the ACTUAL row on the given W,
not just for a replacement covariance law.

Apply the completed J=0 covariance identity C3(12) to Q_JK i_I^*h and
restrict its E inputs/outputs through the accepted isometric inclusion
E->F. The resulting same-W path identity is
 (Lh)_m(u)=sqrt(delta)int_0^min(u,ell_m)
 S_E(-v)mathcalT_R(Q_JK i_I^*h)(s_m+delta v)S_E(v)dv.         (22)
The factor is sqrt(delta) because (19) already includes g_delta; it is
not delta^(a/2) for this SCALED driver. The old exact scalar amplitude
identity g_delta delta^(a/2)=sqrt(delta) is the unchanged accepted
JointTilt.shifted_amplitude application at delta>0. Equality extends from
literal rows and dense states/rational times to the operator paths by the
same fixed-parameter Bochner covariance continuity used in C3; arbitrary
projected controls are handled by its completed H_I mean identity. No
smoothness of P_K controls, finite raw head or time-block independence is
needed. The integrand is Bochner measurable: fixed-R compact operators,
strong continuity of S_E and its adjoint, and finite-horizon bounds give
norm continuity of conjugation on compact operators, exactly as in C3.

We give radius-independent free constants directly on E. In Bessel-unitary
coordinates the full massless wave matrix is
 [cos(v|xi|), <xi>sin(v|xi|)/|xi|;
  -|xi|sin(v|xi|)/<xi>, cos(v|xi|)].
For |v|<=B,B>=1, its upper off-diagonal entry is at most sqrt(2)B:
use |sin(vk)|<=B k for k<=1 and <k>/k<=sqrt(2) for k>=1. Its lower
entry is at most1, its diagonal entries at most1, with the continuous
sine-quotient value v at k=0. The matrix norm is bounded by its Frobenius
norm sqrt(3+2B^2)<=3B. Parseval gives
 G_B=sup_(|v|<=B)||S_E(v)||<=3B.
For the primitive in (22), Holder in time and the affine change from v
to slow time give, with a_m=||mathcalT_R Q_JK i_I^*h||Lr(I_m),
 ||(Lh)_m||Ctheta<=sqrt(delta) C_B delta^(-1/r)a_m,
 C_B=G_B^2[B^(1-1/r)+B^(1-1/r-theta)]
                          <=18B^(3-1/r).                   (23)
The second exponent is positive since r>1/(1-theta); constant stopped
extension preserves the Holder bound and the empty block is zero.

For completeness, the finite Holder input has EXACT application here:
use Real.rpow_sum_le_const_mul_sum_rpow_of_nonneg on the n indices with
exponent r/p>1 and nonnegative values f_m=a_m^p. Its complete accepted
public type then yields
 (sum a_m^p)^(r/p)<=n^(r/p-1)sum a_m^r.
Nonnegative real-power identities and positive exponents, including zero
terms, give after raising to1/r
 (sum a_m^p)^(1/p)<=n^(1/p-1/r)(sum a_m^r)^(1/r).
Here n>=2, delta>0, p>1 and r>p; no negative power of a zero a_m occurs.
Since delta n<=2/B and sum a_m^r is the full Lr norm to the rth power,
(18), (20) and (23) prove
 ||Lh||_(delta,p)
 <=sqrt(delta) C_B (2/B)^(1/p-1/r)
       [M_0 epsilon_J+M_f c_t K^-beta] ||h||H_W.            (24)
This states every block-weight factor; no rank or support volume is hidden.

Finally, this is the actual Cameron embedding bound, not only a surrogate
mean map. The tuple is a centered separable Gaussian linear image of W;
its continuous linear coordinates have the form W(k_l) for k_l in H_W,
as follows from the projected finite-coefficient construction and closure
of the first chaos in scalar L2. Let H_seen be the closed span of all k_l.
The Bochner map L satisfies l(Lh)=<k_l,h>, so it kills H_seen^perp. The
first-chaos Cameron identification established in OWN C3 Section7 gives
its Cameron space L(H_seen). Explicitly, for any h in H_W,
 ||Lh||CM=||P_seen h||H_W,
where P_seen is the orthogonal projection onto H_seen. Applying (24) to
this minimum-norm seen representative bounds ||Lh||_(delta,p) by the
constant in (24) times ||Lh||CM. This is the ACTUAL Cameron embedding,
with no
covariance inverse or finite Gaussian density. This argument does not use
finite rank of P_ret. Gaussian fields generated by the orthogonal P_full
and Q_full directions are independent; different residual time blocks can
remain correlated. No conditioning/infinite-head integration is concluded.
Equation (24), uniformly R>=1, proves the proposed U5.

## 8. Evidence limits and original target

This is a scoped independently accepted argument for the stated LINEAR
deterministic and actual Cameron bounds, with the limitations recorded above. Its all-model core uses the
accepted physical product (1), not the white diagnostic as a premise.
The diagnostics in reviews/2026-10-31-uniform-e-cameron/ use actual d1-white
rows and exact finite tensor algebra; their resolution errors and scope
are stated. They are neither certified enclosures nor a proof of this note.

No new Lean source/kernel/count is claimed. The two old scalar kernels
cover only amplitude cancellation and finite Holder powers under the exact
guards above; source construction, physical products, projections, tensor
limits, Gaussian paths and Cameron identification remain analytic.

Most importantly, (24) does not bound the EXPECTED residual driver norm
uniformly on growing masks. Therefore the prior fixed-R concentration
result cannot yet be upgraded along R_delta=1/delta+2. The retained head
has infinite spatial rank: its eventual local Gaussian Laplace/localization
argument is still absent. GC original-point transfer and SP phase baseline
have their own pending gates. Signed-positive score optimization, intended
author normalization/sharp constants and conditional exact limit remain
OPEN. No F3 reversal, point trace, raw-H Gaussian, Skorohod development,
source repair, contact, HPC, companion, TeX/PDF/wiki/bib or publication act.
