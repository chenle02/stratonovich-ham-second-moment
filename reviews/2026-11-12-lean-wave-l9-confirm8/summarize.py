import json, os, glob, sys
OUT = os.path.dirname(os.path.abspath(__file__))
lines = ['# Wave L9 re-review round 8 (label assignments, pointer Index): summary', '',
         'Companion 06ee849 (wave-l9/repair; every label in a label cell is an assignment, context labels moved, Index regenerated, docs only; reviewed commit 434a7e2), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision 06ee849. Packets built by scratchpad/build-l9-reconfirm8.py. Checkers at 06ee849: index_category_check.py: Index rows: 186; labels: 185; manuscript labels at a284420: 879; problems: 0; index_check_pointer.py: 0 pairs without a table row, bad []. Every finding below is verbatim from report.json.', '', 'Packets: q1a the 15 kept or new label assignments (ASSIGN) and the 7 other changed rows; q1b the 12 rows with labels moved to (Context: ...) and the 33 cleared no-direct-label cells; q2 the 186-row pointer Index and the Scope/FORMALIZATION rule text; q3 no new overclaim over 434a7e2..06ee849 and over lines 241-854 of the a723987..434a7e2 diff. Retry only on tool failure, recorded in the driver log.', '']
for d in sorted(glob.glob(OUT + '/q*/')):
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
