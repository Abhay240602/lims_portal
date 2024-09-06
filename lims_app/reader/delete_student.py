import requests

reader_id = input("What is the reader ID you want to delete?")
try:
    reader_id = int(reader_id)
except:
    reader_id = None
    print("Invalid reader ID. Please enter a valid reader ID.")

if reader_id:
    endpoint = f"http://localhost:8000/readers/{reader_id}/delete"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)