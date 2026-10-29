"""Positive white trace checks with explicit analytical truncation budgets.

Floating quadratures are not certified enclosures. This measures the
critical white trace core, not the full localized operator norm.
"""
from pathlib import Path
import json,hashlib
import mpmath as mp
mp.mp.dps=60
Y=mp.mpf(160)

def D(q):
    return 2*mp.ellipk(-q*q/4)

def D_positive(q):
    nodes=sorted(set([mp.mpf(0),mp.mpf(1),q]))+[mp.inf]
    tail=mp.quad(lambda x:1/(mp.sqrt(1+x*x)*mp.sqrt(1+(x+q)**2)),nodes)
    middle=mp.quad(lambda x:1/(mp.sqrt(1+x*x)*mp.sqrt(1+(q-x)**2)),[0,q/2]) if q else 0
    return 2*(tail+middle)

def white_time(a,h):
    beta=1/(1-a);c=mp.mpf('2.5')+mp.log(1/h)
    value=8*h**(2-a)/(1-a)*mp.quad(lambda y:-mp.expm1(-beta*y)*mp.besselk(0,h*mp.exp(-beta*y))**2*mp.exp(-y),[0,1,4,16,64,Y])
    tail=8*h**(2-a)/(1-a)*mp.exp(-Y)*((c+beta*Y)**2+2*beta*(c+beta*Y)+2*beta**2)
    return value,tail

def J1(a,r):
    if not r:return 2/((1-a)*(2-a))
    z=-1j*abs(r)
    return 2*mp.re(z**(a-1)*mp.gammainc(1-a,0,z)-z**(a-2)*mp.gammainc(2-a,0,z))

def spectral_window(a,h,Q=mp.mpf(32)):
    A=mp.pi/(mp.gamma(a)*mp.cos(mp.pi*a/2));B=2*mp.pi/(mp.gamma(a)*mp.sin(mp.pi*a/2));beta=1/(1-a)
    nodes=sorted(set([mp.mpf(0),h,mp.mpf(1)]+[k*mp.pi for k in range(1,11)if k*mp.pi<Q]+[Q]))
    core=mp.quad(lambda z:D(z/h)*J1(a,z),nodes)
    lead=beta*Q**(a-1)*mp.quad(lambda y:(Q*mp.exp(beta*y))*D(Q*mp.exp(beta*y)/h)*mp.exp(-y),[0,1,4,16,64,Y])
    error=beta*Q**(a-1)*mp.quad(lambda y:D(Q*mp.exp(beta*y)/h)*mp.exp(-y),[0,1,4,16,64,Y])
    lead_tail=24*beta*Q**(a-1)*h*mp.exp(-Y)*(mp.log(2+Q/h)+beta*(Y+1))
    error_tail=lead_tail/Q
    pref=2*h**(1-a)
    center=pref*(core+A*lead)
    budget=pref*(B*(error+error_tail)+A*lead_tail)
    return center,budget

conv=[]
for qx in ['0','.5','2','8','32','128']:
 q=mp.mpf(qx);v=D(q);w=D_positive(q);err=abs(v-w)/v
 assert err<mp.mpf('1e-45')
 assert v<=24*mp.log(2+q)/mp.sqrt(1+q*q)
 conv.append(dict(q=qx,elliptic=str(v),positive_quad=str(w),relative_error=str(err)))
rows=[]
for ax in ['.1','.5','.9']:
 a=mp.mpf(ax)
 for power in [0,4,8,16]:
  h=mp.mpf(2)**(-power);v,tail=white_time(a,h)
  assert v>0 and tail/v<mp.mpf('1e-40')
  ratio=v/(h**(2-a)*(1+abs(mp.log(h)))**2)
  rows.append(dict(a=ax,h=str(h),positive_time_quad=str(v),analytic_y_tail_budget=str(tail),normalized_upper_budget_ratio=str(ratio)))
validation=[]
for ax,hx in [('.1','.25'),('.5','.25'),('.5','.0625'),('.9','.25'),('.9','.0625')]:
 a,h=mp.mpf(ax),mp.mpf(hx);v,tail=white_time(a,h);center,budget=spectral_window(a,h)
 assert abs(v-center)<=budget+tail+mp.mpf('1e-35')*max(v,1)
 validation.append(dict(a=ax,h=hx,time=str(v),spectral_center=str(center),analytic_spectral_tail_budget=str(budget),difference=str(abs(v-center)),relative_budget=str(budget/v)))
out=dict(status='PASS finite floating consistency with analytical tail budgets, not a computer-certified enclosure',mpmath_version=mp.__version__,dps=60,positive_convolution_cases=len(conv),white_trace_cases=len(rows),spectral_time_validation_cases=len(validation),convolution=conv,white_trace=rows,validation=validation,quadrature_y_endpoint=str(Y),scope='Actual critical white spectral trace core; not a full spatial operator-norm or SPDE-flow measurement',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ['convolution','white_trace','validation']},indent=2))
