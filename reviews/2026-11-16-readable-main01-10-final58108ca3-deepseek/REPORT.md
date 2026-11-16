# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

Both the OLD block (`cdde711c`, LF 659–1962) and NEW block (`58108ca3`, LF 659–2145) were read in full for all ten assigned main ordinals. The NEW revision is byte-preserving on the mathematical content of every proof; its only additions are (i) a one-sentence roadmap at the top of each multi-step proof, (ii) numbered `Step k` headings partitioning the already-existing sentences, and (iii) a handful of clarifying sentences resolving notational or source-reference ambiguities. No displayed equation, hypothesis, qualifier, constant, or chain/fusion subcase was added, removed, or altered. Every added heading and remark is an accurate restatement of the sentence it labels, so argument preservation holds for all ten. Public reconstruction is COMPLETE for all ten; the only points I flag as *compressed pre-existing deductions* (common to both revisions) are the conditional removal step in the Brownian occupation-moment bound (proof 7, Step 2) and the reliance on the unassigned declarations `P:mild-construction`/`T:first` as stated boundaries — neither is an introduced defect.

Line-range accounting confirms: P:Jensen is byte-identical (OLD=NEW LF 659–684); L:white-test's proof is byte-identical (shifted by 23 lines); the other eight proofs gain only the roadmap/step/clarification text, all of which is expository. Details follow.

---

## P:Jensen
- Global main ordinal: 1
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. *Absolute summability of means.* By `L:vertex-crude` (assigned, ordinal 10), $\sum_n \|X_n(t,x)\|_2<\infty$. Since the underlying probability space has total mass one, $\|X_n\|_1\le\|X_n\|_2$, so $\sum_n \E|X_n(t,x)|<\infty$. The passage from $\|X_n\|_2$ summability to $\|X_n\|_1$ summability is exactly Hölder with $p=q=2$: $\E|Z|\le(\E Z^2)^{1/2}$.
  2. *Interchange of sum and mean.* Absolute $L^1$ summability (and the $L^2$ limit $U_N\to u$, equivalently $L^1$ on a probability space) gives $\E u=\sum_n \E X_n$.
  3. *Nonnegativity.* By `\eqref{E:expansion}` and the Wick pairings (2.20)–(2.21), $\E S_{2n}(g_{2n})$ is a sum over pair partitions of integrals of nonnegative integrands (for $m+n$ odd the terms vanish), and $S_0=1$, so $\E u \ge 1$.
  4. *Cauchy–Schwarz.* $\E u^2\ge(\E u)^2$. Since $\E u\ge1>0$, the logarithm is defined and
     \[
       t^{-\kappa}\log\E u^2 \ge 2\,t^{-\kappa}\log\E u.
     \]
     Taking $\liminf$ (a positive scalar $2$ commutes with $\liminf$, and $\liminf a_n\ge \liminf b_n$ when $a_n\ge b_n$ eventually) gives the implication for every real $\ell$.
  5. *Conditionality.* Substituting $\ell=L_*$ is explicitly flagged as conditional on the first-moment lower bound of `T:first`; the proof does not claim the normalization unconditionally.
- Argument preservation: PRESERVED (identical lines, OLD=NEW LF 659–684).
- New explanations: N/A (no text added).
- Evidence: $\|X_n\|_1\le\|X_n\|_2$; $t^{-\kappa}\log\E u^2\ge 2 t^{-\kappa}\log\E u$; $\liminf$ monotonicity. OLD/NEW statement LF 659–670, proof LF 672–684.
- Lost steps/qualifiers, pre-existing concerns: none. The dependence on `L:vertex-crude` (a later, assigned lemma) is non-circular because `L:vertex-crude`'s proof invokes only `L:pairing-product-envelope`, `L:damped-homogeneous-norms`, `L:joint-fixed-order`, and Wick's formula, none of which uses this proposition.

---

## P:mixed
- Global main ordinal: 2
- Old reading: COMPLETE (LF 851–904)
- New reading: COMPLETE (LF 851–927)
- Public reconstruction: COMPLETE
- Original-step coverage (OLD→NEW mapping: OLD single block becomes NEW Steps 1–3 with an added roadmap):
  1. *Fixed-order limits without the infinite series.* `L:joint-fixed-order` constructs each $X_n$ (and each two-chain diagram) at arbitrary vertexwise widths including unequal/empty chains. At positive noise widths Wick's formula gives $0$ at odd total order and the finite pairing sum at even order; Green smoothing is removed first. At fixed $m,n$, joint $L^2$ convergence gives $L^1$ product convergence:
     \[
       \|Y_mY_n-X_mX_n\|_1\le\|Y_m-X_m\|_2\|Y_n\|_2+\|X_m\|_2\|Y_n-X_n\|_2\to0,
     \]
     so $\E[X_mX_n]=\lim\E[Y_mY_n]$ equals the finite sum of the diagram limits (each a finite nonnegative limit by `L:joint-fixed-order`).
  2. *Chain reversal (terminal → root-forward).* With $s'_j=t-s_{m+1-j}$, $y'_j=x-y_{m+1-j}$ for the first chain and the analogous length-$n$ map on the second, each terminal chain maps to a root-forward chain with root $(0,0)$. I verify the increment preservation explicitly: for $1\le l<m$, $s'_{m-l+1}-s'_{m-l}=(t-s_l)-(t-s_{l+1})=s_{l+1}-s_l$, and the terminal factor $G(t-s_m,x-y_m)$ becomes $G(s'_1,y'_1)$. Covariance arguments flip sign under both transformations, absorbed by evenness of $|s_j-s_h|$ and $\gamma$. The vertex involution $\rho(j)=m+1-j$ ($j\le m$), $\rho(m+j)=m+n+1-j$ ($j\le n$) induces the pairing bijection on $D\in\Pi_k$. Passing to diagram limits gives `\eqref{E:mixed-moment}` with exactly the diagram `\eqref{E:mixed-diagram}` (self-pairings within a chain and cross-pairings both included in $\Pi_k$).
  3. *Summation.* `L:crude-corrected` and `L:vertex-crude` (both assigned) give fixed-$t$ norm summability; `P:mild-construction` (unassigned declaration, used at its stated hypothesis) identifies $\sum X_n$ as the canonical Stratonovich mild solution. None of these uses the mixed identity, so there is no circularity. Then $U_N=\sum_{n\le N}X_n\to u$ in $L^2$ and
     \[
       |\E U_N^2-\E u^2|\le\|U_N-u\|_2(\|U_N\|_2+\|u\|_2)\to0.
     \]
     Each $\E U_N^2$ expands over $0\le m,n\le N$ (the NEW-added clarification), and each mixed expectation is nonnegative, so the expansions increase; monotone convergence gives the full double sum, and regrouping by total order $2k$ gives `\eqref{E:full-second}` — a convergent series of nonnegative terms. (The proof correctly does not assert orthogonality of different ordered Stratonovich terms; it computes the genuinely off-diagonal mixed terms.)
