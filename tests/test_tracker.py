import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.tracker import Tracker,iou
class TrackingTests(unittest.TestCase):
    def test_identity_and_expiry(self):
        t=Tracker();a=t.update([[0,0,10,10]],0)[0]['id'];self.assertEqual(t.update([[1,0,11,10]],1)[0]['id'],a)
        self.assertNotEqual(t.update([[1,0,11,10]],8)[0]['id'],a)
    def test_iou(self):self.assertEqual(iou([0,0,2,2],[0,0,2,2]),1);self.assertEqual(iou([0,0,1,1],[2,2,3,3]),0)
