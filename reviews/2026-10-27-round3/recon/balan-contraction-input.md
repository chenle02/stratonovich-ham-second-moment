# Balan static contraction input: exact estimate and open transfer boundary

Date: 2026-10-27. Source extraction only; no new moment bound is asserted.
This supplements `literature-crosswalk.md` and does not modify the manuscript.

## Pinned source and hypotheses

Raluca M. Balan, *Stratonovich Solution for the Wave Equation*, J. Theoret.
Probab. 35 (2022), 2643–2689, DOI10.1007/s10959-021-01144-y.
The publisher PDF at
`../SPDEForge/sources/balan-22-stratonovich/balan-22-stratonovich.pdf`
has SHA-256
`ca4a52ae68340516f7c2f3dccf4f7fe8fc39cfde569be841df1b082777187d2c`.
It is byte-identical to the local canonical Balan PDF checked in the preceding
crosswalk. Numbering below is **published**, not inferred from TeX labels.

The relevant hypotheses are:

- d=1 or2; wave operator partial_t²−Delta, Green kernel of mass t;
- data u(0,x)=1 and partial_t u(0,x)=0;
- centered **time-independent** Gaussian spatial field;
- nonnegative, nonnegative-definite spatial covariance gamma;
- Assumption A, p2644: gamma is symmetric, continuous in its extended-valued
  sense, finite exactly off zero; spectral measure mu is absolutely continuous;
- condition (C), p2645:
  K_mu = integral (1+|xi|²)^(-1/2) mu(dxi) < infinity;
- source (3), p2645 uses C_t=2sqrt(2)(t∨1) in
  |Fourier G(t)(xi)| <= C_t (1+|xi|²)^(-1/2).

For homogeneous Riesz gamma, (C) requires alpha<1. This input therefore does
not cover the spatial-white delta case, general spectral measures without
Assumption A, dimension3, or fractional-time noise. The source also has a
separate easier finite-mu discussion; it must not be used to erase the above
hypotheses of Theorems3.2–3.3.

## Indexing and actual trace kernel

Use r for the source's contraction index k, to avoid confusing it with the
project's total pair count. Let n>=1, 0<=r<=floor(n/2), and m=n−2r.
Choose J subset {1,...,n}, |J|=m. Let P be an unordered pair partition of J^c,
with r pairs {ell_i,q_i}. Write T_n(t)={0<s_1<...<s_n<t}, s_(n+1)=t,
x_(n+1)=x. The source's unsymmetrized deterministic trace kernel is

```text
A_(n,r,J,P)((x_j)_(j in J);t,x)
 = integral over T_n(t) ds
   integral over (R^d)^(2r) dx_(J^c)
   product_(l=1)^n G(s_(l+1)−s_l, x_(l+1)−x_l)
   product_({ell,q} in P) gamma(x_ell−x_q).
```

All time variables are integrated here because the source noise depends only
on space. This fact changes in a fractional-time transfer.

Published Theorem3.2, (32), p2657, and the stochastic-Fubini identities/kernel
definitions on p2658 give

```text
H_n(t,x) = sum_(r,J,P) I_(n−2r)(A_(n,r,J,P)(.;t,x)).
```

Here H_n is an original **Stratonovich order**, not a Wiener-chaos projection.
I_m automatically uses the symmetrization of A. The norm is the spatial noise
Hilbert tensor norm H^(tensor m), whose Fourier form is displayed in the
proof on p2661. For m=0 the kernel and Hilbert norm are scalar.

## The exact deterministic norm bound

The load-bearing conclusion is source **(38), p2663**:

```text
||A_(n,r,J,P)(.;t,x)||_(H^(tensor (n−2r)))²
 <= (t^n/n!) K_mu^n C_t^(2(n−r))
       [2^r t^(n+2r)/(n+2r)!]
  = 2^r K_mu^n C_t^(2(n−r)) t^(2n+2r)
       / [n! (n+2r)!].                                  (B-38)
```

The bound is uniform in J, P and x. For t<=T it may be replaced by its
monotone T envelope. The factors are explicit; no n- or r-dependent constant
is hidden. C_t and K_mu are as above, not scale-free homogeneous constants.
The printed calculation ends with an equality after spectral upper bounds;
only the resulting inequality (B-38) is used here, not an asserted equality
between the weights (1+|xi|²)^(-1) and (1+|xi|²)^(-1/2).

The proof mechanism, checked in the published pp2661–2663, is:

1. Fourier trace variables identify xi_(ell_i)=−xi_(q_i)=eta_i.
2. For each closing endpoint q_i, use |Fourier G(delta s)|<=delta s,
   leaving a squared time increment after the Hilbert norm is taken.
3. Apply weighted Cauchy–Schwarz/Hölder with a finite measure built from
   the opening-endpoint Fourier factors. Its mass is at most
   (t^n/n!) C_t^r K_mu^r.
4. Integrate remaining frequencies successively using shifted spectral
   suprema and source Lemma4.1 of its reference[2]. The retained rows each
   introduce a new frequency; the closing rows have been discarded.
