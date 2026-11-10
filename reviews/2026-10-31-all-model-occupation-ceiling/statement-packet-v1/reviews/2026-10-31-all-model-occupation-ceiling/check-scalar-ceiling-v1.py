"""NEW alpha>1 scalar calibration; C_occ values below are synthetic inputs."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

P=Path(__file__).resolve().parent
CASES=[('d2_5over4','5/4','1/2',2,'3','2'),
       ('d3_7over4','7/4','1/8',3,'2','1'),
       ('d3_3over2','3/2','1/3',3,'5','3'),
       ('d2_9over5','9/5','1/10',2,'4','2')]


def number(s):
    v=Fraction(s)
    return mp.mpf(v.numerator)/v.denominator


def run(dps):
    with mp.workdps(dps):
        rows=[]
        for name,als,ats,dim,cs,ps in CASES:
            alpha,a,C,c=map(number,[als,ats,cs,ps])
            assert 1<alpha<dim and 0<a<1 and alpha+a<2
            q,k=4-alpha,3-alpha; beta=alpha/4
            delta=(q*mp.log(q)+(q-2*a)*mp.log(q-2*a))/2-(q-a)*mp.log(q-a)
            D=mp.sqrt(q/4)*(alpha/4)**(alpha/(2*q))*C**(1/q)
            v=(2*c*D/q)**(q/k)
            T=(beta*mp.sqrt(v*C))**(1/(1-beta))
            def score(t,w,cost=mp.mpf(1)/2):
                return c*mp.sqrt(mp.sqrt(w*C)*t**beta-t)-cost*w
            direct=score(T,v)
            gradT=abs(mp.diff(lambda t:score(t,v),T))
            gradV=abs(mp.diff(lambda w:score(T,w),v))
            for eta in [mp.mpf(1)/2,mp.mpf(1),mp.mpf(3)/2]:
                E=(2-alpha)/2*(alpha/(2*eta))**(alpha/(2-alpha))*C**(2/(2-alpha))
                def F(b):
                    return k*((q-2*b)**((q-2*b)/2)/(8*(q-b)**(q-b))
                              *(2*E/(2-alpha))**((2-alpha)/2))**(1/k)
                U=c**(q/k)*(2*eta)**(alpha/(2*k))*F(0)
                ratioLog=mp.log(c**(q/k)*F(a)/U)
                expectedLog=(delta-alpha/2*mp.log(2*eta))/k
                wrong_v=(c*D/q)**(q/k)
                wrong_full_cost=k*wrong_v
                rows.append(dict(case=name,dimension_label=dim,alpha=alpha,a=a,
                                 synthetic_Cocc=C,auxiliary_c=c,eta=eta,E_eta=E,
                                 T_star=T,v_star=v,direct_scalar_score=direct,closed_U=U,
                                 coefficient_residual=abs(direct-U),gradT=gradT,gradV=gradV,
                                 source_ratio_log=ratioLog,source_ratio_residual=abs(ratioLog-expectedLog),
                                 wrong_omit_2eta_gap=abs(U-c**(q/k)*F(0)),
                                 wrong_full_cost_gap=U-wrong_full_cost,
                                 eta1_shortcut_sign=delta-alpha/2*mp.log(2)))
        fields=['coefficient_residual','gradT','gradV','source_ratio_residual']
        maxima={f:dict(value=max(r[f] for r in rows),cases=[dict(case=r['case'],eta=r['eta']) for r in rows if r[f]==max(x[f] for x in rows)]) for f in fields}
        assert all(m['value']<mp.mpf(10)**(-dps+8) for m in maxima.values())
        assert all(r['wrong_full_cost_gap']>0 for r in rows)
        def encode(v):
            if isinstance(v,mp.mpf):return mp.nstr(v,dps+9)
            if isinstance(v,dict):return {k:encode(x) for k,x in v.items()}
            if isinstance(v,list):return [encode(x) for x in v]
            return v
        return encode(dict(dps=dps,rows=rows,maxima=maxima))


lhs=11**11*7**7
base=9**18
rhs=2**5*base
assert base<lhs<rhs
data=dict(schema='all-model-scalar-ceiling-calibration/1',
          source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          mpmath_version=mp.__version__,runs=[run(50),run(80)],
          exact_eta1_shortcut_counterexample=dict(alpha='5/4',a='1/2',dimension=2,
              lhs=lhs,base=base,rhs=rhs,rhs_minus_lhs=rhs-lhs,
              identity='8*(Delta-(alpha/2)log2)=log(lhs/rhs)<0',
              scope='refutes universal COMPARISON OF BOUNDS U<=c^m F_a(E_1), not the actual moment bound'),
          exact_time_CS=dict(rate='1+s',square_of_integral='9/4',integral_of_square='7/3',
                             positive_gap=str(Fraction(7,3)-Fraction(9,4))),
          evidence_scope='abstract scalar calculus only; no actual C_occ/occupation energy/moment/PDE measurements; no enclosure or statistical confidence')
with mp.workdps(90):
    data['precision_differences']=[dict(case=r['case'],eta=r['eta'],
        direct_score_difference=mp.nstr(abs(mp.mpf(r['direct_scalar_score'])-mp.mpf(s['direct_scalar_score'])),85),
        closed_U_difference=mp.nstr(abs(mp.mpf(r['closed_U'])-mp.mpf(s['closed_U'])),85))
        for r,s in zip(data['runs'][0]['rows'],data['runs'][1]['rows'])]
(P/'scalar-ceiling-screen-v1.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(dict(maxima=[dict(dps=r['dps'],maxima=r['maxima']) for r in data['runs']],
                      exact_shortcut=data['exact_eta1_shortcut_counterexample'])))
