# Fixed-mask Young flow on E plus constant phases

FROZEN STATEMENT TARGET; no new analytic proof or theorem adopted yet.
Full original all-dimensional sharp p2 goal ACTIVE. This phase choice
replaces the UNREVIEWED uniformly-local plan for this FIXED-mask consumer.
It changes neither noise, covariance class, data nor desired moment bound.

Use original H:homog, d=1,2,3; a in(0,1); alpha+a<2;
0<alpha<d or alpha=d=1. Fix R,T>0 and the actual real smooth compact
mask m=zeta_R, 0<=m<=1, supp(m) contained in B_(2R), as in accepted
actual-operator-driver.md and source-operator-convergence.md. Let

 E=H^(1/2)(R^d) x H^(-1/2)(R^d),
 1/2<theta<beta<min(1-a/2,(3-a-alpha)/2).

Named accepted inputs: SAME raw W-measurable masked first driver M_E and
its actual source M_E^rho, converging in every finite Lp Ctheta(B(E)),
uniform Gaussian square-exponential pathnorm moments, compact values, actual
source ordinary first-response identity and physical input/output cutoff
localization. The source is the canonical heat/Laplace-slice construction
retaining given W on an extension. No time convolution or original-noise
quotient mask multiplier is assumed. Fixed-mask-moment-transfer.md F1-F3 is
also a named accepted input; F3 has a still-unproved masked L2-limit premise.

## Y1. A complete separable phase containing the actual initial data

Use the real direct sum F=E directsum R^2, with Hilbert sum norm, embedded
in phase distributions by

       (e,c1,c2) -> e+(c1*1,c2*1).

The embedding is injective and continuous into distributions. Neither
nonzero constant belongs to its global Sobolev entry; prove this, rather
than appeal to a finite-box example. Write i:E->F for the isometric
embedding and e0=(0,1,0) for distributional data(1,0).
The massless wave group acts by

 S_F(t)(e,c1,c2)=(S_E(t)e,c1+t*c2,c2).

It is strongly continuous and bounded on finite time horizons, with the
actual full-phase finite propagation on these distributions. No norm
continuity of S_E or S_F is asserted. Global E is a closed proper subspace,
NOT dense in F. No uniformly-local completion or fake periodic state space.

## Y2. Actual cutoff extension, constant columns, source convergence

Choose real chi smooth compact, equal1 on B_(2R+T+1), supported within
B_(2R+T+2). Accepted physical localization gives

 Dchi M_E(t)=M_E(t)=M_E(t)Dchi

and the same for every M_E^rho. Dchi acts diagonally on distributions.
Take psi smooth compact equal1 on a neighborhood of supp chi. Then
Lpsi:F->E, Lpsi(e,c1,c2)=psi*e+(c1*psi,c2*psi), is bounded. Define

       A_E(t)=M_E(t)Lpsi in B(F,E), A(t)=i A_E(t) in B(F),
       A_E^rho(t)=M_E^rho(t)Lpsi, A^rho=i A_E^rho.

These definitions are independent of psi with that neighborhood property,
extend M_E on iE, and have compact values with range in iE. They retain
the TWO actual constant-response columns; no extension-by-density is used.
For all finite p>=1,

 A_E^rho -> A_E in Lp Ctheta([0,T];B(F,E)),
 ||A_E||_Ctheta, ||A_E^rho||_Ctheta have uniform small square-exponential
 moments (one positive constant depending on fixed R,T and exponents).

Raw A is W-measurable. For each fixed rho, A_E^rho agrees indistinguishably
with the actual source statewise first-response integral on F, taking its
values in E:

 int_0^t S_E(-r) B(mY_rho(r)) S_F(r)dr.

Here B(b)(e,c1,c2)=(0,b(e_1+c1)) is regarded as a bounded F->E map for
smooth compact b; the notation S_E(-r) applies after B. Justify this
identity on constants directly using finite propagation, not dense E.
Per-fixed-rho versions suffice; no uncountable common exception set.

## Y3. Young evolution and all-finite-Lp source flow convergence

