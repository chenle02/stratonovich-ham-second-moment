# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

(Original report reproduced below, followed by the requested correction/completion. Verdict and confidence are unchanged: no proof gap was found; the four submission checks confirm the source is correct and my original report had three imprecise notes, now retracted, and one redundant non-defect note, now retired.)

---

## Original report (preserved)

### Critical findings

None. I re-derived the internal logic, signs, boundary terms, scaling factors, and all final coefficients of PROOF135–141, and found no false identity, wrong exponent, sign error, or invalid asymptotics inside the seven audited proofs. In particular the fine coefficients that are easy to get wrong are correct:

- PROOF137: maximizing `L → L − C·L^q` with `q=4−α`, `k=q−1` gives the point `L^k = 1/(qC)` and value `(k/q)(qC)^{−1/k} = k(q^q C)^{−1/k}`; with `u=α/q`, `1+u=4/q`, this reduces exactly to `k[ R(g)α^{α/2}/(8 M_a q^{q/2}) ]^{1/k}`.
- PROOF139: the energy identity constant `((2−α)/2)α^{α/(2−α)}R_sp^{2/(2−α)}` is correct, and the substitution `R_sp α^{α/2} = (2E_sp/(2−α))^{(2−α)/2}` is correct.
- PROOF141: the scalar comparison constant `R_star^{2/(2−α)}·E_sp` is correct.
- Cross-checked the downstream white consumer (`E_sp = c²/6`, `F0 = √c/(3√2)`, bracket `(2/3)√(c/M_a) ≤ C₂ ≤ (2/3)√(cK₀)`) against PROOF139/140/137 formulas; consistent.

The honesty posture is also correct: the proofs explicitly refuse optimizers/attainment, keep Fatou as an inequality until continuity is re-established separately, and never claim `1_E ∈ H¹`.

### Noncritical findings

1. Large external dependency surface (not rederived here): exact equilibrium potential/mass, unmasked Rayleigh rate, mask cutoff `χ`, and finiteness of `S1^pos`/`T:full-upper`. Cited consistently; off-scope.
2. PROOF135 relies implicitly on the extended Tonelli convention `0·∞=0`; degenerate white `α=d=1` not spelled out.
3. `K_star(0)=0` redefines a divergent pointwise limit.
4. Compressed positivity/Lipschitz step in PROOF136.
5. Compressed PSD-extension step in PROOF138.
6. Compactified Bochner-measurability argument in PROOF141.

### Checked derivations

(As in the original submission: PROOF135–141 itemized; signs, scaling, and coefficients verified.)

### Required fixes before production gate

No mathematical corrections required; recommended precision edits listed.

### One-line summary

All seven physical-occupation proofs (PROOF135–141) are correct in logic, signs, scaling, and final coefficients, with no proof gap found; the only qualifications are the properly cited but here-unrederived external inputs and a few compressed standard arguments.

---

## Corrections and coverage completion

### Concrete check 1 — the PROOF136 Lipschitz/positivity bound: **partial retract; remainder defended**

My original note said `λ_z(c)²` is bounded by `‖U_z‖_∞` for arbitrary `c>0`. That pointwise bound is wrong as stated; it is a bound on the *Lipschitz constant of `λ_z(c)²` as a function of `c`*, not on the value of `λ_z(c)²`. Corrected, verified derivation:

- By definition `λ_z(c)² = sup_{‖g‖₂=1} [c·A_g − b_g]` with `A_g = ∫U_z g² ≥ 0`, `b_g = ‖∇g‖₂² ≥ 0`. Hence, dropping the nonpositive kinetic term,
  `λ_z(c)² ≤ c·‖U_z‖_∞`.
  This is the finiteness statement for each fixed `c>0`, and it is **`c`-dependent**, not uniform in `c`.
- As a function of `c`, `λ_z(c)²` is a supremum of affine functions with slopes `A_g ∈ [0,‖U_z‖_∞]`. Therefore it is convex and globally Lipschitz with best constant `sup_g A_g = ‖U_z‖_∞` (its subgradient is an `A_g` attaining near the maximum of the continuous function `U_z`). So the manuscript's line "`λ_z(c)²` is Lipschitz with constant `‖U_z‖_∞`" is **correct**, and it is an assertion about the map `c ↦ λ_z(c)²`, not a uniform-in-`c` value bound.
- The square-root Lipschitz claim is asserted only for `λ_z(c)` on a **compact positive `c`-interval**, where a positive floor exists: `|λ_z(c)−λ_z(c')| = |λ_z²(c)−λ_z²(c')|/(λ_z(c)+λ_z(c')) ≤ ‖U_z‖_∞|c−c'|/(2m)`. **No global Lipschitz claim in `c` is made for the rate itself**, and none is needed.

Verdict on the check: the source is correct; the claimed distinction between a pointwise `c‖U_z‖_∞` bound and the `‖U_z‖_∞` Lipschitz constant is real and matches the source.

### Concrete check 2 — positivity of `λ_z(c)` for every `c>0`: **retract my note; the all-model common-trial argument is correct**

My original explanation (“dilate a bump where `U_z>0`”) was inadequate, because local positivity of an arbitrary compact potential does not by itself produce a negative trial in `d=3`. The source instead uses the homogeneous-`Γ` `ψ_L` construction of `P:compact-original-common-trial`. Correct derivation, verified directly:

- `U_z = Γ*z`, `z∈C_c^∞(ℝ^d)`, `z≥0`, `z≠0`, `supp z ⊂ B_A`. Take `ψ∈C_c^∞(B₂)`, `ψ≥c₀>0` on `B₁`, `‖ψ‖₂=1`, and `ψ_L(x)=L^{−d/2}ψ(x/L)`, `D_ψ=‖∇ψ‖₂²`.
- For `L≥2A` and `y∈B_{L/2}`, every `w∈supp z` has `|w+y|≤A+L/2≤L`, so `ψ_L(w+y)≥c₀L^{−d/2}`. Therefore
  `∫U_z ψ_L² = ∫Γ(dy)∫ z(w)ψ_L²(w+y)dw ≥ Γ(B_{L/2})·c₀²L^{−d}∫z = c₀²2^{α−d}Γ(B₁)(∫z)·L^{−α} =: C_z L^{−α}`.
  The white case `α=d=1` is included: `Γ(B_{L/2})=Γ(B₁)>0` under the exponent-0 scaling `Γ(cA)=c^{d−α}Γ(A)`, so `C_z>0` with `L^{−1}`.
- The kinetic term is `‖∇ψ_L‖₂² = D_ψ L^{−2}`. The Rayleigh value of `ψ_L` is
  `c·C_z L^{−α} − D_ψ L^{−2} > 0` for all large `L` because `α<2` (so `L^{−α}` dominates `L^{−2}`). Hence `λ_z(c)²>0` for **every** fixed `c>0`.
- On a compact interval `[c_−,c_+], c_−>0`, replace `c` by `c_−` to select one common `L` and obtain a **uniform positive floor** `m² = c_−C_z L^{−α} − D_ψL^{−2} > 0`, which supplies the square-root Lipschitz bound of check 1.

No local-binding hypothesis is inserted; the argument is the same homogeneous-`Γ` binding used for the compact mean family and is valid for all `d∈{1,2,3}`. The source's `P:variational-unmasked-rate` supplies the boundedness/complexification machinery; the all-model positivity for `Λ_z(c)` is exactly this construction.

### Concrete check 3 — positivity of cross pairings and the PSD-extension order: **retract my attribution; the source's order is correct**

My original note said positivity of `B_Γ(f²,h²)` on `H¹` comes by polarization. That conflates two different steps.

- For `f,h∈H¹` with **nonnegative square representatives**, `B_Γ(f²,h²)=∫f(x)²h(x−y)²ν(dx,dy) ≥ 0` is immediate from the **nonnegative physical Radon integrand**. It is **not** obtained from PSD. PSD `B_Γ(Q,Q)≥0` is about a *single signed profile* `Q`, via `B_Γ(Q,Q)=∫|Q̂_ord|²μ≥0`.
- The verified order in PROOF138 is:

1. smooth-case homogeneous bound `A_sp(f) ≤ R₀N(f)⁴`;
2. signed smooth `B_Γ(Q,Q)≥0` (Fourier normalization), evenness/symmetry, `Q+tP` covariance CS → square CS for smooth `f,h`;
3. density + Lebesgue-a.e. convergence transferred to `ν`-a.e. (PROOF135), then **Fatou as an inequality only** (upper bound with `R₀N²N²`), with the explicit statement “At this stage Fatou supplies an inequality, not continuity”;
4. ordinary `ν`-Cauchy–Schwarz → four-linear bound, absolute convergence, multilinearity;
5. **telescoping continuity** of `A_sp` and the square pairings;
6. only then PSD extension to finite linear combinations of `H¹` squares, and its two-profile Cauchy–Schwarz.

Continuity is established in step 5 by telescoping, not by Fatou. The source's order is correct; my Noncritical finding 5 is retracted.

### Concrete check 4 — `K_star(0)=0` and null-set transfer: **my note is redundant exposition, not a defect**

- The source already states, at `E:occupation-damped-kernel`: “and set `K_star(0)=0` for time integration” (packet line 333). The divergent pointwise limit is explicitly avoided by this convention, and it is immaterial because the diagonal is a `ν`/product null set. My Noncritical note 3 is withdrawn as redundant; the source is not defective.
- The Tonelli null-transfer in PROOF135 does not manipulate an undefined `0·∞` product. For a Lebesgue-null Borel set `N`:
  - `ν{x∈N} = ∫Γ(dy)∫1_N(x)dx = ∫Γ(dy)·0 = 0` (integrate `x` first);
  - `ν{x−y∈N} = ∫dx∫Γ(dy)1_N(x−y) = ∫dx·0 = 0` (each fixed translate of `N` is null).
  Either order gives a legitimate zero integrand; no product of measures is formed.
- The white `α=d=1` case is included in the positive-radius homogeneity argument in the sense relevant here: `Γ(B_r)=r^{d−α}Γ(B₁)=Γ(B₁)>0` for every `r>0`, so “every origin-centered ball has positive `Γ` mass” holds with exponent 0, and check 2's binding constant `C_z>0` also carries over to `α=d=1`.

---

## OCC01–OCC12 named determinations

