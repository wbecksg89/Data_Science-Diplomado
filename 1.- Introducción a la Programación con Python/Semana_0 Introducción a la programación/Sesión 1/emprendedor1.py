
"""
Utilizando argv:
Crear programa en donde muestre las utilidades en base al 
ingreso de 3 variables:
1.- Precio de venta de un servicio
2.- Número de usuarios suscritos
3.- Gastos

utilidad = (precio_venta * usuarios) - gastos
"""
import sys

precio_venta = int(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = int(sys.argv[3])

utilidad = (precio_venta * usuarios) - gastos
print(utilidad)





