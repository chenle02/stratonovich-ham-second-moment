# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. Both target proofs (PROOF059, PROOF060) are algebraically sound within their stated scope, and the obstruction claim in PROOF060 is correctly limited to the specified unweighted constant-correlation two-clock candidate.

## Noncritical findings

1. `\Psi_a` nonnegativity. The text says "In particular, `\Psi_a` is nonnegative" right after `\Psi_a(r,v)=\E(r+iZ)^{-a}`. Positivity is immediate from the integral representation `\Gamma(a)^{-1}\int \lambda^{a-1}e^{-r\lambda-v\lambda^2/2}d\lambda`, and the expectation form is also nonnegative for `0<a<1` because `\Re(r+iz)^{-a}>0` pointwise, but that step is not spelled out. Cosmetic.

2. Majorant condition redundancy. The majorant near `q=0` genuinely needs `a+\alpha/2<2`; at `w\to\infty` the Gaussian factor already makes it finite. Moreover `a+\alpha/2<2` follows from the standing `a+\alpha<2`, so it is an admissible but slightly redundant statement.

3. Review-history annotation. The `\myCmts` note that PROOF059–060 "passed a source-bound Opus5.5/HIGH review at `e68310f`" is a source-history comment, not a mathematical premise; it was not used here.

4. "For smaller correlations the deficit can be larger" is only established directionally (`J_{\Gamma,\rho}\le J_{\Gamma,1}`); no explicit `\rho<1` deficit is computed. Acceptable as a remark, not a sharp statement.

5. The two-cone spectral identity in the K-computation was spot-checked here at `\lambda=0`, `r=0`, and against the static/white checks; it was not re-derived symbolically end-to-end in this run. It is consistent and standard.

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