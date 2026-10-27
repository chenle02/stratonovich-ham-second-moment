# Upper-bound author v3: degree-one endpoint addition and final freeze

**Status: CANDIDATE, awaiting the next frozen native Opus review.** This author-v3 version adds the natural alpha=1 endpoint in all three dimensions before that review. The author-v2 snapshot is preserved separately; no native review of author v2 was launched. The original d=1 v1 scientific review remains PASS_WITH_NOTES/medium, below the configured high gate, and is not relabeled as covering either extension.

This is the final scope for the next review packet: **0<alpha<=1 in d=1,2,3**, under the source's real, nonnegative, nonnegative-definite homogeneous covariance assumptions. Separate sharper real-space Riesz constants in d=1 remain. The range1<alpha<2-alpha0 in d=2,3 and the sharp second-moment constant remain open. No further scope expansion was undertaken.

## New endpoint argument

The supplied independent memo `work/alpha-one-dimension-extension-audit.md` was read before editing and its normalization was independently checked. New `L:alpha-one-convolution` (Lemma5.4) is fully written in the notes.

For alpha=1, Fourier uniqueness gives spectral degree1 and no atom at zero. Define

    sigma(E)=mu{0<|xi|<=1, xi/|xi| in E},  V=mu(B1).

Then sigma has massV. Dilation gives radial sector massR*sigma(E); subtracting sectors gives mass(r2-r1)*sigma(E) on each polar rectangle. Uniqueness on generating rectangles yields the exact polar product dr*sigma(dtheta), without an angular density assumption. Real covariance symmetry makes mu and sigma even.

Under the Brownian Gaussian convention, covariance and Green smoothing yield exp(-a r²), a=(epsilon+eta)/2>0. Fourier Fubini, polar decomposition and evenness give

    integral G_(h,eta)(dy) gamma_epsilon(y+z)
       = integral sigma(dtheta) I_a(h,theta.z),
    I_a(h,v)=integral_0^infinity exp(-a r²)sin(hr)cos(rv)/r dr.

At fixed smoothing this integral is absolutely convergent. One-dimensional Fourier inversion, with factor1/(2pi), gives

    I_a(h,v)=pi*(g_h*p_(2a)^(1))(v),
    g_h(v)=(1/2)1{|v|<h},
    p_(2a)^(1)(v)=(4pi*a)^(-1/2)exp(-v²/(4a)).

Thus0<=I_a<=pi/2 and the uniform convolution bound is pi*V/2. Both antipodal directions are already included in sigma, so there is no additional factor2. This is an oscillatory endpoint calculation; the divergent alpha=1 absolute Fourier envelope is not used.

## Transfer and constants

`P:low-alpha-upper` (now Proposition5.5; label retained) now covers0<alpha<=1 with

    K_sp^gen = V*2^(2-alpha)*(1-alpha)^(-alpha)/(2-alpha)^(2-alpha), 0<alpha<1,
    K_sp^gen = pi*V,                                             alpha=1.

At the endpoint the closing bound is M=pi*V/2, openings contribute h, and ordinary AM–GM gives M^k product_open h <= (2M)^k t^k/k^k. No weighted formula is applied with a division by1-alpha. All temporal pair-sum symmetry, split factors, factorial relaxation and nonnegative-series summation remain as in the previous candidate. In particular at alpha=1,

    E u²(t,x) <= exp{2 sqrt(2Z pi V) t^((3-alpha0)/2)}.

The detailed eta-first L2 Cauchy argument from author v2 is retained unchanged: fix noise smoothing, use bounded continuous Wick products and weak Green-measure convergence with unchanged masses, then take the noise limit from the source's fixed-order theorem. The endpoint convolution estimate is uniform at both stages.

## Normalization and scope checks

- In d=1, gamma=c_delta delta_0 has mu(dxi)=c_delta dxi/(2pi), so V=c_delta/pi. Hence pi*V/2=c_delta/2 and K_sp^gen=pi*V=c_delta, exactly recovering the direct white bound.
- Evenness is derived from the real covariance, not assumed from positivity of an arbitrary complex-field spectral measure.
- Angular atoms are permitted; all angular mass is in sigma. No isotropy or full-dimensional spectral density is asserted.
- In dimensions2 and3, alpha=1 means degree-one homogeneous covariance, **not** full spatial white noise.
- V=0 is explicitly handled as zero noise, mu=0,u=1. The nontrivial proposition assumes V>0.
- The alpha<1 Fourier constant need not converge to the endpoint value; the endpoint has a separate proof. No parameter-uniform limit of sharp constants is claimed.
- The generalized first-moment calibration applies to the piecewise K_sp^gen as well, with C1=C2/2^((4-alpha)/(3-alpha)); the imported first-moment lower bound again gives the Jensen consistency check.

## Presentation updates and preservation

The abstract, title, candidate box, proposition scope, target-coverage note and upper-route item now consistently say0<alpha<=1 in d=1,2,3, with alpha>1 in d=2,3 open. The original full G:upper goal is unchanged. Every new result remains labelled CANDIDATE.

The existing sharper d=1 Riesz constants and the source-faithful white proof remain. The previously added explicit spatial-noise Tonelli averaging, notation clarification, smoothing pinpoints and softened Skorohod-mild comparison remain. No Skorohod estimate is proved or transferred.

The entire old model/G0/G1 mathematical block still matches checkpoint8358d58, with comparison SHA-256 `aa888a76060f292a4ba5cadf5a9fec5a4d5e1b0084e08a9f184582768c2ec17a`. No Progress, HANDOFF, Lean, sibling, source PDF, bibliography database, Git history or immutable review artifacts were changed.

## Build and final freeze

The owned candidate section was formatted. Complete latexmk build:0 errors,0 undefined references/citations,0 overfull boxes;25 pages. Rendered endpoint and transferred-proof pages21–22 were inspected.

Final TeX SHA-256: `848c545a1c537178509b58f8af20a435f8445855f5f8b95c0e2843aef7c2d55e`.
Final PDF SHA-256: `2c1880fe9201a9b2c72f2e12037edd7698122db37dca79af942b0440aae31bc4`.

## Honesty and review requirements

No defect is known after the independent endpoint audit and writer verification. Fresh cross-family review must still check the polar measure normalization, evenness, Gaussian Fourier inversion factor, absence of a second antipodal factor, and transfer through the same regularization order. The all-dimension statement is not covered retroactively by the d=1 v1 review. This is not human certification, a Lean result, a sharp-constant claim, an alpha>1 result, or full-goal completion.

STATUS: DONE_WITH_CONCERNS — final author-v3 scope and source frozen for the next native review packet; no further edits planned.
