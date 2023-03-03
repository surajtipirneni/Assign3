
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

#Excercise 1

c2n = "#39"
number = int(c2n[1:])   # removes the "#" symbol and converts the remaining characters to an integer
print(number)


# In[ ]:

#Excercise 2


# In[4]:

df = pd.DataFrame({"numbers": ["#23", "#24", "#18", "#14", "#12", "#10", "#35"],
                   "nums": ["23", "24", "18", "14", np.nan, "XYZ", "35"],
                   "colors": ["green", "red", "yellow", "orange", "purple", "blue", "pink"],
                   "other_column": [0, 1, 0, 2, 1, 0, 2]})

df['colors_upper'] = df['colors'].str.upper()


# In[5]:

df


# In[ ]:

#Excercise 3


# In[6]:

df['nums_tonumeric'] = pd.to_numeric(df['nums'], errors='coerce')


# In[24]:

pd.to_numeric(df['numbers'], errors='coerce')

# In pd.to_numeric(), the errors='coerce' parameter is used to replace any non-numeric values in the nums column with NaN
# this end up replacing all the values in the column 'numbers' with NaN


# In[ ]:

#Excercise 4


# In[66]:

url = "https://datascience.quantecon.org/assets/data/chipotle_raw.csv.zip"
chipotle = pd.read_csv(url)

chipotle


# In[60]:

chipotle["item_price_int"] = chipotle["item_price"].str.replace("$", "")


# In[61]:

chipotle["item_price_int1"] = pd.to_numeric(chipotle['item_price_int'], errors='coerce')


# In[62]:

# What is the average price of an item with chicken?
chicken_items = chipotle[chipotle['item_name'].str.contains('Chicken')]
average_price_chicken = chicken_items['item_price_int1'].mean()

# Print the result
print("The average price of an item with chicken is: $", round(average_price_chicken, 2))


# In[63]:

# What is the average price of an item with steak?
steak_items = chipotle[chipotle['item_name'].str.contains('steak') | chipotle['item_name'].str.contains('Steak')]
average_price_steak = steak_items['item_price_int1'].mean()

# Print the result
print("The average price of an item with steak is: $", round(average_price_steak, 2))


# In[64]:

# Did chicken or steak produce more revenue (total)?

chicken_total = chicken_items['item_price_int1'].sum()
steak_total = steak_items['item_price_int1'].sum()

if chicken_total>steak_total:
    print("Chicken items produced more revenue",chicken_total - steak_total)
elif steak_total>chicken_totalsteak_total:
    print("Steak items produced more revenue")
else:
    print("Both produced same revenue")


# In[65]:

# How many missing items are there in this dataset? How many missing items in each column?

total_missing = chipotle.isna().sum().sum()

# Count the number of missing values in each column
column_missing = chipotle.isna().sum()

# Print the results
print("Total missing values: ", total_missing)
print("Missing values in each column: ")
print(column_missing)

# Based on the results from the above code,
# A total of 1246 values are missing in the data frame.
# Only choice_descripton is missing values and it has a total of 1246 missing data points. 
# Rest all the columns dont have missing values


# In[ ]:



