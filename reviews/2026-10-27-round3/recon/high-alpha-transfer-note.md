# Unreviewed future lead: negative closing powers and a spatial maximum input

This is a root calculation for a later wave, NOT part of the frozen upper
candidate, NOT reviewed, and NOT a claimed extension to alpha>1. The current
candidate must keep its advertised alpha<=1 scope. No Skorohod theorem is
being developed. Check every step independently before relying on this note.

Suppose, in a particular spatial model, the uniform smoothed convolution
bound sup_z integral G_h(dy) gamma_epsilon(y+z) <= M h^(1-alpha)
can actually be proved for 1<alpha<2. Put b=alpha-1. Descending spatial
removal would then give M^k product_open h_i product_close h_j^(-b).
Bound only the opening product by (2t/k)^k.

Choose p,p'>1 conjugate such that bp<1 and alpha0*p'<1. This is possible
exactly when b+alpha0<1, the standing threshold alpha+alpha0<2.
Apply Holder on the JOINT discrete pairing/time integration measure, with
H_D=product_close h_j^(-b) and T_D=product_pair |s_i-s_j|^(-alpha0).
For a split m+n=2k, with k1+k2=k closings in the two chains,

  integral H_D^p = Gamma(1-bp)^k t^((2-bp)k)
    /[Gamma(1+m-bp*k1) Gamma(1+n-bp*k2)].

Log-convexity gives the denominator >= Gamma(1+(2-bp)k/2)^2,
which should be >= C^(-k)(k!)^(2-bp) uniformly in k (Stirling plus
finite-prefix control). The OTHER Holder factor is summed before symmetry:

  sum_D integral_ordered T_D^p'
   = Pk/[m!n!] * [Z_(alpha0*p') t^(2-alpha0*p')]^k.

Use m!n! >= (k!)^2 and Pk <= 2^k k!. The proposed combined bookkeeping is

  M^k (2t/k)^k * C^k Pk
     * t^((2/p-b+2/p'-alpha0)k)/(k!)^(2/p-b+2/p')
   <= C1^k t^((4-alpha-alpha0)k)/(k!)^(3-alpha).

Summing 2k+1 splits changes only the exponential-in-k constant. This would
be a conditional target-scale estimate under the genuine spatial maximum
input, not permission to assume that input for arbitrary homogeneous noise.

Potential concrete spatial case: d=3 isotropic Riesz gamma(x)=c|x|^-alpha.
For r=|z|>0, direct spherical integration suggests

  (G_h*gamma)(z)
   = c[(r+h)^(2-alpha)-|r-h|^(2-alpha)]/[2r(2-alpha)].

Scaling and separate regions r<h/2, h/2<=r<=2h, r>2h give a finite bound
M h^(1-alpha) for each fixed alpha<2. Gaussian smoothing averages this
convolution and would preserve its supremum. This is a possible next
restricted-regime application, not yet checked or written in the notes.

Do NOT extend the maximum input to arbitrary anisotropic homogeneous gamma.
For example delta(x1)|x2|^(-b), independent of x3, has degree1+b and its
spherical convolution can blow up as the slice circle shrinks near a pole.
Even function-valued product covariances can have a tangential singularity.
The low-alpha spectral envelope avoids this issue; the proposed high-alpha
conditional statement does not. All these prospective claims need review.
