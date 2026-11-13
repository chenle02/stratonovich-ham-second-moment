# Lean companion publication plan (release sequence 3a, step 1)

Authority: this file records the plan and Le's decisions on it. The plan
text below is the one sent to #16 on 2026-11-11, followed by the Zenodo
addendum. Nothing on GitHub or Zenodo happens before Le's explicit go
(planned Nov 29-30); the release candidate needs Le's approval after the
independent audit (Nov 26).

## HOLD (Le, 2026-11-11, relayed verbatim by #16): "do not turn public yet"

No public step for the companion until Le explicitly says otherwise: no
GitHub repository rename or creation, no visibility change, no push to a new
public repository, no Zenodo action. Private preparation of the release
candidate (scrub, receipts, audit) is unaffected. #16 confirmed on
2026-11-11 that the companion is PRIVATE and the main repository does not
exist on GitHub.

## Le's decisions (2026-11-11, relayed verbatim by #16)

> "Approve #22's companion plan: rename to a private -dev repo and publish a
> fresh public repo, keep Easley named, and post the board as GitHub issues.
> Keep the gaussian-chaos seams in the main repo as development record."

1. Rename-and-fresh-repo APPROVED: the current private repository becomes
   `stratonovich-ham-second-moment-lean-dev` (stays private, full history and
   receipts); one scrubbed root commit is pushed to a fresh repository under
   the canonical name `stratonovich-ham-second-moment-lean`.
2. Easley stays NAMED in the companion (`verification/leanchecker-easley-*`,
   README); the container path is still scrubbed to `<container>.sif`, the
   HPC username to `<user>`.
3. The board is published as GitHub ISSUES after the flip (D9), not as a file
   in the root commit; the `docs/community` branch stays in the -dev repo.
4. The three gaussian-chaos seams in the main repository's
   `lean-progress/local-checks` stay in its public history as development
   record, marked not reproducible until gaussian-chaos-lean is public (no
   new redaction rule).
5. Zenodo approved for both repositories (separate #16 relay): Le links
   Zenodo and switches the public companion repository on BEFORE the v1.0
   release; CITATION.cff valid (cffconvert, companion 73ed477); no history
   bundle for the companion; related works added after both DOIs exist.

Approvals are for the plan only; the GitHub and Zenodo steps wait for Le's go.

## Plan as sent to #16


State now: companion github.com/chenle02/stratonovich-ham-second-moment-lean, PRIVATE, 110 commits on main (all with Claude-Session trailers) plus branches (docs/community = the board; wave branches), registry status verified-private, gate at d40f394, claims ledger READY 0 open. Wave L5 (six items) is being integrated now; its gate is Le's.

(1) Fresh root commit
- Tree: the companion tree at the release-candidate commit X (after the L5 gate closes and the release docs are done), scrubbed (item 4), ONE root commit in a NEW public-to-be repository. The incubation history (110 commits, wave branches) is never pushed to the public repo: anything once public stays fetchable by SHA, so flipping or force-pushing the current repo is not used.
- Repository name: keep the canonical name for the public repo. Proposed: rename the current private repo to stratonovich-ham-second-moment-lean-dev (stays private, keeps the full history and receipts of every earlier commit), then create a fresh private repo with the canonical name, push the single root commit, and flip it when Le says so. Alternatively lean-pkg's fresh-repo export path; I will dry-run it first.
- How the history stays referenced: provenance/DEVELOPMENT.md in the root commit names the private development repository and its final commit SHA (and the tree hash, proving the release tree equals that commit's scrubbed tree), and points to the main repository's public record of the development (lean-progress/PROGRESS.md, reviews/*lean*, which go public with the main repo on Dec 1 under its redaction rules). The comment-only/scrub edits are proved mechanically (non-comment token streams of every .lean file identical to X).
- Registry: re-point the lean-pkg entry to the new repo/commit, cut fresh receipts (both tiers) AT the root commit (receipts bind exact commits, so X's receipts do not carry over), regate, claims ledger READY 0 open, `public-safety --strict` 0 hits (tree and history), then the one-way promote/publish with Le's go. Registry status goes verified-private -> public.

(2) v1.0 tag, DOI, CITATION
- Tag v1.0 = the fresh root commit (or the receipts commit on top of it, docs-only, which stays bound by docs_descendants; I will make the tag the commit that contains the receipts so the tag is self-verifying).
- Zenodo: GitHub integration on the public repo, release v1.0 -> concept DOI and version DOI. CITATION.cff in the tag says "cite by exact commit" plus a preferred-citation to the paper; the DOI goes in by an append-only commit after Zenodo mints it (it cannot be known before), and the main repository cites the version DOI and the tag.
- What the main repo regenerates from: the tag's coverage.yaml, claims.yaml, docs/coverage-scope-tex.yaml, the two receipts in .lean-receipts/<tag-sha12>-*, and `lean-pkg claims ledger --json`. I will send #24 and #16 the tag SHA and the numbers on the day.

(3) The 3 gaussian-chaos seams (9 facts)
- They were never in the companion: they live only in the main repository's lean-progress/local-checks (normalized-coordinate, vector-gaussian-projection, colored-vector-word). The companion's lake-manifest has only Mathlib and its dependencies, and no file imports GaussianChaos, so the public build has no private dependency (verified today).
- Public coverage: unchanged by the release; the README and FORMALIZATION.md already say three development modules depend on a Gaussian-chaos library that is not yet public, that their 9 facts cannot be reproduced from the repository, and that nothing in it relies on them. Board items A2 and B21 stay "blocked". Decision for Le only if wanted: the main repo's local-checks copies of these seams import GaussianChaos; the main repo's filter should treat them like the companion (keep as development record, marked not reproducible) or hold them back until gaussian-chaos-lean is public.

(4) Must not be public, and how I check
Found today in the companion tree (650 files):
- scripts/comparator/scaffold.json: 3 absolute /home/<user> paths (lines 2112, 2124, 2365) -> replace with repository-relative paths and regenerate. [DONE 2026-11-11 at companion 210cc3f: there were 21 such paths; all rewritten to repository-relative `lean-pkg-types/...` names.]
- verification/leanchecker-easley-*: harness sbatch files with /home/<user>/... (already redacted to <user>), the container file name (contains the GitHub handle), job ids and the cluster name Easley; README names Easley. Proposal: keep the Easley evidence (it is the external-kernel replay and Auburn's HPC acknowledgment practice names the cluster) but scrub the container path to <container>.sif; Le decides whether the cluster name stays. [DECIDED: Easley stays named; container path scrubbed.]
- Commit trailers (Claude-Session URLs) and the incubation history: gone with the fresh root.
- Branch docs/community (the board): not in the root commit; the board is published later as GitHub issues per D9, or as docs/community/WORK-PACKAGES.md if Le prefers.
Checks before the flip: an UNTRACKED .lean-pkg-private-patterns with block: lines for the main repo name, private package names (gaussian-chaos-lean and the other private lean-pkg names), host names (duckdns, <HUB>, <MACHINE>), the HPC and local user names, /home/, scratchpad paths, amsg/lean-ops, private emails, Claude-Session; reuse the main repo's release-filter patterns (redact_filter rules) as a second pattern set; `lean-pkg public-safety --strict` on tree and history to 0 hits; then an independent read-only release audit from a different model family over the root commit; and the publish dry-run checklist.
Allowed and intended: manuscript labels and TeX line numbers (the main repo goes public the day after), model names in README, author email in CITATION if Le wants it (currently none).

(5) From Le, and when
- by Nov 20: close the wave L5 correspondence gate (or decide to release at the L4/975feb3 state, d40f394, if L5 slips);
- by Nov 22: approve this plan: the rename-and-fresh-repo approach, Easley named or not, board as issues or file, author metadata (ORCID, CITATION fields), the release tag naming (v1.0);
- by Nov 26: approve the release candidate after the independent audit (I will have the scrubbed root commit, receipts, public-safety 0/0 and the audit report ready by Nov 25);
- Nov 29-30: say "go" for the GitHub steps (create/rename repos, push, flip, Zenodo release). I will not touch GitHub before that.
- Lean/Mathlib: the companion pins Lean 4.35.0; at release-prep I will check the current stable Lean/Mathlib and report whether an upgrade is advisable (not required for v1.0).

## Private release-candidate dry run (2026-11-11; local only, nothing on GitHub or Zenodo)

From companion a7f90b0, by a rerunnable script (session scratch
`rc-dryrun/build-rc.sh <commit>`):
- Scrub: 15 files, all under `verification/`, no `.lean` file: the
  container image path -> `<container>.sif` (5 harness files); the runtime
  tarball's scratch directory, which was named after another private
  project, -> `<runtime-dir>` (5 sbatch files, 7 gate logs); a redaction
  sentence in the three Easley READMEs.
- Comment-only proof: all 493 `.lean` files byte-identical (stripped token
  streams equal; positive and negative controls pass); claims.yaml,
  coverage.yaml, comparator.json, Challenge, Solution and ChallengeDefs
  byte-identical.
- One local root commit (no remote), reproducible: 1 commit, 882 objects,
  no borrowed objects; CITATION.cff valid; board files absent.
- Private-pattern scan (49 block + 5 warn patterns: repository, package,
  host, user, path, tooling and email names): 0 hits on the scrubbed tree
  (27 on the unscrubbed source: positive control).
- `lean-pkg public-safety --strict`: 348 `notes-ref` blocks (manuscript
  paths `notes/...tex` cited in Lean doc comments, the ledger and
  provenance) and 4 false `latex-label` warnings (`sec:05.2f` in a Python
  format string). File-scoped allow lines bring it to 0/0 (tested).

Open decisions for Le (before the Nov 26 release-candidate approval):
1. The 348 `notes-ref` hits: accept file-scoped allow lines (the manuscript
   paths are intended: the main repository is public the next day), or
   rewrite the citations.
2. The 46 existing receipts bind development commits that will not exist
   in the public repository: keep them in the root commit as development
   evidence, or describe them only in provenance (fresh receipts at the
   root commit are cut either way).
3. Author identity of the root commit: the personal address or the GitHub
   noreply address.
4. `provenance/DEVELOPMENT.md` will name the private -dev repository and
   the main repository: allow those names in the public tree.
5. Editorial: internal wave names (`wave L2`-`L5`, folder names such as
   `leanchecker-easley-wave-l3`) in the public tree: keep or rename.
Still to do: rebuild from the commit after the Easley record; README
Verification record rewritten for the root commit; fresh receipts; the
independent release audit by a different model family.

### Le's decisions on the five open items (2026-11-11)

1. The 348 `notes-ref` hits: ACCEPT file-scoped allow lines (the manuscript
   paths are intended), e.g. `allow: *.lean: ^notes/$`,
   `allow: docs/statement-ledger.md: ^notes/$`,
   `allow: provenance/manuscript-anchor.json: ^notes/$`, and
   `allow: replay*.py: sec:05\.2f` for the 4 false `latex-label` warnings.
2. The 46 existing receipts STAY in the root commit as development
   evidence (provenance says they bind development commits of the private
   -dev repository); fresh receipts are cut at the root commit.
3. The root commit uses the GitHub noreply address as author and committer.
4. `provenance/DEVELOPMENT.md` MAY name the private -dev repository and the
   main repository (allow lines for exactly those names in that file).
5. The internal wave names (`wave L2`-`L5`, `leanchecker-easley-wave-l*`)
   are KEPT.
These settle the release-candidate content; the hold on every public step
("do not turn public yet") is unchanged.

## GO: public release now (Le, 2026-11-13)

Le, verbatim (in session, 2026-11-13): "Can you turn this repo public, at the
same time, following lean-pkg to beautify the GitHub document page." "Make
sure that you have milestone tagged for the repo" "Also please register this
at Zenodoo" "Do all the necessary steps to turn this into public". Le's answers
the same day: path "Fresh public repo" (the approved 2026-11-11 plan: rename
the current repository to `stratonovich-ham-second-moment-lean-dev`, private,
full history and the milestone tags `L0-companion-created` ... `L9-gate` kept;
one scrubbed root commit in a fresh public repository under the canonical
name; a direct flip was declined because early history holds the HPC
username, the container path and home paths); version "v0.9.0 at the L9
gate now" (tree of companion `34b65d7`, verified `6eb79c7`; v1.0.0 after the
freeze plan: L10-L14 gates, HYG, re-anchor); Zenodo "Yes, I'll toggle Zenodo"
(Le switches the public repository on in Zenodo before the GitHub release
v0.9.0 is published). This lifts the 2026-11-11 HOLD for these steps only.
Tags (Le, 2026-11-13, verbatim): "Keep only the v0.9.0 tag on the public repo;
skip L9-gate-public. Tell me when the new repo exists so I can switch it on in
Zenodo." The milestone tags L0-companion-created ... L9-gate stay in the
private `stratonovich-ham-second-moment-lean-dev` repository (renamed
2026-11-13; all clones repointed); the public README and COMPLETION.md list
each milestone with its development commit.

Release level (Le's decision, 2026-11-13, relayed by #16): "this release STAYS
AT L9 (option 1)". The book (Appendices F and G, root VERIFICATION.md, front
door) keeps Lean at L9: coverage `34b65d7`, verified `6eb79c7`; the public
companion's first tag is v0.9.0 = the L9 state. L10 (`b2bf7a9`, gate closed
2026-11-13) is not re-pinned for this release; it goes into the next MINOR
release of both. The L10 Appendix F paragraph sent to #24 is held for that
release.

## Held for the book 1.1.0 pin (L10): Appendix F review paragraph

Book release levels (Le, relayed by #24, 2026-11-13): the book v1.0.0 keeps Lean at L9 (Appendices F and G at verified `6eb79c7`, coverage `34b65d7`; VERIFICATION.md at `34b65d7`); L10 goes into book 1.1.0. Pin for 1.1.0 (unless a later gate supersedes it): verified `b2bf7a9`, coverage `d6a0505`. The L11 wording for hQ will replace the hQ sentence if L11 is included. Paragraph as sent to #24:

The statements added in wave L10, and the changes that wave made to existing entries of the coverage record, were checked against the manuscript in eight independent correspondence reviews, done by AI models from a different family than the one that wrote the formal statements, under the conventions the author fixed in wave L9. The reviews found documentation corrections only, and no error in a Lean proof. The corrections were made, a confirmation review checked them, and a final re-confirmation passed with high confidence. The author accepted wave L10 on 2026-11-13, recording one point with it: in the step that assembles Proposition P:interval-coefficients from Lemma L:fixed-split, the formal version assumes a bound on the pairings of the cut-off coefficients that the manuscript does not state as a hypothesis (in the manuscript it follows from Lemma L:finite-word-cutoff); the author accepted this added hypothesis for now. The record states what remains open: Theorem T:white-moment-bounds is formalized for the variational value S_2^pos rather than for C_2, with the white spatial energy supplied as an input; and Lemma L:fixed-split is formalized with its analytic inputs supplied and the cut-off evolution not constructed. Lemma L:higher-riesz is formalized in full for dimensions two and three, and Lemma L:alpha-one-convolution from the homogeneity hypothesis alone. These reviews are not a human verification, and they do not check the analytic inputs that stay outside Lean.

## RELEASED: v0.9.0 public (2026-11-13)

- Public repository `chenle02/stratonovich-ham-second-moment-lean` (fresh, one
  root commit; local checkout `<PRIVATE-PROJECT>`,
  <HUB> clone at the same path). Root `ed66b5b` (scrubbed release tree of
  dev `34b65d7`, verified `6eb79c7`; all 1166 build-input files identical),
  receipts commit `6cc04c1` (lower tier and comparator bound to the root),
  annotated tag `v0.9.0` on `6cc04c1` (noreply tagger), DOI commit `0966ef6`
  (docs only; receipts still bind).
- Gates passed before the flip: comment-only proof (all .lean byte-identical),
  `lean-pkg public-safety --strict --history` 0/0 (rerun after tagging and
  after the DOI commit), gitleaks clean, independent release audit by Codex
  GPT-6.1-Sol (round 3: PASS_WITH_NOTES, high, accepted), consent recorded in
  the registry (Le's instruction).
- Flip by `gh` (Le's choice, 2026-11-13: "Flip now via GitHub"), not by
  `lean-pkg publish`, whose checklist refuses two bookkeeping items: 1408
  compared helper theorems not credited to a coverage row (283 of them
  `reusable`), and the coverage page needs a posted manuscript pin or
  `--allow-private-manuscript`. The release notes state the gap. Registry:
  record moved to the public checkout and gated at `ed66b5b` (status
  verified-private; `doi-minted` refused until `publish` marks it public).
  To fix in v0.10.0.
- Title: kept the a284420 title (Le, 2026-11-13).
- Zenodo: Le switched the repository on; GitHub release v0.9.0
  (https://github.com/chenle02/stratonovich-ham-second-moment-lean/releases/tag/v0.9.0)
  minted version DOI 10.5281/zenodo.24199105 and concept DOI
  10.5281/zenodo.24199104 (record isSupplementTo .../tree/v0.9.0, creator
  Chen, Le, version 0.9.0).
- The private development repository is `chenle02/stratonovich-ham-second-moment-lean-dev`
  (all history, milestone tags L0-L10, waves L11-L14 in progress).

## v0.10.0 started (Le, 2026-11-13)

Le: "Start v0.10.0 for the public companion: map the 1408 helper theorems,
fix the coverage page and lean-pkg publish, and add the generated verification
and coverage pages to the site." Answers the same day: state "L12 gate state"
(L10 + L11 + L12, dev `56fc59e` plus its gate docs once the L12 receipts and
Easley are in); helpers "Credit labelled, smoke the rest": compared theorems
whose ledger row carries a direct manuscript label with a coverage row are
credited to that row; all other compared theorems go to a separate comparator
configuration declared a smoke check (compared, not credited to a result);
helper claims marked `reusable` among them are relabelled `internal` in
claims.yaml, so both receipts are re-cut. The book's 1.1.0 pin follows
(#24/#16 to agree). Recorded locally during #16's book-release push freeze.

## Book 1.1.0 pin (L12): Appendix F review paragraph (sent to #24, 2026-11-13)

Pin: verified `56fc59e` (tag L12-gate), coverage `cb18a64` (or a later docs-only successor). Supersedes the L10 paragraph above.

The statements added in waves L10, L11 and L12, and the changes those waves made to existing entries of the coverage record, were checked against the manuscript in correspondence reviews done by AI models from a different family than the one that wrote the formal statements, under the conventions the author fixed in wave L9. Each wave's reviews found documentation corrections only, and no error in a Lean proof; the corrections were made and confirmed by a confirmation review that passed with high confidence. The author accepted wave L10 on 2026-11-13, recording that one assembly step of Proposition P:interval-coefficients assumed a bound on the pairings of the cut-off coefficients that the manuscript does not state as a hypothesis; wave L11 proves that bound from a supplied expansion of the coefficients. The author accepted wave L11 on 2026-11-13, with two further modelling choices recorded: the Gaussian space is represented by Hermite coefficient vectors, and Lemma L:fock-form and Lemma L:interval-contractions hold with the manuscript's hypotheses but narrower conclusions, on a Fourier-side model not identified with the physical-space operators. The author accepted wave L12 on 2026-11-13, recording that the smoothed covariance of Lemma L:damped-homogeneous-norms is modelled by its density; with that choice the lemma is formalized in full. Lemma L:terminal-wick is now formalized in full for the constructed chain measures, Lemma L:higher-riesz in dimensions two and three, and Lemmas L:source-finite-comparison and L:tube-half-action in full. The record states what remains open: Theorem T:white-moment-bounds is formalized for the variational value S_2^pos rather than for C_2, with the white spatial energy supplied; Proposition P:tube-rayleigh-transfer is proved from two supplied facts of Lemma L:tube-closed-geometry; Corollary C:static-interaction and Proposition P:static-phase-all-orders still rest on supplied analytic inputs; and Theorem T:intrinsic-occupation-ceiling remains narrower. These reviews are not a human verification, and they do not check the analytic inputs that stay outside Lean.
