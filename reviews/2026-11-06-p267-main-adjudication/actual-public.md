# P267 scoped public report — external 267-page candidate integration

**Scope actually reviewed.** By task order this is NOT the whole-manuscript review. I reviewed: (i) the one genuinely new owned statement/proof in the candidate main module, `L:pairing-product-envelope` (prospective OWN215/formal241); (ii) the newly explicit source covariance law at author p9(2.11)/p13(2.24); and (iii) the changed consumer/attribution sites (002/006/007/008/010) against the retained baseline. All 112 full-literal frames were read as text. **No page image was delivered to this tool-free reader**; every image-fidelity claim below is explicitly text-limited.

**Model.** deepseek/deepseek-v4-pro. Prior Opus PASS_WITH_NOTES/MEDIUM (accepted=false) and its ThemeII.1 MEDIUM are immutable and are not rewritten or retried here.

---

## Required rows (24)

**R01 — CHECKED (text-level).**
Candidate `E:pairing-edge-norms` (F026, statement LF≈1005–1017 per F064; generic definitions near LF950 per F062) fixes \(d\ge1\), \(0<a<1\), finite positive \(\mu_e\) with \(\gamma_e=\int e^{i\xi\cdot x}\mu_e\ge0\), measurable \(A_e\subset(0,\infty)\), \(\nu_e=\Gamma_E(a)^{-1}\mathbf1_{A_e}\lambda^{a-1}d\lambda\),
\[N_0(G)=\int G,\quad N_{1,e}(G)=\int|\mathcal L G(\lambda,\xi)|\,\nu_e\mu_e,\quad N_{2,e}(G)^2=\int G(s,x)G(t,y)\kappa_e(s-t)\gamma_e(x-y).\]
The inner modulus is inside the spectral/Laplace integration; the second norm uses independent spatial variables \(x,y\); time integrations are positive; cross-label finiteness is stated for every \(l,e\). This matches long-proof §0/(A) and source (3.1)–(3.5) under the declared independent-\(y\) convention, not the literal repeated-\(x\) p14(3.5). *Remaining:* pixel presence of the p14 inner bars is not independently readable here (ledger F002/Audit F073 F01 assert it; layout text F008 cannot show it); no whole-parent acceptance.

**R02 — CHECKED (text-level).**
The proof at F026 (LF≈1020–1039) invokes `L:translated-covariance-CS` (OWN214) for the finite-cap stationary feature \(h_\lambda(t,r)e^{i\xi\cdot x}\), coefficient-one Cauchy–Schwarz and simultaneous-translation invariance, with Bochner/Fubini justified by finite \(\mu_e\) and capped \(\nu_e\). *Minor scoping note:* OWN214's statement (F018) is written for \(d\in\{1,2,3\}\), while the new lemma is stated for generic \(d\ge1\) and asserts the feature proof is dimension-free ("their only spatial input is the finite measure \(\mu_e\)"). Actual consumers use only d1/2/3, so this is harmless, but the generic-\(d\) extension of OWN214 is asserted, not restated as an own theorem.

**R03 — CHECKED.**
`E:pairing-convolution-norms` (F026 LF≈1039–1041): for one-sided \(F=G*H\), \(N_0(F)=N_0(G)N_0(H)\) and \(N_{1,e}(F)\le N_0(G)N_{1,e}(H)\), since \(|\mathcal LG(\lambda,\xi)|\le N_0(G)\) for \(\lambda\ge0\). Factor-2 preservation arises in R10, not here; the mass factor is exactly \(N_0(G)\) (the earlier kernel \(G\)). Every inherited factor is accounted for.

**R04 — CHECKED.**
Same equation: \(N_{2,e}(F)\le N_0(G)N_{2,e}(H)\) by zero-extending \(H\), translating in the stationary Hilbert feature space (norm-preserving), expressing \(G*H\) as a Bochner integral against the nonnegative density \(G\), and Minkowski. Both translations/zero extension are explicit; cross-label eligibility for every remaining edge is retained. No independently-shifted-kernel PSD is used.

