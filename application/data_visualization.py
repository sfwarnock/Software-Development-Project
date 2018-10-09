# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:14:12 2018

@author: Scott Warnock
"""

def data_Visualazation(cum_DataFrame, period_DataFrame, dateHeaderValues):
    # Project S-curve Chart
    cum_BCWP = cum_DataFrame.loc['Cumulative Earned Value', dateHeaderValues]
    cum_ACWP = cum_DataFrame.loc['Cumulative Total Cost', dateHeaderValues]
    cum_BCWS = cum_DataFrame.loc['Cumulative Planned Value', dateHeaderValues]
    
    fig, ax = plt.subplots()
    ax.plot(cum_ACWP, color = "Green")
    ax.plot(cum_BCWP, color = "Red")
    ax.plot(cum_BCWS, color = "Blue")

    ax.set(xlabel='Month', ylabel= '$', title= 'Project S-Curve')
    ax.legend()
    plt.show()
    
    # Period Bar Chart
    period_BCWP = period_DataFrame.loc['Period Total Planned', dateHeaderValues]
    period_BCWS = period_DataFrame.loc['Period Total Earned', dateHeaderValues]
    period_ACWP = period_DataFrame.loc['Period Total Cost', dateHeaderValues]

    ind = np.arange(len(dateHeaderValues))
    width = 0.25

    fig2, ax = plt.subplots()

    bcwsBar = ax.bar(ind - width, period_BCWS, width, color = 'Red', label = 'Planned Value')
    bcwpBar = ax.bar(ind, period_BCWP, width, color = 'Blue', label = 'Earned Value')
    acwpBar = ax.bar(ind + width, period_ACWP, width, color = 'Green', label = 'Actual Cost')

    ax.set_ylabel('$')
    ax.set_xlabel('Month')
    ax.set_xticks(np.arange(len(dateHeaderValues)))
    ax.set_xticklabels(dateHeaderValues)
    ax.set_title('Monthly Planned, Earned, and Actual Cost')
    ax.legend()

    plt.show()