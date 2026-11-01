"""Bounded deterministic calibration; no PDE simulation or error enclosure."""
import hashlib
import json
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent


def run(dps):
    with mp.workdps(dps):
        a, amp = mp.mpf(1) / 3, mp.mpf(3)
        cells = [(mp.mpf(0), mp.mpf(2) / 5), (mp.mpf(2) / 5, mp.mpf(1))]
        supports = [(mp.mpf(0), mp.mpf(7) / 20), (mp.mpf(27) / 20, mp.mpf(9) / 20)]

        def flat(x):
            return mp.exp(-1 / x) if x > 0 else mp.mpf(0)

        def mask(x):
            t = abs(x) - 1
            if t <= 0:
                return mp.mpf(1)
            if t >= 1:
                return mp.mpf(0)
            eta = flat(1 - t) / (flat(t) + flat(1 - t))
            return eta**2

        def bump(x, c, r):
            z = (x - c) / r
            return mp.exp(-1 / (1 - z*z)) if abs(z) < 1 else mp.mpf(0)

        profiles = []
        for c, r in supports:
            norm2 = mp.quad(lambda x: bump(x, c, r)**2, [c-r, c, c+r])
            profiles.append(lambda x, c=c, r=r, norm2=norm2: bump(x, c, r)**2 / norm2)

        def positive(x):
            return max(x, mp.mpf(0))

        def time_mean(s, j):
            lo, hi = cells[j]
            p = 1-a
            return (positive(s-lo)**p - positive(s-hi)**p
                    + positive(hi-s)**p - positive(lo-s)**p) / (p * (hi-lo))

        rows = []
        for i, (lo, hi) in enumerate(cells):
            ell = hi-lo
            c, r = supports[i]
            rho = profiles[i]
            cuts = sorted(set([c-r, c, c+r] + [v for v in [-1, 1] if c-r < v < c+r]))
            one = mp.quad(lambda x: mask(x)*rho(x)**2, cuts)
            two = mp.quad(lambda x: mask(x)**2*rho(x)**2, cuts)
            raw = mp.quad(lambda x: rho(x)**2, cuts)
            for j, (lj, hj) in enumerate(cells):
                ellj = hj-lj
                time_exact = (abs(hi-lj)**(2-a) + abs(lo-hj)**(2-a)
                              - abs(lo-lj)**(2-a) - abs(hi-hj)**(2-a)) / (
                                  (1-a)*(2-a)*ell*ellj)
                time_direct = mp.quad(lambda s: time_mean(s, j), [lo, hi]) / ell
                # Control h_j tensor rho_i, test h_i tensor m*rho_i.
                pairing = amp*time_exact*one
                averaged_physical_mean = amp*time_direct*one
                rows.append(dict(cell=i, control_time_cell=j,
                                 ell=ell, ell_control=ellj,
                                 time_exact=time_exact, time_direct=time_direct,
                                 time_residual=abs(time_direct-time_exact),
                                 raw_label_pairing=pairing,
                                 averaged_physical_mean=averaged_physical_mean,
                                 row_residual=abs(pairing-averaged_physical_mean),
                                 wrong_no_cell_division_gap=abs(pairing-ell*averaged_physical_mean),
                                 wrong_extra_covariance_gap=abs(pairing-amp*averaged_physical_mean),
                                 wrong_double_mask_gap=abs(pairing-amp*time_direct*two),
                                 masked_gram_diagonal=amp*time_exact*two,
                                 unmasked_gram_diagonal=amp*time_exact*raw,
                                 gram_entry_gap=amp*time_exact*(raw-two)))

        # Nonlocal Riesz cross entry, alpha=1/2. Disjoint supports avoid its singularity.
        # D11-C11=0 exactly; D12-C12>0 implies det(D-C)=-(D12-C12)^2<0.
        cross_rows = []
        for nodes in [24, 40]:
            xx, ww = mp.gauss_quadrature(nodes, 'legendre')
            spatial = mp.mpf(0)
            c0, r0 = supports[0]
            c1, r1 = supports[1]
            for ii in range(nodes):
                x = c0+r0*xx[ii]
                for jj in range(nodes):
                    y = c1+r1*xx[jj]
                    spatial += (r0*r1*ww[ii]*ww[jj]*profiles[0](x)*profiles[1](y)
                                * (1-mask(y)) / mp.sqrt(abs(x-y)))
            lo, hi = cells[0]
            lj, hj = cells[1]
            tij = (abs(hi-lj)**(2-a)+abs(lo-hj)**(2-a)
                   -abs(lo-lj)**(2-a)-abs(hi-hj)**(2-a)) / ((1-a)*(2-a)*(hi-lo)*(hj-lj))
            gap = amp*tij*spatial
            cross_rows.append(dict(nodes=nodes, cross_gap=gap, difference_determinant=-gap**2))

        def encode(x):
            if isinstance(x, mp.mpf):
                return mp.nstr(x, dps+5)
            if isinstance(x, dict):
                return {k:encode(v) for k,v in x.items()}
            if isinstance(x, list):
                return [encode(v) for v in x]
            return x

        maximum = max(rows, key=lambda row:row['row_residual'])
        assert maximum['row_residual'] < mp.mpf(10)**(-dps+6)
        assert all(row['wrong_no_cell_division_gap'] > 0 for row in rows)
        assert all(row['wrong_extra_covariance_gap'] > 0 for row in rows)
        assert all(row['wrong_double_mask_gap'] > 0 for row in rows if row['cell'] == 1)
        assert all(row['gram_entry_gap'] >= 0 for row in rows)
        assert all(row['difference_determinant'] < 0 for row in cross_rows)
        return encode(dict(dps=dps, rows=rows, riesz_cross_rows=cross_rows,
                           max_row_residual=maximum['row_residual'],
                           max_row_case=[maximum['cell'], maximum['control_time_cell']],
                           scope='floating normalization calibration and wrong-factor controls; no certified integration accuracy'))


data = dict(schema='physical-normalization-screen/1',
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            alpha_white=1, alpha_riesz='1/2', a='1/3', covariance_amplitude=3,
            mask='eta(x)^2 with eta=1 on [-1,1], support [-2,2], smooth flat transition',
            runs=[run(40), run(70)],
            jensen_controls=[dict(values=[-1,1], mean_sqrt_positive='1/2', sqrt_positive_mean=0),
                             dict(values=[0,4], mean_sqrt_positive=1, sqrt_positive_mean='sqrt(2)')],
            exclusions=['no optimization/PDE simulation', 'no interval enclosure',
                        'no inference of PB1-PB5', 'no statistical confidence'])
with mp.workdps(80):
    data['cross_precision_rows'] = [
        dict(cell=x['cell'], control_time_cell=x['control_time_cell'],
             row_difference=mp.nstr(abs(mp.mpf(x['raw_label_pairing'])-mp.mpf(y['raw_label_pairing'])), 75))
        for x,y in zip(data['runs'][0]['rows'],data['runs'][1]['rows'])]
    data['riesz_mesh_change'] = [dict(dps=r['dps'], difference=mp.nstr(abs(
        mp.mpf(r['riesz_cross_rows'][0]['cross_gap'])-mp.mpf(r['riesz_cross_rows'][1]['cross_gap'])),75))
        for r in data['runs']]
(HERE/'physical-normalization-screen-v1.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(dict(runs=[dict(dps=r['dps'], max_row_residual=r['max_row_residual'],
                                     max_row_case=r['max_row_case']) for r in data['runs']],
                      riesz_mesh_change=data['riesz_mesh_change'])))
