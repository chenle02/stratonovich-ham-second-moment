# Review Result

**Component scope.** `F_FOUNDATIONS_AND_WHITE` only, per the opening `new10-ID` Markdown assignment. I reconstruct the FOUR assigned owned deductions — `OWN004` (damped homogeneous norms/tails/scaling/smoothing), `OWN214` (stationary finite-measure translated coefficient-one Cauchy–Schwarz), `OWN215` (edge-labelled pairing induction with retained factor 2 and half/case bookkeeping), `OWN005` (complete positive spatial Wick measures) — plus the assigned white/source ancillary scope: `SOURCE-LAW`, `SOURCE-PRINT`, `BENCH-WHITE`, `FOUNDATION-JOIN`, `PRESERVATION`, `GLOBAL-SCOPE`. I do NOT reconstruct `OWN002/006/007/008/009`, the full9 constructor, `upper051`, `constant204`, the whole paper, the full–267-page visual gate, or any cold-read acceptance. All historical verdicts, roles and grades inside the quoted bodies are nonoperative history, not premises.

**Verdict.** `PASS_WITH_NOTES`.

**Confidence.** `MEDIUM` (unforced). The four owned deductions close cleanly from supplied literal sources, and the white `183/176` witness checks exactly; but `SOURCE-PRINT`/`SOURCE-LAW` pixel fidelity is resolved here at **text level only** (no actual image reading is claimed), and the full-owner/beyond-004–215 ambient paper is explicitly unassessed. Confidence is not raised toward `HIGH` by prior checks, and no `HIGH` acceptance is issued.

---

## OWN004 — `L:damped-homogeneous-norms` — status: RECONSTRUCTED

**Statement (candidate main `P267_OLD148/CANDIDATE267/notes/notes_stratonovich_ham_second_moment.tex`, SHA `516d6a65…`, LF 587–613; complete proof LF 615–675).** Under `H:homog`, the integrals in `E:damped-norm-definitions` are finite for every θ>0, `N2(θ)²≥0`, with
`N0(θ)=θ⁻²`, `N1(θ)=θ^{α+α₀−2}N1(1)`, `N2(θ)²=θ^{−β}N2(1)²`, `β=4−α−α₀`,
and the marked tails `N1^{(M)}(1), N2^{(M)}(1)→0` as `M→∞`, with spatial Gaussian, Green-heat and Laplace truncation non-increasing.

**Derivation verified.** Fourier uniqueness on the stated spectral convention gives `μ(cA)=c^αμ(A)` and `μ({0})=0`, hence ball masses `μ(B_r)=Vr^α`, `V=μ(B_1)`. Radial Stieltjes integration (no density/angular assumption) gives `∫μ(dξ)/(a²+|ξ|²)=αV a^{α−2}∫u^{α−1}/(1+u²)du<∞` for `0<α<2`. `N1` finiteness reduces to `∫λ^{α₀−1}(θ+λ)^{α−2}dλ` with endpoint conditions `α₀>0` and `α+α₀<2`. `N2` absolute integrability uses `|Ĝ_s(ξ)|≤min(s,|ξ|⁻¹)`, the `|ξ|≤1`/`|ξ|>1` split with `st` vs `|ξ|⁻²`, and the two explicit time integrals `Γ_E(1−α₀)θ^{α₀−2}` and `(2−α₀)Γ_E(1−α₀)θ^{α₀−4}/2`; the only time singularity is `v^{−α₀}`, `α₀<1`. Nonnegativity of `N2²` holds at each fixed ξ because the damped temporal self-pairing is the positive Laplace mixture of `e^{−λ|s−t|}` convolved through the OU/feature identity `∫h_λ(s,r)h_λ(t,r)dr=e^{−λ|s−t|}`; the explicit per-λ factorization keeps this valid despite the extra `e^{−θ(s+t)}`. Scaling identities follow from `λ=θu, ξ=θη` (first norm) and `s=u/θ, t=v/θ, ξ=θη` with `Ĝ_{u/θ}(θη)=θ⁻¹Ĝ_u(η)` (second norm giving θ to the power `α₀−2 + α−2 = −β`). Tails use `0≤K_M(r)≤|r|^{−α₀}`, `K_M→0` off-diagonal, and dominated convergence against the established absolute majorant; `K_M` is itself PD (positive Laplace mixture), so `N2^{(M)}²≥0` and `→0`. Smoothing/truncation are contractions: the `N1` after-Laplace integrand is nonnegative, and for `N2` the nonnegative per-ξ time form is integrated **before** a `[0,1]` spectral multiplier is removed — this is quadratic-form positivity, not pointwise heat monotonicity.

**Remaining premises.** None for the stated self norms. The cross-label finiteness and heat/Laplace restriction bounds are exactly what `OWN006/007/008` later consume; `OWN004` itself does not use `005/006/214`.

---

## OWN214 — `L:translated-covariance-CS` — status: RECONSTRUCTED

**Statement (candidate main, LF 709–720; proof LF 722–803).** For finite positive spatial measure `μ` with nonnegative inverse `γ=∫e^{iξ·x}μ`, positive temporal `ν` finite on every `(0,L]`, kernel `C_L=κ_L(t−s)γ(x−y)`, and nonnegative Borel `G₁,G₂` with finite `N₀` and `N_C`,
`0≤Q(T_{A,a}G₁⁰,T_{B,b}G₂⁰)≤N_C(G₁)N_C(G₂)` and `Q(T_{A,a}G_i⁰,T_{A,a}G_i⁰)=N_C(G_i)²`.

**Derivation verified, coefficient exactly one.** At cap `L`, the feature `h_λ(t,r)=√(2λ)e^{−λ(t−r)}1_{r≤t}` satisfies `∫h_λ(t,r)h_λ(s,r)dr=e^{−λ|t−s|}` and `∫h_λ²dr=1`; hence `Φ_L(t,x)(λ,ξ,r)=h_λ(t,r)e^{iξ·x}` has `‖Φ_L‖²=m_L=ν((0,L])μ(R^d)` and inner product `C_L`. Bochner Fubini gives `Q_L(f,h)=⟨F_L(f),F_L(h)⟩`, so `|Q_L(f,h)|≤Q_L(f,f)^{½}Q_L(h,h)^{½}`. Translating **both** integration variables of one test leaves its self pairing unchanged; applying Cauchy–Schwarz to the two differently translated tests gives the cross bound with coefficient `1`, uniform in origins, dimension, cap and masses, with the predecessor time offset `A−B` and spatial origin `a−b` **retained** (relativizing yields `κ(u−v+A−B)γ(X−Y+a−b)`). Monotone truncation `min(G_i,M)1_{0<t≤M,|x|≤M}` and positive cap passage to `∞` extend to general kernels; zero/empty norms cause no division. `OWN214` is an inequality over the original stationary covariance, never positivity of an independently shifted cross kernel and never the printed offset-free p21 equality.

**Remaining premises.** None. This is the bridge used inside `OWN215` for its finite-edge Hilbert step.

---

## OWN215 — `L:pairing-product-envelope` — status: RECONSTRUCTED

**Statement (candidate main, LF 1005–1017; proof LF 1019–1135; generic definitions LF 948–1004).** For `d≥1`, `0<a<1`, per-edge finite positive `μ_e` with `γ_e≥0`, measurable `A_e`, `ν_e=Γ_E(a)⁻¹1_{A_e}λ^{a−1}dλ`, independent-`x,y` norms
`N1_e(G)=∫|LG(λ,ξ)|ν_e μ_e`, `N2_e(G)²=∫G(s,x)G(t,y)κ_e(s−t)γ_e(x−y)`,
two separately rooted ordered chains (either empty), the diagram `I_D` is bounded above by the **finite maximum** over admissible products `∏_{Q₀}N₀·∏_{Q₁}2N₁·∏_{Q₂}N₂`, with `|Q₀|=|Q₁|`, `|Q₂|` even, each edge first once or second twice, never both, no incidence requirement. The maximizing assignment is per kernel family, and no kernel-independent partition is asserted. `n=0` gives `1=1`; zeros allowed.

**Derivation verified.** Finite caps make the covariance bounded and `ν`, `μ` finite, so the `OWN214` feature/Bochner step is justified in any finite dimension (the “dimension-free” remark is already explicit at LF 1023–1025). Convolution closures: `N₀(F)=N₀(G)N₀(H)`; `N1_e(F)≤N₀(G)N1_e(H)` from `LF=LG·LH` and `|LG(λ,ξ)|≤N₀(G)` for `λ≥0`; `N2_e(F)≤N₀(G)N2_e(H)` from zero-extension, translation-invariant self norms and Bochner/Minkowski. Base: `n=0` empty; two-vertex one-chain `N₀(G_first)N1_e(G_last)` (chronologically correct, so the printed p16 swap is a source caption error, not an induction error); one-per-chain `N2_e(G_u)N2_e(G_v)`. The endpoint-removal regional **half** uses: `κ` decreasing on the region `s_a≤s_p`, endpoint Fourier/Laplace extraction with the phase inside the *inner* modulus giving exactly `N1_{e₀}(G_v)`, drop of the endpoint-independent region indicator only **after** extraction by positivity; terminal partner gives mass, else fusion `F=G_a*G_b` (with successor in the *partner’s own* chain). The three fused slots are the displayed table: `i=0` union `Q₀=R₀∪{a,b}`, `i=1` retaining `2N₁(F)` and bounding `N1_{e₀}(G_v)[2N1_{e₁}(F)]≤½N₀(G_a)[2N1_{e₁}(G_b)][2N1_{e₀}(G_v)]` (ONE new mass, TWO new first slots, inherited edge still first once, `e₀` first once), `i=2` mass×second with the inherited `e₁` acquiring its second occurrence; in every branch `|Q₀|=|Q₁|` and `Q₂` even, every old edge keeps its type and multiplicity. Global exhaustion: domestic endpoint (covers empty chain), endpoints paired together (Case 2 keeps the predecessor offsets and uses original stationary CS coefficient one), and both endpoint pairs cross/distinct (Case 3 splits by `{s_a≤s_q}` and its complement; the second branch gets `s_p≥s_a>s_q≥s_b`, removes `u` instead; each region contributes a possibly **different** half-product, and `(P+P′)/2≤max(P,P′)`). Cap removal uses monotone diagram/norm integrands and the finiteness of `A_D`, with no measurable selector, no `C^n`, no stronger common partition; edge amplitude stays linear once per edge (first once ⇒ `c¹`, second twice ⇒ `(√c)²=c`).

**Remaining premises.** `μ_e` finite and cross-label `N1_e,N2_e` finite are hypotheses of the lemma; for applications these are supplied by `OWN004` on the heat/Laplace-regularized edges. The intended independent-`x,y` norm, not the literal repeated-`x` print, is the object proved.

---

## OWN005 — `L:spatial-wick-measures` — status: RECONSTRUCTED

**Statement (candidate main, LF 1176–1192; proof LF 1194–1336; definitions LF 1154–1175; also reconstructed in `P267_OLD148/COMPLETE_CONSTRUCTION_SUPPORT/07/full-working.md` and `24/fixed-order-foundation.txt`).** The positive finite measures `ν_{ε,D}` converge weakly as all spatial widths `→0` at arbitrary relative rates to a finite `ν_D`; `ρ_D=e^{Σr_l}ν_D` has `ρ_D(cA)=c^{(4−α)k}ρ_D(A)`; `ρ_D`/`ν_D` give zero mass to every coordinate face `r_l=0` and every positive horizon face `ℓ_i=T>0`; the bounded-continuous finite-horizon integral in `E:spatial-wick-limit` converges.

