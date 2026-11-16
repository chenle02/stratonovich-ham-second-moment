# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

All five assigned proofs were read in both OLD and NEW revisions. The NEW revision of `notes/integrated_occupation_ceiling.tex` adds only roadmap sentences, two named `Step` headings, and two short explanatory sentences inside `T:intrinsic-occupation-ceiling`; all statements, definitions, equation labels and mathematical content are preserved. Every added explanatory assertion is justified under the hypotheses already loading the old proof. No AUDIT-worthy issue was found.

---

## L:occupation-raw-square
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. **Existence and continuity of $Q$.** For real $f\in H^1(\R^d)$ take $f_n\in C_c^\infty$, $f_n\to f$ in $H^1$. The upstream `P:spatial-four-linear` gives
     \[
     \|f_n^2-f_l^2\|_{H_{\mathrm{sp}}}^2
     =C_4(f_n-f_l,f_n+f_l,f_n-f_l,f_n+f_l)
     \le R_{\mathrm{sp}}N(f_n-f_l)^2N(f_n+f_l)^2\to0,
     \]
     with $N(f)=\|f\|_2^{1-\alpha/4}\|\nabla f\|_2^{\alpha/4}\le\|f\|_{H^1}$. Completeness of $H_{\mathrm{sp}}$ defines $Q(f)=\lim f_n^2$; interlacing two sequences bounds $\|Q^1(f)-Q^2(f)\|$ by the same difference bound, so independence holds. Passing pairings and the four-linear functional to the limit gives $\langle Q(f),Q(h)\rangle_{H_{\mathrm{sp}}}=B_\Gamma(f^2,h^2)$ and $\|Q(f)\|^2=A_{\mathrm{sp}}(f)$. The same difference bound gives continuity, since $N$ is $H^1$-continuous. This covers the first displayed identities verbatim in both revisions.

  2. **$L^2$ covariance-valued field.** For $g\in\mathcal{O}$, $F_g(s)=Q(g_s)$. Since $Q$ is continuous, strong $H^1$-measurability of $s\mapsto g_s$ gives strong measurability of $F_g$. For a.e. $s$, $\|g_s\|_2=1$, so from `P:spatial-four-linear`,
     \[
     \|F_g(s)\|^2=A_{\mathrm{sp}}(g_s)\le R_{\mathrm{sp}}b_s^{\alpha/2},\qquad
     b_s=\|\nabla g_s\|_2^2.
     \]
     Then
     \[
     \int_I\|F_g(s)\|^2\ud s
     \le R_{\mathrm{sp}}\int_I b_s^{\alpha/2}\ud s
     \le R_{\mathrm{sp}}T(g)^{\alpha/2}<\infty,
     \]
     where the last step is Jensen for the concave map $x\mapsto x^{\alpha/2}$, $0<\alpha/2<1$, on the unit interval. Hence $F_g\in L^2(I;H_{\mathrm{sp}})$.

  3. **Embedding and covariance norm.** `L:positive-raw-embedding` with $G=H_{\mathrm{sp}}$ gives $\rho_g=J_{H_{\mathrm{sp}}}F_g\in H_I$ and
     \[
     \|\rho_g\|_{H_I}^2=\int_{I^2}K(s,t)\langle Q(g_s),Q(g_t)\rangle_{H_{\mathrm{sp}}}
     =\int_{I^2}K(s,t)B_\Gamma(g_s^2,g_t^2)=A(g).
     \]
     Representative independence follows from the physical pairing on $(H^1)^2$ (`P:spatial-four-linear`, `L:spatial-physical-pair`); absolute integrability from the Schur row bound $K_0=2^a/(1-a)$.

  4. **Pairing with a smooth control.** Choosing compact smooth $\chi\equiv1$ on all spatial supports of $\Psi_t$,
     \[
     \langle\Psi_t,Q(f)\rangle_{H_{\mathrm{sp}}}
     =\lim_n B_\Gamma(\Psi_t,f_n^2)
     =C_4(\chi,\Psi_t,f,f)=B_\Gamma(\Psi_t,f^2).
     \]
     Polarizing `E:positive-bochner-inclusion` gives
     \[
     \langle\Psi,\rho_g\rangle=\int_{I^2}K(s,t)\langle\Psi_t,Q(g_s)\rangle_{H_{\mathrm{sp}}}\ud t\ud s.
     \]
     Absolute boundedness of the integrand by $\|\Psi_t\|\,\|Q(g_s)\|K$ makes Tonelli valid. Evenness of $\Gamma$ and symmetry of $K$, together with $h_{\Psi,s}(x)=\int_I K(s,t)(\Gamma*\Psi_t)(x)\ud t$, identify this with $\int_I\int_{\R^d}h_{\Psi,s}(x)g_s(x)^2\ud x\ud s$, i.e. `E:occupation-raw-identities`.

  5. **Final bound.** Hilbert Cauchy–Schwarz with $\|\rho_g\|^2=A(g)$ and $\|\Psi\|_{H_I}^2=v_\Psi$ gives $\langle\Psi,\rho_g\rangle\le\sqrt{v_\Psi A(g)}$.

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The NEW additions are only the roadmap (“norm bound makes a measurable occupation an $L^2$ covariance-valued field, so the temporal inclusion applies”) and two non-assertive step titles. The norm-bound claim is checkable: it is precisely the displayed $\int_I\|F_g(s)\|^2\le R_{\mathrm{sp}}T(g)^{\alpha/2}$ chain, which is present identically in both revisions and verified above. The phrase “original smooth control” matches $\Psi\in\mathcal{C}_{\mathrm{pos}}$, a smooth compact control.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none identified within this read. The strong-measurability claim is proved by composing continuous $Q$ with the strongly measurable field, as required by the class definition. No step or qualifier was dropped.

---

## P:raw-occupation-energy
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. **Positivity of kinetic energy.** A unit $H^1$ profile has $T(g)>0$: zero weak gradient forces constancy, and the only $L^2$ constant on $\R^d$ is zero. Hence $0<T(g)<\infty$.

  2. **Ratio bound.** From `P:spatial-four-linear`, for unit profiles
     \[
     B_\Gamma(g_s^2,g_t^2)\le\sqrt{A_{\mathrm{sp}}(g_s)A_{\mathrm{sp}}(g_t)}
     \le R_{\mathrm{sp}}b_s^{\alpha/4}b_t^{\alpha/4}.
     \]
     Thus
     \[
     A(g)\le R_{\mathrm{sp}}\int_{I^2}K(s,t)b_s^{\alpha/4}b_t^{\alpha/4}\ud s\ud t.
     \]
     With $u_s=b_s^{\alpha/4}$, Schur gives $\int_{I^2}K u_su_t\le K_0\int_I u_s^2\ud s$, and concavity gives $\int_I b_s^{\alpha/2}\le T(g)^{\alpha/2}$. Hence `E:raw-occupation-bound`:
     \[
     0\le A(g)\le K_0R_{\mathrm{sp}}T(g)^{\alpha/2}.
     \]
     Nonnegativity comes from the nonnegative kernels; positivity of $C_{\rm occ}$ from a time-constant compact smooth unit profile, whose $A=A_{\mathrm{sp}}(g)\int_{I^2}K>0$ (`P:spatial-four-linear` ensures $A_{\mathrm{sp}}(g)>0$).

  3. **Dilation identities.** $(U_\ell g)_s(x)=\ell^{d/2}g_s(\ell x)$ is an $H^1$ isomorphism with inverse $U_{1/\ell}$, preserves $\|g_s\|_2=1$, preserves strong measurability, and maps $\mathcal{O}$ bijectively onto itself. The two densities give $\ell^{2d}$, $\ud x$ gives $\ell^{-d}$, and the homogeneous Radon pushforward gives $\ell^{\alpha-d}$; total exponent $\alpha$. So
     \[
     A(U_\ell g)=\ell^\alpha A(g),\qquad T(U_\ell g)=\ell^2T(g).
     \]
     Approximation by compact smooth fields extends this to all of $H^1$.

  4. **Scalar skew-dilation optimization.** For fixed $A,T>0$, differentiate
     $f(\ell)=A\ell^\alpha-\zeta T\ell^2$:
     \[
     f'(\ell)=\ell^{\alpha-1}\big(\alpha A-2\zeta T\ell^{2-\alpha}\big).
     \]
     The unique interior maximum is $\ell_*=(\alpha A/(2\zeta T))^{1/(2-\alpha)}$, with $\zeta T\ell_*^2=(\alpha/2)A\ell_*^\alpha$, giving
     \[
     f(\ell_*)=\frac{2-\alpha}{2}A\ell_*^\alpha
     =D_\zeta\left(\frac{A}{T^{\alpha/2}}\right)^{2/(2-\alpha)},\qquad
     D_\zeta=\frac{2-\alpha}{2}\left(\frac{\alpha}{2\zeta}\right)^{\alpha/(2-\alpha)}.
     \]
     With $r(g)=A(g)/T(g)^{\alpha/2}$, dilation leaves $r$ invariant and rescales $T$ through all of $(0,\infty)$, so
     \[
     \sup_{g\in\mathcal{O}}\{A(g)-\zeta T(g)\}
     =\sup_{g\in\mathcal{O}}\sup_{\ell>0}\{A(U_\ell g)-\zeta T(U_\ell g)\}
     =D_\zeta C_{\rm occ}^{2/(2-\alpha)}.
     \]
     The case $A=0$ is handled by $\ell\downarrow0$, where the supremum is zero. No optimizer or minimax exchange is used; the right side follows because the bijective dilation leaves $\mathcal{O}$ invariant and ratios approach $C_{\rm occ}$, with positive-power continuity.

  5. **Inversion and scaling.** From `E:raw-occupation-energy`, solving for $C_{\rm occ}$:
     \[
     C_{\rm occ}=\left(\frac{2\mathcal{E}_\zeta^{\mathcal{O}}}{2-\alpha}\right)^{(2-\alpha)/2}
     \left(\frac{2\zeta}{\alpha}\right)^{\alpha/2},
     \]
     which is `E:raw-occupation-ratio`. Since $D_\zeta\propto\zeta^{-\alpha/(2-\alpha)}$,
     \[
     \mathcal{E}_\zeta^{\mathcal{O}}=\zeta^{-\alpha/(2-\alpha)}\mathcal{E}_1^{\mathcal{O}}.
     \]

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The NEW text adds only a roadmap and the two step titles (“positive finite occupation ratio”; “spatial dilation over the same occupation class”). Both are accurate summaries of steps present in the old proof. The two one-direction inequalities in the energy identity are obtained by “bounding every ratio by $C_{\rm occ}$” (upper) and “fixed ratios approaching its positive supremum” (lower); both sentences are preserved verbatim.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none identified within this read. Pre-existing implicit steps (Jensen/Schur for `E:raw-occupation-bound`, the Radon exponent accounting) are stated identically in both revisions.

---

## L:occupation-rayleigh-selection
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. **Countable dense normalized family.** $H^1(\R^d;\R)$ is separable via the isometric embedding $f\mapsto(f,\nabla f)\in L^2(\R^d)^{d+1}$; compact smooth density gives a countable dense family. After discarding zero and $L^2$-normalizing, get $f_j$ dense in the $L^2$-unit $H^1$ sphere; normalization preserves convergence because $\|p_n\|_2\to1$ forces $p_n/\|p_n\|_2\to f$.

  2. **Pointwise Rayleigh values.** With $b_j=\|\nabla f_j\|_2^2$,
     \[
     R_j(s)=\int h_{\Psi,s}f_j^2-b_j.
     \]
     Since $h_{\Psi,s}$ is bounded and $s\mapsto h_{\Psi,s}$ is Lipschitz (`L:variational-global-mean`), each $R_j$ is continuous, and `P:variational-unmasked-rate` plus density gives $\lambda_{\Psi,s}^2=\sup_jR_j(s)$.

  3. **First-index selection.** $U_j=\{s:R_j(s)>\lambda_{\Psi,s}^2-\varepsilon\}$, $A_1=U_1$, $A_j=U_j\setminus\bigcup_{i<j}U_i$. These are Borel, disjoint, and cover $I$ because $\lambda_{\Psi,s}^2=\sup_jR_j(s)$. Set $g_\varepsilon(s)=f_j$ on $A_j$. The finite truncations using $f_1$ elsewhere converge pointwise in $H^1$ to $g_\varepsilon$, giving strong measurability; a null set may be filled by $f_1$.

  4. **Kinetic bound.** With $H_\Psi=\sup_{s,x}h_{\Psi,s}(x)<\infty$, on $A_j$ the selection gives $R_j(s)>\lambda_{\Psi,s}^2-\varepsilon$, hence
     \[
     b(g_\varepsilon(s))=\|\nabla f_j\|_2^2
     <\int h_{\Psi,s}f_j^2-\lambda_{\Psi,s}^2+\varepsilon
     \le H_\Psi+\varepsilon.
     \]
     Thus $\int_I b(g_\varepsilon(s))\ud s\le H_\Psi+\varepsilon<\infty$ and $g_\varepsilon\in\mathcal{O}$.

  5. **Integration and Cauchy–Schwarz.** The near-Rayleigh inequality integrates over the disjoint cover to
     \[
     \langle\Psi,\rho_{g_\varepsilon}\rangle-T(g_\varepsilon)
     =\int_I\int h_{\Psi,s}g_\varepsilon(s)^2-\int_I b(g_\varepsilon(s))
     >\int_I\lambda_{\Psi,s}^2\ud s-\varepsilon,
     \]
     so $\int_I\lambda_{\Psi,s}^2+T(g_\varepsilon)\le\langle\Psi,\rho_{g_\varepsilon}\rangle+\varepsilon$, and `L:occupation-raw-square` bounds the latter by $\sqrt{v_\Psi A(g_\varepsilon)}+\varepsilon$. Time Cauchy–Schwarz on the unit interval gives $I_\Psi^2\le\int_I\lambda_{\Psi,s}^2\ud s$, proving `E:occupation-rayleigh-selection`.

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The NEW text adds only a roadmap and two step titles; the mathematical body is copied verbatim from the OLD proof, including the strict inequality $R_j(s)>\lambda^2-\varepsilon$, the $H_\Psi+\varepsilon$ bound, and the statement that no eigenvector/selector/limiting occupation is used.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none identified within this read. The strict inequality becomes a non-strict one after integrating; this is benign and present identically in both revisions.

