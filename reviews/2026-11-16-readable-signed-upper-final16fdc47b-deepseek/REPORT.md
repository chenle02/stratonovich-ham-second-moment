# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro (deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

The OLD and NEW modules differ only by (i) deletions/additions of roadmap sentences and `\medskip`+step headings inside three proofs, (ii) one added cross-reference sentence in `P:signed-operator-upper`, (iii) one grammatical repair in `P:original-signed-point-upper`, and (iv) dropping the adjective "stochastic" in the parenthetical of `L:signed-score-envelope`. The mathematical statements, hypotheses, definitions, equations, constants, quantifiers and limiting orders are identical. I reconstructed every step of all four assigned proofs with public algebra below; no deduction, qualifier, or limiting order was lost or altered. All added explanatory sentences are accurate descriptions of the steps that follow them.

---

## L:signed-score-envelope

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Statement comparison (old LF 19–44 = new LF 19–44).** The statements are identical except one word: OLD has "in particular at the stochastic radius $R_\delta$", NEW has "in particular at the radius $R_\delta$". Since $R_\delta=\delta^{-1}+2$ is deterministic, "stochastic" was a mislabel; the NEW wording is more accurate and no mathemical content, domain or qualifier changes. The declaration ($\mathcal{S}_R$, $V_{\rm up}$), the ceiling $0\le\mathcal{S}_R,V_{\rm up}\le2+2C_{\rm mean}^2<\infty$, the envelope $\eqref{E:signed-polynomial-envelope}$ with constants $A_0=4C_{\rm gr}$, $A_1=2^{\nu+1-\nu/r}C_{\rm gr}32^\nu C_{\rm mean}^\nu$, $\eta_B=2^{\nu+1-\nu/p}C_{\rm gr}B^{\nu/p}$, the range $0<\delta<\min(1,1/B)$, $\rho\ge0$, and the disclaimer sentence are all verbatim identical.

**Original-step coverage.**

1. (Ceiling) Mean linear ⇒ $\mathcal{T}_R0=0$; free form has nonnegative gradient energy and spectral bottom zero ⇒ $\operatorname{Rate}_R(0)=0$.
2. Upstream `P:uniform-rate-averaging` gives $\operatorname{Rate}_R(\Phi)\le 1+C_{\rm mean}\|\Phi\|$. (Hypothesis check: it is stated for the admissible model and uniform in $R\ge1$; the conclusion used is exactly its last clause.)
3. With $q=\|\Phi\|\ge0$, complete the square: $2\operatorname{Rate}_R(\Phi)-q^2/2\le2+2C_{\rm mean}q-q^2/2=2+2C_{\rm mean}^2-(q-2C_{\rm mean})^2/2\le2+2C_{\rm mean}^2$.
4. Lower bound from the zero control: $2\operatorname{Rate}_R(0)-0=0$ is in the sup set, so $\mathcal{S}_R\ge0$, whence $V_{\rm up}\ge0$ and both are $\le2+2C_{\rm mean}^2$.
5. AM–GM alternative; non-attainment disclaimers (no optimizer/rank/positivity/convergence assumptions; ceiling need not be sharp).
6. (Envelope) For $\|a\|_{\delta,p}\le b_{\delta,B}$, $\|\Phi\|\le\rho$, set $v_m=\|a_m\|_\theta$, $h_m=\|(\mathcal{M}_{\delta,B,R}\Phi)_m\|_\theta$; via $\eqref{E:uniform-product-growth}$ and convexity, $F_{\delta,B}(a+\mathcal{M}_{\delta,B,R}\Phi)\le2C_{\rm gr}B\delta n+2^\nu C_{\rm gr}B\delta\sum_m(v_m^\nu+h_m^\nu)$.
7. Weighted power means, first term, and $B$-cancellation, yielding the three displayed coefficients.

**Public working.**

Ceiling: since $2(1+C_{\rm mean}q)-q^2/2=2+2C_{\rm mean}^2-\frac12(q-2C_{\rm mean})^2$, the expression is maximized by $q=2C_{\rm mean}$ with value $2+2C_{\rm mean}^2$; this is the finite ceiling by completing the square, with the single half-quadratic action $\|\Phi\|_{H_I}^2/2$ intact. Rate at zero: $2\operatorname{Rate}_R(0)-0=0$ gives nonnegativity.

