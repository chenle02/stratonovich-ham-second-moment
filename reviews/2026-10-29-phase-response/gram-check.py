"""Two-resolution check of the actual four-component temporal Gram norm."""
from pathlib import Path
import json,hashlib,math
import mpmath as mp
mp.mp.dps=60

def J(a,t,r):
    if not r:return 2*t**(2-a)/((1-a)*(2-a))
    z=-1j*abs(r)
    return 2*mp.re(t*z**(a-1)*mp.gammainc(1-a,0,z*t)-z**(a-2)*mp.gammainc(2-a,0,z*t))
old=json.loads(Path(__file__).with_name('quadrature.json').read_text())
for row in old['rows']:
    a,t,x=map(mp.mpf,[row['a'],row['t'],row['rt']]);v=J(a,t,x/t)
    assert abs(v-mp.mpf(row['time']))/v<mp.mpf('1e-40')
rows=[]
for a in [.1,.5,.9]:
 for r,k in [(.5,1.25),(3.,2.),(8.,5.)]:
  actual=float((J(mp.mpf(str(a)),mp.mpf(1),mp.mpf(str(r-k)))+J(mp.mpf(str(a)),mp.mpf(1),mp.mpf(str(r+k))))/2)
  samples=[]
  for n in [64,128]:
    h=1/n
    weights=[h**(2-a)*(abs(m+1)**(2-a)+abs(m-1)**(2-a)-2*abs(m)**(2-a))/((1-a)*(2-a))for m in range(n)]
    u=[(i+.5)*h for i in range(n)]
    f=[[math.sin(r*(1-x))*math.cos(k*x),math.sin(r*(1-x))*math.sin(k*x),math.cos(r*(1-x))*math.cos(k*x),math.cos(r*(1-x))*math.sin(k*x)]for x in u]
    four=math.fsum(weights[abs(i-j)]*math.fsum(f[i][v]*f[j][v]for v in range(4))for i in range(n)for j in range(n))
    combined=n*weights[0]+2*math.fsum((n-m)*weights[m]*math.cos(r*m*h)*math.cos(k*m*h)for m in range(1,n))
    assert abs(four-combined)<=1e-11*max(1,abs(four))
    samples.append(dict(n=n,four_component=four,combined=combined,relative_error=abs(four-actual)/actual))
  assert samples[1]['relative_error']<samples[0]['relative_error']
  rows.append(dict(a=a,r=r,k=k,actual=actual,samples=samples))
out=dict(status='PASS finite floating actual Gram check, not enclosure/proof',cases=len(rows),time_cells=[64,128],cell_covariance='exact raw integral over each pair of time cells; singular diagonal retained',old_time_quadrature_cases_rechecked=len(old['rows']),rows=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
