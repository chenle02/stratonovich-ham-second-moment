# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

All seven assigned proofs were read in full in both revisions. The statements are byte-identical; the NEW proofs add only structuring (numbered steps, short intros) and explanatory sentences. I reconstructed each deduction from the stated equations and hypotheses; every added explanation is locally justified, and no step or qualifier of the OLD argument is dropped.

## P:compact-ground-family
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The form-domain identification is unchanged: $A_\sigma=H_\sigma+c\ge1$ with $\|A_\sigma^{1/2}u\|_2^2=q_\sigma(u)+c\|u\|_2^2$; the added sentence "the shifted potential term $c-V_\sigma$ lies between one and $c$" matches $0\le V_\sigma\le M$, giving $\|u\|_{H^1}^2\le\|A^{1/2}u\|^2\le c\|u\|_{H^1}^2$; core-density/completion argument is verbatim. $-M\le E_1\le-\varepsilon$ follows from the imported max--min plus \eqref{E:compact-common-trial}; the bottom is below essential threshold zero only then is Theorem 10.13 invoked — both order and qualifier preserved. The NEW Step-3 gloss "the denominator is at most $2\sqrt M$" is correct: $\lambda_\sigma,\mu_\sigma\le\sqrt M$ (both levels lie in $[-M,0]$), so $(\lambda^2-\mu^2)/(\lambda+\mu)\ge\Delta_*/(2\sqrt M)$; compactness of $I$ gives $\Delta_*=\min_I(E_2-E_1)>0$, including $E_2$ passage to the threshold. Step 4: from $p_\tau=ap_\sigma+r$ with $r\perp p_\sigma$, positivity gives $a=\langle p_\tau,p_\sigma\rangle>0$, $a^2+\|r\|^2=1$; the two bounds $q_\sigma(p_\tau)\le E_1(\sigma)+2d_V$ and $\ge E_1(\sigma)+\Delta_*\|r\|^2$ yield $\|r\|^2\le2d_V/\Delta_*$ and \eqref{E:compact-ground-continuity} via $2(1-a)\le2(1-a^2)$. $H^2$ continuity via $(1-\Delta)p_\sigma=(1-\lambda_\sigma^2+V_\sigma)p_\sigma$ unchanged (the bound $1+2M$ is a harmless conservative tightening over the exact $1+M$).
- Lost steps/qualifiers: none identified within this read. Pre-existing concerns: none.

## L:compact-fractional-phase
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The resolvent order is derived from the variational identity $\langle f,(T+t)^{-1}f\rangle=\sup_u\{2\operatorname{Re}\langle f,u\rangle-q_T(u)-t\|u\|^2\}$, whose maximizer satisfies $(T+t)u=f$; increasing $q$ decreases the bracket, reversing the order $(T+t)^{-1}\ge(S+t)^{-1}$. The NEW "opposite order" gloss is exactly this. The scalar identity $\sqrt x=\pi^{-1}\int_0^\infty t^{-1/2}x/(x+t)dt$ I verified by $t=xr^2$: integrand $x^{-1/2}r^{-1}/(1+r^2)\cdot2xr\,dr=(2/\pi)x^{1/2}dr/(1+r^2)$, integrating to $x^{1/2}$. Spectral calculus via $T/(T+t)$ and positive Tonelli gives $T^{1/2}\le S^{1/2}$ as forms; this is resolvent order, not an assertion about noncommuting powers. Applied to $B\le A_\sigma\le cB$ ($(cB)^{1/2}=\sqrt c\,B^{1/2}$) this reproduces \eqref{E:compact-quarter-power} exactly. Duality: the dual of $\|A^{1/4}u\|$ at $z\in L^2$ is $\|A^{-1/4}z\|$ with attainer a multiple of $A^{-1/2}z$; the NEW sentences about reversed inequalities and the constants depending only on $c$ are correct. The negative completion $H^{-1/2}$ is unchanged.
- Lost steps/qualifiers: none identified within this read. Pre-existing concerns: none.

## P:compact-E-wave
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The phase-isometry entry computation is correct. In $(A^{1/4}u,A^{-1/4}z)$ coordinates the generator is $\begin{psmallmatrix}0&(h+c)^{1/2}\\ -h(h+c)^{-1/2}&0\end{psmallmatrix}$, whose exponential is $\begin{psmallmatrix}C_t(h)&(h+c)^{1/2}S_t(h)\\ -h(h+c)^{-1/2}S_t(h)&C_t(h)\end{psmallmatrix}$, matching \eqref{E:compact-spectral-wave} conjugated by $\operatorname{diag}(A^{1/4},A^{-1/4})$; the NEW gloss about the $(h+c)^{\pm1/4}$ weights is exact. Nonnegative part: $|S_t(h)|\le\min(t,h^{-1/2})$; for $h\le1$, $\sqrt{h+c}\,t\le\sqrt{1+c}\,t$; for $h\ge1$, $\sqrt{h+c}/\sqrt h=\sqrt{1+c/h}\le\sqrt{1+c}$; lower entry $\sqrt h|\sin(t\sqrt h)|/\sqrt{h+c}\le1$ (NEW spell-out correct). Negative part $-\mu_\sigma^2\le h<0$: $|C_t|\le e^{\mu t}$, $|S_t|\le te^{\mu t}$, with $|h|\le M$ (since $E_2\ge E_1\ge-M$) and $1\le h+c\le c$; $\mu=0$ empties the negative branch, so $C(1+t)=C(1+t)e^{0t}$ holds. Both ground copies are retained: the decaying branch $(p_\sigma,-\lambda_\sigma p_\sigma)\cdot(\langle p,u\rangle-\langle p,z\rangle/\lambda)/2$ remains in $I-\Pi_\sigma^E$ with factor $e^{-\lambda t}\le1$; projection norms are bounded since $1\le c-\lambda_\sigma^2\le c$, giving $\|e_\sigma^E\|^2=c/(c-\lambda^2)^{1/2}$ finite. Eigenrelation $\ell_\sigma^EP_\sigma^E(t)=e^{\lambda t}\ell_\sigma^E$ I verified as an adjoint eigenvector of $(z,-Hu)$ with eigenvalue $\lambda$. Duhamel/Picard identification, spectral cutoffs, strong-vs-operator-norm distinction and "No density of $E$ in $F$ is used" are all preserved; the NEW addition "This derivative is not an operator-norm derivative on the whole phase" matches the OLD intent.
- Lost steps/qualifiers: none identified within this read. Pre-existing concerns: none.

## P:compact-F-projection
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: Block formula \eqref{E:compact-F-block} follows from substituting the free-Duhamel identity for $P_\sigma^E(t-r)g(r)$ and exchanging the triangle $0\le r\le s\le t$; the NEW description of the region is exact and the exchange is justified by bounded norms (absolute Bochner convergence in $E$). $Y$ solves free Duhamel with force $B_\sigma^EY+g$; taking $g=D_\sigma C(r)c$ and adjoining $C(t)c$ reproduces the $F$ Duhamel equation up to uniqueness. Dual computation: $\ell_\sigma^ED_\sigma C(r)c=f_\sigma(c_1+rc_2)$ with $f_\sigma=\int V_\sigma p_\sigma/(2\lambda_\sigma)>0$ (finite by Cauchy--Schwarz, positive by $V_\sigma\ne0$ and $p_\sigma>0$ a.e.; no $L^1$ of $p_\sigma$ used). The NEW exponential-integral values $\int_0^\infty e^{-\lambda r}=1/\lambda$ and $\int_0^\infty re^{-\lambda r}=1/\lambda^2$ produce $\ell_\sigma^C(c)=f_\sigma(c_1/\lambda+c_2/\lambda^2)$; the tail identity $\ell_\sigma^C(C(t)c)=\int_t^\infty e^{\lambda(t-r)}f_\sigma(c_1+rc_2)dr$ I verified by translating $r\mapsto r+t$. The eigenrelation $\ell_\sigma P_\sigma(t)=e^{\lambda t}\ell_\sigma$ follows by splitting the growing dual into $[0,t]$-integral (from $\ell^EP^E(t-r)=e^{\lambda(t-r)}\ell^E$) plus the shifted tail. Margins $\ell_\sigma(e_0)=f_\sigma/\lambda_\sigma>0$ and $O_\phi(e_\sigma)=\int\phi p_\sigma>0$ are integral identities (no point trace/1D ODE), and compactness gives positive uniform infima; the NEW positivity gloss ($\phi>0$ on a positive-measure set, $p_\sigma>0$ a.e.) is correct.
- Lost steps/qualifiers: none identified within this read. Pre-existing concerns: none.

