# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:00:05 2019

@author: Patrick Plum

Description: This program is the master program to the slides and should be run as it calls all other scripts
"""


############################### Import other scripts and variables ##########################################
import pandas as pd

import ReadData
from ReadData import crix
from ReadData import dates_of_first
from ReadData import dates_of_others
from ReadData import dates_of_ind_rebalance
from ReadData import logreturn_at_first
from ReadData import logreturn_others
from ReadData import logreturn_at_rebalance
from ReadData import crix_constituents

import WordCloudCRIX

import PlotNumberofConst

import DailyLogReturns
from DailyLogReturns import mean_logreturn_at_first
from DailyLogReturns import mean_logreturn_at_rebalance
from DailyLogReturns import mean_logreturn_others
from DailyLogReturns import var_logreturn_at_first
from DailyLogReturns import var_logreturn_at_rebalance
from DailyLogReturns import var_logreturn_others

import Inference

from Inference import ttest
from Inference import Ftest
from Inference import SWtest_first
from Inference import SWtest_others
from Inference import BFtest
from Inference import MWUtest

######################################## Summary ############################################################

#daily returns of first of the month have about 2.5*expected value and roughly 40% of the variance
comp_mean = mean_logreturn_at_first/mean_logreturn_others
comp_var = var_logreturn_at_first/var_logreturn_others
ratios= pd.DataFrame([['ratio of means',comp_mean],['ratio of variances',comp_var]])

testdata=[['t', ttest[0],ttest[1]],['F', Ftest[0],Ftest[1]],['Shapiro-Wilk`s for 1st of month', SWtest_first[0],SWtest_first[1]],['Shapiro-Wilk`s for 1st of other days',SWtest_others[0],SWtest_others[1]],['Brown-Forsythe', BFtest[0],BFtest[1]],['Mann-Whitney-U', MWUtest[0],MWUtest[1]]]
tests=pd.DataFrame(testdata, columns=['test','statistic','p-value'])

print(ratios)
print(tests)

##############################################################################################################