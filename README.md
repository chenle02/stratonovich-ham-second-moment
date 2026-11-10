# Article-Stratonovich-HAM-Second-Moment

**Primary working branch:** `master`, consolidated with the complete research history on November 9, 2026. The canonical checkout now contains the current manuscript and development history; no change of checkout is needed. The editorial reader history is now merged here; its branch remains preserved.

**Start here:** [STATUS-DIGEST.md](STATUS-DIGEST.md) is a one-page gate board and constraint summary (derived; Progress.md remains the authority).

**Current working draft (2026-11-09):** [267-page PDF](notes/notes_stratonovich_ham_second_moment.pdf) and [TeX](notes/notes_stratonovich_ham_second_moment.tex), preserved as an **unadopted mathematical candidate**. See [draft status](notes/WORKING-DRAFT-STATUS.md), [AI development history](AI-DEV-HISTORY.md), and [build evidence](reviews/2026-11-09-working-draft-267-checkpoint/README.md). Latest whole MAIN remains MEDIUM/unaccepted; the dated scientific and review summaries below are historical.

**Reading guide:** [20-page reader](notes/notes_stratonovich_ham_second_moment_reader.pdf),
[matching TeX](notes/notes_stratonovich_ham_second_moment_reader.tex), and
[guide](notes/README-reader.md). Updated on November 9 to match the current
267-page companion, with 69 matched technical labels and 209 checked external
PDF links. The combined record has 287 pages. It guides the reader through the
argument and depends on the full notes for detailed proofs; independent
clearance remains open. [Current validation](reviews/2026-11-09-reader-current-companion-merge/).
The original 263+20-page pairing at 9895781 remains historical.

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

The first themed working pass is now closed: DeepSeek returned
PASS_WITH_NOTES/medium for nine foundational proofs and fifteen declarations.
Its one factual addendum records eight CHECKED and PROOF010/S040 LIMITED,
because the mixed-series input remains unworked in that pass. The original
factorial calculation is correct; returned captions and metadata errors are
qualified in the [phase adjudication](reviews/2026-11-03-main-af97-theme-I-A-pilot/root-adjudication.md).
This supplies mathematical working and does not meet the required HIGH gate.
The following fifteen-proof pass and the later constructor, phase,
independent-upper and intrinsic-constant passes are also closed. Their returned
confidence and qualifications remain recorded under their original scopes;
none supplies whole-argument acceptance. No source repair was identified in
those adjudications.

The latest remaining-calibration review (2026-11-04) covered 21 proofs,
60 declarations and their canonical join. DeepSeek returned
INCONCLUSIVE/medium, with eight CHECKED and thirteen LIMITED proof records.
Root read the entire public response and all three complete author readbacks.
The [closed adjudication](reviews/2026-11-04-main-af97-calibration-prebound/final/)
distinguishes incomplete reconstruction and returned errors from manuscript
gaps. No new source gap was established under the named inputs; no local grade
or confidence was promoted. The original whole-current-source 214-proof,
240-declaration, 13-join scientific verification remains open. Closed reports
will not be retried for confidence or formatting.

The 263-page PNG preparation supplies no independent visual reading.
Source/application and pixel checks, Kimi, the independent full-PDF visual audit
and a fresh final cold read remain open. Kimi's recorded monthly-quota 429
supplied no review or images. Wiki propagation and final private delivery
remain pending. No whole-paper, goal-completion or circulation clearance is
claimed.

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

## Paper-dev dashboard

From the active research checkout, refresh the ignored session-state mirror
from the canonical sections of `Progress.md`, then launch the dashboard:

```bash
python3 scripts/refresh-paper-dev-state.py
paper-dev-dash
```

The historical round number remains4 while later scientific-cycle accounting
is audited. It is not a count of reviewer calls or a reset of review debt.
Dashboard review-directory counts are heuristic file discovery, not counts of
scientific rounds or accepted reviews. Read the actual adjudications for
qualified confidence. Missing session-local telemetry is not fabricated.

A separate launcher checkout can display the research state using the refresh
script's `--repo LAUNCHER --authority RESEARCH` options. Its own review list
still describes its older snapshot; `paper-dev-dash --repo RESEARCH` displays
the active checkout directly. The state JSON and lock remain gitignored.
This repair adds no reviewer role assignments or passed scientific gates.

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