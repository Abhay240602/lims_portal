import requests

endpoint = "http://127.0.0.1:8000/readers"

data = {
    'reference_id': 6762342,
    'reader_name': 'Abhay',
    'reader_contact': 4687324623,
    'reader_address': 'Vegas',
    'books': [2,4]
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())