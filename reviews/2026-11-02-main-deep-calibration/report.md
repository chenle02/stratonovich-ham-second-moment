# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

None. I found no proof gap, false identity, hidden hypothesis, incorrect constant, sign error, boundary-term error, or invalid asymptotic in any of PROOF010–019 after independent re-derivation. Specifically, no entry in the white order-four table, none of the 27 static sector values, no rollup, and no stated constant ($K_{\rm sp}$, $K_{\rm sp}^{\rm gen}$, $c_0$, $Z$, $C_2$, $C_{1,*}$, $\rho$, $\kappa$, $\beta$, $q$, $b$, $F(a,b,c)$, $\pi/2$, $1/16$, $2^{-(3-\alpha)}$) is wrong.

## Noncritical findings

1. **Chain-exchange relabeling is stated at sum level, not row level.** PROOF011 proves the $(4,0)$ and $(3,1)$ *sums* equal the $(0,4)$ and $(1,3)$ sums "without changing the covariance factors." The exact per-row permutation for the six chain-exchanged diagrams is left implicit. I derived it: for $(0,4)\leftrightarrow(4,0)$ the relabeling is the identity ($A\mapsto A, B\mapsto B, C\mapsto C$); for $(1,3)\leftrightarrow(3,1)$ the 4-cycle $1\mapsto4,\ 2\mapsto1,\ 3\mapsto2,\ 4\mapsto3$ induces $A\leftrightarrow C$, $B\mapsto B$. The displayed multiplicity $2\sum_{(0,4)}D + 2\sum_{(1,3)}D + \sum_{(2,2)}D$ is correct. Only the explicit row table is missing.

2. **Dependency sighting, not re-derivation.** Several regularization passages in PROOF010/012/015/018 invoke the constructor-file lemmas (`L:damped-homogeneous-norms`, `L:joint-fixed-order`). I read these (they are in-scope, embedded), verified the norm scalings $N_0=\theta^{-2}$, $N_1=\theta^{\alpha+\alpha_0-2}N_1(1)$, $N_2^2=\theta^{-\beta}N_2(1)^2$ directly, and followed the joint-limit logic, but I did **not** re-derive the Brownian moment bound `(E:construction-brownian-moments)` line-by-line. This is a spot-checked dependency, not silently assumed.

3. **Imported Theorem 3.1 and Appendix A.1 are text-layer sourced.** They are cited inputs; the notes independently re-derive the $N_0/N_1/N_2$ constants needed to use them. The source PDF rendered pages (PNG) were not inspectable in this read-only run; the manifest itself warns the PDF text layer garbles math. I verified the *statement* of Theorem 3.1 (including the $Q_0/Q_1/Q_2$ count $q_0=q_1$, $q_0+q_2/2=k$ and the base cases reproduced in the embedded text) against its use, but did not sight rendered pages.

4. **Exponent-first vs. static-first scope.** The ten proofs are self-consistent in repeating that they establish the $\alpha\le1$ upper bound and finite-order coefficients only; they do not overclaim the intrinsic limit or sharp constants. The abstract-level claims (limit identification, "component proofs passed") exceed these ten proofs, but that text is outside the assigned target set and is not contradicted by the ten proofs.

## Checked derivations

**PROOF010 (P:envelope).** Verified $N_0=\theta^{-2}$, $2N_0N_1$ and $N_2^2$ both of degree $-\beta$; combined Theorem-3.1 exponent $-2q_0+(\alpha+\alpha_0-2)q_0-\beta(k-q_0)=-\beta k$ independent of the partition; $K\ge\max\{2N_1(1),N_2(1)^2\}$ suffices. Infimum at $\theta=\beta k/(2t)$ equals $e^{\beta k}(2t/\beta k)^{\beta k}$. Factorial bracketing $k!\le P_k\le 2^k k!$, $k!^\beta/k^{\beta k}\in[e^{-\beta k},1]$, $2k+1\le3^k$ give $\sum_k(at^\beta)^k/(k!)^q\le B_K\le\sum_k(bt^\beta)^k/(k!)^q$ with $q=\beta-1$; upper series $\le e^{qz^{1/q}}$, lower by $k=\lfloor z^{1/q}/2\rfloor$ term $\ge2^{qk}$. Hence $ct^\rho\le\log B_K\le Ct^\rho$, $\rho=\beta/(\beta-1)=\frac{4-\alpha-\alpha_0}{3-\alpha-\alpha_0}>\kappa$; $\rho\in(1,2)$ since $\beta>2$. No-go correctly scoped to the numerical majorant only; the missing $(k!)^{\alpha_0}$ and the $p=1$/empty-chain distinction are stated honestly.

**PROOF011 (P:white-four).** Re-derived $F(a,b,c)=4ab-(a+b-c)_+^2+(|a-b|-c)_+^2$ in all three regimes ($c\ge a+b$; $c\le|a-b$; between) and its 3-fold symmetry. Verified all nine displayed rows by reconstructing the position lists $(x,x,y,y)$ etc., computing the areas $4ac,\ 4a\min(b,c,d),\ 4a\min(b,d),\ 4\min(r,a)b,\ F(r,a,\min(b,c)),\ F(r,a,c),\ 4\min(a,c)\min(b,d),\ F(a,c,\min(b,d))$ under the $1/16$ factor, and the time gaps ($b,d;b+c,c+d;b+c+d,c;|r-a|,c;|r-a-b|,b+c;|r-a-b-c|,b;b,d;|a-c|,|a+b-c-d|;|a-c-d|,|a+b-c|$). Scaling $t^4\cdot t^2\cdot t^{-2\alpha_0}=t^{6-2\alpha_0}$ confirmed for all three splits.

**PROOF012 (L:static-four).** Re-derived the static reduction $J=(16\,m!\,n!)^{-1}\int(1-L_1)_+^m(1-L_2)_+^n\,dxdy$ including the simplex-Jacobian reasoning and empty-chain factor $=1$. Verified all nine length pairs ($(0,|x|+w)\dots(|x|+w,|y|+w)$). **Independently recomputed all 27 sector integrals** (table below) via the parametrizations $(u,u+v),(u+v,u),(u,-v)$; every entry matches. In particular the two displayed "explicit" integrals gave $31/1440$ (exact) and $31/2160$ (confirmed two ways: an $(s,t)=(2u+v,u+2v)$ change of variables with $\int=(1/3)\cdot31/720=31/2160$, and the $s$-first full-region split after correcting the antiderivative sign). Rollups with the $2/(16\,m!\,n!)$ reflection factor reproduce the row table exactly; totals reproduce $11/17280, 143/34560, 187/17280$ and $11/540$; static order-2 $t^3/3$ via $c_0|_{\alpha_0=0}=1/6$.

**PROOF013 (P:riesz-small).** Verified the convolution $\int_{\mathbb R^2}G(s,y)G(r,z)c_\alpha|y-z|^{-\alpha}\,dydz=c_\alpha((s+r)^{2-\alpha}-|s-r|^{2-\alpha})/(2(1-\alpha)(2-\alpha))$ (checked at $s=r=1$ against direct integration $2^{1-\alpha}/((1-\alpha)(2-\alpha))$). Both order-two coefficients: $\mathbb E X_2$ via the simplex integral $\int_{r+v<t}rv^{1-\alpha-\alpha_0}$ giving $t^\beta/[(1-\alpha)(2-\alpha-\alpha_0)(3-\alpha-\alpha_0)(4-\alpha-\alpha_0)]$; $\mathbb E X_1^2$ via $s>r$+doubling giving the displayed bracket. Static rollup $\frac{c_\alpha\,2^{3-\alpha}}{(1-\alpha)(2-\alpha)(3-\alpha)(4-\alpha)}$ re-derived; normalized $c_\alpha=(1-\alpha)/2$ limits to $1/3$ and to $c_0/2,c_0$. Order-four parametrization verified: $G=\frac12\mathbf 1$ is $h_l$ times the Uniform$[-1,1]$ law; the $1/16$ sits in the four uniform densities; the map is triangular per chain (det 1); scaling $t^4\cdot t^4\cdot t^{-2\alpha-2\alpha_0}=t^{2\beta}$, $c_\alpha^2$ from two pairs; disjoint-pair finiteness for $\alpha_0,\alpha<1$.

**PROOF014 (L:d1-spatial).** Verified the centered-supremum bound $c_\alpha h^{1-\alpha}/(1-\alpha)$, Tonelli transfer to $\gamma_\epsilon$, and the strong white case bound $c_\delta/2$. Verified the descending-label invariant (at a closing label the only covariance through $y_l$ is its own pair; at an opening label its partner is already removed), giving $\prod_O h_i\prod_C h_j^{1-\alpha}$ (Riesz) and $\prod_O h_i$ (white). Verified the sharp weighted AM-GM (Lagrange form) $\prod h_l^{w_l}\le(2t/bk)^{bk}(1-\alpha)^{(1-\alpha)k}$, which after $(c_\alpha/(1-\alpha))^k$ yields exactly $\frac{c_\alpha 2^{2-\alpha}(1-\alpha)^{-\alpha}}{(2-\alpha)^{2-\alpha}}$; white gives $b=1,\ K_{\rm sp}=c_\delta$.