## P:compact-F-complement
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The exact complementary $E$-component \eqref{E:compact-complement-forcing} I reconstructed: subtracting $P_\sigma(t)\Pi_\sigma$ and rewriting the growing part of $\int_0^t P^E(t-r)D C(r)c\,dr$ as $e_\sigma^E[\int_0^t e^{\lambda(t-r)}f_\sigma(c_1+rc_2)dr]$ yields $-e_\sigma^E\ell_\sigma^C(C(t)c)$ after absorbing $\int_t^\infty$; constant component stays $C(t)c$. Convolution bound: $\|Q_\sigma^ED_\sigma C(r)\|\le C(1+r)$ (via $\|V_\sigma w\|_{H^{-1/2}}\le\|V_\sigma\|_2|w|\le M|K_x|^{1/2}(1+r)|c|$), so the integrand is bounded by $Ce^{\mu(t-r)}(1+t-r)(1+r)\le Ce^{\mu t}(1+t-r)(1+r)$ (using $\mu\ge0$); the NEW explanation of the two linear factors matches. The integral equals $t+t^2+t^3/6$ (I expanded $(1+t-r)(1+r)=1+t+tr-r^2$ and integrated), hence $C(1+t)^3e^{\mu t}$. Normalization: $e^{-\lambda t}e^{\mu t}\le e^{-d_0t}$ and $(1+t)^3e^{-(d_0-\eta)t}$ is bounded for $\eta<d_0$; NEW spelling-out correct. Parameter dependence: subtracting free-Duhamel equations gives the two integrals; one is $\le C\int_0^t\|P_\sigma(r)-P_\tau(r)\|dr$, the other $\le Cd_{\sigma,\tau}\sup_r\|P_\tau(r)\|$; measurability of the operator norm via a countable dense set avoids any $\mathcal B(F)$-valued derivative, exactly as OLD states.
- Lost steps/qualifiers: none identified within this read. Pre-existing concerns: none.

## L:compact-raw-profile
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The mean floor: since $|\sigma-u|^{-a}\ge1$ on $[0,1]^2$ (as $|\sigma-u|\le1$ and $-a<0$), $h_\sigma\ge\int_0^1(\Gamma*\Psi(u,\cdot))du=\Gamma*\bar q$; hence $v_\Psi\ge\int\Psi(\sigma,x)(\Gamma*\bar q)(x)dx\,d\sigma=Q(\bar q)$ by Tonelli and the substitution $x\mapsto x-z$. Positivity of $Q(\bar q)$: homogeneity $\Gamma(B_r)=r^{d-\alpha}\Gamma(B_1)$ with $\Gamma(B_1)>0$ (from $\Gamma\ne0$ charging some ball); the autocorrelation $r(z)=\int\bar q(x)\bar q(x-z)dx$ is continuous with $r(0)=\|\bar q\|_2^2>0$, hence $\ge\delta>0$ on a ball of positive $\Gamma$-mass. The NEW explanations of these two points are correct, and — per the required distinction — neither OLD nor NEW asserts pointwise positivity of the profile $\Gamma*\bar q$, only its nonnegativity/nonzero-ness plus strict positivity of the cost. Finiteness via $\|\Psi\|_\infty^2|B_A|\Gamma(\bar B_{2A})$ and $\int_0^1\int_0^1|\sigma-u|^{-a}=2/((1-a)(2-a))$ is unchanged. Smoothness: after extending $\Psi$ by zero in time, every $\sigma$-derivative is moved onto the compact test by translation invariance ($\partial_\sigma=-\partial_u$ then integration by parts, no boundary terms since $\Psi\in C_c^\infty((0,1)\times\R^d)$ is compactly supported strictly inside the open time interval), so $h$ is smooth and genuinely Lipschitz in $\sigma$; the "differentiate the test, not the singular kernel" remark is the operative argument. Compactness of $V_\sigma=m_Rh_\sigma$ comes from $m_R$, not from $h$.
- Lost steps/qualifiers: none identified within this read. Pre-existing concerns: none. (I initially probed the $\sigma$-Lipschitz claim; the open-interval compact support of $\Psi$ in time resolves the would-be boundary singularity at $\sigma=0,1$.)