5. The remaining time-simplex integral is exactly
   integral_(T_n(t)) product_i(s_(q_i+1)−s_(q_i))² ds
   =2^r t^(n+2r)/(n+2r)!.

This exposes precisely where static-time integration and the pattern of
opening/closing contraction endpoints enter. It is not merely a count of
all pair partitions.

## Combinatorial consumer, including p=2

For a fixed r there are

```text
N_(n,r) = binom(n,2r) (2r)!/(2^r r!)
        = n! / [(n−2r)! 2^r r!]
```

choices of (J,P). Theorem3.3 proof, **p2666**, applies Minkowski and Gaussian
hypercontractivity to obtain the exact pre-simplification estimate

```text
||H_n(t,x)||_p
 <= sum_(r=0)^floor(n/2)
      N_(n,r) (p−1)^((n−2r)/2) sqrt((n−2r)!)
      sqrt( 2^r K_mu^n C_t^(2(n−r)) t^(2n+2r)
                 / [n! (n+2r)!] ),             p>=2.     (B-p)
```

For **p=2**, the (p−1) factor is one; every other factorial remains. One
must not replace N_(n,r) by1 or treat H_n as orthogonal across n. The same
page then relaxes the sum to a compact-time bound with denominator (n!)^(1/4),
using C_(p,mu,T)=(p−1)K_mu C_T² T(T∨1)^(3/2). This is its summability input,
not a sharp homogeneous asymptotic coefficient estimate.

The source's Section6.1, **pp2679–2680**, groups the final solution by Wiener
chaos degree m:

```text
K_0(t,x) = E v(t,x),
K_m(t,x) = sum_(n>=m, n−m even) sum_(J,P with r=(n−m)/2)
              I_m(A_(n,r,J,P)(.;t,x)),       m>=1.
v(t,x) = sum_(m>=0) K_m(t,x).
```

This is the source-backed grouping lead. Summing kernels within each degree
before taking a norm is different from the termwise triangle bound (B-p).
No assertion is made here that such grouping produces the missing factorial
power alpha0 in the present model.

## Named open transfer obligation: TTRACE

A fractional-time analogue must leave **both time and space coordinates** of
unpaired vertices free. Put z=(s,y) and
R(z,z')=|s−s'|^(−alpha0) gamma(y−y'). A candidate partial trace would be

```text
A^(alpha0)_(n,r,J,P)(z_J;t,x)
 = integral dz_(J^c) g_n(z_1,...,z_n;t,x)
     product_({ell,q} in P) R(z_ell,z_q).
```

This formula is only the **proposed interface**, with regularization and
membership in the space-time noise Hilbert tensor power still to be proved.
It is not an imported Balan theorem. In particular, integrating away the
unpaired times as in the static A would change the kernel/space and is invalid.

TTRACE has three explicit parts:

- **TTRACE-definition:** establish the partial traces and their space-time
  Hilbert membership, with a source-faithful limiting construction.
- **TTRACE-estimate:** prove an explicit bound B_(n,r)(t) for
  ||A^(alpha0)_(n,r,J,P)||², uniform in J,P and the regularizations. All
  temporal internal-pair factors and the temporal factors in the Hilbert
  norm must remain represented. The static B-38 is the calibration at
  alpha0=0, not the desired transferred answer.
- **TTRACE-consumer:** audit the fully counted sum
  sum_r N_(n,r) sqrt((n−2r)!) sqrt(B_(n,r)(t)), or a legitimately sharper
  grouped-kernel norm. To reach G:upper by this original-order route, a
  sufficient *unproved* envelope would have the form
  C^n t^(beta n/2)/(n!)^((3−alpha)/2), beta=4−alpha−alpha0, up to
  exponential-in-n factors. That is a target for testing, not a theorem
  assumed into the proof. The static source does not supply this envelope.

[held back: collaborators' unpublished work]

## Bounded check for a first-moment comparison

No theorem comparing ||H_n||_2 directly with E H_(2n), or comparing E v² with
a noise-amplified first moment, was found in the inspected source. What is
actually supplied is B-38/B-p and the identity K_0=E v. I checked
Theorems3.2–3.4, the Section6.1 formulas, and searches in the complete local
TeX for first-moment/Jensen/expectation/mean terminology and H_(2n) patterns.
This is a bounded negative search, not proof that no such inequality exists
elsewhere or can be derived. Any proposed comparison must be tested on the
project's G1 coefficients before investment.

## Evidence and limitations

Selected publisher pages are retained in `balan-source-snippets/`; their
hashes, PDF provenance and checked equation/page map are recorded in
`balan-contraction-receipt.json`. The source PDF itself is unchanged.
The extraction was checked against rendered formulas and the corresponding
local TeX; it is not a fresh proof audit of every Fourier/trace lemma in Balan.
TTRACE is open and has not been independently reviewed, formalized or used
to claim G:upper. No new result is proved in this report.
