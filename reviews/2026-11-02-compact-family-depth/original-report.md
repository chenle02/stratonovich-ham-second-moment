{
  "category": "paper-review-deepseek",
  "model": "deepseek/deepseek-v4-pro",
  "verdict": "PASS_WITH_NOTES",
  "confidence": "high",
  "confidence_justification": "All seven local deductions were reconstructed from the embedded bodies and their algebra was independently re-checked, including the exact growing-response subtraction, the rate-gap denominator direction, the square-root FORM-to-quarter-power passage, the negative-branch spectral entries at threshold mu=0, the raw-covariance floor and mask trial scaling, and every item of the finite-controls file. The Teschl theorem bodies actually supplied match the hypotheses actually cited (Thm 10.2, conditional Thm 10.13, Thm 4.12/Cor 4.13), and the conditional positive-ground step is applied only after the trial puts the bottom below the essential threshold. No fatal or material defect was found in the seven deductions or their stated joins. Confidence is high for these seven local deductions; notes record only the bounded-scope reading limits (downstream modules consumed as named local inputs; imported theorem proofs not re-derived).",
  "source_coverage": [
    "PROOF112-PROOF118 statement/proof bodies and the full module notes/integrated_compact_mean_family.tex: read and rederived",
    "supplements/compact-family-worked-calculations.txt: read and re-checked as author calculations (not premises)",
    "supplements/finite-controls.txt: read and recomputed",
    "primary/teschl-2014-selected.txt (Thm 2.13/2.14 pp.92-93, Thm 3.1/3.2/3.6 pp.114-121, Thm 4.12/Cor 4.13 pp.152-153, Thm 10.2 p.270, Thm 10.13 p.285): read as exact imported statement bodies",
    "primary/friz-hairer-selected.txt (Young estimate pp.13, 61-62; Borell p.190-191): read for context",
    "notes/integrated_constant_phase_young.tex (P:constant-phase-driver, L:constant-source-response, P:constant-young-linear, P:constant-gaussian-flow, L:constant-source-solution, P:constant-raw-average, P:constant-compact-base): read as named local inputs for the g=0 ordinary F-flow join",
    "notes/integrated_source_convergence.tex and notes/integrated_masked_moments.tex: read for the source/ordinary-response and masked-moment application joins",
    "notes/integrated_raw_block_lower.tex and notes/integrated_unmasked_variational.tex: read for the raw-control common-trial and variance-half application joins (not re-proved in this bounded task)",
    "maps/targets.json, maps/proof-index.tsv, primary/source-editions.json, scope.txt, report-contract.json: read for locator/scope identification"
  ],
  "checks": [
    {
      "claim": "CF112 PROOF112 P:compact-ground-family",
      "verdict": "PASS",
      "reason": "H2 is a form core and the H1 form domain is correctly identified via the equivalent A_sigma^{1/2} norm dominating L2. The common trial plus form max-min gives -M <= E1 <= -eps; since ess threshold is 0 (Thm 10.2 applied to -V_sigma, compact smooth hence in L2 for d<=3), the bottom is an isolated eigenvalue below it, and only then is conditional Thm 10.13 used for simplicity/positiveness. E2 is the max-min second level or the threshold zero, giving E1<E2<=0; energy continuity |E_j(sigma)-E_j(tau)| <= ||V_sigma-V_tau||_infty passes through the same infima/suprema. The gap uses (E2-E1)/(lambda+mu) with the correct upper denominator lambda+mu<=2sqrt(M) (not the reverse), so lambda-mu >= Delta_*/(2sqrt M)>0 and no division by mu occurs. Ground-state L2 continuity via p_tau = a p_sigma + r with the cross form term vanishing is correct (||p_tau-p_sigma||_2^2 = 2(1-a) <= 2(1-a^2) <= 4dV/Delta_*), and B^{-1}:L2->H2 turns the eigen-equation into the asserted H2 continuity and uniform bound."
    },
    {
      "claim": "CF113 PROOF113 L:compact-fractional-phase",
      "verdict": "PASS",
      "reason": "The resolvent variational formula, the I-t(T+t)^{-1} order, and the sqrt(x)=pi^{-1}integral t^{-1/2} x/(x+t)dt identity are correct; positive Tonelli gives T^{1/2}<=S^{1/2} as forms (Loevner-Heinz at exponent 1/2). Applying this once more to the square roots yields the genuine quarter-power comparison B^{1/4}<=A_sigma^{1/4}<=c^{1/4}B^{1/4} without squaring a noncommuting operator inequality, so the quarter-power domain is H^{1/2}. The dual norm is ||A_sigma^{-1/4}z|| with attainability by A_sigma^{-1/2}z on L2, and the negative entry is correctly identified as the COMPLETION in that weaker norm, not the L2 domain of the bounded inverse quarter. Uniform equivalence to E=H^{1/2}xH^{-1/2} follows with c-dependent constants."
    },
    {
      "claim": "CF114 PROOF114 P:compact-E-wave",
      "verdict": "PASS",
      "reason": "All weighted spectral entries are checked: for h>=0 |S_t|<=min(t,h^{-1/2}) with the split at h=1; for -mu^2<=h<0 the entries are bounded by C(1+t)e^{mu t} (the negative branch cannot be polynomial for unbounded t); h=0 uses the removable sine-quotient value t. The spatial complement projects out only the growing branch; the decaying branch e^{-lambda t} stays in I-Pi_sigma^E and both ground-branch projections are uniformly bounded using sqrt(eps)<=lambda<=sqrt(M). The resulting E-complement bound C(1+t)e^{mu t} is uniform in sigma. Identification of the spectral matrix with the actual ordinary E flow goes through H2xH1 graph coordinates, Duhamel for compact smooth data, and Picard uniqueness/density inside E; strong free-group continuity is used, not operator-norm differentiability of the free flow, and no density of E in F is claimed."
    },
    {
      "claim": "CF115 PROOF115 P:compact-F-projection",
      "verdict": "PASS",
      "reason": "The full-phase block P_sigma(t)(e,c)=(P_sigma^E(t)e+int_0^t P_sigma^E(t-r)D_sigma C(r)c dr, C(t)c) is justified by strong E-valued Fubini on the bounded finite triangle plus ordinary-flow uniqueness; the force D_sigma(c1,c2)=(0,V_sigma c1) lies in iE. f_sigma=int V_sigma p_sigma/(2 lambda_sigma)>0 is finite by L2 Cauchy-Schwarz and strictly positive because V_sigma is nonzero and p_sigma>0 a.e.; no p_sigma in L1 is used. The direct identities ell_sigma^E D_sigma C(r)c=f_sigma(c1+r c2), ell_sigma^C(c)=int_0^infty e^{-lambda r} f_sigma(c1+r c2)dr, and ell_sigma^C(C(t)c)=int_t^infty e^{lambda(t-r)}(...)dr combine to ell_sigma P_sigma(t)=e^{lambda t} ell_sigma and P_sigma(t)e_sigma=e^{lambda t}e_sigma with ell_sigma(e_sigma)=1, retaining BOTH constant-response columns. Positive margins inf ell_sigma(e0)=f/lambda>0 and inf O_phi(e_sigma)=int phi p_sigma>0 hold by compactness/continuity."
    },
    {
      "claim": "CF116 PROOF116 P:compact-F-complement",
      "verdict": "PASS",
      "reason": "Decomposing D_sigma=(Pi_sigma^E+Q_sigma^E)D_sigma and subtracting the growing projection gives the exact E component P_sigma^E(t)Q_sigma^E e + int_0^t P_sigma^E(t-r)Q_sigma^E D_sigma C(r)c dr - e_sigma^E ell_sigma^C(C(t)c), with constant component C(t)c. The subtraction is necessary and exactly removes the growing response to constants; the pure-velocity check gives int_0^t e^{t-r} r dr = e^t-(t+1), and removing the full growing projection leaves the purely polynomial -(t+1). The integral int_0^t(1+t-r)(1+r)dr=t+t^2+t^3/6<=C(1+t)^3 supplies the full-F complement bound, and (1+t)^3 e^{-(d0-eta)t} is bounded for every eta<d0, covering mu=0. Parameter-flow control is correctly restricted to fixed finite horizon by scalar Gronwall with operator-norm measurability via separability; no B(F)-valued derivative or operator-norm free-group continuity is assumed."
    },
    {
      "claim": "CF117 PROOF117 L:compact-raw-profile",
      "verdict": "PASS",
      "reason": "The raw mean/covariance identities E[W(Psi)W(F0)]=int F0 h_s dx ds and E[W(Psi)W(Psi)]=int Psi h_s dx dsigma follow from absolute Fubini over compact supports, local Radon mass and a<1. Finiteness uses ||Psi||_inf^2|B_A|Gamma(bar B_{2A}) and int_0^1int_0^1|sigma-u|^{-a} du dsigma = 2/((1-a)(2-a)). The floor h_sigma>=Gamma*qbar (since |sigma-u|^{-a}>=1) and v_Psi>=Q(qbar)>0 are correct; Q(qbar)>0 uses positivity of the smooth compact autocorrelation near zero and positivity of every origin-centered ball under homogeneity. Smoothness of h on compacts follows by writing the time convolution with |r|^{-a} and differentiating only the smooth test, dominated since |r|^{-a} is locally integrable. The masked family V_sigma=m_R h_sigma is a smooth compact family, Lipschitz in sigma in L^infty and L2 at fixed R."
    },
    {
      "claim": "CF118 PROOF118 P:compact-original-common-trial",
      "verdict": "PASS",
      "reason": "The plateau trial psi_L=L^{-d/2}psi(x/L) with psi>=c0>0 on B1, support in B2, and mask R>=2L gives, by positive Tonelli and B_{L/2} subset B_L-y for |y|<=A, L>=2A: int V_sigma psi_L^2 >= c0^2 L^{-d} Gamma(B_{L/2}) int qbar = C_Gamma L^{-alpha} with C_Gamma=c0^2 2^{alpha-d}Gamma(B1)int qbar>0, while ||nabla psi_L||_2^2=D_psi L^{-2}. Since alpha<2 this gives a uniform negative margin eps_R for every sigma in I. The rate is then Lipschitz on I with floor sqrt(eps_R), and lambda_0>0 because the mean integrates the whole time test even though Psi(0,.)=0. The raw test Psi, variable Z and variance v_Psi are fixed before the mask grows; enlarging R only covers extra fixed compact supports. The statement is scoped as one common trial for this masked family, not an all-strength binding assertion for every weak fixed compact potential in d=2,3."
    },
    {
      "claim": "APP-GROUND-PHASE",
      "verdict": "PASS",
      "reason": "The join of PROOF112/113/114 is coherent: the negative common trial is verified as an isolated negative bottom below the essential threshold before invoking the conditional positive-ground Theorem 10.13; the form-domain, energy-level, uniformity and fractional-norm inputs are exactly those consumed by the complementary E-wave estimate; ground-state H2 continuity and uniform bounds supply the vector/dual continuity used later. Fixed-family constants remain distinct from any global control/radius bound."
    },
    {
      "claim": "APP-FULL-F",
      "verdict": "PASS",
      "reason": "The join of PROOF115/116 is coherent: the actual ordinary physical F-flow block is specialized from P:constant-compact-base with h=V_sigma and g=0; both constant-response columns enter through D_sigma C(r)c; the exact growing-response subtraction is performed and the resulting polynomial (including the constant-velocity column) is absorbed by the all-time normalized complement estimate. The variation-of-constants and Gronwall steps use strong continuity and fixed-horizon bounds without an operator-norm derivative."
    },
    {
      "claim": "APP-RAW-CONTROL",
      "verdict": "PASS",
      "reason": "The join of PROOF117/118 preserves the original d=1,2,3 homogeneous covariance scope, nonseparable nonnegative controls, the raw covariance amplitude, and the variance-half Gaussian action v_Psi/2. The common negative trial is established only after the raw covariance mean is fixed, and no uniform supremum over controls precedes the individual masked-family bounds. The explicit 'not all-strength binding' scope and 'masks fixed before asymptotics' notes are respected."
    },
    {
      "claim": "FINITE",
      "verdict": "PASS",
      "reason": "All finite controls recompute consistently: (1) B-A=[[1,1],[1,1]] is PSD while B^2-A^2=[[6,5],[5,4]] has negative determinant, confirming that square-root FORM order rather than squaring an operator inequality is required for the quarter-power norm; (2) lambda-mu=(E2-E1)/(lambda+mu) holds at (-1,0,1) and (-4,-3,4) and the positive lower gap requires the upper denominator bound, with mu=0 handled without division; (3) at h=-1/4,c=2 the entries grow exponentially (no all-time polynomial bound), while h=0 gives the removable sine-quotient values; (4) with lambda=f=1 and pure c2 velocity, int_0^t e^{t-r} r dr = e^t-(t+1) and subtracting the full growing projection leaves the polynomial -(t+1), requiring the velocity column; (5) sup_{t>=0}(1+t)^3 e^{-bt} equals 1 at b=4 and (3/b)^3 e^{b-3} at b=1/2; (6) for the d=3 line covariance (alpha=1) Gamma(B_L)=Gamma(B1)L^2 gives L^{-3}Gamma(B_{L/2})=C_Gamma L^{-1} consistent with the stated C_Gamma, potential power L^{-1} versus kinetic L^{-2}, and origin-ball positivity does not imply positivity of translated balls; (7) a continuous sigma-family need only be continuous while the quantitative controls are Lipschitz in the potential distance dV, with sigma-Lipschitz holding only for the smooth masked raw family of 117/118."
    }
  ],
  "findings": {
    "fatal": [],
    "major": [],
    "minor": [
      "Imported Teschl theorem proofs (10.2, 10.13, 4.12/4.13) were read as statement bodies and their hypotheses were checked, but their internal proofs were not re-derived.",
      "Downstream modules (raw-block lower, Gaussian tubes, uniform-mean regulation, point transfer, intrinsic-constant, occupation ceiling) were read for the joins but were not fully re-derived in this bounded task, consistent with the supplied scope.",
      "The Riesz-resolvent rank-one projection Lipschitz control in the worked calculations is supplementary replay evidence; PROOF112 itself asserts only continuity for a generic continuous sigma-family, with sigma-Lipschitz limited to the smooth masked raw family in PROOF117/118."
    ]
  },
  "required_repairs": [],
  "limitations": [
    "No tools, search, execution, delegation, image rendering, or whole-paper/final-cold clearance were used.",
    "No re-proof of all 214 paper arguments was performed or required; only PROOF112-PROOF118 and their stated application joins were reconstructed.",
    "Author calculations were checked, not assumed, but upstream named local inputs (driver construction, source convergence, Young evolution, masked moments) were consumed only after checking their type/hypotheses at the join surface, not independently re-derived line-by-line here.",
    "The verdict concerns the seven compact-family local deductions and their stated joins; it does not certify downstream sharpness, full variational identification, or preceding route/gate arguments."
  ]
}