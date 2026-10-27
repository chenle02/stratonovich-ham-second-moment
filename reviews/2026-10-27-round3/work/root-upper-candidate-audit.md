# Independent GPT audit of the root's d=1 upper-bound candidate

**Disposition: SURVIVES the independent audit below.** No defect was found in the closing-variable argument, regularization, weighted maximum, temporal symmetrization, or constants. If the reviewed G0 mixed expansion is taken as an input, this is a genuine candidate proof of G:upper in d=1 for Riesz/white spatial covariance. It is **not yet cross-family accepted**, not a proof for d=2 or3, and not a sharp-constant result. The root authored the mechanism; this worker checked it independently and tried to break its dependencies before writing this record.

## 1. Exact scope and notation

Fix d=1, 0<a0=alpha0<1. The covariance is either gamma(x)=c|x|^(-alpha), 0<alpha<1, c>0, or gamma=c delta_0, alpha=1, c>0. The physical Green density is G_h(y)=1/2 times1{|y|<h}. No Fourier normalization is introduced.

For m+n=2k, use the two rooted increasing chains of the reviewed G0 formula, labelled in block order1,...,m and m+1,...,2k. The predecessor is the previous label in the same chain; both chains have root(0,0). Put h_l=s_l-s_pred(l)>0 and y_l=x_l-x_pred(l). The spatial change of variables has determinant one. Its inverse is a prefix sum in each chain, so x_i depends only on increments with labels at most i.

The exact integrand for a fixed pairing D is the spatial factor

    S_D(h)=integral_(R^(2k)) product_l G_(h_l)(y_l)
                         product_((i,j) in D) gamma(x_j-x_i) dy,

times the temporal factor product_((i,j) in D)|s_j-s_i|^(-a0). The original terminal-wave convention has already been converted to this rooted convention in G0; there is no missing final Green factor. In particular,

    sum_l h_l = last_time(chain1)+last_time(chain2) <= 2t.

An empty chain contributes zero to this sum. The bound2t is harmlessly loose for an empty chain.

## 2. Descending closing-variable argument: valid

Orient each pair(i,j) with i<j. Call i its opening label and j its closing label. Each of the2k labels occurs exactly once, so there are k distinct opening and k distinct closing labels.

Integrate the closing increments y_j in decreasing order of the closing label j. At the step for(i,j):

1. x_j=y_j plus a sum of earlier increments in its chain; x_i is independent of y_j because i<j. Thus x_j-x_i=y_j+z with z independent of y_j.
2. Every other remaining pair(i',j') has closing label j'<j. Both endpoints of that pair are at most j', so both spatial positions depend only on increments with labels<j. Its covariance factor is independent of y_j.
3. Pairs with larger closing labels have already been removed. Their upper bounds depend only on their h-values, not on any spatial increment, so they cannot reintroduce y_j.
4. All Green factors are separate functions of their own increments. Therefore the only remaining factors involving y_j are G_(h_j)(y_j) and gamma(y_j+z).

This discharges the critical dependency issue. It works for domestic and cross pairings without assuming their spatial paths are chronological across the two chains. Positivity permits Tonelli and replacement by a supremum at each step.

After all closing variables are integrated, all remaining opening variables carry only their Green factors, whose masses are h_i. No opening/closing multiplicity or factorial is introduced in this operation.

Finite verification, separate from the general argument: exact prefix-support bookkeeping was enumerated for k=1,2,3,4 and every split and pairing. Counts were3,15,105,945 split/pairing cases. At each descending pivot its own covariance had coefficient+1 on y_j and every other remaining covariance had coefficient0. All checks passed. This enumeration is not the proof for arbitrary k; the topological-prefix argument above is.

## 3. Spatial bounds and uniform smoothing

For Riesz covariance,

    sup_z integral G_h(y)c|y+z|^(-alpha)dy
       = c h^(1-alpha)/(1-alpha).

The integral of an even decreasing function over an interval of fixed length is maximal when centered at zero. Direct integration at z=0 gives the displayed value, including the1/2 in G. If the covariance is spatially smoothed by any nonnegative mass-one Gaussian density p_epsilon, its interval integral is the average of unsmoothed interval integrals over shifts and is bounded by the same supremum. Hence the bound is uniform in the noise smoothing.

For white covariance, work with c p_epsilon before passing to the delta limit:

    sup_z integral G_h(y)c p_epsilon(y+z)dy <= c/2.

This uses G_h<=1/2 and integral p_epsilon=1. It does not evaluate a delta at a point and is uniform in epsilon. Pair-dependent smoothing variances epsilon_i+epsilon_j make no difference to this bound.

Consequently, with O and C the opening and closing label sets,

    S_D(h) <= [c/(1-alpha)]^k
                 product_(i in O)h_i product_(j in C)h_j^(1-alpha)

in the Riesz case. In white space the corresponding bound is

    S_D(h) <= (c/2)^k product_(i in O)h_i.

For the white case these inequalities can first be applied to the smoothed mixed moments. For either case, temporal truncations are bounded above by |s-r|^(-a0), a nonnegative function. Thus the same full temporal kernel can be used in every pair before invoking its permutation symmetry. The source/G0 fixed-order L2 limits give convergence of products in L1, so the resulting uniform bounds pass to mixed moments. There is no d=3 Green regularization in this d=1 proof.

## 4. Weighted maximum and constants: checked

Set b=2-alpha. In the Riesz case the2k exponents of h are1 at openings and1-alpha at closings, with total bk. Weighted AM–GM gives

    product_open h_i product_close h_j^(1-alpha)
      <= (2t/(bk))^(bk) (1-alpha)^((1-alpha)k).

Multiplication by[c/(1-alpha)]^k gives

    S_D(h) <= K_sp^k t^(bk)/k^(bk),
    K_sp = c*2^(2-alpha)*(1-alpha)^(-alpha)/(2-alpha)^(2-alpha).

