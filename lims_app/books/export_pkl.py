import requests

url = "http://localhost:8000/export_pkl"
response = requests.get(url)

with open("all_data.zip", "wb") as file:
    file.write(response.content)