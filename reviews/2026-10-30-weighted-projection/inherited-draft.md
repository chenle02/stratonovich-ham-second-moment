# Uniform tails and the actual local-phase ground projection

CANDIDATE, not independently accepted. This is standard ODE/spectral
analysis for the original sharp-lower consumer, not a novel theorem or a
complementary wave estimate. Full original goal remains active.

## 1. Inputs and target

Use the accepted actual d1 fixed family and notation of
notes/spectral-ground-family.md: U=Gamma*q>=0 smooth bounded and vanishing
at infinity, b in K=[b0,b1], H_b=-d^2-bU, normalized positive real p_b,
H_b p_b=-lambda_b^2 p_b. Imported scoped results from that note give

    0<l<=lambda_b<=L<infinity,
    E2(b)-E1(b)>=Delta>0,
    |Ej(b)-Ej(c)|<=M|b-c|, j=1,2, M=||U||infinity.

Use the accepted real local phase F and its partitions/cutoff bounds and
physical deterministic flow from notes/local-causal-young-flow.md Sections4-5.
All global E=H1/2 x H-1/2 phases embed continuously into F. Compact phases
alone are not dense in F; compact phases PLUS both constants are dense.
The accepted profile calculation in notes/joint-gaussian-tilt.md Section3
also gives bounded smooth spatial derivatives of U. No global integrability
of a Riesz potential is imposed.

We prove uniform weighted eigenfunction bounds, bounded/continuous wave
projections on F including constant data, and their invariance. We do not
assume or prove the complementary propagator estimate.

## 2. A fixed exterior comparison gives uniform tails

The eigenfunction energy identity gives

    ||p_b'||_2^2=b integral U p_b^2-lambda_b^2<=b1 M.

