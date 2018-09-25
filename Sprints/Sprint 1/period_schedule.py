# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 06:15:24 2018

@author: Scott Warnock
"""

period_BCWS, period_BCWP, period_ACWP = 0, 0, 0

def period_Schedule():
    period_SPI = period_BCWP / period_BCWS
    period_SV = period_BCWP - period_BCWS
    return period_SPI, period_SV