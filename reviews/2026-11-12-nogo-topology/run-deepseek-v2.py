from pathlib import Path
import subprocess,os,json,time
f=Path('reviews/2026-11-12-nogo-topology');out=f/'deepseek-attempt-01';out.mkdir()
carrier=Path('/tmp/stratonovich-ds-carrier.txt').read_text();env=os.environ.copy();env['OPENCODE_CONFIG']=str(Path(carrier)/'opencode.json');env['OPENCODE_PERMISSION']=json.dumps({'*':'deny'});env['OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX']='131072'
a=['opencode','run','--pure','--dir',carrier,'--agent','artifact-reviewer','--model','deepseek/deepseek-v4-pro','--format','json','--title','nogo-topology-eight-mathematics']
(out/'launch.json').write_text(json.dumps({'argv':a,'category':'paper-review-deepseek','model':'deepseek/deepseek-v4-pro','permission':{'*':'deny'},'fresh_session':True,'source_revision':json.loads((f/'packet-manifest-v2.json').read_text())['source_revision'],'automatic_retry':False},indent=2)+'\n')
start=time.time()
try:r=subprocess.run(a,input=(f/'deepseek-prompt-v2.txt').read_text(),text=True,stdout=(out/'raw.jsonl').open('w'),stderr=(out/'stderr.txt').open('w'),env=env,timeout=3600);code=r.returncode
except subprocess.TimeoutExpired:code=124
(out/'exit.json').write_text(json.dumps({'exit':code,'elapsed_seconds':time.time()-start},indent=2)+'\n');print('DeepSeek review exit',code)