**Derivation verified.** Finite heat-weighted edge spectra `μ_e=e^{−b_e|ξ|²/2}μ` with total mass `VΓ_E(1+α/2)(2/b_e)^{α/2}` and `γ_e=p_{b_e}*Γ≥0` justify absolute Fourier/Laplace Fubini, giving the positive `E:spatial-positive-laplace` transform
`L_{ε,D}(λ)=∫e^{−Σ b_e|ξ_e|²/2} ∏_l [(1+λ_l)²+|η_l(ξ)|²]⁻¹ ∏_e μ(dξ_e)`,
no spectral/angular density assumed, `η_l=0` giving `(1+λ_l)⁻²` with no zero-mode issue. Heat bound `(p_t*γ_b)(x)≤A_heat(t+b)^{−α/2}≤A_heat t^{−α/2}` with `A_heat=2^{α/2}VΓ_E(1+α/2)`. Brownian occupation moments: order the `2j` labeled times, condition on the largest **remaining** vertex, remove it and its partner, marginalize the now-free observation (never retaining a removed future vertex, which would create a bridge), select `j` **distinct** right endpoints whose current gaps dominate the original adjacent gaps, and integrate the `j` Dirichlet parameters `1−α/2` with `j+1` parameters `1`, obtaining
`E_B S_b(T)^j ≤ (2j)[A_heat Γ_E(1−α/2)]^j T^{(2−α/2)j}/Γ_E((2−α/2)j+1)`.
Wave-to-Brownian identity `∫e^{−qt}G_t(dx)dt=½∫e^{−q²u/2}p_u(x)dudx` (equal Fourier transforms `(q²+|ξ|²)⁻¹`); the `2^{−2k}` vertex factors and the `¼` two-horizon insertion `1=¼∫∫e^{−[(a−τ₁)+(b−τ₂)]/2}` (also valid for an empty chain with `τ_i=0`, each lifetime integral `=2`) give the explicit uniform mass `U_k=2^{−2k}[Σ_j C(k,j)(2j)!(2^{2−α}A_heatΓ_E(1−α/2))^j]²<∞`, with cross-pairing dominated by spectral CS `C₁₂≤√(S₁S₂)` and domestic/cross occupation counted as `S₁^{v₁+w/2}S₂^{v₂+w/2}≤(1+S₁)^k(1+S₂)^k`. Compactification `y_l=e^{−r_l}`: bounded masses + monomial moments (`L_D` values including the constant moment) + Bernstein polynomial density give uniqueness; continuity of `L_D` at zero and monotone convergence prove the union of `y=0` faces has zero mass, so no mass escapes to infinity. A single `λ_l→∞` under domination by the integrable zero-parameter integrand gives `ν_D{r_l=0}=0`. Undamped homogeneity `ρ_{ε,D}(cA)=c^{(4−α)k}ρ_{ε/c²,D}(A)` from `G_{cr}(c\,dz)=cG_r(dz)`, `γ_b(cx)=c^{−α}γ_{b/c²}(x)` and `2k` time Jacobians, passed through vague limits. Positive horizon faces at `T>0` are null by countably many disjoint positive-mass dilates inside one compact set contradicting local finiteness; an empty chain has `ℓ_empty=0` full pushforward and is never declared null. Finite-horizon passage: `Ω={ℓ₁<T₁,ℓ₂<T₂}` is bounded with boundary in the proved null faces, `e^{Σr_l}≤e^{T₁+T₂}`, compact cutoff handles the otherwise open-orthant test continuity.

**Remaining premises.** None. `OWN005` consumes only `H:homog` and elementary measure/Brownian facts; it does **not** use Theorem 3.1, `004/006/214`, any all-order series, or any upper/constant result, consistent with the required non-funding direction.

---

## SOURCE-LAW — status: RECONSTRUCTED (text level)

**Basis.** Author primary `P267_OLD148/PRIMARY_FULL64/author-full-layout.txt` (SHA `5a6eff97…`), p9 (2.11), p13 (2.24); candidate `E:pairing-source-covariance` in the main at LF ≈869 (printed 3.10 per the draft readback).

**Derivation verified.** Independent Laplace-frequency increments on disjoint intervals intersect on the common prefix `λ≤min(δ_j⁻¹,δ_h⁻¹)=(δ_j∨δ_h)⁻¹`, so temporal widths combine by **MAXIMUM** (`γ⁰_{δ∨δ̃}` in (2.11)); spatial heat semigroup gives `p_{ε_j}*p_{ε_h}=p_{ε_j+ε_h}`, widths by **SUM** (`γ_{ε+ε̃}`); the exact weight `Γ_E(α₀)⁻¹λ^{α₀−1}` and the original covariance amplitude carry through; the endpoint `{0}` has Lebesgue measure zero, so `[0,L]` and `(0,L]` agree. For generalized `Γ`, the spatial identity is justified by testing heat functions / spectral multipliers, requiring no covariance density. The candidate remark correctly separates this **covariance identification** from (i) constructing the common family from the given `W` alone and (ii) the joint `005/006` source limits.

**Remaining premises / limit.** This closes at **text level**. I did not read page pixels; the author pixel-dossier claims (`P267_OLD148/PRIMARY_AUTHOR_AUDIT/*`, `DRAFT_EVIDENCE/source-covariance-application-readback.json`) are quoted evidence, not independently verified images.

---

## SOURCE-PRINT — status: RECONSTRUCTED (text level); explicit literal-variable answer

**Basis.** Primary layout pages 14–21 (`P267_OLD148/ARCHIVE_REQUIRED25/primary/pages/page-14.layout.txt` … `page-21.layout.txt`; also inside `author-full-layout.txt`), candidate pages 16–21 (changed pages), reader audit `P267_OLD148/PRIMARY_AUTHOR_AUDIT/findings.json` and `report.md`.

**Explicit requested answer.** In source (3.5) the **second wave kernel is `G(t,·)` with spatial argument `x`** — the layout prints `G(s,x)G(t,x)` integrated in `ds dx dt dy` against `γ(x−y)`. This is the literal repeated-`x` print, distinct from the intended independent-variable norm `G(s,x)G(t,y)` that `OWN214/004/215` actually use. This answers the “which variable is the second spatial argument” question without reading the covariance `γ(x−y)`.

**Other print qualifications reconstructed (text):** (3.4) has the inner absolute value around the Fourier–Laplace transform, needed for the phase-removal/`N1` bookkeeping; p16 empty-chain base swaps the chronological labels (either empty chain gives `Q₀={first},Q₁={last}`, not the printed reversed assignment); p18 `(3.9)` loses the factor 2 in the fused first-slot branch before a half-bound that Case 3 needs (see `BENCH-WHITE`); p19 prints `∩` where `∪` is required to add the two excluded labels and an off-by-one on the remaining first-slot edge count; p21 Case 2 drops the predecessor time offset `A−B` in its change-of-variables equality (`κ(u−v+A−B)` is the correct expression) while keeping the spatial offsets; p21 Case 3 mislabels the second partition subscripts. These are printed-source discrepancies, **not** theorem falsity, and the candidate repair is not attributed to the printed source.

**Remaining premises / limit.** Text-layout resolution only; no pixel credit claimed. The p14 inner bars and the 200-dpi cropped norm-definition detail are not independently read here.

---

## BENCH-WHITE — status: RECONSTRUCTED (analytic witness verified)

**Setting.** `d=α=1`, `Γ=cδ₀`, spectral convention `μ(dr)=c dr/(2π)`, `0<a<1`, `θ>0`, `G(t,x)=e^{−θt}1_{|x|<t}/2`, `F=G*G`, original amplitude `c≥0`.

**Full closed norms (independently rederived).** `N₀(G)=θ⁻²`. `LG(λ,r)=1/((θ+λ)²+r²)`; `∫_R dr/(A²+r²)=π/A` gives
`N₁(G) = (c/2)Γ_E(1−a)θ^{a−1}`;
the white physical overlap `c∫G_sG_t dx=(c/2)min(s,t)` split over the two off-diagonal quadrants gives
`N₂(G)² = (c/4)Γ_E(1−a)θ^{a−3}`;
`LF=(LG)²` and `∫dr/(A²+r²)²=π/(2A³)` give
`N₁(F) = (c/8)Γ_E(3−a)θ^{a−3}`.
All Gamma steps are positive Tonelli + defining Gamma integral, finite for `0<a<1`; the time diagonal is Lebesgue-null. Hence for `c>0`:
`2N₁(F)/N₂(G)² = Γ_E(3−a)/Γ_E(1−a) = (2−a)(1−a)`, and `2N₀N₁/N₂²=4`, `N₁(F)/(N₀N₁)=(2−a)(1−a)/4<1/2`; at `a=1/4`, `c=θ=1` this is exactly `21/16>1`. `c=0` is the direct zero branch (no ratio formed).

**Explicit finite witness (`ε=1/4`, `L=4`, vertex spatial widths `1/8`, temporal widths `1/4`).** With `B=N₂_full²=Γ_E(3/4)/4` and `A=2N₁_full=(21/16)B`, and `A_{ε,L}=2N₁_{ε,L}(F)`, split the exact loss `N₁_full−N₁_{ε,L}=T+H` with `T` the `λ>L` tail and `H` the capped heat loss (the finite measure is supported on `(0,L]`, so there is no “heat on tail” term). Verified bounds: `2H/B≤ε=1/4` and `2T/B≤1/44`, where `Γ_E(1/4)Γ_E(3/4)=∫λ^{−3/4}/(1+λ)≥½∫₀¹λ^{−3/4}=2` gives the Gamma-product floor. Therefore
`A_{ε,L}/B ≥ 21/16 − 1/4 − 1/44 = 183/176 = 1+7/176 > 1`,
and `N₂_{ε,L}(G)²≤B` by positive temporal quadratic-form / Gaussian-multiplier contraction. The integral `∫r²/((1+λ)²+r²)²dr=π/(2(1+λ))` and the `(3−a)` tail denominators all reproduce; the independent checker’s `1.1888` is quadrature **confirmation**, while `183/176` is the analytic lower bound. This diagnoses only the source first-slot transition (`2N₁(F)` cannot be absorbed into an unmultiplied `N₂·N₂`), not the existential product theorem; the repair `N₁(F)≤N₀(G)N₁(G)` remains valid because `N₁(F)/(N₀N₁)=(2−a)(1−a)/4<1/2`. The existing Lean certificate (`ClockFilter.lean`, SHA `0e501b25…`) validates at most the unchanged rational resolvent partial-fraction identity; the heat/tail/Gamma/`183/176` steps are analytic and are **not** lean-certified (new Lean facts `0`, existing 80 unchanged).

