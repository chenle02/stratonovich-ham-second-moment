# Frozen target: joint Gaussian tilt of the actual local flow

Status: PROPOSED, NOT REVIEWED OR PROVED. This is a statement/falsification
checkpoint, not a new accepted proof round. Base scientific input is
notes/local-causal-young-flow.md at d020a2a (adopted b0d233c).
Workflow authority: Progress.md. The original full sharp goal stays active.

## Objects and quantifiers

Fix d=1, 0<a<1 and the original nonzero homogeneous spatial Radon covariance
Gamma, with 0<alpha<=1 and alpha+a<2. Work with the raw time covariance
|t-s|^-a, with no fractional-Brownian multiplicative normalization.
Let psi be a real C_c^infinity((0,1) x R) test, extended smoothly by zero.
Put Z=W(psi) and v=E Z^2. The centered Gaussian family W is the SAME family
used to construct the raw masked interaction driver. No assertion that the
source cutoffs are measurable from W alone is needed or proposed.

For 0<delta<=1 use fast time u in [0,L], L=1/delta, and mask radius
r_delta=c/delta, with c large enough to protect the terminal observation's
backward cone. This r_delta is the MASK radius, not the physical rescaling
R=T delta from notes/direct-event-calibration.md. Fix a nonnegative unit-mass
compact smooth spatial test phi and the accepted local phase F. Define

    W^delta(u,x)=delta^(a/2) W(delta u,x),
    g_delta=delta^((1-a)/2),
    A_delta(u)=g_delta integral_0^u
        S(-q) B(zeta_rdelta W^delta(dq)) S(q).

This is an identity of the distributionally defined Gaussian first driver,
not a pointwise evaluation of a generalized noise. It is built from the
accepted finite set of localized HS paths on this fixed finite horizon.
Choose 1/2<theta<1-a/2 and a separable little-Holder version (or explicitly
construct a separable closed support using a strictly larger Holder exponent).
Do not assume the full B(F) Holder space is separable.

Let Y_delta(A) be the phi average of the displacement of
S(L) U_A(L,0)(1,0), and let J_delta(A)=|Y_delta(A)|^2. These are defined via
the accepted bounded functional and Young map on the actual admissible path
space; they are not raw point evaluations. The noise-only canonical average
identification is the prior accepted input, not a new nonzero-profile source
limit assertion.

## Exact deterministic profile and proposed identity

Define the raw covariance profile by distributional convolution:

    h(t,x)= integral ds |t-s|^-a integral Gamma(x-dy) psi(s,y).

The required covariance primitive is

    C_delta(u)=Cov(A_delta(u),Z),
    C_delta(u)/sqrt(delta)
       = integral_0^u S(-q) B(zeta_rdelta h(delta q,.)) S(q) dq.

The amplitude cancellation required here is
(1-a)/2+a/2-1/2=0. Time integration and the meaning of W^delta(dq) must be
checked against the accepted distributional-driver convention; an extra
Jacobian cannot be inserted after this equality by interpreting W as dB.
The proposed tilt is, for every nonnegative Borel functional J on the
constructed driver space,

    E J(A_delta)
      = E[exp(-Z/sqrt(delta)-v/(2delta))
            J(A_delta+C_delta/sqrt(delta))].                 (T)

In particular choose J=J_delta. The shifted Young evolution is the actual
retained-residual flow driven by g_delta zeta_rdelta W^delta plus the
physical deterministic profile zeta_rdelta h(delta u,x). No independent
residual, projection model, covariance order or residual discard is involved.
No positivity of the displacement or its average is assumed.

## Obligations before acceptance

1. Verify joint centered Gaussianity of Z and a countable determining set
   of LOCALIZED HS driver coordinates at rational times, including the
   actual common Gaussian closure; covariance contraction alone does not
   identify the joint coupling.
2. Establish (T) for finite coordinate cylinders without requiring an
   invertible covariance matrix. Extend equality of probability laws on
   the countable coordinate product, then transfer through a measurable
   reconstruction of the actual separable driver version. Handle exceptional
   reconstruction sets under the equivalent tilted probability, rather than
   simply assuming that translation preserves an arbitrary version's null set.
3. Identify the deterministic covariance primitive on that support. Establish
   its admissible path membership and the measurability of the assembled
   B(F) driver and J_delta through the finite compatible HS construction.
   Young continuity on bounded sets suffices only after these domains are fixed.
4. Prove h is strongly time measurable in C_b^1, uniformly W1infinity bounded
   on [0,1], with uniform C1 spatial tails to zero. In d1 Riesz, derivatives
   should be placed on the compact smooth test and the spatial |x|^-alpha
   tail retained; for white space use the spatial delta covariance directly.
   The temporal singularity is locally integrable, not bounded pointwise.
   The mask preserves admissibility and its derivative is uniformly controlled
   for r_delta>=1. No uniform-in-delta full-horizon evolution bound is claimed.
5. Check the block profile is zeta_rdelta h(m delta+delta u,x), with phase
   (V,delta V_t), including the last fractional block. Preserve the existing
   canonical noise-only average-to-original-point moment inequality.

## Falsification and formal boundary

check_contract.py uses exact rational exponents of the Gaussian MGF in four
scalar joint-normal cases: fully correlated, residual variance, independent
and constant observable. It checks sign and half-cost; a wrong plus density
is detected only when observable and tilt correlate. Independence and constant
observables are expressly NOT valid sign controls. All four cases reject a
wrong full-variance cost. Three interior a values check the amplitude power.
These finite probes are not a proof of (T) or an analytic/type review.

Lean triage: the two stable finite seams are the universal polynomial
MGF-exponent cancellation and the real-power amplitude cancellation for
delta>0. Search/reuse existing local algebra before adding declarations.
No Gaussian measure, measurability, profile/Young flow or spectral statement
is covered by those algebraic seams. No companion/package is authorized here.

## Next gate and exclusions

Obtain independent statement fidelity review against the exact prior local
flow and scaling inputs before investing in the proof. Then prove the above
consumer, freeze a source packet, and obtain the mandated Opus5.5/HIGH
analytic/type/application review. A quota/transport error is not a review.

After (T), spectral cone/product growth remains the next substantive gap.
There is no claimed event rate, 2 Lambda(h)-v/2 bound, sharp constant,
higher-dimensional extension, source-normalization repair, novelty or
whole-paper/circulation clearance. Canonical TeX/PDF and prior accepted
WHITE13/original9 boundaries are unchanged.
