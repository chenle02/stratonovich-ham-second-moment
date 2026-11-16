# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

Reading was complete for both the OLD (cdde711...) and NEW (7bea84b8...) modules.
All four assigned statements are textually unchanged apart from line shifts caused by
inserted explanatory scaffolding. The new prose is explanatory only; I found no
new mathematical assertion that fails under the stated hypotheses. The notes below
concern pre-existing compressions (fractional-power conversion, dual-norm
convention, loose constant-block slack), not rewrite regressions.

## L:signed-limiting-multiplier
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Pick an approximating sequence $L_{q_n}\to L$ in $\mathcal K(F)$. Applying
     both sides to the unit vector $(0,0,1,0)$ whose second $E$-entry is the
     constant displacement gives
     \[
       \|V_{q_n}-V_{q_j}\|_{H^{-1/2}}
       \le \|L_{q_n}-L_{q_j}\|_{\mathcal K(F)} ,
     \]
     because the $E$-norm of $(0,W,0,0)$ is exactly $\|W\|_{H^{-1/2}}$. Hence
     $V_{q_n}\to V$ in $H^{-1/2}$.
  2. Each $V_{q_n}=m_R(\Gamma*q_n)$ is supported in $\operatorname{supp} m_R$;
     testing against $\varphi\in C_c^\infty$ with support disjoint from
     $\operatorname{supp}m_R$ gives $\langle V_{q_n},\varphi\rangle=0$, and the
     limit preserves this, so $\operatorname{supp}V\subseteq\operatorname{supp}m_R$.
  3. The first, third and fourth columns of $L_{q_n}$ are identically zero; operator
     convergence preserves them. The displacement column $u\mapsto V_{q_n}u$ from
     $H^{1/2}$ into $H^{-1/2}$ has norm at most $\|L_{q_n}\|$; its limit has norm at
     most $k=\|L\|$.
  4. On compact smooth $u$, Lemma L:cutoff-factorization makes multiplication by
     the smooth compact $u$ bounded on $H^{-1/2}$, so $V_{q_n}u\to Vu$; since also
     $(L_{q_n}u)_2\to(Lu)_2$, we get $(Lu)_2=Vu$ for such $u$, and density of
     $C_c^\infty\subset H^{1/2}$ extends the multiplier to all of $H^{1/2}$.
  5. The linear c1-column gives $L(u,0,c_1,0)$ second entry $V_{q_n}(u+c_1)
     \to Vu+c_1V$; and applying $L$ to $(0,0,1,0)$ recovers $V$ itself, proving
     uniqueness of the limit from $L$.
  6. For $u,w\in C_c^\infty$ the operator pairing satisfies
     $\langle V_{q_n}u,w\rangle=\langle V_{q_n},uw\rangle$. Passing to the limit,
     $v_V(u,w):=\langle V_u,w\rangle=\langle V,uw\rangle$, symmetric in $u,w$. The
     norm bound $|\langle Vu,w\rangle|\le\|Vu\|_{H^{-1/2}}\|w\|_{H^{1/2}}
     \le k\|u\|_{H^{1/2}}\|w\|_{H^{1/2}}$ proves continuity, hence extends the
     symmetric form to all $u,w\in H^{1/2}$.
  7. Complexification: for $z=x+iy$, $\|L_{\mathbb C}z\|^2=\|Lx\|^2+\|Ly\|^2
     \le\|L\|^2(\|x\|^2+\|y\|^2)$, with equality on real vectors, so norms
     coincide. The real symmetric bilinear form $v_V$ extends sesquilinearly to a
     Hermitian form whose diagonal is $v_V(a,a)+v_V(b,b)$, the sum of the real and
     imaginary diagonal values (the cross terms cancel by symmetry).
- Argument preservation: PRESERVED
- New explanations: none identified — the proof text is identical (OLD LF 21–37,
  NEW LF 21–37).
- Evidence: norm recovery via the norm-one constant-displacement vector; support
  via testing outside the fixed compact mask; multiplier identification via
  bounded smooth-cutoff multiplication plus density; pairing bound
  $|v_V(u,w)|\le k\|u\|_{H^{1/2}}\|w\|_{H^{1/2}}$.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified
  within this read; the extension-by-density is compressed but correct, and it
  legitimately uses Lemma L:cutoff-factorization as a stated upstream input.

## P:signed-closed-form
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Let $b=\|u\|_2$, $z=\|u\|_{H^1}$. Fourier Cauchy–Schwarz:
     $\|u\|_{H^{1/2}}^2=\int\langle\xi\rangle|\widehat u|^2
     \le\big(\int|\widehat u|^2\big)^{1/2}
     \big(\int\langle\xi\rangle^2|\widehat u|^2\big)^{1/2}=bz$.
     Together with $k\le K$ and \eqref{E:signed-multiplier-form}:
     $|v_V(u,u)|\le k\|u\|_{H^{1/2}}^2\le Kbz$.
  2. Weighted AM–GM on $z^2,(Kb)^2$:
     $Kbz\le\tfrac12z^2+\tfrac12K^2b^2$.
  3. Since $q_V=z^2-b^2-v_V(u,u)$ and $c=2+K^2$,
     \[
       q_V+cb^2\ge\tfrac12z^2+(1+\tfrac{K^2}2)b^2,
     \]
     and
     \[
       q_V+cb^2\le\tfrac32z^2+(1+\tfrac{3K^2}2)b^2
       \le\tfrac{5+3K^2}{2}z^2\le 3(1+K^2)z^2=L_K z^2.
     \]
     The lower bound dominates both $\tfrac12z^2$ and $b^2$ (since
     $1+K^2/2\ge1$), so the shifted form norm is equivalent to the $H^1$ norm on
     the dense domain $H^1$; this gives semiboundedness and closedness
     (completeness in the shifted form norm). Teschl Theorem 2.14 gives the
     unique self-adjoint $H_V$, and Theorem 3.6/(3.51–3.53) gives
     \eqref{E:signed-form-domain}.
  4. The form lower bound gives $q_V+c\|\cdot\|^2\ge\|\cdot\|^2$, i.e. the form
     bound $A\ge1$; a bounded spectral slice below $1$ would produce a unit
     $D(A)$ test contradicting this form bound, so it is the spectral bound.
  5. Set $B_0=1-\Delta$; from the two bounds, as quadratic forms on the common
     $H^1$ domain, $q_{B_0}\le 2q_A$ and $q_A\le L_K q_{B_0}$.
  6. Resolvent variational identity (checked explicitly): for $T_0\ge1$ closed,
     \[
       \langle f,(T_0+t)^{-1}f\rangle
       =\sup_u\{2\operatorname{Re}\langle f,u\rangle-q_{T_0}(u)-t\|u\|^2\}.
     \]
     If $q_{T_0}\le q_{S_0}$ on the common domain then
     $(T_0+t)^{-1}\ge(S_0+t)^{-1}$, hence
     $I-t(T_0+t)^{-1}\le I-t(S_0+t)^{-1}$, i.e.
     $T_0(T_0+t)^{-1}\le S_0(S_0+t)^{-1}$.
  7. Scalar identity (verified by $t=xv^2$):
     $\sqrt x=\frac1\pi\int_0^\infty t^{-1/2}\frac{x}{x+t}\,dt$. Positive spectral
     integration (Tonelli over the PVM) gives
     $T_0^{1/2}\le S_0^{1/2}$ as forms with domain inclusions. Applying to
     $(B_0,2A)$ gives
     $\|B_0^{1/4}u\|_2\le 2^{1/4}\|A^{1/4}u\|_2$ with
     $D(A^{1/4})\subseteq D(B_0^{1/4})=H^{1/2}$; applying to $(A,L_KB_0)$ gives
     $\|A^{1/4}u\|_2\le L_K^{1/4}\|B_0^{1/4}u\|_2$ with
     $D(B_0^{1/4})\subseteq D(A^{1/4})$. Combined:
     $D(A^{1/4})=H^{1/2}$ and \eqref{E:signed-quarter-phase}.
  8. Dual completion: for $v\in L^2$ the norm of the functional
     $u\mapsto\langle v,u\rangle$ against $\|A^{1/4}u\|_2$ is
     $\|A^{-1/4}v\|_2$ (finite or infinite). Cauchy–Schwarz gives the upper bound;
     $u=A^{-1/2}v$ attains equality when $v\in D(A^{-1/4})$; spectral-cutoff
     tests show the norm is infinite otherwise. By the quarter equivalence this
     identifies the negative completion with $H^{-1/2}$.
  9. Uniqueness of form, resolvent and spectral calculus gives commutation with
     conjugation.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - OLD proof LF 65–115; NEW LF 65–131. The NEW proof adds only: (i) a purpose
    sentence; (ii) "Step 1. We make the shifted form coercive and closed.";
    (iii) "Step 2. ... The lower shifted bound controls both the H1 norm and the
    L2 norm, so completion in the shifted form norm keeps the prescribed form
    domain. The upper bound gives the reverse norm comparison. This is what
    permits application of the closed-form representation theorem rather than
    treating the rough potential as a bounded L2 multiplier."
  - The added "keeps the prescribed form domain" is correct: the shifted norm is
    equivalent to the complete $H^1$ norm, so the domain $H^1$ is already closed
    in the shifted form norm.
  - Computed exact constants: lower $1/2$, upper $L_K=3(1+K^2)$; quarter constants
    $2^{-1/4}$ and $L_K^{1/4}$.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: the conversion of
  the two half-power inequalities into the quarter-power domains/norms is implicit
  (it follows by reading $q_{T_0^{1/2}}(u)=\|T_0^{1/4}u\|^2$); the dual-norm
  statement "$v\in L^2$" uses the extended/possibly-infinite value of
  $\|A^{-1/4}v\|$. Both are pre-existing and reconstructable, not rewrite defects.

## L:signed-spectral-wave
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Bottom: for unit $u$, $z=\|u\|_{H^1}\ge1$ and
     $q_V(u)=z^2-1-v_V(u,u)\ge z^2-1-Kz\ge z^2/2-1-K^2/2\ge-\frac{1+K^2}{2}
     \ge-K^2$.
  2. Upper bottom bound: take a unit $C_c^\infty$ bump, dilate to shrink kinetic
     energy, and translate the whole support outside $\operatorname{supp} m_R$.
     Then $v_V(u,u)=0$ and $\|\nabla u\|^2\to0$, so $\beta\le0$. This uses only
     compact support of the fixed mask, never positivity of $V$.
  3. Form–spectral bottom equality: cited Teschl (3.52)–(3.53), plus the explicit
     argument that a spectral slice below the form infimum gives a contradiciting
     unit form test, while the form integral $\int h\,d\mu_u$ is bounded below by
     the spectral infimum. Since $\sigma(H_V)$ is closed inside $[\beta,\infty)$,
     $\beta=\inf\operatorname{spec}H_V\in\sigma(H_V)$.
  4. Spectral support/resolvent: total mass one gives a support point; normalized
     spectral projections on shrinking neighborhoods give approximate eigenvectors,
     so $\Sigma\subseteq\sigma(H_V)$. Conversely for real $z\notin\Sigma$ the
     Borel function $(h-z)^{-1}$ extended by zero off $\Sigma$ is bounded, and so
     is $h/(h-z)$; the calculus maps into $D(H_V)$ and gives a two-sided
     resolvent inverse, so $\sigma(H_V)\subseteq\Sigma$. Hence $\sigma(H_V)=\Sigma$,
     $\lambda=\sqrt{-\beta}\le K$, and every spectral value has $h+c\ge2$.
  5. Equivalent phase norm $\|(u,v)\|_{E_A}^2=\|A^{1/4}u\|_2^2+\|A^{-1/4}v\|_2^2$,
     with $M_K=L_K^{1/4}$ and equivalence
     $M_K^{-1}\|\cdot\|_E\le\|\cdot\|_{E_A}\le M_K\|\cdot\|_E$; the
     condition-number cost
     $M_K^2=\sqrt{3(1+K^2)}\le2(1+K)$, since
     $3(1+K^2)\le4(1+2K+K^2)$.
  6. In $E_A$ isometry the generator has matrix
     \eqref{E:signed-spectral-matrix}. Entry bounds:
     - $h>0$: $|C_t|\le1$; $|S_t|\le\min(t,h^{-1/2})$;
       $\sqrt{h+c}|S_t|\le1+\sqrt c\,t$ (case split $t\sqrt h\le1$ gives
       $t\sqrt{h+c}\le t\sqrt h+t\sqrt c\le1+\sqrt c\,t$; $t\sqrt h\ge1$ gives
       $\sqrt{1+c/h}\le\sqrt{1+ct^2}\le1+\sqrt c\,t$);
       $|hS_t|/\sqrt{h+c}\le\sqrt{h/(h+c)}\le1$.
     - $h=0$: matrix is $[[1,\sqrt c\,t],[0,1]]$.
     - $\beta\le h<0$: $|C_t|\le e^{\lambda t}$;
       $|S_t|\le te^{\lambda t}$ (since $\sinh x\le xe^x$);
       $\sqrt{h+c}|S_t|\le\sqrt c\,te^{\lambda t}$;
       $|hS_t|/\sqrt{h+c}=\sqrt{-h}\sinh(t\sqrt{-h})/\sqrt{h+c}\le Ke^{\lambda t}$
       because $\sqrt{-h}\le K$, $\sinh(t\sqrt{-h})\le e^{\lambda t}$ and
       $h+c\ge2$. No division by $\lambda$; the $h=0$ case is separate.
  7. Since $\sqrt c\le2K$, each entry is at most $2(1+K)(1+t)e^{\lambda t}$. The
     Hilbert–Schmidt (hence operator) norm of the $2\times2$ matrix is at most
     $2$ times this. Transferring from $E_A$ to $E$ multiplies by at most
     $M_K^2\le2(1+K)$, giving exactly
     $2\cdot2(1+K)\cdot2(1+K)(1+t)e^{\lambda t}=8(1+K)^2(1+t)e^{\lambda t}$.
  8. Strong continuity via spectral dominated convergence of the bounded entries on
     compact $t$-intervals; group property via scalar addition identities;
     extensions to graph levels $D(A^{1/2})\times L^2$ and $D(A)\times D(A^{1/2})$
     by the same bounded functions commuting with $A$ and spectral cutoffs.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - OLD proof LF 136–184; NEW LF 152–217. NEW adds: purpose sentence; Step 1/Step 2
    headers; and the closing paragraph "For negative spectral values, the lower
    off-diagonal estimate can be read without dividing by λ ... at most Ke^{λt}.
    Thus, the estimate also remains meaningful when the bottom rate is zero."
  - The added paragraph is correct: for $h<0$,
    $|-hS_t(h)/\sqrt{h+c}|=\sqrt{-h}\sinh(t\sqrt{-h})/\sqrt{h+c}
    \le K e^{\lambda t}/\sqrt{h+c}\le K e^{\lambda t}$, using $h+c\ge2$.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: the
  $\sqrt{h+c}|S_t|\le1+\sqrt c t$ bound is stated without its case split in both
  OLD and NEW; the reconstruction above supplies it. No new defect.

