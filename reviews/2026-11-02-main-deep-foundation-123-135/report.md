# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

1. **Transitive premise gap (production gate, not internal to the four derivations).** PROOF001 and PROOF002 rely on the forward interface lemmas `L:vertex-crude`, `L:crude-corrected`, and `L:joint-fixed-order`, which import the author-version **Theorem 3.1, (3.6)** as a black-box universal pairing bound. The held `author-case2-test-context.md` documents that the printed proof of Theorem 3.1, **Case 2 (page 21)**, writes the cross-pairing temporal argument after the substitution as `s−r` and thereby drops the differing prior-time origin `(B−A)`. The notes do **not** internalize the offered repair (stationary covariance inner product + Cauchy–Schwarz on the two self-norms, each translation-invariant). The four target proof bodies are correct *given* their stated premises, but the summability/diagram-limit premise chain is not fully closed inside the notes until this is adjudicated. This is a real dependency risk and must be resolved before production certification; it does not by itself falsify PROOF001–003/135.

2. **No false Jensen/numerical overclaim found.** The P:Jensen corollary correctly keeps the `ℓ = L_*` implication conditional on the intended first-moment lower bound, and does not adopt the printed `L_*` normalization as unconditional; this respects the honesty role.

## Noncritical findings

- The abstract sentence “The component proofs have passed scoped independent reviews” is historical prose, not a mathematical premise; this review does not rely on it.
- PROOF001 and PROOF002 are forward-referenced to `L:vertex-crude`/`L:joint-fixed-order`. The dependency is acyclic (those lemmas do not use P:Jensen or P:mixed), and the complete constructor bodies are supplied, so this is acceptable, but it should be recorded as a heavy interface dependence.
- PROOF135’s measurability/completion argument is compressed but valid: it uses Borel-null supersets of Lebesgue-null sets and the `ν`-completion, and does not write any unjustified `0·∞`.
- P:Jensen proves `Eu ≥ 1` in the mean sense only (sum of nonnegative even pairing integrals); it correctly does **not** assert pathwise or arbitrary-phase-coefficient positivity.
- The white-noise remark refutes only the *all-time/order uniformity* of source (5.4) at `n = 1`; it explicitly preserves the final `e^{Ct²}` conclusion. See Checked derivations.
- Text-only review: arithmetic is verified against the embedded TeX/held text, not rendered raster. Extraction garbling of exponents/fractions in the PDF text layer is disclosed; no image credit is claimed here.

## Checked derivations

**PROOF001 (P:Jensen, 379–392).**
`L:vertex-crude` gives `Σ_n ‖X_n‖₂ < ∞`, hence `Σ_n E|X_n| ≤ Σ_n ‖X_n‖₂ < ∞`, so `E u = Σ E X_n`. Odd terms vanish by (2.20); each even term is `Σ_{D∈Π_n} ∫ g_{2n}∏|s_j−s_k|^{−α₀}γ(x_j−x_k)` with nonnegative `G ≥ 0`, `γ ≥ 0`, so each term ≥ 0; `S₀ = 1 ⇒ Eu ≥ 1`. Cauchy–Schwarz `Eu² ≥ (Eu)²`; `t^{−κ} log Eu² ≥ 2t^{−κ} log Eu`; lower limits give `liminf ≥ 2ℓ`. `ℓ = L_*` kept conditional. All steps verified. **(0,1) parity, mean≥1, and scaling are correct; no pathwise claim is made.**

**PROOF002 (P:mixed, 453–509).**
Wick’s formula at positive widths: zero at odd `m+n`, finite sum over all pair partitions of `{1..m}∪{m+1..m+n}` at even total order, including self, cross, unequal, and empty chains; `m=n=0` gives 1. The two-chain form has independent roots `(0,0)`. Chain reversal
`(s'_j,y'_j)=(t−s_{m+1−j},x−y_{m+1−j})`,
`(s'_{m+j},y'_{m+j})=(t−s_{n+1−j},x−y_{n+1−j})`
sends `G(t−s_m,x−y_m)→G(s'_1,y'_1)` and each further factor into the corresponding successive increment; spatial differences flip sign and evenness absorbs it; Jacobians `±1`; `ρ(j)=m+1−j`, `ρ(m+j)=m+n+1−j` induces a bijection on pairings with **no factorial**. Joint `L²` convergence of both factors gives the displayed `L¹` product convergence (bounded by `(‖Y_m−X_m‖₂‖Y_n‖₂+‖X_m‖₂‖Y_n−X_n‖₂)`), not independence. Each individual diagram has its finite nonnegative limit from `L:joint-fixed-order`. Then `U_N = Σ_{n≤N} X_n → u` in `L²` (independently from `L:vertex-crude`/`P:mild-construction`, which do not use P:mixed), and
`|E U_N²−E u²| ≤ ‖U_N−u‖₂(‖U_N‖₂+‖u‖₂) → 0`.
Each mixed expectation is nonnegative, so the rectangular partial sums increase (not samplewise). Nonnegativity makes the limit enumeration-independent; regrouping by total order `(m+n)/2` with `0 ≤ m ≤ 2k` gives `E:full-second`, including 0/empty terms and no extra multinomial/factorials. Verified.

**PROOF003 (L:white-test, 524–538).**
`d=α=1`, `γ=δ₀`. `G(s,y)=½1_{|y|<s}`; so `∫ G(s,y)G(r,y)dy = ¼·2min(s,r) = min(s,r)/2`. The `(1,1)` integral over the square, splitting the two time-order regions, equals
`∫_0^t ds∫_0^s r(s−r)^{−α₀}dr`
(since `2·∫_{r<s}(r/2)(s−r)^{−α₀} = ∫_{r<s} r(s−r)^{−α₀}`), whose value is
`t^{3−α₀}/[(1−α₀)(2−α₀)(3−α₀)] = c₀ t^{3−α₀}`,
via the inner Beta integral `∫_0^s r(s−r)^{−α₀}dr = s^{2−α₀}/[(1−α₀)(2−α₀)]` and the outer power integral. The `(0,2)` term: `δ₀` sets the two spatial vertices equal; the first Green factor has mass `r` and `G_{s−r}(0)=1/2`, giving half the `(1,1)` value `½c₀ t^{3−α₀}`; `(2,0)` is identical. Sum of the three order-two splits
`(0,2)+(1,1)+(2,0) = ½c₀ + c₀ + ½c₀ = 2c₀ t^{3−α₀}`. No spectral `2π` factor, no amplitude error. Since `1−α₀>0`, `E X₁² = c₀ t^{3−α₀}` cannot be dominated by `C t²` uniformly in `t`, so source (5.4)’s claimed `(n,t)`-uniformity fails at `n=1`; the remark does **not** refute `Eu² ≤ e^{Ct²}` and makes no silent source correction. Verified.

**PROOF135 (L:spatial-physical-pair, 25–37).**
`ν = dx ⊗ Γ(dy)` is sigma-finite (Lebesgue sigma-finite; `Γ` locally finite, hence sigma-finite on exhausting balls). For a Borel Lebesgue-null `N`, integrate **first in x**:
`ν{x∈N} = ∫[∫1_N(x)dx]Γ(dy)=∫0·Γ(dy)=0`,
`ν{x−y∈N} = ∫[∫1_N(x−y)dx]Γ(dy)=∫0·Γ(dy)=0`
(each translate of `N` is Lebesgue-null). This holds for atoms or infinite total mass of `Γ` because Tonelli applies to sigma-finite products of nonnegative integrands; **no** `Γ ≪ Leb` and **no** `∞·0` appear. An arbitrary null set has a Borel-null superset, which makes arbitrary Lebesgue versions measurable in the `ν`-completion with unchanged nonnegative extended value; the same applies to the exceptional sets of a.e. convergence, so Lebesgue-a.e. convergence transfers at both positions `x` and `x−y`. The reversed inner-`Γ`-integral inference is correctly avoided: for `Γ=δ₀`, `N={0}`, `x=0`, one has `∫1_N(x−y)Γ(dy)=1_N(0)=1`, yet the full product-measure set `{(x,y): x∈N or x−y∈N}` has `ν`-measure zero precisely because `x` is integrated first. Signed pairings deferred until after absolute convergence. Verified.

## FND01–FND12 determinations

[held back until the source author has been told]

## Proof ledger

| Target | Status | Checked steps | Residual gaps |
|---|---|---|---|
| PROOF001 | FULLY_CHECKED | Summability ⇒ mean interchange; odd vanish/even nonnegative; `Eu≥1`; `Eu²≥(Eu)²`; `2·liminf`; `L_*` conditionalized. | Relies on `L:vertex-crude` (imports source Thm 3.1); Case2 shift disclosed, not internalized. |
| PROOF002 | FULLY_CHECKED | Full parity/Wick diagram set; reversal + `ρ` closure; finite diagram limits; `U_N→u` in `L²`; `EU_N²→Eu²`; monotone rectangle sums; regroup by total order; no factorial. | Same Thm 3.1 dependence via `L:joint-fixed-order`/`L:crude-corrected`/`L:vertex-crude`. |
| PROOF003 | FULLY_CHECKED | `(1,1)=c₀t^{3−α₀}`; `(0,2)/(2,0)=½c₀`; total order two `2c₀`; `(5.4)` n=1 uniformity refuted only; `e^{Ct²}` retained. | None internal. |
| PROOF135 | FULLY_CHECKED | Sigma-finite product; x-first Tonelli for both null sets; Borel-null supersets; completion measurability; representative independence; a.e. transfer at `x` and `x−y`; `δ₀` counterexample rejects reversed inference. | None internal. |

## Required fixes before production gate

- **Adjudicate and internalize the imported Theorem 3.1 Case-2 repair** (stationary space–time covariance inner product with Cauchy–Schwarz against the two translation-invariant self-norms, per the held author note) or otherwise certify the `(3.6)` bound before the summability/diagram-limit chain feeding PROOF001–002 is treated as production-closed.
- **Confirm rendered-page/image coverage** for the cited source pinpoints `(2.20)–(2.21)`, `Theorem 3.1 (3.6) pp.14–15`, and `Theorem 4.1 (4.3) p.22`; this text-only review certifies the embedded TeX/held text arithmetic, not raster source fidelity.
- **Preserve the conditional `L_*` label** in every downstream numerical consequence of P:Jensen (currently correct in the source); do not promote it to an unconditional constant.

## One-line summary

All four targeted proofs are internally correct with hand-verified constants (`c₀ t^{3−α₀}`, order-two total `2c₀`, and the x-first Tonelli null transfer with its `δ₀/N={0}` reversed-inference counterexample); the sole production-gate item is the disclosed but uninternalized Case-2 time-offset step of the imported Theorem 3.1 on which the summability interface depends.