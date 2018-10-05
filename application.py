# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:52:53 2018

@author: Scott Warnock
"""

import pandas as pd

cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0
period_BCWS, period_BCWP, period_ACWP = 0, 0, 0

def main():
    csv_DataFrame, csv_header, dateHeaderValues = csv_Read()
    period_DataFrame = period_Data(csv_DataFrame, csv_header, dateHeaderValues)
    period_Cost(period_DataFrame, dateHeaderValues)
    period_Schedule(period_DataFrame, dateHeaderValues)
    cum_DataFrame = cumulative_Data(period_DataFrame)
    cum_Cost(cum_DataFrame, dateHeaderValues)
    cum_Schedule(cum_DataFrame, dateHeaderValues)
    bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, project_SV = project_reporting(cum_DataFrame)
    print (bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, project_SV)
    print (cum_DataFrame)
      
def csv_Read():
    csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)
    csv_header = csv_DataFrame.columns.values.tolist()
    datedateHeaderValues = csv_DataFrame.columns.values[6:].tolist()
    return csv_DataFrame, csv_header, datedateHeaderValues

def period_Data(csv_DataFrame, csv_header, dateHeaderValues):
    acwp = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'ACWP']
    acwp.loc['Period Total Cost', dateHeaderValues] = acwp[dateHeaderValues].sum()
    acwp['Total Actual Cost'] = acwp.loc[:,dateHeaderValues].sum(axis=1)
    acwp_header = acwp.columns.values.tolist()
    for columnHeaders in acwp_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue
        
    bcwp = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWP']
    bcwp.loc['Period Total Earned', dateHeaderValues] = bcwp[dateHeaderValues].sum()    
    bcwp['Total Earned'] = bcwp.loc[:,dateHeaderValues].sum(axis=1)
    bcwp_header = bcwp.columns.values.tolist()
    for columnHeaders in bcwp_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue
        
    bcws = csv_DataFrame.loc[csv_DataFrame['Value Type'] == 'BCWS']
    bcws.loc['Period Total Planned', dateHeaderValues] = bcws[dateHeaderValues].sum()
    bcws['Total Planned'] = bcws.loc[:,dateHeaderValues].sum(axis=1)
    bcws_header = bcws.columns.values.tolist()
    for columnHeaders in bcws_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue
        
    period_DataFrame = pd.concat([acwp, bcwp, bcws], sort = True).sort_values(by='CAM').reindex(columns = csv_header).fillna(0)
    return period_DataFrame
            
def period_Cost(period_DataFrame, dateHeaderValues):
    period_BCWP = period_DataFrame.loc['Period Total Planned', dateHeaderValues]
    period_ACWP = period_DataFrame.loc['Period Total Cost', dateHeaderValues]
    
    period_CPI = period_BCWP / period_ACWP
    period_CV = period_BCWP - period_ACWP
    
    period_DataFrame.loc['Period CV'] = period_CV
    period_DataFrame.loc['Period CPI'] = period_CPI
    return period_CPI, period_CV

def period_Schedule(period_DataFrame, dateHeaderValues):
    period_BCWP = period_DataFrame.loc['Period Total Planned', dateHeaderValues]
    period_BCWS = period_DataFrame.loc['Period Total Earned', dateHeaderValues]
    
    period_SPI = period_BCWP / period_BCWS
    period_SV = period_BCWP - period_BCWS
    
    period_DataFrame.loc['Period SV'] = period_SV
    period_DataFrame.loc['Period SPI'] = period_SPI
    return period_SPI, period_SV

def filter_ChargeCode(period_DataFrame, cum_DataFrame, csv_DataFrame, csv_header):
    filter_ChargeCode_csv = pd.pivot_table(csv_DataFrame, values = csv_header, index=['Charge Code', 'CAM', 'Value Type'])
    filter_ChargeCode_period = pd.pivot_table(period_DataFrame, values = csv_header, index=['Charge Code', 'CAM', 'Value Type'])
    filter_ChargeCode_cum = pd.pivot_table(cum_DataFrame, values = csv_header, index=['Charge Code', 'CAM', 'Value Type'])
    return filter_ChargeCode_period, filter_ChargeCode_cum, filter_ChargeCode_csv

def filter_CAM(period_DataFrame, cum_DataFrame, csv_DataFrame, csv_header):
    filter_CAM_csv = pd.pivot_table(csv_DataFrame, values = csv_header, index=['CAM','Charge Code' 'Value Type'])
    filter_CAM_period = pd.pivot_table(period_DataFrame, values = csv_header, index=['CAM','Charge Code' 'Value Type'])
    filter_CAM_cum = pd.pivot_table(cum_DataFrame, values = csv_header, index=['CAM','Charge Code' 'Value Type'])
    return filter_CAM_csv, filter_CAM_period, filter_CAM_cum

def cumulative_Data(period_DataFrame):
    cum_DataFrame = period_DataFrame

    cum_DataFrame.loc['Cumulative Total Cost'] = cum_DataFrame.loc['Period Total Cost'].cumsum()
    cum_DataFrame.loc['Cumulative Planned Value'] = cum_DataFrame.loc['Period Total Planned'].cumsum()
    cum_DataFrame.loc['Cumulative Earned Value'] = cum_DataFrame.loc['Period Total Earned'].cumsum()
    return cum_DataFrame

def cum_Schedule(cum_DataFrame, dateHeaderValues):
    cum_BCWP = cum_DataFrame.loc['Cumulative Earned Value', dateHeaderValues]
    cum_BCWS = cum_DataFrame.loc['Cumulative Planned Value', dateHeaderValues]
    
    cum_SV = cum_BCWP - cum_BCWS
    cum_SPI = cum_BCWP / cum_BCWS
    
    cum_DataFrame.loc['SPI'] = cum_SPI
    cum_DataFrame.loc['SV'] = cum_SV
    return cum_SV, cum_SPI
    
def cum_Cost(cum_DataFrame, dateHeaderValues):
    cum_BCWP = cum_DataFrame.loc['Cumulative Earned Value', dateHeaderValues]
    cum_ACWP = cum_DataFrame.loc['Cumulative Total Cost', dateHeaderValues]
    
    cum_CV = cum_BCWP - cum_ACWP
    cum_CPI = cum_BCWP / cum_ACWP
    
    cum_DataFrame.loc['CPI'] = cum_CPI
    cum_DataFrame.loc['CV'] = cum_CV
    return cum_CV, cum_CPI

def project_reporting(cum_DataFrame):
    bac = cum_DataFrame['Total Cost'].sum()
    bcwp =cum_DataFrame.loc['Period Total Earned', 'Total Earned']
    acwp = cum_DataFrame.loc['Period Total Cost', 'Total Actual Cost']
    bcws = cum_DataFrame.loc['Period Total Planned', 'Total Planned']
        
    project_CPI = bcwp / acwp
    project_SPI = bcwp / bcws
    project_CV = bcwp - acwp
    project_SV = bcwp - bcws
    return bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, project_SV

def bugeted_cost_work_remaining(cum_DataFrame, bcwp, bac):
    percent_complete = bcwp / bac                  
    bcwr = bac - bcwp
    return percent_complete, bcwr

def estimate_at_complete(cum_DataFrame, bcwr, bac, bcwp, acwp, project_CPI):
    eac = acwp + bcwr
    tcpi = bac / eac                            
    performance_ETC = acwp + (bcwr * project_CPI)  
    performance_EAC = acwp + performance_ETC        
    performance_tpci = bac / performance_EAC
    varaince_at_complete = bac - eac
    return eac, tcpi, performance_ETC, performance_EAC, performance_tpci, varaince_at_complete

main()