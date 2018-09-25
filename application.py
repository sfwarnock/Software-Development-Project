# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:52:53 2018

@author: Scott Warnock
"""

import pandas as pd


cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0
period_BCWS, period_BCWP, period_ACWP = 0, 0, 0

def main():
    csv_Read()
    cum_Schedule()
    cum_Cost()
    
main()
    
def csv_Read():
    csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)
    print(csv_DataFrame)
    
def ev_MetricTypes(csv_DataFrame):
    acwp_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'ACWP']
    bcwp_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWP']
    bcws_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWS']
    
    headerValues = dataFrame.columns.values[6:].tolist()
    
    acwp.loc['Period Total Cost', headerValues] = acwp[headerValues].sum()
    bcwp.loc['Period Total Earned', headerValues] = bcwp[headerValues].sum()
    bcws.loc['Period Total Planned', headerValues] = bcws[headerValues].sum()

def cum_Schedule():
    cum_SV = cum_BCWP - cum_BCWS
    cum_SPI = cum_BCWP / cum_BCWS
    return cum_SV, cum_SPI
    
def cum_Cost(data_file):
    cum_CV = cum_BCWP - cum_ACWP
    cum_CPI = cum_BCWP / cum_ACWP
    return cum_CV, cum_CPI
    
def period_Cost():
    period_CPI = period_BCWP / period_ACWP
    period_CV = period_BCWP - period_ACWP
    return period_CPI, period_CV

def period_Schedule():
    period_SPI = period_BCWP / period_BCWS
    period_SV = period_BCWP - period_BCWS
    return period_SPI, period_SV