import requests

endpoint = 'http://localhost:8000/api/products/'
data = {
    'title':'Curry',
    'price':100
}
response = requests.post(endpoint, json=data)

print(response.json())