# Actual pre-proof controls and their limits

Executed check-diagnostics-v1.py via local uv/numpy/mpmath. Actual data:
diagnostics-v1.json. No eigenvalue/SPDE moment or computer-certified error.

TEMPORAL: smooth f_n=f_a chi(1/(nt))chi(1/(n(1-t))), n=4,8,16,
chi decreasing smooth1 on[0,1],0 on[2,infinity). These are ACTUAL compact
smooth time tests, increasing and below f_a. Covariance uses the raw
|s-t|^-a kernel. For k_fn, substitute distance=u^(1/(1-a)); for raw
variance integrate the lower time triangle and multiply by2. The resulting
integrands have no original diagonal singularity, with all support factors
retained. Degrees256/512 check twelve cases a=.5/.25,n4/8/16. At degree512:
a=.5 costs .157212106,.237633226,.291210961 below M_a=.381379882;
a=.25 costs .205846743,.341465618,.443810121 below M_a=.667662381.
Masses/costs increase; five k_fn grid values lie between0 and1.
Largest two-degree raw-cost difference is about7.51e-7. This is a measured
consistency difference, NOT an error bound or proof of the general limit.

ACTUAL SPATIAL MODELS: d1 white alpha1,a.5; d2 invariant-direction
Gamma=delta_(x1)tensorLeb_(x2),alpha1,a.5; d2/d3 Riesz densities
Gamma(dx)=|x|^-1.5 dx,a.25. All are original admissible covariances.
For real normalized Gaussian g_sigma=(pi sigma²)^(-d/4)e^(-|x|²/(2sigma²)),
b=d/(2sigma²). Its density autocorrelation is the probability Gaussian
p_(sigma²). Thus A_white=A_invariant=1/(sqrt(2pi)sigma), while Riesz
A=(2sigma²)^(-alpha/2)Gamma_E((d-alpha)/2)/Gamma_E(d/2).
The latter follows by polar integration of the ACTUAL physical covariance
measure, sphere area2pi^(d/2)/Gamma_E(d/2), and Gaussian substitution.
Gaussians are actual H1 profiles, NOT compact controls in C_pos. No smooth
approximation or point theorem is inferred from them. Separately compute
normalized C_c^infinity bump exp(-1/(1-x²)) on[-1,1]: white A=int g^4,
b=int(g')²; d2 invariant product has SAME A and twice b. These supply
two ACTUAL COMPACT smooth spatial models; degrees256/512 agree.

OPTIMIZATION: six spatial models,50/80working decimal digits. Exact
feasible parameters theta,ell,L from the target are evaluated, with
radicand=L² and payoff matching k[(R/M_a)alpha^(alpha/2)/(8q^(q/2))]^(1/k).
The separate spatial energy maximum with gradient coefficient1/2 matches
the stated R-to-energy map. These are numerical/algebra consistency checks,
not eigenvalue bounds or an all-parameter theorem. No Gamma amplitude or
Fourier factor is silently normalized away.

PHYSICAL CONTINUITY: nine Gaussian H1 controls in white/invariant/Riesz
alpha>1 models compare the actual covariance norm of squared-profile
differences and H1 distances at widths1 and1+eps,eps.1/.01/.001. The
actual cross integral is the corresponding Gaussian convolution at variance
(sigma²+tau²)/2. Covariance CS holds and both differences tend down0 in
these controls. This does NOT establish full H1 density/continuity or
identify an abstract completion with the physical integral in general.

NEGATIVE controls reject: using Gaussian-test cost degree4-alpha in place
of occupation degreealpha; dropping the kinetic half factor; using the
standard fBm derivative covariance factor (1-a/2)(1-a) instead of raw1.
All are separated from equality by>.01 in tested models. These diagnose
normalizations only. No full stochastic lower or source constant computed.

Gate verdict: no falsification of B1-B5 found in these controls; proceed to
INDEPENDENT STATEMENT gate, not a long proof or theorem adoption. Critical
remaining analytic obligation is the physical four-linear H1 bound/density.
No Fatou-only equality, d1 density split or global H1 supremum embedding.
