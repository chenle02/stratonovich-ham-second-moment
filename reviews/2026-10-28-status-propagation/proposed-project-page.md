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

The two goals are:

1. **Upper bound at the correct scale:** $\limsup_{t\to\infty}t^{-\kappa}\log\mathbb{E}u^2(t,x)<\infty$.
2. **Sharp constant for $p=2$:** two-sided bounds
$$
2^{\frac{4-\alpha}{3-\alpha}}L_*\le\liminf_{t\to\infty}t^{-\kappa}\log\mathbb{E}u^2(t,x)\le\limsup_{t\to\infty}t^{-\kappa}\log\mathbb{E}u^2(t,x)\le2^{\frac{4-\alpha}{3-\alpha}}L^*,
$$
the $p=2$ case of Xia Chen's conjecture, up to the same gap $\mathcal{E}_*<\mathcal{E}$ as his first-moment theorem. The exact limit $2^{(4-\alpha)/(3-\alpha)}L^*$ is the conditional target.

Here $L_*=L(\mathcal{E}_*)$ and $L^*=L(\mathcal{E})$ are the constants of [[papers/chen-25-time-dependency|Chen (2025/26)]], Theorem 1.2 (1.10), in the current author version.

[held back until the source author has been told]

## Current state

**Round 3: reviewed partial upper bound, 2026-10-27.** Under the original nonnegative homogeneous covariance assumptions, the notes prove

$$
\mathbb E u^2(t,x)\le\exp(Ct^\kappa)
$$

for **0 < α ≤ 1 in d = 1,2,3**, with an explicit finite constant. This includes spatial white noise in d=1; degree-one covariance in d=2,3 is spatially correlated, not full spatial white noise. The proof retains a degree-dependent spatial bound, then sums temporal pairings before using time-order symmetry. The α=1 endpoint uses a separate polar-measure/Gaussian Fourier calculation.

Claude Opus 5.5 returned **PASS_WITH_NOTES/high**, all twelve checks passed, complete source delivery verified, no required repairs. The final source differs from the reviewed candidate only by status promotion; proof and statement bodies are byte-identical. This is a mathematical review, not Lean verification, a novelty audit or circulation clearance.

The **full 1 < α < 2−α₀ range in d=2,3 and the sharp constant remain unfinished**. Le reactivated the full goal on 2026-10-28 UTC. The private Lean companion is still proposed, not created, pending decision point 4.

**Later higher-exponent candidates, still unaccepted.** The current notes have 50 pages. Section7 gives Riesz interpolation with a static endpoint, Section8 gives the full admissible planar covariance argument, and Section9 gives a conditional general d3 transfer plus ordinary-product and isotropic-Riesz applications and a separate nonsharp variational limsup constant. Section9's primary Opus review passed all 14 checks with complete text/image delivery and no required repairs, but returned **medium** confidence; `accepted=false` under the unchanged high threshold. Section7/8 also remain below that threshold. No full-goal or scope promotion follows. Section9 evidence: Article `1f4b1702e135c0e6595f871fde7d0afe750f50ef`, `reviews/2026-10-28-product-endpoints/skeptic-adjudication.md`.

The upper-bound candidate uses current fixed-order existence and the separate published static coefficient machinery, not the suspect first-moment upper constant. The abstract/source warning and Section9 first-moment/Jensen calibration were qualified without changing any of the 27 proof bodies or 33 formal statements; canonical source/PDF checkpoint `52350ee57aa3e4ddfccc78ed92cb3195cd5ee20d`. The intended first-moment calibration is conditional until its normalization is clarified. Arbitrary higher-exponent d3 covariance remains outside the discharged endpoint families.

**Accepted additional deterministic endpoints, 2026-10-28 UTC.** A separate source-bound Opus review passed all six checks at high confidence, with complete delivery and no required repairs, for rotated plane-supported covariances with a common normal Dirac measure and tangential product powers whose sum is $s\in(0,1-\alpha_0)$, $\alpha=1+s$. Both endpoints preserve that normal measure; ordinary-density Hölder on a common underlying measure verifies the deterministic Gaussian comparison. Finite nonnegative sums with common $\alpha,\vartheta,\beta$ preserve the comparison. Evidence: Article `190b7e6a59683571dcadd27b90564ba877181a1c`, `reviews/2026-10-28-product-endpoints/plane-adjudication.md`. This is a deterministic auxiliary result, retained separately; the stochastic moment consumer remains below the high threshold, and no representation or density theorem for arbitrary d3 covariances is claimed.

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

This is **not a second-moment upper-bound extension**: temporal covariance factors, terminal-vertex cases, repeated merging and the required factorial denominator remain unresolved. No general anisotropic or d=3 extension, sharp constant, novelty, Lean certificate or circulation clearance follows. At that auxiliary checkpoint the canonical notes had 31 pages; they now have 50 pages including unpromoted Sections7--9. The auxiliary weighted proof remains a separate, precisely scoped result.

G0 historical diagnosis: The full mixed-term expansion and a corrected derivation of the quadratic-exponential bound are written in the notes. The uniform-pairing majorant gave the weaker exponent

$$
\rho=\frac{4-\alpha-\alpha_0}{3-\alpha-\alpha_0},\qquad \kappa<\rho<2.
$$

The explicit majorant itself has this exponent; it therefore cannot deliver the target scale. Its coefficient denominator lacks a factor $(k!)^{\alpha_0}$. This is a no-go for the **uniform pairing estimate**, not for every possible use of Theorem 3.1 and not a lower bound on the actual moment. That bound is superseded by the target-scale proof in the α≤1 regime. Lean stays at L0; no companion exists.

