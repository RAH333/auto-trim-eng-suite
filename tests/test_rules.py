"""
Automated continuous quality checks running under pytest frameworks.
"""



import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from core_rules import TrimDesignValidator

def test_rib_validation_pass():
    v = TrimDesignValidator(2.5)
    res = v.validate_rib_thickness(1.3)
    assert res["status"] == "PASS"

def test_rib_validation_fail():
    v = TrimDesignValidator(2.5)
    res = v.validate_rib_thickness(2.0)
    assert res["status"] == "FAIL_SINK_MARK_RISK"
  
