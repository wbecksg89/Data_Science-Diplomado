"""
6.- Generar programa agrupados.py.
● Se solicita generar un diccionario con "n" claves, una para cada posible valor de
venta dentro del diccionario.
● Para cada clave generada, se debe indicar cuántas veces estuvo presente ese valor
"""

from itertools import groupby
valor = [ i for i in ventas.values()]
valor.sort()
res6 = {k:len(list(v)) for k,v in groupby(valor)}
res6