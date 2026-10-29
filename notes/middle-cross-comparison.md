# Middle-cross/self comparison in white space

Status: candidate analytic proof and local Lean consumer; source/type/application
review is pending. The scope is d=α=1, Γ=δ₀, raw temporal exponent 0<a<1,
and common gap damping θ>0. A positive multiple of δ₀ contributes the same
positive square to every four-vertex term. The original general covariance
comparison remains at nine terms. This note would add two WHITE terms only,
giving thirteen there if accepted. It does not solve the all-order or sharp
constant problem.

The ordered diagram definitions, the analytic shared clock and their white
spatial regularization limits are the named prior inputs from the degree-four
memo. These are auxiliary chain-gap transforms, not physical unequal-time
correlations or diagonal-horizon moment Laplace transforms. Normalize θ=1.

## 1. Statement and labels

For split (1,3), the singleton is vertex 0 and the long chain is 1<2<3.
The partition is 02·13. Attach λ≥0 to the CROSS pair 02 and ν≥0 to the SELF
pair 13. Let I be the actual wave transform and J the shared-clock candidate.
Delete the nonnegative clock-overlap penalty to define the enlarged candidate
J⁺≥J. We propose the strict comparison

    0<J(λ,ν)≤J⁺(λ,ν)≤U(b,c)<I(λ,ν),  λ>0,ν≥0,             (T)
    b=1+ν, c=1+λ.

At λ=0 all four quantities agree. Fractional averaging would give J_a<I_a
for every 0<a<1. The mirrored (3,1) partition is also 02·13, but canonical
pair 02 is then SELF and pair 13 is CROSS. Its parameters must be exchanged.

## 2. Actual wave integral

Let u be the singleton time and v,w,z the three positive long-chain gaps.
The cross time difference is |u−v−w| and the self span is w+z. The white
spatial pairing gives

    G_u(X)G_v(Y)G_w(X−Y)G_z(Y−X),   G_t(x)=1{|x|<t}/2.

Put C=min(w,z). The spatial factor is area{|X|<u,|Y|<v,|X−Y|<C}/16.
For R=u+v, q=u−v, d=|q|, the area derivative with respect to C is
2(R−max(C,d))₊. This follows by differentiating the three rectangle-strip
branches of the reviewed area formula; it can also be checked by integrating
the lengths of the two strip edges. The area is zero at C=0. Including the
coordinate Jacobian 1/2, positive Tonelli and one elementary Gamma integral give

    (1/32)∫_{|q|}∞ e^(−R)area(R,q,C)dR
      = (1/16)∫₀ᶜ e^(−max(|q|,t))dt.                        (V)

For d≥C the value is Ce^(−d)/16. For d<C it is
[(d+1)e^(−d)−e^(−C)]/16. Hence the actual transform is

    I=(1/16)∫ e^(−b(w+z)−λ|q−w|)
                   ∫₀^{min(w,z)}e^(−max(|q|,t))dt dq dw dz.

Swap the positive integrals, integrate z≥t and set w=t+x. This gives
(1/(16b))∫_{t,x≥0}e^(−2bt−bx)∫_ℝe^(−λ|q−t−x|−max(|q|,t))dq dt dx.
There are three q regions. Their respective contributions are

    q<0:    [1/c+1/(2b+λ+1)]/[16b(b+λ)(2b+2λ+1)],
    0≤q≤t:  1/[16b(b+λ)(2b+1)(2b+1+λ)],
    q≥t:    [1/(b+λ)+1/c]/[16b(2b+1)(b+1)].

For q<0 set q=−d, integrate x, then split d≥t and d<t. For the middle
region set q=t−y, 0≤y≤t. For q≥t set q=t+y and split x≥y or x<y.
Each calculation is a product of positive exponential integrals. Their sum is

    I(λ,ν)= [2b²+4bc+2c²−c+1]
              /[8bc(b+1)(2b+1)(b+c−1)(2b+2c−1)].             (I)

No cross delay was discarded and no extra shuffle or factorial factor appears.

## 3. Heat bridge and a survival envelope

The variables in this section are operational times. The two spatial Brownian
pair differences have covariance matrix

    [ u+v+w   −w  ]
    [   −w    w+z ].

With r=w+z and R=u+v, its determinant is rR+wz. The joint δ density at
zero therefore equals h(r)h(R+wz/r), h(t)=(2πt)^(−1/2). This factorization
of density values is not independence of the two pair differences.

