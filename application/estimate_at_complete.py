# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 06:36:10 2018

@author: Scott Warnoc
"""

def estimate_at_complete(cum_DataFrame, bcwr, bac, bcwp, acwp, project_CPI):
    eac = acwp + bcwr
    tcpi = bac / eac                            
    performance_ETC = acwp + (bcwr * project_CPI)  
    performance_EAC = acwp + performance_ETC        
    performance_tpci = bac / performance_EAC
    varaince_at_complete = bac - eac
    return eac, tcpi, performance_ETC, performance_EAC, performance_tpci, varaince_at_complete