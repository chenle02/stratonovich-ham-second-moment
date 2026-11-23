# PROGRESS.md — Lean track (lean-dev authority)

> Authority for the **Lean companion** of Article-Stratonovich-HAM-Second-Moment
> (per the `lean-dev` skill). The mathematics authority is `../Progress.md`.
> `.lean-dev-state.json` mirrors this file and changes only together with it.

## Status

| Track | Current item | State | Since | Next action | Blocking on |
|---|---|---|---|---|---|
| Proof | Wave L20 CLOSED (dev main `e04987d`, tag `L20-gate`); wave L21 (`TubeAttained`) GATE EVIDENCE COMPLETE (gate `38a3e00`, receipts `39c4365`, Easley `ade3f31`) | L21: READY FOR LE'S CLOSURE | 2026-11-23 | Le closes L21 -> merge, tag `L21-gate` -> re-anchor -> review -> v0.11.0 | Le (L21 closure; fence approvals `TubeAttained`, `TubeTail`) |
| Release | v0.10.0 | LINKED (public tag on `261cc68`, version DOI 10.5281/zenodo.24295453; book Appendix F pins it) | 2026-11-18 | v0.11.0 (L15) only if Le wants one | Le |

## Links
- Paper progress: `../Progress.md` (mathematics authority); release sequencing: `RELEASE-PLAN.md` in this folder.
- Companion repos: dev `github.com/chenle02/stratonovich-ham-second-moment-lean-dev` (PRIVATE; local `../../Project-stratonovich-ham-second-moment-lean`); public `github.com/chenle02/stratonovich-ham-second-moment-lean` (local `../../<PRIVATE-PROJECT>`), site on its gh-pages.
- Registry: lean-pkg `stratonovich-ham-second-moment-lean` (status public, promoted at public `dc46f3a`, 2026-11-18).
- Coverage: the companion's `coverage.yaml`, `COMPLETION.md` and `docs/statement-ledger.md`.

## Status detail (kept current; updated at every milestone)

Last updated: 2026-11-23: **wave L20 gate CLOSED by Le** (dev main `e04987d`, tag `L20-gate` on `5cdd493`); wave L21 gate in progress. Earlier: 2026-11-23: **wave L19 merged** (dev main `d813957`, tag `L19-gate` on `fe9f1de`, receipts `5e2b86f`) and **wave L20 in progress** (L20-0 launched; R and L21's item started early). Earlier: 2026-11-22: **wave L19 gate CLOSED by Le** (merge pending receipts) and **wave L20 APPROVED by Le** (checked proposal, default answers to all thirteen decisions). Earlier: 2026-11-21: **wave L19 APPROVED by Le** (checked proposal, default answers to all thirteen decisions; L19-0 launching). Earlier: 2026-11-21: **wave L18 gate CLOSED by Le** at dev `6e4644d` (tag `L18-gate`; merged to dev main `470ee26`). Earlier: 2026-11-21: **wave L18 APPROVED by Le** (checked proposal, default answers to all thirteen decisions). Earlier: 2026-11-21: **wave L17 gate CLOSED by Le** at dev `68d0c5e` (tag `L17-gate`; merged to dev main `02f922f`). Earlier: 2026-11-20: **wave L16 gate CLOSED by Le** at dev `ebac849` (tag `L16-gate`; merged to dev main `38ac748`); L17 launching. Earlier: 2026-11-20: **wave L15 gate CLOSED by Le** at dev `18c5c1d` (tag `L15-gate`; gate record `54d3313` on dev main). Earlier: 2026-11-19: freeze lifted for **L15-UM only** (Le, 2026-11-19: "lift the freeze for L15-UM only and draft the L15 proposal"). L15 is PROPOSED below, not approved; nothing is built. The book is public (v1.0.0, 1.0.1, 1.0.2), and the companion is public at v0.10.0, the release the book's Appendix F pins.

| Item | Current state |
|---|---|
| Current wave | **L21 GATE IN PROGRESS** (`TubeAttained`, Le's end point 2026-11-23): gate commit `38a3e00` on `wave-l21/int` (59 / 22 / 1 / 30 / 2 / 106; coverage 118 rows 85 / 31 / 2; claims 6632); GPT-6.2-Sol docs PASS_WITH_NOTES + one FAIL on comment wording (MINOR, deferred to v0.11.0 release prep), docs repairs `adeac06`; Easley `ade3f31` (2/2 fresh, 212/212 default); receipts running. L21 is the last proof wave |
| Last closed gate | **L20**, closed by Le 2026-11-23 at dev `5cdd493` (tag `L20-gate`; receipts `4842df8`; Easley `1b94926`, `leanchecker --fresh` 12/12 and default 211/211; docs-only repairs `d3b2f8e`, `9706469`, `4fe5c33`, `fdbb0ae`; COMPLETION milestone `e04987d` = dev main; scratch-registry `gate --check` exit 0 at `5cdd493`, `4842df8` and `e04987d`). Previous: L19 at `fe9f1de`, L18 at `6e4644d`, L17 at `68d0c5e`, L16 at `ebac849`, L15 at `18c5c1d`; L13 and L14 at `8f51004` |
| Manuscript anchor | Companion line citations anchored to `39f2597a` (R; re-anchor reviewed and accepted with v0.10.0; dev tag `reanchor-39f2597a` on `402b646`). Book releases: v1.0.0 = original `86cf977b` (public `51a02011`, tag commit `643d1dcc`), v1.0.1 (public `a1c1a8e6`), v1.0.2 = original `c3c2431d` (public `a9d147d8`, tag commit `42fd6a0e`). R to v1.0.2 changes no cited line for v0.10.0 (zero-shift checks of every candidate F, G, 1.0.1, 1.0.2). R itself is a dropped merge in the public history; its TeX equals public `a6fc8b9b` |
| Companion | PUBLIC: v0.10.0 (L14), `chenle02/stratonovich-ham-second-moment-lean`, tag `v0.10.0` on `261cc68`; version DOI 10.5281/zenodo.24295453, concept 10.5281/zenodo.24199104. main `d659c59` (docs-only since the tag: book release note, arXiv pin `arXiv:2611.23014v1` in coverage.yaml, book site and concept DOI 10.5281/zenodo.24342309 in README and CITATION.cff); gh-pages `a265332`. lean-pkg registry: status **public**, promoted at `dc46f3a` (2026-11-18). Development: `...-lean-dev` (PRIVATE), dev main `e9f7bf6`, branch `reanchor-39f2597a` `402b646` |
| Claims | at the L20 gate: 6620 (5314 theorems, 1306 definitions); comparator 2049 credited + 3265 helpers. At the L19 gate: 6314. Public v0.10.0: 4502 |
| Coverage rows (117, at the L20 gate) | 84 same-assumptions, 31 inputs-supplied, 2 outside |
| Manuscript labelled results (220 T/P/L/C; per-label table in the companion's COMPLETION.md) | At the L20 gate: 59 whole with the manuscript's hypotheses; 21 same hypotheses, narrower; 1 whole with named inputs supplied; 30 steps or narrower with inputs supplied; 2 outside (`T:full-upper`, `T:intrinsic-second-moment`); 107 not formalized. No theorem end to end |
| Key named inputs still supplied | `DiagramLimits` (L18), `MixedMoment` and `FirstMomentSeries` (L19, last explicit use removed at L20), the Riesz `hH` (L20) DISCHARGED. Still supplied, by Le's end point (2026-11-23): `SignedMultiplierForm`, `ThreeTransfer`, `TubeTail`, `CutoffCompact`; `TubeAttained` until the L21 gate |
| Narrowed rows to restore | none scheduled. `L:positive-raw-embedding`: conclusion full with nothing supplied at the L16 gate (Le, 2026-11-20: "Upgrade L:positive-raw-embedding to full; keep P:cameron-temporal-map weaker."); `P:cameron-temporal-map` stays narrower |
| External kernel replay (Easley via <MACHINE>, `leanchecker --fresh`) | every library module through wave L14 at `8f51004` (142/142 plus default); wave L15 at `315a332`: the 4 new modules `--fresh` 4/4, default mode 146/146 (`verification/leanchecker-easley-wave-l15/`, `c081b0d`); wave L16 at `ebac849`: the 15 new modules and the umbrella `--fresh` 16/16, default mode 161/161 (`verification/leanchecker-easley-wave-l16/`, `c4df976`); wave L17 at `68d0c5e`: the 15 new modules and the umbrella `--fresh` 16/16, default mode 176/176 (`verification/leanchecker-easley-wave-l17/`, `0bf7a39`); wave L18 at `6e4644d`: the 13 new modules and the umbrella `--fresh` 14/14, default mode 189/189 (`verification/leanchecker-easley-wave-l18/`, `eb19140`) |
| Book Appendix F (#24) | pinned to public v0.10.0 (coverage `142afced`, receipt commit `c8d8e07`, DOI 24295453) in v1.0.0 to v1.0.2. A later companion release changes Appendix F only if a book release re-pins it (Le's decision) |
| Milestone tags (companion, annotated, pushed) | `L0-companion-created` ... `L12-gate` 56fc59e, `L13-gate` and `L14-gate` 8f51004, `reanchor-39f2597a` 402b646, `v0.10.0` 261cc68, `L15-gate` 18c5c1d, `L16-gate` ebac849, `L17-gate` 68d0c5e, `L18-gate` 6e4644d, `L19-gate` fe9f1de, `L20-gate` 5cdd493; a new tag at every gate closure |
| Completion table | companion `COMPLETION.md` (milestones + status of all 220 labelled results), regenerated at every milestone |
| Board (docs/community) | `2c54248`: L7 closure recorded; B3, B4, B9 reserved |
| Compute | Office (36 cores, 62 GB, 258 GB free, load below 1 on 2026-11-18) hosts L15; Easley only via <MACHINE> (Le, 2026-11-13). `lean-pkg page --site` on the full package takes 2 h 20 min to 2 h 40 min on <MACHINE>; start it right after the last coverage or claims change |
| Decisions open for Le | the L21 gate (fence approvals `TubeAttained`, `TubeTail`); v0.11.0 acceptance (L15-L21, one release); release of gaussian-chaos-lean (frozen). Lean end point (Le, 2026-11-23, option A): the companion closes after L21; `SignedMultiplierForm`, `ThreeTransfer`, `TubeTail`, `CutoffCompact` stay supplied |
| Next actions | L21 receipts -> report -> Le closes L21 -> merge, tag `L21-gate` -> re-anchor to the book release the companion anchors to (incl. the deferred comment items RB1-RB4 and two claims summaries) -> review -> Le accepts -> publish v0.11.0 (tag, Zenodo DOI, site) -> book 1.2.0: re-pin Appendices F and G with a zero-shift check |

## Wave records (history; the newest entries are the bullets near the top of this list and the wave log below)
- **L21 gate evidence complete; ready for Le's closure (2026-11-23).** Gate commit `38a3e00` on `wave-l21/int` (merge of `wave-l21/tube` `fcb3f58` onto L20, the deferred Lean-comment list C1-C19 + g1.1, g3.2 comment-only, C11 not applied (TeX 5534 correct), claims 6632, comparator 2056 + 3270 = 5326, CheckFidelity 0 problems, lean-fence CLEAN with approvals `TubeAttained`, `TubeTail` FOR LE, lean-regress CLEAN). Receipts `39c4365` (lower tier 0 sorry, standard axioms, 6632 claims, peak 13.4 GiB; comparator 2/2 PASS); scratch-registry `gate --check` exit 0 at `38a3e00` and `39c4365`; lab registry unchanged. Easley `ade3f31`: 2/2 fresh, 212/212 default, COMPLETE. Reviews: DeepSeek V4 Pro on `SourceTubeAttained` PASS_WITH_NOTES high (docstring fixes `fcb3f58`); GPT-6.2-Sol docs l21-a PASS_WITH_NOTES high, l21-b FAIL on comment wording (two findings rated MINOR by #24), docs-only repairs `adeac06`, RB1-RB4 and two claims summaries deferred to v0.11.0 release prep. COMPLETION 59 / 22 / 1 / 30 / 2 / 106; coverage 118 rows 85 / 31 / 2.
- **L20 gate CLOSED by Le (2026-11-23).** Le, verbatim: "I close the L20 gate. I confirm the 24 L20 fence input names plus MildOccupied.RepOn and LinOn, and your review decisions under my delegation. Merge wave-l20/int to dev main, tag L20-gate on 5cdd493, update COMPLETION.md (fix the stale 'receipts pending' wording), record it in lean-progress/PROGRESS.md on top of origin master, sync <HUB>, and report." Done: `wave-l20/int` (`4842df8`) fast-forwarded into dev main; COMPLETION milestone `e04987d` (L20-gate row; the L20 row's pending wording replaced by the receipts, reviews and Easley evidence); annotated tag `L20-gate` on `5cdd493`; pushed; <HUB> at `e04987d`; scratch-registry `gate --check` exit 0 at `e04987d` (docs-only descendant; claims 6620 ✓). Counts at the L20 gate: 59 / 21 / 1 / 30 / 2 / 107 of 220; coverage 117 rows 84 / 31 / 2.
- **L20 gate evidence complete; ready for Le's closure (2026-11-23).** Gate commit `5cdd493`. Receipts `4842df8` (lower tier 0 sorry, standard axioms, 6620 claims, peak 14.8 GiB; comparator 2049 + 3265 = 5314 PASS, both configurations); scratch-registry `gate --check` exit 0 at `5cdd493` and at the tip (docs-only descendant); lab registry unchanged. Easley `1b94926`: `leanchecker --fresh` 12/12, default 211/211, COMPLETE. DeepSeek V4 Pro gate scopes g1-g8: 4 PASS, 4 PASS_WITH_NOTES, high, no MAJOR/CRITICAL. GPT-6.2-Sol docs: 3 packets FAIL (documentation only; 8 MAJOR, mostly lost retained-credit disclosures), repaired docs-only D1-D9 `d3b2f8e`, confirmation round, E1-E4 `9706469`/`4fe5c33`, narrow E1 confirmation (high), E5 `fdbb0ae` without a further model call (#24 rated F1 MINOR); Lean-comment items C1-C19 + DeepSeek g1.1, g3.2 deferred to the L21 gate commit (receipts kept). For Le: fence approvals (24 interface names + route definitions `MildOccupied.RepOn`, `LinOn`), the review decisions taken by #24 under the delegation (MildConstruction re-categorized proof steps; docs-b F8 MAJOR; deferral of C-list), and the closure. L21 gate step 1 done (`38a3e00`, 59/22/1/30/2/106); its Easley, receipts and docs review running.
- **L20 integrated and gate step 1 done (2026-11-23).** All items proved with no fallback named input: L20-0 `MildInterface` (fidelity review DeepSeek V4 Pro PASS_WITH_NOTES high, two NOTEs, no change), A `MildOccupied`, B `MildPolyMem`, C `MildFields`, D `MildTerminalFubini` + `MildPartialVertex` (the main risk; `TerminalFubini` unused, every d), E `MildGreenWidth`, F `MildConstruction`, `MildFinal` (hypothesis-free `_l20` wrappers, `mild_construction_m9_l20` non-vacuity), R `RieszInstanceOne` (d = 1 Riesz instance of `H:homog`; `hH` off the three Riesz rows), W `CleanupWrappers`, DOC (comment-only, 55 earlier files; strip check 0 non-comment differences). Integration `wave-l20/int` `1b3cb25`; gate commit `5cdd493` (claims 6620: 5314 theorems; comparator 2049 credited + 3265 helpers, CheckFidelity 5314/5314, 0 problems; lean-fence `--check-inputs` CLEAN with the 24 interface names plus two route definitions `MildOccupied.RepOn`, `LinOn` as approvals FOR LE; lean-regress CLEAN, no earlier statement changed); docs tip `8ce53c8`. COMPLETION **59 / 21 / 1 / 30 / 2 / 107** of 220 (as projected); coverage 117 rows 84 / 31 / 2. About 5,100 new Lean lines. Running in parallel: receipts, DeepSeek gate scopes, GPT-6.2-Sol docs scopes (incl. the DOC diff), Easley replay. L21 (`TubeAttained`) item `fcb3f58` reviewed PASS_WITH_NOTES (docstring fixes applied); gate after L20.
- **L19 merged (2026-11-23).** On Le's closure of 2026-11-22: receipts at `fe9f1de` committed as `5e2b86f` (lower tier: 0 sorry, standard axioms, 6314 claims, memory peak 15.3 GiB; comparator: 2 configurations, 1978 + 3099, all 5077 slots PASS); scratch-registry `gate --check` exit 0 at `fe9f1de`, `5e2b86f` and `d813957` (docs-only descendant; claims-declaration ✓ 6314); `comparator check --refuse-dirty --refuse-private` exit 0; lab registry never written. `wave-l19/int` fast-forwarded into dev main; COMPLETION milestone `d813957`; annotated tag `L19-gate` on `fe9f1de`; pushed; <HUB> at `d813957`. Counts at the L19 gate: 54 / 22 / 1 / 34 / 2 / 107 of 220; coverage 117 rows 80 / 35 / 2.
- **Lean end point: option A (Le, 2026-11-23, typed in #23's session, relayed by #23).** Close the companion after L20 plus `TubeAttained` as an item in L21; no further proof waves. Supplied inputs kept: `SignedMultiplierForm`, `ThreeTransfer`, `TubeTail`, `CutoffCompact`. `MixedMoment` and `FirstMomentSeries` close in L20 item W. No operator-layer work. Basis: #24's per-input estimate (amsg `dcace121611e`) and two read-only Office probes (amsg `7c124b40c707`; never committed): `TubeAttained` FEASIBLE, 250-400 lines (closed + compact sum in Mathlib; remaining piece: compact image of the Cameron-Martin ball); `CutoffCompact` FEASIBLE WITH GAPS, 600-1,200 lines (truncation and norm limit proved; Hilbert-Schmidt step open). Release: one companion release v0.11.0 (L15-L21), superseding L20 decision 13; then book 1.2.0 (MINOR) re-pinning Appendices F and G. Order: L21 gates before v0.11.0's re-anchor.

- **Wave:** L0 (setup) — `CLOSED` 2026-11-09 (Le approved decision point 4
  in session; the open-release design D4 binds the companion).
- **Companion package:** `stratonovich-ham-second-moment-lean`, checkout
  `../../Project-stratonovich-ham-second-moment-lean`, remote
  github.com/chenle02/stratonovich-ham-second-moment-lean (PRIVATE until
  Le's public flip; fresh root commit 29e7367, no incubation history).
  Registered in lean-pkg; status `verified-private` at 38d1616 (lower-tier
  systemd receipt: clean build, 0 sorry, standard three axioms, all 88
  claims' axioms read from the built environment). Claims synced at 358529c.
- **Companion content:** 23 Mathlib-only seams, sources byte-identical to
  local-checks (HermiteWordConsumer import path only): 82 public theorems,
  43 public definitions; claims.yaml has 88 rows (78 theorems + 6 defs
  reusable, 4 PositiveGram helpers internal); 68 negative controls all
  rejected; 26 audits compile. The 3 GaussianChaos-dependent seams
  (normalized-coordinate, vector-gaussian-projection, colored-vector-word;
  9 facts) are WITHHELD by Le's 2026-11-09 decision until gaussian-chaos-lean
  is licensed and public; they stay here in local-checks.
- **Manuscript anchor:** revision ba01d98 (2026-11-10; presentation-only
  successor of 669ccc9 with the expanded literature review and diagrams;
  50 TeX inputs, 293-page PDF; companion 48ce162 re-anchored, all 56 cited
  labels and their math unchanged). Previous: revision 669ccc9 (presentation-only successor of
  cf979d6), pinned in the companion's provenance/manuscript-anchor.json at
  companion 4bdffba: 41 TeX inputs (28 core + 12 figures + styles) and the
  275-page PDF; cf979d6 kept under history. Script check: all 46 cited
  labels exist and the math of the 40 cited statements/proofs is unchanged
  up to whitespace and braces, so no Lean correspondence changed.
  The statement ledger maps 33 claims to a label and 55 have no direct
  label at cf979d6 (35/53 before the DeepSeek V4 Pro correspondence review
  of 38d1616, adjudicated in reviews/2026-11-09-lean-ledger-correspondence/:
  0 critical, 1 major, 6 minor, all accepted or confirmatory, MEDIUM
  confidence; ledger corrected at companion a78c5d0, docs-only)
  (whole seams AllAlphaMoment, DampedLower, DimensionalMatrix, GlobalOmega,
  LocalFlow, MiddleCross, OccupationForm, PhaseResponse, ProjectionResidual,
  TerminalCross, plus 8 rows in DirectEvent/InteractionDriver/RawValueCeiling).
  Flagged to #3 as a possible target mismatch; not a Lean defect.
- **Not claimed:** no Comparator tier, no whole-paper gate, no correspondence
  re-review of the packaged statements (the ledger is an AI-drafted review
  draft), no Palomar eligibility (seam companion, ADR-0070 D4).
- **Kimi-K3 ledger review (2026-11-10):** read-only, tool-assisted over
  669ccc9, companion 4bdffba: content PASS_WITH_NOTES/high, 88/88 rows,
  0 fatal/0 major/4 minor (all accepted, wording; companion 01e2480), 55
  absences confirmed by search. Receipt INVALID-REPORT (supervisor's
  contract used non-schema check verdicts; recover-report refused), so the
  correspondence gate is NOT closed by receipt. Record:
  reviews/2026-11-10-lean-ledger-kimi-k3/ADJUDICATION.md.
- **Kimi-K3 v2 (2026-11-10, schema-conforming, contract-checked):** at
  01e2480 over 669ccc9: body PASS_WITH_NOTES/high, 88/88, 0/0/2 minor (both
  accepted, companion 5e0d122) plus a DimensionalMatrix note. Receipt again
  INVALID-REPORT: Kimi prefixed one prose sentence despite the JSON-only
  instruction; recover-report cannot strip a prose prefix. Gate NOT closed
  by receipt. Record: reviews/2026-11-10-lean-ledger-kimi-k3-v2/.
- **Codex GPT-6.1-Sol review (2026-11-10):** at companion 5e0d122 over
  669ccc9, VALID report, FAIL/high: 1 fatal (DimensionalMatrix is the phase
  kernel of P:actual-wave-form, missed by all earlier reviews and the target
  triage), 2 major (HermiteWord zero-count hypothesis; tilt_exponent has no
  displayed step). All accepted; repaired at companion c9e28af (36 labelled,
  52 unlabelled; coverage 20+4). Record:
  reviews/2026-11-10-lean-ledger-codex-gpt61sol/.
- **Successor Codex review (2026-11-10):** at c9e28af, valid, FAIL/medium:
  2 fatal, both accepted and repaired at companion 1a8c419: full_interaction
  is the UNWEIGHTED product (b_r = <r>sin(rt)/r in the manuscript; the
  previous repair dropped <r>), and box_margin/box_scale are the d=2, p=Q
  case of the margin step of P:radius-mean-anchor (overrides the 11-09
  triage). Now 38 labelled / 50 unlabelled; coverage 21+4. Record:
  reviews/2026-11-10-lean-ledger-codex-gpt61sol-v2/.
- **Complete-reading Codex review (2026-11-10):** at 1a8c419, valid,
  FAIL/medium: 17 of 18 required files read completely, main TeX partial
  (about 1,700 of 7,706 lines) so 54 rows INCONCLUSIVE as contracted; 33
  labelled rows PASS; no fidelity defect. 1 fatal accepted:
  two_frequency_average is the cosine case of the L:masked-trig-products
  expansion (companion 0eb9403; 39 labelled / 49 unlabelled; coverage 22+4).
  Record: reviews/2026-11-10-lean-ledger-codex-gpt61sol-v3-complete-reading/.
- **Split Codex review (2026-11-10):** compose cannot take Codex receipts,
  so Le chose two Codex components + a documented join. M (main TeX read
  gapless 1-7706) and S (17 modules complete), both high confidence, same
  candidate 0eb9403, disjoint rows covering all 88: 86 PASS, 2 fatal, both
  accepted (kappa_gt_one -> E:kappa; noise_order -> L:temporal-equilibrium),
  repaired at companion 435fdb0 (40 labelled / 48 unlabelled; coverage
  24+4). Gate NOT closed: no accepted receipt. Record:
  reviews/2026-11-10-lean-ledger-codex-split/ (JOIN.md, ADJUDICATION.md).
- **Narrow confirmation (2026-11-10):** Codex GPT-6.1-Sol at companion
  48ce162 over manuscript ba01d98, six checks (two repaired rows, DirectEvent
  and LocalFlow paragraphs, index, totals): PASS/high, 0 findings,
  ACCEPTED receipt. Script: the other 86 rows are byte-identical to 0eb9403,
  where they passed under complete reading. All 88 rows now covered; closing
  record reviews/2026-11-10-lean-ledger-codex-confirm/ADJUDICATION.md.
  Documented conjunction, not a compose certificate.
- **LEDGER CORRESPONDENCE GATE: CLOSED (Le, 2026-11-10)** at companion
  48ce162 over manuscript ba01d98. Le accepted the documented conjunction
  (split complete-reading review of the 86 unchanged rows + the accepted
  narrow confirmation receipt of the repairs) as closing the gate. Scope:
  AI statement-to-manuscript correspondence of docs/statement-ledger.md
  (40 labelled / 48 unlabelled). Not human verification; analytic inputs
  outside Lean are not verified; any later ledger or cited-label change
  needs a successor review.
- **Wave L1 (2026-11-10, OPENED and built):** five deterministic labelled
  results formalized WHOLE with the paper's hypotheses (W1 packages B1,
  B2, B7, B10, B25): L:gaussian-scalar-powers (weighted AM-GM, integer
  powers, finite Hoelder, E Z^r <= (E Z)^r), L:gram-scalar-algebra,
  E:kappa (1 < kappa < 2), E:driver-parameters (intervals nonempty),
  L:tube-rayleigh-tail (tail integral bound, integrability). 17 theorems,
  2 definitions, 17 refutations (Lean proofs that wrong variants are
  false). Companion commits 25a587d..e36f946; lean-pkg receipt and gate
  verified-private at e36f946 (107 claims' axioms read; 0 sorry); claims
  synced at 9d1c7c4. Coverage: 5 same-assumptions, 19 inputs-supplied, 4
  outside. No manuscript defect found. The 19 new ledger rows await an
  independent correspondence review (Codex, launched 2026-11-10).
- **Wave L1 correspondence (2026-11-10):** three Codex GPT-6.1-Sol reviews:
  (1) 5 findings on overstated same-assumptions claims, repaired with
  exact-hypothesis wrappers (Gram, Rayleigh) and, at Le's choice, a full
  Lean model of H:homog (HomogHypothesis.HomogCovariance) with wrappers
  for E:kappa and E:driver-parameters; (2) confirmation 29/30; (3) H:homog
  model review PASS_WITH_NOTES/high, ACCEPTED, 2 minor wording fixes
  (companion eef3e72). All five coverage same-assumptions rows now cite
  statements with the manuscript's hypotheses. lean-pkg verified-private at
  b876362 (117 claims). Closing record:
  reviews/2026-11-10-lean-homog-model-review/ADJUDICATION.md.
- **WAVE L1 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-10)** at companion
  b876362 over manuscript ba01d98: Le accepted the three-review sequence.
  Scope: AI statement-to-manuscript correspondence of the 29 whole-result
  ledger rows (incl. the H:homog model); not human verification; the
  Rayleigh lemma's "In particular" application stays outside Lean; any
  later change to these rows or cited labels needs a successor review.
- **Wave L2 (2026-11-10, built and reviewed):** three further whole
  results (board C26, B23, B24; B3, B4, B9 stay reserved as community entry
  points per Le via #16): S:temporal-equilibrium (L:equilibrium-gamma-beta
  and L:temporal-equilibrium with the manuscript's hypotheses, nothing
  supplied; the potential identity proved on all of [0,1] by a Moebius
  substitution instead of the TeX series), P:radius-mean-anchor (every
  conclusion; the moment bound of C:radius-covariance-residuals supplied,
  measurability hXmeas explicit) and L:masked-trig-products (every
  conclusion, all four cos/sin cases; completion membership and the
  modulation bound supplied). 84 theorems, 24 public definitions, 13
  refutations; 223 claims; coverage 7 same-assumptions, 18 inputs-supplied,
  4 outside. No manuscript defect found (minor observations: r, rho >= 0 and
  a > 0 for the potential identity are not needed; measurability of the
  C^theta norm is implicit). Companion c4fa5be..a2e9625; lean-pkg receipt at
  79afdde (fresh build, 0 sorry, 223 claim axioms), verified-private
  re-gated b876362 -> 9033c4e -> 79afdde; claims synced at a2e9625.
- **Wave L2 correspondence (2026-11-10):** three Codex GPT-6.1-Sol reviews
  at c4e0620 (TemporalEquilibrium FAIL: two route-auxiliary helpers
  mislabelled as TeX proof steps; RadiusMeanAnchor and MaskedTrigProducts
  PASS_WITH_NOTES), all 6 findings accepted and repaired at 17f0490; narrow
  confirmation at 17f0490 PASS_WITH_NOTES/high, accepted, 1 minor (fixed
  79afdde). Records: reviews/2026-11-10-lean-wave-l2-*/ADJUDICATION.md.
- **WAVE L2 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-10)** at companion
  79afdde over manuscript ba01d98: Le accepted the three-review sequence
  plus the confirmation review. Scope: AI statement-to-manuscript
  correspondence of the 106 wave-L2 ledger rows and their coverage rows;
  not human verification; the supplied inputs of P:radius-mean-anchor and
  L:masked-trig-products stay outside Lean; any later change to these rows
  or cited labels needs a successor review.
- **Post-L2 hardening (2026-11-10, companion 3c2cade..130bba4):**
  (1) all 30 refutations rewritten to import their package module and
  refute the package's own declarations (no local copies), each a named
  theorem whose type is a negation, with `_contrast` theorems applying the
  package theorem at the counterexample (76 theorems, standard axioms
  only); 9 controls that stated bare numerals now state the wrong variant
  in the package theorem's shape (all 68 controls already imported their
  seam; WrongZeroShift header aligned with FALSE-CONTROL-MAP.md);
  (2) Audit printouts and consumer examples for the 9 whole-result modules
  (audits 26 -> 35); (3) re-anchored to manuscript revision 3920258
  (presentation-only: only the uncited literature figure changed; all 78
  cited labels and their statements and proofs unchanged; gates stay
  recorded against ba01d98); (4) check-controls.sh catches Lean 4.35
  setup errors case-insensitively (self-test refuses a broken control).
  check-controls: 68 controls, 30 refutations, 35 audits PASS; lean-pkg
  verified-private re-gated 79afdde -> 64070a7 -> e2903a6 (fresh receipts,
  0 sorry, 223 claim axioms); claims synced at f3e8275. Field reviews of
  lean-pkg proposal 0014 (declared controls) sent to lean-ops: final
  verdict ACCEPT with two fixes; acceptance is Le's.
- **WAVE L4 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-11)** at companion
  ac6f767 over manuscript 3920258: Le accepted the four Codex GPT-6.1-Sol
  reviews (at efec88b: FrequencyRow PASS_WITH_NOTES, three FAIL; 0 fatal,
  4 major, 4 minor, all documentation, all accepted, repaired at 7afcd23)
  plus the confirmation review (PASS_WITH_NOTES/high; C1 fixed at ac6f767).
  Results: P:masked-spectral-growth; P:clock-copy-obstruction now
  same-assumptions (spectral homogeneity derived from H:homog) and the
  finiteness part of L:damped-homogeneous-norms same-assumptions (weaker);
  E:masked-time-schur and L:masked-temporal-modulation (same-assumptions,
  on the defining double integral); L:masked-trig-products input narrowed
  to the completion (hmem, hnorm); P:frequency-row and C:frequency-time;
  L:occupation-kernel-row and L:spatial-physical-pair. 724 claims; ledger
  419 labelled / 305 unlabelled; coverage 20 same-assumptions, 16
  inputs-supplied, 4 outside; both lean-pkg tiers at 2f5ee14, claims
  ledger READY (0 open). Scope: AI statement-to-manuscript correspondence,
  not human verification; supplied inputs stay outside Lean; later changes
  to these rows or cited labels need a successor review. Records:
  reviews/2026-11-11-lean-wave-l4-*.
- **OVERNIGHT TODO LIST (Le, 2026-11-10 evening: "include all todos and
  systematically complete all of them autonomously overnight").** Read as
  approval to RUN wave L4 as proposed below; every gate (L4 correspondence)
  stays Le's to close. Order and status (updated as items complete):
  1. [x] DONE (2026-11-10 23:58): comparator tier merged (companion
     4073c64: comparator.json with 470 theorem_names, Challenge/Solution,
     ChallengeDefs, scripts/comparator/; CheckFidelity: 470/470 Challenge
     types and 717 copied constants Expr-equal, 0 problems). Comparator
     receipt (toolchain, pass, all 470 judged, about 7 min) and lower-tier
     receipt (fresh build, 0 sorry, 557 claim axioms, peak 7.0 GiB) both at
     4073c64, committed at 646e164; gated verified-private
     e2903a6 -> 4073c64 WITH comparator evidence; claims synced at 646e164;
     `lean-pkg claims ledger`: READY, 430 required, 550 verified, 0 open,
     7 out-of-scope. No claim rejected.
     (Original item:) Comparator tier at one commit with the lower tier: refresh branch
     comparator-tier onto main, merge into main, `lean-pkg receipt
     comparator` and `receipt systemd --memory-max 12G` at the same commit,
     `gate --receipt R --comparator C --regate`, `claims sync`, `claims
     ledger` (target: 0 open theorem claims); record; report any rejected
     claim as a statement-fidelity finding.
  2. [x] DONE (2026-11-11): wave-L3 replay at companion 687e631 (job
     5688396, 4:35 h): 12/12 targets pass `lake env leanchecker --fresh`
     (exit 0, empty output), default mode 45/45; evidence companion
     31eb390, verification/leanchecker-easley-wave-l3/.
     (Original item:) Easley `leanchecker --fresh` replay of the wave-L3 modules (job
     5688396 running): review, redact, commit evidence, record here.
  3. [x] DONE; gate closed by Le (2026-11-11): all four items formalized at
     FULL scope, no fallback used, nothing supplied except B24's narrowed
     input: L4-a P:masked-spectral-growth and the DISCHARGE of B14's input
     (spectralHomogeneous_of_homog; ClockCopyHomog re-issues
     clock_copy_obstruction_paper and damped_norms_finite_paper with only
     the manuscript's hypotheses: B14 is now same-assumptions); L4-b
     E:masked-time-schur and L:masked-temporal-modulation (constant
     16/(1-a), different route) and masked_trig_products_bridged_paper
     (B24 input narrowed from hmod to the norm identity hnorm); L4-c
     P:frequency-row and C:frequency-time (all three alpha cases); L4-d
     L:occupation-kernel-row and L:spatial-physical-pair. Code 515101a
     (210 public declarations, standard axioms; check-controls 68/65/50
     PASS); docs a635815..739c327, efec88b (724 claims; ledger 419/305;
     coverage 40 rows: 20 same-assumptions, 16 inputs-supplied, 4
     outside). Codex reviews at efec88b: FrequencyRow PASS_WITH_NOTES,
     three FAIL; 0 fatal, 4 major, 4 minor, all documentation, all
     accepted, repaired at 7afcd23; evidence Article d3e3620
     (reviews/2026-11-11-lean-wave-l4-*). Confirmation review at 7afcd23:
     PASS_WITH_NOTES/high, accepted; C1 (duplicate index row) fixed at
     ac6f767. **WAVE L4 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-11)**
     at companion ac6f767 over manuscript 3920258 (four reviews plus the
     confirmation review accepted).
     (Original item:) Wave L4 (four items L4-a..d below) in parallel worktrees:
     formalize, verify independently, integrate (claims, ledger, coverage,
     README/FORMALIZATION), check-controls; one Codex review per item,
     adjudicate every finding, repair, confirmation review; then STOP for
     Le's gate.
  4. [x] DONE (2026-11-11): comparator extended to all 611 theorem claims
     (comparator-l4 7c02a65 merged at companion 2f5ee14; CheckFidelity
     611/611 and 762 copied constants Expr-equal, 0 problems; copied
     definitions under their own prefix); comparator receipt (pass, all
     611 judged) and lower-tier receipt (0 sorry, 724 claim axioms, peak
     7.1 GiB) both at 2f5ee14, committed at 5ed4cf4; re-gated
     verified-private 4073c64 -> 2f5ee14 with comparator evidence; claims
     synced; `claims ledger`: READY, 513 required, 709 verified, 0 open,
     15 out-of-scope. No claim rejected.
     (Original item:) After L4: lean-pkg receipts of both tiers at one commit again
     (comparator regenerated for the new claims), regate, claims ledger.
  5. [x] DONE (2026-11-11): wave-L4 replay at companion 2f5ee14 (jobs
     5688553 and 5688619): 17/17 targets pass, including 8 modules whose
     sources or imports changed since their earlier replay. With the
     837778a (35/35) and L3 replays, every one of the 51 library modules
     and the umbrella has a passing --fresh replay at a commit where it and
     all its imports are identical to 2f5ee14 (64 runs, all pass). Not
     replayed: the comparator libraries ChallengeDefs, Challenge, Solution
     (not imported by the umbrella). Evidence companion 31eb390,
     verification/leanchecker-easley-wave-l4/; README 56d5002.
     (Original item:) Easley `leanchecker --fresh` replay of the wave-L4 modules.
  6. [x] DONE (2026-11-11): board docs/community 25e63c5 (B14 now nothing
     supplied, B24 input narrowed, C19 and C21 partial, D4 slice) and
     81bfb25/6ed4ae4 (wave-L3 rows and paragraph record the closed L3
     gate); companion README 4a66a69 (L4 reviewed, acceptance pending);
     #3 informed, #16 queued; lean-ops: comparator frictions 8-10 and 11-13
     sent and triaged (folded into the copied-definitions/fidelity
     proposal; pp.explicit retry proposed to Le).
     (Original item:) Community board (docs/community) updated for L4; #16 and #3
     informed; lean-pkg friction to lean-ops (incl. 3 new comparator points:
     open-scoped namespaces in the round-trip check, definitional-only
     round trips without a hint, bridges for copied structures).
  7. [x] DONE (2026-11-11): retro, Le-AI-Lab 28dee02d: new skill
     lean-pkg-comparator-tier-paper-companion; updated
     lean-companion-junk-values-cold-audit-agent-waves (correspondence
     finding classes; agent-wave practice), lean-pkg-receipt-binding-pitfalls
     (end every gate with `claims ledger`), worker-output-multiple-replies
     (reusing a command from the transcript: first match). An earlier retro
     the same day: 909f748a.
  NOT for the night (Le's decisions): release of gaussian-chaos-lean (opens
  D1, A2, B21); investing in a D8 Sobolev/self-adjoint foundation; #3's
  recommended zero-covariance remark after H:homog and the nonzero
  qualification of T:first's strict comparison; closing the L4 gate.
- **WAVE L3 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-10)** at companion
  dfc2fe8 over manuscript 3920258: Le accepted the four Codex GPT-6.1-Sol
  reviews (at 4721cf9: all FAIL with 2 fatal, 12 major and 11 minor
  findings, all documentation: overclaims, route auxiliaries labelled as
  TeX steps, incomplete hypotheses or inventories; every finding verified
  and accepted, repairs merged at 25c5995) plus the confirmation review
  (PASS_WITH_NOTES/high, accepted; C1 fixed at dfc2fe8). Results:
  L:variational-control-dilation (same-assumptions, conclusion weaker),
  L:raw-block-indexed-cone (inputs-supplied, full), P:clock-copy-obstruction
  (inputs-supplied, full, one input) with the finiteness part of
  L:damped-homogeneous-norms, and the finite slice of S:compact-gaussian
  (L:gaussian-trace-bounds, P:finite-gaussian-matrix,
  R:gaussian-one-variance-test, same-assumptions); 557 claims, ledger 347
  labelled / 210 unlabelled. Scope: AI statement-to-manuscript
  correspondence, not human verification; supplied inputs stay outside
  Lean; later changes to these rows or cited labels need a successor
  review. Records: reviews/2026-11-10-lean-wave-l3-*. Still open for the
  wave's evidence: lean-pkg receipts of both tiers at one commit (the
  comparator tier now covers all 470 theorem claims) and the Easley
  leanchecker --fresh replay of the wave-L3 modules (running).
- **WAVE L3: APPROVED by Le (2026-11-10) as proposed; OPENED** (four items launched in parallel worktrees). Chosen from
  the board excluding the reserved B3, B4, B9, after three read-only
  feasibility reconnaissances against the TeX at 3920258 with Mathlib names
  probed by compiling scratch files (reports:
  session scratch l3-feas-{b6-b16,d4-b14-c21,c22}.md; summarized here).
  Four independent work items, one agent and one module each, run in
  parallel in separate worktrees; integration, claims/ledger/coverage and
  gates by the integrator as in wave L2.

  | Item | Target (label, TeX) | Foundations built in this wave | Class (fallback) | Size |
  |---|---|---|---|---|
  | L3-a | B6 `L:variational-control-dilation` (integrated_unmasked_variational.tex 225-273): dilation bijection of the control class, scaling of mean, variance, rate and its integral | hand-rolled weak gradient / `H^1(R^d)` (about 40 lines; Mathlib has no Sobolev spaces), Gamma pushforward under dilation from `HomogCovariance.scaling` (already compiles in a probe) | dilation, mean, variance same-assumptions; rate and its integral defined by the manuscript's proven Rayleigh form `E:variational-real-rayleigh`, with the identifications rate = sqrt(-E_s) (`P:variational-unmasked-rate`, needs D8) and variance = E W(Psi)^2 (`L:compact-raw-profile`, needs D1) recorded as unformalized (fallback: H^1 as a named hypothesis; rate items inputs-supplied) | 12-15 theorems, 400-550 lines |
  | L3-b | B16 `L:raw-block-indexed-cone` (integrated_raw_block_lower.tex 227-330): product lower bound along chains of nearby parameters, c_* = a_* j_*/4 | none (Banach-space algebra; compactness and operator-norm lemmas exist) | inputs-supplied: the C16 ground-family outputs (flows, eigen-relation E:compact-F-eigen, normalized complement, continuity, margins E:compact-positive-margins) as one `GroundFamily` hypothesis structure (fallback: product bound for given B, omega, eps; their existence as a separate lemma) | about 10 theorems, 450-650 lines |
  | L3-c | B14 `P:clock-copy-obstruction` (main TeX 7553-7704, under H:homog with Gamma != 0 and a = alpha0) and the finiteness part of `L:damped-homogeneous-norms` (676-760) | first slice of D4: WaveKernel (s sinc(s|xi|), bounds, scaling, Laplace transform), TimeFractional (Gamma-integral representation of |r|^(-a), the two-time Laplace lemma, Psi_a bounds), SpectralHomog (mu{0}=0, mu(B_r)=V r^alpha, radial integration), DampedNorms (absolute integrability of N_2, which justifies Fubini directly) | inputs-supplied with ONE named input: homogeneity of the spectral measure mu(cA) = c^alpha mu(A) (stretch: derive it from Gamma's scaling via Riesz-Markov uniqueness, making B14 same-assumptions; fallback: K-side Fubini interchange supplied as a named input) | about 35 theorems, 1200-1500 lines |
  | L3-d | C22 finite slice: `L:gaussian-trace-bounds` (integrated_compact_gaussian.tex 47-90), `P:finite-gaussian-matrix` (92-171, even p = 2m, S_p as Tr((A*A)^m)), `R:gaussian-one-variance-test` (173-187) | reusable finite Gaussian integration by parts on polynomial-growth functions (1-d from Mathlib's integration by parts and the density derivative, N-d by Fubini on Measure.pi); Mathlib has no Gaussian IBP and the registry has nothing reusable (lean-pkg search) | same-assumptions (fallback: the IBP identity for F supplied as a named input; then P:finite-gaussian-matrix inputs-supplied) | 20-30 theorems, 1000-1600 lines |

  Gates per item, as in wave L2: compile and `#print axioms` (standard
  three only), no sorry; exact-hypothesis `_paper` wrapper; refutations
  that import the package and name negation theorems; Audit printout;
  claims, ledger section, index, coverage rows; check-controls; fresh
  lean-pkg receipt and re-gate; one Codex GPT-6.1-Sol correspondence
  review per module plus a confirmation review of the repairs; Le closes
  the gate. Stopping condition: all four items integrated and reviewed, or
  an item at its fallback scope with the remainder recorded as a named
  input; at most two repair rounds per item. Reusable foundations to
  consider for extraction after review: finite Gaussian IBP (L3-d), the
  time-fractional Laplace representation (L3-c), the weak-gradient H^1
  (L3-a).
  Not in L3: the deterministic C21 pieces (`P:masked-spectral-growth`,
  E:masked-time-schur, `L:masked-temporal-modulation`, which would
  discharge B24's supplied input; `P:frequency-row`), proposed for wave L4
  on top of the L3-c D4 slice; the seven infinite-dimensional C22 results
  (need Schatten classes, singular values of compact operators,
  Courant-Fischer, torus Sobolev spaces); everything needing D1, D5 or a
  full D8. Zero covariance: statements needing Gamma != 0 carry it
  explicitly, as the TeX does (see #3's answer below).
- **WAVE L4: PROPOSED (2026-11-10); run overnight under Le's "complete all todos" instruction (gate stays Le's).** Builds on
  the wave-L3 D4 slice. From a read-only feasibility study against the TeX
  at 3920258, every Mathlib name probed by compiling scratch files (session
  scratch l4-feas.md; Probe1-5.lean). Mathlib gaps: no Gaussian
  `SchwartzMap` (built by hand) and no C^1 extension from a closed
  interval. Four items, one agent and worktree each, as in wave L3:

  | Item | Target (label, TeX) | Builds on / new foundation | Class (fallback) | Size |
  |---|---|---|---|---|
  | L4-a | `P:masked-spectral-growth` (integrated_covariance_foundation.tex 34-77), and DISCHARGE of the one supplied input of B14: derive the spectral homogeneity mu(cA) = c^alpha mu(A) from Gamma's scaling (translated Gaussian test gives the characteristic function of e^(-|xi|^2/r^2) mu; with `Measure.ext_of_charFun`), then reissue `clock_copy_obstruction_paper` and `damped_norms_finite_paper` with no supplied input | Gaussian Schwartz test function (about 250 lines); `HomogCovariance.scaling` is `SpectralHomogeneous Gamma (d-alpha)`, so `SpectralHomog.integral_comp_smul` applies; `IsTempered` gives integrability | same-assumptions; B14 becomes same-assumptions (fallback: Schwartz membership of the Gaussian as a named input) | about 700 lines |
  | L4-b | `E:masked-time-schur` (150-152, inside `L:masked-time-completion`) and `L:masked-temporal-modulation` (300-345) | MaskedTrigProducts (`bracket`, `modeFn`, `C0`); a bridged `masked_trig_products_paper` taking the norm identity `hnorm` instead of `hmod` | time-Schur same-assumptions (double-integral form; the completion H_a is not built); modulation inputs-supplied: its right side matches `hmod` exactly, but its left side is the double integral, so B24's input narrows to `hnorm` (the complexification clause of `L:masked-time-completion`) rather than disappearing; constants are tight (8 sqrt 2 <= 16) (fallback: supply the oscillatory integration-by-parts bound) | about 800 lines |
  | L4-c | `P:frequency-row` (integrated_wave_variance.tex 23-139) and `C:frequency-time` (141-165): dyadic-shell measure estimate, three alpha cases, constant independent of d (quantifier order `exists K, forall d nu`) | MaskedTrigProducts (`bracket`, `frequencyPair`); with L4-a the instance for mu is a corollary | same-assumptions (fallback: the alpha != 1 cases first) | 700-900 lines |
  | L4-d | C19 slice: `L:occupation-kernel-row` (integrated_spatial_occupation.tex 283-308); optional `L:spatial-physical-pair` | its kernel is exactly `TimeFractional.Psi a abs(u) (abs(u)/D)`; positivity and K <= abs(u)^(-a) already proved | same-assumptions | about 300 lines |

  Gates as in wave L3 (exact-hypothesis wrappers, refutations importing
  the package, Audit, claims/ledger/coverage, check-controls, lean-pkg
  receipts of both tiers at one commit (the comparator tier now covers
  every theorem claim), one Codex review per item plus a confirmation
  review, Easley `leanchecker --fresh` of the new modules, Le's gate).
  Stopping condition: all four items integrated and reviewed, or an item at
  its fallback scope with the remainder recorded as a named input; at most
  two repair rounds per item.
  Stretch (not proposed for L4): the time form is positive semidefinite
  (subordination), then build H_a^C concretely as a completion so that
  `hmem` and `hnorm` hold by construction and B24 becomes same-assumptions;
  `L:masked-continuous-wave` after that.
  Not reachable yet: B22 `P:actual-wave-form` (needs D1 noise completion,
  D8 H^(1/2) x H^(-1/2) duality, H_a-valued Bochner integrals; only its
  continuous-sine-quotient item exists, `WaveKernel.waveHat_zero`); B5,
  C3, C20, E3 (need D5, D8 or D1). B3, B4, B9 stay reserved.
- **WAVE L5: APPROVED by Le (2026-11-11) as proposed, with the default
  answers to the three decisions; OPENED** (six items launched in parallel
  worktrees, branches wave-l5/a..f off companion main 3a7d57f).
  **WAVE L5 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-11)** at companion
  712c307 over manuscript 975feb3: Le accepted the six Codex reviews plus the
  confirmation review. Recorded in the companion README (a7f90b0) and the
  board (docs/community 6064dec); #16, #3 and #24 told. Le's decision was also
  relayed verbatim by #16 ("Approve the Lean wave L5 gate. Tell #22 to record
  it."). Scope: AI statement-to-manuscript correspondence of the 248 wave-L5
  ledger rows and the changed sections and coverage rows; NOT human
  verification; the supplied input (GreenMass for N_0) and every analytic
  input outside Lean are not verified; any later change to these rows or to
  a cited label needs a successor review. Easley replay of the
  new modules: job 5690458 running (record follows).
  - Items (each verified independently by the integrator: build, refutations
    and audit exit 0 with no warnings, no sorryAx, forbidden-token grep
    empty), all with nothing supplied unless stated, no manuscript defect
    found:
    - L5-a TimeCompletion: H_a built as the completion of L^2(0,T) under the
      time form; positivity PROVED (subordination); separability, Schur
      extension, complexified norm, interval amplitudes; density of the real
      compact smooth tests, so H_a is the TeX's completion (decision 3 stretch
      done, not narrower). B24 L:masked-trig-products re-issued with nothing
      supplied (masked_trig_products_completed_paper).
    - L5-b MaskedContinuousWave (exact constant C_1 = 4 3^(1-a) C_0, route via
      B24 at shifted frequencies) and MaskedContinuousWaveCompleted
      (instantiated with H_a): L:masked-continuous-wave nothing supplied.
    - L5-c MaskedAuxiliaryNorm: P:masked-auxiliary-norm, same assumptions,
      narrower only by the real-H clause after complexification.
    - L5-d DampedNormsHomog: rest of L:damped-homogeneous-norms (scalings,
      both tails, smoothing/truncation in Le's reading); N_0 with the Green
      mass identity G_s(R^d) = s supplied as GreenMass. Coverage row by Le's
      decision: inputs-supplied, conclusion full; its scope-tex entry deleted.
    - L5-e VariationalMean: L:variational-heat-envelope (full) and the display
      of L:variational-global-mean (mixed-derivative sentence not
      formalized); the IsRayleighTrial side condition is automatic for h_s.
    - L5-f PhaseBessel: L:phase-bessel, full, more general.
  - Companion: branches wave-l5/a..f, integration 3039df3; umbrella/Axioms
    d476330 (1115 axiom-report entries, standard three only); docs
    225c589..75a34db (claims, coverage, ledger, README/FORMALIZATION);
    comparator 210cc3f (810 of 810 theorem claims; CheckFidelity 975 copied
    constants and 810/810 types equal, 0 problems; planted mutation caught;
    21 absolute paths removed from scaffold.json); check-controls PASS
    (68 controls, 92 refutations, 57 audits).
  - Reviews (Codex GPT-6.1-Sol, high) at 210cc3f over 975feb3: DampedNormsHomog
    PASS_WITH_NOTES (2 minor); TimeCompletion, MaskedContinuousWave,
    MaskedAuxiliaryNorm, VariationalMean, PhaseBessel FAIL on documentation
    only (6 major: index completeness, two route helpers labelled as TeX
    steps, one summary's parameter domains). All 8 accepted, repaired at
    43837e9..712c307 (incl. a comment-only module-doc fix). Evidence Article
    ac92bf5 (reviews/2026-11-11-lean-wave-l5-*). Confirmation at 712c307:
    PASS/high, 16/16, no findings (Article b0cdf9e,
    reviews/2026-11-11-lean-wave-l5-confirm).
  - Receipts at 712c307 (committed 5df6b9e): comparator pass (810 theorems);
    lower tier 0 sorry, 972 claim axioms standard, peak 7.4 GiB. (Receipts at
    210cc3f also passed; superseded by the repair commit, kept in session
    scratch.) Re-gated verified-private d40f394 -> 712c307 with comparator
    evidence; claims synced; `claims ledger`: READY, ok, 655 required, 945
    verified, 0 open, 27 out-of-scope (internal helper definitions).
    README verification record 78819e8.
  - Totals: 972 claims (810 theorems, 162 definitions); 535 labelled, 437
    unlabelled; coverage 46 rows (26 same-assumptions incl. 4 narrower,
    3 more with every conclusion proved and inputs supplied, 13 steps,
    4 outside); 33 whole-result modules, 56 library modules.
  - Open: the Easley leanchecker --fresh replay (job 5690458, nine targets:
    the seven new modules, the umbrella and Axioms; default mode for all 59):
    **PASS 9/9** (COMPLETED 0:0, 03:51:54, node831; each --fresh run
    41:41-43:52, peak 7.7 GB; default mode 59/59). The import-closure check
    (712c307 against 2f5ee14, 687e631, 837778a) shows every other module
    covered by an earlier --fresh replay up to comments. Evidence: companion
    bae18f4, verification/leanchecker-easley-wave-l5/ (HPC username,
    container path and runtime directory redacted), with the README replay
    sentence; DampedNorms and DampedNormsHomog have changed only in comments
    since 712c307; the 14 wave-L6 modules are not replayed yet. #24 told.
  From the board
  (companion branch docs/community), excluding the reserved B3, B4, B9.
  Three read-only feasibility reconnaissances against the TeX at 975feb3,
  every Mathlib name probed by compiling scratch files against the
  companion at 3a7d57f (session scratch l5-feas/R1-R3, Probe*.lean;
  several probes already contain working proofs: the scaling identities
  and the N_1 tail of the damped norms, the heat-envelope identity, the
  exponential-kernel square identity, a compiling H_a completion with B24
  at same assumptions modulo four form facts). Six items, one agent and
  one worktree each, as in waves L3 and L4:

  | Item | Target (label, TeX at 975feb3) | Builds on / new foundation | Class (fallback) | Size |
  |---|---|---|---|---|
  | L5-a | C21 `L:masked-time-completion` (integrated_covariance_foundation.tex 141-181), and B24 `L:masked-trig-products` with NOTHING supplied | Build H_a: the time form on L^2(0,T) as a pre-inner product (`timeForm`), Mathlib `UniformSpace.Completion`; positive semidefiniteness by the TeX's route (exponential-kernel square identity, triple Fubini, Gamma subordination via `TimeFractional`, integrability from the Schur bound); separability; then `hmem` and `hnorm` hold by construction and `masked_trig_products_bridged_paper` instantiates | same-assumptions (0 < a < 1, T > 0; no Gamma != 0, as the TeX says); conclusion narrower unless test density inside (0,T) is added (100-200 lines, stretch): H_a is the completion of L^2(0,T), shown equal to the TeX's completion of compact smooth tests only with that density. B24 becomes same-assumptions (fallback: PSD as one named hypothesis; B24 then has one supplied input instead of two) | 900-1100 lines |
  | L5-b | C21 `L:masked-continuous-wave` (378-423) | A different proof from the TeX's H_a-valued averaging: move the b-factors (r <= 1) and the coefficient <r>/r (r >= 1) into the C^1 amplitude, apply B24 at frequency 0 and compare brackets; the constant C_1 = 4 3^(1-a) C_0 is reproduced exactly (checked case by case). Stated first with B24's `hmem`/`hnorm` inputs, so it runs in parallel with L5-a; the integrator instantiates it with L5-a's H_a | same-assumptions once L5-a lands (fallback: keep the two inputs) | 450-650 lines |
  | L5-c | C21 `P:masked-auxiliary-norm` (77-137) | Paper-convention Fourier transform (`GaussianTest` already converts once); Tonelli with `MaskedSpectralGrowth.closedBall_le` for the uniform ball bound; local finiteness from it; temperedness by Peetre plus Schwartz decay; scalar Fourier inversion and an H-valued Bochner Fubini for the convolution identity | same-assumptions for the even/tempered/Radon, ball-bound and complex-Hilbert parts (H:homog, Gamma != 0, real nonzero Schwartz zeta); the real-H clause narrower (stated via complexification or omitted) (fallback: ball bound and measure properties, about 300 lines, with the convolution identity supplied) | 700-1000 lines |
  | L5-d | The rest of `L:damped-homogeneous-norms` (main TeX 745-846): N_1 and N_2^2 scaling, both tails `E:damped-tail-norms`, smoothing and truncation monotonicity, `N_0 = theta^-2`; bundled into one `_paper` theorem with the finiteness part already in `ClockCopyHomog` | Probes already prove N2sq_scaling, N1_scaling, N0's Laplace value and the N_1 tail; the N_2 tail via `K_eq_integral_weight` restricted to l > M; monotonicity by per-lambda weight comparison and `setIntegral_mono_set` | same-assumptions (H:homog only; no Gamma != 0), with two points for Le below: the reading of the smoothing/truncation sentence, and `N_0` (fallback: N_0's Green mass `G_s(R^d) = s`, imported in the TeX from Chen (2.5), as one named input; stretch: a `WaveGreen` module, d = 1, 2 easy, d = 3 via `Measure.toSphere`) | 450-650 lines (+250-350 stretch) |
  | L5-e | C18 `L:variational-heat-envelope` (integrated_unmasked_variational.tex 23-62) and `L:variational-global-mean` (64-96) | `MaskedSpectralGrowth.spectral_translated_gauss` (the identity is already proved in a probe), `VariationalDilation.conv`/`mean`; Lipschitz in time from `ContDiff.lipschitzWith_of_hasCompactSupport`; also discharges the `integrable_pot` side condition of `IsRayleighTrial` for the paper's potential | heat envelope same-assumptions (Gamma != 0 carried); global mean same-assumptions with a narrower conclusion: the displayed bounds 0 <= h_s <= M and the time-Lipschitz bound; "every mixed derivative is bounded" not formalized (stretch, about 400 lines) | 500-650 lines |
  | L5-f | C21 `L:phase-bessel` (integrated_wave_variance.tex 346-366) | none beyond Mathlib (Bochner integrals, inner products): 0 <= int sum ||g_j - phi_j||^2 with phi_j the projection, the TeX's own argument, no basis or Parseval | same-assumptions, more general (any measure space, any complete complex inner product space; separability not needed) (fallback: scalar H = C first) | 250-350 lines |

  Decisions for Le inside this approval (defaults in brackets):
  1. L5-d smoothing/truncation sentence (main TeX 789-791, used at
     1072-1082 and 1591-1600): read "Gaussian smoothing" as a multiplier g
     on mu with 0 <= g <= 1 and "restriction of a temporal Laplace domain"
     as restricting lambda to a measurable subset of (0,inf) [adopt this
     reading and state it in the ledger row].
  2. L5-d `N_0`: [named input `G_s(R^d) = s` now; `WaveGreen` as stretch].
  3. L5-a test density inside (0,T): [stretch; otherwise the row says
     narrower conclusion].

  Optional, only if an agent finishes early: `P:masked-quotient-obstruction`
  (253-292; the d = 2, alpha = 1 counterexample; E W(F)^2 read as the E:cov
  covariance functional, a definitional D1 boundary; core 250-400 lines,
  plus 300-450 to show this Gamma satisfies H:homog, or that part supplied);
  the finite Gaussian comparison of `P:masked-noise-completion` (d') (A <= B
  in PSD order gives E||N(0,A)||^p <= E||N(0,B)||^p; the convolution
  identity already compiles; 200-300 lines); the Rayleigh-form part of
  `P:variational-unmasked-rate` (rate Lipschitz with a uniform positive
  floor and I_Psi in (0,inf), no inputs, narrower: no operator; 400-550).

  Gates as in wave L4: compile and `#print axioms` (standard three only),
  no sorry; exact-hypothesis `_paper` wrappers; refutations importing the
  package and naming negation theorems; Audit printouts;
  claims/ledger/index/coverage rows; check-controls; comparator
  regeneration (Challenge, ChallengeDefs, Solution, CheckFidelity) for
  every new theorem claim; lean-pkg receipts of both tiers at one commit
  (no edits in the checkout while a receipt runs), regate, `claims ledger`
  READY with 0 open; one Codex GPT-6.1-Sol correspondence review per item
  with a packet built from the declarations its rows name, plus a
  confirmation review; Easley `leanchecker --fresh` of the new and changed
  modules; Le closes the gate. Stopping condition: all six items
  integrated and reviewed, or an item at its fallback scope with the
  remainder recorded as a named input; at most two repair rounds per item.
  Board effect if all land: C21 gains four results and B24 needs nothing
  supplied; `L:damped-homogeneous-norms` becomes complete; C18 gains two
  lemmas.

  Not in L5, with reasons: the rest of C19 (`L:spatial-static-controls`,
  `P:spatial-smooth-ratio`, `P:spatial-four-linear`,
  `P:spatial-energy-map`, `P:occupation-physical-class`): every finiteness
  claim about S_1^pos, R_0 and R_sp comes from T:full-upper (D1), so in
  Lean they would take one stochastic input (`S1Bdd`, boundedness of the
  score set), and their H^1 versions need "D8-lite" (density of smooth
  compact functions in the hand-rolled weak-gradient H^1); class O cannot
  be stated verbatim. Proposed for a later wave once Le decides whether
  results resting on `S1Bdd` are worth stating now. Also out:
  `P:masked-noise-completion` except (d') (needs the noise, D1);
  `P:wave-two-variances` (D1, D8; only an inputs-supplied deterministic
  core with four inputs would be possible), `P:wave-square-columns` and B22
  `P:actual-wave-form` (D1, D8); the operator half of
  `P:variational-unmasked-rate` (D8); the seven infinite-dimensional C22
  results. Mathlib news for the roadmap: the pinned Mathlib has
  `BesselPotentialSpace` (H^{s,p} via the Fourier transform) and
  `SchwartzMap.denseRange_toLpCLM`; connecting them to `WeakSobolev.MemH1`
  would give D8-lite (estimated 800-1500 lines).
- **WAVE L12: APPROVED by Le (2026-11-12) as proposed, with the default answers to its decisions.** Le, verbatim: "I approve Lean waves L12, L13 and L14 as proposed in lean-progress/PROGRESS.md, with the default answers to their decisions. Launch L12's items that cite only a284420 labels now on <MACHINE> and <MACHINE>; start R0 after the L11 docs merge." Proposal as written: From read-only preparations (session scratch
  l12-prep/: INVENTORY.md, DEBT.md, D8-FEASIBILITY.md; probes compiled on
  Office at Mathlib `56a0058`), with classes predicted under Le's 2026-11-12
  rules (strict whole result, split modelled-object rule with the
  model-choice register, every-cell Index rule, version levels); "debt Bx"
  are DEBT.md items, "board Bx" the reserved packages. Consolidation and
  quick wins: the re-anchor, the L11 docs upgrades, the hygiene batch before `v1.0.0`, and
  small deterministic results and no-gos. Excludes board B3, B4, B9.

  WHERE IT RUNS. Office: formalization, 6 agents in worktrees through
  `office-build.sh` (8G cap, `LEAN_NUM_THREADS=4`, at most 6 concurrent
  builds). <MACHINE>: 2-3 agents through `homedell-build.sh` (at most 3
  concurrent builds). <MACHINE>: orchestration, merges, lean-pkg comparator and
  lower-tier receipts (the registry lives here). Easley: gates only (see
  EASLEY STAGING below).

  | Item | Target (labels, TeX at a284420; no-gos at 672a8c56, repinned by R0) | Deliverable | Class after (fallback) | Size |
  |---|---|---|---|---|
  | L12-R0 (Office, 1 agent, first) | all 220 labelled results + 4 covered displays; 33 new `P:nogo-01`..`-33` (`notes/no-go/*.tex`) | line remap of about 4,700 TeX references in about 350 files by the hunk map (scratch `build-reanchor-a284420-*.py` tooling); `provenance/manuscript-anchor.json` (new revision, title, subtitle, sha256 including `notes/no-go/*.tex`); COMPLETION 220 -> 253 rows (33 "not formalized") | no class change: all 227 T/P/L/C statements and proofs byte-identical (sha1 by `work/envs.py`, 0 changed, 0 removed) | script + ~350 files; no Lean statement |
  | L12-DOC (<MACHINE>) | `L:finite-word-cutoff` (main 2531-2571), `L:uniform-series-tail` (3703-3748), `L:terminal-wick` (3600-3699), `L:fixed-split`, `P:interval-coefficients` (debt C2, C3) | docs after merging `wave-l11/K10` into L11 int: multi-mode `finite_word_cutoff_paper` and `finite_word_cutoff_integral` (nothing supplied); constructed chain measures (`e9e62f2`) | `L:finite-word-cutoff` inputs-supplied/weaker -> same-assumptions (whole if the review accepts the coordinatewise reading of the integral sentence, otherwise narrower: "integrals of words taken coordinatewise"); `L:uniform-series-tail` -> whole (constructed measures, split rule); `L:terminal-wick` -> same-assumptions, narrower (partial sums, complex r) until L12-TW; `L:fixed-split`, `P:interval-coefficients` lose hQ (Le's temporary acceptance retired), `DuhamelWords` named instead, stay narrower (SegmentBound, DysonCrossCube, BackgroundPreserves, EntireCoefficients, hsplits) | docs only |
  | L12-TW (<MACHINE>) | `L:terminal-wick` (debt B1, B2) | partial-sum comparison `E(sum r^n Y_n)^2 <= E(sum r^n Y'_n)^2` from `terminal_wick_mono_constructed_paper` and `mixed_moment_odd`; complex r: `E|sum r^n Y_n|^2 = sum r^m conj(r)^n E[Y_m Y_n]` (check the TeX first: is the comparison claimed for complex r, or only the formula) | whole (fallback: real r only, narrower: "complex r not stated") | 180-450 |
  | L12-C1 (<MACHINE>) | `L:damped-homogeneous-norms` (main 803-919), covariance-smoothing remark (debt C1) | `IsSpectralMeasure (volume.withDensity gamma_eps) (e^(-c eps abs(xi)^2) mu)`: Fubini of `phi(x) e^(i xi.x) e^(-eps abs(xi)^2)` against Lebesgue x `mu` (tempered `mu`, Schwartz `phi`), from `gammaEps_spectral`; not Fubini against the infinite `Gamma` (Le's L8 decision 2) | same/weaker -> whole, its only gap (fallback: row stays narrower, "covariance smoothing identified as multiplier membership only") | 250-500 |
  | L12-HYG (Office, 1 agent, after the L10/L11/K10 merges) | no label (debt group a, debt B3, B6, B7) | comment batch A1-A11 (L9 residue deferred three times; six stale "L9-G/L8-c will prove" docstrings); dedup of the nine duplicate groups (`alpha_lt_two` x3 to `HomogCovariance.alpha_lt_two`; `one_add_sum_le_prod`; `heatDens` -> `heatK`; `gammaEps` naming hazard; three Green Fourier predicates; `K0`; `Nnorm`; `SpaceTimeCS`; `HermiteWord` native copy); unused-hypothesis probe of the "carried, unused" K2/K4/K8 fields; `im_root_le` at lambda/2: in-domain witness `r = a + i lambda`, `a^2 >= 3 lambda^2/4`, checked against `PhaseRangeBounds`, or a recorded non-refutation | no row class change; two claim rows removed and `gammaEps` renamed (major after release, so before `v1.0.0`); `ImaginaryRoot` control (c) -> (a) if the witness holds | ~50 comment lines; net -150..-300; 40-150 |
  | L12-NG1 (Office) | `P:nogo-15`, `-16`, `-26`, `-30`, `-33` | `K = M1^T M1 + M0^T M2 + M2^T M0`, `(1,-2)K(1,-2)^T = -16/45` (probed) and the sigma^2 coefficient; `J_c = c^(2/(2-r)) J_1` via `mgf_gaussianReal`; scalar Young with `D = lambda t`; `lp.single` bumps (probed); matrix and integer arithmetic (probed) | whole each (fallback -15: the O(sigma^4) remainder as named input `PhaseSeriesRemainder`, inputs-supplied, whole) | 900-1500 |
  | L12-NG2 (Office) | `P:nogo-22`, `-23`, `-17`, `-28`, `-18` (scalar half) | restatements on `masked_quotient_obstruction_paper` (probed), `gaussian_one_variance_test` with general n (`integral_sum_sq_sq`, probed), ClockCopy (alpha = 1 identity), the exact ceiling at d = 2, alpha = 5/4, a = 1/2; `I = 545/11616`, `M = 1025/21483` from `MiddleCross.actual` at b = 1, c = 11/10 (probed) | -23, -17, -28 whole; -22 narrower: the noise W is not constructed (as its parent); -18 narrower: identification of I and M_b(0;A) with the TeX integrals missing (DIAG) | 700-1300 |
  | L12-NG3 (Office) | `P:nogo-01`; `P:envelope` (main 1937-2007), growth display | Stirling and `SeriesType.log_factorial_bounds`; `c t^rho <= log B_K <= C t^rho`; `log B_K ~ t^(beta/(beta-1))` | -01 whole; `P:envelope` new row, proof steps (first display needs `L:pairing-product-envelope`, D5) | 600-1000 |
  | L12-SRC (<MACHINE>) | `L:source-finite-comparison` (source_convergence.tex 20-40), `L:tube-half-action` (gaussian_tubes.tex 485-501), `P:tube-rayleigh-transfer` (183-224) | `gaussian_seminorm_moment_le_paper` at `B = C I` with `sqrt C` by `CFC.sqrt_algebraMap` (`CFC.sqrt_smul` does not exist; Probe2); sup exchange in extended reals; layer-cake transfer on `RayleighTail` | first two whole; transfer inputs-supplied, whole (named input `TubeTail`, the Borell tail of `L:tube-closed-geometry`, D3, a true statement) | 650-1250 |
  | L12-F1 (Office) | `E:fock-sandwich` of `L:fock-form` (main 2484-2488); `StaticInteractionCompleted.FockSandwich` | Hermite-truncated Fock space `PiLp 2 (idx_(<=N)^m -> L^2_band)`; diagonal `mulOp`; `A_0 = mulOp(abs(eta)^2 1_band)`; `CFC.sqrt (A_0 + rho^2) = mulOp(sqrt(...))` by `CFC.sqrt_eq_iff`, `invSqrtShift` by an explicit inverse (P30, P32 probed); then `FockForm.fock_form` + `FockColumnBound`. No D8, no pilot | no class change: `C:static-interaction`, `P:static-phase-all-orders` lose `FockSandwich`, stay narrower (CPInputs, PropagatorBlock, Gaussian parity, first-variance bounds) (fallback: CFC identification + named input `FockPackaging`) | 500-900 |

  Dependencies: R0 after the L11 docs merge (K10 merged into L11 int) and
  after the Article's uncommitted edits (at drafting time: `notes/no-go/*.tex`,
  `no-go-appendix.tex` and the main TeX, the gold-lexical repair) are
  committed; pin that commit and re-run the byte-identity check against it. DOC after the K10 merge; TW after DOC. HYG on the merged tree,
  once. NG1-NG3 off R0 (their labels exist only at the new anchor). C1, TW,
  SRC, F1 cite only a284420 labels and may start before R0 (remapped by the
  same hunk map at integration). Expected: rows upgraded to whole 4
  (`L:finite-word-cutoff`, `L:uniform-series-tail`, `L:terminal-wick`,
  `L:damped-homogeneous-norms`); new rows 4 (3 whole, 1 proof steps); no-gos
  11 (9 whole, 2 narrower). Gates as in L8-L11 (Codex GPT-6.1-Sol correspondence
  reviews with complete packets, repairs, confirmation, receipts, Easley array
  replay, Le closes the gate); at most two repair rounds per item.

  EASLEY STAGING (applies to L12-L14; Le asked to scale up gradually). Rules:
  compile locally; Easley runs gates and measured work only; preflight the
  container with `type -P`; stop after two identical failures.
  - Stage 1 (approved, L11 decisions 1-3): the array replay (build job,
    one-task pilot, array of `leanchecker --fresh` targets, 2 CPUs / 36G per
    task) at every gate commit. L8 reference: 92/92, 1 h 31 min, 53 CPU-h
    used. D8-style modules peak at 8.75 GB on <MACHINE> (about 1 GB above the
    L11 sizing), inside the 36G allowance.
  - D8 pilot (L11 decision 5, Le's own condition). The premise does not hold:
    77 of 81 modules already `import Mathlib`, so every replay since L3 has
    loaded the D8 slice. Options: (a) waive; (b) one extra task in the next
    array gate, `leanchecker --fresh` of `D8Probe.P50_workload` (Office:
    30.7 min, 8.75 GB); (c) the designed job (`d8/easley/`, 4 CPUs, 16G,
    about 1.3 h). Recommended (b).
  - Stage 2 (APPROVED by Le 2026-11-12): lower-tier receipts by `lean-pkg
    receipt slurm`, piloted at the L9 gate and compared with the local
    receipt at the same commit (claim set, axioms, sorry count); the
    comparator stays local (no bwrap or Landlock on Easley). Pre-gate replays
    of integration commits, new modules only (first run: L10 integration
    `f0b795f`, 21 targets, submitted 2026-11-12).
  - Stage 3 (later, after stage 2): overlapping arrays, at most about 600
    CPUs of the 1440 QOS cap.

  Decisions for Le (defaults in brackets): 1. R0 timing [after the L11 docs
  merge and the commit of the no-go edits; one re-anchor for every L12
  branch]; 2. version level of R0 [patch: references and 33 not-formalized
  rows only, unless the book revision is a new MAJOR]; 3. items citing only
  a284420 labels start before R0 [yes]; 4. HYG in L12, one full rebuild and
  one receipt round, before `v1.0.0` [yes]; 5. F1 now, independent of the D8
  pilot [yes]; 6. `P:nogo-29` [out: it defines the objects of board B3/B4;
  alternative: allowed as a self-contained counterexample module with no
  claim on B3/B4 statements]; 7. class predictions above under the strict,
  split and every-cell rules (-22, -18 narrower; `P:envelope` proof steps)
  [yes]; 8. D8 pilot option [(b)]; 9. Easley stage 2 [approved 2026-11-12;
  after a matching pilot at the L9 gate, L12 receipts come from Slurm]; 10. fallbacks
  are true named inputs, never surrogates; two repair rounds [yes].

  Not in L12: board B3, B4, B9 with `L:gram-realization`,
  `L:gram-dual-minimum`, `L:white-cdf-square`; `P:nogo-29` (decision 6); the
  diagram no-gos (L13); debt B5, B8 and the zero-covariance cases (L14 with
  the class-O bridge); C8-C10 beyond F1 (they shrink input lists, change no
  class; L15 candidates); everything needing D1, D5, D7 or D8.

- **WAVE L13: APPROVED by Le (2026-11-12) as proposed, with the default answers to its decisions.** Le, verbatim: "I approve Lean waves L12, L13 and L14 as proposed in lean-progress/PROGRESS.md, with the default answers to their decisions. Launch L12's items that cite only a284420 labels now on <MACHINE> and <MACHINE>; start R0 after the L11 docs merge." Proposal as written: Structure: the two-chain diagram
  model and the Chapter 3 upper bounds for alpha <= 1 with their no-gos; the
  K5 `H^1` Hilbert layer; three row-upgrading bridges. Runs as L12 (Office 6-8
  agents, <MACHINE> 2-3, <MACHINE> receipts, Easley stage 1 gate).

  | Item | Target (labels, TeX at the R0 anchor; a284420 lines shown) | Deliverable | Class after (fallback) | Size |
  |---|---|---|---|---|
  | L13-DM0 (Office, 1 agent, first) | foundation for `P:mixed` (main 658-728), E:mixed-moment | `DiagramModel`: ordered chains, time simplices, pairings as FiniteWick involutions with self-pairings, d = 1 Green kernels, `J_(m,n,D)(t)`, `A_k(t)`; spectral form for general Gamma; named input `MixedMoment` = the exact statement of `P:mixed` (true; D5). Interfaces frozen, then a fidelity review against E:mixed-moment and (2.21) (self-pairings, chain orientation) before D1-D6 start | foundation; `DiagramModel` entered in the model-choice register (the TeX's deterministic integrals) | 800-1200 |
  | L13-D1 (Office) | `L:d1-spatial` (4525-4594) | opening/closing label-set bound on `S_(D,eps)(h)` | whole on the model | 600-1000 |
  | L13-D2 (Office) | `P:d1-upper` (4605-4687) | `A_k(t) <= (2ZK)^k t^(beta k)/(k! k^(bk))`; `E u^2 <= exp(C_2 t^kappa)` by `sum_rpow_le_rpow_sum` | narrower: coefficient display whole; moment display rests on `MixedMoment` about an unconstructed `u` (split rule) | 800-1300 |
  | L13-D3 (Office) | `P:low-alpha-upper` (4820-4901), `C:d1-first-calibration` (4923-4957) | `K_sp^gen` from LowAlphaConvolution and AlphaOneConvolution (d = 1, 2, 3); `C_1 = C_2/2^((4-alpha)/(3-alpha))`, `2C_1 < C_2` | as D2: narrower (moment displays via `MixedMoment`); calibration constants whole | 800-1300 |
  | L13-D4 (Office) | `L:white-test` (734-758), `P:riesz-small` (4313-4393), `P:nogo-04` | order-two closed forms by Beta integrals; the a -> 1 limit `2^(2-alpha)(1-alpha)` | -04 whole; the two lemmas narrower: values proved for `J_(m,n,D)`, the identification with `E X_1^2`, `E X_2` is `MixedMoment` | 900-1500 |
  | L13-D5 (Office) | `P:nogo-02`, `-05`, `-06`, `-07` (`-03` optional) | adjacent-matching formula and Gamma-vs-factorial-cube consequence (with L12-NG3); chronological-merging support obstruction; geometry-free majorant exponent 3-a; label-span lower bound | whole (stated on diagram integrals); -03 narrower (remainder from D2, `u` unconstructed) | 1000-1600 |
  | L13-D6 (Office, optional) | `P:white-four` (4160-4218) | the nine order-four integrals | whole on the model | 1500-2500 |
  | L13-NG4 (Office) | `P:nogo-13`, `-20`, `-31`, `-24` | test functions near the plane vs `abs(x)^(-3/2)`; two disjoint bumps; 2x2 phase exponential and d'Alembert cutoff; `Lambda^(-gamma)` not compact via `Lp.fourierTransformₗᵢ` (probed) and weakly null translations | whole each (fallback -24: `Lambda^(-gamma)` given as a translation-invariant bounded operator, narrower) | 1100-1900 |
  | L13-K5a (Office, after the pilot decision) | foundation (D8-lite); C19 fidelity | real `f`: `MemH1 f` with weak gradient `g` <-> `MemSobolev 1 2 (toTemperedDistribution f)`; `norm^2 = norm f^2 + (2 pi)^(-2) norm g^2` (Mathlib's convention); density of `C_c^infty` and Schwartz in `H^1` | foundation; P:spatial-four-linear etc. restated on Mathlib `H^1`, no class change (fallback: `MemH1 -> MemSobolev` only, converse named `H1Converse`) | 500-800 |
  | L13-K5b (Office, after K5a) | foundation (form layer) | complex Lax-Milgram ported over `RCLike` (Mathlib has the real one only, P20); `q_V + c` bounded coercive Hermitian on `H^1` (bounded real V; signed V with `E:signed-multiplier-form` as hypothesis); bounded resolvent `R_V`: self-adjoint, positive, injective, `norm <= 1`; the real/complex reduction as a proved lemma | foundation (fallback: real Lax-Milgram, complexification as named input `ComplexifiedResolvent`) | 400-700 |
  | L13-C4 (<MACHINE>) | `L:variational-global-mean` (unmasked_variational 64-96) | every mixed derivative of `h_s` bounded: differentiation under the integral against tempered Gamma | same/weaker -> whole (fallback: first derivatives only, narrower) | 300-700 |
  | L13-C5 (<MACHINE>) | control of `gauss_shift_le`, S:static-phase | in-domain refutation for every `PhaseCovariance` with `mu != 0`, `q != 0`: growth `R^3` vs `R^alpha` mass of `B_(2R)` | control (c) -> (a); no row change | 200-450 |
  | L13-C6 (<MACHINE>) | `P:masked-auxiliary-norm` (covariance_foundation 88-137) | the real-H clause: generalize over `RCLike`, or `H x H` with a complex structure | same/weaker -> whole (fallback: row stays narrower, "real H after complexification") | 300-600 |

  Probed: Probe1 (`Real.Gamma`, `Complex.betaIntegral`, Stirling,
  `Lp.fourierTransformₗᵢ`, `ContDiffBump`); D8 P10, P13, P20, P50 (K5/K6
  workload 8.0 s, 7.0 GB). Not probed: LowAlphaConvolution, AlphaOneConvolution,
  HigherRieszTwo/Three names (checked against the merged tree at start).
  Dependencies: D1-D6 on DM0's frozen interfaces (stubs allowed); D5 on
  L12-NG3; K5a on the pilot decision; K5b on K5a. Expected: 6-7 Chapter 3
  labels (2-3 whole, 4 narrower with `MixedMoment`), 7-9 no-gos whole, 2 rows
  to whole (C4, C6). DM0 is the one new definitional layer of the three waves
  and carries the main fidelity risk.

  Decisions for Le (defaults in brackets): 1. DM0 first, interfaces frozen
  and reviewed by a family other than the author before D1-D6 [yes]; 2.
  `DiagramModel` in the model-choice register, so statements about diagram
  integrals are whole and statements about `u`, `X_n` narrower via
  `MixedMoment` [yes]; 3. `MixedMoment` is the exact statement of `P:mixed`,
  recorded in BOUNDARIES.md [yes]; 4. K5 starts once the D8 pilot task has
  passed [yes]; 5. manuscript norms defined explicitly, never the
  `BesselPotentialSpace` norm (2 pi factor) for manuscript constants [yes];
  6. complex Lax-Milgram in the companion, an upstream Mathlib PR optional
  later [yes]; 7. D6 and -03 only with spare capacity [yes].

  Not in L13: `P:mixed`, `L:joint-fixed-order`, `L:spatial-wick-measures`
  (D1/D5); `L:pairing-product-envelope` (needs `L:translated-covariance-CS`;
  L15 candidate); `P:static-holder-upper`, `P:planar-upper`,
  `P:three-transfer` (very long, static inputs); K6 (L14).

- **WAVE L14: APPROVED by Le (2026-11-12) as proposed, with the default answers to its decisions.** Le, verbatim: "I approve Lean waves L12, L13 and L14 as proposed in lean-progress/PROGRESS.md, with the default answers to their decisions. Launch L12's items that cite only a284420 labels now on <MACHINE> and <MACHINE>; start R0 after the L11 docs merge." Proposal as written: Operator layer: K6 in resolvent form,
  the K1 completion spaces, the higher-dimensional transfer and the d = 3
  endpoint corollaries, the class-O bridge on K5. Runs as L12/L13.

  | Item | Target (labels, TeX at the R0 anchor; a284420 lines shown) | Deliverable | Class after (fallback) | Size |
  |---|---|---|---|---|
  | L14-K6a (Office) | operator half of `P:variational-unmasked-rate` (unmasked_variational 98-140); first sentence of `L:signed-spectral-wave`; `P:signed-closed-form` (signed_static 39-109) | `R^(1/2)` by CFC; `range R^(1/2) = H^1` with `norm(R^(-1/2) u)^2 = q(u) + c norm(u)^2`; `inf spec H := c' - 1/norm R` = Rayleigh infimum, through the real reduction to `WeakSobolev.rayleighRate` | narrower: the operator is defined by its resolvent (H^2 domain and `LinearPMap` self-adjointness missing; `v_Psi = E W(Psi)^2` stays D1) (fallback: named input `FormDomainSqrt`, the KLMN fact) | 500-900 |
  | L14-K6b (Office) | `E:compact-quarter-power`, `E:signed-quarter-phase` | `R_B <= R_A`, `CFC.nnrpow_le_nnrpow` at 1/4 (P42 probed), norm comparisons | proof steps of `L:compact-fractional-phase` and `P:signed-closed-form` (fallback: half powers only) | 300-500 |
  | L14-K6c (Office) | `P:compact-ground-family` (compact_mean_family 33-112); `IndexedCone.GroundFamily` | Birman-Schwinger `K_kappa = V^(1/2)(kappa^2 - Delta)^(-1) V^(1/2)` on the Fourier side with `mulOp`; top eigenvalue attained (P40); `kappa -> norm K_kappa` monotone, continuous; `psi` in `H^1` at `E_1 = -kappa^2`; level Lipschitz bound | new row narrower: simplicity, positivity, `E_2` and gap `d_0` (named input `GroundSimpleGap`; min-max absent), `H^2` continuity of `p_sigma` missing; compactness by the TRUE named input `BirmanSchwingerCompact` (Hilbert-Schmidt for d <= 3; no HS in Mathlib); `L:raw-block-indexed-cone` stays narrower | 800-1400 |
  | L14-K1a (Office) | `L:occupation-raw-square` (occupation_ceiling 23-90); rest of `L:positive-raw-embedding` (intrinsic_constant 22-110) | `H_sp`, `Q: H^1 -> H_sp`, `rho_g`, `H_I`, `J_G` as `Lp G 2` completions, no tensor identification; `norm(rho_g)^2 = A(g)` | new row narrower (class O by joint representatives until L14-O); `L:positive-raw-embedding` stays narrower (mean identity `E:positive-raw-mean` out) with the `H_t`, `H_I`, `J_G` gap closed | 1300-1700 |
  | L14-K1b (Office) | `L:source-spatial-heat` (source_convergence 129-158), `L:positive-physical-gram` (intrinsic_constant 112-155) | `H_Gamma` completion, separability, Schwartz tests, heat positive contraction; finite covariance vectors `k_i` in `H_I` | heat lemma whole; Gram lemma narrower (entrywise order sentence out: adjacent to board B3) | 900-1400 |
  | L14-HT (Office) | `P:higher-transfer` (5020-5163), `C:higher-riesz` (5239-5269), `P:higher-obstructions` = `P:nogo-08` (5271-5329) | debt B4 bridge `smoothCov (riesz c alpha) eps = ofReal (conv ...)`; Hoelder in time and Gamma constants on `DiagramModel`; Riesz corollary with `L:higher-riesz`; divergence of the translated wave convolutions | -08 / `P:higher-obstructions` whole; transfer and corollary narrower (moment displays via `MixedMoment`, `u` unconstructed) (fallback: `C:higher-riesz` with named input `HigherTransfer`) | 1700-2800 |
  | L14-3D (<MACHINE>) | `L:product-endpoints` (6106-6200), `L:endpoint-closure` (6317-6380), `L:plane-endpoints` (6235-6315), `C:three-product-riesz` (6795-6839), `C:three-finite-images` (6841-6885) | endpoint arithmetic, Gaussian Hoelder comparison; closure under nonnegative sums and invertible linear images; plane endpoints, `V_low = c/pi`; the two assemblies | the three lemmas whole (fallback: PD of product Riesz densities as named input `RieszProductPD`, inputs-supplied, whole); corollaries narrower (`ThreeTransfer` = `P:three-transfer` named; `u` unconstructed) | 1500-2400 |
  | L14-O (<MACHINE>) | `P:spatial-four-linear` (debt C7); class-O bridge (debt D3) for `P:occupation-physical-class`, `P:raw-occupation-energy`, `L:occupation-rayleigh-selection`, `T:intrinsic-occupation-ceiling`, `C:intrinsic-spatial-bracket`; their zero-covariance cases (debt B9) | topological joint continuity on `(H^1)^4` via K5; strongly `H^1`-measurable fields <-> joint representatives by simple-function approximation; Gamma = 0 cases | `P:spatial-four-linear`, `P:occupation-physical-class` -> whole; the other four lose the class-O clause and the zero case, stay narrower (C_2 sentences, `T:intrinsic-second-moment`, D1) | 1000-2000 |
  | L14-K6d (optional, deferred) | `L:symplectic-free` supplied free group (C9) | `E = H^(1/2) x H^(-1/2)` from `BesselPotentialSpace` pairs, the free group as a Fourier-multiplier matrix, strong continuity, weak nullity of translations | removes `FreeWaveData`; row stays narrower (Young sums, D7) | 600-900 |

  CORRECTION TO THE L11 TEXT OF K6. L11 listed "compact resolvent as a named
  input (Rellich is not in Mathlib)". That would be a FALSE input: for
  `H = -Delta - V` on `R^d` the essential spectrum is `[0, infty)` (the
  manuscript's imported Teschl Theorem 10.2), so `(H + c)^(-1)` is not
  compact and a wrapper assuming it would be vacuous. The true named input is
  `BirmanSchwingerCompact` (compactness of `V^(1/2)(kappa^2 - Delta)^(-1)
  V^(1/2)`, Hilbert-Schmidt for d <= 3); an alternative true input is "the
  bottom is an isolated eigenvalue". Both go into BOUNDARIES.md with
  provenance.

  Probed (d8/probes, pin `56a0058`): CFC on `H ->L[C] H`, `CFC.sqrt_eq_iff`,
  Loewner-Heinz (`CFC.nnrpow_le_nnrpow`), `CStarAlgebra.inv_le_inv_iff`, the
  compact self-adjoint spectral theorem with the top eigenvalue attained
  (P40), `LinearPMap.adjoint` (P41); absent: `LinearPMap.spectrum`/`cfc`,
  closed forms, min-max, Rellich, Hilbert-Schmidt (P12), CFC on real Hilbert
  spaces (P31). Dependencies: K6a/b/c on K5b; L14-O on K5a; HT on DM0 and
  debt B4; 3D's corollaries on 3D's lemmas. Risk: K6 high (1600-2800 lines
  with K6a-c), K1 medium. Expected: about 12 labels gain or upgrade a row
  (5-6 whole, the rest narrower with the missing part named), 2 rows to whole
  (`P:spatial-four-linear`, `P:occupation-physical-class`).

  Decisions for Le (defaults in brackets): 1. K6 in resolvent form, results
  classed narrower ("operator defined by its resolvent"); full D8 stays a
  separate investment decision [yes]; 2. replace L11's "compact resolvent"
  by the true inputs `BirmanSchwingerCompact` and `GroundSimpleGap` [yes];
  3. K6d [deferred; only with spare capacity]; 4. K1 as `Lp G 2`
  completions, no tensor identification (as L9 decision 4) [yes]; 5. the
  entrywise-order sentence of `L:positive-physical-gram` [out, adjacent to
  board B3]; 6. d = 3 corollaries with `ThreeTransfer` named, `P:three-transfer`
  itself not formalized [yes]; 7. Easley stage 3 (overlapping arrays, at most
  about 600 CPUs) [only after two clean stage-2 runs].

  Not in L12-L14, with reasons: board B3, B4, B9, `L:gram-realization`,
  `L:gram-dual-minimum`, `L:white-cdf-square`; `P:nogo-29` unless Le allows
  it (L12 decision 6); everything needing D1, D2, D3 beyond `TubeTail`, D5
  beyond `MixedMoment`, D7, or full D8 (`LinearPMap` self-adjointness on
  `H^2`, unbounded functional calculus and the spectral wave matrices
  `E:compact-spectral-wave`, the wave half of `L:signed-spectral-wave`,
  min-max for `E_2`, Rellich, pointwise multipliers on `H^s`); Schatten-class
  results (absent from Mathlib); `P:three-transfer`, `P:planar-upper`,
  `P:static-holder-upper`; `P:nogo-21`, `-25`; `T:first`, `T:crude`
  (imported statements: record them as imported, not "not formalized").
- **WAVE L15: FIRST ITEM SCHEDULED (Le, 2026-11-12).** Le, verbatim:
  "Schedule the uniform E-mean layer (T_R, E, B_E, the L^r mean class) as an
  L15 item to close L:positive-raw-embedding; record it in
  lean-progress/PROGRESS.md." Item **L15-UM** (uniform E-mean layer). Target:
  the mean identity `E:positive-raw-mean` (T_R Psi(s) = B_E(m_R h_(Psi,s))
  a.e.) and the canonical-version sentence of `L:positive-raw-embedding`
  (`integrated_intrinsic_constant.tex` lines 33-38 at a284420; proof
  paragraphs 57-66 and 94-109), the last parts missing after L14-K1a
  (`95f45b7`: H_t, H_I, J_G built; both identities of
  `E:occupation-raw-identities` proved). Objects to build, none in the
  companion now: T_R = J_R, the uniform E mean of `S:uniform-physical-products`
  (`integrated_uniform_products.tex` line 2) and `L:uniform-mean-tensor`
  (`integrated_uniform_mean.tex` line 145); the state space E with Lambda and
  the lift/pairing B_E (`L:uniform-E-lift`, `E:uniform-E-pairing`,
  `integrated_uniform_products.tex` lines 33-37); the row
  `E:uniform-mean-row` (`integrated_uniform_mean.tex` line 15); C_t and the
  L^r mean class with fixed r, 2 < r < 2/a; the identification of the mask
  `RemoveMask.mask` (chi(abs(x)/R)) with m_R = eta(./R)^2 where the TeX needs
  it. Builds on K1a's `OccupationCompletion` (and K1b's `SourceHeatGram`
  after their H_I is unified at L14 integration). Expected class:
  `L:positive-raw-embedding` -> whole if every conclusion is reached under
  the TeX hypotheses (fallback: narrower, naming what is missing; true named
  inputs only, no surrogates). Host Office; to be sized and its
  dependencies fixed when L15 is proposed (line refs re-pinned by R0). Other
  L15 candidates noted in L12/L13: C8-C10 beyond F1,
  `L:pairing-product-envelope`.
- **WAVE L20: APPROVED by Le (2026-11-22).** Le, verbatim: "I approve L20 as checked with the default answers to all thirteen decisions. Record it in lean-progress/PROGRESS.md on top of origin master (check for a held candidate first), sync <HUB>, then launch L20-0 on <MACHINE> after the L19 merge and tag, and report." Proposal (checked against the L19 gate `fe9f1de` and TeX `0788ddee`, 2026-11-22): `~/.local/state/n22-l20/L20-PROPOSAL.md`. Scope (decision 1(a)): `P:mild-construction` (2151-2165; proof 2171-2340) for every source field in d = 1, 2, 3 (items L20-0 interface 450-700, A occupied multiplication and closure 300-600, B X_n in the closed polynomial space 200-450, C joint measurability 500-1,100 (fallback `JointMeasurability` 2213-2219), D last-vertex disintegration 400-700 (fallback `TerminalFubini` 2257-2260 with 4276-4285, or d = 1, 2), E d = 3 Green-width limit 200-500, F Steps 5-6 400-900), plus R the d = 1 Riesz instance of H:homog (500-1,200; fallback: the explicit Riesz hH stays), W the deferred wrappers (white P:d1-upper, Riesz wrappers without hH, composed C:d1-first-calibration, P:low-alpha-upper second inequality, rho > kappa reversing the L17 reword-only choice; 150-400) and DOC the deferred comment-only docstring pass (L15-L19 items and the 162 '1.1.0 candidate' labels). Total 3,100-6,550 (likely about 4,000). Probes (Office, throwaway): D FEASIBLE (general n and d; the main risk retired), A FEASIBLE WITH GAPS (transfer and multiplication bound; closure step remains), R FEASIBLE WITH GAPS (posdef field and Gaussian step; spectral identity remains; the triple Fubini needs three separately justified swaps). Expected: COMPLETION 54/22/1/34/2/107 -> 59/21/1/30/2/107 (if R fails 57/20/3/31/2/107); no label leaves 'not formalized', no listed named input removed; hH leaves three rows. Book origin checked first: no held candidate (1.1.3 public, freeze lifted by #23).
- **WAVE L19: GATE CLOSED by Le (2026-11-22).** Le, verbatim: "I close the L19 gate. When the receipts and Easley evidence land, run the gate --check, merge wave-l19/int to dev main, tag L19-gate, update COMPLETION.md, record it in lean-progress/PROGRESS.md on top of origin master (freeze is lifted), sync <HUB>, and report." Gate commit dev `fe9f1de`. Easley `leanchecker --fresh` 12/12 and default 200/200 (`a330722`); docs repairs `e6e1cb1`, `487872f`, `b994fc0`; receipts pending at the time of this record (the merge, tag and COMPLETION milestone follow in a later record).
- **WAVE L19: APPROVED by Le (2026-11-21).** Le, verbatim: "I approve L19 as checked with the default answers to all thirteen decisions. Record it in lean-progress/PROGRESS.md on top of origin master (check for a held candidate first), sync <HUB>, then launch L19-0 on <MACHINE> and report." Proposal (checked against the L18 gate `6e4644d` and TeX `0788ddee`, 2026-11-21): `~/.local/state/n22-l19/L19-PROPOSAL.md`. Scope: L19-0 interface (model M9, frozen targets, M9 fidelity review before C-E) 700-1,000 lines; A isonormal map and Gaussian law, Mathlib only (fallback `SourceNoise`) 450-800; B source-covariance features, `E:pairing-source-covariance` (1352-1370) 500-1,000; C two-family terminal Wick and the reversal identity to M8 at positive widths (1643-1650, 858-905; fallback `TerminalReversal` 888-905 or d = 1, 2) 900-1,800; D `L:joint-fixed-order` Step 4 and the L^2 sentence (1949-1965, 1858-1861, 1651-1655) 700-1,400; E `P:mixed` (834-849; 851-927), `E:expansion` (542-549), `MixedMoment` and `FirstMomentSeries` discharged, seven consumer wrappers 900-1,800; G `L:vertex-crude` (2062-2074; 2076-2145) 600-1,200. Total 4,750-9,000 (middle about 6,900). Probes (Office, throwaway): A at two points FEASIBLE WITH GAPS (finite-support isonormal field is a `CenteredGaussianField`; Gram-matrix Gaussian law); C at m = n = 1 FEASIBLE in d = 1, 2, 3 (E[X_1 Y_1] = `wickF ... (capDom δ) ε ... t t`, TeX 888-905). Expected: `P:mixed` and `L:vertex-crude` formalized, `L:joint-fixed-order` whole, `MixedMoment` and `FirstMomentSeries` discharged (named inputs: five listed, three open); COMPLETION about 55/24/1/31/2/107. Main risk: item C at general m, n (n-vertex reversal change of variables with per-vertex widths). Corrections recorded by the check: positive-width chain integrals do not equal an M4 diagram directly (identification moves to E via `joint_limit_aux`); the d = 3 Green-first sentence is mostly proved (`TerminalWickRegularization`); the L17/L18 records' statement that the L^2 construction needs gaussian-chaos-lean was a planning error. Book origin checked first: no held candidate.
- **WAVE L18: GATE CLOSED by Le (2026-11-21).** Le, verbatim: "I close the L18 gate. Merge wave-l18/int to dev main, tag L18-gate, update COMPLETION.md, record it in lean-progress/PROGRESS.md on top of origin master on a local held/n24-l18-gate branch while the 1.1.2 freeze holds, sync <HUB>, and report." (The 1.1.2 freeze was lifted by #23 before the record was written, so it is pushed directly.) Gate commit dev `6e4644d` (tag `L18-gate`). Content: `L:spatial-wick-measures` whole with nothing supplied (model M8); `L:joint-fixed-order` narrower with nothing supplied (deterministic half; the L^2 construction, Step 4 1949-1965, not formalized); the named input `DiagramLimits` discharged for every `H:homog` covariance in d = 1, 2, 3 (A: domination route and the d = 1 classification; E: joint diagram limits); decision-13 unsmoothed d = 3 bounds; no fallback used. Route differences disclosed: A domination (decision 3), C cap (0,1/(2k)] and damping 1/2 inside route (b) (decision 4), D four Step 4-5 arguments, E spectral d = 3 eta-removal (decision 8) and squeeze. Receipts `afd018d` at `6e4644d`: lower tier 0 sorry, standard axioms, claim_axioms 6022 (none nonstandard or missing); comparator 1902 + 2960 PASS; scratch-registry `gate --check` exit 0 at `6e4644d` and at the tip. Easley `leanchecker --fresh` 14/14 and default 189/189 (`eb19140`). lean-fence and lean-regress CLEAN against `02f922f`. Reviews: DeepSeek V4 Pro eight statement scopes PASS/PASS_WITH_NOTES, high, no MAJOR or CRITICAL (statement side closed by Le); GPT-6.2-Sol documentation FAIL on documentation only (two CRITICAL downgraded to MINOR by Le), repaired at `a83c778`; confirmation per packet with the broadened citation audit FAIL with MINOR remainders, applied at `aad8b91` without a further model call (Le). Deferred: Lean docstring items L1-L8 and `WickMass` wording to the docs-only Lean pass. Merged (fast-forward) to dev main; COMPLETION milestone `L18-gate` at `470ee26`; <HUB> synced. Review records: `~/.local/state/Le-AI-Lab/stratonovich-lean-wave-l18-review/ADJUDICATION.md`.
- **WAVE L18: APPROVED by Le (2026-11-21).** Le, verbatim: "I approve L18 as proposed with the default answers to all decisions." and, after the check against L17 (`68d0c5e`) and TeX `0788ddee`: "I confirm the checked L18 proposal with the default answers to all thirteen decisions, including the new decision 13. Record it in lean-progress/PROGRESS.md on top of origin master (check for a held candidate first), report the two probe results when they finish, then launch L18-0 on <MACHINE>." Proposal (checked 2026-11-21): `~/.local/state/n22-l18/L18-PROPOSAL.md`. Scope: L18-0 interface (model M8: gap coordinates, Green measures, per-vertex widths; identity to M4, inequality to M7) 600-900 lines; A `DiagramLimits` discharge for Riesz d = 1 by domination (route difference, disclosed; the limit coefficients become input-free, `MixedMoment` stays) 300-700 (+150-300 optional d = 1 classification); B spatial positive Laplace (1657-1722) 700-1,200; C Steps 2-3 of `L:spatial-wick-measures` by the envelope route instead of Brownian motion (1726-1798; fallback `WickMassBound`) 700-1,300; D Steps 4-5 (1802-1847; fallback `SpatialWickWeakLimit`) 1,200-2,100; E deterministic half of `L:joint-fixed-order` (1864-1945; fallback `JointTemporalTail` or d = 1, 2), d = 3 by eta-removal through the spectral route (decision 8) and the unsmoothed d = 3 versions of L17's bounds (decision 13) 1,400-2,500 (+100-200). Total 4,900-9,000 (middle about 6,800). Expected: `L:spatial-wick-measures` whole, `L:joint-fixed-order` narrower (111 -> 109 not formalized); `DiagramLimits` discharged (7 named inputs listed, 5 open); `MixedMoment` stays. Main risk: Step 4 measure theory (D); second: d = 3 eta-removal. Probes before launch (decision 9): Step 4 at k = 1 and A's domination lemma. Correction recorded by the check: `d1_upper_paper_riesz` takes `MixedMoment`, not `DiagramLimits` (only `coeffALim_riesz_le` uses `DiagramLimits` directly); the L17 proposal's statement that `DiagramLimits` needs L17 was a planning error (not a manuscript defect). Book origin checked first: no held candidate.
- **WAVE L17: GATE CLOSED by Le (2026-11-21).** Le, verbatim: "I close the L17 gate. Merge wave-l17/int to dev main, tag L17-gate, update COMPLETION.md, record it in lean-progress/PROGRESS.md on top of origin master d72121b0 (check for a held candidate first), sync <HUB>, and report." Gate commit dev `68d0c5e` (tag `L17-gate`). Content: `L:translated-covariance-CS` and `L:pairing-product-envelope` whole with nothing supplied (label-set model M7, bridge from M4; interface amendment 1: `M4BridgeTarget` requires finite Green densities, Le's decision); `L:crude-corrected` and `P:envelope` narrower with `MixedMoment` supplied (diagram bounds d = 1, 2, and d = 3 for Green-smoothed kernels uniformly in eta, time-boxed item E3 funded by Le; `E:envelope-growth` without the comparison rho > kappa, Le's decision). Receipts `d1a3a12` at `68d0c5e`: lower tier 0 sorry, standard axioms, claim_axioms 5642 (none nonstandard or missing); comparator 1798 + 2757 PASS; scratch-registry `gate --check` exit 0 at `68d0c5e`, `be81d6e` and the tip (docs-only descendant, claims-declaration line ✓). Easley `leanchecker --fresh` 16/16 and default 176/176 (`0bf7a39`). lean-fence and lean-regress CLEAN against `38ac748`. Reviews: DeepSeek V4 Pro seven statement scopes PASS_WITH_NOTES/high, no MAJOR or CRITICAL; GPT-6.2-Sol documentation FAIL on documentation only, repaired at `a34a5eb`; confirmation per packet FAIL with PARTIAL remainders, applied at `be81d6e` without a further model call (Le); the docs-a confirmation report was extracted from the reviewer's final message and NOT accepted by the runner, accepted by Le. Deferred: Lean docstring line numbers and wording to the docs-only Lean pass. Merged (fast-forward) to dev main; COMPLETION milestone `L17-gate` at `02f922f`; <HUB> synced. Book origin checked first: no held candidate (1.1.1 public, freeze lifted by #23). Review records: `~/.local/state/Le-AI-Lab/stratonovich-lean-wave-l17-review/ADJUDICATION.md`.
- **WAVE L16: GATE CLOSED by Le (2026-11-20).** Le, verbatim: "I close the L16 gate. Merge wave-l16/int to dev main, tag L16-gate, update COMPLETION.md, record it in lean-progress/PROGRESS.md (check for a held candidate first), sync <HUB>, then launch L17 on <MACHINE>." Gate commit dev `ebac849` (tag `L16-gate`). Receipts `2d34d33` at `ebac849`: lower tier 0 sorry, standard axioms, claim_axioms 5134 (none nonstandard or missing); comparator 1677 + 2460 PASS; scratch-registry `gate --check` exit 0 at `ebac849` and at the tip (docs-only descendant, claims-declaration line ✓). Easley `leanchecker --fresh` 16/16 and default 161/161 at `ebac849` (`c4df976`). Reviews: DeepSeek V4 Pro statement scopes S1-S4 PASS_WITH_NOTES (notes applied, `108fa80`); GPT-6.2-Sol documentation docs-a/docs-b FAIL on documentation only, 19 findings repaired (`ca75d10`); one confirmation per packet on `108fa80` (docs-a FAIL/medium, docs-b INCONCLUSIVE/medium; no CRITICAL or MAJOR left after adjudication); six wording fixes applied at `5f0d8c8` without a further model call (Le). Le's decisions: `CutoffCompact` kept as a named input, not scheduled; `L:positive-raw-embedding` upgraded to full; `P:cameron-temporal-map` stays narrower. Deferred: four Lean docstring line numbers (CameronFinal, UniformMeanCutoff, CameronTemporalMap, CameronSpatial) and the `PositiveRawEmbeddingTarget` docstring, with the L15 docstrings, to a later docs-only Lean pass. Merged (fast-forward) to dev main; COMPLETION milestone `L16-gate` at `38ac748`; <HUB> synced. Review records: `~/.local/state/Le-AI-Lab/stratonovich-lean-wave-l16-review/ADJUDICATION.md`. Book origin checked first: no held candidate (#23, 2026-11-20).
- **WAVE L17: APPROVED by Le (2026-11-20) as proposed, with the default answers to all twelve decisions.** Le, verbatim: "I approve L17 as proposed with the default answers to all twelve decisions. Record it in lean-progress/PROGRESS.md, run the Step-2 probe on <MACHINE>, and launch L17 only after the L16 gate closes." Corrections by #24 (formerly #22) on checking the draft against the TeX: `L:crude-corrected` begins at main line 1978 (not 1970); decision 12's "#3" is #46 (<MACHINE>/n46-svn) after the 2026-11-20 fleet renumbering (sys-ops correction; #7 is a second window on the same Codex conversation).
  Proposal as written (#24, 2026-11-20): Le, verbatim: "At the
  same time, shall we prepare L17?" (asked while the L16 gate runs). This is a draft only.
  Nothing is built and no repository is changed. The Lean track stays FROZEN (Le,
  2026-11-13) except for items Le approves one by one; this proposal asks for one such
  approval. Basis: L16 as integrated on dev `wave-l16/int` `1d9883a` (docs part 1
  `6485db9`). The draft assumes that the L16 gate closes on that content.

  **Scope (recommended): the pairing-envelope chain.** Formalize the deterministic
  core of Chapter 2's finite product bound for two ordered chains:
  `L:translated-covariance-CS` (L16's optional item E, which was not done) and then
  `L:pairing-product-envelope`, both whole. Then apply them on the diagram model M4
  (`DiagramModel`, wave L13) to the deterministic halves of `L:crude-corrected` and
  `P:envelope`, with the same reading L13 used for `P:d1-upper`: bounds proved for the
  model diagrams at every noise width, and the moment sentences only through the
  existing named inputs `MixedMoment` / `DiagramLimits`. No new analytic named input
  is planned. All of it is deterministic: no gaussian-chaos-lean (D1, D5, K9), no
  Hilbert tensor product, no `CutoffCompact`.

  Why this one:
  1. It is the standing next candidate. L13 deferred `L:pairing-product-envelope`
     because it needs `L:translated-covariance-CS`. L16 decision 2 assigned it to "a later
     wave with `L:translated-covariance-CS` as its first item".
  2. It is the hub of Chapters 2-3. The envelope is used by `L:joint-fixed-order`
     (main 1905), `L:crude-corrected` (1999, 2014), `L:vertex-crude` (2096) and
     `P:envelope` (2395), and through `L:crude-corrected` by `T:full-upper` (its proof
     cites `L:crude-corrected` once).
  3. It is the only route that later shrinks the named-input list. The diagram half
     of `L:joint-fixed-order` (marked-edge estimate `E:joint-temporal-tail`, main
     1913-1925) is an application of the envelope. Without the envelope,
     `DiagramLimits` (Riesz case) cannot be discharged.
  4. It is self-contained and needs no new Mathlib theory: lintegrals over ordered
     simplices, Fubini, monotone convergence and finite maxima. Its risk is
     combinatorial (the induction), not missing foundations.

  **Survey of the open work (what was considered and why it is not the default).**
  1. *The eight named inputs still supplied after L16.*
     - `MixedMoment` (`P:mixed`, main 834-849) and `FirstMomentSeries` (main 796,
       5856-5857) are statements about the solution and its chaos terms, which are
       not constructed. They need the noise and the L² chaos limits (D1/D5). Out.
     - `DiagramLimits` (Riesz case) is deterministic. Its TeX proof (main 1864-1966)
       uses `L:spatial-wick-measures` (1679-1848, not formalized) and the envelope (Step
       2). It is feasible only **after** L17 (L18 candidate below).
     - `SignedMultiplierForm` (`E:signed-multiplier-form`, signed_static 16-18) is about
       an unbounded `v_V`. It needs KLMN and self-adjoint forms (full D8). Already proved
       for bounded potentials. Out.
     - `ThreeTransfer` (`P:three-transfer`, main 7537-7556 and its long proof) is very
       long, with static inputs (L13/L14 exclusions). Out.
     - `TubeAttained` and `TubeTail` (`L:tube-closed-geometry`, gaussian_tubes 158-162)
       rest on the imported Borell-Sudakov-Tsirelson theorem for an infinite-dimensional
       Gaussian. Out (D3; no Gaussian-measure layer).
     - `CutoffCompact` (L16) is not scheduled (Le, 2026-11-20: "don't schedule the
       cutoffCompact follow-up now"). It is listed below only as a possible later item.
     - So none of the eight can be discharged in L17 from the companion's current
       foundations. L16's compact-operator foundation, H^s scale, fractional products
       and temporal map do not reach any of them: they serve the Cameron chain, and
       `CutoffCompact` is its only remaining input. The envelope is the prerequisite
       for the one dischargeable input (`DiagramLimits`).
  2. *`L:translated-covariance-CS`, then `L:pairing-product-envelope`.* This is the
     recommendation.
  3. *C8-C10 beyond F1.* DEBT.md is gone, and the records identify only **C9**: the
     supplied free group of `L:symplectic-free` (`FreeWaveData`; L14-K6d row,
     "`L:symplectic-free` supplied free group (C9)", est. 600-900). The context
     names C7 = `P:spatial-four-linear` (L14-O; done), C1 = covariance smoothing
     (L12-C1; done), C2/C3 = the `L:fixed-split` / `P:interval-coefficients` docs
     (L12-DOC; done), and L13 items C4-C6 (done). The records do not determine C8 and
     C10. The L12 note "C8-C10 beyond F1 (they shrink input lists, change no class)"
     and F1 (`E:fock-sandwich` of `C:static-interaction` and `P:static-phase-all-orders`)
     suggest the remaining supplied inputs of those two results: `CPInputs`, the
     imported Crouzeix-Palencia theorem, which Mathlib lacks; `PropagatorBlock`;
     the Gaussian parity; and the first-variance bounds. None changes a class.
     C9 is cheaper now because L15 built `E = H^(1/2) x H^(-1/2)` with its Fourier norm
     (alternative 5 below).
  4. *Narrower rows that could become whole.*
     - `L:uniform-mean-tensor` (L16: finite tensors only) and the projection/tail half
       of `P:uniform-mean-regulator`: both need the completed tensor product (item 5).
     - `L:uniform-mean-cutoff`: uniqueness, and density of tests for every real sigma.
       Density was part of the `CutoffCompact` overrun estimate.
     - `L:positive-raw-embedding`: L16 records it as still narrower. The reasons are
       spec-to-map identification and kernel completions; a small docs+Lean follow-up
       could state "the specifications determine the maps" (cheap, 200-400 lines).
       This is a candidate add-on (decision 6).
     - The rate/cost-identification rows of the occupation chapter: the missing
       identification is stochastic. Out.
  5. *The regulator's projection and tail half: feasible now?* **Yes in principle at the
     Mathlib pin `56a0058`.**
     - Mathlib has `TensorProduct.instInnerProductSpace` on `E ⊗[𝕜] F`
       (`Mathlib/Analysis/InnerProductSpace/TensorProduct.lean`, with `inner_tmul`) and
       `TensorProduct.mapL` with `norm_mapL_le : ‖mapL f g‖ ≤ ‖f‖ * ‖g‖` (lines 603-607).
     - `UniformSpace.Completion.innerProductSpace` exists, so
       `Completion (H_t ⊗[ℝ] H_sp)` is a real Hilbert space, and `pi_J ⊗ P_K` extends
       from `mapL` by continuity.
     - The remaining work is mathematics, not missing Mathlib: the identification of
       M5's kernel completion `H_I` with that completion (`L:cameron-supported-tensor`,
       cameron 194-220), then `L:uniform-mean-spatial-tails` (uniform_mean 81-190) and
       the second display of `E:uniform-completed-mean` (290-334).
     - `L:uniform-mean-tensor` as a whole still needs the extension into
       `L^r(I; G)`, which is not a Hilbert target. Use the TeX's Gaussian route or a
       direct finite-tensor density argument.
     - This is alternative 3 (2,500-4,500 lines, medium-high).
  6. *High-value results near the main theorems (honest distance).*
     - `T:full-upper` (main 4474-4945) needs:
       - the constructed solution (`P:mild-construction`, which needs `L:vertex-crude`
         and the L² limits of `L:joint-fixed-order`, D1);
       - `P:mixed` (supplied);
       - `P:interval-coefficients` (narrower, inputs supplied);
       - `L:terminal-wick` and `L:uniform-series-tail` (whole);
       - `L:fixed-split` (narrower).

       L17 adds the deterministic upstream piece `L:crude-corrected` (diagram level).
       The theorem stays outside Lean until the solution is constructed (gaussian-chaos /
       D1). It is several waves away and not reachable without that foundation.
     - `T:intrinsic-second-moment` (intrinsic_constant 437ff.) needs the Cameron-Martin
       / actual-noise chain: `P:cameron-actual-embedding`, `P:uniform-actual-cameron`,
       the source convergence chapter and `L:positive-uniform-optimizer`, all not
       formalized, most of them stochastic. L16 closed the deterministic Cameron mean
       maps. The stochastic remainder needs gaussian-chaos-lean. Not reachable in L17.

  **Anchor check (2026-11-20).** Book 1.1.0 = `0788ddee` (public). The other revisions
  are the companion's R `39f2597a`, v1.0.2 = `c3c2431d` and v1.0.3 = `dd4f1a78`. Here is
  `git diff --numstat` on every TeX file this proposal cites:

  | File | 39f2597a..c3c2431d | c3c2431d..dd4f1a78 | dd4f1a78..0788ddee | Cited lines moved? |
  |---|---|---|---|---|
  | `notes_stratonovich_ham_second_moment.tex` | +12 / -12 | +1 / -1 | identical | none. The only hunks are line 203 (title date) and 344-354 (front matter), 1:1 replacements. The file has 9276 lines at both ends, so every main-TeX line below is the same at R, v1.0.2, v1.0.3 and 1.1.0 |
  | `integrated_uniform_mean.tex` (alt. 3 only) | identical | identical | +14 / -3 | yes, as in L16: lines after 10 shift by +7 and +11 (1.1.0 lines given) |
  | `integrated_cameron_mean.tex` (alt. 3) | identical | identical | identical | none |
  | `integrated_symplectic_phase.tex` (alt. 5) | identical | identical | identical | none |
  | `integrated_compact_gaussian.tex` (later item) | identical | identical | identical | none |
  | `integrated_intrinsic_constant.tex` (cited) | identical | identical | identical | none |
  | `notes/figures/endpoint-elimination.tex` (figure after the envelope) | identical | identical | identical | none |

  Line ranges at `0788ddee` (statement; proof). For the main TeX they are identical at
  `39f2597a` and `c3c2431d`.

  | Label / display | File | Lines at 0788ddee |
  |---|---|---|
  | setup "Covariance pairings of translated kernels" (`E:translated-covariance-form`) | main | 1156-1185 |
  | `L:translated-covariance-CS` (`E:translated-covariance-CS` 1191-1193) | main | 1186-1197; 1199-1297 (Steps 1-4 begin at 1207, 1239, 1257, 1272) |
  | setup of the section (edge data, `E:pairing-edge-norms`, `E:pairing-diagram-general`, admissible assignments, `E:pairing-product-general`) | main | 1434-1488 |
  | `L:pairing-product-envelope` (`E:pairing-product-envelope` 1492-1495) | main | 1489-1500; 1502-1639 (Step 1 1510-1537 with `E:pairing-convolution-norms` 1527-1535; Step 2 1539-1595; Step 3 1598-1612; Step 4 1615-1627; Step 5 1631-1638) |
  | `E:crude-norms` | main | 1970-1976 |
  | `L:crude-corrected` (`E:crude-corrected`, `E:theta-envelope`) | main | 1978-1985; 1987-2054 |
  | `L:vertex-crude` (optional) | main | 2062-2074; 2076-2145 |
  | `P:envelope` (`E:homogeneous-envelope`, `E:B-envelope`, `E:envelope-growth`) | main | 2352-2373; 2375-2433 |
  | `L:damped-homogeneous-norms` (used; whole since L12) | main | 1010-1055; 1057-1154 |
  | `P:mixed` (named input `MixedMoment`, used) | main | 834-849 |
  | `L:joint-fixed-order` (not targeted; `DiagramLimits` reading) | main | 1853-1862; 1864-1966 |
  | alt. 2: `P:higher-transfer`; `C:higher-riesz`; `P:higher-obstructions` | main | 5936-5956; 5958-6098 / 6192-6197; 6199-6222 / 6230-6236; 6238-6300 |
  | alt. 3: `L:cameron-supported-tensor` | cameron_mean | 194-200; 202-220 |
  | alt. 3: `L:uniform-mean-spatial-tails`; `L:uniform-mean-tensor`; `P:uniform-mean-regulator` | uniform_mean | 81-99; 101-190 / 198-206; 208-255 / 272-288; 290-334 |
  | alt. 5: `L:symplectic-free` | symplectic_phase | 31-61; 63-160 |
  | later: `P:cutoff-singular-values` (compactness sentence) | compact_gaussian | 469-472; Step 1 487-519 |

  Recommendation: anchor all new L17 citations to 1.1.0 (`0788ddee`). L16 already
  re-anchors L15 to it (R1), so no re-anchor item is needed.

  **What each target needs, and what the companion already has.**
  - Already there:
    - `DiagramModel` (M4, L13): two ordered chains on `Fin (m + n)`, `pred`/`incr`,
      `twoSimplex`, pairings `Pi2` as involutions, `diagramPos` with nonnegative
      kernels `g : ℝ → Rd d → ℝ≥0∞`, `card_Pi2` = `(2k-1)!!`, chain reversal.
    - `DampedNormsHomog`, `DampedSmoothing`, `WaveGreen`: `N_0(theta) = theta^(-2)`,
      the scalings `N_1(theta) = theta^(alpha+alpha0-2) N_1(1)` and
      `N_2(theta)^2 = theta^(-beta) N_2(1)^2`, the multiplier comparisons and the
      covariance smoothing (`L:damped-homogeneous-norms` whole). These give
      `E:crude-norms` and `E:homogeneous-norms`.
    - `SeriesType.log_factorial_bounds` (Stirling-type bounds for `P:envelope` Step 2).
    - `RieszPositiveDefinite`: Gaussian subordination of Riesz powers.
    - `D1Spatial`, `TwoSimplexTime`: time integrals on the model.
    - `MixedMoment` and `DiagramLimits` as the established bridge from diagrams to
      moments.
    - Mathlib: `MeasureTheory.lmarginal` with `lmarginal_insert`/`lmarginal_union`
      (`Integral/Marginal.lean`) for integrating out one vertex,
      `integral_rpow_mul_exp_neg_mul_Ioi` (the Gamma mixture
      `|t|^(-a) = Gamma(a)^(-1) ∫ lambda^(a-1) e^(-lambda |t|) d lambda`), `Finset.sup'`
      for the finite maximum, and lintegral monotone convergence.
  - `L:translated-covariance-CS` needs:
    - the capped kernels `kappa_L`, `C_L` and `Q_L`, with the absolute bound
      `m_L ||f||_1 ||h||_1`;
    - the feature identity `∫ h_lambda(t,r) h_lambda(s,r) dr = e^(-lambda|t-s|)`;
    - Cauchy-Schwarz for `Q_L`, with the common-translation invariance;
    - the truncations `G_(i,M)` and monotone limits in M and in the cap L.

    Route choice (decision 4): the TeX's route goes through a Bochner integral of the
    norm-continuous feature map `Phi_L`. The proposed Lean route writes
    `Q_L(f,h) = ∫ F_L f · conj(F_L h) d(nu x mu x dr)`, with
    `F_L f(lambda,xi,r) = ∫ f(t,x) h_lambda(t,r) e^(i xi.x)`, by scalar Fubini, and then
    applies Cauchy-Schwarz in `L^2(nu x mu x dr)`. This avoids proving norm continuity
    and Bochner Fubini. It is the same feature-space argument without the
    vector-valued integral. The review must accept it as a proof of Steps 1-2.
  - `L:pairing-product-envelope` needs:
    - a **general** two-chain pairing integral `I_D(G)` with per-edge data
      `(nu_e on A_e, mu_e finite)`, kernels `G_l` on `(0,inf) x R^d`, infinite
      positive simplices and relative coordinates;
    - the norms `N_0`, `N_(1,e)` (Laplace-Fourier) and `N_(2,e)` (cap limit, using
      `L:translated-covariance-CS`);
    - the admissible assignments `A_D` (a nonempty Finset) and their products;
    - Step 1: the convolution norms (mass multiplicativity, `|LG| <= N_0(G)`, and
      Minkowski for `N_2` by the feature representation);
    - Step 2: the regional half-bound, by induction on n with vertex removal and kernel
      fusion `G_a * G_b`, plus the three-row slot table;
    - Steps 3-4: same-chain and terminal endpoint cases, and the two-region split;
    - Step 5: cap removal and the max of the finitely many limits.

    M4's `Fin (m + n)` indexing is awkward for deleting vertices. The interface should
    use a label-set model: chains as lists over a label type, edges as a Finset of
    pairs, integrals by `lmarginal`. A bridge lemma then maps M4 pairings onto it
    (decision 3).
  - `L:crude-corrected` and `P:envelope` (deterministic halves) need:
    - a bridge from M4 diagrams to `I_D`, with three parts:
      - the damping trick: `e^(-theta(s_n+s_2n)) >= e^(-2 theta t)`, and extending
        the finite-horizon simplex to infinite simplices;
      - the time covariance `|s-r|^(-alpha0)` as the Gamma mixture with
        `A_e = (0,inf)`;
      - the spatial covariance at positive width `eps` as the Fourier transform of the
        finite measure `e^(-eps|xi|^2/2) mu` (finite under `H:homog`, as
        `L:damped-homogeneous-norms` already uses);
    - then `E:theta-envelope` at every noise width, the choice
      `theta = theta_0 + n/t`, `P_n n^(-2n) <= 2^n/n!` and the series bound
      `(sum z^n/sqrt(n!))^2 <= 2 e^(2z^2)`;
    - for `P:envelope`: `E:homogeneous-envelope` at every noise width, the infimum
      `e^(beta k)(2t/(beta k))^(beta k)`, and `E:envelope-growth`
      (`c t^rho <= log B_K <= C t^rho`, `rho = beta/(beta-1)`);
    - the moment sentences (`E X_n^2`, `E u^2 <= ...`, `E u^2 <= B_K`) only for random
      variables satisfying `MixedMoment`, as in `D1Upper`;
    - the Green kernel as a density. That holds in d = 1 (`green1`) and in d = 2 (the
      wave kernel `(2 pi)^(-1)(s^2-|x|^2)_+^(-1/2)`). In d = 3 the TeX first smooths
      the Green measure (`p_eta * G`) and removes eta by an L² limit, which is
      stochastic. In d = 3 the diagram-level bound is therefore stated for the smoothed
      kernel, uniformly in eta (decision 5).

  | Item | Target (1.1.0 lines) | Deliverable | Class after (fallback) | Size on <MACHINE> (estimate) |
  |---|---|---|---|---|
  | L17-0 (orchestrator, first) | interface | label-set two-chain model: chains, matchings, per-edge `(nu_e, mu_e, A_e)`, kernels `G_l : ℝ → Rd d → ℝ≥0∞`, `I_D` on the infinite positive simplices, `N_0`, `N_(1,e)`, `N_(2,e)` (cap iSup), `A_D`, `P_(Q,iota)`; the frozen statements `TranslatedCSTarget`, `ConvolutionNormsTarget`, `RegionalHalfBoundTarget` (Step 2's claim, 1539-1595), `PairingEnvelopeTarget`; the M4 bridge signature; fallback named inputs, each the exact TeX sentence: `ConvolutionNorms` (1527-1535), `RegionalHalfBound` (Step 2); every instance named | infrastructure; `docs/l17/INTERFACE.md` | 400-700 (L16: 518) |
  | L17-A | `L:translated-covariance-CS` (main 1156-1297) | capped forms and absolute bound; feature identity; scalar-Fubini feature representation; Cauchy-Schwarz; common-translation invariance; truncations and cap limits in ℝ≥0∞; zero norms and measures included | whole (fallback: at finite cap L only, narrower) | 800-1,500 (risk: medium) |
  | L17-B | envelope Step 1 and Step 5; envelope setup | `E:pairing-convolution-norms` (mass multiplicativity, `|LG| <= N_0`, `N_2(G*H) <= N_0(G) N_2(H)` by the feature representation from A); cap removal; finite max of limits; `n = 0` and empty-chain cases | proof steps (fallback: `ConvolutionNorms` named input) | 500-900 |
  | L17-C | envelope Step 2 (1539-1595) | regional half-bound by induction on n: endpoint integration giving `N_(1,e0)`, `kappa` monotone, vertex deletion, kernel fusion at the successor, three-case slot table with counts `|Q_0| = |Q_1|`, `|Q_2|` even, factor 1/2 | proof step (fallback: `RegionalHalfBound` named input, true; the envelope then whole with inputs supplied) | 1,200-2,200 (risk: high) |
  | L17-D | envelope Steps 3-4 and assembly (1598-1639) | same-chain case on the whole domain; terminal pair through `L:translated-covariance-CS` with separate origins; region split `{s_a <= s_q}` and its complement; `(P+P')/2 <= max`; `pairing_product_envelope_paper` | `L:pairing-product-envelope` whole (fallback: whole with `RegionalHalfBound` supplied) | 500-1,000 |
  | L17-E | `L:crude-corrected` (1970-2054), `P:envelope` (2352-2433) | M4 -> `I_D` bridge (damping, Gamma mixture, finite smoothed spectral measure); `E:theta-envelope` and `E:homogeneous-envelope` for model diagrams at every noise width, d = 1, 2 (d = 3 with Green smoothing, uniform in eta); theta optimization, `P_n n^(-2n) <= 2^n/n!`, series bound; `B_K` infimum and `E:envelope-growth`; moment sentences for variables satisfying `MixedMoment` (`DiagramLimits` for limit coefficients) | both: not formalized -> inputs supplied, steps/narrower (narrower: solution not constructed; d = 3 only after Green smoothing); `E:envelope-growth` whole | 1,000-1,900 (bridge risk: medium-high) |
  | L17-F (optional, spare capacity) | `P:nogo-01` (L12-NG3's no-go, Stirling growth) | from `E:envelope-growth` | no-go row whole | 100-300 |

  Totals (estimates, not measurements): core L17-0..E 4,400-8,200 Lean lines, middle
  about 6,000, plus 100-300 for F. That is about the L16 scale or a little smaller.
  - Basis:
    - L16 measured 7,281 lines against a core estimate of 4,900-9,100. Its items ran
      9 to 22 Lean lines per TeX statement+proof line: cutoff 563/34, products
      1,378/71, spatial 738/83, temporal 2,010/90.
    - The targets here are about 142 TeX lines (A), 204 (envelope with setup) and
      about 170 (E). Ratios of 6-14 apply because most of it is lintegral bookkeeping,
      not new analysis, except C.
  - Agents: four on <MACHINE>, as in L16: A (L17-A, then helps D), B (L17-B, then D),
    C (L17-C), E (L17-E against the frozen `PairingEnvelopeTarget`, decoupled as L16-D
    was). Expect about 1-1.5 working sessions (L16: one session for 7,281 lines).
    C sets the pace: an induction over diagrams has no L15/L16 precedent. Add about
    half a day for the gate.
  - Labels expected to leave "not formalized": 4. Two become whole
    (`L:translated-covariance-CS`, `L:pairing-product-envelope`) and two inputs-supplied
    narrower (`L:crude-corrected`, `P:envelope`). `L:vertex-crude` stays not formalized:
    M4 has one common width, not vertexwise widths (decision 2). No row moves
    downward.

  **Main risks, Mathlib gaps and true-named-input fallbacks.**
  1. *The induction in Step 2 (high).* This is the main risk. Removing a vertex
     changes the chain structure, fuses two kernels and drops an edge. The induction
     hypothesis must be the full bound over all diagrams with n-1 edges, all kernel
     families and all edge data. Lean has no diagram calculus; a poor model choice
     costs days.
     - Mitigation: the label-set model, frozen in L17-0 before C starts.
     - A probe before launch (decision 7): prove the n = 1 cases and one slot-table
       row on the model, about 150-300 lines, on <MACHINE>.
     - Fallback: the true named input `RegionalHalfBound` (the claim proved in TeX
       lines 1539-1595). The envelope is then whole with inputs supplied, and A, B, D
       and E are unaffected.
  2. *The bridge in E (medium-high).* M4 uses the full `|s-r|^(-alpha0)` on a
     finite-horizon simplex and Green measures. The envelope takes per-edge Laplace
     mixtures, finite spectral measures and kernel functions.
     - Gaps: the Gamma mixture is in Mathlib. The wave Green kernel in d = 2 as a
       density needs a short lemma: `WaveGreen` has it as a measure, so this is a
       check-first item. d = 3 needs Green smoothing (decision 5).
     - Fallback: E restricted to d = 1 (`green1`), narrower with "d = 2, 3 not
       formalized".
  3. *Laplace-Fourier transform (low).* There is no API, but `N_(1,e)` needs only the
     definition and `|LG| <= N_0(G)` for `lambda >= 0`.
  4. *Hilbert-valued integrals (low with the scalar route).* `L^2(nu x mu x dr)` over ℂ
     is in Mathlib. The companion is real-valued elsewhere: the complex feature space
     is used only inside A, with `Q` real-valued at the end.
  5. *The ℝ≥0∞ conventions (low-medium).* The TeX allows zero norms and singular
     diagonals. State everything in ℝ≥0∞ with the TeX's finiteness hypotheses kept,
     since `0 * ∞ = 0` must not hide a case. The reviewers check this against the
     TeX's "zero norms and measures are allowed" (1497-1499).

  **Gate (as L15/L16, with their lessons).**
  - Build and local checks:
    - Local compile on <MACHINE> first. Then an Easley stage-2 pre-gate replay of the
      integration commit, new modules only (Easley via <MACHINE>).
    - Instances: every instance in a claimed module is named. A lint finds zero
      anonymous `instance :` in the new modules before claims sync (L15 dropped nine
      claims that named generated instances).
    - Claims-name check: every `claims.yaml` name resolves in the built environment,
      checked before receipts are cut.
    - Then the scratch-registry `gate --check`, again after every docs-only commit.
  - Receipts and records:
    - Lower-tier receipt and comparator receipt.
    - COMPLETION.md regenerated (milestone `L17-gate`).
    - Coverage rows and statement-ledger rows, with named-input entries for any
      fallback, citing per field the TeX lines that establish it (L15 note N3.1-N3.3).
    - The model-choice register gets the new label-set two-chain model (M7) and its
      bridge to M4.
    - `lean-fence` and `lean-regress` at integration, with no regressions in the L13
      diagram modules.
    - Easley `leanchecker --fresh` of the new modules plus default mode over all
      modules.
  - Reviews:
    - Statement scopes: DeepSeek V4 Pro (Le's main reviewer), tool-denied, one attempt
      per scope, SessionRetry disclosed. Packets are split to fit under the 32000-token
      output cap, or `OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX` is raised (L15 scope 4:
      three NO_REPORT on a 134 KB packet). The envelope's statement packet is small;
      its model definitions need a scope of their own.
    - Documentation scopes (ledger, coverage, COMPLETION, counts): GPT-6.2-Sol via
      Codex (own codex-home, effort high). Each packet contains every cited TeX line.
    - At most two repair rounds.
  - Records and closure:
    - The gate record goes on a held lean-progress branch while #16's book-origin
      freeze holds. Sync <HUB> after every push.
    - Le closes the gate; tag `L17-gate`.

  **Decisions for Le (defaults in brackets).**
  1. Scope: (a) L17-0..E; (b) (a) plus the optional F (`P:nogo-01`); (c) A..D only
     (the two lemmas, no M4 consumers). [(a); F only if an agent is idle]
  2. `L:vertex-crude`: out, because M4 has no vertexwise widths. Adding them to M4 is
     a model change, so it is better done with `L:joint-fixed-order` later. [out]
  3. Model: a new label-set two-chain model (register entry M7) with a bridge to M4,
     rather than proving the induction on M4's `Fin (m + n)`. [yes]
  4. Route for `L:translated-covariance-CS` Steps 1-2: scalar Fubini into
     `L^2(nu x mu x dr)` instead of the Bochner integral of `Phi_L`. Disclose it in the
     ledger as a route difference with the same feature space. [yes]
  5. Dimensions in E: d = 1 and 2 with nothing beyond `MixedMoment`/`DiagramLimits`;
     d = 3 stated for the Green-smoothed kernel uniformly in eta (eta-removal is the
     stochastic L² limit, not formalized). [yes]
  6. Add-on: state that L16's specifications `IsSpatialMeanMap` / `UTensorSpec` determine
     the maps (uniqueness), closing L16's caveat (i) on `L:positive-raw-embedding`
     (200-400 lines, docs + Lean). [no by default; yes if L16's gate review asks for it]
  7. Probe before launch: Step 2 at n = 1 and one slot-table row on the label-set model
     (Office, about half an hour). If the probe fails, launch with `RegionalHalfBound` as
     the planned fallback. [yes]
  8. Fallbacks: only true named inputs (`ConvolutionNorms`, `RegionalHalfBound`, each
     the exact TeX claim with its lines), never surrogates. [yes]
  9. Host and agents: Office, 4 agents in worktrees, `office-build.sh` (8G cap,
     `LEAN_NUM_THREADS` <= 8); Easley only for the gate replay; Mathlib pin unchanged.
     [yes]
  10. Review routes: statements by DeepSeek V4 Pro (split packets or a raised cap);
      documentation by GPT-6.2-Sol via Codex. [yes]
  11. Release: L17 joins the next companion release. If v0.11.0 (L15+L16, L16 decision
      11) is not yet cut when L17 closes, fold L17 into it. No book re-pin by default.
      [fold if timing allows; otherwise v0.12.0]
  12. Any manuscript defect L17 finds goes to #3 for a 1.1.x patch. Lean never narrows a
      statement to hide it. [yes]

  **Ranked alternatives (if Le prefers another L17).**
  1. *(Recommended above.)* Pairing-envelope chain, 4,400-8,200 lines: 4 labels leave
     "not formalized" and `DiagramLimits` becomes dischargeable later.
  2. *L14-HT, approved 2026-11-12 and moved to the future list by the freeze.* Targets
     `P:higher-transfer` (main 5936-6098), `C:higher-riesz` (6192-6222) and
     `P:higher-obstructions` = `P:nogo-08` (6230-6300). The work: the debt B4 bridge
     `smoothCov (riesz c alpha) eps`, Hoelder in time and the Gamma constants on M4,
     and the divergence of translated wave convolutions. L14's estimate was
     1,700-2,800 lines, medium risk. 3 labels move (`P:higher-obstructions` whole, two
     narrower with `MixedMoment`). It is smaller and safer than 1, but a branch rather
     than the hub. It is a good "light L17" or a companion item to 1 if a fifth agent
     is free.
  3. *Completed Hilbert tensor product package.* `Completion (H_t ⊗[ℝ] H_sp)` from
     Mathlib's `TensorProduct.instInnerProductSpace` and `mapL`; then
     `L:cameron-supported-tensor` (cameron 194-220) identified with M5's `H_I`; the
     projection/tail half of `P:uniform-mean-regulator` (uniform_mean 290-334);
     `L:uniform-mean-spatial-tails` (81-190); `L:uniform-mean-tensor` whole (198-255,
     the `L^r(I;G)` extension). Estimate 2,500-4,500 lines, medium-high risk (the H_I
     identification). It finishes the L16 Cameron chain short of `CutoffCompact`. The
     next consumer, `P:uniform-actual-cameron` (363-505), is stochastic.
  4. *No-go batch, approved in L12/L13 and frozen 2026-11-13.* L12 NG1-NG3 and L13 items
     D5 and NG4 (the L13 item names, not the foundations D1/D5): about 15 `P:nogo-*`
     rows, 3,900-6,500 lines at their estimates. Low risk, mostly probed. NG4's
     `P:nogo-24` (`Lambda^(-gamma)` not compact) is cheaper now with
     `CompactOperatorFoundation`. No-go rows are outside the 220-label count.
  5. *C9: `L:symplectic-free` free group (L14-K6d).* The free group on L15's
     `E = H^(1/2) x H^(-1/2)` as a Fourier-multiplier matrix, strong continuity and weak
     nullity of translations; removes `FreeWaveData`. About 500-800 lines (cheaper than
     L14's 600-900 because E exists). The row stays narrower (Young sums, D7), so there
     is no class change.
  6. *Operator layer K6a-c (L14, frozen).* Resolvent-form `P:variational-unmasked-rate`
     operator half, `E:compact-quarter-power`, `P:compact-ground-family`. Estimate
     1,600-2,800 lines, high risk. Several results stay narrower (D8).
  7. *Later only (Le: not now): `CutoffCompact`.* The compactness sentence of
     `P:cutoff-singular-values` (compact_gaussian 469-472, Step 1 487-519). It needs
     the Fourier transform of a product as a convolution, a Schur-test kernel operator
     on `HR d`, and density of tests in H^s for every real s. Estimate 1,100-1,500
     lines, high risk.
  8. *After L17: `DiagramLimits` (Riesz case).* `L:spatial-wick-measures` (main
     1679-1848) plus the marked-edge estimate `E:joint-temporal-tail` (1913-1925, an
     envelope application) give the deterministic half of `L:joint-fixed-order`. This
     would discharge one of the eight named inputs. Size unknown until
     `L:spatial-wick-measures` is read in full (its 150-line proof is not assessed
     here).

  **Could not be determined.**
  - The contents of C8 and C10. Only C9 (`L:symplectic-free` free group) is named in
    the records.
  - The L16 gate's final counts (claims, rows, classes) and whether its review changes
    anything L17 depends on (for example `CompactOperatorFoundation` names). Re-read
    when the L16 gate closes.
  - Whether `WaveGreen` already provides the d = 2 Green density as a function: check
    it in L17-0.
  - Whether DeepSeek's output cap can be raised on the current route.
  - Office load at launch.
- **WAVE L16: APPROVED by Le (2026-11-20) as proposed, with the default answers to all twelve decisions.** Le, verbatim: "I approve L16 as proposed with the default answers to all twelve decisions. Put the proposal into lean-progress/PROGRESS.md on the held branch, run the two compactness probes on <MACHINE> (L²-kernel compactness and CFC.sqrt), report the results, then launch L16." Launch after the probe results.
  Proposal as written (#22, 2026-11-20): Le, verbatim: "Shall we
  prepare L16 now?" Draft only: nothing is built, no repository is changed. The
  Lean track stays FROZEN (Le, 2026-11-13) except items Le approves one by one;
  this proposal asks for one such approval.

  **Scope.** Core: discharge the two named inputs L15 left supplied,
  `CameronSpatialMap` and `UniformMeanRegulator`
  (`StratonovichHAMSecondMoment/UniformMeanInterface.lean`, frozen at dev
  `06c3c6a`), by constructing T_R, C_t and U (the TeX's C_t (x) I) and proving
  the facts the structures carry. Then `L:positive-raw-embedding` can move from
  narrower with inputs supplied to whole, and the Cameron-map chain moves from
  not formalized. Stays FROZEN: C8-C10 beyond F1; `L:pairing-product-envelope`
  (an L17 candidate); everything needing gaussian-chaos-lean (D1, D5, K9); the
  projection and tail half of `P:uniform-mean-regulator` (decision 9). Optional,
  only with spare capacity: `L:translated-covariance-CS` (decision 2).

  **Note on the L15 estimate.** L15's UM-3 row (2500-4000 lines) listed only
  `P:cameron-spatial-map` and the four uniform-mean results. Discharging the
  structures as frozen also needs `L:cameron-fractional-products` (the bound
  that makes T_R bounded), the compactness sentence of
  `P:cutoff-singular-values` (for `isCompactOperator_T` and
  `isCompactOperator_apply`), `P:cameron-temporal-map` (the field `Ct`, its
  compactness and `Ct_test`) and the U part of `P:cameron-full-mean` (`U`,
  `U_tensor`). The sizes below include them, so they are larger than L15's row.

  **Anchor check (2026-11-20).** Revisions: v1.0.2 = original `c3c2431d` (L15's
  anchor); v1.0.3 = `dd4f1a78` (#16's release SHA); 1.1.0 = held candidate
  `0788ddee` (on origin master, not yet public). `git diff --numstat` on every
  TeX file L16 would cite:

  | File | c3c2431d..dd4f1a78 | dd4f1a78..0788ddee | What changed |
  |---|---|---|---|
  | `integrated_cameron_mean.tex` | identical | identical | none |
  | `integrated_uniform_mean.tex` | identical | +14 / -3 | 1.1.0 displays the E inner product (lines 10-17) and states that the row `E:uniform-mean-row` holds for all z, w in E through the product map of `L:cameron-fractional-products` (lines 28-32). Lines after 10 shift by +7 (the row) and +11 (from line 23 on) |
  | `integrated_uniform_products.tex` | identical | +3 / -1 | `L:uniform-E-lift` now states the tie Mu = Vu on tests and the continuous extension (L15 issue 1); lines after 36 shift by +2. Not an L16 target; cited by the L15 modules |
  | `integrated_intrinsic_constant.tex` | identical | identical | none |
  | `integrated_compact_gaussian.tex` | identical | identical | none |
  | `integrated_spatial_occupation.tex` | identical | identical | none |
  | `notes_stratonovich_ham_second_moment.tex` | +1 / -1 | identical | title-page date (line 203) only; no cited line moves |

  So for L16, v1.0.3 is line-identical to v1.0.2, and 1.1.0 differs only in the
  two uniform files. Line ranges (statement; proof):

  | Label | File | at c3c2431d (= v1.0.3) | at 0788ddee (1.1.0) |
  |---|---|---|---|
  | `L:cameron-fractional-products` | cameron_mean | 29-42; 44-99 | same |
  | `P:cameron-spatial-map` (`E:cameron-spatial-row` 113-118) | cameron_mean | 104-119; 121-186 | same |
  | `L:cameron-supported-tensor` (not targeted) | cameron_mean | 194-200; 202-220 | same |
  | `P:cameron-temporal-map` | cameron_mean | 225-237; 239-314 | same |
  | `P:cameron-full-mean` (U part) | cameron_mean | 322-342; 344-408 | same |
  | `E:uniform-mean-row` (equation; following sentence) | uniform_mean | 15-19; 20-21 | 22-26; 28-32 |
  | `L:uniform-mean-cutoff` | uniform_mean | 29-42; 44-62 | 40-53; 55-73 |
  | `L:uniform-mean-spatial-tails` (optional, decision 9) | uniform_mean | 70-88; 90-179 | 81-99; 101-190 |
  | `L:uniform-mean-tensor` | uniform_mean | 187-195; 197-244 | 198-206; 208-255 |
  | `P:uniform-mean-regulator` (`E:uniform-completed-mean` 271 / 282) | uniform_mean | 261-277; 279-323 | 272-288; 290-334 |
  | `L:uniform-E-lift` (cited, not targeted) | uniform_products | 33-44; 46-67 | 33-46; 48-69 |
  | `L:positive-raw-embedding` (`E:positive-raw-mean` 34) | intrinsic_constant | 23-40; 42-132 | same |
  | `P:cutoff-singular-values` (compactness sentence) | compact_gaussian | 469-479; 481-557 | same |
  | `P:spatial-four-linear` (already whole; used) | spatial_occupation | 297-315; 317-398 | same |
  | `L:translated-covariance-CS` (optional) | main | 1186-1197; 1199-1297 | same |
  | `L:pairing-product-envelope` (not in L16) | main | 1489-1500; 1502-1639 | same |

  Recommendation: anchor new L16 citations to 1.1.0 (`0788ddee`; public SHA
  recorded when #16 releases it). Reasons: 1.1.0 is the text that states the
  rough-state row L16 proves and displays the E inner product the Lean already
  uses, and it carries L15's three presentation fixes. In the same docs pass,
  re-anchor L15's citations from c3c2431d to 1.1.0. These are mechanical shifts:
  uniform_mean +7 or +11 and uniform_products +2. The text of `L:uniform-E-lift`
  also changes, which removes L15 interface issue 1. If 1.1.0 is not public when
  L16 docs freeze, cite c3c2431d (= v1.0.3 for these files) and re-anchor at the
  release (decision 3).

  **What each target needs, and what the companion already has.**
  - Already in the companion (dev main `09d3406`): `Hhalf`, `Hmhalf`, `lam`,
    `E`, `BE`, `IsMultiplier`, density of real tests, `exists_isMultiplier`
    (UM-0, `UniformMeanFoundation`, 795 lines); `coord sigma` is already defined
    for every real sigma, so H^s for alpha/4 < s < 1/2 needs no new model.
    `OccupationCompletion`: `Hsp S`, `Ht p`, `HI p S`, `J`, `incl`,
    `separableSpace_Hsp`, `dense_range_toHsp`. `PositiveRawMean`: `kBochner`,
    `inclTwo`, `U_incl_ae`, `inner_kBochner_toHsp`, `T_eq_BE`. `P:spatial-four-linear`
    is whole (wave L14). `MaskedAuxiliaryNorm.peetre` is Peetre's inequality.
    `TimeSchur.kern` and the row bound `row_le` exist. `FiniteGaussianMatrix`
    has Hermitian diagonalization.
  - Needed for `CameronSpatialMap` (E part): (i) the fractional product bound
    `||fg||_Hsp <= A_s ||f||_{H^s} ||g||_{H^s}` (dyadic real Fourier bands, each
    band in H^1, summed through `P:spatial-four-linear`); (ii) the uniform
    cutoff multiplier bound M_sigma (Peetre, `L:uniform-mean-cutoff`), giving
    `||k_R(z,w)|| <= M_0 ||z|| ||w||`; (iii) T_R defined from the bounded
    bilinear row by Riesz, the row on all states, and the smooth-test multiplier
    formula; (iv) compactness of each T_R q (cutoff gain one) and of the map
    q -> T_R q (finite-rank approximation through an orthonormal basis of the
    separable `Hsp S`, uniform on the compact set of rows). (iv) needs
    compactness of the cutoff multiplication `chi Lambda^(-gamma)`, which is
    the risky part.
  - Needed for `UniformMeanRegulator`: (v) C_t on `Ht p`: K bounded on L^2(I)
    (Schur), positive and injective, compact (truncation K_eps, L^2 kernel);
    the isometry iota with `||K^(1/2) f||_2 = ||f||_Ht` on tests; the L^r bound
    by the three-exponent Hoelder form of Young (TeX lines 280-293) and the
    pointwise-direction duality; compactness into L^r by interpolation;
    `Ct_test`. (vi) U on `HI p S` with `U_tensor` and `||U|| <= ||C_t||`, either
    through `L:uniform-mean-tensor` (Gaussian moment route, as in the TeX) or
    through a shorter route specific to this kernel: duality plus pointwise
    positivity of K gives
    `int int K <g_s, g_t> <= int int K ||g_s|| ||g_t||` (decision 5).
    (vii) `mean_bound` from `||T_R|| <= M_0` uniformly in R >= 1 and (vi).
  - Decoupling. `positive_raw_mean_paper` uses T, `row`, `smooth`, U,
    `U_tensor` and the L^r bound, never the compactness fields. L16-D therefore
    proves `E:positive-raw-mean` for the constructed maps directly. Then
    `L:positive-raw-embedding` does not depend on the compactness risk in (iv)
    and (v).

  | Item | Target (1.1.0 lines) | Deliverable | Class after (fallback) | Size on <MACHINE> (estimate) |
  |---|---|---|---|---|
  | L16-0 (orchestrator, first) | interface | frozen signatures: H^s spaces as `coord s` (Hermitian classes) with the embeddings H^(1/2) -> H^s (norm one) and `Lambda^(-1)` isometry; the constructors `cameronSpatialMap` and `uniformMeanRegulator` as the targets; the fallback named inputs `CutoffCompact` and `TemporalCompact`, each the exact compactness sentence of its TeX result; the direct theorem `positive_raw_embedding_constructed`; every instance named (no anonymous `instance :`) | infrastructure; a short design note `docs/l16/INTERFACE.md` | 300-600 Lean lines; about 0.5 h agent time plus the orchestrator's cold read (L15: 480 lines, about 20 min) |
  | L16-A1 | `L:uniform-mean-cutoff` (40-73) | M_sigma for every real sigma, uniform in R >= 1 (Peetre, `eta_R` hat scaling, L^1 * L^2 on the Fourier side, density); `||k_R|| <= M_0 ||z|| ||w||`, `||T_R|| <= M_0` (the second half after B2) | whole (fallback: sigma = +-1/2 only, narrower) | 400-800 |
  | L16-A2 | `L:cameron-fractional-products` (cameron 29-99) | real dyadic bands D_j f in H^1 (L^2 Plancherel `Lp.fourierTransformₗᵢ` to `WeakSobolev.MemH1`), `N(f_j) <= 2^(j alpha/4) ||f_j||_2`, `sum_j N(f_j) <= C_s ||f||_{H^s}`; the product map H^s x H^s -> Hsp with both displays and the identification of pairings with physical integrals | whole (fallback: the bound and the extension, pairings identified only for H^1 factors, narrower) | 900-1600 |
  | L16-B1 | compactness foundation; `P:cutoff-singular-values` (compact_gaussian 469-557), compactness sentence only | integral operators with L^2 kernel are compact (norm <= L^2 norm of the kernel; finite separated kernels dense; `isCompactOperator_of_tendsto`); `chi Lambda^(-gamma)` compact on H^sigma by a Fourier band cutoff (error <= N^(-gamma)) plus an L^2-kernel remainder; shared with C | `P:cutoff-singular-values` narrower: compactness, no s_j rate, no Schatten class (fallback: named input `CutoffCompact`, true) | 600-1200 (risk: high) |
  | L16-B2 | `P:cameron-spatial-map` (cameron 104-186), `E:uniform-mean-row` (22-32) | T_R by Riesz from the row; the row for all z, w in E; null classes to zero; `smooth`; compact values; compactness of the map (orthonormal basis of `Hsp S` by Gram-Schmidt on tests, finite-net argument); `cameronSpatialMap : CameronSpatialMap S eta R` | narrower: E part only (F columns, c_1 eta_R term and B_F not formalized; decision 8) (fallback: compactness fields from `CutoffCompact`, inputs-supplied) | 800-1400 |
  | L16-C | `P:cameron-temporal-map` (cameron 225-314) | Schur bound; strict positivity and injectivity (Gamma representation, Fourier form of e^(-lambda abs v)); compactness of K (truncation plus L^2 kernel, from B1); K^(1/2) by `CFC.sqrt` and its compactness (polynomial approximation through `cfc` continuity, closedness of compact operators); iota on `Ht p`; L^r bound (Hoelder form of Young, duality); interpolation; `Ct_test`; the divergence of finite orthonormal cell sums (not trace class, decision 7) | whole (fallback: narrower without the trace sentence; compactness from named input `TemporalCompact`) | 1200-2200 (risk: high) |
  | L16-D | `L:uniform-mean-tensor` (198-255), `P:uniform-mean-regulator` (272-334, first display), U part of `P:cameron-full-mean` (322-408), `L:positive-raw-embedding` (intrinsic 23-132) | U on `HI p S` through `kBochner` and density of `J`, `U_tensor`, `||U|| <= ||C_t||` (decision 5); `uniformMeanRegulator`; `mean_bound`; `positive_raw_embedding_constructed` (E:positive-raw-mean for the constructed T_R(C_t (x) I), a.e., with the canonical version) | `L:positive-raw-embedding` -> whole if the review accepts the canonical-version reading (L15 4b-F1 concerned exactly that sentence; fallback: narrower, "version agrees a.e., no measurability clause", nothing supplied); `P:uniform-mean-regulator` narrower (first bound and value class; projection/tail half out); `P:cameron-full-mean` proof steps (U and its bound); `L:uniform-mean-tensor` whole on the Gaussian route (fallback: not formalized, the kernel-positivity route used and disclosed) | 700-1300; Gaussian route +400-800 |
  | L16-R1 (<MACHINE>, docs) | all L15 citations | re-anchor of L15 citations c3c2431d -> 1.1.0 with the reviewed re-anchor tool (shifts above) | no class change | docs only |
  | L16-E (optional, spare capacity) | `L:translated-covariance-CS` (main 1186-1297) | Hilbert features h_lambda(t,r) e^(i xi.x) in L^2(nu x mu x dr), Bochner pairing, Cauchy-Schwarz, translation invariance, positive cap limit | whole (fallback: at finite cap only, narrower) | 500-900 |

  Totals (estimates, not measurements): core (L16-0..D) 4,900-9,100 Lean lines,
  plus 400-800 if L:uniform-mean-tensor takes the Gaussian route, plus 500-900
  for the optional E. For comparison, L15 estimated 1,400-2,400 lines and
  produced 2,234. Agent time: at L15's measured pace (UM-0/UM-1, 795 + 326
  lines, and UM-2, 633 lines, each in about 30 min) the core is a few hours of
  agent time. The analytic gaps below make that pace unlikely for B1 and C, so
  I estimate 1-2 days of wall time for the build with 4 agents in parallel,
  including integration. Add about one day for the gate: two receipt tiers of
  about 1 h 10 min each at L15 (longer with more claims), the Easley replay,
  and 2-3 review and repair rounds. Total 2.5-4 days. Labelled results
  expected to move from not formalized: up to 8 (`L:cameron-fractional-products`,
  `P:cameron-spatial-map`, `P:cutoff-singular-values`, `P:cameron-temporal-map`,
  `P:cameron-full-mean`, `L:uniform-mean-cutoff`, `L:uniform-mean-tensor`,
  `P:uniform-mean-regulator`), plus `L:translated-covariance-CS` if E runs. One
  result is expected to upgrade: `L:positive-raw-embedding`.

  **Where Mathlib (pin `56a0058`) lacks something, and the fallback.**
  1. Compactness of integral operators with an L^2 kernel: Mathlib has no
     Hilbert-Schmidt class, no Rellich-Kondrachov and no compactness for
     cutoff multipliers. It does have `isCompactOperator_of_tendsto` and closed
     compact operators. B1 builds the L^2-kernel lemma (the main risk).
     Fallback: the true named input `CutoffCompact` (the compactness sentence
     of `P:cutoff-singular-values`). `P:cameron-spatial-map` then becomes
     inputs-supplied. `L:positive-raw-embedding` is unaffected (decoupled).
  2. There is no spectral theorem for compact self-adjoint operators in
     infinite dimension, and nothing says the square root of a compact
     positive operator is compact. `CFC.sqrt` exists on the C*-algebra of
     operators. The compactness of the root comes from polynomial approximation
     (Weierstrass on the spectrum, p(0) = 0). Fallback: `TemporalCompact`
     (compactness of C_t into L^r, true), with `P:cameron-temporal-map`
     inputs-supplied.
  3. Young's convolution inequality is absent (only the Hoelder integrand
     bound `eLpNorm_convolution_integrand_le`). The TeX proves the needed case
     by a three-exponent Hoelder argument, which C formalizes directly (risk:
     medium-low). L^p-L^q duality uses the pointwise direction
     `|g|^(r-2) g`, as the TeX does.
  4. No completed Hilbert tensor product exists (`InnerProductSpace/TensorProduct`
     is algebraic). Model choice M5 (H_I as the kernel completion) avoids it
     for U. The projection half of `P:uniform-mean-regulator` (pi_J (x) P_K)
     still needs H_I = H_t (x) H_sp (`L:cameron-supported-tensor`), so it stays
     out (decision 9).
  5. The Gaussian route of `L:uniform-mean-tensor` needs rotation invariance or
     diagonalization of a finite Gaussian sum in a Hilbert space. `gaussianReal`
     and independence exist, and `FiniteGaussianMatrix` diagonalizes Hermitian
     matrices, but the Hilbert-space Gaussian layer is thin. Fallback: the
     kernel-positivity route (decision 5).
  6. Bridge risk in A2: real band-limited L^2 functions must be shown to lie
     in the companion's H^1 model (M6, the weak-gradient graph) with the
     gradient bound. Plancherel on L^2 exists. L15's `testSchwartz` and
     `norm_toH1_sq_le_manuscript` help. Risk: medium.
  Overall risk: medium-high for the compactness fields (B1, C), medium for A2,
  low for A1 and D. The most likely bad outcome is that the core lands with one
  or two narrow compactness inputs, while `L:positive-raw-embedding` is still
  whole.

  **Gate (as L15, with its lessons).** Local compile on <MACHINE> first; an Easley
  stage-2 pre-gate replay of the integration commit (new modules only). At the
  gate commit: claims synced, then the scratch-registry `gate --check`
  BEFORE the receipts are cut (and again after every docs-only commit);
  lower-tier receipt and comparator receipt; COMPLETION.md regenerated
  (milestone `L16-gate`); coverage rows and statement-ledger rows, with
  named-input entries for any fallback, citing per field the TeX lines
  (statement or proof) that establish it (L15 note N3.1-N3.3). Instance rule:
  every instance in a claimed module is named. A lint finds zero anonymous
  `instance :` in the new modules before claims sync; L15 dropped nine claims
  that named Lean-generated instances. Easley `leanchecker --fresh` of the
  new modules plus default mode over all modules. Correspondence review:
  statement scopes by DeepSeek V4 Pro (tool-denied, one attempt per scope,
  SessionRetry disclosed), with packets split to fit (L15 scope 4: 134 KB
  packet, three NO_REPORT at the 32000-token output cap) or with a raised
  output cap. Documentation scopes (ledger, coverage, COMPLETION, counts) by
  GPT-6.2-Sol via Codex (own codex-home, effort high), as Le chose for L15
  scope 4. Confirmation rounds use the same route; at most two repair rounds.
  The gate record goes on a held lean-progress branch while #16's book-origin
  freeze holds. <HUB> is synced after every push. Le closes the gate; tag
  `L16-gate`.

  Decisions for Le (defaults in brackets):
  1. Scope: (a) the core L16-0..D plus R1; (b) also the optional E
     (`L:translated-covariance-CS`); (c) also `L:uniform-mean-spatial-tails`.
     [(a); E only if an agent is idle after its core item]
  2. Other candidates: C8-C10 beyond F1 stay frozen. They shrink the input
     lists of `C:static-interaction` and `P:static-phase-all-orders` and change
     no class; `CPInputs` is the imported Crouzeix-Palencia theorem, which
     Mathlib lacks. `L:pairing-product-envelope` (150 TeX lines of diagram
     induction on the L13 `DiagramModel`, est. 1,500-3,000 lines, high risk)
     goes to a later wave with `L:translated-covariance-CS` as its first item.
     D1, D5 and K9 stay out. [yes]
  3. Anchor: new L16 citations to 1.1.0 (`0788ddee`, public SHA when released),
     and L15's citations re-anchored to 1.1.0 in R1; if 1.1.0 is not public
     at the docs freeze, cite c3c2431d (= v1.0.3 for these files) and
     re-anchor at the release. The rest of the companion stays on R
     `39f2597a` until the next release re-anchor. [yes]
  4. Host and agents: Office, 4 agents in worktrees (A: A1, A2; B: B1, B2;
     C: C; D: D, starting against the frozen signatures as UM-2 did with
     `UM0Facts`), `office-build.sh` (8G cap, `LEAN_NUM_THREADS` <= 8); local
     compile first; Easley via <MACHINE> only for the gate replay; Mathlib pin
     unchanged. [yes]
  5. Route for ||U|| <= ||C_t||: try the TeX's Gaussian route for
     `L:uniform-mean-tensor` (general A); if it is not done when B and C land,
     use the kernel-positivity route, disclose it, and leave
     `L:uniform-mean-tensor` not formalized. [yes]
  6. Fallbacks: only true named inputs (`CutoffCompact`, `TemporalCompact`,
     each the exact TeX sentence), never surrogates. `L:positive-raw-embedding`
     is pursued as whole independently of them. [yes]
  7. "Not trace class" in `P:cameron-temporal-map`: Mathlib has no trace
     class, so formalize it as divergence of the finite orthonormal sums
     (cell indicators). For a positive operator that characterizes infinite
     trace, and it is recorded in the model-choice register. [yes]
  8. `P:cameron-spatial-map`: E part only. The F columns, B_F (which needs
     `L:constant-source-response`) and L_F are not formalized, so the result
     is narrower. [yes; F later only if a downstream result needs it]
  9. The projection and tail half of `P:uniform-mean-regulator` and
     `L:uniform-mean-spatial-tails` stay out. They need H_I = H_t (x) H_sp,
     which Mathlib cannot express without a completed tensor product. [out;
     a later-wave candidate]
  10. Review routes: statements by DeepSeek V4 Pro, with split packets or a
      raised output cap; documentation by GPT-6.2-Sol via Codex. [yes]
  11. Release: one companion release v0.11.0 after the L16 gate, covering L15
      and L16, re-anchored to the then-public book release, with receipts,
      Zenodo and `lean-pkg page --site` (2 h 20 min to 2 h 40 min on <MACHINE>).
      This replaces the open L15 v0.11.0 question. The book keeps pinning
      v0.10.0 until a book release re-pins Appendix F. [v0.11.0 after L16; no
      book re-pin by default]
  12. Any manuscript defect L16 finds is recorded and routed to #3 for a book
      patch release (1.1.x). Lean never narrows a statement to hide it. [yes]

  Could not be determined from the records: the exact contents of C8-C10.
  L12's DEBT.md was session scratch and was not found. They are identified
  here from the L12 F1 row and the ledger's remaining inputs of
  `C:static-interaction` and `P:static-phase-all-orders`. Also unknown: whether
  the DeepSeek route can raise its 32000-token output cap, and Office's load at
  launch time. Check it then.
- **WAVE L15: APPROVED by Le (2026-11-19) as proposed, with the default answers to all seven decisions.** Le, verbatim: "I approve L15 as proposed with the default answers to all seven decisions (scope (a) first). Push cc1182dd with the guard, sync <HUB>, then launch L15-UM on <MACHINE>." Scope (a): UM-0..UM-2, one agent; UM-3 is a later follow-up. Launched on <MACHINE> 2026-11-19.
  **L15 interface frozen (2026-11-20)** at dev `06c3c6a` (branch `wave-l15/iface`;
  `UniformMeanInterface.lean`, 480 lines, Office build 0 warnings, no sorry,
  standard axioms; design in the companion's `docs/l15/INTERFACE.md`). Named
  inputs `CameronSpatialMap` and `UniformMeanRegulator` carry only the parts
  of `P:cameron-spatial-map` and `P:uniform-mean-regulator` that UM-1 and UM-2
  use (not the F columns for L_F, the rough-state row, the explicit
  M_0 = A_s M^2, or the regulator's projection and tail half). Le, verbatim
  (2026-11-20): "The scoped named inputs CameronSpatialMap and
  UniformMeanRegulator are acceptable; continue L15 with agents A and B and
  report when both finish." The cold read of the structures against the TeX is
  part of the decision-3 review. Agents A (UM-0, UM-1; `wave-l15/um01`) and B
  (UM-2; `wave-l15/um2`) run in parallel on <MACHINE> (`~/l15wt/um01`, `um2`).
  Three presentation issues found at v1.0.2 (`L:uniform-E-lift` lines 34-36:
  V's defining property only in the proof; `E:uniform-mean-row` lines 15-20:
  rough-state row's support cited only later; the E inner product never
  displayed) were routed to #3 under decision 6; #3's proposals:
  `~/.local/state/Le-AI-Lab/stratonovich-L15-presentation-assessment-20261120/PROPOSED-CHANGES.md`
  (patch queue, Le's word pending).
  **L15 GATE CLOSED by Le (2026-11-20).** Le, verbatim: "Re-run DeepSeek scope 4
  split into 4a and 4b, one attempt each; I accept the extra
  UniformMeanRegulator omission; keep L:positive-raw-embedding as narrower. Then
  close the L15 gate: merge to dev main, tag L15-gate, update COMPLETION.md, and
  record it on a held lean-progress branch." and, after DeepSeek returned no
  report twice more, "Instead of DeepSeek, can you use GPT6.2Sol instead?"; then
  "When DeepSeek scopes 4a and 4b report, adjudicate them, apply any doc repairs,
  then close the L15 gate ... Report the SHAs."
  Lean: four new modules (UniformMeanInterface, UniformMeanFoundation,
  UniformELift, PositiveRawMean; 2234 lines; no sorry, standard axioms):
  `uniform_E_lift_paper` (`L:uniform-E-lift`, nothing supplied; narrower: L_F
  and the complex extension not formalized), `positive_raw_mean_paper`
  (`E:positive-raw-mean` a.e. and the canonical version for a supplied
  `UniformMeanRegulator`), density of real tests in H^(+-1/2) (used, not proved,
  in the book). Gate commit dev `18c5c1d`: lower-tier receipt (0 sorry, 4705
  claims standard axioms) and comparator receipt (1577 + 2226 pass) at
  `4648b3c`; Easley `leanchecker` at `315a332` (4/4 --fresh, 146/146 default;
  no library file changed after it). Reviews: DeepSeek V4 Pro scopes 1-3 (PASS,
  PASS_WITH_NOTES, PASS_WITH_NOTES; one attempt each, no SessionRetry); scope 4
  (documentation): DeepSeek NO_REPORT three times (32000-token client cap spent
  in reasoning), then GPT-6.2-Sol on Le's word: first round FAIL (18 documentation
  findings, all repaired at `48dad18`), confirmation 4a PASS_WITH_NOTES, 4b FAIL
  on one wording overstatement, repaired with the minor notes at `04f6b6a`
  without a further review round. Records: claims 4705 (nine Lean-generated
  instance claims dropped), coverage 102 rows. Merged to dev main `54d3313`
  (gate record, COMPLETION milestone `L15-gate`); tag `L15-gate` on `18c5c1d`.
  Review folder: `~/.local/state/Le-AI-Lab/stratonovich-lean-wave-l15-review/`
  (ADJUDICATION.md).
  **After the gate (2026-11-20, docs only, receipts still bind `18c5c1d`):** two
  GPT-6.2-Sol confirmation attempts on the wording repair `04f6b6a` (Le's word):
  the first FAIL (one MAJOR left partly open, one new MAJOR from the repair: the
  mean typed `L^r(I; K(E))` instead of `L^r(I; L(E))`), repaired at dev main
  `069d88f`; the second INCONCLUSIVE (medium) because its packet lacked two
  passages, with both MAJORs resolved and no new issue; #22 read the two
  undecided passages directly. The last two MINOR wording notes were applied at
  dev main `09d3406` without another model call (Le). Each commit passed the
  scratch-registry `gate --check` as a docs-only descendant of `18c5c1d`. Book issues found by L15: three presentation fixes, accepted
  by Le, released in book 1.1.0.
  Proposal as written (#22, 2026-11-19): Le, verbatim: "Yes, lift
  the freeze for L15-UM only and draft the L15 proposal in
  lean-progress/PROGRESS.md: items, the anchor check against v1.0.2, sizing on
  Office, and the decisions I need to answer." Scope: L15-UM only; C8-C10 and
  `L:pairing-product-envelope` stay frozen.

  **Anchor check against v1.0.2 (original `c3c2431d`, public `a9d147d8`).** The
  three files L15-UM reads are byte-identical in R `39f2597a` and in v1.0.2:
  `integrated_intrinsic_constant.tex`, `integrated_uniform_products.tex` and
  `integrated_uniform_mean.tex` (empty `git diff` R..c3c2431d). The
  `integrated_cameron_mean.tex` file of `P:cameron-spatial-map` is unchanged
  too. The line numbers recorded at the L15 scheduling (a284420) are stale,
  because the readability pass moved them before R. At v1.0.2:
  `L:positive-raw-embedding` statement 23-40, proof 42-130 (`E:positive-raw-mean`
  at 34); `L:uniform-E-lift` 33-65 (`E:uniform-E-pairing` 37);
  `E:uniform-mean-row` 15; `L:uniform-mean-cutoff` 29-61;
  `L:uniform-mean-spatial-tails` 71-177; `L:uniform-mean-tensor` 188-243;
  `P:uniform-mean-regulator` 262-320; `P:cameron-spatial-map`
  (integrated_cameron_mean.tex) 104-140. L15 anchors new citations to v1.0.2
  directly; its proof modules cite v1.0.2 lines. The rest of the companion stays
  on R (the same text) until a full re-anchor (decision 4).

  **What the target needs (read at v1.0.2).** `E:positive-raw-mean` states
  `T_R Psi(s) = B_E(m_R h_(Psi,s))` a.e., where the uniform E mean is
  `T_R(C_t (x) I)`. T_R is the E restriction of `P:cameron-spatial-map` (a
  compact spatial mean map into K(E), E = H^{1/2} x H^{-1/2}), its row is
  `E:uniform-mean-row`, its L^r(I; K(E)) bound (2 < r < 2/a) is
  `P:uniform-mean-regulator`, and B_E is the E operator of `L:uniform-E-lift`.
  None of these five is in the companion (COMPLETION.md: not formalized; no Lean
  file cites them). What exists: L14-K1a `OccupationCompletion` (999 lines; H_t,
  H_I, J_G; both identities of `E:occupation-raw-identities`), K1b
  `SourceHeatGram` (926 lines), `RemoveMask` (85 lines; mask chi(|x|/R)).
  So "close `L:positive-raw-embedding`" needs either the Cameron-map chain or
  named inputs for it (decision 1).

  | Item | Target (v1.0.2 lines) | Deliverable | Class after (fallback) | Size on <MACHINE> |
  |---|---|---|---|---|
  | UM-0 | anchor and objects | L15 citations at v1.0.2; E = H^{1/2} x H^{-1/2} on the companion's Bessel-potential spaces (L13 K5 layer); the cutoff eta, eta_R, m_R = eta_R^2, and the identification with `RemoveMask.mask` where the TeX needs it | infrastructure | 1 agent, about 0.5 day, 300-500 Lean lines |
  | UM-1 | `E:uniform-mean-row` (15), `L:uniform-E-lift` (33-65) | T_R defined through its explicit row k_R(z,w) = (eta_R z_1)(eta_R Lambda^{-1} w_2); B_E(V)(u,v) = (0, Vu) and the pairing bound `E:uniform-E-pairing` | `L:uniform-E-lift`: whole for the operator form and the pairing bound; the lift L_F into the signed-static class narrower (it needs that class) | 1 agent, about 1 day, 500-900 lines |
  | UM-2 | `E:positive-raw-mean` (34), canonical-version sentence (38-39), proof 42-130 | the a.e. identity T_R Psi(s) = B_E(m_R h_(Psi,s)) and the canonical version for smooth Psi, from K1a's H_I and J_G | `L:positive-raw-embedding`: whole if decision 1 is (b); inputs-supplied with named `CameronSpatialMap` and `UniformMeanRegulator` if (a) | 1 agent, about 1-1.5 days, 600-1000 lines |
  | UM-3 (only with decision 1 (b)) | `P:cameron-spatial-map` (104-140), `L:uniform-mean-cutoff` (29-61), `L:uniform-mean-spatial-tails` (71-177), `L:uniform-mean-tensor` (188-243), `P:uniform-mean-regulator` (262-320) | compactness of the spatial mean map into K(E), uniform multiplier and tail bounds, the Hilbert tensor extension, the L^r(I; K(E)) bound | each whole or narrower with named inputs; four labelled results move from not formalized | 2 agents in parallel, 3-5 days, 2500-4000 lines; Easley replay of the new modules |

  Totals: decision 1 (a): UM-0..UM-2, one agent, 2.5-3 days, about 1400-2400
  Lean lines. Decision 1 (b): add UM-3, a second agent, about 6-8 days in all,
  about 4000-6500 lines. Office has 36 cores and 62 GB; each agent builds with
  `LEAN_NUM_THREADS` at most 8 (two agents fit), locally first; Easley (via
  Office) only for the gate replay. Line counts are estimates from the TeX
  length (`L:positive-raw-embedding` 107 TeX lines; the UM-3 chain 292) and the
  sizes of L13/L14 modules of similar kind, not measurements.

  Gate as L12-L14: lower-tier receipt and comparator receipt at the gate commit,
  claims synced, COMPLETION.md regenerated, statement-ledger rows and their
  correspondence review, Easley `leanchecker --fresh` replay of the new modules,
  Le closes the gate.

  Decisions for Le (defaults in brackets):
  1. Scope of the mean identity: (a) UM-0..UM-2 with `P:cameron-spatial-map` and
     `P:uniform-mean-regulator` entering as named inputs, so
     `L:positive-raw-embedding` becomes inputs-supplied, not whole; or (b) also
     UM-3, so it can become whole and four more labelled results are
     formalized. [(a) first; (b) as a follow-up wave if (a) shows no defect]
  2. Host and agents: Office, one agent for (a), two for (b); local compile
     first, Easley via <MACHINE> only for the gate replay. [yes]
  3. Correspondence review of the new ledger rows: DeepSeek V4 Pro (the
     designated main reviewer), tool-denied, one attempt per scope, with any
     OpenCode SessionRetry disclosed as under Choice B. [yes]
  4. Anchor: new L15 citations to v1.0.2; the rest of the companion stays on R
     (same text) until the next release, when the whole companion is
     re-anchored to the then-current book release with the reviewed tool. [yes]
  5. Release: after the gate, companion v0.11.0 (tag, GitHub release, Zenodo
     version DOI), docs-only notes as usual. The book keeps pinning v0.10.0
     until a book release re-pins Appendix F. [v0.11.0 after the gate; no book
     re-pin]
  6. A manuscript defect found by L15: record it and route the repair to #3 as a
     book patch release (1.0.x), as for the earlier waves; Lean never narrows a
     statement to hide it. [yes]
  7. Mask identification: if `RemoveMask.mask` chi(|x|/R) and m_R = eta(./R)^2
     differ where the TeX needs one, use m_R in the new modules and record the
     relation, without changing the L14 modules. [yes]
- **EASLEY STAGE 2 APPROVED (Le, 2026-11-12).** Le, verbatim: "I approve
  Easley stage 2: pilot lower-tier receipts via lean-pkg receipt slurm at the
  L9 gate (compare with a local receipt at the same commit) and run pre-gate
  replays of integration commits (new modules only)." (1) At the L9 gate
  commit, cut the lower-tier receipt twice: `lean-pkg receipt systemd` on
  <MACHINE> as before AND `lean-pkg receipt slurm` from an Easley job (template
  and `--check` preflight first; job sized from the measured local receipt:
  37-41 min, 9.5-10.1 GiB peak); compare the two (claim-axioms count, sorry
  count, axiom sets per claim, build log) and record the comparison; only
  after a matching pilot may later gates use the Slurm receipt alone.
  Comparator receipts stay local (no bwrap/Landlock on Easley). (2) Pre-gate
  replays: after each integration commit is built locally and pushed, an
  Easley array replays `--fresh` only the modules new or changed since the
  last replayed gate (`make-inputs.sh ... new:<BASE>`, plus umbrella and
  Axioms), with the usual pilot task first; the full gate array still runs
  at the gate commit. Easley stays gates and measured heavy work only, never
  an edit-compile loop. Stage 1 (array at every gate) continues; stage 3
  (overlapping arrays, <= ~600 CPUs) waits for two clean stage-2 runs.
- **L12 a284420-ONLY ITEMS DONE (2026-11-12), each independently verified
  (build, refutations, Audit, standard axioms only) and pushed.** TW
  (`50a9687`, Office): L:terminal-wick whole for the constructed chain
  measures (partial-sum and full-series comparison for real r; absolute L^2
  convergence for complex r, the TeX's only complex-r claim; the complex-r
  comparison is false and refuted). C1 (`ce98a8a`, `f99ff58`, <MACHINE>):
  spectral identification of the smoothed covariance p_eps * Gamma by Fubini
  against Lebesgue x mu, plus uniqueness of the tempered spectral measure
  (Gaussian charFun + Measure.ext_of_charFun): L:damped-homogeneous-norms
  whole, nothing supplied (p_eps * Gamma modelled by its density, a register
  entry). SRC (`1bf6302`, <MACHINE>): L:source-finite-comparison and
  L:tube-half-action whole; P:tube-rayleigh-transfer every conclusion on two
  TRUE named inputs from L:tube-closed-geometry (TubeAttained, TubeTail; the
  plan named only TubeTail; accepted under the true-named-input default).
  F1 (`188405f`, Office): FockSandwich discharged on K2's Fourier-side model
  (PiLp Fock layer, CFC sqrt and inverse root with explicit IsUnit, band
  projection); C:static-interaction and P:static-phase-all-orders re-issued
  without it, still narrower (CPInputs, PropagatorBlock and the rest).
  Wording note for Le (manuscript, not acted on): "all finite partial-order
  second moments" in L:terminal-wick could say "mixed moments E[Y_m Y_n],
  hence the partial-sum second moments for real r". L13 items started on free
  slots: DM0 (Office, interface first), C4, C6, C5 (<MACHINE>).
- **FIRST EASLEY PRE-GATE REPLAY PASSED (stage 2, 2026-11-12).** At the L10
  integration commit `f0b795f` (built on <MACHINE>, pushed): `make-inputs.sh
  new:aff7409` selected the 21 targets new since the last replayed gate (the
  12 L9 modules, the 8 L10 modules, the umbrella and Axioms) out of 111
  modules; build 5694096, pilot 5694097, then the rest; collect.py
  VERDICT=COMPLETE, all 23 jobs COMPLETED. No kernel problem in the L9/L10
  modules ahead of their gates. Evidence stays in the Easley run directory
  and session scratch (pre-gate replays are not gate evidence; the full array
  runs again at each gate commit). Found and fixed on the way: the harness's
  `submit.sh rest` exited silently (pipefail on the not-yet-existing pilot
  log) before the pilot started; fixed in the Le-AI-Lab skill copy
  (`94168e1`) and the session copy.
- **INDEX AS A POINTER TABLE (Le, 2026-11-12).** After six L9 re-review
  rounds whose remaining findings all came from the Index-by-label table
  (round 6 at `a723987`: 1 fatal, 40 major, all per-row captions and input
  lists; headings, coverage, counts and the L8 repairs already pass), Le chose
  to make the Index a lookup only: each row maps a label to the module
  section(s) that formalize it, with that section's category word (whole
  result / narrower result / foundation / proof steps) and no per-declaration
  qualifiers or input lists. Per-declaration statements and supplied inputs
  are stated once, in the section tables. The Index is generated by script
  from claims.yaml and the section headings; the checker verifies that every
  label maps and every category equals its section's. This supersedes the
  per-cell qualifier part of the every-cell rule below (category words stay).
  Round-6 findings about specific declarations are applied to the section
  tables wherever the same wording appears there.
- **INDEX-CELL RULE: EVERY CELL (Le, 2026-11-12).** Chosen by Le after the
  L9 re-review round 4 at `e2c50b5` (about 224 of ~395 Index first cells carry
  no category word). Every Index-by-label first cell starts with one of
  "whole result", "narrower result: ...", "foundation: ..." or "proof steps:
  ...", derived from its section's heading with per-row overrides where a
  row's declarations differ; mixed rows (declarations with and without
  supplied inputs, or of different categories) are split; a script check
  enforces the category word on every cell. Applied together with the split
  modelled-object rule as decided earlier, which by its own terms also makes
  RadiusMeanAnchor (abstract random paths M for M_R(Y_m)) and TypeContinuity's
  two moment results (an abstract moment function for log E u^p) narrower
  (missing constructions, not registered model choices).
- **EASLEY L8 ARRAY REPLAY PASSED (2026-11-12).** First full run of the
  L11 array harness, at the L8 gate `aff7409`: build 5692847 (12 min),
  pilot 5692848, then array 5692933 (task 0 default mode + 91 targets).
  collect.py VERDICT=COMPLETE: 92/92 `--fresh` and default mode 92/92, all
  94 jobs COMPLETED 0:0 on the first attempt; no sorryAx; checker and Mathlib
  pins as in L5-L7. Wall time 1 h 31 min from the first submission (52 min
  from the release of the rest), vs 4 h for L7's 10 targets in one job.
  Per `--fresh` task median 48 min, peak RSS 7.7 GiB, cgroup peak 22.5 GB
  (task 0: 29.5 GB of 36G); file-nr max 62,880, guard never waited; 123
  core-hours allocated, 53 CPU-hours used (median 43% of 2 cores, so 2 CPUs
  per task is not undersized). Every library module through wave L8 has now
  passed a `--fresh` replay. Evidence `verification/leanchecker-easley-wave-l8/`
  on companion main `d9ded8f` (docs-only; ledger READY). Lesson: my own
  watcher missed REPLAY_STARTED (a quoting bug); the release went through the
  harness's own `submit.sh rest` check, which is the gate to rely on.
- **MODELLED-OBJECT RULE: SPLIT (Le, 2026-11-12).** Chosen by Le from three
  options after the L9 strict-heading re-check at `d5667f5` flagged six
  whole-result headings. A documented definitional model choice that is the
  standard construction keeps a result "whole", with the model named in a
  model-choice register in the ledger Scope: the d = 3 wave Green measure
  built from `volume.toSphere` (L6 decision 4), so L9Completed,
  LowAlphaConvolution and PhaseContractions stay whole. A missing construction
  makes a result "narrower": QuotientObstruction (the noise W is not
  constructed; covariance functional only), IndexedCone (abstract
  GroundFamily, link to the wave family by documentation only) and
  `L:uniform-series-tail` at L8 (chain measures fixed only by their mass; the
  L11 constructed-measure version can be whole). Their coverage rows move to
  conclusion weaker (rows of gated waves L3, L6 and L8 change class by this
  decision; counts recomputed).
- **"WHOLE RESULT" HEADING CONVENTION: STRICT (Le, 2026-11-12).** Le,
  verbatim: "I approve the strict meaning of \"whole result\" for the L9
  headings; finish the renames, re-run the r2 heading check, and record the
  convention in lean-progress/PROGRESS.md." Prompted by the L9 narrow
  re-confirmation at companion `ba6c565` (r2 audit of all 56 remaining
  "(whole result)" headings: 20 FAIL, 8 INCONCLUSIVE; the companion had used
  the heading also for narrower results and for foundation modules). The
  convention, for every ledger section heading and Index first cell (all
  waves, not only L9): (A) "(whole result)" only when every conclusion of the
  labelled result is a Lean conclusion under the manuscript's hypotheses,
  possibly with named, disclosed supplied inputs (coverage class
  same-assumptions/full or inputs-supplied/full); (B) "(narrower result:
  <what is missing>)" for same-assumptions/weaker rows and other partial but
  labelled results; (C) "(foundation)" or "(proof steps of <label>)" for
  modules proving facts that a result uses. FORMALIZATION.md, the ledger
  Scope and the README counts use these three categories. Docs only: no Lean
  change, and coverage classes change only if a row is found inconsistent
  (to be reported, not silently changed). Renames and the r2 re-run on
  branch `wave-l9/repair`.
- **L8 RECEIPTS AND THE EASLEY L7 REPLAY (2026-11-12).** Receipts at the
  L8 gate commit `aff7409`, committed as `d476e17`: comparator PASS over all
  1747 theorem claims; lower tier 0 sorry, standard axioms only, axioms of
  all 2108 claims (runtime 37 min, peak 9.5 GiB); claims ledger READY (1342
  required, 2058 verified, 0 open). Docs-only successor `27d22a1` (README:
  Le's L8 acceptance and the verification record at `aff7409`; COMPLETION.md:
  `L8-gate` milestone row) sent to #24 for Appendix F. Easley job 5692712
  (`leanchecker --fresh` at the L7 gate `f3be834`): 10/10 PASS (eight wave-L7
  modules, umbrella, Axioms), default mode 81/81, no sorryAx; closure and
  replay-coverage checks: every library module through wave L7 has passed a
  `--fresh` replay (evidence `verification/leanchecker-easley-wave-l7/`,
  companion `ff40157`, docs-only; SHA sent to #24). The wave-L8 array at
  `aff7409` (build and pilot PASS) is running.
- **WAVES L13 AND L14 CORRESPONDENCE GATES: CLOSED (Le, 2026-11-13)** at
  companion `8f51004` (the merge of `wave-l14/stack` into dev main) over
  manuscript `a284420`; annotated tags `L13-gate` and `L14-gate` (private
  development repository). Le, verbatim: "I accept the wave-L13/L14
  correspondence reviews and the confirmation (PASS/high at f7cf727) as
  closing the Lean wave L13 and L14 correspondence gates at companion
  8f51004 over manuscript a284420." Evidence: twelve Codex GPT-6.1-Sol
  packets at `f74d825` (documentation findings only, no Lean error; scratch
  l1314rev), repairs A-R with Le's decision F (ResolventForm narrower,
  coverage row P:signed-closed-form) and the L12 re-merge, confirmation
  PASS/high on all twelve packets at `f7cf727` (round 2 plus one narrow
  re-check; scratch l1314rev-conf); comparator extended to all 3654 theorem
  claims (`11511b4`; CheckFidelity 3654/3654, 0 problems; the checker now
  skips `C.congr_simp` lemmas that simp realizes for non-project constants,
  reviewed and accepted). Le's L13/L14 decisions: M4, M5, M6;
  L:occupation-rayleigh-selection and L:occupation-raw-square narrower;
  MaskedAuxiliaryReal whole with the Frechet reading; L:plane-endpoints
  whole; FirstMomentSeries and SignedMultiplierForm true named inputs. At
  closure the receipts at `8f51004` (unit verify-l1314) were running and the
  Easley array not yet run; the README and COMPLETION gate record on dev main
  follows them. Package: 4504 claims (3654 theorems, 850 definitions; 962
  public definitions, 112 unlisted); coverage 101 rows (48 same/full, 16
  same/narrower, 1 inputs/full, 34 inputs/narrower, 2 outside); COMPLETION
  44 / 16 / 1 / 34 / 2 / 123 of 220. Board `74ea688`. With this the LEAN
  FREEZE is reached (Le, 2026-11-13): no further Lean waves; remaining are
  HYG and the re-anchor before v1.0.0, and the public releases.
- **WAVE L12 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-13)** at companion
  `56fc59e` (the merge of `wave-l12/int` into dev main) over manuscript
  `a284420`; annotated tag `L12-gate` (private development repository). Le,
  verbatim: "I accept the wave-L12 correspondence reviews and the
  confirmation (PASS/high at 0e1e687) as closing the Lean wave L12
  correspondence gate over manuscript a284420, with M3 recorded." Le named
  no commit; the gate commit is the merge `56fc59e` (tree of `wave-l12/int`
  after merging main `eb43105`; Lean sources identical to `0e1e687`).
  Evidence: correspondence reviews at `3c3664c` (documentation findings
  only, no Lean error; scratch l12rev), repairs and the L11 re-merge
  (`9073709`, `7087542`, `0e1e687`), confirmation PASS/PASS_WITH_NOTES high
  on all six packets at `0e1e687` (scratch l12rev-conf). Recorded: register
  entry M3 (accepted 2026-11-13). At closure the receipts at `56fc59e` (unit
  verify-l12) were running and the Easley array not yet run; the README and
  COMPLETION gate record on dev main follows them. Content: L:terminal-wick
  whole for the constructed chain measures (complex-r comparison false,
  refuted; full-series comparison a Lean-side corollary);
  L:damped-homogeneous-norms whole (M1, M3); L:source-finite-comparison,
  L:tube-half-action whole; P:tube-rayleigh-transfer every conclusion on
  true named inputs TubeAttained, TubeTail; FockSandwich proved on K2's
  model (C:static-interaction, P:static-phase-all-orders still narrower;
  model wrappers assume an orthonormal family of every size, so mu != 0).
  Package: 3107 claims (2541 theorems, 566 definitions; 678 public
  definitions, 112 unlisted); coverage 85 rows (37 same/full, 19
  same/narrower, 1 inputs/full, 26 inputs/narrower, 2 outside); COMPLETION
  33 / 19 / 1 / 26 / 2 / 139 of 220. Board `e3d8b83`; <HUB> synced; #16,
  #3, #24 told. Not in the public v0.9.0.
- **WAVE L11 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-13)** at companion
  `b780f10` over manuscript `a284420`; annotated tag `L11-gate` (private
  development repository). Le, verbatim: "I accept the wave-L11
  correspondence reviews and the confirmation (PASS/high at c2acf53) as
  closing the Lean wave L11 correspondence gate at companion b780f10 over
  manuscript a284420." Evidence: eight Codex GPT-6.1-Sol correspondence
  reviews at `6277695` (documentation findings only, no Lean error; scratch
  l11rev), repairs with the merge of the L10 repairs (`56b844b`, `1626776`,
  `c2acf53`), confirmation round PASS/high on all packets at `c2acf53`
  (scratch l11rev-conf). Le's L11 decisions (2026-11-13): register entry M2;
  L:fock-form and L:interval-contractions same-assumptions narrower; both
  Index pointer presentations kept. Merge into main `b780f10` (main `d6a0505`
  merged into L11 at `38f87cd`); receipts `abb3479` (comparator PASS over
  2423 theorem claims; lower tier 0 sorry, 2955 claims, standard axioms only;
  ledger READY: 1886 required, 2896 verified, 59 out-of-scope); Easley array
  116/116 `--fresh` plus default mode via <MACHINE> (evidence `08b00bc`).
  Content: L:finite-word-cutoff whole for several modes per color (M2),
  removing hQ in `interval_coefficient_assembly_paper_words` (DuhamelWords
  supplied; FixedSplit's own wrapper still takes hQ); L:uniform-series-tail
  whole and L:terminal-wick same-assumptions narrower for the constructed
  chain measures; Fock-form spatial column bound on the Fourier-side model;
  static interaction bounds with fewer supplied inputs; Green-regularization
  mass and convergence facts (whole-chain identification not formalized).
  Package at the gate: 2955 claims (2423 theorems, 532 definitions; 644
  public definitions, 112 unlisted); coverage 82 rows: 54 same-assumptions
  (33 full, 21 narrower), 26 inputs-supplied, 2 outside; COMPLETION 29 / 21
  / 0 / 26 / 2 / 142 of 220. Records: companion docs successor `eb43105`,
  board `6680cf5`, STATUS-DIGEST; <HUB> synced; #16, #3, #24 told. Not in
  the public release v0.9.0 (L9 state); goes into the next minor release.
- **WAVE L10 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-13)** at companion
  `b2bf7a9` over manuscript `a284420`; annotated tag `L10-gate` (pushed to the
  private development repository `stratonovich-ham-second-moment-lean-dev`).
  Le, verbatim: "I accept the wave-L10 correspondence reviews, the
  confirmation and the re-confirmation (PASS/high at 0904978) as closing the
  Lean wave L10 correspondence gate at companion b2bf7a9 over manuscript
  a284420, with hQ recorded as accepted for now." Evidence: eight Codex
  GPT-6.1-Sol correspondence reviews at `aac74b5` (documentation findings
  only, no Lean error), repairs `ab37d40`, `b3f773e`, `0904978`;
  confirmation at `b3f773e` (5 of 6 PASS/PASS_WITH_NOTES, high); one-check
  re-confirmation PASS/high 3/3 at `0904978` (evidence in scratch l10rev,
  l10rev-conf, l10rev-conf2; to be copied to reviews/ with the L11 evidence).
  Merge into main `b2bf7a9` (Lean, lakefile, manifest and toolchain identical
  to `0904978`; its subject says "21 modules", wrongly: wave L10 adds 8);
  receipts `c622c25` (comparator PASS over 2268 theorem claims; lower tier 0
  sorry, 2757 claims, standard axioms only; ledger READY: 1764 required,
  2706 verified, 51 out-of-scope); Easley array 111/111 `--fresh` plus
  default mode via <MACHINE>; second stage-2 Slurm receipt identical to the
  local one (evidence `df64d3e`). Recorded with the gate: hQ, the added
  hypothesis on the cutoff coefficients of the fixed-split assembly, is
  accepted for now (L11-K10 removes it in a new wrapper). Earlier L10
  decisions: the 5 VariationalMean lost-disclosure flags are a checker false
  positive; HigherRieszTwo is headed narrower. Content: L:higher-riesz in
  full for d = 2, 3 (optimal constant in d = 3; M1); L:alpha-one-convolution
  from H:homog alone; white-noise model and white moment bounds for S_2^pos
  (spatial energy supplied, B9); fixed split (core and Fock assembly).
  Package at the gate: 2757 claims (2268 theorems, 489 definitions; 97
  unlisted public definitions, 586 in all); coverage 82 rows: 49
  same-assumptions (31 full, 18 narrower), 31 inputs-supplied, 2 outside;
  COMPLETION 27 / 18 / 0 / 31 / 2 / 142 of 220. Records: companion docs
  successor `d6a0505` (README acceptance and verification record,
  COMPLETION L10-gate row), board `4bacc80`, STATUS-DIGEST; <HUB>
  synced; #16, #3 and #24 told.
- **WAVE L9 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-12)** at companion
  `6eb79c7` over manuscript `a284420`; annotated tag `L9-gate` (pushed). Le,
  verbatim: "I accept the wave-L9 correspondence reviews, the ten
  confirmation rounds and the final one-check confirmation (PASS/high at
  ff40fde) as closing the Lean wave L9 correspondence gate at companion
  6eb79c7 over manuscript a284420, with the public-definition count
  correction as its docs-only successor." Evidence: eight Codex GPT-6.1-Sol
  correspondence reviews at `eb253a5`, ten confirmation rounds with
  documentation repairs (the strict whole-result convention, the split
  modelled-object rule with the model-choice register, the pointer Index and
  the labelling convention, all decided by Le), final one-check confirmation
  PASS/high at `ff40fde` (Article `fdc863cc`, reviews/2026-11-12-lean-wave-l9-*;
  adjudication in reviews/.../ADJUDICATION.md); no Lean error found. Merged
  into main at `6eb79c7`; receipts `bb79f83` (comparator PASS over 2050
  theorem claims; lower tier 0 sorry, 2468 claim-axiom lines, standard axioms
  only); regate; claims ledger READY (1570 required, 2417 verified, 51
  out-of-scope). Easley array at `6eb79c7` 103/103 `--fresh` plus default
  mode; D8 pilot task PASS; stage-2 Slurm lower-tier receipt identical to the
  local receipt claim by claim (companion `63ec3be`). Content: low-alpha
  convolution (d = 1, 2, 3) and phase contractions (d = 3) with nothing
  supplied; wave Green Fourier identities (the Green part of
  L:damped-homogeneous-norms in d = 1, 2, 3); complex phase scalar steps;
  exact occupation ceiling C_occ (T:intrinsic-occupation-ceiling still
  narrower: C_2 sentence, class O by joint representatives); Gaussian
  Hermite polynomials, Fock layer, Fock form (FockColumn supplied in the
  abstract wrappers); L:finite-word-cutoff for one mode per color. Package
  at the gate: 2468 claims (2050 theorems); coverage 80 rows: 47
  same-assumptions, 30 inputs-supplied, 3 outside; COMPLETION 25 / 18 / 0 /
  30 / 3 / 144 of 220. Records: companion docs successor `f8c9da0` (README
  acceptance and verification record, COMPLETION L9-gate row), board
  `628a62a`, STATUS-DIGEST; <HUB> synced; #16, #3 and #24 told. Pending:
  the docs-only public-definition count correction (approved), as a further
  successor.
- **WAVE L8 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-12)** at companion
  `aff7409` over manuscript `a284420`; annotated tag `L8-gate` (pushed). Le,
  verbatim: "I accept the six wave-L8 reviews, the two repair rounds, the
  confirmation and the re-confirmation (PASS/high at 168b3c0) as closing the
  Lean wave L8 correspondence gate at companion aff7409 over manuscript
  a284420, with L8-f's mass-supplied chain measures and hK as an added
  restriction recorded." Evidence: six Codex GPT-6.1-Sol groups at `3518233`
  (g2, g3, g5b PASS_WITH_NOTES; g1, g4, g6a-c FAIL on documentation, no Lean
  error), repairs `aeaccf6`, `7af916a`, `bd1c439`; confirmation at `bd1c439`
  (every original finding resolved; two remaining), repairs `5868223`,
  `168b3c0`; re-confirmation PASS/high, 24/24, at `168b3c0`
  (Article `9c0df47`, reviews/2026-11-12-lean-wave-l8-*; adjudication in each
  ADJUDICATION.md). Recorded with the gate: (1) L8-f's chain measures enter
  through their mass (`hmass`, supplied; constructed with the mass proved in
  L11-K4); (2) TerminalWick's `hK`, global measurability of the covariance,
  is an added restriction not in the manuscript (L11-K4 removes it for the
  constructed chain measures); (3) FreeWaveData's non-vacuity is shown on
  L²(R^d) with S = 1, R = 1 and translations, not for the free wave group.
  Content: nine items (spectral mass identity R_alpha = R_Gamma(1);
  damped multiplier lower bounds; space-time positivity; finite occupation
  ceiling with K_0 R_sp; spatial bracket; mask removal; finite and terminal
  Wick; symplectic free group; static phase Cauchy-Schwarz) and
  L8Completed (`S1Bdd` proved with nothing supplied). Package at the gate:
  2108 claims (1747 theorems, 361 definitions; 1122 labelled, 986
  unlabelled); coverage 71 rows: 43 same-assumptions (28 full, 15 narrower),
  25 inputs-supplied (5 full, 20 narrower), 3 outside; COMPLETION 24 full,
  15 narrower, 5, 20, 3 outside, 153 not formalized of 220. Le's
  T:intrinsic-occupation-ceiling decision (same-assumptions, narrower with
  K_0 R_sp) passed review. Receipts at `3518233` PASS (comparator 1747,
  lower tier 2108 claim axioms, 0 sorry; `4e4d173`, historical); final
  receipts at `aff7409` running; the Easley array replay at `aff7409`
  follows. Scope: AI statement-to-manuscript correspondence, **not human
  verification**; supplied inputs stay outside Lean; later changes need a
  successor review.
- **L13/L14 REVIEW ROUND 1 AND DECISION F (2026-11-13).** Twelve Codex
  GPT-6.1-Sol packets at `wave-l14/stack` `f74d825` (scratch l1314rev): all
  FAIL at high confidence on documentation only (no Lean error, no false
  whole/full claim; all 24 new and changed coverage rows pass their checks;
  counts and merge preservation confirmed); repairs A-R accepted. Decision
  F (Le, answer of 2026-11-13: "Narrower + new row"): ResolventForm (K5b) is
  headed "narrower result" and `P:signed-closed-form` gets a coverage row
  (form bounds E:signed-form-bounds, the form version of A >= 1 and the
  Cauchy-Schwarz step, with E:signed-multiplier-form carried as
  SignedMultiplierForm; missing: H_V itself, D(A^1/2) = H^1,
  E:signed-quarter-phase, the H^-1/2 completion, conjugation,
  L:signed-limiting-multiplier). Repairs and a confirmation round running.
- **L13/L14 DOCS DECISIONS (Le, 2026-11-13).** Le, verbatim: "I accept M4,
  M5 and M6 as model-choice register entries, L:occupation-rayleigh-selection
  and L:occupation-raw-square as narrower, MaskedAuxiliaryReal headed whole
  with the Fréchet reading, L:plane-endpoints as whole, and FirstMomentSeries
  and SignedMultiplierForm as true named inputs; record it in
  lean-progress/PROGRESS.md and start the L13/L14 correspondence reviews."
  On `wave-l14/stack` `f74d825`: (1) register entries M4 (the two-chain
  diagram model `DiagramModel`: statements about diagram integrals whole,
  about u and X_n narrower via `MixedMoment`), M5 (the `Lp` completions
  `HK`/`Ht`/`Hsp`/`HI`/`HGamma` of the occupation layer, no tensor
  identification and no `Hsp`/`HGamma` isometry), M6 (`H^1` as the
  weak-gradient graph `ClassOH1.H1R`); (2) `L:occupation-rayleigh-selection`
  narrower (rate in Rayleigh form, cost in integral form) and
  `L:occupation-raw-square` narrower (stated for joint representatives;
  whole would need a composition with ClassOBridge, not done under the
  freeze); (3) MaskedAuxiliaryReal headed "whole result" (whole rests on two
  wrappers together) and `L:variational-global-mean` read with iterated
  Fréchet derivatives; (4) `L:plane-endpoints` whole (V_low = c/pi for the
  exhibited spectral measure); (5) `FirstMomentSeries` (TeX 620, 4949-4950)
  and `SignedMultiplierForm` (E:signed-multiplier-form) are true named
  inputs, listed with the other supplied inputs. L13/L14 correspondence
  reviews started.
- **M3 ACCEPTED (Le, 2026-11-13).** Le, verbatim: "I accept M3 as a
  model-choice register entry (p_eps * Gamma modelled by its density
  gamma_eps), so L:damped-homogeneous-norms counts as whole; record it in
  lean-progress/PROGRESS.md." Register entry M3 (wave L12, `DampedSmoothing`):
  the smoothed covariance p_eps * Gamma of `L:damped-homogeneous-norms` is the
  measure with Lebesgue density gamma_eps (`DampedSmoothing.smoothedCov`); its
  identification with Mathlib's `Measure.conv` of N(0, eps I) and Gamma is not
  proved. With M1 and M3, `L:damped-homogeneous-norms` counts as a whole
  result (same-assumptions/full) on `wave-l12/int` `3c3664c`; the L12
  documentation's "not yet accepted by the author" wording for M3 is updated
  at the L12 repairs.
- **ALL FROZEN ITEMS INTEGRATED (2026-11-13).** Lean-only stacked branch
  `wave-l14/stack` `b2d0a8b` = L11 int `6277695` + L12 (`cfc0285`: TW, C1,
  SRC, F1) + L13 (`ef183d1`: DM0, DM0b, D1-D4, D6, C4-C6, K5a, K5b) + L14
  (`aa17344`: K1a, K1b, 3D, 3Dpd, O). Office: full build 9190 jobs, 0
  warnings; 4822 `#print axioms` lines, standard axioms only; 509/509
  refutation and Audit files compile. Duplicates reported for HYG (not
  refactored): `FockColumnBound.mulOp` (L11) vs `ResolventForm.mulOp` (L13)
  and the two `mulR`; `integral_norm_sq_eq` in TerminalWickComplete and
  H1Mathlib; `heatDens_eq` in WhiteCollapse and SourceHeatGram;
  `measurePreserving_incr` (RieszFourDiagrams, WhiteFour);
  `measurable_covEps_riesz` (D1Spatial, RieszFourDiagrams);
  `lintegral_cube_timeWeight` (D1Upper, TwoSimplexTime); variant pairs of
  `lintegral_pi_prod`, `sum_incr_le`, `card_closers`, `spatialPos_white_le`,
  `timeWeight_smul`. Docs, reviews, receipts and gates of L12-L14 follow
  (L12 docs running on `wave-l12/int`).
- **LEAN FREEZE AFTER THIS WAVE; PUBLICATION NEXT (Le, 2026-11-13).** Le,
  verbatim: "After this wave of lean verification, we will freeze and start the
  publication proceedure and leave the rest of verification for the future
  or for the community". Scope, from Le's answers the same day: (1) "Finish
  started, gate L10-L14": nothing new is started; the items running now
  (L10 gate preparation, L11 reviews, K5b, D4 follow-up, L14-O) finish; then
  everything already built is integrated, reviewed, receipted and gated (L10,
  L11, and L12-L14 as built: L12 TW, C1, SRC, F1; L13 DM0, DM0b, D1-D4, D6,
  C4-C6, K5a, K5b; L14 K1a, K1b, 3D, 3Dpd, O), with HYG (hygiene before
  v1.0.0) before the release. (2) "Yes, R0 before release": the companion is
  re-anchored to the current manuscript (docs only; the 33 no-go results
  enter as not-formalized rows). Moved to the future/community list, not
  started: L12 NG1-NG3 (and DOC beyond what the L11 merge already did); L13
  D5, NG4; L14 HT, K6a-c, K6d; L15-UM; board B3, B4, B9 stay reserved. The
  publication procedure (release candidate, public-safety audits, fresh-repo
  history, Palomar/Zenodo) is prepared after the freeze; the actual public
  flip, release, DOI and submission each still need Le's explicit go (HOLD
  unchanged until then).
- **L11 DOCS DECISIONS (Le, 2026-11-13).** Le, verbatim: "I accept M2 as a
  model-choice register entry, L:fock-form and L:interval-contractions as
  same-assumptions narrower, and both Index pointer presentations as they
  are; record it in lean-progress/PROGRESS.md and start the L11
  correspondence reviews." On `wave-l11/int` `6277695`: (1) register entry
  M2: the Gaussian space L^2(Omega; X) represented by Hermite coefficient
  vectors, with integrals of words taken coordinatewise; with it
  `L:finite-word-cutoff` counts as a whole result (same-assumptions/full).
  (2) `L:fock-form` and `L:interval-contractions` move from
  inputs-supplied/weaker to same-assumptions/weaker: the completed wrappers
  supply nothing; what is missing is the identification of the Fourier-side
  model with the physical-space operators, recorded as a narrowing (same
  precedent as `P:occupation-physical-class`). (3) Index pointers kept: the
  whole `L:uniform-series-tail` points to TerminalWickInputs (headed narrower,
  TypeContinuity precedent); `P:interval-coefficients` and
  `E:interval-coefficient-bound` point to FiniteWordCutoff (whole result,
  with a step row of `P:interval-coefficients`). L11 correspondence reviews
  started at `6277695`.
- **L9 PUBLIC-DEFINITION COUNT CORRECTION APPROVED (Le, 2026-11-12).** Le,
  verbatim: "I approve a docs-only correction on companion main for the
  public-definition count (89 vs 91) once the L10 repair agent names the two
  declarations; record it in lean-progress/PROGRESS.md and push it as a
  successor to 6eb79c7." Background: the L10 review (p7 W1) found that the
  unlisted public definitions are miscounted; a source scan of main
  `6eb79c7` gives 91 where main's reviewed L9 docs (Scope, README,
  FORMALIZATION) say 89. Plan: the L10 repair agent builds the inventory
  from the elaborated environment and names the two declarations; then a
  docs-only commit on main after `bb79f83` (receipts at `6eb79c7`) corrects
  the count and its totals, Lean untouched, pushed and synced to <HUB>.
  The receipts stay bound to `6eb79c7`. DONE: companion main `1c9e15b`
  (docs only; <HUB> synced). #24's pin check then refused: `63ec3be`
  had added the 15 D8 probe inputs as `*.lean` files under `verification/`,
  and `lean-pkg-binding.yaml` treats every `*.lean` as a build input. Fixed
  in `34b65d7` (probes stored as `.lean.txt`, README in that folder); no
  build input differs from `6eb79c7`; #24 sent `34b65d7` for the pin
  (verified `6eb79c7`, coverage `34b65d7`). Lesson: evidence files must not
  carry build-input extensions.
  The inventory, from the elaborated environment (L10 repair agent,
  `scratchpad l10rev-conf/inventory`), counts 91 unlisted public definitions
  at `6eb79c7` (81 `def`, 6 `abbrev`, 4 `TimeCompletion.Pre` instances; 509
  in all), with the convention now stated in the ledger Scope (source
  `def`/`abbrev`/`instance`/`structure`/`inductive`, not private; Lean-
  generated declarations and the derived `instDecidableEqTrig` excluded).
  The two missing definitions cannot be named singly: the running count
  fell one short when wave L2 was added (three new unlisted declarations,
  counted +2: `HomogHypothesis.Rd`, `RadiusMeanAnchor.quotSet`,
  `RadiusMeanAnchor.supSet`) and once when wave L5 was added (eight new,
  counted +7); every later increment matches.
- **L10 DOCS DECISIONS (Le, 2026-11-12).** Le, verbatim: "I accept the 5
  VariationalMean lost-disclosure flags as a checker false positive and keep
  HigherRieszTwo headed as a narrower result." (1) The lost-disclosure check
  (from `f0b795f` to `wave-l10/int` `aac74b5`) flags 5 VariationalMean rows
  ("the mixed-derivative sentence is not formalized"). They are main's
  reviewed L9 text, unchanged; the disclosure stands in the section heading
  ("without the mixed derivatives") and the section prose, and the check
  misses it only because the word "mixed-derivative" is absent. Recorded as a
  checker false positive; the reviewed text is not edited. (2)
  `HigherRieszTwo` stays headed "narrower result" (it covers d = 2 and the
  shared steps; the whole `L:higher-riesz` is in `HigherRieszThree`), not
  "proof steps of `L:higher-riesz`". Both points still go to the L10
  correspondence reviews running at `aac74b5`.
- **L10-FS1 hQ ACCEPTED FOR NOW (Le, 2026-11-12); L11 item K10 scoped to
  remove it.** Le, verbatim: "I accept L10-FS1's added hypothesis hQ for now;
  record it in lean-progress/PROGRESS.md and scope formalizing
  L:finite-word-cutoff as an L11 item to remove it." What hQ is: in
  `FixedSplit.interval_coefficient_assembly_paper_fixed` (L10-FS1 `826a3da`)
  the coefficient `Q p` of `interval_coefficient_assembly_paper_completed` is a
  free function, so FS1 assumes `|Q p| <= ||<U_r v, U_q v>_(1/T)||`. In the TeX
  Q_(r,q) IS that inner product (main TeX ~3473) and L:finite-word-cutoff
  (~3490-3497) shows it is unchanged by the cutoff; neither step is
  formalized. The L:fixed-split coverage row (L10 docs) lists hQ as an added
  hypothesis, with the class inputs-supplied, weaker.

  L11-K10 (scoped, not launched): formalize L:finite-word-cutoff in the
  form FS1 needs and remove hQ.
  - Have: `StratonovichHAMAudit.HermiteWord.cut_eq_raw` (finite words, abstract
    degree bookkeeping); `HermiteWordFock.cut_eq_raw_fock` (L9: one Gaussian
    mode per color, per-coordinate cutoffs); FS1's Fock model (colors `col :
    Fin m -> iota`, cutoff set `cutIdx col N` = color total degree <= N_i).
  - Gap: (1) the cutoff in FS1 and the TeX is on the per-color TOTAL degree
    over several modes, not per coordinate, so the degree-raising lemmas
    (goodDeg_insert etc.) must be redone for `cutIdx`; (2) identify Q_(r,q),
    defined in P:interval-coefficients' coefficient model, with the cutoff
    inner product `<U_r v, U_q v>_(1/T)` of FS1 (the TeX's line ~3473), which
    needs the coefficient model of `interval_coefficient_assembly_paper_completed`
    to be stated through the Fock embedding rather than as a free Q; (3)
    re-issue `interval_coefficient_assembly_paper_fixed` without hQ.
  - Feasibility: (1) is finite combinatorics on coefficient spaces (no new
    analysis); (2) may need restating Q in the existing assembly theorem, a
    statement change of a claimed theorem (companion major-version rule
    applies after release; before release it is a new wrapper plus a
    coverage update). Size 500-900 lines; risk medium (the identification of
    the TeX's coefficient model). Compile on <MACHINE> or <MACHINE> after the
    L10 integration of FS1. Fallback: (1) alone, with Q's identification as a
    named input replacing hQ (a sharper, TeX-shaped input).
  - Class after: L:finite-word-cutoff same-assumptions, narrower (finite
    words) or full for the multi-mode form; L:fixed-split and
    P:interval-coefficients lose hQ.
- **L8 CORRESPONDENCE REVIEWS (2026-11-12), Codex GPT-6.1-Sol, effort high,
  at companion `3518233` over manuscript `a284420`.** No hold on the model
  (checked). Six groups, nine valid runs: g2 (space-time positivity, finite
  ceiling) PASS_WITH_NOTES; g3 (bracket, mask removal, static phase Cauchy)
  PASS_WITH_NOTES; g5 (symplectic) first run INCONCLUSIVE (packet lacked the
  audit step modules), rerun g5b PASS_WITH_NOTES; g1 (spectral mass, damped
  multiplier) FAIL (1 fatal, 2 major); g4 (finite and terminal Wick) FAIL
  (1 fatal, 2 major); g6 (L8Completed and the changed earlier rows) first run
  INCONCLUSIVE (too large), split into g6a FAIL (2 major), g6b FAIL (1 major),
  g6c FAIL (1 major). All high confidence. No finding is a Lean error: they
  concern ledger and coverage text. Main items: the L:damped-homogeneous-norms
  scope sentence overclaims (covariance smoothing is only multiplier
  membership; Green smoothing identified only in d = 1; found independently by
  four reviewers); the TerminalWick hypothesis hK (global measurability of the
  covariance) is an added hypothesis, not implied by the TeX (fatal; docs will
  disclose it and the row leaves same-assumptions; L11-K4 is asked to remove hK
  from the constructed wrappers); refutation comments on R_0 at alpha = 0
  overstate (Lean's totalized 0/0); FiniteWick integrability wording;
  terminal-wick scope (mixed moments only); "fourteen" -> "fifteen" narrower.
  The classification call on T:intrinsic-occupation-ceiling (same-assumptions,
  narrower) PASSED. Repairs running on branch `wave-l8/repair`; then receipts
  at the repaired commit and a confirmation review. Evidence in session
  scratch l8rev/ and l8rev-b/ (to be copied to reviews/ with the confirmation).
- **COMPANION VERSION LEVELS (Le, 2026-11-12, relayed by #24).** Approved
  with #22's three adjustments and the receipt rule: first public tag
  `v1.0.0` (same MAJOR.MINOR.PATCH scheme as the book, Article
  private/drafts/VERSIONING.md); patch = no claim changes (comments, docs,
  statement-preserving refactor, a Lean/Mathlib/lean-pkg upgrade keeping every
  statement, a re-anchor to a book minor/patch release with only references
  changed); minor = claims added or a coverage row widened, every existing
  statement kept; major = a Lean statement changed, a claim removed, a
  coverage row narrowed or removed, or a move to a new book MAJOR version.
  Every tag of any level sits on a commit carrying its own lean-pkg receipts
  (comparator + lower tier, regated) or on a descendant touching no Lean
  file, claim or coverage entry. Files to adopt in the companion at release:
  Article private/drafts/companion/.github/CODEOWNERS and labels.yml. Owner
  bypass while there is one maintainer; rulesets and squash-only merging
  (private/2026-11-12-community-settings.md) apply after the companion is
  public. The `<wave>-gate` milestone tags stay. Public release still HOLD.
- **L8 COVERAGE DECISION (Le, 2026-11-12): `T:intrinsic-occupation-ceiling`
  is recorded as same-assumptions with a narrower conclusion for the L8
  gate.** Le, verbatim: "I accept recording T:intrinsic-occupation-ceiling as
  same-assumptions with a narrower conclusion (constant K_0 R_sp) for the L8
  gate." What Lean proves (L8-c2 `OccupationCeilingFinite`, discharged with
  nothing supplied in `L8Completed`): under the theorem's standing
  hypotheses, for every c > 0, c I_Psi - v_Psi/2 <= U_c and S_c^pos <= U_c
  with the constant K_0 R_sp, a proved upper bound of C_occ, in place of
  C_occ (a larger ceiling). The row moves from outside to same-assumptions,
  narrower (companion coverage.yaml at the L8 merge `3518233`; COMPLETION
  counts 24 full / 15 narrower / 3 outside main theorems). The exact-C_occ
  form is L9-A (`OccupationCeilingExact`, integrated on `wave-l9/int`); the
  row can become full when L9 is gated. The L8 group-6 Codex review is asked
  to check this classification; the L8 gate itself stays open.
- **WAVE L11: APPROVED by Le (2026-11-12) as proposed, with the default
  answers to the seven decisions.** Le, verbatim: "I approve Lean wave L11 as
  proposed in lean-progress/PROGRESS.md, with the default answers to its seven
  decisions. Run the Easley array gate build + one-task pilot via <MACHINE> at the
  L8 integration commit once its receipts exist." The formalization
  candidates K1-K9 are scoped after the L9/L10 results. Proposal as written: From a read-only
  preparation (session scratch l11-prep/: L11-DRAFT.md, the Easley array
  harness in l11-prep/easley/, probe outputs). Nothing submitted.

  PART A, EASLEY ARRAY GATE (the HPC rule holds: Easley runs gates and
  measured-heavy work only, never an edit-compile loop). Probe (read-only via
  Office): nova_20 has 120 nodes (20 cores, 128 GB), 92 idle at probe time;
  QOS resourcecap_plus caps 1440 CPUs per user (about 1110 free); arrays up
  to 5001; scratch 5.3T of 50T. Harness (written, tested locally with bash
  -n, shellcheck, a byte-for-byte manifest reproduction and synthetic
  collector runs; not yet run on Easley): one build job (4 CPUs, 24G, 1 day;
  fresh clone at a pinned commit, cache get, full build, sealed workspace
  tarball with hashes); then array task 1 alone as a PILOT; only after it
  reaches REPLAY_STARTED are task 0 (default-mode replay of all targets) and
  tasks 2..N (one leanchecker --fresh target each) released; collector
  checks exact coverage against the manifest and sacct COMPLETED 0:0 for
  every task, writes the existing evidence format, and writes a STOP file
  when two failures share a signature. Same checks as waves L5-L7 (commit
  and tree pins, Mathlib pin, module manifest, file-nr guard, monitor,
  checker hashes). Sizing: one --fresh run uses one core and 7.7 GB peak;
  tasks at 2 CPUs and 36G (36G caps packing at 3 tasks per node, keeping
  the node's open files near 186k of 262k; 12G would pack 5-10 per node and
  overrun it). Estimate for about 90-101 targets (the L8 and L9 heads):
  about 1.5 h from submission to collection (vs about 33 h two at a time),
  about 70-80 core-hours used, 175-195 reserved. Comparator receipts stay
  local: Easley has no bwrap or Landlock for the judge (kernel 3.10,
  max_user_namespaces = 0), so lean-pkg's Slurm comparator gives no speedup.

  PART B, FORMALIZATION CANDIDATES (compile on <MACHINE> or <MACHINE>; final
  scoping after the L9 and L10 results):

  | Item | Target | Size | Notes |
  |---|---|---|---|
  | K1 | proof devices of L:occupation-raw-square and L:positive-raw-embedding (H_sp, Q, rho_g, J_G, H_I as Lp completions) | 1300-1700 | would also remove SpaceTimePosDef if any fallback used it |
  | K2 | discharge FockColumn (the spatial column bound of L:fock-form / E:interval-column) | 500-900 | after L9-H |
  | K4 | remaining inputs of L:terminal-wick: (i) strong measurability of the product in L^2; (ii) the d = 3 Green-regularization limit; (iii) constructing the chain measures g_n (L8-f took them by their mass) | 200-400; 400-700; size after scoping | |
  | K5 | D8-lite H^1 Hilbert layer (Mathlib's BesselPotentialSpace, Lax-Milgram) | 800-1500 | Easley pilot first (larger Mathlib slice) |
  | K6 | D8-lite operator layer for C16/C3 (bounded resolvent, ground state from the Rayleigh maximum, compact resolvent as a named input: Rellich is not in Mathlib) | 2000-3500, high risk | Easley pilot first |
  | K7 | any named input that L9 or L10 leaves at a fallback | 200-800 each | |
  | K8 | C:static-interaction re-issued with fewer inputs (after L8-h, L9-H3) | 300-600 | |
  | K9 | the three withheld GaussianChaos seams | | only if Le releases gaussian-chaos-lean |

  (L:alpha-one-convolution, the draft's K3, is already L10-A1.)

  Decisions for Le (defaults in brackets): 1. approve the Easley array gate as
  the replay mechanism from now on, starting with the build + one-task pilot
  [yes]; 2. task sizing 2 CPUs / 36G [yes; 4 CPUs / 36G if Le prefers the
  CPU count]; 3. first full run at the L8 integration commit once its
  receipts exist, then at each later gate commit [yes]; 4. comparator
  receipts stay local [yes]; 5. K5 and K6 only after an Easley pilot of
  their Mathlib imports [yes]; 6. K9 only after a release decision on
  gaussian-chaos-lean [yes]; 7. B3, B4, B9 stay reserved [yes].

  Not in L11: anything needing D1, D2, D5 or D7 beyond the named inputs
  above; the C_2 forms; the public release (HOLD).
- **WAVE L10: APPROVED by Le (2026-11-12) as proposed, with the default
  answers to the nine decisions; the four independent items (R2, W0, FS0, A1)
  launched on <MACHINE>; dependent items start when their L8/L9 inputs are
  integrated.** Le, verbatim: "I approve Lean wave L10 as proposed in
  lean-progress/PROGRESS.md, with the default answers to its nine decisions."
  Proposal as written: From a read-only preparation with every name probed by
  compiling on <MACHINE> (companion built there at 0269e61; homedell-lean.sh,
  homedell-build.sh; draft and probes in session scratch l10-prep/). Each
  candidate is split into an INDEPENDENT core (imports only L1-L7 modules;
  starts on approval, off 0269e61, rebased at integration) and a DEPENDENT
  assembly (starts when its L8/L9 input is integrated; Office or <MACHINE>).
  Excludes B3, B4, B9 and everything in L8/L9.

  Independent (<MACHINE>, first batch of four agents; at most 3 concurrent
  8G builds):

  | Item | Target (TeX at a284420) | Deliverable | Class (fallback) | Size |
  |---|---|---|---|---|
  | L10-R2 | L:higher-riesz (main 5167-5236), d = 2 in full + shared steps; H:spatial-maximum 5008-5021 | the 2-D ball-mass bound G_1(B(w,R)) <= 2R^(3/2) (two cases, rotation + slices), layer cake, scaling, Gaussian double averaging, the d = 3 closed-form maximum 2^(1-alpha)/(2-alpha) (chord/convexity), the approximate identity; H:spatial-maximum in d = 2 with M_2 | row stays inputs-supplied, weaker (scope: d = 2 in full), full after R3 (fallback: the 2-D ball mass as named input TwoDimBallMass) | 600-900 |
  | L10-W0 | prerequisites of T:white-moment-bounds (integrated_white_evaluation.tex 1-11, 101-127) | Gamma = c delta_0, mu = (c/2pi) Leb satisfy HomogCovariance 1 1 a (spectral identity by Fourier inversion at 0); V = c/pi; pairing = c int f^4; F_0(c^2/6) = sqrt c/(3 sqrt 2) tied to WhiteRelativeWidth's formulas | library lemmas (fallback: the spectral identity as named input WhiteSpectral) | 300-450 |
  | L10-FS0 | model-free core of L:fixed-split (main 3053-3400): E:split-segment-product (exponents), E:interval-copy-metric, E:split-word-product, E:split-vector-cauchy, E:split-radius-factorial, E:split-explicit-constant | general telescoping lemma for the interval metric; M_k arithmetic; torus Cauchy extraction for absolutely convergent multivariate power series (avoids the missing multivariable Cauchy formula); word-norm product; C_split = 100^8 e^8 max(1, 12 delta^(-2)) | step lemmas (fallback: one-variable Cauchy, iterated) | 600-900 |
  | L10-A1 | L:alpha-one-convolution (main 4760-4817), new row | polar decomposition of a 1-homogeneous spectral measure (sigma on the sphere x dr); I_a = pi (g_h * p_2a)(v) in [0, pi/2] by Fubini and the Gaussian cosine integral (no Fourier inversion); E:alpha-one-polar and 0 <= ... <= pi V/2; _paper wrapper with the L9-L spectral representation and the L9-G identity as explicit hypotheses | new row inputs-supplied until A1i, then same-assumptions, full (fallback: the polar decomposition as named input PolarDegreeOne) | 600-900 |
  | (L10-J, optional) | L:positive-raw-embedding (integrated_intrinsic_constant.tex 22-112), first half of L:occupation-raw-square | J_G as the Lp G 2 completion under the kernel form (no tensor identification), ||J_G F||^2 = double integral <= K_0 ||F||^2; H_sp, Q; ||Psi||^2 = v_Psi | inputs-supplied, weaker (the mean identity out) (fallback: J_G alone) | 900-1300 |

  Dependent (each starts when its input is integrated):

  | Item | Waits for | Deliverable | Class after | Size |
  |---|---|---|---|---|
  | L10-FS1 | L9-H1, L9-H2 (and FS0) | L:fixed-split assembly: Z_S as Fock coefficient subspaces, E:split-fresh-insertion by vacuum insertion and FockColumn; supplied: L:interval-complex's segment bound and the Dyson cube identity E:interval-cross-cube; removes hfixed from interval_coefficient_assembly_paper_completed | L:fixed-split new row inputs-supplied; P:interval-coefficients loses L:fixed-split as input | 900-1400 |
  | L10-W1 | L8-c1/c2, L8-d integrated (and W0) | T:white-moment-bounds for S_2^pos: (2/3) sqrt(c/M_a) <= S_2^pos <= (2/3) sqrt(c K_0), E_sp = c^2/6 as named input WhiteSpatialEnergy (provenance P:white-spatial-energy; B9 untouched); C_2 and c = 0 out | outside -> inputs-supplied, narrower | 150-300 |
  | L10-R3 | L9-G's Archimedes law (stub once frozen), R2 | d = 3 F_3 formula, M_3 = c 2^(1-alpha)/(2-alpha), optimality by Fatou | L:higher-riesz same-assumptions, full | 400-600 |
  | L10-A1i | L9-G, L9-L integrated | instantiate A1's two hypotheses | L:alpha-one-convolution same-assumptions, full | 50-100 |
  | (L10-Jrho, optional) | L9-A1, L10-J | rho_g, ||rho_g||^2 = A(g), <Psi, rho_g> <= sqrt(v_Psi A(g)) | L:occupation-raw-square inputs-supplied, weaker | 300-500 |

  Decisions for Le (defaults in brackets): 1. independent items start on
  approval, on <MACHINE>, off 0269e61, rebased at integration, not waiting for
  the L8/L9 gates [yes]; 2. core/assembly split as above, dependent halves on
  Office or <MACHINE> whichever is free [yes]; 3. hypothesis-stub pattern for
  A1 now and R3 once L9-G's statement is frozen [yes]; 4. white slice: E_sp
  only as the named input WhiteSpatialEnergy, B9 untouched, C_2 and c = 0
  out [yes]; 5. rows: new rows for L:alpha-one-convolution and (after FS1)
  L:fixed-split; L:higher-riesz scope updated after R2, full after R3 [yes];
  6. E:interval-metric overlap with L9-H3: FS0 owns the general telescoping
  lemma, no duplicate claims [yes]; 7. L10-J and L10-Jrho optional, only with
  spare capacity, Lp G 2 completion, the K_0 row lemma taken from L8-c2 [yes];
  8. <MACHINE> capacity: at most 3 concurrent builds, first batch R2, W0, FS0,
  A1 [yes]; 9. fallbacks are named inputs (TwoDimBallMass, WhiteSpectral,
  PolarDegreeOne), never surrogates; at most two repair rounds per item [yes].

  Gates as in L8/L9. Not in L10, with reasons: the narrowing of
  P:occupation-physical-class (needs an H^1-valued type and a
  joint-representative theorem absent from Mathlib; 1000-1500 lines; L11
  candidate); the derivative clause of L:variational-global-mean (no consumer);
  the real-H clause of P:masked-auxiliary-norm (low value); everything needing
  D1/D3/D7/D8 (tube "In particular", P:interval-coefficients' coefficient model,
  operator statements, P:wave-two-variances and P:masked-noise-completion
  links, B5, B11, B12, B17-B19, B22 rest, C2, C16, C9 rest); reserved B3, B4,
  B9; the mean identity E:positive-raw-mean and the C_2 forms.
- **WAVE L9: APPROVED by Le (2026-11-12) as proposed, with the default
  answers to the nine decisions; to launch on <MACHINE> once the wave-L8
  integration commit exists.** Le, verbatim: "I approve Lean wave L9 as
  proposed in lean-progress/PROGRESS.md, with the default answers to its
  nine decisions. Launch the items in parallel subagents compiling on <MACHINE>
  once the L8 integration commit exists." Proposal as written: From
  three read-only feasibility reconnaissances against the TeX at a284420, with
  every Mathlib name probed by compiling on <MACHINE> (session scratch
  l9-feas/R1.md, R2.md, R3.md and their probe files; office-lean.sh). Excludes
  the reserved B3, B4, B9 and everything in wave L8. Seven items (plus one
  optional), one agent each.

  WHERE IT RUNS. Office (36 cores, about 52G free; companion built there at
  0269e61) does all compiling: each agent edits in its own worktree and builds
  through a wrapper that syncs the worktree's new files to a matching Office
  worktree and runs `lake build` there (8G cap, LEAN_NUM_THREADS=4); this
  laptop only orchestrates, integrates and cuts the lean-pkg receipts (the
  registry lives here). <MACHINE> (12 cores, 34G) is the spare builder.

  | Item | Target (label, TeX at a284420) | Builds on | Class (fallback) | Size |
  |---|---|---|---|---|
  | L9-A1 | P:raw-occupation-energy over the ORIGINAL-kernel class (integrated_occupation_ceiling.tex 92-147): new Araw with TimeSchur.kern a on (0,1)^2, Cocc, EO zeta; 0 < C_occ <= K_0 R_sp (Rsp_eq_R0, squarePairingBounds_holds, TimeSchur.integral_row, concavity); dilation A(U_l g) = l^alpha A(g), T(U_l g) = l^2 T(g) (isUnitH1_dil, hasWeakGradient_dilL2, Measure.map_addHaar_smul); both energy formulas (scalar_max) | OccupationPhysicalClass (IsOccField, sqPair), SpatialFourLinear, TimeSchur, WeakSobolev | same-assumptions, narrower (O by joint representatives, as in L7) (fallback: the bounds and E^O <= D_zeta C_occ^(2/(2-alpha)); the equality as named input RawOccupationDilation) | 600-800 |
  | L9-A2 | L:occupation-rayleigh-selection by FINITE INTERVAL CELLS (g_s = f_i, compact smooth unit tests, on cell i; uniform Lipschitz bound from L8-c2; Mathlib has no measurable-selection theorem, and the TeX's selection needs only measurable_find / exists_dense_seq) and T:intrinsic-occupation-ceiling (E2) with the exact C_occ, both forms, for S_c^pos (205-249); with it B13's S_2^pos <= 2^m F_0(E^O_(1/2)) < 2^m F_a(E^O_(1/2)) | L9-A1 (definitions fixed first), L8-c (space-time Cauchy-Schwarz for step fields), L8-d | E2 moves outside -> same-assumptions, narrower (S_c^pos; the C_2 sentence stays out, D1) (fallback: a 200-line extension of L8-c1's positivity to step fields; else the named input SpaceTimePosDef; never S1Bdd) | 500-800 |
  | L9-H1 | Hermite/Fock FOUNDATION (new modules GaussianHermite, HermiteFock): orthogonality E[He_n He_m] = n! delta via the shift E[He_(n+1) f] = E[He_n f'] on GaussianIBP (derivative identity and recurrence already proved in the probe); normalized multi-index Hermite functions, orthonormal under the product Gaussian, with x_i h_k = sqrt(k_i+1) h_(k+e_i) + sqrt(k_i) h_(k-e_i); the X-valued expansion isometry (X a complex Hilbert space); the abstract finite Fock layer (sum a_i* a_i = degree; creation row norm sqrt(j+1); for self-adjoint H_i with sum ||H_i u||^2 <= c||u||^2 the norm bound 2 sqrt(N+1) sqrt(c), truncated and untruncated; vacuum insertion isometry) | GaussianIBP, Mathlib Polynomial.hermite | foundation, nothing supplied (fallback: the X-valued isometry for scalar X only, the Hermite identification as named input HermiteIso) | 1200-1700 |
  | L9-H2 | consumers: L:fock-form (main 2472-2527; E:fock-sandwich; compression by S_b proved; the spatial column bound sum ||H_i u||^2 <= R_alpha rho^(alpha-4) ||u||^2 as named input FockColumn, provenance the Gaussian isometry, Plancherel and E:phase-resolvent); L:interval-contractions (2829-2898): E:interval-fock and the vacuum-insertion bound, E:interval-column as the same input; E:occupied-multiplication (1802, in P:mild-construction) for finitely many coordinates (spanning lemma: degree-<= n polynomials lie in the Hermite span of degree <= n); bonus: discharge the degree-raising hypothesis of HermiteWord.cut_eq_raw with the concrete Fock model | L9-H1 (run after it in the same worktree, or against fixed stubs of its statements) | L:fock-form, L:interval-contractions inputs-supplied; E:occupied-multiplication same-assumptions, narrower (finite coordinates; the closure in P_(<= n) is D1) (fallback: E:occupied-multiplication only for F given in Hermite form) | 600-900 |
  | L9-G | Wave Green Fourier identities in d = 2, 3 (int e^(i xi.x) dG_s = sin(s|xi|)/|xi|; cited at main 4741 in L:low-alpha-convolution, in L:alpha-one-convolution, and in E:phase-trace of L:phase-contractions): d = 2 by rotation (Submodule.reflection_sub, LinearIsometryEquiv.measurePreserving) and Fubini with the slice integral int_(-1)^1 (1-x^2)^(-1/2) = pi (probed); d = 3 by computing the ball integral two ways (measurePreserving_homeomorphUnitSphereProd; volume_preserving_piFinSuccAbove, EuclideanSpace.volume_ball) and differentiating in R; the Archimedes law (image of the sphere measure under omega -> <e,omega> is 2 pi Lebesgue on [-1,1], Measure.ext_of_charFun); a unified waveGreen_fourier for d in {1,2,3}; L8-b's (iii) (Green smoothing as a Fourier multiplier) extended to every d. No Bessel functions needed | WaveGreen, L8-b | same-assumptions; the d = 3 measure stays the recorded toSphere definitional choice (fallback: d = 2 only; d = 3 and Archimedes deferred) | 700-1100 |
  | L9-P | L:phase-contractions (main 2072-2137; new coverage row): E:phase-resolvent (shifted resolvent <= R_alpha lambda^(alpha-2); Gaussian Fourier pairing, resolvent_homog, L8-a); E:phase-trace (|T_eps| <= D_Gamma a^(1-alpha): radial law Gamma(B_r) = M r^(3-alpha), the sphere convolution formula, three regions); feeds P:static-phase-variance and C:static-interaction | L8-a; L9-G's d = 3 identity and Archimedes law as explicit hypotheses with their exact statements, instantiated at integration | same-assumptions, full (fallback: E:phase-resolvent in full plus the sphere formula and the three-region bound; the trace identity as a named input) | 900-1400 |
  | L9-L | L:low-alpha-convolution (main 4702-4757; new coverage row): V h^(1-alpha)/(1-alpha) in every d (Gaussian spectral representation, charFun_conv, layer cake) | L8-b (iii); L9-G's identity as a hypothesis, instantiated at integration | same-assumptions, full | 400-700 |
  | (L9-H3, optional) | scalar steps of L:complex-phase (2288-2465) and L:interval-complex (2899-2947): the numerical-range parabola, scalar bounds on C_h, F_h, H_h, (39+12 lambda h) e^(lambda h) <= 100 e^(2 lambda h), E:interval-metric, the Neumann bounds 7/6 and 6/5 | SeriesType | inputs-supplied, weaker (Crouzeix-Palencia, the functional calculus, the resolvent integrals supplied) | 300-500 |

  Dependencies: A2 needs A1's definitions and L8-c/L8-d (and a re-check that
  L8-c1's Cauchy-Schwarz covers step fields once L8-c lands); H2 needs H1; P
  and L take L9-G's results as hypotheses (L5-b pattern); P needs L8-a, L
  needs L8-b. All items build on wave L8's modules.

  Decisions for Le inside this approval (defaults in brackets):
  1. Start: [after the wave-L8 integration commit (L9 worktrees off that
     commit, so the L8 modules are importable); not waiting for the L8 gate].
  2. Selection: [finite interval cells instead of the TeX's countable
     measurable selection, stated as a route difference].
  3. The class O: [modelled by joint representatives, as in L7].
  4. Proof devices H_I, H_sp, Q, rho_g of L:occupation-raw-square and
     L:positive-raw-embedding: [not in L9 (1300-1700 lines, low payoff); if
     done later, the Lp G 2 completion with no tensor identification].
  5. Hermite/Fock: [in the companion, not in gaussian-chaos-lean;
     probabilists' He_n normalized by sqrt(n!); finite coefficient spaces, no
     tensor-product inner product; FockColumn the named input for the spatial
     half; general coefficient operators H_i instead of the TeX's rotated
     basis, recorded as a route difference].
  6. Green Fourier in d = 2, 3: [by rotation and slicing, no Bessel
     functions; the d = 3 measure stays the toSphere definitional row].
  7. New coverage rows for L:phase-contractions and L:low-alpha-convolution:
     [yes, same-assumptions].
  8. L9-H3: [include if capacity allows].
  9. Fallbacks are named inputs, never S1Bdd or a surrogate; the C_2 forms
     stay out (D1).

  Gates as in waves L7 and L8 (reviews per item with complete packets; a
  confirmation; the mechanical "unused hypothesis" audit; plain-English scope
  sentences checked against the Lean; receipts here; Le closes the gate).
  Stopping condition: all items integrated and reviewed, or at their fallback
  with the rest named; at most two repair rounds per item.

  Not in L9, with reasons: L:fixed-split (L10, inputs-supplied, 1500-2300
  lines, high risk: needs L:interval-complex's segment bound and the Dyson
  cube identity supplied; it would remove hfixed from the interval-coefficient
  wrappers); the white-noise slice of T:white-moment-bounds (L10, after the L8
  gate; E_sp = c^2/6 only as a named input from P:white-spatial-energy, B9 not
  touched); the d = 3 upper bound of L:higher-riesz (L10, reusing the
  Archimedes law); L:alpha-one-convolution (lower priority); the proof
  devices of decision 4; everything needing D1, D2, D5, D7 or full D8.
- **WAVE L8: APPROVED by Le (2026-11-12) as proposed, with the default
  answers to the six decisions; OPENED** (nine item agents in parallel
  worktrees, branches wave-l8/{a,b,c1,c2,d,e,f,g,h} off companion main
  0269e61; Easley replay of the eight wave-L7 modules at f3be834 submitted
  via <MACHINE> at the same time). Le, verbatim: "I approve Lean wave L8 as
  proposed in lean-progress/PROGRESS.md, with the default answers to its six
  decisions." Proposal as written: From three read-only
  feasibility reconnaissances against the TeX at a284420 with every Mathlib
  name probed by compiling scratch files against companion f3be834 (session
  scratch l8-feas/R1.md, R2.md, R3.md and their probe files; beta.lean and
  lower.lean already compile the hardest pieces of L8-a and L8-b). Excludes
  the reserved B3, B4, B9. Eight items, nine agents (L8-c is split in two),
  one worktree each off companion main; dependencies none between items
  (only waves L6/L7 modules).

  | Item | Target (label, TeX at a284420) | Builds on / new | Class (fallback) | Size |
  |---|---|---|---|---|
  | L8-a | R_alpha = R_Gamma(1): E:intro-spectral-mass (main 530-532, R_alpha = alpha pi mu(B_1)/(2 sin(pi alpha/2))) is EXACTLY the resolvent at 1 for 0 < alpha < 2 (the TeX's polar formula, main 851-858, and the proof of L:spatial-fourier-bound, occupation 149-155); Lean: layer-cake (as SpectralHomog.integrable_inv_one_add_sq), level sets are balls, real Beta integral (beta_real from Complex.betaIntegral, probed); R_Gamma(q) = q^(alpha-2) R_alpha; re-issue spatial_fourier_bound_paper with R_alpha; tie IntervalScalar's R_alpha formula to the resolvent | SpectralHomog, SpatialFourierBound, IntervalScalar | same-assumptions; L:spatial-fourier-bound row weaker -> full (fallback: R_Gamma(1) = V int ((1-t)/t)^(alpha/2), beta_real separate; still full) | 150-220 |
  | L8-b | L:damped-homogeneous-norms (main 803-919; E:damped-multiplier-comparison 836-841): the general lower bounds 0 <= N_{1,m,S}, 0 <= N_{2,m,S}^2; and the claims inside the smoothing remarks (845-848, 914-917): (i) Gaussian multipliers exp(-eta|xi|^2) are measurable with values in [0,1] (closed under products); (ii) GreenMass is preserved by convolution with a probability measure (so N_0 unchanged), instantiated with the Gaussian and waveGreen; (iii) Green smoothing is a Fourier multiplier (charFun_conv, charFun_multivariateGaussian), identified with smoothed N_2 in d = 1 (waveGreen_fourier_one) | DampedNormsHomog, WaveGreen | same-assumptions; row weaker -> full (fallback: lower bounds + (i),(ii); row stays weaker, "Green smoothing as a Fourier multiplier not formalized") | 120-200 |
  | L8-c1, L8-c2 | S1BDD DISCHARGED DETERMINISTICALLY (the boundedness claim of P:variational-positive-scores, unmasked 272-274; supplied since L6; TeX proof stochastic via T:full-upper): route of R2 (not the TeX's countable selection): (a) near-optimal unit TEST functions from h1TestDense; (b) finite hat partition in time (R_f(s) and lambda_s^2 Lipschitz in s); (c) space-time positive-definiteness and Cauchy-Schwarz F(Psi,G) <= sqrt(v_Psi F(G,G)) via TimeCompletion.kern_eq_mixture, spatialPair_self_nonneg and mollification; (d) F(G,G) <= K_0 R_0 T^(alpha/2) (smooth_square_bound, squareBound_R0, TimeSchur.integral_row with the sharp K_0 = 2^a/(1-a), Jensen); (e) scalar_max -> I_Psi - v_Psi/2 bounded = S1Bdd. c1: step (c) with the identities F(Psi,Psi) = v and int int h_s G_s = F(Psi,G) (800-1000 lines); c2: steps (a),(b),(d) (700-900 lines); the integrator does (e), re-issues every S1Bdd-dependent statement WITHOUT S1Bdd (variational_positive_scores_sSup_paper, spatial_static_energy_score_sSup, spatial_smooth_score_sSup, the R_0-from-S1Bdd corollaries) and adds occupation_ceiling_K0_paper: S_c^pos <= U_c with K_0 R_sp in place of C_occ (T:intrinsic-occupation-ceiling's display, narrower constant) | WeakSobolev, VariationalFloor/Rate, H1Density, SpatialFourLinear, OccupationPhysicalClass, TimeCompletion, TimeSchur | P:variational-positive-scores inputs-supplied -> same-assumptions (weaker only for Q_2 >= S_2^pos); the sSup forms of L:spatial-static-controls, P:spatial-smooth-ratio, P:spatial-energy-map lose their named input (fallback: one named input SpaceTimePosDef, space-time positive-definiteness for continuous compactly supported fields, provenance L:positive-raw-embedding, deterministic and much weaker than S1Bdd; NEVER fall back to S1Bdd) | 1600-2200 |
  | L8-d | B13 C:intrinsic-spatial-bracket (integrated_occupation_ceiling.tex 251-316) stated for S_2^pos: lower half (E:spatial-static-energy-score, existential form, already in Lean; sSup form after L8-c), upper half (the ceiling with C_occ <= K_0 R_sp, from L8-c taken as an explicit hypothesis with its exact statement, instantiated at integration), F_a and F_b, the log gap Delta > 0, F_0 < F_a, the integer counterexample (norm_num) | SpatialFourLinear (F0, Esp), L8-c (hypothesis) | same-assumptions, narrower (S_2^pos, not C_2: C_2 = S_2^pos is T:intrinsic-second-moment, D1) | 300-500 |
  | L8-e | P:variational-remove-mask (integrated_unmasked_variational.tex 168-222): the mask chi(r) = Real.smoothTransition(2-r) (exactly F(2-r)/(F(2-r)+F(r-1))), m_R(x) = chi(|x|/R) smooth, even, in [0,1], 1 on |x| <= R, increasing to 1; masked rates (Rayleigh convention of VariationalRate); floor for R >= R_0; monotone in R; exchange of suprema (monotone convergence) -> pointwise convergence; continuity in s; uniform convergence on [0,1] by Dini; int_I lambda_{R,s} -> I_Psi | WeakSobolev, VariationalRate, VariationalFloor | inputs-supplied (P:raw-block-original-lower for E:variational-unmasked-point-lower, C17; the rate identification as in L6), rate-convergence clauses same-assumptions (fallback: drop the point-moment display) | 500-800 |
  | L8-f | L:terminal-wick (main 3585-3699) with a NEW finite Wick foundation (a D1 slice): Isserlis/Wick formula for multivariateGaussian 0 K (moments of 2k coordinates = sum over fixed-point-free involutions of Fin (2k); odd orders vanish), by Stein recursion through GaussianIBP.integral_coord_mul_eq_of_growth on x = sqrt(K) g; pairing sums nonnegative and monotone in K >= 0; chain-measure mass T^(2n)/(2n)! (WaveGreen); the majorant sqrt((2n-1)!!) V^(n/2) T^(2n)/(2n)!; absolute convergence; assembly of E:terminal-wick-formula (integral_inner); payoff: discharges both fields of UniformSeriesTail.TerminalWickInput when K >= 0 | GaussianIBP, FiniteGaussianMatrix, WaveGreen, UniformSeriesTail | inputs-supplied (strong measurability of the product map in L^2; the d = 3 Green-regularization limit) (fallback: Wick core + mass recursion + majorant as a standalone foundation; assembly and discharge deferred) | 1300-1900 (Wick core 600-900) |
  | L8-g | L:symplectic-free abstract core (integrated_symplectic_phase.tex 30-134): W^T J W = J at every frequency (zero included; reuses the B22 matrices); abstract lemma: S commuting with isometries tau_y with tau_y z -> 0 weakly gives ||S + K|| >= ||S|| for compact K; norm limits of compact U - I are compact; the ordered product minus the free product is compact (telescoping); ||S(h)|| >= 1; skewness of B(b) for omega | DimensionalMatrix (B22), Mathlib IsCompactOperator | inputs-supplied (E = H^(1/2) x H^(-1/2) with its free group and weak nullity of translations, D8; convergence of the Young sums, D7) (fallback: the matrix identity, the compactness facts and ||S(h)|| >= 1) | 500-800 |
  | L8-h | P:static-phase-all-orders (main 2577-2683), Cauchy and scalar steps (step rows, like L7-f): coefficient bound for an entire operator-valued map bounded on a circle (norm_cauchyPowerSeries_le, Complex.norm_iteratedDeriv_le_of_forall_mem_sphere_norm_le), the arithmetic at lambda = n/h (2631-2643) giving E:all-static-phase-orders with A_alpha = 400 sqrt2 e^2/delta, the squaring to E:all-static-phase-sum (SeriesType.seriesNu_le_two_exp_three); the existing step row extended | SeriesType, IntervalScalar | inputs-supplied, weaker (L:fock-form, the circle bound from L:complex-phase, the X_lambda norm comparisons, cutoff removal) (fallback: the arithmetic and the squaring only) | 300-500 |

  Decisions for Le inside this approval (defaults in brackets):
  1. L8-a: [the main wrapper states the TeX constant R_alpha (open unit ball); the R_Gamma(1) theorem stays as the general form; row full].
  2. L8-b: [carry (i), (ii), (iii) in general form; covariance smoothing recorded as multiplier membership only (smoothing Gamma itself needs Fubini against an infinite locally finite measure); the scaling caveat stays commentary; row full].
  3. L8-c route: [the finite hat partition in time in place of the TeX's countable measurable selection (L:occupation-rayleigh-selection), stated as a route difference; the fallback is the named input SpaceTimePosDef, never S1Bdd].
  4. L8-c/L8-d scope: [the C_2 forms (E2's last sentence, B13 for C_2) stay out: C_2 = S_2^pos is T:intrinsic-second-moment (D1); T:intrinsic-occupation-ceiling with the exact constant C_occ, L:occupation-raw-square (Q, rho_g, H_I), P:raw-occupation-energy over O with the original kernel and the selection lemma are L9 candidates (1500-2000 lines)].
  5. L8-f: [the finite Wick foundation goes in the companion (not in gaussian-chaos-lean, whose release is a separate decision); pairings as fixed-point-free involutions; if the risk materializes, ship the foundation alone].
  6. Classes: [exact-hypothesis _paper wrappers; supplied inputs named with their TeX labels; the Rayleigh-rate convention of L6].

  Gates as in wave L7 (wrappers, refutations importing the package, Audit, claims/ledger/coverage with plain-English scope sentences checked against the Lean definitions, index check, check-controls, comparator extended to every new theorem claim, receipts of both tiers at one commit with no edits during the run, regate, claims ledger READY 0 open; one Codex GPT-6.1-Sol review per item from packets that contain every file the contract names (row counts checked against the fragments), plus a confirmation; a mechanical audit of every "carried but unused" claim; Le closes the gate). Also in this wave: Easley leanchecker --fresh replay of the eight wave-L7 modules at f3be834 (requires the VPN or Office route) and of the L8 modules after integration. Stopping condition: all items integrated and reviewed, or an item at its fallback with the rest recorded as named inputs; at most two repair rounds per item.

  Not in L8, with reasons: L:fixed-split (350-line proof on L:interval-contractions, L:interval-complex, L:complex-phase and a finite Fock space; stays supplied); L:fock-form and E:occupied-multiplication (Hermite orthogonality absent from Mathlib; L9); P:mild-construction, L:joint-fixed-order (diagram limits in Gaussian polynomial spaces, D1/D5); C2 generic part (Young integration for C^theta paths, D7; only a few Banach-algebra steps would be honest, low value); C16 (spectral theorems, D8; its form-level slice already exists); C9 beyond L:symplectic-free (D1/D7/D8); B5 law part (D4/D5), B11 (D1), B12 (no Schatten classes in Mathlib), B17 (Gaussian path law), B18 (D7), B19 (D2), B22 rest (D8); E2 with C_occ and its three lemmas (see decision 4). B3, B4, B9 stay reserved.
- **WAVE L7 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-12)** at companion
  f3be834 over manuscript a284420, together with the re-anchor from 975feb3
  to a284420: Le, verbatim: "I accept the six wave-L7 reviews plus the
  confirmation and the a284420 re-anchor (re-check + confirmation PASS/high)
  as closing the Lean wave L7 correspondence gate at companion f3be834 over
  manuscript a284420." Le's decision was also relayed verbatim by #16
  (2026-11-12): "Approve the Lean wave L7 gate and the re-anchor to a284420
  at companion f3be834. Tell #22 to record it." Recorded in the companion
  README (ed3cd68), the board
  (docs/community c038761) and STATUS-DIGEST; #16, #3 and #24 told, with the
  docs-only HEAD ed3cd68 for Appendix F. Scope: AI statement-to-manuscript
  correspondence of the 268 wave-L7 ledger rows, the changed sections and
  coverage rows, and the re-anchored rows of the two edited results; NOT
  human verification; the supplied inputs (L:terminal-wick's two facts for
  L:uniform-series-tail; the energy-split identity and L:fixed-split for
  P:interval-coefficients; the operator/stochastic inputs of
  C:static-interaction; S1Bdd for the supremum forms) and every analytic
  input outside Lean are not verified; any later change to these rows or to
  a cited label needs a successor review. Details: OVERNIGHT TODO LIST 2
  below (FINAL entry). Open: the Easley replay of the wave-L6 modules (job
  5692528; VPN down, collect when reachable); the wave-L7 modules have not
  been replayed on Easley.
- **OVERNIGHT TODO LIST 2 (Le, 2026-11-11 evening: "make a todo list for
  this overnight work and complete them overnight; the aim is to complete
  the lean verification as much as possible").** Read, as on 2026-11-10, as
  approval to RUN wave L7 as proposed in item 3; every gate stays Le's to
  close. Order and status (updated as items complete):
  1. [x] DONE (2026-11-12): job 5692528 PASS 16/16 (--fresh, each 43:13-44:08,
     peak ~7.7 GB; default mode 73/73; COMPLETED 0:0, 06:09:54, node831;
     collected via <MACHINE> after the laptop VPN dropped). Import-closure check:
     every module not replayed has, comments stripped, the same source and
     imports as at an earlier --fresh replay. Evidence companion 0269e61,
     verification/leanchecker-easley-wave-l6/ (HPC username, container path,
     runtime directory redacted; grep clean), README replay sentence. The
     eight wave-L7 modules are not yet replayed. #24 sent the SHA.
     (Original item:) Easley `leanchecker --fresh` replay of the 14 wave-L6 modules plus
     umbrella and Axioms at companion bfa2fd0, two at a time (harness ready
     in session scratch easley/wavel6: commit/tree pins, 73-target manifest,
     16 fresh targets); evidence verification/leanchecker-easley-wave-l6/,
     README replay sentence, record here. BLOCKED until Le connects the
     Auburn VPN and opens the Duo-authenticated ssh master (`ssh -fN
     Easley`); retried whenever the connection is up.
  2. [x] DONE; accepted by Le 2026-11-12 with the L7 gate: When #3 commits the two approved manuscript points: re-anchor the
     companion (labels, statements/proofs, line citations,
     provenance/manuscript-anchor.json, ledger anchor sentence; new receipts
     if Lean comments move), narrow Codex re-check of P:spatial-smooth-ratio,
     SpatialFourierBound, SpatialSmoothRatio, the DampedNormsHomog smoothing
     rows and coverage notes; adjudicate; record.
  3. [x] DONE; gate closed by Le 2026-11-12 at f3be834 over a284420: Wave L7 (deterministic targets left after L6, from the "Not in L6"
     list), one agent and worktree each off companion main e4c9bd4, same
     gates as L6 (exact-hypothesis wrappers, refutations, audit, no sorry,
     standard axioms):
     - L7-a `L:inventory-product` (main TeX 2949-3015): the coefficient
       bound [z^k] prod (1 + v_i z + sum b_il z^l) <= C^k/(k!)^nu, in full
       (deterministic).
     - L7-b `L:uniform-series-tail` (main 3666-): the L^2 tail and limit
       statements from the uniform r-moment bound, with any structural input
       of its proof (the coefficient extraction in r) as a named hypothesis.
     - L7-c D8-lite half (a): density of smooth compactly supported
       functions in the hand-rolled weak-gradient H^1 (WeakSobolev).
     - L7-d `P:spatial-four-linear` and `P:spatial-energy-map`
       (integrated_spatial_occupation.tex 150-316) on H^1 profiles, with
       L7-c's density as an explicit hypothesis (instantiated at
       integration).
     - L7-e `P:occupation-physical-class` (integrated_spatial_occupation.tex
       317-) over L7-c/L7-d, same pattern.
     - L7-f the deterministic scalar steps of `C:static-interaction` and
       `P:interval-coefficients` (main 2649-, 3365-) as step rows
       (inputs-supplied, weaker), reusing SeriesType.
     Fallback per item: the largest honest scope with the rest as named
     inputs. Then integrate (umbrella, Axioms, claims, ledger, coverage,
     README/FORMALIZATION), check-controls, extend the comparator,
     receipts of both tiers at one commit, regate, claims ledger READY 0
     open; one Codex GPT-6.1-Sol review per item plus a confirmation;
     adjudicate and repair; STOP for Le's gate.
  4. [x] DONE (2026-11-12): Board, README Trust section, STATUS-DIGEST; tell #16, #3, #24.
  5. [x] DONE (2026-11-12, Le-AI-Lab 592207e): Retro of the night's lessons into Le-AI-Lab skills.
  STATUS (2026-11-12, overnight; updated as items complete):
  - Item 1: Easley up at 21:55 (Le connected); job 5692528 submitted at
    companion bfa2fd0 (16 --fresh targets two at a time, default replay of all
    73), running on node831; 1-day limit.
  - Item 3: all six items formalized, independently re-verified by the
    integrator (build, refutations, audit, standard axioms only, forbidden
    tokens absent) and merged (wave-l7/int): L7-a InventoryProduct
    (L:inventory-product in full, nothing supplied); L7-b UniformSeriesTail
    (L:uniform-series-tail, one input from L:terminal-wick: absolute
    summability and nonnegative mixed moments); L7-c H1Density (density of
    test functions in the weak-gradient H^1, nothing supplied); L7-d
    SpatialFourLinear (P:spatial-four-linear, P:spatial-energy-map); L7-e
    OccupationPhysicalClass (P:occupation-physical-class; class O modelled by
    joint representatives); L7-f IntervalScalar (scalar steps of
    C:static-interaction and P:interval-coefficients). Completion modules
    IntervalScalarCompleted (discharges L:inventory-product) and
    SpatialOccupationL7Completed (discharges the density and four-linear
    inputs). 20 TeX line citations corrected comment-only. Docs merged (1731
    claims: 1430 theorems, 301 definitions; 877 labelled, 854 unlabelled;
    coverage 66 rows: 38 same-assumptions incl. 10 narrower, 24
    inputs-supplied, 4 outside). Comparator extended to all 1430 theorem
    claims (CheckFidelity 1430/1430, 0 problems; mutation caught). Companion
    main a8fb495: comparator receipt PASS (1430); lower-tier receipt running.
    No manuscript defect found.
  - Item 3 reviews (Codex GPT-6.1-Sol, high) at a8fb495 over 975feb3: H1Density
    PASS; InventoryProduct, OccupationPhysicalClass, IntervalScalar
    PASS_WITH_NOTES; UniformSeriesTail FAIL (one FATAL: my plain-English
    rewording at d3d7f4c of the L:spatial-static-controls and
    P:spatial-smooth-ratio scope sentences says lambda is the Rayleigh
    supremum; it is its square root; #24 had printed it on book p. 307,
    nothing public; #24 told at once and holds the page); SpatialFourLinear
    FAIL (one MAJOR: Gamma_tempered claimed unused but used transitively).
    Seven minors (wording, one citation). All documentation; repair agent
    running (branch l7-repair), then confirmation review.
  - Item 2: #3 committed the two points at Article a284420 (new
    L:spatial-fourier-bound with E:spatial-fourier-bound before
    P:spatial-smooth-ratio; E:damped-multiplier-comparison in
    L:damped-homogeneous-norms). Re-anchor to a284420 follows the L7 repairs
    (one line-citation remap for all waves), then receipts and the narrow
    re-check.
  - FINAL (2026-11-12 morning): companion main 6a9fa9b (docs-only descendant
    of f3be834; receipts 5aa557b at f3be834: comparator PASS, 1430 theorems;
    lower tier 0 sorry, 1731 claim axioms, standard axioms only, peak 9.3 GiB;
    re-gated verified-private a8fb495 -> f3be834 with comparator evidence;
    claims ledger READY, 1071 required, 1681 verified, 0 open).
    Wave L7 review chain: six reviews at a8fb495 (H1Density PASS; three
    PASS_WITH_NOTES; UniformSeriesTail FAIL fatal = my lambda rewording;
    SpatialFourLinear FAIL major = Gamma_tempered use), all repaired
    (d2d29df; a mechanical field-use audit found one more wrong unused claim);
    confirmation at d19c71a FAIL (C1 major, C2 minor, docs), repaired at
    b0c995b. Re-anchor to a284420 (#3's edits): 255 cited labels exist once,
    249 unchanged, 3 new (L:spatial-fourier-bound, E:spatial-fourier-bound,
    E:damped-multiplier-comparison); 2888 citations, 1386 moved; new coverage
    row L:spatial-fourier-bound (same-assumptions, weaker: Lean's constant is
    R_Gamma(1), the TeX's R_alpha, identity not formalized);
    L:damped-homogeneous-norms now weaker (the revised statement's lower
    bounds for general m, S and the smoothing remarks are not stated in Lean).
    Narrow re-check at 3eaf6ce FAIL (A1-A3 major, A4 minor, docs; A3 = TeX
    locators misattributed to the wrong file by the shift tooling): full
    content check of 1781 citations, 46 corrected (f3be834); confirmation
    v1 INCONCLUSIVE (two changed refutation files missing from the packet),
    v2 PASS/high, no findings. Evidence: reviews/2026-11-11-lean-wave-l7-*
    (06ca20d), reviews/2026-11-12-lean-{wave-l7-confirm,reanchor-a284420,
    reanchor-a284420-confirm} (756d462). Totals: 1731 claims (1430 theorems,
    301 definitions; 891 labelled, 840 unlabelled); coverage 67 rows (39
    same-assumptions incl. 12 narrower, 24 inputs-supplied, 4 outside); 55
    whole-result modules. No manuscript defect found in L7. FOR LE: close the
    wave-L7 gate and accept the re-anchor to a284420, at companion f3be834
    (docs-only HEAD 6a9fa9b), or name changes. Item 1 (Easley L6 replay, job
    5692528) still running.
  - Also: proposal 0015 accepted by Le and merged in lean-pkg (#456, #457);
    unreleased, so the coverage-scope-tex sidecar stays until 0.30.0. Two L6
    scope sentences reworded in plain English at #24's request (companion
    d3d7f4c).
  NOT for the night (Le's decisions): closing the L7 gate; any public
  visibility change (HOLD); acceptance of lean-pkg proposal 0015; a lean-pkg
  upgrade; manuscript edits (#3's, approved by Le, only re-anchored here).
- **Two manuscript points from the Lean verification (asked #3 at Le's
  request, 2026-11-11; answer pending):** (1) R_0 < infinity WITHOUT
  T:full-upper: Lean proves deterministically under H:homog alone, for every
  admissible Gamma, A_sp(g) <= 2^(1+alpha) R_Gamma(1) b^(alpha/2), hence
  R_0 <= 2^(1+alpha) R_alpha (spectral identity of the autocorrelation,
  |Q^| <= 1, integration by parts |xi||Q^| <= 2 sqrt(b), resolvent
  homogeneity; companion SpatialFourierBound.spatial_fourier_bound_paper),
  while P:spatial-smooth-ratio gets it from S1Bdd (occupation TeX 142-145).
  (2) The smoothing/truncation sentence of L:damped-homogeneous-norms (main
  TeX 789-791) read as a measurable multiplier 0 <= g <= 1 of mu and a
  measurable restriction of the Laplace domain (Le's reading; uses at
  1072-1082 and 1591-1600 fit). Asked #3 whether to add both to the
  manuscript; Le decides the edit. **#3's answer (2026-11-11): recommends
  adding BOTH, subject to Le's manuscript decision; no manuscript edit made;
  recorded as recommendations awaiting Le's edit decision, NOT a successor
  manuscript review acceptance.**
  (1) YES, a substantive simplification. #3 checked P:spatial-smooth-ratio,
  its S_1^pos dependency, H:homog, the damped resolvent proof and the pinned
  SpatialFourierBound.lean; the constant is correct:
  8b R_Gamma(2 sqrt b) = 2^(1+alpha) R_Gamma(1) b^(alpha/2), b > 0 for a real
  smooth compact unit test. Notation: write the UNNORMALIZED transform
  FQ(xi) = int exp(-i xi.x) Q(x) dx explicitly; with the chapter's unitary
  hat, A_sp = (2pi)^d int |hat Q|^2 dmu and |hat Q| <= c_d, the factors cancel
  and the constant is unchanged; do not print the unnormalized identity with
  the unitary hat unexplained (Lean's fourierQ is unnormalized, plus sign;
  |.|^2 unaffected for real Q). Place a short deterministic lemma right
  before P:spatial-smooth-ratio (or a separate first part of its proof):
  Schwartz autocorrelation identity, Fourier/gradient bounds, resolvent
  scaling; use it for R_0 finiteness, keep the score argument, cite the
  deterministic resolvent calculation instead of T:full-upper. Covers
  Gamma = 0 (R_0 = 0; strict positivity stays local to Gamma != 0) and
  singular measures; a finiteness bound, not a sharp constant. Keep S1Bdd
  where real-valued S_1^pos conclusions need it: this removes the stochastic
  dependency for R_0 and the downstream purely spatial estimates, not for
  every C19/S_1^pos conclusion.
  (2) YES, useful precision. Scope: for theta > 0, measurable m : R^d -> [0,1]
  and measurable S subset S' subset (0,inf), with N_{1,m,S}, N_{2,m,S}^2 the
  spectral expressions with mu replaced by m mu and the Laplace mixture
  restricted to S: 0 <= N_{1,m,S} <= N_{1,1,S'} and
  0 <= N_{2,m,S}^2 <= N_{2,1,S'}^2 (full and tail comparisons, Gaussian
  spatial/Green multipliers). Use m, not g (g is the spatial profile in (1)).
  Explain that N_2 monotonicity is taken after the time quadratic form at
  each (lambda, xi), nonnegative by positive definiteness of
  exp(-lambda|s-t|), not pointwise for the oscillating wave-kernel product.
  A bound for the spectral expressions only: an arbitrary m need not preserve
  homogeneity or a nonnegative physical covariance; do not extend the
  scaling identities or assert a new admissible H:homog model for m mu.
  N_0 has no covariance multiplier: keep its mass argument separate
  (Gaussian Green smoothing preserves G_s(R^d) = s). The current
  applications fit this reading.
  **Le's decision (2026-11-11): add BOTH as #3 recommended.** Sent to #3:
  (1) the deterministic lemma A_sp(g) <= 2^(1+alpha) R_Gamma(1) b^(alpha/2)
  just before P:spatial-smooth-ratio (unnormalized transform explicit,
  Gamma = 0 and singular measures covered), used for R_0 finiteness instead
  of T:full-upper, S1Bdd kept for the real-valued S_1^pos conclusions;
  (2) the multiplier/Laplace-restriction scope (m, S subset S') in
  L:damped-homogeneous-norms with the quadratic-form and scope notes.
  Next after #3's commit: re-anchor the companion to the new revision
  (labels, statements/proofs, line citations) and re-check the affected
  ledger rows (P:spatial-smooth-ratio, SpatialFourierBound,
  SpatialSmoothRatio, DampedNormsHomog smoothing rows, coverage notes).
- **WAVE L6: APPROVED by Le (2026-11-11) as proposed, with the default
  answers to the four decisions; OPENED** (eight items launched in parallel
  worktrees, branches wave-l6/a..h off companion main). From the board
  (excluding the reserved B3, B4, B9), after three read-only feasibility
  reconnaissances against the TeX at 975feb3 with every Mathlib name probed
  by compiling scratch files against companion main (session scratch
  l6-feas/R1-R3). Several probes already contain working proofs: the wave
  Green masses in d = 2, 3, the finite Gaussian convolution identity, the
  rotation lemma, the weak gradient of a test function, sum a^nu <= (sum
  a)^nu and Gamma((x+y)/2)^2 <= Gamma(x)Gamma(y). Eight items, one agent and
  worktree each, as in wave L5; dependencies noted.
  **WAVE L6 CORRESPONDENCE GATE: CLOSED (Le, 2026-11-11)** at companion
  bfa2fd0 over manuscript 975feb3: Le accepted the eight Codex reviews plus
  the confirmation ("Yes, close L6 at the new commit if the re-confirmation
  is clean"); the narrow re-confirmation at bfa2fd0 was clean (PASS/high,
  4/4, no findings). Recorded in the companion README (e4c9bd4), the board,
  STATUS-DIGEST; #16, #3 and #24 told. Scope: AI statement-to-manuscript
  correspondence of the 491 wave-L6 ledger rows and the changed sections and
  coverage rows; NOT human verification; the supplied inputs (S1Bdd for the
  supremum statements, the D1/D8 links of P:wave-two-variances and
  P:masked-noise-completion, the T:full-upper and static-law inputs of
  P:moment-growth-logconvex and C:static-moment-constant-continuity) and
  every analytic input outside Lean are not verified; any later change to
  these rows or to a cited label needs a successor review (the pending
  manuscript edits to P:spatial-smooth-ratio and L:damped-homogeneous-norms
  will trigger one). Easley replay of the 14 new modules not yet run.
  - Results (coverage rows): L:damped-homogeneous-norms now same-assumptions,
    full (WaveGreen discharges GreenMass for d = 1, 2, 3; the d = 3 measure
    via Measure.toSphere is a recorded definitional choice);
    P:masked-quotient-obstruction same-assumptions, full; P:masked-noise-
    completion inputs-supplied, weaker (the finite Gaussian comparison in
    full; the identification with the masked/auxiliary covariances, D1,
    supplied); P:wave-two-variances inputs-supplied, weaker (spectral core
    input-free; E:variance-normalized-covariance and J supplied);
    P:variational-unmasked-rate same-assumptions, weaker (operator half out,
    D8); P:variational-positive-scores inputs-supplied, weaker (S1Bdd);
    P:spatial-smooth-ratio same-assumptions, weaker, with R_0 < infinity by
    the deterministic bound of SpatialFourierBound (a different route than
    the TeX); L:spatial-static-controls same-assumptions, weaker;
    L:positive-series-type, C:white-relative-width and L:white-clock-laplace
    same-assumptions, full; P:moment-growth-logconvex and
    C:static-moment-constant-continuity inputs-supplied, full; step rows for
    L:higher-riesz and P:static-phase-all-orders. No manuscript defect; two
    manuscript points (the deterministic R_0 bound, the smoothing scope)
    approved by Le for addition (see the bullet above).
  - Companion: 14 modules (WaveGreen, QuotientObstruction,
    GaussianComparison, WaveTwoVariances, SpatialFourierBound,
    VariationalFloor, VariationalRate, SpatialSmoothRatio,
    SpatialStaticControls, SpatialOccupationCompleted, SeriesType,
    TypeContinuity, WhiteRelativeWidth, WhiteClockLaplace); duplicated
    definitions across L6-d/e/f unified, RayleighFloor and StaticControls
    discharged in SpatialOccupationCompleted. Comparator over 1210 theorem
    claims (CheckFidelity 1210/1210 types equal, 0 problems); check-controls
    PASS (68 controls, 139 refutations, 71 audits).
  - Reviews (Codex GPT-6.1-Sol, high) at 250cf39 over 975feb3: eight valid
    reports (3 FAIL, 5 PASS_WITH_NOTES), 16 findings (2 fatal, 1 major,
    13 minor), all in the documentation, none in a Lean statement or proof;
    all accepted and repaired on l6-repair (merged; 4486c57). Evidence
    Article 498f094, 3735f16 (reviews/2026-11-11-lean-wave-l6-*).
    Confirmation at 4486c57: FAIL/high on one minor (C1, a stale GreenMass
    doc comment in DampedNormsHomog; the same claim in DampedNorms), repaired
    comment-only at 4b09ee6, merged 212aeea, comparator copies regenerated
    bfa2fd0 (Article abb6ee4). Narrow re-confirmation at bfa2fd0: PASS/high,
    4/4, no findings (Article 05677ba, reviews/2026-11-11-lean-wave-l6-reconfirm).
  - Receipts at bfa2fd0 (committed d3f6a2b): comparator pass (1210
    theorems); lower tier 0 sorry, 1463 claim axioms standard, peak 9.0 GiB.
    (Receipts at 4486c57 also passed, 1d1eda6; superseded.) Re-gated
    verified-private 4486c57 -> bfa2fd0 with comparator evidence; claims
    synced; `claims ledger`: READY, 914 required, 1417 verified, 0 open,
    46 out-of-scope (internal helper definitions). Docs-only descendants:
    bae18f4 (Easley L5 evidence), e4c9bd4 (README closure); ledger still
    READY at e4c9bd4.
  - Totals: 1463 claims (1210 theorems, 253 definitions); 737 labelled, 726
    unlabelled; coverage 59 rows (34 same-assumptions incl. 7 narrower,
    4 inputs-supplied full, 17 inputs-supplied steps/narrower, 4 outside);
    47 whole-result modules, 70 library modules.

  | Item | Target (label, TeX at 975feb3) | Builds on / new foundation | Class (fallback) | Size |
  |---|---|---|---|---|
  | L6-a | `L:damped-homogeneous-norms` with NOTHING supplied: define the wave Green measures `waveGreen d s` (d = 1: (1/2)1_{|x|<s}dx; d = 2: 1_{|x|<s}dx/(2 pi sqrt(s^2-|x|^2)); d = 3: sigma_s/(4 pi s) via `Measure.toSphere`; main TeX 709, 5106-5112, Chen (2.5)), prove mass s, finiteness, support in the closed s-ball and the scaling G_s(sA) = s G_1(A); discharge `GreenMass` | DampedNormsHomog; mass in d = 2, 3 already proved in probes | same-assumptions, full (the d = 3 measure is a definitional choice, "toSphere is the surface measure", recorded as such; optional: the d = 1 Fourier identity int e^{i xi x} dG_s = waveHat; d = 2 stretch; d = 3 Fourier deferred) | 250-350 (+100-150) |
  | L6-b | C21 `P:masked-quotient-obstruction` (integrated_covariance_foundation.tex 257-292), and the finite Gaussian comparison of `P:masked-noise-completion` (188-249: A <= B in PSD order => E N(X)^p <= E N(Y)^p for X ~ N(0,A), Y ~ N(0,B), p >= 1, any seminorm N) | TimeCompletion/TimeSchur for the time form; Mathlib multivariateGaussian, charFun_conv (convolution identity compiles), Fernique moments | obstruction: same-assumptions with E W(F)^2 read as the E:cov covariance functional (a definitional D1 boundary, stated), including that Gamma = delta_0(dx1)dx2 satisfies H:homog (fallback: that membership as one named input); comparison: the finite statement in full, its identification with the masked/auxiliary covariances stays outside (D1) | 850-1300 |
  | L6-c | C21 `P:wave-two-variances` (integrated_wave_variance.tex 368-460): the purely spectral core with no input (finite orthonormal families, measures nu with ball growth C r^alpha, both directions, the h^(2 beta) form), plus a `_paper` wrapper whose link to E|l_R|^2 (E:variance-normalized-covariance, from B22, D1) and the unitary J (D8) are named inputs | PhaseBessel with H = H_a, MaskedContinuousWaveCompleted, FrequencyRow, MaskedAuxiliaryNorm (all done) | core same-assumptions; wrapper inputs-supplied, conclusion narrower (fallback: strong measurability of the H_a-valued kernel as a named input) | 800-1100 |
  | L6-d | C18 foundations and two results: the dilation floor lemma (positive Rayleigh value for potentials >= Gamma*z, using alpha < 2), Gamma(B_r) > 0, autocorrelation positivity from `Gamma_posdef`, the weak gradient of smooth tests, D8-lite half (b) "zero weak gradient implies zero"; `P:variational-unmasked-rate` (integrated_unmasked_variational.tex 98-111), Rayleigh-form part; `P:variational-positive-scores` (270-337) minus Q_2 | VariationalMean (mean_le, mean_lip, isRayleighTrial_mean_iff_paper), VariationalDilation, WeakSobolev | rate: same-assumptions, narrower (the operator half and lambda = sqrt(-E_s) stay out, D8; positivity floor by a different route than P:compact-original-common-trial, stated); positive scores: nonempty, v > 0, homogeneity, positive test input-free; boundedness of the score set is `S1Bdd` (see decision 1) | 1000-1300 |
  | L6-e | C19 `P:spatial-smooth-ratio` (integrated_spatial_occupation.tex 98-147) on a deterministic bound R_0 <= 2^(1+alpha) R_alpha (Fourier: |Q^|^2 <= min(1, 4b/|xi|^2), then `resolvent_homog`), with the manuscript's own "S1Bdd => R_0 finite" as a corollary; the S_1^pos display in the form "for every y below the bound some control exceeds y" | SpectralHomog.resolvent_homog, IsSpectralMeasure, toSchwartzMap; L6-d's autocorrelation positivity (stated over a hypothesis, instantiated at integration, as L5-b was) | same-assumptions; R_0 < infinity by a different route than the TeX (which derives it from S1Bdd), stated (fallback: R0Fin as one named input, weaker than S1Bdd) | 1000-1200 |
  | L6-f | C19 `L:spatial-static-controls` (40-96): (i) lambda_z positive, finite, Lipschitz; (ii) E:spatial-static-score in the existential form, plus its sSup form on S1Bdd | L6-d's floor lemma (over a hypothesis, instantiated at integration); TemporalEquilibrium (density, potential_eq_one); a smooth endpoint cutoff f_n | same-assumptions (positivity floor by the L6-d route, stated) | 700-900 |
  | L6-g | Series-type foundation (S_nu(x) = sum x^k/(k!)^nu <= e^{nu x^(1/nu)}, the beta < 1 Hoelder variant, r!s! >= (k!)^2, log k! bounds) and the S:temporal-type-continuity cluster: `L:positive-series-type` (main 7149-7190) in full; `P:moment-growth-logconvex` (7443-7499) and `C:static-moment-constant-continuity` (7501-7533) with every conclusion proved | Mathlib Gamma, convexity (`ConvexOn.continuousOn_interior`), NNReal.add_rpow_le_rpow_add (probed) | positive-series-type same-assumptions; the other two inputs-supplied (E:full-moment-coefficient-holder and the type/growth identification; P:static-minorant-lower and Lambda_p(0) = C_p) | 1000-1300 |
  | L6-h | `C:white-relative-width` (integrated_white_evaluation.tex 130-160) and `L:white-clock-laplace` (main 7572-7623) | TemporalEquilibrium.gamma_beta_duplication; Real.Gamma_eq_integral; Tonelli | same-assumptions, full (white-relative-width: Lean proves the inequality between the displayed formulas K_0(a) and M_a; that C_2 lies between them is T:white-moment-bounds, outside Lean) | 350-550 |

  Dependencies: L6-e and L6-f use L6-d's lemmas; they are stated over those
  lemmas as hypotheses and instantiated by the integrator (the L5-b pattern),
  so all eight run in parallel. Total about 5500-7700 lines.

  **Recommendation on stating C19 on `S1Bdd` (decision 1).** `S1Bdd`
  (BddAbove of {I_Psi - v_Psi/2 : Psi in C_pos}) is word for word the first
  claim of `P:variational-positive-scores` (unmasked TeX 272-274), so as a
  named input it is no stronger than the manuscript fact, once the Lean
  values are shown genuine (rate and cost integrable and finite, L6-d). But
  its manuscript proof (309-325) is stochastic twice over: `T:full-upper`
  (D1) and the raw-block point lower bound of `P:variational-remove-mask`,
  and Lean cannot show it is jointly satisfiable with H:homog. And it is
  avoidable for almost all of C19: L6-e proves R_0 < infinity
  deterministically, and the S_1^pos lower bounds hold input-free in the
  existential form (equivalent to the TeX whenever S_1^pos is finite).
  RECOMMENDED: do NOT make `S1Bdd` the foundation of C19. Prove R_0 < infinity
  deterministically (L6-e) and state the C19 bounds input-free; use `S1Bdd`
  only where the manuscript's object is the real number S_1^pos (the
  boundedness and homogeneity in `P:variational-positive-scores`, the
  sSup-form corollaries, and the manuscript-faithful "S1Bdd => R_0 finite"),
  record it in BOUNDARIES.md with its TeX provenance, and name
  `T:intrinsic-occupation-ceiling` as its later deterministic discharge
  (1500-2500 lines plus D8-lite, an L7+ item). Mathematical note for Le: the
  L6-e route makes R_0 < infinity independent of `T:full-upper`, for every
  Gamma in H:homog including singular ones.

  **B9 check (decision 3).** `C:white-relative-width` can be taken: its
  statement is about the two displayed formulas K_0(a) = 2^a/(1-a) and M_a
  of `T:white-moment-bounds` only (c and the spatial energy cancel); its
  proof uses only the duplication and recurrence of `L:equilibrium-gamma-beta`
  (formalized) and Cauchy-Schwarz in Euler's integral; it neither uses nor
  proves any part of B9's `P:white-spatial-energy` (the CDF square
  identity, H^1 profiles, the spatial energy constant).

  Decisions for Le inside this approval (defaults in brackets):
  1. `S1Bdd` scope: [as recommended above].
  2. The existential form of the S_1^pos lower bounds: [classified
     same-assumptions with a note; the sSup form appears as an `S1Bdd`
     corollary].
  3. `C:white-relative-width`: [taken, as checked above].
  4. L6-a's d = 3 Green measure through `Measure.toSphere`: [a definitional
     row; Fourier identity in d = 1 only, d = 2 as stretch, d = 3 deferred].

  Gates as in wave L5 (exact-hypothesis wrappers, refutations importing
  the package, Audit, claims/ledger/coverage, check-controls, comparator
  regeneration for every new theorem claim, lean-pkg receipts of both tiers
  at one commit with no edits in the checkout during the run, regate,
  `claims ledger` READY with 0 open; one Codex GPT-6.1-Sol correspondence
  review per item with a packet built from the declarations its rows name,
  plus a confirmation review; Easley `leanchecker --fresh` of the new and
  changed modules; Le closes the gate). Stopping condition: all eight items
  integrated and reviewed, or an item at its fallback scope with the
  remainder recorded as a named input; at most two repair rounds per item.

  Not in L6, with reasons: the C22 infinite-dimensional results (Mathlib has
  no Schatten classes, trace class, singular values of compact operators or
  min-max: a separate W3 foundation package, approximation numbers,
  2000-3500 lines, high risk); the first `T:full-upper` steps
  (`L:inventory-product` in full, the deterministic parts of
  `C:static-interaction` and `P:interval-coefficients`,
  `L:uniform-series-tail`; they reuse L6-g, proposed for L7); D8-lite half
  (a) (density of smooth compact functions in the weak-gradient H^1,
  600-900 lines) and with it the H^1 versions of `P:spatial-four-linear`,
  `P:spatial-energy-map`, `P:occupation-physical-class` (L7);
  `P:variational-remove-mask` (only consumer stochastic); the
  E:masked-actual-noise-norm identity (low value); everything needing D1,
  D5, D7 or full D8 (B22, `P:wave-square-columns`, the noise parts of
  `P:masked-noise-completion`, C2, C9). B3, B4, B9 stay reserved.
- **Easley external kernel replay (2026-11-10): PASS 35/35** at companion
  837778a (the wave-L2 library; sources byte-identical through 64070a7):
  every module and the umbrella replayed by its own `lake env leanchecker
  --fresh` run (exit 0, empty output), which re-checks every imported
  Mathlib declaration too. Jobs 5685763 (pilot), 5685781 (all targets, 6
  in parallel), 5688166 and 5688359 (reruns); six runs first died after
  about 7 s with "Too many open files in system" (about 65-72k open files
  per --fresh run; six in parallel reached the node limit), an environment
  failure, and passed when run one at a time. About 10.9 h single-thread;
  peak 7.7 GB. Evidence: companion 687e631,
  verification/leanchecker-easley-2026-11-10/ (HPC username redacted).
  Not covered: the wave-L3 modules (need a new replay).
- **H:homog and zero covariance (asked #3 at Le's request; #3 answered
  2026-11-10 at Article 66117c2):** the Lean model admits Gamma = mu = 0,
  and so does the TeX, INTENTIONALLY. (a) Do not add Gamma != 0 to H:homog:
  at zero covariance W = 0, u = 1, every moment is 1 and every rate 0;
  E:kappa and E:driver-parameters depend only on the parameters.
  (b) Zero is permitted by E:kappa, E:driver-parameters, P:mixed,
  P:mild-construction, T:intro-upper/T:full-upper, P:Jensen (equality),
  T:intro-second-moment/T:intrinsic-second-moment (C2 = 0 at zero).
  Strict positivity statements carry their own local or section-level
  Gamma != 0: L:compact-raw-profile, P:compact-original-common-trial,
  L:variational-heat-envelope, P:variational-unmasked-rate,
  P:variational-positive-scores, P:spatial-smooth-ratio,
  P:spatial-energy-map, P:raw-block-original-lower, Appendix D's
  P:static-minorant-lower, P:near-static-mean-gap,
  P:moment-growth-logconvex, C:static-moment-constant-continuity;
  C:white-relative-width needs c > 0; P:clock-copy-obstruction also states
  Gamma != 0 itself. All formalized results (waves L1, L2) need no global
  nondegeneracy. One wording issue: T:first's strict comparison E_* < E
  must not be asserted at Gamma = 0. (c) No TeX or Lean change made. #3
  recommends, for Le's manuscript decision: a short zero-covariance remark
  right after H:homog, and an explicit nonzero qualification on T:first's
  strict source comparison. Keep H:homog and the accepted Lean model; any
  approved statement change gets the usual correspondence check. Lean
  consequence: whole results whose statements need Gamma != 0 must carry
  it as an explicit hypothesis (as P:clock-copy-obstruction does).
- **975feb3 RE-ANCHOR: CLOSED (Le, 2026-11-11)** at companion d40f394
  over manuscript 975feb3: Le accepted the narrow Codex re-check of the
  H:homog rows (attempt v2, PASS/high) as closing it; recorded in the
  companion README at 3a7d57f; #3 and #24 told. Record: at Le's request #3 committed the zero-covariance
  remark after H:homog (main TeX 209-214) and the Gamma != 0 qualification
  of T:first's strict comparison (426-432) at Article 975feb3.
  - Re-anchor (companion c308c82 docs, d9e5ce9 comment/summary line
    shifts): all 150 cited labels exist once, same file; 145 identical up to
    whitespace and braces; exceptions T:full-upper (cross-reference only,
    cited as outside) and four S: sections (prose). 754 line citations
    mapped, 362 moved. d40f394 fixes two pre-existing off-by-ones
    (SpectralHomog 7646->7647 incl. ChallengeDefs copy; WaveKernel
    817->810). Build, CheckFidelity 611/611 and claims check pass.
  - Receipts at d40f394 (companion 1254720): comparator pass (611
    theorems); lower tier 0 sorry, 724 claim axioms, standard axioms only
    (peak 7.2 GiB). A first lower-tier run was refused by lean-pkg because I
    edited coverage.yaml in the working tree during the run (nothing
    written; re-run clean). Re-gated verified-private 2f5ee14 -> d40f394
    with comparator evidence; claims synced; `claims ledger`: READY, ok,
    513 required, 709 verified, 0 open, 15 out-of-scope (internal helper
    definitions).
  - Codex GPT-6.1-Sol narrow re-check (6 checks: anchor paragraph,
    HomogHypothesis section, every H:homog consumer row, line citations,
    T:full-upper, no new error) at d40f394 over 975feb3: attempt v1
    INCONCLUSIVE/medium only because the packet lacked DampedNorms.lean
    (row checked by hand: no Gamma != 0 needed); attempt v2 with all 27
    modules PASS/high, no findings, no repairs. Evidence and ADJUDICATION.md:
    reviews/2026-11-11-lean-reanchor-975feb3 (Article 8df16e1).
  - Docs after the receipts (bound by docs-only descendants): 6633243
    docs/coverage-scope-tex.yaml (LaTeX forms of the three narrower-scope
    sentences for #24's Appendix F; coverage/1 rejects an extra row key);
    31441aa README verification record at d40f394 and the re-anchor note.
    Easley replays not repeated: the Lean sources differ from 2f5ee14 only
    in doc comments. Article commits after 975feb3 (to f4cd8d4) touch only
    preface/Appendix E files, none cited.
  - Open: lean-pkg `coverage check NAME`
    reports 487 comparator theorems named by no coverage row (rule R10/R11
    for a rendered scope page; pre-existing since the comparator tier, the
    offline check skips it; gate and ledger unaffected), sent to lean-ops.
- **Next:** Easley external kernel
  replay (leanchecker --fresh per module) of 837778a (Lean sources
  identical to 79afdde) in progress; human statement read (A1) still
  recommended; remaining W1 board items (excluding the reserved B3, B4,
  B9); W2/W3 need foundations.

- **Standalone local checks (current, 2026-11-09):** 87 accepted finite
  facts in 26 local seams. The latest promotion added three concrete
  colored-vector Gaussian word facts and promoted two earlier provisional
  generic word facts after the completed actual-application review (see the
  last 2026-11-09 log entry and `local-checks/colored-vector-word-v1/`).
  Analytic inputs (H1/CDF, integrals, suprema, attainment, Gamma, PDE,
  complex/background/Bochner bridges) remain informal and outside the
  kernel. These are the development record; the public companion packages 23 of
  the 26 seams (see above). The earlier 80/22 snapshot is superseded history.

## Releases (append-only)

### Release v0.9.0  [LINKED]  opened and closed: dates not recorded here
- Scope: the wave-L9 state of the companion. Public: `github.com/chenle02/stratonovich-ham-second-moment-lean`, tag `v0.9.0` on `6cc04c1`; DOI commit `0966ef6`.
- DOI: version 10.5281/zenodo.24199105, concept 10.5281/zenodo.24199104.
- Other fields: not recorded here (see `RELEASE-PLAN.md` and the companion's README).

### Release v0.10.0  [LINKED]  closed 2026-11-16 (public), linked 2026-11-18
- Scope: waves L10 to L14 (gates L13/L14 at dev `8f51004`), re-anchored to book R `39f2597a`.
- Release tree: public `c8d8e07` (tree of dev `09cfc11`); receipts `4fbbb89`; docs `261cc68` = tag `v0.10.0`.
- PI approval: Le accepted v0.10.0 at `261cc68` (2026-11-16) and gave the go for the flip.
- Public: tag `v0.10.0`; later docs-only commits on main up to `d659c59` (G note, arXiv pin `arXiv:2611.23014v1`, book site and concept DOI links).
- DOI: version 10.5281/zenodo.24295453, concept 10.5281/zenodo.24199104.
- Links: site on gh-pages (`a265332`); lean-pkg registry public, promoted at `dc46f3a` (2026-11-18); book Appendix F pins it (coverage `142afced`, receipt commit `c8d8e07`).
- Next: v0.11.0 (L15) only on Le's word.

## Planned waves (strategy in ROADMAP.md)

| Wave | Target | Opens when |
|---|---|---|
| L1 | The finite combinatorics of Gate G0: pair-partition counts for the two-chain integrals and the counting argument that decides whether Theorem 3.1 reaches the scale t^κ | G0 verdict written in the notes |
| L2 | Laplace-to-time growth lemma (Mittag-Leffler / Tauberian conversion) with the analytic inputs as explicit hypotheses; reusable | G2 route fixed |
| L3 | Scalar/algebraic deductions of the G:upper and G:sharp proofs (constants, exponents, the factor 2^{1/(3-α)}) | the corresponding paper proofs reviewed |

## Wave log (append-only)

| Wave | State | Date | Evidence |
|---|---|---|---|
| L15 | CLOSED | 2026-11-20 | L15-UM scope (a); gate dev `18c5c1d` (tag `L15-gate`), receipts `4648b3c`, Easley `c081b0d`, docs `54d3313` on dev main; see the wave record |
| L16 | CLOSED | 2026-11-20 | Cameron-map chain; gate dev `ebac849` (tag `L16-gate`), receipts `2d34d33`, Easley `c4df976`, docs `ca75d10`/`108fa80`/`5f0d8c8`, COMPLETION `38ac748` on dev main |
| L17 | OPEN (approved by Le) | 2026-11-20 | Pairing-envelope chain; launched on <MACHINE> from dev main `38ac748` after the L16 gate |
| L17 | CLOSED | 2026-11-21 | Pairing-envelope chain; gate dev `68d0c5e` (tag `L17-gate`), receipts `d1a3a12`, Easley `0bf7a39`, docs `a34a5eb`/`be81d6e`, COMPLETION `02f922f` on dev main |
| L18 | APPROVED (Le) | 2026-11-21 | Spatial Wick measures + deterministic half of `L:joint-fixed-order` + `DiagramLimits` discharge; default answers to all thirteen decisions; probes, then L18-0 on <MACHINE> from dev main `02f922f` |
| L18 | CLOSED | 2026-11-21 | Wick-measure chain; gate dev `6e4644d` (tag `L18-gate`), receipts `afd018d`, Easley `eb19140`, docs `a83c778`/`aad8b91`, COMPLETION `470ee26` on dev main; `DiagramLimits` discharged |
| L19 | OPEN (approved by Le) | 2026-11-21 | L^2 construction + `P:mixed` + `L:vertex-crude`; discharge of `MixedMoment` and `FirstMomentSeries`; L19-0 launched on <MACHINE> from dev main `470ee26` |
| L19 | CLOSED by Le (merge pending receipts) | 2026-11-22 | gate dev `fe9f1de`; Easley `a330722`; docs `e6e1cb1`/`487872f`/`b994fc0` |
| L20 | APPROVED (Le) | 2026-11-22 | `P:mild-construction` + Riesz instance + deferred wrappers + docstring pass; L20-0 after the L19 merge and tag |
| L0 | PROPOSED | 2026-10-26 | Setup by session #4; no Lean code yet |
| L0 | PROPOSED | 2026-10-28 | Readiness/strategy refresh after source and plane-endpoint reviews; creation approval still pending, no package or Lean verification |
| L0 | CLOSED | 2026-11-09 | Companion created and registered (verified-private at 38d1616); 23 seams packaged, 3 GaussianChaos seams withheld; manuscript anchor cf979d6 |
| L2 | CLOSED (Le) | 2026-11-10 | Three whole results (C26, B23, B24); verified-private at 79afdde; reviews/2026-11-10-lean-wave-l2-* |
| L3 | CLOSED (Le) | 2026-11-10 | Four items (B6, B16, B14 with a D4 slice, C22 finite slice); gate at companion dfc2fe8 over 3920258; reviews/2026-11-10-lean-wave-l3-* |
| L4 | CLOSED (Le) | 2026-11-11 | Four items (masked spectral growth and B14 input discharge, time-Schur and masked modulation, frequency row, occupation kernel row); gate at companion ac6f767 over 3920258; reviews/2026-11-11-lean-wave-l4-* |
| L5 | CLOSED (Le) | 2026-11-11 | Six items (H_a completion with B24 at same assumptions, masked continuous wave, masked auxiliary norm, rest of the damped-norm lemma, heat envelope and global mean, phase Bessel); gate at companion 712c307 over 975feb3; reviews/2026-11-11-lean-wave-l5-* |
| L6 | OPEN (approved by Le) | 2026-11-11 | Eight items (wave Green measure, quotient obstruction and finite Gaussian comparison, wave two-variances core, variational foundations and two C18 results, deterministic R_0 and the smooth ratio, static controls, series-type cluster, white relative width and clock Laplace); defaults for the four decisions |
| L6 | CLOSED (Le) | 2026-11-11 | Eight items integrated (14 modules); gate at companion bfa2fd0 over 975feb3 after eight reviews, a confirmation (C1 repaired) and a clean narrow re-confirmation; reviews/2026-11-11-lean-wave-l6-* |
| L7 | OPEN (run overnight under Le's instruction) | 2026-11-11 | Six items (inventory product, uniform series tail, H^1 density, spatial four-linear and energy map, occupation physical class, interval/static scalar steps) plus two completion modules |
| L7 | CLOSED (Le) | 2026-11-12 | Gate at companion f3be834 over a284420 (with the re-anchor from 975feb3); six reviews, confirmation, re-anchor re-check and confirmation; reviews/2026-11-11-lean-wave-l7-*, reviews/2026-11-12-lean-* |
| L8 | PROPOSED | 2026-11-12 | Eight items: R_alpha identity; damped-norm lower bounds and smoothing claims; S1Bdd discharged deterministically (two agents); spatial bracket for S_2^pos; mask removal; finite Wick foundation and L:terminal-wick; symplectic-free core; static-phase Cauchy steps; awaiting Le's approval |
| L8 | OPEN (approved by Le) | 2026-11-12 | Defaults for the six decisions; nine agents launched; Easley L7 replay submitted via <MACHINE> |
| L9 | PROPOSED | 2026-11-12 | Seven items (+1 optional) to run on <MACHINE>: exact occupation ceiling (A1, A2), Hermite/Fock foundation and consumers (H1, H2), wave Green Fourier d = 2, 3 (G), L:phase-contractions (P), L:low-alpha-convolution (L); awaiting Le's approval |
| L9 | APPROVED (Le) | 2026-11-12 | Default decisions; launches on <MACHINE> after the L8 integration commit |
| L10 | PROPOSED | 2026-11-12 | Independent cores on <MACHINE> (higher-Riesz d = 2, white-model prerequisites, fixed-split core, alpha-one convolution); dependent assemblies after L8/L9; awaiting Le's approval |
| L10 | OPEN (approved by Le) | 2026-11-12 | Defaults; R2, W0, FS0, A1 launched on <MACHINE>; FS1, W1, R3, A1i wait for their inputs |
| L11 | PROPOSED | 2026-11-12 | Easley array gate (build + pilot, then one --fresh target per task, about 1.5 h for about 90-101 targets) and formalization candidates K1-K9 on <MACHINE>/<MACHINE>; awaiting Le's approval |
| L11 | APPROVED (Le) | 2026-11-12 | Defaults; Easley build + one-task pilot via <MACHINE> at the L8 integration commit once its receipts exist; K1-K9 scoped after L9/L10 |

## New proof seams retained for later statement fences

See ROADMAP.md for exact proposed roles and analytic exclusions. These are
planning items, not opened Lean claims:

- Section9 product-endpoint interval algebra and affine coefficient exponents
  (the full moment review remains all14PASS/medium, below HIGH).
- The accepted plane-endpoint parameter algebra and finite positive-sum
  comparison, with covariance/Holder inputs explicit.
- The exact rational separation used by the independently checked source
  normalization audit, with its functional bounds as named hypotheses.
- Static p2 factor-two algebra, keeping the imported coefficient rate and
  its time-independent order threshold outside a pure arithmetic claim.

The existing creation proposal and initial G0 statement fence are unchanged.
Before execution, renew registry/Mathlib reuse searches and compatible release
pins, then use a private registered package and lease after approval. This
ledger update is not a workaround for the creation gate.

## Standalone local verification authorized by Le (2026-10-29)

Clock-filter pilot:three statements compile using read-only pinned dependencies.
Exact public types/standard-three axiom audit pass. Fresh owned-source replay
passes;three false controls fail semantically. Two development failures are
preserved. Analytic input is explicit and the measure need not be finite.
Evidence:local-checks/clock-filter-v1/local-receipt.json. Independent exact-type/
application correspondence passed4checks/HIGH,source86de3d8,112.922s. This pilot does not create the proposed
companion,claim a package gate or open a cluster job. L0 remains PROPOSED.

Local clock-filter close:source unchanged after review;all three public types
and standard-three axiom lists exact. Concrete positive-lambda measure facts
are hand-checked,not instantiated inLean. Density total extension is zero
outsidepositive lambda;measurability/integrability and K/J representations
remain analytic inputs. See correspondence-adjudication.md for all five minor
notes and both preflight failures. No new companion/package gate is claimed.

## Standalone terminal-cross local pilot (2026-10-29)

Five scalar statements compile with only standard axioms;owned-source replay
and four meaningful false controls pass. The strict finalconsumer includes
its real square root and positive denominators. The positive47termcertificate,
rate bound and exponentialconvexity support a NEWanalytic white terminal-cross
comparison. Exact type/application review passed in the6PASS/HIGHanalytic gate at6475ea0. This is a standalone local
pilot,not an opened companion/package/lease/cluster wave. L0remainsPROPOSED.
Evidence:local-checks/terminal-cross-v1/local-receipt.json.

Terminal-crossclose:all five scalarpublictypes/applicationpassed6HIGHreview,
280.956s. Proofsourceunchangedafterreview. Rootadded2actualconsumerFalse
controls afterreview (total6;reviewer saw4),documented as such. Analyticwave/
clock/mixtureidentities remaininformal proofs. Evidence/type boundary at
local-checks/terminal-cross-v1/local-receipt.json. L0companionunchanged.

## Local middle-cross pilot (2026-10-29)

The actual two-root consumer U<I for b>=1,c>1, root parameterization and
300-term identity compile cleanly with standard axioms. Fresh owned-source
replay and five definition-level False controls pass. Initial compile/setup
errors are preserved. Seven public facts reuse read-only pins; no new
companion, package, lease, registry, cluster or Comparator gate is opened.
Analytic/type/application review passed six groups / seventeen checks HIGH
at e638186. The formal proof source is unchanged after review. Evidence:
local-checks/middle-cross-v1/local-receipt.json. L0 remains PROPOSED.

## Projection-residual scalar pilot (2026-10-29)

Two paper-specific rational/square-root and affine-consumer statements are
fenced before execution. Analytic projection/mean comparison remains a
candidate. Existing local standalone authorization only; L0 remains PROPOSED.

Projection-residual local gate: two actual scalar facts compile cleanly;
exact types/live standard axioms, fresh owned-source replay and two semantic
False controls pass. One division-API failure is preserved, with unchanged
public signatures. Analytic/type/application review remains pending.

Projection-residual: exact two scalar types/application passed the primary
six-check HIGH review at efbdbd9. Formal source unchanged. Analytic common-
noise regularization clarification has a focused source/limit followup
pending; no companion or package wave.

Projection-residual close: source/limit clarification passed2groups/9checks
HIGH at1787644, in addition to the primary6HIGH gate at efbdbd9. Both formal
proofs unchanged. The Gaussian/projection/mean arguments remain informal
reviewed analytic inputs. L0/PROPOSED and package-creation decision4 unchanged.

## Direct-event scaling/gauge pilot (2026-10-29)

Seven actual real-power and scalar2x2matrix consumers are fenced before
execution. Full-model analytic scaling and scalar calibration remain
candidates. No new companion/package/lease/registry/cluster; L0 unchanged.

Direct-event local gate: all seven actual scalar/matrix facts compile cleanly,
exact public types/live standard axioms and fresh owned-source replay pass.
Three current semantic controls fail on False; initial warning-only success
preserved with unchanged public signatures. Analytic/type application pending.

Direct-event close: all7actual scalar/matrix types/application passedC6of
the seven-check HIGH review at9d77f90. Proof source unchanged. Gaussian/
Green/series scaling and scalar ODE/Floquet/Holder inputs are informal
reviewed proofs; rough-SPDE event/stability remains open. L0unchanged.

## Phase-response pilot (2026-10-29)

Five actual phase/Gram/error-window deductions fenced before local execution.
Analytic spectral/HS claims remain candidates. No new companion/package; L0
unchanged. The window input is the computed analytic error bound, not the
open sharp/event target.

Phase-response gate: all5facts compile cleanly; public types/live standard
axioms, owned-source replay and4semantic False controls pass. Initial unused-
hypothesis-name warning preserved; hB->_hB only, propositions unchanged.
Analytic/type application pending; no package/companion wave.

Phase-response pilot now adds a sixth balanced-endpoint budget before the
final gate; the five existing proposition types are unchanged. Analytic
endpoint logarithms and spatial-average moment transfer remain unformalized
new review obligations.

Final phase-response gate: all6facts compile cleanly, exact public types/live
standard axioms and owned replay pass,4semantic controls. Three executions
record the warning/binder cleanup and actual balanced budget addition; no
old proposition weakened. Analytic/type/average application pending.

Phase-response close: all6finite scalar/Gram/rpow application types passed
C6of8HIGH at0ae116c. Formal source unchanged. Gaussian/Sobolev/HS/averaging
arguments remain informal reviewed proofs; time-driver/all-order/event and
source-constant consumers remain open. L0anddecision4unchanged.

## Interaction-driver pilot (2026-10-29)

Eight finite Gaussian-prefactor/variance/rpow/Holder/box consumers fenced
before local execution. All Gaussian/kernel/path/convergence/max analytics
remain candidate obligations. No new companion/package/lease/registry/donor
write/cluster; L0unchanged.

Interaction-driver gate: all8finite facts compile cleanly; exact public types,
live standard axioms, owned replay and5semantic False controls pass. A failed
redundant tactic is preserved, no statement changed. Duplicate setup refused
before overwrite, terminal state inspected. Analytical/type gate pending.

Interaction-driver close: all8finite types/application passedC7of9HIGH at
b398b77. Formal source/statements unchanged;5semantic controls retain their
exact scopes (normalization control hard-codes its reduced abstract case).
Gaussian/convolution/HS/source-cutoff/path/box arguments remain informal
reviewed proofs. All-order/global-or-ulocflow/event/constant/higherdims open.
L0anddecision4unchanged.

## Local-flow pilot (2026-10-29 local date)

Seven finite mask-order/Schur/source-budget consumers compile/replay with
standard axioms and3semantic controls. Warning-only unnecessary sequencing
v1preserved;v2clean, all statement signatures unchanged. All5owned/replay
compiler output hashes match; binary auxiliary outputs are archived, not
decoded as text. Analytic/source/type application pending. Existing eight
InteractionDriver deductions reused unchanged. No new package/companion.

Local-flow close: all7new finite consumers passed C12of13HIGH atd020a2a;
8previous InteractionDriver deductions reused with exact types/pins/receipt.
Formal source unchanged. Uniform-in-p dyadic lower margin remains analytic,
not supplied by only-positive-margin Lean facts. No formal SPDE/Young/
canonical-source/event theorem or package gate. L0anddecision4unchanged.

Lean-ops answered6a7b18143738: minimal committed Lake project enables
source-bound systemd/check receipts without registry; manual evidence stays
project-owned. Optional migration not performed. Separate exact defaultCLI
2.1.314read-ledger compatibility friction a73f556e4e30delivered; dry-run only,
no provider, no gate weakening; current scientific review used2.1.304.

Shared-library metadata followup2026-10-29local: registeredcoefficient-
<PRIVATE-PACKAGE> now points to <PRIVATE-PACKAGE>. Gated7f27788/
evidence5393594checkedread-only; all9Lean files identical to oldd5fde707/
75d9781, pins unchanged, offline receipt20PASS. No Lean/gate/network
execution in that parser, no confidence upgrade of earlierMEDIUMmathreview,
no change to owned45deductions/L0/PROPOSED or package creation decision4.
See coordination/2026-10-29-agent8/factorial-successor/.


## Joint-tilt local pilot (2026-10-30)

Four new finite algebra consumers in local-checks/joint-tilt-v1: Gaussian-MGF
exponent cancellation, wrong-sign and wrong-cost errors, and actual positive-
delta real-power amplitude quotient. No Gaussian MGF/measure/flow theorem.
Clean original/replay compilation, exact public types and standard3axioms;
five owned output hashes match;3altered numerical statements reduce to False.
Raw41member archive hash/member verified. Independent type/application review
PENDING with the full candidate scientific tilt consumer. Prior45deductions
retain their exact earlier gates; total49local finite deductions, not49accepted
new claims. Official latest stable Lean4.35.0/Mathlibv4.35.0 pin56a0058 checked
against the existing read-only donor; no dependency migration or donor write.
L0/PROPOSED, companion decision4 and all package/registry gates unchanged.

Joint-tilt C7type/application gate now accepted8PASS/HIGH within the full
scientific tilt review, sourcee51432c. All4formal sources unchanged;49local
finite deductions retain their exact scoped gates. No formalGaussian/SPDE,
companion or official package gate is inferred. Evidence/adjudication in
reviews/2026-10-30-joint-gaussian-tilt/.


## Moving-cone local scalar budgets (2026-10-30)

Three finite deductions for residual contraction, positive amplitude/cone
conversion and terminal-observable margin compile/replay cleanly on latest
stable Lean/Mathlib4.35.0. Exact public types/live standard3axioms and
three semantic False controls checked; five owned output hashes match.
Evidence local-checks/moving-cone-v1/. Analytic operator/cone/field theorem
not formalized. Independent type/application scientific review pending.
No package/companion/lease/registry/HPC transaction; L0 remains PROPOSED.

Moving-cone local close: full analytic/type/application review atabfdab4
passed17groups/HIGH,292.758seconds,24text delivery complete. Three exact
scalar types and actual applications accepted; all formal source unchanged.
Raw source/replay/standardaxioms/3numeric False controls retain local-only
status; no package/Comparator or formal analytic cone/SPDE theorem.


## Actual event local arithmetic (2026-10-30)

Two actual consumers compile/replay cleanly on pinned latest stable4.35.0:
finite scalar error accumulation for alln and normalized moderate-density
real-power identity. Exact public types/live standard3axioms and2numeric
False controls checked; all5owned outputs match. Evidence in
local-checks/actual-event-v1/. Operator recurrence uses finite identity
extension; its analytic derivation and all probability/source/flow inputs
remain outsideLean. Independent exacttype/application review pending.
No package/companion/lease/registry/HPC; L0 remains PROPOSED.

Actual-event local close: full scientific18groups/HIGH atd5dcd46,
379.671seconds/24texts, no mandatory repairs. Both exact finite public
types/live standardaxioms and actual recurrence/penalty applications
independently checked. Lean sources unchanged; fence clarification was
post-execution and fully in review. Local receipts remain no-package/
no-Comparator/no-formal-analytic-event evidence; L0/PROPOSED unchanged.


## Raw variational local power identities (2026-10-30)

Four public scalar consumers compile/replay cleanly at latest stable4.35.0:
dilation potential/variance exponents, label-score scaling, positive-score
witness and strict label2factor. Complete public types/live standard3axioms,
3numericFalse controls and5ownedhashmatches checked. Initial compile/audit
reached finalhashguard but server artifact differed with two lint warnings;
attempt preserved, successor removes only2unnecessary tactic combinators
and all4public types match. No gate weakened or linterdisabled. Evidence
local-checks/raw-variational-v1/. Independent exacttype/application review
pending. No formal covariance/spectral/supremum/event or package theorem.
L0/PROPOSED/privatecompanioncreation decision unchanged.

Raw-variational local close: scientific20groups/HIGH at0fd2a05,
280.82seconds/29texts+1image,no mandatory repairs. All4complete types/
live standardaxioms and actual exponent/score/positive/strictfactor
applications independently checked. Formal sources unchanged. Both
warning/server refusal and clean5output replay retained; local only,
no formal covariance/spectral/supremum/SPDE or package/companion theorem.


## General positive-profile analytic bridge (2026-10-30)

No new kernel declarations. Actual nonseparable family S1-S3scientific
gate27PASS/HIGH atc0a0093/379.661seconds/22texts+8sourceimages supplies
analytic inputs only. Uniform Rayleigh/maxmin, ODE weightedtails, local
Fduality, fractional spectral calculus and physicalFtransfer are NOT
formal Lean results. Building these foundations was excluded by value
rank; no axiomatized desired-complement shell. Existing finite cone/
power budgets may be reused at exact checked next-consumer applications.
58finite declarations/12localseams unchanged; L0/PROPOSED, no package/
companion/lease/registry/cluster/Comparator transaction.


## General-positive consumer application close (2026-10-30)

Scientific12c9879,24groups/HIGH,462.611seconds,34texts,no requiredrepairs:
all nine unchanged MovingCone/ActualEvent/RawVariational publictypes and
NEWactualgeneral-profile/class applications independently checked.
Source/type/receipt/replay bindings retained, no rebuild needed or claimed
for unchanged internals. Complete individual hypotheses in consumer
scientific-adjudication-v1.md. Root also executed exactproxyJSON controls.
58finite declarations/12seams unchanged; no formal spectral/Young/Gaussian/
probability/supremum or SPDE theorem and no official package/companion/
lease/registry/cluster/Comparator transaction. L0/PROPOSED unchanged.

## Occupation-form finite seam provisional (2026-10-30)

Two new local real inequalities potential_budget/shifted_coercivity compile,
audit and freshownedreplay cleanly on lateststable4.35.0/Mathlib56a0058
(officialGitHublatestreleaseJSON checked). Completepublictypes/std3axioms,
fiveartifacthashmatches andtwoactualFalsecontrols verified. Attempt01
serverhashrefusal with redundanttacticwarning preserved; attempt02 removes
only <;>, publictypes identical, zero warnings; guard unchanged. Bothnative
archives allmembers verified. Evidence local-checks/occupation-form-v1/.
60finite declarations/13localseams now provisional, no form/Sobolev/density/
Bochner/rate/SPDE certificate. Actual newapplication review stillREQUIRED;
no package/companion/lease/registry/donor/HPC/Comparator transaction.


Occupation-form application close: scientific80e47d6,8groups/HIGH,
272.897seconds,25texts,no requiredrepairs. Both complete publictypes,
standardaxioms and actual(8)/(10) formbudget applications independently
checked, including analyticpremises. Nativebinaryversion4.35.0/commiteb6cafb
and bothFalsecontrol logs rootrechecked; all nativearchives verified.
60finite deductions/13localseams now scopedaccepted at their exact gates.
No formal Sobolev/H1form/Bochner/core/density/supremum/SPDE theorem or
package/companion/lease/registry/HPC/Comparator transaction. L0/PROPOSED.

## Raw-value scalar seam provisional — 2026-10-30

Two newlocal lemmas exact_gap(Natlargeintegercertificate) andstrict_log_gap
(actualReal log/strictconvexityscalar) compile/audit/freshreplay cleanly
at4.35.0/Mathlib56a0058; officialreleaseAPI both4.35.0 rechecked. Complete
publictypes/actualstandardaxioms,5matchingownedartifacts,2Falsecontrols.
Initialprojection-namedargs localcompileFAIL retained; routineproofsyntax
repairbinds existingfunction beforearguments,no statement/gatechange.
Evidence local-checks/raw-value-ceiling-v1/.62declarations/14localseams
provisional; exactanalyticapplications remainforindependentscientificgate.
No formaloccupationenergy/covarianceCS/valueceiling/source/SPDE or package/
companion/lease/registry/HPC/Comparator transaction. L0/PROPOSEDunchanged.


Rawvalue scalar application close: scientificad6c188,8groups/HIGH,
322.118seconds,26texts+4images,no requiredrepairs. exact_gap/strict_log_gap
completepublictypes/stdaxioms and actualSection5applications independently
checked; analyticNatcast/log/domain conversion remainsoutsidekernel.
Rootversion4.35.0/eb6cafb andMathlibv4.35.0tag->56a0058/Falsegoals/archives
rechecked.62finite deductions/14localseams scopedaccepted. No formal
energy/covariance/spectral/valueceiling/SPDE or officialpackage/companion/
lease/registry/HPC/Comparator transaction. L0/PROPOSEDunchanged.

## Damped-lower point scalar seam provisional — 2026-10-30

3locallemmas exact_margin/pi_cube_certificate/rational_pi_gain compile,
audit/freshownedreplay cleanly on4.35.0/Mathlib56a0058,latestofficialAPI
verified. Completepublictypes/std3axioms,5matchingartifacts,2Falsecontrols.
Clean2declpilot retained; successorADDSstrongerRealratioforactualzeta,
first2typesunchanged, bothnativearchives allmembersverified. Evidence
local-checks/damped-lower-v1/.65finite deductions/15localseams provisional.
Gamma/Beta/staticcontrol/sourceenergy/pointlower analyticapplications
remainforindependentfullgate. No package/companion/lease/registry/HPC/
Comparator transaction, L0/PROPOSEDunchanged.


Dampedlower application close: scientific8883160,7groups/HIGH,
295.426seconds,28texts+2images,no requiredrepairs. Threecompletepublictypes
and actualSection5Natcast/positive-ratio/pi applications independently
checked; analyticGamma/Beta/static/dampedenergy/point assembly notformal.
Rootversion/tag/Falsegoals/archives rechecked.65finite deductions/15local
seams scopedaccepted. No officialpackage/companion/lease/registry/HPC/
Comparator transaction; L0/PROPOSED anddecision4 unchanged.

## GlobalOmega exact rational core provisional — 2026-10-30

Fournewpublictheorems plusactualpublicQ/D/Vdefinitions compile/audit/
freshreplay at4.35.0/Mathlib56a0058: two16term positivequartercertificates,
Qpositive and ACTUALrationalV<1. Completeprinteddefs/types/std3axioms,
5matchingartifacts,2Falsecontrols. Initialdenominatornormalizationcompile
failure preserved; canonicalnonzerofacts added,no publicstatementchange.
CAS/Leangeneratorreplay byteidentical andsource matchesreceipt; bothnative
archives memberverified.69finite deductions/16localseams provisional.
Independent actualGamma-envelope/applicationreview required, no formal
Gamma/kernel/energy/globalOmega/SPDE or package/companion/HPC theorem.


GlobalOmega finitecore application close: scientificee188ab,7groups/HIGH,
447.816seconds,31texts+2images,no requiredrepairs. Fourpublictheorems,
actualQ/D/Vdefinitions/completepp.alltypes/std3axioms andallactualanalytic
applications independentlychecked. RootCAS/generator/v2replay, sourceSHA,
fiveownedoutputs, actualFalsecontrols and11/30filearchives reverified.
69finitefacts/16localseams scopedaccepted; Gamma/kernel/actualpoint proof
NOTformalizedbythoselemmas. No officialpackage/companion/lease/registry/
HPC/Comparator transaction; L0/PROPOSED/decision4unchanged.

## Dimensional fullphase matrix provisional — 2026-10-30

New1public full_interaction theorem/3actualmatrixdefs compile/audit/fresh
replay cleanlyat4.35.0/Mathlib56a0058,officialreleaseAPIchecked. Complete
pp.alldefs/type/std3axioms,5matchingartifacts,1Falsecontrol. Initialtwo-
upperentry negationnormalizationcompilefailure retained; ringaddedonly
onremaininggoals, no statement/guardchange. Botharchives memberverified.
Evidence local-checks/dimensional-matrix-v1/.70finitefacts/17seams
provisional. TwooldPhaseResponse kernels reusedunchanged,newcontext
applications awaitgate; no newFourier/HS/Gaussian/flow/SPDE/packageproof.


Dimensionalmatrix application close: scientific0743b2d,8groups/HIGH,
407.368seconds,26texts+2images,no requiredrepairs. Newfullphasepublicdefs/
type/Std3axioms andactualpositivefreqapplication checked; twoOLDscalar
kernel NEWcontextbindings/hypotheses independentlychecked. Rootnewsource/
5artifactpairs/Falsegoal/archives andoldsource/fulltypes reverified.
70finitefacts/17seams scopedaccepted. No formalFourier/HS/covariance/
SPDE or officialpackage/companion/lease/registry/HPC/Comparator gate.

## Finite weighted natural-power seam proposed — 2026-10-30

After independent finiteGaussian STATEMENT gate19checks/HIGH207.904s,
propose standalone1lemma N2: allnaturalL>0,q<=L, realx/y, absoluteinteger
powers and realcastweights. Exact pinned Mathlib weightedAMGM found/reused;
bounded registry/public prior-art receipts retained, missing7checkouts and
cappedGitHub not absenceproof. Localtype/compile/replay/threeFalsecontrols
pending, no newclaim fromplanned run. No officialpackage/companion/lease/
registry/HPC; L0/PROPOSED and PROJECT decision4 unchanged. NewGaussian/
trace/continuum arguments not formalized by this finite seam.

## Finite weighted natural powers provisional — 2026-10-30

One public weighted_natural_powers consumer compiled/audited/freshreplayed
at4.35.0/Mathlib56a0058 with exact Mathlib weightedAMGM reuse,5 matching
artifacts,3 actualFalse controls (zeroL, invalidq range, signedpower).
Complete separate pp.allTYPE/standard3axioms printed againstboth modules,
byteidentical. First attempt compiled/audited but private/server bytes
mismatched;51nativefiles preserved. Samepublicheader successor replaced
field_simp with explicit cancellation, fresh5matches; root cause of first
serializer difference not asserted. Second63nativefiles memberverified.
71localfinitefacts/18seams PROVISIONAL pending full exacttype/application
review. No Gaussian/trace/Schatten/continuum/operator/SPDE formal theorem.
L0/PROPOSED/decision4 unchanged, no officialpackage/lease/registry/HPC.

FiniteYoung application close: scientific e59c29b,10checks/HIGH,308.576s
originalread plus47.197s native format-only continuation. Original malformed
JSON/acceptedfalse retained, same115tokens/onecomma deletion/zerotools,
canonical receipt+readcoverage+lineage checks passed. N2completepublictype/
standard3axioms/weightedtraceapplication independentlychecked; source and
proof unchanged. All5artifactpairs/3Falsecontrols/51failed+63success native
files verified; failedprivate/serverreplay notwaived. Addedcustodyclarification
for oneblankline excerpt trimming, extra separateTypeAudit, officialtagpin
and path-only warninglog difference.71finitefacts/18seams scopedaccepted.
FiniteGaussian/trace proof is analytic, NOTformalized byN2. L0/PROPOSED,
decision4/no officialpackage/companion/lease/registry/HPC unchanged.

## Existing finite facts: all-dimensional raw-event applications accepted — 2026-10-31

Full analytic/source/type/application gate at scientific d4d876e, adoption
c426e5a:12PASS/HIGH516.106s, no required repairs. Evidence in
../reviews/2026-10-31-raw-block-event/scientific-adjudication-v1.md.
New actual consumers of MovingCone3, JointTilt4 and ActualEvent2 were
checked against COMPLETE public types and their actual guards. The root
recomputed six unchanged source/public-type bindings to prior-reviewed
packets; no new Lean/compiler/replay execution or new fact is claimed.

Counts remain71finitefacts/18local seams. L0 PROPOSED and companion
creation decision4 unchanged. Gaussian Banach law, compact operator paths,
Young/source restart, continuum cone hypotheses and original point moment
identification remain reviewed INFORMAL analytic inputs, not consequences
formalized in Lean. See FP-RAW-EVENT in BOUNDARIES.md. The next U1-U4
unmasking/dilation target is frozen UNREVIEWED, not a new formal consumer.

## Old scalar score applications: all-dimensional consumer accepted — 2026-10-31

Full U1-U4 scientific61ac2a3/adoption94d85ca,11checks/HIGH303.405s,
no required repairs. Exact application of RawVariational.positive_score,
label_score and strict_label_factor reviewed against complete public types.
Positive-score I/v guard comes from actual unmasked rate and accepted raw
variance; label_score requires only c>0,alpha<3. The d1 dilation_factors
is NOT promoted as an all-dimensional Radon proof. Two source/type bindings
to the old reviewed packet unchanged; no new kernel/compiler/replay run.
71finitefacts18seams/L0 PROPOSED/companion decision4 unchanged.

The resulting unmasked point lower and positive finite intrinsic S_c=c^mS1
are ANALYTIC, including covariance/spectral/form/mask/canonical/supremum
steps. FP-UNMASKED in BOUNDARIES.md records this. B1-B5 static/full-H1
occupation target is frozen UNREVIEWED and introduces no new formal claim.

## Full occupation bridge: old entropy application accepted — 2026-10-31

Scientific249e2c4/adoptionaa4a016,18checks/HIGH366.614seconds/no required
repairs, all18inputs33native files verified. RawValueCeiling.strict_log_gap
complete public type and actual a>0,q-2a=D>0 guards checked in Section6.
Two prior/current source/type byte bindings unchanged; no new kernel/
compiler/replay/module or fact count.71facts18seams/L0 PROPOSED unchanged.

New physical two-point covariance extension, absolute signed four-linear
H1 bound, density/CS, full strongly-H1 measurable occupation energy and
original point comparison are reviewed INFORMAL analytic claims. See
FP-STATIC-OCCUPATION in BOUNDARIES.md; no formal Sobolev/SPDE theorem.
Next scalar target is unreviewed. Two potential new finite moment/rational
seams are only proposed, not Lean declarations; statement/reuse/compiler/
replay/negative-controls/application gates precede any count change.
No official package/companion/lease/registry/HPC transaction.

## All-alpha finite moment/rational pilot — local application pending

Two independently fenced public scalar headers compiled/audited at pinned
4.35.0/Mathlib56a0058, fresh owned replay5matching artifacts, full pp.all
types/standard axioms identical and4semantic False controls. Exact prior
search is bounded/incomplete; reuse existing field/order/tactic primitives,
no absence or competing-library claim. Initial compiled attempt FAILED the
warning gate on redundant sequence focus; both full attempts preserved.
Successor changes proof body only, exact headers match. No linter disabled.

71acceptedfacts18seams remain, plus2PROVISIONAL facts pending FULL actual
type/application gate. Source local-checks/all-alpha-moment-v1/; Gaussian
normalization/integral/IBP/CS/derivative and actual point consumer ANALYTIC.
No official package/companion/lease/registry/HPC transaction, L0 PROPOSED.

## All-alpha two finite applications accepted — 2026-10-31

Scientificed2e5f5/adoptionb5628d5,10checks/HIGH318.460s/no requiredrepairs.
Full public types and ACTUAL moment m1/m2/rational-gap guards passed
fidelity/application gate. Both new public source bodies/headers unchanged
from clean local compiler/axiom/replay evidence. Initial warning-gateFAIL
22files and clean successor41files retained;5artifactpairs/4False controls.
Old V source/complete definitions/types/application reused unchanged.

Promote two provisional facts:73acceptedfinitefacts/19local seams.
L0 PROPOSED and official companion decision4 unchanged. Local state mirror
updated together; see local-checks/all-alpha-moment-v1/application-summary.json.
No formal Gaussian/integral/derivative/SPDE theorem, official package/lease/
registry/HPC gate. Next sharp-upper work is a new analytic research screen.

## Existing finite powermean: Cameron-block application accepted — 2026-10-31

Scientifice0a6f3e/adoptionda1e1f7,12checks/HIGH523.772s/no requiredrepairs.
Pinned Mathlib Real.rpow_sum_le_const_mul_sum_rpow_of_nonneg COMPLETE
public TYPE/standardaxioms audited read-only; actual C3 substitution
kappa=r/p>1,f_m=t_m^p>=0, nonempty cardinality/power-zero/delta bookkeeping
checked in FULL application gate. No new local theorem, compiled formal
operator consumer, donor/package build or fact count:73facts19seams/L0.

C1 fractional physical covariance, actual-F compact CM map, tensor/time
mean compactness and averaged sqrt(delta)epsilon_J bound remain reviewed
INFORMAL analytic interfaces. Exact white guard excludes ONLY uniformR
fixed smooth-projection tails. See FP-CAMERON in BOUNDARIES.md. Future
residual-exponential DRIVER norm estimate still UNREVIEWED, not SPDE upper.
Official companion decision4/registry/lease/HPC unchanged.

## Existing real weightedAMGM: residual-norm application accepted — 2026-10-31

Scientific8b16bb7/adoption0dce26f,20checks/HIGH324.742seconds. Existing pinned
Real.geom_mean_le_arith_mean2_weighted COMPLETE public type/standard axioms
locally audited read-only; actual real weights/bases/positive-denominator/
zero/rpow application passed FULL analytic/source/type/application review.
No new compiled local theorem/module/export/count;73facts19seams/L0.

FP-RESIDUAL-EXP in BOUNDARIES.md records the actual fixedR Gaussian norm
exponential estimate as INFORMAL analysis, not a formally verified SPDE
upper. Original nonlinear/growing-cone/point/sharp/source gaps stay open;
official companion decision4 unchanged. No donor/package/registry/lease/HPC.

## Existing powermean: nonlinear residual application accepted — 2026-10-31

Scientificcdf2056/adoptionb480aca,24checks/HIGH388.122seconds. Exact complete
Mathlib powermean type and actual kappa=p/nu,f=v^nu,n>=1 positive powers/
zero guards/nu=p equality accepted. No new source/compiler/kernel count:
73facts19seams/L0. FP-YOUNG-RESIDUAL in BOUNDARIES.md distinguishes the
new actual fixedR/M nonlinear E1-E4 analysis from the finite formal input.
Original sharp-point/growing-cone/source gaps and companion decision4 open.

## Existing AMGM: signed rough static form application accepted — 2026-10-31

Scientific404354a/adoption7c91352,25checks/HIGH327.286seconds. Existing full
REAL weightedAMGM type with actual weights1/2,basesz²,(Kb)² and norm/zero/
real-power guards passed FULL application. No new source/compiler/kernel
count73facts19seams/L0. FP-SIGNED-STATIC in BOUNDARIES.md records all rough
form/spectral/physical-flow/mean claims as INFORMAL analysis. V1 temporal
rangeFAIL/HIGH retained, corrected2<r<2/a. Original sharp-point/source and
companion decision4 remain OPEN. No package/registry/lease/HPC transaction.

## Existing powermean: physical mean-product upper application — 2026-10-31

Scientificb1d8e5b/adoption2a22cc2,21checks/HIGH232.556seconds. COMPLETE
powermean type reused with actualr/rnu exponents, nonnegative data/cardinal
and positive-zero guards; no new source/compiler/kernel/count73facts19seams/
L0. FP-MEAN-PRODUCT boundary distinguishes actual polynomial-control-ball
mean-product upper INFORMAL analysis from the scalar finite formal input.
Original sharp-point/source gaps and companion decision4 stayOPEN.

## Gaussian cutoff-density local seam — PROVISIONAL 2026-10-31

Exact public header fenced before proof; GLstatement12HIGH360.315s passed.
Local source/types/standardaxioms/fresh replay5pairs/3falsevariants PASS.
New singlefinite scalar inequality pending FULL actual GLapplication gate;
73acceptedfacts19seams plus1PROVISIONALfact/newseam, no promotion yet.
Source lean-progress/local-checks/gaussian-tail-v1/. No formal Gaussian/
integration/conditional law/operator/SPDE, official package/lease/registry/
HPC gate; companionL0/decision4 unchanged.

## Gaussian cutoff-density actual application accepted — 2026-10-31

Scientific180bf1a,18groupedchecks/HIGH335.531seconds,no requiredrepairs.
COMPLETE publictype and EXACT application C=A1B3nu,M=M_B,x=headnorm,
positive cutoff/modelguards checked. Sourceheader/body unchanged, std3axioms,
5ownedreplaypairs,3standalonefalse numeric variants (not theorem calls) and
2valid actual theorem instantiations. Native28members reverified withpost-
cache/source/indexclean pins. Promote ONE previously provisionalfinitefact:
74acceptedfinitefacts20local seams. No Gaussian/conditional/integral/
operator/SPDE formalization, officialpackage/companion/lease/registry/HPC.

Machine mirror reconciliation: before10entries48facts while authoritative
ledger already19/73. Restored9accepted entries25facts, each publicsource
byte-equal its scientificGitblob and HIGH application close in this file;
then added newGaussian entry1fact. Currentmirror20entries74facts. Oldproofs
unchanged, no new compile/review of old25facts claimed. See local-checks/
gaussian-tail-v1/mirror-reconciliation-inputs.json and-summary.json.
L0/PROPOSED and officialcompaniondecision4 unchanged.

## UR original point signed-score upper: exact old-finite reuse — 2026-10-31

Scientific939d697,FULL19checks/HIGH367.538s,no requiredrepairs. Actual
GaussianTail densitycutoff application M>0,rho>=M,C=A1B^(3nu)>=0,nuin(1,2),
4C<=M^(2-nu); Holder p/nu>=1,r/nu>1 and AMGMhalfweights/squaredbases
checked withcompleteoldtypes/axioms. Source/declarations unchanged; no new
compiler/kernel/fact.74acceptedfinitefacts20seams/L0 remain unchanged.
FP-RAYLEIGH-SIGNED-MOMENT records allGaussian/integral/limsup/operator/GC
source-point assertions as reviewed INFORMALanalysis,not formalverification.

Next worthwhilefinite seam proposed,NOT built/promoted: PGactive-branch
scalar2ell sqrt(t)<=ell^2/w+w*t,finiteHilbertcompleted-square upper,Gram
normsquareidentity andpositive-weightentrywisequadraticcomparison. PGsource
fit15HIGH225.532s accepted onlystatements; fullproof/actualapplication gate
stillpending. Searchregistry/cachedMathlib beforebuilding,freezeexactpublic
types/guards,localcompile/replay/axiom/negativecontrols ifdeveloped. No new
officialpackage/companion/lease/registry/HPC authority; decision4 pending.

## Positive-Gram local finite seam — PROVISIONAL 2026-10-31

Fourpublicheaders fencedbeforeproof: scalar_sqrt_dual,gram_norm_square,
active_upper_bound,half_weighted_entrywise_mono. Completepublictypes/std3
axioms,6actualcalls andprivateexactPGbranchconsumer PASS. Freshsource-only
ownedreplay5artifactpairs identical;4standaloneFalse variants rejected at
False(notAPI/importfailure). TwoearlylocalAPI/rewritefailuresandoldunused
 auditbinderwarnings retained; no statement/linterweakening. Finalchecks0
errors/warnings. Currentofficialstable4.35/Mathlib56a0058 independently
verified;9selectedsourceHEADs/indexclean,8Mathlib-onlycachelibraries. No
privateWalsh/Rough libraryadoption,donor/dependencybuild or newpackage.

Perunit2CPU,4GiBhigh/6GiBmax,64tasks,proof-j1/asyncfalse;max2concurrent
units. Complete117membernativearchive readbackhashed. Rawsearchcoverage
incomplete(7nocheckoutpackages); typedLoogle/actualpinRG/APIchecks retained,
notabsence. ReuseMathlibprimitives/onlyconsumerwrappers,notnewlibrary.

74acceptedfacts20seams PLUS4PROVISIONALpublicfacts/newlocalseam awaiting
FULLPGsource/type/actualapplicationfidelity. Privateconsumer is integration
evidence,notfifthpublicfact. PG1-PG2min/existence/attainment/Gramrealization
and actualPDEoccupationapplication are ANALYTIC/opengates,notformalized.
OfficialcompanionL0/decision4unchanged; no officiallease/registry/HPC gate.

## Positive-Gram actual finite application accepted — 2026-10-31

Scientific4e2219d,FULL26checks/HIGH305.393s,no requiredrepairs. Complete
publictypes/std3axioms andACTUALPGguardapplications accepted; source/headers/
compiledproofs unchanged. No subjectivekernelproofscore requested; analytic
dualbarrier/minimum/calculus/attainment/realizationcheckedseparately.
Promote4PROVISIONALpublicfacts/newlocal seam:78acceptedfinitefacts21seams.
Privateintegratedconsumer remainsintegrationevidence,notfifthpublicfact.
Derivedmirror appends1entry4facts,preserves20oldentries74facts exactly;
officialL0/PROPOSED/candidateNone/lease/registry/HPC/companiondecision4stay.
No compile/replay/numericrerun forclarity/promotion. Rawpre-appreceipt/status
preserved,application-summary-v1 current. Kernelcertifiesfiniteconditional
algebraONLY,notwholePGanalyticoptimization oractualoccupation/PDEapplication.

## PB physical comparison: analytic boundary — 2026-10-31

PBstatement/applicationFITpassed21HIGH884.243s at6de6728. The new author
proof includesL2HilberttensorSchurcompletion,nonseparable rawcontrols and
actualmeans,physicalGramguardfit,uniformnorm/smoothing/continuumarguments
andoriginalpointupper/lowersandwich. AlltheseNEWanalyticstepsareOUTSIDE
thekernelandrequiretheirOWNfullgate. ExistingPG finitecertificates and
priorPGapplicationreviewremainunchanged;no directnewLeanapplication or
statementisbeingclaimed. Trivialscalarcoercivityalonewouldnotcertifythe
modelcomparison;no low-valuecompilejusttoincrementcount.78acceptedfacts/
21seams/L0PROPOSED unchanged;existingmirroralreadyagrees. No companion,
package/lease/registry/HPC action. Scientificauthoritystays../Progress.md.

## PB analytic theorem accepted, no new kernel claim — 2026-10-31

Scientific40ec9a9FULL19checks/HIGH387.047s,no requiredrepairs. PB0-PB5 and
theiractualmodelapplications are reviewedINFORMAL mathematics:originalpoint
intrinsiclimitALLmodels,notauthorconstant/p1identity. ExistingPGfinitekernel
deductions are reused unchanged; no newly compiled theorem, new formal fact,
seam or officialpackagegate.78facts/21seams/L0PROPOSED unchanged. New raw
membership/time/mean,Rayleigh/smoothing/optimizationlimits andmomentassembly
remain analytic boundaries. Fullsource/novelty/wholepaper/coldreadopen.

## OC derived bounds accepted, same kernel boundary — 2026-10-31

Scientific25cc688FULL18HIGH302.195s accepts the actualall-model occupation
ceiling and commonspatialenergy bracket. Oldstrict_log_gap reused at its
exacta>0,q-2a>0 type,includingq<3. No newkerneltheorem/compiler/seam/fact
or officialpackagegate.78facts21seams/L0PROPOSED remainunchanged. Actual
roughsquarecompletion,physicalpairing,time/mass/near-selection,scalar
globaloptimization andmomenttransferare reviewedINFORMALmathematics.

## White CDF finite local pilot: kernel pass, application pending — 2026-10-31

Two completeheadersfrozenbeforeproof; source4d3f8ee4350f96d5936a4b213c7aff5a312218743ee43b885e3c91a3b100cbcd
compilescleanfirsttryoncurrentstable4.35.0/Mathlib56a0058. Fulltypes/std3
axioms,privateexactcomposition,positivecalls,ownedsource-onlyreplay5pairs
andauditbytesidentical,twoexactFalsecontrolsPASS.53nativearchive members
readbackhashed. Fail-closedlist/Falseparser14mutationchecks alsoPASS.
No analyticH1/CDF/GN or energy-supremum/PDEkernelclaim. InitialactualWS
statement/definition/applicationfidelityandOWNfullanalyticgatePENDING.
2PROVISIONALpublicfacts/newlocalseam,accepted78facts21seamsunchanged;
mirrorunchangeduntilpromotion. L0/PROPOSED,decision4andofficialpackagegate
unchanged. No newrepo/package/lease/registry/HPC or donordependencybuild.

## White CDF initial FIT passed; analytic application still pending — 2026-10-31

ad9fe4dFIT26HIGH276.215s accepted fulltype/definition/guardpatternsfor
the2conditionalfinitepublicfacts. Written full-H1/CDFproof andphysical
energy/supremum/attainment/model/Gammaapplications awaitOWNFULLreview.
Negativecontrolsourcesnowincludedandhash/name/logboundbyguardv2,
18adversarialtextmutationsrejected; no compiler/proof rerun. Prior artifacts
preserved.2PROVISIONAL/accepted78facts21seams/mirrorunchanged. Private
compositionnotthirdfact, officialL0PROPOSED/decision4 unchanged.

## White CDF actual applications accepted — 2026-10-31

Scientific95d7515,FULL25HIGH313.597s,no requiredrepairs, accepts complete
publictypes/definitions/ACTUALCDFsquare andphysical-energy guardapplications.
Source4d3f8ee4350f96d5936a4b213c7aff5a312218743ee43b885e3c91a3b100cbcd,
headers/typedproofs/replayoutputs unchanged. TwoPUBLICconditionalfacts
promoted:80acceptedfinitefacts22seams. Privategenericconsumer notthirdfact.
Derivedmirror adds2factentry,preserves21oldentries78factsandallofficial
L0fields. Rawpending-statusreceipts preserved;application-summary-v1 current.
AnalyticH1,CDF/IBP/integrals,sechattainment,Gamma andoriginalpoint bounds
reviewedINFORMAL,notLean-certified. No newcompiler/package/registry/lease/
remote/cluster/companionaction. Integration/finalgatesremain.


## Hermite selected-word standalone pilot — 2026-11-08

Two abstract public facts raw_support/cut_eq_raw compile on currentstableLean4.35.0 withStdonly, noMathlibimport. Corefirstcompileclean andheadersunchanged. Exacttypes/axioms audit:raw_supportnone;cut_eq_rawonlypropext/Quot.sound. Ownedsource-onlyreplayproducesbyteidenticalolean/audit; privateall-orderunnormalizedcoefficientrecurrenceconsumerpasses,order2selfpair1/order4selfpair3retained. Three semanticFalsecontrols reject insufficientcutoff1, missingloweringandwrongorder4multiplicity. One privateconsumer simplificationfailure andone control-parser-wordingfailure preserved. Initialexacttype/applicationreviewPENDING;2PROVISIONALfacts, accepted80facts22seams unchanged. Evidence local-checks/hermite-word-v1/. L0/PROPOSED anddecision4unchanged; no companion/package/registry/lease/HPC.


## Selected-word initial FIT remains MEDIUM — 2026-11-08

NativeDS whole19body review terminal18696input/14718output-plus-reasoning within52180bound. Root fullread/canonicalvalidator/exactFIT01-FIT08 all8PASS/no repairs. LiteralPASS_WITH_NOTES/MEDIUM remainsUNACCEPTED; normalizedmultimodeGaussian/Hilbert andcoupled-frame instances remaininformal. No actual false source statement located; no confidence normalization or retry. Two abstract publicfacts stillPROVISIONAL, accepted80facts22seams/L0PROPOSED unchanged. Proof/headers/compiler/replayunchanged; current application-summary-v1 records status separatefromhistoricalpendingreceipts. No new companion/package/registry/lease/HPC.


## Existing Gaussian-basis reuse verified locally — 2026-11-09

Usinglean-pkg0.28.0 search/doctor, foundregistered GaussianChaoswhosecheckoutwasabsent from search. Exact87e02e09/c111340Walsh sourceclosure7modules compiles fresh atlateststable4.35/Mathlib56a0058. Rejectedavailablee054Walsh cachepin; immutable exactsourcescompiledinstead. NormalizedproductGaussianL2basis/rawmultivariatecoordinate recurrence fulltypes/defs visible, targetedtransitiveaxioms Std3. ActualFin2firstmodeinner-square1 consumerpasses; wrongsquare2 rejectssoleFalse. Initialmissingcachehelperrefusal andpp.maxDepth APIfailure preserved; correctedAPIreuses7sameobjects,notrecompile. Canonicalcappedlocaldevelopment only, notofficiallean-pkg/comparator/registry/full-library gate. Evidence reuse-probes/gaussian-basis-028-v1/. Basisprimitiveavailableforreuse, notactualcoloredphysicalwordconsumerformalized; no newpaperfact orpromotion:80accepted/22seams+2oldprovisional. L0PROPOSED/candidateNone/jobids[]/decision4unchanged; mirroraddsONLY0factreuseentryandpreservesalloldentries. Kimi hold andvisualpolicyNOTADOPTED remain.


## Normalized-coordinate target proposed/typechecked, not proved — 2026-11-09

ExistingGaussianbasisreuse unlocks smallnormalizationconsumer. Exactclosedpropositiontypechecks at4.35; statementSHA38c89d8d0626fe279c6000089262da074d42899adbf8b2308519265627d490d1. TargetallMode/finitemultiindex/realcoordinateassignment, bothsqrtraising/lowering includingzero. GaussianprobL2 distinctrawH_I/physicalphase; no physicaldimension/time-independence/torus assumption. FrozenpaperL:fockformLF5466-5531 explicitmatchesline5518. Statement/source/microcontract in statement-proposals/normalized-coordinate-v1/. No proof yet; priorblind independentstatementfidelityrequired beforeproof; no newword/SPDE/acceptedfact/package/companion/HPC claim, old80/22+2provisional/L0 unchanged.


## Normalized-coordinate scalar leaf locally verified — 2026-11-09

Priorblind nativeOpus5.5/high sixNORMchecks PASS/no repairs, exact9sourcecoverage/rawSHAdf425444e1bb1b09328bc91c885ebb227fce5b901853a6ce584b8a210e866d02. Rootfullread/minors/limits adjudicated; exactclosedProp unchanged. ActualGaussianChaos normalization consumer provesbothsqrtraising/lowering inclzero, source594e4b17 at4.35/Mathlib56a0058 compilesclean/Std3. Freshownedleaf replaybyteequalobject/audit,reusespinned7foundationobjects,notfullclosure replay. FullPropassignment/loworderpolynomial/factorial/vacuumlowering/twoactivecoordinateL2norm controlsPASS; omittedlowering rejectssoleFalse. Intermediateproof/consumer/scriptfailure historypreserved. Evidence local-checks/normalized-coordinate-v1/. AddsONE acceptedlocalscalar fact/seam:81/23; old2abstractwordfactsstillprovisional. Actualcoloredphysicalvector/projection/operator/Bochner/cutoff/SPDE boundariesopen. OfficialL0PROPOSED/decision4/no package/registry/HPC unchanged,Kimihold/visualpolicyNOTADOPTED/fullmathHIGH/cold/finalgatesunchanged.


## Actual vector-Gaussian projection target proposed — 2026-11-09

Value-rankednextmissingwordboundary: actualorthogonalprojectiononGaussianLp(E),arbitrarycompleteHilbertEincludingcoupledbackground/spatialphase. ExistingMathlibcompLp/closedspan/starProjection APIs sufficeforstatement,nonewGaussianfoundationorpackage. Generalpredicatetargetandliteralpercolortotaldegreespecializationtypecheckfirsttry; source/defs frozen statement-proposals/vector-gaussian-projection-v1/. IdentityisCONCLUSION,nothypothesis; realificationcomplex/sourcecouplingisindependentfidelityobligation. Registrysearch0hitsbutincomplete6missingcheckouts/indexabsent,notabsence; existingknownGaussianlibraryinspected/read. No proofyet,priorblindfidelityrequired. Existing81/23+2oldprovisional/L0PROPOSEDunchanged,fullgoalgates/Kimihold/visualpolicyunchanged.


## Vector projection statement v1 MEDIUM; exact consumer v2 proposed — 2026-11-09

InitialsixVECchecksPASS/literalMEDIUMunaccepted,no proof. Rootcorrectsreviewerfinite-spatial-dimensioninference; theFourierbandisclosedinfinite-dimensionalandphase-normequivalencegivescompleteness. SuccessoractualconsumerusesSigma_iFin(m_i),notexpandedproduct; mainarbitrarypProjectionPropunchanged. ExplicitfinitebackgroundHermite/physicalphaseisometry,projectionintertwiningandrealificationargumentsplusactualphase/contractiondefinitionsaddedforindependentreview,notkernelclaims. Revisedtypedstatement74afb863b4ce71da8779216629686c7f40f98a5dc30ef1d69033300a02465b19 compilesfirsttryasPROPonly. Eighteenwholebodies/6VECpriorblindchecks prepared,capacity311492incl128000outputreservewithin1M,textdryrunPASS. No newproof/fact/promotion/package/companion/HPC,81/23+2oldprovisional/L0 unchanged. Ready reviews/2026-11-09-vector-projection-statement-v2-ready/,initialreport reviews/2026-11-09-vector-projection-statement-medium-unaccepted/. SeparateonceRootauthorityafterdurablecommitrequired.


## Actual vector-valued Gaussian projection locally verified — 2026-11-09

RevisedpriorblindOpus5.5/high sixVECchecksPASS/no repairs/full18bodycoverage,rawade97a1055d59390a70fdb9af2f4658a55e9d0489dcbb295be9971c80641e7b6. Rootreadall/adjudicated5minor5limits; S_bexplicitLF5472, spatialbandinfinite,actualphase/bg/realificationcorrespondence reviewedMATHonly. ExactgeneralclosedProp+dependentSigma-colorinstance assignedtouniversepolymorphicprojection_realize. ActualLp(E)/closedspan/starProjectionproof compileclean4.35/Mathlib56a0058/Std3; ownedleafsource replayobject/auditbyteequal,reusespinned7foundationobjects. Actual2mode/2vectorprobe selected/discardedselfinnersboth1. WrongretentionwithnoselectedmodesrejectssoleFalse(onealiaswarningpreserved). Onepubliclocalfact/seamadded82/24;2oldwordfactsstillprovisional. Evidence local-checks/vector-gaussian-projection-v1/. CoordinateJ/coloredword/Bochner/complex-instance/bg-isometryformalization/analyticSPDEassemblyremainoutsidekernel. OfficialL0PROPOSED/decision4/no package/HPC unchanged,allfullgates/Kimihold/visualpolicyNOTADOPTEDunchanged.


## Concrete actual colored-vector finite-word target proposed — 2026-11-09

ExactSigma modes,arbitrarycompleteREALHilbertcoefficientsandboundednoncommutingK/F; actualLpGaussianmultiplicationnaturaldomain/orthogonalP,notfilterproxy. ThreeclosedProps: coordinatepoly-domain/realization,allraw/cutprefixdomains,actualfinitewordcutoffequalityunderoccurrencecounts<=N; plusprivateframehelpertype. Outside-domainzeroistotalizationONLY,guardmustbeDERIVEDforallprefixes,notassumed. Typecheckfirstattemptsum-parenthesiscaught/preserved; finalfullstatementcompilesclean. Smallnoncommutingmatrix/order2lowering/cutofffalsificationrecordedBEFOREproof. Frozen statement-proposals/colored-vector-word-v1/. No proof/publicfactpromotion,82/24+2oldprovisional/L0unchanged. Requirespriorblindindependentdefinition/domain/source/applicationfidelitybeforeproof.


## Concrete colored word kernel complete; actual application review pending — 2026-11-09

FullthreefrozenpublicPropscompilecleanStd3, sourceb7d4978f5042753174249cff92448787cfbfa7267eb3d0df6ff8b09b723ec717. ActualLpcoordinatepoly-domain/identity,allraw+compressedprefixdomainsandorthogonalPwordequalityderivedwithonlycounts<=N,arbitrarycompleteREALHilbert/noncommutingboundedK,F/exactSigma modes. Exact3closedPropconsumer/private4thhelpercheckPASS; ownedleafsource replayobject/auditbyteequal(reusespinnedfoundations/localimports,notfullpristine). Actualorder2L2wordmean1/nonzero/cutoff2PASS; wrongselfmean0andwrongcutoff1GUARDrejectsoleFalse. MatrixprobeMATHonly; complex/bgbridgeMATHonly; actualbackgroundextensiononlyrangePcross,notglobalfactorization. ThreeNEWprovisional+old2stillprovisionalpendingcompletedapplicationreview; accepted82/24/L0unchanged. Evidence local-checks/colored-vector-word-v1/. No package/registry/companion/HPC,Kimihold/fullgoalgatesunchanged.


## Concrete Gaussian/vector finite-word application accepted — 2026-11-09

CompletedactualconsumerOpus5.5/high240.493s CWAPP01-06allPASS/no repairs/full23bodies,rawda51be6ebe7792200a12cdfe939978f2ee7ef00f9d5d81dafe7dc7b9bd21ffba. Rootreadall/adjudicated6minor5limits. ExactGood/vacuum/degree/frame/filter premisesDERIVEDfornormalizedmultivariatevectorcoefficientsandlinkedtoactualLpcoordinate-domain/P/raw+cutwords,notabstractproxy. Promote3newfacts+2oldunchangedgenericfacts:87localfacts26seams. OriginalMEDIUM/pendingreceiptsunchanged; currentapplication-summary-v1 incolored-vector-word-v1 andgenericapplication-summary-v2 recordnewactualscope. Sourceb7d4978f/cleanStd3/exact3Props/private4th/ownedleafreplaybyteequal/actualorder2L2mean1nonzero+cutoff2/semanticselfmean0andcutoff1GUARD controlsremainunchanged. Raw-prefixrange followsDIRECTraw_support+cut_fixes_good,notglobalbackgroundfactorization. Complex/bg/height/Bochner/analytic/SPDEbridgesoutsidekernel,officialL0PROPOSED/decision4/fullmathHIGH/cold/visual/adoption/deliverygatesunchanged,Kimihold/visualpolicyNOTADOPTEDremain.
