# Review Result

Category: proof-readability-equivalence  
Model: deepseek-v4-pro  
Verdict: PASS  
Confidence: high

I read both OLD and NEW supplied scientific views in full, including the unchanged
statements and proofs, and independently reconstructed every assigned deduction
below. The view-to-view comparison shows that only No-goes 14 and 15 gained
explanatory prose (a two-sentence roadmap plus `Step 1/Step 2` structure);
No-goes 16, 20, 31 have identical proof text, with line offsets caused solely by
the upstream insertions. All mathematical content—statements, hypotheses,
domains, constants, strictness, limiting order, and obstruction scopes—is
preserved. I did not verify byte equality against the pinned originals directly
(only the supplied rendered payload is available), but the two rendered views
match in every displayed formula and sentence.

Baseline context is used only under checked hypotheses: `E:threshold`
($\alpha_0+\alpha<2$) is invoked in No-go 20 with $\alpha=d=1$ (white spatial
covariance) and time exponent $a$, giving $1+a<2$ since $a<1$.

---

## P:nogo-14

**Old reading:** COMPLETE  
**New reading:** COMPLETE  
**Argument preservation:** PRESERVED  
**New explanations:** JUSTIFIED

The statement (OLD LF 22–34; NEW LF 22–34) is unchanged. The NEW proof
(LF 35–91, versus OLD 35–79) adds a two-sentence roadmap (“We compute the full
two-block phase product rather than resetting the velocity. We then control the
Gaussian series remainders…”) and splits the argument into `Step 1` (formal
variance coefficients) and `Step 2` (remainder control and strict comparison).
This is accurate descriptive organization; it changes no formula, hypothesis, or
deduction.

**Public reconstruction:** COMPLETE

*Original-step coverage:*

1. **Entire functions and propagator.** With
   $c(z)=\sum_{n\ge0} z^n/(2n)!$, $s(z)=\sum_{n\ge0} z^n/(2n+1)!$, one
   reads $c(z)=\cosh(\sqrt z)$, $s(z)=\sinh(\sqrt z)/\sqrt z$. The unit-time
   phase propagator is the matrix
   $M(z)=\begin{pmatrix}c(z)&s(z)\\ zs(z)&c(z)\end{pmatrix}$: rows arise from
   $y''=zy$ with phase $(1,0)$, giving displacement $c$ and velocity $zs$, and
   phase $(0,1)$, giving displacement $s$ and velocity $c$. Hence
   $y(2)=c(Z_2)c(Z_1)+s(Z_2)Z_1 s(Z_1)$, the composition restoring the velocity
   continuity at time one. Verified.

2. **Degree-two expansion.** Using
   $c(w)c(z)=1+\tfrac12(z+w)+\frac1{24}(z^2+w^2)+\frac14 zw$ and
   $s(w)zs(z)=z+\frac16 z w+\frac16 z^2$, one obtains
   \[
   c(w)c(z)+s(w)zs(z)
   =1+\frac32 z+\frac12 w+\frac5{24}z^2+\frac5{12}zw+\frac1{24}w^2+O(3).
   \]
   The coefficients are checked: constant $1$; linear $z/2+z=3z/2$, $w/2$;
   quadratic $z^2$: $1/24+1/6=5/24$; $zw$: $1/4+1/6=5/12$; $w^2$: $1/24$.

3. **Squaring.** For
   $F=1+\frac32z+\frac12w+\frac5{24}z^2+\frac5{12}zw+\frac1{24}w^2+\cdots$,
   the coefficient of $z^2$ in $F^2$ is
   $2(5/24)+(3/2)^2=5/12+9/4=8/3$, and of $w^2$ is
   $2(1/24)+(1/2)^2=1/12+1/4=1/3$. Independence and centering make
   $\E zw=0$, eliminating the only degree-$(1,1)$ term.

4. **One-block moment.** $y(1)=c(Z_1)$, so the $z^2$ coefficient of $c(z)^2$ is
   $2(1/24)+(1/2)^2=1/3$. With $\E Z_1^2=A$,
   $\E y(1)^2=1+A/3+O(A^2)$. The two-block moment has variance contributions
   $(8/3)A+(1/3)A=3A$; thus $\E y(2)^2=1+3A+O(A^2)$.

