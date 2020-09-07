#!/usr/bin/env python
# coding: utf-8

# ## Reviewing the Wine Dataset

# Questions used for exploration of dataset:
# 
# * Do certain varieties of wine receive higher ratings?
# * Do different tasters rate similar wines differently? 
# * Do specific countries produce "better" wines?
# * Is there any relationship between rating and price of a wine?
# * Are there certain descriptions that are associated with higher ratings?
# 

# In[4]:


#Importing Libraries
import numpy as np 
import pandas as pd

pd.set_option('display.max_columns', None) # To display all columns
pd.set_option("display.max_rows",100)

import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns 
sns.set_style('whitegrid') 

data = pd.read_csv("winemag-data-130k-v2.csv")
data.head()


# In[5]:


data = data.iloc[:,1:]


# In[6]:


data.shape


# In[7]:


# remove duplicates
data.drop_duplicates(inplace=True)
data.shape


# In[8]:


for col in data:
    print(data[col].unique());


# ### Points vs. Price

# In[9]:


data.describe()


# In[10]:


sns.regplot(data.points, data.price)

# or plt.scatter(data.points, data.price)


# In[11]:


sns.boxplot(data.points, data.price)


# It appears that the average price of wine is higher as the rating increases. However, this could also be stated as: the rating increases as the price gets higher. Tasters might be biased in their reviews if they know the price of the wine. Alternatively, wines that receive good reviews might tend to get priced higher because of these good reviews.

# In[12]:


data[data.price>=2000]


# The most expensive wine is a French Bordeaux! Overall, 5 out of the 6 most expensive wines come from France.

# ### Points vs. Variety

# In[13]:


data.groupby("variety").agg(['mean', 'median', 'min', 'max','count'])


# There seems to be a wide range of ratings and prices for each wine.

# In[14]:


data.groupby("variety").mean().sort_values(by = "points", ascending = False)


# In[15]:


data.groupby("variety").median().sort_values(by = "points", ascending = False)


# In[16]:


data.groupby("variety").mean().sort_values(by = "price", ascending = False)


# In[17]:


data.groupby("variety").points.count().sort_values(ascending = False)


# In[18]:


data.groupby("variety").points.count().sort_values(ascending = False).describe()


# There are 707 wine varieties, half of which have less than 5 reviews. Pinot Noir is the variety with the most reviews - 12,278.

# ### Points vs. Taster

# In[19]:


data.groupby("taster_name").points.count().sort_values(ascending = False)


# In[20]:


data.groupby("taster_name").points.mean().sort_values(ascending = False)


# In[21]:


data.groupby("taster_name").points.agg(["min","max","mean","count"])


# In[22]:


sns.boxplot(data.taster_name, data.points)
plt.xticks(rotation=90)


# Each taster has completed a different number of reviews, ranging between 6 and 23560 reviews. Overall, tasters seems to cover most of the range of ratings between 80 and 100. The tasters that have a lower ceiling tend to be the ones who have completed fewer reviews.

# ### Points vs. Country

# In[23]:


sns.boxplot(data.country, data.points)
plt.xticks(rotation=90)


# ### Points vs. Reviews

# In[24]:


top = data[data.points >= 95]
top.head()


# In[25]:


bottom = data[data.points <= 85]
bottom.head()

