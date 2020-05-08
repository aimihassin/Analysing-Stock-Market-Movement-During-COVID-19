#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Import libraries

import pandas as pd
import numpy as np
from tabulate import tabulate


# In[36]:


# Read csv from the scraped data and turn it into a dataframe
df = pd.read_csv('CovidOutput.csv')


# In[37]:


df.head()


# In[38]:


# Check any null values
df.isnull().any().any()


# In[39]:


df.info(null_counts=True)


# In[40]:


type(df)


# In[41]:


df.shape


# In[42]:


# Drop any unnecessary information by choosing only the desired columns

new_df = df.loc[1:212, ['Country,Other', 'TotalCases', 'TotalRecovered', 'TotalDeaths', 'Continent']]

# Rename the columns name

new_df.rename(columns = {'Country,Other':'Country', 'TotalCases':'Total Cases', 'TotalRecovered':'Total Recovered', 'TotalDeaths':'Total Deaths'}, inplace=True)
new_df.head()


# In[43]:


print(new_df.describe())


# In[44]:


# Check for any missing values in the new dataframe

new_df.isna()
new_df.isna().sum()


# In[45]:


# Replace the null values in Total Recovered & Total Deaths columns

new_df[['Total Recovered', 'Total Deaths']] = new_df[['Total Recovered','Total Deaths']].fillna(value=0)


# In[46]:


new_df.tail()


# In[47]:


# Drop any missing value in Country & Continent columns

new_df = new_df.dropna(how='any', subset=['Country', 'Continent'])


# In[49]:


new_df.tail()


# In[50]:


# Re-checking for any null values

new_df.info(null_counts=True)


# In[51]:


# Tabulate the data

print(tabulate(new_df, headers='keys', tablefmt='psql'))

