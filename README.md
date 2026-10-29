# Article-Stratonovich-HAM-Second-Moment

The second moment of the Stratonovich hyperbolic Anderson model with noise
fractional in time: an upper bound at the correct scale
t^{(4−α−α₀)/(3−α)} and the sharp p = 2 constant, building on X. Chen,
*Time-dependency in hyperbolic Anderson models: Stratonovich regime*
(author version, submitted to AAP; arXiv:2510.01412).

**Status (2026-10-29):** the full target-scale upper bound is written for the
original covariance class in dimensions one, two and three, and has passed
source-bound cross-family correctness review. The final whole-paper cold
read remains open. The sharp second-moment constant is unproved, and the
private Lean companion has not been created. See `Progress.md` for exact
review scope, source qualifications and remaining gates.

The current [86-page notes](notes/notes_stratonovich_ham_second_moment.pdf)
state the upper bound in Theorem 13.8 on page 81. Resume from `HANDOFF.md`;
the next step is the fresh blind read of the final proof bytes.

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