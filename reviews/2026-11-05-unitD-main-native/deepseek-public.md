# CURRENT UNIT D reconstruction (OWN 094–111 + S064 + both joined implications)

Scientific source `af97ae4db921a660b0a4ed1ffbe9b6f53a487e2b`. I report the literal current deductions from the current modules
`notes/integrated_source_convergence.tex` (094–100),
`notes/integrated_masked_moments.tex` (101–103),
`notes/integrated_constant_phase_young.tex` (104–111),
and `notes/notes_stratonovich_ham_second_moment.tex` (S064).
**No tools or execution were used.** All conclusions below are *conditional reconstructions*: they verify the D-level mathematics at the level of the stated proofs, while naming the C-level and external clauses still required.

## 0. Standing model (S064 as formal/logical given)

- `d ∈ {1,2,3}`, `0 < a = α0 < 1`, `α0+α < 2`, with `0<α<d` or `α=d=1` (white noise).
- `Γ` nonnegative, even, positive-definite, homogeneous tempered Radon measure; `Γ(cA)=c^{d-α}Γ(A)`; spectral convention `Γ=∫e^{iξ·x}μ(dξ)`, unitary spatial Fourier transform `f^(ξ)=c_d∫e^{-iξ·x}f(x)dx`, `c_d=(2π)^{-d/2}`.
- Data `(1,0)`, massless wave speed 1, `G_t` mass `t` (sphere measure in `d=3`).
- `S064` is **formal context / logical given**, not a theorem with a proof body. It is invoked only where actually used; zero covariance handled directly.

This model class is **not** assumed to have angular/spectral density, finite total spectral mass `μ(R^d)`, `H^3`, Hilbert-valued white vector, or a rough point trace.

---

## Part I. Source deductions 094–100

### [D-094] finite correlated Gaussian convex comparison
**Result.** For `v_1,…,v_N` in a real Banach space, `ξ` centered Gaussian with `Cov ξ ≤ C I`, and independent standard real `g_j`,

\[
\Big(\mathbb E\Big\|\sum_j \xi_j v_j\Big\|^p\Big)^{1/p}
\le \sqrt C \Big(\mathbb E\Big\|\sum_j g_j v_j\Big\|^p\Big)^{1/p},\qquad p\ge 1.
\]

**Reasoning.** `x↦‖Σx_jv_j‖^p` is convex (seminorm power). Add an independent Gaussian `Z` with covariance `C I−Cov ξ`; conditional Jensen gives `E φ(ξ) ≤ E φ(ξ+Z)`, and `ξ+Z` has the law of `√C g`. The auxiliary comparison does not resample the actual coefficient family. `C=0` direct.

**Unresolved clause.** None model-specific; this is a pure finite Gaussian-norm inequality.

---

### [D-095] actual Gaussian transfer/stability
**Result.** For a centered Gaussian linear noise `Y` with `Var Y(F) ≤ C‖F‖_{H_W}^2`, the finite paths `M_{Y,N}=Σ_{j≤N}Y(f_j)A_j` converge in every `L^p(B_θ)`, `B_θ=C^θ([0,T];B(E))`, to an actual Gaussian path `M_Y` with compact values at all times on one path event, and

\[
\|M_Y-M_{Y,N}\|_{L^pB_θ} \le \sqrt C\|M_R-M_N\|_{L^pB_θ},\quad
\|M_Y\|_{L^pB_θ} \le \sqrt C\|M_R\|_{L^pB_θ}.
\]

For fixed Schwartz `z,w`, `⟨M_Y(t)z,w⟩=Y(h_{R,t;z,w})` in `L^2`, with the literal raw test class. Stability: if `(W,Y_n)` jointly Gaussian, `D_n=W−Y_n`, `Var D_n(F)→0` on every smooth compact test, then `M_{Y_n}→M_R` in every finite `L^p(B_θ)`.

**Limit order.** The uniform tail is removed first (`N` large, using `√C‖M_R−M_N‖`), then the fixed head. Restated: choose `N` to control the transfer tail; then let the residual parameter `n→∞` in the fixed head via `s_N(n)=Σ_{j≤N}Var D_n(f_j)→0`. This is **not** a uniform Cauchy from a moment bound; it uses the actual residual covariance contraction.

**Unresolved clauses.** Requires the actual coefficient paths `A_j` and raw path convergence `M_N→M_R` from `[D/C-093]`; the no-commutation of filter through mask/wave group is a genuine fixed clause.

---

### [D-096] spatial heat contraction on the physical space
**Result.** `H_Γ` is the separable real completion of Schwartz tests under

\[
B_Γ(f,g)=\int Γ(dy)\int f(x)g(x-y)dx
=(2π)^d\int \hat f(ξ)\overline{\hat g(ξ)}\,μ(dξ).
\]

`C_ε f=p_ε*f` is a positive self-adjoint contraction on `H_Γ`, `I−C_ε` is a contraction, and `C_ε→I` strongly.

**Reasoning.** Spectral multiplier `m_ε(ξ)=e^{-ε|ξ|²/2}`; on dense Schwartz tests positivity/contractivity are direct; dominated convergence gives strong convergence.

**No density of `μ`, no finite `μ(R^d)` used.**

---

### [D-097] retaining isometry keeps the given `W`
**Result.** `G=L²((0,∞)_λ×R_r, λ^{a-1}dλ/Γ_E(a)⊗dr; H_Γ)`; feature map

\[
ΦF(λ,r)=\sqrt{2λ}\int_{t>0,\,t≥r} e^{-λ(t-r)}F(t,\cdot)\,dt
\]

is an isometry `H_W→G` with closed range (uses

\[
\int_{-∞}^{\min(t,u)}2λ\,e^{-λ(t+u-2r)}dr=e^{-λ|t-u|}
\]

and the Laplace representation of `|t-u|^{-a}`). On a product extension retaining `W`,

\[
\mathcal I(g)=W(Φ^{-1}Pg)+J((I-P)g)
\]

is isonormal on `G` with `\mathcal I(Φh)=W(h)` **in `L²` literally** for every `h∈H_W`; here `P` projects onto `ΦH_W` and `J` is one independent isonormal on the complement.

**Control.** The `r` coordinate is auxiliary and ranges over all of `R`; no value of raw negative-time noise is assigned. One fixed retaining coupling serves all source widths and all local/global factors.

---

### [D-098] canonical sources and residual on the retaining space
**Result.** With `Q_ρ=C_εP_η` (`P_η=1_{λ≤η^{-1}}`), both source and residual obey

\[
\operatorname{Var}Y_ρ(F),\ \operatorname{Var}D_ρ(F) ≤ \|F\|_{H_W}^2,
\]

and `Var D_ρ(F)→0` at arbitrary relative widths. The pointfield realizations satisfy the exact joint source law

\[
\operatorname{Cov}(Y_{ε,η}(t,x),Y_{ε',η'}(s,y))
=K_{\max(η,η')}(t-s)\,Γ_{ε+ε'}(x-y),
\]

with `K_η(v)=Γ_E(a)^{-1}\int_0^{η^{-1}}e^{-λ|v|}λ^{a-1}dλ`, spatial width `ε+ε'` obtained from the two heat factors. The residual decomposition

\[
\|(I-Q_ρ)g\|^2=\|(I-P_η)g\|^2+\|P_η(I-C_ε)g\|^2≤\|g\|^2
\]

follows from orthogonal `λ`-ranges. This proves `M_R^ρ→M_R` in every `L^p(B_θ)`, with uniform Gaussian driver `√p` and square-exponential norms.

**Correction retained.** Source and residual are **correlated**, not independent: only the `λ`-disjoint part factorizes; the full heat residual generally does not.

---

### [D-099] pointfield regularity at fixed `ρ`
**Result.** For each fixed `ρ>0`, `Y_ρ(t,x)=\mathcal I(v_{ρ;t,x})` has a version continuous in time and smooth in space, with every spatial derivative jointly continuous on compact rectangles. The increment estimate is

\[
\mathbb E|∂_x^b Y_ρ(t,x)-∂_x^bY_ρ(s,y)|^2
≤ C_{ρ,b}(|t-s|+|x-y|²).
\]

**Scope.** Continuous-time smooth-space versions only for **each fixed positive width**; no common event over uncountably many widths, no uniform `ρ` bounds.

---

### [D-100] ordinary source response
**Result.** For fixed `ρ`, `b_ρ(t,x)=ζ_R(x)Y_ρ(t,x)`, the statewise integral

\[
L_ρ(t)z=\int_0^t S(-u)B(b_ρ(u))S(u)z\,du
\]

is an operator-norm Lipschitz path, and `L_ρ=M_R^ρ` for all `t∈[0,T]` on one probability-one set.

**Reasoning.** At each fixed `u`, the Sobolev adjoint row identity reduces the integrand to the raw wave test `h_{R,t;z,w}`; the point-feature integral equals `Y_ρ(F)` for smooth tests; indicator approximation in the raw completion and test-side `L²` convergence give the equality on the same coupled space, not only in law.

---

## Part II. Masked chain and transfer deductions 101–103

### [D-101] finite chains, Green-first and masked comparison
**Result.** Ordered chain measure `ν_n^{t,x}` has mass `t^{2n}/(2n)!`; finite ordered integrals are Bochner `L²` integrals; Green smoothing is removed **first** using square **and** cross `L²` moment convergence, not a sample bound on heat tails. For all `n,k`,

\[
0≤\mathbb E[X_{ρ,n}^m(t,x)X_{ρ,k}^m(t,y)]
≤\mathbb E[X_{ρ,n}(t,x)X_{ρ,k}(t,y)],
\qquad
\|X_{ρ,n}^m\|_2≤q_n(t),
\]

with `q_n` from `L:vertex-crude`.

**Reasoning.** Nonnegative `C_ρ=K_ηΓ_{2ε}≥0`; each Wick diagram has exactly one factor per vertex; the mask product `∏m(z_i)∈[0,1]` multiplies every diagram identically. This is an expected-displacement-diagram comparison, **not** samplewise solution order or Gaussian PSD order. The determinant `−1` mask countercontrol is a finite-scope warning against `C−DCD≥0`, not a model counterexample.

---

### [D-102] ordinary solutions and tested Bochner average
**Result.** `u_ρ^m=ΣX_{ρ,n}^m`, `u_ρ=ΣX_{ρ,n}` converge absolutely in `L²` and have locally continuous versions that are the unique locally continuous ordinary mild solutions with data `(1,0)`. For `φ≥0` compact smooth,

\[
0≤\mathbb E[u_ρ^m(t,x)u_ρ^m(t,y)]≤\mathbb E[u_ρ(t,x)u_ρ(t,y)],
\]

and

\[
\mathbb E\Big|\int φ(x)u_ρ^m(t,x)dx\Big|^2
≤\|φ\|_1^2\,\mathbb E|u_ρ(t,0)|^2.
\]

**Reasoning.** Picard terms bounded by `M^n t^{2n}/(2n)!`; uniqueness by iterating the homogeneous Volterra equation. Spatial `L²`-continuity plus `Q_t=Σ_nq_n(t)<∞` gives the Bochner average; ordinary Fubini and the sign test identify it with the pathwise average. **Only unmasked stationarity is used**, never masked stationarity.

**Boundary.** Uniform source-width `q_n` comes from the independent `L:vertex-crude` (008); no later `finalC2/B050` premise funds it.

---

### [D-103] canonical point-moment limit and conditional transfer
**Result.** At every fixed `t`, at arbitrary relative widths,

\[
\lim_{ε,η\downarrow0}\mathbb E|u_ρ(t,0)|²=\mathbb E|u(t,0)|².
\]

If the masked averages converge in `L²` to `Z_m(t,φ)`, then

\[
\mathbb E|Z_m(t,φ)|²≤\|φ\|_1²\,\mathbb E|u(t,0)|².
\]

**Reasoning / limit order.** Reversal `s'_j=t−s_{n+1−j}`, `z'_j=−z_{n+1−j}` relabels pairings; fixed-order joint limits from `L:joint-fixed-order`; the outer double tail `Q²−Q_N²=(Q−Q_N)(Q+Q_N)≤2Q(Q−Q_N)` bounds all higher orders. Order: fixed-order limits first, then `N→∞`. **The masked `L²` convergence is an explicit premise here until [D-110] supplies it.** The point-moment limit is a canonical law/series statement, not an alternate pathwise rough solution.

---

## Part III. Constant-phase and Young deductions 104–111

### [D-104] complete/separable `F`, proper closed `iE`, total finite propagation
**Result.** `F=E⊕R²` is complete and separable and injects continuously into total distributions `(e_1+c_1,e_2+c_2)`; `iE` is closed **proper**, not dense (a nonzero constant is a nonzero multiple of `δ_0`, which is not locally `L²` in Fourier). The cutoff

\[
L_ψ(e,c_1,c_2)=ψe+(c_1ψ,c_2ψ)
\]

is bounded `F→E` via Peetre multipliers on `H^{±1/2}`. The actual free group is

\[
S_F(t)(e,c_1,c_2)=(S(t)e,\ c_1+t c_2,\ c_2)
\]

with strong state continuity and finite propagation for the **total** data, including cancellation between the Sobolev and constant parts. Scalar displacement or separate summands are insufficient.

---

### [D-105] actual extended driver with both constant columns
**Result.** `DχM_E=M_E=M_ED_χ` pathwise; `A_E=M_EL_ψ`, `A=iA_E`, `A^ρ=iM_E^ρL_ψ` are independent of `ψ`, have compact values, satisfy `Ai=iM_E`, `π_CA=0`. Both constant columns `iM_E(ψ,0)` and `iM_E(0,ψ)` are retained. `A^ρ→A` in every `L^pC^θ`; uniform `√p` and square-exponential driver bounds; `A` is `W`-measurable.

**Control.** `Dχ` is **not** assumed self-adjoint or a projection; the range in `iE`/`π_CA=0` does **not** annihilate the constant inputs.

---

### [D-106] ordinary response on all of `F`
**Result.** For fixed `ρ`, `B_F(b)(e,c_1,c_2)=(0,b(e_1+c_1))∈E` with

\[
\|B_F(b)\|_{B(F,E)}≤\|b\|_∞+\|b\|_2,
\]

and

\[
A_E^ρ(t)z=\int_0^t S(-r)B_F(b(r))S_F(r)z\,dr
\]

as a statewise strong integral, Lipschitz as an operator primitive. The proof uses total finite propagation to compare the `F` state with a localized `E` state and kills the difference by multiplication with `b`.

**Control.** No density of `E` in `F` is used. Fixed-width identities hold on one event for that width.

---

### [D-107] left-order linear Young equation
**Result.** With `X=D`, `Y_V(r):M↦MV(r)` (norm-one bounded bilinear multiplication on `B(F)`) and `2θ>1`, the exact left Young integral order gives the local contraction and the full linear solution `U_D(t,s)=I+∫_s^t dD\,U_D`; composition, inverses, joint norm continuity, and growth

\[
\sup_{s≤t≤T}\|U_D(t,s)\|≤C_T\exp\big(C_T(1+\|D\|_{C^θ})^{1/θ}\big).
\]

**Reasoning.** `N_ℓ(V)=sup‖V‖+ℓ^θ[V]_θ` gives `N_ℓ(∫dD V)≤c_θ[D]_θℓ^θN_ℓ(V)`; on `c_θKℓ^θ≤1/4` the map is a contraction. The zero-based difference recurrence coefficients are `4a_K,16a_K,48a_K`, verifying the indices. This is **not** an imported nonlinear bounded-vector-field theorem. Noncommutation is addressed: `D(v_j,u)V(u)` is not `V(u)D(u,v)`; the left order is fixed.

---

### [D-108] Gaussian flow and physical flow on the original measure
**Result.** `U_A,U_{A^ρ}` are strongly measurable in uniform triangle norm, have every finite moment, satisfy `U_{A^ρ}→U_A` in every `L^p`, `π_CU_A=π_C`, `(U_A−I)F⊂iE`. The physical flow

\[
P_A(t,s)=S_F(t)U_A(t,s)S_F(-s)
\]

has composition and strong state continuity, constant block `(c_1,c_2)↦(c_1+(t−s)c_2,c_2)`, and analogous `L^p` source convergence. Its difference from the free flow has range in `iE`.

**Working.** Local driver-ball convergence gives probability convergence; the driver **square-exponential** bound plus `ν=1/θ<2` and the crude bound `rC(1+x)^ν≤c x²+C_{r,c}` give every finite flow moment and uniform integrability. **No square-exponential flow moment or tilted-source UI is assumed.** Interaction `U` is norm-continuous; free/physical `P` is strongly continuous on states only, and lives in the bounded-family topology.

---

### [D-109] ordinary source solution identification
**Result.** For fixed `ρ`, the displacement distribution of `P_{A^ρ}(t,0)e_0` is the locally continuous ordinary source solution `u_ρ^m(t,\cdot)`.

**Reasoning.** Young Riemann sums converge to the strong state integral (bounded `C(r)`, uniform modulus of `U`); the `F` Picard series matches every chronological scalar Green term by compact-test absolute Fubini, including the `d3` sphere measure and the constant coordinate. `B_T=sup‖B_F(b)‖`; order-`n` phase bound `C_T^{n+1}B_T^nT^n/n!`. This identifies the actual source displacement distribution and ordinary solution, **not** rough PDE uniqueness.

---

### [D-110] bounded tested observable and log-moment transfer
**Result.** For `φ≥0`, `∫φ=1`,

\[
O_φ(e,c_1,c_2)=⟨e_1,φ⟩+c_1,\quad
Z_m(t,φ)=O_φP_A(t,0)e_0,
\]

and `Z_m` is `W`-measurable. At arbitrary relative source widths, for every finite `p`,

\[
\int φ(x)u_ρ^m(t,x)\,dx\longrightarrow Z_m(t,φ)\quad\text{in }L^p,
\]

hence

\[
\mathbb E|Z_m(t,φ)|²≤\mathbb E|u(t,0)|².
\]

**Reasoning.** At fixed `ρ` the pathwise average equals the Bochner `L²` average by the sign test; `‖O_φ‖≤(‖φ‖_{H^{-1/2}}²+1)^{1/2}`; [108] gives `L^p` flow convergence. This is a bounded total displacement, **not** an `H^{1/2}` point trace. Only now is [103] discharged and the original canonical point moment transferred. Same mask/horizon/model/observable throughout.

---

### [D-111] deterministic compact base
**Result.** For real `h∈C([0,T];C_c^∞(K))` with one fixed compact `K` and continuous derivatives,

\[
A_h(t)=\int_0^t iS(-r)B_F(h(r))S_F(r)\,dr
\]

is Lipschitz in `B(F)`, has range in `iE`, and obeys the displayed budget

\[
\|A_h\|_{C^θ}≤C_{\text{free},T}\sup_r(\|h(r)\|_∞+\|h(r)\|_2).
\]

The flow and moment conclusions of [108] extend to `A_h+gA` and `A_h+gA^ρ`, uniformly on bounded `H/G` budgets.

**Corrections retained.** `h` may have spatial support outside the stochastic mask but **not** vary with source width unless separately handled; `h` is fixed before asymptotics. No Cameron-shift identity or signed moment comparison is asserted. `g=0,h=0` branch: free `U=I,P=S_F`, tested displacement 1; `h≠0` at `g=0` still yields a deterministic `h`-flow, not the original free comparison.

---

## Part IV. The two joined implications

### JOIN-DRIVER-SOURCE
**Actual chain.** `raw/aux admission + normalized Fourier covariance` → `both variance directions/weighted cutoff envelopes` → `real compact coefficients + strong gain/localization` → `localized compact envelopes + vanishing trace tails` → `fixed-even-q interval limits` → `dyadic grid/mesh/Hölder order` → `full-norm all-p C^θ Gaussian output` → `correlated retaining source transfer + ordinary response`.

The needed **CURRENT OWN** clauses and their roles:

| Clause | Role in join |
|---|---|
| `C064` (`P:masked-noise-completion`, Fourier factor `(2π)^d`, actual `W`) | original noise completion and normalized spatial covariance |
| `C085` (`L:driver-noise-basis`) | real smooth compact ONB `f_j`, independent `g_j=W(f_j)` on given `W` |
| `C071/C073` (`P:actual-wave-form`, `P:wave-two-variances`) | actual Sobolev adjoint, both variance directions, `b_I=C_T h^{2-a}B_α(h)` |
| `C087` (`L:driver-gain-localization`) | gain `E_r→E_{r+1}`, dual gain, two-sided localization, no free-group norm derivative |
| `C091` (`L:driver-interval-limit`) | actual trace-tail Cauchy at fixed admissible even `q`, compact limit on original space |
| `C092` (`L:driver-holder-limit`) | uniform moment indices, dyadic sum, finite-grid → mesh → lower-Hölder order |
| `C093` (`P:actual-operator-driver`) | assembled given-`W` compact-valued `C^θ` Gaussian path |
| `C080/C082/C083` (via `C093`) | balanced nonselfadjoint cutoff envelopes, localized finite variance, finite Gaussian operator bound |

**Verification at the D level.** [D-094]/[D-095] consume `C093`’s coefficients/raw path and the finite convex comparison; [D-096]/[D-097]/[D-098]/[D-100] construct the retaining source and ordinary response. I find the stated limit order (finite head after uniform tail, no metric commuting, no independence of source/residual) mathematically consistent.

**Attached unresolved condition.** The join is **conditional on the full proofs of the listed C clauses** (particularly the Fourier/Bessel positive-definite steps, heat contraction on Radon `Γ`, and the compact tail argument). A checked narrow clause may support its application without full-parent clearance, but any genuinely needed unresolved C clause cannot be externalized.

---

### JOIN-F-YOUNG-OBSERVABLE
**Actual chain.** `104–107` construct `F`,`A_E`,`A`, and linear Young flow; additional matched clauses `108–110+103` bind this to consumers.

Complete coupling requirements:

1. **Same retaining source for every E124–126 ordered block factor.** Fix `δ,N`; use one global raw `W` and one retaining source pulled back by `T_{δ,0}`, `T_{δ,m}`; verify pullback source/residual domination and ordinary restart. [D-108] supplies driver/UI transfer; [D-109] supplies ordinary identification.

2. **Both `F` columns.** `A` has `iM_E(ψ,0)` and `iM_E(0,ψ)`, and `π_CA=0` never makes `Range A` an annihilation of constant inputs. Verified in [D-105]/[D-106].

3. **Original-measure Hölder product before Gaussian law/tilt.** For `n=N+1`, ordered factors `F_{m,ρ},F_m`: let `C_ρ` be max norms, `e_ρ` max difference. Then

\[
\|\prod F_{m,ρ}-\prod F_m\| ≤ n\,C_ρ^n e_ρ,
\qquad
\|\prod F_{m,ρ}-\prod F_m\|_{L²}≤n\|C_ρ\|_{L^{4n}}^n\|e_ρ\|_{L⁴},
\]

with all moments on the **original** measure. No growing-`N` uniformity or tilted-source convergence is used. This is the correct `4n/4` Hölder pairing (`1/2=n/(4n)+1/4`).

4. **Terminal remainder `τ=δ^{-1}-NB∈[0,B)`.** Composition retains the final factor at `τ`, including `τ=0`; the last local primitive is stopped, not assumed full-length.

5. **F166/167.** Their deterministic mean/source/ordinary matching is the **additional matched clause**. If the deterministic `h` varies with source width, its primitive convergence and bounded `H/G` budgets are a separate clause, not implied by fixed-`h` [D-111].

6. **G174.** Actual physical same-source restart: the cocycle

\[
S_F(mB)[A_{\text{glob}}(mB+u)-A_{\text{glob}}(mB)]S_F(-mB)=X_m(u)
\]

is obtained by bounded conjugation and path convergence; Young uniqueness gives restart. This is verified as a plausible consequence of `104–109`, conditional on `108`’s joint convergence.

7. **G189.** Requires **two separate fixed-`δ` moment limits before canonical law/scaling**: (i) the physical tested displacement average converges in `L²` using `P_E^ρ→P_E`; (ii) the unmasked canonical point moment `E|u_{Γ_δ,ρ}(L,0)|²→E|u_{Γ_δ}(L,0)|²` at `(ε,τ/δ)→0`. Only then apply the law scaling `E|u_Γ(T_δ,0)|²=E|u_{Γ_δ}(L,0)|²`. The source limit is **not** exchanged with `δ↓0` or a growing cone.

**External imports used inside the D Young section.**
- Friz–Hairer *second edition*, Sections 1.4–1.5 and 4.1, (4.3), printed pp. 13, 61–62: the bounded-bilinear left Young remainder estimate. It is imported, not re-proved.
- Chen author-version Theorem 3.1, (3.6), pp. 14–15: used in the fixed-order/C clauses (upstream), with exact finite spectral/temporal hypotheses and the Case-2 origin qualification.

**No admissible D premise uses:** source Theorem 4.1/Lemma 4.4 as a construction; Section 5(ii) source identification; `H^3`; a rough point trace; `actualC2` rate to fund `A008`; or a native vote/status.

---

## Part V. Constants, corrections and controls retained

- `b_I=C_T h^{2-a}B_α(h)` with `C_T=4A_TK(α,a,γ)C_ν`.
- `B_α(h)=1`, `1+log(1/h)`, `h^{1-α}` for `α<1, =1, >1`.
- Time-exponent window
  `1/2<β<min(1−a/2,(3−a−α)/2)`; Schatten cutoff `qγ>d`.
- Green masses `n=0,1,2,3`: `1, t²/2, t⁴/24, t⁶/720`.
- White order-four/e-four scale: `E X_1²=c_0t^{3−a}`, `E X_2=c_0t^{3−a}/2`; coefficient-one Wick: `E g⁴=3`, empty+2 `=1`, `1+3=3`, odd `3` zero.
- Young recurrence coefficients `4,16,48`; growth exponent `1/θ<2`; `r(1+x)^ν` submajorized.
- Mask PSD control `C−MCM` has determinant `−1`, finite scope only.
- Left-order noncommutation: `Y_V(r)=MV(r)`, sums `D(u,v)V(u)`, norm-one multiplication.
- Cross source covariance `K_max(η,η')(t−s)Γ_{(ε+ε')}(x−y)`.

## Part VI. Verdict and confidence

**Verdict (unforced, scoped).** At the literal level of the current D modules, the 18 deductions `094–111` are mathematically consistent under the named C-level prerequisites; I did not find a concrete D-level contradiction in the displayed derivations. The joined implications **close conditionally**: `JOIN-DRIVER-SOURCE` closes on the full proofs of `064/071/085/087/091/092/093` (together with the finite-Gaussian/cutoff clauses those consume); `JOIN-F-YOUNG-OBSERVABLE` closes on full `104–111+103` plus the explicit matched clauses for `E/F/G` consumers, the original-measure `4n/4` ordered-product limit, and the two fixed-`δ` moments in `G189`. I do **not** claim full unconditional closure, because those C antecedents and the Friz–Hairer/Chen Theorem 3.1 imports are named imports, not re-derived end-to-end here.

**Genuine unfinished/unread work.** I cannot re-verify, within this scoped response, the full internal proofs of the C Fourier/Bessel positivity steps, the compact-trace-tail argument, or the external Theorem 3.1 induction/Friz–Hairer book proof; those remain named clauses. If any of those fails at its exact hypotheses, the corresponding joined conclusion is affected, and that failure would be a genuine consumed-clause gap, not something cured by source presence.

**Categorical confidence: medium**, scoped to “the current D18 are conditionally reconstructed and no D-level contradiction was located,” not high (because upstream C clauses and external imports remain un-re-derived and no tool execution was performed for confirmatory symbolic checks).