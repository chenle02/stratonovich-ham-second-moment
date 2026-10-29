# Exact common-noise projection profiles

This clarifies the regularization step of the projection-residual proof.
The first six-check HIGH review accepted the analytic obstruction but noted
that the regularization operator was unspecified. The generic phrase
"mollifications of m" is replaced by the actual temporal cutoff/spatial heat
construction. The parent coefficient, projection lower bound, strict gap,
full-mean claim and both Lean proof sources are unchanged.

Source: current64-page author PDF, SHA256
5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c,
physical pages8--9, equations(2.9)--(2.11). The source explicitly distinguishes
ordinary temporal convolution from its chosen Laplace cutoff. No arXiv-v1
theorem is substituted. The two full source-page images and extracted text
are supplied for the focused check.

Keep the fixed FULL-noise coordinate Z=W(psi)/sqrt(V) from the proof. Do not
renormalize a regularized coordinate at each width. Write gamma(x)=|x|^-1/2
and separate its amplitude1-a. The source's shared-noise construction uses
independent Gaussian lambda slices, giving

    K_delta(t)=Gamma(a)^(-1)
        integral_0^(1/delta) exp(-lambda|t|)lambda^(a-1)dlambda,
    0<=K_delta(t)<=|t|^-a,
    Cov(W_(epsilon,delta)(s,x),W_(epsilon',delta')(t,y))
       =(1-a)K_(max(delta,delta'))(s-t)
               (p_(epsilon+epsilon')*gamma)(x-y).           (S)

The source writes W as the sum of all independent lambda slices, W_delta
as the sum below1/delta, and W_(epsilon,delta)=p_epsilon*W_delta in SPACE.
Consequently its covariance with W(psi) uses exactly the retained slices,
not a new cutoff of the test coordinate. For the indicator psi this yields

    m_(epsilon,delta)(s,x)=Cov(W_(epsilon,delta)(s,x),Z)
       = [(1-a)integral_0^1 K_delta(s-r)dr]
            (p_epsilon*F)(x)/sqrt(V).                      (P)

This identity first holds for smooth compact test approximants to psi.
The H-norm convergence of those tests and the finite L2 norm of the fixed
W_(epsilon,delta)(s,x) pass the covariance to psi by Cauchy--Schwarz. The
integral passes by dominated convergence: K_delta is bounded at fixed delta,
p_epsilon*gamma is bounded at fixed epsilon, and all tests have bounded
support. Thus the actual Gaussian-coordinate covariance is(P).

For0<=s<=1, the first bracket is bounded by
B_a(s)=s^(1-a)+(1-s)^(1-a)<=2. The heat average of globally bounded positive
F is at most4. Hence0<=m_(epsilon,delta)<=8/sqrt(V), uniformly in BOTH widths.
As delta decreases to zero the first bracket converges to B_a(s) by positive
monotone convergence, and p_epsilon*F converges to F(x) since F is bounded
and continuous. These independent factors give joint convergence to m for
every interior s and every x. The product of two such profiles is bounded
by64/V on the finite-mass terminal n2 kernel. Its integral therefore converges
to A_P by dominated convergence.

At positive widths the joint Gaussian vector with the fixed Z, under L_q(Z),
has covariance C_(epsilon,delta)+(q-1)m_(epsilon,delta) tensor
m_(epsilon,delta). Ordinary Wick expectation of the n2 terminal kernel is
A_(C_(epsilon,delta))+(q-1)A_(P_(epsilon,delta)). Parent fixed-order L2
convergence and L_q in L2 pass the left side to E_Q X_2. The parent term
passes by its already-reviewed construction; the new term passes by the
bounded-profile argument above. This proves E_Q X_2=A_C+(q-1)A_P using the
actual source coupling, with no positivity assumption on C-P and no new
nonstationary existence theorem.

The geometric bound in Section4 also has a direct named-input proof. Apply
canonical P:mixed to the admissible parent covariance r^2C, on the same noise
space. Fixed-order n-linearity gives r^n X_n. All mixed moments in its full
second-moment series are nonnegative, so
r^(2n)E X_n^2<=E|u_C(r)|^2=B_r. Summing the resulting norm bounds gives(T).
No uniform-in-regularization hypothesis of L:uniform-series-tail is invoked.
The remaining density/Picard remainder arguments from the primary proof
then apply unchanged. Density L2 finiteness is0<q<2; variance inflation uses
the narrower1<q<2. The proposed large-time bridge assumes a valid ell>0.

An incidental assertion in the first review reason is NOT adopted: C-P is
not negative on the entire cone. Only its weighted integral is negative here.
The singular positive parent kernel is unbounded near spatial coincidence,
whereas P is bounded. No pointwise cone-sign claim is needed by the proof.
This clarification does not change the accepted integrated coefficient gap.
