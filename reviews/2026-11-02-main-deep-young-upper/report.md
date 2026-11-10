# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I found no false identity, no sign error, no incorrect end-product constant, and no hidden hypothesis in either deterministic proof. The end-point prefactor requirement at `x=0` (no extra factor) is exactly met, the left noncommuting order is correct with exact `U·R = I` cancellation, and the partition-remainder control uses the genuine `2θ−1 > 0` Young exponent. The stochastic conclusions (Gaussian exponential estimates, conditional head/residual independence, Cameron identity, original moment upper bound) are correctly *not* claimed by either proof; those remain properly outside this unit.

Evidence limitation (recorded per instructions): I did not read `packet.md` from disk and did not consult any external file; I audited only the verbatim target excerpt embedded in this prompt (packet lines 1–112, i.e. `young-upper.tex` original LF 1–110) plus the embedded `friz-hairer.txt` pages for (4.1)–(4.3) and the embedded `young.tex` section supplying `P:constant-young-linear` and `E:constant-young-local`. The proofs are complete for adjudication on that basis.

## Noncritical findings

1. **Implicit final constant in the growth lemma.** The small-`d` case yields the sharper linear exponent `log sup‖U_D‖ ≤ 2c_θ B^θ d`, while the large-`d` case yields a `C_{θ,B} d^ν` term. The two are correct individually and are dominated by a single `c_{θ,B}(d+d^ν)`, but the proof never writes down the unifying constant. Cosmetic, not incorrect.

2. **`L′_{θ,B,K}` and `C_{θ,B,K}` are existence-level.** The `‖Z‖_θ ≤ L′x` bound and the folding into `exp{C(x+x^ν)}` are argued but the constants are not quantified. This is legitimate since the proposition only asserts existence of ballot-uniform constants.

3. **Terse combination of the cross term.** The display `P_{s,t} = H_{s,t}P(s) + U(s)R(s)X_{s,t}U(s)V(s) + O(|t−s|^{2θ})` suppresses the expansion `P_{s,t} = U_{s,t}V_s + U_sV_{s,t} + U_{s,t}V_{s,t}` and the observation that `U_{s,t}V_{s,t} = O(|t−s|^{2θ})`. The step is correct (reconstructed fully below).

4. **Inverse Hölder bound is not written with the near/far case split.** The proof derives `[U_H^{-1}]_θ ≤ ‖U_H^{-1}‖_∞² [U_H]_θ` from the exact inverse-difference formula, which is valid. The near/far split is explicitly written only for `U_H`; for `U_H^{-1}` it is redundant, so this is a presentation asymmetry, not a gap.

## Checked derivations

**Local scaled contraction (both proofs depend on it).** From the Young estimate `E:constant-young-estimate`, on `[a,a+ℓ]`: `sup‖I_D(V)‖ ≤ [D]_θ ℓ^θ sup‖V‖ + C_θ[D]_θ ℓ^{2θ}[V]_θ` and `[I_D(V)]_θ ≤ [D]_θ sup‖V‖ + C_θ[D]_θ ℓ^θ[V]_θ`. Adding `ℓ^θ` of the second to the first gives `N_ℓ(I_D V) ≤ 2[D]_θ ℓ^θ sup‖V‖ + 2C_θ[D]_θ ℓ^{2θ}[V]_θ ≤ c_θ[D]_θ ℓ^θ (sup‖V‖ + ℓ^θ[V]_θ)` with `c_θ = 2 max(1,C_θ)`. Correct, because `ℓ^{2θ} = ℓ^θ·ℓ^θ` absorbs the second term. `N_ℓ` is complete on the affine path space with pinned left value, so Banach fixed point applies at ratio ≤ 1/4.

**Growth, small-d case (`c_θ d B^θ ≤ 1/4`).** Whole-interval contraction at ratio ≤ 1/4 gives `N_B(U_D) ≤ (1−c_θ dB^θ)^{-1}·N_B(I) = (1−c_θ dB^θ)^{-1}`, hence `log sup‖U_D‖ ≤ −log(1−x) ≤ 2x = 2c_θ B^θ d` for `x ≤ 1/4`. The claimed `−log(1−x) ≤ 2x` holds on `[0,1/4]`; at `d=0`, `U_D = I` and both sides are exactly `e^0 = 1` (no prefactor).

**Growth, large-d case (`c_θ d B^θ > 1/4`).** With `n_D = ⌈B(4c_θ d)^ν⌉` and `ℓ = B/n_D ≤ (4c_θ d)^{-ν}`, one gets `c_θ d ℓ^θ ≤ 1/4`. Since `c_θ dB^θ > 1/4` forces `B(4c_θ d)^ν > 1` (raise `4c_θ dB^θ > 1` to power `1/θ = ν`), the ceiling is ≤ 2× its argument: `n_D ≤ 2B(4c_θ d)^ν`. Each local factor has `N_ℓ ≤ 4/3`, so `sup‖U_D‖ ≤ (4/3)^{n_D}` and `log sup ≤ C_{θ,B} d^ν`. Both cases are dominated by `exp{c_{θ,B}(d+d^ν)}`.

**Inverse control (`‖H‖_θ ≤ K`).** One uniform partition `c_θ K ℓ^θ ≤ 1/4` serves the whole ball. Each local `Q = U_H(·,a)` satisfies `N_ℓ(Q) ≤ (4/3)‖I‖ = 4/3` and `N_ℓ(Q−I) ≤ (1/4)N_ℓ(Q) ≤ 1/3`, so the Neumann series gives `‖Q^{-1}‖ ≤ 3/2`. Composition gives uniform global sups `(4/3)^n`, `(3/2)^n`. Hölder: same-piece increments `‖U_H(t,0)−U_H(s,0)‖ = ‖(U_H(t,s)−I)U_H(s,0)‖ ≤ ℓ^{−θ}(4/3)sup‖U_H‖·|t−s|^θ`; crossing pairs split at the boundary into two pieces and `h_1^θ + h_2^θ ≤ 2^{1−θ}(h_1+h_2)^θ = 2^{1−θ}|t−s|^θ`; far pairs use `2sup‖U_H‖/ℓ^θ`. Inverse seminorm via `U_H^{-1}(t)−U_H^{-1}(s) = −U_H^{-1}(t)(U_H(t)−U_H(s))U_H^{-1}(s)` — verified by expansion: `−[U^{-1}(t)U(t)−U^{-1}(t)U(s)]U^{-1}(s) = −U^{-1}(s)+U^{-1}(t)`. Correct sign and order.

**Multiplicative proof.** `G(s)Z = R(s)ZU(s)` with `R = U^{-1}`: `‖G‖_{C^θ} ≤ (3/2)^n·(4/3)^n`-scale from Lemma growth, uniformly on the ball; hence the Young integral `Z = ∫ R dX U` exists with `‖Z‖_θ ≤ L′_{θ,B,K} x` (linear in `x`) and `Z_{s,t} = R(s)X_{s,t}U(s) + O(|t−s|^{2θ})` by (4.3). Write `V = U_Z`; then `V_{s,t} = Z_{s,t}V(s) + O(|t−s|^{2θ})` and `U_{s,t} = H_{s,t}U(s) + O(|t−s|^{2θ})`. Expanding `P = UV`:
`P_{s,t} = U_{s,t}V_s + U_sV_{s,t} + U_{s,t}V_{s,t}`. The cross term is `O(|t−s|^{2θ})`. Substitution gives
`P_{s,t} = H_{s,t}P_s + U_sR_sX_{s,t}U_sV_s + O(|t−s|^{2θ})`, and `U_sR_s = I` exactly (no Neumann approximation, since `R = U^{-1}`), so the middle term equals `X_{s,t}P_s`, yielding `P_{s,t} = (H+X)_{s,t}P_s + O(|t−s|^{2θ})`. The remainder sum over a partition is `≤ C Σ|t−s|^{2θ} ≤ C·B·mesh^{2θ−1} → 0`, so left Riemann sums of `P` coincide with the Young integral of `d(H+X)P`; uniqueness from `P:constant-young-linear` gives `U_{H+X} = U_H U_Z`. Multiplying by `A` and using submultiplicativity gives `‖AU_{H+X}(t)‖ ≤ ‖AU_H(t)‖·exp{c_{θ,B}(‖Z‖_θ+‖Z‖_θ^ν)} ≤ ‖AU_H(t)‖·exp{C_{θ,B,K}(x+x^ν)}`, retaining the actual `‖AU_H(t)‖` factor. At `x=0`, `X=0`, `Z=0`, `V=I`, `U_{H+X}=U_H`, so the bound is the exact identity `‖AU_H(t)‖` with no extra factor; no bound on `A` is used.

