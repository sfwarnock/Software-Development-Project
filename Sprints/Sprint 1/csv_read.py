# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:27:36 2018

@author: Scott Warnock
"""

import pandas as pd

def csv_Read():
    data_file = pd.read_csv('datafile.csv').fillna(0)
    print (data_file)
    
csv_Read()