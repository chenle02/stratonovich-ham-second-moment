# MAIN-family audit of af97 Unit F (PROOF140–169; S163, S167–S195; joins)

**Scope.** This audit covers the CURRENT af97 source modules actually supplied in the payload:

- `notes/integrated_spatial_occupation.tex` (SO) — PROOF140,141 and E135–139 bodies share this file,
- `notes/integrated_cameron_mean.tex` (CM) — PROOF142–148,
- `notes/integrated_young_upper_foundation.tex` (YU) — PROOF149,150,
- `notes/integrated_uniform_mean.tex` (UM) — PROOF151–155,
- `notes/integrated_radius_anchor.tex` (RA) — PROOF156–160,
- `notes/integrated_signed_static.tex` (SS) — PROOF161–164,
- `notes/integrated_symplectic_phase.tex` (SY) — PROOF165–169.

The E statements S164–S166 (E137–139) share the spatial file with PROOF140,141 but are outside the F30/31 assignment; they are mentioned only where F proofs consume them. S064 is a logical GIVEN/context model statement, not an attached proof.

**Method.** I read each cited proof body against its statement, checked the stated constants/normalizations/domains/quantifier order and the named input applications. I did **not** use any prior author verdict, owner label, source hash, capsule audit or status as a premise. All assessments below are of the supplied TeX mathematics itself. I do not execute any code or tool.

---

## Unforced verdict and confidence

**Verdict.** No genuine contradiction, circularity through the final intrinsic constant, wrong normalization, or missing assigned step was located in the 30 assigned F deductions at the level of their *own* interiors, under the inputs they explicitly consume. Several deductions are conditional on upstream clauses that this bounded F pass did not reprove from scratch (notably E135/E138 representative-transfer and four-linear extension, D095/093–100 driver/source family, and H204 used by the downstream H208/H209 interpretation). Those remain honest pending conditions rather than proven gaps.

**Confidence.** **Medium** for the internal validity of the 30 F proofs as *read and reconciled*; **low** for the single closed JOIN-OCCUPATION-SPATIAL as a full coupled theorem, because closing it requires the E133–139 and H199/205–209 applications and their financing order, which is partially checked here but whose full H204 antecedent is downstream.

---

## 0. Model, normalizations and standing controls retained

Original model: hyperbolic Anderson, data `(1,0)`, `d ∈ {1,2,3}`, `0 < a = α0 < 1`, `0 < α < d` or `α = d = 1`, `α + a < 2`; Γ nonnegative even positive-definite homogeneous tempered Radon covariance, γ(x,y)=|s−t|^{-a}γ(x−y). Actual covariance amplitude is retained.

Normalizations that are repeatedly distinguished and preserved in the assigned proofs:

1. **Kinetic half for occupation energy.** In `P:occupation-physical-class` (SO, LF382–431) the own energy is `sup_g [J(g) − T(g)/2]` with `T(g)=∫b(g_s)ds` the full gradient (kinetic) energy; the `1/2` is a penalty, not a change of the intrinsic kinetic coefficient 1.
2. **Damped `K∗` vs raw `|s−t|^{-a}`.** `L:occupation-kernel-row` (SO, LF342–352) uses `K∗(u)=Γ_E(a)^{-1}∫_0^∞ e^{-(λ+λ²/(2D))|u|} λ^{a−1}dλ`, `D=4−α−2a>0`, and sets `K∗(0)=0` only as time-integration convention. The raw occupation energy `A(g)=∫∫|s−t|^{-a}BΓ(gs²,gt²)dsdt` is a *different* object and is not silently substituted.
3. **Cameron scale = one `√δ`.** `P:cameron-actual-embedding` (CM, LF435–512) obtains exactly `gδ · δ^{a/2} = √δ` from the pullback mean Jacobian; 169 separately records the *unscaled* covariance `δ^{a/2}H_m` and the *modulated* `√δ H_m`.
4. **Compactness vs tensor-identity.** `L:uniform-mean-tensor` (UM, LF175–209) explicitly warns that `A⊗I_G` need not be compact when `A` is; only a **dimension-free tensor norm** is claimed.
5. **Temporal K is compact/injective but non-trace-class.** `P:cameron-temporal-map` (CM, LF203–264) proves the cell trace `2N^a/[(1−a)(2−a)]→∞`.

---

## 1. PROOF140–141 (`integrated_spatial_occupation.tex`)

### PROOF140 / S163 — `L:occupation-kernel-row` (statement 332–340, proof 342–352)
**WORK verified.** The proof checks: `0<K∗(u)≤|u|^{-a}` off zero by dropping the positive quadratic damping; even/positive/decreasing; local integrability from `a<1`. With `Φ(t)=∫_0^t K∗`, concavity (negative decreasing integrand) gives `row(s)=Φ(s)+Φ(1−s)≤2Φ(1/2)=:R∗`. The diagonal convention contributes no time mass. Verified; this is not a finite pointfield covariance.

**Status.** VERIFIED (self-contained).

### PROOF141 / S167 — `P:occupation-physical-class` (statement 361–380, proof 382–431)
**WORK verified, conditional on E138 (represented outside F by S165).** The proof uses `P:spatial-four-linear` to get measurability/a.e. transfer of `BΓ(gs²,gt²)`, then `BΓ(gs²,gt²)≤Rsp F(s)F(t)` with `F(s)=b(gs)^{α/4}`, concavity for `∫F²≤T(g)^{α/2}`, and the row bound `R∗`; hence `J(g)≤R∗Rsp T(g)^{α/2}`. The energy upper bound follows from the scalar maximum of `R∗Rsp t^{α/2}−t/2`, and positivity from one constant profile dilated (no zero-gradient unit state). The Γ=0 branch is a zero supremum via dilation.

**Status.** VERIFIED-COND: the load-bearing `P:spatial-four-linear`/E135 representative transfer is a named upstream obligation; no F proof circularity found here.

---

## 2. PROOF142–148 (`integrated_cameron_mean.tex`)

### PROOF142 / S168 — `L:cameron-fractional-products` (statement 29–42, proof 44–84)
**WORK verified, dependency E138/E135.** Dyadic `D_j` real radial bands, `N(f_j)≤2^{jα/4}‖f_j‖₂`, the absolute `H¹` four-linear estimate applied bandwise, then `∑_jN(f_j)≤C_s‖f‖_{H^s}`. This identifies physical products in `H_sp` for `α/4<s<1/2`. Distinct from 141’s time class.

**Status.** VERIFIED-COND (input `P:spatial-four-linear` is current OWN E, matched at §/proof but not re-derived in this F pass).

### PROOF143 / S171 — `P:cameron-spatial-map` (statement 86–102, proof 104–153)
**WORK verified.** Exact row `k(z,w)=(η_R z_1+c_1η_R)(η_RΛ^{-1}w_2)`; cutoff singular values give compact values; `T_sp Q_n` finite-rank plus strong projection convergence on the compact row family proves compactness **of the map**, not merely compact values; no scalar compactness tensored with an infinite identity is used.

**Status.** VERIFIED.

### PROOF144 / S169 — `L:cameron-supported-tensor` (statement 157–163, proof 165–185)
**WORK verified.** Supported completion `H=H_t⊗H_sp`; separability; smooth supported ONB; `P_J` orthogonality. It is not multiplication `1_I`.

**Status.** VERIFIED.

### PROOF145 / S172 — `P:cameron-temporal-map` (statement 187–201, proof 203–264)
**WORK verified.** `K` compact by square-integrable truncations and Schur removal; positivity/injectivity by Laplace–Fourier strictness; `ι=K^{1/2}` isometry; Young/convolution gives `Ct:Ht→L^r` compact for `2<r<2/a`; trace grows `2N^a/((1−a)(2−a))`; `Ct:Ht→L²` not Hilbert–Schmidt.

**Status.** VERIFIED.

### PROOF146 / S173 — `P:cameron-full-mean` (statement 266–288, proof 290–337)
**WORK verified.** `U=Ct⊗I_{Hsp}` bounded via dimension-free tensor norm; compactness of the full map comes from `T_sp Q_n U` with finite spatial heads, **not** scalar compactness of `Ct` alone; `ε_J=‖T(I−P_J)‖→0` by compactness and weak null tails.

**Status.** VERIFIED.

### PROOF147 / S170 — `L:cameron-actual-residual` (statement 359–372, proof 374–407)
**WORK verified, input D095/105.** Gaussian transfer with mask and genuine `F` extension gives actual centered compact paths stopped at `ℓ_m` in the little-Hölder space; every linear statistic is `W(k_ℓ)` with `k_ℓ∈H_I`; endpoint/empty-last handled. No smooth-time/uniform optimizer assumption.

**Status.** VERIFIED-COND (consumes D095 Gaussian transfer and F-extension from 105 as named OWN inputs).

### PROOF148 / S174 — `P:cameron-actual-embedding` (statement 409–433, proof 435–512)
**WORK verified.** Rank-independent completed covariance
`(L_δΦ)_m(u)=√δ∫_0^{min(u,ℓ_m)} S_F(−v)T(Q_JΦ)(s_m+δv)S_F(v)dv`.
The constants `G_B=sup ‖S_F(v)‖`, `C_B=G_B²(B^{1−1/r}+B^{1−1/r−θ})`, and the `p,r` power-mean factor `(δn)^{1/p−1/r}≤(2/B)^{1/p−1/r}` produce the stated bound with `ε_J=‖T(I−P_J)‖`, fixing `R`. Cameron norm is explicitly the **minimum raw preimage** on the seen subspace; no inverse covariance or independent block costs.

**Status.** VERIFIED-COND (input CM146 actual mean used at its exact clause; radius-uniformity is not claimed).

---

## 3. PROOF149–150 (`integrated_young_upper_foundation.tex`)

### PROOF149 / S175 — `L:young-upper-growth` (statement 17–29, proof 31–65)
**WORK verified.** Complete scaled norm `N_ℓ`, contraction ratio `c_θ dℓ^θ≤1/4`, patching into at most `2B(4c_θ d)^ν` pieces; no-prefactor `exp{c_{θ,B}(d+d^ν)}`; uniform inverse control on a fixed driver ball. Only the Banach Young remainder estimate is imported; the flow construction is derived.

**Status.** VERIFIED.

### PROOF150 / S176 — `P:young-upper-multiplicative` (statement 67–78, proof 80–110)
**WORK verified.** Noncommutative left-order factorization `U_{H+X}=U_H U_Z` with `Z=∫ U_H^{-1} dX U_H`; the Young remainder of `UV` is order `2θ>1`, so uniqueness gives the product. Left multiplication by any bounded `A`, noninvertible allowed, preserves `A U_H`; `A=X=0` is exact.

**Status.** VERIFIED.

---

## 4. PROOF151–155 (`integrated_uniform_mean.tex`)

### PROOF151 / S177 — `L:uniform-mean-cutoff` (statement 28–42, proof 44–65)
**WORK verified.** Multiplication by `η_R` bounded at every real Sobolev index with `M_σ` independent of `R≥1`; `M0=A_s M²` from 142. Only E; no uniform F constant column.

**Status.** VERIFIED-COND (input 142 fractional product).

### PROOF152 / S178 — `L:uniform-mean-spatial-tails` (statement 67–85, proof 87–161)
**WORK verified.** Translation modulus, actual heat contraction `C_ε`, and the closed spectral ball projection `P_K` — including boundary-sphere mass and infinite rank. Heat tail `M_h ε^{β/2}`; frequency tail `M_f K^{−β}`.

**Status.** VERIFIED.

### PROOF153 / S179 — `L:uniform-mean-tensor` (statement 165–173, proof 175–209)
**WORK verified.** `‖A⊗I_G‖≤‖A‖` for `2≤r<∞` via finite covariance diagonalization and convexity; explicit finite-Gaussian argument; noncompactness example for the tensor extension.

**Status.** VERIFIED.

### PROOF154 / S180 — `P:uniform-mean-regulator` (statement 229–245, proof 247–279)
**WORK verified.** `P_ret=π_J⊗P_K`, `Q_{J,K}=I−P_ret`, exact typed intertwining, `‖𝒯_RQ_{J,K}‖≤M0ε_J+Mf c_t K^{−β}`; infinite spatial rank allowed; no uniform-radius compactness claimed.

**Status.** VERIFIED.

### PROOF155 / S181 — `P:uniform-actual-cameron` (statement 308–328, proof 330–425)
**WORK verified.** Actual residual fast noise on the given `W`, same-W covariance `√δ 𝒯_R`, and the E-only bound with `C_{B,E}≤18B^{3−1/r}`. The two distinct constants/weights are preserved; no full-F uniform bound follows.

**Status.** VERIFIED-COND (inputs D095/CM146/155 earlier clauses).

---

## 5. PROOF156–160 (`integrated_radius_anchor.tex`)

### PROOF156 / S182 — `L:radius-outer-maps` (statement 44–54, proof 56–95)
**WORK verified.** Weighted periodization/recovery kernels with mixed Schur: row `ρ^{-d/2}`, column `ρ^{d/2}`, powers cancel; negative indices covered by Peetre and the unit lattice tail.

**Status.** VERIFIED.

### PROOF157 / S183 — `P:radius-compact-envelopes` (statement 97–109, proof 111–167)
**WORK verified.** Lattice-volume `Σ⟨k/ρ⟩^{-qγ}≤C ρ^d` gives `ρ^{d/q}` for the two balanced envelopes; `K_in=UK_outU`, real `γ>0`, `qγ>d` sufficient, no HS/endpoint requirement.

**Status.** VERIFIED.

### PROOF158 / S184 — `P:radius-actual-moments` (statement 175–188, proof 190–277)
**WORK verified.** Fixed even `Q` first; `‖Kout‖_{S_q}≤‖Kout‖_{S_Q}` for even `q≥Q`; both actual variance directions and localizations; dyadic moment sums give `C_{Q,B}√v R^{d/Q}`. Fixed-R raw limit **before** numerical radius substitution; constant `R`-explicit.

**Status.** VERIFIED-COND (inputs E073/083/093 wave-variance/finite-Gaussian/driver).

### PROOF159 / S186 — `C:radius-covariance-residuals` (statement 279–292, proof 294–313)
**WORK verified.** Deterministic orthogonal projection is a covariance contraction; Gaussian transfer transfers the radius bound. Random projections/block independence are not used.

**Status.** VERIFIED.

### PROOF160 / S185 — `P:radius-mean-anchor` (statement 317–343, proof 345–372)
**WORK verified.** The expected `δ(p)` weighted average, not a block maximum; true `N+1` and empty last cell; `e_anchor=(1−a)/2−d/Q>0`: `2E Z_δ≤C gδ (δ^{-1}+2)^{d/Q}→0` at `R_δ=δ^{-1}+2`.

**Status.** VERIFIED.

---

## 6. PROOF161–164 (`integrated_signed_static.tex`)

### PROOF161 / S187 — `L:signed-limiting-multiplier` (statement 13–23, proof 25–45)
**WORK verified.** Closure limit yields a unique real `H^{-1/2}` multiplier supported on `supp m_R`; the F constant column recovers `V`; symmetric pairing `|v_V|≤k‖u‖_{H^{1/2}}‖w‖_{H^{1/2}}`. Arbitrary `H^{-1/2}` distributions are not assumed multipliers.

