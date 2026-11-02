# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

Verdict applies to the four scoped proofs PROOF161–164 only (`integrated_signed_static.tex`, packet lines 4–305 = original LF 1–302). No whole-paper, source-image, cold, novelty, Skorohod, release, or claim clearance is asserted.

## Critical findings

None. No false identity, hidden hypothesis, incorrect constant, sign error, or invalid asymptotics found in the four proofs. In particular:
- No H² operator-domain assertion (PROOF162 states this negatively, line 69; PROOF164 uses only the one-sided embedding `D(H_V) ↪ H^{3/2}`, line 235, never `D(A^{3/4}) = H^{3/2}`).
- No positivity/ground-state/eigenvalue-at-bottom/essential-spectrum or gap hypothesis is used anywhere (see line 293: "No ground positivity or gap is used").
- The zero branch is handled without division by λ (line 200; λ = 0 case is vacuous for h<0 because β=0 leaves no negative spectrum, and `e^{λt}=1` throughout).
- No final-moment/asymptotic conclusion is claimed.

## Noncritical findings

1. **β ≤ 0 bump construction phrasing (PROOF163, lines 153–156).** "dilate a unit compact smooth bump and translate its whole support outside supp m_R" is compressed. Literal simultaneous dilation and disjointness from a fixed compact mask is not achieved by one translate (dilation enlarges support). The rigorous version, which the scope itself prescribes ("translated dilated test bumps"), places a slowly dilating bump along a ray/half-space disjoint from `supp m_R`, keeping kinetic energy → 0 and L² norm = 1 with zero potential pairing. The intended content is valid; only the prose is loose.

2. **Upper form bound step (PROOF162, line 85).** The passage `(3/2)z²+(1+3K²/2)b² ≤ L_K z²` uses `b ≤ z` without saying so. Explicit: `b² ≤ z²` gives total `(5/2 + 3K²/2)z² ≤ 3(1+K²)z² = L_K z²` for K ≥ 1. Correct, merely implicit.

3. **Cited prerequisites not re-derived inside these four proofs.** Smooth-compact multiplication bounded on every H^r (`L:cutoff-factorization`), norm-continuity of compact conjugation under strong group + strong adjoint (`P:cameron-actual-embedding`), strong continuity of the free group, and the Young/left-Young theory are cited, not re-proven here. Their statement bodies are supplied in the context and are adequate for the citations; I did not audit those bodies as part of this unit.

## Checked derivations

**PROOF161 (closure/multiplier), CHECKED.**
- `‖(0,0,1,0)‖_F = 1`, `(L_{q_n}−L_{q_j})(0,0,1,0) = (0, V_{q_n}−V_{q_j},0,0)`, so `‖V_{q_n}−V_{q_j}‖_{H^{-1/2}} ≤ ‖L_{q_n}−L_{q_j}‖` → Cauchy → `V_{q_n}→V` in H^{-1/2}.
- Support of V lies in `supp m_R`: each `V_{q_n}=m_R(Γ∗q_n)` vanishes off the fixed compact mask; H^{-1/2} test-convergence preserves this.
- Multiplier action: `M_n: u↦V_{q_n}u` converges in `L(H^{1/2},H^{-1/2})` to M with `‖M‖≤k=‖L‖`; smooth-compact multiplication is bounded on H^{-1/2} (cutoff factorization), so `V_{q_n}u→Vu` for test u, hence `Mu=Vu` by density of `C_c^∞ ⊂ H^{1/2}`; Vu is defined through the closure, not as a generic distribution product.
- Uniqueness of V from the unit constant column (norm-one preimage).
- Pairing `v_V(u,w)=⟨V,uw⟩ = ⟨Vu,w⟩_{H^{-1/2},H^{1/2}}` is symmetric; bound `|v_V| ≤ ‖M‖‖u‖‖w‖ ≤ k‖u‖‖w‖` (line 23–24). Complexification preserves norm; Hermitian extension has diagonal = sum of real/imag diagonals.

**PROOF162 (closed form / quarter-power), CHECKED.**
- `‖u‖²_{H^{1/2}} ≤ bz` (Fourier CS). `|v_V(u,u)| ≤ k‖u‖²_{H^{1/2}} ≤ Kbz ≤ z²/2 + K²b²/2` (weighted AM-GM, weights ½,½, bases z²,(Kb)²).
- `q_V = z²−b²−v_V`, `c=2+K²`:
  - lower `q_V+cb² ≥ z²/2 + (1+K²/2)b²` ✓;
  - upper `≤ (3/2)z² + (1+3K²/2)b² ≤ L_K z²`, valid since `b≤z` and `5/2+3K²/2 ≤ 3+3K²`.
- Densely defined Hermitian form on H¹ is closed (shifted norm ≍ complete H¹ norm); Teschl Thm 2.14 (p.81, (2.63), verbatim at embedded page 93) yields unique self-adjoint H_V; shift independence holds.
- `A=H_V+c ≥ 1`: form bound `q_V+c ≥ (1+K²/2)b²+½z² ≥ b²`; the spectral-low-slice contradiction upgrades this to the spectral bound.
- `D(A^{1/2})=H¹` via Teschl 3.6 (3.51)–(3.53) (embedded page 121).
- Quarter power: from `½B₀ ≤ A ≤ L_K B₀` (forms) and the proven square-root order (variational resolvent order + `√x = π^{-1}∫ t^{-1/2} x/(x+t)dt` — substitution t=xv² gives π√x) one gets `2^{-1/4}B₀^{1/4} ≤ A^{1/4} ≤ L_K^{1/4}B₀^{1/4}`, hence `D(A^{1/4})=H^{1/2}`, factors `2^{-1/4}` and `L_K^{1/4}`. No unsupported power-order rule used.
- Negative dual: `sup_u |⟨v,u⟩|/‖A^{1/4}u‖ = ‖A^{-1/4}v‖` (upper by CS; attained by `u=A^{-1/2}v`) → completion = H^{-1/2}.

**PROOF163 (bottom + spectral wave), CHECKED.**
- Unit u, z≥1: `q_V ≥ z²−1−|v_V| ≥ z²/2−1−K²/2 ≥ −(1+K²)/2 ≥ −K²`. ✓
- β ≤ 0 via translated dilated bumps (see noncritical finding 1). Real/complex infima agree by diagonal splitting.
- `inf form = inf spec`: spectral-slice contradiction (spectrum below the form inf would give a unit form test below it) plus `q_V(u)=∫λ dμ_u ≥ inf spec` for unit u; nonempty support/approximate eigenvectors and the bounded off-support resolvent pair `(h−z)^{-1}`, `h/(h−z)` identify spec with PVM support. No discrete-ground/positivity hypothesis.
- `λ=√(−β) ≤ K`; on spec `h+c ≥ −K²+(2+K²) = 2`.
- Matrix (E:signed-spectral-matrix) verified by conjugating `(C_t S_t; −hS_t C_t)` with the A^{1/4} fiber weights: entries `C_t`, `√(h+c)S_t`, `−hS_t/√(h+c)`, `C_t`; correct for h≥0/h=0/h<0 via cos/sin and cosh/sinh derivative identities.
- h≥0 entries: `|C_t|≤1`, `|S_t|≤min(t,h^{-1/2})`, `√(h+c)|S_t| ≤ 1+√c·t` (split `√h ≤/> 1/t`), `|hS_t|/√(h+c) ≤ 1`; zero-frequency off-diagonals `(√c·t, 0)`. h<0: `|C_t|≤e^{λt}`, `|S_t|≤te^{λt}`, `√(h+c)|S_t|≤√c·te^{λt}` (h+c≤c), `|hS_t|/√(h+c) ≤ √(−h)e^{λt} ≤ λe^{λt} ≤ Ke^{λt}` (uses `S_t ≤ e^{λt}/√(−h)`, `h+c≥2`); no division by λ.
- `√c = √(2+K²) ≤ 2K` (K≥1); each entry ≤ `2(1+K)(1+t)e^{λt}`.
- 2×2 operator norm ≤ Frobenius ≤ `2·max entry`; condition cost `M_K² = L_K^{1/2} = √(3(1+K²)) ≤ 2(1+K)` (since `4(1+K)²−(3+3K²)=1+8K+K²>0`). Product: `4(1+K)(1+t)·2(1+K) = 8(1+K)²(1+t)e^{λt}` — EXACT.
- Strong continuity/group from bounded Borel calculus (Teschl 3.1); graph-level extensions via 3.2 and spectral cutoffs.

