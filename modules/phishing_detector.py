import re
from urllib.parse import urlparse
from utils.constants import PHISHING_KEYWORDS, SUSPICIOUS_TLDS


def analyze_url(url):
    """Analyze a URL for phishing indicators."""
    if not url:
        return {"score": 0, "risk": "N/A", "flags": ["Empty URL"]}

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)
    flags = []
    score = 0
    domain = parsed.netloc.lower()

    # IP address check
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(ip_pattern, domain.split(":")[0]):
        flags.append("Uses IP address instead of domain")
        score += 3

    # Suspicious TLD
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            flags.append(f"Suspicious TLD: {tld}")
            score += 2
            break

    # Phishing keywords in URL
    url_lower = url.lower()
    found_keywords = [kw for kw in PHISHING_KEYWORDS if kw in url_lower]
    if found_keywords:
        flags.append(f"Phishing keywords found: {', '.join(found_keywords)}")
        score += len(found_keywords)

    # Excessive subdomains
    parts = domain.split(".")
    if len(parts) > 3:
        flags.append("Excessive subdomains")
        score += 1

    # URL length
    if len(url) > 75:
        flags.append(f"Long URL ({len(url)} chars)")
        score += 1
    if len(url) > 150:
        flags.append("Very long URL")
        score += 1

    # @ symbol (used to obscure real URL)
    if "@" in url:
        flags.append("Contains @ symbol (URL obfuscation)")
        score += 2

    # Double slashes in path
    if parsed.path.count("//") > 0:
        flags.append("Double slashes in path")
        score += 1

    # Hyphens in domain
    if domain.count("-") > 2:
        flags.append("Multiple hyphens in domain")
        score += 1

    # Risk level
    if score <= 1:
        risk = "Low"
    elif score <= 3:
        risk = "Medium"
    elif score <= 5:
        risk = "High"
    else:
        risk = "Critical"

    return {
        "url": url,
        "domain": domain,
        "score": score,
        "risk": risk,
        "flags": flags if flags else ["No suspicious indicators found"],
    }
