# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

Review basis: only the embedded `scope.md`, `assigned-proof-identities.json`, `source-bindings.json`, `packet-line-map.json`, and `packet.md` line-numbered excerpts. No `Progress.md`/`Review.md`/`HANDOFF.md`/reviews ledger, no tools, no delegation, no external paths, no image attestation. Line-number identities of PROOF001–009 were cross-checked against `assigned-proof-identities.json` (offset +2 between TeX source lines and packet lines).

---

## Critical findings

No blocking mathematical break was found in any of the nine proofs. No incorrect constant, wrong sign, false identity, unverified silent import, or circular step surfaced under manual reconstruction. The following are honestly kept as **noncritical** residuals rather than failures.

---

## Noncritical findings

1. **PROOF009 has the most condensed analytic passages.** The Bochner-integrand measurability of the constructed series in `(s,y)`, the spatial `L^2`-continuity transfer, and the d = 3 Green-width `L^2`-convergence are argued via standard vector-valued-integration facts (partition of unity, weak convergence, tightness, dominated Bochner integration), but the write-up compresses them. The core steps are sound; a production write-up should expand these.

2. **Source Theorem 3.1 general induction is outside the supplied carrier.** The bounded context contains the universal pairing theorem statement and the base cases n = 1 (source pp. 14–15) but not the full induction (intervening pages 17–21). Per scope this theorem is an imported statement whose *hypotheses* must be checked at each application, not re-proved; the hypotheses are satisfied everywhere it is used. This is a source-evidence limitation, not a proof gap in the nine proofs.

3. **PDF text extraction is flagged garbled by the manifest itself**, and no PNG images were supplied. All load-bearing applications were re-verified against the text layer alone; image credit is zero. The Theorem 3.1 statement (3.6), including the factor `2` on the `Q_1` product and the counting `#Q_2` even / `#Q_0 = #Q_1`, was legible enough to apply correctly.

4. **Remark R:source-uniformity is an internal source discrepancy, not a defect of the nine proofs.** The `(4.4)`/`(5.4)` label issue and the `C^n t^{2n}/n!` all-`t` uniformity fail (correctly) against the manual white-noise test. The repaired bound in Lemma L:crude-corrected is explicitly weaker (`e^{2θ₀t}`), consistent with the polynomial test, and recovers only the final `e^{Ct²}` scale; it does not claim sharpness.

5. **P:Jensen's `L_*` specialization remains conditional**, as stated. This is correctly scoped, not an overclaim.

---

## Checked derivations

- **PROOF001 (P:Jensen).** Verified non-circular use of forward-referenced L:vertex-crude (`q_n` summability implies `ΣE|X_n|<∞`, hence mean of the `L²`-series equals the sum of means). Verified nonnegativity of each `E S_{2n}(g_{2n})` (Green kernels/measures ≥ 0, `γ ≥ 0`), `E u ≥ 1`, Cauchy–Schwarz, and the liminf–factor‑2 transfer (valid because `log E u ≥ 0` and scaling by 2 is exact).

- **PROOF002 (P:mixed).** Verified Wick parity at fixed widths, product convergence in `L¹` from joint `L²`, the per-chain reversal to initial-root form, evenness absorption of signs in Green/covariances, the index involution `ρ`, the induced pairing bijection, nonnegativity of every mixed expectation, monotone double-sum identification, independent sum invariance, and regrouping by total order. Checked empty-chain factors equal one and the `m=n=0` case equals one.

- **PROOF003 (L:white-test).** Re-derived by hand: `∫ G(s,y)G(r,y)dy = ½min(s,r)`; the `(1,1)` integral equals `c₀ t^{3-α₀}`; the `(0,2)` integral equals `½c₀t^{3-α₀}`; total-order‑two contribution is `2c₀t^{3-α₀}`. Confirmed the contradiction with source (5.4) uniformity.