**YUP checks.**

- **YUP01 — PASS.** Scaled complete-norm contraction, small-`d` whole-interval bound and `−log(1−x) ≤ 2x` at `x ≤ 1/4 = c_θ dB^θ`; large-`d` ceiling `n_D ≤ 2B(4c_θ d)^ν` and `d^ν` growth; uniform partition on the `K`-ball, local Neumann `3/2`, local `4/3` and `‖Q−I‖ ≤ 1/3`, product/global sups, crossing-boundary split with `2^{1−θ}`, far pairs with `2sup/ℓ^θ`, exact inverse-difference formula, dimension-free constants. All reconstructed and correct.
- **YUP02 — PASS.** `G(s)Z = R(s)ZU(s)` is a uniform `C^θ` bounded-linear-map path; existence and linear-in-`x` bound `‖Z‖_θ ≤ L′x`; both `2θ` remainders and the cross term carry the correct LEFT noncommuting order; exact `UR = I` cancellation; `mesh^{2θ−1}` remainder summation; Young uniqueness; product identity `U_{H+X} = U_H U_Z` without smooth-density shortcut; refined growth provides the actual `AU_H` prefactor for singular/zero `A` with `x=0` giving no extra factor. All verified by hand.
- **YUP03 — PASS.** Friz–Hairer (4.1)–(4.3) assumptions (α+β = 2θ > 1, multiplication norm 1) match; the linear Young input `P:constant-young-linear` supplies existence/uniqueness/composition/invertibility; consumer calls in `products-context.tex` (base bound `K`, left multiplier `S_E(B)` as `A`) and the tube growth reduction `d ≤ 1+d^ν`, `(1+d)^ν ≤ 2^{ν−1}(1+d^ν)` are consistent with the target statements. No Gaussian/concentration/conditional-independence/iterated-limit or radius-uniformity conclusion is asserted in 149–150; anything of that kind in consumers is outside this unit.
- **YUP04 — PASS.** Scalar small/large/zero driver cases covered; the multiplicative identity is established in full noncommuting operator generality (no commutativity assumption appears anywhere); A=0 / noninvertible A and the `x=0` no-extra-factor endpoint are explicit; constants depend only on `θ, B` (and `K` for the inverse / `θ,B,K` for the product). No same-`W` head/residual independence or full stochastic bound is inferred.
- **YUP05 — PASS.** Both proofs are self-contained apart from the supplied Young inputs, use no hidden regularity/density/Hilbert hypothesis, and mark their dependence boundaries. All steps I identified as load-bearing were checked by hand; none remain INCONCLUSIVE.

## Required fixes before production gate

None blocking. Recommended clarifications (non-blocking):
- Make the unified constant `c_{θ,B}` in `E:young-upper-refined-growth` explicit (e.g. `max(2c_θB^θ, 2B(4c_θ)^ν log(4/3), 1)`), so the two cases visibly land in the single displayed form.
- Quantify (or at least state the dependence of) `L′_{θ,B,K}` and `C_{θ,B,K}` in the multiplicative proof.
- Optionally spell out the `P_{s,t} = U_{s,t}V_s + U_sV_{s,t} + U_{s,t}V_{s,t}` expansion and the `Z`-remainder substitution one line before the displayed identity, since that is the only place the "cross term of order 2θ" is asserted without its expansion.

## One-line summary

Both deterministic Banach Young proofs (refined `d+d^ν` growth and uniform `C^θ` inverse control; multiplicative upper perturbation with exact left-order `U_{H+X}=U_HU_Z`, linear-in-`x` `Z`, correct `2θ` remainders, `UR=I` cancellation, and exact `AU_H` prefactor with no extra factor at `x=0`) are mathematically correct and free of overclaimed stochastic content; the only findings are presentation-level (implicit unifying constants and terse substitution steps), so this unit passes with notes.