# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:13:44 2019

@author: Patrick Plum

Description: This script plots the number of CRIX constituents over time
- called by: CRIXRebalancingMaster.py - pls run the latter
"""

############################### Import Modules #############################################

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from __main__ import dates_of_ind_rebalance
from __main__ import dates_of_first
from __main__ import crix_constituents


##################### Amount of currencies at a certain time preiod ########################

#amount of currencies in each period
n = []
for i in dates_of_first:
    n.append(len(crix_constituents.loc[i]))

#plotting number of constituents over time
fig=plt.figure(figsize=(18,12))
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.tick_params(axis='both', which='major', labelsize=20)
axes.set_aspect(aspect=9)
x=dates_of_first
y=n
axes.plot(x,y,'go',mew=3,ms=15)
plt.grid(b='TRUE', which='both', axis='x', color='#666666', linestyle='-',alpha=0.7)
axes.set_facecolor('white')
plt.xticks(dates_of_ind_rebalance[:-1])
myFmt = mdates.DateFormatter('%Y-%m-%d')
axes.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()
plt.savefig('Nr_of_Cryptos.png')

############################################################################################
