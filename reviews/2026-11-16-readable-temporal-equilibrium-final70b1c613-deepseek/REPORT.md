# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

Both assigned proof pairs were read completely in OLD and NEW form. The first pair is byte-identical over the assigned ranges. The second pair is a reorganization plus one added explanatory sentence; all mathematical content is preserved and the new explanation is correct. Every required deduction below is reconstructed from public identities and estimates.

## L:equilibrium-gamma-beta

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (no new explanatory text was added inside the assigned proof range LF 25–36; the statement range LF 14–23 and proof range LF 25–36 are byte-identical in OLD and NEW)

### Original-step coverage

The proof has five steps: recurrence, Beta–Gamma identity, reduction of
$\operatorname{Beta}(x,x)$ to $\operatorname{Beta}(1/2,x)$, evaluation of
$\Gamma_E(1/2)$, and substitution to obtain duplication. I reconstruct all of them.

**Step 1: recurrence.**
For $x>0$,
\[
\Gamma_E(x+1)=\int_0^\infty u^x e^{-u}\,du
=\Big[-u^x e^{-u}\Big]_{0}^{\infty}+x\int_0^\infty u^{x-1}e^{-u}\,du
=x\Gamma_E(x).
\]
The boundary term vanishes because $u^x\to 0$ as $u\downarrow 0$ for $x>0$, and $u^xe^{-u}\to 0$ as $u\to\infty$. This matches “vanishing boundary terms.”

**Step 2: Beta–Gamma identity.**
For $x,y>0$,
\[
\Gamma_E(x)\Gamma_E(y)
=\int_0^\infty\int_0^\infty u^{x-1}v^{y-1}e^{-(u+v)}\,du\,dv.
\]
Set $u=Rt$, $v=R(1-t)$, with $R>0$, $0<t<1$. The Jacobian is
\[
\left|\det\begin{pmatrix}t&R\\1-t&-R\end{pmatrix}\right|
=|-Rt-R(1-t)|=R.
\]
Then
\[
\int_0^\infty\int_0^1 (Rt)^{x-1}(R(1-t))^{y-1}e^{-R}R\,dt\,dR
=\int_0^\infty R^{x+y-1}e^{-R}\,dR \int_0^1 t^{x-1}(1-t)^{y-1}\,dt
=\Gamma_E(x+y)\operatorname{Beta}(x,y).
\]
The integrand is nonnegative, so Tonelli justifies the interchange. Hence
$\operatorname{Beta}(x,y)=\Gamma_E(x)\Gamma_E(y)/\Gamma_E(x+y)$.

**Step 3: reduction of $\operatorname{Beta}(x,x)$.**
\[
\operatorname{Beta}(x,x)
=\int_0^1 [t(1-t)]^{x-1}\,dt.
\]
Put $t=(1+v)/2$, so $t(1-t)=(1-v^2)/4$ and $dt=dv/2$:
\[
\operatorname{Beta}(x,x)
=2^{-2x+1}\int_{-1}^1 (1-v^2)^{x-1}\,dv
=2^{-2x+2}\int_0^1 (1-v^2)^{x-1}\,dv,
\]
using evenness on $[-1,1]$. Then $v^2=w$, $dv=dw/(2\sqrt w)$, gives
\[
\int_0^1 (1-v^2)^{x-1}\,dv
=\frac12\int_0^1 w^{-1/2}(1-w)^{x-1}\,dw
=\frac12\operatorname{Beta}(1/2,x).
\]
Therefore
\[
\operatorname{Beta}(x,x)=2^{-2x+2}\cdot \frac12\operatorname{Beta}(1/2,x)
=2^{1-2x}\operatorname{Beta}(1/2,x).
\]
This is exactly what the module states after “symmetry, then $t=(1+v)/2$ and $v^2=w$.” The factor $2$ from evenness and the factor $1/2$ from $v^2=w$ combine correctly.

