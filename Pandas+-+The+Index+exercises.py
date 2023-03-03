
# coding: utf-8

# In[47]:

import pandas as pd
import numpy as np


# In[2]:

url = "https://datascience.quantecon.org/assets/data/wdi_data.csv"
df = pd.read_csv(url)
df.info()

df.head()


# In[3]:

df_small = df.head(5)
df_small


# In[4]:

df_tiny = df.iloc[[0, 3, 2, 4], :]
df_tiny


# In[5]:

im_ex = df_small[["Imports", "Exports"]]
im_ex_copy = im_ex.copy()
im_ex_copy


# In[6]:

im_ex_tiny = df_tiny + im_ex
im_ex_tiny


# In[7]:

#Excercise 1
# What happens when you apply the mean method to im_ex_tiny?

im_ex_tiny.agg('mean')
#This generated the mean of the columns and the ones with NaN, just returned a NaN value


# In[ ]:

#Excercise 2


# In[4]:

url = "https://datascience.quantecon.org/assets/data/wdi_data.csv"
df = pd.read_csv(url)
df.info()
df.head()


# In[5]:

wdi = df.set_index(["country", "year"])
wdi.head(20)


# In[24]:

wdi.loc[["United States", "Canada"]]

# the command returns all the data associated with the outer most index where the values are either United States or Canada
# Type of returned value: dataframe with float values
# The operation is performing a data selecion using the loc command of pandas. 
    #pandas maps data wrt the indices and returns the data associated with the index when .loc is used.


# In[23]:

wdi.loc[(["United States", "Canada"], [2010, 2011, 2012]), :].dtypes

# the command returns all the data associated with the outer most index where the values are either United States or Canada 
    # and the secondary index where year is 2010,or 2011, or 2012
    
# Type of returned value: float 
# The operation is performing a data selecion using the loc command of pandas. 
    #pandas maps data wrt the indices and returns the data associated with the index when .loc is used.


# In[26]:

wdi.loc["United States"]

# all rows where the outer most index value is equal to United States
    
# Type of returned value:  dataframe with float values
# The operation is performing a data selecion using the loc command of pandas. 
    #pandas maps data wrt the indices and returns the data associated with the index when .loc is used.


# In[27]:

wdi.loc[("United States", 2010), ["GDP", "Exports"]]
# all data where the outer-most index value is equal to "United States and the second level is equal to 2010 
    #and the columns are GDP or Exports
    
# Type of returned value: float
# The operation is performing a data selecion using the loc command of pandas. 
    #pandas maps data wrt the indices and returns the data associated with the index when .loc is used.


# In[28]:

wdi.loc[("United States", 2010)]
# all data where the outer-most index value is equal to "United States and the second level is equal to 2010
    
# Type of returned value: float
# The operation is performing a data selecion using the loc command of pandas. 
    #pandas maps data wrt the indices and returns the data associated with the index when .loc is used.


# In[31]:

wdi.loc[[("United States", 2010), ("Canada", 2015)]]
# all rows where the outer most and inner most index value is equal to United States and 2010 or Canada and 2015
    
# Type of returned value:  dataframe with float values
# The operation is performing a data selecion using the loc command of pandas. 
    #pandas maps data wrt the indices and returns the data associated with the index when .loc is used.


# In[32]:

wdi.loc[["United States", "Canada"], "GDP"]
# all data where the outer most index value is equal to United States or Canada and column name is GDP
    
# Type of returned value: float
# The operation is performing a data selecion using the loc command of pandas. 
    #pandas maps data wrt the indices and returns the data associated with the index when .loc is used.


# In[33]:

wdi.loc["United States", "GDP"]
# all rows where the outer most index value is equal to United States and column name is GDP
    
# Type of returned value: float
# The operation is performing a data selecion using the loc command of pandas. 
    #pandas maps data wrt the indices and returns the data associated with the index when .loc is used.


# In[ ]:

#Excercise 3


# In[37]:

my_df = wdi.loc['United States']


# In[42]:


#Then see what happens when you do wdi / my_df or my_df ** wdi.
my_df ** wdiwdi / my_df
# The data frame is divided by a subset using the operator "/". the division operation is performed element-wise.
my_df ** wdi
#Elementwise exponenitation is performed on the values of wdi wrt values of my_df


# In[39]:

wdi.loc['Canada']


# In[43]:

my_df = wdi.loc['Canada']


# In[45]:

wdi / my_df
# The data frame is divided by a subset using the operator "/". the division operation is performed element-wise.
my_df ** wdi
#Elementwise exponenitation is performed on the values of wdi wrt values of my_df


# In[53]:

#Excercise 4


# In[48]:

wdi2 = df.set_index(["year", "country"])


# In[52]:

#replicate wdi.loc["United States"]

wdi2.loc[pd.IndexSlice[:, ["United States"]], :]


# In[56]:

#replicate wdi.loc[(["United States", "Canada"], [2010, 2011, 2012]), :]

wdi2.loc[([2010, 2011, 2012], ["United States", "Canada"]),:]


# In[57]:

#replicate wdi.loc[["United States", "Canada"], "GDP"]
wdi2.loc[pd.IndexSlice[:, ["United States","Canada"]], ["GDP"]]


# In[58]:

#Excercise 5


# In[59]:

wdiT = wdi.T  # .T means "transpose" or "swap rows and columns"
wdiT


# In[64]:

# extracting all data for the years 2010, 2012, and 2014
wdiT.loc[:, pd.IndexSlice[:,[2010,2011,2014]]]


# In[ ]:

#Excercise 6


# In[66]:

#Move just the year level of the index back as a column.
wdi.reset_index(level='year')


# In[67]:

## throw away all levels of index
wdi.reset_index(drop=True)


# In[68]:

#Remove country from the index -- don't keep it as a column
wdi.reset_index(level='country',drop=True)


# In[ ]:




# In[ ]:



