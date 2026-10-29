from pathlib import Path
import difflib,gzip,hashlib,json,re,subprocess,tempfile
ROOT=Path.cwd();R=ROOT/'reviews/2026-10-29-interaction-driver';P=ROOT/'reviews/2026-10-28-status-propagation'
sha=lambda b:hashlib.sha256(b).hexdigest()
summary=json.loads((R/'review-summary.json').read_text())
assert summary['accepted'] and summary['confidence']=='high'
assert summary['source_revision']=='b398b77052718adc8ac4f3439a3c738b504aea86'
wiki=ROOT.parent/'SPDEs-wiki';rel='content/projects/stratonovich-ham-second-moment.md'
base=(wiki/rel).read_bytes();assert sha(base)=='d10c4f829f74eeea0f91c1a2122204365ff1d0c0f4f1cac373a17ea1db1ddb33'
proposal=(P/'proposed-project-page.md').read_text()
new="""**Reviewed local interaction-driver paths (2026-10-29).** In d1 on the balanced H^(1/2)xH^(-1/2) phase, the localized FIRST Gaussian interaction driver has squared increment bound h^(2-a), with a squared logarithmic loss for white space. It has Holder versions for every1/2<theta<1-a/2; SOURCE-compatible common Gaussian cutoffs converge in every finiteLp Holder path norm. The proof uses a positive white trace representation, fixed-horizon finite propagation and both filtered/defect covariance bounds, not cutoff commutation or nonlinear covariance order. A finite-box consequence gives normalized local first-driver smallness under the explicit sufficient moment budget. Scientific source b398b77052718adc8ac4f3439a3c738b504aea86, actual native Opus5.5/HIGH, all9groups PASS,26texts/2exact source images, no required repairs. Eight finite Lean consumers check exact normalization/power/Holder/box applications; Gaussian/operator/integration/path arguments remain informal reviewed proofs. Evidence: Article notes/interaction-driver-path.md and reviews/2026-10-29-interaction-driver/adjudication.md.

This is local d1FIRST-driver progress. A global or uniformly-local Young flow, source-compatible all-order solution identification, growing cone/initial data1, nonzero-profile spectral/event growth, higher-dimensional operators and source-variational constants remain OPEN. The exact original pointwise sharp target, WHITE13/original-class9 and canonical110-page/60-proof TeX/PDF remain unchanged. No new companion/package, Skorohod result, intended source correction, novelty/circulation or canonical-publication claim.

"""
proposal=proposal.replace('## Current state\n\n','## Current state\n\n'+new,1)
proposal=proposal.replace("The interaction driver's time regularity, all-order flow/remainder",'The interaction driver time regularity is now covered by the scoped checkpoint above; all-order flow/remainder',1)
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
prep=json.loads((P/'preparation.json').read_text());prep.update(proposed_page_sha256=sha(proposal.encode()),patch_gzip_sha256=sha(compressed),patch_uncompressed_sha256=sha(patch),interaction_driver_scientific_source=summary['source_revision'],interaction_driver_status='9groups PASS/HIGH;localized d1first-driver Holder/cutoff convergence and finite boxes,not all-order flow/event',interaction_driver_binding='reviews/2026-10-29-interaction-driver/final-status-binding.json',published=False)
(P/'preparation.json').write_text(json.dumps(prep,indent=2)+'\n')
checks=json.loads((P/'local-checks.json').read_text());checks.update(interaction_driver_9high=True,interaction_driver_path_cutoff_convergence=True,interaction_driver_allorder_flow_event_unproved=True,interaction_driver_patch_applies_exactly=True)
(P/'local-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
with (P/'publication-request.md').open('a') as f:f.write('\nPrivate interaction-driver checkpoint added: source b398b77052718adc8ac4f3439a3c738b504aea86,9groups/HIGH. Local d1first-driver Holder/source-cutoff and finite-box result only; all-order flow/event/sharp target open. Exact patch roundtrip/apply verified. Still PRIVATE/unpublished; no queue ticket or canonical write.\n')
assert sha((wiki/rel).read_bytes())==sha(base)
print('Private wiki proposal exact patch/frontmatter/link checks PASS; canonical unchanged.')