**Step 4: $\Gamma_E(1/2)=\sqrt\pi$.**
With $u=z^2$, $du=2z\,dz$,
\[
\Gamma_E(1/2)=\int_0^\infty u^{-1/2}e^{-u}\,du
=2\int_0^\infty e^{-z^2}\,dz
=\int_{\mathbb R}e^{-z^2}\,dz.
\]
Let $I=\int_{\mathbb R}e^{-z^2}\,dz>0$. Then
\[
I^2=\int_{\mathbb R^2}e^{-(x^2+y^2)}\,dx\,dy
=\int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\theta
=2\pi\int_0^\infty re^{-r^2}\,dr=\pi,
\]
since $\int_0^\infty re^{-r^2}dr=\frac12$. Hence $I=\sqrt\pi$, as the Gaussian integral is positive.

**Step 5: duplication.**
From Step 2,
\[
\operatorname{Beta}(x,x)=\frac{\Gamma_E(x)^2}{\Gamma_E(2x)}.
\]
From Steps 3 and 2,
\[
\operatorname{Beta}(x,x)
=2^{1-2x}\operatorname{Beta}(1/2,x)
=2^{1-2x}\frac{\Gamma_E(1/2)\Gamma_E(x)}{\Gamma_E(x+1/2)}
=\frac{2^{1-2x}\sqrt\pi\,\Gamma_E(x)}{\Gamma_E(x+1/2)}.
\]
Equating and using $\Gamma_E(x)>0$,
\[
\frac{\Gamma_E(x)}{\Gamma_E(2x)}
=\frac{2^{1-2x}\sqrt\pi}{\Gamma_E(x+1/2)},
\]
so
\[
\Gamma_E(2x)=\frac{2^{2x-1}\Gamma_E(x)\Gamma_E(x+1/2)}{\sqrt\pi}.
\]
This proves the stated duplication identity.

### Evidence and assessment

The assigned OLD and NEW ranges are identical, which is confirmed by reading both raw modules: the statement at LF 14–23 and the proof at LF 25–36 coincide. The mathematical checks above verify the recurrence, the Jacobian and Tonelli step, the Beta reduction, the Gaussian integral, and the duplication normalization. No missing step or changed qualification was found in this labeled proof.

Pre-existing concerns: none affecting correctness. The proof is compressed—the Beta reduction and Beta–Gamma substitution are asserted in prose—but every assertion reconstructs from the stated definitions with positive arguments.

## L:temporal-equilibrium

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

### Scope of the two versions

The statement is unchanged at LF 39–53. The OLD proof occupies LF 55–97; the NEW proof occupies LF 55–115 because it inserts three step headings and one additional explanatory sentence in Step 2. All OLD mathematical claims are retained; no hypothesis, domain, normalization, or conclusion changed. The added sentence is the one beginning “Expanding $(1-u)^{r-1}$ in $B_s(r,r)$…”; I check it explicitly below.

### Original-step coverage

The proof has: justification of the positive binomial series; the interior left/right split; the incomplete-Beta reexpression; reflection and symmetry; evaluation of the full potential; direct endpoint values; integrability; and the mass computation. I reconstruct each step with the required factors.

Throughout, $0<a<1$ and $r=(1-a)/2$, so
\[
0<r<\frac12,\qquad 2r\in(0,1),\qquad 2r-1=-a\in(-1,0),\qquad 1-r\in(1/2,1).
\]
In particular $-r>-1$ and $-2r=a-1>-1$.

**Step 1: positive binomial expansion.**
Let $p>0$, $0\le z<1$, and
\[
y(z)=\sum_{n\ge0}\frac{(p)_n}{n!}z^n,\qquad (p)_0=1,\quad (p)_n=p(p+1)\cdots(p+n-1).
\]
The coefficient ratio is
\[
\frac{(p)_{n+1}/(n+1)!}{(p)_n/n!}=\frac{p+n}{n+1}\to 1,
\]
so the series has radius $1$. For fixed $R<1$, ratio or Weierstrass comparison gives uniform convergence on $[0,R]$. The differentiated series has coefficients $(p)_{n+1}/n!$, with the same radius, so termwise differentiation gives
\[
(1-z)y'(z)=p\,y(z),\qquad y(0)=1.
\]
Indeed the coefficient of $z^n$ in $(1-z)y'$ is
\[
\frac{(p)_{n+1}}{n!}-\frac{(p)_n}{(n-1)!}
=\frac{(p)_n}{n!}\big((p+n)-n\big)
=p\frac{(p)_n}{n!}
\]
for $n\ge1$, and the constant term is $p$. Hence
\[
\frac{d}{dz}\Big[(1-z)^p y(z)\Big]
=(1-z)^{p-1}\big((1-z)y'(z)-p y(z)\big)=0,
\]
so $(1-z)^py\equiv 1$, i.e. $y=(1-z)^{-p}$. Since all coefficients are positive, all terms used in the expansions below are nonnegative and Tonelli applies.

**Step 2: the left part.**
Define
\[
K(s)=\int_0^1 |s-t|^{2r-1}[t(1-t)]^{-r}\,dt,\qquad 0<s<1,
\]
so the potential identity is equivalent to $K(s)=\Gamma_E(r)\Gamma_E(1-r)$ for every $s\in[0,1]$. On $0<t<s$, set $t=su$:
\[
L(s)
=\int_0^s (s-t)^{2r-1}[t(1-t)]^{-r}\,dt
=s^r\int_0^1 (1-u)^{2r-1}u^{-r}(1-su)^{-r}\,du.
\]
Because $su\le s<1$, expand $(1-su)^{-r}=\sum_{n\ge0}(r)_n(su)^n/n!$:
\[
L(s)=s^r\sum_{n\ge0}\frac{(r)_ns^n}{n!}\int_0^1(1-u)^{2r-1}u^{n-r}\,du.
\]
The integral is
\[
\operatorname{Beta}(n-r+1,2r)
=\frac{\Gamma_E(n-r+1)\Gamma_E(2r)}{\Gamma_E(n+r+1)}.
\]
Using the Gamma recurrence exactly as in the first assigned lemma,
\[
\Gamma_E(n-r+1)=(1-r)_n\Gamma_E(1-r),\qquad
\Gamma_E(n+r+1)=(1+r)_n\Gamma_E(1+r),
\]
and $1-r+2r=1+r$, so
\[
\operatorname{Beta}(n-r+1,2r)
=\operatorname{Beta}(1-r,2r)\frac{(1-r)_n}{(1+r)_n}.
\]
Therefore
\[
L(s)
=\operatorname{Beta}(1-r,2r)s^r
\sum_{n\ge0}\frac{(r)_n(1-r)_ns^n}{(1+r)_n n!},
\]
which is exactly the module’s displayed expression. Nonnegativity justifies termwise integration here.

**Step 3: the $r/(r+n)$ factors and incomplete Beta.**
The module asserts $(r)_n/(1+r)_n=r/(r+n)$. Telescoping,
\[
\frac{(r)_n}{(1+r)_n}
=\frac{r(r+1)\cdots(r+n-1)}{(r+1)(r+2)\cdots(r+n)}
=\frac{r}{r+n},
\]
with the empty-product case $n=0$ giving $1=r/r$, also correct.

Now
\[
B_s(r,r)=\int_0^s u^{r-1}(1-u)^{r-1}\,du,\qquad 0<s<1.
\]
With $p=1-r>0$, the exponent $r-1=-(1-r)$ gives
\[
(1-u)^{r-1}=\sum_{n\ge0}\frac{(1-r)_n}{n!}u^n.
\]
Termwise integration over $[0,s]$ yields
\[
B_s(r,r)
=\sum_{n\ge0}\frac{(1-r)_n}{n!}\frac{s^{r+n}}{r+n},
\]
using $\int_0^s u^{r+n-1}du=s^{r+n}/(r+n)$ with $r+n>0$. This verifies the NEW explanatory sentence’s claim that the expansion gives coefficient $(1-r)_n/n!$ and integral $s^{r+n}/(r+n)$.

Multiplying by $r\operatorname{Beta}(1-r,2r)$:
\[
r\operatorname{Beta}(1-r,2r)B_s(r,r)
=\operatorname{Beta}(1-r,2r)s^r
\sum_{n\ge0}\frac{(1-r)_n}{n!}\frac{r}{r+n}s^n.
\]
By $r/(r+n)=(r)_n/(1+r)_n$, the right side is exactly $L(s)$:
\[
L(s)=r\operatorname{Beta}(1-r,2r)B_s(r,r).
\]
Thus the NEW sentence “Multiplication by $r\operatorname{Beta}(1-r,2r)$ therefore gives exactly the coefficients of $L(s)$” is correct.

**Step 4: reflection and symmetry.**
For the right part, $t\mapsto 1-t$ gives
\[
\int_s^1 (t-s)^{2r-1}[t(1-t)]^{-r}\,dt
=\int_0^{1-s}\big((1-s)-u\big)^{2r-1}[u(1-u)]^{-r}\,du
=L(1-s).
\]
Also, substituting $v=1-u$ in one of the two incomplete Beta integrals,
\[
B_s(r,r)+B_{1-s}(r,r)
=\int_0^s u^{r-1}(1-u)^{r-1}du+\int_s^1 u^{r-1}(1-u)^{r-1}du
=\operatorname{Beta}(r,r).
\]
Hence for $0<s<1$,
\[
K(s)=r\operatorname{Beta}(1-r,2r)\operatorname{Beta}(r,r).
\]

**Step 5: evaluation of the potential.**
\[
r\operatorname{Beta}(1-r,2r)\operatorname{Beta}(r,r)
=r\,\frac{\Gamma_E(1-r)\Gamma_E(2r)}{\Gamma_E(1+r)}
\cdot\frac{\Gamma_E(r)^2}{\Gamma_E(2r)}.
\]
The $\Gamma_E(2r)$ factors cancel, and $\Gamma_E(1+r)=r\Gamma_E(r)$, so
\[
K(s)=\Gamma_E(1-r)\Gamma_E(r)\cdot \frac{r\Gamma_E(r)}{\Gamma_E(1+r)}
=\Gamma_E(r)\Gamma_E(1-r).
\]
Since
\[
f_a(t)=\frac{[t(1-t)]^{-r}}{\Gamma_E(r)\Gamma_E(1-r)},
\]
we obtain for every interior $s$
\[
\int_0^1 |s-t|^{-a}f_a(t)\,dt
=\frac{K(s)}{\Gamma_E(r)\Gamma_E(1-r)}=1.
\]
This is \eqref{E:temporal-equilibrium-potential} without any assumption that $K(s)$ equals the target value being skipped; the full evaluation is above.

**Finiteness of the interior integrals.** Near $u=0$ in the left integrand the exponent is $u^{-r}$ with $-r>-1$; near $u=1$ it is $(1-u)^{2r-1}$ with $2r-1>-1$. The Beta factors have positive arguments because $1-r>0$ and $2r>0$, and $B_s(r,r)$ has exponent $r-1>-1$ at both ends. Thus all displayed integrals are finite.

**Step 6: direct endpoint values.**
At $s=0$,
\[
K(0)=\int_0^1 t^{2r-1}[t(1-t)]^{-r}\,dt
=\int_0^1 t^{r-1}(1-t)^{-r}\,dt
=\operatorname{Beta}(r,1-r)
=\Gamma_E(r)\Gamma_E(1-r),
\]
with the singular exponents $r-1>-1$ near $0$ and $-r>-1$ near $1$. Therefore
\[
\int_0^1 t^{-a}f_a(t)\,dt=1
\]
directly, with no endpoint limit taken. At $s=1$, the same substitution $t\mapsto1-t$ gives the same value. This preserves the statement “for every $s\in[0,1]$” under the stated hypothesis $0<a<1$.

**Step 7: $L^1\cap L^2$ membership.**
The constant in $f_a$ is $\Gamma_E(r)\Gamma_E(1-r)>0$. Near $t=0$ and $t=1$, $f_a(t)$ behaves like $t^{-r}$ and $(1-t)^{-r}$, respectively, and $-r>-1$, so $f_a\in L^1(0,1)$. For $L^2$, $f_a(t)^2$ behaves like $t^{-2r}$ and $(1-t)^{-2r}$, and
\[
-2r=a-1>-1,
\]
because $a>0$. Hence $f_a\in L^2(0,1)$.

**Step 8: exact unrenormalized mass.**
\[
M_a=\int_0^1 f_a(t)\,dt
=\frac{1}{\Gamma_E(r)\Gamma_E(1-r)}
\int_0^1 t^{-r}(1-t)^{-r}\,dt
=\frac{\operatorname{Beta}(1-r,1-r)}{\Gamma_E(r)\Gamma_E(1-r)}.
\]
Using the Beta–Gamma identity,
\[
M_a=\frac{\Gamma_E(1-r)^2/\Gamma_E(2-2r)}
{\Gamma_E(r)\Gamma_E(1-r)}
=\frac{\Gamma_E(1-r)}{\Gamma_E(2-2r)\Gamma_E(r)}.
\]
Translate from $r$ back to $a$: $r=(1-a)/2$, $1-r=(1+a)/2$, and $2-2r=1+a$. Thus
\[
M_a=\frac{\Gamma_E((1+a)/2)}
{\Gamma_E(1+a)\Gamma_E((1-a)/2)}.
\]
All arguments are positive because $0<a<1$, so $M_a>0$. The proof explicitly retains “Its time mass has not been renormalized,” and the derivation does not replace $M_a$ by $1$.

### Evidence and assessment

OLD proof LF 55–97 and NEW proof LF 55–115 were both read completely. The only new mathematical assertion in the second proof is the sentence giving the incomplete-Beta expansion coefficients; it is correct, as shown in Step 3. The NEW Step headings and summary sentence do not alter hypotheses, domains, normalizations, the fixed exterior normalization $1/[\Gamma_E(r)\Gamma_E(1-r)]$, the endpoint treatment, or the unnormalized mass. No byte-retention reasoning was used to establish preservation; the equations above reconstruct the deductions from the module’s public definitions and the Gamma/Beta identities.

Pre-existing concerns: none affecting correctness. A mild pre-existing compression is that the coefficient ratio argument for the binomial series and the Gamma-recurrence step in the Beta ratio are stated tersely; both are standard and are explicitly reconstructed above. The endpoint argument at $s=0,1$ is direct and valid for the open range $0<a<1$, so no unjustified parameter endpoint or asymptotic claim is introduced.

## AUDIT dispositions

- Assigned proof pairs counted: exactly two — “L:equilibrium-gamma-beta” and “L:temporal-equilibrium.”
- Unassigned baseline context file was not counted as an additional reviewed proof and was not needed beyond noting it supplies model context.
- Gamma/Beta proof: OLD and NEW assigned ranges are byte-identical; still read and mathematically reconstructed in full.
- Temporal-equilibrium proof: NEW changes are additive reorganization plus one explanatory sentence; mathematical argument preserved.
- No silent repair, invented claim, tool use, file access beyond the supplied modules, delegation, or authoring workflow was performed.

## Findings and limits

No rewrite defect was found. Both proofs preserve their statements and conclusions under the stated hypotheses. The NEW additions are explanatory and correct. The only limitations are that the source prose is compressed in places and the reconstruction above supplies the routine expansions; this is a pre-existing stylistic feature, not a new defect. I did not certify source PDFs, images, Lean correspondence, rendered pages, or release status. The verification is confined to the two assigned proof modules and their public mathematical content.
