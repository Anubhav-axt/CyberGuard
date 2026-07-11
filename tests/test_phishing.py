import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from modules.phishing_detector import analyze_url


def test_safe_url():
    result = analyze_url("https://www.google.com")
    assert result["risk"] in ["Low", "Medium"]
    assert result["score"] <= 3


def test_ip_url():
    result = analyze_url("http://192.168.1.1/login")
    assert result["score"] >= 2


def test_phishing_keywords():
    result = analyze_url("https://secure-verify-account.tk/login")
    assert result["score"] >= 3
    assert result["risk"] in ["High", "Critical"]


def test_empty_url():
    result = analyze_url("")
    assert result["score"] == 0
    assert result["risk"] == "N/A"


def test_long_url():
    result = analyze_url("https://example.com/" + "a" * 200)
    assert result["score"] >= 1
