# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

The seven assigned rewritten proofs are faithful reorganizations of the old
proofs. Every substantive step, constant, qualifier, hypothesis and cross-reference is
retained; the added material consists of step headings plus short explanatory
sentences, each of which I verified as mathematically correct under the same
hypotheses. No step or qualifier was lost, and no unjustified assertion was
introduced.

## L:cameron-fractional-products
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The old proof (LF 44–79) is reorganized into Steps 1–3 with an
  introductory sentence. All old sentences are present verbatim in the new text
  (LF 44–100): the $H^1$ product map (approximation by compact smooth factors,
  Cauchy property with norm bound $\sqrt{R_{\mathrm{sp}}}N(f)N(g)$, the PSD
  identity $fg=((f+g)^2-(f-g)^2)/4$), the dyadic-band decomposition (Eq.
  E:cameron-dyadic-product), and the identification of physical vs. Hilbert
  product series. The only genuinely new mathematical sentences are in Step 2:
  “On band $j$, the gradient norm is at most $2^j\|f_j\|_2$” — correct, since
  $D_j$ is supported in $|\xi|\in[2^{j-1},2^j)$ (with factor one for $j=0$, as
  the retained sentence notes); substituting into
  $N(f)=\|f\|_2^{1-\alpha/4}\|\nabla f\|_2^{\alpha/4}$ yields
  $N(f_j)\le2^{j\alpha/4}\|f_j\|_2$; and the rewrite
  $2^{j\alpha/4}\|f_j\|_2=2^{-j(s-\alpha/4)}(2^{js}\|f_j\|_2)$ plus
  Cauchy–Schwarz gives $\sum_jN(f_j)\le C_s\|f\|_{H^s}$ under
  $s>\alpha/4$, matching the retained inequality
  $\sum_j2^{-2j(s-\alpha/4)}<\infty$. Statements (OLD 29–42 = NEW 29–42) are
  identical, including the constants $C_s^2\sqrt{R_{\mathrm{sp}}}$ and
  $C_s^4R_{\mathrm{sp}}$.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none
  identified within this read.

