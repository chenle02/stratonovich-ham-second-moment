# Finite Gaussian matrix moments with both variance directions

COMPLETE CANDIDATE, not adopted before independent full proof review.
This note is FINITE dimensional. It constructs no actual Gaussian operator,
Schatten-valued series or path and proves no new SPDE moment asymptotic.

## 1. Precise finite statement

Let A_1,...,A_N be complex o-by-n matrices, with positive finite o,n,N.
Let g_k be independent real standard Gaussians, and set

 X=sum_k g_k A_k,
 Vout=sum_k A_k A_k*,       Vin=sum_k A_k* A_k.

All traces are UNNORMALIZED. For even p=2m>=2 define
||A||_Sp^p=Tr((A*A)^m), using ordinary integer matrix powers.

**Theorem 1.**

 (E||X||_Sp^p)^(1/p)
 <=sqrt(p-1)*[(Tr(Vout^m)+Tr(Vin^m))/2]^(1/p)
 <=sqrt(p-1)*max(||Vout^(1/2)||_Sp,||Vin^(1/2)||_Sp).                (1)

The constant sqrt(p-1) is independent of o,n,N. The variance traces can
depend on those sizes. The FIRST inequality is equality for p=2. Zero
matrices cause no division problem. No commutativity, square-matrix or
real-coefficient restriction is imposed.

The proof is self-contained apart from elementary finite Hermitian
spectral diagonalization and basic scalar calculus. In particular no
external noncommutative Gaussian theorem is being imported. Scalar and
trace inequalities used below are derived explicitly.

## 2. Scalar weighted powers and scalar Holder

For 0<theta<1 and u,v>=0,

    u^theta v^(1-theta)<=theta u+(1-theta)v.                        (2)

If v>0, divide by v and put t=u/v. The function
f(t)=theta t+1-theta-t^theta has derivative theta(1-t^(theta-1)) on
(0,infinity), negative below1 and positive above1. Its minimum is f(1)=0.
Continuity handles t=0. If v=0 the inequality follows directly. We use
theta=0 or1 only as the trivial equality with the corresponding term,
so no analytic limit involving 0^0 is needed.

In particular, for natural L>0 and 0<=q<=L, real x,y,

 |x|^q |y|^(L-q)
   <= (q/L)|x|^L + ((L-q)/L)|y|^L.                                (3)

Here all exponents are natural, and both ratios are REAL casts. For q=0
or q=L this is equality, including zero bases and the convention a^0=1.
For 0<q<L, apply(2) to u=|x|^L,v=|y|^L,theta=q/L; positive bases obey
ordinary real-power multiplication, and zero bases give the same conclusion
directly. The cast of L-q equals L-q in the reals because q<=L. Thus(3)
has no hidden extension to q>L or L=0.

For completeness scalar Holder for finite nonnegative sequences with
exponents m and m/(m-1), m>1, follows from(2). Normalize each sequence by
its corresponding positive power sum; if either norm is zero the desired
inequality is immediate. Apply(2) with theta=1/m to the m-th power of the
first normalized entry and the m/(m-1)-th power of the second. Summing
gives the product sum at most1, and undoing the normalization proves
Holder. Likewise if Z>=0 has finite expectation F and 0<r<1, then

    E Z^r <= F^r.                                                 (4)

If F=0 then Z=0 almost surely. If F>0, apply(2) to u=Z/F,v=1,theta=r,
then integrate; the right side has expectation1. These arguments identify
both the finite scaling and the expectation step used later.

## 3. A Hermitian trace inequality

Let B,Y be Hermitian M-by-M matrices. Put L=2m-2>0 for m>=2, and let
q be an integer with 0<=q<=L. Then

 Re Tr(B Y^q B Y^(L-q)) <=Tr(B^2 |Y|^L).                           (5)

Diagonalize Y, with real eigenvalues lambda_i, and write b_ij for B in
that orthonormal eigenbasis. Hermitian symmetry gives b_ji=conj(b_ij).
The trace on the left is the real sum

    sum_ij |b_ij|^2 lambda_j^q lambda_i^(L-q).

