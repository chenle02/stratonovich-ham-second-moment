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
# Complete direct-bound section, including b=2-alpha and upstream convolution lemmas
\section{Upper bounds for spatial exponents at most one}\label{S:d1-upper}

The upper bound at scale $t^\kappa$ is proved for $0 < \alpha \le 1$ in
dimensions one, two and three under the standing assumptions. The separate
one-dimensional Riesz estimates retain their sharper constants and white
endpoint. Degree-one covariance in dimensions two and three does not mean full
spatial white noise. Section~\ref{S:interval-upper} treats the higher exponents
by a separate argument. The intrinsic constant is identified  in
Theorem~\ref{T:intrinsic-second-moment}.

We retain the two-chain expansion of Proposition~\ref{P:mixed}, but estimate its
spatial and temporal factors in a different order. The spatial estimate keeps a
power of the number of pairs. After taking a common spatial maximum, we sum all
temporal pairings before using the ordered time domains.

Throughout this section $0 < \alpha_0 < 1$. We first work in dimension one with
either of the spatial covariances
\begin{equation}\label{E:d1-covariances}
  \begin{cases}
    \gamma(y)=c_\alpha|y|^{-\alpha},&0<\alpha<1,\quad c_\alpha>0,\\
    \gamma=c_\delta\delta_0,&\alpha=1,\quad c_\delta>0.
  \end{cases}
\end{equation}
Put $b = 2-\alpha$, $q = 3-\alpha$, $\beta = 4-\alpha-\alpha_0$, and
\begin{equation}\label{E:d1-constants}
  Z=\frac{2}{(1-\alpha_0)(2-\alpha_0)},\qquad
  K_{\rm sp}=
  \begin{cases}
    \displaystyle\frac{c_\alpha 2^{2-\alpha}(1-\alpha)^{-\alpha}}
    {(2-\alpha)^{2-\alpha}},&0<\alpha<1,\\[2mm]
    c_\delta,&\alpha=1.
  \end{cases}
\end{equation}
These parameters satisfy Hypothesis~\ref{H:homog}, so the fixed-order
integrability and mixed expansion already established apply.

\subsection{A spatial bound retaining the ordered increments}

For $m+n = 2k$, label the two chains in block order as in~\eqref{E:mixed-diagram}. For each vertex $l$ write
$h_l = s_l-s_{p(l)} > 0$ and $y_l = x_l-x_{p(l)}$, with a separate root zero
in each chain. Thus, $x_l$ is the sum of increments in its own chain
up to label $l$. The spatial change of variables has determinant one.
In this section $x_l$ denotes a spatial position and $y_l$ its increment; this local
notation differs from the position variables $y_l$
in~\eqref{E:mixed-diagram}. The terminal evaluation point of $u(t,x)$
remains denoted by $x$.
Let $p_\epsilon$ be the centered Brownian Gaussian density of variance
$\epsilon$ and mass one, and set
$\gamma_\epsilon = p_\epsilon*\gamma$. Allow a separate positive
$\epsilon_e$ for every pair $e \in D$ and define
\[
  S_{D,\boldsymbol\epsilon}(h)
  =\int_{\R^{2k}}\prod_{l=1}^{2k}G(h_l,y_l)
  \prod_{(i,j)\in D}\gamma_{\epsilon_{i,j}}(x_j-x_i)\ud y,
  \qquad G(h,y)=\tfrac12\mathbf1_{\{|y|<h\}}.
\]
This is an ordinary nonnegative integral; no pointwise delta value is used.