**PROOF015 (P:d1-upper).** Verified $Z=\frac2{(1-\alpha_0)(2-\alpha_0)}$, $\int F_k=P_k(Zt^{2-\alpha_0})^k$, symmetry of $F_k$ under all permutations, and the block-order cell count $\binom{2k}{m}=\frac{(2k)!}{m!(2k-m)!}$ giving $P_k(Zt^{2-\alpha_0})^k/(m!(2k-m)!)$. Verified $P_k=(2k)!/(2^k k!)$, $\sum_m1/(m!(2k-m)!)=2^{2k}/(2k)!$, and the combination to $(2ZK_{\rm sp})^kt^{\beta k}/(k!\,k^{bk})$ with the $(2k)!$ cancellation. Verified $k!\,k^{bk}\ge(k!)^{3-\alpha}$ (correct direction for an upper bound) and $C_2=q(2ZK_{\rm sp})^{1/q}$. Noted and accepted the explicitly non-sharp spot checks ($2(3-\alpha_0)>4$; static order-4 bound $1/2$ vs exact $11/540$).

**PROOF016 (L:low-alpha-convolution).** Verified $\mu(B_R)=V R^\alpha$, $\mu(\{0\})=0$, layer-cake $\int\min(h,|\xi|^{-1})\mu=\frac{V}{1-\alpha}h^{1-\alpha}$; the multiplier bound $|e^{-(\eta+\epsilon)|\xi|^2/2}|,|\sin(h|\xi|)/|\xi||$ giving the upper bound, and nonnegativity ($\gamma$ a nonnegative distribution, $G_{h,\eta}\ge0$) giving the lower bound; uniformity in $\eta,\epsilon,z$; valid for $d=1,2,3$ with $G_h(\mathbb R^d)=h$ and no spectral density.

**PROOF017 (L:alpha-one-convolution).** Verified $\mu(cA)=c\mu(A)$, $\mu(\{0\})=0$, the polar decomposition $\mu(\mathrm d\xi)=\mathrm dr\,\sigma(\mathrm d\theta)$ with $\sigma$ of mass $V$ and even; the combined multiplier $e^{-ar^2}$, $a=(\epsilon+\eta)/2$; the polar formula $\int I_a(h,\theta\cdot z)\sigma(\mathrm d\theta)$; the one-dimensional inversion $(g_h*p^{(1)}_{2a})(v)=\frac1\pi I_a(h,v)$ (factor 2 absent because both antipodal directions are in $\sigma$); $0\le I_a\le\pi/2$ hence the bound $\frac{\pi V}{2}$; $d=1$ white matching $K_{\rm sp}^{\rm gen}=\pi V=c_\delta$ via $\mu(\mathrm d\xi)=c_\delta\,\mathrm d\xi/(2\pi)$; oscillation retained throughout, degree-one ≠ full white in $d=2,3$.

**PROOF018 (P:low-alpha-upper).** Verified the dimension-free descending-label transfer (only which increments enter each position matters), closing masses $Mh_l^{1-\alpha}$ ($M=V/(1-\alpha)$) at $\alpha<1$ and constant $M=\pi V/2$ at $\alpha=1$; the AM-GM giving $K_{\rm sp}^{\rm gen}$ exactly ($\alpha=1$: $M^k\prod_O h_i\le(2M)^kt^k/k^k$ with $2M=\pi V$); the temporal part identical to PROOF015; the $d=3$ two-stage limit (Green width $\eta\downarrow0$ first via weak convergence of measure products with masses $\prod_l h_l$ and bounded Gaussian covariance factors, then noise widths via `L:joint-fixed-order`, products in $L^1$); $V=0\Rightarrow u\equiv1$ guard; scope $\alpha\le1$ only.

