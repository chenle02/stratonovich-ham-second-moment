"""Necessary CM controls, not full operator norms or compactness certificates."""
from pathlib import Path
import json,math
import numpy as np

def bump(x):
 x=np.asarray(x);v=np.zeros_like(x,dtype=float);ok=np.abs(x)<1;v[ok]=np.exp(-1/(1-x[ok]**2));return v

def gl(n,lo=0.,hi=1.):
 x,w=np.polynomial.legendre.leggauss(n);return lo+(hi-lo)*(x+1)/2,(hi-lo)*w/2

def chi(x):
 x=np.asarray(x);v=np.ones_like(x,dtype=float);v[x>=2]=0;ok=(x>1)&(x<2);z=x[ok];a=np.exp(-1/(2-z));b=np.exp(-1/(z-1));v[ok]=a/(a+b);return v

# White-noise coordinate on the ACTUAL F phase: output dual w2=Lambda f.
x,w=gl(512,-.5,.5);norm=math.sqrt(np.dot(w,bump(2*x)**2))
def q(x):return bump(2*x)/norm

def corr(v,degree):
 x,w=gl(degree,-.5,.5);v=np.asarray(v);return ((q(x[:,None]+v[None,:])+q(x[:,None]-v[None,:]))*q(x[:,None])*w[:,None]/2).sum(axis=0)

rows=[]
for a in [.5,.9]:
 M=math.gamma((1+a)/2)/(math.gamma(1+a)*math.gamma((1-a)/2))
 for delta in [.25,.125,.3]:
  N=math.floor(1/delta);last=1/delta-N
  for label,m,ell in [('first',0,1.),('last',N,last)]:
   sm=m*delta
   slow,ws=gl(128,sm,sm+delta*ell);v=(slow-sm)/delta
   fast,wf=gl(192,0,ell)
   for column in [0,1]:
    direct=delta**(-.5)/math.sqrt(M)*np.dot(ws,(v**column)*corr(v,256))
    target=math.sqrt(delta)/math.sqrt(M)*np.dot(wf,(fast**column)*corr(fast,384))
    assert abs(direct-target)<2e-7*(1+abs(target))
    wrongclock=delta**(-.5)/math.sqrt(M)*np.dot(ws,(v**column)*corr(slow-sm,256))
    rows.append({'a':a,'delta':delta,'block':label,'fast_horizon':ell,'constant_column':column,
      'actual_slow_covariance_entry':float(direct),'fast_mean_entry':float(target),
      'wrong_Jacobian_entry':float(delta*direct),'wrong_slow_clock_entry':float(wrongclock),
      'wrong_slow_velocity_column':float(delta*direct) if column==1 else None})
assert max(abs(z['actual_slow_covariance_entry']-z['wrong_slow_clock_entry']) for z in rows)>.01
# Whole-space H1/2 norms of Gaussian modulations, no periodic proxy.
def hhalf(k,degree):
 xi,w=gl(degree,-k-12,k+12);h=(np.exp(-(xi-k)**2/2)+np.exp(-(xi+k)**2/2))/(2*math.pi**.25)
 return math.sqrt(np.dot(w,np.sqrt(1+xi*xi)*h*h))
frequency=[]
for k in [0,2,8,32,64]:
 x,w=gl(768,-2,2);g=np.exp(-x*x/2)/math.pi**.25;f=g*np.cos(k*x);mask=chi(np.abs(x))**2
 productnorm=math.sqrt(np.dot(w,(mask*f*g)**2))
 h512,h1024=hhalf(k,512),hhalf(k,1024)
 frequency.append({'k':k,'noise_direction_norm_Hsp':1,'matrix_entry_lower_for_Tsp_norm':productnorm/(h1024*hhalf(0,1024)),
                   'Hhalf_degree512':h512,'Hhalf_degree1024':h1024})
assert frequency[-1]['matrix_entry_lower_for_Tsp_norm']<frequency[1]['matrix_entry_lower_for_Tsp_norm']
spatial=[]
for name,d,alpha in [('white',1,1.),('invariant',2,1.),('riesz',2,1.5)]:
 A=1/math.sqrt(2*math.pi) if name!='riesz' else 2**(-alpha/2)*math.gamma((d-alpha)/2)/math.gamma(d/2)
 for s in [alpha/4-.05,alpha/4+.05,.5]:
  for L in [2,8,32,128]:
   spatial.append({'model':name,'d':d,'alpha':alpha,'state_s':s,'L':L,'actual_Gaussian_product_Hsp_norm':math.sqrt(A)*L**(alpha/2-2*s),
    'scope':'f_L=L^(d/2-s)g(Lx); whole-space H^s norm uniformly bounded by Fourier scaling. Gaussian H1 profiles, not compact noise/state cutoffs.'})
# Temporal compactness guard: unit H_t spike f_delta, first-block norm ratio.
spikes=[];trace=[]
for a in [.25,.5,.9]:
 critical=2/a
 for r in [(2+critical)/2,critical,critical+.5]:
  for delta in [.25,1/16,1/64,1/256]:
   spikes.append({'a':a,'r':r,'delta':delta,'first_block_Lr_norm_relative_to_fixed_nonzero_base':delta**(1/r-a/2),
                  'scope':'Exact raw-H isometry/mean scaling of smooth time spike, not full Lr norm upper estimate.'})
 for N in [4,8,32,128]:
  trace.append({'a':a,'N':N,'partial_covariance_trace_lower':2*N**a/((1-a)*(2-a)),
                'scope':'Orthonormal normalized time-cell tests; K has infinite trace, not a Radon L2 Gaussian covariance. This says nothing against compactness.'})
data={'status':'PRE-PROOF NECESSARY CONTROLS ONLY','matrix_covariance':rows,'spatial_frequency':frequency,'spatial_scaling':spatial,'time_spikes':spikes,'time_trace':trace,
      'limits':'ordinary floating quadrature/algebra, no rigorous error enclosure; actual F rows include both constant columns via white noise and accepted equilibrium time test, not a point Sobolev trace. No full operator norm, Ctheta norm, projection tail, vector compactness or SPDE upper computed.'}
Path(__file__).with_name('operator-cm-controls-v1.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'actual_F_covariance_rows':len(rows),'frequency_rows':len(frequency),'spatial_scalings':len(spatial),'time_spikes':len(spikes),'trace_controls':len(trace),'status':data['status']}))
