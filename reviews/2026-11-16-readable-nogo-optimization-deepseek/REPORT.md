# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

The four assigned No-go proofs (P:nogo-23, P:nogo-28, P:nogo-29, P:nogo-33) were read in full in both the OLD and NEW scientific views. All concrete deductions were reconstructed independently, including the unchanged proofs. The only differences are inside-proof administrative step headings and two short roadmap sentences in the NEW proofs of P:nogo-28 and P:nogo-33; every displayed formula, every arithmetic witness, every constant, every scope qualifier and every terminal “This proves No-go …” reference is preserved. No assigned mathematical step is dropped, weakened, strengthened, or re-ordered. Named UNASSIGNED upstream statements are invoked only where their application hypotheses are checked.

---

## P:nogo-23

- **Old reading:** COMPLETE (OLD statement LF 19–30, proof LF 32–47, original LF 32–47).
- **New reading:** COMPLETE (NEW statement LF 19–30, proof LF 32–47, original LF 32–47).
- **Argument preservation:** PRESERVED. The statement and proof are byte-identical between OLD and NEW; nothing was added, deleted, or reworded.
- **New explanations:** JUSTIFIED (vacuous — no new explanatory prose was introduced).
- **Public reconstruction:** COMPLETE.

### Original-step coverage

**Statement.** Let \(g_1,\dots,g_n\) be i.i.d. standard real Gaussians, \(A_i=e_i^{\mathsf T}\) the coordinate row matrices (so each \(A_i\) is \(1\times n\)), and \(X=\sum_i g_iA_i\). Define
\[
V_{\mathrm{in}}=\sum_i A_i^*A_i,\qquad V_{\mathrm{out}}=\sum_i A_iA_i^*.
\]

**Step 1 — the singular value.** \(X=\sum_i g_i e_i^{\mathsf T}=(g_1,\dots,g_n)\) is a single \(1\times n\) row. Its only positive singular value is the square root of
\[
XX^*=\sum_i g_i^2,
\]
so the unique nonzero singular value is \((\sum_i g_i^2)^{1/2}\). Hence
\[
\|X\|_{S_4}^4=\sigma_{\max}(X)^4=\left(\sum_i g_i^2\right)^2.
\]
Equivalently \(\|X\|_{S_4}^4=\operatorname{Tr}((X^*X)^2)\); the two-dimensional conventions agree because \(X^*X\) has the single nonzero eigenvalue \(\sum_i g_i^2,\) and all Schatten norms of rank-one rectangular operators coincide with the scalar power of that eigenvalue.

**Step 2 — moment.** Using \(\E g_i^4=3\) and \(\E g_i^2g_j^2=1\) for \(i\neq j\) (independence + unit variance):
\[
\E\left(\sum_i g_i^2\right)^2
=\sum_i \E g_i^4+\sum_{i\neq j}\E g_i^2\E g_j^2
=3n+n(n-1)=n^2+2n=n(n+2).
\]
That is \(\E\|X\|_{S_4}^4=n(n+2)\).

**Step 3 — variance operators.** Since \(A_i=e_i^{\mathsf T}\),
\[
V_{\mathrm{in}}=\sum_i e_ie_i^{\mathsf T}=I_n,\qquad
V_{\mathrm{out}}=\sum_i e_i^{\mathsf T}e_i=\sum_i 1=n
\]
(the latter acting on a one-dimensional target space, since \(X\) is a \(1\times n\) row). Therefore \(\operatorname{Tr}V_{\mathrm{in}}^2=\operatorname{Tr}I_n=n\).

**Step 4 — the refuted one-sided bound.** The proposed input-only bound \(9\operatorname{Tr}V_{\mathrm{in}}^2\) equals \(9n\). At \(n=16\):
\[
\E\|X\|_{S_4}^4=16\cdot 18=288>144=9\cdot 16=9\operatorname{Tr}V_{\mathrm{in}}^2.
\]
The ratio
\[
\frac{\E\|X\|_{S_4}^4}{\operatorname{Tr}V_{\mathrm{in}}^2}
=\frac{n(n+2)}{n}=n+2
\]
is unbounded in \(n\), so no \(n\)-independent constant bounds the left side by \(\operatorname{Tr}V_{\mathrm{in}}^2\) alone over this row-matrix family.

**Step 5 — transposed family.** Transposing replaces \(A_i\) by \(e_i\) (an \(n\times 1\) column family). The singular value \((\sum_i g_i^2)^{1/2}\) is unchanged because \(X^*X\) and \(XX^*\) have the same nonzero spectrum, so \(\E\|X\|_{S_4}^4\) is unchanged while \(V_{\mathrm{in}}=n\) and \(V_{\mathrm{out}}=I_n\) are exchanged. This gives the analogous output-only failure.

**Step 6 — scope.** The proof’s scope paragraph (unchanged) states this is a finite-matrix counterexample, not a counterexample to a wave estimate; Proposition \(P_{\mathrm{finite\text{-}gaussian\text{-}matrix}}\) retains both variances. I verified the quoted numbers against the unassigned context (integrated_compact_gaussian, \(P_{\!f\!g\!m}\)). For \(p=4, m=2\), the average bound is
\[
(p-1)^{p/2}\frac{\operatorname{Tr}V_{\mathrm{out}}^2+\operatorname{Tr}V_{\mathrm{in}}^2}{2}
=9\cdot\frac{256+16}{2}=1224,
\]
and the maximum bound is
\[
9\max(\operatorname{Tr}V_{\mathrm{out}}^2,\operatorname{Tr}V_{\mathrm{in}}^2)
=9\cdot 256=2304,
\]
so “fourth powers \(1224\) and \(2304\)” are correct and neither is contradicted by \(288\).

No lost steps or qualifiers; no pre-existing or new concern detected.

---

## P:nogo-28

- **Old reading:** COMPLETE (OLD statement LF 83–90, proof LF 92–118, original LF 92–118).
- **New reading:** COMPLETE (NEW statement LF 83–90, proof LF 92–130, original LF 92–130).
- **Argument preservation:** PRESERVED. The NEW proof adds one roadmap sentence and two `\medskip\noindent\textit{Step 1./Step 2.}` headings only; every mathematical sentence and every displayed formula is byte-identical to OLD.
- **New explanations:** JUSTIFIED. The added sentence “We compute the ratio of the two comparison formulas with the kinetic penalty retained …” accurately describes that the \((2\zeta)\) penalty factor is retained in the ratio (here evaluated at \(\zeta=1\)), and the two step headings (“exact logarithmic ratio”, “sign at the admissible parameter point”) accurately partition the existing deduction.
- **Public reconstruction:** COMPLETE.

### Original-step coverage

**New prose (Step 1 heading).** The comparison is between \(2^mF_a(\mathcal E_1^{\mathcal O})\) and \(U_2\), i.e. the kinetic-penalty-\(\zeta=1\) energy against the intrinsic ceiling.

**Step 1a — positivity/finiteness.** Proposition \(P_{\mathrm{raw\text{-}occupation\text{-}energy}}\) (UNASSIGNED) is cited for finiteness and positivity of the energies. Its application is legitimate: \(\Gamma\neq 0\) (“every nonzero admissible covariance”), the spatial exponent \(\alpha=5/4\in(0,2)\) (needed for the strict concavity sign and \(z>0\) in the scalar map \(F_b\)), temporal exponent \(a=\alpha_0=1/2\in(0,1)\), and the threshold \(\alpha+a=7/4<2\). Under these hypotheses \(P_{\mathrm{raw\text{-}occupation\text{-}energy}}\) gives \(\mathcal E_\zeta^{\mathcal O}>0\) finite, so \(F_a(\mathcal E_1^{\mathcal O})\) and \(F_0(\mathcal E_1^{\mathcal O})\) are defined at a positive argument; the \(0\le b<q/2\) condition for \(F_b\) holds since \(a=1/2<11/8=q/2\).

**Step 1b — logarithmic ratio.** Define
\[
\Delta=\frac12\left[q\log q+(q-2a)\log(q-2a)\right]-(q-a)\log(q-a).
\]
Using the definition
\[
F_b(z)=k\left[\frac{(q-2b)^{(q-2b)/2}}{8(q-b)^{q-b}}
\left(\frac{2z}{2-\alpha}\right)^{(2-\alpha)/2}\right]^{1/k},
\]
taking logarithms and subtracting the \(b=0\) case from \(b=a\) cancels the \((\frac{2z}{2-\alpha})\), the \(8\), and the outer factors \(k\):
\[
\log\frac{F_a(z)}{F_0(z)}
=\frac1k\left[
\frac{q}{2}\log q+\frac{q-2a}{2}\log(q-2a)-(q-a)\log(q-a)
\right]
=\frac{\Delta}{k}.
\]

**Step 1c — ceiling identity and ratio.** Theorem \(T_{\mathrm{intrinsic\text{-}occupation\text{-}ceiling}}\) (UNASSIGNED) states
\[
U_2=2^m(2\zeta)^{\alpha/(2k)}F_0(\mathcal E_\zeta^{\mathcal O})
\]
(valid for every \(\zeta>0\)). Hence
\[
\frac{2^mF_a(\mathcal E_\zeta^{\mathcal O})}{U_2}
=\frac{F_a(\mathcal E_\zeta^{\mathcal O})}{(2\zeta)^{\alpha/(2k)}F_0(\mathcal E_\zeta^{\mathcal O})}
=\exp\left\{\frac{\Delta-(\alpha/2)\log(2\zeta)}{k}\right\}.
\]

**Step 2 — sign at \(\zeta=1\).** With \(q=11/4\), \(k=7/4\), \(\alpha=5/4\), \(a=1/2\),
\[
\Delta=\frac12\left[\frac{11}{4}\log\frac{11}{4}
+\frac74\log\frac74\right]
-\frac94\log\frac94.
\]
Multiplying \(8\{\Delta-(\alpha/2)\log 2\}\) term by term:
\[
8\Delta=11\log\frac{11}{4}+7\log\frac74-18\log\frac94,\qquad
8\cdot\frac{\alpha}{2}\log2=\frac{8\cdot 5/4}{2}\log2=5\log2.
\]
So, combining the logarithms,
\[
8\{\Delta-(\alpha/2)\log2\}
=11\log\frac{11}{4}+7\log\frac74-18\log\frac94-5\log2
=\log\frac{11^{11}\,7^7}{2^5\,9^{18}},
\]
because \(11\log(11/4)+7\log(7/4)-18\log(9/4)\) produces
\[
\frac{11^{11}7^7\cdot 4^{18}}{4^{11}4^{7}9^{18}}
=\frac{11^{11}7^7}{9^{18}},
\]
and \(-5\log2\) contributes the remaining \(2^{-5}\).

**Step 2 — numerical verification.** I verified all the powers:
\[
11^{11}=285\,311\,670\,611,\quad 7^7=823\,543,
\]
\[
11^{11}7^7=234\,966\,429\,149\,994\,773.
\]
Also
\[
9^{18}=150\,094\,635\,296\,999\,121,\quad
2^{5}\cdot 9^{18}=4\,803\,028\,329\,503\,971\,872.
\]
Indeed
\[
234\,966\,429\,149\,994\,773<4\,803\,028\,329\,503\,971\,872,
\]
so the logarithm is negative, \(\Delta-(\alpha/2)\log2<0\), and with \(k=7/4>0\),
\[
\frac{2^mF_a(\mathcal E_1^{\mathcal O})}{U_2}<1.
\]

**Conclusion.** \(2^mF_a(\mathcal E_1^{\mathcal O})<U_2\), i.e. the reverse comparison is not valid throughout the admissible class. The terminal reference “This proves No-go~\ref{P:nogo-28}” correctly closes the proof.

**Scope (unchanged and verified as a reading).** The paragraph states the result refutes an ordering of two computed quantities, not an inequality for the actual moment constant, and does not decide whether \(C_2\) lies below the smaller comparison value; at \(\zeta=1/2\) the logarithmic difference is \(\Delta/k>0\), which is the strict convexity statement. I checked the convexity claim: with \(x=q\), \(y=q-2a\), the midpoint is \((x+y)/2=q-a\), and strict convexity of \(x\log x\) (second derivative \(1/x>0\) on positives, and \(a>0\) makes \(x\neq y\)) gives
\[
(q-a)\log(q-a)<\frac{q\log q+(q-2a)\log(q-2a)}{2},
\]
so \(\Delta>0\). This supports, not disturbs, the scope text.

No lost steps or qualifiers. No new concern; the added prose does not alter any hypothesis, normalization, constant, or limiting order.

---

## P:nogo-29

- **Old reading:** COMPLETE (OLD statement LF 146–155, proof LF 157–177, original LF 157–177).
- **New reading:** COMPLETE (NEW statement LF 158–167, proof LF 169–189, original LF 169–189). The line shifts are purely because P:nogo-28’s proof grew upstream; the statement and proof text are byte-identical.
- **Argument preservation:** PRESERVED. No change at all to statement or proof.
- **New explanations:** JUSTIFIED (vacuous — none added).
- **Public reconstruction:** COMPLETE.

### Original-step coverage

**Setting (statement).** The finite Gram optimization is
\[
F(\Phi)=2\sum_i\ell_i\sqrt{(\langle\Phi,k_i\rangle-b_i)_+}-\frac12\|\Phi\|^2,
\qquad \ell_i>0,\ b_i\ge0,
\]
with nonnegative Gram entries \(C_{ij}=\langle k_i,k_j\rangle\). Three alleged simplifications are refuted.

**Item 1 — the empty active set.** With one unit vector (so \(C=1\)), \(\ell=1/10\), \(b=4\), the nonempty active-set dual (from the unassigned definition \(D_A^C(w)=\sum_i\ell_i^2/w_i-\sum_i b_iw_i+\tfrac12\sum_{i,j}w_iC_{ij}w_j\)) is
\[
D(w)=\frac{\ell^2}{w}-bw+\frac12 w^2
=\frac{1}{100w}-4w+\frac{w^2}{2}.
\]
At \(w=4\):
\[
D(4)=\frac1{400}-16+8=\frac{1-3200}{400}=-\frac{3199}{400}<0.
\]
Thus \(\inf_{w>0}D(w)\le-3199/400<0\). On the primal side, \(F(0)=0\) because \((\langle0,k\rangle-4)_+=( -4)_+=0\), so the primal supremum is at least \(0\). Therefore dropping the empty value from the maximum of dual infima wrongly replaces a nonnegative primal supremum by a negative maximum; the convention \(d_\varnothing=0\) is exactly what restores equality with \(\mathcal S(C)\).

**Item 2 — nonconcavity.** With \(H=\mathbb R\), \(k=\ell=b=1\),
\[
F(x)=2\sqrt{(x-1)_+}-\frac{x^2}{2}.
\]
Directly,
\[
F(0)=0,\qquad F(2)=2\sqrt{(2-1)_+}-\frac42=2-2=0,
\qquad F(1)=2\cdot0-\frac12=-\frac12.
\]
Concavity at the midpoint would require
\[
F\!\left(\frac{0+2}{2}\right)\ge\frac{F(0)+F(2)}{2}=0,
\]
but \(F(1)=-1/2<0\). Violation of midpoint concavity proves \(F\) is not concave.

**Item 3 — entrywise vs. Loewner order.** Take
\[
C=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
D=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
\]
Entrywise, \(0\le C_{ij}\le D_{ij}\) holds (\(1\le1\) on the diagonal, \(0\le1/2\) off it). Both are PSD: the eigenvalues of \(C\) are \(1,1\); the eigenvalues of \(D\) are \(1\pm1/2\), i.e. \(3/2\) and \(1/2\). But
\[
D-C=\begin{pmatrix}0&1/2\\1/2&0\end{pmatrix}
\]
has eigenvalues \(\pm1/2\) (its characteristic polynomial is \(\lambda^2-1/4\)), so \(D-C\) is not positive semidefinite. Entrywise domination does not give Loewner domination.

**Scope (unchanged).** The paragraph says these are the checks in Remark \(R_{\mathrm{gram\text{-}controls}}\) and that entrywise comparison still works in Proposition \(P_{\mathrm{gram\text{-}entrywise\text{-}comparison}}\) for nonnegative weights \(w_i\): for \(w_i\ge0\),
\[
\sum_{i,j}w_i(D_{ij}-C_{ij})w_j\ge0
\]
whenever \(D_{ij}-C_{ij}\ge0\) entrywise. That is the restricted cone on which the entrywise comparison is asserted; no all-vector Loewner order claim is made.

No lost steps; no pre-existing or new concern in the three computations themselves.

---

## P:nogo-33

- **Old reading:** COMPLETE (OLD statement LF 203–220, proof LF 222–261, original LF 222–261).
- **New reading:** COMPLETE (NEW statement LF 215–232, proof LF 234–289, original LF 234–289).
- **Argument preservation:** PRESERVED. The NEW proof adds one roadmap sentence and three `Step 1./Step 2./Step 3.` headings; all mathematical content is byte-identical to OLD.
- **New explanations:** JUSTIFIED. The roadmap sentence (“free-phase contractivity, the unweighted series-factor identity, and the stronger factorial denominator”) correctly names the three proofs, and the step headings correctly label each deduction.
- **Public reconstruction:** COMPLETE.

### Original-step coverage

**Statement.** Three reviewer assertions are declared false:
1. \(S_0(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix}\) is a contraction in the Euclidean norm for every \(t\ge0\).
2. For \(x>0\), \(n\ge1\), \(0<\vartheta<1\), the term \(x^n/(n!)^{\vartheta}\) equals \(A_nB_n\) with \(A_n=(2x^{1/\vartheta})^n/n!\), \(B_n=2^{-\vartheta n/(1-\vartheta)}\).
3. The denominator \(k!\,k^{(2-\alpha)k}\) may always be replaced by the larger denominator \((k!)^3\) in the coefficient bound of Proposition \(P_{\mathrm{low\text{-}\alpha\text{-}upper}}\).

**Step 1 — free-phase contractivity refuted.** First, the \(2\times2\) matrix: \((0,1)^{\mathsf T}\) has Euclidean norm \(1\), and
\[
S_0(t)\begin{pmatrix}0\\1\end{pmatrix}
=\begin{pmatrix}t\\1\end{pmatrix},
\qquad \left\|\begin{pmatrix}t\\1\end{pmatrix}\right\|_2=\sqrt{1+t^2}>1
\]
for \(t>0\). So the matrix fails to be a contraction for all \(t\ge0\).

**Step 1 — transfer to the wave phase.** Using the inhomogeneous Sobolev norm \(E=H^{1/2}\times H^{-1/2}\) and \(J_0=\operatorname{diag}(\Lambda^{1/2},\Lambda^{-1/2})\), \(\Lambda=(1-\Delta)^{1/2}\), the Fourier-side conjugation is by \(D=\operatorname{diag}(\langle\xi\rangle^{1/2},\langle\xi\rangle^{-1/2})\) where \(\langle\xi\rangle=\sqrt{1+r^2}\), \(r=|\xi|\). The free-phase symbol (from the unassigned \((E_{\mathrm{variance\text{-}free\text{-}matrix}})\)) is
\[
S(t,\xi)=\begin{pmatrix}\cos(tr)&\sin(tr)/r\\ -r\sin(tr)&\cos(tr)\end{pmatrix}.
\]
Computing \(DS(t,\xi)D^{-1}\) explicitly:
\[
\begin{pmatrix}
\langle\xi\rangle^{1/2}&0\\0&\langle\xi\rangle^{-1/2}
\end{pmatrix}
\begin{pmatrix}
c&s/r\\-rs&c
\end{pmatrix}
\begin{pmatrix}
\langle\xi\rangle^{-1/2}&0\\0&\langle\xi\rangle^{1/2}
\end{pmatrix}
=
\begin{pmatrix}
c&\langle\xi\rangle s/r\\
-r s/\langle\xi\rangle&c
\end{pmatrix},
\]
with \(c=\cos(tr)\), \(s=\sin(tr)\). This is exactly the displayed symbol. As \(r\downarrow0\): \(\langle\xi\rangle\to1\), \(\sin(tr)/r\to t\), and \(-r\sin(tr)/\langle\xi\rangle\to0\), so the symbol tends to
\[
\begin{pmatrix}1&t\\0&1\end{pmatrix}=S_0(t).
\]
The symbol is continuous at \(\xi=0\) (the sine quotient and \(r\sin(tr)\) have removable continuous values). Placing normalized Fourier bumps \(\psi_\varepsilon\) with support in balls \(|\xi|<\varepsilon\downarrow0\) into the second coordinate of \(J_0z\) (input norm \(1\), since \(J_0\) is unitary onto \(L^2\times L^2\)) gives, by continuity at zero,
\[
\lim_{\varepsilon\downarrow0}\|M(t,\cdot)\psi_\varepsilon-S_0(t)\psi_\varepsilon\|=0.
\]
But \(S_0(t)(0,\psi)=(t\psi,\psi)\), whose \(L^2\times L^2\) norm is \(\sqrt{1+t^2}\|\psi\|_2\). Hence the image norms tend to \(\sqrt{1+t^2}>1\), so \(S(t)\) is not a contraction on \(E\). The exponent explanation (unchanged) is correct: replacing the inhomogeneous weight \(\langle\xi\rangle\) by the homogeneous \(|\xi|\) would make the conjugated symbol
\[
\begin{pmatrix}\cos(tr)&\sin(tr)\\-\sin(tr)&\cos(tr)\end{pmatrix},
\]
a rotation (hence an isometry), so the zero-frequency non-contraction is specifically an inhomogeneous-norm phenomenon. The valid estimate keeps a free-growth factor.

**Step 2 — series-factor identity refuted.** The correct weighting is
\[
\frac{x^n}{(n!)^{\vartheta}}=A_n^{\vartheta}B_n^{1-\vartheta},
\]
because
\[
A_n^{\vartheta}=\frac{(2x^{1/\vartheta})^{\vartheta n}}{(n!)^{\vartheta}}
=\frac{2^{\vartheta n}x^n}{(n!)^{\vartheta}},\qquad
B_n^{1-\vartheta}=2^{-\vartheta n/(1-\vartheta)\cdot(1-\vartheta)}=2^{-\vartheta n},
\]
so the product is \(2^{\vartheta n-\vartheta n}x^n/(n!)^{\vartheta}=x^n/(n!)^{\vartheta}\). The proposed unweighted product \(A_nB_n\) fails: at \(\vartheta=3/4\), \(n=1\), \(x=1\),
\[
\frac{x^n}{(n!)^{\vartheta}}=\frac1{1^{3/4}}=1,
\]
while
\[
A_1=\frac{(2\cdot 1^{4/3})^1}{1!}=2,\qquad
B_1=2^{-(3/4)\cdot1/(1/4)}=2^{-3}=\frac18,
\]
so \(A_1B_1=2/8=1/4\neq1\). The remark (unchanged) that Hölder applies to the weighted product with conjugate powers is accurate; I cross-checked against the unassigned Proposition \(P_{\mathrm{static\text{-}phase\text{-}all\text{-}orders}}\) proof, whose \(\beta<1\) case applies Hölder to
\[
\left(\frac{(2x^{1/\beta})^n}{n!}\right)^{\beta}
\left(2^{-\beta n/(1-\beta)}\right)^{1-\beta},
\]
matching the corrected identity with \(\beta=\vartheta\).

**Step 3 — factorial denominator refuted.** Choose the permitted spatial-white value \(\alpha=1\) and \(k=3\). Then
\[
k!\,k^{(2-\alpha)k}=6\cdot 3^{(2-1)\cdot 3}=6\cdot 27=162,
\qquad
(k!)^3=6^3=216,
\]
so \(162<216\). Thus \((k!)^3\) is genuinely the larger denominator, and replacing \(162\) by \(216\) would shrink the value of the bound. For \(M>0\), an upper bound of the form \(M/162\) does not imply the stronger upper bound \(M/216\) (indeed \(M/216<M/162\)). The valid factorial weakening is in the opposite, weaker direction:
\[
k!\,k^{(2-\alpha)k}\ \ge\ (k!)^{3-\alpha},
\]
derived in the proof by
\[
k! \le k^k \implies k^{(2-\alpha)k}\ge (k!)^{2-\alpha}\ \text{for }2-\alpha>0,
\]
hence
\[
k!\,k^{(2-\alpha)k}\ge k!(k!)^{2-\alpha}=(k!)^{3-\alpha}.
\]
At the example the right side is \(6^{3-1}=6^2=36\), consistent with \(162\ge36\). This is the “larger value, weaker bound” direction that is legitimately available.

