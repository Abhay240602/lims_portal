import requests

endpoint = "http://localhost:8000/books/2/update"

data = {
    'name': "Mahabharat",
    'isbn': 3435353,
}
get_response = requests.patch(endpoint, json=data)
print(get_response.json())