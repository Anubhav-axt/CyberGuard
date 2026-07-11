import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from modules.hash_generator import generate_hash, generate_all_hashes


def test_sha256_hash():
    result = generate_hash("hello", "sha256")
    expected = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert result["hash"] == expected
    assert result["algorithm"] == "SHA256"


def test_md5_hash():
    result = generate_hash("hello", "md5")
    assert len(result["hash"]) == 32


def test_all_hashes():
    results = generate_all_hashes("test")
    assert "md5" in results
    assert "sha1" in results
    assert "sha256" in results
    assert "sha512" in results


def test_invalid_algorithm():
    result = generate_hash("hello", "invalid")
    assert "error" in result
