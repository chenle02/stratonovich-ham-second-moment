# Exact physical normalization screen and its limits

The target was frozen before these checks. The script uses mpmath 40/70
working digits, actual d1 white covariance 3 delta_0, a=1/3, unequal time
cells of lengths2/5 and3/5, and smooth real compact unit-L2 bumps.
The physical mask is one smooth plateau eta², equal1 on[-1,1], supported
on[-2,2]. One bump is in the core and one crosses the transition region.

For test cell i, the control is h_j tensor rho_i (SAME spatial profile i),
where h_j=1_Ij/ell_j and rho_i=f_i². Thus the four rows test both time
diagonal and time off-diagonal pairings without a zero spatial signal.
The independently integrated averaged temporal mean agrees with the closed
time-kernel pairing formula. All per-row residuals and per-precision maxima
and maximizing cases are retained. Maximum row residuals were
3.6734198463196484624e-40 and2.8978173052245479576e-70, both at(i,j)=(0,0).
This calibrates the normalization; it does not prove PB1 or any SPDE bound.

Wrong-factor controls have nonzero gaps: omit the division by ell_i,
apply covariance amplitude3 a second time, or use m² in place of the one
physical mask (last control evaluated on the transition bump). The same
integrals also calibrate masked/unmasked Gram entries. Raw output field
names `masked_gram_diagonal` and `unmasked_gram_diagonal` denote actual
diagonals ONLY when j=i; for j!=i they are pairings of two different time
labels with the SAME spatial profile i. They are not off-diagonal entries
for the two different spatial bumps. The actual two-bump white Gram has
these j=i diagonals and zero off-diagonals, since the spatial supports
are disjoint. No PSD conclusion is inferred from floating eigenvalues.

The Riesz diagnostic uses alpha=1/2 and the same disjoint supports, so its
cross integral has no singularity. D11-C11=0 exactly, because the first
bump lies entirely in the plateau. D12-C12 is strictly positive by positive
integrands on the two supports and m<1 on the second; hence the exact
2x2 difference determinant is -(D12-C12)²<0, irrespective of its22 entry.
This is a proposed elementary witness for the unnecessary Loewner-order
shortcut, to be independently audited. It does NOT refute PB's entrywise
order or imply a covariance comparison for arbitrary-phase wave evolution.
24/40-node Gauss-Legendre evaluations differ by about2.8972711544e-7 at
BOTH precisions. This exposes quadrature error independent of arithmetic
precision; 70 working digits are not70-digit integration accuracy. Both
mesh values and their changes are retained, with no enclosure assertion.

Scalar q=-1,+1 gives average sqrt(q_+)=1/2 > sqrt((average q)_+)=0;
q=0,4 gives1 < sqrt(2). Both global Jensen directions are therefore
unavailable. These are exact scalar controls, not physical-wave simulations.

No optimizer/global certificate, numerical PDE, statistical confidence,
source constant identity, general covariance proof or PB1-PB5 proof follows.
No prior PG or Lean computation was rerun. The script exit was0.
