# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

The six assigned proof pairs were read in full in both revisions. Every new explanatory sentence was checked against the same hypotheses, constants, domains, normalizations and limiting conventions as the OLD text. The NEW revision is a readability reorganization (introductory sentences, `Step` labels, a few added one-line justifications); no logical step, hypothesis, normalization, or qualifier was changed. Public reconstruction is complete for all six. Details and the checkable working follow.

## L:variational-heat-envelope

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage:

1. Temperedness $\Rightarrow$ polynomial ball growth. Let $0\le\rho\le1$ be smooth, $\rho\equiv1$ on $B_1$; for the dilation $\rho(\cdot/R)$, the finitely many Schwartz seminorms give $|\langle\Gamma,\rho(\cdot/R)\rangle|\le C R^N$, and positivity gives $\Gamma(B_R)\le C R^N$. Summing dyadic annuli, $\int(1+|x|)^{-L}\Gamma(\ud x)\le\sum_j2^{-jL}\Gamma(B_{2^{j+1}})\le C\sum_j2^{j(N-L)}<\infty$ for $L>N$. The NEW Step 1 sentence states exactly this: mass growth $2^{jN}$ times weight decay $2^{-jL}$ is summable for $L>N$. Confirmed.
2. Apply to both $\Gamma$ and $\mu$; Gaussian weights are integrable because $e^{-|y|^2/(2\epsilon)}$ decays faster than every $(1+|y|)^{-L}$.
3. Classical convolution $\Gamma*p_\epsilon$ finite/smooth locally in $x$.
4. Pair with Schwartz $\varphi$; absolute Fubini gives $\langle\Gamma*p_\epsilon,\varphi\rangle=\langle\Gamma,p_\epsilon*\varphi\rangle$. Spectral convention (Hypothesis~H:homog; baseline E:masked-spectral-convention) and $\int p_\epsilon(y)e^{-i\xi y}\ud y=(2\pi\epsilon)^{-d/2}\int e^{-|y|^2/(2\epsilon)}e^{-i\xi y}\ud y=e^{-\epsilon|\xi|^2/2}$ give the RHS distribution. Evenness of $p_\epsilon$ and $\mu$ makes either Fourier sign match; no extra normalization factor. Confirmed (the displayed multiplier is the exact heat normalization).
5. Two continuous distributions equal pointwise. $0\le\Gamma*p_\epsilon$ (nonnegative measure, positive kernel). Evenness of $\mu$ makes $\int e^{i\xi x}e^{-\epsilon|\xi|^2/2}\mu(\ud\xi)$ real with $|\cdot|\le\int e^{-\epsilon|\xi|^2/2}\mu(\ud\xi)=(\Gamma*p_\epsilon)(0)$. Strict positivity at $0$: $\Gamma\ne0\Rightarrow\mu\ne0$ and $e^{-\epsilon|\xi|^2/2}>0$.

Argument preservation: PRESERVED.
New explanations: JUSTIFIED (the dyadic-summation sentence is a correct spelling of the existing bound).
Evidence: the equality and estimate in E:variational-heat-envelope are reproduced verbatim (OLD 33–40, NEW 33–40); the proof adds only a two-sentence framing (NEW 44–46), the Step 1 addition (NEW 50–52), and Step 2 header, all consistent with the OLD body (OLD 52–63).
Lost steps/qualifiers: none identified within this read.

## L:variational-global-mean

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage:

