# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 06:15:46 2018

@author: Scott Warnock
"""

def cumualative_Data():
    cum_DataFrame = period_DataFrame

    cum_DataFrame.loc['Cumualative Total Cost'] = cum_DataFrame.loc['Period Total Cost'].cumsum()
    cum_DataFrame.loc['Cumualative Planned Value'] = cum_DataFrame.loc['Period Total Planned'].cumsum()
    cum_DataFrame.loc['Cumualative Earned Value'] = cum_DataFrame.loc['Period Total Earned'].cumsum()
    return cum_DataFrame