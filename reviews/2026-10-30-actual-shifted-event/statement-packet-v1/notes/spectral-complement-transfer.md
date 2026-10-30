# Complementary wave bound on the actual local phase

ACCEPTED at the scoped analytic/application gate: actual Opus5.5/HIGH,
18 checks PASS,268.893seconds, no required repairs; sourceb07d013.
Original malformed report and reversible syntax-only recovery are retained
in reviews/2026-10-30-complement-transfer/, with all optional adjudications.
The weighted projection dependency is accepted at1242590. This is standard
deterministic groundwork, not novelty or a sharp moment theorem.
Full original goal remains active.

## 1. Fixed objects and conclusion

Use exactly notes/spectral-ground-family.md and
notes/spectral-weighted-projection.md: the fixed actual d1 family
H_b=-d2-bU, b in K=[b0,b1], M=||U||infinity, positive normalized p_b,
0<l<=lambda_b<=L, mu_b=sqrt(-E2(b))>=0, and a fixed d>0 with
lambda_b-mu_b>=d. The latter is the accepted rate gap, not a wave bound.
Take beta=l/2 and the weighted projection constants from the weighted note.
The physical P_b(t) and F are exactly those of
notes/local-causal-young-flow.md Sections4-5: F is the closure of compact
smooth phases PLUS both constants in uniformly local E=H1/2 x H-1/2.

We prove, uniformly b in K and t>=0,

 ||P_b(t)(I-Pi_b)||_(F->F) <= C_eta exp((lambda_b-eta)t),    (1)

for eta=min(d,beta,l)/2>0. In particular eta<inf_b lambda_b.
No assertion about products of changing b, random errors or final averages
is included in (1). All uses of the weighted note below are explicit.

## 2. Uniform fractional phase identification

Set c=1+b1 M and A_b=H_b+c, B=1-d2. Their common form domain is H1, and

 B<=A_b<=cB                                                (2)

in quadratic forms, since 0<=b1M-bU<=b1M. Both operators are >=1.
We give the fractional comparison rather than assume an L2 estimate
automatically holds in E. If positive self-adjoint operators T,S>=1
with common form domain obey T<=S, then for every t>0

 <f,(T+t)^(-1)f> >= <f,(S+t)^(-1)f>.

Indeed each side is the supremum over the common form domain of
2 Re<f,u>-<u,(T+t)u> or the corresponding S expression. Completing
the square in the form norm proves this variational identity, with
maximizer (T+t)^(-1)f. Thus I-t(T+t)^(-1)<=I-t(S+t)^(-1).
The scalar identity

 sqrt(x)=(1/pi) integral_0^infinity t^(-1/2) x/(x+t) dt

follows by substituting t=x s and then s=r2, whose integral is pi.
Apply the spectral theorem and Tonelli to its nonnegative quadratic
forms. Integrating the preceding resolvent inequality, first on finite
intervals then by monotone convergence, proves T^(1/2)<=S^(1/2) in
forms, including the form-domain inclusion. Apply this twice to (2):

 ||B^(1/4)v||2 <= ||A_b^(1/4)v||2
                  <= c^(1/4)||B^(1/4)v||2.                 (3)

The domain is exactly H1/2, with uniform constants. By Hilbert duality
under the L2 pairing, the completion of L2 in ||A_b^(-1/4)w||2 is
H-1/2, with uniform equivalent norms. Explicitly its norm is the supremum
of |<w,v>| over ||A_b^(1/4)v||2<=1; the spectral theorem gives the equality
for w in L2, and completion extends it. Define E_b by the norm

 ||(v,w)||_(E_b)^2=||A_b^(1/4)v||2^2+||A_b^(-1/4)w||2^2.    (4)

Equations (3)-(4) identify it with global E uniformly over b. This proof
uses the self-adjoint spectral theorem already implicit in the accepted
ground note; no new external fractional-domain theorem is imported.

## 3. Global complementary wave calculus, including threshold zero

Let Q_b=I-|p_b><p_b| on L2. It commutes with A_b and extends as a
contraction on both A-weighted entries of (4). Its spectral support for
H_b lies in [E2(b),infinity)=[-mu_b^2,infinity). Define real functions

 C_t(h)=cos(t sqrt(h)), S_t(h)=sin(t sqrt(h))/sqrt(h), h>0;
 C_t(0)=1, S_t(0)=t;
 C_t(h)=cosh(t sqrt(-h)),
 S_t(h)=sinh(t sqrt(-h))/sqrt(-h), h<0.

The spectral wave matrix on the Q phase is

 (v,w) -> (C_t(H_b)v+S_t(H_b)w,
            -H_b S_t(H_b)v+C_t(H_b)w).                    (5)

After the isometry (v,w)->(A_b^(1/4)v,A_b^(-1/4)w), its four scalar
entries are C_t(h), sqrt(h+c)S_t(h),
-h S_t(h)/sqrt(h+c), C_t(h). Here h+c>=1. Uniformly on the stated
spectral support, their absolute values are <=C(1+t)exp(mu_b t).
For h>=0, use |S_t(h)|<=min(t,h^(-1/2)); split h<=1 and h>=1
for the upper off-diagonal entry. The lower one is bounded by1 because
sqrt(h)/sqrt(h+c)<=1. For -mu_b^2<=h<0 use
|S_t(h)|<=t exp(mu_b t), |C_t(h)|<=exp(mu_b t), and
|h|<=b1M, 1<=h+c<=c. These bounds also cover mu_b=0 without dividing
by mu_b or assuming a second negative eigenvalue exists. Spectral integration
and the triangle inequality give the corresponding bounded operator estimate
on (4), hence on E.

On the ground phase, the wave complement I-Pi_b retains just
(v,w)=(a p_b,-lambda_b a p_b), evolving by exp(-lambda_b t).
The rank-one branch projections have uniformly bounded E_b norms, by
l<=lambda_b<=L and 1<=c-lambda_b^2<=c. Combining the Q phase and this
decaying branch yields

 ||P_b(t)(I-Pi_b)||_(E->E) <= C(1+t)exp(mu_b t).             (6)

To justify that (5) is the NAMED physical flow, first use smooth compact
initial phases. The functional-calculus solution lies continuously in
H2 x H1 on every finite horizon (the same scalar bounds at these higher
A scales prove this), has u_tt=-H_b u in L2, and satisfies the free
Duhamel equation. One can obtain that identity by differentiating the
free variation-of-constants formula, or first on bounded H_b spectral
intervals and then passing in H1 x L2. Uniqueness of that equation follows
from Picard/Gronwall, since (v,w)->(0,bUv) is bounded on global E: bound
H1/2->L2, multiplication by bounded U on L2, and L2->H-1/2. The accepted
physical flow satisfies the same equation. Equality on compact smooth
phases extends to all global E by density and finite-horizon boundedness.
This does not assert that global E is dense in F.

## 4. Localization, finite propagation and the missing projection tail

Choose smooth kappa_(j,t),0<=kappa<=1, equal1 on
[j-t-4,j+t+4] and supported in[j-t-5,j+t+5], with every derivative
bounded uniformly for j integer and t>=0. A product of fixed smooth
left/right transition functions gives this family. With the accepted
partition rho_k and chi_k, expand kappa z as the finite sum
kappa rho_k chi_k z. There are <=C(1+t) contributing k. Every multiplier
has uniformly bounded derivatives, so the accepted local Sobolev
multiplier bounds give

 ||kappa_(j,t) z||E <= C(1+t)||z||F.                       (7)

The localized phase is global E; (7) uses the triangle inequality, not
an unjustified orthogonality. Multiplication by 1-kappa is bounded on F
uniformly; compact localization is global E and constants are handled
by the defining compact-plus-constant closure.

For completeness, the bounded-potential physical wave has propagation
speed1 on F. Iterate its free Duhamel equation: every free propagator
expands distributional support by at most its time increment; multiplication
by U preserves support. Each finite Picard term consequently has that
support property. The series converges on each finite horizon in F by
the usual factorial Volterra bound. Distributional testing is continuous
on F, so the support property survives the limit. Thus, since
supp chi_j is contained in[j-3,j+3],

 chi_j P_b(t)z=chi_j P_b(t)(kappa_(j,t)z).                  (8)

Write R_b(t)=P_b(t)(I-Pi_b). The weighted note supplies commutation and
P_b(t)Pi_b=exp(lambda_b t)e_b ell_b. Subtracting this from (8) gives
the EXACT identity

 chi_j R_b(t)z=chi_j R_b(t)(kappa z)
                +exp(lambda_b t)chi_j e_b ell_b((kappa-1)z). (9)

The second term is essential even when the input is a constant.
Using (6)-(7) and the uniform multiplier bound for chi_j, the first
term in (9) has E norm <=C(1+t)^2 exp(mu_b t)||z||F.

For the second term, the weighted note's bounds on p_b,p_b',p_b''
imply ||chi_j e_b||E<=C exp(-beta|j|), uniformly b,j. Also kappa=1
on its inner interval, so 1-kappa can be nonzero only where
|x-j|>=t+4, which implies |x|>=t+4-|j|. Its bounded derivatives
and the same absolutely summable local dual estimates yield

 |ell_b((1-kappa)z)|
       <=C exp(-beta(t-|j|)_+)||z||F.                     (10)

Here r_+=max(r,0). If t<=|j|, the uniform dual bound suffices; if t>|j|,
sum only cells meeting the stated exterior and absorb their fixed width
in C. Multiplication of the two bounds is <=C exp(-beta t)||z||F, since
|j|+(t-|j|)_+>=t. Taking the supremum in j in (9) proves

 ||R_b(t)||_(F->F)
   <=C[(1+t)^2 exp(mu_b t)+exp((lambda_b-beta)t)].          (11)

All operators already map F to F by the accepted physical flow and
weighted projection; the estimate is for that F norm. No passage through
a density assertion about global E in F or a global L2 norm of constants
has occurred. In particular distant output cells are included in (10).

## 5. Uniform exponential margin and scope

Let m=min(d,beta,l)>0 and eta=m/2. Then mu_b<=lambda_b-2eta,
lambda_b-beta<=lambda_b-2eta, and 0<eta<lambda_b. For every t>=0,

 (1+t)^2 exp(-eta t)<=2+4/eta^2.                          (12)

Indeed (1+t)^2<=2+2t^2 and exp(eta t)>=(eta t)^2/2. Combining
(11)-(12) proves (1), with a constant depending only on the frozen family
and partition. This proves the claimed candidate complementary bound.

Finite controls required before downstream use: S_t(0)=t; ground decaying
partner not removed; sign and exact tail term in (9); geometry for both
|j|<=t and |j|>t; positive uniform margin and polynomial absorption.
The fractional-domain/resolvent and actual-flow identifications are analytic
obligations for independent review, not Lean-certified deductions. No
spectral foundation/package/companion is introduced.

Still open: changing-profile/random-error cone and full product, entrance
transient and final fractional block, positive terminal displacement
average, Riesz mask perturbation, stochastic event/cost/variational
optimization, original higher dimensions and source normalization.
This candidate does not prove a sharp moment constant, novelty, or
whole-paper/circulation clearance. Canonical TeX/PDF untouched.
