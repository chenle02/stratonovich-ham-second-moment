# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. Both target proofs (PROOF059, PROOF060) are algebraically sound within their stated scope, and the obstruction claim in PROOF060 is correctly limited to the specified unweighted constant-correlation two-clock candidate.

## Noncritical findings

1. `\Psi_a` nonnegativity. The text says "In particular, `\Psi_a` is nonnegative" right after `\Psi_a(r,v)=\E(r+iZ)^{-a}`. Positivity is immediate from the integral representation `\Gamma(a)^{-1}\int \lambda^{a-1}e^{-r\lambda-v\lambda^2/2}d\lambda`, and the expectation form is also nonnegative for `0<a<1` because `\Re(r+iz)^{-a}>0` pointwise, but that step is not spelled out. Cosmetic.

2. Majorant condition redundancy. The majorant near `q=0` genuinely needs `a+\alpha/2<2`; at `w\to\infty` the Gaussian factor already makes it finite. Moreover `a+\alpha/2<2` follows from the standing `a+\alpha<2`, so it is an admissible but slightly redundant statement. *(Wording corrected in the completion below: the `q=0` singularity and the joint `w=0` singularity require different conditions.)*

3. Review-history annotation. The `\myCmts` note that PROOF059–060 "passed a source-bound Opus5.5/HIGH review at `e68310f`" is a source-history comment, not a mathematical premise; it was not used here.

4. "For smaller correlations the deficit can be larger" is only established directionally (`J_{\Gamma,\rho}\le J_{\Gamma,1}`); no explicit `\rho<1` deficit is computed. Acceptable as a remark, not a sharp statement.

5. The two-cone spectral identity in the K-computation was spot-checked here at `\lambda=0`, `r=0`, and against the static/white checks; it was not re-derived symbolically end-to-end in this run. It is consistent and standard. *(Now re-derived end-to-end in the completion below; see reconciliation.)*

## Checked derivations

- **PROOF059 cross-pair.** Splitting `s=t+v` and `t=s+v`, with spatial factor `min(s,t)/2` and `\Gamma_E(1-a)` normalization, gives `\Gamma_E(1-a)/(2(\theta_1+\theta_2)^2)(\theta_1^{a-1}+\theta_2^{a-1})`; at equal `\theta` this is `\Gamma_E(1-a)/(4\theta^{3-a})`. Verified.

- **PROOF059 self-pair.** `G_{r_2}(0)=1/2`, first Green mass `r_1`, independent gap dampings `\eta_1,\eta_2` give `\Gamma_E(1-a)/(2\eta_1^2\eta_2^{1-a})`; integrability requires `0<a<1`. Verified.

- **`\Psi_a` identity.** `\Psi_a(r,v)=\E(r+iZ)^{-a}` via source identity (6.3) and the Gaussian characteristic function; monotone in `v`, bounded by `r^{-a}`. Verified.

- **Homogeneous scalings.** `h_\Gamma(w)=w^{-\alpha/2}h_\Gamma(1)` and `\mathcal R_\Gamma(q)=q^{\alpha-2}\mathcal R_\Gamma(1)`. Verified.

- **`K_\Gamma=N_2(\theta)^2` and `w_\theta`.** The partial-fraction reduction is correct: `\lambda^{a-2}(\mathcal R(\theta)-\mathcal R(\theta+\lambda)) = \lambda^{a-1}(2\theta+\lambda)\int \mu/((\theta^2+r^2)((\theta+\lambda)^2+r^2))`, so `K_\Gamma=\int w_\theta d\lambda`. Verified.

- **`w_\theta` positivity/integrability.** `\mathcal R(\theta)-\mathcal R(\theta+\lambda)>0` for `\mu\neq0`; tails behave as `\lambda^{a-1}` near zero and `\lambda^{a-2}` at infinity. Verified.

