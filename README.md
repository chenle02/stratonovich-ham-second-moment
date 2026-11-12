# Stratonovich Waves Driven by Space-Time Gaussian Noise

*Second Moment and Exact Asymptotics*

> To make new mathematics found with AI as trustworthy as mathematics proved
> by hand: every step open, every check recorded, every contributor credited.

This repository holds a research project in stochastic partial differential
equations, developed by Le Chen (Auburn University) with Amy, his AI research system,
together with its **complete development history**. It is published so that
mathematicians can study how the work was actually done, check the results,
and help interpret them.

## The mathematics

We study the hyperbolic Anderson model, the stochastic wave equation
$\partial_t^2 u = \Delta u + u\,\dot W$ in dimensions one to three, with initial
data $(1,0)$, in the Stratonovich sense. The Gaussian noise has temporal
covariance $|s-t|^{-\alpha_0}$ and a homogeneous spatial covariance of order
$\alpha$. The paper identifies the large-time behaviour of the second moment at
the scale $t^{\kappa}$, $\kappa = (4-\alpha-\alpha_0)/(3-\alpha)$, with an
intrinsic constant given by an explicit variational formula.

- Reading edition (28 pages): `notes/notes_stratonovich_ham_second_moment_reader.pdf`
- Technical notes (386 pages): `notes/notes_stratonovich_ham_second_moment.pdf`
- arXiv: the identifier is added here after posting.

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
  theorems are outside Lean: three of the four; for the fourth, Lean proves a
  narrower conclusion. VERIFICATION.md says, result by result, what
  Lean covers. See the companion at
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
Every number is rebuilt by the scripts in `scripts/ai-statistics/`. The
milestones are listed in `scripts/ai-statistics/milestones.json` and tagged
in this repository (`m01-project-set-up` … `m14-lean-gates-closed`), so
`git checkout m05-goal-revised` shows the project as it stood that day.

## AI use

Amy, Le Chen's AI research system, developed the mathematics: the models
working within her drafted the proofs, the LaTeX source and the bookkeeping.
Le Chen's role was to drive the work: choosing the problem, setting and
revising the goals, deciding which approaches to pursue or abandon, choosing
the reviewers and deciding which results to keep. Amy is model-agnostic: a
research operating system (workflows and standing rules, plus a research
knowledge base of bibliography, reference library, curated arXiv sources and
an SPDE wiki) within which any capable language model can work. Here models
from several families worked within her: Anthropic Claude, OpenAI GPT
through Codex, DeepSeek and Kimi. Reviews are always recorded with the
reviewer's model family, because a review counts only when that family
differs from the author's. Amy is not an author: Le Chen takes full
responsibility for the content. The paper's AI-use statement gives details.

## License and citation

- Text and manuscript: CC BY 4.0 (`LICENSE`). Scripts and Lean code:
  Apache-2.0 (`LICENSES/Apache-2.0.txt`).
- Cite the paper and this repository; see `CITATION.cff`. The arXiv
  identifier and the Zenodo DOI of the release are added after posting.
