import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from modules.port_scanner import scan_port


def test_scan_common_port():
    result = scan_port("127.0.0.1", 22, timeout=1)
    assert "port" in result
    assert result["status"] in ["open", "closed"]


def test_scan_result_structure():
    result = scan_port("127.0.0.1", 80, timeout=1)
    assert "port" in result
    assert "status" in result
    assert "service" in result
