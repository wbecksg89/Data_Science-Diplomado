"""
Desafío 3
● Actualice un usuario llamado morpheus para que tenga un campo llamado
residence igual a zion. Guarde el diccionario de respuesta en una variable llamada
updated_user e imprímala en pantalla.
"""

import requests

url = "https://reqres.in/api/users/883"

payload = "{\r\n    \"name\": \"morpheus\",\r\n    \"residence\": \"zion\",\r\n    \"userId\": 1\r\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
