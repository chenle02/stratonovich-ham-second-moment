# Rank-one projection does not permit discarding the residual

Status: primary analytic/type/application review passed six checks HIGH at
source efbdbd9. An explicit common-noise cutoff clarification is awaiting
its focused source-fidelity check; no final adoption of that update yet.
This is a fixed-horizon, small-coupling obstruction to a particular proposed
lower-bound shortcut. The parent is an admissible Stratonovich HAM. It is
not an obstruction to every covariance tilt or to the sharp asymptotic goal.

## 1. The proposed consumer and the counterexample

Set d=1, alpha=1/2, a=99/100, horizon T=1, terminal point x=0. Let W have
covariance

    C((s,x),(t,y))=(1-a)|s-t|^(-a)|x-y|^(-1/2).             (C)

The factor1-a is a positive spatial amplitude: Gamma(x)=(1-a)|x|^(-1/2)
is even, nonnegative, positive definite, homogeneous and locally integrable.
The parameters satisfy alpha+a<2. These are the original model assumptions.
For example, positive definiteness follows from the positive Gaussian-kernel
mixture |x|^(-1/2)=Gamma(1/4)^(-1) integral_0^infinity
v^(-3/4) exp(-v x^2)dv. The analogous Gaussian mixture works for the temporal
power. Local integrability and polynomial growth give a tempered Radon kernel.

Let psi=1_[0,1] x 1_[-1,1] be a spacetime test, let V=E[W(psi)^2], and put
Z=W(psi)/sqrt(V). The covariance profile m(s,x)=E[W(s,x)Z], interpreted as a
covariance with a generalized field, gives the rank-one kernel P=m tensor m.
Gaussian projection gives W=Zm+Wperp, with independent residual Wperp and
covariance C-P>=0 in Loewner order. P is also pointwise nonnegative.

For a covariance D write A_D for its ordinary degree-two mean coefficient
at (1,0). We prove

    A_C=20000/1932951 < 1/96,
    A_P >= 101/(3200 sqrt(2)) > 1/48.                       (A)

In particular A_P-A_C>1/96. Thus Loewner positivity of the residual does not
make its contribution to this wave mean nonnegative.

For fixed1<q<2 let Q=C+(q-1)P. This is the actual variance-q tilt of the
coordinate Z, retaining Wperp. Linearity of the degree-two coefficient gives

    A_Q=A_C+(q-1)A_P < q A_P-1/96=A_(qP)-1/96.              (Q)

Both C and Q are pointwise nonnegative covariance kernels. Q and P generally
are nonstationary and nonhomogeneous; only their parent C is claimed to be
in the original class.

The comparison also fails for full means at sufficiently small positive
noise coupling. Let u_C(h) denote the original solution with noise hW. For
Q, use this same measurable solution functional under the equivalent
variance-q law. For qP, use the ordinary bounded-potential mild equation
with noise h sqrt(q) Zm. As h decreases to zero,

    E_Q u_C(h)=1+h^2 A_Q+O(h^4),
    E u_(qP)(h)=1+h^2 q A_P+O(h^4).                         (M)

Consequently E_Q u_C(h)<E u_(qP)(h) for all sufficiently small h>0. The same
argument at q=1 gives E_C u_C(h)<E u_P(h). This refutes the unconditional
mean comparison used to discard a Loewner-positive Gaussian residual.

## 2. Normalize the actual projection

The noise Hilbert space has inner product induced by(C). The indicator psi
belongs to its completion: bounded compactly supported smooth approximants
converge by dominated convergence for the locally integrable product kernel.
They can be chosen bounded by one on a fixed compact set. Direct integration
gives

    E_phi=integral_[-1,1]^2 |x-y|^(-1/2) dxdy=16 sqrt(2)/3,
    V=2 E_phi/(2-a),
    m(s,x)=B_a(s) F(x)/sqrt(V),                             (P)
    B_a(s)=s^(1-a)+(1-s)^(1-a),   0<=s<=1,
    F(x)=integral_[-1,1] |x-y|^(-1/2)dy.

For |x|<=1, F(x)=2(sqrt(1+x)+sqrt(1-x))>=2sqrt(2), since the square of
the sum is at least2. It is globally bounded by4: outside[-1,1] it equals
2(sqrt(|x|+1)-sqrt(|x|-1)), which decreases from2sqrt(2). For s in[0,1],
B_a(s)>=s+(1-s)=1 and B_a(s)<=2. Hence m is nonnegative and bounded on
the observation interval, and on its backward light cone

    m(s,x)m(t,y) >= 8/V=4(2-a)/E_phi.                      (L)

Projection positivity is a separate, elementary Gaussian Hilbert fact:
for any test f, Var(W(f))-Cov(W(f),Z)^2>=0 by Cauchy--Schwarz. Moreover the
Gaussian residual is orthogonal to Z, so independent. This does not imply
that the residual kernel is pointwise nonnegative. No independence of two
wave paths or replacement of the ordinary Stratonovich mean is being used.

## 3. Compute and bound the first mean coefficient

The terminal Picard kernel underlying the named prior fixed-order
Stratonovich construction (canonical P:mixed) gives the single self-pair
integral, with G_t(x)=1{|x|<t}/2,

    A_D=integral_(0<s<t<1) integral_(R^2)
          G_(1-t)(-y) G_(t-s)(y-z) D((s,z),(t,y)) dzdy dsdt. (I)

For the added bounded profile the same formula follows directly by Wick's
identity at positive widths and the limit justified in Section4. No time
reversal of a nonstationary kernel is used. There is one Wick pairing and
no factorial multiplier. For(C), integrate z
first. The spatial factor is (t-s)^(1/2)/(1-alpha) with alpha=1/2; the
remaining Green mass is1-t. Thus

    A_C=(1-a)/(1-alpha)
          /[(2-alpha-a)(3-alpha-a)(4-alpha-a)]
        =20000/1932951.                                    (R)

Indeed with r=t-s the time integral is
(1/2) integral_0^1 r^(1-alpha-a)(1-r)^2 dr, equal to the reciprocal of
the three displayed factors. The kernel is integrable since alpha+a<2.
At the chosen parameters20000*96=1920000<1932951.

For P, every contributing vertex satisfies |y|<1-t and |z|<1-s, so(L)
applies. With covariance replaced by the constant one, the integral(I) is

    integral_(0<s<t<1) (1-t)(t-s) dsdt=1/24.

It follows that

    A_P >= [4(2-a)/E_phi]/24=(2-a)/(32sqrt(2))
          =101/(3200sqrt(2)) > 1/48.                        (B)

The last strict inequality follows from sqrt(2)<3/2 and101>100. This proves
(A), and linearity gives(Q). The local ProjectionResidual scalar consumer
checks the actual rational/square-root gap and its affine tilted-coefficient
application; the Gaussian, cone and integral identifications are outside Lean.

## 4. Pass to full means without assuming a new Q-model theorem

Write the original ordinary Stratonovich expansion at (1,0) as
u_C(h)=sum_(n>=0) h^n X_n. Named prior inputs are canonical P:mixed and the
parent construction: nonnegative mixed moments, convergence in L2 and
finiteness for every amplified homogeneous covariance. Fix r>1 and
B_r=E|u_C(r)|^2<infinity. Apply P:mixed to the admissible covariance r^2 C.
The same-noise n-linearity identifies its coefficients with r^n X_n, so its
nonnegative mixed series contains r^(2n) E X_n^2. This gives the following
bound directly, without the uniform-regularization premise of the separate
L:uniform-series-tail:

    ||X_n||_2 <= sqrt(B_r) r^(-n),
    ||sum_(n>=4) h^n X_n||_2
       <= sqrt(B_r) (|h|/r)^4/(1-|h|/r),   |h|<r.           (T)

