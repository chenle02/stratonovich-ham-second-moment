# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. No false identity, wrong sign, boundary-term loss, incorrect constant, hidden hypothesis, or invalid asymptotic was found in the seven bounded targets PROOF030–PROOF036. All numerical spot-checks (the mandated falsification tuple, the endpoint interval arithmetic, the low-endpoint constant `C_low = 2 Z_b0 π V_low`, the static rate constant `Λ_st = 2 (2√ℳ_st/(4−χ))^{4−χ}`, and both exponent–factorial identities) reproduce the manuscript's statements exactly.

## Noncritical findings

1. **`P:three-transfer` is conditional (by design, stated honestly).** It rests on `H:three-endpoints` (a deterministic Gaussian-convolution comparison on `Γ_low`,`Γ_st`), which the text explicitly says is *not* every homogeneous d=3 covariance. Corollaries discharge it only for products `∏|x_j|^{−a_j}` with `0≤a_j<1`, isotropic Riesz, plane-supported measures (`a_1+a_2=α−1`), and finite positive sums of invertible linear images. This is a scope boundary, not an overclaim; the full class is handled elsewhere (`T:full-upper`). Severity: none (honest).
2. **Chen–Hu p.2175 identification (`2^{χ/(4−χ)}ℳ`) is only partially verifiable from the embedded text extraction.** The full published-PDF text layer is flagged as garbled; the `2^{α/(4−α)}ℳ` square-root-Hamiltonian step is visible on carrier page 32 (journal 2175), but the printed identification sentence itself is not cleanly recovered. This is non-blocking because the manuscript only imports *finiteness* of `ℳ_st`, and that finiteness is independently grounded in Chen 2023 Theorem 1.1 ("the variations … are finite"), which is verbatim in the embedded `chen-2023-full.txt`. Severity: none.
3. **The integrated `\input{notes/integrated_*.tex}` files (lines 7830–7856) are not embedded in this snapshot.** They belong to the intrinsic-constant/occupation/white-evaluation sections, not to PROOF030–036, and none of the seven proofs cite them. Recorded as a limitation; no effect on the bounded verdict. Severity: none.
4. **The Riesz low endpoint `c|x|^{−1}` in d=3** has spectral ball mass `V_low` proportional to `∫_0^1 r^{1−3}·r^2 dr < ∞`; this is finite because the endpoint degree is exactly 1, so `L:alpha-one-convolution` (degree-one oscillatory bound) applies and the constant `πV/2` is correct. No density is assigned, and no radial spectral density is assumed. Verified; noted only because it is the one place the d=3 low endpoint barely stays integrable. Severity: none.

## Checked derivations

- **PROOF030** (`L:product-endpoints`): full interval arithmetic `L_j,U_j`, `Σj L_j<1<Σj U_j`, `0<Λ<1`, `Σb_j=1`, `Σv_j=χ`, coordinate reconstruction `a_j=ϑb_j+(1−ϑ)v_j`, strict `L_j<b_j<U_j`, `0<v_j<1`, zero-coordinate branch, `χ−α>0`, `2−χ>0`, local integrability/temperedness, Gaussian-mixture positive definiteness with **no Euler Gamma at exponent zero**, and the common-width Hölder comparison with amplitude `c` preserved.
- **PROOF031** (`L:plane-endpoints`): measure scaling exponent `2−e_1−e_2` giving `3−α, 2, 3−χ`; normal-Dirac/tangential-mixture positive definiteness; Hölder on the unnormalized finite measure `p_ε(w−(y,z))m` of mass `p_ε^{(1)}(w_3)`; low spectral measure `μ_low=(c/2π)δ_0δ_0 dξ_3`, hence `V_low=c/π`, closing constant `πV_low/2=c/2`.
- **PROOF032** (`L:endpoint-closure`): `q_Σ=q_{Σ−aI}*p_a` extension, boundedness `|F_J(x)|≤F_J(0)`, pushforward PD via `(φ∗φ̃)(Ty)=d_T(ψ∗ψ̃)(y)`, Gaussian transform `(p_ε∗J_T)(x)=d_T^{−1}(q_Σ∗J)(T^{−1}x)` with `Σ=εT^{−1}T^{−T}`, Hölder factor reconciliation `d_T^{−ϑ}d_T^{−(1−ϑ)}=d_T^{−1}`, discrete Hölder for finite nonnegative sums (zero-weight safe).
- **PROOF033** (`P:three-transfer`): static Dalang check `χ<2`; static coefficient homogeneity `t^{(4−χ)k}`; low-endpoint descending-integration bound `(πV_low)^k t^k/k^k`; pairing/split temporal count `2^k/k!`; `C_low^k t^{(3−b_0)k}/(k!k^k)≤C_low^k t^{(3−b_0)k}/(k!)^2`; full Hölder interpolation; static zero-Green approximant identification (Bochner↔pathwise via duality, weak sphere-measure convergence against bounded continuous Gaussian moments); target `γ_δ^0(0)=δ^{−α_0}/(α_0Γ(α_0))`, temporal Lipschitz, spatial second-moment, Gaussian 12th moment `|h|^6` on spacetime dimension 4 for Kolmogorov; exponent/factorial identities; variational tail with kept low-order polynomial, no division by zero static rate.
- **PROOF034** (`C:three-product-riesz`): midpoint `ϑ=(α_0+2−α)/2∈(α_0,2−α)`; product endpoints via PROOF030; Riesz endpoints `c|x|^{−1},c|x|^{−χ}` with exact affine identity `ϑ+(1−ϑ)χ=α`; `a_j=1` explicitly excluded.
- **PROOF035** (`C:three-finite-images`): common `α,ϑ,χ` across all three tolerated families; `L:endpoint-closure` on `T_i` then on finite weights; nonnegativity and `Σw_i>0` for a nonzero target; no coupling/stochastic-sum identity used.
- **PROOF036** (`L:physical-spectral-energy`): Dalang dyadic `Σ2^{j(χ−2)}`; imported unit-Schwartz quartic bound from Chen 2023 Thm 1.1, extended to `ℝ×W^{1,2}` via quartic homogeneity; `Q(fh)` vs quadratic `ℰ(fh)` distinctness; spectral CS for the mixed square pairing `P`, physical CS for `ℰ(fh)`; Lipschitz maps `A_f,B_f` with constant `D(N(f)+N(h))N(f−h)`; Schwartz approximation, translated-a.e. subsequence with Lebesgue first in `y` per `z`, σ-finite Fubini, `L^1` squares → uniform Fourier + `μ`-a.e. identification; representative independence; quartic bound on the limit.

## Required fixes before production gate

None blocking. Optional, non-gate items:
- For repository completeness, re-verify the Chen–Hu p.2175 `2^{χ/(4−χ)}ℳ` sentence from a *rendered* page image if that precise constant-supremum identification is ever promoted from "finiteness only" to a numerical constant. It is not needed for PROOF030–036.
- Keep the "conditional/alternative route" warning attached to `S:three-endpoints` (the manuscript already does this correctly); no editorial change required.

## One-line summary

The three-dimensional endpoint/transfer/energy block is internally correct: endpoint interval arithmetic, singular-plane spectral masses, closure under linear images and finite sums, the conditional `p=2` transfer with its non-sharp variational upper, and the Sobolev energy identification all check out with no proof gap and no overclaim.

---

## TD01–TD14 ledger (worked checks)

[held back until the source author has been told]

## Exact-source / application-role matrix (TD05)

[held back until the source author has been told]

## Prerequisites really read (embedded) vs interface/unread

- **Really read (embedded in the supplied excerpt):** `S:model` and standing conventions (107–251); `P:mixed` mixed expansion (445–518); `L:damped-homogeneous-norms` (595–683); `L:spatial-wick-measures` (950–1110); `L:joint-fixed-order` (1112–1207); `L:low-alpha-convolution` (2260–2318); `L:alpha-one-convolution` (2320–2382); `S:planar-holder` (`L:planar-endpoints`, `L:planar-static-input`, `P:planar-upper`) as the direct two-dimensional template; all seven target bodies (3746–4780); `R:three-endpoint-scope` (4607–4639).
- **Interface-only / partial:** Chen–Hu published PDF text layer (explicitly garbled; pinpoints cross-read as above); Chen 2023 published PDF text layer (verbatim where used); Chen author 64-page PDF — **not** consulted beyond the in-repo constructions (the seven proofs do not import it directly).
- **Unavailable/not supplied:** source images, manuscript renders, the `\input`-integrated TeX files for the intrinsic-theorem sections (not needed here), and any `Progress.md`/`Review.md`/reviews-directory state (intentionally excluded per read order).
- **Blindness disclosure honored:** I did not read any Progress/Review/HANDOFF/reviews artifact; I used only the embedded exact contexts. Historical review-prose phrases in the scientific source (e.g., "passed a scoped review") were read but treated **not** as mathematical premises, as instructed. This is **not** a cold read and no cold credit is claimed.

## Seven-row PROOF ledger

| Proof | Label | Verdict | Scope / notes |
|-------|-------|---------|---------------|
| PROOF030 | `L:product-endpoints` | FULLY_CHECKED | Interval arithmetic, reconstruction, PD, Hölder — all correct; TD01 tuple verifies. |
| PROOF031 | `L:plane-endpoints` | FULLY_CHECKED | Scaling exponent `2−e_1−e_2`, `V_low=c/π`, closing `c/2` — correct; singularity handled by measure. |
| PROOF032 | `L:endpoint-closure` | FULLY_CHECKED | Gaussian extension, pushforward determinant `d_T`, finite sums — correct. |
| PROOF033 | `P:three-transfer` | FULLY_CHECKED | Conditional transfer, Green-limit identification, non-sharp variational limsup — correct under `H:three-endpoints`. |
| PROOF034 | `C:three-product-riesz` | FULLY_CHECKED | Midpoint `ϑ`, product and Riesz endpoints discharge the hypothesis. |
| PROOF035 | `C:three-finite-images` | FULLY_CHECKED | Closure under `T_i` and finite weights; no coupling identity. |
| PROOF036 | `L:physical-spectral-energy` | FULLY_CHECKED | Spectral=physical energy; quartic bound; representative independence — correct. |

## Parameter / model / no-go boundaries

- **Parameter window:** `0<α_0<1`, `1<α<2−α_0` (so `α_0<ϑ<2−α` nonempty), `χ=(α−ϑ)/(1−ϑ)∈(1,2)`, `b_0=α_0/ϑ∈(0,1)`.
- **No-go / conditional boundaries (all stated in the manuscript):** `H:three-endpoints` is an additional condition not verified for arbitrary homogeneous d=3 covariances; product route requires `a_j<1` (excludes `a_j=1` coordinate white noise); no infinite-mixture uniform estimate; no representation/density theorem for general `Γ`; the variational constant is not sharp and not substituted into the all-time bound; `S:three-endpoints` is explicitly *not* an input to `T:intrinsic-second-moment`; no Skorohod matching and no enlargement of the published Balan–Conus comparison.
- **Zero credit:** zero source-image/render credit; zero cold-read credit; no Prior REPORT or identity-verdict rows were supplied and none are assumed.

## Explicit zero credit statement

- **Zero source-image credit:** no raster/source-image/manuscript-render was supplied or used; all formulas were read from the embedded text and the flag "PDF extraction may garble mathematics" is recorded.
- **Zero cold credit:** this is a bounded, non-cold depth audit with the full scientific source embedded; no cold-read claim is made.
- **No tools, no delegation:** performed directly in this model run within the project root; no absolute/external path was read.

END OF BOUNDED THREE-DIMENSION REVIEW