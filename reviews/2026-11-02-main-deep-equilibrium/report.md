# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. Both PROOF133 (Lemma `L:equilibrium-gamma-beta`) and PROOF134 (Lemma `L:temporal-equilibrium`) are mathematically correct as stated. No proof gap, sign error, wrong constant, hidden hypothesis inside the stated domains, or invalid asymptotic claim was found. All parameter-range checks (`0<a<1`, hence `0<r<1/2`) are used exactly where needed.

## Noncritical findings

1. **Terse IBP/change-of-variables attribution (PROOF133).** Line 25–26 says "Tonelli gives the Beta–Gamma identity," but the step is really (i) the bijective substitution `(u,v)=(Rt,R(1-t))` with `|det|=R`, plus (ii) Tonelli/Fubini on the nonnegative product integrand. Correct result; attribution is slightly imprecise. The single point value `(R,t)` is a null set, so no issue, but the proof does not say this.

2. **Boundary terms and finiteness are asserted, not shown (PROOF133).** "Vanishing boundary terms" for `u^x e^{-u}` (zero at `0` for `x>0`, zero at `∞`) and the finiteness of `Γ_E`, `Beta` for positive arguments are stated without demonstration. Standard and correct; the statement at lines 8–10 (`Both integrals are positive and finite`) is fully justified by `x-1>-1`, `y-1>-1`, and exponential decay.

3. **Compressed second binomial expansion (PROOF134).** Lines 75–80 jump from the series in `(r)_n/(1+r)_n = r/(r+n)` to `L(s)=r Beta(1-r,2r) B_s(r,r)`. The unstated ingredient is expanding `(1-u)^{r-1} = Σ_{n≥0}(1-r)_n u^n/n!` (positive binomial with `p=1-r>0`), justified by the same machinery already proven at lines 55–61. The identity is correct; it would be cleaner to flag that this second use is covered by the earlier binomial argument.

4. **Reflection/substitution not written out (PROOF134).** Lines 81–82 assert `R(s)=L(1-s)` and `B_s+B_{1-s}=Beta(r,r)`; the substitutions `t=1-τ` and `u=1-v` are implicit. Both are correct.

None of these affect validity.

## Checked derivations

**PROOF133 (lines 12–35) — all verified:**

- `Γ(x+1)=xΓ(x)`: IBP `[-u^x e^{-u}]_0^∞ + x∫u^{x-1}e^{-u}du`; both boundary terms vanish. ✓
- Beta–Gamma identity: substitution `u=Rt, v=R(1-t)`, Jacobian `|det|=R`, `du dv = R dR dt`; product = `Γ(x+y)·Beta(x,y)`. ✓
- `Beta(x,x)=2^{1-2x}Beta(1/2,x)`: symmetry → `t=(1+v)/2` gives factor `2^{2-2x}·(1/2)`, evenness of `(1-v²)^{x-1}`, then `v²=w` → `Beta(1/2,x)`. ✓ (every power of 2 confirmed)
- `Γ(1/2)=√π`: `u=z²` gives `Γ(1/2)=∫_ℝ e^{-z²}dz`; squaring + polar → `2π∫_0^∞ r e^{-r²}dr = π`. ✓
- Duplication: `Beta(x,x)=Γ(x)²/Γ(2x)` combined with `2^{1-2x}√π Γ(x)/Γ(x+1/2)` gives `Γ(2x)=2^{2x-1}Γ(x)Γ(x+1/2)/√π` after cancelling one `Γ(x)`. ✓ No circularity: duplication is *derived* from Beta–Gamma plus the Gaussian value, never assumed.
- EQB01/EQB02 satisfied (positivity/finiteness structure, all powers of 2 and the exact `√π`).

**PROOF134 (lines 54–104) — all verified:**

- **Positive binomial series** (lines 55–61): ratio test radius 1, termwise derivative `(1-z)y'=py`, `d/dz[(1-z)^p y]=0`, `y(0)=1` ⇒ `y=(1-z)^{-p}`. Includes `(p)_0=1`; no convergence claimed at `z=1`. ✓ (EQB03)
- **Left substitution `t=su`** (lines 64–73): `|s-t|^{2r-1} → s^{2r-1}(1-u)^{2r-1}`, `[t(1-t)]^{-r} → s^{-r}u^{-r}(1-su)^{-r}`, `dt=sdu`; total power of `s` is `(2r-1)-r+1 = r`, matching `s^r`. ✓ (EQB04)
- **Pochhammer/Beta ratio** (line 74): `Beta(1-r+n,2r)=Beta(1-r,2r)·(1-r)_n/(1+r)_n` from `Γ`. ✓
- **Incomplete Beta identity** (lines 75–79): `(r)_n/(1+r)_n = r/(r+n)`; combining with `(1-sv)^{r-1}=Σ(1-r)_n(sv)^n/n!` and termwise (nonnegative) integration gives `L(s)=r Beta(1-r,2r) B_s(r,r)`, `B_s(r,r)=∫_0^s u^{r-1}(1-u)^{r-1}du`. Coefficient `r·Beta(1-r,2r)` confirmed. ✓ (EQB05)
- **Reflection + completion** (lines 81–82): right part `=L(1-s)`; `B_s+B_{1-s}=Beta(r,r)`. ✓
- **Final constant** (lines 84–85): `r Beta(1-r,2r) Beta(r,r) = r·[Γ(1-r)Γ(2r)/Γ(1+r)]·[Γ(r)²/Γ(2r)] = Γ(r)Γ(1-r)` (using `Γ(1+r)=rΓ(r)`). ✓ Normalizing by the density divisor `Γ(r)Γ(1-r)` yields potential ≡ 1. ✓
- **Endpoints** (lines 87–89): at `s=0` integrand `t^{r-1}(1-t)^{-r}` integrates to `Beta(r,1-r)=Γ(r)Γ(1-r)`; `s=1` by reflection. ✓ EQB06: integrability at `t=s` (`2r-1>-1` since `r>0`) and at `t=0,1` (`-r>-1`) is explicit; endpoints are direct, not a dominated-convergence limit.
- **L¹∩L²** (lines 93–94): `-r>-1` and `-2r=a-1>-1` (equivalently `r<1/2`). ✓
- **Mass** (lines 95–101): `M_a = Beta(1-r,1-r)/(Γ(r)Γ(1-r)) = Γ(1-r)/(Γ(2-2r)Γ(r))`; with `r=(1-a)/2` this equals `Γ((1+a)/2)/(Γ(1+a)Γ((1-a)/2))`, matching `E:temporal-equilibrium-mass`. ✓ EQB07: no renormalization (explicit at line 102), no temporal white-limit substitution.

**EQB08 falsification controls (checked):**
- `a=1/2 ⇒ r=1/4`. Direct endpoint check: `∫_0^1 t^{-3/4}(1-t)^{-1/4}dt = Beta(1/4,3/4) = Γ(1/4)Γ(3/4)`, so potential `=1`; midpoint follows from the general s-independent constant. `M_{1/2}=Γ(3/4)/(Γ(3/2)Γ(1/4))>0`. ✓
- Formal `a→0+` (`r→1/2-`): density → arcsine `1/(π√(t(1-t)))`, `M_a→1`. Formal `a→1-` (`r→0+`): `Γ(r)~1/r→∞`, `M_a→0`. The manuscript makes no long-time/endpoint limit interchange; the white module (line 1073) explicitly disclaims one. ✓

**EQB09 consumer checks (occupation/spatial/white):**
- `M_a` used correctly in `C:intrinsic-spatial-bracket` (`2^m M_a^{-1/k}F_0(ℰ_sp)`, line 395), in `L:spatial-static-controls` (cost → `M_a B_Γ(z,z)`, lines 549–554), and in `T:white-moment-bounds` lower bound `(2/3)√(c/M_a)`.
- Normalized potential 1 used correctly: `k_n(s)↑1` for every `s∈[0,1]` via monotone convergence against `E:temporal-equilibrium-potential` (line 539–540), and the two-sided bound `0<c₀≤k_n(s)≤1` follows from kernel `|s-t|^{-a}≥1`.
- White relative-width consumer (`C:white-relative-width`) uses Lemma `L:equilibrium-gamma-beta` duplication/recurrence correctly: `Γ(1+a)=2^a Γ((1+a)/2)Γ(1+a/2)/√π` and `(1-a)Γ((1-a)/2)=2Γ((3-a)/2)` yield `K₀M_a = √π/(2Γ(1+a/2)Γ((3-a)/2))`, Cauchy–Schwarz with `ª x=1+a/2, y=(3-a)/2, x+y=5/2` and norms `Γ(x),Γ(y)`, inner product `Γ(5/4)`; equality at `a=1/2`. ✓
- The two lemmas themselves are self-contained; they do not claim any intrinsic-model theorem (consistent with EQB09's warning, which the manuscript also honors at line 102 and via the white module's scope caveats).
- **Upstream obligations named (outside these two proofs; not verified here, hence recorded as such):** `P:variational-unmasked-rate`, `P:variational-remove-mask`, `T:intrinsic-second-moment` (identification `C₂=S₂^pos` and the `S₂≥2^m S₁` step), `P:spatial-four-linear`, `P:spatial-energy-map`, `L:occupation-raw-square`, `T:intrinsic-occupation-ceiling`. These are consumer-internal dependencies and are not established by PROOF133–134.

**EQB10 ledger:** PROOF133 PASS, PROOF134 PASS; EQB01–EQB09 all PASS; EQB10 satisfied here.

## Required fixes before production gate

None. All mandatory corrections are absent. Optional (non-blocking) clarity edits:
- State the change-of-variables determinant explicitly rather than attributing the whole Beta–Gamma step to Tonelli.
- Spell out the `(1-u)^{r-1}` positive-binomial expansion when deriving `B_s(r,r)`, and the `t→1-τ` / `u→1-v` substitutions for reflection and completion.

## One-line summary

PROOF133 and PROOF134 are both correct: every constant (duplication `2^{2x-1}/√π`, normalization `Γ(r)Γ(1-r)`, mass `Γ((1+a)/2)/(Γ(1+a)Γ((1-a)/2))`), every sign, every boundary/endpoint term, every exponent (`-a=2r-1`), and every consumer use of potential-1 and `M_a` checks out, with only minor terseness/attribution notes and no gate-blocking errors.