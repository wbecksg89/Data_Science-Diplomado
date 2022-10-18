"""
3.- Se pide crear un programa llamado iter3.py que tenga un método llamado
filter_dict() que reciba un diccionario y devuelva uno nuevo con los valores superiores a
un parámetro que será ingresado al momento de llamar al programa.
"""
n = int(input("Ingrese La CANTIDAD de LLAVES"))
d = {}

for i in range(n):
    keys = input(f'Ingrese la LLAVE {i+1}\n') # here i have taken keys as strings
    values = int(input(f'Ingrese el VALOR {i+1}\n')) # here i have taken values as integers
    d[keys] = values
print(d)

parametro = int(input("Ingrese el parametro a filtrar para recibir los parametros superiores\n"))

def filter_dict(d,parametro):
    result = {v for k,v in d.items() if v>int(parametro) }
    return print(result)

filter_dict(d,parametro)