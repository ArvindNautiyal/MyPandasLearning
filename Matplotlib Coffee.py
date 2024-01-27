#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv(r"C:\Users\DELL\Documents\total-production.csv")


# In[3]:


df.head()


# In[4]:


df2 = df.copy()


# In[5]:


df2 = df2.transpose()


# In[6]:


df2.columns = df2.iloc[0]


# In[7]:


df2.drop(index="total_production",inplace=True)


# In[8]:


pd.set_option('display.max_columns', None)


# In[9]:


df2.head()


# In[10]:


l = list()
for i in df2.columns:
    a = df2[i].sum()
    l.append(a)


# In[11]:


df.set_index("total_production",inplace=True)


# In[12]:


df["Overall_Production"] = l


# In[13]:


df.columns


# In[14]:


df3 = df.nlargest(10,columns="Overall_Production")


# In[15]:


df3


# In[16]:


l2 = []
for i in df3.index:
    b = i[0:2]
    l2.append(b.upper())


# In[17]:


l2


# In[18]:


fig , ax = plt.subplots(figsize=(6,6))
ax.bar(l2,df3["Overall_Production"]/1000000)
ax.set_title("Top Coffee Production Nation 1990-2018",fontsize=12)
ax.set_xlabel("Countries Producing Coffee")
ax.set_ylabel("Production in Million (60kg Bags)",fontsize=13)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False);


# In[19]:


top5 = df3.nlargest(5,columns="Overall_Production")


# In[20]:


top5.drop(columns="Overall_Production",axis=1,inplace=True)


# In[21]:


top5


# In[22]:


top5 = top5.transpose()


# In[23]:


top5


# In[24]:


top5.head()


# In[25]:


fig , ax =plt.subplots()
ax.plot(top5.index,top5["Brazil"]/1000,label="Brazil")
ax.plot(top5.index,top5["Viet Nam"]/1000,label="Viet Nam")
ax.plot(top5.index,top5["Colombia"]/1000,label="Colombia")
ax.plot(top5.index,top5["Indonesia"]/1000,label="Indonesia")
ax.plot(top5.index,top5["Ethiopia"]/1000,label="Ethiopia")
ax.legend()
ax.set_xticks(top5.index[::4]);
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("Top Coffee Producing Nations 1990-2018 \n Vietnam Surges to Number 2 Spot");
ax.set_ylabel("Production (Thousand 60kg Bags)");
ax.set_xlabel("Year of Production");


# In[26]:


df2.head()


# In[29]:


coffee = df2.sum()


# In[30]:


coffee.head()


# In[31]:


coffee_production = df2.assign(rest_of_world=df2.drop("Brazil",axis=1).sum(axis=1)).loc[:,["Brazil","rest_of_world",]].astype({"Brazil":"float64"})


# In[32]:


coffee_production


# In[33]:


fig , ax = plt.subplots()
ax.stackplot(coffee_production.index.astype("datetime64[ns]"),coffee_production["Brazil"],coffee_production["rest_of_world"],labels=["Brazil","Rest_Of_World"])
ax.legend(loc="upper left")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xlabel("Years",fontsize=12)
ax.set_ylabel("Production(60kg Bags)",fontsize=12)
ax.set_title("Brazil Production compare to Rest of the World",fontsize=13);


# In[34]:


df2.columns


# In[35]:


brazil_venezula = df2[["Brazil","Venezuela"]]


# In[36]:


brazil_venezula.head()


# In[37]:


fig , ax = plt.subplots()
ax.scatter(brazil_venezula["Brazil"],brazil_venezula["Venezuela"])
ax.set_xlabel("Brazil Production (Million 60kg Bag)",fontsize=12)
ax.set_ylabel("Venezuela Production (Million 60Kg Bag)")
ax.set_title("Venezuela Production declined while \n Brazil Increases by the years",fontsize=12);


# In[38]:


brazil_vietnam = df2[["Brazil",'Viet Nam']]


# In[39]:


fig , ax = plt.subplots()
ax.scatter(brazil_vietnam["Brazil"],brazil_vietnam["Viet Nam"])
ax.set_xlabel("Brazil Production (Million 60kg Bag)",fontsize=12)
ax.set_ylabel("Viet Nam Production (Million 60Kg Bag)")
ax.set_title("Venezuela Production Increase while \n Brazil Production Increases by the years",fontsize=12);


# In[40]:


coffee_production1 = df2.assign(rest_of_world=df2.drop(["Brazil","Viet Nam","Colombia","Indonesia","Ethiopia"],axis=1).sum(axis=1)).loc[:,["Brazil","rest_of_world","Viet Nam","Colombia","Indonesia","Ethiopia"]].astype({"Brazil":"float64","Viet Nam":"float64","Colombia":"float64","Indonesia":"float64","Ethiopia":"float64"})


# In[41]:


coffee_production1.head()


# In[42]:


coffee_production1=coffee_production1.transpose()


# In[43]:


coffee_production1


# In[44]:


coffee_production1["Total_P"]=coffee_production1.sum()


# In[45]:


l = coffee_production1.index


# In[46]:


l5 = list()
for i in l:
    b = coffee_production1.loc[i].sum()
    l5.append(b)


# In[47]:


coffee_production1["Total_pr"] = l5


# In[48]:


coffee_production1 = coffee_production1[["Total_pr"]]


# In[49]:


coffee_production1


# In[50]:


fig , ax = plt.subplots()
ax.pie(coffee_production1["Total_pr"],startangle=90,autopct="%.0f%%",labels=coffee_production1.index);


# In[51]:


df2.head()


# In[52]:


coffee_production.iloc[0]


# In[53]:


fig ,ax = plt.subplots()
ax.pie(coffee_production.iloc[0],colors=["Red","White"])
ax.text(0,0,"29%",fontsize=29)
donut_hole = plt.Circle((0,0),0.70,fc="white")
fig = plt.gcf()
fig.gca().add_artist(donut_hole)


# In[67]:


imports = pd.read_csv(r"C:\Users\DELL\Documents\imports.csv")


# In[68]:


imports.set_index("imports",inplace=True)


# In[71]:


imports.head()


# In[72]:


imports.shape


# In[104]:


imports.iloc[0]


# In[105]:


l1 = list()
for i in range(0,len(imports.index)):
    a = (imports.iloc[i].sum()/29)
    l1.append(a)


# In[106]:


range(0,len(imports.index))


# In[108]:


imports["Mean_of _production"]=l1


# In[109]:


imports


# In[114]:


imports.columns


# In[116]:


consumptions =imports['Mean_of _production']


# In[117]:


consumptions


# In[119]:


prices = pd.read_csv(r"C:\Users\DELL\Documents\retail-prices.csv")
prices.head()


# In[120]:


prices.set_index("retail_prices",inplace=True)


# In[122]:


prices.head()


# In[123]:


l2 = list()
for i in range(0,len(prices.index)):
    a = (prices.iloc[i].sum()/29)
    l2.append(a)


# In[125]:


prices["Average_prices"] = l2


# In[127]:


avg_price = prices["Average_prices"]


# In[130]:


avg_price.head()


# In[131]:


consumptions.head()


# In[152]:


price_con =pd.concat([consumptions, avg_price], axis=1).reset_index()


# In[155]:


price_con1 = price_con.copy()


# In[158]:


price_con1.dropna(axis="index",how="any",inplace=True)


# In[161]:


price_con1


# In[165]:


price_con1.sort_values("Mean_of _production",ascending=False,inplace=True)


# In[168]:


price_con1.set_index("index",inplace=True)


# In[175]:


price_con1.head()


# In[182]:


import numpy as np


# In[210]:


fig , ax = plt.subplots(figsize=(13,8))
width = 0.35
x = np.arange(0,len(price_con1.index))
bar1 = ax.bar(x-width/2,price_con1["Mean_of _production"],color="orange",width=width)
ax2=ax.twinx()
bar2 = ax2.bar(x+width/2,price_con1["Average_prices"],width=width)
plt.xticks(x,price_con1.index,fontsize=8);
ax.legend([bar1,bar2],["Mean Production","Average Price"],prop={"size":15});
fig.suptitle("Price Paid Vs Consumption of select Importing Nations",fontsize=16);
ax.set_ylabel("Consumption (k 60kg Bags)",fontsize=18);
ax2.set_ylabel("Average price paid per year",fontsize=18);


# Thanks a lot
