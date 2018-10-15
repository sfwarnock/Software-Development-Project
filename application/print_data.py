# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 07:11:03 2018

@author: Scott Warnock
"""

def tables_data(bac, bcwp, bcws, acwp, project_CPI, project_SPI, project_CV, 
                project_SV, percent_complete, bcwr, eac, tcpi, performance_ETC, 
                performance_EAC, performance_tcpi, varaince_at_complete, cum_DataFrame): 
    print()
    print ("Planned Value:", '${:.{prec}f}'.format(bcws, prec = 2), "Earned Value:", '${:.{prec}f}'.format(bcwp, prec = 2), 
           "Percent Complete: %", '{:.{prec}f}'.format(percent_complete * 100, prec = 1), 
           "Total Cost:",'${:.{prec}f}'.format(acwp, prec = 2), "EAC:",'${:.{prec}f}'.format(eac, prec = 2), 
           "VAC:",'${:.{prec}f}'.format(varaince_at_complete, prec = 2))
    print ()
    print ("Project CPI:", project_CPI.round(2), "Project SPI", project_SPI.round(2), 
           "Project Cost Variance:",'${:.{prec}f}'.format(project_CV, prec = 2), 
           "Project Schedule Variance:", '${:.{prec}f}'.format(project_SV, prec = 2))
    print()
    print("TCPI:", tcpi.round(2), "Performace EAC:", '${:.{prec}f}'.format(performance_EAC, prec =2),
          "Performance ETC:", '${:.{prec}f}'.format(performance_ETC, prec = 2), "Performance TCPI", 
          '${:.{prec}f}'.format(performance_tcpi, prec = 2))
    print()
    print (cum_DataFrame)