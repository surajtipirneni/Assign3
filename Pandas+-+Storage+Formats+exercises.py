
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

url = "https://raw.githubusercontent.com/fivethirtyeight/nfl-elo-game/"
url = url + "3488b7d0b46c5f6583679bc40fb3a42d729abd39/data/nfl_games.csv"


# In[11]:

nf1 = pd.read_csv(url, index_col=0)


# In[12]:

get_ipython().run_cell_magic('time', '', 'nf1.to_excel("nfl.xlsx")')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



