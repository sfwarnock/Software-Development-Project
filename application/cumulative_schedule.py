# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 06:09:32 2018

@author: Scott Warnock
"""

cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0 

def cum_Schedule(cum_DataFrame, headerValues):
    cum_BCWP = cum_DataFrame.loc['Cumulative Earned Value', headerValues]
    cum_BCWS = cum_DataFrame.loc['Cumulative Planned Value', headerValues]
    
    cum_SV = cum_BCWP - cum_BCWS
    cum_SPI = cum_BCWP / cum_BCWS
    
    cum_DataFrame.loc['SPI'] = cum_SPI
    cum_DataFrame.loc['SV'] = cum_SV
    return cum_SV, cum_SPI