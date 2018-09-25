# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:48:38 2018

@author: Scott Warnock
"""

def ev_MetricTypes(csv_DataFrame):
    acwp_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'ACWP']
    bcwp_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWP']
    bcws_DataFrame = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWS']
    
    headerValues = dataFrame.columns.values[6:].tolist()
    
    acwp.loc['Period Total Cost', headerValues] = acwp[headerValues].sum()
    bcwp.loc['Period Total Earned', headerValues] = bcwp[headerValues].sum()
    bcws.loc['Period Total Planned', headerValues] = bcws[headerValues].sum()
    
    acwp['Total Cost'] = acwp.loc[:,headerValues].sum(axis=1)
    bcwp['Total Earned'] = bcwp.loc[:,headerValues].sum(axis=1)
    bcws['Total Planned'] = bcws.loc[:,headerValues].sum(axis=1)