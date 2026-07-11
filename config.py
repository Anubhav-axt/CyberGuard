import secrets

class Config:
    SECRET_KEY = secrets.token_hex(32)
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/cyberguard.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT_SCAN_TIMEOUT = 1
    MAX_PASSWORD_LENGTH = 128
    HASH_ALGORITHMS = ["md5", "sha1", "sha256", "sha512"]