Import the ALREADY SOURCE-CHECKED Banach Young estimate and elementary
linear contraction argument in local-causal-young-flow.md Section5; its
generic Banach-algebra argument does not require d1, HS structure or the
old noise-multiplier lemma. Equivalently use the supplied held Friz--Hairer
Sections1.4-1.5/4.1 estimate(4.3) with ordinary left composition. Do not
invoke the analytic-semigroup Theorem12.18 for this wave group.

For each actual driver A in Y2, let U_A(t,s)=I+int_s^t dA(r) U_A(r,s).
There is a unique global interaction evolution, with the composition law,
and bounds at fixed T

 sup_(s<=t<=T)||U_A(t,s)|| <= C exp(C(1+||A||_Ctheta)^(1/theta)).

The solution map is locally Lipschitz in the driver Ctheta norm into the
uniform norm on the time triangle. The increment U_A(t,s)-I has range in
iE and preserves both constant coordinates in the INTERACTION phase.
With the actual raw/source drivers, for every finite p,

 E sup_(s<=t<=T)||U_(A^rho)(t,s)-U_A(t,s)||_B(F)^p ->0.

Uniform all-finite moments of the individual evolution sup norms hold,
by the Gaussian square-exponential driver bounds and 1/theta<2. Strong
measurability/separable path versions must be justified; no unjustified
operator-valued Radon--Nikodym property is used. Do not replace Ctheta
convergence by testwise or mere uniform driver convergence.

## Y4. Physical source identity and the actual masked raw average

P_A(t,s)=S_F(t)U_A(t,s)S_F(-s) is a strongly continuous physical evolution;
source physical differences converge in the same all-finite-Lp uniform
operator-difference norm. This does NOT claim norm continuity of the
individual physical operator paths. For each fixed rho and initial e0,
P_(A^rho)(t,0)e0 is the actual ordinary wave phase for coefficient mY_rho,
and its displacement equals u_rho^m of accepted F2.

Prove the source strong Duhamel/Young identity rather than assume it from
linearity: B(mY_rho) is F->E bounded, statewise strong continuity suffices,
and Young Riemann sums must converge to the strong integral on states.
The ordinary source phase minus the free constant phase lies in E; no
boundedness of an unmasked Gaussian field over all space is needed.

For real phi>=0 smooth compact with integral1, define the bounded functional

 J_phi(e,c1,c2)=<e_1,phi>+c1,
 A_m(t,phi)=J_phi P_A(t,0)e0.

Then int phi u_rho^m(t,.) -> A_m(t,phi) in every finite Lp, in particular L2,
on the retaining space, at arbitrary relative source cutoff rates, fixed
R,T. This raw variable is W-measurable and closes the exact premise of
accepted F3, so

                  E|A_m(t,phi)|^2 <= E|u(t,0)|^2.

There is no point Sobolev evaluation or masked pathwise sample order.

## Optional compact deterministic base, same consumer

For deterministic h(t,x) continuous in time with spatially smooth values
and support in one fixed compact set, its actual statewise first-response
primitive A_h is Lipschitz in B(F), with constants depending on support
and sup_t(||h(t)||_W1infinity+||h(t)||_L2). The same flow/source conclusions
hold for A_h+gA and A_h+gA^rho at any fixed scalar g, uniformly for bounded
g and bounded displayed h norms (individual bounds, not a claim of an
uncountable coupled family). Only h=0,g=1 is used for F3 above. This does
not identify a raw Cameron shift, optimize its cost or prove block growth.

## Boundaries

Fixed physical mask/horizon only; no full-line stationary operator or
uniform growing-R bound. Phase choice still includes every global E input
and both constants needed by the original initial datum and full-phase
cone; it does not change the actual masked source PDE. Different-phase
ground projections/complement estimates must be re-proved before reusing
the abstract moving-block cone. No new ground state at all d3 strengths,
raw shifted event/cost, all-dimensional lower rate, sharp upper constant,
author-energy normalization, exact limit, Lean/package/companion/HPC,
contact, source repair, TeX/PDF/wiki or publication claim. No independent
operator-Young method novelty; this is a concrete application bridge.
