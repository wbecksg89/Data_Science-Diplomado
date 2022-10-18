#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# In[4]:


plt.style.use('seaborn-whitegrid') #grafico estilo seaborn
plt.rcParams["figure.figsize"] = (10,6) # tamaño
plt.rcParams["figure.dpi"] = 200 #Resolución grafico


# In[11]:


def dotplot(df, plot_var, plot_by, global_stat = False ,statistic = 'mean'):
    
    temp_df = df.loc[:,[plot_by, plot_var]]
    
    if statistic is 'mean':
        temp_group = temp_df.groupby(plot_by)[plot_var].mean()
        
    if statistic is 'median':
        temp_group = temp_df.groupby(plot_by)[plot_var].median()
    
    plt.plot(temp_group.values, temp_group.index, 'o',color='grey')
    
    if global_stat is True and statistic is 'mean':
        plt.axvline(df[plot_var].mean(),color='tomato',linestyle='--')
    
    if global_stat is True and statistic is 'median':
        plt.axvline(df[plot_var].mean(),color='tomato',linestyle='--')


# In[6]:


def inspeccion(df,var,print_list=False):
    for i in df.axes[1]:
        if i == var:
            print(f"Variable: {i}"," - ",f"Casos perdidos: {df[i].isna().sum()}" ," - ",f"Casos totales: {len(df[i])}" ," - ", f"Porcentaje: {round(df[i].isna().sum()/len(df[i])*100,2)} %")
            if print_list:
                return df[df[i].isna()]


# In[ ]:




