# Exact scaling and a residual-driven scalar calibration

Status: CANDIDATE. Independent analytic/source/type/application review is
pending. The exact scaling below applies to the original covariance class.
The scalar growth result and weak-norm counterexample are auxiliary tests,
not HAM lower bounds. The full sharp target remains open.

## 1. The exact full-class weak-noise problem

Keep d in{1,2,3},0<a<1 and the original nonnegative even positive-definite
homogeneous tempered Radon covariance of degree alpha, alpha+a<2. Set

    kappa=(4-alpha-a)/(3-alpha),
    delta=T^(-kappa), R=T delta=T^((a-1)/(3-alpha)).          (S)

For fixed T>0 define V_delta(t,x)=u(Tt,Rx). Equality here means equality in
law after the noise rescaling; it does not assume pathwise uniqueness. Its
canonical mild series solves the rescaled equation

    delta^2 partial_t^2 V_delta
       =Delta_x V_delta+sqrt(delta) W V_delta,
    V_delta(0,x)=1, partial_t V_delta(0,x)=0,                (W)

where W again has raw covariance |s-t|^(-a)Gamma(x-y). Consequently

    T^(-kappa) log E u(T,0)^2
       =delta log E V_delta(1,0)^2.                         (M)

Here is the complete canonical-series justification. At positive noise
widths, the rescaled Gaussian field W(Tt,Rx) has covariance amplitude
T^(-a)R^(-alpha). This holds distributionally for a homogeneous covariance
measure, including the white endpoint; no angular density is required.
The source's temporal Laplace cutoff obeys
K_eta(Ts)=T^(-a)K_(eta/T)(s), and spatial heat width epsilon becomes
epsilon/R^2. The shared-width max and heat-width sum laws are preserved.
Thus the common Gaussian noise can be rescaled jointly at every vertex.

The wave Green MEASURE obeys

    G_(T tau)(R dz)=R G_(tau/delta)(dz).                    (G)

This follows from G_t scaling as a distribution of degree1-d and remains
true for the spherical measure in d3. Each terminal Duhamel vertex therefore
contributes the time/spatial measure factor TR and the noise amplitude
T^(-a/2)R^(-alpha/2). The scalar exponent identities are

    T^(-a/2) R^(2-alpha/2)=sqrt(delta),
    T^(1-a/2) R^(1-alpha/2)=delta^(-1/2).                   (A)

The second line is the mild vertex factor. The Green kernel of(W) applied
to its forcing is delta^(-1)G_((t-s)/delta), so multiplying by sqrt(delta)
gives exactly delta^(-1/2)G_((t-s)/delta). This proves equality of every
finite list of fixed-order terminal coefficients under the same rescaled
Gaussian law. It includes self-pairings and all unequal/empty-chain splits.
Noise widths tend to zero jointly at fixed T,R; the named prior fixed-order
L2 construction and absolute L2 series convergence pass this identity to
the canonical solution and second moment. In d3 Green smoothing is removed
first on both sides, with its spatial width rescaled by R^2. No interchange
of the large-T limit and regularization limits is used. This proves(S)--(M).

The actual real-power equalities(A), kappa>1 and the physical-space power
in(S) are intended local Lean consumers. The Gaussian/Green/series
identifications remain analytic inputs. In particular(W) is a fast wave
equation, not the usual fixed-speed weak-noise equation in a support theorem.

## 2. Why the held pathwise theorem cannot fill the gap unchanged

The held Chen--Deya--Song--Tindel source, "Hyperbolic Anderson model2:
Strichartz estimates and Stratonovich setting", Theorem thm:wave-eq and
Corollary cor:wave-eq, gives the homogeneous conditions alpha+a<1 in d1
and alpha+a<1/2 in d2. These are stricter than our original alpha+a<2,
and exclude d=alpha1 with positive a. Theorem theo:wellposedness requires
global Sobolev initial data H^(1+k) x H^k; constant1 is not in global L2.
Localizing data would require a growing-cutoff/finite-propagation argument.
Its proof explicitly chooses global Picard iteration rather than patching
small time intervals. It does not supply a restartable phase-space transfer
bound or a spectral lower bound uniform in delta. These are source gaps,
not claims that no such extension can exist.

There is also a normalization to retain. The time primitive of a raw scalar
covariance |t-s|^-a has covariance

    [t^(2-a)+s^(2-a)-|t-s|^(2-a)]/[(1-a)(2-a)].              (P)

The source's R_a has the same numerator divided by2. With H=1-a/2 its
derivative covariance is H(2H-1)|t-s|^-a. Thus a raw primitive is the source
primitive divided by sqrt(H(2H-1)). No first-moment normalization repair is
being adopted here.

## 3. Scalar stability with the residual retained

Consider the scalar calibration

    delta^2 y''=y+y b_delta', y(0)=1,y'(0)=0,               (C)
    eta_delta=delta^(-1) sup_(|t-s|<=delta)
                          |b_delta(t)-b_delta(s)|.

Here0<delta<=1. The driver is continuous on[0,1], with b_delta(0)=0. For a smooth driver
this is the classical equation; for a continuous driver it is defined by
the gauge equation below, equivalently integration by parts for integral
y db_delta since y is C1. If eta_delta tends to zero, then

    y(1)>0 eventually, delta log y(1) -> 1.                 (L)

The conclusion is uniform over drivers with this microscopic increment
bound. It retains the residual rather than replacing it by a deterministic
surrogate. It is scalar: spatially constant covariance has spatial degree alpha=0 and is
outside the target positive-alpha covariance class.