## P:cameron-spatial-map
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 101–142 is reorganized into Steps 1–4 (NEW LF 122–190) with
  no sentence removed. Step 1 (row identification via physical Fubini, evenness
  of $\Gamma$, $L^2$ state approximation, use of
  Lemma L:cameron-fractional-products), Step 3 (compact-operator values via
  cutoff singular values with gain one, finite-rank $c_1$ column, zero $c_2$
  column), and Step 4 (Gram–Schmidt basis, projection $Q_n$, operator-norm
  approximation $\|T_{\mathrm{sp}}(I-Q_n)\|\le\sup_{k\in\mathcal L}\|(I-Q_n)k\|\to0$)
  are unchanged. Two additions are justified. (i) Step 2 adds “The velocity
  coordinate $w_2$ lies in $H^{-1/2}$, so $w'=\Lambda^{-1}w_2$ lies in
  $H^{1/2}$ with the corresponding bound”: correct since
  $\Lambda^{-1}:H^r\to H^{r+1}$, consistent with the retained statement’s
  definition $w'=\Lambda^{-1}w_2$. The claim that both localized state factors
  $\eta_Rz_1$, $\eta_Rw'$ use the same cutoff map is consistent with
  Proposition P:cutoff-singular-values at $\sigma=s$, $\gamma=1/2-s>0$
  (requiring $s<1/2$, present in the hypothesis $\alpha/4<s<1/2$; nonemptiness
  uses $\alpha<2$ from the threshold, as retained). (ii) Step 4’s spelled-out
  finite-net argument is the standard one: strong convergence on net centers
  plus $\|I-Q_n\|\le1$ gives uniformity on compact $\mathcal L$. Statements
  (OLD 84–99 = NEW 105–120) are identical, including the exact row identity
  $k(z,w)=(\eta_Rz_1+c_1\eta_R)(\eta_Rw')$.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none
  identified within this read (the reliance on P:cutoff-singular-values is
  pre-existing and its stated hypotheses are respected).

## L:cameron-supported-tensor
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (no new explanations; text is verbatim)
- Evidence: The proofs (OLD LF 158–176, NEW LF 206–224) are identical, including
  the uniform-error tensorization estimate, countable smooth-test density,
  Gram–Schmidt skipping zeros, the closed-image isometric embedding into $H_W$,
  and the explicit disclaimers “It is not multiplication by a time indicator and
  gives no independence of disjoint time intervals.” Statements (OLD 150–156 =
  NEW 198–204) are identical.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none
  identified within this read.

## P:cameron-temporal-map
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 195–242 becomes Steps 1–4 (NEW LF 243–328). All old content is
  retained: Schur bounds, Gamma representation and uniform Fayérier expression
  $\int_{\R}2\lambda(\lambda^2+\xi^2)^{-1}|\widehat f(\xi)|^2 d\xi>0$ “in the
  unitary Fourier convention,” $\int\lambda^{a-1}/\Gamma_E(a)$ weighting,
  truncated kernel $K_\epsilon$ compactness with Schur norm
  $2\epsilon^{1-a}/(1-a)$, the isometry $\iota$ and $C_tf=Kf$ on tests, the
  $L^{r/2}$ membership of $K_a$, Young duality with exponents $u=r/2$, $v=r'$,
  the three-factor Hölder split, interpolation compactness, and the cell
  indicators summing to $2N^a/((1-a)(2-a))$. Additions verified: Step 2’s
  “orthogonal to the range of the self-adjoint square root implies in its
  kernel” is the standard $\operatorname{Ran}(K^{1/2})^\perp=\ker K^{1/2}=\ker
  K=0$ argument, justifying onto-ness. Step 3’s “$r<2/a$ gives $ar/2<1$, so the
  truncated power kernel belongs to $L^{r/2}$”: $\int_0^1|v|^{-ar/2}dv<\infty$
  iff $ar/2<1$; the Young pairing $\langle K_a*g,g\rangle\le\|K_a\|_{r/2}\|g\|_{r'}^2$
  is exactly the retained displayed bound. The subsubsequence argument for
  $L^{r}$-compactness from $L^2$-compactness plus $L^{r_2}$-boundedness via
  interpolation is a correct elaboration of the retained sentence. Step 4’s
  cell computation is exact: for a cell of length $1/N$ the double integral is
  $2N^{a-2}/((1-a)(2-a))$, the orthonormal normalization contributes $N$, and
  summing $N$ cells gives $2N^a/((1-a)(2-a))\to\infty$; positivity then bounds
  every finite orthonormal sum by the trace, excluding trace class. Statements
  (OLD 181–193 = NEW 229–241) are identical, including the non-trace-class and
  non-Hilbert–Schmidt conclusions.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: the word
  “strictly positive” is a pre-existing form-positivity statement (the proof
  establishes $\langle Kf,f\rangle>0$ for $f\ne0$, not $K\ge cI$); this nuance
  is present identically in both versions and is not a rewrite defect.

## P:cameron-full-mean
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 272–315 becomes Steps 1–4 (NEW LF 358–423). Retained verbatim:
  the dimension-free temporal estimate, $L^{r'}$-duality via the pointwise
  direction $\|\mathcal U\Phi\|^{r-2}\mathcal U\Phi$, strong measurability of the
  Bochner field, the statement that spatial covariance is applied once by
  $T_{\mathrm{sp}}$, the multiplier identification $iB_F(m_Rh_\Phi(s))$, the
  $T_n=T_{\mathrm{sp}}Q_n\mathcal U$ approximation, and the weak-null
  subsequence argument for the tail
  $\epsilon_J=\|T(I-P_J)\|_{H\to L^r(\mathcal K(F))}\to0$ with the correct
  order of limits (fixed $R$, independent of $\delta$). The single added
  Step 3 elaboration (“for a fixed finite spatial projection, only finitely many
  scalar temporal images… choose a convergent subsequence for the first
  coordinate, then successively for the remaining coordinates… finite linear
  combination converges in the operator-valued $L^r$ norm”) is the correct
  finite diagonal argument, compatible with the retained sentence that each
  coordinate extraction $H\to H_t$ has norm at most one and its image under
  $C_t$ is precompact in $L^r$. The retained caveat “Scalar time compactness
  alone tensored with an infinite identity would not prove this” is preserved.
  Statements (OLD 250–270 = NEW 336–356) are identical.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none
  identified within this read.

## L:cameron-actual-residual
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 354–381 becomes Steps 1–2 (NEW LF 462–506). Retained verbatim:
  the variance bound $\operatorname{Var}Y_{m,J}(f)\le\|f\|_{H_W}^2$ via
  pullback isometry and $Q_J$ orthogonality, application of
  Proposition P:source-gaussian-transfer, retention of the true $F$ extension
  and both constant columns, choice $\theta<\beta<\beta_2$, constant stopping
  into the little $C^\theta$ closure, separability via L:raw-block-inputs, the
  slow-pullback membership of every observed row in $H_I$ by dominated
  convergence, the endpoint inclusion, the projected transfer
  $f\mapsto W(P_HQ_JT_{\delta,m}f)$ preserving observed rows, and the final
  disclaimers “Original global-basis tests were not assumed individually
  supported. No time-support independence or Hilbert-valued noise is used.”
  The single added Step 2 sentence (“The projection $P_J$ has range in $H_I$, so
  subtracting it from a vector already in $H_I$ keeps that vector in $H_I$… This
  is a Hilbert-subspace statement, not multiplication of the original noise by a
  time indicator”) is correct: each basis vector $e_j$ has a representative
  supported inside $I\times\R^d$, so $\operatorname{Ran}P_J\subset H_I$, and
  $H_I$ is a closed subspace of $H_W$ by the tensor lemma, so $Q_JH_I\subset
  H_I$. This addition correctly preserves the required distinction between a
  legitimate subspace projection and an unjustified multiplier on the
  covariance-null noise quotient. Statements (OLD 341–352 = NEW 449–460) are
  identical.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none
  identified within this read.

## P:cameron-actual-embedding
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD LF 409–478 becomes Steps 1–5 (NEW LF 534–636). Retained verbatim:
  the pullback covariance $\E[Y_{m,J}(f)W(\Phi)]=\delta^{a/2}\int f(v,x)h_{Q_J\Phi}(s_m+\delta v,x)$,
  the $g_\delta$ factor producing $\sqrt\delta$, Eq. E:cameron-actual-covariance
  with both constant columns, the strong continuity of $S_F$ and its adjoint, the
  Bessel-unitary Fourier matrix, the norm continuity of conjugation
  $S_F(-v)AS_F(v)$ on compact $A$ and the avoided claim of norm continuity of
  the free group, the primitive bound E:cameron-local-primitive-bound, the
  identification of the Cameron preimage norm via
  $H_{\mathrm{seen}}=\overline{\operatorname{span}}\{k_\ell\}$ and
  $\ker L_{\delta,J}=H_{\mathrm{seen}}^\perp$ without an inverse covariance, and
  the finite power-mean/true-partition summation including an empty last
  interval. Two additions verified. Step 3’s derivation of the primitive bound
  is exact: increment
  $\le G_B^2(u_2-u_1)^{1-1/r}\delta^{-1/r}\|M\|_{L^r(I_m)}$ (Hölder in the fast
  variable and affine pullback), giving supremum coefficient $B^{1-1/r}$ and
  $\theta$-seminorm coefficient $B^{1-1/r-\theta}$, exactly the two terms in
  $C_B=G_B^2[B^{1-1/r}+B^{1-1/r-\theta}]$. Step 5’s algebra is exact:
  $\delta^{1/p}$ from the $\delta$-weighted norm leaves
  $\sqrt\delta\,\delta^{1/p-1/r}$; power mean gives $n^{1/p-1/r}$
  ($n=N+1\ge2$), combined as $(\delta n)^{1/p-1/r}$; $n\le2/(\delta B)$ and the
  positivity of $1/p-1/r$ (since $p<r$, from E:cameron-block-parameters
  $1/\theta\le p<2<r$) give $(2/B)^{1/p-1/r}>0$. The retained final bounds
  E:cameron-averaged-bound and the radius-fixing/no-uniform-radius caveats are
  unchanged. Statements (OLD 383–407 = NEW 508–532) are identical, including
  $G_B$, $C_B$ and the $\sqrt\delta\,C_B(2/B)^{1/p-1/r}\epsilon_J$ scale.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none
  identified within this read.

## AUDIT dispositions
No AUDIT comments remain and I found no AUDIT-worthy issue introduced by the
rewrite. Items I checked and confirmed preserved rather than flagged: (i) the
fixed-radius character of all compactness conclusions and both
No-go 25/27 contextual disclaimers remain; (ii) no block independence and no
uniform-in-radius compactness is inferred anywhere; (iii) the constant
$F$-coordinates ($c_1,c_2$ and both columns) are retained in the spatial map,
the residual transfer and the Cameron covariance; (iv) the noise-space inclusion
$H_I\hookrightarrow H_W$ and source-coupling (restriction to $W$ on $H_I$) are
unchanged; (v) the exact scalar time pullbacks, the true full/last/empty cells
($\ell_N=\delta^{-1}-NB\in[0,B)$), the residual norm $M=TQ_J\Phi$, and all
ordered limits ($\epsilon_J\to0$ after fixing $R$, independent of $\delta$) are
retained; (vi) all normalization conventions (unitary Fourier in the temporal
positivity computation and the Bessel-unitary Fourier matrix) are unchanged.

## Findings and limits
Scope: I read both whole modules (OLD and NEW) as embedded, so every assigned
proof is COMPLETE. I compared the statements and proofs in their exact LF
ranges; all seven statements are byte-equivalent in mathematical content and all
seven proofs preserve every step with only justified explanatory insertions and
step formatting. I did not certify any unassigned upstream result
(P:cutoff-singular-values, P:source-gaussian-transfer, L:raw-block-inputs,
P:nogo-25/27, Lemma L:spatial-physical-pair, or the source/operator-driver
machine). Consumer uses of those imported results respect their stated
hypotheses as supplied: the cutoff gain $1/2-s>0$ needs $s<1/2$ (given), the
transfer needs a variance bound by $\|f\|_{H_W}^2$ (given by pullback isometry
plus $Q_J$ orthogonality), and the little-Hölder separability and slow-pullback
membership invoked from L:raw-block-inputs are consistent with that baseline’s
supplied statement and proof. The one pre-existing terminological nuance, the
word “strictly positive” for the compact time operator (form positivity, not
uniform positivity), is clarified by the proof in both versions and is not a
rewrite defect. I did not review rendered pages, primary-source fidelity, or
Lean quotation correspondence, as assigned. No missing genuinely needed context
was identified; the cross-module references match the supplied baseline
sources.
