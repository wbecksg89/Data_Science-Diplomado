import sys

numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])
numero3 = int(sys.argv[3])

if numero1 > numero2:
    if numero1 > numero3:
        print(numero1)
    else:
        print(numero3)
elif numero2 > numero1:
    if numero2 > numero3:
        print(numero2)
    else: 
        print(numero3)
else:
    print("Error")
        
