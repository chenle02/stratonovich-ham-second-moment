# Article-Stratonovich-HAM-Second-Moment

The second moment of the Stratonovich hyperbolic Anderson model with noise
fractional in time: an upper bound at the correct scale
t^{(4−α−α₀)/(3−α)} and the sharp p = 2 constant, building on X. Chen,
*Time-dependency in hyperbolic Anderson models: Stratonovich regime*
(author version, submitted to AAP; arXiv:2510.01412).

**Goal revised by Le (2026-10-31):** derive the actual asymptotic constant,
whatever the computation gives. Chen's conjectured constants remain a
comparison rather than a required answer. See [PROJECT-GOAL.md](PROJECT-GOAL.md).

**Current written result (2026-11-03):** the original second-moment
limit for every admissible dimension and covariance has an explicit
intrinsic positive-control variational formula. The covariance amplitude,
kinetic coefficient one and variance-half action are specified in
[the limit theorem](notes/integrated_intrinsic_constant.tex). Zero covariance
is treated directly. The earlier independent full upper bound is retained.

The [occupation bounds](notes/integrated_occupation_ceiling.tex) and
[spatial-white example](notes/integrated_white_evaluation.tex) bound this
same constant. The white spatial energy is evaluated exactly; the moment
bounds are not an exact numerical evaluation of the intrinsic supremum.
The auxiliary label-one score is not identified with an actual first-moment
limit or Chen's printed constants.

The current scientific source, `af97ae4`, contains 28 TeX files, 214 proof
identities, 240 formal statements and a clean 263-page PDF. Its new compact
Young norm argument and direct real conservation proof passed a bounded
DeepSeek V4 Pro review of six changed deductions and their applications.
See the [adjudication](reviews/2026-11-03-structural-baseline-candidate/root-adjudication.md).

The [current index](reviews/2026-11-02-main-deepseek/proof-index-v7-neutral.json)
and [depth ledger](reviews/2026-11-02-main-deepseek/depth-ledger-v54.json)
record exact body and statement bindings. There are 210 locally accepted
HIGH scopes, one unaccepted proof row (010), and three pending editorial
changes. These scoped states do not establish whole-argument acceptance. Scoped
reviews bind their recorded versions and do not certify the whole argument.

DeepSeek V4 Pro is the main reviewer under Le's direction. The current
`af97ae4` whole MAIN is terminal after one fresh session and one factual
same-session public-record supplement: actual INCONCLUSIVE/low, with 214
reported proof rows (13 CHECKED, 201 LIMITED) and 13 literal joins (2 PASS,
11 PARTIAL). No source mathematical defect was located; the critical end-to-end
reconstruction remains incomplete. The [terminal record](reviews/2026-11-03-main-af97-terminal/)
preserves both original and supplemental texts and their reporting qualifiers.
Earlier whole reports on `8ce03ae` remain dated history. Local scoped states
are preserved and are not combined into whole acceptance.

The planned next work is substantive themed review with the full current
source and original model/constant obligations retained. This is preparation,
not a dispatched review or a union of earlier grades. The 263-page PNG
preparation supplies no independent visual reading. Source/application and
pixel checks, Kimi, the independent full-PDF visual audit and a fresh final
cold read remain open. Kimi's recorded monthly-quota 429 supplied no review
or images. Wiki propagation of this terminal outcome and final private
delivery remain pending. No whole-paper, goal-completion, readiness or
circulation clearance is claimed.

The 80 finite Lean facts retain their 22 analytic boundaries; an official
private companion and its package gate are separately authorized steps.
Private wiki maintenance and Git delivery have verified earlier checkpoints;
current outcome propagation and final delivery remain separate obligations.
`Progress.md` is the workflow authority. The human launcher's `HANDOFF.md`
identifies the active research checkout.

## Start here

1. `AGENTS.md`: goal, scope boundary, structural facts, rules
2. `PROJECT-GOAL.md`: completion contract
3. `Progress.md`: workflow authority and round plan
4. `sources/SOURCE-MANIFEST.md`: hash-pinned sources and page pinpoints
5. `notes/notes_stratonovich_ham_second_moment.tex`: model, known results, targets, route

## Building

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
```

## Hosting

`origin` is the <HUB> bare repository
`<HUB>:<HOME>/<REMOTES>/Article-Stratonovich-HAM-Second-Moment.git`.
The wiki project page is
`../SPDEs-wiki/content/projects/stratonovich-ham-second-moment.md`.

## Related projects

[held back: collaborators' unpublished work]