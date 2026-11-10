# White-space total-order-four calibration: full sector derivation and custody

Author-only finite calibration audit at exact scientific source `b4b6efccacbbccd8f747225330e9ccb27bc097a6`. This is not a new moment theorem, a closed moment formula, a Skorohod result, an asymptotic constant, an independent review, or a confidence upgrade. Original MEDIUM and the newly reported ungraded LIMITED state are preserved. No provider, Article/ref/sibling edit, Lean or HPC work occurred; the live six-proof candidate was not changed.

**Result.** All 27 printed canonical sector integrals, their 28 polynomial pieces, all nine normalized static entries and all 15 ordered split/pairing diagrams check exactly. The static total-order-four coefficient is `11 t^6/540`. No mathematical error or missing author-side polynomial case was found. The prior author calculation was already complete for the 27 canonical integrals; the new contribution here is an explicit readable geometric/integration derivation, current-source custody, and direct exchanged-split arithmetic. It does not invent a new proof or independent coverage where only author evidence exists.

## 1. What already existed, and what this packet checks

Read first, as requested: `<HOME>/.local/state/Le-AI-Lab/stratonovich-static-sectors-worked-v1/check.py` and `worked-sectors.json`. The old JSON already records every canonical sector's chain lengths, full bivariate integrand, active u/v bounds, inner polynomial, exact piece value, total and normalization. It includes both pieces at u=1/3 of the last sector. Thus its author-side all-27 polynomial work was complete. The unresolved depth was an independent fully worked review of those calculations and/or exchanged-split correspondence, not a missing 28th polynomial case.

The old script used SymPy1.14.0, hard-coded the nine physical length pairs and expected printed values, and checked the old full-main hash at887. It writes its existing JSON, so it was not rerun in place. Those two files are preserved byte-for-byte as `prior-check.py` and `prior-worked-sectors.json`.

`exact_check.py` is a new small standard-library/Fractions custody/replay implementation. It derives spatial chain lengths from the actual pair partitions and vertex-position lists; it does not input the nine old length pairs. It enumerates all five ordered chain-length splits and all three pairings, integrates all45 representative sectors, and checks all27 canonical integrands, piece bounds, inner polynomials and values against the old artifact, as well as the currently printed sector/static tables. This is an additional exact local calculation, not an independent model review.

Exact current bindings:

- Main file SHA256: `364753242f9d02e57036af586ab8e777b184d897862750d3170d79f028067914` at `b4b6efc`.
- PROOF011 is `P:white-four`, statement starts line1682, proof1709–1744; raw body SHA256 `cd91ff9d36f8c300f7f30b49bf7ff059fd1196e39f96d070a05305aeb6c13662`.
- PROOF012 is `L:static-four`, statement starts line1746, proof1762–1837; raw body SHA256 `d70d1f064e2f7441e6663c26d985f8cc9459c7dea6a451ddb3455f225f0d6e1a`.
- Both bodies are byte-identical to887, although the complete main file and line offsets changed outside them. Historical proof-index-v3 locators are seven lines later; this packet resolves current declarations/proofs by exact labels and hashes.
- `source-white-static-excerpt.tex.txt` contains exact source lines1636–1838, including the full white and static tables/proofs. `exact-results.json` binds the complete-source hash, excerpt, legacy files and every integration case.

## 2. Physical pairings: every white-space table row

Use exactly d=α=1, Γ=δ0 and `G(h,z)=1/2 · 1{abs(z)<h}`. There are four noise vertices and four Green indicators, so the spatial Green prefactor is `(1/2)^4=1/16`. The three **labeled** Wick pair partitions are

    A={(1,2),(3,4)}, B={(1,3),(2,4)}, C={(1,4),(2,3)}.

Each has coefficient one. Delta contractions identify the two vertices of the first listed pair with a free position x and those of the other pair with y. This leaves ordinary Lebesgue integration dx dy with unit contraction Jacobian; it adds neither a factor2 nor a factor3. Write w=abs(x−y).

Within each chain the root is zero. For a nonempty chain, cumulative noise times are a, a+b, a+b+c, a+b+c+d as needed. For the1+3 split the single time is r. The chain gap domains are exactly the source domains: four positive gaps of sum<t for0+4; r∈(0,t) and three positive gaps of sum<t for1+3; a+b<t and c+d<t for2+2.

Define F(a,b,c) as the area of `abs(x)<a, abs(y)<b, abs(x−y)<c`. Subtracting the two corner triangles from the rectangle gives

    F(a,b,c)=4ab−(a+b−c)_+²+(|a−b|−c)_+².

It is symmetric under swapping x/y and the determinant-one map (x,y)↦(x,x−y). This symmetry is an area identity, not an extra multiplicity in a Wick sum.

The following displays every canonical row. A position list is written in chain order; “—” means the empty chain. Its spatial factor V is area/16, and q1,q2 are the time differences read from the same pairing labels.

| Split,D | Positions in the two chains | Actual spatial constraints / area | V | q1,q2 |
|---|---|---|---|---|
| 0+4,A | — ; (x,x,y,y) | abs(x)<a, w<c; area4ac | ac/4 | b,d |
| 0+4,B | — ; (x,y,x,y) | abs(x)<a, w<min(b,c,d); area4a min(b,c,d) | a min(b,c,d)/4 | b+c,c+d |
| 0+4,C | — ; (x,y,y,x) | abs(x)<a, w<min(b,d); area4a min(b,d) | a min(b,d)/4 | b+c+d,c |
| 1+3,A | (x) ; (x,y,y) | abs(x)<min(r,a), w<b; area4 min(r,a)b | min(r,a)b/4 | abs(r−a),c |
| 1+3,B | (x) ; (y,x,y) | abs(x)<r, abs(y)<a, w<min(b,c) | F(r,a,min(b,c))/16 | abs(r−a−b),b+c |
| 1+3,C | (x) ; (y,y,x) | abs(x)<r, abs(y)<a, w<c | F(r,a,c)/16 | abs(r−a−b−c),b |
| 2+2,A | (x,x) ; (y,y) | abs(x)<a, abs(y)<c; area4ac | ac/4 | b,d |
| 2+2,B | (x,y) ; (x,y) | abs(x)<min(a,c), w<min(b,d); area4 min(a,c)min(b,d) | min(a,c)min(b,d)/4 | abs(a−c),abs(a+b−c−d) |
| 2+2,C | (x,y) ; (y,x) | abs(x)<a, abs(y)<c, w<min(b,d) | F(a,c,min(b,d))/16 | abs(a−c−d),abs(a+b−c) |

A zero spatial increment still has a positive time gap and a Green factor1/2; it is not deleted. For example in0+4,A the second and fourth minimal spatial gaps are zero, but all four time slack variables remain. This matters for the later4! denominator.

Thus the finite fractional-time coefficient for a row is the integral of `V(q1 q2)^(−α0)` over its stated four-dimensional time domain. Time-coordinate scaling yields t^4, spatial area scaling yields t², and the two covariance factors yield t^(−2α0): each coefficient scales as `t^(6−2α0)`. This reproduces PROOF011's finite-order claim, with no all-order inference.

## 3. Static limit and the time-first simplex formula

Fix 0<ā<1. On the unit time cube all paired differences are at most1, so for0≤α0≤ā the two temporal powers are dominated by their powersā. The spatial factor is at most1/4: the four vertices lie in[−1,1], and two free positions have area≤4, multiplied by1/16. Each pairing uses two disjoint pairs of labels, hence on the full cube the dominating temporal integral is

    [ ∫_0^1∫_0^1 |s−r|^(−ā) ds dr ]²
      = [ 2/((1−ā)(2−ā)) ]² <∞.

The gap/time-coordinate change has Jacobian one. Restricting to ordered chain domains only decreases this nonnegative majorant. Dominated convergence therefore sets α0=0 in each finite row. No large-time/static limit is exchanged, and no uniform asymptotic constant in α0 is asserted.

