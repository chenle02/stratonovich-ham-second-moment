#!/usr/bin/env python3
"""Generate and validate the curated index and notation files (standard library)."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[2]
FOLDER = Path(__file__).resolve().parent
MAIN = ROOT / 'notes/notes_stratonovich_ham_second_moment.tex'


def sources(path: Path, seen: set[Path] | None = None) -> set[Path]:
    seen = set() if seen is None else seen
    if path in seen:
        return seen
    seen.add(path)
    for name in re.findall(r'\\input\{([^}]+)\}', path.read_text()):
        child = ROOT / (name if name.endswith('.tex') else name + '.tex')
        if child.exists():
            sources(child, seen)
    return seen


def source_labels() -> dict[str, list[dict[str, str | int]]]:
    result = defaultdict(list)
    for path in sorted(sources(MAIN)):
        text = path.read_text()
        for match in re.finditer(r'\\label\{([^}]+)\}', text):
            result[match[1]].append({
                'path': str(path.relative_to(ROOT)),
                'line': text[:match.start()].count('\n') + 1,
            })
    return dict(result)


def reference_keys(text: str) -> list[str]:
    return re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', text)


def wrap(text: str, indent: str = '') -> str:
    return '\n'.join(textwrap.wrap(
        text, width=80, initial_indent=indent, subsequent_indent=indent,
        break_long_words=False, break_on_hyphens=False))


def notation_tex(groups: list[dict]) -> str:
    lines = [
        '% Selected notation with explicit scope and definition links.',
        '% Generated from notes/index/notation.json.',
        '\\chapter*{List of notation}',
        '\\addcontentsline{toc}{chapter}{List of notation}',
        '\\markboth{List of notation}{List of notation}',
        '\\label{S:notation}',
        '',
        'The tables collect recurring notation and point to its definition or',
        'principal use. Symbols introduced for one calculation are defined there.',
        'Several letters are reused in different sections; the scope column records',
        'the main distinctions. These tables do not add assumptions to the model.',
        '',
        '\\begingroup',
        '\\small',
        '\\setlength{\\LTpre}{0pt}',
        '\\setlength{\\LTpost}{12pt}',
    ]
    for group in groups:
        lines += [
            '', '\\Needspace{8\\baselineskip}', '\\section*{' + group['title'] + '}',
            '\\begin{longtable}{@{}>{\\raggedright\\arraybackslash}p{0.20\\textwidth}',
            '  >{\\raggedright\\arraybackslash}p{0.49\\textwidth}',
            '  >{\\raggedright\\arraybackslash}p{0.25\\textwidth}@{}}',
            '  \\toprule',
            '  Symbol & Meaning and scope & Definition or use \\\\',
            '  \\midrule',
            '  \\endfirsthead',
            '  \\toprule',
            '  Symbol & Meaning and scope & Definition or use \\\\',
            '  \\midrule',
            '  \\endhead',
            '  \\midrule',
            '  \\multicolumn{3}{r}{\\emph{Continued on the next page}} \\\\',
            '  \\endfoot',
            '  \\bottomrule',
            '  \\endlastfoot',
        ]
        for row in group['rows']:
            lines += [
                wrap(row['symbol'] + ' &', '  '),
                wrap(row['meaning'] + ' &', '  '),
                wrap(row['reference'] + r' \\[5pt]', '  '),
            ]
        lines.append('\\end{longtable}')
    lines += ['\\endgroup', '']
    return '\n'.join(lines)


def normalize_idx_entry(entry: str) -> str:
    if entry.endswith('|hyperpage'):
        return entry[:-len('|hyperpage')]
    match = re.search(r'\|hyperxindexformat\{\\(see|seealso)\{(.*)\}\}$', entry)
    if match:
        return entry[:match.start()] + '|' + match[1] + '{' + match[2] + '}'
    return entry


def brace_argument(text: str, start: int) -> tuple[str, int]:
    assert text[start] == '{'
    depth = 1
    pos = start + 1
    while pos < len(text):
        if text[pos] == '{':
            depth += 1
        elif text[pos] == '}':
            depth -= 1
            if not depth:
                return text[start + 1:pos], pos + 1
        pos += 1
    raise ValueError('Unclosed index argument')


def verify_compiled(rows: list[dict], idx: Path, aux: Path) -> dict:
    page_by_label = dict(re.findall(
        r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{([^}]+)\}', aux.read_text()))
    expected = Counter()
    for row in rows:
        for anchor in row['anchors']:
            if anchor not in page_by_label:
                raise ValueError('Missing compiled label: ' + anchor)
            expected[(row['entry'], page_by_label[anchor])] += 1
    actual = Counter()
    for line in idx.read_text().splitlines():
        if not line.startswith('\\indexentry{'):
            continue
        entry, pos = brace_argument(line, len('\\indexentry'))
        page, _ = brace_argument(line, pos)
        actual[(normalize_idx_entry(entry), page)] += 1
    if actual != expected:
        raise ValueError(json.dumps({
            'missing': list((expected - actual).items()),
            'unexpected': list((actual - expected).items()),
        }, indent=2))
    return {'index_records': sum(actual.values()), 'page_correspondence': 'PASS'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='write generated TeX and refreshed source locations')
    parser.add_argument('--verify-index', type=Path, help='check every emitted record against the compiled label page')
    parser.add_argument('--aux', type=Path, default=MAIN.with_suffix('.aux'))
    args = parser.parse_args()
    rows = json.loads((FOLDER / 'entries.json').read_text())
    groups = json.loads((FOLDER / 'notation.json').read_text())
    labels = source_labels()
    seen_pairs = set()
    by_anchor = defaultdict(list)
    targets = set()
    for row in rows:
        target = row['entry'].split('|', 1)[0]
        if '|' not in row['entry']:
            levels = target.split('!')
            targets.add(', '.join(level.split('@')[-1] for level in levels))
            targets.add(levels[0].split('@')[-1])
        if not row['anchors']:
            raise ValueError('Unanchored entry: ' + row['entry'])
        locations = []
        for anchor in row['anchors']:
            if anchor not in labels:
                raise ValueError('Unknown index anchor: ' + anchor)
            if len(labels[anchor]) != 1:
                raise ValueError('Nonunique source anchor: ' + anchor)
            pair = (row['entry'], anchor)
            if pair in seen_pairs:
                raise ValueError('Duplicate entry/anchor: ' + repr(pair))
            seen_pairs.add(pair)
            by_anchor[anchor].append(row['entry'])
            locations.append({'label': anchor, **labels[anchor][0]})
        row['locations'] = locations
    for row in rows:
        if match := re.search(r'\|(see|seealso)\{(.*)\}$', row['entry']):
            if match[2] not in targets:
                raise ValueError('Missing cross-reference target: ' + match[2])
    notation_locations = []
    for group in groups:
        for row in group['rows']:
            refs = reference_keys(row['reference'])
            if not refs:
                raise ValueError('Notation without source reference: ' + row['symbol'])
            for key in refs:
                if key not in labels:
                    raise ValueError('Unknown notation reference: ' + key)
            notation_locations.append({
                'group': group['title'], 'symbol': row['symbol'],
                'locations': [{'label': key, **labels[key][0]} for key in refs],
            })
    lines = [
        '% Curated subject entries attached to existing document labels.',
        '% Generated from notes/index/entries.json; see notes/index/README.md.',
    ]
    for anchor in sorted(by_anchor):
        lines.append('\\SubjectIndexAt{' + anchor + '}{%')
        lines.extend('\\index{' + entry + '}%' for entry in by_anchor[anchor])
        lines.append('}')
    outputs = {
        'anchors.tex': '\n'.join(lines) + '\n',
        'list-of-notation.tex': notation_tex(groups),
    }
    if args.write:
        for name, text in outputs.items():
            (FOLDER / name).write_text(text)
        (FOLDER / 'entries.json').write_text(json.dumps(rows, indent=2) + '\n')
        (FOLDER / 'notation-locations.json').write_text(json.dumps(notation_locations, indent=2) + '\n')
    else:
        for name, text in outputs.items():
            if (FOLDER / name).read_text() != text:
                raise ValueError('Generated file differs; run --write: ' + name)
    summary = {
        'entry_mappings': len(rows),
        'index_records': len(seen_pairs),
        'anchors': len(by_anchor),
        'top_level_headings': len({r['entry'].split('!')[0].split('|')[0].split('@')[-1] for r in rows}),
        'notation_groups': len(groups),
        'notation_rows': sum(len(g['rows']) for g in groups),
        'indexed_source_files': sorted({loc['path'] for r in rows for loc in r['locations']}),
    }
    if args.verify_index:
        summary['compiled'] = verify_compiled(rows, args.verify_index, args.aux)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, ValueError) as exc:
        sys.exit(str(exc))
