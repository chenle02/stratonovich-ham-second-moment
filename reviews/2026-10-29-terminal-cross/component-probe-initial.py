"""Independent positive-quadrature check of exponential component formulas."""
from pathlib import Path
import hashlib
import json
import mpmath as mp


mp.mp.dps=60
rows=[]
pairs=[(mp.mpf(a),mp.mpf(t))for a in ['.105','1.5','60']
       for t in ['.5','.6','1','2','61']]+[(mp.mpf(1),mp.mpf(1)),(mp.mpf('.5'),mp.mpf('.5'))]
for A,t in pairs:
    for text in ['0','.1','1','10']:
        w=mp.mpf(text)
        value=mp.quad(lambda q:mp.exp(-t*q)*(mp.exp(-A*abs(w-q))
                      +(1+2*t*q)*mp.exp(-A*(w+q))),[0,w,mp.inf])
        mass=2*(A+2*t)/(A+t)**2
        if A==t:
            closed=mp.exp(-A*w)*(w+mp.mpf(3)/(2*A))
        else:
            closed=(4*t*t*mp.exp(-A*w)-2*A*(t+A)*mp.exp(-t*w))/((t-A)*(t+A)**2)
        rate=A*t/(A+2*t)
        bound=mass*mp.exp(-rate*w)
        uniform=mass*mp.exp(-A/(2*(A+1))*w)
        relative=abs(closed-value)/value
        assert relative<mp.mpf('1e-45'), (str(A),str(t),text,str(value),str(closed),str(relative))
        assert closed<=bound+mp.mpf('1e-50')
        assert bound<=uniform+mp.mpf('1e-50')
        rows.append(dict(A=str(A),s=str(t),w=text,value=str(value),closed=str(closed),
                         relative_error=str(relative),rate_bound=str(bound),uniform_bound=str(uniform)))
out=dict(status='PASS finite high-precision checks;quadrature not certified',dps=mp.mp.dps,
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cases=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cases':len(rows),'max_relative_error':str(max(mp.mpf(r['relative_error'])for r in rows)),
                  'scope':out['status']},indent=2))