**PROOF019 (C:d1-first-calibration).** Verified: one chain means $\sum h_l\le t$, driving the $t/2$ substitution in the spatial bound, giving $K_*^k t^{bk}/(2^{bk}k^{bk})$; temporal sum on the single simplex is $P_k(Zt^{2-\alpha_0})^k/(2k)!$; combined exponent $2^{-(bk+k)}=2^{-k(3-\alpha)}=(2^{b+1})^{-k}$; hence $\mathbb E X_{2k}\le(ZK_*/2^{3-\alpha})^kt^{\beta k}/(k!\,k^{bk})\le(ZK_*/2^{3-\alpha})^kt^{\beta k}/(k!)^q$; $C_{1,*}=q(ZK_*/2^{3-\alpha})^{1/q}=C_{2,*}/2^{(4-\alpha)/(3-\alpha)}$; $2C_{1,*}<C_{2,*}$ since $(4-\alpha)/(3-\alpha)>1$; Jensen comparison conditional on a verified first-moment lower bound; auxiliary constants honestly flagged as bounds, not sharp first-moment constants.

## Required fixes before production gate

None required for the correctness of PROOF010–019. Two recommended (not blocking) items for a full cold close:

1. Write out the explicit A/B/C relabeling table for the six chain-exchanged white diagrams (currently proved at sum level; the per-row maps are $(0,4)\leftrightarrow(4,0)$: identity; $(1,3)\leftrightarrow(3,1)$: $A\leftrightarrow C$, $B$ fixed).
2. Close rendered-page sighting of the imported Theorem 3.1 (3.6) and Appendix (A.1)/(A.3) pinpoints, since the PDF text layer is extraction-garbled; no rendered PNG was inspectable in this run. This affects dependency record-keeping, not the ten proofs' deductions.

## One-line summary

The ten assigned proofs are internally consistent and correct: I independently re-derived all 15 white order-four diagrams, all 27 static sector integrals with their rollups ($11/540$, $t^3/3$), the Riesz order-two/four coefficients, the $d=1$ spatial bound and $\alpha\le1$ upper bounds, the low-$\alpha$/$\alpha=1$ spectral convolution constants, and the first-moment calibration, and every stated constant, sign, boundary term, factorial direction, and asymptotic exponent matched — with only the explicit chain-exchange row table and source rendered-page sighting left implicit (both non-blocking).

---

### CAL01–CAL12 checks

| Check | Verdict | Basis |
|---|---|---|
| CAL01 PROOF010 P:envelope | PASS | Norm scalings, partition identity, $\theta$ optimum, both factorial directions, $\rho>\kappa$, no-go scoped to the majorant. |
| CAL02 PROOF011 P:white-four | PASS | 9 rows + 6 chain-exchange sums + $F$ formula + $1/16$ + $t^{6-2\alpha_0}$; exact per-row A/B/C exchange map left implicit (noncritical). |
| CAL03 PROOF012 L:static-four | PASS | All 27 sectors, 9 row integrals, rollups, $11/540$, $t^3/3$ re-derived independently. |
| CAL04 PROOF013 P:riesz-small | PASS | Double-interval convolution, both order-2 terms, $c_\alpha^2$, $t^{2\beta}$, unit-domain parametrization, finiteness, normalization remarks. |
| CAL05 PROOF014 L:d1-spatial | PASS | Descending-label invariant, both branches, consumed powers, exact $K_{\rm sp}$, white endpoint. |
| CAL06 PROOF015 P:d1-upper | PASS | Sum-before-symmetry, $P_k$, binomial/counts, factorial direction, vanishing-noise, no individual-diagram overclaim. |
| CAL07 PROOF016 L:low-alpha-convolution | PASS | Ball mass, layer-cake, min/h bound, uniform smoothing, $d=1/2/3$. |
| CAL08 PROOF017 L:alpha-one-convolution | PASS | Polar decomposition, $\pi/2$, Gaussian inversion, $d=1$ white match, no density, no $d\ge2$ white substitution. |
| CAL09 PROOF018 P:low-alpha-upper | PASS | Dimension-free closure, exact $K_{\rm sp}^{\rm gen}$, $d=3$ limit, $V=0$ guard, $\alpha\le1$ scope. |
| CAL10 PROOF019 C:d1-first-calibration | PASS | $t$ vs $2t$ budget, $2^{-(3-\alpha)k}$, $C_{1,*}/C_{2,*}$ ratio, conditional Jensen, nonzero guards. |
| CAL11 Falsification/consumer audit | PASS | Zero amplitude/order, white order-2/4 normalization, chain exchange, $\alpha_0\downarrow0$, normalized Riesz $\alpha\uparrow1$, $\alpha=1$ without isotropy all checked; only Theorem 3.1 + supplied constructor lemmas consumed; source §5(ii)/(5.3)–(5.4) correctly not imported. |
| CAL12 Coverage/honesty | PASS | All 10 proofs CHECKED; full row ledgers below; no forced HIGH, no global/full-213/image clearance; rendered-page sighting limitation recorded. |

### Proof status table (canonical PROOF010–019)

| ID | Label | Status |
|---|---|---|
| PROOF010 | P:envelope | CHECKED |
| PROOF011 | P:white-four | CHECKED |
| PROOF012 | L:static-four | CHECKED |
| PROOF013 | P:riesz-small | CHECKED |
| PROOF014 | L:d1-spatial | CHECKED |
| PROOF015 | P:d1-upper | CHECKED |
| PROOF016 | L:low-alpha-convolution | CHECKED |
| PROOF017 | L:alpha-one-convolution | CHECKED |
| PROOF018 | P:low-alpha-upper | CHECKED |
| PROOF019 | C:d1-first-calibration | CHECKED |

### White order-four diagram ledger (15 diagrams)

**(a) Nine displayed rows**

| (m,n) | D | V | q1 | q2 | Status |
|---|---|---|---|---|---|
| (0,4) | A | $ac/4$ | $b$ | $d$ | CHECKED |
| (0,4) | B | $a\min(b,c,d)/4$ | $b+c$ | $c+d$ | CHECKED |
| (0,4) | C | $a\min(b,d)/4$ | $b+c+d$ | $c$ | CHECKED |
| (1,3) | A | $\min(r,a)b/4$ | $\|r-a\|$ | $c$ | CHECKED |
| (1,3) | B | $F(r,a,\min(b,c))/16$ | $\|r-a-b\|$ | $b+c$ | CHECKED |
| (1,3) | C | $F(r,a,c)/16$ | $\|r-a-b-c\|$ | $b$ | CHECKED |
| (2,2) | A | $ac/4$ | $b$ | $d$ | CHECKED |
| (2,2) | B | $\min(a,c)\min(b,d)/4$ | $\|a-c\|$ | $\|a+b-c-d\|$ | CHECKED |
| (2,2) | C | $F(a,c,\min(b,d))/16$ | $\|a-c-d\|$ | $\|a+b-c\|$ | CHECKED |

**(b) Six chain-exchanged diagrams**

| (m,n) | Status | Relabeling |
|---|---|---|
| (4,0) A,B,C | CHECKED | Identity ($u\mapsto u$); rows equal (0,4) rows |
| (3,1) A,B,C | CHECKED (sum level) | 4-cycle induces $A\leftrightarrow C$, $B$ fixed; row sums equal (1,3) sums |

### Static four row ledger (Lemma L:static-four, $\alpha_0=0$)

**27 sector integrals** (columns: $0\le x\le y$, $0\le y\le x$, $x\ge0\ge y$)

| (m,n) | D | S1 | S2 | S3 | Status |
|---|---|---|---|---|---|
| (0,4) | A | $1/30$ | $1/60$ | $1/60$ | CHECKED |
| (0,4) | B | $1/90$ | $1/120$ | $1/360$ | CHECKED |
| (0,4) | C | $1/60$ | $1/90$ | $1/180$ | CHECKED |
| (1,3) | A | $1/24$ | $3/160$ | $11/480$ | CHECKED |
| (1,3) | B | $1/72$ | $3/160$ | $11/1440$ | CHECKED |
| (1,3) | C | $1/48$ | $1/30$ | $1/48$ | CHECKED |
| (2,2) | A | $1/18$ | $1/18$ | $1/9$ | CHECKED |
| (2,2) | B | $1/30$ | $1/60$ | $1/60$ | CHECKED |
| (2,2) | C | $31/1440$ | $31/1440$ | $31/2160$ | CHECKED (two independent exact routes) |

**9 static row integrals and totals**

| (m,n) | A | B | C | row sum | Status |
|---|---|---|---|---|---|
| (0,4) | $1/2880$ | $1/8640$ | $1/5760$ | $11/17280$ | CHECKED |
| (1,3) | $1/576$ | $29/34560$ | $1/640$ | $143/34560$ | CHECKED |
| (2,2) | $1/144$ | $1/480$ | $31/17280$ | $187/17280$ | CHECKED |

Static total-order-four $=11\,t^6/540$ (CHECKED), static total-order-two $=t^3/3$ (CHECKED).