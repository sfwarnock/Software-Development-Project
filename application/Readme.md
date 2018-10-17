


# **Python Earned Value Reader**
#### Version 1.0.0_2018.OCT.16


## About
The standalone Python application, 'earned value CSV Reader.py', is a program which reads earned value management data from a 
CSV file. Version 1.0.0_2018.OCT.16 is intended to be a demonstrable MVP and the Applcaiton Tier of a 3-tier Architecture design.
The program reads an input CSV file containing period earned value management data from a schedule software program. The data is
processed to generate earned value metrics for period and cumulative reporting. The program calculates the following earned value
data from the CSV input file:
```python
# Variables
period_BCWS, period_BCWP, period_ACWP = 0, 0, 0 # Period (Current Month) Buguted Cost of Work Scheduled,
                                                # Bugeted Cost od Work Performed, Actual Cost of Work Performed

cum_BCWS, cum_BCWP, cum_ACWP = 0, 0, 0          # Cumalative (Total-to-Date) Buguted Cost of Work Scheduled,
                                                # Bugeted Cost od Work Performed, Actual Cost of Work Performed

bac, pmb = 0, 0                                 # Budget at Complete, Performance Management Baseline

# Variances
period_CV = period_BCWP - period_ACWP           # Cost Variance (Period)
period_SV = period_BCWP - period_BCWS           # Schedule Variance (Period)
cum_CV = cum_BCWP - cum_ACWP                    # Cumalative Cost Variance (Cumalative)
cum_SV = cum_BCWP - cum_BCWS                    # Schedule Variance (Cumalative)


# Performace Indicies
period_CPI = period_BCWP / period_ACWP          # Cost Performance Index (Period)
cum_CPI = cum_BCWP / cum_ACWP                   # Cost Performance Index (Cumalative)
period_SPI = period_BCWP / period_BCWS          # Schedule Performance Index (Period)
cum_SPI = cum_BCWP / cum_BCWS                   # Scheudle Performance Index (Cumalative)


# Status
percent_complete = cum_BCWS / bac               # Overall project % complete            
bcwr = bac - cum_BCWP                           # Bugeted Cost of Work Remaning

# Estimate at Complete
eac = cum_ACWP + bcwr                           # Estimate at complete
tcpi = bac / eac                                # To Complete Perforamce Index
performance_ETC = cum_ACWP + (bcwr * cum_CPI)   # Ajusted EAC
performance_EAC = cum_ACWP + performance_ETC    # Performance EAC
performance_tcpi = bac / performance_EAC        # Performance EAC
```

The data from the CSV generates two indvidual pandas dataframes, one for period data and one for cumalative data. The program
completes with generating a bar graph for the period data by month and an S-curve line graph for the project cumalative data.

## Use
Users can copy the program code and use in a Python IDE. The IDE used to develop the code was [Spyder IDE](https://www.spyder-ide.org/) 
which comes installed through the [Anaconda Navigator Shell](https://www.anaconda.com/download/). It is recomended that users use the
Spyder IDE to run the program as all the libraies used to run the program come pre-loaded (see Dependencies below for a list of
libraries).

Once downloaded the user can modifiy the program to read the their own csv file. The location of the read_csv() is the def csv_Read()
function:
```python
def csv_Read():
    csv_DataFrame = pd.read_csv('datafile.csv').fillna(0)
    csv_header = csv_DataFrame.columns.values.tolist()
    dateHeaderValues = csv_DataFrame.columns.values[6:].tolist()
 
```
As stated in the 'About' section above, the Version 1.0.0_2018.OCT.16 is a MVP demonstration program. Therefore the program is written
to read from a CSV with a set number of headervalues. It is recomended users download the datafile.csv and run the project with the
datefile to undestand how the program is processing the columns of the csv.

## Dependencies

* Python 3.7
* pandas 0.23.4
* numpy 1.15.1
* matplotlib 2.2.3

## Getting Help
The backbone of the program is dependent on the pandas library. You can visit the [pandas github](https://github.com/pandas-dev/pandas/blob/master/README.md) 
and the [pandas documentation site](http://pandas.pydata.org/pandas-docs/stable/) for further information. Another useful resource
for code trouble shooting is [StackOverflow](https://stackoverflow.com/).
