# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I found no proof-logic errors, false identities, hidden hypotheses that invalidate the stated conclusions, wrong signs, wrong boundary terms, incorrect constants, or invalid asymptotic claims in PROOF210–213 themselves. All four reconstructions close exactly and the two Lean conditional deductions match their analytic premises precisely.

Caveat governing the verdict: PROOF212 and parts of PROOF211/213 consume upstream facts (the spatial occupation four-linear extension, the temporal equilibrium Gamma/Beta mass, the occupation ceiling bracket, the variational/intrinsic second-moment theorem). Those upstream modules are *named* dependencies, not re-derived inside PROOF210–213; their use is verified, their internal proofs are outside this four-proof audit. This is the reason for `PASS_WITH_NOTES` rather than a plain `PASS`.

## Noncritical findings

- **NC1 (exposition/scope, WHT08):** Kinetic-coefficient perturbation is not checked. The model explicitly fixes the wave kinetic coefficient to one (`packet.md` line 11), so this is a scope limitation, not a mathematical error. If a perturbed kinetic coefficient were introduced, the identity `3A^2 ≤ b` and the constants `c/√3`, `c²/6` would change; this is not claimed.
- **NC2 (exposition):** The step “weak derivative zero ⇒ constant a.e.” in the Lemma is asserted via a compact sketch (“test against derivatives of compact smooth primitives of all zero-integral test functions,” lines 28–30) rather than citing a standard distribution/Sobolev result. The argument is correct: a distributional derivative zero forces local constancy; patching the locally absolutely continuous representatives is valid for d = 1.
- **NC3 (dependency):** The identification `R_sp = sup A_sp/b^{α/2}` over full H¹ (with α = 1) and the sentence “compact approximation equality is Proposition P:spatial-four-linear” (lines 102–104) are consumed from the upstream spatial-occupation module, not re-proved here.
- **NC4 (dependency):** PROOF212’s bounds depend on `Corollary C:intrinsic-spatial-bracket`, which in turn depends on `T:intrinsic-occupation-ceiling`, `T:intrinsic-second-moment`, `P:spatial-energy-map`, `E:spatial-static-energy-score`, and the variational score machinery. These are correctly cited but are upstream obligations.
- **NC5 (endpoints):** Only `0 < a < 1` is claimed. At `a ↑ 1` the upper/lower formulas degenerate (`K₀ → ∞`, `M_a → 0`); no endpoint continuity or interchange is asserted, and the manuscript explicitly disclaims temporal-limit interchange (lines 178–180).
- **NC6 (wording):** “only this ratio of bound formulas is symmetric” (lines 173–174) is accurate: `√(K₀M_a)` is symmetric under `a ↦ 1−a`, while `K₀`, `M_a`, `C₂`, and the time exponent individually are not. The sentence correctly scopes itself; no overclaim.

## Checked derivations

### WHT01 — full real H¹ CDF proof: PASS
- On a bounded interval `f' ∈ L¹` by Cauchy–Schwarz from `f' ∈ L²`.
- The Lebesgue primitive has weak derivative `f'` by Fubini; subtracting it from `f` gives zero weak derivative, hence local constancy; representatives patch into one continuous (locally AC) representative.
- `ρ = f² ≥ 0`, `∫ρ = 1`, `ρ' = 2ff' ∈ L¹(ℝ)` (Hölder), so `ρ` has finite limits at both ends; `L¹` integrability of `ρ ≥ 0` forces both limits to be 0.
- Boundedness of `ρ` gives `A = ∫f⁴ < ∞`. No positivity of `f` and no strict increase of the CDF is used (correct — `F' = ρ = f²` holds even with plateaus).

### WHT02 — CDF square identity: PASS
Expansion:
`∫[f' − zf(1−2F)]² = b − 2z∫f'f(1−2F) + z²∫f²(1−2F)²`.
- Cross term: `ff' = ρ'/2`, and `∫ρ'(1−2F) = [ρ(1−2F)]_{−∞}^{∞} + 2∫ρ² = 2A` (boundary terms vanish because `ρ→0`, while `1−2F → ∓1`). Hence `∫f'f(1−2F) = A`. Coefficient `−2z` is correct.
- Square term: with `y = F`, `∫f²(1−2F)² dx = ∫₀¹(1−2y)² dy`. `P(y) = y − 2y² + (4/3)y³` has `P' = (1−2y)²`; `P(1)−P(0) = 1/3`. The `1/3` is exact.
- No hidden smoothness beyond the H¹ AC representative is needed.

### WHT03 — `3A² ≤ b`, positivity, Dirac pairing: PASS
- At `z = 3A`: `b − 2(3A)A + (3A)²/3 = b − 3A² ≥ 0`, so `3A² ≤ b`. Matches `WhiteCDF.lean` `cdf_square_bound` exactly (premise: every real `z`; conclusion: `3A² ≤ b`).
- `A > 0` (`∫f⁴ = 0 ⇒ f = 0` a.e., contradicting unit mass) and `b > 0` (`f' = 0` makes the continuous representative constant in `L²(ℝ)`, hence zero) are justified.
- Physical pairing: `A_sp(f) = c∫f⁴ = cA` from `Γ = cδ₀`; no Fourier constant, no `|x|⁻¹` substitution is inserted.

### WHT04 — sech profile, ratio and energy attainment: PASS
- `f_ℓ = √(ℓ/2)sech(ℓx)`, `f_ℓ' = −ℓ tanh(ℓx)f_ℓ` is correct.
- With `t = tanh(ℓx)`, `dt = ℓsech²(ℓx)dx`:
  - `∫f_ℓ² = (1/2)∫_{−1}^{1}dt = 1`,
  - `∫f_ℓ⁴ = (ℓ/4)∫(1−t²)dt = ℓ/3`,
  - `∫(f_ℓ')² = (ℓ²/2)∫t²dt = ℓ²/3`.
- `A/√b = (ℓ/3)/(ℓ²/3)^{1/2} = 1/√3`, so `R_sp = c·(1/√3) = c/√3` is attained for every `ℓ > 0`.
- Energy: `cA − b/2 ≤ cA − (3/2)A² = c²/6 − (3/2)(A − c/3)² ≤ c²/6`. At `ℓ = c`, `A = c/3`, `b = c²/3`, giving `c²/6`.
- `c = 0`: ratio 0; `sup(−b/2) = 0` approached by `f_ℓ` as `ℓ↓0`; no zero-scale unit vector is used. Correct.

### WHT05 — definitions/bracket: PASS
- Kinetic penalty half (`−b/2`), kinetic coefficient one, covariance mass `c` (unit-noise coefficient `√c` not confused with `A_sp = cA`) all consistent.
- Time exponent `(3−a)/2 = (4−α−a)/(3−α)` at `α = 1`. Correct.

### WHT06 — moment bounds: PASS
- `q = 3`, `k = 2`, `m = 3/2` from `q = 4−α`, `k = 3−α`, `m = q/k`.
- `F₀(z) = 2[(2z)^{1/2}/(8·3^{3/2})]^{1/2}` (correct instantiation of `E:spatial-static-energy-score`).
- `√(2E_sp) = √(2·c²/6) = c/√3`, so
  `F₀(E_sp) = 2√(c/72) = √c/(3√2)`. Then `2^m F₀ = 2^{3/2}·√c/(3√2) = (2/3)√c`.
- Substitution into `C:intrinsic-spatial-bracket` with `k = 2` gives lower `(2/3)√(c/M_a)` and upper `(2/3)√(cK₀)`; `K₀ = 2^a/(1−a)`, `M_a` as stated, all Gamma arguments positive/finite for `0<a<1`.
- `c = 0`: both bounds vanish and `C₂ = 0` via `T:intrinsic-second-moment`; consistent.

### WHT07 — relative width: PASS
- Duplication: `Γ_E(1+a) = 2^a Γ_E((1+a)/2)Γ_E(1+a/2)/√π` (from `Γ_E(2x)` with `x = (1+a)/2`). Recurrence: `(1−a)Γ_E((1−a)/2) = 2Γ_E((3−a)/2)`. Both exact.
- Product:
  `K₀M_a = √π/[2Γ_E(1+a/2)Γ_E((3−a)/2)]`.
- With `x = 1+a/2`, `y = (3−a)/2`, `x+y = 5/2`; the `L²(0,∞)` functions `t^{(x−1)/2}e^{−t/2}`, `t^{(y−1)/2}e^{−t/2}` have squared norms `Γ_E(x),Γ_E(y)` and inner product `Γ_E(5/4)`. Cauchy–Schwarz gives the bound; equality at `a = 1/2` (`x = y = 5/4`).
- Symmetry `a ↦ 1−a` exchanges `x,y`, so only the bound ratio is symmetric; no claim that `C₂` or the exponent is symmetric. Correct.

### WHT08 — adversarial controls: PASS (with one scoped gap)
- `c = 0`: handled by limiting profiles.
- Sign-changing/zero-crossing `f`, CDF plateaus: handled (identity uses `F' = f² ≥ 0`, no positivity or strict monotonicity).
- Translation, sech scale `ℓ > 0`, `a` endpoints `0<a<1`: consistent.
- Kinetic coefficient perturbation: not treated (scope note NC1).

### WHT09 — Lean/analytic match: PASS
- `cdf_square_bound(A,b,h)` requires exactly the all-`z` inequality `0 ≤ b − 2zA + z²/3`, which the Lemma supplies. Substitution `z = 3A` is the actual use.
- `energy_upper(c,A,b,h3)` with `h3 : 3A² ≤ b` proves `cA − b/2 ≤ c²/6` for any real `c`; the analytic proof at lines 98–99 is the identical completion (`(c−3A)² ≥ 0`). Matches.
- All representative/IBP/CDF/attainment/Gamma analysis is outside the two finite conditional deductions and is audited above; no full formalization is claimed.

### WHT10 — ledger and obligations: PASS with named upstream
- PROOF210 (Lemma `L:white-cdf-square`): **PASS** — fully self-contained within the packet.
- PROOF211 (Proposition `P:white-spatial-energy`): **PASS** — self-contained except the borrowed `R_sp` definition/compact-approximation note from `P:spatial-four-linear`.
- PROOF212 (Theorem `T:white-moment-bounds`): **PASS** — conditional on `C:intrinsic-spatial-bracket` (itself conditional on the occupation ceiling/intrinsic-second-moment chain).
- PROOF213 (Corollary `C:white-relative-width`): **PASS** — conditional on `L:equilibrium-gamma-beta` (standard Gamma/Beta identities, correct here).

Unresolved upstream obligations (consumed, not re-proved in this audit):
1. `P:spatial-four-linear` (physical four-linear continuity, `R_sp = R₀`, `A_sp(f) > 0` for nonzero H¹, compact approximation equality).
2. `L:equilibrium-gamma-beta` and `L:temporal-equilibrium` (Gamma/Beta identities; potential and mass `M_a`).
3. `T:intrinsic-occupation-ceiling` and `C:intrinsic-spatial-bracket` (raw occupation energy, scarmap, ceiling, own-energy comparison).
4. `T:intrinsic-second-moment` (identification `C₂ = S₂^{pos} = 2^m S₁^{pos}`), `P:variational-positive-scores`, `P:variational-unmasked-rate`, `P:variational-remove-mask`, and the original point-limit existence/exponent.
5. The original point-limit identification itself — the manuscript correctly states this is an upstream theorem, not established by the substitution alone.

No full-main/image/cold acceptance, source-constant normalization correction, or Skorohod result is claimed; the final disclaimers (lines 178–187) are honest and consistent with the audit.

## Required fixes before production gate

None (mandatory). I found no actual mathematical errors and no false identities in PROOF210–213.

Optional (exposition only, not gate-blocking):
- Cite the standard one-dimensional “weak derivative zero ⇒ locally AC constant representative” fact instead of sketching it.
- Add an explicit one-line scope statement that the kinetic-coefficient-one specialization is fixed and kinetic perturbation is out of scope (WHT08).
- In the final ledger, keep the named upstream obligations attached to PROOF212/PROOF213, since their constants inherit from the occupation/temporal/variational chain.

## One-line summary

PROOF210–213 are internally correct: the CDF square identity `b − 2zA + z²/3 ≥ 0`, the bound `3A² ≤ b`, `R_sp = c/√3`, `E_sp = c²/6`, the moment bounds `(2/3)√(c/M_a) ≤ C₂ ≤ (2/3)√(cK₀)` with exponent `(3−a)/2`, and the width bound `√(K₀M_a) ≤ [√π/(2Γ_E(5/4)²)]^{1/2}` all close with exact constants, correct signs and boundary terms, and the two Lean deductions match their analytic premises — conditional only on the explicitly named upstream occupation/temporal/variational modules.