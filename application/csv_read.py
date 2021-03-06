# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:27:36 2018

@author: Scott Warnock
"""

import pandas as pd

def csv_Read():
    csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)
    csv_header = csv_DataFrame.columns.values.tolist()
    dateHeaderValues = csv_DataFrame.columns.values[6:].tolist()
    
    assert len(dateHeaderValues) != 0; "No values in 'dateHeaderValues' list."
    
    return csv_DataFrame, csv_header, dateHeaderValues