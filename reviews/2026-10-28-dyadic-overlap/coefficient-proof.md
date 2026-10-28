# Refined finite-interval coefficient proof

Status: UNREVIEWED. This fills the main operator/counting obligation in
candidate.md;it does not carry the static report's acceptance. All notation
and the bivariate energy orientation below are part of the proposed proof.

Assume the shifted covariance resolvent bound with R>0. Set
a=alpha/2 in(0,1),gamma=3-alpha>1,beta=4-alpha-alpha0>2,p=2-alpha0>1.
Take a finite connected-interval inventory I_i with lengths h_i,
independent unit stationary Gaussian fields W_i,epsilon,and
sigma_i²<=c h_i^{-alpha0}. At fixed smoothing and finite inventory,the
ordinary Gaussian Duhamel series is entire in all interval amplitudes in
L2 phase. One direct existence bound uses global Hermite cutoffN=n,
instantaneous variancev_max<infinity,and the bounded weak-phase insertion
2sqrt(n+1)sqrt(v_max)/lambda. Dyson's time simplex contributes T^n/n!.
This existence bound need not be uniform in inventory or smoothing.

For the uniform coefficient estimate,work first at finite Gaussian basis
and a spatial Fourier band. All operator applications of the CP theorem
are bounded. Fix a variance multiindex k_i>=1 of total k=sum k_i.
Put lambda=k/T. All scalar products are linear in the FIRST slot.

## A. Exact two-copy coefficient

Let M(z) be the phase evolution with interval couplings z_i sigma_i.
Use the SAME Gaussian fields in the two phase factors. The scalar
 F(z,w)=<M(z)v,M(conj(w))v>_{Gaussian;X_lambda}
is jointly holomorphic. At real equal couplings it is the actual mean-square
phase norm. Its (r_i,s_i)coefficient is the ordinary Gaussian inner product
of the two corresponding Duhamel coefficients. No independent replica of
the noise has been substituted.

Gaussian sign symmetry in each color makes coefficients with r_i+s_i odd
zero. At r_i+s_i=2k_i,the local Hermite cutoffN_i=2k_i preserves every
partial word from the Gaussian vacuum in both phase factors.
There are at most product_i(2k_i+1)<=3^k possible splits.

If k_i1,the split is mean-left(2,0),mean-right(0,2),or cross(1,1).
Let M be the singleton mean colors,C the cross singleton colors,and H the
colors with k_i>=2. Unused amplitude variables of mean colors are set
EXACTLYto0,not bounded on an unnecessary Cauchy circle.
Higher colors may be overestimated on both phase profiles.

## B. Complex circle background,with the degree local to each color

For each i in M union H,let
 lambda_i=k_i/h_i, d_i=2sqrt(2k_i+1)sqrt(R),
 rho_i=delta_a lambda_i^{2-a}/(sigma_i d_i).
Here d_i is for the field with its own Hermite cutoffN_i=2k_i,tensored
with identities on all the other Gaussian Hilbert factors.
The sandwich bound follows separately for each color,so NO global sqrt(k)
loss is inserted into every color radius.

On either phase factor,for fixed circle amplitudes,the background is
piecewise constant. Its profile is
 Lambda(t)=lambda+sum_{circle colors in that factor}lambda_i 1_{I_i}(t).
The sandwich norm of the complex potential is at most
 [sum_i |z_i|sigma_i d_i]rho^{a-2}.
For each constant segment this bracket is at most
 delta_a sum_i lambda_i^{2-a}<=delta_a Lambda(t)^{2-a}.
The complex phase lemma applies to this sum even though it need not be
selfadjoint:the adjoint has the identical all-rho sandwich norm bound,
and every resolvent/root/numerical-range step uses only those two bounds.

The segment norm is <=100exp(2Lambda times segment length).
The profile has at most2|M union H|endpoints. Inserting the cross-color
times below adds at most|C|cuts. Thus there are at most3k+1segments.
Moreover int_0^T Lambda(t)dt<=lambda T+sum_i lambda_i h_i<=2k.
All segment constants and exponential costs are therefore C^k.

Metric changes use the EXACT weak-phase comparison
 ||x||_{X_{rho_new}}<=max(1,rho_old/rho_new)||x||_{X_{rho_old}}.
At a downward jump,with ending circle colorsE,
 rho_old/rho_new<=1+sum_{i in E}lambda_i/lambda
                 <=product_{i in E}(1+lambda_i/lambda).
Only a downward change costs. At the initial point entering a larger profile
costs nothing. At T return toX_lambda. Each interval ends only once,including
a clipped endpoint atT. Thus the product metric cost per phase factor is
 product_{circle colors present}(1+k_i/(lambda h_i)).
A mean singleton appears in only ONE factor;higher colors cost at most
the square of this quantity in the two-copy energy.

This argument requires connected interval supports. A repeatedly active
field on many disjoint intervals is not covered by the one-exit count.

## C. Simultaneous cross extraction,with no permutation factorial

Extract the coefficient linear in each color inC in one phase factor.
It is the cube integral over t_i in I_i cap[0,T] of the background-evolution
word whose insertions are sorted by the t_i. The permutation simplices
partition that cube up to null diagonals. This is the multi-Duhamel formula;
there is no extra |C|! multiplying the cube.

Immediately before its ONLY insertion,color i is still in its Gaussian
vacuum. Background operators and insertions of other colors act as identity
on its Gaussian factor. For a phase u in the other Hilbert factors,
the creation insertion for color i is a bounded map with squared norm
 <=sigma_i² R Lambda(t_i)^{alpha-2}||u||_{X_{Lambda(t_i)}}².
This is the column identity
 sum_m M_{e_m}^* A_Lambda^{-1}M_{e_m}=J_Lambda(D)
 <=R Lambda^{alpha-2}I,
with the spatial band compression included by the positive operator
inequality S_b A_Lambda^{-1}S_b<=A_Lambda^{-1}.
The position component has norm at most the phase norm.

Already created distinct cross colors can be absorbed into the other
Hilbert factor,so these creation embeddings can be composed successively.
This is not an unsandwiched annihilation estimate;no color inC is used
twice on the same phase factor. Background evolution preserves its degree1.
Since alpha<2,Lambda(t_i)^{alpha-2}<=lambda^{alpha-2}.

For each point of the cube,the composition of these embeddings with the
background segments has all segment/metric costs counted once along the
word. Dividing a segment at an insertion increases the number of fixed
100factors by one,not the exponent of the earlier metric costs.
Minkowski in the common product-Gaussian Hilbert space gives a time-volume
factor product_i h_i. Cauchy-Schwarz between the two phase factors gives
the weight product_{i inC}(R sigma_i² h_i² lambda^{alpha-2}).

The entire construction is holomorphic in the remaining circle variables.
It can therefore be bounded uniformly on their polydiscs before applying
Cauchy's formula. The coefficient extraction inC and subsequent extraction
inM unionH commute at bounded cutoffs.

## D. Cauchy weights and the global reference phase

For l=k_i and i inM unionH,the total Cauchy power in the two copies is2l.
 d_i²<=12lR, so
 rho_i^{-2l}<=[12delta_a^{-2}R sigma_i² h_i^{4-alpha}/l^{3-alpha}]^l
 <=(C R sigma_i² h_i^{4-alpha})^l/(l!)^gamma.
The one-flow metric cost for mean colors is retained;the two-flow bound
is used for higher colors. Cross colors use sectionC instead.

All constants for segments,time growth and splits are C^k. The change of
the final energy test from X_lambda to X_{1/T} costs at mostk²;the initial
X_lambda norm is no larger than the initial X_{1/T} norm. Absorb this
polynomial intoC^k. The resulting coefficient bound is the product of:
 l1: C R [h_i^beta(1+1/(lambda h_i))
                   +lambda^{alpha-2}h_i^{2-alpha0}];
 l>=2: (C R)^l h_i^{beta l}(1+l/(lambda h_i))²/(l!)^gamma.
Every same-chain pairing and every cross-copy pairing remains represented.
No covariance monotonicity for arbitrary phases is asserted.

## E. Inventory product lemma,with uniform constants

Suppose the decreasing lengths satisfy h_i<=L T/i. The powers in sectionD
are monotone in h_i,because beta>2. Extract C^k R^k T^{beta k}.
The remaining coefficient sum is at most[t^k]product_i f_i(t),where
 f_i(t)=1+v_i t+sum_{l>=2}b_{i,l}t^l,
 v_i=i^{-beta}+k^{-1}i^{-(beta-1)}
                  +k^{alpha-2}i^{-p},
 b_{i,l}=i^{-beta l}(1+li/k)²/(l!)^gamma.
Constants depending onL,c can be absorbed per total variance order intoC^k.

Take t=theta k^gamma,theta1/4. Put
 P_i=theta k^gamma i^{-beta}, Q_i=theta k i^{-p}.
The cross part is Q_i because gamma+alpha-2=1.
Using1+A+B<=(1+A)(1+B),separate the product of(1+Q_i).
Forp>1,
 sum_i log(1+A i^{-p})
 <=int_0^infty log(1+A x^{-p})dx
 =A^{1/p}int_0^infty log(1+x^{-p})dx.
The integral is finite,so its contribution is <=C k^{1/p}<=C k.

Fori<=k,the remaining factor is at most S_gamma(4P_i).
Indeed the mean singleton is <=2P_i and(1+l i/k)²<=(1+l)²<=4^l.
Since gamma>1,log S_gamma(x)<=gamma x^{1/gamma}. Hence its total logarithm
is <=gamma(4theta)^{1/gamma} k sum_{i<=k}i^{-beta/gamma}<=C k,
using beta/gamma>1.

Fori>k,P_i<=theta. The remaining singleton sums to at most
 theta[1/(beta-1)+1/(beta-2)]k^{gamma+1-beta}=C k^{alpha0}.
Also sum_{l>=2}P_i^l(1+l i/k)²/(l!)^gamma
 <=C P_i²(1+(i/k)²).
Summing yields
 C k^{2gamma}[k^{1-2beta}/(2beta-1)
                +k^{-2}k^{3-2beta}/(2beta-3)]
 =C k^{2alpha0-1}<=C k.
Use log(1+y)<=y for these fine factors.
Therefore every finite inventory product at t=theta k^gamma is <=exp(C k).
Its positive coefficients give
 [t^k]product_i f_i(t)<=theta^{-k} k^{-gamma k}exp(C k)
                     <=C^k/(k!)^gamma.
No infinite-product existence is assumed;the bounds are uniform in the
finite inventory size.

## F. Cutoff and whole-phase conclusion

At fixed positive smoothing and finite interval inventory,the bounded
finite-degree v_max multiplication estimate gives strong convergence of
Gaussian-basis and Fourier-band cutoffs for each word,as in the static
proof. It also gives absolute L2 convergence of the full Duhamel series
uniformly over those cutoffs on compact coupling sets. Thus the coefficient
identities above pass to the actual finite-interval Gaussian model.

For every k>=1,its total global variance coefficient inX_{1/T} is bounded
in absolute value by
 C^k R^k T^{beta k}/(k!)^gamma ||(f,g)||_{1/T}²,
uniformly in the interval depth and positive spatial smoothing.
The zero coefficient is the free phase norm,at moste times initial norm².
Summing at real coupling1 gives
 E||M_V(T)(f,g)||_{1/T}²
 <=C exp(C R^{1/gamma}T^{beta/gamma})||(f,g)||_{1/T}².
Combining this with the explicitly proved dyadic covariance majorant and
the finite-order source transfer in candidate.md would prove G:upper.

Every assertion in this document still requires a full cross-family check.
The main danger is a hidden extra metric or combinatorial cost in sections
B--C;finite cube diagnostics alone cannot certify the Hilbert-valued proof.
