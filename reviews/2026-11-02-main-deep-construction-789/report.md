# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

Scope note (honesty): reviewed only the embedded line-numbered `target.tex` excerpt (lines 1–319), the embedded `upstream-model.tex` context (damped norms, fixed-order construction), the held author-version primary text (Theorem 3.1, Definition 2.1, (2.12), pp. 9–21), `time-boundary-context.tex`, and `author-case2-test-context.md`. I did not read Progress.md / Review.md / HANDOFF.md / reviews-tree state. No images were supplied; this carries no image/functional-render or independent cold-read credit. Full213/global/source/image/cold gates are untouched by this unit.

## Critical findings

None. I found no proof-breaking sign error, incorrect constant, false identity, or invalid limit in PROOF007, PROOF008, or PROOF009. The three arguments are internally correct and their constants were checked by hand.

## Noncritical findings

1. **Strong-measurability / spatial-continuity argument is compressed.** Lines 201–219 state the rescaling-to-unit-domain Bochner construction and the “joint spatial stationarity” step in prose rather than fully expanded measure-theoretic detail. The steps are standard and sound: (a) at positive widths the Gaussian evaluations are jointly measurable (continuous modification, source p. 9) with the finite Wick bound `‖Π W‖₂ ≤ √((2n-1)!!) V^{n/2}` and finite Green masses giving Bochner domination; (b) the stationarity equality `‖Y^b_n(s,y) − X_n(s,y)‖₂ = ‖Y^b_n(s,0) − X_n(s,0)‖₂` holds because a joint spatial translation moves all vertices (including the fixed root) in the two-chain diagram while preserving every Green increment; only the field is translated, and the coupled noise is spatially stationary. This is correct but deserves a sentence more of expansion for readers.
2. **Product identification `W_a u = Σ_n W_a X_{n-1}` is compressed.** Lines 287–298 rely on: partial sums `U_N → u` in L²; the occupied estimate makes `Σ_n ‖W_a X_{n-1}‖₂` converge, so `W_a U_N → Z` in L²; along an a.s. subsequence `W_a U_N → W_a u` a.s.; hence `Z = W_a u`. This is valid (multiplication by a fixed Gaussian multiplier preserves a.s. convergence; no boundedness of multiplication on all of L² is invoked). The wording “their products converge by this estimate” elides the subsequence-identification detail, but the logic is there and correct.
3. **Import of source Theorem 3.1.** The manuscript imports the universal pairing bound as an input under its stated hypotheses (finite nonnegative-covariance measures, Laplace temporal kernels); its application verifies those hypotheses (lines 104–126, 1234–1241). It does not re-derive, and does not invoke, the source’s printed Case-2 shifted-cross-kernel equality that `author-case2-test-context.md` flags. The author-supplied repair (stationary-covariance Cauchy–Schwarz on the two different translates) is consistent with, and does not alter, the manuscript’s import. So the manuscript is faithful to the theorem’s hypotheses; any residual issue is inside the source, not this derivation.
4. **Minor phrasing.** In Lemma `L:crude-corrected` the prelude fixes `θ₀=1` from Lemma `L:damped-homogeneous-norms` (line 6), while the lemma statement says “suitable `C<∞` and `θ₀>0`”. Harmless; the proof only needs `θ₀=1`. Also lines 246–247 say the terminal-kernel moment bound “was established before Lemma L:vertex-crude”; it is established by the same Wick bound that underlies `L:vertex-crude` (which admits arbitrary vertexwise widths, including the mixed `(b,a)` profile), so the claim is correct.

(No text-carrier garbling was relied upon for `target.tex`; the LaTeX equations there are clean. The garbled source-PDF fractions are correctly cross-read against the manuscript’s own `L:damped-homogeneous-norms` and the note at upstream lines 899–904.)

## Checked derivations

