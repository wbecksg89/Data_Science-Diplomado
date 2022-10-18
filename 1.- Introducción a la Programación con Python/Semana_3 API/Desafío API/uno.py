

"""
Desafío 1
● Obtenga toda la información de los usuarios retornada por la API, guárdela en una
variable llamada users_data e imprímala en pantalla.
"""
import requests
import json


url = 'https://reqres.in/api/users'
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
results = json.loads(response.text)
users_data = results['data']
print(users_data)