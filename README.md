# CyberGuard

A comprehensive cybersecurity toolkit web application built with Flask.

## Features

- **Password Checker** - Analyze password strength with entropy calculations
- **Password Generator** - Generate secure passwords and passphrases
- **Hash Generator** - Create hashes using MD5, SHA1, SHA256, SHA512
- **Port Scanner** - Scan target systems for open ports
- **Phishing Detector** - Analyze URLs for phishing indicators

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Tech Stack

- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML5, Tailwind CSS, JavaScript
- **Database:** SQLite
