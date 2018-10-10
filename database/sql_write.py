# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:14:12 2018

@author: Scott Warnock
"""

from sqlalchemy import create_engine

def sql_database(csv_DataFrame, period_DataFrame, cum_DataFrame):
    engine = create_engine('mssql+pymssql://something:something@hostname:port/dbname')
    
    csv_DataFrame.to_sql(csv_DataFrame, con = engine, if_exisits = 'replace', index_labels = 'id')
    
    period_DataFrame.to_sql(period_DataFrame, con = engine, if_exisits = 'replace', index_labels = 'id')
    
    cum_DataFrame.to_sql(cum_DataFrame, con = engine, if_exisits = 'replace', index_labels = 'id')