# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

Scope: exactly the 6 assigned proof labels in
`notes/integrated_intrinsic_constant.tex`, comparing OLD
`cdde711c248862f33207860107dd0e6b31d60852` against NEW
`16fdc47b22b74feffded7aeb223f2d579b505176`. Context modules were read only as
unassigned inputs/definitions; their proofs are not counted as extra reviewed
proofs.

## L:positive-raw-embedding
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. *Scalar Schur bound.* For \(0<a<1\), \(\varphi(x)=x^{1-a}\) is concave, so
     \(\varphi(s)+\varphi(1-s)\le 2\varphi(1/2)=2^{a}\). Hence
     \[
       \int_0^1 K(s,t)\,dt=\frac{s^{1-a}+(1-s)^{1-a}}{1-a}\le K_0:=\frac{2^a}{1-a}.
     \]
  2. *Operator bound for \(K\).* For \(f\ge0\), Cauchy–Schwarz against
     \(K(s,t)\,dt\) gives, with Tonelli,
     \[
       \|Kf\|_2^2\le K_0\int_0^1(Kf)(t)f(t)\,dt\le K_0^2\|f\|_2^2,
     \]
     hence \(\|Kf\|_2\le K_0\|f\|_2\). Absolute values give the same bilinear
     bound \(|\iint K fg|\le K_0\|f\|_2\|g\|_2\).
  3. *Definition of \(J_G\).* Approximation of \(L^2(I)\) scalars by
     \(C_c^\infty(I)\) makes the test-null classes Cauchy in \(H_t\), defines the
     bounded inclusion with pairing equal to \(\iint K\langle F,G\rangle_G\), and
     the same bound on differences extends from finite \(G\)-valued tensors and
     simple fields to all of Bochner \(L^2(I;G)\). This establishes
     \eqref{E:positive-bochner-inclusion}.
  4. *Hilbert-valued identification.* For \(G=H_{\mathrm{sp}}\), the Bochner
     integral \(\int_I K(s,t)F(t)\,dt\) converges a.e. since
     \(\int_I K(s,t)\|F(t)\|\,dt=(K\|F\|)(s)\in L^2(I)\). On smooth finite
     tensors it equals \((C_t\otimes I)J_GF\). The completed tensor map converges
     in \(L^r(I;G)\) by Lemma L:uniform-mean-tensor and
     \eqref{E:positive-bochner-inclusion}; since \(|I|=1\) and \(r>2\),
     \(L^r\subset L^2\), so uniqueness of \(L^2\) limits identifies the two
     versions, and the integral lies in \(L^r\).
  5. *Original smooth-test norm.* With \(B\) a closed ball containing the spatial
     supports of \(\Psi\),
     \[
       \|q\|_{H_{\mathrm{sp}}}^2\le |B|\,\Gamma(B-B)\|q\|_\infty^2
       \tag{\ref{E:positive-local-spatial-bound}}
     \]
     because only \(x\in B\), \(y\in B-B\) contribute. Using compact-support
     tensor approximation from Lemma L:cameron-supported-tensor, the image of
     \(J_{H_{\mathrm{sp}}}\) is the original test class, and absolute Fubini gives
     \[
       \|\Psi\|_{H_I}^2=\iint K(s,t)\langle\Psi_s,\Psi_t\rangle\,ds\,dt
       =\int_{I\times\mathbb R^d}\Psi(s,x)h_{\Psi,s}(x)\,dx\,ds=v_\Psi.
     \]
  6. *Masked operator row.* Testing \eqref{E:uniform-mean-row} with \(z=(f,0)\),
     \(w=(0,\Lambda g)\), the row is
     \((\eta_Rf)(\eta_R\Lambda^{-1}\Lambda g)=m_Rfg\), and Fubini (two compact
     supports, integrable time kernel) gives
     \[
       \Big\langle\int_I K(s,t)\Psi_t\,dt,\ m_Rfg\Big\rangle_{H_{\mathrm{sp}}}
       =\int m_Rh_{\Psi,s}fg.
     \]
     Both sides are bounded operators on \(E\); dense states extend to \(E\) and
     \(J_R\) provides a canonical version for every \(R,s\), with no
     simultaneous version over rough controls.

