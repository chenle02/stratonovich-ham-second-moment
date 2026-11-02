# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. All three proofs are mathematically sound; no false identity, sign error, incorrect constant, hidden hypothesis, or invalid limit was found. The final coefficient, exponent κ=(4−α−α₀)/(3−α), the parameter-only constant C=C(α,α₀), and the volume prefactor (T+2)^d are all correct and non-circularly derived.

## Noncritical findings

1. **Cross-scale grid nesting is true but not strictly load-bearing.** The claim (target line 197–198) that parent grid ⊂ child grid via `3t ∈ ℤ` is *correct* (parent point `h_j(n+(-1)^j t)` equals child point `(h_j/2)(2n + (-1)^j·3t)`), but neither the dyadic domination `E:dyadic-time-majorant` nor the inventory `h_i ≤ 78T/i` actually uses cross-scale nesting; they only need the three grids *at the chosen scale* and the per-level interval count. Expositional redundancy, not an error.

2. **The `K_∞` upper bound is "for context" only.** Line 210–212 claims `Σ ... ≤ C_{α₀}|s−r|^{−α₀}` off the diagonal, but no explicit `C_{α₀}` is pinned down because it is not used in the main derivation (only the lower bound `|s−r|^{−α₀} ≤ K_∞(s,r)` is used). Correct and honestly labeled, but loose.

3. **Terse but correct localization identity.** The step `G_s*f_T(y)=s, so C_s f_T(y)=1` (line 232–233) is correct because `G_s*f_T(y)=∫G_s(y−z)f_T(z)dz = mass(G_s)=s` on the cone, and `∂_sG_s=C_s`. The reader must recall `∂_sG_s=C_s`; no error.

4. **`v_max`-dependent pointwise-convergence majorant.** Line 250–253 uses `√((2n−1)!!)v_max^{n/2}T^{2n}/(2n)!` with `v_max` defined upstream (in `P:interval-coefficients`) as a J,ε-dependent quantity; it is used only for fixed-(J,ε) series convergence, never for the uniform bound. Fine, but `v_max` is referenced without local definition.

5. **Source fidelity is textual only.** The held source is a PDF text carrier (explicitly "may garble mathematics"); the imported formulas `(1.21),(2.9),(2.11),(2.23)–(2.24)`, Theorem 3.1 `(3.6)`, and Crouzeix–Palencia `(3)`/Theorem 6 are legible and self-consistent in the carrier, but raster/PDF-image authentication remains an open, separate gate (recorded in scope, not a defect of these proofs).

## Checked derivations

### PROOF049 — L:terminal-wick (source 6273–6329; excerpt 69–125)

- **Terminal mass `M_n = T^{2n}/(2n)!`.** Hand-verified: `M_0=1`; `M_1=∫_0^T (T−s)ds = T²/2`; `M_2=∫_0^T(T−s)(s²/2)ds = T⁴/24`. The recursion `M_n(T)=∫_0^T(T−s)M_{n−1}(s)ds` is correct ("integration at the last vertex": mass of `G_{T−s}` is `T−s`, remaining chain is `g_{n−1}^{s,y_n}` of total mass `M_{n−1}(s)`). Induction gives `T^{2n}/(2n)!`. Holds in d=1,2,3 (mass of `G_h` is `h` in all dimensions, including the d=3 sphere measure `σ_h/(4πh)`).
- **Gaussian majorant.** Generalized Hölder (`Σ_{j=1}^n 1/2n = 1/2`) gives `‖∏W_j‖₂ ≤ ∏‖W_j‖_{2n} ≤ ∏[V^{1/2}((2n−1)!!)^{1/(2n)}] = √((2n−1)!!)V^{n/2}`. Multiplying by the kernel mass gives `E:terminal-term-majorant` exactly.
- **Bochner integrability.** Mean-square continuity of Gaussian variables implies continuity in every fixed `L^p` (via `E|X−Y|^p = C_p(E|X−Y|²)^{p/2}`), so the product is strongly measurable on the time cells; finite mass + uniform bound give Bochner integrability.
- **Isserlis coefficient = 1, hand-verified.** Coefficient of `t_1⋯t_{2k}` in `(1/k!)(1/2)^k(Σ_{ij}K_{ij}t_it_j)^k`: for one pairing there are `k!` orderings and `2^k` orientations of the ordered pairs, giving `k!·2^k·∏K`; divided by `(1/k!)(1/2)^k` yields exactly `∏_{(a,b)∈D}K_{ab}`. Odd total degree gives 0. Correct.
- **Symmetrization.** Product of scalar field values is relabeling-invariant; averaging the `n!` pushforwards with `1/n!` gives no extra factorial (lines 100–106). Correct.
- **d=3.** `p_η*G` is positive, same total mass, converges weakly to `G`; off the time cut points the finite Gaussian moments are bounded continuous in space, so dominated convergence passes the Wick sums in `L²`, matching the source's Green-width convention. Correct.
- **Ratio test, exact.** `a_{n+1}/a_n = |r|√V·T²·√(2n+1)·(2n)!/(2n+2)! = |r|√V T²/((2n+2)√(2n+1)) → 0`, proving absolute `L²` convergence of `Σ r^n Y_n` for every real/complex `r`. Zero-variance case `V=0` is immediate. Correct.

Small cases (distinguished from proof): n=0 empty tuple `Y_0=1`; n=1 gives `‖Y_1‖₂ ≤ √V·T²/2`, consistent with the explicit first moment `∫KG_{T−s}G_{T−r}`; unequal chains (1,1) give the single cross-pairing integral with coefficient 1; (2,0) gives the self-paired mean `E[Y_2]` with coefficient 1; odd (1,0) gives 0.

### PROOF050 — L:uniform-series-tail (source 6357–6377; excerpt 153–173)

- **Diagonal domination.** With nonnegative mixed moments (Lemma L:terminal-wick under `K≥0`), `E|u^{ε,δ}(r)|² = Σ_n r^{2n}E|Y_n|² + Σ_{m≠n}r^{m+n}E[Y_mY_n]` with every cross term `≥0`, so `r^{2n}E|Y_n^{ε,δ}|² ≤ B_r`. Correct.
- **Fixed-order limit.** `Y_n^{ε,δ}→X_n` in `L²` implies `‖Y_n‖₂→‖X_n‖₂`, which passes the same bound to `X_n`. Correct.
- **Geometric tails.** `Σ_{n>N}B_r^{1/2}r^{−n} = B_r^{1/2}r^{−(N+1)}/(1−r^{−1})`; absolute convergence of `u=ΣX_n` is proved, not assumed. Correct.
- **Double-limit.** Splitting at N gives distance `≤ 2B_r^{1/2}r^{−(N+1)}/(1−r^{−1}) + ‖Σ_{n=0}^N(Y_n^{ε,δ}−X_n)‖₂`; `ε,δ↓0` at fixed finite N first, then `N→∞`; this proves full regularized convergence without assuming the original series converges. Continuity of the `L²` norm passes `E|u^{ε,δ}(1)|²≤B_1` to `E|u|²≤B_1`. Correct.

### PROOF051 — T:full-upper (source 6397–6618; excerpt 193–414)

- **Grid domination, exact constant.** For `s≠r`, choose `j` with `3|s−r|<h_j≤6|s−r|` (exists since `h_0=H_0≥6T≥6|s−r|` and `h_j→0`); the three grids at that scale have boundaries spaced `h_j/3>|s−r|` apart, so at least one (indeed two) grid has no boundary strictly between `s,r`, i.e., a common cell. Hand-verified representative: `T=1, h=1/2, s=0.1, r=0.2` — the only boundary in (0.1,0.2) is `1/6` (grid `t=1/3`); grids `t=0` (cell `[0,0.5]`) and `t=2/3` (cell `[−1/6,1/3]`) both contain the pair. Hence `|s−r|^{−α₀} ≤ 6^{α₀}|I|^{−α₀} ≤ 6^{α₀}Σ_{3 grids,|I|≤H₀}|I|^{−α₀}1_I(s)1_I(r)=K_∞(s,r)`. Correct.
- **Inventory, exact.** At level j: `≤3(T/h_j+2)` intervals; cumulative through level j `≤6T/h_j + 6(j+1) ≤ 6T/h_j + 6·2^j ≤ 78T/h_j` (using `j+1≤2^j` and `2^j=H₀/h_j<12T/h_j`); sorted decreasing lengths give `h_i ≤ 78T/i` (ties handled since even the earliest index in a tie block satisfies `i ≤ 78T/h_j`). So `L=78`, `c=6^{α₀}` in `P:interval-coefficients`. Correct.
- **Interval-model covariance.** `E[W_{J,ε}(s,y)W_{J,ε}(r,z)] = Σ_I σ_I²1_I(s)1_I(r)Γ_ε(y−z) = K_J(s,r)Γ_ε(y−z)`, with `σ_I²=6^{α₀}|I|^{−α₀}` and independent static fields. Correct; `K_J↑K_∞`, `K_J` not assumed stationary.
- **Localization, exact.** `f_T=1` on `B_{T+1}`, support `B_{T+2}`, velocity 0; on the cone `G_s*f_T=s` (mass of `G_s`) hence `C_s f_T=∂_s(G_s*f_T)=1`. Chain points ending at `x∈B_1` satisfy `|y_j|+s_j ≤ |x|+T < T+1` (triangle inequality through the Green supports), so every free initial-data factor is 1; termwise identification with the constant-data model on `B_1`. Correct.
- **Moment bound of the interval model.** `P:interval-coefficients` (phase norm `‖·‖_{1/T}`, `‖(f_T,0)‖²_{1/T}=‖f_T‖²≤|B_{T+2}|`) gives `E‖u_{f_T,J,ε}(T)‖²_{L²} ≤ e|B_{T+2}|exp{C R_α^{1/ν}T^{β/ν}}`; stationarity and the `B_1` identification give `|B_1|E|u_{J,ε}(T,0)|² ≤` that, i.e. `E|u_{J,ε}(T,0)|² ≤ B(T)=e(T+2)^d exp{C R_α^{1/ν}T^{β/ν}}`. Correct.
- **Monotone comparison, exact.** Both source and interval partial moments are finite sums over the *same* terminal-chain kernels and pairings; only the time covariance factor differs. `γ_δ^0(s−r) ≤ |s−r|^{−α₀} ≤ K_∞(s,r)=lim_J K_J(s,r)` pointwise (with `∞=∞` on the time diagonal, which is Lebesgue-null), so by nonnegative Tonelli `E|U_N^{ε,δ}|² ≤ lim_JE|V_{N,J}^ε|² ≤ sup_JE|u_{J,ε}|² ≤ B(T)`. `K_∞` is used only inside these monotone limits of positive integrals; no infinite-depth field is constructed. Correct.
- **Amplitude scaling, exact.** Amplitude a ⟺ spatial covariance `a²Γ`; `a²Γ` ⟹ `R_α↦a²R_α` with unchanged parameter-only `C`; order-n term scales as `a^n`; result `E:regularized-scaled-moment`: `E|u^{ε,δ}(a;T,x)|² ≤ B(T;a)=e(T+2)^d exp{C(a²R_α)^{1/ν}T^κ}`. `N→∞` at positive widths uses L:terminal-wick, not the unsmoothed theorem. Correct.
- **Tail passage.** `L:joint-fixed-order` gives `Y_n^{ε,δ}→X_n=S_n(g_n)` in `L²` (arbitrary relative widths); L:uniform-series-tail with `r=2`, `B_r=B(T;2)` proves absolute `L²` convergence of `u=ΣX_n` and the full regularized limit; final bound uses `B(T;1)`, not the larger tail `B(T;2)`. Correct.
- **Non-circularity.** Depends only on L:terminal-wick, L:uniform-series-tail, `P:interval-coefficients` (upstream), and `L:joint-fixed-order` (constructor, proved from Theorem 3.1 + homogeneous norms, *not* source Theorem 4.1/Lemma 4.4). Independent of `P:mixed`, `L:crude-corrected`, the source's Section 5, and (per the embedded downstream module) *precedes and independently supplies* the intrinsic-constant finiteness. Correct.
- **Constants.** `ν=3−α`, `β=4−α−α₀`, `κ=β/ν`, `R_α=απμ(B_1)/(2sin(πα/2))` (from `∫_0^∞u^{α−1}/(1+u²)du=π/(2sin(πα/2))`), `|B_{T+2}|/|B_1|=(T+2)^d`, `L=78`, `c=6^{α₀}`. All verified. Zero-covariance (`Γ=0`, `u=1`, bound `e(T+2)^d≥1`) correct.

## Required fixes before production gate

None for the mathematics. The three proofs and their upstream/constructor dependencies are consistent and complete as audited. Outstanding items are the *separate*, already-documented project gates, not defects of these proofs: (a) raster/PDF-image authentication of the imported source formulas (textual carrier only); (b) the fresh independent whole-paper cold-read gate; (c) global/full-goal/source-image/render/cold sign-off — none of which this Unit-D deep assignment is authorized to clear on its own.

## D01–D11 determination

All eleven risk checks **pass**. D01 (terminal-chain construction, mass `T^{2n}/(2n)!`, `√((2n−1)!!)V^{n/2}`, exact ratio, complex-amplitude `L²` convergence, no hidden d=3 density) ✓. D02 (exact Wick, coefficient 1 per pairing with `2^kk!` cancellation, odd=0, `1/n!` symmetrization, scalar/constant-data positivity only, no arbitrary-phase coefficient positivity) ✓. D03 (uniform tails, `r^{2n}E|Y_n|²≤B_r`, geometric tails, finite-partial-order-then-`N→∞`, `B_1≠B_r`, zero-noise) ✓. D04 (three shifted grids `h_j(n+(-1)^jt)`, `t∈{0,1/3,2/3}`, nesting via `3t∈ℤ`, scale `3|s−r|<h≤6|s−r|`, common cell, `6^{α₀}`, no stationary-`K_J` assumption) ✓. D05 (finite-J inventory `≤3(T/h_j+2)`, cumulative `≤78T/h_j`, `h_i≤78T/i`, `σ_I²=6^{α₀}|I|^{−α₀}`, covariance `K_JΓ_ε`, `L=78/c=6^{α₀}`, only-`R_α` dependence, finite-mode covariance not assumed nonnegative) ✓. D06 (compact-data localization, `f_T`, `C_sf_T=1` on cone, chain points `|y|+s<T+1`, volume ratio `(T+2)^d`, `L²(Ω;X)` norm not pointwise operator norm) ✓. D07 (finite-model point Wick sum, covariance `K_JΓ_ε`, no time reversal, nonnegativity incl. unequal/self/empty, partial-order moment ≤ full moment without samplewise monotonicity) ✓. D08 (author `(2.23)–(2.24)` Euler-Gamma truncated-Laplace `γ_δ^0≤|t|^{−α₀}`, spatial `p_{2ε}`, Green width before noise width, Bochner/pathwise identification, no arXiv-v1 or first-moment normalization) ✓. D09 (`J→∞` positive monotone convergence at fixed N, no infinite-depth field, `N→∞` via terminal lemma) ✓. D10 (amplitude `a²Γ ↦ a²R_α`, `r=2` tails, `a=1` final, no inflation to `B(T;2)`, same canonical `u` via separate `P:mild-construction`, no circular use) ✓. D11 (every `T≥1`/d=1,2,3/zero-`Γ`, `C=C(α,α₀)` with explicit `R_α`, negligible volume prefactor, no uniform-in-T rate, downstream confirms `T:full-upper` is an earlier independent premise, hand small-cases done) ✓.

## PROOF049–051 ledger

| Proof | Verdict | Checked steps | Limits/constants | Residual gaps |
|---|---|---|---|---|
| PROOF049 (6273–6329) `L:terminal-wick` | **FULLY_CHECKED** | Mass induction to `T^{2n}/(2n)!` (n=0,1,2 hand-checked); Hölder/Gaussian bound; Isserlis coefficient-1 (`2^k k!` cancellation hand-computed); posistivity; ratio `|r|√V T²/((2n+2)√(2n+1))→0`; complex-`r` absolute `L²` convergence; d=3 `p_η*G` Green limit | `M_n`, `(2n−1)!!`, coefficient 1, ratio `(2n+2)√(2n+1)` | None within the proof (only Gaussianity + `V<∞` used) |
| PROOF050 (6357–6377) `L:uniform-series-tail` | **FULLY_CHECKED** | Nonnegativity → `r^{2n}E|Y_n|²≤B_r`; fixed-order `L²` limit; geometric tail; double-limit `(ε,δ↓0, N→∞)`; norm continuity passes `B_1` | `B_r^{1/2}r^{−n}`; `r^{−(N+1)}/(1−r^{−1})`; factor 2 | None within the proof |
| PROOF051 (6397–6618) `T:full-upper` | **FULLY_CHECKED** | Three-grid domination `6^{α₀}`; nesting via `3t∈ℤ`; scale existence; inventory `≤78T/h_j`; interval model covariance `K_JΓ_ε`; `P:interval-coefficients` application; `f_T` localization; monotone comparison; amplitude `a²Γ↦a²R_α`; tail `r=2`; non-circularity | `(T+2)^d`, `κ=(4−α−α₀)/(3−α)`, `ν=3−α`, `R_α=απμ(B_1)/(2sin(πα/2))`, `L=78`, `c=6^{α₀}`, `C=C(α,α₀)` | (a) upstream `P:interval-coefficients` and `L:joint-fixed-order` accepted as supplied proof bodies (statements/constants/exponents/usage audited; exhaustive per-line re-derivation outside deep-unit target scope); (b) source fidelity textual only (raster verification separate) |

## One-line summary

PROOF049–051 are all correct as stated and in full: terminal-chain Wick, uniform geometric tails, and the full upper bound `𝔼u²(T,x) ≤ e(T+2)^d exp{C R_α^{1/(3−α)} T^{(4−α−α₀)/(3−α)}}` with parameter-only constant, every constant and limit hand-checked, establishing unchanged Goal G:upper without circularity or source-normalization contamination.