# Fixed-mask Young evolution on Sobolev phases plus constants

COMPLETE CANDIDATE, not adopted before independent full proof review.
This applies known Banach Young calculus to the SAME masked source equation.
Full original all-dimensional sharp second-moment goal remains ACTIVE.

## 1. Scope, named inputs and the exact new consumer

Use original H:homog, d=1,2,3; a in(0,1); alpha+a<2;
0<alpha<d or alpha=d=1. Choose the freely specified real smooth mask
m=zeta_R with values in[0,1], equal1 on B_R and supported in the closed
ball of radius2R. Fix R,T>0 and

 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<beta<min(1-a/2,(3-a-alpha)/2),
 E=H^(1/2)(R^d) x H^(-1/2)(R^d).

Named OWN accepted inputs, not re-certified here:
- actual-operator-driver.md Theorem, Section4(12): same-W Gaussian compact
  driver M_E in Ctheta(B(E)), sqrt(p) norm moments, full-phase free group
  on E and physical input/output cutoff identities of deterministic A_j.
- source-operator-convergence.md Theorems1-2: canonical source M_E^rho
  from the same raw A_j, arbitrary-rate all-finite-Lp Ctheta source limit,
  uniform sqrt(p) moments, retaining Gaussian extension, actual source
  ordinary first response on E and Ct,C-infinity-x pointfield versions.
- fixed-mask-moment-transfer.md F2-F3: ordinary source scalar solution
  u_rho^m, and CONDITIONAL tested-moment transfer if its averages convergeL2.

The integration input is the standard Banach Young estimate from the held
Friz--Hairer Sections1.4-1.5/4.1,(4.3), already used in the dimension-free
Banach argument of local-causal-young-flow.md Section5. We derive its exact
linear consumer below. No d1 HS/noise-multiplier result or analytic-semigroup
Theorem12.18 is imported. Independent method novelty is not asserted.

We prove Y1-Y4 of the frozen target: on F=E directsum R2, construct the
actual raw/source drivers including their constant-response columns,
apply Young stability and Gaussian moments, identify actual ordinary source
phases, and construct the W-measurable average required by F3. Constants
throughout may depend on model, mask shape, R,T, gamma/theta/beta, auxiliary
physical cutoffs and fixed test. No growing-R or growing-T estimate follows.

## 2. The distributional phase and full free-wave propagation

Let F=E directsum R2 with norm squared ||e||E^2+c1^2+c2^2. Embed it into
real phase distributions by (e,c1,c2)->e+(c1*1,c2*1). This is injective.
Indeed, the Fourier transform of a nonzero constant is a nonzero multiple
of delta0. Every Hsigma Fourier transform is locally L2 near frequency0,
because its weight is bounded above/below there. A locally L2 function f
cannot represent delta0: test against chi(xi/epsilon), chi(0)=1, compactly
supported near0. Its integral against f is at most
||f||L2(B_epsilon) epsilon^(d/2)||chi||2, tending to0, whereas delta0 gives1.
This excludes constants from BOTH Sobolev entries, and proves injectivity.

The embedding is continuous into distributions: for compact smooth phase
tests, use the Hsigma/H(-sigma) dual norms for e and the two test integrals
for c. These bounds are uniform on bounded test families with a common
compact support. F is complete/separable Hilbert as a direct sum. The map
i:E->F is isometric with closed proper range, not dense range. Put
e0=(0,1,0), representing physical data(1,0).

For any real smooth compact psi, Lpsi(e,c1,c2)=psi e+(c1 psi,c2 psi) is
bounded F->E. Here is the spatial multiplier justification in all d.
In the unitary Fourier convention, the weighted kernel for multiplication
on Hsigma obeys, by the two Peetre inequalities,

 <xi>^sigma <eta>^(-sigma) <= 2^(|sigma|/2)<xi-eta>^|sigma|.

Thus its absolute action is bounded by convolution with
2^(|sigma|/2)c_d |psihat(q)|<q>^|sigma|, an L1 kernel. The elementary L1*L2
inequality gives boundedness for sigma=+/-1/2. Also psi is in both Sobolev
spaces, so the constant columns have bounded E norm. This proves the claim.

Define the free group by

 S_F(t)(e,c1,c2)=(S_E(t)e,c1+t c2,c2).                            (1)

