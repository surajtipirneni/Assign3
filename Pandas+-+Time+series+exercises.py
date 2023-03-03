
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

get_ipython().magic('matplotlib inline')


# In[ ]:

# Excercise 1

# parse christmas_str2 with format string "%Y:%m:%d"
christmas = pd.to_datetime("2017:12:25", format="%Y:%m:%d")

# parse dbacks_win with format string "M:%m D:%d Y:%Y %I:%M %p"
dbacks = pd.to_datetime("M:11 D:4 Y:2001 9:15 PM", format="M:%m D:%d Y:%Y %I:%M %p")

# parse america_bday with format string "America was born on %B %d, %Y"
america = pd.to_datetime("America was born on July 4, 1776", format="America was born on %B %d, %Y")


# In[3]:

# Excercise 2

# define name and birth date
name = "John"
birth_date = pd.to_datetime("10 Jun 1989")

# format message using name, birth date, and day of week
message = f"{name}'s birthday is {birth_date.strftime('%B %d, %Y')} (a {birth_date.strftime('%A')})"
print(message)


# In[4]:

# Excercise 3

import quandl

# set start date for data
start_date = "2015-01-01"

# get btc_usd data
btc_usd = quandl.get("BCHARTS/BITSTAMPUSD", start_date=start_date)

# July 2017 through August 2017 (inclusive)
btc_july_aug_2017 = btc_usd.loc['2017-07':'2017-08']

# April 25, 2015 to June 10, 2016
btc_apr_2015_jun_2016 = btc_usd.loc['2015-04-25':'2016-06-10']

# October 31, 2017
btc_oct_31_2017 = btc_usd.loc['2017-10-31']


# In[ ]:

# Excercise 4

# set start date for data
start_date = "2015-01-01"

# get btc_usd data
btc_usd = quandl.get("BCHARTS/BITSTAMPUSD", start_date=start_date)

# calculate percent change in volume of trades
btc_usd["Volume_Pct_Change"] = btc_usd["Volume (BTC)"].pct_change()

# calculate the week with the largest percent change in volume of trades
largest_pct_change_week = btc_usd["Volume_Pct_Change"].shift(1).idxmax()

# print result
print("Week with the largest percent change in volume of trades: ", largest_pct_change_week)


# In[ ]:

# Bi weekly frequency

# calculate percent change in volume of trades
btc_usd["Volume_Pct_Change"] = btc_usd["Volume (BTC)"].pct_change()

# resample data at bi-weekly frequency and calculate percent change
btc_usd_biweekly = btc_usd.resample("2W").first()
btc_usd_biweekly["Volume_Pct_Change"] = btc_usd_biweekly["Volume (BTC)"].pct_change()

# calculate the bi-week with the largest percent change in volume of trades
largest_pct_change_biweek = btc_usd_biweekly["Volume_Pct_Change"].shift(1).idxmax()

# print result
print("Bi-week with the largest percent change in volume of trades: ", largest_pct_change_biweek)


# In[ ]:

# monthly frequency

# calculate percent change in volume of trades
btc_usd["Volume_Pct_Change"] = btc_usd["Volume (BTC)"].pct_change()

# resample data at monthly frequency and calculate percent change
btc_usd_monthly = btc_usd.resample("M").first()
btc_usd_monthly["Volume_Pct_Change"] = btc_usd_monthly["Volume (BTC)"].pct_change()

# calculate the month with the largest percent change in volume of trades
largest_pct_change_month = btc_usd_monthly["Volume_Pct_Change"].shift(1).idxmax()

# print result
print("Month with the largest percent change in volume of trades: ", largest_pct_change_month)


# In[ ]:

# Excercise 5

'''Inorder to calculate the ideal date that fulfills the criteria, I would calculate the rolling 30 day returns for all the dates.
Assuming that the first 29 dates need not be considered for the analysis.'''


# In[ ]:

# Excercise 6


# In[ ]:

def rolling_returns(dataframe):
    # Calculate the daily returns
    daily_returns = dataframe["Close"].pct_change()

    # Calculate the rolling 30-day returns
    rolling_returns = daily_returns.rolling("30d").sum()

    return rolling_returns


# In[ ]:

rolling_btc = rolling_returns(btc_usd)
max_date = rolling_btc["Open"].idxmax()
max_open = rolling_btc.loc[max_date, "Open"]


# In[ ]:

# Excercise 7
'''We can determine the date of purchase and sale by first sampling the data with monthly frequency using resample("MS")
Then we can calcualte the reurns in the windows and then extrat the dates which match the criteria'''


# In[ ]:

# Excercise 8


# In[ ]:

btc_monthly = btc_usd.loc[:, "Close"].resample("MS")
monthly_returns = (btc_monthly.last() - btc_monthly.first()) / btc_monthly.first()


# In[ ]:

btc_monthly_returns = btc_monthly["Open"].pct_change()
max_date = btc_monthly_returns.idxmax()
print("Date associated with the maximum value:", max_date)

