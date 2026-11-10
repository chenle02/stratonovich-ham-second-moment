# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. All seven target proofs (PROOF094–100) reconstruct correctly with the stated constants, normalizations, boundary nullities, and scope restrictions. I found no proof-breaking sign error, false identity, hidden hypothesis, or invalid asymptotic claim within the bounded unit. The manuscript’s overclaim discipline is strong: each result explicitly limits itself to fixed finite `R,T`, rules out `H_W`-valued Gaussian vectors, all-cutoff path events, filter–mask commutation, and residual independence, and defers Young flow / moment asymptotics.

## Noncritical findings

1. **PROOF095, finite Banach moment finiteness.** “Gaussian expectations are finite by the finite-sum bound” is compressed. It is a standard fact (a finite Gaussian linear combination in a normed space has all moments via exponential tails of the driving Gaussian coordinates), but the manuscript does not spell out the polynomial growth argument. Not a gap.

2. **PROOF098, variance-domination display.** The equality `‖(I−Q_ρ)g‖² = ‖(I−P_η)g‖² + ‖P_η(I−C_ε)g‖² ≤ ‖g‖²` is correct but terse. The bound uses the λ-support decomposition and fiberwise contraction of `I−C_ε`: on the `λ≤η⁻¹` support the two projections are orthogonal and `P_η(I−C_ε)` kills the `λ>η⁻¹` part, so the sum is `‖g₂‖² + ‖(I−C_ε)g₁‖² ≤ ‖g‖²`. This is right but should be stated as such; as written it could be misread as “two terms each ≤ ‖g‖² imply their sum ≤ ‖g‖²”.

3. **PROOF099, dyadic continuity construction.** The Gaussian Kolmogorov-type modification in `d+1` parameters is compressed to the level of a standard argument (increment root moments `C√q · distance^{1/2}`, `2^{nm}` dyadic edges, weighted dyadic sum, binary refinement). It is correct, but the edge-count/exponent `1/2 − m/q` and the patching over countably many rectangles/multiindices are not expanded to full detail. Noncritical; no circularity.

4. **Source-fidelity verification is text-layer bounded.** The author identities (1.20), (1.21), (2.9), (2.11) are verified here only against the embedded `chen-author.txt` pages 5–9. The manifest explicitly warns that the PDF text layer garbles mathematics and that the page-8 increment display uses a differing spatial index; that specific display is not visually re-verified in this run (image credit is ZERO per scope). This limitation is recorded, not a defect of the manuscript’s own derivation, which re-derives the increment bound from the correct joint covariance.

## Checked derivations

**PROOF094 — `L:source-finite-comparison` — CHECKED.**
`φ(x)=‖Σx_jv_j‖^p` is convex (norm power, seminorm image allowed). Conditional Jensen with an independent completion `Z` of covariance `CI − Cov ξ` (nonnegative since `Cov ξ ≤ CI`) gives `Eφ(ξ) ≤ Eφ(ξ+Z)`; `ξ+Z` has law `√C·g`. Exponent root gives exactly the `√C` factor; `C=0` gives the zero identity. The comparison is a law comparison on an auxiliary space and does not alter the actual coupling of `ξ` or any downstream nonlinear object.

**PROOF095 — `P:source-gaussian-transfer` — CHECKED.**
`Var Y(F) ≤ C‖F‖²_{H_W}` annihilates null tests and extends `Y` to `H_W`; finite orthonormal families satisfy covariance `≤ CI` (used on every real linear combination, so independence of `Y(f_j)` is correctly not assumed). The `L^p(𝒞^θ)` Cauchy property of `M_{Y,N}` follows by applying PROOF094 to finite heads/tails with comparison vector law `(W(f_j))`. The raw-row identity `⟨A_j(t)z,w⟩=⟨h,f_j⟩_{H_W}` gives finite rows `Y(P_Nh)`, and `P_Nh→h` plus the noise bound gives `Y(P_Nh)→Y(h)`. Stability uses uniform tail control plus finite-head vanishing via `s_N(n)=Σ_j Var D_n(f_j)→0` (trace bounds the operator norm of a PSD matrix); arbitrary parameter rates are handled. No filter is commuted through `ζ_R` or the wave group.

