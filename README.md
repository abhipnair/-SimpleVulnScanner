# 🛡️ SimpleVulnScanner

A lightweight, beginner-friendly Web Vulnerability Scanner for detecting SQL Injection (SQLi) and Cross-Site Scripting (XSS) vulnerabilities.
Supports error-based, blind, and time-based blind SQL injection detection.

Built with ❤️ by abhipnair.
## 📜 Features

    🔍 Scan for SQL Injection vulnerabilities:

        Error-based detection

        Blind SQLi detection

        Time-based blind SQLi detection

    🛡️ Scan for Cross-Site Scripting (XSS) vulnerabilities

    ⚡ Simple Command-Line Interface (CLI)

    🖋️ Custom payload files support

    🎯 Lightweight, fast, and easy to use

## 🚀 Installation

### Clone this repository
      git clone https://github.com/abhipnair/SimpleVulnScanner.git

### Navigate into the project directory
      cd SimpleVulnScanner/CLI_Version

### Install dependencies
      pip install -r requirements.txt

requirements.txt
    requests
    beautifulsoup4

## 🎯 Usage

    python3 vulnscanner.py -u <TARGET_URL> -f <FIELD_NAME> -t <TYPE>

Arguments:

    -u or --url : Target URL (e.g., http://example.com/login)

    -f or --field : Form field/input name to test (e.g., username, search, query)

    -t or --type : Type of scan (sql, xss, both)

Examples:

### Scan for SQL Injection vulnerabilities
    python3 vulnscanner.py -u "http://testphp.vulnweb.com/listproducts.php" -f cat -t sql

### Scan for XSS vulnerabilities
    python3 vulnscanner.py -u "http://example.com/search" -f search -t xss

### Scan for both SQLi and XSS
    python3 vulnscanner.py -u "http://example.com/login" -f username -t both


📂 Project Structure

    SimpleVulnScanner/
    ├── CLI_Version/
    │   ├── vulnscanner.py
    │   ├── sql_payloads.txt
    │   ├── xss_payloads.txt
    │   └── requirements.txt
    └── README.md

## ⚠️ Disclaimer

This tool is made for educational purposes and authorized testing only.
Unauthorized use of this scanner against websites without permission is illegal.

By using this tool, you agree:

    You are solely responsible for your actions.

    You will not use it for unlawful activities.

## ✍️ Authors

Made with ❤️ and countless cups of coffee by abhipnair.

## 🛡️ License

This project is licensed under the MIT License.
Author accreditation must be retained in any forks, copies, or usage.
Misuse for illegal activities is strictly prohibited.

See LICENSE file for more details.
