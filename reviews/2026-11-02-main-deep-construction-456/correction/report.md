# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

This is the continuation/correction audit of the SAME constructor 004–006 session. The original report is preserved except where explicitly retracted and corrected below. The verdict and the FULLY_CHECKED status of the three target proofs are unchanged; what changes is the review's own sideline repair of the source's Theorem 3.1 Case 2, which contained one genuine mathematical error now withdrawn.

---

## Original-report-error adjudication

**My prior assertion was WRONG and is withdrawn.** In Finding 2 of my original report I wrote that the Case 2 offset kernel “is a Schur product of shifted PSD kernels (hence PSD).” That is false.

**Verification of the counterexample (as posed).** Take `K(t)=exp(−|t|)` and the shifted two-point kernel `L(s,r)=K(s−r+1)` on `{0,1}×{0,1}`:

- `L(0,0)=e^{−1}`, `L(0,1)=e^{0}=1`, `L(1,0)=e^{−2}`, `L(1,1)=e^{−1}`.
- `L(0,1)=1 ≠ L(1,0)=e^{−2}`, so `L` is **not symmetric**, hence **not PSD** — already decisive.
- Direct quadratic form at `v=(1,−1)`:
`vᵀLv = L(0,0) − L(0,1) − L(1,0) + L(1,1) = 2e^{−1} − 1 − e^{−2} = −(1−e^{−1})² < 0`.

**Verification of the Laplace-mixture version (source class).** With `A=[1,2]` and weights `λ^{α0−1}/Γ(α0)` (strictly positive), the corresponding temporal kernel `γ⁰_c(t)=Γ(α0)^{−1}∫_1^2 e^{−λ|t+c|}λ^{α0−1}dλ` gives, at the same `v=(1,−1)`:

`vᵀγ⁰_c v = Γ(α0)^{−1}∫_1^2 (2e^{−λ} − 1 − e^{−2λ}) λ^{α0−1} dλ = −Γ(α0)^{−1}∫_1^2 (1−e^{−λ})² λ^{α0−1} dλ < 0`.

Each `λ`-layer is strictly negative (`2e^{−λ}−1−e^{−2λ}=−(1−e^{−λ})²`), so the positive-weight integral is strictly negative. **Confirmed.** A shifted temporal covariance kernel in the exact source class is not PSD, and Schur products cannot rescue it.

**Also retracted:** my claim that the printed page 21 dropped a *spatial* offset. See the corrected source-fidelity reading below — the printed line retains the spatial origins inside the test arguments and prints `γ(x−y)` without spatial offset; only the **temporal** prior-time offset is omitted.

**The replacement under audit is CORRECT** (verified below on its own mathematical merits, not by relying on the author note). It does not use PSD of any shifted cross kernel; it uses only PSD of the single stationary product covariance and the common-translation invariance of each self pairing.

---

## Corrected worked translated-test covariance proof

Fix the stationary product covariance on full space–time,

`C((s,x),(r,y)) := γ⁰_{n1,2n}(s−r)·γ_{n1,2n}(x−y)`,

which is PSD (Schur product of PSD `γ⁰` — a finite positive Laplace mixture of `e^{−λ|·|}` — and PSD `γ`; in the source's Theorem 3.1 setting `γ_{j,k}` is pointwise because `μ_{j,k}` is a finite measure). The bilinear form

`⟨f,g⟩_C := ∫∫ f(z) C(z,w) g(w) dz dw`

is PSD, so **Cauchy–Schwarz** `|⟨f,g⟩_C| ≤ ‖f‖_C‖g‖_C` holds for all `f,g` with finite self-norms.

**Translate the tests to their own origins** (extending positive-time kernels by zero for negative time). With `A=s_{n1−1}`, `a=x_{n1−1}`, `B=s_{2n−1}`, `b=x_{2n−1}`:

`f_A(s,x) = G_{n1}(s−A, x−a)`,  `g_B(r,y) = G_{2n}(r−B, y−b)`.

The Case 2 pair integral equals `I_{A,B} = ⟨f_A, g_B⟩_C`.

**Variable changes, signs explicit.** Set `S=s−A`, `X=x−a`, `R=r−B`, `Y=y−b`:

`I_{A,B} = ∫∫ G_{n1}(S,X) γ⁰((S+A)−(R+B)) γ((X+a)−(Y+b)) G_{2n}(R,Y) dS dX dR dY`\
`= ∫∫ G_{n1}(S,X) γ⁰(S−R+(A−B)) γ(X−Y+(a−b)) G_{2n}(R,Y) dS dX dR dY`.   **(★)**

The offsets `A−B` (temporal) and `a−b` (spatial) are **retained**; evenness of `γ⁰` can only replace `S−R+(A−B)` by `R−S+(B−A)`, never remove the offset. This is **not** the zero-offset cross pairing `∫ G_{n1}(S,X)γ⁰(S−R)γ(X−Y)G_{2n}(R,Y)`; independent translation does not preserve the cross pairing.

**Self-norms.** Computing `‖f_A‖²_C = ⟨f_A,f_A⟩_C`, the substitution `S=s−A, S′=s′−A` gives `s−s′ = S−S′`, so the shift `A` cancels identically (and `a` similarly). Hence

`‖f_A‖²_C = ∫∫ G_{n1}(S,X) γ⁰(S−R) γ(X−Y) G_{n1}(R,Y) dS dX dR dY = ‖G_{n1}‖²^{(2)}_{n1,2n}`,

and likewise `‖g_B‖²_C = ‖G_{2n}‖²^{(2)}_{n1,2n}`. This uses **only** the invariance of each *self* pairing under the *common* translation of its two arguments. No statement about the cross pairing is made.

**Therefore**

`|I_{A,B}| ≤ ‖G_{n1}‖^{(2)}_{n1,2n}·‖G_{2n}‖^{(2)}_{n1,2n}`,

exactly the source's printed final inequality in Case 2.

**Regularization and limits.** For nonnegative, possibly unbounded `G_l`: (i) bounded compact test truncations `G_l^{m}↑G_l` (monotone); (ii) temporal Laplace caps `A_{j,k}^{cap}↑A_{j,k}` (monotone, nonnegative integrand). By monotone convergence the self-norms converge up to the finite `‖·‖^{(2)}` values (finite by the source hypothesis), and the cross pairing converges upward, dominated by the finite product of self-norms via CS. Spatial `γ_{j,k}` is already a finite-measure pointwise covariance in the source theorem, so **no spatial mollifier removal is required inside the source-theorem argument.** The spatial Gaussian-mollifier removal is **not** a pointwise monotone step and is deliberately **not** performed here; at the target application level (see boundary below) it is handled by the already-established spatial weak limit of Lemma `L:spatial-wick-measures`, not by a pointwise covariance passage.

---

## Exact source/application boundary

**Source (held page 21, embedded text).** After substituting relative times `s=s_{n1}−s_{n1−1}`, `r=s_{2n}−s_{2n−1}` and absolute spatial variables `x=x_{n1}`, `y=x_{2n}`, the printed line reads

`γ⁰(s−r) γ(x−y) G_{n1}(s, x−x_{n1−1}) G_{2n}(r, y−x_{2n−1})`.

- **Spatial:** because `x,y` are absolute, `γ(x_{2n}−x_{n1})=γ(y−x)` carries **no offset**; the spatial origins `x_{n1−1}, x_{2n−1}` remain inside the test arguments. Hence the printed page **retains spatial origins**. My earlier statement that a spatial offset was dropped is retracted.
- **Temporal:** because `s,r` are relative, `γ⁰(s_{2n}−s_{n1}) = γ⁰(r−s+(s_{2n−1}−s_{n1−1}))`; the printed `γ⁰(s−r)` omits the prior-time offset `c := s_{2n−1}−s_{n1−1}`. Evenness only flips `(r−s)`, never removes `c`.

So the omitted quantity is the **temporal prior-time difference only**. This is a presentation gap in the *source's* proof of its imported theorem; the equality as printed is not justified, but the conclusion is true by the corrected translated-test CS argument above (no PSD of the shifted kernel is used, and no silent re-derivation is needed).

**Application (PROOF006).** The target imports Theorem 3.1 as a cited bound (`\cite{...}*{Theorem~3.1, (3.6), pp.~14--15}`). At the point of use every spatial edge measure is the positive finite Gaussian-weighted measure `e^{−(ε_j+ε_h)|ξ|²/2}μ(dξ)`, i.e. the spatial covariance `γ_{ε_j+ε_h}` has **positive finite heat width**; the temporal covariances are finite Laplace intervals. The target never reproduces the printed dropped-offset equality, never claims PSD of a shifted cross kernel, and never applies the bound to a singular unregularized cross covariance. Spatial-width removal is postponed to the pre-proved weak limit of Lemma `L:spatial-wick-measures`; `d=3` Green removal uses the weak Green convergence at fixed spatial widths with bounded continuous covariance products and the integrable time-cube majorant (lines 376–380). All of these are actual existing hypotheses; no “broader unneeded singular theorem” is invented or assumed.

**Source (3.5) still on record:** the printed second norm displays `G(s,x)G(t,x)` with duplicated `x`; the target correctly reads the second slot as `y` and discloses this (lines 25–26). This is unchanged.

---

## Auxiliary `T1,T2` caps versus physical unequal terminal times (J11, explicit formulas)

**Auxiliary caps.** In PROOF005/006, `T1,T2` cap the *initial-root gap diagrams*: each chain has its own root `(0,0)`, `ℓ_i = Σ_{l∈I_i} r_l` is the chain's terminal time measured from `0`, and the diagrams are integrated over `{ℓ_1<T_1, ℓ_2<T_2}` (and bounded test regions for the limit). These are **auxiliary horizon caps**, not physical terminal times of two independent copies.

**Physical mixed moment at possibly distinct terminal times `τ1≠τ2`.** Reversing copy 1 by `s=τ1−u` (`0≤u≤τ1`) and copy 2 by `r=τ2−v` (`0≤v≤τ2`), a cross temporal factor becomes

`|s−r|^{−α0} = |(τ1−u)−(τ2−v)|^{−α0} = |(u−v)+(τ1−τ2)|^{−α0}`

(up to the overall even sign: `|u−v+τ1−τ2| = |v−u+τ2−τ1|`). The offset `σ:=τ1−τ2` **persists**. Only when `τ1=τ2=τ` do the offsets cancel:

`|(τ−u)−(τ−v)|^{−α0} = |u−v|^{−α0}`.

**Target usage.** Lines 398–406 reverse **both** terminal chains at the **common** horizon `t`, so the offset cancels and only `|u−v|` appears; evenness absorbs the residual sign. Hence the target's unshifted-capped formula `Q_n=Σ_D b_D` is exactly the `L²`-Cauchy object for `E[Y_n(t,x)Y_n(t,x)]` (same `t` on both copies), giving `‖Y_n^a−Y_n^b‖₂² → Q_n+Q_n−2Q_n = 0`. The target **does not** assert a formula for `E[Y_m(τ1)Y_n(τ2)]` with `τ1≠τ2`; the per-diagram limits `b_D` use two independent auxiliary caps, not an unequal-physical-terminal-time claim. No overclaim.

---

## j=2 Brownian fixed-pair control (J04, worked)

`S_b(T)² = ∫∫∫∫_{[0,T]⁴} γ_b(B_{t1}−B_{t2}) γ_b(B_{t3}−B_{t4}) dt₁dt₂dt₃dt₄`.

**Fixed pairing, not enumeration.** The product pairs `{t1,t2}` (copy 1) and `{t3,t4}` (copy 2). There is exactly one pairing; there is **no ×3 factor** (the 3 pair partitions of `{1,2,3,4}` would arise only from expanding two *Gaussian* products via Wick, but `γ_b(B−B')` is a single nonlinear factor, and the two factors are two fixed copies).

**24 orderings.** Decompose `[0,T]⁴` into `4! = 24` strict orderings of the four labeled variables. On one ordering with time-ordered labels `w1<w2<w3<w4`, adjacent gaps `Δ1=w1`, `Δ2=w2−w1`, `Δ3=w3−w2`, `Δ4=w4−w3`, slack `Δ5=T−w4`; `Δ1+…+Δ5=T`.

**Conditional pair bound.** The latest vertex `w4` has its fixed partner at rank `r∈{1,2,3}`. Condition on all vertices except `w4`. By Markov, `B_{w4}−B_{w3}` is independent of the rest, so

`E[γ_b(B_{w4}−B_{w_r}) | B(w1),B(w2),B(w3)] = (p_{Δ4}∗γ_b)(B_{w_r}−B_{w3}) ≤ (p_{Δ4}∗γ_b)(0) = A(Δ4+b)^{−α/2} ≤ A Δ4^{−α/2}`,

using max-at-zero of the even PSD convolution (shift `m=B_{w_r}−B_{w3}` arbitrary). The bound uses the **last adjacent gap `Δ4`** (gap to the temporal predecessor), not the gap to the partner. **Negative-power direction:** `y ↦ y^{−α/2}` is decreasing, so `(Δ4) ≥`-type gaps give smaller values; the adjacent gap at the right endpoint is the valid (largest) upper bound.

**Second removal.** Delete `w4` and its partner `w_r`. The two survivors are the other copy, at larger time `w_m` and smaller `w_{m'}`. The reduced adjacent gap `Δred := w_m − w_{m'} ≥ w_m − w_{m−1} = Δ_m` (an original adjacent gap). Conditioning on the smaller gives the remaining pair factor mean ≤ `A Δred^{−α/2} ≤ A Δ_m^{−α/2}`. The two selected original adjacent gaps `Δ4` and `Δ_m` are **distinct** (`w4≠w_m`, right endpoints distinct).

**Dirichlet normalization.** Integrating `Δ4^{−α/2}Δ_m^{−α/2}` over `Δ1,…,Δ5≥0, Σ=T`:

`∫ Δ4^{−α/2}Δ_m^{−α/2} dΔ₁dΔ₂dΔ₃dΔ₄ = T^{4−α}·Γ(1−α/2)²/Γ(5−α)`

(exponents: two gaps with `a_l=1−α/2`, three weights with `a_l=1`; `Σa_l=5−α`, so exponent `(Σa_l)−1=4−α=(2−α/2)·2`, denominator `Γ(Σa_l)=Γ((2−α/2)·2+1)=Γ(5−α)`). This value is independent of the choice of `m∈{1,2,3}`. Summing the 24 orderings:

`E[S_b(T)²] ≤ 24·A²·Γ(1−α/2)²·T^{4−α}/Γ(5−α)`,

matching `(2j)=4` with `j=2`, exponent `(2−α/2)j=4−α`, and denominator `Γ((2−α/2)j+1)=Γ(5−α)`. **No ×3.** (`j=1` reduces to `2!·A·Γ(1−α/2)·T^{2−α/2}/Γ(3−α/2)=2A T^{2−α/2}/((1−α/2)(2−α/2))`, verified in the original report; `j=0` gives `1`.)

---

## Critical findings

1. **(Retracted, corrected.)** My original sideline claim that the Case 2 offset kernel is PSD by Schur product is false and is withdrawn; a source-class shifted temporal kernel is strictly negative on `v=(1,−1)` (verified above). The corrected translated-test covariance–CS argument is verified and closes the gap without using PSD of the cross kernel.
2. **(Source-proof presentation gap, now correctly scoped.)** Held page 21 omits the **temporal** prior-time offset from the printed `γ⁰(s−r)`; spatial origins are retained in the printed variables. The printed equality is not justified as printed, but the Case 2 conclusion `≤‖G_{n1}‖^{(2)}‖G_{2n}‖^{(2)}` is true by the corrected argument.

No other critical findings: the target proofs themselves (PROOF004/005/006) do not use the retracted claim, every target constant/limit/sign checked in the original report remains correct, and the fixed-`k` marked constant is verified.

## Noncritical findings (updated)

1. Source (3.5) prints `G(t,x)` twice; target reads the second slot as `y` and discloses it (unchanged).
2. `C_{k,T1,T2}` is asserted abstractly in the manuscript, not displayed; an explicit admissible value `4k·e^{T1+T2}·max{1,2N1(1),N2(1)}^{2k}` exists and is verified (no uniformity in `k,T,covariance` claimed).
3. `N2(θ)²≥0` positivity is correct but compressed (Schur of `e^{−θ(s+t)}` and Laplace mixture; note this is the *unshifted single-kernel* Schur, which IS valid — distinct from the retracted shifted-kernel claim).
4. The temporal-cap and Green-smoothing removals are terse; they are monotone (caps, positivity) and weak (Green), respectively — correct.
5. Homogeneity is passed through vague limits and then to Borel `ρ_D`-null boundary; implicit but standard.
6. Statement `N2^{(M)}(1)→0` vs proof `N2^{(M)}(1)²→0`; harmless (nonnegative).

## Checked derivations (updated)

All items from the original report stand **except** the Case 2 sideline, which is replaced by the corrected translated-test proof above. In summary, re-verified in this session:

- **PROOF004** (scaling `μ(cA)=c^αμ(A)`, `μ({0})=0`, resolvent `αV a^{α−2}∫u^{α−1}/(1+u²)du`, `N0=θ⁻²`, `N1` power `α+α0−2`, `N2` power `−β`, `β=4−α−α0`, positivity, tails, smoothing non-increase) — unchanged, correct.
- **PROOF005** (Laplace identity, heat bound `A=αV∫u^{α−1}e^{−u²/2}du`, Brownian moments incl. the new `j=2` worked control, `2^{−2k}`, horizon `¼`, `(1+S₁)^k(1+S₂)^k`, mass `2^{−2k−2}(∫e^{−a/2}M_k da)²`, homogeneity `c^{(4−α)k}`, zero/horizon faces) — correct.
- **PROOF006** (telescope `k·K_{1/η}`, imported Theorem 3.1 hypothesis checks, explicit `C_{k,T1,T2}`, marked tail `N1^{(1/η)}(1)` or `N2^{(1/η)}(1)²`, bracket `b_D(η)`, `Q+Q−2Q=0`, common-horizon reversal) — correct; the imported-theorem application is at positive finite spatial widths and is unaffected by the source Case 2 presentation issue.

## Twelve individual J01–J12 determinations

- **J01 — FULLY_CHECKED.** `μ(cA)=c^αμ(A)`; `V` finite and no origin atom; radial (layer-cake) resolvent `αV a^{α−2}∫u^{α−1}/(1+u²)du`; `N1` finite at 0/∞ via `α0>0`, `α+α0<2`; `N0=θ⁻²`; `N1=θ^{α+α0−2}N1(1)`; `N2²=θ^{−β}N2(1)²`; exact time/Fourier scaling and all `Γ`/parameter guards; no density/isotropy assumed.
- **J02 — FULLY_CHECKED.** Absolute integrability near 0/∞ and on the time diagonal; nonnegative time quadratic form at fixed frequency (unshifted Schur of `e^{−θ(s+t)}` and the Laplace mixture; retained, distinct from the retracted shifted-kernel claim); `K_M→0` off-diagonal dominated with square-vs-root correct; Gaussian/Green factors removable only after integrating the signed time product; Laplace-domain restriction lowers the form; tail kernel PSD by the same Laplace mixture.
- **J03 — FULLY_CHECKED.** Two chains each rooted at `0`; gaps/`s_l` cumulative and vertex weights finite; `γ_{ε_j+ε_h}`, `e^{−Σr_l}` damping; positive Fourier/Laplace formula with denominators `((1+λ_l)²+|η_l|²)`; Fubini via finite spectral/time Green masses; transform coefficients exact; width-monotonicity of transforms only, not physical pointwise `γ` monotonicity.
- **J04 — FULLY_CHECKED.** `A` exact; `p_t*γ_b` bound from radial spectral mass; `2j` time variables; conditional latest-remaining vertex with arbitrary spatial shift; pair removal preserving marginal law; distinct selected right endpoints/original adjacent gaps with negative-power direction; Dirichlet `Γ(1−α/2)^j T^{(2−α/2)j}/Γ((2−α/2)j+1)`; `(2j)!`; `j0/j1` and the explicit nontrivial `j2` control above with no ×3.
- **J05 — FULLY_CHECKED.** Common-minimum-width transform domination; resolvent-to-Brownian identity `½`; `2^{-2k}`; horizon `¼` incl. empty chain; ordered-to-cube extension; per-pair occupation; `A12≤√(S1S2)`; self/cross exponents; `(1+S₁)^k(1+S₂)^k`; finite `M_k`; `2^{-2k-2}(∫e^{−a/2}M_k(a)da)²`; fixed `k`/covariance finite, no uniform-`k`.
- **J06 — FULLY_CHECKED.** `y_l=e^{−r_l}` into `[0,1]^{2k}`; bounded-mass subsequences; integer monomial moments + polynomial density uniqueness; `L_D(c,…,c)→L_D(0)` rules out `y=0`/infinity mass; Portmanteau tail control; bounded continuous tests after pullback; arbitrary width sequences; tightness proven, not assumed; transform monotonicity not confused with monotone physical measures.
- **J07 — FULLY_CHECKED.** `λ_l→∞` gives `ν_D{r_l=0}=0` via zero-param domination; `ρ_D` scaling `c^{(4−α)k}`; compact-test vague convergence; homogeneity + disjoint dilates ⇒ no positive horizon `ℓ_i=T` face; empty-chain case; finite-horizon boundary parts; damping removal for bounded continuous `φ`.
- **J08 — FULLY_CHECKED.** `(3.5)` second-variable typo disclosed (target reads `y`). Case 2: previous *time* origins **not** retained in the printed `γ⁰(s−r)` equality; stationary-covariance CS with translated tests **does** supply the bound (verified above, no PSD of the cross kernel); spatial origins retained; application bound at positive finite spatial widths unaffected. Source verdict and application verdict stated separately.
- **J09 — FULLY_CHECKED.** Telescope `∏|s_e|^{−α0} − ∏γ⁰_η(s_e) = Σ_l [∏_{i<l}γ⁰_η·(|s_l|^{−α0}−γ⁰_η(s_l))·∏_{i>l}|s_i|^{−α0}]`, each nonnegative difference `=K_{1/η}`; explicit admissible `C_{k,T1,T2}=4k·e^{T1+T2}·max{1,2N1(1),N2(1)}^{2k}` (with `N0(1)=1`), uniform over allowed partitions; marked edge once (`N1` tail) or twice (`N2` tail²); no spurious square-root tail; no uniform `k/T/covariance` claim; verifies existence, not a new sharper theorem.
- **J10 — FULLY_CHECKED.** At positive spatial widths the full temporal diagram is finite (bounded spatial covariances/Green mass, `α0<1`); imported bound at finite Laplace caps and `d=3` Green width; caps removed by positivity, then Green width at fixed spatial widths via bounded continuous covariances and integrable time majorant; fixed-`η` spatial weak limit; bracket when all `δ_j<η`; every spatial/time width ratio covered; no unjustified simultaneous limit.
- **J11 — FULLY_CHECKED.** Auxiliary `T1,T2` are initial-root gap-diagram caps, **not** physical terminal times; explicit unequal-terminal reversal offset `|(u−v)+(τ1−τ2)|^{−α0}`; target uses same-`t` two-copy `L²`-Cauchy where the offset cancels; common reversal cancels offset and evenness handles sign; `Q+Q−2Q`; empty/unequal chain lengths allowed; no arbitrary-unequal-terminal-time formula claimed.
- **J12 — FULLY_CHECKED.** `k=1` self vs cross pair; nonempty/empty chains; zero covariance; Brownian `j1/j2`; no-mass-at-infinity and zero faces; explicit physical-unequal-terminal offset formula; canonical multiple-Stratonovich and Green-before-noise order mapped to source; all precision/limits/repairs stated honestly; new source pages are text only (no raster/`PROOF009`/source-image/cold/goal credit).

## PROOF004/005/006 corrected coverage/status and residual gaps

| Proof | Status | Coverage / residual |
|---|---|---|
| PROOF004 `L:damped-homogeneous-norms` (611–671) | **FULLY_CHECKED** | All constants, limits, signs verified; no residual gap. Positivity derivation is compressed but correct (unshifted Schur). |
| PROOF005 `L:spatial-wick-measures` (730–872) | **FULLY_CHECKED** | All measure/heat/Brownian/Laplace bounds verified, incl. `j=2` worked control and `2^{-2k-2}(∫e^{−a/2}M_k)²`. Residual: none. |
| PROOF006 `L:joint-fixed-order` (885–969) | **FULLY_CHECKED** | Telescope, imported bound (at positive finite spatial widths), explicit `C_{k,T1,T2}`, Cauchy bracket, `Q+Q−2Q`. Residual: none in the target proof. The imported theorem's own Case 2 proof has a *source* presentation gap (temporal offset omitted) now closed by the corrected translated-test CS argument; the target imports the bound as valid and does not depend on the printed equality. |

Fixed-`k` marked constant (explicit, hypotheses retained, original proof text unchanged): for fixed order `k` and auxiliary horizon caps `T1,T2`,

`0 ≤ F_{ε,0,D} − F_{ε,η,D} ≤ C_{k,T1,T2}(N1^{(1/η)}(1) + N2^{(1/η)}(1)²)`,  `C_{k,T1,T2} = 4k·e^{T1+T2}·max{1,2N1(1),N2(1)}^{2k}`,

uniform in spatial widths; depends on the fixed covariance only through `N1(1)`, `N2(1)`; no uniformity in `k`, `T`, or covariance is asserted or required.

## Required fixes before production gate

None blocking. Optional editorial items (unchanged): display the explicit `C_{k,T1,T2}`; spell out unshifted Schur positivity and the cap/Green removals; add a source-fidelity remark pinning (i) the (3.5) duplicated variable and (ii) the page-21 *temporal*-offset omission with the translated-test CS repair. All are presentation, not proof.

## One-line summary

The target proofs stay **PASS_WITH_NOTES / HIGH / FULLY_CHECKED**: my sideline “shifted cross kernel is PSD by Schur” claim is verified false and withdrawn, the printed page-21 gap is correctly re-scoped as a temporal-only offset omission, and the corrected translated-test covariance Cauchy–Schwarz argument closes it rigorously without using PSD of any shifted kernel — no change to the manuscript bytes `887fbfbe…`, no second scientific vote, no implicit source-theorem correction, and no raster/source-image/whole-213/main/global/cold or imported-full-proof credit claimed.