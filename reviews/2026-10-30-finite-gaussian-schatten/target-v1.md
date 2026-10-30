# Finite Gaussian matrix moments: proposed independent ingredient

UNREVIEWED statements before long proof. Finite-dimensional ONLY; no
continuum/operator-valued Gaussian series or original-noise theorem.
All Schatten norms use UNNORMALIZED trace. Real independent standard
Gaussians g_1,...,g_N, arbitrary fixed complex matrices A_k of size o x n,
positive integer o,n,N. X=sum g_k A_k, Vout=sum A_k A_k*, Vin=sum A_k* A_k.
For even p=2m>=2, ||A||_Sp^p=Tr((A*A)^m).

N1. Prove the finite inequality
 (E||X||_Sp^p)^(1/p)
 <=sqrt(p-1)*[(Tr(Vout^m)+Tr(Vin^m))/2]^(1/p)
 <=sqrt(p-1)*max(||Vout^(1/2)||_Sp,||Vin^(1/2)||_Sp).
No dependence on o,n,N. p2 equality in the FIRST inequality. Zero matrices
trivial. No noncommutativity, realmatrix or squarematrix restriction.

Proposed self-contained route (not yet proved): Hermitian dilation
Y=sum g_k B_k, B_k=[[0,A_k],[A_k*,0]], D=sum B_k^2=diag(Vout,Vin).
Tr(Y^(2m))=2Tr((X*X)^m), by rectangular trace cyclicity and powers.
For m>=2, Gaussian polynomial IBP should give
 F=ETr(Y^(2m))
   =sum_k sum_(q=0)^(2m-2) ETr(B_k Y^q B_k Y^(2m-2-q))
   <=(2m-1)ETr(D |Y|^(2m-2)).
Finite trace Holder plus expectation Holder/Jensen yields
 F<=(2m-1)(Tr D^m)^(1/m) F^((m-1)/m), with F0 case explicit.
Prove all finite identities/inequalities, not quote an unverified external
noncommutative theorem. Spectral theorem/finite sum calculus is elementary
background; scalar trace inequalities can be derived in an eigenbasis.
Treat m1 separately so no division by m-1 or 0^0 ambiguity is hidden.

N2. The required finite scalar inequality: for natural L>0,0<=q<=L,
x,y real,
 |x|^q |y|^(L-q) <= (q/L)|x|^L+((L-q)/L)|y|^L.
Here ratios are REAL casts, integer exponents. Zero endpoints/q0/qL are
explicit. Possible standalone local Lean seam after statement gate; it
would formalize THIS finite inequality only, not Gaussian/operator claims.
No official package/companion creation authorized by this target.

N3. Explain necessity of retaining BOTH variance sides in this general
finite estimate. For A_k=e_k^T, k1..16 (1x16 row), p4,
E||X||_S4^4=16*18=288, while the input-only proposed upper is9*16=144.
Transpose to16x1 to refute output-only upper. Use elementary Gaussian
moments Eg^2=1,Eg^4=3 and independence, not a numerical simulation.
This concerns the finite matrix inequality, not impossibility of any
special actual wave variance bound.

Falsification code contains12 finite polynomial Hermite quadrature rows
(scalarcomplex/noncommutingHermitian/rectangularcomplex,p2/4/6/8), plus
both negative controls. Quadrature floating arithmetic is not proof.
No non-evenp assertion, Gaussianpath/Schattenseries, sourcecutoff/Young/
PDE/noise comparison or newmoment/sourceconstant result. Original full
all-dimensional sharp/source goal ACTIVE. Actual wave-variance target has
an independent pending gate and is not assumed or consumed here. No
external theorem/literature or new Lean proof imported, no sourcefix/
Skorohod/contact/HPC/newcompanion/TeX/PDF/wiki/publication/circulation.
