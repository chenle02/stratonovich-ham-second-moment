# Article-Stratonovich-HAM-Second-Moment

The second moment of the Stratonovich hyperbolic Anderson model with noise
fractional in time: an upper bound at the correct scale
t^{(4−α−α₀)/(3−α)} and the sharp p = 2 constant, building on X. Chen,
*Time-dependency in hyperbolic Anderson models: Stratonovich regime*
(author version, submitted to AAP; arXiv:2510.01412).

**Goal revised by Le (2026-10-31):** derive the actual asymptotic constant,
whatever the computation gives. Chen's conjectured constants remain a
comparison rather than a required answer. See [PROJECT-GOAL.md](PROJECT-GOAL.md).

**Current internal result (2026-10-31):** the correct-scale full upper is
retained. An independently reviewed proof now identifies the original
second-moment limit for all admissible dimensions/covariances by an explicit
intrinsic positive-control variational constant. Scientific source40ec9a9
passed19checks/HIGH; see the [proof](notes/physical-signed-positive-score-comparison.md).

Further constant simplification and bounds are in progress. The tracked
[TeX/PDF notes](notes/notes_stratonovich_ham_second_moment.pdf) are the earlier
baseline; the new result has not yet been integrated there. Earlier failed
cold-read records remain preserved, and no whole-paper or circulation
clearance is implied. The official private Lean companion remains separately
gated. Use `Progress.md` and the root loader `HANDOFF.md` for the active checkout.

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