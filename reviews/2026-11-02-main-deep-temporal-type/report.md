# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. No false identity, hidden hypothesis, incorrect constant, sign error, or invalid asymptotic was found in the seven audited bodies (PROOF052–058) or in the ST01–ST18 sub-obligations. All constants, exponents, boundary/exponent-removal orders, and limit orders verify algebraically against the supplied bodies and the embedded published Chen–Hu primary inputs.

## Noncritical findings

1. Positivity of the imported static rate `L0` (line 6911–6914) is justified by a sketched Gaussian-competitor argument (interaction `A c^{α/2}` vs kinetic `B c²`, both > 0 for nonzero Γ), not by a verbatim source pinpoint. The source's variational domain `F_d = {g ∈ W^{1,2}: ‖g‖₂=1}` (held text, journal p. 2147) admits such a competitor, and the scaling/positivity conclusion is standard and correct. This is an import-justification note, not a proof defect.
2. Lemma `L:mean-coefficient-holder` (PROOF052) proves the Hölder interpolation at the `a=0` endpoint but its *statement* restricts to `0<a<b`. The needed `a₁=0` endpoint is stated and proved separately in `L:full-moment-coefficient-holder` (PROOF056), which is what PROOF057/058 actually consume. Cosmetic/over-informative mismatch only; no gap.
3. Historical `\myCmts{}` annotations claiming prior Opus5.5/HIGH acceptance are present. Per the review protocol these are non-premises; I re-derived every step independently and confirm the claims stand on the mathematics, not on those receipts.

## Checked derivations

**Notation.** `ν = 3−α > 1`, `β(a) = 4−α−a`, `κ(a) = β(a)/ν`, `κ_st = (4−α)/ν = 1 + 1/ν`. `a_max = min(1, 2−α)` correctly encodes both `a<1` (temporal exponent integrability) and `a<2−α` (time-dependent Dalang form `α+a<2`), so `a<a_max ⟹ a<1` always.

**Diagram degree (mean and second moment).** A total-order-`2k` diagram carries `2k` time Jacobians (`t^{2k}`), `2k` Green masses (`G(cs,c dx)=cG(s,dx)`, each `t^{1}`), `k` spatial covariance factors (`t^{−α}` each), `k` temporal factors (`t^{−a}` each): total `t^{(4−α−a)k}=t^{β(a)k}`. Holds verbatim for empty-chain splits (`m=0` or `m=2k`): the single surviving chain still contributes `2k` Green factors, `2k` time variables, `k` pairs. Confirms E:mean-positive-series and E:full-moment-positive-series degree.

**Type identity (PROOF053).** With `z = t^{β(a)}`, `t^{−κ(a)} = z^{−κ(a)/β(a)} = z^{−1/ν}` since `κ(a)/β(a)=1/ν`. Hence `limsup_t t^{−κ(a)} log F_a(t^{β(a)}) = limsup_z z^{−1/ν} log F_a(z) = ν K(a)^{1/ν}` where `K(a)=limsup ((k!)^ν c_k)^{1/k}`. Forward bound: at `z=(νk/L)^ν`, `c_k z^k ≤ F(z) ≤ C_L e^{L z^{1/ν}} = C_L e^{νk}`, giving `c_k ≤ C_L e^{νk}(L/(νk))^{νk}`; Stirling `log k! ≤ k log k − k + 1 + log k` gives `K ≤ (L/ν)^ν`, `L↓τ`. Converse via `ℓ^ν ≤ ℓ¹` (`ν≥1`): `Σ (Az)^k/(k!)^ν ≤ e^{ν(Az)^{1/ν}}`, `A↓K`. Equality `τ=νK^{1/ν}` both directions — correct.

**Static-time/amplitude clock (PROOF054).** `σ^{2/(4−α)}T` at `σ=T^{−a/2}` gives effective time `T^{1−a/(4−α)}`, and `(T^{1−a/(4−α)})^{κ_st} = T^{κ_st(1−a/(4−α))} = T^{(4−α−a)/(3−α)} = T^{κ(a)}` (uses `κ_st=(4−α)/ν`, `β(a)=4−α−a`). Moment-identity check: total-order-`2k` carries amplitude `σ^{2k}` and static time `T^{(4−α)k}`; `σ^{2k}T^{(4−α)k} = (σ^{2/(4−α)}T)^{(4−α)k}`. Correct; only moments identified, not random fields (explicitly stated).

**Mean-gap exponent (PROOF055).** `K(0)=(L0/ν)^ν` via type lemma and `M(0)=L0`. Weighted limsup: `((k!)^ν m_k(a))^{1/k} ≤ [((k!)^ν m_k(0))^{1/k}]^{1−a/b}[((k!)^ν m_k(b))^{1/k}]^{a/b}` (valid since `(k!)^ν = ((k!)^ν)^{1−a/b}((k!)^ν)^{a/b}` and limsup of nonnegative products multiplies), giving `K(a) ≤ K(0)^{1−a/b}B_b^{a/b}`. Then `M(a)=νK(a)^{1/ν} ≤ ν K(0)^{(1−a/b)/ν}B_b^{a/(bν)} = ν(L0/ν)(B_b/K(0))^{a/(bν)} = L0(B_b/K(0))^{a/(bν)}`. Verified algebraically.

**Window (PROOF055/ST12).** `a_* = b log2/log(B_b/K(0)) ∈ (0,b]` since `B_b/K(0)≥2`. For `a<a_*`: `(B_b/K(0))^{a/(bν)} < 2^{1/ν}`, so `2M(a) < 2L0·2^{1/ν} = 2^{1+1/ν}L0 = 2^{κ_st}L0`. Hand control `B_b/K(0)=4 ⟹ a_*=b log2/(2 log2)=b/2` — confirmed.

**Log-convexity (PROOF057).** `K_p(a)=(Λ̄_p(a)/ν)^ν`; coefficient interpolation raises to `1/ν` and multiplies by `ν`, with `ν K_p(a_i)^{(w)/ν} = Λ̄_p(a_i)^w ν^{…}` powers cancelling exactly (`ν^θ ν^{−θ}=1`). Produces `log Λ̄_p` convex with only the limsup (upper) rate; secant-slope continuity on `(0,a_max)`, not at 0.

**Static recovery (PROOF058).** `Λ̄_p(a) ≤ Λ̄_p(0)^{1−a/b}Λ̄_p(b)^{a/b} = C_p(Λ̄_p(b)/C_p)^{a/b}`, ratio ≥1 finite; squeeze at fixed `b` as `a↓0`; `Λ̄₂/Λ̄₁ → 2^{κ_st}L0/L0 = 2^{κ_st}`.

**Source-fidelity spot checks.** Held Chen–Hu (1.9) text (journal p.2147) confirms `lim t^{−(4−α)/(3−α)} log E uᵖ = (3−α)/2 · p^{(4−α)/(3−α)} · (2M^{1/2}/(4−α))^{(4−α)/(3−α)}`, i.e. the `p^{κ_st}` factor with the same spatial constant for all `p`, so `E U²-rate = 2^{κ_st} L0` is an exact consequence of the import, not an assumption. Theorem 3.8(i) L² fixed-order existence and (2.18) heat-regularized generalized-covariance convention are present in the held published text. No author-`L_*/L^*` or source-(4.3) is used anywhere in the seven bodies.

## Required fixes before production gate

None. All seven bodies and all eighteen applicability/measure/limit obligations are fully discharged and correctly scoped. The iterated-limit scope (first `t→∞` at fixed `a` with its own `T^{−κ(a)}`, then `a↓0`; no uniformity, no fixed-`a` time-limit existence, no identification of Chen's printed endpoints) is stated explicitly in `R:temporal-type-scope` and matches the proofs exactly.

## Worked proof audit

### ST01–ST18 determinations

| # | Determination | Verification |
|---|---|---|
| ST01 | SATISFIED | Parameters `ν=3−α>1`, `a_max=min(1,2−α)`, `a∈[0,a_max)`, `a=0 ⟹` static covariance 1 (not `Γ_E(a)` substitution), all d∈{1,2,3}. Dyadic sum finite (α<2). Static `L0` and `p^{κ_st}` factor imported only from Chen–Hu Thm 1.2; no guessed coefficient identity. Gaussian competitor in the source domain `F_d` gives positivity. |
| ST02 | SATISFIED | Time-constant field ⟹ bounded variance at positive ε; L:terminal-wick Bochner construction; L:spatial-wick-measures with temporal multiplier 1; Cauchy gives static fixed-order `X_n^{(0)}` with heat-limit convention; d3 Green-before-noise; no infinite-series circularity. |
| ST03 | SATISFIED | `c=γ^0_{δ0,b0}(1)>0`, `γ^0(s−r')≥c` on `[0,1]` (decreasing kernel); amplitude `r/√c` pair factor `(r²/c)γ^0(s−r')≥r²`, termwise dominance; bounded by `B_{b0}(1;r/√c)` uniform in N,ε; L:uniform-series-tail ⟹ geometric `‖X_n^{(0)}(1)‖₂ ≤ B_r^{1/2}r^{−n}`; homogeneity `‖X_n^{(0)}(t)‖₂=t^{(4−α)n/2}‖X_n^{(0)}(1)‖₂`. |
| ST04 | SATISFIED | Finite positive `ω_{ε,D}` on unit simplex; a<1 integrable powers; diagonals null; one copy per pairing (coefficient 1); multiplier at `a` is exactly `a/b`-power at `b`; Hölder with g≡1 at 0; no Laplace-prefix interpolation. |
| ST05 | SATISFIED | E:joint-temporal-tail generalized to exponent `a` gives `F_{ε,η}≤F_{ε,0}≤F_{ε,η}+r_a(η)`, `r_a→0` uniformly in ε; ε→0 then η→0; static endpoint direct; degree `2(2k)−αk−ak=β(a)k`; β(a)>0 ⟹ `F_a` finite on `[0,∞)`. |
| ST06 | SATISFIED | Optimization `z=(νk/L)^ν`; `exp(νk)(L/(νk))^{νk}`; integral log-factorial bounds; kth roots ⟹ `K≤(τ/ν)^ν`; sparse/vanishing, τ=0, ν=1 handled. |
| ST07 | SATISFIED | Eventual `c_k≤A^k/(k!)ν`; ℓ^ν-ineq for ν≥1; polynomial ⟹ 0 logarithmic growth; `τ=νK^{1/ν}`; K=0 and ν=1 cases covered; no Tauberian overclaim. |
| ST08 | SATISFIED | `γ^0_{δ,a}(s−r)≥γ^0_{δ,a}(T)→T^{−a}`; finite Wick sums entry-by-entry, all self/cross pairs included; no phase/covariance-order comparison; p=1 mean distinct from E|u|. |
| ST09 | SATISFIED | Fixed T,N order of limits (d3 Green first, then joint ε,δ→0, then N→∞); `c_{δ,T}` finite polynomial at fixed order; static summability at σ=`T^{−a/2}` via effective time; 0<T<1 covered. |
| ST10 | SATISFIED | `σ^{2k}T^{(4−α)k}` per total order; identity only at `σ^{2/(4−α)}T`; limit inf; `T^{κ(a)}` raised exponent; `p^{κ_st}L0` from import. |
| ST11 | SATISFIED | `K(0)=(L0/ν)^ν>0`; `K(b)<∞` via CS + T:full-upper at exponent b; eventual `K(0)+η`, `B_b+η` bounds; `M(a)≤L0(B_b/K(0))^{a/(bν)}` (verified). |
| ST12 | SATISFIED | `a_*∈(0,b]`; strict `2M(a)<2^{κ_st}L0` for `a<a_*`; boundary strictness not claimed; p=1 is E[u] not E|u|; hand control B/K=4 ⟹ a*=b/2. |
| ST13 | SATISFIED | `c₁` = one split (0,2k); `c₂` = all 2k+1 splits incl. both empty orientations; pairing coefficient 1; `c_{p,0}=1` (no double count); Holder on disjoint-union measure; no factorial/binomial overcount. |
| ST14 | SATISFIED | `a₁=0` admissible; joint-temporal-tail covers unequal/empty chains; terminal reversal identifies static mixed moments; regroup nonnegative mixed terms (P:mixed); no phase/coupling/exponential/uniform-a overreach. |
| ST15 | SATISFIED | `C_p=p^{κ_st}L0`; liminf≥C_p (static minorant); p2 finite (full upper), p1 finite (CS, mean≥1); x-independence (spatial stationarity); `z^{1/ν}=T^{κ(a)}` matches. |
| ST16 | SATISFIED | `K_p(a)=(Λ̄_p(a)/ν)^ν`; ν-powers cancel; log-convexity of upper rate only; zero/oscillating subsequences handled by η-endpoints; no lower-liminf or p-order convexity claimed. |
| ST17 | SATISFIED | Secant bound on `(L,l,x,y,r,R)` with `L<l≤x<y≤r<R`; finite outer slopes; absolute Lipschitz on compact interiors; continuity only on `(0,a_max)`. |
| ST18 | SATISFIED | Endpoints 0,b give envelope; ratio ≥1 finite; fixed b/covariance squeeze; `Λ̄₂/Λ̄₁→2^{κ_st}` (L0>0); iterated `T→∞` then `a↓0`; no simultaneous/uniform limit, no author-constant identification, no all-p/E|u|/Skorohod/intrinsic acceptance. |

All eighteen obligations are met. Each cited limit order, amplitude-fraction, exponent identity, and boundary is reproduced explicitly in the bodies and re-derived above.

### PROOF052–058 rows

| ID | Claim | Status | Checked constants/limits; residual gap |
|---|---|---|---|
| PROOF052 | `L:mean-coefficient-holder` | FULLY_CHECKED | Static/bootstrap norm series; `m_k^ε(a)≤m_k^ε(0)^{1−a/b}m_k^ε(b)^{a/b}`; ε→0 then η→0; degree `t^{β(a)k}`; `F_a` finite on `[0,∞)`. No gap. |
| PROOF053 | `L:positive-series-type` | FULLY_CHECKED | τ→K with `(L/ν)^ν`; K→τ with ℓ^ν; equality `τ=νK^{1/ν}` both directions; τ=0, K=0, ν=1. No gap. |
| PROOF054 | `P:static-minorant-lower` | FULLY_CHECKED | `c_{δ,T}→T^{−a}`; entrywise Wick domination; effective clock `T^{1−a/(4−α)}`; `T^{κ(a)}` exponent; `p^{κ_st}L0` lower rate. No gap. |
| PROOF055 | `P:near-static-mean-gap` | FULLY_CHECKED | `K(0)=(L0/ν)^ν`; `K(b)<∞`; `M(a)≤L0(B_b/K(0))^{a/(bν)}`; nonempty window; strict `2M(a)<2^{κ_st}L0`. No gap. |
| PROOF056 | `L:full-moment-coefficient-holder` | FULLY_CHECKED | Split/empty-chain counting for p=1,2; k=0 coefficient 1; Holder at `a₁=0`; degree `β(a)k` incl. empty chains; regroup via P:mixed and static norm series. No gap. |
| PROOF057 | `P:moment-growth-logconvex` | FULLY_CHECKED | `Λ̄_p(0)=C_p`; CS+fminiteness; `K_p=(Λ̄_p/ν)^ν`; ν-power cancellation; log-convex upper rate; secant continuity on (0,a_max). No gap. |
| PROOF058 | `C:static-moment-constant-continuity` | FULLY_CHECKED | `Λ̄_p(a)≤C_p(Λ̄_p(b)/C_p)^{a/b}`; squeeze at a↓0; ratio `2^{κ_st}`; iterated-limit scope stated. No gap. |

## Limitations

1. The held primary PDFs are text extractions; mathematics in such extraction is garbling-prone. The key imported facts these seven proofs consume — the `p^{κ_st}` common factor and `p=1,2` static rates (Chen–Hu (1.9), p. 2147), homogeneity (1.8), generalized covariance (2.18), canonical kernels (2.10)–(2.14), and fixed-order Theorem 3.8(i) — are all confirmed structurally present in the held text; no numerical normalization of Chen's variational constant is used. Visual/source-image certification of those pages is outside this text-only bounded context and is recorded as not performed.
2. Positivity of the static variational input (`L0>0`) rests on the manuscript's Gaussian-competitor sketch plus the imported finiteness/law of Chen–Hu Theorem 1.2, which I could not re-derive from first principles here; it is a legitimate scoped import (ranked noncritical above).
3. This bounded unit does not establish the global/intrinsic `p=2` constant, all-order `p`, `E|u|`, Skorohod, or full214/all-model acceptance; the manuscript's remarks state this explicitly, and nothing in this unit overclaims it.

## One-line summary

All seven worked temporal-coefficient/static-endpoint proofs (PROOF052–058) and all eighteen ST01–ST18 obligations are mathematically sound with correct constants, exponents, limit orders, and honest iterated-limit scoping; no required fixes, verdict PASS at HIGH confidence.