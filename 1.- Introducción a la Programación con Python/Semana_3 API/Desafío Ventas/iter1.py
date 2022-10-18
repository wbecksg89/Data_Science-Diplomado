
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
1.- Crear el programa iter1.py.
● Se solicita iterar el diccionario ventas y mostrar en pantalla todas las ventas
superiores a 45000 (sólo el valor de la venta).
Se evaluará el output en pantalla.
● El diccionario utilizado para evaluar puede ser distinto y tener más o menos meses.
"""
iter1 = {v for k,v in ventas.items() if v>45000 }
for i in iter1:
    print(i)