5. **Comparison.** $(\E y(1)^2)^2=1+2A/3+O(A^2)$, so the difference is
   $(1+3A)-(1+2A/3)+O(A^2)=7A/3+O(A^2)>0$ for small $A>0$. This is the stated
   strict mismatch.

6. **Remainder justification (Step 2).** Using the closed forms,
   $|c(z)|=|\cosh\sqrt z|\le e^{\sqrt{|z|}}$ and
   $|s(z)|=|\sinh(\sqrt z)/\sqrt z|\le e^{\sqrt{|z|}}$, so
   $|c(z)|+|s(z)|\le2e^{\sqrt{|z|}}$. The two-block displacement is
   $F=c(w)c(z)+s(w)zs(z)$, so $|F|^2$ is controlled by
   $C(1+|z|)^2e^{2\sqrt{|z|}+2\sqrt{|w|}}$, Gaussian-integrable at fixed
   $A_1>0$. Absolute integrability licenses termwise expectation; odd powers
   vanish; remaining terms have even total degree and nonnegative coefficients
   (products of nonnegative-coefficient series), so $\sum_{j\ge0}b_jA^j$ with
   $b_j\ge0$. For $0\le A\le A_1$,
   $\sum_{j\ge2}b_jA^j\le(A/A_1)^2\sum_{j\ge2}b_jA_1^j=O(A^2)$. The one-block
   moment is handled identically. This is a rigorous small-variance
   counterexample, turning the “formal coefficients” into an actual result.

All steps survive verbatim; the new Step headings only relabel them. No lost
qualifier; no new obstruction introduced.

---

## P:nogo-15

**Old reading:** COMPLETE  
**New reading:** COMPLETE  
**Argument preservation:** PRESERVED  
**New explanations:** JUSTIFIED

Statement OLD LF 97–113, NEW LF 109–125: unchanged. NEW proof (LF 126–163 vs
114–140) adds a roadmap and `Step 1/Step 2` headings; the mathematics is
identical.

**Public reconstruction:** COMPLETE

*Original-step coverage:*

1. **Taylor coefficients of $M(z)$.** From $c(z)=1+z/2+z^2/24+\cdots$,
   $s(z)=1+z/6+z^2/120+\cdots$, $zs(z)=z+z^2/6+\cdots$,
   \[
   M_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
   M_1=\begin{pmatrix}1/2&1/6\\1&1/2\end{pmatrix},\quad
   M_2=\begin{pmatrix}1/24&1/120\\1/6&1/24\end{pmatrix}.
   \]

2. **Coefficient of variance.** With $Z$ standard Gaussian and
   $M(\sigma Z)=M_0+\sigma Z M_1+\sigma^2 Z^2 M_2+\cdots$,
   $\|Mx\|^2=x^{\mathsf T}M^{\mathsf T}Mx$. First-order cross terms have factor
   $\E Z=0$; second-order terms give $\E Z^2=1$, hence
   $K=M_1^{\mathsf T}M_1+M_0^{\mathsf T}M_2+M_2^{\mathsf T}M_0$. This retains
   the second-order mean (Duhamel) term, which is the point of the no-go.

3. **Matrix arithmetic.**
   \[
   M_1^{\mathsf T}M_1
   =\begin{pmatrix}1/2&1\\1/6&1/2\end{pmatrix}
    \begin{pmatrix}1/2&1/6\\1&1/2\end{pmatrix}
   =\begin{pmatrix}5/4&7/12\\7/12&5/18\end{pmatrix},
   \]
   \[
   M_0^{\mathsf T}M_2+M_2^{\mathsf T}M_0
   =\begin{pmatrix}1/12&13/60\\13/60&1/10\end{pmatrix}.
   \]
   Summation gives
   $K=\begin{pmatrix}5/4+1/12&7/12+13/60\\7/12+13/60&5/18+1/10\end{pmatrix}
   =\begin{pmatrix}4/3&4/5\\4/5&17/45\end{pmatrix}$.

4. **Signed quadratic form.** For $x=(1,-2)$,
   \[
   x^{\mathsf T}Kx=\frac43-4\cdot\frac45+4\cdot\frac{17}{45}
   =\frac{60-144+68}{45}=-\frac{16}{45}.
   \]
   Correct.

