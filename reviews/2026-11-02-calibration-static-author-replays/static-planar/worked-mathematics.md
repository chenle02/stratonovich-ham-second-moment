# Static coefficient and planar transfer: complete author replay024–029

This is an author-only replay of the existing six claims, bound to scientific
source8ce03ae09cca984b32aaddf3da0a6ded07f47ebc. The main TeX has SHA256
364753242f9d02e57036af586ab8e777b184d897862750d3170d79f028067914;
its six bodies are unchanged from the preceding scientific base. No manuscript,
source edition, Git ref, provider, Lean, cluster or sibling project is changed.
The existing PROOF027 source-reconciliation-v1 receipt was read FIRST. It already
supplies the exact source-class and normalization checks; no claim is made that
this author work was previously missing. Its prior grades are not proof premises.

Write a=alpha_0. Keep the original nonnegative even positive-definite tempered
Radon covariance, Gaussian amplitude, data(1,0) and wave operatorDelta. The
original range is d in{1,2,3},0<a<1,alpha+a<2,0<alpha<d or alpha=d=1.
The static inputs below have temporal covariance1 and spatial degreechi.
The fractional-time coefficient is

    A_k(t)=sum_(m=0)^(2k) E[X_m(t,x) X_(2k-m)(t,x)],   A_0=1.

It is the FULL total-order2k coefficient, not the diagonal chaos coefficient.
We retain all unequal, within-chain, cross-chain and empty-chain terms. No
orthogonality of different Stratonovich orders is used.

## Subaim1 —024/027: exact static class, coefficient type and normalization

**Pinned imports and their roles.** The held published Chen–Hu PDF is the
52-page Annals of Probability53(6),2144–2195 edition, SHA256
58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22.
The held EJP28(2023),119 PDF of X.Chen is SHA256
9ed4b0ae633cc79eb1b985ecf00b2ae67db83061fd0d8a73628704b5b664a5da.
The latter has18 physical pages and printed article numbering1–17; its visible
FIXME running header is part of these held bytes. No edition is silently changed.
Fresh full-text extractions and selected-page hashes are retained in this replay
directory. Existing source render frames were viewed author-side only.

The exact imported source/application matrix is:

- Chen–Hu standing assumptions(1.1)–(1.3),p2145: static centered possibly
  generalized Gaussian noise, gamma>=0 and positive definite, d=1,2,3,
  gamma(x)=integral exp(i xi.x) mu(dxi), waveDelta. Its(2.18),p2152,
  interprets generalized covariance products by heat smoothing before limits.
- Chen–Hu homogeneity(1.8)/Theorem1.2,p2147 has0<chi<min(2,d), with a
  separately allowed chi=d=1 white case, and flat data(1,0). For024,
  gamma_chi=c|x|^(-chi),d=2 or3,1<chi<2 meets this range. For027,
  Xi is an arbitrary nonnegative even PD tempered Radon measure in d=2,
  of degreechi in(1,2). Here chi<2=d, NOT chi<2<d. No density is required.
- Chen–Hu Theorem3.8(i),(3.23),p2165 supplies the actual joint vertexwise
  noise-width L2 fixed-order limits under static Dalang. Its(2.17)/(2.19),
  pp2151–2152 are respectively the even Wick expectation and product rule.
- X.Chen Theorem1.1,(1.4),p2 and p1 standing assumptions permit generalized
  nonnegative PD covariances under Dalang. Only finiteness of the square-root
  covariance-energy minus HALF gradient supremum is used. The different
  nonsquare-root variational expression(1.5) is not substituted for it.
- Chen–Hu(5.1),p2173 gives total-order coefficient homogeneity, and(5.15),
  p2180 gives the upper factorially normalized COEFFICIENT rate at each fixed
  integer p. The p2 specialization is used below, not a large-p limit or an
  assumed uniform-in-smoothing moment asymptotic.

These published results are explicitly imported with their hypotheses. Their
full external proofs are not reproved here; the deductions and normalizations
needed for the manuscript's applications are derived next.

**Dalang from homogeneous spectral ball masses.** Let Xi be either static
endpoint. Its physical measure scaling is Xi(rA)=r^(d-chi)Xi(A). Fourier
uniqueness in tempered distributions gives

    mu_Xi(rA)=r^chi mu_Xi(A),
    mu_Xi(B_r)=V_Xi r^chi,   V_Xi=mu_Xi(B_1)<infinity.

The positive spectral measure is Radon. Positivechi also gives
mu_Xi({0})=0 by continuity from above. On dyadic annuli,

    integral (1+|xi|²)^(-1) mu_Xi(dxi)
      <=V_Xi +2^chi V_Xi sum_(j>=0)2^(j(chi-2)) <infinity.

Thus static Dalang holds for every angular profile in the stated class. No
angular/spectral density was inserted. For024 the Riesz covariance itself is
locally integrable becausechi<d, tempered, nonnegative and PD: the exact positive
Gaussian mixture of |x|^(-chi), paired with a Schwartz autocorrelation, is
absolutely integrable near0 and at infinity. Its amplitude is the statedc.
For027, PD/nonnegativity are its explicit covariance hypotheses; their physical
measure interpretation is allowed by the source's generalized convention.

**Full coefficients, including empty chains.** Put U_0=1 and use the source's
fixed-order static integrals U_n for n>=1. Define

    B_k(t)=sum_(m=0)^(2k) E[U_m(t,x) U_(2k-m)(t,x)].

When both orders are positive, the product rule gives the combined2k-integral,
and its expectation is the Wick sum over ALL pair partitions. If an order is0,
its factor is1 and the remaining even integral uses that same Wick rule. There
are exactly2k+1 splits, each once; the two empty-chain end cases are distinct
when k>=1. Different split products need not vanish or be orthogonal. Each is
finite by fixed-order L2 and Cauchy–Schwarz; the nonnegative covariance/Green
interpretation makes every contribution nonnegative.

For a time dilationt, each vertex contributes one time differential and one
wave measure: G_(t h)(t dz)=t G_h(dz). Across2k vertices this gives t^(4k).
Each of the k spatial covariance factors has degree-chi, giving t^(-chi k).
Thus B_k(t)=t^((4-chi)k)B_k(1), consistently with the actual p2 sum in source(5.1).
No extra terminal Green factor, binomial coefficient, or(2k)! is introduced.

**Unit-gradient M versus half-gradient E.** On the SAME real unit-L2 H1 class
F_d, write A_Xi(g) for the source's covariance quartic energy and
K(g)=integral|grad g|². Use the source's heat/generalized interpretation for
A_Xi if necessary. The two precise suprema are

    M_Xi =sup_(g inF_d){ sqrt(A_Xi(g)) - K(g) },
    E_half=sup_(g inF_d){ sqrt(A_Xi(g)) - K(g)/2 }<infinity.

The second finiteness statement is the imported Chen2023(1.4), not an asserted
new local theorem. For D_s g(x)=s^(d/2)g(sx), the norm stays1 and

    A_Xi(D_s g)=s^chi A_Xi(g),       K(D_s g)=s² K(g).

For a singular covariance, the first identity follows already at heat width
epsilon from A_epsilon(D_sg)=s^chi A_(s²epsilon)(g), then takes the same defining
source limit. It does not require monotonicity of the heat approximation.
Choose s=2^(2/(4-chi)). Then

    s^(chi/2)=s²/2=2^(chi/(4-chi)),
    E_half(D_sg)=2^(chi/(4-chi)) [sqrt(A_Xi(g))-K(g)].

D_s is one-to-one and onto the same entire F_d, with inverse D_(1/s).
Consequently

    E_half=2^(chi/(4-chi)) M_Xi.

This is exactly the source's printed p2175 dilation. Covariance amplitude,
H1 domain and signs of realg are unchanged; no optimizer/density restriction or
endpoint value is used. Finiteness of M follows. For nonzeroXi a unit Gaussian
g gives a positive finite covariance energy; a sufficiently small dilation
makes the chi/2-power term dominate the quadratic gradient, so M>0. No static
white-noise numerical corollary is needed.

**The actual published coefficient rate.** At fixed integerp let

    C_(k,p)(1)=sum_(l1+...+lp=2k) E product_(j=1)^p U_lj(1,x).

The actual statement(5.15), read with its preceding claim(5.3), is

    limsup_(k->infinity) (1/k) log[(k!)^(3-chi) C_(k,p)(1)]
      <=log[(1/2)^(3-chi) p^(4-chi)
             (2sqrt(M_Xi)/(4-chi))^(4-chi)].

The right side is the log of the FULL positive coefficient-rate quantity.
It is not a theorem about log of the moment divided by a time power. Atp=2,
C_(k,2)=B_k and (1/2)^(3-chi)2^(4-chi)=2. Therefore, with

    Lambda_st=2 (2sqrt(M_Xi)/(4-chi))^(4-chi),

    limsup (1/k)log[(k!)^(3-chi)B_k(1)]<=log Lambda_st<infinity.

For any finite R strictly above this limsup, eventually
(k!)^(3-chi)B_k(1)<=exp(Rk). Enlarge expR to dominate the finitely many
remaining kth roots. All are finite by the fixed-order L2 argument, and0
coefficients have root0. This produces a positive C_st valid for EVERY k>=1:

    0<=B_k(t)<= C_st^k t^((4-chi)k)/(k!)^(3-chi).

B_0=1 is treated separately. At Xi=0 all U_n,n>=1 vanish, B_k,k>=1 vanish,
and C_st=1 suffices; no log0 or Gamma(0) manipulation is required.

C_st is an all-order enlargement and need NOT equal Lambda_st. The source
rate alone does not prove the all-k inequality with Lambda_st substituted for
C_st. This distinction is retained in024/027 and in the transfer below.

## Subaim2 —025/028: actual regularized all-diagram Holder and fixed-order limits

Fix a=alpha_0,1<alpha<2-a. Choose ONCE

    a<theta<2-alpha,
    b=a/theta in(0,1),    chi=(alpha-theta)/(1-theta) in(alpha,2).

Indeed theta<2-alpha<1 and
chi-alpha=theta(alpha-1)/(1-theta)>0,
2-chi=(2-alpha-theta)/(1-theta)>0. The affine identities are

    alpha=theta+(1-theta)chi,       a=theta b.

For025 use isotropic gamma_e(x)=c|x|^(-e),e=1,alpha,chi in d=2 or3, with
ONE SAME physical amplitudec. The unsmoothed identity

    gamma_alpha=gamma_1^theta gamma_chi^(1-theta)

retains c^theta c^(1-theta)=c. Since the heat kernel is a probability density,
Holder gives gamma_(alpha,2epsilon)(z)<=gamma_(1,2epsilon)(z)^theta
 gamma_(chi,2epsilon)(z)^(1-theta), with no multiplicative loss. For028 use
the weighted planar endpoint measures of Subaim3, where exactly the analogous
heat inequality holds even for singular angular measures.

**One common positive diagram measure.** For k>=1 and fixedt, take the disjoint
union over all m=0,...,2k and all pairingsD of2k vertices. Each chain has its
own root; positions are cumulative vector increments in that chain. Let
h_l=s_l-s_predecessor(l)>0. With common positive spatial noise widthepsilon,
target temporal cutoffdelta>0 and, in d3, an additional Green widtheta>0, set

    integral Phi dnu =sum_m sum_D
      integral_(ordered_m x ordered_(2k-m)) ds
      integral Phi product_(l=1)^(2k) G_(h_l,eta)(dy_l).

In d2 takeeta=0. At fixedtimes the spatial mass is product h_l; the time
simplexes are bounded and both discrete sums are finite. Hence nu is finite.
It is identical for the target and both endpoints, including empty blocks.
The covariance on each edge is heat-regularized at2epsilon, because both
vertices have the same source width. Distinct endpoint models need not be
coupled on one probability space: the argument is Holder on their common
DETERMINISTIC diagram measure after each actual Gaussian moment formula.

Write H_J=product_(edges)(p_(2epsilon)*J)(x_i-x_j), and
T_b=product_(edges)|s_i-s_j|^(-b). The target's temporal productQ_delta obeys

    0<=Q_delta<=T_a=T_b^theta.

This is raw temporal domination from its Laplace-prefix regularization. It
asserts no interpolation identity between different temporal cutoff kernels.
For either the Riesz or planar spatial endpoints the common-width edge
inequality gives H_target<=H_low^theta H_static^(1-theta). Thus

    A_k^(epsilon,delta,eta)(t)
      =integral Q_delta H_target dnu
      <=(L_k^(epsilon,eta)(t))^theta (B_k^(epsilon,eta)(t))^(1-theta),

    L_k^(epsilon,eta)=integral T_b H_low dnu,
    B_k^(epsilon,eta)=integral H_static dnu.