- Argument preservation: PRESERVED. The only NEW sentences are the roadmap, the Step headings, the identification `Y_m=Y_m^{\boldsymbol a},Y_n=Y_n^{\boldsymbol a}` in Step 1, and "Each finite square expands over the square of indices $0\le m,n\le N$" in Step 3 — all accurate.
- New explanations: JUSTIFIED.
- Evidence: $L^1$-product convergence display; increment identity $s'_{m-l+1}-s'_{m-l}=s_{l+1}-s_l$; involution formulas; $|\E U_N^2-\E u^2|$ bound. OLD LF 851–904; NEW LF 851–927.
- Lost steps/qualifiers: none. Pre-existing note: the two-chain diagram uses each chain's own root, matching `\eqref{E:Sn2}` of the canonical-expansion context; the no-go references (`P:nogo-05`, `P:nogo-07`) prevent chronological concatenation, which this proof respects.

---

## L:white-test
- Global main ordinal: 3
- Old reading: COMPLETE (LF 928–941)
- New reading: COMPLETE (LF 951–964)
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. *Wave Green and overlap.* $d=\alpha=1$, $G(s,y)=\frac12\mathbf 1_{\{|y|<s\}}$, so
     \[
       \int_\R G(s,y)G(r,y)\,dy=\frac14\cdot2\cdot\min(s,r)=\frac{\min(s,r)}{2}.
     \]
  2. *The $(1,1)$ term.* Root-forward two-chain, one vertex each:
     \[
       \E X_1^2=\int_0^t\!\!\int_0^t \frac{\min(s,r)}{2}|s-r|^{-\alpha_0}\,ds\,dr.
     \]
     By symmetry under $s\leftrightarrow r$ this equals $\int_0^t ds\int_0^s r(s-r)^{-\alpha_0}dr$. Inner: with $r=su$,
     \[
       \int_0^s r(s-r)^{-\alpha_0}dr=s^{2-\alpha_0}\!\int_0^1 u(1-u)^{-\alpha_0}du
       =s^{2-\alpha_0}B(2,1-\alpha_0)
       =\frac{s^{2-\alpha_0}}{(1-\alpha_0)(2-\alpha_0)}.
     \]
     Hence the total equals $\frac{t^{3-\alpha_0}}{(1-\alpha_0)(2-\alpha_0)(3-\alpha_0)}=c_0t^{3-\alpha_0}$, matching the displayed constant.
  3. *The $(0,2)$ term.* Chain 2 has vertices at $0<r<s<t$; the delta covariance pins the two cumulative spatial positions. In root-forward increments this means $y_1=y_2$, giving
     \[
       J_{0,2}=\int_{0<r<s<t}|s-r|^{-\alpha_0}\,G_{s-r}(0)\Big(\int G_r\,dy_1\Big)dr\,ds,
     \]
     with $G_{s-r}(0)=\tfrac12$ and $\int G_r\,dy_1=r$, hence exactly half the previous display, $\tfrac12c_0t^{3-\alpha_0}$. (I checked this against the terminal form $\int_{0<s_1<s_2<t}(t-s_2)(s_2-s_1)^{-\alpha_0}ds_1ds_2\cdot\frac12$, which reproduces the same constant, confirming the terminal/root-forward conventions match.)
  4. *Symmetry and total.* The $(2,0)$ term is identical, so the total-order-two contribution to `\eqref{E:full-second}` is $c_0+\frac12c_0+\frac12c_0=2c_0t^{3-\alpha_0}$.
- Argument preservation: PRESERVED (proof text byte-identical; only line numbers shifted).
- New explanations: N/A.
- Evidence: overlap $\min/2$; Beta integral $B(2,1-\alpha_0)=[(1-\alpha_0)(2-\alpha_0)]^{-1}$; $G_{s-r}(0)=\tfrac12$, mass $r$. OLD LF 928–941, NEW LF 951–964.
- Lost steps: none. Pre-existing note: the small-order calibration contradicts the imported uniform bound (5.4) of `R:source-uniformity`, which is the stated motivation for `L:crude-corrected`; this remark is outside the assigned proof and is not counted.

---

