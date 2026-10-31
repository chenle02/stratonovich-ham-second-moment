#!/usr/bin/env python3
"""Exact finite wave/constant forcing projection controls, not a spectral proof."""
from fractions import Fraction as F
from pathlib import Path
import json

def zero(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n):
 a=zero(n,n)
 for i in range(n):a[i][i]=F(1)
 return a
def mul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def scale(c,a):return [[c*x for x in row] for row in a]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
rows=[]
for lam in [F(1),F(2),F(3)]:
 for mu in [F(0),lam/2]:
  for beta in [F(1),F(3)]:
   for eta in [F(-1),F(0),F(2)]:
    L=zero(6,6)
    L[0][2]=L[1][3]=L[4][5]=F(1)
    L[2][0]=lam*lam;L[3][1]=mu*mu
    L[2][4]=beta;L[3][4]=eta
    e=[[F(1)],[F(0)],[lam],[F(0)],[F(0)],[F(0)]]
    ell=[[F(1,2),F(0),1/(2*lam),F(0),beta/(2*lam**2),beta/(2*lam**3)]]
    Pi=mul(e,ell);Q=sub(eye(6),Pi)
    assert mul(L,e)==scale(lam,e)
    assert mul(ell,L)==scale(lam,ell)
    assert mul(ell,e)==[[F(1)]]
    assert mul(Pi,Pi)==Pi and mul(Pi,Q)==zero(6,6)
    assert mul(L,Pi)==mul(Pi,L)==scale(lam,Pi)
    bad_ell=[ell[0][:4]+[F(0),F(0)]]
    bad_Pi=mul(e,bad_ell)
    defect=sub(mul(bad_ell,L),scale(lam,bad_ell))
    assert defect[0][4]==beta/(2*lam)>0
    assert mul(L,bad_Pi)!=mul(bad_Pi,L)
    e0=zero(6,1);e0[4][0]=F(1)
    assert mul(bad_ell,e0)==[[F(0)]]
    assert mul(ell,e0)==[[beta/(2*lam**2)]]
    # Proposed growing-projection remainder on constant forcing is polynomial.
    v=beta/(2*lam)
    for t in [F(0),F(1,2),F(2),F(5)]:
     for c1,c2 in [(F(1),F(0)),(F(0),F(1)),(F(-2),F(3))]:
      residual=-v*((c1+t*c2)/lam+c2/lam**2)
      derivative=-v*c2/lam
      assert derivative==lam*residual+v*(c1+t*c2)
      if t==0:assert residual==-(ell[0][4]*c1+ell[0][5]*c2)
    rows.append({'lambda':str(lam),'mu':str(mu),'ground_forcing':str(beta),'complement_forcing':str(eta),'correct_constant_entrance':str(beta/(2*lam**2)),'wrong_projection_commutator_defect':str(defect[0][4])})
out={'scope':'Exact rational finite six-coordinate wave generator: two spatial-mode markers and two constant markers. Not a continuum spectral theorem, covariance substitution, ground existence/gap or moment lower bound.',
     'coordinate_order':['u_ground','u_complement','v_ground','v_complement','c_displacement','c_velocity'],
     'checked':'right/left eigenvector, normalized rank-one projection, commutation; wrong missing-constant projection fails; polynomial forcing residual differential and initial identities',
     'case_count':len(rows),'cases':rows,'residual_checks':len(rows)*4*3,
     'limitations':'The continuum ground positivity, common negative Rayleigh trial, L2/H2 continuity and global-E/F complement estimates remain unproved targets. Zero mu cases test threshold algebra only.'}
Path(__file__).with_name('constant-projection-v0.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS 36 exact wave/constant projection cases and432 forcing-residual identities; missing-constant projection rejected.')