Envelope. From $\eqref{E:uniform-product-growth}$ ($\log\|S_E(\ell)U_D(\ell,0)\|\le C_{\rm gr}B(1+\|D\|_\theta^\nu)$, including the free factor $S_E$) and convexity $(u+w)^\nu\le2^{\nu-1}(u^\nu+w^\nu)$ for $\nu\ge1$:
$$F_{\delta,B}(\cdot)=2\delta\log\max(1,\|\mathcal P\|)\le2\delta\sum_m C_{\rm gr}B\bigl(1+2^{\nu-1}(v_m^\nu+h_m^\nu)\bigr)=2C_{\rm gr}B\delta n+2^\nu C_{\rm gr}B\delta\sum_m(v_m^\nu+h_m^\nu).$$

Weighted power mean with exponents $p/\nu\ge1$ and $r/\nu>1$:
$$\delta\sum_m v_m^\nu\le(\delta n)^{1-\nu/p}\|a\|_{\delta,p}^\nu\le(2/B)^{1-\nu/p}b_{\delta,B}^\nu,$$
$$\delta\sum_m h_m^\nu\le(\delta n)^{1-\nu/r}(\delta\sum_m h_m^r)^{\nu/r}\le(2/B)^{1-\nu/r}\bigl(C_B C_{\rm mean}\rho\bigr)^\nu,\qquad C_B\le32B^{3-1/r}.$$

Assembling, with $\delta n\le2/B$:
- first term: $2C_{\rm gr}B\delta n\le4C_{\rm gr}=A_0$;
- residual term: $2^\nu C_{\rm gr}B(2/B)^{1-\nu/p}b^\nu=2^{\nu+1-\nu/p}C_{\rm gr}B^{\nu/p}b^\nu=\eta_B b^\nu$;
- mean term: $2^\nu C_{\rm gr}B(2/B)^{1-\nu/r}\bigl(32B^{3-1/r}C_{\rm mean}\rho\bigr)^\nu=2^{\nu+1-\nu/r}C_{\rm gr}32^\nu C_{\rm mean}^\nu B^{3\nu}\rho^\nu=A_1B^{3\nu}\rho^\nu$; here $B^{1+\nu/r-1+3\nu-\nu/r}=B^{3\nu}$, the factors $B^{\nu/r},B^{-\nu/r}$ cancel exactly.

Both OLD and NEW contain these identical steps; NEW only prefixes the roadmap "We bound the signed score by completing the square in the control norm…" and "We then use the explicit physical Young growth bound and weighted block estimates…", both of which accurately describe Steps 3 and 6–7.

- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read. The old wording "stochastic radius" is a pre-existing mislabel now corrected; no deduction depended on it.

---

## P:signed-moment-bulk-tail

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Statement comparison (old LF 93–117 vs new LF 106–130).** Verbatim identical: definition of the deterministic $\mathcal{E}_{\delta,B,M}$, finiteness, $\eqref{E:signed-error-limit}$ ($e_B$ finite, nonnegative, $e_B\to0$ for every polynomial $M_B=c_{\rm ball}B^{\kappa_{\rm ball}}$), the cutoff condition $4A_1B^{3\nu}\le M^{2-\nu}$, and $\eqref{E:signed-finite-moment}$ with front factor $M^2/(2\delta)$, exponent $(\mathcal{S}_{R_\delta}+\mathcal{E}_{\delta,B,M})/\delta$, tail front factor $4$ and exponent $(A_0+\eta_B b_{\delta,B}^\nu-M^2/4)/\delta$. No qualifier changed.

**Original-step coverage.**