## L:damped-homogeneous-norms
- Global main ordinal: 4
- Old reading: COMPLETE (LF 1034–1103)
- New reading: COMPLETE (LF 1057–1154)
- Public reconstruction: COMPLETE
- Original-step coverage (NEW adds roadmap and Steps 1–5):
  1. *Radial spectral mass and $N_1$.* Homogeneity of $\Gamma$ plus Fourier uniqueness gives $\mu(cA)=c^\alpha\mu(A)$; Radon finiteness and $\alpha>0$ give $\mu(\{0\})=0$ and $\mu(B_r)=r^\alpha V$ with $V=\mu(B_1)<\infty$. Then for $a>0$,
     \[
       \int\frac{\mu(d\xi)}{a^2+|\xi|^2}=\alpha V a^{\alpha-2}\int_0^\infty\frac{u^{\alpha-1}}{1+u^2}\,du<\infty
     \]
     (integrable at $0$ since $\alpha>0$, at $\infty$ since $\alpha<2$). Substituting into $N_1$ reduces finiteness to $\int_0^\infty\lambda^{\alpha_0-1}(\theta+\lambda)^{\alpha-2}d\lambda<\infty$: near $0$ need $\alpha_0>0$, near $\infty$ need $\alpha+\alpha_0-2<-1$, i.e. $\alpha+\alpha_0<2$ — exactly the hypothesis threshold `\eqref{E:threshold}`.
  2. *Absolute integrability and positivity of $N_2$.* With $|\widehat G_s(\xi)|\le\min(s,|\xi|^{-1})$: on $|\xi|\le1$ the bound is $V\iint e^{-\theta(s+t)}|s-t|^{-\alpha_0}st\,ds\,dt<\infty$; on $|\xi|>1$, $\int_{|\xi|>1}|\xi|^{-2}\mu(d\xi)=\alpha V\int_1^\infty r^{\alpha-3}dr=\alpha V/(2-\alpha)$ with the $st$-free time integral finite (split $s\le t$, $t\le s$, variables $u=\min$, $v=|s-t|$; the only singular factor is $v^{-\alpha_0}$, $\alpha_0<1$). Nonnegativity: for fixed $\xi$ the time form is a positive Laplace mixture of $e^{-\lambda|s-t|}$ (product of rank-one $e^{-\theta s}e^{-\theta t}$ with $e^{-\lambda|s-t|}$, both positive definite), so $N_2(\theta)^2\ge0$.
  3. *Homogeneous powers.* $N_0(\theta)=\int_0^\infty e^{-\theta s}s\,ds=\theta^{-2}$. For $N_1$: $\lambda=\theta u$, $\xi=\theta\eta$ give $\theta^{\alpha_0}\cdot\theta^{\alpha}\cdot\theta^{-2}=\theta^{\alpha+\alpha_0-2}$. For $N_2^2$: $s=u/\theta,t=v/\theta,\xi=\theta\eta$, $\widehat G_{u/\theta}(\theta\eta)=\theta^{-1}\widehat G_u(\eta)$: two time Jacobians and two wave factors give $\theta^{-4}$, temporal kernel and spatial measure give $\theta^{\alpha_0+\alpha}$, total $\theta^{\alpha+\alpha_0-4}=\theta^{-\beta}$, $\beta=4-\alpha-\alpha_0$ (the NEW power-counting sentence states precisely this).
  4. *Tails.* $N_1^{(M)}(1)$ is a tail of a finite nonnegative integral. For the second, $0\le K_M(r)\le|r|^{-\alpha_0}$ and $K_M(r)\to0$ for $r\ne0$; the absolute majorant of Step 2 gives dominated convergence in $(s,t,\xi)$, so $N_2^{(M)}(1)^2\to0$; the tail kernel is a positive Laplace mixture, so its quadratic form is nonnegative.
  5. *Multiplier comparisons.* With
     \[
       B_\theta(\lambda,\xi)=\iint e^{-\theta(s+t)}e^{-\lambda|s-t|}\widehat G_s(\xi)\overline{\widehat G_t(\xi)}\,ds\,dt\ge0,
     \]
     Fubini (justified by the absolute bound, $0\le m\le1$, $0\le K_S\le|\cdot|^{-\alpha_0}$) gives
     \[
       N_{2,m,S}(\theta)^2=\frac1{\Gamma_E(\alpha_0)}\int_S\lambda^{\alpha_0-1}\int m(\xi)B_\theta(\lambda,\xi)\mu(d\xi)d\lambda,
     \]
     whence the second comparison; the first is direct from the nonnegative $N_1$ integrand. Gaussian spatial/Green smoothing contribute $[0,1]$-valued $\xi$-multipliers, and Green smoothing preserves $G_s(\R^d)=s$.
- Argument preservation: PRESERVED (additions are roadmap, headings, and the Step-3 exponent tally).
- New explanations: JUSTIFIED.
- Evidence: $\int(a^2+|\xi|^2)^{-1}\mu=\alpha V a^{\alpha-2}B$-style integral; $\int_{|\xi|>1}|\xi|^{-2}\mu=\alpha V/(2-\alpha)$; exponent bookkeeping $\theta^{\alpha+\alpha_0-4}$; $0\le K_M\le|\cdot|^{-\alpha_0}$. OLD LF 1034–1103; NEW LF 1057–1154.
- Lost steps: none. Note the comparison is asserted after time integration, not pointwise on the oscillating $\widehat G_s\overline{\widehat G_t}$ product — correctly stated in both revisions.

---

## L:translated-covariance-CS
- Global main ordinal: 5
- Old reading: COMPLETE (LF 1148–1225)
- New reading: COMPLETE (LF 1199–1297)
- Public reconstruction: COMPLETE
- Original-step coverage (NEW adds roadmap and Steps 1–4):
  1. *Hilbert feature.* For $\lambda>0$, $h_\lambda(t,r)=\sqrt{2\lambda}e^{-\lambda(t-r)}\mathbf 1_{\{r\le t\}}$ satisfies
     \[
       \int_\R h_\lambda(t,r)h_\lambda(s,r)dr=2\lambda e^{-\lambda(t+s)}\int_{-\infty}^{\min(t,s)}e^{2\lambda r}dr=e^{-\lambda|t-s|},
     \]
     and $\int h_\lambda(t,r)^2dr=1$. On $\mathcal H_L=L^2((0,L]\times\R^d\times\R,\nu\mu\,dr)$ define $\Phi_L(t,x)=h_\lambda(t,r)e^{i\xi\cdot x}$. Then $\|\Phi_L(t,x)\|^2=\nu((0,L])\mu(\R^d)=:m_L$ and $\langle\Phi_L(t,x),\Phi_L(s,y)\rangle=\kappa_L(t-s)\gamma(x-y)=C_L((t,x),(s,y))$ (the $r$-integrals are absolutely convergent by Cauchy–Schwarz since $\int|h_\lambda(t,r)h_\lambda(s,r)|dr\le1$, and the cap measures are finite).
  2. *Bochner pairing.* Continuity of $C_L$ by dominated convergence makes $\Phi_L$ norm-continuous, strongly measurable with separable range, and bounded. The Bochner integral $F_L(f)=\int f\Phi_L$ exists for $f\in L^1$; Bochner Fubini (bound $m_L\|f\|_1\|h\|_1$) gives $Q_L(f,h)=\langle F_L(f),F_L(h)\rangle$, hence $|Q_L(f,h)|\le Q_L(f,f)^{1/2}Q_L(h,h)^{1/2}$. The feature space is deterministic (no new Gaussian field).
  3. *Translation invariance.* The change of both integration variables in `\eqref{E:translated-covariance-form}` (full time line, Lebesgue translation invariance) gives $Q_L(T_{A,a}f,T_{A,a}h)=Q_L(f,h)$. Applying Cauchy–Schwarz to the *two different* translates and the identity to each *self* pairing yields the capped form: $0\le Q_L(T_{A,a}G_1^0,T_{B,b}G_2^0)\le Q_L(G_1^0,G_1^0)^{1/2}Q_L(G_2^0,G_2^0)^{1/2}$ (nonnegativity uses $C_L\ge0$).
  4. *Passage.* The truncations $G_{i,M}=\min(G_i,M)\mathbf 1_{\{0<t\le M,|x|\le M\}}$ increase to $G_i$; monotone convergence passes the inequality and identity as $M\to\infty$ (equivalently via $L^1$ convergence and the absolute bound). Then positivity of $\nu$, nonnegativity of $\gamma$ give $Q_L(G_i^0,G_i^0)\uparrow N_C(G_i)^2$ and the cross pairing $\uparrow Q(\cdot,\cdot)$, bounded by $N_C(G_1)N_C(G_2)$. No division by norms, so zero norms/measures cause no exception; no spatial mollifier is removed.
