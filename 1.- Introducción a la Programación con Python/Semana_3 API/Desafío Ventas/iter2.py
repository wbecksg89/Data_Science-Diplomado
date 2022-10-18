
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

"""
2.- Iterar el diccionario ventas y mostrar en pantalla todos los meses cuyas ventas sean
superiores a 45000.
"""
iter2 = {k for k,v in ventas.items() if v>45000 }
for i in iter2:
    print(i)