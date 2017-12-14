#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:49:12 2017

@author: obarquero
"""

#script to download database into local directory

import wfdb
import os

#%%
# Create a folder where download the entire database
#
# Make a temporary download directory in your current working directory
cwd = os.getcwd()
dldir = os.path.join(cwd, 'ctu_database')
# Make sure to use a new directory
if(os.path.exists(dldir)) :
    print "Folder already existed"
else:
    wfdb.dldatabase('ctu-uhb-ctgdb', dlbasedir = dldir)

# Display the downloaded content in the folder
print os.listdir(dldir)


#%%
# Read one and plot
#
#record = wfdb.rdsamp('ctu_database/1001')
#wfdb.plotrec(record)

signals, fields=wfdb.srdsamp('ctu_database/1001', channels=[0, 1], sampfrom=100, sampto=15000)
plot(signals)
print signals
print fields
