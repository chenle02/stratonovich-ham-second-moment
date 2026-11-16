# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

The seven assigned proofs were each reconstructed with public working. All seven statements/definitions (OLD 33–44 vs NEW 33–44, 69–87 vs 69–87, 212–231 vs 246–265, 284–302 vs 335–353, 338–358 vs 404–424, 419–429 vs 504–514, 461–490 vs 546–575) are textually identical. The NEW proofs are verbatim the OLD deductions interleaved with roadmap sentences and `\textit{Step N.}` headings; two proofs (L:uniform-E-lift, C:uniform-polynomial-balls) have no structural additions at all. The three genuinely new deterministic sentences (the added static-baseline identity, the added `$K(s)+2$` bound, the added `$A_{\rm prod}\ge1$` max-preservation sentence) were each checked and are correct consequences of the surrounding deductions. No mathematical step, hypothesis, qualifier, exponent, prefactor or limit order was lost; no unjustified new assertion was found.

---

## L:uniform-E-lift

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (none added; the proof is text-identical, OLD 46–67 = NEW 46–67)

**Original-step coverage.** (1) Zero covariance: `$L=M=V=L_F=0$` gives all claims. (2) If `$L_n^E\to L$` in the operator-norm closure `$\mathcal V_{E,R}\subseteq\mathcal K(E)$`, the zero second column persists and `$M_n\to M$` in `$\mathcal L(H^{1/2},H^{-1/2})$`, with `$\|L\|=\|M\|=:k$`. This equality holds because `$L(u,v)=(0,Mu)$` depends only on the `$H^{1/2}$` slot, so the `$E$`-norm supremum over the full pair reduces to the `$H^{1/2}\to H^{-1/2}$` norm of `$M$`. (3) Fix real compact smooth `$\chi_R=1$` near `$\operatorname{supp}m_R$`; since `$M_n\chi_R=V_n$` (multiplication `$V_n=m_R(\Gamma*q_n)$` vanishes where `$\chi_R=1$` is not needed, and equals `$V_n$` on its support), `$\|V_n-V_j\|_{H^{-1/2}}\le\|\chi_R\|_{H^{1/2}}\|M_n-M_j\|$`. Hence `$V_n\to V$` in `$H^{-1/2}$` with support in `$\operatorname{supp}m_R$` (test against functions supported outside). (4) Smooth multiplication bounded on `$H^{-1/2}$` identifies `$Mu=Vu$` on compact tests, then by density on `$H^{1/2}$`; `$M\chi_R=V$` gives uniqueness. (5) Symmetry and `\eqref{E:uniform-E-pairing}` pass to the limit. (6) The `$F$` lift operators `$(u,v,c_1,c_2)\mapsto(0,M_nu+c_1V_n,0,0)$` have differences bounded by `$(1+\|\chi_R\|_{H^{1/2}})\|M_n-M_j\|$` (the `$c_1$` column contributes `$|c_1|\|V_n-V_j\|$` under the `$F$`-norm with `$|c_1|\le1$`), so they converge in the old `$F$` class; the `$R$`-dependent constant enters no uniform estimate. (7) Dense smooth controls plus bounded completion of `$T_R$` put all completed mean fields in `$\mathcal V_{E,R}$` a.e.; Bochner averages preserve the closed linear class; complexification preserves `$k$` by real/imaginary splitting. All steps check. The only mildly compressed appeal is "dense smooth original controls... lie in `$\mathcal V_{E,R}$`": this follows because `$\mathcal V_{E,R}$` is by definition the operator-norm closure of `$L_q^E$` and `$T_R$` is that bounded completion — valid, and unchanged between revisions.

**Evidence.** The lift norm bound `$(1+\|\chi_R\|_{H^{1/2}})\|M_n-M_j\|$` is verified entrywise; the identification `$M\chi_R=V$` uses `$V$` supported in `$\operatorname{supp}m_R$` and `$\chi_R=1$` there. No step or qualifier differs between OLD and NEW.

---

## P:uniform-E-spectral

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** The NEW proof (89–236) reorganizes the OLD (89–202) into Steps 1–6, plus one added identity sentence; no deduction was removed.

Step 1 (form): With `$b=\|u\|_2$`, `$z=\|u\|_{H^1}$`, Fourier Cauchy–Schwarz gives `$\|u\|_{H^{1/2}}^2\le bz$`; the pairing bound and weighted AGM give `$|v_V(u,u)|\le Kbz\le z^2/2+K^2b^2/2$`; hence the two-sided budget `\eqref{E:uniform-E-form-budget}`. The lower bound dominates `$2b^2$` because `$z\ge b$`, `$K\ge1$`. The cited Teschl Thm 2.14/3.6 gives the closed semibounded form, `$A=H_V+c\ge2$`, `$D(A^{1/2})=H^1$`; bounded spectral slices below 2 would contradict the form bound.

Step 2 (quarter-power): with `$B_0=1-\Delta$`, `$L_K=3(1+K^2)$`, the completing-the-square resolvent comparison, the identity `$\sqrt x=\pi^{-1}\int_0^\infty t^{-1/2}x/(x+t)\,dt$` (verified: `$t=xv^2$` gives `$\pi^{-1}2\sqrt x\int_0^\infty(1+v^2)^{-1}dv=\sqrt x$`), and Tonelli yield `$D(A^{1/4})=H^{1/2}$` with `$2^{-1/4}\le$` ratio `$\le L_K^{1/4}$`; the dual `$\|A^{-1/4}v\|_2$` with equality test `$u=A^{-1/2}v$` completes `$H^{-1/2}$`; condition cost `$M_K^2=\sqrt{3(1+K^2)}\le2(1+K)$`.

Step 3 (bottom): `$q_V\ge z^2/2-1-K^2/2\ge -K^2$`; a dilated unit bump translated off `$\operatorname{supp}m_R$` gives `$\beta\le0$`; real/complex infima agree by convex-splitting of complex diagonals; bounded spectral slices identify `$\beta=\inf\operatorname{spec}H_V$`; the PVM-support/resolvent argument gives `$\lambda\le K$` and `$h+c\ge2$` on the spectrum.

Step 4 (wave matrix): In the `$E_A$` isometry the matrix is
`$\begin{pmatrix}\mathrm{Cos}_t(h)&\sqrt{h+c}\,\mathrm{Sin}_t(h)\\ -h\,\mathrm{Sin}_t(h)/\sqrt{h+c}&\mathrm{Cos}_t(h)\end{pmatrix}$`.
I verified the entries: on an `$h$`-fiber `$A=h+c$`, `$\tilde u=A^{1/4}u$`, `$\tilde v=A^{-1/4}v$` gives upper `$(h+c)^{1/4}(1/\sqrt h)(h+c)^{1/4}\sin=\sqrt{h+c}\,\sin/\sqrt h$` and lower `$-\sqrt h\sin(h+c)^{-1/2}=-h\,\mathrm{Sin}_t/\sqrt{h+c}$`. For `$h\ge0$`: upper `$\le1+\sqrt c\,t$` (via `$\sqrt{h+c}\le\sqrt h+\sqrt c$`), lower `$\le1$`, at zero `$(\sqrt c\,t,0)$`. For `$\beta\le h<0$`: `$|\mathrm{Cos}_t|\le e^{\lambda t}$`, `$|\mathrm{Sin}_t|\le te^{\lambda t}$`, upper `$\le\sqrt c\,te^{\lambda t}$` (since `$h+c\le c$`), lower `$\le Ke^{\lambda t}$` (since `$\sqrt{-h}\le K$`, `$\sqrt{h+c}\ge\sqrt2$`). With `$\sqrt c\le2K$` each entry `$\le2(1+K)(1+t)e^{\lambda t}$`; matrix norm `$\le$` twice that, condition cost `$M_K^2$` gives `$8(1+K)^2(1+t)e^{\lambda t}$`, matching `\eqref{E:uniform-E-static-bound}`.

Step 5 (identification): the fixed-`$R$` lift belongs to the class of P:signed-physical-wave; same form `$q_V$`, same self-adjoint representative, Cos/Sin equality on cutoffs, boundedness extends to all `$E$`; compact `$L$` makes the conjugation norm-continuous (finite-rank + strong continuity), so the Young equation is the bounded-interaction equation (P:constant-young-linear). The **added sentence** states the static baseline `$S_E(t)U_H(t,0)=P_V^E(t)$` with `$H(u)=\int_0^u S_E(-v)LS_E(v)\,dv$`. This is exactly the identification just established (the physical flow equals the spectral wave), so the addition is justified; it is the sentence P:uniform-mean-product later cites as "the baseline is the static wave".

Step 6 (rate continuity): an `$\varepsilon$`-minimizer for `$W$` has `$q_W\le\beta(W)+\varepsilon\le1$`; `$z^2-1-Kz\le1$` has positive root `$(K+\sqrt{K^2+8})/2\le K+2$`; multiplier difference changes the form by `$\le\|L_V-L_W\|\|u\|_{H^{1/2}}^2\le(K+2)\|L_V-L_W\|$`; infima, `$\varepsilon\downarrow0$`, reversal, and `$|\sqrt x-\sqrt y|\le\sqrt{|x-y|}$` on nonnegative `$-\beta$` give `\eqref{E:uniform-E-rate-continuity}` with no bottom eigenstate. Zero covariance is the free case.

**Evidence.** All quantitative constants use only the `$E$` multiplier norm `$k=\|L\|$`; the fixed-radius lift `$L_F$` and its `$\chi_R$` constant appear only in Step 5 (identification), matching the stated "used only for identification" and the assigned check "quantitative spectral/wave/rate estimates use E norms alone." Form domain, quarter-power comparison, spectral slices, real/complex infima and the approximate-minimizer argument are all present and correct.

---

## P:uniform-rate-averaging

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** Step 1: Bochner averaging is a contraction on `$L^r(I;\mathscr Z)$` by Jensen; on continuous fields the error is bounded by the modulus of continuity at the mesh; simple-field/indicator density gives strong convergence; compactness of `$C_t:H_t\to L^r(I)$` (upstream, fixed `$r\in(2,2/a)$`) makes `$C_t(B_1)$` relatively compact, so a finite net plus `$\|\mathcal A_\delta-I\|\le2$` gives uniform convergence on the unit ball, i.e. `$\omega_\delta\to0$` at fixed `$B$`. Step 2: the diagonal identity `$\mathcal A_\delta^{\mathcal K(E)}T_R(C_t\otimes I)\Phi=T_R((\mathcal A_\delta C_t)\otimes I)\Phi$` on finite tensors extends via the dimension-free tensor bound (L:uniform-mean-tensor) and `$\|T_R\|\le M_0$`, giving `$\|\overline W_R-W_R\|_{L^r}\le M_0M\omega_\delta=\Omega_\delta(M)$` and `$\|W_R\|_{L^r},\|\overline W_R\|_{L^r}\le Z$`; the explicit non-compactness disclaimers are retained. Step 3: pointwise `\eqref{E:uniform-E-rate-continuity}` with `$K(s)=\max(1,\|W_1(s)\|,\|W_2(s)\|)$` and the **added** `$K(s)+2\le3+\|W_1(s)\|+\|W_2(s)\|$` (correct, since `$\max(1,a,b)\le1+a+b$`) yields, via Cauchy–Schwarz,
`$\int_I|\lambda(W_1)-\lambda(W_2)|\le\sqrt{3+\|W_1\|_{L^1}+\|W_2\|_{L^1}}\sqrt{\|W_1-W_2\|_{L^1}}$`.
For `$W_1=W_R$`, `$W_2=\overline W_R$`: `$\|W_R\|_{L^1},\|\overline W_R\|_{L^1}\le Z$` (since `$|I|=1$`, `$L^r\subset L^1$`), so the bound is `$\sqrt{3+2Z}\sqrt{\Omega_\delta(M)}=\Lambda_\delta(M)\to0$`; rate finiteness follows from `$\lambda(L)\le\max(1,\|L\|)$` and `$\|\mathcal T_R\Phi\|_{L^r}\le C_{\rm mean}\|\Phi\|$`; the same estimate also establishes continuity of `$\mathrm{Rate}_R$` in `$\Phi$`. Uniformity in `$R$`: `$M_0$` and `$C_{\rm mean}$` are `$R$`-independent and `$\omega_\delta$` does not involve `$R$`.

**Evidence.** The full chain `$\mathcal A_\delta$`-identity → `\eqref{E:uniform-field-averaging}` → rate comparison → `\eqref{E:uniform-rate-averaging}` was reconstructed with exact constants, and the scalar-time compactness is used only for `$\omega_\delta\to0$` (the tensor map `$A\otimes I$` is explicitly not asserted compact), matching the assigned check.

---

## L:uniform-product-budgets

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** Step 1 (free group and primitive): in balanced coordinates the free matrix has upper entry `$\langle k\rangle\sin(vk)/k$` (bounded by `$\sqrt2B$`: `$\sqrt{1+k^2}/k\le\sqrt2$` for `$k\ge1$` and `$|\sin(vk)|/k\le B$` for `$k\le1$`), lower `$-k\sin(vk)/\langle k\rangle$` (bounded by 1), diagonals 1; at zero the off-diagonals are `$(v,0)$`. Frobenius squared is `$\le2\cos^2+2B^2+1\le3+2B^2$` (two diagonal squares, upper square `$\le2B^2$`, lower square `$\le1$`), so `$G_B\le\sqrt{3+2B^2}\le3B$`; `$G_B\ge1$` since `$S_E(0)=I$`. Then `$C_B=G_B^2[B^{1-1/r}+B^{1-1/r-\theta}]\le9(B^{3-1/r}+B^{3-1/r-\theta})\le18B^{3-1/r}\le32B^{3-1/r}$`, and `$C_BB^{1/r}=G_B^2(B+B^{1-\theta})\ge B$`. The primitive bound `$\|H_m\|_\theta\le a_m$`: the sup part is `$\le G_B^2B^{1-1/r}\delta^{-1/r}\|W_R\|_{L^r(I_m)}$` and the `$\theta$`-seminorm part `$\le G_B^2B^{1-1/r-\theta}\delta^{-1/r}\|W_R\|_{L^r(I_m)}$` (Hölder in time with `$1-1/r>\theta$`, `$\delta^{-1/r}$` from the affine change of time, constant stopping), matching the upstream explicit constant `$C_{B,E}=G_B^2[B^{1-1/r}+B^{1-1/r-\theta}]$` of P:uniform-actual-cameron. Then `$\delta\sum a_m^r=C_B^r\|W_R\|_{L^r}^r$` exactly (true partition, empty cell zero). Step 2 (Young growth): with `$d=\|D\|_\theta$`, `$c_\theta=2\max(1,C_{\rm Young})$`, if `$c_\theta dB^\theta\le1/4$` the whole-interval contraction gives `$\log\sup\|U_D\|\le\log(4/3)<1/2$`; otherwise at most `$\lceil B(4c_\theta d)^\nu\rceil\le2B(4c_\theta d)^\nu$` pieces of local norm `$\le4/3$` give `$\log\sup\|U_D\|\le2B(4c_\theta d)^\nu\log(4/3)$`. Combining with `$\log G_B\le\log(3B)$` and absorbing `$\log(3B)+1/2\le4B$` (`$B\ge1$`), the choice `$C_{\rm gr}=4+\log4+2(4c_\theta)^\nu$` satisfies both cases, giving `\eqref{E:uniform-product-growth}`; this is generic algebra on `$\mathcal L(E)$` (multiplication norm one), hence no Gaussian/Hamiltonian hypothesis. Step 3 (endpoint lower bound): `$W_R\in L^r(I;\mathcal K(E))$` (upstream), compact conjugation plus compact Bochner integration make `$H_m$` a compact-valued `$C^\theta$` path starting at zero, so L:symplectic-free gives `$\|P_m^{\rm mean}\|\ge\|S_E(\ell_m)\|\ge1$`; empty endpoint is `$I$`.

**Evidence.** `$G_B\le3B$`, `$C_B\le18B^{3-1/r}\le32B^{3-1/r}$`, `$C_BB^{1/r}\ge B$` and the explicit `$C_{\rm gr}$` are all reconstructed; the contraction-piece count matches L:young-upper-growth's `$n_D$` computation, and compactness is used only for the endpoint lower bound, as the new roadmap states.

---

## P:uniform-mean-product

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (headings/roadmap only)

