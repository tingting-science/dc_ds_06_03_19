#!/usr/bin/env python
# coding: utf-8

# # Pandas and numpy - pair-up
# ### Discussion session

# 1. How will you read the following data into a pandas data frame ? 
#  ` ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt`

# In[6]:


import numpy as np
import pandas as pd


# In[7]:


url = 'ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt' #file link


# In[8]:


cols = ['Year','Month','Date', 'average','interpolated','trend','days'] #col names


# In[9]:


df=pd.read_csv(url,comment='#', delim_whitespace=True, names = cols) #load file


# In[10]:


df.head(5) #check


# 2. How would you pick columns 0,1,3 ?  
# `[[0, 1, 3]]`

# In[11]:


cols_sub =[df.columns[n] for n in(0,1,3)] #retrieve col list
cols_sub


# In[12]:


df[cols_sub].head() #check


# 3. Use a for loop to find all rows where 
# Co2 (column 3) enteries with the value -99.99 (these are missing values) and replace them with NaN values (try using np.nan - do you know what it is? )

# In[13]:


mask = df['average'] == -99.99 #check 
df.loc[mask,'average']


# In[14]:


df['average'].replace(to_replace = -99.99, value = np.nan, inplace=True) #replace value


# In[15]:


df.loc[mask,'average'] #check


# 4. Change names of columns to year, month, and CO2 (use colnames)

# strip spaces of col names
# ```python
# df.columns = df.columns.str.strip()
# ```

# In[16]:


df.columns = ['Year','Month','Date', 'C02_average','interpolated','trend','days'] #update col names


# In[17]:


df.head() #check


# 5. Add a column 'Day' and specifiy the day 15 for all enteries

# In[18]:


df.insert(len(df.columns),'Day',15) #insert col at the end


# In[19]:


df.head() #check


# 6. Add a date column according to the 'year', 'month' and 'day' columns (options: use apply with lambda or for loop together with datetime.date (make sure to import it)) 
# 
# **? datetime.date ?**
# 
# ```python
# pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute']])
# or 
# pd.to_datetime(dict(year=df.Y, month=df.M, day=df.D))
# #dtype: datetime64[ns]
# #2015-02-04 02:10:00
# ```

# In[26]:


from datetime import date


# In[27]:


df.insert(len(df.columns),'date',pd.to_datetime(df[['Year','Month','Day']])) #add date col


# In[51]:


print(df.head())


# 7. Drop the 'Day' column

# In[29]:


df.drop(columns=['Day'], inplace=True) #drop col


# In[33]:


df.head(10)


# In[34]:


df.shape


# 8. use pandas groupby to print the yeaerly avg. of co2 per year. 

# In[50]:


print(df['C02_average'].groupby(df['Year']).mean())


# 9. Pick columns that you think could be used to build a model and store them in numpy array (Answer why do we do that?)

# ```python
# # The "average" column contains the monthly mean CO2 mole fraction determined
# # from daily averages.  The mole fraction of CO2, expressed as parts per million
# # (ppm) is the number of molecules of CO2 in every one million molecules of dried
# # air (water vapor removed). 
# 
# # CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
# #
# #  (-99.99 missing data;  -1 no data for #daily means in month)
# 
# # The interpolated monthly mean is then the sum of the average seasonal cycle
# # value and the trend value for the missing month.
#     # seasonal: compute for each month the average seasonal cycle in a 7-year window around each monthly value
#     # trend: by removing the seasonal cycle, linearly interpolated for missing months
# ```

# **Q? Depends what is the goal of the analysis? Not sure**
# 
# Pick col ['Year', 'Month', 'C02_average'] for now

# In[35]:


col_arr = ['Year', 'Month', 'C02_average']
arr = df[col_arr].values
arr


# 10. repeat step (3) but this time using the np.where command. 
# ```python
# # Intuitively, np.where is like asking "tell me where in this array, entries satisfy a given condition".
# a = np.arange(5,10)
# np.where(a < 8)       # tell me where in a, entries are < 8
# Out[]: (array([0, 1, 2]),)       # answer: entries indexed by 0, 1, 2
# a[np.where(a < 8)] 
# Out[]: array([5, 6, 7])          # selects from a entries 0, 1, 2    
# ```

# In[47]:


np.isnan(arr) #check


# In[46]:


np.isnan(arr).any() #check


# In[45]:


print(np.where(np.isnan(arr))) # return list of row index, list of col index, with nan values


# In[42]:


#does not work:  np.where(arr is np.nan)


# In[48]:


arr[np.where(np.isnan(arr))]


# ```python
# # If you have an ndarray named arr, you can replace all elements >255 with a value x as follows:
# arr[arr > 255] = x
# # test
# In [1]: import numpy as np
# In [2]: A = np.random.rand(500, 500)
# In [3]: timeit A[A > 0.5] = 5
# 100 loops, best of 3: 7.59 ms per loop
# ```    

# 11. Download the notebook as .py script and run it from your terminal. 

# In[ ]:





# 12. Create a branch in github repository called warm_up_draft  

# In[ ]:





# 13. push the notebook with the name CO2 to your new branch on github.

# In[ ]:




