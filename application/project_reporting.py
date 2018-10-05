# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 06:13:06 2018

@author: 175272
"""

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