For fixed free x,y, let Lρ be the sum of the absolute successive spatial increments along chainρ, starting at zero. Each chain gap can be written as its required nonnegative absolute displacement plus a positive slack. With nρ vertices, the remaining time domain is an nρ-dimensional simplex of volume `(1−Lρ)_+^(nρ)/nρ!`. An empty chain contributes one everywhere. Therefore

    J_(m,n,D)(1)|static
       = 1/(16 m! n!) ∫_(R²) (1−L1)_+^m (1−L2)_+^n dx dy.      (3.1)

The factorials come from these time simplex volumes, not a new Wick weight or an extra symmetrization. Reading the position lists gives all nine length pairs:

| Split,D | L1 | L2 |
|---|---|---|
| 0+4,A | 0 | abs(x)+w |
| 0+4,B | 0 | abs(x)+3w |
| 0+4,C | 0 | abs(x)+2w |
| 1+3,A | abs(x) | abs(x)+w |
| 1+3,B | abs(x) | abs(y)+2w |
| 1+3,C | abs(x) | abs(y)+w |
| 2+2,A | abs(x) | abs(y) |
| 2+2,B | abs(x)+w | abs(x)+w |
| 2+2,C | abs(x)+w | abs(y)+w |

Split the free plane into three representative chambers and their simultaneous reflections (x,y)↦(−x,−y):

    S1: 0≤x≤y,       (x,y)=(u,u+v),  (abs(x),abs(y),w)=(u,u+v,v),
    S2: 0≤y≤x,       (x,y)=(u+v,u),  (abs(x),abs(y),w)=(u+v,u,v),
    S3: x≥0≥y,       (x,y)=(u,−v),   (abs(x),abs(y),w)=(u,v,u+v).

Here u,v≥0 and every chart has absolute Jacobian one. Their interiors and reflected interiors are disjoint and cover the plane apart from the lines x=0,y=0,x=y, which have dx dy measure zero. Every length is reflection invariant. Thus the one factor2 in the normalized row is exactly the reflection factor, and not a chain-exchange factor:

    J_(m,n,D)(1)|static = [2/(16m!n!)] (I_S1+I_S2+I_S3).         (3.2)

## 4. Explicit integration of every one of the27 canonical sectors

On a sector, L1 and L2 are the linear functions listed below. Its domain is u≥0,v≥0 and Lρ≤1 only for a nonempty chain. Put P(u,v)=(1−L1)^m(1−L2)^n on that domain. The table gives **every** active case, its v integral Q(u), and its exact outer integral. `u^k` denotes an ordinary integer power. The last sector has two pieces, so there are27 sectors and28 lines. There is no omitted support region or crossing constraint.