**Remaining premises.** None for the witness. Finite-edge cross-label norm finiteness holds because the Gaussian heat spectrum, the capped Laplace measure, and the nonnegative `L¹` kernels `G,F` give finite bounded-covariance norms; the literal repeated-`x` self-quadratic is likewise finite here (bounded `κ_L`, total heat mass 1).

---

## FOUNDATION-JOIN — status: RECONSTRUCTED (funding direction)

**Actual direction (candidate main + `constructor/source-bindings-and-graph.json` + `source-evidence.json`).** The owned spine is `004,214,005,215 → 006 → 007/008 → 002`, with `009` depending on `006/008` and `002` additionally on `005/009/215`. None of `004,214,005,215` consumes `006/009/051/204`; `006` consumes only `004/005/215`; there is **no** backward funding arrow from the later `051` (independent upper) and `204` (intrinsic constant) into the foundation. Verified from quoted source: `OVERVIEW_051_DEPENDENCY` lists `joint-fixed-order` as an input of the full upper construction; `POSITIVE_SCORE_FINITE` (in `integrated_unmasked_variational.tex`) uses `051` for the finite score; `INTRINSIC204` (`integrated_intrinsic_constant.tex`) consumes that finiteness. Hence `006 → 051 → positive-score finiteness → 204` is a genuine **downstream** route, while `051/204` do **not** fund the earlier construction, and `215` alone proves neither later theorem. This matches the required “no backward funding” condition.

**Minor metadata defect (not a cycle).** The bindings graph lists `OWN007` among `OWN008`’s `actual_current_owned_inputs`, but `OWN008`’s literal `\ref`s do not include `L:crude-corrected`, and the `L:vertex-crude` proof in the candidate main does not consume `007`; `007/008` are parallel descendants of `004/006/215`. The extra edge is a curation overclaim, adds no cycle, and should be removed from the metadata.

**Remaining premises.** `006/009/002` full proofs are outside this assignment; the JOIN is verified only for the funding/direction structure, with `051/204` and all Young/operator material explicitly non-financing context.

---

## PRESERVATION — status: RECONSTRUCTED (mechanical, quoted-body level)

**Verified from quoted bodies.** Candidate 28 modules pin to the stated SHAs, with only the main module differing from the baseline (`516d6a65…` vs `36475324…`); the 27 included modules are byte-identical in both listings. Proof environments `214→215`, formal declarations `240→241`; `209` old proof bodies byte-identical, the five changed bodies (`P:mixed`, `L:joint-fixed-order`, `L:crude-corrected`, `L:vertex-crude`, `P:envelope`) are attribution/every-product prose only with all inline/display/equation/align math spans equal; all `214` owned statement bodies retained; `OWN214` raw proof body unchanged (`8a187e…`); `R:source-case2-time-shift` (S071) is the only altered old formal body and is explicitly qualified as “not corrections attributed to the source”; the new owner `L:pairing-product-envelope` is an explicit lemma with separate statement/proof, not hidden in a remark; labels added (`E:pairing-*`, `L:pairing-product-envelope`), none removed. The one new-proof (`215`/`241`) claim and the “unadopted external candidate” status are preserved.

**Remaining premises / limit.** This is byte/text-presence identity, not proof of correctness and not a full-267 visual gate; I did not re-execute hash tooling, so the mechanical receipts remain author/checker evidence, verified here only against the quoted body text.

---

## GLOBAL-SCOPE — status: NOT_READ (outside assignment)

