# Review Result
Category: proof-readability-equability-equivalence
Model: deepseek-v4-pro (deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

The five assigned rewrite pairs preserve the mathematics. The NEW revision adds only
structural step headers, proof outlines, and correct explanatory sentences; no
equation, constant, quantifier, normalization, or limiting convention changed. All
five target deductions reconstruct publicly from checkable estimates, using only the
unchanged statements and the named (UNASSIGNED) upstream statements under verified
application hypotheses. No new defect was found.

## L:uniform-mean-cutoff

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (proof LF 44–62 verbatim identical)
- New explanations: JUSTIFIED (none added; text is identical)
- Original-step coverage:
  1. Peetre multiplier kernel. In the unitary convention the pointwise product
     satisfies $(\eta_R f)^{\hat{}}(\xi)=c_d(\widehat\eta_R*\widehat f)(\xi)$ with
     $c_d=(2\pi)^{-d/2}$: writing $\eta_R(x)=c_d\int e^{ipx}\widehat\eta_R(p)dp$ and
     $f(x)=c_d\int e^{iqx}\widehat f(q)dq$ gives
     $(\eta_R f)^{\hat{}}(\xi)=c_d\int\widehat\eta_R(\xi-q)\widehat f(q)dq$, since
     $c_d\cdot c_d^2\cdot(2\pi)^d=c_d$. Conjugating by $\langle\xi\rangle^{\sigma}$,
     Peetre $\langle\xi\rangle^{\sigma}\le2^{|\sigma|/2}\langle\xi-\eta\rangle^{|\sigma|}
     \langle\eta\rangle^{\sigma}$ (valid for all real $\sigma$ via $|\sigma|$) bounds
     the kernel by $2^{|\sigma|/2}c_d|\widehat\eta_R(\xi-\eta)|\langle\xi-\eta
     \rangle^{|\sigma|}$, a convolution kernel.
  2. $R$-independence. $\widehat\eta_R(q)=R^d\widehat\eta(Rq)$; substituting
     $p=Rq$ gives $L^1$ norm $2^{|\sigma|/2}c_d\int|\widehat\eta(p)|\langle p/R
     \rangle^{|\sigma|}dp\le2^{|\sigma|/2}c_d\int|\widehat\eta(p)|\langle p
     \rangle^{|\sigma|}dp=M_\sigma$, using $\langle p/R\rangle\le\langle p\rangle$
     for $R\ge1$. This is exactly the stated $M_\sigma$, so the $(2\pi)^{-d/2}$
     normalization and constant are correct (I checked by recomputing the
     convolution constant; it is $c_d=(2\pi)^{-d/2}$, not $+d/2$). $L^1*L^2$
     then bounds the multiplier norm on $H^\sigma$ and extends from Schwartz to
     all of $H^\sigma$ by density.
  3. Row bound. $\Lambda^{-1}:H^{-1/2}\to H^{1/2}$ is isometric
     ($\|\Lambda^{1/2}\Lambda^{-1}w_2\|_2=\|w_2\|_{H^{-1/2}}$); $H^{1/2}
     \hookrightarrow H^s$ has norm $\le1$ since $\langle\xi\rangle^{2s}\le
     \langle\xi\rangle$. Hence $\|\eta_Rz_1\|_{H^s}\le\|\eta_Rz_1\|_{H^{1/2}}\le
     M\|z_1\|_{H^{1/2}}$, $\|\eta_R\Lambda^{-1}w_2\|_{H^s}\le M\|w_2\|_{H^{-1/2}}$,
     with $M=M_{1/2}$. The fractional product bound
     (L:cameron-fractional-products, hypotheses $s$ real in $(\alpha/4,1/2)$, real
     $H^s$ factors — both of which our real states satisfy) gives $\|k_R(z,w)\|\le
     A_sM^2\|z\|_E\|w\|_E=M_0\|z\|_E\|w\|_E$.
  4. Operator bound via Cauchy–Schwarz: $\|T_Rq\|=\sup_{z,w}|\langle q,k_R(z,w)
     \rangle|\le M_0\|q\|$. Values lie in $\mathcal K(E)$ as $E$-restricted compact
     operators (retained from P:cameron-spatial-map); the row agrees on smooth
     controls and extends through the completion.
- Evidence: the closed-form computation of $(\eta_Rf)^{\hat{}}$, the substitution
  $p=Rq$ in $\int|\widehat\eta_R|\langle\cdot\rangle^{|\sigma|}$, and the product
  bound composition all reproduce the displayed $M_\sigma,M_0$.
- Lost steps/qualifiers: none identified within this read. Pre-existing dependence:
  the fractional product constant $C_s^2\sqrt{R_{\rm sp}}$ is an upstream statement.

## L:uniform-mean-spatial-tails

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (new proof adds outline, four step headers, one
  explanatory sentence; no math changed)
- New explanations: JUSTIFIED (the added sentence on the constant $4A_sM^2$ is
  correct, see below)
- Original-step coverage:
  1. Translation bound. $\tau_h$ multiplies by $e^{-i\xi\cdot h}$ in the covariance
     Fourier isometry, so $\|\tau_hf-f\|_{H^s}^2=\int|e^{-i\xi h}-1|^2\langle\xi
     \rangle^{2s}|\widehat f|^2d\xi$. With $|e^{-it}-1|\le2\min(1,|t|^\beta)$ and
     $\beta+s=1/2$, I verified the claimed
     $\|\tau_hf-f\|_{H^s}\le2\min(1,|h|^\beta)\|f\|_{H^{1/2}}$ by splitting: for
     $|h|\ge1$ the bound is $\langle\xi\rangle^s\le\langle\xi\rangle^{1/2}$; for
     $|h|\le1$ and $|\xi||h|\le1$ one has $\langle\xi\rangle^s|\xi|^\beta\le\langle
     \xi\rangle^{1/2}$, while for $|\xi||h|>1$ one has $|h|\ge\langle\xi\rangle^{-1}$
     so $\langle\xi\rangle^{s}=\langle\xi\rangle^{1/2-\beta}\le\langle\xi\rangle^{1/2}
     |h|^\beta$. Strong continuity of $\tau_h$ on $H_{\rm sp}$ follows from dominated
     convergence of the multiplier on $L^2(\mu)$ and $V$-invariance.
  2. Row translation estimate. The product identity $\tau_h(fg)-fg=(\tau_hf-f)\tau_hg
     +f(\tau_hg-g)$ extends from smooth to $H^s$ by continuity of the bilinear product
     map into $H_{\rm sp}$ (translations are isometric on $H^s$). With $f=\eta_Rz_1$,
     $g=\eta_R\Lambda^{-1}w_2$: first term $\le A_s(2\min M\|z\|)(M\|w\|)=2A_sM^2
     \min\|z\|\|w\|$, second term identical, total $4A_sM^2\min(1,|h|^\beta)\|z\|
     \|w\|$ — matching (E:uniform-mean-row-translation). The NEW added sentence
     (“$2A_sM^2$ twice”) is exactly this accounting.
  3. Heat averaging. $C_\varepsilon=p_\varepsilon*$ has Fourier multiplier
     $e^{-\varepsilon|\xi|^2/2}$, and $\mathcal F[p_\varepsilon](\xi)=e^{-\varepsilon
     |\xi|^2/2}$ for variance $\varepsilon$ (no extra Fourier factor). Bochner integral
     $\int p_\varepsilon(h)\tau_hk\,dh$ exists ($H_{\rm sp}$ separable, orbit strongly
     continuous, isometric$\Rightarrow$bounded). Then $\|(I-C_\varepsilon)k\|\le
     4A_sM^2\E[\min(1,|\sqrt\varepsilon G_d|^\beta)]\|z\|\|w\|\le4A_sM^2
     \varepsilon^{\beta/2}\E|G_d|^\beta\|z\|\|w\|$; selfadjointness of the row pairing
     in (E:uniform-mean-row) yields (E:uniform-mean-heat) with
     $M_h=4A_sM^2\E|G_d|^\beta$.
  4. Projection $P_K$ without surjectivity/spectral density. $V$ is the closed image
     of $f\mapsto(2\pi)^{d/2}\widehat f$ in $L^2(\mu)$ (the $(2\pi)^{d/2}$ factor from
     $B_\Gamma(f,f)=(2\pi)^d\int|\widehat f|^2d\mu$). For real Schwartz $f$,
     $\widehat f\in V$; $\chi_n\widehat f$ is Schwartz (smooth compact $\times$
     Schwartz) and real/even when $\chi_n,f$ are, hence in $V$; dominated convergence
     ($|\chi_n\widehat f|^2\le|\widehat f|^2\in L^1(\mu)$) gives $1_{\{|\xi|\le K\}}
     \widehat f\in V$ with the closed-ball indicator, the pointwise limit everywhere
     including the boundary sphere (so a $\mu$-charged boundary is harmless).
     Multiplication by the indicator is a contraction and idempotent, preserves $V$,
     and pulls back to a real orthogonal $P_K$; it commutes with the heat multiplier.
  5. Heat-tail conversion. On $|\xi|>K$,
     $1-e^{-|\xi|^2/(2K^2)}\ge1-e^{-1/2}$, hence as multipliers
     $1_{|\xi|>K}\le(1-e^{-1/2})^{-1}(1-e^{-|\xi|^2/(2K^2)})$, so
     $\|(I-P_K)k\|\le(1-e^{-1/2})^{-1}\|(I-C_{K^{-2}})k\|\le M_h/(1-e^{-1/2})
     K^{-\beta}\|z\|\|w\|$; selfadjointness of $P_K$ gives (E:uniform-mean-frequency)
     with $M_f=M_h/(1-e^{-1/2})$.
- Evidence: explicit regime split for the $\min$ bound; the $p=Rq$ identity;
  $\mathcal F[p_\varepsilon]=e^{-\varepsilon|\xi|^2/2}$; the pointwise (not merely
  a.e.) convergence of $\chi_n$ including $|\xi|=K$; the two-sided comparison
  $1_{|\xi|>K}$ vs the heat weight.
- Lost steps/qualifiers: none. Pre-existing/contextual: strong continuity of
  translations is re-proved from the multiplier description; compactness at fixed
  $R$ is inherited, not re-derived here.

## L:uniform-mean-tensor

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (adds outline, two step headers, one paragraph
  of explanation)
- New explanations: JUSTIFIED
- Original-step coverage:
  1. Gaussian moment bound. For $v=\sum_{j\le n}f_j\otimes e_j$ orthonormal $(e_j)$,
     $\|v\|^2=\sum_j\|f_j\|^2$. $X=\sum_j\gamma_jf_j$ has $\|X\|^2=\sum_\ell
     \lambda_\ell\zeta_\ell^2$ with $\lambda_\ell$ the Gram eigenvalues,
     $L=\sum_\ell\lambda_\ell=\sum_j\|f_j\|^2$. Since $r/2\ge1$, Jensen with weights
     $(\lambda_\ell/L)$ gives $(\sum_\ell(\lambda_\ell/L)\zeta_\ell^2)^{r/2}\le
     \sum_\ell(\lambda_\ell/L)|\zeta_\ell|^r$, so $\E\|X\|^r\le L^{r/2}\cdot
     m_r\sum_\ell\lambda_\ell/L=m_r(\sum_j\|f_j\|^2)^{r/2}$; $L=0$ is immediate.
  2. Scalar moments + Tonelli. $\sum_j\gamma_jAf_j(t)$ has variance $\sum_j|Af_j(t)|^2$,
     $r$-th moment $m_r(\sum_j|Af_j|^2)^{r/2}$; integrating,
     $m_r\int_I(\sum_j|Af_j(t)|^2)^{r/2}dt=\E\|A\sum_j\gamma_jf_j\|_{L^r}^r\le
     \|A\|^r m_r(\sum_j\|f_j\|^2)^{r/2}$. Cancel finite $m_r>0$, take $r$-th roots:
     $\|\sum_j(Af_j)\otimes e_j\|_{L^r(I;G)}\le\|A\|\|v\|$ (the image has $G$-norm
     $(\sum_j|Af_j(t)|^2)^{1/2}$, the standard ONB picture). Density of finite tensors
     + Bochner completeness extend to $H_0\otimes G$; zero space trivial. The NEW
     paragraph (identical $m_r$ on both sides, “no dimension-dependent factor”) is
     accurate.
  3. Noncompactness counterexample. If $Af\neq0$ and $(e_j)$ is an infinite ONB of
     $G$, then $\|(Af)\otimes(e_j-e_k)\|_{L^r(I;G)}=\sqrt2\|Af\|_{L^r}>0$ for $j\neq
     k$; the images of the bounded sequence $f\otimes e_j$ admit no convergent
     subsequence even when $A$ is compact. This covers “compact scalar time map
     tensored with an infinite identity need not be compact.”
- Evidence: the convexity/Jensen computation for $r/2\ge1$; $\text{trace}(Gram)=\sum_j
  \|f_j\|^2$; exact cancellation of $m_r$; pairwise distance $\sqrt2\|Af\|$.
- Lost steps/qualifiers: none. The boundedness direction uses only $2\le r<\infty$
  (so $r/2\ge1$); the zero-space/$L=0$ cases are handled.

## P:uniform-mean-regulator

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (adds outline and two step headers)
- New explanations: JUSTIFIED
- Original-step coverage:
  1. Tensor projections: $\pi_J\otimes P_K$ selfadjoint/idempotent/contractive on
     finite tensors, hence on the Hilbert completion; hence
     $Q_{J,K}=I-\pi_J\otimes P_K$ is a real orthogonal projection.
  2. Scalar tail $\varepsilon_J\to0$. If not, unit $v_J$ with
     $\|C_t(I-\pi_J)v_J\|_{L^r}$ bounded below on a subsequence; but
     $(I-\pi_J)v_J\rightharpoonup0$ (pairing with $h$ is bounded by
     $\|(I-\pi_J)h\|$), and $C_t$ compact (P:cameron-temporal-map,
     $2<r<2/a$) maps weakly convergent to strongly convergent; the norm limit is $0$
     (every bounded linear observable vanishes on it), contradicting the lower bound.
     The tensor lemma transfers this scalar tail to $L^r(I;H_{\rm sp})$ without a
     dimension factor, since
     $\|(C_t(I-\pi_J))\otimes I\|_{H_t\otimes H_{\rm sp}\to L^r(I;H_{\rm sp})}\le
     \varepsilon_J$.
  3. First bound. $\|\mathcal T_R\|=\|T_R U\|\le\|T_R\|\|U\|\le M_0c_t$ using
     (E:uniform-spatial-mean), $U=C_t\otimes I$, and the tensor lemma for
     $\|U\|\le c_t$.
  4. Exact two-term decomposition. $Q_{J,K}=(I-\pi_J)\otimes I+\pi_J\otimes(I-P_K)$
     (add/subtract $\pi_J\otimes I$). First term: $U((I-\pi_J)\otimes I)=
     (C_t(I-\pi_J))\otimes I$, then $T_R$ pointwise $\le M_0$ norm, giving
     $M_0\varepsilon_J$. Second term: the intertwining
     $U(\pi_J\otimes(I-P_K))=(I_{L^r}\otimes(I-P_K))(C_t\pi_J\otimes I)$ holds on
     finite tensors then by continuity; applying (E:uniform-mean-frequency) pointwise
     ($\|T_R(I-P_K)\|\le M_fK^{-\beta}$) and the tensor lemma for $C_t\pi_J$ (norm
     $\le c_t$) gives $M_fc_tK^{-\beta}$.
  5. Measurability/compact values: for fixed $R$, $T_R$ bounded into the separable
     $\mathcal K(E)$; composition with the Bochner field $U\Phi$ (from
     P:cameron-full-mean) yields the strongly measurable $L^r(I;\mathcal K(E))$
     field. Compact values are retained; uniform-radius compactness is explicitly
     disclaimed.
- Evidence: the identity $Q_{J,K}=(I-\pi_J)\otimes I+\pi_J\otimes(I-P_K)$ is checked
  by expansion; the intertwining is the definition of tensor composition;
  $C_t\pi_J$ norm bound via the tensor lemma.
- Lost steps/qualifiers: none. The two additive constants $M_0\varepsilon_J$ and
  $M_fc_tK^{-\beta}$ are both retained exactly; one fixed $r$ is used throughout.

## P:uniform-actual-cameron

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED (adds outline, five step headers, one
  explanatory paragraph in Step 4)
- New explanations: JUSTIFIED
- Original-step coverage:
  1. Residual paths (Step 1). $Y_m(f)=W(Q_{\rm full}T_{\delta,m}f)$;
     $\operatorname{Var}Y_m(f)=\|Q_{\rm full}T_{\delta,m}f\|_{H_W}^2\le
     \|T_{\delta,m}f\|^2=\|f\|_{H_{\rm fast}}^2$ (pullback isometry of $T_{\delta,m}$,
     L:raw-block-inputs). Gaussian transfer (P:source-gaussian-transfer, with $C=1$)
     gives centered Gaussian operator paths on the given $W$, finite path moments at
     fixed $R,B,\delta,J,K$. Admissible exponent above $\theta$ (L:cameron-actual-
     residual) and constant stopping place them in the separable little $C^\theta$
     closure; first-chaos membership of every continuous linear coordinate is from
     finite-coefficient $L^2$ limits.
  2. Covariance direction (Step 2). Supported rows pull back into $H_I$; for such a
     row $k$ (so $T_{\delta,m}k\in H_I$), decomposing $H_W=H_I\oplus H_I^\perp$ and
     using
     $Q_{\rm full}=i_IQ_{J,K}i_I^*+P_{H_I^\perp}$ gives
     $\langle Q_{\rm full}T_{\delta,m}k,h\rangle=\langle T_{\delta,m}k,i_IQ_{J,K}
     i_I^*h\rangle$; the $H_I^\perp$ directions drop out. Applying the completed
     $J=0$ covariance identity (P:cameron-actual-embedding, linear in the projected
     control, valid for the projection $Q_{J,K}$ and the $E$-restricted mean) yields
     (E:uniform-actual-covariance). Amplitude: $g_\delta\delta^{a/2}=
     \delta^{(1-a)/2+a/2}=\sqrt\delta$. $S_F(v)$ preserves the $E$ copy and restricts
     to $S_E(v)$; $\mathcal T_R$ is the restriction of the mean. Conjugation
     $S_E(-v)AS_E(v)$ is norm-continuous in compact $A$, giving a compact-operator
     Bochner integral.
  3. Free-group constants (Step 3). In Bessel-unitary coordinates the Fourier matrix
     is $\begin{pmatrix}\cos(v|\xi|)&\langle\xi\rangle\sin(v|\xi|)/|\xi|\cr
     -|\xi|\sin(v|\xi|)/\langle\xi\rangle&\cos(v|\xi|)\end{pmatrix}$. For $|v|\le B$,
     $B\ge1$: the upper entry is $\le\sqrt2B$ ($|\sin(vk)|\le Bk$ for $k\le1$,
     $\langle k\rangle/k\le\sqrt2$ for $k\ge1$); the lower entry is $\le1$; both
     diagonals $\le1$; the zero limit of the sine quotient is $v$. Frobenius:
     $\le\sqrt{2+2B^2+1}=\sqrt{3+2B^2}\le3B$, so $G_{B,E}\le3B$.
  4. Primitive bound. With $\mathcal M_h(t)=\mathcal T_R(Q_{J,K}i_I^*h)(t)$ and
     $t_m=\|\mathcal M_h\|_{L^r(I_m;\mathcal L(E))}$: on $[0,B]$ the primitive of the
     conjugated field satisfies, by the Hölder primitive estimate and the affine
     change of variables ($\|\mathcal M_h(s_m+\delta v)\|_{L^r(0,\ell_m)}=
     \delta^{-1/r}t_m$),
     $\|(Lh)_m\|_{C^\theta}\le\sqrt\delta\,G_{B,E}^2[B^{1-1/r}+B^{1-1/r-\theta}]
     \delta^{-1/r}t_m=\sqrt\delta\,C_{B,E}\delta^{-1/r}t_m$. The exponent
     $1-1/r>\theta$ comes from $r>1/(1-\theta)$; constant stopping preserves the
     bound; an empty last block contributes zero. Then
     $C_{B,E}\le9B^2\cdot2B^{1-1/r}=18B^{3-1/r}$ ($B\ge1$, so
     $B^{1-1/r-\theta}\le B^{1-1/r}$). The NEW explanation of this is correct.
  5. Block weighting (Step 4). $n=N+1\ge2$; power mean at exponent $r/p>1$ (valid
     since $r>2>p$) gives $(\sum_m t_m^p)^{1/p}\le n^{1/p-1/r}(\sum_mt_m^r)^{1/r}$.
     True partition gives $\sum_m t_m^r=\|\mathcal M_h\|_{L^r(I)}^r$;
     $\delta n=\delta(\lfloor1/(\delta B)\rfloor+1)\le1/B+\delta<2/B$. So
     $\|Lh\|_{\delta,p}\le\sqrt\delta C_{B,E}(\delta n)^{1/p-1/r}\|\mathcal M_h
     \|_{L^r}\le\sqrt\delta C_{B,E}(2/B)^{1/p-1/r}(M_0\varepsilon_J+M_fc_tK^{-\beta})
     \|h\|_{H_W}$, using the regulator bound and $\|i_I^*h\|_{H_I}\le\|h\|_{H_W}$.
     The NEW “power is increasing since $p<r$” sentence matches
     $1/p-1/r>0$.
  6. Minimum-norm Cameron representative (Step 5). First-chaos Cameron identification
     (P:cameron-actual-embedding): $L$ kills $H_{\rm seen}^\perp$, its Cameron space
     is $L(H_{\rm seen})$ with the minimum original-covariance preimage norm, so
     $\|Lh\|_{\rm CM}=\|P_{\rm seen}h\|_{H_W}$. Applying the bound to the minimum-norm
     representative gives exactly the Cameron embedding bound, with no inverse
     covariance and no finite-dimensional density.
- Evidence: pullback-isometry variance bound; exact $g_\delta\delta^{a/2}=\sqrt\delta$
 ; matrix-entry bounds producing $G_{B,E}\le3B$; $\|C_{B,E}\|\le9B^2\cdot2B^{1-1/r}$
  ; $\delta n<2/B$; power-mean exponent arithmetic.
- Lost steps/qualifiers: none. The closing paragraph (verbatim preserved) explicitly
  disclaims what these linear bounds do *not* prove: growing-mask expected residual
  norms, concentration, conditioning/integration over an infinite sum, or a moment
  upper theorem; residual time blocks may remain correlated; the retained head may
  have infinite rank. Spatial constants are $R$-independent while path moments are
  fixed-parameter.

## AUDIT dispositions

- Assigned inventory: 5 proof pairs, all read in both revisions (COMPLETE/COMPLETE).
  Public reconstruction COMPLETE for all five. No PARTIAL/NOT_READ/NOT_RECONSTRUCTED.
- Unchanged cutoff proof reconstructed explicitly; its Peetre/normalization constant
  $M_\sigma=2^{|\sigma|/2}(2\pi)^{-d/2}\int|\widehat\eta(p)|\langle p\rangle^{|\sigma|}
  dp$ re-derived (convolution constant $c_d$, substitution $p=Rq$, $\langle p/R\rangle
  \le\langle p\rangle$).
- E = $H^{1/2}\times H^{-1/2}$ is preserved throughout; the constant columns remain in
  $F\setminus E$ and the uniform claims concern $E$, consistent with the instructions.
- Mask placement unchanged: $k_R(z,w)=(\eta_Rz_1)(\eta_R\Lambda^{-1}w_2)$, so the
  physical mask $m_R=\eta_R^2$ occurs once, after covariance convolution.
- NEW differences are: (i) outline sentences; (ii) step headers; (iii) three
  explanatory paragraphs (constant $4A_sM^2$ in tails; $m_r$ cancellation in tensor;
  power-mean monotonicity in Cameron). Each was checked arithmetically and is correct.
  No statement text, no displayed equation, and no quantifier was altered.
- Application hypotheses of UNASSIGNED upstream inputs were checked where used:
  L:cameron-fractional-products ($s$ real in $(\alpha/4,1/2)$, real $H^s$ factors);
  P:cameron-spatial-map ($E$ restriction, fixed-$R$ compact values);
  P:cameron-temporal-map ($C_t$ compact for $2<r<2/a$); L:cameron-supported-tensor
  ($H_I=H_t\otimes H_{\rm sp}$); L:raw-block-inputs (pullback isometry, amplitude
  $\delta^{a/2}$); P:source-gaussian-transfer (variance bound $\le C\|f\|^2$ with
  $C=1$); L:source-spatial-heat (heat multiplier $e^{-\varepsilon|\xi|^2/2}$,
  variance $\varepsilon$); P:cameron-actual-embedding (completed covariance identity
  applied linearly to $Q_{J,K}$, first-chaos Cameron identification).
  These upstream proofs themselves were not reviewed (by contract).

## Findings and limits

No rewrite defect was detected: the two revisions are deduction-equivalent. The only
facts I must flag are contextual, present in both revisions and inherited from the
unassigned upstream modules: the compactness of $T_R$ (value-wise and as a map) at
fixed $R$ is asserted rather than re-derived here; the block covariance identity's
validity for the enlarged projection $Q_{J,K}$ rests on the linearity of the baseline
covariance computation in the control; and the tail bound $\|T_R(I-P_K)\|$ is a
Fourier-multiplier statement, so its use requires the frequency projection to be
compatible with the mean's row — established by commuting multipliers on the
covariance image $V$. The review covers only the five assigned proof pairs and does
not certify source PDFs, Lean correspondence, rendered pages, upstream analytic
results, or a whole-book theorem. Reading and reconstruction state is COMPLETE for
all five target proofs; this is not a claim that every upstream statement used has
itself been proved here.
