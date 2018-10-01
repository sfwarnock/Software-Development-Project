# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 06:15:23 2018

@author: Scott Warnock
"""
period_BCWS, period_BCWP, period_ACWP = 0, 0, 0

def period_Cost():
    period_CPI = period_BCWP / period_ACWP
    period_CV = period_BCWP - period_ACWP
    
    period_BCWP = period_DataFrame.loc['Period Total Planned', headerValues]
    period_ACWP = period_DataFrame.loc['Period Total Cost', headerValues]
    
    period_DataFrame.loc['Period CV'] = period_CV
    period_DataFrame.loc['Period CPI'] = period_CPI
    return period_CPI, period_CV