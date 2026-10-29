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

**Independent mild construction accepted at its own primary/HIGH gate.** Actual source `a7e725e4490513d55dd6ae5390ebcc3eeba84e48`,mathematical freeze `3705ad77ce44cc77c9865c442e420fbebdef62c9`:Opus5.5/HIGH775.593s,all19checksPASS,27required texts/36PNGimages complete and exact,no required repairs. The new vertexwise bound and independent mild equation have their own checksC18/C19;sourceSection5(ii) is no longer imported. All9minor findings adjudicated. Final92pages retain every formal statement and44of48proofs byte-for-byte;four proofs have explanatory clarifications. Exact final binding is in Article reviews/2026-10-29-mild-construction/final-status-binding.json. A fresh prior-blind whole-paper read remains required. All five old cold reports remain NOT CLEAR;no sharp,Lean,novelty or circulation claim.

**Independent mild-construction repair: new92page candidate,not yet reviewed.** The notes now include a uniform arbitrary-vertex regularization bound and a self-contained proof of the onefold Stratonovich mild equation. Coupled Gaussian multiplication,Bochner/Green limits and width-uniform order tails are explicit;sourceSection5(ii) is no longer imported. The moment estimate retains its separate dependency path and original constant. Two new proofs and two changed consumers;all earlier statements unchanged. Exact binding:Article reviews/2026-10-29-mild-construction/change-binding.json. Fresh19check primary/HIGH and cold are required. Complete36image carrier calibration precedes science. All five older cold reports remain NOT CLEAR;no sharp,Lean,novelty or circulation claim.

**Fifth cold read NOT CLEAR: mild-equation dependency needs closure.** DeepSeek V4-Pro read Article `20c5571301a9ccb67551e1ec5abb501761d787f9` in899.313s,24successful tools,actual partial source consultation. The core is described as coherent and checked parts correct,but item2 asks for proof that the mild identification survives the source's faulty uniform estimate(5.3). We must trace our corrected mixed-vertex bound through the onefold integral and width/order limits. All14items are adjudicated in Article reviews/2026-10-29-full-upper-cold-v5/adjudication-v1.md;the concrete repair plan remains UNREVIEWED. The17HIGHprimary is not a waiver. All five cold reports remain NOT CLEAR. Original full upper/sharp scope unchanged;no sharp,Lean,novelty or circulation claim.

**Explicit-justification revision accepted at the primary gate.** Fresh native Opus5.5/HIGH source `431a3d685752224da3ce480214f6d62562b19c1b` completed846.204s:all17checksPASS,23required texts/24PNGimages complete and exact,no required repairs. All8minor findings are adjudicated in Article reviews/2026-10-29-explicit-justifications/adjudication-v1.md. Final89pages retain all formal statements and44of46proofs byte-for-byte;the new finite-word lemma and critical fixed-split proof are exactly reviewed. Two minor explanatory proof paragraphs,pinpoints and status prose are clarified. Exact final binding is in final-status-binding.json. A fresh prior-blind read is next;all four earlier cold reports remain NOT CLEAR. No sharp,Lean,novelty or circulation claim.

**Fourth cold read: NOT CLEAR; repairs in progress.** DeepSeek V4-Pro read Article `27e9746433eec5afdb4fa2b58d01f34d044c7556` in886.086s,with15successful tools and partial source consultation. The report requests explicit colour/source reduction,nonselfadjoint estimates,metric monotonicity and finite-word/fresh-vacuum accounting. A valid missing real-part justification is now supplied;this repair is not yet re-reviewed. All15items are adjudicated in Article reviews/2026-10-29-full-upper-cold-v4/adjudication-v1.md. Historical16PASS/HIGH remains scoped to its reviewed source;all four cold reports remain NOT CLEAR. Original full upper/sharp targets unchanged;no sharp,Lean,novelty or circulation claim. Fresh primary/HIGH and then cold review follow actual repairs.

**Source-repaired chronological deduction accepted at the primary gate.** Fresh native Opus5.5/HIGH source `ec7a9c4449eb3f16b085c579f293813191bc5f1a` completed641.655s:all16checksPASS,complete19-text/24-image delivery,no required repairs,accepted=true. All8minor findings are adjudicated in Article reviews/2026-10-29-chronological-word/adjudication-v2.md. A final elementary doubled-polydisc Cauchy paragraph explains an already-asserted absolute convergence;every formal statement and44of45proofs match reviewed bytes,and the critical fixed-split proof is unchanged. Final86page adoption is Article `3b248ea37c588055f2cc712606f5767be9d898e3`;hashes are in final-status-binding.json. Originalv1remainsUNACCEPTED;carrier calibration is not a mathematical vote and its format rejection remains. All three older cold reports remain NOT CLEAR for their source versions. A fresh prior-blind full-paper read of the final bytes is next;no sharp,Lean,novelty or circulation claim.

**Chronological review:16PASS/HIGH but UNACCEPTED source carrier.** Native review of source `dcbed86f599bbd505754ebe91963ecbd928e7c2b` completed715.188s with all16checksPASS and no mandatory mathematical repairs. All18required texts and22of23images were exact;one direct PNG Read returned JPEG. The old receipt stays accepted=false/coverage_verified=false. Full failure/evidence is retained in Article reviews/2026-10-29-chronological-word/. Two overlapping direct-PDF windows now preserve all of sourcep2145. A separate24image carrier run verified every PNG byte;its legibility advisory had a format-rejected preamble,retained without relabelling or scientific credit. New immutable repaired-input review is next at the same HIGH threshold. Mathematical TeX/PDF remain the same86page candidate;no primary adoption or cold clearance.

**2026-10-29 chronological-word revision: CANDIDATE,86pages.** In response to the third cold report,the actual fixed-split proof now displays the common partition,every identity between phase norms,cross-vacuum subspaces,the complete word product,normalized Cauchy integration and an explicit finite constant. The unequal-chain proof and limit trace are clarified. A direct Chen--Hu source-class audit uses the explicit generalized-covariance convention on printedp2152;the coefficient rate is imported from(5.15),not inferred from variational finiteness. All formal statements remain unchanged;five proof bodies are revised. Fresh16check Opus/HIGH review is next,with18required texts and23source-page images. The old15HIGH verdict applies to the earlier source,not this rewrite. Exact candidate source/PDF hashes are in Article reviews/2026-10-29-chronological-word/change-binding.json. All earlier cold reports remain NOT CLEAR;no new sharp,Lean,novelty or circulation claim.

**Round 3: reviewed partial upper bound, 2026-10-27.** Under the original nonnegative homogeneous covariance assumptions, the notes prove

$$
\mathbb E u^2(t,x)\le\exp(Ct^\kappa)
$$

for **0 < α ≤ 1 in d = 1,2,3**, with an explicit finite constant. This includes spatial white noise in d=1; degree-one covariance in d=2,3 is spatially correlated, not full spatial white noise. The proof retains a degree-dependent spatial bound, then sums temporal pairings before using time-order symmetry. The α=1 endpoint uses a separate polar-measure/Gaussian Fourier calculation.

Claude Opus 5.5 returned **PASS_WITH_NOTES/high**, all twelve checks passed, complete source delivery verified, no required repairs. The final source differs from the reviewed candidate only by status promotion; proof and statement bodies are byte-identical. This is a mathematical review, not Lean verification, a novelty audit or circulation clearance.

The full upper scale has a written Section13 proof for the original class, including **1 < α < 2−α₀ in d=2,3**. Its earlier versions passed scoped correctness reviews; the current terminal/modular revision passed a fresh fifteen-check primary review after two cold reads raised substantive assembly concerns. A third blind whole-paper read has now returned substantive concerns;see the latest checkpoint below. The sharp constant remains unfinished. Le reactivated the full goal on 2026-10-28 UTC. The private Lean companion is still proposed, not created, pending decision point 4.

**Later higher-exponent candidates, still unaccepted.** The current notes have 86 pages. Sections7/8 contain the Riesz/static interpolation and full admissible planar covariance candidates. Expanded Section9 includes plane-supported endpoints, invertible-linear/finite-positive-sum closure, their actual moment applications and a nonsharp variational limsup bound. Its fresh primary Opus review passed all **17 checks**, with complete source delivery and no required repairs, but returned **medium** confidence; `accepted=false` at the unchanged high threshold. Section7/8 likewise remain below that threshold. No full-goal or scope promotion follows. Expanded assembly: Article `92a3eed518f10cc9797f1660050da8e69dcc644d`; review disposition `67b4211f8822449aa78b6d6d3acd6cdd9327eefe`, `reviews/2026-10-28-endpoint-integration/adjudication.md`. The earlier 50-page Section9 review remains all14PASS/medium at `1f4b1702e135c0e6595f871fde7d0afe750f50ef`.

The upper-bound candidate uses current fixed-order existence and the separate published static coefficient machinery, not the suspect first-moment upper constant. The earlier source/calibration qualification at `52350ee57aa3e4ddfccc78ed92cb3195cd5ee20d` preserved all then-existing 27 proof bodies and 33 formal statements. The expanded assembly adds three statements/proofs and rewrites only the conditional transfer proof; Sections1--8 and the original targets stay byte-identical. The intended first-moment/Jensen calibration remains conditional. Arbitrary higher-exponent d3 covariance is outside those earlier endpoint arguments; no representation or uniformly controlled infinite approximation is asserted there. The different Section13 interval method below covers the original full class.

**Accepted additional deterministic endpoints, 2026-10-28 UTC.** A separate source-bound Opus review passed all six checks at high confidence, with complete delivery and no required repairs, for rotated plane-supported covariances with a common normal Dirac measure and tangential product powers whose sum is $s\in(0,1-\alpha_0)$, $\alpha=1+s$. Both endpoints preserve that normal measure; ordinary-density Hölder on a common underlying measure verifies the deterministic Gaussian comparison. Finite nonnegative sums with common $\alpha,\vartheta,\beta$ preserve the comparison. Evidence: Article `190b7e6a59683571dcadd27b90564ba877181a1c`, `reviews/2026-10-28-product-endpoints/plane-adjudication.md`. This is a deterministic auxiliary result, retained separately; the stochastic moment consumer remains below the high threshold, and no representation or density theorem for arbitrary d3 covariances is claimed.

**Accepted energy-identification lemma, 2026-10-28.** Section10 proves that the positive-measure physical quartic energy agrees with its Fourier form for every real Sobolev profile, including singular plane covariances. It imports Chen2023 Theorem1.1(1.5) only on Schwartz profiles, then uses two Cauchy--Schwarz estimates and strong density limits. The actual static variational functional and source-mollified Gaussian model are identified. Opus5.5 returned all eight checks PASS/high, complete required source delivery, no mandatory repairs. Evidence: Article source `27186474297ccdbbaba1be8b3b33b86e5632e55a`, disposition `734d0bfa1895b5d06360b44b721f075f12e891b3`, `reviews/2026-10-28-energy-fidelity/adjudication.md`. This scoped acceptance does not promote the full moment argument or settle arbitrary-covariance factorization.

**Reviewed approximation screen, 2026-10-28.** A separate source audit and deterministic counterexample passed all six checks at high confidence with full source delivery. At an admissible singular plane covariance, angular Poisson approximants remain positive-definite covariances and retain their homogeneity, Gaussian pairing and spectral unit-ball mass, but their least scalar isotropic Riesz-envelope amplitudes diverge. Thus smoothing followed only by an angular-supremum Riesz majorant does not provide uniform constants. Rubin's real-parameter analytic-transform closure, checked in arXiv0704.0061v2, is not a positive ellipsoid-endpoint representation theorem; no global representation impossibility is claimed. Evidence: Article source `cd6b490803115e7051e2404e69fc48542d92a50b`, disposition `a79ee25`, `reviews/2026-10-28-general-covariance-cones/adjudication.md`. The full moment target remains open. A separate scalar time-block/velocity diagnostic is UNREVIEWED and supplies no SPDE estimate.

