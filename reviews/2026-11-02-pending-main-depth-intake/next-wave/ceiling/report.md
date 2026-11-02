# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None.

No false identity, sign error, boundary-term error, incorrect constant, or invalid asymptotic was found in PROOF205–209. All five proofs are self-contained chains over in-project prerequisites, and every final coefficient (K_0, D_ζ, D, v_*, the denominator 8, M_a^{-1/k}, K_0^{1/k}, Δ, the α=5/4 counter-control) recomputes exactly. The strict-log-gap sign is established by strict midpoint convexity of x↦x log x only; no external spectral/variational theorem is needed for the sign itself.

## Noncritical findings

1. **PROOF206 wording ("No optimizer or minimax interchange is assumed") is a touch generous.** The step E_ζ^O = D_ζ C_occ^{2/(2-α)} does use sup over a dilation-closed class plus the monotone map x↦x^{2/(2-α)} applied to the single supremum C_occ. It is a *valid* sup-sup reduction (the class is dilation-invariant, and a ray-wise maximum over ℓ is genuinely attained at ℓ_*=(αA/(2ζT))^{1/(2-α)}), so there is no gap; but "no minimax" overstates the absence of a sup-exchange. The exchange is legitimate because it factorizes through a monotone function of one supremum.

2. **PROOF205 leans on N(f)≤‖f‖_{H¹} and continuity of N** stated without re-deriving them inline. These follow immediately from the prerequisite N(f)=‖f‖₂^{1−α/4}‖∇f‖₂^{α/4} (0<α/4<1/2) via weighted AM–GM, so the statements are correct; only the inline justification is compressed.

3. **PROOF207 keeps a residual +ε in the O-membership gradient bound** (b(g_ε(s)) ≤ H_Ψ + ε). This is harmless: ε is fixed per application, T(g_ε) ≤ H_Ψ + ε < ∞, and the near-Rayleigh linear term is the only place ε enters; Σ_J selection is still Borel and strongly measurable.

4. **PROOF209's lower bracket passes through the auxiliary label-one score S₁^pos**, which is explicitly (and correctly) labeled as not an actual first-moment identity ("not Chen energy or first moment identity"). No overclaim.

5. **Strictness Δ>0 needs a>0** (so q ≠ q−2a; separate from the positivity q−2a>0). The text records exactly this: "Here a>0 and q−2a>2−a>1." Correct as written.

## Checked derivations

- **OCC07/C₂ derivation.** N(g_s)^4 = ‖g_s‖₂^{4−α}‖∇g_s‖₂^α = b_s^{α/2} (unit profile); ∫_I b_s^{α/2} ds ≤ (∫_I b_s ds)^{α/2} = T(g)^{α/2} (|I|=1, concavity); B_Γ(g_s²,g_t²) ≤ R_sp b_s^{α/4}b_t^{α/4} (square-root CS); raw kernel row sup_s∫|s−t|^{−a}dt = [s^{1−a}+(1−s)^{1−a}]/(1−a) ≤ 2^a/(1−a) = K_0 (max at s=1/2). Hence A(g) ≤ K_0 R_sp T^{α/2}. ✓
- **OCC07 dilation.** (U_ℓ g)_s² contributes ℓ^d·ℓ^d over dx; dx↦ℓ^{−d}; Γ(dy) pushforward under y↦ℓy scales ℓ^{α−d} (from Γ(cA)=c^{d−α}Γ(A)); total A↦ℓ^α. ∇ scaling ℓ^{d/2+1}: T↦ℓ². ✓
- **OCC08 optimizer.** Max over ℓ of Aℓ^α−ζTℓ² at ℓ_*=(αA/(2ζT))^{1/(2−α)} equals ((2−α)/2)(α/2)^{α/(2−α)}A^{2/(2−α)}(ζT)^{−α/(2−α)} = D_ζ(A/T^{α/2})^{2/(2−α)}, D_ζ=((2−α)/2)(α/(2ζ))^{α/(2−α)}. At α=1: D_ζ=1/(4ζ), E_ζ=C_occ²/(4ζ); half penalty E_{1/2}=C_occ²/2. Inverse: C_occ=(2E/(2−α))^{(2−α)/2}(2ζ/α)^{α/2}; scaling E_ζ=ζ^{−α/(2−α)}E₁. ✓
- **OCC08/OCC11 first scalar maximization.** c=(vC)^{1/2}, f(T)=cT^β−T, β=α/4. Root T_*=(βc)^{1/(1−β)}; value c^{4/q}[β^{α/q}−β^{4/q}] = c^{4/q}β^{α/q}(1−β) = (q/4)(α/4)^{α/q}(vC)^{2/q} (using 1−β=q/4, α/q = β·4/q). Square root: I ≤ Dv^{1/q}, D=√(q/4)(α/4)^{α/(2q)}C^{1/q}. ✓
- **OCC11 second scalar maximization.** g(v)=cDv^{1/q}−v/2; root v_*=(2cD/q)^{q/k}; value (q/2)(2cD/q)^{q/k}−(1/2)(2cD/q)^{q/k} = (k/2)(2cD/q)^{q/k}=kv_*/2. (2D/q)^q = q^{−q/2}(α/4)^{α/2}C. U_c = c^m k[α^{α/2}C/(8q^{q/2})]^{1/k}. Denominator 8 because (1/2)(α/4)^{α/(2k)} = α^{α/(2k)}2^{−1−α/k} = α^{α/(2k)}2^{−3/k} with k+α=3. ✓
- **OCC12 energy rewriting.** U_c = c^m(2ζ)^{α/(2k)}F_0(E_ζ^O) exactly: α^{α/(2k)}C^{1/k}/(8^{1/k}q^{q/(2k)}) = (2E/(2−α))^{(2−α)/(2k)}(2ζ)^{α/(2k)}/(8^{1/k}q^{q/(2k)}); ζ-dependence cancels against the (2ζ)^{α/(2k)} prefactor. ζ=1/2 factor 1, ζ=1 factor 2^{α/(2k)}. ✓
- **OCC13 brackets.** Upper: C_occ≤K_0R_sp ⟹ C₂ ≤ 2^m K_0^{1/k}F_0(E_sp), where (2E_sp/(2−α))^{(2−α)/2}=α^{α/2}R_sp exactly. Lower: C₂=2^mS₁^pos ≥ 2^m M_a^{−1/k}F_0(E_sp). Both use the same E_sp (own half-gradient energy), same M_a (unnormalized), same raw K_0. ✓
- **OCC14 Δ and ratio.** log(F_a/F_0) = (1/k)[(q−2a)/2 log(q−2a) + (q/2)log q − (q−a)log(q−a)] = Δ/k. Ratio c^mF_a(E_ζ)/U_c = exp((Δ−(α/2)log(2ζ))/k). At ζ=1/2 strict >1; at ζ=1 general. ✓
- **OCC14 α=5/4, a=1/2, d=2 counter-control.** q=11/4, q−2a=7/4, q−a=9/4, 8Δ −8(α/2)log2 = 11log(11/4)+7log(7/4)−18log(9/4)−5log2 = log(11¹¹7⁷/(2⁵9¹⁸)). 11¹¹7⁷=234,966,429,149,994,773; 2⁵9¹⁸=4,803,028,329,503,971,872; ratio<1, sign negative. ✓ (admissible: α=5/4<d=2, α+a=7/4<2.)
- **OCC01 white check.** a=1/2, α=1: Z_a=∬|s−t|^{−1/2}=2/((1/2)(3/2))=8/3; K_0=2^{1/2}/(1/2)=2√2. Time-constant profile: A=Z_aA_sp=(8/3)A_sp, T=b, so C_occ≥(8/3)A_sp/√b and ≤2√2 R_sp. Consistent with the downstream T:white-moment-bounds C₂ ≤ (2/3)√(cK_0). ✓
- **PROOF205 Cauchy square.** C_4(f_n−f_l,f_n+f_l,f_n−f_l,f_n+f_l) = B_Γ(f_n²−f_l²,f_n²−f_l²) = ‖Q(f_n)−Q(f_l)‖² ≤ R_spN(f_n−f_l)²N(f_n+f_l)². Signed real f allowed (f²≥0 physical pairing). ✓
- **PROOF207 integration.** On A_j, ∫h_{Ψ,s}g_s²−b_s = R_j(s) > λ²−ε, so ⟨Ψ,ρ_g⟩−T(g) ≥ ∫λ²−ε; hence I²+T ≤ ∫λ²+T ≤ ⟨Ψ,ρ_g⟩+ε ≤ √(vA)+ε (I²≤∫λ² by time CS on |I|=1, and the last by PROOF205 Hilbert CS). ✓

## Required fixes before production gate

None required. Optional polish: (i) replace "no minimax interchange is assumed" in PROOF206 with an explicit note that the sup-sup is valid because O is dilation-closed and x↦x^{2/(2−α)} is monotone; (ii) in PROOF205 add one sentence deriving N(f)≤‖f‖_{H¹} from N(f)=‖f‖₂^{1−α/4}‖∇f‖₂^{α/4}. Neither is a correctness issue.

---

## OCC01–OCC14 ledger (complete)

| ID | Worked check | Status |
|---|---|---|
| OCC01 | d=1, Γ=cδ₀, a=1/2, α=1, fixed time-constant unit profile: A=Z_aA_sp=(8/3)A_sp, T=b, C_occ≥(8/3)A_sp/√b, ≤2√2·(c/√3); K_0=2√2; x-first Lebesgue null transfer is L:spatial-physical-pair; reverting Γ(dy)-first not used; two-cell two-profile cross-covariance covered by the non-separable bilinear form B_Γ(·,·) with ∬K(s,t) in PROOF205; controlling class is not restricted to separable/time-constant controls | PASS |
| OCC02 | Model/domain ledger exact: d∈{1,2,3}, white α=d=1 included, 0<a<1, α+a<2, Γ>0 vs Γ=0 treated separately; O = strongly H¹-measurable real unit profile with T(g)=∫‖∇g_s‖²<∞, no compact-support/time-continuity condition; raw K vs damped K_* distinguished; own energies E_ζ^O/E_sp vs Chen printed E,E_* not identified; amplitude retained; kinetic one; Rayleigh penalty ζ vs raw variance half-action v/2; Nonseparable C_pos permitted; no Riesz density/angular or α≤1 imposed | PASS |
| OCC03 | R_0 from smooth compact profiles bounded before any rough H¹ extension (P:spatial-smooth-ratio); four-linear PSD/CS to H¹ squares via Fatou then full physical Cauchy; R_sp=R_0, strict positivity of A_sp(f) for nonzero H¹; no circular use of C_occ ceiling or T:intrinsic-second-moment in R_sp finiteness | PASS |
| OCC04 | Q:H¹→H_sp defined by compact-smooth-square Cauchy with C_4(f−h,f+h,f−h,f+h) ≤ R_spN(f−h)²N(f+h)²; N continuous ≤H¹; interlacing independence; physical pairing identity ⟨Q(f),Q(h)⟩=B_Γ(f²,h²); Q continuous; raw completion class vs actual f² (f² itself not a raw test) separated; signed real f allowed | PASS |
| OCC05 | J_G embedding for general (possibly inseparable) G via dense finite tensors, Schur row K_0=2^a/(1−a), norm identity + bilinear polarization; H_I=H_t⊗H_sp by supported-tensor lemma; for g∈O, ∫‖Q(g_s)‖² ≤ R_spT(g)^{α/2}; exact physical A(g) norm equality; joint measurability & representative independence; temporal diagonal null vs spatial singular measure handled separately | PASS |
| OCC06 | χ=1 on spacetime support of Ψ; ⟨Ψ_t,Q(f)⟩=C_4(χ,Ψ_t,f,f)=B_Γ(Ψ_t,f²); polarize J → ⟨Ψ,ρ_g⟩=∬K(s,t)B_Γ(Ψ_t,g_s²) = ∫h_{Ψ,s}g_s², ≤√(v_ΨA(g)); no rough occupation inserted into stochastic flow, no extra Fourier/physical-mask factor | PASS |
| OCC07 | C_occ positive & finite: T>0 for unit H¹ (no zero-gradient unit state); CS+Schur+concavity exact K_0R_sp; fixed compact unit profile positivity via physical Γ; dilation U_ℓ a bijection of O preserving strong measurability; Radon ℓ^{α−d}, Lebesgue ℓ^{−d}, squares ℓ^{2d} → Aℓ^α, Tℓ²; no density assumption | PASS |
| OCC08 | Full scalar optimizer; derivative sign; global max Aℓ^α−ζTℓ²; exact D_ζ; C_occ^{2/(2−α)}; inverse ratio; ζ^{−α/(2−α)} scaling; α=1 D_ζ=1/(4ζ), E_ζ=C_occ²/(4ζ); A=0 branch zero via ℓ↓0; no attained optimizer/minimax over a gap | PASS |
| OCC09 | H¹ separability; countable normalized dense family; sup_jR_j=λ² by bounded-potential form continuity; Borel first-index cells; strongly measurable via finite-valued truncations; b≤H_Ψ+ε membership using λ²≥0; integrate near-Rayleigh then raw pairing; I²≤∫λ² by time CS; no eigenstate/continuum selector/temporal regularity control | PASS |
| OCC10 | β=α/4∈(0,1/2); sup of √(vC)T^β−T; v=0 branch; derivative/root; exact max (q/4)(α/4)^{α/q}(vC)^{2/q}; square root I≤Dv^{1/q}; ε per Ψ/ε with numeric sup before ε↓0 | PASS |
| OCC11 | cI−v/2 over original smooth positivity class; cDv^{1/q}−v/2; v_*=(2cD/q)^{q/k}; value kv_*/2; denominator 8 via k+α=3; α=1 control U_c = 2c^{3/2}√(C/(8·3^{3/2})); homogeneity c^m matches class bijection; optimization is only an upper bound | PASS |
| OCC12 | U_c=c^m(2ζ)^{α/(2k)}F_0(E_ζ^O); ζ cancels; ζ=1/2 factor 1, ζ=1 factor 2^{α/(2k)} not omitted/reversed; C₂=S₂^pos lower/upper uses same canonical Stratonovich solution, original covariance, fixed x, kinetic one, variance-half action; S₁^pos explicitly not a first moment | PASS |
| OCC13 | Common spatial bracket; upper via C_occ≤K_0R_sp and E_sp half-gradient; lower via temporal equilibrium M_a and C₂=2^mS₁^pos; same E_sp domain/normalization throughout; M_a unnormalized mass; K_0 raw row; no bound-equals-constant claim | PASS |
| OCC14 | Strict Δ>0 via x log x midpoint convexity (q>2, 0<a<1, α+a<2 ⇒ q−2a>2−a>1; no q≥3 needed); log(F_a/F_0)=Δ/k; general ratio with −(α/2)log(2ζ)/k; half penalty strict; α=5/4,a=1/2,d=2 counter-control numerator 234,966,429,149,994,773 < denominator 4,803,028,329,503,971,872 (negative sign); compares computed bounds only; zero Γ: Q=A=C_occ=0, energy sup 0 via small dilations, F_b(0)=0, strict statements only for Γ≠0, no zero-gradient unit | PASS |

---

## Five-row proof ledger (PROOF205–209)

| Proof | Status | Coverage |
|---|---|---|
| PROOF205 L:occupation-raw-square | FULLY_CHECKED | Statement (4622–4642) + proof (4644–4696). Q map well-defined/continuous; ‖ρ_g‖²=A(g); pairing identity = ∫h_{Ψ,s}g_s²; CS bound √(vA). All correct. |
| PROOF206 P:raw-occupation-energy | FULLY_CHECKED | Statement (4698–4718) + proof (4720–4762). 0<C_occ≤K_0R_sp; D_ζ, 2/(2−α), inverse ratio, ζ-scaling, α=1 check all exact. |
| PROOF207 L:occupation-rayleigh-selection | FULLY_CHECKED | Statement (4764–4772) + proof (4774–4814). Countable selection, measurability, O-membership, integrated near-Rayleigh, time CS all valid. |
| PROOF208 T:intrinsic-occupation-ceiling | FULLY_CHECKED | Statement (4826–4840) + proof (4842–4878) + scalar map (4816–4824). Two scalar optimizations and both ceiling forms exact; zero-Γ handled. |
| PROOF209 C:intrinsic-spatial-bracket | FULLY_CHECKED | Statement (4880–4894) + proof (4896–4932) + zero-Γ paragraph (4934–4941). Bracket bounds and strict comparison exact; integer counter-control exact and honest. |

---

## Exact model / domain / action / source-role matrix

- **Model**: hyperbolic Anderson (H:homog), spatial homogeneity Γ(cA)=c^{d−α}Γ(A), temporal |s−t|^{−a}, d∈{1,2,3}, 0<a<1, α+a<2, white α=d=1 permitted.
- **Domain O**: real, strongly H¹(ℝᵈ;ℝ)-measurable s↦g_s on I=(0,1), ‖g_s‖₂=1 a.e., T(g)=∫‖∇g_s‖²ds<∞; no compact support / time regularity / separability restriction on controls.
- **Raw quadratic action**: A(g)=∬_I²|s−t|^{−a}B_Γ(g_s²,g_t²)ds dt; raw variance half-action v_Ψ/2 (not a penalty).
- **Occupation constant**: C_occ=sup_g A(g)/T(g)^{α/2}.
- **Own energies**: E_ζ^O=sup_g[A(g)−ζT(g)] (scalar penalty), E_sp=sup_{‖g‖₂=1}[A_sp(g)−‖∇g‖₂²/2] (half-gradient spatial energy). Distinct from Chen's printed E_*, E and from the damped kernel K_* energy.
- **Source role**: occupation raw space is the *original* covariance; mask/physical factors occur exactly once elsewhere and are not inserted here; auxiliary S₁^pos is a variational label, not a first-moment theorem.

## Read / interface-only / unread / missing input ledger

**Read (verbatim embedded excerpt, target section lines 4598–4943 plus the prerequisite sections it cites):**
Propositions/lemmas actually read inside the excerpt needed by the five proofs: P:spatial-four-linear / L:spatial-physical-pair / N(f) definition / E:spatial-square-CS / E:spatial-dilation (integrated_spatial_occupation, lines 7651–8091); A_sp, R_sp=R_0 (same file); L:positive-raw-embedding / K_0=2^a/(1−a) (integrated_intrinsic_constant lines 3933–4371); E:spatial-energy-map / E:spatial-static-energy-score (integrated_spatial_occupation 7918–7970); E:variational-positive-class / P:variational-positive-scores / S_c^pos=c^m S₁^pos and C₂=S₂^pos (integrated_unmasked_variational 9651–10034, integrated_intrinsic_constant 4306–4361); E:temporal-equilibrium-mass / M_a (integrated_temporal_equilibrium 8520–8586); P:positive-signed-comparison / P:positive-score-cutoff only as context for S_R=S₂^pos (integrated_intrinsic_constant 4182–4304); white evaluation (integrated_white_evaluation 10593–10779) used as a downstream consistency cross-check.

**Interface-only (statement trusted, proof not re-derived here, because they are prerequisites not targets):**
P:variational-unmasked-rate (Rayleigh formula λ² = sup(∫h f²−‖∇f‖²), negative floor, continuity); T:intrinsic-second-moment (C₂=S₂^pos=2^{(4−α)/(3−α)}S₁^pos, 0<C₂<∞, zero case); P:compact-original-common-trial (binding); P:spatial-smooth-ratio / P:spatial-four-linear full proof (R_0 finiteness before extension). These are consistent with all downstream algebra and were sanity-checked at the interface level only.

**Unread/missing:**
PaperDev-Tailored-Workflow.md excerpt is marked `[missing: PaperDev-Tailored-Workflow.md]`; no workflow-specific obligations could be audited. No manuscript render or source image supplied (zero image/render credit). Prior REPORT / identity-verdict rows not supplied (scope states they were stripped) — this run is thus not a prior-review-disputed second read, but the verdict does not rely on them. External source PDFs (Chen author version, Chen–Hu, Teschl, Friz–Hairer, Crouzeix–Palencia, Balan–Conus, chen-2023, crouzeix-v1) are embedded as text carriers but are not needed for the five-target derivation chain: the five proofs import only in-project propositions and the self-contained x log x convexity argument; no external theorem is cited inside PROOF205–209 themselves.

**Limitations propagated:** the five bounded-target proofs are fully verified; the whole-argument theorem T:intrinsic-second-moment (and its positive/raw upper-lower chain) and the original 214/global/fullmodel obligations remain outside this bounded acceptance, as the scope states.

## Own-energy / source comparison and no-go boundaries

- Own energies E_ζ^O, E_sp are explicitly **not** identified with Chen's printed energies; the corollary's strict gap and the ceiling are comparisons of the manuscript's own bounds and do not claim attainment or equality with C₂.
- The α=5/4, a=1/2 counter-control refutes only the *penalty-1 F_a-form* as an upper bound; it does not refute C₂≤U_𝔠, which is unaffected.
- No Riesz density, angular regularity, or α≤1 restriction is imposed anywhere in the five proofs; the only restrictions are H:homog and the strict subcritical threshold α+a<2.
- Zero image/render/cold-read credit: none taken.

## One-line summary

All five occupation-ceiling proofs (raw square, raw energy, Rayleigh selection, occupation ceiling, spatial bracket) are mathematically sound with every constant, sign, boundary case, and the α=5/4 arithmetic re-verified exactly, so PASS_WITH_NOTES is unnecessary and the clean grade is PASS (HIGH).

END OF BOUNDED OCCUPATION CEILING REVIEW