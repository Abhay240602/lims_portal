import requests

book_id = input("What is the Book ID you want to delete?")
try:
    book_id = int(book_id)
except:
    book_id = None
    print("Invalid Book ID. Please enter a valid Book ID.")

if book_id:
    endpoint = f"http://localhost:8000/books/{book_id}/delete"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)