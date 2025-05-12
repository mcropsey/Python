import requests

# Target URL (Juice Shop login endpoint)
url = "http://192.168.1.51/rest/user/login"

# Send multiple failed login attempts
for i in range(10):
    payload = {
        "email": f"test{i}@example.com",
        "password": "wrongpassword"
    }
    response = requests.post(url, json=payload)
    print(f"Failed Login Attempt {i+1}: Status Code = {response.status_code}")

# Check if logs are generated (manually verify logs on the server)
print("Verify if logs were generated for failed login attempts.")