- **PROOF004 (L:damped-homogeneous-norms).** Verified `N₀=θ⁻²`, the spectral-annulus scaling `μ(B_r)=r^αV`, `I(a)=αV a^{α-2}∫u^{α-1}(1+u²)⁻¹du`, `N₁(θ)=θ^{α+α₀-2}N₁(1)`, `N₂(θ)²=θ^{-β}N₂(1)²`, nonnegativity of the time quadratic form, tail decay of `N₁^{(M)},N₂^{(M)}`, and the smoothing/truncation-monotonicity claims. The key conditions `0<α<2`, `α₀>0`, `α₀+α<2` match each finiteness/summability checkpoint.

- **PROOF005 (L:spatial-wick-measures).** Verified the Laplace representation, width-monotonicity of the transform (explicitly distinguished from pointwise covariance monotonicity), the heat bound `(p_t*γ_b)(x)≤A t^{-α/2}`, the Brownian moment bound with Dirichlet normalization `T^{(2-α/2)j}/Γ((2-α/2)j+1)` (re-checked for j=1 and general j), the uniform mass bound `2^{-2k-2}(∫e^{-a/2}M_k(a)da)²`, the Laplace/weak-cluster uniqueness argument, zero mass on `y_l=0` faces (mass at `r=∞`), zero mass on `r_l=0` faces (via `λ_l→∞`), and the homogeneity exponent `(4-α)k`.

- **PROOF006 (L:joint-fixed-order).** Verified the finite-horizon spatial limits, the differences-of-products telescoping to a single marked edge with `K_{1/η}`, the exact Theorem 3.1 hypothesis fit (finite Gaussian-weighted spectral measures, Laplace-interval temporal domains, d = 3 Green smoothing and domain caps), the marked-edge contribution `N₁^{(1/η)}(1)` or `N₂^{(1/η)}(1)²`, the `e^{T₁+T₂}` loss, the η-monotonic bracketing for arbitrary relative rates, and the `Q+Q-2Q` Cauchy argument for uniqueness of the `L²` limits.

- **PROOF007 (L:crude-corrected).** Verified `#Q₀=#Q₁` and `#Q₀+#Q₂/2=n`, the per-pairing `e^{2θt}C^nθ^{-2n}` envelope, `θ=θ₀+n/t`, `P_n n^{-2n}≤2^n/n!`, the ratio-test summability, and the final Cauchy–Schwarz `2e^{2θ₀t+2Ct²}`. Checked that the finite-spectral-measure regularization and the two-limit transfer to the unsmoothed covariance are monotone and uniform.

- **PROOF008 (L:vertex-crude).** Verified edge covariance `γ⁰_{δ∨δ}(·)γ_{ε+ε}(·)`, per-edge reversal and evenness, per-edge finite spectral measures/temporal truncations, width-uniform norm bounds with the factor `2C₀` handled by `D=max{1,2C₀}`, `C₁=D²`, and the norm ratio `√(n+2)q_{n+1}/(√(n+1)q_n)→0`.

- **PROOF009 (P:mild-construction).** Verified the Hermite creation/annihilation multiplication bound `2√(n+1)` (weights `a₁` and `a₁+1`), degree/measurability closure, spatial `L²` continuity via joint stationarity, fixed-external-width Bochner domination, the terminal-kernel Fubini identity `I_{n,a}=lim_b Y_n^{(b,a)}`, the independent width-uniform bound `sup_a ‖I_{n,a}‖≤q_n(t)` (from vertex-crude, not from the `V_a`-dependent domination), Green-before-noise ordering (no interchange of the source limits), external-width joint convergence, sum/product interchange, and the final `a↓0` then `N→∞` double-limit. Confirmed no uniqueness claim.

---

## CON01–CON11 checks

- **CON01 — PROOF001 P:Jensen — PASS**; proof-level: **CHECKED**. Summability of the nonnegative-mean series is non-circular; squared-mean inequality and liminf guards verified; `L_*` specialization is explicitly conditional.

- **CON02 — PROOF002 P:mixed — PASS**; proof-level: **CHECKED**. Unequal/empty/self/cross chains, separate roots, reversal bijection, `L²`-to-`L¹` product limit, nonnegative finite expansions, enumeration-independent infinite sum all verified.

