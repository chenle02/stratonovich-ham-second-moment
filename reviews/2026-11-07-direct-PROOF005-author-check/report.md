# Direct AUTHOR check of the spatial Wick-measure construction

Target: frozen candidate PROOF005, main SHA516d6a650bdac7d3da68672f37836afd084b651c39553b43d5135d0512e39d14, complete proofLF1194–1336. Root read the entire statement/proof and preceding construction. This verifies the displayed deductions at their stated hypotheses; it is not an independent-family review, new paper theorem or whole-goal acceptance.

The Fourier–Laplace formula is nonnegative: finite heat-weighted edge measures give the product of resolvents ((1+lambda_l)^2+|eta_l|^2)^(-1). Comparing arbitrary vertex widths to their minimum is valid in this positive transform, not as a pointwise comparison of heat-smoothed physical covariances.

The heat estimate is uniform in translations and positive smoothing width: Fourier absolute value and radial spectral mass mu(B_r)=V r^alpha give (p_t*gamma_b)(x)<=A(t+b)^(-alpha/2)<=A t^(-alpha/2). Nonnegativity comes from the physical covariance. Since alpha<2, all selected singular time gaps are integrable.

For the jth Brownian occupation moment, condition on the last remaining chronological vertex. Given all earlier remaining observations, its independent final Brownian increment bounds its sole pair factor by A times the last remaining gap^(-alpha/2). Remove that vertex and its partner: no other pairing factor uses either endpoint, and the marginal of the remaining observations is Brownian. Iteration selects j distinct right endpoints. Their remaining gaps dominate their original adjacent gaps. Each ordered2j-simplex therefore has the Dirichlet integral Gamma_E(1-alpha/2)^j T^((2-alpha/2)j)/Gamma_E((2-alpha/2)j+1); there are (2j)! orders. The j=1 value agrees with direct integration of the two-time heat bound. No independence of the pair factors is assumed.

The wave-resolvent identity introduces2^(-2k). The two final Brownian horizons introduce a further1/4; the exponential gap weights cancel their endpoint terms, leaving exp(-(h1+h2)/2). At fixed horizons each self-pair is an occupation S_i and each cross-pair is at most sqrt(S1 S2), by spectral Cauchy–Schwarz. Thus the product is bounded by (1+S1)^k(1+S2)^k. Only these two auxiliary Brownian paths are independent. Expanding each factor gives a finite polynomial M_k(h). In its horizon integral,

 integral_0^infinity exp(-h/2) h^((2-alpha/2)j) dh
   = 2^((2-alpha/2)j+1) Gamma_E((2-alpha/2)j+1).

The Gamma denominator cancels exactly. In particular the expanded base is2^(2-alpha/2) A Gamma_E(1-alpha/2), not2^(2-alpha). The resulting bound is finite for every fixed k, including an empty chain. No uniform-in-k growth estimate is needed for this fixed-order lemma.

Monotone convergence of the positive transforms gives an integrable zero-parameter limit F0. Dominated convergence by F0 gives continuity at lambda=0. Under y_l=exp(-r_l), bounded masses have compact-cube cluster limits; integer monomial moments determine them by polynomial density. For c>0, integral(product y_l^c)=L_D(c,...,c). Letting c decrease to zero and using continuity at zero excludes every y-zero face. Portmanteau on closed neighborhoods controls the approximating mass there, so no mass escapes to infinite r. This proves weak convergence after pulling back, at arbitrary relative width rates.

Sending only lambda_l to infinity in the positive spectral integral gives zero by domination with F0, excluding r_l=0. Wave/heat/time scaling gives rho(cA)=c^((4-alpha)k)rho(A). Positive mass on a compact subset of a horizon face ell_i=T>0 would produce arbitrarily many disjoint dilates within one compact set, each with a common positive mass lower bound, contradicting local finiteness. The finite-horizon region is bounded; its boundary consists of the already null horizon/coordinate faces. A compact cutoff and bounded continuous weighted test therefore pass the weak limit to the asserted horizon integral.

No missing load-bearing step or false inequality was found in this direct AUTHOR check. The result does not certify other foundation claims, the eventual asymptotic limit or the required MAIN/Kimi HIGH gates. Source bytes remain unchanged.
