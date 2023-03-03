
# coding: utf-8

# In[2]:

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.transforms as transforms


quandl.ApiConfig.api_key = os.environ.get("QUANDL_AUTH", "Dn6BtVoBhzuKTuyo6hbp")
get_ipython().magic('matplotlib inline')


# In[ ]:

import quandl
aapl = quandl.get("WIKI/AAPL", start_date="2006-12-25")
aapl.head()


# In[ ]:

# Excercise 1


# In[ ]:

import quandl

aapl = quandl.get("WIKI/AAPL", start_date="2006-12-25")
aapl['Open'].plot()

'''The object returned from the .plot() method is a matplotlib AxesSubplot object.

This object has various methods that can be used to customize the plot, such as set_title(), set_xlabel(), set_ylabel() etc. 
These methods can be used to add additional data to the plot or to customize the visual appearance of the plot.'''


# In[ ]:

# Excercise 2


# In[ ]:

fig, axes = plt.subplots(nrows=2, ncols=1)

aapl['Adj. Close'].plot(ax=axes[0])
aapl['Adj. Volume'].plot(kind='area', ax=axes[1])

axes[0].set_title('Adjusted Close Price')
axes[1].set_title('Adjusted Volume')

plt.tight_layout()
plt.show()


# In[ ]:

# Excercise 3


# In[ ]:

aapl.plot(x='Date', y=['Adj. Open', 'Adj. Close'], sharex=True, grid=True, style=['b-', 'r--'], color=['blue', 'red'], kind='line')

plt.title('Apple Stock Prices from 2006 to Present')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend(['Adjusted Open', 'Adjusted Close'])
plt.show()


# In[ ]:

# Excercise 4


# '''sharex=True: Specifies that both subplots should share the same x-axis. 
# This argument is optional and useful when you want to plot multiple subplots with the same x-axis range for easy comparison.
# 
# grid=True: Specifies that gridlines should be added to the plot. 
# This argument is optional and useful for better readability of the plot.
# 
# style=['b-', 'r--']: Specifies the line styles for each variable being plotted. 
# 
# color=['blue', 'red']: Specifies the colors for each variable being plotted. 
# In this case, 'blue' specifies the color for the 'Adj. Open' variable, and 'red' specifies the color for the 'Adj. Close' variable. 
# 
# kind='line': Specifies that the plot type should be a line chart. 
# This argument is required to specify the type of plot to be created'''

# In[ ]:

# Excercise 5


# Change background color: fig.set_facecolor()
# Add Axes titles: set_title() and set_xlabel()/set_ylabel()
# Remove the x axis titles: set_xlabel() and set_ylabel()
# Remove tick marks on y axis: tick_params()
# Add a “faint” version of the line from the first subplot: plot() with alpha parameter
# Remove x axis tick labels: set_xticklabels()
# Make x axis ticks longer and semi-transparent: tick_params()
# Make sure all Axes have same y limits: ylim()
# Remove the spines (the border on each Axes): spines()
# Add a white circle to (0, 100) on each Axes: scatter()

# In[ ]:




# In[ ]:



