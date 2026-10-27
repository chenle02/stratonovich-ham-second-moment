# HANDOFF

**Last updated**: 2026-10-26 23:59
**Project**: Article-Stratonovich-HAM-Second-Moment (second moment of the Stratonovich hyperbolic Anderson model with time-fractional noise)
**Wiki page (authoritative strategy)**: `../SPDEs-wiki/content/projects/stratonovich-ham-second-moment.md`

---

## ⏭ Next session: where to stand and what to do

Stand in the repository root on `master`, level with `origin` (<HUB>). Set the run's goal to the **Goal statement** in `PROJECT-GOAL.md`, then start **math Round 1 = Gate G0** from `Progress.md` with the paper-dev workflow (`<HOME>/workspace/Le-AI-Lab/commands/paper-dev.md`). The Lean track (`lean-progress/`) stays at wave L0 until G0 produces a written, reviewed statement worth formalizing. Then stop at decision point 1 (end of Round 1) and report to Le.

## Pre-flight checks

1. `git fetch && git status -sb` → `## master...origin/master` with no ahead/behind and a clean tree.
2. `sha256sum sources/chen-2026-author/aap-chen-2025.pdf` → `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.
3. `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex` → exit 0; then `grep -c '^!' notes/*.log` = 0 and no `Overfull` or `undefined` lines.
4. `ls -l All.bib` → symlink to `../refdb/All.bib`; `grep -c '{chen:25:time-dependency,' All.bib` = 1.
5. `lean-pkg doctor` → exit 0 (registry readable). Do not create a package yet.
6. Read, in order: `AGENTS.md`, `PROJECT-GOAL.md`, `Progress.md`, `sources/SOURCE-MANIFEST.md`, the notes, `lean-progress/PROGRESS.md`. Read the source pages marked in bold in the manifest from the **rendered** PDF (`pdftoppm -f N -l N -r 150`), not the text layer.

## Concrete deliverables for the next session

| Deliverable | File | Definition of done |
|---|---|---|
| G0(a) cross-term formula | notes, new section after §2 | 𝔼u² = Σ_{m+n even} 𝔼[S_m(g_m)S_n(g_n)] justified from (2.13), (2.18), (2.21) and Theorem 1.1; each term written in the form of (3.6) with n₁=m, n₂=n; proof ends with "This proves …" |
| G0(b) diagnosis of e^{Ct²} | same section | Remark 5.1 reproduced from (2.13), (4.4); the exact step where exponent 2 enters instead of κ identified and written out |
| G0(c) verdict | same section + `Progress.md` | "Theorem 3.1 route viable / not viable for G:upper", with the counting argument; a no-go recorded under *Failed routes* if not viable |
| Cross-family review | `reviews/2026-10-27-round1/` | Claude Opus 5.5 skeptic report on the frozen packet; every finding adjudicated in `Progress.md` |
| Clean build + state | notes PDF, `Progress.md`, `HANDOFF.md` | Clean build committed with the source; round-close protocol done; HANDOFF refreshed for Round 2 |

### After the immediate step
Round 2 (G1 calibration) and Lean wave L1 (the G0 counting statement) start only after Le reads the Round 1 report (decision point 1).

## Success criteria for the immediate next step

1. The cross-term formula has a complete proof that cites only pinpointed results of the author version.
2. The diagnosis names the specific inequality or count (pair-partition count, a norm in (3.3)–(3.5), or the (m,n) summation) responsible for t² versus t^κ.
3. The verdict is supported by an explicit counting estimate, not by intuition.
4. The Opus skeptic report exists, was produced on the frozen packet, and every finding is adjudicated.
5. Build clean (0 errors, 0 undefined references, 0 overfull boxes); commits pushed; <HUB> at the same SHA.

## Anti-success criteria

[held back: collaborators' unpublished work]

## What the previous sessions produced

[held back: collaborators' unpublished work]

## Repo & git state at handoff

| Repository | Branch | HEAD | Remote |
|---|---|---|---|
| Article-Stratonovich-HAM-Second-Moment | master | see `git log -1` (the HANDOFF commit) | <HUB> bare, synced |
| SPDEs-wiki | v4 | `ef2039b2d` | GitHub + <HUB> synced |
| refdb | main | unchanged by this setup | — |

## Operating notes

- Commit atomically per unit of work and push after each; then sync <HUB> (`AGENTS.md`, Git). Stage only your own paths.
- Refresh this file at every round close; keep the parser-facing `##` headings exactly.
- Report honestly: a no-go or a partial result is a result; never stamp a proof complete before its cross-family review.

[held back: collaborators' unpublished work]

## Risks to monitor

[held back: collaborators' unpublished work]

### Previous failure modes
- On this machine the SPDEs-wiki push hook needs a Python with the wiki dependencies and `ruff==0.11.13` (<HUB>'s version); a newer ruff flags untouched scripts. Use a scratch venv and `SPDES_WIKI_PYTHON`; never bypass the gate.
