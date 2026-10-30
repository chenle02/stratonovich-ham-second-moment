# Three actual scalar margins; local standalone only

The candidate consumer is notes/moving-block-cone.md, equations18,
17-18and20-21. These proofs use Mathlib arithmetic/multiplication directly;
no nontrivial new definition or general spectral/cone library is introduced.
Existing direct-event/phase-response/interaction-driver finite sources
were inspected; none supplies this combination of quantitative budgets.
Direct reuse is Mathlib mul_le_mul_of_nonneg_right/left and nlinarith.
No claim of missing public general cone theorem or novelty is made.
Official release queries still show Lean/Mathlib4.35.0; donor pins read-only.

residual_budget: theta is aperture, q is normalized contraction, d is
nu*B, e is B_Q*epsilon*B. Analytic estimates supplying these numbers
are NOT formalized. The conclusion is the coefficient theta/2 in(18).
cone_conversion: a is old amplitude, x is new normalized amplitude,
y bounds the normalized residual. rho<1/2 and a>0 produce x>0 and
y<=theta*x, the exact cone closure application in(17)-(18).
terminal_margin: j=j_*,K=H*C_R,e=H*epsilon*B,y is normalized final
observable divided by current positive amplitude. The budgets in(8),(12)
and analytic lower bound(20) are inputs, not verified by this kernel fact.

Three incorrect omitted-budget numerical endpoints are False controls.
No spectral/ODE/Sobolev/wave/Gaussian/SPDE or complete cone theorem is
formalized. No new companion/package/registry/lease/cluster transaction.
Local compilation, exact public types/live axioms, fresh owned-source
replay, semantic False controls and independent application review required.
