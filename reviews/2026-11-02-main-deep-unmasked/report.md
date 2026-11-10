# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. No false identity, sign error, incorrect constant, hidden hypothesis, boundary-term fault, or invalid interchange was found in PROOF127–132. The auxiliary label-one score $S_1^{\mathrm{pos}}$ is nowhere identified with a first moment or with any Chen constant (this is asserted and respected). The independent finiteness input is the actual `T:full-upper` (same canonical solution), not the final intrinsic theorem.

## Noncritical findings

1. **PROOF129 (Lipschitz constant).** The Lipschitz constant $C_\Psi/(2\sqrt{\varepsilon_0})$ for $\lambda_{\Psi,s}$ depends on the fixed margin $\varepsilon_0$ supplied by the common trial in `P:compact-original-common-trial`. That margin is $\Psi$-dependent (it is $\varepsilon_R = C_\Gamma L^{-\alpha}-D_\psi L^{-2}$ for a specific trial $\psi_L$) but otherwise a legitimate fixed constant. No error; worth stating once that $\varepsilon_0$ is fixed by the trial, not by a mask parameter that later changes.

2. **PROOF127 (peak at zero).** The conclusion $0\le(\Gamma*p_\varepsilon)(x)\le(\Gamma*p_\varepsilon)(0)$ is only an inequality, obtained from $\operatorname{Re}\int e^{i\xi\cdot x}e^{-\varepsilon|\xi|^2/2}\mu(d\xi)=\int\cos(\xi\cdot x)e^{-\varepsilon|\xi|^2/2}\mu(d\xi)\le\int e^{-\varepsilon|\xi|^2/2}\mu(d\xi)$. This uses evenness of $\mu$ (from `H:homog`) and $\cos\le1$; it is not an assertion of radial monotonicity. Correct, and it is correctly not used as monotonicity (satisfies VAR01).

3. **PROOF132 (auxiliary-score remark).** The statement $S_2^{\mathrm{pos}}=2^mS_1^{\mathrm{pos}}>2S_1^{\mathrm{pos}}$ ($m=(4-\alpha)/(3-\alpha)>1$) is explicitly flagged as an auxiliary-score comparison only, not a Jensen-type improvement of an actual first moment. This is the required honesty, not an overclaim.

4. **Notation.** `PROOF128` re-derives $h_s$ via the substitution $r=s-u$; the singular kernel $|r|^{-a}$ is never differentiated, so no bound on $|r|^{-a-1}$ is needed. This is correct but could be stated even more explicitly (the derivative always falls on $\Psi$).

## Checked derivations

All six proofs were reconstructed by hand from the embedded excerpts and checked against the in-packet inputs (`compact-mean.tex` for `L:compact-raw-profile`/`P:compact-original-common-trial`, `raw-lower.tex` for `P:raw-block-original-lower`, `model.tex` for `H:homog` and `T:full-upper`, and the spectral convention in `covariance.tex`). No source outside the embedded packet was used.

### PROOF127 — `L:variational-heat-envelope` — CHECKED

- **Hypotheses.** Nonzero covariance satisfying `H:homog`; $\Gamma$ nonnegative/even/positive-definite tempered Radon, $\mu$ positive/even/tempered Radon spectral measure in the convention $\Gamma=\int e^{i\xi\cdot x}\mu(d\xi)$; $a=\alpha_0$.
- **Steps.** (i) tempered positivity $\Rightarrow$ ball-mass growth $CR^N$, dyadic annuli $\Rightarrow$ $(\Gamma,|\cdot|)$ and $(\mu,|\cdot|)$ both admit integrability of any polynomial-inverse weight for $L>N$, so Gaussians are integrable against both. (ii) $\Gamma*p_\varepsilon$ finite and $C^\infty$: translated Gaussian derivatives are bounded by any fixed polynomial weight. (iii) Schwartz pairing gives $\langle\Gamma*p_\varepsilon,\varphi\rangle=\langle\Gamma,p_\varepsilon*\varphi\rangle$; spectral convention gives the RHS $\int e^{i\xi\cdot x}e^{-\varepsilon|\xi|^2/2}\varphi(x)dx$ paired against $\mu$. (iv) Fourier constant $\int p_\varepsilon(y)e^{-i\xi\cdot y}dy=e^{-\varepsilon|\xi|^2/2}$ is exact for $p_\varepsilon=(2\pi\varepsilon)^{-d/2}e^{-|x|^2/(2\varepsilon)}$; evenness makes either Fourier sign give the same multiplier. (v) Both sides are continuous distributions in $x$ (dominated convergence on the $\mu$-integral), so equality is pointwise with no normalization correction.
- **Sign/constant check.** $\int e^{i\xi\cdot(x-z)}p_\varepsilon(z)dz=e^{i\xi\cdot x}e^{-\varepsilon|\xi|^2/2}$ (set $z=x-y$); exact. $\Gamma\neq0$, $p_\varepsilon>0$ and positivity give $(\Gamma*p_\varepsilon)(0)>0$. Verified.
- **Status.** No arbitrary translation-monotonicity assumption; the upper bound at $x=0$ follows from $\cos\le1$ and evenness.

### PROOF128 — `L:variational-global-mean` — CHECKED

- **Hypotheses.** $\Psi\in C_c^\infty((0,1)\times\R^d)$, nonnegative; $h_s$ from `E:compact-raw-mean`; $a<1$.
- **Steps.** (i) smooth zero-extension in time (support inside $(0,1)$). (ii) $|D\Psi(t,x)|\le C_D p_\varepsilon(x)$ by compact support and the positive minimum of $p_\varepsilon$ on that support. (iii) `PROOF127` bounds $\Gamma*|D\Psi(t,\cdot)|$ uniformly. (iv) $r=s-u$ transforms $h_s=\int_0^1|s-u|^{-a}\Gamma*\Psi(u,\cdot)du$ into $\int_\R |r|^{-a}\Gamma*\Psi(s-r,\cdot)dr$; on a compact time interval the $r$-range is bounded and $|r|^{-a}\in L^1_{\rm loc}$ since $a<1$. (v) All mixed time–space derivatives fall on $\Psi$ and pass the integral by dominated convergence; resulting global spatial bounds; $\partial_s h_s$ bounded $\Rightarrow$ Lipschitz estimate; nonnegativity from positive kernels.
- **Sign/constant check.** $h_s=\int_\R |r|^{-a}(\Gamma*\Psi(s-r,\cdot))(x)dr$ is exact; the time derivative only hits $\Psi(s-r)$ so no $|r|^{-a-1}$ singularity appears. Lipschitz constant $C_\Psi$ is read off the bounded time derivative. No directional decay claimed. Verified.

### PROOF129 — `P:variational-unmasked-rate` — CHECKED

- **Hypotheses.** $h_s$ real, $0\le h_s\le M$ (`PROOF128`); $H_s=-\Delta-h_s$ on complex $L^2(\R^d)$.
- **Domain.** $A=-\Delta$ self-adjoint on $H^2$ (Fourier multiplier $|\xi|^2$). $B_s=-h_s$ bounded self-adjoint, $\|B_s\|\le M$. $H_s=A+B_s$ on $D=H^2$ is closed (graph norms equivalent: $\|Af\|\le\|H_sf\|+M\|f\|$ and conversely), symmetric, densely defined.
- **Self-adjointness.** For real $b>M$, $H_s-ib=(I+B_s(A-ib)^{-1})(A-ib)$ with $\|B_s(A-ib)^{-1}\|\le M/b<1$, so $I+B_s(A-ib)^{-1}$ has a Neumann inverse and $\operatorname{Ran}(H_s-ib)=L^2$; likewise $+ib$. Then the adjoint-domain argument is valid: solve $(H_s-ib)v=(H_s^*-ib)u$, so $u-v\in\ker(H_s^*-ib)=\operatorname{Ran}(H_s+ib)^\perp=\{0\}$, giving $D(H_s^*)=D(H_s)$.
- **Form domain.** $c_{\rm shift}=1+M$, $J_s=H_s+c_{\rm shift}\ge1$. Integration by parts: $\|J_s^{1/2}f\|_2^2=\|\nabla f\|^2-\int h_s|f|^2+(1+M)\|f\|^2$; since $0\le h_s\le M$, $\|f\|_{H^1}^2\le\|J_s^{1/2}f\|^2\le(1+M)\|f\|_{H^1}^2$, and both norms dominate $\|\cdot\|_2$. Spectral cutoffs $1_{[1,n]}(J_s)$ make $H^2=D(J_s)$ a form core for $J_s^{1/2}$; Fourier cutoffs give density in $H^1$; completion identifies $D(J_s^{1/2})=H^1$ as actual $L^2$ subspaces.
- **Rayleigh/principles.** $E_s=\inf\sigma(H_s)$ finite; spectral lower bound gives one direction, spectral projections $1_{[E_s,E_s+\varepsilon]}$ give unit $H^2$ vectors with Rayleigh $\le E_s+\varepsilon$, so the reverse holds (no eigenvalue needed). Real/complex: $q_s(u+iv)=q_s(u)+q_s(v)$ with $\|u+iv\|^2=\|u\|^2+\|v\|^2$, so the complex infimum equals the real infimum. Negative floor: the common trial $w$ (support $B_{2L}$, mask plateau $R_0\ge2L$) has $m_{R_0}h_s=h_s$ on $\operatorname{supp}w$, so $q_s(w)\le-\varepsilon_0<0$; hence $\sqrt{\varepsilon_0}\le\lambda_{\Psi,s}\le\sqrt M$.
- **Lipschitz/integral.** $|E_s-E_t|\le\|h_s-h_t\|_\infty$ (compare identical unit form tests), so $|\lambda_{\Psi,s}-\lambda_{\Psi,t}|\le C_\Psi|s-t|/(2\sqrt{\varepsilon_0})$; $I_\Psi=\int_0^1\lambda_{\Psi,s}ds\in[\sqrt{\varepsilon_0},\sqrt M]$, positive and finite. No compact-potential ground-state theorem is applied to the (bounded, possibly non-decaying) unmasked potential. Verified.

### PROOF130 — `P:variational-remove-mask` — CHECKED

- **Mask.** $F(t)=e^{-1/t}\mathbf 1_{t>0}$ is flat at $0$; $\chi(r)=F(2-r)/(F(2-r)+F(r-1))$ is $C^\infty$, nonincreasing, $=1$ on $r\le1$, $=0$ on $r\ge2$ (checked at endpoints $r=1,2$ using $F(0)=0$; derivatives from the right vanish by flatness). $m_R(x)=\chi(|x|/R)$ is even, smooth at the origin and monotone in $R$ (since $\chi$ nonincreasing), $\uparrow1$ pointwise.
- **Compact ground rates.** For fixed $R\ge R_0$ ($R_0\ge2L$, trial in plateau), $V_s=m_Rh_s$ is a real nonnegative compactly supported smooth family with the same common negative margin, so `P:compact-ground-family` supplies $E_1(\sigma)$, $\lambda_{R,s}=\sqrt{-E_1(\sigma)}$, all rates positive, $\le\sqrt M$, continuous, monotone in $R$ (potential pointwise increasing).
- **Interchange.** $\sup_{R\ge R_0}\lambda_{R,s}^2=\sup_R\sup_f(\int m_Rh_sf^2-\|\nabla f\|^2)=\sup_f\sup_R(\cdots)=\sup_f(\int h_sf^2-\|\nabla f\|^2)=\lambda_{\Psi,s}^2$. The two-supremum interchange is the universally valid equality over a product index set; the $R$-supremum for fixed $f$ is monotone convergence ($m_Rh_s\uparrow h_s$). Positive roots give $\lambda_{R,s}\uparrow\lambda_{\Psi,s}$ pointwise.
- **Uniform convergence.** $\lambda_{\Psi,s}-\lambda_{R_n,s}\ge0$ continuous, decreasing in $n$; open sets $\{s:\lambda_{\Psi,s}-\lambda_{R_n,s}<\varepsilon\}$ cover compact $I$; finite subcover + monotonicity gives uniform convergence (Dini); extends to all real $R$; $\int_0^1\lambda_{R,s}ds\uparrow I_\Psi$ by monotone convergence.
- **Point lower bound.** For each fixed $R$ the identical mask is used in the driver and mean of `P:raw-block-original-lower`, giving $\liminf T^{-\kappa}\log\E|u(T,x)|^2\ge2\int_0^1\lambda_{R,s}ds-v_\Psi/2$ for the same original point liminf. Numerically $\sup_R(2I_R-v_\Psi/2)=2I_\Psi-v_\Psi/2\le Q_2$. No $R(T)$, no unmasked noisy wave, no uniform-in-mask Gaussian estimate, no source/time-limit exchange. Verified.

### PROOF131 — `L:variational-control-dilation` — CHECKED

- **Bijection.** $(D_r\Psi)(s,x)=r^{d+2-\alpha}\Psi(s,rx)$ preserves $C_c^\infty((0,1)\times\R^d)$-positivity/nonvanishing (time variable untouched); amplitude powers give inverse $D_{1/r}$; entire nonseparable class is bijected for every $r>0$ (including $r>1$).
- **Radon pushforward.** Using `H:homog` scaling $\Gamma(cA)=c^{d-\alpha}\Gamma(A)$: $\int G(ry)\Gamma(dy)=\int G(z)\,\Gamma(\cdot/r)(dz)=r^{\alpha-d}\int G(z)\Gamma(dz)$; with $G(y)=\Psi(u,rx-y)$ this gives $\Gamma*D_r\Psi(u,\cdot)=r^{2}\Gamma*\Psi(u,\cdot)(r\,\cdot)$, hence $h_{D_r\Psi,s}(x)=r^2h_{\Psi,s}(rx)$.
- **Raw cost.** $v_{D_r\Psi}=\int\int(D_r\Psi)(\sigma,x)h_{D_r\Psi,\sigma}(x)dx\,d\sigma=r^{d+2-\alpha}\cdot r^2\cdot r^{-d}\,v_\Psi=r^{4-\alpha}v_\Psi$ (the $r^{-d}$ is the Lebesgue volume Jacobian, distinct from the Radon pushforward $r^{\alpha-d}$). Covers singular/white covariances.
- **Unitary/Rayleigh.** $U_rf(x)=r^{d/2}f(rx)$ is $L^2$-unitary and maps $H^1,H^2$ bijectively; $\|\nabla U_rf\|_2^2=r^2\|\nabla f\|_2^2$; $\int h_{D_r\Psi,s}(U_rf)^2=r^2\int h_{\Psi,s}f^2$; hence $q_{D_r\Psi,s}(U_r f)=r^2q_{\Psi,s}(f)$ and $\lambda_{D_r\Psi,s}=r\lambda_{\Psi,s}$, $I_{D_r\Psi}=rI_\Psi$.
- **Intertwiner.** $H_{D_r\Psi,s}U_r=r^2U_rH_{\Psi,s}$ on $H^2$ (checked on $\Delta$ and on $h$ separately). Time is not rescaled; $m_R(rx)=m_{R/r}(x)$. Verified.

### PROOF132 — `P:variational-positive-scores` — CHECKED

