# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I re-derived every constant, exponent, limit, and boundary convention in PROOF046 (L:inventory-product), PROOF047 (L:fixed-split), and PROOF048 (P:interval-coefficients) by hand, including small-k and two-colour controls, and found no false identity, sign error, missing factorial/multinomial factor, wrong coefficient, or invalid limiting exchange.

## Noncritical findings

1. **Notation (expository only).** Line 517–520 sets `Q_{r,q} = ⟨U_r v,U_q v⟩_{H_{1/T}}`, and line 525–527 uses it in `[s^{2k}]E‖U(T;s)v‖² = Σ Q_{r,q}`. The expectation is present because `H_{1/T}=L²(Ω;X_{1/T})` (line 195), so the inner product already averages over the Gaussian fields. This is correct, but a reader not tracking line 195 could momentarily misread it. Suggest writing `Q_{r,q} = E⟨U_rv,U_qv⟩_{X_{1/T}}` once.

2. **Implicit elementary factorial step.** PROOF046 line 62 closes via `k^{-νk} ≤ (k!)^{-ν}`. This uses the trivial `k! ≤ k^k` (hence `k^{νk} ≥ (k!)^ν`), not Stirling. Correct, but unstated; one clause would help.

3. **Conservative partition count.** Line 185 writes `M ≤ 3k+1`; the sharper `2k+1` suffices (since `|A| ≤ Σ_{i∈B}k_i`, `m=Σ_{i∈C}k_i`). Harmless, absorbed into `C_split^k`, but conservative.

4. **Zero-order constant sharpness.** Line 626 gives zero-order energy `≤ e‖v‖²`; the actual bound is `e^{1}‖v‖² = e‖v‖²` from `‖Z_0(T)‖_{1/T} ≤ e^{T/(2T)} = e^{1/2}`. Correct and used consistently in `e+Y−1 ≤ eY`.

None of these affect any constant, exponent, or conclusion. There are no required repairs before the production gate.

## Checked derivations

### PROOF046 — inventory product

- Parameters: `ν=3−α>1` (α<2), `β=4−α−α₀>2` (α+α₀<2), `p=2−α₀>1` (α₀<1), `β−ν=1−α₀>0` → `β/ν>1`. ✓
- At `z=θ k^ν`, `θ=1/4`: singleton `v_i z = θ k^ν i^{−β} + θ k^{ν−1}i^{−(β−1)} + θ k^{ν+α−2}i^{−p}`; since `ν+α−2=1`, third term = `θ k i^{−p}=Q_i`. ✓
- Separation `1+A+B ≤ (1+A)(1+B)` pulls out `1+Q_i`; `Σ_i log(1+θk i^{−p}) ≤ ∫₀^∞log(1+A x^{−p})dx = A^{1/p}∫₀^∞log(1+x^{−p})dx` (finite, p>1), giving `≤ C k^{1/p} ≤ Ck`. ✓
- Coarse `i≤k`: middle term `θ k^{ν−1}i^{−(β−1)} ≤ θ k^ν i^{−β}=P_i` iff `i≤k`; singleton `≤2P_i≤4P_i`; higher `P_i^l(1+li/k)²/(l!)^ν ≤ (4P_i)^l/(l!)^ν` using `(1+l)² ≤ 4^l`. So remaining factor `≤ S_ν(4P_i)`. `S_ν(x) ≤ e^{ν x^{1/ν}}` (ℓ^ν≤ℓ¹ argument, ν≥1). `Σ_{i≤k}ν(4θ)^{1/ν} k i^{−β/ν} ≤ Ck` since `β/ν>1`. ✓
- Fine `i>k`: `P_i ≤ θ k^{ν−β} ≤ 1/4`. Singleton tail = `θ k^ν Σ i^{−β} + θ k^{ν−1}Σ i^{−(β−1)} ≤ θ(1/(β−1)+1/(β−2))k^{ν+1−β} = Ck^{α₀}` because `ν+1−β=α₀`. Higher tail `Σ_{l≥2}P^l(1+ly)²/(l!)^ν ≤ CP²(1+y²)`; summing over `i>k` with `y=i/k` gives exactly `Ck^{2ν}(k^{1−2β}/(2β−1)+k^{−2}k^{3−2β}/(2β−3)) = Ck^{2α₀−1} ≤ Ck` (both terms have exponent `2ν+1−2β=2α₀−1≤1`; denominators `2β−1,2β−3>0` since β>2). ✓
- Total `log ∏ ≤ Ck` (independent of M, all sums extended to ∞). `[z^k] ≤ e^{Ck}(θk^ν)^{−k} = 4^k e^{Ck}k^{−νk} ≤ 4^k e^{Ck}/(k!)^ν`. ✓

### PROOF047 — fixed split

- Radii: `a=α/2`, `ω_i=k_i/h_i`, `d_i=2√(2k_i+1)√R_α` (from `2√(N+1)√R_α`, N=2k_i), `ϱ_i=δ_a ω_i^{2−a}/(σ_i d_i)` so `|z_i|σ_i d_i = δ_a ω_i^{2−a}`; hence `D(t)=δ_a Σ ω_i^{2−a}1_{I_i^T} ≤ δ_a Λ^{2−a}` by `Σ x_i^{2−a}≤(Σx_i)^{2−a}` (2−a>1) and `λ≥0`. ✓
- Partition from both background endpoints and cross times: `M ≤ 2|A|+m+1 ≤ 3k+1`. Segment product `∏‖P_j‖_{H_{Λ_j}→H_{Λ_j}} ≤ 100^M exp(2ΣΛ_jΔt_j) ≤ 100^{3k+1}e^{4k}`; `ΣΛΔt = λT+Σω_i|I_i^T| ≤ k+k = 2k` (single integral, refinement adds no charge). ✓
- Phase-metric identities: `q_j = max{1,Λ_j/Λ_{j+1}}`; at a cut `Λ_j/Λ_{j+1} ≤ 1+Σ_{E_j}ω_i/λ ≤ ∏_{E_j}(1+ω_i/λ)`; insertion-only cuts give `q_j=1`; initial increase `q_0=1`; final return charged at T. Each connected clipped interval ends exactly once ⇒ `∏q_j ≤ D_A = ∏_{i∈A}(1+k_i/(λh_i))`, with no duplicate copy at overlaps/starts/insertions. ✓
- Cross subspaces `𝒵_S` (background ≤ N_i, inserted cross degree 1, uninserted vacua); each `P_j`,`𝒥_j` preserves them. Fresh insertion `J_i(u,w)=(0,σ_iB_i u)` on a vacuum color gives, by Gaussian orthogonality `E[g_{ij}g_{il}]=δ_{jl}` and the column bound `Σ_m‖A_ρ^{−1/2}M_{e_m}f‖² ≤ R_αρ^{α−2}‖f‖²` (tensored over `ℛ_i`):
  `‖J_i‖ ≤ σ_i√R_α Λ(t_i)^{(α−2)/2} ≤ c_i := σ_i√R_α λ^{(α−2)/2}` (using α−2<0, Λ≥λ). No occupied-colour annihilation treated as vacuum. ✓
- Chronological word `𝒲_A = 𝒥_M P_M B^{cut}_{M−1}𝒥_{M−1}P_{M−1}⋯B^{cut}_1𝒥_1P_1𝒥_0` (rightmost first; no commuting of spatial operators). Norm bound `≤ (∏‖P_j‖)(∏q_j)(∏_{i∈C}c_i) ≤ M_k D_A ∏c_i`. ✓
- Dyson cube: `Φ_A(z)=[∏_{i∈C}y_i]M^cut_{(z,y,0)}v = Σ_π∫_{D_π}𝒲_A(z,t)v dt`, each ordered simplex coefficient 1; `Σ_π|D_π|=∏|I_i^T|≤∏h_i` — no `m!` or `1/m!`. Minkowski gives `‖Φ_A‖_λ ≤ M_k D_A ∏_{i∈C}c_i h_i ‖v‖_λ`. `m=0` handled (unit cube). ✓
- Normalized polytorus Cauchy (mass 1): `U_r v = (∏ϱ_i^{−r_i})∫ e^{−ir·θ}Φ_{A_r}(ϱe^{iθ})dθ/2π`; cross exponents already extracted as degree one, omitted amplitudes zero. Bounds each copy with `∏ϱ_i^{−r_i}` (resp. `−q_i`); no holomorphic norm squared. ✓
- Two-copy product via Cauchy–Schwarz in `L²(Ω)`: `‖w‖_{1/T} ≤ k‖w‖_λ` (since `max_ξ (T^{−2}+|ξ|²)/(k²T^{−2}+|ξ|²) = k²`), `‖v‖_λ ≤ ‖v‖_{1/T}`. Gives (E:split-before-absorption) with `k²M_k² D_{A_r}D_{A_q}∏_{i∈B}ϱ_i^{−2k_i}∏_{i∈C}(R_ασ_i²h_i²λ^{α−2})‖v‖²`, `r_i+q_i=2k_i`, and `D_{A_r}D_{A_q}=∏_{i∈B}(1+k_i/(λh_i))^{ℓ_i}`. ✓
- Radius reduction: `ϱ_i^{−2k_i}=(σ_i²d_i²/δ_a²)^{k_i}(h_i/k_i)^{(4−α)k_i}`; `d_i²≤12k_iR_α`; `k_i^{−(3−α)k_i}≤(k_i!)^{−(3−α)}`. Final constants: `M_k²=100^{6k+2}e^{8k} ≤ (100⁸e⁸)^k`; `|C|+Σ_{i∈B}k_i=k` gives `R_α^k`. `C_split = 100⁸e⁸ max{1,12δ_{α/2}^{−2}}`, only α. ✓

### PROOF048 — interval coefficients, existence, substitution, summation

- Reductions: omit zero σ; `L→max{1,L}`; `σ_i→|σ_i|`, `W_i→sgn(σ_i)W_i` preserves law and potential ⇒ `σ_i>0`. ✓
- Existence/local convergence: `v_max=sup_t Σσ_i²1_{I_i}Γ_ε(0)`; order-n phase ≤ `e^{λT/2}(2z_*√(n+1)√v_max T/λ)^n/n! ‖v‖_λ` (insertion cost = unweighted mult norm/λ; free phase ≤ `e^{λh/2}` per segment). Locally uniform ⇒ entire in z. Coefficientwise absolute convergence on the `2z_*`-polydisc: `Σ_r z_*^{|r|}‖U_r‖ ≤ 2^{|F|}K_{2z_*}`; Cauchy–Schwarz bounds the energy double series by `4^{|F|}K²` (identity only — does not enter the uniform bound). ✓
- Exact energy identity for real `s`: `[s^{2k}]E‖U(T;s)v‖² = Σ_{|r|+|q|=2k}Q_{r,q}`; reflection `W_i→−W_i` (measure-preserving) forces `r_i+q_i=2k_i`, `Σk_i=k`; `k_i=0` removes the field; active colours ≤ k; `∏(2k_i+1)≤3^k`. Truncation `N_i=2k_i` is exact per coefficient by L:finite-word-cutoff (includes creation→annihilation self-contractions); no Hermite-degree limit. ✓
- Local weight table (after `σ_i²≤ch_i^{−α₀}`, absorbing `c^k`, with `C_split^k3^kk²` into `C^k`): `(2,0)/(0,2): R_αh^β(1+1/(λh))`; `(1,1): R_αλ^{α−2}h^{2−α₀}`; `k_i=l≥2: R_α^lh^{βl}(1+l/(λh))²/(l!)^ν`. All whole weights monotone increasing in h because every expanded power is positive (`β>2,l≥2 ⇒ βl−2>0`; singleton powers β,β−1; cross power p>0); the inverse-length factor is never bounded separately. At `h=LT/i`, `1+l/(λh)=1+li/(kL) ≤ 1+li/k` (L≥1). Extracts exactly `C^kR_α^kT^{βk}` and leaves the inventory `v_i` (k_i=1) and `b_{i,l}` (k_i=l≥2). ✓
- No extra multinomial: `Σ_{Σk_i=k}∏w_{i,k_i}=[z^k]∏_i(Σ_{l≥0}w_{i,l}z^l)` (w_{i,0}=1). L:inventory-product ⇒ `C^k/(k!)^ν`. ✓
- Identification/cutoff removal at fixed ε, finite family, fixed coefficient: creation tail →0 by dominated convergence (bounded by `v_ε`); annihilation tail zero on finite-coordinate vectors; density + closedness; band projections commute with free evolution; strong convergence of each Duhamel word; entire majorant rebuilds the full series (uniform on compact amplitude sets). `v_max` used only for identification, absent from the uniform bound (constants from `δ_{α/2}`, phase bound, inventory, `L,c`; covariance only via `R_α^k`). ✓
- Phase bound: zero order `≤e‖v‖²`; `Σ_{k≥0}x^k/(k!)^ν ≤ e^{ν x^{1/ν}}` (ν>1); summing absolute coefficient bounds gives `≤(e+Y−1)‖v‖² ≤ eY‖v‖²`; absorb `νC^{1/ν}` ⇒ (E:interval-phase-bound). Exponent `β/ν=κ=(4−α−α₀)/(3−α)`. ✓

### Hand computations (controls, not proofs)

- **k=1, λ=1/T.** Cross (1,1): `R_αλ^{α−2}h^{2−α₀} → R_αT^{β}L^{2−α₀}i^{−p}` (inventory third term at k=1). Mean (2,0): `R_αh^β(1+1/(λh)) → R_αT^β(L^β i^{−β}+L^{β−1}k^{−1}i^{−(β−1)})` (first two `v_i` terms). Both match inventory exactly up to L-powers. ✓
- **Two fresh colours (two Dyson orders).** m=2: two simplices `{t_1<t_2}`,`{t_2<t_1}`, each measure `h_1h_2/2`; total `h_1h_2`; coefficient 1 per order; Minkowski yields product `h_1h_2` — no `2!`. ✓
- **Nested/overlapping intervals, metric endings.** Nested `I_1⊃I_2`: starts uncharged, `I_2` charged once at `b_2`, `I_1` at `b_1`, final return uncharged ⇒ `D_A=(1+ω_1/λ)(1+ω_2/λ)`. Shared endpoint `b_1=a_2`: only the ending colour charged `≤1+ω_1/λ`. No double charge. ✓

### Imported-input check

Crouzeix–Palencia `‖F(T)‖ ≤ (1+√2)sup_{W(T)}|F|` is confirmed textually in the embedded `crouzeix-v1.txt` (eq. (3), p.1, lines 2148–2150; Theorem 6, pp.5–6, line 2366). Application is to bounded operators on the band (A₀=−Δ on S_b bounded); numerical-range parabola and root comparisons in L:complex-phase/L:interval-complex verified (`‖Q−I‖≤1/6 ⇒ ‖Q‖,‖Q^{−1}‖≤2`; block sum `(39+12λh)e^{λh} ≤ 100e^{2λh}`). Original raster/page-image verification remains unperformed (text carrier only), recorded as a custody limitation, not a defect.

## Scope checks (C01–C10)

- **C01: CHECKED** — all admissible α,α₀ give ν>1, β>2, p>1, β>ν; θk^ν evaluation; Q_i=θki^{−p}; log-integral finite; k^{1/p}≤k; S_ν used with β/ν>1; 2α₀−1 exponent; finite denominators; constants independent of M,k; correct factorial direction.
- **C02: CHECKED** — r_i+q_i=2k_i, k=Σk_i, λ=k/T, N_i=2k_i; Gaussian vacuum; Hermite finite-word identification incl. self-contractions; whole evolution entire; unused amplitudes zero; fixed-degree propagator not identified with untruncated evolution (explicit at lines 301, 617).
- **C03: CHECKED** — ω_i,d_i,ϱ_i,a=α/2 exact; D(t)≤δ_aΛ^{2−a}; non-selfadjoint V and adjoint/root guards present; common partition across both endpoints and cross insertions; M≤3k+1; `ΣΛΔt` is a single integral ≤2k with no repeated exponential charge; deterministic joint-space norm, no conditioning.
- **C04: CHECKED** — initial/final X_λ and all phase components; q_j formula; simultaneous end/start/remain; insertion-only q=1; initial increase/final return; each clipped interval ends once per active copy; D_A exact; noncommuting maps stay ordered.
- **C05: CHECKED** — fresh cross-colour insertion on actual tensor subspaces; exact column identity tensored with arbitrary Hilbert factor; Λ^{(α−2)/2} ≤ λ^{(α−2)/2}; no occupied colour estimated as vacuum; no independence asserted between the two energy copies; no random-operator-norm claim.
- **C06: CHECKED** — each cross colour once; coefficient 1 per ordered simplex; permutation domains partition the cube mod null ties; product h_i with no m!/1/m!; m₀ unit cube; Bochner integrability from finite-cutoff boundedness.
- **C07: CHECKED** — normalized polytorus mass 1; exact r/q powers; omitted amplitudes zero; no squared-norm holomorphy; cross first degree extracted first; k² phase conversion; radius exponent 2k_i; exact ℓ_i; d_i²≤12k_iR_α; factorial inequality; M_k²≤(100⁸e⁸)^k; C_split only α; singleton mean one charge; cross singleton special factor; higher ≤ two charges.
- **C08: CHECKED** — v_max majorant uniform mode/band (not smoothing/family); locally uniform entire series; coefficientwise absolute convergence via larger polydisc with finite 2^{|F|} only for identity; even-parity selection; same fields on both copies; inactive removal; ∏(2k_i+1)≤3^k counted once; exact per-coefficient N_i; no Hermite limit.
- **C09: CHECKED** — sorted labels retained; signed-σ reduction; clipped interval ≤h_i; L≥1; three weights exact; monotonicity from positive expanded powers; inverse length not separately bounded; exact v_i/b_{i,l} recovery and R^kT^{βk}; all L/c/k²/3^k absorbed without extra multinomial; no reindexing/duplicate-count defect.
- **C10: CHECKED** — mode/band removal at fixed width/family/order; creation-tail dominated convergence; density/closedness; sufficient Hermite cutoff per order + separate entire reconstruction; uniform coefficient excludes v_max, depends only on α,α₀,L,c and R^k; zero energy ≤e; e+Y−1≤eY; hand controls (above) all match; no random-operator-norm assertion in the phase bound.

## Proof ledger

| ID | Determination | Checked steps / limits | Constant uniformity | Residual gaps |
|---|---|---|---|---|
| PROOF046 | FULLY_CHECKED | θ=1/4; ν=3−α; β=4−α−α₀; p=2−α₀; Q_i and P_i exact; S_ν bound `e^{νx^{1/ν}}`; fine/coarse split at i=k; exponents α₀ and 2α₀−1; final `4^k e^{Ck}/(k!)^ν` | C=C(α,α₀), independent of M,k | none |
| PROOF047 | FULLY_CHECKED | radii/d_i/ϱ_i; D(t)≤δ_aΛ^{2−a}; Λ-integral ≤2k; M≤3k+1; q_j and D_A; fresh cross insertion c_i; cube Σ_π|D_π|=∏h_i (no m!); Cauchy over torus; k² conversion; ϱ_i^{−2k_i}≤(12δ⁻²)^{k_i}R_α^{k_i}σ^{2k_i}h^{(4−α)k_i}/(k_i!)^ν; C_split=100⁸e⁸max{1,12δ_{α/2}^{−2}} | C_split=C_split(α); uniform in inventory, m_i, S_b, N_i | none |
| PROOF048 | FULLY_CHECKED | entire-majorant and coefficientwise absolute convergence (2^{|F|} identity-only); parity r_i+q_i=2k_i; N_i=2k_i exact; three weight table with β,p,ν; h-monotonicity; h≤LT/i substitution to v_i/b_{i,l}; no-multinomial identity; identification and cutoff removal; Σ_k x^k/(k!)^ν ≤ e^{νx^{1/ν}}; e+Y−1≤eY | C=C(α,α₀,L,c); uniform in ε and family | none |

## Required fixes before production gate

None. The three proofs are complete and correct at the stated depth. The four noncritical items are optional exposition improvements (clarify the L²(Ω) expectation in `Q_{r,q}`; state `k! ≤ k^k`; optionally tighten `M≤2k+1`). No constant, exponent, sign, boundary term, factorial, or limiting exchange needs repair.

## One-line summary

PROOF046–048 are hand-verified correct — every constant (`θ=1/4`, `δ_{α/2}`, `C_split=100⁸e⁸max{1,12δ_{α/2}^{−2}}`), exponent (`2α₀−1`, `α₀`, `(4−α)k`, `(α−2)/2`, `ν=3−α`, `β/ν=κ`), limit, Dyson/multinomial accounting (no `m!`, no repeated metric charge), and fact-proof-adjoint root sign checks out — with only minor notational/exposition notes; no defects found; downstream terminal/source/upper-assembly and full-goal gates remain separate as scoped.