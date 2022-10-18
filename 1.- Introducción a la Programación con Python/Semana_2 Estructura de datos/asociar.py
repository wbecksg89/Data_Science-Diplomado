velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
 11, 11, 12, 12, 12, 12, 13, 13,
 13, 13, 14, 14, 14, 14, 15, 15,
 15, 16, 16, 17, 17, 17, 18, 18,
 18, 18, 19, 19, 19, 20, 20, 20,
 20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
 17, 28, 14, 20, 24, 28, 26, 34, 34,
 46, 26, 36, 60, 80, 20, 26, 54, 32,
 40, 32, 40, 50, 42, 56, 76, 84, 36,
 46, 68, 32, 48, 52, 56, 64, 66, 54,
 70, 92, 93, 120, 85]
"""
Con esta función se le solicita que, utilizando contadores, cuente cuántas veces ocurre cada
uno de los siguientes eventos:
● Velocidad bajo el promedio.
● Velocidad bajo el promedio y distancia sobre el promedio.
● Velocidad sobre el promedio.
● Velocidad sobre el promedio y distancia bajo el promedio.
"""

vd = [i for i in zip(velocidad,distancia)]

#1.- Velocidad Promedio
vel_promedio = sum(velocidad)/len(velocidad)
dist_promedio = sum(distancia)/len(distancia)

#1.1.- Velocidades bajo el promedio
cantidad_vel_bajo_promedio = len(list(filter(lambda x: x<vel_promedio,velocidad)))
print(f"La cantidad de eventos bajo el promedio son: {cantidad_vel_bajo_promedio} de {len(velocidad)} eventos totales")

#2.- Velocidad bajo promedio & distancia sobre el promedio
dos = [i for i in vd if i[0]< vel_promedio and i[1]> dist_promedio]
dos_total = len(dos)
print(f"La cantidad de eventos bajo la velocidad y distancia promedio son: {dos_total} de {len(vd)} eventos totales")

#3.- Velocidad sobre el promedio
tres = len(velocidad)-cantidad_vel_bajo_promedio
print(f"La cantidad de eventos sobre el promedio son: {tres} de {len(vd)} eventos totales")

#4.- Velocidad sobre el promedio y distancia bajo el promedio.
print(f"La cantidad de eventos de velocidad sobre el promedio y distancia bajo el promedio son: {len(vd)-dos_total} de {len(vd)} eventos totales")