1. Finiteness of $\mathcal{E}_{\delta,B,M}$ from the polynomial envelope and nonnegativity of the rate; a deterministic real number (no selector/measurability needed).
2. Zero control + zero path give rate zero and $F_{\delta,B}(0)\ge0$, so the untruncated sup is already nonnegative.
3. $b_{\delta,B}\to0$ at fixed $B$ matches upstream `P:uniform-arbitrary-residual`; its polynomial-radius conclusion gives $\limsup_B e_B\le0$; fixed-$B$ finiteness plus $e_B\ge0$ prove $\eqref{E:signed-error-limit}$.
4. Transfer: $M_\delta\le\int_0^\infty\frac{\rho}{\delta}e^{(G_{\delta,B}(\rho)-\rho^2/2)/\delta}\,d\rho$.
5. Bulk: for $\rho\le M$, all base-ball $a$ and $\|\Phi\|\le\rho$, $F-\rho^2/2\le2\operatorname{Rate}_{R_\delta}(\Phi)-\|\Phi\|^2/2+\mathcal{E}\le\mathcal{S}_{R_\delta}+\mathcal{E}$; integrate $[0,M]$ → first term, valid even if $M^2/(2\delta)<1$.
6. Tail: apply `L:tube-rayleigh-tail` with $C=A_1B^{3\nu}$ and intercept $A_0+\eta_Bb^{\nu}$; conditions hold; get factor $4$ and exponent $-M^2/4$.
7. Sum → $\eqref{E:signed-finite-moment}$; no infinite-dimensional density / Laplace principle.

**Public working.**

Step 1–3. The sup is bounded by $\sup_{\|\Phi\|\le M}G_{\delta,B}(\|\Phi\|)\le A_0+A_1B^{3\nu}M^\nu+\eta_B b^\nu<\infty$ because the upper expression in step 4's bound is nonnegative; $\operatorname{Rate}\ge0$ so subtractive term only decreases. $F(0)=2\delta\log\max(1,\|\mathcal P(0)\|)\ge0$. The residual proposition `P:uniform-arbitrary-residual`'s $\eqref{E:uniform-residual-integrated-rate}$ is applied with its $b_\delta=b_{\delta,B}$ and $M=M_B$; its double limit $\limsup_{B}\limsup_{\delta}\sup_{\ldots}\{F-2\operatorname{Rate}\}\le0$ over $R\ge1,\|\Phi\|\le M_B,\|x\|_{\delta,p}\le b_{\delta,B}$ is exactly the untruncated sup defining $e_B$, giving $\limsup_B e_B\le0$; $e_B\ge0$ gives $e_B\to0$.

Step 5 bulk exponent bound: for $\rho\le M$, $\|\Phi\|\le\rho\le M$, and $\|a\|_{\delta,p}\le b_{\delta,B}$, and since $R_\delta=\delta^{-1}+2\ge1$ belongs to the $R\ge1$ sup set,
$$F(a+\mathcal M_{\delta,B,R_\delta}\Phi)-2\operatorname{Rate}_{R_\delta}(\Phi)\le\mathcal E_{\delta,B,M},$$
hence
$$F-\rho^2/2\le2\operatorname{Rate}_{R_\delta}(\Phi)-\|\Phi\|^2/2+\mathcal E_{\delta,B,M}\le\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M},$$
using $\rho^2\ge\|\Phi\|^2$. Suprema and $\int_0^M\frac{\rho}{\delta}\,d\rho=M^2/(2\delta)$ give exactly the bulk term $\frac{M^2}{2\delta}e^{(\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M})/\delta}$; correctness does not need $M^2/(2\delta)\ge1$, as stated.

Step 6 tail. `L:tube-rayleigh-tail` (unassigned upstream) requires $M>0$, $C\ge0$, $1<\nu<2$, $4C\le M^{2-\nu}$. Here $C=A_1B^{3\nu}\ge0$, $1<\nu<2$ by the strict subcritical parameter choices, and $4A_1B^{3\nu}\le M^{2-\nu}$ is the proposition's hypothesis. Its algebra: $r^{2-\nu}\ge M^{2-\nu}\ge4C$ gives $Cr^\nu\le r^2/4$, and $r^2\ge M^2$ splits $-r^2/4$ into $-M^2/8-r^2/8$, so $Cr^\nu-r^2/2\le-M^2/8-r^2/8$; since $-\tfrac{d}{dr}[4e^{-r^2/(8\delta)}]=\frac r\delta e^{-r^2/(8\delta)}$, the integral is $4e^{-M^2/(8\delta)}$, times $e^{(A_0'−M^2/8)/\delta}=e^{(A_0+\eta_Bb^\nu-M^2/8)/\delta}$ gives front factor $4$ and exponent $-M^2/4$. Exactly as written in both versions.

- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read.

---

## P:signed-operator-upper

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Statement comparison (old LF 155–163 vs new LF 181–189).** Verbatim identical: $0\le\liminf_\delta\delta\log M_\delta\le\limsup_\delta\delta\log M_\delta\le V_{\rm up}\le2+2C_{\rm mean}^2$.

**Original-step coverage.**

1. Choose $c_{\rm ball}>0$, $\kappa_{\rm ball}>3\nu/(2-\nu)$, $M_B=c_{\rm ball}B^{\kappa_{\rm ball}}$; cutoff ratio computation $\to\infty$ (trivial if $A_1=0$).
2. Fixed $B$: a positive sum $\le2\max$ of its terms; take $\delta\log$ of $\eqref{E:signed-finite-moment}$ → displayed two-term max + $\delta\log2$.
3. At fixed $B$, $b_{\delta,B}\to0$; logarithmic normalizers vanish, specifically $\delta\log(M_B^2/(2\delta))\to0$ via $te^{-t}\le2/t$ with $t=-\log\delta$; limsup subadditivity → $\limsup_\delta\delta\log M_\delta\le\max\{V_{\rm up}+e_B,\ A_0-M_B^2/4\}$.
4. Left side is $B$-independent (restart, same endpoint $P_\delta$); send integer $B\to\infty$: $e_B\to0$, $M_B\to\infty$, $V_{\rm up}$ finite → $\le V_{\rm up}\le2+2C_{\rm mean}^2$.
5. Lower bound $M_\delta\ge1$ → $\liminf\ge0$; order is $\delta$ first, then $B$; no diagonal and no limit of $\mathcal S_{R_\delta}$ assumed.

**Public working.**

Step 1: cutoff requires $M_B^{2-\nu}\ge4A_1B^{3\nu}$; the ratio
$$\frac{M_B^{2-\nu}}{4A_1B^{3\nu}}=\frac{c_{\rm ball}^{2-\nu}}{4A_1}B^{\kappa_{\rm ball}(2-\nu)-3\nu}\longrightarrow\infty$$
because $\kappa_{\rm ball}(2-\nu)-3\nu>0$ (and $2-\nu>0$). Constants and the strictly positive exponent retained.

Step 2: for positive $u,v$, $u+v\le2\max(u,v)$; with $u=\frac{M_B^2}{2\delta}e^{(\mathcal S+\mathcal E)/\delta}$, $v=4e^{(A_0+\eta b^\nu-M_B^2/4)/\delta}$,
$$\delta\log M_\delta\le\delta\log2+\max\Bigl\{\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M_B}+\delta\log(M_B^2/(2\delta)),\ A_0+\eta_Bb^\nu-M_B^2/4+\delta\log4\Bigr\},$$
matching the displayed equation in both versions.

Step 3: $\delta\log(M_B^2/(2\delta))=\delta\log(M_B^2/2)-\delta\log\delta$; with $t=-\log\delta$, $\delta\log\delta=-te^{-t}$, and $te^{-t}\le2/t\to0$. $\delta\log2,\delta\log4\to0$. Subadditivity of limsup over the sum $\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M_B}$ (both finite) gives the stated $\max$. NEW adds the sentence "The lower bound $M_\delta\ge1$ used here is $\eqref{E:point-fixed-finiteness}$ of Lemma `L:point-actual-finiteness`." This is correct: $\eqref{E:point-fixed-finiteness}$ is $1\le\E\|P_\delta\|_{\mathcal L(E)}^2<\infty$ and $M_\delta=\E\|P_\delta\|^2$. (For zero covariance this exact numbered bound is stated for nonzero covariance, but $M_\delta\ge1$ still holds there via $\|S_E(L)\|\ge1$, as `P:original-signed-point-upper` states; so the citation is sound for the nonzero case and no circularity arises.)

