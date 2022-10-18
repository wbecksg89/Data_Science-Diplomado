"""
5.- Generar programa quarters.py.
Se pide generar un diccionario, llamado quarters, con las ventas de cada trimestre. Las
claves tienen que ser "Q1", "Q2", "Q3", "Q4".
Tips:
● Los valores ingresados serán distintos.
● El diccionario de resultados debe llamarse quarters, pues este será el que se evalúe.
● ¿Se necesitan los keys?
    ○ ¿Necesitamos iterar elementos, o elementos e índices a la vez?
"""
q1 = ['Enero', 'Febrero', 'Marzo']
q2 = ['Abril', 'Mayo','Junio']
q3 = ['Julio', 'Agosto', 'Septiembre']
q4 = ['Octubre', 'Noviembre', 'Diciembre']

def quarters(diccionario):
    obj = {}
    for index, q in enumerate([q1,q2,q3,q4]):
        obj[f'Q{index+1}'] =  sum([v for k,v in ventas.items() if k in q])
        
    return obj
quarters(ventas)