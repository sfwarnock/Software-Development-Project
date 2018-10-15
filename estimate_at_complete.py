# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 06:36:10 2018

@author: Scott Warnoc
"""

def estimate_at_complete(cum_DataFrame, bcwr, bac, bcwp, acwp, project_CPI, project_CV):
    eac = acwp + bcwr
    tcpi = bac / eac                            
    performance_ETC = acwp + (bcwr * project_CPI)  
    performance_EAC = acwp + performance_ETC        
    performance_tpci = bac / performance_EAC
    varaiance_at_complete = bac - eac
    
    assert varaiance_at_complete == project_CV, 'VAC and CV are not equal'
    
    return eac, tcpi, performance_ETC, performance_EAC, performance_tpci, varaiance_at_complete