# Stratonovich Waves Driven by Space-Time Gaussian Noise

*Second Moment and Exact Asymptotics*

[![Version 1.0.0](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![Text: CC BY 4.0](https://img.shields.io/badge/text-CC%20BY%204.0-lightgrey)](LICENSE)
[![Code: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-lightgrey)](LICENSES/Apache-2.0.txt)

> To make new mathematics found with AI as trustworthy as mathematics proved
> by hand: every step open, every check recorded, every contributor credited.

This repository holds a research project in stochastic partial differential
equations, developed by Le Chen (Auburn University) with Amy, his AI research system,
together with its **complete development history**. It is published so that
mathematicians can study how the work was actually done, check the results,
and help interpret them.

**Contents:**
[The mathematics](#the-mathematics) ·
[What is established, and what is not](#what-is-established-and-what-is-not) ·
[How you can help](#how-you-can-help) ·
[How this was built](#how-this-was-built) ·
[AI use](#ai-use) ·
[Documents in this repository](#documents-in-this-repository) ·
[License and citation](#license-and-citation)

## The mathematics

We study the hyperbolic Anderson model, the stochastic wave equation
$\partial_t^2 u = \Delta u + u\,\dot W$ in dimensions one to three, with initial
data $(1,0)$, in the Stratonovich sense. The Gaussian noise has temporal
covariance $|s-t|^{-\alpha_0}$ and a homogeneous spatial covariance of order
$\alpha$. The paper identifies the large-time behaviour of the second moment at
the scale $t^{\kappa}$, $\kappa = (4-\alpha-\alpha_0)/(3-\alpha)$, with an
intrinsic constant given by an explicit variational formula.

| Read | Where |
| --- | --- |
| Reading edition (<!--s:pages.reader-->28<!--/s--> pages) | [`notes/notes_stratonovich_ham_second_moment_reader.pdf`](notes/notes_stratonovich_ham_second_moment_reader.pdf) |
| Technical notes (<!--s:pages.book-->388<!--/s--> pages) | [`notes/notes_stratonovich_ham_second_moment.pdf`](notes/notes_stratonovich_ham_second_moment.pdf) |
| arXiv | The identifier is added here after posting. |

## What is established, and what is not

Please read this before citing anything.

- The proofs are written out in full. Part I (the reading edition) has not
  yet been checked line by line by a human reader.
- The technical notes have been reviewed by AI systems from several model
  families. The latest whole-paper review returned *pass with notes* at
  **medium** confidence and is **not accepted** under the project's own
  standard, which requires high confidence.
- A Lean companion formalizes some results in full under the manuscript's
  own hypotheses. For others it proves every conclusion, or checks steps,
  with the analytic inputs entering as explicit hypotheses. Most of the main
  theorems are outside Lean: <!--s:lean.outside_main_words-->three<!--/s--> of the <!--s:main.count_words-->four<!--/s-->; for the fourth, Lean proves a
  narrower conclusion. [VERIFICATION.md](VERIFICATION.md) says, result by
  result, what Lean covers. See the companion at
  https://github.com/chenle02/stratonovich-ham-second-moment-lean and its
  statement ledger. The correspondence between Lean and the manuscript was
  reviewed by AI, not by a human reader.
- **No AI review grade is a proof.** Human verification is recorded,
  result by result, in [VERIFICATION.md](VERIFICATION.md).

## How you can help

- **Check a result.** Pick a row in [VERIFICATION.md](VERIFICATION.md), check
  it, and open a pull request that changes that row and says exactly what you
  checked.
- **Report a gap or an error.** Open an issue with the result's label.
- **Discuss interpretation.** Use GitHub Discussions.
- **Formalize.** See the Lean companion's contributor guide and its work
  packages.

Credit is set out in advance in [CONTRIBUTING.md](CONTRIBUTING.md): every
merged contribution is acknowledged by name, and substantial contributions
lead to coauthorship.

## Video introduction

An eleven-episode video introduction to the book is on YouTube:
<https://www.youtube.com/playlist?list=PLWiXjeUrQ62k>. Each episode runs about
twenty minutes with a synthetic voice and follows the book chapter by chapter;
the book's guide to the proof lists what each episode covers, and the badges
in its Figure 1.2 link to the episodes.

Le Chen made the series with Amy. She drafted the scripts and the Manim
animations from the book; every displayed formula is copied from the
statement carrying its label and checked by script, the narration was checked
to be exactly the script, and each script was reviewed against the manuscript
by a model family different from the one that drafted it. Episodes 1-10 follow
the draft at version `38d67ec` and episode 11 (Chapter 12) the draft at
`0f553e08`, so theorem numbers in them may differ from later versions. The
videos explain the argument; they are not part of it or of its review. They
were built in a separate repository, which is not public.

## How this was built

[HOW-THIS-WAS-BUILT.md](HOW-THIS-WAS-BUILT.md) is a guided tour of the
development history: the workflow, the reviewer model families, the routes
that failed, and where to look in the record. Some material was removed from
the published history (other authors' copyrighted texts, private
infrastructure details, collaborators' unpublished work, and private planning
notes); [REDACTIONS.md](REDACTIONS.md) lists every class of removal with its
reason and counts.

The book's Appendix E, "The AI work in numbers", counts the work from this
record: tokens and sessions by model family, every review run and its
outcome, the failed approaches, and a day-by-day timeline with 14 milestones.
Every number is rebuilt by the scripts in
[`scripts/ai-statistics/`](scripts/ai-statistics/). The milestones are listed
in [`scripts/ai-statistics/milestones.json`](scripts/ai-statistics/milestones.json)
and tagged in this repository (`m01-project-set-up` … `m14-lean-gates-closed`),
so `git checkout m05-goal-revised` shows the project as it stood that day.

## AI use

Amy, Le Chen's AI research system, developed the mathematics: the models
working within her drafted the proofs, the LaTeX source and the bookkeeping.
Le Chen's role was to drive the work: choosing the problem, setting and
revising the goals, deciding which approaches to pursue or abandon, choosing
the reviewers and deciding which results to keep.

Amy is model-agnostic: a research operating system (workflows and standing
rules, plus a research knowledge base of bibliography, reference library,
curated arXiv sources and an SPDE wiki) within which any capable language
model can work. Here models from several families worked within her:
Anthropic Claude, OpenAI GPT through Codex, DeepSeek and Kimi. Reviews are
always recorded with the reviewer's model family, because a review counts
only when that family differs from the author's.

Amy is not an author: Le Chen takes full responsibility for the content. The
paper's AI-use statement gives details.

## Documents in this repository

| File | What it holds |
| --- | --- |
| [VERIFICATION.md](VERIFICATION.md) | Human verification, result by result, and what Lean covers |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute, and how credit is given |
| [HOW-THIS-WAS-BUILT.md](HOW-THIS-WAS-BUILT.md) | A guided tour of the development history |
| [AI-USE-STATEMENT.md](AI-USE-STATEMENT.md) | Statement on the use of AI |
| [REDACTIONS.md](REDACTIONS.md) | Every class of removal from the published history, with its reason and counts |
| [VERSIONING.md](VERSIONING.md) | How version numbers are assigned |
| [CHANGELOG.md](CHANGELOG.md) | What changed in each version |
| [CITATION.cff](CITATION.cff) | Citation metadata |

## License and citation

- Text and manuscript: CC BY 4.0 ([`LICENSE`](LICENSE)). Scripts and Lean code:
  Apache-2.0 ([`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt)).
- Cite the paper and this repository; see [`CITATION.cff`](CITATION.cff). The
  arXiv identifier and the Zenodo DOI of the release are added after posting.
