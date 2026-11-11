# Lean companion publication plan (release sequence 3a, step 1)

Authority: this file records the plan and Le's decisions on it. The plan
text below is the one sent to #16 on 2026-11-11, followed by the Zenodo
addendum. Nothing on GitHub or Zenodo happens before Le's explicit go
(planned Nov 29-30); the release candidate needs Le's approval after the
independent audit (Nov 26).

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