**Original-step coverage.** Step 1 (freezing errors): `$e_m=C_B\delta^{-1/r}\|W_R-\overline W_R\|_{L^r(I_m)}$`; Jensen/modulus gives `$\|\overline H_m\|_\theta\le a_m$`, `$\|H_m-\overline H_m\|_\theta\le e_m$`; `$\delta\sum e_m^r\le C_B^r\Omega_\delta(M)^r$`, `$\delta\sum a_m^r\le D_M:=C_B^rZ^r$`. Finite power mean at exponents `$r$` and `$r/\nu>1$` (inputs `$e_m,e_m^\nu$`, `$\delta n\le2/B$`) gives `$\delta\sum(e_m+e_m^\nu)\le E_\delta$`; both terms verified with the `$(\delta n)^{1-1/r}$` and `$(\delta n)^{1-\nu/r}$` factors. Step 2 (good full blocks): full cells have `$\ell_m=B$`; `$\|\overline M_m\|\le(\delta B)^{-1/r}\|W_R\|_{L^r(I_m)}=a_m/(C_BB^{1/r})\le a_m/B$` using `$C_BB^{1/r}\ge B$`. On `$a_m\le K$`, P:young-upper-multiplicative with base `$\overline H_m$`, perturbation `$H_m-\overline H_m$`, left multiplier `$S_E(B)$` gives `$\|S_E(B)U_{H_m}(B,0)\|\le\|S_E(B)U_{\overline H_m}(B,0)\|e^{C(\theta,B,K)(e_m+e_m^\nu)}$`; the static baseline identity (from P:uniform-E-spectral) and `$\|\overline M_m\|\le K$` give the baseline `$\le8(1+K)^2(1+B)e^{B\lambda(\overline M_m)}$`, so `$\log\|P_m^{\rm mean}\|\le L_{B,K}+B\lambda(\overline M_m)+C(\theta,B,K)(e_m+e_m^\nu)$` with `$L_{B,K}=\log16+4\log(1+K)+3\log(1+B)$` (indeed `$\log8+2\log(1+K)+\log(1+B)\le L_{B,K}$`). Since `$\delta N\le1/B$`, prefactors sum to `$\le L_{B,K}/B$`; nonnegativity of `$\lambda$` and `\eqref{E:uniform-rate-averaging}` give `$\delta\sum_{\rm good}B\lambda(\overline M_m)\le\mathrm{Rate}_R(\Phi)+\Lambda_\delta(M)$`. Step 3 (bad full blocks): `\eqref{E:uniform-product-growth}` gives `$C_{\rm gr}B(1+a_m^\nu)$`; `$a_m>K\ge1$`, `$r>\nu$` give `$1+a_m^\nu\le(K^{-r}+K^{\nu-r})a_m^r$`; weighted sum `$\le C_{\rm gr}BC_B^rZ^r(K^{-r}+K^{\nu-r})\le C_{\rm gr}32^rZ^rB^{3r}(K^{-r}+K^{\nu-r})$` using `$C_B\le32B^{3-1/r}$` (hence the displayed exponent `$3r=1+r(3-1/r)$`). Step 4 (last cell): if `$\ell_N=0$`, `$\log\|I\|=0$`; otherwise `$a_N\le C_B\delta^{-1/r}Z$` and `\eqref{E:uniform-product-growth}` gives `$\delta\log\|P_N^{\rm mean}\|\le C_{\rm gr}B[\delta+C_B^\nu Z^\nu\delta^{1-\nu/r}]=\mathrm{Last}_\delta\to0$` since `$\nu<r$`; no division by `$\ell_N$`. All four contributions assemble into `\eqref{E:uniform-mean-product}`; constants independent of `$R$`.

**Evidence.** Good/bad split, both bad exponents `$K^{-r},K^{\nu-r}$`, the `$32^rB^{3r}$` prefactor, the true-last-cell estimate and the empty-cell case are each independently verified; the perturbation error `$E_\delta$` and the rate error `$\Lambda_\delta(M)$` enter exactly once each. No change from OLD beyond headings.

---

## C:uniform-polynomial-balls

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (none added; proof text-identical, OLD 431–452 = NEW 516–537)

**Original-step coverage.** Take `$s>r(3+\kappa_{\rm ball})/(r-\nu)$` and `$K_B=B^s$`, `$M_B=c_{\rm ball}B^{\kappa_{\rm ball}}$`, `$Z=C_{\rm mean}M_B$`. The bad-block term becomes `$C_{\rm gr}32^rC_{\rm mean}^rc_{\rm ball}^r\{B^{r(3+\kappa_{\rm ball})-sr}+B^{r(3+\kappa_{\rm ball})+s(\nu-r)}\}$` (verified by expanding `$B^{3r}B^{\kappa r}Z^{-sr}$`-type powers; the second exponent is negative by the choice of `$s$`, the first because `$s>3+\kappa_{\rm ball}$`, the latter following from `$r/(r-\nu)>1$`). Also `$L_{B,K_B}/B\le[\log16+7\log2+(4s+3)\log B]/B\to0$` (using `$1+B^s\le2B^s$`, `$1+B\le2B$`). The three `$\delta$`-vanishing errors vanish at fixed finite `$B,M_B,K_B$`. No diagonal `$(B_\delta,M_\delta)$` choice is asserted. The continuity/separability observations: primitive maps are bounded linear into separable little-Hölder products; Young local Lipschitz dependence and positive endpoint norms make `$\log\|P_m^{\rm mean}\|$` continuous; rate continuity is from P:uniform-rate-averaging; growth bounds make each control-ball supremum finite; a countable dense subset of the closed `$M_B$`-ball carries the same supremum; the `$\sup_{R\ge1}$` is an ordinary deterministic supremum.

**Evidence.** Both negative exponents and the `$L_{B,K_B}/B\to0$` estimate are checked; the successive `$\delta\downarrow0$` then integer-`$B\to\infty$` limits are respected, with no diagonal-limit claim.

---

## P:uniform-arbitrary-residual

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Original-step coverage.** Step 1 (ratios): all endpoint norms are positive by Young/free inverses. On good cells `$a_m\le K_{\rm res}$`, P:young-upper-multiplicative with base `$H_m$` (`$\|H_m\|_\theta\le a_m\le K_{\rm res}$`), perturbation `$x_m$` (`$v_m=\|x_m\|_\theta$`), left multiplier `$S_E(\ell_m)$` gives `$\log(\|P_m^{\rm pert}\|/\|P_m^{\rm mean}\|)\le C(\theta,B,K_{\rm res})(v_m+v_m^\nu)$`. On bad cells `$a_m>K_{\rm res}$`, `\eqref{E:uniform-product-growth}` and `$(a_m+v_m)^\nu\le2^{\nu-1}(a_m^\nu+v_m^\nu)$` (convexity, `$\nu>1$`) and `$\|P_m^{\rm mean}\|\ge1$` give `$\log$`-ratio `$\le c_B(1+a_m^\nu+v_m^\nu)$` with `$c_B=2^{\nu-1}C_{\rm gr}B$`. Enlarging `$C_{K_{\rm res}}$` to dominate `$c_B$` and summing (with `$\log\max(1,z_{\rm rat})\le\sum_m\max(0,\log\text{ratio}_m)$`) gives the displayed sum bound. The bad budget: `$1+a_m^\nu\le(K_{\rm res}^{-r}+K_{\rm res}^{\nu-r})a_m^r$`, so `$\delta\sum_{\rm bad}(1+a_m^\nu)\le D_M(K_{\rm res}^{-r}+K_{\rm res}^{\nu-r})$`. Power means at exponents `$p\ge1$` and `$p/\nu\ge1$`: `$\delta\sum v_m\le(2/B)^{1-1/p}Y$` and `$\delta\sum v_m^\nu\le(2/B)^{1-\nu/p}Y^\nu$` (verified via `$Y^p=\delta\sum v_m^p$` and `$\delta n\le2/B$`); the case `$p=\nu$` makes `$p/\nu=1$` an equality, and zero entries/empty blocks are covered by positive exponents — no singular powers. This proves `\eqref{E:uniform-residual-ratio}`. Step 2 (ordered product and limits): `$A_{\rm prod}:=\prod_m\|P_m^{\rm mean}\|\ge1$`; submultiplicativity (no commutation) gives `$\|P_N^{\rm pert}\cdots P_0^{\rm pert}\|\le A_{\rm prod}z_{\rm rat}$`. The **added** sentence `$\max(1,A_{\rm prod}z_{\rm rat})\le A_{\rm prod}\max(1,z_{\rm rat})$` is verified (`$z_{\rm rat}\ge1$`: equality; `$z_{\rm rat}<1$`: LHS `$=1\le A_{\rm prod}$`), so `$\max(1,\|\prod P^{\rm pert}\|)\le A_{\rm prod}\max(1,z_{\rm rat})$` and `$\mathcal F-2\delta\sum_m\log\|P_m^{\rm mean}\|\le2\delta\log\max(1,z_{\rm rat})$`. At fixed `$B,M,K_{\rm res}$` the residual terms vanish on `$Y\le b_\delta$`; taking `$\delta\downarrow0$` first, then `$K_{\rm res}\to\infty$` (using `$r>\nu$`), the residual excess has limsup `$\le0$` uniformly in `$R,\Phi$`; with `$M=M_B$` and C:uniform-polynomial-balls, "sup of sums ≤ sum of suprema," and the outer `$B\to\infty$` limit gives `\eqref{E:uniform-residual-integrated-rate}`. No Gaussian/Cameron/Hamiltonian condition; nothing was multiplied as scalar displacement moments (the comparison is `$2\delta\log\max(1,\|\cdot\|)$` of an ordered noncommuting product); successive `$\delta$`, then `$K_{\rm res}$`, then `$B$` limits are explicit.

**Evidence.** Little-Hölder compact residual paths, the `$p=\nu$` boundary, the `max(1,·)` and factor-2 bookkeeping, the `$2^{\nu-1}$` convexity constant, and the three-level limit order are all reconstructed and correct; the added sentence is a true inequality, not a new hypothesis.

---

## AUDIT dispositions

No AUDIT comments or markers remain in either revision of this module. I found no AUDIT-worthy defect introduced by any rewrite. The only mildly terse pre-existing points (unchanged in both revisions) are: (i) L:uniform-E-lift's one-sentence "dense smooth original controls and bounded completion" claim, which is definitionally sound; (ii) the primitive Hölder estimate `\eqref{E:uniform-product-primitive}` compressed to one sentence, but fully consistent with (and verifiable against) the explicit `$C_{B,E}$` computation in the upstream unassigned P:uniform-actual-cameron; neither rises to an audit-level issue.

## Findings and limits

All seven assigned proof pairs preserve their mathematics: the NEW revision is additive (roadmaps + Step headings + three checked explanatory sentences) with identical statements and no lost steps, hypotheses or qualifiers. The specific mandated checks — `$E$`-norm-only quantitative constants with the fixed-radius `$F$` lift confined to identification; form domain and quarter-power comparison; bounded spectral slices; real/complex infima; approximate-minimizer rate continuity without a bottom eigenstate; scalar-time compact averaging vs dimension-free tensor extension; exact integrated rate error and `$R$`-uniform bounds; free-group/primitive/generic Young constants `$G_B\le3B$`, `$C_B\le18B^{3-1/r}\le32B^{3-1/r}$`, `$C_BB^{1/r}\ge B$`, explicit `$C_{\rm gr}$`; good/bad full-cell budgets with both exponents `$K^{-r},K^{\nu-r}$`; true last/empty cell; polynomial-ball thresholds `$s>r(3+\kappa)/(r-\nu)$`, `$K_B=B^s$`; finite/dense-ball suprema and successive `$\delta,B$` limits; arbitrary little-Hölder residual ratios including `$p=\nu$`; ordered noncommuting product with `max(1,·)` and factor 2; successive `$\delta,K_{\rm res},B$` limits — were all verified with public working. I did not certify the upstream unassigned theorems (Teschl form/spectral calculus; P:signed-physical-wave; P:constant-young-linear; L:young-upper-growth; P:young-upper-multiplicative; L:symplectic-free; P:uniform-mean-regulator; L:uniform-mean-tensor; P:cameron-*): their proofs are not assigned and were used only under their checked hypotheses. Forward references (Sections S:actual-gaussian-tubes–S:intrinsic-second-moment) were not counted as assigned proofs. No unitary-Fourier inversion kernel appears in the assigned proofs, so no normalization was at risk there. Reading is COMPLETE and public reconstruction is COMPLETE for all seven labels.
