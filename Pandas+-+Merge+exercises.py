
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

# from WDI. Units trillions of 2010 USD
url = "https://datascience.quantecon.org/assets/data/wdi_data.csv"
wdi = pd.read_csv(url).set_index(["country", "year"])
wdi.info()

wdi2017 = wdi.xs(2017, level="year")
wdi2017


# In[3]:

wdi2017_no_US = wdi2017.drop("United States")
wdi2017_no_US


# In[5]:

# Data from https://www.nationmaster.com/country-info/stats/Geography/Land-area/Square-miles
# units -- millions of square miles
sq_miles = pd.Series({
   "United States": 3.8,
   "Canada": 3.8,
   "Germany": 0.137,
   "United Kingdom": 0.0936,
   "Russia": 6.6,
}, name="sq_miles").to_frame()
sq_miles.index.name = "country"
sq_miles


# In[6]:

sq_miles_no_germany = sq_miles.drop("Germany")
sq_miles_no_germany


# In[ ]:

#Excercise 2


# In[ ]:

#Compare the how="left" with how="inner" options using the DataFrames wdi2017_no_US and sq_miles_no_germany.
#Are the different? How?

'''The how="inner" option specifies that we only want to include the rows that have a matching value in both DataFrames. 
This means that any rows in wdi2017_no_US that do not have a corresponding value in sq_miles_no_germany will be excluded 
from the merged DataFrame.'''

'''By using merge, the DataFrame will have the same number of rows as wdi2017_no_US and will include the values for 
all countries in wdi2017_no_US, but some of the values for the "sq_miles" column may be NaN.'''

#Will this happen for all pairs of DataFrames, or are wdi2017_no_US and sq_miles_no_germany special in some way?

'''this will not happen for all pairs of Data frames. The behavior of how="left" versus how="inner" will depend on
the specific DataFrames being merged and the values in the columns used for merging.'''

# Also compare how="right" and how="outer" and answer the same questions. 

'''When using how="right", the resulting DataFrame will contain all rows from the right DataFrame (sq_miles_no_germany), 
with NaN values in the columns from the left DataFrame (wdi2017_no_US) if there are no matching rows in the left DataFrame. 
When using how="outer", the resulting DataFrame will contain all rows from both DataFrames 
(wdi2017_no_US and sq_miles_no_germany), with NaN values in any columns where there are missing values in either DataFrame.

In this specific case, since there are no rows in sq_miles_no_germany that are not in wdi2017_no_US,
using how="right" will produce the same result as how="left", and using how="outer" will produce the same result as
how="inner". 
However, this may not be true for other pairs of DataFrames'''


# In[ ]:

#Excercise 1


# In[7]:

# from WDI. Units millions of people
pop_url = "https://datascience.quantecon.org/assets/data/wdi_population.csv"
pop = pd.read_csv(pop_url).set_index(["country", "year"])
pop.info()
pop.head(10)


# In[9]:

# What is the population density of each country? How much does it change over time?
# Merge population data with land area data
merged = pop.merge(sq_miles, left_index=True, right_index=True)

# Calculate population density
merged["pop_density"] = merged["Population"] / merged["sq_miles"]

# Group by country and year and calculate the mean population density
density_by_country_year = merged.groupby(["country", "year"])["pop_density"].mean()

# Print the resulting DataFrame
print(density_by_country_year)


# In[10]:

import matplotlib.pyplot as plt

# Pivot the data to get population density by country for each year
density_by_country = density_by_country_year.unstack(level="country")

# Plot the data
density_by_country.plot.line()
plt.ylabel("Population density (people per square mile)")
plt.show()


# In[ ]:

#Excercise 3


# In[12]:

#Can you pick the correct argument for how such that 
# pd.merge(wdi2017, sq_miles, how="left") is equal to pd.merge(sq_miles, wdi2017, how=XXX)?

pd.merge(wdi2017, sq_miles, how="left") == pd.merge(sq_miles, wdi2017, how="right")


# In[15]:

#Excercise 4

url = "https://datascience.quantecon.org/assets/data/goodreads_books.csv"
books = pd.read_csv(url)
# we only need a few of the columns
books = books[["book_id", "authors", "title"]]

url = "https://datascience.quantecon.org/assets/data/goodreads_ratings.csv.zip"
ratings = pd.read_csv(url)

rated_books = pd.merge(ratings, books)


# In[16]:

# determine the average rating for the books with the least number ratings.
# Is there a distinguishable difference in the average rating compared to the most rated books?
# Did you recognize any of the books?

