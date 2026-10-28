# Local rejection of an isotropic heat-Mellin-square endpoint recipe

Status: UNREVIEWED deterministic falsification screen,not part of the main
54page proof/report. It rejects only the recipe below,not H9 or the target
upper bound. No accepted no-go or novelty claim is made.

A tempting universal recipe,with F_s=p_s*Gamma,would define a static endpoint
density by int_0^infinity s^{(2alpha-beta)/2-1} F_s(x)^2 ds. Its formal
homogeneity is beta and its positive mixtures would preserve positive
definiteness. Local finiteness is an indispensable additional condition.

Take the ordinary admissible d3 product
 Gamma(x)=|x1|^(-9/10)|x2|^(-1/5),constant in x3,
 alpha=11/10,alpha0=1/4,theta=7/8,beta=9/5.
All source thresholds and the H9parameter interval hold. This target already
has valid coordinate-product endpoints;the new recipe is a different route.

For0<s<1/16 and |x1|<=sqrt(s),Gaussian integration over
y1 in[sqrt(s),2sqrt(s)] gives
 (p_s^(1)*|.|^-9/10)(x1)>=C s^(-9/20).
For x2 in[1/2,1],the other Gaussian convolution has a uniform positive lower
bound,by integrating y2 near x2. The third factor is1. Integrating F_s² on
the fixed box B=[-1,1]x[1/2,1]x[-1,1],using the shrinking x1strip,gives
 int_B F_s(x)^2 dx >= C s^(1/2-9/10)=C s^(-2/5).

The Mellin weight is s^(-4/5). Positive Tonelli therefore yields
 int_B int_0^infinity s^(-4/5)F_s(x)^2 ds dx
   >= C int_0^(1/16) s^(-6/5) ds =infinity.
Thus the recipe is not a locally finite Radon covariance for this valid
input. The exact exponent/parameter control is in the JSON.

Total homogeneity and centered Gaussian variance are not enough to certify
this nonlinear construction;coordinate singularities matter. A possible
repair requires an actually locally finite endpoint construction and the
full Gaussian comparison,for example with justified anisotropic regularization.
Neither is supplied here. This does not question the manuscript's linear-map
closure:that proof convolves already admissible endpoints and never constructs
a new covariance by this Mellin-square formula. No Skorohod result is developed.
