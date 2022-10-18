import string


def gen(cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad > 0:
            is_pos = True
            abc = string.ascii_lowercase
            result = []
            for i,j in enumerate(abc):
                if i < cantidad:
                    result.append(j)
            return print(''.join(result))

        else:
            print("Error, ingrese un número entero positivo")

    except ValueError:
        print("Error, ingrese un número entero positivo")

def letra_o(num):
    lista = []
    try:
        num = int(num)
        if num > 0:
            for i in range(num):
                lista.append(i)

            for k in lista:
                if k == 0 or k == lista[-1]:
                    print("*"*num)
                elif k != 0 or k == lista[-1]:
                    print("*"+ " "*(num-2) + "*")
        else:
            print("Error, ingrese un número entero positivo")
    except ValueError:
        print("Error, ingrese un número entero positivo")


def letra_i(num):
    lista = []
    es_par = False
    try:
        num = int(num)
        if num % 2==0:
            es_par = True
        else:
            es_par = False
        if num > 0:
            for i in range(num):
                lista.append(i)

            for k in lista:
                if k == 0 or k == lista[-1]:
                    print("*"*num)
                elif es_par and (k != 0 or k == lista[-1]):
                    print(" "*(int((num-1)/2))+ "*" + " "*(int((num-1)/2)))
                elif not es_par and (k != 0 or k == lista[-1]):
                    print(" "*(int((num-1)/2))+ "*" + " "*(int((num-1)/2)))
        else:
            print("Error, ingrese un número entero positivo")
    except ValueError:
        print("Error, ingrese un número entero positivo")


def letra_x(num):
    try:
        num = int(num)
        if num > 0:
            for n in range(1,num+1):     
                print(" "*min(n-1,num-n)+"*"+" "*max(num-(2*n),2*(n-1)-num,0)+"*"*(1-(num%2)*(1-max(min(max(num-(2*n),2*(n-1)-num),1),0))))
        
        else:
            print("Error, ingrese un número entero positivo")
    except ValueError:
        print("Error, ingrese un número entero positivo")

print("1.2 Dibujando letras: letra_o(valor)\n1.2.a Función letra 'N': letra_n(valor)\n1.2.b Letra 'I': letra_i(valor)\n1.2.c Letra 'X': letra_x(valor)")

valor = int(input("Ingrese un numero entero positivo\n"))

print("1.1 Concatenando letras: gen(valor)\n")
gen(valor)
print("\n")
print("1.2 Dibujando letras:\n")
print("1.2.a Letra_o(valor)\n")
letra_o(valor)
print("\n")
print("1.2.b Letra_i(valor)\n")
letra_i(valor)
print("\n")
print("1.2.c Letra_x(valor)\n")
letra_x(valor)
