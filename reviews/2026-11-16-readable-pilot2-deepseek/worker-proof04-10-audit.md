# Fresh worker QA: pilot-2 proofs 4 and 10

Complete OLD and NEW statements/proofs were freshly read against cdde711c
and 5d05a6b1; the section's Fourier/Sobolev conventions were included.
Both NEW bodies are byte-identical to the corrected 53a5570e versions.
This is same-GPT argument-preservation QA, not another independent vote.

## L:cutoff-factorization

Argument preserved. The added Peetre/lattice explanations retain both signs
of the real order, the fixed lattice-spacing constants, and all old kernels.
Unitary Fourier inversion contributes c_d; the ordinary cutoff transform
contributes c_d^-1, so the factors cancel. Dense finite sequences and smooth
compact functions give mixed-Schur cores, with extension and truncation
identification in the L2 coordinates. Periodic coefficient decay gives
Sobolev convergence of partial sums; bounded cutoff extension and distributional
uniqueness identify the recovery limit for every real sigma. Gamma remains
positive. No point sampling, alias term or extra hypothesis is introduced.
Both former AUDIT comments are replaced by the approved explicit bridges.

## P:cutoff-boundary-tests

Argument preserved. The corrected roadmap attributes plateau support to the
physical test functions, rather than nonlocal Bessel-transformed vectors.
The inverse smoothing multiplier is only applied to Schwartz vectors; the
identity for general x follows by adjointness of the bounded forward map.
The common finite variance constant, plateau qualification and translation
noncompactness argument remain unchanged. No general nonzero source-family
existence or Schatten-Bochner conclusion is added.

No source edits, builds, provider call or independent scientific grade from
this worker read. The separate DeepSeek reread and its adjudication are in
REPORT.md and ADJUDICATION.md.
