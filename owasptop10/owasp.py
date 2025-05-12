import requests
import json

# Set the target URL (replace with the actual URL of the web app you are testing)
target_url = "http://127.0.0.1:5000/"

# 1. Broken Access Control
def test_broken_access_control():
    # Attempt to access a restricted resource without authentication
    response = requests.get(f"{target_url}/admin")
    if response.status_code == 200:
        print("[!] Potential Broken Access Control: Access to /admin without authorization")
    else:
        print("[-] Access Control seems secure for /admin")

# 2. Cryptographic Failures
def test_cryptographic_failures():
    response = requests.get(target_url)
    if not response.url.startswith("https://"):
        print("[!] Potential Cryptographic Failure: Site does not use HTTPS")
    else:
        print("[-] Site is secured with HTTPS")

# 3. Injection (SQL Injection example)
def test_injection():
    payload = "' OR '1'='1"
    response = requests.get(f"{target_url}/search?query={payload}")
    if "error" in response.text.lower() or "syntax" in response.text.lower():
        print("[!] Potential SQL Injection vulnerability")
    else:
        print("[-] No SQL Injection detected in /search endpoint")

# 4. Insecure Design (basic endpoint discovery)
def test_insecure_design():
    sensitive_endpoints = ["/admin", "/config", "/backup", "/debug"]
    for endpoint in sensitive_endpoints:
        response = requests.get(target_url + endpoint)
        if response.status_code == 200:
            print(f"[!] Potential Insecure Design: Sensitive endpoint {endpoint} is accessible")
        else:
            print(f"[-] Endpoint {endpoint} not accessible")

# 5. Security Misconfiguration
def test_security_misconfiguration():
    # Check for server headers
    response = requests.get(target_url)
    server = response.headers.get("Server", "")
    if server:
        print(f"[!] Security Misconfiguration: Server header is exposed ({server})")
    else:
        print("[-] No Server header exposed")

# 6. Vulnerable and Outdated Components
def test_vulnerable_components():
    # Check for known outdated components (e.g., old libraries in /vendor/)
    known_paths = ["/vendor/", "/lib/", "/static/", "/js/"]
    for path in known_paths:
        response = requests.get(target_url + path)
        if response.status_code == 200:
            print(f"[!] Potential Vulnerable Component: Accessible directory {path}")
        else:
            print(f"[-] No vulnerable component detected at {path}")

# 7. Identification and Authentication Failures
def test_authentication_failures():
    login_data = {"username": "admin", "password": "wrongpassword"}
    response = requests.post(f"{target_url}/login", data=login_data)
    if response.status_code == 200 and "error" not in response.text.lower():
        print("[!] Potential Authentication Failure: Login allowed with invalid credentials")
    else:
        print("[-] Authentication seems secure")

# 8. Software and Data Integrity Failures
def test_software_data_integrity():
    # Test if the application allows code injection (e.g., uploading PHP files in an image upload field)
    files = {"file": ("malicious.php", "<?php echo 'malicious code'; ?>")}
    response = requests.post(f"{target_url}/upload", files=files)
    if response.status_code == 200 and "malicious.php" in response.text:
        print("[!] Potential Software Integrity Failure: Allows file upload without validation")
    else:
        print("[-] File upload seems secure")

# 9. Security Logging and Monitoring Failures
def test_logging_monitoring():
    # Send an invalid request and check if it’s handled
    response = requests.get(f"{target_url}/thispagedoesnotexist")
    if response.status_code == 404:
        print("[-] Monitoring appears to handle 404 errors")
    else:
        print("[!] Monitoring may not be logging all errors correctly")

# 10. Server-Side Request Forgery (SSRF)
def test_ssrf():
    ssrf_payload = {"url": "http://localhost:22"}
    response = requests.post(f"{target_url}/fetch-url", json=ssrf_payload)
    if "connection refused" not in response.text.lower():
        print("[!] Potential SSRF vulnerability")
    else:
        print("[-] No SSRF detected")

# Main test runner
if __name__ == "__main__":
    print("Starting OWASP Top 10 Security Testing...")
    test_broken_access_control()
    test_cryptographic_failures()
    test_injection()
    test_insecure_design()
    test_security_misconfiguration()
    test_vulnerable_components()
    test_authentication_failures()
    test_software_data_integrity()
    test_logging_monitoring()
    test_ssrf()
    print("Testing complete.")