Step 4: $M_\delta=\E\|P_\delta\|^2$ is the global endpoint moment; `L:tube-actual-endpoint`/restart identify every block product's endpoint with the same $P_\delta$, so the left side has no $B$. Letting $B\to\infty$: $e_B\to0$, $A_0-M_B^2/4\to-\infty$, so the max tends to $V_{\rm up}$; hence $\limsup_\delta\delta\log M_\delta\le V_{\rm up}$. Lower bound: $M_\delta\ge1\Rightarrow\delta\log M_\delta\ge0\Rightarrow\liminf\ge0$. Order of limits preserved; no assumption of convergence of $\mathcal S_{R_\delta}$ (only its limsup $V_{\rm up}$, which exists and is finite) and no diagonal $B=B(\delta)$.

- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read; the added citation is an improvement, not a changed deduction.

---

## P:original-signed-point-upper

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Statement comparison (old LF 203–214 vs new LF 245–256).** Verbatim identical: for every original admissible model and every fixed $x$,
$$\limsup_{T\to\infty}T^{-\kappa}\log\E|u_\Gamma(T,x)|^2\le\limsup_{\delta\downarrow0}\mathcal S_{\delta^{-1}+2}\le2+2C_{\rm mean}^2,$$
plus the zero-covariance rate-zero clause.

**Original-step coverage.**

1. Upstream `P:original-point-transfer` bounds the original point moment by $\operatorname{DataPref}_\delta M_\delta$ with $\delta\log\operatorname{DataPref}_\delta\to0$; its proof (regularization removed first, full chain, canonical law) is the input; no original $E$ point trace.
2. Decreasing bijection $T_\delta=\delta^{-1/\kappa}$, inverse $\delta=T^{-\kappa}$; take logs, normalized limsup, and `P:signed-operator-upper`.
3. Original canonical spatial stationarity from `P:raw-block-original-lower` extends to every fixed $x$.
4. Moment $\ge1$ by full expansion and finite by the bound → no infinite log differences.
5. Zero covariance: $C_{\rm mean}=0$ directly; $H_I=\{0\}$, $\operatorname{Rate}_R=\mathcal S_R=V_{\rm up}=0$, $u=1$, $P_\delta=S_E(\delta^{-1})$; free bounds give $0\le\delta\log M_\delta\le2\delta\log[C(1+\delta^{-1})]\to0$; no nonzero Gaussian/nondegenerate Cameron assumption; formal $a\downarrow0$ exponent $(4-\alpha)/(3-\alpha)$; no new endpoint-in-$a$ theorem.

**Public working.**

Step 1–2. `P:original-point-transfer`'s $\eqref{E:original-point-rate-reduction}$ gives $\limsup_T T^{-\kappa}\log\E|u_\Gamma(T,x)|^2\le\limsup_\delta\delta\log\E\|P_\delta\|^2=\limsup_\delta\delta\log M_\delta$, with $\kappa=(4-\alpha-a)/(3-\alpha)>1>0$, so $T_\delta=\delta^{-1/\kappa}$ is a decreasing bijection $(0,1)\to(1,\infty)$ with inverse $\delta=T^{-\kappa}$. The data prefactor cost is negligible: $\delta\log\operatorname{DataPref}_\delta=\delta\log(C_\eta/v_d)+d\delta[\log(1+2\delta)-\log\delta]\to0$ (using $te^{-t}\to0$). Chaining with `P:signed-operator-upper` gives $\limsup_\delta\delta\log M_\delta\le V_{\rm up}=\limsup_\delta\mathcal S_{\delta^{-1}+2}\le2+2C_{\rm mean}^2$. Stationarity is imported from `P:raw-block-original-lower` (spatial translation equality of point second moments), exactly as needed to pass from $x=0$ to every fixed $x$. $\E|u(T,x)|^2\ge1$ by the full pairing expansion's unit empty chain, and finiteness by the established bound, so all logarithms are well defined.

