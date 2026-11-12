# Frozen candidate: two approved deterministic clarifications

## Damped norms, complete definitions, lemma and proof

```latex
\section{Recovering the quadratic-exponential bound}

Write $G_\theta(s,y) = e^{-\theta s}G(s,y)$ and $\widehat{G}_s(\xi) =
\sin(s|\xi|)/|\xi|$, with value $s$ at $\xi = 0$. We use the norms in the
source's (3.3)--(3.5), with the full covariance, but give their bounds directly.
Write $\Gamma_{\mathrm{E}}$ for Euler's Gamma function in the following
definitions, to distinguish it from the covariance measure:
\begin{equation}\label{E:damped-norm-definitions}
  \begin{split}
    N_0(\theta)&=\int_0^\infty e^{-\theta s}G_s(\R^d)\ud s,\\
    N_1(\theta)&=\frac1{\Gamma_{\mathrm{E}}(\alpha_0)}
    \int_0^\infty\lambda^{\alpha_0-1}\ud\lambda
    \int\frac{\mu(\ud\xi)}{(\theta+\lambda)^2+|\xi|^2},\\
    N_2(\theta)^2&=\int_0^\infty\int_0^\infty
    e^{-\theta(s+t)}|s-t|^{-\alpha_0}
    \int\widehat{G}_s(\xi)\overline{\widehat{G}_t(\xi)}
    \mu(\ud\xi)\ud s\ud t.
  \end{split}
\end{equation}
The second expression uses the elementary wave Laplace transform $\int_0^\infty
e^{-as}\widehat{G}_s(\xi)\ud s = (a^2+|\xi|^2)^{-1}$. The last expression is the
space-time covariance quadratic form; in physical variables it pairs
$G_\theta(s,x)$ with $G_\theta(t,y)$. Thus, the second Green factor in the
printed source (3.5) is read with the independent variable $y$; see
Lemma~\ref{L:translated-covariance-CS} and
Remark~\ref{R:source-case2-time-shift} for the independent justification and the
exact source qualification.

\begin{lemma}[Homogeneous damped norms and temporal tails]
  \label{L:damped-homogeneous-norms}
  Under Hypothesis~\ref{H:homog}, the integrals
  in~\eqref{E:damped-norm-definitions} are finite for every $\theta > 0$, with
  $N_2(\theta)^2 \ge 0$, and
  \[
    N_0(\theta)=\theta^{-2},\qquad
    N_1(\theta)=\theta^{\alpha+\alpha_0-2}N_1(1),\qquad
    N_2(\theta)^2=\theta^{-\beta}N_2(1)^2,
    \quad\beta=4-\alpha-\alpha_0.
  \]
  Let
  \[
    K_M(r)=\frac1{\Gamma_{\mathrm{E}}(\alpha_0)}
    \int_M^\infty e^{-\lambda|r|}\lambda^{\alpha_0-1}\ud\lambda.
  \]
  Denote by $N_1^{(M)}(1)$ the first norm with $\lambda > M$, and by
  $N_2^{(M)}(1)$ the second norm with $K_M(s-t)$ in place of
  $|s-t|^{-\alpha_0}$. Then
  \begin{equation}\label{E:damped-tail-norms}
    N_1^{(M)}(1)\longrightarrow0,\qquad
    N_2^{(M)}(1)\longrightarrow0\quad(M\to\infty).
  \end{equation}
  More precisely, let $m:\R^d\to[0,1]$ be measurable and let
  $S\subset S'\subset(0,\infty)$ be measurable. Define $N_{1,m,S}(\theta)$
  by replacing $\mu$ with $m\mu$ and restricting the $\lambda$ integral in
  $N_1$ to $S$. Define $N_{2,m,S}(\theta)^2$ by replacing $\mu$ with $m\mu$
  and the temporal kernel in $N_2^2$ with
  \[
    K_S(r)=\frac1{\Gamma_{\mathrm{E}}(\alpha_0)}
    \int_S e^{-\lambda|r|}\lambda^{\alpha_0-1}\ud\lambda.
  \]
  Then, for every $\theta>0$,
  \begin{equation}\label{E:damped-multiplier-comparison}
    \begin{split}
      0\le N_{1,m,S}(\theta)&\le N_{1,1,S'}(\theta),\\
      0\le N_{2,m,S}(\theta)^2&\le N_{2,1,S'}(\theta)^2.
    \end{split}
  \end{equation}
  These are comparisons of spectral expressions, including full and tail
  domains. An arbitrary $m$ need not preserve Hypothesis~\ref{H:homog}; the
  scaling identities above are asserted for the original covariance only.
  Spatial Gaussian smoothing and Gaussian smoothing of the Green kernel
  give multipliers in this class. The separate mass identity for $N_0$ is
  unchanged by Gaussian smoothing of the Green kernel.
\end{lemma}

\begin{proof}
  Scaling the Fourier representation of $\Gamma$ and using Fourier uniqueness
  gives $\mu(cA) = c^\alpha\mu(A)$. Radon finiteness and $\alpha > 0$ then imply
  $\mu(\{0\}) = 0$. In particular, $\mu(B_r) = r^\alpha V$, where $V = \mu(B_1)
  < \infty$. Therefore, for $a > 0$,
  \[
    \int\frac{\mu(\ud\xi)}{a^2+|\xi|^2}
    =\alpha V a^{\alpha-2}
    \int_0^\infty\frac{u^{\alpha-1}}{1+u^2}\ud u<\infty.
  \]
  The last integral is finite since $0 < \alpha < 2$. Substitution into $N_1$
  reduces its finiteness to
  $\int_0^\infty\lambda^{\alpha_0-1}(\theta+\lambda)^{\alpha-2} \ud\lambda <
  \infty$: the conditions at zero and infinity are $\alpha_0 > 0$ and
  $\alpha+\alpha_0 < 2$.

  For $N_2$ use $|\widehat{G}_s(\xi)| \le \min(s,|\xi|^{-1})$. On $|\xi| \le 1$,
  absolute integration is bounded by
  \[
    V\int_0^\infty\int_0^\infty
    e^{-\theta(s+t)}|s-t|^{-\alpha_0}st\ud s\ud t<\infty.
  \]
  On $|\xi| > 1$, use $\int_{|\xi|>1}|\xi|^{-2}\mu(\ud\xi) = \alpha
  V/(2-\alpha)$ and the same time integral without $st$. Both time integrals are
  finite by splitting into $s \le t$ and $t \le s$, then using $u = \min(s,t)$
  and $v = |s-t|$; the only singular factor is $v^{-\alpha_0}$, with $\alpha_0 <
  1$. This proves absolute integrability of the displayed spectral formula. For
  each $\xi$, its time integral is nonnegative because the temporal kernel is
  positive definite. Indeed, it is a positive Laplace mixture of the kernels
  $e^{-\lambda|s-t|}$. This proves $N_2(\theta)^2 \ge 0$.

  The mass identity $G_s(\R^d) = s$ proves the formula for $N_0$. In $N_1$
  change $\lambda = \theta u$ and $\xi = \theta\eta$. In $N_2$ change $s =
  u/\theta$, $t = v/\theta$ and $\xi = \theta\eta$, using
  $\widehat{G}_{u/\theta}(\theta\eta) = \theta^{-1}\widehat{G}_u(\eta)$. These
  changes give exactly the stated powers.

  The first tail in~\eqref{E:damped-tail-norms} is a tail of the finite
  nonnegative $N_1(1)$ integral. For the second, $0 \le K_M(r) \le
  |r|^{-\alpha_0}$ and $K_M(r) \to 0$ for $r \ne 0$. The absolute majorant just
  proved permits dominated convergence in $(s,t,\xi)$, giving $N_2^{(M)}(1)^2
  \to 0$. The tail kernel is positive definite by the same Laplace-mixture
  argument, so its quadratic form is nonnegative.

  For the multiplier comparisons, define
  \[
    B_\theta(\lambda,\xi)=\int_0^\infty\int_0^\infty
    e^{-\theta(s+t)}e^{-\lambda|s-t|}
    \widehat G_s(\xi)\overline{\widehat G_t(\xi)}\ud s\ud t.
  \]
  For each $\lambda>0$ and $\xi$, the positive definiteness of
  $e^{-\lambda|s-t|}$ gives $B_\theta(\lambda,\xi)\ge0$.
  The absolute-integrability bound above, $0\le m\le1$ and
  $0\le K_S\le|\cdot|^{-\alpha_0}$ justify changing the integration order:
  \[
    N_{2,m,S}(\theta)^2
    =\frac1{\Gamma_{\mathrm{E}}(\alpha_0)}
    \int_S\lambda^{\alpha_0-1}
    \int m(\xi)B_\theta(\lambda,\xi)\mu(\ud\xi)\ud\lambda.
  \]
  Nonnegativity now proves the second comparison
  in~\eqref{E:damped-multiplier-comparison}. It is used after time integration,
  not pointwise on the oscillating product of wave Fourier kernels. The first
  comparison follows directly from the nonnegative integrand defining $N_1$.
  The choices $S=(0,\infty)$ or $S=(M,\infty)$ give the full or tail bounds.
  Gaussian spatial and Green smoothing contribute products of multipliers in
  $[0,1]$ depending only on $\xi$. Gaussian Green smoothing also preserves
  $G_s(\R^d)=s$, proving its separate assertion for $N_0$. This proves
  Lemma~\ref{L:damped-homogeneous-norms}.
\end{proof}


```

## Spatial occupation module, complete current source

```latex
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

```
