"""Exact finite static d1 white calibration from pairings, not copied length formulas."""
import json
from sympy import symbols, Abs, simplify, expand, Poly, Rational, integrate, factorial, Matrix
u,v=symbols('u v',nonnegative=True)
pairings={'A':[(0,1),(2,3)],'B':[(0,2),(1,3)],'C':[(0,3),(1,2)]}
sectors=[(u,u+v),(u+v,u),(u,-v)]
expected_sector={
 (0,'A'):['1/30','1/60','1/60'],(0,'B'):['1/90','1/120','1/360'],(0,'C'):['1/60','1/90','1/180'],
 (1,'A'):['1/24','3/160','11/480'],(1,'B'):['1/72','3/160','11/1440'],(1,'C'):['1/48','1/30','1/48'],
 (2,'A'):['1/18','1/18','1/9'],(2,'B'):['1/30','1/60','1/60'],(2,'C'):['31/1440','31/1440','31/2160']}
expected_coeff={(0,'A'):'1/2880',(0,'B'):'1/8640',(0,'C'):'1/5760',(1,'A'):'1/576',(1,'B'):'29/34560',(1,'C'):'1/640',(2,'A'):'1/144',(2,'B'):'1/480',(2,'C'):'31/17280'}
def integrate_sector(m,n,l1,l2):
    cs=[(l1,m),(l2,n)]
    constraints=[]
    for L,power in cs:
        if power:
            assert expand(L).subs({u:0,v:0})==0
            a,b=expand(L).coeff(u),expand(L).coeff(v)
            assert a>=0 and b>=0 and (a>0 or b>0)
            constraints.append((a,b))
    upper=min(1/a for a,b in constraints if a>0)
    bounds=[(1-a*u)/b for a,b in constraints if b>0]
    assert bounds
    cuts={Rational(0),upper}
    for i,h in enumerate(bounds):
        for g in bounds[i+1:]:
            d=expand(h-g);slope=d.coeff(u)
            if slope:
                cross=simplify(-d.subs(u,0)/slope)
                if 0<cross<upper:cuts.add(cross)
    cuts=sorted(cuts);pieces=[];value=0
    poly=expand((1-l1)**m*(1-l2)**n)
    for lo,hi in zip(cuts,cuts[1:]):
        mid=(lo+hi)/2
        h=min(bounds,key=lambda z:z.subs(u,mid))
        val=integrate(integrate(poly,(v,0,h)),(u,lo,hi))
        assert val.is_Rational
        pieces.append({'u_from':str(lo),'u_to':str(hi),'v_upper':str(h),'integral':str(val)})
        value+=val
    return simplify(value),pieces
rows=[];row_sums={m:0 for m in [0,1,2]}
for m in [0,1,2]:
    n=4-m
    for tag,pp in pairings.items():
        vals=[];detail=[]
        for x,y in sectors:
            assert abs(Matrix([[x.diff(u),x.diff(v)],[y.diff(u),y.diff(v)]]).det())==1
            positions=[None]*4
            for p,z in zip(pp,[x,y]):
                for i in p:positions[i]=z
            def length(indices):
                prev=0;L=0
                for i in indices:
                    L+=Abs(positions[i]-prev);prev=positions[i]
                return simplify(L)
            l1=length(range(m));l2=length(range(m,4))
            val,pieces=integrate_sector(m,n,l1,l2);vals.append(val)
            detail.append({'map':[str(x),str(y)],'L1':str(l1),'L2':str(l2),'value':str(val),'pieces':pieces})
        assert vals==[Rational(z) for z in expected_sector[m,tag]],(m,tag,vals)
        coeff=simplify(2*sum(vals)/(16*factorial(m)*factorial(n)))
        assert coeff==Rational(expected_coeff[m,tag]),(m,tag,coeff)
        row_sums[m]+=coeff
        rows.append({'split':[m,n],'pairing':tag,'sector_values':[str(z) for z in vals],'coefficient':str(coeff),'derivation':detail})
assert [row_sums[m] for m in [0,1,2]]==[Rational('11/17280'),Rational('143/34560'),Rational('187/17280')]
total=simplify(2*row_sums[0]+2*row_sums[1]+row_sums[2]);assert total==Rational(11,540)
controls={'omit_plane_reflection_factor':total/2,'omit_mirrored_chain_splits':sum(row_sums.values())}
assert all(z!=total for z in controls.values())
print(json.dumps({'status':'ALL27_EXACT_SECTORS_AND9_COEFFICIENTS_PASS_NOT_REVIEW_GRADE','frozen_main_sha256':'516d6a650bdac7d3da68672f37836afd084b651c39553b43d5135d0512e39d14','source_labels':['L:static-four','E:static-sector','E:sector-values','E:static-four-table'],'basis':'Positions from actual pair partitions, reset at each chain root; absolute-increment lengths derived per sector; exact linear constraint intersections and polynomial integration. Factor1/16 from four Green densities; factorial simplex volumes and reflection factor explicit.','unit_time':1,'spatial_covariance':'unit Dirac delta','sector_integrals':27,'table_coefficients':9,'row_sums':{str(k):str(w) for k,w in row_sums.items()},'full_total':str(total),'falsification_controls':{k:str(w) for k,w in controls.items()},'rows':rows,'static_fixed_order_calibration_only':True,'no_large_time_constant_or_Lean_claim':True},indent=2))
