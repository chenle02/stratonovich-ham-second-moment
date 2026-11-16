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

## v0.10.0 retargeted to the L14 state (Le, 2026-11-13)

Le (via #24): the book skips companion v0.10.0 at L12; book 1.1.0 pins the
public companion release that carries the final L14 state (`8f51004`). Le's
answer the same day: "Retarget v0.10.0 to L14". The L12 candidate
(`$SP/v010/pub`, dc7755e/7a5d573/40cfe87) is not published; v0.10.0 is rebuilt
from the L14 gate state (dev `8f51004` plus its receipts, Easley evidence and
gate record) with the same helper accounting (credit labelled rows, smoke the
rest, reusable helpers in the smoke set relabelled internal), fresh receipts,
an independent audit and the generated pages; it waits for the book repository
to be public so the manuscript can be pinned. Then: push, `lean-pkg publish`,
tag v0.10.0, GitHub release (Zenodo DOI), site, and the 1.1.0 pin to #24 with
an L10-L14 Appendix F paragraph.

## The book cites L14: v0.10.0 is re-anchored to the release SHA R (Le, 2026-11-13)

- Le decided that the book appendix (F/G) and the video series (#29) anchor to Lean L14, the public companion v0.10.0. This supersedes "book v1.0.0 pins v0.9.0" and the "Wait for the book" order. #16 relayed Le's confirmation and confirmed the sequence.
- The re-anchor is folded into v0.10.0 (Le: "Fold into v0.10.0"). It targets R, not 98f45bed (#3's C_dir rename), because notes/*.tex still changes before the release (#16).
- Sequence (#16, confirmed):
  1. #16 cuts R after #3's scientific closure and Le's typesetting pass and announces its full SHA.
  2. #22 re-anchors to R, gets the re-anchor reviewed and confirmed, and Le accepts it.
  3. #22 publishes v0.10.0: tag, GitHub release and Zenodo version DOI, with the manuscript pinned to R and its sha256.
  4. Re-pin: #24 does Appendices F and G; #16 does release_sync (VERIFICATION, README, HOW-THIS-WAS-BUILT, AI-USE, CHANGELOG, CITATION). Before #16 approves the push, #22 runs the remap R -> candidate, and it must show 0 shifted citations.
  5. The release date and cover date are set at F, the day of going public.
  6. At F: the strict rehearsal, the rule-33a trial audit, Le's accept file and the live export. #22 then adds a docs-only companion note recording F.
- The words Le must choose: at L14 two of the four main theorems are outside Lean, not three. This affects preface.tex:62 ("most of the main theorems are outside Lean"), Appendix F and the front-door files. #24 asks Le before step 4.
- State on the companion dev repo (private):
  - Branch reanchor-98f45bed at 1220baf holds the adopted C_dir wording only, and is comment-only.
  - The line remap is a rerunnable dry-run tool (run_reanchor.sh) that commits nothing. Its dry run against 98f45bed counted 8745 citations: 5093 shifted, 3427 unchanged, 225 hand-resolved, 4 already wrong at a284420.
  - Spot-check of the attribution (five multi-file modules, Codex GPT-6.1-Sol) is running.

### Re-anchor tool cleared for R (2026-11-14, overnight)
Four independent review rounds were run on the dry run against 98f45bed, all with Codex GPT-6.1-Sol at high effort, read-only. The evidence is kept in session scratch and will be copied to reviews/ with the review at R.
- Round 1 (FAIL): 4 wrong-file attributions and 3 ranges already wrong at a284420. The 3 were fixed in companion dev commit `2487458`, comment-only.
- Round 2 (FAIL): the guard's file candidates were too narrow (ClassOBridge's zero-case citation left at 303 instead of 309), and a header range was missed.
- Round 3 (FAIL): 8 citations the scanner had missed, in label + bare range, "and N-M" and "Nff." forms.
- Round 4 (INCONCLUSIVE/medium, only because the orchestrator's packet left out one generated file; those 3 rows were verified by hand): no remap error found. The census sample, all 37 printed changes and a search of 17 modules turned up no stale citation.

Tool state:
- A pattern-free census decides all 14972 uncaptured prose numbers; the run stops if any number is undecided.
- 8915 citations, 0 unresolved.
- The dry run at manuscript tip 2f534eda is identical to the one at 98f45bed.

## Book pin (L14 = v0.10.0): Appendix F and preface paragraph (approved by Le and sent to #24, 2026-11-14)

Pins (placeholders until v0.10.0 is published): verified = <v0.10.0 public commit> (replaces `6eb79c7`), coverage = <v0.10.0 coverage commit> (replaces `34b65d7`), version DOI = <v0.10.0 Zenodo DOI>. The concept DOI `10.5281/zenodo.24199104` is unchanged. This paragraph supersedes the L10 and L12 paragraphs above. Suggested use: the full text in Appendix F, and its first and last paragraphs in the preface.

The statements added in waves L10 to L14, and the changes those waves made to existing entries of the coverage record, were checked against the manuscript in correspondence reviews. The reviews were done by AI models from a different family than the one that wrote the formal statements, under the conventions the author fixed in wave L9. Each wave's reviews found documentation corrections only, and no error in a Lean proof. The corrections were made, and a confirmation review passed with high confidence.

The author accepted waves L10 and L11 on 2026-11-13:
- In wave L10, one assembly step of Proposition P:interval-coefficients assumed a bound on the pairings of the cut-off coefficients that the manuscript does not state as a hypothesis. Wave L11 proves that bound from a supplied expansion of the coefficients.
- In wave L11, the Gaussian space is represented by Hermite coefficient vectors. Lemmas L:fock-form and L:interval-contractions hold with the manuscript's hypotheses but narrower conclusions, on a Fourier-side model not identified with the physical-space operators.

The author accepted wave L12 the same day, recording that the smoothed covariance of Lemma L:damped-homogeneous-norms is modelled by its density; with that choice the lemma is formalized in full.

Waves L13 and L14 were accepted together, with three further modelling choices recorded:
- the second moment's two-chain pairing integrals are represented by a deterministic diagram model, with the mixed-moment expansion of Proposition P:mixed supplied as an input;
- the occupation spaces are modelled by their L² completions;
- H¹ is modelled as the graph of the weak gradient.

On these models:
- Propositions P:spatial-four-linear, P:occupation-physical-class, P:raw-occupation-energy and P:masked-auxiliary-norm, and Lemma L:variational-global-mean, are formalized in full.
- Theorem T:intrinsic-occupation-ceiling is formalized in both forms with the exact constant C_occ over the occupation class itself, without its moment sentence C_2 ≤ U_2.
- Propositions P:d1-upper and P:low-alpha-upper have their diagram values and coefficient bounds proved on the model, and their statements about the solution follow from the supplied P:mixed.

Open items in the record:
- Theorems T:full-upper and T:intrinsic-second-moment are outside Lean.
- Theorem T:white-moment-bounds is formalized for the variational value S_2^pos rather than for C_2, with the white spatial energy supplied.
- Several results rest on named inputs, each listed with the result that supplies it. These include Propositions P:mixed and P:three-transfer, the first-moment series, and the signed multiplier form.
- No theorem of the manuscript is verified end to end.

For this release the companion's line citations were re-anchored to the published manuscript, and the re-anchor was reviewed in the same way.

These reviews are not a human verification, and they do not check the analytic inputs that stay outside Lean.

### Re-anchor tool committed (2026-11-14)
The tool now lives on the private companion dev branch `reanchor-98f45bed` at `1fa1508`, in `reanchor/`. Session scratch is no longer the reference copy.
- **Not exported.** `.gitattributes` marks `reanchor/` (and itself) `export-ignore`, so `git archive` and the public release tree built from it contain neither. This matters because `overrides.json` and `census-decisions.json` quote manuscript context.
- **Not a build input.** The receipts are unaffected.
- **Contents:**
  - `tools/`: `run_reanchor.sh`, `reanchor_locators.py`, `census2.py`, `anchor_pin.py`, `anchor-changes.json`, `lean_comment_only.py`, `add_new_lines.py`, `cited_ranges.py`;
  - `overrides.json` (the hand resolutions, keyed on the a284420 side);
  - `census-decisions.json`;
  - `spans-new.tsv`;
  - `README.md`.
- **Usage:** from any checkout of the dev repository, with the manuscript repository at `<HOME>/workspace/svn/Article-Stratonovich-HAM-Second-Moment`:
  `reanchor/tools/run_reanchor.sh NEW_SHA [OLD_SHA=a284420] [COMPANION_REF=reanchor-98f45bed]`
  - Output goes to `${REANCHOR_OUT:-~/.local/state/stratonovich-reanchor}/run-<NEW8>/`, outside the repository.
  - Nothing is committed.
  - Before rerunning the same SHA: `git worktree remove --force <OUT>/tree; rm -rf <OUT>`.
- **Adding a notable manuscript change:** add one entry to `tools/anchor-changes.json`. An entry is used only if its SHA is an ancestor of NEW_SHA. The three entries now are 98f45bed (the C_dir rename), 6f27a8ec (the Chen attribution) and 9581d7c6 (the front-guide paragraph).
- **Tested from the committed location against 9581d7c6.** The result is identical to the scratch run: 8915 locator rows, the same tree, 2002 files scanned, and every check passes.
- At R: run the committed copy against R, then rebuild the v0.10.0 public candidate with receipts, then the re-anchor review and confirmation, then Le's acceptance.

## v0.10.0 and video dependency order (#16, 2026-11-15; agreed by #22 with three precisions)
Le chose option A for the release on 2026-11-15: the honest-standing release states every grade as recorded and upgrades none. R is issued only after Le's typesetting pass on master `33ed4ef7`.
1. R, after Le's typesetting pass.
2. #22 re-anchors the companion to R, verifies it and has it reviewed. Le accepts the v0.10.0 candidate. The acceptance is of the exact commit that step 3 tags.
3. #22 creates the IMMUTABLE v0.10.0 tag on a fixed commit SHA. This is not yet a public release, and no DOI is claimed.
4. #29 renders against R plus the v0.10.0 tag name and commit SHA. The on-screen identity uses these and never a DOI. #29 uploads the 11 episodes PRIVATE and collects the new IDs.
5. #22 publishes the v0.10.0 release, and Zenodo mints its DOI. Steps 4 and 5 depend only on step 3: they can run in either order or in parallel, and both must finish before step 6.
6. Re-pin. #24 puts the v0.10.0 DOI and the 11 new video IDs into the book, followed by one rebuild of the book, reader and combined editions. #3 reseals, #22 runs the zero-shift check, #16 verifies, and Le names the push. That push is F.
7. Rehearsal and trial audit, Le's accept file, then export and the repository flip. The new videos are PUBLIC no later than the flip, and the old ones are made Unlisted after each signed-out check. Le submits to arXiv (the book only).
The DOI and final links go into the video descriptions, which stay editable, so no video waits for a DOI.

#22's precisions (none changes the order):
- Step 3, a local tag before publication. The v0.10.0 tag is created on the local public-candidate commit and is NOT pushed to the public GitHub repository before step 5, because a pushed tag would make the commit public. The SHA is fixed from the moment the tag is created. #22 keeps a private backup (a git bundle on <HUB>) and gives #29 the tag name and the full commit SHA. #29 uses no GitHub URL for it until step 5.
- Step 5, the GitHub route as for v0.9.0. Push main and the tag, publish the gh release, and Zenodo mints the DOI. `lean-pkg publish` refuses while the manuscript is unposted, because the book stays private until F. The lean-pkg registry record stays verified-private until F; after F, #22 records it with lean-pkg.
- Step 6, the DOI as a docs-only successor. The Zenodo DOI is written into the companion by a docs-only commit on top of the tag, as `0966ef6` did for v0.9.0. The book pins are: verified = the v0.10.0 tag commit; coverage = the same commit, or the DOI successor if #24 wants the DOI-bearing docs. #22 sends both SHAs and the DOI after step 5.

### Lean-coverage badges in the book: contract and prerequisite (#5 asked, 2026-11-15)
- Source: the same `coverage.yaml` as Appendix F, keyed on `rows[].paper.label`. The meaning comes from `class` × `conclusion` only:
  - same-assumptions/full: 48 rows, 44 results plus 4 displays or remarks. Only these may be called "full".
  - same-assumptions/weaker: 16.
  - inputs-supplied/full: 1.
  - inputs-supplied/weaker: 34.
  - outside: 2.
  - no row: not formalized.
- An E: or R: row covers that display or remark only.
- Gates:
  - (a) Before R, a badge may change cited TeX lines (the re-anchor absorbs it). After R, a badge must add no line in a cited file, otherwise the zero-shift check at F fails.
  - (b) No scope strings in the book before F: they contain TeX line numbers that change at the re-anchor.
  - (c) Until v0.10.0 is published, the wording is "wave L14 (gate 8f51004), release pending", with no DOI or URL.
- Prerequisite, not started: no structured, approved label -> model-scope source exists. The M1-M6 register is prose, in the README and the scope fields. A regex finds M-numbers in 19 of the 101 rows, but it is incomplete, because some rows name their model in words only.
  - Before any rollout across the book, #22 builds a curated sidecar keyed by label (models plus a one-line qualifier), reads every row and has it reviewed. This waits for Le to choose the badge style.
  - Until then, unknown scope fails closed: no marker, never "full".

### Lean-marker draft map (2026-11-15; #16 asked for it as a held draft that does not depend on Le's style choice)
- The map is at `private/lean-markers/lean-marker-map.draft.json`, with a README beside it. Article `4e50f437`, sha256 `cb1defdf566c1b476258858a41de286e5cbaa748c25af1608c5f6fad0a289cce`. It is a HELD, UNREVIEWED draft.
- Source: 101 rows keyed by `paper.label`, from the companion `coverage.yaml` at dev `74a04f57`. Class and conclusion are identical to the L14 gate record.
- Markers by class × conclusion:

  | Marker | Rows |
  |---|---|
  | full statement | 48 |
  | narrower statement | 16 |
  | supplied inputs | 1 |
  | partial, with inputs | 34 |
  | outside (unmarked) | 2 |

- 0 HOLD rows. 26 rows name a registered model; 14 of them are "full statement".
- Models come only from M-codes named in the coverage text, from the README/ledger register consumers, and from reading the modules. No model is inferred from claim ids.
- The four rows first held were resolved by reading the modules:
  - C:static-interaction and P:static-phase-all-orders carry M2 through FockSandwichModel;
  - L:interval-contractions carries M2 through HermiteFock/FockForm;
  - none of the three uses M1;
  - T:white-moment-bounds has no registered model: joint representatives are a narrowing, not M5 or M6.
- The map contains no TeX line numbers and no scope strings.
- Still needed before production:
  1. an independent review of the map;
  2. Le's choice of badge style;
  3. #24's integration;
  4. the final words from the exact v0.10.0 coverage at the re-pin.

  Until then, unknown or unsettled entries stay unmarked and are never "full".

### Lean-marker map: independent review and repair (2026-11-16)
- **Review.** Codex GPT-6.1-Sol, high effort, read-only. The map's author was #22 (Claude), so the reviewer is from a different family. The run is review-complete, with verdict FAIL and medium confidence.
  - Mechanical check: PASS on all 101 rows.
  - Five major findings: missing registered models. M2 on L:fixed-split and P:interval-coefficients; M6 on C:intrinsic-spatial-bracket, L:occupation-rayleigh-selection and T:intrinsic-occupation-ceiling.
  - One further finding: the assignment policy, "codes named in the coverage text", was too narrow.
- **Verification.** #22 checked all five against the modules and accepted them. The coefficient-model objects are in FixedSplit and FiniteWordCutoff; the H1R-valued class O is in ClassOBridge. None of the five rows is a "full statement", and no marker category changed.
- **Systematic follow-up.** The new rule is: a row carries a model when a covered declaration's statement uses a construction the register assigns to it, judged by module and object. It was applied to all 101 rows in three ways:
  - against the register's module lists for each claim file;
  - against the direct imports of every model-free "full statement" row;
  - by reading every flagged declaration.

  No further missing model was found. These candidates were checked and rejected, with reasons in the map:
  - P:mild-construction (M2 appears only in proof steps);
  - L:positive-raw-embedding (M5 only);
  - P:spatial-four-linear (M6 only);
  - the three endpoint lemmas (no Green measure).
- **Result.** Map at Article `62394f18`, `private/lean-markers/lean-marker-map.draft.json`, sha256 `faa7bcdca1995f88c0cfa0844dc9e5977dc91f9d5c2c8f8f5dc172470f0d7fd2`.
  - 0 HOLD rows.
  - 31 rows name a model; 14 of them are "full statement".
  - Review evidence and the adjudication are in `private/lean-markers/review-2026-11-16/`.
- **Still to come.** #24 integrates the heading-line markers (Le's style choice), and #22 checks the built PDF against the map. The final words come from the v0.10.0 data at the re-pin.

### Lean-marker map: confirmation review (2026-11-16)
- **Review.** Codex GPT-6.1-Sol, high effort, read-only. The run is review-complete, with verdict FAIL and high confidence.
- **Passed:**
  - the diff `4e50f437..62394f18`: all five additions are supported, and no marker changed;
  - the mechanical check and the claim-file inventory, on all 101 rows;
  - 5 of the 6 rejected candidates.
- **One further missing model.** P:mild-construction needs M2. Its covered claim HermiteFock.gaussian_field_bound is stated in the Hermite coefficient model (HermiteFock.lean:597-605). #22 verified this and added M2. The marker stays "partial, with inputs (M2)", and the "full statement" rows are unchanged.
- **Map now.** Article `aee543e8`, sha256 `23b8b90172bb21cd7d64bb836f6c04cf28791c5605f0e8bc01b9fbad6f6c4c91`. 32 rows name a model, 14 of them "full statement". Evidence is in `private/lean-markers/review-2026-11-16-confirm/`.
- **Reviewer's limit.** 41 of the 48 "full statement" rows were screened by the claim-file/register join only. #22's module and import check covered all 101 rows.
- **Open for #16.** Accept the one-row repair as verified, or ask for a narrow recheck of that row.
- **Prototype check.** #22 checked #24's marker prototype (414 pages, map 62394f18) read-only:
  - 75 markers individually equal to their map rows;
  - all 96 equal in aggregate;
  - the outside rows unmarked.

### Lean-marker map: bounded review of P:mild-construction and the 41 "full statement" rows (2026-11-16; #16's pre-re-pin item, not blocking R under option A)
- **Review.** Codex GPT-6.1-Sol, high effort, read-only. The run is review-complete, with verdict INCONCLUSIVE and medium confidence. Findings: none.
- **P:mild-construction:** PASS (M2 present).
- **The 41 rows**, each decided individually:
  - 8 PASS, with every credited declaration read;
  - 33 PARTIAL, with the paper wrapper and its key definitions read but not every helper claim.
  - Count reconciled: the report has 42 checks, P:mild-construction plus the 41 rows. Its 9 PASS are P:mild-construction and 8 rows.
  - In every row the statements examined support the listed models exactly. The grade reflects incomplete reading of helper claims only.
- **Disposition:** no repair, and the map stays at `aee543e8`. The residual risk is a helper claim stated in a model. It is covered by #22's module check, which matched every claim file against the register's module lists and checked the direct imports of every model-free full row.
- **Evidence:** `private/lean-markers/review-2026-11-16-full/`.
- **Marker candidate b74af3ef (option A, Appendix F words).** #22 checked it read-only.
  - One wrong marker: L:spatial-fourier-bound is printed "full" in Appendix F but its marker says "narrower". The cause is a generator bug: cross-references inside scope text were parsed as rows.
  - The fix (take only row-leading references) was sent to #24. With it, 0 mismatches.
  - H:homog and L:compact-raw-profile are cross-references, not Appendix F rows, and stay unmarked.
  - Every other check passed: 74 markers equal the data, 22 reserved slots are empty, and the outside and equation rows are unmarked.
  - The recheck is pending on #24's regenerated SHA.

- **#16's call (2026-11-16).** INCONCLUSIVE does not meet the HIGH standard for a public "full statement". Before the re-pin, but not blocking R, the same reviewer finishes every credited helper claim of the 33 PARTIAL rows, read-only, for a decided PASS or FAIL per row. Any row with a helper stated in a model is repaired and rechecked. The re-pin uses the map only after that result.
  - Running: three parallel batches of 11 rows each (about 230 credited declarations per batch).
- **Result (2026-11-16).** The same reviewer read every credited declaration of the 33 PARTIAL rows in three batches: 232, 234 and 231 declarations.
  - Every one of the 33 rows was decided PASS. There were no findings: no missing or unsupported model.
  - Batch grades: batches 2 and 3 PASS, high confidence. Batch 1 INCONCLUSIVE, medium confidence, only because whole source files were not read beyond the credited statements; its 11 row decisions are definite.
  - So all 41 "full statement" rows are decided PASS, with the models exact. The map stays at `aee543e8` and is ready for the re-pin.
  - Evidence: `private/lean-markers/review-2026-11-16-helpers/`.
- **Marker candidate 075df319 (successor to b74af3ef; #22's read-only recheck): PASS.**
  - All 96 slots are correct against the row-leading Appendix F rows: 74 worded markers (26 full, 18 narrower, 30 partial) and 22 empty.
  - The 74 printed PDF markers equal the data, and L:spatial-fourier-bound now reads "full statement".
  - The outside and equation rows are unmarked.

### Appendix F at the L14 gate before R (2026-11-16; Le's decisions, relayed by #16)
- Appendix F gets its L14 content before R. #24 owns the generator and the generated files; #22 owns the data payload; #3 audits the wording.
- The gate is named exactly as "wave-L14 gate (development commit 8f51004 of the private development repository; to be released as v0.10.0)". There is no tag URL or DOI until the re-pin.
- The data: rows from coverage.yaml at dev 74a04f57; markers from map aee543e8; receipts at 8f51004. The ledger "verified/open" sentence is omitted, because it cannot be computed at 8f51004 with lean-pkg 0.29.0.
- No manuscript TeX line numbers anchored to a284420 are printed. #22 supplies the line-free scope, inputs and proves/not-formalized texts in `appf-l14-payload.yaml` (in `~/.local/state/stratonovich-appf-l14-inputs/`). The re-anchored v0.10.0 data can restore line numbers at the re-pin.
- Le dropped one sentence from the pre-R L10-L14 paragraph: "For this release the companion's line citations were re-anchored to the published manuscript, and the re-anchor was reviewed in the same way." It returns at the re-pin, when it is true. The rest of the paragraph stays as approved.
- Le asked for margin markers on the three displayed equations, and they stay. The legend drops "displayed equations carry no link".

### #22's check of the held Appendix F L14 chain (2026-11-16): PASS
- **Chain checked:** fa49a953 (Appendix F successor, parent 046572f3), b6c515b4 (combined edition), 29edae78 (#3's reseal, manifest only). All are held, with no push.
- **Data:**
  - the payload is `appf-l14-payload.90315b65.yaml`, which is 7daed384 plus 8 `no_analytic_input` flags; #3's audits found no corrections;
  - the inputs come from companion dev 74a04f57 (coverage) and the gate 8f51004 (receipts);
  - the margin notes follow map aee543e8.
- **Pin:** #24's `pin_companion.py` (from fa49a953), run by #22 with the companion and its receipts, as `pin_companion.py <companion> 8f51004 74a04f57 --successor-check verify_l14_successor.py`, writes coverage.yaml, completion.md, coverage-commit.txt, lean-receipt-summary.json, coverage-scope-tex.yaml and successor-check.json byte-identical to the committed files. The ledger summary is the stored one for 8f51004.
- **The successor check** (`verify_l14_successor.py`; record 769717ba) has the exception categories named:
  - Lean library comment-only;
  - Challenge.lean and Solution.lean drop only the restated Cx.ext_iff;
  - two generated-declaration claims removed;
  - 491 status relabellings;
  - coverage claim lists and three text fields.

  #16 accepted it as a checked exception.
- **Book PDF at fa49a953 (419 pages):**
  - 101 Appendix F rows in categories matching coverage class × conclusion (48/16/1/34/2);
  - 99 margin notes on 198 links, each equal to its own row and to the map, none missing or extra, no outside row marked;
  - the 8 flagged rows print "Assumptions and limits" with the named text, and the old generic sentence appears 0 times.
- **Remap dry run at fa49a953:** it passes (0 unresolved, census decided, comment-only, copies identical). Against 046572f3, all 4914 main-TeX citations move exactly +5 (the `\lcCategory` macro in the preamble), and nothing else changes. Tool on dev branch reanchor-98f45bed at 3908d0f.
- **Carry at the re-pin (companion coverage.yaml, docs-only, v0.10.0):**
  1. Replace the summary sentence with the one #24's generator now substitutes ("…; the entries distinguish supplied hypotheses, where present, from analytic work left outside Lean"). The override then becomes a no-op, and #24 removes it.
  2. Correct the input wording of the 8 no-analytic-input rows. "which enter the Lean statements as explicit hypotheses" overstates: their Lean statements take only parameter conditions, and the analytic facts are outside Lean. These rows are L:driver-holder-limit, L:driver-interval-limit, L:exact-canonical-scaling, L:raw-block-inputs, P:actual-wave-form, P:gram-entrywise-comparison, P:gram-positive-optimizer and P:raw-block-original-lower.
- **The AI-use L14 block** (#3's a54aff89) is not in this chain. Per #16 it goes in at the re-pin through the release_sync template; #22 has confirmed its counts.

### Companion coverage.yaml corrections for the re-pin (2026-11-16; done)
These are on the private dev branch `reanchor-98f45bed`: `e415c36` (coverage.yaml) and `4f07611` (re-anchor census decision). Pushed; <HUB> fetched. Both are docs-only: coverage.yaml is not a build input, and the Lean is unchanged.
1. **summary.**
   - It carries #24's Appendix F sentence verbatim ("…; the entries distinguish supplied hypotheses, where present, from analytic work left outside Lean").
   - It is shortened to the coverage/1 limit of 400 characters, with the meaning unchanged: numerals, and "in full" for "with every conclusion".
   - New summary (392 characters): "With the manuscript's hypotheses, 48 labelled results are formalized in full and 16 with a narrower conclusion; P:tube-rayleigh-transfer in full with two inputs supplied; steps, parts or narrower forms of 34 further labelled results; the entries distinguish supplied hypotheses, where present, from analytic work left outside Lean; T:full-upper and T:intrinsic-second-moment are outside Lean."
   - At the re-pin, Appendix F prints this wording. #24 removes the generator's summary override, and #3 audits the wording.
2. **inputs of the 8 no-analytic-input rows** (L:driver-holder-limit, L:driver-interval-limit, L:exact-canonical-scaling, L:raw-block-inputs, P:actual-wave-form, P:gram-entrywise-comparison, P:gram-positive-optimizer, P:raw-block-original-lower):
   - New text: "none beyond the paper's hypotheses: the checked Lean statements assume only parameter conditions; the analytic and probabilistic facts of the proof are outside Lean (see docs/statement-ledger.md, section <Module>)".
   - L:raw-block-restart and P:white-spatial-energy, which have real hypotheses, keep their wording.
   - The payload's ascii is regenerated from this at the re-pin.

Checks:
- `lean-pkg coverage check`: schema PASS. The only failure is the expected "manuscript unposted".
- `verify_l14_successor.py` 8f51004 -> e415c36: ALLOWED-SUCCESSOR. Lean library comment-only; coverage changes only in claims, inputs (9), conclusion_scope and note.
- Remap dry run at fa49a953 with the new head: passes after one recorded census decision ("16" in the summary is a count). 14974 numbers decided.

### #22's check of the held Appendix G chain (2026-11-16)
- **Chain checked:** a906b4a1 -> b2b34fc3 -> 81fc189e -> 05e65c2e -> 995a56bc (ledger pinned, Appendix G counts) -> 1d64c44a (combined). All held, no push.
- **VERIFICATION.md at 995a56bc: data correct.** All 253 rows were cross-tabulated against coverage.yaml at 74a04f57:
  - 44 formalized in full;
  - 16 narrower conclusion;
  - 1 every conclusion, inputs supplied;
  - 34 inputs supplied;
  - 2 outside Lean;
  - 156 no Lean claim.

  No other combination occurs, and every claim count equals its row.
- **Legend:** #16's sentence ("…steps, parts or a narrower form of the result, as listed in the companion's statement ledger…") is fine, because the ledger lists every claim row. No successor is needed.
- **Table G.1** (`notes/verification-status-data.tex`): the numbers are correct.
  - 44 + 16 + 1 + 34 + 2 + 156 = 253.
  - The column sums 31 / 72 / 82 / 35 / 33 match.
  - \vsLeanAny = 95; \vsOutside = two.
  - **Wording issue sent to #16 (open):** the row label "Steps checked, inputs supplied" (and VERIFICATION.md's class name "inputs supplied") overstates for the 8 rows whose checked steps take no analytic input, the same point as Appendix F's group heading. Suggested: "Steps checked; inputs supplied or left outside Lean". Class and counts are unchanged.
- **Remap dry run at 1d64c44a: PASS** after 15 new text-anchored overrides (dev branch reanchor-98f45bed, `f7069cf`, pushed; <HUB> fetched).
  - The reworded free-phase sentence in the proof of P:interval-coefficients (approved by Le; #3's citation of the energy calculation in P:static-phase-variance) lies inside 15 cited statement-and-proof ranges (FiniteWordCutoff, FixedSplit, IntervalScalar, coverage, ledger).
  - Each now maps by the text of its first and last lines to exactly the diff-mapped endpoints. Three ranges that ended on a blank line now end on the line before it.
  - Main-TeX shifts: +8 before the edit (the Chapter 3 guide sentence), +11 after it. Nothing else changes.
  - Census 14974/14974 decided; Lean comment-only; comparator copies identical.
- **Renamed-cell recheck at the corrected tip 4171c4d7 (2026-11-16): PASS.** Chain: 15d2d25e -> b6f7da39 -> 52421603 -> 90296c39 -> 6791e487 -> c1ced0e3 -> c88827bb -> 4171c4d7.
  - VERIFICATION.md: all 253 rows equal coverage.yaml at 74a04f57.
    - The 34 inputs-supplied/weaker rows read "steps checked", following #16's decision of 22:43.
    - The single inputs-supplied/full row keeps "every conclusion, inputs supplied".
    - 44 / 16 / 2 / 156 are unchanged, no "inputs supplied" class cell remains, and every claim count equals its row.
  - The legend keys "steps checked" and "every conclusion, inputs supplied" are present. The provenance line reads "Manuscript read at revision 6791e48", per #3's fix.
  - Table G.1 row: "Steps checked; inputs supplied or left outside Lean", 8 / 11 / 7 / 8 / 0 / 34. The counts are unchanged.
  - No cited TeX file changed since 1d64c44a. The remap pass with overrides `f7069cf` therefore still holds for this tip.
  - From the Lean side the chain is ready for #3's audit and manifest-only reseal and for #16's verification.
- **Recheck at the replacement candidate d889e2e1 (2026-11-16): PASS.** #24 withdrew 4171c4d7. The chain is now 90296c39 -> e8434f71 -> 948cb27d -> d889e2e1, i.e. 90296c39 plus the rename and the read-revision label.
  - VERIFICATION.md: all 253 rows equal coverage.yaml at 74a04f57 (44 / 16 / 1 / 34 / 2 / 156).
    - The 34 partial rows read "steps checked", and the single row keeps "every conclusion, inputs supplied".
    - No "inputs supplied" class cell remains, and the claim counts are equal.
  - The provenance line reads "Manuscript read at revision b6f7da3", this chain's read point.
  - Table G.1 row: "Steps checked; inputs supplied or left outside Lean", 8 / 11 / 7 / 8 / 0 / 34.
  - The data lines of VERIFICATION.md and verification-status-data.tex are byte-equal to those at 4171c4d7, apart from the read revision.
  - No cited TeX file changed since 90296c39, so the remap pass with overrides `f7069cf` holds.

### Proof-readability rewrite: Lean impact and the pilot measurement (2026-11-16)
- **Context.** Le asked #24 and #7 to make all proofs reader-friendly. #22 measured the companion's exposure:
  - of 8278 hand-written TeX-line citations, 4322 (52%) lie entirely inside proofs, and 4503 overlap one;
  - by file: main .tex 2676, spatial_occupation 449, covariance_foundation 288, unmasked_variational 239, occupation_ceiling 216, and others;
  - many companion sentences also quote or paraphrase proof steps.

  Rewriting proofs edits these lines rather than shifting them.
- **Options sent to #16 and Le:**
  - (a) Rewrite before R and do a large re-anchor by reading, with a review round.
  - (b) Rewrite before R with a per-file step map (old proof lines -> new lines, exact or inexact), so the remap stays mechanical. #24 generates the maps; #22 adds a step-map input to the re-anchor tool.
  - (c) Coarsen the in-proof citations to "in the proof of <label>" at the re-pin.
  - (d) Defer the rewrite until after v0.10.0.

  #22 recommends (b), or (c) as the fallback.
- **Step-map format (agreed with #24).** One JSON file per rewritten .tex file: {file, old_rev, new_rev, segments: [[old_start, old_end, new_start, new_end, exact|inexact]]}.
  - The segments cover every line of each old proof body, with no gaps or overlaps.
  - Kept labels and \eqref anchors appear as exact one-line segments.
- **Pilot 118de5f7** (held; parent cdde711c; notes/integrated_compact_gaussian.tex only; #7 editor, #24 gate):
  - 10 of 10 proofs rewritten; 87% of old proof lines kept byte-identical.
  - Book 427 -> 430 pages.
  - 2 AUDIT comments, both in the sample proof L:cutoff-factorization.
  - Map: 63 segments, 13 inexact.
- **#22's measurement.** The companion cites this file 140 times: 79 in or overlapping a proof, 61 outside.
  - **140 of 140 map mechanically:** every cited old line is byte-identical at its new position, and none touches a reworded line. The 43 inexact lines of the sample proof carry no citation.
  - **72 of the 79 in-proof citations map line for line.**
  - **7 map by endpoints with inserted reader lines inside.** These are whole-proof ranges in FiniteGaussianMatrix.lean and the ledger, e.g. 49-92 -> 60-112 and 101-180 -> 121-212. They are the existing span case.
  - **0 need reading.**
- **Caveat.** The pilot is mostly insertion. The share of citations landing on reworded lines must be measured per file as the rewrite proceeds; the main .tex alone has 2676 in-proof citations.
- **Open, for Le:** the depth of the rewrite, the Lean option, and how rewritten proofs are reviewed (#3's per-file packets). #16 sequences it relative to R.
