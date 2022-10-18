
import sys

usuarios_normales = int(sys.argv[1])
usuarios_premium = int(sys.argv[2])
usuarios_prueba = int(sys.argv[3])
precio_normal = int(sys.argv[4])
gastos = int(sys.argv[5])
precio_premium = precio_normal*2
precio_prueba = 0

utilidad = (usuarios_normales*precio_normal + usuarios_premium*precio_premium + usuarios_prueba*precio_prueba) - gastos
print(utilidad)





