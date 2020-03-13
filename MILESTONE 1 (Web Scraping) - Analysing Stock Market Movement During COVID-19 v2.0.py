#!/usr/bin/env python
# coding: utf-8

# # Analysing Stock Market Movement During COVID-19
# 
# Coronavirus disease 2019 (COVID-19) is a respiratory illness that can spread from one person to another. This infectious disease is caused by a novel coronavirus that was first identified during an investigation into an outbreak in Wuhan, China, in December 2019. On March 11th, 2020 WHO has characterized COVID-19 as a pandemic as the number of cases that have been detected in most countries worldwide and community spread is keep on increasing. 
# 
# Due to COVID-19, many sectors have been deeply affected including retailers, financial services, travel and hospitality, airline, event management and many more. In this assignment, we would like to see how COVID-19 affects the stock market movement in a few selected sectors that we have chosen. We are using Yahoo Finance in assessing the stock market movement during COVID-19.

# In[36]:


#Install pandas datareader

get_ipython().system('pip install pandas_datareader==0.7.0')

import pandas_datareader
pandas_datareader.__version__

import pandas as pd
from pandas_datareader import data


# Install the yfinance

get_ipython().system('pip install yfinance')

import yfinance as yf


# In[37]:


#Set the start date of the COVID-19 outbreak and the current date

start_date = '2019-12-31'
current_date = '2020-03-12'


# ## Sector 1 : Healthcare
# 
# In this sector, we investigate 5 companies namely Johnson  & Johnson (JNJ), Merk & Co. Inc (MRK), Abbott Laboratories (ABT), Moderna, Inc. (MRNA) and Vir Biotechnology (VIR).

# In[38]:


#Setting for multiple tickers in health sector

tickers_health = ('JNJ', 'MRK', 'ABT', 'MRNA', 'VIR')


# In[39]:


#Get the data from multiple tickers

data_hlth = yf.download(tickers_health,
 start_date,
 current_date)

data_hlth.head()


# In[40]:


df_datahealth=pd.DataFrame(data_hlth)
df_datahealth


# In[41]:


#Visualisation of the adjusted close price data for all tickers

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

data_hlth['Adj Close'].plot(figsize=(10,7))
plt.title("Adjusted Close Price", fontsize=16)
plt.ylabel('Price', fontsize=12)
plt.xlabel('Date', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.1)
plt.show


# In[42]:


#Group the data by tickers

dataHT = yf.download(tickers_health,
 start_date,
 current_date,
 group_by="tickers")

dataHT.head()


# In[43]:


df_dataHT=pd.DataFrame(dataHT)
df_dataHT


# In[44]:


#Convert data to csv file

## Data by stock movement
data_hlth.to_csv("C:/Users/ASUS/Desktop/DataHealthSector_All.csv")

## Data grouped by tickers
dataHT.to_csv("C:/Users/ASUS/Desktop/DataHealthSector_byTickers.csv")


# ## Sector 2 : Industrials
# 
# Meanwhile, in industrials sector, we pick these 5 companies namely Honeywell International Inc. (HON), Union Pacific Corporation (UNP), The Boeing Company (BA), Thomson Reuters Corporation (TRI) and Delta Air Lines, Inc. (DAL).

# In[45]:


#Setting for multiple tickers in industrials sector

tickers_industrials = ('HON', 'UNP', 'BA', 'TRI', 'DAL')


# In[46]:


#Get the data from multiple tickers in industrials

data_ind = yf.download(tickers_industrials,
 start_date,
 current_date)

data_ind.head()


# In[47]:


df_dataindustrials=pd.DataFrame(data_ind)
df_dataindustrials


# In[48]:


#Visualisation of the adjusted close price data for all tickers

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

data_ind['Adj Close'].plot(figsize=(10,7))
plt.title("Adjusted Close Price", fontsize=16)
plt.ylabel('Price', fontsize=12)
plt.xlabel('Date', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.1)
plt.show


# In[49]:


#Group the data by tickers

dataIT = yf.download(tickers_industrials,
 start_date,
 current_date,
 group_by="tickers")

dataIT.head()


# In[50]:


df_dataIT=pd.DataFrame(dataIT)
df_dataIT


# In[51]:


#Convert data to csv file

## Data by stock movement
data_ind.to_csv("C:/Users/ASUS/Desktop/DataIndustrialsSector_All.csv")

## Data grouped by tickers
dataIT.to_csv("C:/Users/ASUS/Desktop/DataIndustrialsSector_byTickers.csv")

