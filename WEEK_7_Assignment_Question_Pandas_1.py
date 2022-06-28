#!/usr/bin/env python
# coding: utf-8

# ![image-2.png](attachment:image-2.png)

# 

# # Data Analysis Problem on Data Wrangling and Exploring

# 
# 
# ### 1. Import the necessary libraries

# In[ ]:


import numpy as np
import pandas as pd


# ### 2. Import the dataset from this [address](https://raw.githubusercontent.com/svkarthik86/Advance-Python-Numpy/main/olympics_dirty.csv). 

# In[ ]:



olympics_dirty=pd.read_csv("https://raw.githubusercontent.com/svkarthik86/Advance-Python-Numpy/main/olympics_dirty.csv",skiprows=4)
olympics_dirty


# ### 3. Assign it to a variable called odata.

# In[8]:


import pandas as pd
odata=pd.read_csv("https://raw.githubusercontent.com/svkarthik86/Advance-Python-Numpy/main/olympics_dirty.csv",skiprows=4)
odata


# ### 4. show the first 5 entries

# In[ ]:


odata.head(5)


# ###  5. What is the number of observations in the dataset?

# In[ ]:


odata.info()


# In[3]:


odata.size


# ### 6. What is the number of columns in the dataset?

# In[4]:


odata.columns.size


# In[ ]:


odata.shape


# ### 7. Print the name of all the columns.

# In[ ]:


odata.columns


# In[ ]:





# ### 8. How is the dataset indexed?

# In[ ]:


odata.index


# ### 9. Rename the column as  Available_City to City, Edition_year to Edition , Sport_name  to Sport

# In[9]:


odata.rename(columns={'Available_City':'City','Edition_year':'Edition','Sport_name':'Sport'},inplace=True)
odata


# ### 10. How many Athletes own the Gold medal?

# In[5]:


odata[odata['Medal']=='Gold'].shape[0]


# ### 11. Display the male gold medal winners for the 100m Track?

# In[ ]:


odata.query("(Medal=='Gold')and(Gender=='Men')and(Event=='100m')")


# ### 12. Which three countries have won the most medals in recent years (from 1984 to 2008)?

# In[11]:


odata[odata.Edition>1984]


# In[ ]:


odata.NOC.value_counts().head(3)


# ### 13. Which country has won the most men's gold medals in singles badminton over the years? Sort the results alphabetically by the player's  names.

# In[13]:


Mens_Badminton=odata.query("(Medal=='Gold')and(Gender=='Men')and(Discipline=='Badminton')")
Mens_Badminton[Mens_Badminton.Event.str.contains("singles")].sort_values(by='Athlete')


# ### 14. Display the women gold medal winners for the 100m Track?

# In[ ]:


odata.query("(Medal=='Gold')and(Gender=='Women')and(Event=='100m')")


# ### 15. list out the Sliver medal winner @ year 2008?

# In[ ]:


odata.query("(Medal=='Silver')and(Edition=='2008')")


# ### 16.Group by Countries and apply aggregate function min,max,count  on over the year

# In[14]:


odata.rename(columns={'NOC':'Country'},inplace=True)
odata


# In[ ]:


odata.groupby('Country')


# In[ ]:


import numpy as np
odata.groupby('Country')[['Edition']].agg([np.min,np.max])


# In[ ]:




