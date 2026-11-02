# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. The five foundational proofs reconstruct correctly under the stated hypotheses. All Fourier constants, signs, scaling exponents, Schur constants, and the rawness obstruction check out by hand. No hidden density, isotropy, or nonzero-noise assumption is silently imported; the anisotropic non-density case and the zero-covariance case behave as claimed. The "physical mask is not a bounded map on the raw quotient" conclusion is genuinely established and is not confused with the auxiliary completion.

## Noncritical findings

1. PROOF061 (P:masked-spectral-growth) states "Then $0<M_\Gamma<\infty$" without restating the section-wide premise $\Gamma\neq0$. For the zero covariance $\Gamma=0=\mu$ one has $M_\Gamma=0$, violating that line, but the section preamble (packet line 8) explicitly excludes $\Gamma=0$ and packet lines 9–10 handle it separately; the translated-ball and Gaussian bounds then hold trivially. This is a documentation-level nit, not a mathematical error.
2. PROOF064's admission of $\mathcal D$ into the "original test-noise completion" (packet lines 234–237) is compressed ("smooth expanding cutoffs converge in the Schwartz topology; the spectral form is continuous in that topology"). Reconstructed explicitly it is valid: the spatial bilinear form $C(f,g)=(2\pi)^d\int \widehat f\,\overline{\widehat g}\,d\mu$ is continuous in Schwartz seminorms by temperedness of $\mu$, and compact-support cutoff sequences converge in that topology, giving a unique completion extension without changing the probability space. No change is needed; the text is just terse.
3. PROOF062's finite-dimensional/zero-space reduction and the projection argument (lines 127–134) assume $H$ separable, which is stated in the proposition. The zero space is genuinely immediate (all terms vanish).

## Checked derivations

**PROOF061 — P:masked-spectral-growth (statement lines 37–55; proof lines 57–82).**

- $J(b)=\int_\mathbb{R}e^{-Ax^2}e^{ibx}dx$: $J(0)=\sqrt{\pi/A}$; $J'(b)=-(b/(2A))J(b)$ by integration by parts ($\partial_x e^{-Ax^2}=-2Ax e^{-Ax^2}$); hence $J(b)=\sqrt{\pi/A}\,e^{-b^2/(4A)}$.
- Product over coordinates with $A=r^2/4$, $b=\xi_k-y_k$: $\int e^{-r^2|x|^2/4}e^{i(\xi-y)\cdot x}dx=(2\sqrt\pi/r)^d e^{-|\xi-y|^2/r^2}$. Constant correct with the unitarily normalized $c_d$ because the pairing convention (E:masked-spectral-convention) integrates $e^{+i\xi\cdot x}$ without normalization.
- Applying the convention to the single Schwartz test $e^{-r^2|x|^2/4}e^{-iy\cdot x}$ yields exactly $\int e^{-|\xi-y|^2/r^2}\mu(d\xi)=(r/(2\sqrt\pi))^d\int e^{-r^2|x|^2/4}e^{-iy\cdot x}\Gamma(dx)$.
- Homogeneity pushforward $x\mapsto rx$: $\Gamma(r^{-1}A)=r^{\alpha-d}\Gamma(A)$ by $\Gamma(cA)=c^{d-\alpha}\Gamma(A)$ with $c=r^{-1}$; hence $\int e^{-r^2|x|^2/4}\Gamma(dx)=r^{\alpha-d}M_\Gamma$.
- Gaussian bound $\le (r/(2\sqrt\pi))^d r^{\alpha-d}M_\Gamma = r^\alpha M_\Gamma/(2\sqrt\pi)^d$; the absolute-value step is valid (and even equality) because $\Gamma\ge0$.
- Ball bound: $e^{-|\xi-y|^2/r^2}\ge e^{-1}$ on either open or closed $B(y,r)$, so $\mu(B(y,r))\le e\,r^\alpha M_\Gamma/(2\sqrt\pi)^d = C_\Gamma r^\alpha$ with $C_\Gamma=eM_\Gamma/(2\sqrt\pi)^d$. Constant and $r^\alpha$ exponent correct.
- **Status: CHECKED.**

Calibration: $d{=}1$ white $\Gamma=\delta_0$, $\alpha=1$, $M_\Gamma=1$, $\mu=(2\pi)^{-1}d\xi$, $\int e^{-|\xi-y|^2/r^2}\mu = r/(2\sqrt\pi)$, $\mu(B(y,r))=r/\pi\le C_\Gamma r=(e/(2\sqrt\pi))r$. Correct.

**PROOF062 — P:masked-auxiliary-norm (statement lines 93–106; proof lines 108–144).**

- $k_R(u)=R^d\widehat\zeta(Ru)$, $\|k_R\|_1=\|\widehat\zeta\|_1=L>0$. Correct by unitary Fourier scaling.
- $\rho_R(\eta)=c_d^2L\int|k_R(\xi-\eta)|\mu(d\xi)$: finiteness at each $\eta$ and on compact $\eta$-sets follows from $|k_R(\xi-\eta)|\lesssim(1+|\xi-\eta|)^{-N}\lesssim(1+|\xi|)^{-N}$, integrable against the polynomially-grown tempered $\mu$; dominated convergence gives continuity; $\nu_R=\rho_R d\eta$ is Radon.
- Evenness: $k_R(-u)=\overline{k_R(u)}$ ($\zeta$ real) plus $\mu$ even gives $\rho_R(-\eta)=\rho_R(\eta)$.
- Tonelli translated mass: $\nu_R(B(y,r))=c_d^2L\int|k_R(u)|\,\mu(B(y+u,r))\,du$ (change $u=\xi-\eta$; determinant 1). Then $\le c_d^2L\cdot C_\Gamma r^\alpha\cdot L$, uniform in $R$.
- Bochner identity $\widehat{\zeta_RF}(\xi)=c_d\int k_R(\xi-\eta)\widehat F(\eta)d\eta$: verified via $\zeta_R(x)=c_d\int e^{i\eta x}k_R(\eta)d\eta$, giving the $c_d$ factor (no $c_d^2$). Scalar → finite-rank → separable projections by dominated convergence; the Schwartz bounds on $F$ dominate the Fourier integrals.
- Weighted Cauchy–Schwarz: $\|\widehat{\zeta_RF}\|_H^2\le c_d^2L\int|k_R(\xi-\eta)|\|\widehat F(\eta)\|_H^2d\eta$. Tonelli against $\mu$ yields exactly $\int\|\widehat F\|_H^2\nu_R(d\eta)$.
- **Status: CHECKED.**

**PROOF063 — L:masked-time-completion (statement lines 148–163; proof lines 165–189).**

- $|t-s|^{-a}=\frac1{\Gamma_E(a)}\int_0^\infty\lambda^{a-1}e^{-\lambda|t-s|}d\lambda$: correct Gamma substitution.
- $e^{-\lambda|t-s|}=\int_{-\infty}^{\min(t,s)}2\lambda e^{-\lambda(t-u)}e^{-\lambda(s-u)}du$: verified directly (substitute $v=t+s-2u$).
- PSD: for each $\lambda$ the double form is $\int 2\lambda\big(\int_{u<t}f(t)e^{-\lambda(t-u)}dt\big)^2du\ge0$; integrating against $\lambda^{a-1}d\lambda\ge0$ preserves PSD. Exchanges are absolutely integrable for compact smooth tests.
- Row bound $\int_0^T|t-s|^{-a}ds\le 2T^{1-a}/(1-a)$; Schur gives $\|f\|_a^2\le(2T^{1-a}/(1-a))\|f\|_2^2$ — constant correct.
- Separability: $L^2$-density of compact smooth functions transfers to $H_a$ by the Schur bound.
- Complexification: norm is $\iint f(t)\overline{f(s)}|t-s|^{-a}$; imaginary cross term vanishes by kernel symmetry; same Schur bound holds.
- $L^2$ extension and bounded-measurable interval amplitudes: valid.
- **Status: CHECKED.**

**PROOF064 — P:masked-noise-completion (statement lines 197–215; proof lines 217–257).**

