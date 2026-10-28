# Complete operator bridge for the interval coefficient candidate

Status: UNREVIEWED extension/application,not part of the accepted static
report. The exact external input is the bounded-Hilbert spectral-set
inequality CPv1(3)/Theorem6. Its full actual source is supplied separately.

## General complex potential (no selfadjointness assumption on V)

Let A0 be bounded nonnegative selfadjoint,on a complex Hilbert space,
A_rho=rho²+A0. Suppose V is bounded and
||A_rho^{-1/2}V A_rho^{-1/2}||<=D rho^{a-2}for allrho>0,0<a<1.
Let I_a anddelta_a be as in the static complex lemma,and assume
D<=delta_a Lambda^{2-a}. Put L=A0-V,L_Lambda=L+Lambda².

For kappa=sqrt(Lambda²+t),K_kappa=A_kappa^{-1/2}V A_kappa^{-1/2}
has norm<=delta_a. Factor
L_Lambda+t=A_kappa^{1/2}(1-K_kappa)A_kappa^{1/2}.
It is accretive with real part>=(1-delta_a)A_kappa.
The resolvent difference is exactly
 A_kappa^{-1/2}(1-K_kappa)^{-1}K_kappa A_kappa^{-1/2}.
After multiplying by A_Lambda^{1/2},its norm is at most
D kappa^{a-3}/(1-delta_a).
The norm-convergent principal inverse-root integral consequently gives
 ||A_Lambda^{1/2}L_Lambda^{-1/2}-1||
 <=D Lambda^{a-2} I_a/[pi(1-delta_a)]<=1/6.
This integral follows from the scalar half-plane resolvent identity and
bounded holomorphic calculus;at the spatial band A_Lambda^{1/2}is bounded.
The norm hypothesis for V* is identical to that for V. Applying the same
argument to the adjoint and taking inverses gives norm<=2 for all four:
 A_Lambda^{1/2}L_Lambda^{-1/2},
 L_Lambda^{-1/2}A_Lambda^{1/2},
 L_Lambda^{1/2}A_Lambda^{-1/2},
 A_Lambda^{-1/2}L_Lambda^{1/2}.

For ||u||1,s=||A0^{1/2}u||,the rho=Lambda REAL-PART estimate gives
Re<L u,u>+Lambda²>=(1-delta_a)(s²+Lambda²).
Separately,optimizing the all-rho form estimate at rho=s gives
|<V u,u>|<=2D s^a (rho->0if s0).
Thus,for w=x+iy in numerical range,
 y²<=[4delta_a²/(1-delta_a)]Lambda²(x+Lambda²)
    <=Lambda²(x+Lambda²)/3, and x>=-Lambda²/4.
Therefore |w|<=x+2Lambda² and |Im sqrt(w)|<=Lambda.

Use C_h(w)=cos(h sqrt w),
F_h(w)=sqrt(w+Lambda²)sin(h sqrt w)/sqrt w,
H_h(w)=w sin(h sqrt w)/(sqrt(w+Lambda²)sqrt w).
The only branch is sqrt(w+Lambda²),in a strict right half-plane;the values
atw0are removable. Their suprema on numerical range are bounded by
e^{Lambda h},2(1+Lambda h)e^{Lambda h},2e^{Lambda h}.
CP then gives operator bounds3,6(1+Lambda h),6 times e^{Lambda h}.
Whitening the phase bydiag(1,A_Lambda^{-1/2})gives the four blocks
 C_h(L),
 F_h(L)L_Lambda^{-1/2}A_Lambda^{1/2},
 -A_Lambda^{-1/2}L_Lambda^{1/2}H_h(L),
 A_Lambda^{-1/2}L_Lambda^{1/2}C_h(L)L_Lambda^{-1/2}A_Lambda^{1/2}.
The root comparisons give norm<=100e^{2Lambda h}.
This proves the general complex-potential bound at BOUNDED cutoffs.

## Any admissible spatial dimension and a fresh-color creation bound

Let Gamma>=0be even PD homogeneous Radon onR^d,d1/2/3,with original
alpha range and spectral mu. Homogeneity yields mu(B_r)=r^alpha mu(B1).
For rho>0,Gaussian Fourier pairing and physical nonnegativity give
 int exp(-s|eta+xi|²)mu(dxi)<=int exp(-s|xi|²)mu(dxi).
