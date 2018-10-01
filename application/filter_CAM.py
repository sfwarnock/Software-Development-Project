# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 06:21:41 2018

@author: Scott Warnock
"""

def filter_CAM():
    filter_CAM = pd.pivot_table(period_DataFrame, values = csv_header, index=['CAM','Charge Code' 'Value Type'])
    return filter_CAM