Holder is applied to the FULL direct-sum measure, includingm andD. It introduces
no split count or pairing factor. The target and static integrals are actual
finite sums of regularized Gaussian-polynomial mixed moments: the Wick formula
and separate within-chain reversals give these precise expressions. Self-pairs
are included. B is the actual regularized STATIC coefficient. L is only a
deterministic positive integral with a raw temporal power; no fictitious
mixed-regularization stochastic solution or source limit for L is assumed.

**The low coefficient and exact combinatorics.** Suppose its common closing
convolution is bounded by M_low, independent of both widths, shift andh. At a
closing vertex in descending block-label order, precisely its own pair is the
only remaining covariance involving that increment. Integrating removes it
at costM_low. At an opening vertex its paired covariance was already removed,
so integrating contributes only its Green massh_l. This invariant concerns
positions in their OWN chains and works for all splits, self/cross pairs and
empty chains. It retains positive Green measures, also in d3.

There arek opening/closing vertices and sum h_l<=2t. Thus

    spatial integral <=M_low^k product_(openings)h_l
                       <=(2 M_low)^k t^k/k^k.

The temporal SUM over pairings is invariant under every permutation of its2k
labels; a single pairing generally is not symmetric. Its full-cube integral is
P_k (Z_b t^(2-b))^k, where

    P_k=(2k)!/(2^k k!),       Z_b=2/[(1-b)(2-b)].

The integral on a pair of ordered blocks is the full-cube integral divided by
m!(2k-m)!, by symmetry of the SUM. Consequently

    sum_m sum_D integral_(ordered_m x ordered_(2k-m)) T_b ds
      =P_k (Z_b t^(2-b))^k sum_(m=0)^(2k)1/[m!(2k-m)!]
      =(2^k/k!)(Z_b t^(2-b))^k,

because the reciprocal-factorial sum is2^(2k)/(2k)!. Multiplying gives

    L_k^(epsilon,eta)(t)
      <=(4 M_low Z_b)^k t^((3-b)k)/(k! k^k)
      <=(4 M_low Z_b)^k t^((3-b)k)/(k!)².

All raw temporal integrals are finite sinceb<1. No statistical independence
of time edges or chain fields is used in this deterministic cube computation.
At025, M_low=pi V_1/2, so C_low=2 Z_b pi V_1. At028, Subaim3 gives
M_low=S/4, hence C_low=Z_b S. The factor1/4 in the physical planar closing
bound and the temporal factor2^k are both indispensable.

**Actual Green-FIRST and source L2 limits.** At fixed positive noise widths,
every spatial covariance is bounded continuous, with a finite uniform bound
from its Gaussian-weighted spectral measure. Every finite-order source
integral is an actual Gaussian-polynomial Bochner integral; finite covariance
bounds and Gaussian moments justify its stochastic Fubini/Wick formula.
The current constructor L:joint-fixed-order includes its independent Case2
covariance bridge and supplies the later canonical source limit. We use its
stated original-model hypotheses, not the target asymptotic conclusion.

In d3, BEFORE removing any noise width, let the Green widtheta go to0. At a
fixed strict time vector, products of the finite Green measures converge
weakly to their actual wave measures, preserving masses product h_l. The
smoothed covariance product is a bounded continuous spatial test. A constant
at the fixed noise widths times product h_l dominates on the bounded time
simplexes. Dominated convergence therefore passes every Wick expectation.
For two Green widths eta andeta-prime the same argument applies to their
cross moment and gives the SAME limit. Thus

    E|Y_n^eta-Y_n^(eta-prime)|²
       =E|Y_n^eta|²+E|Y_n^(eta-prime)|²
           -2E[Y_n^eta Y_n^(eta-prime)] ->0.

This constructs the fixed-noise ordinary wave-measure integral in L2 and
matches the inner Green limit in both named sources. It is not a density
replacement for the d3 sphere measure. No such inner Green step is needed
in d2. At this stage the inequality keeps the same uniform deterministic
bound on L; L itself needs no limiting stochastic interpretation.

Next send target noise widths(epsilon,delta) to0 using the OWN current
L:joint-fixed-order, and static spatial widths to0 using Chen–Hu Theorem3.8(i).
The latter allows vertexwise widths, in particular the common-width limit.
Each fixed order converges in L2, on its own model's regularizing space.
For a split pair on that space,

    ||YZ-Y'Z'||1
      <=||Y-Y'||2 ||Z||2 +||Y'||2 ||Z-Z'||2 ->0.

