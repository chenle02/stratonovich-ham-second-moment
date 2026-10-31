from pathlib import Path
import itertools,json,hashlib,math
import numpy as np
import mpmath as mp
from scipy.optimize import differential_evolution,minimize
P=Path(__file__).resolve().parent
assert hashlib.sha256((P/'target-v0.md').read_bytes()).hexdigest()==json.loads((P/'target-freeze-v0.json').read_text())['sha256']
cases=[
 ('zero', [['0']],['1'],['0']),
 ('zero_heavy',[['0']],['1'],['3']),
 ('scalar',[['1']],['1'],['0']),
 ('scalar_heavy',[['1']],['.1'],['4']),
 ('orthogonal',[['1','0'],['0','1']],['1','1'],['0','0']),
 ('overlap',[['1','0'],['.5','sqrt3over2']],['1','1'],['0','0']),
 ('parallel',[['1'],['1']],['1','2'],['0','0']),
 ('parallel_heavy',[['1'],['1']],['1','.5'],['0','20']),
 ('zero_redundant',[['1','0'],['0','1'],['0','0']],['1','1','2'],['0','0','0']),
 ('three_mixed',[['1','0'],['0','1'],['1','1']],['1','2','.5'],['0','.5','1']),
 ('near_parallel',[['1','0'],['1','.001']],['1','1'],['.5','1']),
 ('small_norm',[['.1','0'],['0','.1']],['1','1'],['.25','.25'])]
def num(x):return mp.sqrt(3)/2 if x=='sqrt3over2' else mp.mpf(x)
def dual(K0,l0,b0,dps):
 with mp.workdps(dps):
  K=mp.matrix([[num(x) for x in row] for row in K0]);ell=list(map(mp.mpf,l0));b=list(map(mp.mpf,b0));C=K*K.T
  keep=[i for i in range(len(ell)) if C[i,i]>0];branches=[]
  best=mp.mpf(0);bestphi=mp.matrix(K.cols,1);bestactive=[];maxgrad=mp.mpf(0)
  for count in range(1,len(keep)+1):
   for A in itertools.combinations(keep,count):
    CA=mp.matrix([[C[i,j] for j in A] for i in A]);la=mp.matrix([ell[i] for i in A]);ba=mp.matrix([b[i] for i in A]);n=len(A)
    w=mp.matrix([max(mp.mpf(1),(la[i]**2/CA[i,i])**(mp.mpf(1)/3),ba[i]/CA[i,i]+1) for i in range(n)])
    D=lambda z:sum(la[i]**2/z[i]-ba[i]*z[i] for i in range(n))+(z.T*CA*z)[0]/2
    for it in range(150):
     g=CA*w-ba-mp.matrix([la[i]**2/w[i]**2 for i in range(n)])
     if max(abs(x) for x in g)<mp.mpf(10)**(-(dps-15)):break
     H=mp.matrix(CA)
     for i in range(n):H[i,i]+=2*la[i]**2/w[i]**3
     step=-mp.lu_solve(H,g);alpha=mp.mpf(1)
     for i in range(n):
      if step[i]<0:alpha=min(alpha,-mp.mpf('.9')*w[i]/step[i])
     slope=(g.T*step)[0];old=D(w)
     for bt in range(120):
      nw=w+alpha*step
      if min(nw)>0 and D(nw)<=old+mp.mpf('.0001')*alpha*slope+mp.mpf(10)**(-dps+5)*max(1,abs(old)):break
      alpha/=2
     else:raise RuntimeError('line search')
     w=nw
    else:raise RuntimeError('Newton iterations')
    g=CA*w-ba-mp.matrix([la[i]**2/w[i]**2 for i in range(n)]);grad=max(abs(x) for x in g);maxgrad=max(maxgrad,grad)
    val=D(w);phi=mp.matrix([sum(w[j]*K[A[j],h] for j in range(n)) for h in range(K.cols)])
    branches.append({'A':list(A),'value':mp.nstr(val,30),'weights':[mp.nstr(x,30) for x in w],'gradient_max':mp.nstr(grad,14)})
    if val>best:best=val;bestphi=phi;bestactive=list(A)
  primal=2*sum(ell[i]*mp.sqrt(max(mp.mpf(0),sum(K[i,h]*bestphi[h] for h in range(K.cols))-b[i])) for i in range(K.rows))-(bestphi.T*bestphi)[0]/2
  full=next((x['value'] for x in branches if len(x['A'])==len(keep)),'0')
  return {'score':+best,'candidate_primal':+primal,'max_gradient':+maxgrad,'phi':[mp.nstr(x,30) for x in bestphi],'active':bestactive,'branches':branches,'full_active_only':full,'discarded_zero':len(ell)-len(keep)}
