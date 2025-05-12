import requests
import threading
import time

# Target URL
TARGET_URL = "http://192.168.1.33"  # Replace with your target URL
NUMBER_OF_REQUESTS = 10000  # Number of requests to send
THREAD_COUNT = 10  # Number of concurrent threads

def send_request(thread_id):
    """Function to send a GET request to the target URL."""
    try:
        response = requests.get(TARGET_URL)
        print(f"Thread {thread_id}: Status Code: {response.status_code}, Response Time: {response.elapsed.total_seconds()}s")
    except requests.exceptions.RequestException as e:
        print(f"Thread {thread_id}: Error - {e}")

def simulate_traffic():
    """Simulate web traffic by sending multiple requests."""
    threads = []
    
    for i in range(NUMBER_OF_REQUESTS):
        thread = threading.Thread(target=send_request, args=(i,))
        threads.append(thread)
        thread.start()
        
        # To limit the number of concurrent threads
        if len(threads) >= THREAD_COUNT:
            for t in threads:
                t.join()  # Wait for all threads to finish
            threads = []  # Reset threads list

    # Wait for remaining threads to finish
    for t in threads:
        t.join()

if __name__ == "__main__":
    start_time = time.time()
    print("Starting web traffic simulation...")
    simulate_traffic()
    end_time = time.time()
    print(f"Simulation completed in {end_time - start_time:.2f} seconds.")