\begin{lemma}[Spatial estimate]\label{L:d1-spatial}
  Suppose~\eqref{E:d1-covariances} holds, $k \ge 1$, and $D$ is any pairing of
  the two chains. Orient every pair $(i,j)$ by $i < j$ and let $O_D$ and $C_D$
  be its opening and closing label sets. Then, uniformly in
  $\boldsymbol\epsilon$,
  \begin{equation}\label{E:d1-spatial-product}
    S_{D,\boldsymbol\epsilon}(h)\le
    \begin{cases}
      \displaystyle\left(\frac{c_\alpha}{1-\alpha}\right)^k
      \prod_{i\in O_D}h_i\prod_{j\in C_D}h_j^{1-\alpha},
      &0<\alpha<1,\\[2mm]
      \displaystyle\left(\frac{c_\delta}{2}\right)^k
      \prod_{i\in O_D}h_i,&\alpha=1.
    \end{cases}
  \end{equation}
  In particular, if $\sum_{l=1}^{2k}h_l \le 2t$, then
  \begin{equation}\label{E:d1-spatial-max}
    S_{D,\boldsymbol\epsilon}(h)
    \le K_{\rm sp}^{\,k}\frac{t^{bk}}{k^{bk}}.
  \end{equation}
\end{lemma}

\begin{proof}
  We first record the convolution bounds. For $0 < \alpha < 1$, the
  integral of the even decreasing function $|y|^{-\alpha}$ over an
  interval of fixed length is maximal when the interval is centered
  at zero. Therefore,
  \[
    \sup_z\int_\R G(h,y)c_\alpha|y+z|^{-\alpha}\ud y
    =\frac{c_\alpha h^{1-\alpha}}{1-\alpha}.
  \]
  By Tonelli's theorem, the integral with $\gamma_\epsilon$ equals the
  $p_\epsilon(w)\ud w$ average of the unsmoothed integrals with shifts $z-w$.
  Its nonnegative mass-one average is therefore bounded by the same supremum. In
  the white case, $\gamma_\epsilon = c_\delta p_\epsilon$, so
  \[
    \sup_z\int_\R G(h,y)\gamma_\epsilon(y+z)\ud y
    \le\frac{c_\delta}{2}.
  \]
  Both estimates are uniform in $\epsilon > 0$.

  Now integrate \emph{all} spatial increments in descending label order
  $2k,2k-1,\ldots,1$. Before processing label $l$, the remaining covariance
  factors are exactly those pairs whose closing labels are at most $l$; the
  bounds from the removed pairs depend only on $h$. If $l \in C_D$, its pair is
  $(i,l)$ with $i < l$ and $x_l-x_i = y_l+z$, where $z$ is independent of $y_l$.
  Every other remaining pair has both endpoints smaller than $l$, so its two
  positions are independent of $y_l$: positions involve only earlier increments
  in their own block chain. Thus, the only covariance involving $y_l$ is its own
  pair, and the convolution bound removes it. If $l \in O_D$, its partner has a
  larger label and its covariance factor has already been removed. All remaining
  covariances have endpoints smaller than $l$, so integration of $y_l$ gives
  only $\int G(h_l,y_l)\ud y_l = h_l$. This also preserves the stated invariant
  for the next label. Tonelli's theorem and the nonnegativity of all factors
  justify each step. There are $k$ labels of each type,
  proving~\eqref{E:d1-spatial-product} for every split and pairing.

  For Riesz covariance, weighted arithmetic--geometric mean gives
  \[
    \prod_{i\in O_D}h_i\prod_{j\in C_D}h_j^{1-\alpha}
    \le\left(\frac{2t}{bk}\right)^{bk}
    (1-\alpha)^{(1-\alpha)k}.
  \]
  Indeed, the weights are one at the $k$ openings and $1-\alpha$ at the $k$
  closings, with total $bk$, and the sum of the increments is at most $2t$.
  Multiplication by $(c_\alpha/(1-\alpha))^k$ gives~\eqref{E:d1-spatial-max}
  with the stated $K_{\rm sp}$. In the white case, $\prod_{i\in O_D}h_i \le
  (2t/k)^k$; multiplying by $(c_\delta/2)^k$ gives the same conclusion with $b =
  1$ and $K_{\rm sp} = c_\delta$. This proves Lemma~\ref{L:d1-spatial}.
\end{proof}

\subsection{Summing temporal pairings before using time ordering}

Define the total-order coefficients
\[
  A_k(t)=\sum_{m=0}^{2k}\E[X_m(t,x)X_{2k-m}(t,x)],\qquad A_0(t)=1.
\]
They do not depend on $x$, by spatial stationarity. By
Proposition~\ref{P:mixed}, $\E u^2(t,x) = \sum_{k\ge0}A_k(t)$.

