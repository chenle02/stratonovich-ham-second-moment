# G2 route reconnaissance and falsification screen

[held back: collaborators' unpublished work]

## Objects and goal boundary

Work first in d=1, with either spatial white noise (alpha=1, gamma=delta_0) or gamma=c_alpha |x|^(-alpha), 0<alpha<1, c_alpha>0. Fix 0<a0=alpha0<1 and beta=4-alpha-a0. Write

- a_k = E X_(2k)(1,x), the **Stratonovich first-moment** coefficient;
- A_k = sum_(m+n=2k) E[X_m(1,x) X_n(1,x)], the full second-moment coefficient;
- D_n = E X_n(1,x)^2.

At a general time the first two coefficients are multiplied by t^(beta*k), and D_n by t^(beta*n). If the noise is multiplied by lambda, X_n is multiplied by lambda^n. The scalar coefficient series are convergent, with nonnegative expectation coefficients. In particular, E u_lambda(t)=sum lambda^(2k) a_k t^(beta*k).

The target factorial denominator is (k!)^(3-alpha). A bound A_k <= C^k/(k!)^(3-alpha) suffices for G:upper. This screen neither establishes that bound nor adjusts the project's target.

## Screen 1 — a uniform stronger bound on every diagram is false

**Candidate being tested.** In white space, uniformly in k, split, and pairing, suppose

    J_(m,n,D)(t) <= C^k t^((3-a0)*k)/(k!)^3,
    m+n=2k.

Summing approximately C^k k! pairings would give the desired denominator (k!)^2. This simple diagram-by-diagram strategy is false for every fixed a0>0.

**Exact witness.** Take the one-chain split (0,2k) and adjacent pairing
D_adj={(1,2),(3,4),...,(2k-1,2k)}. Write its positive time increments as h_1,...,h_(2k). A pair contraction integrates the odd Green factor to mass h_(2j-1), evaluates the even Green factor at spatial zero as 1/2, and contributes temporal factor h_(2j)^(-a0). Thus

    J_adj(t)
      = 2^(-k) integral_(h_i>0, sum h_i<t)
                    product_j h_(2j-1) h_(2j)^(-a0) dh
      = [Gamma(1-a0)/2]^k
        t^((3-a0)*k)/Gamma(1+(3-a0)*k).

The last equality is the Dirichlet simplex integral; it can also be verified inductively by the beta integral. All shape parameters are positive: 2 and 1-a0. At k=1 this is G0's E X2=c0*t^(3-a0)/2. At k=2,a0=0 it is G1's (0,4),A value t^6/2880.

For fixed b=3-a0, log Gamma(1+bk)=b*k*log k+O(k), whereas log(k!)^3=3*k*log k+O(k). Consequently

    log[(k!)^3 J_adj(1)] = a0*k*log k+O(k),

which exceeds k*log C for every fixed C eventually.

**Verdict: FALSIFIED, narrowly.** This kills the displayed uniform bound on each diagram. It does not kill a grouped pairing estimate: there is only one completely adjacent matching on this fixed chain. Its own denominator is (k!)^(3-a0), which is stronger than the desired denominator (k!)^2 because a0<1. Exceptional large diagrams may be harmless after their multiplicity is retained. It does not prove that every use of Chen's Theorem 3.1 fails.

## Screen 2 — Gaussian mean-square amplification is not a universal identity or bound

**Candidate being tested.** With unit prefactor and every t>0,

    E u(t,x)^2 <= [E u_(sqrt(2))(t,x)]^2.

This is tempting because a positive mixture of exponentials of linear Gaussian functionals would satisfy it: E exp(<W,h+k>) <= [E exp(sqrt(2)<W,h>)][E exp(sqrt(2)<W,k>)] by ||h+k||²/2 <= ||h||²+||k||². A wave solution must not be assumed to admit such a positive mixture.

**First-order necessary condition.** Write b_1=E X1(1)^2 and a_1=E X2(1). Then the two sides have coefficients b_1+2a_1 and 4a_1 at t^beta. Thus b_1<=2a_1 is necessary. A coefficient violation implies a violation for sufficiently small t, not merely a formal objection: positivity and convergence at a fixed time bound the remaining terms by O(t^(2beta)) near zero.

**White test.** G0 gives b_1=2a_1, so equality holds at this order for every a0. At a0=0, G1 gives a_1=1/12 and a_2=11/17280. The order-four coefficient of the proposed right side is

    8a_2+4a_1² = 71/2160,

whereas A_2=11/540=44/2160. The difference is 1/80>0. Thus the first two static white orders do not falsify the candidate restricted to white noise. They do not prove it.

**Rigorous Riesz countertest.** Choose alpha=a0=1/2 and c_alpha=1, an interior admissible parameter point. G1 gives a_1=1/3. For independent U uniform[-s,s] and V uniform[-r,r], 0<r<=s,

    E|U-V| = s/2+r²/(6s) <= 2s/3.

Convexity of z^(-alpha) on z>0 gives

    integral G(s,x)G(r,y)|x-y|^(-alpha) dxdy
      = sr E|U-V|^(-alpha)
      >= (3/2)^alpha s^(1-alpha) r.

Hence

    b_1 >= 2(3/2)^alpha /
           [(1-a0)(2-a0)(4-alpha-a0)]
         = (8/9)sqrt(3/2) > 2/3 = 2a_1.

No floating quadrature is required for this strict countertest. The G1 floating value b_1 approximately1.713864 is consistent but is not its proof.

**Verdict: FALSIFIED for the universal all-time, unit-prefactor inequality.** The result also rules out the specified positive Gaussian-exponential mixture mechanism in this Riesz case. It does **not** refute a white-space-only statement, an eventual large-time comparison, a comparison with a constant prefactor K>1, or the conjectured asymptotic constant. An added prefactor removes the low-time coefficient test. Those variants require separate arguments.

## Screen 3 — integrated Stratonovich mean comparisons survive the available tests

### 3a. Full coefficient compression

**Precise candidate.** For the fixed covariance and fixed a0, find C<infinity such that

    A_k <= C^k a_k for all k>=1.                         (MC)

This uses all self-pairings in both coefficients. If proved, (MC) gives the exact all-time comparison

    E u(t,x)^2 <= E u_(sqrt(C))(t,x).

Chen's author-version first-moment upper bound would then imply G:upper, using noise-strength scaling lambda^(2/(3-alpha)) of the first-moment exponential constant. The particular choice C=2^(4-alpha) would give the conjectured sharp **upper** constant, but is much stronger than needed for G:upper and is not established here.

**Tests.** White noise has A_1/a_1=4 for every a0. At the static endpoint, G1 gives A_2/a_2=32, so a uniform C must be at least sqrt(32); C=4 fails at order four. The sharp candidate C=8 in white space passes these two tests (4<=8,32<=64). At alpha=a0=1/2,c_alpha=1, G1 gives A_1/a_1=3b_1+2 approximately7.141593, so C must exceed that value; the proposed sharp value 2^(7/2) approximately11.313708 is not falsified by this one coefficient. The numerical ratios are diagnostic only; the exact necessary constraint is C>=3b_1+2 with b_1 given by the proved G1 one-dimensional integral.

**Additional boundary kill test (root-proposed, independently checked).** Fix any 0<alpha<1 and c_alpha>0, and let a0↑1 through the admissible range. The G1 one-dimensional formula has the form b_1=c_alpha/[(1-alpha)(2-alpha)] times integral_0^1 v^(-a0) H_alpha(v) dv, with H_alpha continuous at zero and H_alpha(0)=2^(2-alpha)/(3-alpha). The elementary approximate-identity identity epsilon*integral_0^1 v^(-1+epsilon)H(v)dv→H(0) therefore gives

    (1-a0)b_1 → c_alpha*2^(2-alpha)/
                         [(1-alpha)(2-alpha)(3-alpha)],
    a_1 → c_alpha/[(1-alpha)^2(2-alpha)(3-alpha)],
    (1-a0) A_1/a_1 → 2^(2-alpha)(1-alpha)>0.

Thus A_1/a_1 diverges. In particular the parameter-uniform coefficient candidate C=2^(4-alpha) is **false** for all a0 sufficiently close to one at this fixed alpha. No numerical threshold is asserted. This does not refute (MC) with C depending on alpha and a0; indeed the necessary C then diverges as the boundary is approached. It does not refute an eventual large-time bound with a prefactor, an eventual large-k coefficient comparison with a parameter-dependent prefactor or cutoff, or the conjectured asymptotic constant. The sharp constant must not be demanded of every low-order coefficient without such qualifications.

**Surviving obligation.** Prove an integrated comparison of the full two-chain Wick sum to the single-chain Wick sum with an exponential cost in k, retaining covariance normalization and finite horizons. Merely naming (MC) is not progress: first-moment coefficient asymptotics make it close to a reformulation of the target factorial question. A concrete rearrangement or coupling of the integrated diagrams is still missing.

### 3b. Diagonal trace/mean comparison

A potentially narrower sufficient statement is

    D_n <= C^n a_n for all n>=1.                        (DT)

Here D_n is a two-chain length-(n,n) moment and a_n is a single-chain length-2n expectation. In d=1, the source's first-moment coefficient upper bounds have denominator (n!)^q, q=3-alpha>=2. If (DT) holds, summing the square roots by Minkowski gives a scalar series with denominator (n!)^(q/2) and argument proportional to t^(beta/2), hence the same scale t^(beta/q)=t^kappa. No sharp constant for this norm-summation route is claimed here.

The static white tests give D_1/a_1=2 and D_2/a_2=17. Thus C=2, or any proposed trace inequality with that fixed cost, is false already at n=2; C>=sqrt(17) is necessary. A sufficiently large unspecified C remains possible.

**Import requirement for either route.** Use the author-version first-moment upper bound (Theorem1.2) and its amplitude scaling, or its coefficient estimate in Section8, with an exact pinpoint checked before proof investment. The existence of a positive coefficient series alone is insufficient to supply its factorial rate. Neither route uses the Skorohod mean, which is one and has no counterpart of these nonzero a_k.

### Pointwise concatenation is not the missing mechanism

For Riesz covariance, already two one-vertex chains can have |x|<s, |y|<r but |y-x|>r-s when s<r. Their product Green kernel is positive while the chronologically concatenated single-chain kernel is zero. A constant multiplier cannot repair this support defect.

It persists even in white space with domestic pairs. In the (2,2),A diagram take the first chain's times (1/4,3/4), positions (x,x) with x=1/5; the second chain's times (1/2,7/8), positions (y,y) with y=-2/5; t=1. All four original Green factors are positive. In chronological order the first jump from x at1/4 to y at1/2 has distance3/5>1/4, so the corresponding single-chain factor vanishes. The inequalities remain strict in open neighborhoods of the free spatial positions and times: this is a positive-measure obstruction in the contracted integral, not a boundary example.

**Verdict:** (MC)/(DT) SURVIVE the finite tests with an unspecified exponential cost; the naive pointwise concatenation mechanism is FALSIFIED. Only an integrated/grouped argument remains eligible. A white-only mean-square amplification route also survives, with no current mechanism.

## Screen 4 — dropping the spatial geometry before temporal symmetrization is too weak

In white space, after any k delta contractions all free vertex positions lie in [-t,t]. Bounding all 2k wave indicators by one leaves the spatial factor at most t^k/2^k. After this replacement the sum of temporal pairing factors is symmetric in all 2k time labels. Its integral over a split (m,n) simplex is exactly1/(m!n!) times its integral over the full cube. Therefore the resulting bound on the full coefficient is

    sum_(m+n=2k) sum_D J_(m,n,D)(t)
      <= [2/((1-a0)(2-a0))]^k t^((3-a0)*k)/k!.

Indeed, sum_(m+n=2k)1/(m!n!)=2^(2k)/(2k)!, the pairing count is (2k)!/(2^k k!), and each disjoint temporal pair integrates to 2t^(2-a0)/((1-a0)(2-a0)). The bound yields exponent3-a0, worse than both the G0 bound and the target.

**Verdict: quantitatively inadequate for G:upper.** Symmetrizing the temporal factors after erasing the spatial chain constraints loses too much. This is not a lower bound on the moment and does not rule out a symmetrization retaining its spatial dependence.

## Temporal-order retention: exact obstruction and scope hold

A natural attempt is to retain a penalty depending on the number of time ranks spanned by each pair, rather than replacing every temporal gap by a local increment. The adjacent-diagram test shows why a uniform improvement cannot hold: short pairs must be allowed their larger contributions. A weighted sum over rare short-pair configurations might still recover the missing factorial power.

**Block labels are not chronological ranks.** Consider the pure-cross identity matching j<->k+j on two length-k white-space chains. Its spatial contraction is

    2^(-k) product_(j=1)^k min(h_j,g_j),

where h_j,g_j are the two chains' increments, and its temporal weight is product_j |s_j-r_j|^(-a0). Restrict both s_j,r_j to ((j-1/4)/k,j/k). The domain has volume(4k)^(-2k), every increment is at least3/(4k), and every paired time difference is at most1/(4k). Thus the diagram is at least

    [3*4^a0/128]^k k^(-(3-a0)*k).

Every pair has block-label distance k, so a proposed span penalty based on |j-(k+j)| would assign no short-pair penalty and would wrongly demand a denominator(k!)³. On these configurations the paired vertices are adjacent in the actual chronological order. Consequently any useful temporal-span statement must condition on an actual time shuffle, not the block labeling of the two chains.

[held back: collaborators' unpublished work]

## Proposed next bounded action, with no promotion

[held back: collaborators' unpublished work]

No claim here has received the required non-GPT scientific review. The only inherited accepted results are the cited G0/G1 finite coefficients and source inputs. STATUS: DONE_WITH_CONCERNS (bounded reconnaissance complete; surviving obligations unproved).
