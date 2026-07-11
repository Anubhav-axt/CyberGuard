COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "passw0rd", "shadow", "123123", "654321",
    "superman", "qazwsx", "michael", "football", "password1",
]

WEAK_PATTERNS = [
    r"(.)\1{2,}",      # 3+ repeated chars
    r"^(012|123|234|345|456|567|678|789)",  # sequential numbers
    r"^(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)",  # sequential letters
]

PHISHING_KEYWORDS = [
    "verify", "account", "suspend", "urgent", "click here",
    "update", "confirm", "security", "login", "bank",
    "paypal", "amazon", "apple", "microsoft", "netflix",
]

SUSPICIOUS_TLDS = [
    ".tk", ".ml", ".ga", ".cf", ".gq", ".buzz", ".xyz",
    ".top", ".work", ".click", ".link",
]

PORT_COMMON = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    111: "RPCBind",
    135: "MSRPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Proxy",
}
