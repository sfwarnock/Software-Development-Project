# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 06:15:24 2018

@author: Scott Warnock
"""

period_BCWS, period_BCWP, period_ACWP = 0, 0, 0

def period_Schedule(period_DataFrame, headerValues):
    period_BCWP = period_DataFrame.loc['Period Total Planned', headerValues]
    period_BCWS = period_DataFrame.loc['Period Total Earned', headerValues]
    
    period_SPI = period_BCWP / period_BCWS
    period_SV = period_BCWP - period_BCWS
    
    period_DataFrame.loc['Period SV'] = period_SV
    period_DataFrame.loc['Period SPI'] = period_SPI
    return period_SPI, period_SV