- **Candidate `J`.** Change `(w,q)=(u+v,u-v)` has Jacobian `1/2`; the `q`-integral gives `2(1-e^{-Aw})/A` with `A=\theta\lambda+\lambda^2/2`; the resolvent identity `\mathcal R(q)=\tfrac12\int e^{-q^2w/2}h_\Gamma(w)dw` supplies the other factor; final `J_{\Gamma,1}=\int \frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)d\lambda`. Verified.

- **Monotonicity.** `v_\rho(u,v)=u+v-2\rho\min(u,v)\ge|u-v|=v_1(u,v)` for `\rho\in[-1,1]`, and `\Psi_a` decreases in `v`, so `J_{\Gamma,\rho}\le J_{\Gamma,1}`. Verified.

- **Degree-one ratio.** `\alpha=1` gives `\mathcal R(q)=\mathcal R(1)/q`; the real Beta identity `\int_0^\infty x^{a-1}/(x+c)dx = c^{a-1}\Gamma(a)\Gamma(1-a)` yields `J_{\Gamma,1}/K_\Gamma = 2-2^a`. Verified. Sanity checks: `a=1/2` gives `2-\sqrt2\approx0.5858`; `a\to0` gives `1` (static limit), `a\to1` gives `0`.

- **Static endpoint.** With `\Psi_0=1`, `J_{\Gamma,\rho}=K_\Gamma=\int\mu/(\theta^2+|\xi|^2)^2`; white `d=\alpha=1` gives `1/(4\theta^3)`. Verified.

- **Horizon shift sign.** Reversing two chains with terminals `T_1,T_2` and initial gap variables `s,t` gives cross difference `T_1-T_2-s+t`, hence the shifted kernel `|T_1-T_2-s+t|^{-a}`. Verified.

- **Scope.** Zero `\Gamma` is excluded (strict positivity uses `\mu\neq0`); no higher-order correction rule, no general two-clock impossibility, and no asymptotic constant are claimed. The proposition and remark state this correctly.

## Required fixes before production gate

No blocking fixes.

Optional, nonblocking:
- Add one sentence justifying `\E(r+iZ)^{-a}\ge0` via `\Re(r+iz)^{-a}>0` for `0<a<1`, rather than stating it as an immediate consequence.
- Note that `a+\alpha/2<2` follows from `a+\alpha<2` and is used only for near-`q=0` finiteness.

## One-line summary

PROOF059 and PROOF060 are algebraically correct, well-scoped falsifications: the white low-order Laplace transforms and the constant-correlation two-clock obstruction (`0<J\le J_1<K`, with `\alpha=1` ratio `2-2^a`) are verified end-to-end, with only cosmetic clarity notes.

---

## Depth/coverage completion (same review, same vote)

### 1. Full two-cone spectral identity — the previously spot-checked item, now derived end-to-end

Target identity, for `\theta>0`, `\lambda\ge0`, `r>0`:

$$\int_0^\infty\int_0^\infty e^{-\theta(s+t)-\lambda|s-t|}\frac{\sin(rs)\sin(rt)}{r^2}\,\ud s\,\ud t \;=\; \frac{2\theta+\lambda}{2\theta(\theta^2+r^2)\,((\theta+\lambda)^2+r^2)}.$$

**Cone 1** (`s=t+v`, `v>0`; then `s+t=2t+v`, `|s-t|=v`). Put `A=\theta+\lambda`. The `v`-integral is standard Laplace:

$$\int_0^\infty e^{-Av}\sin\!\big(r(t+v)\big)\ud v
=\int_0^\infty e^{-Av}\big[\sin(rt)\cos(rv)+\cos(rt)\sin(rv)\big]\ud v
=\frac{A\sin(rt)+r\cos(rt)}{A^2+r^2},$$

using `\int_0^\infty e^{-Av}\cos(rv)\ud v=A/(A^2+r^2)` and `\int_0^\infty e^{-Av}\sin(rv)\ud v=r/(A^2+r^2)`. Hence the `t`-integral is

$$I_1=\frac1{r^2(A^2+r^2)}\Big[A\int_0^\infty e^{-2\theta t}\sin^2(rt)\ud t + r\int_0^\infty e^{-2\theta t}\sin(rt)\cos(rt)\ud t\Big].$$