1. Extend $\Psi$ by zero in time (smooth, since support $\subset(0,1)$).
2. For any mixed derivative $D\Psi$ and fixed $\epsilon>0$, compactness of the common spatial support $K$ gives $\|D\Psi\|_\infty<\infty$, and $p_\epsilon\ge p_{\min}>0$ on $K$ gives $|D\Psi(t,x)|\le\|D\Psi\|_\infty 1_K(x)\le C_D p_\epsilon(x)$ with $C_D=\|D\Psi\|_\infty/p_{\min}$.
3. Since $\Gamma\ge0$ and the convolution is order-preserving, $\Gamma*|D\Psi(t,\cdot)|(x)\le C_D(\Gamma*p_\epsilon)(x)\le C_D(\Gamma*p_\epsilon)(0)<\infty$ by E:variational-heat-envelope, uniformly in $t,x$.
4. Derivatives of the convolution fall on the smooth test: $\partial_x(\Gamma*\Psi)=\Gamma*\partial_x\Psi$ (dominated differentiation against the Radon measure), so each $\Gamma*D\Psi$ is globally bounded.
5. Change of variable $r=s-u$ in $h_s(x)=\int_0^1|s-u|^{-a}(\Gamma*\Psi(u,\cdot))(x)\ud u$: since $\Psi$ is extended by zero, $h_s(x)=\int_\R|r|^{-a}(\Gamma*\Psi(s-r,\cdot))(x)\ud r$, with the relevant $r\in[s-1,s]\subseteq[-1,1]$ for $s\in[0,1]$.
6. $|r|^{-a}$ integrable on $[-1,1]$ since $a=\alpha_0<1$; dominated convergence passes derivatives through; e.g. $\partial_s h_s(x)=\int|r|^{-a}(\Gamma*\partial_t\Psi(s-r,\cdot))(x)\ud r$ is bounded by $\sup|\Gamma*\partial_t\Psi|\cdot\int_{-1}^1|r|^{-a}\ud r=2\sup(\cdot)/(1-a)$. Nonnegativity: $\Gamma\ge0$, $\Psi\ge0$, $|r|^{-a}>0$. This gives $0\le h_s\le M$ and the $C_\Psi$-Lipschitz bound in E:variational-global-mean.

Argument preservation: PRESERVED.
New explanations: JUSTIFIED (the NEW text differs only by a paragraph break after the displayed $h_s$ integral; no new assertion).
Evidence: OLD 82–102 and NEW 97–118 are identical in mathematical content; the statement E:variational-global-mean (OLD 75–80, NEW 90–95) is unchanged.
Lost steps/qualifiers: none; a pre-existing cosmetic item in both versions: the text writes “change $r=s-t$” though the displayed substitution is $r=s-u$ (the integration variable of $h_s$). The displayed formula is correct; this is not a new defect.

## P:variational-unmasked-rate

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage:

Step 1 (self-adjointness on $H^2$):
- $A=-\Delta$ is self-adjoint on its maximal $H^2$ domain (Fourier multiplier $|\xi|^2$).
- $B_s=-h_s$ is bounded self-adjoint with $\|B_s\|\le M$ (since $0\le h_s\le M$ by E:variational-global-mean).
- $H_s=A+B_s$ densely defined, symmetric, closed on $H^2$; graph norms equivalent.
- For $b>M$: $H_s-ib=(I+B_s(A-ib)^{-1})(A-ib)$. Resolvent estimate $\|(A-ib)^{-1}\|\le1/b$ gives $\|B_s(A-ib)^{-1}\|\le M/b<1$, so the first factor is Neumann-invertible; same with $+ib$. Hence $H_s\pm ib$ are surjective (deficiency indices $(0,0)$), i.e. $H_s$ is self-adjoint.
- The direct kernel check: for $u\in D(H_s^*)$, solve $(H_s-ib)v=(H_s^*-ib)u$ (solvable by surjectivity); then $u-v\in\ker(H_s^*-ib)=\operatorname{Ran}(H_s+ib)^\perp=\{0\}$, so $D(H_s^*)=D(H_s)$. Valid.

Step 2 (form domain):
- $c_{\mathrm{shift}}=1+M$, $J_s=H_s+c_{\mathrm{shift}}\ge1$ (since $q_s\ge-M\|f\|^2$).
- Integration by parts on $H^2$: $\|J_s^{1/2}f\|^2=q_s(f)+c\|f\|^2$.
- Bounds: lower $\|J_s^{1/2}f\|^2=\|\nabla f\|^2+c\|f\|^2-\int h_s|f|^2\ge\|\nabla f\|^2+\|f\|^2=\|f\|_{H^1}^2$ (using $c=1+M\ge M+?$, and $\int h_s|f|^2\le M\|f\|^2$); upper $\le c\|f\|_{H^1}^2$. Confirmed.
- Spectral cutoffs $1_{[1,n]}(J_s)$ give $H^2$ a core for the half-power norm; Fourier cutoffs give density in $H^1$; completion identifies $D(J_s^{1/2})=H^1$.

Step 3 (real Rayleigh formula):
- Spectral lower bound gives one direction of $\inf\sigma(H_s)=\inf_{\|f\|=1}q_s(f)$.
- Reverse: $E_s\in\sigma(H_s)$; nonzero spectral projections in $[E_s,E_s+\epsilon]$ give unit $H^2$ vectors with Rayleigh values $\le E_s+\epsilon$; $\epsilon\downarrow0$.
- $\sup_f(\int h_sf^2-\|\nabla f\|^2)=\sup_f(-q_s(f))=-\inf_fq_s(f)=-E_s$.
- Real/complex reduction: for $f=u+iv$, $q_s(u+iv)=\|\nabla u\|^2+\|\nabla v\|^2-\int h_s(u^2+v^2)=q_s(u)+q_s(v)$ (the cross terms $\pm i\operatorname{Re}\langle\nabla u,\nabla v\rangle$ cancel; $|f|^2=u^2+v^2$), and $\|f\|_2^2=\|u\|_2^2+\|v\|_2^2$. The complex quotient $\frac{q_s(u)+q_s(v)}{\|u\|^2+\|v\|^2}$ is the norm-weighted average of the real quotients, so at least one nonzero component has quotient no greater than the average. Confirmed; the NEW added sentence (NEW 183–186) is an exact justification of “real tests give the same infimum.”

Step 4 (strict negativity and Lipschitz rate):
- Baseline P:compact-original-common-trial supplies unit compactly supported $w$, finite plateau mask, common strictly negative upper bound: $\|\nabla w\|^2-\int m_Rh_sw^2\le-\epsilon_0$.
- Unmasked form on the same $w$ is no larger: since $0\le m_R\le1$ and $h_s\ge0$, $-\int h_sw^2\le-\int m_Rh_sw^2$, so $q_s(w)\le-\epsilon_0$. Hence $-M\le E_s\le-\epsilon_0<0$, giving $\sqrt{\epsilon_0}\le\lambda_{\Psi,s}\le\sqrt M$. Direction of comparison confirmed.
- $\lambda_{\Psi,s}^2=-E_s$ with $E_s<0$ justifies the positive rate.
- Continuity: for unit $f$, $|q_s(f)-q_t(f)|=|\int(h_s-h_t)f^2|\le\|h_s-h_t\|_\infty$, so $|E_s-E_t|\le\|h_s-h_t\|_\infty$. Then $|\lambda_s-\lambda_t|=\frac{|\lambda_s^2-\lambda_t^2|}{\lambda_s+\lambda_t}\le\frac{C_\Psi|s-t|}{2\sqrt{\epsilon_0}}$. Square-root denominator $2\sqrt{\epsilon_0}$ confirmed, constants dependent on the fixed $\Psi$ (no universal spectral gap is introduced).
- $I_\Psi=\int_0^1\lambda_s\ud s\in(0,\infty)$.

Argument preservation: PRESERVED.
New explanations: JUSTIFIED (intro and Step 3 complex-vector paragraph are correct; all quantities and constants unchanged).
Evidence: E:variational-real-rayleigh and the Lipschitz bound are unchanged (OLD 118–123, 150–171; NEW 134–139, 204–215); the shift constant $c_{\mathrm{shift}}=1+M$ and Lipschitz constant $C_\Psi/(2\sqrt{\epsilon_0})$ are identical in both.
Lost steps/qualifiers: none identified within this read. “No eigenstate at the unmasked bottom” is retained in both statements (OLD 123, NEW 139) and in both proofs.

## P:variational-remove-mask

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage:

Step 1 (nested masks):
- $F(t)=e^{-1/t}$ ($t>0$), $\chi(r)=F(2-r)/(F(2-r)+F(r-1))$, $m_R(x)=\chi(|x|/R)$.
- Denominator strictly positive: for $r\le1$, $F(r-1)=0$ and $F(2-r)>0$; for $1<r<2$ both terms positive; for $r\ge2$, $F(2-r)=0$ and $F(r-1)>0$.
- $F(2-r)$ decreases and $F(r-1)$ increases in $r$, so $\chi$ is nonincreasing, $\chi=1$ on $r\le1$, $\chi=0$ on $r\ge2$; flat at zero gives smoothness; $\chi$ constant near $0$ makes $m_R$ smooth at the origin; masks even, $[0,1]$-valued, pointwise increasing to $1$. Confirmed.

Step 2 (Rayleigh limits):
- NEW added majorant sentence: for unit form test $f\in H^1$, $m_Rh_sf^2\le Mf^2$ pointwise ($0\le m_R\le1$, $h_s\le M$) and $Mf^2\in L^1$; dominated convergence applies. Confirmed.
- NEW added input sentence: compact-family input P:compact-ground-family with common trial from P:compact-original-common-trial; $\lambda_{R,s}^2=-E_1$, the (negative) form bottom of $-\Delta-m_Rh_s$ on $H^1$. Confirmed against baseline E:compact-energy-levels / E:compact-rate-gap.
- $R_0$ chosen so the common trial lies in the plateau; each $R\ge R_0$ retains the negative margin. Compact-family theorem applies to $m_Rh_s$; analogous real Rayleigh formula. Rates continuous, positive, $\le\sqrt M$, monotone in $R$ (larger mask ⇒ larger potential ⇒ more negative bottom ⇒ larger rate, bounded above by $\lambda_{\Psi,s}$ since masked potential $\le$ unmasked potential).
- Sup interchange (two numerical suprema only):
  \[\sup_{R\ge R_0}\lambda_{R,s}^2=\sup_{R\ge R_0}\sup_{\|f\|_2=1,\,f\in H^1(\R^d;\R)}\Big(\int m_Rh_sf^2-\|\nabla f\|_2^2\Big)\]
  Exchanging $\sup_R\sup_f=\sup_f\sup_R$ (valid; sup over a product set), then $\sup_{R\ge R_0}\int m_Rh_sf^2=\int h_sf^2$ (monotone convergence, $m_R\uparrow1$), while $\|\nabla f\|^2$ is $R$-independent, giving $\lambda_{\Psi,s}^2$. Correct.
- Uniform convergence: $R_n=R_0+n$; $\lambda_{R_n,s}\uparrow\lambda_{\Psi,s}$ monotonically, all continuous in $s$; the increasing open sets $\{s:\lambda_{\Psi,s}-\lambda_{R_n,s}<\epsilon\}$ cover compact $I$; finitely many and monotonicity give the largest, i.e. uniform convergence (Dini). Monotonicity extends to real $R\to\infty$. Hence $\int_I\lambda_{R,s}\ud s\uparrow I_\Psi$ by monotone convergence. Confirmed.

Step 3 (supremum of fixed-mask bounds):
- For each fixed $R\ge R_0$, apply P:raw-block-original-lower with the same mask in the operator path and mean: $\liminf_{T\to\infty}T^{-\kappa}\log\E|u(T,x)|^2\ge2\int_I\lambda_{R,s}\ud s-v_\Psi/2$. The LHS is $R$-independent, so taking the numerical supremum over $R$ (using $2\int_I\lambda_{R,s}\ud s\uparrow2I_\Psi$) yields E:variational-unmasked-point-lower. The variance $v_\Psi$ is the original, mask-unchanged variance.
- Disclaimers about no $R(T)$, no unmasked random wave, no uniform-in-mask Gaussian estimate, no exchange of source/radius/large-time limits: retained verbatim (OLD 233–238, NEW 296–301).

Argument preservation: PRESERVED.
New explanations: JUSTIFIED (both additions, the $Mf^2$ majorant and the identification of the compact-family input and $E_1$, are correct and consistent with the baselines).
Evidence: the mask construction $\chi$ and the two-sup identity are unchanged (OLD 204–225, NEW 254–288); E:variational-unmasked-point-lower unchanged (OLD 193–197, NEW 234–238).
Lost steps/qualifiers: none identified within this read.

## L:variational-control-dilation

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage:

Step 1 (bijection, mean, cost):
- $D_r\Psi(s,x)=r^{d+2-\alpha}\Psi(s,rx)$ preserves $C^\infty_{\mathrm{c}}((0,1)\times\R^d;\R)$, $\ge0$, $\ne0$; inverse $D_{1/r}$: $(D_{1/r}D_r\Psi)(s,x)=r^{-(d+2-\alpha)}r^{d+2-\alpha}\Psi(s,r(x/r))=\Psi(s,x)$. Confirmed for the full class.
- Homogeneous Radon pushforward: $\Gamma(cA)=c^{d-\alpha}\Gamma(A)$ gives $\int G(ry)\Gamma(\ud y)=r^{\alpha-d}\int G(z)\Gamma(\ud z)$ (pushforward mass of $A$ equals $\Gamma(r^{-1}A)=r^{\alpha-d}\Gamma(A)$).
- Mean: $h_{D_r\Psi,s}(x)=\int_0^1|s-u|^{-a}r^{d+2-\alpha}\int\Psi(u,r(x-y))\Gamma(\ud y)\ud u=r^{d+2-\alpha}r^{\alpha-d}\int_0^1|s-u|^{-a}(\Gamma*\Psi(u,\cdot))(rx)\ud u=r^2h_{\Psi,s}(rx)$. Confirmed via Radon pushforward only.
- Cost: using the baseline self-adjoint formula $v_\Psi=\int_0^1\int\Psi(\sigma,x)h_\sigma(x)\ud x\ud\sigma$ (E:compact-raw-cost),
  \[v_{D_r\Psi}=\int\!\int(D_r\Psi)(\sigma,x)\,h_{D_r\Psi,\sigma}(x)\ud x\ud\sigma=r^{d+2-\alpha}r^2\int\!\int\Psi(\sigma,rx)h_{\Psi,\sigma}(rx)\ud x\ud\sigma.\]
  The Lebesgue substitution $z=rx$ gives $\ud x=r^{-d}\ud z$, hence $v_{D_r\Psi}=r^{d+2-\alpha}r^2r^{-d}v_\Psi=r^{4-\alpha}v_\Psi$. This cleanly separates the Radon pushforward (in the mean factor) from the Lebesgue volume factor $r^{-d}$; no density is assumed, so singular covariances and white noise are covered. Confirmed.

Step 2 (Rayleigh rate):
- $U_rf(x)=r^{d/2}f(rx)$ is unitary on real $L^2$ (change of variable gives $\|U_rf\|_2^2=\|f\|_2^2$), a bijection preserving $H^1,H^2$ sets under $U_{1/r}$.
- $\|\nabla U_rf\|_2^2=\int r^d|r\nabla f(rx)|^2\ud x=r^2\|\nabla f\|_2^2$.
- $\int h_{D_r\Psi,s}(U_rf)^2=\int r^2h_{\Psi,s}(rx)r^d|f(rx)|^2\ud x=r^2\int h_{\Psi,s}(z)|f(z)|^2\ud z$.
- The real Rayleigh bijection (cf. E:variational-real-rayleigh) maps unit tests $f\mapsto U_rf$, so $\lambda_{D_r\Psi,s}^2=\sup_f r^2(\int h_{\Psi,s}f^2-\|\nabla f\|^2)=r^2\lambda_{\Psi,s}^2$; positive square roots give $\lambda_{D_r\Psi,s}=r\lambda_{\Psi,s}$; integrating over $I$ gives $I_{D_r\Psi}=rI_\Psi$. This uses the real Rayleigh class rather than any unsupported operator-domain scaling rule. Confirmed.
- Supplementary operator identity on $H^2$: $\Delta U_r=r^2U_r\Delta$ and $(h_{D_r\Psi,s}U_rf)(x)=r^{d/2}r^2h_{\Psi,s}(rx)f(rx)=r^2(U_rh_{\Psi,s}f)(x)$, so $H_{D_r\Psi,s}U_r=r^2U_rH_{\Psi,s}$. Correct. Compact-mask remark $m_R(rx)=m_{R/r}(x)$ is the identity $\chi(|rx|/R)=\chi(|x|/(R/r))$. Correct; “a fixed mask radius is not invariant” is accurate.

Argument preservation: PRESERVED.
New explanations: JUSTIFIED (only Step headers added; no new mathematical claim).
Evidence: E:variational-control-dilation and E:variational-dilation-values unchanged (OLD 257–264, NEW 320–327); the factoring $r^{d+2-\alpha}r^2r^{-d}=r^{4-\alpha}$ is explicit in both (OLD 278–282, NEW 343–347).
Lost steps/qualifiers: none identified within this read.

