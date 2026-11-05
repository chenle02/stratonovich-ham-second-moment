# Independent MAIN-family audit — CURRENT af97 Unit G (OWN170–193, 25 roles, three joins)

**Model/edition.**  
Manuscript `af97ae4db921a660b0a4ed1ffbe9b6f53a487e2b`. Audited scope is exactly the canonical G OWN deductions 170–193 and formal roles S196–S219, plus S064 as an optional logical-GIVEN/context role. Original model preserved: \(d\in\{1,2,3\}\), \(0<a=\alpha_0<1\), \(0<\alpha<d\) or \(\alpha=d=1\), \(\alpha+a<2\), nonnegative even positive-definite homogeneous tempered Radon \(\Gamma\), actual amplitude, data \((1,0)\), white/singular/zero cases, full real \(H_I\) signed controls.

**Method.**  
This is a source-facing mathematical audit. Every item is assessed against the complete current proof text supplied for the four module bodies `GT` (`integrated_gaussian_tubes.tex`), `UP` (`integrated_uniform_products.tex`), `PT` (`integrated_point_transfer.tex`), `SU` (`integrated_signed_moment_upper.tex`). No tools/execution were used. Upstream OWN clauses (C/A/D/E/F/B and earlier units) are application-matched, not accepted full parents. H199–213 are treated as downstream, not premises.

**Unforced verdict/confidence.**  
- Global verdict: **not a complete all-cases closed proof; the G24 deductions are mathematically coherent and mostly complete individually, conditional on named upstream OWN inputs.**
- Overall confidence: **MEDIUM** for the G24 local deductions, **LOW-MEDIUM** for the full three-join closure without additional outside-parent work.

---

## 1. Individual coverage — `integrated_gaussian_tubes.tex` (GT)

### 170 / S200 `P:tube-wiener-realization` (GT34–124, stmt 21–32)
**WORK/PROOF.**  
Establishes a genuine abstract Wiener realization from an actual first-chaos Gaussian variable \(X\): countable norming family generates Borel sets; Gaussian regression \(X_j=\mathbb{E}[X\mid \sigma(W(e_1),\dots,W(e_j))]\) in a Bochner \(L^2\) sense; \(L^2(\mathscr B)\) convergence; support \(E_0=\overline{C(H)}\); minimal Cameron norm \(\|Ch\|_{\mathrm{CM}}=\|P_{\mathrm{seen}}h\|_H\); Radon tightness; full support via finite-head/tail independence; explicit measurable-norm tail.
**Exact hypotheses.**  
H separable, \(W\) isonormal, \(\mathbb E\|X\|^2<\infty\), all coordinates in \(W(H)\), \(C=\sqrt\delta\mathcal M_\delta\) with compact \(\mathcal M_\delta\).
**Coverage/status.** **FULL_LOCAL_DEDUCTION.**  
The proof is complete for the stated abstract setting. It does not by itself prove the actual law is eligible; that is 173.
**Remaining obligation.**  
Application-specific compactness and same-\(W\) coordinate checks; no gap found in the abstract deduction.

### 171 / S196 `L:tube-closed-geometry` (GT162–200, stmt 144–160)
**WORK/PROOF.**  
Compact image of a closed Hilbert ball; closed \(A_\delta+\mathcal M_\delta\overline B_H(r)\); least finite radius attainment; sublevel identity; tail \(\mathbb P(d_\delta(X)>r)\le e^{-r^2/(2\delta)}\) via imported FH11.6 after actual closed/Borel eligibility.
**Exact constants.** \(b_\delta=2\mathbb E\|X\|\); unit Cameron ball scaled by \(\sqrt\delta\).
**Coverage/status.** **FULL_LOCAL_DEDUCTION.**  
Borel/closedness handled explicitly; nonzero and zero-law branches separated.
**Remaining obligation.**  
FH11.6 is imported; its actual hypothesis application is checked here.

### 172 / S201 `P:tube-rayleigh-transfer` (GT217–247, stmt 202–215)
**WORK/PROOF.**  
Scalar Rayleigh layer-cake domination: upper level sets as upper intervals; open/closed endpoints; zero law with \(F(0)\le G(0)\), not \(F(0)=0\); least-radius attainment gives \(F(X)\le G(d_\delta(X))\).
**Exact topology.** Borel \(F,G\); \(G\) nondecreasing.
**Coverage/status.** **FULL_LOCAL_DEDUCTION.**
**Distinction.** Scalar stochastic domination, not spectral ground-state Rayleigh (that is 179).

### 173 / S202 `P:tube-actual-law` (GT299–352, stmt 275–297)
**WORK/PROOF.**  
Constructs actual stopped same-\(W\) tuple \(X_\delta=(X_m)\); separable little \(C^\theta\) compact-operator product; \(H=H_I\); normalized mean \(\mathcal M_\delta\); covariance \(C_\delta=\sqrt\delta\mathcal M_\delta\); compactness at fixed parameters; typical radius \(b_\delta\le C_{Q,B,p}\delta^{(1-a)/2-d/Q}\to0\).
**Coverage/status.** **FULL_CONDITIONAL.**  
Depends on 155/160/169/173 interactions and fixed-Q guards. The proof is internally complete conditional on those upstream OWN results.
**Constants.** Fixed even \(Q\): \(Q\gamma>d\), \(\beta_t-\eta_t-1/Q>0\), \(Q>2d/(1-a)\).
**Remaining obligation.** Radius-anchor and path norms themselves are upstream (158/160), not re-derived here.

### 174 / S197 `L:tube-actual-endpoint` (GT375–417, stmt 354–373)
**WORK/PROOF.**  
Every ambient compact tuple has compact Young/free norm floor \(\ge1\); actual124 same-source physical restart; global endpoint \(P_{\delta,E}^R(L,0)\) equals ordered block product; \(e^{F_\delta/\delta}=\|P_\delta\|^2\).
**Coverage/status.** **FULL_CONDITIONAL.**  
Uses 124 restart and165 norm floor; they are named OWN inputs, not re-proved.

### 175 / S203 `P:tube-coarse-envelope` (GT441–512, stmt 421–439)
**WORK/PROOF.**  
Coarse envelope \(G_\delta(r)\le C_{\mathrm{env}}(1+b_\delta^\nu+r^\nu)\); radial moment bound from172.
**Exact constants.** \(D_0,D_1,D_2\) with \(D_0=4/B(\log G_B+c_Y)\) etc.
**Coverage/status.** **FULL_LOCAL_DEDUCTION.**

### 176 / S198 `L:tube-rayleigh-tail` (GT526–547, stmt 514–524)
**WORK/PROOF.**  
For \(A_0+Cr^\nu\), \(1<\nu<2\), \(4C\le M^{2-\nu}\), exact tail:
\[
\int_M^\infty \frac r\delta e^{(G(r)-r^2/2)/\delta}\,dr
\le 4e^{(A_0-M^2/4)/\delta}.
\]
**Coverage/status.** **FULL.** Simple but correct.

### 177 / S199 `L:tube-half-action` (GT558–567, stmt 549–556)
**WORK/PROOF.**  
Finite radial supremum identity equals full Hilbert supremum; avoids \(\infty-\infty\).
**Coverage/status.** **FULL.**

---

## 2. Individual coverage — `integrated_uniform_products.tex` (UP)

### 178 / S204 `L:uniform-E-lift` (UP53–81, stmt 38–51)
**WORK/PROOF.**  
Unique compact-supported distributional multiplier \(M\) in \(\mathcal V_{E,R}\); fixed-\(R\) lift into the old F class; actual symmetric pairing.
**Coverage/status.** **FULL_CONDITIONAL.**  
Depends on signed-static class; uniquely identified.

