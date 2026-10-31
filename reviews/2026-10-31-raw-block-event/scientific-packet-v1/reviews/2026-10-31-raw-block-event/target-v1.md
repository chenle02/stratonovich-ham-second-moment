# New-F coupled raw block/cone/event and original-point lower target

FROZEN STATEMENT ONLY, not an adopted proof. Full original sharp p2 goal
ACTIVE. This retains ALL positive Psi(t,x), all original admissible d1/2/3
covariance measures and the ORIGINAL raw Gaussian cost.

Fix nonzero original H:homog Gamma, d=1,2,3, a in(0,1), alpha+a<2,
0<alpha<d or alpha=d=1. Fix nonnegative nonzero real
Psi in C_c^infinity((0,1)xR^d). W is the raw-law Gaussian noise in the
accepted semiscaling problem, not an asserted samplewise equality to
the original unscaled noise at every physical time. Put Z=W(Psi),v=E Z²>0,
h_sigma=int_0^1 |sigma-r|^-a Gamma*Psi(r,.)dr. Choose ONE finite mask
m_R as in accepted compact-mean-ground-family.md (scientificbfbd472,
adoptionab6596f), keeping Psi/Z/v fixed. Let V_sigma=m_R h_sigma,
sigma in I=[0,1], and lambda_sigma its accepted positive ground rate.
The mean formula extends smoothly on[0,2], though no spectral family
outside I is assumed. Set I_R=int_0^1 lambda_sigma d sigma.

Use EXACT accepted F=E directsum R², E=H1/2 x H-1/2, e0=(0,1,0),
O_phi(e,c1,c2)=<e1,phi>+c1 for fixed real phi>=0 smooth compact, integral1.
Let P_sigma(t),e_sigma,ell_sigma,Pi_sigma,Q_sigma and their uniform gap/
norm/continuity/positive entrance+test margins be the accepted actual
ground-family objects. Raw/source bounded-operator Young drivers and the
tested-average comparison are named accepted inputs, not re-proved here.

## A1. Re-establish the actual indexed cone on THIS phase

For every 0<rho<1/2 there are aperture vartheta>0, INTEGER B>=1,
omega>0,epsilon_op>0,c_*>0, depending only on this family/phi/rho, so that
for ANY N>=1, indices sigma_0,...,sigma_N in I with adjacent gaps<=omega,
and real bounded operators D_m(u) on F,0<=m<=N,0<=u<=B, satisfying

 sup_(m,u)||D_m(u)-P_(sigma_m)(u)||B(F)<=epsilon_op,

the full-state product obeys, for every 0<=s<=B,

 O_phi(D_N(s)D_(N-1)(B)...D_0(B)e0)
 >=c_*(1-rho)^(N-1)
       exp(B sum_(m<N)lambda_(sigma_m)+s lambda_(sigma_N)).     (A1)

No positivity, composition or independence of the perturbing operators is
assumed. Prove entrance, rebase the whole projection/residual BEFORE each
new block, preserve the two-entry cone and prove positive terminal average.
Use the normalized full complementary bound to choose aperture BEFORE B;
do not hide an exp(CB) terminal constant in that aperture choice. The old
d1 uniformly-local cone is a METHOD, not automatically a theorem on this F.

## A2. Actual common raw W/Z block array and mean covariance

Fix B,0<delta<min(1,1/B),N=floor(1/(delta B)),s_m=m delta B,
tau=1/delta-NB in[0,B). On the SAME given W define the fast noises by

 W_(delta,m)(f)=delta^(a/2-1) W(f((.-s_m)/delta,.)), 0<=m<=N,

where a positive-time test is extended by zero before pullback. This is an
isometry on the raw test-noise Hilbert completion; each fast noise has the
original raw covariance. They are not independent between m or from Z.
Choose accepted auxiliary gamma and Holder exponents
0<gamma<min(1/2,(2-alpha)/2),
1/2<theta<beta<min(1-a/2,(3-a-alpha)/2).
Let A_R(W_(delta,m)) be the actual masked first driver on F, local clock
u in[0,B], and X_(delta,m)=g_delta A_R(W_(delta,m)),
g_delta=delta^((1-a)/2). These are actual functions of this W, not only
equal-law substitutes.

Construct a real SEPARABLE Banach input space
mathcalB=h0^theta([0,B];K(F)), the Ctheta closure of zero-initial polygonal
compact-operator paths. Show the actual drivers lie there (finite raw
coefficient paths are Lipschitz/compact and converge in Lp Ctheta).
The tuple X_delta=(X_(delta,m))_(m<=N) and Z are jointly centered Gaussian,
strongly measurable, with all finite moments. Define b_delta=E[X_delta Z]
as a Bochner mean in mathcalB^(N+1). On ACTUAL matrix tests and both
constant-response columns prove the FULL path identity

 b_(delta,m)(u)=sqrt(delta) H_(delta,m)(u),
 H_(delta,m)(u)=int_0^u S_F(-r)iB(V_(s_m+delta r))S_F(r)dr.      (A2)

The right integral is strong on states, a Lipschitz operator path, and
belongs to the same input space by this identification. The time Jacobian
in X's slow raw matrix test is delta^(-1/2), not delta^(1/2). Do not
commute masks through free groups or assume a multiplier on the original
noise quotient. Mean profile is from the WHOLE Psi, not Psi(s_m,.).

## A3. Exact same-Z Gaussian shift on all Borel inputs

For EVERY nonnegative norm-Borel j on ALL mathcalB^(N+1), prove

 E j(X_delta)
 =E[exp(-Z/sqrt(delta)-v/(2delta))j(X_delta+H_delta)].          (A3)

Prove the common-space Gaussian law statement, not just an MG-function
check. One route is finite Gaussian completion of the square plus countable
coordinates generating the norm-Borel sigma-field on the actual separable
path space. The alternative scalar orthogonal decomposition needs its
independence/measurability justification. Degenerate joint covariances are
allowed; no infinite-dimensional conditional expectation/RNP is assumed.

## A4. Actual noisy/shifted Young blocks and uniform errors

For each input in mathcalB define its everywhere-defined Young interaction
flow and physical local-clock flow on F. Let D^0_(delta,m)(u) be the actual
noise-only flow for X_(delta,m) and D^+_(delta,m)(u) that for
X_(delta,m)+H_(delta,m). It is the actual mean V_(s_m+delta u) plus noise,
not a law-only drift hypothesis. For all p>=1,

 ||max_(m<=N)||X_(delta,m)||Ctheta||Lp
 <=C_R,B sqrt(p)g_delta (N+1)^(1/p).

Thus it tends to0 in any requested finite norm after choosing a larger
moment p>2/(1-a). Derive a uniform small square-exponential moment of this
scaled maximum for sufficiently high moments and use Young stability,
the smooth mean extension on[0,2] and its O(delta B) drift variation to prove

 max_(m<=N) sup_(0<=u<=B)||D^+_(delta,m)(u)-P_(s_m)(u)||B(F)
                      ->0 in EVERY finite Lq as delta->0.    (A4)

Only marginal moment bounds/finite maximum are used, no independence.
Probability convergence is not by itself an Lq proof. The final full block
may reach slow time1+delta B<=2 for these bounds, while the observable uses
only tau. Templates P_(s_m) have s_m<=1, so no ground outside I is claimed.

## A5. Actual canonical masked observable and squared shift identity

Define signed averages on the SAME raw space by the ordered full-phase
products

 U_delta=O_phi D^0_(delta,N)(tau)D^0_(delta,N-1)(B)...D^0_(delta,0)(B)e0,
 Y_delta=O_phi D^+_(delta,N)(tau)D^+_(delta,N-1)(B)...D^+_(delta,0)(B)e0.

Every restart carries displacement AND FAST velocity (V,delta V_t).
Using the common slow-field heat/Laplace-slice regularizations, show at
FIXED delta,N that these raw products are actual source limits; noise-only
U_delta is the tested masked semiscaled solution. Temporal source cutoff
becomes eta/delta in the fast clock; it is not temporal convolution.
No interchange of source and delta/time limits, no pathwise uniqueness of
the full unmasked canonical solution, or scalar moment products assumed.

The Young product-square functional is norm-Borel on ALL the input Banach
product, so A2-A3 give the EXACT same-Z identity

 E U_delta²=E[exp(-Z/sqrt(delta)-v/(2delta))Y_delta²].         (A5)

All moments needed at each fixed delta are finite. Use accepted fixed-mask
source/average comparison in the fast clock with noise amplitude g_delta
to obtain E U_delta²<=E|V_delta(1,0)|², where the FULL canonical V_delta
solves delta² V_tt=Delta V+sqrt(delta) W V with data(1,0).
No nonlinear shifted covariance comparison or Sobolev point trace is used.

## A6. Positive event, raw cost and original-point lower rate

For every e>0, construct the parameters B,rho from A1 and events E_delta
on this SAME W with P(E_delta)->1, such that for small delta

 Y_delta>=exp((I_R-e)/delta), |Z|<=delta^(-1/4) on E_delta.

The operator errors must be the ACTUAL A4 errors, and adjacent s_m gaps
must meet A1's omega. Include entrance and terminal remainder, including
tau0; use actual lambda Lipschitz/Riemann sums and the (1-rho)-loss budget.
Chebyshev for Z and a union bound suffice, not independence from errors.
Restrict the NONNEGATIVE SQUARE integrand in A5 to this event. The penalty
delta*delta^(-3/4)=delta^(1/4) is subleading; the cost is the ORIGINAL v/2.
Then

 liminf_(delta->0)delta log E U_delta² >=2I_R-v/2,
 Q2:=liminf_(T->infinity)T^(-kappa)log E|u(T,0)|² >=2I_R-v/2, (A6)
 kappa=(4-alpha-a)/(3-alpha).

The second inequality uses the EXACT accepted full-class canonical scaling
delta=T^-kappa, spatial compression r_T=Tdelta and point-moment identity.
r_T is NOT the fixed noise-mask R. It holds for each original positive
Psi and eligible finite R; a supremum follows only after per-test bounds.
No angular density, source first-moment equality or author normalization fix.

## Boundaries and finite verification

Recheck the nine OLD finite facts at their actual new consumers, with exact
source/type hashes in lean-reuse-readiness-v0.json. This is not new kernel
execution/application acceptance or a formal Gaussian/Young/cone/SPDE
theorem; existing71facts18seams/L0 unchanged pending the new gate.
The d1 raw first-chaos/completion covariance/MGF checks reject wrong signs/
Jacobian/cost models but are not proof of A1-A6 or point trace on F.
No source-large-time limit exchange, independent blocks, scalar moments
multiplied or p1 lower claim inferred by formal p-scaling. Variational
unmasking/all-alpha bridge, intended source L_* dictionary, sharp upper and
conditional exact limit remain OPEN after this proposed raw lower theorem.
Original full goal ACTIVE; no new companion/package/HPC/contact/Skorohod/
source fix/TeX/PDF/wiki/publication or independent novelty clearance.
