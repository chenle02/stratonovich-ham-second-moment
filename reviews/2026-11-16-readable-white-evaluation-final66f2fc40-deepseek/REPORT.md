# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

## L:white-cdf-square

- Old reading: COMPLETE (old proof LF 26–56).
- New reading: COMPLETE (new proof LF 26–71).
- Public reconstruction: COMPLETE.

**Original-step coverage.** The proof has six logical stages. All are present in both versions; the new version adds a two-sentence roadmap, a `Step 1`/`Step 2` division, and one explanatory sentence.

1. *Locally absolutely continuous representative.* For real unit \(f\in H^1(\mathbb R)\) with \(A=\int f^4\), \(b=\int(f')^2\), the weak derivative \(f'\) is in \(L^1\) on each bounded interval by Cauchy–Schwarz, since \(f,f'\in L^2\). Its integral primitive has weak derivative \(f'\) by Fubini. Subtracting that primitive from \(f\) yields weak derivative zero, hence a locally constant representative; the locally absolutely continuous patches glue to one continuous representative. This gives \(\rho=f^2\in\operatorname{Lip}_{\mathrm{loc}}\)-type ACL with \(\rho'=2ff'\in L^1(\mathbb R)\), \(\rho\ge0\), and \(\int\rho=\int f^2=1\).

2. *Tail limits of \(\rho\).* Since \(\int|\rho'|<\infty\), \(\rho\) is Cauchy on each infinite tail, so it has finite limits at \(\pm\infty\). Integrability of \(\rho\) forces both limits to be zero: otherwise \(\rho\) would be eventually bounded below by a positive constant and \(\int\rho\) would diverge. Therefore \(\rho\) is bounded, and
\[
A=\int \rho^2\le \|\rho\|_\infty\int\rho<\infty.
\]

3. *Distribution function.* With \(\mathsf F(x)=\int_{-\infty}^x\rho\), one has \(0\le\mathsf F\le1\), \(\mathsf F'=\rho\) continuously, \(\mathsf F(-\infty)=0\), \(\mathsf F(\infty)=1\). Neither \(\rho>0\) nor strict monotonicity of \(\mathsf F\) is assumed, and neither is needed.

4. *Cross-term identity.* The derivative
\[
\frac{\mathrm d}{\mathrm dx}[\rho(1-2\mathsf F)]
=\rho'(1-2\mathsf F)-2\rho^2\in L^1(\mathbb R),
\]
and its endpoint limits vanish, because \(\rho\to0\) while \(1-2\mathsf F\to 1\) at \(-\infty\) and \(-1\) at \(+\infty\). Integrating on \([-R,R]\) and sending \(R\to\infty\):
\[
0=\int_\mathbb R\rho'(1-2\mathsf F)-2\int_\mathbb R\rho^2
=\int_\mathbb R\rho'(1-2\mathsf F)-2A.
\]
Hence \(\int \rho'(1-2\mathsf F)=2A\). Since \(\rho'=2ff'\), division by two gives
\[
\int_\mathbb R f'f(1-2\mathsf F)=A.
\]
This is exactly the added sentence in the new Step 2: “dividing the integrated derivative identity by two gives the cross term with a positive sign.” The sign is correct: \(\int f'f(1-2\mathsf F)=+A\).

5. *Square term.* With \(P(y)=y-2y^2+\tfrac43y^3\), one has
\[
P'(y)=1-4y+4y^2=(1-2y)^2.
\]
The chain rule and the endpoints of \(\mathsf F\) give
\[
\int_\mathbb R f^2(1-2\mathsf F)^2
=\int_\mathbb R P'(\mathsf F)\mathsf F'
=P(1)-P(0)=\frac13.
\]

6. *Expansion.* For each real \(z\), \(f'\in L^2\) and \(zf(1-2\mathsf F)\in L^2\), since \(0\le\mathsf F\le1\). The cross term \(|f'f(1-2\mathsf F)|\le|f'f|\in L^1\), so expansion is legitimate:
\[
\begin{aligned}
\int_\mathbb R[f'-zf(1-2\mathsf F)]^2
&=\int (f')^2-2z\int f'f(1-2\mathsf F)+z^2\int f^2(1-2\mathsf F)^2\\
&=b-2zA+\frac{z^2}{3}\ge0.
\end{aligned}
\]
This is \eqref{E:white-cdf-square}.

**Argument preservation: PRESERVED.** The new roadmap and step headings are organizational. The only new mathematical sentence (“Since \(\rho'=2ff'\), dividing … by two gives the cross term with a positive sign,” new LF ≈ 53–54) restates the already-implicit derivation of step 4.

**New explanations: JUSTIFIED.** The sentence is verified above: the integrated derivative identity yields \(\int\rho'(1-2\mathsf F)=2A\), and \(\rho'=2ff'\) gives \(\int f'f(1-2\mathsf F)=A\). The only phrasing caveat is that “the cross term with a positive sign” refers to the identity \(\int f'f(1-2\mathsf F)=+A\); inside the final expansion the corresponding term is \(-2zA\). The final displayed equation makes the sign unambiguous, so this is not a mathematical defect.

**Evidence.** Equation \eqref{E:white-cdf-square} is reproduced with the three integrals \(b\), \(A\), \(1/3\) computed independently from the definitions; the constant \(1/3\) follows from \(P(1)-P(0)=1-\tfrac{3}{3}+\tfrac{4}{3}=\tfrac13\). Substitution \(z=3A\) is also checked in the next proposition (giving \(b-3A^2\)).

**Lost steps/qualifiers, unresolved issues:** none identified within this read. The explicit qualifiers “neither positivity of \(f\) nor strictly increasing CDF is required” are preserved in both versions.

---

## P:white-spatial-energy

- Old reading: COMPLETE (old proof LF 73–105).
- New reading: COMPLETE (new proof LF 88–133).
- Public reconstruction: COMPLETE.

**Original-step coverage.**

1. *Sharp ratio bound.* Substitute \(z=3A\) into \eqref{E:white-cdf-square}:
\[
0\le b-2(3A)A+\frac{(3A)^2}{3}=b-6A^2+3A^2=b-3A^2,
\]
so
\[
3A^2\le b.
\]
The proof explicitly records this as the exact premise/conclusion of the unassigned conditional WhiteCDF deduction, whose application conditions are satisfied: \(f\in H^1\) real unit, \(A<\infty\) by lemma \ref{L:white-cdf-square}. The proof verifies \(A>0\) (if \(A=0\) then \(f=0\) a.e., contradicting unit mass) and \(b>0\) (if \(b=0\), the continuous representative is constant; the only \(L^2\) constant on \(\mathbb R\) is zero, again contradicting unit mass). Thus
\[
\frac A{\sqrt b}\le\frac1{\sqrt3}.
\]

2. *Hyperbolic-secant profile.* For \(\ell>0\), \(f_\ell(x)=\sqrt{\ell/2}\operatorname{sech}(\ell x)\). Then
\[
f_\ell'=-\ell\tanh(\ell x)f_\ell,\qquad
\mathrm dt=\ell\operatorname{sech}^2(\ell x)\,\mathrm dx,\quad t=\tanh(\ell x).
\]
Direct integration:
\[
\int f_\ell^2=\frac{\ell}{2}\cdot\frac1\ell\int_{-1}^1\mathrm dt=1,
\]
\[
\int f_\ell^4=\frac{\ell^2}{4}\cdot\frac1\ell\int_{-1}^1(1-t^2)\,\mathrm dt
=\frac\ell4\cdot\frac43=\frac\ell3,
\]
\[
\int(f_\ell')^2=\frac{\ell^3}{2}\cdot\frac1\ell\int_{-1}^1t^2\,\mathrm dt
=\frac{\ell^2}{2}\cdot\frac23=\frac{\ell^2}{3}.
\]
Hence
\[
\frac{A}{\sqrt b}=\frac{\ell/3}{\ell/\sqrt3}=\frac1{\sqrt3},
\]
attaining the ratio bound. For the physical ratio \(R_{\mathrm{sp}}=\sup cA/\sqrt b\) with \(\Gamma=c\delta_0\), this gives \(R_{\mathrm{sp}}=c/\sqrt3\).

3. *Dirac caveat.* The sentence that the Dirac measure introduces no Fourier constant or nonintegrable convolution kernel \(|x|^{-1}\) is correct: for \(\Gamma=\delta_0\),
\[
A_{\mathrm{sp}}(f)=B_\Gamma(f^2,f^2)
=\int_{\mathbb R}f^2(x)f^2(x-y)\delta_0(\mathrm dy)\,\mathrm dx
=\int f^4=A,
\]
the direct pairing, with no distributional inverse-Fourier kernel. This matches the instruction to distinguish Dirac covariance \(\delta_0\) from \(|x|^{-1}\).

4. *Energy bound.* The existing conditional energy deduction applied to \(3A^2\le b\), with \(c>0\):
\[
cA-\frac b2\le cA-\frac32A^2
=\frac{c^2}{6}-\frac32\left(A-\frac c3\right)^2\le\frac{c^2}{6}.
\]
The completed square is checked:
\[
\frac{c^2}{6}-\frac32\left(A-\frac c3\right)^2
=\frac{c^2}{6}-\frac32A^2+cA-\frac{c^2}{6}
=cA-\frac32A^2.
\]
Thus \(\mathcal E_{\mathrm{sp}}=\sup(cA-b/2)\le c^2/6\).

5. *Attainment at \(\ell=c\).* For \(f_c\), \(A=c/3\) and \(b=c^2/3\), so
\[
cA-\frac b2=\frac{c^2}{3}-\frac{c^2}{6}=\frac{c^2}{6},
\]
and \(A=c/3\) is exactly the maximizer of the completed square. Therefore \(\mathcal E_{\mathrm{sp}}=c^2/6\).

6. *Zero covariance case.* At \(c=0\), \(A_{\mathrm{sp}}=0\), so \(R_{\mathrm{sp}}=0\) and
\[
\mathcal E_{\mathrm{sp}}=\sup_{\|g\|_2=1}\left(-\frac{b(g)}2\right)=0.
\]
The supremum is approached by \(f_\ell\) as \(\ell\downarrow0\) since \(b_\ell=\ell^2/3\to0\), while each \(f_\ell\) remains unit. No zero-scale or zero-gradient unit vector is used, as stated.

7. *Profile class and formalization caveats.* The proof explicitly retains that these are full \(H^1\) profiles; equality for compact approximations is supplied by unassigned Proposition~\ref{P:spatial-four-linear}, and the noncompact profile itself is not claimed to be a compact stochastic control. The CDF, integral and attainment arguments remain analytic; the two finite conditional deductions do not formalize them. All retained in the new version.

**Argument preservation: PRESERVED.**

**New explanations: JUSTIFIED.** The added roadmap and step headings are organizational. The added sentence “The coefficient is covariance mass \(c\) in the physical pairing, not a noise coefficient of size \(c\)” is justified by the module preamble: “The parameter \(c\) is covariance mass; the coefficient of unit noise would be \(\sqrt c\).” Consequently \(A_{\mathrm{sp}}=cA\) uses \(c\), while the moment bounds scale as \(\sqrt c\).

**Evidence.** All integrals for \(f_\ell\) are recomputed explicitly above; the sharp ratio \(c/\sqrt3\) and energy \(c^2/6\) are derived from \eqref{E:white-cdf-square} and the completed-square argument. Cross-check with the unassigned energy formula at \(\alpha=1\),
\[
\mathcal E_{\mathrm{sp}}=\frac{2-\alpha}{2}\alpha^{\alpha/(2-\alpha)}R_{\mathrm{sp}}^{2/(2-\alpha)}
=\frac12R_{\mathrm{sp}}^2=\frac12\cdot\frac{c^2}{3}=\frac{c^2}{6},
\]
is consistent.

**Lost steps/qualifiers, unresolved issues:** none identified. The distinctions (covariance mass \(c\) vs noise amplitude \(\sqrt c\); \(\delta_0\) vs \(|x|^{-1}\); full \(H^1\) profiles vs compact controls) are all retained.

---

## T:white-moment-bounds

- Old reading: COMPLETE (old proof LF 125–139).
- New reading: COMPLETE (new proof LF 153–167).
- Public reconstruction: COMPLETE.

**Original-step coverage.**

1. *Exponents.* With \(d=\alpha=1\), the upstream conventions give
\[
q=4-\alpha=3,\qquad k=3-\alpha=2,\qquad m=\frac qk=\frac32.
\]
These match the proof’s opening “\(q=3,k=2,m=3/2\).”

2. *Instantiate \(F_0\).* From \eqref{E:spatial-static-energy-score},
\[
F_0(z)=k\left[\frac{(2z/(2-\alpha))^{(2-\alpha)/2}}{8q^{q/2}}\right]^{1/k}.
\]
At \(\alpha=1\), \(2-\alpha=1\), \((2-\alpha)/2=1/2\), so
\[
F_0(z)=2\left[\frac{(2z)^{1/2}}{8\cdot3^{3/2}}\right]^{1/2}.
\]

3. *White energy input.* From Proposition~\ref{P:white-spatial-energy}, \(\mathcal E_{\mathrm{sp}}=c^2/6\) for \(c>0\), so
\[
\sqrt{2\mathcal E_{\mathrm{sp}}}=\sqrt{c^2/3}=\frac c{\sqrt3}.
\]

4. *Evaluate \(F_0(\mathcal E_{\mathrm{sp}})\).*
\[
F_0(\mathcal E_{\mathrm{sp}})
=2\left[\frac{c/\sqrt3}{8\cdot3^{3/2}}\right]^{1/2}
=2\sqrt{\frac c{72}}
=\frac{\sqrt c}{3\sqrt2}.
\]
Indeed
\[
\frac{c/\sqrt3}{8\cdot3^{3/2}}
=\frac{c}{8\cdot3^{1/2}\cdot3^{3/2}}
=\frac{c}{8\cdot3^2}
=\frac c{72}.
\]

5. *Apply \(2^m\).*
\[
2^mF_0(\mathcal E_{\mathrm{sp}})
=2^{3/2}\cdot\frac{\sqrt c}{3\sqrt2}
=2\sqrt2\cdot\frac{\sqrt c}{3\sqrt2}
=\frac23\sqrt c.
\]

6. *Common bracket.* Corollary~\ref{C:intrinsic-spatial-bracket} gives
\[
2^mM_a^{-1/k}F_0(\mathcal E_{\mathrm{sp}})
\le C_2(c,a)
\le2^mK_0^{1/k}F_0(\mathcal E_{\mathrm{sp}}).
\]
With \(k=2\):
\[
\frac23\sqrt c\,M_a^{-1/2}
=\frac23\sqrt{\frac c{M_a}},
\]
and
\[
\frac23\sqrt c\,K_0^{1/2}
=\frac23\sqrt{cK_0(a)}.
\]
Together with \(K_0(a)=2^a/(1-a)\) and
\[
M_a=\frac{\Gamma_E((1+a)/2)}{\Gamma_E(1+a)\Gamma_E((1-a)/2)},
\]
this is exactly \eqref{E:white-moment-bounds}.

7. *Zero covariance case.* At \(c=0\), the model assumptions give \(u=1\), and Theorem~\ref{T:intrinsic-second-moment} gives \(C_2=0\). Both displayed bounds have the factor \(\sqrt c\) and vanish: \((2/3)\sqrt{c/M_a}=0\), \((2/3)\sqrt{cK_0(a)}=0\).

8. *Qualifiers.* The time exponent is
\[
\frac{4-\alpha-a}{3-\alpha}\Big|_{\alpha=1}
=\frac{3-a}{2},
\]
matching the statement. The statement’s “these are bounds, not a numerical evaluation of the intrinsic supremum” is preserved.

**Argument preservation: PRESERVED.** The new proof text appears identical to the old proof text (only line numbers shifted); no new explanatory assertions were inserted.

**New explanations: JUSTIFIED.** No new explanatory sentence is added in this proof; the unchanged argument is internally justified as recomputed above.

**Evidence.** The constants \(F_0(\mathcal E_{\mathrm{sp}})=\sqrt c/(3\sqrt2)\) and \(2^mF_0=(2/3)\sqrt c\) are recomputed from the supplied formula; the bracket substitution yields exactly the displayed lower and upper bounds. The positivity/finiteness of all Gamma factors for \(0<a<1\) follows because \(\Gamma_E\) is positive finite on \((0,\infty)\).

**Lost steps/qualifiers, unresolved issues:** none identified. The original temporal kernel \(|s-t|^{-a}\), kinetic normalization, \(c=0\) treatment, and bounds-vs-evaluation limit are all retained.

---

## C:white-relative-width

- Old reading: COMPLETE (old proof LF 155–176).
- New reading: COMPLETE (new proof LF 183–204).
- Public reconstruction: COMPLETE.

**Original-step coverage.**

1. *Ratio of the two bounding formulas.* For \(c>0\),
\[
\frac{\frac23\sqrt{cK_0(a)}}{\frac23\sqrt{c/M_a}}
=\sqrt{K_0(a)M_a}.
\]

2. *Gamma identities.* From Lemma~\ref{L:equilibrium-gamma-beta} with positive arguments:
\[
\Gamma_E(1+a)
=\frac{2^a}{\sqrt\pi}\Gamma_E\!\left(\frac{1+a}{2}\right)\Gamma_E\!\left(1+\frac a2\right),
\]
(the duplication formula with \(x=(1+a)/2\)), and
\[
(1-a)\Gamma_E\!\left(\frac{1-a}{2}\right)
=2\Gamma_E\!\left(\frac{3-a}{2}\right),
\]
(the recurrence \(\Gamma(x+1)=x\Gamma(x)\) with \(x=(1-a)/2\)). All arguments are positive for \(0<a<1\), so the identities apply.

3. *Compute \(K_0M_a\).* Since
\[
K_0(a)=\frac{2^a}{1-a},
\]
one has
\[
K_0M_a
=\frac{2^a\Gamma_E((1+a)/2)}
{(1-a)\Gamma_E(1+a)\Gamma_E((1-a)/2)} .
\]
Performing the substitutions spelled out above:
\[
K_0M_a
=\frac{2^a\Gamma_E((1+a)/2)}
{2\Gamma_E((3-a)/2)\cdot\frac{2^a}{\sqrt\pi}\Gamma_E((1+a)/2)\Gamma_E(1+a/2)}
=\frac{\sqrt\pi}{2\Gamma_E(1+a/2)\Gamma_E((3-a)/2)} .
\]
This matches the displayed identity.

4. *Set \(x=1+a/2\), \(y=(3-a)/2\).* Then \(x,y>0\) and
\[
x+y=\left(1+\frac a2\right)+\left(\frac32-\frac a2\right)=\frac52.
\]

5. *Cauchy–Schwarz in the Gamma integral.* On \(L^2(0,\infty)\),
\[
u(t)=t^{(x-1)/2}e^{-t/2},\qquad
v(t)=t^{(y-1)/2}e^{-t/2}.
\]
Then
\[
\|u\|^2=\int_0^\infty t^{x-1}e^{-t}\,\mathrm dt=\Gamma_E(x),
\]
\[
\|v\|^2=\Gamma_E(y),
\]
and
\[
\langle u,v\rangle
=\int_0^\infty t^{(x+y-2)/2}e^{-t}\,\mathrm dt
=\int_0^\infty t^{1/4}e^{-t}\,\mathrm dt
=\Gamma_E(5/4),
\]
since \((x+y)/2=5/4\). Cauchy–Schwarz gives
\[
\Gamma_E(5/4)^2=\langle u,v\rangle^2
\le\|u\|^2\|v\|^2=\Gamma_E(x)\Gamma_E(y).
\]

6. *Invert and take the increasing square root.* All quantities are positive, so inversion reverses the inequality:
\[
\frac1{\Gamma_E(x)\Gamma_E(y)}
\le\frac1{\Gamma_E(5/4)^2}.
\]
Multiplying by \(\sqrt\pi/2>0\) and taking the increasing square root:
\[
\sqrt{K_0M_a}
=\left(\frac{\sqrt\pi}{2\Gamma_E(x)\Gamma_E(y)}\right)^{1/2}
\le\left(\frac{\sqrt\pi}{2\Gamma_E(5/4)^2}\right)^{1/2}.
\]

7. *Equality at \(a=1/2\).* Then \(x=y=5/4\), so \(u=v\) and Cauchy–Schwarz holds with equality; hence all subsequent steps hold with equality.

8. *Symmetry clause.* Replacing \(a\) by \(1-a\) sends
\[
1+\frac a2\longleftrightarrow\frac{3-a}{2},
\]
i.e. exchanges \(x\) and \(y\). Since \(K_0M_a=\sqrt\pi/[2\Gamma(x)\Gamma(y)]\) is symmetric in \((x,y)\), the ratio of the two bounding formulas is symmetric under \(a\mapsto1-a\). The moment constant \(C_2\) and the time exponent \((3-a)/2\) are not symmetric; the proof states exactly this distinction.

**Argument preservation: PRESERVED.** The new proof text appears identical to the old proof text (only line numbers shifted); no new explanatory assertions were inserted.

**New explanations: JUSTIFIED.** No new explanatory sentence is added; the existing argument is recomputed and verified above.

**Evidence.** The algebra reducing \(K_0M_a\) to \(\sqrt\pi/[2\Gamma(1+a/2)\Gamma((3-a)/2)]\) is recomputed explicitly; the \(L^2\) inner product \(\Gamma(5/4)\) is verified; and the inversion/monotonicity step is checked. Equality at \(a=1/2\) follows from \(x=y=5/4\).

**Lost steps/qualifiers, unresolved issues:** none identified.

---

## AUDIT dispositions

The assigned module contains no `AUDIT` or TODO markers. No AUDIT-worthy issue is introduced by the rewrite. The two non-organizational additions in the new version are:

1. L:white-cdf-square, new LF ≈ 53–54: “Since \(\rho'=2ff'\), dividing the integrated derivative identity by two gives the cross term with a positive sign.” This is mathematically verified; the only minor wording caveat is that “positive sign” refers to \(\int f'f(1-2\mathsf F)=+A\), while the term in the final expansion carries \(-2zA\). The displayed formula removes any ambiguity, so this does not rise to an AUDIT item.

2. P:white-spatial-energy, the sentence “The coefficient is covariance mass \(c\) in the physical pairing, not a noise coefficient of size \(c\).” This is verified against the module preamble and is correct.

No AUDIT-worthy defect found in the assigned module as presented.

## Findings and limits

The rewrite in `notes/integrated_white_evaluation.tex` from `cdde711c…` to `66f2fc4…` is a readability-only revision: it inserts a two-sentence roadmap and two displayed step headings in L:white-cdf-square, and inserts a roadmap, two step headings, and one clarifying sentence in P:white-spatial-energy; T:white-moment-bounds and C:white-relative-width are unchanged in mathematical content. The unchanged statements at the inventory line ranges are identical in content. All four assigned proofs are fully read in both revisions and publicly reconstructed above with explicit working; no missing derivation was silently supplied.

The mathematical checks confirm: the one-dimensional \(H^1\) ACL representative and CDF square identity, including the tail limits, absolute integrability, and the cross-term sign, without assuming positive \(f\) or strict monotonicity of the CDF; the sharp spatial ratio \(c/\sqrt3\) and original physical energy \(c^2/6\) via the sech family with \(\ell=c\), and the \(c=0\) limiting profile without a zero-scale unit vector; the exact white moment constants
\[
\frac23\sqrt{\frac c{M_a}}\le C_2(c,a)\le\frac23\sqrt{cK_0(a)}
\]
from the supplied common bracket; and the Gamma duplication/recurrence reduction of \(K_0M_a\) with equality at \(a=1/2\) at the stated temporal exponent \((3-a)/2\). The distinctions between covariance mass \(c\) and noise amplitude \(\sqrt c\), between Dirac covariance \(\delta_0\) and the inverse kernel \(|x|^{-1}\), and between full \(H^1\) profiles and compact stochastic controls are preserved and used consistently. The original temporal kernel, kinetic normalization, strict temporal range \(0<a<1\), and the \(c=0\) treatment are retained; no white-time, Skorohod, source-constant, or numerical-evaluation substitution occurs.

I did not independently certify the unassigned upstream proofs (spatial energy map, occupation ceiling, intrinsic second-moment theorem, temporal equilibrium, model assumptions). I used their stated inputs under their checked hypotheses only, as instructed. The explicit limitation that the two conditional Lean deductions do not formalize the CDF, analytic integral, or attainment arguments is preserved, not introduced, in the new version. The review is confined to the embedded old/new modules and the supplied baseline contexts; no tools, files, network, rendering, or Lean quotation verification were used. The overall verdict is PASS_WITH_NOTES solely because of the two added explanatory sentences, which are sound but could in principle be reworded for maximal clarity.
