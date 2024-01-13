import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.detection import detections
class DetectorTests(unittest.TestCase):
    def test_empty_frame(self):self.assertEqual(detections({}),[])
    def test_invalid_box(self):
        with self.assertRaises(ValueError):detections({'boxes':[[2,2,1,1]]})
