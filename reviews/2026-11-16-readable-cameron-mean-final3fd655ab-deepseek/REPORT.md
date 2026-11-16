# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro (model id `deepseek/deepseek-v4-pro`)
Verdict: PASS
Confidence: high

The 7 assigned proof labels were compared between OLD (`cdde711`) and NEW (`3fd655ab`). In every label the statements/definitions are unchanged in content, only the line intervals shifted. No step, quantifier, constant, or fixed-radius/block qualifier was lost. The changes are step relabelling plus added explanatory sentences; each added assertion was re-derived independently below and holds under the same hypotheses. Remaining imperfections are pre-existing compressions, listed in Findings, not rewrite defects.

## L:cameron-fractional-products

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage.
(i) *Business on $H^1$ factors.* The input is the unassigned
`P:spatial-four-linear`, which supplies $N(f)=\lVert f\rVert_2^{1-\alpha/4}\lVert\nabla f\rVert_2^{\alpha/4}$ and the absolute four-linear bound `\eqref{E:spatial-four-linear}`. For smooth compact $f,g$, PSD plus that bound makes products Cauchy in $H_{\mathrm{sp}}$ with $\lVert fg\rVert\le\sqrt{R_{\mathrm{sp}}}N(f)N(g)$. Expanding $(fg-f'g')$ gives independence of approximation. The polarization $fg=((f+g)^2-(f-g)^2)/4$ gives PSD for products, since `P:spatial-four-linear` already proves PSD of the square pairing.
(ii) *Dyadic bands.* $D_0=1_{\{|\xi|<1\}}$, $D_j=1_{\{2^{j-1}\le|\xi|<2^j\}}$, $f_j=D_jf$. Since $\lVert\nabla f_j\rVert_2\le 2^j\lVert f_j\rVert_2$ (with factor $1$ on $D_0$),
\[
N(f_j)\le \big(2^j\lVert f_j\rVert_2\big)^{\alpha/4}\lVert f_j\rVert_2^{1-\alpha/4}=2^{j\alpha/4}\lVert f_j\rVert_2.
\]
Weighted Cauchy–Schwarz,
\[
\sum_j 2^{j\alpha/4}\lVert f_j\rVert_2
=\sum_j 2^{-j(s-\alpha/4)}\big(2^{js}\lVert f_j\rVert_2\big)
\le \Big(\sum_j2^{-2j(s-\alpha/4)}\Big)^{1/2}\Big(\sum_j2^{2js}\lVert f_j\rVert_2^2\Big)^{1/2},
\]
converges iff $s>\alpha/4$; the second factor is $\le 2^{s}\lVert f\rVert_{H^s}$ by $\langle\xi\rangle^{2s}\ge 2^{-2s}2^{2js}$ on the $j$-band. This yields `\eqref{E:cameron-dyadic-product}`. Summability $\sum_j\lVert f_j\rVert_2<\infty$ follows the same way using $s>0$.
(iii) *Series identification.* Applying the absolute $H^1$ four-linear bound bandwise gives total mass $\le R_{\mathrm{sp}}\prod_{\ell=1}^4\sum_jN((f_\ell)_j)<\infty$; Tonelli plus the null-set transfer of unassigned `L:spatial-physical-pair` gives an a.e. converging physical product series and `\eqref{E:cameron-fractional-absolute}`. The double series $\sum_{j,k}f_jg_k$ is absolutely convergent in $H_{\mathrm{sp}}$ by the $H^1$ bound, and its partial sums are products of $H^1$ functions; the physical identification gives `\eqref{E:cameron-fractional-product}`. Density of compact smooth functions in $H^s$ gives uniqueness of the bilinear extension.

Constants check: product bound $\sqrt{R_{\mathrm{sp}}}C_s^2$; absolute bound $R_{\mathrm{sp}}C_s^4$; both match.

