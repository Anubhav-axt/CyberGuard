import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from modules.password_checker import check_password
from modules.password_generator import generate_password, generate_passphrase


def test_empty_password():
    result = check_password("")
    assert result["score"] == 0
    assert result["strength"] == "None"


def test_weak_password():
    result = check_password("123")
    assert result["score"] <= 3
    assert result["strength"] in ["Very Weak", "Weak"]


def test_strong_password():
    result = check_password("MyStr0ng!P@ssw0rd#2024")
    assert result["score"] >= 6
    assert result["strength"] in ["Strong", "Very Strong"]


def test_common_password():
    result = check_password("password")
    assert result["score"] <= 3


def test_generate_password_length():
    pwd = generate_password(length=32)
    assert len(pwd) == 32


def test_generate_password_charset():
    pwd = generate_password(
        length=20,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_special=True,
    )
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    assert has_upper and has_lower and has_digit and has_special


def test_generate_passphrase():
    phrase = generate_passphrase(word_count=4)
    words = []
    for sep in ["-", ".", "_", " "]:
        words = phrase.split(sep)
        if len(words) == 4:
            break
    assert len(words) == 4
