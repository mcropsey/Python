import requests
import sys

def test_proxy(proxy_url, test_url="http://httpbin.org"):
    """
    Sends HTTP traffic through a proxy to test GET and POST requests.

    Args:
        proxy_url (str): Proxy server URL in the format 'http://username:password@proxyserver:port'.
        test_url (str): URL to send requests to (default: httpbin.org).

    """
    # Setup the proxy configuration
    proxies = {
        "http": proxy_url,
        "https": proxy_url,  # Optional if proxy supports HTTPS
    }
    print(f"Testing proxy: {proxy_url}")
    print(f"Sending traffic to test URL: {test_url}\n")

    try:
        # Test GET Request
        print("--- Testing GET request ---")
        response = requests.get(f"{test_url}/get", proxies=proxies)
        print("Response Status Code:", response.status_code)
        print("Response Body:")
        print(response.json())

        # Test POST Request
        print("\n--- Testing POST request ---")
        data = {"key": "value", "proxy_test": True}
        response = requests.post(f"{test_url}/post", data=data, proxies=proxies)
        print("Response Status Code:", response.status_code)
        print("Response Body:")
        print(response.json())

    except requests.exceptions.ProxyError:
        print("[ERROR] Proxy connection failed. Verify the proxy URL and connectivity.")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python test_proxy_http.py <proxy_url>")
        print("Example: python test_proxy_http.py http://username:password@proxyserver:port")
        sys.exit(1)

    proxy_url = sys.argv[1]  # Proxy URL passed as argument

    # You can replace 'http://httpbin.org' with any test server URL
    test_url = "http://74.135.128.147"  # Default test server
    test_proxy(proxy_url, test_url)

