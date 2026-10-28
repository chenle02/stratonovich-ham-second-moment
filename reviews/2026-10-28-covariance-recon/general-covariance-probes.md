# Full-class covariance controls for the remaining d3 question

Status: local deterministic deductions,UNREVIEWED;may be classical existing
inputs and require source recon before any novelty claim. Not part of the
frozen54page proof or its17check report. These do NOT give an all-order
moment theorem or rehabilitate the uniform-per-pairing G0 route.

Assume d=3,0<alpha<2,and a nonnegative even positive-definite homogeneous
tempered covariance Gamma,with positive spectral measure mu and V=mu(B1).
Let Gamma_epsilon=p_epsilon*Gamma in the source Brownian Gaussian convention.
Zero covariance is trivial. Spectral scaling gives mu(B_R)=V R^alpha.

Falsification/calibration first: for Gamma=c dy delta0(dz),alpha1,the
spectral mass is c/pi. Its ball mass at a plane point is pi*c*r² and its
wave normal marginal is(1/2)1_|z|<h. For isotropic c/|x| atalpha1,V=2c/pi.
The two-free-wave convolution at0 is respectively(c/2)min(a,b) and
c min(a,b). Both are below the coarse bound in(3)below. These are exact
normalization controls,not numerical proof or new asymptotics.

## 1. Uniform translated-ball bound

Gaussian smoothing of Gamma is a bounded positive-definite covariance,so
0<=Gamma_(r²)(z)<=Gamma_(r²)(0). By spectral scaling and radial integration,

  Gamma_(r²)(0)=2^(alpha/2)GammaEuler(1+alpha/2)V*r^(-alpha).

On B(z,r),p_(r²)(z-y)>=(2pi)^(-3/2)exp(-1/2)r^(-3). Consequently

  Gamma(B(z,r)) <= M r^(3-alpha),
  M=(2pi)^(3/2)exp(1/2)2^(alpha/2)GammaEuler(1+alpha/2)V.

This is uniform in z,r>0. It uses the physical Gamma mass and the SPECTRAL
V with their explicit Gaussian conversion;they are not identified. No point
atoms are possible. Gaussian covariance smoothing preserves the same bound
by averaging translated balls.

## 2. Time-integrated single-wave closing

In d3,the positive measure integral of G_s for0<s<h has density
K_h(y)=(4pi|y|)^(-1)1_{|y|<h}. This follows directly from
G_s=(4pi s)^(-1)sphere_surface_s and spherical coordinates. Layer cake gives

  integral_|y-z|<h |y-z|^(-1) Gamma(dy)
    = h^(-1) Gamma(B(z,h))
      +integral_0^h Gamma(B(z,r))r^(-2)dr
    <= M(3-alpha)/(2-alpha) h^(2-alpha).

Thus sup_z(K_h*Gamma)(z)<=M(3-alpha)/(4pi(2-alpha))*h^(2-alpha).
The same bound holds after any covariance/Green Gaussian smoothing,by
Tonelli and positive probability averaging. The integral near0 is finite
because3-alpha>1. This is a time-integrated bound,not a bound on each G_h.

## 3. Two FREE wave increments against one covariance

For epsilon>0 and eta1,eta2>=0,Fourier Fubini followed by Cauchy--Schwarz gives

  0<=(G_(a,eta1)*G_(b,eta2)*Gamma_epsilon)(z)
    <= [integral min(a²,|xi|^-2)mu(dxi)]^(1/2)
       [integral min(b²,|xi|^-2)mu(dxi)]^(1/2)
    = [2V/(2-alpha)](ab)^(1-alpha/2).

Indeed |hatG_a|<=min(a,|xi|^-1),the smoothing multipliers have absolute
value<=1,and radial spectral integration gives

  integral min(a²,|xi|^-2)mu(dxi)
    =V a^(2-alpha)+alpha*V/(2-alpha)*a^(2-alpha)
    =2V/(2-alpha)*a^(2-alpha).

The Gaussian weight justifies Fubini at positive epsilon;the unweighted
Cauchy majorant is integrable foralpha<2,so the bound is uniform in widths
and translations. No isotropy or angular density is needed.

## Consumer boundary

(2)has already integrated a time gap,and(3)needs two independent spatial
increments with NO other remaining factors involving either one. A generic
pairing diagram can leave a remote covariance on one increment. Neither bound
permits removing that weight or summing as if all pairings had two free leaves.
Temporal weights and the all-order factorial budget remain the actual problem.
Compare these elementary bounds with the pinned source LemmaA.1 and known
Dalang/BNZ inputs before treating them as a new route. No Skorohod work is
developed. The new queued geometry references do not by themselves discharge
a general endpoint representation or a uniform approximation bound.
