# Falsification of unrestricted additive-covariance logconvexity

Status: local exact control,UNREVIEWED;not part of the54page assembly/review.
This is a guard on a possible time-block-mixture proof,not a new accepted no-go.

Consider the static scalar wave ODE y''=Zy,y(0)=1,y'(0)=0,where Z is a real
centered Gaussian of variance A. The entire solution is cosh(sqrt(Z)) at t1,
interpreted by its real power series also for negative Z. Gaussian moments
and cosh²(w)=(1+cosh(2w))/2 give

 F(A)=E[y(1)²]=1+sum_(k>=1)2^(3k-1)(2k)! A^k/[k!(4k)!].

Termwise expectation is justified by E exp(2sqrt(|Z|))<infinity. All remaining
series terms are positive. For k>=1,the next/current term ratio is
16A(2k+1)/[(4k+1)(4k+2)(4k+3)(4k+4)]<=16A/(4k+1)^3.
After order N20,the positive tail is at most term_(N+1)/(1-q),
q=16A/(4N+1)^3<1. Exact Fraction calculations at A99,100,101 show

 lowerF(100)² > upperF(99)*upperF(101),

with the exact positive rational margin retained in the JSON. Hence a generic
argument claiming logconvexity in ADDITIVE Gaussian covariance amplitudes is
false. This does not affect the valid coefficient Holder in the manuscript:
that uses geometric interpolation,which corresponds to log amplitude rather
than amplitude. Positive power-series coefficients indeed give logconvexity
in log A.

This toy is the alpha=alpha0=0 endpoint,outside the strict project regime.
No false claim is made that this alone refutes a specialized interior-noise
inequality. Its role is falsification BEFORE investing in an unrestricted
Gaussian covariance-mixture shortcut. Any restricted replacement needs its
own proof;the original full upper/sharp targets remain open.
