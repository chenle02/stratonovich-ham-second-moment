# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

No blocking proof gaps found within the audited scope (PROOF185–189). The transfer chain closes: fixed-parameter finiteness → retaining fast-source convergence and source-law identity → compact-data ordinary/Ek identification → total-free-cone average-of-squares → source-first law/time scaling → polynomial data/log control → zero-covariance case.

One dependency is worth recording as an explicit "not re-derived here" rather than a defect: PROOF185's finiteness input delegates to `P:tube-actual-law`, `P:tube-coarse-envelope`, `L:tube-rayleigh-tail`, and the identification of the tube endpoint with this exact `P_δ` is made via literal row identities + rational times + Young uniqueness with a common admissible exponent. That identification is asserted rather than expanded line-by-line in the proof, but the surrounding sections (`actual-operator-driver`, `constant-phase-young`) supply the stated intertwinings and are consistent with the claim.

## Noncritical findings

1. **Terminology "Bessel-unitary"** (PROOF187, line 157): the displayed free matrix is bounded and strongly continuous on `E_k = H^k×H^{k-1}`, but it is not unitary on `L²(ℝᵈ;ℂ²)` in the standard basis; the named "Bessel" weighting is doing the work. The proof only needs boundedness and strong continuity, so this is nomenclature only.

2. **`P:masked-canonical-transfer` applied at covariance `Γ_δ`** (PROOF186, line 137–140): the sentence "applies to this single-source law … no newly reconstructed auxiliary family for `Γ_δ` is required" is correct because `Γ_δ = g²Γ` is again in Hypothesis `H:homog`, but the reader should note the covariance reparameterization `Γ → Γ_δ`, `(ε,τ) → (ε,τ/δ)` is what makes the point limit a `Γ_δ` law statement.

3. **Cross-δ pathwise identity is not claimed** (PROOF189, line 327): the manuscript correctly separates law/moment identity from pathwise same-noise coupling; no correction needed, but this distinction must not be flattened in downstream compression.

4. **Source texts are OCR text layer only** (teschl/friz/crouzeix/chen carriers note "PDF extraction may garble mathematics; assigned PNGs remain required"). The pinpoints actually consumed by PROOF185–189 are algebraic/numeric ones already restated in the manuscript, so this did not affect the five-proof check; images were not available to me.

## Checked derivations

**Setup constants**
- `κ=(4−α−a)/(3−α)>1` ⇔ `1−a>0`, `a<1`; `3−α>0` since `α<3`.
- `L=δ⁻¹`, `R=L+2=δ⁻¹+2`, `T_δ=δ^{-1/κ}`, `g=δ^{(1−a)/2}`, `Γ_δ=g²Γ=δ^{1−a}Γ`.
- `δ↦T_δ=δ^{-1/κ}` is a decreasing bijection `(0,1)→(1,∞)` with inverse `δ=T^{-κ}`, so `(T→∞) ⇔ (δ↓0)`.
- No spatial Jacobian at `x=0`: `r_T·0=0`.

**PROOF185 — restriction and finiteness**
- From `A_F = g A_{F,R}(Wfast)` and `A_F i = i D_E`, `D_E=g M_R(Wfast)`; `S_F(t)i=i S_E(t)`.
- Applying the isometry `i` to the Young system for `U_F` and using uniqueness gives `U_F(t,s)i=iU_E(t,s)` and matching `P_F i=iP_E`; same for sources. `iE` closed/isometric; density of `E` in `F` is neither used nor true.
- Measurability: the continuous Young map on the separable closed path span, then bounded conjugation `P(t,s)=S_E(t)U(t,s)S_E(−s)` and restriction to `E`, gives measurable endpoint norms and uniform time-triangle difference norms; no free-group operator-norm continuity assumed.
- Finiteness: with `B=1` the clock condition is `0<δ<min(1,1/B)=1`, valid for all `δ∈(0,1)`; the tube envelope `G_δ(r)≤C_env(1+b_δ^ν+r^ν)` is independent of `R≥1`, and the Rayleigh-tail lemma makes finite `∫ r/δ e^{(G_δ(r)−r²/2)/δ}dr`; `P:tube-global-endpoint` identifies the tube product with the same actual `P_δ`.
- Lower bound `≥1` from `P:symplectic-raw` (conserved symplectic form ⇒ `‖P_δ‖≥1`), not from a fixed-mask rate.

**PROOF186 — fast sources and source law**
- `Yfast(t,x)=δ^{a/2}Y_{ε,τ}(δt,x)`; testwise `Yfast(f)=Y_{ε,τ}(T_{δ,0}f)`.
- Laplace-prefix kernel: with `K_τ(v)=Γ_E(a)⁻¹∫₀^{τ⁻¹}e^{−λ|v|}λ^{a−1}dλ`, the substitution `λ'=δλ` gives exactly
  `δ^a K_τ(δv) = K_{τ/δ}(v)`.
- Covariance of `gYfast`: `Cov(gYfast)=g²·Cov(Yfast)=δ^{1−a}·δ^a K_τ(δ(t−s))Γ_{2ε}(x−y)=K_{τ/δ}(t−s)·(p_{2ε}∗Γ_δ)(x−y)`. Spatial heat-sum width and temporal `max` conventions preserved.
- Driver convergence: source/residual domination `Var Y_ρ, Var D_ρ≤‖F‖_{H_fast}²`, `Var D_ρ→0` on compacts ⇒ Gaussian transfer gives `A^ρ→A` in every finite `L^pC^θ` retaining `Wfast`; Young local dependence plus `1/θ<2` tails ⇒ finite moments, uniform integrability, `L²` uniform triangle convergence; restriction to `E` gives `E sup ‖P_E^{ε,τ}(t,s)−P_E(t,s)‖²→0`.
- Ordinary/statewise identity: Schwartz rows `gYfast(h_R)`; Fubini via `E|ZY|≤‖Z‖₂‖Y‖₂`; dense states/rational times/continuity; `L:constant-source-solution` + `P:symplectic-source` identify Young and ordinary interaction on `E`.

**PROOF187 — compact-data Ek identification**
- `b=mgYfast` smooth in space, compactly supported in `B_{2R}`, continuous in time in every spatial derivative norm; `k>d/2+1`, `E_k=H^k×H^{k−1}`.
- The displayed free matrix is bounded: upper/right multiplier `⟨ξ⟩sin(t|ξ|)/|ξ|≤√2 max(1,t)`; lower/left `|ξ|sin/⟨ξ⟩≤1`; zero sine quotient is `t`; dominated Fourier convergence gives strong continuity.
- Leibniz + derivative-norm equivalence give `‖b(t)f‖_{H^{k−1}}≤C_k max_{|j|≤k−1}‖∂^jb‖_∞‖f‖_{H^{k−1}}`; `B(b(t))` is a norm-continuous bounded force with finite sample `B_L`.
- Picard bound `sup_{t≤L}‖Z_n‖≤C_L^{n+1}B_L^n L^n‖z‖/n!`; uniqueness via homogeneous Volterra differences; embedding into `E` + ordinary `E` uniqueness identify the sum with `P_E^{ε,τ}(t,0)z`.
- Fourier `L¹` embedding `‖f̂‖₁≤‖f‖_{H^k}(∫⟨ξ⟩^{−2k}dξ)^{1/2}<∞` for `k>d/2`; same for velocity with `k−1>d/2`.
- Scalar mild identity: `v(t)=cos(t√−Δ)ψ+∫₀^t G_d(t−r)∗[b(r)v(r)]dr`; `G_d(h)` positive Green measure, mass `h`, support in `B_h`, sphere measure in `d=3`; product `bv` continuous compactly supported; Fubini bound `∫₀^t‖φ‖_∞‖b(r)v(r)‖₁(t−r)dr<∞`; `G_d(h)=h×(unit-time dilation probability)` gives continuity; distributional equality equals the everywhere-continuous version. No `d=3` density, no Sobolev point trace.

**PROOF188 — cone identity and average of squares**
- Cone `C={(t,x):0≤t≤L,|x|≤1+L−t}` is causally closed and compact: a predecessor satisfies `|y|≤1+L−s`; spatial projection is inside the plateau `|x|≤R−1`.
- Initial difference `(ψ−1,0)=(ψ,0)+(−1,0)` in `F`-coordinates; total distributional data vanishes for `|x|<R`. On the cone `|x|+t≤R−1<R`, the translated free-phase kernel support lies in the vanishing region. Since the top-left free entry is `∂_t G_d(t)` with mass `1`, `L:constant-phase-free` gives `cos(t√−Δ)ψ(x)=1` there; testing `E` and constant summands separately would NOT give this total finite-propagation statement.
- The two mild equations share the coefficient `gYfast` on the cone (`m=ψ²=1`). The difference `w=v−u_full` has zero free term there and satisfies the homogeneous forcing integral; with finite sample constants `H=sup_C|w|`, `M=sup_C|gYfast|`, positive-Green iteration with mass recursion `f₀=1`, `f_{n+1}(t)=∫₀^t(t−r)f_n(r)dr=t^{2n+2}/(2n+2)!` gives `|w(t,x)|≤H M^n t^{2n}/(2n)!→0`. No sample positivity of the coefficient is used.
- At `t=L`, `D=B₁⊂C`; samplewise `v=u_full` on `D`, Tonelli + unmasked single-source spatial stationarity give
  `E‖pr₁P_E^{ε,τ}(L,0)z‖²_{L²(D)}=∫_D E|u_full(L,x)|²dx=v_d E|u_full(L,0)|²=finiteness`. This is an integral of squares, not a squared average.

**PROOF189 — source-first transfer, polynomial cost, zero case**
- `‖pr₁e‖_{L²(D)}≤‖e‖_E`; hence source-flow `L²` convergence in `L²(Ω;L²(D))`; Cauchy–Schwarz for square-norm differences:
  `|E|X|²−E|Y|²|≤‖X−Y‖₂‖X+Y‖₂`.
- Right side converges by `P:masked-canonical-transfer` at covariance `Γ_δ` and widths `(ε,τ/δ)`; fixed `δ` ⇒ both cutoffs tend to zero. The equal prelimit moments give
  `E|u_{Γ_δ}(L,0)|²=v_d^{-1}E‖pr₁P_δz‖²_{L²(D)}`.
- `P:raw-block-point-comparison` + `L:exact-canonical-scaling`: `V_δ` has law `u_Γ(Tt,r_Tx)` solving `δ²V_tt=ΔV+√δW V`; `U(t,x)=V_δ(δt,x)` has coefficient `√δ Y_{ε,τ}(δt,x)=gYfast(t,x)`, and `U(L,0)=V_δ(1,0)` gives the law/moment identity
  `E|u_Γ(T_δ,0)|²=E|u_{Γ_δ}(L,0)|²`, preserving all self/cross/unequal/empty chains and Green-before-noise `d=3`; `r_T` is not the mask radius `R`.
- Operator inequality: `E‖pr₁P_δz‖²_{L²(D)}≤‖ψ‖²_{H^{1/2}}E‖P_δ‖²`.
- Data polynomial: `‖ψ‖²_{H^{1/2}}≤‖ψ‖²_{H¹}=R^d‖η‖²+R^{d−2}‖∇η‖²≤C_ηR^d` (includes negative power `d=1`, `R^{d−2}≤R^d`); `δ log DataPref_δ=δ log(C_η/v_d)+dδ[log(1+2δ)−log δ]→0` via `te^{−t}→0`.
- Moment `≥1` from the unit empty pair; finiteness from the transfer and `E‖P_δ‖²<∞`; logs legal; taking `δ log` and `δ=T^{−κ}` gives the limsup reduction at `x=0`; canonical spatial stationarity extends to fixed `x`.
- Zero covariance: `u=1`, `P_δ=S_E(L)`; the same free cone argument gives the exact spatial-square identity on `B₁`; `1≤‖S_E(L)‖≤C(1+L)`, so `δ log‖S_E(δ⁻¹)‖²→0`.

## Required fixes before production gate

None blocking. Optional clarifying edits only:

1. (PROOF185) Expand the "smaller common admissible exponent" identification into the explicit uniqueness lemma it invokes, so the tube `P_δ` and the point-transfer `P_δ` are visibly the same object rather than argued in one sentence.
2. (PROOF186/189) Make the covariance reparameterization `Γ→Γ_δ` and width substitution `(ε,τ)→(ε,τ/δ)` explicit at the `P:masked-canonical-transfer` invocation.
3. (PROOF187) Replace "Bessel-unitary" with "Bessel-bounded/strongly continuous," or define the intended Bessel-weighted unitarity, to avoid a standard-basis false reading.

## PNT checks

- **PNT01 — PASS.** Intertwining `A_F i=iD_E`, `S_F i=iS_E`, closed isometric restriction, `E` not dense in `F`, measurability via separable path span, invertibility via Young Neumann pieces and free inverse; larger auxiliary cutoff ≠ datum `ψ`.
- **PNT02 — PASS (dependency noted).** `B=1` valid for all `0<δ<1`; literal endpoint identification with same `Wfast`, amplitude `g`, mask `η²`, horizon `δ⁻¹`; finiteness via tube/Rayleigh tail; norm ≥1 from symplectic raw; no fixed-mask rate or growing-`R` premise.
- **PNT03 — PASS.** `Yfast=δ^{a/2}Y(δt,·)`; testwise pullback; source/residual variance domination; Gaussian transfer retains `Wfast`; square-exponential path moments; Young convergence + `1/θ<2` ⇒ UI and `L²` uniform triangle; no δ-uniform assertion.
- **PNT04 — PASS.** Statewise integral `∫S_E(−r)B(mgYfast)S_E(r)dr`; Gaussian Fubini `E|ZY|≤‖Z‖₂‖Y‖₂`; `δ^aK_τ(δv)=K_{τ/δ}(v)`; covariance `K_{τ/δ}·(p_{2ε}∗Γ_δ)`; fixed-δ limits, no new raw family, no pathwise canonical identity.
- **PNT05 — PASS.** `E_k=H^k×H^{k−1}`, `k>d/2+1`; bounded zero-quotient free matrix; Leibniz bounded force; Picard factorial `C_L^{n+1}B_L^nL^n/n!`; Fourier `L¹` embedding for displacement and velocity; jointly measurable continuous version; no uniform source-width hypothesis, no raw `H^{1/2}` point trace.
- **PNT06 — PASS.** Distributional Duhamel with `cos(t|D|)ψ`; positive Green measure all `d`, including sphere `d=3`; `G_d(h)=h×unit dilation` continuity; absolute Fubini; distributional = everywhere-continuous version; no `d=3` density, no omitted initial velocity.
- **PNT07 — PASS.** Causally closed `C`; positive plateau margin `R−1` for both `ψ,m`; total `(ψ−1,0)` cancellation treated jointly; top-left `∂_tG_d(t)`; `cos(t|D|)ψ=1` on cone; no separate `E`/constant testing; data `(1,0)` not confused with the larger auxiliary cutoff.
- **PNT08 — PASS.** Same realized pullback field/common coefficient on the compact cone; locally continuous solutions give finite `H,M`; positive-kernel mass recursion `t^{2n}/(2n)!` drives `w→0`; Tonelli + unmasked source stationarity give exact `E∫_D|v|²=v_d E|u_full(L,0)|²`; average of squares, not squared average.
- **PNT09 — PASS.** Source displacement `L²(Ω;L²(D))` convergence; bounded `pr₁`; Cauchy–Schwarz for squared-norm expectations; canonical point-moment limit at `Γ_δ`; equal prelimit moments pass to the raw spatial-square identity; no δ-down interchange with width limits.
- **PNT10 — PASS.** `δ=T^{−κ}`, `r_T=Tδ`; `V_δ` law of `u_Γ(Tt,r_Tx)`; `U=V_δ(δt)` coefficient `√δY(δt)=gYfast`; covariance `Γ_δ=g²Γ`; `L=δ⁻¹`; fixed-order/series/d3 Green-first conventions retained; law/moment identity only.
- **PNT11 — PASS.** `‖ψ‖²_{H^{1/2}}≤R^d‖η‖²+R^{d−2}‖∇η‖²≤C_ηR^d`; `δ log DataPref_δ→0`; moment ≥1 and finite; `κ>1`, bijection covers the whole asymptote; free case `1≤‖S_E(L)‖≤C(1+L)` ⇒ `δ log‖S_E(δ⁻¹)‖²→0`.
- **PNT12 — PASS.** All five statuses above; both phase entries/free zero, d3 sphere/boundary margins, d1 white (d−2 negative power), distinct aux vs datum cutoffs, covariance shared-width max, fixed-δ vs growing-R, average-of-squares vs squared-average counterdistinction, no H1/Sobolev point embedding in d2/3, no nonlinear Gaussianity/positivity/sample-moment multiplication; no whole-28/213/global/cold/novelty/Skorohod/release certificate claimed.

## One-line summary

PROOF185–189 form a correct, internally consistent original-point/growing-cone transfer with verified constants (`κ`, `δ^aK_τ(δv)=K_{τ/δ}(v)`, Picard factorial, Green mass recursion, polynomial `R^d` data cost) and correct average-of-squares law/moment scaling; no blocking defect found, with only a documented dependency on the tube-finiteness identification in PROOF185.