# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:14:12 2018

@author: Scott Warnock
"""

import pyodbc

def sql_database(csv_DataFrame, period_DataFrame, cum_DataFrame):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER={(LOCAL\SQLEXPRESS};DATABASE={SELECTED DB};Trusted_Connection=yes')
    
    csv_DataFrame.to_sql(csv_DataFrame, conn, if_exisits = 'append', index_labels = 'id')
    
    #period_DataFrame.to_sql(period_DataFrame, con = engine, if_exisits = 'append', index_labels = 'id')
    
    #cum_DataFrame.to_sql(cum_DataFrame, con = engine, if_exisits = 'append', index_labels = 'id')