## P:variational-positive-scores

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Original-step coverage:

Step 1 (positive value):
- $k=3-\alpha>0$ (since $\alpha<2$ by $\alpha_0+\alpha<2$), $q=4-\alpha=k+1$, $m=q/k>1$.
- Fix $\Psi_0$; $I_0>0$, $v_0>0$ by baseline L:compact-raw-profile (E:compact-raw-cost gives $0<v_\Psi$).
- $r_0=(I_0/v_0)^{1/k}>0$ (no requirement $r_0<1$). Then $r_0^k=I_0/v_0$ and $q=k+1$ gives $r_0^q v_0=r_0r_0^kv_0=r_0I_0$. Hence $I_{D_{r_0}\Psi_0}-v_{D_{r_0}\Psi_0}/2=r_0I_0-r_0^qv_0/2=r_0I_0/2>0$. The NEW added sentence spells this out correctly.

Step 2 (set scaling):
- $r_c=c^{1/k}$, $K_c=c^m>0$. New added check: $cr_c=c^{1+1/k}=c^{(k+1)/k}=c^{q/k}=K_c$ and $r_c^q=(c^{1/k})^q=c^{q/k}=K_c$. So by Lemma L:variational-control-dilation, $cI_{D_{r_c}\Psi}-v_{D_{r_c}\Psi}/2=c r_c I_\Psi-r_c^qv_\Psi/2=K_c(I_\Psi-v_\Psi/2)$, i.e. E:variational-score-set-scaling.
- Since $D_{r_c}$ is a bijection of $\mathcal C_{\mathrm{pos}}$, the coefficient-$c$ value set equals $K_c$ times the coefficient-one set. Correct.

Step 3 (boundedness from the independent upper estimate — noncircular):
- Baseline T:full-upper for the same canonical solution: $\E|u(T,0)|^2\le e(T+2)^d e^{C_{\mathrm{up}}T^\kappa}$, $T\ge1$.
- Negligible prefactor: $\epsilon=\kappa/2>0$; $T^\epsilon=e^{\epsilon\log T}\ge1+\epsilon\log T$ gives $\log T\le(T^\epsilon-1)/\epsilon$, so $\log T/T^\kappa\le O(T^{-\kappa/2})\to0$; and $\log(T+2)\le\log T+\log3$ for $T\ge1$. Thus the original point limsup $\le C_{\mathrm{up}}<\infty$.
- A fixed positive test/mask lower bound (Step 1, with value $2I_0-v_0/2\ge I_0>0$) makes $Q_2$ finite from below; hence $Q_2\in\R$, $Q_2\le C_{\mathrm{up}}$.
- E:variational-unmasked-point-lower gives $Q_2\ge2I_\Psi-v_\Psi/2$ for every $\Psi$, i.e. every coefficient-two variational value is $\le Q_2\le C_{\mathrm{up}}$.
- E:variational-score-set-scaling at $c=2$ (with $K_2=2^m>0$) bounds every coefficient-one value by $C_{\mathrm{up}}/K_2$; the nonempty set has finite real supremum $S_1^{\mathrm{pos}}>0$. Confirmed; the order of choices (upper bound before taking suprema) is preserved.

Step 4 (suprema and interpretation):
- For general $c$, $K_cS_1^{\mathrm{pos}}$ is the supreum of the coefficient-$c$ set (scaling of a nonempty supremum by $K_c>0$): it is an upper bound, and any smaller number is exceeded by $K_c$ times a coefficient-one expression within positive distance of $S_1^{\mathrm{pos}}$. Finiteness, positivity, and the first identity in E:variational-score-homogeneity follow: $S_c^{\mathrm{pos}}=c^mS_1^{\mathrm{pos}}=c^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}}$.
- Numerical supremum of coefficient-two lower bounds gives $Q_2\ge S_2^{\mathrm{pos}}$ (second identity).
- Qualifications retained: $m>1$ gives $2^m>2$, so $S_2^{\mathrm{pos}}>2S_1^{\mathrm{pos}}$, but this is only a comparison of auxiliary variational values, not a Jensen improvement absent a first-moment identification; no optimizing control is assumed. Confirmed.

