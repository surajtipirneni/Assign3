
# coding: utf-8

# In[24]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')


# In[2]:

#Exercise 1


# In[3]:

C = np.arange(1, 7, dtype=float)
C[[3, 5]] = np.nan
df = pd.DataFrame({
    "A" : [1, 1, 1, 2, 2, 2],
    "B" : [1, 1, 2, 2, 1, 1],
    "C": C,
})

gbA = df.groupby("A")


# In[4]:

gbA.sum()

#How did pandas compute the sum
'''Calling gbA.sum() will return a new DataFrame where the values in column "C" have been summed for each group in column "A". 
The other columns ("B") are not included in the result because they are not numeric.'''

#What happened to the NaN entries in column C?
'''When the sum() method is called on a Pandas DataFrame, the NaN values are automatically excluded by default. 
Therefore, when we call gbA.sum(), the NaN values in column C for group 1 and group 2 are excluded 
    from the calculation of the sum for each group.'''


# In[8]:

#Exercise 2


# In[9]:

# Mean of column C for each group
gbA.mean()


# In[10]:

# Minimum value of column C for each group
gbA.min()


# In[11]:

# Maximum value of column C for each group
gbA.max()


# In[ ]:

'''The output of each of these commands will have a similar format to the output of gbA.sum(), 
    with one row for each group in column "A" and one column for the aggregated value of column "C" for each group. 
However, the values themselves will be different.'''


# In[ ]:

#Exercise 3


# In[12]:

#1 Write a function that, given a DataFrame, computes each entry’s deviation from the mean of its column.

def deviation_from_mean(df):
    # Calculate the mean of each column
    means = df.mean(axis=0)
    # Calculate the deviation of each entry from the mean of its column
    deviations = df - means

    return deviations


# In[14]:

# 2. Apply the function to gbA.
gbA.apply(deviation_from_mean)


# In[ ]:

# 3. With your neighbor describe what the index and and columns are? Where are the group keys (the A column)?

'''In the output of gbA.apply(deviation_from_mean), the index refers to the row labels of the new DataFrame, 
and the columns refer to the column labels of the new DataFrame. 
The row labels are simply integers, starting from 0 and ending at 5, and the column labels are the same as the 
column labels of the original DataFrame df, which are "B" and "C".

The group keys, which are the values in the "A" column of the original DataFrame, are not explicitly shown in the 
output of gbA.apply(deviation_from_mean). However, they are used internally by the groupby() method to group the 
DataFrame by the values in the "A" column. Each group is then operated on separately by the deviation_from_mean() function,
and the resulting output is a new DataFrame that shows the deviations from the mean of each column within each group.'''


# In[15]:

# 4. Determine the correct way to add these results back into df as new columns.
deviations = gbA.apply(deviation_from_mean)
df = df.join(deviations, rsuffix='_deviation')
df


# In[16]:

#Exercise 4

#Which type of delay was the most common?

'''Lateaircraftdelay was the most common'''

#Which one caused the largest average delay?

'''Lateaircraftdelay caused the largest average delay'''

#Does that vary by airline?


# In[17]:

# Excercise 5
url = "https://datascience.quantecon.org/assets/data/airline_performance_dec16.csv.zip"
air_dec = pd.read_csv(url, parse_dates = ['Date'])


# In[18]:

weekly_delays = (
    air_dec
    .groupby([pd.Grouper(key="Date", freq="W"), "Carrier"])
    ["ArrDelay"]               # extract one column
    .mean()                    # take average
    .unstack(level="Carrier")  # Flip carrier up as column names
)
weekly_delays


# In[25]:

# plot
axs = weekly_delays.plot.bar(
    figsize=(10, 8), subplots=True, legend=False, sharex=True,
    sharey=True, layout=(4, 3), grid=False
)

# tweak spacing between subplots and xaxis labels
axs[0,0].get_figure().tight_layout()
for ax in axs[-1, :]:
    ax.set_xticklabels(weekly_delays.index.strftime("%a, %b. %d'"))


# In[20]:

delay_cols = [
    'CarrierDelay',
    'WeatherDelay',
    'NASDelay',
    'SecurityDelay',
    'LateAircraftDelay'
]


# In[21]:

pre_christmas = air_dec.loc[
    (air_dec["Date"] >= "2016-12-12") & (air_dec["Date"] <= "2016-12-18")
]

# custom agg function
def positive(df):
    return (df > 0).sum()

delay_totals = pre_christmas.groupby("Carrier")[delay_cols].agg(["sum", "mean", positive])
delay_totals


# In[22]:

reshaped_delays = (
    delay_totals
    .stack()             # move aggregation method into index (with Carrier)
    .T                   # put delay type in index and Carrier+agg in column
    .swaplevel(axis=1)   # make agg method outer level of column label
    .sort_index(axis=1)  # sort column labels so it prints nicely
)
reshaped_delays


# In[23]:

for agg in ["mean", "sum", "positive"]:
    axs = reshaped_delays[agg].plot(
        kind="bar", subplots=True, layout=(4, 3), figsize=(10, 8), legend=False,
        sharex=True, sharey=True
    )
    fig = axs[0, 0].get_figure()
    fig.suptitle(agg)
#     fig.tight_layout();


# In[26]:

# Evaluating functions
def mean_delay_plot(df, freq, figsize=(10, 8)):
    """
    Make a bar chart of average flight delays for each carrier at
    a given frequency.
    """
    mean_delays = (
        df
        .groupby([pd.Grouper(key="Date", freq=freq), "Carrier"])
        ["ArrDelay"]               # extract one column
        .mean()                    # take average
        .unstack(level="Carrier")  # Flip carrier up as column names
    )

    # plot
    axs = mean_delays.plot.bar(
        figsize=figsize, subplots=True, legend=False, sharex=True,
        sharey=True, layout=(4, 3), grid=False
    )

    # tweak spacing between subplots and x-axis labels
    axs[0, 0].get_figure().tight_layout()
    for ax in axs[-1, :]:
        ax.set_xticklabels(mean_delays.index.strftime("%a, %b. %d'"))

    # return the axes in case we want to further tweak the plot outside the function
    return axs


def delay_type_plot(df, start, end):
    """
    Make bar charts for total minutes, average minutes, and number of
    occurrences for each delay type, for all flights that were scheduled
    between `start` date and `end` date
    """
    sub_df = df.loc[
        (df["Date"] >= start) & (df["Date"] <= end)
    ]

    def positive(df):
        return (df > 0).sum()

    aggs = sub_df.groupby("Carrier")[delay_cols].agg(["sum", "mean", positive])

    reshaped = aggs.stack().T.swaplevel(axis=1).sort_index(axis=1)

    for agg in ["mean", "sum", "positive"]:
        axs = reshaped[agg].plot(
            kind="bar", subplots=True, layout=(4, 3), figsize=(10, 8), legend=False,
            sharex=True, sharey=True
        )
        fig = axs[0, 0].get_figure()
        fig.suptitle(agg)
#         fig.tight_layout();


# In[27]:

mean_delay_plot(air_dec, "D", figsize=(16, 8));


# In[28]:

# both days
delay_type_plot(air_dec, "12-17-16", "12-18-16")


# In[ ]:



