# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

I compared the complete OLD and NEW scientific views for `notes/no-go/pairings.tex` at the two pinned revisions, proof by proof, including the statements, all proof paragraphs, and the following outside-proof explanatory prose. The NEW revision only adds step-level roadmap sentences and `\texttt{Step n}` headings to five proofs (P:nogo-02, P:nogo-03, P:nogo-04, P:nogo-05, P:nogo-18); the scientific derivations are byte-identical in mathematical content to OLD. The remaining five proofs (P:nogo-01, P:nogo-06, P:nogo-07, P:nogo-10, P:nogo-17) are unchanged in both statement and proof. I found no rewrite defect. All public reconstructions below were done independently from the supplied text; unchanged proofs are read, not hashed.

---

## P:nogo-01

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (no new prose added; unchanged proof)
- **Public reconstruction:** COMPLETE

**Original-step coverage.**

1. Compute the infimum: minimizing \(e^{2\theta t}\theta^{-\beta k}\) gives
   \[
   \theta_*=\beta k/(2t),\quad
   e^{2\theta_* t}\theta_*^{-\beta k}
   =e^{\beta k}\left(\frac{2t}{\beta k}\right)^{\beta k}.
   \]
   This is the step "the infimum equals \(e^{\beta k}(2t/(\beta k))^{\beta k}\)" and is exact.

2. Factorial controls. With \(P_k=(2k)!/(2^k k!)\),
   \[
   \frac{P_k}{k!}=\frac{(2k)!}{2^k(k!)^2}=\frac{\binom{2k}{k}}{2^k}.
   \]
   For \(k\ge1\) this is at least \(1\) (it equals \(1\) at \(k=1\), then grows), so \(P_k\ge k!\). Also \(P_k/k!=\binom{2k}{k}/2^k\le 4^k/2^k=2^k\), so \(P_k\le 2^k k!\). For the additional factor, \(k!/k^k=\prod_{j=1}^k (j/k)\) satisfies \(k!/k^k\le1\) and, since \(\log\prod(1-j/k)\ge k\int_0^1\log(1-u)\,du=-k\), we get \(k!/k^k\ge e^{-k}\).

3. Sandwiching \(B_K\). After substituting the infimum,
   \[
   B_K(t)=1+\sum_{k\ge1}(2k+1)P_kK^k e^{\beta k}\left(\frac{2t}{\beta}\right)^{\beta k}
   k^{-\beta k}.
   \]
   Using \((k!)^\beta/k^{\beta k}=(k!/k^k)^\beta\in[e^{-\beta k},1]\), and \(2k+1\le3^k\), and the two-sided \(P_k\) bounds, each summand lies between \(a^k t^{\beta k}/(k!)^{\beta-1}\) and \(b^k t^{\beta k}/(k!)^{\beta-1}\) for positive constants \(a,b\). This yields the claimed two series sandwich with \(q=\beta-1\).

4. Upper growth. With \(z=ct^\beta\) and \(p_k=z^{k/q}/k!\),
   \[
   \sum_{k\ge0}\frac{z^k}{(k!)^q}
   =\sum_{k\ge0}p_k^q\le\left(\sum_{k\ge0}p_k\right)^q
   =e^{qz^{1/q}},
   \]
   the \(\ell^q\le\ell^1\) step for \(q>1\).

5. Lower growth. For \(k=\lfloor z^{1/q}/2\rfloor\), \(z^k/(k!)^q\ge z^k/k^{qk}=(z^{1/q}/k)^{qk}\ge2^{qk}\), because \(z^{1/q}/k\approx2\). Thus the single summand grows at least exponentially in \(qk\), giving \(\log S(z)\gtrsim qz^{1/q}\) and preserving the two-sided order. Combining the sandwich constants proves \(\log B_K(t)\asymp t^{\beta/(\beta-1)}\).

6. Scale comparison. Since \(a=\alpha_0\in(0,1)\),
   \[
   \beta-1=4-\alpha-a-1=3-\alpha-a<3-\alpha,
   \]
   so
   \[
   \frac{\beta}{\beta-1}>\frac{\beta}{3-\alpha}=\kappa.
   \]
   Hence \(B_K\) grows on scale \(t^{\beta/(\beta-1)}\), too large to certify a bound of order \(\exp(Ct^{\kappa})\). Verdict follows.

**Lost steps/qualifiers:** none. **Concerns:** none. The phrase "upper constant on the scale \(t^\kappa\)" is the intended statement-local comparison; it takes the \(\kappa\) definition from the unassigned baseline `E:kappa`, whose hypotheses coincide.

---

## P:nogo-02

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (NEW adds an introductory roadmap sentence and splits the old paragraph into Step 1 / Step 2; no mathematical text changed)
- **Public reconstruction:** COMPLETE

**Original-step coverage (with NEW step structure).**

*Step 1 (root-forward integral and smoothing limit).*
1. Split \((0,2k)\), adjacent matching \((1,2),(3,4),\ldots,(2k-1,2k)\), root-forward chain increments \(h_i\) with \(\sum h_i<t\).
2. For each adjacent pair \((2j-1,2j)\), white contraction forces the two positions equal. The even Green factor at zero is \(G_{h_{2j}}(0)=1/2\); the preceding free increment integrates to its mass \(h_{2j-1}\). The temporal covariance factor is \(|s_{2j-1}-s_{2j}|^{-a}=h_{2j}^{-a}\). Hence
   \[
   J_{\rm adj}(t)=2^{-k}\int_{\sum h_i<t}\prod_{j=1}^k h_{2j-1}h_{2j}^{-a}\,dh.
   \]
3. Smoothing justification is stated and valid: Gaussian approximate identities let paired positions converge; the even Green factors are continuous at the diagonal value zero; the remaining wave-indicator boundary set is a finite union of hyperplanes of vanishing measure in the free spatial variables. On the spatial box \([-t,t]\) the replacement \(G\mapsto 1/2\) gives per disjoint smoothed pair at most \((1/4)(2t)=t/2\), i.e. the \(2^{-2k}(2t)^k\) bound; the temporal factors are a product of \(k\) disjoint integrable \(|\cdot|^{-a}\) factors since \(a<1\), so dominated convergence and the truncation limits apply. This is a fixed-order limit, not an all-order interchange.

*Step 2 (Dirichlet evaluation and factorial comparison).*
4. Dirichlet formula with exponents (parameters) \(2\) for each odd increment and \(1-a\) for each even increment:
   \[
   \int_{\sum h_i<t}\prod_j h_{2j-1}h_{2j}^{-a}\,dh
   =\frac{\Gamma_{\mathrm E}(1-a)^k}{\Gamma_{\mathrm E}\big(1+(3-a)k\big)}t^{(3-a)k},
   \]
   because the exponent sum is \(k(3-a)\) and the simplex-over-\([0,t]\) normalization contributes the \(+1\) in the gamma denominator. Multiplying by \(2^{-k}\) gives exactly the displayed \(J_{\rm adj}(t)\). Independent check at \(k=1\): \(\int_{h_1+h_2<t}h_1h_2^{-a}dh=8t^{5/2}/15\) for \(a=1/2\), while \(2^{-1}\Gamma_{\mathrm E}(1/2)/\Gamma_{\mathrm E}(7/2)t^{5/2}=(8/15)t^{5/2}\); consistent.
5. Stirling comparison. Writing \(N=(3-a)k\),
   \[
   \log\!\left((k!)^3J_{\rm adj}(1)\right)
   =3\log(k!)-k\log\tfrac{2}{\Gamma_{\mathrm E}(1-a)}
   -\log\Gamma_{\mathrm E}(1+N).
   \]
   Since \(\log\Gamma_{\mathrm E}(1+N)=N\log N-N+O(\log N)\) and \(N=(3-a)k\),
   \[
   3(k\log k-k)-(3-a)k\log k+O(k)
   =ak\log k+O(k).
   \]
   Since \(a>0\), this exceeds \(k\log C\) for every fixed \(C\) eventually, so no uniform \(C^k t^{(3-a)k}/(k!)^3\) diagram-by-diagram bound exists.

**Lost steps/qualifiers:** none. **Concerns:** none. The NEW Step 1/Step 2 headings correctly partition "compute + justify" from "growth comparison."

---

## P:nogo-03

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (NEW splits into Step 1/Step 2 and adds an accurate summary sentence)
- **Public reconstruction:** COMPLETE

**Original-step coverage.**

*Step 1 (first-order coefficients).*
1. For \(\Gamma(x)=c|x|^{-\alpha}\), length-two chain \(a_1=\E X_2(1,x)\). With increments \(h_1,h_2\), the spatial integral is
   \[
   \int G_{h_1}(y_1)\int G_{h_2}(y_2-y_1)c|y_1-y_2|^{-\alpha}dy_2dy_1
   =\frac{c\,h_1h_2^{1-\alpha}}{1-\alpha},
   \]
   because \(G_{h_2}\) has mass \(h_2\) and \(\int_{-h_2}^{h_2}|u|^{-\alpha}du=2h_2^{1-\alpha}/(1-\alpha)\) with the factor \(1/2\) from \(G\). Temporal factor \(h_2^{-a}\). Then
   \[
   \int_{h_1+h_2<1}c h_1h_2^{1-\alpha-a}\,dh
   =\frac{c}{(1-\alpha)(2-\alpha-a)(3-\alpha-a)(4-\alpha-a)}=a_1.
   \]
   The four ordered factors appear from \(\Gamma(2)\Gamma(2-\alpha-a)/\Gamma(1+4-\alpha-a)\); at \(\alpha=a=1/2\), \(a_1=1/3\).
2. Uniform pair: for \(U\sim U[-s,s]\), \(V\sim U[-r,r]\), \(0<r\le s\),
   \[
   \E|U-V|=\frac1{2r}\int_{-r}^r\frac{s^2+v^2}{2s}dv
   =\frac{s}{2}+\frac{r^2}{6s}\le\frac{2s}{3}.
   \]
   Jensen with convex \(z\mapsto z^{-\alpha}\):
   \[
   \int G_s(x)G_r(y)|x-y|^{-\alpha}\,dxdy
   =sr\,\E|U-V|^{-\alpha}\ge sr\left(\E|U-V|\right)^{-\alpha}
   \ge(3/2)^\alpha s^{1-\alpha}r.
   \]
3. \(b_1\) lower bound. On the two triangles \(r<s\) and \(s<r\),
   \[
   \int_{0<r<s<1}s^{1-\alpha}r(s-r)^{-a}\,drds
   =\int_0^1 s^{2-a}s^{1-\alpha}\int_0^1\tau(1-\tau)^{-a}d\tau\,ds
   =\frac{1}{(1-a)(2-a)(4-\alpha-a)}.
   \]
   Doubling and multiplying by \((3/2)^\alpha\) gives the asserted lower bound. At \(\alpha=a=1/2\) this is \(\frac89\sqrt{3/2}>2/3=2a_1\).

*Step 2 (strict small-time failure).*
4. With \(z=t^\beta\), expansion of the second moment uses \(A_1=2a_1+b_1\), and the squared mean at amplitude \(\sqrt2\) has linear coefficient \(2(\sqrt2)^2a_1=4a_1\). Thus
   \[
   \E u^2=1+(2a_1+b_1)z+O(z^2),\quad
   (\E u_{\sqrt 2})^2=1+4a_1z+O(z^2).
   \]
5. Remainder justification: for nonnegative coefficients \((c_j)\) and \(0\le z\le z_0\),
   \[
   \sum_{j\ge2}c_jz^j
   =\sum_{j\ge2}c_jz_0^j\left(\frac{z}{z_0}\right)^j
   \le\left(\frac{z}{z_0}\right)^2\sum_{j\ge2}c_jz_0^j,
   \]
   requiring convergence of both series at a fixed \(z_0>0\), which the unassigned \(P:mixed\)-type expansion provides (also at amplitude \(\sqrt2\)). The Cauchy product for the squared mean is a nonnegative-coefficient series, so the same bound applies. Thus for small \(z\),
   \[
   \E u^2-(\E u_{\sqrt2})^2=(b_1-2a_1)z+O(z^2)>0,
   \]
   since \(b_1-2a_1>0\).

**Lost steps/qualifiers:** none. **Concerns:** none.

---

## P:nogo-04

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (NEW splits the original paragraph into Step 1/Step 2)
- **Public reconstruction:** COMPLETE

**Original-step coverage.**

*Step 1 (diagonal time contribution).*
1. Define \(K(s,r)=\int G_s(x)G_r(y)c|x-y|^{-\alpha}dxdy\). Local Riesz integrability (\(\alpha<1\)) and dominated convergence give continuity on \([0,1]^2\). Direct computation:
   \[
   K(s,s)=\frac{c}{4}\int_{[-s,s]^2}|x-y|^{-\alpha}dxdy
   =\frac{c\,2^{1-\alpha}s^{2-\alpha}}{(1-\alpha)(2-\alpha)};
   \]
   verifying by centering coordinates \(x+y,\,x-y\) gives \(\int (2s-v)v^{-\alpha}\) and the displayed difference \(1/(1-\alpha)-1/(2-\alpha)\).
2. With \(v=s-r\ge0\), \(H(v)=2\int_v^1K(s,s-v)ds\) is continuous and
   \[
   b_1=\int_0^1\int_0^1K(s,r)|s-r|^{-a}dsdr
   =\int_0^1v^{-a}H(v)dv,
   \]
   by splitting the two triangles (mirror symmetry gives the factor 2). Then
   \[
   H(0)=2\int_0^1K(s,s)ds
   =\frac{c\,2^{2-\alpha}}{(1-\alpha)(2-\alpha)(3-\alpha)}.
   \]

*Step 2 (boundary limit).*
3. For continuous \(H\), the measures \(\varepsilon v^{-1+\varepsilon}dv\) have unit mass on \([0,1]\), mass \(1-\delta^\varepsilon\to0\) on \([\delta,1]\), and continuity controls \([0,\delta]\). Hence
   \[
   (1-a)b_1=(1-a)\int_0^1v^{-a}H(v)dv\to H(0).
   \]
4. From P:nogo-03’s \(a_1\) formula,
   \[
   \lim_{a\uparrow1}a_1=\frac{c}{(1-\alpha)^2(2-\alpha)(3-\alpha)}.
   \]
5. With \(A_1=2a_1+b_1\),
   \[
   (1-a)\frac{A_1}{a_1}=2(1-a)+\frac{(1-a)b_1}{a_1}
   \to\frac{H(0)}{\lim a_1}=2^{2-\alpha}(1-\alpha)>0.
   \]
   Therefore \(A_1/a_1\sim 2^{2-\alpha}(1-\alpha)/(1-a)\to\infty\), so no constant \(C\) depending only on \(\alpha\) (including \(2^{4-\alpha}\)) works uniformly in \(a\).

**Lost steps/qualifiers:** none. **Concerns:** none.

---

## P:nogo-05

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (NEW adds Step 1/Step 2 headings and summarizes)
- **Public reconstruction:** COMPLETE

**Original-step coverage.**

*Step 1 (positive original product, zero merged product).*
1. Horizon one, root \((0,0)\). Chain 1: times \((1/4,3/4)\), positions \((x,x)\), \(x=1/5\). Chain 2: times \((1/2,7/8)\), positions \((y,y)\), \(y=-2/5\).
2. Displacements/elapsed pairs:
   \[
   (1/5,1/4),\ (0,1/2),\ (2/5,1/2),\ (0,3/8).
   \]
   Each displacement is strictly less than its elapsed time (e.g. \(2/5<1/2\)), so all four Green factors equal \(1/2\); product \(=1/16=2^{-4}\).
3. Chronological merge produces times \(1/4,1/2,3/4,7/8\). The jump from \((1/4,1/5)\) to \((1/2,-2/5)\) has displacement
   \[
   |{-2/5}-1/5|=3/5>1/4=\text{elapsed},
   \]
   so that Green factor is zero. All displayed inequalities are strict, giving robustness.

*Step 2 (positive-measure persistence for both covariances).*
4. White covariance: choose domestic pairs inside each chain, so the delta contractions leave exactly the free variables \(x,y\). Near the displayed four times and \(x=1/5,y=-2/5\), strictness of \(|y-x|>1/4\) persists on open neighborhoods; the measure is positive in the contracted variables, and Gaussian regularization gives the contraction as in P:nogo-02.
5. Riesz covariance: perturb the four spatial positions independently in small neighborhoods avoiding the domestic diagonals. The original covariance factors are finite and positive; the merged zero jump persists. A positive-measure set remains, so no multiplier can bound the positive original product by the zero merged kernel pointwise.

**Lost steps/qualifiers:** none. **Concerns:** none. This is a pointwise/measure-contingent support obstruction; the after-proof scope statement (integrated comparisons remain possible) is preserved unchanged.

---

## P:nogo-06

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (no new prose; unchanged)
- **Public reconstruction:** COMPLETE

**Original-step coverage.**

1. Spatial replacement \(G\mapsto1/2\) on the box \([-t,t]\) with white contractions. Each of \(k\) pairings identifies two vertices, leaving \(k\) free spatial variables, each contributing mass \(2t\); the \(2k\) factors \(G=1/2\) contribute \(2^{-2k}\). So the spatial factor is \((2t)^k2^{-2k}=t^k/2^k\) for each pairing.
2. After this replacement, the pairing sum
   \[
   F_k=\sum_{D\in\Pi_k}\prod_{(i,j)\in D}|s_i-s_j|^{-a}
   \]
   is symmetric in the \(2k\) times. For a fixed pairing the disjoint pair-factorization gives, for a split \((m,n)\) simplex,
   \[
   \int_{[0,t]^m_< \times [0,t]^n_<}\prod_{\text{pairs}}|s_i-s_j|^{-a}ds
   =\frac1{m!n!}\int_{[0,t]^{2k}}\prod_{\text{pairs}}|s_i-s_j|^{-a}ds,
   \]
   because the ordered-simplex restriction divides the full cube into \(m!n!\) equal-volume ordering regions within the two chains. This is the precise meaning of "cube integral divided by \(m!n!\)".
3. Identities used:
   \[
   \sum_{m+n=2k}\frac1{m!n!}=\frac{2^{2k}}{(2k)!},\qquad
   P_k=\frac{(2k)!}{2^k k!},
   \]
   \[
   \int_0^t\int_0^t|s-r|^{-a}dsdr
   =\frac{2t^{2-a}}{(1-a)(2-a)}.
   \]
   The last follows by \(2\int_{0<t_1<t_2<t}(t_2-t_1)^{-a}\).
4. Multiply the counts: summing over splits and pairings gives
   \[
   \text{coefficient}\le\frac{t^k}{2^k}\cdot P_k\cdot\frac{2^{2k}}{(2k)!}\cdot
   \left[\frac{2t^{2-a}}{(1-a)(2-a)}\right]^k
   =\frac1{k!}\left[\frac{2t^{3-a}}{(1-a)(2-a)}\right]^k.
   \]
   Multiplying by \(t^{(3-a)k}\) gives the displayed majorant; its sum is the exponential with exponent \(2t^{3-a}/((1-a)(2-a))\). Since \(3-a>(3-a)/2\), the time exponent is too large.

**Lost steps/qualifiers:** none. **Concerns:** none. The after-proof scope sentences are unchanged and correct.

---

## P:nogo-07

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (no new prose; unchanged)
- **Public reconstruction:** COMPLETE

**Original-step coverage.**

1. Two length-\(k\) chains, common root, increments \(h_j,g_j\). The matching \(j\leftrightarrow k+j\) has label span \(k\) for every pair.
2. White contraction forces paired positions equal. For each \(j\), the two Green factors \(G_{h_j}(p_j-p_{j-1})\) and \(G_{g_j}(p_j-p_{j-1})\) integrate over the identified free position to \(\frac12\min(h_j,g_j)\); over \(k\) indices this is \(2^{-k}\prod_{j=1}^k\min(h_j,g_j)\).
3. Restrict \(s_j,r_j\in((j-\tfrac14)/k,\,j/k)\). Then each increment satisfies
   \[
   h_j=s_j-s_{j-1}>\frac{j-\tfrac14-(j-1)}k=\frac{3}{4k},
   \]
   and likewise \(g_j>3/(4k)\); each paired time difference satisfies \(|s_j-r_j|<1/(4k)\).
4. Volume of the time domain is \((4k)^{-2k}\). Hence
   \[
   J_k(1)\ge2^{-k}\left(\frac{3}{4k}\right)^k(4k)^{ak}(4k)^{-2k}
   =\left(\frac{3\cdot4^a}{128}\right)^{k}k^{-(3-a)k}.
   \]
5. Stirling comparison:
   \[
   \log\!\left((k!)^3J_k(1)\right)
   \ge3(k\log k-k)+(a-3)k\log k+O(k)
   =ak\log k+O(k),
   \]
   contradicting any bound \(J_k(1)\le C^k/(k!)^3\) uniformly in \(k\).
6. The Gaussian-smoothing limit is justified as in P:nogo-02 for fixed \(k\).

**Lost steps/qualifiers:** none. **Concerns:** none. The statement carefully says "solely on account of their block-label span," and that qualifier is preserved.

---

## P:nogo-10

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (no new prose; unchanged)
- **Public reconstruction:** COMPLETE

**Original-step coverage.**

1. Parameters: \(t=5,a=1,b=3,T=4,x=(0,0),z=(1/2,0),w=(1/4,0)\). For \(v\) near \(2\),
   \[
   |w-x|=\tfrac14<v-a\approx1,\qquad |z-w|=\tfrac14<b-v\approx1,
   \]
   so \(y=w\) lies strictly inside both disks in the merge lens. Also \(|w-z|=\tfrac14<T-b=1\) and \(|x|=0<a\), so the displayed point is in the admissible set.
2. Hence an interior ball \(B_\varepsilon(w)\) lies in the merge lens. Inside a radius \(\rho<\varepsilon\), \(|w-y|^{-\alpha}\ge\rho^{-\alpha}\), which exceeds any prescribed \(M\) by taking \(\rho<M^{-1/\alpha}\). Therefore \(\operatorname{ess\,sup}_y|w-y|^{-\alpha}=\infty\).
3. Robustness: all the pointwise strict inequalities persist under small perturbations of the fixed data, so the infinite essential supremum holds on a full admissible parameter neighborhood.
4. Factorization: pair \((1,3)\) contributes \((b-a)^{-\alpha_0}c|z-x|^{-\alpha}\) to \(W\)'s context but does not depend on the merge variables \((v,y)\), while the pair \((2,4)\) factors \((T-v)^{-\alpha_0}|w-y|^{-\alpha}\) depend on \((v,y)\) and remain in the weighted integral \(W\). The temporal weight alone is bounded by \((T-b)^{-\alpha_0}\). Thus a uniform spatial-supremum pullout of \(|w-y|^{-\alpha}\) would produce \(\infty\cdot\)(unweighted bound), not a finite unweighted two-wave convolution bound.

**Lost steps/qualifiers:** none. **Concerns:** none (pre-existing, correctly flagged after the proof: infinite essential supremum does not imply divergence of \(W\), since \(\alpha<2\) makes the singularity locally integrable; the no-go claims only that the *finite uniform supremum pullout* fails).

---

## P:nogo-17

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (no new prose; unchanged)
- **Public reconstruction:** COMPLETE

This proof's transform identities are imported from the unassigned statement `P:clock-copy-obstruction`. I checked the hypotheses there (arbitrary nonzero covariance under `H:homog`, temporal exponent \(0<a<1\), \(0<\alpha<2\), \(a+\alpha<2\)) and they are compatible with the present application.

**Original-step coverage.**

1. Resolvent declaration:
   \[
   \mathcal R_\Gamma(q)=\int\frac{\mu(d\xi)}{q^2+|\xi|^2}.
   \]
   The imported identities are
   \[
   w_\theta(\lambda)=\frac{\lambda^{a-2}}{2\theta\Gamma_{\mathrm E}(a)}
   \left(\mathcal R_\Gamma(\theta)-\mathcal R_\Gamma(\theta+\lambda)\right),
   \qquad
   K_\Gamma=\int_0^\infty w_\theta(\lambda)d\lambda,
   \]
   \[
   J_{\Gamma,1}=\int_0^\infty\frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)d\lambda.
   \]
2. Positivity: \(\mu\ne0\) and, for every \(\lambda>0\),
   \[
   \mathcal R_\Gamma(\theta)-\mathcal R_\Gamma(\theta+\lambda)
   =\int\frac{\lambda(2\theta+\lambda)}{(\theta^2+|\xi|^2)((\theta+\lambda)^2+|\xi|^2)}\mu(d\xi)>0
   \]
   on some positive-\(\mu\) annulus, so \(w_\theta>0\).
3. Integrability: \(\mathcal R_\Gamma(q)\) is bounded below the sharp threshold and \(q\mapsto\mathcal R_\Gamma(q)\) decreases. Near \(\lambda=0\),
   \(\mathcal R_\Gamma(\theta)-\mathcal R_\Gamma(\theta+\lambda)=O(\lambda)\), so \(w_\theta(\lambda)=O(\lambda^{a-1})\), integrable since \(a>0\); for large \(\lambda\), \(w_\theta(\lambda)=O(\lambda^{a-2})\), integrable since \(a<1\).
4. Since \(0<2\theta/(2\theta+\lambda)<1\) for \(\lambda>0\), with \(w_\theta>0\),
   \[
   0<J_{\Gamma,1}<K_\Gamma.
   \]
5. Correlation comparison. \(v_\rho(u,v)=u+v-2\rho\min(u,v)\ge|u-v|=v_1(u,v)\) for \(-1\le\rho\le1\). The positive Laplace mixture
   \[
   \Psi_a(r,v)=\frac1{\Gamma_{\mathrm E}(a)}\int_0^\infty\lambda^{a-1}e^{-r\lambda-v\lambda^2/2}d\lambda
   \]
   is strictly decreasing in \(v\) (positive decreasing integrand in \(v\)). Substituted into
   \[
   J_{\Gamma,\rho}=\frac14\iint e^{-\theta^2(u+v)/2}h_\Gamma(u+v)
   \Psi_a(\theta|u-v|,v_\rho(u,v))\,du\,dv,
   \]
   this gives \(J_{\Gamma,\rho}\le J_{\Gamma,1}\), and \(J_{\Gamma,\rho}>0\) since \(\Gamma\ne0\) makes the integrand positive on a positive-measure set. This proves the full chain
   \(0<J_{\Gamma,\rho}\le J_{\Gamma,1}<K_\Gamma\).
6. Ratio at \(\alpha=1\). Homogeneity gives \(\mathcal R_\Gamma(q)=\mathcal R_\Gamma(1)/q\). Substituting,
   \[
   K_\Gamma=\frac{\mathcal R_\Gamma(1)}{2\theta^2\Gamma_{\mathrm E}(a)}
   \int_0^\infty\frac{\lambda^{a-1}}{\theta+\lambda}d\lambda,
   \]
   \[
   J_{\Gamma,1}=\frac{\mathcal R_\Gamma(1)}{\theta^2\Gamma_{\mathrm E}(a)}
   \int_0^\infty\lambda^{a-1}\left(\frac1{\theta+\lambda}-\frac1{2\theta+\lambda}\right)d\lambda.
   \]
   Using
   \[
   \int_0^\infty\frac{x^{a-1}}{x+c}dx=c^{a-1}\Gamma_{\mathrm E}(a)\Gamma_{\mathrm E}(1-a),
   \]
   valid for \(0<a<1\),
   \[
   K_\Gamma=\frac{\mathcal R_\Gamma(1)\Gamma_{\mathrm E}(1-a)}{2}\theta^{a-3},
   \]
   and
   \[
   J_{\Gamma,1}=\mathcal R_\Gamma(1)\Gamma_{\mathrm E}(1-a)\theta^{a-3}
   (1-2^{a-1}).
   \]
   Hence
   \[
   \frac{J_{\Gamma,1}}{K_\Gamma}=2(1-2^{a-1})=2-2^a.
   \]

**Lost steps/qualifiers:** none. **Concerns:** none. I note explicitly that the first two transform identities are imported from the unassigned proposition, not re-derived inside this no-go; the no-go's own deduction (strictness, monotonicity, and the \(\alpha=1\) ratio) is fully reconstructed above.

---

## P:nogo-18

- **Old reading:** COMPLETE
- **New reading:** COMPLETE
- **Argument preservation:** PRESERVED
- **New explanations:** JUSTIFIED (NEW adds Step 1/Step 2/Step 3 and a clarifying preamble; no mathematics changed)
- **Public reconstruction:** COMPLETE

**Original-step coverage**, following the NEW step structure.

*Step 1 (actual wave transform).*
1. Spatial factor of the white middle-cross \((1,3)\) diagram:
   \[
   \int G_u(X)G_v(Y)G_w(X-Y)G_z(Y-X)dXdY,
   \]
   where \(|X-Y|\le\min(w,z)\). Setting \(R=u+v,q=u-v\), the stated area identity for
   \[
   A(C)=\big|\{|X|<u,\ |Y|<v,\ |X-Y|<C\}\big|
   \]
   is
   \[
   \frac{d}{dC}A(C)=2\big(R-\max(C,|q|)\big)_+,
   \qquad A(0)=0.
   \]
   This is the convex-geometry derivative of the intersection of two intervals in dimension one (the spatial integrals are over one-dimensional \(X,Y\)); it is a standard piecewise-linear area count and is consistent at \(C=0\) (zero area). Integrating against \(e^{-R}/32\) for \(R>|q|\) (accounting for the four factors \(1/2\) and the change of variables) gives the stated exact expression
   \[
   I=\frac1{16}\int_{w,z>0}\int_{\mathbb R}
   e^{-b(w+z)-\lambda|q-w|}
   \int_0^{\min(w,z)}e^{-\max(|q|,t)}dt\,dq\,dw\,dz.
   \]
2. Integrate \(z\ge t\) and substitute \(w=t+x\): \(dt\,d(w,z)=dt\,dx\,dz\), bringing \(t\) into \([0,z]\), \(x\ge0\). Splitting the \(q\)-integral at \(q=0\) and \(q=t\) produces three elementary Laplace-type terms, claimed to be:
   \[
   \frac{1/c+1/(2b+\lambda+1)}{16b(b+\lambda)(2b+2\lambda+1)},\qquad
   \frac1{16b(b+\lambda)(2b+1)(2b+1+\lambda)},
   \]
   \[
   \frac{1/(b+\lambda)+1/c}{16b(2b+1)(b+1)}.
   \]
   I verified this split by independent substitution.

   *Check 1, \(b=c=1\) (\(\nu=\lambda=0\))*: the three pieces become \(1/36,\ 1/144,\ 1/48\), which sum to \(8/144=1/18\). The closed form \(I=8/144=1/18\). Consistent.

   *Check 2, \(b=2,c=1\)*: the pieces are \(3/800,\ 1/1600,\ 1/320\), summing to \(6/1600+1/1600+5/1600=12/1600=3/400\); the closed form \(18/2400=3/400\). Consistent.
3. The addition of the three pieces gives the displayed closed form
   \[
   I=\frac{2b^2+4bc+2c^2-c+1}
   {8bc(b+1)(2b+1)(b+c-1)(2b+2c-1)}.
   \]
   I verified the closed form at both sample points above.

*Step 2 (root kernel and shift factor).*
4. For the clock envelope, \(h(r)=(2\pi r)^{-1/2}\) and \(m(s)=1/(\pi\sqrt2\sqrt{s-1/2})\). The covariance matrix of the two pair differences is
   \[
   \begin{pmatrix}u+v+w&-w\\-w&w+z\end{pmatrix},
   \]
   whose determinant with \(r=w+z\), \(R=u+v\) is
   \[
   (R+w)(w+z)-w^2=rR+rw+wz-w^2? 
   \]
   Correctly: \((R+w)(w+z)-w^2=R(w+z)+wz=rR+wz\). Hence the joint white density factors as \(h(r)h(R+wz/r)\).
5. The root kernel after deleting the nonnegative clock-overlap penalty:
   \[
   H_\gamma(q)=\int_{|q|}^\infty e^{-R/2}h(R+\gamma)dR
   =\int_{1/2}^\infty\frac{m(s)}{s}e^{-(s-1/2)\gamma}e^{-s|q|}ds,
   \]
   with \(\gamma=wz/r\). This equality is the positive Gamma/mixture representation of \(h(R+\gamma)\); substituting and integrating the exponential in \(R\) gives the second line. 
6. Convolution of the component \(e^{-s|q|}\) with \(e^{-A|q|}\) evaluated at \(w\):
   \[
   \int_{\mathbb R}e^{-s|q|}e^{-A|w-q|}dq=\frac{2S_{A,s}(w)}{s+A},
   \]
   \[
   S_{A,s}(w)=e^{-Aw}+\int_0^wAe^{-At}e^{-s(w-t)}dt\le1.
   \]
   The inequality holds because the second integral is bounded by \(\int_0^wAe^{-At}dt=1-e^{-Aw}\), and the sum is bounded by \(1\). Dropping the decreasing factor \(e^{-s(w-t)}\) (replacing \(S\) by \(1\)) is exactly the shift erasure.
7. Definition of the envelope: replacing \(S\) by \(e^{-\eta w}\), \(\eta\ge0\),
   \[
   M_b(\eta;A)=\frac1{16}\int_{1/2}^\infty\frac{m(s)}{s(s+A)}
   \int_0^\infty h(r)e^{-b^2r/2}
   \int_0^r e^{-(s-1/2)w(r-w)/r-\eta w}dw\,dr\,ds.
   \]
   All integrands are positive, as claimed.

*Step 3 (evaluation and comparison).*
8. Substitute \(w=rt\), \(\tau=s-1/2\), \(p=\sqrt{b^2+2\eta}\). The bridge integral
   \[
   \int_0^1\big[b^2+2\eta t+2\tau t(1-t)\big]^{-3/2}dt
   =\frac{2(p+b)}{bp\big((p+b)^2+2\tau\big)}.
   \]
   At \(\eta=\tau=0\) the integrand is \(b^{-3}\), the right side is \(4b/(4b^4)=b^{-3}\), consistent. Substituting \(z=\sqrt{2s-1}\) and partial fractions gives
   \[
   M_b(\eta;A)=\frac{p+b}{2\pi bp}
   \int_0^\infty\frac{dz}{(z^2+1)(z^2+c^2)(z^2+(p+b)^2)}
   =\frac{1+c+p+b}{4bp\,c(c+1)(c+p+b)(1+p+b)},
   \]
   using \(\int_0^\infty(z^2+q^2)^{-1}dz=\pi/(2q)\).
9. At \(\eta=0\), \(p=b\):
   \[
   M_b(0;A)=\frac{1+c+2b}{4b^2\,c(c+1)(c+2b)(1+2b)}.
   \]
10. Parameter evaluation at \(b=1,c=11/10\):
   \[
   I=\frac{2+4.4+2.42-1.1+1}
   {8\cdot1\cdot1.1\cdot2\cdot3\cdot1.1\cdot3.2}
   =\frac{218/25}{23232/125}
   =\frac{545}{11616}.
   \]
   Also
   \[
   M_b(0;A)=\frac{1+1.1+2}
   {4\cdot1\cdot1.1\cdot2.1\cdot3.1\cdot3}
   =\frac{41/10}{85932/1000}
   =\frac{1025}{21483}.
   \]
   The difference:
   \[
   I-M_b(0;A)=\frac{545}{11616}-\frac{1025}{21483}.
   \]
   Cross-multiplying, \(545\cdot21483=11\,708\,235\), \(1025\cdot11616=11\,906\,400\), difference \(-198\,165\). Denominator \(11616\cdot21483=249\,546\,528\); dividing numerator and denominator by \(33\):
   \[
   -\frac{198165}{249546528}=-\frac{6005}{7562016}<0.
   \]
   Hence \(M_b(0;A)>I\), disproving the pointwise closure \(M_b(0;A)\le I\).

**Lost steps/qualifiers:** none. **Concerns:** none. The after-proof qualifications are unchanged and correct: the boundary value \(\nu=0\) is legitimate, continuity gives a nearby positive-\(\nu\) overshoot, and the no-go does not refute the original shared-clock candidate \(J\le I\) nor decide an integrated comparison.

---

## Findings and limits

- **Readings:** All ten OLD and NEW statements/proofs read COMPLETE; all argument preservations PRESERVED; all new explanations JUSTIFIED. No rewrite defect found.
- **What NEW adds:** Only step-level roadmap headings/summary sentences in P:nogo-02, P:nogo-03, P:nogo-04, P:nogo-05, P:nogo-18. These are outside-proof administrative/organizing prose, ordered within the proof environments, and they do not alter any hypothesis, quantifier, normalization, range, obstruction scope, or formula.
- **Public reconstruction:** COMPLETE for all ten assigned proofs. Key rational arithmetic independently rechecked: P:nogo-02 Dirichlet normalization (including the \(+1\) in \(\Gamma_{\mathrm E}(1+(3-a)k)\)), the \(ak\log k\) comparisons in P:nogo-02 and P:nogo-07, the \(a_1,b_1\) coefficients in P:nogo-03/04, the support coordinates in P:nogo-05, the \(t^k/k!\) product in P:nogo-06, the merge-lens geometry in P:nogo-10, the \((2-2^a)\) ratio in P:nogo-17, and the rational values \(I=545/11616\), \(M_b(0;A)=1025/21483\), difference \(-6005/7562016\) in P:nogo-18, plus the intermediate rational-part checks in P:nogo-18.
- **Pre-existing vs new concerns:** No new concerns introduced by the NEW revision. Pre-existing (unchanged) text already carries its own scope qualifiers, e.g. the P:nogo-10 warning that infinite essential supremum does not imply divergence of \(W\), and the P:nogo-18 boundary/scope cautions. These are retained byte-mathematically and are scientifically sound. I identified no silent repair needed.
- **Unassigned inputs used:** The baseline `E:kappa`/model definitions, `P:mixed`, `P:envelope`, `P:d1-upper`, and `P:clock-copy-obstruction` contexts were used only to check normalization/application hypotheses where the assigned proofs invoke them. P:nogo-17’s own deduction was reconstructed independently from the imported transform identities; the imported proposition's proof itself is not part of this assignment and was not reviewed as such.
- **Limits:** This is readability-preservation review of the ten assigned statements/proofs only. It is not a skeptical synthesis, primary-source verification, Lean quotation, rendered-page, sign-off, whole-book, or release certification. No tools were used; all checks are hand arithmetic performed on the supplied embedded text.
