# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

Scope note: I reviewed only the three assigned proof targets in
`notes/integrated_masked_moments.tex` (OLD revision
`cdde711c...`, NEW revision `4e750612...`). The supplied unassigned contexts
(`notes_stratonovich_ham_second_moment.tex`, `integrated_source_convergence.tex`,
and the small fixed-LF declaration snippets) were used only to check the
hypotheses and definitions appealed to by the target proofs; their own proofs
were not counted or re-reviewed. The reconstructed working below is public and
does not rely on treating OLD as an oracle.

## L:masked-chain-comparison

- Old reading: COMPLETE (OLD statement LF 23–37; proof LF 39–98)
- New reading: COMPLETE (NEW statement LF 23–37; proof LF 39–127)
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Chain measure construction.** Both versions define a positive
     time-space chain measure \(\nu_n^{t,x}\) on
     \(0<s_1<\cdots<s_n<t\) with successive spatial factors
     \(G_d(s_{j+1}-s_j,\mathrm dz_j)\), \(s_{n+1}=t\), the terminal point \(x\)
     recovered backwards, and \(\nu_0^{t,x}(1)=1\).
     The mass recursion \(f_n(t)=\int_0^t(t-r)f_{n-1}(r)\,\mathrm dr\)
     is unchanged. Public check: with \(f_{n-1}(r)=r^{2n-2}/(2n-2)!\),
     \[
     f_n(t)=\frac{1}{(2n-2)!}\int_0^t(t-r)r^{2n-2}\,\mathrm dr
     =\frac{t^{2n}}{(2n-2)!}B(2,2n-1)
     =\frac{t^{2n}}{(2n-2)!}\cdot\frac{(2n-2)!}{(2n)!}
     =\frac{t^{2n}}{(2n)!}.
     \]
     This is the asserted \eqref{E:masked-chain-mass} and proves finiteness at
     every fixed order. Measurability via \(G_d(r)=r(D_r)_\#\mu_1\) is
     unchanged.
  2. **Covariance and Gaussian integrability.** Both use
     \[
     C_\rho(s,z;r,w)=K_\eta(s-r)\Gamma_{2\varepsilon}(z-w),\qquad
     0\le C_\rho\le c_\rho=K_\eta(0)\Gamma_{2\varepsilon}(0)<\infty.
     \]
     Check of the bound: since \(C_\rho\) is a Gaussian covariance,
     \(|C_\rho(s,z;r,w)|\le\sqrt{C_\rho(s,z;s,z)C_\rho(r,w;r,w)}=c_\rho\),
     with \(K_\eta(0)=\Gamma_E(a)^{-1}\int_0^{\eta^{-1}}\lambda^{a-1}\mathrm
     d\lambda<\infty\). This matches the declared common-width covariance:
     setting \(\varepsilon'=\varepsilon\), \(\eta'=\eta\) in
     \eqref{E:source-joint-covariance} gives
     \(K_{\max(\eta,\eta)}=K_\eta\) and
     \(\Gamma_{\varepsilon+\varepsilon}=\Gamma_{2\varepsilon}\). Positivity
     of \(C_\rho\ge0\) uses nonnegativity of \(\Gamma\) and positivity of the
     heat/Laplace kernels; the Gaussian Cauchy–Schwarz route is also stated in
     both.
  3. **Bochner and stochastic Fubini.** Hölder and scalar Gaussian moments
     bound \(\mathbb E|\prod_{i=1}^{2n}Y_\rho(s_i,z_i)|\) uniformly over the
     vertex positions at fixed \(\rho,n\) by a constant depending only on
     \(c_\rho\). Hence \(\|\prod_{i=1}^nY_\rho(s_i,z_i)\|_2\) is uniformly
     bounded on the chain support, and its integral against the finite
     \(\nu_n^{t,x}\) is finite; doing the same for two products gives the
     absolute integrability needed for the two-chain expectation exchange.
     This supports the Bochner-\(L^2\) and stochastic-Fubini claims.
  4. **Green smoothing before noise removal.** Both versions carry the same
     Green-width identification: replace each \(G_d(r)\) by its convolution
     with a positive heat approximate identity; at fixed times the measures
     converge weakly with mass preserved; each Wick covariance product is
     bounded by a power of \(c_\rho\) and spatially continuous by
     Lemma~\ref{L:source-pointfield-regularity}; the chain-mass integrands
     from \eqref{E:masked-chain-mass} provide an integrable time majorant, so
     square/cross moments converge and the integrals converge in \(L^2\).
     Both explicitly say no samplewise heat-tail bound is needed and that
     Lemma~\ref{L:joint-fixed-order} gives the Green-before-noise limit.
  5. **Wick diagram comparison.** For \(n+k=2l\), each pair partition \(D\)
     contributes the nonnegative
     \(\int\prod_{\{i,j\}\in D}C_\rho(s_i,z_i;s_j,z_j)\mathrm
     d(\nu_n^{t,x}\otimes\nu_k^{t,y})\). The masked integrand carries the extra
     factor \(\prod_{i=1}^{2l}m(z_i)\in[0,1]\). Since \(C_\rho\ge0\) and every
     vertex appears exactly once, each masked diagram is between \(0\) and the
     unmasked diagram. Summing over all pair partitions, including
     self-pairings and unequal/empty chains, gives
     \eqref{E:masked-order-comparison}. For odd \(n+k\) Gaussian centering
     gives zero. For \(n=k=0\) both sides are \(1\).
  6. **Norm bound.** Taking \(k=n\), \(y=x\), the squared masked \(L^2\) norm
     is dominated by the squared unmasked one; \eqref{E:masked-order-bound}
     then follows from the unmasked \(q_n(t)\) bound of
     Lemma~\ref{L:vertex-crude} (and \(q_0(t)=e^{\theta_0t}\ge1\) from the
     supplied context, matching \(\|X_{\rho,0}\|_2=1\)).

- Argument preservation: PRESERVED. The NEW proof reorganizes OLD LF 39–98
  into three labelled Steps but keeps every old logical step listed above, and
  retains the key final qualifier that the comparison is about expected
  displacement diagrams, not samplewise solution order or covariance order.
- New explanations: JUSTIFIED.
  (i) The added note that \(z_i\) is the recovered vertex position, not the
  Green increment, is consistent with the mask/covariance factors and removes
  a potential notational ambiguity.
  (ii) The added induction computation of \eqref{E:masked-chain-mass} is
  correct (Beta-integral shown above).
  (iii) The added sentences spelling out the Bochner integrability condition
  and the absolute integrability for expectation exchange follow from the
  already-proved uniform Gaussian bound and finiteness of the chain measure.
  (iv) The added identification of \(X_{\rho,n}(t,x)\) with
  \(Y_n^{\boldsymbol a}(t,x)\) from Lemma~\ref{L:vertex-crude} at every
  vertexwise width equal to \(\rho\) is a definitional/common-width
  identification consistent with the module’s “canonical regularized terminal
  integrals at common noise widths”; it adds no new hypothesis.
- Evidence: equation checks above use \eqref{E:masked-chain-mass},
  \eqref{E:masked-order-comparison}, \eqref{E:masked-order-bound},
  \eqref{E:source-joint-covariance}, and the upstream definitions of
  \(K_\eta,\Gamma_\varepsilon\). OLD LF 39–98 and NEW LF 39–127 contain the
  same proof content; the only additions are the explanatory sentences
  identified above.
- Lost steps/qualifiers: none identified within this read. The explicit
  statements about positive sphere measures in \(d=3\), Green smoothing before
  noise removal, all pair partitions including self-pairings, equal/unequal/
  empty chains, mask factors in \([0,1]\), the order-zero case \(n=k=0\), and
  the absence of samplewise ordering are all preserved.
- Pre-existing concerns: the proof depends on unassigned
  Lemma~\ref{L:vertex-crude} and Lemma~\ref{L:joint-fixed-order}; that is
  upstream scope, not a rewrite defect. The case \(\Gamma=0\) is handled
  implicitly (then \(C_\rho\equiv0\), so all \(n+k\ge2\) diagrams vanish and
  \(n=k=0\) gives \(1\)); no separate branch is required. No new hypothesis is
  silently added.

## P:masked-source-moments

- Old reading: COMPLETE (OLD statement LF 100–115; proof LF 117–159)
- New reading: COMPLETE (NEW statement LF 129–144; proof LF 146–210)
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Absolute \(L^2\) convergence of the series.** With
     \(Q_T=\sum_{n\ge0}q_n(T)<\infty\) by \eqref{E:vertex-summability},
     Lemma~\ref{L:masked-chain-comparison} gives
     \(\sum_{n\ge0}\|X_{\rho,n}^{(m)}(t,x)\|_2\le Q_t\), so the series
     converge absolutely in \(L^2\), uniformly over \((t,x)\) in bounded
     sets and over widths. This is unchanged.
  2. **Pathwise Picard identification and uniqueness.** Both proofs fix
     \(\rho\), a compact observation set, and a horizon \(T\). On the source
     regularity event the coefficient \(mY_\rho\) is bounded by a
     sample-dependent \(M\) on the backward-cone enlargement. The
     \(n\)-th Picard term is bounded by \(M^nt^{2n}/(2n)!\) using finite
     propagation and the chain mass \eqref{E:masked-chain-mass}; this series
     converges uniformly. Continuity of each term follows from the unit-time
     Green representation with dominated integration. Summing the Volterra
     recursion gives the ordinary mild equation with data \((1,0)\).
     Uniqueness: if \(z\) is the difference of two continuous mild solutions,
     iterating \(z(t,x)=\int_0^t\int G_d(t-r,x-y)(mY_\rho)(r,y)z(r,y)\mathrm
     dy\,\mathrm dr\) bounds the observation-set value by
     \(B M^nT^{2n}/(2n)!\to0\), where \(B\) bounds the difference on a larger
     compact cone. This is the asserted local-cone existence/uniqueness.
  3. **Version identification.** Bochner Fubini plus the absolute product
     integrability from the preceding lemma identifies each Bochner term with
     the pathwise chain integral at a fixed terminal point, simultaneously over
     countably many orders. An a.s. convergent subsequence of the \(L^2\)
     partial sums identifies the limit with the continuous Picard version at
     that point; the continuous versions then define the solution for all
     terminal points at the fixed \(\rho\), without any common event over
     uncountably many widths. Both versions keep this same-source pointwise
     modification language.
  4. **Passing the comparison through the sums.** For masked or unmasked
     terms,
     \[
     \sum_{n,k\ge0}\mathbb E|X_{\rho,n}^{(m)}(t,x)X_{\rho,k}^{(m)}(t,y)|
     \le\sum_{n,k\ge0}q_n(t)q_k(t)=Q_t^2<\infty,
     \]
     so the product partial sums converge in \(L^1\). Passing
     \eqref{E:masked-order-comparison} termwise gives
     \eqref{E:masked-two-point}.
  5. **Stationarity only for the unmasked law.** The unmasked source law is
     spatially stationary; its finite Picard integrals commute with
     translations, and their \(L^2\) limits inherit stationarity. Thus
     \[
     \mathbb E[u_\rho(t,x)u_\rho(t,y)]
     =\mathbb E[u_\rho(t,0)u_\rho(t,y-x)]
     \le\mathbb E|u_\rho(t,0)|^2.
     \]
     The masked solution is explicitly not required to be stationary.
  6. **Bochner spatial average.** Each finite Bochner term is
     \(L^2\)-continuous in \(x\) by the source increment continuity on compact
     cones and dominated Gaussian product moments; the uniform \(q_n\)-tails
     propagate this to the full sum. The separable \(L^2\) image and the
     \(Q_t\)-bound give the Bochner integral in \(x\), and the absolute bound
     \(\|\phi\|_1^2Q_t^2\) justifies Fubini. Then
     \[
     \mathbb E\Bigl|\int\phi(x)u_\rho^m(t,x)\mathrm dx\Bigr|^2
     =\iint \phi(x)\phi(y)\mathbb E[u_\rho^m(t,x)u_\rho^m(t,y)]\mathrm dx
     \mathrm dy
     \le\|\phi\|_1^2\,\mathbb E|u_\rho(t,0)|^2,
     \]
     proving \eqref{E:masked-average-source} for \(\phi\ge0\).

- Argument preservation: PRESERVED. The NEW proof splits the same content
  into four Steps and retains all old assertions and qualifiers, including the
  unmasked-only stationarity statement and the fixed-\(\rho\) "no common event
  over uncountably many widths" qualifier.
- New explanations: JUSTIFIED.
  (i) The added sentence in Step 3 that Cauchy–Schwarz bounds the stationary
  two-point expectation by the geometric mean of two equal point second
  moments is correct: for real \(u\),
  \(\mathbb E[u_xu_y]\le(\mathbb Eu_x^2\,\mathbb Eu_y^2)^{1/2}\), and
  stationarity makes the two point moments equal to
  \(\mathbb E|u_\rho(t,0)|^2\).
  (ii) The added Step 4 sentence translating every recovered vertex position
  by \(x\) is consistent with the chain measure definition: the Green factors
  depend only on spatial *differences*, so moving the terminal point from
  \(0\) to \(x\) shifts each source argument \(z_i\) by \(x\), while the
  increment measure stays fixed; the mask \(m(z_i)=m(x+w_i)\) is exactly where
  the masked case changes. This is a valid explanatory restatement of
  translation-invariance/continuity, not a new hypothesis.
- Evidence: the checks use \eqref{E:vertex-summability},
  \eqref{E:masked-chain-mass}, \eqref{E:masked-order-comparison},
  \eqref{E:masked-two-point}, and \eqref{E:masked-average-source}. OLD LF
  117–159 and NEW LF 146–210 contain the same derivation; the NEW-SF additions
  are only the four Step headings, the two explanatory sentences, and the Step
  4 translation remark.
- Lost steps/qualifiers: none identified within this read. The local-cone
  Picard existence and uniqueness, the summable mixed-order majorant, the
  Bochner testing, and the restriction of stationarity to the unmasked law are
  all present in both.
- Pre-existing concerns: none material; "an Bochner \(L^2\) integral" in the
  statement is an unchanged editorial typo in both revisions and is not a
  mathematical defect. The proof again relies on the unassigned
  Lemma~\ref{L:vertex-crude} and the preceding lemma, which is scope, not a
  new issue.

## P:masked-canonical-transfer

- Old reading: COMPLETE (OLD statement LF 161–175; proof LF 177–212)
- New reading: COMPLETE (NEW statement LF 212–226; proof LF 228–283)
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Fixed-order canonical limit.** For fixed \(n,k\) and terminal
     \((t,0)\), at even \(n+k=2l\) the common-width diagram is
     \[
     A_{\rho,n,k}=\sum_{D\in\Pi_l}\int\prod_{\{i,j\}\in D}
     C_\rho(s_i,z_i;s_j,z_j)\mathrm d(\nu_n^{t,0}\otimes\nu_k^{t,0}).
     \]
     Reversal \(s'_j=t-s_{n+1-j}\), \(z'_j=-z_{n+1-j}\) (and likewise for the
     second chain) preserves the covariances: \(K_\eta\) depends on \(|s-r|\)
     and \(\Gamma_{2\varepsilon}\) is even, so time differences and spatial
     differences are unchanged up to sign. The vertex relabelling \(r\) sends
     each pairing \(\{i,j\}\) to \(\{r(i),r(j)\}\), producing the exact
     initial-chain convention in Proposition~\ref{P:mixed}, including the
     empty-chain case. The Green smoothing is removed first, and
     Lemma~\ref{L:joint-fixed-order} gives the joint limit of each two-chain
     diagram at arbitrary relative noise-width rates; odd mixed moments stay
     zero. Hence
     \[
     \mathbb E[X_{\rho,n}(t,0)X_{\rho,k}(t,0)]
     \longrightarrow\mathbb E[X_n(t,0)X_k(t,0)].
     \]
  2. **Double majorant and full moment.** Every absolute mixed moment, before
     and after the limit, is bounded by \(q_n(t)q_k(t)\). Since
     \(\sum_{n,k}q_nq_k=Q_t^2<\infty\), given \(\delta>0\) one can choose a
     finite square \(F\) of orders with
     \(\sum_{(n,k)\notin F}q_nq_k\le\delta\). For \(\rho\to0\),
     \[
     |A_\rho-A|\le\sum_{(n,k)\in F}|A_{\rho,n,k}-A_{n,k}|+2\delta,
     \]
     where \(A_\rho=\mathbb E|u_\rho(t,0)|^2\) and \(A=\mathbb E|u(t,0)|^2\).
     The finite limits hold jointly; \(\delta\) is arbitrary, so
     \eqref{E:masked-unmasked-moment-limit} follows. Proposition~\ref{P:mixed}
     identifies \(A\) with the canonical sum, and both versions explicitly note
     this uses single-width diagram laws without constructing a new pathwise
     canonical solution family.
  3. **Conditional masked transfer.** If the masked averages
     \(\int\phi u_\rho^m\) converge in \(L^2\) to \(Z_m(t,\phi)\), then
     their second moments converge:
     \[
     |\mathbb E|B|^2-\mathbb E|A|^2|
     =|\|B\|_2^2-\|A\|_2^2|
     \le\|B-A\|_2(\|B\|_2+\|A\|_2)\to0.
     \]
     Passing to the limit in \eqref{E:masked-average-source}, whose right-hand
     side converges by \eqref{E:masked-unmasked-moment-limit}, gives
     \eqref{E:masked-conditional-transfer}. Both versions keep the masked
     limit as an explicit premise and note the next section constructs it on
     the relevant phase.

- Argument preservation: PRESERVED. The NEW proof preserves the reversal,
  relabelling, Green-removal, arbitrary-relative-rates, odd-zero, double
  majorant, and explicit conditional premise steps exactly.
- New explanations: JUSTIFIED.
  (i) "The relabelling \(r\) below reverses the vertex order separately within
  each chain" accurately describes the subsequent mapping.
  (ii) The added factoring of the squared-norm difference is correct: the
  displayed inequality follows from factoring
  \(\|B\|_2^2-\|A\|_2^2=(\|B\|_2-\|A\|_2)(\|B\|_2+\|A\|_2)\) and the reverse
  triangle inequality (equivalently Cauchy–Schwarz plus the triangle
  inequality), and \(L^2\) convergence makes both right-hand factors bounded
  and the difference tend to zero.
- Evidence: the public working above checks the reversal/invariance, the
  \(\varepsilon\)-\(\delta\) tail argument, the second-moment continuity, and
  the conditional transfer using \eqref{E:masked-average-source},
  \eqref{E:masked-unmasked-moment-limit}, and the declared arbitrary
  relative-rate content of Lemma~\ref{L:joint-fixed-order}. OLD LF 177–212 and
  NEW LF 228–283 match step-for-step apart from the inserted Step markers and
  the two explanatory clarifications.
- Lost steps/qualifiers: none identified within this read. The requirement
  the limit hold "at arbitrary relative rates of the two widths" is preserved,
  and the masked-limit convergence remains explicitly conditional. The
  order-zero/empty-chain cases remain included via Proposition~\ref{P:mixed}
  and Lemma~\ref{L:joint-fixed-order}.
- Pre-existing concerns: the proof delegates the joint diagram limits to
  unassigned Lemma~\ref{L:joint-fixed-order} and the canonical sum to
  unassigned Proposition~\ref{P:mixed}; those are upstream inputs, not rewrite
  defects. With \(\Gamma=0\), all \(n+k\ge2\) diagrams vanish, the canonical
  and regularized second moments reduce to \(1\), and the transfer inequality
  becomes the consistent \(\|\phi\|_1^2\le\|\phi\|_1^2\) case; no separate
  assumption is missing here.

## AUDIT dispositions

No literal `AUDIT` marker or comment remains in the NEW module text. No
AUDIT-worthy defect introduced by the rewrite was found in the three assigned
proofs. The only items worth recording are editorial/scope notes, not defects:

- The statement "an Bochner \(L^2\) integral" is an unchanged typographical
  error in both revisions (P:masked-source-moments); it does not affect
  mathematics.
- The proofs rely on unassigned upstream results
  (Lemma~\ref{L:vertex-crude}, Lemma~\ref{L:joint-fixed-order},
  Lemma~\ref{L:source-pointfield-regularity}, Proposition~\ref{P:mixed},
  and the source-convergence module). Their hypotheses were checked as applied;
  their proofs are outside the assigned scope.
- No missing condition was identified in the target consumers’ use of the
  supplied upstream statements: common-width \(\rho=(\varepsilon,\eta)\)
  matches the declared joint covariance
  \(K_\eta(s-r)\Gamma_{2\varepsilon}(z-w)\), the arbitrary-relative-width
  limit premise matches Lemma~\ref{L:joint-fixed-order}, and the
  positive-\(\rho\) hypothesis is respected throughout.

## Findings and limits

The three assigned proofs are mathematically equivalent between OLD and NEW.
The rewrite reorganizes each proof with explicit Step headings and adds
short explanatory sentences, several labeled "new explanations" above; every
added sentence was checked and found justified under the same hypotheses, with
no lost step, qualifier, normalization factor, width specification, or
order-zero/Gamma=0 special case dropped. The target statements are unchanged
for all three labels (only line offsets shifted).

The public reconstruction is COMPLETE for all three proofs, including the
chain-mass induction, covariance bound, Walsh-diagram comparison, Picard
existence/uniqueness, stationarity/testing, fixed-order reversal, double
majorant, and conditional transfer. No required target step was left
unreconstructed, so no partial-reading restriction applies.

These findings concern only the readability-equivalence of the three assigned
proofs in this one module. I do not certify the upstream analytic results, the
whole book, Lean quotation correspondence, source images, rendered pages, or
any release claim. Confidence is high for the assigned comparison; confidence
in the upstream results is deliberately not asserted here.
