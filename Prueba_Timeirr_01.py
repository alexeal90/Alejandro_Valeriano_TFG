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

Timeirr_01 = []
Timeirr_02 = []
Timeirr_03 = []
Timeirr_04 = []
Timeirr_05 = []
Timeirr_06 = []
Timeirr_07 = []
Timeirr_08 = []
Timeirr_09 = []

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

t01_m = [np.mean(s) for s in Timeirr_01]
t01_std = [np.std(s) for s in Timeirr_01]
t02_m = [np.mean(s) for s in Timeirr_02]
t02_std = [np.std(s) for s in Timeirr_02]
t03_m = [np.mean(s) for s in Timeirr_03]
t03_std = [np.std(s) for s in Timeirr_04]
t04_m = [np.mean(s) for s in Timeirr_04]
t04_std = [np.std(s) for s in Timeirr_04]
t05_m = [np.mean(s) for s in Timeirr_05]
t05_std = [np.std(s) for s in Timeirr_05]
t06_m = [np.mean(s) for s in Timeirr_06]
t06_std = [np.std(s) for s in Timeirr_06]
t07_m = [np.mean(s) for s in Timeirr_07]
t07_std = [np.std(s) for s in Timeirr_07]
t08_m = [np.mean(s) for s in Timeirr_08]
t08_std = [np.std(s) for s in Timeirr_08]
t09_m = [np.mean(s) for s in Timeirr_09]
t09_std = [np.std(s) for s in Timeirr_09]

P_tau = np.arange(0.1, 1, 0.1)

plt.errorbar(P_tau,t01_m,t01_std,fmt = 'o-')
plt.errorbar(P_tau,t02_m,t02_std,fmt = 'o-')
plt.errorbar(P_tau,t03_m,t03_std,fmt = 'o-')
plt.errorbar(P_tau,t04_m,t04_std,fmt = 'o-')
plt.errorbar(P_tau,t05_m,t05_std,fmt = 'o-')
plt.errorbar(P_tau,t06_m,t06_std,fmt = 'o-')
plt.errorbar(P_tau,t07_m,t07_std,fmt = 'o-')
plt.errorbar(P_tau,t08_m,t08_std,fmt = 'o-')
plt.errorbar(P_tau,t09_m,t09_std,fmt = 'o-')