**R05 — CHECKED.**
Admissibility in F026 (LF≈992–1004): \((Q,\iota)\) with \(Q_0,Q_1,Q_2\) partitioning kernel labels, \(|Q_0|=|Q_1|\), each edge of \(D\) used once on \(Q_1\) or twice on \(Q_2\), never both; **no incidence requirement**; the set \(\mathcal A_D\) is finite/nonempty. The statement is per-family \(\exists(Q,\iota)\) (finite max), not \(\exists Q\forall G\); no measurable selector and no common partition.

**R06 — CHECKED.**
F026 LF≈1046–1052: \(n=0\) gives both sides 1; two vertices on one chain give \(\le N_0(G_{\rm first})N_{1,e}(G_{\rm last})\) (with whichever chain empty, correct chronological labels); one vertex per chain gives \(N_{2,e}N_{2,e}\) via covariance CS. Both nonempty orientations are noted; zero kernels/measures/norms handled via the positive cap convention, and there is no division by a norm. The p16 swapped caption is addressed in Remark `R:source-case2-time-shift` item (iv) (F026), not silently adopted.

**R07 — CHECKED.**
F026 LF≈1053–1064: on a region with partner \(s_a\le s_p\), monotonicity of \(\kappa_{e_0}\) replaces \(s_v-s_a\) by \(s_v-s_p\); the endpoint integral contributes \(\int|\mathcal LG_v|\nu_{e_0}\mu_{e_0}=N_{1,e_0}(G_v)\) (the predecessor phase is inside the inner modulus); the region indicator is dropped by positivity **after** extraction.

**R08 — CHECKED.**
F026 LF≈1065–1070: if the partner \(a\) is terminal after removing \(v\), it integrates to \(N_0(G_a)\); full \(n-1\) induction supplies \(P_{\rm rest}\), yielding \(N_{1,e_0}(G_v)N_0(G_a)P_{\rm rest}=\frac12 N_0(G_a)[2N_{1,e_0}(G_v)]P_{\rm rest}\). HALF is derived from the **full** hypothesis, not assumed; no hidden inductive half.

**R09 — CHECKED.**
F026 LF≈1085 and the three-row table: \(i=0\) uses \(Q_0=R_0\cup\{a,b\}\), \(Q_1=R_1\cup\{v\}\), \(Q_2=R_2\); with \(|R_0|+1=|R_1|\) this gives \(|Q_0|=|R_0|+2=|Q_1|\), \(Q_2\) even; the printed p19 intersection typo is replaced by union; all labels covered; inherited edges keep their multiplicities and \(e_0\) is first once.

**R10 — CHECKED.**
F026 LF≈1087–1094: the inducted first-slot term is kept as \(N_{1,e_0}(G_v)[2N_{1,e_1}(F)]B_{\rm rest}\) and bounded by \(\frac12 N_0(G_a)[2N_{1,e_1}(G_b)][2N_{1,e_0}(G_v)]B_{\rm rest}\). \(Q_0=R_0\cup\{a\}\), \(Q_1=R_1\cup\{b,v\}\), \(Q_2=R_2\): one new mass, **two** new first slots, inherited \(e_1\) still first once (now on \(G_b\)), new \(e_0\) first once; exact HALF; no conversion to two second slots (the finite control \(1+2/\pi>1\) of F001/F006 shows the printed unmultiplied conversion cannot preserve the half).

**R11 — CHECKED.**
F026 LF≈1095–1102: second-slot term \(N_{1,e_0}(G_v)N_{2,e_1}(F)B_{\rm rest}\le \frac12 N_0(G_a)[2N_{1,e_0}(G_v)]N_{2,e_1}(G_b)B_{\rm rest}\); \(Q_2=R_2\cup\{b\}\) so \(e_1\) acquires its second occurrence (its first was in \(R_2\)), \(e_0\) first once; \(|Q_0|=|Q_1|\) and \(Q_2\) even. Counts check.