**PROOF096 — `L:source-spatial-heat` — CHECKED.**
Spatial identity `B_Γ(f,g)=(2π)^d∫ f̂ ‾ĝ μ` is consistent with `c_d=(2π)^{−d/2}`. The heat kernel transform is `p̂_ε(ξ)=c_de^{−ε|ξ|²/2}`, so `(C_εf)^ = e^{−ε|ξ|²/2}f̂`; the multiplier lies in `[0,1]`, giving positivity, self-adjointness, and contractions for both `C_ε` and `I−C_ε`. Strong convergence `C_ε→I` follows by dominated convergence on Schwartz tests plus uniform boundedness. Separability/Schwartz inclusion are justified by the compact-support bound and temperedness of `Γ`.

**PROOF097 — `L:source-retaining-isometry` — CHECKED.**
`‖ΦF‖²_G = ‖F‖²_{H_W}` is exactly the identity `∫_{-∞}^{min(t,u)} 2λe^{−λ(t+u−2r)}dr = e^{−λ|t−u|}` composed with the Laplace kernel `∫Γ_E(a)^{−1}λ^{a−1}e^{−λ|t−u|}dλ = |t−u|^{−a}`; signed Fubini is finite for finite tensors because `a<1` and temporal/spatial factors are compactly supported. Closed range is automatic for an isometry. Retention `𝒾(Φh)=W(h)` uses `Φ` injective, orthogonal projection `P`, and an independent isonormal `J` on `(ΦH_W)^⊥`; `𝒾(g)=W(Φ^{-1}Pg)+J((I−P)g)` is isonormal and reproduces the actual `W(h)` variable, with equality on one countable-basis event. No negative-time raw noise and no uncountable equality event.

**PROOF098 — `P:source-canonical-convergence` — CHECKED.**
The heat-pair factor cancels `(2π)^d` exactly (`(2π)^dc_d²=1`), giving `B_Γ(p_ε(x−·),p_{ε′}(y−·))=Γ_{ε+ε′}(x−y)` after evenness of `μ`. The λ common range is `λ≤min(η^{−1},η′^{−1})=(max(η,η′))^{−1}`, matching the author’s `δ∨δ̃` upper limit; the `r` integral gives `e^{−λ|t−s|}`, so the joint covariance is `K_{max(η,η′)}(t−s)Γ_{ε+ε′}(x−y)`. Pointfield Bochner integration reproduces `Q_ρΦF`. The two variance dominations hold for source and residual; strongly `Q_ρ→I` at arbitrary relative rates (heat and λ-cutoff separately), residual independence is correctly not assumed, and driver convergence follows from PROOF095 without a simultaneous path event over all cutoffs.

**PROOF099 — `L:source-pointfield-regularity` — CHECKED.**
`∂_x^b v_{ρ;t,x}` is `G`-valued because the squared norms are the finite heat moments `∫ξ^{2b}e^{−ε|ξ|²}μ`; spatial increment uses `|e^{iξx}−e^{iξy}|≤|ξ||x−y|` and the next moment, temporal increment uses `1−e^{−λh}≤λh` on the finite λ range, giving `E|Z_b(t,x)−Z_b(s,y)|² ≤ C_{ρ,b}(|t−s|+|x−y|²)`. The `d+1`-dimensional dyadic Gaussian continuity/modification and multiindex/rectangle patching are standard and correct. The FTC in `G`, applied through bounded `𝒾`, converts the continuous modification into actual spatial derivatives `∂_iZ_b=Z_{b+e_i}` via pathwise+L² Riemann sums. Held for fixed `ρ` only; no density assumption and no substituted author increment formula.

**PROOF100 — `P:source-ordinary-response` — CHECKED.**
`b_ρ = ζ_RY_ρ` is compact smooth spatially and continuous in time, so the statewise integral defines a Lipschitz operator path (finite sample gain argument; no norm continuity of `S(t)` needed). The Sobolev adjoint identity holds at each fixed `u` using only spatial smoothness; integration gives the ordinary source-field integral against the literal raw test `h_{R,t;z,w}`. Smooth/indicator approximation plus bounded point-feature norms and the variance domination identify this with `Y_ρ(h)=⟨M_R^ρ(t)z,w⟩` in `L²`; countably dense states/times plus boundedness and path continuity extend to all states/times on one fixed-`ρ` event. Equality is on the actual coupled space, not merely in law.

## SRC checks (required 10)

- **SRC01 — PASS.** `L:source-finite-comparison` reconstructed: Banach/seminorm images, convex powers `p≥1`, independent covariance completion `CI−Cov ξ`, conditional Jensen, `√C`, `C=0`; comparison is auxiliary and does not replace the actual coupling.
- **SRC02 — PASS.** `P:source-gaussian-transfer`: raw-null annihilation, covariance `≤CI` without independence, full-path finite tails, `Y(P_Nh)=ΣY(f_j)⟨h,f_j⟩`, separable span limits, basis/complex/long-interval versions, residual finite-head + uniform-tail with arbitrary rates; no filter–mask commutation.
- **SRC03 — PASS.** `L:source-spatial-heat`: exact `(2π)^d` normalization, multiplier `exp(−ε|ξ|²/2)`, positive self-adjoint `C_ε`, contractions of `C_ε` and `I−C_ε`, strong convergence, Schwartz inclusion/separability; no physical quotient mask.
- **SRC04 — PASS.** `L:source-retaining-isometry`: `√(2λ)` finite-tensor norm identity, signed Fubini/support bounds, closed range and a.e. formula, actual-`W` retention via `P`+independent `J`, countable-basis event; no negative-time noise or uncountable equality event.
- **SRC05 — PASS.** `P:source-canonical-convergence`: `c_d`/`(2π)^d` cancellation, heat-pair `Γ_{ε+ε′}`, joint covariance `K_{max(η,η′)}Γ_{ε+ε′}`, pointfield Bochner identity, two variance dominations via orthogonal λ-ranges + heat contraction, arbitrary-relative-width limits, driver transfer, `√p`/square-exponential norms; residual not independent; no all-cutoff path event.
- **SRC06 — PASS.** `L:source-pointfield-regularity`: `G`-valued spatial derivatives via heat moments, increment bound `C(|t−s|+|x−y|²)`, `d+1` dyadic Gaussian continuity/modification, patch over countably many rectangles/multiindices, FTC+isometry+Riemann sums give actual derivatives; fixed `ρ`, no substituted increment formula or density assumption.
- **SRC07 — PASS.** `P:source-ordinary-response`: fixed-`ρ` regularity event, statewise strong integrals and finite gain give Lipschitz primitive without `S`-norm derivability, exact Sobolev adjoint, pointfield/raw-test `L²` equality, compact-support indicator-wave approximation, countable-dense states/times extension; actual coupled-space equality, not mere equal law.
- **SRC08 — PASS with limitation.** Author heat/Laplace definitions and joint-source convention at (1.20),(1.21),(2.9),(2.11) match the embedded pages 5–9; the page-9 same-law redefinition is correctly distinguished from the retaining coupling; no first-moment import or silent normalization correction. Limitation: no rendered-image re-verification of the page-8 increment display; recorded per scope.
- **SRC09 — PASS.** Zero covariance, white/delta and non-density/anisotropic spectral measures, differing widths and cross covariances, source/residual `≤‖F‖²` domination and covariance completion, time-0/large-`q` derivative scaling, actual coupling vs same-law, and the non-commutation / residual-non-independence handling all check; finite `R,T` constants and exact parameter ranges are preserved.
- **SRC10 — PASS.** All seven bodies reconstructed; the raw driver (`M_R`, bounded `A_j`) is a supplied input whose hypotheses were checked in the driver unit; no new Young-flow/moment/asymptotic/global-`R` assertion; no `H_W`-valued Gaussian or all-uncountable-cutoff event; every non-expanded step is standard and none leaves a load-bearing gap.

## Required fixes before production gate

None blocking. Optional polish (non-gating): (i) spell out finite-moment finiteness in PROOF095; (ii) expand the `‖(I−Q_ρ)g‖²` support decomposition in PROOF098; (iii) optionally expand the `d+1` dyadic modification in PROOF099 to fully explicit edge counting and patching. These do not change any conclusion or constant.

## One-line summary

All seven canonical Gaussian source proofs (finite comparison, Gaussian transfer, spatial heat, retaining isometry, canonical convergence, pointfield regularity, ordinary response) independently check out with correct constants, normalizations, nullity/boundary handling, and scope discipline at fixed finite `R,T`, with every retention-vs-same-law and residual-dependence caveat faithfully stated.