This is uniform in D and the split. The chain constraints may make the maximizing h-vector unattainable for a particular split; enlarging to sum h<=2t only increases the maximum, so this does not invalidate the bound.

In white space alpha=1, use ordinary AM–GM on the k opening increments:

    (c/2)^k product_open h_i <= (c/2)^k(2t/k)^k
                            = c^k t^k/k^k.

Thus K_sp=c and b=1. The zero exponents on closing increments are handled directly, not by an undefined0^0 manipulation. The k=0 contribution is separately1.

A useful normalization check: with c_alpha=(1-alpha)/2, the Riesz K_sp tends to1 as alpha↑1, agreeing with unit white covariance. This checks the spatial factor without asserting any uniform large-time limit in alpha.

## 5. Temporal symmetrization and full count: checked

The preceding spatial maximum is a CONSTANT over the whole ordered time domain; this is the crucial difference from the failed conditional-density comparison. Only now define

    F(s_1,...,s_(2k)) = sum_(D in Pi_k)
                         product_((i,j) in D)|s_i-s_j|^(-a0).

F is invariant under every permutation of its2k labels, because each permutation bijects Pi_k. It is integrable on[0,t]^(2k): each pairing consists of k disjoint temporal pairs, and

    integral_[0,t]^2 |s-r|^(-a0) dsdr
       = Z t^(2-a0),   Z=2/[(1-a0)(2-a0)].

For a fixed split(m,n), permutation invariance within each block gives exactly

    integral_(Delta_m(t) x Delta_n(t)) F
       = 1/(m!n!) integral_[0,t]^(2k) F.

This equality is used only AFTER summing all pairings and replacing their spatial parts by the same bound. It is not asserted for a fixed pairing or for a spatially weighted pairing sum.

The three scalar counts are

    sum_(m+n=2k)1/(m!n!) = 2^(2k)/(2k)!,
    |Pi_k| = (2k)!/(2^k k!),
    integral_cube F = |Pi_k| [Z t^(2-a0)]^k.

Combining them with the spatial maximum yields the candidate full coefficient bound

    A_k(t)
      <= (2 Z K_sp)^k t^((4-alpha-a0)k)
                            / [k! k^((2-alpha)k)].          (U1)

Since k!<=k^k and2-alpha>0,

    k! k^((2-alpha)k) >= (k!)^(3-alpha).

The direction is correct, so(U1) implies

    A_k(t) <= (2 Z K_sp)^k t^(beta k)/(k!)^q,
    beta=4-alpha-a0, q=3-alpha.                           (U2)

No pair count, split count or covariance normalization is missing.

## 6. Scalar series and actual conclusion

The reviewed G0 expansion is E u(t,x)^2=sum_(k>=0)A_k(t). For z>=0 and q>=1,

    sum_(k>=0) z^k/(k!)^q
      = sum_(k>=0)[z^(k/q)/k!]^q
      <= [sum_(k>=0)z^(k/q)/k!]^q
      = exp(q z^(1/q)).

Here q>=2. Substituting z=2ZK_sp*t^beta in(U2) gives the candidate bound

    E u(t,x)^2 <= exp{ q(2 Z K_sp)^(1/q) t^(beta/q) },
    beta/q=(4-alpha-a0)/(3-alpha)=kappa.

Thus this is a direct upper-bound proof candidate in the stated d=1 class; it does not merely assume a mean comparison. It does not need the source's first-moment theorem or any unproved coefficient comparison. Its constant is explicit but no sharpness is claimed.

## 7. Checks against established controls and earlier no-gos

- White order two: the exact A1(t) is2t^(3-a0)/[(1-a0)(2-a0)(3-a0)]. The candidate coefficient is2Zc; for unit white noise the ratio of candidate bound to exact coefficient is2(3-a0)>4. Exact rational checks at a0=0,1/4,1/2,3/4,9/10 give ratios6,11/2,5,9/2,21/5.
- Static white order four: exact A2=11/540; (U1) gives1/2, and the relaxed factorial(U2) gives1. Both are safely above the exact coefficient.
- The adjacent-diagram obstruction is not contradicted. The new proof never claims a (k!)^(-3) bound on each white diagram. It combines a common SPATIAL maximum with a symmetrized SUM of temporal pairing factors; it is this ordered sum that supplies the needed factorial count.
- The failed time-slice density comparison is not used. The proof does not compare H_c(s) with a one-chain density at the same times. It removes the spatial dependence by an upper bound retaining k^(-(2-alpha)k), rather than by the earlier volume bound t^k/2^k that lost this essential power of k.
- All self-pairings remain present. No Skorohod development is made here.
- As a0↓0 the time exponent has the correct static limit. The proof does not establish uniformity of any sharp asymptotic constant or exchange that limit with t→infinity.
- The conclusion is an upper bound at the same scale as the existing Jensen lower bound, not a sharp constant or improved lower bound.

## 8. Review priorities and limits

A cross-family reviewer should particularly check:

1. the descending closing-label dependency claim across the two block-indexed chains;
2. uniformity of the Riesz/white convolution bound under pair-dependent Gaussian smoothing;
3. the timing of symmetrization—only after a common spatial maximum is extracted and all pairings are summed;
4. the all-split factorial and final series constants;
5. that only d=1 Riesz/white covariance is claimed.

The audit found no blocking gap. The finite checks support the bookkeeping but do not replace the general proof. No imported Balan trace inequality, Chen–Hu lower-bound lemma, false source(5.4) uniformity, or shared pure-cross estimate is used.

**STATUS: DONE_WITH_CONCERNS — genuine d=1 G:upper candidate validated by same-family independent audit; mandatory Opus review still pending.**
