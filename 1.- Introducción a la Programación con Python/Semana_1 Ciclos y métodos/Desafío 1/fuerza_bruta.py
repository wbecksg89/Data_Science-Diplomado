import string
abc = string.ascii_lowercase
adivinadas=[]
contador = 0

password = input("Escriba la contraseña\n").lower()
#password.lower()

if not password.isalpha():
    print("Error, su contraseña no es letra")
else:
    for x in range(len(password)):
        for y in abc:
            if y==password[x]:
                adivinadas.append(y)

    for k in adivinadas:
        for i,j in enumerate(abc):
            if k in j:
                contador+=i+1


print(f"Iteraciones: {contador}")
print(f"Contraseña es: {password}")
            
  