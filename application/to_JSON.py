# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 06:48:20 2018

@author: Scott Warnock
"""

import json

def data_to_JSON(bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, 
                project_SV, percent_complete, bcwr, eac, tcpi, performance_ETC, 
                performance_EAC, performance_tcpi, variance_at_complete, cum_DataFrame,
                period_BCWS, period_BCWP, period_ACWP, period_SPI, period_SV, period_CPI,
                period_CV):
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
    cum_todateUI_table["VAC"] = variance_at_complete
    cum_todateUI_table["Period BCWS"] = period_BCWS
    #cum_todateUI_table["Period Percent Complete"] =
    cum_todateUI_table["Period BCWP"] = period_BCWP
    cum_todateUI_table["Period ACWP"] = period_ACWP
    cum_todateUI_table["Period SPI"] = period_SPI
    cum_todateUI_table["Period SV"] = period_SV
    cum_todateUI_table["Period CPI"] = period_CPI
    cum_todateUI_table["Period CV"] = period_CV
    with open('cum_json.txt', 'w') as outfile:
        json.dump(cum_todateUI_table, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
    
    return periodArray_toJSON, cumArray_toJSON, cum_todateUI_table, #cum_to_json