5. **Underestimation claim.** For $e_1=(1,0)$, the first random contribution is
   $\|M_1e_1\|^2=\|(1/2,1)\|^2=1/4+1=5/4$, while
   $e_1^{\mathsf T}Ke_1=4/3$. Since $4/3>5/4$, dropping the second-order mean
   term underestimates the coefficient in this direction. The negative value
   for $x=(1,-2)$ shows the full coefficient matrix need not be positive
   semidefinite (it is not required to be a covariance matrix).

6. **Remainder (Step 2).** The entries obey
   $|c(z)|+|s(z)|+|zs(z)|\le C(1+|z|)e^{\sqrt{|z|}}$ (the polynomial factor
   is exactly `zs(z)`), so $\|M(\sigma Z)\|^2$ is Gaussian-integrable. The
   series is even in $\sigma$; the degree-$\ge4$ tail at an anchor $\sigma_1$
   is $O(\sigma^4)$ for $|\sigma|\le|\sigma_1|$. For $x=(1,-2)$,
   $M(0)x=(1\cdot1+1\cdot(-2),\,0+1\cdot(-2))=(-1,-2)$ with norm $5$, so
   \[
   \E\|M(\sigma Z)x\|^2=5-\frac{16}{45}\sigma^2+O(\sigma^4).
   \]
   This exhibits an actual phase whose expected energy decreases at second
   order.

No mathematical change; the new text accurately describes keeping “the
complete first variance matrix” and uses the remainder to prove an actual
decreasing-energy phase.

---

## P:nogo-16

**Old reading:** COMPLETE  
**New reading:** COMPLETE  
**Argument preservation:** PRESERVED  
**New explanations:** no new explanatory prose detected; proof LF length
identical (20 lines: OLD 174–193, NEW 197–216).

**Public reconstruction:** COMPLETE

*Original-step coverage:*

1. **Scaling of the score.** Substitute $H=c^{1/(2-r)}K$ in
   $J_c=\sup_{H\ge0}\{cAH^r-H^2/2\}$. Then
   $H^r=c^{r/(2-r)}K^r$, $H^2/2=c^{2/(2-r)}K^2/2$, and
   $cAH^r=A c^{1+r/(2-r)}K^r=A c^{2/(2-r)}K^r$, since
   $1+\frac r{2-r}=\frac2{2-r}$. Hence $J_c=c^{2/(2-r)}J_1$.

2. **Finiteness and positivity of $J_1$.** For $r<2$ the positive term is
   subquadratic, so the supremum is finite; for small $H>0$,
   $AH^r-H^2/2>0$, so $J_1>0$.

3. **Strict surrogate comparison.** The surrogate objective
   $\sup_{H\ge0}\{2AH^r-H^2\}=2\sup_{H\ge0}\{AH^r-H^2/2\}=2J_1$ (factor two
   in the objective). By contrast $J_2=2^{2/(2-r)}J_1$, and $2/(2-r)>1$ because
   $r>0$, so $2J_1<J_2$. This is the claimed loss.

4. **Gaussian tilted mean.** For $Q_h$ with density
   $L_h=e^{hZ-h^2/2}$, $\E L_h^2=e^{-h^2}\E e^{2hZ}=e^{h^2}$. Cauchy–Schwarz
   gives $\E Y^2\ge(\E_{Q_h}Y)^2e^{-h^2}$. Under $Q_h$, $Z$ has mean $h$ and
   variance $1$, so $\E_{Q_h}Y=\E_{Q_h}e^{\sigma Z}=e^{\sigma^2/2+\sigma h}$.
   Squaring gives exponent $\sigma^2+2\sigma h-h^2$, maximized at $h=\sigma$
   with value $2\sigma^2$; hence the bound recovers
   $e^{2\sigma^2}=\E Y^2$ exactly.

5. **Deterministic surrogate loss.** Replacing the tilted mean by the
   deterministic value $Y(h)=e^{\sigma h}$ gives exponent $2\sigma h-h^2$,
   maximized at $h=\sigma$ with value $\sigma^2$; the resulting bound
   $e^{\sigma^2}$ misses a logarithmic factor $\sigma^2$ relative to the exact
   annealed $\E Y^2=e^{2\sigma^2}$.

The statement and proof remain a scalar score calculation identifying the lost
annealed factor, and explicitly avoid claiming an obstruction to Gaussian
shifts. Preserved.

---

## P:nogo-20

**Old reading:** COMPLETE  
**New reading:** COMPLETE  
**Argument preservation:** PRESERVED  
**New explanations:** none beyond LF offset (24 lines each: OLD 221–244,
NEW 244–267).

**Public reconstruction:** COMPLETE

*Original-step coverage:*

1. **Construction.** $f_2(u)=f_1(1-u)$, $\psi=f_1q_1+f_2q_2$ with disjoint
   spatial bumps $q_1\subset(-2,-1)$, $q_2\subset(1,2)$ and $f_1$ supported in
   $(1/8,1/4)$. The test $\psi$ is nonnegative, smooth, compactly supported.

2. **Constants.** $A=\int_0^1u^{-a}f_1(u)\,\mathrm du$,
   $B=\int_0^1(1-u)^{-a}f_1(u)\,\mathrm du$. On the support of $f_1$,
   $u<1-u$ and, for $a>0$, $u^{-a}>(1-u)^{-a}$, so $A>B>0$ (both positive since
   $f_1\ge0$ nonzero).

3. **End profiles.** $h_\sigma=c_\Gamma\big(q_1\int|\sigma-u|^{-a}f_1(u)\,\mathrm du
   +q_2\int|\sigma-u|^{-a}f_1(1-u)\,\mathrm du\big)$. At $\sigma=0$ the second
   integral is $\int u^{-a}f_1(1-u)\,\mathrm du=\int(1-v)^{-a}f_1(v)\,\mathrm dv=B$
   (substituting $v=1-u$), giving $h_0=c_\Gamma(Aq_1+Bq_2)$. At $\sigma=1$ the
   first integral becomes $B$ and the second $A$, giving
   $h_1=c_\Gamma(Bq_1+Aq_2)$. Both verified.

4. **Determinant test.** Choose $x_1,x_2$ with $q_i(x_i)>0$; disjoint supports
   give $q_1(x_2)=q_2(x_1)=0$. Then
   \[
   h_0(x_1)h_1(x_2)-h_1(x_1)h_0(x_2)
   =c_\Gamma^2(A^2-B^2)q_1(x_1)q_2(x_2)>0.
   \]
   Any representation $h_\sigma=b(\sigma)U(x)$ makes the two vectors
   $(h_0(x_1),h_0(x_2))$ and $(h_1(x_1),h_1(x_2))$ both lie in the span of
   $(U(x_1),U(x_2))$ (with coefficients $b(0),b(1)$), so the same determinant
   would be zero. Contradiction establishes the nonseparable full control class.

5. **Parameter condition.** The spatial white covariance $\Gamma=\delta_0$ has
   $\alpha=d=1$ in the baseline hypothesis, and the displayed time kernel has
   exponent $a$; the stated condition $1+a<2$ is exactly
   $\alpha_0+\alpha<2$ with $\alpha_0=a$, guaranteed by $a<1$. Verified against
   the baseline `E:threshold`.

The side remarks after the proof (weaker common lower profile
$h_\sigma\ge\Gamma*\int\psi\,\mathrm du$) also appear unchanged in both views.
Preserved.

---

## P:nogo-31

**Old reading:** COMPLETE  
**New reading:** COMPLETE  
**Argument preservation:** PRESERVED  
**New explanations:** none beyond LF offset (22 lines each: OLD 272–293,
NEW 295–316).

**Public reconstruction:** COMPLETE

*Original-step coverage:*

1. **Non-lower growth for every phase.** For
   $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, the eigenvectors
   $(1,1)^{\mathsf T}$ and $(1,-1)^{\mathsf T}$ have eigenvalues $1$ and $-1$.
   Thus $e^{tB}(1,1)^{\mathsf T}=e^{t}(1,1)^{\mathsf T}$ and
   $e^{tB}(1,-1)^{\mathsf T}=e^{-t}(1,-1)^{\mathsf T}$. Since $B$ is symmetric,
   $\|e^{tB}\|=e^{t}$ for $t\ge0$. So the propagator norm grows at rate $1$,
   while the specific nonzero vector $(1,-1)$ decays. This distinguishes global
   growth from every-phase lower growth without raising the initial
   phase-vector to arbitrary phase-space data.

