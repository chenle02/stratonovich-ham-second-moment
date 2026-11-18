# Changelog

Versions follow [VERSIONING.md](VERSIONING.md): MAJOR is a new arXiv version,
MINOR changes the mathematics but not the statement of any main theorem, and
PATCH changes no mathematics. Results are named by label; labels do not change
between versions, numbers may.

## 1.0.2 — <!--s:release.date-->2026-11-18<!--/s-->

Patch release: no mathematics changed.

- **arXiv:** the book is arXiv:2611.23014. The imprint page links it,
  `CITATION.cff` gives it as the preferred citation, the README links it, and
  `.zenodo.json` records that the deposit supplements it.
- **Book site:** the README and `CITATION.cff` (`url`) link the book's site,
  <https://chenle02.github.io/stratonovich-ham-second-moment/>.
- **Version and date** on the title page, the imprint and the reading edition,
  and the release links in the preface, Appendix G and the AI-use statement,
  now name 1.0.2.

## 1.0.1 — 2026-11-17

Patch release: no mathematics changed.

- **Episode 10:** the link in the book's episode table now points to the
  replacement video `hQYXmznXji8`; the earlier upload is unlisted.
- **Archiving:** a `.zenodo.json` gives Zenodo the deposit metadata (one
  deposit licence, CC BY 4.0, for the text and manuscript; the scripts and
  Lean code stay Apache-2.0). Release 1.0.0 was not archived, because Zenodo
  could not read the two licences listed in `CITATION.cff`.
- **Records:** the README and HOW-THIS-WAS-BUILT.md now count the 15
  milestones that the book's Appendix E draws (`m01` … `m15`).
- **Version and date** on the title page, the imprint and the reading edition,
  and the release links in the preface, Appendix G and the AI-use statement,
  now name 1.0.1.

## 1.0.0 — 2026-11-16

First public release: the book, its reading edition and the complete
development history.

- **Main theorems:** `T:full-upper` (full upper scale),
  `T:intrinsic-second-moment` (intrinsic original second-moment constant),
  `T:intrinsic-occupation-ceiling` (the computed occupation ceiling) and
  `T:white-moment-bounds` (explicit white moment bounds).
- **Size:** technical notes <!--s:pages.book-->476<!--/s--> pages, with <!--s:chapters-->12<!--/s--> chapters and appendices <!--s:appendices.letters-->A–G<!--/s-->;
  reading edition <!--s:pages.reader-->28<!--/s--> pages; <!--s:results-->220<!--/s--> numbered results and <!--s:nogo-->33<!--/s--> numbered no-go
  results (Chapter 12), each listed with its check status in
  [VERIFICATION.md](VERIFICATION.md); <!--s:proofs-->249<!--/s--> proofs written in this project.
- **Lean:** the companion's release v0.10.0 (DOI 10.5281/zenodo.24295453; commits
  <!--s:lean.coverage-->`6e83b60`<!--/s--> for coverage, <!--s:lean.verified-->`c8d8e07`<!--/s--> verified) records <!--s:lean.full-->60<!--/s--> results formalized under the manuscript's own
  hypotheses (<!--s:lean.narrow-->16<!--/s--> with a narrower conclusion) and steps or parts of <!--s:lean.inputs-->35<!--/s--> more,
  with named analytic inputs supplied. Two of
  the four main theorems are outside Lean; for `T:intrinsic-occupation-ceiling`
  and `T:white-moment-bounds` Lean proves a narrower conclusion, for the second
  with analytic inputs supplied.
- **How it was made:** see [HOW-THIS-WAS-BUILT.md](HOW-THIS-WAS-BUILT.md) and
  [AI-USE-STATEMENT.md](AI-USE-STATEMENT.md).