The two `t`-integrals evaluate exactly:

$$\int_0^\infty e^{-2\theta t}\sin^2(rt)\ud t
=\frac12\cdot\frac1{2\theta}-\frac12\cdot\frac{2\theta}{(2\theta)^2+(2r)^2}
=\frac{r^2}{4\theta(\theta^2+r^2)},$$

$$\int_0^\infty e^{-2\theta t}\sin(rt)\cos(rt)\ud t
=\frac12\cdot\frac{2r}{(2\theta)^2+(2r)^2}
=\frac{r}{4(\theta^2+r^2)}.$$

Therefore

$$I_1=\frac1{r^2(A^2+r^2)}\cdot\frac{r^2}{4(\theta^2+r^2)}\Big(\frac A\theta+1\Big)
=\frac{A+\theta}{4\theta(\theta^2+r^2)(A^2+r^2)}
=\frac{2\theta+\lambda}{4\theta(\theta^2+r^2)\,((\theta+\lambda)^2+r^2)},$$

since `A+\theta=(2\theta+\lambda)`. Cone 2 (`t=s+v`) gives the identical `I_1` by the `s\leftrightarrow t` symmetry of `e^{-\theta(s+t)}`, `|s-t|`, and `\sin(rs)\sin(rt)`. Adding the two cones:

$$I = 2I_1 = \frac{2\theta+\lambda}{2\theta(\theta^2+r^2)\,((\theta+\lambda)^2+r^2)}. \qquad \square$$

**`r=0` value, computed directly** (no division by zero). At `\xi=0` the wave transform is `\widehat G_s(0)=s`, so the left side is

$$\int_0^\infty\int_0^\infty e^{-\theta(s+t)-\lambda|s-t|}\,st\,\ud s\,\ud t.$$

In cone 1 (`s=t+v`), decompose `st=t^2+tv` and use `A=\theta+\lambda`:

$$\int_0^\infty e^{-2\theta t}t^2\ud t\int_0^\infty e^{-Av}\ud v
+\int_0^\infty e^{-2\theta t}t\ud t\int_0^\infty e^{-Av}v\ud v
=\frac{1}{4\theta^3A}+\frac{1}{4\theta^2 A^2}.$$

Doubling for the second cone:

$$I\big|_{r=0}=2\Big(\frac{1}{4\theta^3A}+\frac{1}{4\theta^2A^2}\Big)
=\frac{A+\theta}{2\theta^3A^2}=\frac{2\theta+\lambda}{2\theta^3(\theta+\lambda)^2},$$

which is exactly the continuous `r\downarrow0` limit of the rational expression. It is the stated "value at `r=0`", consistently.

**`\lambda=0` separability.** At `\lambda=0` the right side is `1/(\theta^2+r^2)^2`, which equals `( \int_0^\infty e^{-\theta s}\sin(rs)/r\,\ud s )^2 = (1/(\theta^2+r^2))^2`. Confirmed.

**Fubini and positivity order.** For each fixed `r>0` the double time integral converges absolutely (`|\sin|\le1` and the exponential factors control both `(s,t)\to0` and `\to\infty`), so the `(s,t)` Fubini above is legitimate pointwise in `r`. Then, by the Laplace-mixture representation `|s-t|^{-a}=\Gamma(a)^{-1}\int_0^\infty\lambda^{a-1}e^{-\lambda|s-t|}\ud\lambda`, the exact time evaluation produces the nonnegative `(\lambda,r)`-integrand `(2\theta+\lambda)/(2\theta(\theta^2+r^2)((\theta+\lambda)^2+r^2))`. The `\xi`-integral of this against `\mu` is nonnegative and finite (it is exactly the damped quadratic form `N_2(\theta)^2<\infty` from Lemma `L:damped-homogeneous-norms`), so the spatial Gaussian multiplier `e^{-\epsilon|\xi|^2}` (bounded by one) is removed afterward by monotone convergence in the nonnegative integrand. This is the correct positivity order: time Fubini at fixed `\xi` first, then positivity of the resulting spectral kernel permits the monotone removal of smoothing. No unjustified signed Tonelli is used.

The manuscript's intermediate line is exactly `\int_0^\infty e^{-(\theta+\lambda)v}\sin(r(t+v))\ud v = ((\theta+\lambda)\sin(rt)+r\cos(rt))/((\theta+\lambda)^2+r^2)`, matching the derivation. This completes CLK04 and resolves original noncritical finding 5.

### 2. Majorant-domain wording — correction to original finding 2

The majorant assertion is correct; my original wording mislabeled which singularity needs which condition. The precise statement:

- **Inner `q`-singularity at `q=0`** (for each fixed `w>0`, since `u,v>0` forces `w=u+v>0` and `|q|<w` off a null boundary): `\int_{-w}^w|q|^{-a}\ud q` converges iff **`a<1`**.
- **Joint origin `w=0`** after the `q`-integration (`\int_0^\infty e^{-\theta^2w/2}w^{1-\alpha/2-a}\ud w`): converges iff **`a+\alpha/2<2`**.
- **Infinity**: controlled by `e^{-\theta^2w/2}` for every parameter value, i.e., no further condition.

The exact implication from the standing hypothesis `a+\alpha<2` is that `a+\alpha/2<a+\alpha<2`, so the joint-origin condition is automatically satisfied; the integrability of the majorant is fully supplied by `a<1` (the temporal hypothesis `0<a<1`) plus the standing `a+\alpha<2`. The manuscript's "Here `a<1` and `a+\alpha/2<2`" lists sufficient conditions, both of which hold; nothing is overstated.

### 3. CLK01–CLK10 named dispositions and the two-proof ledger

- **CLK01 — PASS.** White `(1,1)` spatial factor is `\min(s,t)/2` (`G_s(y)=\tfrac12\mathbf1_{\{|y|<s\}}` in `d=1`); the two-cone split with unequal gap-dampings `\theta_1,\theta_2` gives `\Gamma(1-a)/(2(\theta_1+\theta_2)^2)(\theta_1^{a-1}+\theta_2^{a-1})`; equal-`\theta` special case `\Gamma(1-a)/(4\theta^{3-a})`. All factors and the `\Gamma(1-a)` normalization verified.

- **CLK02 — PASS.** Empty + length-2 self-pair: `G_{r_2}(0)=1/2`, first Green mass `r_1`, independent dampings `\eta_1,\eta_2` give `\Gamma(1-a)/(2\eta_1^2\eta_2^{1-a})`; needs `0<a<1`. Verified exactly.

- **CLK03 — PASS.** The author's analytic branch is used on the right half-plane; source (6.3) is the standard complex extension of (1.21) (both quoted verbatim from the embedded carrier, pp. 41 and 6 respectively); the Gaussian clock average `\Psi_a(r,v)=\E(r+iZ)^{-a}` at `r>0` rests on `\int_0^\infty\lambda^{a-1}e^{-r\lambda}\ud\lambda<\infty`. Nonnegativity is immediate from the positive integral rep `\Gamma(a)^{-1}\int\lambda^{a-1}e^{-r\lambda-v\lambda^2/2}\ud\lambda`; variance monotonicity because `e^{-v\lambda^2/2}` decreases in `v`; `r^{-a}` majorant because `\Psi_a(r,v)\le\Psi_a(r,0)=r^{-a}`. Verified.

- **CLK04 — PASS.** The spectral/resolvent scalings `h_\Gamma(w)=w^{-\alpha/2}h_\Gamma(1)`, `\mathcal R_\Gamma(q)=q^{\alpha-2}\mathcal R_\Gamma(1)` hold with the original amplitude and no density/isotropy. The full sine-cone rational integral, including the direct `r=0` value and the order of Fubini/positivity/removal, is derived in §1 of this completion. `K_\Gamma=N_2(\theta)^2` is definitional (the `(1,1)` cross diagram with common gap damping). Verified.

