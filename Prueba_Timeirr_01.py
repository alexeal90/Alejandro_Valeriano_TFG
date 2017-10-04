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

r = np.logspace(-2,0,30) #vector of r
hrv = HRV_entropy() #create class of hrv entropy

Timeirr_01 = []
Timeirr_05 = []
Timeirr_09 = []

for ii, r_aux in enumerate(r):
    print (ii, 'of', len(r))
    print (r_aux)
    Timeirr_aux_01 = [] #save sampen for each 100 simulations for a given r
    Timeirr_aux_05 = []
    Timeirr_aux_09 = []
    for i in range(10):
        Mix1 = mix(500,0.1)
        Mix5 = mix(500,0.1)
        Mix9 = mix(500,0.9)

        #S1 = hrv.TimeIrreversibility(Mix1[:,0],r = r_aux)
        #S5 = hrv.TimeIrreversibility(Mix1[:,0],r = r_aux)
        #S9 = hrv.TimeIrreversibility(Mix9[:,0],r = r_aux)
        Timeirr_aux_01.append(S1)
        Timeirr_aux_05.append(S5)
        Timeirr_aux_09.append(S9)

    Timeirr_01.append(Timeirr_aux_01)
    Timeirr_05.append(Timeirr_aux_05)
    Timeirr_09.append(Timeirr_aux_09)


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
