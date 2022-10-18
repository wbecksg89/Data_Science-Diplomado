"""
Desafío 2
● Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el
diccionario de respuesta en una variable llamada created_user e imprímala en
pantalla.
"""
import requests
import json

url = "https://reqres.in/api/users"

payload = json.dumps({
  "name": "Ignacio",
  "job": "Profesor",
  "userId": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

