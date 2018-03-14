#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:46:36 2017

Database preprocessing TFG Alejandro 

@author: obarquero
"""

from HRV_Entropy import HRV_entropy
import wfdb
import os
import numpy as np
import glob


#%% Read and process database
#
cwd = os.getcwd()
dldir = os.path.join(cwd, 'ctu_database/')
hrv = HRV_entropy()
index = 1

#get signal and header info
#samp_end 30 min
#4Hz, so 30*60 = sec and samp =
fs = 4. #Hz
dur = 30 #min
samp_end = int((dur*60)*fs)

sampen02_std = []

def get_value_from_field(field):
    """
    Function that gest a float value from a string in a field
    """
    
    field_aux = field.split()
    value = float(field_aux[1])
    
    return value

#def get_sampen_01(fhr):
#    s01 = hrv.SampEn(fhr,np.std(fhr))
    
#    return s01


#loop over .dat files to calculate r of Sampen02
for filename in glob.iglob(dldir+'*.dat'):
    
     fname = os.path.basename(filename)

     dot_idx = fname.index('.')    
     
     fet_id = fname[:dot_idx]
     
     signals, fields=wfdb.srdsamp(dldir + fet_id, channels=[0, 1], sampfrom=0, sampto=samp_end)
     
     fhr = signals[:,0]
     fhr = fhr[fhr != 0]
    
     sampen02_std.append(np.std(fhr))

r2 = np.mean(sampen02_std)

#loop over .dat files
for filename in glob.iglob(dldir+'*.dat'):
     #print(dldir+'/%s' % filename)
     print(index,'/',len(glob.glob(dldir+'*.dat')))
     index = index + 1
     #get fname
     fname = os.path.basename(filename)
     
     #get dot idx
     dot_idx = fname.index('.')
     
     fet_id = fname[:dot_idx]
     
     signals, fields=wfdb.srdsamp(dldir + fet_id, channels=[0, 1], sampfrom=0, sampto=samp_end)
     
     fhr = signals[:,0]
     uc = signals[:,1]
     t = np.arange(0,len(signals))/fs
     
     #simple correction
     uc = uc[fhr!=0]
     fhr = fhr[fhr != 0]
     t_c = np.arange(0,len(fhr))/fs
     #exit
     ##ALEX CODE#####
     
     #definition of the dict
     pH = fields['comments'][2]
     pH = get_value_from_field(pH)
     apgar_1 = fields['comments'][6]
     apgar_1 = get_value_from_field(apgar_1)
     
     apgar_5 = fields['comments'][7]
     apgar_5 = get_value_from_field(apgar_5)
     
     
     
     #fhr2 = fhr[0:9] #Cojo las 10 primeras muestras de cada fhr para que las pruebas sean mas cortas.
     
     r1 = np.std(fhr)
     sampen_r1 = hrv.SampEn(fhr,r = r1) #Luego cambiar fhr2 por fhr
     sampen_r2 = hrv.SampEn(fhr,r = r2) #Sale 0 porque fhr2 muy pequeño. Luego cambiar fhr2 por fhr
     
     tau = np.floor(len(fhr)/1200.)
     asi,time_irrever = hrv.TimeIrreversibility(fhr,tau)
     #print (len(fhr)) #Para comprobar que la longitud de cada fhr es diferente
     
     fet = {'id':fet_id,'sampen_r1':sampen_r1,'sampen_r2':sampen_r2,'time_irrever':time_irrever,
            'case':None,'pH':pH,'apgar_1':apgar_1,'apgar_5':apgar_5}
     
    #computing each index
    
    
    #sampen
    
    #timeirrev
    
    #save all the information needed into the dict
 #   fet['sampen_r1'] = 
    #save dict using np.save
     np.save(dldir + fet_id+'.npy',fet)  
     
     #to load fet dictionary
     #fet = np.load(dldir + fet_id+'.npy').flat[0]
     
     
     ##ALEX CODE#####

