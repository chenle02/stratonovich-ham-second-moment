# Author calculation: high-alpha transfer (UNREVIEWED)

Let b=alpha-1 in (0,1), and assume the genuine uniform convolution bound
sup_z (G_h * gamma_epsilon)(z) <= M h^(-b), also uniform in Green smoothing.
Choose p in (1/(1-alpha0),1/b), p'=p/(p-1). This interval is nonempty exactly
when alpha+alpha0<2. Put theta=alpha0*p'<1, a=1-b*p/2 in (1/2,1),
Z_theta=2/((1-theta)(2-theta)), D_a=exp(2)*(exp(1)/a)^(2*a).

For fixed split m+n=2k the existing descending-label invariant gives
S_D <= M^k product_open h_i product_close h_j^(-b).
Opening AMGM gives product_open <= (2t/k)^k. Apply Holder to the JOINT
counting measure on all P_k pairings and Lebesgue time measure on the two
ordered simplexes. H_D=product_close h_j^(-b), T_D=product_pairs |s_i-s_j|^-alpha0.

If there are k1 and k2 closings in the blocks, the Dirichlet formula is
integral H_D^p = Gamma(1-b*p)^k t^((2-b*p)*k) /
[Gamma(1+m-b*p*k1) Gamma(1+n-b*p*k2)]. Empty-chain convention Gamma(1)=1.
Log convexity bounds the denominator below by Gamma(1+a*k)^2.
An explicit elementary lower bound is
Gamma(1+a*k) >= integral_[a*k,a*k+1] x^(a*k) exp(-x) dx
 >= exp(-1)*(a/exp(1))^(a*k)*k^(a*k)
 >= exp(-1)*(a/exp(1))^(a*k)*(k!)^a.
For k>=1 its square is >= D_a^(-k)*(k!)^(2-b*p).
Hence sum_D integral H_D^p <= P_k [Gamma(1-b*p)*D_a]^k
 t^((2-b*p)*k)/(k!)^(2-b*p).

Only after summing pairings, temporal symmetry gives
sum_D integral T_D^p' = P_k [Z_theta*t^(2-theta)]^k/(m!n!)
 <= P_k [Z_theta*t^(2-theta)]^k/(k!)^2.
Combining Holder factors with P_k <= 2^k k! and k^k>=k! yields
sum_D integral S_D*T_D <= [4*M*(Gamma(1-b*p)*D_a)^(1/p)*Z_theta^(1/p')]^k
 t^((3-b-alpha0)*k)/(k!)^(2-b).
There are 2k+1 <=3^k splits. Thus with K equal to three times the bracket,
A_k(t) <= K^k t^((4-alpha-alpha0)*k)/(k!)^(3-alpha).
The existing nonnegative scalar series bound gives
E u^2 <= exp((3-alpha)*K^(1/(3-alpha))*t^kappa).

Review obligations: no illegal separate pairing symmetrization, all split
and closing counts, the two Gamma normalizations, actual convolution input,
regularization and L2/L1 passage inherited from Section5, no assertion that
this input holds for every homogeneous covariance. Constants are crude.
This does not address sharp constants or certify a new result.
