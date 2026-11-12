
# notes/integrated_wave_variance.tex

\section{Frequency estimates and both wave variance directions}
\label{S:wave-variance}

We now apply the covariance and temporal estimates of
Section~\ref{S:masked-covariance} to the full wave phase. We retain
Hypothesis~\ref{H:homog}, write $a = \alpha_0$, and choose and fix
\begin{equation}\label{E:variance-gamma-range}
  0 < \gamma < \min\left(\frac12,\frac{2-\alpha}{2}\right).
\end{equation}
The interval is nonempty because $\alpha+a < 2$. We use $\langle\xi\rangle =
\sqrt{1+|\xi|^2}$ and set
\begin{equation}\label{E:variance-scale-profile}
  B_\alpha(h) =
  \begin{cases}
    1, & \alpha < 1,\\
    1+\log(1/h), & \alpha = 1,\\
    h^{1-\alpha}, & \alpha > 1,
  \end{cases}
  \qquad 0 < h \le 1.
\end{equation}

\subsection{A scalar row estimate for a measure}

Let $\nu$ be a positive Radon measure satisfying
\begin{equation}\label{E:frequency-translated-growth}
  \nu(B(y,r)) \le C r^\alpha,
  \qquad y \in \R^d,\quad r > 0,
\end{equation}
where $C \ge 0$. If the estimate is initially known for open balls, apply it at
radius $r+\epsilon$ and let $\epsilon \downarrow 0$ to obtain the closed-ball
estimate. Neither evenness nor a density is assumed here.
Using~\eqref{E:masked-frequency-pair}, define
\begin{align}
  \Phi_h(\xi,\eta)
  &:= \frac{\mathcal{Q}_h(|\xi|,|\eta|)}
  {\langle\xi\rangle\langle\eta\rangle},
  \label{E:frequency-row-kernel}\\
  J_h(\xi)
  &:= \langle\xi\rangle^{2\gamma}
  \int_{\R^d}\Phi_h(\xi,\xi-\lambda)\nu(\ud\lambda).
  \label{E:frequency-row-integral}
\end{align}
These are initially nonnegative extended integrals. In particular, the notation
denotes a pushforward of $\nu$, not integration against an assumed spectral
density.

\begin{proposition}[Uniform scalar row]\label{P:frequency-row}
  There is a finite $K = K(\alpha,a,\gamma)$, independent of $d,\nu,C,h$ and
  $\xi$, such that
  \begin{equation}\label{E:frequency-row-bound}
    \sup_{\xi\in\R^d}J_h(\xi) \le K C B_\alpha(h),
    \qquad 0 < h \le 1.
  \end{equation}
\end{proposition}

\begin{proof}
  If $C = 0$, a countable covering by finite balls gives $\nu = 0$, and the
  result is immediate. Suppose $C > 0$. For each $\xi$, let $\nu_\xi$ be the
  pushforward under $\lambda \mapsto \eta = \xi-\lambda$. Then $\nu_\xi(B(0,R))
  \le CR^\alpha$. For $q \ge 1$, put
  \[
    A_\xi(q) = \int_{|\eta|\le5q}\langle\eta\rangle^{-1}
    \nu_\xi(\ud\eta).
  \]
  Choose $N = \lceil\log_2(5q)\rceil$, so $5q \le 2^N < 10q$. Splitting into the
  unit ball and the annuli $2^j < |\eta| \le 2^{j+1}$ gives
  \[
    A_\xi(q) \le C\left(1+2^\alpha
    \sum_{j=0}^{N-1}2^{j(\alpha-1)}\right).
  \]
  The geometric sum is bounded when $\alpha < 1$, is $N$ when $\alpha = 1$, and
  is at most $2^{N(\alpha-1)}/(2^{\alpha-1}-1)$ when $\alpha > 1$. Hence,
  \begin{equation}\label{E:frequency-inverse-bessel}
    A_\xi(q) \le K_\alpha C
    \begin{cases}
      1, & \alpha < 1,\\
      1+\log q, & \alpha = 1,\\
      q^{\alpha-1}, & \alpha > 1,
    \end{cases}
  \end{equation}
  with a constant depending only on $\alpha$.

  Set $q = \max(1,|\xi|)$ and $\epsilon = 1-2\gamma > 0$. On $|\lambda| \le 4q$
  we have $|\eta| \le 5q$. Both bracket powers in $\mathcal{Q}_h$ are at most
  one, since $a-1 < 0$. The contribution of this region to $J_h(\xi)$ is at most
  \[
    2\langle\xi\rangle^{-\epsilon}A_\xi(q)
    \le 2q^{-\epsilon}A_\xi(q).
  \]
  If $\alpha < 1$, this is uniformly bounded
  by~\eqref{E:frequency-inverse-bessel}. If $\alpha = 1$, the bound follows from
  \[
    e^{-\epsilon u}(1+u) \le 1+\frac1{e\epsilon},
    \qquad u = \log q \ge 0,
  \]
  since $u e^{-\epsilon u}$ has maximum $1/(e\epsilon)$. If $\alpha > 1$, the
  remaining power is $q^{\alpha+2\gamma-2}$, whose exponent is negative
  by~\eqref{E:variance-gamma-range}. Thus, the near contribution is at most a
  constant times $C$ in all three cases.

  On the far region write $r = |\lambda| > 4q$. Then
  \[
    |\eta| \ge \frac{3r}4,\qquad
    \big||\eta|-|\xi|\big| \ge \frac r2,\qquad
    |\eta|+|\xi| \ge \frac r2.
  \]
  Each oscillatory bracket is at least $\langle hr\rangle/2$, whereas
  $\langle\eta\rangle^{-1} \le 4/(3r)$ and $\langle\xi\rangle^{-\epsilon} \le
  1$. Consequently, the far contribution is at most
  \[
    \frac43\,2^{2-a}\int_{|\lambda|>4q}
    |\lambda|^{-1}\langle h|\lambda|\rangle^{a-1}\nu(\ud\lambda).
  \]
  Enlarge the domain to $|\lambda| > 1$ and split it into dyadic annuli.
  Applying~\eqref{E:frequency-translated-growth} to their masses bounds this
  expression by a constant depending only on $\alpha,a$ times $C S(h)$, where
  \[
    S(h) = \sum_{j=0}^\infty
    2^{j(\alpha-1)}\langle h2^j\rangle^{a-1}.
  \]
  Choose $L = \lfloor\log_2(1/h)\rfloor \ge 0$. For $j \le L$ the bracket power
  is at most one. For $j \ge L+1$ it is at most $(h2^j)^{a-1}$. Since
  $\alpha+a-2 < 0$, the tail is
  \[
    \frac{h^{a-1}2^{(L+1)(\alpha+a-2)}}{1-2^{\alpha+a-2}}
    \le \frac{h^{1-\alpha}}{1-2^{\alpha+a-2}}.
  \]
  The inequality uses $2^{L+1} > 1/h$ and the negative exponent. The finite sum
  is bounded by $1/(1-2^{\alpha-1})$ for $\alpha < 1$, by $1+\log_2(1/h)$ for
  $\alpha = 1$, and by
  \[
    \frac{2^{\alpha-1}h^{1-\alpha}}{2^{\alpha-1}-1}
  \]
  for $\alpha > 1$. Since $h^{1-\alpha} \le 1$ in the first case, we obtain
  $S(h) \le K_{\alpha,a}B_\alpha(h)$. Combining the near and far bounds, and
  using $B_\alpha(h) \ge 1$, proves the assertion and finiteness of the original
  integral. All constants arose from numerical shell estimates and are
  independent of $d$. This proves Proposition~\ref{P:frequency-row}.
\end{proof}

\begin{corollary}[A time exponent above one half]\label{C:frequency-time}
  For every
  \begin{equation}\label{E:variance-beta-range}
    \frac12 < \beta < \min\left(1-\frac a2,
    \frac{3-a-\alpha}{2}\right),
  \end{equation}
  there is a finite $K_\beta = K_\beta(\alpha,a,\gamma,\beta)$ such that
  \begin{equation}\label{E:frequency-time-bound}
    h^{2-a}\sup_\xi J_h(\xi) \le K_\beta C h^{2\beta},
    \qquad 0 < h \le 1.
  \end{equation}
\end{corollary}

\begin{proof}
  Both upper endpoints in~\eqref{E:variance-beta-range} exceed one half, by $a <
  1$ and $\alpha+a < 2$. If $\alpha < 1$, use $2-a > 2\beta$ in
  Proposition~\ref{P:frequency-row}. If $\alpha > 1$, use $3-a-\alpha > 2\beta$.
  For $\alpha = 1$, set $\delta = 2-a-2\beta > 0$ and $u = \log(1/h)$. Then
  \[
    h^\delta(1+\log(1/h))
    = e^{-\delta u}(1+u) \le 1+\frac1{e\delta}.
  \]
  This absorbs the critical logarithm. No endpoint value of $\beta$ is used.
  This proves Corollary~\ref{C:frequency-time}.
\end{proof}

\subsection{Forms on the full phase}

Choose and fix $T > 0$. Set $\Lambda = (1-\Delta)^{1/2}$, $s = 1/2$ and $E_r =
H^r(\R^d)\times H^{r-1}(\R^d)$. On the complexification of $E = E_s$, use inner
products linear in the first slot. The map
\[
  Jz(\xi) = \left(\langle\xi\rangle^{1/2}\widehat{z}_1(\xi),
  \langle\xi\rangle^{-1/2}\widehat{z}_2(\xi)\right)
\]
is unitary onto $L^2(\R^d;\mathbb{C}^2)$. The full massless wave group has
Fourier matrix
\begin{equation}\label{E:variance-free-matrix}
  S(t,\xi) =
  \begin{pmatrix}
    \cos(t|\xi|) & \sin(t|\xi|)/|\xi|\\
    -|\xi|\sin(t|\xi|) & \cos(t|\xi|)
  \end{pmatrix},
\end{equation}
where the sine quotient is $t$ at zero. Let $B(b)(u,v) = (0,bu)$. Choose and fix
a real even nonnegative $\zeta \in C_c^\infty(\R^d)$ equal to one on $B_1$ and
zero off $B_2$, and put $\zeta_R(x) = \zeta(x/R)$ for $R > 0$. For $I =
[t_0,t_0+h] \subset [0,T]$, $0 < h \le 1$, and Schwartz phases $z,w$, put
\begin{align}
  v_z(t) &= [S(t)z]_1,
  \label{E:variance-displacement}\\
  G_w(t) &= -\frac{\sin(t|D|)}{|D|}\Lambda w_1
  +\cos(t|D|)\Lambda^{-1}w_2,
  \label{E:variance-dual-wave}\\
  F_{z,w}(t,x) &= 1_I(t)v_z(t,x)\overline{G_w(t,x)},
  \qquad \ell_R(I;z,w) = W_{\mathbb{C}}(\zeta_RF_{z,w}),
  \label{E:variance-actual-form}
\end{align}
where $W_{\mathbb{C}}(F) = W(\operatorname{Re}F)+iW(\operatorname{Im}F)$. There
is no observation cutoff in this definition.

We first assume $\Gamma \ne 0$. If $\Gamma = 0$, all forms and the column maps
below are zero, so their bounds hold directly. For the nonzero case, let $\nu_R$
be~\eqref{E:masked-auxiliary-measure} and set
\begin{equation}\label{E:variance-actual-growth-constant}
  L_\zeta = \|\widehat{\zeta}\|_1,\qquad
  C_\nu = c_d^2L_\zeta^2C_\Gamma.
\end{equation}
Proposition~\ref{P:masked-auxiliary-norm} gives a positive even tempered Radon
measure with $\nu_R(B(y,r)) \le C_\nu r^\alpha$, uniformly in $R$.

\begin{proposition}[Form and phase kernel]\label{P:actual-wave-form}
  The tests $\zeta_RF_{z,w}$ in~\eqref{E:variance-actual-form} belong to the
  original noise completion. The form $\ell_R$ is linear in $z$ and conjugate
  linear in $w$, and uses the same $W$ as the model. For a smooth deterministic
  coefficient $b$ with common compact spatial support and bounded spatial
  derivatives on $[0,T]$,
  \begin{equation}\label{E:variance-physical-adjoint}
    \langle S(-t)B(b(t))S(t)z,w\rangle_E
    = \int b(t,x)v_z(t,x)\overline{G_w(t,x)}\ud x.
  \end{equation}
  For a real compact smooth $\chi$, multiplication $D_\chi$ on both phase
  entries has adjoint
  \begin{equation}\label{E:variance-cutoff-adjoint}
    D_\chi^{*,E}w
    = \left(\Lambda^{-1}\chi\Lambda w_1,
    \Lambda\chi\Lambda^{-1}w_2\right).
  \end{equation}
  With $U = Jz$, $V = Jw$, $r = |\xi|$, $\rho = |\eta|$ and the continuous
  functions $c_r,b_r$ of Lemma~\ref{L:masked-continuous-wave}, set
  \begin{equation}\label{E:variance-normalized-kernel}
    \mathcal{K}(t;\xi,\eta)
    = \frac1{\sqrt{\langle\xi\rangle\langle\eta\rangle}}
    \begin{pmatrix}
      -b_rc_\rho & -b_rb_\rho\\
      c_rc_\rho & c_rb_\rho
    \end{pmatrix}(t).
  \end{equation}
  Then
  \begin{equation}\label{E:variance-normalized-covariance}
    \E|\ell_R(I;z,w)|^2
    \le \int\left\|\int\sum_{i,j=1}^2
    1_I\mathcal{K}_{ij}(\cdot;\eta+\lambda,\eta)
    U_j(\eta)\overline{V_i(\eta+\lambda)}\ud\eta
    \right\|_{H_a^{\mathbb{C}}}^2\nu_R(\ud\lambda).
  \end{equation}
\end{proposition}

\begin{proof}
  The wave multipliers are smooth at zero through the continuous sine quotient,
  with polynomially bounded frequency derivatives on finite time intervals.
  Bessel multipliers preserve Schwartz space. Thus, $v_z,G_w$ and their product
  are continuous in all Schwartz seminorms on $[0,T]$. For tests supported in a
  fixed compact $K$, the absolute spatial pairing is bounded by
  \[
    |K|\Gamma(K-K)\|F(t)\|_\infty\|H(u)\|_\infty.
  \]
  Indeed, only $y \in K-K$ contributes to $\int\Gamma(\ud y)\int
  F(t,x)\overline{H(u,x-y)}\ud x$. Combine this with the temporal Schur bound
  and approximate the interval indicator and the continuous time dependence by
  smooth interior temporal tests, keeping the spatial support of $\zeta_R$. This
  admits the masked product in the original completion in every allowed
  dimension.

  We also identify its auxiliary and spectral limits. Approximate a
  Schwartz-valued function on $I$ by time partitions with frozen spatial values,
  and then replace the finitely many indicators by compact smooth temporal
  functions. A diagonal sequence $F_n$ of finite temporal tensors converges in
  $L^2$ time in every Schwartz seminorm. Fourier integration by parts and the
  spatial weighted supremum bounds give, for sufficiently large fixed $N$,
  \[
    \|\widehat{F_n-F}(\xi)\|_{L^2(0,T)}
    \le \epsilon_n\langle\xi\rangle^{-N},\qquad \epsilon_n \to 0.
  \]
  Choose $N$ so that the square weight is integrable against both tempered
  measures $\mu$ and $\nu_R$. Lemma~\ref{L:masked-time-completion} gives
  convergence in their spectral $H_a$ norms. Multiplication by the fixed
  $\zeta_R$ preserves these $L^2$ Schwartz-seminorm limits, so the masked
  differences converge in the $\mu$ spectral norm too. The preceding
  compact-support estimate also gives convergence in the original completion.
  Hence, the auxiliary extension and original-noise limit agree on these
  products. Constants for this admission argument may depend on $R$; they are
  not the uniform variance constants below.

  For real tensor tests $f,g$, the Hermitian symmetry of their spatial
  transforms gives
  \[
    A(-\xi) = \overline{A(\xi)},\qquad
    A(\xi) = \langle\widehat{f}(\xi),\widehat{g}(\xi)\rangle_{H_a^{\mathbb{C}}}.
  \]
  Integration against either even $\mu$ or even $\nu_R$ cancels the imaginary
  mixed term. Expanding the squared norm of $\widehat{f}+i\widehat{g}$, then
  using the preceding approximation, extends
  Proposition~\ref{P:masked-noise-completion} to the present complex tests:
  \begin{equation}\label{E:variance-complex-noise}
    \E|W_{\mathbb{C}}(\zeta_RF)|^2
    = (2\pi)^d\int\|\widehat{\zeta_RF}(\xi)\|_{H_a^{\mathbb{C}}}^2\mu(\ud\xi)
    \le (2\pi)^d\int\|\widehat{F}(\lambda)\|_{H_a^{\mathbb{C}}}^2\nu_R(\ud\lambda).
  \end{equation}
  This is a bound for the masked noise, not a declaration that its law is
  stationary. Complex linearity of $W_{\mathbb{C}}$ and linearity of $v_z,G_w$
  prove the stated sesquilinearity.

  Smooth multiplication is bounded on each Sobolev space: Fourier convolution,
  the inequality $\langle\xi\rangle^r\langle\eta\rangle^{-r} \le
  2^{|r|/2}\langle\xi-\eta\rangle^{|r|}$ and weighted Schwartz decay reduce this
  to the $L^1*L^2$ bound. The free matrix is strongly continuous and bounded on
  $E$ on compact time intervals, directly by its weighted Fourier entries. Thus,
  the ordinary first-response integral exists on states. Since $S(-t)(0,f) =
  (-\sin(t|D|)f/|D|,\cos(t|D|)f)$, moving the real self-adjoint multipliers and
  the two Sobolev weights onto $w$ proves \eqref{E:variance-physical-adjoint}.
  The same weighted duality gives \eqref{E:variance-cutoff-adjoint}. Inserting
  this adjoint in $G_w$ is the correctly observed form; $D_\chi$ need not be
  self-adjoint on $E$. This deterministic identity does not identify a
  positive-width source with the original noise or assert a source limit.

  The definitions give exactly
  \begin{align*}
    \widehat{v}_z(t,\eta)
    &= \langle\eta\rangle^{-1/2}
    [c_\rho(t)U_1(\eta)+b_\rho(t)U_2(\eta)],\\
    \widehat{G}_w(t,\xi)
    &= \langle\xi\rangle^{-1/2}
    [-b_r(t)V_1(\xi)+c_r(t)V_2(\xi)].
  \end{align*}
  Their product gives~\eqref{E:variance-normalized-kernel}. At zero frequencies
  one uses the continuous sine quotient, not division by zero; at $\xi = \eta =
  0$ the matrix is
  $\left(\begin{smallmatrix}-t&-t^2\\1&t\end{smallmatrix}\right)$. Fourier
  multiplication with the conjugate yields
  \[
    \widehat{F}_{z,w}(t,-\lambda)
    = c_d1_I(t)\int\sum_{i,j=1}^2\mathcal{K}_{ij}(t;\eta+\lambda,\eta)
    U_j(\eta)\overline{V_i(\eta+\lambda)}\ud\eta.
  \]
  The spatial integral is absolutely convergent uniformly on the finite time
  interval by Schwartz decay. The Schur bound also makes it a Bochner
  $H_a^{\mathbb{C}}$ integral. Reflect $\lambda$ using evenness of $\nu_R$
  in~\eqref{E:variance-complex-noise}. Since $(2\pi)^dc_d^2 = 1$, this
  proves~\eqref{E:variance-normalized-covariance} with no remaining Fourier
  factor. This proves Proposition~\ref{P:actual-wave-form}.
\end{proof}

\subsection{Bessel's inequality and the two variances}

\begin{lemma}[Hilbert-valued finite Bessel inequality]\label{L:phase-bessel}
  Let $H$ be a separable complex Hilbert space, let $\{u_k\}$ be a finite
  orthonormal family in $L^2(\R^d;\mathbb{C}^2)$, and let $g = (g_1,g_2) \in
  L^2(\R^d;H^2)$. Then
  \begin{equation}\label{E:phase-bessel}
    \sum_k\left\|\int\sum_{j=1}^2u_{k,j}(\eta)g_j(\eta)\ud\eta\right\|_H^2
    \le \int\sum_{j=1}^2\|g_j(\eta)\|_H^2\ud\eta.
  \end{equation}
  The same bound holds with $\overline{u_{k,j}}$ in place of $u_{k,j}$.
\end{lemma}

\begin{proof}
  Expand $g$ in a countable orthonormal basis of $H$. On each scalar coefficient
  apply scalar Bessel to the orthonormal family $\{\overline{u_k}\}$, or to
  $\{u_k\}$ for the conjugated version. Scalar finite Bessel follows by
  subtracting an orthogonal finite projection and expanding its nonnegative
  squared norm. Sum over the $H$ basis and use Parseval and nonnegative Tonelli.
  The Bochner integrals exist by $L^2$ Cauchy--Schwarz. A finite-dimensional $H$
  uses its finite basis, and the zero space is immediate. No independence is
  involved. This proves Lemma~\ref{L:phase-bessel}.
\end{proof}

\begin{proposition}[Both variance directions]\label{P:wave-two-variances}
  There is a finite $C_T$, depending on the fixed model, mask,
  $a,\alpha,\gamma,T$, but not on $R,I$ or the orthonormal family, such that for
  every finite complex $E$-orthonormal Schwartz family $\{e_k\}$ and every
  Schwartz phase $z$,
  \begin{align}
    \sum_k\E|\ell_R(I;e_k,z)|^2
    &\le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2,
    \label{E:wave-input-variance}\\
    \sum_k\E|\ell_R(I;z,e_k)|^2
    &\le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2.
    \label{E:wave-output-variance}
  \end{align}
  For every $\beta$ in~\eqref{E:variance-beta-range}, either right side may be
  replaced by $C_{T,\beta}h^{2\beta}\|z\|_{E_{s-\gamma}}^2$.
\end{proposition}

\begin{proof}
  Each entry in~\eqref{E:variance-normalized-kernel} is a product of two
  continuous wave factors times $(\langle\xi\rangle\langle\eta\rangle)^{-1/2}$,
  with a possible minus sign. Lemma~\ref{L:masked-continuous-wave} therefore
  gives
  \begin{equation}\label{E:variance-kernel-time-bound}
    \|1_I\mathcal{K}_{ij}(\cdot;\xi,\eta)\|_{H_a^{\mathbb{C}}}^2
    \le A_T h^{2-a}\Phi_h(\xi,\eta),
    \qquad A_T = C_1(a)(1+T)^4.
  \end{equation}
  The positive even Radon measure $\nu_R$ satisfies the growth bound
  \eqref{E:variance-actual-growth-constant}. Thus, all hypotheses of
  Proposition~\ref{P:frequency-row} hold, and
  \begin{equation}\label{E:variance-actual-row-bound}
    \int\Phi_h(\xi,\xi-\lambda)\nu_R(\ud\lambda)
    \le K C_\nu B_\alpha(h)\langle\xi\rangle^{-2\gamma}.
  \end{equation}
  No nonnegative physical inverse covariance of $\nu_R$ is needed.

  The kernels used in Lemma~\ref{L:phase-bessel} belong to its stated $L^2$
  space for each fixed $\lambda$. Indeed, $|c_r(t)| \le 1$ and $|b_r(t)| \le
  \sqrt{2}\max(1,T)$ on $[0,T]$, by the high- and low-frequency representations.
  The kernels are continuous into $L^2(0,T)$ in their frequency variables, hence
  into $H_a^{\mathbb{C}}$ by Schur. Separability gives strong measurability.
  Multiplication by shifted Schwartz components of $U$ or $V$ then gives the
  required $L^2$ integrability. Later $\lambda$ integrals are of nonnegative
  functions; their finiteness follows from the estimates below.

  First fix $V = Jz$ and let $U_k = Je_k$ be the input family.
  In~\eqref{E:variance-normalized-covariance} set
  \[
    g_j^\lambda(\eta) = \sum_{i=1}^2
    1_I\mathcal{K}_{ij}(\cdot;\eta+\lambda,\eta)
    \overline{V_i(\eta+\lambda)}.
  \]
  Lemma~\ref{L:phase-bessel} and Cauchy--Schwarz over the two output components
  give
  \begin{align*}
    \sum_j\|g_j^\lambda(\eta)\|_{H_a^{\mathbb{C}}}^2
    &\le 2\sum_{i,j}|V_i(\eta+\lambda)|^2
    \|1_I\mathcal{K}_{ij}(\cdot;\eta+\lambda,\eta)\|_{H_a^{\mathbb{C}}}^2\\
    &\le 4A_T h^{2-a}\Phi_h(\eta+\lambda,\eta)
    \sum_i|V_i(\eta+\lambda)|^2.
  \end{align*}
  Change variables $\xi = \eta+\lambda$ in the Lebesgue integral for each
  $\lambda$, apply Tonelli and~\eqref{E:variance-actual-row-bound}, and use
  $\|z\|_{E_{s-\gamma}} = \|\langle\xi\rangle^{-\gamma}Jz\|_2$. This
  proves~\eqref{E:wave-input-variance} with $C_T = 4A_TKC_\nu$.

  Next fix $U = Jz$ and let $V_k = Je_k$ be the output family. After $\eta =
  \xi-\lambda$ in~\eqref{E:variance-normalized-covariance}, put
  \[
    f_i^\lambda(\xi) = \sum_{j=1}^2
    1_I\mathcal{K}_{ij}(\cdot;\xi,\xi-\lambda)U_j(\xi-\lambda).
  \]
  Apply the conjugated version of Lemma~\ref{L:phase-bessel}. Cauchy--Schwarz
  over the two input components bounds its right side by
  \[
    4A_T h^{2-a}\int\Phi_h(\xi,\xi-\lambda)
    \sum_j|U_j(\xi-\lambda)|^2\ud\xi.
  \]
  After the change of variables and Tonelli, the row at fixed $\eta$ is
  $\int\Phi_h(\eta+\lambda,\eta)\nu_R(\ud\lambda)$. Reflect $\lambda$ using the
  evenness of $\nu_R$ and then use symmetry of $\Phi_h$. This row becomes
  $\int\Phi_h(\eta,\eta-\lambda)\nu_R(\ud\lambda)$, which is bounded
  by~\eqref{E:variance-actual-row-bound} with $\xi = \eta$. This proves
  \eqref{E:wave-output-variance} with the same $C_T$.

  Use Corollary~\ref{C:frequency-time} for $h^{2-a}$ times the row integral at
  the two applications above to obtain the asserted $h^{2\beta}$ bounds,
  including strict absorption of the critical logarithm. The constants are
  uniform in $R,I$ and family size. The $R$-dependent admission estimate was not
  used as this uniform variance bound. This proves
  Proposition~\ref{P:wave-two-variances}.
\end{proof}

\subsection{Mean-square columns on the original probability space}

Write $E_r^{\mathrm{real}}$ for the real phase space in dimension $d$.

\begin{proposition}[Column and adjoint-column maps]\label{P:wave-square-columns}
  On the same probability space there are deterministic bounded real linear maps
  \[
    m_{R,I},n_{R,I}:E_{s-\gamma}^{\mathrm{real}}\longrightarrow
    L^2(\Omega;E_s^{\mathrm{real}}),
  \]
  with squared bounds $C_T h^{2-a}B_\alpha(h)$, such that, for every fixed real
  Schwartz pair $z,w$,
  \begin{equation}\label{E:variance-square-columns}
    \langle m_{R,I}z,w\rangle_E
    = \ell_R(I;z,w) = \langle z,n_{R,I}w\rangle_E
    \quad\text{in }L^2(\Omega).
  \end{equation}
  Fixed-vector values and finite families of values are centered Gaussian.
\end{proposition}

\begin{proof}
  Choose a countable real Schwartz orthonormal basis $\{e_k\}$ of $E_s$. Such a
  basis follows by Gram--Schmidt from a countable dense Schwartz family,
  discarding zero residuals. Schwartz density follows by smooth Fourier cutoff
  approximation in the weighted $L^2$ norms: approximate by compact smooth
  Fourier coordinates, replace $g(\xi)$ by $(g(\xi)+\overline{g(-\xi)})/2$, and
  apply the inverse Bessel/Fourier maps. The resulting phases are real Schwartz,
  and Gram--Schmidt preserves that class. The same density holds in
  $E_{s-\gamma}$.

  For fixed real Schwartz $z$, define
  \[
    m_N(z) = \sum_{k\le N}\ell_R(I;z,e_k)e_k,
    \qquad n_N(z) = \sum_{k\le N}\ell_R(I;e_k,z)e_k.
  \]
  Both are finite Gaussian sums on the original $W$. By
  Proposition~\ref{P:wave-two-variances}, their coefficient expected squares
  have finite sum. Orthogonality gives the squared tail norms as the
  corresponding sums of expected squares. Thus, both sequences converge in
  $L^2(\Omega;E_s)$ to $m(z),n(z)$ with the asserted bounds, without
  independence of the coefficients. Finite-sum measurability and separable $E_s$
  give strong measurability of the limits. The bounded real linear maps extend
  uniquely from Schwartz phases to $E_{s-\gamma}$.

  If $w_N$ is the $E_s$ projection of a Schwartz $w$ onto the first $N$ basis
  vectors, then $\langle m_N(z),w\rangle_E = \ell_R(I;z,w_N)$. The singleton
  form of~\eqref{E:wave-output-variance}, after normalizing $w-w_N$ in $E_s$,
  gives
  \[
    \E|\ell_R(I;z,w-w_N)|^2
    \le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2\|w-w_N\|_{E_s}^2.
  \]
  The zero residual is immediate. The right side tends to zero, giving the first
  identity in~\eqref{E:variance-square-columns}. For the second, project $z$
  instead and use the singleton input bound \eqref{E:wave-input-variance}. A
  fixed countable Schwartz orthonormal basis and Parseval show basis
  independence of the constructed limits.

  Continuous linear functionals of the limits, and finite linear combinations of
  such functionals, are $L^2$ limits of centered Gaussian variables with
  convergent variances. Their characteristic functions therefore converge to
  those of centered Gaussians. The same reasoning after the bounded input
  extension proves joint Gaussianity for arbitrary fixed inputs and finite
  families of the two maps. This proves Proposition~\ref{P:wave-square-columns}.
\end{proof}

These are maps into $L^2(\Omega;E_s)$ for fixed intervals. No common uncountable
almost-sure version, random bounded operator, Hilbert--Schmidt realization, time
path, source convergence or new solution-moment bound is inferred by this
section alone. Both variance directions are retained in
Section~\ref{S:actual-operator-driver}.

# notes/integrated_positive_gram.tex

\section{Finite optimization with nonnegative Gram entries}
\label{S:finite-positive-gram}

Let $H$ be any real Hilbert space, $\mathcal{I}$ a finite index set, $k_i \in
H$, $\ell_i > 0$ and $b_i \ge 0$. Write $C_{ij} = \langle k_i,k_j\rangle$ and
assume $C_{ij} \ge 0$ for every pair. The Gram matrix is symmetric and positive
semidefinite, since $\sum_{i,j}a_iC_{ij}a_j = \|\sum_i a_i k_i\|^2$. Put $t_+ =
\max(t,0)$ and define
\begin{equation}\label{E:finite-gram-score}
  \mathfrak{F}_C(\Phi)
  =2\sum_{i\in\mathcal{I}}\ell_i
  \sqrt{(\langle\Phi,k_i\rangle-b_i)_+}-\|\Phi\|^2/2,
  \qquad \mathscr{S}(C)=\sup_{\Phi\in H}\mathfrak{F}_C(\Phi).
\end{equation}
Let $\mathcal{J} = \{i:k_i\ne0\} = \{i:C_{ii}>0\}$. Zero vectors contribute zero
because $b_i \ge 0$. Empty index sets, singular Grams and $H = \{0\}$ are
allowed. For nonempty $A \subset \mathcal{J}$ and $w_i > 0$, set
\begin{equation}\label{E:finite-gram-dual}
  D_A^C(w)=\sum_{i\in A}\frac{\ell_i^2}{w_i}
  -\sum_{i\in A}b_iw_i
  +\frac12\sum_{i,j\in A}w_iC_{ij}w_j,
  \qquad d_A^C=\inf_{w_i>0}D_A^C(w).
\end{equation}
Set $d_\varnothing^C = 0$.

\begin{lemma}[Scalar and Hilbert identities]\label{L:gram-scalar-algebra}
  For real $\ell$, $w > 0$ and $t \ge 0$,
  \begin{equation}\label{E:gram-sqrt-dual}
    2\ell\sqrt t\le\ell^2/w+wt.
  \end{equation}
  For $\Phi,z \in H$,
  \begin{equation}\label{E:gram-hilbert-square}
    \langle\Phi,z\rangle-\|\Phi\|^2/2
    =\|z\|^2/2-\|\Phi-z\|^2/2\le\|z\|^2/2.
  \end{equation}
  For finite real $w_i$, $\|\sum_iw_ik_i\|^2 = \sum_{i,j}w_iC_{ij}w_j$.
\end{lemma}

\begin{proof}
  Since $\sqrt w > 0$ and $\sqrt{wt} = \sqrt w\sqrt t$,
  \[
    0\le(\ell/\sqrt w-\sqrt{wt})^2
    =\ell^2/w+wt-2\ell\sqrt t.
  \]
  This includes $t = 0$. If $\ell,t > 0$, equality holds for $w = \ell/\sqrt t$.
  Expanding $\|\Phi-z\|^2$ proves~\eqref{E:gram-hilbert-square}. Bilinearity of
  the real inner product proves the finite Gram identity. These identities use
  neither compactness of a Hilbert ball nor an inverse covariance matrix. This
  proves Lemma~\ref{L:gram-scalar-algebra}.
\end{proof}

\begin{lemma}[Interior dual minimum]\label{L:gram-dual-minimum}
  Each nonempty $A \subset \mathcal{J}$ has a unique positive minimizer $w^A$ of
  $D_A^C$. At this minimizer,
  \begin{equation}\label{E:gram-dual-stationarity}
    \sum_{j\in A}C_{ij}w_j^A-b_i
    =\frac{\ell_i^2}{(w_i^A)^2}>0,\qquad i\in A.
  \end{equation}
\end{lemma}

\begin{proof}
  Put $c_i = C_{ii} > 0$ and $K_A = \sum_{i\in A}b_i^2/c_i$. Nonnegative entries
  and positive weights give
  \[
    D_A^C(w)\ge
    \sum_i\left(\ell_i^2/w_i-b_iw_i+c_iw_i^2/2\right).
  \]
  Completing the square in $c_iw_i^2/4-b_iw_i$ yields
  \begin{equation}\label{E:gram-dual-coercivity}
    D_A^C(w)\ge
    \sum_i\ell_i^2/w_i+\frac14\sum_i c_iw_i^2-K_A.
  \end{equation}
  Thus, no coordinate can approach zero or infinity in a bounded sublevel while
  a different negative term hides its growth. Take $w^0 = (1,\ldots,1)$, $d_0 =
  D_A^C(w^0)$ and $L_A = d_0+K_A$. Equation~\eqref{E:gram-dual-coercivity} at
  $w^0$ gives $L_A \ge \sum_i\ell_i^2+\sum_i c_i/4 > 0$. Every $w$ with
  $D_A^C(w) \le d_0$ satisfies
  \[
    \ell_i^2/L_A\le w_i\le\sqrt{4L_A/c_i}.
  \]
  The sublevel is nonempty and closed inside this compact box, which lies in the
  open positive orthant. A minimizing sequence chosen in the sublevel has a
  convergent subsequence there. Continuity attains its infimum. Outside this
  sublevel the values exceed $d_0$, so the minimum is global on the entire
  positive orthant.

  The function is smooth in that orthant. Its Hessian on a nonzero vector $\xi$
  has value
  \[
    \sum_i\frac{2\ell_i^2}{w_i^3}\xi_i^2
    +\sum_{i,j}\xi_iC_{ij}\xi_j>0.
  \]
  The first term is strictly positive and the second is a squared Hilbert norm.
  Restriction to any nonconstant line segment is strictly convex, proving
  uniqueness. Each coordinate permits both signs of a small perturbation at the
  interior minimum. Differentiation gives $-\ell_i^2/w_i^2-b_i+\sum_jC_{ij}w_j =
  0$. This is~\eqref{E:gram-dual-stationarity}. This proves
  Lemma~\ref{L:gram-dual-minimum}.
\end{proof}

\begin{proposition}[Positive conic maximizer]\label{P:gram-positive-optimizer}
  The finite real value in~\eqref{E:finite-gram-score} satisfies
  \begin{equation}\label{E:gram-active-duality}
    \mathscr{S}(C)=\max_{A\subset\mathcal{J}}d_A^C .
  \end{equation}
  If a maximizing subset is empty, $\Phi = 0$ attains the supremum. If a
  maximizing subset $A$ is nonempty, a maximizer is $\Phi_A = \sum_{i\in A}w_i^A
  k_i$ with strictly positive coefficients. No uniqueness of the primal
  maximizer or maximizing subset is asserted.
\end{proposition}

\begin{proof}
  For arbitrary $\Phi$, let $A(\Phi) = \{i:\langle\Phi,k_i\rangle>b_i\}$. It is
  contained in $\mathcal{J}$. All other terms in the objective vanish, including
  equality at the threshold. If $A(\Phi)$ is empty, $\mathfrak{F}_C(\Phi) =
  -\|\Phi\|^2/2 \le 0$. Otherwise, for any positive $w$ on $A = A(\Phi)$, set
  $t_i = \langle\Phi,k_i\rangle-b_i > 0$ and $z = \sum_{i\in A}w_ik_i$.
  Lemma~\ref{L:gram-scalar-algebra} gives
  \[
    \mathfrak{F}_C(\Phi)
    \le\sum_i\ell_i^2/w_i-\sum_i b_iw_i
    +\langle\Phi,z\rangle-\|\Phi\|^2/2
    \le D_A^C(w).
  \]
  This holds for every positive $w$, so $\mathfrak{F}_C(\Phi) \le d_A^C$. There
  are finitely many subsets and their values are finite by
  Lemma~\ref{L:gram-dual-minimum}. Taking the supremum bounds $\mathscr{S}(C)$
  above by their maximum.

  Conversely, $\mathfrak{F}_C(0) = 0 = d_\varnothing^C$. For nonempty $A$, take
  its dual minimizer. Equation~\eqref{E:gram-dual-stationarity} makes every
  vector in $A$ strictly active at $\Phi_A$, with
  $\sqrt{\langle\Phi_A,k_i\rangle-b_i} = \ell_i/w_i^A$. Both inequalities in the
  preceding display are then equalities for the sum restricted to $A$, since $z
  = \Phi_A$. This restricted objective equals $d_A^C$. All omitted vectors
  contribute nonnegative terms to the full objective, hence
  $\mathfrak{F}_C(\Phi_A) \ge d_A^C$, even if this value is negative. Maximizing
  over $A$, including the empty set, proves \eqref{E:gram-active-duality} and
  the asserted attainment. For a maximizing nonempty subset the upper and lower
  bounds force $\mathfrak{F}_C(\Phi_A) = d_A^C$; no outside inactivity was
  assumed. All-zero vectors give $\mathscr{S}(C) = 0$ directly. This proves
  Proposition~\ref{P:gram-positive-optimizer}.
\end{proof}

No-go~\ref{P:nogo-29} gives the three finite counterexamples behind this
formulation: the empty active set cannot be omitted, the primal objective
need not be concave, and entrywise matrix order is not positive
semidefinite order.


\input{notes/figures/active-subset-optimization}

\input{notes/figures/positive-gram}

\begin{lemma}[Real Gram realization]\label{L:gram-realization}
  Every finite real symmetric positive semidefinite matrix is the Gram matrix of
  vectors in a finite-dimensional real Hilbert space. When its entries are
  nonnegative, the value $\mathscr{S}(C)$ is independent of its realization.
\end{lemma}

\begin{proof}
  Induct on the size, with the empty matrix realized in $\{0\}$. Diagonal
  entries are nonnegative. If all vanish, testing on $e_i+t e_j$ gives $2tC_{ij}
  \ge 0$ for every real $t$, hence $C = 0$, realized by zero vectors. Otherwise
  permute a positive diagonal $c$ into the first position and write $C =
  \left[\begin{smallmatrix}c&v^{\mathsf{T}}\\v&A\end{smallmatrix}\right]$. The
  Schur complement $B = A-vv^{\mathsf{T}}/c$ is positive semidefinite: test the
  original quadratic form on $(-v^{\mathsf{T}}y/c,y)$. Realize $B$ by vectors
  $u_i$ using the induction hypothesis. Then $k_1 = (\sqrt c,0)$ and $k_i =
  (v_i/\sqrt c,u_i)$ for the other indices realize $C$. Undo the permutation.
  Entries of $B$ need not be nonnegative; this construction requires neither
  nonnegative coordinates nor complete positivity.

  In any realization, $C_{ii} = 0$ means $k_i = 0$, so its entire row vanishes.
  Formula~\eqref{E:gram-active-duality} depends only on $C,\ell,b$ and these
  eligible indices. It therefore proves realization independence whenever the
  entries are nonnegative, which is the scope in which $\mathscr{S}(C)$ is used.
  This proves Lemma~\ref{L:gram-realization}.
\end{proof}

\begin{proposition}[Entrywise Gram comparison]\label{P:gram-entrywise-comparison}
  Let $C,D$ be real symmetric positive semidefinite matrices on the same finite
  index set, with $0 \le C_{ij} \le D_{ij}$. With the same $\ell_i > 0,b_i \ge
  0$,
  \[
    \mathscr{S}(C)\le\mathscr{S}(D).
  \]
  No positive-semidefinite order on $D-C$ is required.
\end{proposition}

\begin{proof}
  Lemma~\ref{L:gram-realization} defines both values. Their eligible sets
  satisfy $\mathcal{J}_C \subset \mathcal{J}_D$. For nonempty $A \subset
  \mathcal{J}_C$ and positive weights,
  \[
    D_A^D(w)-D_A^C(w)
    =\frac12\sum_{i,j\in A}w_i(D_{ij}-C_{ij})w_j\ge0.
  \]
  Taking infima gives $d_A^C \le d_A^D$. The empty values are both zero. Taking
  maxima and using the inclusion of eligible families proves the claim by
  Proposition~\ref{P:gram-positive-optimizer}. This includes the appearance of
  previously zero vectors. This proves
  Proposition~\ref{P:gram-entrywise-comparison}.
\end{proof}

\begin{remark}[Exact checks and scope]\label{R:gram-controls}
  The empty value is essential: for one vector with $C = 1$, $\ell = 1/10,b =
  4$, the nonempty dual has $D(4) = -3199/400 < 0$, whereas the primal objective
  at zero is zero. Global concavity is unavailable: for $k = \ell = b = 1$ the
  objective $2\sqrt{(\phi-1)_+}-\phi^2/2$ decreases on $[0,1]$ and has infinite
  positive right slope at one. For $k = \ell = 1,b = 0$, differentiation on
  $\phi > 0$ gives the maximum $3/2$ at $\phi = 1$; on $\phi \le 0$ the
  objective is nonpositive. Doubling the cost changes the positive critical
  point to $2^{-2/3}$ and the maximum to $3\,2^{-4/3}$. Finally, $C = I_2$, $D =
  \left[\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\right]$ are nonnegative
  positive semidefinite Grams but $D-C$ has eigenvalues $1/2,-1/2$. These are
  finite analytic checks, not a covariance-order theorem for physical waves.

  The scalar, finite Gram, conditional active upper and half-quadratic entrywise
  deductions have existing local Lean certificates at their exact hypotheses.
  Dual coercivity, calculus, attainment, realization and the infimum/maximum
  argument above remain analytic proofs. No new kernel fact or formalization of
  the physical application follows merely from these certificates.
\end{remark}

# notes/integrated_occupation_ceiling.tex

\section{Occupation bounds for the intrinsic constant}
\label{S:intrinsic-occupation-ceiling}

Retain all original models and amplitudes, put $a = \alpha_0$, $q = 4-\alpha >
2$, $k = 3-\alpha = q-1 > 1$ and $m = q/k$. The temporal kernel is $K(s,t) =
|s-t|^{-a}$ on $I = (0,1)$; its diagonal value may be set to zero. Let
$\mathcal{O}$ be the full strongly $H^1$-measurable unit-profile class defined
before Proposition~\ref{P:occupation-physical-class}. Here we use the
\emph{original} kernel, defining
\begin{equation}\label{E:raw-occupation-definitions}
  \begin{aligned}
    A(g)&=\int_{I^2}K(s,t)B_\Gamma(g_s^2,g_t^2)\ud s\ud t,\\
    C_{\rm occ}&=\sup_{g\in\mathcal{O}}
    \frac{A(g)}{T(g)^{\alpha/2}},&
    \mathcal{E}_\zeta^{\mathcal{O}}
    &=\sup_{g\in\mathcal{O}}\{A(g)-\zeta T(g)\},\qquad \zeta>0.
  \end{aligned}
\end{equation}
The scalar penalty $\zeta$ is not a spatial mask. These objects differ from the
earlier damped-kernel energy. Assume $\Gamma \ne 0$ until the direct zero case
below.

\begin{lemma}[Full-profile squares in the original space]
  \label{L:occupation-raw-square}
  There is a continuous map $Q:H^1(\R^d;\R) \to H_{\mathrm{sp}}$ with
  \[
    \langle Q(f),Q(h)\rangle_{H_{\mathrm{sp}}}
    =B_\Gamma(f^2,h^2),\qquad
    \|Q(f)\|^2=A_{\mathrm{sp}}(f).
  \]
  For $g \in \mathcal{O}$, the element $\rho_g = J_{H_{\mathrm{sp}}}(s\mapsto
  Q(g_s))$ belongs to the original $H_I$ and satisfies
  \begin{equation}\label{E:occupation-raw-identities}
    \|\rho_g\|_{H_I}^2=A(g),\qquad
    \langle\Psi,\rho_g\rangle_{H_I}
    =\int_I\int_{\R^d}h_{\Psi,s}(x)g_s(x)^2\ud x\ud s
  \end{equation}
  for every $\Psi \in \mathcal{C}_{\mathrm{pos}}$. In particular,
  \[
    \langle\Psi,\rho_g\rangle_{H_I}\le\sqrt{v_\Psi A(g)}.
  \]
\end{lemma}

\begin{proof}
  Approximate $f$ in $H^1$ by real compact smooth $f_n$.
  Proposition~\ref{P:spatial-four-linear} gives
  \[
    \|f_n^2-f_l^2\|_{H_{\mathrm{sp}}}^2
    =C_4(f_n-f_l,f_n+f_l,f_n-f_l,f_n+f_l)
    \le R_{\mathrm{sp}}N(f_n-f_l)^2N(f_n+f_l)^2\to0.
  \]
  Here $N$ is continuous on $H^1$ and $N(f) \le \|f\|_{H^1}$. Completeness
  defines $Q(f)$; interlacing two approximating sequences proves independence.
  Passing the physical four-linear continuity and Hilbert pairings to limits
  proves the first identities. The same difference bound, first for smooth
  approximants and then by passage to the limit, proves continuity of $Q$.

  Thus, $F_g(s) = Q(g_s)$ is strongly measurable. Writing $b_s = \|\nabla
  g_s\|_2^2$, the unit norm and $0 < \alpha/2 < 1$ give
  \[
    \int_I\|F_g(s)\|^2\ud s
    \le R_{\mathrm{sp}}\int_I b_s^{\alpha/2}\ud s
    \le R_{\mathrm{sp}}T(g)^{\alpha/2}<\infty .
  \]
  Lemma~\ref{L:positive-raw-embedding} now constructs $\rho_g$ and identifies
  its squared norm with the physical $A(g)$. Joint measurability and
  representative independence follow from the continuous physical pairing on
  $(H^1)^2$. Absolute time integrability follows from the same Schur bound.

  Choose one compact smooth $\chi$ equal to one on all spatial supports of
  $\Psi_t$. For real $f \in H^1$, smooth approximation gives
  \[
    \langle\Psi_t,Q(f)\rangle_{H_{\mathrm{sp}}}
    =\lim_n B_\Gamma(\Psi_t,f_n^2)
    =C_4(\chi,\Psi_t,f,f)=B_\Gamma(\Psi_t,f^2).
  \]
  Proposition~\ref{P:spatial-four-linear} justifies these absolute integrals and
  limits. Polarizing~\eqref{E:positive-bochner-inclusion} gives
  \[
    \langle\Psi,\rho_g\rangle
    =\int_{I^2}K(s,t)\langle\Psi_t,Q(g_s)\rangle_{H_{\mathrm{sp}}}
    \ud t\ud s .
  \]
  The absolute integrand is bounded by the product of two $H_{\mathrm{sp}}$
  norms against $K$, integrable by Schur and $L^2$ Cauchy--Schwarz. Evenness of
  $\Gamma$ and Tonelli for the nonnegative physical integrands
  yield~\eqref{E:occupation-raw-identities}. Hilbert Cauchy--Schwarz with
  $\|\Psi\|^2 = v_\Psi$ proves the bound. No rough occupation is inserted into a
  stochastic flow. This proves Lemma~\ref{L:occupation-raw-square}.
\end{proof}

\begin{proposition}[Original occupation energy and dilation]
  \label{P:raw-occupation-energy}
  With $K_0 = 2^a/(1-a)$,
  \[
    0<C_{\rm occ}\le K_0R_{\mathrm{sp}}<\infty .
  \]
  Moreover,
  \begin{align}
    \mathcal{E}_\zeta^{\mathcal{O}}
    &=D_\zeta C_{\rm occ}^{2/(2-\alpha)},&
    D_\zeta&=\frac{2-\alpha}{2}
    \left(\frac{\alpha}{2\zeta}\right)^{\alpha/(2-\alpha)},
    \label{E:raw-occupation-energy}\\
    C_{\rm occ}
    &=\left(\frac{2\mathcal{E}_\zeta^{\mathcal{O}}}{2-\alpha}\right)^{(2-\alpha)/2}
    \left(\frac{2\zeta}{\alpha}\right)^{\alpha/2}.
    \label{E:raw-occupation-ratio}
  \end{align}
  In particular, $\mathcal{E}_\zeta^{\mathcal{O}} > 0$ is finite and equals
  $\zeta^{-\alpha/(2-\alpha)}\mathcal{E}_1^{\mathcal{O}}$.
\end{proposition}

\begin{proof}
  A unit $H^1$ profile has positive gradient energy: a zero weak gradient makes
  it constant, and an $L^2$ constant on $\R^d$ is zero. Hence, $0 < T(g) <
  \infty$. Spatial covariance Cauchy--Schwarz gives $B_\Gamma(g_s^2,g_t^2) \le
  R_{\mathrm{sp}}b_s^{\alpha/4}b_t^{\alpha/4}$. Schur with row bound $K_0$, then
  concavity, proves
  \begin{equation}\label{E:raw-occupation-bound}
    0\le A(g)\le K_0R_{\mathrm{sp}}T(g)^{\alpha/2}.
  \end{equation}
  A fixed compact smooth unit profile, constant in time, belongs to
  $\mathcal{O}$ and has positive $A$ by Proposition~\ref{P:spatial-four-linear}.
  This proves positivity and finiteness of $C_{\rm occ}$.

  The map $(U_\ell g)_s(x) = \ell^{d/2}g_s(\ell x)$ is an $H^1$ isomorphism
  preserving unit mass and strong measurability. It has inverse $U_{1/\ell}$ and
  is a bijection on $\mathcal{O}$. The physical Radon change of variables gives
  \[
    A(U_\ell g)=\ell^\alpha A(g),\qquad
    T(U_\ell g)=\ell^2T(g).
  \]
  Indeed, the two densities contribute $\ell^{2d}$, $\ud x$ contributes
  $\ell^{-d}$, and the pushforward of $\Gamma$ contributes $\ell^{\alpha-d}$.
  Approximation extends the identity to full $H^1$. Taking the union over
  $g,\ell$ leaves the class unchanged. For fixed $A,T > 0$, the derivative of
  $A\ell^\alpha-\zeta T\ell^2$ has the sign of $\alpha A-2\zeta
  T\ell^{2-\alpha}$. Its global maximum occurs at $\ell = (\alpha A/(2\zeta
  T))^{1/(2-\alpha)}$ and equals $D_\zeta[A/T^{\alpha/2}]^{2/(2-\alpha)}$. For
  $A = 0$ the supremum is zero as $\ell\downarrow0$. Bounding every ratio by
  $C_{\rm occ}$ gives one inequality in~\eqref{E:raw-occupation-energy}. Fixed
  ratios approaching its positive supremum give the other by continuity of the
  positive power. Algebra gives~\eqref{E:raw-occupation-ratio} and the penalty
  scaling. No optimizer or minimax interchange is assumed. This proves
  Proposition~\ref{P:raw-occupation-energy}.
\end{proof}

\begin{lemma}[Countable Rayleigh near-occupations]
  \label{L:occupation-rayleigh-selection}
  For fixed $\Psi \in \mathcal{C}_{\mathrm{pos}}$ and every $\varepsilon > 0$
  there is $g_\varepsilon \in \mathcal{O}$ such that
  \begin{equation}\label{E:occupation-rayleigh-selection}
    I_\Psi^2+T(g_\varepsilon)
    \le\sqrt{v_\Psi A(g_\varepsilon)}+\varepsilon .
  \end{equation}
\end{lemma}

\begin{proof}
  The real $H^1$ space is separable, for example by its isometric embedding
  $f\mapsto(f,\nabla f)$ into a finite product of $L^2$ spaces. Compact smooth
  density therefore supplies a countable real family. Discard zero and normalize
  each member in $L^2$ to obtain $f_j$ dense in the $L^2$-unit $H^1$ class.
  Normalization preserves convergence because the approximating $L^2$ norms tend
  to one. Put $b_j = \|\nabla f_j\|_2^2$ and $R_j(s) = \int
  h_{\Psi,s}f_j^2-b_j$. Bounded-potential form continuity and
  Proposition~\ref{P:variational-unmasked-rate} give $\lambda_{\Psi,s}^2 =
  \sup_jR_j(s)$. The canonical functions are measurable, indeed continuous. Let
  $U_j = \{s:R_j(s)>\lambda_{\Psi,s}^2-\varepsilon\}$, $A_1 = U_1$ and $A_j =
  U_j\setminus\bigcup_{i<j}U_i$. These first-index cells are Borel and cover
  $I$. Put $g_\varepsilon(s) = f_j$ on $A_j$. Finite-valued truncations using
  $f_1$ on the remaining cells converge pointwise in $H^1$, proving strong
  measurability. A null-set representative may be filled by $f_1$.

  With $H_\Psi = \sup_{s,x}h_{\Psi,s}(x) < \infty$, the selection implies
  \[
    b(g_\varepsilon(s))
    <\int h_{\Psi,s}g_\varepsilon(s)^2-\lambda_{\Psi,s}^2+\varepsilon
    \le H_\Psi+\varepsilon .
  \]
  Thus, it belongs to the $\mathcal{O}$. Integrating the near-Rayleigh
  inequality, using Lemma~\ref{L:occupation-raw-square}, gives
  \[
    \int_I\lambda_{\Psi,s}^2\ud s+T(g_\varepsilon)
    \le\langle\Psi,\rho_{g_\varepsilon}\rangle+\varepsilon
    \le\sqrt{v_\Psi A(g_\varepsilon)}+\varepsilon .
  \]
  Time Cauchy--Schwarz on the unit interval gives $I_\Psi^2 \le
  \int_I\lambda_{\Psi,s}^2\ud s$. This
  proves~\eqref{E:occupation-rayleigh-selection}. No eigenvector, continuum
  selector or limiting occupation is required. This proves
  Lemma~\ref{L:occupation-rayleigh-selection}.
\end{proof}

For $0 \le b < q/2$ define $F_b(0) = 0$ and
\begin{equation}\label{E:occupation-scalar-map}
  F_b(z)=k\left[
  \frac{(q-2b)^{(q-2b)/2}}{8(q-b)^{q-b}}
  \left(\frac{2z}{2-\alpha}\right)^{(2-\alpha)/2}
  \right]^{1/k},\qquad z>0.
\end{equation}
At $b = 0$ this is exactly the map in~\eqref{E:spatial-static-energy-score}. The
display parameter $b$ does not change the temporal exponent $a$.

\begin{theorem}[The computed occupation ceiling]\label{T:intrinsic-occupation-ceiling}
  For every variational value over nonnegative controls coefficient
  $\mathfrak{c}$,
  \begin{align}
    S_{\mathfrak{c}}^{\mathrm{pos}}
    &\le U_{\mathfrak{c}}
    :=\mathfrak{c}^m k
    \left[\frac{\alpha^{\alpha/2}C_{\rm occ}}{8q^{q/2}}\right]^{1/k}
    \label{E:occupation-score-ceiling}\\
    &=\mathfrak{c}^m(2\zeta)^{\alpha/(2k)}
    F_0(\mathcal{E}_\zeta^{\mathcal{O}}),\qquad \zeta>0.\notag
  \end{align}
  In particular, the original moment constant satisfies $C_2(\Gamma,a) \le U_2$
  for every original model. This ceiling is not asserted to be attained or equal
  to $C_2$.
\end{theorem}

\begin{proof}
  Fix $\Psi$ and write $v = v_\Psi$, $C = C_{\rm occ}$ and $\beta = \alpha/4$.
  Lemma~\ref{L:occupation-rayleigh-selection} gives $I_\Psi^2 \le
  \sqrt{vC}T^\beta-T+\varepsilon$ for some $T > 0$. Bound it by the supremum
  over all $T \ge 0$ before sending $\varepsilon\downarrow0$. If $v = 0$, that
  supremum is zero. If $v > 0$, the derivative $\beta\sqrt{vC}T^{\beta-1}-1$
  strictly decreases from infinity to $-1$. Its unique positive zero is $T_* =
  (\beta\sqrt{vC})^{1/(1-\beta)}$. The global maximum equals
  $(q/4)(\alpha/4)^{\alpha/q}(vC)^{2/q}$. In both cases,
  \[
    I_\Psi\le Dv^{1/q},\qquad
    D=\sqrt{q/4}(\alpha/4)^{\alpha/(2q)}C^{1/q}.
  \]
  The scalar function $\mathfrak{c} Dv^{1/q}-v/2$ vanishes at zero, tends to
  minus infinity, and has strictly decreasing derivative. Its unique positive
  maximum is at $v_* = (2\mathfrak{c} D/q)^{q/k}$, with value $kv_*/2$. Direct
  positive-power algebra gives
  \[
    (2D/q)^q=q^{-q/2}(\alpha/4)^{\alpha/2}C .
  \]
  Since $k+\alpha = 3$, the maximum is precisely $U_{\mathfrak{c}}$
  in~\eqref{E:occupation-score-ceiling}, with denominator eight. Substitution
  of~\eqref{E:raw-occupation-ratio} gives the second form, retaining the factor
  $(2\zeta)^{\alpha/(2k)}$. Take the supremum over the smooth positive-control
  class. Theorem~\ref{T:intrinsic-second-moment} identifies $C_2 =
  S_2^{\mathrm{pos}}$, proving the moment ceiling. The penalty factor cancels
  its energy scaling, so the ceiling is independent of $\zeta$. This proves
  Theorem~\ref{T:intrinsic-occupation-ceiling}.
\end{proof}

\begin{corollary}[A common spatial-energy bracket]
  \label{C:intrinsic-spatial-bracket}
  With the same original covariance and $M_a$
  of~\eqref{E:temporal-equilibrium-mass},
  \begin{equation}\label{E:intrinsic-spatial-bracket}
    2^m M_a^{-1/k}F_0(\mathcal{E}_{\mathrm{sp}})
    \le C_2(\Gamma,a)
    \le2^m K_0^{1/k}F_0(\mathcal{E}_{\mathrm{sp}}).
  \end{equation}
  For $\Gamma \ne 0$ there is also the comparison of the energies defined here
  \[
    C_2\le2^mF_0(\mathcal{E}_{1/2}^{\mathcal{O}})
    <2^mF_a(\mathcal{E}_{1/2}^{\mathcal{O}}).
  \]
\end{corollary}

\begin{proof}
  Insert $C_{\rm occ} \le K_0R_{\mathrm{sp}}$ into
  \eqref{E:occupation-score-ceiling} and use \eqref{E:spatial-energy-map}. This
  gives the upper bracket; the lower is \eqref{E:spatial-static-energy-score}
  multiplied by $2^m$, using Theorem~\ref{T:intrinsic-second-moment}. Both
  concern one common spatial energy, not an assumed first moment.

  For completeness put
  \[
    \Delta=\tfrac12[q\log q+(q-2a)\log(q-2a)]
    -(q-a)\log(q-a)>0.
  \]
  Here $a > 0$ and $q-2a > 2-a > 1$. The scalar inequality for the difference of
  logarithms applies at exactly these conditions, without $q \ge 3$.
  Equivalently the strict midpoint convexity of $x\log x$ on positive arguments,
  whose second derivative is $1/x$, gives the sign. Subtracting logarithms
  in~\eqref{E:occupation-scalar-map} gives
  \[
    \log(F_a(z)/F_0(z))=\Delta/k,\qquad
    \frac{\mathfrak{c}^mF_a(\mathcal{E}_\zeta^{\mathcal{O}})}{U_{\mathfrak{c}}}
    =\exp\!\left(\frac{\Delta-(\alpha/2)\log(2\zeta)}{k}\right).
  \]
  At $\zeta = 1/2$ this and the ceiling prove the strict comparison. At $\zeta =
  1$ the comparison is not universally favorable. For $\alpha = 5/4,a = 1/2,d =
  2$,
  \[
    8[\Delta-(\alpha/2)\log2]
    =\log\frac{11^{11}7^7}{2^5 9^{18}}<0,
  \]
  since $11^{11}7^7 = 234966429149994773$ and $2^5 9^{18} =
  4803028329503971872$. This contrasts computed bounds; it refutes no moment
  inequality. This proves Corollary~\ref{C:intrinsic-spatial-bracket}.
\end{proof}

The kinetic normalization matters in this comparison.
No-go~\ref{P:nogo-28} shows that changing it can reverse an ordering
between the computed ceiling and a comparison value. That example makes
no claim about the ordering of the actual moment constant.


For $\Gamma = 0$, all original means and variational values vanish and $C_2 =
0$. Here $Q = 0$, $A = 0$ and $C_{\rm occ} = 0$. The supremum of $-\zeta T(g)$
is zero: dilate a fixed unit compact profile by $\ell^{d/2}f(\ell x)$ and let
$\ell\downarrow0$. The same argument gives $\mathcal{E}_{\mathrm{sp}} = 0$ and
the earlier damped energy zero, without using a zero vector as a unit profile.
With $F_b(0) = 0$, every non-strict bound above is the zero identity. These
energies are not identified with Chen's printed energies.

# notes/integrated_spatial_occupation.tex

\section{Physical spatial pairings and the full occupation class}
\label{S:spatial-occupation-foundation}

Retain a nonzero original covariance from Hypothesis~\ref{H:homog} with its
amplitude. Set $a = \alpha_0$, $k = 3-\alpha > 1$, $q = 4-\alpha = k+1$ and $D =
q-2a > 0$. The scalar $D$ is fixed. All profiles are real. The original positive
temporal exponent and threshold imply $\alpha < 2$; this is the strict
inequality used in the scalar powers and concavity. The finite variational value
over nonnegative controls $S_1^{\mathrm{pos}}$ is that of
Proposition~\ref{P:variational-positive-scores}.

\begin{lemma}[The physical two-point integral]\label{L:spatial-physical-pair}
  The positive measure $\nu(\ud x,\ud y) = \ud x\,\Gamma(\ud y)$ is
  sigma-finite. For nonnegative functions define
  \begin{equation}\label{E:spatial-physical-pair}
    B_\Gamma(f,h)=\int f(x)h(x-y)\nu(\ud x,\ud y)
  \end{equation}
  initially as an extended nonnegative integral, using finite Borel
  representatives of Lebesgue classes. Its value is representative independent.
  Lebesgue-a.e. convergence transfers to $\nu$-a.e. convergence at both
  positions $x$ and $x-y$.
\end{lemma}

\begin{proof}
  Local finiteness of $\Gamma$ gives sigma-finiteness on exhausting balls, and
  Lebesgue measure is sigma-finite. If $N$ is Borel and Lebesgue null, Tonelli
  applied first in $x$ gives $\nu\{x\in N\} = 0$ and $\nu\{x-y\in N\} = 0$,
  because every fixed translate of $N$ is null. An arbitrary Lebesgue null set
  has a Borel null superset. Thus, arbitrary versions are measurable in the
  $\nu$ completion with the same value, and the same observation applies to the
  exceptional sets of a.e. convergence. Signed pairings will be used only after
  absolute convergence. This proves Lemma~\ref{L:spatial-physical-pair}.
\end{proof}

Put $A_{\mathrm{sp}}(g) = B_\Gamma(g^2,g^2)$ and $b(g) = \|\nabla g\|_2^2$ on
$H^1$; initially $A_{\mathrm{sp}}$ is used only for smooth compact profiles
before the extension below. For smooth compact $z$, write $U_z = \Gamma*z$ in
its usual pointwise sense.

\begin{lemma}[Smooth temporal controls]\label{L:spatial-static-controls}
  For every nonnegative nonzero $z \in C_c^\infty(\R^d)$, let
  \[
    \lambda_z(c)^2=
    \sup_{\substack{g\in H^1(\R^d;\R)\\\|g\|_2=1}}
    \left(c\int U_zg^2-b(g)\right),\qquad c>0.
  \]
  This is positive and finite, and $\lambda_z$ is Lipschitz on every compact
  positive $c$ interval. With the exact $M_a$
  in~\eqref{E:temporal-equilibrium-mass},
  \begin{equation}\label{E:spatial-static-score}
    S_1^{\mathrm{pos}}\ge
    \lambda_z(1)-\frac{M_a}{2}B_\Gamma(z,z).
  \end{equation}
\end{lemma}

\begin{proof}
  Choose nonnegative nonzero $f \in C_c^\infty(0,1)$ and $s_0 = 1/2$. Let
  $k_f(s_0) = \int_0^1|s_0-t|^{-a}f(t)\ud t > 0$. The smooth test $\Psi(t,x) =
  cf(t)z(x)/k_f(s_0)$ has mean $cU_z$ at $s_0$.
  Proposition~\ref{P:variational-unmasked-rate} gives boundedness of this
  potential, the displayed real Rayleigh formula, and a positive rate for every
  $c > 0$. Comparing identical unit tests makes $\lambda_z(c)^2$ Lipschitz with
  constant $\|U_z\|_\infty$. On a positive compact interval its rate has a
  positive floor by monotonicity, giving the square-root Lipschitz bound.

  Use the nonincreasing smooth cutoff $\chi$ constructed in the proof of
  Proposition~\ref{P:variational-remove-mask}. For integers $n \ge 4$, set on
  $(0,1)$
  \[
    f_n(t)=f_a(t)\chi(1/(nt))\chi(1/(n(1-t))),\qquad
    k_n(s)=\int_0^1|s-t|^{-a}f_n(t)\ud t.
  \]
  Extend $f_n$ by zero. It is smooth compact, vanishes near both endpoints, is
  nonzero, and increases to $f_a$. Thus, $\Psi_n = f_n\otimes z$ is a positive
  smooth control. Monotone convergence
  and~\eqref{E:temporal-equilibrium-potential} give $k_n(s)\uparrow1$ for every
  $s \in [0,1]$. Since the kernel is at least one on the unit square off its
  null diagonal, $0 < c_0: = \int_0^1f_4 \le k_n(s) \le 1$. The mean is
  $k_n(s)U_z$; hence its rate is $\lambda_z(k_n(s))$, converging to
  $\lambda_z(1)$ and bounded by that finite number. Dominated convergence gives
  $I_{\Psi_n} \to \lambda_z(1)$.

  The Gaussian cost is exactly the nonnegative Tonelli pairing
  \[
    v_{\Psi_n}=B_\Gamma(z,z)\int_0^1f_n(s)k_n(s)\ud s.
  \]
  Its time integrand increases to $f_a$, so the cost tends to
  $M_aB_\Gamma(z,z)$. The spatial factor is finite and positive: its smooth
  compact autocorrelation is positive near zero, and homogeneity scales any
  origin-centered ball of positive $\Gamma$ mass to every other positive radius.
  Such a ball exists by exhaustion. Take the limit of the individual
  inequalities $S_1^{\mathrm{pos}} \ge I_{\Psi_n}-v_{\Psi_n}/2$. The variational
  expression differences need not increase. No control depends on original large
  time and no rough stochastic evolution has been used. This proves
  Lemma~\ref{L:spatial-static-controls}.
\end{proof}

The next estimate also allows zero covariance and does not use the finiteness
of $S_1^{\mathrm{pos}}$.

\begin{lemma}[Deterministic Fourier bound for the spatial energy]
  \label{L:spatial-fourier-bound}
  Under Hypothesis~\ref{H:homog}, allowing $\Gamma=0$, let
  $g\in C_c^\infty(\R^d;\R)$ satisfy $\|g\|_2=1$ and put
  $b=\|\nabla g\|_2^2$. Then $b>0$ and
  \begin{equation}\label{E:spatial-fourier-bound}
    0\le A_{\mathrm{sp}}(g)
    \le 2^{1+\alpha}R_\alpha b^{\alpha/2},
  \end{equation}
  where $R_\alpha$ is defined in~\eqref{E:intro-spectral-mass}.
\end{lemma}

\begin{proof}
  If $b=0$, smoothness makes $\nabla g=0$ everywhere. Thus, $g$ is constant,
  and compact support forces $g=0$, contrary to $\|g\|_2=1$. Put $Q=g^2$ and
  use the unnormalized Fourier transform
  \[
    \mathcal{F}_0Q(\xi)=\int_{\R^d}e^{-i\xi\cdot x}Q(x)\ud x.
  \]
  In the unitary convention of Section~\ref{S:masked-covariance}, this is
  $c_d^{-1}\widehat Q$, with $c_d=(2\pi)^{-d/2}$.
  The autocorrelation
  \[
    c_Q(y)=\int_{\R^d}Q(x)Q(x-y)\ud x
  \]
  is smooth and compactly supported. Apply the distributional spectral
  identity~\eqref{E:masked-spectral-convention} to this Schwartz function.
  Its inner Fourier integral is $|\mathcal{F}_0Q(\xi)|^2$, since $Q$ is real.
  Hence
  \[
    A_{\mathrm{sp}}(g)=\int c_Q(y)\Gamma(\ud y)
    =\int|\mathcal{F}_0Q(\xi)|^2\mu(\ud\xi).
  \]
  Both integrals are finite: $c_Q$ is compactly supported and $\Gamma$ is
  Radon, while $|\mathcal{F}_0Q|^2$ is Schwartz and $\mu$ is tempered.
  No density of either measure is required.

  Since $\|Q\|_1=1$, we have $|\mathcal{F}_0Q|\le1$. Integration by parts
  and the Cauchy--Schwarz inequality give
  \[
    |\xi|\,|\mathcal{F}_0Q(\xi)|
    \le\|\nabla Q\|_1
    \le2\|g\|_2\|\nabla g\|_2=2\sqrt b.
  \]
  Splitting into $|\xi|^2\le4b$ and $|\xi|^2>4b$ therefore yields
  \[
    |\mathcal{F}_0Q(\xi)|^2\le\frac{8b}{4b+|\xi|^2}.
  \]
  The deterministic resolvent calculation in the proof of
  Lemma~\ref{L:damped-homogeneous-norms}, together
  with~\eqref{E:intro-spectral-mass}, gives, for $q>0$,
  \[
    \mathcal{R}_\Gamma(q):=\int\frac{\mu(\ud\xi)}{q^2+|\xi|^2}
    =q^{\alpha-2}R_\alpha<\infty.
  \]
  Consequently,
  \[
    A_{\mathrm{sp}}(g)\le8b\mathcal{R}_\Gamma(2\sqrt b)
    =2^{1+\alpha}R_\alpha b^{\alpha/2}.
  \]
  Nonnegativity follows from the spectral identity. If $\Gamma=0$, then
  $\mu=0$ and both sides of~\eqref{E:spatial-fourier-bound} vanish. This proves
  Lemma~\ref{L:spatial-fourier-bound}.
\end{proof}

\begin{proposition}[The finite smooth spatial ratio]
  \label{P:spatial-smooth-ratio}
  For real unit $g \in C_c^\infty(\R^d)$ put $R(g) =
  A_{\mathrm{sp}}(g)/b(g)^{\alpha/2}$. Its supremum $R_0$ over these profiles is
  a positive finite real number, and
  \begin{equation}\label{E:spatial-smooth-score}
    S_1^{\mathrm{pos}}\ge
    k\left[
    \frac{R(g)\alpha^{\alpha/2}}{8M_aq^{q/2}}
    \right]^{1/k}.
  \end{equation}
\end{proposition}

\begin{proof}
  The gradient energy $b(g)$ is positive: a nonzero $L^2$ function with zero
  weak gradient would have Fourier transform supported only at zero, and hence
  would vanish. Its square is nonnegative nonzero smooth compact, so the
  autocorrelation argument in the proof of
  Lemma~\ref{L:spatial-static-controls} gives
  $0 < A:=A_{\mathrm{sp}}(g)<\infty$. Lemma~\ref{L:spatial-fourier-bound} gives
  $R(g)\le2^{1+\alpha}R_\alpha$ for every such profile. A normalized compact
  bump supplies a positive ratio. Thus, $0<R_0<\infty$, independently of the
  finiteness of $S_1^{\mathrm{pos}}$. It remains to prove the score inequality.
  With $U_\ell g(x)=\ell^{d/2}g(\ell x)$, the physical changes of variables give
  \begin{equation}\label{E:spatial-dilation}
    A_{\mathrm{sp}}(U_\ell g)=\ell^\alpha A,\qquad
    b(U_\ell g)=\ell^2b(g).
  \end{equation}
  The factors in the first identity are $\ell^{2d}$ from the two squares,
  $\ell^{-d}$ from $\ud x$, and $\ell^{\alpha-d}$ from the Radon pushforward.

  For $\theta,\ell > 0$ choose the smooth control $z = \theta(U_\ell g)^2$. The
  Rayleigh test $U_\ell g$ gives $\lambda_z(1)^2 \ge \theta\ell^\alpha
  A-\ell^2b$, while $B_\Gamma(z,z) = \theta^2\ell^\alpha A$. For any $L > 0$,
  put $u = \alpha/q > 0$ and choose
  \[
    \ell^2=uL^2/b,\qquad
    \theta=(1+u)L^2/(\ell^\alpha A).
  \]
  The radicand is $L^2$. Lemma~\ref{L:spatial-static-controls} consequently
  gives
  \[
    S_1^{\mathrm{pos}}\ge L-CL^q,\qquad
    C=\frac{M_a(1+u)^2}{2R(g)u^{\alpha/2}}>0.
  \]
  Its maximum occurs at $L^k = 1/(qC)$ and is $(k/q)(qC)^{-1/k}$. Since $1+u =
  4/q$, $1/(q^qC) = R(g)\alpha^{\alpha/2}/(8M_aq^{q/2})$,
  proving~\eqref{E:spatial-smooth-score}. This argument retains the finite
  real value $S_1^{\mathrm{pos}}$ fixed at the start of the section; only the
  proof of $R_0<\infty$ is independent of that input. This proves
  Proposition~\ref{P:spatial-smooth-ratio}.
\end{proof}

\begin{proposition}[The physical four-linear extension]
  \label{P:spatial-four-linear}
  For real $f \in H^1(\R^d)$ define $N(f) = \|f\|_2^{1-\alpha/4}\|\nabla
  f\|_2^{\alpha/4}$. Every physical square pairing is finite and
  \begin{align}
    A_{\mathrm{sp}}(f)&\le R_0N(f)^4,\label{E:spatial-homogeneous-bound}\\
    0\le B_\Gamma(f^2,h^2)
    &\le\sqrt{A_{\mathrm{sp}}(f)A_{\mathrm{sp}}(h)}.
    \label{E:spatial-square-CS}
  \end{align}
  The signed integral $C_4(f_1,f_2,f_3,f_4) = B_\Gamma(f_1f_2,f_3f_4)$ is
  absolutely convergent and jointly continuous on $(H^1)^4$, with
  \begin{equation}\label{E:spatial-four-linear}
    \int|f_1(x)f_2(x)f_3(x-y)f_4(x-y)|\ud\nu
    \le R_0\prod_{j=1}^4N(f_j).
  \end{equation}
  The ratio supremum $R_{\mathrm{sp}}$ over all real unit $H^1$ profiles equals
  $R_0$. Every nonzero $H^1$ profile has $A_{\mathrm{sp}}(f) > 0$.
\end{proposition}

\begin{proof}
  For smooth compact $f$, normalization in $R_0$ proves
  \eqref{E:spatial-homogeneous-bound}, including $f = 0$. All exponents in $N$
  are positive and $N(f) \le \|f\|_{H^1}$. For smooth compact signed $Q,P$, the
  absolute correlation is compactly supported and bounded by $\|Q\|_2\|P\|_2$.
  Local finiteness of $\Gamma$ therefore makes its physical integral finite.
  Smooth signed covariance is positive: with the ordinary transform
  $\widehat{Q}_{\mathrm{ord}}(\xi) = \int e^{i\xi\cdot x}Q(x)\ud x$, the model
  convention gives
  \[
    B_\Gamma(Q,Q)=\int|\widehat{Q}_{\mathrm{ord}}(\xi)|^2\mu(\ud\xi)
    \ge0,\qquad Q\in C_c^\infty(\R^d;\R).
  \]
  Pair $\Gamma$ with the smooth compact correlation to obtain this identity;
  rapid Fourier decay and tempered $\mu$ give finiteness. Evenness of $\Gamma$
  and $(x,y)\mapsto(x-y,-y)$ give symmetry. The quadratic polynomial for $Q+tP$
  gives covariance Cauchy--Schwarz. In particular, for smooth real $f,h$,
  \[
    0\le B_\Gamma(f^2,h^2)
    \le R_0N(f)^2N(h)^2.
  \]
  The squares of signed smooth profiles are already smooth and nonnegative.

  Smooth compact functions are dense in $H^1$. Cutoffs equal to one on the
  radius-$R$ ball, vanishing beyond $2R$ and with gradient at most $C/R$,
  converge by the function and gradient tails and the bound $C\|f\|_2/R$ for the
  extra gradient term. Mollification then converges in $H^1$ by $L^2$
  translation continuity of the function and its weak gradients. The space is
  separable through its closed isometric image $f\mapsto(f,\nabla f)$ in
  $L^2(\R^d)^{d+1}$.

  For arbitrary $f,h \in H^1$ take smooth approximants converging in $H^1$ and
  along a common subsequence Lebesgue-a.e. Lemma~\ref{L:spatial-physical-pair}
  transfers this convergence at both positions to $\nu$-a.e. convergence. Fatou
  and continuity of $N$ give $B_\Gamma(f^2,h^2) \le R_0N(f)^2N(h)^2 < \infty$,
  including the diagonal bound. At this stage Fatou supplies an inequality, not
  continuity.

  Apply ordinary Cauchy--Schwarz under the positive measure $\nu$ to
  $f_1(x)f_3(x-y)$ and $f_2(x)f_4(x-y)$. The two squared integrals are finite by
  the last bound; their square root is at most $R_0\prod_jN(f_j)$. This
  proves~\eqref{E:spatial-four-linear}, absolute convergence and multilinearity.
  Telescoping a difference one argument at a time and using $N(f) \le
  \|f\|_{H^1}$ proves joint continuity. Thus, $A_{\mathrm{sp}}$ and the square
  pairings are continuous. PSD for smooth compact profiles passes to finite
  linear combinations of $H^1$ squares by this continuity, and its two-profile
  Cauchy--Schwarz gives \eqref{E:spatial-square-CS}. This completes the physical
  pairing argument beyond Fatou.

  Every real unit $H^1$ profile has positive gradient energy by the Fourier
  argument above. The homogeneous bound gives $R_{\mathrm{sp}} \le R_0$, and
  smooth inclusion gives the reverse. Normalized smooth approximations preserve
  the ratio by continuity. Finally, for nonzero $f$, choose a bounded set $E$ of
  finite positive measure where $|f| \ge c > 0$. The correlation of $1_E$ is
  continuous and positive near zero by $L^2$ translation continuity. An
  origin-centered ball there has positive $\Gamma$ mass, so $A_{\mathrm{sp}}(f)
  \ge c^4B_\Gamma(1_E,1_E) > 0$. This uses a nonnegative integral, not an $H^1$
  claim for $1_E$. Finiteness was already proved. This proves
  Proposition~\ref{P:spatial-four-linear}.
\end{proof}

\begin{proposition}[The spatial energy and static lower variational expression]
  \label{P:spatial-energy-map}
  Over all real unit $H^1$ profiles define the energy
  \[
    \mathcal{E}_{\mathrm{sp}}
    =\sup_{\|g\|_2=1}
    \left(A_{\mathrm{sp}}(g)-\frac{b(g)}2\right).
  \]
  Then
  \begin{equation}\label{E:spatial-energy-map}
    \mathcal{E}_{\mathrm{sp}}
    =\frac{2-\alpha}{2}\alpha^{\alpha/(2-\alpha)}
    R_{\mathrm{sp}}^{2/(2-\alpha)}
    \in(0,\infty).
  \end{equation}
  In particular,
  \begin{equation}\label{E:spatial-static-energy-score}
    S_1^{\mathrm{pos}}\ge M_a^{-1/k}F_0(\mathcal{E}_{\mathrm{sp}}),
    \qquad
    F_0(z)=k\left[
    \frac{(2z/(2-\alpha))^{(2-\alpha)/2}}{8q^{q/2}}
    \right]^{1/k},\quad z>0.
  \end{equation}
  The subscript in $F_0$ labels this scalar map; the covariance retains its
  original temporal exponent $a$.
\end{proposition}

\begin{proof}
  Physical change of variables, or smooth approximation and
  Proposition~\ref{P:spatial-four-linear}, extends \eqref{E:spatial-dilation} to
  real $H^1$ profiles. For fixed unit $g$, with $A,b > 0$, the maximum of
  $\ell^\alpha A-\ell^2b/2$ occurs at $\ell^{2-\alpha} = \alpha A/b$ and equals
  \[
    \frac{2-\alpha}{2}\alpha^{\alpha/(2-\alpha)}
    R(g)^{2/(2-\alpha)}.
  \]
  Dilation preserves the whole unit class and includes $\ell = 1$. Taking both
  numerical suprema, then profiles with ratio tending to $R_{\mathrm{sp}}$,
  proves~\eqref{E:spatial-energy-map}. No optimizer is assumed. Smooth ratios
  also approach $R_{\mathrm{sp}}$ by Proposition~\ref{P:spatial-four-linear}.
  Pass them through~\eqref{E:spatial-smooth-score} and substitute
  \[
    R_{\mathrm{sp}}\alpha^{\alpha/2}
    =\left(\frac{2\mathcal{E}_{\mathrm{sp}}}{2-\alpha}
    \right)^{(2-\alpha)/2}.
  \]
  This gives~\eqref{E:spatial-static-energy-score}. This proves
  Proposition~\ref{P:spatial-energy-map}.
\end{proof}

\subsection{The kernel row and full occupation energy}

Define, for $u \ne 0$,
\begin{equation}\label{E:occupation-damped-kernel}
  K_\star(u)=\frac1{\Gamma_E(a)}
  \int_0^\infty
  e^{-(\lambda+\lambda^2/(2D))|u|}
  \lambda^{a-1}\ud\lambda,
\end{equation}
and set $K_\star(0) = 0$ for time integration.

\begin{lemma}[Exact row maximum]\label{L:occupation-kernel-row}
  The kernel is even, positive off zero, locally integrable, decreasing on
  $(0,\infty)$, and $K_\star(u) \le |u|^{-a}$ off zero. Its exact row maximum on
  $[0,1]$ is
  \begin{equation}\label{E:occupation-kernel-row}
    \max_{s\in[0,1]}\int_0^1K_\star(s-t)\ud t
    =R_\star:=2\int_0^{1/2}K_\star(u)\ud u\in(0,\infty).
  \end{equation}
\end{lemma}

\begin{proof}
  Dropping the positive quadratic damping bounds the mixture by the Gamma
  integral $|u|^{-a}$. Positivity and monotonicity follow directly from the
  integrand, and $a < 1$ gives local integrability. Put $\Phi(t) =
  \int_0^tK_\star(u)\ud u$. It is concave because its integrand is decreasing on
  positive arguments. The row is $\Phi(s)+\Phi(1-s) \le 2\Phi(1/2)$, with
  equality at $s = 1/2$. The diagonal value changes no time integral. This
  proves Lemma~\ref{L:occupation-kernel-row}.
\end{proof}

Let $\mathcal{O}$ be the full class of strongly $H^1(\R^d;\R)$-measurable fields
$s\mapsto g_s$ on $(0,1)$ with $\|g_s\|_2 = 1$ a.e. and $T(g) =
\int_0^1b(g_s)\ud s < \infty$. No time smoothness, common compact support or
optimizer condition is imposed.

\begin{proposition}[The full physical occupation class]
  \label{P:occupation-physical-class}
  The pairings $(s,t)\mapsto B_\Gamma(g_s^2,g_t^2)$ are measurable,
  representative independent and equal to their physical integrals. With
  \[
    J(g)=\int_0^1\int_0^1
    K_\star(s-t)B_\Gamma(g_s^2,g_t^2)\ud s\ud t,
  \]
  every $g \in \mathcal{O}$ satisfies
  \begin{equation}\label{E:occupation-physical-bound}
    0\le J(g)\le R_\star R_{\mathrm{sp}}T(g)^{\alpha/2}<\infty.
  \end{equation}
  The energy over exactly this full class satisfies
  \begin{equation}\label{E:occupation-own-energy}
    0<\mathcal{E}_\star^{\mathcal{O}}
    :=\sup_{g\in\mathcal{O}}\big(J(g)-T(g)/2\big)
    \le R_\star^{2/(2-\alpha)}\mathcal{E}_{\mathrm{sp}}<\infty.
  \end{equation}
\end{proposition}

\begin{proof}
  The map $s\mapsto b(g_s)$ is measurable by continuity of the squared gradient
  norm. Also $\int_0^1\|g_s\|_{H^1}^2\ud s = 1+T(g)$. Use a separably valued
  strong representative and replace exceptional null times by one fixed real
  unit compact bump. Joint measurable spatial representatives exist: approximate
  this Bochner $L^2$ field by simple $H^1$-valued functions with summable
  $L^2(0,1;H^1)$ errors, and choose measurable spatial versions for their
  countably many values. A subsequence has a measurable spacetime $L^2$ limit,
  and for a.e. $s$ its spatial $L^2$ class is $g_s$.
  Lemma~\ref{L:spatial-physical-pair} makes every pairing independent of the
  spatial versions. The continuous pairing map on the separable space $H^1\times
  H^1$ from Proposition~\ref{P:spatial-four-linear} consequently gives a
  measurable function of $(s,t)$ agreeing a.e. with the nonnegative physical
  integral.

  Set $F(s) = b(g_s)^{\alpha/4}$. Equations~\eqref{E:spatial-homogeneous-bound}
  and~\eqref{E:spatial-square-CS} give $B_\Gamma(g_s^2,g_t^2) \le
  R_{\mathrm{sp}}F(s)F(t)$. Since $0 < \alpha/2 < 1$, concavity on the unit time
  interval yields $\int_0^1F^2 = \int_0^1b(g_s)^{\alpha/2}\ud s \le
  T(g)^{\alpha/2}$. Now use $2F(s)F(t) \le F(s)^2+F(t)^2$ and the exact row
  bound \eqref{E:occupation-kernel-row}, whose column bound is the same because
  $K_\star$ is even, to obtain \eqref{E:occupation-physical-bound}. Positive
  Tonelli is valid before finiteness is known. Null-time modifications affect
  only a product-null set, so they cannot change $J$.

  The scalar maximum of $R_\star R_{\mathrm{sp}}T^{\alpha/2}-T/2$ over $T \ge 0$
  is $R_\star^{2/(2-\alpha)}\mathcal{E}_{\mathrm{sp}}$, by the same
  differentiation as~\eqref{E:spatial-energy-map}. This bounds the occupation
  supremum from above. For positivity take a constant-in-time unit compact
  profile and its spatial dilation $U_\ell$. Its $J$ is $J_0\ell^\alpha
  A_{\mathrm{sp}}(g)$, where $J_0 = \int_0^1\int_0^1K_\star(s-t)\ud s\ud t \in
  (0,\infty)$, while $T = \ell^2b(g)$. For sufficiently small $\ell > 0$,
  $\alpha < 2$ makes $J-T/2 > 0$. Thus, the nonempty supremum is a positive
  finite real number. This is a comparison bound; no attaining profile or
  equality in it has been asserted. No spatial point trace or rough stochastic
  evolution was used. This proves Proposition~\ref{P:occupation-physical-class}.
\end{proof}

For zero covariance all spatial pairings vanish and set $R_{\mathrm{sp}} = 0$.
The spatial and occupation energies are zero suprema of $-b/2$ and $-T/2$: small
spatial dilations of one fixed unit compact profile make these energies tend to
zero, with the profile constant in time for the latter. No zero-gradient unit
state is used. The temporal identities remain valid, and the moment model is the
free case already treated.

# notes/integrated_compact_gaussian.tex

\section{Finite Gaussian moments and whole-space Sobolev compactness}
\label{S:compact-gaussian}

We prove the finite Gaussian and compact-cutoff estimates needed to construct
the wave operator path. All traces and Schatten norms in this section are
unnormalized. The spatial states remain on $\R^d$, $d \in \{1,2,3\}$. Here $p$
is an auxiliary Schatten and Gaussian-moment index. The auxiliary periodic space
below is used only to factor a compactly supported multiplication operator. No
infinite Gaussian series or time path is constructed in this section.

\subsection{Finite Gaussian matrices with both variance powers}

\begin{lemma}[Scalar power estimates]\label{L:gaussian-scalar-powers}
  For $0 < \theta < 1$ and $u,v \ge 0$,
  \begin{equation}\label{E:gaussian-weighted-power}
    u^\theta v^{1-\theta} \le \theta u+(1-\theta)v.
  \end{equation}
  Consequently, if $L > 0$ and $0 \le q \le L$ are integers, then for real
  $x,y$,
  \begin{equation}\label{E:gaussian-integer-power}
    |x|^q|y|^{L-q}
    \le \frac qL|x|^L+\frac{L-q}L|y|^L.
  \end{equation}
  For nonnegative finite sequences, the usual H\"older inequality holds with
  exponents $m$ and $m/(m-1)$, $m > 1$. If $Z \ge 0$ has finite expectation $F$
  and $0 < r < 1$, then $\E Z^r \le F^r$.
\end{lemma}

\begin{proof}
  If $v > 0$, divide~\eqref{E:gaussian-weighted-power} by $v$ and put $t = u/v$.
  The function $\theta t+1-\theta-t^\theta$ decreases to zero at one and then
  increases, by its derivative $\theta(1-t^{\theta-1})$. Continuity covers $t =
  0$; if $v = 0$ the inequality is immediate. For $0 < q < L$, apply this with
  $u = |x|^L$, $v = |y|^L$ and $\theta = q/L$. The endpoint cases $q = 0,L$ are
  identities, with the ordinary integer convention $a^0 = 1$.

  To prove finite H\"older, divide the two sequences by their respective
  $\ell^m$ and $\ell^{m/(m-1)}$ norms. If either norm vanishes, the result is
  immediate. Apply~\eqref{E:gaussian-weighted-power} with $\theta = 1/m$ to the
  corresponding normalized powers and sum; the sum of products is at most one.
  Undo the normalization. Finally, $F = 0$ gives $Z = 0$ almost surely. If $F >
  0$, apply \eqref{E:gaussian-weighted-power} to $u = Z/F$, $v = 1$ and $\theta
  = r$, and integrate. The right side has expectation one. This proves
  Lemma~\ref{L:gaussian-scalar-powers}.
\end{proof}

\begin{lemma}[Two Hermitian trace bounds]\label{L:gaussian-trace-bounds}
  Let $B,Y$ be finite Hermitian matrices, $m \ge 2$ an integer, and $L = 2m-2$.
  For integers $0 \le q \le L$,
  \begin{equation}\label{E:gaussian-trace-word}
    \operatorname{Re}\operatorname{Tr}(BY^qBY^{L-q})
    \le \operatorname{Tr}(B^2|Y|^L).
  \end{equation}
  If $D \ge 0$ is Hermitian, then
  \begin{equation}\label{E:gaussian-trace-holder}
    \operatorname{Tr}(D|Y|^{2m-2})
    \le (\operatorname{Tr}D^m)^{1/m}
    (\operatorname{Tr}|Y|^{2m})^{(m-1)/m}.
  \end{equation}
\end{lemma}

\begin{proof}
  Diagonalize $Y$, with real eigenvalues $\lambda_i$, and write $b_{ij}$ for the
  entries of $B$ in that basis. Hermitian symmetry gives $b_{ji} =
  \overline{b_{ij}}$. The trace word is the real sum
  \[
    \sum_{i,j}|b_{ij}|^2\lambda_j^q\lambda_i^{L-q}.
  \]
  Bound each product by its absolute value and use
  \eqref{E:gaussian-integer-power}. After interchanging $i,j$, the two resulting
  sums agree because $|b_{ij}| = |b_{ji}|$. Each equals
  $\sum_{i,j}|b_{ij}|^2|\lambda_i|^L = \operatorname{Tr}(B^2|Y|^L)$. The two
  weights sum to one, proving \eqref{E:gaussian-trace-word}. No commutation of
  $B$ and $Y$ is used.

  In the same basis put $d_i = D_{ii} \ge 0$. If $\theta_j$ are the nonnegative
  eigenvalues of $D$, a unitary change of basis gives $d_i =
  \sum_j|U_{ij}|^2\theta_j$. Both row and column sums of $|U_{ij}|^2$ equal one.
  Finite convexity therefore yields
  \[
    \sum_i d_i^m \le \sum_{i,j}|U_{ij}|^2\theta_j^m
    = \operatorname{Tr}D^m.
  \]
  For completeness, the convexity step follows from $t^m \ge s^m+ms^{m-1}(t-s)$
  for $s,t \ge 0$, obtained by differentiating the difference. Average this
  inequality with $s$ equal to the weighted mean. Now apply finite H\"older from
  Lemma~\ref{L:gaussian-scalar-powers} to $\sum_i d_i|\lambda_i|^{2m-2}$. Since
  $(2m-2)m/(m-1) = 2m$, the last display proves \eqref{E:gaussian-trace-holder},
  including zero sums. This proves Lemma~\ref{L:gaussian-trace-bounds}.
\end{proof}

The estimate below is a finite-dimensional Gaussian noncommutative Khintchine
inequality. For its origins in the work of Lust-Piquard and a Gaussian
integration-by-parts proof, see Tropp~\cite{tropp:source2018:second-order}*{arXiv:1504.05919v2,
Proposition~2.3 and Section~7}. We include the proof and Hermitian dilation
to fix the normalization and retain both variance operators.

\begin{proposition}[Finite Gaussian matrix moment]\label{P:finite-gaussian-matrix}
  Let $A_1,\ldots,A_N$ be complex $o$-by-$n$ matrices, with $o,n,N \ge 1$, and
  let $g_k$ be independent real standard Gaussians. Put
  \[
    X=\sum_k g_kA_k,\qquad V_{\rm out}=\sum_k A_kA_k^*,
    \qquad V_{\rm in}=\sum_k A_k^*A_k.
  \]
  For even $p = 2m \ge 2$, with $\|A\|_{S_p}^p = \operatorname{Tr}((A^*A)^m)$,
  \begin{align}
    (\E\|X\|_{S_p}^p)^{1/p}
    &\le \sqrt{p-1}\left(
    \frac{\operatorname{Tr}V_{\rm out}^m+
    \operatorname{Tr}V_{\rm in}^m}{2}\right)^{1/p}
    \label{E:finite-gaussian-average}\\
    &\le \sqrt{p-1}\max\left(
    \|V_{\rm out}^{1/2}\|_{S_p},\|V_{\rm in}^{1/2}\|_{S_p}\right).
    \label{E:finite-gaussian-maximum}
  \end{align}
  The constants are independent of $o,n,N$. The first inequality is an equality
  at $p = 2$. Empty or zero families give the zero identity.
\end{proposition}

\begin{proof}
  First suppose $B_k$ are Hermitian and put $Y = \sum_k g_kB_k$ and $D = \sum_k
  B_k^2$. All polynomial moments are finite because Gaussian decay dominates
  every fixed power. Componentwise integration by parts against the product
  Gaussian density gives $\E[g_kP(g)] = \E[\partial_kP(g)]$, with zero boundary
  terms. It applies to complex polynomials through their real and imaginary
  parts; absolute polynomial integrability justifies Fubini.

  For $m \ge 2$, put $F = \E\operatorname{Tr}Y^{2m}$ and $L = 2m-2$. Write
  $\operatorname{Tr}Y^{2m} = \sum_k g_k \operatorname{Tr}(B_kY^{2m-1})$ and
  differentiate the $2m-1$ factors in their order. This gives exactly
  \[
    F=\sum_k\sum_{q=0}^{L}
    \E\operatorname{Tr}(B_kY^qB_kY^{L-q}).
  \]
  The eigenbasis calculation above shows these traces are real. The
  differentiated polynomial is real by conjugation and trace cyclicity. No
  derivative of a spectral absolute value or measurable choice of an eigenbasis
  is needed. The two trace bounds give
  \begin{align*}
    F&\le (2m-1)\E\operatorname{Tr}(D|Y|^{2m-2})\\
    &\le (2m-1)(\operatorname{Tr}D^m)^{1/m}
    \E(\operatorname{Tr}|Y|^{2m})^{(m-1)/m}\\
    &\le (2m-1)(\operatorname{Tr}D^m)^{1/m}F^{(m-1)/m}.
  \end{align*}
  Here $\operatorname{Tr}|Y|^{2m} = \operatorname{Tr}Y^{2m}$, and the last
  inequality is the expectation bound in Lemma~\ref{L:gaussian-scalar-powers}.
  If $F = 0$ the conclusion is immediate. Otherwise divide by its positive
  fractional power and raise to $m$ to obtain
  \begin{equation}\label{E:finite-hermitian-gaussian}
    \E\operatorname{Tr}Y^{2m} \le (2m-1)^m\operatorname{Tr}D^m.
  \end{equation}
  For $m = 1$, independence gives directly $\E\operatorname{Tr}Y^2 =
  \sum_k\operatorname{Tr}B_k^2 = \operatorname{Tr}D$, proving the same formula
  as equality.

  For rectangular $A_k$, use the Hermitian dilation
  \[
    B_k=\begin{pmatrix}0&A_k\\A_k^*&0\end{pmatrix},\qquad
    Y=\begin{pmatrix}0&X\\X^*&0\end{pmatrix},\qquad
    D=\operatorname{diag}(V_{\rm out},V_{\rm in}).
  \]
  Finite entrywise summation proves $\operatorname{Tr}(UV) =
  \operatorname{Tr}(VU)$ for compatible rectangular matrices. Since $(XX^*)^m =
  X(X^*X)^{m-1}X^*$, it follows that
  \[
    \operatorname{Tr}Y^{2m}=2\operatorname{Tr}((X^*X)^m),\qquad
    \operatorname{Tr}D^m=\operatorname{Tr}V_{\rm out}^m+
    \operatorname{Tr}V_{\rm in}^m.
  \]
  Substitute in~\eqref{E:finite-hermitian-gaussian}, divide by two and take the
  $p$th root. This proves~\eqref{E:finite-gaussian-average}. For positive $V$,
  spectral diagonalization gives $\|V^{1/2}\|_{S_p}^p = \operatorname{Tr}V^m$,
  and the average of two nonnegative numbers is bounded by their maximum. At $p
  = 2$, $\E\operatorname{Tr}X^*X = \operatorname{Tr}V_{\rm in} =
  \operatorname{Tr}V_{\rm out}$, proving the claimed equality. This proves
  Proposition~\ref{P:finite-gaussian-matrix}.
\end{proof}

Both variance directions are needed: the row-matrix example in
No-go~\ref{P:nogo-23} rules out a dimension-independent estimate that
keeps only one of them.


\begin{remark}[Both variance directions are necessary]
  \label{R:gaussian-one-variance-test}
  Let $n = 16$ and $A_k = e_k^{\mathsf{T}}$ be the coordinate row matrices. The
  only nonzero singular value of $X$ is $(\sum_k g_k^2)^{1/2}$. Gaussian
  integration by parts gives $\E g^2 = 1$, $\E g^4 = 3$, and hence
  \[
    \E\|X\|_{S_4}^4=3n+n(n-1)=n(n+2)=288.
  \]
  Here $V_{\rm out} = n$ and $V_{\rm in} = I_n$. Keeping only the input variance
  in~\eqref{E:finite-gaussian-maximum} would give fourth power
  $9\operatorname{Tr}I_n^2 = 144$, which is false. Transposing the family
  refutes the corresponding output-only bound. The average and maximum bounds
  have fourth powers $1224$ and $2304$, respectively. This finite example
  asserts nothing about a specialized wave estimate.
\end{remark}

\subsection{Whole-space cutoffs through an auxiliary periodic space}

Use the unitary Fourier transform with $c_d = (2\pi)^{-d/2}$ and $\Lambda =
(1-\Delta)^{1/2}$. For real $r$, the norm on $H^r(\R^d)$ is
$\|\langle\xi\rangle^r\widehat{u}\|_2$. The deterministic cutoff arguments allow
any smoothing order $\gamma > 0$. Fix real $\sigma$ and a real compact smooth
$\chi$. Singular values $s_j$, $j \ge 1$, are counted with multiplicity, with
zeros appended when necessary. For compact $K$, put $\|K\|_{S_p}^p = \sum_j
s_j(K)^p$.

\begin{lemma}[Cutoff factorization]\label{L:cutoff-factorization}
  Choose a cube $Q_L = (-L/2,L/2)^d$ containing $\operatorname{supp}\chi$ in its
  interior, and a real $\psi \in C_c^\infty(Q_L)$ equal to one near
  $\operatorname{supp}\chi$. On the auxiliary torus $\mathbb{T}_L$ use Lebesgue
  measure and the orthonormal basis
  \[
    e_k(x)=L^{-d/2}e^{i\kappa_k\cdot x},\qquad
    \kappa_k=2\pi k/L,\qquad k \in \mathbb{Z}^d,
  \]
  with $\|v\|_{H^r(\mathbb{T}_L)}^2 = \sum_k\langle\kappa_k\rangle^{2r}|v_k|^2$.
  Periodization of $\psi u$ and multiplication of a periodic function by $\chi$
  extend to bounded maps
  \begin{equation}\label{E:cutoff-periodic-maps}
    \mathcal{P}_\psi:H^r(\R^d)\to H^r(\mathbb{T}_L),\qquad
    \mathcal{E}_\chi:H^r(\mathbb{T}_L)\to H^r(\R^d)
  \end{equation}
  for every real $r$. If $\mathcal{I}_\gamma$ denotes the identity inclusion
  from $H^{\sigma+\gamma}(\mathbb{T}_L)$ to $H^\sigma(\mathbb{T}_L)$, then
  \begin{equation}\label{E:cutoff-whole-space-recovery}
    \mathcal{E}_\chi\mathcal{I}_\gamma\mathcal{P}_\psi u=\chi u,
    \qquad u \in H^{\sigma+\gamma}(\R^d).
  \end{equation}
\end{lemma}

\begin{proof}
  For $x,y \in \R^d$ and real $r$, the elementary inequality $\langle x\rangle
  \le \sqrt{2}\langle y\rangle\langle x-y\rangle$ gives
  \begin{equation}\label{E:cutoff-peetre}
    \left(\frac{\langle x\rangle}{\langle y\rangle}\right)^r
    \le 2^{|r|/2}\langle x-y\rangle^{|r|}.
  \end{equation}
  For negative $r$, interchange $x,y$ before raising to $|r|$. Integration by
  parts gives rapid decay of the Fourier transform of every compact smooth
  cutoff. For any lattice spacing $a > 0$ and $N > d$,
  \begin{equation}\label{E:cutoff-lattice-sum}
    \sup_y\sum_{k\in\mathbb{Z}^d}\langle y-ak\rangle^{-N}<\infty.
  \end{equation}
  Indeed, translate $y$ into a centered lattice cell, where $|y| \le a\sqrt
  d/2$. For $|k| \ge \sqrt d$ we have $|y-ak| \ge a|k|/2$. The remaining terms
  are finite; the tail converges by dyadic lattice counting, since there are at
  most $C_d2^{jd}$ lattice points in the $j$th shell in $k$. More precisely, for
  $|k| \ge \sqrt d$, the preceding inequality gives
  \[
    \langle y-ak\rangle^{-N}
    \le \max(1,2/a)^N\langle k\rangle^{-N}.
  \]
  The comparison-series terms are bounded by $2^{-jN}$ on each dyadic $k$-shell.
  Thus, its convergent geometric sum carries constants depending on $a,d,N$, as
  does~\eqref{E:cutoff-lattice-sum}.

  We use the mixed Schur bound for a kernel whose absolute row and column
  integrals are bounded by $M_1,M_2$. Weighted Cauchy--Schwarz at each output
  point, followed by Tonelli, bounds its squared operator norm by $M_1M_2$. The
  same proof works with counting measure on one side and Lebesgue measure on the
  other, first on dense finite or compact inputs.

  For Schwartz $u$, the $k$th coefficient of its cutoff periodization is
  \[
    (\mathcal{P}_\psi u)_k
    = L^{-d/2}\int\psi(x)u(x)e^{-i\kappa_k\cdot x}\ud x
    = L^{-d/2}\int\widehat{\psi}(\kappa_k-\xi)\widehat{u}(\xi)\ud\xi.
  \]
  The $c_d$ from Fourier inversion cancels the $c_d^{-1}$ in the ordinary
  Fourier integral of $\psi$. After weighting, its exact kernel is
  \[
    L^{-d/2}\left(\frac{\langle\kappa_k\rangle}{\langle\xi\rangle}\right)^r
    \widehat{\psi}(\kappa_k-\xi).
  \]
  For a finite torus polynomial $v$, the normalized Fourier kernel of
  $\mathcal{E}_\chi v$ is
  \[
    L^{-d/2}\left(\frac{\langle\xi\rangle}{\langle\kappa_k\rangle}\right)^r
    \widehat{\chi}(\xi-\kappa_k).
  \]
  There is no additional $c_d$ in this kernel. By~\eqref{E:cutoff-peetre}, each
  is bounded in absolute value by a rapidly decreasing function of its frequency
  difference, times a fixed constant. One Schur quantity is its $L^1$ integral
  and the other a uniformly translated lattice sum, bounded
  by~\eqref{E:cutoff-lattice-sum}. This proves~\eqref{E:cutoff-periodic-maps},
  including negative $r$.

  Smooth compact approximation in weighted Fourier $L^2$ proves Schwartz density
  on $\R^d$; weighted sequence truncation proves polynomial density on the
  torus. Hence, these maps extend uniquely. Their distributional meanings follow
  by testing against compact smooth functions and density: each periodic
  coefficient pairs the distribution with a compact smooth test. No point
  sampling of a rough Fourier function is used. The same full-Lebesgue Schur
  argument proves smooth compact multiplication bounded on every whole-space
  $H^r$.

  For Schwartz $u$, the periodic Fourier series of $\psi u$ converges smoothly
  on the cube. Since $\chi\psi = \chi$ and $\chi$ is supported strictly inside
  the cube, multiplying this series by $\chi$ recovers $\chi u$ with no alias
  term. Both sides are bounded from $H^{\sigma+\gamma}(\R^d)$ to
  $H^\sigma(\R^d)$, using the just-proved maps, the inclusion and smooth
  multiplication. Density proves \eqref{E:cutoff-whole-space-recovery} on that
  full domain. This proves Lemma~\ref{L:cutoff-factorization}.
\end{proof}

\begin{proposition}[Whole-space cutoff singular values]\label{P:cutoff-singular-values}
  For real $\sigma$ and $\gamma > 0$, the initially Schwartz-defined operator
  $K_{\chi,\sigma,\gamma} = \Lambda^\sigma\chi\Lambda^{-\sigma-\gamma}$ extends
  uniquely to a compact operator on $L^2(\R^d)$, and
  \begin{equation}\label{E:cutoff-singular-values}
    s_j(K_{\chi,\sigma,\gamma})
    \le C_{\chi,\sigma,\gamma,d}j^{-\gamma/d},\qquad j \ge 1.
  \end{equation}
  Consequently, $K_{\chi,\sigma,\gamma} \in S_p$ whenever $p \ge 1$ and $p\gamma
  > d$.
\end{proposition}

\begin{proof}
  The zero cutoff is immediate. Fix one cube and cutoff pair $L,\psi$ as in
  Lemma~\ref{L:cutoff-factorization}. Its recovery identity gives
  \[
    K_{\chi,\sigma,\gamma}
    =\Lambda^\sigma\mathcal{E}_\chi\mathcal{I}_\gamma
    \mathcal{P}_\psi\Lambda^{-\sigma-\gamma}.
  \]
  In the weighted torus coordinates, $\mathcal{I}_\gamma$ is diagonal with
  entries $\langle\kappa_k\rangle^{-\gamma}$. Let $Q_n$ retain $|k|_\infty \le
  n$. Its rank is $(2n+1)^d$, and
  \[
    \|(1-Q_n)\mathcal{I}_\gamma\|
    \le [1+(2\pi/L)^2(n+1)^2]^{-\gamma/2}\longrightarrow0.
  \]
  Replacing the inclusion by $Q_n\mathcal{I}_\gamma$ gives finite-rank $K_n$
  converging in norm to $K_{\chi,\sigma,\gamma}$. This proves compactness:
  finite-dimensional images have finite nets of each positive radius, and norm
  approximation transfers those nets to the limiting image of the unit ball.

  Put
  \[
    M=\|\mathcal{E}_\chi:H^\sigma(\mathbb{T}_L)\to H^\sigma(\R^d)\|
    \|\mathcal{P}_\psi:H^{\sigma+\gamma}(\R^d)
    \to H^{\sigma+\gamma}(\mathbb{T}_L)\|.
  \]
  The outer Bessel maps are unitary. For $j \ge 3^d$, choose $n = \lfloor
  j^{1/d}/4\rfloor$. Then
  \[
    (2n+1)^d\le(j^{1/d}/2+1)^d<j,\qquad
    \|K-K_n\|\le M(2L/\pi)^\gamma j^{-\gamma/d}.
  \]
  The second estimate follows from $n+1 > j^{1/d}/4$. For a compact operator,
  every rank less than $j$ approximation $F$ satisfies $s_j(K) \le \|K-F\|$: the
  span of the first $j$ right singular vectors contains a unit vector in $\ker
  F$, on which $\|K\cdot\| \ge s_j(K)$. If $s_j(K) = 0$ the inequality is
  immediate. For $j < 3^d$ use $s_j(K) \le \|K\| \le M$. Thus, one may take
  \[
    C_{\chi,\sigma,\gamma,d}
    =M\max(3^\gamma,(2L/\pi)^\gamma).
  \]
  Finally, $\sum_j j^{-p\gamma/d}$ converges for $p\gamma > d$. This proves
  Proposition~\ref{P:cutoff-singular-values}.
\end{proof}

No uniform support-radius constant or endpoint necessity is asserted in
Proposition~\ref{P:cutoff-singular-values}. The periodic inclusion was only a
factor of the recovered whole-space operator.

\subsection{Balanced adjoints and localized variance envelopes}

For $E = H^{1/2}(\R^d)\times H^{-1/2}(\R^d)$ use the physical unitary
coordinates
\[
  J_0(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v),\qquad
  H=L^2(\R^d;\mathbb{C}^2).
\]
The frequency map $J$ in Section~\ref{S:wave-variance} is
$(\mathcal{F}\oplus\mathcal{F})J_0$. Let $D_\chi$ multiply both phase entries
and define
\begin{align}
  P_\chi&=J_0D_\chi J_0^{-1},\qquad
  D_\gamma=\operatorname{diag}(\Lambda^{-\gamma},\Lambda^{-\gamma}),
  \label{E:compact-balanced-cutoff}\\
  K_{\rm out}&=P_\chi D_\gamma,\qquad
  K_{\rm in}=P_\chi^*D_\gamma.
  \label{E:compact-two-factors}
\end{align}

\begin{proposition}[Both compact envelopes]\label{P:compact-two-envelopes}
  The operator $P_\chi$ is bounded. For the unitary swap $U(v,w) = (w,v)$,
  \[
    P_\chi^*=UP_\chi U,\qquad K_{\rm in}=UK_{\rm out}U.
  \]
  Both factors are compact and have equal $S_p$ norms for $p \ge 1$, $p\gamma >
  d$. For $p \ge 2$, $p\gamma > d$, the positive compact operators
  \[
    B_{\rm out}=P_\chi D_\gamma^2P_\chi^*=K_{\rm out}K_{\rm out}^*,
    \qquad B_{\rm in}=P_\chi^*D_\gamma^2P_\chi=K_{\rm in}K_{\rm in}^*
  \]
  satisfy
  \begin{equation}\label{E:compact-envelope-traces}
    \operatorname{Tr}B_{\rm out}^{p/2}
    =\operatorname{Tr}B_{\rm in}^{p/2}=\|K_{\rm out}\|_{S_p}^p.
  \end{equation}
\end{proposition}

\begin{proof}
  Put $A_\sigma = \Lambda^\sigma\chi\Lambda^{-\sigma}$. The full-Lebesgue Schur
  argument in Lemma~\ref{L:cutoff-factorization} shows boundedness for every
  real $\sigma$. On Schwartz functions, self-adjointness of real multiplication
  and of the Bessel powers gives $A_\sigma^* = A_{-\sigma}$. Density and
  boundedness extend this to the Hilbert adjoints. No evenness of $\chi$ is
  needed. Thus,
  \[
    P_\chi=\operatorname{diag}(A_{1/2},A_{-1/2}),\qquad
    P_\chi^*=\operatorname{diag}(A_{-1/2},A_{1/2})=UP_\chi U.
  \]
  The swap commutes with $D_\gamma$, giving the claimed factor identity. The
  blocks of $K_{\rm out}$ are $K_{\chi,1/2,\gamma}$ and $K_{\chi,-1/2,\gamma}$.
  Proposition~\ref{P:cutoff-singular-values} gives compactness and $S_p$
  membership. The singular values of their direct sum form the multiset union,
  so
  \[
    \|K_{\rm out}\|_{S_p}^p
    =\|K_{\chi,1/2,\gamma}\|_{S_p}^p+
    \|K_{\chi,-1/2,\gamma}\|_{S_p}^p.
  \]
  Unitary conjugation preserves them. Finally, the positive eigenvalues of
  $KK^*$ and $K^*K$ agree with multiplicity: on an eigenspace with eigenvalue
  $\lambda > 0$, the maps $K/\sqrt\lambda$ and $K^*/\sqrt\lambda$ are inverse
  isometries. Zero eigenvalues contribute nothing to the trace. Summing these
  scalar powers proves~\eqref{E:compact-envelope-traces}. This proves
  Proposition~\ref{P:compact-two-envelopes}.
\end{proof}

We use the usual positive square root of a bounded positive operator and the
spectral decomposition of compact positive operators. The needed order argument
is recorded explicitly.

\begin{lemma}[Compact positive order and trace]\label{L:compact-positive-order}
  If $A,B$ are bounded self-adjoint operators with $0 \le A \le B$ and $B$
  compact positive, then $A$ is compact and its ordered eigenvalues satisfy
  $\lambda_j(A) \le \lambda_j(B)$, including zero padding. Consequently, for $t
  \ge 1$ with finite $\operatorname{Tr}B^t$,
  \begin{equation}\label{E:compact-positive-trace}
    \operatorname{Tr}A^t\le\operatorname{Tr}B^t.
  \end{equation}
\end{lemma}

\begin{proof}
  Let $Q_n$ be finite spectral projections of $B$ whose tails tend to zero in
  norm. Then
  \[
    \|(1-Q_n)A^{1/2}\|^2
    =\|(1-Q_n)A(1-Q_n)\|
    \le\|(1-Q_n)B(1-Q_n)\|\longrightarrow0.
  \]
  Thus, $A^{1/2}$ is a norm limit of finite-rank operators and is compact, as is
  $A$. For compact positive operators, the max-min formula for $\lambda_j$
  follows in an eigenbasis: the span of the first $j$ eigenvectors gives the
  lower bound for the supremum over $j$-dimensional subspaces of their minimum
  Rayleigh quotient, while every such subspace meets the orthogonal complement
  of the first $j-1$ eigenvectors, giving the upper bound. Compare the Rayleigh
  quotients of $A$ and $B$ to obtain the eigenvalue inequality. Sum the ordered
  scalar powers to prove \eqref{E:compact-positive-trace}. No inequality $A^t
  \le B^t$ is asserted. This proves Lemma~\ref{L:compact-positive-order}.
\end{proof}

\begin{proposition}[Localized finite variance bounds]\label{P:localized-finite-variance}
  Suppose finitely many bounded operators $Z_\ell$ on $H$ satisfy
  \begin{equation}\label{E:localized-finite-hypotheses}
    P_\chi Z_\ell=Z_\ell=Z_\ell P_\chi,\qquad
    V_{\rm out}:=\sum_\ell Z_\ell Z_\ell^*\le CD_\gamma^2,\qquad
    V_{\rm in}:=\sum_\ell Z_\ell^*Z_\ell\le CD_\gamma^2,
  \end{equation}
  with $C \ge 0$. If $p \ge 2$ and $p\gamma > d$, every $Z_\ell$ is compact in
  $S_p$, the two variances are compact in $S_{p/2}$, and
  \begin{align}
    V_{\rm out}&\le CB_{\rm out},\qquad V_{\rm in}\le CB_{\rm in},
    \label{E:localized-two-envelopes}\\
    \operatorname{Tr}V_{\rm out}^{p/2},\quad
    \operatorname{Tr}V_{\rm in}^{p/2}
    &\le C^{p/2}\|K_{\rm out}\|_{S_p}^p.
    \label{E:localized-trace-bounds}
  \end{align}
\end{proposition}

\begin{proof}
  Left localization gives $V_{\rm out} = P_\chi V_{\rm out}P_\chi^*$. Apply
  positive congruence to the output bound
  in~\eqref{E:localized-finite-hypotheses} to get $V_{\rm out} \le CP_\chi
  D_\gamma^2P_\chi^* = CB_{\rm out}$. Right localization similarly gives $V_{\rm
  in} = P_\chi^*V_{\rm in}P_\chi \le CB_{\rm in}$.
  Proposition~\ref{P:compact-two-envelopes} and
  Lemma~\ref{L:compact-positive-order} prove compactness and the two trace
  bounds with $t = p/2$. If $C = 0$, both variances and every $Z_\ell$ vanish,
  so all assertions are immediate.

  For each $\ell$, $Z_\ell Z_\ell^* \le V_{\rm out}$ is compact by the same
  lemma. Its finite spectral projections $Q_n$ give $\|(1-Q_n)Z_\ell\|^2 =
  \|(1-Q_n)Z_\ell Z_\ell^*(1-Q_n)\| \to 0$. Hence, $Z_\ell$ is compact. Its
  singular values squared are the nonzero eigenvalues of $Z_\ell Z_\ell^*$.
  Comparing with $V_{\rm out}$ and summing proves $Z_\ell \in S_p$ with
  $\|Z_\ell\|_{S_p}^p \le \operatorname{Tr}V_{\rm out}^{p/2}$. This proves
  Proposition~\ref{P:localized-finite-variance}.
\end{proof}

The two localization identities are hypotheses here; a noise coefficient family
has not yet been shown to satisfy them. In particular, $P_\chi$ is not assumed
self-adjoint or a projection.

\begin{corollary}[Finite Gaussian operators]\label{C:finite-gaussian-operators}
  Under~\eqref{E:localized-finite-hypotheses}, let $g_\ell$ be independent real
  standard Gaussians. For even $p \ge 2$ with $p\gamma > d$, the finite sum $X =
  \sum_\ell g_\ell Z_\ell$ satisfies
  \begin{equation}\label{E:finite-gaussian-operator-bound}
    (\E\|X\|_{S_p}^p)^{1/p}
    \le\sqrt{p-1}\sqrt C\|K_{\rm out}\|_{S_p}.
  \end{equation}
  Its extended norm is measurable, with finite expectation as displayed.
\end{corollary}

\begin{proof}
  Choose finite-rank orthogonal projections $\Pi_n$ from a countable orthonormal
  basis of $H$, with $\Pi_n \to I$ strongly. Put $Z_{\ell,n} = \Pi_nZ_\ell\Pi_n$
  and $X_n = \sum_\ell g_\ell Z_{\ell,n}$, viewed as matrices on
  $\operatorname{ran}\Pi_n$. Their output variance satisfies
  \[
    \sum_\ell\Pi_nZ_\ell\Pi_nZ_\ell^*\Pi_n
    \le\Pi_nV_{\rm out}\Pi_n,
  \]
  since the difference is $\sum_\ell\Pi_nZ_\ell(1-\Pi_n)Z_\ell^*\Pi_n \ge 0$.
  The input inequality is identical with adjoints interchanged. Compact max-min
  also gives $\lambda_j(\Pi_nV\Pi_n) \le \lambda_j(V)$ for positive compact $V$,
  since Rayleigh subspaces inside $\operatorname{ran}\Pi_n$ form a subset of all
  subspaces. Thus, both variance trace powers of these matrices are bounded by
  $C^{p/2}\|K_{\rm out}\|_{S_p}^p$.

  Proposition~\ref{P:finite-gaussian-matrix} applies to these finite complex
  matrices, the same real independent Gaussians and the even $p$. Taking the
  average of the two already bounded trace powers gives
  \begin{equation}\label{E:finite-gaussian-compression-bound}
    \E\|X_n\|_{S_p}^p
    \le(p-1)^{p/2}C^{p/2}\|K_{\rm out}\|_{S_p}^p.
  \end{equation}
  No factor two is added by this average.

  For each Gaussian coordinate vector, $X$ is a finite sum of compact operators.
  Strong convergence of $\Pi_n$ implies $\Pi_nX\Pi_n \to X$ in operator norm:
  approximate $X$ by a finite-rank $F$, use uniform strong convergence on the
  finite-dimensional ranges of $F$ and $F^*$, and control the remainder using
  $\|\Pi_n\| \le 1$. Singular values are norm-Lipschitz. Indeed, their formula
  \[
    s_j(A)=\inf_{\dim L<j}
    \sup_{v\in L^\perp,\ \|v\|=1}\|Av\|
  \]
  follows from compact singular vectors and gives $s_j(A) \le s_j(B)+\|A-B\|$,
  and the reverse bound by interchanging $A,B$. Hence, $s_j(X_n) \to s_j(X)$ for
  each $j$. Fatou for the nonnegative singular-value sum gives $\|X\|_{S_p}^p
  \le \liminf_n\|X_n\|_{S_p}^p$, allowing extended infinity. These variables are
  measurable: the finite Gaussian coordinate map into operators is
  norm-continuous, each singular value is continuous, and the norm power is
  their nonnegative measurable sum. Fatou in probability
  and~\eqref{E:finite-gaussian-compression-bound} prove the bound and
  almost-sure finiteness. No $S_p$-Bochner convergence is assumed. This proves
  Corollary~\ref{C:finite-gaussian-operators}.
\end{proof}

\subsection{A nonzero witness and the need for a compact cutoff}

\begin{proposition}[Whole-space cutoff tests]\label{P:cutoff-boundary-tests}
  If $\chi$ equals one on a nonempty open set, there is a nonzero rank-one
  operator satisfying~\eqref{E:localized-finite-hypotheses} with a finite common
  $C$. On the other hand, $\Lambda^{-\gamma}$ on $L^2(\R^d)$ is not compact for
  any $\gamma > 0$.
\end{proposition}

\begin{proof}
  Choose nonzero real $v,f \in C_c^\infty$ supported inside the plateau, and put
  $\widetilde{v} = (\Lambda^{1/2}v,0)$ and $\widetilde{w} =
  (\Lambda^{-1/2}f,0)$. Both are Schwartz. The block formulas give
  $P_\chi\widetilde{v} = \widetilde{v}$ and $P_\chi^*\widetilde{w} =
  \widetilde{w}$. Therefore, $Zx = \langle x,\widetilde{w}\rangle\widetilde{v}$
  satisfies $P_\chi Z = Z = ZP_\chi$. Its two variances are
  $\|\widetilde{w}\|^2\widetilde{v}\otimes\widetilde{v}^*$ and
  $\|\widetilde{v}\|^2\widetilde{w}\otimes\widetilde{w}^*$. For any Schwartz $a$
  and any $x \in H$,
  \[
    |\langle x,a\rangle|
    =|\langle D_\gamma x,D_\gamma^{-1}a\rangle|
    \le\|D_\gamma x\|\|D_\gamma^{-1}a\|.
  \]
  The inverse multiplier is applied only to Schwartz $a$, so it belongs to $H$.
  Apply the inequality with $a = \widetilde{v},\widetilde{w}$ to obtain the two
  variance bounds with
  \[
    C=\max\left(
    \|\widetilde{w}\|^2\|D_\gamma^{-1}\widetilde{v}\|^2,
    \|\widetilde{v}\|^2\|D_\gamma^{-1}\widetilde{w}\|^2\right)<\infty.
  \]
  This witness uses a plateau; no nonzero family is inferred for every compact
  cutoff or identified with a source family.

  For noncompactness, take $f$ with nonzero Gaussian Fourier transform. Then $g
  = \Lambda^{-\gamma}f$ is a nonzero Schwartz function. The images of translates
  of $f$ are the same translates of $g$. With $T_hg(x) = g(x-h)$, Plancherel
  gives
  \[
    \langle T_hg,g\rangle
    =\int e^{-i\xi\cdot h}|\widehat{g}(\xi)|^2\ud\xi
    =c_d^{-1}\widehat{|\widehat{g}|^2}(h).
  \]
  This tends to zero because $|\widehat{g}|^2$ is Schwartz. Choose a large
  spacing so that any two distinct translates in the resulting sequence have
  image distance at least $\|g\|$. The input norms are identical, but the images
  have no Cauchy subsequence. This disproves compactness. This proves
  Proposition~\ref{P:cutoff-boundary-tests}.
\end{proof}

The translation obstruction is restated in No-go~\ref{P:nogo-24}:
frequency decay alone does not replace compact spatial localization.


Thus, the choice $\chi = 1$ cannot be substituted into the compact-cutoff
argument. No necessity at the Schatten endpoint $p\gamma = d$ is asserted. The
results concern finite matrices and conditional finite operator sums.
Coefficient localization, compact variance tails, an infinite Gaussian series
and time regularity are proved in Section~\ref{S:actual-operator-driver}; source
and Young identification are proved in
Sections~\ref{S:source-driver-convergence}--\ref{S:constant-phase-young}. They
are not consequences of the finite comparison alone.

# Main-source context H:homog
\begin{hypothesis}[Homogeneous covariance]\label{H:homog}
  Let $d \in \{1,2,3\}$ and $0 < \alpha_0 < 1$. The spatial covariance is a
  nonnegative, even, positive-definite tempered Radon measure $\Gamma$ on
  $\R^d$, with positive even tempered Radon spectral measure $\mu$ in the
  convention
  \[
    \Gamma=\int e^{i\xi\cdot x}\mu(\ud\xi)
    \quad\text{in the sense of tempered distributions}.
  \]
  The symbol $\gamma$ in~\eqref{E:cov} denotes this covariance as a function
  when one exists, and as a distribution otherwise. For every Borel set $A$ and
  $c > 0$, $\Gamma(cA) = c^{d-\alpha}\Gamma(A)$, and
  \begin{equation}\label{E:threshold}
    \alpha_0+\alpha<2,
  \end{equation}
  with $0 < \alpha < d$, or $\alpha = d = 1$. In particular, the last case
  includes spatial white noise $\Gamma = \delta_0$.
\end{hypothesis}

# Main-source context P:low-alpha-upper
\begin{proposition}[Upper bound for $\alpha \le 1$]\label{P:low-alpha-upper}
  Suppose that Hypothesis~\ref{H:homog} and the standing covariance positivity
  assumptions hold, $d \in \{1,2,3\}$, $0 < \alpha \le 1$, and $V > 0$. Define
  \begin{equation}\label{E:low-alpha-constants}
    \begin{split}
      K_{\rm sp}^{\rm gen}
      &=\begin{cases}
        \displaystyle\frac{V2^{2-\alpha}(1-\alpha)^{-\alpha}}
        {(2-\alpha)^{2-\alpha}},&0<\alpha<1,\\[2mm]
        \pi V,&\alpha=1,
      \end{cases}\\
      C_2^{\rm gen}&=q(2ZK_{\rm sp}^{\rm gen})^{1/q}.
    \end{split}
  \end{equation}
  With the same $A_k$, $b$, $q$, $\beta$, and $Z$ as above, for
  $k \ge 1$ and $t > 0$,
  \begin{equation}\label{E:low-alpha-coefficient}
    A_k(t)\le\frac{(2ZK_{\rm sp}^{\rm gen})^k t^{\beta k}}
    {k!\,k^{bk}}
    \le\frac{(2ZK_{\rm sp}^{\rm gen})^k t^{\beta k}}{(k!)^q},
    \qquad
    \E u^2(t,x)\le\exp(C_2^{\rm gen}t^\kappa).
  \end{equation}
\end{proposition}

\begin{proof}
  First smooth the noise as in~\cite{chen:author2026:time-dependency}*{(2.9), (2.11), (2.23)--(2.24)}.
  In dimension three also use $G_{h,\eta}$ with $\eta > 0$, as in the
  source's pp.~13--14. The increment change of variables is now a
  triangular map on vectors in $\R^d$, still of determinant one.
  The descending-label proof of Lemma~\ref{L:d1-spatial} depends only
  on which increments enter each position, not on their dimension.
  Its invariant therefore remains valid: at a closing label there
  is exactly one covariance depending on that vector increment, and
  at an opening label its pair has already been removed.
  If $0 < \alpha < 1$, Lemma~\ref{L:low-alpha-convolution} gives the
  closing bound $Mh_l^{1-\alpha}$ with $M = V/(1-\alpha)$.
  At $\alpha = 1$, Lemma~\ref{L:alpha-one-convolution} gives the
  constant closing bound $M = \pi V/2$. Every opening gives mass
  $h_l$, uniformly in $\eta$ and all noise-smoothing parameters.
  For $\alpha < 1$, the same weighted arithmetic--geometric mean
  calculation gives
  \[
    M^k\prod_{i\in O_D}h_i\prod_{j\in C_D}h_j^{1-\alpha}
    \le (K_{\rm sp}^{\rm gen})^k\frac{t^{bk}}{k^{bk}}.
  \]
  At $\alpha = 1$, ordinary arithmetic--geometric mean on the $k$ opening
  increments gives $M^k\prod_{i\in O_D}h_i \le (2M)^kt^k/k^k$, which is the same
  bound with $b = 1$ and $K_{\rm sp}^{\rm gen} = \pi V$. Both cases use
  $\sum_lh_l \le 2t$. For $d = 1,2$ one may use the Green densities directly;
  their opening mass and closing convolution obey these same bounds.

  Replace the nonnegative truncated temporal factors by $|s_i-s_j|^{-\alpha_0}$
  before taking their pairing sum. The temporal symmetry, cube integral and
  split count in~\eqref{E:d1-time-symmetry} do not involve the spatial
  dimension. Thus, exactly the multiplication of counts in the proof of
  Proposition~\ref{P:d1-upper} gives the first bound
  in~\eqref{E:low-alpha-coefficient} for the regularized moments.

  We spell out the limit in dimension three. Fix every noise-smoothing parameter
  and first let $\eta\downarrow0$. At each time vector, the Gaussian moment
  formula is a finite sum of bounded continuous products of the smoothed
  covariance functions, integrated against products of the finite Green
  measures. These products of measures converge weakly as $\eta\downarrow0$,
  with the same masses $\prod_l h_l$. At fixed noise smoothing the Gaussian
  covariance factors are uniformly bounded, so a constant times $\prod_lh_l$
  dominates on each bounded time simplex. Dominated convergence applies also to
  the covariance between two approximations with different $\eta$ values. The
  resulting common joint covariance limit proves the $L^2$ Cauchy property of
  each fixed-order random integral. This is the inner limit used in the source's
  definition on pp.~13--14. Products of two factors converge in $L^1$ by
  Cauchy--Schwarz, so the moment inequality survives this limit. Next send the
  noise-smoothing parameters to zero using the fixed-order $L^2$ convergence of
  Lemma~\ref{L:joint-fixed-order}, and again pass products in $L^1$. In
  dimensions one and two only the latter limit is required. The bounds at both
  stages are uniform.

  We have proved the first coefficient bound for $A_k(t)$. The factorial
  inequality and nonnegative-series argument in Proposition~\ref{P:d1-upper}
  apply unchanged, with $K_{\rm sp}^{\rm gen}$ in place of $K_{\rm sp}$ and $A_0
  = 1$. This proves Proposition~\ref{P:low-alpha-upper}.
\end{proof}

# Main-source context P:static-phase-all-orders
\begin{proposition}[All regularized static phase orders]
  \label{P:static-phase-all-orders}
  Retain the full covariance class of Section~\ref{S:static-phase}. For real
  Schwartz $f,g$, let $Z_n^\epsilon(h)$ be the $n$th regularized static Duhamel
  phase, with the recursion \eqref{E:phase-duhamel} for every $n \ge 0$. This is
  an ordinary Gaussian polynomial of degree at most $n$, including
  self-contractions; it is not a pure Wick chaos. There is an explicit finite
  constant
  \[
    A_\alpha=\frac{400\sqrt2\,e^2}{\delta_{\alpha/2}}
  \]
  such that, for $n \ge 1$, uniformly in $\epsilon > 0$,
  \begin{equation}\label{E:all-static-phase-orders}
    \|Z_n^\epsilon(h)\|_{L^2(\Omega;X_{1/h})}
    \le
    \frac{(A_\alpha\sqrt{R_\alpha})^n
    h^{(4-\alpha)n/2}}{(n!)^{(3-\alpha)/2}}
    \|(f,g)\|_{1/h}.
  \end{equation}
  At every fixed positive smoothing and real coupling $\sigma$,
  $\sum_{n\ge0}\sigma^nZ_n^\epsilon(h)$ converges in $L^2$ phase. Its squared
  norm is at most
  \begin{equation}\label{E:all-static-phase-sum}
    (\sqrt e+2)^2
    \exp\left\{6A_\alpha^{2/(3-\alpha)}
    (|\sigma|^2R_\alpha)^{1/(3-\alpha)}
    h^{(4-\alpha)/(3-\alpha)}\right\}\|(f,g)\|_{1/h}^2.
  \end{equation}
\end{proposition}

\begin{proof}
  If $R_\alpha = 0$, spectral homogeneity gives $\mu = 0$, and every
  positive-order term is zero. Assume $R_\alpha > 0$. First work at finite
  Gaussian cutoff $m$, degree cutoff $N$ and spatial band $b$, with initial
  phase $S_b(f,g)$ times the Gaussian vacuum $1$. All relevant operators are
  bounded. Lemmas~\ref{L:fock-form} and~\ref{L:complex-phase}, with $a =
  \alpha/2$, give a bound $100e^{2\lambda h}$ on the complex coupling circle of
  radius $\delta_{\alpha/2}\lambda^{2-\alpha/2}/d_N$.

  The four phase entries are entire in the coupling, by the power series for
  $\cos(h\sqrt L)$ and $\sin(h\sqrt L)/\sqrt L$ of a bounded $L$. Cauchy's
  formula for their operator-valued series bounds the $n$th coefficient by
  \[
    100e^{2\lambda h}
    \left(\frac{d_N}
    {\delta_{\alpha/2}\lambda^{2-\alpha/2}}\right)^n
    \|S_b(f,g)\|_\lambda .
  \]
  The coefficient is exactly the $n$th Duhamel phase from the vacuum. Apply
  Lemma~\ref{L:finite-word-cutoff} with one color, $N = n$, the spatial phase
  Hilbert space as $\mathscr{X}$, and its free wave operators as the $F_l$. It
  identifies each cutoff Duhamel word exactly with its uncompressed word,
  including self-contractions. Dominated time integration preserves this
  identity.

  Choose $\lambda = n/h$. For any phase $z$, $\|z\|_{1/h} \le n\|z\|_{n/h}$ and
  $\|(f,g)\|_{n/h} \le \|(f,g)\|_{1/h}$. Also $d_n \le
  2\sqrt{2n}\sqrt{R_\alpha}$. The preceding bound is therefore at most
  \[
    100n\left(\frac{2\sqrt2 e^2}{\delta_{\alpha/2}}\right)^n
    R_\alpha^{n/2}h^{(4-\alpha)n/2}
    n^{-(3-\alpha)n/2}\|(f,g)\|_{1/h}.
  \]
  Since $100n \le 200^n$ and $n! \le n^n$, this gives
  \eqref{E:all-static-phase-orders} at the cutoffs.

  We justify removal of those cutoffs at fixed $\epsilon$ and $n$. On Gaussian
  degrees at most $N$, the unweighted field multiplication has norm at most
  $2\sqrt{N+1}\sqrt{v_\epsilon}$, uniformly in $m$, by the same
  creation/annihilation argument applied pointwise in $x$. It follows that the
  noise phase insertion $(u,v)\mapsto(0,W_\epsilon u)$, between the required
  finite degree levels, is bounded on $X_\lambda$ by this constant divided by
  $\lambda$. Free phase evolution is bounded by $e^{\lambda h/2}$. For finite
  $m$, $S_b \to I$ strongly and commutes with the free propagator. Each fixed
  Duhamel word therefore converges strongly as $b \to \infty$, by dominated time
  integration.

  Next let $m \to \infty$ on the full Gaussian space. The truncated field
  multiplications converge strongly between finite degree levels. To see this,
  first take a vector depending on finitely many Gaussian coordinates. The
  annihilation tail is then zero, while the creation tail is bounded by a
  constant times
  \[
    \left(\int\sum_{i>m}e_i(x)^2\|F(x)\|^2\ud x\right)^{1/2},
  \]
  which tends to zero by dominated convergence, since the sum is bounded by
  $v_\epsilon$. Such vectors are dense; the uniform multiplication bound extends
  strong convergence to all vectors in those degree levels. Dominated time
  integration again gives convergence of every fixed word. The limit is
  precisely $Z_n^\epsilon$, so the estimate survives both limits. We assert no
  zero-smoothing phase limit in this argument.

  Finally, put $\beta = (3-\alpha)/2 \in (1/2,3/2)$ and $x =
  A_\alpha|\sigma|\sqrt{R_\alpha}h^{(4-\alpha)/2}$. The elementary series
  satisfies
  \[
    \sum_{n\ge0}\frac{x^n}{(n!)^\beta}
    \le2e^{3x^{1/\beta}}.
  \]
  For $\beta \ge 1$, this follows from $\sum a_n^\beta \le (\sum a_n)^\beta$
  with $a_n = x^{n/\beta}/n!$. For $\beta < 1$, apply H\"older to
  $((2x^{1/\beta})^n/n!)^\beta (2^{-\beta n/(1-\beta)})^{1-\beta}$. The second
  geometric sum is at most two. Since $\|Z_0(h)\|_{1/h} \le \sqrt
  e\|(f,g)\|_{1/h}$, absolute $L^2$ summation and squaring give
  \eqref{E:all-static-phase-sum}. This proves
  Proposition~\ref{P:static-phase-all-orders}.
\end{proof}
