# Static variational finiteness: exact source supplement

Date:2026-10-28 UTC. Scope: locate the source of finiteness of the static
variational quantity M used in the finite coefficient constant. This is an
additive source/application check. The existing audit, manuscript, frozen
Riesz packet and actual Opus verdict/confidence are unchanged.

## Exact printed link

Chen–Hu(2025), published p2175, in the proof of Lemma5.1, explicitly invokes
**[11],Theorem1.1** and displays

  sup_(g in F_d) { [integral gamma(x-y)g(x)^2g(y)^2 dxdy]^(1/2)
                  -(1/2) integral |grad g|^2 }
    = 2^(alpha/(4-alpha)) M.

The immediately following line gives the homogeneous rescaling responsible
for the factor. Reference[11] is Xia Chen(2023), *Exponential asymptotics for
Brownian self-intersection local times under Dalang's condition*,
Electron.J.Probab.28,article119, DOI10.1214/23-EJP985.

## Explicit finiteness statement in the cited source

The actual local DOI-bearing source
`../SPDEForge/sources/chen-23-exponential/chen-23-exponential.pdf`
has SHA256
`9ed4b0ae633cc79eb1b985ecf00b2ae67db83061fd0d8a73628704b5b664a5da`.
Its title page identifies that paper and DOI. Its Theorem1.1, printed p2,
assumes Dalang's spectral integral(1.3), gives the square-root variational
quantity in(1.4), and **explicitly states that the variations on the right
sides of(1.4) and(1.5) are finite**. Page1 expressly permits generalized
nonnegative positive-definite covariances on Schwartz space. The p2 running
header reads `FIXME!`; this typographical artifact is preserved, not silently
removed or treated as a mathematical qualification of the theorem.

Thus Chen–Hu's p2175 source invocation identifies a finite quantity and its
positive multiple of M. For the present use, an even simpler local deduction
is enough: M has gradient penalty1 whereas the cited finite supremum has
penalty1/2, so M is no larger. Either route supplies M<infinity under Dalang.
The comparison is our deduction; the explicit finiteness is from Chen2023.
No sharp value of M, white-noise corollary constant or LDP proof is used.

For the static homogeneous endpoint of degree beta<2, its Dalang condition
is the one already checked in Chen–Hu p2146. This applies to the Riesz
endpoint and, once its positive definiteness is independently validated, to
the proposed planar weighted endpoint. It does not itself validate the planar
construction or any interpolation proof.

## Actual viewing and limitations

Newly rendered and viewed in this supplement:
- Chen–Hu publisher PDF p2175 (PDF page32), hash
  `58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22`.
- Chen2023 title/assumption page1 and Theorem1.1 page2.

Images are retained in `finiteness-source-pages/`. Bibliographic identification
of[11] was also checked in Chen–Hu's extracted reference list. No source PDF
was modified. Only the stated theorem and its application were checked; the
underlying variational/LDP theorem was not re-proved, and this is GPT-family
work rather than an independent reviewer certificate.
