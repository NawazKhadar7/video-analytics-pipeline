import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
import asyncio
from syslab.ingestion import ingest
class IngestTests(unittest.TestCase):
    def test_drop_conservation(self):
        case={'id':'test','family':'overload','size':2,'seed':1};r=run_case(case)['metrics']
        self.assertEqual(r['processed']+r['dropped'],24);self.assertGreater(r['dropped'],0)
    def test_backpressure_no_loss(self):self.assertEqual(run_case({'id':'a','family':'steady','size':2,'seed':1})['metrics']['dropped'],0)
