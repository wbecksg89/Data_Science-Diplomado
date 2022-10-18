suma = 0
i = 0
lista = []
ingreso = int(input("Ingrese un número para comenzar\n"))
for i in range(1,ingreso+1):
    if i% 2 == 0 and i > 0 :
        suma+=i
        lista.append(i)

print(f"Iteraciones: {lista}")

print(f"La suma es: {suma}")