**Exactly out of scope.** Not reconstructed or accepted here: `OWN002/006/007/008/009` full proofs (only their funding direction and the `006` application-clause hypotheses were used), the full9 Kimi constructor, the independent `upper051`, the intrinsic `constant204` and occupation/white-evaluation chains, all Young/operator/rough/tube material, the whole 214-OWN/240-formal/13-join paper, the full–267-page visual gate, Kimi/native cross-family pixel coverage, the fresh independent cold read, and private-delivery/<HUB> gates. The prior `PASS_WITH_NOTES/MEDIUM` (P267) and `SOURC-IN-RNAL-DISCREPANCY` source qualification remain unchanged; my result does not regrade them, does not reuse them as premises, and is **not** a whole-paper or completion certificate.

---

## Fatal findings
None in the assigned scope.

## Major findings
None in the assigned scope.

## Minor findings
- **M1 (metadata, curation).** `constructor/source-bindings-and-graph.json` adds an unsupported edge `OWN007→OWN008`; the candidate `L:vertex-crude` does not reference `L:crude-corrected`. Remove the edge; no mathematical consequence.
- **M2 (source quantifier).** p15 “possibly depending on `n1,n2` and `D`” is weaker than the actually proved per-family dependence (`∃Q` per kernel/edge/cap data); `OWN215` keeps this explicit. Any citation should use the per-family/finite-maximum form and not infer a kernel-independent `Q`.
- **M3 (source print).** (3.5) literally repeats `x` in `G(t,x)` (second spatial argument `x`). The intended/used norm is `G(s,x)G(t,y)`; this remains a source display qualification, text-resolved, not pixel-certified.
- **M4 (benchmark scope).** The finite-edge numeric control `1.1888…` is quadrature, not an interval proof; the rigorous statement is the analytic `183/176` bound; the kept Lean certificate covers only the unchanged rational resolvent identity.

## Required repairs
None (mandatory blockers).

## Limitations
- Text-only reconstruction: no actual page-image reading was performed or claimed; `SOURCE-PRINT`/`SOURCE-LAW` are certified at layout-text level only, with author pixel-dossier claims quoted as non-operative evidence.
- `OWN005`, `OWN214`, `OWN215` are reconstructed from the supplied quoted sources; this is one-model verification, not the separate Kimi/source-image/native cross-family gate.
- The ambient `006/009/051/204`, whole-paper, cold-read and full-267-visual obligations remain open; no old verdict was regraded and no `HIGH` acceptance is issued.
- LF/byte locators are cited from the supplied bindings and quoted bodies; I did not independently re-run a line-counting tool.

## Actual reading inventory (bodies actually used)
- `C026` candidate main (SHA `516d6a65…`): own statements/proofs `L:damped-homogeneous-norms`, `L:translated-covariance-CS`, `L:spatial-wick-measures`, `L:pairing-product-envelope`, `E:pairing-*` definitions, `R:source-case2-time-shift`, source-law remark, `L:vertex-crude` (funding check), `OVERVIEW/POSITIVE_SCORE` context.
- `C017/C018` (norm and translated-CS support), `C019/C092/C106` (OWN005 full reconstruction), `C002/C061/C063–C065/C071–C074` (source print/law/audit), `C008–C015` and `C070` (primary pp14–21 and full64 layout text; pp9/13), `C124–C146` (benchmark-white original + independent + explicit-finite witness), `C119/C153` (owner/definition/cutout coverage bindings), `C055/C057/C058` (goal/scope/joins), `C077/C078/C120/C121` (prior MEDIUM reports/adjudication — nonoperative only), `C110/C112` (historical native reports — challenge evidence only).

## Global scope statement
This PASS_WITH_NOTES covers exactly the four owned deductions `004/214/215/005`, the text-level source law/print qualifications, the analytic `BENCH-WHITE` `183/176` witness, the acyclic foundation funding direction, the quoted-body preservation identity, and the explicit out-of-scope boundary. It is a bounded component reconstruction. It does **not** establish the five construction deductions, the full9 constructor, `upper051`, `constant204`, any pixel/cold/flood gate, the whole paper, or whole-goal completion; all original models, amplitude, data `(1,0)`, zero-covariance branch, and the actual-C2 goal remain exactly as stated, with every unresolved ASSIGNED implication listed above rather than silently discharged.