rows=[];fullwrong=[];precisionmax=mp.mpf(0);maxcase=None
for label,K0,l0,b0 in cases:
 lo=dual(K0,l0,b0,50);hi=dual(K0,l0,b0,80)
 with mp.workdps(80):
  pdiff=abs(lo['score']-hi['score']);cdiff=abs(hi['candidate_primal']-hi['score'])
  if pdiff>precisionmax:precisionmax=pdiff;maxcase=label
  assert cdiff<mp.mpf('1e-55')
  if abs(mp.mpf(hi['full_active_only'])-hi['score'])>mp.mpf('1e-6'):fullwrong.append(label)
 K=np.array([[math.sqrt(3)/2 if x=='sqrt3over2' else float(x) for x in row] for row in K0]);ell=np.array(l0,float);b=np.array(b0,float)
 radius=(4*sum(ell*np.sqrt(np.linalg.norm(K,axis=1))))**(2/3)+1
 objective=lambda phi:float(2*np.dot(ell,np.sqrt(np.maximum(K@phi-b,0)))-np.dot(phi,phi)/2)
 samples=[(0.0,np.zeros(K.shape[1]))]
 for seed in [7,29]:
  opt=differential_evolution(lambda x:-objective(x),[(-radius,radius)]*K.shape[1],seed=seed,popsize=20,maxiter=500,tol=1e-10,polish=False,workers=1)
  pol=minimize(lambda x:-objective(x),opt.x,method='Powell',bounds=[(-radius,radius)]*K.shape[1],options={'xtol':1e-11,'ftol':1e-11,'maxiter':1000})
  for q in [opt,pol]:samples.append((objective(q.x),q.x))
 value,phi=max(samples,key=lambda x:x[0]);gap=float(hi['score'])-value
 assert gap>=-1e-6
 rows.append({'case':label,'K':K0,'ell':l0,'b':b0,'dual_score_50':mp.nstr(lo['score'],30),'dual_score_80':mp.nstr(hi['score'],30),'unrounded_precision_diff':mp.nstr(pdiff,14),'gradient50':mp.nstr(lo['max_gradient'],14),'gradient80':mp.nstr(hi['max_gradient'],14),'positive_candidate_primal_gap80':mp.nstr(cdiff,14),'dual_positive_phi':hi['phi'],'best_active':hi['active'],'branches80':hi['branches'],'discarded_zero_labels':hi['discarded_zero'],'full_active_only':hi['full_active_only'],'direct_primal_float64':value,'direct_phi':phi.tolist(),'coercive_search_radius':radius,'dual_minus_heuristic_primal':gap,'scope':'direct global search is heuristic lower evidence,not certified global optimum; candidate equality is calibration only'})
ort=next(float(x['dual_score_80']) for x in rows if x['case']=='orthogonal');ov=next(float(x['dual_score_80']) for x in rows if x['case']=='overlap');assert ov>ort
out={'scope':'UNREVIEWED PG1-PG2 finite screen only; no proof/UR premise/physical application','rows':rows,'cases':len(rows),'seeds':[7,29],'precision':[50,80],'percase_residuals_retained':True,'max_score_precision_diff':mp.nstr(precisionmax,14),'max_case':maxcase,'wrong_full_active_formula_failures':fullwrong,'wrong_halfaction_scalar':{'correct_score':'3/2','wrong_cost_norm_squared_score':'3/2^(4/3)','scope':'explicit scalar comparison,not a model theorem'},'gram_comparison':{'C':[[1,0],[0,1]],'D':[[1,.5],[.5,1]],'D_minus_C_eigenvalues':[-.5,.5],'C_score':ort,'D_score':ov,'scope':'entrywise increase without Loewner increase; finite comparator only'},'formal_or_analytic_proof':False}
s=json.dumps(out,indent=2)+'\n';(P/'finite-score-screen-v0.json').write_text(s)
print(json.dumps({'cases':len(rows),'max_precision_diff':out['max_score_precision_diff'],'max_case':maxcase,'wrong_full_active':fullwrong,'max_heuristic_gap':max(x['dual_minus_heuristic_primal'] for x in rows),'gram_scores':[ort,ov]}))
