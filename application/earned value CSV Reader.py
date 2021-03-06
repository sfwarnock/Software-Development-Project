# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:52:53 2018
@author: Scott Warnock
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas.api.types as ptypes

def main():
    csv_DataFrame, csv_header, dateHeaderValues = csv_Read()
    period_DataFrame = period_Data(csv_DataFrame, csv_header, dateHeaderValues)
    period_Cost(period_DataFrame, dateHeaderValues)
    period_Schedule(period_DataFrame, dateHeaderValues)
    cum_DataFrame = cumulative_Data(period_DataFrame)
    cum_Cost(cum_DataFrame, dateHeaderValues)
    cum_Schedule(cum_DataFrame, dateHeaderValues)
    bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, project_SV = project_reporting(cum_DataFrame)
    percent_complete, bcwr = bugeted_cost_work_remaining(cum_DataFrame, bcwp, bac)
    eac, tcpi, performance_ETC, performance_EAC, performance_tcpi, varainace_at_complete = estimate_at_complete(cum_DataFrame, 
                                                                                                               bcwr, bac, bcwp, 
                                                                                                               acwp, project_CPI,
                                                                                                               project_CV)
    tables_data(bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, 
                project_SV, percent_complete, bcwr, eac, tcpi, performance_ETC, 
                performance_EAC, performance_tcpi, varainace_at_complete, cum_DataFrame)   
    data_Visualazation(cum_DataFrame, period_DataFrame, dateHeaderValues)
      
def csv_Read():
    csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)
    csv_header = csv_DataFrame.columns.values.tolist()
    dateHeaderValues = csv_DataFrame.columns.values[6:].tolist()
    
    assert len(dateHeaderValues) != 0; "No values in 'dateHeaderValues' list."
    
    return csv_DataFrame, csv_header, dateHeaderValues

def period_Data(csv_DataFrame, csv_header, dateHeaderValues):
    assert ptypes.is_string_dtype(csv_DataFrame['Value Type']), "Datatypes in 'Value Types' are not strings" 
    
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
    return period_CPI, period_CV, period_ACWP

def period_Schedule(period_DataFrame, dateHeaderValues):
    period_BCWP = period_DataFrame.loc['Period Total Planned', dateHeaderValues]
    period_BCWS = period_DataFrame.loc['Period Total Earned', dateHeaderValues]
    
    period_SPI = period_BCWP / period_BCWS
    period_SV = period_BCWP - period_BCWS
    
    period_DataFrame.loc['Period SV'] = period_SV
    period_DataFrame.loc['Period SPI'] = period_SPI
    return period_SPI, period_SV, period_BCWP, period_BCWS

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
        
    return cum_SV, cum_SPI, cum_BCWP, cum_BCWS
    
def cum_Cost(cum_DataFrame, dateHeaderValues):
    cum_BCWP = cum_DataFrame.loc['Cumulative Earned Value', dateHeaderValues]
    cum_ACWP = cum_DataFrame.loc['Cumulative Total Cost', dateHeaderValues]
    
    cum_CV = cum_BCWP - cum_ACWP
    cum_CPI = cum_BCWP / cum_ACWP
    
    cum_DataFrame.loc['CPI'] = cum_CPI
    cum_DataFrame.loc['CV'] = cum_CV
    return cum_CV, cum_CPI, cum_ACWP

def project_reporting(cum_DataFrame):
    bac = cum_DataFrame['Total Cost'].sum()
    bcwp =cum_DataFrame.loc['Period Total Earned', 'Total Earned']
    acwp = cum_DataFrame.loc['Period Total Cost', 'Total Actual Cost']
    bcws = cum_DataFrame.loc['Period Total Planned', 'Total Planned']
    
    assert bac > 0, 'BAC contains no values'
    assert bcws > 0, 'BCWS contains no values' 
        
    project_CPI = bcwp / acwp
    project_SPI = bcwp / bcws
    project_CV = bcwp - acwp
    project_SV = bcwp - bcws
        
    return bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, project_SV

def bugeted_cost_work_remaining(cum_DataFrame, bcwp, bac):
    percent_complete = bcwp / bac                  
    bcwr = bac - bcwp
    return percent_complete, bcwr

def estimate_at_complete(cum_DataFrame, bcwr, bac, bcwp, acwp, project_CPI, project_CV):
    eac = acwp + bcwr
    tcpi = bac / eac                            
    performance_ETC = acwp + (bcwr * project_CPI)  
    performance_EAC = acwp + performance_ETC        
    performance_tcpi = bac / performance_EAC
    varaiance_at_complete = bac - eac
    
    assert varaiance_at_complete == project_CV, 'VAC and CV are not equal'
    
    return eac, tcpi, performance_ETC, performance_EAC, performance_tcpi, varaiance_at_complete

def data_Visualazation(cum_DataFrame, period_DataFrame, dateHeaderValues):
    cum_BCWP = cum_DataFrame.loc['Cumulative Earned Value', dateHeaderValues]
    cum_ACWP = cum_DataFrame.loc['Cumulative Total Cost', dateHeaderValues]
    cum_BCWS = cum_DataFrame.loc['Cumulative Planned Value', dateHeaderValues]
    
    plt.style.use('dark_background')
    
    fig, ax = plt.subplots()
    ax.plot(cum_ACWP, color = "Green")
    ax.plot(cum_BCWP, color = "Red")
    ax.plot(cum_BCWS, color = "Blue")

    ax.set(xlabel='Month', ylabel= '$', title= 'Project S-Curve')
    ax.grid(False)
    ax.legend()
    plt.show()
    
    
    period_BCWP = period_DataFrame.loc['Period Total Planned', dateHeaderValues]
    period_BCWS = period_DataFrame.loc['Period Total Earned', dateHeaderValues]
    period_ACWP = period_DataFrame.loc['Period Total Cost', dateHeaderValues]

    ind = np.arange(len(dateHeaderValues))
    width = 0.25

    fig2, ax = plt.subplots()

    bcwsBar = ax.bar(ind - width, period_BCWS, width, color = 'Red', label = 'Planned Value')
    bcwpBar = ax.bar(ind, period_BCWP, width, color = 'Blue', label = 'Earned Value')
    acwpBar = ax.bar(ind + width, period_ACWP, width, color = 'Green', label = 'Actual Cost')

    ax.set_ylabel('$')
    ax.set_xlabel('Month')
    ax.set_xticks(np.arange(len(dateHeaderValues)))
    ax.set_xticklabels(dateHeaderValues)
    ax.set_title('Monthly Planned, Earned, and Actual Cost')
    ax.grid(False)
    ax.legend()

    plt.show()
    
def tables_data(bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, 
                project_SV, percent_complete, bcwr, eac, tcpi, performance_ETC, 
                performance_EAC, performance_tcpi, varaiance_at_complete, cum_DataFrame): 
    print()
    print ("Planned Value:", '${:.{prec}f}'.format(bcws, prec = 2), "Earned Value:", '${:.{prec}f}'.format(bcwp, prec = 2), 
           "Percent Complete: %", '{:.{prec}f}'.format(percent_complete * 100, prec = 1), 
           "Total Cost:",'${:.{prec}f}'.format(acwp, prec = 2), "EAC:",'${:.{prec}f}'.format(eac, prec = 2), 
           "VAC:",'${:.{prec}f}'.format(varaiance_at_complete, prec = 2))
    print ()
    print ("Project CPI:", project_CPI.round(2), "Project SPI", project_SPI.round(2), 
           "Project Cost Variance:",'${:.{prec}f}'.format(project_CV, prec = 2), 
           "Project Schedule Variance:", '${:.{prec}f}'.format(project_SV, prec = 2))
    print()
    print("TCPI:", tcpi.round(2), "Performace EAC:", '${:.{prec}f}'.format(performance_EAC, prec =2),
          "Performance ETC:", '${:.{prec}f}'.format(performance_ETC, prec = 2), "Performance TCPI", 
          '${:.{prec}f}'.format(performance_tcpi, prec = 2))
    print()
    print (cum_DataFrame)
main()