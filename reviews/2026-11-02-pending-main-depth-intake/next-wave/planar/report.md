# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

None found among PROOF024–PROOF029. No sign error, false identity, wrong boundary factor, or invalid large-time exponent was located in the six audited proofs. The affine interpolation identities, the closing constants (`πV/2`, `S/4`), the temporal `Z_b`, the pairing/split counts, and the final `exp(q z^{1/q})` series identification all check.

The two substantive limitations are (i) imported-theorem premises and (ii) source-rendering ambiguity, recorded below as noncritical because they do not break the six deductions themselves.

## Noncritical findings

1. **Imported source-theorem bodies are unread.** The delivered excerpt contains the *statements* of Chen–Hu (5.1) p.2173, (5.15) p.2180, Theorem 3.8(i) p.2165, and Chen2023 Theorem 1.1 pp.2, but not their proofs. I matched hypotheses/roles (Dalang, generalized covariance, `γ≥0`, homogeneity, `p=2`), and only the *finite* upper coefficient rate is actually used, so this is robust; it remains unperformed evidence rather than a mathematical gap.

2. **PDF text-layer garble.** The carriers prominently warn that PDF text extraction garbles fractions/exponents, and no rendered images were delivered. The exact numerical normalization inside Chen–Hu (5.15) was not letter-verified; again only its *finiteness* is used, so the deduction is insensitive to the garbling.

3. **Mild citation-mapping looseness.** PROOF024/027 write “product rule and Wick expectation formula in (2.17) and (2.19)”; in the held pages (2.17) is the even-order Wick expectation and (2.19) is the product rule. Both displays exist on pp.2151–2152, so the import is valid, but the label pairing is slightly sloppy.

4. **PROOF024/027 constants are not evaluated.** `C_st` is only required finite; no sharp constant is derived or claimed. This is correct scope discipline, not a defect.

## Checked derivations

**Admissible tuple check (PLN10).** `α=5/4, α0=1/4, ϑ=1/2, χ=3/2, b0=1/2`.
- Parameter range: `α0<ϑ<2−α` → `0.25<0.5<0.75` ✓; `b0=α0/ϑ=0.5<1` ✓; `χ=(α−ϑ)/(1−ϑ)=1.5∈(1,2)` ✓.
- Affine identities:
  - `2ϑ+(1−ϑ)(3−χ) = 1+0.75 = 1.75 = 3−α` ✓.
  - `ϑ(3−b0)+(1−ϑ)(4−χ) = 1.25+1.25 = 2.5 = 4−α−α0` ✓.
- `q=3−α=1.75>1`, `β=4−α−α0=2.5`, `κ=β/q=10/7` ✓.

**Counting/split/Pairing counts.**
- `P_k = (2k)!/(2^k k!)` (recurrence `P_k=(2k−1)P_{k−1}`): `P_1=1`, `P_2=3`, `P_3=15` ✓.
- `∑_{m=0}^{2k} 1/(m!(2k−m)!) = 2^{2k}/(2k)!` ✓; multiplying by `P_k` gives `2^k/k!` for the temporal pairing-sum after partition, i.e. the factor in `E:d1-time-symmetry` and the planar analogue ✓.
- `Z_b = 2/((1−b)(2−b))`; for `b=1/2`, `Z=8/3`, matching `∫∫_{[0,t]²}|s−r|^{-1/2} = (8/3)t^{3/2}` ✓.

**PROOF024 (static coefficient input).** Degree `1<χ<2<d` satisfies Dalang `χ<2` for the static source; `(2.17)/(2.19)` plus Theorem 3.8(i) give well-defined nonnegative `B_k`; homogeneity `(5.1)` gives `B_k(t)=t^{(4−χ)k}B_k(1)`; `(5.15)` for `p=2` gives `limsup_k (1/k)log((k!)^{3−χ}B_k(1))<∞`; finite-order enlargement produces finite `C_st`. Verified.

**PROOF025 (Riesz interpolation).** Closure multiplication for `α=1` is `πV_1/2` per `L:alpha-one-convolution`; descending integration gives spatial `(πV_1)^k t^k/k^k`; temporal sum gives `2^k(Z_{b0}t^{2−b0})^k/k!`; product gives `C_low=2Z_{b0}πV_1`, `t^{(3−b0)k}/(k!k^k)≤…/(k!)^2`. Hőlder on the common measure (before limits), `Q_δ≤T_{b0}^ϑ` (raw domination, no temporal-kernel interpolation), `H_α≤H_1^ϑ H_χ^{1−ϑ}` (pointwise Riesz identity then Gaussian Hölder), affine identities → `A_k ≤ C^k t^{(4−α−α0)k}/(k!)^{3−α}`, `C=C_low^ϑ C_st^{1−ϑ}`. Series `Σz^k/(k!)^q≤e^{qz^{1/q}}`, `q=3−α`, exponent `β/q=κ`. Verified. The Green-width/noise-width limit order and product-`L¹` passage are spelled out and do not use monotonicity in widths.

