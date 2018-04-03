#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:24:59 2018

Script to perfomr complete analysis

@author: obarquero
"""
import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt

def create_pandas_db():
    """
    Fucntion to create pandas db from ctu_database
    """
    
    #read npy data
    ctu_df = pd.DataFrame(columns=['id','apgar_1','apgar_5','pH','sampen_r1','sampen_r2','time_irrever'])
    
    folder = './ctu_database'
    
    for filename in glob.iglob(folder+'/'+'*.npy'):
        
        print(filename)
        fet = np.load(filename).flat[0]
        
        fet['time_irrever'] = np.sum(fet['time_irrever']) #we use assimetry index
        
        #remove case
        del fet['case']
        
        df_aux = pd.DataFrame(data = fet,index = [0])
        
        ctu_df = ctu_df.append(df_aux,ignore_index = True)
        
        
    return ctu_df
        
        
ctu_df = create_pandas_db()

#Include differente criterias as case

#case according to apgar_1
#a newborn is a case if apgar_1 <= 7
ctu_df['case_apgar_1'] = ctu_df['apgar_1'] <= 7

#case according to pH
#a newborn is a case if ph < 7.20
ctu_df['case_ph'] = ctu_df['pH'] <= 7.20


###################################################
#%%
#Exploratory analysis.

#1) Plot histograms af all variables

plt.close('all')

ctu_df['apgar_1'].hist()
ctu_df['apgar_5'].hist()
plt.legend(['apgar_1', 'apgar_5'])
plt.xlabel('Puntuación')
plt.ylabel('Fetos')
plt.title('Histograma Apgar')

plt.figure()
ctu_df['pH'].hist()
plt.xlabel('pH')
plt.ylabel('Fetos')
plt.title('Histograma pH')

plt.figure()
ctu_df['sampen_r1'].hist()
ctu_df['sampen_r2'].hist()
plt.legend(['sampen_r1', 'sampen_r2'])
plt.xlabel('SampEn')
plt.ylabel('Fetos')
plt.title('Histograma Sample Entropy')

plt.figure()
ctu_df['time_irrever'].hist()
plt.xlabel('Time_irrever')
plt.ylabel('Fetos')
plt.title('Histograma Time Irreversibility')

#2) Plot scatter plots with apgar_1 and Ph with any other variable

#example
plt.figure()
ctu_df.plot.scatter('sampen_r1','pH')
plt.figure()
ctu_df.plot.scatter('sampen_r1','apgar_1')

plt.figure()
ctu_df.plot.scatter('sampen_r2','pH')
plt.figure()
ctu_df.plot.scatter('sampen_r2','apgar_1')

plt.figure()
ctu_df.plot.scatter('time_irrever','pH')
plt.figure()
ctu_df.plot.scatter('time_irrever','apgar_1')
#3) Create boxplot between any variable agouped by case_ph and case_apgar_1

#example
plt.figure()
ctu_df.boxplot('sampen_r1',by='case_apgar_1')
plt.ylabel('sampen_r1')
plt.figure()
ctu_df.boxplot('sampen_r1',by='case_ph')
plt.ylabel('sampen_r1')


plt.figure()
ctu_df.boxplot('sampen_r2',by='case_apgar_1')
plt.ylabel('sampen_r2')
plt.figure()
ctu_df.boxplot('sampen_r2',by='case_ph')
plt.ylabel('sampen_r2')


plt.figure()
ctu_df.boxplot('time_irrever',by='case_apgar_1')
plt.ylabel('time_irrever')
plt.figure()
ctu_df.boxplot('time_irrever',by='case_ph')
plt.ylabel('time_irrever')



#4) Describe de la base de datos. Media y desviación estandar de cada vairable
print(ctu_df.describe())


#%%
# Test estadísticos

#linear regression between apgar_1 y ph con las otras variables. Para cada variable y para 
#todas las variables 
#Vamos a testear si apgar_1 (ph) = w0 + w1 x_1
#donde x_1 puede ser sampen_r1,sampen_r2 y time_irrer
#y también apgar_1(ph) = w0 + w1x1 +w2 x2 +w3 x3
#(con las tres variables explicativas a la vez) 

#example
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

X_s1 = ctu_df['sampen_r1']
X_s2 = ctu_df['sampen_r2']
X_ti = ctu_df['time_irrever']
y = ctu_df['apgar_1']

model_s1 = sm.OLS(y,X_s1).fit()
print(model_s1.summary())
prstd, iv_l, iv_u = wls_prediction_std(model_s1)

fig, ax = plt.subplots(figsize=(10,8))

ax.plot(X_s1, y, 'o', label="data")
#ax.plot(X_s1, X_s1, 'b-', label="True")
ax.plot(X_s1, model_s1.fittedvalues, 'r-o', label="OLS")
ax.plot(X_s1, iv_u, 'b--', label= "upper confidence limit")
ax.plot(X_s1, iv_l, 'b--', label= "lower confidence limit")
plt.xlabel('sampen_r1')
plt.ylabel('puntuación test apgar_1')
plt.title('Mínimos cuadrados ordinarios sampen_r1/apgar_1')
ax.legend(loc='best');

# --Verificación de normalidad de los datos---
# Comprobar si las variables explicativas (todas, menos apgar, ph y caseX) son normales o no
model_s2 = sm.OLS(y,X_s2).fit()
print(model_s2.summary())
prstd, iv_l, iv_u = wls_prediction_std(model_s2)

fig, ax = plt.subplots(figsize=(10,8))

ax.plot(X_s2, y, 'o', label="data")
#ax.plot(X_s2, X_s2, 'b-', label="True")
ax.plot(X_s2, model_s2.fittedvalues, 'r-o', label="OLS")
ax.plot(X_s2, iv_u, 'b--', label= "upper confidence limit")
ax.plot(X_s2, iv_l, 'b--', label= "lower confidence limit")
plt.xlabel('sampen_r2')
plt.ylabel('puntuación test apgar_1')
plt.title('Mínimos cuadrados ordinarios sampen_r2/apgar_1')
ax.legend(loc='best');




model_ti = sm.OLS(y,X_ti).fit()
print(model_ti.summary())
prstd, iv_l, iv_u = wls_prediction_std(model_ti)

fig, ax = plt.subplots(figsize=(10,8))

ax.plot(X_ti, y, 'o', label="data")
#ax.plot(X_ti, X_ti, 'b-', label="True")
ax.plot(X_ti, model_ti.fittedvalues, 'r-o', label="OLS")
ax.plot(X_ti, iv_u, 'b--', label= "upper confidence limit")
ax.plot(X_ti, iv_l, 'b--', label= "lower confidence limit")
plt.xlabel('time_irrever')
plt.ylabel('puntuación test apgar_1')
plt.title('Mínimos cuadrados ordinarios time_irrever/apgar_1')
ax.legend(loc='best');

#Let's perform classification analysis using case. Statistical comparisons
#between variables for differente cases
from statsmodels.stats.diagnostic import kstest_normal

#Example 1
#get different variables for healthy and case
sampen_r1_health = ctu_df['sampen_r1'][ctu_df['case_apgar_1']==False]
sampen_r1_case = ctu_df['sampen_r1'][ctu_df['case_apgar_1']==True]

#evaluate normality
stat, p_value1 = kstest_normal(sampen_r1_health)

#evaluate normality
stat, p_value2 = kstest_normal(sampen_r1_case)

#ambos son menores de 0.05, por lo que podemos utilizar t-test

from statsmodels.stats.weightstats import ttest_ind

t,p_value,df = ttest_ind(sampen_r1_health,sampen_r1_case)