The equation p_b''=(lambda_b^2-bU)p_b also gives a uniform L2 bound on
p_b''. Therefore ||p_b||_H2<=C uniformly in b. In d1 the elementary Sobolev
inequality ||g||infinity^2<=2||g||_2||g'||_2 bounds p_b and p_b' uniformly
(use it on p_b and p_b'). A function in H1(R) has a continuous representative
vanishing at both infinities: approximate it in H1 by compact smooth functions
and use this same supremum inequality. Thus p_b and p_b' vanish at infinity.

Fix beta=l/2>0. Since U tends uniformly to0, choose ONE R>=1 such that
b1 U(x)<=l^2/2 for |x|>=R. On either exterior half-line,

    p_b''(x)>= (l^2/2)p_b(x)>=beta^2 p_b(x).

On x>=R compare with z(x)=p_b(R)exp(-beta(x-R)). The difference w=p_b-z
vanishes at R and tends to0 at infinity; it satisfies w''-beta^2 w>=0.
If w were positive somewhere, it would attain a strictly positive interior
maximum (its boundary values/limit are0), where w''-beta^2w<0, a contradiction.
Hence p_b(x)<=C exp(-beta(x-R)) on that half-line. Reversing x gives the
same bound on the other side. Increasing C handles the fixed interior:

    0<p_b(x)<=C exp(-beta|x|), uniformly b.                  (1)

The bounded coefficient in its ODE gives |p_b''(x)|<=C exp(-beta|x|).
Because p_b' tends to0, integration of p_b'' from the appropriate infinity
gives |p_b'(x)|<=C exp(-beta|x|) as well. In particular for every fixed
0<gamma<beta,

    sum_(k=0,1,2) ||exp(gamma|x|) p_b^(k)||_2 <= C_gamma.    (2)

This follows by integrating the squares of the pointwise bounds. No claim
that Simon's individual decay constant is already uniform is used.

## 3. Dual pairings on F, tail bounds, projection normalization

Use the accepted real chi_j,rho_j partition, rho_j supported in[j-1,j+1]
and chi_j=1 there. Smooth multiplier bounds and (1)-(2) give

    ||rho_j p_b||_H1 <= C exp(-beta|j|), uniformly j,b.       (3)

For z=(v,w) in F, define each distributional pairing locally and sum:

    <p_b,v>=sum_j <rho_j p_b,chi_j v>,
    <p_b,w>=sum_j <rho_j p_b,chi_j w>.                       (4)

These sums converge absolutely. For v in local H1/2, its dual H-1/2 norm
is bounded by the H1 bound in (3); for w in local H-1/2, use the H1/2 bound,
also bounded by H1. Consequently both sums have absolute value<=C||z||_F.
They extend the ordinary global E pairings and the ordinary integrals for
constant data. This specified partition defines continuous functionals.
Independence from another such partition follows first on compact smooth
phases and both constants, where all are the same integral, then by the
DEFINING density of that larger class in F.

If kappa_D is a smooth cutoff equal1 on[-D,D], supported in[-D-1,D+1],
0<=kappa_D<=1, with uniformly bounded first derivatives for D>=1, the
same argument applied to (1-kappa_D)p_b gives

    |<p_b,(1-kappa_D)v>|+|<p_b,(1-kappa_D)w>|
        <=C exp(-beta D)||z||_F.                            (5)

Indeed only cells with |j|>=D-1 contribute, and their geometric tail in
(3) is bounded by C exp(-beta D). Derivative bounds of kappa_D are uniform.
This is a local duality estimate, not pointwise evaluation of w.

Define, for every z in F,

    e_b=(p_b,lambda_b p_b),
    ell_b(z)=(<p_b,v>+<p_b,w>/lambda_b)/2,
    Pi_b z=e_b ell_b(z).                                    (6)

Global H2 bounds, the embedding E->F and lambda bounds show ||e_b||_F<=C;
(4) and lambda_b>=l give ||ell_b||_(F*)<=C and hence ||Pi_b||<=C uniformly.
Since ||p_b||_2=1, ell_b(e_b)=1 and Pi_b^2=Pi_b. Also
ell_b(p_b,-lambda_b p_b)=0, so the decaying wave partner is retained in
the complement. For e0=(1,0),

    ell_b(e0)=(1/2)integral p_b >=1/(2 sup_b||p_b||infinity)>0. (7)

Here integrability follows from (1), and 1=integral p_b^2<=||p_b||infinity
integral p_b. Thus the entrance coefficient of constant data is uniformly
positive, not just nonzero separately for each b.

## 4. Continuity of the actual F projection

Let Q_c be the GLOBAL L2 orthogonal complement of p_c, distinct from the
wave complement I-Pi_c. On it, H_c-E1(c) has spectral lower bound>=Delta,
by the accepted first-two-level gap. Its spectral measure therefore gives
||Q_c y||_2<=Delta^-1||(H_c-E1(c))y||_2 for y in H2. Apply this to p_b:

    ||Q_c p_b||_2<=2M Delta^-1 |b-c|.                       (8)

The residual is (E1(b)-E1(c)+(b-c)U)p_b, whose norm has the stated bound.
Because both eigenfunctions are positive, a=<p_b,p_c>>0. Their normalization
gives ||p_b-p_c||_2^2=2(1-a)<=2(1-a^2)=2||Q_c p_b||_2^2. Thus p_b is
L2-Lipschitz in b with this positive normalization. Subtracting their ODEs
and using (8), bounded U and Lipschitz E1 yields

    ||p_b-p_c||_H2<=C|b-c|.                                (9)

To see the H2 estimate explicitly, its second derivative is the sum of a
uniformly bounded coefficient times p_b-p_c and a coefficient O(|b-c|)
times p_c. The first derivative is then bounded by L2 and second derivative
using integration by parts or the Fourier inequality xi^2<=1+xi^4.

Hence e_b is continuous into E and F, since lambda_b is continuous. To
prove ell_b continuous into F*, first fix D and use the finitely many local
pairings with kappa_D p_b and (9). Their operator-norm differences tend to0.
The remainder is bounded uniformly by (5), and lambda_b and its reciprocal
are uniformly bounded/continuous. First choose D large, then let b->c.
This proves operator-norm continuity of ell_b and Pi_b on F. Compact K makes
these continuous maps uniformly continuous. No global E density in F or
uniform-in-D continuity constant is being assumed.

## 5. Invariance for the actual deterministic wave flow

Write P_b(t) for the named deterministic physical wave evolution on F.
On the global E phase e_b, the exact solution e^(lambda_b t)e_b solves
u_tt=u_xx+bUu; uniqueness of the named evolution gives

    P_b(t)e_b=exp(lambda_b t)e_b.                            (10)

For smooth compact initial phases AND both constant initial phases, the
bounded smooth potential gives classical solutions with bounded spatial
and time derivatives on every fixed finite horizon. One elementary
justification is the d1Duhamel formula: its kernel has mass t-s, spatial
supremum bounds follow from the convergent Volterra iteration, and
successive differentiated equations have bounded coefficients/forcing
from bounded derivatives of U. The same argument applies to compact smooth
initial derivatives and constant phases; it does not require compact U.

Put a(t)=<p_b,u(t)> for such data. The exponential bounds on p_b,p_b',p_b''
and the bounded solution derivatives justify differentiation and integration
by parts, with boundary terms vanishing. Thus

    a'= <p_b,u_t>,
    a''=<p_b,u_xx+bUu>=<p_b''+bU p_b,u>=lambda_b^2 a.

Therefore ell_b(P_b(t)z)=(a+a'/lambda_b)/2 solves y'=lambda_b y, giving

    ell_b(P_b(t)z)=exp(lambda_b t)ell_b(z).                  (11)

For each fixed t, both sides are bounded linear functionals on F by (4)
and the accepted flow bound. Extend from compact smooth phases PLUS constants
by their defining density in F. Combining (10)-(11),

    P_b(t)Pi_b=Pi_b P_b(t)=exp(lambda_b t)Pi_b.              (12)

No norm continuity of the free wave group is asserted. Invariance alone
does not bound the complementary propagator.

## 6. Scope and falsification/formal boundary

The correct wave projection includes BOTH entries and the factor1/2:
(p,lambda p) has coefficient1, whereas (p,-lambda p) has coefficient0.
Dropping velocity or its reciprocal-lambda factor would fail these two
normalization tests. These are finite diagnostic consumers, not formal
spectral certification. Core analytic content is ODE comparison/regularity,
local Sobolev duality, spectral gap and actual wave invariance; it remains
outside the existing standalone finite Lean proofs. No new spectral
foundation, axiomatized shell or private companion is created here.

Still open: global fractional-Sobolev complementary wave estimate and its
transfer to F with the cutoff projection tails; growing cone/product and
terminal averaged observable, random event/rate, full sharp constants and
original higher dimensions/source normalization. No novelty or whole-paper/
circulation clearance. Canonical TeX/PDF and earlier accepted proofs unchanged.
