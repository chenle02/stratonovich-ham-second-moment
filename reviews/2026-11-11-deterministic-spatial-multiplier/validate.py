"""Check the exact scoped proof changes and current paired build artifacts."""
from pathlib import Path
import hashlib,json,re,subprocess
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[2]
FOLDER=Path(__file__).resolve().parent
manifest=json.loads((FOLDER/'candidate-v2/packet-manifest.json').read_text())
BASE=manifest['baseline']
main=ROOT/'notes/notes_stratonovich_ham_second_moment.tex'
reader=ROOT/'notes/notes_stratonovich_ham_second_moment_reader.tex'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sources(p,seen=None):
 seen=set() if seen is None else seen
 if p in seen:return seen
 seen.add(p)
 for name in re.findall(r'\\input\{([^}]+)\}',p.read_text()):
  q=ROOT/(name if name.endswith('.tex') else name+'.tex')
  if q.exists():sources(q,seen)
 return seen
def proof_at(text,label):
 a=text.index('\\label{'+label+'}');a=text.index('\\begin{proof}',a);b=text.index('\\end{proof}',a)+len('\\end{proof}');return text[a:b]
def proof_list(s):return re.findall(r'\\begin\{proof\}.*?\\end\{proof\}',s,re.S)
changed={'notes/notes_stratonovich_ham_second_moment.tex':['L:damped-homogeneous-norms'],'notes/integrated_spatial_occupation.tex':['P:spatial-smooth-ratio']}
added={'notes/integrated_spatial_occupation.tex':['L:spatial-fourier-bound']}
mt,rt=sources(main),sources(reader);old_count=0;new_count=0;unchanged_count=0
for p in sorted(mt):
 path=str(p.relative_to(ROOT));new=p.read_text()
 if not proof_list(new):continue
 old=subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT,text=True)
 old_count+=len(proof_list(old));new_count+=len(proof_list(new))
 for label in changed.get(path,[]):
  a,b=proof_at(old,label),proof_at(new,label);assert a!=b,label
  old=old.replace(a,'',1);new=new.replace(b,'',1)
 for label in added.get(path,[]):new=new.replace(proof_at(new,label),'',1)
 assert proof_list(old)==proof_list(new),path
 unchanged_count+=len(proof_list(old))
assert (old_count,new_count,unchanged_count)==(215,216,213)
# The existing global model and statement labels are not silently weakened.
oldmain=subprocess.check_output(['git','show',BASE+':'+str(main.relative_to(ROOT))],cwd=ROOT,text=True)
pat=r'\\begin\{hypothesis\}\[Homogeneous covariance\].*?\\end\{hypothesis\}'
assert re.search(pat,oldmain,re.S)[0]==re.search(pat,main.read_text(),re.S)[0]
# Concurrent committed Appendix F/G and Preface work may change the containing
# file. Bind the reviewed mathematical region, not unrelated back matter.
packet=(FOLDER/'candidate-v2/packet/TARGET.md').read_text()
region=main.read_text().split('\\section{Recovering the quadratic-exponential bound}',1)[1].split('\\paragraph{Covariance pairings of translated kernels.}',1)[0]
assert ('\\section{Recovering the quadratic-exponential bound}'+region) in packet
spatial=ROOT/'notes/integrated_spatial_occupation.tex'
assert sha(spatial)==manifest['live_sources'][str(spatial.relative_to(ROOT))]

mp,rp=PdfReader(main.with_suffix('.pdf')),PdfReader(reader.with_suffix('.pdf'))
names=set(mp.named_destinations);links=[]
for page_no,page in enumerate(rp.pages,1):
 for ref in page.get('/Annots',[]):
  action=ref.get_object().get('/A',{})
  if action.get('/S')!='/GoToR':continue
  dest=action.get('/D');valid=(isinstance(dest,list) and dest and isinstance(dest[0],int) and 0<=dest[0]<len(mp.pages)) or str(dest) in names
  assert valid,(page_no,dest);links.append({'reader_page':page_no,'destination':str(dest)})
labels={m[1]:line for line in main.with_suffix('.aux').read_text().splitlines() if (m:=re.match(r'\\newlabel\{([^}]+)\}',line))}
embedded=reader.read_text().split('\\end{filecontents*}')[0]
for line in embedded.splitlines():
 if m:=re.match(r'\s*\\newlabel\{([^}]+)\}',line):assert line.strip()==labels[m[1]],m[1]
for p in [main,reader]:assert not re.search(r'(^!|Overfull \\|undefined)',p.with_suffix('.log').read_text(),re.M),p
assert all('\t' not in p.read_text() for p in mt|rt)
v=json.loads((ROOT/'notes/figures/VALIDATION.json').read_text())
v.update(appendices=7, schema='deterministic-spatial-multiplier-validation/1',technical_pages=len(mp.pages),reader_pages=len(rp.pages),total_main_tex_inputs=len(mt),all_tex_files_including_reader=len(mt|rt),tex_sources=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in sorted(mt|rt)],main_tex_sha256=sha(main),main_pdf_sha256=sha(main.with_suffix('.pdf')),reader_tex_sha256=sha(reader),reader_pdf_sha256=sha(reader.with_suffix('.pdf')),bibliographies=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in [main.with_suffix('.bbl'),reader.with_suffix('.bbl')]],technical_proofs=216,proof_text_preserved_ignoring_whitespace=False,proof_comparison_commit=BASE,unchanged_proof_bodies=213,changed_existing_proof_labels=['L:damped-homogeneous-norms','P:spatial-smooth-ratio'],new_proof_labels=['L:spatial-fourier-bound'],mapped_technical_labels=embedded.count('\\newlabel'),external_pdf_links=len(links),all_external_targets_valid=True,errors=0,undefined_references_citations=0,overfull_boxes=0,tabs=0,editorial_scope_only=False,independent_mathematical_review=False,whole_document_visual_clearance=False,old_review_receipts_transferred=False,completed_local_date='2026-11-11',current_validation_scope='Approved deterministic spatial-energy lemma, independent R0 finiteness and precise spectral multiplier/Laplace-domain comparison. This is build/source validation; review disposition is recorded separately in the scoped review directory.')
idx=json.loads((FOLDER/'index-verification.json').read_text())
v['subject_index'].update({k:idx[k] for k in ['entry_mappings','index_records','anchors','top_level_headings']})
notation=re.search(r'\\newlabel\{S:notation\}\{\{[^}]*\}\{([^}]+)\}',main.with_suffix('.aux').read_text())
if notation:
 start=int(notation[1]);v['notation_list']['printed_pages']=str(start)+'--'+str(start+v['notation_list']['pages']-1)
for x in v.get('book_component_sources',[]):x['sha256']=sha(ROOT/x['path'])
(ROOT/'notes/figures/VALIDATION.json').write_text(json.dumps(v,indent=2)+'\n')
(FOLDER/'validation.json').write_text(json.dumps(v,indent=2)+'\n');(FOLDER/'reader-links.json').write_text(json.dumps(links,indent=2)+'\n')
print(json.dumps({k:v[k] for k in ['technical_pages','reader_pages','technical_proofs','unchanged_proof_bodies','external_pdf_links']},indent=2))