**Accepted first-variance static phase estimate, 2026-10-28.** Section11 treats the full stated spatial covariance class in dimension three, without an angular-density or endpoint-representation assumption. It bounds both the random first Duhamel phase and the mean second-order phase for arbitrary real Schwartz displacement/velocity data, uniformly in spatial smoothing, in the position L2/velocity negative-Sobolev phase norm. Their complete first-variance coefficient has the expected static block-length power. Opus5.5 passed all seven checks at high confidence, with complete source delivery and no required repairs. Evidence: Article source `8d8a43e32080c2c47e501b316cd833c510f2d261`, dispatch `aa57b91374b2a450bea8d842f45f0597ef7fba68`, disposition `e38e561`, `reviews/2026-10-28-phase-propagator/adjudication.md`. This is a first-variance estimate, not an all-order propagator, overlapping-time-block estimate or full HAM upper bound. The subsequent all-order static estimate has its own scoped review below; this first-variance report does not certify it.

**Accepted all regularized static phase orders, 2026-10-28.** Section12 proves a complex weak-phase estimate using the bounded-operator Crouzeix--Palencia theorem, a Gaussian-Fock sandwich retaining creation and annihilation, all static Duhamel orders, interaction estimates and finite independent successive-block bounds. Fresh native Opus5.5/high passed all nine checks, complete source delivery, no required repairs. All six optional findings are adjudicated. Scientific source: Article eb7d754fe4b88bcc9fb3cb37cacb9354fcacda1e; dispatch da197b3a95f86c4959b401bf988ed7d42a487493; disposition cba14f908c21488331570e88e312f917f41378be. Static growth exponents were already known; this is scoped arbitrary-phase/operator control, not a novelty verdict or an overlapping-time theorem. The first transport attempt failed DNS without a scientific report and does not count as a review.

**Historical full upper claim: earlier proof accepted at scoped correctness gate.** Section13 proves the original full correct-scale upper bound in every admissible dimension and homogeneous covariance, without angular-density or Riesz restrictions. Local Gaussian degrees, one-copy mean versus cross-chain terms and a positive inventory product retain the denominator $(k!)^{3-\alpha}$. Dyadic time-covariance domination and the current author's fixed-order construction then give the full-upper theorem (currently Theorem13.8). Fresh native Opus5.5/high returned PASS_WITH_NOTES/HIGH, all eleven checks PASS, complete eleven-text/seven-image delivery, no fatal/major findings or required repairs, accepted=true. All seven minor findings and source/AI limitations are adjudicated at Article reviews/2026-10-28-dyadic-overlap/adjudication-v1.md. Scientific source/dispatch bee4b2a3ebdff2ac1cbae9208f436084ad2ad549 is the frozen73page packet. The final74page notes update status/consistency and clarify one integral upper-bound phrase without changing any formula. This is scoped correctness acceptance, not a whole-paper cold read, formal verification, novelty or circulation clearance. The sharp constant remains open; PROJECT-GOAL decision5 now requires reporting to Le before further sharp-constant work.

**Complete cold read and proof expansion, 2026-10-28.** A fresh native DeepSeek V4-Pro read of source26bb560 received the complete manuscript/bibliography and consulted pinned sources inside an isolated packet. It returned fifteen items, including substantive difficulty following the interval counting, phase blocks, colored-chain limits and calibration premises. This is NOT cold-read clearance; a prior scoped HIGH verdict does not waive those concerns. Exact report/adjudication: Article b310b1191bd95516a1d112fb7dc718eb38367d8f, reviews/2026-10-28-full-upper-cold/. The source was expanded at ce11214e804eaf43abe2941b1b794fdddc3fb545: the then-78-page notes give explicit same-noise coefficients, joint Gaussian operator backgrounds, time-ordering cube, split weights, source joint-limit imports, terminal-chain Wick comparison, and limit/uniformity trace. Numerical L_star calibrations are locally conditional; original upper/sharp targets remain unchanged. Static covariance degree is now chi, distinct from the time coefficient power beta. The NEW complete primary Opus review passed all14checks/HIGH,full12text/14image delivery,no required repairs,617.957s;every optional finding is adjudicated in reviews/2026-10-28-cold-core-expansion/adjudication-v1.md. Final changes clarify notation,the Gaussian-amplitude sign convention and an already-checked scalar prefactor. A second prior-blind cold read subsequently returned two substantive assembly concerns; see the new checkpoint below. The earlier substantive report is not erased or converted into clearance. No sharp,Lean,novelty,publication or circulation clearance.

**Second cold read and new terminal/modular revision.** Fresh DeepSeek V4-Pro source `32ee0ce9f00a02558811162d42efb5cbc1ba09a3` received the complete 77-page blind manuscript and bibliography. It made zero tool calls: source texts were available but unconsulted, so no source-proof audit is credited. Its report is NOT CLEAR, with two substantive requests: explicit terminal-chain Wick kernels/factors and a separately stated fixed-split estimate. All nine items are adjudicated at Article `6f2dc0c1a3cab62bc213b29b5d1e368d6b026f0a`, reviews/2026-10-28-full-upper-cold-v2/. New source `65b134243de4ea91cdd4c8e1ca6315975c26979c` has 82 pages and 45 proofs, adding fixed-split, terminal-Wick and uniform-series-tail lemmas. The final full-series limit is proved from a uniform scaled finite-model bound and the known fixed-order input, rather than importing source Section5 convergence. The new deduction passed fresh native Opus5.5/HIGH review: all 15 checks PASS, complete 15-text/14-image delivery, no required repairs,636.876s. All six minor findings are adjudicated in reviews/2026-10-28-terminal-modular/adjudication-v1.md. Final clarifications retain every formal statement and43of45proofs byte-for-byte;the other two change only the recorded reviewer clarifications. Another prior-blind whole-paper cold read is required. The original sharp target remains open; no Lean, novelty or circulation clearance.

**Third full-paper cold read: NOT CLEAR.** Fresh native DeepSeek V4-Pro source `da0864bc4b688ba260ab648f487623b9b2da7928`, canonical mathematics `9054ece422489d278833c914b5b73569d2cbbb24`, returned after994.522s. Complete80page blind manuscript/bibliography and all45proofs were delivered;HEAD/input stability and actual model verified. There were32tool calls,one failed grep,with actual partial consultation of Chen current author,Chen--Hu,Chen2023,Crouzeix--Palencia and Balan--Conus. Exact report/coverage/adjudication are in reviews/2026-10-28-full-upper-cold-v3/. The main remaining concern is that L:fixed-split's operator-word and metric count is not independently followable at referee pace. Auxiliary generalized-measure static imports,unequal-chain exposition and uniformity tracking also need repair/audit. The reader found downstream inventory arithmetic and the geometric tail device consistent. Earlier primary15PASS/HIGH is retained as scoped evidence and does not waive these findings. Main notes remain82pages;no new proof rewrite is adopted yet. Fresh primary and blind gates are required after actual repair. No sharp,Lean,novelty or circulation clearance.

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

This is **not a second-moment upper-bound extension**: temporal covariance factors, terminal-vertex cases, repeated merging and the required factorial denominator remain unresolved. No general anisotropic or d=3 extension, sharp constant, novelty, Lean certificate or circulation clearance follows. At that auxiliary checkpoint the canonical notes had 31 pages; they now have 86 pages, with Sections7--9 unpromoted and Sections10--12 accepted only at their separate scoped gates; Section13 has fresh scoped terminal/modular acceptance and still awaits whole-paper cold clearance. The auxiliary weighted proof remains a separate, precisely scoped result.

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
3. **Gate G2, upper bound.** Proved for α≤1 by descending spatial endpoint integration, a common degree-dependent bound, full temporal Wick-sum symmetry, and direct coefficient summation. Section13 now covers the remaining higher-α range by independent interval fields, a uniform coefficient inventory bound and dyadic covariance domination. The sharp constant is not obtained.
4. **Gate G3, sharp constant.** A two-clock analogue of Chen's Theorem 6.1, and the matching [[concepts/large-deviations|large deviations]] for the time-randomized [[concepts/intersection-local-time|intersection local time]]; a lower bound beyond Jensen first.

