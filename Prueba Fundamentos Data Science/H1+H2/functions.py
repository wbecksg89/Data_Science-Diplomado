#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns


def recodificaciones(df):
    
    df['collars'] = df['occupation'].replace({


        'Prof-specialty': 'white-collar',
         'Exec-managerial': 'white-collar',
         'Adm-clerical': 'white-collar',
         'Sales': 'white-collar', 
         'Tech-support': 'white-collar',

         'Craft-repair': 'blue-collar',
         'Machine-op-inspct': 'blue-collar',
         'Transport-moving': 'blue-collar',
         'Handlers-cleaners': 'blue-collar',
         'Farming-fishing': 'blue-collar',
         'Protective-serv': 'blue-collar',
         'Priv-house-serv': 'blue-collar',

         'Other-service': 'others',
         'Armed-Forces': 'others'
    })

    df['workclass_recod'] = df['workclass'].replace({

        'Federal-gov': 'federal-gov',
        'State-gov': 'state-level-gov',
        'Local-gov': 'state-level-gov',
        'Self-emp-inc': 'self-employed',
        'Self-emp-not-inc': 'self-employed',
        'Never-worked': 'unemployed',
        'Without-pay': 'unemployed',
        'Private': 'private'


    })

    df['educ_recod'] = df['education'].replace({


        'Preschool': 'preschool',
        '1st-4th': 'elementary-school',
        '5th-6th': 'elementary-school',
        '7th-8th': 'high-school',
        '9th': 'high-school',
        '10th': 'high-school',
        '11th': 'high-school',
        '12th': 'high-school',
        'HS-grad': 'high-school',
        'Assoc-voc': 'college',
        'Assoc-acdm': 'college',
        'Some-college': 'college',
        'Bachelors': 'university',
        'Masters': 'university',
        'Prof-school': 'university',
        'Doctorate': 'university'




    })

    df['civstatus'] = df['marital-status'].replace({


        'Married-civ-spouse': 'married',
        'Married-spouse-absent': 'married',
        'Married-AF-spouse': 'married',
        'Widowed': 'widowed',
        'Divorced' : 'divorced',
        'Separated' : 'separated',
        'Never-married': 'never-married'

    })
    
    df['region'] = df['native-country'].replace(
    ["United-States", 
     "Mexico", 
     "Puerto-Rico", 
     "Canada", 
     "El-Salvador", 
     "Cuba", 
     "Jamaica", 
     "Dominican-Republic",
     "Guatemala", 
     "Columbia", 
     "Haiti", 
     "Nicaragua", 
     "Peru", 
     "Ecuador", 
     "Trinadad&Tobago",
     "Outlying-US(Guam-USVI-etc)", 
     "Honduras",
     "Philippines", 
     "India", 
     "China", 
     "South", 
     "Japan", 
     "Vietnam", 
     "Taiwan", 
     "Iran", 
     "Thailand", 
     "Hong", 
     "Cambodia", 
     "Laos",
     "Germany", 
     "England", 
     "Italy", 
     "Poland", 
     "Portugal", 
     "Greece" ,
     "France", 
     "Ireland", 
     "Yugoslavia", 
     "Scotland", 
     "Holand-Netherlands", 
     "Hungary"],
    ["america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "america",
     "asia",
     "asia",
     "asia", 
     "asia", 
     "asia", 
     "asia", 
     "asia",
     "asia",
     "asia", 
     "asia", "asia","asia",
     "europa","europa", "europa","europa","europa","europa","europa","europa","europa","europa","europa","europa"  ])

    return df.drop(['occupation', 'workclass', 'education', 'marital-status', 'native-country'], axis = 1)



def recodificaciones_d2(df):
    df['G2'] = df['G2'].apply(lambda x: str(x)) 
    df = df.apply(lambda x: x.str.replace('"', ''))
    
    bin1 = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet','romantic']

    bin2 = ['Mjob', 'Fjob', 'reason', 'guardian']

    bateria = ['famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health'] 

    promedios = ['G1', 'G2', 'G3']

    numerizar = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'absences']



    #convertir en numero.
    df_numerics = df.loc[:, numerizar + bateria + promedios]

    for i in numerizar + bateria + promedios:

        df_numerics[i] = pd.to_numeric(df_numerics[i])


    #binarizar
    df_dummies = pd.get_dummies(df.loc[:, bin1 + bin2], drop_first = True)

    df_join = df_numerics.join(df_dummies)
    
    return df_join


   
def normalizar(df, exclude = None):
    
    df_ = df.drop(exclude, axis = 1)
    
    df_continuas = df_.loc[:, df_.dtypes[df_.dtypes != 'object'].index.tolist()]
    
    df_categoricas = df_.loc[:, df_.dtypes[df_.dtypes == 'object'].index.tolist()]
    
    df_normalizado = df_continuas.apply(lambda x: (x - x.mean())/x.std())
    
    return df_normalizado.join(df_categoricas).join(df[exclude])  


def plot_hist(df, variables):
    
    """
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
    Devuelve un histograma para cada variable continua.
    
    df: Dataframe
    
    variables: Lista o array con los nombres de las columnas a ser ploteadas.
    
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    """
    plt.figure(figsize = (20,10))
    for index, var in enumerate(variables):
        
        plt.subplot(3,3,index+1)
        
        plt.title(var)

        sns.distplot(df[var].dropna())

        media = df[var].dropna().mean()
        mediana = df[var].dropna().median()

        plt.hist(df[var],color='dodgerblue',alpha=.7)
        plt.axvline(media, color = 'tomato', linestyle = '--', label = f'Media')
        plt.axvline(mediana, color = 'green', linestyle = '--', label = f'Mediana', alpha = .6)

        plt.legend()

def plot_hist2(df, variables):
    
    """
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
    Devuelve un histograma para cada variable continua ingresada, versión2
    
    df: Dataframe
    
    variables: Lista o array con los nombres de las columnas a ser ploteadas.
    
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    """
 
    for index, var in enumerate(variables):
        
        
        plt.subplot(4,4,index+1)
        
        plt.title(f"Variable: {var}")

        sns.distplot(df[var].dropna())

        media = df[var].dropna().mean()
        mediana = df[var].dropna().median()

        plt.axvline(media, color = 'tomato', linestyle = '--', label = f'Media de {var}')
        plt.axvline(mediana, color = 'green', linestyle = '--', label = f'Mediana de {var}', alpha = .6)

        plt.legend()

def grafico_hist(df,var,binarize):
    
    """
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
    Devuelve un histograma para variables continuas y variable objetivo.
    
    df: Dataframe
    
    var: Nombres de las columnas a ser ploteadas.

    binarize: Nombre de la columna binaria a graficar
    
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    """

    g = sns.histplot(data=df,x=var, hue=binarize,bins=30)
    ax = plt.gca()
    ax.axvline(df[df[binarize]==1][var].mean(),color='green',lw=3,ls='--')
    ax.text(df[df[binarize]==1][var].mean()/df[df[binarize]==1][var].count()/2, 0.7, f"mean_{var}={df[df[binarize]==1][var].mean():.0f} ",transform=ax.transAxes,color='green',fontweight='bold',fontsize=6)
    
    ax.axvline(df[df[binarize]==0][var].mean(),color='blue',lw=3,ls='--')
    ax.text(df[df[binarize]==0][var].mean()/df[df[binarize]==0][var].count()/2, 0.8, f"mean_{var}={df[df[binarize]==0][var].mean():.0f} ",transform=ax.transAxes,color='blue',fontweight='bold',fontsize=6)
    


