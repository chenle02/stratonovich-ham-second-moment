# Weighted two-wave sufficiency screen

Date: 2026-10-28 UTC. Status: **UNREVIEWED CANDIDATE — elementary argument
closes for the unsmoothed two-wave object**. This is GPT-author work, not an
accepted theorem or independent certification. The current manuscript, source
PDFs, siblings, registry and git were not changed. No all-order pairing
algorithm, factorial estimate, full moment theorem or novelty claim is supplied.

The bounded falsification screen found no defect in the proposed geometric
majorant after checking its sign-sensitive split. The argument below states
all its elementary ingredients; it does not treat the pending review of
quadrature-memo.md as an accepted premise. No floating calculation is used.

## 1. Candidate statement and exact scope

Let

  G_h(y)=1_(|y|<h)/(2 pi sqrt(h^2-|y|^2)),
  I_alpha(h;Z,W)=integral_0^h du integral_R^2 dy
                   G_u(y)G_(h-u)(Z-y)|W-y|^(-alpha).

For3/2<alpha<2 and alpha-1<=q<1, the candidate conclusion is

  I_alpha(h;Z,W) <= C_(alpha,q) h^(2q-alpha)G_h(Z)^(2q-1)        (WC)

for every h>0 and Z,W in R^2, taking G_h=0 on and outside its boundary.
For alpha=3/2, the same conclusion holds for every1/2<q<1.
The constant is finite and independent of h,Z,W. Concrete constants appear
below. No statement at alpha=2 or q=1/2 is made.

For the original Stratonovich application, one still requires
0<alpha0<1/2 and alpha+alpha0<2. Alpha0 is absent from this deterministic
spatial assertion. A temporal pullout has its separately recorded remote-gap
cost; neither this assertion nor that pullout proves the needed all-order
iteration.

The change u=hv, y=hY gives
I_alpha(h;Z,W)=h^(1-alpha)I_alpha(1;Z/h,W/h). Also
h^(2q-alpha)G_h(Z)^(2q-1)=h^(1-alpha)G_1(Z/h)^(2q-1).
It therefore suffices to prove the normalized case h=1.

## 2. Exact time density, rederived

Put z=|Z|, a=|y|, b=|Z-y|. Both wave kernels are nonzero precisely when

  a<u<1-b.

Thus their time integral is zero unless a+b<1. Inside that open ellipse,
for a,b>0, put L=1-a-b and substitute u=a+L sin(theta)^2. Tonelli and this
ordinary change of variables give

  I_alpha(1;Z,W)=integral_R^2 K_Z(y)|W-y|^(-alpha)dy,
  K_Z(y)=(1/(2 pi^2)) integral_0^(pi/2)
      dtheta / sqrt((2a+L sin(theta)^2)(2b+L cos(theta)^2)).

To verify the elliptic formula without importing an identity, set A=2a,C=2b,
then t=tan(theta). The last integral becomes

  integral_0^infinity dt /
       sqrt((A+(A+L)t^2)(C+L+Ct^2)).

Now t=sqrt(A/(A+L))tan(psi). Since
D=(A+L)(C+L)=1-(a-b)^2 and k=AC/D=4ab/D, this equals

  (1/sqrt(D)) E(k),
  E(k)=integral_0^(pi/2) dpsi/sqrt(cos(psi)^2+k sin(psi)^2).

Consequently

  K_Z(y)=E(k)/(2 pi^2 sqrt(D)),  k=4ab/D.                        (TD)

On a+b<1, D-4ab=1-(a+b)^2>0, hence0<k<1. The exceptional points a=0
or b=0 are null in y; assign extended values there. The upper integrability
bounds below justify their harmlessness even when W equals one of them.
If z>=1, the triangle inequality gives a+b>=z>=1, so the entire time-space
integrand has empty support. The normalized inequality then reads0<=0.
All remaining arguments assume z<1 and delta=1-z^2 in(0,1].

## 3. An elementary logarithmic upper bound for E(k)

For0<k<=1 split the defining integral at psi=pi/4. On[0,pi/4], cos(psi)
>=1/sqrt(2), so this part is at most pi sqrt(2)/4. On the other half put
v=pi/2-psi. For0<=v<=pi/4, concavity of sin on[0,pi/2] gives
sin(v)>=2v/pi, while cos(v)>=1/sqrt(2). Therefore the remaining part is
bounded by

  integral_0^(pi/4) dv/sqrt(4v^2/pi^2+k/2)
    = (pi/2) asinh(1/sqrt(2k))
    <= (pi/2)log(1+sqrt(2))+(pi/4)log(1/k).

The last inequality uses asinh(x)=log(x+sqrt(1+x^2))<=log(1+2x) and
1+sqrt(2)/sqrt(k)<=(1+sqrt(2))/sqrt(k). Define the universal finite constant

  C_E = pi sqrt(2)/4+(pi/2)log(1+sqrt(2))+pi/4.

Both coefficients of the preceding upper bound are at most C_E, giving

  E(k) <= C_E[1+log(1/k)].                                    (EL)

