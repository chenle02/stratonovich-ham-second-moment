"""Pure synthetic Git-response tests; no repository commits or release exports."""
import contextlib,hashlib,importlib.util,io,json,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('indexer',Path(__file__).with_name('index_filtered_reviews.py'));mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class IndexTests(unittest.TestCase):
 def test_versions_links_and_private_refusal(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)/'filtered-fixture';root.mkdir();out=root/'experiment/index';receipt=Path(td)/'fixture-receipt.json';receipt.write_text('{"synthetic_test_only":true}')
   blobs={'a'*40:b'failed fixture report\n','b'*40:b'success fixture report\n','c'*40:b'{"fixture_usage":7}\n'};blocked=[False]
   def entry(oid,path):return ('100644 blob '+oid+'\t'+path).encode()+b'\0'
   def git(args):
    cmd=args[3:]
    if cmd==['rev-parse','--is-inside-work-tree']:return b'true\n'
    if cmd==['rev-parse','HEAD']:return b'2'*40+b'\n'
    if cmd==['log','--all','--format=%H %T']:return (('2'*40+' '+'4'*40+'\n')+('1'*40+' '+'3'*40+'\n')).encode()
    if cmd[:3]==['ls-tree','-rz','--full-tree']:
     tree=cmd[-1];data=entry('a'*40,'reviews/result.txt') if tree=='3'*40 else entry('b'*40,'reviews/result.txt')+entry('c'*40,'telemetry.json')
     return data+(entry('a'*40,'private/fixture.json') if blocked[0] else b'')
    raise AssertionError(cmd)
   class Proc:
    def __init__(self,args,stdout=None):self.stdout=io.BytesIO(blobs[args[-1]])
    def wait(self):return 0
   argv=['indexer','--filtered-root',str(root),'--output',str(out),'--filter-receipt',str(receipt),'--ack-filtered']
   with patch.object(sys,'argv',argv),patch.object(mod.subprocess,'check_output',git),patch.object(mod.subprocess,'Popen',Proc),contextlib.redirect_stdout(io.StringIO()):mod.main()
   d=json.loads((out/'inventory.json').read_text());self.assertEqual(len(d['versions']),3);self.assertEqual(d['reachable_commits_scanned'],2)
   for r in d['versions']:self.assertEqual(r['sha256'],hashlib.sha256(blobs[r['git_blob']]).hexdigest());self.assertEqual(r['content_exported'],False)
   historical=[r for r in d['versions'] if r['git_blob']=='a'*40][0];self.assertIsNone(historical['relative_link'])
   blocked[0]=True
   with patch.object(sys,'argv',argv),patch.object(mod.subprocess,'check_output',git),patch.object(mod.subprocess,'Popen',Proc),self.assertRaises(SystemExit):mod.main()
if __name__=='__main__':unittest.main()
