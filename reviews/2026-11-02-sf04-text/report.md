# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

**1. Full SF04 clearance remains INCONCLUSIVE.**
This run is a bounded text/application audit only. No full SF04 completion certificate can or should be issued. Image obligations SF04-01, SF04-07, SF04-11 are missing by design (no assigned PNG is supplied or displayable in this text-only route), so edition/copyright/pagination/printed-offset verification is UNVERIFIED. Source hashes and metadata in `crosswalk.md`, `primary-scope.json`, `source-bindings.json` are custody/context only and were not treated as visual attestation.

**2. Several upstream proofs needed to close SF04-10 are not supplied.**
The direct Wiener/Borel/Cameron/zero-law steps in `integrated_gaussian_tubes.tex` are checkable and largely correct, but the *eligibility of the actual law* and the endpoint/raw-transfer chain cite results not present in this packet, e.g.:
- `P:radius-mean-anchor`, `P:uniform-actual-cameron`, `P:cameron-full-mean`, `P:uniform-mean-regulator`, `L:cameron-supported-tensor`, `L:cameron-actual-residual`, `L:radius-covariance-residuals`, `L:raw-block-restart`, `P:symplectic-raw`, `P:symplectic-block-mean`, `L:symplectic-free`, `P:masked-canonical-transfer`, `P:masked-source-moments`, `P:source-gaussian-transfer`, `P:source-ordinary-response`, `L:cutoff-factorization`, `L:driver-gain-localization`.
Without these, the end-to-end application cannot be certified from the supplied text alone. **SF04-10 is therefore INCONCLUSIVE**, even though the imported Theorem 11.6 application itself is faithful.

**3. The abstract-level claim of the white-energy constant and the variational identification is outside the supplied excerpt.**
`model-context.tex` claims the one-dimensional white energy is `c^2/6` and states an explicit variational identification, but `S:intrinsic-white-evaluation` and the finite Gram optimization are not supplied here. I record this as UNVERIFIED. It does not affect the source-application verdicts, but it is a boundary the manuscript and task scope must preserve.

**SF04 ID verdicts (exact 13):**

- **SF04-01 — INCONCLUSIVE/UNVERIFIED.** Teschl title/copyright/pagination images not supplied; metadata described but not certified.
- **SF04-02 — PASS.** Theorem 2.14/(2.63) applied only after the form is shown closed and semibounded (shift `c=2+K^2` in `P:signed-closed-form`, lines 666–671; `P:uniform-E-spectral`, lines 1007–1013); matches supplied p. 80–81.
- **SF04-03 — PASS.** Theorems 3.1–3.2, 3.6 used for bounded Borel calculus, strong continuity, form domains, and spectral bottom (`L:signed-spectral-wave` 779–781; `P:signed-physical-wave` 831–832; `P:uniform-E-spectral` 1088–1090); consistent with (3.18)–(3.21), (3.29)–(3.33), (3.51)–(3.53).
- **SF04-04 — PASS.** Max–min Theorem 4.12/(4.41) with the quadratic-form-domain allowance is used; common-trial lower inputs and essential-threshold fallback match the supplied theorem; no all-radius assertion is smuggled in (compact-ground family only).
- **SF04-05 — PASS.** Theorem 10.2 applied to `−V_σ` with real compact smooth `V_σ`, `d≤3`; self-adjoint `H²` operator, bounded below, `σ_ess=[0,∞)`, `C_c^∞` core (lines 64–66). No rough-potential substitution.
- **SF04-06 — PASS.** Ground eigenvalue is established below the essential threshold via the common negative trial *before* Theorem 10.13 is invoked (lines 82–87); simplicity/positivity is conditional and properly gated.
- **SF04-07 — INCONCLUSIVE/UNVERIFIED.** Friz–Hairer edition/physical-printed-offset image verification unavailable.
- **SF04-08 — PASS.** (4.1)–(4.3) imported with `θ>1/2`, giving local exponent `2θ`; bounded bilinear multiplication of norm one and left composition are the exact hypotheses used; the linear solution is derived rather than importing a nonlinear vector-field theorem (lines 2101–2116, 2373–2384).
- **SF04-09 — PASS.** Theorem 11.6 p. 190 with footnote 3 p. 190, p. 191 as adjacent context; Theorem 11.7 explicitly not invoked; `Φ_N` normal-CDF and `Φ̄(y)≤e^{−y²/2}` normalization match the supplied extract (lines 1627–1641, 1687–1694).
- **SF04-10 — INCONCLUSIVE.** Direct Cameron/abstract-Wiener/Borel-enlargement/zero-law checks pass, but upstream eligibility lemmas listed above are absent; end-to-end completion not possible from supplied text.
- **SF04-11 — INCONCLUSIVE/UNVERIFIED.** All 21 assigned source/edition PNGs absent and uninspected; mandatory.
- **SF04-12 — PASS with limits.** Every supplied text carrier and all six consumer modules were read; absent source/upstream/extraction limitations are recorded; no prior vote, hash, or build count was treated as proof.
- **SF04-13 — PASS.** Scope honesty preserved; this is a supplemental text/application audit, not full SF04 clearance, synthesis, or image clearance.

## Noncritical findings

- **Line 224–225 (`L:compact-fractional-phase` consumer context, compact file lines 224–225):** the ground-state spectral projection `Q_σ^sp` is asserted "contractive on both entries" of the weighted phase norm. A spectral (L²-orthogonal) projection need not be a contraction in the half-power weighted norm; uniform boundedness over the compact family suffices and appears to be what is actually used. Overclaim, nonfatal.
- **Lines 90–96 (`compact`):** continuity of the second max–min level `E_2(σ)` across the essential threshold is asserted via form differences but not fully proved; it is standard for norm-resolvent-continuous families below/at the threshold, yet the passage is sketched.
- **Line 492 (`compact`):** the step "nonzero Γ charges some ball → `Γ(B_1)=r^{α−d}Γ(B_r)>0`" relies on homogeneity plus positivity to force `Γ(B_1)>0`; correct for the intended class but deserves one explicit sentence.
- **Line 2109 (`young_upper_foundation`):** `log sup‖U_D‖ ≤ 2c_θB^θd` is not literally implied by `(1−c_θdB^θ)^{−1}` for very small `d`; the later usage only needs `log(4/3)<1/2`, so it is absorbed by constants.
- **Line 1334 vs 1314 (`uniform_products`):** `δN≤1/B` is used while the earlier cell count gives `δn≤2/B`; a factor-2 discrepancy is presumably absorbed, but the two bounds are stated inconsistently.
- **Line 27–28 (`compact`, import paraphrase):** Theorem 10.2 is paraphrased as supplying a "compact smooth core" where the theorem states `C_c^∞` is a core; faithful in substance but narrower than the source wording.

## Checked derivations

- **Square-root comparison:** the subordination identity `√x = π^{−1}∫_0^∞ t^{−1/2}x/(x+t)dt` verified by `t=xv²` (compact 159–164; signed 690–692; uniform 1025–1027); application to `B≤A_σ≤cB` gives quarter-power equivalence `H^{1/2}`.
- **Common trial scaling:** `∫V_σψ_L² ≥ c_0²L^{−d}∫q̄(y)Γ(B_L−y)dy ≥ c_0²2^{α−d}Γ(B_1)∫q̄ · L^{−α}` and kinetic `D_ψL^{−2}`; `α<2` makes `C_ΓL^{−α}−D_ψL^{−2}>0` for large `L` (compact 538–550). Verified.
- **Ground-family continuity:** decomposition `p_τ=ap_σ+r`, `r⊥p_σ`, gives `E_1+Δ_*‖r‖² ≤ q_σ(p_τ) ≤ E_1+2d_V`, hence `‖p_τ−p_σ‖² = 2(1−a) ≤ 2(1−a²) ≤ 4d_V/Δ_*` (compact 106–116). Verified.
- **Phase-isometry wave matrix:** entries `[[C_t, √(h+c)S_t], [−hS_t/√(h+c), C_t]]` in the `E_A` norm; bounds `|S_t|≤min(t,h^{−1/2})` for `h≥0`, `cosh/sinh` for `h<0`; per-entry bound `2(1+K)(1+t)e^{λt}`, 2×2 matrix norm ≤ twice that, condition cost `√(3(1+K²))≤2(1+K)` gives `8(1+K)²(1+t)e^{λt}` (signed 750–782; uniform 1066–1091). Verified.
- **Signed form budget:** `|v_V(u,u)|≤Kbz≤z²/2+K²b²/2`, `c=2+K²`, lower `½z²+(1+K²/2)b²`, upper `≤3(1+K²)z²=` `L_K z²` (signed 649–662; uniform 990–1003). Verified.
- **Rate continuity:** unit `ε`-minimizer with `β(W)≤0` forces `z≤K+2`; multiplier difference bounded by `(K+2)‖L_V−L_W‖`; square-root step on `−β≥0` (uniform 1116–1123). Verified.
- **Primitive/growth constants:** `G_B≤√(2B²+3)≤3B`, `C_B=G_B²[B^{1−1/r}+B^{1−1/r−θ}]≤18B^{3−1/r}`, `C_BB^{1/r}≥B`; Hölder exponent `1−1/r>θ` from `r>(1−θ)^{−1}` (uniform 1211–1243). Verified.
- **Power-mean identities:** `δ∑v_m≤(2/B)^{1−1/p}Y`, `δ∑v_m^ν≤(2/B)^{1−ν/p}Y^ν` with `p/ν≥1`, including `p=ν` and empty cells (uniform 1311–1314, 1462–1467; tubes 1972–1983). Verified.
- **Polynomial balls:** with `K_B=B^s`, exponent `B^{r(3+κ)−sr}` negative since `s>3+κ`; second exponent `B^{r(3+κ)+s(ν−r)}` negative for `s>r(3+κ)/(r−ν)`; `L_{B,K_B}/B→0` (uniform 1375–1389). Verified.
- **Borell radius chain:** `K=C(B̄_H(1))=√δ M_δ(B̄_H(1))`, `T_r=A_δ+(r/√δ)K`, `â≥0`, so `P(d_δ(X)>r)≤e^{−r²/(2δ)}` (tubes 1684–1696). Verified.
- **Rayleigh transfer:** density `(r/δ)e^{−r²/2δ}` has mass 1 and survival `e^{−r²/2δ}`; `Cr^ν−r²/2 ≤ −M²/8−r²/8` under `4C≤M^{2−ν}`, `1<ν<2`; integral `4e^{(A_0−M²/4)/δ}` (tubes 1542–1746, 2021–2040). Verified.
- **Half-action identity:** `sup_{r≥0}{g_J(r)−r²/2} = sup_h{J(h)−‖h‖²/2}` (tubes 2052–2060). Verified.
- **Young local contraction:** `N_ℓ(I_D(V)) ≤ c_θ[D]_θℓ^θN_ℓ(V)`; covering-piece growth; inverse via Neumann and identity for inverse seminorm (young 2103–2133; constant-young 2402–2456). Verified modulo the noted small-`d` log constant.
- **Multiplicative perturbation identity:** `U_{H+X}=U_HU_Z` with `Z=∫R dX U`, via `2θ` remainder substitution (young 2150–2173). Verified.
- **Constant-phase free kernel:** entry masses `1,t,0,1`; constants lie outside `H^{±1/2}` (`δ_0` not locally `L²`); Peetre-based boundedness of `L_ψ` (constant 2221–2277). Verified.
- **F-Duhamel/branches:** `D_σ(c_1,c_2)=(0,V_σc_1)`, `ℓ_σ^C(c)=f_σ(c_1/λ_σ+c_2/λ_σ²)`, tail identity, `f_σ=∫V_σp_σ/(2λ_σ)>0`, positive margins `ℓ_σ(e_0)=f_σ/λ_σ>0` (compact 347–375). Verified.
- **Signed F bound:** `∫_0^t(1+t−s)(1+s)ds=t+t²+t³/6`, combined constants via `√(8²+9²)<13` give `16(1+K)^4(1+t)³e^{λt}` (signed 860–880). Verified.
- **Actual covariance scale:** `g_δδ^{a/2}=δ^{(1−a)/2}δ^{a/2}=√δ`; zero-covariance classes consistent throughout (tubes 1831; uniform 910–913, 1124–1125). Verified.

## Required fixes before production gate

1. **Supply and display-verify all 21 assigned PNGs** (SF04-01, SF04-07, SF04-11). Text metadata cannot establish Teschl second-edition title/copyright/pagination or Friz–Hairer printed offsets. This is a hard gate for the full SF04 component and was not changed by this supplemental pass.
2. **Supply or re-audit the upstream lemmas/propositions listed in Critical finding 2** before certifying SF04-10 and the actual-law/point-transfer chain end to end.
3. **Soften or prove the "contractive" claim** for the ground-state spectral projection `Q_σ^sp` (compact 224–225); uniform boundedness is enough and should be stated instead.
4. **Add an explicit sentence** proving `Γ(B_1)>0` for nonzero homogeneous even covariance, and a precise argument for continuity of `E_2(σ)` across the essential threshold at level zero.
5. **Reconcile** `δN≤1/B` with the stated `δn≤2/B`, and the small-`d` logarithm bound in `L:young-upper-growth`, or explicitly absorb both into constants.
6. **Provide the `c²/6` white-energy and finite-Gram variational identification** if the abstract's quantitative claims are to be considered checked; they are outside the supplied excerpt.

## One-line summary

The six supplied consumer modules are largely internally coherent, with correct signs, constants, branches, and source-theorem hypotheses at the directly supplied applications, but full SF04 clearance stays INCONCLUSIVE (missing images SF04-01/07/11 and several unsupplied upstream lemmas for SF04-10), so this is a favorable supplemental text/application pass only.