**PROOF026 (planar endpoints).** `Γ({0})=0`; polar disintegration `Γ = r^{1−α}dr σ(dω)`, `S=σ(S¹)` finite positive; endpoints `Γ_low=dr σ(dω)` (degree 1) and `Γ_st=r^{1−χ}dr σ(dω)` (degree 2−χ). Positive definiteness is proved by the full-sphere line mixture `(1/2)∫∫f(rω)drσ` with Radon/Fourier-slice positivity, and by the Gaussian mixture `|x|^{-λ}` for `Γ_st` (no fractional covariance power). Convolution `G_h*Γ_low ≤ S/4` from the line integral `∫G_h(z−rω)dr = 1/2·1_{|z·ω^⊥|<h}`, then `(1/2)·(1/2)σ ≤ S/4`; Gaussian mass-one averaging preserves it. Hölder exponent identity `ϑ(α−1)+(1−ϑ)(α−χ)=0` verified. Signs: convolution uses evenness; `cos` vs `e^{iξ}` factor-free. Verified.

**PROOF027 (planar static input).** Fourier homogeneity `μ_Ξ(rA)=r^χμ_Ξ(A)`; dyadic Dalang sum `μ(B_1)+2^χμ(B_1)Σ2^{j(χ−2)}<∞`. Generalized covariance matches Chen–Hu (2.18)/(2.22), Theorems 1.1 and 3.8(i) (Dalang, `γ≥0`, `PD`). Chen2023 Theorem 1.1 is imported **only** for finiteness of the variational constant under Dalang, and the p.2175 scaling `2^{χ/(4−χ)}M =` Chen2023’s `sup{A^{1/2}−(1/2)G}` is consistent with the extracted line (I also rederived this factor from the scale `s↦s^{d/2}g(s·)`). No Riesz-only transfer or name-only import. Verified at statement level; imported proof bodies unread.

**PROOF028 (planar upper).** Same Hőlder-on-common-measure skeleton as PROOF025, with closing `S/4`, opening mass `h_l`, `∏_open h_l ≤ (2t/k)^k`; spatial `(S/2)^k t^k/k^k`; temporal `2^k(Z_{b0}t^{2−b0})^k/k!`; product `(Z_{b0}S)^k t^{(3−b0)k}/(k!k^k)`, so `C_low=Z_{b0}S` exactly. Affine identities identical → `A_k≤C^k t^{(4−α−α0)k}/(k!)^{3−α}`, `C=C_low^ϑ C_st^{1−ϑ}`; series identity gives `exp(qC^{1/q}t^κ)`. Fixed-order convergence via `L:joint-fixed-order` and Chen–Hu Theorem 3.8(i); product-`L¹` passage explicit. Verified.

**PROOF029 (planar range).** `0<α≤1` → `P:low-alpha-upper`; `1<α<2−α0` → `P:planar-upper`; `Γ=0` → `u=1`, `C_2=0`. Covers `0<α<2−α0` in `d=2`. No inferred `d=3`, no sharp equality, no Skorohod, no limit interchange. Verified.

## Required fixes before production gate

1. **Rendered-page verification (not text layer):** confirm Chen–Hu p.2173 (5.1) and p.2180 (5.15) for the `p=2` specialization, and confirm the finite upper-rate form `limsup (1/k)log((k!)^{3−χ}B_k(1))<∞` on the rendered page; also confirm p.2165 Theorem 3.8(i) and p.2175 `2^{χ/(4−χ)}M` scaling from the rendered page.
2. **Chen2023 Theorem 1.1 rendering:** confirm it states finiteness under Dalang for nonnegative definite possibly-generalized `γ` (page 1 text does; page 2 statement needs rendered confirmation).
3. **Generalized-covariance scope:** explicitly retain that Chen–Hu Theorem 3.8(i)/(5.1)/(5.15) and Theorem 1.2 are applied to a homogeneous measure `Ξ` via the heat-regularized convention (2.18)/(2.22); the manuscript states this, keep it in the production gate evidence.
4. **Source-proof debt remains:** if the production gate requires end-to-end independence, the proofs of the imported source results themselves (Chen–Hu (5.15), Chen2023 Theorem 1.1) must be supplied or explicitly declared as accepted premises.
5. **Presentation:** disclaim sharpness of `C` (already done); do not promote these upper bounds to equality or to a dimension-three general endpoint theorem.

## One-line summary

The six static-holder/planar-upper proofs are internally correct with verified constants, signs, affine exponents, and final `t^κ` series identification; the only residual debt is that two imported source-theorem gates (Chen–Hu coefficient rate and Chen2023 variational finiteness) are matched to held statements but their proofs were not independently read in this snapshot.

**Per-proof ledger**

| Target | Status |
|---|---|
| PROOF024 `L:static-holder-input` | fully reconstructed; imports `(5.1)/(5.15)/(3.8)` matched, source-internal proofs unread |
| PROOF025 `P:static-holder-upper` | fully reconstructed |
| PROOF026 `L:planar-endpoints` | fully reconstructed |
| PROOF027 `L:planar-static-input` | partially checked; spectral/Dalang part full, imported finiteness chain statement-matched only |
| PROOF028 `P:planar-upper` | fully reconstructed |
| PROOF029 `C:planar-range` | fully reconstructed |

**Check ledger**

| Check | Status |
|---|---|
| PLN01 | checked (import caveat) |
| PLN02 | checked |
| PLN03 | checked |
| PLN04 | checked |
| PLN05 | checked |
| PLN06 | checked |
| PLN07 | checked (import caveat) |
| PLN08 | checked |
| PLN09 | checked |
| PLN10 | checked with unread/unperformed items: rendered-source proof bodies for the imported theorems, exact coefficient normalization |

[held back: collaborators' unpublished work]