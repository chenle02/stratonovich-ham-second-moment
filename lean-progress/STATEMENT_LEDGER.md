# Statement ledger

| Lean name (namespace StratonovichHAMAudit.ClockFilter) | Paper label | Exact boundary | Status |
|---|---|---|---|
| resolvent_partial_fraction | P:clock-copy-obstruction | Real positive theta/lambda,arbitrary r;exact resolvent difference divided by2theta*lambda | Local compile/replay;type/application4PASS/HIGH |
| clock_filter_bounds | P:clock-copy-obstruction | Positive theta/lambda imply filter strictly between0and1 | Local compile/replay;type/application4PASS/HIGH |
| strict_filter_integral | P:clock-copy-obstruction | Nonzero measure,lambda>0a.e.,integrable positive w;derives filtered integrability and strict integral deficit | Local compile/replay;conditional model input;type/application4PASS/HIGH |

Full types:local-checks/clock-filter-v1/StratonovichHAMAudit/ClockFilter.lean
and evidence/attempt-03/Audit.txt. No companion/package gate is claimed.

## Terminal-cross pilot: namespace StratonovichHAMAudit.TerminalCross

| Lean name | Consumer | Status |
|---|---|---|
| polynomial_identity | Exact shifted47termcertificate | Local compile/replay;application6PASS/HIGH |
| polynomial_pos | b>=1,c>1imply strict positivity | Local compile/replay;application6PASS/HIGH |
| rate_le | Uniform positive-mixture exponential rate | Local compile/replay;application6PASS/HIGH |
| exponential_difference | Convexity bound for slow/fast exponential difference | Local compile/replay;application6PASS/HIGH |
| terminal_bound | ACTUALstrict rational/square-root clock-envelope versus wave-integral bound | Local compile/replay;application6PASS/HIGH |

Exact hypotheses/types and excluded analytic inputs are in
local-checks/terminal-cross-v1/STATEMENT-FENCE.md and the source/Audit evidence.

The five terminal-cross names were checked together inC5of the six-group
analytic/type/applicationreview at6475ea0,not five separate six-checkreviews.

## Middle-crosspilot:StratonovichHAMAudit.MiddleCross

| Name | Scope | Status |
|---|---|---|
| certificate_pos | Positive300termHornercertificate | Local compile/replay; application HIGH at e638186 |
| parameter_identity | Exactrationalparameterizednumeratoridentity | Local compile/replay; application HIGH at e638186 |
| parameter_numerator_pos | z>=2,t>1giveclearednumeratorpositive | Local compile/replay; application HIGH at e638186 |
| difference_identity | ActualrationalI-Uequalsnum/positiveoriginaldenominator | Local compile/replay; application HIGH at e638186 |
| resolvent_difference | ExactnonsingularMdivideddifference | Local compile/replay; application HIGH at e638186 |
| root_numerator_pos | Actualrootsgiverootparameterizationandpositivenum | Local compile/replay; application HIGH at e638186 |
| middle_bound | ACTUALstrictU<Iwithbothsquarerootsanddomain | Local compile/replay; application HIGH at e638186 |

## Projection residual: StratonovichHAMAudit.ProjectionResidual

| Name | Scope | Status |
|---|---|---|
| projection_gap | Actual rational/sqrt coefficient lower gap greater than1/96 | Local compile/replay; exact type/application HIGH at efbdbd9 |
| tilted_gap | Affine retained-residual versus projected coefficient consumer | Local compile/replay; exact type/application HIGH at efbdbd9 |

Gaussian projection, cone/integral and full-mean/asymptotic inputs stay
outside Lean. Evidence: local-checks/projection-residual-v1/.

## Direct event: StratonovichHAMAudit.DirectEvent

| Name | Exact scope | Status |
|---|---|---|
| kappa_gt_one | Real target kappa greater than1 | Local compile/replay; exact type/application HIGH at9d77f90 |
| physical_scale | Actual positive-T real power for physical radius | Local compile/replay; exact type/application HIGH at9d77f90 |
| noise_scale | Actual equation amplitude equals Real.sqrt(delta) | Local compile/replay; exact type/application HIGH at9d77f90 |
| vertex_scale | Actual mild vertex amplitude equals delta^(-1/2) | Local compile/replay; exact type/application HIGH at9d77f90 |
| gauge_inverse | Exact2x2matrix inverse | Local compile/replay; exact type/application HIGH at9d77f90 |
| gauge_drift | Actual drift includes negative square | Local compile/replay; exact type/application HIGH at9d77f90 |
| monodromy | Scalar pulse product/determinant/trace | Local compile/replay; exact type/application HIGH at9d77f90 |

Gaussian/Green/series scaling, ODE/Floquet analysis and all rough-SPDE event
consumers are outside Lean. No companion or canonical package gate.

## Phase response: StratonovichHAMAudit.PhaseResponse

| Name | Scope | Status |
|---|---|---|
| rough_phase_choice | Actual s0 and strict trace/sector margins | Local compile/replay; exact type/application HIGH at0ae116c |
| balanced_phase | Actual balanced endpoint strict tail budget | Local compile/replay; exact type/application HIGH at0ae116c |
| energy_boundary | Exact energy-phase critical inequality | Local compile/replay; exact type/application HIGH at0ae116c |
| four_component_gram | Actual four-phase temporal Gram factorization | Local compile/replay; exact type/application HIGH at0ae116c |
| two_frequency_average | Exact half-factor cosine product | Local compile/replay; exact type/application HIGH at0ae116c |
| frequency_window | Actual rpow two-sided window from proved error input | Local compile/replay; exact type/application HIGH at0ae116c |

All temporal/Gaussian/spectral/Sobolev/HS-operator inputs and all-order flow
are outside Lean; this is not a formal SPDE or canonical package gate.

## Interaction driver: StratonovichHAMAudit.InteractionDriver

| Name | Scope | Status |
|---|---|---|
| temporal_range | Actual H=1-a/2 range | Local compile/replay; exact type/application HIGH atb398b77 |
| variance_norm | Actual variance sqrt/rpow/log-factor normalization | Local compile/replay; exact type/application HIGH atb398b77 |
| gaussian_prefactor | Actual positive Gaussian-mixture prefactor, P=pi application | Local compile/replay; exact type/application HIGH atb398b77 |
| gaussian_exponent | Actual harmonic Gaussian exponent separation | Local compile/replay; exact type/application HIGH atb398b77 |
| holder_parameters | Actual midpoint and high-moment dyadic margins | Local compile/replay; exact type/application HIGH atb398b77 |
| dyadic_ratio | Actual real-power summation ratio in(0,1) | Local compile/replay; exact type/application HIGH atb398b77 |
| box_margin | Sufficient two-index maximum margin | Local compile/replay; exact type/application HIGH atb398b77 |
| box_scale | Actual delta real-power Gaussian-max normalization | Local compile/replay; exact type/application HIGH atb398b77 |

Every Gaussian/HS/path/convergence/max/Young-flow and event/constant input
remains outside Lean. No companion or canonical package gate.
