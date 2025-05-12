import requests

# Target URL
url = "http://192.168.1.51/rest/products/search"

# SQL Injection payload
#payload = {"q": "' OR 1=1 --"}
#try simpler payload
payload = {"q": "apple"}  # A valid search term to test if the endpoint works

# Send the request
response = requests.get(url, params=payload)

# Print the response
print(response.json())