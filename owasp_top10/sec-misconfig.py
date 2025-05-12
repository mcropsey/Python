import requests

# Target URL (Juice Shop admin panel)
url = "http://192.168.1.51/admin"

# Send a request to the admin panel
response = requests.get(url)

# Check if the admin panel is accessible
if response.status_code == 200:
    print("Security Misconfiguration Detected: Admin panel is accessible!")
else:
    print("Admin panel is not accessible.")