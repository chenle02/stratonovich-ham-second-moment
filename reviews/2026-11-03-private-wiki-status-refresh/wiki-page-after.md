[held back: collaborators' unpublished work]

## Problem

For the [[concepts/hyperbolic-anderson-model|hyperbolic Anderson model]]

$$
\partial_t^2 u(t,x)=\Delta u(t,x)+\dot W(t,x)u(t,x),\qquad u(0,x)=1,\quad \partial_t u(0,x)=0,
$$

in $d\in\{1,2,3\}$, interpreted in the [[concepts/stratonovich-integral|Stratonovich]] sense, with Gaussian noise fractional in time,

$$
\operatorname{Cov}\big(\dot W(s,x),\dot W(t,y)\big)=|s-t|^{-\alpha_0}\gamma(x-y),\qquad 0<\alpha_0<1,
$$

and homogeneous covariance $\gamma(cx)=c^{-\alpha}\gamma(x)$ with $\alpha_0+\alpha<2$ ($0<\alpha<d$, or $\alpha=d=1$), determine the large-time growth of the **second moment** $\mathbb{E}u^2(t,x)$. Set

$$
\kappa:=\frac{4-\alpha-\alpha_0}{3-\alpha}.
$$

**Goal revised by Le on 2026-10-31:** derive the actual $p=2$ asymptotic constant, whatever value or complete variational formula the proof yields. Matching Chen's conjectured constants is comparison context, not a completion requirement. Preserve every original admissible homogeneous covariance and its amplitude, $d=1,2,3$, $0<a=\alpha_0<1$, $\alpha+a<2$, $0<\alpha<d$ or $\alpha=d=1$, data $(1,0)$, and every fixed $x$. Treat zero covariance directly.

The current goals are an independent finite upper bound at scale $t^\kappa$ and a proof of

$$
\lim_{t\to\infty}t^{-\kappa}\log\mathbb E|u(t,x)|^2=C_2(\gamma,a),
$$

with the complete variational domain, original covariance amplitude, kinetic coefficient and Gaussian action specified. An exact variational characterization qualifies as a derived constant; a nonsharp bound does not constitute its numerical evaluation. The completion contract and remaining review gates are in the active research checkout's `PROJECT-GOAL.md` and `Progress.md`.

### Historical original goal — superseded on 2026-10-31

The original two goals were:

1. **Upper bound at the correct scale:** $\limsup_{t\to\infty}t^{-\kappa}\log\mathbb{E}u^2(t,x)<\infty$.
2. **Sharp constant for $p=2$:** two-sided bounds
$$
2^{\frac{4-\alpha}{3-\alpha}}L_*\le\liminf_{t\to\infty}t^{-\kappa}\log\mathbb{E}u^2(t,x)\le\limsup_{t\to\infty}t^{-\kappa}\log\mathbb{E}u^2(t,x)\le2^{\frac{4-\alpha}{3-\alpha}}L^*,
$$
the $p=2$ case of Xia Chen's conjecture, up to the same gap $\mathcal{E}_*<\mathcal{E}$ as his first-moment theorem. The exact limit $2^{(4-\alpha)/(3-\alpha)}L^*$ is the conditional target.

Here $L_*=L(\mathcal{E}_*)$ and $L^*=L(\mathcal{E})$ are the constants of [[papers/chen-25-time-dependency|Chen (2025/26)]], Theorem 1.2 (1.10), in the current author version.

## Current state — 2026-11-02 resumed full goal

**ACTIVE: Le resumed the full original all-model actual-constant goal; actual DeepSeek V4 Pro is MAIN.** The goal is not user-paused, blocked or complete. The written intrinsic formula below remains qualified by the open whole-argument, source/application, visual and fresh independent cold-review gates. Chen matching is not required, and the auxiliary label-one score is not an actual first-moment limit.

Current <HUB> authority is workflow `14d82c078a4b02a42fecebc61ef0de9ece0ccb80` on `research/fixed-mask-young-20261031`, a verified descendant of `ad5dac7b01c63e94e85e03577fd9492579ca41da`. Latest `Progress.md`, `PROJECT-GOAL.md` and its current `reviews/2026-11-02-main-deepseek/depth-ledger-v39.json` bind scientific **`8ce03ae09cca984b32aaddf3da0a6ded07f47ebc`**: **28 TeX files, 214 proof identities, 240 formal statements and a clean 263-page PDF**, SHA-256 `bd1bacf8bdf992ca2e271d671839dfd6a03cd9e84160327045ce45f6d93b7ab6`. All source/PDF bytes and current proof-body hashes were verified. Expanded analytic bodies **088/091/108/110/125/126** were adopted after scoped cross-family DeepSeek review; 208 other bodies and all formal statements are unchanged. The **80 finite Lean facts / 22 seams** retain their existing limitations; analytic formalization and an official companion are not implied.

**Ledger v39: 189 exact scoped HIGH adoptions, 22 unaccepted lower-depth/current-report rows and three editorial deltas.** This is neither a completion percentage nor whole-argument acceptance. Complete calibration returned raw PASS/HIGH, including its factual correction, but only **011–019** were adopted: **010 remains unaccepted because the independent explanations misstate factorial normalization, while the manuscript and author replay are correct**. The later complete temporal-control/smooth-spatial-ratio review adopts only **136/137**, with named-input, endpoint, cost, dilation and noncircularity qualifications; no actual first-moment or Chen-constant identity follows. Each original/correction pair is one lineage, not independent votes. Current ledger evidence retains every exact target/body binding and reading limitation; earlier reports are immutable.

The full **214-proof MAIN on `b4b6efc` is terminal UNGRADED, 120 CHECKED / 94 LIMITED**; scoped adoptions do not rewrite it or transfer that report to changed bodies. The historical **213-proof MAIN MEDIUM** report remains immutable history. Required primary-source images, full **263-page independent render**, Kimi, whole-main HIGH, a fresh independent cold read and final private delivery remain **OPEN**. The latest actual Kimi monthly HTTP 429 at **2026-11-02T17:26:09Z** produced **zero reads, zero images and a null report**; no retry or substitute is authorized. No current review launch is acceptance, and no public release or goal closure follows.

**Maintenance provenance:** internal status-only successor `tk-20261102-223931-codex-stratonovich-status-refresh` uses the newly authorized science/status snapshot and verified later scoped metadata. Exact predecessor **`tk-20261102-052608-codex-stratonovich-main-depth` remains failed**, with its receipt and history unchanged; this successor neither depends on that failed state nor relabels it. The dated blocked checkpoint below is preserved as history. Queueing/claiming is not maintained publication; this ticket requires its own terminal receipt and owned published wiki commits. No manuscript, bibliography, relationship, companion, cluster, Skorohod, correspondence or public-deployment work is authorized.

## Historical terminal blocked checkpoint — superseded on 2026-11-02

The following checkpoint is retained as dated history. Its BLOCKED/paused state, terminal-attempt inventory and scientific 887/257-page/213-proof identity describe that earlier capture only; the current resumed status and science8ce snapshot above supersede them.

**BLOCKED: the goal service records the unchanged full objective as blocked; whole-argument acceptance remains open.** The required Kimi image/cold route still has an actual monthly HTTP 429, with no report, tool execution or image-read credit. The same blocker persisted over multiple continuations after useful authorized audit and adjudication work was completed. All current reviewer processes are terminal; no retry is queued. The next external prerequisite is restored Kimi capacity or Le's explicit replacement-reviewer direction. No restoration or replacement authorization has arrived; no silent provider or HIGH-threshold change is authorized.

The schema-valid project field `status: paused` means blocked or waiting for input; the goal-service state is **BLOCKED**, not complete or user-paused. Le explicitly resumed the full goal on 2026-11-02. The actual all-original-model second-moment constant remains the objective, without forcing Chen endpoints. Original HIGH, source/application/visual and fresh independent cold-review requirements remain unchanged. Written all-model proofs retain only their original scoped cross-family reviews. The independent target-scale full upper and the intrinsic original point-moment limit now cover all original admissible models above, including the higher-$\alpha$ range that was open in October. The result is for the same canonical Stratonovich solution, with all mixed, unequal, self and empty chains retained. The older independent full upper supplies variational finiteness without using the final constant identification.

The integrated theorem `T:intrinsic-second-moment` in `notes/integrated_intrinsic_constant.tex` states

$$
C_2(\gamma,a)=S_2^{\mathrm{pos}}
=2^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}}.
$$

For nonzero covariance, put $I=(0,1)$ and use the full positive raw spacetime control class

$$
\mathcal C_{\mathrm{pos}}
=\{\Psi\in C_c^\infty(I\times\mathbb R^d;\mathbb R):\Psi\ge0,\ \Psi\ne0\}.
$$

This includes **nonseparable** controls. In the original covariance units define

$$
\begin{aligned}
h_{\Psi,s}(x)&=\int_I|s-t|^{-a}(\gamma*\Psi_t)(x)\,dt,\\
v_\Psi&=\int_{I\times\mathbb R^d}\Psi(s,x)h_{\Psi,s}(x)\,dx\,ds,\\
I_\Psi&=\int_I\sqrt{\sup_{\substack{f\in H^1(\mathbb R^d;\mathbb R)\\\|f\|_2=1}}
\left\{\int_{\mathbb R^d}h_{\Psi,s}f^2-\|\nabla f\|_2^2\right\}}\,ds,\\
S_b^{\mathrm{pos}}&=\sup_{\Psi\in\mathcal C_{\mathrm{pos}}}
\{bI_\Psi-v_\Psi/2\},\qquad b>0.
\end{aligned}
$$

The full-gradient kinetic coefficient is **one**, the Gaussian cost is the **raw variance divided by two**, and the covariance keeps its original amplitude. Here $b$ labels an auxiliary score, not an asserted moment theorem. In particular $S_1^{\mathrm{pos}}$ is **not** an actual first-moment limit or Chen's $L$. For nonzero covariance the theorem gives $0<C_2<\infty$; for zero covariance $u=1$ and $C_2=0$ directly.

The underlying physical positive-score comparison is scientific commit `40ec9a9342df2eb1de455b0a2743dce204615eb9`. The integrated intrinsic theorem at scientific commit `a880288423d7824b0ca902b0e3a83b57f9086558` received an actual full Opus 5.5/HIGH proof/application review with 30 named checks, overall PASS_WITH_NOTES/HIGH and no required repairs. The occupation/white integration at scientific commit `d041546d60693abdbe8ccedea12da2fb6ebb7d0d`, packet-contract repair `691f413ea74657a446df256def3301eb28321b6f`, received 31 HIGH checks, overall PASS_WITH_NOTES/HIGH and no required repairs. Optional findings were adjudicated in the retained research review artifacts; these are scoped reviews of their frozen inputs.

The occupation module gives an all-model ceiling and a common spatial-energy bracket for this same $C_2$. Spatial white covariance $c\delta_0$ in $d=\alpha=1$ is an **example**, with exact spatial energy $\mathcal E_{\mathrm{sp}}=c^2/6$ for covariance mass $c$. The explicit moment bounds in `notes/integrated_white_evaluation.tex` are **not an exact numerical evaluation of $C_2$**. They introduce no Fourier or temporal normalization repair and do not reduce the all-model scope.

[held back until the source author has been told]

### Consolidation and open gates

The current common scientific review candidate remains `887fbfbe0fa4368d6b32a436615d73349b2445d8`, tree `6a48b34d7ec9bc686453ee5c656938475ea48774`, with editorial source/PDF `b2fda02`: **257 manuscript pages and 213 proofs**. Exact PDF SHA-256: `10bfeae6eb576e23ba928b8ef9eca968d87f23ac7eff884c632bf50acb3294c9`. This status update changes no manuscript mathematics or PDF. The resumption inventory records an all-448-path unchanged readback of `reviews/2026-11-01-coverage-recovery/common-binding-v2.json`. At this maintenance readback, 447 paths still match; the sole later change is `PROJECT-GOAL.md`'s reviewer-directive paragraph, reconciled to DeepSeek V4 Pro + Kimi-K3. The scientific inputs and PDF remain unchanged. Byte identity and counts are author custody evidence, not proof acceptance.

The older whole-argument attempt on `4a65c79` and its supported continuation are **TERMINAL and unaccepted**: the first timed out; the continuation returned **INCONCLUSIVE/medium with incomplete source/image coverage**. The former live-review snapshot below is historical. All current reviewer processes are now terminal, with no queued retry. Follow latest `Progress.md` for the authoritative blocked frontier; process IDs are not durable project status.

**Authorized new-review directive:** actual **DeepSeek V4 Pro + Kimi-K3**, HIGH confidence, immutable input identity, exact source/application/visual coverage, full findings adjudication and a fresh independent final cold read. Earlier Opus receipts retain their original names, frozen inputs and scopes. The older canonical composition adapter is Opus-specific: renaming DeepSeek/Kimi receipts does not satisfy it. Its refusal and the earlier unsuccessful attempts remain preserved.

**Full verification remains OPEN.** The coverage contract retains 15 components, 390 required check IDs and a separate synthesis, covering 86 primary-source frames, 257 manuscript pages, 28 TeX files, 44 sections and 213 proofs. Assignments and inventories are not passing reviews. Whole-mathematical synthesis, primary-source/application and visual checks, consolidated model calibrations, and the final independent cold read remain unmet. Final delivery still requires a clean bound source/PDF build, handoff, synchronized private Git delivery and an explicit completion audit under `PROJECT-GOAL.md` and `reviews/2026-11-02-resumption/completion-obligations.md`. There is **no whole-paper, full-goal, novelty, human, circulation or publication clearance**.

### Auxiliary cutoff and source-review outcomes

The cutoff v1 proof review returned PASS_WITH_NOTES/HIGH with seven production requests. Successor `dd27f38e55506930352725bdb4ce6162283c2c3d` repairs them without imposing stronger Hölder regularity on C: Young regularity belongs to the primitive M and state V; C is bounded and strongly continuous. At the ticket's earlier snapshot, the actual DeepSeek followup was pending and the successor unadopted. The authoritative descendant `23b484a` records its terminal PASS_WITH_NOTES/HIGH, all F01–F10 PASS, and **scoped compatibility adoption of the bounded O1/O2/O3 deduction on its named analytic inputs**. This was a non-blind production followup, not a cold vote. Retained source/workflow/image limitations and the reviewer-summary slips are adjudicated in `reviews/2026-11-02-cutoff-overlap-proof-v2/adoption-adjudication.md`. This is neither a full local-flow theorem nor a new second-moment result, and closes none of the full-source, visual, novelty or whole-goal gates.

The actual native **Kimi 2.3.3 / kimi-code / k3 / max / OAuth** source-image attempt on 2026-11-02 returned **monthly HTTP 429, terminal exit 1**, with zero report, tool execution, image reading or review credit. Raw evidence remains in `reviews/2026-11-02-sf04-young-kimi/`. No retry, purchase or substitute is authorized; the assigned image and independent Kimi obligations remain OPEN.

At workflow descendant `b49dd36d26e12ff5a70ea15f055f4b2c2f454276`, the supplementary actual DeepSeek SF04 text/application audit is also terminal: **PASS_WITH_NOTES/MEDIUM**, below the required HIGH threshold. Nine determinations pass only at their limited scope; SF04-01/07/11 remain INCONCLUSIVE without the assigned images, and SF04-10 remains INCONCLUSIVE without the supplied upstream eligibility proof chain. Every finding is adjudicated in `reviews/2026-11-02-sf04-text/adjudication.md`; no manuscript repair or confidence upgrade is inferred. This is not full-component, synthesis or cold acceptance.

The subsequent **full-context actual-law/application DeepSeek V4 Pro review is TERMINAL PASS_WITH_NOTES/MEDIUM**, not HIGH. All 28 complete scientific TeX files supplied the 17 formerly omitted upstream inputs; E01–E10 returned favorable scoped determinations, and all five author rebuttals were accepted. The earlier missing-input finding above describes the first text audit, not an unsupplied input in this expanded review. The full report and all 71 native archive members were preserved and readback verified. Depth and source-image limitations remain; no full SF04, source-image, whole-synthesis, cold or goal acceptance follows. Both MEDIUM verdicts remain immutable; no rerun merely for confidence is warranted. Findings and dispositions are retained in `reviews/2026-11-02-sf04-eligibility/adjudication.md`; the blocking and completion audit is `reviews/2026-11-02-resumption/blocker-and-completion-audit.md`. No new mathematical theorem or defect is established, and scientific `887fbfbe` and the 257-page PDF remain unchanged.

The review's short mainchain non-input classification is **not a whole-paper source waiver**: Chen–Hu and Chen2023 imports remain genuine dependencies of retained auxiliary sections. Full 213-proof source coverage remains due. Scoped cutoff HIGH adoption stays bounded and unchanged; neither MEDIUM review replaces the missing full-source, visual, synthesis or independent cold gates.

**Lean boundary:** 80 accepted finite facts across 22 standalone seams remain unchanged; analytic inputs and consumers remain unformalized. The proposed official companion remains **L0 PROPOSED**, decision-point-4 approval is absent, and no companion package, lease or HPC authorization is implied. Finite kernel checks are not analytic or whole-argument verification.

