# WebInspect
A Python CLI tool for web reconnaissance, server fingerprinting, security header auditing, directory and subdomain enumeration.

This is my first github project. There might be some errors,bugs,and logical mistakes. If so, please feel free to contact me. Thank you

# Features
- Server Fingerprinting
- Security Header Audit
- Directory Enumeration
- Subdomain Enumeration
- Markdown Report Generation

## Installation

Clone the repository:


#bash

git clone https://github.com/tunar-cyber/WebInspect.git

Move into the project:

#bash
cd WebInspect


Install dependencies:

#bash
pip install -r requirements.txt

## Technologies

- Python3
- Requests
- argparse
- urllib.parse
- Colorama

## Usage 

python Webinspect.py enum -u https://example.com

python Webinspect.py enum -u https://example.com -o report.md

python Webinspect.py dir -u https://example.com -w wordlists/common.txt

python Webinspect.py subdomain -u https://example.com -w wordlists/subdomains.txt

## Disclaimer

This project is intended for educational purposes and authorized security assessments only. Always obtain permission before scanning systems that you do not own or administer.

---

## License

MIT License