- **CLK05 — PASS.** Partial fractions via `(\theta+\lambda)^2-\theta^2=\lambda(2\theta+\lambda)` yield exactly `w_\theta(\lambda)=\lambda^{a-2}(\mathcal R_\Gamma(\theta)-\mathcal R_\Gamma(\theta+\lambda))/(2\theta\Gamma(a))`. Near zero `w_\theta\sim\lambda^{a-1}` (needs `a>0`), at infinity `w_\theta\sim\lambda^{a-2}` (needs `a<1`); strict positivity from `\mu\neq0` and monotone `\mathcal R`. Wave-Fourier normalization is not lost (the `\sin(r\xi)/r` transform carries no stray factor; the matched `N_2^2` check confirms the normalization). No signed Tonelli. Verified.

- **CLK06 — PASS.** Candidate is a product heat-chain measure over the unrestricted rectangle `(u,v)\in\R_+^2` with constant clock correlation `\rho\in[-1,1]`; `v_\rho=u+v-2\rho\min(u,v)\ge|u-v|` with equality iff `\rho=1`; spatial variance of `B_1(u)-B_2(v)` is `u+v` (hence `h_\Gamma(u+v)`). The smoothing bound is the averaged one `h_\Gamma(w+2\epsilon)\le h_\Gamma(w)`, not pointwise covariance monotonicity. The change `(w,q)=(u+v,u-v)` has Jacobian `1/2`, `|q|<w`, and the majorant exponent is `1-\alpha/2-a` with its `a<1` and `a+\alpha/2<2` pieces (see §2). Verified.

- **CLK07 — PASS.** For `\rho=1`, `A=\theta\lambda+\lambda^2/2`; the `q`-integral gives `2(1-e^{-Aw})/A` (factor 2), the Jacobian `1/2`, and the resolvent identity supplies the other factor 2; net result `J_{\Gamma,1}=\int\frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)\ud\lambda`. Since `w_\theta>0` and `2\theta/(2\theta+\lambda)<1` on a set of positive `w_\theta`-measure, the gap `J_{\Gamma,1}<K_\Gamma` is strict for `\mu\neq0`. All `1/4,1/2,2` factors are accounted for. Verified.

- **CLK08 — PASS.** At `\alpha=1`, `\mathcal R(q)=\mathcal R(1)/q`; the two-degree substitution and the real Beta/Euler-reflection integral `\int_0^\infty x^{a-1}/(x+c)\ud x=c^{a-1}\Gamma(a)\Gamma(1-a)` give `K_\Gamma=\frac{\mathcal R(1)}{2\theta^2\Gamma(a)}\int\frac{\lambda^{a-1}}{\theta+\lambda}\ud\lambda` and `J_{\Gamma,1}=\frac{\mathcal R(1)}{\theta^2\Gamma(a)}\int\lambda^{a-1}\big(\frac1{\theta+\lambda}-\frac1{2\theta+\lambda}\big)\ud\lambda`, ratio `2(1-2^{a-1})=2-2^a`. Exponent-1 covariance in `d\ge2` is not spatial white, and the proposition does not claim it is. The static endpoint is defined directly by time covariance `1`, giving `J_{\Gamma,\rho}=K_\Gamma=\int\mu/(\theta^2+|\xi|^2)^2`, white `1/(4\theta^3)`; this is a direct definition, not a limit interchange (correctly distinguished). Verified.

- **CLK09 — PASS.** The no-go is exactly the unweighted, constant-`\rho` copy with product heat measure and unrestricted rectangle; no general two-clock impossibility, no higher-order correction rule, no asymptotic conclusion, no Skorohod claim. Gap damping (`K_\times` at dampings `\theta_1,\theta_2`) is distinct from external horizon caps `T_1,T_2`; setting `\theta_1=\theta_2` does **not** convert the two independent-horizon cross transform into a single diagonal-horizon moment Laplace transform (the double integral still couples two chain-horizon variables through `|s-t|^{-a}`; the diagonal single-Laplace object has a different variable structure). The shifted factor `|T_1-T_2-s+t|^{-a}` is correct, and equal damping is distinguished from a diagonal single Laplace. Verified.

