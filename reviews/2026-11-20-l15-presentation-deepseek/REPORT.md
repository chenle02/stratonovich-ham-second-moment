Verdict: PASS
Confidence: high

## Edit 1

**Reading:** COMPLETE

**Truth:** CORRECT

The added statement about the lift lemma is true in the setting in force. Let
`L in \mathcal V_{E,R}` be an operator-norm limit of operators
`L_q^E(u,v) = (0, M_q u)`, where `M_q` is multiplication by the smooth compact
potential `V_q = m_R(\Gamma*q)`. Then the zero-column form `L(u,v)=(0,Mu)` and
the equality `||L|| = ||M||` are correct: from the `E` norm,

\[
||L|| = \sup_{(u,v)\neq 0}
\frac{||(0,Mu)||_{H^{1/2}\times H^{-1/2}}}
{\sqrt{||u||_{H^{1/2}}^2+||v||_{H^{-1/2}}^2}}
= ||M||,
\]

with `v=0` attaining the supremum.

The representation `Mu = Vu` for `u in C_c^\infty` is also correct. The
construction in the proof produces `V = M\chi_R` as the `H^{-1/2}`-limit of the
smooth compact potentials `V_n = M_n\chi_R`, and the product `Vu` for
`V in H^{-1/2}` and `u in C_c^\infty` is well defined, because a compactly
supported smooth `u` acts as a bounded multiplier on `H^{-1/2}`. This is the
standard dual estimate: for `s < 0`, multiplication by `u in C_c^\infty` on
`H^s` is bounded by duality from its boundedness on `H^{-s}`.

Uniqueness is exactly as claimed. If a second `W in H^{-1/2}` were supported in
`supp m_R` and satisfied `Mu = Wu` on all compact tests, then evaluating both
at the fixed compact smooth cutoff `\chi_R = 1` near `supp m_R` gives
`W = W\chi_R = M\chi_R = V`.

**Support:** SUPPORTED

The supporting lines are in the proof of `L:uniform-E-lift`:

- “At fixed `R` choose real compact smooth `\chi_R = 1` near
  `\operatorname{supp}m_R`. Since `M_n\chi_R = V_n`,
  `||V_n - V_j||_{H^{-1/2}} \le ||\chi_R||_{H^{1/2}}||M_n-M_j||`.”
  This proves the `V_n` converge and defines `V`.
- “`V_n \to V`, with the same support by testing outside it.” This proves the
  support claim.
- “Smooth multiplication on `H^{-1/2}` identifies `Mu = Vu` on compact tests,
  then on `H^{1/2}` by density.” This proves both the distribution identity on
  `C_c^\infty` and the continuous extension of multiplication by `V` to `M`.
- “The identity `M\chi_R = V` gives uniqueness.” This is the uniqueness
  argument described above.

One small point is that boundedness of multiplication by `C_c^\infty` on
`H^{-1/2}` is invoked rather than proved in this excerpt, but it is a standard
Sobolev-space fact and the proof line states precisely that fact as the
mechanism. It is not a hidden assumption.

**Faithfulness:** FAITHFUL

The added sentences state exactly the content already used in the unchanged
proof. They do not strengthen the lemma: the extension claim is precisely the
density step already present. They do not weaken it: the asserted distribution
identity and support property are the ones subsequently needed to define
`v_V(u,w)` and the spectral form `\beta(V)` on `H^1`. The uniqueness claim is
also the right one, preventing ambiguity in the later use of `V`.

**Findings:** none identified within this read.

## Edit 2

**Reading:** COMPLETE

**Truth:** CORRECT

The added explanation of the row

\[
k_R(z,w)=(\eta_R z_1)(\eta_R\Lambda^{-1}w_2)
\]

is true. The exponents satisfy `\alpha/4 < s < 1/2`, an interval that is
nonempty because the governing threshold has `\alpha < 2`. Both displayed
factors do lie in `H^{1/2}`:

- `z_1 in H^{1/2}` by definition of `z in E`.
- `w_2 in H^{-1/2}` and `\Lambda^{-1}w_2 in H^{1/2}`, because the Fourier
  weights give
  \[
  ||\Lambda^{-1}w_2||_{H^{1/2}}
  = ||\Lambda^{-1/2}w_2||_{L^2}
  = ||w_2||_{H^{-1/2}}.
  \]
- Multiplication by the smooth compact cutoff `\eta_R` is bounded on
  `H^{1/2}`; hence `\eta_R z_1` and `\eta_R \Lambda^{-1}w_2` both belong to
  `H^{1/2}`.

Since `s < 1/2` and the Fourier weights satisfy `\langle\xi\rangle \ge 1`,
`H^{1/2}` embeds continuously in `H^s`, with embedding norm at most one.
Therefore both factors lie in `H^s`.

The product then makes sense by `L:cameron-fractional-products`. That lemma
gives a bounded bilinear map

\[
H^s \times H^s \to H_{\mathrm{sp}},
\qquad
||fg||_{H_{\mathrm{sp}}}
\le C_s^2\sqrt{R_{\mathrm{sp}}}||f||_{H^s}||g||_{H^s},
\]

and its proof explicitly establishes “uniqueness of the bilinear extension.”
This is precisely a continuous `H_{\mathrm{sp}}`-valued product, so the phrase
“continuous `H_{\mathrm{sp}}`-valued product” is accurate and not stronger than
the lemma.

**Support:** SUPPORTED

The supporting text is:

- `L:cameron-fractional-products`, especially the estimate
  `\eqref{E:cameron-fractional-product}` and Step 3, which proves uniqueness
  of the bilinear extension.
