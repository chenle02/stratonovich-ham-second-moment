# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

Both assigned proof pairs were read in full, in both revisions, including the unchanged statement and definition lines. Public reconstruction of the target deductions is COMPLETE for both labels: each original logical step is recoverable from supplied public equations, the linear Young construction in `P:constant-young-linear`, and standard one-dimensional estimates. The rewrite adds only explanatory framing and three new explanatory assertions, all of which are correct under the same hypotheses, constants, normalizations and limiting conventions. No new rewrite defect was found. The argument content is PRESERVED sentence-for-equation, with the exception of cosmetic restructuring (`\medskip`, `Step` labels). The constructive check uses the induced operator norm on a nonzero real Banach algebra `B(X)` with submultiplicative norm-one multiplication; no Hilbert or finite-dimensional hypothesis is imported.

---

## L:young-upper-growth

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: statement lines are materially identical at OLD LF 14–26 and NEW LF 14–26; the proof occupies OLD LF 28–54 and NEW LF 28–69. The new material is the small/large separation sentence, the `−log(1−x)` derivative assertion, and the `Step 1`/`Step 2` labels.

### Statement unchanged

The lemma retains the two equations
\[
\sup_{t\le B}\|U_D(t)\|\le \exp\{c_{\theta,B}(d+d^\nu)\},\qquad d=\|D\|_\theta,
\]
\[
\|U_H\|_{C^\theta}+\|U_H^{-1}\|_{C^\theta}\le L_{\theta,B,K}<\infty .
\]
This is the same statement in both revisions, including `d=\|D\|_\theta=\sup_t\|D(t)\|+[D]_\theta`, zero-initial paths, `B\ge 1`, `1/2<\theta<1`, and `\nu=1/\theta<2`. The application hypothesis is checked: `B(X)` is complete because `X` is a Banach space, and the induced operator norm satisfies `\|AB\|\le\|A\|\|B\|`, so the bilinear multiplication in the Young estimate has norm one. The local estimate `E:constant-young-local` is therefore imported into `B(X)` without Hilbert structure.

### Step 1: small driver, linear logarithmic bound

Let `c_\theta=2\max(1,C_\theta)` and `N_\ell(V)=\sup\|V\|+\ell^\theta[V]_\theta`. From the baseline `E:constant-young-estimate` applied to subintervals of `[a,a+\ell]`,
\[
\sup_{[a,a+\ell]}\left\|\int_a^\cdot \ud D\,V\right\|
\le [D]_\theta\ell^\theta\sup\|V\|+C_\theta[D]_\theta\ell^{2\theta}[V]_\theta,
\]
\[
\left[\int_a^\cdot \ud D\,V\right]_\theta
\le [D]_\theta\sup\|V\|+C_\theta[D]_\theta\ell^\theta[V]_\theta .
\]
With `c_\theta=2\max(1,C_\theta)` this is exactly
\[
N_\ell\left(\int_a^\cdot \ud D\,V\right)
\le c_\theta[D]_\theta\ell^\theta N_\ell(V).
\]
This is a genuine contraction setup only if the coefficient is `<1`.

If `c_\theta d B^\theta\le 1/4`, then on the whole interval `[0,B]` the contraction coefficient is
\[
q\le c_\theta[D]_\theta B^\theta\le c_\theta d B^\theta\le 1/4.
\]
The fixed point starts at the identity, so
\[
N_B(U_D)\le\frac{\|I\|}{1-q}=\frac1{1-q},
\quad\text{hence}\quad
\sup_{t\le B}\|U_D(t)\|\le\frac1{1-q}.
\]
Therefore
\[
\log\sup_{t\le B}\|U_D(t)\|\le -\log(1-q)\le 2q\le 2c_\theta B^\theta d.
\]
The new assertion that `\frac d{dx}[-\log(1-x)]=1/(1-x)` is at most two on `[0,1/4]` is correct: the maximum is `1/(1-1/4)=4/3<2`. This verifies the new explanatory claim under the same small-driver regime.

### Step 2: large driver, partition and `d^\nu` bound

