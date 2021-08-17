#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 12:11:25 2021

@author: emmadevin
"""

import glob
import os.path as path
import numpy as np
import dread
import time
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt



#read in the cut and corrected spectra = records
#records are in m/s
#should be binned frequencies and amplitudes
#make list of records and the corresponding events and stations

# working directory and outfil path for inversion
working_dir = '/Users/emmadevin/Work/USGS 2021/Data/Prelim'
outfile_path = working_dir + '/Andrews_inversion'

# df with station locations
stations = pd.read_csv(working_dir + '/station_locs.csv')

# list of record files
record_list = glob.glob(working_dir + '/record_spectra/*/*')

# list of files
   
    
# get lists of station ids and station locations
stn_list = (stations['network']+stations['station']).tolist()
stn_lat = stations['latitude']
stn_lon = stations['longitude']


df = pd.DataFrame()

amp1 = []
amp2 = []
amp3 = []
amp4 = []
amp5 = []
f1 = 0.01
f2 = 0.1
f3 = 1.0
f4 = 10
distlist = []


for record in record_list: 
    
    base = record.split('/')[-1]
    eventid = base.split('_')[-1]
    eventid = eventid.split('.')[0]
    ntwk = base.split('_')[0]
    stn = base.split('_')[1]
    stn_id = ntwk + stn
    
    # print some updates to track progress
    print('Event: ', eventid)
    print('Station: ', stn)
    
    # read phase file fo get event locations
    phase_file = working_dir + '/RC_phase_beta/' + eventid + '.phase'
    phase = pd.read_csv(phase_file, sep = '\s+', index_col=0, nrows = 0).columns.tolist()
    
    # assign event coordinates and depth
    evlat = float(phase[4])
    evlon = float(phase[5])
    evdepth = float(phase[6])
    
    # assign station corrdinates and depth
    stlat = stn_lat[stn_list.index(stn_id)]
    stlon = stn_lon[stn_list.index(stn_id)]
    stdepth = 0
    
    #find distance between event and station
    dist =  dread.compute_rrup(evlon, evlat, evdepth, stlon, stlat, stdepth) #in km
    distlist.append(dist)
    
    #read in record
    data = np.genfromtxt(record, dtype = float, comments = '#', delimiter = None, usecols = (0,1,2))  #only read in first two cols
    
    amp1.append(data[7,1])
    amp2.append(data[30,1])
    amp3.append(data[52,1])
    amp4.append(data[74,1])
    
    
  
df['record'] = record_list
df['amp:f1'] = amp1
df['amp:f2'] = amp2
df['amp:f3'] = amp3
df['amp:f4'] = amp4

df['dist'] = distlist

edges = np.logspace(1,2,10)

bin_means1, bin_edges1, binnumber1 = stats.binned_statistic(df['dist'], df['amp:f1'], statistic='mean', bins=edges)
bin_width1 = (bin_edges1[1] - bin_edges1[0])
bin_centers1 = bin_edges1[1:] - bin_width1/2

bin_means2, bin_edges2, binnumber2 = stats.binned_statistic(df['dist'], df['amp:f2'], statistic='mean', bins=edges)
bin_width2 = (bin_edges2[1] - bin_edges2[0])
bin_centers2 = bin_edges2[1:] - bin_width2/2

bin_means3, bin_edges3, binnumber3 = stats.binned_statistic(df['dist'], df['amp:f3'], statistic='mean', bins=edges)
bin_width3 = (bin_edges3[1] - bin_edges3[0])
bin_centers3 = bin_edges3[1:] - bin_width3/2

bin_means4, bin_edges4, binnumber4 = stats.binned_statistic(df['dist'], df['amp:f4'], statistic='mean', bins=edges)
bin_width4 = (bin_edges4[1] - bin_edges4[0])
bin_centers4 = bin_edges4[1:] - bin_width4/2

plt.scatter(distlist,amp4, edgecolors = 'grey', facecolors = 'none', label = 'data')
plt.scatter(bin_centers4,bin_means4, label = 'binned means')


x = np.logspace(1,3,100)
y = 1/16000*1/x
plt.plot(x,y, c = 'k',label = '~1/r')

plt.xscale('log')
plt.yscale('log')
plt.xlim(6,11**2)
plt.ylim(10**-10, 10**-4)
plt.xlabel('distance (km)')
plt.ylabel('amplitude')
plt.title('f = '+str(f4)+' Hz')
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), facecolor = 'w', ncol = 2, fontsize = 10)

  