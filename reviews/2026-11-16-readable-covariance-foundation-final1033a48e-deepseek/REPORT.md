# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

The notes are confined to a single informal roadmap sentence in the new
proof of `P:masked-noise-completion`; the surrounding computation, and all
eight rewritten proofs, are mathematically equivalent to the old arguments and
do not lose hypotheses, quantifiers, or constants. This does not certify the
later wave/operator/no-go results referenced contextually in the module.

---

## P:masked-spectral-growth

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Finiteness of `M_Gamma`: temperedness makes the Gaussian integral finite;
     `Gamma != 0` makes it strictly positive since the Gaussian is everywhere positive.
  2. One-dimensional Gaussian Fourier computation: `J(b) = int_R e^{-Ax^2} e^{ibx}dx`,
     `J(0)=sqrt(pi/A)`; differentiating under the integral and integrating by parts
     give `J'(b) = -bJ(b)/(2A)`, so `J(b)=sqrt(pi/A)e^{-b^2/(4A)}`.
  3. Product over coordinates:
     `int_{R^d} e^{-r^2|x|^2/4} e^{i(xi-y)·x}dx = (2 sqrt(pi)/r)^d e^{-|xi-y|^2/r^2}`.
  4. Apply the spectral convention `(E:masked-spectral-convention)` to the single
     Schwartz test `e^{-r^2|x|^2/4}e^{-iy·x}`, obtaining
     `(E:masked-gaussian-transform)`.
  5. The left side of `(E:masked-gaussian-transform)` is nonnegative; since `Gamma`
     is nonnegative, the absolute value of the right side equals the integral of
     the absolute Gaussian.
  6. Homogeneity `Gamma(cA)=c^{d-alpha}Gamma(A)` gives the pushforward scaling:
     `int e^{-r^2|x|^2/4}Gamma(dx) = r^{alpha-d}M_Gamma`.
  7. The Gaussian bound follows with the prefactor `r^d/(2 sqrt(pi))^d`.
  8. On a ball `B(y,r)` the Gaussian is at least `e^{-1}`, so
     `mu(B(y,r)) <= e * r^alpha M_Gamma/(2 sqrt(pi))^d = C_Gamma r^alpha`.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence (OLD proof LF 57-80; NEW proof LF 57-94):
  The new Step 1 justification that differentiation of `J(b)` is permitted by its
  integrable first moment and that Gaussian decay kills the boundary term in the
  integration by parts is correct. The explicit multiplication check
  `(r^d/(2 sqrt(pi))^d)(r^{alpha-d}M_Gamma)=r^alpha M_Gamma/(2 sqrt(pi))^d` is
  exact. Statements at OLD/NEW LF 37-55 are unchanged, including
  `C_Gamma = eM_Gamma/(2 sqrt(pi))^d` and the open/closed ball clause.
- Lost steps/qualifiers: none identified within this read.
- Unresolved issues/pre-existing concerns: none identified within this read.

---

## P:masked-auxiliary-norm

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. `k_R(u)=R^d hat zeta(Ru)` and `||k_R||_1=L` are used throughout.
  2. Density finiteness and continuity: for each `eta`, Schwarz decay of `k_R`
     plus polynomial growth of `mu` make `rho_R(eta)` finite; on compact sets of
     `eta` a common rapid-decay majorant is chosen with decay power large enough
     to be `mu`-integrable; dominated convergence gives continuity, hence
     `nu_R` is Radon.
  3. Evenness: `zeta` real gives `k_R(-u)=overline{k_R(u)}`; evenness of `mu`
     gives evenness of `rho_R`.
  4. Ball mass via Tonelli: with `u=xi-eta` and `xi in B(y+u,r)` when
     `eta in B(y,r)`,
     `nu_R(B(y,r)) = c_d^2 L int |k_R(u)| mu(B(y+u,r))du`.
     Applying `P:masked-spectral-growth` and `||k_R||_1=L` gives
     `(E:masked-auxiliary-growth)`, independent of `R`.
  5. Temperedness follows from the polynomial growth of centered ball masses and
     the same dyadic-shell argument as in the preamble.
  6. Hilbert-valued Bochner convolution identity:
     `widehat{zeta_R F}(xi) = c_d int k_R(xi-eta) widehat F(eta)d eta`.
     This is the unitary-transform product formula: `widehat{fg}(xi)=c_d int
     hat f(xi-eta)hat g(eta)d eta`. The scalar case is Fourier inversion; the
     finite-rank and general separable-range cases follow by projections of norm
     at most one and dominated convergence; zero and finite-dimensional spaces are
     explicit.
  7. Weighted Cauchy-Schwarz:
     `||widehat{zeta_R F}(xi)||_H^2 <= c_d^2 L int |k_R(xi-eta)|||widehat F(eta)||_H^2 d eta`.
  8. Integrate against `mu` and apply Tonelli to obtain
     `(E:masked-hilbert-fourier)`.
  9. The real-Hilbert-space clause follows by complexifying `H` with preserved
     norm and separability.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence (OLD proof LF 106-141; NEW proof LF 120-180):
  The new Step 1 uses "For fixed `R`" and correctly limits the common decay
  majorant to compact `eta` sets; this distinguishes fixed-radius density
  continuity from the radius-uniform ball bound
  `(E:masked-auxiliary-growth)`. The new Step 2 explanation of the `c_d` product
  constant is correct under the stated unitary convention. The new Step 3 is
  only a roadmap; the integrations are the same as OLD.
- Lost steps/qualifiers: none. The real-`H` complexification clause is stated in
  the proposition and not expanded in either proof; the standard complexification
  argument covers it, so no rewrite defect.
- Unresolved issues/pre-existing concerns: none identified within this read.

---

## L:masked-time-completion

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Positivity is obtained from
     `|t-s|^{-a} = 1/Gamma_E(a) int_0^infty lambda^{a-1}e^{-lambda|t-s|}d lambda`,
     with
     `e^{-lambda|t-s|} = int_{-infty}^{min(t,s)} 2lambda e^{-lambda(t-u)}e^{-lambda(s-u)}du`.
     For fixed `lambda>0` the associated quadratic form is the integral of a
     square, so the temporal form is positive semidefinite.
  2. Row/column integrability: for fixed `t`,
     `int_0^T |t-s|^{-a}ds = [t^{1-a}+(T-t)^{1-a}]/(1-a) <= 2T^{1-a}/(1-a)`.
     This justifies the exchanges for compact smooth tests.
  3. Schur bound: `2|xy| <= |x|^2+|y|^2` and the row bound give
     `(E:masked-time-schur)`.
  4. Separability: a countable `L^2`-dense family of compact smooth tests is
     dense in the null-quotient completion `H_a`.
  5. Complexification: for the real symmetric kernel, the imaginary cross term
     cancels, so the complex norm is the same double integral with
     `f(t)overline{f(s)}`.
  6. `L^2` extension: smooth density plus the Schur bound on the absolute bilinear
     form extends both the inclusion and the integral identity to `L^2(0,T)`,
     including bounded measurable interval amplitudes extended by zero.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence (OLD proof LF 167-190; NEW proof LF 206-241):
  The added explicit row computation
  `[t^{1-a}+(T-t)^{1-a}]/(1-a) <= 2T^{1-a}/(1-a)` is correct because each summand
  is at most `T^{1-a}` and the sum therefore at most `2T^{1-a}`. The new Step 1/2
  split does not alter the representation or the Schur constant
  `2T^{1-a}/(1-a)`.
- Lost steps/qualifiers: none identified within this read.
- Unresolved issues/pre-existing concerns: none identified within this read.

---

