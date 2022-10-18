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


def invlogit(x):
    
    """
    Recibe Log odds y devuelve probabilidad.
    """
    
    return round(1 / (1 + np.exp(-x)),3)


def normalizar(df, exclude = None):
    
    df_ = df.drop(exclude, axis = 1)
    
    df_continuas = df_.loc[:, df_.dtypes[df_.dtypes != 'object'].index.tolist()]
    
    df_categoricas = df_.loc[:, df_.dtypes[df_.dtypes == 'object'].index.tolist()]
    
    df_normalizado = df_continuas.apply(lambda x: (x - x.mean())/x.std())
    
    return df_normalizado.join(df_categoricas).join(df[exclude])  



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




def custom_logit(df, target_variable, z, regresors = None, characteristics = None):
    
    if regresors is not None:
        
        regresors_list = ' + '.join(regresors)
        
    else:
    
        regresors_list = ' + '.join([i for i in df.drop([target_variable], axis = 1).columns])

    model = smf.logit(f"{target_variable} ~ {regresors_list}", data = df).fit()

    pseudo_r2 = pd.read_html(model.summary().tables[0].as_html())[0].iloc[1:, [2,3]].iloc[2].values[1]
    
    x = pd.read_html(model.summary().tables[1].as_html())[0].iloc[1:, [0,1,4]]

    x.columns = ['regresor', 'coef', 'pval']

    x['pval'] = pd.to_numeric(x['pval'])
    x['coef'] = pd.to_numeric(x['coef'])

    x_trust = x[x['pval'] <= z].sort_values(by = 'pval')
    
    B0 = x_trust[x_trust['regresor'] == 'Intercept']['coef'].values[0]
    
    x_trust_B = x_trust[x_trust['regresor'] != 'Intercept']
    
    x_trust_B['mean'] = x_trust_B['regresor'].apply(lambda x: df[x].mean())
    
    if characteristics is not None:
        
        x_trust_B['characteristics'] = characteristics
        
        estimate_y = invlogit(x_trust_B.apply(lambda x: x['coef'] * x['characteristics'], axis = 1).sum() + B0)
        
    else:
    
        estimate_y = invlogit(x_trust_B.apply(lambda x: x['coef'] * x['mean'], axis = 1).sum() + B0)
    
    
    return {'pseudo_r2': pseudo_r2, 'data': x_trust , 'estimate_y': estimate_y}



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
   

def custom_ols(df, target_variable, z, regresors = None, characteristics = None):
    
    if regresors is not None:
        
        regresors_list = ' + '.join(regresors)
        
    else:
    
        regresors_list = ' + '.join([i for i in df.drop([target_variable], axis = 1).columns])

    model = smf.ols(f"{target_variable} ~ {regresors_list}", data = df).fit()

    pseudo_r2 = pd.read_html(model.summary().tables[0].as_html())[0].iloc[1:, [2,3]].iloc[2].values[1]
    
    x = pd.read_html(model.summary().tables[1].as_html())[0].iloc[1:, [0,1,4]]

    x.columns = ['regresor', 'coef', 'pval']

    x['pval'] = pd.to_numeric(x['pval'])
    x['coef'] = pd.to_numeric(x['coef'])

    x_trust = x[x['pval'] <= z].sort_values(by = 'pval')
    
    B0 = x_trust[x_trust['regresor'] == 'Intercept']['coef'].values[0]
    
    x_trust_B = x_trust[x_trust['regresor'] != 'Intercept']
    
    x_trust_B['mean'] = x_trust_B['regresor'].apply(lambda x: df[x].mean())
    
    if characteristics is not None:
        
        x_trust_B['characteristics'] = characteristics
        
        estimate_y = invlogit(x_trust_B.apply(lambda x: x['coef'] * x['characteristics'], axis = 1).sum() + B0)
        
    else:
    
        estimate_y = invlogit(x_trust_B.apply(lambda x: x['coef'] * x['mean'], axis = 1).sum() + B0)
    
    
    return {'pseudo_r2': pseudo_r2, 'data': x_trust , 'estimate_y': estimate_y}


def report_scores_linear(y_predicted, y_test):
    
    """
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
    Compara dos vectores de datos y devuelve un objeto con dos llaves: MSE y R2.
    
    y_predicted: Vector objetivo predicho de un modelo ajustado.
    
    y_test: Valores de testing a comparar.
    
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    """
    
    MSE = mean_squared_error(y_test, y_predicted)
    
    R2 = r2_score(y_test, y_predicted)
    
    obj = {
        
        'MSE': MSE,
        'R2': R2
    }
    
    return obj

def plot_hist(df, variables):
    
    """
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
    Devuelve un histograma para cada variable continua.
    
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
    
     
    

