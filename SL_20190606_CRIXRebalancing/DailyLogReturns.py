# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:19:48 2019

@author: Patrick Plum

Description: This script plots daily log returns of the CRIX and provides first summary statistics for the three classes of dates
- called by: CRIXRebalancingMaster.py - pls run the latter
"""

############################# Import Modules and data #######################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from __main__ import dates_of_first
from __main__ import dates_of_others
from __main__ import dates_of_ind_rebalance
from __main__ import logreturn_at_first
from __main__ import logreturn_others
from __main__ import logreturn_at_rebalance


######### statistical inference on influence of index rebalancing ##########################


# plotting
fig=plt.figure(figsize=(40,12))

axes=fig.add_axes([0.1,0.1,0.8,0.8])
plt.grid(b='TRUE', which='major', color='#666666', linestyle='-',alpha=0.7)
axes.set_facecolor('white')
axes.set_aspect(aspect=800)
# ...dates of others
x1=dates_of_others
y1=logreturn_others
axes.plot(x1,y1,marker='',color='blue',alpha=0.7)
# ...dates of index amount rebalancing = 1st of each 3rd month
x3 = dates_of_ind_rebalance
y3 = logreturn_at_rebalance
axes.plot(x3,y3,'rx',mew=9, ms=30)
# ...dates of usual index change = 1st of a month
x2 = dates_of_first
y2 = logreturn_at_first
axes.plot(x2,y2,'g+',mew=9, ms=30)
axes.set_ylim([-0.25,0.25])
myFmt = mdates.DateFormatter('%Y-%m-%d')
axes.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()
axes.tick_params(axis='both', which='major', labelsize=30)
plt.savefig('DailyLogReturns.png')

############## Summary of mean and variances of daily log returns #########################

#mean
mean_logreturn_at_first=np.mean(logreturn_at_first)
mean_logreturn_at_rebalance=np.mean(logreturn_at_rebalance)
mean_logreturn_others=np.mean(logreturn_others)

#variance
var_logreturn_at_first=np.var(logreturn_at_first)
var_logreturn_at_rebalance=np.var(logreturn_at_rebalance)
var_logreturn_others=np.var(logreturn_others)

