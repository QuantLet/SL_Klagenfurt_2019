# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:03:37 2019

@author: Patrick Plum

Description: This script just reads data from CRIX and processes this data for the use in the other scripts
- called by: CRIXRebalancingMaster.py - pls run the latter
"""

############################### Import Modules ###########################################

import pandas as pd
import numpy as np
import json


############################### Read in data #############################################

# read crix_constituents file
crix_constituents = pd.read_csv('index_members.csv', parse_dates=True,index_col=[1])

# all constituents
crix_constituents_all= np.unique(crix_constituents.values.flatten())

with open('crix1.json', 'r') as myfile:
    crix=myfile.read()
    
# read all CRIX data
crix = json.loads(crix)
crix = pd.DataFrame(crix)

###############################  Pre-process for further use ###############################

# dates of index shift (=first of each month)
dates_of_first = np.unique(crix_constituents.index)
#converting to a more convenient data type
dates_of_first = pd.to_datetime(dates_of_first)

    
# convert dates to dateformat
crix['date'] = pd.to_datetime(crix['date'])

# calculation of logreturns and adding to the dataframe
crix['logreturn'] = np.log(crix['price']).diff()


# rebalancing of amount of constituents every 3 months
dates_of_ind_rebalance = []
i=0
while i<len(dates_of_first):
    dates_of_ind_rebalance.append(dates_of_first[i])
    i=i+3
# last month out of rule (see Nr_of_Cryptos.png)
dates_of_ind_rebalance.append(dates_of_first[i-1])

# get indices of monthly turns
ind=[]
#...and of the rebalancing months
ind2=[]

# go for the logreturns of these
for i in range(len(dates_of_first)):
    ind.append(crix.loc[crix['date'] == dates_of_first[i]].index[0])
for i in range(len(dates_of_ind_rebalance)):
    ind2.append(crix.loc[crix['date'] == dates_of_ind_rebalance[i]].index[0])
logreturn_at_first = crix.logreturn.loc[ind]
logreturn_at_rebalance = crix.logreturn.loc[ind2]

# get other indices
ind_others = list(range(0,len(crix)))
ind_others = list(set(ind_others)-set(ind))
ind_others.remove(0)

#... and get the logreturns of all other dates
logreturn_others=crix.logreturn[ind_others]
dates_of_others = crix.date[ind_others]


############################################################################################