---

## T:intrinsic-occupation-ceiling
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. **Kinetic optimization before error removal.** Fix $\Psi$, $v=v_\Psi$, $C=C_{\rm occ}$, $\beta=\alpha/4$. `L:occupation-rayleigh-selection` gives $g_\varepsilon\in\mathcal{O}$ with
     \[
     I_\Psi^2\le\sqrt{vA(g_\varepsilon)}-T(g_\varepsilon)+\varepsilon,\qquad T(g_\varepsilon)>0.
     \]
     By definition of $C_{\rm occ}$, $A(g_\varepsilon)\le C T(g_\varepsilon)^{\alpha/2}$, hence $\sqrt{vA(g_\varepsilon)}\le\sqrt{vC}\,T^\beta$. So
     \[
     I_\Psi^2\le\sqrt{vC}\,T^\beta-T+\varepsilon
     \le\sup_{T\ge0}\big(\sqrt{vC}\,T^\beta-T\big)+\varepsilon,
     \]
     then let $\varepsilon\downarrow0$.

  2. **Supremum computation.** For $v>0$, $f(T)=\sqrt{vC}\,T^\beta-T$ has derivative $\beta\sqrt{vC}\,T^{\beta-1}-1$, strictly decreasing from $+\infty$ to $-1$. Its zero is
     \[
     T_*=(\beta\sqrt{vC})^{1/(1-\beta)},\qquad 1-\beta=q/4,
     \]
     and the derivative-zero relation $T_*=\beta\sqrt{vC}\,T_*^\beta$ gives the value
     \[
     f(T_*)=(1-\beta)(vC)^{1/2}T_*^\beta
     =\frac q4\left(\frac\alpha4\right)^{\alpha/q}(vC)^{2/q}.
     \]
     For $v=0$ the supremum over $T\ge0$ is $0$. Hence in both cases
     \[
     I_\Psi\le Dv^{1/q},\qquad
     D=\sqrt{q/4}\,(\alpha/4)^{\alpha/(2q)}C^{1/q}.
     \]

  3. **Variance optimization.** The expression $S_\mathfrak{c}^{\mathrm{pos}}\le\sup_\Psi(\mathfrak cI_\Psi-v/2)$ gives, pointwise in $v\ge0$,
     \[
     \mathfrak cI_\Psi-\frac v2\le\mathfrak cDv^{1/q}-\frac v2.
     \]
     The function $g(v)=\mathfrak cDv^{1/q}-v/2$ vanishes at $0$, tends to $-\infty$, and has strictly decreasing derivative $\mathfrak cDq^{-1}v^{-k/q}-1/2$. The unique positive maximum is
     \[
     v_*=(2\mathfrak cD/q)^{q/k},\qquad
     g(v_*)=\frac{k v_*}2.
     \]

  4. **Constant matching.** Direct algebra:
     \[
     (2D/q)^q=2^q q^{-q}\cdot(q/4)^{q/2}(\alpha/4)^{\alpha/2}C
     =q^{-q/2}(\alpha/4)^{\alpha/2}C.
     \]
     Then
     \[
     g(v_*)=\frac k2\mathfrak c^m(2D/q)^{q/k}
     =\mathfrak c^m k\,q^{-q/(2k)}(\alpha/4)^{\alpha/(2k)}C^{1/k}.
     \]
     Writing $(\alpha/4)^{\alpha/(2k)}=\alpha^{\alpha/(2k)}4^{-\alpha/(2k)}=\alpha^{\alpha/(2k)}2^{-\alpha/k}$, the prefactor is
     \[
     \frac 12 2^{-\alpha/k}2^{-1}=2^{-(1+\alpha/k)}=2^{-(k+\alpha)/k}=2^{-3/k}=8^{-1/k},
     \]
     using $k+\alpha=3$. Hence
     \[
     g(v_*)=\mathfrak c^mk\left[\frac{\alpha^{\alpha/2}C}{8q^{q/2}}\right]^{1/k}=U_\mathfrak c .
     \]

  5. **Energy form.** Iterating `E:raw-occupation-ratio`,
     \[
     \alpha^{\alpha/2}C_{\rm occ}
     =(2\zeta)^{\alpha/2}\left(\frac{2\mathcal{E}_\zeta^{\mathcal{O}}}{2-\alpha}\right)^{(2-\alpha)/2},
     \]
     so
     \[
     U_\mathfrak c=\mathfrak c^m(2\zeta)^{\alpha/(2k)}F_0(\mathcal{E}_\zeta^{\mathcal{O}}).
     \]

  6. **Conclusion.** Taking the supremum over $\Psi\in\mathcal{C}_{\mathrm{pos}}$ gives $S_\mathfrak c^{\mathrm{pos}}\le U_\mathfrak c$. The upstream `T:intrinsic-second-moment` identifies $C_2=S_2^{\mathrm{pos}}$, so $C_2\le U_2$. The $\zeta$-independence is consistent: $F_0(z)\propto z^{(2-\alpha)/(2k)}$ and $\mathcal E_\zeta\propto\zeta^{-\alpha/(2-\alpha)}$ cancel the factor $(2\zeta)^{\alpha/(2k)}$, leaving the first, $\zeta$-free form.

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The two NEW sentences are exact partial algebra. (i) “$T_*=\beta\sqrt{vC}\,T_*^\beta$, so the value is $(1-\beta)\sqrt{vC}\,T_*^\beta$” follows from the displayed derivative zero and substitution established above. (ii) “$4^{-\alpha/2}=2^{-\alpha}$ ... contributes $2^{-k}$ ... product $2^{-3}$ because $k+\alpha=3$” is exactly the denominator-eight computation in step 4. There is no change to the order “kinetic sup first, then $\varepsilon\downarrow0$”, and the second form retains $(2\zeta)^{\alpha/(2k)}$.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none identified within this read. The ceiling is explicitly stated, in both revisions, not to be attained or equal to $C_2$; that qualifier is retained.

---

## C:intrinsic-spatial-bracket
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:

  1. **Upper bracket.** From `T:intrinsic-occupation-ceiling` with $\mathfrak c=2$,
     \[
     C_2\le U_2=2^mk\left[\frac{\alpha^{\alpha/2}C_{\rm occ}}{8q^{q/2}}\right]^{1/k}.
     \]
     Inserting `P:raw-occupation-energy` ($C_{\rm occ}\le K_0R_{\mathrm{sp}}$) yields the upper bound. `E:spatial-energy-map` gives
     \[
     \left(\frac{2\mathcal{E}_{\mathrm{sp}}}{2-\alpha}\right)^{(2-\alpha)/2}
     =\alpha^{\alpha/2}R_{\mathrm{sp}},
     \]
     hence
     \[
     k\left[\frac{\alpha^{\alpha/2}K_0R_{\mathrm{sp}}}{8q^{q/2}}\right]^{1/k}
     =K_0^{1/k}F_0(\mathcal{E}_{\mathrm{sp}}).
     \]
     So $C_2\le 2^mK_0^{1/k}F_0(\mathcal{E}_{\mathrm{sp}})$.

  2. **Lower bracket.** `E:spatial-static-energy-score` gives
     \[
     S_1^{\mathrm{pos}}\ge M_a^{-1/k}F_0(\mathcal{E}_{\mathrm{sp}}).
     \]
     Using $S_2^{\mathrm{pos}}=2^mS_1^{\mathrm{pos}}$ (`P:variational-positive-scores`) and $C_2=S_2^{\mathrm{pos}}$ (`T:intrinsic-second-moment`) gives
     \[
     2^mM_a^{-1/k}F_0(\mathcal{E}_{\mathrm{sp}})\le C_2.
     \]

  3. **Scalar map comparison.** With
     \[
     \Delta=\tfrac12[q\log q+(q-2a)\log(q-2a)]-(q-a)\log(q-a),
     \]
     strict midpoint convexity of $x\log x$ (second derivative $1/x>0$) applied to $x=q$ and $y=q-2a>0$ gives $\Delta>0$; $q-2a>2-a>1$ holds under $a>0$ and $\alpha+a<2$. From `E:occupation-scalar-map`,
     \[
     \frac{F_a(z)}{F_0(z)}
     =\left[\frac{q^{q/2}(q-2a)^{(q-2a)/2}}{(q-a)^{q-a}}\right]^{1/k},
     \]
     so
     \[
     \log\frac{F_a(z)}{F_0(z)}=\frac\Delta k.
     \]
     Together with `E:occupation-score-ceiling`,
     \[
     \log\frac{\mathfrak c^mF_a(\mathcal E_\zeta^{\mathcal O})}{U_\mathfrak c}
     =\frac{\Delta-(\alpha/2)\log(2\zeta)}{k}.
     \]

  4. **Comparison at $\zeta=1/2$.** Then $\log(2\zeta)=0$, so
     $\mathfrak c^mF_a(\mathcal E_{1/2}^{\mathcal O})>U_\mathfrak c$. With $\mathfrak c=2$ and $C_2\le U_2$ this gives
     \[
     C_2\le2^mF_0(\mathcal E_{1/2}^{\mathcal O})
     <2^mF_a(\mathcal E_{1/2}^{\mathcal O}).
     \]

  5. **Non-favorability at $\zeta=1$.** For $\alpha=5/4$, $a=1/2$,
     $q=11/4$, $q-2a=7/4$, $q-a=9/4$, the exponent is
     \[
     8[\Delta-(\alpha/2)\log2]
     =11\log(11/4)+7\log(7/4)-18\log(9/4)-5\log2
     =\log\frac{11^{11}7^7}{2^5 9^{18}}<0,
     \]
     numerically $234966429149994773/4803028329503971872<1$. Hence at $\zeta=1$ the comparison value $\mathfrak c^mF_a(\mathcal E_1^{\mathcal O})$ lies below $U_\mathfrak c$, and no strict comparison is produced; the text correctly says this refutes no moment inequality.

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: The NEW text adds only the roadmap (“combine the spatial ratio estimate with the occupation ceiling ... compare the scalar maps by strict convexity, keeping the kinetic penalty normalization explicit”). It is a faithful summary; the body is verbatim identical to OLD.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns: none identified within this read. The restriction $\Gamma\ne0$ on the energy comparison and the explicit “no-go” contextualization after the proof are retained. Both revisions keep the `M_a` normalization, the $(2\zeta)$ factor, and the strictness scope of the midpoint-convexity comparison.

---

## AUDIT dispositions
No AUDIT comments are present in the NEW module, and no AUDIT-worthy issue was found. The additions are explanatory only and are mathematically sound under the existing hypotheses and quantifiers. In particular:
- `L:occupation-raw-square`: roadmap claim about $L^2$ covariance-valued field is verified by the displayed norm-bound chain.
- `T:intrinsic-occupation-ceiling`: both inserted sentences are correct partial algebra (critical-point relation and the $2^{-3}$ denominator), reproducing the old “denominator eight” exactly.
- `C:intrinsic-spatial-bracket`: the roadmap is descriptive and changes no argument.

Disposition: no items.

## Findings and limits
All five assigned proof pairs were reconstructed with public working; the OLD and NEW statements and definitions (`E:raw-occupation-definitions`, the five environments, and the scalar map `E:occupation-scalar-map`) are unchanged within their listed line ranges. Argument preservation is PRESERVED in all five; New explanations are JUSTIFIED in all five. I certify reading/argument-preservation equivalence of the rewrite, not the truth of the upstream primary-source arguments: the reconstruction uses the named UNASSIGNED inputs `P:spatial-four-linear`, `L:positive-raw-embedding`, `P:variational-unmasked-rate`, `P:variational-positive-scores`, `E:spatial-energy-map`, and `T:intrinsic-second-moment` only after checking their stated hypotheses match the consumers (real $H^1$ profiles, unit-profile occupation class $\mathcal{O}$, bounded potential with $H_\Psi<\infty$, positivity of $T$ for unit profiles, $\Gamma\ne0$ where positivity is claimed, and $C_2=S_2^{\mathrm{pos}}$). Under the unitary-Fourier context, no raw normalization was silently introduced; the `M_a`, $K_0$, $(2\zeta)$ factors, and denominator eight were all recomputed and agree. The computed occupation quantity is used and presented as a ceiling, not an attained value or equality with $C_2$, consistent with the theorem’s explicit disclaimer in both revisions.