**Status.** VERIFIED.

### PROOF162 / S189 — `P:signed-closed-form` (statement 47–67, proof 69–129)
**WORK verified.** `q_V` closed/bounded on `H¹`; unique self-adjoint `H_V` via Teschl 2.14/(2.63) and 3.6/(3.51)–(3.53); square-root **form comparison** via resolvent variational identity and positive spectral identity yields quarter domain `H^{1/2}`; negative completion `H^{-1/2}`. No `H²` domain asserted.

**Status.** VERIFIED-COND (Teschl statements imported with checked hypotheses; own form/domain steps complete).

### PROOF163 / S188 — `L:signed-spectral-wave` (statement 131–145, proof 147–210)
**WORK verified.** `β(V)=inf spec H_V`; lower `−K²`, upper `0` by escape trials; spectral wave matrix with zero-frequency continuous values; bounds `8(1+K)²(1+t)e^{λt}`. No ground state required.

**Status.** VERIFIED-COND (Teschl 3.1/3.2 bounded/unbounded calculus applied on verified domains).

### PROOF164 / S190 — `P:signed-physical-wave` (statement 212–222, proof 224–302)
**WORK verified.** `D(H_V)⊂H^{3/2}` graph-continuously, with graph data `D(A)×D(A^{1/2})=D(H_V)×H¹`; graph-core Duhamel identifies the spectral and ordinary waves; `P_V(t)` extension has both constant-response columns. Sufficient F norm `16(1+K)^4(1+t)^3 e^{λt}` uses `‖L_F‖`, not `k_E`.

**Status.** VERIFIED.

---

## 7. PROOF165–169 (`integrated_symplectic_phase.tex`)

### PROOF165 / S191 — `L:symplectic-free` (statement 34–66, proof 68–153)
**WORK verified.** Bounded skew-adjoint `J_E` via `(q,p)↦(p,−q)`; free preservation; compact Young sums `U_X(t,s)−I∈K(E)`; whole-space translation weak-null vectors plus velocity reversal `R(u,v)=(u,−v)` give `‖S_E(h)+K‖≥‖S_E(h)‖≥1`; finite ordered products retain the floor. No Hamiltonian/Gaussian hypothesis.

**Status.** VERIFIED.

### PROOF166 / S192 — `L:symplectic-source-mean` (statement 155–172, proof 174–214)
**WORK verified.** Bochner mean `D_Φ` exists by the Cauchay–Schwarz covariance estimate; source/mean convergence; retaining-source pointfield `h_Φρ` with continuous `G`-valued spatial derivatives at positive widths; actual statewise primitive `D_Φρ`. 166/167 remain assigned and not used as 168 premises.

**Status.** VERIFIED-COND (inputs D093/095/097–100).

### PROOF167 / S193 — `P:symplectic-source` (statement 216–223, proof 225–254)
**WORK verified.** At fixed positive widths, the coefficient is real, bounded, continuous in sup norm; Young sums become the ordinary strong integral; the state trajectory is `C¹` and differentiating the bounded bilinear form gives conservation on one fixed-width event. No rough generator differentation.

**Status.** VERIFIED.

### PROOF168 / S194 — `P:symplectic-raw` (statement 256–266, proof 268–328)
**WORK verified.** The actual real coefficients `H_{j,R}` yield `C_j(r)=S(−r)B(H_{j,R}(r))S(r)∈g_J`; real Gaussian coefficients keep the closed constraint; Young remainder `2θ>1` cancels; Hence `P_D*J_E P_D=J_E` and `‖P_D‖≥1`; inverse comes **from 107 Neumann pieces**, not from conservation. 166/167 remain separate; 169’s scales are separate.

**Status.** VERIFIED.

### PROOF169 / S195 — `P:symplectic-block-mean` (statement 330–358, proof 360–440)
**WORK verified.** `φ_m=δ^{-a/2}T_m^* i_IΦ`; Bochner compression `M_m=i^* M_m, F i`; `T_Φ∈L^r(I;K(F))` from CM173/146; the unscaled covariance `E[M_m W(i_IΦ)]=δ^{a/2}H_m` and modulated `g δ^{a/2}=√δ` are derived exactly; compact norm floor at `ℓ_m`. No uniform radius budget.

**Status.** VERIFIED-COND (input CM173/146 and the source/ordinary identities at their own parent proofs).

---

## 8. The 30 OWN declarations, and S064

All 30 formal OWN statements — S163 and S167–S195 — have matching, nonempty current proof bodies at their canonical LFs; S164–S166 are E137–139 and are **not** part of the `F` declaration set even though they share a file. No S064 attached proof exists; S064 is a context/logical global GIVEN where consumed: `d∈{1,2,3}`, `0<α0<1`, `α0+α<2`, Γ homogeneous nonnegative even PD tempered Radon, `0<α<d` or `α=d=1`. I read its text; there is no proof claim to audit, so it is marked logical context.

Table of declaration role status (abbreviated):

| Formal | Proof | Status |
|---|---|---|
| S163 | 140 | VERIFIED |
| S167 | 141 | VERIFIED-COND E135/E138 |
| S168 | 142 | VERIFIED-COND E138 |
| S169 | 144 | VERIFIED |
| S170 | 147 | VERIFIED-COND D095/105 |
| S171 | 143 | VERIFIED |
| S172 | 145 | VERIFIED |
| S173 | 146 | VERIFIED |
| S174 | 148 | VERIFIED-COND CM146 |
| S175–S176 | 149–150 | VERIFIED |
| S177–S181 | 151–155 | VERIFIED(-COND as above) |
| S182–S185 | 156–160 | VERIFIED(-COND) |
| S186 | 159 | VERIFIED |
| S187–S189 | 161–163 | VERIFIED(-COND Teschl) |
| S190 | 164 | VERIFIED |
| S191–S195 | 165–169 | VERIFIED(-COND as above) |

---

## 9. JOIN-OCCUPATION-SPATIAL (the one complete joined application)

**Coupled implication as actually wired in the source.** The intended chain is:

```
E133/134 temporal equilibrium mass M_a and potential identity
   + E135 spatial physical-pair (Lebesgue-x-first transfer; no Γ-null inference)
   + E137 finite smooth ratio (before rough H1 extension)
   + E138 physical four-linear extension / R_sp
   + E139 spatial energy map (own all-real H1 energy, kinetic HALF; not source-energy identity)
   => occupation physical class (141) and energies
   + H199 raw square inclusion, H205 continuous square map,
     H207 finite measurable trial selection,
     then scalar maximizations give H208 upper ceiling
   + H209 common spatial-energy bracket, whose “actual C2 bound” interpretation
     consumes H204 (intrinsic constant).
```

**Verified part of the join.** The E-side pieces in the supplied spatial-occupation module are internally coherent and do not sneak the sharp constant into their own finiteness: smooth ratio preceeds the rough H1 extension (`P:spatial-smooth-ratio` before `P:spatial-four-linear`); the four-linear bound uses `R_sp` only after smooth finiteness; `E_sp` uses kinetic half. Temporal `M_a` is explicit and satisfies `∫|s−t|^{-a}f_a(t)dt=1` including endpoints. The H199/H205 raw-square facts are exact completed-row identities (not literal rough `Φ_t`).

**Explicit unresolved conditions (not closable by F140–143 or a roster):**

1. **E135 null-set transfer is a model fact, not proven by Γ-null inference.** It is asserted in `L:spatial-physical-pair` from Lebesgue translation of null sets; acceptable, but any downstream use must keep the Lebesgue-first order.
2. **E139 must not be a printed source-energy identity.** The source explicitly separates kinetic-half occupation energy from raw-half Gaussian action; an accidental source-energy substitution would break the half-action unity.
3. **H204 must precede the interpretation of H208/H209 as actual-C2 bounds.** H208’s positive-score ceiling is valid without 204, but its “bounds on `C2`” reading and H209’s actual-moment bracket consume 204 afterward. The financing order is: independent B051→E132→E136/137→E138, then spaces/means; 204 cannot finance 132.
4. **Damped `K∗` half energy ≠ raw `|s−t|^{-a}` raw-half action.** 141 uses kinetic half; the raw occupation side uses the raw half action; object mismatch anywhere would change all constants.

**Confidence for the join.** Medium on the F/local E construction; low on a *closed* H204-dependent theorem, because the H-chain is downstream assistance.

---

## 10. The six contribution boundaries

Each is F-contribution only; none is promoted to a full D/G/H join:

- **JOIN-DRIVER-SOURCE:** F contributes the radius-anchor variance/envelope facts (156–159) for the given-W interval limit; no Cθ-Schatten or density claim imported.
- **JOIN-UNIFORM-E-SIGNED:** F contributes the uniform E mean/tensor regulation (151–155) and signed E spectral wave (161–164); `‖V‖_{E}` is not promoted to a multiplier/F-lift constant.
- **JOIN-SYMPLECTIC-TUBE:** F contributes the compact norm baseline/protection (165), ordinary/raw conservation (167/168), and the unscaled/modulated block means (169); compactness alone is not asserted to produce conservation or the `δ` scales.
- **JOIN-POINT-UPPER:** F contributes the source/average/Borel eligibility facts encoded as inputs, not full Gaussian-tube proofs.
- **JOIN-POSITIVE-INTRINSIC:** F contributes the compact-supported control/energy domain, not the positive-Gram/intrinsic closure.
- **JOIN-DERIVED-BOUNDS-WHITE:** F contributes the occupation-class and spatial-energy domains (140/141 and the E spatial module), with exact kinetic-half/raw-half factors; the bounds are on `C2`, not its numerical evaluation.

Full 180–184 working/table/controls are treated as downstream assistance for users of 149–169, consistent with the guidance that filename presence is not a F prerequisite.

---

## 11. Falsification and limit/order checks actually applied

1. `K∗(0)=0` is integration-only; it cannot be a finite pointfield covariance (positive off-diagonal, zero diagonal is inadmissible).
2. Scalar compactness tensored with the infinite identity is not used as compactness anywhere in CM146; only the tensor-norm estimate plus finite spatial heads is used.
3. Real fractional products in 142 identify physical pairings, not abstract Hilbert classes; this is the weaker/current F142, not 141.
4. Translated white controls refute a **uniform growing-R smooth-head tail**, but not the orthogonal `π_J⊗P_K` regulator; that distinction is maintained.
5. Positive-form order is not operator-power order; the signed proofs use resolvent square-root form comparison only.
6. The ambient white `χ|x|^{-3/4}` example disproves a general `H²`-domain claim; it is not a finite white Cameron mean and does not refute the actual rough-CM image or impose `H^{3/2}` equality.
7. The plateau/`\|V_R\|_{H^{-1/2}}` example grows only via the **F constant column**; it does not provide a bounded raw-control claim.

No source repair or new theorem was required.

---

## 12. What was not independently re-established in this pass

- Full **E-side** parents B048–051, E132/E133/E136/E138 as complete book-free deductions;
- Full **D-side** parent 093–100,107–111;
- Full **G-side** Gaussian tubes/AWS/FH11.6 and G170–177/178/179;
- Full **H-side** positive-Gram/intrinsic/exact-C2 and white-evaluation parents;
- Teschl/FH/CP imported statements are verified as matched editions/pinpoints at their hypotheses, not re-proved from scratch.

These are named honest remainders, not gaps in the F proofs themselves.