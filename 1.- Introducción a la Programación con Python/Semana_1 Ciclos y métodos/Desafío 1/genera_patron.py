i = 0
lista = []
ingreso = int(input("Número de filas\n"))
for i in range(1,ingreso+1):
    lista.append(i)
    for i in lista:
        print(i, end='')
    print()