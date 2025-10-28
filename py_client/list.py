import requests
from getpass import getpass

password = getpass("Enter admin password: ")
authorization_token = requests.post('http://localhost:8000/api/auth/', data={'username':'admin', 'password':password}).json().get('token')
if authorization_token is not None:
    headers ={
    'Authorization': f'Bearer {authorization_token}'
    }
    endpoint = 'http://localhost:8000/api/products/'

    response = requests.get(endpoint, headers=headers)

    print(response.json())