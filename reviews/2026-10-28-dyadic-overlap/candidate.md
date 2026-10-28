# Candidate reduction of overlapping interval fields to the full upper scale

Status: UNREVIEWED full-target proof candidate. Not covered by the static
nine-check report. No G:upper proof or breakthrough is claimed before full
adversarial/source-bound review. The argument below must be falsified first,
especially the simultaneous cross-singleton extraction and coefficient count.

## 1. Setup and the operator inputs

Let d=1,2,3,0<alpha<2,and Gamma be the original nonnegative even
positive-definite homogeneous Radon covariance,with the original admissible
dimension range (including d=alpha=1). Write
Gamma=int exp(i xi.x)mu(dxi),
R=alpha*pi*mu(B1)/(2sin(pi alpha/2)),
a=alpha/2,gamma=3-alpha.
If R0,noise is zero. Otherwise R>0.

The Gaussian Fourier comparison proving Section11's shifted-resolvent bound
works in every d:pair Gamma with p_{2s}(x)exp(i q.x),use its physical sign,
then integrate e^{-rho²s}ds. Thus
sup_q int mu(dxi)/(rho²+|q+xi|²)<=R rho^{alpha-2}.
For smoothed fields mu_epsilon=e^{-epsilon|xi|²}mu the same upper bound holds.
No angular density and no physical origin-atom exclusion are needed.
For white space in d1,Gamma=delta0,this gives1/(2rho)as it should.

Two consequences at a bounded Fourier band,with finite real Gaussian bases:
(A) A Gaussian phase insertion B_e(u,v)=(0,M_e u),on a new color in its
    Gaussian vacuum,has column norm at most sqrt(R)rho^{(alpha-2)/2}
    from X_rho to L2(new Gaussian color;X_rho).
    Proof:sum_e M_e^* A_rho^{-1}M_e is the shifted-resolvent multiplier
    J_rho(D)<=R rho^{alpha-2}I;the input only uses its position component.
    This holds with the identity on every other Gaussian Hilbert factor.
(B) With the Hermite degree of color i truncated at N_i,its sandwiched
    selfadjoint field has all-rho bound
    2sqrt(N_i+1)sqrt(R)rho^{a-2}.
    This is the full creation+annihilation estimate of Section12.

The complex phase lemma extends to a bounded NOT NECESSARILY selfadjoint
potential V when
||A_rho^{-1/2}V A_rho^{-1/2}||<=D rho^{a-2}, allrho.
Indeed the same norm bound holds for V*,the inverse-root resolvent estimate
is unchanged,and numerical range uses only absolute form bounds. If
D<=delta_a Lambda^{2-a},the four phase blocks have norm
100exp(2Lambda h)inX_Lambda. This extension needs an explicit new proof
in the final manuscript;it is not silently part of the frozen static lemma.

## 2. Finite interval model and its coefficient target

Fix T>0. Let I_i be a finite family of connected intervals meeting[0,T],
with lengths h_i. Order the lengths decreasingly and assume
h_i<=L T/i for one fixed L. Take independent copies W_i,epsilon of the
unit covariance Gamma_epsilon. Let
V(t,x)=sum_i sigma_i 1_{I_i}(t)W_i,epsilon(x),
sigma_i²<=c h_i^{-alpha0}, 0<alpha0<1,alpha+alpha0<2.
All fields may overlap;each individual field is supported on ONE interval.

For a deterministic Schwartz phase v=(f,g),the desired bound is
|[z^{2k}] E||M_{zV}(T)v||_{X_{1/T}}²|
 <=C^k R^k T^{beta k}/(k!)^gamma ||v||_{X_{1/T}}²,
beta=4-alpha-alpha0>2, gamma=3-alpha>1.
The coefficient is also even in each individual interval amplitude.
For fixed epsilon and a finite interval family,the full series exists:
the instantaneous variance is bounded by finite v_max. Global Hermite
cutoffN=n bounds a noise phase insertion by Csqrt(n+1)sqrt(v_max)/lambda.
Time-ordered Dyson integration supplies T^n/n!. This gives absolute L2
convergence at every coupling,though that existence bound depends on the
finite family and epsilon. It also justifies the amplitude expansions below.

## 3. Fix a variance multiindex and split its two-copy degrees

Let k_i>=1 for the active fields and sum_i k_i=k. The total degree of color i
in the two-copy energy is2k_i. Split it as r_i+s_i=2k_i,between the two
phase factors. The number of splits is at most product_i(2k_i+1)<=3^k.
A color with k_i1 has three types:
- mean-left:(r_i,s_i)=(2,0);
- mean-right:(0,2);
- cross:(1,1).
Colors k_i>=2 will all be called higher colors.

Introduce separate complex amplitude variables in the two phase factors.
With inner products linear in the first slot,
F(z,w)=<M(z)v,M(conj(w))v> is jointly holomorphic at bounded cutoffs.
Its coefficients are the ordinary Gaussian energy coefficients.
Use local Hermite cutoff N_i=2k_i. Every relevant partial word has at most
2k_i uses of color i,so this preserves the exact vacuum coefficient.
It retains self-pairings. No pure Wick-chaos assumption is made.

For each mean or higher color put lambda_i=k_i/h_i and choose the Cauchy
radius
rho_i=delta_a lambda_i^{2-a}/(sigma_i d_i),
d_i=2sqrt(2k_i+1)sqrt(R).
A mean color is present in only ONE phase factor. A higher color may be
present in both;overestimate its eventual metric loss by a square.
Cross colors are NOT placed on a circle:extract their linear coefficient
in each phase factor directly.

Let lambda=k/T. On either phase factor,the circle background has profile
Lambda(t)=lambda+sum_{circle colors present in that factor}
lambda_i 1_{I_i}(t).
At each constant-potential segment,
sum |z_i|sigma_i d_i<=delta_a sum lambda_i^{2-a}
 <=delta_a Lambda(t)^{2-a}.
Thus the generalized complex phase lemma applies inX_{Lambda(t)}.

There are at most2k+1background segments. Splitting also at the at-mostk
cross insertion times gives at most3k+1segments. Their exponential cost is
exp(2int Lambda(t)dt)<=exp(2lambda T+2sum_i lambda_i h_i)<=exp(4k)
per phase factor. All fixed100factors are C^k.

Metric conversion only loses when Lambda decreases:
||x||_{X_{rho_new}}<=max(1,rho_old/rho_new)||x||_{X_{rho_old}}.
At an endpoint,the loss is at most
1+sum_{ending i}lambda_i/lambda<=product_{ending i}(1+lambda_i/lambda).
Each connected interval ends once (also count a clipped endpointTonce).
Entering a larger metric incurs no loss. Hence each circle color contributes
one factor(1+k_i/(lambda h_i))PER PHASE FACTOR in which it occurs.
This is why a mean singleton costs one factor,not two.

## 4. Extract all cross singletons simultaneously

With the circle fields held at their complex values,the coefficient linear
in every cross color is the integral over the cube t_i in I_i cap[0,T] of
the time-sorted background-propagator word with one phase insertion for
each cross color. The permutation simplices are disjoint subsets of this
cube;there is NO extra factorial from summing orders.

Before its sole insertion,color i is still in its Gaussian vacuum.
All background operators act as identity on its Gaussian factor.
Thus consequence(A)can be composed at that insertion. Already-created
other cross colors can be included in the remaining Hilbert factor.
After insertion,background evolution cannot annihilate that color.
This gives a factor
sigma_i sqrt(R)Lambda(t_i)^{(alpha-2)/2}
 <=sigma_i sqrt(R)lambda^{(alpha-2)/2}
per insertion,without an unsandwiched row-variance estimate.

Minkowski over the cube gives product_i h_i. All background segments and
metric conversions occur only once along each time-sorted word,so their
bounds are the costs counted in section3,not powers of those costs for
each insertion. Cauchy-Schwarz between the two phase factors then gives,
for each cross singleton,the weight
R sigma_i² h_i² lambda^{alpha-2}.
This step is the main simultaneous-extraction point for independent review.

## 5. Resulting multicolor coefficient weights

Apply Cauchy to every circle variable after the cross extraction.
At k_i=l,
rho_i^{-2l}
 <=(C R sigma_i² h_i^{4-alpha})^l/(l!)^gamma.
Here d_i²<=12lR and l!<=l^l. The mean singleton has only one metric factor;
the higher colors can have two. Therefore,absorbing all segment/split
constants intoC^k,the coefficient for this active variance multiindex is
bounded by the product of:
k_i1:
 C R [h_i^beta(1+1/(lambda h_i))
       +lambda^{alpha-2}h_i^{2-alpha0}];
k_i=l>=2:
 (C R)^l h_i^{beta l}(1+l/(lambda h_i))²/(l!)^gamma.
The two mean orientations and the cross type are included in the singleton
sum. The phase-reference change fromX_lambda toX_{1/T}costs at most k²
in energy;absorb it intoC^k. Initial X_lambda norm is no larger than the
initial X_{1/T} norm.

Gaussian basis and Fourier-band cutoffs can now be removed at fixed
epsilon and fixed finite family/order,using the bounded finite-degree
multiplication/v_max argument from section2. The constants above do not
depend on those cutoffs or on epsilon.

## 6. The coefficient sum over ALL interval assignments

Use h_i<=L T/i and lambda=k/T. Each weight is increasing in h_i
(beta>2 suffices). ExtractC^k R^k T^{beta k}. The remaining coefficient
sum is bounded by the coefficient of t^k in the positive product
product_{i>=1}(1+v_{i,1}t+sum_{l>=2}v_{i,l}t^l),where
 v_{i,1}=i^{-beta}+k^{-1}i^{-(beta-1)}
          +k^{alpha-2}i^{-(2-alpha0)},
 v_{i,l}=i^{-beta l}(1+li/k)²/(l!)^gamma, l>=2.
All L-dependent constants can be absorbed per variance order intoC^k.