- $h(z)=\int f(y+z)g(y)dy$ and $h(z)=\int e^{i\xi\cdot z}\widehat f(\xi)\overline{\widehat g(\xi)}d\xi$: checked carefully; with $\widehat f=c_d\int e^{-i\xi x}f$, one gets $\widehat h = \widehat f\,\overline{\widehat g}/c_d$, and inversion supplies exactly $h=\int e^{i\xi z}\widehat f\overline{\widehat g}d\xi$ (the $c_d$'s cancel; the text's displayed formula is correct, not missing a $c_d$).
- Then $\int e^{i\xi\cdot z}h(z)dz=(2\pi)^d\widehat f(-\xi)\overline{\widehat g(-\xi)}$; reflecting $\xi$ (using $\widehat f(-\xi)=\overline{\widehat f(\xi)}$, $\widehat g(-\xi)=\overline{\widehat g(\xi)}$, $\mu$ even) gives spatial covariance $(2\pi)^d\int\widehat f(\xi)\overline{\widehat g(\xi)}\mu(d\xi)$. This agrees with the direct Fubini computation $C(f,g)=(2\pi)^d\int\overline{\widehat f(\xi)}\widehat g(\xi)\mu(d\xi)$ (complex conjugate; real and equal by evenness). Constant $(2\pi)^d$ correct.
- Summing temporal factors and using the $H_a^\mathbb{C}$ inner product gives $E\,W(F)^2=(2\pi)^d\int\|\widehat F(\xi)\|^2_{H_a^\mathbb{C}}\mu(d\xi)$.
- Applying P:masked-auxiliary-norm with $H=H_a^\mathbb{C}$ gives $E\,W(\zeta_RF)^2\le N_R(F)^2$; null-space annihilation and Cauchy-sequence transfer yield the contraction; uniqueness by density.
- Joint Gaussianity: finite linear images are $L^2$ limits of centered Gaussians with convergent variances.
- PSD covariance comparison: $b^{\mathsf T}Ab\le b^{\mathsf T}Bb$; $B-A$ diagonalizes to an independent centered Gaussian $Z$ with $X+Z\sim N(0,B)$; conditional Jensen on $\|\cdot\|^p$ ($p\ge1$) gives $E\|X\|^p\le E\|X+Z\|^p$. Correct.
- **Status: CHECKED.**

**PROOF065 — P:masked-quotient-obstruction (statement lines 267–273; proof lines 275–306).**

- Admissibility of $\Gamma=\delta_0(dx_1)dx_2$, $d=2$, $\alpha=1$: $\Gamma(cA)=c\,\Gamma(A)$ (Dirac in $x_1$ is scale-neutral, Lebesgue in $x_2$ scales by $c$), so $d-\alpha=1$; nonnegative, even, positive definite, tempered. Spectral measure $\mu=(2\pi)^{-1}d\xi_1\delta_0(d\xi_2)$: verified, since $\int e^{i\xi_1x_1}(2\pi)^{-1}d\xi_1=\delta(x_1)$.
- Spatial variance $V(g)=\int_\mathbb{R}\big(\int_\mathbb{R}g(x_1,x_2)dx_2\big)^2dx_1$ by ordinary Fubini: correct.
- Bump function $\chi$: the displayed formula $e^{-1/(2-r)}/(e^{-1/(2-r)}+e^{-1/(r-1)})$ equals $1$ at $r\to1^+$ and $0$ at $r\to2^-$ with flat endpoints, so the plateau pastes to $C_c^\infty$; $I_\chi=\int(\chi')^2>0$, $J_\chi=\int\chi^4\ge2$.
- $g=\chi(x_1)\chi''(x_2)$, $\zeta=\chi(x_1)\chi(x_2)$: unmasked marginal $\chi(x_1)\int\chi''=0$; masked marginal $\chi(x_1)^2\int\chi\chi''=-\chi(x_1)^2 I_\chi$; hence $V(g)=0$ and $V(\zeta g)=I_\chi^2 J_\chi>0$.
- Temporal factor: $F=\tau g$ with $0\le\tau\in C_c^\infty(0,T)$, $\tau\ne0$ gives $E\,W(F)^2=\|\tau\|_a^2 V(g)=0$ and $E\,W(\zeta F)^2=\|\tau\|_a^2 V(\zeta g)>0$, with $0<\|\tau\|_a^2<+\infty$. Therefore the quotient boundedness inequality fails for every finite $C$. Correct, and it disproves bounded masking on the **raw** quotient (a raw-null test whose mask is not raw-null), exactly as scoped.
- **Status: CHECKED.**

## Required fixes before production gate

- None required for mathematical correctness of PROOF061–PROOF065.
- Optional (non-blocking) text clarification: in PROOF061, add "$(\Gamma\ne0)$" or "under the standing assumption $\Gamma\ne0$" next to "$0<M_\Gamma<\infty$" so the zero-covariance case is not read as contradicted. This is already resolved by the section preamble.

## COV01–COV08

**COV01 (PROOF061 P:masked-spectral-growth) — PASS.** Proof-level status: CHECKED. Temperedness finiteness, single-test pairing, exact Gaussian constant $(2\sqrt\pi/r)^d$ and $C_\Gamma=eM_\Gamma/(2\sqrt\pi)^d$, homogeneity pushforward $r^{\alpha-d}$, absolute-phase bound, open/closed ball bound all verified.

**COV02 (PROOF062 P:masked-auxiliary-norm) — PASS.** Proof-level status: CHECKED. Tonelli translated mass, $k_R(-u)=\overline{k_R(u)}$, evenness, Radon/temperedness, $c_d^2L$ Cauchy–Schwarz, exact $\nu_R(B)\le c_d^2L^2C_\Gamma r^\alpha$, no invented uniform density bound.

**COV03 (PROOF063 L:masked-time-completion) — PASS.** Proof-level status: CHECKED. Gamma/Laplace representation, exponential feature (constant $2\lambda$), Schur $2T^{1-a}/(1-a)$, separability, complex conjugation cancellation, $L^2$/interval-amplitude inclusion all correct.

**COV04 (PROOF064 P:masked-noise-completion) — PASS.** Proof-level status: CHECKED. Exact $(2\pi)^d$ same-noise factor and signs, test inclusion via cutoffs without enlarging the probability space, contraction from the auxiliary null quotient, Gaussian limits, PSD finite comparison + independent Gaussian completion + conditional Jensen for $p\ge1$; no nonlinear/global quotient claim made.

**COV05 (PROOF065 P:masked-quotient-obstruction) — PASS.** Proof-level status: CHECKED. Admissible anisotropic (non-density, hyperplane) covariance, exact $\mu=(2\pi)^{-1}d\xi_1\delta_0(d\xi_2)$, marginal and integration-by-parts computations, strictly positive finite temporal factor, genuine raw-quotient obstruction (not auxiliary).

**COV06 (input/application boundaries) — PASS.** Uses of the five results in the wave/driver/source consumers match: P:masked-auxiliary-norm supplies $C_\nu=c_d^2L_\zeta^2C_\Gamma$ and the ball growth used by P:frequency-row; P:masked-noise-completion supplies the actual-noise spectral identity and the auxiliary contraction; L:masked-time-completion supplies $H_a$ norms/Schur/Laplace factorization in the driver and source isometries. Constants and class claims agree. I did not certify the downstream wave/driver/source proofs wholesale (not assigned), only that these five results are not silently overextended. No overextension found.

**COV07 (by-hand falsification/calibration) — PASS.** $d{=}1$ white ($\mu=(2\pi)^{-1}d\xi$, $\alpha=1$, constants above) and zero covariance confirmed. Anisotropic non-density/hyperplane example is exactly PROOF065. Signs (spatial covariance real conjugate pair, $\int\chi\chi''=-I_\chi$) and Fourier constants recomputed; translated-ball and quotient non-boundedness claims hold; no forbidden stronger variant is asserted.

**COV08 (completeness/non-circularity/scope) — PASS.** All five proofs reconstructed only from elementary Fourier/measure/Hilbert/Gaussian facts with explicit dependency order (061 → 062 → 064, with 063 independent temporal). No prior-review premise, no assumed density/isotropy, no arbitrary covariance monotonicity, no zero-noise exclusion smuggled in (zero covariance is only excluded within PROOF061's positivity clause, outside its quantitative bounds), no hidden source-normalization repair. Whole-paper 213-proof/all-model/global/image/cold obligations remain open and are not claimed here.

## One-line summary

PROOF061–PROOF065 are mathematically valid under the stated anisotropic tempered-measure model: all Fourier constants, exponents, Schur constants, and signs check out by hand, the mask-null obstruction genuinely disproves bounded masking on the raw quotient, and the contract's eight checks (COV01–COV08) all pass.