import requests

# Target URL (Juice Shop version endpoint)
url = "http://192.168.1.51/rest/version"

# Send a request to get the application version
response = requests.get(url)

# Check if the version is vulnerable
vulnerable_versions = ["1.0.0", "2.0.0"]  # Replace with actual vulnerable versions
app_version = response.json().get("version")

if app_version in vulnerable_versions:
    print(f"Vulnerable Component Detected: Version {app_version} is vulnerable!")
else:
    print("No Known Vulnerable Components Found.")