- The proof of `L:uniform-mean-cutoff`, which states “The map
  `w_2 \mapsto \Lambda^{-1}w_2` is an isometry from `H^{-1/2}` to `H^{1/2}`,
  and `H^{1/2}\hookrightarrow H^s` has norm one.” This is exactly the missing
  regularity step for the second factor.
- The same proof applies the cutoff bound at `\sigma = 1/2` and
  `L:cameron-fractional-products` to the two factors. Earlier,
  `P:cameron-spatial-map` also uses the fact that multiplication by `\eta_R`
  maps bounded `H^{1/2}` sets into `H^s` via `P:cutoff-singular-values`.

Thus all new assertions are either immediate from definitions, already proved
in the preceding section, or proved a few lines later in
`L:uniform-mean-cutoff`.

**Faithfulness:** FAITHFUL

The row formula is unchanged; only the explanation was added. The added text
matches what later proofs actually need. In particular,
`L:uniform-mean-spatial-tails` uses the product identity

\[
\tau_h(fg)-fg = (\tau_h f - f)\tau_h g + f(\tau_h g - g)
\]

“first for smooth factors and then by the continuous fractional product
extension.” The new sentence supplies exactly the continuity that justifies
that step, no more and no less.

**Findings:** none identified within this read.

## Edit 3

**Reading:** COMPLETE

**Truth:** CORRECT

The displayed real inner product on `E = H^{1/2}\times H^{-1/2}`,

\[
\langle z,w\rangle_E
=\langle\Lambda^{1/2}z_1,\Lambda^{1/2}w_1\rangle_{L^2}
+\langle\Lambda^{-1/2}z_2,\Lambda^{-1/2}w_2\rangle_{L^2},
\]

is the correct one for the stated Sobolev norm convention
`||u||_{H^r} = ||\langle\xi\rangle^r \widehat u||_{L^2}` and for
`\Lambda = (1-\Delta)^{1/2}` with symbol `\langle\xi\rangle`.

For `r = 1/2`, polarization of the Fourier-weighted norm gives

\[
\langle u,v\rangle_{H^{1/2}}
= \int \langle\xi\rangle \widehat u \overline{\widehat v}\,d\xi
= \langle\Lambda^{1/2}u,\Lambda^{1/2}v\rangle_{L^2}.
\]

For `r = -1/2`,

\[
\langle u,v\rangle_{H^{-1/2}}
= \int \langle\xi\rangle^{-1}\widehat u \overline{\widehat v}\,d\xi
= \langle\Lambda^{-1/2}u,\Lambda^{-1/2}v\rangle_{L^2}.
\]

Therefore the display is exactly the inner product induced by the fixed norm
convention. It also makes `J_0(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)` an
isometry from `E` to `L^2(\R^d;\C^2)`, hence unitary onto its image (and in
fact onto all of `L^2(\R^d;\C^2)` by the invertibility of `\Lambda^{1/2}` and
`\Lambda^{-1/2}`).

The consistency with the velocity row is also correct. The second term in the
inner product satisfies

\[
\langle z_2,w_2\rangle_{H^{-1/2}}
= \langle z_2,\Lambda^{-1}w_2\rangle_{L^2}
\]

on real states. Taking `z_2 = M_q z_1 = V_q z_1`, the physical Fubini argument
produces exactly the row test `(\eta_R z_1)(\eta_R \Lambda^{-1}w_2)`; the
`\Lambda^{-1}` factor in the velocity entry is therefore consistent with the
display.

**Support:** SUPPORTED

The supporting text is the norm convention stated in
`integrated_compact_gaussian.tex`:

- “For real `r`, the norm on `H^r(\R^d)` is
  `||\langle\xi\rangle^r\widehat u||_2`,” together with the definition
  `\Lambda=(1-\Delta)^{1/2}`.
- “For `E = H^{1/2}(\R^d)\times H^{-1/2}(\R^d)` use the physical unitary
  coordinates `J_0(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)`.”

These lines determine the displayed inner product uniquely as the real
polarization making `J_0` unitary. The row consistency is further supported by
`P:cameron-spatial-map`, whose proof says the velocity pairing in `E` has
weight `\Lambda^{-1}` and sets `w' = \Lambda^{-1}w_2`.

**Faithfulness:** FAITHFUL

The display does not change any proof or add a hidden convention. The inner
product was already implicit in the unitary coordinates `J_0`; making it
explicit is exactly what the row identity
`\eqref{E:uniform-mean-row}` needs. It does not misrepresent the `F`-level
operator: the constant-data columns remain outside `E`, and the displayed
inner product only claims to describe `E`, not `F`.

**Findings:** none identified within this read.

## Findings and limits

No material defect was identified in the three edits. All three statements are
correct under the hypotheses and conventions in force; each is supported by
the existing proof text or by a cited supplied statement; and each is faithful
to the subsequent uses.

The main reliance on background material is the boundedness of multiplication
by compactly supported smooth functions on negative Sobolev spaces, invoked in
the proof of `L:uniform-E-lift`. It is a standard fact and is stated as the
mechanism in the proof line itself; I do not count it as an unsupported new
claim. Similarly, the cutoff boundedness on `H^{1/2}` used in Edit 2 is proved
immediately afterward in `L:uniform-mean-cutoff` and was already used in
`P:cameron-spatial-map`.

This review covers only the three specified edits and the supplied frozen
excerpts. It does not certify the whole book, the untouched surrounding
arguments, or any omitted material outside the excerpts.
