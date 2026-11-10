# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None blocking for the four targeted proofs.

The four proofs (PROOF190–193) are internally coherent, and the recomputed constants, signs, boundary terms, cutoff guards, and two-limit order all match the supplied bodies. No false identity (wave norm vs. potential/coefficient norm), no hidden block-independence, no diagonal `B,δ` limit, and no illegal `∞−∞` was found in these four deductions.

## Noncritical findings

1. **Pending upstream production wording (uniform_products ~438–449).** The frozen sentence “Its norm bound is at most `K/B <= K`” is ambiguous in isolation, but in its actual surroundings “Its” refers to the averaged operator coefficient `barM_m`, where the bound `a_m/B ≤ K/B ≤ K` is correct. The distinct typed objects are all present and used correctly in the target proofs:
   - operator/coefficient norm: `||barM_m|| ≤ a_m/B ≤ K/B`;
   - mean-norm (primitive) budget: `||barH_m||_θ ≤ a_m ≤ K` on good blocks;
   - physical static wave norm: `8(1+K)^2(1+B) e^{B λ(barM_m)}`.
   The WAVE norm is NOT `K/B`. PROOF190–193 do not use a false wave bound. This wording clarification remains **PENDING** and is not adopted here as a replacement/clearance.

2. Imported deep-source statements (Borell 11.6 in friz–hairer, Teschl form/spectral theorems, Friz–Hairer Young estimates, Crouzeix–Palencia) are available only as held text carriers and are **not certified** in this run. PROOF190–193 reference downstream propositions (uniform-rate-averaging, tube-coarse-envelope, tube-rayleigh-tail, uniform-arbitrary-residual, point-transfer, raw-block-original-lower) whose own proofs are present in the packet but whose external prerequisites stay at source-depth limitation.

3. The `a↓0` exponent `(4−α)/(3−α)` in PROOF193’s zero/boundary closing is flagged as a **formal** exponent only, with no endpoint-in-`a` theorem; this is an honest scoping statement and is not an overclaim.

## Checked derivations

**PROOF190 (L:signed-score-envelope).**
- `Rate_R(0)=0` via `𝒯_R0=0` and free spectral bottom zero; `Rate_R(Φ)≤1+C_mean||Φ||` from `P:uniform-rate-averaging`.
- Completion square is exact: `2+2C_mean q−q²/2 = 2+2C_mean²−(q−2C_mean)²/2`, giving ceiling `2+2C_mean²` and lower bound `0` (zero control).
- Envelope: from the growth bound `log||S_E(ℓ_m)U_D(ℓ_m,0)|| ≤ C_gr B(1+||D||_θ^ν)` and submultiplicativity of the block product,
  `F_{δ,B}(a+M_{δ,B,R}Φ) ≤ 2C_grBδn + 2^ν C_grBδ Σ_m(v_m^ν+h_m^ν)`,
  using `(v+h)^ν ≤ 2^{ν−1}(v^ν+h^ν)` (ν>1). The bound is nonnegative, so it controls the `max(1,·)`.
- Weighted power means:
  `δΣv_m^ν ≤ (δn)^{1−ν/p}b_{δ,B}^ν ≤ (2/B)^{1−ν/p}b_{δ,B}^ν` (exponent `p/ν≥1`, `p=ν` legal),
  `δΣh_m^ν ≤ (δn)^{1−ν/r}(32B^{3−1/r}C_mean ρ)^ν ≤ (2/B)^{1−ν/r}(32B^{3−1/r}C_meanρ)^ν` (exponent `r/ν>1`).
- Constants check out: `A0=4C_gr`; for `A1` the `B`-powers cancel `B^{ν/r}·B^{−ν/r}` leaving `B^{3ν}`; `η_B=2^{ν+1−ν/p}C_grB^{ν/p}`.
- `n=N+1≥2`, `δn≤2/B`, zero/empty-cell cases legal.

**PROOF191 (P:signed-moment-bulk-tail).**
- `E_{δ,B,M}` finite via the polynomial envelope plus `Rate≥0`; ordinary deterministic real supremum; zero path/control give nonnegativity (so truncation by `max(0,·)` consistent).
- `e_B→0`: `P:uniform-arbitrary-residual` applied with the actual anchor `b_{δ,B}→0` at fixed `B`, uniform in `R≥1` and control ball, `δ` first, then `B`. Since `e_B≥0`, `limsup_B e_B≤0` forces `e_B→0`. No uniform `δ/B` rate and no diagonal `B_δ` is inferred.
- Bulk: for `ρ≤M`, `E`-definition gives `F−ρ²/2 ≤ 2Rate(Φ)−||Φ||²/2+E ≤ S_{R_δ}+E`; hence `G_{δ,B}(ρ)≤S+E+ρ²/2`, and `∫_0^M ρ/δ e^{(S+E)/δ}dρ = M²/(2δ)e^{(S+E)/δ}` with the prefactor retained even when `M²/(2δ)<1`. Uses only `ρ²≥||Φ||²`, no equality/optimizer.
- Tail: `L:tube-rayleigh-tail` with `C=A1B^{3ν}`, intercept `A0+η_Bb_{δ,B}^ν`; guards `M>0`, `ρ≥M`, `C≥0`, `1<ν<2`, `4C≤M^{2−ν}` ≡ `4A1B^{3ν}≤M^{2−ν}`; front factor `4`, exponent `−M²/4`.

**PROOF192 (P:signed-operator-upper).**
- Cutoff guard via side ratio `M_B^{2−ν}/(4A1B^{3ν})=(c_ball^{2−ν}/(4A1))B^{κ_ball(2−ν)−3ν}→∞` (`κ_ball(2−ν)−3ν>0`); `A1=0` treated separately.
- `δlog` of the two-term positive sum: `δlogM_δ ≤ δlog2 + max{ S_{R_δ}+E_{δ,B,M_B}+δlog(M_B²/(2δ)), A0+η_Bb^ν−M_B²/4+δlog4 }`.
- Normalizers vanish: `δlog(M_B²/(2δ)) = δlog(M_B²/2)−δlogδ→0` via `te^{−t}≤2/t` with `t=−logδ`; `δlog2, δlog4→0`.
- Limsup subadditivity (valid with finite `S,E`) gives `limsup_δ δlogM_δ ≤ max{V_up+e_B, A0−M_B²/4}`; then `B→∞`, `e_B→0`, `M_B→∞` yield `≤V_up`. The left side is `B`-independent because `P_δ` is the same actual global endpoint for every `B` (`L:tube-actual-endpoint`).
- Lower bound `liminf δlogM_δ≥0` from `M_δ≥1` (`P:symplectic-raw`); order is `δ` first at fixed `B`, then `B`.

**PROOF193 (P:original-signed-point-upper).**
- `P:original-point-transfer` gives `E|u_Γ(T_δ,x)|² ≤ DataPref_δ · M_δ` with `δlogDataPref_δ→0`.
- `T_δ=δ^{−1/κ}` is a decreasing bijection with inverse `δ=T^{−κ}`; normalized limsup gives
  `limsup_T T^{−κ}logE|u_Γ(T,x)|² ≤ 0 + limsup_δ δlogM_δ ≤ V_up ≤ 2+2C_mean²`.
- Spatial stationarity transfers to every fixed `x` (`P:raw-block-original-lower`); moments `≥1` and finite make logs legal.
- Zero branch: `C_mean=0`, `H_I={0}`, `Rate_R=S_R=V_up=0`, `u=1`, `P_δ=S_E(δ^{−1})`, `0≤δlogM_δ≤2δlog[C(1+δ^{−1})]→0`; free `F_δ(0)` may be positive; no nonzero-Gaussian/Cameron import.

## Required fixes before production gate

- No mathematical fixes are required for PROOF190–193 as written against the supplied statements.
- Keep the uniform_products ~438–449 **wording clarification PENDING**; the external paragraph proposal is not adopted. Do not clear the upstream production paragraph or the whole paper solely on the strength of this four-proof audit.
- Do not clear: full 213-proof/44-section coverage, global/source-image/cold/strict-blind novelty, Skorohod, companion, release, or the original full goal. Imported Borell/Teschl/Friz/Crouzeix deep proofs remain at source-depth limitation.

## Four-proof status ledger

| PROOFID | Label | Status | Hypotheses | Conclusion / Use | Limitations |
|---|---|---|---|---|---|
| PROOF190 | L:signed-score-envelope | CHECKED | Fixed aux `α/4<s<1/2`, `θ,ν,r,p`, `C_mean`, `Rate_R≤1+C_mean||Φ||`, `P:uniform-rate-averaging`, product-growth + true primitive + power means, `n≥2`, `δn≤2/B` | `0≤S_R,V_up≤2+2C_mean²`; polynomial envelope `A0,A1,η_B` with `A1B^{3ν}ρ^ν` | Envelope is sufficient/non-sharp; ceiling auxiliary-dependent; no author-constant identification |
| PROOF191 | P:signed-moment-bulk-tail | CHECKED | Polynomial envelope, `b_{δ,B}→0` fixed `B`, `P:uniform-arbitrary-residual`, `L:tube-rayleigh-tail`, actual-law tube Rayleigh `M_δ≤∫ρ/δ e^{(G−ρ²/2)/δ}` | `E_{δ,B,M}` finite; `e_B→0`; finite-`δ` bulk+tail bound | Guard `4A1B^{3ν}≤M^{2−ν}` is a hypothesis inside the proposition; no diagonal controls |
| PROOF193 | P:original-signed-point-upper | CHECKED | `P:original-point-transfer` (`DataPref_δ M_δ`, `δlog→0`), `P:raw-block-original-lower` stationarity, bijection `T_δ=δ^{−1/κ}`, moment `≥1` and finite | `limsup_T T^{−κ}logE|u_Γ(T,x)|² ≤ limsup_δ S_{δ^{−1}+2} ≤ 2+2C_mean²`; zero branch rate 0 | Signed-score UPPER only; positive-score equality/final `C2` not identified here |
| PROOF192 | P:signed-operator-upper | CHECKED | `M_B=c_ballB^{κ_ball}`, `κ_ball>3ν/(2−ν)`, two-limit cutoff, `e_B→0`, `V_up` finite, `M_δ≥1`, `B`-independent same `P_δ` | `0≤liminf δlogM_δ≤limsup δlogM_δ≤V_up≤2+2C_mean²` | Order `δ` first then `B`; no `S_R` limit assumed |

All four statuses are **CHECKED** by direct recomputation from the embedded text; none is FAIL or NOT_FULLY_CHECKED at the stated target depth.

## SUP01–SUP12 checks

- SUP01 **PASS** — `S_R`, `V_up` finiteness/ceiling `2+2C_mean²`, zero-control lower bound, no optimizer/positivity/finite-rank/convergence assumptions; original `H_I` norm/amplitude preserved.
- SUP02 **PASS** — envelope constants reconstituted exactly (`A0=4C_gr`, `A1=2^{ν+1−ν/r}C_gr32^νC_mean^ν`, `η_B=2^{ν+1−ν/p}C_grB^{ν/p}`, `B^{3ν}ρ^ν`); every power-mean exponent sign verified; `B`-power cancellation correct; no unspecified `c_Y(B)` or `F`-norm rate used.
- SUP03 **PASS** — `E_{δ,B,M}` finite and deterministic; no measurable maximizing selector; polynomial-radius `P:uniform-arbitrary-residual` applied `δ`-first, fixed `B`, uniform `R`/control class; `e_B→0`.
- SUP04 **PASS** — exact bulk with retained prefactor `M²/(2δ)`, `ρ²≥||Φ||²`, no cost replacement/optimizer/Gaussian-Hilbert-norm assumption.
- SUP05 **PASS** — tail with `C=A1B^{3ν}`, intercept `A0+η_Bb^ν`, front `4`, exponent `−M²/4`, guard `1<ν<2` and `4A1B^{3ν}≤M^{2−ν}`; no infinite-dimensional density/head conditioning/Laplace principle.
- SUP06 **PASS** — cutoff ball polynomial inside the error theorem; side ratio and `A1=0` branch correct; `B` fixed before `δ` limsup; same `P_δ` independent of `B` (actual restart), not a `B`-dependent surrogate or assumed joint family.
- SUP07 **PASS** — `δlog(2·max)` inequality, vanishing normalizers via `−δlogδ→0`, limsup subadditivity, then `B→∞`, lower bound via `M_δ≥1`; no diagonal, no `∞−∞`.
- SUP08 **PASS** — original-point transfer, bijection, stationarity, point moment `≥1`, original `Γ`/dims/amplitudes and one global raw half-action preserved; signed-score UPPER only, not positive-score equality/`C2`.
- SUP09 **PASS** — zero/boundary branch correct; no nonzero-Gaussian/Cameron assumption; formal `a↓0` exponent only; no Jensen/lower silently forced to Chen constants.
- SUP10 **PASS (with PENDING wording)** — actual typed coefficient/primitive/wave statements are distinct and used correctly; no false `wave≤K/B`; upstream wording clarification retained **PENDING**, external proposal not adopted, source production not declared closed.
- SUP11 **PASS** — `ρ0`/control `0`, `p=ν`, empty last cell, `A1=0`, small bulk prefactor, growing `R_δ`, signed rough controls, nonmeasurable selector unnecessary, potential/primitive/wave type distinctness, fixed-`B` `cY` vs quantitative `C_gr`, `C=√δM` and `1/2`-action, `B`-independent endpoint all verified at stated depth; Borell/deep-source limitations explicit.
- SUP12 **PASS** — explicit four-proof ledger returned; own calculations completed; all 28 references not certified; pending upstream wording open; no full 213-proof/global/source-image/cold/strict-blind/novelty/Skorohod/companion/release/goal clearance; no forced HIGH or reliance on prior verdict rows.

## One-line summary

The four signed-score/operator/original-point upper proofs (PROOF190–193) check out internally — constants, boundary terms, cutoff guards, and the `δ`-first-then-`B` two-limit order all reconcile — with only the upstream uniform-products wording clarification retained as PENDING and the imported deep-source proofs left at source-depth limitation.

Completion statement: This run performed a direct, by-hand, read-only audit of exactly PROOF190–193 using only the embedded tracked context; no tools, delegation, builds, network, prior reports, or write access were used. Pending upstream wording status: **PENDING** (uniform_products ~438–449); no production closure is declared.