# Falsification first: actual positive white rank-two profile

CANDIDATE short witness for independent audit, not yet adopted.
This refutes a universal exact b(sigma)U reduction, not optimizer
sufficiency or the original sharp moment conjecture.

Fix ANY0<a<1 and original d1 white Gamma=c_Gamma delta0,c_Gamma>0.
Choose nonzero nonnegative smooth f1 supported in(1/8,1/4), let
f2(u)=f1(1-u), and choose nonzero nonnegative smooth spatial bumps
q1 supported in(-2,-1),q2 supported in(1,2). Then
psi(u,x)=f1(u)q1(x)+f2(u)q2(x) is a legal positive nonseparable test.

Put A=int_0^1 u^-a f1(u)du and B=int_0^1 (1-u)^-a f1(u)du.
Both are finite/positive because support stays away from endpoints.
On supp f1, u<1-u, so u^-a>(1-u)^-a. Since f1 is positive on an
interval, A>B>0. Direct change of variable using the reflected f2 gives

 h_0=c_Gamma(Aq1+Bq2), h_1=c_Gamma(Bq1+Aq2).

Choose x1 with q1(x1)>0 and x2 with q2(x2)>0. Disjoint supports give

 h_0(x1)h_1(x2)-h_1(x1)h_0(x2)
       =c_Gamma^2(A^2-B^2)q1(x1)q2(x2)>0.

Thus the endpoint profiles are not proportional, so there cannot exist
a single spatial U and scalar b(sigma) representing ALLh_sigma. No
Fourier normalization or numerical singular-integral computation was used.
For a time where f1>0 only q1 appears, while for a time where f2>0 only
q2 appears. A single product would require these nonzero disjoint spatial
bumps to be proportional, which is impossible. Thus psi itself is not a
single product.
This is inside the actual allowed white model, with1+a<2.

Separate common-positive-profile screen: for any nonnegative psi and
sigma,u in[0,1], |sigma-u|^-a>=1 except the harmless integrable diagonal.
Hence q_sigma>=int psi(u,.)du=:q_avg and h_sigma>=Gamma*q_avg by the
positive Radon convolution. q_avg is nonzero smooth compact because
psi is nonzero/nonnegative. This screen supplies a candidate fixed
attractive comparison profile; it is NOT the desired uniform F-wave
complement, which still needs proof.

At the static endpoint a=0 the two endpoint weights coincide (A=B);
this witness is deliberately restricted to the stated positivea range.
