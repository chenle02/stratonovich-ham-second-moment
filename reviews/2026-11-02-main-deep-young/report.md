# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

None. I found no invalid identity, sign error, incorrect constant, false hypothesis, or invalid asymptotic in PROOF104–111. The eight target proofs are analytically coherent, and their joins to the embedded source/operator prerequisites have consistent hypotheses.

## Noncritical findings

1. **PROOF107** claims growth bound `exp(C_T(1+‖D‖_{C^θ})^{1/θ})`. The proof actually yields `exp(C'(1+‖D‖_{C^θ}^{1/θ}))`. Because `(1+x)^{1/θ} ≥ 1+x^{1/θ}` for `x≥0`, `θ∈(0,1)`, the stated bound is a valid (but looser) upper bound. Not mathematically wrong.
2. **PROOF107** uses `E:constant-young-estimate` with the integrator increment composed **to the left** of the integrand, whereas Friz–Hairer (4.3) is printed for the integrand composed to the left of the increment. The left-composition version is equivalent by symmetry of the bounded-bilinear Sewing/Young estimate: the refinement error becomes `D(u,t)(V(u)−V(s))` instead of `(V(t)−V(u))D(u,t)`; the same `C_θ[D]_θ[V]_θ|t−s|^{2θ}` estimate holds with the same constant since `‖AB‖≤‖A‖‖B‖`. The manuscript does not state this symmetry explicitly.
3. **PROOF105** `ψ`-independence and the `Ai=iM_E` identity rely on `χ=1` on `B_{2R+T+1}` and `ψ=1` on a neighborhood of `supp χ`. The margins are present and consistent, but the argument is finitely precise and should be checked against the exact support margins at production time.
4. **Joins, not full re-derivation:** I verified the actual hypotheses/joins to `P:source-gaussian-transfer`, `P:source-canonical-convergence`, `P:source-ordinary-response`, `L:driver-gain-localization`, `P:masked-source-moments`, `P:masked-canonical-transfer`, and `L:source-pointfield-regularity`. I did not independently re-prove those unassigned prerequisite modules end-to-end; this is recorded as a limitation, not a discovered defect.
5. Friz–Hairer extraction is text-garbled in places, but pinned (4.1)/(4.3) on printed pp. 61–62 are legible and match the manuscript's use. No source image (credit 0) is supplied; extraction ambiguity is disclosed.

## Checked derivations

All eight bodies were hand-checked against the embedded line-numbered excerpt.

- **YNG01 / PROOF104 (L:constant-phase-free) — PASS, CHECKED.** Distributional injectivity via `δ_0` vs locally-`L²` weighted Fourier functions; Peetre factor `2^{|σ|/2}⟨ξ−η⟩^{|σ|}` correct; `L_ψ` bounded via `L¹*L²` at `σ=±1/2`; free block `S_F(t)(e,c₁,c₂)=(S(t)e,c₁+tc₂,c₂)` matches wave-kernel masses `(1,t;0,1)`; `∂ₜG_d↔cos`, `G_d↔sin/|ξ|`, `ΔG_d↔−|ξ|sin`; finite propagation incl. d=3 sphere kernel; local cancellation between Sobolev and constant parts is sound. `iE` closed proper.

- **YNG02 / PROOF105 (P:constant-phase-driver) — PASS, CHECKED.** `D_χ M_E=M_E=M_E D_χ` from `L:driver-gain-localization` and rational-time/continuity patching; `ψ`-independence via `D_χ(L_ψ−L_{ψ'})z=0`; `Ai=iM_E`, `π_C A=0`, constant columns retained; compact values by bounded composition; `A^ρ→A` in finite `L^p C^θ`; `√p` moments give `E X^{2n}≤C^{2n}(2n)^n`, and `n!≥(n/e)^n` gives square-exponential finite moment exactly when `2ecC²<1`; raw `A` is a deterministic transform of the `W`-measurable driver.

- **YNG03 / PROOF106 (L:constant-source-response) — PASS, CHECKED.** `B_F(b)(e,c₁,c₂)=(0,b(e₁+c₁))`; norm `≤‖b‖∞+‖b‖₂` via `‖·‖_{H^{-1/2}}≤‖·‖₂` (correct, needs only `L²` multiplication, not a full `H^{1/2}` multiplier bound); strong continuity of integrand; operator-norm Lipschitz primitive without an operator-norm derivative; constant-column identity from equality of total free displacement near `supp m` where `ψ=1`, then `P:source-ordinary-response` on the actual `E`-state `L_ψ z`; no density of `E` in `F` used.

- **YNG04 / PROOF107 (P:constant-young-linear) — PASS, CHECKED.** Local estimates verified:
  - `sup‖I_D(V)‖≤[D]_θℓ^θ sup‖V‖+C_θ[D]_θℓ^{2θ}[V]_θ`,
  - `[I_D(V)]_θ≤[D]_θ sup‖V‖+C_θ[D]_θℓ^θ[V]_θ`,
  - hence `N_ℓ(I_D(V))≤c_θ[D]_θℓ^θ N_ℓ(V)` with `c_θ=2max(1,C_θ)`;
  contraction at `c_θKℓ^θ≤1/4`, `N_ℓ(V)≤(4/3)‖V_a‖≤2‖V_a‖`; difference bound `N_ℓ(W)≤2‖W_a‖+2c_θℓ^θδN_ℓ(V')`; induction `E_{j+1}≤2E_j+2^{j+2}c_θℓ^θδB`, `E_j≤2^jE_0+j2^{j+1}c_θℓ^θδB`; piece count uniform in `s,t`; local invertibility `‖U−I‖∞≤1/3` and Neumann inverse; composition, uniqueness, joint continuity via `U_D(t,0)U_D(s,0)^{-1}`. Noncommuting/right-multiplication composition is handled; short last piece reduces coefficient.

- **YNG05 / PROOF108 (P:constant-gaussian-flow) — PASS, CHECKED.** Separable closed path spans + continuous Young map give strong measurability; `π_C U_A=π_C` and `(U−I)F⊂iE` from `π_C A=0` and increment-range in closed `iE`; convergence in probability on radius-`K` balls plus uniform Gaussian tails; uniform integrability via `pC(1+x)^{1/θ}≤cx²+C_{p,c}` with `1/θ<2`; physical flow composition and constant block `(c₁,c₂)↦(c₁+(t−s)c₂,c₂)` verified; conjugation map bounded by `C_T²` transfers moments/convergence; correctly does **not** assert operator-norm continuity of the free group.

- **YNG06 / PROOF109 (L:constant-source-solution) — PASS, CHECKED.** `C(r)=S(−r)B_F(b(r))S_F(r)` with primitive `A_E^ρ`; Young sums become ordinary strong integrals because `U` is uniformly (operator-norm) continuous and `C` bounded — no Hölder hypothesis on `C`; Picard bound `C_T^{n+1}B_T^n T^n/n!` verified; Duhamel map norm `≤C_TB_T T`; cycle/chain identification: forcing `(0,f_r)` with `f_r=b(r)X_{n−1}(r)` yields displacement `∫G_d(t−r)*f_r`; testing identity and absolute Fubini with `‖φ‖∞‖f_r‖₁(t−r)` cover the d=3 sphere measure; exact ordinary canonical data `(1,0)`; no invented weak-SPDE uniqueness.

- **YNG07 / PROOF110 (P:constant-raw-average) — PASS, CHECKED.** `‖O_φ‖≤(‖φ‖_{H^{-1/2}}²+1)^{1/2}`; `Z_m` `W`-measurable and independent of auxiliary `J`; Bochner average `B_φ` equals ordinary integral `C_φ` via `E[ΞB_φ]=E[ΞC_φ]` and `Ξ=sign(B_φ−C_φ)`; `E|C_φ|²≤Q_t²‖φ‖₁²`; source/raw observable difference controlled by `‖O_φ‖‖e₀‖`; `L²` limit realizes the premise of `P:masked-canonical-transfer`; `‖φ‖₁=1` gives `E|Z_m|²≤E|u(t,0)|²`; zero-Γ equality at free constant solution; fixed mask/horizon before time asymptotics; observable is `E|∫φu|²` (square of average), not average of point squares; no `H^{1/2}` point trace.

- **YNG08 / PROOF111 (P:constant-compact-base) — PASS, CHECKED.** `B_F(h)` bound `≤‖h‖∞+‖h‖₂`, range in `iE`, operator-norm Lipschitz primitive with bound `C_T sup_r(‖h(r)‖∞+‖h(r)‖₂)`; `‖A_h+gA‖_θ≤H+GX`; square-exponential shift `E e^{c'‖A_h+gA‖²}≤e^{2c'H²}E e^{2c'G²X²}<∞` for `c'≤c/(2(1+G²))`; alternative `pC(1+H+Gx)^{1/θ}≤cx²+C` transfers all finite moments; source convergence, Young stability, uniform integrability; `h+gmY_ρ` support in one compact union; individual estimates only, no uncountable common-parameter event; only `h=0,g=1` enters the original point comparison; no Cameron–shift claim.

[held back until the source author has been told]

- **YNG10 (Adversarial controls) — PASS.** Free/zero-noise, constant-velocity, scalar/noncommuting order, contraction/inverse signs, `J`/`W` retention, two source-width limits, signed base, square-of-average vs average-of-squares, and `E|Z|²` transfer all checked manually with no formal/kernel claim.

- **YNG11 (Completeness/noncircularity/scope) — PASS.** All eight bodies inspected with exact input-hypothesis joins; no circular canonical-moment identification; closed `iE` not dense in `F`; no point trace/global-`R`/arbitrary-weak-uniqueness/uncountable-common-event assumption; unassigned modules recorded as prerequisite joins, not silently claimed as independently re-reviewed.

## Required fixes before production gate

None blocking. Optional non-blocking clarifications worth adding to the manuscript:

1. In PROOF107, state explicitly that `(1+‖D‖_{C^θ})^{1/θ}` in `E:constant-young-growth` is a conservative majorant of the computed `1+‖D‖_{C^θ}^{1/θ}`.
2. In PROOF107, add a one-line remark that the left-composition Young/sewing estimate is the symmetric (increment-on-left) form of Friz–Hairer (4.3) and holds with the same constant because the product is bounded bilinear.
3. Optional: spell out the exact support-margin inequalities (`supp m ⊂ \overline{B}_{2R}` inside the `χ`-plateau) used in PROOF105/106, for traceability.

## One-line summary

All eight constant-phase Young-flow proofs (PROOF104–111) have correct logic, boundary terms, constants, and joins; the only notes are a conservative growth exponent and an unstated left-composition symmetry of the Friz–Hairer Young estimate, so the set passes with notes at medium confidence.