Step 5 zero covariance. $\Gamma=0\Rightarrow$ noise $\equiv0$, $u=1$, all operator paths vanish, $P_\delta=S_E(\delta^{-1})$, so $M_\delta=\|S_E(\delta^{-1})\|^2$ deterministic; $H_I=\{0\}$ forces $\operatorname{Rate}_R(0)=0$, $\mathcal S_R=0$, $V_{\rm up}=0$. Free bounds (upstream `L:symplectic-free` lower bound $\ge1$ and Fourier-matrix upper bound $\le C(1+L)$) give $0\le\delta\log M_\delta\le2\delta\log[C(1+\delta^{-1})]\to0$: hence both normalized moments and the signed expression have rate zero, without any nonzero-Gaussian or nondegenerate Cameron-Martin hypothesis. The formal exponent statement is the arithmetic limit of $\kappa$ as $a\downarrow0$, flagged as formal, asserting no new theorem. NEW's only change rewords the broken OLD sentence "Its with the regularization removed first, full-chain and canonical law proof is the input here" into "Its proof, which removes the regularization first, keeps the full chain and works with the canonical law, is the input here": the three qualifiers (regularization removed first; full chain retained; canonical law) are all preserved; meaning and domain unchanged.

- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read. The OLD sentence was grammatically defective; the NEW repair preserves content.

---

## AUDIT dispositions

No AUDIT comments or Lean markers appear in the assigned module (OLD or NEW); the `\LeanMarker` lines in the provided context files belong to unassigned baseline modules and are not AUDIT comments. No AUDIT-worthy issue is introduced by the rewrite. The two OLD phrasing defects ("stochastic radius"; the broken "Its with …" sentence) are repaired in NEW and require no further disposition. I found no remaining defect warranting an AUDIT flag.

## Findings and limits

Scope. This review certifies argument-preservation/readability equivalence of the four assigned proofs in `integrated_signed_moment_upper.tex` between revisions `cdde711…` and `16fdc47…`, not whole-book truth and not the upstream analytic results (`P:uniform-rate-averaging`, `P:uniform-arbitrary-residual`, `L:tube-rayleigh-tail`, `P:original-point-transfer`, `P:raw-block-original-lower`, `L:tube-actual-endpoint`, `L:point-actual-finiteness`), whose proofs remain unassigned. Each upstream result was used only under its stated hypotheses, which I checked at the consumption site.

Verified content. (a) The signed score is a single-control half-quadratic action $\sup_{\Phi\in H_I}\{2\operatorname{Rate}-\|\Phi\|^2/2\}$ in the original covariance $\Gamma$, unweighted by $g$; (b) the finite ceiling $2+2C_{\rm mean}^2$ follows by completing the square with coefficient $\tfrac12$; (c) the envelope constants $A_0=4C_{\rm gr}$, $A_1=2^{\nu+1-\nu/r}C_{\rm gr}32^\nu C_{\rm mean}^\nu$, $\eta_B=2^{\nu+1-\nu/p}C_{\rm gr}B^{\nu/p}$ and the powers $B^{3\nu}\rho^\nu$, $B^{\nu/p}b^\nu$ are reproduced exactly, including the $B^{\nu/r}B^{-\nu/r}$ cancellation; (d) the deterministic product error $e_B\to0$ on polynomial balls $M_B=c_{\rm ball}B^{\kappa_{\rm ball}}$; (e) bulk integral front factor $M^2/(2\delta)$ and exponent $(\mathcal S_{R_\delta}+\mathcal E)/\delta$; (f) tail front factor $4$ and exponent $-M^2/4$ via the $-M^2/8-r^2/8$ cutoff; (g) the order $\delta\downarrow0$ first at fixed $B$, ball, thresholds, then integer $B\to\infty$, with the endpoint moment $B$-independent via restart and no diagonal limit or assumed signed-score limit; (h) the full point transfer, canonical scaling, negligible data cost, stationarity, and the direct zero-covariance free-flow case without an $E$ point trace or nondegenerate Gaussian assumption; (i) the signed upper expression is not identified with any source constant or nonnegative-control variational value, per the retained disclaimers. No Fourier inversion step occurs in the assigned module itself; the covariance convention is distributional in the supplied hypothesis and is respected downstream.

Limits. This is a text-level comparison of the two embedded module copies; no compilation, rendering, cross-file LaTeX resolution, or primary-source PDF/image review was performed. Line references use the inventory's raw-module LF convention. Reading of both versions for all four proofs is complete; public reconstruction of every assigned step is complete; no step was silently repaired. The OLD text is not treated as an oracle; the comparisons above were done against the reconstructed mathematics on both sides.

PASS (high confidence): all four assigned proof pairs preserve their statements, hypotheses, equations, constants and deductions; the additions are correct, benign explanatory scaffolding and one correct citation.
