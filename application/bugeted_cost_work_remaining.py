# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 06:36:10 2018

@author: Scott Warnock
"""

def bugeted_cost_work_remaining(cum_DataFrame):
    bac = cum_DataFrame['Total Cost'].sum()
    bcwp =cum_DataFrame.loc['Period Total Earned', 'Total Earned']
    percent_complete = bcwp / bac                  
    bcwr = bac - bcwp
    return percent_complete, bcwr, bac