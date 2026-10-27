# One bounded mean-comparison mechanism attempt

**Status:** unreviewed mathematical attempt; no proof of G:upper or of a mean comparison. This is a single attempt to obtain a genuine mechanism behind A_k<=K C^k a_k or D_k<=K C^k a_k, not another finite-coefficient sampling run. Its proposed intermediate comparison is falsified, while the fully integrated comparisons remain open. The new shuffle identity and conditional no-go should receive non-GPT review before promotion.

[held back: collaborators' unpublished work]

## 1. Exact chronological-shuffle identity

Write N=2k and Delta_N(t)={0<s_1<...<s_N<t}. A word c=(c_1,...,c_N) in {1,2}^N records which of the two original chains owns each vertex after their times are merged into chronological order. Let p_c(i) be the previous index of the same color, or0 if none; set s_0=0 and spatial root z_0=0. For a pairing D of {1,...,N}, assign an independent spatial coordinate z_e to each pair e, and write e(i) for the pair containing i. Define the nonnegative spatial volume

    V_(c,D)(s)
      = 2^(-2k) integral_(R^k)
          product_(i=1)^(2k)
          1{ |z_(e(i))-z_(e(p_c(i)))|
                                  < s_i-s_(p_c(i)) } dz,

where the previous spatial value is0 when p_c(i)=0. This is the result of integrating all k delta covariances; there is no extra factorial in this spatial contraction. Put

    H_c(s) = sum_(D in Pi_k) V_(c,D)(s)
                         product_((i,j) in D)|s_i-s_j|^(-alpha0).

Let c_* be the constant word. Then the exact identities are

    a_k(t) := E X_(2k)(t,x)
      = integral_(Delta_(2k)(t)) H_(c_*)(s) ds,

    A_k(t) := sum_(m+n=2k) E[X_m(t,x)X_n(t,x)]
      = sum_(c in {1,2}^(2k))
          integral_(Delta_(2k)(t)) H_c(s) ds,                 (SH)

    D_k(t) := E X_k(t,x)^2
      = sum_(c: number of1s = number of2s = k)
          integral_(Delta_(2k)(t)) H_c(s) ds.

**Derivation, including multiplicities.** For a fixed split(m,n), partition the product of its two ordered time simplices according to their merged chronological order. Ties form a null set. Each compatible shuffle is uniquely encoded by a binary word with m occurrences of1 and n of2. Relabel every spatial variable and every pairing by the same permutation. This is a bijection on Pi_k, preserves Lebesgue measure and temporal covariance factors, and changes each chain predecessor precisely to p_c. White-space contractions then give V_(c,D). Summing over splits includes each binary word once. For an empty chain there is exactly one constant word of that color. There are2^(2k) words in total, and binom(2k,k) balanced words; neither an extra binomial nor a compensating factorial is permitted in(SH). Nonnegative integrands justify the finite decompositions and changes of order. The generalized-kernel passage is exactly the already-reviewed G0/G1 delta convention.

This identity begins with the actual chain domains and includes the self-pairings. It does not posit a mean comparison.

## 2. The attempted integrated mechanism: spatial integration first

The proposed intermediate inequality was

    H_c(s) <= K L^k H_(c_*)(s)                              (TSC)

for every admissible ordered time vector s and every word c, with K,L depending only on alpha0. This would be more than a pointwise Green-kernel domination: all spatial variables are already integrated, and all Wick pairings are already summed. If it held, the exact word counts in(SH) would immediately give

    A_k(t) <= K(4L)^k a_k(t),
    D_k(t) <= K(4L)^k a_k(t),

which would establish the required mean comparisons without assuming them as hypotheses. This was the concrete mechanism tested.

### Exact obstruction at four vertices

Choose k=2, the balanced word c=1212, and ordered times

    (s_1,s_2,s_3,s_4)=(b,b+epsilon,b+2epsilon,b+3epsilon),
    b>0, epsilon>0, b+3epsilon<t.

Denote the chronological pairings by A=(12)(34), B=(13)(24), C=(14)(23). The one-chain spatial volumes are, by the G1 calculation with increments(b,epsilon,epsilon,epsilon),

    V_(*,A)=V_(*,B)=V_(*,C)=b*epsilon/4.

Their temporal factors are respectively epsilon^(-2alpha0), (2epsilon)^(-2alpha0), and3^(-alpha0)epsilon^(-2alpha0). Consequently

    H_*(s)
      = (b/4) epsilon^(1-2alpha0)
        [1+2^(-2alpha0)+3^(-alpha0)].

For c=1212, the pairing B=(13)(24) is **domestic in both chains**. Its first chain has positions(x,x), times(s_1,s_3); the second has positions(y,y), times(s_2,s_4). Thus the two root factors permit |x|<b and |y|<b+epsilon, while both within-chain displacements vanish. The four Green factors contribute1/16, so

    V_(1212,B)(s)=b(b+epsilon)/4.

Its temporal factor remains(2epsilon)^(-2alpha0). All other summands are nonnegative. Therefore

    H_(1212)(s)/H_*(s)
      >= 2^(-2alpha0)(b+epsilon)
          / { epsilon[1+2^(-2alpha0)+3^(-alpha0)] }
      -> infinity as epsilon↓0 with b fixed.                (OB)

This contradicts(TSC) for every finite K,L even at the fixed degree k=2. Since c=1212 is balanced, it obstructs both the full coefficient route and the diagonal route when attempted by this conditional comparison. Summing over all words cannot help at fixed times because the offending term is positive. The inequalities are stable for small perturbations of the chosen increments, so the failure is not confined to an isolated time vector.

**What this proves, if independently confirmed.** No uniform comparison can be obtained by first conditioning on every time variable, then integrating space and summing pairings, and finally comparing that density with the one-chain density at the same time vector.

**What it does not prove.** It does not disprove A_k<=K C^k a_k or D_k<=K C^k a_k after time integration. The bad region shrinks when epsilon becomes small; a temporal change of variables or an averaged inequality might compensate. The same conditional obstruction already exists at alpha0=0, where G1's fully integrated ratios at k=2 are finite(32 and17). That calibration explicitly prevents promoting(OB) to a global no-go. It also does not rule out Chen's Theorem3.1 in every form.

[held back: collaborators' unpublished work]

## 3. Why the attempted repair remains unresolved

The white-space proof attempt has reached a precise missing step. An integrated mechanism must move or average the time variables together with the spatial cone volume; it cannot use(TSC) as its local lemma. In the witness, the two-chain volume retains a factor of order b² while every one-chain volume has a factor b*epsilon. Moving some initial waiting time b into a later gap could increase the one-chain spatial volume, but it changes the temporal covariance factors. For B, increasing an internal gap changes both short temporal distances; their fractional singularity cannot simply be discarded or replaced by a uniform constant. No measure-preserving transformation with a controlled Jacobian and covariance ratio was found in this bounded attempt.

Accordingly the unresolved step is **not** “assume A_k<=K C^k a_k.” It is to construct a justified time-and-space integrated rearrangement, or another explicit operator inequality, that compensates for the loss in(OB) with at most exponential cost in k. Neither the Gaussian product formula nor the static trace estimates supply such a transformation. No alternative long proof wave or further numerical probe was opened after this failure.

## 4. Chen–Hu source direction: two different lower bounds

There is a label/number distinction in the local source that matters here.

### Local label L-5

In `sources/llm_pack/chen_hu-25-hyperbolic.tex`, label L-5 is the coefficient lower bound. The published counterpart is **Lemma5.3,(5.22), p2183**, not the introduction's “moment inequality” Lemma5.4. Its exact direction is

    liminf_(n→infinity) (1/n) log {
       (n!)^(3-alpha)
       sum_(l_1+...+l_p=2n) E product_(j=1)^p S_(l_j)(g_(l_j)(.,1,0)) }
      >= log { (1/2)^(3-alpha) p^(4-alpha)
                         [2*sqrt(M)/(4-alpha)]^(4-alpha) }.

This is a **lower** bound, under the time-independent assumptions of their Theorem1.2. Its proof uses concentration in the time-randomized moment representation. It cannot be reversed to bound D_n or A_k from above by a first moment.

### The introduction's moment inequality

The actual moment inequality is local label **L-6**, published **Lemma5.4,(5.29), p2186**. For p>1 and nonnegative f in the spatial noise Hilbert space H it says

    ||u(t,0)||_p
      >= exp[-||f||_H²/(2(p-1))]
         sum_(n>=0) <f^(tensor n), g_n(.,t,0)>_(H^(tensor n)).

The direction is again **lower**. The proof starts from Hölder duality with a particular normalized Gaussian exponential test variable and then retains a subset of nonnegative pairings. Optimizing over such f still produces a lower bound: these test variables are not shown to exhaust the whole L^q unit ball, and the discarded pairings have the wrong sign for an upper estimate. Thus this lemma is a potential input to a future lower-bound question, not the missing upper norm/mean comparison in the present attempt. No fractional-time extension is asserted.

Both displayed source statements were checked from rendered published PDF pages40 and43(journal pp2183,2186). Publisher artifact: `../SPDEForge/sources/chen_hu-25-hyperbolic/published-24-AOP1758.pdf`, SHA-256 `58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22`. The local TeX was used to resolve labels, not to invent published numbering.

## 5. Balan trace input: read, but not silently transferred

The extraction in `recon/balan-contraction-input.md` was read, and the rendered publisher p2663,(38), was checked. It bounds a partial-trace Hilbert norm in the time-independent model, with its original spectral constant and trace-counting consumer. Its condition involving integral(1+|xi|²)^(-1/2)mu(dxi) excludes one-dimensional spatial white noise, and unpaired time variables have already been integrated away in that static kernel. Therefore it is not an upper bound for the white, fractional-time objects in this attempt.

The extracted TTRACE-definition/estimate/consumer remains a separate open transfer obligation. It was not taken as a proved lemma, and the existing static estimate was not altered by replacing alpha with alpha+alpha0 or by dropping temporal Hilbert factors. This avoids hiding the current missing mechanism in a source citation.

## Outcome, review boundary and ownership

[held back: collaborators' unpublished work]

STATUS: DONE_WITH_CONCERNS — one bounded serious mechanism attempt completed; no main-goal proof and no accepted new theorem.