**R12 — CHECKED.**
F026 LF≈1104–1105: exhaustive trichotomy — domestic endpoint (covers an empty chain, since the nonempty chain's endpoint has a domestic partner), endpoints paired to each other, or both endpoint pairs cross/distinct. One-vertex chains fall into domestic or endpoint-pair; cross case assumes own-chain successors only when an internal partner exists.

**R13 — CHECKED.**
F026 LF≈1106–1109: Case 2 conditions on separate predecessors \((A,z),(B,w)\) and keeps the temporal argument \(r-q+A-B\) in relative time; the endpoint integral is bounded by \(N_{2,e}(G_u)N_{2,e}(G_v)\) via the **original** stationary covariance CS (coefficient one), translating each self pairing separately; spatial origins remain in the tests. No unjustified independently-shifted covariance PSD or discarded offset.

**R14 — CHECKED.**
F026 LF≈1114–1122: on \(\{s_a\le s_q\}\) endpoint \(v\) is removed (indicator independent of \((s_v,x_v)\)); on the complement the chain order \(s_p\ge s_a>s_q\ge s_b\) removes \(u\) instead; each endpoint's own-chain successor exists; each region gives possibly **different** admissible half-products \(P/2,P'/2\); the half-sum is \(\le\max(P,P')\). No common partition is assumed.

**R15 — CHECKED.**
F026 LF≈1127–1135: increase \(L\to\infty\) with monotone diagram/norm integrands; \(\mathcal A_D\) finite, so the max of finitely many nonnegative products passes to the limit without a measurable selector or uniform-in-order claim; positivity/zero handling avoids \(0\cdot\infty\); there is no hidden \(C^n\). This matches the long-proof §7 cap-to-full argument.

**SOURCE-LAW — CHECKED (text-only; images unavailable).**
From the primary **layout text** F070 p13 (2.24), \(\gamma^0_\delta(u)=\Gamma(\alpha_0)^{-1}\int_0^{\delta^{-1}}e^{-\lambda|u|}\,\lambda^{\alpha_0-1}d\lambda\) (the layout prints \(d\lambda/\lambda^{1-\alpha_0}\)); p9 (2.11) states \(\operatorname{Cov}(\dot W_\epsilon^{(\delta)},\dot W_{\tilde\epsilon}^{(\tilde\delta)})=\gamma^0_{\delta\vee\tilde\delta}(s-t)\gamma_{\epsilon+\tilde\epsilon}(x-y)\). By disjoint Laplace-frequency increments the common prefix is \(\lambda\le\min(\delta_j^{-1},\delta_h^{-1})=(\delta_j\vee\delta_h)^{-1}\) (inverse-maximum width); heat semigroup gives \(p_{\epsilon_j}*p_{\epsilon_h}=p_{\epsilon_j+\epsilon_h}\); the \(\Gamma_E(a)^{-1}\lambda^{a-1}\) weight and amplitude carry through; \(0\) is Lebesgue-null so \([0,L]\) equals \((0,L]\); generalized \(\Gamma\) is tested against heat functions/spectral multipliers. The candidate `E:pairing-source-covariance` (F026 LF≈869; printed as (3.10) per F067) reproduces exactly this. The candidate remark explicitly separates this covariance **identification** from (i) constructing the common family from \(W\) alone and (ii) the joint 005/006 source limits. *Remaining:* page-image pixels pp9/13 were not read by this tool; dependence is on F070 layout text plus author-only audit claims (F071/F075/F083).

**CONSUMER006 — CHECKED (conditional on named parents).**
`L:joint-fixed-order` (candidate LF≈1349–1432, F026): marked-tail envelope at unit damping is \(H^{k-1}(2A_M+B_M^2)\) with \(H=\max(1,2A,B^2)\), summed over \(k\) difference-of-products terms, uniform in all spatial vertex widths/caps/Green widths, \(F_0-F_\eta\le C_{k,T_1,T_2}(N_1^{1/\eta}(1)+N_2^{1/\eta}(1)^2)\to0\). Temporal cap removal is by positivity; d3 Green smoothing is removed at fixed positive noise widths; then fixed-\(\eta\) spatial limit, Cauchy, and the \(\delta<\eta\) positivity squeeze give the joint arbitrary-rate fixed-order limit; Green-before-noise; square **and cross** moments give \(Q_n+Q_n-2Q_n=0\). Consumes OWN004 (tails), OWN005 (spatial measure), OWN214 (inside the pairing lemma), and the new `L:pairing-product-envelope` (attribution changed in the diff F061). *Remaining:* 004/005/214 full internals and the interior of the owned lemma are consumed as clauses, not re-derived here; this is the construction premise for the later source-limit passes, which are supported only as far as those clauses hold.

**CONSUMER007 — CHECKED.**
`L:crude-corrected` (candidate LF≈1452–1504): for every admissible product \(q_0=q_1\), \(q_0+q_2/2=n\) (so \(2q_0+q_2=2n\)); coarse norms \(N_0=\theta^{-2}\), \(N_1\le C_0\), \(N_2\le C_0\theta^{-1}\) for \(\theta\ge1\); uniform-in-width constants before maximization/summation; \(\theta=\theta_0+n/t\); \(P_n=(2n)!/(2^nn!)\), \(P_n n^{-2n}\le2^n/n!\) from \((2n)!\le(2n)^{2n}\); factorial count and limit order (Green at fixed noise widths, then noise via `L:joint-fixed-order`). The re-pointing to the per-family lemma (diff F061) needs no fixed-\(Q\) assumption — the every-product envelope is what is used.

**CONSUMER008 — CHECKED.**
`L:vertex-crude` (candidate LF≈1522–1581): Wick with joint covariance (2.11) copied per-chain; terminal-chain reversal permutes widths and absorbs signs by evenness; edge spatial measure \(e^{-(\epsilon_j+\epsilon_l)|\xi|^2/2}\mu\) finite by (1.5); temporal domain \([0,(\delta_j\vee\delta_l)^{-1}]\); all cross-label norms bounded by OWN004 uniformly in widths via nonnegative transforms and nonnegative temporal quadratic forms; d3 Green smoothing removed first; \(D=\max(1,2C_0)\), \(D^{q_1+q_2}\le D^{2n}\), \(C_1=D^2\); ratio test gives \(\sum\sqrt{n+1}\,q_n(T)<\infty\). This is the vertexwise bound, not a completed mild-parent statement (009 is separate).

**CONSUMER010 — CHECKED (numerical majorant; loss retained).**
`P:envelope` (candidate LF≈1784–1836): homogeneous scales \(N_0=\theta^{-2}\), \(N_1=\theta^{\alpha+a-2}N_1(1)\), \(N_2^2=\theta^{-\beta}N_2(1)^2\); \(2N_0N_1\) and \(N_2^2\) both have degree \(-\beta\); \(K\ge\max(2N_1(1),N_2(1)^2)\) bounds every admissible product by \(K^k\,\theta^{-\beta k}\); factorial denominator \((k!)^{\beta-1}=(k!)^{3-\alpha-a}\); the scalar infimum over \(\theta\) and pairing sums occur only after \(Q\) is eliminated. The exponent loss \(\rho=\beta/(\beta-1)>\kappa\) and the sole-majorant lower growth are again stated; this is **not** the target-scale proof and not claimed as one.

**ATTRIBUTION002 — CHECKED (text-level; byte receipts are author/mechanical).**
Diff F061 and F064/F082: only the main module changes; 27/28 included modules byte-identical (F066); the new lemma/proof is explicit and not hidden in a remark; the five changed old proof bodies (P:mixed, L:joint-fixed-order, L:crude-corrected, L:vertex-crude, P:envelope) change attribution/every-product prose only with all inline/display/equation/align math spans equal; all 214 owned statement bodies retained; OWN214 proof body unchanged; old \(R:source-case2-time-shift\) (S071) is the only changed formal body and is expanded with explicit **qualifications "not corrections attributed to the source"** (F026 item (iv)). The finite exact-constant lemma is distinguished from proofs of its indirect applications, as required.

**LIMITS-DEPENDENCIES — CHECKED direction; several LIMITED parents.**
Dependency direction (F023, F058, F060): source covariance law (2.11)/(2.24) \(\to\) edge/mixed width data; OWN004/005/214 + owned pairing lemma \(\to\) fixed-order `L:joint-fixed-order` \(\to\) crude/vertex bounds \(\to\) mild/series (009/002); 010 is downstream; the independent upper (051) and intrinsic constant (204) are not financed by this pairing-lemma construction. The final constant theorem does **not** fund its own earlier steps. Correct d3 Green-before-noise, heat-sum/time-max, original amplitude, \(\Gamma_E(a)\) factor, and zero branch (\(u=1\), constant0) are retained. No new \(\sigma(W)\)-only point-field or uniqueness requirement is invented. *Unreconstructed/imported:* full 004/005/006 internals, the Friz–Hairer Young remainder (used only in later F/G/H sections), and the later operator/phase material — all named, not silently accepted.

**PRESERVATION — LIMITED (custody evidence, not scientific acceptance).**
The receipts (F061 main diff; F064 body/formal delta; F066; F082/F084 independent custody) support: 28 modules with only the main file differing; 215/241 honest counts; 209/214 old proof bodies byte-identical; five attribution-only changes; OWN214 body unchanged; labels added, none removed. I cannot reproduce hashes without code; byte-equality of math spans does not by itself establish the correctness of the new application, and it is not a full visual or scientific gate.

**GLOBAL-SCOPE — NOT_READ (out of assigned scope / images not delivered).**
This report establishes only: the compact owned pairing lemma is internally coherent at text level; the source covariance law matches the primary **text** at pp9/13; and the four consumers' attribution/envelopes are consistent with the lemma. It does **not** establish the all-model upper/constant theorem, integrated MAIN HIGH, Kimi participation, source-image/full-267 visual clearance, fresh cold read, or delivery gates. Images were not delivered to this tool-free reader, so no new visual credit is claimed. Prior MEDIUM, current-SOURCE-INTERNAL-DISCREPANCY source verdict, and the 263-source acceptance state are not rewritten.

---

## Findings

**Fatal:** none located in the scoped candidate text.

**Major:** none located.

**Minor:**
1. Generic-\(d\) scope: the new lemma (d≥1) invokes OWN214 (`L:translated-covariance-CS`), whose stated domain in the baseline is \(d\in\{1,2,3\}\). The dimension-free extension is asserted by the candidate ("applies in any finite dimension"). Harmless for the actual d1/2/3 consumers; should be stated explicitly when used by the generic-d lemma.
2. The p14 inner-absolute-bars/repeated-\(x\) confirmations are pixel-dependent; this text-only review relies on F008 layout (which drops bars) plus ledger/audit claims (F002, F073-F01). Not independently re-verified here.
3. The full-parent internals 004/005/006 and the later Young/operator foundation remain consumed clauses, not independently re-derived.

**Required repairs:** none blocking for the scoped candidate review. Recommended before adoption: (i) state the generic-dimension extension of the translated-CS proof once; (ii) obtain actual image verification of p14(3.4) bars and pp9/13 pixels through an image-capable gate; (iii) finish full-parent reconstruction and the required Kimi/cold/visual gates.

## Source/application and image limitations

No image pixels were readable in this tool-free session. Author-pixel/audit claims (F071–F076, F083) and draft-render claims (F067) are evidence only. All source-page math statements above rest on the delivered **text** (F008–F015 layout text, F070 full layout) and the candidate TeX (F026).

## Text inventory actually used for the derivations

F001 (long proof), F002/F003/F004/F005 (author repair/quantifier), F006/F007 (controls), F008–F015 (pp14–21 layout), F016–F022 (current-source clauses), F023 (application map), F026 (candidate main), F027 (baseline main), F061 (exact diff), F062/F064/F065/F066/F067/F068/F069 (integration/preservation receipts), F070 (full64 layout text), F071–F076 (author audit), F077–F079 (immutable prior Opus), F082/F084 (independent preservation), F110/F112 (historical native reports as evidence only). Images: **not delivered**.

## Verdict and confidence

**Verdict (scoped to the assigned external 267-page candidate integration, source covariance law, and application attribution): PASS_WITH_NOTES.** The owned pairing lemma's statement/proof are mathematically coherent at the text level with exact \(2N_1/N_2\) factors, edge multiplicities, HALF/Case-2/Case-3 bookkeeping, cap passage and per-family quantifier; the source covariance identification matches the primary text pp9/13; the changed consumers are consistent envelopes of the lemma.

**Confidence: medium.** HIGH is not granted: no image reading, several full parents remain named/conditional, and the whole-paper integrated MAIN acceptance is explicitly out of scope. The prior Opus MEDIUM and ThemeII.1 MEDIUM remain unchanged.