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
