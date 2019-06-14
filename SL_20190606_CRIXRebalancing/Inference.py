# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:32:05 2019

@author: Patrick Plum

Description: This script compares 1st-day-of-a-month daily log returns with those of 1st-day-of-every-3rd-month (rebalancing date of number of constituents of the CRIX) and in particular with those of all other days
It performs parametric tests for testing difference in variance and mean as well as non-parametric tests. 
Meanwhile, it also tests for normality
- called by: CRIXRebalancingMaster.py - pls run the latter
"""

############################# Import Modules and data #######################################

import numpy as np
import matplotlib.pyplot as plt

import scipy
import statsmodels.graphics.gofplots as sp
import statsmodels.stats.weightstats as ws

from __main__ import logreturn_at_first
from __main__ import logreturn_others
from __main__ import logreturn_at_rebalance



#########################for normal data, paramteric tests ###################################

var_logreturn_at_first=np.var(logreturn_at_first)
var_logreturn_others=np.var(logreturn_others)

# F-Test
F=var_logreturn_at_first/var_logreturn_others #teststatistic, F-distributed (=comp_var)
df1 = len(logreturn_at_first) - 1   #degrees of freedom1
df2 = len(logreturn_others) - 1     #degrees of freedom2
Ftest_pvalue=scipy.stats.f.cdf(F,df1,df2) 
Ftest=(F,Ftest_pvalue,df1,df2)
# reject, if small -> clearly reject

# t-test for checking, if means are significantly different - assumption: normality, variance equal or not according to previus result
if Ftest_pvalue>0.05:
    ttest=ws.ttest_ind(logreturn_at_first,logreturn_others,alternative='larger',usevar='equal')
else: 
    ttest=ws.ttest_ind(logreturn_at_first,logreturn_others,alternative='larger',usevar='unequal')


#################################### Testing for normality #################################

# QQPLots
    
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
fig1=sp.qqplot(logreturn_others, line='45',fit='TRUE',color='blue',alpha=0.5,marker='o',ax=ax1)

ax2 = fig.add_subplot(1, 1, 1)
fig2=sp.qqplot(logreturn_at_first, line='45',fit='TRUE',color='green',marker='+',ms=10,ax=ax2)
plt.axis('scaled')
plt.xticks(np.arange(-6, 7, 2))
plt.yticks(np.arange(-6, 7, 2))
plt.ylim(-7,7)
plt.xlim(-7,7)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
ax=plt.gca()
ax.set_facecolor('white')
plt.gcf()
fig.tight_layout()
plt.savefig('QQPlots.png')



# Shapiro Wilk's test
SWtest_first=scipy.stats.shapiro(logreturn_at_first)
SWtest_others=scipy.stats.shapiro(logreturn_others)
# If p-value (= 2nd entry is small, reject normality)


##################################for non-normal: non-paramteric test ######################
#only account for values within 2 standard deviations ->95% center ->cut 2.5% on each side
BFtest=tuple(scipy.stats.levene(logreturn_others,logreturn_at_first,center='trimmed',proportiontocut=0.025))

# Mann-Whitney-U Test for hypothesis test if distributions are similar
MWUtest=tuple(scipy.stats.mannwhitneyu(logreturn_at_first,logreturn_others,alternative='greater'))

############################################################################################
