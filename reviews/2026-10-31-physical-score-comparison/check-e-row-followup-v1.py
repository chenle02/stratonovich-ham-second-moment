"""Post-fit independent spatial E-row discretization, not a PDE solver."""
import hashlib
import json
from pathlib import Path
import mpmath as mp
import numpy as np

P = Path(__file__).resolve().parent
mp.mp.dps = 70
amp, a = mp.mpf(3), mp.mpf(1)/3
ell_i, ell_j = mp.mpf(3)/5, mp.mpf(2)/5
time_pair = (1-(mp.mpf(3)/5)**(2-a)-(mp.mpf(2)/5)**(2-a))/((1-a)*(2-a)*ell_i*ell_j)
center, radius = mp.mpf(27)/20, mp.mpf(9)/20


def flat(t):
    return mp.exp(-1/t) if t > 0 else mp.mpf(0)


def mask(x):
    t = abs(x)-1
    if t <= 0:
        return mp.mpf(1)
    if t >= 1:
        return mp.mpf(0)
    return (flat(1-t)/(flat(t)+flat(1-t)))**2


def bump(x):
    z = (x-center)/radius
    return mp.exp(-1/(1-z*z)) if abs(z) < 1 else mp.mpf(0)


cuts = [center-radius, mp.mpf(1), center, center+radius]
norm2 = mp.quad(lambda x:bump(x)**2, cuts)
# This raw covariance pairing is evaluated by adaptive multiprecision integration.
raw_pair = amp*time_pair*mp.quad(lambda x:mp.exp(-x*x)*mask(x)*bump(x)**2/norm2,cuts)
wrong_double_mask = amp*time_pair*mp.quad(lambda x:mp.exp(-x*x)*mask(x)**2*bump(x)**2/norm2,cuts)
rows = []
for N in [512,1024,2048]:
    dx = 8/N
    x = np.linspace(-4,4,N,endpoint=False)
    f = np.array([float(bump(mp.mpf(float(t)))/mp.sqrt(norm2)) for t in x])
    m = np.array([float(mask(mp.mpf(float(t)))) for t in x])
    # Construct the actual white deterministic mean ONCE: Gamma*q = 3q.
    # Apply Lz=(0,m*Gamma*q*f) and w=(0,Lambda*f) in the periodic spectral model.
    V = float(amp*time_pair)*m*np.exp(-x*x)
    freq = 2*np.pi*np.fft.fftfreq(N,d=dx)
    Lambda = np.sqrt(1+freq*freq)
    displacement_hat = np.fft.fft(f,norm='ortho')
    output_velocity_hat = np.fft.fft(V*f,norm='ortho')
    dual_velocity_hat = Lambda*displacement_hat
    e_row = float((dx*np.sum(output_velocity_hat*np.conj(dual_velocity_hat)/Lambda)).real)
    # The wrong E metric deliberately omits Lambda^-1, held independently fixed.
    wrong_metric = float((dx*np.sum(output_velocity_hat*np.conj(dual_velocity_hat))).real)
    rows.append(dict(N=N,dx=dx,e_row=e_row,
                     residual=float(abs(mp.mpf(e_row)-raw_pair)),
                     wrong_extra_covariance_gap=float(abs(mp.mpf(e_row)-amp*raw_pair)),
                     wrong_no_cell_division_gap=float(abs(mp.mpf(e_row)-ell_i*raw_pair)),
                     wrong_double_mask_gap=float(abs(mp.mpf(e_row)-wrong_double_mask)),
                     wrong_e_metric_gap=abs(wrong_metric-e_row),
                     grid_L2_norm_squared=float(dx*np.sum(f*f))))
assert rows[-1]['residual'] < 1e-10
assert all(r[k]>1e-3 for r in rows for k in ['wrong_extra_covariance_gap','wrong_no_cell_division_gap','wrong_double_mask_gap','wrong_e_metric_gap'])
data=dict(schema='actual-e-row-followup/1',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          timing='AFTER statement FIT and initial author proof draft; not credited as the earlier pre-proof screen',
          libraries=dict(mpmath=mp.__version__,numpy=np.__version__),
          covariance='3 delta_0',a='1/3',control='h_0 tensor exp(-x^2)',test='h_1 tensor m*f_1^2',
          raw_pair=mp.nstr(raw_pair,75),wrong_double_mask_pair=mp.nstr(wrong_double_mask,75),
          mpmath_dps=70,fft_arithmetic='float64',periodic_interval=[-4,4],rows=rows,
          scope='spatial spectral E-row calibration and one-sided wrong-factor contrasts, not convergence proof/enclosure/operator construction/PDE simulation')
(P/'e-row-followup-v1.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(dict(rows=rows,scope=data['scope'])))
