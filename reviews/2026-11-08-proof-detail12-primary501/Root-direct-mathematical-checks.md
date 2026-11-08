# Direct checks of the current proof-detail questions

These are Root checks of the frozen candidate, not an independent review or a new accepted manuscript theorem. The complete mathematical review remains open.

## First pairing, spatial white covariance

For d=1, Gamma=delta_0, G_r(dz)=1_{|z|<r} dz/2. Before any temporal weight, the single self-pair on a two-vertex chain gives J(r1,r2)=r1/2: the second increment is forced to zero and the first Green measure has mass r1. One vertex on each chain gives J(r1,r2)=min(r1,r2)/2. Consequently their damped integrals at positive dampings a1,a2 are respectively 1/(2 a1^2 a2) and 1/(2 a1 a2(a1+a2)). At unit damping these are 1/2 and 1/4. Both densities have degree one and their two-gap measures degree three, agreeing with (4-alpha)k=3. No temporal diagonal factor is included in this spatial-measure test.

## Fresh-cross insertion and inventory

In the fixed-split proof, an incoming vector for a new cross color lies in its vacuum, tensored with all previously used colors and background degrees. Background propagators and phase identities act as identity on that unused Gaussian factor. Orthogonality therefore turns the squared insertion norm into the spatial column variance. This does not use the false one-variance bound for a general occupied random operator. Each cross color occurs once per selected word.

The two copies incur metric factors only for background colors used on that copy. A (2,0) or (0,2) singleton therefore has one ending factor, while (1,1) uses the fresh-cross bound. After sigma_i^2 <= c h_i^(-a), the mean singleton powers are beta and beta-1; higher degree l>=2 gives beta*l, beta*l-1 and beta*l-2. They are positive since beta>2. The cross singleton has h_i^(2-a), with 2-a>1, so its sorted inventory sum converges. This validates substituting the upper bound on h_i into each whole weight before summing.

## Covariance amplitude, independently of label scaling

Let kappa_den=3-alpha, Q=4-alpha, b>0 and r=b^(1/kappa_den). Define D_r Psi(s,x)=r^(d+2-alpha) Psi(s,r*x). Spatial Radon homogeneity gives h_(D_r Psi)(s,x)=r^2 h_Psi(s,r*x) and v_(D_r Psi)=r^Q v_Psi. For covariance b*Gamma use Psi_b=b^(-1)D_r Psi. Its actual mean is still r^2 h_Psi(s,r*x), its raw variance is b^(-1)r^Q v_Psi=r*v_Psi, and unit-kinetic Rayleigh scaling gives I_(Psi_b)=r*I_Psi. Thus every label-p score scales by r. This is a bijection on the full nonseparable nonnegative compact smooth test class, so the suprema scale by b^(1/(3-alpha)). No separated-control restriction or change in Gaussian half-action is used.

As a separate model check, each order-2n paired coefficient scales by b^n and time homogeneity is t^(beta*n). Therefore the second moment at covariance b*Gamma equals that at Gamma with time b^(1/beta)*t. Interpreting the established candidate limit with exponent beta/(3-alpha) gives the same amplitude exponent. Noise amplitude sigma corresponds to b=sigma^2; zero covariance is treated directly. This is distinct from homogeneity in the moment-score label p.
