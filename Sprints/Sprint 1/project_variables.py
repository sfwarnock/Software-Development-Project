# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 06:16:23 2018

@author: Scott Warnock
"""

# Variables

period_BCWS, period_BCWP, period_ACWP = 0, 0, 0 # Period (Current Month) Buguted Cost of Work Scheduled,
#   Bugeted Cost od Work Performed, Actual Cost of Work Performed

cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0          # Cummalative (Total-to-Date) Buguted Cost of Work Scheduled,
#   Bugeted Cost od Work Performed, Actual Cost of Work Performed

# Variances

period_CV = period_BCWP - period_ACWP  # Cost Variance (Period)

period_SV = period_BCWP - period_BCWS  # Schedule Variance (Period)

cum_CV = cum_BCWP - cum_ACWP    # Cummalative Cost Variance (Cummalative)

cum_SV = cum_BCWP - cum_BCWS    # Schedule Variance (Cummalative)

# Performace Indicies

period_CPI = period_BCWP / period_ACWP  # Cost Performance Index (Period)