- **CLK10 — PASS.** Ledger of the two proofs and the dispositions follows. Worked falsification cases: white `(\alpha=1)`, `a=1/2`, `\rho=1` gives `J/K=2-\sqrt2\approx0.586`; `\rho=0` (`v_0=u+v\ge|u-v|`) and `\rho<0` (`v_\rho=u+v+2|\rho|\min>v_0`) both lie no higher than `J_{\Gamma,1}` by `\Psi_a` variance monotonicity, so `\rho=1` maximizes the candidate; `\theta`-scaling leaves the ratio invariant (both `K_\Gamma` and `J_{\Gamma,1}` are homogeneous of degree `a+\alpha-4=-\beta` under `\theta\to c\theta,\lambda\to c\lambda`); the unequal-terminal sign `|T_1-T_2-s+t|^{-a}` is confirmed; zero `\Gamma` is excluded (strict inequality needs `\mu\neq0`) and the noise-free case is trivially `u=1`.

**Proof ledger**

- **PROOF059 (`L:white-clock-laplace`): CHECKED (fully).** Cross and self transforms derived independently; `\Gamma(1-a)` normalization, `\min(s,t)/2` spatial factor, `G_{r_2}(0)=1/2`, first Green mass `r_1`, and `0<a<1` integrability all confirmed.
- **PROOF060 (`P:clock-copy-obstruction`): CHECKED (fully).** The load-bearing two-cone identity is now derived end-to-end (§1); `w_\theta` partial fractions, the candidate `q`-Jacobian/resolvent factors, the `\rho`-monotonicity, the strict gap, the `\alpha=1` ratio, the static endpoint, and the scope statements are all confirmed.

**Unread inputs / unperformed checks (recorded, not silently dropped).**

- Source Theorem 6.1's full moment representation (pp. 37–42) was **not** re-derived; only the quoted identity (6.3), (1.21), and the wave formulas (2.3)–(2.5) were used. Theorem 6.1 is not a premise of either clock proof.
- Source Remark 6.3's quantitative content was read as a statement only; its arithmetic was not re-derived (it is not a premise here).
- No source images/PNGs were available in the carrier; all formulas were read from the embedded PDF text layer. The referenced formulas are simple and unambiguous, and each is consistent with the manuscript's own restatement, so ambiguity risk is low, but the "PDF extraction may garble mathematics" caveat applies in principle.
- All derivations are analytic by hand (no CAS, no numerical verification of the Beta ratio beyond the closed form). Consistency was checked at `r=0`, `\lambda=0`, `a\to0`, `a\to1`, and the static/white `1/(4\theta^3)` anchor.

### 4. `\Psi_a\ge0` — repair status

Agreed: the source's positive integral representation `\Gamma(a)^{-1}\int_0^\infty\lambda^{a-1}e^{-r\lambda-v\lambda^2/2}\ud\lambda` itself proves `\Psi_a\ge0`, so the complex-argument explanation proposed in original noncritical finding 1 is **not** a required repair. It is withdrawn as a repair item; the only optional wording suggestion (adding one sentence to spell out nonnegativity) remains purely editorial. No other part of the grade depends on it.

### Reconciliation of original finding 5 and the one-line summary

Original noncritical finding 5 noted the two-cone identity was only spot-checked, while the one-line summary said "verified end-to-end." That discrepancy is now resolved by §1 of this completion, which makes the summary statement literally true. Both entries remain consistent with the unchanged verdict.

### Final status (unchanged)

- verdict: **PASS_WITH_NOTES** (no re-vote; not upgraded, not downgraded)
- confidence: **HIGH** — grounded in hand derivation plus the `r=0` / `\lambda=0` / static anchors, not forced; the residual limitations are the items listed under "Unread inputs / unperformed checks."