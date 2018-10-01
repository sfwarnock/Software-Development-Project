# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 06:21:39 2018

@author: Scott Warnock
"""

def filter_ChargeCode():
    filter_ChargeCode = pd.pivot_table(period_DataFrame, values = csv_header, index=['Charge Code', 'CAM', 'Value Type'])
    return filter_ChargeCode