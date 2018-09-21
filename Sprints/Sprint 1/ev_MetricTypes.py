# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:48:38 2018

@author: Scott Warnock
"""

def ev_MetricTypes(data_file):
    acwp = data_file.loc[data_file['Value Type'] == 'ACWP']
    bcwp = data_file.loc[data_file['Value Type'] == 'BCWP']
    bcws = data_file.loc[data_file['Value Type'] == 'BCWS']
    return acwp, bcwp, bcws