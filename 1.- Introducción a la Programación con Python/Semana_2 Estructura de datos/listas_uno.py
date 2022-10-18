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
print(f"1.- Lista anidada que contenga los 6 autos: {autos}\n")

