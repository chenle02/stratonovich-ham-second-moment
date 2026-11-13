# How this repository was built

This guide is for mathematicians who want to study how an AI-assisted research
project was actually carried out. It assumes no knowledge of the tooling. It
summarizes the longer record in `AI-DEV-HISTORY.md`. Where the two differ, the
longer record and the original files win.

## 1. What this repository is

The project studies the Stratonovich hyperbolic Anderson model: a stochastic
wave equation with multiplicative Gaussian noise that is fractional in time
(exponent α₀) and homogeneous in space (scaling exponent α), in dimensions
d = 1, 2, 3, with initial data (1, 0). The question is how fast the second
moment E u(t,x)² grows. The source paper on this model (X. Chen) gives the
crude bound E u² ≤ exp(C t²). The project has two goals. First, prove an upper
bound at the scale t^κ, with κ = (4 − α − α₀)/(3 − α). Second, prove that
t^(−κ) log E u²(t,x) has a limit and identify that limit as an intrinsically
defined constant, given by a fully specified variational formula. The work
was done with AI systems under the direction of Le Chen (the PI), who set the
goals, made the decisions and changed direction when needed.

**Size of the record at manuscript revision `cc2a43d`:**
- **Technical notes:** 386 pages, with 12 chapters and 7 appendices (A–G).
  Chapter 12, "Obstructions and failed approaches", states 33 numbered no-go
  results with proofs.
- **Reading edition:** 28 pages.
- **Results:** 220 numbered results (8 theorems, 93 propositions, 106
  lemmas, 13 corollaries) and the 33 no-go results of Chapter 12, each
  listed in `VERIFICATION.md`.
- **Proofs:** 249 proofs were written in this project: 216 for numbered
  results and 33 for the no-go results of Chapter 12. The other four numbered
  results either restate the source paper (`T:first`, `T:crude`) or are
  the introduction's statements of theorems proved later
  (`T:intro-upper`, `T:intro-second-moment`).

## 2. How the work was organized

### Amy

**Amy**, Le Chen's AI research system, developed the mathematics: the models
working within her drafted the proofs, the LaTeX source and the bookkeeping.
Le Chen's role was to drive the work: choosing the problem, setting and
revising the goals, deciding which approaches to pursue or abandon, choosing
the reviewers and deciding which results to keep. Amy is not a model. She is
a model-agnostic research operating system, a harness that any capable
language model can be plugged into. (The name began as a
typo for "my AI Army" in an email to a coauthor.) She consists of:

- **Workflows and standing rules** (the Le-AI-Lab skills, commands and
  governance): how a round is run, how reviews are dispatched, what counts
  as evidence, and when to stop.
- **A six-part research knowledge base**: a master bibliography, a reference
  library, a PDF collection, curated arXiv LaTeX sources, a retrieval index,
  and an SPDE wiki, kept in step by a single queue.
- **Interfaces for the models that work within her.** In this project,
  models from several families worked within Amy: Anthropic Claude, OpenAI GPT
  through Codex, DeepSeek and Kimi. The same workflows run whichever model
  is plugged in, which is also what makes cross-family review possible.

Wherever independence matters, this record names the model family, not just
"Amy": a review only counts when its model family differs from the author
of the work under review. Amy is a tool. She is never an author; Le Chen
drives the work and takes full responsibility for the results.

### Roles

- **The PI (Le Chen)** set and revised the objective, approved or rejected
  changes of direction, and decided which reviewers to use.
- **Worker models** wrote the mathematics, the LaTeX and the bookkeeping. The
  main worker was a GPT-family model running in Codex. Other models did some
  editorial and auditing tasks.
- **Reviewer models** checked the work. A review had to come from a different
  model family than the author of the argument it checked. Earlier rounds used
  Claude (Opus) reviewers. From November 1 the PI designated DeepSeek V4 Pro
  and Kimi-K3, with DeepSeek V4 Pro as the main reviewer. Later checks of the
  Lean ledger used a Codex GPT model.

### Review gates

Each round that added a proof froze a "review packet": the exact source files,
their hashes and the questions asked. The reviewer returned a report. The
worker then wrote an adjudication: a response to every finding, recorded in
`Progress.md`. Raw reports were kept unchanged, including reports with format
errors.

The project used these gates:

- **Independent cross-family review.** Described above.
- **Confidence levels.** Each review states its own confidence: LOW, MEDIUM or
  HIGH. This is the reviewer's statement of how sure it is, given what it
  actually read and checked. The completion contract required HIGH. A MEDIUM
  report with no errors found is therefore not enough.
- **"Unaccepted".** A result is "unaccepted" when its review did not meet the
  contract (for example, MEDIUM confidence, or incomplete coverage). It does
  not mean an error was found. It means the procedure did not certify it.
- **Visual checks.** Rendered PDF pages were checked against the source, page
  by page, to catch typesetting errors that change mathematics. This is
  separate from proof review.
- **Final cold read.** A fresh session, independent of the authors of the
  proof and of earlier reviewers, reads the finished paper. This gate has not
  started.
- **Calibrations.** Every proposed bound had to pass fixed sanity checks: the
  limit α₀ → 0 must recover the known time-independent exponent; the result
  must be consistent with the first-moment results as stated in their sources;
  and Jensen's inequality E u² ≥ (E u)² must hold.
- **Clean build.** Every LaTeX change had to compile with zero errors, zero
  undefined references and zero overfull boxes before it was committed.

Rule adopted after experience: a review may not be re-run on unchanged source
just to raise MEDIUM to HIGH. A new review needs new evidence or changed text.

### The Lean companion

Lean, a proof assistant, was first used only for finite and algebraic steps:
for example, recurrences, projections and bounds on finite words of
operators. Later waves formalized whole labelled results under the
manuscript's own hypotheses (section 6). Analytic inputs (limits, integration, the stochastic construction) stay as
named hypotheses, listed in `lean-progress/BOUNDARIES.md`. Each Lean fact was
tested with "negative controls": deliberately false statements that must be
rejected. This checks that the formal statement means what the paper means.

## 3. Timeline

The 14 milestones drawn in the book's Appendix E are tagged in this
repository (`m01-project-set-up` … `m14-lean-gates-closed`; dates, commits
and sources in `scripts/ai-statistics/milestones.json`). The account below
follows them.

**October 26–27: fixing the problem.** Careful reading of the source paper
settled two points. The Stratonovich expansion has self-pairings inside a
chain and cross terms between chains of different lengths, so a diagonal-only
expansion cannot give the full second moment. And the author version of the
source proves only two-sided first-moment bounds; an earlier arXiv version
states an exact limit, which may not be cited. A first test (gate "G0") asked
whether the source's universal two-chain integral bound plus counting could
reach the scale t^κ. It could not: the common majorant was too crude. This
ruled out that route, not the theorem.

**October 28–30: routes and framework.** Low-dimensional cases, endpoint cases
and conditional routes were explored. Small white-noise and static examples
served as falsification tests; they do not prove all-order asymptotics. The
upper-bound route that survived used Gaussian phase and operator estimates on
time intervals. Several tempting shortcuts failed and were recorded: scalar
moments cannot be multiplied over time blocks, because the wave equation
carries both displacement and velocity; monotonicity of covariance in an
arbitrary phase is not available; the second-order mean term in the variance
calculation cannot be dropped. A parallel difficulty was to keep the same
stochastic solution throughout: cutoffs, auxiliary randomness and, in
dimension three, the order of the Green operation and noise evaluation all had
to be handled explicitly.

**October 31: deriving the constant instead of matching a prediction.** The
source paper conjectures a value for the constant. The PI revised the goal:
derive whatever constant the computation gives, and treat the conjecture as a
comparison only. An exact, fully specified variational formula counts as a
derived constant. An all-model formula for the second-moment constant was
drafted and accepted at the local (component) review level that day. It is
expressed through an auxiliary first-moment-type score; that score is not shown
to equal the actual first-moment constant.

**November 1–3: integration.** The constant, occupation bounds and an explicit
white-spatial-noise example were integrated into one manuscript. A compact
Young-norm argument and a direct conservation proof produced a 263-page
baseline. Integration showed that checking components is not the same as
checking the whole proof. The first whole-manuscript review ended
INCONCLUSIVE with limited coverage. It found no mathematical defect, but it did
not verify the whole argument either.

**November 4–5: themed review and a reader.** Reviews by theme (foundations,
construction, phase estimates, upper bound, constant, calibration) had
different scopes and confidence levels. Combining positive partial reports does
not produce a whole-paper acceptance. A 20-page reading guide was written; it
is a guide, not a short proof. A 267-page candidate added a self-contained
pairing estimate. Its inventory has 215 proofs written in this project and
263 required review rows (proofs, 13 joins between parts, and 9 global checks).

