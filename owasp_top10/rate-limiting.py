import requests

# Target URL (Juice Shop login endpoint)
url = "http://192.168.1.51/rest/user/login"

# Payload for login (replace with actual credentials or test data)
payload = {
    "email": "test@example.com",
    "password": "password123"
}

# Number of requests to simulate a brute-force attack
num_requests = 100

for i in range(num_requests):
    response = requests.post(url, json=payload)
    print(f"Request {i+1}: Status Code = {response.status_code}")
    if response.status_code == 429:  # 429 indicates rate limiting is working
        print("Rate limiting detected! Attack blocked.")
        break