It is strongly continuous with finite-horizon norm bound C_T: the global
E bound is a named input (also follows from the sine quotient and Bessel
weights), and the finite constant block is triangular. Formula(1) is the
actual distributional free wave. For t>0 its kernel matrix is

             [[partial_t G_t, G_t],[Delta G_t, partial_t G_t]].

Every entry is a compactly supported distribution in the closed ball of
radius t, including in d3. On constants the entries have masses1,t,0,1,
giving exactly(1); time reversal gives negative t. Compact-support
distribution convolution also defines this matrix on E plus constants.
Consequently full-phase finite propagation holds for the TOTAL data e+c,
even when e and c cancel locally: if e+c vanishes on the enlarged initial
region, convolution against each translated compact kernel vanishes in
the smaller cone. One cannot check the two summands separately. Equivalently
localize constants with a cutoff equal1 on the enlarged region and use the
constant kernel masses for the remainder. No operator-norm continuity of
S_E or S_F is claimed. This proves Y1.

## 3. Actual driver extension, including both constant columns

Choose chi real compact smooth, equal1 on B_(2R+T+1) and supported inside
B_(2R+T+2). For the raw finite sums and source finite sums, accepted(12)
holds termwise with the SAME chi, since both retain deterministic A_j.
Their Ctheta operator-norm limits therefore satisfy, simultaneously in t,

 Dchi M_E(t)=M_E(t)=M_E(t)Dchi,                                  (2)

and likewise M_E^rho for each fixed rho. Take a common path set using a
uniformly convergent subsequence, or rational times and path continuity.
No uncountable-rho path set is asserted.

For psi compact smooth equal1 on a neighborhood of supp chi define

 A_E=M_E Lpsi in Ctheta(B(F,E)), A=i A_E in Ctheta(B(F)),          (3)

and use the same formula for rho. These operators are independent of psi.
For two choices, (Lpsi-Lpsi')z belongs to E and Dchi of it is zero. Equation(2)
kills it. For z=i e, Dchi Dpsi e=Dchi e, so A i e=i M_E e. The columns
on constants are M_E(psi,0), M_E(0,psi), not artificially set to zero.
Compactness is preserved by bounded composition. All values lie in iE.

The bounded linear map M->M Lpsi transfers the accepted source convergence
to every finite Lp Ctheta(B(F,E)), at arbitrary relative cutoff rates.
It also transfers uniform sqrt(p) norm moments. For completeness these give
uniform square-exponential moments: if ||X||Lp<=C sqrt(p), then
E X^(2n)<=C^(2n)(2n)^n and n!>=(n/e)^n. Expanding exp(cX²), its nth term is
at most(2e c C²)^n; choose c<1/(2e C²). All constants listed in Section1
are fixed. Raw A is W-measurable by its raw countable Gaussian construction
and the deterministic map(3). The source may use the retaining auxiliary J.

We next prove the source identity on constants, not by density of E in F.
For a fixed rho take the actual pointfield on its Ct,C-infinity-x event
and set b(r)=mY_rho(r). It has one compact spatial support and is continuous
in L-infinity and L2 on[0,T]. For any such b,

 B(b)(e,c1,c2)=(0,b(e1+c1)) in E,
 ||B(b)||B(F,E)<=||b||infinity+||b||2.                           (4)

Indeed e1 belongs to L2 and H(-1/2) norm is bounded by L2 norm. For every
fixed state z in F,
C(r)z=S_E(-r)B(b(r))S_F(r)z is strongly continuous in E, uniformly bounded
as an operator F->E on this fixed horizon. Its statewise integral defines
a Lipschitz B(F,E) primitive, without any Banach Radon--Nikodym assumption.

By the full propagation just proved, S_F(r)z and S_E(r)Lpsi z have the same
displacement near supp m: the initial difference is zero on the entire
needed enlarged ball. Multiplication by b(r) kills this difference.
The accepted ordinary source identity on E then gives, statewise,

 int_0^t C(r)z dr=M_E^rho(t)Lpsi z=A_E^rho(t)z.                  (5)

The integral bound and separability/rational times give operator-path
identity on a single event for this fixed rho. This proves Y2, including
its actual source-response assertion on all of F.

## 4. Apply the standard Banach Young estimate at this exact phase

We recall the linear deduction to specify the application. For a driver
D in Ctheta([0,T];B(F)), D(0)=0, theta>1/2, Young integration under ordinary
LEFT composition has estimate

 ||int_s^t dD(r)V(r)-D(s,t)V(s)||
           <=C_theta [D]_theta [V]_theta |t-s|^(2theta).         (6)

On an interval length ell use sup||V||+ell^theta[V]_theta and fixed initial
value. The integral map is a contraction on paths with that initial value
when C_theta[D]_theta ell^theta<=1/4 (enlarge the constant if needed).
It gives a unique Ctheta solution U_D(t,s) of I+int_s^t dD U_D. The local
norm is at most2 times the initial norm. Cover any subinterval by at most
C_T(1+||D||Ctheta^(1/theta)) such pieces. Patching and uniqueness give the
composition law and the uniform bound

 sup_(s<=t<=T)||U_D(t,s)||
       <= C_T exp(C_T(1+||D||Ctheta)^(1/theta)).                 (7)

The same local estimate for differences, on a common partition for drivers
in a bounded Ctheta ball, proves local Lipschitz dependence into the uniform
norm on the time triangle. Small local increments can be made within1/2
of I, hence invertible by a Neumann series; their products are invertible.
The formula U_D(t,s)=U_D(t,0)U_D(s,0)^(-1) then gives joint operator-norm
continuity in(s,t). Uniqueness here is in the Ctheta Young class. These
are standard consequences of(6), not an invocation of a bounded nonlinear
vector-field theorem on an unbounded linear vector field.

Apply this to D=A and D=A^rho. The path versions are strongly measurable
in separable closed path spans by the named driver construction; (3) and
the continuous Young map preserve strong measurability in the uniform
triangle norm. Let pi_C:F->R2 be the continuous constant-coordinate map.
Since pi_C A(s,t)=0, applying pi_C to the Young Riemann sums proves

          pi_C U_A(t,s)=pi_C, (U_A(t,s)-I)F contained in iE.    (8)

The same holds for rho. The second assertion uses closedness of iE, not
density. It is interaction-phase preservation only.

For every finite p the source evolutions converge in the uniform
operator-difference norm in Lp. To see this without an unstated random
Lipschitz constant, first restrict both driver norms to a fixed ball K.
Local Lipschitz dependence and driver convergence imply convergence in
probability on that ball. Uniform Gaussian norm tails make its complement
arbitrarily small uniformly in rho, proving convergence in probability
without restriction. Set q=1/theta<2. For any fixed p and positive c,
pC(1+x)^q<=c x²+C_(p,c). The uniform square-exponential estimate of Section3
and (7) therefore give uniform moments of every order for the evolution
sup norms. They give uniform integrability of the pth difference powers,
so convergence is in Lp, not just probability. This proves Y3.

## 5. Physical evolution and the actual ordinary source solution

Define

       P_A(t,s)=S_F(t)U_A(t,s)S_F(-s).                          (9)

It has the composition law and is strongly continuous on states. Its
physical constant coordinates are (c1+(t-s)c2,c2) by(1),(8). Uniform
operator source-difference convergence in every finite Lp follows from
the bound C_T² times the interaction difference. There is no assertion
that each physical operator family is operator-norm continuous. Strong
measurability of its uniform differences follows from the bounded linear
map V(t,s)->S_F(t)V(t,s)S_F(-s) into the bounded-family supremum-norm space.

For fixed rho, (5) identifies the driver primitive. Young Riemann sums on
a state give

 sum_j [A^rho(t_(j+1))-A^rho(t_j)]U(r_j,s)v
       =sum_j int_(t_j)^(t_(j+1)) i C(r)U(r_j,s)v dr,

with left endpoints r_j=t_j. The right side converges to the statewise
strong integral of i C(r)U(r,s)v, since U is uniformly continuous and C
is uniformly bounded on this horizon. Thus the Young equation is exactly
the ordinary interaction integral on states. Multiplying by free groups
gives the full-phase Duhamel equation with B(b):F->E from(4). Its unique
Ct(F) solution follows by the bounded-coefficient Picard argument (or
Gronwall), since S_F is strongly continuous and bounded on the horizon.
No operator-norm derivative of S_F or B(F)-valued density is assumed.

For initial e0, identify its displacement with u_rho^m as follows. Iterate
the ordinary full-phase Duhamel equation. The nth phase term has norm
at most C_T^(n+1) B_T^n T^n/n!, with B_T=sup||B(b(r))||B(F,E), finite
on this fixed source event. Its displacement is exactly the nth ordered
Green-chain term X_(rho,n)^m, by the wave kernel convention. The phase
series converges in Ct(F), hence distributionally. Its displacement series
also converges locally uniformly to the actual continuous scalar mild
solution u_rho^m by accepted F2's compact-cone factorial bound. Distribution
limits agree. This identifies the displacement of P_(A^rho)(t,0)e0 with
u_rho^m as a distribution and its continuous source version. In particular
their smooth spatial averages agree. No point trace of H^(1/2) is used,
and no global bound on an unmasked Gaussian field is assumed.

## 6. Construct the raw average and close the exact F3 premise

Fix phi>=0 real smooth compact, integral1. Define

 J_phi(e,c1,c2)=<e1,phi>+c1,
 Z_m(t,phi)=J_phi P_A(t,0)e0.                                   (10)

Sobolev duality gives ||J_phi||<=sqrt(||phi||H(-1/2)^2+1). Here Z_m is the observable called A_m in the frozen target. The raw variable
in(10) is W-measurable, since the raw driver is W-measurable and the Young
and deterministic maps are continuous/measurable as above. It does not
depend on an auxiliary J used to realize source cutoffs.

The source averages equal J_phi P_(A^rho)(t,0)e0 by Section5. This is also
the Bochner L2 average in F2: that average is represented by the same
pathwise spatial integral, by F2's measurability and absolute Fubini bounds.
The all-finite-Lp uniform operator-difference convergence of Section5 gives

 int phi(x)u_rho^m(t,x)dx -> Z_m(t,phi) in every finite Lp,      (11)

at arbitrary relative source cutoff rates. Bound the difference by
||J_phi|| ||e0|| times the uniform physical operator difference. Thus in
particular the EXACT assumed L2 premise of accepted F3 is now established,
on the actual retaining source space. F3 yields

                     E|Z_m(t,phi)|²<=E|u(t,0)|².               (12)

Here u is the ORIGINAL canonical stationary Stratonovich model, and all
limits are at fixed R,T before asymptotics. This proves Y4. It constructs
an actual tested observable, not a raw point evaluation or a pathwise
ordering of solutions. For zero covariance the same construction is the
free constant solution and gives equality.

## 7. Compact deterministic base and the remaining original goal

For the optional base specify real h in C([0,T];C_c^infinity(K)) for one fixed
compact K (all spatial derivatives continuous on the common compact).
Equation(4) applies with h, so the statewise primitive

 int_0^t i S_E(-r)B(h(r))S_F(r)dr

is Lipschitz in B(F), with range in iE and bound
C_T sup_r(||h(r)||infinity+||h(r)||2), in particular bounded by the displayed
W1infinity-plus-L2 budget of the target. Replace A by A_h+gA. Equations(6)-(9)
still apply; the deterministic bounded primitive and bounded g preserve
uniform square-exponential driver bounds after a deterministic shift.
The same probability/uniform-integrability argument proves all-finite-Lp
source convergence, with constants uniform on bounded displayed budgets.
The strong-integral and source Picard arguments apply to h+g mY_rho, using
the union of their fixed compact supports. These are individual bounds,
not an uncountable coupled-version assertion. Only h=0,g=1 enters(12).
No raw Cameron-shift identity follows merely from this deterministic base.

The seven analytic groups here are phase/distribution/free propagation;
actual cutoff extension; source response on constants; Young flow/range;
Gaussian moments and measurability/source limit; ordinary source identity;
actual raw tested-average transfer. Finite block/loop controls test selected
algebraic failure modes, not these continuum proofs. Existing71 finite
facts/18 Lean seams/L0 unchanged pending worthwhile typed finite consumers.

Next required work: compact-mean negative trial/gap and ground family on
this exact F, full-phase projections/complement and growing products, raw
Gaussian shift/event/cost and all-alpha variational lower comparison.
The old d1 uniformly-local estimates are not silently estimates on F.
Sharp upper constant, author-energy dictionary and conditional exact limit
remain open. No full-goal completion, companion/package/HPC/contact,
Skorohod development, source repair, TeX/PDF/wiki or publication claim.