**PROOF164 (physical/Young identification, F coefficients), CHECKED.**
- Distributional identity `H_Vu = −Δu − Vu` (test Teschl 2.14 representation against C_c^∞); `D(H_V)⊂H¹`, `Vu∈H^{-1/2}` (H_Vu∈L², multiplier bounded), so `(1−Δ)u = H_Vu+Vu+u ∈ H^{-1/2}` → `D(H_V)↪H^{3/2}`, graph-continuous (form bound + `2⟨Au,u⟩≤‖Au‖²+‖u‖²` + multiplier bound on the H^{3/2} norm).
- Free generator ζ domain `H^{3/2}×H^{1/2}` (forward cutoff differentiation, converse via distributional components); no operator-norm differentiability of the group.
- Spectral data `D(A)×D(A^{1/2}) = D(H_V)×H¹` → continuous graph trajectories, C¹ in H¹×L², `u_t=v, v_t=−H_Vu` (spectral cutoffs + dominated tails). Chain rule gives the interaction Duhamel identity; density (D(A) dense in H¹; H¹ dense in H^{1/2} and H^{-1/2}) + boundedness + Picard uniqueness identify the spectral wave with the bounded-perturbation (mild/Young) wave on E.
- On F: bounded compact L + strongly continuous S_F → unique Duhamel with term bound `C_T^{n+1}‖L‖^nT^n/n!`, horizon consistency, composition. Compact L + strong group and adjoint → norm-continuous conjugation → Lipschitz interaction primitive → left Young = ordinary on states.
- Constant block `(c₁+tc₂, c₂)`; E force `(0, V(c₁+sc₂))`; variation-of-constants via bounded finite-triangle E-Fubini (independent of ground/gap). Forcing norm ≤ `‖V‖_{H^{-1/2}}·|c₁+sc₂| ≤ K(1+s)|c|` (uses `‖V‖_{H^{-1/2}} ≤ ‖L‖ ≤ K`).
- `∫₀^t (1+t−s)(1+s)ds = t + t² + t³/6 ≤ (1+t)³`; λ≥0.
- E-component norm ≤ `(1+t)³e^{λt}[8(1+K)²‖e‖ + 8K(1+K)²|c|]`; constant block ≤ `(1+t)|c|`; total coefficients `8(1+K)²` and `[8K(1+K)²+1]`; `√(8²+9²)<13` and `8K(1+K)²+1 ≤ 9(1+K)³` (K≥1) give `13(1+K)³ → 16(1+K)⁴` sufficient bound. No missed constant-velocity term, no hidden exponential prefactor in K.

**Teschl pinpoints** (against the embedded `teschl-2014.txt`): 2.14/(2.63) at book p.81 ✓; 3.6/(3.51)–(3.53) at p.109 ✓; 3.1/(3.18)–(3.21) at pp.102–103 ✓; 3.2/(3.29)–(3.33) at p.104 ✓. The proofs use exactly these and do **not** invoke 10.2 (bounded potential/compact V) or 10.13 (positive ground state), consistent with the rough signed scope.

## Required fixes before production gate

None blocking.

Optional clarity (not mathematical repairs):
- (PROOF163) Replace "dilate … and translate its whole support outside" with the explicit ray/half-space placement so the β ≤ 0 argument is self-contained.
- (PROOF162) State the `b ≤ z` step in the upper-bound chain.

## SSW check ledger

| Check | Result | Note |
|---|---|---|
| SSW01 closure/multiplier | PASS | constant column σ→V Cauchy; support; zero columns; multiplier norm ≤ k; Vu via closure + density; uniqueness; symmetric bounded pairing; complexification |
| SSW02 form/constants | PASS | c=2+K², L_K=3(1+K²); lower/upper bounds verified; closed Hermitian H¹ form; unique H_V; A≥1 spectral; D(A^{1/2})=H¹; no H² domain |
| SSW03 quarter/duality | PASS | ½B₀≤A≤L_KB₀; resolvent order + 1/π subordination; pairs (B₀,2A),(A,L_KB₀); factor 2^{-1/4} and L_K^{1/4}; dual via A^{-1/2}v; completion H^{-1/2} |
| SSW04 spectral bottom | PASS | β≥−(1+K²)/2≥−K²; β≤0 via bumps; real/complex agree; form inf=spec (two directions, nonempty support, resolvent off support); λ≤K; h+c≥2; λ=0 ok |
| SSW05 spectral wave/prefactors | PASS | M_K²=√(3(1+K²))≤2(1+K); matrix entries verified; each entry ≤2(1+K)(1+t)e^{λt}; 2‖entry‖·M_K² = 8(1+K)²(1+t)e^{λt} exact; no λ-division |
| SSW06 rough domain/E id | PASS | H_Vu=−Δu−Vu; D(H_V)↪H^{3/2} graph-continuous; free gen on H^{3/2}×H^{1/2}; C¹ trajectories; Duhamel + density + Picard; no D(A^{3/4})=H^{3/2} |
| SSW07 F/Young id | PASS | unique Duhamel `C_T^{n+1}‖L‖^nT^n/n!`; compact+strong→norm-continuous conjugation, Lipschitz primitive; left Young=ordinary on states; E invariant, constants retained |
| SSW08 F coefficients | PASS | forcing ≤K(1+s)|c|; integral t+t²+t³/6≤(1+t)³; coeffs 8(1+K)² and [8K(1+K)²+1]; CS √(8²+9²)<13 → 13(1+K)³ → 16(1+K)⁴ |
| SSW09 adversarial/source ledger | PASS | V=0/λ=0; signed/no-bound-state; all spectral signs; pure/constant velocity; closure vs arbitrary H^{-1/2}; bumps; real/complex; fixed-R K vs uniform-R E (no mixing); Teschl pinpoints; no trace/positivity/covariance-order/moment claim |
| SSW10 depth/honesty | PASS | all four reconstructed fully; no whole 28/213-proof or non-production clearance claimed |

## Proof status ledger

- **PROOF161** (L:signed-limiting-multiplier): **CHECKED** — closure → unique V∈H^{-1/2} with bounded multiplier action and symmetric pairing bound `k‖u‖‖w‖`.
- **PROOF162** (P:signed-closed-form): **CHECKED** — closed semibounded form, unique H_V, A≥1, D(A^{1/2})=H¹, D(A^{1/4})=H^{1/2} with factors 2^{-1/4}, L_K^{1/4}, negative completion H^{-1/2}.
- **PROOF163** (L:signed-spectral-wave): **CHECKED** — −K²≤β≤0 = inf spec, λ≤K, `‖P_V^E(t)‖ ≤ 8(1+K)²(1+t)e^{λt}`.
- **PROOF164** (P:signed-physical-wave): **CHECKED** — spectral wave = bounded-perturbation/Young physical wave on E; F bound `‖P_V(t)‖ ≤ 16(1+K)⁴(1+t)³e^{λt}` with both constant columns.

## One-line summary

The four rough signed static-potential proofs (limiting multiplier closure, closed form with quarter-power phase, spectral bottom and E-wave bound, and the physical/Young F-identification) are internally correct; every displayed constant and Teschl pinpoint verifies, with no H²/positive-ground/gap hypothesis and no division by λ, and the final coefficient 16(1+K)⁴ follows with ample margin.

*Completion/limitations: This is a direct, single-run audit of PROOF161–164 using only the supplied source. Prerequisite lemmas (cutoff factorization, compact conjugation norm continuity, free group/cameron mean facts, Young theory) were read in the provided statement bodies but not independently re-proven as part of this unit; the Teschl/Friz–Hairer/Crouzeix primary-text excerpts supplied were consulted and their pinpoint numbers matched. Broader dependencies in the 28-body manuscript (e.g., integrated_signed_moment_upper, positive Gram, intrinsic constant, downstream moment conclusions) were not audited. Historical workflow annotations were treated as non-premises, and no prior review state informed this verdict.*