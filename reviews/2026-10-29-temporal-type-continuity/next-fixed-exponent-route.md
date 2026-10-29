# Next bounded research: fixed-positive-time-exponent two-clock route

The full original G:sharp is still open. The new scalar interpolation/constant
calibration is reviewed;the scalar-shape obstruction shows that it alone
cannot identify the positive-a sharp curve. Stop adding scalar corollaries
as a substitute. Next inspect the MODEL information retained by two chains.

## Exact source and scope

Use current64page author PDF,not arXivv1:Theorem6.1andRemark6.3,printed
roughlypp37--42 (locate exact statement/page before quoting). Standing fact:
one-chain monotone order drives the source representation;each p2chain is
still ordered,but their interleaving is not. Preserve ALLStratonovich
self-pairings and unequal/empty splits. No Skorohod result or sibling edit.

The target is a fixed-total-order transform/inequality retaining two clocks,
then a coefficient asymptotic feeding the actual p2rate. Ordinary full-moment
time Laplace transforms are not finite:the proved positive superlinear
growth lower bound dominates exp(theta*T) for every fixedtheta>0. Work at
FIXED degree before any series/resummation. Do not identify double external-
horizon Laplace damping with the Laplace transform of the diagonal T1=T2.

## Lowest-order calibration to derive/test first

Unreviewed workpad formulas below are explicit checks to VERIFY at the next
step,not an adopted new representation. Spatial white d=alpha=1,G=indicator/2,
raw temporal covariance |s-t|^-a,0<a<1.

For the(1,1)cross pair,the spatial factor is min(s,t)/2. Its GAP-damping
transform should be
K_cross(theta1,theta2)
 = Gamma(1-a)/(2*(theta1+theta2)^2)
   *(theta1^(a-1)+theta2^(a-1)), theta1,theta2>0.
Check by splitting s=t+v or t=s+v:
each term factors integral t*exp[-(theta1+theta2)t]dt
times integral exp[-theta_i*v]*v^-a dv,then factor1/2.
At theta1=theta2=theta this is Gamma(1-a)/(4theta^(3-a)).
At a=0it must recover1/[2theta1theta2(theta1+theta2)],
the already checked static cross transform. For the DOUBLEEXTERNALhorizon
transform there is an additional1/(theta1theta2),not the same object.

For the empty+length2self pair,the spatial gap factor is r1/2and time
difference r2. Independent-gap damping should give
K_self(rho1,rho2)=Gamma(1-a)/(2rho1^2*rho2^(1-a)).
Common-gap damping at theta gives Gamma(1-a)/(2theta^(3-a)).
One external-horizon Laplace transform adds1/theta;inversion recovers the
known mean coefficient1/[2(1-a)(2-a)(3-a)]*T^(3-a).
The single-horizon diagonal X1squared coefficient is
1/[(1-a)(2-a)(3-a)]*T^(3-a);do not confuse it with settingtheta1=theta2
in the double-horizon transform.

Any proposed two-clock formula must reproduce both cases,full theta symmetry,
homogeneous degreea-3and the static endpoint. Test before large proof
investment. A failed pure-product guess only refutes that named guess;
record exact parameter/small-order witness.

## After the calibration

Read the actual source6.1proof and identify exactly where one-chain order
turns |s_j-s_h|into ordered increments. State a two-chain candidate with
explicit joint clock/relative-order constraint;do not erase it by unproved
independence. Freeze claims/source crosswalk and get skeptical review before
long variational/LDP work. Original full covariance/dimension target remains;
white noise is a falsification case,not a replacement objective.

Positive-series type already identifies the ACTUAL upper growth limsup with
nu*limsup[(k!)^nu*c_2k(a)]^(1/(nu*k)). To obtain a time-liminf sharp lower
constant,an eventual coefficient lower envelope or comparable order control
must be proved;do not infer it from a root limsup. Agent8's existing
series_saddle_lower may later consume such a REAL lower-envelope hypothesis;
it cannot supply the SPDE input. Lean remains L0/PROPOSED until creation approval.
