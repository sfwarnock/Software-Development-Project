# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:16:11 2018

@author: Scott Warnock
"""

def dataframe_to_JSON(cum_DataFrame):
    periodArray_toJSON = cum_DataFrame.loc[cum_DataFrame.index.isin(['Period Total Planned', 'Period Total Earned', 
                                                                     'Period Total Cost'])].to_json(orient = 'index')

    cumArray_toJSON = cum_DataFrame.loc[cum_DataFrame.index.isin(['Cumulative Planned Value', 'Cumulative Earned Value', 
                                                                  'Cumulative Total Cost'])].to_json(orient = 'index')
    
    return periodArray_toJSON, cumArray_toJSON