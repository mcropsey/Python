import requests

# Target URL (Juice Shop protected endpoint)
url = "http://192.168.1.51/rest/user/whoami"

# Send request without authentication
response = requests.get(url)

# Check if the resource is accessible without authentication
if response.status_code == 200:
    print("Broken Authentication Vulnerability Detected!")
else:
    print("Authentication is working as expected.")