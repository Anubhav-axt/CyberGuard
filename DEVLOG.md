# CyberGuard Development Log

## Project Overview
CyberGuard is a cybersecurity toolkit web application designed to provide essential security analysis tools through a clean, modern web interface.

## Modules

### Password Checker
Analyzes password strength based on length, character variety, common password databases, pattern detection, and entropy calculation.

### Password Generator
Cryptographically secure password generation using Python's `secrets` module with configurable character sets and passphrase support.

### Hash Generator
Multi-algorithm hash generation (MD5, SHA1, SHA256, SHA512, SHA3) with HMAC support.

### Port Scanner
Multi-threaded TCP port scanner with service identification for common ports.

### Phishing Detector
URL analysis using pattern matching, keyword detection, and suspicious TLD checking.

## Architecture
- Flask blueprints for modular route organization
- Separated utility functions and constants
- AJAX-powered form submissions for smooth UX
- SQLite for lightweight persistence