Every new proof gets a cross-family adversarial review (Claude Opus 5.5 skeptic of a GPT-authored argument) before it counts.

## Scope boundary

[held back: collaborators' unpublished work]

## Timeline

- **2026-10-29 — chronological full-upper adoption:**Article `3b248ea37c588055f2cc712606f5767be9d898e3`,86pages;source-repaired primary16PASS/HIGH with all19texts24images. Final minor Cauchy clarification bound explicitly;fresh85page blind whole-paper packet ready. No cold or circulation clearance yet.

- **2026-10-29 — chronological-word candidate:**86pages,explicit word/metric/Cauchy/constant derivation;source-class and unequal-chain/limit repairs written. Fresh primary gate next;previous cold findings are not yet independently cleared.

- **2026-10-28 UTC — third whole-paper cold read:** source `da0864bc4b688ba260ab648f487623b9b2da7928`,994.522s,32tool calls with actual partial source consultation. NOT CLEAR:fixed-split transparency and auxiliary source/limit interfaces remain open. No new mathematical counterexample or circulation clearance is claimed.

- **2026-10-28 UTC — terminal/modular candidate after second cold read:** source `65b134243de4ea91cdd4c8e1ca6315975c26979c`, 82 pages and three new lemmas. Second blind report at `6f2dc0c1a3cab62bc213b29b5d1e368d6b026f0a` remains NOT CLEAR for its source. Revised deduction passed15checks/HIGH with full delivery and no mandatory repairs;fresh whole-paper cold clearance remains due.

- **2026-10-28 UTC — complete cold read and core exposition revision:** DeepSeek source26bb560 returned substantive concerns;NOT CLEAR. Adjudication b310b1191bd95516a1d112fb7dc718eb38367d8f. New78page source ce11214e804eaf43abe2941b1b794fdddc3fb545 expands the same full upper proof and conditions source-dependent calibrations;renewed primary14PASS/HIGH,full delivery,no required repairs;fresh cold read next. Original sharp goal retained.

- **2026-10-28 UTC — static all-orders and new interval candidate:** Section12 accepted9PASS/high, all source delivery, disposition cba14f908c21488331570e88e312f917f41378be. Full Section13 upper-bound proof frozen at bee4b2a3ebdff2ac1cbae9208f436084ad2ad549 passed all11checks/HIGH with full source delivery and no required repairs. Final74page notes adopt the ORIGINAL full upper scale; sharp constant,novelty,Lean and final whole-paper cold read remain open.

- **2026-10-28 UTC — 56page energy-fidelity checkpoint:** new Lemma10.1 and exact variational/source-field identification accepted all8PASS/high with full delivery. Scientific source `27186474297ccdbbaba1be8b3b33b86e5632e55a`, disposition `734d0bfa1895b5d06360b44b721f075f12e891b3`. Full moment argument remains MEDIUM and arbitrary covariance remains open.

- **2026-10-28 UTC — expanded54page assembly:** integrated plane endpoints, new invertible-linear Gaussian comparison and finite-sum moment consumers, with explicit pathwise/Bochner/eta0 source identification. Full17check review PASS_WITH_NOTES/medium, complete delivery, no required repairs; HIGH acceptance unmet. Assembly `92a3eed518f10cc9797f1660050da8e69dcc644d`, disposition `67b4211f8822449aa78b6d6d3acd6cdd9327eefe`.

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
- Main tex: `notes/notes_stratonovich_ham_second_moment.tex` (tracked PDF, 86 pp.;chronological-word candidate pending fresh primary and whole-paper review)
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
