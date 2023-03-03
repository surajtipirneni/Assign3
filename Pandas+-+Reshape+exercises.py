
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[3]:

url = "https://datascience.quantecon.org/assets/data/bball.csv"
bball = pd.read_csv(url)
bball.info()
bball.head()


# In[ ]:

#Excercise 1


# In[7]:

bball.drop("TeamName", axis=1).set_index(["Year", "Player", "Team"]).stack().unstack(level=[1, 3, 2]).sort_index(axis=1)


# In[ ]:

#Excercise 2


# In[ ]:

# What do you think would happen if we wrote bball.melt(id_vars=["Year", "Player"]) 
    #rather than bball.melt(id_vars=["Year", "Player", "Team", "TeamName"])? 
#Were you right? Write your thoughts.

'''The resulting melted DataFrame would have only two identifier columns: "Year" and "Player". 
The other columns in the original DataFrame, such as "Team" and "TeamName", 
would be combined into a single "variable" column in the melted DataFrame, 
with their values in a corresponding "value" column.'''


# In[ ]:

#Read the documentation and focus on the argument value_vars. 
#How does bball.melt(id_vars=["Year", "Player"], value_vars=["Pts", "Rebound"]) differ from bball.melt(id_vars=["Year", "Player"])?

'''the main difference between the two calls is that 
bball.melt(id_vars=["Year", "Player"], value_vars=["Pts", "Rebound"]) specifies two variable columns to melt 
into the resulting DataFrame, while bball.melt(id_vars=["Year", "Player"]) 
does not specify any variable columns and therefore includes all non-identifier columns in the melted DataFrame.'''


# In[ ]:

#Consider the differences between bball.stack and bball.melt. Is there a way to make them generate the same output?

'''To make bball.stack() and bball.melt() generate the same output, we can first use bball.stack() 
to stack the column labels down one level to create a hierarchical index, and then use bball.reset_index() 
to move the index levels back to columns. 
Finally, we can use bball.melt() to unpivot the resulting data frame'''


# In[ ]:

bball_stacked = bball.set_index(['Year', 'Player']).stack().reset_index()

# unpivot the data frame
bball_melted = bball_stacked.rename(columns={'level_2': 'variable', 0: 'value'}).melt(id_vars=['Year', 'Player', 'variable'], value_vars='value')


# In[ ]:

#Excercise 3

#Can you think of a reason to ever use pivot rather than pivot_table? Write your thoughts. 

'''Yes, there are cases where using pivot may be more suitable than using pivot_table. Here are some possible reasons:

Simplicity: pivot is simpler to use than pivot_table and requires fewer parameters. 
            If you have a simple DataFrame and want to quickly pivot it based on one or two columns, 
            pivot can be a good option.

Flexibility: pivot allows you to reshape a DataFrame by specifying a single column to use as the index, 
             a single column to use as the columns, and a single column to use as the values. 
             This means that you can create a pivot table that does not perform any aggregation or calculation on the values, 
                 but simply reshapes the data in a useful way. pivot_table, on the other hand, 
                 requires you to specify a function to apply to the values.

Speed: pivot may be faster than pivot_table for small DataFrames. pivot_table involves more complex operations 
such as grouping and aggregation, which can be slower than a simple reshaping of the data using pivot. 
However, for larger DataFrames, the difference in speed may be negligible.'''


# In[8]:

# 
pivot_table = bball.pivot_table(index='Player', columns='TeamName', values=['Rebound', 'Assist'])

# print the pivot table
print(pivot_table)


# In[9]:

pivot_table1 = bball.pivot_table(index='Player', columns='TeamName', values=['Rebound', 'Assist'], aggfunc=[np.max, np.min, len])

# print the pivot table
print(pivot_table1)

'''When you use aggfunc=[np.max, np.min, len] as an argument in the pivot_table method, 
Python produces a pivot table with multiple levels of column headers.'''


# In[ ]:

'''he resulting pivot table will have a multi-level column index, 
where the first level corresponds to the Rebound and Assist columns, 
and the second level corresponds to the applied aggregation function. 
The index of the table remains the same, with one row for each player.'''

