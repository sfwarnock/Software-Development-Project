# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 06:09:29 2018

@author: Scott Warnock
"""

cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0 

def cum_Cost(data_file):
    cum_CV = cum_BCWP - cum_ACWP
    cum_CPI = cum_BCWP / cum_ACWP