
# coding: utf-8

# ### 1.  Create a dictionary where each object contains a list of one float (Age) and one string (Family name) (at least 5 objects)
# Example:
# `{Charles: [23.4, "Darwin"], Alan: [42.5, "Turing"]}`

# In[9]:


people_dict = {'Andrew':[20.4, 'Li'] ,
               'Bob':[15.5, 'Wang'],
               'Cindy':[30.6, 'Zhou'],
               'Roger':[40.8, 'Sun'],
               'Hellen':[25.3,'Qian']}
print(people_dict)


# ### 2. Delete one object from the dictionary

# In[10]:


people_dict.pop('Cindy')


# In[11]:


print(people_dict)


# ### 3. Replace the float number of one of your objects - we are changing a list entry inside a dictionary record! look at Darwin's new age
#
# Example:
# `{Charles: [99.73, "Darwin"], Alan: [42.5, "Turing"]}`

# In[12]:


people_dict['Bob'][0]=19
print(people_dict)


# ### 4. write a for loop that goes through all records in the dictionary, prints the family name and assigns the float numbers into one merged list (see ages)
#
# `ages = [23.4, 22.9, 552.9]`

# In[13]:


names = []
ages = []
for key, value in people_dict.items():
    ages.append(value[0])
    names.append(value[1])
print(names)
print(ages)


# ### 5. Download your notebbok as a .py (regular python script) save it somewhere you know

# ### 6. Go to terminal, navigate to the folder where you have saved the script and execute it through the terminal
#
# `use commandds:
# cd and
# python your_script.py`

# ### [optional] Calculate with a for loop the median and mean of the ages list
