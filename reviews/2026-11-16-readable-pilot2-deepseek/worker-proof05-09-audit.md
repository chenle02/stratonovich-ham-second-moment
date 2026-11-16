# Readability pilot2: fresh proofs05–09 QA

All five arguments are preserved. No required wording correction or new unresolved material gap was found in these assigned units; no old material gap was identified during this bounded read. This is same-GPT worker QA, not independent review or a scientific grade.

Whole old/new statements and proofs were freshly read at `cdde711c248862f33207860107dd0e6b31d60852` and `5d05a6b1fef244fc5416c9d25d50c6fca0ca75c0`. All statement bytes match. Frozen TeX hashes and exact Git bytes match; diff and step-map hashes match INPUTS.json.

## Proof5: P:cutoff-singular-values — ARGUMENT_PRESERVED

Old LF313–368; new LF501–604.

- New LF514–528, Roadmap and factor selection: The bounded cutoff factorization reduces approximation to the torus inclusion. The spatial domain remains whole-space L²; no periodic replacement of the model or radius-uniform constant is inferred.
- New LF529–532, Bessel domains and unique extension: By the stated Sobolev Fourier norm, Lambda^(-sigma-gamma) maps L² isometrically onto H^(sigma+gamma), even for negative sigma+gamma, and Lambda^sigma maps H^sigma onto L². The bounded product agrees on dense Schwartz functions, so extension is unique.
- New LF533–547, Diagonal weights and finite-rank tail: Input/output weights divide to <kappa_k>^-gamma. For integer k outside |k|_infinity<=n, some coordinate has size>=n+1, hence |kappa_k|>=(2pi/L)(n+1). This yields the stated sup tail and exactly (2n+1)^d retained modes.
- New LF548–558, Compactness via finite nets: K_n has rank at most that retained-mode count. Its norm approximation carries finite nets from a bounded finite-dimensional image to the limiting unit-ball image, with twice the chosen radius; completeness yields compact closure.
- New LF569–595, Rank/index threshold and constant: Set x=j^(1/d)>=3 and n=floor(x/4). Then 2n+1<=x/2+1<x, so rank K_n<j, including the n=0 boundary (d=1,j=3). Since n+1>x/4, (L/(2pi))^gamma(n+1)^-gamma <=(2L/pi)^gamma j^(-gamma/d). Restriction of a rank<j map to the first j singular vectors has a kernel vector. For j<3^d, 3^gamma j^(-gamma/d)>1 supplies the operator-norm bound. The stated maximum constant is unchanged.
- New LF598–604, Schatten sum: The explanation explicitly raises the singular bound to p and sums; p gamma>d is exactly the convergent power-series condition. It does not replace this by an unpowered singular-value sum.
- New LF606–608, Retained qualifications: No uniform support-radius constant and no necessity at the endpoint are asserted.

## Proof6: P:compact-two-envelopes — ARGUMENT_PRESERVED

Old LF394–439; new LF630–716.

- New LF649–672, Bounded adjoints and factor order: For real compact smooth chi, the inner-product calculation on Schwartz reverses Lambda^sigma, multiplication, Lambda^-sigma to Lambda^-sigma chi Lambda^sigma. Both products have bounded extensions by the preceding multiplier result, so density establishes their Hilbert-adjoint identity on all L². No commutation of chi with a Bessel power or evenness of chi is assumed.
- New LF676–681, Swap and envelopes: D_gamma has identical diagonal entries and thus commutes with the swap U. Therefore P_chi* D_gamma=U P_chi D_gamma U, without any unsupported P_chi/D_gamma commutation. Input/output factors are unitary conjugates.
- New LF682–694, Direct-sum singular values: The product of the block-diagonal operator with its adjoint is block diagonal; the eigenvalues of the two product blocks give the singular-value multiset union after square roots. Unitary conjugation preserves multiplicity and the S_p norm.
- New LF697–713, Trace identification: K/sqrt(lambda) maps the lambda eigenspace of K*K isometrically to that of KK*, with inverse K*/sqrt(lambda), because the composed maps are the identity there. Positive eigenvalues are squared singular values; raising them to p/2 gives s_j^p. Zero modes contribute zero and S_p membership makes the sum finite.
- New LF630–646, Parameter preservation: Both compact factors use p>=1 and p gamma>d for Schatten membership; the trace statement retains p>=2. The proof adds no assumption of cutoff projection or selfadjointness of P_chi.

## Proof7: L:compact-positive-order — ARGUMENT_PRESERVED

Old LF445–472; new LF722–778.

- New LF733–755, Compactness and noncommuting order: For T=(I-Q_n)A^(1/2), TT*=(I-Q_n)A(I-Q_n), hence ||T||² equals its norm. Congruence preserves A<=B; the compressed products are positive, so their norms are ordered. This does not require A and Q_n to commute. Q_n A^(1/2) has finite rank and converges in norm, so A^(1/2) and then its product A are compact.
- New LF759–770, Max-min and zero padding: On every fixed j-dimensional subspace, pointwise Rayleigh order survives infimum and then supremum. The standard compact eigenbasis comparison gives lambda_j. In the ambient infinite-dimensional H, if fewer than j positive eigenvalues exist, that subspace meets their orthogonal complement, making the positive Rayleigh infimum zero. Zero padding remains valid.
- New LF772–777, Trace limit: Only scalar powers of nonnegative eigenvalues are compared. Finite partial sums increase to the trace and are bounded by finite Tr B^t. The explicit refusal to assert A^t<=B^t remains. The premise t>=1 and finite Tr B^t is not weakened.

## Proof8: P:localized-finite-variance — ARGUMENT_PRESERVED

Old LF474–511; new LF780–845.

- New LF800–809, Left/right localization: P_chi Z=Z gives P_chi ZZ* P_chi*=ZZ*. Independently, ZP_chi=Z and its adjoint give P_chi* Z*Z P_chi=Z*Z. Finite summation yields the two variance identities. This uses no P_chi selfadjointness or idempotence.
- New LF810–827, Congruence, trace scaling and zero case: Congruence on the output/input variance bounds gives respectively C B_out and C B_in. p>=2 gives t=p/2>=1; p gamma>d supplies finite envelope trace. Scaling the positive eigenvalues by C contributes C^(p/2). C=0 forces both positive variances, then each positive summand and each Z, to vanish.
- New LF830–843, Individual summand compactness and Schatten bound: Removing one positive summand leaves a positive sum, so ZZ*<=V_out. Positive-order compactness applies to ZZ*, not directly to nonpositive Z. Its finite spectral projections give Q_n Z finite-rank approximants with squared norm error equal to the compressed ZZ* tail. Eigenvalue domination and p/2 powers give exactly the stated S_p estimate.
- New LF847–849, Retained application boundary: Two localization identities remain hypotheses, and no source-noise coefficient family is identified. The added explanations do not treat P_chi as a projection.

## Proof9: C:finite-gaussian-operators — ARGUMENT_PRESERVED

Old LF517–572; new LF851–955.

- New LF863–880, Compression variance and positivity: The finite matrix output variance differs from Pi V_out Pi by a sum of positive terms Pi Z(I-Pi)Z*Pi; each quadratic form is ||(I-Pi)Z*Pi x||². The input estimate follows with adjoints interchanged. These estimates do not require the compressed family to satisfy the original cutoff localization.
- New LF881–892, Two eigenvalue comparisons: First use positive-form order to compare the finite compressed variance with Pi V Pi. Then compare Pi V Pi with V by max-min over subspaces of ran Pi, where their quadratic forms agree. Zeros after the finite compression do not increase any eigenvalue. Applying scalar p/2 powers and summing preserves the trace bound.
- New LF895–906, Finite matrix bound and averaging: The same independent real standard Gaussians drive finite complex matrices, and even p>=2 matches the matrix theorem. Each variance trace is <=C^(p/2)||K_out||_Sp^p, so their average has the same bound. Raising the matrix estimate to p gives (p-1)^(p/2), with no extra factor2.
- New LF909–922, Pointwise norm convergence: For each fixed finite coordinate vector, X is compact and finite rank F approximates it. ||X-Pi X Pi||<=2||X-F||+||F-Pi F Pi||; the latter splits into (I-Pi)F+Pi F(I-Pi). Strong convergence is uniform on finite-dimensional ran F and, after adjoint, ran F*. This justifies operator-norm convergence without uniform convergence over all Gaussian coordinates.
- New LF924–936, Singular-value variational formula: Upper bound uses the first j-1 right singular vectors; lower bound uses a kernel vector of projection onto any subspace of dimension<j within the first j singular vectors, for s_j>0. The s_j=0 case is nonnegative and immediate; zero padding covers finite rank. Triangle inequality under the same supremum/infimum yields the norm-Lipschitz bound in both directions.
- New LF937–952, Measurability and distinct Fatou operations: Finite linear coordinate dependence makes X norm-continuous; each singular value is Lipschitz and partial p-power sums are measurable. Their increasing limit is measurable even at infinity. First Fatou uses counting measure for each fixed coordinate vector; then probability Fatou yields E||X||_Sp^p<=liminf E||X_n||_Sp^p. The finite uniform bound gives almost-sure finiteness; pth root gives the asserted constant.
- New LF951–954, Retained convergence boundary: No S_p-Bochner convergence, infinite Gaussian sum or time-path construction is claimed.

## Scope limits

Definitions of Sobolev norms, real compact smooth chi, zero-padded singular values, complete L:cutoff-factorization statement (used as upstream input), balanced H/E coordinates, envelope definitions and adjacent retained application caveats. Step-map was hash-checked as custody only; its global line-map correctness is parent scope.

First four full proofs, proof10, the two factorization AUDIT matters and downstream operator/source/Young construction are not cleared by this report. Earlier finite-matrix dilation tail was seen incidentally but its proof was not fully audited here. No external mathematical source or prior reviewer reasoning was used.

The five old/new statement/proof units were freshly read and all edits considered; no clearance was transferred from the118 pilot or inferred merely from unchanged formulas. No source edits, repairs, builds, tests, Lean/provider/literature calls, Git mutations or independent scientific vote.
