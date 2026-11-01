# Article-Stratonovich-HAM-Second-Moment

The second moment of the Stratonovich hyperbolic Anderson model with noise
fractional in time: an upper bound at the correct scale
t^{(4−α−α₀)/(3−α)} and the sharp p = 2 constant, building on X. Chen,
*Time-dependency in hyperbolic Anderson models: Stratonovich regime*
(author version, submitted to AAP; arXiv:2510.01412).

**Goal revised by Le (2026-10-31):** derive the actual asymptotic constant,
whatever the computation gives. Chen's conjectured constants remain a
comparison rather than a required answer. See [PROJECT-GOAL.md](PROJECT-GOAL.md).

**Current working result (2026-11-01):** the original second-moment
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

All planned mathematical modules are integrated in the
[TeX/PDF notes](notes/notes_stratonovich_ham_second_moment.pdf), and each
component passed its scoped independent proof/application review. Those
reviews bind their frozen versions. The current consolidation adds clarity,
repairs stale status text and retains the full proof scope; it requires
fresh whole-argument skeptical review and the final independent cold read.
Earlier failed attempts remain preserved. No whole-paper, goal-completion
or circulation clearance is claimed. Calibration/source checks, canonical
wiki propagation and actual Git/<HUB> convergence also remain open.
The proposed private Lean companion is separately gated; local finite
checks do not constitute its package gate. `Progress.md` is the workflow
authority; the root loader `HANDOFF.md` identifies the active checkout.

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