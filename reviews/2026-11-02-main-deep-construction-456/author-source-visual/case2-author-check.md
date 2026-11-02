# Author check of Chen author-page21 Case2

Status: pending adjudication with the already-running constructor audit.
This is not a source-theorem failure claim, manuscript amendment or independent
source-image gate. The printed page was viewed directly; its displayed equality
really removes differing prior-time origins.

Let A,B be the two fixed previous times, and a,b the previous spatial positions.
After setting s=t-A and r=u-B, the temporal argument is
(r+B)-(s+A), not simply r-s. Evenness can reverse the sign but cannot discard
B-A. Retain the shifted argument in the cross integral.

A route to the same final inequality uses the stationary covariance inner
product on full time-space. Extend each positive-time kernel G_i by zero for
negative time, then translate it to its own origin (A,a) or (B,b). The cross
integral is the covariance pairing of these two different translates.
Cauchy–Schwarz bounds it by the product of their covariance norms. Each
self-pairing is invariant under a COMMON translation of its two variables,
so these norms are the original N2 norms. No equality of the cross pairing
with the zero-shift cross pairing is needed.

For nonnegative possibly unbounded kernels, perform the covariance argument
first on bounded compact truncations and pass by monotone convergence; finite
self norms bound the cross limit. Temporal covariance is a positive Laplace
mixture of exp(-lambda*|t-u|), and the spatial covariance is positive definite,
so the full stationary product kernel supplies the positive pairing.

This distinguishes individual self-norm translation invariance from an
invalid independent-translation equality for a cross pairing. The ongoing
DeepSeek packet explicitly asks for the same source shift audit and was not
changed to include this later author note.
