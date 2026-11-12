import json, os, glob, sys
OUT = os.path.dirname(os.path.abspath(__file__))
lines = ['# Wave L9 final confirmation (round 9): summary', '',
         'Companion 6d108c0 (wave-l9/repair; convention text, step_Q, 55 rows repaired after the lost-disclosure check, docs only; reviewed commit 06ee849), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision 6d108c0. Packets built by scratchpad/build-l9-reconfirm9.py. Lost-disclosure check re-run at 6d108c0 (identical output): 657 removed Index rows, 376 checks, 291 row, 85 section, 0 lost. Pointer checker: Index rows 186, problems 0; table checker totals 2468/1300/1168. Section-level sample: seed 20261112, stratified by module (packet f4, tools/section-sample.txt). Every finding below is verbatim from report.json.', '', 'Packets: f1 convention text and the step_Q row; f2/f3 the 55 repaired section-table rows (28 + 27) with full Lean modules and TeX with proofs; f4 25 sampled section-level matches and no new overclaim over 06ee849..6d108c0. Retry only on tool failure, recorded in the driver log.', '']
for d in sorted(glob.glob(OUT + '/f*/')):
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
