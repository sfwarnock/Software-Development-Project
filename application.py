# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:52:53 2018

@author: Scott Warnock
"""

import pandas as pd

cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0
period_BCWS, period_BCWP, period_ACWP = 0, 0, 0

def main():
    csv_DataFrame, csv_header, headerValues = csv_Read()
    period__DataFrame = period_Data(csv_DataFrame, csv_header, headerValues)
    cum_DataFrame = cumualative_Data(period_DataFrame)
    
    
main()
    
def csv_Read():
    csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)
    csv_header = csv_DataFrame.columns.values.tolist()
    headerValues = csv_DataFrame.columns.values[6:].tolist()
    return csv_DataFrame, csv_header, headerValues
    
def period_Data(csv_DataFrame, csv_header, headerValues):
    acwp = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'ACWP']
    acwp.loc['Period Total Cost', headerValues] = acwp[headerValues].sum()
    acwp['Total Actual Cost'] = acwp.loc[:,headerValues].sum(axis=1)
    acwp_header = acwp.columns.values.tolist()
    for columnHeaders in acwp_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue
        
    bcwp = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWP']
    bcwp.loc['Period Total Earned', headerValues] = bcwp[headerValues].sum()    
    bcwp['Total Earned'] = bcwp.loc[:,headerValues].sum(axis=1)
    bcwp_header = bcwp.columns.values.tolist()
    for columnHeaders in bcwp_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue
        
    bcws = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWS']
    bcws.loc['Period Total Planned', headerValues] = bcws[headerValues].sum()
    bcws['Total Planned'] = bcws.loc[:,headerValues].sum(axis=1)
    bcws_header = bcws.columns.values.tolist()
    for columnHeaders in bcws_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue
        
    period_DataFrame = pd.concat([acwp, bcwp, bcws], sort = True).sort_values(by='CAM').reindex(columns = csv_header).fillna(0)
    print (period_DataFrame)
    return period_DataFrame
    
def period_Cost(period_DataFrame, headerValues):
    period_BCWP = period_DataFrame.loc['Period Total Planned', headerValues]
    period_ACWP = period_DataFrame.loc['Period Total Cost', headerValues]
    
    period_CPI = period_BCWP / period_ACWP
    period_CV = period_BCWP - period_ACWP
    
    period_DataFrame.loc['Period CV'] = period_CV
    period_DataFrame.loc['Period CPI'] = period_CPI
    return period_CPI, period_CV

def period_Schedule(period_DataFrame, headerValues):
    period_BCWP = period_DataFrame.loc['Period Total Planned', headerValues]
    period_BCWS = period_DataFrame.loc['Period Total Earned', headerValues]
    
    period_SPI = period_BCWP / period_BCWS
    period_SV = period_BCWP - period_BCWS
    
    period_DataFrame.loc['Period SV'] = period_SV
    period_DataFrame.loc['Period SPI'] = period_SPI
    return period_SPI, period_SV

def filter_ChargeCode(period_DataFrame, csv_header):
    filter_ChargeCode = pd.pivot_table(period_DataFrame, values = csv_header, index=['Charge Code', 'CAM', 'Value Type'])
    return filter_ChargeCode

def filter_CAM(period_DataFrame, csv_header):
    filter_CAM = pd.pivot_table(period_DataFrame, values = csv_header, index=['CAM','Charge Code' 'Value Type'])
    return filter_CAM

def cumualative_Data(period_DataFrame):
    cum_DataFrame = period_DataFrame

    cum_DataFrame.loc['Cumualative Total Cost'] = cum_DataFrame.loc['Period Total Cost'].cumsum()
    cum_DataFrame.loc['Cumualative Planned Value'] = cum_DataFrame.loc['Period Total Planned'].cumsum()
    cum_DataFrame.loc['Cumualative Earned Value'] = cum_DataFrame.loc['Period Total Earned'].cumsum()
    return cum_DataFrame

def cum_Schedule():
    cum_SV = cum_BCWP - cum_BCWS
    cum_SPI = cum_BCWP / cum_BCWS
    return cum_SV, cum_SPI
    
def cum_Cost(data_file):
    cum_CV = cum_BCWP - cum_ACWP
    cum_CPI = cum_BCWP / cum_ACWP
    return cum_CV, cum_CPI