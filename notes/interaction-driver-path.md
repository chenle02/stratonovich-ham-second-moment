# Localized interaction paths and source-cutoff convergence

Status: CANDIDATE. Independent source/type/application review is pending.
The result concerns a LOCALfirst Gaussian driver in d1. It does not construct
an all-order flow, a global operator for stationary noise, an event growth
bound or a sharp moment constant. The original full target remains open.

Fix0<a<1 and a nonzero original d1homogeneous covariance Gamma of degree
0<alpha<=1. Write E=H^(1/2)(R) x H^(-1/2)(R) and let S(t) be the free wave
phase group. Its Fourier matrix is [cos(tr),sin(tr)/r;-r sin(tr),cos(tr)].
It is bounded on E on each compact time interval and has finite propagation.
Let D_chi=diag(chi,chi) for a real compact smooth observation cutoff.
All temporal covariances are RAW |u-v|^-a. Put H=1-a/2.

## 1. Precise local statements

On Schwartz phase inputs define the first Gaussian interaction form

    M(t)=integral_0^t S(-u) B(W(du)) S(u),
    B(f)=[0,0;multiplication by f,0],
    X_chi(t)=D_chi M(t).                                   (D)

The raw M need not be a global bounded operator. The localized X_chi(t)
has the following concrete realization. For every fixed T0<infinity and
0<=s<t<=T0, h=t-s<=1,

    E||X_chi(t)-X_chi(s)||_(HS(E))^2
       <=C h^(2-a)                          if alpha<1,
       <=C h^(2-a)(1+|log h|)^2              if alpha=1.     (I)

Constants may depend on T0,a,Gamma and chi, not on h. The same estimates
hold uniformly for the common source noise cutoffs described in Section5.
For each1/2<theta<H, these processes admit HS(E)-valued C^theta versions.
The source-cutoff versions converge to the raw version in

    L^p(Omega;C^theta([0,T0];HS(E))) for every finite p>=1.  (P)

Compatible versions may be chosen for any fixed countable collection of
cutoffs chi. None of these assertions says that the whole stationary-noise
M(t) is globally Hilbert--Schmidt or gives an all-order solution map.

Named prior inputs from notes/phase-response-test.md, source0ae116c:
the exact localized first-response Gaussian HS trace and its balanced
endpoint; carrier weights w_(chi,v)(r) comparable to <r>^(2v); the Gaussian
Hilbert-valued Lp bound; and the temporal quadratic norm/modulation bounds.
Their scoped8HIGHsource/type gate is retained. The new time-uniform,
localization, cutoff and path arguments are proved below.

## 2. Balanced spatial convolution and a positive white trace identity

Use <x>=(1+x^2)^(1/2). The balanced convolution is

    D(q)=integral_R dk/(<k+q><k>),
    D(q)<=24 log(2+|q|)/<q>.                               (C)

Here is an explicit bound. D is even, and Cauchy--Schwarz gives D(q)<=pi
for bounded q. For q>=2 split |k|<=q/2, |k+q|<=q/2 and their complement.
The first two integrals are each at most4asinh(q/2)/q; the two remaining
tails are each at most2/q. Thus D(q)<=[8log(1+q)+4]/q. With
<q>/q<3/2, log(2+q)>1/2, this implies(C). For0<=q<=2 the same(C) follows
from pi<4, log2>1/2 and sqrt5<3.

For white space the critical spectral trace is

    I_a(h)=integral_R D(q)J_(a,h)(q)dq,
    J_(a,h)(q)=2integral_0^h(h-z)z^(-a)cos(qz)dz.            (W)

The prior temporal norm makes J nonnegative, not merely an oscillating
formula. An exact POSITIVErepresentation is

    L(z)=integral_0^infinity exp(-u-z^2/(4u))du/u,
    I_a(h)=2integral_0^h(h-z)z^(-a)L(z)^2 dz.                (B)

To justify it without a conditional Fourier interchange, insert
1/<k>=pi^(-1/2)integral_0^infinity u^(-1/2)exp(-u(1+k^2))du into D.
Positive Tonelli and the k Gaussian integral give

    D(q)=pi^(-1/2)integral_(u,v>0)
      exp(-u-v)/sqrt(uv(u+v)) exp(-c q^2)dudv,
    c=uv/(u+v)>0.                                         (G)

Since J>=0, Tonelli first interchanges this positive mixture with the
q integral in(W), allowing extended values. For each c>0, Gaussian q decay
and integrability of(h-z)z^-a justify Fubini in the formula for J. The
Gaussian cosine transform is sqrt(pi/c)exp(-z^2/(4c)), which is positive.
Tonelli applies again. Its prefactor becomes1/(uv), and
z^2/(4c)=z^2/(4u)+z^2/(4v), so the u,v integrals factor into L(z)^2.
This proves(B). The value L(0)=infinity is harmless on a time endpoint;
no uniform bound on that fiber has been used.

For0<z<=1 split the u integral at z^2 and1. The first part is at most4
after w=z^2/(4u), the middle at most2log(1/z), and the last at most1.
Consequently

    0<L(z)<=5+2log(1/z),
    I_a(h)<=C_a h^(2-a)(1+|log h|)^2, 0<h<=1.              (L)

Indeed set z=hv; the remaining integral is bounded by a constant times
integral_0^1(1-v)v^-a(1+|log v|)^2dv, finite for a<1. This also proves
that all extended positive integrals above are finite in their actual
consumer. For numerical checks only, L(z)=2K_0(z): the substitution
u=(z/2)exp(w) gives2integral_0^infinity exp(-z cosh w)dw.
No Bessel identity is needed by the analytic upper bound.

## 3. Uniform short-time first-response bound

Let N_chi(h) be the prior localized first-response operator over[0,h].
The exact time scaling gives

    J_(a,h)(q)=h^(2-a)J_(a,1)(hq),
    J_(a,h)(q)<=C_a h^(2-a)<hq>^(a-1).                     (S)

The second line follows from the prior unit-time global bound. It does
not use a fixed-time constant C_h as if uniform. The unit-time modulation
lemma is also uniform for low-mode factors after rescaling u=hv: cosine
and sin(ku)/k with |k|<=1 have uniformly bounded rescaled C1 norms for
h<=1, including their limiting values at k=0. The same applies to the
output low-mode factors at h-u.

If alpha<1, an absolute-time estimate already suffices. In the balanced
normalized trace the output factors satisfy, at EVERYr,

    sqrt(w_(chi,1/2)(r)) |sin((h-u)|r|)/|r||
       <=C/<r>^(1/2),
    sqrt(w_(chi,-1/2)(r)) |cos((h-u)|r|)|
       <=C/<r>^(1/2).                                     (F)

Use |sin x|<=min(|x|,1) and h<=1, so low r causes no division problem.
The two normalized input factors are bounded by C/<k>^(1/2) in the same
way. Since the raw covariance kernel is positive, each quadratic norm is
bounded by its amplitude squared times integral_[0,h]^2|u-v|^-a dudv.
The old exact HS isometry therefore gives

    E||N_chi(h)||_HS^2
       <=C h^(2-a)integral_R |q|^(alpha-1)D(q)dq
       <=C_(a,Gamma,chi)h^(2-a), alpha<1.                  (R)

The spatial integral is finite: near0 use D<=pi and alpha>0; at infinity
use(C), giving q^(alpha-2)log q and alpha<1.

For alpha1 WHITEspace retain the oscillations. On |r|,|k|>=1, the prior
four-component trace is bounded by a constant times

    integral dr dk [J_(a,h)(r-k)+J_(a,h)(r+k)]/(<r><k>).     (H)

Extending the positive integrand to the whole plane is legitimate. Since
the white spectral density is constant, k->-k makes the two integrals
equal. Their common value is I_a(h) from(W). This step is not valid by
that same change of variables for a nonconstant spectral density, which
was separately handled in(R).

The remaining frequency sectors require their own estimates. If |k|<=1
and |r|>=1, rescale the temporal integral to[0,1] and apply the prior
unit-time modulation bound to the uniformly C1 input factor. That gives
C h^(2-a)<hr>^(a-1). With the balanced output weight the sector is bounded
by C h^(2-a)integral_1^infinity <hr>^(a-1)dr/<r>.
The same argument with the output low-mode factor handles |r|<=1,|k|>=1.
The integral is at most C_a(1+|log h|), by splitting at1/h. Both modes
bounded contributes at most C h^(2-a). Together with(L),(H), this proves

    E||N_chi(h)||_HS^2
       <=C h^(2-a)(1+|log h|)^2, alpha=1.                  (N)

All trace constants retain the prior unitary spatial Fourier factor1/(2pi)
and the covariance amplitude of Gamma. The inequalities are norm bounds,
not an identification of a sharp moment constant.