This deliberately nonsharp bound is enough; no elliptic-integral asymptotic
or source theorem is used.

## 4. Geometry when 1/2<=z<1

Partition the ellipse into a<=b and b<=a; their overlap may be counted twice
in an upper bound. On a<=b we have

  a<=1/2,  b>=z/2>=1/4,  b<1.

The reverse triangle inequality gives |a-b|<=z, hence D>=delta.
Also b-a lies in[0,1-2a), so squaring is legitimate and

  D=1-(b-a)^2 >= 1-(1-2a)^2=4a(1-a)>=2a.

Thus D>=(delta+a)/2. For the upper bound there are two sign-sensitive cases.
If z>=2a, then b-a>=z-2a>=0; therefore

  D<=1-(z-2a)^2=delta+4az-4a^2<=delta+4a.

If z<2a, use D<=1 and

  delta+4a > 1-z^2+2z >=1

because0<=z<1. This gives the same upper bound. In particular,

  (delta+a)/2 <= D <= 4(delta+a),
  k=4ab/D >= a/[4(delta+a)].

The weaker denominator4 is kept to simplify constants. Combining(TD),(EL),

  K_Z(y) <= C_N (delta+a)^(-1/2)[1+log(1+delta/a)],
  C_N = sqrt(2) C_E(1+log(4))/(2 pi^2).

Indeed log(1/k)<=log(4)+log(1+delta/a). By symmetry the same estimate uses
b on the region b<=a. Set

  f_delta(r)=1_(0<r<1)(delta+r)^(-1/2)[1+log(1+delta/r)].

Its nonnegative radial profile is decreasing: both positive factors decrease
with r, and the cutoff at1 is downward. As a,b<1 on the ellipse,

  K_Z(y) <= C_N[f_delta(|y|)+f_delta(|Z-y|)]                    (ENV)

almost everywhere, also off the ellipse where K_Z=0.

## 5. The radial rearrangement needed here, proved by layer cake

For any nonnegative radial decreasing f with disk superlevel sets and any
W in R^2,

  integral f(|y|)|W-y|^(-alpha)dy
    <= integral f(|y|)|y|^(-alpha)dy.                          (RR)

To see this directly, write each nonnegative factor as the integral of the
indicator of its superlevel sets. The sets for f are disks B_R(0), and those
for |W-y|^(-alpha) are disks B_S(W). For every R,S,

  area(B_R(0) intersect B_S(W))
    <= min{pi R^2,pi S^2}
    = area(B_R(0) intersect B_S(0)).

Integrate this inequality over the two layer-cake variables by Tonelli.
The argument permits extended values before the final upper bound; it does
not assume finiteness in order to prove finiteness. Open/closed disk endpoints
are null and do not affect it. Translation applies the same result to a
profile centered at Z.

Applying(RR) to(ENV) gives, uniformly in W,

  I_alpha(1;Z,W) <= 4 pi C_N J_alpha(delta),
  J_alpha(delta)=integral_0^1
    r^(1-alpha)(delta+r)^(-1/2)[1+log(1+delta/r)]dr.             (J)

This is the actual Riesz-weighted time-integrated object; no covariance
factor is dropped and no mass-only estimate is substituted for its energy.

## 6. Evaluation of the remaining scalar majorant

For3/2<alpha<2, substitute r=delta*s in(J). On s<=1 use
(1+s)^(-1/2)<=1 and log(1+1/s)<=log(2)+log(1/s). On s>=1 use
(1+s)^(-1/2)<=s^(-1/2) and log(1+1/s)<=log(2). Hence

  J_alpha(delta) <= B_alpha delta^(3/2-alpha),
  B_alpha = (1+log(2))/(2-alpha) + 1/(2-alpha)^2
            + (1+log(2))/(alpha-3/2).                         (B)

All three integrals converge in the stated strict alpha range. Since
q>=alpha-1, q-1/2>=alpha-3/2 and0<delta<=1 imply

  delta^(3/2-alpha) <= delta^(-(q-1/2)).

At alpha=3/2 the same split, retaining the finite upper limit1/delta, gives

  J_(3/2)(delta) <= B_0+(1+log(2))log(1/delta),
  B_0=2(1+log(2))+4.

For eta=q-1/2>0, the elementary maximization of x exp(-eta*x), x>=0,
gives delta^eta log(1/delta)<=1/(e eta). Consequently

  J_(3/2)(delta) <= B_(0,q) delta^(-(q-1/2)),
  B_(0,q)=B_0+(1+log(2))/(e(q-1/2)).                           (B0)

The logarithmic bound at alpha=3/2 is an upper estimate, not a claim that the
actual integral diverges logarithmically. In particular, it need not match
the floating endpoint observations in quadrature-memo.md.

## 7. Geometry when z<1/2

Here D>=delta>3/4 and D<=1. Since a,b<1 on the ellipse,

  k=4ab/D>=4ab,
  1+log(1/k)<=1+log(1/a)+log(1/b).

Thus(TD),(EL) give

  K_Z(y) <= C_F[f_0(|y|)+f_0(|Z-y|)],
  C_F=C_E/(pi^2 sqrt(3)),
  f_0(r)=1_(0<r<1)[1+log(1/r)].

The right side has an extra harmless constant1. Applying(RR) once more,

  I_alpha(1;Z,W) <= 4 pi C_F B_F(alpha),
  B_F(alpha)=1/(2-alpha)+1/(2-alpha)^2.                        (F)

This is finite for every alpha<2 and uniform in Z,W in this subregion.

## 8. Assembly and precise output

For|Z|<1,

  G_1(Z)^(2q-1)=(2 pi)^(-(2q-1))delta^(-(q-1/2)).

For3/2<alpha<2 and alpha-1<=q<1, the estimates above prove the candidate
normalized(WC) with the explicit finite constant

  C_(alpha,q)=(2 pi)^(2q-1)
       max{4 pi C_N B_alpha, 4 pi C_F B_F(alpha)}.

At alpha=3/2 and1/2<q<1 replace B_alpha by B_(0,q). For z>=1 both sides
are zero, as already explained. Scaling proves the stated h>0 form.
All upper bounds are uniform in the remote displacement W. The endpoint
q=alpha-1 is included when alpha>3/2; no strict inequality was needed in
that last exponent comparison.

Combined with the separately written, still-unreviewed necessary-condition
probe, this is a candidate exact q-threshold in the original allowed range:
q>=alpha-1 for alpha>3/2, while all q>1/2 pass at alpha=3/2. Do not report
that threshold as accepted before independent review of both arguments.

## 8a. Ordinary-wave corollary (same unreviewed status)

Let p=2q-1 in(0,1). On |Z|<h, G_h(Z)>=1/(2 pi h). Since p-1<0,

  G_h(Z)^p = G_h(Z) G_h(Z)^(p-1)
            <= (2 pi h)^(1-p)G_h(Z).

Together with(WC), this gives the candidate corollary

  I_alpha(h;Z,W) <= C'_(alpha,q) h^(2-alpha)G_h(Z),
  C'_(alpha,q)=(2 pi)^(2-2q) C_(alpha,q).

The power is exactly2q-alpha+1-p=2-alpha; outside the open support both
sides are zero under the stated boundary convention. This is uniform in W
and also holds with covariance-only mass-one nonnegative smoothing by the
averaging argument below. One admissible fixed choice is q=alpha/2 for
every3/2<=alpha<2: it lies in(1/2,1), and q>=alpha-1. No sharpness of the
resulting constant is claimed. Restoring the ordinary G form alone does not
close an iteration: h is the gap between neighboring retained times, and the
remote temporal covariance and its singular-gap cost remain to be handled.

## 9. Smoothing and consumer boundaries

A narrow extension follows immediately from the uniform-W estimate: if only
the Riesz covariance is convolved with a mass-one nonnegative spatial
mollifier p_epsilon, Tonelli writes the left side as an average over W-v.
The same constant therefore works, for every epsilon>0, with the two Green
kernels left unsmoothed. This statement does not cover arbitrary smoothing
of the Green factors.

In fact, replacing both Green factors by positive Gaussian convolutions
while retaining the SAME compactly supported right side cannot hold for all
Z: the left side is positive for |Z|>h, while the stated right side is zero.
A valid Green-smoothed version needs a correspondingly averaged right side,
or an application-specific limit argument. This is not an issue for the
literal unsmoothed d2(WC), where the Green kernel is already a function.

The crossing-diagram temporal factor is still present. Its previous upper
pullout costs(T-b)^(-alpha0). This note neither controls the accumulation
of such costs across diagrams nor shows that merged fractional wave powers
stay inside a closed family of estimates. It supplies no pairing-removal
algorithm, no recovery of the required factorial denominator, no d3 or
anisotropic extension, and no bound on the full moment series.

## Screen disposition

| Check | Disposition |
|---|---|
| Root's D>=4a(1-a) inequality | PASS after a<=b, a+b<1 imply0<=b-a<1-2a. |
| D upper comparison when z-2a changes sign | PASS only with the explicit two-case argument above. |
| Elliptic logarithm and endpoint singularities | Elementary upper bound and integrability supplied. |
| Uniform remote W | Supplied through the proved disk layer-cake comparison. |
| Alpha>3/2, q>=alpha-1 | Unreviewed sufficiency argument closes. |
| Alpha=3/2, q>1/2 | Unreviewed sufficiency via logarithmic loss absorption. |
| Covariance-only positive mass-one smoothing | Follows by uniform-W averaging; Green factors unchanged. |
| Same RHS with Gaussian-smoothed Green kernels | Fails outside compact support; a different formulation is needed. |
| Full Stratonovich upper-bound goal | OPEN; no all-order consumer supplied. |

The scientific next action is an independent source-bound review of this
bounded deterministic candidate, not immediate promotion or an all-order
proof wave built on unchecked geometry.
