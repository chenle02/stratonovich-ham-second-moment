# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro (deepseek/deepseek-v4-pro)
Verdict: PASS
Confidence: high

Scope note. The five assigned proofs live entirely in the target module
`notes/integrated_symplectic_phase.tex`. I read both whole-file revisions
provided. The baseline modules (cameron mean, constant-phase Young, source
convergence, actual operator driver, raw-block lower, model assumptions) were
used only to check that the target's *consumer uses* of their declarations
respect their stated hypotheses; I did not re-prove those unassigned upstream
proofs, and I do not count reading them as extra assigned reviews.

The rewrite (old `cdde711`, new `a512b15`) changes **no statements** (verified
verbatim for all five), changes **no deductions**, and loses **no qualifier**.
Its additions are: per-proof roadmap sentences, `Step n.` headings, and a small
number of explanatory paragraphs. I checked each added explanatory assertion
against the actual deduction; all are correct (see below). Statements (old
`31–61`, new `31–61`, etc.) are byte-identical in mathematical content.

---

## L:symplectic-free

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: 6 steps, all reconstructible.

**Step 1 — the form on $E = H^{1/2}\times H^{-1/2}$.**
$C_{\rm bal}(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)$ is onto $L^2\times L^2$ and
isometric because $\|u\|^2_{H^{1/2}}+\|v\|^2_{H^{-1/2}}=\|\Lambda^{1/2}u\|^2+\|\Lambda^{-1/2}v\|^2$.
$J_{\rm symp}(q,p)=(p,-q)$ has matrix $\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$,
so $J_{\rm symp}=-\!J_{\rm symp}^{\mathsf T}$ and $J_{\rm symp}^2=-I$; conjugating
by the isometry preserves these. Then $J_E(f,g)=C_{\rm bal}^{-1}(\Lambda^{-1}g,-\Lambda f)=(\Lambda^{-1}g,-\Lambda f)$,
and
$$\omega(z,w)=\langle z,J_Ew\rangle_E=\langle u,\Lambda^{-1}g\rangle_{H^{1/2}}-\langle v,\Lambda f\rangle_{H^{-1/2}}=\langle u,g\rangle_{H^{1/2},H^{-1/2}}-\langle f,v\rangle_{H^{1/2},H^{-1/2}},$$
matching the displayed duality. Correct.

**Step 2 — free-wave invariance.**
The balanced Fourier matrix
$W_t(\xi)=\begin{psmallmatrix}\cos(tk)&\langle\xi\rangle\sin(tk)/k\\ -k\sin(tk)/\langle\xi\rangle&\cos(tk)\end{psmallmatrix}$,
$k=|\xi|$, has determinant $\cos^2+\sin^2=1$; for $2\times2$, $W^{\mathsf T}J_{\rm symp}W=J_{\rm symp}\Leftrightarrow\det W=1$.
At $k=0$, $\langle 0\rangle\sin(tk)/k\to t$ and $-k\sin/\langle\xi\rangle\to0$, giving
$\begin{psmallmatrix}1&t\\0&1\end{psmallmatrix}$; entries are real, even, bounded. So
the Fourier multiplier is symplectic a.e.; $L^2$ Cauchy–Schwarz makes the integration
legitimate and gives $\omega(S_E(t)z,S_E(t)w)=\omega(z,w)$. Correct; no frequency-zero
trace needed.

**Step 3 — force skewness.**
$\|bu\|_{H^{-1/2}}\le\|bu\|_2\le\|b\|_\infty\|u\|_{H^{1/2}}$ (since $\|\cdot\|_{H^{-1/2}}\le\|\cdot\|_2$).
For $L^2$ functions the cancellation $-\int fbu+\int ubf=0$ is absolutely justified,
i.e. $B(b)\in\mathfrak g_J$ w.r.t. $\omega$, not the $E$ inner product.

**Step 4 — Young compact endpoint.**
Each left Young sum $\sum_j(X(t_{j+1})-X(t_j))U_X(t_j,s)$ is compact (compact increments,
bounded $U_X$); operator-norm convergence to $U_X(t,s)-I$ plus closedness of the compact
ideal give $U_X(t,s)-I\in\mathcal K(E)$; then $S_E(t)U_X(t,s)S_E(-s)-S_E(t-s)=S_E(t)(U_X-I)S_E(-s)$
is compact. The application of `P:constant-young-linear` on $\mathcal L(E)$ is legitimate:
that proposition's proof uses only completeness and norm-one multiplication, dimension-free
(its statement is on $\mathcal B(F)$ but the method transfers verbatim).

**Step 5 — compact-perturbation norm bound.**
Translations $\tau_y$ are $E$-isometries commuting with $S_E(h)$. The translated pairing
$\langle\tau_yz,w\rangle_E$ is a Fourier transform of an $L^1$ function (Bessel-weighted
$\widehat u\,\widehat f\langle\xi\rangle$ and $\widehat v\,\widehat g\langle\xi\rangle^{-1}$
are $L^1$ by weighted CS), so $\langle\tau_y z,w\rangle\to0$; hence $\tau_yz\rightharpoonup0$.
For compact $K$, $\|K\tau_yz\|\to0$ (weak$\to$norm on compact maps). For unit $z$,
$\|S_E(h)+K\|\ge\liminf\|(S_E(h)+K)\tau_yz\|\ge\|S_E(h)z\|$, then sup over $z$:
$\|S_E(h)+K\|\ge\|S_E(h)\|$. Velocity reversal $\mathcal R(u,v)=(u,-v)$ gives
$S_E(-h)=\mathcal R S_E(h)\mathcal R$; the group law yields
$1\le\|S_E(-h)\|\|S_E(h)\|=\|S_E(h)\|^2$. Correct.

**Step 6 — finite products.**
$P_j-S_E(\ell_j)=S_E(\ell_j)(U_{X_j}(\ell_j,0)-I)$ is compact; telescoping
$P_N\cdots P_0-S_E(\sum\ell_j)$ is a finite sum of bounded–compact–bounded products. Only
free factors are combined by the group law; zero length gives $P_j=I$. Correct.

- Argument preservation: PRESERVED

The new proof *adds* in Step 3 (its Step 3, compact-perturbation bound):
"Since translations commute with the free group and preserve the norm,
$\|S_E(h)\tau_yz\|=\|S_E(h)z\|$. … The reverse triangle inequality therefore gives the
second inequality in the display for each fixed unit vector, before the supremum over
vectors is taken." This is a clarification of the second inequality in Step 5 above:
$\|(S_E(h)+K)\tau_yz\|\ge\|S_E(h)\tau_yz\|-\|K\tau_yz\|=\|S_E(h)z\|-\|K\tau_yz\|$,
so $\liminf\ge\|S_E(h)z\|$. The new sentence correctly supplies exactly the missing
justification. No step is reordered or weakened.

- New explanations: JUSTIFIED (the only new explanatory content is the reverse-triangle-inequality sentence and the Step-1..4 roadmap, both faithful).
- Lost steps/qualifiers: none identified within this read (all "No $L^2$ pairing…",
  "No rough generator derivative…", "no noisy factors are commuted", "no uniform compact
  approximation" qualifiers retained verbatim).

---

## L:symplectic-source-mean

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: 3 steps.

**Step 1 — Bochner mean and convergence.**
Since $Z=W(\Phi)$ is a *scalar* Gaussian, $\|ZM\|_{C^\theta}=|Z|\|M\|_{C^\theta}$ pointwise, so
$\mathbb E\|ZM\|_{C^\theta}\le\|\Phi\|_{H_W}\|M\|_{L^2C^\theta}$, giving Bochner integrability in the
$C^\theta$ path space. Hence
$$\|D_\Phi^\rho-D_\Phi\|_{C^\theta}=\|\mathbb E[Z(M^\rho-M)]\|_{C^\theta}\le\|\Phi\|_{H_W}\|M^\rho-M\|_{L^2C^\theta}\to0,$$
which is `E:symplectic-mean-convergence`. The uniform source bound has the same form. Correct.

**Step 2 — the deterministic coefficient.**
From `L:source-retaining-isometry` there is an isometry $j_{\rm src}:H_W\to\mathcal G$ and isonormal
$\mathcal I$ with $\mathcal I(j_{\rm src}h)=W(h)$ in $L^2$; the point field is
$Y^\rho(t,x)=\mathcal I(v_{\rho;t,x})$. Therefore
$$h_\Phi^\rho(t,x)=\mathbb E[W(\Phi)Y^\rho(t,x)]=\mathbb E[\mathcal I(j_{\rm src}\Phi)\mathcal I(v_{\rho;t,x})]=\langle j_{\rm src}\Phi,v_{\rho;t,x}\rangle_{\mathcal G},$$
which has the claimed continuous-time, smooth-space regularity (used only under
`L:source-pointfield-regularity`, whose hypotheses — fixed $\rho>0$ — are respected). After $m_R$
multiplication: one compact support, bounded derivatives. Correct.

**Step 3 — primitive identification.**
For Schwartz states, the row of $\int_0^t S_E(-r)B(m_Rh_\Phi^\rho(r))S_E(r)dr$ is the integral of
$h_\Phi^\rho$ against the masked source wave product; Fubini is valid by
$\mathbb E|ZY^\rho|\le\|\Phi\|\sqrt{\mathbb E|Y^\rho|^2}$ and bounded positive-width point variance;
indicator/test approximation extends to completed rows; countable dense states + rational times +
continuity identify the operator path; the uniformly bounded integrand gives the Lipschitz bound, and
$b^\rho=m_R(cY^\rho+h_\Phi^\rho)$. The new statement that "the combined source is generally
noncentered and the mask occurs once" matches the fact that $h^\rho$ is a mean (nonzero in general)
and $m_R$ multiplies once, outside. Correct.

- Argument preservation: PRESERVED (new text only reorders the same sentences into Step 1–3 and adds a
  one-sentence roadmap; the final "noncentered/mask once" sentence is kept verbatim).
- New explanations: JUSTIFIED (roadmap accurately summarizes Steps 1–3).
- Lost steps/qualifiers: none. Consumer-hypothesis check: `L:source-retaining-isometry`,
  `L:source-pointfield-regularity`, `P:source-ordinary-response` are used at a fixed positive $\rho$,
  exactly as their statements require.

---

## P:symplectic-source

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: 4 steps.

**Step 1 — coefficient regularity event.** Intersection of (a) the source-coefficient regularity event
and (b) the event identifying its first primitive with the ordinary primitive for all times/states is a
finite intersection of probability-one sets (the all-times/states event is established in the source
baseline by dense states + rational times + continuity). On it $b^\rho$ has common compact support,
sup-norm continuity, uniform boundedness, so $C_b(r)=S_E(-r)B(b^\rho(r))S_E(r)$ is uniformly bounded and
strongly continuous.

**Step 2 — skewness of the conjugate.** The old text cites `L:symplectic-free` directly for
$\omega(C_b z,w)+\omega(z,C_b w)=0$. The new text adds the explicit transfer:
$$\omega(C_bz,w)=\omega(S_E(-r)B(b)S_E(r)z,w)=\omega(B(b)S_E(r)z,S_E(r)w),$$
$$\omega(z,C_bw)=\omega(S_E(r)z,B(b)S_E(r)w),$$
using $\omega(S_E(-r)x,w)=\omega(x,S_E(r)w)$ (free invariance) twice; the sum is the force-skewness
identity with arguments $S_E(r)z,S_E(r)w$, hence zero. The added sentence "This uses the symplectic
form, not skew-adjointness in the phase Hilbert norm" is correct: $B(b)$ is symmetric (it is the
force $(0,bu)$ with symmetric multiplication contribution) while the symplectic requirement is
$B^*J_E+J_EB=0$, the $J_E$-twisted antisymmetry.

