# Existing009 Green-limit calculation, made explicit

This is author mathematical working on scientific af97/index7, expanding the existing P:mild-construction calculation. It is not a new theorem, source edit, review, grade or retry of Ar. Bindings below refer to the main TeX:009 statement1347–1362/proof1368–1515;006 proof1114–1198;008 proof1287–1345;002 proof453–509; the scalar finite-moment analogue018 proof2401–2464. Exact hashes are in source-bindings.json.

Assume the actual H:homog model and coupled retaining source family, including any fixed auxiliary coordinates already in that construction. Dimensions are1,2,3, with all original admissible nonnegative even positive-definite homogeneous Radon covariances, original amplitude and data(1,0). No independence between a source Gaussian variable and an occupied polynomial is assumed.

All norms here are in E=L²(Ω), at spatial points or under finite Green integration. They are not global spatial L² norms of constant data, Sobolev point traces or F/radius operator norms.

## Fixed external width and the actual product

Fix T>0 and a=(epsilon,delta)>0. Write H(s,y)=Wa(s,y) and

    Va = gamma_delta^0(0) gamma_(2epsilon)(0) < infinity.

Input008 gives, uniformly in y,0≤s≤T and all positive vertex widths,

    ||X_m(s,y)||E, ||Y_m^b(s,y)||E ≤ q_m(T),
    q_m(T)=exp(theta0 T) C^(m/2) T^m/sqrt(m!),
    sum_(m≥0) sqrt(m+1) q_m(T) < infinity.                 (1)

Constants are for the fixed covariance; the displayed estimates are finite-horizon ones. The m=0 object is1, bounded by q0(T).

For centered linear Gaussian H and R in the closed total-degree≤m Gaussian polynomial space, the existing occupied bound is

    ||HR||E ≤ 2 sqrt(m+1) ||H||E ||R||E.                  (2)

Normalized Hermite multiplication is creation plus annihilation, with norms at most sqrt(m+1) and sqrt(m); sum their bounds, retaining lower contractions. Finite-coordinate approximation extends this to the degree-closed space. An a.s. subsequence identifies the product limit with the actual product. If H=0 no division is needed. This proof allows R to depend on H.

The positive-width Y_m^b are spatially E-continuous: their bounded continuous smoothed Gaussian covariance products and finite Green masses give dominated convergence of mixed second moments. Coupled spatial stationarity gives

    ||Y_m^b(s,y)-X_m(s,y)||E
      = ||Y_m^b(s,0)-X_m(s,0)||E.

Thus006's fixed-order limit is spatially uniform at each fixed s. Consequently X_m(s,·) is E-continuous; (1) gives the same for u=sum_m X_m.

Applying (2) twice yields

    ||H_y R_y-H_y' R_y'||E
    ≤ 2sqrt(m+1) [
        sqrt(Va)||R_y-R_y'||E
        + ||H_y-H_y'||E ||R_y'||E ].                     (3)

Here R=X_m; both R differences remain in the same degree space. The fixed-a field is mean-square continuous, because its finite Gaussian-weighted spatial spectral measure and finite temporal Laplace prefix give continuous covariance. Hence (3) proves continuity of H X_m.

Define the actual products at fixed a. Their global bounds are

    ||Wa X_(n-1)(s,y)||E ≤ M_(n,a)(T)
       :=2sqrt(n) sqrt(Va) q_(n-1)(T),                    (4)
    ||Wa u(s,y)||E ≤ M_a(T)
       :=2sqrt(Va) sum_(m≥0) sqrt(m+1)q_m(T) < infinity.  (5)

This is a bound on sup_y||Wa*u(s,y)||E, not on the E-norm of a spatial supremum.

For (5), do NOT apply (2) directly to the infinite-degree u. The series of products Wa X_m converges in E uniformly in(s,y), by its summable bound. Partial sums of u converge in E; an a.s. subsequence at each parameter identifies the product-series limit with Wa u. Uniform convergence also proves spatial E-continuity of this product.

The maps are jointly strongly measurable in(s,y). At positive widths this follows from the measurable source evaluations and Bochner integration on fixed rescaled time/increment domains. Countable-width E limits give X_m, then the uniformly norm-summable series gives u and the products. A common separable closed E subspace contains these maps: use the fixed external field and a countable source-approximation family, rational parameters and their mean-square closures. Separability of all of L²(Ω) is unnecessary.

