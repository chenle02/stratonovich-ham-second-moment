# Next mechanism screen: static blocks must retain velocity

Status: UNREVIEWED research-direction and exact finite diagnostic. No new
moment bound,no accepted route kill,no source theorem or novelty claim.
The example below is scalar,with spatially constant noise and independent
static time blocks,outside the project's homogeneous covariance class. It does not refute the target or a correctly weighted operator
norm estimate.

The geometric approximation route has not supplied the arbitrary-covariance
step. A different possible mechanism is to dominate the temporal covariance
by a dyadic sum of static spatial fields supported on time blocks,then use
static Gaussian-wave estimates on the phase vector (u,du/dt). A formal scale
calculation is encouraging but is NOT a proof: static growth power
q=(4-alpha)/(3-alpha),block length h,variance amplitude h^{-alpha0},and
approximately t/h blocks would give

 (t/h) h^{(4-alpha)/(3-alpha)} h^{-alpha0/(3-alpha)}
 =t h^{(1-alpha0)/(3-alpha)}.

The largest block h=t has the target exponent kappa. This would require a
valid covariance domination INCLUDING shifted dyadic grids,uniform estimates
for full phase-space propagators,control of the sum of overlapping independent
levels,and a legitimate infinite-level/noise-regularization limit. No such
composition estimate has been established. In particular no Gaussian
additive-covariance logconvexity may be used;the previous exact scalar test
already refuses that shortcut.

Falsification before investing in that program: even two independent scalar
static blocks do NOT multiply their second moments for data(1,0). Let y''=Z_i y
on consecutive unit intervals,i=1,2,with independent centered Gaussian Z_i of
variance A. Set c(z)=cosh(sqrt(z)),s(z)=sinh(sqrt(z))/sqrt(z),understood by
their entire power series,so negative z gives the corresponding cosine/sine.
The exact phase propagator is

 M(z)=[[c(z),s(z)],[z s(z),c(z)]].

Thus the final value is c(Z2)c(Z1)+s(Z2)Z1s(Z1),not c(Z2)c(Z1).
The exact rational FORMAL expansion gives

 E y(1)^2=1+A/3+O(A²),
 E y(2)^2=1+3A+O(A²),
 [E y(1)^2]^2=1+2A/3+O(A²).

The formal first-order gap is7A/3. The accompanying script computes through
A² by independent Gaussian even-moment substitution,without floating-point
quadrature. This is a finite diagnostic,not an analytic remainder certificate.
It says to carry velocity and study an operator/energy norm BEFORE attempting
an SPDE block theorem. It neither proves that such a norm estimate exists nor
rules it out. Any proposed inequality must state which phase norm,noise
amplitude,interval length and constants it uses,then pass this test.

[held back: collaborators' unpublished work]