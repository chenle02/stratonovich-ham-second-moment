# Static endpoint and coefficient-interpolation source audit

Date:2026-10-28 UTC. Status: **DONE_WITH_CONCERNS**.
Decision: **PROCEED to a bounded complete candidate proof for isotropic Riesz
covariance in d=2,3,1<alpha<2-alpha0** using the two-input interpolation below.
This is a source/application gate, not acceptance of that prospective theorem.
Novelty remains UNVERIFIED; general anisotropic covariances and sharp constants
are outside this gate. No manuscript/sibling/source edits or git action occurred.

The original one-input power/Jensen proposal gives only alpha+2alpha0<2.
The root's sharper two-input proposal has compatible static and degree-one
fractional-time endpoints throughout alpha+alpha0<2. No source obstruction was
found to its *bounded* proof investment. All deductions identified below still
need to appear in the written candidate and receive cross-family review.

## 1. Exact source and rendered coverage

Chen–Hu, *Stratonovich hyperbolic Anderson equations*, Ann. Probab.53(6),
2144–2195(2025), DOI10.1214/24-AOP1758, published52-page PDF:
`../SPDEForge/sources/chen_hu-25-hyperbolic/published-24-AOP1758.pdf`.
SHA256:
`58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22`.

Actually rendered and viewed: journal pp2145,2146,2147,2149,2150,2151,2152,
2153,2165,2173,2179,2180 (PDF pages2,3,4,6,7,8,9,10,22,30,36,37).
Images retained in `source-pages/`; hashes in `source-evidence.json`.
Extracted text was used for navigation and adjoining selected proof context.
This is not a full audit of the source's Brownian/LDP arguments.

The current project's notes and previous Round3/Round4 implication crosswalks
were read. The prior pinned time-dependent author source remains
`sources/chen-2026-author/aap-chen-2025.pdf`, SHA256
`5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.
Its relevant fixed-order and d3 conventions were rendered in the preceding
`../2026-10-28-round4-cold/source-followup.md`; this audit does not expand
any earlier reviewer's reading coverage.

## 2. Source/application matrix

| Input | Printed hypotheses and conclusion | Application |
|---|---|---|
| Model(1.1)–(1.3),p2145 | Wave operator Delta, static centered Gaussian potential of covariance gamma; nonnegative gamma,d=1,2,3; Stratonovich interpretation | Same spatial normalization as project. Noise amplitude belongs to gamma; no H(2H-1) temporal normalization or Wick replacement. |
| Theorem1.1,p2146 | Data(1,0),d=1,2,3,Dalang integral finite | For gamma=c|x|^(-beta),0<beta<min(2,d),the source's homogeneity calculation supplies the criterion. |
| Theorem1.2(1.9),p2147 | Homogeneous covariance degree beta,0<beta<min(2,d),data(1,0); finite p-moment large-time scale(4-beta)/(3-beta),all positive integer p | p2 provides finite static growth upper bound. No disputed spatial-white sharp constant or claimed exact value is needed. |
| (2.7)–(2.8),p2149 | p_epsilon Gaussian variance epsilon I; smoothing both noise endpoints gives gamma_(2epsilon) | Common covariance smoothing p_(2epsilon)*gamma matches the current source conventions exactly. |
| (2.12)–(2.14),p2150; (2.15)–(2.19),pp2151–2152 | Ordered chain kernels, full Wick pairings, nonnegative even moments, finite-Lp convergence and tensor-product identity | Includes self-pairs and unequal order products. There is no Wiener-chaos orthogonality assumption. |
| d3 measure convention(2.22),pp2152–2153 | Time-integrated products of sphere Green measures define the deterministic chain measure; same noise-smoothed L2 limit | This is compatible with first removing the project's Green smoothing at fixed noise smoothing. |
| Theorem3.8(i),(3.23),p2165 | Under Dalang, fixed-order L2 convergence with all endpoint spatial widths tending to zero | Products of two fixed orders converge in L1. Finite split sums converge; individual raw-diagram identification is unnecessary. |
| (5.1)–(5.3),p2173; upper half(5.15),p2180 | Full total-order coefficient homogeneity; positive moment series; factorial coefficient asymptotics for each fixed p | At p2 this is exactly the needed static all-pairing,all-split coefficient input. |

Each endpoint covariance is an ordinary locally integrable Riesz function
in d2 or d3. Its positive definiteness follows from the standard positive
Gaussian-mixture identity already written in the current notes. In the initial
power proposal gamma^r=c^r|x|^(-alpha r), so beta=alpha r and amplitude c^r;
it is not the covariance with amplitude c. In the sharper interpolation both
endpoints can instead use the same amplitude c.

## 3. Static coefficient bound: directly supported by the source

Write U_n for the static Stratonovich orders and

  B_k(t)=sum_(m=0)^(2k) E[U_m(t,x) U_(2k-m)(t,x)],  B_0=1.

Equations(2.17),(2.19) and the nonnegative Green measure show that this is
the same complete positive Wick-pairing sum used by the project, with temporal
covariance1. The finite-order regularized version is the expectation of a
product of regularized orders. In particular no missing binomial coefficient
or additional factorial is introduced by this notation.

For p2, source(5.1) says

  B_k(t)=t^((4-beta)k) B_k(1).

The finite upper coefficient rate in(5.15) says that

  limsup_(k->infinity) (1/k) log[(k!)^(3-beta) B_k(1)] < infinity.

It follows, by increasing a finite parameter-dependent constant to cover the
finitely many low orders, that

  B_k(t) <= C_(beta,c,d)^k t^((4-beta)k)/(k!)^(3-beta),  k>=1,t>0.   (S)

The passage from the source's asymptotic coefficient statement to an all-k
finite C is a local elementary deduction. It is not a claim that the source
prints this particular C. Source(5.13),p2179, also supplies a non-asymptotic
intermediate coefficient bound with a Gamma denominator; the argument for its
upper asymptotics is visible in(5.15). Only finiteness is used here, not the
sharp variational expression.

### Independent alternative deduction from the source growth theorem

This requested alternative is not needed if (5.15) is cited directly.
Put Q=3-beta>1,P=4-beta and kappa_s=P/Q. Source positivity and(5.2) give
B_k(1)s^(Pk)<=E u_static(s,x)^2. By the finite growth upper bound, choose
L>0 and s0 so that the latter is at most exp(L s^kappa_s) for s>=s0.
For all sufficiently large k choose s_k=(Qk/L)^(1/kappa_s), obtaining

  B_k(1) <= [e^Q(L/Q)^Q]^k k^(-Qk)
          <= [e^Q(L/Q)^Q]^k/(k!)^Q.

The last direction uses k!<=k^k. Absorb the finitely many smaller k into C
and use homogeneity. No all-time source growth bound is assumed; no uniformity
in beta,c,or smoothing width is claimed. This establishes precisely the
coefficient-majorant consequence queried by the initial power proposal.

## 4. Two-input parameter compatibility

For1<alpha<2-alpha0 choose once and for all

  alpha0<theta<2-alpha,
  b0=alpha0/theta,
  beta=(alpha-theta)/(1-theta).

Then0<theta<1,0<b0<1,1<beta<2, and

  alpha=theta*1+(1-theta)*beta,
  alpha0=theta*b0+(1-theta)*0.

The interval is nonempty exactly under the standing higher-alpha existence
condition. A concrete witness beyond the strictly partial original proposal:
alpha=7/4,alpha0=1/8,theta=3/16 gives beta=25/13 and b0=2/3.
Here alpha+2alpha0=2, so the original strict partial regime does not apply.
Both static and degree-one fractional-time endpoints are valid in d2 and d3.
No limit to b0=1 or beta=2 is used, and constants may deteriorate near either.

With gamma_lambda(x)=c|x|^(-lambda), the pointwise profile identity is

  gamma_alpha = gamma_1^theta gamma_beta^(1-theta).

The endpoint at degree1 in d2/d3 is correlated Riesz noise, not spatial white
noise. The accepted Proposition P:low-alpha-upper includes exactly this case.
The two endpoint Gaussian fields need not be probabilistically coupled:
Hölder is on deterministic diagram integrands, not on random solutions.

## 5. Regularized common measure and limits: compatibility check

Fix total order2k and horizon t. Take the disjoint union over all splits
m+n=2k and all pairings D, with counting measure, ordered time Lebesgue
measure and the positive product of the2k Green increment measures. The
roots and finite horizons are identical for both endpoints. This is a finite
positive measure (the spatial mass is product_l h_l; time simplexes are bounded).
In d3 one may first use common smoothed Green measures G_(h,eta).

For each common positive edge covariance width epsilon,
Gaussian Hölder on the probability density p_epsilon gives

  (p_epsilon*gamma_alpha)(z)
    <= (p_epsilon*gamma_1)(z)^theta
       (p_epsilon*gamma_beta)(z)^(1-theta).

Every edge in each endpoint uses the same width as its target edge; choosing
one common noise width gives edge width2epsilon in all three models.
All spatial convolutions are finite because the Riesz degrees are below d.
The target temporal cutoff satisfies

  gamma_delta^0(s-r) <= |s-r|^(-alpha0)
                       = (|s-r|^(-b0))^theta.

Do **not** assert a Hölder identity for the different temporal cutoff kernels.
It is unnecessary. The endpoint1 diagram factor uses spatial smoothing and
raw temporal power b0; the accepted Section5 deterministic estimates apply
uniformly to it, as they already bound the smoothed temporal covariance by
that raw kernel. Thus this endpoint is not being identified with an unproved
mixed-smoothing random solution.

Multiplying the pointwise bounds and applying Hölder on the complete common
measure leads to the candidate finite-order estimate

  A_(alpha,alpha0;epsilon,delta,eta),k(t)
    <= C_low^theta*k t^((3-b0)theta*k)/(k!)^(2theta)
       * [B_(beta;epsilon,eta),k(t)]^(1-theta).                 (H)

Here `C_low^theta*k` means `(C_low)^(theta k)`. It should be typeset
unambiguously in the actual candidate. The endpoint1 bound includes the full
pairing/split sum; applying Hölder separately and forgetting the discrete
measure would lose the desired coefficient control.

For fixed positive spatial noise width, each covariance is bounded continuous.
In d3, product Green weak convergence and the bound by a constant times
product_l h_l let eta decrease to zero in the static endpoint. The source's
measure convention pp2152–2153 is exactly that limit. The target uses its
source-prescribed inner Green limit at fixed noise smoothing. The uniform
low-endpoint bound needs no new limit identification.

Next Theorem3.8(i) gives B_(beta;epsilon),k(t)->B_beta,k(t): for every finite
split, the two regularized static orders converge in L2, so their product
converges in L1; there are only2k+1 splits. Constant/empty chains cause no
problem. For the target, the time-dependent author's Theorem4.1 and the
existing P:mixed argument give the corresponding fixed-order mixed limit as
noise smoothing vanishes. This uses neither monotonicity in epsilon nor a
uniform-in-epsilon static large-time theorem. One takes the finite-order
limit first and only then invokes(S).

Consequently the proposed interpolation's exponents are consistent:

  factorial power = 2theta+(1-theta)(3-beta)=3-alpha,
  time power = theta(3-b0)+(1-theta)(4-beta)=4-alpha-alpha0.

These are application checks supporting the proof assignment, not independent
acceptance of an unwritten interpolation theorem. A finished proof must spell
out(H), its measure and limit order, and the final nonnegative coefficient
series summation. No raw singular-diagram equality is silently needed here.

## 6. Literature implication and true remaining obligations

The static theorem is printed and directly supplies(S), but does not itself
state the fractional-time result. The prior bounded crosswalk found only the
cruder second-moment estimate in the pinned time-dependent author source;
its first-moment theorem does not imply this p2 conclusion. CDST's narrower
pathwise hypotheses and Balan's static stronger spectral condition remain as
recorded; this audit finds no reason to reopen those rejected direct mappings.
This is not a fresh comprehensive citation-chain/MathSciNet/zbMATH search and
not a novelty verdict.

**PROCEED scope:** write and falsify-check the precise two-input Riesz
interpolation theorem, including d3's inner Green limit and all discrete
multiplicities, then obtain the mandated cross-family scientific review.
The static endpoint compatibility is established at the source/application
level. The absent temporal-cutoff logconvexity is **not** an unresolved premise.

**Remaining work before any promotion:**
1. A complete self-contained interpolation deduction with exact source pinpoints
   and constants dependent on the fixed theta,b0,beta,c,d.
2. Finite-order2/4 checks for all splits/empty blocks and amplitude powers;
   they diagnose counting but do not replace the all-order Hölder argument.
3. Root scrutiny and independent cross-family review of the actual candidate,
   plus normal manuscript/build/provenance gates.
4. Keep the scope isotropic Riesz; arbitrary homogeneous anisotropic covariance
   need not factor into admissible endpoint covariances. Sharp constants remain
   open and the full original goal must not be silently narrowed.

This audit is GPT-family work. It supplies neither a skeptic vote nor Lean
verification and does not alter the pending Round4 acceptance boundary.