**Scope (unchanged).** The last arithmetic check refutes an inference between numerical bounds; it does not assert that the actual coefficient exceeds \(M/216\). The “What would permit” paragraph (unchanged) states the correct replacements: an invariant norm or restricted state class for contractivity, conjugate Hölder powers for the series, and an additional estimate for a stronger factorial bound — none obtainable by relabeling the exponent in the denominator.

No lost steps or qualifiers. No new concern from the added headings.

---

## Findings and limits

**Preservation.** All four assigned proofs preserve their mathematical argument. P:nogo-23 and P:nogo-29 are byte-identical in both statement and proof. P:nogo-28 and P:nogo-33 add only inside-proof administrative prose (roadmap sentences and `Step n.` headings); every equation, every witness number, every hypothesis qualifier, every scope statement, and every concluding “This proves No-go …” reference is unchanged. I read every unchanged proof fully and checked its mathematics rather than relying on equality of ranges or hashes.

**Reconstruction.** The finite/variational/arithmetic witnesses were each verified independently:
- NG-23: singular value \((\sum_i g_i^2)^{1/2}\); \(\E\|X\|_{S_4}^4=n(n+2)=288\) vs \(9\operatorname{Tr}V_{\mathrm{in}}^2=144\) at \(n=16\); ratio \(n+2\) unbounded; transposition exchanges \(V_{\mathrm{in}}=I_n\) and \(V_{\mathrm{out}}=n\) and preserves singular values; the valid two-variance average/maximum bounds give \(1224\) and \(2304\), both above \(288\).
- NG-28: \(\log(F_a/F_0)=\Delta/k\); \(U_2=2^m(2\zeta)^{\alpha/(2k)}F_0(\mathcal E_\zeta^{\mathcal O})\); the ratio formula; and the exact arithmetic \(11^{11}7^7=234\,966\,429\,149\,994\,773 < 2^59^{18}=4\,803\,028\,329\,503\,971\,872\), giving a negative logarithm at \((\alpha,a,d)=(5/4,1/2,2)\), \(\zeta=1\). Full (not restricted) occupation-class energies are used, and the reverse/one-sided comparison fails without touching the moment inequality.
- NG-29: \(D(4)=-3199/400<0=F(0)\); \(F(0)=F(2)=0\) but \(F(1)=-1/2\) destroys midpoint concavity; \(C=I_2\), \(D=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}\) have entrywise order but \(D-C\) has eigenvalues \(\pm1/2\), so entrywise order is not Loewner order.
- NG-33: \(\|S_0(t)(0,1)\|=\sqrt{1+t^2}>1\); the conjugated symbol \(\begin{pmatrix}\cos(tr)&\langle\xi\rangle\sin(tr)/r\\ -r\sin(tr)/\langle\xi\rangle&\cos(tr)\end{pmatrix}\to S_0(t)\) at \(r=0\), transferring non-contractivity to \(E=H^{1/2}\times H^{-1/2}\) via shrinking Fourier bumps; \(x^n/(n!)^{\vartheta}=A_n^{\vartheta}B_n^{1-\vartheta}\neq A_nB_n\), witnessed at \((3/4,1,1)\) by \(1\neq1/4\); and \(162<216\), so replacing \(k!k^{(2-\alpha)k}\) by \((k!)^3\) would strengthen, not merely validly weaken, the bound, whereas the valid weakening is to \((k!)^{3-\alpha}=36\).

**Limits.** Only the assigned No-go statements/proofs and the supplied UNASSIGNED context were used. Upstream named inputs (\(P_{\mathrm{raw\text{-}occupation\text{-}energy}}\), \(T_{\mathrm{intrinsic\text{-}occupation\text{-}ceiling}}\), \(P_{\mathrm{finite\text{-}gaussian\text{-}matrix}}\), \(P_{\mathrm{static\text{-}phase\text{-}all\text{-}orders}}\), the Gram dual formulas, the wave-variance free matrix) are treated as stated UNASSIGNED context; their own proofs were not assigned or reconstructed here, though their application hypotheses were checked at each cite point. Imported-source bibliographic claims and primary-source theorem/PDF contents were not verified. Neither view contains any dropped hypothesis, changed constant, altered strictness, or narrowed/expanded witness scope relative to its counterpart.

No failure or partial-reconstruction condition was triggered.