- **CON03 — PROOF003 L:white-test — PASS**; proof-level: **CHECKED**. Order-one calculation reproduced by hand with exact `c₀`; source (5.4) all-time uniformity falsified correctly; no numerical experiment involved.

- **CON04 — PROOF004 L:damped-homogeneous-norms — PASS**; proof-level: **CHECKED**. All `N₀/N₁/N₂` finiteness/scalings, alpha₀+α<2, tail positivity, zero behavior, Fourier/Laplace exchanges, smoothing domination and temporal tails verified.

- **CON05 — PROOF005 L:spatial-wick-measures — PASS**; proof-level: **CHECKED**. Finite heat-weighted edge measures, nonnegative covariance, positive Laplace representation, uniform mass, tightness/uniqueness/weak limits, non-atomic horizon boundaries, full Green-measure cases verified; no transform-to-pointwise monotonicity error.

- **CON06 — PROOF006 L:joint-fixed-order — PASS**; proof-level: **CHECKED**. Theorem 3.1 hypotheses fit exactly for independently smoothed finite edge measures and restricted Laplace domains; squared `N₂` marked-edge bound, Green-first removal, arbitrary width ratios, and coupled `L²` Cauchy existence verified.

- **CON07 — PROOF007 L:crude-corrected — PASS**; proof-level: **CHECKED**. Pairing-count constants, θ choice, all-time corrected quadratic bound, and non-reliance on source (5.3)–(5.4) uniformity verified.

- **CON08 — PROOF008 L:vertex-crude — PASS**; proof-level: **CHECKED**. Arbitrary vertex smoothing, same universal inequality, finite constants, `q_n` bound and fixed-time weighted summability verified without importing unproved all-time uniformity.

- **CON09 — PROOF009 P:mild-construction — PASS**; proof-level: **CHECKED**. Gaussian polynomial degree/multiplication closure, measurability and spatial `L²` continuity, fixed external smoothing Bochner integral, inner-then-external limits with arbitrary ratios, d = 3 Green before noise, sum/product interchange and onefold mild integral for the same canonical series verified. Residual compactness is notation-level only (see Noncritical #1). No extra uniqueness claim present.

- **CON10 — Source/application and small-order falsification — PASS**. Author-version Theorem 3.1 hypotheses and the source’s pairing/regularization conventions are met at every application; smallest unequal/empty/self-pair cases and the d = 1 white case were tested manually. Extraction ambiguity disclosed (Theorem 3.1 full induction not in carrier; PDF text garbled; no images). No load-bearing hypothesis is missing or violated.

- **CON11 — Combined non-circularity/completeness — PASS**. Logical order among the nine proofs is acyclic (004 → 005 → 006 → 007/008; 001/002/009 consume only these plus Theorem 3.1 and Hypothesis H:homog; no reverse dependency). Fixed-time moment construction is kept separate from later correct-scale asymptotics; the t^κ variational claims in the abstract are not premises of these nine proofs. Scope/zero-law/calibration boundaries are preserved.

---

## Required fixes before production gate

None are strictly blocking (hence PASS_WITH_NOTES, not FAIL). Recommended before gate:

1. **PROOF009**: spell out the vector-valued Bochner measurability, the partition-of-unity/tightness approximation for the d = 3 Green-width limit, and the continuous-representative selection; these are currently compact.
2. **PROOF005/PROOF006**: state the marked-edge constant `C_{k,T₁,T₂}` explicitly (its `k` dependence and the `e^{T₁+T₂}` factor) so residuals are actionable.
3. **Source custody**: record in the manuscript that Theorem 3.1’s general induction proof is imported and its hypotheses, not its proof, are re-verified; note the parity between the two applied versions (`Q₁` factor 2).
4. **P:Jensen**: keep (as now) the explicit statement that the `L_*` numerical consequence presupposes the intended first-moment lower bound.

---

## One-line summary

The nine foundational proofs reconstruct cleanly with correct constants, signs, limit orders, and non-circular dependencies; only non-blocking presentational compression in PROOF009 and a source-evidence limitation (no images; Theorem 3.1 induction outside carrier) prevent attestation at HIGH.