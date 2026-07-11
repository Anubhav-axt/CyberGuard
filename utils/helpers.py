import hashlib
import time
from functools import wraps


def timer(func):
    """Decorator to measure execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        return result, elapsed
    return wrapper


def format_time(seconds):
    """Format seconds into human readable string."""
    if seconds < 0.001:
        return f"{seconds*1000000:.0f}µs"
    if seconds < 1:
        return f"{seconds*1000:.1f}ms"
    return f"{seconds:.2f}s"


def safe_int(value, default=0):
    """Safely convert to int."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default
