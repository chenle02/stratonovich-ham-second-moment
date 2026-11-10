# Joint Gaussian tilt for the actual masked local flow

Status: ACCEPTED at the scoped scientific statement/analytic/type/application
 gate: Opus5.5/HIGH,8PASS,366.846seconds,23texts, no required repairs.
Scientific source e51432c7d36f3a93aeb1ffcfa45b0dfa78f88a76; deterministic
byte-reversible report-fence recovery, no new provider call. Exact adoption
and seven optional clarifications are in
reviews/2026-10-30-joint-gaussian-tilt/scientific-adjudication-v1.md.
This is a standard Gaussian-tilt application, not a sharp constant, spectral
product estimate, whole-paper clearance or formal Gaussian Lean result.

## 1. Named inputs and exact objects

All Hilbert/Banach spaces and noises below are REAL. Use these scoped
accepted analytic inputs, with their internal definitions/dependencies:

- notes/interaction-driver-path.md Sections5-6: raw common-Gaussian local
  HS coordinate construction, finite Lp Holder paths, polygonal/little-Holder
  versions, and compatible source limits. This is a FIRST-driver result.
- notes/local-causal-young-flow.md Sections3-7: physical mask; local phase
  F containing e0=(1,0); cutoff K:F->E; HS-to-operator construction, input/
  output support; Banach Young evolution, deterministic profiles and canonical
  NOISE-ONLY smooth average. E=H^(1/2)(R)xH^(-1/2)(R).
- notes/direct-event-calibration.md Section1: exact original-to-semiclassical
  scaling, with delta=T^-kappa, physical R=T delta, and raw-law equation(W).
- notes/phase-response-test.md Section5, inequality(M), lines302-325:
  Bochner smooth-average-to-original-point second-moment inequality. It holds
  without samplewise positivity, for every physical T,R>0.

No source theorem is re-proved or upgraded here. In particular Gaussian
covariance contraction is NOT a nonlinear solution comparison.

Fix d1, 0<a<1, 0<alpha<=1, alpha+a<2 and a nonzero original homogeneous
nonnegative even positive-definite Radon covariance Gamma. In this d1 class
Gamma=c_Gamma |x|^-alpha dx for alpha<1, and c_Gamma delta_0 for alpha1,
with its actual positive amplitude retained (accepted phase-response Section4).
W denotes the raw-law Gaussian noise of the SEMICLASSICAL equation(W),
not an asserted equality to the original unscaled field on the same samples.
For real psi in C_c^infinity((0,1)xR), extended by zero, put Z=W(psi) and
v=E Z^2. The raw driver and Z use the same common W construction.

Fix 0<delta<=1, L=1/delta, nonnegative smooth compact phi of unit mass,
M=max{|x|:x in supp phi}, c>=1+M and mask radius r=c/delta. Thus the
backward cone of {L}xsupp phi lies in[-r,r]. This r is NOT the physical R.
Define the derivative noise distribution W^delta by

    W^delta(f)=delta^(a/2-1) W(f(./delta,.)),
    g=delta^((1-a)/2),
    A(u)=g integral_0^u S(-q)B(zeta_r W^delta(dq))S(q).       (1)

W^delta has raw covariance |u-u'|^-a Gamma: the two amplitude factors
cancel the time dilation in the covariance. Apply the accepted local-flow
construction on the SINGLE horizon T=L, mask R=r, to this field; its source
temporal cutoff is eta/delta. Every limit in this note is at fixed delta,r,L.

## 2. Explicit separable input and everywhere linear assembly

Let chi_j,rho_j be the accepted cutoffs/partition from local-flow Section4,
with supp rho_j contained in[j-1,j+1], chi_j=1 there and sum rho_j=1.
Set O=[-2r-L,2r+L], let I be the finite set of j whose supp rho_j intersects
O, and choose smooth compact kappa=1 on a neighborhood of O. Multiplication
K by kappa is bounded F->E by the accepted finite local cutoff bound(4.2).
Multiplication D_rhoj maps E boundedly into F: it is bounded on E, and all
global E phases embed continuously in F (local-flow Section4). For fixed
r,L these are ordinary finite constants; no volume-uniform estimate is used.

Choose 1/2<theta<gamma<1-a/2. Let h^theta_0([0,L];HS(E)) be the Ctheta
closure of polygonal HS paths starting at0, with norm sup plus Holder
seminorm. It is a closed Banach subspace. It is separable: first approximate
a polygonal path by one with dyadic breakpoints (in Ctheta for theta<1),
then approximate its finitely many vertices by a countable dense set in
HS(E). Taking the union over all finite grids gives a countable dense set.
Equivalently, the accepted polygonal approximation of every Cgamma path
converges here. Define the finite product Banach space

    B=product_(j in I) h^theta_0([0,L];HS(E)),
    X_j(u)=chi_j A(u) on global E inputs,       X=(X_j).       (2)

By the named local driver/path inputs, X is a strongly measurable B-valued
random variable with every finite norm moment. At rational/dyadic times its
HS matrix entries in a real Schwartz ONB of E are deterministic Gaussian
noise-test limits. They are jointly centered Gaussian WITH Z. Indeed finite
linear combinations of approximating tests are centered Gaussian; L2
convergence makes their variances converge and their characteristic functions
converge, which preserves the Gaussian law of each such combination.
This uses the common raw construction, not just a covariance upper bound.

For all x in B and w in F set

    Phi(x)(u)w=sum_(j in I) D_rhoj x_j(u) K w.               (3)

Each term is a bounded operator F->F, and

    ||Phi(x)||_Ctheta(B(F))
       <= ||K|| max_j||D_rhoj:E->F|| sum_j||x_j||_Ctheta(HS).

Thus Phi is an everywhere-defined continuous linear map into zero-initial
Ctheta operator paths. No compatibility of an arbitrary input tuple is
required. Its range has separable closure; the full B(F)-valued Holder
space is not asserted separable.

For the actual X, Phi(X)=A. To see this, the accepted input support O and
cutoff extension give A(u)w=A(u)K w for EVERY w in F, including constants.
Its output lies in O; hence sum_(j in I)rho_j times that output is itself.
Since rho_j chi_j=rho_j, (3) gives the equality. These identities can first
be imposed at countably many HS coordinates and dyadic times, then extended
by boundedness and path continuity. K handles constant inputs; global E is
not being assumed dense in F. No mask/free-group commutation or E-adjoint
support argument is used. This proves the assembly assertion.

Define b=E[XZ] as a Bochner integral in B. It exists since
E||XZ||_B <= (E||X||_B^2)^(1/2) v^(1/2)<infinity. Every continuous linear
coordinate of b equals the corresponding covariance with Z. Bounded
linearity gives

    C=Phi(b)=E[A Z] in Ctheta([0,L];B(F)).                  (4)

Bochner means are taken on the separable ranges just constructed.

## 3. Raw covariance profile and exact shift

Define convolution with the even covariance measure by

    h(t,x)= integral_0^1 |t-s|^-a (Gamma*psi(s,.))(x) ds.     (5)

This is a smooth bounded function for t in[0,1], with bounded spatial
first derivative. Here are the regularity and tail details needed by the
actual F-profile consumer. Every derivative of psi is smooth with one
compact support. For Riesz, convolution of any such derivative with
c_Gamma |x|^-alpha is uniformly bounded: near the compact support use
integrability of |x|^-alpha for alpha<1, and away from it use its bounded
power tail. For |x| larger than twice the spatial support radius plus1,
the same bound is C(1+|x|)^-alpha. Derivatives may be moved onto psi by
convolution of a tempered distribution and a smooth compact test. This
proves the uniform spatial C1 tail for the convolution and its time
derivative, with c_Gamma retained. For white noise the convolutions are
c_Gamma times the corresponding psi derivatives and are spatially compact.

To differentiate (5) in t, extend psi smoothly by zero and move the
derivative onto its time argument in the convolution with |.|^-a. This
is legitimate distributionally and gives an ordinary absolutely convergent
integral, since a<1. For t in[0,1], the relevant temporal distances have
absolute value at most1, and the integral of |q|^-a there is finite.
The same reasoning for one spatial derivative and one time derivative
gives uniform C_b^1 and time-derivative C_b^1 bounds. Consequently

    ||h(t)-h(t')||_Cb1 <= C |t-t'|,
    sup_(t in[0,1]) ||h(t)||_W1infinity < infinity,
    lim_(D->infinity) sup_t ||h(t)||_W1infinity(|x|>=D)=0.    (6)

The first bound also proves strong time measurability into C_b^1, despite
that ambient space being nonseparable. These are the accepted local-flow
(5.6) profile hypotheses with constant part0. Multiplication by zeta_r
preserves them. Its W1infinity bound is uniform for r>=1 because
||zeta_r'||_infinity=r^-1||zeta'||_infinity. The masked profile is compact.
The singular kernel in (5) is not pointwise bounded; its convolution h is.

Let H_delta be the deterministic interaction primitive of that profile:

    H_delta(u)w=integral_0^u
       S(-q)B(zeta_r h(delta q,.))S(q)w dq.                 (7)

This is the STRONG vector integral on F from the accepted local-flow(5.5).
It is Lipschitz in B(F); no operator-norm continuity of S is assumed.

For a smooth compact fast-time test f the raw Gaussian covariance gives

    E[W^delta(f)Z]
       =delta^(a/2-1) integral dt dx f(t/delta,x) h(t,x)
       =delta^(a/2) integral dq dx f(q,x)h(delta q,x).       (8)

All integrals are absolutely convergent on the compact test support: the
positive temporal kernel is locally integrable, and the spatial covariance
is a locally finite Radon measure. Signed tests are controlled by their
absolute smooth bounds. This calculation retains the distributional
Jacobian from (1); W is not an integrated time primitive.

Apply (8) to each scalar matrix coordinate of the first driver. The
coordinate kernel at time u is a bounded smooth space-time function on
[0,u]x[-2r,2r], multiplied by 1_[0,u] in time. This follows by taking real
Schwartz input/output basis phases in the accepted Gaussian form: free
wave multipliers preserve Schwartz functions on fixed horizons and the
physical mask makes the noise variable spatially compact. Approximate the
time indicator by bounded smooth cutoffs. Locally integrable |q-q'|^-a
and spatial local finiteness on this compact set give convergence in the
noise-Hilbert norm by dominated convergence; the corresponding deterministic
h-pairings converge by the same bounds. Thus (8) extends to the literal
coordinate kernels and then to their accepted noise-Hilbert limits.

It follows, coordinatewise and after the continuous assembly (3), that

    C(u)=g delta^(a/2) H_delta(u)=sqrt(delta) H_delta(u).
    Phi(b)/sqrt(delta)=H_delta.                             (9)

The scalar identity used is (1-a)/2+a/2=1/2, for positive delta. Equality
on a countable dense family of global E inputs/tests and rational times
extends by the bounded operator/cutoff construction to all F inputs and
times; both sides are continuous operator paths. No global stationary
bounded operator or covariance-order argument enters (9).

## 4. A countable Gaussian law calculation on B

The following elementary law calculation is included to fix signs, cost
and null sets. Let X be the B-valued variable above and b=E[XZ]. For every
real s and every nonnegative norm-Borel j on ALL of B,

    E j(X)=E[exp(-s Z-s^2 v/2) j(X+s b)].                  (10)

First, exp(-sZ-s^2v/2) has mean1 by completing the square in the scalar
normal density; if v=0 then Z=0 a.s. Its value is positive and finite a.s.,
so it defines a probability Q equivalent to P.

For finitely many real coordinate functionals l_1,...,l_n, put xi=l(X).
The vector (xi,Z) is centered jointly Gaussian. It can be represented in
law as (T N,z.N), where N is a finite vector of independent standard real
normals. This follows from a positive-semidefinite covariance square root;
singular covariance is allowed. Its covariance with Z is Tz=l(b) and
|z|^2=v. In the standard normal density for N, multiplication by
exp(-s z.N-s^2|z|^2/2) replaces exp(-|N|^2/2) by
exp(-|N+s z|^2/2). Substitution N'=N+s z therefore gives, for every bounded
Borel f on R^n,

    E_Q f(l(X+s b))=E f(l(X)).                              (11)

No inverse of the covariance of xi was used. This also proves the scalar
normalization just invoked (take f=1, or the one-dimensional integral).

For completeness these finite coordinate tests determine the B-valued law.
Take all HS matrix entries at times in (Q intersect[0,L]) union{0,L},
for each j in the finite set I. They are countably many continuous linear
functionals. For a continuous HS path its supremum norm and Holder
seminorm are suprema over rational times/pairs; each HS norm is the square
root of the countable sum of squared matrix entries. Hence the distance
to any fixed path in B is measurable with respect to these coordinates.
B is separable, so every open set is a countable union of balls with
centers in a fixed countable dense set and rational radii. Thus the
coordinates generate its full norm-Borel sigma-algebra. The finite
coordinate cylinders form a pi-system; the class of Borel sets on which
the two probability laws in (11) agree is a lambda-system. The elementary
pi-lambda uniqueness argument gives equality on all Borel sets. Integrate
simple nonnegative functions and use monotone convergence to obtain(10),
allowing either side to be infinite.

This is a law equality for variables defined on the full Banach space B.
No reconstruction on an unspecified exceptional coordinate subset is used.
Changing a version under P changes it only on a Q-null set, by equivalence.
The deterministic translate X+s b belongs to B on every sample where X
does, so it introduces no translated-domain exceptional set. This proves(10).

## 5. The actual squared average and the retained profile

For every x in B define

    J_delta(x)=|ell_phi S(L) U_(Phi x)(L,0)e0|^2,           (12)

where ell_phi is displacement pairing with phi. It is a bounded functional
on F by the accepted local cutoff bound and Sobolev duality with a smooth
compact test. Phi is continuous, S(L) is bounded on F, and the accepted
Young map is locally Lipschitz on bounded driver sets. Therefore J_delta
is continuous and nonnegative on B. This requires no samplewise sign of
the solution and no point evaluation on H^(1/2).

Use (10) with s=1/sqrt(delta) and j=J_delta. By (9) the translated operator
driver is A+H_delta. The accepted local-flow(5.5) deterministic-base Young
consumer therefore identifies the translated physical evolution with the
ACTUAL retained potential

    g zeta_r W^delta(u,x)+zeta_r h(delta u,x).

Thus, denoting its squared final smooth average by J_delta^h,

    E J_delta(X)
      = E[exp(-Z/sqrt(delta)-v/(2delta)) J_delta^h].         (13)

J_delta^h is a nonnegative measurable random variable on the original
common Gaussian probability space. The residual W^delta is fully retained;
no independent Gaussian copy, projection or residual-discard flow appears.
Existence and equality of the shifted flow follow from the accepted Young
map with deterministic base; a nonzero-profile source-series identity is
not being assumed. Equation(13) also makes its weighted expectation finite,
since the noise-only average has finite second moment.

At fixed delta, the mask is1 on the noise-only observation's backward
cone because M+L <= (1+M)/delta <=r. Accepted local-flow(6.1), applied at
T=L,R=r and amplitude g, identifies J_delta(X) with the canonical noise-
only semiclassical squared average. Direct-event Section1 maps that law
to the average of u(T,Rx), delta=T^-kappa,R=Tdelta. Finally, the named
phase-response Section5(M), lines302-325, gives

    E J_delta(X) <= E |u(T,0)|^2.                          (14)

It has no factor R^d because phi has unit L1 mass. This proves the tilt
consumer (13) toward the ORIGINAL point second moment. It does not
substitute an averaged end target.

On a unit fast block starting at m the deterministic coefficient in(13)
is zeta_r h(m delta+delta u,x), while the retained field is
W_m^delta(u,x)=delta^(a/2)W(m delta+delta u,x). The amplitude is still g,
and the physical phase is(V,delta V_t). Restriction of a continuous Young
path and its evolution composition law preserve the final fractional block.
This identifies the blocks but gives no bound on their entire product.

## 6. Honesty and remaining target

The new analytic claims are the explicit full-product assembly and Borel
consumer, raw profile/covariance shift, finite-coordinate tilt and its
actual squared-average application. Standard Young theory and the prior
canonical average/point inequality are named inputs, not re-proved here.
The exact finite sign/cost probes are supporting falsification only.

[held back: collaborators' unpublished work]