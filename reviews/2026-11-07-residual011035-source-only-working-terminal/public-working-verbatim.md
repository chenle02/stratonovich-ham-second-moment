## PROOF011

**Statement (P:white-four).** Let \(d=\alpha=1\), \(\gamma=\delta_0\), and keep the normalization
\[
G(s,y)=\frac12\mathbf1_{\{|y|<s\}},\qquad
\operatorname{Cov}\text{ time factor }= |s-r|^{-\alpha_0},\quad 0<\alpha_0<1.
\]
For \(a,b,c\ge0\) define
\[
F(a,b,c)=4ab-(a+b-c)_+^2+(|a-b|-c)_+^2,
\]
the area of \(\{(x,y):|x|<a,|y|<b,|x-y|<c\}\). With the three pairings of four vertices
\[
A=\{(1,2),(3,4)\},\quad B=\{(1,3),(2,4)\},\quad C=\{(1,4),(2,3)\},
\]
each \(J_{m,n,D}(t)\), \(m+n=4\), is a nonnegative integral of
\(V(q_1q_2)^{-\alpha_0}\) over its row domain, with the exact table
\[
\begin{array}{c|c|c|c|c}
(m,n)&D&V&q_1&q_2\\ \hline
(0,4)&A&ac/4&b&d\\
(0,4)&B&a\min(b,c,d)/4&b+c&c+d\\
(0,4)&C&a\min(b,d)/4&b+c+d&c\\ \hline
(1,3)&A&\min(r,a)b/4&|r-a|&c\\
(1,3)&B&F(r,a,\min(b,c))/16&|r-a-b|&b+c\\
(1,3)&C&F(r,a,c)/16&|r-a-b-c|&b\\ \hline
(2,2)&A&ac/4&b&d\\
(2,2)&B&\min(a,c)\min(b,d)/4&|a-c|&|a+b-c-d|\\
(2,2)&C&F(a,c,\min(b,d))/16&|a-c-d|&|a+b-c|
\end{array}
\]
with domains
\[
(0,4):a,b,c,d>0,\ a+b+c+d<t;\qquad
(1,3):0<r<t,\ a,b,c>0,\ a+b+c<t;\qquad
(2,2):a,b,c,d>0,\ a+b<t,\ c+d<t.
\]
The partition split is \((0,4),(1,3),(2,2)\). The total-order-four contribution is
\[
2\sum_{D\in\{A,B,C\}}J_{0,4,D}(t)
+2\sum_{D\in\{A,B,C\}}J_{1,3,D}(t)
+\sum_{D\in\{A,B,C\}}J_{2,2,D}(t),
\]
and every row scales as \(t^{6-2\alpha_0}\).

**Derivation.** Two delta covariances pin the two spatial pairs, so spatial integration leaves the areas listed from the position lists:
\[
(x,x,y,y),(x,y,x,y),(x,y,y,x)
\]
for the single chain \(A,B,C\), i.e. areas \(4ac,\ 4a\min(b,c,d),\ 4a\min(b,d)\); for \((1,3)\) the single position is \(x\) and the long-chain lists are \((x,y,y),(y,x,y),(y,y,x)\) giving \(4\min(r,a)b,\ F(r,a,\min(b,c)),\ F(r,a,c)\); for \((2,2)\) the lists are \((x,x),(y,y)\), \((x,y),(x,y)\), \((x,y),(y,x)\) giving \(4ac,\ 4\min(a,c)\min(b,d),\ F(a,c,\min(b,d))\). The \(1/16\) is exactly the product \((1/2)(1/2)\) of the two Green factors. Reading paired times yields \(q_1,q_2\). Exchange of the two chains gives the \((4,0),(3,1)\) sums without changing covariance factors. Scaling: four time Jacobians \(t^4\), area \(t^2\), two covariance factors \(t^{-2\alpha_0}\).

**Consumed hypotheses/conditions.** \(d=\alpha=1\), \(\gamma=\delta_0\), \(G(s,y)=\tfrac12\mathbf1_{\{|y|<s\}}\), \(0<\alpha_0<1\). The distributional delta integration is justified by spatial approximate identities with the uniform bound \(2^2/16=1/4\); no pointwise delta value is used. No all-order conclusion follows.

---

## PROOF012

**Statement (L:static-four).** As \(\alpha_0\downarrow0\), each unit-time coefficient converges to
\[
\begin{array}{c|ccc|c}
(m,n)&A&B&C&\text{sum}\\ \hline
(0,4)&1/2880&1/8640&1/5760&11/17280\\
(1,3)&1/576&29/34560&1/640&143/34560\\
(2,2)&1/144&1/480&31/17280&187/17280
\end{array}
\]
The static total-order-four contribution is \(11t^6/540\); the static total-order-two contribution is \(t^3/3\) (from `L:white-test` at \(\alpha_0=0\)). These are coefficients, not large-time constants.

**Derivation.** On the unit-time domain all positions are in \([-1,1]\), so the spatial factor is bounded by \(1/4\) (two free positions in a \(2\times2\) square). For a fixed \(0<\bar a<1\) and \(0\le\alpha_0\le\bar a\), the two temporal factors are dominated by the exponent-\(\bar a\) product whose full-cube integral is
\[
\left(\int_0^1\int_0^1|s-t|^{-\bar a}\ud s\ud t\right)^2
=\left(\frac{2}{(1-\bar a)(2-\bar a)}\right)^2<\infty,
\]
because the two pairs use disjoint labels. Dominated convergence sets \(\alpha_0=0\). The resulting static value is evaluated via
\[
J_{m,n,D}(1)\big|_{\alpha_0=0}
=\frac1{16\,m!\,n!}\int_{\R^2}(1-L_1(x,y))_+^m(1-L_2(x,y))_+^n\ud x\ud y,
\]
with empty-chain factor one, where \(L_1,L_2\) are the two chain lengths; the sector computation gives exactly the `sector-values` table, and each value follows from \(\int_{u,v\ge0}(1-pu-qv)_+^4\ud u\ud v=1/(30pq)\) and the explicitly displayed \((2,2)\) integrals. Summing and multiplying by \(2/(16\,m!\,n!)\), then applying the multiplicities of (2.1), gives \(11/540\).

**Consumed hypotheses/conditions.** Same as PROOF011. The passage uses disjoint-pair dominated convergence only; it does not exchange \(t\to\infty\) and \(\alpha_0\downarrow0\), and it does not prove any all-order factorial power.

---

## PROOF013

**Statement (P:riesz-small).** Let \(d=1\), \(0<\alpha<1\), \(0<\alpha_0<1\), \(\gamma(y)=c_\alpha|y|^{-\alpha}\), \(c_\alpha>0\), and \(\beta=4-\alpha-\alpha_0\). Then
\[
\begin{aligned}
\E X_2(t,x)
&=
\frac{c_\alpha t^\beta}
{(1-\alpha)(2-\alpha-\alpha_0)(3-\alpha-\alpha_0)(4-\alpha-\alpha_0)},\\
\E X_1(t,x)^2
&=\frac{c_\alpha}{(1-\alpha)(2-\alpha)}
\int_0^t v^{-\alpha_0}
\Big[\frac{(2t-v)^{3-\alpha}-v^{3-\alpha}}{2(3-\alpha)}
-(t-v)v^{2-\alpha}\Big]\ud v.
\end{aligned}
\]
Their total is \(\E X_1^2+2\E X_2\). For order four, define
\[
H_m=\Big\{h\in(0,\infty)^4:\sum_{l\le m}h_l<1,\ \sum_{l=m+1}^4h_l<1\Big\},
\qquad b(l)=\text{first index of the nonempty chain of }l,
\]
\[
S_l(h)=\sum_{i=b(l)}^l h_i,\qquad
Y_l(h,U)=\sum_{i=b(l)}^l h_iU_i,\quad U_1,\dots,U_4\ \text{iid uniform on }[-1,1].
\]
For \(D\in\{A,B,C\}\),
\[
J_{m,n,D}(t)
=
c_\alpha^2t^{2\beta}
\int_{H_m}\Big(\prod_{l=1}^4h_l\Big)
\prod_{(j,q)\in D}|S_j(h)-S_q(h)|^{-\alpha_0}
\E_U\Big[\prod_{(j,q)\in D}|Y_j(h,U)-Y_q(h,U)|^{-\alpha}\Big]\ud h.
\]
This is finite and nonnegative and specifies all five splits and all three pairings.

**Derivation.** The order-two cross integral uses
\[
\int_{\R^2}G(s,y)G(r,z)c_\alpha|y-z|^{-\alpha}\ud y\ud z
=\frac{c_\alpha\big((s+r)^{2-\alpha}-|s-r|^{2-\alpha}\big)}{2(1-\alpha)(2-\alpha)}.
\]
Integrating \(s>r\), \(v=s-r\), \(r\in(0,t-v)\) gives the second formula; the single-chain term uses the spatial integral \(c_\alpha rv^{1-\alpha}/(1-\alpha)\) and then \(\int_{r+v<t}rv^{1-\alpha-\alpha_0}\ud r\ud v\). For order four, each spatial increment is \(h_lU_l\); the triangular chain map has determinant one, and the factors \(1/16\) are already in the four uniform laws. Scaling gives \(t^8\) time/space vs \(t^{-2\alpha-2\alpha_0}\) covariance, i.e. \(t^{2\beta}\). Finiteness is by Tonelli on the bounded domains, since \(\alpha_0,\alpha<1\).