**November 6–8: review mechanics and diminishing returns.** Much time went to
packet inventories, hashes, provider transport, context limits and report
formats. Some of this was necessary: a review must see the actual source, and
a failed or truncated request is not a review. But repeated rounds on unchanged
text displaced mathematical work. Several whole reports were positive at MEDIUM
confidence, which did not meet the HIGH requirement. Visual checking accepted
230 of 267 pages; 37 remained open. A proposed rule to accept MEDIUM visual
reports was not adopted.

**November 9: Lean connected to the actual objects.** The Lean work moved from
toy algebra to statements about the actual Gaussian objects used in the paper:
the Hermite-coordinate recurrence, Gaussian Hilbert projection with the
source's indexing, and the colored-word estimate with its real operators and
cutoffs. Statement review caught one overly broad index and corrected it. The
accepted local total became 87 facts in 26 groups. These counts are
bookkeeping, not a percentage of the theorem formalized.

**November 9: the last whole review and the stall.** The fifth whole-manuscript
review (DeepSeek V4 Pro) received all operative proofs plus the new Lean
evidence. It returned PASS_WITH_NOTES at MEDIUM confidence: 226 PASS and 37
PASS_WITH_NOTES rows out of 263, with no fatal or major findings and no
required repairs. Separately, 22 rows had a delimiter format error. Neither the
report nor the parser was edited to claim a pass. With no concrete defect left
to repair, but the HIGH, visual and cold-read gates still open, the project
stalled. The PI agreed in conversation on a recovery direction: map claims to
dependencies and evidence, and use qualified human mathematical adjudication as
the final authority, with AI confidence as supporting evidence. That direction
has not yet been written into the project contract.

**After November 9: editorial work.** Later work was editorial and did not
change any proof. A literature review was revised; the PI pointed out an
omitted central reference (Chen–Guo–Song), which was restored. Diagrams were
added (12 in the long text, 7 in the reader); a separate reviewer found four
geometric errors in the first drafts, all corrected. The prose was read in full
for jargon. The long text was reorganized as a book with 11 proof chapters and
4 appendices; alternative and abandoned approaches are kept whole in the
appendices. All 215 proofs keep their mathematics through these changes, and
no earlier review grade was transferred to the new edition.

**Lean ledger review.** A Lean companion was created on the PI's instruction.
- **Reviews:** four successive cross-family reviews (Codex GPT) of the
  correspondence between Lean statements and manuscript labels each failed
  with fatal findings. All the defects were repaired. Earlier reviews of
  the same ledger had missed them.
- **Gate closed:** on November 10 the PI closed the correspondence gate.
  The evidence is the conjunction of a split review that read the whole
  manuscript file and a high-confidence confirmation of the repairs. Its
  scope is AI-checked correspondence, not human verification.
- **Whole results:** later waves formalized whole labelled results under
  the manuscript's own hypotheses.

## 4. Lessons the record supports

- Fix the source edition, the model, the normalizations and the stochastic
  construction before borrowing an asymptotic constant. An attractive formula
  cannot repair a mismatch in the problem.
- Use low-order and degenerate examples early. Record exactly which route a
  failed check excludes. The failure of a bound is not the failure of a model.
- Review the actual joins and uses of lemmas, not only isolated lemmas. Keep
  each review bound to the exact version it read.
- Tie Lean statements to the actual analytic objects, test them with positive
  and negative controls, and state the remaining analytic hypotheses plainly.
- Keep raw independent reports, including their format errors and stated
  uncertainty. Correct factual errors in an adjudication, but do not edit the
  reviewer's confidence.
- Stop re-running confidence-only reviews on unchanged material. Look for a
  concrete gap, ask a qualified human, or change the agreed workflow openly.
- Keep source, PDF, reader and review bindings together. A short reader, a
  matching rendering, a delivery receipt and a proof answer different
  questions.
- Measure progress by closed mathematical obligations and usable exposition.
  A thousand commits and many review packets do not by themselves prove a
  theorem.

### Approaches that did not work

