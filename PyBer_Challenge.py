#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')

# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load
city_data_to_load = "Resources/city_data.csv"
ride_data_to_load = "Resources/ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)


# In[2]:


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df.head()


# In[3]:


#  1. Get the total rides for each city type
total_rides_by_city_type = pyber_data_df.groupby(["type"]).count()["ride_id"]
total_rides_by_city_type


# In[4]:


# 2. Get the total drivers for each city type
total_drivers_by_city_type = city_data_df.groupby(["type"]).sum()["driver_count"]
total_drivers_by_city_type


# In[5]:


# 3. Get the total amount of fares for each city type
total_fares_by_city_type = pyber_data_df.groupby(["type"]).sum()["fare"]
total_fares_by_city_type


# In[6]:


#  4. Get the average fare per ride for each city type.
avgfares_perride_by_city_type = total_fares_by_city_type / total_rides_by_city_type
avgfares_perride_by_city_type


# In[7]:


# 5. Get the average fare per driver for each city type.
avgfare_perdriver_by_city_type = total_fares_by_city_type / total_drivers_by_city_type
avgfare_perdriver_by_city_type


# In[8]:


#  6. Create a PyBer summary DataFrame.
pyber_summary_df = pd.DataFrame({
            "Total Rides": total_rides_by_city_type,
            "Total Drivers": total_drivers_by_city_type,
            "Total Fares": avgfares_perride_by_city_type,
            "Average Fare per Ride": avgfares_perride_by_city_type,
            "Average Fare per Driver": avgfare_perdriver_by_city_type
})
pyber_summary_df


# In[9]:


#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None


# In[10]:


#  8. Format the columns.
pyber_summary_df['Total Rides'] = pyber_summary_df['Total Rides'].map('{:,}'.format)
pyber_summary_df['Total Drivers'] = pyber_summary_df['Total Drivers'].map('{:,}'.format)
pyber_summary_df['Total Fares'] = pyber_summary_df['Total Fares'].map('${:,.2f}'.format)
pyber_summary_df['Average Fare per Ride'] = pyber_summary_df['Average Fare per Ride'].map('${:,.2f}'.format)
pyber_summary_df['Average Fare per Driver'] = pyber_summary_df['Average Fare per Driver'].map('${:,.2f}'.format)
pyber_summary_df


# In[11]:


# Deliverable 2


# In[12]:


# 1. Read the merged DataFrame
pyber_data_df.head()


# In[13]:


# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.
total_fare_per_day = pyber_data_df.groupby(['type','date']).sum()['fare']
total_fare_per_day


# In[14]:


# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
# df = df.reset_index()

total_fare_per_day = total_fare_per_day.reset_index()
total_fare_per_day.head()


# In[15]:


# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date.
total_fare_per_day_pivot = total_fare_per_day.pivot(index='date', columns='type', values='fare')
total_fare_per_day_pivot


# In[16]:


# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
jan_apr_fare_per_day = total_fare_per_day_pivot.loc['2019-01-01':'2019-04-28']
jan_apr_fare_per_day.tail()


# In[17]:


# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)
jan_apr_fare_per_day.index = pd.to_datetime(jan_apr_fare_per_day.index)


# In[18]:


# 7. Check that the datatype for the index is datetime using df.info()
jan_apr_fare_per_day.info()


# In[19]:


# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
jan_apr_fare_per_week = jan_apr_fare_per_day.resample("W").sum()
jan_apr_fare_per_week.head()


# In[20]:


# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 

import matplotlib.dates as mdates

# Import the style from Matplotlib.
from matplotlib import style

# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')

fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(jan_apr_fare_per_week)
ax.set_ylabel('Fare ($USD)',fontsize=14)
ax.set_xticks(pd.date_range(start = "2019-01-01", end = "2019-04-30", freq="MS"))
ax.set_title("Total Fare by City Type")
# Make ticks on occurrences of each month:
ax.xaxis.set_major_locator(mdates.MonthLocator())

# Get only the month to show in the x-axis:
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.legend(["Rural","Suburban","Urban"])

# Import the style from Matplotlib.
from matplotlib import style

# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')

# Save the figure.
plt.savefig("PyBer_fare_summary.png")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




