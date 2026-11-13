# Changelog

Versions follow [VERSIONING.md](VERSIONING.md): MAJOR is a new arXiv version,
MINOR changes the mathematics but not the statement of any main theorem, and
PATCH changes no mathematics. Results are named by label; labels do not change
between versions, numbers may.

## 1.0.0 — 2026-12-01

First public release: the book, its reading edition and the complete
development history.

- **Main theorems:** `T:full-upper` (full upper scale),
  `T:intrinsic-second-moment` (intrinsic original second-moment constant),
  `T:intrinsic-occupation-ceiling` (the computed occupation ceiling) and
  `T:white-moment-bounds` (explicit white moment bounds).
- **Size:** technical notes 386 pages, with 12 chapters and appendices A–G;
  reading edition 28 pages; 220 numbered results and 33 numbered no-go
  results (Chapter 12), each listed with its check status in
  [VERIFICATION.md](VERIFICATION.md); 249 proofs written in this project.
- **Lean:** the companion's coverage at its commit `34b65d7` (verified commit
  `6eb79c7`) records 43 results formalized under the manuscript's own
  hypotheses (18 with a narrower conclusion) and steps or parts of 30 more,
  with named analytic inputs supplied. Three of
  the four main theorems are outside Lean; for `T:intrinsic-occupation-ceiling`
  Lean proves a narrower conclusion.
- **How it was made:** see [HOW-THIS-WAS-BUILT.md](HOW-THIS-WAS-BUILT.md) and
  [AI-USE-STATEMENT.md](AI-USE-STATEMENT.md).
