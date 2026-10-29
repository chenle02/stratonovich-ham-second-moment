# Article-Stratonovich-HAM-Second-Moment

The second moment of the Stratonovich hyperbolic Anderson model with noise
fractional in time: an upper bound at the correct scale
t^{(4−α−α₀)/(3−α)} and the sharp p = 2 constant, building on X. Chen,
*Time-dependency in hyperbolic Anderson models: Stratonovich regime*
(author version, submitted to AAP; arXiv:2510.01412).

**Status (2026-10-29):** the preceding quantitative upper-bound and mild
construction passed 19 source-bound checks at high confidence. The sixth
cold read remains NOT CLEAR and requests a proof-level fixed-order-input
check plus explicit hypothesis/object statements.

The current [94-page revision](notes/notes_stratonovich_ham_second_moment.pdf)
makes the original covariance class and canonical solution explicit and adds
a direct norm-and-tail lemma. That new lemma is unreviewed; the spatial
Wick-measure and joint-limit construction lemmas remain to implement.
The full upper statement is Theorem 13.8 on page 89. See `Progress.md` and
`HANDOFF.md`. The sharp constant and private Lean companion remain open.

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