Argument preservation: PRESERVED. New explanations: JUSTIFIED. The added Step 2 sentences (“gradient norm at most $2^j\lVert f_j\rVert_2$”, the rewritten weighted CS) are exactly the derivation above. No quantifier lost; “no $L^p$ multiplier result is used” is retained.

Evidence: labels `\eqref{E:cameron-dyadic-product}`, `\eqref{E:cameron-fractional-product}`, `\eqref{E:cameron-fractional-absolute}` agree in both revisions; expanded text lies in OLD LF 44–79 / NEW LF 44–99 with no structural change.

Lost steps/qualifiers: none identified within this read. Pre-existing concern: the $H^1$-product completion step is compressed, but it is inherited from `P:spatial-four-linear` and is not changed.

## P:cameron-spatial-map

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage.
(i) *Row identity.* For smooth compact $q$, $\Gamma*q$ is smooth on compacts by differentiation under the compact Radon integral, so $m_R(\Gamma*q)$ is smooth compact. With $w'=\Lambda^{-1}w_2$, the velocity pairing carries weight $\Lambda^{-1}$, and Fubini produces
\[
\langle T_{\mathrm{sp}}q\,z,w\rangle_F = B_\Gamma(q,k(z,w)),\qquad k(z,w)=(\eta_Rz_1+c_1\eta_R)(\eta_Rw'),
\]
with evenness supplying symmetry. This is `\eqref{E:cameron-spatial-row}`. Extension to $q\in H_{\mathrm{sp}}$ uses density of smooth compact tests and continuity of both sides: the left by the bounded extension of $T_{\mathrm{sp}}$ and the right because $k(z,w)\in H_{\mathrm{sp}}$ for the relevant states.
(ii) *Compact test family.* $w'=\Lambda^{-1}w_2\in H^{1/2}$ whenever $w_2\in H^{-1/2}$, since $\lVert w'\rVert_{H^{1/2}}=\lVert w_2\rVert_{H^{-1/2}}$. Unassigned `P:cutoff-singular-values` gives that multiplication by $\eta_R$ sends bounded $H^{1/2}$ sets to precompact $H^s$ sets with gain $1/2-s>0$; apply to $z_1$ and $w'$. The $c_1\eta_R$ family is one-dimensionally parameterised, hence compact. The product map $(f,g)\mapsto fg$ is continuous on $H^s\times H^s\to H_{\mathrm{sp}}$ by the fractional bound, so the image of two compact factors has compact closure $\mathcal{L}$. Then
\[
\lVert T_{\mathrm{sp}}q\rVert_{\mathcal K(F)}\le \sup_{z,w}\lVert k(z,w)\rVert_{H_{\mathrm{sp}}}\lVert q\rVert_{H_{\mathrm{sp}}}\le \sup_{k\in\mathcal L}\lVert k\rVert\,\lVert q\rVert,
\]
so null classes map to $0$.
(iii) *Compact operator values.* For smooth $q$, multiplication by its potential is compact $H^{1/2}\to H^{-1/2}$ by the same cutoff result with gain $1$; the $c_1$ column is finite rank and the instantaneous $c_2$ column is zero. Operator-norm closure gives values in $\mathcal K(F)$.
(iv) *Compactness of the map.* Separability of $H_{\mathrm{sp}}$ (now explicitly justified) gives a complete smooth-test ONB via Gram–Schmidt; $Q_n$ projects onto its first $n$ terms. The row identity yields
\[
\lVert T_{\mathrm{sp}}(I-Q_n)\rVert\le \sup_{k\in\mathcal L}\lVert(I-Q_n)k\rVert\to0,
\]
by uniform strong convergence on the compact set $\mathcal L$ (finite-net argument, $\lVert I-Q_n\rVert\le1$). Each $T_{\mathrm{sp}}Q_n$ has finite-rank range; the operator-norm limit is compact.

Argument preservation: PRESERVED. New explanations: JUSTIFIED.
- Step 2 sentence “$w_2\in H^{-1/2}$ and $w'=\Lambda^{-1}w_2\in H^{1/2}$” is the Bessel identity above.
- Step 4 separability sentence: for a fixed compact $K$, local Radon finiteness gives $|B_\Gamma(f,g)|\le \Gamma(K-K)\lVert f\rVert_\infty\lVert g\rVert_\infty$, so a countable sup-norm-dense smooth family on exhausting compacts is $H_{\mathrm{sp}}$-dense (this is the same bound used in unassigned `L:source-spatial-heat`). Therefore the new justification is valid.

Evidence: `\eqref{E:cameron-spatial-row}` identical; radius $R$ fixed; “the same whole-space cutoff result with gain one” retained; new separability paragraph is local-Radon based and consistent.

Lost steps/qualifiers: none identified within this read. Pre-existing concern: the phrase “for general states the localized products are $L^1$” is imprecise as a literal statement for arbitrary $q\in H_{\mathrm{sp}}$, but the row extension only needs density and continuity, which are supplied; unchanged in both revisions.

## L:cameron-supported-tensor

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage.
(i) *Separated tests.* On $f(t,x)=\tau(t)\sigma(x)$, absolute Fubini turns the original inner product into the tensor of the time form ($|s-t|^{-a}$) and the spatial form $B_\Gamma$, after the respective null quotients. This is legitimate because the spatial pairing is absolutely integrable on compact supports and the time kernel row is finite for $a<1$.
(ii) *Finite-tensor density.* A smooth compact spacetime test is uniformly approximated by a smooth time partition times its spatial slices on one compact support $I\times A$. For an error of sup norm $\le\varepsilon$, its squared $H$-norm is bounded by
\[
\varepsilon^2|A|\,\Gamma(A-A)\int_I\int_I |s-t|^{-a}\,ds\,dt<\infty.
\]
This also yields countability/density on exhausting compacts in $H$ and $H_{\mathrm{sp}}$.
(iii) *Basis and embedding.* Gram–Schmidt skipping zero residuals keeps smooth compact support. The isometric embedding into $H_W$ has closed image by completeness. The finite orthonormal projection $P_Jf=\sum_{j\le J}\langle f,e_j\rangle e_j$ remains an orthogonal projection on $H_W$. It is not a time-indicator multiplication and gives no independence of disjoint time intervals.

Argument preservation: PRESERVED (the proof text is unchanged; only LF locations shifted).
New explanations: none introduced (text identical).
Evidence: the displayed covariance bound and the final non-independence qualifier are verbatim in both.

Lost steps/qualifiers: none. Pre-existing concern: “tensor product after both null quotients” relies on the unassigned temporal completion `L:masked-time-completion` and spatial square completion; that is an upstream input, not re-proved here.

## P:cameron-temporal-map

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage.
(i) *Positivity/compactness of $K$.* Schur bounds $K$ by its finite row/column integrals. For the zero-extended test $f$,
\[
\int_{\mathbb R}\int_{\mathbb R} e^{-\lambda|s-t|}f(s)f(t)\,ds\,dt
=\int_{\mathbb R}\frac{2\lambda}{\lambda^2+\xi^2}|\widehat f(\xi)|^2\,d\xi>0\quad(f\ne0),
\]
in the unitary convention; this follows because the unitary Fourier transform of $e^{-\lambda|\cdot|}$ convolved as above gives multiplier $2\lambda/(\lambda^2+\xi^2)$. Integrating this against $\lambda^{a-1}/\Gamma_E(a)$ gives $\langle f,Kf\rangle>0$, hence strict positivity and injectivity. Symmetry gives self-adjointness. The truncation $K_\varepsilon=K1_{\{|s-t|\ge\varepsilon\}}$ is square-integrable, hence Hilbert–Schmidt and compact, and the Schur norm of $K-K_\varepsilon$ is at most
\[
2\int_0^\varepsilon v^{-a}\,dv=\frac{2\varepsilon^{1-a}}{1-a}\to0.
\]
Compact spectral theorem gives compact positive square root.
(ii) *Completion identification.* On tests $\lVert K^{1/2}f\rVert_2^2=\langle f,Kf\rangle=\lVert f\rVert_{H_t}^2$. Dense smooth tests in $L^2$ plus $\ker K=0$ make the range dense; the isometry from $H_t$ has closed range, hence is onto $L^2(I)$. On tests $C_tf=K^{1/2}\iota(f)=K^{1/2}K^{1/2}f=Kf$. Thus `\eqref{E:cameron-temporal-map}` first means the $L^2$ map.
(iii) *$L^r$ bound.* Extend $K_a(v)=|v|^{-a}1_{\{|v|\le1\}}$. Since $r<2/a$, $ar/2<1$, so $K_a\in L^{r/2}$. For $g$ supported in $I$,
\[
\lVert g\rVert_{H_t}^2=\iint |s-t|^{-a} g(s)g(t)\,ds\,dt
=\int (K_a*g)(t)g(t)\,dt
\le \lVert K_a*g\rVert_r\lVert g\rVert_{r'}.
\]
With $u=r/2$, $v=r'$ the Young exponents satisfy $1/u+1/v=1+1/r$; the proof’s three-way Hölder split with exponents $r$, $(1/u-1/r)^{-1}$, $(1/v-1/r)^{-1}$ gives $\lVert f*h\rVert_r\le\lVert f\rVert_u\lVert h\rVert_v$, so $\lVert K_a*g\rVert_r\le\lVert K_a\rVert_{r/2}\lVert g\rVert_{r'}$. Duality then gives $\lVert Kf\rVert_r\le C_{a,r}\lVert f\rVert_{H_t}$ on tests, extended by density. Taking $r<r_2<2/a$, compactness into $L^2$ plus boundedness into $L^{r_2}$ and the interpolation
\[
\lVert u\rVert_r\le\lVert u\rVert_2^{\tau}\lVert u\rVert_{r_2}^{1-\tau},\quad 1/r=\tau/2+(1-\tau)/r_2
\]
give compactness into $L^r$.
(iv) *Non-trace-class.* For cell indicators of length $1/N$, the double integral is
\[
2\int_0^{1/N}\int_0^t (t-s)^{-a}\,ds\,dt=\frac{2N^{a-2}}{(1-a)(2-a)};
\]
multiplying by the normalization factor $N$ gives a diagonal entry $2N^{a-1}/((1-a)(2-a))$. Summing $N$ cells gives $2N^a/((1-a)(2-a))\to\infty$, so $K$ is not trace class, and $K^{1/2}\iota$ is not Hilbert–Schmidt into $L^2$ (its Gramian is exactly $K$, since $\iota$ is a surjective isometry).

Argument preservation: PRESERVED. New explanations: JUSTIFIED.
- The added sentence “$r<2/a$ gives $ar/2<1$” is exactly the integrability of $|v|^{-ar/2}$ at zero.
- The added cell computation matches the closed form above.

Evidence: `\eqref{E:cameron-temporal-map}` unchanged; range $2<r<2/a$ unchanged; “not trace class” and “not Hilbert–Schmidt” retained.

Lost steps/qualifiers: none. Pre-existing concern: strict positivity of $e^{-\lambda|v|}$ is asserted via the displayed Fourier form; for zero-extended $f$ this uses that $\widehat f$ cannot vanish on a set of positive measure (Paley–Wiener), which is not spelled out. Unchanged and acceptable. No trace-class truncation is used as a Gaussian covariance in either revision.

## P:cameron-full-mean

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage.
(i) *Time-only tensor bound.* For a finite-dimensional spatial field $g_s=\sum_j\varphi_j(s)q_j$ with orthonormal $q_j$, Cauchy–Schwarz over the finite sum gives $\sum_j\varphi_j(s)\varphi_j(t)\le\lVert g_s\rVert\lVert g_t\rVert$. Positivity of $|s-t|^{-a}$ gives
\[
\lVert g\rVert_{H_t\otimes H_{\mathrm{sp}}}^2
=\sum_j\iint |s-t|^{-a}\varphi_j(s)\varphi_j(t)\,ds\,dt
\le\iint |s-t|^{-a}\lVert g_s\rVert\lVert g_t\rVert\,ds\,dt.
\]
Applying the scalar bound of `P:cameron-temporal-map` to $a_s=\lVert g_s\rVert\in L^{r'}$ gives the displayed $\le C_{a,r}^2\lVert g\rVert_{L^{r'}(H_{\mathrm{sp}})}^2$. Finite-dimensional $L^r/r'$ duality (with the norming direction $\lVert\mathcal U\Phi\rVert^{r-2}\mathcal U\Phi$ and smooth coefficient approximation in $L^{r'}$) then gives
\[
\lVert\mathcal U\Phi\rVert_{L^r(H_{\mathrm{sp}})}\le C_{a,r}\lVert\Phi\rVert_H,
\]
with no dimension factor. Tensor density and completeness extend to a strongly measurable Bochner field.
(ii) *Multiplier identification.* On separated tests the identity follows from `\eqref{E:cameron-spatial-row}`. For a smooth spacetime test, the tensor-proof separated approximations with uniform error $\varepsilon$ give mean errors controlled by the multiplier bound $\lVert B_F(b)\rVert\le\lVert b\rVert_\infty+\lVert b\rVert_2$ (from unassigned `L:constant-source-response`), and on the fixed support of $m_R$, $\lVert b\rVert_2\le|\operatorname{supp} m_R|^{1/2}\lVert b\rVert_\infty$; hence operator convergence identifies `\eqref{E:cameron-full-mean}`. General $H$ controls carry no pointwise-potential assertion.
(iii) *Compactness of $T$.* With spatial projections $Q_n$,
\[
\lVert T-T_n\rVert\le\lVert T_{\mathrm{sp}}(I-Q_n)\rVert_{\mathcal K(F)}\lVert\mathcal U\rVert_{H\to L^r(H_{\mathrm{sp}})}\to0,\quad T_n=T_{\mathrm{sp}}Q_n\mathcal U.
\]
For fixed $n$, the coefficient extraction $H\to H_t$ along each $q_j$ has norm $\le1$; composing with compact $C_t:H_t\to L^r$ and the compact operators $T_{\mathrm{sp}}q_j$ makes $T_n$ compact. The note that scalar time compactness tensored with an infinite identity cannot prove this is retained.
(iv) *Projection tails.* If `\eqref{E:cameron-compact-tail}` failed, choose unit $v_J$ with $\lVert T(I-P_J)v_J\rVert$ bounded below. Since $(I-P_J)h\to0$ for fixed $h$, the $(I-P_J)v_J\to0$ weakly; compactness gives a strongly convergent image subsequence with weak limit $0$, contradiction.

