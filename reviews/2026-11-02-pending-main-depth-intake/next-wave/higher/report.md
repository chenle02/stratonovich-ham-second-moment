# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. Every load-bearing identity, constant, exponent, sign, boundary term, and limit claim in PROOF020–PROOF023 and HD01–HD14 survives direct hand re-derivation. The final coefficient `K = 12M[Γ(1−δr)·D_a]^{1/r}·Z_θ^{1/r′}`, the factorial power `q = 3−α`, the time power `β = 4−α−α₀`, and `β/q = κ` all reproduce with the exact constants stated in the manuscript.

## Noncritical findings

1. **Cross-reference imprecision (cosmetic).** In PROOF020 (review-material lines 2734–2737) the dimension-three Green-smoothing removal is called “detailed in Proposition P:low-alpha-upper.” That proposition was stated for `0<α≤1`, whereas the present context is `1<α<2−α₀`. The argument is, however, reproduced self-contained immediately before the pointer (lines 2728–2736: bounded smoothed covariances, weak convergence of finite Green-measure products, mixed-Green joint covariance limit giving the fixed-order L2 Cauchy property). The mechanism is dimension/covariance-independent and does not depend on `α≤1`; no repair is needed, only a more precise pointer.

2. **`at least` vs `equal` in Dₐ absorption (cosmetic).** Line 2695 says “its square is at least `D_a^{-k}(k!)^{2−δr}`.” The bound `Γ(1+ak) ≥ e^{−1}(a/e)^{ak}k^{ak}` squared gives exactly `e^{−2}(a/e)^{2ak}(k!)^{2a}`, which equals `D_a^{-k}(k!)^{2−δr}` only under the `k≥1` correction the proof already states; the claimed `≥` direction is correct because `e^{−2} ≥ e^{−2k}` for `k≥1`. The wording “at least” is slightly loose but the conclusion is right and the `k≥1` clause is present.

3. **No raster images supplied.** Per the scope disclosure, image-based certification is impossible here. All load-bearing formulas — (2.5) Green measures, (3.1)–(3.6) Theorem 3.1, Theorem 4.1 (4.3), and Balan–Conus Theorem 2.1(b) — are present in the embedded text carriers and read unambiguously; no decisive step depends on a garbled page.

## Checked derivations

- **Parameter window.** `1/(1−α₀) < r < 1/δ`, `δ=α−1`. Nonempty iff `δ < 1−α₀`, i.e., `α−1+α₀<1 ⟺ α+α₀<2` (line 2628). `r>1` since `α₀<1`. `θ=α₀r′<1 ⟺ r>1/(1−α₀)`. `a=1−δr/2 ∈ (1/2,1) ⟺ δr<1`. `q=3−α>1` since `α<2`. `β/q=κ` by definition.
- **Witness:** `α=3/2, α₀=1/4` (d=3, `α+α₀=7/4<2`): `δ=1/2`, interval `(4/3, 2)`, rational witness `r=5/3`; `θ=α₀·(5/3)/(2/3)=5/8<1`, `a=1−3/8=5/8∈(1/2,1)`.
- **Dirichlet integral.** `∫_{Ω_{m,n}} H_D^r = Γ(1−δr)^k t^{(2−δr)k}/[Γ(1+m−δr k₁)Γ(1+n−δr k₂)]`. Re-derived: t-power is `Σ aₗ = (m−δr k₁)+(n−δr k₂) = (2−δr)k` (terminal-gap exponent zero contributes `Γ(1)=1`, no extra t-power but `+1` in the denominator). Direct k=1 check for split (1,1) equals `t^{2−δr}/(1−δr)`, matching.
- **Log-convexity.** Denominator sum `=2+2ak`, average `1+ak`; `Γ(x)Γ(y) ≥ Γ(1+ak)²`.
- **Dₐ lower bound.** `Γ(1+ak) ≥ ∫_{ak}^{ak+1} x^{ak}e^{−x}dx ≥ e^{−1}(a/e)^{ak}k^{ak} ≥ e^{−1}(a/e)^{ak}(k!)^a`; squared `≥ D_a^{−k}(k!)^{2−δr}`, constants exact for `k≥1`.
- **Pairing/symmetry.** `∫_{[0,t]^{2k}} F_k = P_k(Z_θ t^{2−θ})^k`; `Z_θ = 2/[(1−θ)(2−θ)]` (verified by direct double integral). Split restriction gives `/ (m!n!)`; `m!n! ≥ (k!)^2`, `P_k ≤ 2^k k!`, `k^k ≥ k!`, `2k+1 ≤ 3^k`. Final accumulation: `2^kM^k · 2^k[k^{-k}P_k] → 4^kM^k`; splits → `3^k`; so `K=12M[…]`.
- **Exponent bookkeeping.** Per-k time exponent `1 + (2−δr)/r + (2−θ)/r′ = 3−δ−α₀ = β`; factorial exponent `(2−δr)/r + 2/r′ = 2−δ = q`.
- **F₃ radial form.** `F₃ = [(1+ρ)^v − |1−ρ|^v]/(2vρ)`, `v=2−α`; maximum `F₃(e₁)=2^{1−α}/(2−α)`, so `M₃=c2^{1−α}/(2−α)`; `α=3/2` gives `c√2`.
- **2D small ball.** `G₁(B(w,R)) ≤ 2R^{3/2}` for `R≤1/4` (constants `2/√7 < 2` and `2√2/π < 2`); layer cake gives `M₂ = c(4^α + 2α·4^{α−3/2}/(3/2−α))`; divergence at `α=3/2`.
- **Anisotropic obstruction.** `a₁=(1+max{2−α,α−1})/2`, `a₂=α−a₁`: `0<a₁,a₂<1` and `a₁+a₂/2>1` verified for all `1<α<2` (case split at `α=3/2`); beta factor `B((1−a₂)/2,1/2)` and divergent `u^{-a₁−a₂/2}`; sphere→disk projection exactly `G₁^{(2)}` (two caps, Jacobian `(1−|y|²)^{−1/2}/(4π)` each).

## Explicit HD01–HD14 rows

| Row | Status | Concrete verification |
|---|---|---|
| HD01 Parameter window | FULLY_CHECKED | Nonempty iff `δ+α₀<1` (lines 2609, 2628–2629). Witness `α=3/2, α₀=1/4, r=5/3` rational; strict endpoint behavior `r→1/(1−α₀)` forces `θ↑1`, `r→1/δ` forces `a↓1/2`; no α-limit inference made. |
| HD02 Descending invariant | FULLY_CHECKED | Lines 2643–2663: at closing `l` only pair `(i,l)` involves `y_l` (`γ_ε(y_l+z)`); at opening the partner is removed and `∫G_{h_l}=h_l`; Tonelli by positivity; widths arbitrary (`ε_e>0`, `η_l≥0`). Order-2 splits (2,0),(1,1),(0,2) and order-4 all obey the invariant; opening AGM uses `Σ openings ≤ Σ increments ≤2t`. No interleaving assumption (order is by block label, not time). |
| HD03 Hölder factors/Dirichlet | FULLY_CHECKED | Hölder on counting×Lebesgue (lines 2668–2672); factors `H_D^r`, `T_D^{r′}` integrable via `δr<1`, `θ<1`. Dirichlet: terminal gap parameter 1, empty chain `Γ(1)=1`, t-power `(2−δr)k`, denominator mean `1+ak`. Verified k=1 direct match. |
| HD04 Log-convex Gamma | FULLY_CHECKED | Integral over `[ak,ak+1]` gives `e^{−1}(a/e)^{ak}k^{ak}`; `D_a=e²(e/a)^{2a}`; `Γ(1+ak)² ≥ D_a^{−k}(k!)^{2−δr}` with exact (not just asymptotic) constants, valid `k≥1`. |
| HD05 Pairing sum/symmetry | FULLY_CHECKED | `Z_θ^k t^{(2−θ)k}` full-cube; `/ (m!n!) ≥ (k!)^2`; `P_k≤2^k k!`, `k^k≥k!`, `2k+1≤3^k`; powers → `4M`, then `12M`, factorial `q`, time `β`. k=1 and nonbalanced/equal splits all consistent; cross terms retained. |
| HD06 Regularization→solution | FULLY_CHECKED | Chen (2.9),(2.11),(2.23)–(2.24); endpoint widths sum via `(2.11)`; d3 positive Green `G_η`, fixed-noise Green-zero covariance limit, mixed-Green L2 Cauchy; then joint fixed-order noise limit (L:joint-fixed-order) valid for `α>1`; L1 products via Cauchy–Schwarz; P:mixed infinite series used without circularity; zero chains constant one. |
| HD07 Entire moment sum | FULLY_CHECKED | `Σ z^k/(k!)^q ≤ e^{qz^{1/q}}` for `q>1`, all `t>0`,`x`,`k₀=1`; constants explicit/order-time-width independent. Jensen gives `𝔼u ≤ exp{qK^{1/q}t^κ/2}`; `2L_* ≤ qK^{1/q}` explicitly conditional on intended first-moment lower bound; exponent calibration `α₀→0` only; H:spatial-maximum does not cover all homogeneous `α>1`. |
| HD08 Green measures/F₃ | FULLY_CHECKED | (2.5) masses `h`, `G_h(hA)=hG₁(A)`; `∫=c h^{1−α}F_d(z/h)`; `F₃` radial formula and normalization verified; monotonicity `ρ<1` by convex chord, `ρ>1` by distance derivative; continuity 0/1; `M₃=c2^{1−α}/(2−α)`; `α=3/2` gives `c√2`; unsmoothed max distinct from uniform-width optimum. |
| HD09 2D small ball | FULLY_CHECKED | `G₁(B(w,R))≤2R^{3/2}` with all constants (`2/√7`, `2√2/π`); inside/outside disk; `A≥1/2` slices, `L+x>1`; layer-cake at `R=1/4`; `M₂` denominator `3/2−α`, restriction `α<3/2` genuine; no rearrangement claim. |
| HD10 Gaussian averaging | FULLY_CHECKED | Mass-one averaging preserves maxima for all `ε>0, η≥0`; approximate identity off the singular point with local continuity, near-origin integrability, Gaussian tail; Fatou recovers optimal `M₃` (singular point sphere-null); fixed-width positivity kept; no function/d distribution substitution outside the stated Riesz case. |
| HD11 Riesz covariance corollary | FULLY_CHECKED | Local integrability `α<d`, tempered/homogeneous; Gamma mixture normalization `1/Γ(α/2)∫s^{α/2−1}e^{−s|x|²}`; complex autocorrelation `ψ=φ*φ̃`, absolute Fubini via `∫|x|^{−α}|ψ|<∞`; ranges `α+α₀<2`, original dimension restrictions, H:spatial-maximum discharged with all widths; no endpoint (`α=3/2` in d2) or broader covariance. |
| HD12 2D Riesz obstruction | FULLY_CHECKED | Wedge `0<1−|y|²≤2ρ`, angular `c/(3√2)`, exponent `1/2−α`, logarithmic at `3/2`; Fatou extends unsmoothed divergence to failure of uniform positive-width bound; kept distinct from existence/full-scale failure (lines 2960–2963). |
| HD13 Anisotropic counterexample | FULLY_CHECKED | `0<a₁,a₂<1`, `a₁+a₂/2>1` for all `1<α<2`; local/tempered; product Gaussian PSD (x₃-independent constant included); beta factor rederived `B((1−a₂)/2,1/2)`; divergent `u^{-a₁−a₂/2}`; sphere→disk projection exactly `G₁^{(2)}`; sample `α=3/2 → a₁=a₂=3/4, a₁+a₂/2=9/8>1`; near-endpoint inequalities hold; no hidden spectral-density assumption. |
| HD14 Uniform smoothing obstruction | FULLY_CHECKED | Product Gaussian factorization; 1D approximate-identity limit off each axis; Green-null singular axes in d2/d3; Fatou infinity; `η=ε` positive-width variant; product kernel explicitly unbounded along axes (line 2931–2932), no bounded-at-infinity claim; conclusions conditional/alternative; residual global/source-image/cold/actual-constant gates stated (lines 2941–2963); no broadening to main theorem or Skorohod. |

## Explicit PROOF020–PROOF023 rows

| Proof | Status | Verification |
|---|---|---|
| PROOF020 P:higher-transfer | FULLY_CHECKED | Window, invariant, Hölder exponents, Dirichlet normalization, Dₐ constants, symmetry, and final accumulation all re-derived; `K=12M[Γ(1−δr)D_a]^{1/r}Z_θ^{1/r′}`, time `β`, factorial `q`; passage to `A_k`/`𝔼u²` valid with all hypotheses retained. |
| PROOF021 L:higher-riesz | FULLY_CHECKED | `F₃` formula/normalization, convex-chord and distance-derivative monotonicity, continuity, peak `2^{1−α}/(2−α)`; 2D small-ball `2R^{3/2}` and layer-cake `M₂` re-derived with all constants; averaging and Fatou optimality correct. |
| PROOF022 C:higher-riesz | FULLY_CHECKED | Riesz covariance locally integrable (`α<d`), tempered, homogeneous `−α`; Gamma-mixture PSD with absolute Fubini; stated ranges satisfy `α+α₀<2`, additional spatial hypothesis discharged uniformly in all widths; no endpoint/broader inclusion claimed. |
| PROOF023 P:higher-obstructions | FULLY_CHECKED | 2D Riesz divergence (`3/2≤α<2`, wedge, `c/(3√2)`, exponent `1/2−α`); anisotropic `a₁,a₂` construction valid for all `1<α<2`, divergent `u^{-a₁−a₂/2}`; sphere→disk projection exact; Fatou/`η=ε` extension rigorous; scope kept distinct from existence/scale. |

## Required fixes before production gate

None required. Two optional editorial improvements (noncritical findings 1 and 2): (a) replace the “detailed in Proposition P:low-alpha-upper” pointer at lines 2734–2737 with “detailed in Proposition P:lower-alpha/… (or: as in the dimension-three inner-limit argument just given)” to avoid the `α≤1` context mismatch; (b) sharpen “at least” to “equal to” with the `k≥1` clause already stated.

## One-line summary

PROOF020–PROOF023 and HD01–HD14 are fully checked and correct by hand; all signs, boundary terms, constants, exponents, and asymptotics reproduce, with the conditional nature of the convolution-bound route and its residual gates honestly scoped — no required repairs.

## Limitations

- Bounded unit only: this does not transfer credit to the unrelated S:interval-upper full-class argument, to zero-covariance/mild-equation/image coverage, or to any final whole-paper cold read; those gates remain open per scope.md and PROJECT-GOAL.md.
- No raster images were supplied, so no image-based source certification was possible; all decisive formulas were read from the embedded text carriers (held Chen pp. 7, 14–16, 22; Balan–Conus p. 1492) without ambiguity.
- Historical review annotations and votes in the source excerpts were treated as non-premises; every step was re-derived from the supplied bodies and held primary statements.