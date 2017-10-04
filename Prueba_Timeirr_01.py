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
Timeirr_05 = []
Timeirr_09 = []
asi_01 = []
asi_05 = []
asi_09 = []

tau  = 10
N = 300*tau
for i in range(10):
    Mix1 = mix(N,0.1)
    Mix5 = mix(N,0.1)
    Mix9 = mix(N,0.9)

    asi_1,tirr_1 = hrv.TimeIrreversibility(Mix1[:,0],tau)
    asi_5,tirr_5 = hrv.TimeIrreversibility(Mix5[:,0],tau)
    asi_9,tirr_9 = hrv.TimeIrreversibility(Mix9[:,0],tau)
    
    
    Timeirr_01.append(tirr_1)
    Timeirr_05.append(tirr_5)
    Timeirr_09.append(tirr_9)
    asi_01.append(asi_1)
    asi_05.append(asi_5)
    asi_09.append(asi_9)

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