The record of this project holds 42 approaches that did not work: 33
mathematical (18 failed routes and 15 counterexamples or errata), 4 defects
in the source paper, 4 failures of a method or check, and 1 process record.
None of them refutes the target theorem; each closes one route. Chapter 12
of the book states the 33 mathematical ones as numbered no-go results, with
proofs. Patrick
Morris argues in the same direction when he asks for "more accounts of failed
attempts", so that others do not have to repeat them
([*Let's stop writing papers…*](https://proofsandprompts.com/2026/10/30/lets-stop-writing-papers/),
Proofs and Prompts, October 30, 2026). The main mathematical ones, with how
far each reaches:

1. **One estimate for every pairing is too weak.** Using the source's
   Theorem 3.1 with a single bound for every pairing gives the exponent
   ρ = β/(β − 1) > κ, where β = 4 − α − α₀: the order-k term misses a factor
   (k!)^α₀. Only that use of Theorem 3.1 is ruled out. In the book:
   `P:envelope`, `R:G0-verdict`.
2. **Single diagrams cannot each be bounded by (k!)³.** The fully adjacent
   white-noise diagram already exceeds this for every α₀ > 0. A bound on the
   sum of the diagrams was proved later. Reviewed.
3. **The spatial-maximum input fails for rougher covariances.** In d = 2 a
   Riesz covariance with 3/2 ≤ α < 2 makes the shifted Green integral diverge,
   and product covariances have no uniform maximum. This concerns only that
   input, not existence, finiteness of moments or the time scale. In the book:
   `P:higher-obstructions`.
4. **Copying the first-moment Brownian clock to two chains fails.** A shared
   clock with constant correlation undercounts the cross pairs:
   0 < J_ρ ≤ J₁ < K for every nonzero covariance (white-noise check: 0.4431
   against 0.2596). Other clock couplings and other two-clock methods are not
   ruled out. In the book: `P:clock-copy-obstruction`, in the appendix on
   static comparisons and the clock obstruction.
5. **Joining the two chains into one, point by point, fails** on a set of
   positive measure in explicit Riesz and white-noise examples. An integrated
   comparison is a separate question. Reviewed.
6. **Dropping a positive Gaussian remainder can lower the wave mean.** An
   explicit example in d = 1 (Riesz exponent 1/2, a = 99/100) has a gap larger
   than 1/96. Only dropping it unconditionally is ruled out; the large-time
   question stays open. Reviewed at HIGH confidence.
7. **The masked L² Hilbert–Schmidt reconstruction fails in d = 2, 3 for every
   s,** because a trace diverges at high frequency. Other operator frameworks
   are not ruled out. Reviewed: 8 PASS at HIGH confidence.
8. **A physical mask need not preserve tests of zero noise variance**
   (d = 2, Γ = δ₀ ⊗ Lebesgue). In the book: `P:masked-quotient-obstruction`.
9. **Fixed smooth projections give no tail bounds uniform in the radius R.**
   This does not rule out fixed-radius bounds or the sharp upper bound.
   Reviewed.
10. **A whole-space cutoff cannot replace the compact cutoff,** because
    Λ^(−γ) on L²(ℝ^d) is not compact for any γ > 0. In the book:
    `P:cutoff-boundary-tests`.

Practical failures are kept apart from these and are not treated as
mathematical results. `Progress.md` gives a heading to 27 of them: quota and
session limits (5), invalid or prose-wrapped reports (10), transport
failures (2), timeouts (2), refusals before any request was sent (5) and gaps
in image delivery (3). Many smaller ones are mentioned only in passing. A
further 33 sections of the log record a MEDIUM-confidence review that was
therefore not accepted.

## 5. How to read the history

Start with these files, in this order:

1. `STATUS-DIGEST.md`: a one-page summary of the current state and the gate
   board. It is derived; it does not override the files below.
2. `PROJECT-GOAL.md`: the objective and the completion contract, including the
   October 31 revision.
3. `Progress.md`: the workflow authority. Rounds, decisions, failed routes and
   every adjudication, in date order. The last entries give the latest state.
4. `AI-DEV-HISTORY.md`: the longer narrative this guide condenses.
5. `reviews/`: one dated directory per review, with the frozen inputs, the raw
   report and the adjudication. The directory name states the outcome, for
   example `2026-11-09-full-main-v5-kernel-medium-unaccepted/`.
6. `lean-progress/`: the Lean ledger (`PROGRESS.md`), the strategy
   (`ROADMAP.md`) and the analytic boundaries (`BOUNDARIES.md`). Dated
   additions in the ledger supersede its older summary paragraphs.
7. `history/git-history.tsv`: the full commit chronology up to the November 9
   checkpoint, with dates and subjects.
8. `scripts/ai-statistics/`: the scripts and data behind the book's
   Appendix E (tokens, review runs, failed approaches, the milestones). They
   rebuild every number from the files above.

To see a manuscript as it was on a given date, use
`git show <commit>:notes/notes_stratonovich_ham_second_moment.tex`.

**Commit IDs.** The history of this repository was rewritten before
publication, so every commit has a new ID.
- **Old IDs in files.** Commit IDs quoted inside files (for example
  `2e2ce0e`, `af97ae4`, `11e009a`) are the old IDs; the commit-map file
  translates them.
- **The commit map.** `history/commit-map.tsv` has one line per original
  commit: the old ID, then the new ID. To follow an old ID, look it up there
  and run `git show <new ID>`.
- **Dropped commits.** A commit that touched only removed material became
  empty and was dropped; its new ID is all zeros. In the final dry run,
  1,310 original commits became 1,258, and 52 were dropped.
- **Messages.** Commit messages are otherwise kept, except where
  `REDACTIONS.md` lists a change.

### How the public history was prepared

The public history was produced from the private original by a filter whose
classes of removal are listed, with counts, in `REDACTIONS.md`. Each dry
run of the filter was checked twice:
- **Automatically,** for commit counts, file sizes, archives by content,
  OCR of every image, text of every PDF, email addresses and every removal
  pattern. A secret scanner also ran on every dry run.
- **By a blind audit:** an AI model from a different family read the
  filtered history without access to the original and listed anything that
  should not be published.

Each audit found something earlier audits had missed, and each find became
a new rule, approved by the PI, and another dry run. The last four runs:

| Dry run | What the blind audit found | Rule added |
|---|---|---|
| 8 | Names of other private Lean package repositories, among them collaborators' | replace them with `<PRIVATE-PACKAGE>`; remove a coordination folder |
| 9 | A copied README of another project; two records tying an address to an AI account | remove copied READMEs; blank auth emails and glued account ties |
| 10 | Text extracts of pages of the source author's unpublished paper; other projects' wiki page names | remove page extracts of other papers; replace wiki page names |
| 11 | Nothing outside the PI's recorded decisions | none: the stop condition was met |

The stop condition was fixed in advance: an audit whose only findings are
items the PI has decided to keep, notes, and the metadata of removed
archives. A final audit, required to cover every image, every PDF and every
passage about other people's work, precedes publication. One lesson
recurs: a single sampled audit can miss a whole class of material, so "no
finding" is evidence, not clearance.

Commit subjects such as "Accept" describe the scope of that commit at that
time. They are not endorsements of the whole present paper.

## 6. What is and is not established

**Written:** complete written proofs for both goals, in the current book-format
manuscript (215 proofs written in this project). The upper bound at scale t^κ
is stated as `T:full-upper`. The limit is stated for every admissible model in
d = 1, 2, 3, with the constant given by a variational formula over nonnegative
smooth compactly supported spacetime controls. The constant is positive for
nonzero covariance and zero for zero covariance, and the manuscript gives
explicit bounds in a one-dimensional example.

**Reviewed:** parts of the argument passed component reviews at HIGH confidence
under their own scopes. The latest whole-manuscript review found no fatal or
major problem but had MEDIUM confidence. Under the project's own rules, the
whole paper is therefore **not accepted**. The second whole review, the
remaining visual checks, the final calibrations and the final cold read are
open.

**Formally checked:** the Lean companion's coverage at its commit `34b65d7`
(documentation changes only after `6eb79c7`, where wave L9 was verified; the
PI closed its correspondence gate on November 12) records the
following, result by result in `VERIFICATION.md`:
- forty-three numbered results, three displayed equations and one remark
  formalized under the manuscript's own hypotheses (eighteen of the results
  with a narrower conclusion);
- steps or parts of thirty more, with named analytic inputs supplied.

Three of the four main theorems and the analytic parts of the argument are
not formally verified; for the fourth, `T:intrinsic-occupation-ceiling`, Lean
proves a narrower conclusion. The Lean-to-manuscript correspondence was accepted by the
PI on AI review, which is not human verification.

**Not claimed:** the auxiliary score in the constant is not shown to be the
actual first-moment constant; the constant is not identified with the value
conjectured in the source paper; no correction of the source's normalization is
claimed; no closed numerical value is claimed; and no claim of priority is
made. "No defect found" is not a proof of correctness, and "MEDIUM" is not a
counterexample. Readers should treat the manuscript as a written candidate
proof, not as a refereed result.
