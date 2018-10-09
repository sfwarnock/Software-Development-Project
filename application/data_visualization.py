# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:14:12 2018

@author: Scott Warnock
"""

def data_Visualazation(cum_ACWP, cum_BCWP, cum_BCWS, period_ACWP, period_BCWS, period_BCWP, headerValues):
    fig, ax = plt.subplots()
    ax.plot(cum_ACWP, color = "Green")
    ax.plot(cum_BCWP, color = "Red")
    ax.plot(cum_BCWS, color = "Blue")

    ax.set(xlabel='Month', ylabel= '$', title= 'Project S-Curve')
    plt.show()

    ind = np.arange(len(period_BCWP))
    width = 0.25

    fig, ax = plt.subplots()

    bcwsBar = ax.bar(ind - width, period_BCWS, width, color = 'Red', label = 'Planned Value')
    bcwpBar = ax.bar(ind, period_BCWP, width, color = 'Blue', label = 'Earned Value')
    acwpBar = ax.bar(ind + width, period_ACWP, width, color = 'Green', label = 'Actual Cost')

    ax.set_ylabel('$')
    ax.set_xticklabels(headerValues)
    ax.set_title('Monthly Planned, Earned, and Actual Cost')
    ax.legend()

    plt.show()