import requests

# Target URL (Juice Shop API endpoint)
url = "http://192.168.1.51/rest/user/login"

# Send a request to the endpoint
response = requests.post(url, json={"email": "test@example.com", "password": "password123"})

# Check if sensitive data is exposed in the response
sensitive_keywords = ["password", "api_key", "token"]
for keyword in sensitive_keywords:
    if keyword in response.text:
        print(f"Sensitive Data Exposure Detected: {keyword}")