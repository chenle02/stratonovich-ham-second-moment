# Pre-proof falsification screen for the proposed unmasking target

DIAGNOSTIC, not independent U1-U4 acceptance. No numerical eigenvalue,
new kernel run or certified approximation is claimed.

## Invariant-direction covariance rejects unmasked ground-state assumption

Take d2, Gamma=delta0(dx1) dx2, alpha1, and ANY 0<a<1. Homogeneity is
Gamma(rA)=r Gamma(A), so alpha+a<2. This is positive definite: its
spatial covariance pairing of q with q is
int_R (int_R q(x1,x2)dx2)^2 dx1>=0, up to the same fixed Fourier convention.
It is a nonnegative locally finite tempered measure. Choose positive
smooth compact f(t),q1(x1),q2(x2), with f supported inside(0,1), and
Psi=f q1 q2. Direct integration gives
 h_s(x1,x2)=k_f(s) q1(x1) int q2,
independent of x2. Thus global C0 decay and compact spatial support of
unmasked h are FALSE in the original admissible class.

Fix one s. The one-dimensional bounded compact potential
b(x1)=k_f(s)q1(x1)int q2 is nonzero positive. The accepted compact family
trial/minmax input in d1 gives bottom e1<0, with a unit ground p in H1.
For every real unit g in C_c^infinity(R), let g_L(y)=L^-1/2 g(y/L).
Then the unit product p(x1)g_L(x2) has two-dimensional Rayleigh value
 e1+L^-2 ||g'||2².
Conversely applying the one-dimensional Rayleigh lower bound on each
x2-slice and adding the nonnegative x2-gradient term shows H>=e1.
The two-dimensional bottom is therefore e1. If a unit H2 vector F were
an eigenvector at e1, its shifted quadratic form would be zero; both
nonnegative terms force ||partial_(x2)F||2²=0. An L2 function independent
of x2 is zero (Fourier transform or weak-derivative slicing). Contradiction.
So the bottom is NOT an L2 ground eigenvalue. These form steps use smooth
approximation/Fubini and extend to H1; no stochastic result is inferred.

This falsifies the tempting stronger claim, not U1-U4: those statements
use the unmasked Rayleigh bottom and only compact-mask ground states.
No unmasked ground projection, gap or cone is allowed in the next proof.

## Covariance and scalar scale controls

For d1 white Gamma=c delta0, alpha1, D_r Psi=r² Psi(t,r x).
Then h_r=r² h(t,r x), the raw variance scales as r^3, and the Rayleigh
rate as r. This matches q=4-alpha=3. A wrong omission of the spatial
Jacobian would give r^4 cost and fail this exact white control.

For the d2 invariant Gamma above, alpha1, D_r Psi=r³ Psi(t,r x).
The integral in the invariant direction contributes r^-1, again giving
h_r=r² h(t,r x); pairing with Psi_r and dx contributes r^(3+2-2)=r³.
The same raw variance exponent holds as in white d1, without treating
Gamma as a Riesz density. At compact level m_R(r x)=m_(R/r)(x), so
keeping R fixed under dilation is generally FALSE.

The factor c^(q/(q-1)) comes from r=c^(1/(q-1)) and c r=r^q.
It is an identity of auxiliary score suprema, not an actual p1 growth
statement. This screen does not identify S_1 with a source constant.
No dimension-specific rough occupation X estimates are imported.