For forward scalar-clock increments the covariance is their nonnegative
interval overlap O. Deleting exp(−λνO) increases the positive averaged
integrand. Put A=λ+λ²/2. The self factor and heat damping combine to
exp(−b²r/2). The root change R=u+v,q=u−v has Jacobian 1/2. Thus

    J⁺=(1/32)∫₀∞ h(r)e^(−b²r/2)
            ∫₀ʳ∫_ℝ e^(−A|q−w|) H_{w(r−w)/r}(q)dq dw dr,
    H_γ(q)=∫_{|q|}∞e^(−R/2)h(R+γ)dR.                        (J)

The elementary Gamma representation of h gives the positive mixture

    H_γ(q)=∫_{1/2}∞ [m(s)/s]e^(−(s−1/2)γ)e^(−s|q|)ds,
    m(s)=1/[π√2√(s−1/2)].

The measure [m(s)/s]ds has mass one, since H₀(0)=∫e^(−R/2)h(R)dR=1.
All interchanges are positive Tonelli. Direct integration of the even root
kernel gives

    ∫_ℝe^(−s|q|−A|q−w|)dq = [2/(s+A)]S_{A,s}(w),
    S_{A,s}(w)=e^(−Aw)+∫₀ʷAe^(−At)e^(−s(w−t))dt.

In particular 0≤S≤1. On the mixing support s≥h_*:=1/2, the positive
integral formula proves S_{A,s}(w)≤S_{A,h_*}(w). It retains the shift w.
For A≠s, S=(s e^(−Aw)−A e^(−sw))/(s−A), and for A=s,
S=(1+Aw)e^(−Aw). These closed forms are not integrated separately in s.

## 4. Exact bridge–resolvent integral

Define M_b(η;A), η≥0, by replacing the root kernel in (J) with
[2/(s+A)]e^(−ηw) after inserting the positive s mixture. It equals

    (1/16)∫ [m(s)/(s(s+A))] h(r)e^(−b²r/2)
                e^(−(s−1/2)w(r−w)/r−ηw) ds dw dr, 0<w<r.

Set w=rt and integrate r. With τ=s−1/2 and p=√(b²+2η), the remaining
bridge integral is

    ∫₀¹[b²+2ηt+2τt(1−t)]^(−3/2)dt
       =2(p+b)/[bp((p+b)²+2τ)].                              (B)

For (η,τ)≠(0,0), integrate the quadratic directly and use p²=b²+2η.
The result before cancellation is
[(η+τ)/b−(η−τ)/p]/[(η+τ)²+2b²τ]. Factor the denominator as
[τ+(p−b)²/2][τ+(p+b)²/2] to obtain (B). At (0,0) both sides are 1/b³;
continuity also follows from the bound b^(−3) on the positive integrand.

Now substitute z=√(2s−1), so m(s)ds=dz/π, and 1+2A=c². Then

    M_b(η;A)=(p+b)/(2πbp)
      ∫₀∞ dz/[(z²+1)(z²+c²)(z²+(p+b)²)]
      =(1+c+p+b)/[4bp c(c+1)(c+p+b)(1+p+b)].                  (M)

The last identity follows by partial fractions and
∫₀∞(z²+q²)^(−1)dz=π/(2q): for positive rates q₁,q₂,q₃ the triple integral
is π(q₁+q₂+q₃)/[2q₁q₂q₃(q₁+q₂)(q₂+q₃)(q₃+q₁)]. One first obtains
the two-factor value π/[2q₁q₂(q₁+q₂)] by subtraction,then subtracts the
two-factor formulas at q₂ and q₃ and cancels q₃²−q₂². Coincident rates follow
by dominated convergence; all rates here are positive. Every preceding
integral is positive and finite.

## 5. A nonsingular upper bound

The survival envelope from §3 bounds J⁺ by the positive integral obtained
with S_{A,h_*}. For A≠h_* it is

    U=[h_* M_b(A;A)−A M_b(h_*;A)]/(h_*−A).

This combination must not be split into separate fractional λ integrals
across A=h_*. We now eliminate that apparent singularity.
Put d=√(b²+c²−1), e=√(b²+1), B=b+c, C=b+1, K=1/[4bc(c+1)], and

    m₀(x)=K[1/(x(x+C))+1/(x(x+B)(x+C))].

Formula (M) is m₀(p). Since e²−d²=1−2A,
U=m₀(e)+(m₀(d)−m₀(e))/(e²−d²). The locally Lean-checked algebra identity is

    m₀(d)−m₀(e)=(e−d)K(F₁+F₂),
    F₁=(d+e+C)/[de(d+C)(e+C)],
    F₂=[d²+de+e²+(B+C)(d+e)+BC]
          /[de(d+B)(e+B)(d+C)(e+C)].

Therefore the nonsingular form is

    U(b,c)=m₀(e)+K(F₁+F₂)/(d+e).                             (U)

It is finite, positive and continuous for b,c≥1. It also equals the
survival-envelope integral at A=h_*. Indeed 2/(s+A)≤4, S≤1 and
e^(−(s−1/2)γ)≤1 give an integrable dominating bound whose total is
(1/8)∫rh(r)e^(−b²r/2)dr=1/(8b³), uniformly in A≥0. The survival integral
and (U) are continuous; their equality away from A=h_* extends to that
point. No derivative or singular signed integral is needed there.

Erasing the shift instead would give M_b(0;A). That larger bound is too
weak: at b=1,c=11/10, I=545/11616 while M_b(0;A)=1025/21483, with
I−M_b(0;A)=−6005/7562016. This excludes that shortcut, not J≤I.
The even root component has zero initial hazard; the terminal-cross note's
positive pure-exponential component rate cannot simply be reused here.

## 6. The actual two-root consumer in Lean

The local MiddleCross module proves

    upper b c √(b²+c²−1) √(b²+1) < actual b c,  b≥1,c>1.       (L)

Here actual is exactly (I), and upper is exactly (U), with m₀,F₁,F₂ written
out. The desired inequality and numerator positivity are not hypotheses.
The proof verifies the original rational difference and denominator signs,
not just a separate positive polynomial.

For completeness, its certificate construction is as follows. Clear the
original positive denominator

    8bcde(b+1)(2b+1)(c+1)(d+e)(b+c−1)
      ·(b+c+d)(b+c+e)(b+d+1)(b+e+1)(2b+2c−1).

For the root parameters Z=b+e≥2 and T=(d+c)/(b+1)>1, the root equations give

    b=(Z²−1)/(2Z), e=(Z²+1)/(2Z),
    c=((b+1)T−(b−1)/T)/2, d=((b+1)T+(b−1)/T)/2.

The code derives these inverse identities from the actual square roots.
After substitution, the cleared numerator multiplied by 32768T⁷Z⁹ is the
explicit certificate Cert(Z−2,T−1). Cert has 300 positive integer monomials,
all divisible by its second argument, including terms with first-argument
degree zero. Thus it is positive for Z−2≥0,T−1>0. The full identity,
positivity, inverse/domain facts, rational difference, resolvent difference
and actual consumer (L) are source-checked in Lean. The certificate is in
the source, with the exact monomial data retained by its generator.

The analytic wave, Gaussian bridge and survival-integral identifications
remain outside Lean and require the independent source/type/application
review. This is a local proof/replay using pinned read-only dependencies,
not a new companion, full Mathlib rebuild, Comparator or formal SPDE gate.

## 7. Fractional averaging and scope

For λ>0,ν≥0, combine J≤J⁺≤U with (L) to obtain (T). At λ=0, the overlap
factor is one, S=1 and (M) gives
J=J⁺=U=I=(b+1)/[4b²(2b+1)²]. No Gamma(0) is used.

For 0<a<1 average with Γ(a)^(−2)λ^(a−1)ν^(a−1)dλdν on the positive
quadrant. Let s₀=b+c≥2. The numerator in (I) is at most 2s₀², while
(b+1)≥b, (2b+1)≥2b, (s₀−1)≥s₀/2 and (2s₀−1)≥s₀. Hence
I≤1/(4b³c)≤1/(4bc). The two positive Gamma integrals give
I_a≤Γ(1−a)²/4<∞. Thus J_a<I_a by positivity of the pointwise difference
on the positive parameter domain, not by a limit of strict inequalities.

At common θ>0 the fixed-parameter factor is θ^(−6) with parameters
λ/θ,ν/θ, and the fractional factor is θ^(2a−6). Positive white amplitudes
give a common positive square. Swapping chain names gives the mirror with
its canonical parameters exchanged.

[held back: collaborators' unpublished work]