Each product is at most |lambda_j|^q |lambda_i|^(L-q). Apply(3), then
sum with nonnegative weights |b_ij|^2. The two resulting sums, weighted
by q/L and (L-q)/L, are equal: interchange i and j and use
|b_ij|=|b_ji|. Either sum is

 sum_ij |b_ij|^2 |lambda_i|^L =Tr(B^2 |Y|^L).

The weights add to1. This proves(5), including q=0,L. No assertion that
B and Y commute was made; the trace was evaluated in Y's eigenbasis.

We also need a two-matrix trace Holder bound. If D>=0 is Hermitian and
Y Hermitian, then

 Tr(D |Y|^(2m-2))
   <=(Tr D^m)^(1/m) (Tr |Y|^(2m))^((m-1)/m), m>=2.                (6)

In Y's eigenbasis write d_i=D_ii>=0. If theta_j>=0 are D's eigenvalues,
then d_i=sum_j |U_ij|^2 theta_j for a unitary change of basis. BOTH row
and column sums of |U_ij|^2 are1. Convexity of t->t^m gives

    sum_i d_i^m<=sum_ij |U_ij|^2 theta_j^m=Tr D^m.                 (7)

This finite convexity step can be checked directly: for t,s>=0,
t^m>=s^m+m s^(m-1)(t-s), by the sign of the derivative of the difference;
s=0 is immediate. Multiply by normalized nonnegative weights and take
s equal to their weighted mean. This proves the finite convex-power
inequality used in(7). Thus the two eigenbases are handled explicitly.

Now Tr(D |Y|^(2m-2))=sum_i d_i |lambda_i|^(2m-2). Apply the finite
scalar Holder proved in Section2, then(7). Since
(2m-2)*m/(m-1)=2m, this gives exactly(6). Zero sums are already covered by
the scalar argument. This proves all trace inequalities needed below.

## 4. Gaussian integration by parts and the finite moment bound

First let B_k be arbitrary Hermitian matrices, Y=sum g_k B_k, and
D=sum B_k^2>=0. Every entry of Y is a linear Gaussian polynomial, so all
polynomial moments below are finite: Gaussian density dominates each
fixed power at infinity. Componentwise integration by parts against the
one-dimensional standard Gaussian density has zero boundary term for
polynomials and gives E[g_k P(g)]=E[partial_k P(g)]. Fubini is legitimate
by absolute polynomial integrability.

For m>=2 put F=ETr(Y^(2m))>=0 and L=2m-2. Since Y=sum g_k B_k,
product differentiation and that Gaussian identity give EXACTLY

 F=sum_k sum_(q=0)^L ETr(B_k Y^q B_k Y^(L-q)).                      (8)

Indeed Tr(Y^(2m))=sum_k g_k Tr(B_k Y^(2m-1)), and differentiating the
2m-1 factors of Y gives the displayed ordered terms, once each. No
commutations or derivative of a spectral absolute value are involved.
These traces are real by the eigenbasis expression of Section3.
Equation(5) therefore yields

 F <= (2m-1) ETr(D |Y|^(2m-2))
   <= (2m-1)(Tr D^m)^(1/m) E[(Tr |Y|^(2m))^((m-1)/m)]
   <= (2m-1)(Tr D^m)^(1/m) F^((m-1)/m).                           (9)

The second line uses(6) and the last uses(4). Hermitian even powers give
Tr |Y|^(2m)=Tr Y^(2m), so the expectation in(4) is indeed F. If F=0 the
result below is immediate. Otherwise divide by its positive fractional
power and raise to m, obtaining

    ETr(Y^(2m)) <= (2m-1)^m Tr D^m.                               (10)

For m=1, directly ETr(Y^2)=sum_k Tr(B_k^2)=Tr D using independence and
Eg_k g_l=delta_kl. This is equality in(10) at m=1, without a division
by m-1 or a scalar trace inequality with L=0.

For general rectangular A_k, apply this Hermitian result to

 B_k=[[0,A_k],[A_k*,0]],      Y=[[0,X],[X*,0]].

Block multiplication gives D=diag(Vout,Vin). For every m>=1,

 Tr(Y^(2m))=Tr((XX*)^m)+Tr((X*X)^m)=2Tr((X*X)^m),
 Tr(D^m)=Tr(Vout^m)+Tr(Vin^m).                                    (11)

To check the rectangular trace identity, ordinary entrywise finite sums
give Tr(UV)=Tr(VU) for compatible rectangular U,V. Also
(XX*)^m=X(X*X)^(m-1)X* by induction. Apply that trace identity to conclude
the two traces agree; no equality of the ambient dimensions is assumed.
Substitute(11) in(10), divide by2 and take the p=2m root. This proves
the first inequality of(1). For positive V,
||V^(1/2)||_Sp^p=Tr V^m by spectral diagonalization, so the average of
the two trace powers is at most their maximum. This proves the second.
For p=2, ETr X*X=Tr Vin=Tr Vout, giving the claimed FIRST equality.
This proves Theorem 1.

## 5. Both variance directions: explicit negative controls

Let n=16 and A_k=e_k^T, k=1,...,16. X is a real Gaussian row, with its
only nonzero singular value equal to (sum g_k^2)^(1/2). Consequently

 E||X||_S4^4=E(sum g_k^2)^2
   =sum_k Eg_k^4+sum_(k!=l)Eg_k^2 Eg_l^2
   =3n+n(n-1)=n(n+2)=288.

Here Eg^2=1 and Eg^4=3 follow by elementary one-dimensional Gaussian
integration by parts applied to g and g^3; Eg^0=1. Independence gives
the mixed moments. Vout=n as a scalar, whereas Vin=I_n. The proposed
p4 bound with ONLY Vin would have fourth power9 Tr Vin^2=144, which is
false. For the transposed column family Vout=I_n and Vin=n, so dropping
the input variance gives the same false bound. This establishes the
necessity of retaining both sides in this general finite estimate with
the stated constant. It does not refute any specialized wave estimate.
The correct maximum bound has fourth power2304; the stronger average
bound in(1) has fourth power1224. Both exceed288.

## 6. Verification boundaries and actual project use

The finite diagnostics check complex scalar coefficients, a noncommuting
Hermitian family (the identity member itself commutes), and complex
rectangular matrices, at p2/4/6/8. Hermite quadrature uses standard-Gaussian
sqrt2 scaling and1/sqrtpi weights, with orderm+1 motivated by polynomial
degree. Floating precision50 is not a certified proof of integration
accuracy. v1 checks the MAX bound only; an average-bound supplementary
check, if supplied, is still just a finite control. The negative controls
are analytic moment prescriptions, not sixteen-dimensional simulations.

The standalone local Lean consumer of pinned Mathlib's weighted AM-GM checks
ONLY the natural-power/cast inequality(3). Its actual compile, audit,
controls and replay status must be read from the local receipt. It compiled,
audited and freshly replayed with all five owned artifacts matching and
three false-statement controls. Exact type/application fidelity still needs
the present independent full gate. An earlier private/server byte mismatch
is preserved; the public statement was unchanged in the successful proof
refactor. No Gaussian
IBP, Hermitian spectral/trace step, actual continuum variance, Schatten
series, time path or SPDE result is certified by that finite consumer.

Application still requires actual TWO operator variance directions, correct
physical/Sobolev localization and compact singular-value estimates, then
actual Gaussian series/cutoff convergence and time paths. The separate
actual-wave variance proof has its own gate and is not an input here.
The original full all-dimensional lower/sharp upper/source objective remains
ACTIVE. No new source-energy identity, exact limit, Skorohod work, contact,
HPC, private companion, canonical TeX/PDF/wiki edit or public release or
whole-paper/cold-reader clearance follows from this finite note.