The variance-q density is

    L_q(Z)=q^(-1/2) exp((1-1/q) Z^2/2),
    E L_q=1,   E L_q^2=[q(2-q)]^(-1/2),  1<q<2.           (D)

These are the elementary one-coordinate Gaussian integrals already screened
in the earlier variance-tool work. Cauchy--Schwarz transfers(T) to an O(h^4)
L1 remainder under this density. The tilted law is Gaussian with covariance
Q and is equivalent to the parent, so the original measurable solution is
well-defined under it. Global sign symmetry kills odd-order expectations.
The fixed-order Wick identity gives E_Q X_2=A_Q: at positive regularization
widths this is the ordinary Gaussian covariance formula; L2 parent
convergence and L_q in L2 pass the expectation to the limit. The projection
profiles use the source's common-noise temporal Laplace cutoff and spatial
heat average, not temporal convolution. Explicitly, with K_delta the
truncated temporal covariance of current author(2.9)--(2.11),

    m_(epsilon,delta)(s,x)
      = [(1-a) integral_0^1 K_delta(s-r)dr]
          (p_epsilon*F)(x)/sqrt(V).

The bound0<=K_delta<=|.|^(-a) gives0<=m_(epsilon,delta)<=8/sqrt(V), and
the profiles converge to m at interior times and every spatial point by
monotone convergence in the temporal factor and the heat approximate
identity for bounded continuous F. Thus the P integral passes by dominated
convergence on the finite-mass terminal kernel. The source coupling, cross-
covariance with Z and this exact limit are detailed in the accompanying
regularization addendum. Therefore the first line of(M) follows. We do not
invoke Chen's stationary representation for the nonstationary Q.

For qP, m is bounded by some M on[0,1] x R. Deterministic Picard iteration
has coefficients d_n with |d_n|<=M^n/(2n)! at horizon one, by the Green mass
identity integral G_t=t and induction. With noise h sqrt(q) Zm, the absolute
mean series is bounded by E cosh(sqrt(M sqrt(q)|Z|)) at |h|<=1. It is finite:
sqrt(v)<=1+v and the Gaussian has all exponential moments of |Z|. Factoring
|h|^4 from its tail gives O(h^4); odd Gaussian powers vanish. Its degree-two
term is q A_P. This proves the second line of(M), hence the strict full-mean
comparison for small h. This proves the stated obstruction.

## 5. What remains for a useful large-time lower bridge

The known finite-coordinate density mechanism itself is not disproved. For
an N-dimensional orthogonal Gaussian projection P_T and fixed1<q<2 it gives

    E u_C(T,x)^2 >= [q(2-q)]^(N/2) [E_Q u_C(T,x)]^2,
    Q=C+(q-1)P_T.                                         (F)

A sufficient MODEL-specific bridge would require, for each fixed q in(1,2)
and each tolerance delta>0, projections of ranks N_T=o(T^kappa) for which
the modified mean is eventually positive and

    liminf_(T->infinity) T^(-kappa) log E_Q u_C(T,x)
       >= q^(1/(3-alpha)) ell-delta.                        (H)

Here ell>0 must be an independently valid first-mean lower constant. Applying
this to the original sharp target requires its intended source constant;
no correction of the recorded printed normalization discrepancy is adopted.
If(H) held, (F) would give the lower factor2^(1+1/(3-alpha)) by first taking
T to infinity, then delta to zero and q up to2. No q(T)->2 substitution or
uniform q estimate is needed. This is only the missing micro-contract, not
a proof of(H) or the original conjectured sharp constant.

The new counterexample shows why(H) cannot be replaced by the unconditional
instruction 'discard the independent residual and use qP'. It does not rule
out specially chosen projections, a leading-order comparison or a different
model-specific route. The failed deterministic-surrogate mean-shift argument
is a separate recorded shortcut. No Skorohod result is developed here: this
obstruction uses the ordinary Stratonovich self-pair contribution to the mean.
No new general existence, all-order sharpness, novelty or circulation claim.
