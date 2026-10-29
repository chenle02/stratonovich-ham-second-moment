# Restricted deterministic-tilt shortcut: planning screen only

This is a scalar optimization diagnostic,not an SPDE theorem,a new proof wave,
a novelty claim or a no-go for all Gaussian tilts. The full sharp target stays
unchanged. It concerns a tempting shortcut for the eventual lower bound.

For a Gaussian Cameron--Martin density L_h, Cauchy--Schwarz gives
E[u^2] >= (E[L_h u])^2 / E[L_h^2]
       = exp(-||h||^2) (E^h u)^2.
If one THEN discards every residual Gaussian contribution and replaces the
tilted mean by only a deterministic surrogate exp(A H^r),the variational
objective is 2 A H^r-H^2. It is exactly TWICE
A H^r-H^2/2,at every H. Thus this shortcut supplies 2F where
F=sup_H(A H^r-H^2/2),rather than the desired annealed objective
sup_H(2 A H^r-H^2/2)=2^[2/(2-r)] F.
For the prospective static-wave homogeneity r=2/(4-alpha),the latter exponent
is q=(4-alpha)/(3-alpha)>1. The missing factor is 2^(q-1).

This only screens THAT deterministic-surrogate substitution. F is not being
identified here with any unproved fractional-time first-moment constant.
The Gaussian residual may contribute at leading order,and Cauchy--Schwarz
itself is not a no-go. Elementary negative control:for Y=exp(aZ),Z standard
normal,E^h Y=exp(ah+a^2/2). The FULL tilted-mean Cauchy bound optimized at
h=a is exp(2a^2)=E Y^2 exactly. Replacing it by exp(ah) gives only exp(a^2),
twice the log first mean. The missing residual is precisely the loss.

Investment consequence:do not launch a long deterministic-mean Cauchy
argument expecting the conjectured factor merely from amplitude optimization.
A successful shift route must retain a leading residual contribution or use
a different measure/positivity argument. The already screened static temporal
minorant is a separate route and does not make this substitution.

[held back: collaborators' unpublished work]