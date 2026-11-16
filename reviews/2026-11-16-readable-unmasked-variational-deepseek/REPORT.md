# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

The NEW revision restructures each proof into labeled steps and inserts clarifying sentences; the statements and equation bodies are word-identical to OLD. I read all six complete proofs in both revisions, including unchanged portions, and reconstructed the added assertions from public equations/estimates. Every new explanatory sentence is mathematically consistent with the surrounding argument and with the supplied baseline/context declarations; no step, qualifier, or disclaimer of OLD is dropped, and no new defect is introduced.

## L:variational-heat-envelope
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  OLD proof (LF 42–67) is one paragraph; NEW (LF 42–87) splits it into Step 1/Step 2. Statement (LF 28–40 both) and E:variational-heat-envelope are unchanged. NEW Step 1's added dyadic expansion ("mass bound … $2^{jN}$ and … weight … $2^{-jL}$; summable when $L>N$") is exactly the OLD sentence "Summing dyadic annuli shows $(1+|x|)^{-L}$ is integrable for $L>N$": on $\{2^j\le|x|<2^{j+1}\}$ the tempered ball-mass bound contributes $O(2^{jN})$, $e^{-\epsilon|x|^2/2}$ (and its derivatives) contributes $O(2^{-jL})$ for every $L$, and $\sum_j 2^{-j(L-N)}<\infty$ for $L>N$. The claim "A Gaussian and each of its derivatives decrease faster than any such polynomial weight" is standard and correctly justifies integrability against both $\Gamma$ and $\mu$.
  NEW Step 2's addition is the correct modulus bound: $|e^{i\xi\cdot x}e^{-\epsilon|\xi|^2/2}|=e^{-\epsilon|\xi|^2/2}$, so the spectral integral is bounded by its $x=0$ value (phase = 1 there); OLD stated the same as "absolute value is bounded by its total Gaussian mass, the value at zero." Normalization is preserved: $p_\epsilon=(2\pi\epsilon)^{-d/2}e^{-|x|^2/(2\epsilon)}$ has Fourier transform $e^{-\epsilon|\xi|^2/2}$, and NEW retains "without an extra normalization factor." Evenness of $\mu$ still kills the odd (imaginary) part; strict positivity at 0 from $\Gamma\ne0$, $p_\epsilon>0$ is retained.
- Lost steps/qualifiers: none identified within this read.

## L:variational-global-mean
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  Statement (OLD LF 70–80, NEW LF 90–100) and E:variational-global-mean unchanged. OLD proof LF 82–102; NEW LF 102–126 adds only the time-support confinement explanation: the zero-time extension of $\Psi$ has support in $(0,1)$, so $s-r\in(0,1)$ confines $r$ to a bounded interval for $s$ in compact $I=[0,1]$; the same holds for any derivative of the test. This is correct ($r\in(s-1,s)\subset(-1,1)$ for $s\in[0,1]$) and is precisely what OLD's "the relevant $r$ lie in a fixed bounded interval" used; hence $|r|^{-a}$ integrable near $r=0$ since $a=\alpha_0<1$. The ordering $\Gamma*|D\Psi(t,\cdot)|\le C_D\,\Gamma*p_\epsilon\le C_D(\Gamma*p_\epsilon)(0)$ follows from $\Gamma\ge0$ and $|D\Psi(t,x)|\le C_Dp_\epsilon(x)$ (positive minimum of $p_\epsilon$ on the compact support), so the uniform-in-$t,x$ bound is still Lemma L:variational-heat-envelope. "Every derivative thus falls on the smooth test" (not the singular temporal kernel) and "No directional decay … inferred" are retained.
- Lost steps/qualifiers: none identified within this read.

## P:variational-unmasked-rate
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  Statement (OLD LF 110–123, NEW LF 134–147) identical, including "No eigenstate at the unmasked bottom is asserted." OLD proof LF 125–176, NEW LF 149–233 in four steps.
  Step 1 (self-adjointness): NEW explains the two-parameter surjectivity. Factorization $(H_s-ib)=(I+B_s(A-ib)^{-1})(A-ib)$ with $\|B_s(A-ib)^{-1}\|\le\|B_s\|\|(A-ib)^{-1}\|=M/b<1$ gives Ran$(H_s-ib)=\mathcal H$; surjectivity at $-ib$ enables solving $(H_s-ib)v=(H_s^*-ib)u$, and $\ker(H_s^*-ib)=\operatorname{Ran}(H_s+ib)^\perp=\{0\}$ uses surjectivity at $+ib$. This is a correct restatement of OLD's adjoint-domain argument.
  Step 3 (real Rayleigh without eigenstate): NEW adds that a vector in the range of $\mathbf 1_{[E_s,E_s+\epsilon]}(H_s)$ lies in $D(H_s)=H^2$ (bounded spectral multiplier) and has Rayleigh quotient in $[E_s,E_s+\epsilon]$; correct, this produces the test vectors for the reverse inequality. It also spells out the complex splitting $q_s(u+iv)=q_s(u)+q_s(v)$ and $\|u+iv\|_2^2=\|u\|_2^2+\|v\|_2^2$ (cross terms vanish), so the quotient is the norm-weighted average of the two real quotients, with one nonzero component ≤ the average. This is exactly the required two-component, additive, norm-weighted comparison; the real part alone is not used.
  Step 4 (strict negativity, Lipschitz): unchanged; compact trial from P:compact-original-common-trial gives masked form ≤ $-\epsilon_0$ on $w$, and masking with $0\le m_R\le1$ reduces potential energy, so the unmasked form on the same $w$ is no larger; hence $-M\le E_s\le-\epsilon_0<0$, $\sqrt{\epsilon_0}\le\lambda_{\Psi,s}\le\sqrt M$. Lipschitz denominator $1/(2\sqrt{\epsilon_0})$ from $|\sqrt{-E_s}-\sqrt{-E_t}|=|E_s-E_t|/(\sqrt{-E_s}+\sqrt{-E_t})$. "No compact-potential spectral theorem was applied to $H_s$" retained. No universal gap or eigenstate invented.
- Lost steps/qualifiers: none identified within this read.

## P:variational-remove-mask
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  Statement (OLD LF 186–197, NEW LF 243–254) unchanged. OLD proof LF 199–239, NEW LF 256–320 in three steps.
  Masks: $m_R=\chi(|x|/R)$, $\chi$ nonincreasing, $\chi=1$ on $\{|x|\le R\}$, $0$ on $\{|x|\ge2R\}$; since $\chi\equiv1$ on $[0,1)$ (because $F(r-1)=0$ there), $m_R$ is smooth at the origin and the family is nested and increases pointwise to 1. Retained.
  Step 2 sup-interchange: NEW's majorant $0\le m_Rh_sf^2\le Mf^2$ uses $0\le h_s\le M$ (E:variational-global-mean) and $0\le m_R\le1$; $Mf^2\in L^1$ for unit $f$. The displayed identity swaps exactly two numerical suprema over the product of the radius and test index sets: $\sup_a\sup_b g(a,b)=\sup_{a,b}g(a,b)$, so no analytic interchange is at stake; monotonicity $m_R\uparrow1$ and $h_s\ge0$ give $\sup_R\int m_Rh_sf^2=\int h_sf^2$. Correct, and "Only two numerical suprema were interchanged. Positive square roots give the pointwise rate convergence" is retained.
  NEW's uniformity explanation is correct: $\lambda_{\Psi,s}-\lambda_{R_n,s}\ge0$ is continuous (both rates continuous), the sets $\{s:\lambda_{\Psi,s}-\lambda_{R_n,s}<\epsilon\}$ are open and increasing in $n$; a finite subcover of compact $I$ has a largest member which then contains all of $I$; larger radii only decrease the (nonnegative) error. Correct deterministic compactness; no unmasked random flow.
  Step 3 unchanged and disclaimers retained verbatim: no $R(T)$, no unmasked noisy wave, no uniform-in-mask Gaussian estimate, no exchange of source/radius/large-time limits; each fixed-mask bound (P:raw-block-original-lower) gives $Q_2\ge2\int_I\lambda_{R,s}\,ds-v_\Psi/2$ for the SAME fixed original point liminf $Q_2$, and $\sup_R(2\int_I\lambda_{R,s}\,ds-v_\Psi/2)=2I_\Psi-v_\Psi/2$ since $\int_I\lambda_{R,s}\,ds\uparrow I_\Psi$. The mean and covariance are not changed by the mask.
- Lost steps/qualifiers: none identified within this read.

## L:variational-control-dilation
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  Statement (OLD LF 251–264, NEW LF 332–345) and E:variational-control-dilation/E:variational-dilation-values unchanged. OLD proof LF 266–294, NEW LF 347–389 in two steps.
  Step 1 exponent accounting is correct: amplitude $r^{d+2-\alpha}$ times Radon factor $r^{\alpha-d}$ gives $r^2$ for the mean, matching the pushforward identity $\int G(ry)\Gamma(dy)=r^{\alpha-d}\int G(z)\Gamma(dz)$ (from $\Gamma(A/r)=(1/r)^{d-\alpha}\Gamma(A)=r^{\alpha-d}\Gamma(A)$). The cost computation $v_{D_r\Psi}=r^{d+2-\alpha}r^2r^{-d}v_\Psi=r^{4-\alpha}v_\Psi$ is the Lebesgue substitution $z=rx$, $dx=r^{-d}dz$, cleanly separated from the Radon pushforward; NEW's added sentence states exactly this bookkeeping.
  Step 2 uses the real Rayleigh bijection via $U_rf(x)=r^{d/2}f(rx)$, a unitary on $L^2$ with $\|\nabla U_rf\|_2^2=r^2\|\nabla f\|_2^2$ and $\int h_{D_r\Psi,s}(U_rf)^2=r^2\int h_{\Psi,s}f^2$, giving $\lambda_{D_r\Psi,s}=r\lambda_{\Psi,s}$ and $I_{D_r\Psi}=rI_\Psi$. The operator identity $H_{D_r\Psi,s}U_r=r^2U_rH_{\Psi,s}$ appears only as a supplementary remark after the Rayleigh argument, not as its basis, so the instruction to "use the real Rayleigh class" is honored. Bijectivity with inverse $D_{1/r}$ is via the amplitude power. The fixed-mask non-invariance remark ($m_R(rx)=m_{R/r}(x)$) is retained.
- Lost steps/qualifiers: none identified within this read.

## P:variational-positive-scores
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  Statement (OLD LF 297–311, NEW LF 392–406) unchanged, including "no first-moment or source-constant identification is asserted." OLD proof LF 313–364, NEW LF 408–484 in four steps.
  Step 1 algebra is correct: $k=3-\alpha>0$, $q=4-\alpha=k+1$, $r_0=(I_0/v_0)^{1/k}$; $r_0^kv_0=I_0$ and $q=k+1$ give $r_0^qv_0=r_0I_0$, so $r_0I_0-r_0^qv_0/2=r_0I_0/2>0$, using $I_0>0$ (P:variational-unmasked-rate) and $v_0>0$ (L:compact-raw-profile).
  Step 2 scalar agreement is correct: $cr_c=c^{1+1/k}=c^{q/k}=K_c$ and $r_c^q=c^{q/k}=K_c$; combined with the dilation lemma this reproduces E:variational-score-set-scaling, and bijectivity of $D_{r_c}$ shows the coefficient-$c$ set is $K_c$ times the coefficient-one set.
  Step 3 boundedness is non-circular and uses the independent Theorem T:full-upper. The prefactor estimate $\log T\le(T^{\epsilon}-1)/\epsilon$ (from $e^x-1\ge x$) and $\log(T+2)\le\log T+\log3$ for $T\ge1$ makes $T^{-\kappa}\log e(T+2)^d\to0$. Then $Q_2\le C_{\mathrm{up}}$ by liminf ≤ limsup, and E:variational-unmasked-point-lower gives $2I_\Psi-v_\Psi/2\le Q_2$ for every $\Psi$, so $S_2^{\mathrm{pos}}\le Q_2\le C_{\mathrm{up}}$; scaling at $c=2$ bounds the coefficient-one set by $C_{\mathrm{up}}/K_2$.
  Step 4 set equality gives $S_c^{\mathrm{pos}}=K_cS_1^{\mathrm{pos}}=c^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}}$; positivity from Step 1. The comparison $S_2^{\mathrm{pos}}>2S_1^{\mathrm{pos}}$ (since $2^m>2$) is kept as auxiliary and explicitly not a Jensen improvement without a first-moment identification; the separate zero-covariance convention paragraph ("For $\Gamma=0$ … set all these variational values to zero …") is retained verbatim. No optimizing control is assumed.
- Lost steps/qualifiers: none identified within this read.

## AUDIT dispositions
All six assigned proof pairs: Old reading COMPLETE, New reading COMPLETE, Argument preservation PRESERVED, New explanations JUSTIFIED. Statement/definition text is preserved for every label; the full nonnegative nonzero class $C_{\mathrm{pos}}$, original $W(\Psi)$, $v_\Psi=\E W(\Psi)^2$, original amplitude, and $0<a=\alpha_0<1$ are retained throughout. Heat normalization, distributional spectral convention, bounded-perturbation self-adjointness on $H^2$, closed $H^1$ form domain, no-eigenstate caveat, real Rayleigh via two-component norm-weighted quotient, masked/unmasked comparison direction, square-root Lipschitz denominator, two-numerical-suprema interchange, Radon-versus-Lebesgue scaling, real-Rayleigh dilation, non-circular boundedness, coefficient-two lower comparison, Jensen/source-normalization qualification, and zero-covariance convention are all present and correctly retained. Unassigned baseline proofs were used only under their stated hypotheses and were not counted as additional reviewed proofs.

## Findings and limits
- No rewrite defects were found; the NEW text adds only faithful restatements and bookkeeping clarifications.
- Contextual limits (not target defects): the target proofs import several unassigned upstream results — P:compact-original-common-trial and L:compact-raw-profile (compact mean family), P:raw-block-original-lower (fixed-mask point lower bound), T:full-upper (point upper bound), and the compact-family real-Rayleigh/form-domain machinery. I verified these are invoked at the correct application hypotheses (fixed mask/trial, original control and covariance, same canonical solution), but their own proofs are not part of this assignment and are not certified here.
- Minor delegation note: in P:variational-remove-mask the masked compact rates are asserted to satisfy the real Rayleigh over the full unit $H^1$ class via "the same real/complex quotient argument"; this is consistent with the baseline declaration that the common compact form domain is $H^1$, but full verification of that transfer is upstream.
- This review addresses rewrite preservation, not whole-book truth or primary-source/Lean/render certification; those are outside the assigned scope.