- **Constants.** $k=3-\alpha>0$, $q=4-\alpha=k+1$, $m=q/k=(4-\alpha)/(3-\alpha)>1$.
- **Positivity competitor.** $\Psi_0$ fixed; $I_0>0$ (via `PROOF129`), $v_0>0$ (via `L:compact-raw-profile`). $r_0=(I_0/v_0)^{1/k}>0$ (unrestricted above/below $1$); exact powers give $I_{D_{r_0}\Psi_0}-v_{D_{r_0}\Psi_0}/2=r_0I_0-r_0^qv_0/2=r_0I_0/2>0$ since $r_0^qv_0=r_0^{k+1}v_0=r_0I_0$. The positive score is realized by an actual smooth test.
- **Scaling bijection.** $r_c=c^{1/k}$, $K_c=c^m$; $cI_{D_{r_c}\Psi}-v_{D_{r_c}\Psi}/2=c^{1+1/k}I_\Psi-c^{q/k}v_\Psi/2=K_c(I_\Psi-v_\Psi/2)$. Since $D_{r_c}$ bijects the whole class, the $c$-score set equals $K_c$ times the label-one score set, exactly.
- **Finiteness before supremum.** `T:full-upper` (independent, same canonical solution): $\E|u(T,0)|^2\le e(T+2)^d e^{C_{\rm up}T^\kappa}$, with $\kappa=(4-\alpha-\alpha_0)/(3-\alpha)$. Prefactor $\log e+d\log(T+2)$, $\log(T+2)\le\log T+\log3$, $\log T\le(T^{\kappa/2}-1)/(\kappa/2)$, all $o(T^\kappa)$; so the original point limsup $\le C_{\rm up}<\infty$. One fixed test/mask lower bound makes $Q_2$ finite, and `PROOF130` gives every label-two score $\le Q_2\le C_{\rm up}$ uniformly in $\Psi$. The $c=2$ scaling then bounds every label-one score by $C_{\rm up}/K_2$.
- **Supremum/scaling.** The nonempty label-one set has a finite real supremum $S_1^{\rm pos}>0$. Set equality and $K_c>0$ give $S_c^{\rm pos}=K_cS_1^{\rm pos}=c^{(4-\alpha)/(3-\alpha)}S_1^{\rm pos}$; the numerical supremum of label-two lower bounds gives $Q_2\ge S_2^{\rm pos}$. The remark $S_2^{\rm pos}>2S_1^{\rm pos}$ is flagged as auxiliary only (not a Jensen improvement without first-moment identification). **Zero covariance branch** (lines 379–383) sets everything to $0$ consistently ($h=0$, $v=0$, $\lambda=0$, $u=1$, rate $0$). Verified.

## Required fixes before production gate

None blocking. Optional clarity edits only:
1. In `PROOF129`, state once that the margin $\varepsilon_0$ and Lipschitz constant are fixed by the trial $\psi_L$ (via `P:compact-original-common-trial`), hence $\Psi$-dependent but not mask-evolving.
2. In `PROOF128`, optionally make explicit that $\partial_s$ never hits $|r|^{-a}$ because the substitution already absorbed the singularity into the test argument.

## Nine scoped checks (VAR01–VAR09)

