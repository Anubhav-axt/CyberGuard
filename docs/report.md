# CyberGuard Security Report

## Tool Descriptions

### Password Strength Analysis
The password checker evaluates passwords using multiple criteria:
- Length scoring (8, 12, 16+ characters)
- Character variety (upper, lower, digits, special)
- Common password database matching
- Sequential and repeated character detection
- Shannon entropy calculation

### Port Scanning Methodology
- TCP connect scan with configurable timeout
- Multi-threaded execution (up to 100 threads)
- Service identification for 22+ common ports
- Range: configurable start/end port (default 1-1024)

### Phishing Detection
URL analysis covers:
- IP address usage instead of domain names
- Suspicious TLDs (.tk, .ml, .ga, etc.)
- Phishing keyword detection
- URL length and structure analysis
- Subdomain count analysis
- URL obfuscation techniques (@ symbol, double slashes)
