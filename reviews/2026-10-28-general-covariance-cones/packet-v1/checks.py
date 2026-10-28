"""Finite normalizations; not proof, formal verification or review."""
import json
from fractions import Fraction
import mpmath as mp
mp.mp.dps=60
rows=[]
for n in [2,3,4,6]:
    delta=mp.mpf(10)**(-n);t=1-delta
    peak=(1-t*t)/mp.pi*mp.quad(lambda phi:(delta*delta+2*t*(1-mp.cos(phi)))**(-mp.mpf('1.5')),[0,delta,mp.sqrt(delta),1,mp.pi])
    lower=1/(2*mp.sqrt(2)*mp.pi*delta)
    assert peak>=lower
    exact=2*(10**(n//2)-1) if n%2==0 else None
    cut=2*(delta**(-mp.mpf('.5'))-1)
    if exact is not None:assert mp.almosteq(cut,exact)
    mass=(1-t*t)/2*mp.quad(lambda v:(1-2*t*v+t*t)**(-mp.mpf('1.5')),[-1,0,1-delta,1])
    assert abs(mass-1)<mp.mpf('1e-45')
    rows.append({'delta':str(delta),'poisson_peak':str(peak),'peak_times_delta':str(peak*delta),'lower':str(lower),'raw_cosine_cutoff':str(cut),'poisson_total_mass':str(mass)})
a=Fraction(3,2);a0=Fraction(1,4)
assert a+a0<2
print(json.dumps({'alpha':str(a),'alpha0':str(a0),'rows':rows,'status':'PASS','scope':'finite normalization/numerical checks only; continuous proofs in proof.md'},indent=2))