- **VAR01 — PROOF127 `L:variational-heat-envelope`: PASS.** Polynomial tempered mass, Schwartz integrability, translated Gaussian derivative bounds, single Schwartz pairing, exact heat Fourier constant $e^{-\epsilon|\xi|^2/2}$, absolute Fubini, equality of continuous representatives, nonnegativity + centered-Gaussian spectral upper via evenness, nonzero-$\Gamma$ strict positivity at zero; no translation-monotonicity assumption.
- **VAR02 — PROOF128 `L:variational-global-mean`: PASS.** Smooth zero extension in time, compact derivative dominated by a fixed Gaussian, uniform convolution bound, time-change puts derivatives on $\Psi$, $|r|^{-a}$ locally integrable ($a<1$), all mixed derivatives with compact-time bounds, global space boundedness and Lipschitz-in-time, no directional decay.
- **VAR03 — PROOF129 `P:variational-unmasked-rate`: PASS.** Full $H^2$ self-adjoint bounded perturbation via both resolvents/Neumann and an adjoint-domain argument; $J$-shift $\ge1$ and the equivalent half-power/$H^1$-norm completion as actual $L^2$ subspaces; spectral-projector Rayleigh bottom tests; real/complex quotient equality; common compact trial supplies a uniform negative floor without an unmasked eigenstate; rate Lipschitz with positive finite integral; no compact-potential theorem misuse.
- **VAR04 — PROOF130 `P:variational-remove-mask`: PASS.** Explicit smooth radial monotone plateau family including the origin; fixed $R\ge R_0$ trial margin; full real $H^1$ Rayleigh formula; fixed-trial dominated convergence and exactly two numerical suprema; positive roots and compact-time uniform convergence by open-cover (Dini); same fixed mask in driver and mean provides the original-point lower bound before the numerical $\sup_R$; no $R(T)$, unmasked noisy wave, or source–time exchange.
- **VAR05 — PROOF131 `L:variational-control-dilation`: PASS.** Bijection of the entire nonseparable positive class with amplitude $r^{d+2-\alpha}$; exact Radon pushforward $r^{\alpha-d}$ vs Lebesgue $r^{-d}$; mean $r^2$, raw cost $r^{4-\alpha}$; real $L^2$ unitary and $H^1/H^2$ weak-gradient maps; rate/integral $r$; operator intertwining $H_{D_r\Psi,s}U_r=r^2U_rH_{\Psi,s}$; time unchanged and $m_R(rx)=m_{R/r}(x)$; singular/white covariances included.
- **VAR06 — PROOF132 `P:variational-positive-scores`: PASS.** Positive competitor with $r_0=(I_0/v_0)^{1/k}$ unrestricted, score $r_0I_0/2>0$; whole-score-set bijection for $c>0$ via $r_c$, $K_c=c^m$; independent SAME-canonical `T:full-upper` provides finiteness before score suprema; lower $Q_2$ bound plus uniform label-2/label-1 ceilings; supremum existence/scaling and $Q_2\ge S_2^{\rm pos}$; $S_1^{\rm pos}$ explicitly auxiliary; $\Gamma=0$ branch handled separately.
- **VAR07 — input/source application audit: PASS.** All explicit references (`L:compact-raw-profile`, `P:compact-original-common-trial`, `P:raw-block-original-lower`, `T:full-upper`, `H:homog`) are in-packet and correctly joined; no prior-vote reliance; finiteness uses `T:full-upper`, not the final intrinsic theorem; no Chen-endpoint normalization substitution.
- **VAR08 — manual adversarial controls: PASS.** White/heat/zero case (d=α=1: amplitude $r^2$, cost $r^3$), anisotropic nondecaying potential with a non-eigenvalue bottom, real/complex trial test, explicit mask monotonicity, $r=2$ and fractional-$r$ scalings of mean/raw-cost/kinetic/rate, nonseparable $\Psi$, $c$-score bijection, finite supremum before limits.
- **VAR09 — completeness/noncircularity/scope: PASS.** All six bodies reconstructed with exact domains/classes/amplitudes; every load-bearing step verified or sourced; lower bound and full-upper concern the same canonical solution; fixed parameter/source/mask/time orders preserved; no auxiliary-score first-moment identity and no exact original-point limit are claimed here; the full-213-proof and original-model obligations are unchanged.

## One-line summary

PROOF127–132 are mathematically sound: the unmasked $H^2$-self-adjoint Rayleigh rate, the uniform mask-removal lower bound $Q_2\ge2I_\Psi-v_\Psi/2$, the full-class Radon/Lebesgue dilation scaling, and the positive finite fully-homogeneous scores (with `T:full-upper` as the independent pre-supremum finiteness input and $S_1^{\rm pos}$ kept auxiliary) all check out with correct signs, constants, domains, and boundary/joint treatments — PASS.