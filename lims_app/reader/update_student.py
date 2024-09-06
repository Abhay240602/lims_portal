import requests

endpoint = "http://localhost:8000/readers/2/update"

data = {
    'reader_name': "Chris",
    'reader_contact': 3435353,
    'books': [2]
}
get_response = requests.patch(endpoint, json=data)
print(get_response.json())