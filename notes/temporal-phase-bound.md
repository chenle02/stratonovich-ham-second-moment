# Raw temporal modulation and continuous wave factors

ACCEPTED internal temporal estimates: native Opus5.5/high full review,
PASS_WITH_NOTES/HIGH, scientific revision 81d9158; see the
2026-10-30-temporal-phase-bound proof packet and adjudication.
Only temporal estimates are proved below. The actual spatial two-phase
operator, its Fourier normalization, both variances and source cutoff
limits remain separate matching and construction obligations.

## 1. Temporal Hilbert space and interval indicators

Fix a=alpha_0 in (0,1), T>0. From the accepted own covariance foundation,
spectral-mask-covariance-foundation.md Section4 (exact supplied excerpt),
the symmetric raw form with kernel |t-u|^-a is positive semidefinite and

    ||f||_a^2 <= [2T^(1-a)/(1-a)] ||f||_L2(0,T)^2                 (1)

on real compact smooth tests, with a separable Hilbert null-quotient
completion H_a. We import precisely this result, not a modulation bound.
The complexification has the form

    ||f||_a^2 = int_0^T int_0^T f(t)conj(f(u))|t-u|^-a dt du.

Indeed symmetry cancels the imaginary cross term, leaving the sum of the
two nonnegative real quadratic forms for Re f and Im f. The same bound
(1) follows by adding those real bounds. Smooth compact tests are dense
in complex L2, so (1) extends the map from L2 into this Hilbert completion.
In particular any bounded measurable function on I=[s,s+h] subset[0,T], extended by
zero outside I, is admitted. Formula (1) and the integral formula persist
by L2 approximation: the absolute bilinear form is bounded by the same
Schur constant via Cauchy-Schwarz. No differentiability of the zero
extension or its endpoints is asserted.

Hereafter 0<h<=1, I subset[0,T], and <x>=sqrt(1+x^2) for real x.

## 2. A modulated C1 amplitude

**Proposition 1.** Let A in C1(I;C), M=sup_I|A|, D=sup_I|A'|. Uniformly
over T,s,h,A and omega in R,

 ||1_I A(t)exp(i omega t)||_a^2
     <= C0(a) h^(2-a)(M+hD)^2 <h omega>^(a-1),                    (2)

where one may take C0(a)=16/(1-a).

*Proof.* Set

 c(v)=int_s^(s+h-v) A(u+v)conj(A(u))du, 0<=v<=h.

Ordinary differentiation of an integral with moving endpoint gives

 c'(v)=-A(s+h)conj(A(s+h-v))
            +int_s^(s+h-v) A'(u+v)conj(A(u))du.

Thus c is C1 on the closed interval (one-sided derivatives at endpoints),
c(h)=0, |c(v)|<=h M^2, and |c'(v)|<=M^2+hMD. The two triangles t>u and
t<u in the covariance integral are complex conjugates, so, by absolute
integrability of the kernel against bounded functions, the squared norm in (2)
is exactly

    2 Re int_0^h v^-a exp(i omega v)c(v)dv.                         (3)

Put K=M+hD, kappa=omega h, and f(y)=c(hy)/h for 0<=y<=1. Then
f(1)=0, |f|<=K^2, |f'|<=K^2, and (3) is

    2h^(2-a) Re int_0^1 y^-a exp(i kappa y)f(y)dy.                 (4)

If K=0 there is nothing to prove. If |kappa|<=1, the absolute value of
the integral in (4) is at most K^2/(1-a), and
<kappa>^(a-1)>=2^((a-1)/2). Thus the desired bound follows with any
C0>=2sqrt(2)/(1-a).

If k=|kappa|>1, split at delta=1/k. The small interval contributes at
most K^2 k^(a-1)/(1-a). On [delta,1], integrate exp(i kappa y) by parts.
The endpoint at1 vanishes because f(1)=0. The endpoint at delta is at
most K^2 k^(a-1). The integral of the absolute derivative, divided by k,
is bounded by

 (K^2/k)[a int_delta^1 y^(-a-1)dy +int_delta^1 y^-a dy]
   <=K^2[k^(a-1)+k^-1/(1-a)]
   <=K^2 k^(a-1)[1+1/(1-a)].

In the last step k^-1<=k^(a-1) since a>0. Summing these three bounds
gives at most 4K^2 k^(a-1)/(1-a). For k>1,
k^(a-1)<=sqrt(2)<kappa>^(a-1). Multiply by the factor 2h^(2-a) in
(4); 8sqrt(2)/(1-a)<=16/(1-a) proves (2). The sign of kappa was never
restricted. This proves Proposition 1.

## 3. Correlated sine and cosine products

**Proposition 2.** For r,rho>=0, let P_r be either cos(rt) or sin(rt),
and let Q_rho be either cos(rho t) or sin(rho t). Then, uniformly over
these choices and the parameters of Proposition 1,

 ||1_I A P_r Q_rho||_a^2 <= C0(a) h^(2-a)(M+hD)^2
      [<h(r-rho)>^(a-1)+<h(r+rho)>^(a-1)].                         (5)

*Proof.* Expand each sine or cosine into its two signed complex
exponentials. Their product is a sum of four modes at frequencies
sigma r+tau rho, sigma,tau in {+1,-1}, with coefficients of absolute
value1/4. In any Hilbert space, the triangle inequality and weighted
Cauchy-Schwarz give

    ||sum_j c_j v_j||^2 <= (sum_j |c_j|) sum_j |c_j| ||v_j||^2.

Apply this to the four modulated amplitudes. The first coefficient sum
is1. Apply (2) separately to every mode. Two frequencies have magnitude
|r-rho| and two magnitude r+rho, so the result is at most one half of
the right side of (5). Increasing this harmless numerical factor to1
proves (5). Repeated or zero frequencies cause no issue. No modes are
assumed independent or orthogonal. This proves Proposition 2.

## 4. Continuous sine factors, including zero frequency

Define the family

    c_r(t)=cos(rt),
    b_r(t)=<r>sin(rt)/r if r>0, and b_0(t)=t.

**Proposition 3.** For F_r in {c_r,b_r} and G_rho in {c_rho,b_rho},

 ||1_I F_r G_rho||_a^2 <= C1(a)(1+T)^4 h^(2-a)
      [<h(r-rho)>^(a-1)+<h(r+rho)>^(a-1)],                         (6)

with C1(a)=4*3^(1-a) C0(a), independent of r,rho,T,s,h and the choices.

*Proof.* If r>=1, b_r is a sine with coefficient <r>/r<=sqrt(2).
If 0<=r<=1, the elementary fundamental-theorem identity is

    b_r(t)=t<r> int_0^1 cos(vrt)dv.                                (7)

For r>0 it follows by integrating the cosine; for r=0 both sides equal t.
The coefficient <r> is at most sqrt(2). A c_r is a cosine with unit
coefficient. Thus a product F_r G_rho is a scalar coefficient of absolute
value at most2 times a normalized integral (over zero, one or two copies
of[0,1]) of

    t^j P_(r')(t) Q_(rho')(t),  j in {0,1,2}.

Each altered frequency r' is either r itself or v r in a low-frequency
b case; consequently |r'-r|<=1. Likewise |rho'-rho|<=1. If no averages
are present use a one-point probability space for this statement.
The map from averaging parameters into L2(0,T) is continuous by dominated
convergence, since t is bounded and every frequency here is finite.
Equation (1) makes it continuous into H_a as well, so these are genuine
Bochner integrals. Their images under the continuous L2-to-H_a map
agree with the pointwise-in-t averages: this follows first in L2 by joint
continuity and ordinary integration, then by continuity into H_a.
Hilbert Jensen bounds the squared norm of the average
by the average of the squared norms.

Apply Proposition 2 to each integrand with A=t^j. For j=0,
M+hD=1; for j=1, M+hD<=T+1; for j=2,
M+hD<=T^2+2T<=(1+T)^2. Therefore in every case
(M+hD)^2<=(1+T)^4.

For any real x,delta, the Euclidean triangle inequality gives
<x+delta><=(1+|delta|)<x>, and applying it in the reverse direction gives
<x+delta> >= <x>/(1+|delta|). The changes from h(r+-rho) to
h(r'+-rho') have size at most2 because h<=1. Thus, since a-1<0,

 <h(r'+-rho')>^(a-1)<=3^(1-a)<h(r+-rho)>^(a-1).

Apply these two comparisons to (5), then Hilbert Jensen and the squared
coefficient bound4. This proves (6) and Proposition 3.

Taking C_a=C1(a) gives a single constant depending only on a which can
replace the constants in all three propositions.

## 5. Exact scope and diagnostic limits

The c_r,b_r family is defined and estimated here. Its use in the actual
normalized two-phase interaction kernel, the signs/time argument/Fourier
constants and BOTH Gaussian operator variance directions still require
separate verification. A shifted free-wave time or a different factor
must be matched explicitly; the name 'balanced factor' is not that proof.
Nothing here uses the separate scalar frequency theorem as an input.

The 120 diagnostics concern only real amplitudes1,t,t^2 at a .1/.5/.9,
h1 or1/8, omega0/1/16/64, with starts0 or2 for polynomials. They use exact
polynomial autocorrelations and the substitution v=h z^(1/(1-a)) to remove
the kernel singularity. Constant-amplitude omega0 is compared with the
exact value2h^(2-a)/((1-a)(2-a)). Working precision40 digits is not certified
accuracy. No complex/negative-omega/product/sinc/operator numeric coverage
is claimed. The proof, rather than these finite controls, handles those
parameters and continuous averages. No new Lean theorem was made.

Original full all-dimensional lower/sharp-upper/source goal remains ACTIVE;
the present higher-dimensional task is one component. No operatornorm,
Schatten/path/Young/sourcecutoff/actual new moment/source-energy identity,
Skorohod result, correspondence, HPC, official companion, public release,
canonical TeX/PDF/wiki edit or whole-paper/cold-reader clearance follows.
