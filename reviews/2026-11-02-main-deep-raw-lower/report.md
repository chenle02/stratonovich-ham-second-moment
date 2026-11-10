# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

None blocking. I found no sign error, no false identity, no hidden hypothesis, no incorrect final constant, and no invalid limit-order interchanges in PROOF119–PROOF126. The final lower-bound constant `2∫λ_s ds − v/2`, the `√δ`/`δ^{-1/2}` scaling pair, the Gaussian tilt sign `−sZ − s²v/2`, the moderate penalty `δ^{-3/4}`, and the `δ^{1/4} → 0` normalization all check out by hand. The proof chains satisfy the fixed-control/mask/B-before-δ ordering and carry both phase components, the same raw `Z = W(Ψ)`, and the original raw `v/2` action throughout.

## Noncritical findings

1. **PROOF119** asserts equality *in law* of the full canonical series, but the proof only passes finite-order joint laws and `L²`-absolute summability to the **second moment** (Eq. `E:exact-moment-scaling`). This is exactly what downstream proofs need, so it is not a gap, but the stronger “law of the solution” wording is only carried at the moment level inside this proof body.

2. **PROOF124** product-accumulation bound (lines 521–526) reads `d(n+1) ≤ C d(n) + C^n e_src`, whose solution is `d(N+1) ≤ (N+1) C^N e_src`. The text writes `(N+1) C^{N+1} e_src`, which is a (valid) overestimate with one extra factor of `C`. The Hölder step requiring `C ∈ L^{4(N+1)}` still holds, so no consequence.

3. **PROOF120** mean-response identity `b = √δ H`, and in particular the two constant columns and the “total finite propagation” argument, is compressed. It is consistent with `L:constant-phase-free`, `L:constant-source-response`, and the driver column expansions, but the derivation is not spelled out line-by-line here.

4. **PROOF123** rebasing bound `ℓ_c(z) ≥ (1 − νM_z)A` is correct but implicitly uses `|ℓ_c(r)| ≤ νϑA` together with `M_e + ϑ ≤ M_z`; these ingredients are not written on the line. The aperture/entrance/recursion/terminal budgets all close.

5. **PROOF125/126** depend on the premise of `P:masked-canonical-transfer` (that the masked average is the source `L²` limit); this is supplied by `L:raw-block-restart`, but the comparison to `V_δ(1,0)` is a *moment* inequality, not a pathwise field identity. This matches the scope requirement and is stated correctly.

6. **External source fidelity** (Teschl 10.2/10.13/4.12/4.13; Friz–Hairer Young (4.3); Chen author citations) is verified against the embedded excerpts at the invoked uses. The embedded extraction carries the stated caveat that PDF math text may be garbled and PNGs remain required; I did not verify the full citable texts, only the embedded carriers.

## Checked derivations

- **RBL01 — PROOF119 `L:exact-canonical-scaling` — PASS.**
  Checked the scaling algebra by hand. Dilated covariance `Cov(Ẇ(Ts, r_T x), Ẇ(Tt, r_T y)) = T^{-a} r_T^{-α} |s−t|^{-a} Γ(x−y)`; with `r_T = Tδ` the noise amplitude satisfies `r_T^4 (T^{-a} r_T^{-α}) = T^{-a} r_T^{4-α} = δ` (using `κ(3−α)=4−a−α`). Green scaling `G_d(Tτ, r_T dz) = r_T G_d(τ/δ, dz)` is the correct `c G_d(ct, c dz)` homogeneity; `δ^{-1}G_d((t−s)/δ)` multiplied by `√δ` gives the vertex factor. Both displayed positive-power identities verify:
  `T^{-a/2} r_T^{2-α/2} = δ^{1/2}` and `T^{1-a/2} r_T^{1-α/2} = δ^{-1/2}` (each reduces to `4−a−α = κ(3−α)`). Green-before-noise (d=3) and fixed-T ordering are respected; no large-time/source interchange.

- **RBL02 — PROOF120 `L:raw-block-inputs` — PASS.**
  Pullback isometry recomputed: `δ^{a−2}·δ²·δ^{-a} = 1`; null-quotient respected because the map is exactly isometric. `W_{δ,m}(f)=W_fast(f(·−mB,·))` is a literal common-space identity. Mean-Jacobian `E[W_{δ,m}(f)Z]=δ^{a/2}∫f(u,x)h_{s_m+δu}` follows by the substitution `u=(s−s_m)/δ`. Then `g_δ δ^{a/2} = δ^{1/2}` gives `b = √δ H`. `‖X_m‖_{L^p} ≤ C√p g_δ` follows from the driver `√p` norm bound scaled by `g_δ`. Separability of `B_0` via polygonal rational matrices and the `[f]_θ ≤ (2‖f‖_∞)^{1−θ} Lip(f)^θ` interpolation are sound. Mean extension `[0,2]` vs templates `[0,1]` is consistent since `s_m ≤ NδB ≤ 1` and `s_m+δB ≤ 1+δB < 2`.

- **RBL03 — PROOF121 `P:raw-block-gaussian-law` — PASS.**
  Tilt sign and constant verified. Under `Q_s` (density `exp(−sZ − s²v/2)`), completing the square shifts `Z` by `−sv` and `X` by `−sb`; hence `E_P[e^{-sZ−s²v/2} j(X+sb)] = E_P j(X)`. With `s=δ^{-1/2}` and `sb = δ^{-1/2}√δ H = H`, this is exactly `E j(X) = E[e^{-Z/√δ − v/(2δ)} j(X+H)]`. Norm-Borel generation by matrix entries at rational times plus `{0,B}`, countable dense unit vectors for `‖T‖`, Hölder norms as rational-time suprema, cylinder pi-system/monotone extension including extended nonnegative integrals, and absence of any translated exceptional-domain assumption are all correct. The variance `v` stays the original raw `E[Z²]`.

- **RBL04 — PROOF122 `L:raw-block-uniform-error` — PASS.**
  Maximum bound `‖M_δ‖_p ≤ C√p δ^{(1−a)/2 − 1/p}` uses `N+1 ≤ 2/δ`, so `M_δ→0` in every `L^q` by choosing `p > max(q, 2/(1−a))`. Even moments `E M^{2n} ≤ 2 C^{2n}(2n)^n δ^{n(1−a)−1} ≤ 2C^{2n}(2n)^n` for `n0(1−a)≥1`, Lyapunov for `n<n0`, and `n! ≥ (n/e)^n` give the square-exponential tail `Σ(2ecC²)^n`. Uniform `H_0` plus `‖H_m − H_m^stat‖ ≤ Cδ`, local Young stability on `{M≤1}`, and the global Young growth dominated by `exp(cM²)` (using `1/θ<2`) close the `L^q` operator-error convergence and uniform integrability. Operator-norm measurability via rational times/states is standard; no independence claim is used for the maximum bound.

- **RBL05 — PROOF123 `L:raw-block-indexed-cone` — PASS.**
  All five ε-budgets close. Entrance checks: normalized amplitude ≥ `a_*/2`, normalized residual ≤ `q_B M_Q E0 + M_Q ε_op E0 ≤ ϑ a_*/4`, ratio ≤ `ϑ/2`. Recursion: `x ≥ (1 − νM_z − M_ℓ ε_op M_z)A ≥ (1−ρ)A`; `y ≤ q_B(ϑ+νM_z)A + M_Q ε_op M_z A ≤ ϑA/2`; with `x> A/2` this forces `y ≤ ϑx` and cone preservation with amplitude factor `e^{λ_c B}(1−ρ)`. Terminal: `ℓ_c(z) ≥ 3A/4`, `‖Q_c z‖ ≤ 2ϑA`, `e^{-λu}O_φ(P_c(u)z)/A ≥ 3j_*/4 − 2H_obs C_gap ϑ`, and `16H_obs C_gap ϑ ≤ j_*` with the perturbation budget give `≥ j_*/2`; the assembled constant is `c_* = a_* j_*/4`. `N=1` and `u=0` are covered. No positivity/composition/independence premise on the `D_m` is needed.

- **RBL06 — PROOF124 `L:raw-block-restart` — PASS.**
  One retaining slow source and its pointfields are consistent: `Y_fast(u,x)=δ^{a/2}Y(δu,x)`, `Y_m(u,x)=Y_fast(mB+u,x)`, and `δ^a K_η(δr)=K_{η/δ}(r)`. The conjugation identity `S_F(mB)[A_glob^src(mB+u)−A_glob^src(mB)]S_F(−mB)=X_m^src(u)` is a group-cocycle computation with no mask commuted through a free group and no separate retaining-extension commutation assumed. Ordinary primitives equal their Gaussian-transfer drivers; fixed-δ,N source limits pass to finite `m` and piecewise-continuity gives simultaneous identities in `u`. The recurrence solution is actually `d(N+1) ≤ (N+1)C^N e_src` (text overestimates to `C^{N+1}`), and Hölder with `C∈L^{4(N+1)}`, `e_src∈L^4` gives `L²` convergence at fixed `δ,N` without growing-product uniformity.

- **RBL07 — PROOF125 `P:raw-block-point-comparison` — PASS.**
  `j_δ` is everywhere-defined, continuous, nonnegative on the whole `B_δ`; the square identity is `P:raw-block-gaussian-law` applied to `j_δ`. `Γ_δ = g_δ² Γ` preserves degree `α` and temporal parameter `a`; source chains scale by `g_δ^n`. The masked-to-unmasked comparison is a moment inequality at amplitude `Γ_δ` via `P:masked-canonical-transfer`; the ordinary fast-to-slow change `t=δu` with phase `(V, δV_t)` gives `g_δ Y_fast(u)=√δ Y(δu)` with cutoff `η/δ`, i.e. exactly the regularized fast equation. The `r_T = Tδ` physical scale is correctly distinguished from the fixed mask radius `R`, and source limits precede large-time comparisons.

- **RBL08 — PROOF126 `P:raw-block-original-lower` — PASS.**
  Fixed `e_rate` → `ρ`, then cone constants and fixed `B`, then `δ→0`; `e_rate→0` only afterward. `P(E_δ)→1` by `L:raw-block-uniform-error` (L^q → in probability) and Chebyshev `P(|Z|>δ^{-1/4}) ≤ v δ^{1/2}`, with no independence. On `E_δ` the cone yields `Y_{δ,B}>0` and the exponential bound; the last two summands form the left Riemann sum for `I_R` with final cell length `δτ` and mesh `δB`, Lipschitz error `C_R δB`; `log(1−ρ) > −e_rate/3` plus `δ|log c_*|` and `C_R δB` each `≤ e_rate/3` give `Y ≥ exp((I_R−e)/δ)`. Restricting the nonnegative square integrand to `E_δ` gives `E U² ≥ p_δ exp((2I_R−2e−v/2)/δ − δ^{-3/4})`; `δ δ^{-3/4}=δ^{1/4}→0` and `δ log p_δ→0` give `liminf δ log E U² ≥ 2I_R − 2e − v/2`. The comparison `E U² ≤ E|u(T,0)|²=E|V_δ(1,0)|²` is B-independent, so `e→0` yields `2I_R − v/2`; translation preserves the point second moment. The `−v/2` is the correct half-action from `s=δ^{-1/2}`.

- **RBL09 — Primary/input fidelity — PASS (with extraction limitation).**
  Compact-mean ground family/`F`-projection/normalized-complement, Young/source/masked identities, original Green/noise conventions, and the Teschl statements (10.2, 10.13, 4.12, 4.13) are present in the embedded inputs and used consistently at their named uses. No old-review premise, first-moment constant, or Skorohod comparison enters the proofs. Image credit zero and extract uncertainty are explicit.

- **RBL10 — Manual adversarial controls — PASS.**
  Dilation exponents and one-vertex test factor close; Gaussian tilt sign and half-variance close; `N1/τ` cone product and `N=1`/`u=0` edges close; old residual is explicitly not assumed to lie in the new kernel; `c_* = a_*j_*/4` and the `u=τ∈[0,B)` terminal are correct. The square-functional inequality `E U²↔E[· Y²]` replaces any point/average-of-squares or independence shortcut; zero-Γ goes through the free/source model; the fixed source-product order is retained. No ordering rule, positivity premise, or scalar-moment block multiplication is introduced.

- **RBL11 — Completeness/noncircularity/scope — PASS for the bounded unit (global obligations out of scope).**
  All eight proof bodies and the same-canonical-solution joins are reconstructed; every material unverified passage is named as INCONCLUSIVE-adjacent-but-consistent above (constant-column identity, law-vs-moment strength, recurrence constant). Original dimensions/covariances/amplitudes are retained and fixed-control/mask/B/source-limit order is correct. The full 213-proof/global/source-image/main/cold obligations are explicitly not part of this bounded MAIN unit and remain unverified here.

## Required fixes before production gate

None blocking for this unit. Recommended clarifications (not proof-breaking):

- In `L:raw-block-restart`, write the accumulation bound as `d(N+1) ≤ (N+1) C^N e_src` (or keep `C^{N+1}` but note it is a deliberate overestimate).
- In `L:exact-canonical-scaling`, state that the equality-in-law assertion is used only through its second-moment consequence in this chapter, to avoid overclaiming full process-law strength beyond what is carried.
- In `L:raw-block-inputs`, add a short explicit display deriving `b=√δ H` on the two constant columns (finite propagation + `L_ψ` columns), instead of the current prose.
- Record the extraction limitation (PDF math garbling, PNG-required) in the review-facing artifact of this unit, matching the honesty requirement.

## One-line summary

All eight proofs (PROOF119–PROOF126) reconstruct with correct scaling powers, tilt sign, half-variance, cone budgets, and limit ordering; no blocking gap found — PASS_WITH_NOTES, MEDIUM confidence.