Argument preservation: PRESERVED.
New explanations: JUSTIFIED (the two added sentences — the $r_0^k=I_0/v_0$, $r_0^qv_0=r_0I_0$ check and the $cr_c=r_c^q=K_c$ check — are correct scalar-power verifications).
Evidence: E:variational-score-homogeneity and E:variational-score-set-scaling unchanged (OLD 307–311, 331–335; NEW 380–384, 405–410); constants $k,q,m$, the scaling factor $K_c=c^m$, and the upper-bound chain $2I_\Psi-v_\Psi/2\le Q_2\le C_{\mathrm{up}}$ are identical in both.
Lost steps/qualifiers: none identified within this read. The separate zero-covariance convention (tail paragraph, OLD 366–369, NEW 464–467) and the Jensen-qualification sentence are retained in both revisions.

## AUDIT dispositions

- L:variational-heat-envelope — PRESERVED; new explanations JUSTIFIED; reconstruction COMPLETE.
- L:variational-global-mean — PRESERVED; new explanations JUSTIFIED; reconstruction COMPLETE.
- P:variational-unmasked-rate — PRESERVED; new explanations JUSTIFIED; reconstruction COMPLETE.
- P:variational-remove-mask — PRESERVED; new explanations JUSTIFIED; reconstruction COMPLETE.
- L:variational-control-dilation — PRESERVED; new explanations JUSTIFIED; reconstruction COMPLETE.
- P:variational-positive-scores — PRESERVED; new explanations JUSTIFIED; reconstruction COMPLETE.

Only the six inventory labels were treated as assigned; the supplied baseline modules (compact-mean family, raw-block lower, constant-Young, covariance foundation, model/upper/Jensen declarations) were used only as named upstream inputs with their application hypotheses checked, and their own proofs were not counted as individually reviewed proofs. Referenced literature (Teschl, Janson, Young, Friz–Hairer, chen:author2026) remains imported as stated; no primary-source, rendered-page, Lean, or image review was performed or certified.

## Findings and limits

Mathematical outcome: the NEW revision preserves every statement, hypothesis, normalization (heat kernel $(2\pi\epsilon)^{-d/2}$ with multiplier $e^{-\epsilon|\xi|^2/2}$; temporal kernel $|r|^{-a}$, $a=\alpha_0\in(0,1)$; exponents $k=3-\alpha$, $q=4-\alpha$, $m=q/k$), spectral convention, and Rayleigh qualification of the OLD proofs. All six new explanatory additions were verified by direct computation and are correct; no constant, comparison direction, or limiting order was altered. The required application boundaries were all respected: the unmasked operator is constructed by bounded perturbation on the whole space with form domain $H^1$ and no asserted unmasked eigenstate; the real Rayleigh formula keeps both components of a complex vector and uses the norm-weighted quotient comparison; mask removal uses nested deterministic masks, two numerical Rayleigh suprema, Dini uniform convergence, and fixed-$R$ lower bounds with mask-unchanged mean and variance; the dilation lemma distinguishes the Radon pushforward $r^{\alpha-d}$ from the Lebesgue Jacobian $r^{-d}$, giving the mean factor $r^2$, the cost factor $r^{4-\alpha}$, and the rate factor $r$; the positive-score proposition bounds the sets via the independent point upper estimate before taking finite real suprema and preserves all conditional Jensen/source-normalization and zero-covariance qualifiers.

Pre-existing items (identical in both revisions, hence not rewrite defects): (i) a cosmetic variable-naming slip in L:variational-global-mean (“change $r=s-t$” while the actual substitution is $r=s-u$); the displayed formula is correct. (ii) The phrase “negative form bottom” in the new P:variational-remove-mask Step 2 is slightly terse but refers correctly to the negative bottom $E_1\le-\varepsilon$.

Limits: this is independent rewrite-preservation review. It verifies that the NEW six proofs preserve the OLD six proofs and that every newly added explanatory assertion is correct under the stated hypotheses; it does not re-derive the unassigned upstream analytic results, certify the cited external literature, or pass judgment on whole-book correctness beyond the assigned scope. All readings and reconstructions are COMPLETE for the six assigned proofs, so the assignment is fully covered.

No evidence of a new rewrite defect, changed argument, or introduced unsupported claim was found in the assigned pairs.
