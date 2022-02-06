#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Load in csv
pyber_ride_df = pd.read_csv("Resources/PyBer_ride_data.csv")
pyber_ride_df


# In[7]:


pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)")
plt.show()


# In[8]:


# Set x-axis and tick locations.
x_axis = np.arange(len(pyber_ride_df))
tick_locations = [value for value in x_axis]
# Plot the data.
pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)")
plt.xticks(tick_locations, pyber_ride_df["Month"])
plt.show()


# In[9]:


pyber_ride_df.plot.bar(x="Month", y="Avg. Fare ($USD)")
plt.show()


# In[10]:


pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)", kind='bar')
plt.show()


# In[11]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd


# In[12]:


# Files to load
city_data_to_load = "Resources/city_data.csv"
ride_data_to_load = "Resources/ride_data.csv"


# In[13]:


# Read the city data file and store it in a pandas DataFrame.
city_data_df = pd.read_csv(city_data_to_load)
city_data_df.head(10)


# In[14]:


# Read the ride data file and store it in a pandas DataFrame.
ride_data_df = pd.read_csv(ride_data_to_load)
ride_data_df.head(10)


# In[15]:


# Get the columns and the rows that are not null.
city_data_df.count()


# In[16]:


# Get the columns and the rows that are not null.
city_data_df.isnull().sum()


# In[17]:


# Get the data types of each column.
city_data_df.dtypes


# In[18]:


# Get the unique values of the type of city.
city_data_df["type"].unique()


# In[19]:


# Get the number of data points from the Urban cities.
sum(city_data_df["type"]=="Urban")


# In[20]:


# Get the number of data points from the Suburban cities.
sum(city_data_df["type"]=="Suburban")


# In[21]:


# Get the number of data points from the Rural cities.
sum(city_data_df["type"]=="Rural")


# In[22]:


# Get the columns and the rows that are not null.
ride_data_df.count()


# In[23]:


# Get the columns and the rows that are not null.
ride_data_df.isnull().sum()


# In[24]:


# Get the data types of each column.
ride_data_df.dtypes


# In[25]:


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the DataFrame
pyber_data_df.head()


# In[ ]:




