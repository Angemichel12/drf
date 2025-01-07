import requests

endpoint = 'http://localhost:8000/api/products/1/update/'
data = {
    "title":"Monitor updated",
}
response = requests.patch(endpoint, json=data)

print(response.json())