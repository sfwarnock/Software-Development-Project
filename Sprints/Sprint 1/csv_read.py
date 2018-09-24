# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:27:36 2018

@author: Scott Warnock
"""

import pandas as pd

csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)

def csv_Read():
    csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)
    print(csv_DataFrame)

csv_Read()