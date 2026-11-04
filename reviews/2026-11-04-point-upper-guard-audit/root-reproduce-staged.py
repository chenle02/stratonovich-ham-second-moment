#!/usr/bin/env python3
"""Bounded synthetic record controls. No native review or producer writes."""
import importlib.util
import hashlib
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
PACKET = OUT.parent / 'stratonovich-af97-point-signed-packet-v2'
preimage = OUT / 'validate_report-staged-preimage.py'
assert hashlib.sha256(preimage.read_bytes()).hexdigest() == 'd9a74827a0ba39ba55d8d0bea8e3ca627c092b5081ac728ccd1c02f21fdcc935'
spec = importlib.util.spec_from_file_location('root_preserved_guard', preimage)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.ROOT = PACKET  # Read held inputs; execute ONLY the independently copied old code.
canonical = {q['id']:q for q in json.loads((OUT.parent/'stratonovich-af97-themed-main-plan-20261103/proof-ownership.json').read_text())['proofs']}
def dependency(target, reference, state):
  q = canonical[target]
  return {'target':target,'target_label':q['claim_label'],'owner_unit':q['owner_unit'],
    'kind':'OWN','premise_role':'PREMISE','state':state,'use_scope':'IDENTIFIED_SUBCLAUSE',
    'clause_id':'SOURCE_SUBCLAUSE:bounded structural witness',
    'actual_hypotheses':'Actual compact zero-start Holder path with the stated phase and horizon.',
    'actual_consumer_check':'Apply exactly the identified compact endpoint or multiplier clause, with the full parent unresolved.',
    'source_body_sha256':q['raw_body_sha256'],'math_reference':reference,
    'unresolved_parent_condition':'Full parent remains unreconstructed; no full-parent completion follows from this subclause.'}
def checked(label, target, reference, state, expected, actual_entry=None):
  r = mod.fixture()
  row = next(p for p in r['proofs'] if p['id'] == ('PROOF185' if target=='PROOF165' else 'PROOF179'))
  d = dependency(target,reference,state)
  if label=='full165-positive': d['clause_id']='SOURCE_FULL_PROOF:complete165'
  row['inputs']=[d]
  if actual_entry:
    next(p for p in r['proofs'] if p['id']==target)['actual_working']=[actual_entry]
  issues=mod.problems(r)
  return {'id':label,'expected_reference_eligibility':expected,'actual_record_accepted':not issues,'issues':issues,
    'synthetic_fixture_not_native_report':True}
result=[]
result.append(checked('full165-positive','PROOF165','source-proof:notes/integrated_symplectic_phase.tex#PROOF165@68:153','PRIOR_MATH_CONSUMER_VALIDATED',True))
for line in [79,85,108,110,130,134]:
  result.append(checked('display-only-negative-'+str(line),'PROOF165',f'source-proof:notes/integrated_symplectic_phase.tex#PROOF165@{line}:{line}','PRIOR_MATH_CONSUMER_VALIDATED',False))
for field in ['consumer_check','remaining_obligation']:
  result.append(checked('current-no-working-negative-'+field,'PROOF178','current#/proofs/3/'+field,'CURRENT_MATH_RECONSTRUCTED',False))
result.append(checked('current-real-subclause-limited-parent-positive','PROOF178','current#/proofs/3/actual_working/0','CURRENT_MATH_RECONSTRUCTED',True,'M_n chi_R=V_n and ||V_n-V_j||_(H^-1/2)<=||chi_R||_(H^1/2)||M_n-M_j||, so the unique potential converges at fixed R.'))
payload={'scope':'ROOT_SYNTHETIC_CODE_COUNTEREXAMPLES_NOT_MATHEMATICAL_REVIEW','staged_preimage_sha256':hashlib.sha256(preimage.read_bytes()).hexdigest(),'cases':result,'producer_writes':False,'provider_actions':False}
(OUT/'results.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload,indent=2))