In the complementary case `c_\theta d B^\theta>1/4`, set
\[
n_D=\left\lceil B(4c_\theta d)^\nu\right\rceil
\]
equal pieces. With piece length `\ell=B/n_D`,
\[
n_D\ge B(4c_\theta d)^\nu
\implies
n_D^\theta\ge B^\theta(4c_\theta d)^{\nu\theta}
=B^\theta 4c_\theta d
\implies
\ell^\theta\le\frac1{4c_\theta d},
\]
using `\nu\theta=1`. Hence
\[
c_\theta d\,\ell^\theta\le 1/4,
\]
so every local contraction ratio is at most `1/4` and the local solution starting from the identity has `N_\ell(Q)\le 4/3`. The assertion that the quantity inside the ceiling exceeds one follows from the strict large-driver inequality:
\[
4c_\theta d>B^{-\theta}
\implies
B(4c_\theta d)^\nu
>B^{1-\nu\theta}=B^0=1 .
\]
Since `\lceil x\rceil\le 2x` for `x\ge1`,
\[
n_D\le 2B(4c_\theta d)^\nu .
\]
Composing the local evolutions multiplies norms, so with `\log(4/3)<1`,
\[
\sup_{t\le B}\|U_D(t)\|
\le (4/3)^{n_D}
\le\exp\!\big(n_D\log(4/3)\big)
\le\exp\!\big(2B(4c_\theta)^{\nu}d^{\nu}\big).
\]
This is a `d^\nu` bound; the displayed `\exp\{c_{\theta,B}(d+d^\nu)\}` absorbs this by enlarging `c_{\theta,B}`. At `d=0`, `D\equiv0` and the unique Young solution is `U_D=I`, so the bound is `\exp(0)=1` with no prefactor. This checks the requirement to retain both the linear `d` term and the `d^\nu=d^{1/\theta}` term.

### Step 3: global sup and inverse control on a fixed ball

On the ball `\|H\|_\theta\le K`, choose one uniform step `\ell_K=(4c_\theta K)^{-1/\theta}`, so `c_\theta K\ell_K^\theta\le 1/4`. On each piece the local evolution `Q_j` starts from the identity and satisfies `N_{\ell_K}(Q_j)\le 4/3`. Writing `Q_j-I=\int\ud H\,Q_j`,
\[
\sup\|Q_j-I\|
\le c_\theta K\ell_K^\theta N_{\ell_K}(Q_j)
\le \frac14\cdot\frac43=\frac13 .
\]
Thus the Neumann inverse satisfies
\[
\|Q_j(t)^{-1}\|\le\left(1-\frac13\right)^{-1}=\frac32 .
\]
With `n_K=\lceil B/\ell_K\rceil` pieces, the composition law from `P:constant-young-linear` gives, for `t` in the `j`-th piece,
\[
U_H(t)=Q_j(t)U_H(t_j),
\qquad
U_H(t)^{-1}=U_H(t_j)^{-1}Q_j(t)^{-1}.
\]
Hence, uniformly in `H` on the `K`-ball,
\[
\sup_{[0,B]}\|U_H\|\le(4/3)^{n_K},
\qquad
\sup_{[0,B]}\|U_H^{-1}\|\le(3/2)^{n_K}.
\]
This justifies the compressed “products give uniform global sup bounds” sentence.

### Step 4: global Hölder seminorms

On one piece, the identity `U_H(t)=Q_j(t)U_H(t_j)` gives
\[
\|U_H(t)-U_H(s)\|
\le\|Q_j(t)-Q_j(s)\|\,\|U_H(t_j)\|
\le [Q_j]_\theta\,|t-s|^\theta\,(4/3)^{n_K}.
\]
Since `N_{\ell_K}(Q_j)\le 4/3` forces `[Q_j]_\theta\le(4/3)\ell_K^{-\theta}`,
\[
[U_H]_{\text{piece}}\le (4/3)^{n_K+1}\ell_K^{-\theta}.
\]
This supplies the omitted `\|U_H(t_j)\|` factor. For a pair crossing a partition boundary at distance `< \ell_K`, split into at most two subincrements `h_1+h_2=h`, bound each by the local seminorm, and use
\[
h_1^\theta+h_2^\theta
\le 2^{1-\theta}(h_1+h_2)^\theta .
\]
For `h\ge \ell_K`,
\[
\|U_H(t)-U_H(s)\|\le 2\sup\|U_H\|
\le 2\sup\|U_H\|\,\ell_K^{-\theta}h^\theta .
\]
Together with the sup bound, this proves a finite global `C^\theta` norm for `U_H`, uniformly on the ball.

### Step 5: inverse seminorm

The identity
\[
U_H^{-1}(t)-U_H^{-1}(s)
=-U_H^{-1}(t)\big(U_H(t)-U_H(s)\big)U_H^{-1}(s)
\]
is algebraically exact for `s<t`. With finite sup bounds for `U_H` and `U_H^{-1}`,
\[
[U_H^{-1}]_\theta\le \|U_H^{-1}\|_\infty^2\,[U_H]_\theta,
\]
completing the `C^\theta` bound for the inverse. This proves the lemma.

### New material verdict

The new Step 1 explanatory sentence and the derivative estimate are correct; the new Step 2 framing merely labels the unchanged inverse argument. No old sentence, estimate or qualifier is lost.

---

## P:young-upper-multiplicative

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: statement unchanged at OLD LF 62–72 and NEW LF 77–87; proof moves from OLD LF 74–100 to NEW LF 89–135. The display equations are identical. New material consists of the summary sentences, the `Step 1`/`Step 2`/`Step 3` labels, the mesh-power explanation, and the `x=0` observation.

