# Exact manuscript diff against the baseline

```diff
diff --git a/notes/integrated_spatial_occupation.tex b/notes/integrated_spatial_occupation.tex
index 0031860..a987dca 100644
--- a/notes/integrated_spatial_occupation.tex
+++ b/notes/integrated_spatial_occupation.tex
@@ -95,6 +95,74 @@ its usual pointwise sense.
   Lemma~\ref{L:spatial-static-controls}.
 \end{proof}
 
+The next estimate also allows zero covariance and does not use the finiteness
+of $S_1^{\mathrm{pos}}$.
+
+\begin{lemma}[Deterministic Fourier bound for the spatial energy]
+  \label{L:spatial-fourier-bound}
+  Under Hypothesis~\ref{H:homog}, allowing $\Gamma=0$, let
+  $g\in C_c^\infty(\R^d;\R)$ satisfy $\|g\|_2=1$ and put
+  $b=\|\nabla g\|_2^2$. Then $b>0$ and
+  \begin{equation}\label{E:spatial-fourier-bound}
+    0\le A_{\mathrm{sp}}(g)
+    \le 2^{1+\alpha}R_\alpha b^{\alpha/2},
+  \end{equation}
+  where $R_\alpha$ is defined in~\eqref{E:intro-spectral-mass}.
+\end{lemma}
+
+\begin{proof}
+  If $b=0$, smoothness makes $\nabla g=0$ everywhere. Thus, $g$ is constant,
+  and compact support forces $g=0$, contrary to $\|g\|_2=1$. Put $Q=g^2$ and
+  use the unnormalized Fourier transform
+  \[
+    \mathcal{F}_0Q(\xi)=\int_{\R^d}e^{-i\xi\cdot x}Q(x)\ud x.
+  \]
+  In the unitary convention of Section~\ref{S:masked-covariance}, this is
+  $c_d^{-1}\widehat Q$, with $c_d=(2\pi)^{-d/2}$.
+  The autocorrelation
+  \[
+    c_Q(y)=\int_{\R^d}Q(x)Q(x-y)\ud x
+  \]
+  is smooth and compactly supported. Apply the distributional spectral
+  identity~\eqref{E:masked-spectral-convention} to this Schwartz function.
+  Its inner Fourier integral is $|\mathcal{F}_0Q(\xi)|^2$, since $Q$ is real.
+  Hence
+  \[
+    A_{\mathrm{sp}}(g)=\int c_Q(y)\Gamma(\ud y)
+    =\int|\mathcal{F}_0Q(\xi)|^2\mu(\ud\xi).
+  \]
+  Both integrals are finite: $c_Q$ is compactly supported and $\Gamma$ is
+  Radon, while $|\mathcal{F}_0Q|^2$ is Schwartz and $\mu$ is tempered.
+  No density of either measure is required.
+
+  Since $\|Q\|_1=1$, we have $|\mathcal{F}_0Q|\le1$. Integration by parts
+  and the Cauchy--Schwarz inequality give
+  \[
+    |\xi|\,|\mathcal{F}_0Q(\xi)|
+    \le\|\nabla Q\|_1
+    \le2\|g\|_2\|\nabla g\|_2=2\sqrt b.
+  \]
+  Splitting into $|\xi|^2\le4b$ and $|\xi|^2>4b$ therefore yields
+  \[
+    |\mathcal{F}_0Q(\xi)|^2\le\frac{8b}{4b+|\xi|^2}.
+  \]
+  The deterministic resolvent calculation in the proof of
+  Lemma~\ref{L:damped-homogeneous-norms}, together
+  with~\eqref{E:intro-spectral-mass}, gives, for $q>0$,
+  \[
+    \mathcal{R}_\Gamma(q):=\int\frac{\mu(\ud\xi)}{q^2+|\xi|^2}
+    =q^{\alpha-2}R_\alpha<\infty.
+  \]
+  Consequently,
+  \[
+    A_{\mathrm{sp}}(g)\le8b\mathcal{R}_\Gamma(2\sqrt b)
+    =2^{1+\alpha}R_\alpha b^{\alpha/2}.
+  \]
+  Nonnegativity follows from the spectral identity. If $\Gamma=0$, then
+  $\mu=0$ and both sides of~\eqref{E:spatial-fourier-bound} vanish. This proves
+  Lemma~\ref{L:spatial-fourier-bound}.
+\end{proof}
+
 \begin{proposition}[The finite smooth spatial ratio]
   \label{P:spatial-smooth-ratio}
   For real unit $g \in C_c^\infty(\R^d)$ put $R(g) =
@@ -112,9 +180,13 @@ its usual pointwise sense.
   The gradient energy $b(g)$ is positive: a nonzero $L^2$ function with zero
   weak gradient would have Fourier transform supported only at zero, and hence
   would vanish. Its square is nonnegative nonzero smooth compact, so the
-  autocorrelation argument in the preceding proof gives $0 < A: =
-  A_{\mathrm{sp}}(g) < \infty$. With $U_\ell g(x) = \ell^{d/2}g(\ell x)$, the
-  physical changes of variables give
+  autocorrelation argument in the proof of
+  Lemma~\ref{L:spatial-static-controls} gives
+  $0 < A:=A_{\mathrm{sp}}(g)<\infty$. Lemma~\ref{L:spatial-fourier-bound} gives
+  $R(g)\le2^{1+\alpha}R_\alpha$ for every such profile. A normalized compact
+  bump supplies a positive ratio. Thus, $0<R_0<\infty$, independently of the
+  finiteness of $S_1^{\mathrm{pos}}$. It remains to prove the score inequality.
+  With $U_\ell g(x)=\ell^{d/2}g(\ell x)$, the physical changes of variables give
   \begin{equation}\label{E:spatial-dilation}
     A_{\mathrm{sp}}(U_\ell g)=\ell^\alpha A,\qquad
     b(U_\ell g)=\ell^2b(g).
@@ -138,11 +210,9 @@ its usual pointwise sense.
   \]
   Its maximum occurs at $L^k = 1/(qC)$ and is $(k/q)(qC)^{-1/k}$. Since $1+u =
   4/q$, $1/(q^qC) = R(g)\alpha^{\alpha/2}/(8M_aq^{q/2})$,
-  proving~\eqref{E:spatial-smooth-score}. The already finite
-  $S_1^{\mathrm{pos}}$ bounds every ratio by
-  $8M_aq^{q/2}(S_1^{\mathrm{pos}}/k)^k/\alpha^{\alpha/2}$. A normalized compact
-  bump supplies a positive ratio. This proves positivity and finiteness of $R_0$
-  before any rough spatial extension is invoked. This proves
+  proving~\eqref{E:spatial-smooth-score}. This argument retains the finite
+  real value $S_1^{\mathrm{pos}}$ fixed at the start of the section; only the
+  proof of $R_0<\infty$ is independent of that input. This proves
   Proposition~\ref{P:spatial-smooth-ratio}.
 \end{proof}
 
diff --git a/notes/notes_stratonovich_ham_second_moment.tex b/notes/notes_stratonovich_ham_second_moment.tex
index 2d0c700..ab14275 100644
--- a/notes/notes_stratonovich_ham_second_moment.tex
+++ b/notes/notes_stratonovich_ham_second_moment.tex
@@ -822,9 +822,28 @@ exact source qualification.
     N_1^{(M)}(1)\longrightarrow0,\qquad
     N_2^{(M)}(1)\longrightarrow0\quad(M\to\infty).
   \end{equation}
-  Spatial Gaussian smoothing, Gaussian smoothing of the Green kernel, and
-  restriction of a temporal Laplace domain do not increase these corresponding
-  full or tail norm bounds.
+  More precisely, let $m:\R^d\to[0,1]$ be measurable and let
+  $S\subset S'\subset(0,\infty)$ be measurable. Define $N_{1,m,S}(\theta)$
+  by replacing $\mu$ with $m\mu$ and restricting the $\lambda$ integral in
+  $N_1$ to $S$. Define $N_{2,m,S}(\theta)^2$ by replacing $\mu$ with $m\mu$
+  and the temporal kernel in $N_2^2$ with
+  \[
+    K_S(r)=\frac1{\Gamma_{\mathrm{E}}(\alpha_0)}
+    \int_S e^{-\lambda|r|}\lambda^{\alpha_0-1}\ud\lambda.
+  \]
+  Then, for every $\theta>0$,
+  \begin{equation}\label{E:damped-multiplier-comparison}
+    \begin{split}
+      0\le N_{1,m,S}(\theta)&\le N_{1,1,S'}(\theta),\\
+      0\le N_{2,m,S}(\theta)^2&\le N_{2,1,S'}(\theta)^2.
+    \end{split}
+  \end{equation}
+  These are comparisons of spectral expressions, including full and tail
+  domains. An arbitrary $m$ need not preserve Hypothesis~\ref{H:homog}; the
+  scaling identities above are asserted for the original covariance only.
+  Spatial Gaussian smoothing and Gaussian smoothing of the Green kernel
+  give multipliers in this class. The separate mass identity for $N_0$ is
+  unchanged by Gaussian smoothing of the Green kernel.
 \end{lemma}
 
 \begin{proof}
@@ -871,13 +890,30 @@ exact source qualification.
   \to 0$. The tail kernel is positive definite by the same Laplace-mixture
   argument, so its quadratic form is nonnegative.
 
-  Spatial and Green Gaussian smoothing multiply the spectral integrals by
-  factors in $[0,1]$. For $N_1$ the integrand is nonnegative. For $N_2$, first
-  integrate in time: the quadratic form at each $\xi$ is nonnegative, so its
-  Gaussian multiplier can be removed in an upper bound. Restricting a temporal
-  Laplace domain likewise decreases the first norm and its nonnegative
-  covariance quadratic form. This proves all smoothing and truncation
-  assertions, including the bounds for temporal tails. This proves
+  For the multiplier comparisons, define
+  \[
+    B_\theta(\lambda,\xi)=\int_0^\infty\int_0^\infty
+    e^{-\theta(s+t)}e^{-\lambda|s-t|}
+    \widehat G_s(\xi)\overline{\widehat G_t(\xi)}\ud s\ud t.
+  \]
+  For each $\lambda>0$ and $\xi$, the positive definiteness of
+  $e^{-\lambda|s-t|}$ gives $B_\theta(\lambda,\xi)\ge0$.
+  The absolute-integrability bound above, $0\le m\le1$ and
+  $0\le K_S\le|\cdot|^{-\alpha_0}$ justify changing the integration order:
+  \[
+    N_{2,m,S}(\theta)^2
+    =\frac1{\Gamma_{\mathrm{E}}(\alpha_0)}
+    \int_S\lambda^{\alpha_0-1}
+    \int m(\xi)B_\theta(\lambda,\xi)\mu(\ud\xi)\ud\lambda.
+  \]
+  Nonnegativity now proves the second comparison
+  in~\eqref{E:damped-multiplier-comparison}. It is used after time integration,
+  not pointwise on the oscillating product of wave Fourier kernels. The first
+  comparison follows directly from the nonnegative integrand defining $N_1$.
+  The choices $S=(0,\infty)$ or $S=(M,\infty)$ give the full or tail bounds.
+  Gaussian spatial and Green smoothing contribute products of multipliers in
+  $[0,1]$ depending only on $\xi$. Gaussian Green smoothing also preserves
+  $G_s(\R^d)=s$, proving its separate assertion for $N_0$. This proves
   Lemma~\ref{L:damped-homogeneous-norms}.
 \end{proof}
 

```
