# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 06:21:39 2018

@author: Scott Warnock
"""

def filter_ChargeCode(period_DataFrame, cum_DataFrame, csv_DataFrame, csv_header):
    filter_ChargeCode_csv = pd.pivot_table(csv_DataFrame, values = csv_header, index=['Charge Code', 'CAM', 'Value Type'])
    filter_ChargeCode_period = pd.pivot_table(period_DataFrame, values = csv_header, index=['Charge Code', 'CAM', 'Value Type'])
    filter_ChargeCode_cum = pd.pivot_table(cum_DataFrame, values = csv_header, index=['Charge Code', 'CAM', 'Value Type'])
    return filter_ChargeCode_period, filter_ChargeCode_cum, filter_ChargeCode_csv