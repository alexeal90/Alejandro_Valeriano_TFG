# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:54:17 2017

@author: Alex
"""

from mix_processes import mix
from HRV_Entropy import HRV_entropy
import matplotlib.pyplot as plt

import numpy as np
import scipy as sc

r = np.logspace(-2,0,30) #vector of r
hrv = HRV_entropy() #create class of hrv entropy

Sampen_01 = []
Sampen_09 = []

for ii, r_aux in enumerate(r):
    print (ii, 'of', len(r))
    print (r_aux)
    Sampen_aux_01 = [] #save sampen for each 100 simulations for a given r
    Sampen_aux_09 = []
    for i in range(10):
        Mix1 = mix(200,0.1)
        Mix9 = mix(200,0.9)

        S1 = hrv.SampEn(Mix1[:,0],r = r_aux)
        S9 = hrv.SampEn(Mix9[:,0],r = r_aux)
        Sampen_aux_01.append(S1)
        Sampen_aux_09.append(S9)

    Sampen_01.append(Sampen_aux_01)
    Sampen_09.append(Sampen_aux_09)


#%% Now let's plot some error bar.
#We want: for each r, a mean an std
    
s01_m = [np.mean(s) for s in Sampen_01]
s01_std = [np.std(s) for s in Sampen_01]
s09_m = [np.mean(s) for s in Sampen_09]
s09_std = [np.std(s) for s in Sampen_09]

#now x-axis is going to be r, y-axis mean sampen, error std

plt.errorbar(r,s01_m,s01_std,fmt = 'o-',label = 'Sampen Mix 0.1')
plt.errorbar(r,s09_m,s09_std,fmt = '^-',label = 'Sampen Mix 0.9')
plt.xscale('log')
plt.legend()
