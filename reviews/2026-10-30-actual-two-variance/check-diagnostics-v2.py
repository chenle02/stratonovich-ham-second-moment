#!/usr/bin/env python3
"""Falsification controls: full normalized kernel; actual raw covariance; finite algebra."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=50
br=lambda r:m.sqrt(1+r*r)
sinc=lambda r,t:t if r==0 else m.sin(r*t)/r
def S(r,t):return m.matrix([[m.cos(r*t),sinc(r,t)],[-r*m.sin(r*t),m.cos(r*t)]])
def K(r,p,t):
 b=br(r)*sinc(r,t);c=m.cos(r*t);B=br(p)*sinc(p,t);C=m.cos(p*t)
 return m.matrix([[-b*C,-b*B],[c*C,c*B]])/m.sqrt(br(r)*br(p))
def J(r):return m.diag([m.sqrt(br(r)),1/m.sqrt(br(r))])
def err(A,B):return max(abs(A[i,j]-B[i,j]) for i in range(A.rows) for j in range(A.cols))
rows=[];coupling=m.matrix([[0,0],[1,0]])
for rr in ['0','0.001','0.5','1','3','10']:
 for pp in ['0','0.01','1','4']:
  for tt in ['0','0.125','0.5','1','2']:
   r=m.mpf(rr);p=m.mpf(pp);t=m.mpf(tt)
   direct=J(r)*S(r,-t)*coupling*S(p,t)*J(p)**-1
   e=err(direct,K(r,p,t));assert e<m.mpf('1e-45')
   rows.append({'r':rr,'rho':pp,'t':tt,'max_error':m.nstr(e,10)})
# Product/conjugation/reflection Fourier constants, generic complex Gaussian carriers.
fourier=[]
for d in [1,2,3]:
 p=[m.mpf(j+1)/3 for j in range(d)];q=[-m.mpf(j+2)/5 for j in range(d)]
 for shift in ['-2','0','0.5','3']:
  lam=[m.mpf(shift)*(j+1) for j in range(d)]
  closed=2**(-m.mpf(d)/2)*m.exp(-sum((p[j]-q[j]+lam[j])**2 for j in range(d))/4)
  convolution=(2*m.pi)**(-m.mpf(d)/2)
  for j in range(d):
   pp,qq,ll=p[j],q[j],lam[j]
   convolution*=m.quad(lambda eta:m.exp(-(eta-pp)**2/2-(eta+ll-qq)**2/2),[-m.inf,(pp+qq-ll)/2,m.inf])
  assert abs(closed-convolution)<m.mpf('1e-45')
  fourier.append({'d':d,'lambda_multiplier':shift,'hat_v_conjG_at_minus_lambda':m.nstr(closed,30),'c_d_convolution':m.nstr(convolution,30)})
# Actual admissible d2 Gamma=delta_x1 tensorLeb_x2, alpha1. Spatial covariance only.
physical=[]
for dp1,dp2 in [('0','0'),('1','2'),('-3','0.5')]:
 x=m.mpf(dp1);y=m.mpf(dp2)
 direct=m.pi**m.mpf('1.5')/m.sqrt(2)*m.exp(-y*y/2)
 spec=(2*m.pi)**2/(2*m.pi)*m.quad(lambda lam1:m.mpf(1)/4*m.exp(-((lam1-x)**2+y*y)/2),[-m.inf,x,m.inf])
 assert abs(direct-spec)<m.mpf('1e-45')
 physical.append({'carrier_difference':[dp1,dp2],'physical_spatial_variance':m.nstr(direct,30),'spectral_with_2pi_squared':m.nstr(spec,30)})
# Finite Gaussian matrix algebra ONLY. The atomic frequency weights below are NOT H:homog.
xis=[-2,0,1,3];etas=[-1,0,2];n=2*len(etas);o=2*len(xis);a=m.mpf('0.5')
ncell=4;edges=[m.mpf(j)/ncell for j in range(ncell+1)];mid=[(edges[j]+edges[j+1])/2 for j in range(ncell)]
def cv(i,j):
 A,B=edges[i],edges[i+1];C,D=edges[j],edges[j+1];p=2-a
 return (abs(B-C)**p+abs(A-D)**p-abs(B-D)**p-abs(A-C)**p)/((1-a)*(2-a))
Ct=m.matrix([[cv(i,j) for j in range(ncell)] for i in range(ncell)])
assert min(m.eigsy(Ct,eigvals_only=True))>0
Ms={}
for lam in sorted(set(x-y for x in xis for y in etas)):
 mats=[]
 for t in mid:
  M=m.matrix(o,n)
  for ix,x in enumerate(xis):
   for iy,y in enumerate(etas):
    if x-y==lam:
     kk=K(abs(m.mpf(x)),abs(m.mpf(y)),t)
     for i in range(2):
      for j in range(2):M[2*ix+i,2*iy+j]=kk[i,j]
  mats.append(M)
 Ms[lam]=mats
Vout=m.matrix(o);Vin=m.matrix(n)
for lam,mats in Ms.items():
 w=m.mpf(1)/(1+lam*lam)
 for j in range(ncell):
  for k in range(ncell):
   Vout+=w*Ct[j,k]*mats[j]*mats[k].H
   Vin+=w*Ct[j,k]*mats[j].H*mats[k]
assert min(m.eigsy(Vout,eigvals_only=True))>-m.mpf('1e-45')
assert min(m.eigsy(Vin,eigvals_only=True))>-m.mpf('1e-45')
trace=lambda A:sum(A[i,i] for i in range(A.rows))
assert abs(trace(Vout)-trace(Vin))<m.mpf('1e-45')
def dft(N):return m.matrix([[m.exp(2j*m.pi*j*k/N)/m.sqrt(N) for k in range(N)] for j in range(N)])
Qin=dft(n);Qout=dft(o)
assert err(Qin.H*Qin,m.eye(n))<m.mpf('1e-45') and err(Qout.H*Qout,m.eye(o))<m.mpf('1e-45')
z=m.matrix([m.mpc(j+1,j-2) for j in range(n)]);w=m.matrix([m.mpc(1-j,j+2) for j in range(o)])
def form_variance(z,w,wrong=False):
 v=m.mpc(0)
 for lam,mats in Ms.items():
  coeff=[(w.H*M*z)[0] for M in mats]
  for j in range(ncell):
   for k in range(ncell):v+=Ct[j,k]*coeff[j]*(coeff[k] if wrong else m.conj(coeff[k]))/(1+lam*lam)
 return v
out_basis=[Qout[:,k] for k in range(o)];in_basis=[Qin[:,k] for k in range(n)]
left=sum(form_variance(e,w) for e in in_basis);right=sum(form_variance(z,e) for e in out_basis)
assert abs(left-(w.H*Vout*w)[0])<m.mpf('1e-43')
assert abs(right-(z.H*Vin*z)[0])<m.mpf('1e-43')
partial_left=sum(form_variance(e,w) for e in in_basis[:2]);partial_right=sum(form_variance(z,e) for e in out_basis[:2])
assert m.re(partial_left)<=m.re(left) and m.re(partial_right)<=m.re(right)
wrong=sum(form_variance(e,w,wrong=True) for e in in_basis)
wrong_out=sum(form_variance(z,e,wrong=True) for e in out_basis)
assert abs(wrong-left)>m.mpf('1e-3') and abs(wrong_out-right)>m.mpf('1e-3')
assert abs(m.im(partial_left))<m.mpf('1e-43') and abs(m.im(partial_right))<m.mpf('1e-43')
out={'working_precision':50,'scope':'120 full wave kernel snapshots incl zero;12 Schwartz Gaussian Fourier convolutions;3 actual singular d2 raw spatial covariance normalizations; finite Gaussian two-variance algebra with correlated time cells (atomic spatial weights NOT original H:homog and no continuum/operator bound). No certified quadrature accuracy.','kernel_snapshots':rows,'complex_Fourier_product':fourier,'actual_singular_covariance':physical,'finite_matrix_algebra':{'input_dimension':n,'output_dimension':o,'time_cells':ncell,'a':'0.5','output_trace':m.nstr(trace(Vout),30),'input_trace':m.nstr(trace(Vin),30),'input_basis_sum_fixed_output':m.nstr(left,30),'output_basis_sum_fixed_input':m.nstr(right,30),'partial_input_basis_sum':m.nstr(partial_left,30),'partial_output_basis_sum':m.nstr(partial_right,30),'missing_conjugate_negative_control_discrepancy':m.nstr(abs(wrong-left),30),'output_missing_conjugate_discrepancy':m.nstr(abs(wrong_out-right),30),'output_PSD_minimum':m.nstr(min(m.eigsy(Vout,eigvals_only=True)),30),'input_PSD_minimum':m.nstr(min(m.eigsy(Vin,eigvals_only=True)),30),'input_family_Bessel_residual':m.nstr(left-partial_left,30),'output_family_Bessel_residual':m.nstr(right-partial_right,30)}}
Path(__file__).with_name('diagnostics-v2.json').write_text(json.dumps(out,indent=2)+'\n')
print('120 kernel/12 Fourier/3 actual singular covariance controls and finite two-variance/negative-conjugation controls PASS.')
