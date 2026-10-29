"""Freeze the independent fixed-order construction; preserve exact prior image cohort."""
from pathlib import Path
import hashlib,json,re,shutil,subprocess,gzip
R=Path(__file__).resolve().parent;ROOT=R.parents[1]
P=R/'packet-v1';assert not P.exists();P.mkdir()
old=ROOT/'reviews/2026-10-29-mild-construction'
src=ROOT/'notes/notes_stratonovich_ham_second_moment.tex';s=src.read_text()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
# Required texts contain the whole construction, original hypotheses, and every
# changed downstream proof. Full canonical source/PDF provide optional context.
end=s.index(r'\section{G2 upper bounds for spatial exponents at most one}')
(P/'construction.txt').write_text(s[:end].rstrip()+'\n')
binding=json.loads((R/'change-binding.json').read_text())
consumer=[]
for key in binding['changed_existing_proofs']:
 pos=s.index(r'\label{'+key+'}')
 a=s.index(r'\begin{proof}',pos);b=s.index(r'\end{proof}',a)+len(r'\end{proof}')
 if b>end:
  # Include the formal statement preceding its proof; changes only concern the
  # target construction input, not the retained quantitative argument.
  env=max(s.rfind(r'\begin{'+x+'}',0,pos) for x in ['proposition','theorem','lemma'])
  consumer.append('CANONICAL CONSUMER '+key+'\n'+s[env:b])
(P/'consumers.txt').write_text('\n\n'.join(consumer)+'\n')
for a,b in [(src,'canonical.tex'),(src.with_suffix('.pdf'),'canonical.pdf'),(src.with_suffix('.bbl'),'references.bbl'),(ROOT/'PROJECT-GOAL.md','project-goal.md'),(R/'change-binding.json','change-binding.json')]:shutil.copyfile(a,P/b)
req=[{'path':x} for x in ['construction.txt','consumers.txt','project-goal.md','change-binding.json','construction-map.md','laplace-construction-screen.py','laplace-construction-screen.json']]
images=[x for x in json.loads((old/'required-v1.json').read_text()) if x.get('kind')=='image'];assert len(images)==36
for row in images:
 f=old/'packet-v1'/row['path'];assert sha(f)==row['sha256'];shutil.copyfile(f,P/f.name)
req+=images
for name in ['chen-current-author.pdf','crouzeix-palencia-v1.pdf','chen-hu-2025.pdf','chen-2023.pdf','source-excerpts.txt','author-section4.txt']:
 shutil.copyfile(old/'packet-v1'/name,P/name)
for name in ['laplace-construction-screen.py','laplace-construction-screen.json']:
 shutil.copyfile(ROOT/'reviews/2026-10-29-full-upper-cold-v6/source-proof-audit'/name,P/name)
(P/'construction-map.md').write_text('''Scope: independent fixed-order construction under the ORIGINAL homogeneous
nonnegative even positive-definite tempered RADON covariance/spectral class,
d1,2,3 including white-space endpoint. No nonhomogeneous theorem, uniqueness,
sharp constant, source normalization correction or novelty claimed.

Three unreviewed proofs need audit: L:damped-homogeneous-norms (written in
previous checkpoint), L:spatial-wick-measures, L:joint-fixed-order. The mixed
proof is simplified from the known-result/colour argument. Twelve existing
proofs have construction-consumer changes; 37 existing proofs are byte equal
to ebe4852. Every old formal statement is byte equal at this baseline.
The change-binding machine comparison is supplied; it is not proof acceptance.

Construction uses ONLY imported universal Chen Theorem3.1(3.6),pp14--15,
not the source fixed-order Theorem4.1/Lemma4.4/AppendixA.1. The joint Gaussian
regularizations, Green-before-noise convention and multiple Stratonovich
integral are the source DEFINITIONS. In source(3.5), the covariance quadratic
form uses the two independent spatial integration variables, as defined in
our norms. Finite Gaussian-weighted spectral measures, temporal Laplace
intervals and marked-edge norm factors must meet the actual theorem.
The36source PNGs are unchanged from an earlier carrier calibration. Required
actual delivery must still be proved by THIS attempt's own read ledger.
Old calibration is neither scientific review nor current-source reading.

Dependency graph: direct norm lemma + positive Brownian/heat mass bound ->
spatial weak measure -> marked temporal tail -> joint Gaussian L2 limits.
Then q_n/crude -> mild construction. P:mixed uses that independent branch.
Main moment passage uses joint fixed-order + its OWN amplitude2geometric
tails and amplitude1moment bound; covariance-dependent construction constants
must never enter its parameter-only upper constant. No circular use of the
mixed expansion or sourceSection5 uniform bounds constructs the fixed orders.

The finite white cross/self Laplace diagnostics and homogeneous boundary
negative control are falsification evidence only, not convergence proofs.
Book-edition custody is unresolved; no book-numbered result is imported.
The finite-measure Laplace continuity/tightness argument is written directly.
Optional complete PDFs/source tex give context; availability is not coverage.
''')
dump(R/'required-v1.json',req)
dump(R/'manifest-v1.json',{p.name:sha(p) for p in sorted(P.iterdir()) if p.is_file()})
(R/'build-driver.txt.gz').write_bytes(gzip.compress(Path('<HOME>/.local/state/tmp/stratonovich-construction-build.txt').read_bytes(),mtime=0))
print(json.dumps({'required_texts':len(req)-len(images),'images':len(images),'packet_members':len(list(P.iterdir())),'pages':binding['pages'],'proofs':binding['proofs']}))