L2 convergence also bounds the needed factor norms near the limit. There
are only2k+1 split products; an empty-chain factor is exactly1 throughout.
Hence A_k^(epsilon,delta,0)->A_k and B_k^(epsilon,0)->B_k. Pass the
inequality to these limits using the UNIFORM numerical L bound; only now
apply024 or027's raw static coefficient estimate. No pointwise monotonicity
in spatial smoothing and no static large-time asymptotic uniform inepsilon
have been used. The low temporal/spatial endpoint itself satisfies its
admissibility1+b<2, but constructing an additional mixed-regulation solution
is unnecessary for this passage.

**Factorial/time powers and the all-time result.** Substituting the two endpoint
bounds gives C=C_low^theta C_st^(1-theta) and

    A_k(t)<=C^k t^([theta(3-b)+(1-theta)(4-chi)]k)
                 /(k!)^[2theta+(1-theta)(3-chi)].

The exponents simplify EXACTLY:

    2theta+(1-theta)(3-chi)=3-alpha=:q>1,
    theta(3-b)+(1-theta)(4-chi)=4-alpha-a=:beta.

Thus A_k(t)<=C^k t^(beta k)/(k!)^q. SinceA_0=1, positivity and the actual
mixed-series construction identify Eu²=sum_k A_k. With z=C t^beta,

    sum_(k>=0) z^k/(k!)^q
       =sum_(k>=0) [z^(k/q)/k!]^q
       <=[sum_(k>=0) z^(k/q)/k!]^q
       =exp(q z^(1/q)).

This is the elementary nonnegative lq-versus-l1 inequality, valid for real
q>1, not an integer expansion assertion. It proves for EVERY t>0

    E u²(t,x)<=exp(q C^(1/q) t^kappa),  kappa=beta/q.

The exact covariance amplitude remains in both endpoint constants.

**Distinguish C_st from the nonsharp asymptotic Lambda.** The current all-time
statements use the enlarged C_st from Subaim1, including all finitek. The
source(5.15) alone does not justify replacing it by Lambda_st there. Separately,
for everyepsilon_*>0, the normalized static coefficient kth roots are eventually
at mostLambda_st+epsilon_*. The transfer then gives eventual kth-root bound
C_low^theta(Lambda_st+epsilon_*)^(1-theta) for the target coefficients.
The finitely many exceptional coefficient contributions are bounded by a
polynomial in t^beta using the already proved all-k bound; its log/t^kappa
tends to0. The remaining series is bounded by the same
nonnegative-series inequality. Therefore the separate, nonsharp consequence is

    limsup_(t->infinity)t^(-kappa)log E u²(t,x)
       <= Lambda_theta,
    Lambda_theta=q [C_low^theta Lambda_st^(1-theta)]^(1/q).

This numerical asymptotic bound is not a pure all-time C, not the derived
intrinsic moment constant, and not a sharp-value/source-endpoint identification.
Nothing here forces equality with Chen's printed first-moment L_* or L^*.

## Subaim3 —026/029: planar measures, positive definiteness and exact constants

Letd=2,1<alpha<2 and nonzeroGamma satisfy the standing covariance assumptions.
Put sigma(E)=(2-alpha)Gamma{0<|x|<=1,x/|x|inE}, S=sigma(S1). Scaling forces
Gamma({0})=0, and Radon finiteness gives S<infinity. S>0, since otherwise
homogeneity would make every ball masszero. Gamma-evenness makes sigma even.
For0<u<v and a Borel angular setE,

    Gamma{u<|x|<=v, directioninE}
       =[(v^(2-alpha)-u^(2-alpha))/(2-alpha)] sigma(E).

These finite-annulus polar rectangles generate the Borel sigma-field. Measure
uniqueness followed by increasing annuli gives the genuine polar disintegration

    Gamma(dx)=r^(1-alpha)dr sigma(domega),       r>0.

This is a measure statement and allows angular atoms or singular profiles.
The two weighted endpoints, with zero origin mass, have polar forms

    Gamma_low(dx)=|x|^(alpha-1)Gamma(dx)=dr sigma(domega),
    Gamma_st(dx)=|x|^(alpha-chi)Gamma(dx)=r^(1-chi)dr sigma(domega).

They are nonnegative, even, locally finite and tempered. The static radial
integral at0 is1/(2-chi), finite precisely forchi<2; Schwartz decay handles
infinity uniformly inomega. Their measure scaling degrees are1 and2-chi,
respectively, i.e. covariance homogeneity degrees1 andchi.

