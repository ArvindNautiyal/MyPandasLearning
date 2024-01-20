#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import numpy as np


# Merging 12 months of Data in One Dataframe

# In[2]:


files = [file for file in os.listdir(r"C:\Users\DELL\Documents\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data") ]
files


# In[3]:


df = pd.DataFrame()


# In[4]:


for file in files: 
    df_temp = pd.read_csv( r"C:\Users\DELL\Documents\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data/" + file )
    df = pd.concat([df,df_temp],ignore_index=True)


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.to_csv(r"E:\Python 100 Days\Pandas\Sales.Analysis-1.csv",index=False,)


# In[8]:


df= pd.read_csv(r"E:\Python 100 Days\Pandas\Sales.Analysis-1.csv")
df.head()


# In[9]:


filt = df.groupby("Order Date")


# In[10]:


filt.head(10)


# In[11]:


df.rename(columns={"Order Date":"Order_Date"},inplace=True)


# In[ ]:





# In[13]:


df["Month"] = df["Order_Date"].str[0:2]
df.drop(index=1,inplace=True)


# In[14]:


df.head()


# In[15]:


a = np.arange(0,186849)


# In[16]:


df["Index"]=a


# In[17]:


df.set_index("Index",inplace=True)


# In[18]:


df.shape


# In[19]:


df.head(4)


# In[20]:


df.isnull().sum()
df.shape


# In[21]:


df.dropna(axis="index",how="all",inplace=True)


# In[22]:


df.isnull().sum()


# In[23]:


df.drop_duplicates(df[df.Order_Date.str[0:2]=="Or"],inplace=True)


# In[24]:


df.drop(index=518,inplace=True)


# In[25]:


df["Month"] = df["Month"].astype("int32")


# In[26]:


df.head(10)


# In[27]:


df["Quantity Ordered"]  = df["Quantity Ordered"].astype("int32")


# In[28]:


df["Price Each"]  = pd.to_numeric(df["Price Each"])


# In[29]:


df["Sales"] = df["Quantity Ordered"] * df["Price Each"]


# In[ ]:





# In[30]:


df


# In[31]:


df.loc[df["Month"]==4]["Sales"].count()


# In[32]:


mf=df.groupby("Month").sum()


# In[34]:


mf.nlargest(5,columns="Sales")


# In[ ]:


df["Month in Name"] = df["Month"].map({1:"Jan",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"oct",11:"Nov",12:"Dec"})


# In[35]:


df


# In[36]:


a = mf["Sales"]


# What is the best month for sales , How much was earned that month

# In[37]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[38]:


mf.nlargest(5,columns="Sales")


# In[40]:


mf.nlargest(5,columns="Sales")


# In[42]:


import matplotlib.pyplot as plt
b = range(1,13)


# In[43]:


colors =["b"  ,"g", "r", "c" , "m" , "y" , "k" , "g", "b"  ,"g", "r", "c"]
plt.bar(b,a,color=colors)
plt.xticks(b)
plt.title("Sales Monthly")
plt.xlabel("Months")
plt.ylabel("Sales")



# Which US city have the highest number of sales

# In[44]:


df


# In[45]:


def get_city(address):
    return address.split(",")[1]
def get_state(address):
    return address.split(",")[2].split(" ")[1]


# In[ ]:





# In[46]:


df["City-name"]= df["Purchase Address"].apply(lambda x: get_city(x) + " " + (get_state(x)))


# In[47]:


df


# In[48]:


mf=df.groupby("City-name").sum()


# In[49]:


mf


# In[50]:


mf.nlargest(4,"Sales")


# In[51]:


a = df["City-name"].unique()


# In[52]:


a


# In[53]:


c = mf["Sales"]
c


# In[54]:


a


# In[55]:


df


# In[56]:


b = np.arange(1,11)
plt.bar(b,c)
plt.show()



# In[57]:


df


# In[61]:


df["Order_Date"] = pd.to_datetime(df["Order_Date"])


# In[62]:


df.head()


# In[63]:


df["Order_Date"]


# In[64]:


df["Order_Date"].dtype


# In[72]:


df["Order_Date"] = df["Order_Date"].astype(str)


# In[73]:


df.head()


# In[74]:


df["Order_Date"]


# In[77]:


def hours(hour):
    return hour.split(" ")[1].split(":")[0]
df["Hour"] = df["Order_Date"].apply(lambda x: hours(x))


# In[78]:


df.head(5)


# In[81]:


df1= df.groupby("Hour").sum()


# In[82]:


df1.nlargest(5,columns="Sales")


# In[83]:


df


# In[87]:


df["Order_Date"] = pd.to_datetime(df["Order_Date"])


# In[88]:


df["Hours"] = df["Order_Date"].dt.hour


# In[89]:


df


# In[95]:


df["Minute"]= df["Order_Date"].dt.minute


# In[96]:


df


# In[97]:


df2=df.groupby("Minute").sum()


# In[98]:


df2.nlargest(5,columns="Sales")


# What product has been sold often ?

# In[99]:


df.head()


# In[ ]:





# In[ ]:





# In[100]:


df["Product"].unique()


# In[101]:


df3 = df.groupby("Product").sum()


# In[103]:


df3.nlargest(5,columns="Sales")


# In[105]:


df["Order ID"].value_counts()


# In[115]:


df.head()


# In[131]:


df


# In[141]:


df5 = df[df["Order ID"].duplicated(keep=False)]


# In[158]:


df5


# In[165]:


df5["Grouped"] = df5.groupby("Order ID")["Product"].transform(lambda x: ",".join(x))


# In[166]:


df5


# In[171]:


df = df5[["Order ID","Grouped"]].drop_duplicates()


# In[172]:


df


# In[174]:


df5.head(2)


# In[175]:


product_sold = df5.groupby("Product")["Quantity Ordered"].count()


# In[177]:


product_sold.nlargest(5)

