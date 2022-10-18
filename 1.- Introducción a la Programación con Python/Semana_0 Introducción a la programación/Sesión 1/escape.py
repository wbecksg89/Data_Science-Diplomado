import sys
"""
Se pide crear el programa escape.py donde el usuario ingrese la gravedad y el radio y como 
resultado obtenga la velocidad de escape.
"""

#g = 9.8
#r = 6371
g = float(sys.argv[1])
r = float(sys.argv[2])
#Respuesta: 11174.59 aprox.
ve = (2*g*r*1000)**(1/2)
print(ve)