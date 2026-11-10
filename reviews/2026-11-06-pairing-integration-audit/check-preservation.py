#!/usr/bin/env python3
"""Read-only independent custody/preservation audit; stdout is the JSON receipt.

No producer script is imported or executed. Body hashes include only bytes
strictly between begin/end markers, preserving comments/newlines verbatim.
Run from any directory. Source and held draft are never written.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess

BASE = Path(__file__).resolve().parents[3]
RESEARCH = BASE / 'stratonovich-fixed-mask-young-wave'
DRAFT = BASE / 'themeII-pairing-product-envelope-integration-draft-20261105'
MAIN = Path('notes/notes_stratonovich_ham_second_moment.tex')
FORMAL_ENVS = {'theorem', 'lemma', 'proposition', 'corollary', 'conjecture',
               'definition', 'hypothesis', 'remark', 'goal'}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def read(p):
    return p.read_bytes()

def comment_mask(text):
    # Keep offsets intact. A percent is active iff preceded by an even run
    # of backslashes. This is sufficient for the actual TeX corpus; there
    # are no verbatim environments in its formal statements/proofs.
    out = list(text)
    for line_match in re.finditer(r'[^\n]*(?:\n|$)', text):
        line = line_match.group()
        for i, char in enumerate(line):
            if char == '%':
                j = i - 1
                while j >= 0 and line[j] == '\\':
                    j -= 1
                if (i - 1 - j) % 2 == 0:
                    for k in range(i, len(line.rstrip('\n'))):
                        out[line_match.start() + k] = ' '
                    break
    return ''.join(out)

def modules(root):
    found = []
    def walk(rel):
        assert rel not in found, ('repeated include', rel)
        found.append(rel)
        text = read(root / rel).decode()
        for match in re.finditer(r'\\(?:input|include)\{([^}]+)\}', comment_mask(text)):
            child = Path(match.group(1))
            if not child.suffix:
                child = child.with_suffix('.tex')
            walk(child)
    walk(MAIN)
    return found

def parse(root, paths):
    proofs, formals, labels = {}, {}, set()
    for rel in paths:
        text = read(root / rel).decode()
        masked = comment_mask(text)
        labels.update(re.findall(r'\\label\{([^}]+)\}', masked))
        tokens = list(re.finditer(r'\\(begin|end)\{([^}]+)\}', masked))
        stack = []
        for t in tokens:
            side, env = t.groups()
            if side == 'begin':
                stack.append(t)
            else:
                assert stack, ('unmatched end', rel, env)
                start = stack.pop()
                assert start.group(2) == env, ('mismatched env', rel, env)
                if env not in FORMAL_ENVS | {'proof'}:
                    continue
                body = text[start.end():t.start()]
                body_mask = masked[start.end():t.start()]
                line = text.count('\n', 0, start.start()) + 1
                record = {'path': str(rel), 'environment': env, 'line': line,
                          'environment_ordinal': sum(1 for x in tokens if x.start() <= start.start()
                                                     and x.group(1) == 'begin' and x.group(2) == env),
                          'body_sha256': sha(body.encode()), 'body': body}
                if env == 'proof':
                    # The closing statement, not an arbitrary prior reference,
                    # binds each proof to its stable statement owner.
                    refs = re.findall(r'\\ref\{([^}]+)\}', body_mask)
                    assert refs, ('no proof closing owner', rel, line)
                    owner = refs[-1]
                    assert re.search(r'This proves\s+(?:Lemma|Theorem|Proposition|Corollary)',
                                     body_mask[-350:]), ('missing close', owner)
                    assert owner not in proofs, ('duplicate proof owner', owner)
                    record['owner'] = owner
                    proofs[owner] = record
                else:
                    own_labels = re.findall(r'\\label\{([^}]+)\}', body_mask)
                    assert own_labels, ('unlabelled formal', rel, env, line)
                    owner = own_labels[0]
                    assert owner not in formals, ('duplicate formal owner', owner)
                    record['owner'] = owner
                    formals[owner] = record
        assert not stack, ('unclosed env', rel)
    assert set(proofs) <= set(formals), ('proof without formal', set(proofs)-set(formals))
    return proofs, formals, labels

def math_spans(body):
    # Collect top-level inline/bracket and equation/align forms in source
    # order. Explicit environment boundaries avoid conflating prose with math.
    masked = comment_mask(body)
    pattern = re.compile(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath)\}'
                         r'.*?\\end\{\1\}|\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$.*?(?<!\\)\$', re.S)
    return [body[m.start():m.end()] for m in pattern.finditer(masked)]

def no_bodies(record):
    return {k:v for k,v in record.items() if k != 'body'}

def tree_state(root):
    return {str(p.relative_to(root)): sha(read(p))
            for p in sorted(root.rglob('*')) if p.is_file()}

def main():
    original_draft = tree_state(DRAFT)
    original_git = subprocess.check_output(['git','status','--porcelain=v1'], cwd=RESEARCH).decode()
    manifest_bytes = read(DRAFT/'manifest.json')
    assert sha(manifest_bytes) == '7744c7359f02c93560fef6b51782c50ad5fc253eb80bb326d7c6d8dde6656d66'
    manifest = json.loads(manifest_bytes)
    assert len(manifest['members']) == 69
    for item in manifest['members']:
        p = DRAFT / item['file']
        assert p.resolve().is_relative_to(DRAFT.resolve())
        content = read(p)
        assert len(content) == item['bytes'], item['file']
        assert sha(content) == item['sha256'], item['file']
    held = json.loads(read(DRAFT/'HELD.json'))
    assert held['manifest_sha256'] == sha(manifest_bytes)
    assert held['accepted_or_adopted'] is False
    old_paths = modules(RESEARCH)
    new_paths = modules(DRAFT/'build')
    assert old_paths == new_paths and len(old_paths) == 28
    source_before = {str(p): sha(read(RESEARCH/p)) for p in old_paths}
    pins = json.loads(read(DRAFT/'baseline-source-pins.json'))
    pin_map = {r['path']: r['sha256'] for r in pins['source28']}
    assert source_before == pin_map
    old_proofs, old_formals, old_labels = parse(RESEARCH, old_paths)
    new_proofs, new_formals, new_labels = parse(DRAFT/'build', new_paths)
    assert (len(old_proofs),len(new_proofs),len(old_formals),len(new_formals)) == (214,215,240,241)
    assert not set(old_proofs)-set(new_proofs)
    assert not set(old_formals)-set(new_formals)
    assert not old_labels-new_labels
    changed_modules = [str(p) for p in old_paths if read(RESEARCH/p) != read(DRAFT/'build'/p)]
    assert changed_modules == [str(MAIN)]
    changed_proofs = [key for key in old_proofs
                      if old_proofs[key]['body'] != new_proofs[key]['body']]
    expected = {'P:mixed','L:joint-fixed-order','L:crude-corrected','L:vertex-crude','P:envelope'}
    assert set(changed_proofs) == expected
    changed_detail = []
    for key in changed_proofs:
        old, new = old_proofs[key], new_proofs[key]
        before, after = math_spans(old['body']), math_spans(new['body'])
        assert before == after, ('mathematical spans changed',key)
        changed_detail.append({'owner':key,'math_spans_unchanged':len(before),
                               'old':no_bodies(old),'draft':no_bodies(new)})
    changed_formals = [key for key in old_formals
                       if old_formals[key]['body'] != new_formals[key]['body']]
    assert changed_formals == ['R:source-case2-time-shift']
    assert all(old_formals[k]['body']==new_formals[k]['body'] for k in old_proofs)
    assert old_proofs['L:translated-covariance-CS']['body'] == new_proofs['L:translated-covariance-CS']['body']
    added = set(new_proofs)-set(old_proofs)
    assert added == {'L:pairing-product-envelope'}
    assert set(new_formals)-set(old_formals) == added
    new_owner = next(iter(added))
    main_hash = sha(read(DRAFT/'build'/MAIN))
    pdf = DRAFT/'build'/MAIN.with_suffix('.pdf')
    pdf_hash = sha(read(pdf))
    assert main_hash == held['Tex_sha256'] == '516d6a650bdac7d3da68672f37836afd084b651c39553b43d5135d0512e39d14'
    assert pdf_hash == held['PDF_sha256'] == '26f9f4a5ee65b08449cedc41dc34e688d15147f0ab4e3b9d23e4ee3f9a8624f8'
    old_pdf_hash = sha(read(RESEARCH/MAIN.with_suffix('.pdf')))
    assert old_pdf_hash == '096cb3cd4610c91d7dc8718bd56526e777cdd06ebca41651a8955bc230eb2f35'
    pages = int(re.search(r'^Pages:\s+(\d+)',subprocess.check_output(['pdfinfo',str(pdf)],text=True),re.M).group(1))
    assert pages == 267
    assert original_draft == tree_state(DRAFT), 'held draft mutated during audit'
    assert source_before == {str(p):sha(read(RESEARCH/p)) for p in old_paths}
    assert original_git == subprocess.check_output(['git','status','--porcelain=v1'],cwd=RESEARCH).decode()
    return {'kind':'INDEPENDENT_AUTHOR_MECHANICAL_CUSTODY_AND_PRESERVATION_NOT_SCIENTIFIC_ACCEPTANCE',
            'status':'PASS','manifest_members':69,'held_tree_before_after_equal':True,
            'research_source_and_git_status_before_after_equal':True,'source_modules':28,
            'unchanged_modules':27,'changed_modules':changed_modules,
            'baseline_proofs':214,'draft_proofs':215,'unchanged_old_proof_bodies':209,
            'changed_old_proofs':changed_detail,
            'baseline_formals':240,'draft_formals':241,'unchanged_old_formals':239,
            'all_214_owned_statement_bodies_unchanged':True,
            'changed_old_formals':changed_formals,'translated_CS_proof_unchanged':True,
            'new_lemma_statement':no_bodies(new_formals[new_owner]),
            'new_lemma_proof':no_bodies(new_proofs[new_owner]),
            'added_labels':sorted(new_labels-old_labels),'removed_labels':[],
            'draft_tex_sha256':main_hash,'draft_pdf_sha256':pdf_hash,'draft_pdf_pages':pages,
            'baseline_pdf_sha256':old_pdf_hash,
            'limits':['No proof correctness, scientific acceptance, HIGH or whole-paper clearance.',
                      'Math-span equality does not imply prose equivalence or application correctness.',
                      'PDF hash/page identity does not verify all rendered pages.',
                      'No source or held file was written; no model, build, git mutation or Lean job ran.']}

if __name__ == '__main__':
    print(json.dumps(main(),indent=2))