## 4. The actual interaction increment: no cutoff commutation

Define the unlocalized first response N_(s,h) on Schwartz inputs using
the shifted noise W(s+du),0<=u<=h. Group multiplication gives

    M(t)-M(s)=S(-t)N_(s,h)S(s), t=s+h.                     (A)

This is an identity of Gaussian operator forms before localization. Its
source noise shift has the same law as W on[0,h], by stationarity of the
DERIVATIVEcovariance. No independent temporal increments are assumed.

Choose a fixed smooth psi equal to1 on a neighborhood of the T0-enlargement
of supp chi. Finite propagation, including the derivative kernel of the
wave phase, gives D_chi S(-t)=D_chi S(-t)D_psi for t<=T0. Thus

    X_chi(t)-X_chi(s)
       =D_chi S(-t) [D_psi N_(s,h)] S(s).                  (Q)

There is no commutation of D_chi with S. The two exterior operators are
bounded on E with constants uniform for s,t in[0,T0]. The middle operator
is exactly the prior localized first response. The HS ideal inequality
and(R),(N) prove(I). This also constructs localized fixed-time interaction
operators without asserting that M itself is globally bounded.

## 5. Common source cutoffs and Gaussian covariance domination

Use the current author's shared Gaussian construction(2.9)--(2.11), pp8--9.
W_eta retains independent temporal Laplace slices below1/eta, and W is
the sum of all slices; W-W_eta is independent of W_eta. The spatial heat
operator has multiplier exp(-epsilon q^2/2). An optional sharp spatial
projection |q|<=L is allowed for these linear integrals. Write F_(epsilon,L)
for their product, whose multiplier lies in[0,1], and

    W_rho=F_(epsilon,L)W_eta,
    W-W_rho=(I-F_(epsilon,L))W_eta+(W-W_eta).               (C0)

Work on that COMMON, possibly enlarged Gaussian space, not by assuming the
temporal cutoff is a convolution of the raw field. For every deterministic
noise test f, spatial Fourier isometry and independent slices imply

    Var(W_rho(f))<=Var(W(f)),
    Var((W-W_rho)(f))<=Var(W(f)).                           (V)

For the second bound, the two terms in(C0) are orthogonal. The first is
at most Var(W_eta(f)), since |1-F|<=1; the second is its complementary
slice variance. The same proof covers real and complex tests. Each test
variance of the difference tends to0 as epsilon,eta decrease to0 and L
increases to infinity, at arbitrary relative rates. The omitted slice
variance vanishes by positive monotone convergence, while the spatial
multiplier tends to1 and is bounded by1. Extend from smooth tests by
density and the contraction bounds. There is no claim that every cutoff
field is measurable with respect to the raw field alone.

Apply(V) to coordinates of any localized interaction response in an ONB
of HS(E). One may choose a Schwartz ONB of E by Gram--Schmidt from a dense
Schwartz set, then use its rank-one HS basis. The coordinates are literal
deterministic Gaussian noise tests first, and extend in the noise Hilbert
closure by the contraction bounds. The cutoff need not preserve the minimal
Gaussian span of the raw field; the common enlarged construction suffices.
Summing gives(I) uniformly for X_chi^rho and for X_chi-X_chi^rho. At a
fixed time, the raw sum is finite, each coordinate error tends to0, and
dominated convergence in this series gives

    X_chi^rho(t)->X_chi(t) in L2(Omega;HS(E)).               (T)

Their differences are Gaussian Hilbert-valued variables, so the prior
Gaussian Lp inequality upgrades(T) to every finite Lp. Covariance domination
is used only for LINEARresponses. It is not a nonlinear mean/solution
ordering or a residual-discard argument. No localization or wave operator
is commuted through a noise filter.
The argument after(V) uses only these common-space Gaussian covariance
bounds and convergence on deterministic tests. Any other jointly Gaussian
approximation satisfying them, up to fixed uniform constants, has the same
conclusions. The concrete source cutoffs above verify those hypotheses;
no such hypothesis is being asserted for a nonlinear solution map.

## 6. Hölder versions and convergence in the DRIVERnorm

We give the path argument explicitly. The unified(I) and Gaussian moments
give, uniformly for the raw, cutoff and difference processes,

    ||X(t)-X(s)||_(L^q HS)
       <=C_q h^H(1+|log h|), H=1-a/2 in(1/2,1).            (G0)

