# G1 derivation (candidate, before independent review)

Todo: [x] derive white order-four spatial reductions; [x] derive Riesz order-two formulas; [ ] exact static controls by independent spatial-sector method; [ ] manuscript/proofs; [ ] clean build; [ ] independent review (root).

Write a=alpha0, beta=4-alpha-a. For white space alpha=1. Let F(A,B,C)=4AB-(A+B-C)_+²+(|A-B|-C)_+², the area of |x|<A, |y|<B, |x-y|<C. It is symmetric in its three arguments by determinant-one linear changes of variables.

All white order-four spatial factors below include the 1/16 from four wave kernels. Each must be multiplied by the listed two temporal covariance factors and integrated over the appropriate ordered time domain.

## Split (0,4)

Times a,b,c,d now denote positive increments (use different letters in final notes): sum<t. Pairings A=(12)(34), B=(13)(24), C=(14)(23).

| Pairing | Spatial factor | Temporal pair gaps |
|---|---|---|
| A | a*c/4 | b,d |
| B | a*min(b,c,d)/4 | b+c,c+d |
| C | a*min(b,d)/4 | b+c+d,c |

Static unit-time coefficients: 1/2880,1/8640,1/5760; sum 11/17280.

## Split (1,3)

Single time r in (0,t), other chain increments a,b,c with a+b+c<t. Pairing indexed by j=1,2,3, the vertex in the long chain paired to the single vertex.

| j | Spatial factor | Temporal pair gaps |
|---|---|---|
| 1 | min(r,a)*b/4 | abs(r-a),c |
| 2 | F(r,a,min(b,c))/16 | abs(r-a-b),b+c |
| 3 | F(r,a,c)/16 | abs(r-a-b-c),b |

## Split (2,2)

First chain increments a,b, second c,d, with a+b<t and c+d<t. Pairings use global labels (12)(34),(13)(24),(14)(23).

| Pairing | Spatial factor | Temporal pair gaps |
|---|---|---|
| A | a*c/4 | b,d |
| B | min(a,c)*min(b,d)/4 | abs(a-c),abs(a+b-c-d) |
| C | F(a,c,min(b,d))/16 | abs(a-c-d),abs(a+b-c) |

Splits (3,1),(4,0) are chain exchanges. All terms scale t^(6-2alpha0), so total order four scales t^(2beta).

## Riesz order two in d=1

Fix gamma(x)=c_alpha |x|^-alpha, 0<alpha<1, c_alpha>0. Set p=2-alpha. The spatial convolution in the (1,1) term is
c_alpha[(s+r)^p-|s-r|^p]/[2(1-alpha)(2-alpha)]. Thus

I11(t)=c_alpha/[(1-alpha)(2-alpha)] times integral_0^t v^-alpha0 {[(2t-v)^(3-alpha)-v^(3-alpha)]/[2(3-alpha)] -(t-v)v^(2-alpha)} dv.

I02(t)=c_alpha*t^beta/[(1-alpha)(2-alpha-alpha0)(3-alpha-alpha0)(4-alpha-alpha0)].

At alpha0=0 the total degree-two coefficient is c_alpha*2^(3-alpha)/[(1-alpha)(2-alpha)(3-alpha)(4-alpha)]. Taking c_alpha=(1-alpha)/2 and alpha→1 recovers white static 1/3. This is a normalized distributional limit, not identifying unnormalized |x|^-alpha with delta.

Riesz order four will be given as explicit unit-cube increments with all three pairings and all split domains; this is a finite coefficient representation, not an asymptotic solution. Static coefficients and exponent limits cannot determine the missing all-order factorial power.

## Completion note

All worker todo items are complete; the independent review remains pending. The finalized formulas, static rational table, normalization checks and exact/floating evidence distinctions are in `worker-report.md` and the notes. This preliminary derivation is retained to show the order of work; it is not the review authority.
