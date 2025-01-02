import requests

endpoint = 'http://localhost:8000/api/products/'
data = {
    'title':'Hp elitebook',
    'price':500
}
response = requests.post(endpoint, json=data)

print(response.json())