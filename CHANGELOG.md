# Changelog

Versions follow [VERSIONING.md](VERSIONING.md): MAJOR is a new arXiv version,
MINOR changes the mathematics but not the statement of any main theorem, and
PATCH changes no mathematics. Results are named by label; labels do not change
between versions, numbers may.

## 1.0.3 — <!--s:release.date-->2026-11-20<!--/s-->

Patch release: no mathematics changed.

- **Citation metadata:** the `message` in `CITATION.cff` no longer says the
  paper's arXiv citation "is added after posting"; it names the arXiv preprint
  arXiv:2611.23014 and the Zenodo DOI 10.5281/zenodo.24342309 (all versions).
- **Wording:** the README says that the spatial covariance is homogeneous of
  order $-\alpha$, as in the book and the arXiv abstract (it said "of order
  $\alpha$").
- **Changelog record:** the 1.0.2 entry gives its version DOI,
  10.5281/zenodo.24371883.
- **Lean records:** `lean-progress/` records the approval and launch of the
  Lean companion's wave L15 (the companion's own release is unchanged,
  v0.10.0).
- **Version and date** on the title page, the imprint and the reading edition,
  and the release links in the preface, Appendix G and the AI-use statement,
  now name 1.0.3.
- **Contributors:** Le Chen, with Amy (his AI research system); no outside
  contributions. **Verification ledger:** no status changed.
- **Archive:** tag `v1.0.3`; Zenodo, all versions:
  [10.5281/zenodo.24342309](https://doi.org/10.5281/zenodo.24342309) (the
  version DOI of 1.0.3 is assigned on release).

## 1.0.2 — 2026-11-18

Patch release: no mathematics changed.

- **arXiv:** the book is arXiv:2611.23014. The imprint page links it,
  `CITATION.cff` gives it as the preferred citation, the README links it, and
  `.zenodo.json` records that the deposit supplements it.
- **Zenodo DOI:** the releases are archived on Zenodo, DOI
  10.5281/zenodo.24342309 (all versions; v1.0.1 is 10.5281/zenodo.24342310).
  The imprint page and the README link it, and `CITATION.cff` gives it as
  `doi`.
- **Book site:** the README and `CITATION.cff` (`url`) link the book's site,
  <https://chenle02.github.io/stratonovich-ham-second-moment/>.
- **Version and date** on the title page, the imprint and the reading edition,
  and the release links in the preface, Appendix G and the AI-use statement,
  now name 1.0.2.
- **Contributors:** Le Chen, with Amy (his AI research system); no outside
  contributions. **Verification ledger:** no status changed.
- **Archive:** tag `v1.0.2`; Zenodo
  [10.5281/zenodo.24371883](https://doi.org/10.5281/zenodo.24371883) (all
  versions: [10.5281/zenodo.24342309](https://doi.org/10.5281/zenodo.24342309)).

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
- **Redactions record:** `REDACTIONS.md` states its commit counts as those
  of the first publication (v1.0.0); later releases state theirs in their
  commit-map commit, because the published history is append-only.
- **Version and date** on the title page, the imprint and the reading edition,
  and the release links in the preface, Appendix G and the AI-use statement,
  now name 1.0.1.
- **Contributors:** Le Chen, with Amy (his AI research system); no outside
  contributions. **Verification ledger:** no status changed.
- **Archive:** tag `v1.0.1`; Zenodo
  [10.5281/zenodo.24342310](https://doi.org/10.5281/zenodo.24342310), the
  first archived release.

## 1.0.0 — 2026-11-16

First public release: the book, its reading edition and the complete
development history.

- **Main theorems:** `T:full-upper` (full upper scale),
  `T:intrinsic-second-moment` (intrinsic original second-moment constant),
  `T:intrinsic-occupation-ceiling` (the computed occupation ceiling) and
  `T:white-moment-bounds` (explicit white moment bounds).
- **Size:** technical notes 476 pages, with 12 chapters and appendices A–G;
  reading edition 28 pages; 220 numbered results and 33 numbered no-go
  results (Chapter 12), each listed with its check status in
  [VERIFICATION.md](VERIFICATION.md); 249 proofs written in this project.
- **Lean:** the companion's release v0.10.0 (DOI 10.5281/zenodo.24295453; commits
  `6e83b60` for coverage, `c8d8e07` verified) records 60 results formalized under the manuscript's own
  hypotheses (16 with a narrower conclusion) and steps or parts of 35 more,
  with named analytic inputs supplied. Two of
  the four main theorems are outside Lean; for `T:intrinsic-occupation-ceiling`
  and `T:white-moment-bounds` Lean proves a narrower conclusion, for the second
  with analytic inputs supplied.
- **How it was made:** see [HOW-THIS-WAS-BUILT.md](HOW-THIS-WAS-BUILT.md) and
  [AI-USE-STATEMENT.md](AI-USE-STATEMENT.md).
- **Contributors:** Le Chen, with Amy (his AI research system); no outside
  contributions. **Verification ledger:** first public version.
- **Archive:** tag `v1.0.0` (commit `643d1dcc8911`); not archived on
  Zenodo (see 1.0.1).