## P:signed-physical-wave
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Distributional equation: the Teschl form representation tested against
     $C_c^\infty$ functions gives $H_Vu=-\Delta u-Vu$ in distributions for
     $u\in D(H_V)$. Since $u\in H^1$ and $Vu\in H^{-1/2}$,
     $(1-\Delta)u=H_Vu+Vu+u\in H^{-1/2}$, so $u\in H^{3/2}$ by the Bessel
     isometry. Graph continuity: \eqref{E:signed-form-bounds} gives
     $\|u\|_{H^1}^2\le2\langle Au,u\rangle\le\|Au\|_2^2+\|u\|_2^2$, and
     $\|(1-\Delta)u\|_{H^{-1/2}}\le\|H_Vu\|_2+K\|u\|_{H^{1/2}}+\|u\|_{H^{1/2}}$
     bounds the $H^{3/2}$ norm by the graph norm.
  2. Free generator: $A_0(u,v)=(v,\Delta u)$ on $H^{3/2}\times H^{1/2}$; Fourier
     computation after frequency cutoff, no operator-norm derivative.
  3. Spectral data in $D(A)\times D(A^{1/2})=D(H_V)\times H^1$. Spectral cutoffs
     $1_{[1,n]}(A)$, graph-norm estimates and Teschl Theorem 3.2 give continuous
     graph trajectories with $u_t=v$, $v_t=-H_Vu$ in $H^1\times L^2$. Then
     $z_t=A_0z+L_Ez$ in $E$ with $L_E=L|_E$ (the identity
     $-H_Vu=\Delta u+Vu$ is exactly the distributional equation).
  4. Strong-group chain rule on $D(A_0)$:
     $S_E(-t)z(t)=z(0)+\int_0^tS_E(-s)L_Ez(s)\,ds$. Density (spectral cutoffs make
     $D(A)$ dense in $H^1$; $H^1$ is dense in $H^{1/2}$ and $H^{-1/2}$) plus
     finite-horizon boundedness extends the identity to $E$; Picard/Volterra
     uniqueness identifies the spectral wave with the bounded-perturbation
     physical wave. No $D(A^{3/4})=H^{3/2}$ is used.
  5. On $F$: bounded $L$ and strongly continuous $S_F$ define a unique Duhamel flow
     by the same Volterra/Picard argument (the $n$-th term
     $\le C_T^{n+1}\|L\|^nT^n/n!$). The interaction primitive
     $\int_0^tS_F(-s)LS_F(s)\,ds$ is norm-continuous because $L$ is compact and
     the group and its adjoint are strongly continuous; this is the compact-
     conjugation argument of P:cameron-actual-embedding. Hence the primitive is
     Lipschitz and the ordinary equation is the Young equation.
  6. Constant columns: for $(e,c_1,c_2)$ the constant block is
     $(c_1+tc_2,c_2)$ and the $E$ component is
     $P_V^E(t)e+\int_0^tP_V^E(t-s)(0,V(c_1+sc_2))\,ds$. Substituting the $E$
     Duhamel formula and interchanging the absolutely bounded finite-time triangle
     (as in \eqref{E:compact-F-block}) shows it solves the full system; uniqueness
     identifies it. $E$ is not dense in $F$; the constant columns are handled
     directly. The forcing norm is $\|V(c_1+sc_2)\|_{H^{-1/2}}\le K(1+s)|(c_1,c_2)|$.
  7. Polynomial cost: $\int_0^t(1+t-s)(1+s)\,ds=t+t^2+t^3/6\le(1+t)^3$. The full
     norm is at most
     \[
       (1+t)^3e^{\lambda t}\{8(1+K)^2\|e\|+[8K(1+K)^2+1]|(c_1,c_2)|\}.
     \]
     The constant block is bounded by $(1+t)|(c_1,c_2)|\le(1+t)^3|(c_1,c_2)|$,
     which is the $+1$ term.
  8. Coefficient bound (newly made explicit): $8(1+K)^2\le8(1+K)^3$; and
     $8K(1+K)^2+1\le8(1+K)^3+(1+K)^3=9(1+K)^3$, using $K\le1+K$ and
     $1\le(1+K)^3$. Cauchy–Schwarz on the two components gives
     $\sqrt{8^2+9^2}(1+K)^3<13(1+K)^3$. Hence the norm is at most
     $13(1+K)^3(1+t)^3e^{\lambda t}\|(e,c_1,c_2)\|_F\le16(1+K)^4(1+t)^3
     e^{\lambda t}\|(e,c_1,c_2)\|_F$, since $2\le1+K$.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - OLD proof LF 202–265; NEW LF 235–327. NEW adds: purpose sentence; Step 1–4
    headers; the sentence "The two domain requirements are different ... the
    ordinary Sobolev inclusion supplies the second."; and the coefficient-bounding
    sentences before the final Cauchy–Schwarz step.
  - The domain-requirement remark is correct: the free generator needs
    $u\in H^{3/2}$ and $v\in H^{1/2}$; the spectral graph data are
    $D(H_V)\times H^1$, with Step 1 supplying $D(H_V)\subset H^{3/2}$ and
    $H^1\subset H^{1/2}$.
  - The new coefficient arithmetic is exact as checked above.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: the final
  constant-block coefficient is a (valid but non-sharp) slack; the step
  "13(1+K)^3≤16(1+K)^4" is generous. The reliance on upstream
  \eqref{E:compact-F-block} and P:cameron-actual-embedding is explicit and remains
  within the stated application hypotheses. No new defect.

## AUDIT dispositions
- L:signed-limiting-multiplier: preserved; unchanged proof; reconstruction complete.
- P:signed-closed-form: preserved; additive scaffold only; reconstruction complete.
- L:signed-spectral-wave: preserved; additive scaffold and a correct threshold-note;
  reconstruction complete.
- P:signed-physical-wave: preserved; additive scaffold plus explicit coefficient
  arithmetic; reconstruction complete.

No assigned target conclusion or its counterpart was invoked to skip a target
derivation. The unassigned context modules (model assumptions, constant-phase
Young, compact Gaussian, Cameron mean, compact mean family) were used only through
their stated equations/lemmas under checked application hypotheses; their proofs
were not counted as reviewed proofs. Teschl imports are treated as stated inputs.

## Findings and limits
The new revision is a readability rewrite with step headings and two inserted
justifications. All new explanatory assertions recheck under the same signed
hypotheses: the shifted form stays closed on the prescribed $H^1$ domain, the
negative-branch lower off-diagonal bound needs no division by $\lambda$, the
graph-domain requirements for the free generator are met before density, and the
final coefficient arithmetic is exact.

Pre-existing (not rewrite-caused) notes: (i) the quarter-power conversion in
P:signed-closed-form is compacted and the dual-norm identity uses the possibly
infinite value of $\|A^{-1/4}v\|$; (ii) the entry bound
$\sqrt{h+c}|S_t(h)|\le1+\sqrt c\,t$ is asserted without its case split; (iii) the
constant block is bounded with non-sharp slack and the final constant $16$ is
generous. These are recoverable and do not falsify the stated bounds.

This review does not certify upstream analytic results, the Teschl citations, the
source PDFs/images, Lean correspondence, rendered pages, or any release. No
uniform growing-radius, source/noise limit, or new stochastic solution claim is
made by the module, and none was attributed to it.
