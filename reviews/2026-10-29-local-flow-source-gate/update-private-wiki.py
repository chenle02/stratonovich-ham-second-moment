from pathlib import Path
import difflib,gzip,hashlib,json,re,subprocess,tempfile
ROOT=Path.cwd();R=ROOT/'reviews/2026-10-29-local-flow-source-gate';P=ROOT/'reviews/2026-10-28-status-propagation'
sha=lambda b:hashlib.sha256(b).hexdigest()
summary=json.loads((R/'review-summary.json').read_text())
assert summary['accepted'] and summary['confidence']=='high'
assert summary['source_revision']=='d020a2a9e04f0ef8bcaa74de53cc8a6f76c2fbca'
wiki=ROOT.parent/'SPDEs-wiki';rel='content/projects/stratonovich-ham-second-moment.md'
base=(wiki/rel).read_bytes();assert sha(base)=='d10c4f829f74eeea0f91c1a2122204365ff1d0c0f4f1cac373a17ea1db1ddb33'
proposal=(P/'proposed-project-page.md').read_text()
new='**Reviewed masked/local causal flow (2026-10-29).** For the original d1covariance class, the physical-mask driver defines a source-compatible causal Young evolution on a separable uniformly-local phase containingdata1, with operator norm controlled by a finite MAXIMUM of local HS norms. Its noise-only smooth averages agree with the ORIGINALcanonical Stratonovich averages. Actual growing-unit-block flows converge to their deterministic-profile flows in every finiteLp under the stated profile hypotheses. Scientific source d020a2a9e04f0ef8bcaa74de53cc8a6f76c2fbca, Opus5.5/HIGH,13groups PASS,35texts/9exact source images, no required repairs. Seven new finite Lean consumers and8unchanged reused deductions support exact applications; operator/Young/Gaussian/causality/canonical/block analysis remains informal reviewed proof. Evidence: Article notes/local-causal-young-flow.md and reviews/2026-10-29-local-flow-source-gate/adjudication.md.\n\nThis is an ALLORDERmasked/local d1flow bridge, not a global stationary operator or an entire-product growth estimate. Nonzero-profile canonical Cameron-shift identity, spectral cone/product growth, sharp event/variational constants and higher dimensions remain OPEN. Full pointwise sharp target, WHITE13/original9andcanonical110-page/60-proofTeX/PDF unchanged. CLO2026is method prior art and the10th queued reference, not completed ingestion/novelty clearance. Private proposal only; no canonical publication/circulation or intended source correction.\n\n'
proposal=proposal.replace('## Current state\n\n','## Current state\n\n'+new,1)
front=lambda s:s.split('---',2)[1]
links=lambda s:set(re.findall(r'\[\[([^]|]+)',s))
assert front(base.decode())==front(proposal)
assert links(base.decode())==links(proposal)
(P/'proposed-project-page.md').write_text(proposal)
patch=''.join(difflib.unified_diff(base.decode().splitlines(keepends=True),proposal.splitlines(keepends=True),fromfile='a/'+rel,tofile='b/'+rel)).encode()
compressed=gzip.compress(patch,mtime=0);assert gzip.decompress(compressed)==patch
(P/'project-page.patch.gz').write_bytes(compressed)
with tempfile.TemporaryDirectory(prefix='stratonovich-private-patch-') as tmp:
 d=Path(tmp);target=d/rel;target.parent.mkdir(parents=True);target.write_bytes(base)
 subprocess.run(['git','init','-q',str(d)],check=True)
 subprocess.run(['git','-C',str(d),'apply','--check','-'],input=patch,check=True)
 subprocess.run(['git','-C',str(d),'apply','-'],input=patch,check=True)
 assert target.read_bytes()==proposal.encode()
prep=json.loads((P/'preparation.json').read_text());prep.update(proposed_page_sha256=sha(proposal.encode()),patch_gzip_sha256=sha(compressed),patch_uncompressed_sha256=sha(patch),local_flow_scientific_source=summary['source_revision'],local_flow_status='13groups PASS/HIGH;actual d1masked/local causal flow,canonical average,block stability;not spectral productgrowth/sharp',local_flow_binding='reviews/2026-10-29-local-flow-source-gate/final-status-binding.json',published=False)
(P/'preparation.json').write_text(json.dumps(prep,indent=2)+'\n')
checks=json.loads((P/'local-checks.json').read_text());checks.update(local_flow_13high=True,local_flow_causal_source_compatible=True,local_flow_canonical_average_identified=True,local_flow_spectral_productgrowth_sharp_unproved=True,local_flow_patch_applies_exactly=True)
(P/'local-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
with (P/'publication-request.md').open('a') as f:f.write('\nPrivate actual local-flow checkpoint added: source d020a2a9e04f0ef8bcaa74de53cc8a6f76c2fbca,13groups/HIGH. Actual d1masked/local causal flow,canonical average/block stability; spectral productgrowth/event/sharp target open. Exact patch roundtrip/apply verified. Still PRIVATE/unpublished; no queue ticket or canonical write.\n')
assert sha((wiki/rel).read_bytes())==sha(base)
print('Private wiki proposal exact patch/frontmatter/link checks PASS; canonical unchanged.')
