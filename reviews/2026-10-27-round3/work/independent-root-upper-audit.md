# Independent audit of the root's d=1 target-scale upper-bound candidate

Status: **same-family independent audit; no defect found in the stated d=1
argument**. This is not the required cross-family acceptance. No manuscript,
Lean package, sibling source or git history was changed. The argument below
is written to expose every consumer and constant for the Opus review.

## Scope checked

- d=1, 0<alpha0<1.
- Either gamma(x)=c|x|^(-alpha), c>0 and 0<alpha<1, or gamma=c delta_0,
  c>0 and alpha=1. A zero covariance is trivial separately.
- The two chains have arbitrary lengths m,n>=0 with m+n=2k; k>=1 in the
  estimates. The total-order-zero term is treated separately as one.
- Roots are zero separately in each chain. Global block labels are used only
  for triangular spatial dependence, never as chronological temporal ranks.
- The reviewed G0 mixed-moment formula is the consumer identifying the sum
  of these nonnegative integrals with E u(t,x)^2.

## 1. Descending spatial integration is valid

For fixed positive chain increments h_l, change spatial variables from
vertices x_l to increments y_l, separately in each chain. The map has
absolute determinant one and

    x_l = sum_(i from the beginning of l's chain through l) y_i.

Thus x_l depends only on increments with global index <=l, even across the
block-label reset. All Green factors become the independent-coordinate
factors G_(h_l)(y_l).

For each pair (i,j), orient it by i<j. Call i an opening and j a closing.
There are exactly k of each. The following induction invariant makes the
argument precise: after eliminating labels N,N-1,...,j+1, the remaining
covariance factors are exactly those whose larger endpoint is <=j.
The bounds already extracted depend on the time increments only.

- If j is a closing, there is exactly one remaining covariance containing
  x_j. Its other endpoint i<j has no dependence on y_j. The factor therefore
  has form gamma(y_j+z), up to an irrelevant sign, where z is independent of
  y_j. Every other remaining pair has both endpoints <j and hence is also
  independent of y_j. The uniform convolution bound below applies.
- If j is an opening, its partner has index >j, so that covariance was
  already removed. No remaining covariance depends on y_j, and integrating
  G_(h_j) gives its mass h_j.

One can equivalently integrate just the closing indices in descending order,
then the opening variables. A higher opening carries no surviving covariance
after its partner is removed. Descending all indices is an expositional
choice, not a correction to the root's closing-first argument.

There is no obstruction from crossing or nested pairings. At total order
four the closing sets are {2,4} for (12)(34), and {3,4} for both (13)(24)
and (14)(23); the invariant applies in all three cases and for every split.
Empty-chain splits simply give one triangular block.

## 2. Uniform convolution bounds, including mollification

For G_h(y)=(1/2)1_{|y|<h} and 0<alpha<1,

    sup_z integral G_h(y)c|y+z|^(-alpha) dy
      = c h^(1-alpha)/(1-alpha).                         (A1)

The maximum is at z=0 because an interval of fixed length maximizes the
integral of an even decreasing nonnegative function when centered at zero.
This follows directly by layer cake and interval intersection lengths.
The displayed value is the elementary integral at zero.

If gamma_epsilon is a convolution of gamma with a probability Gaussian,
Tonelli expresses the left side with gamma_epsilon as an average of the
same shifted convolutions. Hence (A1) is uniform in every smoothing
parameter, including different parameters for different pairs.

For gamma=c delta_0, use the regularized covariance c p_epsilon. Since
G_h<=1/2 and p_epsilon has mass one,

    integral G_h(y)c p_epsilon(y+z) dy <= c/2,           (A2)

uniformly in z,h>0 and epsilon. This justifies the white-noise estimate
without assigning a pointwise value to delta. Passing the integrated bound
through the G0 defining limits is legitimate. Temporal truncations, if kept
at this stage, are bounded above by the full |s-r|^(-alpha0) kernel before
symmetrization.

Consequently the fixed-time spatial integral S_D satisfies

    S_D(h) <= [c/(1-alpha)]^k
              product_open h_l product_close h_l^(1-alpha)   (Riesz),

and

    S_D(h) <= (c/2)^k product_open h_l                        (white).

This estimate is independent of the detailed pairing after the next step.

## 3. Common spatial bound and constants

In either two-chain domain, sum_l h_l <2t. Put w=2-alpha.
For Riesz, weighted AM–GM with k weights1 and k weights1-alpha gives

    product_open h_l product_close h_l^(1-alpha)
      <= (1-alpha)^((1-alpha)k)
         [2t/(k(2-alpha))]^((2-alpha)k).

Thus

    S_D <= Ksp^k t^((2-alpha)k) k^(-(2-alpha)k),          (A3)
    Ksp = c 2^(2-alpha) (1-alpha)^(-alpha)
                /(2-alpha)^(2-alpha).

All AM–GM weights here are strictly positive. At white alpha=1 the closing
weights vanish and must be handled separately: sum_open h_l<=2t, so
product_open h_l<=(2t/k)^k. Combining with (c/2)^k gives the same form A3
with alpha=1 and **Ksp=c**.

The crucial domain restriction is alpha<=1. This common bound is not justified
by the same AM–GM argument when 1-alpha<0. In particular it is not a d=2/3
proof merely by replacing the convolution constant. The d=1 result should
not be promoted to all dimensions without a separate argument.

## 4. Temporal symmetrization must follow the common bound

Let

    F_k(s_1,...,s_(2k))
      = sum_(D in Pi_k) product_((i,j) in D)|s_i-s_j|^(-alpha0).

This full sum is invariant under every permutation of the labels. A fixed
pairing summand is not. The spatial majorant A3 is already independent of
D and all time coordinates, so the symmetry may now be used.

For any split m+n=2k, permutations within the first and second blocks
partition the full cube into m!n! ordered sectors, up to null diagonals.
Therefore

    integral_(ordered m-chain x ordered n-chain) F_k
      = [1/(m!n!)] integral_[0,t]^(2k) F_k.             (A4)

The integrand is integrable: each pairing has disjoint label pairs and
0<alpha0<1. Specifically, with

    Z = 2/[(1-alpha0)(2-alpha0)],

    integral_[0,t]^(2k) F_k
      = P_k [Z t^(2-alpha0)]^k,
    P_k = (2k)!/(2^k k!).                               (A5)

No extra shuffle factor is needed. Summing the split factors gives

    sum_(m=0)^(2k) 1/[m!(2k-m)!] = 2^(2k)/(2k)!.

Combining A3–A5 yields the full total-order-2k coefficient bound

    A_k(t)
      <= (2 Z Ksp)^k t^((4-alpha-alpha0)k)
            /[k! k^((2-alpha)k)]
      <= (2 Z Ksp)^k t^((4-alpha-alpha0)k)
            /(k!)^(3-alpha).                           (A6)

The last step uses k!<=k^k and 2-alpha>0; its inequality direction is correct.
All constants depend only on the fixed covariance and alpha0, not on k,m,n,t.

If the noise is regularized with vertex-dependent temporal cutoffs, first
replace each truncated temporal covariance by the common full kernel. One
must not claim that the differently truncated finite Wick sum is symmetric
without this replacement. This is harmless for the upper bound because all
factors are nonnegative.

## 5. Series conversion and actual target

Set beta=4-alpha-alpha0 and q=3-alpha>=2. A6, the nonnegative mixed expansion
and the separately included k=0 term give

    E u(t,x)^2 <= sum_(k>=0) [(2 Z Ksp)t^beta]^k/(k!)^q
      <= exp{q (2 Z Ksp)^(1/q) t^(beta/q)}.              (A7)

The last inequality follows from sum a_k^q <= (sum a_k)^q for nonnegative
sequences and q>=1, taking a_k=z^(k/q)/k!. It can be obtained first for finite
sums and then by monotone convergence. Thus the proposed explicit upper
constant is

    C_upper = (3-alpha)(2 Z Ksp)^(1/(3-alpha)).

Since beta/q=kappa, A7 is the requested target-scale upper bound in the
stated d=1 covariance classes. It is not a sharp-constant theorem, and neither
Gaussian positivity of u nor almost-sure monotonicity of u is needed.
Only the expectation coefficients and the underlying kernels are nonnegative.

## Checks against the retained small cases and no-gos

1. White alpha0=1/2 has Ksp=c and 2ZKsp=16c/3. At k=1 the exact coefficient
   for c=1 is16/15, below16/3. At static alpha0=0,k=2 the sharper first line
   of A6 gives1/2, above the exact11/540. No normalization contradiction.
2. The one-chain adjacent-pair diagram has denominator approximately
   (k!)^(3-alpha0) in white space. That is compatible with A6's denominator
   (k!)² because 3-alpha0>2. This proof never claims the false stronger
   diagram-wise denominator(k!)³ from the prior screen.
3. The decisive new gain is A4 applied to the **complete temporal Wick sum**
   after retaining the spatial factor k^(-(2-alpha)k). The previously failed
   cube symmetrization discarded that spatial factor. The two operations
   are therefore quantitatively different.
4. The spatial elimination uses block labels for triangular dependence only;
   it makes no temporal-span claim from their numerical distances. The prior
   block-label-versus-chronological-rank obstruction does not apply.
5. With normalized Riesz c=(1-alpha)/2, Ksp tends to1 as alpha tends to1,
   matching unit white noise. With unnormalized fixed c it diverges, as
   expected. This is a constant normalization check, not an endpoint theorem.
6. At alpha0 down to zero, beta/q tends to(4-alpha)/(3-alpha), as required.
   The constant is coarse and does not adopt the disputed printed Chen–Hu
   white constant. The bound is consistent with the Jensen lower bound.

## Required presentation conditions before promotion

- State d=1 and the precise Riesz/white covariance classes.
- Define the restarted spatial increments explicitly for both blocks.
- Include the induction invariant for removal of covariance factors.
- Treat white alpha=1 and zero order separately rather than using zero
  AM–GM weights or expressions divided by k without explanation.
- Use the full temporal kernel before symmetry when regularizations differ.
- Apply symmetry to the full pairing sum only, never to individual terms.
- Label C_upper as an upper-bound constant, not the conjectured sharp value.
- Obtain the required Opus review. This independent GPT audit alone is not
  scientific acceptance, and no Lean certificate was produced here.

STATUS: DONE_WITH_CONCERNS — no mathematical defect found within the stated
d=1 scope; precise cross-family verification and source/literature disposition
remain the parent's gates.