[held back until the source author has been told]

What is known (all from the author version of [[papers/chen-25-time-dependency|Chen]], 64 pp., submitted to *Ann. Appl. Probab.*, SHA-256 `5f7385ca…`; arXiv v1 is superseded for Theorem 1.2):

- **Printed first-moment statement:** two-sided bounds $L_*\le\liminf\le\limsup\le L^*$ (Theorem 1.2, p. 3), with the normalization qualification above. The exact limit is only predicted (p. 4); no corrected constants are assumed.
- **Source second moment:** the crude bound $\mathbb{E}u^2(t,x)\le e^{Ct^2}$ (Remark 5.1, p. 37). Since $1<\kappa<2$, this is far from the right scale.
- **Jensen inequality:** $\mathbb{E}u^2\ge(\mathbb{E}u)^2$ holds. Its calibration $\liminf t^{-\kappa}\log\mathbb{E}u^2\ge2L_*$ is conditional on the intended first-moment lower bound while the printed normalization is unresolved. The conjectured constant $2^{(4-\alpha)/(3-\alpha)}L^*$ is larger, so the substantive lower-bound content is the extra factor $2^{1/(3-\alpha)}$.
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

## Approach

1. **Gate G0, diagnosis (falsification first).** Write $\mathbb{E}u^2$ as two-chain pairing integrals; reproduce the $e^{Ct^2}$ bound and find where the exponent 2 enters instead of $\kappa$; decide with a counting argument whether Theorem 3.1 with Laplace-weighted kernels can reach $t^\kappa$, and record a no-go if not.
2. **Gate G1, calibration.** Explicit chaos orders 2 and 4 in $d=1$; the $\alpha_0\to0$ limit must match the time-independent exponent $(4-\alpha)/(3-\alpha)$ of [[papers/chen_hu-25-hyperbolic|Chen–Hu (2025)]].
3. **Gate G2, upper bound.** Proved for α≤1 by descending spatial endpoint integration, a common degree-dependent bound, full temporal Wick-sum symmetry, and direct coefficient summation. The remaining higher-α range needs another estimate; the sharp constant is not obtained.
4. **Gate G3, sharp constant.** A two-clock analogue of Chen's Theorem 6.1, and the matching [[concepts/large-deviations|large deviations]] for the time-randomized [[concepts/intersection-local-time|intersection local time]]; a lower bound beyond Jensen first.

Every new proof gets a cross-family adversarial review (Claude Opus 5.5 skeptic of a GPT-authored argument) before it counts.

## Scope boundary

[held back: collaborators' unpublished work]

## Timeline

- **2026-10-28 UTC — plane-supported/finite-sum endpoints:** accepted deterministic Gaussian covariance comparison, Opus/high, all6checks passed with complete source delivery. Article `190b7e6a59683571dcadd27b90564ba877181a1c`. The moment consumer remains a candidate; no arbitrary-covariance representation is supplied.

- **2026-10-28 UTC — full Section9 primary review:** all14checks PASS, complete source delivery, no required repairs, PASS_WITH_NOTES/medium; unchanged high gate unmet, no theorem promotion. Article `1f4b1702e135c0e6595f871fde7d0afe750f50ef`. Full d3 general-covariance and sharp goals stay open.

- **2026-10-28 UTC — scoped source-normalization audit:** Opus/high, all9checks PASS and complete exact source delivery; the printed variational definitions reverse their stated ordering under the finite-energy interpretation in an admissible white test. Intended correction unknown; no source-author contact or source/goal repair. Article `84572a371b666ad63cb0161f86832f72f435ae49`.

- **2026-10-28 UTC — weighted two-wave tool:** accepted deterministic Riesz convolution estimate in d=2 for3/2<=alpha<2; Opus PASS_WITH_NOTES/high, all9checks passed. Article `5107781a7c7f813c277e8f50032659019f4942d5`. Temporal and all-order application remain open; no promotion of Round4's separate medium-confidence moment candidate.

- **2026-10-28 UTC — full goal reactivated:** completed a fresh DeepSeek cold read and source followup, preserving source-coverage limitations. Round4 remains a candidate; accepted Round3 scope unchanged. Article `e356037dd11dc9b7ea7da0dcb5137ac1b89dec77`.

- **2026-10-27 — Round 3 / partial G2:** target-scale upper bound for 0<α≤1 in d1,2,3, explicit constant; Opus PASS_WITH_NOTES/high, all12checks passed. Article `53e2817eafd9ed4de30f3acda6427629b61c71e0`. Stop at decision point5; higher-α and sharp-constant goals remain open, private companion awaits point4.

- **2026-10-27 — Round 2 / Gate G1:** all fifteen white order-four terms, exact static coefficient 11/540, Riesz formulas and explicit integral representation; Opus PASS_WITH_NOTES/high. Article `8358d58c40591922a971790827f10ebe576932e0`. Private companion creation is proposed, not performed.

- **2026-10-27 — Round 1 / Gate G0:** Claude Opus 5.5 skeptic: PASS_WITH_NOTES/high, all eight checks passed, complete source delivery verified; optional exposition findings retained. Article checkpoint `4ff2bca60e666482480596cc1e53b9be06750ea7`; findings adjudicated in `Progress.md`. Stopped before Round 2 and Lean L1.

## Files

- Local folder: `<HOME>/Dropbox/workspace/svn/Article-Stratonovich-HAM-Second-Moment`
- Main tex: `notes/notes_stratonovich_ham_second_moment.tex` (tracked PDF, 50 pp.; accepted Round3 plus unpromoted higher-exponent candidates in Sections6--9)
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
