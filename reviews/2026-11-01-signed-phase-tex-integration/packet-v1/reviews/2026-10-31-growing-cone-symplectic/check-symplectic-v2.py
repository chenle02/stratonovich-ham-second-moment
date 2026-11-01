"""Exact rational finite Hamiltonian screening; not a PDE discretization."""
import json
from pathlib import Path
import sympy as s
import mpmath as mp
mp.mp.dps=60
n=3
I=s.eye(n); O=s.zeros(n); J=O.row_join(I).col_join((-I).row_join(O))
lamroot=s.diag(1,s.Rational(5,4),s.Rational(5,3))
lam=lamroot**2
K=lam**2-I
A=O.row_join(lam).col_join((-K*lam.inv()).row_join(O))
def defect(P):
 D=P.T*J*P-J
 return str(max(abs(x) for x in D))
def cayley(A,h):
 return (s.eye(6)-h*A/2).inv()*(s.eye(6)+h*A/2)
def norm(P):
 G=P.T*P
 M=mp.matrix([[mp.mpf(str(s.N(G[i,j],65))) for j in range(6)] for i in range(6)])
 return mp.sqrt(max(mp.eigsy(M,eigvals_only=True)))
V0=s.zeros(3)
V1=s.diag(2,-3,1)
V2=s.Matrix([[0,1,-2],[1,0,3],[-2,3,0]])
V3=s.Matrix([[2,-1,0],[-1,-4,2],[0,2,1]])
rows=[]
for name,V in [('free',V0),('signed_diagonal',V1),('signed_offdiagonal',V2),('mixed',V3)]:
 B=O.row_join(O).col_join((lamroot.inv()*V*lamroot.inv()).row_join(O))
 H=A+B
 C=lamroot.row_join(O).col_join(O.row_join(lamroot.inv()))
 Hphysical=O.row_join(I).col_join((-K+V).row_join(O))
 assert C*Hphysical*C.inv()==H
 assert H.T*J+J*H==s.zeros(6)
 P=s.eye(6)
 for h in [s.Rational(1,7),s.Rational(1,11),s.Rational(1,13)]:
  P=cayley(H,h)*P
 assert defect(P)=='0'
 assert P.det()==1
 rows.append({'case':name,'physical_Bessel_similarity_exact':True,'symplectic_defect_exact':defect(P),'determinant_exact':str(P.det()),'norm_60digit_diagnostic':mp.nstr(norm(P),35)})
# Three explicit false models: no surrogate is an SPDE approximation.
P=cayley(A,s.Rational(1,7))
Q=s.diag(1,1,1,0,0,0)*P
assert defect(Q)!='0'
badV=s.Matrix([[0,1,0],[0,0,0],[0,0,0]])
Bbad=O.row_join(O).col_join((lamroot.inv()*badV*lamroot.inv()).row_join(O))
Pbad=cayley(A+Bbad,s.Rational(1,7))
assert defect(Pbad)!='0'
# Physical coordinates transformed using the SAME weight for u and v.
# Then top-right is I and bottom-left -K+lam*V*lam^-1, not symmetric.
V=V2
Abad=O.row_join(I).col_join((-K+lamroot*V*lamroot.inv()).row_join(O))
Pweight=cayley(Abad,s.Rational(1,7))
assert defect(Pweight)!='0'
guards=[{'guard':'delete_velocity','symplectic_defect_exact':defect(Q)}, {'guard':'nonsymmetric_force','symplectic_defect_exact':defect(Pbad)}, {'guard':'same_Bessel_weights','symplectic_defect_exact':defect(Pweight)}]
out={'scope':'exact rational finite surrogate algebra, plus approximate norm diagnostics; no PDE projection, enclosure, stochastic estimate or raw flow result','cases':rows,'false_guards':guards,'sympy_version':s.__version__,'mpmath_version':mp.__version__}
Path(__file__).with_name('symplectic-controls-v2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
