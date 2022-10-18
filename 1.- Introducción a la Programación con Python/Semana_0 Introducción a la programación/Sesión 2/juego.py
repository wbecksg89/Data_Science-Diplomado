import random
import sys

usuario = sys.argv[1]
usuario = usuario.lower()
opciones = {1:"piedra",2:"papel",3:"tijera"}
cpu = random.randint(1,3)
cpu = opciones[cpu]
print(f"Jugador juega {usuario}")
    
if usuario not in ('piedra','papel','tijera'):
    print("Debe ingresar piedra, papel o tijera")
else:

    if usuario == cpu:
        print(f"Computador juega: {cpu}")
        print('Empate')
    elif (usuario == 'papel' and cpu == 'piedra') or (usuario == 'piedra' and cpu == 'tijera') or (usuario == 'tijera' and cpu == 'papel'):
        print(f"Computador juega: {cpu}")
        print("Gana usuario")
    else:
        print(f"Computador juega: {cpu}")
        print("Gana Computador")

