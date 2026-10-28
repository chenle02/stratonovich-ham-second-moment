# General covariance recon: what the real-parameter theory supplies

Status: new scoped source audit and deterministic approximation screen;
independent review pending. No full moment theorem or covariance-cone
non-density theorem is claimed. Original arbitrary-covariance goal unchanged.

## Exact source boundary

Rubin, arXiv0704.0061v2 (2007-05-03), source SHA256 in source-map.json;
published Adv.Math218(2008), DOI10.1016/j.aim.2008.01.011. All labels below
refer to this arXiv version; journal numbering is unverified.

From Rubin Theorem4.1,pp19-20, for n3 and 0<lambda<3, an even angular
DISTRIBUTION f has positive-definite homogeneous extension
iff M^{lambda-2}f is a nonnegative angular measure, equivalently
f=M^{1-lambda}mu with mu>=0. For our normalization use the polar extension H_{-lambda}f,defined by
int_0^infty r^{2-lambda}<f,phi(r dot)>dr,with probability angular area
sigma=dOmega/(4pi). Thus H_{-lambda}(f sigma) has ordinary density
|x|^{-lambda}f(x/|x|)/(4pi). The usual pointwise homogeneous extension
of a scalar f differs by the positive factor4pi. We import only the source
POSITIVITY characterization,which is invariant under that scalar;we do not
borrow an unexamined Fourier normalization from its p18 extension notation. This is an angular analytic-transform representation,
not a positive ellipsoid mixture.

From Definition5.7 and Theorem5.8,pp24-25, the real-lambda intersection
body class is the radial-uniform closure of lambda-intersection bodies of
STAR BODIES, defined via that same analytic transform. It is not stated as
an ellipsoid-sum characterization. The star-body radial functions are
continuous and strictly positive; a singular angular covariance measure is
not such a radial function. Example6.3,pp28-29, gives a sufficient positive
dual-Radon construction,not the converse for every Fourier-positive object.
This audit does not assert that a majorant theorem is globally impossible.

## First falsification: analytic continuation is not a positive raw kernel

Rubin(2.9)-(2.10),p8, defines M^a by an ordinary cosine-kernel integral
initially at Re(a)>0. It is continued by its spherical-harmonic multipliers
(3.4),p10. For lambda in(1,2),a=1-lambda<0, so the integral formula cannot
be used as an ordinary positive mixture. Already at mu=sigma,the cutoff
of the unnormalized purported positive kernel is

 J_lambda(delta)=int_{|u dot e3|>delta}|u dot e3|^{-lambda}sigma(du)
               =int_delta^1 v^{-lambda}dv
               =(delta^{1-lambda}-1)/(lambda-1) -> infinity.

This uses the uniform[-1,1] normal-coordinate marginal on S2. In contrast,
the degree-zero multiplier in(3.4) is the finite positive number

 M^{1-lambda}1=Gamma(lambda/2)/Gamma((3-lambda)/2).

For lambda3/2 the divergent cutoff is2(delta^{-1/2}-1). The analytic
normalizer itself is negative here; multiplying the divergent positive
integral by it does not define the finite analytically continued operator.
This refutes only that raw-kernel interpretation,even for the isotropic
admissible covariance. It does not refute Rubin's theorem or our target.

## Second falsification: no uniform isotropic Riesz envelope after smoothing

Fix s=1/2, alpha=1+s=3/2 and alpha0=1/4,so alpha+alpha0<2. Consider

 Gamma(dy,dz)=(1/(2pi))|y|^{-s}dy delta0(dz), y in R2,z in R.

It is nonnegative,even,Radon,tempered,and homogeneous as a measure with
Gamma(rA)=r^{3-alpha}Gamma(A). Local radial mass is int_0^R r^{1-s}dr;
rapid decay of a Schwartz test gives temperedness. Positive definiteness:
|y|^{-s}=Gamma(s/2)^{-1}int_0^infty q^{s/2-1}exp(-q|y|²)dq.
Each tangential Gaussian is positive definite. The normal delta sets the
two normal coordinates equal in the quadratic pairing and leaves an
integral over z of the nonnegative tangential Gaussian quadratic form.
Absolute Fubini follows from the same local radial integrability and
Schwartz decay. Thus Gamma is an actual admissible singular covariance.

In polar form Gamma=H_{-alpha}nu,where nu is uniform probability measure
on the equator u(phi)=(cos phi,sin phi,0). Define Rubin's spherical Poisson
regularization(2.1),p7, by

 P_t(theta,u)=(1-t²)/(1-2t theta dot u+t²)^{3/2}, 0<t<1,
 f_t(theta)=int P_t(theta,u)nu(du),  Gamma_t=H_{-alpha}(f_t sigma).

For fixed t, f_t is smooth,even,strictly positive. Here a smooth angular
function is identified with its density against sigma. In ordinary spatial
coordinates Gamma_t has density |x|^{-alpha} f_t(x/|x|)/(4pi).

These approximants REMAIN positive definite. To check this rather than
assume it, put eta=M^{alpha-2}nu, a nonnegative finite measure by the
already-verified positive definiteness and Rubin Theorem4.1. The Poisson
operator has multiplier t^j on harmonics(2.1),while M has scalar multiplier
m_{j,a}(3.4). Therefore they commute on angular distributions, and

 M^{alpha-2}(f_t sigma)=Pi_t eta >=0.

The last inequality follows from the positive bounded Poisson kernel on a
finite measure. Theorem4.1 now gives positive definiteness of Gamma_t.
This argument uses the distributional theorem,not a star-body assumption
on the original singular angular measure. It does not apply an ordinary
cosine integral outside its convergence range.

Normalization and convergence: int P_t(theta,u)sigma(dtheta)=1,by integrating
(1-t²)/2 int_{-1}^1(1-2tv+t²)^{-3/2}dv. Its mass outside any fixed angular
neighborhood of u tends to zero,while it stays positive. Hence f_t sigma
converges weakly to nu as t->1. For a Schwartz phi, the radial integral
h(theta)=int_0^infty r^{2-alpha}phi(r theta)dr is continuous and bounded
by dominated convergence and rapid decay. Thus Gamma_t->Gamma in S'.
All Gamma_t have the same homogeneity and the same finite angular mass1.
In particular their heat pairings at the origin all equal

 <Gamma_t,p1>=(2pi)^{-3/2}int_0^infty r^{2-alpha}exp(-r²/2)dr,

independent of t. Homogeneous spectral scaling then also makes their
spectral unit-ball masses constant: <Gamma_t,p1>=
2^{alpha/2}Gamma(1+alpha/2) mu_t(B1). No inverse-Fourier factor is missing.

Nevertheless their least isotropic Riesz envelope amplitudes diverge.
Set delta=1-t and theta=e1. For |phi|<=delta,

 |theta-t u(phi)|²=delta²+2t(1-cos phi)<=delta²+phi²<=2delta²,
 1-t²>=delta.

Integrating just this equatorial arc,whose nu-mass is delta/pi, gives

 f_t(e1)>=1/(2sqrt(2)pi delta).

If Gamma_t(x)<=C_t|x|^{-alpha} almost everywhere, continuity away from the
origin implies the same bound on the sphere,and therefore

 C_t >= f_t(e1)/(4pi) >= 1/(8sqrt(2)pi²(1-t)) -> infinity.

Thus angular Poisson smoothing followed ONLY by a scalar isotropic Riesz
majorant cannot give a uniform comparison amplitude,even for an admissible
plane example with fixed homogeneity,heat pairing and spectral ball mass.
This is a counterexample to that approximation shortcut,not to a different
endpoint comparison or to the full moment theorem. The plane example has
other known endpoint constructions;their constants are not refuted here.

## Consequence for the actual next research step

Rubin's real-parameter analytic closure is not the missing positive endpoint
majorant, and generic angular regularization plus its angular supremum loses
uniformity. A useful general theorem must control endpoint constants by
more than smooth-approximation existence or an angular L-infinity norm.
No new reference ticket is needed: Rubin is already queued under the exact
published DOI. No source-author contact,Lean creation,source normalization
repair or source-PDF/sibling-repository edit occurred.