**PD of the endpoints; the zero radial power is direct.** Evenness gives

    Gamma_low(f)=(1/2) integral_(S1) integral_R f(r omega) dr sigma(domega).

Both line orientations occur on the full sphere, so the factor1/2 is required.
For phi Schwartz and psi=phi*tildephi, line/perpendicular Fubini gives

    integral_R psi(r omega)dr
      =integral_(omega-perp) |integral_R phi(s omega+v)ds|² dv >=0.

Schwartz decay justifies absolute Fubini uniformly over unitomega. Integrating
againstsigma proves PD ofGamma_low. In particular a zero radial Riesz power
on a line is handled by line Lebesgue measure, not by an invalid Gamma_E(0)
Gaussian-mixture formula.

ForGamma_st letlambda=chi-alpha>0. Onx!=0,

    |x|^(-lambda)=1/Gamma_E(lambda/2)
                    integral_0^infinity s^(lambda/2-1)exp(-s|x|²)ds.

Multiplication ofGamma byexp(-s|x|²) is PD: paired with a Schwartz
autocorrelation, its Fourier expression is the original positive spectral
measure paired with a positive Gaussian convolution of |hatphi|². Temperedness
makes the Schwartz pairing finite. Moreover integral|psi| dGamma_st<infinity
by its just-proved polar integrability. Tonelli on absolute values and then
Fubini justify the mixture, givingGamma_st(psi)>=0. This uses multiplication
by smooth PD Gaussians and a convergent scalar mixture; it is not a fractional
power of a distribution or an unsupported claim that arbitrary positive
weighting preserves PD.

**Physical closing constant.** Use G_h(y)=1_(|y|<h)/(2pi sqrt(h²-|y|²)),
zero on its boundary. Writez=u omega+v omega-perp. If|v|<h, then

    integral_R G_h(z-r omega)dr
       =(1/(2pi)) integral_(-sqrt(h²-v²))^(sqrt(h²-v²))
              [h²-v²-s²]^(-1/2)ds =1/2.

If|v|>=h, the line misses the open support or is tangent, and the integral is0.
A tangent singleton has zero line Lebesgue mass. Tonelli and the full-sphere
factor1/2 give

    (G_h*Gamma_low)(z)
       =(1/4)integral_(S1)1_(|z.omega-perp|<h) sigma(domega)<=S/4.

After positive heat smoothing of the covariance and optional Green measure,

    integral G_(h,eta)(dy)(p_epsilon*Gamma_low)(y+z)
      =[p_(epsilon+eta)*(G_h*Gamma_low)](z)<=S/4.

Evenness supplies the harmless sign change; heat variance adds and its mass
is1. The bound is uniform in h>0,epsilon>0,eta>=0 andz.

**Independent spectral normalization check.** In the paper's convention,
line Lebesgue measureL_omega onR2 has spectral measure
(1/(2pi))L_(omega-perp), because foromega=e1 this is exactly

    delta0(x2)=(1/(2pi))integral_R exp(i xi2 x2)dxi2.

Rotate the identity. Consequently

    mu_low=(1/(4pi))integral_(S1) L_(omega-perp) sigma(domega),
    V_low=mu_low(B1)=S/(2pi),
    pi V_low/2=S/4.

The unit-ball intersection with each line has length2. This independently
matches the degree-one convolution lemma and fixes every antipodal/2pi factor.
Combining the spatial and temporal calculation of Subaim2 gives

    C_low=4(S/4)Z_b=Z_b S=2Z_b pi V_low.

S is a PHYSICAL angular mass, not the original target spectral unit-ball mass.
For isotropicGamma=c|x|^(-alpha)dx inR2, sigma=c domega,S=2pi c andV_low=c.
For the line case below S=2c andV_low=c/pi. These different profiles must not
be normalized to a common fictitious angular density or massone measure.

**Unnormalized Gaussian-measure Holder.** Define the finite positive measure
m_(epsilon,z)(dx)=p_epsilon(z-x)Gamma(dx). Polynomial radial growth and Gaussian
decay give finiteness of it and both endpoint convolutions. With

    theta=(chi-alpha)/(chi-1),
    theta(alpha-1)+(1-theta)(alpha-chi)=0,

Holder with reciprocal exponents1/theta and1/(1-theta) gives

    (p_epsilon*Gamma)(z)
       =integral [|x|^(alpha-1)]^theta
                   [|x|^(alpha-chi)]^(1-theta) dm_(epsilon,z)
       <=(p_epsilon*Gamma_low)(z)^theta
          (p_epsilon*Gamma_st)(z)^(1-theta).

There is no normalization by m_(epsilon,z)(R2) and no extra mass factor.
Gamma has no origin atom, so the displayed multiplicative identity holds
where needed even if a radial factor is singular at0. No product or power
of generalized covariance distributions is used.

**Required singular-line falsification/control.** Retain amplitudec>0 and take

    Gamma(dx1,dx2)=c |x1|^(-1/4) dx1 delta0(dx2),
    alpha=5/4, a=1/5, theta=3/8, chi=7/5, b=8/15.

This is a nonnegative even PD tempered Radon covariance: the1D Riesz power
has exponent1/4 in(0,1), and the transverse delta has nonnegative constant
spectral density. Its physical scaling exponent is3/4=2-alpha. No full2D
density exists. The parameter window is strict:1/5<3/8<3/4,1<alpha<chi<2,
a+alpha=29/20<2. Its actual angular measure is

    sigma=c delta_(e1)+c delta_(-e1),       S=2c,
    Gamma_low=c dx1 delta0(dx2),
    Gamma_st=c |x1|^(-2/5) dx1 delta0(dx2).

The low endpoint has zero radial power along the line and is PD by the direct
line/spectral identity above. Applying a Gamma_E(0) mixture here would be wrong.
The exact unsmoothed closing convolution is
c/2 *1_(|z2|<h), so S/4=c/2 is correct. Dropping the antipodal mass or the
full-sphere1/2 would give the wrong constant. At amplitudeone,

    Z_(8/15)=225/77,       C_low=450/77,
    2theta+(1-theta)(3-chi)=7/4,
    theta(3-b)+(1-theta)(4-chi)=51/20,
    kappa=(51/20)/(7/4)=51/35.

For general amplitudec, C_low=450c/77; the static constant is evaluated for
that SAMEc inGamma_st. In fact B_k for a covariance multiplied byc is c^k
times its amplitudeone coefficient; the linear amplitude dependence of the
coefficient budget can be retained. M_(cXi)=c^(2/(4-chi))M_Xi, by a control
dilation, so Lambda_st(cXi)=c Lambda_st(Xi), consistently with this check.
No covariance amplitude is changed to make a constant agree with a prediction.

This line example also rejects pointwise heat monotonicity as a shortcut:
(p_epsilon*Gamma_low)(z)=c p_epsilon^(1)(z2), which tends toinfinity atz2=0
and to0 at fixedz2!=0 as epsilon decreases. The fixed-order L2 limit argument
above, rather than a presumed covariance order inepsilon, is therefore essential.

**All planar parameter ranges and exact scope.** Given any1<alpha<2-a in d2,
the open intervala<theta<2-alpha is nonempty. Its chi lies in(alpha,2), and
its b lies in(0,1), as checked in Subaim2. The target spectral ball exponent
alpha makes the fractional-time condition

    integral (1+|xi|²)^(-(2-a)/2) mu(dxi)<infinity

follow from a dyadic series with exponent alpha-(2-a)<0. The degree-one low
endpoint at temporalb has1+b<2, and the static endpoint haschi<2. Thus the
OWN target constructor and the exact imported static fixed-order theorem
both apply under their actual hypotheses.026,027 and028 yield the desired
upper scale in the whole higher-degree planar window, regardless of angular
singularity. For0<alpha<=1, the earlier general nonnegative-PD Radon bound
P:low-alpha-upper applies, including its oscillatory degree-one endpoint.
ForGamma=0, u=1 andC2=0. These cases cover the original entire planar range
0<alpha<2-a. They do not imply a general high-degree factorization in d3;
025 is only the isotropic Riesz transfer there. The separate later all-model
upper/intrinsic arguments are not inputs to these calculations.

[held back until the source author has been told]

**Disposition.** The own calculations above account for the six existing claims
under their named source hypotheses. In this replay I have not identified a
contradiction or additional mathematical gap in those deductions. This is
AUTHOR evidence, not an independent review or grade upgrade. Published theorem
proofs remain imported, and the actual source-image/global/fresh independent
cold gates and other all-model obligations remain separate. No automatic
review or manuscript edit follows from this artifact; root must inspect the
actual mathematics before deciding later bounded review.
