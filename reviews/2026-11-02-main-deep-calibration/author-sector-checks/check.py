from pathlib import Path
import sympy as s
import json,hashlib,subprocess
u,v=s.symbols('u v',nonnegative=True)
# Independent reconstruction from the nine physical chain length pairs.
sectors=[(u,u+v,v),(u+v,u,v),(u,v,u+v)]
expected=[['1/30','1/60','1/60'],['1/90','1/120','1/360'],['1/60','1/90','1/180'],['1/24','3/160','11/480'],['1/72','3/160','11/1440'],['1/48','1/30','1/48'],['1/18','1/18','1/9'],['1/30','1/60','1/60'],['31/1440','31/1440','31/2160']]
rows=[]
for row in range(9):
 m,n=[(0,4),(1,3),(2,2)][row//3];label='ABC'[row%3]; vals=[]
 for j,(x,y,w) in enumerate(sectors):
  L1,L2=[(0,x+w),(0,x+3*w),(0,x+2*w),(x,x+w),(x,y+2*w),(x,y+w),(x,y),(x+w,x+w),(x+w,y+w)][row]
  constraints=[s.expand(L) for L,power in [(L1,m),(L2,n)] if power]
  umax=min(1/L.coeff(u) for L in constraints if L.coeff(u)>0)
  lines=[(1-L.coeff(u)*u)/L.coeff(v) for L in constraints if L.coeff(v)>0]
  breaks={s.Integer(0),umax}
  for a in lines:
   for b in lines:
    if a!=b:
     for z in s.solve(a-b,u):
      if 0<z<umax:breaks.add(z)
  breaks=sorted(breaks);poly=s.expand((1-L1)**m*(1-L2)**n);pieces=[];total=s.Integer(0)
  for left,right in zip(breaks,breaks[1:]):
   mid=(left+right)/2;top=min(lines,key=lambda a:a.subs(u,mid));assert top.subs(u,mid)>0
   inner=s.expand(s.integrate(poly,(v,0,top)));value=s.integrate(inner,(u,left,right));total+=value
   pieces.append({'u_from':str(left),'u_to':str(right),'v_from':'0','v_to':str(top),'inner_integral_polynomial':str(inner),'piece_value':str(value)})
  assert total==s.Rational(expected[row][j]),(row,j,total)
  vals.append(total);rows.append({'split':[m,n],'pairing':label,'sector':j+1,'L1':str(L1),'L2':str(L2),'integrand':str(poly),'pieces':pieces,'total':str(total),'printed_matches':True})
 rowval=s.simplify(2*sum(vals)/(16*s.factorial(m)*s.factorial(n)))
 for r in rows[-3:]:r['reflected_normalized_row']=str(rowval)
rolled=[s.Rational(rows[i]['reflected_normalized_row']) for i in range(0,27,3)]
total=2*sum(rolled[:3])+2*sum(rolled[3:6])+sum(rolled[6:]);assert total==s.Rational(11,540)
r=Path(__file__).resolve().parents[3];p='notes/notes_stratonovich_ham_second_moment.tex';raw=(r/p).read_bytes();assert raw==subprocess.check_output(['git','show','887fbfbe0fa4368d6b32a436615d73349b2445d8:'+p],cwd=r)
out={'scope':'Author-side exact finite polynomial verification only; not an independent review, regularization proof, asymptotic claim or HIGH upgrade.','source_revision':'887fbfbe0fa4368d6b32a436615d73349b2445d8','source_path':p,'source_sha256':hashlib.sha256(raw).hexdigest(),'sympy_version':s.__version__,'sector_parameterization':['(|x|,|y|,|x-y|)=(u,u+v,v)','(u+v,u,v)','(u,v,u+v)'],'method':'For each physical length pair impose L1<=1 if m>0 and L2<=1 if n>0; split u where active affine v upper bounds cross; integrate the polynomial exactly. Reflected sectors give factor2/(16*m!*n!).','rows':rows,'all27_match':True,'normalized_rows':[str(x) for x in rolled],'total':str(total)}
Path(__file__).with_name('worked-sectors.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:27 exact sector integrals;9 normalized rows;total11/540. Author check only.')
