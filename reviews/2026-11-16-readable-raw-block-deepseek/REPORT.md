# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

The seven assigned proofs were reorganized from single paragraphs into labeled Steps with short explanatory sentences and a few added justifications. I compared both revisions line by line. All original deductions, quantifiers, constants and caveats are retained; the statements/definitions are textually unchanged. The new explanatory assertions I checked are mathematically correct under the supplied hypotheses. The notes below are pre-existing phrasing issues or scope notes, not defects introduced by the rewrite.

## L:raw-block-inputs
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The pullback isometry check is unchanged: substituting $s=s_m+\delta u$, $t=s_m+\delta r$ into the original covariance gives factor $\delta^{a-2}\delta^2\delta^{-a}=1$ (OLD 75–77; NEW 74–77). The common-space shift identity $W_{\delta,m}(f)=W_{\mathrm{fast}}(f(\cdot-mB,\cdot))$ is retained. In new Step 3 the added "time change … contributes one Jacobian factor $\delta$" is correct: $T_{\delta,m}$ has prefactor $\delta^{a/2-1}$ and the substitution $\mathrm ds=\delta\,\mathrm du$ yields net $\delta^{a/2}$, exactly \eqref{E:raw-block-mean-jacobian}; then $g_\delta\delta^{a/2}=\delta^{(1-a)/2}\delta^{a/2}=\sqrt\delta$, matching \eqref{E:raw-block-covariance} $b=\E[XZ]=\sqrt\delta\,H$. The added Step 2 sentences ("number of blocks is finite for each fixed $\delta$", "product path space is separable", "correlations … retained by taking all coefficients from the same original noise") are correct: $N=\lfloor1/(\delta B)\rfloor$ is finite, a finite product of separable Banach spaces is separable, and Gaussianity of the Banach tuple is testable on finite linear combinations of block coordinate functionals together with $Z$. The matrix-element extension, Sobolev adjoint \eqref{E:driver-covariance-row}, and the "span of $E$ and both constant coordinates is dense in $F$; $E$ alone is not" qualification are all retained.
- Lost steps/qualifiers: none identified within this read.

## P:raw-block-gaussian-law
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The Cameron–Martin identity \eqref{E:raw-block-gaussian-law} with exact quadratic cost $v/(2\delta)$ is retained: density $\exp(-sZ-s^2v/2)$ with $s=\delta^{-1/2}$ gives $\exp(-Z/\sqrt\delta-v/(2\delta)$/2)\Rightarrow -Z/\sqrt\delta-v/(2\delta)$; completing the square in the $N(0,v)$ density yields the equivalent measure $Q_s$. The added sign/direction check is correct: $Z=z\cdot G$, $|z|^2=v$, so $\exp(-sz\cdot G-s^2|z|^2/2)e^{-|G|^2/2}=e^{-|G+sz|^2/2}$, i.e. $G+sz$ is standard under $Q_s$; the translate $\ell(X+sb)=TG+s\ell(b)=TG+sTz=T(G+sz)$ cancels that shift. (The phrase "shifts the standard Gaussian vector by $-sz$" is terse but its next sentence states the correct cancellation.) The coordinate-to-Borel extension (matrix entries + $0,B$ generating the sigma-field, norm as supremum over a countable dense set, cylinder pi-system, monotone convergence, $sb=H$ via \eqref{E:raw-block-covariance}) is unchanged, including the "no translated exceptional-domain assumption" qualification.
- Lost steps/qualifiers: none identified within this read. Minor pre-existing wording risk: "shifts the standard Gaussian vector by $-sz$" is direction-terse; harmless because the following sentence fixes the sign.

## L:raw-block-uniform-error
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The maximum bound remains $(N+1)^{1/p}C\sqrt p\,g_\delta\le C'\sqrt p\,\delta^{(1-a)/2-1/p}$; the added "pth power of the maximum is at most the sum of the pth powers … without independence" is exactly the justification for the factor $(N+1)^{1/p}$, and $p>2/(1-a)$ makes the $\delta$-exponent strictly positive. The moment computation $\E M_\delta^{2n}\le 2C^{2n}(2n)^n\delta^{n(1-a)-1}\le 2C^{2n}(2n)^n$ for $n\ge n_0$, $n_0(1-a)\ge1$, is unchanged; $n!\ge(n/e)^n$ yields the geometric tail $2\sum_{n\ge n_0}(2ecC^2)^n$ for small $c$, proving \eqref{E:raw-block-maximum-exponential}. The added sentences about "the supremum over blocks is already inside the displayed random bound, through $M_\delta$" and "a higher moment … together with convergence in probability gives convergence in the requested lower moment" correctly unpack the old uniform-integrability step: the global Young bound $\max_m\sup_{u\le B}\|D_m^+(u)\|\le C_B\exp(C_B(1+H_0+M_\delta)^{1/\theta})$ has the block maximum already inside via $M_\delta$, and $1/\theta<2$ makes every finite power dominated by a multiple of $e^{cM_\delta^2}$ (controlled by \eqref{E:raw-block-maximum-exponential}). The $H_m^{\mathrm{stat}}$ approximation $\|H_m-H_m^{\mathrm{stat}}\|_{C^\theta}\le C\delta$ and "only $s_m\le1$ supplies the ground templates" qualifier are retained.
- Lost steps/qualifiers: none identified within this read.

## L:raw-block-indexed-cone
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: Deterministic lemma; all choices and five smallness conditions are byte-for-byte retained. Entrance: normalized amplitude $\ge a_*-M_\ell\varepsilon_{\mathrm{op}}E_0\ge a_*/2$, normalized residual $\le q_BM_QE_0+M_Q\varepsilon_{\mathrm{op}}E_0\le\vartheta a_*/4$; the added "dividing … $\vartheta a_*/4$ by … $a_*/2$ gives aperture $\le\vartheta/2$" is exactly right. Rebase: the added identity $Q_c-Q_b=\Pi_b-\Pi_c$ is correct ($(I-\Pi_c)-(I-\Pi_b)=\Pi_b-\Pi_c$), giving $\|Q_cz\|\le\|Q_bz\|+\|\Pi_b-\Pi_c\|\|z\|\le(\vartheta+\nu M_z)A$; likewise $\ell_c(z)\ge(1-\nu M_z)A$. The propagation quantities $x=e^{-\lambda_cB}\ell_c(Dz)$, $y=e^{-\lambda_cB}\|Q_cDz\|$ are unchanged, with $x\ge(1-\nu M_z-M_\ell\varepsilon_{\mathrm{op}}M_z)A\ge(1-\varrho)A>A/2$ and $y\le[q_B(\vartheta+\nu M_z)+M_Q\varepsilon_{\mathrm{op}}M_z]A\le\vartheta A/2$ (using $q_B\le1/8$, $\nu M_z\le\vartheta$, $M_Q\varepsilon_{\mathrm{op}}M_z\le\vartheta/4$); since $x>A/2$, $y\le\vartheta A/2\le\vartheta x$. Terminal: $\ell_c(z)\ge3A/4$, $\|Q_cz\|\le2\vartheta A$, and the added "normalized complementary flow is at most $C_{\mathrm{gap}}$ for every nonnegative terminal time … uniformly even at $u=0$" matches $\|e^{-\lambda t}P(t)Q\|\le C_{\mathrm{gap}}e^{-\eta_{\mathrm{gap}}t}\le C_{\mathrm{gap}}$, which at $t=0$ needs $C_{\mathrm{gap}}\ge\|Q\|$ (already supplied by the imported normalized-complement estimate). Result $\ge 3j_*/4-2H_{\mathrm{obs}}C_{\mathrm{gap}}\vartheta-j_*/8\ge j_*/2$ using $16H_{\mathrm{obs}}C_{\mathrm{gap}}\vartheta\le j_*$. The final target \eqref{E:raw-block-positive-product} with $c_*=a_*j_*/4$, exponent $(1-\varrho)^{N-1}$, $N=1$ empty induction and $u=0$ inclusion are all retained. Ground-family hypotheses ($\lambda_\sigma\in[\sqrt\varepsilon,\sqrt M]$, $d_0>0$, positive margins \eqref{E:compact-positive-margins}) are the unchanged inputs.
- Lost steps/qualifiers: none identified within this read.