## P:compact-original-common-trial
- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: Dilated unit trial $\psi_L=L^{-d/2}\psi(x/L)$ (Lebesgue $L^2$-normalization); on $B_L$, $\psi_L^2\ge c_0^2L^{-d}$. The exact Radon-vs-Lebesgue pairing: $\int_{B_L}(\Gamma*\bar q)=\int\bar q(y)\Gamma(B_L-y)dy\ge\int\bar q(y)\Gamma(B_{L/2})dy$, using $B_{L/2}\subset B_L-y$ for $|y|\le A\le L/2$; homogeneity gives $\Gamma(B_{L/2})=(L/2)^{d-\alpha}\Gamma(B_1)$, so the potential term is $\ge c_0^22^{\alpha-d}\Gamma(B_1)(\int\bar q)L^{-\alpha}=C_\Gamma L^{-\alpha}$, matching \eqref{E:compact-trial-potential}; the NEW Step-1 spelling of this is exact. Kinetic energy $\|\nabla\psi_L\|^2=L^{-2}D_\psi$; $\alpha<2$ selects $L$ with $\varepsilon_R=C_\Gamma L^{-\alpha}-D_\psi L^{-2}>0$, uniform over $\sigma\in I$, then $R$ (or enlarged $R$) is fixed *before* invoking \eqref{E:compact-common-trial} and Proposition 1. Rate Lipschitz: $|\lambda_\sigma-\lambda_\tau|=|E_1(\sigma)-E_1(\tau)|/(\lambda_\sigma+\lambda_\tau)\le\|V_\sigma-V_\tau\|_\infty/(2\sqrt{\varepsilon_R})$, using $\lambda_\sigma,\lambda_\tau\ge\sqrt{\varepsilon_R}$; the NEW denominator explanation is correct, and Lipschitz-ness of $V$ in $\sigma$ feeds in via Lemma 6 as justified above. $\lambda_0>0$ because $E_1(0)\le-\varepsilon_R<0$ (the mean integrates the full time test, not point values). Fixed-$\Psi$/fixed-$Z$/fixed-$v_\Psi$ preservation, the no-all-strength caveat, and "masks fixed before source/time asymptotics" are all retained verbatim.
- Lost steps/qualifiers: none identified within this read. Pre-existing concerns: none.

## AUDIT dispositions
No rewrite-introduced defects found in any of the seven proofs. No lost steps, qualifiers, hypotheses, or equation labels. All NEW explanatory insertions are locally justified by the surrounding argument, the stated identities, or the supplied hypotheses. No AUDIT action is required.

## Findings and limits
The review is confined to the seven assigned proofs and their unchanged statements; upstream baseline proofs (constant-phase Young, covariance foundation, compact Gaussian) were consulted only as stated inputs/definitions for target-application hypotheses (in particular the phase space $F=E\oplus\R^2$, the $B_F$ bound $\|B_F(h)\|\le\|h\|_\infty+\|h\|_2$, the observable $O_\phi(e,c)=\langle e_1,\phi\rangle+c_1$, and Hypothesis \ref{H:homog}) and were not counted as additional reviewed proofs. I did not certify primary Teschl citations, the Young/PDF sources, source images, Lean correspondence, or rendered pages. Line ranges were read per the inventory's local-LF convention and cross-checked against the embedded raw files; the statements are verbatim identical and the proof bodies differ only by structuring and explanation. No tools, browsing, edits, or external communication were used.
