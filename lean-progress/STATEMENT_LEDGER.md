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

## Local flow: StratonovichHAMAudit.LocalFlow

| Name | Scope | Status |
|---|---|---|
| noise_order | Actual finite mask/Schur/source-budget consumer | Local compile/replay; exact type/application HIGH atd020a2a |
| schur_row | Actual finite mask/Schur/source-budget consumer | Local compile/replay; exact type/application HIGH atd020a2a |
| schur_column | Actual finite mask/Schur/source-budget consumer | Local compile/replay; exact type/application HIGH atd020a2a |
| schur_rescale | Actual finite mask/Schur/source-budget consumer | Local compile/replay; exact type/application HIGH atd020a2a |
| source_overlap | Actual finite mask/Schur/source-budget consumer | Local compile/replay; exact type/application HIGH atd020a2a |
| source_white_obstruction | Actual finite mask/Schur/source-budget consumer | Local compile/replay; exact type/application HIGH atd020a2a |
| source_tail_obstruction | Actual finite mask/Schur/source-budget consumer | Local compile/replay; exact type/application HIGH atd020a2a |

## FiniteYoung local consumer: StratonovichHAMAudit.FiniteYoung

| Name | Scope | Status |
|---|---|---|
| weighted_natural_powers | Natural L>0,q<=L,real x/y, absolute integer powers and realcastweights; exact pinned Mathlib AM-GM reuse | Local compile/audit/owned5artifact replay/3False controls; exacttype/application HIGH scientific e59c29b, native format lineage preserved |

## Reconciled already-accepted local entries (state mirror only)

These25facts were already accepted in PROGRESS.md; sources checked equal
reviewed scientificGitblobs. No new proof/build/promotion in this inventory.

| Local seam | Public finite facts | Scientific application source |
|---|---|---|
| joint-tilt-v1 | 4 | e51432c |
| moving-cone-v1 | 3 | abfdab4 |
| actual-event-v1 | 2 | d5dcd46 |
| raw-variational-v1 | 4 | 0fd2a05 |
| occupation-form-v1 | 2 | 80e47d6 |
| raw-value-ceiling-v1 | 2 | ad6c188 |
| damped-lower-v1 | 3 | 8883160 |
| global-omega-v1 | 4 | ee188ab |
| dimensional-matrix-v1 | 1 | 0743b2d |

## Gaussian density split: StratonovichHAMAudit.GaussianTail

| Name | Scope | Status |
|---|---|---|
| cutoff_density_split | REAL M>0,x>=M,C>=0,1<nu<2,4C<=M^(2-nu) implies Cx^nu-x²/2<=-M²/8-x²/8; no Gaussian measure or operator assertion | Local clean source/type/stdaxioms/5pairreplay/3falsevariants; COMPLETE actualGLtail application HIGH scientific180bf1a |

## Positive-Gram finite core: StratonovichHAMAudit.PositiveGram

| Public name | Exact application/boundary | Status |
|---|---|---|
| scalar_sqrt_dual | Realell,w>0,t>=0; exact2ell sqrt(t)<=ell^2/w+w*t,includingt0 | Localtypes/std3/replay/Falsecontrols; PGapplication26HIGH |
| gram_norm_square | Finiteindex,realinnerproductspace,anysignedweights; exactnormsum^2=doubleGram | Sameexactgate |
| active_upper_bound | Finiteactiveindex,positivew,nonnegativeinner(Phi,k)-b; halfnormcost; no minimum/selection | Sameexactgate |
| half_weighted_entrywise_mono | Finiteindex,w>=0,Cij<=Dij; halfquadraticorder,noPSDdifference | Sameexactgate |

PrivateAudit.active_consumer integratesactiveupper+GramidentitytotheEXACT
conditionalPGbranchD_A bound; integrationevidence,notfifthpublicfact.
Scientific4e2219d,FULL26HIGH305.393s checksactualguards/type/application
anduncoveredPGanalyticproof. WholePGminimum/attainment/realization/PDE
notLean-certified. Source/types/receipts inlocal-checks/positive-gram-v1/.
