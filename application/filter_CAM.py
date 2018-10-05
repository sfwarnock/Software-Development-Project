# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 06:21:41 2018

@author: Scott Warnock
"""

def filter_CAM(period_DataFrame, cum_DataFrame, csv_DataFrame, csv_header):
    filter_CAM_csv = pd.pivot_table(csv_DataFrame, values = csv_header, index=['CAM','Charge Code' 'Value Type'])
    filter_CAM_period = pd.pivot_table(period_DataFrame, values = csv_header, index=['CAM','Charge Code' 'Value Type'])
    filter_CAM_cum = pd.pivot_table(cum_DataFrame, values = csv_header, index=['CAM','Charge Code' 'Value Type'])
    return filter_CAM_csv, filter_CAM_period, filter_CAM_cum