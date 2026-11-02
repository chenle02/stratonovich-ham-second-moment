# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I found no false identity, sign error, incorrect final coefficient, or invalid large-time/asymptotic claim inside PROOF165–PROOF169. The five proofs are internally consistent with each other (free → source-mean → source → raw → block-mean) and each of the load-bearing claims specified in the scope is discharged in the direction the manuscript states.

Specific dishonest-overclaim screens:
- The distinction “determinant-one concerns only each finite 2×2 Fourier matrix of the FREE group; no determinant of the full infinite operator; `P*J_EP=J_E` gives norm≥1 but NOT surjectivity” is respected throughout. PROOF165 (Lemma L:symplectic-free) verifies det-one only blockwise via `W_t^T J_symp W_t = J_symp` in `L^2×L^2`; PROOF168 (P:symplectic-raw) proves invertibility separately through Young short-piece Neumann inverses, never by invoking `P*JP=J` alone.
- The unscaled covariance factor in the block direction is stated and used as `δ^{a/2}`, not `√δ` (`E[M_m(u)W(i_IΦ)]=δ^{a/2}H_{m,E}`), and the direction is `φ_m=δ^{-a/2}T_m^*i_IΦ`. The `√δ` factor appears only in the *full driver* covariance `E[g_δA_{F,m}W(i_IΦ)]=√δ H_{m,F}`, and the normalization relationship `g_δ δ^{a/2}=√δ` is correct with `g_δ=δ^{(1-a)/2}`.
- The `E`-closed-not-dense-in-`F` restriction is explicit, and the constant columns are retained until compression. No `E`-dense-in-`F` argument is used.
- No uncountable-parameter event, rough free-generator derivative, or `H_W`-valued Gaussian random vector is asserted. All almost-sure arguments run through countable source sequences / countable dense states / rational times and fixed parameters.

## Noncritical findings

1. **PROOF165 over-hypothesizes smoothness of `b`.** The lemma statement says “bounded real smooth `b`,” but the skewness proof uses only `‖b‖_∞<∞`: the cancellation is `−∫fbu + ∫ubf = 0` on `L^2` functions with `bu,bf∈L^2⊂H^{-1/2}`. Smoothness is unnecessary. This is not an error; it is a formulation nuisance (the condition is stronger than needed and makes the hypothesis look analytic when only boundedness is used).

2. **PROOF167 `C^1` trajectory claim is conditional on the established Lipschitz primitive of `D^ρ`.** The differentiability `d/dt U = C_b(t)U` is immediate because `D^ρ` is already the primitive of a bounded, strongly continuous `C_b`, so the Young integral coincides with the strong Lebesgue integral. The proof sketches rather than spells out this “Young = Lebesgue for a Lipschitz driver” identification; it is correct but compressed.

3. **PROOF168/169 cannot be externally verified at their imported sources.** The proofs cite `friz.hairer:20:course` sections and the completed full-`F` mean `T` of P:cameron-full-mean, none of whose full bodies are in this bounded packet (the friz–hairer excerpt is not supplied; the Cameron-mean proposition is in the prerequisite chain outside the target excerpt). I audited the specific constants each proof exports (`1/θ<2`, the `2^{-4n}` Borel–Cantelli budget, `δ^{a/2}`, `‖φ_m‖≤δ^{-a/2}‖Φ‖`), but the derived Young constant `C_θ` and the `L^r` compactness of `T` are taken as established upstream inputs, not re-proved here. This is a scope limitation, not a defect found.

4. **PROOF169 relies on `ℓ_m=0` giving identity, and on stopped equality only up to `ℓ_m`.** Both are stated exactly; the empty-last-cell case is explicitly handled (`U=I`, norm one). No unstopped equality beyond `ℓ_m` is asserted. Recorded as a note only to confirm compliance with the scope’s “stopped driver identity holds only through ℓ_m.”

5. **Notation collision `D` = symplectic form vs. `D` = driver is only mildly risky.** In proofs 166–169, `D_Φ`, `D^ρ`, `D` denote drivers, while `ω(z,w)` denotes the symplectic form; there is no conflict but the reading requires care at `D_Φ = E[ZM]`.

## Checked derivations

**SYM01 — PROOF165 `L:symplectic-free` — PASS (full coverage).**
Reconstructed: balanced unitary `C_bal(u,v)=(Λ^{1/2}u,Λ^{-1/2}v)` is an onto real isometry `E→L^2×L^2`; `J_symp(q,p)=(p,−q)` is bounded, isometric, skew, `J_symp²=−I`; pullback `J_E=C_bal^{-1}J_symp C_bal` inherits all properties, with `J_E(f,g)=(Λ^{-1}g,−Λ f)` and `J_E²=−I`. The duality form `ω(z,w)=⟨u,g⟩_{1/2,−1/2}−⟨f,v⟩_{1/2,−1/2}` follows from the balanced `L^2` pairing; no `L^2` pairing of a distributional velocity is taken. Free group: balanced kernel `W_t(ξ)` is symplectic blockwise because det `=cos²+sin²=1`; at `k=0` the matrix is `[[1,t],[0,1]]` and `W_t(0)^T J W_t(0)=J` (computed). Integration against real phases with Hermitian symmetry and `L^2` Cauchy–Schwarz legitimizes `ω(S_E z,S_E w)=ω(z,w)`; no rough generator derivative, no frequency-zero trace. Force skewness: `‖bu‖_{H^{-1/2}}≤‖bu‖_2≤‖b‖_∞‖u‖_{H^{1/2}}`; the cancellation `−∫fbu+∫ubf=0` (with `w=(f,g)`) is exact on `L^2` functions — this is L²-multiplier cancellation, NOT Hilbert-skewness.

**SYM02 — PROOF166 `L:symplectic-source-mean` — PASS (full coverage).**
`D_Φ=E[ZM]`, `D_Φ^ρ=E[ZM^ρ]` are Bochner-defined; `‖D_Φ^ρ−D_Φ‖_{C^θ}≤‖Φ‖_{H_W}‖M^ρ−M‖_{L^2C^θ}` is Bochner Cauchy–Schwarz (plus Z∈L² with `‖Z‖_{L²}=‖Φ‖_{H_W}`), and the uniform bound `‖D_Φ^ρ‖_{C^θ}≤‖Φ‖_{H_W}‖M‖_{L^2C^θ}` is the covariance-contraction counterpart. The regularized mean `h_Φ^ρ(t,x)=⟨j_srcΦ, v_{ρ;t,x}⟩_G` is a genuine point evaluation of a deterministic `G`-valued map, so time continuity and all spatial derivatives (bounded linear testing commutes with derivatives) — NOT a pointwise raw potential. The primitive identity `D_Φ^ρ(t)=∫ S_E(−r)B(m_R h_Φ^ρ(r))S_E(r)dr` is the same physical-adjoint row computation as P:source-ordinary-response with `(Y^ρ↔h_Φ^ρ)`, with mask once after covariance convolution and Fubini/indicator approximation completing the rows. Linearity in `(c,Φ)` and the potentially noncentered/sign-changing combined source `b^ρ=m_R(cY^ρ+h_Φ^ρ)` are stated correctly.

**SYM03 — PROOF167 `P:symplectic-source` — PASS (full coverage).**
Intersect finitely many source coefficient events (fixed positive `ρ`) with the event identifying the actual primitive with the ordinary primitive for all times. On it `C_b(r)=S_E(−r)B(b^ρ(r))S_E(r)` is uniformly bounded and strongly continuous; ω-skewness at each `r` comes directly from `L:symplectic-free`. The Young sums coincide with statewise integrals because `D^ρ` is a Lipschitz primitive and `U` is uniformly continuous on the partition; each state trajectory is `C^1` with derivative `C_b(t)U(t,s)e`; applying the derivative to the bounded bilinear form `ω(Ue,Uf)` gives zero. This is the ordinary-integral route (no Hölder continuity of the noise path and no uncountable null intersection). Free conjugation `P=S_E(t)U S_E(−s)` preserves the identity and inherits `C^1` on all `E`.

**SYM04 — PROOF168 `P:symplectic-raw` — PASS (full coverage).**
`D^ρ→D` in every finite `L^p C^θ` and `‖D^ρ‖_{L^p C^θ}≤C√p`, giving square-exponential tails; the Young upgrade uses `C_T exp(C_T(1+‖D^ρ‖)^{1/θ})` with `1/θ<2` to get uniform `L^p` triangle convergence. The almost-sure subsequence uses `2^{-4n}` squared-uniform-difference bound + Markov + Borel–Cantelli, then intersects countably many source-conservation events; `P_D` is `W`-measurable, so the conservation event of probability one on the extension descends to the base. The `E/F` restriction `U_F i=i U_E`, `P_F i=i P_E` is proven from `A_F i=iM` and Young uniqueness (E closed, isometric, not dense in F). `P_D^*J_EP_D=J_E` gives `1≤‖P_D‖²`, and invertibility is the separate Young Neumann argument. `c=0` deterministic, `Φ=0`, and the fixed `δ` growing-cone instance `W_fast=W∘T_{δ,0}`, `R=δ^{-1}+2`, `T=δ^{-1}`, `c=g_δ` are all stated as pointwise fixed-parameter facts, not a uniform budget.

**SYM05 — PROOF169 `P:symplectic-block-mean` — PASS (full coverage).**
True partition `B,δ,N,s_m,ℓ_m`; `i_I:H_I→H_W` closed inclusion; `T_m:H_fast→H_W` isometry (covariance factor `δ^{a-2}δ²δ^{-a}=1`); `φ_m=δ^{-a/2}T_m^*i_IΦ` (adjoint a contraction, finite at fixed δ). The rank-zero completed-mean identity `E[g_δA_{F,m}(u)W(i_IΦ)]=√δ H_{m,F}(Φ)(u)` compresses though `i` to `E[M_m(u)W(i_IΦ)]=δ^{a/2}H_{m,E}(Φ)(u)` (unscaled `δ^{a/2}`); first-chaos orthogonality to `I−T_mT_m^*` converts `W(i_IΦ)` to `W_m(T_m^* i_IΦ)`; multiplying by `δ^{-a/2}` gives the direction identity up to `ℓ_m`, stopped afterward. Applying P:symplectic-raw with `c=0`, reference `W_m`, gives `‖S_E(ℓ_m)U_{H_m}(ℓ_m,0)‖≥1`; `ℓ_m=0` gives identity. Parameter compatibility follows `1−1/r>θ` in the full package. All direction/norm/covariance scalings match the scope exactly.

**SYM06 — Input/consumer fidelity — PASS (within bounded context).**
The exact joins — source/Young/Cameron/raw-pullback parameters, full-phase/adjoint identities, mean-as-Bochner-covariance (not pointwise potential), finite-2×2 determinant vs. infinite invertibility, norm-baseline vs. uniform stochastic budget — are all present and correctly connected. No covariance-order shortcut and no old-review premise is used inside the five bodies. The external text (friz–hairer/Teschl/Crouzeix) is not verified here; the specific constants each proof carries out of those imports are checked.

**SYM07 — Manual falsification — PASS; controls all produce the expected behavior.**
Zero-frequency free shear: `W_t(0)^T J W_t(0)=J` and the skewness bracket still vanish at the shared zero eigenvalue mode. Real bounded force: `∫bug=∫ubf` cancellation is real-valued and sign-exact. Sign-changing mean: nothing requires `h_Φ^ρ≥0`; noncenteredness is preserved. Zero `Γ/c/Φ`: drivers/means vanish and reduce to the free symplectic identity (stated at the section end). Finite 2×2 vs. infinite proper embedding: the determinant claim scopes to free Fourier blocks; no determinant of the infinite operator appears. Actual δ-exponents and raw-range projection: `φ_m=δ^{-a/2}T_m^*i_IΦ` and `δ^{a/2}` covariance verified; the projection `T_mT_m^*` is used only as the raw-range projection for first-chaos orthogonality. Stopped/empty block: `ℓ_m=0` gives `U=I`, norm one. None of the falsification controls breaks a claim.

**SYM08 — Completeness / noncircularity / scope — PASS (full coverage with the one external-input limitation recorded).**
All five bodies are reconstructed with actual domains/measurability/common-events/limits. Every missing input I could not check is sourced from the prerequisite chain (not from the five bodies): the completed compact mean `T` (P:cameron-full-mean) used by PROOF169, the `r`/`θ` parameter package of S:actual-cameron-mean, and the Friz–Hairer Young estimates. The only missing in-packet citation bodies are the external text carriers (friz–hairer excerpts, Teschl, Crouzeix); none puts an internal step of the five proofs at risk. `E` is used closed, not dense in `F`; no uncountable parameter event, rough generator, or `H_W`-valued random vector appears. No coarse/hidden hypothesis was smuggled into the bodies.

## Required fixes before production gate

No mandatory fixes. Recommended non-blocking edits only:
1. In Lemma L:symplectic-free, replace “bounded real smooth `b`” with “bounded measurable real `b`” (or explicitly note that smoothness is not used), because the skewness proof and the `H^{-1/2}` bound need only `b∈L^∞`.
2. In P:symplectic-raw, make the one-line identification “Young integral of a Lipschitz primitive equals the strong Lebesgue integral of its derivative” explicit, as it is implicit in the a.s. conservation passage.
3. Optionally state beside each genuinely external constant (`C_θ` of Young, `r` of the Cameron package) that it enters as an upstream input; this is cosmetic, since the bodies already carry those specific constants correctly.

## One-line summary

PROOF165–169 reconstruct entirely; the symplectic/norm-baseline/invertibility split, the actual Bochner source/raw conservation, and the exact unscaled `δ^{a/2}` block-mean direction with the pure-mean endpoint norm bound are all correct and non-circular, with only cosmetic over-hypothesization and compressed-but-valid C¹/Young identifications.