Argument preservation: PRESERVED. New explanations: JUSTIFIED. The added Step 2 citation is the correct bound and the support-volume remark is elementary.

Evidence: `\eqref{E:cameron-full-mean}`, `\eqref{E:cameron-compact-tail}` unchanged; “dimension-free”, “strongly measurable Bochner”, fixed $r\in(2,2/a)$, and the no-infinite-identity caveat all retained.

Lost steps/qualifiers: none. Pre-existing concern: the finite-dimensional duality step is compressed; it is unchanged and the norming-direction/approximation clause explains it.

## L:cameron-actual-residual

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage.
(i) *Construction of the stopped paths.* The pullback isometry (`L:raw-block-inputs`) and orthogonality of $Q_J=I-P_J$ give
\[
\operatorname{Var}Y_{m,J}(f)=\lVert Q_JT_{\delta,m}f\rVert^2_{H_W}\le\lVert f\rVert^2_{H_W}.
\]
Unassigned `P:source-gaussian-transfer` applies to the Gaussian linear noise $Y_{m,J}$, producing compact-valued transferred $E$-paths and the $F$ extension $A_{m_R}(Y)=iM_YL_\psi$ from `\eqref{E:constant-phase-driver}`. The two localizations (`\eqref{E:constant-phase-localization}`) pass from the shared deterministic coefficients to the transferred path by bounded multiplication. Choose $\theta<\beta<\beta_2$ below the upper threshold in `\eqref{E:cameron-block-parameters}`; path construction at exponent $\beta$ with auxiliary $\beta_2$ gives compact values and $C^\beta$ bounds. Constant stopping $u\mapsto\min(u,\ell_m)$ does not increase the $C^\theta$ norm, so polygonal approximation puts the paths in the little $C^\theta$ closure $\mathscr B_0$, which is separable by `L:raw-block-inputs`.
(ii) *First-chaos statistics.* As in `L:raw-block-inputs`, each observed row’s slow pullback belongs to $H_I$: the time support lies in $[0,1]$ and the indicator approximation converges against the integrable time kernel and locally finite $\Gamma$ on the common compact support, including endpoints. Schwartz $E$ states plus both constant columns supply the identities, extended to $F$ by boundedness. Since $P_J$ has range in $H_I$, subtracting it preserves membership in $H_I$; this is a subspace statement, not a time-indicator multiplication of the noise. Projecting transfer to $P_HQ_JT_{\delta,m}$ leaves observed rows unchanged; countable states and rational times identify the same operator paths. Applying a continuous linear functional $\ell$ gives an $L^2$ limit in the closed isonormal image $W(H_I)$, so $\ell(X)=W(k_\ell)$ with $k_\ell\in H_I$. An empty last interval gives zero.

Argument preservation: PRESERVED. New explanations: JUSTIFIED.
- The added Step 1 notation “$A_{m_R}(Y)$ means $iM_YL_\psi$” is consistent with `P:constant-phase-driver` and the Gaussian transfer machinery.
- The added Step 2 subspace sentence is exactly the closedness of $H_I$ under projection subtraction.

Evidence: `\eqref{E:cameron-block-parameters}` untouched; hollow-Ø notation and separability of $\mathscr B_0$ retained; “No time-support independence or Hilbert-valued noise is used” retained.

Lost steps/qualifiers: none. Pre-existing concern: the phrase “as in `L:raw-block-inputs`, every observed row’s slow pullback belongs to $H_I$” draws on the argument in that unassigned proof rather than a literal hypothesis in its statement; the target supplies its own one-sentence derivation, so this is not a missing context.

## P:cameron-actual-embedding

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage.
(i) *Covariance and $\sqrt\delta$ factor.* For smooth supported $\Phi$, $Q_J\Phi$ is likewise fine. The pullback covariance (the general form of `\eqref{E:raw-block-mean-jacobian}` applied to $\Phi$) gives
\[
\mathbb E[Y_{m,J}(f)W(\Phi)]
=\delta^{a/2}\int f(v,x)\,h_{Q_J\Phi}(s_m+\delta v,x)\,dx\,dv,
\]
where $h_\Phi=|\cdot|^{-a}*(\Gamma*\Phi)$; this substitution is the same $\delta^{a/2}$ computation as in `L:raw-block-inputs` with $s=s_m+\delta v$. Multiplying by $g_\delta=\delta^{(1-a)/2}$ gives $\sqrt\delta$. Inserting the transferred row `\eqref{E:source-transferred-row}` and the row `\eqref{E:cameron-spatial-row}`, with `P:cameron-full-mean` identifying the masked mean as $T(Q_J\Phi)$, yields `\eqref{E:cameron-actual-covariance}`. The $S_F(v)$ action produces displacement $v$ for the velocity entry and leaves the constant displacement equal to one; both columns are included.
(ii) *Bochner compact-operator integral.* $S_F$ and its adjoint are strongly continuous on Hilbert $F$; in Bessel-unitary coordinates the displayed cosine/sine-quotient matrix has a continuous zero-frequency quotient and uniform bound $C(1+B)$, and the same for the adjoint. The constant block is finite-dimensional. For compact $A$, $v\mapsto S_F(-v)AS_F(v)$ is operator-norm continuous: strong convergence is uniform on compact images, and the right factor by adjoints. Joint $(v,A)$ continuity and uniform bounds give Bochner measurability of the conjugated strongly measurable compact-operator field, without asserting norm continuity of the free group.
(iii) *Primitive Hölder bound and extension.* With $M=TQ_J\Phi$, for $u<u'$,
\[
\Big\lVert\int_u^{u'}S_F(-v)M(s_m+\delta v)S_F(v)\,dv\Big\rVert
\le G_B^2|u'-u|^{1-1/r}\delta^{-1/r}\lVert M\rVert_{L^r(I_m)},
\]
because Hölder bounds the pulled-back $L^r$ norm and $s=s_m+\delta v$ has derivative $\delta$. The supremum term uses length $\le B$ and the $\theta$-seminorm divides increments by $|u'-u|^\theta$, with $1-1/r-\theta>0$ by $1/(1-\theta)<r$. This produces exactly
\[
\lVert(L_{\delta,J}\Phi)_m\rVert_{C^\theta}\le\sqrt\delta\,C_B\delta^{-1/r}\lVert M\rVert_{L^r(I_m)},
\]
with $C_B=G_B^2[B^{1-1/r}+B^{1-1/r-\theta}]$, i.e. `\eqref{E:cameron-local-primitive-bound}`. Constant stopping preserves the little $C^\theta$ membership because the stopped path agrees on initial pieces and is constant after; simple compact-operator integrand approximation in $L^r$ places the primitive in $\mathscr B_0$. Density on smooth controls extends the identity to all $H$.
(iv) *Cameron embedding norm.* The covariance map satisfies $\ell(L_{\delta,J}\Phi)=\langle k_\ell,\Phi\rangle_H$ with $\ker L_{\delta,J}=H_{\mathrm{seen}}^\perp$; the first Wiener chaos/Cameron space is $L_{\delta,J}(H_{\mathrm{seen}})$ with the minimum $H$ preimage norm, so a bound in the original $H$ norm is the embedding bound, without inverting a covariance.
(v) *Partition summation.* With $t_m=\lVert M\rVert_{L^r(I_m)}$ and $n=N+1\ge2$, the power mean at exponent $r/p>1$ gives
\[
\Big(\sum_m t_m^p\Big)^{1/p}\le n^{1/p-1/r}\Big(\sum_m t_m^r\Big)^{1/r}.
\]
The true partition gives $\sum_mt_m^r=\lVert M\rVert_{L^r(I)}^r$ including an empty last interval, and $n\le2/(\delta B)$. Since $p<r$, $1/p-1/r>0$, so
\[
\lVert L_{\delta,J}\Phi\rVert_{\delta,p}
\le\sqrt\delta\,C_B(\delta n)^{1/p-1/r}\lVert M\rVert_{L^r}
\le\sqrt\delta\,C_B(2/B)^{1/p-1/r}\epsilon_J\lVert\Phi\rVert_H,
\]
with $M=TQ_J\Phi=T(I-P_J)\Phi$ and $\epsilon_J=\lVert T(I-P_J)\rVert$. This is `\eqref{E:cameron-averaged-bound}`.

Argument preservation: PRESERVED. New explanations: JUSTIFIED.
- Step 1’s citation of `\eqref{E:source-transferred-row}` is applicable because $Y_{m,J}$ satisfies the variance-bound hypotheses of `P:source-gaussian-transfer`.
- Step 3’s incremental derivation reproduces $C_B$ and the exponent $1-1/r$ exactly.

Evidence: `\eqref{E:cameron-actual-covariance}`, `\eqref{E:cameron-averaged-norm}`, `\eqref{E:cameron-averaged-bound}`, `\eqref{E:cameron-local-primitive-bound}` all unchanged; “compact-operator Bochner integral”, “$\epsilon_J\to0$ fixes $R$ independent of $\delta$”, “true partition including an empty last interval”, and the explicit $B$ factor are retained.

Lost steps/qualifiers: none identified within this read. Pre-existing concern: the Cameron-space identification in Step (iv) invokes the standard RKHS/first Wiener chaos correspondence without a formal citation; unchanged and mathematically standard.

## AUDIT dispositions

No new AUDIT-worthy defect was found in the NEW module. The added explanatory sentences are local, justified under the same hypotheses, and do not change any theorem statement, constant, domain of integrability, or fixed-radius/block qualifier. No silent repair of a pre-existing gap was detected: where the rewrite adds words (the $w'$ regularity in `P:cameron-spatial-map`, the $ar/2<1$ integrability and cell computation in `P:cameron-temporal-map`, the multiplier bound source in `P:cameron-full-mean`, the subspace statement in `L:cameron-actual-residual`, the primitive exponent derivation in `P:cameron-actual-embedding`), each is a correct spelling-out of a step already present. The only items one could call AUDIT-worthy are pre-existing compressions (listed below), and they occur identically in OLD.

## Findings and limits

Scope. This report certifies readability/argument-preservation between the two revisions of `notes/integrated_cameron_mean.tex` for the 7 assigned proofs only. It does not certify primary-source fidelity of the imported unassigned inputs (`P:spatial-four-linear`, `P:cutoff-singular-values`, `P:source-gaussian-transfer`, `L:raw-block-inputs`, `L:constant-source-response`, the temporal/spatial completion lemmas, the Gaussian-Schatten machinery, or the Young/trace-class facts). Those were used only after checking the target consumer’s hypotheses.

Preserved qualifiers. Fixed radius $R$ throughout; no uniform-in-radius compactness or tail bound is claimed. No block independence of the $W_{\delta,m}$, no time-support independence, and no Hilbert-valued noise are inferred. The covariance and mask each occur once; the $B$ factor is explicit; the true full/last/empty cell structure of the partition is retained; the physical mask roots state tests and does not multiply an original noise class.

Pre-existing concerns (not introduced by the rewrite, unchanged in both revisions):
1. `P:cameron-spatial-map` row extension: the literal sentence “for general states the localized products are $L^1$” is imprecise for arbitrary $H_{\mathrm{sp}}$ representatives; the actual argument is density plus continuity, which is present.
2. `P:cameron-temporal-map` injectivity uses the Paley–Wiener non-vanishing of the Fourier transform of a zero-extended $f\in L^2(I)$; this is true but implicit.
3. `P:cameron-full-mean` Step 1 finite-dimensional duality and `L:cameron-actual-residual` Step 2’s appeal to the *argument* of `L:raw-block-inputs` (rather than its literal statement) are compressed; both are unchanged and supplied with enough self-contained explanation.
4. `P:cameron-actual-embedding` Step (iv) uses the standard first Wiener chaos/RKHS identification without citation; unchanged.

Contextual limitations. No-go `\ref{P:nogo-25}` and `\ref{P:nogo-27}` in the surrounding text are contextual statements, not separately assigned proofs; they were not re-reviewed. Under unitary Fourier conventions, the inversion/kernel identities used in `P:cameron-temporal-map` and `P:cameron-actual-embedding` are distributional identities, and all normalizations were retained.

Public reconstruction status. All seven assigned proofs are publicly reconstructed to the granularity of their logical steps, including unchanged sections; no target step is left unreconstructed. Reading is COMPLETE for both old and new in all seven labels.
