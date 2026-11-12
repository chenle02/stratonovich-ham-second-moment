## 9. White controls obstruct uniform-R fixed smooth projections; scope

Here is a precise negative guard against an automatic growing-mask upgrade.
Take the admissible d1 white Gamma=delta0,alpha1, any0<a<1. From the scalar equilibrium identity/mass in damped-lower-endpoint-bridge.md Section2,
f_a in L2(I), K_a*f_a=1 and ||f_a||H_t²=M_a>0. Its H_t membership follows
by smooth L2 approximation and the Schur norm bound. Let q be a nonnegative
unit-L2 compact smooth bump and q_n(x)=q(x-x_n), centers escaping to infinity.
The raw H unit direction Phi_n=f_a tensor q_n/sqrt(M_a) has actual mean
q_n/sqrt(M_a), constant in time. This follows either directly from the
scalar identity or from the L2/mean completion in Sections5-6.

Fix J. The finitely many smooth compact basis tests spanning P_J have a
common compact spatial support. Choose x_n outside that support by more
than the radius of q. White spatial covariance gives P_J Phi_n=0 exactly,
regardless of temporal correlation. Choose R_n large enough that m_(R_n)=1
on supp q_n. Use F input e_disp=(0,0,1,0) in this section's four-entry
notation, norm1, and output dual w_n=(0,Lambda q_n/||q||H1/2,0,0), norm1.
The completed multiplier has the constant-in-time coordinate

 <T_(R_n)Phi_n(s)e_disp,w_n>F=1/[sqrt(M_a)||q||H1/2]>0.       (16)

Indeed the E velocity inner product has weight Lambda^-1, and q_n is unit
L2 with translation-invariant H1/2 norm. Thus for every fixed J,
 sup_R ||T_R(I-P_J)||H->Lr(K(F))>=1/[sqrt(M_a)||q||H1/2].
There is NO projection-tail convergence uniform in R for this fixed family.
This refutes ONLY that proposed extension, not fixed-R C1-C3, not all
projection/localization strategies and not the original sharp-upper goal.
For fixed R, sufficiently far white-noise q_n misses its mask. The negative
guard uses a bounded phase functional, no Sobolev point trace. It is the
exact control proposed separately in globalization-guard-v0.md.

