
# coding: utf-8

# In[2]:

import pandas as pd
get_ipython().magic('matplotlib inline')


# In[2]:

#Excercise 1


# In[3]:

## Load up the data -- this will take a couple seconds
url = "https://datascience.quantecon.org/assets/data/state_unemployment.csv"
unemp_raw = pd.read_csv(url, parse_dates=["Date"])


# In[5]:

# Don't worry about the details here quite yet
unemp_all = (
    unemp_raw
    .reset_index()
    .pivot_table(index="Date", columns="state", values="UnemploymentRate")
)
unemp_all.head()


# In[6]:

states = [
    "Arizona", "California", "Florida", "Illinois",
    "Michigan", "New York", "Texas"
]
unemp = unemp_all[states]
unemp.head()


# In[ ]:

# In the above data frame, state names are columns and dates are indices


# In[7]:

unemp.columns


# In[8]:

unemp.index


# In[ ]:

# Excercise 2


# In[13]:

# At each date, what is the minimum unemployment rate across all states in our sample?
unemp.agg([min],axis=1)


# In[18]:

#What was the median unemployment rate in each state?
unemp.agg(['median'])


# In[35]:

#What was the maximum unemployment rate across the states in our sample? 
#What state did it happen in? In what month/year was this achieved


# In[38]:

max_value = unemp.values.max()
max_index = unemp.values.argmax()
max_col = unemp.columns[max_index % len(unemp.columns)]
max_row = unemp.index[max_index // len(unemp.columns)]

# Print the results
print(f"The maximum value is {max_value}, located at index ({max_row}, {max_col})")


# In[ ]:

# the aggregation returned a series.
#The maximum value is 14.6, located at index (2009-06-01 00:00:00, Michigan)


# In[82]:

#Classify each state as high or low volatility based on whether the variance of their unemployment is above or below 4.

var_data = unemp.agg(['var']).T


# In[83]:

for i in var_data.index:
    if var_data.loc[i].values[0] > 4:
        var_data.loc[i,'classification'] = 'high'
    elif var_data.loc[i].values[0] <= 4:
        var_data.loc[i,'classification'] = 'low'
        


# In[84]:

print(var_data)


# In[ ]:

# Excercise 3


# In[78]:

# 1. Write a Python function that takes a single number as an input 
# and outputs a single string noting if that number is high, medium, or low.


# In[90]:

def categorize_number(num):
    if num > 4:
        return "high"
    elif num > 2 and num <=4:
        return "medium"
    else:
        return "low"


# In[91]:

#Pass your function to applymap (quiz: why applymap and not agg or apply?) 
# and save the result in a new DataFrame called unemp_bins.


# In[92]:

dummy = pd.DataFrame({'data':[100,150,20,40,30]})

unemp_bins = unemp.applymap(categorize_number)

# Print the original and new DataFrames
print("Original DataFrame:")
print(unemp)
print("\nNew DataFrame with categorized values:")
print(unemp_bins)


# In[ ]:

# Applymap maps the function to all the columns of the data frame irrespective of the datatype.


# In[ ]:

#1) Use another transform on unemp_bins to count how many times each state had each of the three classifications.


# In[103]:

state_counts = unemp_bins.stack().reset_index(name='classification').groupby(['state', 'classification']).count()

state_counts


# In[104]:

# 2) Construct a horizontal bar chart of the number of occurrences of each level with one bar per state and classification
state_counts.unstack().plot(kind='barh', stacked=True)


# In[107]:

# 4) count how many states had each classification in each month

month_counts = unemp_bins.apply(pd.Series.value_counts, axis=1)
month_counts


# In[113]:

# Which month had the most states with high unemployment? What about medium

#Ans - high -> 2001-04-01 00:00:00
# medium -> 2000-11-01 00:00:00

print(month_counts.loc[:, 'high'].idxmax())
print(month_counts.loc[:, 'medium'].idxmax())

# As per the classification defined above there is not data point which qualifies under 'low'


# In[114]:

#Excercise 4

tx_unemp_bins = unemp_bins.loc[:, 'Texas']
tx_unemp = unemp.loc[:, 'Texas']
tx_unemp_by_bins = tx_unemp.groupby(tx_unemp_bins)

tx_unemp_by_bins.mean()

#Inorder to iterate this among all the states, I would either use a loop or apply functions such as applymap/apply


# In[115]:

# Which states in our sample performs the best during “bad times?” To determine this, 
# compute the mean unemployment for each state only for months in which the mean unemployment rate 
    #in our sample is greater than 7

state_means = unemp.mean()
high_unemp_months = unemp.loc[unemp.mean(axis=1) > 7, :]
state_means_high_unemp = high_unemp_months.mean()

# based on the results generated above, Texas performed the best among the sampled states.


# In[ ]:



