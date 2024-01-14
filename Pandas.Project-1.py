#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Reation_types = pd.read_csv(r"C:\Users\DELL\Downloads\ReactionTypes.csv")
Reactions = pd.read_csv(r"C:\Users\DELL\Downloads\Reactions.csv")
Content = pd.read_csv(r"C:\Users\DELL\Downloads\Content.csv")
df1 = pd.DataFrame(Reation_types)
df2 = pd.DataFrame(Reactions)
df3 = pd.DataFrame(Content)


# In[3]:


df1.isnull().sum()


# In[4]:


df1.shape


# In[5]:


df2.shape


# In[6]:


df3.shape


# In[7]:


df1.isnull().sum() #no null values


# In[8]:


df2.dropna(inplace=True)


# In[9]:


df2.isnull().sum()


# In[10]:


df3.isnull().sum()


# In[11]:


df3.dropna(inplace=True)


# In[12]:


df3.isnull().sum()


# In[13]:


df1.columns


# In[14]:


df1.drop(["Unnamed: 0"],axis=1,inplace=True)


# In[15]:


df1


# In[16]:


df2.drop(["Unnamed: 0"],axis=1,inplace=True)


# In[17]:


df2.head()


# In[18]:


df3.head()


# In[19]:


df3.drop(["Unnamed: 0"],axis=1,inplace=True)


# In[20]:


df3.head()


# In[21]:


df3.drop(["URL"],axis=1,inplace=True)


# In[22]:


df3.columns


# In[23]:


df2.head()


# In[24]:


df1.rename(columns={"Type":"Reaction Type"},inplace=True)


# In[25]:


df2


# In[26]:


df3.rename(columns={"Type":"Content Type"},inplace=True)
df3.head()


# In[27]:


df2.rename(columns={"Type":"Reaction Type"},inplace=True)
df2.head()


# In[28]:


df2.drop(["User ID"],axis=1,inplace=True)
df2.head()


# In[29]:


df3.drop(["User ID"],axis=1,inplace=True)


# In[30]:


df1.head(2)


# In[31]:


df2.head(2)


# In[32]:


df3.head(2)


# In[33]:


df1.duplicated().sum()


# In[34]:


df2.duplicated().sum()


# In[35]:


df3.duplicated().sum()


# In[36]:


df1.columns


# In[37]:


df2.columns


# In[38]:


df3.columns


# In[ ]:


df1.to_csv(r"E:\Python 100 Days\Pandas\DF-1.csv",index=False)


# In[40]:


df2.to_csv(r"E:\Python 100 Days\Pandas\DF-2.csv",index=False)


# In[41]:


df3.to_csv(r"E:\Python 100 Days\Pandas\DF-3.csv",index=False)


# In[42]:


df1


# In[43]:


df3


# In[44]:


df2


# In[45]:


df2.columns


# In[46]:


df1.columns


# In[47]:


df1.head()


# In[48]:


a =df1.set_index("Reaction Type")


# In[49]:


dictionary2 = a.to_dict()["Sentiment"]


# In[50]:


dictionary2


# In[51]:


dictionary= a.to_dict()["Score"]


# In[52]:


dictionary


# In[53]:


df2


# In[54]:


df2["Reaction-Score"]=df2["Reaction Type"].map(dictionary)
df2["Reaction-Sentiment"]=df2["Reaction Type"].map(dictionary2)
df2


# In[55]:


df2


# In[56]:


m = df3.set_index("Content ID") 


# In[57]:


df3.columns


# In[58]:


dictionary3 = m.to_dict()["Category"]


# In[59]:


df2["Category"]=df2["Content ID"].map(dictionary3)


# In[60]:


df2


# In[61]:


dictionary4 = m.to_dict()["Content Type"]


# In[69]:


df2["Content Type"]=df2["Content ID"].map(dictionary4)


# In[74]:


df4=df2


# In[70]:


df2["Content Type"].value_counts()


# In[75]:


df4["Category"].value_counts()


# In[76]:


df4.isnull().sum()


# In[ ]:





# In[77]:


df4["Category"].value_counts()


# In[ ]:





# In[78]:


df4.to_csv(r"E:\Python 100 Days\Pandas\DF-FINAL.csv",index=False)


# In[79]:


df4["Category"].value_counts()


# In[81]:


df4.loc[df4["Category"]=="travel"]["Reaction-Score"].sum()


# In[82]:


l = df4["Category"]


# In[85]:


l2 = []
for i in l:
    if i not in l2:
        l2.append(i)


# In[86]:


l2


# In[87]:


l3 = []
for i in l2:
    a = df4.loc[df4["Category"]==i]["Reaction-Score"].sum()
    l3.append(a)
    


# In[90]:


l3


# In[88]:


res = {l2[i]: l3[i] for i in range(len(l3))}
res


# In[91]:


df4


# How many unique categories are there?
# How many reactions are there to the most popular category?
# What was the month with the most posts?

# In[93]:


df4["Category"].nunique()


# In[94]:


df4["Category"].unique()


# In[ ]:




