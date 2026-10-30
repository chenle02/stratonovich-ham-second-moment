# Actual-driver Gaussian tilt: explicit separable path-space target

Status: PROPOSED statement, not a proved or accepted Gaussian/flow result.
The target uses a finite product and an everywhere-defined continuous linear
assembly. Named accepted analytic inputs, together with their internal
definitions and dependencies, are notes/interaction-driver-path.md Sections5-6,
notes/local-causal-young-flow.md Sections3-7, notes/direct-event-calibration.md
Section1, and notes/phase-response-test.md Section5, inequality(M), lines302-325.
They retain their own scoped acceptance; this target does not freshly certify
them. No previous reviewer verdict is a mathematical input.

## 1. Original objects

Fix d=1, raw covariance |t-s|^-a Gamma(x-y), 0<a<1, 0<alpha<=1,
alpha+a<2, Gamma nonzero in the original homogeneous nonnegative Radon
class. No fBm normalization, covariance projection or residual discard.
Let psi be a real C_c^infinity((0,1) x R) test, extended by zero, Z=W(psi),
v=E Z^2. Here W is the raw-law noise in the SEMICLASSICAL equation of
notes/direct-event-calibration.md( W ), not the original unscaled field.
All raw drivers and Z use this SAME common Gaussian family W.
There is no assumption that each source cutoff is measurable from raw W.

Fix 0<delta<=1, L=1/delta, a nonnegative unit-mass smooth compact spatial
test phi, M=max{|x|:x in supp phi}, c>=1+M and r=c/delta. The mask zeta_r
is the one in the accepted local-flow note. The mask radius r is distinct
from the physical rescaling R=T delta. Use the accepted separable local
phase F, its massless free wave group S, and e0=(1,0) in F.
Define the distributional rescaled field and the actual interaction driver:

    W^delta(u,x)=delta^(a/2) W(delta u,x),
    g=delta^((1-a)/2),
    A(u)=g integral_0^u S(-q)B(zeta_r W^delta(dq))S(q), 0<=u<=L.

For an ordinary deterministic test f in fast time,
W^delta(f)=delta^(a/2-1) W(f(./delta,.)); this pins the distributional
Jacobian. W is a derivative noise, not an already integrated primitive.
The phase in a fast block is (V,partial_u V)=(V,delta partial_t V).

## 2. An explicit path space and assembly, at fixed parameters

Use the accepted chi_j and rho_j from local-flow Section4: rho_j is
supported in[j-1,j+1], sum_j rho_j=1 and chi_j=1 on supp rho_j. Put
O=[-2r-L,2r+L] and I={j in Z: supp rho_j intersects O}; I is finite.
Choose smooth compact kappa=1 on a neighborhood of O. Its multiplier
K:F->E is bounded, with E=H^(1/2)xH^(-1/2), by the accepted local cutoff
bound. No bound uniform in r or L is requested here.

Let H=HS(E), and choose 1/2<theta<gamma<1-a/2. Write h^theta_0([0,L];H)
for the closure of polygonal H-valued paths starting at0 in the C^theta
norm. This is a separable Banach space. Define the finite product Banach
space

    B = product_(j in I) h^theta_0([0,L];H),
    X_j(u)=chi_j A(u) on global E inputs,     X=(X_j)_(j in I).

Apply local-flow Sections3-6 to the raw-law field W^delta, single horizon
T=L and mask radius R=r; its source temporal cutoff is eta/delta. The
accepted local HS construction and its stronger-gamma paths give a
strongly measurable B-valued X with finite moments of every finite order.
Coordinates <X_j(q)e_k,e_l> at rational/dyadic q and a fixed Schwartz ONB
of E are deterministic noise-Hilbert limits, jointly Gaussian with Z.
These coordinates are required to generate the norm-Borel sigma-algebra
of B. The full little-Holder space with values in B(F) is NOT assumed
separable.

For EVERY x in B, not just compatible tuples, specify

    [Phi(x)(u)] w = sum_(j in I) rho_j [x_j(u)(K w)], w in F.     (A)

Multiplication by rho_j maps E continuously into F. The proposed assembly
is an everywhere-defined continuous linear map

    Phi:B -> C^theta_0([0,L];B(F)),
    ||Phi(x)||_Ctheta <= C_(r,L) sum_(j in I) ||x_j||_Ctheta.

It agrees with the accepted ACTUAL driver: Phi(X)=A a.s. This agreement
uses the accepted input support O, kappa=1 near O, output support O, and
partition of unity; it does not commute a mask with the wave group. This
full-product assembly removes any need for a Borel inverse of a compatible
HS-coordinate map. Its separable closed linear image closure may be used
as an operator-driver support, but equality of laws will be proved on B.
The displayed fixed-parameter Holder bound does not replace the accepted MAX bound or
its uniform growing-block estimates.

## 3. Covariance shift and the actual observable

Define the Bochner covariance b=E[X Z] in B and C=Phi(b). Bochner
integrability must follow from the finite B moments and Cauchy-Schwarz.
Thus C(u)=E[A(u)Z] in B(F) on its separable range. Set

    h(t,x)= integral_0^1 ds |t-s|^-a integral Gamma(x-dy) psi(s,y),
    H_delta(u)= integral_0^u S(-q)B(zeta_r h(delta q,.))S(q) dq.

This integral is a STRONG integral on each w in F, exactly as in the
accepted local-flow(5.5); norm continuity of S on F is not a premise.
Required exact identity:

    Phi(b)/sqrt(delta)=H_delta.                              (C)

The temporal kernel is locally integrable and singular; its convolution
h with the smooth test is bounded and smooth. Required application bounds:
t->h(t) is Lipschitz into C_b^1 on[0,1], uniformly W1infinity bounded,
with uniform C1 spatial tails to zero. For Riesz use the actual homogeneous
kernel c_Gamma|x|^-alpha with c_Gamma>0 and derivatives transferred to psi;
for white use c_Gamma times the spatial delta covariance. Convolution with
Gamma means convolution with the even covariance measure, preserving c_Gamma. Masked profiles are compactly supported and have
uniform W1infinity bounds for r>=1. These are obligations, not assumed
Cameron-shift or source-constant identifications.

For x in B let U_(Phi x) be the accepted linear Young evolution on F. Put

    J_delta(x)=|integral phi(y)
       [S(L)U_(Phi x)(L,0)e0]_1(y)dy|^2.                    (J)

The compact test is a bounded functional on F, so J_delta is required to
be a continuous nonnegative function on B. No raw point evaluation or
samplewise positivity of the displacement is requested. Noise-only J_delta(X)
is the squared canonical semiclassical smooth average by the accepted
local-flow Section6 identification and notes/direct-event-calibration.md Section1. Its expectation
is bounded above by the original point second moment, by the accepted
notes/phase-response-test.md Section5, inequality(M), lines302-325. This is a consumer toward the
original POINT target, not a redefinition of the target as an average.

## 4. Tilt target and exact application

For every nonnegative norm-Borel j:B->[0,infinity], prove

    E j(X)= E[exp(-Z/sqrt(delta)-v/(2delta))
                  j(X+b/sqrt(delta))].                     (T)

Degenerate finite-dimensional covariances, and v=0, are allowed. Finite
Gaussian coordinate cylinders followed by uniqueness on the countable
generating family may be used; no Gaussian inverse matrix or unnecessary
raw-field reconstruction is a premise. Equivalence of the tilted probability
to the original probability, its normalization, and all version/null-set
passages must be justified. Defining j on ALL of B avoids translating an
arbitrary exceptional coordinate-reconstruction set.

Take j=J_delta. Equations(A),(C) must identify the right observable as the
actual local flow with retained potential

    g zeta_r W^delta(u,x) + zeta_r h(delta u,x).

The raw amplitude calculation is g delta^(a/2)/sqrt(delta)=1. On fast block
m use h(m delta+delta u,x), retaining the last fractional block. Neither
independent increments nor a new source-regularized nonzero-profile
canonical series identity is assumed.

## 5. Non-vacuity, gate and remaining original target

The conditions hold for the actual d1 Riesz and white covariances; a
nonzero smooth test has positive variance in their raw Gaussian Hilbert
space. No spectral growth, event rate or sharp constant is a premise.
This is a standard Gaussian change-of-measure application, not a claim of
novel Gaussian theory or a publishable standalone theorem.

Before proof investment: obtain independent statement-fidelity review of
these exact objects and the assembly contract. Before scientific adoption:
write full self-contained proofs of the assembly/covariance/profile/tilt and
observable applications, check the small scalar sign/cost and exact real
powers, then obtain the mandated independent Opus5.5/HIGH analytic/type/
application review. The finite Lean audit will cover only feasible algebra,
not Gaussian measures or the Young flow. No new companion/package is created.

Still OPEN after (T): deterministic spectral projection/complementary
propagator on F, cone and entire growing product growth including constant
initial data/transients, nonzero final observable and event/variational rate,
profile-class approximation to the relevant optimizer and exact source
constant map. Profile-shifted causal mask independence must also be proved
before using it in the eventual sharp lower bound. Original higher dimensions,
sharp upper/lower constants, intended normalization, final whole-paper cold
read/novelty/circulation remain separate. Canonical TeX/PDF unchanged.
