"""Actual d1 white spatial rows; floating quadrature, no operator certificate."""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
sigma=.25; beta=.125
Ks=[1.,4.,8.,16.]; epss=[.25,.0625,.015625,.00390625]
ns=[]
for prec in [35,65]:
 mp.mp.dps=prec
 sig=mp.mpf(1)/4
 ns.append(mp.quad(lambda y:2*sig**2*mp.sqrt(1+y*y)*mp.exp(-sig**2*y*y),[0,1,4,16,mp.inf]))
state_n2=float(ns[-1])
def eta(x,R):
 t=np.abs(x)/R-1
 y=np.ones_like(x);y[t>=1]=0
 mid=(t>0)&(t<1)
 v=t[mid];a=np.exp(-1/v);b=np.exp(-1/(1-v));y[mid]=b/(a+b)
 return y

def evaluate(R,b,level,masked=True):
 L=(16 if level==0 else 32)*R
 N=int((4096 if level==0 else 16384)*R)
 dx=L/N;x=(np.arange(N)-N/2)*dx
 f2=np.exp(-(x-b)**2/sigma**2)/state_n2
 k=f2*(eta(x,R)**2 if masked else 1)
 kh=dx/np.sqrt(2*np.pi)*np.fft.fft(k)
 xi=2*np.pi*np.fft.fftfreq(N,d=dx);dq=2*np.pi/L;power=np.abs(kh)**2
 total=float(power.sum()*dq)
 physical=float(np.sum(k*k)*dx)
 tails={}
 for K in Ks:
  # Partial frequency boundary cells approximate the whole-space integral.
  overlap=np.maximum(0,np.minimum(xi+dq/2,K)-np.maximum(xi-dq/2,-K))
  outside=1-overlap/dq
  tails[str(K)]=float(np.sqrt(np.maximum(0,np.sum(power*outside)*dq)))
 heats={str(e):float(np.sqrt(np.sum(power*(-np.expm1(-e*xi*xi/2))**2)*dq)) for e in epss}
 return {'R':R,'center':b,'level':level,'physical_mask':masked,'N':N,'dx':dx,'frequency_step':dq,'nyquist':np.pi/dx,'row_Hsp_norm':total**.5,'Parseval_squared_defect':abs(total-physical),'frequency_tail_norms':tails,'heat_residual_norms':heats,'scaled_frequency_ratios':{str(K):K**beta*tails[str(K)] for K in Ks},'scaled_heat_ratios':{str(e):heats[str(e)]/e**(beta/2) for e in epss}}
rows=[]
for R in [1,2,4,8]:
 for b in [0.,float(R),1.5*R]:
  rows.extend(evaluate(R,b,l) for l in [0,1])
cal=[]
for l in [0,1]:
 q=evaluate(1,0,l,False)
 exactnorm2=sigma*np.sqrt(np.pi/2)/state_n2**2
 q['exact_row_norm']=exactnorm2**.5
 q['relative_row_norm_error']=abs(q['row_Hsp_norm']/q['exact_row_norm']-1)
 q['frequency_tail_relative_errors']={str(K):abs(q['frequency_tail_norms'][str(K)]/float(mp.sqrt(mp.mpf(str(exactnorm2))*mp.erfc(mp.mpf(str(sigma*K))/mp.sqrt(2))))-1) for K in Ks}
 exactheat={str(e):float(mp.sqrt(mp.mpf(str(sigma))**2*mp.sqrt(2*mp.pi)/2*(1/mp.mpf(str(sigma))-2/mp.sqrt(mp.mpf(str(sigma*sigma+e)))+1/mp.sqrt(mp.mpf(str(sigma*sigma+2*e))))/mp.mpf(str(state_n2))**2)) for e in epss}
 q['heat_residual_relative_errors']={str(e):abs(q['heat_residual_norms'][str(e)]/exactheat[str(e)]-1) for e in epss}
 cal.append(q)
assert all(np.isfinite(x['row_Hsp_norm']) and x['row_Hsp_norm']>=0 for x in rows)
assert max(x['relative_row_norm_error'] for x in cal)<1e-12
assert max(max(x['heat_residual_relative_errors'].values()) for x in cal)<1e-10
pairs=[]
for lo,hi in zip(rows[::2],rows[1::2]):
 pairs.append({'R':lo['R'],'center':lo['center'],'row_norm_absolute_change':abs(lo['row_Hsp_norm']-hi['row_Hsp_norm']),'max_frequency_tail_absolute_change':max(abs(lo['frequency_tail_norms'][str(K)]-hi['frequency_tail_norms'][str(K)]) for K in Ks),'max_heat_residual_absolute_change':max(abs(lo['heat_residual_norms'][str(e)]-hi['heat_residual_norms'][str(e)]) for e in epss)})
out={'scope':'actual d1 white spatial covariance Gamma=delta0, alpha1, a may be1/4; s3/8,beta1/8; real Gaussian states normalized in WHOLE-SPACE H1/2; physical eta_R^2 row after masking; only a tested family, not operator supremum/allGamma proof','state_Hhalf_norm_squared_35digits':mp.nstr(ns[0],32),'state_Hhalf_norm_squared_65digits':mp.nstr(ns[1],62),'state_quadrature_difference':mp.nstr(abs(ns[0]-ns[1]),12),'rows':rows,'resolution_pairs':pairs,'unmasked_exact_Gaussian_calibrations':cal,'limitations':['No certified enclosure; mp digits/resolution agreement not error proof.','Finite spatial/frequency grids and Nyquist truncation; unobserved masked tails not rigorously enclosed.','Frequency boundary cells partially weighted to approximate integral; no periodic STATE or raw covariance replacement.','d1 white only and selected Gaussian states; no bound on operator supremum or other original covariances.','No stochastic first driver, CM probability or growingR exponential estimate measured.'],'versions':{'numpy':np.__version__,'mpmath':mp.__version__}}
Path(__file__).with_name('white-row-controls-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'rows':len(rows),'resolution_pairs':len(pairs),'max_free_tail_relative_error_by_level':[max(x['frequency_tail_relative_errors'].values()) for x in cal],'max_masked_tail_absolute_resolution_change':max(x['max_frequency_tail_absolute_change'] for x in pairs),'max_scaled_freq_ratio':max(max(x['scaled_frequency_ratios'].values()) for x in rows),'max_scaled_heat_ratio':max(max(x['scaled_heat_ratios'].values()) for x in rows),'scope':'floating actual white row diagnostics only'},indent=2))
