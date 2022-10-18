"""
4.- Crear un programa llamado busqueda.py que pueda buscar a cuál mes pertenece una o
más cifras específicas. En caso de no encontrarlo mostrar el mensaje "no encontrado".
"""
import sys

lista = sys.argv[1:]
busqueda = {v:k for k,v in ventas.items()}
#lista = [15000,31000,27000,22000]

for i in lista:
    if i in busqueda:
        print(busqueda[i])
    else:
        print("no encontrado")
