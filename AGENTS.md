# Article-Stratonovich-HAM-Second-Moment — AGENTS.md

## Project overview

**Goal.** For the Stratonovich hyperbolic Anderson model with Gaussian noise
fractional in time (X. Chen, author version, `chen:author2026:time-dependency`):

1. **Upper bound at the correct scale:**
   limsup_{t→∞} t^{-κ} log 𝔼u²(t,x) < ∞, with κ = (4−α−α₀)/(3−α),
   improving Chen's 𝔼u² ≤ e^{Ct²} (Remark 5.1, p. 37).
2. **Actual constant for p = 2 (Le's 2026-10-31 revision):** prove the
   asymptotic limit and derive its constant from the model, including an
   exact fully specified variational characterization if that is what the
   proof yields. Simplify and bound it as justified. Chen's conjectured
   constants are comparisons, not values we must attain. Do not force the
   derivation to match them or require closing his energy gap to finish.

The precise statements, notation and known results are in
`notes/notes_stratonovich_ham_second_moment.tex` (book format; begin with
the front guide and Chapters 1–3). Read it first.
**Progress.md is the workflow authority** (rounds, gates, decisions).
`PROJECT-GOAL.md` is the completion contract.

[held back: private planning]

**Wiki project page:**
`../SPDEs-wiki/content/projects/stratonovich-ham-second-moment.md`.

## Scope boundary (read before doing anything)

[held back: collaborators' unpublished work]

## Key structural facts (from the 2026-10-26 setup reading; do not relearn)

1. **Expansion.** u = Σ S_n(g_n) with ordered single-chain kernels
   (2.13)–(2.16). Expected Stratonovich integrals include **self-pairings**
   within a chain (Wick sum over all pair partitions, (2.21)), unlike the
   Skorohod chaos.
2. **Second moment = two-chain pairing integrals.** 𝔼[S_n(g_n)]² is given
   exactly by Theorem 4.1 (4.3) (two ordered chains I₁, I₂, all pair
   partitions of 2n points). The full 𝔼u² also has cross terms
   𝔼[S_m S_n], m ≠ n, m+n even (via (2.18)): justify and write them (Gate G0).
3. **Theorem 3.1 (3.6)** is a universal bound for exactly these two-chain
   integrals, including cross-pairings, with Laplace-weighted kernels in
   Lemma A.1. Chen uses it only for integrability.
4. **The crude bound** 𝔼u² ≤ e^{Ct²} (Remark 5.1) comes from (2.13) and
   (4.4). Where the exponent 2 enters, instead of κ, is the first question.
5. **Why Chen stops at p = 1** (Remark 6.3): his exact representation
   (Theorem 6.1) needs the monotone order of one chain. For p = 2 each chain
   is still ordered; only the interleaving is lost. That is the opening for a
   two-clock representation.
6. **Actual Jensen remains a constraint:** E|u|² ≥ (Eu)² (Proposition
   P:Jensen). Any verified applicable first-moment lower constant gives
   the corresponding doubled lower bound. Numerical use of the source
   label L_* retains the known normalization qualification. The guessed
   factor in Chen's conjecture is not a required answer, and an auxiliary
   S₁^pos is not automatically the actual first-moment constant.
7. **Version trap.** arXiv:2510.01412v1 states an exact first-moment limit;
   the author version proves only two-sided bounds. Never cite v1 for
   Theorem 1.2. See `sources/SOURCE-MANIFEST.md`.

## Calibrations every proposed bound must pass

[held back: collaborators' unpublished work]

## Repository layout

```
AGENTS.md            this file
PROJECT-GOAL.md      objective, completion contract, scope limits
Progress.md          workflow authority (rounds, gates, decisions, failed routes)
CODEX-START.md       the launch prompt for the Codex run
README.md
notes/notes_stratonovich_ham_second_moment.tex   (+ tracked PDF)
sources/SOURCE-MANIFEST.md, sources/chen-2026-author/, sources/llm_pack/
reviews/             review packets and reports (one dated directory each)
handoffs/            session handoffs
All.bib -> ../refdb/All.bib (read-only), extra.bib (local additions)
20/ 29/ 4/           Le_Chen_Publications symlinks (BCC 2022, Chen–Eisenberg 2023, Chen–Dalang 2015)
```

## Workflow and rules

### Mathematics
- Self-contained proofs for every new claim. Imported results are labeled
  ("From [Chen, Theorem 3.1]") with an exact pinpoint and are never presented
  as proved here.
- State conditional results as conditional. Never stamp a proof as complete
  on reconnaissance or a one-pass argument.
- Falsification first: before a long proof, test the claim on the simplest
  case (small n, p = 2 chaos order 2 or 4, d = 1, α = 1) and record the test.
- Record every failed route in Progress.md with the reason (a no-go is a
  result).
- For a time-block approach, carry displacement AND velocity. Scalar
  solution-value moments do not multiply across blocks. The section labelled `S:static-phase` controls
  both terms of the static first-variance phase coefficient;its second-order
  mean term cannot be dropped,and arbitrary-phase covariance monotonicity
  is unavailable. This is a full-spatial-class tool,not an all-order bound.

### Workforce (paper-dev)
- **Worker:** the Codex session running this project (GPT family).
- **Reviews must come from a different model family than the author** of
  the argument. Per Le's 2026-11-01 direction, use **DeepSeek V4 Pro +
  Kimi-K3** for newly assigned reviews. Le explicitly designated
  **DeepSeek V4 Pro as the main reviewer on 2026-11-02**. This does not
  waive image verification or the fresh independent cold-review gate.
  DeepSeek uses the configured
  `paper-review-deepseek` route with `deepseek/deepseek-v4-pro`; Kimi uses
  native `subscription-review-cli run kimi --model kimi-code/k3` with its
  verified configured effort. Use frozen inputs and read-only execution.
  Keep HIGH confidence, exact source/application/visual coverage and final
  cold-reader requirements. A final cold read needs a fresh session and a
  family independent of any author of a material repair. Do not silently
  substitute another model, purchase quota or relax a missing-source gate.
  Preserve prior Opus reviews under their original scope and identity.
  A quota error, generation-limit stop or missing report is not a review:
  record it. A text-only review does not certify source-image coverage.
- Every round that adds a proof: freeze a packet in `reviews/<date>-<round>/`,
  get the skeptic report, adjudicate every finding in Progress.md.
- Canonical workflow: `<HOME>/workspace/Le-AI-Lab/commands/paper-dev.md`.
  Skills (read the SKILL.md before using; under
  `<HOME>/workspace/Le-AI-Lab/skills/omc-learned/` unless noted):
  `progress-md-authority-paper-dev`, `paper-dev-review-layers-are-mandatory`,
  `paper-dev-round-close-protocol`, `falsification-first-differentiated-routes`,
  `numerics-gate-before-proof-investment`, `cited-theorem-source-fidelity-gate`,
  `le-chen-writing-style`, and `skills/latex-conventions`.

### LaTeX
- Build from the repo root:
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex`
- Gate before every commit of a .tex change: 0 errors, 0 undefined
  references/citations, 0 overfull boxes; commit the rebuilt PDF with it.
- No tab characters (2-space indent). Labels: `T:` `L:` `P:` `C:` `R:` `D:`
  `H:` `E:` `S:` `Conj:` (Goals use `G:`). Every `\end{proof}` is preceded by
  "This proves Lemma~\ref{...}." (or Theorem/Proposition).
- amsrefs: `\cite{key}*{Theorem~3.1}` for pinpoints; `\cites{k1,k2}` takes
  one comma-separated argument.

### Bibliography
- `All.bib` is a read-only symlink to `../refdb/All.bib`. New entries go in
  `extra.bib` (or through the refdb workflow, not by editing All.bib).
- Before citing a key: `grep -n '{key,' All.bib extra.bib`.

### Literature recon and retention (Le, 2026-10-28)
- Before external recon, query SPDEs-wiki with `scripts/cli.py search` and
  `cite`, then read the relevant synthesized pages. A filename/raw-text
  search alone is not the complete wiki recon. Use the wiki to check model,
  parameter, technique and no-go boundaries before importing a result.
- When a helpful reference is missing from the six-repository corpus,
  enqueue it through the canonical `repo-queue` for future use, as Le
  explicitly requested. Prefer a verified published DOI when available,
  retain the accessible source edition and precise reason for relevance,
  and avoid duplicate preprint/publication records.
- `repo-queue check` takes a citekey or exact DOI; its five addressable
  layer checks do not replace a Papis metadata check. Retain exact ticket
  identities and receipts. Queued, claimed and fully ingested are distinct.
  Normal reference queueing does not authorize source-author correspondence,
  public release or creation of the private Lean companion.

### Git
- Remote: `origin` = <HUB> bare repo
  `<HUB>:<HOME>/<REMOTES>/Article-Stratonovich-HAM-Second-Moment.git`.
- Atomic commits per unit of work; push after each; stage only your own
  paths (never `git add -A`).
- Several agents share this checkout and its Git index. **Commit by
  pathspec only:** `git commit -m "msg" -- <path> ...`. A pre-commit guard
  (`scripts/guard-shared-index.sh`, called from `.git/hooks/pre-commit`)
  refuses plain, `-a`, `-i` and `--amend` commits; for a deliberate
  whole-index commit use `SHARED_INDEX_OK=1 git commit ...`. Never use
  `--no-verify`. Before pushing, check `git show --stat HEAD` and that the
  branch is not already ahead with another agent's commits.
- After every push from a non-<HUB> machine, sync <HUB>:
  `ssh <HUB> 'cd "<HOME>/workspace/svn/Article-Stratonovich-HAM-Second-Moment" && git fetch origin --prune && git pull --rebase --autostash'`
  and verify HEAD parity. Never drop or reset another agent's work.
- Repository-relative paths only in committed files.

### Lean track (lean-pkg)
- Authority for Lean waves: `lean-progress/PROGRESS.md` (lean-dev skill); the
  mathematics authority stays `Progress.md`. Strategy: `lean-progress/ROADMAP.md`.
- Canonical workflow: `<HOME>/workspace/Le-AI-Lab/commands/lean-companion.md`
  and the skills `lean-dev`, `lean-paper-verification-ladder`,
  `lean-pkg-search-registry-before-new-package`, `search-before-building-lean`.
- Before any new package: `lean-pkg search <terms>`; then `lean-pkg new` and
  `lean-pkg register`; take a lease with `lean-pkg lease claim` while working.
  Evidence: `lean-pkg verify` / `receipt` / `gate`. The package stays private.
- Lean verifies finite and algebraic steps; analytic inputs are explicit named
  hypotheses recorded in `lean-progress/BOUNDARIES.md`. Compile locally first;
  Easley only for gates (CLAUDE.md HPC rules).

### Compute
- This is pen-and-paper mathematics. Small symbolic or numerical checks run
  locally (sympy/mpmath via `uv run --with ...`). Do not use Easley for this
  project without Le's instruction.
