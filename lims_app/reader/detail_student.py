import requests

endpoint = "http://localhost:8000/readers/1"

get_response = requests.get(endpoint)
print(get_response.json())