"""Exact and finite local calibration; not the all-order theorem or Lean."""
from fractions import Fraction as F
import json
import mpmath as mp
mp.mp.dps=50
M0=[[F(1),F(1)],[F(0),F(1)]]
M1=[[F(1,2),F(1,6)],[F(1),F(1,2)]]
M2=[[F(1,24),F(1,120)],[F(1,6),F(1,24)]]
K=[[sum(M1[k][i]*M1[k][j]+M0[k][i]*M2[k][j]+M2[k][i]*M0[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert K==[[F(4,3),F(4,5)],[F(4,5),F(17,45)]]
x=[F(1),F(-2)]
negative=sum(x[i]*K[i][j]*x[j] for i in range(2) for j in range(2))
assert negative==F(-16,45)
rows=[]
for a in [mp.mpf('.5'),mp.mpf('1'),mp.mpf('1.5'),mp.mpf('1.9')]:
    c=2**a+3**(2-a)/(2-a)
    values=[]
    for r in [mp.mpf('0'),mp.mpf('.25'),mp.mpf('.5'),mp.mpf('1'),mp.mpf('2'),mp.mpf('4')]:
        val=mp.mpf(1) if r==0 else ((1+r)**(2-a)-abs(1-r)**(2-a))/(2*r*(2-a))
        assert val<=c
        values.append(str(val))
    radial=a*mp.quad(lambda r:r**(a-1)/(1+r*r),[0,1,mp.inf])
    exact=a*mp.pi/(2*mp.sin(mp.pi*a/2))
    assert mp.almosteq(radial,exact,rel_eps=mp.mpf('1e-4')) # alpha1.9 has a slow infinite tail.
    rows.append({'alpha':str(a),'riesz_bound':str(c),'sample_wave_values':values,'resolvent_numeric':str(radial),'resolvent_exact':str(exact)})
print(json.dumps({'scalar_toy':'spatially constant static field,alpha=0 outside the strict theorem','first_variance_phase_matrix':[[str(x) for x in row] for row in K],'phase_1_minus2_coefficient':str(negative),'note':'full phase energy need not increase with covariance; the mean second-order term must be retained','normalization_rows':rows,'status':'PASS'},indent=2))
