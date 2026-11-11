#!/usr/bin/env python3
"""Refresh book navigation from actual numbered chapters and compiled labels."""
from pathlib import Path
import json
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
main = ROOT / 'notes/notes_stratonovich_ham_second_moment.tex'
book = pymupdf.open(main.with_suffix('.pdf'))
reader = pymupdf.open(ROOT / 'notes/notes_stratonovich_ham_second_moment_reader.pdf')
aux = main.with_suffix('.aux').read_text()
labels = {m[1]: (m[2], m[3]) for m in re.finditer(
    r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}', aux)}
chapters = re.findall(r'\\chapter\{([^}]+)\}\s*\\label\{([^}]+)\}', main.read_text())
if not chapters:
    raise SystemExit('No numbered chapter labels found')
outline = book.get_toc()
resolved = []
for title, key in chapters:
    number, printed = labels[key]
    hits = [row for row in outline if row[0] == 1 and row[1] == f'{number} {title}']
    if len(hits) != 1:
        raise SystemExit(f'Chapter outline mismatch: {key}: {hits}')
    resolved.append((number, title, printed, hits[0][2]))
bibliography = [row[2] for row in outline if row[0] == 1 and row[1] == 'Bibliography']
if len(bibliography) != 1:
    raise SystemExit('Expected one bibliography in the book outline')
rows = []
for i, (number, title, printed, _) in enumerate(resolved):
    next_page = resolved[i + 1][3] if i + 1 < len(resolved) else bibliography[0]
    end = book[next_page - 2].get_label()
    rows.append(f'| {number} | {title} | {printed}–{end} |')
p = ROOT / 'notes/BOOK-GUIDE.md'
s = p.read_text()
header = '| Chapter | Topic | Printed pages |\n|---|---|---|\n'
a = s.index(header) + len(header)
b = s.index('\n\n', a)
s = s[:a] + '\n'.join(rows) + s[b:]
s = re.sub(r'The book has \*\*\d+ pages,', f'The book has **{len(book)} pages,', s)
s = re.sub(r'\*\*\d+ pages\*\*', f'**{len(reader)} pages**', s)
s = re.sub(r'contains \d+ pages', f'contains {len(book) + len(reader)} pages', s)
p.write_text(s)
p = ROOT / 'notes/book-numbering-map.json'
data = json.loads(p.read_text())
def refresh(item):
    if isinstance(item, dict):
        if item.get('label') in labels and 'new_number' in item:
            item['new_number'], item['new_page'] = labels[item['label']]
        for child in item.values():
            refresh(child)
    elif isinstance(item, list):
        for child in item:
            refresh(child)
refresh(data)
p.write_text(json.dumps(data, indent=2) + '\n')
print(f'{len(resolved)} numbered chapter/appendix rows; book {len(book)}, reader {len(reader)} pages')