**PROOF007 — Lemma `L:crude-corrected` (E:crude-corrected).**
- Telescoping: per chain `Π_l e^{-θ(s_l−s_{l−1})} = e^{-θ s_n}` (chain 1) and `e^{-θ s_{2n}}` (chain 2); since `s_n,s_{2n} ≤ t`, `e^{-θ(s_n+s_{2n})} ≥ e^{-2θt}`. Undamped pairing ≤ `e^{2θt}` · damped pairing. Correct.
- Theorem 3.1 pair accounting: `#Q₀ = #Q₁`, `#Q₂` even, and total pairs `n = #Q₁ + #Q₂/2`, hence `#Q₀ + #Q₂/2 = n` and `2#Q₀ + #Q₂ = 2n`. Norm powers: `θ^{-2·#Q₀}` (N₀) times `θ^{0·#Q₁}` (N₁ ≤ C₀) times `θ^{-1·#Q₂}` (N₂ ≤ C₀θ^{-1}) ⇒ exact `θ^{-2n}`. Constant `(2C₀)^{#Q₁}C₀^{#Q₂} ≤ Cⁿ`. Correct.
- Norm decay for `θ ≥ θ₀ = 1`: `N₁(θ)=θ^{α+α₀−2}N₁(1) ≤ N₁(1)` (since `α+α₀<2`); `N₂(θ)²=θ^{-β}N₂(1)²` with `β=4−α−α₀>2`, so `N₂(θ) ≤ C₀ θ^{-β/2} ≤ C₀ θ^{-1}` (since `β/2>1`). `N₀(θ)=θ^{-2}` exact. Correct.
- Finite-spectral regularization: Gaussian multiplier `e^{-ε|ξ|²/2} ≤ C(1+|ξ|²)^{−(2−α₀)/2}`, integrable by (1.5); temporal caps `[0,δ^{-1}]`; Green smoothing `G_η=p_η*G` has Fourier multiplier ≤ 1 and unchanged mass. Bounds uniform in regularizations; no radial density used. Correct.
- Limit transfer: `η↓0` at fixed noise widths (L², observed squared moments), then `(ε,δ)→0` via `L:joint-fixed-order`; d = 1,2 need only the latter. Correct; no pointwise δ-covariance bound used.
- `θ = θ₀ + n/t` ⇒ `e^{2θt} = e^{2θ₀t} e^{2n}` and `(θ₀+n/t)^{-2n} ≤ t^{2n} n^{-2n}`. `P_n = (2n)!/(2^n n!)`; `(2n)! ≤ (2n)^{2n}` ⇒ `P_n n^{-2n} ≤ 2^n/n!`. Absorbing `2^n e^{2n}` into `Cⁿ` gives `e^{2θ₀t} Cⁿ t^{2n}/n!`. Correct.
- Weighted Cauchy–Schwarz: `(Σ zⁿ/√(n!))² ≤ (Σ 2^{-n})(Σ (2z²)ⁿ/n!) = 2 e^{2z²}`. Correct ⇒ `E u² ≤ 2 e^{2θ₀t + 2Ct²}`.
- Ratio test for square-root summability: `(√C t)^n/√(n!)` has ratio `√C t/√(n+1) → 0`. Correct.

**PROOF008 — Lemma `L:vertex-crude` (E:vertex-crude, E:vertex-summability).**
- Wick (2.19) with joint covariance (2.11) on the squared copy: edge `(j,l)` covariance `γ⁰_{δ_j∨δ_l}(s_j−s_l) γ_{ε_j+ε_l}(y_j−y_l)`. Correct; uses the same (dependent) field, no independence of the two moment copies.
- Terminal-chain reversal `s'_j=t−s_{n+1-j}`, `y'_j=x−y_{n+1-j}`: reverses Green increments, negates spatial differences and each covariance argument; all kernels (`G`, `γ`, `γ⁰`) even, so signs absorbed; vertex widths only permute. Correct.
- Edge hypotheses for Theorem 3.1: spatial spectral measure `e^{-(ε_j+ε_l)|ξ|²/2} μ(dξ)` finite by (1.5); temporal Laplace domain `[0,(δ_j∨δ_l)^{-1}]`. Correct.
- Uniform-in-width norm bounds with correct positivity order: N₁ integrand `1/((θ+λ)²+|ξ|²)` nonnegative; N₂: integrate time first (positive-definite `γ⁰` gives nonnegative per-ξ quadratic form), then remove the spatial Gaussian multiplier (≤1) and enlarge temporal truncation to full `|s−t|^{-α₀}`. Constants independent of all vertex widths. Correct.
- `D = max{1,2C₀}`: since `D ≥ 2C₀` and `D ≥ C₀`, `(2C₀)^{#Q₁}C₀^{#Q₂} ≤ D^{#Q₁+#Q₂} ≤ D^{2n} = C₁ⁿ` with `C₁ = D²`. Correct.
- `‖Y^a_n‖₂² ≤ P_n e^{2θt} C₁ⁿ θ^{-2n}`; `θ=θ₀+n/t`; `P_n n^{-2n} ≤ 2^n/n!` ⇒ `q_n(t)=e^{θ₀t}C^{n/2}t^n/√(n!)`. Correct. Green width removed first at fixed positive noise widths, then joint noise limit `X_n` via `L:joint-fixed-order`; bound passes. Correct.
- Ratio: `√(n+2) q_{n+1}(T)/(√(n+1) q_n(T)) = √C T √(n+2)/(n+1) → 0`. Correct ⇒ `Σ√(n+1) q_n(T) < ∞`.

**PROOF009 — Proposition `P:mild-construction` (E:mild-construction).**
- Occupied multiplication `‖HF‖₂ ≤ 2√(n+1)‖H‖₂‖F‖₂`: normalized Hermite creation `√(a₁+1) ≤ √(n+1)`, annihilation `√(a₁) ≤ √n`; operator `a + a†` has norm `≤ √n + √(n+1) ≤ 2√(n+1)`. `H=0` trivial. Approximation in the degree-closed chaos identifies `HF`; allows `F` to depend on `H`. Correct (no independence or all-L² boundedness assumed).
- `V_a = γ⁰_δ(0) γ_{2ε}(0) < ∞` for `a>0` (finite-width endpoint; blows up only as `a↓0`). Correct.
- Fixed-external domination `‖W_a X_{n−1}‖₂ ≤ 2√n √V_a q_{n−1}(T)`, Green mass `t−s`, so the Bochner integral `I_{n,a}` exists. Correct.
- Terminal-kernel Fubini: `Y^{(b,a)}_n = ∫ G(t−s,x−dy) W_a(s,y) Y^b_{n−1}(s,y) ds`; inner `b→0` preserved by the occupied bound + uniform `q_{n−1}(T)` domination; `n=1` exact. Gives `I_{n,a}=lim_b Y^{(b,a)}_n` and `sup_a ‖I_{n,a}‖₂ ≤ q_n(t)`, derived from `L:vertex-crude` (not from the `V_a`-dependent domination). Correct.
- d=3 product spatial continuity: two-term split using `W_a(y)(X_{n−1}(y)−X_{n−1}(y'))` and `(W_a(y)−W_a(y'))X_{n−1}(y')`, both → 0 (continuity of `X_{n−1}(s,·)` and of smoothed `γ_{2ε}`). Correct, uniform in `y`.
- Green limit at fixed external width: partition-of-unity + scalar vague convergence + tightness/uniform bound against `p_η*G_{t−s} → G_{t−s}`; dominated time integration via mass `t−s`. Green limit occurs at positive noise widths before the inner noise limit; no Green/noise interchange. Correct.
- External-vertex limit using joint `L:joint-fixed-order` with a width-hypercube `r`: `‖Y^{(b,a)}_n − X_n‖ < ζ`, fix `a<r`, `b→0` ⇒ `‖I_{n,a}−X_n‖ ≤ ζ`; arbitrary relative rates; no partial-limit theorem. Correct.
- Full product: `Σₙ ‖W_a X_{n−1}‖₂ ≤ 2√V_a Σ√n q_{n−1}(T) < ∞` (uniform in `s`); closedness + a.s. subsequence identifies the limit with `W_a u` (actual fixed `u`, not a regularized `u_a`). Dominated Green integration ⇒ `I_a = Σ_n I_{n,a}`. Correct.
- Tail: `‖I_a − (u−1)‖₂ ≤ Σ_{n=1}^N‖I_{n,a}−X_n‖₂ + 2Σ_{n>N}q_n(t)` (each difference bounded by `q_n(t)+q_n(t)`, independent of `a`). Let `a↓0` then `N→∞` using `Σ q_n(t)<∞`; tail uniform in `a` despite `V_a↑∞`. Matches Definition 2.1/(2.12) with the d=3 generalized-integrand convention and random factor fixed. No uniqueness claim; source (5.3)–(5.4) and §5(ii) not imported. Correct.

**Hand controls (distinct from proofs).**
- Correlated `H=F` standard Gaussian: `‖H·F‖₂ = √(E H⁴) = √3`; bound `2√2 ≈ 2.83` holds (an independence factorization would give the wrong value `1`, so the dependence-respecting bound is what is needed, and it is what is used).
- `n0/n1/n2/self-contractions`: `#Q₀=#Q₁`, `#Q₀+#Q₂/2=n`, hence `2#Q₀+#Q₂=2n`; the source’s own (3.6) examples (`n=2,3`, pp. 15) and the induction (pp. 15–21) confirm the pair accounting, including domestic/self-pairings within a chain.
- Zero Γ: bounds degenerate correctly (all norms 0, `C=0` admissible); mild equation trivial `I_a=0=u−1`.
- Finite-width endpoints: `V_a<∞` for `a>0`; `γ⁰_δ(0) ~ δ^{-α₀}`, `γ_{2ε}(0) ~ ε^{-α}` blow up only at `a=0`, and the tail argument deliberately avoids `V_a`.

## Required fixes before production gate

None within the verified scope (PROOF007–009, MILD01–MILD12). Optional, non-blocking improvements: expand the strong-measurability/stationarity paragraph (lines 201–219) and the `W_a u` subsequence-identification sentence (lines 287–298) by one or two sentences each; and add a sentence noting that Theorem 3.1 is imported under its stated hypotheses and is not re-derived here. These are clarity edits, not correctness repairs.

## MILD01–MILD12 individual determinations

1. **MILD01 — PASS (FULLY_CHECKED).** Damped N₀/N₁/N₂ with exact `θ^{-2}`, `≤C₀`, `≤C₀θ^{-1}` at `θ≥θ₀`; `#Q₀=#Q₁`, `#Q₀+#Q₂/2=n`; factor 2 on Q₁ absorbed; exact `θ^{-2n}`; `P_n` pairing count; common-horizon reversal with independent roots; finite edge measures/capped Laplace domains satisfy Theorem 3.1 hypotheses; Green (η) before joint noise limit; no source Appendix normalization or time-uniform (5.4) assumption.
2. **MILD02 — PASS (FULLY_CHECKED).** `θ=θ₀+n/t` ∀t>0; `e^{2θt}` factor explicit; `P_n n^{-2n} ≤ 2^n/n!`; constants independent of n,t; ratio-test norm series independent of `P:mixed`; n₀=0 handled; weighted CS `sum² ≤ 2e^{2z²}`. The `e^{Ct²}` result is explicitly the nonsharp quadratic bound, no circular `T:full-upper`.
3. **MILD03 — PASS (FULLY_CHECKED).** Joint covariance `ε_j+ε_l` / `δ_j∨δ_l`; per-chain reversal; finite Gaussian-weighted edge spectral measures; norm bounds uniform in vertex widths; N₂ positivity in correct spectral order; `D=max{1,2C₀}`, `C₁=D²`; Green before noise; `q_n(t)` and the `√(n+1)q_n(T)` ratio; no independence of the two moment copies.
4. **MILD04 — PASS (FULLY_CHECKED).** Closed Gaussian polynomial spaces with lower contractions; occupied multiplication of correlated linear Gaussian `H` via `H/‖H‖` first coordinate and normalized Hermite creation `√(n+1)`/annihilation `√n`; constant `2√(n+1)`; H=0 case; approximation + a.s.-subsequence identifies `HF`; no independence or all-L² bounded multiplication assumed.
5. **MILD05 — PASS (FULLY_CHECKED).** Positive-width joint measurability via unit-domain rescaling, jointly measurable Gaussian evaluations, bounded moments + finite Green mass ⇒ Bochner domination; countable-width pointwise L² limits give `X_n`, then `u`; continuity (not merely a.e. representatives) is separately established, which is what the singular d=3 sphere measure requires.
6. **MILD06 — PASS (FULLY_CHECKED).** Spatial L² continuity at positive widths; joint spatial stationarity gives `‖Y^b_n(s,y)−X_n(s,y)‖₂ = ‖Y^b_n(s,0)−X_n(s,0)‖₂` (joint translation preserves all Green increments; only the field is translated); uniform-in-y convergence at fixed s; `X_n(s,·)` and `u(s,·)` have continuous L² representatives by `q_n` summability. No unwarranted time/noise-width rate.
7. **MILD07 — PASS (FULLY_CHECKED).** `a` fixed, `V_a=γ⁰_δ(0)γ_{2ε}(0)`; `‖W_a X_{n−1}‖₂ ≤ 2√n√V_a q_{n−1}(T)`; Bochner integrand with Green mass `t−s`; inner-regularization L² limit preserved by the occupied bound under dependence; terminal-kernel Fubini; `n=1` exact; uniform `q_n` from vertex-crude (not `V_a`).
8. **MILD08 — PASS (FULLY_CHECKED).** Two-term product continuity; uniform y norm; partition-of-unity + tightness proves `p_η*G_{t−s} → G_{t−s}` for the vector integral at fixed s; dominated time integration via `t−s`; Green limits at positive noise widths precede the inner noise limit; no Green/noise exchange.
9. **MILD09 — PASS (FULLY_CHECKED).** Uses joint `L:joint-fixed-order` width-hypercube to get `‖Y^{(b,a)}_n−X_n‖<ζ` for all small widths; fix external `a`, send inner `b→0` ⇒ `‖I_{n,a}−X_n‖≤ζ`; arbitrary ε/δ rates; no partial-limit theorem; common terminal time only; no unequal-terminal claim.
10. **MILD10 — PASS (FULLY_CHECKED).** Unbounded total chaos per term bounded by `q_n`; uniform `Σ‖W_a X_{n−1}‖₂ ≤ 2√V_aΣ√n q_{n−1}(T)`; multiplication closed (not bounded); a.s.-subsequence identifies `W_a u`; dominated Green integration; actual fixed `u` (not `u_a`); product series spatial continuity and Green limit.
11. **MILD11 — PASS (FULLY_CHECKED).** Finite-N external limit then `N→∞` with `2Σ_{n>N}q_n(t)`; tail uniform in external width despite `V_a↑∞`; `I_a→u−1` in L²; matches Definition 2.1/(2.12) and d=3 Green convention with random factor fixed; no uniqueness assertion; §5(ii)/(5.3)–(5.4) unused.
12. **MILD12 — PASS (FULLY_CHECKED).** Acyclic 004–006 → 007/008 → 009; `P:mixed` consumes the bounds but is not used to derive them (007/008/009 cite only the damped norms and `L:joint-fixed-order`, never `P:mixed` for their bounds); Theorem 3.1 applied under exact hypotheses, no shifted-cross-kernel PSD interpretation; correlated `F=H` hand test, `n0/n1/n2/self-contraction`, zero-Γ, finite-width endpoint controls all consistent.

## PROOF007–009 ledger

| ID | Verdict | Checked steps | Limits | Constants | Residual gaps |
|---|---|---|---|---|---|
| PROOF007 (`L:crude-corrected`, 989–1040) | **FULLY_CHECKED** | Telescoping `e^{-θ(s_n+s_{2n})}≥e^{-2θt}`; Theorem 3.1 pair accounting `2#Q₀+#Q₂=2n`; smoothed finite-spectral/truncated-Laplace hypotheses; norm bounds `N₀=θ^{-2}, N₁≤C₀, N₂≤C₀θ^{-1}`; `P_n n^{-2n}≤2^n/n!`; weighted CS. | `η↓0` at fixed noise widths, then joint `(ε,δ)→0` via `L:joint-fixed-order`; d=1,2 only the latter. | Exact `θ^{-2n}`; final `e^{2θ₀t}Cⁿt^{2n}/n!`; `u²≤2e^{2θ₀t+2Ct²}`. | None (minor θ₀ phrasing). |
| PROOF008 (`L:vertex-crude`, 1058–1116) | **FULLY_CHECKED** | Wick with joint (2.11); chain reversal/evenness; edge hypotheses; uniform-in-width N₁/N₂ positivity order; `D=max{1,2C₀}`, `C₁=D²`; ratio test. | Green width before noise width; joint noise limit via `L:joint-fixed-order`. | `q_n(t)=e^{θ₀t}C^{n/2}t^n/√(n!)`; ratio `√C T√(n+2)/(n+1)→0`. | None. |
| PROOF009 (`P:mild-construction`, 1139–1286) | **FULLY_CHECKED** | Occupied bound `2√(n+1)`; Bochner `I_{n,a}`; terminal-kernel Fubini; product spatial continuity; Green limit via partition of unity; joint→external width hypercube; full-product closedness; tail `2Σ_{n>N}q_n(t)`. | Inner `b→0` then external `a→0` (arbitrary rates); Green limit at positive noise widths; `N→∞` tail (uniform in `a`). | `V_a=γ⁰_δ(0)γ_{2ε}(0)`; `2√n√V_a q_{n−1}(T)`; `sup_a‖I_{n,a}‖≤q_n(t)`; final `I_a→u−1`. | None (two compressed-but-valid paragraphs, see noncritical 1–2). |

## One-line summary

PROOF007–009 are correct and complete under their stated hypotheses and imported Theorem 3.1: constants, exponents, width/Green/noise limit orders, Gaussian product closure, and the onefold mild-equation tail all verify by hand, with no blocking defect — PASS_WITH_NOTES at HIGH confidence.