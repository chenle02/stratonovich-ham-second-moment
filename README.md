# Article-Stratonovich-HAM-Second-Moment

**Current reading copy:** [research notes, 263 pages](../../../../.local/state/Le-AI-Lab/stratonovich-fixed-mask-young-wave/notes/notes_stratonovich_ham_second_moment.pdf),
built November 3, 2026. The [110-page PDF stored here](notes/notes_stratonovich_ham_second_moment.pdf)
is the older October 29 snapshot. It is not a shortened edition of the current
notes. The scientific source and current technical PDF have not been cut.

**Compact reading prototype:** the [20-page reader](../../../../.local/state/Le-AI-Lab/stratonovich-reading-notes-20261105/notes/notes_stratonovich_ham_second_moment_reader.pdf)
and its [matching TeX](../../../../.local/state/Le-AI-Lab/stratonovich-reading-notes-20261105/notes/notes_stratonovich_ham_second_moment_reader.tex)
are committed together at `9895781` on `editorial/reading-notes-20261105`.
Read it with the complete 263-page technical companion above: 283 supplied
pages. This shortens the main reading route; total proof length and final
independent clearance remain separate questions.

The second moment of the Stratonovich hyperbolic Anderson model with noise
fractional in time: an upper bound at the correct scale
t^{(4−α−α₀)/(3−α)} and the sharp p = 2 constant, building on X. Chen,
*Time-dependency in hyperbolic Anderson models: Stratonovich regime*
(author version, submitted to AAP; arXiv:2510.01412).

**Active research status (2026-11-05):** the research checkout contains a
written correct-scale upper bound and a fully specified positive-control
variational formula for the original second-moment limit. Every original
admissible dimension/covariance, covariance amplitude, kinetic coefficient one,
variance-half action and zero-covariance case remain in scope. Chen's predicted
constants are comparisons; matching them is not a completion requirement.

This directory is the human launcher and retains an older manuscript snapshot.
The active checkout and exact source/verification state are identified by
[HANDOFF.md](HANDOFF.md). Its current
[workflow authority](../../../../.local/state/Le-AI-Lab/stratonovich-fixed-mask-young-wave/Progress.md)
and [research README](../../../../.local/state/Le-AI-Lab/stratonovich-fixed-mask-young-wave/README.md)
record the 28-file scientific source `af97ae4` and clean 263-page PDF. Use that
checkout for current research and builds.

Whole-argument acceptance remains open. Earlier whole/depth reviews returned
INCONCLUSIVE; later scoped A/B/C reports and their exact qualifications are
recorded in the active workflow authority above. Scoped reviews do not establish
whole-argument acceptance. Full 214-proof, 240-declaration, 13-join review,
required Kimi/source/visual checks, fresh final cold read and final private
delivery remain open. No completion or circulation clearance is claimed.

The existing 80 standalone finite Lean facts retain their 22 analytic seams.
An official private companion repository requires Le's separate authorization.

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