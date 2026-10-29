# Article-Stratonovich-HAM-Second-Moment

The second moment of the Stratonovich hyperbolic Anderson model with noise
fractional in time: an upper bound at the correct scale
t^{(4−α−α₀)/(3−α)} and the sharp p = 2 constant, building on X. Chen,
*Time-dependency in hyperbolic Anderson models: Stratonovich regime*
(author version, submitted to AAP; arXiv:2510.01412).

**Status (2026-10-29):** the full target-scale upper-bound argument and its
independent mild-solution construction passed a fresh 19-check source-bound
review at high confidence, with complete required source delivery. Final
whole-paper cold clearance remains open. The sharp second-moment constant
is unproved, and the private Lean companion has not been created.

The current [92-page notes](notes/notes_stratonovich_ham_second_moment.pdf)
state the full upper bound in Theorem 13.8 on page 87 and the independent
construction in Proposition 3.6 on page 13. All nine minor findings are
adjudicated in `reviews/2026-10-29-mild-construction/adjudication-v1.md`.
Resume from `HANDOFF.md`; a new blind read of the final bytes is next.
All five earlier cold reports remain NOT CLEAR for their respective sources.

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