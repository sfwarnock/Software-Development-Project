# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:52:53 2018

@author: Scott Warnock
"""

import pandas as pd


cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0 

def csv_Read():
    csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)
    print(csv_DataFrame)
    
def ev_MetricTypes(csv_DataFrame):
    acwp_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'ACWP']
    bcwp_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWP']
    bcws_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWS']
    
def cum_Schedule():
    cum_SV = cum_BCWP - cum_BCWS
    cum_SPI = cum_BCWP / cum_BCWS
    
def cum_Cost(data_file):
    cum_CV = cum_BCWP - cum_ACWP
    cum_CPI = cum_BCWP / cum_ACWP
    
def main():
    csv_Read()
    ev_MetricTypes()
    cum_Schedule()
    cum_Cost()
    
main()