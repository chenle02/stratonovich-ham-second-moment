import json, os, glob, sys
OUT = os.path.dirname(os.path.abspath(__file__))
lines = ['# Wave L9 re-review round 7 (pointer Index): summary', '',
         'Companion 434a7e2 (wave-l9/repair; pointer Index and section-table repairs, docs only; reviewed commit a723987), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision 434a7e2. Packets built by scratchpad/build-l9-reconfirm7.py. Checkers at 434a7e2: index_category_check.py: Index rows: 177; labels: 176; manuscript labels at a284420: 879; problems: 0; index_check_pointer.py: 0 problems (pairs without a table row 0; bad []). Every finding below is verbatim from report.json.', '', 'Packets: p1 the pointer Index (177 rows, two checks), the Scope description and the FORMALIZATION wording; p2 the 25 changed section-table rows and the 13 rows flagged in round 6 that the agent judged correct (confirm or refute); p3 no new overclaim over the diff a723987..434a7e2 and classification consistency. Retry only on tool failure, recorded in the driver log.', '']
for d in sorted(glob.glob(OUT + '/p*/')):
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
