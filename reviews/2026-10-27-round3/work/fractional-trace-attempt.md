# One fractional-time self-trace attempt: HLS and fixed-time Fourier estimates

Date: 2026-10-27. **Working derivation, not independently reviewed or promoted.**
This is one bounded mechanism attempt following `recon/balan-contraction-input.md`.
It obtains an explicit candidate estimate, diagnoses its loss, and stops at the
missing step. No target-scale theorem or Skorohod result is claimed.

## Outcome first

In d=1, for gamma(x)=c_alpha |x|^(-alpha), 0<alpha<1 and 0<a=alpha0<1,
the mechanism below is quantitatively usable in the narrower region

```text
alpha + (3/2)a < 2.                                      (R)
```

It retains the correct homogeneous factor t^(beta n/2), beta=4-alpha-a.
The free-time symmetrization is essential. After the exact contraction
multiplicity, its remaining factorial loss is exp(O(n)) times (r!)^a for
r self-pairs. Thus bounded-r sectors are compatible with the desired
factorial scale, but summing all r is not controlled at that scale. At
r=n/2 the loss reproduces the G0 exponent, not kappa. Region(R) is an
artifact of the Hölder step, not a new existence restriction.

The missing improvement cannot hold uniformly for each self-pair pattern:
the full-trace adjacent pattern below is an exact countertest. A sum retaining
pattern-dependent time spans is still open. No-go scope: this termwise
improvement only, not every trace-grouping or Theorem3.1 strategy.

## 1. Objects and imported analytic input

Use Balan's terminal-time convention:
0<s_1<...<s_n<t, s_(n+1)=t, h_i=s_(i+1)-s_i.
There is also the unused initial slack s_1; equivalently h_i>0 and sum h_i<t.
Let J contain m=n-2r unpaired labels and P partition J^c into r pairs
{ell_i,q_i} with ell_i<q_i. The unpaired (time,space) variables remain free.

At fixed full time vector s, let a_P(s) be the spatial kernel obtained by
integrating the 2r paired spatial variables against the r spatial covariances,
leaving the m unpaired spatial variables free. Let H_x be the spatial-noise
Hilbert space. The candidate space-time partial trace is obtained by integrating
w_P(s) a_P(s) over the contracted times, where

```text
w_P(s) = product_({ell,q} in P) (s_q-s_ell)^(-a).
```

This is a classical nonnegative Riesz kernel calculation, not a delta argument.
At fixed n the energy integral has disjoint covariance pair labels on two copies;
bounded d1 Green kernels and compact finite-time supports give an integrable
cube envelope for alpha,a<1. A regularized version can be used throughout;
passing to the exact partial trace still requires the usual Hilbert-energy
identification. No space-time Hilbert norm is replaced by a spatial norm.

Imported temporal input: Balan–Conus (2016), published Lemma B.3, (73),
journal p1531 (PDF page44), with H=1-a/2 and q=1/H=2/(2-a):

```text
integral phi(s)phi(u) product_(j=1)^m |s_j-u_j|^(-a) ds du
 <= D_a^m ||phi||_(L^q(R^m))².                            (HLS)
```

D_a=C_H from that lemma is finite and depends only on a. The kernel in (73)
has no H(2H-1) prefactor; none is inserted here. The source PDF hash is
`4fc3f73cc6164c1c9cc6a384ffdfb3389d21d34be1e86bcfbc681375a59d2756`.
This standard analytic inequality is imported read-only. Its r=0 moment
application is already known; no new Skorohod estimate is developed below.

## 2. Homogeneous spatial estimate at fixed times

Write mu(dxi)=nu_alpha |xi|^(alpha-1) dxi, with nu_alpha fixed by
c_alpha |x|^(-alpha)=integral exp(i xi x)mu(dxi). One may take
nu_alpha=c_alpha/[2 Gamma(alpha) cos(pi alpha/2)] in this convention.
The elementary wave estimate is

```text
|Fourier G(h)(xi)| <= sqrt(2) h/(1+h²xi²)^(1/2).
```

Using the maximum-at-zero bound for the convolution of the even decreasing
Riesz density with the Bessel weights gives

```text
sup_z integral |Fourier G(h)(z+xi)| mu(dxi)
 <= C1 h^(1-alpha),
C1 = sqrt(2) nu_alpha B(alpha/2,(1-alpha)/2),

sup_z integral |Fourier G(h)(z+xi)|² mu(dxi)
 <= C2 h^(2-alpha),
C2 = 2 nu_alpha B(alpha/2,1-alpha/2).
```

Both constants are finite in the declared alpha range. These are homogeneous
replacements of the coarse K_mu,C_t factors, not a citation of a sharper
printed Balan theorem.

Apply the fixed-time version of the Fourier trace argument behind Balan(38):
opening labels ell_i supply single Fourier factors; closing labels q_i are
bounded by h_(q_i); free labels supply squared factors in the Hilbert norm.
Weighted Cauchy–Schwarz in the r trace frequencies and successive integration
of the retained rows yield

```text
||a_P(s)||_(H_x^(tensor m))
 <= C1^r C2^(m/2)
    product_(ell in openings) h_ell^(1-alpha)
    product_(q in closings) h_q
    product_(j in J) h_j^(1-alpha/2).                    (S)
```

The row deletion/opening argument is the same as Balan pp2661–2663, but now
no time integration occurs in that spatial step. Only the fixed positive
h_i are used. This is where alpha<1, positivity and the Riesz shift estimate
enter. No bound is asserted at zero increments.

Since s_q-s_ell = h_ell+...+h_(q-1) >= h_ell, (S) gives

```text
w_P(s)||a_P(s)|| <= C1^r C2^(m/2) f_P(s),
f_P(s)=product_open h^(1-alpha-a)
        product_close h
        product_free h^(1-alpha/2).                    (L)
```

This loses the actual pair span: every internal temporal covariance is now
charged to the local opening increment. It is a valid upper bound, not an
identity except in adjacent cases.

## 3. Free-time symmetrization must precede the HLS estimate

Let F_P(s_J)=integral_(contracted times compatible with s_J) f_P(s) ds_(J^c),
zero unless the m free times are ordered. Spatial Minkowski and Cauchy–Schwarz
bound the space-time trace norm by the temporal energy of F_P.

The Wiener integral I_m uses symmetrization in **both** free time and space
coordinates. For distinct free times, the m! permuted ordered supports are
disjoint. Thus the scalar amplitude of the symmetrized kernel satisfies

```text
||Sym F_P||_q = (m!)^(1/q-1) ||F_P||_q
             = (m!)^(-a/2) ||F_P||_q.
```

Combining this with the Wiener isometry factor sqrt(m!) and (HLS), a
single (J,P) term is bounded by

```text
||I_m(A_P)||_2
 <= D_a^(m/2) C1^r C2^(m/2)
      (m!)^((1-a)/2) ||F_P||_q.                        (H)
```

For m=0 use the scalar interpretation and 0!=1. Omitting this symmetrization
would lose a factorial power a/2 even in the known r=0 input.

## 4. Actual Hölder/Dirichlet calculation

At fixed s_J, the domain of the 2r contracted times has volume at most
V=t^(2r)/(2r)!. Hölder gives

```text
||F_P||_q <= V^(1-1/q) [integral_(T_n(t)) f_P(s)^q ds]^(1/q).
```

Set e_o=1-alpha-a, e_c=1, e_f=1-alpha/2. The Dirichlet integral is

```text
integral f_P^q
 = Gamma(1+q e_o)^r Gamma(1+q)^r Gamma(1+q e_f)^m
    t^[n+q(n(1-alpha/2)-r a)]
   / Gamma(1+n+q(n(1-alpha/2)-r a)).
```

Its opening-gap integrability requires q e_o>-1, exactly region(R).
For example alpha=a=.9 satisfies the original condition alpha+a<2 but
violates(R); this attempt's Hölder integral then diverges even though that
does not imply divergence of the actual trace.

Since 1-1/q=a/2, all powers of t combine to beta n/2. Define

```text
G_(n,r) = Gamma(1+q(1-alpha-a))^r
          Gamma(1+q)^r
          Gamma(1+q(1-alpha/2))^m.
```

Equations(H) and the calculated integral give the explicit single-pattern bound

```text
||I_m(A_P)||_2 <=
 D_a^(m/2) C1^r C2^(m/2) G_(n,r)^(1/q)
 (m!)^((1-a)/2) t^(beta n/2)
 / { ((2r)!)^(a/2)
     Gamma(1+q(beta n/2-r a))^(1/q) }.                 (T)
```

Every n,r-dependent factor is displayed. Constants C1,C2,D_a depend only
on the fixed covariance parameters. This is the concrete outcome of the
attempt, subject to independent checking of the stated Hilbert-limit details.

## 5. Counted consumer and the remaining loss

For each r the number of trace patterns is
N_(n,r)=n!/[(n-2r)! 2^r r!]. Multiplying(T) by this count is the termwise
Minkowski consumer, not a statement about a single summed chaos kernel.
The Gamma factors G_(n,r) contribute only exp(O(n)) for fixed parameters
strictly inside(R).

For r/n tending to theta in [0,1/2], the coefficient of n log n in the
logarithm of this counted envelope is

```text
-(3-alpha)/2 + a theta.
```

Indeed its denominator factorial order is beta n/2; the numerator order
from N_(n,r)(m!)^((1-a)/2) is (1-a)n/2 + a r.
Equivalently, up to exponential-in-n factors, the residual relative to
(n!)^(-(3-alpha)/2) is (r!)^a. The explicit Gamma formula(T), rather than
this shorthand, is the auditable finite-n statement.

- At r=0 this agrees with the known fractional-time chaos input. It is a
  normalization check, not a new Skorohod theorem.
- For r bounded independently of n, the loss does not change the leading
  n log n coefficient. This only concerns a truncated self-trace sector,
  not the full Stratonovich solution.
- At r=n/2 the denominator has order (n!)^((3-alpha-a)/2), precisely the
  weaker G0 order. Thus this termwise mechanism does **not** prove G:upper,
  even where(R) holds.

## 6. Full-trace adjacent countertest

Take n=2r, m=0 and the adjacent matching
P={{1,2},{3,4},...,{2r-1,2r}} in one chain. The spatial integrals factor:
each opening increment gives c_alpha h^(1-alpha)/(1-alpha), each closing
increment gives its wave mass h, and the temporal pair gap is exactly the
opening increment. Direct Dirichlet integration gives

```text
A_adj(t) = [c_alpha Gamma(2-alpha-a)/(1-alpha)]^r
           t^(beta r)/Gamma(1+beta r).                 (A)
```

Checks: r=1 reproduces G1's E X_2 formula. Under
c_alpha=(1-alpha)/2 and alpha increasing to1, (A) becomes the white witness
[Gamma(1-a)/2]^r t^((3-a)r)/Gamma(1+(3-a)r); at r=2,a=0 this gives1/2880,
the G1 adjacent (0,4) entry.

Dividing a uniform per-pattern envelope of this factorial order by (r!)^a
would demand denominator order (r!)^(4-alpha) instead of the actual
(r!)^(4-alpha-a). Formula(A) contradicts such an improvement by Stirling.
There is only one adjacent pattern on this fixed chain, so this does not
contradict a stronger *sum* over patterns. It diagnoses the need to retain
pattern-dependent temporal spans rather than charging every pair locally
and multiplying the worst envelope by the entire count.

## 7. Exact missing step and stopping point

The attempt stops at the replacement of the counted per-pattern envelope
by a sharp bound on the summed self-trace kernels. An improvement must be
compatible with(A), exploit how rare the worst short-span patterns are,
and remain controlled in the L^q norm of the free times. The first-moment
result controls the completely contracted sum, but it is not an estimate
for partial-trace kernels with free time/space arguments.

No interpolation between fully contracted and uncontracted endpoints, no
trace-to-first-moment comparison, and no uniform factorial gain has been
assumed. None has been proved here. The mechanism is therefore a useful
loss diagnosis, not G:upper, a claim of a new regime, or a proof that all
trace-grouping methods fail. It should be independently reviewed before
any mathematical claim is promoted into the notes.

## 8. The fully contracted **sum** is already sharply bounded

This is stronger than the individual-pattern bound and must not be discarded.
For n=2r,m=0, summing every full-trace pattern gives exactly

```text
sum_(P in Pi_r) A_P(t) = E X_(2r)(t,x)
                      = t^(beta r) a_r,
a_r = E X_(2r)(1,0) >= 0.
```

There is no further J multiplicity when J is empty. This is the Wick formula,
not a proposed comparison. The pinned Chen author version explicitly states
in (8.1), p55, that limsup_r (1/r)log[(r!)^(3-alpha)a_r] is finite, and
(8.2) on that page gives the scaling. Hence its established first-moment
argument supplies

```text
sum_(P in Pi_r) A_P(t) <= K^r t^(beta r)/(r!)^(3-alpha)
```

for a fixed K, enlarging it to cover finitely many small r. The source page
was rendered and inspected in this follow-up. This is an imported existing
endpoint consequence; it is not obtained from (T) and is not a new proof
of the first-moment theorem. The same coefficient estimate can also be
extracted from nonnegative coefficients and the source's large-time bound
by minimizing exp(C t^kappa)t^(-beta r), since beta/kappa=3-alpha.

The distinction is decisive: multiplying the largest per-pattern envelope
by #Pi_r loses the known gain of (r!)^a. The actual full-trace sum has that
gain because the source controls the sum, not because every pattern is
uniformly smaller. Formula(A) is consistent with the source's summed bound.

## 9. No valid endpoint interpolation has been obtained

Let T_(n,r) denote the kernel obtained by summing the partial traces over
all J,P and then symmetrizing its m=n-2r free arguments. Its Wiener integral
has degree m. The source-backed endpoint information is:

- r=0: the known uncontracted-chaos estimate, imported read-only;
- r=n/2 for even n: the fully contracted sum above, from Chen's first moment.

These are norms in different tensor degrees. Ordinary log-convexity of Lp
norms is not an interpolation theorem between these contraction operators.
No source result or direct argument found here establishes the missing
log-convexity/positivity property for this ordered wave kernel.

A basic algebraic test shows why positive integration weights alone are
insufficient. In a two-dimensional Gaussian Hilbert space with orthonormal
basis e1,e2, take the symmetric four-tensor

```text
f = Sym(e1 tensor e1 tensor e1 tensor e2).
```

Its coordinate entries are nonnegative. Its full trace is zero, while

```text
Tr(f) = (e1 tensor e2 + e2 tensor e1)/4 != 0,
Tr²(f)=0.
```

Thus a proposed geometric interpolation with a positive power of the full
trace on the right cannot hold for every nonnegative-entry symmetric tensor.
Equivalently, the ordinary Gaussian polynomial is X1³X2, whose mean is zero
but whose second-chaos correction is nonzero. This is a test of a **generic
interpolation principle**, not a counterexample within the Riesz wave model.
Additional structure of g_n would need to be proved and used.

Likewise, no nonnegativity of even-order Stratonovich random polynomials is
assumed. Positivity of their Wick expectations is different from samplewise
positivity. A Gaussian L1-to-mean shortcut is therefore unavailable without
an independent argument.

The exact missing property is a quantitative control of the **summed partial
trace kernel** in its space-time Hilbert norm, uniform over the free-variable
configuration and preserving the target factorial order. Calling this an
interpolation assumption would merely hide the central unresolved estimate.
This attempt does not do so and stops here.