**Consumed hypotheses/conditions.** Only \(d=1\), Riesz covariance, \(0<\alpha,\alpha_0<1\). No closed form for \(M_4(1)\) is asserted; finite-order coefficients cannot determine all-order constants.

---

## PROOF014

**Statement (L:d1-spatial).** Under
\[
\gamma(y)=c_\alpha|y|^{-\alpha}\ (0<\alpha<1)\quad\text{or}\quad \gamma=c_\delta\delta_0\ (\alpha=1),
\]
\(k\ge1\), and every pairing \(D\) of the two chains, orient each pair \((i,j)\) with \(i<j\), and let \(O_D,C_D\) be the opening/closing label sets. Then, uniformly in all edge widths \(\boldsymbol\epsilon\), with
\[
S_{D,\boldsymbol\epsilon}(h)=\int_{\R^{2k}}\prod_{l=1}^{2k}G(h_l,y_l)
\prod_{(i,j)\in D}\gamma_{\epsilon_{i,j}}(x_j-x_i)\ud y,
\qquad G(h,y)=\frac12\mathbf1_{\{|y|<h\}},
\]
one has
\[
S_{D,\boldsymbol\epsilon}(h)\le
\begin{cases}
\Big(\dfrac{c_\alpha}{1-\alpha}\Big)^k\prod_{i\in O_D}h_i\prod_{j\in C_D}h_j^{1-\alpha},
&0<\alpha<1,\\[1ex]
\Big(\dfrac{c_\delta}{2}\Big)^k\prod_{i\in O_D}h_i,
&\alpha=1.
\end{cases}
\]
If \(\sum_{l=1}^{2k}h_l\le2t\), then
\[
S_{D,\boldsymbol\epsilon}(h)\le K_{\rm sp}^{\,k}\frac{t^{bk}}{k^{bk}},
\qquad b=2-\alpha,
\]
with
\[
K_{\rm sp}=
\begin{cases}
\dfrac{c_\alpha 2^{2-\alpha}(1-\alpha)^{-\alpha}}{(2-\alpha)^{2-\alpha}},&0<\alpha<1,\\[1ex]
c_\delta,&\alpha=1.
\end{cases}
\]

**Derivation.** The convolution bounds are
\[
\sup_z\int_\R G(h,y)c_\alpha|y+z|^{-\alpha}\ud y
=\frac{c_\alpha h^{1-\alpha}}{1-\alpha},
\qquad
\sup_z\int_\R G(h,y)\gamma_\epsilon(y+z)\ud y\le\frac{c_\delta}{2},
\]
the latter by the mass-one Gaussian average of the supremum. Descending integration in the order \(2k,2k-1,\dots,1\) maintains the invariant: at a closing label exactly its own pair still involves that increment, and the convolution bound removes it; at an opening label its pair is already removed, leaving mass \(h_l\). Thus exactly \(k\) openings and \(k\) closings. Weighted arithmetic–geometric mean with weights \(1\) and \(1-\alpha\), total \(bk\), gives the spatial maximum.

**Consumed hypotheses/conditions.** Only the two one-dimensional covariances and their smoothing (via \(\gamma_\epsilon=p_\epsilon*\gamma\); no pointwise delta). This is a spatial estimate; it does not by itself bound temporal pairing sums.

---

## PROOF015

**Statement (P:d1-upper).** Under the same one-dimensional covariances, for \(k\ge1\) and \(t>0\),
\[
A_k(t)\le\frac{(2ZK_{\rm sp})^k t^{\beta k}}{k!\,k^{bk}}
\le\frac{(2ZK_{\rm sp})^k t^{\beta k}}{(k!)^q},
\qquad
\E u^2(t,x)\le\exp(C_2t^\kappa),
\]
where \(Z=\frac{2}{(1-\alpha_0)(2-\alpha_0)}\), \(\beta=4-\alpha-\alpha_0\), \(q=3-\alpha\), \(b=2-\alpha\),
\[
C_2=q(2ZK_{\rm sp})^{1/q},\qquad \kappa=\frac{\beta}{q}.
\]

**Derivation.** On the regularized terms, Wick's formula expresses each mixed expectation of total order \(2k\) as a sum over \(D\in\Pi_k\). After chain reversal the spatial factor is bounded by the pair/pairing-independent spatial maximum \(K_{\rm sp}^kt^{bk}/k^{bk}\), because the increments sum to at most \(2t\). The remaining temporal factor is the fully symmetric pairing sum
\[
F_k(s_1,\dots,s_{2k})=\sum_{D\in\Pi_k}\prod_{(i,j)\in D}|s_i-s_j|^{-\alpha_0},
\]
whose full cube integral is \(P_k(Zt^{2-\alpha_0})^k\) by the disjoint-pair computation. Partioning the cube into the two within-block order sets gives
\[
\int_{[0,t]^m_<\times[0,t]^{2k-m}_<}F_k\ud s
=\frac{P_k(Zt^{2-\alpha_0})^k}{m!(2k-m)!}.
\]
With \(P_k=(2k)!/(2^kk!)\) and \(\sum_m\frac{1}{m!(2k-m)!}=\frac{2^{2k}}{(2k)!}\), summation over \(m\) gives the coefficient. The scalar inequality \(\sum_{k\ge0}\frac{z^k}{(k!)^q}\le e^{qz^{1/q}}\) with \(z=2ZK_{\rm sp}t^\beta\) gives the exponential.

**Consumed hypotheses/conditions.** The \(L^2\) limit to the canonical terms is supplied by `L:joint-fixed-order` (`PROOF006`); the bound is uniform for the passage. The crucial point is that the temporal symmetry is applied only to the summed pairing factor after the common spatial bound, not to an individual diagram. No stronger per-diagram factorial bound is asserted.

---

## PROOF016

**Statement (L:low-alpha-convolution).** Under `Hypothesis H:homog`, \(d\in\{1,2,3\}\), \(0<\alpha<1\), and \(V=\mu(\{\xi:|\xi|\le1\})\), for every \(R,h>0\),
\[
\mu(\{\xi:|\xi|\le R\})=VR^\alpha,\qquad
\int_{\R^d}\min\{h,|\xi|^{-1}\}\mu(\ud\xi)=\frac{V}{1-\alpha}h^{1-\alpha}.
\]
For \(\epsilon>0\), \(\eta\ge0\), and \(z\in\R^d\),
\[
0\le\int_{\R^d}G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
\le\frac{V}{1-\alpha}h^{1-\alpha}.
\]
The estimate is uniform in both smoothing parameters and in \(z\).

**Derivation.** \(\mu(cA)=c^\alpha\mu(A)\) by Fourier uniqueness and covariance homogeneity; the layer-cake identity gives the \(\min\{h,|\xi|^{-1}\}\) integral from the ball masses. The wave Fourier multiplier is \(|\widehat G_h(\xi)|\le\min\{h,|\xi|^{-1}\}\), and the Gaussian multipliers are bounded by \(1\), so
\[
\Big|\int G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)\Big|
\le\int_{\R^d}\frac{|\sin(h|\xi|)|}{|\xi|}\mu(\ud\xi)
\le\int_{\R^d}\min\{h,|\xi|^{-1}\}\mu(\ud\xi).
\]
Nonnegativity uses \(\gamma_\epsilon\ge0\) and \(G_{h,\eta}\ge0\). No radial density is assumed.

**Consumed hypotheses/conditions.** Only `H:homog`, \(0<\alpha<1\), and the positive Radon spectral measure \(\mu\). The positivity of the oscillatory integrand inside the Fourier expression is not asserted; the bound is via \(|\sin|\le1\).

---

## PROOF017

**Statement (L:alpha-one-convolution).** Under degree-one homogeneous covariance, for every \(h>0\), \(\epsilon>0\), \(\eta\ge0\), and \(z\in\R^d\),
\[
0\le\int_{\R^d}G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
\le\frac{\pi V}{2}.
\]
No isotropy or angular density is required.

**Derivation.** Homogeneity gives \(\mu(cA)=c\mu(A)\) and \(\mu(\{0\})=0\); polar uniqueness gives \(\mu(\ud\xi)=\ud r\,\sigma(\ud\theta)\), \(r>0\), \(\sigma\) even with total mass \(V\). Gaussian weighting gives a finite measure, so Fourier Fubini yields
\[
\int G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
=\int_{\mathbb S^{d-1}}I_a(h,\theta\cdot z)\sigma(\ud\theta),
\qquad
I_a(h,v)=\int_0^\infty e^{-ar^2}\frac{\sin(hr)}r\cos(rv)\ud r.
\]
The one-dimensional inversion factor connects this to \(g_h*p_{2a}^{(1)}\) with \(g_h(v)=\frac12\mathbf1_{\{|v|<h\}}\), giving \(0\le I_a(h,v)\le\pi/2\); integrating against \(\sigma\) gives \(\pi V/2\). This retains the oscillation and does not use the divergent absolute Fourier envelope.

**Consumed hypotheses/conditions.** Degree-one homogeneity and the spectral measure; the estimate is the \(\alpha=1\) endpoint of PROOF016 and is not obtained by taking the \(\alpha<1\) constant limit.

---

## PROOF018

**Statement (P:low-alpha-upper).** Under `H:homog`, standing covariance positivity, \(d\in\{1,2,3\}\), \(0<\alpha\le1\), and \(V>0\),
\[
K_{\rm sp}^{\rm gen}=
\begin{cases}
\dfrac{V2^{2-\alpha}(1-\alpha)^{-\alpha}}{(2-\alpha)^{2-\alpha}},&0<\alpha<1,\\[1ex]
\pi V,&\alpha=1,
\end{cases}
\qquad
C_2^{\rm gen}=q(2ZK_{\rm sp}^{\rm gen})^{1/q}.
\]
With the same \(A_k,b,q,\beta,Z\),
\[
A_k(t)\le\frac{(2ZK_{\rm sp}^{\rm gen})^k t^{\beta k}}{k!\,k^{bk}}
\le\frac{(2ZK_{\rm sp}^{\rm gen})^k t^{\beta k}}{(k!)^q},\qquad
\E u^2(t,x)\le\exp(C_2^{\rm gen}t^\kappa).
\]

**Derivation.** Same descending-label argument as PROOF014, using PROOF016 (closing bound \(Mh_l^{1-\alpha}\), \(M=V/(1-\alpha)\)) or PROOF017 (closing bound \(M=\pi V/2\)); openings give mass \(h_l\). Weighted arithmetic–geometric mean, with \(\alpha=1\) the ordinary mean, gives \((K_{\rm sp}^{\rm gen})^k t^{bk}/k^{bk}\). The temporal symmetry and split count are dimension-free and identical to PROOF015. In \(d=3\) the Green width \(\eta\) is removed first at fixed noise smoothing with weak Green convergence, then the noise-width limit via `L:joint-fixed-order`.

**Consumed hypotheses/conditions.** `H:homog` and positivity for \(0<\alpha\le1\). The limit identifications use `PROOF006`; the constants are not asserted sharp. This covers degree-one covariance in dimensions two and three, not spatial white noise there.

---

## PROOF019

**Statement (C:d1-first-calibration).** Let \(K_*\) be \(K_{\rm sp}\) (d1 covariances) or \(K_{\rm sp}^{\rm gen}\) (PROOF018). Put \(C_{2,*}=q(2ZK_*)^{1/q}\). Then
\[
\E u(t,x)\le\exp(C_{1,*}t^\kappa),\qquad
C_{1,*}=q\Big(\frac{ZK_*}{2^{3-\alpha}}\Big)^{1/q}
=\frac{C_{2,*}}{2^{(4-\alpha)/(3-\alpha)}}.
\]
In either nonzero case \(2C_{1,*}<C_{2,*}\). Conditionally on a first-moment lower rate at least \(L_*\),
\[
2L_*\le2C_{1,*}<C_{2,*}.
\]

**Derivation.** For one chain of length \(2k\), the increments sum to at most \(t\); the spatial estimate with \(t/2\) in place of \(t\) applies, and the temporal pairing sum on one ordered simplex is \(P_k(Zt^{2-\alpha_0})^k/(2k)!\), giving
\[
\E X_{2k}(t,x)\le\frac{(ZK_*/2^{b+1})^kt^{\beta k}}{k!\,k^{bk}}
\le\frac{(ZK_*/2^{3-\alpha})^kt^{\beta k}}{(k!)^q}.
\]
Odd expectations vanish; the scalar series sum gives \(C_{1,*}\). Since \((4-\alpha)/(3-\alpha)>1\), \(2C_{1,*}<C_{2,*}\).

**Consumed hypotheses/conditions.** The statement \(\E u\le\exp(C_{1,*}t^\kappa)\) is unconditional under the corresponding upper-bound hypotheses. The \(2L_*\le2C_{1,*}\) comparison is conditional on the intended first-moment lower bound with constant \(L_*\); no printed normalization is adopted or sharp constant identified.

---

## PROOF020

**Statement (P:higher-transfer).** Under `H:homog` and the additional `H:spatial-maximum`
\[
0\le\int_{\R^d}G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)\le Mh^{-\delta},
\qquad \delta=\alpha-1,\quad d\in\{2,3\},\quad 1<\alpha<2-\alpha_0,
\]
choose
\[
\frac1{1-\alpha_0}<r<\frac1\delta,\qquad
r'=\frac r{r-1},\qquad \theta=\alpha_0r',\qquad a=1-\frac{\delta r}{2}.
\]
Define
\[
Z_\theta=\frac2{(1-\theta)(2-\theta)},\qquad
D_a=e^2(e/a)^{2a},\qquad
K=12M[\Gamma(1-\delta r)D_a]^{1/r}Z_\theta^{1/r'}.
\]
Then, with \(\beta=4-\alpha-\alpha_0\), \(q=3-\alpha\),
\[
A_k(t)\le\frac{K^kt^{\beta k}}{(k!)^q}\ (k\ge1),\qquad
\E u^2(t,x)\le\exp\{qK^{1/q}t^\kappa\}.
\]

**Derivation.** Descending increment integration gives \(S_D(h)\le M^k(2t/k)^k\prod_{j\in C_D}h_j^{-\delta}\). Hölder on the counting/lebesgue product splits each diagram integral into \(H_D^r\) and \(T_D^{r'}\) parts. The Dirichlet integral gives
\[
\int_{\Omega_{m,n}}H_D^r\ud s
=\frac{\Gamma(1-\delta r)^k t^{(2-\delta r)k}}
{\Gamma(1+m-\delta rk_1)\Gamma(1+n-\delta rk_2)}
\le\frac{P_k[\Gamma(1-\delta r)D_a]^kt^{(2-\delta r)k}}{(k!)^{2-\delta r}},
\]
using \(\Gamma(1+ak)\ge e^{-1}(a/e)^{ak}k^{ak}\ge e^{-1}(a/e)^{ak}(k!)^a\). The paired temporal sum is symmetric on the full cube:
\[
\sum_D\int_{\Omega_{m,n}}T_D^{r'}\ud s
=\frac{P_k(Z_\theta t^{2-\theta})^k}{m!n!}\le\frac{P_k(Z_\theta t^{2-\theta})^k}{(k!)^2}.
\]
\(P_k=\prod_{j=1}^k(2j-1)\le2^kk!\); the \(2k+1\le3^k\) splits give the \(12\) factor. The time power is \(1+(2-\delta r)/r+(2-\theta)/r'=3-\delta-\alpha_0=\beta\); the factorial power is \(2-\delta=q\). Passing Green then noise limits via `PROOF006` preserves the bound.

**Consumed hypotheses/conditions.** This proposition is conditional on `H:spatial-maximum`, which is an additional assumption beyond homogeneity. It gives only nonsharp constants and does not cover arbitrary homogeneous covariances; the parameter interval for \(r\) is nonempty because \(\delta+\alpha_0<1\).

---

## PROOF021

**Statement (L:higher-riesz).** For \(\gamma(x)=c|x|^{-\alpha}\), \(c>0\):
- \(d=3\), \(1<\alpha<2\): `H:spatial-maximum` holds with the optimal uniform constant
\[
M_3=\frac{c2^{1-\alpha}}{2-\alpha}.
\]
- \(d=2\), \(1<\alpha<3/2\): it holds with
\[
M_2=c\Big\{4^\alpha+\frac{2\alpha}{3/2-\alpha}4^{\alpha-3/2}\Big\}.
\]

**Derivation.** Write the unsmoothed convolution as \(ch^{1-\alpha}F_d(z/h)\), \(F_d(w)=\int G_1^{(d)}(\ud y)|y+w|^{-\alpha}\). In dimension three the spherical computation gives \(F_3(w)=\big((1+\rho)^{2-\alpha}-|1-\rho|^{2-\alpha}\big)/(2(2-\alpha)\rho)\), maximized at \(F_3(e_1)=2^{1-\alpha}/(2-\alpha)\). In dimension two, the disk measure bound \(G_1(B(w,R))\le2R^{3/2}\) for \(0<R\le1/4\) and layer-cake give the displayed \(M_2\). Gaussian convolution by \(p_{\epsilon+\eta}\) is a mass-one average, preserving both bounds and yielding optimality via Fatou.

**Consumed hypotheses/conditions.** The discharge is only for the stated Riesz ranges. It does not extend to \(\alpha\ge3/2\) in dimension two and does not touch anisotropies.

---

## PROOF022

**Statement (C:higher-riesz).** For isotropic Riesz covariance \(c|x|^{-\alpha}\), the bounds of PROOF020 hold:
- \(d=3\) for \(1<\alpha<2-\alpha_0\);
- \(d=2\) for \(1<\alpha<\min\{3/2,2-\alpha_0\}\),
with \(M=M_d\) from PROOF021.

**Derivation.** The Riesz covariance is nonnegative, homogeneous of degree \(-\alpha\), locally integrable, and nonnegative definite via the Gaussian-mixture representation
\[
|x|^{-\alpha}=\frac1{\Gamma(\alpha/2)}\int_0^\infty s^{\alpha/2-1}e^{-s|x|^2}\ud s,
\]
verified distributionally against autocorrelation functions. It therefore satisfies `H:homog`; PROOF021 supplies the additional `H:spatial-maximum`, and PROOF020 applies.

**Consumed hypotheses/conditions.** Only the isotropic stated ranges. The two-dimensional interval \(3/2\le\alpha<2-\alpha_0\) is not obtained by this route.

---

## PROOF023

**Statement (P:higher-obstructions).** In dimension two, Riesz covariance with \(3/2\le\alpha<2\) fails `H:spatial-maximum`. For every \(1<\alpha<2\) there exist nonnegative, nonnegative definite, homogeneous, locally integrable covariance functions in dimensions two and three that fail `H:spatial-maximum`.

**Derivation.** For the planar Riesz at \(h=1\), \(z=-e_1\), on the wedge \(0<\rho<1/2\), \(2\pi/3\le\phi\le4\pi/3\), one has \(0<1-|y|^2\le2\rho\), hence
\[
\int G_1^{(2)}(\ud y)c|y-e_1|^{-\alpha}
\ge\frac{c}{3\sqrt2}\int_0^{1/2}\rho^{1/2-\alpha}\ud\rho=\infty
\qquad(3/2\le\alpha<2),
\]
including logarithmic divergence at \(\alpha=3/2\). For the product obstruction choose \(a_1=(1+\max\{2-\alpha,\alpha-1\})/2\), \(a_2=\alpha-a_1\), satisfying \(0<a_1,a_2<1\) and \(a_1+a_2/2>1\), and set \(\gamma(x)=c|x_1|^{-a_1}|x_2|^{-a_2}\). Gaussian-mixture factorization shows nonnegative definiteness and \(p_\epsilon\)-factorized convergence; the planar disk computation
\[
\int G_1^{(2)}(\ud y)\gamma(y-e_1)
=\frac{cB((1-a_2)/2,1/2)}{2\pi}
\int_0^2u^{-a_1}(2u-u^2)^{-a_2/2}\ud u=\infty,
\]
with the same divergence in dimension three via the projection of \(G_1^{(3)}\), shows failure.

**Consumed hypotheses/conditions.** These are no-go results for the spatial supremum only, not for existence, moment finiteness, or the target time scale. They constrain this method, not the independent full upper theorem.

---

## PROOF024

**Statement (L:static-holder-input).** Let \(U_n\) be the ordered Stratonovich integrals for static Gaussian noise with covariance \(\gamma_\chi\), \(d\in\{2,3\}\), \(1<\chi<2\), \(U_0=1\), and
\[
B_k(t)=\sum_{m=0}^{2k}\E[U_m(t,x)U_{2k-m}(t,x)].
\]
Then \(B_0=1\) and there is a finite \(C_{\rm st}=C_{\rm st}(\chi,c,d)>0\) such that
\[
0\le B_k(t)\le\frac{C_{\rm st}^{\,k}t^{(4-\chi)k}}{(k!)^{3-\chi}},\qquad k\ge1,\ t>0.
\]

**Consumed hypotheses.** This is an imported source input: the static solution for data \((1,0)\), Dalang condition \(\chi<\min\{2,d\}\), generalized covariance allowed. The fixed-order \(L^2\) existence is Chen–Hu `Theorem 3.8(i), p. 2165`; the product/Wick identification of \(B_k\) uses the published `(2.17)` and `(2.19)` (pp. 2151–2152), including self-pairs and empty chains. The homogeneity \(B_k(t)=t^{(4-\chi)k}B_k(1)\) is the published `(5.1) p. 2173`; the finite coefficient upper rate is
\[
\limsup_{k\to\infty}\frac1k\log\big((k!)^{3-\chi}B_k(1)\big)<\infty
\]
from the published `(5.15) p. 2180`. The derivation enlarges a rate bound to a uniform \(C_{\rm st}\) by keeping the finitely many low orders.

**Conditions.** The coefficient rate is imported, not proved here; \(C_{\rm st}\) is not given numerically and is not asserted sharp. Chen’s 2023 variational theorem is not invoked for a coefficient rate.

---

## PROOF025

**Statement (P:static-holder-upper).** Under \(d\in\{2,3\}\), \(c>0\), \(0<\alpha_0<1\), \(1<\alpha<2-\alpha_0\), and spatial covariance \(\gamma_\alpha=c|x|^{-\alpha}\): choose
\[
\alpha_0<\vartheta<2-\alpha,\qquad
b_0=\frac{\alpha_0}{\vartheta},\qquad
\chi=\frac{\alpha-\vartheta}{1-\vartheta}.
\]
Let \(V_1\) be the spectral mass of the unit ball for \(\gamma_1\), and set
\[
Z_{b_0}=\frac2{(1-b_0)(2-b_0)},\qquad
C_{\rm low}=2Z_{b_0}\pi V_1,\qquad
C=C_{\rm low}^{\,\vartheta}C_{\rm st}^{\,1-\vartheta},
\qquad q=3-\alpha.
\]
Then
\[
A_k(t)\le\frac{C^kt^{(4-\alpha-\alpha_0)k}}{(k!)^{3-\alpha}},\qquad
\E u^2\le\exp(qC^{1/q}t^\kappa).
\]

**Derivation.** With a common measure \(\nu_{k,t,\eta}\) over all splits/pairings, Hölder on the Gaussian probability measure gives
\[
\gamma_{\alpha,2\epsilon}(z)\le\gamma_{1,2\epsilon}(z)^\vartheta\gamma_{\chi,2\epsilon}(z)^{1-\vartheta},
\]
since \(c=c^\vartheta c^{1-\vartheta}\). The temporal domination is \(Q_\delta\le T_{\alpha_0}=T_{b_0}^{\,\vartheta}\). Define
\[
L_k^{\epsilon,\eta}=\int T_{b_0}H_1\ud\nu,\qquad
B_k^{\epsilon,\eta}=\int H_\chi\ud\nu,
\]
the latter the actual regularized static coefficient. Then
\[
A_k^{\epsilon,\delta,\eta}\le(L_k^{\epsilon,\eta})^\vartheta(B_k^{\epsilon,\eta})^{1-\vartheta}.
\]
The raw low temporal integral is bounded by
\[
L_k^{\epsilon,\eta}\le\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{k!k^k}
\le\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{(k!)^2}
\]
using the degree-one closing bound \(\pi V_1/2\) and opening arithmetic mean. Take Green/noise limits first, then apply the static input `PROOF024`; the parameter identities \(\alpha=\vartheta+(1-\vartheta)\chi\), \(\alpha_0=\vartheta b_0\) give the powers \(3-\alpha\) and \(4-\alpha-\alpha_0\).

**Consumed hypotheses/conditions.** Isotropic Riesz only; the static coefficient input comes from the published Chen–Hu theorem. No monotonicity in the spatial width or uniform smoothed static asymptotic is used. Constants depend on \(\alpha,\alpha_0,c,d,\vartheta\), not on \(k,t,x\); no sharp constant.

---

## PROOF026

**Statement (L:planar-endpoints).** Let \(d=2\), \(\Gamma\) a nonnegative, even, positive-definite tempered Radon measure with homogeneity exponent \(1<\alpha<2\). For \(\alpha<\chi<2\) define
\[
\sigma(E)=(2-\alpha)\Gamma\big\{x:0<|x|\le1,\ x/|x|\in E\big\},\qquad S=\sigma(\mathbb S^1),
\]
and
\[
\Gamma_{\rm low}(\ud x)=|x|^{\alpha-1}\Gamma(\ud x),\qquad
\Gamma_{\rm st}(\ud x)=|x|^{\alpha-\chi}\Gamma(\ud x),
\]
zero mass at the origin. Both are nonnegative, even, positive-definite tempered Radon measures with scaling exponents \(1\) and \(2-\chi\), respectively. For every \(h>0\), \(\epsilon>0\), \(\eta\ge0\), \(z\in\R^2\),
\[
\int G_{h,\eta}(\ud y)(p_\epsilon*\Gamma_{\rm low})(y+z)\le\frac S4.
\]
For \(\vartheta=(\chi-\alpha)/(\chi-1)\), \(0<\vartheta<1\), and
\[
(p_\epsilon*\Gamma)(z)
\le(p_\epsilon*\Gamma_{\rm low})(z)^\vartheta(p_\epsilon*\Gamma_{\rm st})(z)^{1-\vartheta}.
\]

**Derivation.** Scaling and local finiteness force \(\Gamma(\{0\})=0\); polar uniqueness gives
\[
\int f(x)\Gamma(\ud x)=\int_{\mathbb S^1}\int_0^\infty f(r\omega)r^{1-\alpha}\ud r\,\sigma(\ud\omega).
\]
The low endpoint has the full-sphere line representation
\[
\int f(x)\Gamma_{\rm low}(\ud x)=\frac12\int_{\mathbb S^1}\int_\R f(r\omega)\ud r\,\sigma(\ud\omega),
\]
with factor \(1/2\) essential because both orientations occur. Positive definiteness of the low endpoint uses the line Fubini identity
\[
\int_\R\psi(r\omega)\ud r=\int_{\omega^\perp}\Big|\int_\R\varphi(s\omega+v)\ud s\Big|^2\ud v\ge0.
\]
The static endpoint uses \(|x|^{-\lambda}\), \(\lambda=\chi-\alpha>0\), as a Gaussian mixture multiplied against the positive-definite \(e^{-s|x|^2}\Gamma(\ud x)\). The convolution bound uses the planar Green line integral
\[
\int_\R G_h(z-r\omega)\ud r=
\begin{cases}1/2,&|z\cdot\omega^\perp|<h,\\0,&\ge h,\end{cases}
\]
so \((G_h*\Gamma_{\rm low})(z)=\frac14\int_{\mathbb S^1}\mathbf1_{\{|z\cdot\omega^\perp|<h\}}\sigma(\ud\omega)\le S/4\). Hölder on the finite measure \(p_\epsilon(z-x)\Gamma(\ud x)\), with \(\vartheta(\alpha-1)+(1-\vartheta)(\alpha-\chi)=0\), gives the comparison.

**Consumed hypotheses/conditions.** \(d=2\), \(1<\alpha<2\), \(\Gamma\ne0\). No angular density or isotropy; the constant \(S/4\) uses the physical angular mass.

---

## PROOF027

**Statement (L:planar-static-input).** Let \(\Xi\) be a nonnegative, even, positive-definite tempered Radon measure on \(\R^2\) with \(\Xi(rA)=r^{2-\chi}\Xi(A)\), \(1<\chi<2\). For the static Stratonovich integrals \(U_n\), \(U_0=1\), there is a finite \(C_{\rm st}=C_{\rm st}(\Xi)>0\) with
\[
0\le B_k(t):=\sum_{m=0}^{2k}\E[U_m(t,x)U_{2k-m}(t,x)]
\le\frac{C_{\rm st}^{\,k}t^{(4-\chi)k}}{(k!)^{3-\chi}}.
\]
Also \(B_0=1\).

**Derivation.** If \(\Xi=0\), \(B_k=0\) for \(k\ge1\) and \(C_{\rm st}=1\) works. For \(\Xi\ne0\), spectral homogeneity gives \(\mu_\Xi(rA)=r^\chi\mu_\Xi(A)\) and the dyadic bound
\[
\int_{\R^2}(1+|\xi|^2)^{-1}\mu_\Xi(\ud\xi)
\le\mu_\Xi(B_1)+2^\chi\mu_\Xi(B_1)\sum_{j\ge0}2^{j(\chi-2)}<\infty,
\]
verifying Dalang without an angular density. The published generalized-covariance convention covers this \(\Xi\). Chen–Hu `Theorem 3.8(i) p. 2165` gives fixed-order \(L^2\) existence; `(2.17)/(2.19)` identify \(B_k\) with all pairings/splits; `(5.1) p. 2173` gives homogeneity; `(5.15) p. 2180` gives the finite coefficient upper rate, with the finiteness of the variational \(\mathcal M\) supplied by Chen’s 2023 `Theorem 1.1` (finiteness only), identified on p. 2175 as \(2^{\chi/(4-\chi)}\mathcal M\). The rate is then converted to \(C_{\rm st}\) by enlarging over finitely many low orders.

**Consumed hypotheses/conditions.** Source result imported under its exact hypotheses. No angular density; finiteness of the variational constant imported, not a coefficient-rate theorem from Chen 2023.

---

## PROOF028

**Statement (P:planar-upper).** Let \(d=2\), \(0<\alpha_0<1\), \(1<\alpha<2-\alpha_0\), and \(\Gamma\ne0\) homogeneous of exponent \(\alpha\). Choose
\[
\alpha_0<\vartheta<2-\alpha,\qquad
b_0=\alpha_0/\vartheta,\qquad
\chi=(\alpha-\vartheta)/(1-\vartheta).
\]
With \(S\) from PROOF026,
\[
Z_{b_0}=\frac2{(1-b_0)(2-b_0)},\qquad
C_{\rm low}=Z_{b_0}S,\qquad
C=C_{\rm low}^{\,\vartheta}C_{\rm st}^{\,1-\vartheta},
\qquad q=3-\alpha,
\]
one has
\[
A_k(t)\le\frac{C^kt^{(4-\alpha-\alpha_0)k}}{(k!)^{3-\alpha}},\qquad
\E u^2\le\exp(qC^{1/q}t^\kappa).
\]

**Derivation.** Same common-measure/Hölder machinery as PROOF025 on a finite measure \(\nu_{k,t}\) over the planar Green kernels \(G_{h_l}(\ud y_l)\), with no Green smoothing needed in \(d=2\). Define
\[
L_k^\epsilon=\int T_{b_0}H_{\Gamma_{\rm low}}\ud\nu,\qquad
B_k^\epsilon=\int H_{\Gamma_{\rm st}}\ud\nu,
\]
so
\[
A_k^{\epsilon,\delta}\le(L_k^\epsilon)^\vartheta(B_k^\epsilon)^{1-\vartheta}
\]
with \(Q_\delta\le T_{b_0}^{\,\vartheta}\). Descending integration and the \(S/4\) closing bound give the common spatial bound \((S/2)^kt^k/k^k\); the summed temporal pairing count exactly gives
\[
\sum_{m=0}^{2k}\sum_{D\in\Pi_k}\int_{[0,t]^m_<\times[0,t]^{2k-m}_<}T_{b_0}\ud s
=\frac{2^k}{k!}(Z_{b_0}t^{2-b_0})^k,
\]
hence
\[
L_k^\epsilon\le\frac{(Z_{b_0}S)^kt^{(3-b_0)k}}{k!k^k}
\le\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{(k!)^2}.
\]
Take fixed-order noise limits for both target and static, then apply PROOF027. The identities
\[
\alpha=\vartheta+(1-\vartheta)\chi,\quad \alpha_0=\vartheta b_0
\]
give \(2\vartheta+(1-\vartheta)(3-\chi)=3-\alpha\) and \(\vartheta(3-b_0)+(1-\vartheta)(4-\chi)=4-\alpha-\alpha_0\). The scalar series gives the exponential.

**Consumed hypotheses/conditions.** \(d=2\) general homogeneous nonzero covariance only; the static coefficient is imported for \(\Xi=\Gamma_{\rm st}\). Target fixed-order limits are `PROOF006`; static limits imported. No sharp constant; constants may depend on \(\Gamma,\alpha_0,\vartheta\) but not \(k,t,x\).

---

## PROOF029

**Statement (C:planar-range).** In dimension two, under `H:homog` and standing covariance positivity, the upper bound \(\E u^2(t,x)\le\exp(C_2t^\kappa)\) holds throughout \(0<\alpha<2-\alpha_0\), with a finite \(C_2\) depending on \(\alpha_0\) and the spatial covariance.

**Derivation.** For \(0<\alpha\le1\) apply PROOF018 (`P:low-alpha-upper`); for \(1<\alpha<2-\alpha_0\) apply PROOF028 (`P:planar-upper`). If the covariance vanishes, \(u=1\) and \(C_2=0\). A nonnegative generalized covariance is interpreted as the homogeneous measure with its Gaussian approximations.

**Consumed hypotheses/conditions.** The two pieces require their respective hypotheses: PROOF018 needs \(0<\alpha\le1\); PROOF028 needs \(1<\alpha<2-\alpha_0\) and a nonzero homogeneous measure. This is a planar result only; no dimension-three higher-exponent claim follows.

---

## PROOF030

**Statement (L:product-endpoints).** Let \(0\le a_j<1\), \(\alpha=\sum_{j=1}^3a_j\in(1,2)\), choose \(0<\vartheta<2-\alpha\), and set \(\chi=(\alpha-\vartheta)/(1-\vartheta)\). Define
\[
L_j=\max\{0,(a_j-1+\vartheta)/\vartheta\},\quad
U_j=\min\{1,a_j/\vartheta\},\quad
\Lambda=\frac{1-\sum_jL_j}{\sum_jU_j-\sum_jL_j},
\]
\[
b_j=L_j+\Lambda(U_j-L_j),\qquad
v_j=\frac{a_j-\vartheta b_j}{1-\vartheta}.
\]
Then \(0<\Lambda<1\), \(\sum_jb_j=1\), \(\sum_jv_j=\chi\), \(a_j=\vartheta b_j+(1-\vartheta)v_j\); \(a_j>0\Rightarrow0<b_j,v_j<1\); \(a_j=0\Rightarrow b_j=v_j=0\). The covariance densities
\[
\gamma_e(x)=c\prod_{j=1}^3|x_j|^{-e_j},\qquad e\in\{a,b,v\},
\]
are nonnegative, even, positive definite, locally integrable and tempered with homogeneity exponents \(\alpha,1,\chi\), and \(\alpha<\chi<2\). For every \(\epsilon>0\), \(z\in\R^3\),
\[
(p_\epsilon*\gamma_a)(z)\le(p_\epsilon*\gamma_b)(z)^\vartheta(p_\epsilon*\gamma_v)(z)^{1-\vartheta}.
\]

**Derivation.** There are at least two positive coordinates because \(a_j<1\) and \(\sum a_j>1\). Feasibility of the interval follows from \(\sum_jL_j<1<\sum_jU_j\), so \(0<\Lambda<1\), and strictness of \(L_j<U_j\) at positive coordinates gives \(0<b_j,v_j<1\). Local integrability is the product of one-dimensional exponents below one; the Gaussian-mixture representation per active coordinate proves nonnegative definiteness; zero coordinates are the defined constant factor one. The endpoint convolution finiteness follows from Gaussian decay. Hölder on the Gaussian probability measure, using \(\gamma_a=\gamma_b^\vartheta\gamma_v^{1-\vartheta}\) a.e., gives the comparison.

**Consumed hypotheses/conditions.** Only the strict product family with \(0\le a_j<1\), \(\alpha\in(1,2)\). Zero exponents denote constant factors, not one-dimensional white noise. This is a deterministic covariance comparison.

---

## PROOF031

**Statement (L:plane-endpoints).** Fix \(d=3\), \(0<\alpha_0<1\), \(1<\alpha<2-\alpha_0\), \(\alpha_0<\vartheta<2-\alpha\), \(b_0=\alpha_0/\vartheta\), \(\chi=(\alpha-\vartheta)/(1-\vartheta)\). Let \(c>0\), \(a_1,a_2\ge0\) with \(s=a_1+a_2=\alpha-1\), coordinates \((y,z)\in\R^2\times\R\),
\[
m(\ud y,\ud z)=\ud y\,\delta_0(\ud z),\qquad
v_j=\frac{a_j}{1-\vartheta},\qquad
\Gamma_{\rm pl}=c\prod_{j=1}^2|y_j|^{-a_j}m.
\]
Then
\[
\Gamma_{\rm low}=cm,\qquad
\Gamma_{\rm st}=c\prod_{j=1}^2|y_j|^{-v_j}m
\]
satisfy `H:three-endpoints` for \(\Gamma_{\rm pl}\), and \(V_{\rm low}=c/\pi\) in the convention of `L:alpha-one-convolution`.

**Derivation.** Since \(0<s<1-\alpha_0\) and \(\vartheta<2-\alpha=1-s\), one has \(0\le a_j<1\), \(0\le v_j<1\), \(v_1+v_2=s/(1-\vartheta)<1\). A planar measure on the zero-\(z\) plane with plane density \(|y_1|^{-e_1}|y_2|^{-e_2}\) is σ-finite, tempered and has covariance scaling exponent \(2-e_1-e_2\), matching \(3-\alpha,2,3-\chi\). Positive definiteness uses the normal Dirac component and positive Gaussian mixtures in each active coordinate, verified by rapid-decay bounds on the autocorrelation \(A(u)\). Hölder on the finite measure \(p_\epsilon(w-(y,z))m(\ud y,\ud z)\) with the a.e. identity
\[
c|y|^{-a}=c^\vartheta(c|y|^{-v})^{1-\vartheta}
\]
gives the comparison. The low spectral measure is
\[
\mu_{\rm low}(\ud\xi)=\frac{c}{2\pi}\delta_0(\ud\xi_1)\delta_0(\ud\xi_2)\ud\xi_3,
\]
so its unit-ball mass is \(c/\pi\).

**Consumed hypotheses/conditions.** Plane-supported covariances only; both endpoint convolutions are finite and the zero-coordinate convention is retained.

---

## PROOF032

**Statement (L:endpoint-closure).** With the parameters \(\vartheta,b_0,\chi\) fixed, the comparison in `H:three-endpoints` is preserved by:
1. simultaneously pushing the target and both endpoint covariances forward by any invertible linear map \(T:\R^3\to\R^3\);
2. finite sums with nonnegative weights when all component comparisons use the same \(\alpha,\vartheta,\chi\).

**Derivation.** First extend from \(p_\epsilon\) to any centered nondegenerate Gaussian \(q_\Sigma\): write \(q_\Sigma=p_a*q_{\Sigma-aI}\), define \(F_J=p_a*J\) for \(J\in\{\Gamma,\Gamma_{\rm low},\Gamma_{\rm st}\}\), and apply Hölder on the Euclidean Gaussian factor, which introduces no factor beyond the three convolutions. For \(J_T=T_\#J\), \(d_T=|\det T|\), the quadratic-form compatibility
\[
(\varphi*\widetilde\varphi)(Ty)=d_T(\psi*\widetilde\psi)(y),\qquad \psi(y)=\varphi(Ty),
\]
proves positive definiteness, and
\[
(p_\epsilon*J_T)(x)=d_T^{-1}(q_\Sigma*J)(T^{-1}x)
\]
preserves the comparison, the three pushforward factors contributing total \(d_T^{-1}=d_T^{-\vartheta}d_T^{-(1-\vartheta)}\). For finite sums, discrete Hölder gives
\[
p_\epsilon*\Big(\sum_iw_i\Gamma_i\Big)
=\sum_iw_i(p_\epsilon*\Gamma_i)
\le\sum_i(w_il_i)^\vartheta(w_is_i)^{1-\vartheta}
\le\Big(p_\epsilon*\sum_iw_i\Gamma_{{\rm low},i}\Big)^\vartheta
\Big(p_\epsilon*\sum_iw_i\Gamma_{{\rm st},i}\Big)^{1-\vartheta}.
\]

**Consumed hypotheses/conditions.** Closure is deterministic on covariance measures. Nonorthogonal maps change endpoint variational quantities; no claim is made that wave constants are unchanged under such maps.

---

## PROOF033

**Statement (P:three-transfer).** Under `H:three-endpoints`, \(\Gamma\ne0\), in \(d=3\): there is a finite \(C>0\) such that for \(k\ge1\) and all \(t>0,x\),
\[
A_k(t)\le\frac{C^kt^{(4-\alpha-\alpha_0)k}}{(k!)^{3-\alpha}},\qquad
\E u^2(t,x)\le\exp(qC^{1/q}t^\kappa),\qquad q=3-\alpha.
\]
Moreover the explicit variational upper constant satisfies
\[
\limsup_{t\to\infty}t^{-\kappa}\log\E u^2(t,x)
\le q\big(C_{\rm low}^{\,\vartheta}\Lambda_{\rm st}^{\,1-\vartheta}\big)^{1/q},
\]
where \(C_{\rm low}=2Z_{b_0}\pi V_{\rm low}\),
\[
\mathcal Q_{\rm st}(g)=\int_{\R^3}\int_{\R^3}g(y+z)^2g(y)^2\ud y\,\Gamma_{\rm st}(\ud z),
\qquad
\mathcal F_3=\{g\in W^{1,2}(\R^3):\|g\|_2=1\},
\]
\[
\mathcal M_{\rm st}=\sup_{g\in\mathcal F_3}\{\mathcal Q_{\rm st}(g)^{1/2}-\|\nabla g\|_2^2\},
\qquad
Q=3-\chi,\quad \nu_{\rm st}=4-\chi,
\]
\[
\Lambda_{\rm st}=2\Big(\frac{2\sqrt{\mathcal M_{\rm st}}}{4-\chi}\Big)^{4-\chi}.
\]
`\(\Lambda_{\rm st}\)` is not asserted sharp and is not substituted into the pure all-time exponential.

**Derivation, cf. PROOF028.** Define the target static input from the endpoint covariance \(\Xi=\Gamma_{\rm st}\): spectral homogeneity gives \(\mu_\Xi(rA)=r^\chi\mu_\Xi(A)\); the dyadic sum verifies Dalang. Chen–Hu fixed-order existence `Theorem 3.8(i)` and `(2.17)/(2.19)` identify the nonnegative coefficients; the static all-time coefficient bound
\[
B_k(t)\le\frac{C_{\rm st}^{\,k}t^{(4-\chi)k}}{(k!)^{3-\chi}}
\]
is imported from the published `(5.1)/(5.15)` after converting the rate with the finitely many low orders. The target uses the fixed-order construction `PROOF006`; the low endpoint closure uses PROOF017 with \(V_{\rm low}\) and \(Z_{b_0}\). The common-measure Hölder structure is identical to PROOF025/028, with the three-dimensional Green measures and Green width \(\eta\); the target static identification at zero Green width uses the continuous pathwise integral of the static field as a Bochner integral, and for the target the actual zero Green-width approximant is given by the same Bochner structure. The essential additional content is the double passage: first Green \(\eta\downarrow0\) at fixed noise widths via weak Green convergence against bounded continuous Gaussian moments (both second and mixed \(\eta/0\) moments), then noise widths via the imported fixed-order \(L^2\) limits and the `\(L^1\)` product inequality; the target and static objects are identified with the source’s prescribed approximants, not merely shown Cauchy. The all-time coefficient \(C\) uses \(C_{\rm st}\). The asymptotic limsup is obtained separately by the exact static coefficient-rate formula at \(p=2\):
\[
\limsup_{k\to\infty}\big((k!)^Q B_k(1)\big)^{1/k}\le\Lambda_{\rm st},
\]
used only after the fixed-order noise limit, combined with the Hölder split, and with the finitely many low orders kept as a polynomial \(P_r(t)\) whose \(t^{-\kappa}\log\) vanishes; the final limsup is nonsharp and independent of the all-time constant.

**Consumed hypotheses/conditions.** Conditional on `H:three-endpoints` for general \(\Gamma\); static coefficient-rate and fixed-order limits are imported from the published source. The positive-measure energy \(\mathcal M_{\rm st}\) is justified by `PROOF036` (`L:physical-spectral-energy`), whose analytic finiteness input is Chen 2023 `Theorem 1.1` (quartic variation) only. The variational upper constant is not identified with the all-time constant, and no sharpness is claimed.

---

## PROOF034

**Statement (C:three-product-riesz).** In \(d=3\), \(0<\alpha_0<1\), \(1<\alpha<2-\alpha_0\), the coefficient, all-time moment, and nonsharp variational estimates of PROOF033 hold for:
1. \(\gamma(x)=c\prod_{j=1}^3|x_j|^{-a_j}\), \(0\le a_j<1\), \(\sum a_j=\alpha\);
2. \(\gamma(x)=c|x|^{-\alpha}\).
In the first case the constant depends only on \(a_1,a_2,a_3,c,\alpha_0\); in the second only on \(\alpha,c,\alpha_0\). A zero coordinate exponent is a constant factor; \(a_j=1\) interpreted as coordinate white noise is excluded.

**Derivation.** Fix the midpoint \(\vartheta=(\alpha_0+2-\alpha)/2\) and define \(b_0,\chi\) from the three-parameters. For the product case, PROOF030 gives \(b,v\) and the endpoints \(\gamma_b,\gamma_v\) of exponents \(1,\chi\) satisfying the Gaussian comparison. For the Riesz case, \(\gamma_1=c|x|^{-1}\), \(\gamma_\chi=c|x|^{-\chi}\) are admissible covariants via the Gaussian-mixture identity, and \(\alpha=\vartheta+(1-\vartheta)\chi\) gives \(\gamma_\alpha=\gamma_1^\vartheta\gamma_\chi^{1-\vartheta}\) a.e., hence Hölder gives the comparison. Thus `H:three-endpoints` holds and PROOF033 applies.

**Consumed hypotheses/conditions.** Only the two listed subclasses. No general three-dimensional factorization is asserted.

---

## PROOF035

**Statement (C:three-finite-images).** Let \(d=3\), \(0<\alpha_0<1\), \(1<\alpha<2-\alpha_0\). Let each \(\Gamma_i\) belong to one of: the ordinary products of PROOF034; the isotropic Riesz covariances of PROOF034; or the plane-supported measures of PROOF031 with \(a_1+a_2=\alpha-1\). Let \(T_i\) be invertible linear maps and \(w_i\ge0\) with \(\sum_iw_i>0\). Then the coefficient, all-time, and nonsharp variational estimates hold for
\[
\Gamma=\sum_{i=1}^Nw_i(T_i)_\#\Gamma_i,
\]
with endpoints
\[
\Gamma_{\rm low}=\sum_iw_i(T_i)_\#\Gamma_{{\rm low},i},\qquad
\Gamma_{\rm st}=\sum_iw_i(T_i)_\#\Gamma_{{\rm st},i}.
\]

**Derivation.** Fix the common midpoint \(\vartheta=(\alpha_0+2-\alpha)/2\). Each component endpoint triple is supplied by PROOF030, by the Riesz computation, and by PROOF031. Apply the pushforward closure and finite-sum closure of PROOF032 to obtain a target-endpoint triple satisfying `H:three-endpoints`, then apply PROOF033.

**Consumed hypotheses/conditions.** Only finite positive sums of invertible linear images of the listed classes. No infinite-mixture limit or representation theorem for arbitrary covariances is proved; the endpoint variational quantities are those of the constructed transformed covariances, and are not claimed to be wave constants unchanged under nonorthogonal maps.

---

## APPLICATION-SOURCE-COUPLING

This is the named foundation application supplied by **F007** (`integrated_source_convergence.tex`), not a new proof ID and not the operator-driver convergence. Full notation: \(a=\alpha_0\), Euler Gamma \(\Gamma_E(a)\); \(\nu_a(\ud\lambda)=\lambda^{a-1}\ud\lambda/\Gamma_E(a)\).

### 1. Spatial Hilbert space and heat
For \(\Gamma\) nonnegative even positive-definite tempered Radon, define the real test-null completion **\(H_\Gamma\)** with
\[
B_\Gamma(f,g)=\int\Gamma(\ud y)\int f(x)g(x-y)\ud x
=(2\pi)^d\int\widehat f(\xi)\overline{\widehat g(\xi)}\mu(\ud\xi),
\]
\[
p_\varepsilon(x)=(2\pi\varepsilon)^{-d/2}e^{-|x|^2/(2\varepsilon)},\qquad
C_\varepsilon f=p_\varepsilon*f.
\]
Heat is a positive self-adjoint contraction on \(H_\Gamma\), \(I-C_\varepsilon\) is a contraction, and \(C_\varepsilon\to I\) strongly. The Fourier multiplier of \(C_\varepsilon\) is \(m_\varepsilon(\xi)=e^{-\varepsilon|\xi|^2/2}\); \(H_\Gamma\) is separable by countable smooth approximation on compacts. This is the real quotient of the completed test space; no physical mask on a noise quotient is used.

### 2. Feature space
Set
\[
\mathcal G=L^2((0,\infty)_\lambda\times\R_r,\nu_a(\ud\lambda)\ud r;H_\Gamma).
\]
On finite smooth spacetime tensors define the actual Laplace feature
\[
\Phi F(\lambda,r)=\sqrt{2\lambda}\int_{t>0,\ t\ge r}e^{-\lambda(t-r)}F(t,\cdot)\ud t.
\]
The identity \(\int_{-\infty}^{\min(t,u)}2\lambda e^{-\lambda(t+u-2r)}\ud r=e^{-\lambda|t-u|}\) and the raw temporal Laplace representation give
\[
\|\Phi F\|_{\mathcal G}^2=\|F\|_{H_W}^2.
\]
Signed Fubini is absolutely integrable on finite tensors because compact temporal factors give \(\int|\tau(t)\sigma(u)||t-u|^{-a}\ud t\ud u<\infty\) for \(a<1\). Smooth partitions of a compact support uniformly approach a smooth spacetime test, so \(\Phi\) extends to an isometry with **closed range** in \(H_W\to\mathcal G\).

### 3. Retaining the original \(W\) (fixed \(W+J\), not W-only)
Let \(P\) be the orthogonal projection onto \(\Phi H_W\). On a product extension take one independent isonormal \(J\) on \((\Phi H_W)^\perp\), and define
\[
\mathcal I(g)=W(\Phi^{-1}Pg)+J((I-P)g).
\]
Orthogonality and independence make \(\mathcal I\) isonormal on all of \(\mathcal G\), and
\[
\mathcal I(\Phi h)=W(h)\quad\text{in }L^2,\qquad h\in H_W.
\]
This retains the actual original random variable \(W\). No independent replacement \(W\) and no \(\Phi\)-range/W-only assumption is made; cutoff fields may use \(J\). **F194** shows that for nonzero \(\Gamma\) and positive finite cutoffs the point feature is not in \(\Phi H_W\) and has positive conditional variance given \(\sigma(W)\), so any claim of W-only measurability of positive-cutoff point sources through a Phi-range argument is false; the nonlinear-limit W-measurability question is separate and open.

### 4. Cutoffs and the point/test law
Let \(P_\eta\) project \(\mathcal G\) onto \(\lambda\le\eta^{-1}\); let \(C_\varepsilon\) act fiberwise on \(H_\Gamma\). Define
\[
Q_\rho=C_\varepsilon P_\eta,\qquad
Y_\rho(F)=\mathcal I(Q_\rho\Phi F),\qquad
D_\rho(F)=\mathcal I((I-Q_\rho)\Phi F)=W(F)-Y_\rho(F),
\]
where the last equality uses the actual retention coupling. With
\[
\Gamma_e=(p_e*\Gamma),\qquad
K_\eta(v)=\frac1{\Gamma_E(a)}\int_0^{\eta^{-1}}e^{-\lambda|v|}\lambda^{a-1}\ud\lambda,
\]
\[
v_{\rho;t,x}(\lambda,r)=
\mathbf1_{\{\lambda\le\eta^{-1}\}}\sqrt{2\lambda}e^{-\lambda(t-r)}\mathbf1_{\{r\le t\}}p_\varepsilon(x-\cdot),
\qquad
Y_\rho(t,x)=\mathcal I(v_{\rho;t,x}),
\]
the joint covariance is
\[
\operatorname{Cov}\big(Y_{\varepsilon,\eta}(t,x),Y_{\varepsilon',\eta'}(s,y)\big)
=K_{\max(\eta,\eta')}(t-s)\Gamma_{\varepsilon+\varepsilon'}(x-y).
\]
The heat inner product reproduces \(\Gamma_{\varepsilon+\varepsilon'}\) by
\[
B_\Gamma(p_\varepsilon(x-\cdot),p_{\varepsilon'}(y-\cdot))=\Gamma_{\varepsilon+\varepsilon'}(x-y),
\]
so the pointfield–test Bochner identity on the same retaining space is
\[
\int F(t,x)v_{\rho;t,x}\ud t\ud x=Q_\rho\Phi F,
\qquad
Y_\rho(F)=\int F\,Y_\rho(\cdot,\cdot)\quad\text{in }L^2.
\]

### 5. Domination, residual decomposition, strong convergence
For \(g\in\mathcal G\),
\[
\|(I-Q_\rho)g\|_{\mathcal G}^2
=\|(I-P_\eta)g\|_{\mathcal G}^2+\|P_\eta(I-C_\varepsilon)g\|_{\mathcal G}^2\le\|g\|_{\mathcal G}^2,
\qquad
\|Q_\rho g\|_{\mathcal G}\le\|g\|_{\mathcal G},
\]
hence both source and full residual variances obey
\[
\operatorname{Var}Y_\rho(F),\ \operatorname{Var}D_\rho(F)\le\|F\|_{H_W}^2,
\qquad
\operatorname{Var}D_\rho(F)\to0
\]
for every \(F\in H_W\) as \(\varepsilon,\eta\downarrow0\) at arbitrary relative rates. The orthogonal \(\lambda\)-tail decomposition is exactly the two-range orthogonality in the identity above. The full spatial heat residual \(D_\rho\) need not be independent of \(Y_\rho\); only the disjoint \(\lambda\) ranges are independent. Pointwise \(L^2\) convergence transfers through the test class by common-support indicator approximation and the domination. Consequently the driver paths \(M_R^\rho=M_{Y_\rho}\) converge to \(M_R\) in \(L^p(\mathscr B_\theta)\), with \(M_{D_\rho}=M_R-M_R^\rho\), and have uniform local Gaussian driver moments and square-exponential norms at fixed \(R,T\).

### 6. Connection to the F001 foundations
- **`PROOF006` (`L:joint-fixed-order`)**: the exact positive-width covariance law computed here produces the diagonal/cross two-chain Wick sums whose Green-then-noise joint limits are asserted there; the common feature space realizes every finite diagram covariance for a fixed retaining extension, including unequal and empty chains.
- **`PROOF008` (`L:vertex-crude`)**: the bounded source variance and the explicit edge-by-edge heat/Laplace structure supply the finite edge norms used in `(E:vertex-crude)`, with the vertexwise copy widths treated edge-by-edge.
- **`PROOF009` (`P:mild-construction`)**: F007 (`P:source-ordinary-response`) supplies the fixed-cutoff statewise ordinary response \(L_\rho(t)=M_R^\rho\) on one probability-one set, giving the source-side product-limit leg for the held-integrand/Green-first construction. The canonical mild-source passage remains in F001, not in F007.

### 7. Explicit non-premises
No operator-driver Gaussian parent (`085/093/095`) is imported; full operator-driver convergence is not assigned here. The derivative estimate uses the correct `temporalMAX/spatialSUM` joint covariance, not the differing spatial-indexed author display. Nonlinear Young flow, canonical initial datum \((1,0)\), and its solution-moment transfer are separate parts of the argument. The ordinary raw variance-half action appearing in the retained original \(W\) variables is unchanged by this extension.

---

## GLOBAL-UNPROVED-CONDITIONS

1. **Scope of the 011–035 + F007 reconstruction.** This response reconstructs exactly the 25 target proofs and the named F007 source coupling. It is not full `MAIN/cold/fullgoal` closure, not the original135? full operator-driver convergence, and not the sharp intrinsic constant \(C_2\) identification. All debts outside these sections are unchanged.

2. **Finite-order calibrations (011–013) do not determine all-order asymptotics.** The values \(11/540\), \(t^3/3\), the Riesz integrals, and the white order-four table are nonnegative finite coefficients. The limits use disjoint-pair dominated convergence and do not exchange \(t\to\infty\) with \(\alpha_0\downarrow0\). The normalized Riesz-to-white check is a finite-coefficient normalization check only; unnormalized \(|y|^{-\alpha}\) is not identified with \(\delta_0\). No application of these calibrations to an asymptotic constant is discharged.

3. **One- and low-dimensional upper bounds (014–019).** PROOF015 proves the upper scale for the two explicit one-dimensional covariances; PROOF018 for \(0<\alpha\le1\), \(d=1,2,3\), under `H:homog` and positivity. The descending closing/opening invariant and the \(k^{-(2-\alpha)k}\) factor are established. The pairwise temporal symmetry is applied only to the summed pairings after the common spatial bound. PROOF019’s \(2L_*\le2C_{1,*}\) is conditional on a valid first-moment lower rate with the printed source normalization; no printed normalization is adopted. No all-order per-diagram factorial estimate is claimed.

4. **Higher exponents (020–023) remain conditional on `H:spatial-maximum`.** The Riesz discharges cover \(d=3,1<\alpha<2\), and \(d=2,1<\alpha<3/2\); the anisotropic product divergence is an anti-to-this-method result valid for every \(1<\alpha<2\) in dimensions two and three. The planar Riesz divergence at \(\alpha=3/2\) is a genuine failure of the spatial supremum, not of the full upper theorem or of moment finiteness. These no-go results constrain this method, not the independent full upper theorem.

5. **Static coefficient inputs (024–029) are imported published results, not proved.** The coefficient upper rate is supplied by Chen–Hu published `(5.1) p. 2173` and `(5.15) p. 2180` with fixed-order \(L^2\) existence `Theorem 3.8(i) p. 2165`; the generalized covariance class, Dalang verification, product/Wick, and the `(2.18)/(2.22)/(3.1)` conventions are consumed under their stated hypotheses. The homogeneity factor \(B_k(t)=t^{(4-\chi)k}B_k(1)\) and the rate are first converted to the all-order \(C_{\rm st}\). The values are not sharp, depend on \(\vartheta\), and are not claimed uniform in the covariance.

6. **Chen–Hu 2023 is only variational finiteness.** Chen 2023 `Theorem 1.1 p. 2` is consumed only as finiteness of the variational quantity under Dalang; it is not a coefficient-rate theorem and is not used to import a constant.

7. **Balan–Conus is comparison only.** `Theorem 2.1(b)/(8)/(10) p. 1492` and the \((2H+2-a)/(3-a)\) exponent are used only as same-parameter comparison context in different (Skorohod) solution and covariance normalization. No Skorohod proof, solution, or constant is imported.

8. **Three-dimensional endpoint route (030–035) is conditional on `H:three-endpoints`.** It is discharged only for strict products, isotropic Riesz, plane-supported Dirac-plane covariances, and finite positive sums of invertible linear images. No general three-dimensional factorization is proved; nonorthogonal maps change endpoint spectral masses, closing bounds, and variational quantities; zero static rate is handled without division by that rate.

9. **PROOF033 all-time vs asymptotic separation.** The all-time coefficient uses the imported finite \(C_{\rm st}\); the asymptotic
\[
\Lambda_{\rm st}=2\Big(\frac{2\sqrt{\mathcal M_{\rm st}}}{4-\chi}\Big)^{4-\chi}
\]
is used only in the limsup statement, with the finitely many low orders kept as a polynomial whose normalized logarithm vanishes. The variational limsup is nonsharp and is not substituted into the pure all-time constant.

10. **Physical/spectral energy for measure covariances (consumed by 033) is `PROOF036`, outside this set.** The positive-measure energy equality and finiteness of \(\mathcal M_{\rm st}\) originate in `L:physical-spectral-energy`, whose finiteness input is the quartic variation in Chen 2023 `Theorem 1.1`. If PROOF036 is not supplied in this response, the \(\mathcal M_{\rm st}\), \(\Lambda_{\rm st}\) displays and the bounded measure-energy functional remain a retained premise.

11. **F007 applicability boundaries.** The extension is the actual \(W+J\) construction with one fixed auxiliary isonormal \(J\). No independent replacement \(W\), no cutoff-W-only/Phi-range assumption, and no fixed-filter commutator through a physical mask is used. F194 establishes that positive-cutoff point features have a nontrivial \((I-P)v\) part; simultaneous W-only representation across cutoff parameters is not required for F007’s conclusions. The nonlinear flow, canonical initial datum, and moment transfer remain F001 obligations.

12. **Dirac/plane spectral \(c/\pi\), closing \(S/4\), planar line factor \(1/2\), and anisotropic \(a_1+a_2/2>1\)** were reported as needed for the falsification. The \(c/\pi\) value and the \(1/2\) factor are the exact computations; positivity of `<PROOF036>`-style covariances applies only to the justified Gaussian-mixture forms, not to arbitrary multiplication by covariance weights.

13. **No verdict, confidence, grade, favorable example, or acceptance.** Every coefficient, constant, domain, quantifier, and consumed source hypothesis above is reported only with its actual proof or its precise missing premise.