# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:14:12 2018

@author: Scott Warnock
"""

def data_Visualazation(cum_ACWP, cum_BCWP, cum_BCWS, period_ACWP, period_BCWS, period_BCWP, headerValues):
    fig, ax = plt.subplots()
    ax.plot(cum_ACWP, color = "Blue")
    ax.plot(cum_BCWP, color = "Red")
    ax.plot(cum_BCWS, color = "Green")

    ax.set(xlabel='Month', ylabel= '$', title= 'Project S-Curve')
    plt.show()


    bar_acwp = period_ACWP
    bar_bcwp = period_BCWP
    bar_bcws = period_BCWS

    ind = np.arange(len(bar_bcwp))
    width = 0.35

    fig, ax = plt.subplots()

    bcwsBar = ax.bar(ind - width/2, bar_bcws, width, color = 'Red', label = 'Planned Value')
    bcwpBar = ax.bar(ind + width/2, bar_bcwp, width, color = 'Green', label = 'Earned Value')
    acwpBar = ax.bar(ind + width/2, bar_acwp, width, color = 'Blue', label = 'Actual Cost')

    ax.set_ylabel('$')
    ax.set_xticklabels(headerValues)
    ax.set_title('Monthly Planned, Earned, and Actual Cost')
    ax.legend()
    
    plt.show()