### 179 / S206 `P:uniform-E-spectral` (UP104–243, stmt 83–102)
**WORK/PROOF.**  
E-only H1 closed form; quarter-power domain; spectral bottom; E wave bound \(8(1+K)^2(1+t)e^{\lambda t}\); real Rayleigh; rate continuity; actual Duhamel/Young identification.
**Coverage/status.** **FULL_CONDITIONAL.**  
Heavy; conditional on Teschl form/PVM imports, rough-multiplier closure, and compact conjugation facts. No \(H^2\) operator-domain assertion.

### 180 / S207 `P:uniform-rate-averaging` (UP269–314, stmt 247–267)
**WORK/PROOF.**  
Finite-net scalar averaging; typed dimension-free tensor extension; completed mean; rate continuity/coercive ceiling.
**Coverage/status.** **FULL_LOCAL_DEDUCTION.**

### 181 / S205 `L:uniform-product-budgets` (UP346–385, stmt 325–344)
**WORK/PROOF.**  
Stopped little-Hölder primitive; key constants \(G_B\le3B\), \(C_B\le18B^{3-1/r}\le32B^{3-1/r}\); generic \(C_{\mathrm{gr}}\); compact mean endpoint norm \(\ge1\).
**Coverage/status.** **FULL_CONDITIONAL.**

### 182 / S208 `P:uniform-mean-product` (UP411–479, stmt 389–409)
**WORK/PROOF.**  
Good/bad full-cell comparison; multiplicative Young; bad cell \(B C_B^r\le32^rB^{3r}\); true last-cell positive exponent; no inverse last length.
**Coverage/status.** **FULL_CONDITIONAL.**

### 183 / S210 `C:uniform-polynomial-balls` (UP494–520, stmt 481–492)
**WORK/PROOF.**  
Every polynomial ball; threshold \(s>r(3+k_{\mathrm{ball}})/(r-\nu)\); both bad powers negative.
**Coverage/status.** **FULL.** Correctly excludes the weak historical \(s>3+k\).

### 184 / S209 `P:uniform-arbitrary-residual` (UP560–611, stmt 524–558)
**WORK/PROOF.**  
Arbitrary compact little-Hölder residuals; exact mean denominator \(\ge1\); \(p\ge\nu\) including equality; ordered noncommuting product; limit order \(\delta\to0\) then \(K_{\mathrm{res}}\to\infty\), then outer \(B\to\infty\).
**Coverage/status.** **FULL_CONDITIONAL.**

---

## 3. Individual coverage — `integrated_point_transfer.tex` (PT)

### 185 / S211 `L:point-actual-finiteness` (PT31–71, stmt 21–29)
**WORK/PROOF.**  
Closed E restriction of F flow; endpoint measurability; fixed-parameter radial finiteness via173/175/176 at \(B=1\); compact norm floor.
**Coverage/status.** **FULL_CONDITIONAL.**

### 186 / S212 `L:point-fast-sources` (PT91–143, stmt 73–89)
**WORK/PROOF.**  
One retaining pullback source; source/residual domination; same \(W\) path limit; ordinary primitive; UI at fixed \(\delta,R,L\); exact \(\delta^a K_\tau(\delta v)=K_{\tau/\delta}(v)\).
**Coverage/status.** **FULL_CONDITIONAL.**

### 187 / S213 `L:point-compact-source` (PT153–216, stmt 145–151)
**WORK/PROOF.**  
Positive-width \(E_k\), \(k>d/2+1\); Leibniz/Picard; measurable continuous displacement/velocity; Green-measure Fubini including d3 sphere.
**Coverage/status.** **FULL_CONDITIONAL.**

### 188 / S214 `P:point-source-cone` (PT235–280, stmt 218–233)
**WORK/PROOF.**  
Total initial-data cancellation on causal cone; same coefficient; \(H M^n t^{2n}/(2n)!\to0\); average of squares.
**Coverage/status.** **FULL_CONDITIONAL.** Observable type explicitly average of squares, not squared average.

### 189 / S215 `P:original-point-transfer` (PT297–370, stmt 282–295)
**WORK/PROOF.**  
Two fixed-\(\delta\) source limits; squared displacement identity; datum cost; scaling law; rate reduction.
**Coverage/status.** **FULL_CONDITIONAL.**

---

## 4. Individual coverage — `integrated_signed_moment_upper.tex` (SU)

### 190 / S216 `L:signed-score-envelope` (SU49–96, stmt 22–47)
**WORK/PROOF.**  
Original signed raw score; finite ceiling \(2+2C_{\mathrm{mean}}^2\); actual \(A_0,A_1,\eta_B\), \(B^{(3\nu)}\) cancellation.
**Coverage/status.** **FULL_LOCAL_DEDUCTION.**

### 191 / S217 `P:signed-moment-bulk-tail` (SU125–166, stmt 98–123)
**WORK/PROOF.**  
Finite deterministic envelope; true bulk/tail; exact \(4e^{A_0+\eta_B b^\nu-M^2/4}\).
**Coverage/status.** **FULL_CONDITIONAL.**

### 192 / S218 `P:signed-operator-upper` (SU178–219, stmt 168–176)
**WORK/PROOF.**  
\(k_{\mathrm{ball}}>3\nu/(2-\nu)\), \(A_1=0\) branch; \(\delta\to0\) at fixed \(B\) then \(B\to\infty\); same \(P_\delta\).
**Coverage/status.** **FULL_CONDITIONAL.**

### 193 / S219 `P:original-signed-point-upper` (SU234–260, stmt 221–232)
**WORK/PROOF.**  
Combines189 and192; negligible data factor; original stationarity; zero covariance direct.
**Coverage/status.** **FULL_CONDITIONAL.**

---

## 5. 25 formal-role coverage table

| Formal ID | Parent proof | Coverage | Reason |
|---|---|---|---|
| S196 | 171 | FULL_LOCAL | closed geometry proven |
| S197 | 174 | FULL_COND | restart/floor inputs named |
| S198 | 176 | FULL | analytic tail |
| S199 | 177 | FULL | half-action identity |
| S200 | 170 | FULL_LOCAL | abstract Wiener realization |
| S201 | 172 | FULL_LOCAL | scalar Rayleigh transfer |
| S202 | 173 | FULL_COND | actual law/compactness/anchor |
| S203 | 175 | FULL_LOCAL | coarse envelope |
| S204 | 178 | FULL_COND | E multiplier closure/lift |
| S205 | 181 | FULL_COND | primitive/growth budgets |
| S206 | 179 | FULL_COND | spectral wave/rate |
| S207 | 180 | FULL_LOCAL | finite-net averaging |
| S208 | 182 | FULL_COND | mean-product bounds |
| S209 | 184 | FULL_COND | arbitrary residual |
| S210 | 183 | FULL | polynomial-ball threshold |
| S211 | 185 | FULL_COND | actual finiteness |
| S212 | 186 | FULL_COND | fast sources |
| S213 | 187 | FULL_COND | compact source regularity |
| S214 | 188 | FULL_COND | source cone/average of squares |
| S215 | 189 | FULL_COND | original point transfer |
| S216 | 190 | FULL_LOCAL | signed score envelope |
| S217 | 191 | FULL_COND | bulk/tail |
| S218 | 192 | FULL_COND | operator upper |
| S219 | 193 | FULL_COND | original signed point upper |
| S064 | context | LOGICAL_GIVEN_WHERE_USED | standalone domains retained |

---

## 6. Three complete canonical joins — assessment

### JOIN-UNIFORM-E-SIGNED
**Worked path.** 178/179 establish the E-mean/spectral multiplier closure; 180–184 establish uniform-R E-only mean/product/rate estimates and arbitrary residual comparison; 190–193 carry the signed score through the Gaussian tube.
**Actual outside/consumer clauses used.** F153 scalar tensor norm; F-youth 149/150; E/Gaussian-tube AWS; fixed-\(Q\) radius anchor; Teschl form/PVM imports after own hypotheses.
**Pending/unresolved clause.** Full quantitative spectral/domain proofs outside UP are upstream OWN; no literal rough \(\Phi_s\) potential is used; fixed-\(R\) F-lift constants must not enter uniform E budgets.
**Verdict.** **MEDIUM — genuine, conditional.**

### JOIN-SYMPLECTIC-TUBE
**Worked path.** OWN107 → compact Young; OWN165 whole-space translations/weak-null + velocity reversal gives endpoint/finite product norm \(\ge\) free norm. Real E coefficients and closed J-skew path give direct Young conservation in168; inverse from107. Gaussian eigenvalues/tubes from170–174 remain separate.
**Actual outside clauses.** 165’s compact norm floor is not conservation; 168 is real Lie/conservation, not compactness; 169 scales are not supplied by165/168.
**Pending/unresolved clause.** Arbitrary compression/complex coefficients invalid; no independent block costs.
**Verdict.** **MEDIUM — structural, conditional.**

### JOIN-POINT-UPPER
**Worked path.** 188/189 exact source cone and average-of-squares identity; 185–187 actual finiteness/sources/regularity; 190–193 operator upper with global raw score.
**Actual outside clauses.** D_SOURCE same-W retaining source; D_CODE exact scaling; F-radius; tube/tail; no uniform growing-R compactness or independence.
**Pending/unresolved clause.** Positive/occupation matching \(C_2\) is downstream, not this G join.
**Verdict.** **MEDIUM — genuine, conditional.**

---

## 7. Consumer seams status

| Seam | G consumer | Audit finding |
|---|---|---|
| C_RAW | 170/173–176/185–187 | Application-matched: real first-chaos path, both variance/adjoint/localization/Gaussian bounds. Full parent not re-proved. |
| D_SOURCE | 174/186–189 | Joint retaining source, heatSUM/timeMAX, ordinary primitive, source UI. Full parent conditional. |
| D_F_YOUNG | 174/178/179/185–189 | Closed E/F, LEFT Young estimate/inverse, compact base. No flawed E-density or operator-norm free derivative. |
| E_CLOCK | 173/174/186/189/193 | raw isometries/Jacobians; same-source restart124, law121, canonical stationarity. |
| A_CONSTRUCTOR | 186–189/193 | fixed-order/Green-first joint limits; summable series; physical designation. No generic L2 factor shortcut. |
| B_E_FINANCE | F mean before 170/173/178–180/190 | SAME-canonical051 finances finite E132 scores; smooth R0→Rsp. Not funded by193/204. |
| F_MEAN/RADIUS/YOUNG_FORM/STRUCTURE | various | supported tensor/CM, fixed-even-Q anchor, real multiplier closure/spectral form, compact norm floor and real conservation. |

**Overall seam verdict:** no discovered seam gap; all are conditional on upstream OWN work and must not be accepted laborlessly.

---

## 8. Findings and limitations

1. **Per-item integrity is generally good** for the audited G source text; no concrete algebraic/domain/limit order defect was identified inside the four modules under their stated hypotheses.
2. **Main limitation:** this audit did **not** re-derive full upstream owner inputs (C/D/E/F/B and earlier units). Some G proofs are heavy and were marked `FULL_COND` rather than `FULL`.
3. **Main limitation:** the G upper/point reduction does **not** prove H positive matching, actual \(C_2\), Chen energy identification or all13 joins.
4. **Main limitation:** no independent numerical/computer verification; all checks are source/analytic reading.
5. **No H199–213 theorem was used as a G premise** in the audited text.

**Unforced verdict.**  
The G24 deductions are **individually plausible and largely complete conditional on named inputs**; the complete three-join, all-model actual \(C_2\) closure remains **not accepted** by this audit. Confidence **MEDIUM** in the G24 local deductions; **LOW-MEDIUM** in the full closure.