## L:raw-block-restart
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The restart relation \eqref{E:raw-block-restart} is unchanged and rests on $W_{\delta,m}(f)=W_{\mathrm{fast}}(f(\cdot-mB,\cdot))$ from L:raw-block-inputs; $L_{\mathrm{ext}}=(N+1)B\ge L=\delta^{-1}$ follows from $N+1\ge1/(\delta B)$. The conjugation identity $S_F(mB)[A_{\mathrm{glob}}^{\mathrm{src}}(mB+u)-A_{\mathrm{glob}}^{\mathrm{src}}(mB)]S_F(-mB)=X_m^{\mathrm{src}}(u)$ and the "no physical mask is commuted through a wave group" disclaimers are retained. The added Step 4 explanation of the recurrence is correct: subtracting the next pair of ordered products by adding/subtracting the source factor times the old partial product gives $d(n+1)\le\|F^{\mathrm{src}}_{n+1}\|d(n)+\|F^{\mathrm{src}}_{n+1}-F_{n+1}\|\|\Pi_n\|\le C\,d(n)+C^n e_{\mathrm{src}}$, then extension by identities yields $d(N+1)\le(N+1)C^{N+1}e_{\mathrm{src}}$; Hölder with $C\in L^{4(N+1)}$ and the error in $L^4$ gives $L^2$ convergence at fixed $\delta,N$. The fixed-$\delta$ limitation ("This is only a fixed-$\delta$ source limit" and "no growing-product stability assertion") is retained.
- Lost steps/qualifiers: none identified within this read.

## P:raw-block-point-comparison
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (one pre-existing phrasing note below)
- Evidence: The squared observable $j_\delta$ and its continuity are unchanged; applying \eqref{E:raw-block-gaussian-law} at $j_\delta$ with translate $X+H$ gives \eqref{E:raw-block-square-identity} using the single $Z=W(\Psi)$ and $v$. The amplitude rescaling is unchanged: $\Gamma_\delta=g_\delta^2\Gamma$, $W'=g_\delta W_{\mathrm{fast}}$, same degrees $\alpha,a$; the $n$th chain is multiplied by $g_\delta^n$. The source-limit verification is unchanged: $F_m=D_m^0(B)$ ($m<N$), $F_N=D_N^0(\tau)$, telescoping gives $\le nC_\rho^ne_\rho$. The added sentences correctly justify the telescoping bound (each of the $n$ terms has one error factor and $\le n-1$ factors $\le C_\rho$, and $C_\rho\ge1$ permits replacing $C_\rho^{n-1}$ by $C_\rho^n$), and the Hölder step gives $\|\cdot\|_{L^2}\le n\|C_\rho\|_{L^{4n}}^n\|e_\rho\|_{L^4}\to0$. The masked comparison and canonical-scaling chain are retained, including the identity $g_\delta Y_{\mathrm{fast}}(u)=\delta^{(1-a)/2}\delta^{a/2}Y_{\epsilon,\eta}(\delta u)=\sqrt\delta\,Y_{\epsilon,\eta}(\delta u)$ and the statement that the comparison is a moment inequality, with $r_T=T\delta$ distinct from the fixed mask $R$ and "no tilted source limit or change of the original slow $\Psi,Z,v$".
- Lost steps/qualifiers: none lost. Pre-existing loose phrase, present identically in both revisions: "Hölder with exponents $4n$ and $4$." Read literally $1/(4n)+1/4\neq1/2$; the correct reading is Hölder(4,4) on $(C_\rho^n,e_\rho)$, giving exactly the displayed $\|C_\rho\|_{L^{4n}}^n\|e_\rho\|_{L^4}$. This is cosmetic; the conclusion is valid.

## P:raw-block-original-lower
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The union bound $\mathbb P(M_\delta>\eta)\le A_p\eta^{-p}\delta^{\gamma_p}$, $\gamma_p=p(1-a)/2-1>0$, with "no independence is needed", and Chebyshev $\mathbb P(|Z|>\delta^{-1/4})\le v\delta^{1/2}$ are unchanged, giving $p_\delta\to1$. The common event $E_\delta=\{E_{\mathrm{op},\delta}\le\varepsilon_{\mathrm{op}}\}\cap\{|Z|\le\delta^{-1/4}\}$ is retained; on it the cone lemma applies with $\sigma_m=s_m=m\delta B\in I$, $\delta B\le\omega$, so $Y_{\delta,B}>0$ and $\delta\log Y_{\delta,B}\ge\delta\log c_*+\delta(N-1)\log(1-\varrho)+$ (left Riemann sum). The added Riemann-sum explanation is correct: subintervals have length $\delta B$ (N of them) and $\delta\tau$ (one), total length $N\delta B+\delta\tau=\delta(NB+\tau)=1$; left-endpoint error on a subinterval of length $\ell\le\delta B$ is $\le C_\lambda\ell\,\delta B$, summing over total length one to $C_\lambda\delta B$. The estimate $\delta(N-1)\log(1-\varrho)\ge\log(1-\varrho)$ uses $0\le\delta(N-1)\le1/B\le1$ and $\log(1-\varrho)<0$, retained. Substituting into \eqref{E:raw-block-square-identity} and \eqref{E:raw-block-original-comparison} gives $\E|u(T,0)|^2\ge p_\delta\exp((2I_R-2e_{\mathrm{rate}}-v/2)/\delta-\delta^{-3/4})$; normalizing by $\delta$ gives the penalty $\delta^{1/4}\to0$ and $\delta\log p_\delta\to0$. The quantification order ("first fixed its own $B=B(e_{\mathrm{rate}})$ and then took $\delta\downarrow0$ … only now let $e_{\mathrm{rate}}\downarrow0$; no choice $B=B(\delta)$") and the translation argument for fixed $x$ are unchanged.
- Lost steps/qualifiers: none identified within this read.

## AUDIT dispositions
No `AUDIT` markers or comments remain in either the OLD or NEW module text (only `LeanMarker`/`LeanEqMarker` appear). I found no AUDIT-worthy defect introduced by the rewrite. The three items noted (terse "shifts by $-sz$", "exponents $4n$ and $4$", "original slow original variance" wording) are cosmetic and pre-existing; they do not change the mathematics and are not rewrite defects.

## Findings and limits
The rewrite is purely additive: Step labels, one-paragraph summaries, and explanatory sentences inserted into otherwise unchanged proof bodies. All seven statements/definitions are unchanged. Every added explanation I checked is justified under the same hypotheses: the $\delta^{a/2-1}\delta=\delta^{a/2}$ and $g_\delta\delta^{a/2}=\sqrt\delta$ covariances; the sign/direction of the Cameron–Martin translate; the max-moment factorization without independence; the $Q_c-Q_b=\Pi_b-\Pi_c$ rebasing identity; the left-endpoint Riemann-sum error including the remainder interval; and the telescoping recurrence and Hölder estimates for finite ordered products at fixed $\delta,N$. The prohibited substitutions are absent: no deterministic-surrogate replacement of the tilted mean (the random $X+H$ is retained throughout and the No-go16/19 cautions remain), no scalar displacement-moment multiplication in place of the full-displacement/velocity $F$-phase argument, and no mask commuting through waves (explicitly disclaimed). Consumer uses of upstream inputs respect their stated hypotheses (fixed $R,B,\Psi$, fixed finite horizons, $0<\eta_{\mathrm{gap}}<d_0$, $\Gamma\ne0$ locality, fixed-$\delta$ source limits completed before $\delta\downarrow0$).

Scope: this is a proof-readability/argument-preservation comparison of the seven labeled proofs only. It does not certify the imported upstream theorems (ground family, variance envelopes, source convergence, canonical scaling, masked moments), their primary-source fidelity, or whole-book correctness; those remain unassigned. Readings of all seven OLD and NEW proof bodies and their statements were COMPLETE for the purposes of this comparison; no auxiliary-file or rendered-page verification was performed.