Take t=theta k^gamma with fixed small theta,say1/4. Put
p_i=theta k^gamma i^{-beta},q_i=theta k i^{-(2-alpha0)}.
For i<=k,the non-cross part of each factor is at most
S_gamma(4p_i)=sum_l(4p_i)^l/(l!)^gamma.
Since gamma>1,log S_gamma(x)<=gamma x^{1/gamma}. Thus
sum_{i<=k}log S_gamma(4p_i)
 <=C k sum_i i^{-beta/gamma}<=C k,
because beta-gamma=1-alpha0>0.
The cross product obeys
sum_i log(1+q_i)<=C_{alpha0} k^{1/(2-alpha0)}<=C k.
This elementary estimate follows by splitting at i approximately
k^{1/(2-alpha0)} and using Stirling/integral bounds on the initial part,
and the convergent power tail.

For i>k,p_i<=theta. The non-cross singleton tail sums to
C k^{gamma+1-beta}=C k^{alpha0}.
The l>=2tail is bounded by
C p_i²(1+(i/k)²),whose sum is
C k^{2gamma+1-2beta}=C k^{2alpha0-1}.
Both are <=C k. The cross logarithm was already included.
Consequently the whole product at t=theta k^gamma is <=exp(C k),
uniformly in the finite interval inventory. Positivity of its coefficients
gives coefficient<=C^k k^{-gamma k}<=C^k/(k!)^gamma.
This proves the stated finite-interval phase coefficient target IF all
operator/multicolor steps above survive detailed review.

## 7. Three adjacent dyadic grids dominate the temporal covariance

Choose a dyadic H0 with6T<=H0<12T,and grids at lengths h_j=H0*2^{-j},
with boundary shifts(-1)^j t h_j for t=0,1/3,2/3.
Each is nested because3t is an integer. At a scale3|s-r|<h_j<=6|s-r|,
the combined boundary locations have spacing h_j/3>|s-r|;
at least one grid interval contains both s and r. Hence,off the diagonal,
 |s-r|^{-alpha0}
 <=6^{alpha0} sum_{grid,I:|I|<=H0}|I|^{-alpha0}1_I(s)1_I(r).
The infinite sum is also <=C_{alpha0}|s-r|^{-alpha0},since only scales
h>=|s-r|can contribute and there is at most one interval per grid/scale
containing both points.

Keep only intervals meeting[0,T],through depthJ. Their decreasing lengths
satisfy h_i<=L T/i for an absolute L:at lengthh there are at most
3(T/h+2)intervals,and summing coarser dyadic levels gives that bound.
Use independent interval fields with sigma_I²=6^{alpha0}|I|^{-alpha0}.
The finite-interval target and the series in total variance order give a
phase upper bound C exp(C R^{1/gamma}T^{beta/gamma})uniformly inJ,epsilon.

## 8. Transfer to the ORIGINAL constant-data Stratonovich model

This step uses the already-reviewed Gaussian Wick expansion with ALL self
and mixed pairings (Section3/G0),not arbitrary-phase covariance monotonicity.
All wave Green measures are nonnegative in d1,2,3.

For the finite interval model,choose Schwartz f_T that equals1onB_{T+1},
is supported inB_{T+2},and0<=f_T<=1;take g0. Finite propagation,or induction
on the Duhamel position kernels,identifies its position at timeT onB1 with
the constant-data model. Each interval field is spatially stationary,so
 vol(B1)E|u_J,epsilon(T,0)|²
 <=E||u_{f_T,J,epsilon}(T)||_2²
 <=C(T+2)^d exp(C R^{1/gamma}T^{beta/gamma}).
No spatial band is left when finite propagation is used.

The finite models have nonnegative two-chain pairing coefficients for
constant data. Their temporal covariances increase to the dyadic majorant.
The author's actual temporal regularizations are nonnegative and dominated
by |s-r|^{-alpha0};the exact source formula/pinpoint must be rechecked.
Compare the finite partial-order ORIGINAL regularized expansion to the
majorant pairing integrals,then letJ->infinity by nonnegative Tonelli.
The preceding bound is uniform inJandspatial smoothing.

At fixed partial order,the source's defining L2 noise limits give the
original finite sum. Finally let the partial-order cutoff tend to infinity
using the source/G0 L2 series construction. This avoids assuming convergence
of the whole regularized propagator before the finite-order limit.
The resulting upper bound is
 E u(T,x)^2<=C(T+2)^d exp(C R^{1/(3-alpha)}
                              T^{(4-alpha-alpha0)/(3-alpha)}), T>=1,
which would establish the unchanged full Goal G:upper.
No first-moment variational constant,sharp constant,Skorohod exact theorem,
novelty,Lean or circulation claim is used or established here.

## Review blockers to resolve BEFORE any promotion

- Write and check the general complex-potential extension explicitly.
- Verify the simultaneous cross-singleton cube/column-variance estimate
  as an operator-valued statement,with no missing factorial or metric cost.
- Verify separate-flow Cauchy extraction for every split r_i+s_i=2k_i.
- Give fully explicit uniform constants in the inventory generating bound.
- Pin the source temporal cutoff domination and fixed-order L2 limits.
- Freeze the entire proof and obtain a full-source cross-family skeptic.
