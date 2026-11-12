from pathlib import Path
import json,sys,hashlib
sys.path.insert(0,'<HOME>/.claude/bin')
from review_report_contract import parse_report_text
b=Path(__file__).parent;out=b/'deepseek-confirmation-01';events=[json.loads(x) for x in (out/'raw.jsonl').read_text().splitlines()]
texts=[e['part']['text'] for e in events if e.get('type')=='text'];raw=''.join(texts)
(out/'public-report.txt').write_text(raw)
sessions=sorted({e['sessionID'] for e in events if 'sessionID' in e})
meta={'sessions':sessions,'event_types':sorted({e.get('type','') for e in events}),'tool_events':[e.get('type') for e in events if 'tool' in e.get('type','')],'public_bytes':len(raw.encode()),'raw_sha256':hashlib.sha256((out/'raw.jsonl').read_bytes()).hexdigest()}
try:
 v=parse_report_text(raw);r=v.report
 meta.update({'schema_valid':True,'verdict':v.verdict,'confidence':v.confidence,'check_ids':[x.get('id') for x in r['checks']]})
 (out/'report.json').write_text(json.dumps(r,indent=2)+'\n')
except Exception as e:meta.update({'schema_valid':False,'error':str(e)})
(out/'collection.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta,indent=2))