Integrating exp(-rho²s)ds yields the shifted resolvent boundRrho^{alpha-2},
with R=alpha*pi*mu(B1)/(2sin(pi alpha/2)).
No condition Gamma({0})0 is used;d1white space is included.

Take W_epsilon=W(p_epsilon(x-dot)),covariance p_{2epsilon}*Gamma,
and a real orthonormal Gaussian basis g_m with deterministic coefficients
e_m(x). Then sum_m e_m(x)²=v_epsilon<infinity. With M_m multiplication
by e_m,the exact Gaussian/Plancherel identity is
 sum_m||A_rho^{-1/2}M_m f||²
 =(2pi)^{-d}int J_{rho,epsilon}(eta)|fhat(eta)|²deta
 <=Rrho^{alpha-2}||f||².
The same holds tensor any other Hilbert factor.
Replacing f byA_rho^{-1/2}f gives
sum_m(A_rho^{-1/2}M_m A_rho^{-1/2})²<=Rrho^{alpha-4}I.
Finite mode sums and Fourier-band compressions preserve these positive
operator inequalities.

For a Gaussian color not yet used,the phase creation map
 (u,v)->sum_m g_m(0,M_m u)
has squared norm<=Rrho^{alpha-2}||(u,v)||_{X_rho}².
It is a map from the other Hilbert factors to their tensor product with
this color's first Gaussian chaos. It is NOT asserted bounded on inputs
already depending on this color. This is exactly the situation for a
cross singleton whose amplitude coefficient is linear on each copy.

For a repeated color,use normalized Hermites and truncate its total degree
atN. For the selfadjoint spatial sandwiches H_m above,the creation-row
identity on degreej is CC*=(j+1)I. Composition with the column(H_m)gives
creation norm<=sqrt(j+1)sqrt(R)rho^{a-2}. Truncated annihilation is its
adjoint. Hence the sandwiched field norm is
<=2sqrt(N+1)sqrt(R)rho^{a-2}.
This remains true with identities on all other Gaussian factors.

For multiple interval colors at local degreesN_i,therefore
 ||A_rho^{-1/2}sum_i z_i sigma_i B_i A_rho^{-1/2}||
 <=[sum_i |z_i|sigma_i 2sqrt(N_i+1)sqrt(R)]rho^{a-2}.
Its adjoint has the same bound. The preceding general complex-potential
proof applies to the sum whenever that bracket is<=delta_a Lambda^{2-a}.

## Existence and cutoff identification for a finite interval inventory

At fixed epsilon and finite inventory,the instantaneous variance of the
sum field is bounded by finite v_max. On total Hermite degrees<=n,the
unweighted field multiplication has norm<=2sqrt(n+1)sqrt(v_max),by the
same pointwise creation/annihilation estimate. A phase insertion has
X_lambda norm at most that number divided bylambda.
The nth Duhamel coefficient from the Gaussian vacuum is therefore bounded
by exp(lambda T/2)(2sqrt(n+1)sqrt(v_max)T/lambda)^n/n!times initial norm.
Its series is entire in the global noise amplitude,and locally entire in
all finitely many amplitudes. Energy double series converge absolutely.

Fixed-word Gaussian-mode and Fourier-band limits follow by strong
convergence and these finite-degree bounds. For finite-coordinate inputs,
the annihilation tail is zero and the creation tail is dominated by
sum_{m>M}e_m(x)²<=v_epsilon;dominated convergence applies.
Finite-coordinate inputs are dense,and multiplication by the actual
measurable W_epsilon is closed,so the limit is the ordinary product.
This identifies every finite-order coefficient with the actual finite
interval model. No uniformity of v_max in the inventory/epsilon is claimed
or needed for this identification;uniform coefficient bounds are proved
separately with R.

For a given energy multiindex k_i,the local cutoffN_i=2k_i is exact:
each partial word in either phase factor contains at most2k_i appearances
of that field. It does not delete any self-contraction or introduce
Wick renormalization. All claims still await independent adversarial review.
