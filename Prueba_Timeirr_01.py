# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:51:31 2017

@author: Alex
"""

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

T_irr = [[0 for x in range(10)] for y in range(9)]

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

    T_irr_aux = np.arange(9)

    asi_1,T_irr_aux[0] = hrv.TimeIrreversibility(Mix1[:,0],tau)
    asi_2,T_irr_aux[1] = hrv.TimeIrreversibility(Mix2[:,0],tau)
    asi_3,T_irr_aux[2] = hrv.TimeIrreversibility(Mix3[:,0],tau)
    asi_4,T_irr_aux[3] = hrv.TimeIrreversibility(Mix4[:,0],tau)
    asi_5,T_irr_aux[4] = hrv.TimeIrreversibility(Mix5[:,0],tau)
    asi_6,T_irr_aux[5] = hrv.TimeIrreversibility(Mix6[:,0],tau)
    asi_7,T_irr_aux[6] = hrv.TimeIrreversibility(Mix7[:,0],tau)
    asi_8,T_irr_aux[7] = hrv.TimeIrreversibility(Mix8[:,0],tau)
    asi_9,T_irr_aux[8] = hrv.TimeIrreversibility(Mix9[:,0],tau)
    
    
    for j in range(9):
        T_irr[j][i] = T_irr_aux[j]

T_irr_mean = np.arange(9)
T_irr_std = np.arange(9)
for k, l in enumerate(T_irr):
    T_irr_mean[k] = np.mean(T_irr[k])
    T_irr_std[k] = np.std(T_irr[k])

plt.errorbar(0.1,T_irr_mean[0],yerr = T_irr_std[0],fmt = 'o-')
plt.errorbar(0.2,T_irr_mean[1],yerr = T_irr_std[1],fmt = 'o-')
plt.errorbar(0.3,T_irr_mean[2],yerr = T_irr_std[2],fmt = 'o-')
plt.errorbar(0.4,T_irr_mean[3],yerr = T_irr_std[3],fmt = 'o-')
plt.errorbar(0.5,T_irr_mean[4],yerr = T_irr_std[4],fmt = 'o-')
plt.errorbar(0.6,T_irr_mean[5],yerr = T_irr_std[5],fmt = 'o-')
plt.errorbar(0.7,T_irr_mean[6],yerr = T_irr_std[6],fmt = 'o-')
plt.errorbar(0.8,T_irr_mean[7],yerr = T_irr_std[7],fmt = 'o-')
plt.errorbar(0.9,T_irr_mean[8],yerr = T_irr_std[8],fmt = 'o-')

