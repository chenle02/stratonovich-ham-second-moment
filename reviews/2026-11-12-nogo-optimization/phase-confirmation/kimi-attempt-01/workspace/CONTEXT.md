# Exact phase and unitary normalization
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


# P:low-alpha-upper
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
# P:static-phase-all-orders
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