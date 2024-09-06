import requests

url = "http://localhost:8000/import_all"
files = {'file': open('D:/myworld/lims_portal/lims_app/all_data.zip', 'rb')}

response = requests.post(url, files=files)
print(response.json())
