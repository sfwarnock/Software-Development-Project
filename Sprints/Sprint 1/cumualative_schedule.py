# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 06:09:32 2018

@author: 175272
"""

cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0 

def cum_Schedule():
    cum_SV = cum_BCWP - cum_BCWS
    cum_SPI = cum_BCWP / cum_BCWS
    return cum_SV, cum_SPI