2. **Masks and velocities.** Zero initial displacement, nonnegative smooth
   velocity $v$ supported in $(5,6)$, $\int v=1$. Masks: $\chi_s=1$ on
   $[-2,2]$, support in $[-4,4]$; $\chi_l=1$ on $[-14,14]$. Both equal $1$ on
   $[-2,2]$ (the observation interval), so they agree there. Since
   ${\operatorname{supp}} v\subset(5,6)\subset[-14,14]$ and
   $(5,6)\cap[-4,4]=\emptyset$, $\chi_l v=v$ and $\chi_s v=0$.

3. **D'Alembert at time nine.** With initial displacement zero,
   $u(9,x)=\frac12\int_{x-9}^{x+9}v(y)\,\mathrm dy$ for the masked velocity.
   For $x\in[-2,2]$, $[x-9,x+9]$ ranges from $[-11,7]$ (at $x=-2$) to
   $[-7,11]$ (at $x=2$), both containing $(5,6)$. Hence
   $u_l(9,x)=\frac12\cdot1=1/2$ and $u_s(9,x)=0$ for all $x\in[-2,2]$:
   different free displacements throughout the observation interval, despite
   equal initial displacements everywhere (both zero) and agreement of the
   masks on the observer.

4. **Scope.** The first example does not refute a terminal lower bound for the
   specified phase $(1,0)$; the second requires agreement of displacement and
   velocity on the full backward cone, not merely on the observer. Both
   statements and the post-proof guidance survive unchanged.

---

## Findings and limits

**Findings.**
- All five assigned statements are view-identical; all five proofs preserve
  their logical deductions, hypotheses, normalizations, constants, strictness,
  order of small-coupling limits, and obstruction scopes.
- The only changes are explanatory: in No-goes 14 and 15 the NEW proof adds a
  two-sentence roadmap and `Step 1/Step 2` headings. These are accurate
  summaries of the two-phase structure (formal coefficient computation, then
  integrable-series remainder control), introduce no new mathematical
  assertion, and are **JUSTIFIED**.
- No-goes 16, 20, 31 have equal proof LF lengths (20, 24, 22) and byte-identical
  rendered content; the inventory line offsets reflect only the upstream
  insertion from No-goes 14/15.
- I verified the key arithmetic independently: degree-two expansion
  $1+\frac32z+\frac12w+\frac5{24}z^2+\frac5{12}zw+\frac1{24}w^2$; squared
  coefficients $8/3,1/3$; one-block coefficient $1/3$; difference
  $7A/3+O(A^2)$; $K$-matrix entries $4/3,4/5,17/45$; quadratic form
  $-16/45$; $5/4$ vs $4/3$; scaling $J_c=c^{2/(2-r)}J_1$; tilted-mean exponent
  $2\sigma^2$ vs $\sigma^2$; determinant
  $c_\Gamma^2(A^2-B^2)q_1(x_1)q_2(x_2)$; and the D'Alembert interval
  argument.
- The specified distinctions are all preserved: independent-block scalar
  moments vs phase-space data (14), the full variance coefficient including the
  second-order mean term and the signed-vector quadratic-form arithmetic (15),
  the tilted-mean versus deterministic-surrogate factor (16), the nonseparable
  full control class (20), and the growing-versus-decaying solution branches
  together with displacement-vs-velocity cutoff agreement (31).
- No rewrite defect was found, and no pre-existing defect was uncovered that
  changes the claimed results. Two minor pre-existing brevities (the bound
  $|c|+|s|\le2e^{\sqrt{|z|}}$ is asserted but follows from the closed forms
  $\cosh,\sinh$, and the $K$-entries are said to come from “matrix
  multiplication” without printing intermediate products) occur identically in
  both versions; I verified both and treat them as presentation economy, not
  mathematical gaps.

**Limits.**
- I could not independently re-derive byte equality to the pinned repository
  revisions or the two module SHA-256 values from the rendered payload alone;
  the comparison is over the supplied OLD/NEW scientific views plus the stated
  LF/byte-inventory.
- Baseline upstream proofs (Crouzeix–Palencia, Teschl, Young theory, etc.) are
  unassigned; I used only their declared statements under checked application
  hypotheses (notably `E:threshold` for No-go 20). Primary-source verification
  and rendered-page/human-signoff checks are outside this task.

No partial reads occurred, and no lost step or qualifier was identified.
