# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

Both assigned proofs preserve their statements and deduction. The Gamma/Beta proof is
byte-identical between revisions and is mathematically sound. The temporal-equilibrium
proof is rewritten into numbered steps with new explanatory sentences, all of which I
verified against the same hypotheses, normalizations and limiting conventions; no new
defect was found. I reconstructed all deductions from public definitions rather than
from labels.

## L:equilibrium-gamma-beta

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (no new explanatory text; OLD lines 25–36 and NEW lines
  25–36 are identical, including the surrounding `\begin{proof}...\end{proof}`)
- Evidence: I reconstructed all three identities.

  1. Recurrence (lines 17, 26). Γ_E(x+1)=∫₀^∞ u^x e^{-u}du = [−u^x e^{−u}]₀^∞ +
     x∫₀^∞u^{x−1}e^{−u}du. The boundary term vanishes: at u=0, u^x e^{−u}→0 for x>0;
     at u=∞, u^x e^{−u}→0. Hence Γ_E(x+1)=xΓ_E(x).

  2. Beta–Gamma (lines 18, 27–28). Γ_E(x)Γ_E(y)=∫∫_{u,v>0}u^{x−1}v^{y−1}e^{−(u+v)}du dv.
     Set (u,v)=(Rt,R(1−t)), R>0, 0<t<1. The Jacobian determinant is
     ∂(u,v)/∂(R,t)=t·(−R)−R·(1−t)=−R, absolute value R, and u+v=R. So
     Γ_E(x)Γ_E(y)=∫₀^∞R^{x+y−1}e^{−R}dR·∫₀¹t^{x−1}(1−t)^{y−1}dt =
     Γ_E(x+y)Beta(x,y); positivity legitimizes Tonelli.

  3. Duplication (lines 19, 28–34). Symmetry of Beta(x,x); substitute t=(1+v)/2 so
     [t(1−t)]^{x−1}=4^{1−x}(1−v²)^{x−1} and dt=dv/2, giving
     Beta(x,x)=2^{1−2x}∫_{−1}^1(1−v²)^{x−1}dv=2^{2−2x}∫₀¹(1−v²)^{x−1}dv; then v²=w gives
     ∫₀¹(1−v²)^{x−1}dv=(1/2)Beta(1/2,x). Hence
     Beta(x,x)=2^{1−2x}Beta(1/2,x), as asserted (line 29–30).
     Γ_E(1/2)=√π: u=z² gives Γ_E(1/2)=2∫₀^∞e^{−z²}dz=∫_ℝe^{−z²}dz, and squaring with
     polar coordinates gives (∫_ℝ e^{−z²}dz)²=2π∫₀^∞ r e^{−r²}dr=2π·(1/2)=π,
     matching lines 30–33. Combining
     Beta(1/2,x)=Γ_E(1/2)Γ_E(x)/Γ_E(x+1/2)=√πΓ_E(x)/Γ_E(x+1/2) with
     Beta(x,x)=Γ_E(x)²/Γ_E(2x) yields
     Γ_E(2x)=2^{2x−1}Γ_E(x)Γ_E(x+1/2)/√π.

- Lost steps/qualifiers: none identified within this read. Pre-existing note: the
  duplication step is terse — the factor‑of‑2 bookkeeping in the substitution chain
  (lines 28–30) is left implicit — but it is checkable and correct.

## L:temporal-equilibrium

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (every added sentence in NEW lines 56–124 checks out;
  detailed below)
- Evidence (equation-level reconstruction; OLD proof lines 55–97, NEW proof lines
  55–124; statements lines 39–53 unchanged):

  Setup. 0<a<1 gives r=(1−a)/2∈(0,1/2), and −a=2r−1, so the kernel is
  |s−t|^{2r−1}; the density is f_a(t)=[t(1−t)]^{−r}/(Γ_E(r)Γ_E(1−r)).

  Step 1 (binomial, NEW 61–68, same as OLD 56–61). (1−z)^{−p}=Σ_{n≥0}(p)_n z^n/n! has
  coefficient ratio (p)_{n+1}/(n+1)!·n!/(p)_n=(p+n)/(n+1)→1, so radius 1 and uniform
  convergence on [0,ρ], ρ<1; the differentiated series has ratio (p+n)/n→1 as well.
  Termwise differentiation: the n-th coefficient of (1−z)y′ is
  (p)_{n+1}/n!−(p)_n/(n−1)! = [(p)_{n+1}−n(p)_n]/n! = p(p)_n/n!, since
  (p)_{n+1}=(p+n)(p)_n, and the constant term is (p)_1=p. Hence
  (1−z)y′=py, y(0)=1; then d/dz[(1−z)^p y]=(1−z)^{p−1}[(1−z)y′−py]=0, so
  (1−z)^p y≡1. All terms nonnegative → Tonelli applies.

  Step 2 (interior potential, NEW 74–104, OLD 63–85). For 0<s<1, the left half with
  t=su gives
  L(s)=s^r∫₀¹u^{−r}(1−u)^{2r−1}(1−su)^{−r}du (NEW 77–78, OLD 66–67).
  The NEW addition (lines 83–86) is correct: expanding (1−su)^{−r}=Σ(r)_n s^n u^n/n!,
  the term of order n integrates ∫₀¹u^{n−r}(1−u)^{2r−1}du = Beta(n+1−r,2r), and
  Beta(n+1−r,2r)/Beta(1−r,2r) =
  [Γ(n+1−r)/Γ(1−r)]·[Γ(1+r)/Γ(n+1+r)] = (1−r)_n/(1+r)_n,
  using (1−r)_n=Γ(n+1−r)/Γ(1−r) and Γ(1+r)/Γ(n+1+r)=1/(1+r)_n. So
  L(s)=Beta(1−r,2r)s^rΣ(r)_n(1−r)_n s^n/[(1+r)_n n!] (NEW 79–81).

  The r/(r+n) factor: (r)_n/(1+r)_n =
  [r(r+1)⋯(r+n−1)]/[(r+1)⋯(r+n)] = r/(r+n), correct (NEW 87–88, OLD 72–73). For
  B_s(r,r)=∫₀^s u^{r−1}(1−u)^{r−1}du, expand (1−u)^{r−1} with p=1−r>0:
  (1−u)^{r−1}=Σ(1−r)_n u^n/n!, giving ∫₀^s u^{n+r−1}du=s^{n+r}/(n+r). Hence
  r·Beta(1−r,2r)B_s = Beta(1−r,2r)s^rΣ r(1−r)_n s^n/[(n+r)n!]
  = Beta(1−r,2r)s^rΣ(r)_n(1−r)_n s^n/[(1+r)_n n!] = L(s), because
  r/(n+r)=(r)_n/(1+r)_n. This validates the NEW sentences at 93–95 exactly, including
  the stated coefficient (1−r)_n/n! and integral s^{r+n}/(r+n).

  Reflection (t↦1−t, s↦1−s) sends the right half to L(1−s); since
  g(u)=[u(1−u)]^{r−1} is symmetric about u=1/2, ∫₀^{1−s}g=∫_s¹g, so
  B_s+B_{1−s}=Beta(r,r) (NEW 97–98, OLD 78–79). Therefore the unnormalized kernel
  integral equals
  r·Beta(1−r,2r)Beta(r,r)
  = r·[Γ(1−r)Γ(2r)/Γ(1+r)]·[Γ(r)²/Γ(2r)]
  = rΓ(1−r)Γ(r)²/Γ(1+r) = Γ(r)Γ(1−r),
  using Γ(1+r)=rΓ(r). Dividing by the denominator Γ(r)Γ(1−r) of f_a gives
  ∫₀¹|s−t|^{−a}f_a(t)dt=1. The assertion "the full integral is therefore
  …=Γ_E(r)Γ_E(1−r)" (NEW 99–100, OLD 80–81) is the unnormalized value, exactly the
  normalizing Gamma product — consistent.

  Endpoints (NEW 101–104, OLD 82–85) are direct evaluations, not a limit argument.
  At s=0: ∫₀¹t^{2r−1}t^{−r}(1−t)^{−r}dt=∫₀¹t^{r−1}(1−t)^{−r}dt=Beta(r,1−r)
  =Γ(r)Γ(1−r)/Γ(1)=Γ(r)Γ(1−r); s=1 is the reflected version; both equal 1 after
  normalization.

  Finiteness. The exponents −r and 2r−1 satisfy −r>−1 (r<1) and 2r−1>−1 (r>0), so the
  endpoint density singularities and the interior kernel singularity at t=s are all
  integrable; L² additionally requires −2r=a−1>−1, i.e. a>0 (NEW 100, 110–115, OLD
  81–82, 87–88). The NEW addition "0<r<1/2; density ~ distance^{−r}, square ~
  distance^{−2r}; both powers exceed −1" is correct: −r>−1 and −2r>−1 hold for
  0<r<1/2.

  Step 3 (mass, NEW 116–123, OLD 89–96).
  M_a=∫₀¹[t(1−t)]^{−r}dt/(Γ(r)Γ(1−r))=Beta(1−r,1−r)/(Γ(r)Γ(1−r))
  =Γ(1−r)²/Γ(2−2r)·1/(Γ(r)Γ(1−r))=Γ(1−r)/(Γ(2−2r)Γ(r)).
  Translating back: r=(1−a)/2, so 1−r=(1+a)/2, 2−2r=1+a, r=(1−a)/2. This gives
  M_a=Γ((1+a)/2)/(Γ(1+a)Γ((1−a)/2)), exactly
  \eqref{E:temporal-equilibrium-mass}. The mass is genuinely unrenormalized: e.g. at
  a=1/2, M_{1/2}=Γ(3/4)/(Γ(3/2)Γ(1/4))≈0.676≠1, and the text states "Its time mass has
  not been renormalized" (NEW 122, OLD 94). No probability normalization is silently
  imposed.

- Lost steps/qualifiers: none identified. The rewrite preserves the every-s∈[0,1]
  assertion for the open range 0<a<1, without claiming endpoints of the parameter
  range or extra asymptotics. The only compression is inherited from OLD: the two
  distinct Beta-ratio computations are both summarized by the phrase "The Beta ratio
  follows from the Gamma recurrence" (first for (1−r)_n/(1+r)_n, then for
  Beta(1−r,2r) itself); NEW lines 83–86 now spell out the first occurrence, so the
  NEW text is strictly clearer, not less careful.

## AUDIT dispositions

- NEW 56–58 (restructuring sentence): accurate description of the three-step proof; no
  mathematical claim at risk.
- NEW 62 (Step 1 label): merely labels the unchanged binomial argument.
- NEW 83–86 ("term of order n integrates u^{n−r}(1−u)^{2r−1}; … divides … to give
  (1−r)_n/(1+r)_n"): verified; Beta(n+1−r,2r)/Beta(1−r,2r)=(1−r)_n/(1+r)_n via the
  Gamma recurrence.
- NEW 93–95 ("expanding (1−u)^{r−1} gives coefficient (1−r)_n/n! and integral
  s^{r+n}/(r+n); multiplication by r·Beta(1−r,2r) gives exactly the coefficients of
  L(s)"): verified term by term, including r/(n+r)=(r)_n/(1+r)_n.
- NEW 95–96 ("Reflection in the time interval then supplies the other half"): correct;
  the right half equals L(1−s).
- NEW 108–113 ("0<r<1/2; density behaves as distance^{−r}; square as distance^{−2r};
  both powers exceed −1"): correct for both L¹ (−r>−1) and L² (−2r>−1).
- Unchanged OLD-equivalent lines (endpoint Beta evaluations, mass computation,
  "not renormalized" statement): verified as shown above.

## Findings and limits

No rewrite defects were found: the target deductions are preserved, and every new
explanatory assertion is justified under the unchanged hypotheses (0<a<1,
r=(1−a)/2∈(0,1/2), Euler Gamma and Beta integrals as positive finite integrals,
unrenormalized f_a, s∈[0,1]). The Gamma/Beta proof is identical across revisions; its
duplication step is compressed but every step repairs to a correct identity, and this
terseness predates the rewrite. Pre-existing concerns are limited to compression of
convergence/ODE bookkeeping in Step 1 and of the Jacobian polar argument in the
Gamma/Beta proof, all checkable and correct. The Calef–Hardin citation is historical
context only; the target lemmas prove the stated identities directly. The unassigned
introductory lines define the two special functions and were used only under their
stated application hypotheses. This review is limited to preservation of the two
assigned proofs and does not certify primary-source PDFs, images, Lean correspondence,
rendered pages, or the historical source literature.

