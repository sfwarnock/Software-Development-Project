# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 06:15:23 2018

@author: Scott Warnock
"""
period_BCWS, period_BCWP, period_ACWP = 0, 0, 0

def period_Cost():
    period_CPI = period_BCWP / period_ACWP
    period_CV = period_BCWP - period_ACWP
    return period_CPI, period_CV