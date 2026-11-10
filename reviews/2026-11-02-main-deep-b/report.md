# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. All four target proofs (PROOF042–PROOF045) check out under hand verification of every coefficient, sign, boundary term, limit, and asymptotic claim, given the supplied upstream lemmas. No false identities, hidden hypotheses, incorrect constants, or invalid asymptotics were found.

## Noncritical findings

1. **Dimension specificity of `D_Gamma` (scope note, not an error).** `L_alpha(h,lambda)` in Corollary C:static-interaction contains `D_Gamma = (3-alpha)M/(4pi)*(2^alpha + 3^(2-alpha)/(2-alpha))`, which is the *d=3* spherical-wave constant from Section S:static-phase (upstream L:phase-contractions). The corollary lives inside that d=3 static context, so it is internally correct; but `D_Gamma` must not be silently reused in d=1,2. The interval section (PROOF044) correctly avoids this by relying only on the dimension-free radial spectral mass `R_alpha`.

2. **Source-image/render verification not performed.** The Crouzeix–Palencia import was checked against the supplied *text extraction* (crouzeix-v1.txt, eq. (3) p.1 and Theorem 6 pp.5–6, giving `C_Omega <= 1+sqrt2`), which matches E:cp-input. The carrier itself warns "PDF extraction may garble mathematics; assigned PNGs remain required." I flag the extracted-formula equivalence as unverified at the raster level; the algebraic consequence E:cp-input as used is correct from the text.

3. **Downstream fixed-split lemma is context-only.** L:fixed-split (fixed-split-context.tex) is not certified here, consistent with scope. The four targets do not depend on it being proved; they only need to be consistent with its setup (bounded `A_0`, finite colors, real/complex couplings), which they are.

4. **Honesty/overclaim check:** the target text correctly and repeatedly disclaims zero-smoothing limits, overlap/interval-field identification, and propagator-level cutoff identities ("We assert no zero-smoothing phase limit…", "This is an equality of selected finite words, not of full propagators at a fixed cutoff", "…does not identify a product with an evolution driven by overlapping or repeated fields"). The `myCmts` review-status prose and abstract status sentences are historical metadata, not used as premises. No overclaim found.

## Checked derivations

### PROOF042 — P:static-phase-all-orders (B01+B02+B03)

**Holomorphic extraction (B01).** The four phase entries of the propagator of `u''+(A_0-zB)u=0` are entire in the coupling `z` (`cos(h sqrt L)`, `sin(h sqrt L)/sqrt L` have power series in the bounded `L=A_0-zB`); the map is holomorphic operator-valued, *not* a squared norm. Cauchy's formula with radius `r = delta_{alpha/2} lambda^{2-alpha/2}/d_N` gives

  `||c_n||_{X_lambda} <= 100 e^{2 lambda h} (d_N/(delta_{alpha/2} lambda^{2-alpha/2}))^n ||S_b(f,g)||_lambda`.

The `n`-th coefficient is exactly the `n`-th vacuum Duhamel word (verified against the perturbation series of the entire propagator and E:phase-duhamel). Lemma L:finite-word-cutoff applies with one color, `N=n`, `r_i=n`, `F_l` = free propagators, `K_ij = M_{e_j}`; it preserves lowering terms and self-contractions exactly. `a = alpha/2 in (0,1)` holds since `alpha < 2-alpha_0 < 2`.

**Constants (B02).** With `lambda = n/h` and `d_n = 2 sqrt(n+1) sqrt(R_alpha) <= 2 sqrt2 n^{1/2} sqrt(R_alpha)`:

  intermediate `= 100 e^{2n} (2 sqrt(n+1) sqrt(R_alpha) h^{2-alpha/2} n^{-(2-alpha/2)}/delta_{alpha/2})^n ||.||_{n/h}`.

Metric comparisons: `A_{n/h} <= n^2 A_{1/h}` gives `||z||_{1/h} <= n||z||_{n/h}`; `A_{n/h} >= A_{1/h}` gives `||.||_{n/h} <= ||.||_{1/h}`. Result:

  `100 n (2 sqrt2 e^2/delta_{alpha/2})^n R_alpha^{n/2} h^{(4-alpha)n/2} n^{-(3-alpha)n/2} ||(f,g)||_{1/h}`,

