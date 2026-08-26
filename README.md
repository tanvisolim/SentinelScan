SentinelScan 🔐

SentinelScan is a Flask-based web security scanner that analyzes websites for common security configuration issues.

🚀 Features
🔒 Checks SSL/TLS configuration
🛡️ Checks important HTTP security headers
📊 Generates an overall security score
💡 Provides security recommendations
🌐 Simple and user-friendly web interface
🔍 Security Checks

SentinelScan currently checks:

Strict-Transport-Security (HSTS)
Content-Security-Policy (CSP)
X-Frame-Options
X-Content-Type-Options
Referrer-Policy
SSL/TLS configuration
🛠️ Technologies Used
Python
Flask
HTML
CSS
Requests
Jinja2


Project Structure
SentinelScan/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── scanner/
│   ├── headers_checker.py
│   ├── ssl_checker.py
│   ├── score_engine.py
│   └── recommendations.py
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css


🎯 Purpose

SentinelScan was developed as a cybersecurity project to understand website security headers, SSL/TLS configuration, vulnerability assessment, and automated security scoring.

⚠️ Disclaimer

SentinelScan is intended for educational and authorized security testing purposes only. Only scan websites that you own or have permission to test.

👩‍💻 Author

Tanvi Solim
