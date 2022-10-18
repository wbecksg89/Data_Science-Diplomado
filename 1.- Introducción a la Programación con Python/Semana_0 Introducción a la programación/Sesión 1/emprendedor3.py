
import sys

"""
1.- Precio
2.- Usuarios
3.- Gastos
4.- Utilidad año anterior (optativo, si no lo ingresa entonces 1000)
- Mostrar razón entre la utilidad presente y pasado
- Mostrar utilidades actuales
- 1 tipo de usuario y precio
"""
precio_venta=int(sys.argv[1])
usuarios=int(sys.argv[2])
gastos=int(sys.argv[3])

try:
    utilidad_pasada = int(sys.argv[4])
except:
    utilidad_pasada=1000

utilidad_actual = (precio_venta * usuarios) - gastos
razon = ((utilidad_actual-utilidad_pasada)/utilidad_pasada)+1
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon}")
print(f"La utilidad actual es: {utilidad_actual}")




