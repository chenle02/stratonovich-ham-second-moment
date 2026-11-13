# Changelog

Versions follow [VERSIONING.md](VERSIONING.md): MAJOR is a new arXiv version,
MINOR changes the mathematics but not the statement of any main theorem, and
PATCH changes no mathematics. Results are named by label; labels do not change
between versions, numbers may.

## 1.0.0 — <!--s:release.date-->2026-11-13<!--/s-->

First public release: the book, its reading edition and the complete
development history.

- **Main theorems:** `T:full-upper` (full upper scale),
  `T:intrinsic-second-moment` (intrinsic original second-moment constant),
  `T:intrinsic-occupation-ceiling` (the computed occupation ceiling) and
  `T:white-moment-bounds` (explicit white moment bounds).
- **Size:** technical notes <!--s:pages.book-->391<!--/s--> pages, with <!--s:chapters-->12<!--/s--> chapters and appendices <!--s:appendices.letters-->A–G<!--/s-->;
  reading edition <!--s:pages.reader-->28<!--/s--> pages; <!--s:results-->220<!--/s--> numbered results and <!--s:nogo-->33<!--/s--> numbered no-go
  results (Chapter 12), each listed with its check status in
  [VERIFICATION.md](VERIFICATION.md); <!--s:proofs-->249<!--/s--> proofs written in this project.
- **Lean:** the companion's release v0.9.0 (DOI 10.5281/zenodo.24199105; development commits
  <!--s:lean.coverage-->`34b65d7`<!--/s--> for coverage, <!--s:lean.verified-->`6eb79c7`<!--/s--> verified) records <!--s:lean.full-->43<!--/s--> results formalized under the manuscript's own
  hypotheses (<!--s:lean.narrow-->18<!--/s--> with a narrower conclusion) and steps or parts of <!--s:lean.inputs-->30<!--/s--> more,
  with named analytic inputs supplied. Three of
  the four main theorems are outside Lean; for `T:intrinsic-occupation-ceiling`
  Lean proves a narrower conclusion.
- **How it was made:** see [HOW-THIS-WAS-BUILT.md](HOW-THIS-WAS-BUILT.md) and
  [AI-USE-STATEMENT.md](AI-USE-STATEMENT.md).