### Step 1: the conjugated perturbation driver

Put `U=U_H`, `R=U^{-1}`, and define
\[
G(s):\mathcal B(\mathcal X)\to\mathcal B(\mathcal X),\qquad
G(s)(Y)=R(s)YU(s).
\]
By the lemma,
\[
\|R(s)\|\le L_{\theta,B,K},\qquad\|U(s)\|\le L_{\theta,B,K}.
\]
Therefore
\[
\|G(s)\|_{\mathcal B(\mathcal B(\mathcal X))}
\le\|R(s)\|\,\|U(s)\|\le L_{\theta,B,K}^2 .
\]
For the Hölder seminorm,
\[
G(s)-G(t)=L_{R(s)-R(t)}\circ R_{U(s)}+L_{R(t)}\circ (L_{U(s)}-L_{U(t)}),
\]
so
\[
\|G(s)-G(t)\|
\le[R]_\theta\|U\|_\infty|s-t|^\theta
+\|R\|_\infty[U]_\theta|s-t|^\theta .
\]
Hence `G` is a `C^\theta` path of bounded linear maps, uniformly bounded on the fixed `\|H\|_\theta\le K` ball. The Young integral is then the bilinear-evaluation integral
\[
Z(t)=\int_0^t G(s)\,\ud X(s)
=\int_0^t R(s)\,\ud X(s)\,U(s).
\]
The evaluation map `(T,Y)\mapsto T(Y)` from `B(B(X))\times B(X)` to `B(X)` is bilinear with norm at most one, so the standard Young estimate applies. Since `X(0)=0`, the Young local approximation is
\[
Z_{s,t}=R(s)X_{s,t}U(s)+O(|t-s|^{2\theta}),
\]
with remainder controlled by `C_\theta[G]_\theta[X]_\theta`. The claimed bound `\|Z\|_\theta\le L'_{\theta,B,K}x` follows because, for `s<t`,
\[
\|Z(t)-Z(s)\|
\le\|G\|_\infty[X]_\theta|t-s|^\theta
+C_\theta[G]_\theta[X]_\theta|t-s|^{2\theta}
\]
and `|t-s|^{2\theta}\le B^\theta|t-s|^\theta` on `[0,B]`; the sup bound is analogous using `Z(0)=0`. This recovers `L'` depending only on `\theta,B,K`.

### Step 2: the two remainders

Let `V=U_Z` be the unique Young solution of
\[
V(t)=I+\int_0^t \ud Z(s)V(s).
\]
The Young estimate gives
\[
V_{s,t}=Z_{s,t}V(s)+O(|t-s|^{2\theta}).
\]
Similarly,
\[
U_{s,t}=H_{s,t}U(s)+O(|t-s|^{2\theta}).
\]

### Step 3: exact product increment

For `P(t)=U(t)V(t)`, with `P_{s,t}=P(t)-P(s)`,
\[
P_{s,t}=U_{s,t}V(s)+U(s)V_{s,t}+U_{s,t}V_{s,t}.
\]
The last term is the cross term:
\[
\|U_{s,t}V_{s,t}\|\le[U]_\theta[V]_\theta |t-s|^{2\theta},
\]
so it is `O(|t-s|^{2\theta})`. The first piece gives
\[
U_{s,t}V(s)
=H_{s,t}U(s)V(s)+O(|t-s|^{2\theta})V(s)
=H_{s,t}P(s)+O(|t-s|^{2\theta}),
\]
using the boundedness of `V(s)` on `[0,B]`. The second piece gives
\[
U(s)V_{s,t}
=U(s)Z_{s,t}V(s)+O(|t-s|^{2\theta})
=U(s)R(s)X_{s,t}U(s)V(s)+O(|t-s|^{2\theta})
=X_{s,t}P(s)+O(|t-s|^{2\theta}).
\]
The decisive cancellation is
\[
U(s)R(s)=I,
\]
which is purely adjacent left-order cancellation; `X_{s,t}` is never commuted past `U(s)`. Since both `H_{s,t}` and `X_{s,t}` multiply `P(s)` on the left,
\[
P_{s,t}=(H+X)_{s,t}P(s)+O(|t-s|^{2\theta}).
\]

### Step 4: uniqueness via vanishing remainder sums

For a partition of `[0,t]`,
\[
P(t)-P(0)
=\sum_j P_{t_j,t_{j+1}}
=\sum_j (H+X)_{t_j,t_{j+1}}P(t_j)
+\sum_j O(|t_{j+1}-t_j|^{2\theta}).
\]
For `h_j=t_{j+1}-t_j` and mesh `h=\max h_j`, since `2\theta>1`,
\[
h_j^{2\theta}=h_j\,h_j^{2\theta-1}\le h_j\,h^{2\theta-1}.
\]
Summing,
\[
\sum_j h_j^{2\theta}
\le h^{2\theta-1}\sum_j h_j
= t\,h^{2\theta-1}
\le B\,h^{2\theta-1}
\longrightarrow 0.
\]
This is exactly the new explanatory sentence: each interval length raised to `2\theta` is at most the interval length times the mesh raised to `2\theta-1`.

The left sums `\sum_j(H+X)_{t_j,t_{j+1}}P(t_j)` converge to the Young integral because `H+X` and `P` are both `C^\theta` operator paths. Since `P(0)=U(0)V(0)=I`, the limit gives
\[
P(t)=I+\int_0^t \ud (H+X)(r)\,P(r).
\]
Uniqueness in `P:constant-young-linear` yields
\[
U_{H+X}=P=U_HU_Z.
\]
This identification uses only `2\theta>1` and uniqueness; no smooth density in the full Hölder norm is invoked.

### Step 5: refined growth applied only to `Z`

The lemma applies to `Z`, since `Z(0)=0` and `Z\in C^\theta`. With `z=\|Z\|_\theta\le L'x`,
\[
\sup_{t\le B}\|U_Z(t)\|
\le\exp\{c_{\theta,B}(z+z^\nu)\}
\le\exp\{c_{\theta,B}M(x+x^\nu)\},
\]
where `M=\max(L',(L')^\nu)`, because
\[
L'x+(L'x)^\nu
\le M x+M x^\nu=M(x+x^\nu).
\]
Define `C_{\theta,B,K}=c_{\theta,B}M`. Since `U_{H+X}=U_HU_Z`,
\[
\|AU_{H+X}(t)\|
=\|AU_H(t)U_Z(t)\|
\le\|AU_H(t)\|\,\|U_Z(t)\|.
\]
No inverse or lower bound for `A` is used. If `x=0`, then `X\equiv0`, so `Z(t)=\int_0^t R(s)0\,U(s)=0`, and `U_Z=I`; the refined growth exponent is zero, so there is no extra factor. This verifies the new `x=0` assertion and the `A=0` case.

### New material verdict

The three new explanatory assertions are correct: the mesh-power inequality, the `2\theta>1` remainder-bounding mechanism, and the `x=0` edge case. There is no change to the derivation, order of multiplication, cross-term accounting, or growth application.

---

## AUDIT dispositions

- `L:young-upper-growth`: Old COMPLETE / New COMPLETE / Reconstruction COMPLETE / Preservation PRESERVED / New explanations JUSTIFIED. PASS.
- `P:young-upper-multiplicative`: Old COMPLETE / New COMPLETE / Reconstruction COMPLETE / Preservation PRESERVED / New explanations JUSTIFIED. PASS.

Both assigned statements are unchanged. No assigned target conclusion was used as an input to skip its own deduction. The unassigned `P:constant-young-linear` result was used only after checking its hypotheses (complete operator algebra, bounded multiplication, zero-initial drivers, `\theta>1/2`); its proof was not counted as an additional reviewed proof. The unassigned model-assumptions context is not invoked by these two deterministic pathwise inequalities.

## Findings and limits

The rewrite is a readability-preserving restructuring: the new proof adds step labels and explanatory sentences while retaining every old equation, estimate and qualifier. The two assigned Young arguments reconstruct entirely from checkable public equations: the local `E:constant-young-local` contraction, the one-dimensional `-\log(1-x)` inequality, the ceiling inequality for the large-driver partition, the Neumann inverse bound, the Hölder splitting `h_1^\theta+h_2^\theta\le 2^{1-\theta}(h_1+h_2)^\theta`, the bilinear-evaluation Young integral for `Z`, the exact product increment with left-order cancellation, and the `B\,h^{2\theta-1}` remainder bound. The retained linear term `d` and power term `d^{1/\theta}` both appear, and the `A=0`/`x=0` edge case is handled without a prefactor. The Banach-space setting is respected: only completeness of `B(X)` and induced-operator-norm submultiplicativity are used; no Hilbert or finite-dimensional structure is imported.

No new rewrite defects were identified within this read. The following are pre-existing or contextual limitations, not rewrite defects: the global Hölder argument in `L:young-upper-growth` is compressed — it omits the right-multiplication factor `\|U_H(t_j)\|` in the one-piece seminorm, but the factor is bounded by the already-established global sup bound, so the step is repairable transparently and is not an error; and the inter-proof remark citing `No-go P:nogo-26`, as well as the Friz–Hairer citation, are external references whose proofs are not supplied in this review. The assigned bounds themselves do not depend on verifying `P:nogo-26`; that remark was outside the assigned proof inventory. Nothing here certifies the upstream analytic results, the source PDFs, rendered pages, or the external references beyond their use under the checked application hypotheses stated in the supplied modules.
