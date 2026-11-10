# AI development history: Stratonovich HAM second moment

Snapshot: November 9, 2026. Prepared at Le Chen's request for a detailed record
that humans can study. This is a retrospective synthesis of committed work,
public review reports and adjudications, not a verbatim session transcript.
It does not contain private model reasoning or reproduce credentials.

The project has a substantial written candidate proof and an explicit intrinsic
variational expression for the second-moment constant. **Whole-project acceptance
is still open.** The current 267-page working draft is versioned for preservation;
that action does not adopt the candidate or upgrade any review result.

## How to study the record

Start with this narrative, then follow the cited commit and source links.
[Progress.md](Progress.md) is the detailed workflow authority;
[PROJECT-GOAL.md](PROJECT-GOAL.md) records the scientific completion contract.
The [source manifest](sources/SOURCE-MANIFEST.md) identifies the source editions.
The [Lean ledger](lean-progress/PROGRESS.md) records local formal verification;
its dated additions must be read alongside its older summary paragraphs.

The [complete Git chronology](history/git-history.tsv) contains all **1,068**
commits reachable from this research branch through
`11e009aac6fcc9fdeddb00cdd7063dc56c457aad`, immediately before this checkpoint.
It includes full hashes, parents, author/committer dates and subjects.
[The JSON snapshot](history/git-history-snapshot.json) supplies the same records
and an explicit scope boundary. It excludes unmerged branches, external
work directories and uncommitted conversations. Commit count measures recorded
activity, not mathematical progress. Subjects such as “Accept” describe their
historical scopes; they are not blanket endorsements of today's whole paper.

To inspect a landmark, run `git show <hash>` or `git log <hash> -- <path>`.
To recover an earlier manuscript without changing the checkout, use
`git show <hash>:notes/notes_stratonovich_ham_second_moment.tex`.
Paths in this narrative are relative to the research repository.

## Timeline and changes in the research approach

| Period | Main development | Qualification |
|---|---|---|
| October 26–27 | Source reading, two-chain expansion and G0 test | A counting bound's failure is not a failure of the model |
| October 28–30 | Dimension-dependent routes, operator/phase methods and source construction | Conditional and finite-order results keep their limitations |
| October 31 | Actual-constant objective; all-model intrinsic formula checkpoint | Local acceptance is separate from whole-manuscript clearance |
| November 1–3 | Integration, occupation bounds, compact norm proof and 263-page baseline | Whole reconstruction remained incomplete |
| November 4–5 | Themed review, 20-page reader, 267-page integration candidate | Candidate and reader have different version bindings |
| November 6–8 | Whole-review, visual and provenance work | Much effort improved evidence rather than the mathematics |
| November 9 | Actual Gaussian Lean consumers, fresh MAIN v5, working-draft save | 87 local facts; whole MAIN still MEDIUM/unaccepted |

### 1. Establishing the correct problem, October 26–27

[held back: collaborators' unpublished work]

Two source-reading decisions shaped the rest of the project. First, the
Stratonovich expansion has self-pairings and unequal-chain cross terms.
A diagonal-only or Skorohod-style expansion cannot supply the desired full
second moment. Second, the author-version first-moment theorem gives two-sided
bounds: the earlier arXiv version's stronger formulation cannot be silently
imported. The manifest and notes preserve this source-version distinction.

The G0 investigation examined whether Chen's universal two-chain integral bound,
combined with counting, could reach the desired time exponent. The resulting
common majorant was too crude. This ruled out that majorization route rather
than the target theorem. The early checkpoint is visible at `2e2ce0e`
(October 27). Jensen supplied a baseline lower bound but not the full proposed
second-moment enhancement. Both checks constrained later arguments.

### 2. Testing routes and building the analytic framework, October 28–30

Early work explored low-dimensional estimates, endpoint cases and conditional
higher-parameter routes. Small white/static orders served as falsification
checks; they did not establish all-order asymptotics. Source time-shift and
uniformity issues required explicit treatment instead of treating a cited
estimate as stronger than its printed assumptions.

The eventual independent upper-bound route used Gaussian phase/operator and
interval-coefficient estimates. Creation and annihilation contributions both
matter. So do the background coupling and the second-order mean term in the
static variance calculation. Arbitrary-phase covariance monotonicity was not
available. Scalar solution moments alone cannot be multiplied over time blocks:
the wave equation carries displacement and velocity.

A parallel difficulty was identifying the same stochastic solution throughout
the argument. The construction needed compatible cutoffs, the source Gaussian
noise, controlled auxiliary randomness and mixed moments; in dimension three,
the Green operation must precede noise evaluation. Raw Sobolev point traces
could not simply be assumed. Later estimates therefore carried spatial-radius
uniformity and explicit links between the canonical construction, upper bound
and lower comparison. These are analytic proof obligations, not consequences
of finite-dimensional algebra checks.

### 3. Deriving the constant instead of forcing a prediction, October 31

Le explicitly revised the objective: derive whatever constant the computation
gives rather than force Chen's predicted value. The revised contract permits
an exact, fully specified variational characterization; it does not require a
numerical closed form. Literature constants remain comparison objects, with
their domain and normalization qualifications intact.

The all-model physical-score draft is recorded at `40ec9a9`, with the intrinsic
second-moment checkpoint accepted locally at `d52d1d8`. The variational domain,
original covariance amplitude, unit kinetic coefficient and Gaussian half-action
must all be specified. Zero covariance is handled directly. The auxiliary
label-one score is not thereby identified with an actual first-moment limit
or Chen's printed constants.

This was a scientific milestone within the local review process. It did not
settle all later source/application, integration or whole-proof review gates.
The relevant current source is
[the intrinsic-constant module](notes/integrated_intrinsic_constant.tex).

### 4. Integration and bounds, November 1–3

Commit `a880288` integrated finite Gram optimization and the intrinsic formula.
Commit `d041546` integrated occupation and white-spatial-energy bounds.
The [occupation module](notes/integrated_occupation_ceiling.tex) and
[white example](notes/integrated_white_evaluation.tex) bound the same constant.
Evaluating the white spatial energy exactly does not evaluate the complete
moment variational supremum numerically.

Integration exposed the difference between checking components and reconstructing
the complete proof. Scientific baseline `af97ae4` introduced a compact Young norm
argument and direct real conservation proof and produced the 263-page version.
The [bounded-review adjudication](reviews/2026-11-03-structural-baseline-candidate/root-adjudication.md)
records its changed deductions. The
[whole MAIN terminal record](reviews/2026-11-03-main-af97-terminal/)
retains an INCONCLUSIVE/low disposition and substantial reconstruction limits.
No source mathematical defect was located there; incomplete verification
remained incomplete verification.

### 5. Readability, themed review and the 267-page candidate, November 4–5

Themed passes worked through foundations, constructors, phase estimates,
independent upper bounds, the intrinsic constant and calibration. Their scopes,
versions and confidence differed. Combining locally positive reports cannot
manufacture a whole-paper acceptance that no reviewer supplied.

A separate editorial branch, `editorial/reading-notes-20261105`, committed a
20-page reader with matching TeX/PDF at `9895781`. It was paired with the
263-page technical manuscript: the package totaled 283 pages. It was a reading
aid, not a reduction of the full proof to twenty pages. Its historical
[paired validation](reviews/2026-11-05-reader-v4-paired-revision/) keeps that binding.

The later 267-page integration candidate added the self-contained pairing
product envelope. Its inventory has 215 OWN proofs and 241 declarations,
including 26 non-OWN declarations. Whole-candidate coverage also requires
13 joins and nine global checks: 263 required review rows in total.
All 27 included TeX modules remained whole. This candidate was preserved
externally during review; this checkpoint places its main TeX/PDF at the normal
tracked paths with an explicit unadopted status.

### 6. Review and visual work: useful evidence and diminishing returns

Substantial time went to frozen packets, source inventories, exact input hashes,
provider transport, context capacity, report schemas and confidence accounting.
Some of this was necessary: a review must bind the actual source and actual
applications, and a missing or quota-failed request is not a review.
But repeated transport and confidence work increasingly displaced mathematical
progress. That imbalance contributed to the stall. More reports on unchanged
material did not automatically close the scientific question.

Several whole reports returned positive substantive assessments at MEDIUM
confidence; the recorded contract required HIGH. Some outputs also had JSON
or row-format defects. Raw reports and adjudications were retained rather than
editing grades or silently treating failed output as acceptance. Source delivery
and context-size evidence establish what was sent, not what a model understood.

Kimi's weekly quota failure was confirmed from native records. Le directed a
few-day hold; no further Kimi probes or review calls are authorized by the
mere passage of time. Separately, provider auto-update behavior complicated
binary reproducibility. Fixing transport controls was infrastructure work,
not a new mathematical result.

Visual verification has its own boundary. Accepted coverage is 230 of 267
pages, leaving 37. Images being prepared or delivered does not mean that pages
were independently accepted. A proposed MEDIUM visual policy was not adopted.
The rendered-document audit and mathematical proof review remain distinct.

### 7. Lean: from finite algebra to actual Gaussian applications, November 9

Lean work remains in this research repository under
[lean-progress/local-checks](lean-progress/local-checks), not in a separate
project companion. The official companion wave is still L0/PROPOSED; no package,
lease, registry gate or cluster job is implied by the local checks.
Earlier work had 80 accepted finite/conditional facts in 22 groups. The latest
accepted local total is 87 facts in 26 groups; older summary paragraphs retain
historical counts. Counts are bookkeeping, not a measure of the theorem's
percentage formalized.

The latest sequence deliberately strengthened the actual consumer connection:

1. `76a8260` verified the normalized Hermite-coordinate recurrence, including
   both raising/lowering coefficients and the zero case. Actual unit Gaussian
   L2 controls and a false-statement rejection accompanied local kernel replay.
2. `9d65bd3` verified vector Gaussian Hilbert projection with exact source modes.
   Statement review corrected an overly broad product index to the dependent
   Sigma indexing used by the source. The physical Hilbert space can be infinite
   dimensional; a finite Fourier band does not make it finite dimensional.
3. `e459eb3` closed the concrete Gaussian colored-word application. Its actual
   coordinate operators, raw/compressed prefix domains, occupation cutoffs and
   noncommuting bounded coefficient operators were connected to the word theorem.
   Three new facts and the now-supported application of two older generic facts
   brought the total to 87/26. Nonzero order-two controls and deliberately wrong
   self-mean/cutoff controls tested the semantic boundary.

These checks are more informative than a scalar toy representation alone.
They still do not kernel-verify the entire SPDE argument. Complex-to-real
identification, background/phase source bridges, Bochner integration and analytic
limits remain explicitly mathematical boundaries. The background-only extension
agrees with the full potential only on the cross-projection range, not globally.
Compilation without application fidelity would not settle that distinction.
See the [boundaries ledger](lean-progress/BOUNDARIES.md) and the local application
summaries for the exact fences.

### 8. The last whole review and the stall

Commit `11e009a` archives
[MAIN v5](reviews/2026-11-09-full-main-v5-kernel-medium-unaccepted/).
This review had genuinely new kernel-consumer evidence while retaining the
original all-model scientific scope. It received all 83 unchanged operative
source bodies plus ten new kernel bodies, together with current challenges.
The returned assessment was PASS_WITH_NOTES/MEDIUM: 226 PASS and 37
PASS_WITH_NOTES rows, no fatal/major findings or required repairs.

All 263 semantic IDs were present once. Twenty-two join/global IDs lacked
required trailing delimiters, causing a collector refusal. An initial description
suggesting renamed IDs was corrected: none were renamed or missing. This format
issue is separate from the MEDIUM confidence, which independently failed the
recorded HIGH gate. Neither the report nor parser was repaired to claim a pass.
Root also recorded source-backed corrections to limitations in the report,
without presenting those corrections as a reviewer confidence upgrade.

At that point there was no newly identified concrete source repair to perform,
yet the whole-paper HIGH, remaining visual and cold-reader gates were open.
That was the impasse: substantial written mathematics and local checks, but
insufficient final acceptance under the chosen procedure. “No identified defect”
is not a proof of correctness; “MEDIUM” is not a counterexample either.

## Proposed recovery and what has actually happened

Le agreed to a focused recovery direction: preserve the original model scope,
map claims to dependencies and evidence, use qualified independent human
mathematical adjudication as the final scientific authority, and keep AI
confidence as supporting evidence. A private companion would migrate existing
local facts in bounded scope; any next formalization should test a concrete
bridge rather than start a new Gaussian/SPDE foundation. Final cold, visual,
source and delivery work would still need explicit completion.

This direction was discussed and approved in conversation, but the project
contract was not rewritten and the private companion was not created before
Le stopped the run. The earlier research goal was cleared; a separate objective
literally named “stop” was completed. That did not complete the research goal.
This retrospective does not silently implement the proposed new acceptance policy.

Le then requested an atomic commit/push of the current working TeX/PDF and this
human-study history. This checkpoint performs that preservation task. The
[working-draft status](notes/WORKING-DRAFT-STATUS.md) and
[build receipt](reviews/2026-11-09-working-draft-267-checkpoint/README.md)
distinguish the current 267-page candidate from the preserved 263-page baseline.
The fresh PDF matches the previously verified rebuild byte for byte, with zero
build errors, undefined references/citations or overfull boxes. Build success
is reproducibility evidence, not mathematical acceptance.

## Lessons supported by this record

- Fix source edition, model, normalizations and stochastic construction before
  borrowing an asymptotic constant. An attractive formula cannot repair a
  mismatch in the problem being proved.
- Use low-order and degenerate examples early. Record precisely which route a
  failed check excludes; do not turn failure of a bound into failure of a model.
- Review actual joins and consumers, not just isolated lemmas. Retain version
  bindings when either source or application changes.
- Couple Lean propositions to the actual analytic objects and use meaningful
  positive and negative controls. State the remaining analytic hypotheses plainly.
- Preserve raw independent opinions, including format errors and uncertainty.
  Adjudicate factual errors without editing the reviewer's confidence.
- Stop confidence-only retries on unchanged material. Investigate a concrete
  gap, seek qualified human adjudication or revise the agreed workflow explicitly.
- Keep source, PDF, reader and review bindings together. A compact reader,
  raster equality, delivery receipt and theorem proof answer different questions.
- Measure progress by closed mathematical obligations and usable exposition,
  alongside unresolved obligations. A thousand commits and many review packets
  do not by themselves establish a completed theorem.

This history is a navigational synthesis. Where a summary and an original
artifact differ, inspect the exact source, raw report and dated adjudication;
record a correction rather than retroactively rewriting the historical outcome.

## Primary-branch consolidation after this snapshot

After the checkpoint above, Le requested merging the research work into master.
The comparison found 116 master-only and 769 research-only commits, with content
conflicts only in README.md and HANDOFF.md. A regular two-parent merge preserves
all commits from both histories. The README and current handoff now identify
master as the working branch; both previous handoffs are archived verbatim in
handoffs/2026-11-09-before-master-consolidation/. The research and editorial
branches are retained. The chronology files remain the explicitly bounded
pre-checkpoint snapshot above; use Git itself for subsequent commits and the
merged master-only history. This consolidation changes no scientific acceptance
state and leaves the source, PDF and earlier review evidence unchanged.
