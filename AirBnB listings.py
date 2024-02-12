#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


listing = pd.read_csv(r"C:\Users\Admin\Desktop\EDA\Listings.csv", low_memory=False ,encoding = "ISO-8859-1" )


# In[5]:


listing.head()


# In[6]:


listing.info()


# In[7]:


listing["host_since"] = pd.to_datetime(listing["host_since"] )


# In[8]:


listing.info()


# In[9]:


listing.head()


# In[10]:


listing.shape


# In[11]:


listing.columns


# In[12]:


listing["city"].value_counts()


# In[13]:


paris = listing.loc[listing["city"]=="Paris"]


# In[14]:


paris.shape


# In[15]:


paris.columns


# In[16]:


paris1 = paris.loc[:,["host_since","neighbourhood","city","accommodates","price"]]


# In[17]:


paris1.columns


# In[18]:


paris1.head()


# In[19]:


paris1.shape


# In[20]:


paris1.isnull().sum()


# In[21]:


paris1.dropna(axis="index",how="any",inplace=True)


# In[22]:


paris1.isnull().sum()


# In[23]:


paris1.shape


# In[24]:


paris1.head()


# In[25]:


paris1_neighbour = paris1.groupby("neighbourhood",as_index=False).agg({"price":"mean"})


# In[26]:


paris1_neighbour.sort_values("price",inplace=True)


# In[27]:


paris1_neighbour.tail()


# In[28]:


paris2_accomodate = paris1.loc[paris1["neighbourhood"]=="Elysee"].groupby("accommodates").agg({"price":"mean"}).sort_values("price")


# In[29]:


paris2_accomodate.head()


# In[30]:


paris1.head(3)


# In[31]:


paris1.info()


# In[32]:


paris_ot = paris1.set_index("host_since").resample("Y").agg({"neighbourhood":"count","price":"mean"})


# In[34]:


paris_ot.head()


# In[36]:


paris1_neighbour.head()


# In[47]:


fig , ax = plt.subplots()
ax.barh(paris1_neighbour["neighbourhood"],paris1_neighbour["price"])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xlabel("Average Price",fontsize=14)
ax.set_ylabel("Paris Neighbourhood",fontsize=14)
ax.set_title("Average Price by Neighbourhood",fontsize=14);


# In[49]:


paris2_accomodate.head()


# In[52]:


paris2_accomodate.drop(index=0,inplace=True)


# In[53]:


fig , ax = plt.subplots()
ax.barh(paris2_accomodate.index,paris2_accomodate["price"])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xlabel("Accommodations",fontsize=14)
ax.set_ylabel("Mean Price",fontsize=14)
ax.set_title("Average accomodate",fontsize=14);


# In[54]:


paris_ot


# In[57]:


fig , ax = plt.subplots()
ax.plot(paris_ot.index,paris_ot["neighbourhood"])


# In[58]:


fig , ax = plt.subplots()
ax.plot(paris_ot.index,paris_ot["price"])


# In[81]:


fig , ax = plt.subplots(figsize=(8,6))
ax.plot(paris_ot.index,paris_ot["price"],label="Price")
ax2 = ax.twinx()
ax2.plot(paris_ot.index,paris_ot["neighbourhood"],color="orange",label="Neighbourhood")
fig.legend(bbox_to_anchor=(0.9,0.8))


# In[ ]:




