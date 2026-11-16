# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

The OLD and NEW complete proofs are mathematically equivalent for all four assigned
proof pairs. The NEW revision adds forward references, step labels, an explicit
phase-isometry/conjugation identity, and explicit coefficient bookkeeping; these new
explanatory passages are all justified by the surrounding estimates. I reconstructed
the nontrivial deductions directly from the displayed equations and scalar estimates,
treating OLD as a peer copy rather than an oracle. Unassigned upstream inputs
(`L:cutoff-factorization`, `L:constant-phase-free`,
`P:cameron-actual-embedding`, `E:compact-F-block`, and the stated Teschl imports) are
used only under their checked hypotheses, and their proofs are not counted.

---

## L:signed-limiting-multiplier

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

### Original-step coverage and working

Let the unit constant-displacement vector be $e_c=(0,0,1,0)\in F$.
For $L_q(u,v,c_1,c_2)=(0,V_q(u+c_1),0,0)$, the image
$L_q e_c=(0,V_q,0,0)$ has $F$-norm exactly
$\|V_q\|_{H^{-1/2}}$, because the first $E$-coordinate vanishes and the $E$-norm is
$\|(u,v)\|_E^2=\|u\|_{H^{1/2}}^2+\|v\|_{H^{-1/2}}^2$. Hence, for an operator-norm
Cauchy sequence $L_{q_n}$,
\[
\|V_{q_n}-V_{q_j}\|_{H^{-1/2}}
=\|(L_{q_n}-L_{q_j})e_c\|_F
\le\|L_{q_n}-L_{q_j}\|\to0 .
\]
Completeness of $H^{-1/2}$ gives a limit $V$. Testing against $\varphi\in
C_c^\infty(\mathbb R^d)$ with $\operatorname{supp}\varphi\cap\operatorname{supp}
m_R=\varnothing$ gives $\langle V_{q_n},\varphi\rangle=0$ for every $n$, so the
weak/distributional limit satisfies $\langle V,\varphi\rangle=0$; hence
$\operatorname{supp}V\subseteq\operatorname{supp}m_R$. Real conjugation commutes with
closure, so $V$ is real.

The zero columns are preserved: $L_{q_n}$ has zero first $E$-coordinate, zero
constant output, and depends on $(u,c_1)$ only through $u+c_1$; these identities
pass to the operator-norm limit. Define the multiplier $M_n:H^{1/2}\to H^{-1/2}$,
$M_n u=(L_{q_n}(u,0,0,0))_{v\text{-coordinate}}=V_{q_n}u$. Then
\[
\|M_n-M_j\|_{\mathcal B(H^{1/2},H^{-1/2})}
=\sup_{\|u\|_{H^{1/2}}\le1}\|(V_{q_n}-V_{q_j})u\|_{H^{-1/2}}
\le\|L_{q_n}-L_{q_j}\|,
\]
so $M_n$ is Cauchy with limit $M$ of norm at most $k=\|L\|$. For compact smooth
$u$, multiplication by $u$ is bounded on $H^{-1/2}$ by
Lemma~`L:cutoff-factorization`, so $V_{q_n}u\to Vu$ in $H^{-1/2}$; thus $Mu=Vu$
on tests. Since $C_c^\infty$ is dense in $H^{1/2}$, the bounded identification
extends to all of $H^{1/2}$, and $L(u,v,c_1,c_2)=(0,Vu+c_1V,0,0)$. The
constant-displacement column recovers $V$ uniquely from $L$.

For compact smooth $u,w$,
\[
v_V(u,w)=\langle Vu,w\rangle_{H^{-1/2},H^{1/2}}
=\langle V,uw\rangle,
\]
which is symmetric in $u,w$. The bound
\[
|v_V(u,w)|
\le\|Vu\|_{H^{-1/2}}\|w\|_{H^{1/2}}
\le k\|u\|_{H^{1/2}}\|w\|_{H^{1/2}}
\]
is exactly `E:signed-multiplier-form`; it extends by sesquilinear density. For
complexification, $\|L_{\mathbb C}\|=\|L\|$ by splitting real/imaginary parts into
the Hilbert direct sum, and the Hermitian diagonal is
$v_V(a+ib,a+ib)=v_V(a,a)+v_V(b,b)$ with cross terms canceling from symmetry.

### NEW-vs-OLD

NEW proof (LF21--41) adds the opening sentence defining $v_V$ as the duality
pairing and a forward reference to the multiplier bound; OLD proof (LF21--37) begins
directly with the approximation. All subsequent steps and displays are identical in
content. The opening is consistent, not circular (the bound is proved immediately
afterward), and the forward reference is harmless.

- Lost steps/qualifiers: none identified within this read.
- Pre-existing concerns: relies on the unassigned facts that smooth compact
  multiplication is bounded on $H^{-1/2}$ (`L:cutoff-factorization`) and that the
  $L_{q_n}$ belong to $\mathcal K(F)$; these are supplied upstream and checked in
  application.

---

## P:signed-closed-form

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

### Step 1: closed, semibounded shifted form

Put $b=\|u\|_2$, $z=\|u\|_{H^1}=\|B_0^{1/2}u\|_2$ with $B_0=1-\Delta$. Fourier
Cauchy--Schwarz gives
\[
\|u\|_{H^{1/2}}^2=\int(1+|\xi|^2)^{1/2}|\hat u|^2
\le\bigl(\int(1+|\xi|^2)|\hat u|^2\bigr)^{1/2}
\bigl(\int|\hat u|^2\bigr)^{1/2}=bz .
\]
Using $|v_V(u,u)|\le K\|u\|_{H^{1/2}}^2$ (`E:signed-multiplier-form`) and
$Kbz=\sqrt{z^2\cdot (Kb)^2}\le\frac12 z^2+\frac12K^2b^2$ (weighted AM--GM, valid at
zero norms), and $q_V=z^2-b^2-v_V(u,u)$, $c=2+K^2$:
\[
q_V(u)+c b^2
\ge z^2-b^2-\tfrac12z^2-\tfrac12K^2b^2+(2+K^2)b^2
=\tfrac12 z^2+\bigl(1+\tfrac{K^2}{2}\bigr)b^2,
\]
\[
q_V(u)+c b^2
\le z^2-b^2+\tfrac12z^2+\tfrac12K^2b^2+(2+K^2)b^2
=\tfrac32 z^2+\bigl(1+\tfrac{3K^2}{2}\bigr)b^2 .
\]
Since $b\le z$ and $L_K=3(1+K^2)$, the upper side is
$\le(\tfrac52+\tfrac32K^2)z^2\le L_Kz^2$. Thus the shifted form
$q_A=q_V+c\|\cdot\|_2^2$ is equivalent to the complete $H^1$ norm, hence is
closed (the $c\|\cdot\|_2^2$ perturbation is relatively bounded), densely defined,
and semibounded; Teschl Theorem~2.14 (p.~81, (2.63)) then yields a unique
self-adjoint $H_V$. The lower bound also gives
$q_A(u)\ge\frac12b^2+(1+\frac{K^2}{2})b^2\ge b^2$, so $A=H_V+c\ge1$ as a form; a
bounded spectral slice below $1$ would give a unit $D(A)$ vector with
$\langle Au,u\rangle<1$, contradicting this form bound, so $A\ge1$ spectrally.
The closed-form domain is $Q(q_A)=\overline{}^{q_A}H^1=H^1=D(A^{1/2})$ (Teschl
Thm.~3.6/(3.51)--(3.53), applied after shifting). The representation of $H_V$ is
independent of the admissible shift, and the stated `E:signed-form-bounds` follow.

### Step 2: square-root comparison via resolvents

On $H^1$, the Step-1 bounds give $\frac12 B_0\le A\le L_KB_0$ as forms. For
positive self-adjoint $T_0,S_0\ge1$ with common form domain and
$q_{T_0}\le q_{S_0}$, completing the square yields
\[
\langle f,(T_0+t)^{-1}f\rangle
=\sup_u\bigl\{2\operatorname{Re}\langle f,u\rangle-q_{T_0}(u)-t\|u\|^2\bigr\}
\ge\langle f,(S_0+t)^{-1}f\rangle,
\]
so $(T_0+t)^{-1}\ge(S_0+t)^{-1}$, hence
$I-t(T_0+t)^{-1}\le I-t(S_0+t)^{-1}$.
The scalar identity
\[
\sqrt x=\frac1\pi\int_0^\infty t^{-1/2}\frac{x}{x+t}\,dt
\]
follows from $t=xr^2$ and $\int_0^\infty 2(1+r^2)^{-1}dr=\pi$. Writing
$x/(x+t)=1-t/(x+t)$, positive spectral integration and Tonelli give
$T_0^{1/2}\le S_0^{1/2}$ with the corresponding domain inclusions. This is an
explicit resolvent argument, not an assumed order rule for noncommuting powers.

Apply to $(B_0,2A)$: since $q_{B_0}\le q_{2A}$, one gets
$B_0^{1/2}\le(2A)^{1/2}=\sqrt2 A^{1/2}$. On the core $H^1$,
$\langle f,B_0^{1/2}f\rangle=\|B_0^{1/4}f\|_2^2$ and
$\langle f,\sqrt2 A^{1/2}f\rangle=\sqrt2\|A^{1/4}f\|_2^2$, so
\[
\|B_0^{1/4}f\|_2\le 2^{1/4}\|A^{1/4}f\|_2,\qquad f\in H^1 .
\]
Because $H^1$ is a core for $A^{1/4}$ and $B_0^{1/4}$ is closed, this domination
extends to $f\in D(A^{1/4})$ with $D(A^{1/4})\subseteq D(B_0^{1/4})=H^{1/2}$, giving
\[
2^{-1/4}\|f\|_{H^{1/2}}\le\|A^{1/4}f\|_2 .
\]
Apply to $(A,L_KB_0)$: $q_A\le q_{L_KB_0}$ gives
$A^{1/2}\le(L_KB_0)^{1/2}=L_K^{1/2}B_0^{1/2}$, hence
$\|A^{1/4}f\|_2^2\le L_K^{1/2}\|B_0^{1/4}f\|_2^2$ on $H^1$. Since $H^1$ is dense in
$H^{1/2}=D(B_0^{1/4})$, domination by the closed operator $A^{1/4}$ extends this,
giving $H^{1/2}\subseteq D(A^{1/4})$ and
\[
\|A^{1/4}f\|_2\le L_K^{1/4}\|f\|_{H^{1/2}} .
\]
Combining the two inclusions gives `E:signed-quarter-phase` with exact constants
$2^{-1/4}$ and $L_K^{1/4}$.

### Negative dual completion

The dual norm of the phase space $X=D(A^{1/4})=\{\|A^{1/4}u\|_2<\infty\}$ under
the $L^2$ pairing is
\[
\|A^{-1/4}v\|_2
=\sup_{\|A^{1/4}u\|_2=1}|\langle v,u\rangle|,
\]
the upper bound by Cauchy--Schwarz and the attainment by $u=A^{-1/2}v$ after
normalization. Completion therefore identifies the dual with the negative space
$H^{-1/2}$ under $A^{-1/4}$.

### NEW-vs-OLD

OLD proof LF65--115; NEW proof LF69--130. NEW inserts the two-sentence overview and
`Step 1`/`Step 2` headings; the displayed inequalities and constants are identical.
No $H^2$ operator domain claim is made, and no $A$-power comparison is imported.

- Lost steps/qualifiers: none identified.
- Pre-existing concerns: the text compresses the extension from the core $H^1$ to
  the quarter-power domains; I filled this via closure/core density. It is a
  presentational abbreviation, not a new rewrite defect.

---

## L:signed-spectral-wave

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

### Step 1: spectral bottom

