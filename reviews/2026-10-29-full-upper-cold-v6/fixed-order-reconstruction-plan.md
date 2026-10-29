# Bounded independent reconstruction of the known fixed-order input

Decision:REFRAME as a known-result reconstruction at the ORIGINAL homogeneous
class,not a novelty claim,new lower wave,or a weaker target. Value:the sixth
cold report disputes the fixed-order import;the rendered source audit finds
repairable intermediate issues. Remove Chapter4as a black box rather than
assert its independence again. Expected cost:three lemmas(roughly5--8pages),
one focused cross-family proof audit plus the next full cold read. Stop and
diagnose if positivity/tightness/tail bounds need narrower covariance
assumptions;do not quietly add a density or isotropy restriction.

CURRENT STATE:the first lemma L:damped-homogeneous-norms is WRITTEN in the
notes and builds. Hypothesis H:homog now explicitly states the ORIGINAL
Radon covariance class;T:full-upper explicitly names the original canonical
series object;P:Jensen's forward-reference interchange is justified. Next
implement the remaining TWO lemmas,then update consumers. Do not spend a
new turn redesigning this plan. All new work remains UNREVIEWED.

## 1. Damped norms(already implemented)

Derive directly,without AppendixA.1:mu(B_r)=r^alpha*V gives the finite
resolvent integral proportional to a^(alpha-2). Thus N1finite follows from
integral lambda^(alpha0-1)*(theta+lambda)^(alpha-2),using alpha+alpha0<2.
For N2split frequencies <=1 and>1,use |Ghat_s|<=min(s,1/|xi|),mu(B1)<infty
and integral_|xi|>1 |xi|^-2 mu=alpha*V/(2-alpha). The time integrals with
and without st are finite since alpha0<1. Time covariance is PD so its
quadratic form perxi is nonnegative;this justifies removing Gaussian
multipliers,not pointwise heat-covariance domination. Scaling gives N0,N1,
N2powers. High Laplace-window tails M->infinity vanish by dominated
convergence. These are exactly the norms needed by the universal source
Theorem3.1;that is the remaining source inequality,not Chapter4or AppendixA.

## 2. Positive spatial Wick-measure lemma(to implement)

Fix chains m,n with m+n=2k>=2,possibly one empty,and pairingD. Let r_l>0
be each chain's successive time gaps,x_l the cumulative spatial increments,
and define
J_eps,D(r)=integral product_l G_(r_l)(dz_l)*product_e gamma_(eps_j+eps_h)(x_j-x_h).
Set rho_eps,D(dr)=J_eps,D(r)dr and nu_eps,D=e^(-sum r_l)*rho_eps,D.
All are positive at fixed widths. Spatial heat functions are bounded.

Independent gap Laplace transforms are POSITIVE SPECTRAL integrals:
L_eps,D(lambda)=integral exp[-sum_e(eps_j+eps_h)|xi_e|^2/2]
 *product_l[(1+lambda_l)^2+|eta_l(xi)|^2]^-1*product_e mu(dxi_e).
Define eta_l as the coefficient of spatial increment z_l in
sum_e xi_e*(x_j-x_h). Finite heat spectra justify Fourier/Laplace Fubini.
The transform,not the physical covariance,is monotone as each eps decreases.

Uniform total mass needs no imported static theorem. Use the wave/heat
resolvent identity integral e^-a t G_t dt=(1/2)integral e^-a^2 u/2 p_u du,
proved by Fourier transforms and mass. At lambda0,the2kGreen factors give
2^(-2k) times a two-Brownian-chain integral. First replace all widths by
their minimum in the EXPECTED positive spectral integral,not pathwise.

For common heat b,0<=(p_t*gamma_b)(x)<=A*t^(-alpha/2),by Fourier triangle
and homogeneity. If S_b(T)=integral_0^T integral_0^T gamma_b(B_s-B_t)dsdt,
order the2jtime variables in E S_b^j. Condition on the last remaining BM
vertex,then remove it and its partner. Its conditional heat bound costs
A*(last-previous remaining gap)^(-alpha/2). After jpeels the selected
right-endpoint gaps are DISTINCT and each dominates its original adjacent
gap. Dirichlet-simplex integration gives
E S_b(T)^j <= (2j)!*[A*Gamma_E(1-alpha/2)]^j
 *T^((2-alpha/2)j)/Gamma_E((2-alpha/2)j+1),uniformb.
Explain this peeling;do not invoke unavailable Lemma6.1from another edition.

Introduce BM terminal horizons with EXACT normalization
1=(1/4)integral_(s1>=tau_last1,s2>=tau_last2)
 exp[-(s1-tau_last1+s2-tau_last2)/2]ds1ds2.
Extend ordered BM domains to cubes by positivity. Mutual occupation obeys
A12<=sqrt(S1*S2) by spectral Cauchy--Schwarz. If pair counts are a,b,c with
a+b+c=k,the product is <=S1^(a+c/2)*S2^(b+c/2)
 <=(1+S1)^k*(1+S2)^k. NEVER use S1^k*S2^k without adding1.
Independence of the two BMs and the moment bound make their exponentially
damped horizon integrals finite,uniformly in every spatial width.

Hence L_eps,D(lambda) has a finite limit for alllambda>=0,continuous at0
by domination by its finite lambda0integrand. Apply/prove the finite-positive
multivariate Laplace continuity criterion to obtain nu_Dweakly. A short
self-contained criterion proof can use compactification y_l=e^-r_l:
bounded measures on[0,1]^(2k)have weak cluster limits,integer moments fix
them by polynomial density,and continuity atlambda0excludes mass at y_l0.
Do not cite Kallenberg2002Th5.22from the misfiled THIRD-edition PDF.

Coordinate-zero faces require a SEPARATE check:L_D(lambda*e_l)->0 aslambda
infinity by the same dominated positive resolvent integral. This equals
nu_D({r_l0}),so it is0. Global homogeneity alone does NOT prove this;the
negative control delta_0(dr1)*r2^2dr2is homogeneous of degree3and charges r1=0.

Let rho_D=e^(sum r)*nu_D. Heat/Green scaling gives
rho_eps,D(cA)=c^((4-alpha)k)*rho_(eps/c^2),D(A).
Vague limits give the same homogeneity for rho_D. For a nonempty chain
ell_i(r)=sum its gaps,each face ell_i=T>0 has zero mass:if a compact piece
had positive mass,its scaled copies with c in[1,2]would be disjoint,
positive uniformly,and lie in one compact set,contradicting local finiteness.
Thus finite-horizon regions are continuity sets. Bounded continuous temporal
weights pass through spatial limits at every positive T1,T2.

## 3. Joint diagram limits and Gaussian L2 construction(to implement)

At fixed temporal cutoffeta,the product of gamma_eta^0(time differences)
is bounded/continuous,so lemma2gives every spatial limit. Let
K_M(r)=Gamma_E(alpha0)^-1*integral_M^infty e^-lambda|r| lambda^(alpha0-1)dlambda.
The difference between a full temporal product and its eta-truncated product
is bounded by a sum with ONE edgeK_(1/eta),all other edges raw gamma^0.
Apply ONLY the universal sourceTheorem3.1 to damped Green functions at
fixed theta1(first Green smoothing if d3). Lemma1bounds all other norms,
and the marked edge contributes N1tail or N2tailSQUARED. Thus
sup_eps [F_eps,0,D-F_eps,eta,D] <= C_(k,T1,T2)*psi(1/eta)->0.
Use finite upper Laplace caps first if needed,then monotone convergence.

For every vertex delta_j<eta,positivity gives
F_eps,eta,D <= F_eps,bold_delta,D <= F_eps,0,D.
The uniform remainder and fixed-etaspacial limit give a finite joint limit
for ALL width ratios,including unequal/empty chains. State this explicitly.
For two copies of the same n-term,each Wick mixed moment tends to the same
finite sumQ_n. Therefore||Y_n^a-Y_n^b||_2^2->Q_n+Q_n-2Q_n=0.
Hilbert completeness definesX_nindependently of all width ratios. This
reproduces the KNOWN construction underH,without importing source4.1/4.4.

## Consumers and proof graph

Place these construction results in G0with norm definitions before the
crude/mild consumers. Move the existing fixed-positive-width Y_nprelude
before them. Simplify P:mixed using the new all-chain diagram limit;preserve
its prior valid source/colour proof in a review text artifact,not as a new
input. Replace ALL construction-consumer citations to source4.1/4.4by the
new lemma,including auxiliary covariances after checking their hypotheses.
Keep source4.1as historical comparison only. Do not claim the full general
spectral/nonhomogeneous source theorem was reproved;the original target is
HOMOGENEOUS throughout. Crude/mild constants remain separate from the
parameter-only upper moment constant. No cycle:heat/norms+universalbound ->
spatial/joint construction ->crude/mild;finite Gaussian interval estimates
are independently proved and feed the final moment branch.

Review gate:complete written proofs,clean source/PDF and exact semantic
scope/change map,new source-bound primary/HIGH(recheck universalTheorem3.1
proof independently),then fresh blind cold. No unchanged confidence retries.
All quantitative interval/CP/Fock proofs should remain as reviewed unless a
real defect is found. No source-normalization correction,uniqueness,Lean,
Skorohod development,novelty or circulation claim is authorized here.
