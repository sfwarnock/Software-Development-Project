n# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 06:48:38 2018

@author: Scott Warnock
"""

def ev_MetricTypes(csv_DataFrame):
    headerValues = data_file.columns.values[6:].tolist()

    acwp = data_file.loc[data_file['Value Type'] == 'ACWP']
    acwp.loc['Period Total Cost', headerValues] = acwp[headerValues].sum()
    acwp['Total Actual Cost'] = acwp.loc[:,headerValues].sum(axis=1)
    acwp_header = acwp.columns.values.tolist()
    for columnHeaders in acwp_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue

    bcwp = data_file.loc[data_file['Value Type'] == 'BCWP']
    bcwp.loc['Period Total Earned', headerValues] = bcwp[headerValues].sum()    
    bcwp['Total Earned'] = bcwp.loc[:,headerValues].sum(axis=1)
    bcwp_header = bcwp.columns.values.tolist()
    for columnHeaders in bcwp_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue

    bcws = data_file.loc[data_file['Value Type'] == 'BCWS']
    bcws.loc['Period Total Planned', headerValues] = bcws[headerValues].sum()
    bcws['Total Planned'] = bcws.loc[:,headerValues].sum(axis=1)
    bcws_header = bcws.columns.values.tolist()
    for columnHeaders in bcws_header:
        if columnHeaders not in csv_header:
            csv_header.append(columnHeaders)
        if columnHeaders in csv_header:
            continue

    period_DataFrame = pd.concat([acwp, bcwp, bcws]).sort_values(by='CAM').reindex(columns = csv_header)