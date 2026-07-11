import re
import math
from utils.constants import COMMON_PASSWORDS, WEAK_PATTERNS


def check_password(password):
    """Check password strength. Returns dict with score and details."""
    if not password:
        return {"score": 0, "strength": "None", "color": "#6c757d", "details": ["No password provided"], "entropy": 0}

    score = 0
    details = []
    length = len(password)

    # Length check
    if length >= 8:
        score += 1
        details.append("Good length (8+)")
    if length >= 12:
        score += 1
        details.append("Strong length (12+)")
    if length >= 16:
        score += 1
        details.append("Excellent length (16+)")

    # Character variety
    if re.search(r"[a-z]", password):
        score += 1
    else:
        details.append("No lowercase letters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        details.append("No uppercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        details.append("No numbers")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{}|;':\",./<>?`~]", password):
        score += 1
        details.append("Has special characters")
    else:
        details.append("No special characters")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = max(0, score - 4)
        details.append("⚠ Common password detected!")

    # Weak patterns
    for pattern in WEAK_PATTERNS:
        if re.search(pattern, password.lower()):
            score = max(0, score - 1)
            details.append("⚠ Weak pattern detected")
            break

    # Entropy calculation
    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"\d", password):
        charset_size += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset_size += 32
    entropy = length * math.log2(charset_size) if charset_size > 0 else 0

    if entropy >= 60:
        score += 1
    if entropy >= 80:
        score += 1
    if entropy >= 100:
        score += 1

    # Clamp score
    score = min(score, 10)

    # Strength label
    if score <= 2:
        strength, color = "Very Weak", "#dc3545"
    elif score <= 4:
        strength, color = "Weak", "#fd7e14"
    elif score <= 6:
        strength, color = "Fair", "#ffc107"
    elif score <= 8:
        strength, color = "Strong", "#20c997"
    else:
        strength, color = "Very Strong", "#198754"

    return {
        "score": score,
        "strength": strength,
        "color": color,
        "details": details,
        "entropy": round(entropy, 1),
        "length": length,
    }
