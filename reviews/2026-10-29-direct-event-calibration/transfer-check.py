"""Floating closed-transfer consistency only, not a certified enclosure."""
import mpmath as mp
import json,hashlib
from pathlib import Path
mp.mp.dps=60

def flow(q,t):
    if q>0:
        z=mp.sqrt(q);a=mp.cosh(z*t);b=mp.sinh(z*t)/z
    elif q<0:
        z=mp.sqrt(-q);a=mp.cos(z*t);b=mp.sin(z*t)/z
    else:a,b=mp.mpf(1),t
    return mp.matrix([[a,b],[q*b,a]])
E=flow(mp.mpf(1),mp.mpf(1));rows=[]
for e in ['0','.001','.01','.0125']:
 eta=mp.mpf(e)
 for m in [1,3,8,40,64,512,4096]:
    d=1/(2*mp.mpf(m));qm,qp=1-2*m*eta,1+2*m*eta
    T=(flow(qp,d)*flow(qm,d))**m
    error=max(abs(T[i,j]-E[i,j])for i in range(2)for j in range(2))
    for i in range(2):
     for j in range(2):
      assert (1-40*eta)*E[i,j]-mp.mpf('1e-48') <= T[i,j]
      assert T[i,j] <= (1+40*eta)*E[i,j]+mp.mpf('1e-48')
    rows.append(dict(eta=e,periods=m,qminus=str(qm),qplus=str(qp),entry_error=str(error),qminus_is_negative=qm<0,transfer=[[str(T[i,j])for j in range(2)]for i in range(2)]))
out=dict(status='PASS finite floating transfer checks, not proof/enclosure',dps=60,cases=len(rows),negative_potential_cases=sum(q['qminus_is_negative']for q in rows),zero_potential_cases=sum(q['qminus']=='0.0'for q in rows),rows=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
