import requests

endpoint = "http://127.0.0.1:8000/books"

data = {
    'name': 'Before the coffee gets cold',
    'isbn': 5652646327,
    'author': 'Toshikazu Kawaguchi',
    'category': 'Fantasy'
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())