# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro (exact model ID: deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

The NEW revision of all twelve assigned global main ordinals preserves the mathematical argument. The only substantive changes are added proof roadmaps/steps (ordinals 53, 54, 55, 56, 57, 58, 59, 61, 62) and inserted step headings; ordinals 51, 52, 60 have no added headings and are line-shifted identical proofs. The added roadmaps are accurate summaries and introduce no changed hypotheses, constants, limits, or quantifiers. Public reconstruction is COMPLETE for all twelve; in several places the deductions are completed through named UNASSIGNED upstream statements (checked against their hypotheses) rather than by re-proving those upstream statements, which the contract permits. Details follow.

## C:three-product-riesz
- Global main ordinal: 51
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Fix $\vartheta=(\alpha_0+2-\alpha)/2$, $b_0,\chi$ by \eqref{E:three-parameters}. Check $\alpha_0<\vartheta<2-\alpha$: $\vartheta>\alpha_0\iff\alpha+\alpha_0<2$ (true), $\vartheta<2-\alpha\iff\alpha_0<2-\alpha$ (true since $\alpha+\alpha_0<2$).
  2. For the ordinary product, Lemma~\ref{L:product-endpoints} produces exponent vectors $b,v$ with $\sum_j b_j=1$, $\sum_j v_j=\chi$, $a_j=\vartheta b_j+(1-\vartheta)v_j$, and the Gaussian comparison \eqref{E:product-gaussian-comparison} with common amplitude $c$; this is exactly Hypothesis~\ref{H:three-endpoints}.
  3. For Riesz, set $\gamma_1=c|x|^{-1}$, $\gamma_\chi=c|x|^{-\chi}$. For $e\in\{1,\alpha,\chi\}$, $e<3$ (for $\chi$: $\chi<\alpha<2-\alpha_0<2<3$; $2-\chi=(2-\alpha-\vartheta)/(1-\vartheta)>0$), so local integrability and temperedness follow. Positive definiteness follows from the Gaussian mixture
  \[
    c|x|^{-e}=\frac{c}{\Gamma(e/2)}\int_0^\infty s^{e/2-1}e^{-s|x|^2}\,ds,
  \]
  each Gaussian being positive definite.
  4. The affine identity $\vartheta+(1-\vartheta)\chi=\alpha$ gives $\gamma_\alpha=\gamma_1^\vartheta\gamma_\chi^{1-\vartheta}$ a.e. with amplitude $c$. Hölder on $p_\epsilon\,dz$ gives
  \[
    (p_\epsilon*\gamma_\alpha)(z)\le(p_\epsilon*\gamma_1)(z)^\vartheta(p_\epsilon*\gamma_\chi)(z)^{1-\vartheta},
  \]
  which is \eqref{E:three-gaussian-comparison}.
  5. Discharge Hypothesis~\ref{H:three-endpoints}; apply Proposition~\ref{P:three-transfer}.
- Argument preservation: PRESERVED (text identical, shifted).
- New explanations: none added in this proof.
- Evidence: the mixture identity, the affine identity, and the Hölder comparison above are checkable; the constant dependence (only on $a,c,\alpha_0$ resp. $\alpha,c,\alpha_0$) is carried through.
- Lost steps/qualifiers: none. Upstream unassigned inputs: Lemma~\ref{L:product-endpoints}, Hypothesis~\ref{H:three-endpoints}, Proposition~\ref{P:three-transfer} (all present in context; hypotheses checked). Pre-existing concern: the transfer to \eqref{E:three-transfer}/\eqref{E:three-variational-upper} is inherited from the unassigned conditional transfer.

## C:three-finite-images
- Global main ordinal: 52
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Common $\vartheta,b_0,\chi$.
  2. Riesz component endpoints $c_i|x|^{-1}, c_i|x|^{-\chi}$ reuse the mixture/Hölder argument of ordinal 51; product endpoints from Lemma~\ref{L:product-endpoints}; plane-supported endpoints from Lemma~\ref{L:plane-endpoints} with $a_1+a_2=\alpha-1$.
  3. Lemma~\ref{L:endpoint-closure}: comparison pushes forward under invertible $T$ (the factor $|\det T|^{-1}$ in each of target/low/static convolutions cancels in the comparison $p_\epsilon*T_\#J=|\det T|^{-1}(q_\Sigma*J)(T^{-1}x)$), and finite weighted sums obey discrete Hölder
  \[
    \sum_i(w_i l_i)^\vartheta(w_i s_i)^{1-\vartheta}
    \le\Big(\sum_i w_il_i\Big)^\vartheta\Big(\sum_i w_is_i\Big)^{1-\vartheta}.
  \]
  4. Resulting $\Gamma_{\rm low}=\sum_iw_i(T_i)_\#\Gamma_{{\rm low},i}$, $\Gamma_{\rm st}$ analogous satisfy \eqref{E:three-gaussian-comparison}; the target is nonzero because each component is a nonzero nonnegative measure and some $w_i>0$.
  5. Apply Proposition~\ref{P:three-transfer}; no cross-solution coupling used.
- Argument preservation: PRESERVED.
- New explanations: none added.
- Evidence: the pushforward factorization and discrete Hölder are the two substantive identities. Note (as the surrounding text states) endpoint spectral/ variational quantities need not be invariant under nonorthogonal $T$.
- Lost steps/qualifiers: none. Upstream: Lemmas~\ref{L:product-endpoints}, \ref{L:plane-endpoints}, \ref{L:endpoint-closure}, Proposition~\ref{P:three-transfer}.

## L:physical-spectral-energy
- Global main ordinal: 53
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Fourier uniqueness gives $\mu_\Xi(rA)=r^\chi\mu_\Xi(A)$; unit-ball mass finite; Dalang condition via dyadic annuli:
  \[
    \int\frac{\mu_\Xi(d\xi)}{1+|\xi|^2}\le \mu_\Xi(B_1)\Big(1+C_\chi\sum_{j\ge0}2^{j(\chi-2)}\Big)<\infty.
  \]
  2. For Schwartz $h$, $\mathscr E(h)=\int|\widehat h|^2\mu_\Xi$, $Q(f)=\mathscr E(f^2)$; Schwartz pairing identifies $Q(f)$ with the physical integral. The imported Chen finiteness (used only on smooth profiles) gives $Q(g)\le\frac12\|\nabla g\|_2^2+C_0$ for real unit-$L^2$ Schwartz $g$; quartic homogeneity extends to
  \[
    Q(f)=\|f\|_2^4 Q(f/\|f\|_2)\le\frac12\|f\|_2^2\|\nabla f\|_2^2+C_0\|f\|_2^4,
  \]
  and since $\|f\|_2^2\|\nabla f\|_2^2\le N(f)^4/4$, $Q(f)^{1/2}\le D N(f)^2$ with $D=\sqrt{1/8+C_0}$.
  3. Two Cauchy–Schwarz bounds: spectral
  \[
    P(f,h):=\int\Xi(dz)\int f(y+z)^2h(y)^2dy
    =\int\widehat{f^2}\,\overline{\widehat{h^2}}\,\mu_\Xi\le Q(f)^{1/2}Q(h)^{1/2},
  \]
  using $\widehat{\int f^2(\cdot+z)h^2(\cdot)}(\xi)=\widehat{f^2}(\xi)\overline{\widehat{h^2}(\xi)}$; and measure Cauchy–Schwarz
  \[
    \mathscr E(fh)=\int\Xi(dz)\int f(y+z)f(y)h(y+z)h(y)dy\le Q(f)^{1/2}Q(h)^{1/2}.
  \]
  4. For $A_f(y,z)=f(y+z)f(y)$, $B_f=\widehat{f^2}$, the decomposition and the two bounds give
  \[
    \|A_f-A_h\|_{L^2(ydz\,\Xi(dz))},\ \|B_f-B_h\|_{L^2(\mu_\Xi)}
    \le D\big(N(f)+N(h)\big)N(f-h),
  \]
  since $f^2-h^2=(f-h)(f+h)$ and $N(f+h)\le N(f)+N(h)$.
  5. For Schwartz $f_n\to g$ in $W^{1,2}$, both sequences are Cauchy; an a.e.-convergent subsequence and sigma-finite Fubini/translation invariance give $f_n(y+z)f_n(y)\to g(y+z)g(y)$ for $ydz\,\Xi(dz)$-a.e.; hence the strong limit is $A_g$, invariant under the Borel representative. Also $\|f_n^2-g^2\|_1\to0$, so $\widehat{f_n^2}\to\widehat{g^2}$ uniformly; the $L^2(\mu_\Xi)$–a.e. limit coincides, identifying $B_g$. Equality $\|A_{f_n}\|^2=Q(f_n)=\|B_{f_n}\|^2$ passes to the limit, giving \eqref{E:physical-spectral-energy} and \eqref{E:energy-quartic-bound}.
- Argument preservation: PRESERVED. NEW inserts the accurate preamble and Steps 1–4; the body is the same.
- New explanations: JUSTIFIED ("imported finiteness only on smooth profiles"; "two distinct Cauchy–Schwarz bounds"; "identify strong limits").
- Evidence: the two Cauchy–Schwarz pairings, the $D\,N^2$ control, and the a.e. identification are all checkable as above.
- Lost steps/qualifiers: none introduced. Pre-existing/imported: the quantitative bound $Q(g)\le\frac12\|\nabla g\|^2+C_0$ on unit Schwartz profiles is imported from Chen Theorem 1.1 (used only at smooth level, as the new preamble emphasizes).

## L:mean-coefficient-holder
- Global main ordinal: 54
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Static endpoint: at positive widths the static terms are the bounded-variance Bochner integrals of Lemma~\ref{L:terminal-wick} with time-constant field; Lemma~\ref{L:spatial-wick-measures} (multiplier one) gives a diagram limit; the Hilbert-Cauchy argument of Lemma~\ref{L:joint-fixed-order} gives static fixed-order $X_n^{(0)}$.
  2. Static norm series: with $b_0\in(0,a_{\max})$, $\delta_0>0$, $c=\gamma^0_{\delta_0,b_0}(1)>0$ and $\gamma^0_{\delta_0,b_0}(s-r')\ge c$ on $[0,1]^2$, every static pair factor $1$ is dominated by $(r/\sqrt c)^2\gamma^0_{\delta_0,b_0}\ge r^2$, whence $\E|U_N^\epsilon(r;1,x)|^2\le \E|u^{\epsilon,\delta_0}_{b_0}(r/\sqrt c;1,x)|^2\le B_{b_0}(1;r/\sqrt c)$, uniformly in $N,\epsilon$ (positivity and \eqref{E:regularized-scaled-moment}). Sending $N\to\infty$ and applying Lemma~\ref{L:uniform-series-tail} gives geometric coefficient bounds at every $r>1$; homogeneity
  \[
    \|X_n^{(0)}(t,x)\|_2=t^{(4-\alpha)n/2}\|X_n^{(0)}(1,0)\|_2
  \]
  with $r>t^{(4-\alpha)/2}$ proves norm summability at every $t>0$.
  3. Interpolation at fixed width: with $\omega_{\epsilon,D}$ finite positive spatial Green–Wick measures and
  \[
    m_k^\epsilon(a)=\sum_{D\in\Pi_k}\int\prod_{\{j,h\}\in D}|s_j-s_h|^{-a}\,d\omega_{\epsilon,D},
  \]
  the identity $|s_j-s_h|^{-a}=(|s_j-s_h|^{-b})^{a/b}$ and Hölder on the disjoint union $\Omega=\sqcup_D\omega_{\epsilon,D}$ give
  \[
    \int_\Omega\varphi_b^{a/b}\cdot1\,d\Omega
    \le\Big(\int_\Omega\varphi_b\,d\Omega\Big)^{a/b}\Big(\int_\Omega1\,d\Omega\Big)^{1-a/b}
    =m_k^\epsilon(b)^{a/b}m_k^\epsilon(0)^{1-a/b}.
  \]
  4. Width removal: \eqref{E:joint-temporal-tail} gives $F_{\epsilon,\eta,D}\le F_{\epsilon,0,D}\le F_{\epsilon,\eta,D}+r_a(\eta)$ uniformly in $\epsilon$, so the spatial limit at fixed $\eta$ followed by $\eta\to0$ identifies the joint diagram value; at $a=0$ Lemma~\ref{L:spatial-wick-measures} gives the limit directly. Hence $m_k^\epsilon(a)\to m_k(a)$ at $0,a,b$; nonnegativity follows.
  5. Homogeneity and series: scaling all times/displacements by $t$ changes width to $\epsilon/t^2$ and gives factor $t^{2(2k)-\alpha k-ak}=t^{\beta(a)k}$; odd means vanish by Wick; the mean-series interchange uses Lemma~\ref{L:vertex-crude} ($a>0$) and the static norm series ($a=0$). Since $\beta(a)>0$ every $z\ge0$ equals $t^{\beta(a)}$, so $F_a(z)=\sum m_k(a)z^k<\infty$.
- Argument preservation: PRESERVED. NEW adds preamble and Steps 1–4; body unchanged.
- New explanations: JUSTIFIED.
- Evidence: $\beta(a)=4-\alpha-a$; the Hölder–disjoint-union computation; the sandwich $F_{\epsilon,\eta,D}\le F_{\epsilon,0,D}\le F_{\epsilon,\eta,D}+r_a(\eta)$; the scaling exponent $4k-\alpha k-ak$.
- Lost steps/qualifiers: none introduced. Upstream: Lemmas~\ref{L:terminal-wick}, \ref{L:spatial-wick-measures}, \ref{L:joint-fixed-order}, \ref{L:uniform-series-tail}, \ref{L:vertex-crude}, Proposition~\ref{P:mixed}, \eqref{E:regularized-scaled-moment}, and the imported static heat-limit convention for Chen–Hu.

## L:positive-series-type
- Global main ordinal: 55
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Forward direction: $L>\tau$ gives $F(z)\le C_Le^{Lz^{1/\nu}}$ on $[0,\infty)$ (uniform bound on compact sets + tail estimate). At $z=(\nu k/L)^\nu$, $c_kz^k\le F(z)$, so
  \[
    c_k\le C_Le^{\nu k}\Big(\frac{L}{\nu k}\Big)^{\nu k}.
  \]
  The two-sided Stirling-type bound $k\log k-k+1\le\log(k!)\le k\log k-k+1+\log k$ gives $(k!)^{1/k}=ke^{-1+o(1)}$, and inserting it into $((k!)^\nu c_k)^{1/k}$ cancels the $e^{\nu}$ exactly, yielding $K\le(L/\nu)^\nu$. Then $L\downarrow\tau$ gives $K\le(\tau/\nu)^\nu$ (so also $\tau\ge\nu K^{1/\nu}$).
  2. Converse: for $A>K$, eventually $c_k\le A^k/(k!)^\nu$, so $F(z)\le P(z)+\sum_k(Az)^k/(k!)^\nu\le P(z)+\exp\{\nu(Az)^{1/\nu}\}$ by the $\ell^\nu$ bound with $a_k=(Az)^{k/\nu}/k!$; the polynomial contributes $0$ to normalized growth, so $\tau\le\nu A^{1/\nu}$, and $A\downarrow K$ gives $\tau\le\nu K^{1/\nu}$. Equality follows.
- Argument preservation: PRESERVED. NEW adds preamble and Steps 1–2.
- New explanations: JUSTIFIED (the preamble correctly separates forward coefficient-type from the exponential majorant).
- Evidence: the cancellation using the refined Stirling bound is the key checkable step; the $\ell^\nu$ estimate $\sum_k a_k^\nu\le(\sum_k a_k)^\nu$ is explicit.
- Lost steps/qualifiers: none. $\nu\ge1$ and $c_0=1$ (so $\tau\ge0$) are used as stated.

## P:static-minorant-lower
- Global main ordinal: 56
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. On $[0,T]^2$, $\gamma^0_{\delta,a}(s-r)\ge c_{\delta,T}:=\gamma^0_{\delta,a}(T)>0$, and $c_{\delta,T}\to T^{-a}$ as $\delta\downarrow0$. Since each regularized temporal factor dominates the static constant $c_{\delta,T}$ and the spatial factor $\gamma_{2\epsilon}$ is shared, the order-$N$ finite Wick sums satisfy $\E|U_N^{(a),\epsilon,\delta}|^2\ge\E|U_{N,\sigma=c_{\delta,T}^{1/2}}^{(0),\epsilon}|^2$, and likewise for the mean.
  2. At fixed $N$, the joint limit $(\epsilon,\delta)\to0$ uses Lemma~\ref{L:joint-fixed-order} ($a>0$) and static fixed-order $L^2$ convergence; $c_{\delta,T}\to T^{-a}$ is a finite polynomial at fixed order. So the limiting static model has amplitude $\sigma=T^{-a/2}$.
  3. Static homogeneity $\sigma^n\|X_n^{(0)}(T,x)\|_2=\|X_n^{(0)}(\sigma^{2/(4-\alpha)}T,x)\|_2$ (checked via $t^{(4-\alpha)n/2}$ scaling) makes the amplitude-scaled static series summable at the effective time; Lemma~\ref{L:mean-coefficient-holder} supplies the static $L^2$ expansion. Sending $N\to\infty$ in both $L^2$ expansions preserves the inequality.
  4. Exact moment identity: for $p=1,2$, total order $2k$ carries $\sigma^{2k}$ and time factor $T^{(4-\alpha)k}$, so the regrouping of the nonnegative double series gives
  \[
    \E[U_\sigma(T,x)^p]=\E[U(\sigma^{2/(4-\alpha)}T,x)^p].
  \]
  At $\sigma=T^{-a/2}$ the effective time is $T^{1-a/(4-\alpha)}$. Finally
  \[
    \big(T^{1-a/(4-\alpha)}\big)^{\kappa_{\rm st}}
    =T^{(4-\alpha)(1-a/(4-\alpha))/\nu}=T^{(4-\alpha-a)/\nu}=T^{\kappa(a)},
  \]
  so \eqref{E:static-ratio-input} gives $\liminf T^{-\kappa(a)}\log\E[u^{(a)}(T,x)^p]\ge p^{\kappa_{\rm st}}L_0$.
- Argument preservation: PRESERVED. NEW adds preamble and Steps 1–3.
- New explanations: JUSTIFIED.
- Evidence: $\gamma^0_{\delta,a}(T)\to T^{-a}$ (Laplace-cutoff completeness); the $\sigma^{2/(4-\alpha)}$ clock; the exponent identity. Assigned dependency: Lemma~\ref{L:mean-coefficient-holder} (ordinal 54) is re-derived above.
- Lost steps/qualifiers: none; the argument is only for moments $p\in\{1,2\}$ (as stated).

## P:near-static-mean-gap
- Global main ordinal: 57
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Type identification: $F_a(T^{\beta(a)})=\sum m_k(a)T^{\beta(a)k}=\E u^{(a)}(T,x)$; since $z^{1/\nu}=T^{\beta(a)/\nu}=T^{\kappa(a)}$, the normalized type of $F_a$ equals $M(a)$, and at $a=0$ it is $L_0$. Lemma~\ref{L:positive-series-type} gives $K(a)=(\tau_a/\nu)^\nu$, so $K(0)=(L_0/\nu)^\nu>0$.
  2. $K(b)<\infty$: Cauchy–Schwarz gives $\E u\le(\E u^2)^{1/2}$, so $M(b)\le\frac12\limsup_t t^{-\kappa(b)}\log\E[u^{(b)2}]<\infty$ by Theorem~\ref{T:full-upper}; type transfer gives $K(b)<\infty$.
  3. Multiplying \eqref{E:mean-coefficient-holder} by $(k!)^\nu$, taking $k$th roots and limsup (with the $\eta$-regularization for zero coefficients) gives
  \[
    K(a)\le K(0)^{1-a/b}K(b)^{a/b}\le K(0)^{1-a/b}B_b^{a/b}.
  \]
  Then $M(a)=\nu K(a)^{1/\nu}\le\nu K(0)^{1/\nu}(B_b/K(0))^{a/(b\nu)}=L_0(B_b/K(0))^{a/(b\nu)}$.
  4. Window: $B_b/K(0)\ge2$ so $a_*=b\log2/\log(B_b/K(0))\in(0,b]$; for $a<a_*$, $(B_b/K(0))^{a/(b\nu)}<2^{1/\nu}$, hence $2M(a)<2L_0 2^{1/\nu}=2^{1+1/\nu}L_0=2^{\kappa_{\rm st}}L_0$ (using $\kappa_{\rm st}=1+1/\nu$). Proposition~\ref{P:static-minorant-lower} at $p=2$ then gives strict inequality.
- Argument preservation: PRESERVED. NEW adds preamble and Steps 1–2.
- New explanations: JUSTIFIED.
- Evidence: $K=(L_0/\nu)^\nu$; the geometric-mean upper rate; the strict gap $2M(a)<2^{\kappa_{\rm st}}L_0$.
- Lost steps/qualifiers: none introduced. Assigned inputs re-derived: ordinals 54, 55, 56; unassigned input: Theorem~\ref{T:full-upper}.

## L:full-moment-coefficient-holder
- Global main ordinal: 58
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Common measures: $\omega_{\epsilon,m,n,D}$ finite positive Green–Wick measures (initial-chain convention, $\gamma_{2\epsilon}$); $p=1$ uses only the split $(0,2k)$; $p=2$ uses all $m=0,\dots,2k$, keeping both empty-chain orientations; Wick coefficient one per pairing per ordered domain.
  2. Interpolation: on the disjoint union
  \[
    c^\epsilon_{p,k}(a)=\int\prod_{\{j,h\}}\!|s_j-s_h|^{-a}\,d\omega_{\epsilon,p,k},
  \]
  with $a=(1-\theta)a_1+\theta a_2$, the multiplier equals $f^{1-\theta}g^\theta$ off null diagonals, so Hölder gives $c^\epsilon_{p,k}(a)\le c^\epsilon_{p,k}(a_1)^{1-\theta}c^\epsilon_{p,k}(a_2)^\theta$.
  3. Limits: the common temporal-cutoff sandwich and \eqref{E:joint-temporal-tail} identify each fixed positive-endpoint spatial limit with the joint diagram value (all splits, including empty/unequal); $a=0$ uses Lemma~\ref{L:spatial-wick-measures}; static diagonal/mixed-width Gaussian limits and the Proposition~\ref{P:mixed} chain reversal identify diagram values with the static split expectations.
  4. Homogeneity and series: each diagram has $2k$ time Jacobians, $2k$ Green scalings, $k$ spatial and $k$ temporal covariance factors, so degree $4k-\alpha k-ak=\beta(a)k$; positive $a$ series from Proposition~\ref{P:mixed} (second moment) and \eqref{E:mean-positive-series} (mean); $a=0$ from the static norm series; regrouping the nonnegative double series by total order gives \eqref{E:full-moment-positive-series}.
- Argument preservation: PRESERVED. NEW adds preamble and Steps 1–4.
- New explanations: JUSTIFIED.
- Evidence: the Hölder interpolation and the homogeneity degree $4k-\alpha k-ak$ are the checkable computations.
- Lost steps/qualifiers: none introduced. Upstream: Proposition~\ref{P:mixed}, Lemma~\ref{L:spatial-wick-measures}, \eqref{E:joint-temporal-tail}; assigned input \eqref{E:mean-positive-series} (ordinal 54) re-derived.

## P:moment-growth-logconvex
- Global main ordinal: 59
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Positivity/finiteness: $C_p=p^{\kappa_{\rm st}}L_0>0$; \eqref{E:static-ratio-input} gives $\overline\Lambda_p(0)=\underline\Lambda_p(0)=C_p$; Proposition~\ref{P:static-minorant-lower} gives $\underline\Lambda_p(a)\ge C_p$; the full upper bound gives finiteness for $p=2$ and Cauchy–Schwarz for $p=1$ (whose mean is $\ge1$). All logarithms well defined.
  2. Type transfer: $F_{p,a}(z)=\sum c_{p,k}(a)z^k$ is entire; with $z=T^{\beta(a)}$, $(z^{1/\nu}=T^{\kappa(a)})$ its type equals $\overline\Lambda_p(a)$, so Lemma~\ref{L:positive-series-type} gives $K_p(a)=(\overline\Lambda_p(a)/\nu)^\nu$. Multiplying \eqref{E:full-moment-coefficient-holder} by $(k!)^\nu$, roots/limsup give $K_p(a)\le K_p(a_1)^{1-\theta}K_p(a_2)^\theta$; raising to $1/\nu$ and multiplying by $\nu$ gives
  \[
    \overline\Lambda_p(a)\le\overline\Lambda_p(a_1)^{1-\theta}\overline\Lambda_p(a_2)^\theta.
  \]
  3. Continuity: for $f=\log\overline\Lambda_p$, convexity's secant bound
  \[
    \frac{f(l)-f(L)}{l-L}\le\frac{f(y)-f(x)}{y-x}\le\frac{f(R)-f(r)}{R-r}
  \]
  bounds the difference quotient on each compact subinterval, giving local Lipschitz continuity of $f$ (finite convex on an open interval), hence continuity of $\overline\Lambda_p$.
- Argument preservation: PRESERVED. NEW adds preamble and Steps 1–3.
- New explanations: JUSTIFIED.
- Evidence: $K_p(a)=(\overline\Lambda_p(a)/\nu)^\nu$; the weighted-geometric mean of types; secant-slope continuity.
- Lost steps/qualifiers: none introduced; the continuity assertion is only for the upper rate on the open interval (matching the remark).

## C:static-moment-constant-continuity
- Global main ordinal: 60
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Lower bound $C_p\le\underline\Lambda_p(a)$ is Proposition~\ref{P:static-minorant-lower}.
  2. Upper: Proposition~\ref{P:moment-growth-logconvex} with endpoints $(0,b)$ and $\theta=a/b$ gives
  \[
    \overline\Lambda_p(a)\le C_p^{1-a/b}\overline\Lambda_p(b)^{a/b}
    =C_p\Big(\frac{\overline\Lambda_p(b)}{C_p}\Big)^{a/b},
  \]
  proving \eqref{E:static-constant-envelope}.
  3. The finite ratio $\overline\Lambda_p(b)/C_p\ge1$; its $a/b$ power tends to 1 with $b$ fixed, squeezing both rates to $C_p$.
  4. Ratio: numerator $\underline\Lambda_2(a)\to2^{\kappa_{\rm st}}L_0$, denominator $\overline\Lambda_1(a)\to L_0>0$; division gives $2^{\kappa_{\rm st}}$.
- Argument preservation: PRESERVED (unchanged).
- New explanations: none added.
- Evidence: $C_p(ratio)^{a/b}\to C_p$; the limit ratio $(2^{\kappa_{\rm st}}L_0)/L_0$.
- Lost steps/qualifiers: none. This is an iterated limit (time limits at fixed $a$, then $a\downarrow0$); the surrounding remark makes this explicit and is retained.

## L:white-clock-laplace
- Global main ordinal: 61
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Cross spatial factor: $\int G_s(y)G_t(z)\delta_0(y-z)dydz=\frac14\int\mathbf1_{\{|y|<s\wedge t\}}dy=\frac{\min(s,t)}2$ (using $G_s=\frac12\mathbf1_{\{|y|<s\}}$ in $d=1$).
  2. Split into $s=t+v$ and $t=s+v$ ($v>0$). For $s=t+v$: integrand $\frac12 t e^{-(\theta_1+\theta_2)t}e^{-\theta_1 v}v^{-a}$; separates by Tonelli into
  \[
    \tfrac12\Big(\int_0^\infty te^{-(\theta_1+\theta_2)t}dt\Big)\Big(\int_0^\infty e^{-\theta_1v}v^{-a}dv\Big)
    =\tfrac12(\theta_1+\theta_2)^{-2}\Gamma_E(1-a)\theta_1^{a-1};
  \]
  the other cone contributes $\theta_2$, giving
  \[
    K_\times=\frac{\Gamma_E(1-a)}{2(\theta_1+\theta_2)^2}\big(\theta_1^{a-1}+\theta_2^{a-1}\big),
  \]
  and at $\theta_1=\theta_2=\theta$, $K_\times=\Gamma_E(1-a)/(4\theta^{3-a})$.
  3. Self-pair: delta covariance forces equal positions; $G_{r_2}(0)=1/2$, first Green mass $r_1$; hence
  \[
    K_{\rm self}=\frac12\Big(\int_0^\infty e^{-\eta_1r_1}r_1dr_1\Big)\Big(\int_0^\infty e^{-\eta_2r_2}r_2^{-a}dr_2\Big)
    =\frac{\Gamma_E(1-a)}{2\eta_1^2\eta_2^{1-a}}.
  \]
- Argument preservation: PRESERVED. NEW adds preamble and Steps 1–2.
- New explanations: JUSTIFIED.
- Evidence: both Laplace integrals evaluate directly; $a<1$ makes $\int e^{-\theta v}v^{-a}dv=\Gamma_E(1-a)\theta^{a-1}$ finite.
- Lost steps/qualifiers: none.

## P:clock-copy-obstruction
- Global main ordinal: 62
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Cross transform: smoothing makes Fubini absolute. For the first cone $s=t+v$, the $v$-integral is
  \[
    \int_0^\infty e^{-(\theta+\lambda)v}\sin(r(t+v))dv
    =\frac{(\theta+\lambda)\sin(rt)+r\cos(rt)}{(\theta+\lambda)^2+r^2}.
  \]
  Using $\int_0^\infty e^{-2\theta t}\sin^2(rt)dt=r^2/(4\theta(\theta^2+r^2))$ and $\int e^{-2\theta t}\sin(rt)\cos(rt)dt=r/(4(\theta^2+r^2))$, the first cone plus its mirror gives
  \[
    \iint e^{-\theta(s+t)-\lambda|s-t|}\widehat G_s\overline{\widehat G_t}\,dsdt
    =\frac{2\theta+\lambda}{2\theta(\theta^2+r^2)((\theta+\lambda)^2+r^2)}.
  \]
  2. Laplace formula $|s-t|^{-a}=\Gamma_E(a)^{-1}\int\lambda^{a-1}e^{-\lambda|s-t|}d\lambda$ and monotone convergence (removing the spatial Gaussian multiplier, justified by nonnegativity and Lemma~\ref{L:damped-homogeneous-norms}) give
  \[
    K_\Gamma(\theta)=\frac1{\Gamma_E(a)}\int_0^\infty\lambda^{a-1}\frac{2\theta+\lambda}{2\theta}
    \int\frac{\mu(d\xi)}{(\theta^2+|\xi|^2)((\theta+\lambda)^2+|\xi|^2)}d\lambda.
  \]
  Partial fractions with $(\theta+\lambda)^2-\theta^2=\lambda(2\theta+\lambda)$ convert this to
  \[
    K_\Gamma(\theta)=\int_0^\infty w_\theta(\lambda)d\lambda,\qquad
    w_\theta(\lambda)=\frac{\lambda^{a-2}}{2\theta\Gamma_E(a)}\big(\mathcal R_\Gamma(\theta)-\mathcal R_\Gamma(\theta+\lambda)\big).
  \]
  Positivity of $w_\theta$ comes from strict monotonicity of $\mathcal R_\Gamma$ under $\mu\ne0$; integrability from $\lambda^{a-1}$ near $0$ and $\lambda^{a-2}$ at $\infty$.
  3. Candidate integrability: $\Psi_a(\theta|u-v|,v_\rho)\le(\theta|u-v|)^{-a}$ and $h_\Gamma(w)=h_\Gamma(1)w^{-\alpha/2}$; with $w=u+v$, $q=u-v$ (Jacobian $1/2$), the majorant is
  \[
    \frac{2}{1-a}\int_0^\infty e^{-\theta^2w/2}w^{1-\alpha/2-a}dw<\infty
  \]
  because $a<1$ and $a+\alpha/2<2$; the same bound dominates heat-regularized averages via $h_\Gamma(w+2\epsilon)\le h_\Gamma(w)$. Since $v_\rho(u,v)\ge|u-v|=v_1(u,v)$ and $\Psi_a$ decreases in $v$, $J_{\Gamma,\rho}\le J_{\Gamma,1}$.
  4. Evaluation of $J_{\Gamma,1}$: $A=\theta\lambda+\lambda^2/2$; the $q$-integral is $2(1-e^{-Aw})/A$; the resolvent identity $\mathcal R_\Gamma(q)=\frac12\int_0^\infty e^{-q^2w/2}h_\Gamma(w)dw$ yields
  \[
    J_{\Gamma,1}(\theta)=\int_0^\infty\frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)d\lambda.
  \]
  Since $w_\theta>0$ and $2\theta/(2\theta+\lambda)<1$ for every $\lambda>0$, $0<J_{\Gamma,\rho}\le J_{\Gamma,1}<K_\Gamma(\theta)$.
  5. Degree one: $\mathcal R_\Gamma(q)=\mathcal R_\Gamma(1)/q$ gives
  \[
    K_\Gamma(\theta)=\frac{\mathcal R_\Gamma(1)}{2\theta^2\Gamma_E(a)}\int_0^\infty\frac{\lambda^{a-1}}{\theta+\lambda}d\lambda,\qquad
    J_{\Gamma,1}(\theta)=\frac{\mathcal R_\Gamma(1)}{\theta^2\Gamma_E(a)}\int_0^\infty\lambda^{a-1}\Big(\frac1{\theta+\lambda}-\frac1{2\theta+\lambda}\Big)d\lambda.
  \]
  The beta identity $\int_0^\infty x^{a-1}/(x+c)dx=c^{a-1}\Gamma_E(a)\Gamma_E(1-a)$ gives
  \[
    \frac{J_{\Gamma,1}}{K_\Gamma}=2(1-2^{a-1})=2-2^a,
  \]
  hence \eqref{E:degree-one-clock-loss}.
- Argument preservation: PRESERVED. NEW adds preamble and Steps 1–5.
- New explanations: JUSTIFIED (the preamble correctly delimits that the proposition concerns exactly the direct unweighted constant-correlation candidate).
- Evidence: the cone identity for the wave Fourier kernels; the partial-fraction reduction; the shared-clock density $2\theta/(2\theta+\lambda)w_\theta$; the beta evaluation. Consistency check for the white case: in $d=\alpha=1$, $\mu(d\xi)=d\xi/(2\pi)$, $\mathcal R_\Gamma(1)=1/2$, and $K_\Gamma(\theta)=\Gamma_E(1-a)/(4\theta^{3-a})=K_\times(\theta,\theta)$ of ordinal 61, as required.
- Lost steps/qualifiers: none introduced. The surrounding remark retains the restricted scope (no claim over general two-clock, order-weighted, matrix, modulus, or Skorohod representations; no correction rule at higher orders), which is preserved unchanged. Upstream input: finiteness of $N_2(\theta)^2$ from Lemma~\ref{L:damped-homogeneous-norms}.

## Findings and limits

All twelve assigned ordinals (51–62) were read explicitly in both OLD and NEW; no reading was inferred from hashes or line matches. Public reconstruction is COMPLETE for all twelve. Argument preservation is PRESERVED for all twelve: the NEW texts for 51, 52, and 60 are verbatim (line-shifted); the NEW texts for 53, 54, 55, 56, 57, 58, 59, 61, 62 add only accurate proof roadmaps and step headings, with no change to statements, hypotheses, constants, or limit orders. All added roadmaps are JUSTIFIED.

The main cross-referenced assigned arguments were re-derived rather than taken as oracles: ordinal 56 uses ordinal 54 (static norm-series construction and homogeneity), ordinals 57 and 59 use 54/55/56, ordinal 58 uses 54, ordinal 60 uses 56/59; each was reconstructed in its own section. Named UNASSIGNED upstream inputs used inside the assigned proofs include: Lemmas~\ref{L:product-endpoints}, \ref{L:endpoint-closure}, \ref{L:plane-endpoints}, Hypothesis~\ref{H:three-endpoints}, Proposition~\ref{P:three-transfer} (ordinals 51–52); the imported Chen finiteness (ordinal 53); Lemmas~\ref{L:terminal-wick}, \ref{L:spatial-wick-measures}, \ref{L:joint-fixed-order}, \ref{L:uniform-series-tail}, \ref{L:vertex-crude}, Theorem~\ref{T:full-upper}, \eqref{E:joint-temporal-tail}, \eqref{E:regularized-scaled-moment} (ordinals 54–60); Lemma~\ref{L:damped-homogeneous-norms} (ordinal 62); these were checked against their stated hypotheses and were not counted as assigned completion. The imported static laws \eqref{E:static-ratio-input} and the Chen–Hu static coefficient-rate inputs remain imported facts; their own proofs are unassigned.

Pre-existing (not introduced) concerns worth recording: (i) in ordinal 53, the passage from Chen's finiteness statement to the quantitative bound $Q(g)\le\frac12\|\nabla g\|_2^2+C_0$ on unit Schwartz profiles is an imported specialisation, used only at the smooth level; (ii) ordinals 51–52 and 56–60 inherit finiteness/rate inputs from the unassigned transfer/upper theorems; (iii) ordinals 56 and 60 involve iterated limits (time normalization fixed at each $a$, then $a\downarrow0$), no simultaneous limit, which the proofs and retained scope remarks state explicitly; (iv) the clock obstruction is restricted, and the surrounding remarks (retained unchanged) limit it to the direct unweighted constant-correlation candidate of \eqref{E:naive-clock-candidate}, not to all two-clock representations or Skorohod results. No introduced defect, no lost qualifier, and no numerical constant identification was found.
