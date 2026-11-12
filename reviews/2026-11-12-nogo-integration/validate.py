"""Validate the no-go chapter, unchanged existing proofs, and paired PDFs."""
from pathlib import Path
import hashlib,json,re,subprocess,os
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[2]
FOLDER=Path(__file__).resolve().parent
BASE='474d678d3d0152a690ad98232769a2ac6e33dc20'
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
def proofs(s):return re.findall(r'\\begin\{proof\}.*?\\end\{proof\}',s,re.S)
mt,rt=sources(main),sources(reader);old_count=new_count=0
for p in sorted(mt):
 path=p.relative_to(ROOT).as_posix();new=proofs(p.read_text());new_count+=len(new)
 if path.startswith('notes/no-go/'):continue
 if path.startswith('notes/figures/nogo-'):
  assert not new
  continue
 old=proofs(subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT,text=True));old_count+=len(old)
 assert old==new,('Existing proof changed',path)
assert(old_count,new_count)==(216,249),(old_count,new_count)
alltext='\n'.join(p.read_text() for p in mt)
ids=re.findall(r'\\label\{P:nogo-(\d+)\}',alltext)
assert sorted(ids)==[f'{i:02}' for i in range(1,34)]
assert alltext.count('\\begin{nogo}')==33
assert main.read_text().index('\\label{S:book-no-go}')<main.read_text().index('\\appendix')
labels={m[1]:line for line in main.with_suffix('.aux').read_text().splitlines() if (m:=re.match(r'\\newlabel\{([^}]+)\}',line))}
assert '{{12}' in labels['S:book-no-go']
for i in range(1,34):assert '{{'+f'{i:02}'+'}' in labels[f'P:nogo-{i:02}']
mp,rp=PdfReader(main.with_suffix('.pdf')),PdfReader(reader.with_suffix('.pdf'))
names=set(mp.named_destinations);links=[]
for pn,page in enumerate(rp.pages,1):
 for ref in page.get('/Annots',[]):
  action=ref.get_object().get('/A',{})
  if action.get('/S')!='/GoToR':continue
  dest=action.get('/D');valid=(isinstance(dest,list) and dest and isinstance(dest[0],int) and 0<=dest[0]<len(mp.pages)) or str(dest) in names
  assert valid,(pn,dest);links.append({'reader_page':pn,'destination':str(dest)})
embedded=reader.read_text().split('\\end{filecontents*}')[0]
for line in embedded.splitlines():
 if m:=re.match(r'\s*\\newlabel\{([^}]+)\}',line):assert line.strip()==labels[m[1]],m[1]
for p in [main,reader]:assert not re.search(r'(^!|Overfull \\|undefined|multiply defined)',p.with_suffix('.log').read_text(),re.M),p
assert all('\t' not in p.read_text() for p in mt|rt)
backlinks={f'{i:02}':[] for i in range(1,34)}
for p in sorted(mt):
 if p.relative_to(ROOT).as_posix().startswith('notes/no-go'):continue
 for key in backlinks:
  if '\\ref{P:nogo-'+key+'}' in p.read_text():backlinks[key].append(p.relative_to(ROOT).as_posix())
assert all(backlinks.values()),backlinks
v=json.loads((ROOT/'notes/figures/VALIDATION.json').read_text())
v.update(SOURCE_DATE_EPOCH=os.environ.get('SOURCE_DATE_EPOCH'),FORCE_SOURCE_DATE=os.environ.get('FORCE_SOURCE_DATE'),schema='nogo-chapter-validation/1',chapters=12,appendices=6,technical_pages=len(mp.pages),reader_pages=len(rp.pages),technical_figures=len(re.findall(r'\\contentsline \{figure\}',main.with_suffix('.lof').read_text())),reader_figures=sum(p.read_text().count('\\begin{figure}')+p.read_text().count('\\begin{wrapfigure}') for p in rt),chapter_openings=16,total_main_tex_inputs=len(mt),all_tex_files_including_reader=len(mt|rt),tex_sources=[{'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)} for p in sorted(mt|rt)],main_tex_sha256=sha(main),main_pdf_sha256=sha(main.with_suffix('.pdf')),reader_tex_sha256=sha(reader),reader_pdf_sha256=sha(reader.with_suffix('.pdf')),technical_proofs=249,proof_text_preserved_ignoring_whitespace=True,proof_preservation_scope='All 216 pre-existing proof bodies byte-identical; 33 additional no-go proofs.',proof_comparison_commit=BASE,unchanged_proof_bodies=216,changed_existing_proof_labels=[],new_proof_labels=[f'P:nogo-{i:02}' for i in range(1,34)],mapped_technical_labels=embedded.count('\\newlabel'),external_pdf_links=len(links),all_external_targets_valid=True,errors=0,undefined_references_citations=0,overfull_boxes=0,tabs=0,editorial_scope_only=False,independent_mathematical_review=False,whole_document_visual_clearance=False,old_review_receipts_transferred=False,completed_local_date='2026-11-12',current_validation_scope='Chapter 12 with 33 numbered no-gos, contextual backlinks, four diagrams, subject index and reader navigation. Build/source validation only; scientific and visual review dispositions are separate.')
# Keep bibliography and component pins current; historical review evidence is not inherited.
v['bibliographies']=[{'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)} for p in [main.with_suffix('.bbl'),reader.with_suffix('.bbl')]]
for x in v.get('book_component_sources',[]):x['sha256']=sha(ROOT/x['path'])
idx=json.loads(subprocess.check_output(['python3','notes/index/generate.py','--verify-index',str(main.with_suffix('.idx')),'--aux',str(main.with_suffix('.aux'))],cwd=ROOT,text=True))
v['subject_index'].update({k:idx[k] for k in ['entry_mappings','index_records','anchors','top_level_headings']})
notation=re.search(r'\\newlabel\{S:notation\}\{\{[^}]*\}\{([^}]+)\}',main.with_suffix('.aux').read_text())
if notation:
 start=int(notation[1]);v['notation_list']['printed_pages']=f'{start}--{start+5}'
index_page=re.search(r'\\contentsline \{chapter\}\{Subject index\}\{(\d+)\}',main.with_suffix('.toc').read_text())
if index_page:v['subject_index']['pages']=len(mp.pages)-mp.page_labels.index(index_page[1])
(FOLDER/'index-verification.json').write_text(json.dumps(idx,indent=2)+'\n')
(FOLDER/'validation.json').write_text(json.dumps(v,indent=2)+'\n')
(ROOT/'notes/figures/VALIDATION.json').write_text(json.dumps(v,indent=2)+'\n')
(FOLDER/'reader-links.json').write_text(json.dumps(links,indent=2)+'\n')
(FOLDER/'backlinks.json').write_text(json.dumps(backlinks,indent=2)+'\n')
print(json.dumps({k:v[k] for k in ['chapters','appendices','technical_pages','reader_pages','technical_proofs','unchanged_proof_bodies','external_pdf_links']},indent=2))