**Step 3 — Young equation = ordinary equation.** Replacing each operator-path increment in a Young sum
by its statewise integral, with error bounded by (uniform coefficient bound)$\times$(uniform continuity
of $U$), makes $U(t,s)e=e+\int_s^tC_b(r)U(r,s)e\,dr$; by the statewise difference quotient the
trajectory is $C^1$ with derivative $C_b(t)U(t,s)e$.

**Step 4 — zero derivative of $\omega$.** Differentiating
$\omega(U(t,s)e,U(t,s)f)=\langle Ue,J_EUf\rangle_E$ gives $\omega(C_bUe,Uf)+\omega(Ue,C_bUf)=0$, so the form
is constant; free conjugation gives
$P_{D^\rho}^*J_EP_{D^\rho}=S_E(s)^*U^*S_E(t)^*J_ES_E(t)US_E(-s)=J_E$ (using free invariance twice). Correct;
"same path set for all states and time pairs" is legitimate because the bounded ordinary evolution is
defined simultaneously on all $E$.

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (the conjugation transfer is a correct derivation of the previously
  one-line citation; roadmap and Step headings are neutral).
- Lost steps/qualifiers: none ("No uncountable intersection…" retained). Pre-existing observation: the
  differentiation in Step 4 compresses a product-rule argument into one sentence; it is standard and
  unchanged from old, not a rewrite defect.

---

## P:symplectic-raw

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: 4 steps.

**Step 1 — the closed constraint $\mathfrak g_J=\{A:A^*J_E+J_EA=0\}$.**
$H_{j,R}$ in `E:driver-covariance-coefficient` is real smooth. Free conservation gives
$S_E(-r)^*J_E=J_ES_E(r)$ and $J_ES_E(-r)=S_E(r)^*J_E$; then for $C=S_E(-r)B(H_{j,R})S_E(r)$:
$$C^*J_E+J_EC=S_E(r)^*[B^*J_E+J_EB]S_E(r)=0,$$
since `L:symplectic-free` gives $B^*J_E+J_EB=0$. Testing the statewise integral in
`E:driver-coefficient-operator` against two states gives $A_j(0,t)\in\mathfrak g_J$; the finite real sums in
`E:driver-path-convergence` obey it; the map $A\mapsto A^*J_E+J_EA$ is bounded ($\le2\|A\|$), so the
$L^2C^\theta$ limit $M$ is in $\mathfrak g_J$ at all times on one path set. Correct.

**Step 2 — the combined driver.** $\mathbb E\|W(\Phi)M\|_{C^\theta}\le\|\Phi\|_{H_W}\|M\|_{L^2C^\theta}<\infty$
($W(\Phi)$ scalar), so the Bochner expectation exists and bounded real linear maps commute with it:
$D_\Phi(t)^*J_E+J_ED_\Phi(t)=\mathbb E[Z(M(t)^*J_E+J_EM(t))]=0$. Hence $D=cM+D_\Phi$ starts at zero and is a
$C^\theta$ path in $\mathfrak g_J$ on that path set. Correct; no complex coefficients used.

