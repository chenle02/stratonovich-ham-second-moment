# Source manifest

Every mathematical citation of X. Chen's paper in this project uses the
**author version** below. Verify its hash before you rely on it.

## Authority: X. Chen, author version

| Field | Value |
|---|---|
| File | `chen-2026-author/aap-chen-2025.pdf` |
| Title | *Time-dependency in hyperbolic Anderson models: Stratonovich regime* |
| Status line | "Submitted to the Annals of Applied Probability" (title page) |
| Pages | 64 |
| URL | https://web.math.utk.edu/~xchen3/aap-chen-2025.pdf |
| Server Last-Modified | 2026-09-25 13:06:28 GMT |
| Retrieved | 2026-10-26 |
| SHA-256 | `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c` |
| Citekey | `chen:author2026:time-dependency` (in `extra.bib`) |

[held back: collaborators' unpublished work]

### Pinpoints (PDF page numbers)

| Item | Page | Content |
|---|---|---|
| (1.1)–(1.3) | 2 | Model, covariance, spectral measure |
| Theorem 1.1, (1.5) | 2–3 | Existence iff spectral condition; homogeneous form α₀+α<2 |
| Theorem 1.2, (1.9)–(1.10) | 3 | **Two-sided** first-moment bounds (not an exact limit) |
| (1.11)–(1.13) | 4 | Variational constants 𝓔, 𝓔_*, kernel γ_*⁰; 𝓔_* < 𝓔 |
| Discussion after (1.13) | 4 | Exact limit *predicted* = upper bound; needs LDP for the complex functional (1.14) |
| (1.22) | 6 | Conjecture: all integer p, constant p^{(4−α)/(3−α)} × upper bound |
| (2.13)–(2.16) | 10 | Stratonovich expansion, kernels g_n |
| Lemma 2.4–2.5, (2.18) | 11 | Integrability test; product rule S(f₁⊗f₂)=S(f₁)S(f₂) |
| (2.19)–(2.22) | 12 | Wick formula, expected even Stratonovich integrals |
| (3.1)–(3.5) | 14 | Norms ‖·‖^{(0)}, ‖·‖^{(1)}_{j,k}, ‖·‖^{(2)}_{j,k} |
| **Theorem 3.1, (3.6)** | 15 | Universal two-chain pairing bound (includes cross-pairings) |
| **Theorem 4.1, (4.3)** | 22 | Exact formula for 𝔼[S_n(g_n)]² (two chains) |
| (4.4) | 22 | Limit used for integrability |
| Lemma 4.4, Remark 4.5 | 30 | Individual equal-length diagram limits; used via independent noise colors for G0 mixed diagrams |
| (5.1)–(5.4) | 34–35 | Norm summability and the printed time-uniform estimate; see G0 source audit below |
| **Remark 5.1, (5.8)** | 37 | 𝔼u²(t,x) ≤ e^{Ct²} for large t (the source’s coarse p=2 upper bound) |
| Theorem 6.1, Remark 6.2 | 37 | Stratonovich moment representation (single chain) |
| **Remark 6.3** | 42 | Single-chain monotone order: "the major reason why the current idea can not work for 𝔼uᵖ, p>1" |
| Theorem 7.1, Remark 7.2 | 44 | LDP for time-randomized intersection local time; difficulty without 2α₀+α<2 |
| Section 8 | 55 | Proof of Theorem 1.2 |
| Remark 8.1, Lemma A.1 | 60 | Why the lower bound is not sharp; Laplace-weighted version of Theorem 3.1 |

## Superseded: arXiv v1

`llm_pack/chen-25-time-dependency.tex` is the SPDEForge flattened TeX of
arXiv:2510.01412v1 (citekey `chen:25:time-dependency`). It is **useful for
TeX-level reading of the unchanged parts** (Sections 2–7), but its
Theorem 1.2 states an exact limit, which the author version weakens to
two-sided bounds. Cross-check any statement you take from v1 against the
author PDF. The labels in v1 (`th-2`, `intro-10`, …) are not the author
version's numbering.

## Other sources (SPDEForge llm_pack copies, SPDEForge commit 29b4c3ad)

| File | Citekey | Role | SHA-256 |
|---|---|---|---|
| `llm_pack/chen_hu-25-hyperbolic.tex` | `chen.hu:25:hyperbolic` | Time-independent Stratonovich wave equation; calibration α₀→0 | `b7864be2…5a75e8b` |
| `llm_pack/chen_deya_ea-23-hyperbolic.tex` | `chen.deya.ea:23:hyperbolic` | Stratonovich wave equation, Strichartz route (d=1,2) | `f17acdaf…dfd89af` |
| `llm_pack/balan_chen_ea-22-exact.tex` | `balan.chen.ea:22:exact` | Skorohod time-independent exact asymptotics (BCC) | `88262631…fdebfdf3` |
| `llm_pack/balan_conus-16-intermittency.tex` | `balan.conus:16:intermittency` | Skorohod p≥2 bounds with time-fractional noise | `b89af528…0d1ff84f` |
| `llm_pack/chen-25-time-dependency.tex` | `chen:25:time-dependency` | arXiv v1 (see above) | `1602dff7…1ebabf` |

Full hashes: run `sha256sum sources/llm_pack/*.tex`.

## Read-only sibling projects (do not edit)

[held back: collaborators' unpublished work]

## G0 source audit (2026-10-27)

The rendered author PDF prints (4.4) as the citation in Remark 5.1, but (4.4)
is a smoothing limit; the growth estimate appears as (5.4). The preceding
sentence at (5.3) states a constant independent of the order and time.
The exact spatial-white-noise first-order test in the project notes shows
that this uniformity over all time cannot hold. The proof uses theta=n/t:
the first norm is finite at each positive theta but not uniformly bounded
as theta tends to zero, and the second-norm bound (A.3) is explicitly only
for large theta. The project retains that restriction and recovers the final
large-time exp(Ct²) bound with a corrected argument.

[held back until the source author has been told]

## G1 static calibration source (2026-10-27)

Chen–Hu, published *Annals of Probability* 53(6) (2025), 2144–2195,
DOI `10.1214/24-AOP1758`, is available read-only at
`../../SPDEForge/sources/chen_hu-25-hyperbolic/published-24-AOP1758.pdf`.
SHA-256: `58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22`.
Rendered PDF page 4 (journal p.2147) was inspected for Theorem 1.2, (1.9).
The G1 calibration imports only its exponent (4-alpha)/(3-alpha).

The accompanying publication audit records an internal numerical mismatch
between the general theorem's printed white-noise specialization and the
printed Corollary 1.4. Neither disputed constant is used here. Static finite-
order coefficients are calculated independently; they are not asymptotic
constant estimates and do not settle the sibling constant-verification project.
A frozen image and source map accompany the G1 review packet.

## Reviewed G2 partial upper bound (2026-10-27)

The project notes now prove the target upper time scale for 0<alpha<=1 in
d=1,2,3. The new proof imports the pinned author's fixed-order construction
and uses wave Fourier/mass formulas (2.3)–(2.5), common-field regularization
(2.9),(2.11),(2.23)–(2.24), and the d3 limit convention on pp13–14. The new
spectral ball-mass and degree-one polar/Gaussian-inversion estimates are proved
in the notes, not attributed to an external theorem. The repaired source
(5.4) issue is not used as an input. Higher-alpha cases and sharp constants
remain open. Exact review/promotion bindings are in the Round3 evidence.

## Static phase operator input (2026-10-28)

Crouzeix--Palencia, *The numerical range as a spectral set*, author preprint
arXiv:1702.00668v1 (eight pages; PDF date February 3, 2017).
Local exact source: crouzeix-palencia-2017/arxiv-1702.00668v1.pdf.
SHA-256: 0e33b65b3fab07632364111290e380b0696d7ace8168c9b834028de57d943c53.
Acquired from https://arxiv.org/pdf/1702.00668v1; identity and pages 1,
5 and 6 visually inspected. The imported bounded-Hilbert-operator spectral-set
inequality is (3), p.1, and Theorem 6, pp.5--6. The numerical-range closure and
holomorphic-neighborhood hypotheses are retained. No unbounded-operator
extension is used: spatial Fourier bands make each operator application bounded.

The later published work is DOI 10.1137/17M1116672, already retained under
the ordinary six-repository reference queue. The local source-specific
bibliography key crouzeix.palencia:source2017:numerical explicitly identifies
the preprint; none of its numerical pinpoints assert journal numbering.
The new static phase proof, complete predecessor section, source images and
hash bindings are in ../reviews/2026-10-28-static-phase-all-orders/.
This input does not establish a colored-time or overlapping-block result.

## Published comparison-pinpoint custody (2026-10-29)

Existing-corpus Balan--Conus2016published PDF is preserved at
`reviews/2026-10-29-full-upper-cold-v7/source-checks/balan-conus-published.pdf`,
SHA256`4fc3f73cc6164c1c9cc6a384ffdfb3389d21d34be1e86bcfbc681375a59d2756`.
Header/first5pages checked;full rendered printed1492opened:Theorem2.1(b),
Eq8/10and the current manuscript pinpoints agree. This supplements the local
source-TeX comparison with publisher numbering,not a full proof audit or a
new Skorohod theorem. Chen--Hu published2180was also reopened to authenticate
the existing p2specialization ofEq5.15. Exact images/hashes/coverage are in
that directory's pinpoint-binding.json. Neither check changes the author-
version authority,first-moment normalization,reference identities or corpus.


## Published lifetime-concentration source reading (2026-10-29)

The same publishedChen--HuPDFSHA58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22
was reopened at printed2174and2183--2185 (PDF31,40--42). Lemma5.1(5.6)
has unequal-dampingupper control;Lemma5.3balances lifetimes near(4-alpha)n/p.
The held older llm_packTeX around2510--2620omits that1/pand a denominator
weight retained in the published proof. Use the publication for that import,
not the older/generated TeX. Four direct renders were opened;source custody
and exact scope are in ../reviews/2026-10-29-degree-four-clock-probe/balanced-horizon-recon/.
This is reconnaissance for a future sharp transfer,NOTa proved fractional-
time extension or an adopted numerical/variational/source1.24correction.
