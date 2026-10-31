#!/usr/bin/env python3
"""Actual normalized raw-test source correlations and finite convex-moment control."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=45
p=Path(__file__).parent
base=json.loads((p/'diagnostics-v1.json').read_text())
r=next(x for x in base['test_variance_controls'] if x['a']=='.5' and x['T']=='1' and x['epsilon']=='.5')
e=m.mpf(r['epsilon']);rawtime=m.mpf(r['raw_variance'])/m.sqrt(m.pi)
cuttime=m.mpf(r['source_variance'])/m.sqrt(m.pi/(1+e));k=cuttime/rawtime
v1=k/(1+e)**m.mpf('.5');v2=k/(1+e)**m.mpf('1.5')
assert 0<v2<v1<1
U=m.matrix([[1,1],[1,-1]])/m.sqrt(2)
C=U*m.diag([v1,v2])*U.T
root=U*m.diag([m.sqrt(v1),m.sqrt(v2)])*U.T
assert abs(C[0,1])>m.mpf('.001')
assert max(abs((root*root-C)[i,j]) for i in range(2) for j in range(2))<m.mpf('1e-35')
A=[m.matrix([[1,1],[0,0]]),m.matrix([[0,1],[1,1]])]
nodes=[-m.sqrt(3),m.mpf(0),m.sqrt(3)];weights=[m.mpf(1)/6,m.mpf(2)/3,m.mpf(1)/6]
# Three-node rule matches all standard Gaussian moments throughdegree4 exactly in exact arithmetic.
assert abs(sum(w*x*x for w,x in zip(weights,nodes))-1)<m.mpf('1e-40')
assert abs(sum(w*x**4 for w,x in zip(weights,nodes))-3)<m.mpf('1e-40')
def moment(R):
 v=m.mpf(0)
 for i,x in enumerate(nodes):
  for j,y in enumerate(nodes):
   c=R*m.matrix([x,y]);X=c[0]*A[0]+c[1]*A[1];G=X.T*X
   v+=weights[i]*weights[j]*sum((G*G)[q,q] for q in range(2))
 return v
raw=moment(m.eye(2));source=moment(root)
wrong=moment(m.diag([m.sqrt(C[0,0]),m.sqrt(C[1,1])]))
assert source<=raw and abs(source-wrong)>m.mpf('1e-6')
coupled=[]
for row in base['test_variance_controls']:
 ee=m.mpf(row['epsilon']);ct=m.mpf(row['source_variance'])/m.sqrt(m.pi/(1+ee))
 cov=ct*(m.sqrt(m.pi/(1+ee/2))-m.sqrt(m.pi/(1+ee)))
 assert cov>0
 coupled.append({'a':row['a'],'T':row['T'],'epsilon':row['epsilon'],'delta':row['delta'],'Cov_source_residual':m.nstr(cov,25)})
out={'source_and_residual_are_not_independent_with_heat':coupled,'working_precision':45,'scope':'Actual raw-completion two-test white1d source-covariance restriction; rotated source evaluations correlated. Finite2x2 matrix S4^4 convex comparison only, not an actual driver/timepath calculation or certifiedaccuracy.','raw_test_basis':'same normalizedtime1_[0,1]; spatialnormalized Gaussian and normalized xGaussian, then45degree realrotation. RawGramI; indicator/Schwartztests inrawcompletion, notliteralCcsmoothONbasis.','epsilon':str(e),'delta':r['delta'],'time_cut_over_raw':m.nstr(k,25),'source_covariance':[[m.nstr(C[i,j],25) for j in range(2)] for i in range(2)],'eigenvalues':[m.nstr(v1,25),m.nstr(v2,25)],'finite_S4_fourth_moments':{'raw_independent_coordinates':m.nstr(raw,25),'correct_correlated_source_coordinates':m.nstr(source,25),'incorrect_independence_same_source_variances':m.nstr(wrong,25),'incorrect_independence_discrepancy':m.nstr(abs(source-wrong),25)},'comparison_assertion':'correct source moment <= raw moment; no assumption source evaluations independent'}
(p/'correlated-diagnostics-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('Actual two-test correlated source-covariance and finite S4 comparison/missing-correlation control PASS.')