**Step 3 — conservation.**
Fix $s$, $V(r)=U_D(r,s)$. Young remainder gives
$V(v)-V(u)=D_{u,v}V(u)+R_{u,v}$, $\|R_{u,v}\|\le C|v-u|^{2\theta}$. Expanding
$(V(u)+D_{u,v}V(u)+R)^*J_E(V(u)+D_{u,v}V(u)+R)-V(u)^*J_EV(u)$:
the two linear-in-$D_{u,v}$ terms combine into
$V(u)^*(D_{u,v}^*J_E+J_ED_{u,v})V(u)=0$ (driver constraint). All remaining terms are
$V^*JR$, $R^*JV$ (order $2\theta$), $(D_{u,v}V)^*J(D_{u,v}V)$ (two increments, order $2\theta$), the
mixed $(D_{u,v}V)^*JR$, $R^*J(D_{u,v}V)$ (order $3\theta\le2\theta$), and $R^*JR$ (order $4\theta\le2\theta$);
each is $O(|v-u|^{2\theta})$ since $[D]_\theta$ and $\sup\|V\|$ are finite. Summing over a partition gives
$C(t-s)\,\mathrm{mesh}^{2\theta-1}\to0$, so $V(t)^*J_EV(t)=J_E$. Free conjugation then gives
$P_D^*J_EP_D=J_E$ (two uses of $S_E(\pm t)^*J_ES_E(\pm t)=J_E$), and
$1=\|J_E\|\le\|P_D\|^2$ gives the norm bound `E:symplectic-raw-conservation`. Correct.

The new explanatory paragraph ("In the increment of $V^*J_EV$, the two terms linear in $D_{u,v}$ cancel
by the driver constraint. Every remaining term contains either a Young remainder of order $2\theta$ or two
increments of order $\theta$.") is exactly the enumeration above; justified.

**Step 4 — invertibility, $c=0$, fixed-$\delta$ instance.** Invertibility from local Young Neumann pieces +
finite products + free inverse (per `P:constant-young-linear`), not from infinite-dimensional conservation
alone; for $c=0$ the path and argument are deterministic; zero covariance gives the free flow directly;
the fixed-$\delta$ reference $W\circ T_{\delta,0}$, $R=\delta^{-1}+2$, $T=\delta^{-1}$, $c=g_\delta$, $\Phi=0$
is an instance claim with **no** uniform-radius conclusion. Correct.

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (roadmap; Step headings; the remainder-term enumeration in Step 3 is a correct
  classification with the necessary $|v-u|^{3\theta},|v-u|^{4\theta}\le|v-u|^{2\theta}$ bounds for
  $|v-u|\le1$).
- Lost steps/qualifiers: none ("No operator-norm derivative of the free group is taken", "Complex Gaussian
  coefficients are not used", "it is not inferred from conservation in infinite dimension", "No
  uniform-radius or uniform bound…" all retained).

---

## P:symplectic-block-mean

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: 4 steps.

**Step 1 — fast control and completed mean path.** The pullback `E:raw-block-pullback` has covariance factor
$\delta^{a-2}\delta^2\delta^{-a}=1$, so it respects nulls and extends isometrically fast$\to$slow; its adjoint
$T_m^*$ is a contraction, so $\|\phi_m\|\le\delta^{-a/2}\|\Phi\|$ with $\phi_m=\delta^{-a/2}T_m^*i_I\Phi$, finite at
fixed $\delta$ (no uniform control-radius claim). Regularized noises are built with $W_m$ as reference via an
independent auxiliary source; no slow-source pullback is presumed. By `P:cameron-full-mean`, $\mathcal T_E\Phi=i^*T\Phi\,i\in L^r(I;\mathcal K(E))$ with
$r\in(2,2/a)$ from `E:cameron-block-parameters` (nonempty since $\theta<1-a/2$ and $\theta>1/2$: $1/(1-\theta)<2/a$
and $>2$); the compact-conjugation argument makes `E:symplectic-block-primitive` Bochner, and $1-1/r>\theta$
gives $C^\theta$; closedness of $\mathcal K(E)$ under Bochner integration gives a compact-valued path starting at
zero, also after constant stopping. Correct.

**Step 2 — unscaled covariance by compression.** With $A_{F,m}$ the full $F$ path from
`P:constant-phase-driver` and $H_{m,F}$ the stopped completed mean primitive in
`E:cameron-actual-covariance`, at original projection rank zero ($Q_J=I$),
$$\mathbb E[g_\delta A_{F,m}(u)W(i_I\Phi)]=\sqrt\delta\,H_{m,F}(\Phi)(u).$$
Compress through $i$ using $S_Fi=iS_E$ (true: $S_F(t)i e=(S_E(t)e,0,0)$) and $M_m=i^*A_{F,m}i$ (from
"A$i=iM_E$" in `P:constant-phase-driver`); the constant columns are present in $A_{F,m}$ and the mean until
this compression, inactive on $iE$ inputs. Since $g_\delta\delta^{a/2}=\delta^{(1-a)/2+a/2}=\sqrt\delta$ and
$g_\delta>0$, division gives
$$\mathbb E[M_m(u)W(i_I\Phi)]=\delta^{a/2}H_{m,E}(\Phi)(u),\quad u\le\ell_m.$$
The remark "the factor here is $\delta^{a/2}$, not $\sqrt\delta$" is correct. Completion permits every
$\Phi\in H_I$. Correct.

**Step 3 — fast-noise direction.** $T_mT_m^*$ is the orthogonal projection onto $\operatorname{ran}T_m$
($T_m$ isometry), so $(I-T_mT_m^*)i_I\Phi\perp\operatorname{ran}T_m$ and $W((I-T_mT_m^*)i_I\Phi)$ is orthogonal to
the fast first chaos (spanned by $W(T_mf)$): $\langle T_mf,(I-T_mT_m^*)i_I\Phi\rangle=\langle f,T_m^*(I-T_mT_m^*)i_I\Phi\rangle=0$.
Every continuous linear coordinate of $M_m$ is an $L^2$ limit of finite $W_m$-basis sums, so
$$\mathbb E[M_m(u)W(i_I\Phi)]=\mathbb E[M_m(u)W_m(T_m^*i_I\Phi)].$$
Multiplying by $\delta^{-a/2}$ and using Step 2:
$$D_{\phi_m}(\min(u,\ell_m))=\delta^{-a/2}\mathbb E[M_m(u)W_m(T_m^*i_I\Phi)]=H_{m,E}(\Phi)(u),$$
which is `E:symplectic-block-direction` after stopping both sides; no unstopped equality beyond $\ell_m$.

The new explanatory paragraph ("The adjoint pullback contributes $\delta^{-a/2}$ in $\phi_m$, canceling the
$\delta^{a/2}$ of the unscaled covariance. Orthogonality removes only the slow-noise component perpendicular to
the range of $T_m$; it does not replace the joint noise by an independent copy.") is an exact and correct summary
of the computation above and the orthogonality step; justified.

**Step 4 — compact endpoint lower bound.** Apply `L:symplectic-free` to the compact-valued $C^\theta$ path
$H_{m,E}(\Phi)$ starting at zero on $[0,B]$ (this uses only the compact baseline, which needs no Gaussian or
Hamiltonian hypothesis): $\|S_E(\ell_m)U_{H_{m,E}(\Phi)}(\ell_m,0)\|\ge\|S_E(\ell_m)\|\ge1$; if $\ell_m=0$ the
endpoint is $I$. The radius $\delta^{-1}+2$ is a fixed-parameter choice. Correct.

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Lost steps/qualifiers: none ("without a uniform control-radius assertion", "no slow-source pullback is
  presumed", "the factor here is $\delta^{a/2}$, not $\sqrt\delta$", "No unstopped equality beyond $\ell_m$",
  "all identities are fixed-parameter instances" all retained). Consumer-hypothesis checks: `P:cameron-full-mean`
  is used for $2<r<2/a$ (satisfied by `E:cameron-block-parameters`), `E:cameron-actual-covariance` at rank zero
  (satisfied), `E:raw-block-pullback` covariance factor (satisfied). No missing condition found.

---

## AUDIT dispositions

No AUDIT-worthy issues found. Specifically:

- **No lost step or qualifier** in any of the five proofs; all caveats (no uniform radius/control bound, no
  uncountable null-set intersections, no operator-norm free-group derivative or continuity, no unstopped
  equality, no independent-copy replacement of the fast noise, "mask occurs once", "$\delta^{a/2}$ not
  $\sqrt\delta$", no uniform compact approximation) are retained verbatim or with the same force.
- **Added explanatory assertions are all correct**: the reverse-triangle-inequality justification
  (`L:symplectic-free`), the interaction-conjugation transfer of the force identity (`P:symplectic-source`), the
  Young-remainder term classification (`P:symplectic-raw`), and the $\delta^{a/2}$/$\delta^{-a/2}$ cancellation plus
  orthogonality reading (`P:symplectic-block-mean`).
- **Separation of hypotheses** is correctly maintained: the compact-perturbation norm lower bounds
  (`E:symplectic-compact-young-baseline`, `E:symplectic-compact-product-baseline`, and the pure-mean endpoint in
  `P:symplectic-block-mean`) are explicitly de-coupled from Gaussianity/Hamiltonian structure; the symplectic
  conservation assertions (`P:symplectic-source`, `P:symplectic-raw`) are the ones that invoke $\mathfrak g_J$.
- **Zero-covariance case** is handled identically in both revisions (trailing paragraph; "$c=0$/zero covariance
  gives the free flow directly"), consistent with the model assumptions context that permits $\Gamma=0$.

Pre-existing observations (not rewrite defects, present in both revisions): (i) the differentiation of
$\omega(Ue,Uf)$ in `P:symplectic-source` suppresses an explicitly written product rule; it is a standard
consequence of the $C^1$ trajectories established just before, and is unchanged. (ii) The free-matrix symplectic
identity in `L:symplectic-free` is asserted via "determinant $=1$" — which is the correct $2\times2$ criterion — and
I verified it; this is not a defect. (iii) The use of "$\mathbb E\|ZM\|_{C^\theta}\le\|\Phi\|\|M\|_{L^2C^\theta}$"
relies on $Z=W(\Phi)$ being a single scalar Gaussian, which is exactly the definition in
`E:symplectic-combined-driver`; correct, but the proof's compactness means the reader must recognize $Z$ is scalar.

## Findings and limits

1. **All five proofs are preserved.** The rewrite is purely cosmetic plus *true* explanatory insertions. Every
substantive step reconstructed above is identical between old and new; the new text adds no assumption, removes no
hypothesis, and weakens no conclusion.

2. **Public reconstruction is COMPLETE for all five.** For each proof I enumerated the steps and supplied the
checkable public working (form/weight computation, determinant-$1$ symplectic criterion coinciding with
$B^*J_E+J_EB=0$, the conjugation transfer, the $\mathfrak g_J$ closure argument, the Young increment expansion with all
remainder terms, the $\delta^{a/2}$ scaling with $g_\delta\delta^{a/2}=\sqrt\delta$, and the
$T_mT_m^*$ orthogonal-projection cancellation).

3. **Upstream results were used, not re-proved.** The target consumer uses of
`P:constant-young-linear` (on $\mathcal L(E)$), `P:cameron-full-mean` ($r\in(2,2/a)$), `E:cameron-actual-covariance`
(rank-zero specialization), `L:source-retaining-isometry`/`L:source-pointfield-regularity`/`P:source-ordinary-response`
(at fixed $\rho$), and `E:raw-block-pullback` (unit covariance factor) respect their stated conditions. Their own
proofs are unassigned and were not counted as additional reviews.

4. **Separation of scope.** This verdict certifies *argument preservation and readability equivalence* between the
two revisions of this module, not the truth of the whole book, the upstream analytic results, source-image
fidelity, Lean quotation correspondence, or release readiness.

5. **Minor acceptable terseness** (inherited, not introduced): the one-line product-rule differentiation in
`P:symplectic-source` and the scalar-$Z$ recognition in the moment bounds. Both are standard and unchanged; flagging
them here as pre-existing context-limitation notes only, not as rewrite defects.
