#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


df=pd.read_csv("C:\Users\akank\Desktop\Academic\Sem3\Capstone\311_Service_Requests_from_2010_to_Present.csv","r")


# In[14]:


df=pd.read_csv(r"C:\Users\akank\Desktop\Academic\Sem3\Capstone\311_Service_Requests_from_2010_to_Present.csv")


# In[15]:


print(df)


# In[16]:


data.head(3)


# In[17]:


df.head(3)


# In[18]:


df.tail(3)


# In[19]:


df.shape


# In[20]:


df.ndim


# In[21]:


df.dtypes


# In[27]:


df["Borough"].value_counts().plot(kind="barh")


# In[28]:


df["Complaint Type"].value_counts()


# In[29]:


from pandas import crosstab
complaints = crosstab(df["Borough"],df["Complaint Type"])
complaints


# In[46]:


HEAT = df[df["Complaint Type"]=="HEATING"]


# In[47]:


HEAT 


# In[48]:


df['Item Code'].astype(str)


# In[ ]:


#Importing the required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')

#Read csv file
df_NYC_dataset = pd.read_csv('../input/311_Service_Requests_for_2009.csv')

#5 rows × 52 columns
df_NYC_dataset.head()

#Shape before dropping nan values
df_NYC_dataset.shape

#Displaying the names of the columns in the dataset
df_NYC_dataset.columns

#Complaint type Breakdown with bar plot to figure out majority of complaint types and top 10 complaints
df_NYC_dataset['Complaint Type'].value_counts().plot(kind='barh',alpha=0.6,figsize=(15,30))
plt.show()


#Have a look at the status of tickets
df_NYC_dataset['Status'].value_counts().plot(kind='bar',alpha=0.6,figsize=(7,7))
plt.show()

#Group dataset by complaint type to display plot against city
groupedby_complainttype = df_NYC_dataset.groupby('Complaint Type')

grp_data = groupedby_complainttype.get_group('HEATING')
grp_data.shape


#To get nan values in the entire dataset
df_NYC_dataset.isnull().sum()


#fix blank values in City column
df_NYC_dataset['City'].dropna(inplace=True)


#Shape after dropping nan values
df_NYC_dataset['City'].shape


#count of null values in grouped city column data
grp_data['City'].isnull().sum()


#fix those NAN with "unknown city" value instead
grp_data['City'].fillna('Unknown City', inplace =True)



#Scatter plot displaying all the cities that raised complaint of type 'HEATING'
plt.figure(figsize=(20, 15))
plt.scatter(grp_data['Complaint Type'],grp_data['City'])
plt.title('Plot showing list of cities that raised complaint of type HEATING')
plt.show()
#Should be somewhat like a straight line


#Find top 10 major complaint types and their counts
groupedby_complainttype['Complaint Type'].value_counts().nlargest(10)


#fix Location type those NAN with "unknown Location" value instead
df_NYC_dataset['Location Type'].fillna('Unknown Loc', inplace =True)



df_NYC_dataset['Location Type'].values

#count of null values in grouped location type column data
grp_data['Location Type'].isnull().sum()



#Plot Major complaint type Heating against location type to check for any pattern
plt.figure(figsize=(3,3))
plt.scatter(grp_data['Complaint Type'],grp_data['Location Type'])
plt.title='Plot complaint type Heating against location type'
plt.xlabel='Complaint Type'
plt.ylabel='Location Type'
plt.show()
#Plot below gives us a clear picture of the fact that all the complaints rasied of type "HEATING" in 2009 
#occured only in Residential Building! This shows that majority of complaints recorded was from Residential Building!



# In[80]:


#Already done still testing once again
import pandas as pd


# In[52]:


import numpy as np


# In[53]:


import matplotlib.pyplot as plt


# In[54]:


import seaborn as sns 


# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[59]:



#read file
df=pd.read_csv(r"C:\Users\akank\Desktop\Academic\Sem3\Capstone\311_Service_Requests_from_2010_to_Present.csv")


# In[61]:



#5 rows × 52 columns
df.head()



# In[62]:


# Shape with nan values
df.shape


# In[63]:


#Display the names of the columns
df.columns


# In[81]:


#analysis of complaints,  majority of complaint types and top 10 complaints
#we can change the attributes or any co-ordinates and try some diff analysis
df['Complaint Type'].value_counts().plot(kind='barh',alpha=0.6,figsize=(15,30))
plt.show()


# In[65]:


#ticket statuses
df['Status'].value_counts().plot(kind='bar',alpha=0.6,figsize=(7,7))
plt.show()


# In[66]:


#Group dataset by complaint type,  displayed  plot against city(doubtful happended)
groupedby_complainttype = df.groupby('Complaint Type')


# In[67]:




grp_data = groupedby_complainttype.get_group('HEATING')


# In[68]:


grp_data.shape



# In[69]:


#total nan values in the dataset
df.isnull().sum()



# In[70]:


#fix blank values in City column or replacing the nan values
df['City'].dropna(inplace=True)



# In[71]:


#Shape w/o nan values
df['City'].shape


# In[72]:


#count of total null values in grouped city column
grp_data['City'].isnull().sum()


# In[73]:


# NAN values replaced with the "unknown city" value 
grp_data['City'].fillna('Unknown City', inplace =True)




# In[74]:


# display all the cities that complained of HEATING
plt.figure(figsize=(20, 15))
plt.scatter(grp_data['Complaint Type'],grp_data['City'])
plt.title('Plot showing list of cities that raised complaint of type HEATING')
plt.show()
#its a straight line (Pushkar-look into it)


# In[75]:


#Top 10 complaint, their counts and types. 
groupedby_complainttype['Complaint Type'].value_counts().nlargest(10)



# In[76]:


#nan Location type palced with "unknown Location" 
df['Location Type'].fillna('Unknown Loc', inplace =True)




# In[77]:


df['Location Type'].values


# In[78]:


#no of null values in location type column
grp_data['Location Type'].isnull().sum()




# In[79]:


#Plot Major complaint type Heating against location type to check for any pattern
plt.figure(figsize=(3,3))
plt.scatter(grp_data['Complaint Type'],grp_data['Location Type'])
plt.title='Plot complaint type Heating against location type'
plt.xlabel='Complaint Type'
plt.ylabel='Location Type'
plt.show()
#Plot below gives us a clear picture of the fact that all the complaints rasied of type "HEATING" in 2010 
#occured only in Residential Building! This shows that majority of complaints recorded was from Residential Building!


# In[115]:


import numpy as np


# In[117]:


temp = df.sample(frac=0.01, replace=True)


# In[125]:


#Randomly selecting some records from the dataset.
print(temp)
#[10150 rows x 41 columns]


# In[119]:


meanDict = dict(df.isnull().mean())


# In[122]:


#Finding the mean off the non null values
print(meanDict)


# In[121]:


mean = np.mean(list(meanDict.values()))


# In[133]:


#Finding the mean of the above calculated mean
print(mean)


# In[126]:


print(df)
#[1014998 rows x 41 columns]


# In[128]:


#Setting the threshold
df1 = df.loc[:, df.isnull().mean() < .8]


# In[130]:


#[1014998 rows x 30 columns]
print(df1)


# In[131]:


deletedCols = list(set(list(df.columns)) - set(list(df1.columns)))


# In[132]:


print(deletedCols)