Strongly measurable E-valued maps have jointly measurable scalar representatives here: quantize the separable range by countable simple approximations with summable E errors and take their pointwise limit. Each section represents the prescribed E class. For any finite kernel measure, the integrable E-norm bound gives pathwise L¹ integrability by Tonelli and an E-valued integral by Minkowski. Testing with bounded random variables identifies that ordinary random integral with the Bochner integral. This uses the actual kernel measure, including a d3 sphere, not a transfer of Lebesgue-null sets to a singular measure.

## Direct Gaussian averaging of the Green measure

Fix t≤T,x and s<t; put tau=t-s. The positive wave measure G_tau has mass tau, support in the closed ball of radius tau, and

    G_tau = tau (v↦tau v)_#G_1,       G_1(R^d)=1.

For either product in (4)/(5), put F_s(z)=Wa(s,x-z)R(s,x-z), with R=X_(n-1) or u. It is E-continuous in z and globally bounded by the corresponding M. At this step F_s is FIXED as eta varies.

Let p_eta be the Gaussian probability density with covariance eta I. Bochner Fubini is valid since

    integral G_tau(dz) integral p_eta(dw) ||F_s(z+w)||E
       ≤ tau M < infinity.

Consequently,

    integral (p_eta*G_tau)(dz) F_s(z)
       = integral G_tau(dz) integral p_eta(dw) F_s(z+w).  (6)

Let K be the closed ball of radius t+1 and

    omega_(s,x,K)(r)
      = sup { ||F_s(z')-F_s(z)||E :
              z,z' in K, |z-z'|≤r }.

Compact E-continuity implies omega(r)→0 as r↓0. For0<r<1, z in support G_tau and |w|≤r both z,z+w lie in K. Splitting the Gaussian average in (6) gives

    || integral (p_eta*G_tau)F_s - integral G_tau F_s ||E
      ≤ tau [ omega_(s,x,K)(r) + 2M P(|Z_eta|>r) ]
      ≤ tau [ omega_(s,x,K)(r) + 2M min(1,d eta/r²) ].    (7)

Z_eta denotes the deterministic Gaussian averaging law, not resampling of the noise. First eta↓0 at fixed r, then r↓0 proves the E limit for each s. The direct bound on the left is also2tau M, for every eta.

Time measurability follows explicitly by writing (6) as

    tau integral G_1(dv) integral p_1(dz)
             F_s(tau v+sqrt(eta)z).

The maps are jointly strongly measurable, and their norms are bounded by tau M. Set G_0=0 at s=t. Dominated Bochner integration, using2(t-s)M, yields

    integral_0^t ds integral(p_eta*G_(t-s))F_s
      → integral_0^t ds integral G_(t-s)F_s in E.         (8)

No time-uniform modulus is needed: pointwise-in-s convergence and the integrable bound suffice. No bound uniform in a is claimed or needed. The Green limit precedes noise removal.

## Inner vertices, external widths and the full mild product

At fixed positive a and inner widths b, ordinary terminal-kernel Fubini gives the nested integral with Wa Y_(n-1)^b. Its source Green limit agrees with the finite-measure expression: apply (6) to its finitely many Green factors. At fixed noise widths the full Gaussian product is E-continuous and globally bounded by

    sqrt((2n-1)!!) product_j sqrt(V_(a_j)).

The finite ordered Green mass is t^(2n)/(2n)!, so domination justifies the product-kernel/time integrals and the common Green limit. No noise limit or eta-dependent factor is inserted here.

Now fix external a. From (2),

    ||Wa(Y_(n-1)^b-X_(n-1))||E
      ≤2sqrt(n)sqrt(Va)||Y_(n-1)^b-X_(n-1)||E.

Equation(4) supplies domination in time and space. Bochner integration therefore proves the actual partial-vertex limit

    I_(n,a)=integral_0^t ds integral G_(t-s)(dz)
                       Wa(s,x-z)X_(n-1)(s,x-z)
            = lim_(b→0) Y_n^(b,a) in E.                 (9)

The n=1 identity has no inner widths. Each positive-width Y_n already has its Green limit first. Input008 passes through (9):

    sup_(a>0)||I_(n,a)||E ≤ q_n(t).                     (10)

To remove a, input006's JOINT convergence is essential. Given zeta>0, choose rho>0 so every vertex width below rho gives

    ||Y_n^(b,a)-X_n||E < zeta.

Fix any a below rho, then let b→0 in (9). This gives ||I_(n,a)-X_n||E≤zeta, with no relation imposed between the two external widths. Hence I_(n,a)→X_n as a→0; no separate partial-limit theorem or rate is assumed.

At each fixed a, (5), Fubini and absolute product summability identify

    I_a = integral G Wa*u = sum_(n≥1) I_(n,a) in E.

Its Green-first meaning is (8) applied to the FIXED actual Wa*u. From (10), for every N,

    ||I_a-(u-1)||E
      ≤ sum_(n=1)^N ||I_(n,a)-X_n||E
        +2 sum_(n>N) q_n(t).                            (11)

First a→0 at fixed N, then N→infinity. This is precisely009's mild identity. Bounds(4)/(5) may diverge as a→0; (10) is the different width-uniform estimate used for (11). Neither002 nor source Section5(ii), source4.1/L4.4 or a uniqueness theorem is needed in this argument.

## What002 and018 actually consume

For fixed m,n,006 gives joint E convergence and

    ||Y_mY_n-X_mX_n||1
      ≤||Y_m-X_m||2 ||Y_n||2
        +||X_m||2 ||Y_n-X_n||2 →0.

Finite positive-width Wick sums therefore pass to their individual two-chain limits, including empty chains. Reversal of both terminal chains at the same horizon is a change of variables in these moment integrals, not pathwise reversal of the noise. Summability from008 gives U_N=sum_(n≤N)X_n→u in E;009 now supplies the actual mild identification. Thus E U_N²→E u², and finite nonnegative mixed sums increase to the full double sum, which can be regrouped by total order. This is the consumer direction009→002;002 was not a premise above.

Explicitly, the first chain uses s'_j=t-s_(m+1-j),y'_j=x-y_(m+1-j), and the second uses its length-n counterpart. The vertex involution is rho(j)=m+1-j and rho(m+j)=m+n+1-j; it bijects pair partitions. Covariance differences change sign, absorbed by evenness. Zero-length factors remain1. The last square passage is

    |E U_N²-E u²|
      ≤||U_N-u||2 (||U_N||2+||u||2) →0.

Nonnegativity concerns these expected pairing terms, not samplewise monotonicity of U_N.

For018's fixed-noise finite moments, bounded continuous Gaussian covariance products satisfy the same averaging/Fubini argument on finite products of Green measures. Mixed Green approximations give the common second-moment limit, followed by006's noise limit and product L¹ convergence. This is not spatial covariance monotonicity or an all-order phase comparison.
It does not extend018's upper-bound conclusion beyond that proposition's low-alpha hypotheses.

## Falsification controls and scope

Weak positive-measure convergence alone is insufficient for unbounded integrands. On R,

    mu_j=(1-1/j)delta_0+(1/j)delta_j → delta_0 weakly,
    f(x)=x,      integral f dmu_j=1 ≠ f(0)=0.

All measures have mass1 and all displayed integrals are finite; the missing condition is uniform integrability/global control.

Even bounded continuous moving integrands need a uniform modulus. For mu_eta=p_eta,

    f_eta(z)=cos(z/sqrt(eta)),
    integral f_eta dmu_eta=exp(-1/2),     f_eta(0)=1.

The failure also occurs with an actual d3 wave measure: fix tau>0 and take

    f_eta(z)=exp(-(|z|-tau)²/(2eta)).

Its G_tau integral equals tau. Rotational invariance and

    (|tau e_1+sqrt(eta)Z|-tau)/sqrt(eta) → Z_1

give its p_eta*G_tau integral tending to tau E exp(-Z_1²/2)=tau/sqrt2, by bounded dominated convergence. These examples explain why the random factor is held fixed in (6)–(8), and why continuity alone at each eta would not suffice.

The calculation applies to all original H:homog covariances, singular spectra and d1white; heat smoothing supplies the finite Va actually used. For zero noise everything is direct with M=0. There is no new radius-uniform estimate, F-space lift, spatial point-trace theorem, uniqueness assertion, sharp-constant evaluation or independent-review credit.
