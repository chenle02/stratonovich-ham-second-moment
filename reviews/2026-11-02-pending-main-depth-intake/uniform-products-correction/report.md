# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

**SAME-SESSION CORRECTION AND PROPOSED-PARAGRAPH REVIEW.** This is the single authorized followup in my same reviewer session; it is not an independent re-vote, not a confidence retry, and not a global or whole-paper clearance. Original source 887, my prior report, and the 63-member capsule remain immutable; the proposed paragraph is an external author candidate only. Both concrete corrections are resolved: one is a **retraction of an error in my own prior report**, and the other is an **acceptance of a correct, clarifying proposed replacement**. The underlying seven proofs were already valid, and they remain valid under the proposed text.

## Critical findings

None in the manuscript. The only genuine mathematical error surfaced by this correction round was in **my prior report**, not in the source.

**Correction 1 (my report error).** My prior PROOF178 write-up stated the pairing bound "follows from `‖V‖_{H^{-1/2}}=‖M‖=k`". That equality is **false and is asserted nowhere in the manuscript**. The manuscript asserts only `‖L‖_{B(E)} = ‖M‖_{H^{1/2}→H^{-1/2}} = k` (current line 41–42 = proposed line 42, `\|L\|=\|M\|=:k`), and proves the pairing bound `|v_V(u,w)| ≤ k‖u‖_{H^{1/2}}‖w‖_{H^{1/2}}` **directly** from the multiplier action, since `v_V(u,w)=⟨Vu,w⟩=⟨Mu,w⟩`, never through `‖V‖`. I retract the sentence containing the invented equality; it was a report provenance slip, not a flaw in PROOF178. No source repair is needed to remove it.

**Correction 2 (source ambiguity, correctly fixed by the proposal).** The current PROOF182 line "Its norm bound is at most `K/B≤K`, so" has an ambiguous antecedent ("its") that a reader could misread as bounding the physical endpoint wave by `K/B`, which is false. The proposed replacement disambiguates three distinct objects and is **mathematically correct**. Full verification below.

## Noncritical findings

- N1 (the ambiguity being fixed): the current pronoun is the only load-bearing phrasing defect in the seven proofs; it is a clarity issue, not an error in the bounding chain — the downstream display `≤ L_{B,K}+Bλ(M̄_m)+C(θ,B,K)(e_m+e_m^ν)` is already correct in the current source. The proposal makes the justification explicit.
- N2 (benign round-ups, unchanged): `8(1+K)²(1+B) ≤ 16(1+K)⁴(1+B)³ = L_{B,K}` exponent, `C_B ≤ 18B^{3-1/r} ≤ 32B^{3-1/r}`, `C_BB^{1/r} ≥ B` — all re-verified in the proposed module.
- N3 (diagnostic regularity caveat): the hand diagnostic's `‖M_{V_R}‖≤‖V_R‖_∞≤1` is valid here because `m_R=η_R²` is a perfect square, giving `∫η_Ru·η_Rφ ≤ ‖η_Ru‖₂‖η_Rφ‖₂ ≤ ‖u‖₂‖φ‖₂`. It is not invoked as a theorem by the manuscript.

## Checked derivations

**Disposition of the norm-equality error — RETRACTED vs report; manuscript correct.**
- The manuscript's exact identities: `‖L‖_{B(E)} = ‖M‖_{H^{1/2}→H^{-1/2}}` is exact because `L(u,v)=(0,Mu)`, so `‖L(u,v)‖_E = ‖Mu‖_{H^{-1/2}}` and the supremum over `‖u‖²+‖v‖²≤1` collapses to `sup_{‖u‖≤1}‖Mu‖=‖M‖`. This survives.
- The potential recursion `M_n χ_R = V_n` gives only `‖V_n−V_j‖_{H^{-1/2}} ≤ ‖χ_R‖_{H^{1/2}}‖M_n−M_j‖` (R-dependent factor `‖χ_R‖_{H^{1/2}}`, current line 62 = proposed line 63). So `‖V‖ ≤ ‖χ_R‖_{H^{1/2}} k`, **not** `‖V‖=k`.
- Hand diagnostic replicated (valid, not assumed as a theorem): for `Γ=δ₀` in d=1 and `m_R=η(x/R)²=:v_R` one computes in the unitary convention `V̂_R(ξ)=R v̂(Rξ)`, hence
  `‖V_R‖²_{H^{-1/2}} = R∫(1+(z/R)²)^{-1/2}|v̂(z)|²dz ≥ (R/√2)∫_{|z|≤1}|v̂|² dz = cR`, `c>0` (continuity and `v̂(0)=∫v>0`). Meanwhile `‖M_{V_R}‖ ≤ 1` by the perfect-square factorization above. Thus the potential norm is unbounded in R while the multiplier norm stays bounded; the two norms are genuinely distinct objects, and my prior equation was false. **No change to PROOF178 is needed.**

**Disposition of the proposed replacement — ACCEPTED (author candidate; recommend adoption).**
- The inserted block reads: `‖M̄_m‖≤K/B≤K`, `‖H̄_m‖_θ ≤ a_m ≤ K`, then `‖S_E(B)U_{H̄_m}(B,0)‖ ≤ 8(1+K)²(1+B)e^{Bλ(M̄_m)}`, then "Consequently," followed by the unchanged logarithmic display.
- Verification of applicability: the spectral estimate (Eq. `E:uniform-E-static-bound`) requires `K ≥ max(1, ‖M̄_m‖)`. On a good full cell `a_m ≤ K` gives `‖M̄_m‖ ≤ a_m/B ≤ K/B ≤ K` (using `B≥1`), and `K≥1` holds by the standing `K≥1` guard; hence the spectral theorem applies. Correct.
- Verification of the Young base: the multiplicative Young theorem needs `‖H̄_m‖_θ ≤ K`, and `‖H̄_m‖_θ ≤ a_m ≤ K` holds. The distinction is exactly the point of the fix — the perturbation theorem uses the **primitive** norm `a_m` (bounded by K), not the instantaneous potential norm `K/B`.
- Composition: the complete good-cell bound is the product identity `P_m^mean = S_E(B)U_{H_m}(B,0)` (full cell, `ℓ_m=B`, `m<N`) with base `S_E(B)U_{H̄_m}(B,0)` and perturbation `H_m−H̄_m` of size `e_m`; the multiplicative estimate yields `log‖P_m^mean‖ ≤ log[8(1+K)²(1+B)] + Bλ(M̄_m) + C(θ,B,K)(e_m+e_m^ν)`, and `log[8(1+K)²(1+B)] ≤ L_{B,K}=log16+4log(1+K)+3log(1+B)`. The following display and all subsequent steps (prefactor sum `≤L_{B,K}/B`, good-cell λ sum `≤Rate+Λ_δ`, bad cells, last stopped cell, PROOF183, PROOF184) are unchanged and remain valid.
- Zero-potential hand test confirmed: `M̄_m = H̄_m = 0` gives baseline `S_E(B)` with `‖S_E(B)‖≥1`. At `B=2, K=1` the wrong reading "physical wave ≤ K/B = 1/2" is contradicted (`‖S_E(2)‖≥1`), whereas the proposed exponential bound gives `8(1+1)²(1+2)e^{2·0}=96 ≥ ‖S_E(2)‖` (in fact `≤G_B≤3B=6`), and `λ(0)=0`. The proposal is therefore the correct reading and works in this case.

**Full re-verification of PROOF178–184 under the proposal.** All constant/limit/hypothesis checks from my prior report are re-confirmed; only PROOF182 differs, by the 7-line insertion.
- PROOF178 (proposed lines 53–81): lift/norm equality, `V` extraction uniqueness, direct pairing bound, R-dependent F-lift used only for identification — CHECKED. (My prior explanation line retracted; the proof itself is correct.)
- PROOF179 (104–243): `c=2+K²`, `A≥2`, full `H¹` form domain, Teschl 2.14/3.6/3.1–3.2, quarter-power/negative completion, condition cost `√{3(1+K²)}≤2(1+K)`, `−K²≤β≤0`, closed-PVM spectrum, spectral wave `8(1+K)²(1+t)e^{λt}`, physical-wave identification without lift-budget transfer, rate continuity via ε-minimizer `z≤K+2` — CHECKED.
- PROOF180 (269–314): Bochner averaging contraction, compact `C_t` image uniformity (`ω_δ→0`), typed tensor commutation, `√{3+2Z}√{Ω_δ(M)}`, uniform-in-R, no tensor compactness — CHECKED.
- PROOF181 (346–388): `G_B≤3B`, `C_B` bounds, `C_BB^{1/r}≥B`, primitive exponent `1−1/r>θ`, `C_grB(1+d^ν)`, symplectic endpoint `≥1` — CHECKED.
- PROOF182 (414–482): as verified above with the accepted insertion; good/bad/last cells, `δN≤1/B` full-cell count vs `n=N+1` all-cell count, no division by `ℓ_N` — CHECKED.
- PROOF183 (497–523): `K_B=B^s`, `s>r(3+κ_ball)/(r−ν)`, both bad exponents negative, `L_{B,K_B}/B→0`, δ-first then integer-B, no diagonal, deterministic ball/`sup_R` — CHECKED.
- PROOF184 (563–614): multiplicative good cells, bad cells with mean denominator `≥1`, `c_B=2^{ν−1}C_grB`, finite power means incl. `p=ν`, ordered noncommuting submultiplicativity with `A_prod≥1`, `δ→0` then `K_res→∞` then `M_B, B→∞`, no Gaussian/Hamiltonian premise, no scalar moment multiplication — CHECKED.

## Required fixes before production gate

- **Report fix only:** my prior sentence claiming `‖V‖_{H^{-1/2}}=‖M‖=k` is hereby retracted in full; it is not a manuscript claim and requires no TeX change.
- **Source fix recommended:** adopt the proposed paragraph (proposal-binding `replaced_exact` → `replacement_exact`). It is correct, removes a genuine potential misreading in the current PROOF182, and leaves all line/constant/budget claims unchanged except the 7-line disambiguation. The proposal remains an author candidate until the root adjudicates this report; no production adoption is asserted by me.
- **No other source repair is required.** I identified no second actual defect in any of PROOF178–184 beyond the pronoun ambiguity; all E-only budgets, domains, seeds of constants, and iterated limit orders are correct.

## One-line summary

Same-session correction: my prior report's `‖V‖=‖M‖` claim is retracted (the manuscript never asserts it and it is false — the diagnostic shows `‖V_R‖_{H^{-1/2}}` unbounded in R while `‖M‖` stays bounded), the proposed PROOF182 replacement is correct and should be adopted, and all seven proofs remain PASS with no further source repair required.

---

## Uniform requirements checks (UPR01–UPR10, under the proposed paragraph)

**UPR01 — PASS.** PROOF178 closed E class, `‖L‖=‖M‖`, potential uniqueness/support via `Mχ_R=V`, direct multiplier pair bound (no `‖V‖=‖M‖` needed), full-F lift R-dependent for identification only, complexification preserves E norm and Hermitian pairing.

**UPR02 — PASS.** PROOF179 exact `c=2+K²`, `A≥2`, full-H¹ form, Teschl at correct domains, resolvent/square-root order, quarter/negative completion, `E_A` cost `≤2(1+K)`, `β≥−K²`, `β≤0` by dilated trial, real/complex infimum, closed-PVM spectrum/resolvent domains, `8(1+K)²(1+t)e^{λt}`, fixed-R lift no-budget-transfer, Young primitive identification, eps-minimizer `z≤K+2`, zero-covariance.

**UPR03 — PASS.** PROOF180 true partition/empty cell, Bochner averaging contraction/density, `ω_δ→0` uniform on compact `C_t` image, typed tensor commutation via dimension-free bound and `‖T_R‖≤M_0`, uniform-R errors, `√{3+2Z}√{Ω_δ(M)}`, finite continuous rate, no tensor compactness/global-family shortcut.

**UPR04 — PASS.** PROOF181 `G_B≤√{3+2B²}≤3B`, `C_B≤18B^{3−1/r}≤32B^{3−1/r}`, `C_BB^{1/r}≥B`, `L^r` primitive `1−1/r>θ`, `C_grB(1+d^ν)`, symplectic block baseline endpoint `≥1` with `δ^{-a/2}` direction and no uniform-direction cost, empty/zero cases.

**UPR05 — PASS.** PROOF182 with the accepted replacement: own Bochner cell average, `a_m/e_m` budgets, good cells `a_m≤K` with **instantaneous** `‖M̄_m‖≤K/B`, **primitive** `‖H̄_m‖_θ≤a_m≤K`, and **spectral endpoint** `≤8(1+K)²(1+B)e^{Bλ(M̄_m)}`; prefactor `L_{B,K}`; `δN≤1/B` vs `δn≤2/B`; nonnegative dropped rate cells; bad-tail `K` powers and `B^{3r}`; last stopped-path bound `C_grB[δ+C_B^νZ^νδ^{1−ν/r}]` without dividing short cells; fixed-parameter errors vanish uniformly in R.

**UPR06 — PASS.** PROOF183 `M_B=c_ballB^{κ_ball}`, `K_B=B^s`, `s>r(3+κ_ball)/(r−ν)`, both bad exponents strictly negative, `L_{B,K_B}/B→0`, δ-first then integer-B, no diagonal choice, deterministic finiteness/continuity/countable-dense/ordinary `sup_R` (no random compactness).

**UPR07 — PASS.** PROOF184 arbitrary little-Hölder zero-start paths, good-cell exact ratio, bad-cell mean denominator `≥1` (no perturbed-Hamiltonian claim), `c_B=2^{ν−1}C_grB`, finite power means incl. `p=ν`/zeros/empty cell, `max(1,z_rat)`, ordered noncommuting submultiplicativity with `A_prod≥1`, `δ→0` then `K_res→∞` then `M_B` and `B→∞`, deterministic `b_δ`, no scalar displacement-moment or Gaussian inference.

**UPR08 — PASS.** Input-use ledger (this session): **read and consumed** — `proposed-products.tex.txt`, `current-products.tex.txt` (verified byte-differ only by the single hunk in `proposal-binding.json`), `signed-static.tex` (physical-wave identification), `uniform-mean.tex` (`T_R`, `C_mean=M_0‖C_t‖`), `cameron-mean.tex` (compact `C_t`, block partition), `young-upper.tex` (refined growth, multiplicative perturbation), `symplectic.tex` (endpoint baseline), `teschl-2014.txt` (2.14/3.6/3.1–3.2 with `(2.63)`,`(3.18)–(3.33)`,`(3.51)–(3.53)`), `friz-hairer.txt` (Young `(4.1)–(4.3)`, Sections 1.4–1.5/4.1). **Delivered in earlier session context, not re-read this session (residual upstream limit):** the 21 remaining files (variance, operator driver, source convergence, compact Gaussian, Gaussian tubes, radius anchor, masked moments, constant-phase-young, compact mean family, exact scaling, raw block lower, unmasked variational, temporal equilibrium, spatial occupation, point transfer, signed moment upper, positive Gram, intrinsic constant, occupation ceiling, white evaluation, chen-author, crouzeix — excluding only the re-inlined prereqs). Their conclusions are trusted inputs; I do not re-derive them here, and I explicitly do not claim all-28-proof re-derivation.

**UPR09 — PASS.** Signed/zero potential, non-eigen bottom, N=1/empty/short last cell, `p=ν`, `Y=0`/`M=0`, noncommuting product, non-Hamiltonian residual, polynomial `M_B` with valid `s`, fixed-R lift constants not in uniform budgets, all limit orders; additionally the zero-potential (`M̄=0`) test now explicitly passes under the proposed paragraph. No control blocks its claim.

**UPR10 — PASS.** Seven proofs reconstructed with every hypothesis/constant/limit explicit under the proposal; original models and E-only budgets preserved; source/phase/constant interfaces not overextended (identification vs bound, no lift-norm or `χ_R`-constant transfer into uniform budgets); no concentration/independence/point-transfer/moment-asymptotic/whole-213/source-image/cold/global credit; no new Lean/kernel/formalization claim.