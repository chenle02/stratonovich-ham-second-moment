# Ordinary-G corollary: finite consumer inventory

Date: 2026-10-28 UTC. Status: **finite combinatorial inventory only**.
No analytic estimate was evaluated or proved in this task. No manuscript,
source PDF, sibling, registry or git mutation. The inventory neither certifies
nor enlarges the separately reviewed deterministic weighted-convolution result.
No all-order or second-moment conclusion is asserted.

Inputs read: the exact crossing-pair merge diagnostic, the source audit, and
sufficiency-screen.md, especially its ordinary-G corollary(Section8a).
Enumeration: consumer_inventory.py, with exact output consumer-inventory.json.
Reproduce from the repository root with

  python3 reviews/2026-10-28-wc-probe/consumer_inventory.py

The script enumerates3 diagrams at total order2 and15 at total order4.
These are all pair partitions times all chain-length splits at these degrees,
including empty chains. It does not evaluate stochastic or spatial integrals.

## Roles and notation

A chain has its fixed root0 followed by its ordered pairing vertices. Every
vertex except the LAST one in a nonempty chain has one incoming and one
outgoing Green factor; call it I(interior). This includes the FIRST vertex of
a chain of length at least2. The last vertex has only its incoming Green
factor; call it T(terminal). A chain of length1 has one terminal and no
interior vertex. Roots are not paired vertices. The final time horizon is an
upper integration limit, not an additional outgoing Green factor.

For a pairing edge joining interior i and terminal j, let a,b be the times
of the surviving predecessor and successor of i, and let T be j's time.
These are clocks, not graph-type symbols. The ordinary-G spatial corollary
integrates i over(a,b), but does NOT include its temporal covariance
|T-v|^(-alpha0).

Table shorthand:

- `IT-end`: terminal j is i's same-chain successor, so T=b exactly.
- `IT-gap`: same chain, terminal is later than the successor, so T>b.
- `IT-cross0`: different chains and i is first in its chain; T can lie inside
  (0,b) or to its right, in positive-measure time regions.
- `IT-cross`: different chains and i is not first; T can lie to the left,
  inside or to the right of(a,b), again on positive-measure regions.
- `TT`: neither paired endpoint has two adjacent Green factors.
- `II`: neither endpoint is terminal; this edge is not selected by the proposed
  terminal-incident-edge rule at that stage.

## Complete total-order2 inventory

| Split | Pairing | Edge classification |
|---|---|---|
| (0,2) | (1,2) | IT-end |
| (1,1) | (1,2) | TT |
| (2,0) | (1,2) | IT-end |

Already at this degree the temporal-endpoint and two-terminal cases occur.
The deterministic spatial corollary alone does not cover either full
fractional-time integrand.

## Complete total-order4 inventory

Use A=(1,2)(3,4), B=(1,3)(2,4), C=(1,4)(2,3).
In each row edge classifications are in that pairing's printed order.

| Split | Pairing | Edge classifications |
|---|---|---|
| (0,4) | A | II; IT-end |
| (0,4) | B | II; IT-gap |
| (0,4) | C | IT-gap; II |
| (1,3) | A | IT-cross0; IT-end |
| (1,3) | B | IT-cross; IT-gap |
| (1,3) | C | TT; II |
| (2,2) | A | IT-end; IT-end |
| (2,2) | B | II; TT |
| (2,2) | C | IT-cross0; IT-cross0 |
| (3,1) | A | II; TT |
| (3,1) | B | IT-gap; IT-cross |
| (3,1) | C | IT-cross0; IT-end |
| (4,0) | A | II; IT-end |
| (4,0) | B | II; IT-gap |
| (4,0) | C | IT-gap; II |

Exact totals across the30 edges are II9,IT18,TT3. The18 IT edges split into:
6 IT-end,6 IT-gap,4 IT-cross0,2 IT-cross.

Every listed diagram has a terminal-incident pairing edge. Such an edge has
an interior partner or a terminal partner, as proposed in the root's screen.
This classification does not by itself provide an admissible analytic merge.
For example, split(2,2), pairing B has the terminal edge(2,4) of type TT,
while its other edge(1,3) is II. There is no IT edge to select instead.

The script additionally deletes both paired labels for every possible
terminal-incident choice and reclassifies the surviving chains. All finite
paths at these two degrees can be completed as GRAPH deletions. At order4,
9 diagrams admit one such initial choice and6 admit two, hence21 complete
pair-deletion sequences in this finite bookkeeping. These are algorithm
choices, not extra diagram multiplicities. Multiplying an integral by21 or
counting each sequence as a separate Wick term would be unjustified.

## What the ordinary-G corollary actually permits

Holding the other positions/times fixed, removing a covariance edge incident
to an interior vertex would require estimating the actual object

  W(a,b,T;x,z,w) = integral_a^b dv |T-v|^(-alpha0)
    integral_R^2 dy G_(v-a)(y-x)G_(b-v)(z-y)gamma_epsilon(w-y).

The corollary controls the expression WITHOUT |T-v|^(-alpha0), uniformly in w.
If a valid temporal-weighted estimate eliminated the pairing factor, its
uniformity in w would make the paired terminal spatial variable carry only
its remaining incoming Green factor at that stage. Integrating such a
terminal spatial factor gives its mass(the current incoming time gap), but
its time variable and any inherited weights remain. This is bookkeeping of
which factors occur, not a claim that the needed weighted estimate holds.

The current sufficient estimate has an h^(2-alpha) prefactor, h=b-a, and
replaces two adjacent Green factors by G_h(z-x). The following obligations
remain separate.

### A. Same-chain endpoint temporal singularity

For IT-end, T=b identically. The old bound
|T-v|^(-alpha0)<=(T-b)^(-alpha0) is infinite and unusable. This is not a rare
cross-chain coincidence: it occurs in2 of3 total-order2 diagrams and on6 IT
edges at order4. A useful argument must integrate(b-v)^(-alpha0) jointly
with the two wave factors and spatial covariance, or retain additional
structure. Alpha0<1 alone does not license removing the temporal weight
from this nonuniform spatial integral.

### B. Cross-chain temporal singularity inside the merge interval

For cross-chain IT edges, T may lie INSIDE(a,b). For example split(2,2),
pairing C, select edge(1,4). Vertex1 merges between its root time0 and s2,
while T=s4. The domain permits0<s3<s4<s2, with s1 integrated over(0,s2),
so v=T is an interior temporal singularity. The region s4<s2 has positive
measure. A distance-to-interval pullout is infinite throughout that region.

For split(1,3), pairing B and edge(1,3), the interior vertex3 merges between
s2 and s4 while the other chain's terminal time s1 can be before, inside or
after that interval. The independent chain order does not put it outside.

### C. Both endpoints terminal

TT is present in split(1,1) at order2 and in3 order4 diagrams. Neither endpoint
has an outgoing Green factor, so the interior-vertex corollary cannot be
applied directly. The actual conditional object has two terminal clocks:

  integral_a^t du integral_b^t dv |u-v|^(-alpha0)
    integral_R^2 dy integral_R^2 dz
       G_(u-a)(y-x)G_(v-b)(z-w)gamma_epsilon(y-z).

Here(a,x),(b,w) are the retained parents, possibly the roots. This is not the
single-intermediate-clock object W. Chen's integrated pair norms are a source
lead already recorded in source-audit.md, but this inventory neither imports
an order-sharp consequence nor resolves the known common-theta factorial loss.

### D. Previously created gap powers and surviving temporal factors

After a merge, h^(2-alpha) depends on the two neighboring surviving times.
A later merge may integrate one of those times, so the prefactor is not
necessarily constant in the new integral. The powers can involve overlapping
or nested gaps. Likewise terminal time integration can still meet a remote
temporal factor or an earlier bound's gap cost. Each factor must be recorded
before invoking another kernel estimate. Restoring ordinary G form only solves
one spatial shape issue; it does not show that the complete weighted family
is closed under repeated elimination.

### E. Counting and factorial budget

The target requires a denominator of order(k!)^(3-alpha) after summing all
pairings and all2k+1 splits. A finite graph-deletion schedule does not supply
this denominator. A future induction must state whether its choice of edge is
unique, how different diagrams map to descendants, and how time domains and
pairing multiplicities are counted. The successful lower-alpha argument used
symmetry only after summing temporal pairings; selectively merging clocks can
destroy that visible common domain. Nothing here proves it is preserved.

## Next bottleneck and stop boundary

The next analytic question is a temporal-weighted interior merge(or a bound
that deliberately retains the remote-time average), handling both T=b and
T inside(a,b) with stated uniformities. A separate two-terminal estimate is
also unavoidable for this particular terminal-edge selection strategy.
The need for both cases is already visible in the exact low-order inventory.

No full all-order bound should be inferred from the ordinary-G spatial
corollary or this enumeration. No Skorohod result was developed. No conclusion
against the Stratonovich moment conjecture is drawn. This inventory stops
before deriving either missing analytic estimate.