- Argument preservation: PRESERVED. Step-by-step, the NEW proof is the OLD proof
  with added roadmap sentences and Step 1–4 headings; paragraphs are verbatim.
- New explanations: JUSTIFIED. The two added summary sentences merely describe
  Steps 1–2 ("temporal Schur bound ... completed temporal mean") and Steps 3–4.
  The phrase "completed temporal mean" is mildly imprecise for Step 2 (it is the
  completed *tensor map* \(C_t\otimes I\), not \(T_R\)), but no deduction uses
  that summary sentence.
- Evidence: the NEW proof at LF 44–132 reproduces old LF 42–111 verbatim apart
  from headings; the bounds
  \(K_0=2^a/(1-a)\), \(L^r\subseteq L^2\) uniqueness, and the explicit row
  computation are unchanged.
- Lost steps/qualifiers: none identified within this read.

## L:positive-physical-gram
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. *Realization in \(H_I\).* \(h_i=\mathbf1_{I_i}/\ell_i\in H_t\) by
     L:positive-raw-embedding, and the smooth compact \(f_i^2,m_Rf_i^2\) lie in
     \(H_{\mathrm{sp}}\) via the fractional-product/test definition and
     \eqref{E:positive-local-spatial-bound}. Hence
     \(k_i^R=h_i\otimes m_Rf_i^2\), \(k_i^\infty=h_i\otimes f_i^2\in H_I\).
  2. *Label row.* On smooth finite tensors, \eqref{E:uniform-mean-row} with
     \(z=(f_i,0)\), \(w=(0,\Lambda f_i)\) has row
     \((\eta_Rf_i)(\eta_R\Lambda^{-1}\Lambda f_i)=m_Rf_i^2\); temporal
     integration with \(h_i\) proves \eqref{E:positive-label-row} on dense
     tensors:
     \[
       \langle\Phi,k_i^R\rangle=\ell_i^{-1}\int_{I_i}
       v_{\mathcal T_R\Phi(s)}(f_i,f_i)\,ds.
     \]
  3. *Completion.* The right side is bounded by
     \(\ell_i^{-1/r}C_{\mathrm{mean}}\|\Phi\|\|f_i\|_{H^{1/2}}^2\) (Hölder plus
     \eqref{E:uniform-completed-mean}), and the left by Hilbert Cauchy–Schwarz;
     the identity extends to the completed \(H_I\). `v_L` is the displacement
     form of L:uniform-E-lift.
  4. *Gram entrywise order.* Writing \(C^R_{ij}=\langle h_i,h_j\rangle\langle
     m_Rf_i^2,m_Rf_j^2\rangle\), \(D_{ij}=\langle h_i,h_j\rangle\langle
     f_i^2,f_j^2\rangle\), one has \(0\le m_R\le1\), \(\langle h_i,h_j\rangle\ge0\),
     and the spatial pairing is
     \[
       \langle m_Rf_i^2,m_Rf_j^2\rangle
       =\iint \Gamma(dy)\,m_R(x)f_i^2(x)m_R(x-y)f_j^2(x-y)\,dx,
     \]
     dominated pointwise by the same expression without \(m_R\). Tonelli gives
     \(0\le C^R_{ij}\le D_{ij}\) entrywise. The row cancellation
     \((m_R=m_R)\) introduces no extra Fourier factor, and no PSD order of
     \(D-C^R\) is used (matching P:gram-entrywise-comparison).
- Argument preservation: PRESERVED. NEW adds a roadmap and Step 1/Step 2 headings;
  all proof sentences are unchanged.
- New explanations: JUSTIFIED (pure summary of the two steps).
- Evidence: the entrywise comparison uses mask order \(0\le m_R\le1\) applied to
  both spatial positions, not PSD-difference order; unchanged.
- Lost steps/qualifiers: none identified within this read.

## L:positive-uniform-optimizer
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. *Uniform ball restriction.* With \(C=C_{\mathrm{mean}}\), \(q=\|\Phi\|\),
     Proposition P:uniform-rate-averaging gives
     \[
       2\operatorname{Rate}_R(\Phi)-q^2/2\le 2+2Cq-q^2/2<2-2q<0\quad(q>M).
     \]
     The middle inequality is \(2Cq-q^2/2<-2q\iff q>4C+4=M\), and \(M=4C+4\).
     The zero control gives value zero, so the supremum of \(\mathcal S_R\) is
     attained inside \(\|\Phi\|\le M\).
  2. *Finite optimizer in the same ball.* For the unmasked objective
     \(\mathfrak F_D\), Proposition P:gram-positive-optimizer gives a maximizer
     at zero or a positive conic sum \(\Phi_D\). Choose \(R'\) with plateau
     containing all \(f_i\)-supports so \(k_i^{R'}=k_i^\infty\). With
     \(W_i=\ell_i^{-1}\int_{I_i}\mathcal T_{R'}\Phi(s)\,ds\), the label row and
     Rayleigh formula give
     \[
       \mathfrak F_D(\Phi)\le 2\sum_i\ell_i\lambda(W_i)-q^2/2
       \le 2+2\sum_i\ell_i\|W_i\|-q^2/2
       \le 2+2Cq-q^2/2,
     \]
     using \(\lambda(L)\le\max(1,\|L\|)\le1+\|L\|\), norm-of-average bounds, and
     \(L^1\le L^r\). No averaging error \(e_n\) is used here. Hence
     \(\|\Phi_D\|\le M\) independently of partition, profiles, \(R'\).
  3. *Nonnegative smoothing.* On the nonzero branch write
     \(\Phi_D=\sum_{i\in A}w_i h_i\otimes f_i^2\), \(w_i>0\). Convolve the
     zero-extended \(h_i\) with a nonnegative smooth approximate identity and
     multiply by cutoffs \(0\le\chi_j\le1\uparrow1\); then \(h_{i,j}\to h_i\) in
     \(L^2(I)\), hence \(\Psi_j=\sum_i w_i h_{i,j}f_i^2\to\Phi_D\) in \(H_I\) by
     \eqref{E:positive-bochner-inclusion}. Positivity of \(\|\Phi_D\|^2\) (one
     eligible positive diagonal, all entries nonnegative) forces
     \(\Psi_j\ne0\) eventually, so \(\Psi_j\in\mathcal C_{\mathrm{pos}}\). Rate
     continuity from P:uniform-rate-averaging gives
     \[
       |\operatorname{Rate}_{R'}(\Psi_j)-\operatorname{Rate}_{R'}(\Phi_D)|
       \le\sqrt{3+C\|\Psi_j\|+C\|\Phi_D\|}\sqrt{C\|\Psi_j-\Phi_D\|}\to0,
       \tag{\ref{E:positive-rate-continuity}}
     \]
     uniformly in \(R'\). The zero branch is handled separately by
     \(S_2^{\mathrm{pos}}\ge0\).
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The Step readings match the actual order: the
  optimizer bound is established before any averaging error is invoked.
- Evidence: \eqref{E:positive-rate-continuity} is exactly the integrated form of
  \eqref{E:uniform-E-rate-continuity} with \(K(s)=\max(1,\|W_1(s)\|,\|W_2(s)\|\),
  \(L^1\le L^r\), giving \(\sqrt{3+C\|\Psi_j\|+C\|\Phi_D\|}\sqrt{C\|\Psi_j-\Phi_D\|}\).
- Lost steps/qualifiers: none identified within this read.

## P:positive-signed-comparison
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. *Uniform averaging error.* Uniform \(n\)-cell partitions of length \(1/n\)
     realize the \(B=1,\delta=1/n\) scheme of P:uniform-rate-averaging (last empty
     cell omitted), giving \(e_n\to0\) independent of \(R\) with
     \[
       \Big|\operatorname{Rate}_R(\Phi)-\sum_i\ell_i\lambda(W_i)\Big|\le e_n,
       \qquad W_i=\ell_i^{-1}\int_{I_i}\mathcal T_R\Phi(s)\,ds,
     \]
     for \(\|\Phi\|\le M\).
  2. *Finite Rayleigh trials.* For fixed \(R,\Phi,n\), each \(W_i\) has
     \eqref{E:positive-label-row} pairing. \(C_c^\infty\) unit trials are dense in
     the \(H^1\) unit sphere, and form continuity gives
     \[
       \lambda(W_i)=\sup_{\substack{f\in C_c^\infty\\\|f\|_2=1}}
       \sqrt{(v_{W_i}(f,f)-\|\nabla f\|_2^2)_+}.
     \]
     The real Rayleigh supremum is nonnegative (P:uniform-E-spectral), so the
     positive part does not change it. Choose one near-maximizing \(f_i\) per
     cell with error \(\le\varepsilon\) in the square root, contributing
     \(2\varepsilon\) after weighting by \(\sum_i\ell_i=1\). Thus
     \[
       2\operatorname{Rate}_R(\Phi)-\|\Phi\|^2/2
       \le\mathfrak F_{C^R}(\Phi)+2e_n+2\varepsilon.
     \]
  3. *Optimized Gram comparison.* Optimizing gives
     \(\mathfrak F_{C^R}(\Phi)\le\mathscr S(C^R)\le\mathscr S(D)=\mathfrak
     F_D(\Phi_D)\) (optimized values, not the same control). By
     L:positive-uniform-optimizer, \(\|\Phi_D\|\le M\) before averaging is
     reused. With \(R'\) covering the supports, the label row, Rayleigh bound and
     the same averaging estimate give
     \[
       \mathfrak F_D(\Phi_D)
       \le2\operatorname{Rate}_{R'}(\Phi_D)-\|\Phi_D\|^2/2+2e_n.
       \tag{\ref{E:positive-finite-optimizer-bound}}
     \]
  4. *Smoothing and closing.* If \(\Phi_D=0\) the finite value is zero.
     Otherwise \(\Psi_j\to\Phi_D\) positive-smooth; L:positive-raw-embedding
     identifies the means with \(B_E(m_{R'}h_{\Psi_j,s})\) and cost with
     \(v_{\Psi_j}\). Since \(h_{\Psi_j,s}\ge0\) and \(0\le m_{R'}\le1\), form
     order gives \(\operatorname{Rate}_{R'}(\Psi_j)\le I_{\Psi_j}\), so
     \[
       2\operatorname{Rate}_{R'}(\Psi_j)-\|\Psi_j\|^2/2\le S_2^{\mathrm{pos}}.
     \]
     Rate and cost convergence pass this to \(\Phi_D\); combining the two
     \(2e_n\) terms gives
     \[
       2\operatorname{Rate}_R(\Phi)-\|\Phi\|^2/2\le S_2^{\mathrm{pos}}+4e_n+2\varepsilon.
     \]
     Then \(\varepsilon\downarrow0\), supremum over the ball via
     L:positive-uniform-optimizer, and \(n\to\infty\) prove
     \eqref{E:positive-signed-comparison}.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The roadmap says entrywise comparison replaces the
  masked optimizer by an unmasked positive-conic optimizer, and the uniform ball
  permits reuse of the same \(e_n\); this is exactly Steps 3–4.
- Evidence: the exact constants \(2\varepsilon\) (weighted trial error) and
  \(2e_n\) twice (summing to \(4e_n\)) are retained; the additive identity
  \(4e_n+2\varepsilon\) is the same in both versions.
- Lost steps/qualifiers: none identified within this read.

## P:positive-score-cutoff
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. *Mask removal for a fixed control.* Fix \(\Psi\in\mathcal C_{\mathrm{pos}}\)
     before any \(R\) or moment limit. The explicit mean version of
     L:positive-raw-embedding gives rate \(\lambda_R(s)\) with
     \(0\le\lambda_R(s)\le\lambda_{\Psi,s}\) by real form order. For each real
     compact smooth unit \(f\), \(m_R=1\) on its support for all large \(R\)
     (plateau property, no monotonicity needed), so
     \[
       \liminf_{R\to\infty}\lambda_R(s)^2
       \ge\int h_{\Psi,s}f^2-\|\nabla f\|_2^2.
     \]
     Trial density and \eqref{E:variational-real-rayleigh} identify the supremum
     of the right side with \(\lambda_{\Psi,s}^2\); hence
     \(\lambda_R(s)\to\lambda_{\Psi,s}\) for these versions. The global bound
     \(H_\Psi=\sup_{s,x}h_{\Psi,s}(x)<\infty\) gives
     \(\lambda_R(s)\le\sqrt{H_\Psi}\), so dominated convergence gives
     \(\operatorname{Rate}_R(\Psi)\to I_\Psi\).
  2. *Liminf and suprema.* Since \(\|\Psi\|^2=v_\Psi\) is \(R\)-independent,
     \(\liminf_R\mathcal S_R\ge2I_\Psi-v_\Psi/2\) for each fixed \(\Psi\). For
     \(\varepsilon>0\) choose one fixed \(\Psi\) with
     \(2I_\Psi-v_\Psi/2>S_2^{\mathrm{pos}}-\varepsilon\) (valid by finiteness and
     the definition of the supremum); taking the liminf and \(\varepsilon\downarrow0\)
     gives \(\liminf_R\mathcal S_R\ge S_2^{\mathrm{pos}}\). The reverse
     \(\limsup\) is \eqref{E:positive-signed-comparison}.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED (the added preamble summarizes exactly the two
  paragraphs).
- Evidence: the cutoff removal uses only \(m_R=1\) on compact supports, not
  monotonicity; the dominated bound \(\sqrt{H_\Psi}\) and the choice of a single
  near-supremal test are unchanged.
- Lost steps/qualifiers: none identified within this read.

## T:intrinsic-second-moment
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. *Nonzero covariance.*
     - Upper: P:original-signed-point-upper gives
       \[
         \limsup_{T\to\infty}T^{-\kappa}\log\mathbb E|u_\Gamma(T,x)|^2
         \le\limsup_{\delta\downarrow0}\mathcal S_{\delta^{-1}+2}.
       \]
       Along \(R=\delta^{-1}+2\to\infty\), P:positive-score-cutoff gives
       \(\lim_{\delta\downarrow0}\mathcal S_{\delta^{-1}+2}=S_2^{\mathrm{pos}}\).
     - Lower: P:variational-positive-scores gives the same \(S_2^{\mathrm{pos}}\)
       as a lower bound for the original point liminf.
     - Both bounds concern the same canonical Stratonovich solution, the same
       exponent \(\kappa=(4-\alpha-a)/(3-\alpha)\), original covariance and
       variance-half action \(v_\Psi/2\), with regularization removed first and
       all mixed/unequal/self/empty chains and both phase components for data
       \((1,0)\). Original spatial stationarity (P:raw-block-original-lower)
       extends both bounds to fixed \(x\). Hence the limit exists and equals
       \(S_2^{\mathrm{pos}}\).
     - Homogeneity, positivity and finiteness are
       \eqref{E:variational-score-homogeneity}, giving
       \(S_2^{\mathrm{pos}}=2^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}}\).
       \eqref{E:variational-real-rayleigh} and the definition of \(v_\Psi\)
       produce \eqref{E:intrinsic-positive-formula}.
  2. *Zero covariance.* If \(\Gamma=0\), \(H_I=\{0\}\), all means, variances and
     rates vanish, \(\mathcal S_R=S_c^{\mathrm{pos}}=0\), and \(u=1\); both
     formulas are direct zero identities.

- Argument preservation: PRESERVED. The only changes are (i) the grammatical
  repair "Their with the regularization removed first identifications" →
  "Their identifications, made with the regularization removed first, retain",
  preserving the qualifier; (ii) the added sentence that
  \(\delta^{-1}+2\to\infty\), so cutoff convergence applies along that radius
  without an exchange of limits; (iii) the added sentence that the \(S_2/S_1\)
  factor is the control-dilation factor, not a first-moment identification.
- New explanations: JUSTIFIED. The radius tends to infinity, so
  \(\lim_{\delta\downarrow0}\mathcal S_{\delta^{-1}+2}=S_2^{\mathrm{pos}}\) is a
  single limit along a sequence (no interchange of limits). The homogeneity
  factor \(2^{(4-\alpha)/(3-\alpha)}\) is exactly
  \eqref{E:variational-score-homogeneity} at \(c=2\), i.e. the control-dilation
  factor of L:variational-control-dilation; it is not an inference of a printed
  first-mean constant.
- Evidence: upper and lower bounds are combined for the same derived constant
  \(S_2^{\mathrm{pos}}\) and exponent; the direct zero-covariance branch is
  retained; the new sentences do not alter any inequality.
- Lost steps/qualifiers: none identified within this read.

## AUDIT dispositions
No AUDIT-worthy issue is found. The six NEW proofs retain every original step,
equation label, quantifier, constant, limiting order, zero/nonzero branch and
qualifier of the OLD proofs. The module contains no residual AUDIT comments.

Minor non-AUDIT notes (pre-existing and cosmetic, not rewrite defects):
- L:positive-raw-embedding NEW roadmap describes Step 2 as "completed temporal
  mean"; mathematically Step 2 identifies the completed temporal *tensor map*
  \(C_t\otimes I\), while the mean \(T_R\) is identified in Step 4. This is a
  summary-sentence imprecision only; no deduction depends on it.
- The textual repair in T:intrinsic-second-moment Step 1 removes a pre-existing
  grammatical defect ("Their with the regularization removed first
  identifications") without changing the mathematical claim.

## Findings and limits
Both versions of all 6 assigned proofs are completely readable and their public
reconstructions are complete. The NEW revision is an explanatory restructure:
roadmap sentences and numbered Steps are added, and two clarifying sentences are
added to Theorem T:intrinsic-second-moment; the mathematical content is
unchanged or only rephrased in an equivalent way. Specifically verified:
- Original covariance inclusion \(J_G\) with \(\|J_GF\|^2\le K_0\|F\|^2_{L^2(I;G)}\),
  \(K_0=2^a/(1-a)\), Hilbert-valued Schur/tensor bounds, and the \(L^r\subseteq
  L^2\) uniqueness used to identify the Bochner integral with
  \((C_t\otimes I)J_G\).
- Original smooth-test norm/variance identity \(\|\Psi\|^2_{H_I}=v_\Psi\), the
  physical masked row \(m_Rfg\), and the explicit no-rough-control
  version disclaimer.
- Finite physical Gram factors \(C^R_{ij}=\langle h_i,h_j\rangle\langle m_Rf_i^2,
  m_Rf_j^2\rangle\), \(D_{ij}=\langle h_i,h_j\rangle\langle f_i^2,f_j^2\rangle\)
  with entrywise mask order, not PSD-difference order.
- Uniform optimizer ball \(M=4C_{\mathrm{mean}}+4\) before reuse of the
  averaging error; nonnegative temporal smoothing with cost/rate convergence and
  a separate zero branch.
- The exact trial error \(2\varepsilon\) and the two \(2e_n\) averaging errors
  (total \(4e_n\)), optimized-Gram comparison (not same-control comparison), the
  positive-control upper bound \(\operatorname{Rate}_{R'}(\Psi_j)\le I_{\Psi_j}\),
  and nonmonotone plateau cutoff removal.
- Retention of the variance-half action \(v_\Psi/2\), the full nonseparable
  nonnegative class \(\mathcal C_{\mathrm{pos}}\), original covariance amplitude,
  kinetic coefficient one, and the direct zero-covariance branch in the final
  theorem.

Limits: this review compares the two written revisions and checks internal
deduction preservation; it does not certify the unassigned upstream statements
(P:uniform-rate-averaging, P:uniform-E-spectral, P:gram-positive-optimizer,
P:gram-entrywise-comparison, P:variational-positive-scores,
P:original-signed-point-upper, P:raw-block-original-lower, etc.), does not
review source PDFs/images/rendered pages, and does not verify Lean quotation
correspondence. Mechanical byte retention was not treated as mathematical
evidence; the working above was reconstructed from the stated equations and
estimates.
