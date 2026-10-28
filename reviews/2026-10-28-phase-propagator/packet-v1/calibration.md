# Falsification and next-use boundaries

The static phase estimate is a new full-spatial-class building block,NOT a
proof of G:upper. It controls only the complete first variance coefficient
of the displayed three-term Duhamel polynomial. No all-order static phase
estimate,temporal covariance comparison or time-block composition is proved.

## Scalar falsification before the proof

The scalar spatially constant covariance is alpha=0,outside the theorem.
For y''=sigma Z y,unit-time Z standard Gaussian,and phase norm u²+v²,
the entire phase matrix is M(sigma Z),where

 M(z)=[[cosh(sqrt z),sinh(sqrt z)/sqrt z],
       [z sinh(sqrt z)/sqrt z,cosh(sqrt z)]].

M=M0+zM1+z²M2+...,with the exact rational matrices in checks.py. For any
initial phase x,the coefficient of sigma² in E|M(sigma Z)x|² is x^T K x,
where K=M1^T M1+M0^T M2+M2^T M0. Exact arithmetic gives

 K=[[4/3,4/5],[4/5,17/45]],  (1,-2)K(1,-2)^T=-16/45.

The first random term alone has a nonnegative squared norm,but its cross
term with the mean second-order phase cannot be dropped. This also shows
why arbitrary-phase energy cannot simply inherit the original (1,0)
solution-value covariance monotonicity. If the exact scalar full flow is
considered,the same coefficient is its actual local Taylor coefficient:
for bounded real sigma,each of the first four sigma derivatives of M(sigma Z)
is bounded by a polynomial in |Z| times exp(C sqrt(|Z|));Gaussian integration
is finite. Dominated differentiation and Gaussian symmetry give
E|M(sigma Z)(1,-2)^T|²=5-16sigma²/45+O(sigma^4).
This observation is not a counterexample to the HAM target or its original
data and temporal assumptions.

The local checks also sample the exact centered spherical Riesz convolution
and radial resolvent formula. The slow alpha1.9 improper quadrature is only
required to agree at relative1e-4;the proof uses the exact beta integral,
not a claim of fifty correct digits in that quadrature.

## Positive fine-block arithmetic,but no composition theorem

There is a useful necessary scale check for a future block argument. Fix
lambda>0,and take fine block lengths h_j=2^{-j}/lambda with j>=0 and variance
amplitudes a_j=h_j^{-alpha0}. The proposition's first-random contribution
per block is bounded by C a_j h_j² lambda^{alpha-2}. Its mean-second-order
contribution to the phase energy is bounded by C a_j h_j^{3-alpha}/lambda.
Here lambda h_j<=1 absorbs the explicit free factors into C.

For T/h_j disjoint blocks,the SUM of these individual coefficient BOUNDS
(not an identified coefficient of the product) is proportional to

 T lambda^{alpha-2} sum_j h_j^{1-alpha0}
 +T/lambda sum_j h_j^{2-alpha-alpha0}.

Both geometric series converge because alpha0<1 and alpha+alpha0<2.
Their total is at most C T lambda^{alpha+alpha0-3}. This is exactly the
original integrability range,without an angular-density restriction. The
calculation only sums deterministic upper bounds;it does not exchange a
solution limit or control the mixed Wick terms between overlapping levels.

## Next unresolved operator question

A useful all-order estimate must have small-block losses approaching1 at a
rate summable over this hierarchy. A fixed multiplicative constant per block
would diverge as the mesh tends to zero. Existing static solution-value
asymptotics do not give that estimate. The Gaussian second-order mean must
remain in every norm expansion,and arbitrary-phase covariance monotonicity
is unavailable. Keep the same spatial covariance class and actual regularized
Stratonovich model when testing any proposed higher-order estimate.