- Argument preservation: PRESERVED (additions are roadmap and step headings only).
- New explanations: JUSTIFIED.
- Evidence: $e^{-\lambda|t-s|}$ feature computation; $\|\Phi_L\|^2=m_L$; $Q_L=\langle F_L(f),F_L(h)\rangle$; $Q_L(T_{A,a},T_{A,a})=Q_L$. OLD LF 1148–1225; NEW LF 1199–1297.
- Lost steps: none. The coefficient one is correctly independent of origins, dimension, cap, and covariance masses.

---

## L:pairing-product-envelope
- Global main ordinal: 6
- Old reading: COMPLETE (LF 1430–1539)
- New reading: COMPLETE (LF 1502–1639)
- Public reconstruction: COMPLETE
- Original-step coverage (NEW adds roadmap and Steps 1–5; NEW adds the $r,q$-notation clarification in Step 3):
  1. *Finite cap and convolution bounds.* Cap temporal domains at $L<\infty$ (finite since $a>0$). The stationary covariance pairing of `L:translated-covariance-CS` supplies the second norm $N_{2,e}$ and its coefficient-one Cauchy–Schwarz plus translation invariance in any finite dimension (only input: finite measure $\mu_e$). For one-sided spacetime convolution $F=G*H$: $N_0(F)=N_0(G)N_0(H)$; $N_{1,e}(F)\le N_0(G)N_{1,e}(H)$ since $|\mathcal L G|\le N_0(G)$ for $\lambda\ge0$; $N_{2,e}(F)\le N_0(G)N_{2,e}(H)$ by expressing $G*H$ as a Bochner integral of translates of $H$ and using Minkowski. Hence fused kernels satisfy all edge hypotheses.
  2. *Regional half-bound (induction).* Induction on $n$ ($n=0$: both sides 1; $n=1$: same-chain gives $N_0(G_{\rm first})N_{1,e}(G_{\rm last})$, cross-chain gives two second norms via covariance Cauchy–Schwarz). For an endpoint $v$ with predecessor $p$ and partner $a$ satisfying $s_a\le s_p$, since $\kappa_{e_0}$ is decreasing and $s_v-s_a\ge s_v-s_p\ge0$, replace $\kappa_{e_0}(s_v-s_a)$ by $\kappa_{e_0}(s_v-s_p)$ (an upper bound). The spatial integral collapses to $N_{1,e_0}(G_v)$: writing $c=x_p-x_a$, the factor $\kappa_{e_0}(u)\gamma_{e_0}(w+c)$ has Fourier $\iint e^{-\lambda u+i\xi(w+c)}\nu\mu$, and integrating against $G_v(u,w)$ gives $\int\mathcal L G_v(\lambda,\xi)e^{i\xi c}\nu\mu$, whose modulus is $\le N_{1,e_0}(G_v)$. Dropping the region indicator (positivity), removing $v$ and edge $e_0$: if $a$ is terminal, integrate it to $N_0(G_a)$ and apply induction (so $a\in Q_0$, $v\in Q_1$ with $e_0$, giving half the product, since $N_{1,e_0}$ lacks the displayed factor 2); otherwise let $b$ be $a$'s successor, integrate $a$ to get $F=G_a*G_b$ at $b$, apply induction to $D\setminus\{e_0\}$, and use the slot table ($i=0,1,2$) — for $i=0$ mass multiplicativity gives $\tfrac12 N_0(G_a)N_0(G_b)$; for $i=1$ the displayed chain
     \[
       N_{1,e_0}(G_v)[2N_{1,e_1}(F)]B_{\rm rest}\le\tfrac12 N_0(G_a)[2N_{1,e_1}(G_b)][2N_{1,e_0}(G_v)]B_{\rm rest};
     \]
     for $i=2$ the second-norm convolution bound puts the other second norm on $G_b$ with a mass on $G_a$ and $2N_{1,e_0}(G_v)$ on $v$. The counts $|Q_0|=|Q_1|$, $|Q_2|$ even, $|Q_0|+|Q_2|/2=n$ are verified in all three cases; only the full induction hypothesis at $n-1$ is used.
  3. *Same-chain and mutual endpoints.* If an endpoint is self-paired, its partner lies at/before its predecessor, so the half-bound applies on the whole domain (also covers empty chains). If the two endpoints are paired to each other, condition on predecessors $(A,z),(B,w)$; `L:translated-covariance-CS` applies with these origins, giving $N_{2,e}(G_u)N_{2,e}(G_v)$ (translating each self-pairing separately), and induction on the rest; add $u,v$ to $Q_2$. The NEW clarification ("Here $r=s_u-A$ and $q=s_v-B$ are relative times... The symbol $q$ is reused as a vertex label only in the next step") resolves the OLD overloaded $q$.
  4. *Two distinct cross pairs.* With partners $a$ (of $v$), $b$ (of $u$), $p=u-1$, $q=v-1$ (note the OLD/NEW reuse of $q$ here is harmless and now flagged): on $\{s_a\le s_q\}$ remove $v$ by the half-bound (indicator independent of $s_v,x_v$); on the complement $s_p\ge s_a>s_q\ge s_b$, so remove $u$ (indicator independent of $s_u,x_u$). In both cases the removed partner has a successor on its own chain. The two bounds are $P/2$ and $P'/2$, so the sum is $\le(P+P')/2\le\max(P,P')$.
  5. *Cap removal.* $L\to\infty$: monotone convergence for integrands and norm factors, finite admissible-product set, so the maximum converges to the maximum of limits.
- Argument preservation: PRESERVED (additions are roadmap, headings, and the single clarifying sentence in Step 3).
- New explanations: JUSTIFIED (the $q$-overload clarification is accurate and improves readability).
- Evidence: convolution norm estimates; $\kappa_{e_0}$ monotonicity $s_v-s_a\ge s_v-s_p$; modulus-of-phase collapse to $N_{1,e_0}$; slot table counts; $(P+P')/2\le\max(P,P')$. OLD LF 1430–1539; NEW LF 1502–1639.
- Lost steps: none. The endpoint-elimination figure reference is outside the proof text and unchanged; no matching/incidence requirement between $l$ and $\iota(l)$ is needed, correctly stated.

---

## L:spatial-wick-measures
- Global main ordinal: 7
- Old reading: COMPLETE (LF 1596–1724)
- New reading: COMPLETE (LF 1696–1848)
- Public reconstruction: COMPLETE
- Original-step coverage (NEW adds roadmap and Steps 1–5):
  1. *Laplace transform.* Writing $x_j-x_h=\sum_l\eta_l(\xi)z_l$ with $\eta_l$ the coefficient of $z_l$ in $\sum_{e}\xi_e(x_j-x_h)$, the wave Laplace transform $\int_0^\infty e^{-ar}\widehat G_r(\xi)dr=(a^2+|\xi|^2)^{-1}$ ($a=1+\lambda_l$) and the smoothed covariance spectrum give
     \[
       L_{\varepsilon,D}(\lambda)=\int e^{-\frac12\sum_e(\epsilon_j+\epsilon_h)|\xi_e|^2}\prod_l\frac{1}{(1+\lambda_l)^2+|\eta_l(\xi)|^2}\prod_e\mu(d\xi_e).
     \]
     Nonnegativity implies the transforms increase as any spatial width decreases (transform monotonicity, not pointwise covariance monotonicity).
  2. *Occupation moments.* With $A=\alpha V\int_0^\infty u^{\alpha-1}e^{-u^2/2}du$, the pointwise bound $(p_t*\gamma_b)(x)\le At^{-\alpha/2}$ follows from the multiplier $e^{-(t+b)|\xi|^2/2}$ and radial homogeneity. The claimed Brownian bound
     \[
       \E_B S_b(T)^j\le\frac{(2j)![A\Gamma_E(1-\alpha/2)]^j}{\Gamma_E((2-\alpha/2)j+1)}T^{(2-\alpha/2)j}
     \]
     is verified as follows at the simplex level: the $j$ selected pair gaps, each dominated below by a distinct adjacent gap at its right endpoint, give $\prod_j(\text{gap})^{-\alpha/2}$; the Dirichlet integral $\int_{\sum u_i\le T}\prod_{i=1}^{j}u_{2i}^{-\alpha/2}du=\Gamma_E(1-\alpha/2)^jT^{(2-\alpha/2)j}/\Gamma_E((2-\alpha/2)j+1)$ matches the displayed constant, and there are $(2j)!$ orders. (The conditional-removal "condition on all but the last remaining vertex" step that produces this adjacent-gap domination is the one genuinely compressed spot — see Findings.)
  3. *Uniform mass bound.* Bounding $L_{\varepsilon,D}(0)$ by the common width $\epsilon_*$ and applying the wave-to-heat identity $\int_0^\infty e^{-at}G_t(dx)dt=\tfrac12\int_0^\infty e^{-a^2u/2}p_u(x)du\,dx$ (equal Fourier transforms $(a^2+|\xi|^2)^{-1}$) turns the transform into $2^{-2k}$ times a two-Brownian-chain integral; inserting $1=\frac14\iint e^{-((a-\tau_1)+(b-\tau_2))/2}dadb$ over $[0,\infty)^2$ with $\tau_i$ the last chain time, extending the ordered domains to full cubes by positivity, factoring into occupation integrals, and using spectral Cauchy–Schwarz $A_{12}\le\sqrt{S_1S_2}$ gives the pairing product bound $S_1^{v_1+w/2}S_2^{v_2+w/2}\le(1+S_1)^k(1+S_2)^k$; Step 2 bounds each expected factor by a finite $M_k$ independent of $\epsilon_*$, yielding $\sup_\varepsilon L_{\varepsilon,D}(0)<\infty$.
  4. *Finite-measure limit.* Monotone convergence gives finite limits $L_D(\lambda)$, continuity at $0$ by dominated convergence. Pushing forward via $y_l=e^{-r_l}$ onto $[0,1]^{2k}$, bounded masses give weak cluster limits whose monomial moments are the $L_D$ values; polynomial (Stone–Weierstrass) density gives uniqueness; as $c\downarrow0$, $\int\prod y_l^c d(\text{limit})=L_D(c,\dots,c)\to L_D(0)$ shows no mass on the $y_l=0$ faces (no escape to $r_l=\infty$), portmanteau bounds the approximating tails, and pulling back proves weak convergence on $[0,\infty)^{2k}$ independent of relative rates.
  5. *Boundary mass and scaling.* $\lambda_l\to\infty$ in the limiting integrand gives zero by domination, i.e. $\nu_D\{r_l=0\}=0$. Scaling: $G_{cr}(c\,dz)=cG_r(dz)$, $\gamma_b(cx)=c^{-\alpha}\gamma_{b/c^2}(x)$, $2k$ time Jacobians give $\rho_{\varepsilon,D}(cA)=c^{(4-\alpha)k}\rho_{\varepsilon/c^2,D}(A)$, passing to the limit gives the stated homogeneity of $\rho_D$. If a compact $A\subset\{\ell_i=T\}$, $T>0$, had positive mass, the dilates $cA$, $c\in[1,2]$, would be disjoint with common positive lower mass inside a compact set, contradicting local finiteness; compact exhaustion proves the face is null. The finite-horizon region's boundary lies in the horizon and coordinate-zero faces, so the bounded continuous cutoff plus multiplier $e^{\sum r_l}\varphi$ gives `\eqref{E:spatial-wick-limit}`.
- Argument preservation: PRESERVED (additions are roadmap and headings only).
- New explanations: JUSTIFIED.
- Evidence: resolvent Laplace transform; Dirichlet integral matching the $(2j)!$-constant; wave-to-heat Fourier identity; $A_{12}\le\sqrt{S_1S_2}$; homogeneity exponent $2k+2k-\alpha k=(4-\alpha)k$. OLD LF 1596–1724; NEW LF 1696–1848.
- Lost steps: none removed. Pre-existing compression noted above in Step 2.

---

## L:joint-fixed-order
- Global main ordinal: 8
- Old reading: COMPLETE (LF 1740–1818)
- New reading: COMPLETE (LF 1864–1966)
- Public reconstruction: COMPLETE
- Original-step coverage (NEW adds roadmap and Steps 1–4; NEW adds the $\gamma^0_\delta$ identification in Step 1):
  1. *Spatial limit at fixed temporal cutoff.* On $\ell_1<T_1,\ell_2<T_2$, define $F_{\varepsilon,\delta,D}=\int\prod_e\gamma^0_{\delta_j\vee\delta_h}(s_j-s_h)d\rho_{\varepsilon,D}$. Here $\gamma^0_\delta=\kappa_\delta$ is the capped kernel of `\eqref{E:pairing-source-covariance}`, and off the diagonal $|r|^{-\alpha_0}-\gamma^0_\eta(r)=K_{1/\eta}(r)$ is the omitted Laplace tail (the NEW-added sentence). At common width $\eta$, the multiplier is bounded continuous, so the spatial limit exists at every $T_1,T_2$ by `\eqref{E:spatial-wick-limit}`.
  2. *Uniform temporal remainder.* $F_{\varepsilon,0,D}$ (full factors $|s_j-s_h|^{-\alpha_0}$) is finite at positive spatial widths (finite covariance suprema, Green horizon masses, and $\alpha_0<1$ makes each $|s-r|^{-\alpha_0}$ integrable). The difference-of-products bound gives
     \[
       F_{\varepsilon,0,D}-F_{\varepsilon,\eta,D}\le\sum_{k\text{ terms}}\Big(K_{1/\eta}(e_j)\prod_{i\ne j}|s_i-s_h|^{-\alpha_0}\Big).
     \]
     Applying `L:pairing-product-envelope` to $e^{-s}G_s$ (Green smoothing in $d=3$, capped Laplace domains; each edge a finite Gaussian-weighted $\mu$ with nonnegative covariance) and `L:damped-homogeneous-norms` for all unmarked norms, with the marked edge appearing once in a first-norm slot or twice in a second-norm slot, yields `\eqref{E:joint-temporal-tail}`:
     \[
       0\le F_{\varepsilon,0,D}-F_{\varepsilon,\eta,D}\le C_{k,T_1,T_2}\big(N_1^{(1/\eta)}(1)+N_2^{(1/\eta)}(1)^2\big),
     \]
     uniformly in spatial widths, with the right side $\to0$ as $\eta\downarrow0$ by `\eqref{E:damped-tail-norms}`.
  3. *Squeeze.* The common-$\eta$ spatial limits $b_D(\eta)$ increase as $\eta$ decreases and are Cauchy with finite limit $b_D$. If all $\delta_j<\eta$, positivity gives $F_{\varepsilon,\eta,D}\le F_{\varepsilon,\delta,D}\le F_{\varepsilon,0,D}$; fixing $\eta$, passing to the spatial limit in the lower term, using the uniform remainder, and letting $\eta\downarrow0$ proves the joint limit $b_D$ at arbitrary spatial/temporal rates (empty chains included).
  4. *$L^2$ completion.* Wick's formula gives the mixed second moments of two copies of $Y_n$ as the finite diagram sum after reversing both terminal chains at horizon $t$ (evenness absorbs signs). Every mixed moment, including both diagonal moments, tends to the same $Q_n=\sum_D b_D$, so
     \[
       \|Y_n^{\boldsymbol a}-Y_n^{\boldsymbol b}\|_2^2\to Q_n+Q_n-2Q_n=0,
     \]
     and completeness gives the unique limit $X_n$ independent of width ratios, with Green smoothing removed before noise smoothing (Green-width limit was taken in the terminal construction), and common noise widths reproduce the multiple Stratonovich integral of $g_n$.
- Argument preservation: PRESERVED (additions are roadmap, headings, and the $\gamma^0_\delta$-vs-$\kappa_\delta$ identification, which is correct).
- New explanations: JUSTIFIED.
- Evidence: tail identification $|r|^{-\alpha_0}-\gamma^0_\eta(r)=K_{1/\eta}(r)$; difference-of-products inequality; `\eqref{E:joint-temporal-tail}` with `\eqref{E:damped-tail-norms}`; $\|Y^{\boldsymbol a}-Y^{\boldsymbol b}\|^2\to Q+Q-2Q=0$. OLD LF 1740–1818; NEW LF 1864–1966.
- Lost steps: none. Disjoint-pair temporal tails are exactly the marked $K_{1/\eta}$ factors; arbitrary relative width rates and the joint limit are correctly handled.

---

## L:crude-corrected
- Global main ordinal: 9
- Old reading: COMPLETE (LF 1839–1888)
- New reading: COMPLETE (LF 1987–2054)
- Public reconstruction: COMPLETE
- Original-step coverage (NEW adds roadmap and Steps 1–2; NEW adds the (1.5)/(2.24) source attribution):
  1. *Damped pairing envelope.* Telescoping weights give $e^{-\theta(s_n+s_{2n})}\ge e^{-2\theta t}$ on the finite chains, so the original diagram is $\le e^{2\theta t}$ times the damped infinite-simplex diagram. Applying `L:pairing-product-envelope` with $q_0=q_1$, $q_0+q_2/2=n$ and `\eqref{E:crude-norms}` ($N_0=\theta^{-2}$, $N_1\le C_0$, $N_2\le C_0\theta^{-1}$) bounds each pairing by $e^{2\theta t}C^n\theta^{-2n}$ (the $\theta$-power is $2q_0+q_2=2n$), summing the $P_n$ pairings to `\eqref{E:theta-envelope}`:
     \[
       \E X_n(t,x)^2\le P_ne^{2\theta t}C^n\theta^{-2n},\quad\theta\ge\theta_0.
     \]
     Regularization handling: `L:pairing-product-envelope` needs finite edge measures $\mu_e$; the Gaussian-weighted measure $e^{-b|\xi|^2/2}\mu$ is finite since the multiplier is bounded by $C(1+|\xi|^2)^{-(2-\alpha_0)/2}$ whose integral converges because $\alpha+\alpha_0<2$ (the NEW attribution to source (1.5) and `R:source-case2-time-shift`(iii) is accurate). The zero norm is unchanged, first/second norms are bounded by `L:damped-homogeneous-norms`, uniform in regularizations; in $d=3$ use $G_\eta=p_\eta*G$ (multiplier $\le1$, mass equal). Take $\eta\downarrow0$ at fixed noise regularization (squared moments converge), then $(\epsilon,\delta)\to0$ via `L:joint-fixed-order`; in $d=1,2$ only the latter limit is needed.
  2. *Optimize and sum.* With $\theta=\theta_0+n/t$, $(2n)!\le(2n)^{2n}$ gives $P_nn^{-2n}\le2^n/n!$, absorbing $2^ne^{2n}$ into $C^n$ yields $\E X_n^2\le e^{2\theta_0t}C^nt^{2n}/n!$. Square roots are summable by the ratio test ($(\sqrt Ct)/\sqrt{n+1}\to0$), so the norm series converges independently of `P:mixed`. Minkowski and Cauchy–Schwarz:
     \[
       \Big(\sum_{n\ge0}\frac{z^n}{\sqrt{n!}}\Big)^2\le\Big(\sum_{n\ge0}2^{-n}\Big)\Big(\sum_{n\ge0}\frac{2^nz^{2n}}{n!}\Big)=2e^{2z^2},
     \]
     giving $\|u\|_2\le e^{\theta_0t}\sum(\sqrt Ct)^n/\sqrt{n!}$ and $\E u^2\le2e^{2\theta_0t+2Ct^2}$.
- Argument preservation: PRESERVED (additions are roadmap, headings, and the source-identification sentence).
- New explanations: JUSTIFIED.
- Evidence: $e^{-2\theta t}$ telescoping inequality; $\theta$-power $2q_0+q_2=2n$; $P_nn^{-2n}\le2^n/n!$; Cauchy–Schwarz series bound. OLD LF 1839–1888; NEW LF 1987–2054.
- Lost steps: none. The proof explicitly avoids the imported uniform bound (5.4); no pointwise delta-covariance bound is used.

---

## L:vertex-crude
- Global main ordinal: 10
- Old reading: COMPLETE (LF 1910–1962)
- New reading: COMPLETE (LF 2076–2145)
- Public reconstruction: COMPLETE
- Original-step coverage (NEW adds roadmap and Steps 1–2; NEW adds the (1.5) cross-reference):
  1. *Edgewise regularizations.* Wick's formula (2.19) with the joint covariance (2.11) gives $\E|Y_n^{\boldsymbol a}|^2$ with widths copied to the second chain and edge covariances $\gamma^0_{\delta_j\vee\delta_l}(s_j-s_l)\gamma_{\epsilon_j+\epsilon_l}(y_j-y_l)$. Reversing each terminal chain ($s'_j=t-s_{n+1-j}$, $y'_j=x-y_{n+1-j}$) only permutes vertex widths; covariance differences change sign under even kernels. For each pairing apply `L:pairing-product-envelope` to $e^{-\theta r}G_r$ (Green smoothing if $d=3$); the per-edge hypotheses hold with spectral measure $e^{-(\epsilon_j+\epsilon_l)|\xi|^2/2}\mu$ finite by (1.5) (the NEW cross-reference to `R:source-case2-time-shift`(iii) is accurate) and temporal Laplace domain $[0,(\delta_j\vee\delta_l)^{-1}]$. All edge norms obey `\eqref{E:crude-norms}` uniformly in widths: for the first norm the positive Laplace–Fourier transform is only decreased by the $[0,1]$-valued Gaussian multiplier and temporal truncation; for the second norm enlarging the temporal covariance to $|s-r|^{-\alpha_0}$ (positivity) and removing the spatial Gaussian multiplier (squared absolute transform against nonnegative measures) only increase it; Green smoothing has multiplier $\le1$ and unchanged mass. Constants are independent of all vertex widths, justified by `L:damped-homogeneous-norms`.
  2. *Count and optimize.* With $\#Q_0=\#Q_1$, $\#Q_0+\#Q_2/2=n$, and $D=\max(1,2C_0)$, the constant contribution is $D^{\#Q_1+\#Q_2}\le D^{2n}$, i.e. $C_1=D^2$, giving
     \[
       \|Y_n^{\boldsymbol a}(t,x)\|_2^2\le P_ne^{2\theta t}C_1^n\theta^{-2n},\quad\theta\ge\theta_0.
     \]
     Take the Green width to zero at fixed noise widths, set $\theta=\theta_0+n/t$, and use $P_nn^{-2n}\le2^n/n!$ to obtain `\eqref{E:vertex-crude}` (increasing $C$). `L:joint-fixed-order` transfers the bound to $X_n$; $q_0(t)=e^{\theta_0t}\ge1$. Finally the ratio test
     \[
       \frac{\sqrt{n+2}\,q_{n+1}(T)}{\sqrt{n+1}\,q_n(T)}=\sqrt C\,T\frac{\sqrt{n+2}}{n+1}\to0
     \]
     proves `\eqref{E:vertex-summability}` $\sum_n\sqrt{n+1}\,q_n(T)<\infty$.
- Argument preservation: PRESERVED (additions are roadmap, headings, and the (1.5) cross-reference).
- New explanations: JUSTIFIED.
- Evidence: edge covariance form; $D^{\#Q_1+\#Q_2}\le D^{2n}$; $\|Y_n^{\boldsymbol a}\|_2^2\le P_ne^{2\theta t}C_1^n\theta^{-2n}$; ratio $\to0$. OLD LF 1910–1962; NEW LF 2076–2145.
- Lost steps: none. This lemma supplies the input to `P:Jensen` (ordinal 1) and `P:mixed` (ordinal 2) exactly as they claim ($\sum_n\|X_n(t,x)\|_2<\infty$ follows from `\eqref{E:vertex-summability}`).

---

## Findings and limits

**Overall.** All ten assigned main-file proofs are preserved between OLD `cdde711c` and NEW `58108ca3`. The NEW text is a pure readability edit: each multi-step proof gains an accurate roadmap and `Step k` headings partitioning pre-existing sentences, plus (in P:mixed, L:damped-homogeneous-norms, L:pairing-product-envelope, L:joint-fixed-order, L:crude-corrected, L:vertex-crude) a handful of correct clarifying sentences. No mathematical object, hypothesis, displayed bound, constant, or subcase was altered. Every added heading and sentence was checked against the sentence(s) it labels and found accurate. The five jointly-used target results — Jensen's implication (1), the mixed-term/full-second-moment identity (2), the homogeneous damped norms and tails (4), the translated covariance Cauchy–Schwarz (5), the pairing-product envelope (6), the spatial Wick-measure and joint vertexwise limits (7,8), and the corrected crude/uniform vertex bounds (9,10) — were each rebuilt from the embedded statements and the assigned lemmas they invoke, without treating OLD as an oracle and without substituting any imported solution-series identification for a deduction (where the series is identified, `P:mild-construction` is used as a stated unassigned boundary at its stated hypothesis, which the contract permits).

**Convention checks.** The terminal→root-forward reversal (P:mixed Step 2, L:vertex-crude Step 1) is exact; I verified the increment identity $s'_{m-l+1}-s'_{m-l}=s_{l+1}-s_l$ and cross-checked the `(0,2)` white test against the direct terminal form, obtaining the same $c_0t^{3-\alpha_0}/2$. The two chains use independent roots $(0,0)$ throughout, matching `\eqref{E:Sn2}`. Odd/even Stratonovich orders, self/unequal/empty chains, and mixed off-diagonal terms are all retained; no orthogonality between different ordered Stratonovich terms is invoked. Finite positive measures are used at every point requiring a finite edge spectral measure (via Gaussian weighting in 9,10; via $\mu_e$ finiteness in 6,8), and singular/Radon covariance is handled through measures rather than densities. Dimensions 1–3 and Green-smoothing-before-noise-removal are respected in 7,8,9,10.

**Pre-existing, non-introduced concerns (notes).**
1. In L:spatial-wick-measures Step 2, the conditional-removal step producing the adjacent-gap domination for the Brownian occupation moment bound ("order the $2j$ times … condition on all but the last remaining vertex … remove this vertex and its partner … repeat") is compressed. The resulting simplex integral is correct and indeed reproduces the displayed constant $\Gamma_E(1-\alpha/2)^jT^{(2-\alpha/2)j}/\Gamma_E((2-\alpha/2)j+1)$; but the rigorous justification that each selected pair gap dominates the corresponding adjacent gap, and that the marginal law of the remaining vertices after conditioning is the Brownian law, is asserted in one sentence. This is a standard pinching argument and both revisions state it identically; I therefore mark it as a compressed (not defective) deduction, common to OLD and NEW.
2. P:Jensen's unconditional conclusion $\E u\ge1$ depends on $S_0=1$ and nonnegativity of each pairing term, which is sound, but the specialization $\ell=L_*$ is explicitly conditional on the unassigned declared `T:first` bound — the proofs correctly do not numerically specialize unconditionally, so no spurious constant is imported.
3. Proofs 2, 8, 9, 10 rely on the unassigned declaration `P:mild-construction` (series = Stratonovich mild solution) and on the source's Wick formula (2.19)–(2.21). These are used as stated boundaries at their stated hypotheses; their own proofs are unassigned and not counted. No circularity arises because none of the assigned lemmas feeding `P:mixed` and `P:Jensen` uses their conclusions.
4. The white-test lemma (3) is an order-two calibration that contradicts the imported uniform bound (5.4) of the source remark; this is the stated motivation for the corrected estimates and is correctly flagged as a remark, not silently repaired.

**Limits.** Only the ten assigned global main ordinals were reconstructed; the unassigned declarations (`H:homog`, `E:expansion`, `T:first`, `T:intro-second-moment`, `T:full-upper`, `P:mild-construction`, the intrinsic-constant module, occupation-ceiling, spatial-bracket, white-moment-bounds, navigation headings, and the no-gos) were read as boundary context and used only at their stated hypotheses, never as oracles for assigned deductions. No external files, tools, or network were used; everything was reconstructed from the embedded raw source. The verdict is therefore PASS_WITH_NOTES with high confidence: the NEW revision is readability-equivalent to the OLD, all ten proofs reconstruct in public with checkable equations, and the only caveats are the two pre-existing compressions/imported boundaries noted above, neither introduced by the NEW edit.