## P:masked-noise-completion

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Spatial covariance identification: for real Schwartz `f,g`, define
     `h(z)=int f(y+z)g(y)dy`. Fourier inversion and Parseval give
     `h(z) = int e^{i xi·z} widehat f(xi) overline{widehat g(xi)}d xi`.
  2. Computing
     `int e^{i xi·z}h(z)dz = (2pi)^d widehat f(-xi) overline{widehat g(-xi)}`
     follows from `int e^{i(xi+eta)z}dz = (2pi)^d delta_0(xi+eta)`.
  3. Apply `(E:masked-spectral-convention)` to the Schwartz test `h`, then reflect
     `xi` using evenness of `mu`:
     spatial covariance equals
     `(2pi)^d int widehat f(xi) overline{widehat g(xi)}mu(d xi)`.
  4. Summing the finitely many temporal factors gives
     `(E:masked-actual-noise-norm)`.
  5. Continuity and admission of `D` into the original completion use Schwartz
     decay, temperedness, temporal integrability, and smooth expanding cutoffs.
  6. Apply `P:masked-auxiliary-norm` with `H=H_a^{mathbb C}` to get
     `E W(zeta_R F)^2 <= N_R(F)^2`. The auxiliary null class is annihilated; an
     auxiliary Cauchy sequence becomes an `L^2(Omega)` Cauchy sequence, giving the
     contraction extension and uniqueness.
  7. Gaussianity of limits: finite linear combinations of finite-dimensional
     Gaussian limits have converging covariances, so characteristic functions
     give centered joint Gaussian limits.
  8. Covariance comparison: with `A` the masked covariance matrix and `B` the
     auxiliary Gram matrix, `b^TAb <= b^TBb` for all real `b`; since `B-A` is
     positive semidefinite, construct a centered Gaussian `Z` independent of `X`
     on a product space with covariance `B-A`. Then `X+Z` has covariance `B`, and
     conditional Jensen gives `E||X||^p <= E||X+Z||^p` for every norm and
     `p>=1`; finite Gaussian moments give finiteness.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED, with one wording note
- Evidence (OLD proof LF 218-257; NEW proof LF 269-328):
  The inserted sentence "the product of the two Fourier transforms is Schwartz,
  so the inverse Fourier identity can be applied again" is a slightly informal
  summary of the `c_d`-normalized inversion/Parseval computation; the constants in
  the displayed lines are nevertheless correct and reproduce the factor
  `(2pi)^d`. The added Jensen explanation for Step 3 is standard and correct.
  The later module disclaimer asserting that no multiplier on the noise quotient
  and no nonlinear covariance comparison is claimed remains present.
- Lost steps/qualifiers: none identified within this read.
- Unresolved issues/pre-existing concerns: the informal roadmap sentence is not
  an error; it is the only note. No pre-existing mathematical concern found.

---

## P:masked-quotient-obstruction

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. In the spectral convention, `Gamma=delta_0(dx_1)dx_2` has
     `mu=(2pi)^{-1}d xi_1 delta_0(d xi_2)`, because the Fourier transform of
     `delta_0(dx_1)dx_2` is `(2pi)delta_0(d xi_2)` and the convention has
     `Gamma = int e^{i xi·x}mu(d xi)`.
  2. Hypothesis check: `Gamma` is nonnegative, even, positive definite, tempered,
     with `Gamma(cA)=c Gamma(A)`, so it satisfies `H:homog` with `d=2`,
     `alpha=1`; it is not two-dimensional spatial white noise.
  3. Spatial covariance for real compact smooth `g` is, by Fubini,
     `V(g)=int_R (int_R g(x_1,x_2)dx_2)^2 dx_1`.
  4. Bose-plateau function `chi` equal to 1 on `[-1,1]`, supported in `[-2,2]`,
     built with the displayed smooth pasting; set
     `I_chi=int(chi')^2>0`, `J_chi=int chi^4>0` (indeed `J_chi>=2`).
  5. Put `g(x)=chi(x_1)chi''(x_2)` and `zeta(x)=chi(x_1)chi(x_2)`.
     Then `int g(x_1,·)dx_2=0`, so `V(g)=0`.
  6. For the masked test, `int zeta g dx_2 = -I_chi chi(x_1)^2`, so
     `V(zeta g)=J_chi I_chi^2>0`.
  7. Choose a nonzero nonnegative `tau in C_c^infty(0,T)`; the temporal factor
     `||tau||_a^2` is finite and strictly positive because the nonnegative
     integrand is positive on a set of positive two-dimensional measure.
     Therefore `E W(F)^2=0` while `E W(zeta F)^2>0`, ruling out any finite `C`.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence (OLD proof LF 276-303; NEW proof LF 347-382):
  The new Step 1/Step 2 split adds no new assertion. The only added text is
  organizational. The counterexample lies in the admissible singular covariance
  class indicated by the statement (`d=2`, `alpha=1`, `0<a<1`), and the
  construction does not invoke spatial white noise.
- Lost steps/qualifiers: none identified within this read.
- Unresolved issues/pre-existing concerns: none identified within this read.

---

## L:masked-temporal-modulation

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Define
     `c(v)=int_s^{s+h-v} A(u+v)overline{A(u)}du` for `0<=v<=h`.
  2. Differentiation gives
     `c'(v)=-A(s+h)overline{A(s+h-v)} + int_s^{s+h-v}A'(u+v)overline{A(u)}du`,
     so `c(h)=0`, `|c(v)|<=hM^2`, `|c'(v)|<=M^2+hMD`.
  3. Splitting the covariance square into the two conjugate triangles gives
     `||1_I A e^{i omega t}||_a^2
      = 2 Re int_0^h v^{-a}e^{i omega v}c(v)dv
      = 2h^{2-a} Re int_0^1 y^{-a}e^{i omega h y}f(y)dy`,
     with `f(y)=c(hy)/h`, `f(1)=0`, `|f|,|f'|<=K^2`, `K=M+hD`.
  4. Low frequency `|omega h|<=1`: use `int_0^1 y^{-a}dy=1/(1-a)` and
     `|f|<=K^2`; the bracket lower bound is
     `<omega h>^{a-1} >= 2^{(a-1)/2}`. The needed constant check is
     `2/(1-a) <= C_0(a)2^{(a-1)/2}`, which holds since `C_0=16/(1-a)` and
     `2 <= 16·2^{-(1-a)/2}` for `0<a<1`.
  5. High frequency `k=|omega h|>1`: on `[0,1/k]`, bound
     `K^2 k^{a-1}/(1-a)`.
  6. On `[1/k,1]`, integrate by parts. The endpoint at 1 vanishes because
     `f(1)=0`; the endpoint at `1/k` contributes at most `K^2 k^{a-1}`.
  7. The derivative term, divided by `k`, is at most
     `K^2/k(a int_{1/k}^1 y^{-a-1}dy + int_{1/k}^1 y^{-a}dy)
      <= K^2 k^{a-1}(1+1/(1-a))`.
     Here `k^{-1}<=k^{a-1}` uses `a>0`.
  8. Total high-frequency bound: `4K^2 k^{a-1}/(1-a)`, since
     `1/(1-a)+1+1+1/(1-a) <= 4/(1-a)`.
  9. Compare brackets: `k^{a-1} <= sqrt2 <omega h>^{a-1}` for `k>1`, and
     `8 sqrt2 <=16`; including `2h^{2-a}` proves the stated bound.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence (OLD proof LF 328-362; NEW proof LF 407-452):
  The new explicit low-frequency constant check is the only added mathematical
  assertion and it is correct. The new Step 2 roadmap correctly describes the
  high-frequency partition as separating the singular endpoint before integrating
  by parts.
- Lost steps/qualifiers: none identified within this read.
- Unresolved issues/pre-existing concerns: none identified within this read.

---

## L:masked-trig-products

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Each of `P_r Q_rho` expands into four complex exponential modes with
     frequencies `sigma r + tau rho`, `sigma,tau in {-1,1}`, and coefficients of
     absolute value `1/4`.
  2. The Hilbert-space inequality
     `||sum_j c_j v_j||^2 <= (sum_j |c_j|) sum_j |c_j|||v_j||^2`
     follows from the triangle inequality followed by Cauchy-Schwarz applied to
     `|c_j|^{1/2}` and `|c_j|^{1/2}||v_j||`.
  3. Here `sum_j |c_j|=1`, so `||sum c_j v_j||^2 <= sum|c_j|||v_j||^2`.
  4. Apply `L:masked-temporal-modulation` to each mode: two frequencies have
     absolute value `|r-rho|` and two have `r+rho`. This yields
     `(1/2)C_0(a)h^{2-a}(M+hD)^2 Q_h(r,rho)`, which is no larger than the asserted
     `(E:masked-trig-products)`.
  5. Repeated or zero frequencies are allowed; no orthogonality or independence
     is used.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence (OLD proof LF 384-398; NEW proof LF 474-491):
  The added derivation of the Hilbert-space inequality is correct. The new text
  does not change the coefficients, frequencies, or the factor `1/2`.
- Lost steps/qualifiers: none identified within this read.
- Unresolved issues/pre-existing concerns: none identified within this read.

---

## L:masked-continuous-wave

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Representation of factors:
     - `c_r(t)=cos(rt)` needs no adjustment.
     - For `r>=1`, `b_r(t)=<r> sin(rt)/r` is a sine with coefficient at most
       `sqrt2`.
     - For `0<=r<=1`, the fundamental theorem of calculus gives
       `b_r(t)=t<r> int_0^1 cos(vrt)dv`; at `r=0` this is exactly `t`.
  2. Therefore `F_r G_rho` equals a scalar coefficient of absolute value at most
     two times a normalized average of `t^j P_{r'}(t)Q_{rho'}(t)`, with
     `j in {0,1,2}`, `|r'-r|<=1`, `|rho'-rho|<=1`; zero-average cases use a
     one-point probability space.
  3. Parameter continuity: each `t^j P_{r'}Q_{rho'}` depends continuously on the
     parameters in `L^2(0,T)` by dominated convergence, and hence in `H_a` by
     the continuous inclusion from `L:masked-time-completion`.
  4. The normalized averages are Bochner integrals in `H_a`; continuity of the
     inclusion makes the `H_a` image agree with the pointwise average. Hilbert
     Jensen gives `||mean n||^2 <= mean ||n||^2`.
  5. Apply `L:masked-trig-products` to each integrand with `A(t)=t^j`:
     `M+hD` is at most `1`, `T+1`, `T^2+2T` for `j=0,1,2`, and each square is at
     most `(1+T)^4`.
  6. Frequency comparison: for real `x,e`,
     `<x>/(1+|e|) <= <x+e> <= (1+|e|)<x>`. The changes in `h(r±rho)` have
     magnitude at most two because `h<=1`. Since `a-1<0`, each altered bracket
     raised to `a-1` is at most `3^{1-a}` times the original. Combining the
     squared coefficient bound `4`, Jensen, and `C_0` gives
     `C_1(a)=4·3^{1-a}C_0(a)`.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence (OLD proof LF 415-446; NEW proof LF 508-558):
  The added Step 1 computation of
  `b_r(t)=t<r>int_0^1 cos(vrt)dv` at `r=0` is correct, as is the added
  explanation of the bracket inequality via the Euclidean norm of `(1,x)` and the
  triangle inequality. The new text does not change the leading constant
  `C_1(a)=4·3^{1-a}C_0(a)` or the factor `(1+T)^4`.
- Lost steps/qualifiers: none identified within this read.
- Unresolved issues/pre-existing concerns: none identified within this read.

---

## AUDIT dispositions

No AUDIT-worthy issues were found in the assigned module. In particular, no
uncountable null-set intersection, no noise-quotient multiplier, no uniform
density bound in `R`, and no nonlinear wave covariance monotonicity are silently
asserted. The disclaimers after `P:masked-noise-completion` are retained in the
new module. The sentence in the new `P:masked-noise-completion` Step 1 about the
"inverse Fourier identity" is informal but supported by the displayed computation,
so it is a note rather than an AUDIT item.

## Findings and limits

All eight assigned proofs were read completely in both OLD and NEW versions and
publicly reconstructed with checkable estimates. The statements and definitions
at the listed local line ranges are unchanged; no step, qualifier, constant, or
limiting order was lost. The added roadmaps and explanatory sentences are each
mathematically justified under the same hypotheses, with the single informal
wording noted above.

The review uses the unassigned baseline `H:homog` from
`notes_stratonovich_ham_second_moment.tex` only after checking its supplied
hypotheses against the target consumer uses. The later wave/operator application
reference, the `No-go22` citation, and all upstream results outside the assigned
module are not certified by this packet. No tools, files, or network were used.
