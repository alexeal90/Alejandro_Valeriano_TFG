# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:37:16 2017

@author: Alex
"""

from mix_processes import mix
from HRV_Entropy import HRV_entropy
import matplotlib.pyplot as plt

import numpy as np
import scipy as sc


hrv = HRV_entropy() #create class of hrv entropy

asi = np.zeros((10,9))

tau  = 10
N = 300*tau
for i in range(10):
    Mix1 = mix(N,0.1)
    Mix2 = mix(N,0.2)
    Mix3 = mix(N,0.3)
    Mix4 = mix(N,0.4)
    Mix5 = mix(N,0.5)
    Mix6 = mix(N,0.6)
    Mix7 = mix(N,0.7)
    Mix8 = mix(N,0.8)
    Mix9 = mix(N,0.9)
    

    asi[i,0],tirr_1 = hrv.TimeIrreversibility(Mix1,tau)
    asi[i,1],tirr_2 = hrv.TimeIrreversibility(Mix2[:,0],tau)
    asi[i,2],tirr_3 = hrv.TimeIrreversibility(Mix3[:,0],tau)
    asi[i,3],tirr_4 = hrv.TimeIrreversibility(Mix4[:,0],tau)
    asi[i,4],tirr_5 = hrv.TimeIrreversibility(Mix5[:,0],tau)
    asi[i,5],tirr_6 = hrv.TimeIrreversibility(Mix6[:,0],tau)
    asi[i,6],tirr_7 = hrv.TimeIrreversibility(Mix7[:,0],tau)
    asi[i,7],tirr_8 = hrv.TimeIrreversibility(Mix8[:,0],tau)
    asi[i,8],tirr_9 = hrv.TimeIrreversibility(Mix9[:,0],tau)
    
    #for j in range(9):
     #   asi[j][i] = asi_aux[j]


#asi_mean = np.arange(9)
#asi_std = np.arange(9)
#for k, l in enumerate(asi):
#    asi_mean[k] = np.mean(asi[k])
#    asi_std[k] = np.std(asi[k])

asi_mean = np.mean(asi,axis=0)
asi_std = np.std(asi, axis = 0)

P = np.arange(0.1, 1, 0.1)
for Each_P in range(9):
    plt.errorbar(P[Each_P],asi_mean[Each_P],yerr = asi_std[Each_P],fmt = 'o-')

plt.xlabel('MIX parameter $p$')
plt.ylabel('Asymmetry index $m\pm std$')

plt.axhline(y=0, color='gray', linestyle='--')
#%% Antiguo codigo
'''
hrv = HRV_entropy() #create class of hrv entropy

Timeirr_01 = []
Timeirr_02 = []
Timeirr_03 = []
Timeirr_04 = []
Timeirr_05 = []
Timeirr_06 = []
Timeirr_07 = []
Timeirr_08 = []
Timeirr_09 = []
asi_01 = []
asi_02 = []
asi_03 = []
asi_04 = []
asi_05 = []
asi_06 = []
asi_07 = []
asi_08 = []
asi_09 = []

tau  = 10
N = 300*tau
for i in range(10):
    Mix1 = mix(N,0.1)
    Mix2 = mix(N,0.2)
    Mix3 = mix(N,0.3)
    Mix4 = mix(N,0.4)
    Mix5 = mix(N,0.5)
    Mix6 = mix(N,0.6)
    Mix7 = mix(N,0.7)
    Mix8 = mix(N,0.8)
    Mix9 = mix(N,0.9)

    asi_1,tirr_1 = hrv.TimeIrreversibility(Mix1[:,0],tau)
    asi_2,tirr_2 = hrv.TimeIrreversibility(Mix2[:,0],tau)
    asi_3,tirr_3 = hrv.TimeIrreversibility(Mix3[:,0],tau)
    asi_4,tirr_4 = hrv.TimeIrreversibility(Mix4[:,0],tau)
    asi_5,tirr_5 = hrv.TimeIrreversibility(Mix5[:,0],tau)
    asi_6,tirr_6 = hrv.TimeIrreversibility(Mix6[:,0],tau)
    asi_7,tirr_7 = hrv.TimeIrreversibility(Mix7[:,0],tau)
    asi_8,tirr_8 = hrv.TimeIrreversibility(Mix8[:,0],tau)
    asi_9,tirr_9 = hrv.TimeIrreversibility(Mix9[:,0],tau)
    
    
    Timeirr_01.append(tirr_1)
    Timeirr_02.append(tirr_2)
    Timeirr_03.append(tirr_3)
    Timeirr_04.append(tirr_4)
    Timeirr_05.append(tirr_5)
    Timeirr_06.append(tirr_6)
    Timeirr_07.append(tirr_7)
    Timeirr_08.append(tirr_8)
    Timeirr_09.append(tirr_9)
    asi_01.append(asi_1)
    asi_02.append(asi_2)
    asi_03.append(asi_3)
    asi_04.append(asi_4)
    asi_05.append(asi_5)
    asi_06.append(asi_6)
    asi_07.append(asi_7)
    asi_08.append(asi_8)
    asi_09.append(asi_9)

t01_m = np.mean(asi_01)
t01_std = np.std(asi_01)
t02_m = np.mean(asi_02)
t02_std = np.std(asi_02)
t03_m = np.mean(asi_03)
t03_std = np.std(asi_03)
t04_m = np.mean(asi_04)
t04_std = np.std(asi_04)
t05_m = np.mean(asi_05)
t05_std = np.std(asi_05)
t06_m = np.mean(asi_06)
t06_std = np.std(asi_06)
t07_m = np.mean(asi_07)
t07_std = np.std(asi_07)
t08_m = np.mean(asi_08)
t08_std = np.std(asi_08)
t09_m = np.mean(asi_09)
t09_std = np.std(asi_09)
plt.errorbar(0.1,asi_mean[0],yerr = asi_std[0],fmt = 'o-')
plt.errorbar(0.2,asi_mean[1],yerr = asi_std[1],fmt = 'o-')
plt.errorbar(0.3,asi_mean[2],yerr = asi_std[2],fmt = 'o-')
plt.errorbar(0.4,asi_mean[3],yerr = asi_std[3],fmt = 'o-')
plt.errorbar(0.5,asi_mean[4],yerr = asi_std[4],fmt = 'o-')
plt.errorbar(0.6,asi_mean[5],yerr = asi_std[5],fmt = 'o-')
plt.errorbar(0.7,asi_mean[6],yerr = asi_std[6],fmt = 'o-')
plt.errorbar(0.8,asi_mean[7],yerr = asi_std[7],fmt = 'o-')
plt.errorbar(0.9,asi_mean[8],yerr = asi_std[8],fmt = 'o-')
'''