least_rated_books = rated_books.groupby("title").agg({"rating": "count"}).sort_values(by="rating").head()
average_rating_least_rated = rated_books[rated_books["title"].isin(least_rated_books.index)]["rating"].mean()
print("Average rating for the least rated books:", average_rating_least_rated)


# In[17]:

most_rated_books = rated_books.groupby("title").agg({"rating": "count"}).sort_values(by="rating", ascending=False).head()
average_rating_most_rated = rated_books[rated_books["title"].isin(most_rated_books.index)]["rating"].mean()
print("Average rating for the most rated books:", average_rating_most_rated)


# In[ ]:

'''The difference in average rating between the least rated books and the most rated books depends on the dataset 
and the specific books in it. However, it's worth noting that the number of ratings can be an important factor in book ratings,
as books with more ratings are likely to have a more representative average rating'''


# In[ ]:

#Excercise 5


# In[19]:

dfL = pd.DataFrame(
    {"Key": ["A", "B", "A", "C"], "C1":[1, 2, 3, 4], "C2": [10, 20, 30, 40]},
    index=["L1", "L2", "L3", "L4"]
)[["Key", "C1", "C2"]]


dfR = pd.DataFrame(
    {"Key": ["A", "B", "C", "D"], "C3": [100, 200, 300, 400]},
    index=["R1", "R2", "R3", "R4"]
)[["Key", "C3"]]


# In[ ]:

pd.concat([dfL, dfR], axis=1)


# In[ ]:

'''The output of pd.concat([dfL, dfR], axis=1) will be a new DataFrame that concatenates dfL and dfR horizontally 
(i.e., along axis 1).

The resulting DataFrame will have four rows (L1-L4), corresponding to the indexes of dfL.

The columns of the resulting DataFrame will be "Key", "C1", "C2", "Key", "C3". 
Since both DataFrames have a column named "Key", this will result in two columns with the same name in the output.

The first "Key" column will contain the values from the "Key" column of dfL, 
while the second "Key" column will contain the values from the "Key" column of dfR.

The columns "C1" and "C2" will contain the values from dfL, and the column "C3" will contain the values from dfR.

Since dfR does not have any rows with the index values of dfL, there will be NaN values in the cells where the values
from dfR would be. Specifically, there will be NaNs in rows L2 and L4 for the "Key" and "C3" columns, 
because there are no corresponding values in dfR for those rows.'''


# In[ ]:

# Excercise 6


# In[ ]:

#Determine what happens when you run each of the two cells below.

#For each cell, answer the list of questions from the previous exercise.

# First code cell for above exercise
pd.concat([dfL, dfL], axis=0)

'''The resulting DataFrame has the same columns as the original DataFrames dfL, namely Key, C1, and C2.
The index of the resulting DataFrame has repeated index values. Specifically, the index values of dfL 
appear twice in the resulting DataFrame, with indices L1 through L4 followed by indices L1 through L4 again.
NaNs are not introduced in the resulting DataFrame because all rows have values for all columns.

The resulting DataFrame is essentially the original DataFrame dfL stacked on top of itself, with each row repeated.'''


# In[ ]:

# Second code cell for above exercise
pd.concat([dfR, dfR], axis=1)

'''What are the columns? What about columns with the same name?
The columns are ['Key', 'C3'] and they are the same in both dfR DataFrames, so there are no columns with the same name.

What is the index?
The index is ['R1', 'R2', 'R3', 'R4', 'R1', 'R2', 'R3', 'R4'] since both DataFrames have the same index values.

Do any NaNs get introduced? If so, where? Why?
No, there are no NaNs introduced. All rows have a value for both columns 'Key' and 'C3'.'''


# In[ ]:

# Excercise 7


# In[ ]:

# Describe in words why the output of pd.merge(dfL, dfR, how="right") has more rows than either dfL or dfR.

'''The output of pd.merge(dfL, dfR, how="right") has more rows than either dfL or dfR because "right" merge type 
includes all the rows from the right DataFrame dfR and only those rows from the left DataFrame dfL that have matching values
in the key column(s). 
If there are duplicate values in the key column(s) in the left DataFrame, 
then the number of rows in the output will be greater than the number of rows in the left DataFrame, 
as the duplicate rows will be included in the output for each matching row in the right DataFrame.'''


# In[20]:

# Run the cell below to see the output of that operation
pd.merge(dfL, dfR, how="right")


# In[ ]:



