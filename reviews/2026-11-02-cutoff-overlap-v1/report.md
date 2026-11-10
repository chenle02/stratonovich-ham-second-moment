# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

**C3 is not literally an interface of the inlined sources.** `P:source-ordinary-response` supplies C2 at initial time zero: for fixed `rho` and fixed `R`, the statewise strong integral `L_rho(t)z = ∫_0^t S(-u)B(b_rho(u))S(u)z du` is an operator-norm Lipschitz path on `E` and equals `M_R^rho`. But C3 claims the full-phase ordinary Duhamel equation for *every* initial `E` state and *all* `s≤t`, on a common event for fixed `R,T,n`. That statement appears only inside the proof of `L:constant-source-solution`: the paragraphs "Thus the Young equation is precisely the ordinary interaction integral on states… Its unique `C([0,T];F)` solution follows…" It is not a stated lemma, and the printed lemma conclusion covers only the `(1,0)` displacement `P_{A^ρ}(t,0)e_0`. The two-point case (initial state at time `s`, on `[s,T]`) is implicit, not written. This is the central seam of O1, and it is not yet stated as a theorem. The candidate itself flags this honestly in C3, so this is a required repair, not a hidden assumption — but it must be emitted as a lemma before the gate.

**C5’s ordinary-propagation half is also unstated.** Free propagation is genuinely proved: `L:driver-gain-localization` (both entries of `S(±t)`, support enlargement `≤|t|`, nonpositive boundary flux, no scalar restart) and `L:constant-phase-free` (finite propagation on `F` for total distributional data including constants). But the ordinary *perturbed* propagation — "coefficient `b=m_R Y_n` with speed-one dependence domain implies `D_χ_j P^n_R D_ψ_N` is independent of `R,N` subject to `R,N≥2j+T+3`" — is not a named theorem in the inlined texts. It follows from free propagation plus the Duhamel/Picard support induction already sketched in `L:constant-source-solution` (the `G_d` recursion with chronological supports), but the quantitative two-mask/two-data-cutoff identity required for O1’s zero middle term must be stated with its cone guard. As written, C5 declares this as an obligation; it is not supplied by any cited label.

These two items are the reason for NOTES rather than a clean PASS. They are not fatal: the arguments exist in proof form, and the candidate explicitly requires their derivation rather than assuming raw overlap.

## Noncritical findings

- **C1 field lives on a retaining extension, not on `W` alone.** `L:source-retaining-isometry` introduces an independent completion noise `J`; `Y_ρ = I(Q_ρΦF)` is a function of `(W,J)`, not of `W`. This is acceptable for O1/O2 because the raw flows are `W`-measurable (`P:constant-phase-driver`, last sentence) and the source term cancels in the zero-expectation argument, so the limiting event `Ω0` is on the original probability space. But any downstream claim that `Y_n` is a *function of the given `W`* is false; it is only a same-space/common-extension realization.
- **F→E restriction and C4 compression are routine but unwritten.** `P:constant-flow-range` gives `π_C U = π_C` and `(U-I)F ⊂ iE`, and `S_F(±r)` preserve `E`, so `P_A(t,s)` maps `E` into `E`; the compression `B(F) → B(E)` is norm-bounded (`≤1` on the inherited norm), so the `L^p` uniform-triangle convergence transfers from `F` to `E`. This is sound but should be one sentence in a lemma.
- **Cutoff norms are not uniform in `j,N`.** `D_{χ_j}` and `D_{ψ_N}` are bounded multipliers on `H^{±1/2}`, but with `(j,N)`-dependent operator norms. The O1 proof needs only per-tuple finiteness (`‖D_χ‖‖D_ψ‖` is a fixed finite constant for each integer tuple), not uniformity; this should be stated so no one reads a false uniform constant into the bound.
- **Horizon compatibility of the raw driver base is never stated.** The inlined driver builds `M_R` on fixed `[0,T]`. O2 is rescued by extremals: define `P_{R,T}` as the `n→∞` uniform-triangle limit of `P^n_{R,T}`, and since `b_{R,n} = m_R Y_n` is time-horizon-independent, `P^n_{R,T2}|_{T1} = P^n_{R,T1}` pathwise; uniqueness of `L^p` limits then gives O2. This sidesteps the need for a separate `M_R`-horizon-gluing lemma, but that convention must be recorded.
- **Constant check.** The margin `R,N ≥ 2j+T+3` is correct for the given `ζ` (equal one on a neighborhood of `B_1`, zero off `B_2`): observation support is `B_{2j}`, the influence domain has radius at most `T`, so `B_{2j}+T ⊂ B_{2j+T+3}` is covered by `R=j-span` scale and by `N`; the extra `+3` is strict margin. No wrong constant was found here.
- **External citations.** The author-source normalization matches (`(1.20),(1.21),(2.9),(2.11)`) and the Friz–Hairer Young estimate are cited by label. Per instructions I did not verify the external papers; the target does not depend on them as premises (C1–C5, O1–O3 are self-contained), so this is recorded, not blocking.

## Checked derivations

**L01 — same noise/source across masks and horizons.** PASS. The driver basis `{f_j}` and `g_j = W(f_j)` are `R`-independent (`L:driver-noise-basis`); only the coefficients `A_j(I)`, hence `M_R`, depend on the mask. The retaining isometry gives one `I` on `G` and one point field `Y_ρ(t,x) = I(v_{ρ;t,x})` independent of `R,T`, so C1’s "same `Y_n` for every mask and horizon" is genuinely supplied, on the extension.

**L02 — fixed-mask E restriction and phase interpretation.** PASS. `P_{R,T}` is the closed `E` restriction of the `F` flow; invariance uses `π_C U = π_C` and `(U-I)F⊂iE`, not density of `E` in `F`, exactly as the candidate claims. `Ai = iM_E` and free-group intertwining give the correct `E` driver, with `L_ψ` a harmless localization dummy.

**L03 — all-E ordinary Duhamel identification.** PASS_WITH_NOTES (see critical finding). C2 is literal; C3 is actionable from the proof of `L:constant-source-solution` but must be promoted to a stated all-state/all-`(s,t)` theorem.

**L04 — finite propagation and the `2j+T+3` guard, both components.** CONDITIONAL/PASS. Guard arithmetic is correct for both phase components at speed one. The ordinary-potential half must be stated from the free support results plus the Duhamel support induction already present.

**L05 — measurable uniform triangle convergence; expectation transfer.** PASS. `P:constant-gaussian-flow` gives strong measurability and finite `L^p` moments in uniform triangle norm, locally Lipschitz in the driver; the transfer to O1 uses only triangle inequality with bounded cutoffs and expectation of a nonnegative `W`-measurable variable tending to zero. No optimizer, no `S_q` transfer, no impossible norm continuity of `S(t)` is invoked.

**L06 — horizon restriction and countable common events.** PASS. `P^n` is pathwise horizon-consistent (coefficient independent of `T`); the O2 event follows by uniqueness of `L^p` limits and countable intersection over `(R,T1,T2)`. Not obtained from equal laws.

**L07 — cut-off local data extension, no point trace.** PASS. `D_{ψ_N}` maps `H^s_loc×H^{-1/2}_loc` into global `E` (compact support), so O1 applies to `D_{ψ_N}z`; no local phase is fed into `P`, no point trace is used, and O3 does not claim the complete local flow.

**L08 — executed falsification and logical witnesses.** PASS. The `d=1` free-wave arithmetic is correct: observer `[-2,2]`, `T=9`, velocity `1_[5,6]` gives `u = 1/2` on the observer for the large cutoff and `0` for the small one, with endpoint integrals `[1/2,1/2]`; it is a guard about insufficient terminal agreement, not a refutation. `G` vs `-G` and the coordinate-projection operator-topology witness are valid and correctly scoped as abstract/logical notes.

**L09 — no tautological raw-overlap premise; satisfiability.** PASS. C1–C5 rest on the ordinary source equation and free propagation, not on the raw O1 equality. The original model supplies the retaining extension (`L:source-retaining-isometry`) and raw `W`-measurability; the zero-expectation argument is not circular.

**L10 — honest exclusions.** PASS. `not_claimed` correctly excludes the complete local Fréchet flow, point-moment equality, source-image/novelty clearance, Lean, global unmasked group, and arbitrary-weak-solution uniqueness. `P:constant-raw-average` is only a tested-average moment bound, not a point trace.

## Required fixes before production gate

1. Emit and prove a named lemma: for fixed `n`, on one probability-one event, `D_{χ_j} P^n_{R1}(t,s) D_{ψ_{N1}} = D_{χ_j} P^n_{R2}(t,s) D_{ψ_{N2}}` for all `s≤t≤T`, whenever `R1,R2,N1,N2 ≥ 2j+T+3`, both components; prove it from the ordinary potential finite propagation (`b = m_R Y_n`) with an explicit speed-one cone and the strict margin.
2. Promote the general-state paragraph inside `L:constant-source-solution` to an all-E, all-`(s,t)` ordinary Duhamel identification lemma, including initial time `s` and uniqueness on `[s,T]`.
3. State the E-restriction/compression step: `P_{R,T}` is the N→∞ uniform-triangle limit of `P^n_{R,T}` restricted to the invariant subspace `E`, so C4 holds on `B(E)`.
4. Record the cutoff-norm finiteness (no uniform `(j,N)` constant claimed) and the `W`-measurability of the O1/O2 limiting events despite the source field living on the retaining extension.
5. Document that `M_R`-horizon compatibility is not separately proved; O2 is derived through the horizon-consistent source paths and uniqueness of `L^p` limits.

## One-line summary

The conditional interface is logically sound and honest — O1/O2/O3 follow from C1–C5 without restating the raw overlap conclusion and with correct cone constants — but two central bridges (the all-state/all-`(s,t)` ordinary Duhamel identification and the ordinary potential mask/data-cutoff propagation identity) exist only inside proof bodies and must be promoted to stated lemmas before the gate can be cleared at HIGH confidence.