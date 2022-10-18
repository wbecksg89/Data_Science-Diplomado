
from functools import reduce

velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
 11, 11, 12, 12, 12, 12, 13, 13,
 13, 13, 14, 14, 14, 14, 15, 15,
 15, 16, 16, 17, 17, 17, 18, 18,
 18, 18, 19, 19, 19, 20, 20, 20,
 20, 20, 22, 23, 24, 24, 24, 24, 25]

def promedio(arreglo):
    return sum(arreglo)/len(arreglo)

auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

#1.- Lista anidada que contenga los 6 autos
autos=[]

for i in [auto1,auto2,auto3,auto4,auto5,auto6]:
    autos.append(i)

velocidades = []
automoviles = []

lista_temporal2=[]
lista_temporal3=[]

for i in autos:
    #print(vel[1])
    velocidades.append(i[1])
    automoviles.append(i[0])
    lista_temporal2.append(i[2])
    lista_temporal3.append(i[4])
"""
3.- Generar un loop que muestre en pantalla aquellos autos cuyo segundo campo (el número flotante)
es mayor al de la media de todos los autos.
La solución debe estar dentro del programa listas_tres.py.
""" 

resultado3 = [i[0:2] for i in autos if i[1]>promedio(velocidades)]

print(f"3.- Los autos que superan el promedio: {promedio(velocidades)} son: {resultado3[0][0],resultado3[1][0]}, con un valor de: {resultado3[0][1],resultado3[1][1]} respectivamente")

