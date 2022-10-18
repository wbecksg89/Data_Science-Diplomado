"""
Desafío 4
● Elimine un usuario llamado Pepe. Imprima el código de respuesta en pantalla.
"""
import requests
import json

url = "https://reqres.in/api/users/2"

payload = json.dumps({
  "name": "Pepe"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
