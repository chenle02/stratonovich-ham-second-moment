# Preliminary audit of the printed variational normalization

[held back until the source author has been told]

This audit attempted to refute the root's proposed discrepancy by checking the
actual PDF, normalization, functional domain, kernel inequality, time operator
bound and spatial dilation. No defeating factor or error was found under the
usual meaningful finite-energy interpretation of the displayed variational
functionals. The printed domain's omitted integrated-energy/measurability
condition is retained explicitly below. This is preliminary GPT-family work,
not an independent cross-family verdict or permission to change the manuscript.

**Scope:** a potential incompatibility among the printed constants, not a claim
that the SPDE or its asymptotic conjecture is false. No silent repair is proposed.
This is unrelated to the separately unadopted citation/sign proposal for(1.24).
No canonical manuscript, source, goal, bibliography or external communication
was changed by this task.

## 1. Exact edition and pages actually viewed

Author source: `sources/chen-2026-author/aap-chen-2025.pdf`,64pages,
SHA256 `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.
I freshly rendered and viewed PDF pages **2,3,4,13** at2100-pixel maximum size;
images are in `pages/` and hashes in `evidence.json`. Text extraction was only
navigation. The older llm_pack TeX is not this version and is NOT used as an
authority for the formulas below.

Literal observations:
- p2: covariance is |s-t|^(-alpha0)gamma(x-y), with no additional temporal
  amplitude; initial data are(1,0).
- p3: Theorem1.2 permits d=alpha=1 and0<alpha0<1,alpha+alpha0<2.
  Its(1.10) uses the same map L on E_star for the lower bound and E for
  the upper bound.
- p4,(1.11): E has the raw temporal kernel and gradient penalty **1**.
- p4,(1.12): E_star has gamma0_star and gradient penalty **1/2**.
  Both suprema are over the **same Ad** immediately defined below.
- p4,(1.13):

    gamma0_star(u)=1/Gamma(alpha0) integral_0^infinity
      exp[-(lambda+lambda^2/(2(4-alpha-2alpha0)))|u|]
      lambda^(alpha0-1) d lambda.

  The text then asserts E_star<E.
- p13 explicitly permits gamma=delta_0 in d1 under the generalized-covariance
  convention; this test does not replace white noise by a covariance function.

The white spatial covariance is the physical distribution delta_0. Its action
in these energy forms is integral g_s(x)^2g_r(x)^2 dx; no Fourier2pi factor
appears after this physical-space evaluation.

## 2. The legitimate fixed parameter test and functional domain

Take

  d=1, alpha=1, a=alpha0=1/10, gamma=delta_0.

The standing threshold is1+1/10<2. The source's printed Ad requires that every
slice g(s,.) lies in W^(1,2)(R), with integral |g(s,x)|^2dx=1. It does not
explicitly list time measurability or finiteness of the integrated gradient
energy. In interpreting the displayed integrals, use measurable real-valued
profiles with

  T=integral_0^1 B_s ds<infinity,
  B_s=integral_R |partial_x g(s,x)|^2 dx.

This is the standard well-defined variational class. The upper bound below
covers every such profile, and the lower bound uses smooth constant-in-time
profiles, admitted by the printed class and every usual finite-energy variant.
A profile for which both positive energy and gradient cost are infinite gives
an undefined infinity-minus-infinity, not an ordinary larger variational value.
The source's own finite-variational assertion requires a meaningful convention;
this audit does not invent one that changes its constants. If a different
nonstandard domain/renormalized meaning was intended, it must be supplied
explicitly before applying this preliminary conclusion to it.

## 3. A common finite positive Sobolev ratio, with no numerical sharp constant

Define for real g in H1(R),norm_L2(g)=1,

  I(g)=integral_R g(x)^4 dx,
  B(g)=integral_R |g'(x)|^2 dx,
  R=sup I(g)/sqrt(B(g)).

B(g)>0 for every normalized g: derivative zero would make g a constant,
and a nonzero constant is not L2(R). Also0<R<infinity. Indeed the elementary
one-dimensional Sobolev estimate

  ||g||_infinity^2 <=2 ||g||_2 ||g'||_2

follows from integrating the derivative of g^2 and Cauchy–Schwarz (first for
smooth compactly supported g, then H1 density). Thus I(g)<=2sqrt(B(g)), so
R<=2. A normalized nonzero smooth compactly supported function gives R>0.
No optimizer, sharp Gagliardo–Nirenberg value, static M, or disputed white-noise
constant is used.

For normalized g_s,g_r, spatial Cauchy–Schwarz gives

  A_sr:=integral g_s^2 g_r^2
    <=sqrt(I(g_s)I(g_r))
    <=R B_s^(1/4)B_r^(1/4).                                  (A)

All powers here depend on B being the **squared** derivative L2 norm.
Changing that convention would change the powers; it has been kept fixed.

## 4. Independent upper bound for the printed E

For k_a(s,r)=|s-r|^(-a), its row integral on[0,1] is

  integral_0^1 k_a(s,r)dr
    =[s^(1-a)+(1-s)^(1-a)]/(1-a)
    <=K:=2^a/(1-a).

Concavity of u^(1-a) gives the maximum at s=1/2, so this is the exact row
supremum. Put f(s)=B_s^(1/4). Using2f(s)f(r)<=f(s)^2+f(r)^2 and symmetry,
not an assumed spectral eigenvalue formula,

  integral integral k_a(s,r)f(s)f(r)dsdr
    <=K integral f(s)^2 ds
     =K integral sqrt(B_s)ds
    <=K sqrt(T).

The last step is Cauchy–Schwarz on the unit time interval. By(A), the positive
interaction term is finite when T is finite. The printed objective is bounded by

  R K sqrt(T)-T <=R^2 K^2/4.

Therefore

  E <=R^2 K^2/4.                                             (U)

The time-dependent choice of g has not been restricted to constant profiles
for this upper bound. It therefore cannot be evaded by changing the spatial
profile with time within the finite-energy class.

## 5. Independent lower bound for the printed E_star

The damping parameter at this fixed test is

  D=4-alpha-2a=14/5.

Since the integrand defining gamma0_star is decreasing in |u|,
for0<|u|<=1 its value is at least gamma0_star(1). At |u|=0 it has an extended
infinite value, harmless on the time diagonal. At u=1, view
Gamma(a)^(-1)e^(-lambda)lambda^(a-1)d lambda as the Gamma(a,rate1)
probability density. From exp(-x)>=1-x for x>=0 and its second moment
E[lambda^2]=a(a+1),

  gamma0_star(1)
    >=1-a(a+1)/(2D)
     =1-11/560=549/560=:m.                                  (K)

The factor2D and the normalization Gamma(a) have both been checked against
rendered(1.13). No missing time-interval length appears: the unit square has
Lebesgue area1. For a constant-in-time normalized spatial profile g, the
positive energy is at least m I(g), while the printed gradient penalty is
B(g)/2.

Apply the mass-preserving spatial dilation g_l(x)=sqrt(l)g(l x),l>0:

  ||g_l||_2=1, I(g_l)=l I(g), B(g_l)=l^2 B(g).

These profiles remain constant in time and admissible. Maximizing
m l I(g)-(l^2/2)B(g) over l gives the value

  m^2 I(g)^2/[2B(g)].

Take a sequence of g whose ratio tends to R; attainment is unnecessary.
Thus

  E_star >=m^2 R^2/2.                                       (L)

The temporal interaction used here is finite: gamma0_star(u)<=|u|^(-a),
whose integral on the unit square is finite. The upper argument with penalty
1/2 also gives E_star<=K^2R^2/2. Similarly the raw kernel is at least1 on
the unit square, so constant profiles and dilation give E>=R^2/4>0.
Both quantities are therefore finite and positive under the same usual domain.

## 6. Exact separation and source theorem consequence

At a=1/10,

  K=(10/9)2^(1/10)<11/9,

because(11/10)^10>2. Exact rational controls give

  2(549/560)^2-(11/9)^2 =5440681/12700800>0,

or equivalently

  (549/560)^2/2-(11/9)^2/4=5440681/50803200>0.

Combining(U),(L),R>0 gives E_star>E for the literal printed objectives.
The rational controls are in `controls.json`; this is not a floating fit.

For alpha=1, the common source map L(v) in(1.10) is a positive constant times
v^(1/4), so it is strictly increasing for positive v. More generally its power
is(2-alpha)/(2(3-alpha))>0. Hence the displayed lower constant L(E_star)
would exceed its displayed upper constant L(E). Such an ordering is
incompatible with a lower-bound<=liminf<=limsup<=upper-bound assertion for
one real asymptotic sequence. This is a discrepancy in the combined printed
normalizations; it does not identify the intended correction or disprove the
underlying asymptotic statement under its intended constants.

Mechanism sanity check: as a approaches0, the raw row bound tends to1 and
the lower estimate m tends to1; the two gradient penalties remain1 and1/2.
The dilation optimum consequently differs by a factor approaching2. This is
only an explanation of why the fixed positive-a test is plausible; no excluded
alpha0=0 theorem is used in the certificate above.

## 7. Attempts to defeat the finding and remaining uncertainty

| Possible failure | Audit result |
|---|---|
| OCR/old-version mixup | Refuted: current hash and actual rendered pages read; old llm_pack excluded. |
| Different admissible classes for E and E_star | Not printed: both use the same Ad. |
| Extra1/2 in E's gradient cost | Not present in(1.11); it is present in(1.12). |
| Wrong damping denominator | Recomputed2(4-1-2/10)=28/5; agrees with image. |
| Missing Gamma or covariance amplitude | Gamma(a) normalized exactly; physical gamma=delta0 evaluated without Fourier factors. |
| White case excluded | It is explicitly included in Theorem1.2 and the generalized convention. |
| Restricting E to constant-time g | Not done; upper bound covers every measurable finite-energy profile. |
| Assuming a sharp Sobolev optimizer/value | Not done; same abstract finite positive R used on both sides. |
| Wrong dilation powers | Directly recomputed: I scales l and B scales l^2. |
| Finiteness/undefined objectives | Proof uses the standard meaningful finite-energy domain; printed Ad omits this condition and must be clarified if another meaning is intended. |
| Different increasing maps in(1.10) | Images show the same map with E_star/E substituted. |

No defeating mathematical error was found. The exact intended source
normalization is still UNKNOWN. A different model-family reviewer must now
recompute the finding from the pinned pages, with an explicit invitation to
refute it; routine checklist agreement is insufficient. Until then this remains
a preliminary source-normalization audit, not an accepted correction.
