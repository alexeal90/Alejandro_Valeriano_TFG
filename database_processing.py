#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:46:36 2017

Database preprocessing TFG Alejandro 

@author: obarquero
"""


import wfdb
import os
import numpy as np
import glob


#%% Read and process database
#
cwd = os.getcwd()
dldir = os.path.join(cwd, 'ctu_database/')


#loop over .dat files
for filename in glob.iglob(dldir+'*.dat'):
     #print(dldir+'/%s' % filename)
     
     #get fname
     fname = os.path.basename(filename)
     
     #get dot idx
     dot_idx = fname.index('.')
     
     fet_id = fname[:dot_idx]
     
     #get signal and header info
     #samp_end 30 min
     #4Hz, so 30*60 = sec and samp = 
     fs = 4. #Hz
     dur = 30 #min
     samp_end = int((dur*60)*fs)
     signals, fields=wfdb.srdsamp(dldir + fet_id, channels=[0, 1], sampfrom=0, sampto=samp_end)
     
     fhr = signals[:,0]
     uc = signals[:,1]
     t = np.arange(0,len(signals))/fs
     
     #simple correction
     uc = uc[fhr!=0]
     fhr = fhr[fhr != 0]
     t_c = np.arange(0,len(fhr))/fs
     exit
     ##ALEX CODE#####
     
     #definition of the dict
     
    #computing each index
    #sampen
    
    #timeirrev
    
    #save all the information needed into the dict
    
    #save dict using np.save
     
     ##ALEX CODE#####

