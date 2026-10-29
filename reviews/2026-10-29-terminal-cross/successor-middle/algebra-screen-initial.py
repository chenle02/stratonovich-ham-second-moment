import sympy as S,json,hashlib
from pathlib import Path
b,c,d,e,z,t,x,y=S.symbols('b c d e z t x y',positive=True)
B=b+c;C=b+1
K=1/(4*b*c*(c+1))
M=lambda r:K*(1/(r*(r+C))+1/(r*(r+B)*(r+C)))
f1=(d+e+C)/(d*e*(d+C)*(e+C))
f2=(d*d+d*e+e*e+(B+C)*(d+e)+B*C)/(d*e*(d+B)*(e+B)*(d+C)*(e+C))
U=M(e)+K*(f1+f2)/(d+e)
I=(2*b*b+4*b*c+2*c*c-c+1)/(8*b*c*(b+1)*(2*b+1)*(b+c-1)*(2*b+2*c-1))
D=S.factor(I-U);num,den=S.fraction(D)
bz=(z*z-1)/(2*z);ez=(z*z+1)/(2*z)
cz=((bz+1)*t-(bz-1)/t)/2;dz=((bz+1)*t+(bz-1)/t)/2
expr=S.cancel(num.subs({b:bz,c:cz,d:dz,e:ez}))
poly=S.fraction(expr)[0];shift=S.Poly(S.expand(poly.subs({z:x+2,t:y+1})),x,y)
terms=shift.terms();neg=[(m,int(v))for m,v in terms if v<0]
out={'scope':'UNREVIEWED exact coefficient screen for a middle-diagram envelope;not a model proof','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'terms':len(terms),'negative_terms':neg,'all_coefficients_nonnegative':not neg,'numerator_factored':str(S.factor(poly)),'denominator_before_parameterization':str(den),'shifted_coefficients':[{'x':m[0],'y':m[1],'coefficient':int(v)}for m,v in terms]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['shifted_coefficients','numerator_factored','denominator_before_parameterization']},indent=2))
