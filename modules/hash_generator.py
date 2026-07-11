import hashlib
import hmac


def generate_hash(data, algorithm="sha256"):
    """Generate hash of input data."""
    if isinstance(data, str):
        data = data.encode("utf-8")

    algorithm = algorithm.lower()
    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
        "sha3_256": hashlib.sha3_256,
        "sha3_512": hashlib.sha3_512,
    }

    if algorithm not in algorithms:
        return {"error": f"Unsupported algorithm: {algorithm}"}

    h = algorithms[algorithm](data)
    return {
        "hash": h.hexdigest(),
        "algorithm": algorithm.upper(),
        "length": h.digest_size * 8,
    }


def generate_all_hashes(data):
    """Generate hashes using all available algorithms."""
    results = {}
    for algo in ["md5", "sha1", "sha256", "sha512"]:
        results[algo] = generate_hash(data, algo)
    return results


def hmac_hash(key, data, algorithm="sha256"):
    """Generate HMAC hash."""
    if isinstance(key, str):
        key = key.encode("utf-8")
    if isinstance(data, str):
        data = data.encode("utf-8")

    h = hmac.new(key, data, getattr(hashlib, algorithm))
    return {
        "hmac": h.hexdigest(),
        "algorithm": algorithm.upper(),
    }
