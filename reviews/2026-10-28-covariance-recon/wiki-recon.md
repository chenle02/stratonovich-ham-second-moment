# Wiki recon and retained references

Le2026-10-28: whenever helpful references are missing from the six-repository
corpus,enqueue them for future use;do not omit SPDEs-wiki recon. This standing
instruction is now in project AGENTS.md.

## Actual recon and its limits

Initial project-page reading and raw filename/text/bibliography search preceded
the external cone search. The full synthesized CLI search/cite pass was done
after Le's steering. This was an application miss of the existing wiki-first
rule,not a new missing policy. The next recon starts with CLI search/cite and
reading the returned pages,before web/librarian work.

The default Python CLI lacked frontmatter. Process-local uv with the declared
click/python-frontmatter/PyYAML dependencies ran the actual queries. No global
installation/editor/service configuration changed. Exact5query output is in
wiki-cli-recon.json. Broad multiword queries gave irrelevant RMT hits;author
filters and exact citekeys retrieved the intended HAM sources.

Synthesized pages actually consulted:
- projects/stratonovich-ham-second-moment: accepted versus candidate scope and
  the uniform-pairing no-go;the page's31page-era status needs the prepared update.
- concepts/hyperbolic-anderson-model and spatially-homogeneous-noise: solution
  concept split,spectral Hilbert spaces,Laplace rather than direct heat-style FK.
- concepts/curved-angular-covariance-noise: its curvature gain changes to a
  non-homogeneous angular,white-time,additive model;not an input to this target.
- insights/four-fold-pairing-classes-preserve-anisotropic-moment-bounds: a
  random-matrix dependence-orbit mechanism,not a HAM estimate.
- papers/balan-22-stratonovich: Poisson/random-flight method provenance,but
  its d<=2 and alpha<1 spectral scope cannot supply the missing d3 result.
- papers/chen_hu-25-hyperbolic: exact static coefficient/Laplace roles and
  a separate published white-noise constant warning;no disputed value used.
- papers/chen-25-time-dependency: current-author/v1 distinction,one-chain
  ordering obstacle and two-chain question. Its printed first-moment constants
  still need the later normalization qualification from this Article audit.
- papers/chen-23-exponential: finite square-root variational input and the
  correct DOI/body identity needed by the static endpoint.

The Chen2023 page also points to a deterministic quartic form bound. Root
checked the actual pinned p2 image: Theorem1.1 says the variation in(1.5)
is finite. On real unit-L2 Schwartz profiles this gives a finite bound for
Q(f)-(1/2)||grad f||²;normalization gives the corresponding quartic estimate
for arbitrary Schwartz profiles. This is a concrete input for the next
physical-measure/Fourier energy-identification lemma,not a new source theorem.
The spatially-homogeneous-noise concept uses a different Fourier convention;
constants must continue to come from the pinned primary source.

This is useful method/scope recon,not a replacement for reading exact primary
theorem hypotheses. No matching cone-representation theorem was found in the
local wiki for arbitrary d3 covariance and real alpha in(1,2).

## Enqueued references

Four ordinary nonblocking priority5 paper tickets,using verified published
DOIs and idempotent UIDs,are recorded in reference-queue.json. Exact remote
request/claimed IDs and DOI fields were verified,without prefix globs, in
exact-ticket-state.json and queue-verification.json. One was claimed and three
were pending at the observed snapshot;no completed-ingestion claim is made.
No force,wake,service restart or source-author contact was used.

The initial repo-queue checks with raw arXiv IDs were not comprehensive:
the command is citekey/exact-DOI based. Before enqueue,canonical DOI checks,
predicted-key checks and canonical author/title inventories were performed;
Papis metadata was separately searched by title/arXiv. No matching records
were found. Queue check's five addressable layers are not a six-layer Papis
lookup by themselves.

## Primary-source leads and applicability boundaries

- Milman, Generalized Intersection Bodies,JFA240(2),530--567(2006),
  DOI10.1016/j.jfa.2006.04.004,arXivmath/0512058v2: covariance-cone structure
  and ellipsoid/radial-sum approximation background. Not imported here.
- Milman, Generalized Intersection Bodies are not Equivalent,Adv.Math217(6),
  2822--2840(2008),DOI10.1016/j.aim.2007.11.007,arXivmath/0701779v2:
  that version's Theorem1.1/Corollary5.5 require n>=4 and integer2<=k<=n-2.
  Its final paragraph suggests a noninteger extension but does not prove one.
  Hence it neither proves representation nor supplies a no-go for our
  n=3,real1<alpha<2 case. No ellipsoid-density shortcut is adopted.
- Rubin, Intersection Bodies and Generalized Cosine Transforms,Adv.Math218(3),
  696--727(2008),DOI10.1016/j.aim.2008.01.011,arXiv0704.0061v2: real-parameter
  cosine transforms/positive-definite homogeneous distributions are a relevant
  next source;exact application hypotheses remain to be checked.
- Frank--Mateu--Mora--Rondi--Scardia--Verdera,Explicit minimisers for anisotropic
  Riesz energies,Calc.Var65,34(2026),DOI10.1007/s00526-025-03185-1,
  arXiv2504.11644v2: angular Fourier positivity/degeneracy tools. Its quadratic-
  confinement probability-measure minimizer is a different functional from
  the square-root Sobolev/gradient M in this project. No constants are borrowed.

Official publisher/arXiv identities were checked. This bounded recon used
abstract/metadata plus Milman's HTML/PDF text for the exact range;it did not
reprove those papers or establish their use as an SPDE theorem. Nothing here
changes the original full goal or source-normalization disposition.
