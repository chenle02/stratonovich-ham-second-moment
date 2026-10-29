Next fixed-split repair: UNREVIEWED derivation plan, not an adopted proof.

Keep the full statement, covariance class, self-pairings and ordinary degrees.
Do not weaken the theorem or promote this plan using the previous HIGH report.

1. For each copy fix its background set A, its cross set C and a tuple of
   distinct insertion times outside background endpoints. Define the common
   partition from 0,T,all clipped background endpoints and these insertion
   times. Write its constant heights Lambda_j explicitly. Its number of open
   pieces is at most 2|A|+|C|+1, hence at most3k+1.
2. Write the identity map between successive phase norms. Its bound is
   max(1,Lambda_old/Lambda_new). At simultaneous endings E and starts S,
   with R the sum of remaining weights, the ratio is
   (lambda+R+sum_E omega)/(lambda+R+sum_S omega).
   Bound the loss by product_E(1+omega/lambda). The initial height increase
   contracts;the final return charges all still-active intervals as endings.
   Each connected interval is charged once. Insertion cuts change no height.
   endpoint-budget-check.py tests this finite rational budget;it is not proof.
3. Define the tensor subspace in which unused cross colors are vacuum and
   used cross colors are in first Gaussian degree. Background evolution acts
   identically on all cross-color factors and preserves this subspace.
   Each J_i maps to the subspace with i newly used. Its bound is the fresh
   vacuum column sigma_i sqrt(R_alpha) lambda^((alpha-2)/2), not an occupied
   annihilation estimate. State this for every partial word, not informally.
4. Display the chronological word norm as the product of segment norms,
   identity-map norms and insertion norms. Segment constants are at most
   100^(3k+1);their exponentials multiply to at most exp(4k),because splitting
   at insertion times does not change the integral of Lambda.
   A proposed uniform word prefactor is M_k=100^(3k+1)exp(4k).
5. Write the coefficient integral over the full insertion cube,using its
   time-sorted word. Sum of permutation-simplex measures is exactly the cube
   measure,at most product_i h_i. There is no factor |C|! or its inverse.
6. Write normalized vector Cauchy integration over every background angle,
   with measure product_i dtheta_i/(2pi). Show each radius power explicitly.
   Then apply Cauchy--Schwarz between the two SAME-noise vectors;output phase
   conversion gives k^2 and initial norm conversion contracts. Do not apply
   a holomorphic formula to a squared norm.
7. Display the bound BEFORE absorption:
   k^2 M_k^2 D_A_r D_A_q product_B varrho_i^(-2k_i)
   times product_C(R_alpha sigma_i^2 h_i^2 lambda^(alpha-2)) times ||v||^2.
   Here D_A_r D_A_q has exactly exponent ell_i on each B color.
   Using d_i^2<=12k_i R_alpha,the planned radius inequality is
   varrho_i^(-2k_i) <= (12 delta_a^(-2))^k_i
     * (R_alpha sigma_i^2 h_i^(4-alpha))^k_i / (k_i!)^(3-alpha).
   M_k^2<= (100^8 exp(8))^k for k>=1. A proposed explicit admissible choice
   is C_split=100^8 exp(8) max(1,12 delta_(alpha/2)^(-2)).
   All these interfaces and this constant must be proved in the manuscript
   and freshly reviewed;the finite endpoint diagnostic does not establish them.

Also required before the next whole-paper gate:direct source-class audit for
the alternative static-measure imports;explicit structure in P:mixed without
an assumed product identity;indexed limit/uniformity trace;notation flags.
