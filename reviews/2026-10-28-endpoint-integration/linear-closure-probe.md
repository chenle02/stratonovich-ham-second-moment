# Gaussian and linear closure of the covariance endpoint condition

Date: 2026-10-28. Status: local argument, independent review pending.
This extends the previously reviewed rotation/finite-sum result; that earlier
review does not certify this new linear-map argument or a moment consumer.

Fix theta in (0,1). Let Gamma,L,S be nonnegative even positive-definite
tempered Radon covariances in R³ with exponents alpha,1,beta, and assume

    p_a*Gamma <= (p_a*L)^theta (p_a*S)^(1-theta)

for EVERY a>0 and EVERY translation. This is the actual deterministic H9
condition; the underlying wave kernel is not transformed.

## Falsification controls first

Take T=diag(2,1,1/2), detT=1. Then eps T^(-1)T^(-transpose) has diagonal
(eps/4,eps,4eps). For the low covariance c dy delta0(dz), the pushforward
is (c/2)dy delta0(dz), not c dy delta0(dz). The normal factor of the
anisotropic Gaussian at T^(-1)x is p_(4eps)(2x3)=p_eps(x3)/2. It matches
the actual pushforward. For T=diag(2,1,1), detT=2, the anisotropic normal
variance remains eps; the required factor1/2 now comes from the determinant.
These two tests distinguish the normal delta scaling from the density Jacobian.

The separate rational matrix check confirms that
Sigma=eps T^(-1)T^(-transpose) and the determinant factor match for these
diagonal cases and a nonsymmetric shear. It is a finite algebra diagnostic,
not a proof or independent certification.

## 1. The comparison holds for every nondegenerate Gaussian

Let q_Sigma be the centered probability density with positive-definite
covariance matrix Sigma. Choose a>0 strictly below its smallest eigenvalue.
Then q_Sigma=p_a*q_(Sigma-aI), by the Gaussian convolution identity. Put
F_J=p_a*J. For J in {Gamma,L,S}, F_J is nonnegative and bounded: it is the
covariance obtained by Gaussian smoothing a positive-definite tempered
covariance, so its absolute value is at most F_J(0)<infinity. Gaussian
weighting of the positive tempered spectral measure proves finiteness.

By Tonelli and Holder on q_(Sigma-aI)(x-dy),

    q_Sigma*Gamma
       <= q_(Sigma-aI)*(F_L^theta F_S^(1-theta))
       <= (q_Sigma*L)^theta (q_Sigma*S)^(1-theta).

All quantities are finite. No limiting or degenerate Gaussian is required.

## 2. Invertible pushforwards preserve the condition

Let T be any invertible real3x3 matrix and d_T=|detT|. Define the three
new covariances by measure pushforward J_T=T_#J. They are positive even
locally finite tempered measures and have the same homogeneous scaling
as J, since T commutes with isotropic dilations. Positive definiteness
can be checked directly. If psi(y)=phi(Ty), then

    (phi*phi_tilde)(Ty)=d_T(psi*psi_tilde)(y),

and hence the quadratic form of T_#J equals d_T times a nonnegative
quadratic form of J. This also treats singular measures.

At every eps>0 and x, put Sigma=eps T^(-1)T^(-transpose). The exact
Gaussian density identity is

    p_eps(Tz) = d_T^(-1) q_Sigma(z).

Consequently

    (p_eps*J_T)(x) = d_T^(-1)(q_Sigma*J)(T^(-1)x).

Apply section1 to Gamma,L,S. The two endpoint Jacobian factors combine
as d_T^(-theta)d_T^(-(1-theta))=d_T^(-1), exactly the target factor.
The common-width comparison therefore holds for the pushforwards at every
eps and x. For an ordinary covariance density j,

    J_T(dx) = d_T^(-1) j(T^(-1)x) dx.

For a plane-supported measure the normal delta and the tangential Jacobian
must be transformed as measures; they cannot be copied as unchanged densities.

## 3. Finite sums and scope

After applying independently chosen invertible T_i to components sharing
alpha,theta,beta, the already reviewed nonnegative finite-sum Holder argument
gives endpoints for sum_i w_i (T_i)_#Gamma_i. The actual static covariance
and low spectral mass are those of the resulting endpoint sums. They need
not retain their untransformed numerical values; no uniform distortion bound
as a matrix approaches singularity is asserted.

In particular linear images of isotropic Riesz densities include ellipsoidal
Riesz covariances, and linear images of ordinary products include oblique
products. This changes only the noise covariance. The conditional moment
theorem, when valid, is reapplied to the original isotropic wave kernel.
No coordinate covariance of the PDE under general T is claimed.

No assertion of an arbitrary-covariance representation, cone density, countable
mixture control, sharp constant, Skorohod result, novelty or Lean proof follows.
