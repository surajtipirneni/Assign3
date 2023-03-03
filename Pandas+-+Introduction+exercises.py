
# coding: utf-8

# In[9]:

import pandas as pd
get_ipython().magic('matplotlib inline')


# In[ ]:

#Excercise 1


# In[7]:

values = [5.6, 5.3, 4.3, 4.2, 5.8, 5.3, 4.6, 7.8, 9.1, 8., 5.7]
years = list(range(1995, 2017, 2))

unemp = pd.Series(data=values, index=years, name="Unemployment")


# In[12]:

# Display only the first 2 elements of the Series using the .head method.

First_two_elements = unemp.head(2)
First_two_elements


# In[17]:

# Using the plot method, make a bar plot.

unemp.plot('bar')


# In[31]:

# Use .loc to select the lowest/highest unemployment rate shown in the Series

#Highest unemployment rate
high= unemp.index[unemp.values == unemp.max()]
print('Highest', unemp.loc[high])

#Lowest unemployment rate
low = unemp.index[unemp.values == unemp.min()]
print('Lowest', unemp.loc[low])


# In[33]:

# Run the code unemp.dtype below. What does it give you? Where do you think it comes from?
unemp.dtype

# It gives the datatype of the underlying values in the series unemp 


# In[ ]:

#Excercise 2


# In[34]:

data = {
    "NorthEast": [5.9,  5.6,  4.4,  3.8,  5.8,  4.9,  4.3,  7.1,  8.3,  7.9,  5.7],
    "MidWest": [4.5,  4.3,  3.6,  4. ,  5.7,  5.7,  4.9,  8.1,  8.7,  7.4,  5.1],
    "South": [5.3,  5.2,  4.2,  4. ,  5.7,  5.2,  4.3,  7.6,  9.1,  7.4,  5.5],
    "West": [6.6, 6., 5.2, 4.6, 6.5, 5.5, 4.5, 8.6, 10.7, 8.5, 6.1],
    "National": [5.6, 5.3, 4.3, 4.2, 5.8, 5.3, 4.6, 7.8, 9.1, 8., 5.7]
}

unemp_region = pd.DataFrame(data, index=years)
unemp_region


# In[41]:

# Use introspection (or google-fu) to find a way to obtain a list with all of the column names in unemp_region.
unemp_region.columns


# In[45]:

# Using the plot method, make a bar plot. What does it look like now?

unemp_region.plot(kind = 'bar')

#The graph provides a split in data wrt to the columns, 'regions'


# In[ ]:

# Use .loc to select the the unemployment data for the NorthEast and West for the years 1995, 2005, 2011, and 2015.


# In[46]:

unemp_region.loc[[1995,2005,2011,2015],['NorthEast','West']]


# In[48]:

#Run the code unemp_region.dtypes below. What does it give you? How does this compare with unemp.dtype?
unemp_region.dtypes

# It gives the datatypes of all the columns in the dataframe 


# In[ ]:



