# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 06:36:10 2018

@author: Scott Warnoc
"""

def estimate_at_complete(cum_DataFrame, bcwr, bac, bcwp):
    acwp = cum_DataFrame.loc['Period Total Cost', 'Total Actual Cost']
    bcws = cum_DataFrame.loc['Period Total Planned', 'Total Planned']

    eac = acwp + bcwr
    tcpi = bac / eac                            

    project_CPI = bcwp / acwp
    project_SPI = bcwp / bcws
    project_CV = bcwp - acwp
    project_SV = bcwp - bcws

    performance_ETC = acwp + (bcwr * project_CPI)  

    performance_EAC = acwp + performance_ETC        

    performance_tpci = bac / performance_EAC

    varaince_at_complete = bac - eac
    return eac, tcpi, project_CPI, project_SPI, project_CV, project_SV, performance_ETC, performance_EAC, performance_tpci, varaince_at_complete