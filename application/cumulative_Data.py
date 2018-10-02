# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 06:15:46 2018

@author: Scott Warnock
"""

def cumulative_Data(period_DataFrame):
    cum_DataFrame = period_DataFrame

    cum_DataFrame.loc['Cumulative Total Cost'] = cum_DataFrame.loc['Period Total Cost'].cumsum()
    cum_DataFrame.loc['Cumulative Planned Value'] = cum_DataFrame.loc['Period Total Planned'].cumsum()
    cum_DataFrame.loc['Cumulative Earned Value'] = cum_DataFrame.loc['Period Total Earned'].cumsum()
    print(cum_DataFrame)
    return cum_DataFrame