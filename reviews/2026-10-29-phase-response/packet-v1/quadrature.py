"""Independent time/Laplace checks; floating consistency, not enclosure."""
import mpmath as mp
import hashlib,json
from pathlib import Path
mp.mp.dps=60

def constants(a):
 return mp.pi/(mp.gamma(a)*mp.cos(mp.pi*a/2)),2*mp.pi/(mp.gamma(a)*mp.sin(mp.pi*a/2))

def time_integral(a,t,r):
    power=1/(1-a);x=r*t
    nodes=[mp.mpf(0)]+[(k*mp.pi/x)**(1-a)for k in range(1,int(mp.floor(x/mp.pi))+1)if k*mp.pi<x]+[mp.mpf(1)]
    return 2*t**(2-a)/(1-a)*mp.quad(lambda z:(1-z**power)*mp.cos(x*z**power),nodes)

def laplace_integral(a,t,r):
    def core(z):
        q=z-1j*r
        return mp.re(t/q-(1-mp.exp(-q*t))/(q*q))
    low=mp.quad(lambda u:core(u**(1/a))/a,[0,1])
    def high(u):
        if not u:return t/(1-a)
        z=u**(-1/(1-a));v=1-1j*r/z
        return mp.re(t/v-(1-mp.exp(-(z-1j*r)*t))/(z*v*v))/(1-a)
    return 2*(low+mp.quad(high,[0,1]))/mp.gamma(a)
rows=[]
for ax in ['.1','.5','.9']:
 a=mp.mpf(ax);A,B=constants(a)
 for tx in ['.5','2']:
  t=mp.mpf(tx)
  for xx in ['1','8','32']:
   r=mp.mpf(xx)/t;v=time_integral(a,t,r);w=laplace_integral(a,t,r)
   err=abs(v-w)/v;assert err<mp.mpf('1e-40')
   lead=A*t*r**(a-1);bound=B*r**(a-2)
   assert abs(v-lead)<=bound*(1+mp.mpf('1e-45'))
   window=r>=2*B/(A*t)
   if window:assert lead/2<=v<=3*lead/2
   rows.append(dict(a=ax,t=tx,rt=xx,time=str(v),laplace=str(w),relative_error=str(err),lead=str(lead),error_bound=str(bound),window=window))
out=dict(status='PASS finite floating consistency, not proof/enclosure',dps=60,cases=len(rows),rows=rows,max_relative_error=str(max(mp.mpf(x['relative_error'])for x in rows)),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
