# Numerical quantities and analytical tail budgets

These are floating consistency checks, not computer-certified enclosures
or a measurement of the full localized operator norm. The core uses unit
Lebesgue spectral density; the actual operator constants also contain the
fixed covariance amplitude and the prior1/(2pi)Fourier factor.

For the convolution, a positive Feynman parameter identity gives
D(q)=integral_0^1 du/[sqrt(u(1-u))sqrt(1+u(1-u)q^2)]. To verify it, use
1/sqrt(AB)=pi^(-1)integral_0^1 du/[sqrt(u(1-u))(uA+(1-u)B)], proved by
u=sin^2(theta) and tan(theta). Complete the k square and integrate its
Cauchy kernel. Substituting u=(1+cos(theta))/2 yields
D(q)=2integral_0^(pi/2)(1+(q^2/4)sin^2(theta))^(-1/2)dtheta,
so the numerical evaluator2ellipk(-q^2/4) has exactly the convention used
by mpmath. Six cases compare it with an independent positive k quadrature.

The positive white trace I_a(h)=8integral_0^h(h-z)z^-a K0(z)^2dz uses the
main proof's L=2K0. After z=h exp(-y/(1-a)), the code integrates y in[0,160].
The actual positive remainder is bounded by

    8h^(2-a)/(1-a) exp(-Y)
      [(c+bY)^2+2b(c+bY)+2b^2],
    c=2.5+log(1/h), b=1/(1-a), Y=160.

This follows from K0(z)<=2.5+log(1/z) for z<=1 and the exact polynomial
exponential tail integral. It is recorded for every case. No small-positive
argument is clipped, and the singular endpoint is retained by the change
of variables.

For an independent spectral/time comparison use
I_a(h)=2h^(1-a)integral_0^infinity D(z/h)J_(a,1)(z)dz.
On[0,32] the code evaluates J by the same lower-incomplete-Gamma formula
checked in the preceding phase-response wave. It follows directly from
integrating(1-v)v^-a exp(izv), with J(0)defined by its continuous limit.
Beyond Q=32, the already-reviewed J error bound gives
J_(a,1)(z)=A z^(a-1)+error, |error|<=B z^(a-2), with the same A,B as before.

For the positive tail integrals set z=Q exp(b y), b=1/(1-a). The leading
tail becomes bQ^(a-1)integral zD(z/h)exp(-y)dy, and the error tail becomes
bQ^(a-1)integral D(z/h)exp(-y)dy. The code integrates[0,160]. From the
main proof's explicit D bound, the omitted leading tail is at most

    24bQ^(a-1)h exp(-Y)[log(2+Q/h)+b(Y+1)],

and the omitted error tail is at most that divided by Q. Combining these
with A and B yields the displayed spectral tail budget. Five cases check
agreement with the positive time integral inside that analytical budget,
allowing only the stated floating-quadrature tolerance. This does not turn
the floating quadratures themselves into rigorous intervals.

The twelve short-time cases record the ratio to h^(2-a)(1+|log h|)^2;
finite ratios are not a proof of a uniform bound. The Gaussian-mixture/time
argument in the main note supplies that bound. Actual runtime version is
recorded as mpmath1.4.1 by the executed script. All computations were local,
with the named numerical service capped at CPU200%,MemoryMax3G,Runtime300s.
