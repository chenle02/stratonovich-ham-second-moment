# PILOT2: fresh author-side proof01–03 comparison

All three: **SUPPORTED editorial equivalence**. Required corrections:0. Unresolved possible material gaps:0. No old-text concern was newly identified.

Original: cdde711c248862f33207860107dd0e6b31d60852; new: 5d05a6b1fef244fc5416c9d25d50c6fca0ca75c0. Source and pilot2.diff hashes match INPUTS.json.

## L:gaussian-scalar-powers

Full old/new statements and proofs read; statements exactly equal. New proof LF30–74.

- **Roadmap and three step headings:** Match the same four claims: weighted powers, integer consequence, finite sequence Holder, fractional expectation. No additional theorem or infinite sequence scope is asserted.
- **Step1 reduction/derivative sign:** For v>0 division gives t^theta<=theta*t+1-theta. With0<theta<1, theta-1<0 makes derivative negative on(0,1),positive on(1,infinity), and value0 at1. Continuity handles t=0; v=0 remains separate.
- **Step1 integer substitution and endpoints:** u=|x|^L,v=|y|^L,theta=q/L is admissible exactly when0<q<L. Resulting exponents q,L-q and weights q/L,(L-q)/L are correct. Unchanged0^0 integer convention covers endpoint identities.
- **Step2 explicit normalized powers:** For m>1 the normalized nonnegative entries a,b give u=a^m,v=b^(m/(m-1)); u^(1/m)v^(1-1/m)=ab. Both sums are1 after the nonzero-norm branch, so the weighted sum is1. Multiplying by both original norms restores finite Holder.
- **Step3 integrability and scaling:** For F=E Z finite and positive, (Z/F)^r<=rZ/F+1-r has integrable right side of expectation1. Nonnegative left side is thus integrable, permitting E(Z/F)^r<=1 and multiplication by F^r. F=0 remains Z=0 almost surely. No circular assumption of fractional integrability.

## L:gaussian-trace-bounds

Full old/new statements and proofs read; statements exactly equal. New proof LF92–151.

- **Roadmap and fixed eigenbasis:** Finite Hermitian Y is diagonalized; B and D are represented in that basis. A unitary representation of D supplies its diagonal entries without simultaneous diagonalization or commutation.
- **Step1 expanded entry calculation:** The ith diagonal entry of B Y^q B Y^(L-q) sums b_ij lambda_j^q b_ji lambda_i^(L-q). Hermitian symmetry gives |b_ij|^2; real eigenvalues and integer powers ensure real summands, including negative eigenvalues.
- **Step1 scalar weights/index swap:** After absolute values, weight q/L multiplies |lambda_j|^L and (L-q)/L multiplies |lambda_i|^L. Swapping finite indices in the first sum preserves |b_ij|^2 by Hermitian symmetry. (B^2)_ii=sum_j|b_ij|^2 identifies both unweighted sums with Tr(B^2|Y|^L); weights sum1. Noncommuting factors are not reordered.
- **Step2 row/column sums and convexity:** For each i, |U_ij|^2 are nonnegative weights of sum1 with weighted mean d_i. Averaging t^m>=s^m+m*s^(m-1)*(t-s) at s=d_i,t=theta_j cancels the linear term. Summation over i then uses column sums1 for equality with Tr D^m; it does not assert equality in Jensen.
- **Step2 explicit Holder factors:** Scalar Holder with conjugates m,m/(m-1) gives (sum d_i^m)^(1/m) and (sum |lambda_i|^(2m))^((m-1)/m), since(2m-2)*m/(m-1)=2m. Positivity of D, m>=2 and zero sums remain exactly as stated. No operator Holder or extra spectral domain is assumed.

## P:finite-gaussian-matrix

Full old/new statements and proofs read; statements exactly equal. New proof LF182–281.

- **Roadmap/headings:** Hermitian estimate precedes rectangular dilation, with three matching steps; endpoint m=1 is separate. No stronger moments or dimension/covariance assumptions are introduced.
- **Step1 Gaussian density/sign/boundary explanation:** For fixed other coordinates, standard Gaussian density derivative is -g_k times density. Integrating -P times this derivative by parts gives +partial_k P. Polynomial times Gaussian tends to zero at both infinities. Prior absolute polynomial integrability justifies Fubini; complex polynomials remain treated by real/imaginary parts.
- **Step2 ordered product rule:** partial_k Y=B_k. Differentiating Y^(2m-1) produces Y^q B_k Y^(L-q),q=0..L,L=2m-2; leading B_k is retained from Tr(B_k Y^(2m-1)). This preserves noncommutative order and exactly2m-1 terms.
- **Step2 first two inequalities and sums/expectation:** Finite sums and integrable polynomials allow linearity of expectation. Pointwise trace-word bounds sum k to D=sum B_k^2 and q to2m-1. Pointwise scalar trace Holder then permits deterministic (Tr D^m)^(1/m) outside expectation. No eigenbasis random selection/differentiation is required.
- **Step2 positivity/fractional bound:** Hermitian B_k gives B_k^2>=0, hence D>=0. Tr|Y|^(2m)=Tr Y^(2m)>=0 with finite expectation F. Scalar expectation estimate applies to r=(m-1)/m in(0,1) for m>=2, retaining the correct inequality direction.
- **Step2 division and exponent:** F>0 division gives F^(1/m)<=(2m-1)*(Tr D^m)^(1/m). Raising nonnegative sides to m yields(2m-1)^m Tr D^m. F=0 remains separate; no division by Tr D^m or assumption it is positive.
- **Step2 m=1 endpoint expansion:** E g_k g_l=0 for k!=l by centering/independence, and E g_k^2=1. Thus E Y^2=sum B_k^2 before trace, proving the equality. No Gaussian higher-moment recursion is substituted.
- **Step3 block calculations:** B_k Hermitian dilation squares to diag(A_k A_k*,A_k* A_k); summed squares give D. Y^2=diag(XX*,X*X); its mth power is Y^(2m) with corresponding powered blocks. All are finite square blocks although o and n may differ.
- **Step3 equal block traces/factor2:** Rectangular trace cyclicity gives Tr(XX*)^m=Tr(X*X)^m for m>=1. Their sum is2 times Schatten pth power. Substitution into Hermitian estimate divides by2 before p=2m root, yielding sqrt(p-1) and the average of both variance powers. Maximum bound and equality atp=2 are unchanged; no dimensional factor is introduced.

## Read limits

- Only the first three assigned complete statement/proof pairs are adjudicated. Other diff portions are not certified.
- This fresh comparison does not rely on the earlier118de5f7 QA disposition.
- No map contents, rendered PDF, Lean correspondence, cited external literature, or independent review grade audited. map_tip/hash are recorded from supplied INPUTS.json only.
- No source edits/repairs, Git operations, builds/tests, provider calls or literature calls.