| ID | Determination | Coverage and limits |
|---|---|---|
| **OCC01** | **PASS** | σ-finiteness of `dx⊗Γ(dy)` by exhausting balls; representative independence and a.e.-transfer at both `x` and `x−y`; argument is purely Radon-measure-theoretic, so singular `Γ` (white `δ₀`, hyperplane-supported, anisotropic) is covered without a density. Checked directly in PROOF135. |
| **OCC02** | **PASS** (with named imports) | `f_n` cutoff sequence smooth/nondecreasing, `k_n↑1` (uses `E:temporal-equilibrium-potential`), monotone-convergence score limit, raw cost → `M_aB_Γ(z,z)` (uses `E:temporal-equilibrium-mass`), no monotonic score assertion; positivity/Lipschitz of `λ_z(c)` now independently verified via the all-model `ψ_L` binding (check 2). Not re-derived here: the exactness of the equilibrium potential/mass identities and the `χ` cutoff of `P:variational-remove-mask`; both spot-checked against the supplied packet. |
| **OCC03** | **PASS** | Dilation `A_sp(ℓ^{d/2}g(ℓx))=ℓ^αA`, `b=ℓ²b` (`ℓ^{2d}·ℓ^{−d}·ℓ^{α−d}`); `b(g)>0` for nonzero `H¹`/smooth profiles via Fourier-supported-at-zero; positive finite smooth autocorrelation; exact `L−CL^q` optimization with `u=α/q`, `1+u=4/q`, final `8M_a q^{q/2}`. `M_a` is an external input, named. |
| **OCC04** | **PASS** (non-circularity verified; upstream finiteness external) | `R₀`'s finiteness comes from `E:spatial-smooth-score` inverted against the already-finite `S1^pos` (positivity via a normalized compact bump), strictly before PROOF138 and without using the rough extension or the intrinsic theorem. The finiteness of `S1^pos` itself is upstream: original lower (`P:raw-block-original-lower`) plus the independent old `T:full-upper`. That upstream chain is not re-derived in this seven-proof audit. |
| **OCC05** | **PASS** | `B_Γ(Q,Q)=∫|Q̂_ord(ξ)|²μ(dξ)` checked against the model convention `Γ=∫e^{iξx}μ(dξ)` (no stray `2π`); smooth PSD/CS; `H¹` density; transferred a.e. convergence; **Fatou kept as inequality**, not continuity; exponents of `N(f)=‖f‖₂^{1−α/4}‖∇f‖₂^{α/4}` all positive (`α<2`) and dilation-consistent. |
| **OCC06** | **PASS** | Order verified: Fatou inequality → `ν`-Cauchy–Schwarz giving the absolutely convergent `C₄` bound → telescoping joint continuity → PSD on finite combinations of `H¹` squares → sharp two-profile CS, `R_sp=R₀` by density/continuity; strict positivity via a measurable `E`, `|f|≥c>0`, continuity of the correlation of `1_E` near 0, an origin ball with positive `Γ`-mass, and explicitly **only** a nonnegative integral — no claim `1_E∈H¹`. |
| **OCC07** | **PASS** | Exact energy `sup_t[t^αA − t²b/2]` via dilation of the unit `H¹` class with `t=1` admissible; maximizer `t^{2−α}=αA/b`; coefficient `((2−α)/2)α^{α/(2−α)}`; two suprema exchanged without an assumed optimizer; scalar `F₀` and `M_a^{−1/k}F₀(E_sp)`; positivity/finiteness/full-`H¹` scope from OCC04 and PROOF138. |
| **OCC08** | **PASS** | `K_star` even, positive, decreasing, locally integrable (`a<1`); `K_star≤|u|^{−a}` by dropping `λ²|u|/(2D)`; `Φ` concave by decreasing integrand; row `Φ(s)+Φ(1−s)≤2Φ(1/2)` with equality at `1/2`; diagonal irrelevant (`K_star(0)=0` convention); **`D=q−2a=(4−α)−2α₀>0`** since `α<2` and `2α₀<2`. |
| **OCC09** | **PASS** | Measurability of `s↦b(g_s)`; `∫‖g_s‖_{H¹}²ds=1+T(g)`; separably-valued representative; simple-`H¹` approximation with summable `L²(0,1;H¹)` errors; measurable spatial versions; a.e. representative reconciliation via PROOF135; pairing measurability by continuity on `H¹×H¹`; product-null changes alter nothing. No time smoothness or common compact support imposed. |
| **OCC10** | **PASS** | `B_Γ(g_s²,g_t²)≤R_spF(s)F(t)`, `∫F²≤T^{α/2}` (concavity, `0<α/2<1`), `2F(s)F(t)≤F²+F²`, row/column `R_star` → `J≤R_starR_spT^{α/2}`; scalar maximum equals `R_star^{2/(2−α)}E_sp`; positivity via constant-in-time `U_ℓ` profile, `J=J₀ℓ^αA_sp`, `T=ℓ²b`, `α<2` ⇒ positive for small `ℓ`; zero covariance/free case via dilation, **no** zero-gradient unit profile, **no** optimizer/equality claimed. |
| **OCC11** | **PASS** (in-scope scalar checks; consumer-only items recorded, not re-proved) | In the seven proofs: signed profiles are handled through their squares (PROOF138); zero profile/zero covariance through `R_sp=0` and dilations (PROOF141) with the free case; constant-in-time trial for positivity (PROOF141); normalization/amplitude retained throughout (`F₀` labels the scalar map; kinetic coefficient is `−b/2` and `−T/2`). The generic falsification consumers — white `d=1` numerical evaluation (`E_sp=c²/6`, `(2/3)√(c/M_a)≤C₂≤(2/3)√(cK₀)`), `α=1` and `1<α<2−α₀` cases, singular anisotropy — are **outside** these seven proofs (white evaluation / earlier sections); their formulas were only spot-checked for consistency, not re-proved here. |
| **OCC12** | **PASS** (ledger completed below) | Every named dependency is either verified in the seven proofs or explicitly recorded as an unrederived external input. No arbitrary spatial point trace (PROOF138 refuses `1_E∈H¹`; PROOF141 integrates pairings, no point evaluation); no raw-Hilbert mask; no Skorohod argument; no temporal-limit interchange (only monotone/Fatou on finite horizon); no forced author constant (`M_a` re-derived from the supplied equilibrium; covariance amplitude preserved). **Not cleared here as scoped out:** the whole-213-proof goal, source-image/fullmain/cold/wholegoal gates, and any cross-file “final whole-argument” clearance. Correctness repairs inside this scope vs. prose are distinguished below. |

---

## Seven-proof status ledger

| Proof | Status | Owner OCC | Internal coverage | Unrederived externals named |
|---|---|---|---|---|
| **PROOF135** (`L:spatial-physical-pair`) | **CHECKED** | OCC01 | σ-finite product; null-transfer at `x`,`x−y`; completion/representative independence; singular `Γ` covered measure-theoretically. | none for its own claim |
| **PROOF136** (`L:spatial-static-controls`) | **NOT_FULLY_CHECKED** (internal chain correct; externals not re-derived) | OCC02 | cutoff `f_n↑f_a`, `k_n↑1`; mean `k_n(s)U_z`; rate `λ_z(k_n(s))`; `I_{Ψ_n}→λ_z(1)`; cost `→M_aB_Γ(z,z)`; no monotone score assertion; positivity/Lipschitz now verified via `ψ_L` binding. | exact `∫|s−t|^{−a}f_a=1` and `M_a` formula (temporal file); unmasked Rayleigh boundedness/positivity (`P:variational-unmasked-rate`); `χ` cutoff (`P:variational-remove-mask`) |
| **PROOF137** (`P:spatial-smooth-ratio`) | **NOT_FULLY_CHECKED** (internal correct; externals named) | OCC03/OCC04 | `b(g)>0`; positive finite smooth `A_sp`; dilation; exact optimization constant; `R₀` positive and finite **before** rough extension (non-circular). | `M_a`; finiteness/positivity of `S1^pos` (upstream `P:raw-block-original-lower` + `T:full-upper`) |
| **PROOF138** (`P:spatial-four-linear`) | **CHECKED** | OCC05/OCC06 | Fourier normalization; smooth PSD/CS; density/Fatou (inequality only); four-linear CS/absolute convergence; telescoping continuity; PSD extension and sharp CS; `R_sp=R₀`; strict positivity via `1_E` correlation without `H¹` claim. | `R₀` (from 137); PROOF135 transfer |
| **PROOF139** (`P:spatial-energy-map`) | **CHECKED** | OCC07 | dilation energy; exact constant; two-sup exchange without optimizer; `F₀`; `M_a^{−1/k}F₀(E_sp)`. | 137/138 for `R_sp` and `H¹` dilation extension; `M_a` |
| **PROOF140** (`L:occupation-kernel-row`) | **CHECKED** | OCC08 | `K_star≤|u|^{−a}`; parity/monotonicity/local integrability; concavity row maximum `R_star`; `D>0`; diagonal convention. | Euler `Γ_E(a)` normalization (standard) |
| **PROOF141** (`P:occupation-physical-class`) | **CHECKED** | OCC09/OCC10 | measurability/representatives; Schur/concavity bound; scalar energy upper; small-dilation positivity; zero-covariance free case; no optimizer/equality. | 135/138 (pairings, `R_sp`); 140 (`R_star`); 139 (`E_sp`) |

---

## Honest corrected verdict

- **verdict: PASS_WITH_NOTES** (unchanged). No mathematical defect found in PROOF135–141; the four submission checks confirm the manuscript is correct where my original report was imprecise.
- **confidence: HIGH** for the internal proof chains, signs, scaling, and final coefficients inside the seven proofs; the only residual uncertainty is the explicitly named upstream external inputs (equilibrium identities, unmasked Rayleigh machinery, `S1^pos` finiteness via the independent full-upper), which were spot-checked from the supplied packet but are not re-proved inside this seven-proof scope.

## One-line summary

PROOF135–141 remain correct — with the four corrected points confirming the source (pointwise `c‖U_z‖_∞` vs. the `‖U_z‖_∞` Lipschitz constant; all-model `ψ_L` binding for positivity at every `c>0`; nonnegative-integrand cross positivity followed by the Fatou-then-continuity-then-PSD order; and the explicit `K_star(0)=0` convention) — and the named OCC01–OCC12 ledger is now complete with three of my four original noncritical notes retracted as imprecise/redundant and the seven-proof statuses CHECKED/NOT_FULLY_CHECKED assigned per verified vs. unrederived upstream dependencies.