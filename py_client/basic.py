import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, params={"id":1}, json={'title':"Apple","price":100, "content":"Iphone"})

print(get_response.json())