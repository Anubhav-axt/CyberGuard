import secrets
import string


def generate_password(length=16, use_uppercase=True, use_lowercase=True,
                      use_numbers=True, use_special=True):
    """Generate a secure random password."""
    charset = ""
    required = []

    if use_lowercase:
        charset += string.ascii_lowercase
        required.append(secrets.choice(string.ascii_lowercase))
    if use_uppercase:
        charset += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        charset += string.digits
        required.append(secrets.choice(string.digits))
    if use_special:
        special = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        charset += special
        required.append(secrets.choice(special))

    if not charset:
        charset = string.ascii_letters + string.digits
        required = [secrets.choice(charset)]

    length = max(length, len(required))
    remaining = [secrets.choice(charset) for _ in range(length - len(required))]
    password_chars = required + remaining

    # Shuffle using Fisher-Yates via secrets
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def generate_passphrase(word_count=4):
    """Generate a passphrase using common English words."""
    word_list = [
        "alpha", "bravo", "cache", "delta", "echo", "flask", "gamma",
        "hydra", "index", "julia", "kilo", "lemon", "matrix", "nexus",
        "omega", "proxy", "qubit", "radar", "sigma", "tower", "ultra",
        "vector", "whiskey", "xenon", "yacht", "zenith", "anchor",
        "binary", "cipher", "drift", "ember", "forge", "glitch",
        "haven", "ivory", "joker", "karma", "lunar", "marsh",
        "nerve", "orbit", "prism", "quest", "rogue", "stealth",
        "token", "unity", "vault", "warden", "xray", "yield",
    ]
    words = [secrets.choice(word_list) for _ in range(word_count)]
    separator = secrets.choice(["-", ".", "_", " "])
    return separator.join(words)