| Sector | L1; L2 | u range | v upper bound | Q(u)=integral P dv | Exact integral Q du |
|---|---|---|---|---|---|
| 0+4 A S1 | 0; u+v | [0,1] | 1 - u | `(1-u)^5/5` | 1/30 |
| 0+4 A S2 | 0; u+2v | [0,1] | 1/2 - u/2 | `(1-u)^5/10` | 1/60 |
| 0+4 A S3 | 0; 2u+v | [0,1/2] | 1 - 2*u | `(1-2·u)^5/5` | 1/60 |
| 0+4 B S1 | 0; u+3v | [0,1] | 1/3 - u/3 | `(1-u)^5/15` | 1/90 |
| 0+4 B S2 | 0; u+4v | [0,1] | 1/4 - u/4 | `(1-u)^5/20` | 1/120 |
| 0+4 B S3 | 0; 4u+3v | [0,1/4] | 1/3 - 4*u/3 | `(1-4·u)^5/15` | 1/360 |
| 0+4 C S1 | 0; u+2v | [0,1] | 1/2 - u/2 | `(1-u)^5/10` | 1/60 |
| 0+4 C S2 | 0; u+3v | [0,1] | 1/3 - u/3 | `(1-u)^5/15` | 1/90 |
| 0+4 C S3 | 0; 3u+2v | [0,1/3] | 1/2 - 3*u/2 | `(1-3·u)^5/10` | 1/180 |
| 1+3 A S1 | u; u+v | [0,1] | 1 - u | `(1-u)^5/4` | 1/24 |
| 1+3 A S2 | u+v; u+2v | [0,1] | 1/2 - u/2 | `9·(1-u)^5/80` | 3/160 |
| 1+3 A S3 | u; 2u+v | [0,1/2] | 1 - 2*u | `(1-u)·(1-2·u)^4/4` | 11/480 |
| 1+3 B S1 | u; u+3v | [0,1] | 1/3 - u/3 | `(1-u)^5/12` | 1/72 |
| 1+3 B S2 | u+v; u+2v | [0,1] | 1/2 - u/2 | `9·(1-u)^5/80` | 3/160 |
| 1+3 B S3 | u; 2u+3v | [0,1/2] | 1/3 - 2*u/3 | `(1-u)·(1-2·u)^4/12` | 11/1440 |
| 1+3 C S1 | u; u+2v | [0,1] | 1/2 - u/2 | `(1-u)^5/8` | 1/48 |
| 1+3 C S2 | u+v; u+v | [0,1] | 1 - u | `(1-u)^5/5` | 1/30 |
| 1+3 C S3 | u; u+2v | [0,1] | 1/2 - u/2 | `(1-u)^5/8` | 1/48 |
| 2+2 A S1 | u; u+v | [0,1] | 1 - u | `(1-u)^5/3` | 1/18 |
| 2+2 A S2 | u+v; u | [0,1] | 1 - u | `(1-u)^5/3` | 1/18 |
| 2+2 A S3 | u; v | [0,1] | 1 | `(1-u)^2/3` | 1/9 |
| 2+2 B S1 | u+v; u+v | [0,1] | 1 - u | `(1-u)^5/5` | 1/30 |
| 2+2 B S2 | u+2v; u+2v | [0,1] | 1/2 - u/2 | `(1-u)^5/10` | 1/60 |
| 2+2 B S3 | 2u+v; 2u+v | [0,1/2] | 1 - 2*u | `(1-2·u)^5/5` | 1/60 |
| 2+2 C S1 | u+v; u+2v | [0,1] | 1/2 - u/2 | `31·(1-u)^5/240` | 31/1440 |
| 2+2 C S2 | u+2v; u+v | [0,1] | 1/2 - u/2 | `31·(1-u)^5/240` | 31/1440 |
| 2+2 C S3 | 2u+v; u+2v | [0,1/3] | 1/2 - u/2 | `(1-u)^3·(141·u^2-132·u+31)/240` | 995/69984 |
| 2+2 C S3; piece2 | 2u+v; u+2v | [1/3,1/2] | 1 - 2*u | `(1-2·u)^3·(3·u^2-3·u+2)/15` | 47/349920 |

Here are derivations of the displayed polynomial forms, sufficient to reproduce every entry without a numerical quadrature or unexplained CAS assertion.

1. The triangular fourth-power case obeys

       ∫_0^((1−pu)/q) (1−pu−qv)^4 dv = (1−pu)^5/(5q),
       ∫_0^(1/p) (1−pu)^5/(5q) du =1/(30pq),       p,q>0.

   This covers all nine0+4 entries and all three2+2,B entries, with the p,q shown by their L-functions.
2. If the short-chain length is u and the long-chain length u+cv, the1+3 integrand is `(1−u)(1−u−cv)^3`; integrating v gives `(1−u)^5/(4c)`, whose outer integral is1/(24c). This covers1+3,A/S1, B/S1, C/S1 and C/S3. The1+3,C/S2 case has both lengths u+v, so it is the triangular fourth-power case.
3. For1+3,A/S2 and B/S2, substitute `v=(1−u)t/2`. The v integral is

       (1−u)^5/2 ∫_0^1(1−t/2)(1−t)^3 dt
       =(1−u)^5/2 ·(1/4−1/40)=9(1−u)^5/80.

   Its outer integral is9/(80·6)=3/160.
4. For1+3,A/S3 the v integral is `(1−u)(1−2u)^4/4`. Substituting z=1−2u in the outer integral gives

       1/16 ∫_0^1(1+z)z^4 dz =1/16(1/5+1/6)=11/480.

   The B/S3 case has an additional factor1/3 from its v slope and is11/1440.
5. For2+2,A/S1 and S2, the v integral is `(1−u)^5/3`, giving1/18. In S3 the domain is the unit square and P=(1−u)²(1−v)², giving(1/3)²=1/9.
6. For2+2,C/S1 and S2, substitute `v=(1−u)t/2`. The two squared factors give

       Q(u)=(1−u)^5/2 ∫_0^1 (1−t/2)^2(1−t)^2 dt
           =(1−u)^5/2 ·[1−3/2+13/12−3/8+1/20]
           =31(1−u)^5/240.

   The outer value is31/1440. Swapping the two length factors is harmless here because both exponents are2; no pairing itself is merged or counted twice.
7. For the final2+2,C/S3 entry,

       P=(1−2u−v)^2(1−u−2v)^2,
       0≤u≤1/2,
       0≤v≤min(1−2u,(1−u)/2).

   The upper lines meet at u=1/3. Direct polynomial antiderivation in v gives exactly the two Q polynomials factored in the table. In expanded form they are

       Q1=−47u^5/80+37u^4/16−85u^3/24+21u²/8−15u/16+31/240,
       Q2=−8u^5/5+4u^4−14u^3/3+3u²−u+2/15.

   Applying `∫_a^b Σ c_j u^j du =Σ c_j(b^(j+1)−a^(j+1))/(j+1)` yields

       ∫_0^(1/3)Q1 du=995/69984,
       ∫_(1/3)^(1/2)Q2 du=47/349920,
       sum=(4975+47)/349920=31/2160.

The new Fraction implementation expands P binomially, integrates each term in v up to the active affine upper bound, then uses that last rational antiderivative formula. It selects crossings by exact rational arithmetic and verifies all constraints on both endpoints and the midpoint of every piece. It checks each factored Q above against the independently generated polynomial, and checks each canonical polynomial/domain/piece value against the already complete old JSON. No float, sampled quadrature or statistical test is used.

## 5. The nine normalized rows, and every multiplicity

The normalization factors in (3.2) are1/192 for0+4,1/48 for1+3 and1/32 for2+2. Applying them to the three-sector sums gives

| Canonical row | Sum of three representative sector integrals | Reflection/Green/simplex factor | Normalized J(1) |
|---|---|---|---|
| 0+4 A | 1/15 | 1/192 | 1/2880 |
| 0+4 B | 1/45 | 1/192 | 1/8640 |
| 0+4 C | 1/30 | 1/192 | 1/5760 |
| 1+3 A | 1/12 | 1/48 | 1/576 |
| 1+3 B | 29/720 | 1/48 | 29/34560 |
| 1+3 C | 3/40 | 1/48 | 1/640 |
| 2+2 A | 2/9 | 1/32 | 1/144 |
| 2+2 B | 1/15 | 1/32 | 1/480 |
| 2+2 C | 31/540 | 1/32 | 31/17280 |

The total order is the sum of two Stratonovich orders, not an orthogonal chaos order. The expansion uses all five ordered splits (0,4),(1,3),(2,2),(3,1),(4,0); each has exactly the three pair partitions A,B,C with unit coefficient. There is no binomial shuffle factor: each chain already has its own ordered time integration. There is no factor3 in addition to summing A,B,C, and no second factor2 for2+2.

**Exchange0+4 with4+0.** The nonempty four-vertex chain keeps its labels1,2,3,4; A,B,C remain A,B,C. These are two different terms of the product expansion, so each contributes its full row sum11/17280.

**Exchange1+3 with3+1.** Relabel the old long-chain vertices2,3,4 as new1,2,3 and the old single vertex1 as new4. This permutation sends

    old A=(12)(34) → new C=(14)(23),
    old B=(13)(24) → new B=(13)(24),
    old C=(14)(23) → new A=(12)(34).

It is not correct to retain each pairing label individually in this exchange. More explicitly the3+1 position lists are `(x,x,y);(y)` for A, `(x,y,x);(y)` for B and `(x,y,y);(x)` for C. Their length pairs are respectively

    (abs(x)+w,abs(y)), (abs(x)+2w,abs(y)), (abs(x)+w,abs(x)).

Swapping the free names x,y in the first two shows the A↔C/B-fixed correspondence with the1+3 lengths; C already has the1+3,A integrand with the exponents exchanged. Direct spatial table checking at nonzero α0 gives the same result:3+1,A has V=F(r,a,c)/16 and temporal gaps b,abs(a+b+c−r); B has V=F(r,a,min(b,c))/16 and gaps b+c,abs(a+b−r); C has V=min(r,a)b/4 and gaps abs(r−a),c. These are precisely the1+3,C/B/A integrands, with the two temporal factors merely interchanged when necessary.

The new exact script also integrates all3+1 sectors directly from these vertex lists, not just by declaring symmetry. Their representative sector triples are A=(1/30,1/48,1/48), B=(3/160,1/72,11/1440), C=(1/24,3/160,11/480). Multiplication by1/48 gives normalized A=1/640, B=29/34560, C=1/576. Their sum is143/34560, exactly the1+3 sum. Exchanging the two2-vertex chains preserves A,B,C, but that is a symmetry within the one2+2 product term, not a new term or multiplicity.

For clarity, all15 directly computed static diagram coefficients are

| Ordered split | A | B | C | Split sum |
|---|---|---|---|---|
| 0+4 | 1/2880 | 1/8640 | 1/5760 | 11/17280 |
| 1+3 | 1/576 | 29/34560 | 1/640 | 143/34560 |
| 2+2 | 1/144 | 1/480 | 31/17280 | 187/17280 |
| 3+1 | 1/640 | 29/34560 | 1/576 | 143/34560 |
| 4+0 | 1/2880 | 1/8640 | 1/5760 | 11/17280 |

Restoring the finite t^6 factor, the full rollup is therefore

    2·11/17280 + 2·143/34560 +187/17280
       =(22+143+187)/17280
       =352/17280=11/540.

The root's independent0+4 arithmetic matches exactly: h1 h3/4, h1 min(h2,h3,h4)/4 and h1 min(h2,h4)/4 integrate over Σh<t to t^6/2880,t^6/8640,t^6/5760. Their sum is11t^6/17280. At this one finite order the full coefficient is32 times that mean0+4 sum; the decomposition is2+13+17=32 in units of the mean sum. **No all-order moment identity is inferred or developed from this finite consistency check.**

As a separate finite check of PROOF012's last sentence, with one paired position x the static0+2 integral is

    (1/(4·2!))∫_(−1)^1(1−abs(x))^2 dx=1/12,

whereas1+1 is `(1/4)∫_(−1)^1(1−abs(x))^2 dx=1/6`. Thus the total-order-two coefficient is1/6+2·1/12=1/3, and the2+2,A self-pair row is(1/12)²=1/144. These are finite normalization checks only.

## 6. Disposition and limits

No real error was found in the white/static source table, the all27 canonical integrations, the exchanged3+1 sum, pairing counts or the11/540 rollup. The old author all-sector calculation was already complete; this packet makes its source/geometry/case correspondence explicit and adds direct exchanged-split enumeration and a separate exact arithmetic implementation. It does not transform that author evidence into independent review coverage. The old MEDIUM and the new ungraded LIMITED statuses remain what they were until root obtains and adjudicates actual sufficient review.

[held back: collaborators' unpublished work]