[held back: collaborators' unpublished work]

### Historical maintenance provenance — resumption checkpoint

[held back: collaborators' unpublished work]

## Current approach

Retain the independent full upper, then join the signed original point upper to the positive raw-control lower through finite Gram optimization, physical entrywise comparison, uniformly bounded optimizers and positive smoothing. Remove the possibly nonmonotone physical cutoff with each control fixed first. The upper and lower concern the same original point moment and give the intrinsic constant above. Occupation estimates and the white spatial-energy computation provide rigorous bounds, without forcing Chen matching or claiming a closed numerical value.

The next acceptance steps concern the frozen whole argument and final independent cold read, with source/calibration findings adjudicated in `Progress.md`. No new proof wave, manuscript change or review dispatch is authorized by this wiki correction.

### Historical consolidation snapshot — superseded on 2026-11-02

The following is the prior ticket's 2026-11-01 snapshot, retained verbatim as history. Its LIVE/PENDING/NOT DISPATCHED wording and 258-page candidate describe that earlier capture only; the terminal outcomes and current 257-page scientific identity above supersede them.

The frozen consolidated scientific candidate is `4a65c79d9d4b5c6a7e0cb712a88f1a973cc9c3fd`: a clean 258-page PDF, 213 proof blocks, 174 bodies unchanged and 39 clarified, zero new blocks. These counts and the clean build are author metadata, not evidence of whole-paper acceptance. Exact PDF SHA-256: `e1e15974b154c5a36302b402dcd8c9cd99883159255f5a5a679795a9441d6546`.

As of the authoritative snapshot, fresh whole-argument **Opus 5.5/HIGH review is LIVE under native session 44594**. Its final report, actual coverage, findings and adjudication remain **PENDING**. The requested coverage includes all 44 sections, 213 proof blocks, 258 manuscript renders and 86 selected primary/edition images, with 63 named obligations; a requested coverage ledger is not completed coverage. The final independent **DeepSeek V4-Pro cold read is NOT DISPATCHED**. Earlier scoped reviews do not accept the changed consolidated bytes.

Whole-argument review, final independent cold read and calibration/source adjudication remain open. There is **no whole-paper, novelty, human, circulation, publication or goal-completion clearance**. This page records internal project status and changes no theorem. `Progress.md` remains the authority for proof/review status.

**Lean boundary:** 80 accepted finite facts across 22 standalone seams; analytic inputs and consumers remain unformalized. The proposed official companion remains **L0 PROPOSED**, decision-point-4 approval is absent, and no companion package, lease or HPC authorization is implied. Finite kernel checks are not analytic or whole-argument verification.

**Delivery boundary:** workflow checkpoint `4463f3d9052b8a89df492cfdcc0f95eab3ecf97d` records restored research/canonical <HUB> Git synchronization and the matching current-PDF hash. It records delivery, not proof acceptance. This maintenance ticket was queued and then claimed; completion is established only by its exact terminal receipt and published wiki commit.

## Historical proof status — through 2026-10-28

The following rounds, failures and source observations are preserved as history. Their “unfinished,” “now,” “remain” and Lean-count statements describe their original checkpoints; the current status above supersedes them.

**Round 3: reviewed partial upper bound, 2026-10-27.** Under the original nonnegative homogeneous covariance assumptions, the notes prove

$$
\mathbb E u^2(t,x)\le\exp(Ct^\kappa)
$$

for **0 < α ≤ 1 in d = 1,2,3**, with an explicit finite constant. This includes spatial white noise in d=1; degree-one covariance in d=2,3 is spatially correlated, not full spatial white noise. The proof retains a degree-dependent spatial bound, then sums temporal pairings before using time-order symmetry. The α=1 endpoint uses a separate polar-measure/Gaussian Fourier calculation.

Claude Opus 5.5 returned **PASS_WITH_NOTES/high**, all twelve checks passed, complete source delivery verified, no required repairs. The final source differs from the reviewed candidate only by status promotion; proof and statement bodies are byte-identical. This is a mathematical review, not Lean verification, a novelty audit or circulation clearance.

The **full 1 < α < 2−α₀ range in d=2,3 and the sharp constant remain unfinished**. Le reactivated the full goal on 2026-10-28 UTC. The private Lean companion is still proposed, not created, pending decision point 4.

**Round4 candidate, not accepted.** Section6 gives a conditional transfer from a uniform spatial convolution maximum and Riesz applications in d=3 for $1<\alpha<2-\alpha_0$, and d=2 for $1<\alpha<\min\{3/2,2-\alpha_0\}$. Two native Opus reviews returned PASS_WITH_NOTES/medium, all nine checks passed, no required repairs; the second verified complete source delivery. The configured high-confidence gate remains unmet. A fresh DeepSeek V4-Pro cold read returned concerns that were adjudicated, but its source access was incomplete and strict prior-blindness was limited by a source-manifest read. It does not upgrade the Opus confidence or grant clearance. Exact evidence and source followup are retained at Article checkpoint `e356037dd11dc9b7ea7da0dcb5137ac1b89dec77`.

**Accepted deterministic tool, 2026-10-28 UTC.** For the usual two-dimensional wave density, define

$$
I_\alpha(h;Z,W)=\int_0^h\int_{\mathbb R^2}G_u(y)G_{h-u}(Z-y)|W-y|^{-\alpha}\,dy\,du.
$$

For $3/2\le\alpha<2$, a uniform remote-point estimate gives

$$
I_\alpha(h;Z,W)\le C_\alpha h^{2-\alpha}G_h(Z).
$$

The constant is explicit and nonsharp. Covariance-only positive mass-one smoothing preserves it; the Green kernels remain unsmoothed. A stronger fractional-power form has the exact threshold $q\ge\alpha-1$ for $\alpha>3/2$ within $1/2<q<1$, and holds for every such $q$ when $\alpha=3/2$. The proof integrates time exactly, bounds the two focal singularities, and uses disk layer cake. Native Opus5.5 returned PASS_WITH_NOTES/high, all nine checks passed, complete delivery verified, no required repairs. Frozen proof and review evidence: Article checkpoint `5107781a7c7f813c277e8f50032659019f4942d5`, directory `reviews/2026-10-28-wc-probe/`.

This is **not a second-moment upper-bound extension**: temporal covariance factors, terminal-vertex cases, repeated merging and the required factorial denominator remain unresolved. No general anisotropic or d=3 extension, sharp constant, novelty, Lean certificate or circulation clearance follows. The canonical notes remain 31 pages; this auxiliary proof is retained separately in the review checkpoint.

G0 historical diagnosis: The full mixed-term expansion and a corrected derivation of the quadratic-exponential bound are written in the notes. The uniform-pairing majorant gave the weaker exponent

$$
\rho=\frac{4-\alpha-\alpha_0}{3-\alpha-\alpha_0},\qquad \kappa<\rho<2.
$$

The explicit majorant itself has this exponent; it therefore cannot deliver the target scale. Its coefficient denominator lacks a factor $(k!)^{\alpha_0}$. This is a no-go for the **uniform pairing estimate**, not for every possible use of Theorem 3.1 and not a lower bound on the actual moment. That bound is superseded by the target-scale proof in the α≤1 regime. Lean stays at L0; no companion exists.

[held back until the source author has been told]

What is known (all from the author version of [[papers/chen-25-time-dependency|Chen]], 64 pp., submitted to *Ann. Appl. Probab.*, SHA-256 `5f7385ca…`; arXiv v1 is superseded for Theorem 1.2):

- **First moment:** two-sided bounds $L_*\le\liminf\le\limsup\le L^*$ (Theorem 1.2, p. 3), not an exact limit; the exact limit is only predicted (p. 4).
- **Source second moment:** the crude bound $\mathbb{E}u^2(t,x)\le e^{Ct^2}$ (Remark 5.1, p. 37). Since $1<\kappa<2$, this is far from the right scale.
- **Lower bound for free:** $\mathbb{E}u^2\ge(\mathbb{E}u)^2$ gives $\liminf t^{-\kappa}\log\mathbb{E}u^2\ge2L_*$ (proved in the project notes). The conjectured constant $2^{(4-\alpha)/(3-\alpha)}L^*$ is larger, so the substantive lower-bound content is the extra factor $2^{1/(3-\alpha)}$.
- **All-$p$ conjecture:** $\lim t^{-\kappa}\log\mathbb{E}|u|^p=p^{(4-\alpha)/(3-\alpha)}L^*$ for $p=1,2,\dots$ (1.22), p. 6.
- **The named obstruction:** Chen's exact representation (Theorem 6.1) needs the monotone order of a single chain; Remark 6.3 (p. 42) calls this "the major reason why the current idea can not work for $\mathbb{E}u^p(t,x)$ for $p>1$".

Key technical facts the project starts from:

- $\mathbb{E}[S_n(g_n)]^2$ is an exact two-chain pairing integral (Theorem 4.1 (4.3), p. 22), and the full second moment adds cross terms $\mathbb{E}[S_mS_n]$, $m\ne n$.
- Theorem 3.1 (3.6) (p. 15) is a universal bound for exactly these two-chain integrals, including cross-pairings. Chen uses it only for integrability.
- For $p=2$, each of the two chains is still ordered; only the interleaving is lost. That is the opening for a two-clock representation.

G1 now supplies all fifteen white-space order-four diagrams, including their
pairing relabeling under chain exchange. Its exact static total-order-two
and total-order-four contributions are $t^3/3$ and $11t^6/540$. It also gives
Riesz order-two formulas and an explicit finite order-four integral
representation. These are finite coefficients, not asymptotic constants;
no disputed Chen–Hu white-noise constant is adopted. G1 received Opus
PASS_WITH_NOTES/high with all eight checks passed. The reviewed G0 section
was preserved unchanged. These finite checks were not used as substitutes for the new all-order proof.

## Historical approach — superseded by the current all-model route

1. **Gate G0, diagnosis (falsification first).** Write $\mathbb{E}u^2$ as two-chain pairing integrals; reproduce the $e^{Ct^2}$ bound and find where the exponent 2 enters instead of $\kappa$; decide with a counting argument whether Theorem 3.1 with Laplace-weighted kernels can reach $t^\kappa$, and record a no-go if not.
2. **Gate G1, calibration.** Explicit chaos orders 2 and 4 in $d=1$; the $\alpha_0\to0$ limit must match the time-independent exponent $(4-\alpha)/(3-\alpha)$ of [[papers/chen_hu-25-hyperbolic|Chen–Hu (2025)]].
3. **Gate G2, upper bound.** Proved for α≤1 by descending spatial endpoint integration, a common degree-dependent bound, full temporal Wick-sum symmetry, and direct coefficient summation. The remaining higher-α range needs another estimate; the sharp constant is not obtained.
4. **Gate G3, sharp constant.** A two-clock analogue of Chen's Theorem 6.1, and the matching [[concepts/large-deviations|large deviations]] for the time-randomized [[concepts/intersection-local-time|intersection local time]]; a lower bound beyond Jensen first.

Every new proof gets a cross-family adversarial review (Claude Opus 5.5 skeptic of a GPT-authored argument) before it counts.

## Scope boundary

[held back: collaborators' unpublished work]

## Timeline

- **2026-11-02 — resumed full goal; current authorized science/status refresh:** workflow `14d82c0`, science `8ce03ae`, 28 TeX / 214 proofs / 240 statements / 263 pages, unchanged 80 finite Lean facts / 22 seams. Current ledger v39 records 189 scoped HIGH, 22 unaccepted rows and three editorial deltas; calibration 010 remains unaccepted despite raw PASS/HIGH, while 011–019 and later 136/137 have bounded adoptions. Full MAIN remains UNGRADED 120 CHECKED / 94 LIMITED on `b4b6efc`; source/image/render/Kimi/whole-main/fresh-cold/private-delivery gates stay OPEN. Successor `tk-20261102-223931-codex-stratonovich-status-refresh` preserves failed `tk-20261102-052608-codex-stratonovich-main-depth` and the older blocked checkpoint without rewriting either.

- **2026-11-02 — terminal MEDIUM review; goal service BLOCKED:** expanded actual-law/application DeepSeek audit supplied all 28 TeX files and 17 previously omitted inputs; E01–E10 favorable, rebuttals accepted, 71 native members verified, confidence still MEDIUM with depth/image limits. Both MEDIUM verdicts immutable; all reviewers terminal, no queued retry. Required Kimi monthly429 still gives no report/read credit; await restored capacity or Le's explicit replacement direction. Full original all-model objective, HIGH/source/visual/synthesis/fresh cold gates and auxiliary Chen–Hu/Chen2023 source obligations remain unchanged. No whole-goal acceptance or user pause; scientific `887fbfbe`, 257-page PDF and conditional 80-fact/22-seam Lean boundary unchanged. Prior resumption maintenance completed at `984fe7b146648c88ed2f0f0ee72b588fcc555bcd`.

- **2026-11-02 — full goal resumed; terminal outcomes reconciled:** current scientific `887fbfbe`, 257 pages; old whole review unaccepted INCONCLUSIVE/medium, actual Kimi monthly429 with no credit, scoped cutoff production adoption and supplementary SF04 MEDIUM audit retained at their exact scopes. Whole/source/visual/synthesis/final cold gates OPEN.

- **2026-11-01 — historical live-review snapshot (now terminal and unaccepted):** intrinsic theorem `a880288` (30 HIGH checks) and occupation/white module `d041546`, packet `691f413` (31 HIGH checks), no required repairs. Consolidation `4a65c79`: 258 pages and 213 proof blocks; fresh whole-argument session 44594 LIVE, final report/coverage/adjudication PENDING; final DeepSeek V4-Pro cold read NOT DISPATCHED. Git checkpoint `4463f3d` restores delivery only. No whole-paper or goal clearance.

- **2026-10-31 — goal revised by Le:** derive the actual second-moment constant or complete variational formula, whatever the proof yields; matching Chen is no longer a required endpoint. Every original model and verification/scope boundary is retained.

- **2026-10-28 UTC — weighted two-wave tool:** accepted deterministic Riesz convolution estimate in d=2 for3/2<=alpha<2; Opus PASS_WITH_NOTES/high, all9checks passed. Article `5107781a7c7f813c277e8f50032659019f4942d5`. Temporal and all-order application remain open; no promotion of Round4's separate medium-confidence moment candidate.

- **2026-10-28 UTC — full goal reactivated:** completed a fresh DeepSeek cold read and source followup, preserving source-coverage limitations. Round4 remains a candidate; accepted Round3 scope unchanged. Article `e356037dd11dc9b7ea7da0dcb5137ac1b89dec77`.

- **2026-10-27 — Round 3 / partial G2:** target-scale upper bound for 0<α≤1 in d1,2,3, explicit constant; Opus PASS_WITH_NOTES/high, all12checks passed. Article `53e2817eafd9ed4de30f3acda6427629b61c71e0`. Stop at decision point5; higher-α and sharp-constant goals remain open, private companion awaits point4.

- **2026-10-27 — Round 2 / Gate G1:** all fifteen white order-four terms, exact static coefficient 11/540, Riesz formulas and explicit integral representation; Opus PASS_WITH_NOTES/high. Article `8358d58c40591922a971790827f10ebe576932e0`. Private companion creation is proposed, not performed.

- **2026-10-27 — Round 1 / Gate G0:** Claude Opus 5.5 skeptic: PASS_WITH_NOTES/high, all eight checks passed, complete source delivery verified; optional exposition findings retained. Article checkpoint `4ff2bca60e666482480596cc1e53b9be06750ea7`; findings adjudicated in `Progress.md`. Stopped before Round 2 and Lean L1.

## Files

- Canonical project folder and root loader: `<HOME>/Dropbox/workspace/svn/Article-Stratonovich-HAM-Second-Moment`, `HANDOFF.md`. Canonical master contains historical science and is **not** the current manuscript authority.
- Active clean research checkout: `<HOME>/.local/state/Le-AI-Lab/stratonovich-fixed-mask-young-wave`, branch `research/fixed-mask-young-20261031`; workflow evidence checkpoint `14d82c078a4b02a42fecebc61ef0de9ece0ccb80`.
- Current consolidated TeX/PDF: `notes/notes_stratonovich_ham_second_moment.tex` and `.pdf` in that research checkout, scientific source/PDF `8ce03ae09cca984b32aaddf3da0a6ded07f47ebc` (263 pages; exact current PDF hash above).
- Integrated modules: `notes/integrated_intrinsic_constant.tex`, `notes/integrated_occupation_ceiling.tex`, `notes/integrated_white_evaluation.tex`.
- Goal/status authority in the active checkout: `PROJECT-GOAL.md`, latest `Progress.md` entries, `reviews/2026-11-02-resumption/completion-obligations.md`, `README.md`; original source identities remain in `sources/SOURCE-MANIFEST.md`.
- Historical whole-argument native output: sibling state directory `../stratonovich-whole-argument-review-v1/native` from the active checkout; terminal and unaccepted. Coverage-recovery evidence: `reviews/2026-11-01-coverage-recovery/`. Follow latest `Progress.md` for current attempts.

### Historical file snapshot — 2026-10-28

The following 31-page description is preserved as the earlier snapshot, not the current manuscript.

- Local folder: `<HOME>/Dropbox/workspace/svn/Article-Stratonovich-HAM-Second-Moment`
- Main tex: `notes/notes_stratonovich_ham_second_moment.tex` (tracked PDF, 31 pp.; accepted Round3 plus unpromoted Round4 candidate)
- Governance: `AGENTS.md`, `PROJECT-GOAL.md`, `Progress.md` (workflow authority), `CODEX-START.md`
- Sources: `sources/SOURCE-MANIFEST.md` (hash-pinned author PDF with page pinpoints; SPDEForge TeX copies)
- Remote: <HUB> bare repository `<REMOTES>/Article-Stratonovich-HAM-Second-Moment.git`

## Collaborators

- [[people/chen-le|Le Chen]]

## Project relations

### Upstream
*(none yet)*

### Downstream
*(none yet)*

[held back: collaborators' unpublished work]

## Connections

- Related concepts: [[concepts/hyperbolic-anderson-model]], [[concepts/stochastic-wave-equation]], [[concepts/stratonovich-integral]], [[concepts/wave-anderson-skorohod-vs-stratonovich]], [[concepts/intermittency]], [[concepts/moment-bounds]], [[concepts/lyapunov-exponent]], [[concepts/intersection-local-time]], [[concepts/large-deviations]], [[concepts/wiener-chaos-expansion]]
- Related open problems: [[open-problems/wave-hyperbolic]]
- Anchor papers: [[papers/chen-25-time-dependency]], [[papers/chen_hu-25-hyperbolic]], [[papers/chen_deya_ea-23-hyperbolic]], [[papers/balan_conus-16-intermittency]], [[papers/balan_chen_ea-22-exact]]
