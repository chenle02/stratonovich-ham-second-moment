# A terminal-cross/self comparison in white space

Status: the analytic comparison and its scalar type/application correspondence
passed source-bound Opus5.5/HIGH review at 6475ea0, all six checks passing.
Five supporting scalar statements have local Lean source/replay evidence.
The model reductions and integral identifications remain informal proofs;
the full sharp-constant problem remains open.

The scope here is d=α=1, Γ=δ₀, with raw temporal exponent 0<a<1. A positive
multiple of δ₀ multiplies every four-vertex term by the same positive square.
The previously reviewed nine-term comparison for the original covariance
class is unchanged. This note adds two white-space diagrams,
giving eleven controlled terms there; it does not give eleven terms for
the general covariance class.

Use the ordered initial-chain convention and the shared analytic clock from
the degree-four memo. All transforms are auxiliary chain-gap transforms,
not physical unequal-time correlations or diagonal-horizon Laplace transforms.
Normalize the common gap damping to θ=1 initially.

## 1. Exact statement and pair labels

For split (1,3), the partition is 03·12 in zero-based chain labels. The
singleton and the last vertex of the long chain form the cross pair. Attach
λ≥0 to this pair, and ν≥0 to the self pair formed by the first two long-chain
vertices. Let I(λ,ν) be the actual wave gap transform. Let J(λ,ν) be the
shared-clock candidate, with each pair oriented forward in global time.

Write J⁺ for the enlarged candidate obtained by deleting the nonnegative
clock-overlap term λνO from the Gaussian exponential. This is a diagram
upper bound, not a claim about a new Gaussian process or a Feynman–Kac formula.
The resulting comparison is

    0 < J(λ,ν) ≤ J⁺(λ,ν) < I(λ,ν)      if λ>0, ν≥0.          (T)

At λ=0 all three are equal. Consequently their fractional averages have
J_a<I_a for every 0<a<1. Swapping chain names gives the same result for
split (3,1), partition 01·23. In that mirrored partition the canonical first
pair 01 is the SELF pair: its parameter is ν, while the second pair 23 gets
λ. The pair parameters must therefore be exchanged when using the original
canonical-pair table. The fractional averaging measure is symmetric in them.

## 2. A rational formula for the actual transform

Let u be the singleton time and let v,w,z be the long chain's three positive
gaps. Their two covariance factors are exp(−λ|u−v−w−z|) and exp(−νw).
The spatial integrand is

    G_u(X) G_v(Y) G_w(0) G_z(X−Y),
    G_t(x)=1{|x|<t}/2.

Keep the delay w in the cross factor. Set L=v+z only after observing that
all temporal factors depend on v,z through L. The space-time convolution is

    ∫₀ᴸ∫ G_v(Y)G_{L−v}(X−Y)dYdv = (L²−X²)₊/8.

Indeed set p=v+Y, q=v−Y. The allowed rectangle is 0<p<L+X,
0<q<L−X; the coordinate Jacobian is 1/2 and the two Green factors give
1/4. The expression is zero outside |X|<L. Thus, after integrating v and Y,
the spatial factor is

    V(u,L) = (L²m−m³/3)/16,       m=min(u,L).

Put R=u+L, q=u−L; the Jacobian is 1/2 and R>|q|. Direct integration gives

    (1/2)∫_{|q|}∞ e^(−R)V((R+q)/2,(R−q)/2)dR
      = e^(−q)/64                         if q≥0,
      = e^(−d)(d+1)²/64, d=−q            if q<0.

For the first branch use V=(R−q)³/192. For the second write R=d+t,
so V=t d²/32+t²d/32+t³/192 and integrate the three Gamma moments.

Let c=1+λ and b=1+ν. The negative-q half-plane contributes the second
term below. Separately split the positive (q,w) quadrant into q>w and w>q
to obtain the first term. The actual integral becomes

    64 I = [1/(b+1)] [1/c+1/(b+λ)]
            +[1/(b+λ)] [1/c+2/c²+2/c³]
         = 2[b(c²+c+1)+c³+c+1]/[c³(b+c−1)(b+1)].             (I)

Every exchange above is nonnegative Tonelli. In particular I is finite for
all λ,ν≥0; no oscillatory Fourier exchange was used.

