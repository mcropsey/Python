import requests
import random
import time

# Target URL for testing
target_url = "https://172-178-40-122.mycitrixcloud.com/"

# List of user agents to simulate various devices and browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
    "curl/7.68.0",
    "python-requests/2.31.0"
]

# List of IPs to simulate traffic from (use a proxy or header to set them)
source_ips = [
    "192.168.1.1",
    "203.0.113.42",
    "198.51.100.25",
    "172.16.0.50",
    "10.0.0.100"
]

# Headers for requests
def generate_headers():
    return {
        "User-Agent": random.choice(user_agents),
        "X-Forwarded-For": random.choice(source_ips),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

# Random query parameters to simulate different requests
def generate_query_params():
    params = {
        "search": random.choice(["test", "netscaler", "ipreputation", "attack", "random-query"]),
        "id": random.randint(1, 1000),
        "flag": random.choice(["true", "false"])
    }
    return params

# Perform a single HTTPS request
def send_request():
    headers = generate_headers()
    params = generate_query_params()
    try:
        response = requests.get(target_url, headers=headers, params=params, timeout=5)
        print(f"Request sent with IP {headers['X-Forwarded-For']} and User-Agent {headers['User-Agent']}. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Simulate traffic in a loop
def simulate_traffic(num_requests, delay=1):
    for _ in range(num_requests):
        send_request()
        time.sleep(delay)  # Add delay to mimic real-world traffic

if __name__ == "__main__":
    print("Starting HTTPS traffic simulation...")
    simulate_traffic(num_requests=100, delay=2)

