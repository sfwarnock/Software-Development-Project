# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:52:53 2018

@author: Scott Warnock
"""

import pandas as pd

def ev_MetricTypes(data_file):
    acwp = data_file.loc[data_file['Value Type'] == 'ACWP']
    bcwp = data_file.loc[data_file['Value Type'] == 'BCWP']
    bcws = data_file.loc[data_file['Value Type'] == 'BCWS']
    return acwp, bcwp, bcws


def csv_Read():
    data_file = pd.read_csv('datafile.csv').fillna(0)
    return data_file