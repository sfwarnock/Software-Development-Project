# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 06:36:10 2018

@author: Scott Warnock
"""

def bugeted_cost_work_remaining(cum_DataFrame, bcwp, bac):
    percent_complete = bcwp / bac                  
    bcwr = bac - bcwp
    return percent_complete, bcwr