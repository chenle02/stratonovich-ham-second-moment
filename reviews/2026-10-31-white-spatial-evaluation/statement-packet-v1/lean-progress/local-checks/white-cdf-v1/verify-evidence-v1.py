"""Fail-closed parsing of complete axiom lists and exact arithmetic False logs."""
import hashlib
import json
import re
from pathlib import Path

P = Path(__file__).resolve().parent
TARGETS = {'StratonovichHAMAudit.WhiteCDF.cdf_square_bound',
           'StratonovichHAMAudit.WhiteCDF.energy_upper',
           '_private.Audit.0.actual_energy_consumer'}


def axioms(text):
    lines = [x for x in text.splitlines() if 'depends on axioms:' in x]
    if len(lines) != 3:
        raise ValueError('wrong inventory count')
    found = []
    for line in lines:
        m = re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]", line)
        if m is None:
            raise ValueError('malformed axiom inventory')
        found.append(m[1])
        names = [re.sub(r'\.\{[^}]*\}', '', x.strip()) for x in m[2].split(',') if x.strip()]
        if not set(names) <= {'propext', 'Classical.choice', 'Quot.sound'}:
            raise ValueError('unapproved axiom')
    if set(found) != TARGETS or len(set(found)) != len(found):
        raise ValueError('wrong or duplicate target')


def negative(text):
    if re.fullmatch(r'[A-Za-z0-9_./-]+\.lean:\d+:\d+: error: unsolved goals\n⊢ False\n?', text) is None:
        raise ValueError('not the sole exact arithmetic False goal')


def rejects(fn, text):
    try:
        fn(text)
    except ValueError:
        return True
    return False


s = (P/'types-and-axioms.txt').read_text()
axioms(s)
rows = json.loads((P/'negative-controls-v1.json').read_text())
assert set(rows) == {'negative-cdf', 'negative-energy'}
for row in rows.values():
    assert row['exit'] == 1
    assert hashlib.sha256(row['stdout'].encode()).hexdigest() == row['stdout_sha256']
    negative(row['stdout'])
inventories = [x for x in s.splitlines() if 'depends on axioms:' in x]
mutations = []
for line in inventories:
    mutations.append(('extra_unapproved_axiom', rejects(axioms, s.replace(line, line[:-1]+', PhantomAxiom]'))))
    mutations.append(('sorryAx', rejects(axioms, s.replace(line, line.replace('propext', 'sorryAx')))))
mutations += [('missing_inventory', rejects(axioms, s.replace(inventories[0], ''))),
              ('duplicate_inventory', rejects(axioms, s+'\n'+inventories[0]))]
for row in rows.values():
    t = row['stdout']
    mutations += [('compound_false', rejects(negative, t.replace('⊢ False', '⊢ False ∧ True'))),
                  ('extra_error', rejects(negative, t+'Other.lean:1:1: error: unknown constant x\n')),
                  ('API_error', rejects(negative, t.replace('unsolved goals', 'unknown identifier')))]
assert all(ok for _, ok in mutations)
result = dict(actual_axiom_inventories=3, actual_exact_false_controls=2,
              mutations=[dict(case=k,rejected=v) for k,v in mutations],
              all_rejected=True, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              scope='text evidence guard only; no new Lean or analytic theorem')
(P/'evidence-guard-v1.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: complete axiom inventories, two exact False logs,',len(mutations),'adversarial mutations rejected')
