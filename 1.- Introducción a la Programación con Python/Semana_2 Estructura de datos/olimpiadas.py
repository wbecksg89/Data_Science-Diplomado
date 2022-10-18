import pandas as pd
import numpy as np

ejercicio_1 = pd.read_csv("athlete_events.csv")
ejercicio_1.shape
print(f"1.- El data set tiene {ejercicio_1.shape[0]} filas y {ejercicio_1.shape[1]} columnas")

# 2. Reportar cuántas competencias se han realizado a lo largo del tiempo.
ejercicio_2 = ejercicio_1['Games'].nunique()
print(f"2.- Se han realizado: {ejercicio_2} competencias")


"""
Reportar el porcentaje (número entre 0 y 1) de atletas que participaron tanto en los
juegos olímpicos de Verano como en los de Invierno. El resultado debe guardarse en
una variable llamada ejercicio_3.
"""

atletas_temporadas = ejercicio_1.loc[:,['Name','Season','Games']]
ejercicio_3 = atletas_temporadas['Season'].value_counts()/len(atletas_temporadas['Name'])
ejercicio_3
#resultado = atletas_temporadas.groupby('Name').Season.nunique()
#resultado = pd.DataFrame(resultado)
#resultado = resultado[(resultado['Season']>1)]

#ejercicio_3 = str(round(len(resultado)*100/len(atletas),2))+"%"
#print(f"Atletas que participaron en juegos olimpicos de verano e invierno: {len(resultado)}, de un total: {len(atletas)}, el porcentaje es: {ejercicio3}")

"""4. Informar dónde fue la primera celebración de un Juego Olímpico de Verano. El
resultado debe guardarse en una variable llamada ejercicio_4.
Tip: Investige sobre las funciones min() y unique() de una Serie de pandas."""

ejercicio4 = ejercicio_1['Games'].drop_duplicates()
ejercicio_4 = ejercicio4.min()
ejercicio_4

"""
5. Informar dónde fue la primera celebración de un Juego Olímpico de Invierno. El
resultado debe guardarse en una variable llamada ejercicio_5.
"""
ejercicio5 = ejercicio_1['Games'].drop_duplicates()
ejercicio5 = ejercicio5[ejercicio5.str.contains('Winter')]
ejercicio_5 = ejercicio5.min()
ejercicio_5

"""
6. Reportar los 10 primeros países con mayor cantidad de atletas participantes a lo largo
de los juegos. El resultado debe guardarse en una variable llamada ejercicio_6.
"""
atleta_pais = ejercicio_1.loc[:,['Name','Team']]
atleta_pais = atleta_pais.drop_duplicates()
atleta_pais = atleta_pais.groupby('Team').Name.nunique()
atleta_pais = pd.DataFrame(atleta_pais)
atleta_pais = atleta_pais.sort_values(by='Name', ascending=False)
ejercicio_6 = atleta_pais.head(10)
ejercicio_6

#resultado = atletas_temporadas.groupby('Name').Season.nunique()

"""
7. Reportar el porcentaje de medallas asignadas (oro, bronce, plata). El resultado debe 
guardarse en una variable llamada ejercicio_7.
"""
ejercicio_7 = ejercicio_1.loc[:,['Medal','Name']]
ejercicio_7 = ejercicio_7[ejercicio_7['Medal'].notna()]
ejercicio_7 = ejercicio_7['Medal'].value_counts()/ejercicio_7['Medal'].count()
ejercicio_7

"""
8. Reportar cuáles fueron los países participantes en las primeras olimpiadas de verano. 
El resultado debe guardarse en una variable llamada ejercicio_8.
"""
pd.set_option('display.max_rows', 500)
ejercicio_8 = ejercicio_1[ejercicio_1['Games']==ejercicio_4]

duplicates = [1,2,5,9,10,12,13,14]
ejercicio_8 = ejercicio_8.loc[:,['Team','NOC']].drop_duplicates().sort_values(by='Team').reset_index(drop=True)
ejercicio_8 = ejercicio_8[~ejercicio_8.index.isin(duplicates)].reset_index(drop=True)
ejercicio_8 = ejercicio_8.loc[:,['Team']]
ejercicio_8