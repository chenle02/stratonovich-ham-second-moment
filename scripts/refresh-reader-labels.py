#!/usr/bin/env python3
"""Refresh the reading edition's external labels after building the book."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
READER = ROOT / 'notes/notes_stratonovich_ham_second_moment_reader.tex'
text = READER.read_text()
start = text.index('\n', text.index(r'\begin{filecontents*}')) + 1
end = text.index(r'\end{filecontents*}', start)
keys = set(re.findall(r'\\newlabel\{([^}]+)\}', text[start:end]))
seen = set()

def collect(path):
    if path in seen:
        return
    seen.add(path)
    body = path.read_text()
    keys.update(re.findall(r'\\(?:TNref|ProofRef|GuideRef)\s*\{[^{}]*\}\s*\{([^{}]+)\}', body))
    keys.update(re.findall(r'\\TN\s*\{([^{}]+)\}', body))
    for name in re.findall(r'\\input\{([^}]+)\}', body):
        child = ROOT / (name if name.endswith('.tex') else name + '.tex')
        if child.exists():
            collect(child)

collect(READER)
keys = {key for key in keys if '#' not in key}
aux = (ROOT / 'notes/notes_stratonovich_ham_second_moment.aux').read_text()
labels = {m[1]: line for line in aux.splitlines()
          if (m := re.match(r'\\newlabel\{([^}]+)\}', line))}
missing = keys - labels.keys()
if missing:
    raise SystemExit(f'Missing technical labels: {sorted(missing)}')
READER.write_text(text[:start] + ''.join('  ' + labels[key] + '\n'
                  for key in sorted(keys)) + text[end:])
print(f'{len(keys)} technical labels refreshed from {len(seen)} reader sources')
