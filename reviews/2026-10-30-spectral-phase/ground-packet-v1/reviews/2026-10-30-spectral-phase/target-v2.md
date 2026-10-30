# Frozen spectral target on the actual local phase

PROPOSED, unproved and unreviewed. No spectral, product or lower rate
acceptance is asserted. Original full sharp/dimensional goal remains active.
This is a deterministic bridge, not a proposed novel spectral theorem.

## Objects

Use the accepted real phase F: closure of compact smooth phases plus the
two constants in uniformly local H^(1/2)xH^(-1/2). The free group and the
bounded-potential physical wave evolution are those in
notes/local-causal-young-flow.md Sections4-5. Initial data e0=(1,0).

All spaces are real. Fix0<a<1,0<alpha<=1,alpha+a<2, as in the accepted
local-flow/tilt notes. Fix the actual positive covariance-generated family

  psi(t,x)=f(t)q(x),
  k(t)=integral_0^1 |t-s|^-a f(s)ds,
  V_b(x)=b (Gamma*q)(x), b in K=[b0,b1],

where f,q are nonzero nonnegative compact smooth tests, f supported in(0,1),
and K contains the range of k on[0,1], with0<b0<=b1<infinity. Gamma is
the original nonzero d1 Riesz/white covariance including its amplitude.
Only in the white case is Gamma*q=c_Gamma q, with its actual positive
amplitude c_Gamma retained. Do not assume a compact Riesz potential. Freeze the family BEFORE selecting any gap constants.

Write H_b=-partial_x^2-V_b on real L2(R), and P_b(t) for the physical wave
flow on F with generator (v,w)->(w,partial_x^2 v+V_b v). All parameter
uniformity below is over this FIXED family K. No circle operator is used.

## Desired statement S1: projection and complementary propagator

Establish a simple negative lowest eigenvalue -lambda_b^2 of H_b with
lambda_b>0 and positive L2-normalized eigenfunction p_b, and constants
eta>0,C<infinity independent of b such that the growing wave projection is

  e_b=(p_b,lambda_b p_b),
  ell_b(v,w)=(<p_b,v>+<p_b,w>/lambda_b)/2,
  Pi_b z=e_b ell_b(z).

The pairings MUST be defined and bounded on the actual F, including its
constant phases, by decay/local Sobolev duality. Prove Pi_b^2=Pi_b,
P_b(t)Pi_b=e^(lambda_b t)Pi_b, uniform projection norms, and nonzero positive
ell_b(e0). No premise may assume the desired F-complement estimate.

Target the actual bound for all t>=0:

  ||P_b(t)(I-Pi_b)||_(F->F) <= C exp((lambda_b-eta)t),

with0<eta<inf_b lambda_b. The necessary gap between lambda_b and every
remaining growing rate (and the threshold0) must be established uniformly;
it is an obligation, not a spectral premise assumed from the complement bound. A proved polynomial-prefactor version with a
strictly smaller exponent is acceptable as an intermediate, but must be
converted with exact uniform constants before use in a fixed-block cone.
Do not assume only one negative Schrodinger eigenvalue; remove only the
largest growing wave mode. The decaying partner is in the complement.

The L2 spectral theorem is only an input to investigate. The passage to
H1/2xH-1/2 and then F needs a proof: finite propagation/localizing arbitrary
F data creates a growing global Sobolev norm, and the removed global
projection has tails that must be tracked after exponential growth. Compact
phases are not dense in F, since constants are separately included.

## Subsequent S2 consumers, not premises of S1

Uniform continuity of b->Pi_b,e_b,ell_b and the appropriate flow estimates
must support a fixed sufficiently long fast-block cone. Prove stability
under slow changes b=k(m delta) AND the actual small random block errors.
Track initial entrance, entire product, final fractional block and positive
terminal smooth displacement average. Phase-norm growth alone is insufficient.

For Riesz profiles, the actual tilted profile is zeta_r V_b. The difference
from V_b is small in W1infinity as r grows, but this requires its own fixed-
block estimate before the cone consumer. It is not equality of the profiles.
White compact support allows equality once the mask is1 on that support.

Only after S1/S2 can the accepted Gaussian tilt be used to prove an event
rate and optimize 2Lambda(h)-v/2. No such rate is asserted here. The exact
cost v=E W(psi)^2 and intended source normalization remain fixed/open.
Separable psi is a lower-bound subclass only; approximation by general
non-separable profiles/variational optimizers remains a separate obligation.

## Falsification and source gate

The exact finite diagnostics show both general implications are invalid:
large norm of each block does not force product growth, and large phase
norm does not force a nonzero displacement observable. They are NOT model
counterexamples or a no-go for the invariant-cone route.

Before proof investment, obtain source-level bounds for the Schrodinger
input at matched scope and a primary-source crosswalk for the F transfer,
then independent statement fidelity review of this frozen target. Local
wiki recon currently supplies no exact F transfer theorem. A survey or heat
semigroup estimate is not an imported wave theorem. Lean triage: projection
normalization/cone inequalities may be finite seams AFTER their actual
analytic consumer and hypotheses are fixed; do not build Gaussian/spectral
foundations or a new companion at this planning stage.