where `(2-alpha/2)n = (4-alpha)n/2`. Then `100 n <= 200^n` gives `A_alpha = 400 sqrt2 e^2/delta_{alpha/2}`, and `n! <= n^n` gives `n^{-(3-alpha)n/2} <= (n!)^{-(3-alpha)/2}` (factorial direction correct). E:all-static-phase-orders follows with `A_alpha sqrt(R_alpha)`.

Elementary series (both cases verified): `beta=(3-alpha)/2 in (1/2,3/2)`. For `beta >= 1`, `sum a_n^beta <= (sum a_n)^beta` with `a_n = x^{n/beta}/n!`; for `beta < 1`, Hölder with exponents `1/beta`, `1/(1-beta)` gives geometric series `sum 2^{-beta n/(1-beta)} <= 2` (needs `beta >= 1/2`, satisfied). Both yield `sum x^n/(n!)^beta <= 2 e^{3 x^{1/beta}}`.

Squared sum (verified): `||Z_0||_{1/h} <= sqrt(e)||.||`; triangle inequality on the `L^2(Omega;X_{1/h})` norm gives `||sum sigma^n Z_n|| <= (sqrt e + 2 e^{3x^{1/beta}})||.|| <= (sqrt e+2)e^{3x^{1/beta}}||.||`; squaring gives `(sqrt e+2)^2 e^{6x^{1/beta}}`, and `x^{1/beta} = A_alpha^{2/(3-alpha)} |sigma|^{2/(3-alpha)} R_alpha^{1/(3-alpha)} h^{(4-alpha)/(3-alpha)}`. Matches E:all-static-phase-sum exactly (factor 6, exponents (3-alpha) checked).

**Cutoff removal (B03).** Unweighted field multiplication on degree `<= N` has norm `<= 2 sqrt(N+1) sqrt(v_epsilon)` uniformly in `m` (pointwise creation `sqrt(N+1)` + annihilation `sqrt N`, coordinate norm `<= sqrt(v_epsilon)`); insertion `(u,v)->(0,W_epsilon u)` is bounded by that over `lambda` (since `||A_lambda^{-1/2}|| <= 1/lambda`). Free evolution `e^{lambda h/2}`. `S_b -> I` strongly and commutes with the free propagator; finite-coordinate vectors have zero annihilation tail and creation tail dominated by `v_epsilon`; density + uniform bound extends strong convergence; dominated time integration gives the Bochner limit identifying `Z_n^epsilon`. No zero-smoothing limit asserted. Uniform-in-epsilon is legitimate: `A_alpha` is epsilon-independent (L:fock-form and L:complex-phase are epsilon-uniform), removal is per fixed epsilon.

### PROOF043 — C:static-interaction (B04+B05)

`||S_0(-h)||_lambda <= sqrt e` (both directions; `lambda h <= 1`). `Y_0 = (f,g)`. First variance coefficient `K_eps = E||Y_1||^2 + 2 Re<Y_0, E Y_2>` is bounded by `L_alpha N^2`: first term `<= e * R_alpha h^2 lambda^{alpha-2}(1+lambda^2 h^2)^2 <= 4 e R_alpha h^2 lambda^{alpha-2}`; cross term `<= 2 sqrt(e) N * D_Gamma(1+lambda^2h^2)h^{3-alpha}/(lambda(2-alpha)(3-alpha)) N <= 4 sqrt(e) D_Gamma h^{3-alpha}/(lambda(2-alpha)(3-alpha)) N^2`. Both `<= 2`-type reductions use `lambda h <= 1`. Verified; no sign or monotonicity assumption used.

