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

plt.errorbar(0.1,t01_m,yerr = t01_std,fmt = 'o-')
plt.errorbar(0.2,t02_m,yerr = t02_std,fmt = 'o-')
plt.errorbar(0.3,t03_m,yerr = t03_std,fmt = 'o-')
plt.errorbar(0.4,t04_m,yerr = t04_std,fmt = 'o-')
plt.errorbar(0.5,t05_m,yerr = t05_std,fmt = 'o-')
plt.errorbar(0.6,t06_m,yerr = t06_std,fmt = 'o-')
plt.errorbar(0.7,t07_m,yerr = t07_std,fmt = 'o-')
plt.errorbar(0.8,t08_m,yerr = t08_std,fmt = 'o-')
plt.errorbar(0.9,t09_m,yerr = t09_std,fmt = 'o-')


#%% Now let's plot some error bar.
#We want: for each r, a mean an std
    
#s01_m = [np.mean(s) for s in Sampen_01]
#s01_std = [np.std(s) for s in Sampen_01]
#s09_m = [np.mean(s) for s in Sampen_09]
#s09_std = [np.std(s) for s in Sampen_09]

#now x-axis is going to be r, y-axis mean sampen, error std

#plt.errorbar(r,s01_m,s01_std,fmt = 'o-',label = 'Sampen Mix 0.1')
#plt.errorbar(r,s09_m,s09_std,fmt = '^-',label = 'Sampen Mix 0.9')
#plt.xscale('log')
#plt.legend()