## 3. One-dimensional kernel for the enlarged clock candidate

The variables in this section are operational times,not the physical times
of §2. The two spatial Brownian differences, before any temporal averaging, can be
written B₀(u)−B₁(v+w+z) and B₁(v+w)−B₁(v). Their covariance matrix is

    [ u+v+w+z   −w ]
    [    −w       w ].

It is positive definite, with determinant w(u+v+z). Thus their joint δ
density at zero is h(w)h(u+v+z), where h(t)=(2πt)^(−1/2). The differences
are correlated; a product of density VALUES here is not independence.

The forward scalar-clock increments have nonnegative overlap O. The joint
Gaussian characteristic function contributes exp(−λνO). Dropping this factor
increases the positive averaged integrand. Here O is the overlap of
[min(u,v+w+z),max(u,v+w+z)] with [v,v+w]. Thus the original J has exactly
the integrand below times exp(−λνO), as in the prior degree-four definition.
Put A=λ+λ²/2; the self damping
combines with heat damping to give b²/2. Therefore

    J⁺ = (1/16)∫ L e^(−(u+L)/2) h(u+L) h(w)
                     e^(−b²w/2−A|u−L−w|) du dL dw.

The factor L is the length of the remaining v-integration, 0<v<L. The same
R,q change of variables gives

    J⁺ = (1/64)∫₀∞ h(w)e^(−b²w/2) F_A(w)dw,                 (J)
    F_A(w)=∫_ℝ H(q)e^(−A|q−w|)dq,
    H(q)=∫_{|q|}∞ f(R)(R−q)dR,     f(R)=h(R)e^(−R/2).

The factor 1/64 is (1/16) times the coordinate Jacobian 1/2 times
L=(R−q)/2. These formulas use the joint Gaussian density, not products
of marginal spatial expectations. They also follow as the white spatial
regularization limits in the already reviewed degree-four construction.

## 4. A positive mixture and uniform exponential envelope

For q≥0 let g(q)=H(q). The elementary Gamma integral yields

    f(R)=∫_{1/2}∞ e^(−sR) ds/[π√2√(s−1/2)],
    g(q)=∫_{1/2}∞ e^(−sq) ω(ds),
    H(−q)=∫_{1/2}∞ e^(−sq)(1+2sq) ω(ds),
    ω(ds)=ds/[π√2 s²√(s−1/2)].

All exchanges are positive Tonelli. This ω is a probability measure because
g(0)=∫Rf(R)dR=1. Consequently

    F_A(w)=∫ L_{A,s}(w)ω(ds),
    L_{A,s}(w)=∫₀∞e^(−sq)[e^(−A|w−q|)+(1+2sq)e^(−A(w+q))]dq.

For A>0, s>0, define

    m_{A,s}=2(A+2s)/(A+s)²,       k_{A,s}=As/(A+2s).

We claim L_{A,s}(w)≤m_{A,s}e^(−k_{A,s}w) for w≥0. If A≠s, integration
of the three positive exponential pieces gives

    L_{A,s}(w) = [4s²e^(−Aw)−2A(s+A)e^(−sw)]/[(s−A)(s+A)²].

For A<s this is C e^(−Aw)−D e^(−sw), with
C=4s²/[(s−A)(s+A)²], D=2A/[(s−A)(s+A)]. For s<A exchange the roles of
the two exponential rates and use C=2A/[(A−s)(A+s)],
D=4s²/[(A−s)(A+s)²]. In either case C>D≥0, C−D=m_{A,s}, and
(C−D)k_{A,s}=C·(slow rate)−D·(fast rate).

The following convexity deduction is checked in Lean. If 0≤D<C and
(C−D)k=Cr−DR, then

    C e^(−rw)−D e^(−Rw) ≤ (C−D)e^(−kw).

To see this directly, r=((C−D)/C)k+(D/C)R and use convexity of the
exponential. At A=s the component is e^(−Aw)(w+3/(2A)); its asserted
bound follows from 1+t≤e^t with t=2Aw/3. The signed C,D representation
is used pointwise only. Its pieces are never integrated separately in s
near s=A, where they can individually diverge.

On the actual mixing support s≥1/2, the locally Lean-checked rate inequality is

    k_{A,s} ≥ k := A/[2(A+1)].

Integrating the component bound gives F_A(w)≤F_A(0)e^(−kw). The mass is
computed without signed cancellation inside the mixing integral:

    F_A(0) = (2/A)∫ Rf(R)(1−e^(−AR))dR
           = (2/A)[1−(1+2A)^(−3/2)]
           = 4(c²+c+1)/[c³(c+1)] =: F₀.                       (E)

The required Gaussian moments are ∫Rf=1 and ∫Rfe^(−AR)=(1+2A)^(−3/2).
The rate and mass are finite and positive. Thus (J) and the elementary heat
resolvent integral ∫h(w)e^(−d²w/2)dw=1/d imply

    J⁺ ≤ F₀/[64√(b²+2k)]
       = (c²+c+1)/[16c³(c+1)√(b²+(c²−1)/(c²+1))].            (U)

This envelope controls the integrated object. The earlier stronger Rayleigh-
fiber inequality tested in closed-probe.py is not an input to this proof.

## 5. The scalar consumer, checked in Lean

Put P=c²+c+1 and N=bP+c³+c+1. For b≥1 and c>1, (U) is strictly less
than I in (I). Both denominators and the square root are positive. Squaring
after clearing them reduces exactly to positivity of

    (c+1)²[(c²+1)b²+c²−1]N²
      −4(c²+1)P²(b+c−1)²(b+1)².                              (Q)

At b=1+x, c=1+y the polynomial has 47 positive monomials, every one divisible
by y. Its y coefficient at x=0 is 96. Thus it is positive for x≥0,y>0.
The exact certificate, its identity with (Q), the domain conditions, clearing
positive denominators and the STRICT square-root comparison are all checked
by terminal_bound in the local TerminalCross Lean module. The formal consumer
starts with the closed form displayed in (U), not merely a sample or a
polynomial sign. The preceding identifications F₀=4P/[c³(c+1)] and
2k=(c²−1)/(c²+1) are algebraically proved above and were independently
checked for this application; they are not part of the formal statement.
No desired bound is a Lean hypothesis.

The formal boundary excludes the physical/Brownian reductions, the positive
mixture identification, and their application. Those analytic steps are covered by the separate source-bound review of
this note,not by the Lean statements. No new companion/package gate, full
dependency rebuild, Comparator run or full SPDE formalization is claimed.

## 6. Fractional averaging, scaling and the remaining problem

Combine J≤J⁺ with (U) and (I). For λ>0, ν≥0 this proves (T) at its stated
finite-degree scope. At λ=0, A=0 and F_A(w)=∫H(q)dq=6; hence J⁺=3/(32b)=I.
The clock overlap factor is then one, so J=J⁺ also. No Gamma(0) is used.

For every 0<a<1, average with

    Γ(a)^(−2) λ^(a−1)ν^(a−1)dλdν     on (0,∞)².

Finiteness follows directly from (I): P≤3c², c³+c+1≤3c³,
b+c−1≥(b+c)/2 and b+1≥b give I≤3/(16bc). Moreover
Γ(a)^(−1)∫₀∞λ^(a−1)/(1+λ)dλ=Γ(1−a): insert
(1+λ)^(−1)=∫₀∞e^(−r(1+λ))dr and perform the two positive Gamma integrals.
Hence I_a≤(3/16)Γ(1−a)²<∞, consistent with the previously reviewed (W).
All new integrands are nonnegative and J≤J⁺<I pointwise on the positive
parameter domain, so Tonelli and strict positivity of the difference give
J_a<I_a. Strictness is not inferred by a limit of strict inequalities.

At arbitrary θ>0 the fixed-parameter quantities scale as θ^(−6) times
their θ=1 values at λ/θ,ν/θ. After fractional averaging the factor is
θ^(2a−6). This is the original white four-vertex homogeneity. Swapping chain
names proves the mirrored (3,1)01·23 comparison, with its pair parameters
exchanged as specified in §1.

This adds two controlled diagrams only in the white endpoint, giving
eleven there and leaving four: (1,3)02·13, its (3,1)02·13 mirror, and the
two fully cross-paired (2,2) diagrams. The original covariance-class count
stays at nine. No all-order comparison, full sharp constant, novelty,
Skorohod result or circulation clearance follows from this finite-degree step.