\begin{proposition}[One-dimensional upper bound]\label{P:d1-upper}
  Under~\eqref{E:d1-covariances}, for every $k \ge 1$ and $t > 0$,
  \begin{equation}\label{E:d1-coefficient}
    A_k(t)\le
    \frac{(2ZK_{\rm sp})^k t^{\beta k}}{k!\,k^{bk}}
    \le\frac{(2ZK_{\rm sp})^k t^{\beta k}}{(k!)^q}.
  \end{equation}
  Consequently,
  \begin{equation}\label{E:d1-upper}
    \E u^2(t,x)\le\exp(C_2t^\kappa),\qquad
    C_2=q(2ZK_{\rm sp})^{1/q},\quad \kappa=\frac{\beta}{q}.
  \end{equation}
\end{proposition}

\begin{proof}
  We first work with the Gaussian spatial smoothing and temporal truncation
  in~\cite{chen:author2026:time-dependency}*{(2.9), (2.11), (2.23)--(2.24)}. Let
  $X_n^{\epsilon,\delta}$ be the smoothed Stratonovich term, using common
  parameters in every factor. Wick's formula expresses each mixed expectation of
  total order $2k$ as a sum over $D \in \Pi_k$. After the chain reversal in
  Proposition~\ref{P:mixed}, its spatial factor is the one in
  Lemma~\ref{L:d1-spatial}; its temporal factors are nonnegative and bounded by
  $|s_i-s_j|^{-\alpha_0}$. For times in $[0,t]^m_ < \times[0,t]^{2k-m}_ <$, the
  increments sum to the two terminal times and therefore to at most $2t$.
  Extract~\eqref{E:d1-spatial-max}, which is independent of the time vector, the
  split, the pairing, and the smoothing parameters. The remaining temporal sum
  is
  \[
    F_k(s_1,\ldots,s_{2k})
    =\sum_{D\in\Pi_k}\prod_{(i,j)\in D}|s_i-s_j|^{-\alpha_0}.
  \]
  Every permutation of the $2k$ labels bijects $\Pi_k$, so $F_k$ is fully
  symmetric. Moreover,
  \[
    \int_{[0,t]^2}|s-r|^{-\alpha_0}\ud s\ud r
    =Zt^{2-\alpha_0},\qquad
    \int_{[0,t]^{2k}}F_k(s)\ud s
    =P_k(Zt^{2-\alpha_0})^k<\infty.
  \]
  The second equality uses the disjoint endpoints of every pairing. Partitioning
  the time cube according to the order within each block now gives
  \begin{equation}\label{E:d1-time-symmetry}
    \int_{[0,t]^m_<\times[0,t]^{2k-m}_<}F_k(s)\ud s
    =\frac{P_k(Zt^{2-\alpha_0})^k}{m!(2k-m)!}.
  \end{equation}
  Ties have measure zero. Crucially, this symmetry is applied to the \emph{sum}
  of pairings after taking the common spatial bound, not to an individual
  temporally weighted diagram.

  The number of pairings obeys $P_0 = 1$ and $P_k = (2k-1)P_{k-1}$, by choosing
  the partner of the smallest label. Hence, $P_k = (2k)!/(2^kk!)$. The binomial
  identity gives
  \[
    \sum_{m=0}^{2k}\frac1{m!(2k-m)!}=\frac{2^{2k}}{(2k)!}.
  \]
  Multiplying~\eqref{E:d1-time-symmetry} by the spatial bound and summing over
  $m$ yields
  \[
    \sum_{m=0}^{2k}\E[X_m^{\epsilon,\delta}X_{2k-m}^{\epsilon,\delta}]
    \le K_{\rm sp}^{\,k}\frac{t^{bk}}{k^{bk}}
    \frac{2^{2k}}{(2k)!}
    \frac{(2k)!}{2^kk!}(Zt^{2-\alpha_0})^k
    =\frac{(2ZK_{\rm sp})^kt^{\beta k}}{k!\,k^{bk}}.
  \]
  The same proof covers empty chains, with $X_0^{\epsilon,\delta} = 1$.

  By Lemma~\ref{L:joint-fixed-order}, each smoothed factor converges in $L^2$.
  Products converge in $L^1$ by Cauchy--Schwarz; for fixed $k$ the sum over
  splits is finite. The bound is uniform in $\epsilon,\delta$, so it passes to
  $A_k(t)$. Since $k! \le k^k$ and $b > 0$, we have $k!\,k^{bk} \ge (k!)^{b+1} =
  (k!)^q$, proving both inequalities in~\eqref{E:d1-coefficient}.

  Finally, for $z \ge 0$ and $q \ge 1$,
  \[
    \sum_{k\ge0}\frac{z^k}{(k!)^q}
    =\sum_{k\ge0}\left(\frac{z^{k/q}}{k!}\right)^q
    \le\left(\sum_{k\ge0}\frac{z^{k/q}}{k!}\right)^q
    =\exp(qz^{1/q}).
  \]
  Apply this inequality with $z = 2ZK_{\rm sp}t^\beta$, adding the separately
  defined term $A_0 = 1$. Proposition~\ref{P:mixed} then
  gives~\eqref{E:d1-upper}. This proves Proposition~\ref{P:d1-upper}.
\end{proof}

\subsection{Spectral bounds for $0 < \alpha \le 1$ in all three dimensions}

We now retain Hypothesis~\ref{H:homog} with $d \in \{1,2,3\}$ and $0 < \alpha
\le 1$. The covariance is nonnegative and nonnegative definite as in
Section~\ref{S:model}; when it is a distribution, both these properties and its
homogeneity are understood distributionally. Let $\mu$ be its positive Radon
spectral measure in the convention $\gamma(x) = \int e^{i\xi\cdot
x}\mu(\ud\xi)$, and put $V = \mu(\{\xi:|\xi|\le1\})$. No isotropy or spectral
density is assumed. Write $G_h$ for the positive wave-kernel measure of mass
$h$, and $G_{h,\eta} = p_\eta*G_h$ for $\eta > 0$; set $G_{h,0} = G_h$. The
measure notation includes the sphere kernel in dimension three. The mixed-moment
definition of $A_k(t)$ is now applied to the present $d$-dimensional solution.

\begin{lemma}[Low-$\alpha$ convolution bound]\label{L:low-alpha-convolution}
  Under the preceding assumptions with $0 < \alpha < 1$, for every $R,h > 0$,
  \begin{equation}\label{E:low-alpha-radial}
    \mu(\{\xi:|\xi|\le R\})=VR^\alpha,\qquad
    \int_{\R^d}\min\{h,|\xi|^{-1}\}\mu(\ud\xi)
    =\frac{V}{1-\alpha}h^{1-\alpha}.
  \end{equation}
  For $\epsilon > 0$ and $\eta \ge 0$,
  \begin{equation}\label{E:low-alpha-convolution}
    0\le\int_{\R^d}G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
    \le\frac{V}{1-\alpha}h^{1-\alpha},
    \qquad z\in\R^d.
  \end{equation}
  The estimate is uniform in both smoothing parameters and in $z$.
\end{lemma}

\begin{proof}
  The spectral measure of $\gamma(c\,\cdot)$ is the pushforward of $\mu$ under
  $\xi\mapsto c\xi$. Homogeneity and uniqueness of the Fourier transform on
  tempered distributions therefore give $\mu(A/c) = c^{-\alpha}\mu(A)$ for every
  Borel set $A$. Equivalently, $\mu(cA) = c^\alpha\mu(A)$. This proves the
  ball-mass formula. Since $\mu$ is Radon, $V < \infty$, and continuity from
  above gives $\mu(\{0\}) = \lim_{R\downarrow0}VR^\alpha = 0$. By the layer-cake
  identity and Tonelli's theorem,
  \[
    \int_{\R^d}\min\{h,|\xi|^{-1}\}\mu(\ud\xi)
    =\int_0^h\mu(\{\xi:|\xi|\le u^{-1}\})\ud u
    =V\int_0^h u^{-\alpha}\ud u.
  \]
  The endpoint of each indicator has no effect on its $u$ integral. Since
  $\alpha < 1$, the last expression is the finite quantity
  in~\eqref{E:low-alpha-radial}. This computation uses ball masses, not a radial
  density for $\mu$.

  Gaussian weighting gives a finite measure, by the polynomial ball growth of
  $\mu$. Thus, Fourier Fubini is justified for $\gamma_\epsilon$ and the finite
  measure $G_{h,\eta}$. From the source's wave-kernel
  formulas~\cite{chen:author2026:time-dependency}*{(2.3)--(2.5), p.~7},
  \[
    \widehat{G}_h(\xi)=\frac{\sin(h|\xi|)}{|\xi|},\qquad
    G_h(\R^d)=h,
  \]
  with value $h$ in the Fourier formula at zero. The Fourier multipliers of
  $p_\epsilon$ and $p_\eta$ have absolute value at most one, with the latter
  multiplier equal to one when $\eta = 0$. Consequently,
  \[
    \left|\int G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)\right|
    \le\int_{\R^d}\frac{|\sin(h|\xi|)|}{|\xi|}\mu(\ud\xi)
    \le\int_{\R^d}\min\{h,|\xi|^{-1}\}\mu(\ud\xi).
  \]
  Nonnegativity of $\gamma$ as a distribution implies $\gamma_\epsilon \ge 0$,
  since Gaussian translates are nonnegative test functions; $G_{h,\eta}$ is also
  nonnegative. This proves the lower bound in~\eqref{E:low-alpha-convolution}.
  Combining the preceding displays proves its upper bound. No positivity of the
  oscillatory Fourier integrand is asserted. This proves
  Lemma~\ref{L:low-alpha-convolution}.
\end{proof}

\begin{lemma}[Degree-one convolution bound]\label{L:alpha-one-convolution}
  Under the preceding covariance assumptions with $\alpha = 1$, for every $h >
  0$, $\epsilon > 0$, $\eta \ge 0$, and $z \in \R^d$,
  \begin{equation}\label{E:alpha-one-convolution}
    0\le\int_{\R^d}G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
    \le\frac{\pi V}{2}.
  \end{equation}
  No isotropy or angular density is required.
\end{lemma}

\begin{proof}
  Fourier uniqueness, applied to the distributional homogeneity as above, gives
  $\mu(cA) = c\mu(A)$ and $\mu(\{0\}) = 0$. Define a finite measure on the unit
  sphere by
  \[
    \sigma(E)=\mu\{\xi:0<|\xi|\le1,\ \xi/|\xi|\in E\}.
  \]
  Its total mass is $V$. Homogeneity implies that the corresponding sector of
  radius $R$ has mass $R\sigma(E)$. Subtracting two such sectors shows that a
  polar rectangle $(r_1,r_2]\times E$ has mass $(r_2-r_1)\sigma(E)$. Uniqueness
  of measures on these generating rectangles therefore gives the polar
  decomposition $\mu(\ud\xi) = \ud r\,\sigma(\ud\theta)$, $r > 0$, $\theta \in
  \mathbb{S}^{d-1}$. The real stationary covariance is even; Fourier uniqueness
  makes $\mu$, and hence $\sigma$, even.

  Use the Brownian Gaussian convention, so the combined covariance and Green
  smoothing multiplier is $e^{-ar^2}$ with $a = (\epsilon+\eta)/2 > 0$. Gaussian
  weighting makes the spectral measure finite. Fourier Fubini and evenness give
  \begin{equation}\label{E:alpha-one-polar}
    \begin{split}
      \int G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
      &=\int_{\mathbb{S}^{d-1}} I_a(h,\theta\cdot z)\sigma(\ud\theta),\\
      I_a(h,v)&=\int_0^\infty e^{-ar^2}
      \frac{\sin(hr)}r\cos(rv)\ud r.
    \end{split}
  \end{equation}
  The radial integral is absolutely convergent: its integrand is bounded near
  zero and Gaussian-decaying at infinity. Passing from the complex exponential
  to cosine introduces no factor two, since both antipodal directions are
  already included in $\sigma$.

  Let $g_h(v) = \tfrac12\mathbf1_{\{|v|<h\}}$ and let $p_{2a}^{(1)}(v) = (4\pi
  a)^{-1/2}e^{-v^2/(4a)}$ be the one-dimensional Gaussian density. Their Fourier
  transforms are $\sin(hr)/r$ and $e^{-ar^2}$. The one-dimensional inversion
  factor is $1/(2\pi)$ in the source convention, so
  \[
    (g_h*p_{2a}^{(1)})(v)
    =\frac1{2\pi}\int_\R e^{irv}e^{-ar^2}
    \frac{\sin(hr)}r\ud r
    =\frac1\pi I_a(h,v).
  \]
  The sign in the inversion exponential is immaterial because the integrand
  pairs evenly under $r\mapsto-r$. Since $p_{2a}^{(1)}$ has mass one and $0 \le
  g_h \le 1/2$, we obtain $0 \le I_a(h,v) \le \pi/2$. Integrating against
  $\sigma$, whose mass is $V$, proves~\eqref{E:alpha-one-convolution}. This
  retains the oscillation until the one-dimensional integral is evaluated; the
  divergent absolute Fourier envelope at $\alpha = 1$ is not used. This proves
  Lemma~\ref{L:alpha-one-convolution}.
\end{proof}

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

\begin{remark}[Scope of the spectral estimates]\label{R:low-alpha-scope}
  If $V = 0$, spectral homogeneity gives $\mu(B_R) = 0$ for every $R$, hence
  $\mu = 0$ and $u = 1$; the noise-free conclusion is immediate. Otherwise, all
  angular and dimensional dependence is allowed in $V$. For $0 < \alpha < 1$,
  the example $\gamma(x) = c|x_1|^{-\alpha}$ in dimensions two or three has its
  spectral measure supported on an axis; a full-dimensional density is not
  required. The absolute Fourier envelope diverges at $\alpha = 1$, where the
  separate oscillatory calculation in Lemma~\ref{L:alpha-one-convolution} is
  essential. The endpoint is not obtained by taking a limit in $K_{\rm sp}^{\rm
  gen}$ for $\alpha < 1$. For $d = 1$ and $\gamma = c_\delta\delta_0$, the
  source convention gives $\mu(\ud\xi) = c_\delta\ud\xi/(2\pi)$ and $V =
  c_\delta/\pi$. Hence, the endpoint constant $K_{\rm sp}^{\rm gen} = \pi V =
  c_\delta$ agrees exactly with Proposition~\ref{P:d1-upper}, with no extra
  antipodal factor. In dimensions two and three the endpoint covers degree-one
  homogeneous covariance, not full spatial white noise. No result for $\alpha >
  1$ follows from these estimates.
\end{remark}

\subsection{Checks on the scale, constants and scope}

\begin{corollary}[First-moment calibration]\label{C:d1-first-calibration}
  Let $K_*$ be $K_{\rm sp}$ under~\eqref{E:d1-covariances}, or $K_{\rm sp}^{\rm
  gen}$ under the hypotheses of Proposition~\ref{P:low-alpha-upper}. Put
  $C_{2,*} = q(2ZK_*)^{1/q}$. Then
  \begin{equation}\label{E:d1-first-calibration}
    \E u(t,x)\le\exp(C_{1,*}t^\kappa),\qquad
    C_{1,*}=q\left(\frac{ZK_*}{2^{3-\alpha}}\right)^{1/q}
    =\frac{C_{2,*}}{2^{(4-\alpha)/(3-\alpha)}}.
  \end{equation}
  In either nonzero case $2C_{1,*} < C_{2,*}$. Conditionally on a first-moment
  lower rate at least $L_*$, $2L_* \le 2C_{1,*} < C_{2,*}$, consistently with
  Proposition~\ref{P:Jensen}.
\end{corollary}

\begin{proof}
  For one chain of length $2k$, the increments sum to at most $t$. The spatial
  estimate in Lemma~\ref{L:d1-spatial}, or in the proof of
  Proposition~\ref{P:low-alpha-upper}, therefore applies with $t/2$ in place of
  $t$. The temporal pairing sum on one ordered simplex is
  $P_k(Zt^{2-\alpha_0})^k/(2k)!$. Using the same regularization and limit order
  as in the respective upper-bound proof gives
  \[
    \E X_{2k}(t,x)
    \le\frac{(ZK_*/2^{b+1})^k t^{\beta k}}{k!\,k^{bk}}
    \le\frac{(ZK_*/2^{3-\alpha})^k t^{\beta k}}{(k!)^q}.
  \]
  Every odd term has zero expectation. The $L^2$ expansion permits taking
  expectations of partial sums, and the resulting nonnegative even series is
  summed by the scalar inequality in the proof of Proposition~\ref{P:d1-upper}.
  This gives~\eqref{E:d1-first-calibration}. If the first-moment lower rate is
  at least $L_*$, \eqref{E:d1-first-calibration} implies $L_* \le C_{1,*}$. In
  the stated nonzero cases $K_* > 0$, hence $C_{1,*} > 0$; and
  $(4-\alpha)/(3-\alpha) > 1$ gives $2C_{1,*} < C_{2,*}$. This proves
  Corollary~\ref{C:d1-first-calibration}.
\end{proof}

\begin{remark}[Checks and comparison with the uniform pairing bound]\label{R:d1-upper-checks}
  The argument preserves the factor $k^{-(2-\alpha)k}$ from the spatial
  increment maximum. Replacing the spatial volume merely by a constant times
  $t^{(2-\alpha)k}$ would lose the factorial power needed
  in~\eqref{E:d1-coefficient}. This proof does not use the
  common-Laplace-parameter norm majorant of Proposition~\ref{P:envelope}, and it
  does not assert a stronger factorial estimate for every individual diagram.
  Instead, the temporal ordering is exploited after summing pairings
  in~\eqref{E:d1-time-symmetry}. Thus, the scoped G0 obstruction remains valid.
  For unit white covariance, the bound on the total-order-two coefficient is
  $2Z$, whereas the exact value from Lemma~\ref{L:white-test} is $2c_0$; their
  ratio is $2(3-\alpha_0) > 4$. At the static endpoint the exact order-four
  coefficient is $11/540$, while the first bound in~\eqref{E:d1-coefficient}
  gives $1/2$. These are checks of normalization, not evidence of sharp
  constants.
\end{remark}

No-go~\ref{P:nogo-06} quantifies the loss avoided here: discarding the
spatial constraints before summation gives the wrong time exponent.


\begin{remark}[Boundary and literature comparisons]\label{R:d1-comparisons}
  As $\alpha_0\downarrow0$, the time exponent tends to $(4-\alpha)/(3-\alpha)$,
  the Chen--Hu static exponent cited in Remark~\ref{R:G1-scope}. This is an
  exponent calibration, not an interchange of the static and large-time limits.
  With the Riesz normalization $c_\alpha = (1-\alpha)/2$, the displayed $K_{\rm
  sp}$ tends to one as $\alpha\uparrow1$, matching unit white covariance. For
  comparison only, the Skorohod upper bound of
  Balan--Conus~\cite{balan.conus:16:intermittency}*{Theorem~2.1(b), (8), (10),
  p.~1492} has time exponent $(2H+2-a)/(3-a)$. Setting $H = 1-\alpha_0/2$ and $a
  = \alpha$ yields the same $\kappa$. Their covariance normalization contains
  $H(2H-1)$ and they use a Skorohod mild solution. No constants or solutions are
  identified, and their theorem is not an input to the present proof. The
  current coverage of this section is $0 < \alpha \le 1$ in $d = 1,2,3$,
  including the one-dimensional white case. It does not address $1 < \alpha <
  2-\alpha_0$ in dimensions two and three.
\end{remark}


# Full wave-variance section
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
