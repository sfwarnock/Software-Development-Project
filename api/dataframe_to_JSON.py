# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:16:11 2018

@author: Scott Warnock
"""

def dataframe_to_JSON(csv_DataFrame, period_DataFrame, cum_DataFrame):
    csv_DataFrame_JSON = csv_DataFrame.to_json(orient = 'index')
    period_DataFrame_json = period_DataFrame.to_json(orient = 'index')
    cum_DataFrame_json = cum_DataFrame.to_json(orient = 'index')
    
    return csv_DataFrame_JSON, period_DataFrame_json, cum_DataFrame_json