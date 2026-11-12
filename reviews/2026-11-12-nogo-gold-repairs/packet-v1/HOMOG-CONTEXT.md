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