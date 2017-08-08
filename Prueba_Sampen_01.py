# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:54:17 2017

@author: Alex
"""

from mix_processes import *
from HRV_Entropy import *

import numpy as np
import scipy as sc

r = np.logspace(-2,0,100) #vector of r
hrv = HRV_entropy() #create class of hrv entropy

Sampen_01 = []
Sampen_09 = []

for r_aux in r:
    Sampen_aux_01 = []
    Sampen_aux_09 = []
    for i in range(100):
        Mix1 = mix(1000,0.1)
        Mix9 = mix(1000,0.9)

        S1 = hrv.Sampen(mix1[:,0],r = r_aux)
        S2 = hrv.Sampen(mix9[:,0],r = r_aux)
        Sampen_aux_01.append(S1)
        Sampen_aux_09.append(S9)

    Sampen_01.append(Sampen_aux_01)
    Sampen_09.append(Sampen_aux_09)


Plot (errorbarr)

