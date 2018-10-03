# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 06:09:29 2018

@author: Scott Warnock
"""

cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0 

def cum_Cost(cum_DataFrame, headerValues):
    cum_BCWP = cum_DataFrame.loc['Cumulative Earned Value', headerValues]
    cum_ACWP = cum_DataFrame.loc['Cumulative Total Cost', headerValues]
    
    cum_CV = cum_BCWP - cum_ACWP
    cum_CPI = cum_BCWP / cum_ACWP
    
    cum_DataFrame.loc['CPI'] = cum_CPI
    cum_DataFrame.loc['CV'] = cum_CV
    return cum_CV, cum_CPI