To prove(L), on a block t=j delta+delta tau of length delta set
Y=(y,delta y'), omega(tau)=(b_delta(t)-b_delta(j delta))/delta,
and A=!![0,1;1,0], N=!![0,0;1,0]. Then

    dY=A Y d tau+N Y d omega,
    Y=(I+omega N)X,
    X'=B_omega X, B_omega=!![omega,1;1-omega^2,-omega].      (B)

Because N^2=0 and y has bounded variation, this change of variables uses
ordinary integration by parts; no rough-path enhancement is required for
the scalar equation. Conversely a continuous omega gives a continuous
matrix B and an ordinary linear ODE for X, which defines(C) uniquely.

Use the induced infinity matrix norm. Write E(t)=exp(t A); its entries are
cosh(t),sinh(t), and ||E(t)||=exp(t). If |omega|<=eta<=1/80, then
||B_omega-A||<=eta+eta^2<=2eta and ||B_omega||<=2. Duhamel gives, on a unit
block, ||F_omega(1)-E(1)||<=2eta exp(2)<=18eta. The endpoint gauge factor
therefore bounds the actual transfer matrix T_j by

    ||T_j-E(1)|| <=40 eta,
    (1-40eta)E(1) <= T_j <= (1+40eta)E(1) entrywise.         (T)

Indeed ||I+omega N||<=2, ||omega N||<=eta and exp(1)<3 give the error at most39eta. Every entry of E(1) exceeds1, which implies the entrywise claim.
In particular each full-block matrix is positive. With n=floor(1/delta),
positivity and induction, without any commutation of the T_j, yield

    (1-40eta)^n E(n)(1,0) <= Y_n
       <= (1+40eta)^n E(n)(1,0).                           (F)

After at least one full block, the component ratio is at most
3 coth(1)<6: each component ratio of a positive T_j vector is bounded by
the largest column ratio, and(1+40eta)/(1-40eta)<=3. On the final fractional
block, the off-diagonal entries of B_omega are nonnegative. Its ODE preserves
nonnegative X, so X_1'>=-eta X_1. Also ||F_omega(tau)||<=exp(2) for tau<=1.
As y=X_1, this gives

    exp(-eta)y_n <= y(1) <=54 y_n.                          (R)

Using exp(n)/2<=cosh(n)<=exp(n), (F)--(R) imply

    delta n[1+log(1-40eta)]-delta(log2+eta)
       <= delta log y(1)
       <=delta n[1+log(1+40eta)]+delta log54.                (Q)

Since delta n tends to1 and eta tends to zero, (L) follows. This proves the
scalar stability assertion, including the final fractional block.

For example, take b_delta=sqrt(delta)(B-B(0)) with a fixed theta-Hölder continuous
path B and theta>1/2. Then eta_delta<=||B||_theta delta^(theta-1/2) tends to
zero. A Gaussian time primitive with covariance(P) is almost surely
theta-Hölder for every theta<1-a/2, by its Gaussian increment moments and
the Kolmogorov criterion. Such a theta>1/2 exists for every0<a<1. Thus(L)
holds samplewise in this scalar weak-noise calibration. No SPDE stability
claim follows from this statement.

## 4. A uniform C0 replacement is false

Small global C0 norm of b_delta is insufficient. Take delta=1/(2n) and
b_delta triangular periodic of period2delta, with derivative-1 on the
first half and+1 on the second. Its sup norm is delta, so even
||b_delta/sqrt(delta)||_infinity tends to zero. In time tau=t/delta the
coefficient of(C) alternates between0 and2, each for one unit of time.
The two transfer matrices give the period monodromy

    P0=!![1,1;0,1], P2=!![c,s;2s,c],
    M=P2 P0=!![c,c+s;2s,c+2s],
    c=cosh(sqrt2), s=sinh(sqrt2)/sqrt2,
    det M=1, tr M=2(c+s).                                  (D)

All entries are positive. Its Perron eigenvalue is
lambda=c+s+sqrt((c+s)^2-1)>1; the other is1/lambda. The coefficient of
lambda^n in the first component of M^n(1,0) is
(c-1/lambda)/(lambda-1/lambda)>0. Hence

    delta log y(1) -> rho=(log lambda)/2, 0<rho<1.           (N)

For the strict upper inequality no floating computation is needed. Take
the positive Perron solution y_* in one period; its derivative is positive
because the initial Perron vector is positive and q(tau) is0 or2. Then
r=y_*'/y_*>0 is2-periodic and r'+r^2=q almost everywhere. Integration gives
(1/2)integral_0^2 r^2=1, while rho=(1/2)integral_0^2 r. The function r is
not constant, since q takes two different values. Strict Cauchy--Schwarz
therefore gives rho^2<1. This proves(N) and the weak-norm counterexample.
Its microscopic eta_delta is1, so it does not contradict Section3. It also
does not refute convergence in probability for a fixed Gaussian driver.

## 5. The first open SPDE consumer

The scalar gauge drift contains the NEGATIVE square-omega^2. If one tries
to apply the same velocity gauge to a spatially rough noise primitive, the
corresponding square is not automatically defined. A spatial mollification
does not solve this consumer unless the resulting bounds are uniform as the
cutoff is removed and compatible with the chosen delta scale. Our accepted
projection-residual obstruction forbids simply dropping the omitted noise
by covariance Loewner order. We establish no such cutoff-uniform estimate.

For a direct lower bound one would need actual events A_delta with

    liminf delta log P(A_delta)>=-I(h),
    liminf delta inf_(A_delta) log|V_delta(1,0)|>=Lambda(h).  (H)

Their nonnegative squared contribution would give2Lambda(h)-I(h). This is
only the missing micro-contract: no such SPDE events/growth bound or
identification of its variational value with the intended source constant
is proved. The held pathwise theorem and the scalar gauge do not fill it
unchanged. General covariance, all-order/sharp upper and sharp lower targets
remain intact. No Skorohod, novelty, circulation or companion claim.
