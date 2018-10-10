# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:14:12 2018

@author: Scott Warnock
"""

import pyodbc

def sql_database():
    sql_conn = pyodbc.connect('DRIVER = {}; SERVER=SQLSERVER2017; DATABASE= ; Trusted_Connection=yes')
    cursor = connStr.cursor()
    
    for index, row in cvs_DataFrame.iterrow():
        cursor.excute("INSERT INTO dbo.csv([Activity ID], [Activity Name], [Total Cost], [Charge Code], [CAM], [Value Type]) values ( )", 
                      row ['Activity ID'],
                      row ['Aciivity Name'],
                      row ['Total Cost'],
                      row ['Charge Code'],
                      row ['CAM'],
                      row ['Value Type'])
        
        connStr.commit()
    cursor.close()
    connStr.close()