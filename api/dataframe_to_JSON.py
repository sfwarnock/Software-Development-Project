# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:16:11 2018

@author: Scott Warnock
"""

import json

def data_to_JSON(bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, 
                project_SV, percent_complete, bcwr, eac, tcpi, performance_ETC, 
                performance_EAC, performance_tcpi, varaiance_at_complete, cum_DataFrame):
    periodArray_toJSON = cum_DataFrame.loc[cum_DataFrame.index.isin(['Period Total Planned', 'Period Total Earned', 
                                                                     'Period Total Cost'])].to_json(orient = 'index')

    cumArray_toJSON = cum_DataFrame.loc[cum_DataFrame.index.isin(['Cumulative Planned Value', 'Cumulative Earned Value', 
                                                                  'Cumulative Total Cost'])].to_json(orient = 'index')
    
    cum_todateUI_table = {"Budget at Complete": bac, "BCWP": bcwp, "Percent Complete": percent_complete,
                      "Bugeted Cost of Work Remaining": bcwr}
    cum_todateUI_table["BCWS"] = bcws
    cum_todateUI_table["ACWP"] = acwp
    cum_todateUI_table["EAC"] = eac
    cum_todateUI_table["TCPI"] = tcpi
    cum_todateUI_table["CPI"] = project_CPI
    cum_todateUI_table["SPI"] = project_SPI
    cum_todateUI_table["CV"] = project_CV
    cum_todateUI_table["SV"] = project_SV
    cum_todateUI_table["Performance ETC"] = performance_ETC
    cum_todateUI_table["Performance EAC"] = performance_EAC
    cum_todateUI_table["Perfromance TCPI"] = performance_tcpi
    cum_todateUI_table["VAC"] = varaiance_at_complete
    cum_to_json = json.dumps(cum_todateUI_table, indent = 4)
    
    
    return periodArray_toJSON, cumArray_toJSON, cum_todateUI_table, cum_to_json