`||Y_n||_{X_lambda} <= (sqrt e/(lambda h)) (A_alpha sqrt(R_alpha))^n h^{(4-alpha)n/2}/(n!)^{gamma/2} N`, where `gamma=3-alpha`. The `1/(lambda h)` is correct via `A_{1/h} <= (lambda h)^{-2} A_lambda` ⟹ `||z||_{X_lambda} <= (1/(lambda h))||z||_{X_{1/h}}`. Gaussian parity: `E<Y_r,Y_s>=0` for `r+s` odd. `r!s! >= (k!)^2` (binom coefficient maximized at `k`). Sum over the `2k+1` pairs (including `r=0,s=2k` and `r=2k,s=0`, using `||Y_0||=N`) is bounded by `e(2k+1)/(lambda h)^2 (A_alpha^2 R_alpha)^k h^{(4-alpha)k}/(k!)^gamma N^2`. `e(2k+1) <= (3e)^k` for `k>=2`, and `x = B_alpha sigma^2 R_alpha h^{4-alpha} = 3e A_alpha^2 sigma^2 R_alpha h^{4-alpha}`. Since `gamma>1`, `sum_j x^j/(j!)^gamma <= e^{gamma x^{1/gamma}}`, hence the `k>=2` tail `<= x^2 e^{gamma x^{1/gamma}}/(lambda h)^2 N^2`. Keeping the sharper first coefficient separately gives `E:static-interaction` with `E = sigma^2 L_alpha + x^2 e^{gamma x^{1/gamma}}/(lambda h)^2` (form matches).

Dyadic summability: three powers `1-alpha_0 > 0`, `2-alpha-alpha_0 > 0`, `2 beta-3 > 1 > 0` with `beta=4-alpha-alpha_0>2`; exponential `e^{gamma (B_alpha R_alpha)^{1/gamma} h_j^{beta/gamma}}` bounded at `h_0`. Geometric series converge; E:static-block-series holds. Independent-block product: `||M_j||^2 <= e^{lambda h_j}(1+E_j)`, tensoring with independent past, iteration, `1+y <= e^y` gives E:independent-static-blocks. No overlap inference made.

### PROOF044 — L:interval-contractions (B06)

`mu(B_r) = r^alpha mu(B_1)` is dimension-free (radial mass only, no `S^{d-1}` surface used). Gaussian comparison `int e^{-s|eta+xi|^2} mu(d xi) = int p_{2s}^{(d)} e^{i eta x} Gamma(dx) <= int e^{-s|xi|^2} mu(d xi)` (evenness → real, `Gamma>=0`, `cos<=1`). Integrating against `e^{-rho^2 s}`: `sup_eta int mu/(rho^2+|eta+xi|^2) <= R_alpha rho^{alpha-2}` with `R_alpha = alpha pi mu(B_1)/(2 sin(pi alpha/2))` from `int_0^inf r^{alpha-1}/(rho^2+r^2) dr = rho^{alpha-2} pi/(2 sin(pi alpha/2))` (needs `0<alpha<2`, satisfied). Column identity verified: `S = sum_m M_{e_m} A_rho^{-1} M_{e_m}` has kernel `G_rho Gamma_epsilon` (since `sum_m e_m(x)e_m(y)=Gamma_epsilon(x-y)`), Fourier multiplier `J_{rho,eps}(eta)=int e^{-eps|xi|^2} mu/(rho^2+|eta+xi|^2)`; hence E:interval-column with NO extra `1/(rho^2+|eta|^2)` factor (correct: one-sided `A_rho^{-1/2}M_{e_m}`, not the sandwiched `H_m`). Substituting `A_rho^{-1/2}f`: `sum_m H_m^2 <= R_alpha rho^{alpha-4}I`; row/column equality by selfadjointness; creation row `sqrt(j+1) <= sqrt(N+1)`, annihilation adjoint; total `2 sqrt(N+1) sqrt(R_alpha) rho^{alpha/2-2}` (E:interval-fock). Insertion norm `sqrt(R_alpha) rho^{(alpha-2)/2}` = `sqrt(R_alpha) rho^{alpha/2-1}` (consistent: one fewer `rho^{-1}` than the sandwich). `S_b A_rho^{-1} S_b <= A_rho^{-1}` gives band version. White-noise check `d=alpha=1`: `mu(dxi)=dxi/(2pi)`, `mu(B_1)=1/pi`, `R_1=1/2`, and `int mu/(rho^2+xi^2)=1/(2rho)` matches. No unsmoothed norm or angular mass absorbed.

### PROOF045 — L:interval-complex (B07+B08)

Non-selfadjoint extension verified step by step. Adjoint sandwich `A_rho^{-1/2}V^*A_rho^{-1/2}=(A_rho^{-1/2}VA_rho^{-1/2})^*` (same bound). Accretivity `Re<(L+Lambda^2)u,u> >= (1-delta_a)<A_Lambda u,u>` from `|<Vu,u>| <= D Lambda^{a-2}(s^2+Lambda^2) <= delta_a(s^2+Lambda^2)`. Resolvent identity `A_Lambda^{1/2}[(L+Lambda^2+t)^{-1}-A_kappa^{-1}] = A_Lambda^{1/2}A_kappa^{-1/2}(1-K_kappa)^{-1}K_kappa A_kappa^{-1/2}` with norm `<= D kappa^{a-3}/(1-delta_a)` (factors: 1, `1/(1-delta_a)`, `D kappa^{a-2}`, `1/kappa`; `||K_kappa||<=D Lambda^{a-2}<=delta_a<1`). Inverse-root integral gives `||Q-1|| <= D Lambda^{a-2} I_a/(pi(1-delta_a)) <= delta_a I_a/(pi(1-delta_a)) <= 1/6`, verified in both cases of `delta_a=min{1/4, pi/(8I_a)}`. Hence `||Q||<=7/6`, `||Q^{-1}||<=6/5`; adjoint integral gives `(L_Lambda^{-1/2})^*=(L_Lambda^*)^{-1/2}`; all four root comparisons `<= 2` (in fact `<= 7/6` or `<= 6/5`). Numerical range: `|<Vu,u>| <= 2Ds^a` at `rho=s` (and `rho↓0` for `s=0`), `x+Lambda^2 >= (1-delta_a)(s^2+Lambda^2)`, `|y| <= 2 delta_a Lambda^{2-a}s^a`; parabola `y^2 <= (4delta_a^2/(1-delta_a))Lambda^2(x+Lambda^2) <= (1/3)Lambda^2(x+Lambda^2)`, `x >= -Lambda^2/4`, `|Im sqrt w| <= Lambda`. Crouzeix–Palencia applies to the non-selfadjoint bounded `L` (hypotheses met; no selfadjointness or commutation used). Block norms `3e^{Lambda h}, 12(1+Lambda h)e^{Lambda h}, 12e^{Lambda h}, 12e^{Lambda h}`; sum `(39+12Lambda h)e^{Lambda h} <= 39(1+Lambda h)e^{Lambda h} <= 100e^{2Lambda h}`. Metric loss: `||z||_{rho_new} <= max{1, rho_old/rho_new}||z||_{rho_old}` (both directions checked via `A_{rho_old} <= (rho_old/rho_new)^2 A_{rho_new}` when decreasing); ratio `(lambda+R+E)/(lambda+R+S) <= 1+sum_E omega_i/lambda <= prod_E(1+omega_i/lambda)`; each connected interval ends exactly once including the final return at `T`; product form E:interval-metric. `D <= delta_a Lambda^{2-a}` is stated as the guard and left to the application (not assumed globally).

### Falsification controls (distinct from proof)

- `n=1`: Cauchy bound is far looser than the sharp `2 sqrt(R_alpha) h^{(4-alpha)/2}` (E:phase-born at `lambda=1/h`) but consistent — no contradiction.
- `sigma=0`: RHS `(sqrt e+2)^2` exceeds LHS `1`; correct.
- `R_alpha=0`: `mu=0`, all `n>=1` terms zero; handled explicitly.
- `d=1` white noise `Gamma=delta_0`: `R_1=1/2`, resolvent `1/(2rho)`; matches.
- Non-selfadjoint scalar `V`: accretive right-half-plane, `100e^{2Lambda h}` holds.
- Simultaneous starts/ends: handled by `E` vs `S` sets; endpoints counted once.

## B01–B08 determination

- **Determination: B01–B08 all PASS; four proofs FULLY_CHECKED.**
  - B01 (coefficient extraction), B02 (static-order constants), B03 (cutoff removal) — PROOF042: verified.
  - B04 (static-interaction first variance/mean), B05 (higher series + independent blocks) — PROOF043: verified.
  - B06 (dimension-free interval contractions) — PROOF044: verified.
  - B07 (non-selfadjoint complex extension), B08 (phase weights/controls) — PROOF045: verified.
  - No hidden hypotheses, no sign errors, no incorrect constants, no invalid asymptotics. The only residuals are (a) `D_Gamma` is d=3-specific and must stay in its section, (b) downstream L:fixed-split and source raster checks remain outside this unit's clearance.

## Proof ledger

| Proof | Verdict | Checked steps | Limits / constant dependence | Residual gaps |
|---|---|---|---|---|
| PROOF042 (P:static-phase-all-orders) | FULLY_CHECKED | Entire-in-`z` operator phase map; Cauchy radius `delta_{alpha/2} lambda^{2-alpha/2}/d_N`; `N=n` exact word identity incl. self-contractions; `lambda=n/h` metric comparisons; `100n<=200^n`, `n!<=n^n`; series `beta>=1`/`beta<1`; `(sqrt e+2)^2 e^{6x^{1/beta}}`. | `A_alpha=400 sqrt2 e^2/delta_{alpha/2}`; `h^{(4-alpha)n/2}`, `(n!)^{-(3-alpha)/2}`; uniform in `eps` via `R_alpha`-only constants; `R_alpha=0` case. | None within scope. |
| PROOF043 (C:static-interaction) | FULLY_CHECKED | `||S_0(-h)||<=sqrt e`; `L_alpha` from E:phase-born + E:phase-mean (`4`,`e`,`2` factors); `1/(lambda h)` norm conversion; Gaussian parity; `r!s!>=(k!)^2`; `e(2k+1)<=(3e)^k`; `gamma>1` series; dyadic powers `1-alpha_0, 2-alpha-alpha_0, 2beta-3`; exp metric factor. | `B_alpha=3eA_alpha^2`, `x=B_alpha sigma^2 R_alpha h^{4-alpha}`, `gamma=3-alpha`; `beta=4-alpha-alpha_0>2`. | `D_Gamma` is d=3-specific (scope note). |
| PROOF044 (L:interval-contractions) | FULLY_CHECKED | Radial `mu(B_r)=r^alpha mu(B_1)` (no sphere); Gaussian comparison; `R_alpha` via Beta integral; column Plancherel identity (no extra `rho^{-2}`); `sum H_m^2<=R_alpha rho^{alpha-4}`; creation/annihilation; band compression `S_b A_rho^{-1}S_b<=A_rho^{-1}`. | Only `R_alpha` (and `alpha`); `rho^{(alpha-2)/2}` insertion, `rho^{alpha/2-2}` sandwich; white `d=alpha=1` consistent. | None within scope. |
| PROOF045 (L:interval-complex) | FULLY_CHECKED | Adjoint sandwich; accretivity; resolvent identity `D kappa^{a-3}/(1-delta_a)`; `1/6` via `delta_a=min{1/4, pi/(8I_a)}`; four root comparisons `<=2`; numerical-range parabola incl. `s=0`; CP on non-selfadjoint `L`; `100e^{2Lambda h}`; metric ratio `<= prod_E(1+omega_i/lambda)`, each interval ends once. | `D<=delta_a Lambda^{2-a}` guard; `(3-alpha)` exponents `2-alpha/2`; constants `3,12,100`. | `D<=delta_a Lambda^{2-a}` enforcement left to the application (by design). |

## Required fixes before production gate

None for the four audited proofs. Recommended (non-blocking) hygiene: (i) annotate `D_Gamma` in C:static-interaction as the d=3 static-phase constant so it is not reused in d=1,2; (ii) complete raster/source-image verification of Crouzeix–Palencia (3)/Theorem 6 once a rendered PDF/PNG is available, since the current carrier is text-extracted. The downstream L:fixed-split proof and the full upper-bound assembly remain outside this unit and still require their own clearance; the four targets do not inherit that clearance.

## One-line summary

PROOF042–PROOF045 are all fully correct on hand-checked constants, inequalities, signs, boundary terms, limits, and asymptotics (B01–B08 pass); the only residuals are the d=3-specific `D_Gamma` annotation and out-of-unit downstream/source-image items.