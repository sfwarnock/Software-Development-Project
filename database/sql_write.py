# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:14:12 2018

@author: Scott Warnock
"""

import urllib
from sqlalchemy import create_engine

def sql_database(csv_DataFrame, period_DataFrame, cum_DataFrame):

    params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER={(LOCAL)\SQLEXPRESS};DATABASE={DATABASE NAME};Trusted_Connection=yes')

    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    csv_DataFrame.to_sql('csv_DataFrame', engine, if_exists = 'replace')    
    period_DataFrame.to_sql('period_DataFrame', engine, if_exists = 'replace', index = False)    
    cum_DataFrame.to_sql('cum_DataFrame', engine, if_exists = 'replace', index = False)