#!/usr/bin/env python3
"""Whole-space compact-cutoff controls; auxiliary Fourier sums are not the state space."""
import mpmath as m,json,itertools
from pathlib import Path
m.mp.dps=40
br=lambda x:m.sqrt(1+x*x)
def chi(x):
 r=abs(x)
 if r<=1:return m.mpf(1)
 if r>=2:return m.mpf(0)
 A=m.exp(-1/(2-r));B=m.exp(-1/(r-1));return A/(A+B)
def psi(x):return chi(x/3)
L=m.mpf(14);carrier=m.mpf('0.7')
u=lambda x:m.exp(-x*x/2)*m.exp(1j*carrier*x)
# OrthONORMAL torus basis e_k=L^-1/2 exp(i kappa_k x).
# Ppsi coefficients are L^-1/2 int psi(x)u(x)e^-ikappa.x dx.
coeff={}
for k in range(-64,65):
 kappa=2*m.pi*k/L
 coeff[k]=m.quad(lambda x:psi(x)*u(x)*m.exp(-1j*kappa*x),[-6,-4.5,-3,0,3,4.5,6])/m.sqrt(L)
recover=[]
for N in [8,16,32,64]:
 for xx in ['0','0.5','1.5','2.5']:
  x=m.mpf(xx)
  val=chi(x)*sum(coeff[k]*m.exp(2j*m.pi*k*x/L)/m.sqrt(L) for k in range(-N,N+1))
  expected=chi(x)*u(x)
  recover.append({'N':N,'x':xx,'global_chi_u':[m.nstr(m.re(expected),22),m.nstr(m.im(expected),22)],'auxiliary_reconstruction':[m.nstr(m.re(val),22),m.nstr(m.im(val),22)],'absolute_error':m.nstr(abs(val-expected),20)})
# Exact recovery in the proposed proof uses psi=1 on suppchi, not generic Schwartz masks.
assert all(psi(m.mpf(x))==1 for x in ['-2','-1','0','1','2'])
assert max(m.mpf(r['absolute_error']) for r in recover if r['N']==64)<m.mpf('1e-5')
# Weighted Peetre controls, including negative r needed for E_(1/2).
peetre=[]
for rr in ['-1.25','-0.5','-0.25','0.5','0.75','1.25']:
 r=m.mpf(rr);maxratio=m.mpf(0)
 for xx in ['-5','-1','0','0.2','3']:
  for yy in ['-3','-0.5','0','1','7']:
   x=m.mpf(xx);y=m.mpf(yy)
   lhs=(br(x)/br(y))**r;rhs=2**(abs(r)/2)*br(x-y)**abs(r)
   assert lhs<=rhs;maxratio=max(maxratio,lhs/rhs)
 peetre.append({'r':rr,'cases':25,'maximum_lhs_over_bound':m.nstr(maxratio,22)})
# Whole-space multiplication Fourier kernel sampled on a finite grid, algebra ONLY.
nodes=[m.mpf(x) for x in ['-3','-1','0','1','2']]
cache={}
def chihat(q):
 if q not in cache:cache[q]=2*m.quad(lambda x:chi(x)*m.cos(q*x),[0,1,m.mpf('1.5'),2])/m.sqrt(2*m.pi)
 return cache[q]
def A(s):return m.matrix([[(br(x)/br(y))**s*chihat(x-y)/m.sqrt(2*m.pi) for y in nodes] for x in nodes])
def err(a,b):return max(abs(a[i,j]-b[i,j]) for i in range(a.rows) for j in range(a.cols))
a=A(m.mpf('0.5'));b=A(m.mpf('-0.5'));assert err(a.H,b)<m.mpf('1e-35')
assert err(a,a.H)>m.mpf('0.01')
n=len(nodes);P=m.matrix(2*n);U=m.matrix(2*n)
for i in range(n):
 for j in range(n):P[i,j]=a[i,j];P[n+i,n+j]=b[i,j]
 U[i,n+i]=1;U[n+i,i]=1
D=m.diag([br(x)**m.mpf('-0.25') for x in nodes]*2)
Kout=P*D;Kin=P.H*D
assert err(P.H,U*P*U)<m.mpf('1e-35')
assert err(Kin,U*Kout*U)<m.mpf('1e-35')
# Both positive compact covariance envelopes have correct adjoints.
assert err(Kout*Kout.H,P*(D*D)*P.H)<m.mpf('1e-35')
assert err(Kin*Kin.H,P.H*(D*D)*P)<m.mpf('1e-35')
eout=m.eigsy(Kout*Kout.H,eigvals_only=True);ein=m.eigsy(Kin*Kin.H,eigvals_only=True)
assert max(abs(eout[i]-ein[i]) for i in range(2*n))<m.mpf('1e-35')
# Finite lattice diagonal checks concern ONLY the auxiliary embedding.
lattice=[]
for d in [1,2,3]:
 gamma=m.mpf('0.25')
 vals=sorted([(1+(2*m.pi/L)**2*sum(k*k for k in ks))**(-gamma/2) for ks in itertools.product(range(-8,9),repeat=d)],reverse=True)
 C=max(3**gamma,(2*L/m.pi)**gamma)
 for j in [1,2,10,27,100]:
  if j<=len(vals):
   assert vals[j-1]<=C*m.mpf(j)**(-gamma/d)
   lattice.append({'d':d,'gamma':'0.25','j':j,'finite_diagonal_value':m.nstr(vals[j-1],22),'proposed_uniform_upper':m.nstr(C*m.mpf(j)**(-gamma/d),22)})
# A missing physical cutoff is a real failure: Lambda^-gamma alone is noncompact.
# At gamma1/2, Gaussian input translates have norm^2 int exp(-xi²)/<xi> dxi.
# Their image cross-inner-products decay; evaluated here as a control, not proof of RL.
gamma=m.mpf('0.5');density=lambda x:m.exp(-x*x)*(1+x*x)**(-gamma)
norm=m.quad(density,[-m.inf,0,m.inf]);translations=[]
for gap in [4,8,16]:
 cross=2*m.quad(lambda x:density(x)*m.cos(gap*x),[0,1,2,4,8,m.inf])
 translations.append({'gap':gap,'image_squared_norm':m.nstr(norm,22),'cross_inner_product':m.nstr(cross,22),'squared_distance':m.nstr(2*norm-2*cross,22)})
 assert 2*norm-2*cross>norm
out={'working_precision':40,'scope':'16 actual compact-cutoff auxiliary Fourier recoveries,150Peetre finite controls, finite sampled full-space Fourier adjoint algebra,13 auxiliary diagonal checks,3 uncut translation controls. NO continuum singular-value/PDE/operator theorem from finite grids, no certified quadrature accuracy.','cutoffs':{'chi':'C_infinity compact plateau1 on[-1,1],0 off[-2,2]','psi':'chi(x/3),1 on[-3,3],0 off[-6,6]','L':'14, supports strictly interiorQ; psi1 onneighborhood ofsuppchi'},'recoveries':recover,'Peetre_controls':peetre,'finite_adjoint_algebra':{'frequency_nodes':[str(x) for x in nodes],'Ahalf_adjoint_minus_half_error':m.nstr(err(a.H,b),20),'nonselfadjoint_discrepancy':m.nstr(err(a,a.H),20),'swap_identity_error':m.nstr(err(P.H,U*P*U),20),'both_envelope_eigenvalues_error':m.nstr(max(abs(eout[i]-ein[i]) for i in range(2*n)),20)},'auxiliary_diagonal':lattice,'missing_cutoff_translation_control':translations}
Path(__file__).with_name('diagnostics-v2.json').write_text(json.dumps(out,indent=2)+'\n')
print('Compact-cutoff Fourier recovery,negative-index Peetre,adjoint/swap/two-envelopes and uncut noncompactness controls PASS.')
