# All-order static phase question: Gaussian Fock cutoff and numerical range

Status: UNREVIEWED proposal,not part of the seven-check phase review.
This is a route toward the ORIGINAL full spatial covariance class,not a
replacement target. Every operator/domain/limit claim below needs proof or
an exactly matching imported theorem before use. No all-order result is
accepted here.

The reviewed first-variance estimate is complete but does not iterate by
covariance monotonicity. A potentially useful next tool is a Gaussian chaos
cutoff before taking spatial smoothing to zero. For a finite real Gaussian
basis write W_epsilon(x)=sum_i g_i e_i(x). With A_lambda=lambda²-Delta put

 H_i=A_lambda^{-1/2} M_{e_i} A_lambda^{-1/2}.

These are selfadjoint. A CANDIDATE row/column variance bound follows from
the new shifted resolvent lemma:

 sum_i H_i² <= R_alpha lambda^{alpha-4} I.

For the full stationary basis the middle expectation is the Fourier
multiplier J_lambda(eta)=int mu_epsilon(dxi)/(lambda²+|eta+xi|²),and the
outer A_lambda^{-1/2} factors give the extra lambda^{-2}. Finite basis sums
are positive sub-sums. This must be written rigorously on L2 before reuse.

On normalized Hermite chaoses,multiplication by g_i is creation plus
annihilation with coefficients sqrt(n+1),sqrt(n). If P_N keeps chaos degrees
at most N,the corresponding CANDIDATE sandwiched form bound is

 ||A_lambda^{-1/2} P_N W_epsilon P_N A_lambda^{-1/2}||
 <= 2 sqrt(N+1) sqrt(R_alpha) lambda^{(alpha-4)/2}.

Unlike unsandwiched multiplication,this uses selfadjoint H_i with BOTH
row and column variances. Do not assume the same estimate for
A_lambda^{-1/2}W_epsilon: its row variance can diverge as epsilon->0.
That distinction is precisely why a naive bounded-generator proof stops
at the low-alpha threshold.

If the displayed bound holds uniformly for every lambda,optimizing lambda
suggests a numerical-range form bound of order a=alpha/2<1:

 |<P_N W_epsilon P_N u,u>|
 <= C sqrt(N+1)||u||^{2-a}||grad u||^a.

The intended next source check is whether a COMPLEX coupling z then has a
uniform cosine-family bound on a Cauchy circle of radius proportional to
lambda^{2-a}/sqrt(N+1). A real selfadjoint energy bound is NOT sufficient to
extract Taylor coefficients by Cauchy. Complex numerical-range control,
weak phase norm conversion,and constants independent of smoothing/chaos/
spatial cutoff must all be justified. The new Crouzeix references were
queued for precisely that question,not imported as already matching it.

A useful proof assignment would establish the complex phase bound
||M_z(h)||_{X_lambda->X_lambda} <= C exp(C lambda h)
on that circle,with uniform constants. Gaussian chaos cutoff N>=n leaves
the nth Duhamel word from the vacuum unchanged. Formally,Cauchy plus
lambda approximately n/h would then recover static n-term bounds with
(n!)^{-(3-alpha)/2},rather than losing the all-order factorial budget.
This remains conditional until the phase bound and cutoff removal are proved.

There is a separate SMALL-BLOCK ISSUE even after that program. Changing
output norm from X_{n/h} back to one fixed global X_lambda can lose a factor
n/(lambda h). Squaring that loss for two positive orders can destroy the
summability that the exact first-variance calculation retained. Coarse
coefficient bounds therefore do not suffice for a multilevel time-block
argument. Retain the distinct cross/creation and same-chain/mean contraction
bounds,or find a stronger uniform phase estimate. Overlapping time levels
and the colored temporal limit are still further open steps.

[held back: collaborators' unpublished work]

## More concrete bounded-cutoff proof assignment

One can first use a spatial Fourier BAND cutoff (bounded operator,not
necessarily finite-dimensional)and finite Gaussian basis,then take limits.
Crouzeix-Palencia2017 is for bounded Hilbert-space operators,so finite
matrix dimension is not the key restriction. Let L(z)=-Delta-z P_NWP_N
and L_lambda(z)=L(z)+lambda². On a sufficiently small normalized coupling
circle,the candidate sandwich bound gives coercivity of L_lambda+t
uniformly in t>=0. A proposed square-root comparison uses

 A_lambda^{1/2}[L_lambda^{-1/2}-A_lambda^{-1/2}]
 = (1/pi)int_0^infty t^{-1/2} A_lambda^{1/2}
   [ (L_lambda+t)^{-1}-(A_lambda+t)^{-1} ]dt.

Resolvent identity and the sandwich bound at kappa=sqrt(lambda²+t)
suggest an integrable norm majorant C |z| sqrt(N+1) kappa^{a-3}t^{-1/2}.
Its integral scales as C |z| sqrt(N+1)lambda^{a-2}. This step and its
adjoint/inverse variants must be checked:it is intended to control the
WEAK phase weights,not just a position-only cosine norm. A generic Kato
square-root identification must not be assumed without such an estimate.

If numerical range L(z) is in a horizontal parabola and Re(L+lambda²)>0,
the bounded-operator spectral-set estimate could be applied to the functions
cos(h sqrt(w)), sqrt(w+lambda²)sin(h sqrt(w))/sqrt(w),and
w sin(h sqrt(w))/(sqrt(w+lambda²)sqrt(w)). The removable values at w=0,
branch at -lambda²,normalized-circle coercivity,and uniform bounds must be
spelled out. Together with the square-root comparisons these would bound
all four phase blocks,including incoming H^{-1}_lambda velocity. The
matrix phase entries themselves are entire in z,so Cauchy extraction must
be applied to those entries,not to a branch-dependent auxiliary expression.

This is an explicit proof assignment,NOT a completed result. First obtain
and read a version-pinned primary2017 PDF and verify the bounded-operator
holomorphic-calculus statement. Then prove cutoff independence and the
vacuum-to-nth-Duhamel identification. Do not claim that this assignment
already solves small-block uniformity or overlapping colored-time levels.
