# Actual C1-C3 controls, endpoint guards and limits

Root executed check-operator-cm-v1.py, data operator-cm-controls-v1.json.
Ordinary floating arithmetic/quadrature, not a rigorous enclosure, full
operator norm, Ctheta path norm, projection tail or compactness certificate.

ACTUAL bounded F rows, not a point trace. Use d1 white Gamma=delta0,
a=.5/.9, fixed smooth square mask=1 on[-2,2], B=1. q=f is a nonnegative
L2-normalized compact smooth bump supported[-.5,.5]. The output E-dual is
w=(0,Lambda f), whose H-1/2 norm is ||f||H1/2, hence it is a legitimate
bounded phase test. Free one-dimensional velocity propagation gives
 cos(v|D|)f(x)=[f(x+v)+f(x-v)]/2.
Input constant columns are e_disp=(0,1,0) and e_vel=(0,0,1); after free
propagation their displacements are1 and v. The ACTUAL raw noise kernel
for column j=0,1 at a local endpoint is therefore
 delta^-1/2 1_(I_m)(s) m_R(x) ((s-s_m)/delta)^j
                                      cos(((s-s_m)/delta)|D|)f(x).
Choose unit raw CM direction Phi=f_a tensor q /sqrt(M_a), using the
ACCEPTED scalar equilibrium identity/mass in the old damped bridge Sec2.
It is a completion direction, not a C_c^infinity time test; no new rough
Gaussian variable construction is inferred. Its actual covariance mean
is q(x)/sqrt(M_a) on[0,1]. Thus the two-point covariance integral reduces
to delta^-1/2/sqrt(M_a) int_(I_m) v^j A_q(v)ds, where
 A_q(v)=int q(x)cos(v|D|)f(x)dx.
The fast mean primitive is sqrt(delta)/sqrt(M_a) int_0^ell v^j A_q(v)dv.
Both evaluators are exercised separately with differing quadrature degrees.
24rows:delta.25/.125/.3, both columns, first and true lastpartial horizons
including0 and1/3. Max absolute discrepancy about3.05e-12, a consistency
difference only. Wrong Jacobian, slow-clock cosine and missing fast-velocity
factor are explicit wrong controls. The physical mask was not commuted
through a free group. Both state and noise functionals are actual F/raw-H
ones; no Sobolev point evaluation or whole operator norm computed.

ACTUAL selected frequency rows. With d1white, take whole-line Gaussian
f_k=g cos(kx), smooth square physical mask m_R. Noise direction
q_k=m_R f_k g /||m_R f_k g||2 is compact smooth and has white H_sp norm1.
Input f_k/||f_k||H1/2 and output dual Lambda g/||g||H1/2 give matrix entry
 ||m_R f_k g||2/(||f_k||H1/2||g||H1/2).
This is a LOWER bound on an operator norm, not its evaluation or an upper.
Five k0/2/8/32/64 entries decrease about.524,.403,.202,.101,.0717. The
whole-line Fourier Gaussian formula is integrated at degrees512/1024;
two-degree H1/2 norm difference about5.16e-14, not certified error. No
periodic replacement. Decay in selected rows alone does NOT prove compactness.

ACTUAL spatial concentration guards. For real unit Gaussian g in white d1,
invariant d2 Gamma=delta_(x1)tensorLeb_(x2), or d2Riesz alpha1.5, let
 f_L(x)=L^(d/2-s)g(Lx). Fourier scaling makes ||f_L||H^s uniformly bounded
for L>=1,s>=0. Physical covariance gives
 ||f_L²||H_sp=L^(alpha/2-2s)sqrt(A_sp(g)).
The exact Gaussian A formulas are those already checked in the static
occupation controls.36cases compare s=alpha/4±.05 and1/2,L2/8/32/128.
Below alpha/4 the product is unbounded; above it these profiles decay.
This rejects dropping the positive Sobolev margin. It proves no full map
bound at the allowed s and asserts no failure of endpoint continuity.
Gaussians here are H1 profiles, not compact noise/state tests.

ACTUAL temporal concentration guard. For smooth nonzero positive f supported
in(0,1), its raw-H-normalized rescaling f_delta(t)=delta^(a/2-1)f(t/delta)
has fixed norm and literal mean
 K*f_delta(delta u)=delta^-a/2 (K*f)(u).
The first-block Lr norm relative to a fixed nonzero base is exactly
 delta^(1/r-a/2). At r=2/a it stays positive while the mean tends to0 at
each fixed positive time; hence no strong-Lr compactness there. For r>2/a
the first-block norm diverges, refuting boundedness.36scale controls record
this. The first-block lower bound tending to0 for r<2/a is NOT a proof of
full-Lr compactness. All scalings are raw covariance, not fBm-normalized.

Trace guard: normalized cell indicators are orthonormal in time L2. Their
covariance Rayleigh sums are C_a N^a ->infinity. Thus positive K has infinite
trace: the raw instantaneous field is NOT a Radon L2 Gaussian, even if K
is compact. This is not a claim that K fails Hilbert-Schmidt for every a;
the Cameron mean map K^1/2 cannot be Hilbert-Schmidt. Twelve trace controls
record the exact formula. Truncated near-diagonal kernels used to approximate
K need NOT be covariance/PSD kernels; they are only deterministic compact
operator approximants in the proposed proof.

Vector guard: time compactness alone is not vector compactness. For white
spatial H_sp infinite dimensional, fixed unit f in H_t and orthonormal q_n,
f tensor q_n have mean-field images (K*f)(t)q_n separated in Lr(H_sp).
The spatial compact map is essential. This is a counter to a weakened
argument, not to C2 which explicitly includes C1.

No C1/C2/C3 theorem or Gaussian concentration/Young product/point upper
from these controls. Proceed only to independent STATEMENT feasibility
and exact-source gate before long proof. Original all-Gamma goal intact.