Coarse increments on a fixed[0,T0] are bounded by finitely many unit
increments; constants depend on T0. Fix1/2<theta<H. Choose gamma=(H+theta)/2
and q>max(2,p,2/(H-theta)), where p is any requested finite moment. Let
D_n be the maximum of the2^n adjacent increments on the dyadic grid of
[0,T0]. The elementary maximum bound and(G0), without independence, give

    ||D_n||_L^q<=C 2^(-n(H-1/q))(1+n).

The random sum Z_gamma=sum_n2^(n gamma)D_n has finite Lq norm, because

    epsilon=H-gamma-1/q>0,
    sum_n (1+n)2^(-n epsilon)<infinity.                     (D0)

Dyadic chaining constructs a C^gamma modification with norm at most a
constant times Z_gamma (and its zero initial value). To see the version
claim, first define limits of dyadic approximations; their uniform Cauchy
bound follows from the summable D_n. The limits agree at each fixed time
with the initial Gaussian response in Lq by(G0). Chaining the two endpoints
of any interval gives the Hölder bound. This does not exchange an arbitrary
uncountable set of exceptional null sets.

Let P_n be polygonal interpolation on that grid. Deterministically,
||f-P_n f||_C^theta <=C 2^(-n(gamma-theta))||f||_C^gamma.
The interpolation terms are strongly measurable in C^theta and the uniform
Lq bound gives a strongly measurable C^theta limit. Equivalently one may
use the separable little-Hölder space containing these C^gamma paths.
At fixed n, (T) gives P_n(X^rho-X)->0 in Lq C^theta. The two interpolation
errors are uniform in rho and vanish as n increases. First take the source
cutoffs to their limits at fixed n, then n to infinity. This proves(P) in
Lq, hence in the requested Lp. No regularization/large-time limit is
interchanged here. The argument applies to any sequence of joint source
widths and thus to the full joint limit.

For a fixed countable collection of spatial cutoffs, the identities
D_chi_i X_chi_j(t)=D_chi_j X_chi_i(t) hold in HS at dyadic times by the
common Gaussian form. Countable intersection and path continuity preserve
them at all times, so compatible local versions may be chosen. This is
still not a global stationary-noise operator-valued path on the whole line.

## 7. A finite-box local-driver estimate, not a flow event

For completeness a useful finite-grid consequence requires no temporal or
spatial independence. For0<delta<=1 and integers j,m, the normalized fields

    W_(j,m)^delta(u,x)=delta^(a/2)W(m delta+delta u,j+x)      (B0)

have the same raw covariance law as W. A source time cutoff eta becomes
eta/delta; spatial widths are unchanged. The bounds above are uniform
over these parameters. Form the unit-time localized drivers using these
fields and one fixed cutoff shape, and let K_delta be the maximum of their
C^theta HS norms over |j|<=ceil(1/delta),0<=m<=ceil(1/delta).
There are at most15delta^-2 boxes. Since max z_i^p<=sum z_i^p,

    ||delta^((1-a)/2) K_delta||_Lp
       <=C_p delta^((1-a)/2-2/p),
    p>4/(1-a) gives convergence to0.                       (U0)

The factor delta^((1-a)/2) is the actual residual amplitude after a block
time change in delta^2 Vtt=Delta V+sqrt(delta)WV. For a smooth
regularization the unit-block phase is (V,partial_u V)=(V,delta partial_t V);
this identifies the first-driver normalization only. Given any desired smaller
moment, choose a larger p satisfying this sufficient threshold. Markov then
gives local first-driver smallness events of probability tending to1.
It is not a necessary threshold for Gaussian maxima. Uniformity over source
widths is only a bound; it does not interchange their limits with delta->0.
It does not bound a
global stationary HS norm, construct a Young flow, or give an event on which
the actual solution has the required exponential growth. Noise truncation
on a growing cone, data1, nonzero deterministic profiles, spectral cones,
all-order remainders and source variational constants remain open.

## 8. Evidence and claim boundary

The finite Lean consumers check the actual square-root variance prefactor,
Gaussian-mixture prefactor/exponent, time-Hölder range/parameters, dyadic
ratio and finite-box scaling budget. All temporal/HS/measure/path arguments
above remain analytic review obligations. No global Gaussian/operator norm,
nonlinear covariance ordering, primitive square or sourceCDSTrestart estimate
has been assumed. This is d1 operator work; the original higher dimensions
and full sharp constant remain the goal. No Skorohod moment/asymptotic result,
intended source-normalization repair, novelty or circulation claim.
