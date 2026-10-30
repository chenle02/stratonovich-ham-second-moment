# Next complementary-wave bridge: proof obligations

UNREVIEWED planning, not a theorem or proof adoption. Do not use downstream.
This stays inside the independently audited S1 target at
reviews/2026-10-30-spectral-phase/target-v2.md.

1. On global E=H1/2 x H-1/2 set A_b=H_b+c with c=1+b1||U||infinity,
B=1-d2. Quadratic forms obey B<=A_b<=cB uniformly. Need a complete
fractional-power comparison and negative-dual identification, not just
H1/L2 endpoint bounds. A route is the positive square-root resolvent
integral, inverse form monotonicity and spectral theorem, with domains
and truncation limits explicit. This is not yet a source-imported lemma.

2. On the global L2 complement of p_b, spectral support is contained in
[E2(b),infinity). For h in that support the physical wave matrix has
cos(t sqrt(h)) and sin(t sqrt(h))/sqrt(h), continued through h=0
and to negative h with cosh/sinh. In the A-weighted phase norm, bound
cos and sqrt(h+c)sin/sqrt(h), and h sin/(sqrt(h+c)sqrt(h)).
The zero threshold costs a polynomial (1+t), not an inverse mu_b.
Remove ONLY the growing ground branch; its decaying partner stays.
Expected intermediate: C(1+t)exp(mu_b t) on global E. Must prove equality
with the named physical flow, not a different spectral evolution.

3. For every output cell j choose a smooth input cutoff kappa_(j,t)
equal1 on its backward cone, centered at j with radius t+C. A finite
partition/triangle argument should give global E norm <=C(1+t)||z||F
for kappa z. Do not assume global E dense in F. Prove deterministic
potential finite propagation for the actual F flow from Duhamel and
local distributions, then the exact localized projection identity.

4. The identity to check, for R_b(t)=P_b(t)(I-Pi_b), is

 chi_j R_b(t)z = chi_j R_b(t)(kappa z)
                  +exp(lambda_b t)chi_j e_b ell_b((kappa-1)z).

The second term cannot be discarded. Weighted projection tails suggest
||chi_j e_b||E<=C exp(-beta |j|), while the missing-input pairing is
<=C exp(-beta(t-|j|-C)_+)||z||F. Their product is <=C exp(-beta t)||z||F,
including cells outside the cone and constant initial phases. Prove the
geometry and cutoff derivative estimates uniformly in t,j,b. This would
leave exponents mu_b and lambda_b-beta, both separated from lambda_b.

5. Uniform absorption: with d=inf(lambda_b-mu_b)>0 and beta>0, choose
0<eta<min(d,beta,inf lambda_b)/2 and absorb the polynomial with an exact
uniform bound. No entire-product, endpoint observable, stochastic event,
variational optimizer or sharp-constant conclusion follows from this alone.

Finite falsification controls before proof: threshold h=0 must retain the
linear-in-t velocity solution; outside-cone j must keep the projection
tail correction; the decaying ground partner must remain; constant data
must be handled by cutoff, not a global L2 inclusion.