From Step 1 of the closed-form proposition, for $\|u\|_2=1$ and $z=\|u\|_{H^1}\ge1$,
\[
q_V(u)\ge\tfrac12 z^2-1-\tfrac{K^2}{2}
\ge-\tfrac{1+K^2}{2}\ge-K^2,
\]
so $\beta(V)\ge-K^2$. For the upper bound, take a real unit $\varphi\in C_c^\infty$
and set $\varphi_\varepsilon(x)=\varepsilon^{-d/2}\varphi((x-x_0)/\varepsilon)$ with
$\varepsilon\to\infty$ and $x_0$ chosen so that $\operatorname{supp}\varphi_\varepsilon$
is disjoint from $\operatorname{supp}m_R$. Then $\|\varphi_\varepsilon\|_2=1$, the
pairing $v_V(\varphi_\varepsilon,\varphi_\varepsilon)=0$, and
$\|\nabla\varphi_\varepsilon\|_2^2=\varepsilon^{-2}\|\nabla\varphi\|_2^2\to0$.
This is purely the compact support and dilation/translation argument; no positivity
of $V$ is used. Hence $\beta\le0$, so $-K^2\le\beta\le0$ and
$\lambda=\sqrt{-\beta}$ is well defined with $0\le\lambda\le K$.

Complex form infima agree with real ones because for a complex diagonal
$a+ib$, $q_V(a+ib)=q_V(a)+q_V(b)$. The form/spectral equality: for
$u\in Q(q_V)$, $q_V(u)=\int h\,d\mu_u(h)$ with $\mu_u$ the spectral measure, so
$q_V(u)\ge\inf\operatorname{spec}H_V$; conversely spectral projections onto
arbitrarily small neighborhoods of the bottom give approximate form tests,
equality follows (`(3.52)--(3.53)`). The PVM support equals the spectrum via the
resolvent argument (bounded $(h-z)^{-1}$ off the closed support, approximate
eigenvectors on it), and a unit vector's spectral measure is a nonzero finite
measure, so the spectrum is nonempty. Therefore every spectral value satisfies
$h\ge\beta$, hence $h+c\ge\beta+c\ge -K^2+2+K^2=2$.

### Step 2: phase norm and matrix entries

Define $\|(u,v)\|_{E_A}^2=\|A^{1/4}u\|_2^2+\|A^{-1/4}v\|_2^2$. By
`E:signed-quarter-phase` and duality, both entries are trapped with
$M_K=L_K^{1/4}$:
\[
M_K^{-1}\|(u,v)\|_E\le\|(u,v)\|_{E_A}\le M_K\|(u,v)\|_E,
\]
with condition-number cost
$M_K^2=\sqrt{3(1+K^2)}\le2(1+K)$.

The NEW text makes explicit that $(u,v)\mapsto(A^{1/4}u,A^{-1/4}v)$ is an
isometry onto $L^2\times L^2$ (the negative-power map extended to completed
velocity space), and that the displayed matrix is the conjugation of
\[
P_V^E(t)\binom uv=\binom{C_t(H_V)u+S_t(H_V)v}{-H_VS_t(H_V)u+C_t(H_V)v}.
\]
This is correct: the upper-right entry is
$A^{1/4}S_t(H_V)v=A^{1/4}S_t A^{1/4}(A^{-1/4}v)=A^{1/2}S_t(A^{-1/4}v)$,
with multiplier $\sqrt{h+c}S_t(h)$; the lower-left entry is
$A^{-1/4}(-H S_t u)=-H S_t A^{-1/2}(A^{1/4}u)$, with multiplier
$-hS_t(h)/\sqrt{h+c}$.

Entry bounds. For $h\ge0$, $|C_t|\le1$, $|S_t|\le\min(t,h^{-1/2})$, and, using
$\sqrt{h+c}\le\sqrt h+\sqrt c$,
\[
\sqrt{h+c}|S_t|
\le(\sqrt h+\sqrt c)\min(t,h^{-1/2})
\le1+\sqrt c\,t,
\]
while $|hS_t|/\sqrt{h+c}=\sqrt{h}|\sin(t\sqrt h)|/\sqrt{h+c}\le1$; at $h=0$ the
off-diagonal entries are $\sqrt c\,t$ and $0$. For $\beta\le h<0$, with
$\rho=\sqrt{-h}$ and $\lambda=\sqrt{-\beta}$: $|C_t|=\cosh(t\rho)\le e^{\lambda t}$,
$|S_t|=\sinh(t\rho)/\rho\le te^{\rho t}\le te^{\lambda t}$ (using $\sinh s\le
s e^{s}$), and since $\rho\le\lambda\le K$ and $h+c\le c$,
\[
\sqrt{h+c}|S_t|\le\sqrt c\,t e^{\lambda t}.
\]
The lower off-diagonal absolute value is
\[
\left|\frac{hS_t}{\sqrt{h+c}}\right|
=\frac{\rho\sinh(t\rho)}{\sqrt{h+c}}\le Ke^{\lambda t},
\]
using $\sinh(t\rho)\le\cosh(t\rho)\le e^{\lambda t}$, $\rho\le K$, and
$h+c\ge2$. This is exactly the NEW added zero-rate remark: the estimate reads
without dividing by $\lambda$, so it remains valid when $\beta=0$ ($\lambda=0$).

Since $\sqrt c\le2K$, every matrix entry is at most
$2(1+K)(1+t)e^{\lambda t}$; the $2\times2$ operator norm is at most twice an
entrywise bound, and the condition-number cost gives
\[
\|P_V^E(t)\|_{\mathcal B(E)}
\le M_K^2\cdot 4(1+K)(1+t)e^{\lambda t}
\le8(1+K)^2(1+t)e^{\lambda t},
\]
i.e. `E:signed-E-wave`. Bounded Borel calculus (`Teschl` Thm.~3.1), zero
extension off the spectral support, and dominated convergence give strong
continuity; scalar addition identities give the group property. The same
entrywise bounds apply on the graph levels $D(A^{1/2})\times L^2$ and
$D(A)\times D(A^{1/2})$, since e.g. $A^{1/2}S_t(H_V)$ has the bounded multiplier
$\sqrt{h+c}S_t(h)$ and $H_VS_t(H_V)$ is controlled by the displayed entries;
spectral cutoffs justify extensions and continuity there.

### NEW-vs-OLD

OLD LF136--184; NEW LF151--226. NEW adds `Step 1`/`Step 2`, the explicit isometry
map, the explicit spectral-solution formula, and the zero-rate lower off-diagonal
explanation. All are correct enhancements.

- Lost steps/qualifiers: none identified.
- Pre-existing concerns: graph-level membership is summarized rather than expanded;
  the entrywise controls above justify the summary. No bottom eigenstate is asserted,
  and no division by $\lambda$ appears.

---

## P:signed-physical-wave

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

### Step 1: distributional equation and graph embedding

Testing the form representation $q_V(u,\varphi)=\langle H_Vu,\varphi\rangle$
against compact smooth $\varphi$ gives, since
$q_V(u,\varphi)=\int\nabla u\cdot\nabla\varphi-v_V(u,\varphi)$,
\[
\langle H_Vu,\varphi\rangle=\langle-u,\Delta\varphi\rangle-\langle Vu,\varphi\rangle,
\]
so $H_Vu=-\Delta u-Vu$ in distributions for $u\in D(H_V)$. Since $u\in H^1$ and the
multiplier bound gives $Vu\in H^{-1/2}$,
\[
(1-\Delta)u=u-(-\Delta u)=u+H_Vu+Vu\in H^{-1/2},
\]
hence $u=(1-\Delta)^{-1}(u+H_Vu+Vu)\in H^{3/2}$. Graph continuity: by
`E:signed-form-bounds`, $\|u\|_{H^1}^2\le2\langle Au,u\rangle\le\|Au\|_2^2+\|u\|_2^2$,
and with $H_Vu=Au-cu$,
\[
\|u\|_{H^{3/2}}=\|(1-\Delta)u\|_{H^{-1/2}}
\le c\|u\|_2+\|Au\|_2+K\|u\|_{H^1},
\]
which is controlled by the $A$-graph norm. No $H^2$-operator-domain identity is
needed.

### Step 2: free generator and Duhamel identity on graph data

The free generator is $A_0(u,v)=(v,\Delta u)$ on $H^{3/2}\times H^{1/2}$. This is
checked by differentiating the free Fourier matrix after a frequency cutoff and
removing the cutoff in the graph norm; conversely a strong generator derivative has
components $v\in H^{1/2}$ and $\Delta u\in H^{-1/2}$, which together with
$u\in H^{1/2}$ force $u\in H^{3/2}$. No operator-norm differentiability of the free
group is used.

On spectral data in $D(A)\times D(A^{1/2})=D(H_V)\times H^1$, the cutoff trajectory
$u_n(t)=C_t(H)u_n+S_t(H)v_n$, $v_n(t)=-H S_t(H)u_n+C_t(H)v_n$ differentiates (using
$C_t'=-hS_t$, $S_t'=C_t$) to $u_t=v$, $v_t=-Hu$. The graph-level entry bounds pass to
the limit by spectral dominated convergence, giving graph-continuous trajectories
and $C^1$ motion in $H^1\times L^2$. The graph embedding gives continuity in
$D(A_0)$ and
\[
z_t=A_0z+L_Ez,\qquad L_Ez=(0,Vu).
\]
The strong-group chain rule on $D(A_0)$ gives
\[
S_E(-t)z(t)=z(0)+\int_0^t S_E(-s)L_Ez(s)\,ds.
\]
Graph data are dense in $E$: spectral cutoffs make $D(A)$ dense in
$D(A^{1/2})=H^1$, and $H^1$ is dense in both $H^{1/2}$ and $H^{-1/2}$. Boundedness
on finite horizons extends the identity to all of $E$, and Volterra/Picard uniqueness
identifies the spectral wave with the bounded-perturbation physical wave on $E$.
No $D(A^{3/4})=H^{3/2}$ identity is asserted.

### Step 3: full $F$ flow and Young identification

On $F$, bounded $L$ and strongly continuous $S_F$ define the Duhamel flow; the $n$-th
Volterra term obeys
$\|W_n(t)\|\le C_T^{n+1}\|L\|^nT^n/n!$ with
$C_T\ge\max(1,\sup_{|r|\le T}\|S_F(r)\|)$, giving convergence and uniqueness.
The interaction primitive is $\int_0^t C(s)\,ds$ with
$C(s)=S_F(-s)LS_F(s)$. To see norm continuity, for $s_n\to s$:
$\|(S_F(-s_n)-S_F(-s))LS_F(s_n)\|$ is the left strong difference applied to the
precompact set $L(B_F)$, so it vanishes uniformly; and
$\|L(S_F(s_n)-S_F(s))\|$ vanishes by adjoint strong convergence applied to the
compact $L^\*$ on $B_F$, followed by taking adjoints. This uses compactness of $L$,
strong continuity of $S_F$ and its adjoint (the latter available from the explicit
Fourier matrix/direct-sum structure), exactly as in
`P:cameron-actual-embedding`. Hence the primitive is Lipschitz in $\mathcal B(F)$,
and the ordinary interaction equation is the Young equation.

### Step 4: both constant columns

For initial $(e,c_1,c_2)$ the constant block evolves exactly as
$(c_1+tc_2,c_2)$, and the $E$-component is
\[
P_V^E(t)e+\int_0^t P_V^E(t-s)\bigl(0,V(c_1+sc_2)\bigr)\,ds .
\]
Substituting the free/Duhamel expression for $P_V^E$ under the integral and changing
order on the triangle $0\le r\le s\le t$ (absolute in $E$ by the finite-horizon
bounds) shows the candidate solves the full free Duhamel equation with force
$B_Ey+(0,V(c_1+sc_2))$; uniqueness then identifies it. The forcing norm is
\[
\|(0,V(c_1+sc_2))\|_E
=\|V(c_1+sc_2)\|_{H^{-1/2}}
\le\|V\|_{H^{-1/2}}|c_1+sc_2|
\le K(1+s)|(c_1,c_2)|,
\]
using $\|V\|_{H^{-1/2}}=\|Le_c\|_F\le\|L\|\le K$ and
$|c_1+sc_2|\le\sqrt{1+s^2}|c|\le(1+s)|c|$. Since $\lambda\ge0$,
$\int_0^t(1+t-s)(1+s)\,ds=t+t^2+t^3/6\le(1+t)^3$, and the constant block has norm
at most $(1+t)|c|$, the total norm is at most
\[
(1+t)^3e^{\lambda t}
\bigl\{8(1+K)^2\|e\|+
[8K(1+K)^2+1]|(c_1,c_2)|\bigr\}.
\]
The NEW added coefficient chain is valid:
$8(1+K)^2\le8(1+K)^3$, and
$8K(1+K)^2+1\le8(1+K)^3+(1+K)^3=9(1+K)^3$, since $K\le1+K$ and $1\le(1+K)^3$.
Cauchy--Schwarz on the two scalar components gives
\[
\sqrt{8^2+9^2}(1+K)^3\le13(1+K)^3,
\]
and $13(1+K)^3\le16(1+K)^4$, so
\[
\|P_V(t)\|_{\mathcal B(F)}
\le16(1+K)^4(1+t)^3 e^{\lambda t},
\]
i.e. `E:signed-F-wave`. Both constant response columns are included; positivity or a
spectral gap is never used.

### NEW-vs-OLD

OLD LF202--265; NEW LF244--330. NEW adds the four step headings and the explicit
coefficient inequalities leading from $8K(1+K)^2+1$ to $9(1+K)^3$ and
$\sqrt{8^2+9^2}<13$. The mathematical content is unchanged and correct.

- Lost steps/qualifiers: none identified.
- Pre-existing concerns: the compact-conjugation continuity and the
  variation-of-constants Fubini identity are referred to upstream arguments; I
  reconstructed both explicitly above. No uniform growing-radius or source/noise
  limit is claimed, and no new stochastic solution is introduced.

---

## AUDIT dispositions

- `L:signed-limiting-multiplier`: Old/New stmt LF11--19 unchanged; proofs
  LF21--37 (old) vs LF21--41 (new). PRESERVED; new framing JUSTIFIED.
- `P:signed-closed-form`: stmt old LF45--63 / new LF49--67 unchanged; proofs
  LF65--115 vs LF69--130. PRESERVED; step labels JUSTIFIED.
- `L:signed-spectral-wave`: stmt old LF122--134 / new LF137--149 unchanged; proofs
  LF136--184 vs LF151--226. PRESERVED; isometry/conjugation and zero-rate remarks
  JUSTIFIED.
- `P:signed-physical-wave`: stmt old LF190--200 / new LF232--242 unchanged; proofs
  LF202--265 vs LF244--330. PRESERVED; coefficient bookkeeping JUSTIFIED.

No byte-retention claim is used as evidence in any disposition; all listed constants
were re-derived from the displayed estimates.

## Findings and limits

- The NEW revision is purely additive/expository over OLD within the four assigned
  proofs: no displayed equation, hypothesis, constant, normalization, or qualifying
  condition changed.
- Sign generality is preserved: the closed-form proof bounds $v_V$ in absolute value
  and never imports positivity; the spectral wave obtains $\beta\le0$ from
  dilation/translation of a bump off $\operatorname{supp}m_R$, not from $V\ge0$.
- Both constant columns remain part of the physical phase, and the proof of
  `P:signed-physical-wave` handles the non-dense embedding $E\subsetneq F$ separately
  via variation of constants.
- The quarter-power comparison is reconstructed via resolvent order and the scalar
  square-root integral, extended from the core $H^1$ to the domains by closedness;
  no arbitrary noncommuting-power order rule is assumed.
- The limiting multiplier, spectral matrix entries (positive, zero, negative),
  strong continuity, graph-level extensions, compact-operator conjugation, and the
  final constants
  $8(1+K)^2(1+t)e^{\lambda t}$ and
  $16(1+K)^4(1+t)^3e^{\lambda t}$ are all reproduced above.
- External Teschl imports (`Thm.~2.14`, `Thm.~3.1`, `Thm.~3.2`, `Thm.~3.6`,
  `(3.51)--(3.53)`, `(3.18)--(3.21)`) are treated as stated inputs, with their
  application hypotheses checked on the closed shifted form and spectrum; no primary
  PDF/image/render verification is performed or claimed.
- Fixed radius and control-dependent constants are preserved; no uniform
  growing-radius family, source/noise limit, ground state, or stochastic solution
  claim is introduced in these four proofs.
- No new rewrite defect, lost step, or lost qualifier was identified. Remaining
  compactness of the presented arguments are pre-existing presentational reliance on
  unassigned upstream lemmas and imported literature statements, not induced by the
  NEW revision.
