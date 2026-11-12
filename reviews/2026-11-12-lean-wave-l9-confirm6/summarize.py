import json, os, glob, sys
OUT = os.path.dirname(os.path.abspath(__file__))
lines = ['# Wave L9 re-review round 6 (Index regenerated per declaration): summary', '',
         'Companion a723987 (wave-l9/repair; round-5 repairs, Index regenerated per declaration, docs only; reviewed commit 350d191), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision a723987. Packets built by scratchpad/build-l9-reconfirm6.py. Mechanical checker at a723987: cells checked: 657; problems: 0. Every finding below is verbatim from report.json.', '', 'Packets: i1-i8 the Index table (657 rows) in pieces of at most 83 rows with every named Lean declaration (statements, original line numbers, module headers); h2a/h2b the round-5 findings (i1-i3; h1, h2, i4, i5) and NO-NEW-OVERCLAIM over the two halves of the ledger diff 350d191..a723987 (h2b also the other files); h3 classification consistency of counts and L8 repairs kept. Retry only on tool failure, recorded in the driver log.', '']
for d in sorted(glob.glob(OUT + '/h*/') + glob.glob(OUT + '/i*/')):
    g = os.path.basename(d.rstrip('/'))
    lines.append(f'## {g}'); lines.append('')
    lines.append('Preflight: contract-check ' + open(d + 'contract-check-1.txt').read().strip() + '; dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt ' + open(d + 'contract-check-2.txt').read().strip()); lines.append('')
    lines.append('Driver log:'); lines.append('```'); lines.append(open(d + 'driver.log').read().rstrip()); lines.append('```')
    atts = sorted(glob.glob(d + 'attempt-*'))
    for a in atts:
        st = open(a + '/STATUS.md').read() if os.path.exists(a + '/STATUS.md') else '(no STATUS.md)'
        lines.append(f'### {os.path.basename(a)}'); lines.append('```'); lines.append(st.strip()); lines.append('```')
    final = atts[-1] if atts else None
    rp = final + '/report.json' if final else None
    if rp and os.path.exists(rp):
        r = json.load(open(rp))
        lines.append(f'Verdict: **{r.get("verdict")}**, confidence: **{r.get("confidence")}** ({os.path.basename(final)})')
        ch = r.get('checks', [])
        from collections import Counter
        lines.append('Check verdicts: ' + ', '.join(f'{k} {v}' for k, v in Counter(c['verdict'] for c in ch).items()) + f' (of {len(ch)})')
        bad = [c for c in ch if c['verdict'] not in ('PASS', 'PASS_WITH_NOTES')]
        if bad:
            lines.append(''); lines.append('Checks not PASS/PASS_WITH_NOTES:')
            for c in bad:
                lines.append(f'- {c["claim"]}: {c["verdict"]}: {c["reason"]}')
        for sev in ('fatal', 'major', 'minor'):
            f = r.get('findings', {}).get(sev, [])
            lines.append(''); lines.append(f'Findings, {sev} ({len(f)}):')
            for x in f:
                lines.append(f'- {x}')
        lines.append(''); lines.append(f'Required repairs ({len(r.get("required_repairs", []))}):')
        for x in r.get('required_repairs', []):
            lines.append(f'- {x}')
        lines.append(''); lines.append(f'Limitations ({len(r.get("limitations", []))}):')
        for x in r.get('limitations', []):
            lines.append(f'- {x}')
    else:
        lines.append('No valid report.json: not a review.')
    lines.append('')
open(OUT + '/SUMMARY.md', 'w').write('\n'.join(lines) + '\n')
print(OUT + '/SUMMARY.md')
