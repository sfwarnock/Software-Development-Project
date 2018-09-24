# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:48:38 2018

@author: Scott Warnock
"""

def ev_MetricTypes(csv_DataFrame):
    acwp_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'ACWP']
    bcwp_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWP']
    bcws_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWS']