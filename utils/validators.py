import re
from urllib.parse import urlparse


def validate_url(url):
    """Validate and parse a URL."""
    if not url:
        return False, "URL cannot be empty"
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        result = urlparse(url)
        if not result.netloc:
            return False, "Invalid URL format"
        return True, url
    except Exception:
        return False, "Invalid URL format"


def validate_target(target):
    """Validate a scan target (IP or hostname)."""
    if not target:
        return False, "Target cannot be empty"
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    hostname_pattern = r"^[a-zA-Z0-9]([a-zA-Z0-9\-\.]*[a-zA-Z0-9])?$"
    if re.match(ip_pattern, target):
        parts = target.split(".")
        if all(0 <= int(p) <= 255 for p in parts):
            return True, target
        return False, "Invalid IP address"
    if re.match(hostname_pattern, target):
        return True, target
    return False, "Invalid target format"


def validate_password(password):
    """Validate password input."""
    if not password:
        return False, "Password cannot be empty"
    if len(password) > 128:
        return False, "Password too long (max 128 characters)"
    return True, password
