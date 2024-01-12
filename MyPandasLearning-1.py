#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# DataFrame is the object that is used to represent data in from of Rows and Columns

# Different ways to create DataFrame Objects

# Creation of Dataframe using List

# In[6]:


mylist = [10,20,30]
df = pd.DataFrame(mylist)
print(df)


# Creation of Dataframe using Tuple

# In[8]:


mytuple= (10,20,30)
df = pd.DataFrame(mytuple)
print(df)


# Creation of Dataframe using Dictionary

# In[10]:


mydict = {"A":101,"B":102,"C":103,"D":104}
df = pd.DataFrame(mydict,index=["a","b","c","d"])
print(df)


# Creation of Dataframe using CSV

# In[14]:


myfile = pd.read_csv(r"C:\Users\DELL\Downloads\apple_products.csv")
df = pd.DataFrame(myfile)
print(myfile)


# Creation of Dataframe using Excel

# In[16]:


myfile = pd.read_excel(r"C:\Users\DELL\Documents\Manufacturer sales data.xlsx")
df = pd.DataFrame(myfile)
print(df)


# Creation of Dataframe using Clipboard

# In[17]:


df = pd.read_clipboard()
print(df)


# How to export Python Pandas DataFrame to CSV and EXCEL files

# In[23]:


myfile = pd.read_csv(r"C:\Users\DELL\Downloads\apple_products.csv")
df = pd.DataFrame(myfile)
df.to_csv(r"E:\Python 100 Days\Pandas\CSV.csv",index=False)


# In[25]:


myfile = pd.read_excel(r"C:\Users\DELL\Documents\Manufacturer sales data.xlsx")
df = pd.DataFrame(myfile)
df.to_excel(r"E:\Python 100 Days\Pandas\EXCEL.xlsx")


# Attributes of DataFrame

# In[30]:


#index 
mylist = [(101,"Vishal",9000),(102,"Manish",10000),(103,"Kartik",8900)]
df = pd.DataFrame(mylist,index=["A","B","C"])
df


# In[31]:


#columns
df = pd.DataFrame(mylist,columns=["Roll No","Name","Money"])
df


# In[32]:


df = pd.DataFrame(mylist,index=["A","B","C"],columns=["Roll No","Name","Money"])
df


# Size = Tells about total number of elements present in the dataframe

# In[34]:


df.size


# Shape = Tells about the number of rows and columns in dataframe

# In[35]:


df.shape


# In[36]:


print("Number of Rows : ",df.shape[0])
print("Number of Columns : ",df.shape[1])


# ndim - Tells about the dimension , in our case when we are using dataframe then ndim will be always 2 , which means 2 Dimension

# In[37]:


df.ndim


# Columns - Use to get all columns of dataframe

# In[46]:


df.columns


# memory_usage - Tells about the memory occupied by the Dataframe including its index also

# In[38]:


df.memory_usage()


# Sclicing in Pandas DataFrame

# In[40]:


myfile = pd.read_csv(r"C:\Users\DELL\Downloads\apple_products.csv")
df = pd.DataFrame(myfile)
df


# In[41]:


df.shape


# Head method - Head method display top rows of dataframe , by default it display top 5 rows if no argument is given

# In[42]:


df.head()


# In[43]:


df.head(10)


# Tail method - Tail method display Bottom  rows of dataframe , by default it display Bottom 5 rows if no argument is given

# In[44]:


df.tail()


# In[45]:


df.tail(13)


# dataframe_name["Column Name"] used to get only column Name details , it include all rows but only the column whose name is given

# In[47]:


df.columns


# In[48]:


df["Brand"]


# In[49]:


df["Brand"].head()


# In[50]:


df["Brand"].tail()


# dataframe_name[["Column Name 1","Column Name 2"]]  used to get only column Name details of two or more columns , it include all rows but only the column whose name is given

# In[51]:


df.columns


# In[52]:


df[["Product Name","Brand"]]


# In[53]:


df[["Product Name","Brand","Upc"]]


# In[54]:


df[["Product Name","Brand"]].head()


# In[55]:


df[["Product Name","Brand"]].tail()


# dataframe_name[start:stop:end] here we can do sciling , on rows .

# In[56]:


df[1:15]


# In[57]:


df[1:15:2]


# Sciling in columns

# In[58]:


df.columns


# In[60]:


df["Product Name"][1:15]


# In[61]:


df[["Product Name","Brand"]][10:15]


# How to Handle missing values in pandas Datframe

# In[63]:


myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\CSV.csv")
df = pd.DataFrame(myfile)
df.head()


# dataframe_name.isnull() is a method to check null values in dataframe it return boolean results True(for null values) and False(no-null values)

# In[64]:


df.isnull()


# dataframe_name.isnull().sum() will count the number of null values in each columns

# In[65]:


df.isnull().sum()


# dataframe_name.dillna(fill) we replace the NaN (null values) with fill value.

# Remember dataframe is immutable datatype so we have to make another dataframe to store changes or we can use inplace parameter to make changes in original dataframe

# In[69]:


df1=df.fillna("Hello")  
df1
#or
# df.fillna("Hello",inplace=True)


# dataframe_name.dropna() will simly drop all the null values from dataframe

# In[70]:


df2=df.dropna()
df2
#or
#df.dropna(inplace=True)


# In[74]:


df["Sale Price"].head(10).fillna("Hello")


# Sorting Pandas Dataframe

# dataframe_name.sort_index() and dataframe_name.sort_values()

# In[76]:


df.sort_index()   # sort on the basis of index


# In[77]:


df.sort_index(ascending=False) # sorting will done in descending order on the basis of index


# df.sortvalues("column Name")  or df.sort_values(["Column 1","Column 2"])

# In[78]:


df.columns


# In[79]:


df.sort_values("Ram")


# In[80]:


df.sort_values(["Ram","Star Rating"])


# In[81]:


df.sort_values("Star Rating",ascending=False)


# In[83]:


df.sort_values(["Star Rating","Ram"],ascending=False)


# In[84]:


df.sort_values("Star Rating",ascending=[0])  # works same as acending = Flase


# How to handel Duplicates in Pandas DataFrame

# In[85]:


myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\CSV.csv")
df = pd.DataFrame(myfile)
df


# dataframe_name.duplicated tells return boolean values True(Duplicates) and False(No duplicates)

# In[88]:


df.duplicated()


# In[91]:


df.drop_duplicates(inplace=True)


# If your dataframe is havind duplicate values then all duplicates values will be removed inplace is used to make changes in original df

# More in Pandas DataFrame 

# dataframe_name["Column Name"].nunique() , Tells us about the number of unique values present in particular column.

# df.columns

# In[93]:


df["Mrp"].nunique() # Tells us about the number of unique values present in particular column.


# dataframe_name["Column Name"].unique() ,  Will return the list will all unqiues values .

# In[94]:


df["Mrp"].unique() 


# dataframe_name.rename(columns={column name : column name},inplace=True) , Changes the particular cloumn name of dataframe

# In[95]:


df.columns


# In[96]:


df.rename(columns={"Brand":"Brand Name"},inplace=True) #Here we are going to change the Brand column to Brand Name


# In[98]:


df.head()


# How to apply filter on Pandas Dataframe using loc and iloc

# loc method - Label wise data selection 

# In[99]:


df.columns


# df.loc[row,cloumn name]

# In[100]:


df.loc[3,"Product Name"]


# In[102]:


df.loc[3,"Number Of Ratings"]


# In[103]:


df.loc[3,["Product Name","Number Of Ratings"]]


# In[104]:


df.loc[1:5,"Product Name"]


# In[105]:


df.loc[1:5,["Product Name","Ram"]]


# iloc = index wise data selection

# In[106]:


df.columns


# df.iloc[row index , column index]

# In[107]:


df.iloc[3,2]


# In[109]:


df.iloc[3,3] 


# In[112]:


df.iloc[3,[3,4]]


# In[113]:


df.iloc[1:10,2] # 1:10 10 is excluded


# In[114]:


df.iloc[1:10,[2,4]]


# More in loc and iloc

# df.loc[df["Column name"]condition]

# In[115]:


df.columns


# In[116]:


df.loc[df["Ram"]=="2 GB"]


# In[117]:


df.loc[df["Star Rating"]>4.4]


# In[118]:


df.loc[(df["Star Rating"]>4.4) & (df["Ram"]=="2 GB")]


# In[119]:


df.columns


# In[120]:


df.loc[(df["Ram"]=="2 GB") | (df["Ram"]=="4 GB")]


# Advance Data Analysis Using Pandas 

# Join in Pandas DataFrame , Where condition , Aggregate Function , Groupby , Sql Equivalent Statements , Regular Expression , Concat

# Inner join is the most common type of join you’ll be working with. It returns a dataframe with only those rows that have common characteristics. source = Analytics Vidhya

# In[7]:


import pandas as pd
customer=pd.DataFrame({
    'id':[1,2,3,4,5,6,7,8,9],
    'name':['Olivia','Aditya','Cory','Isabell','Dominic','Tyler','Samuel','Daniel','Jeremy'],
    'age':[20,25,15,10,30,65,35,18,23],
    'Product_ID':[101,0,106,0,103,104,0,0,107],
    'Purchased_Product':['Watch','NA','Oil','NA','Shoes','Smartphone','NA','NA','Laptop'],
    'City':['Mumbai','Delhi','Bangalore','Chennai','Chennai','Delhi','Kolkata','Delhi','Mumbai']
})
product=pd.DataFrame({
    'Product_ID':[101,102,103,104,105,106,107],
    'Product_name':['Watch','Bag','Shoes','Smartphone','Books','Oil','Laptop'],
    'Category':['Fashion','Fashion','Fashion','Electronics','Study','Grocery','Electronics'],
    'Price':[299.0,1350.50,2999.0,14999.0,145.0,110.0,79999.0],
    'Seller_City':['Delhi','Mumbai','Chennai','Kolkata','Delhi','Chennai','Bengalore']
})


# In[6]:


customer


# In[8]:


product


# In[10]:


pd.merge(customer,product,on="Product_ID",how="inner")


# Full Join, also known as Full Outer Join, returns all those records which either have a match in the left or right dataframe.

# pd.merge(customer,product,on="Product_ID",how="outer")

# Left join, also known as Left Outer Join, returns a dataframe containing all the rows of the left dataframe.
# pd.merge(df1=left,df2=right,on="column name",how="type of join")

# In[12]:


pd.merge(customer,product,on="Product_ID",how="left")


# Right join, also known as Right Outer Join, is similar to the Left Outer Join. The only difference is that all the rows of the right dataframe are taken as it is and only those of the left dataframe that are common in both.

# In[13]:


pd.merge(customer,product,on="Product_ID",how="right")


# In the above example we were having one column that was same o both dataframes ,but when we have two different dataframes

# In[15]:


import pandas as pd
customer=pd.DataFrame({
    'id':[1,2,3,4,5,6,7,8,9],
    'name':['Olivia','Aditya','Cory','Isabell','Dominic','Tyler','Samuel','Daniel','Jeremy'],
    'age':[20,25,15,10,30,65,35,18,23],
    'P-ID':[101,0,106,0,103,104,0,0,107],
    'Purchased_Product':['Watch','NA','Oil','NA','Shoes','Smartphone','NA','NA','Laptop'],
    'City':['Mumbai','Delhi','Bangalore','Chennai','Chennai','Delhi','Kolkata','Delhi','Mumbai']
})
product=pd.DataFrame({
    'Product_ID':[101,102,103,104,105,106,107],
    'Product_name':['Watch','Bag','Shoes','Smartphone','Books','Oil','Laptop'],
    'Category':['Fashion','Fashion','Fashion','Electronics','Study','Grocery','Electronics'],
    'Price':[299.0,1350.50,2999.0,14999.0,145.0,110.0,79999.0],
    'Seller_City':['Delhi','Mumbai','Chennai','Kolkata','Delhi','Chennai','Bengalore']
})


# In[16]:


customer


# In[17]:


product


# pd.merge(datframe1 , datframe2 , left_on = "column name", right_on = "column name",how="type of join")

# In[18]:


pd.merge(customer,product,left_on="P-ID",right_on="Product_ID",how="inner")


# In[20]:


pd.merge(customer,product,left_on="P-ID",right_on="Product_ID",how="outer")


# In[21]:


pd.merge(customer,product,left_on="P-ID",right_on="Product_ID",how="left")


# In[22]:


pd.merge(customer,product,left_on="P-ID",right_on="Product_ID",how="right")


# By default when we dont give type of join then , inner join is the default value of how 

# In[23]:


pd.merge(customer,product,left_on="P-ID",right_on="Product_ID")


# Where function - Pandas where() method in Python is used to check a data frame for one or more conditions and return the result accordingly. By default, The rows not satisfying the condition are filled with NaN value.

# In[25]:


myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\nba.csv")
df = pd.DataFrame(myfile)
df.head(10)


# First to use where we have to set index of our dataframe using set_index(cloumn_name) it will change the particular column name to index

# In[26]:


df.set_index("Team",inplace=True)


# In[28]:


df.head(3)


# In[31]:


df.where(df["Position"]=="PG")


# In[32]:


df.where(df["Position"]=="PG","SMILE")


# In[34]:


df.head(5)


# In[ ]:





# In[40]:


import pandas as pd
technologies= {
    'Courses':["Spark","PySpark","Spark","Python","PySpark"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Discount':[1500,1000,1200,800,1300],
    'Duration':['30days','50days','30days','35days','40days']
          }
df = pd.DataFrame(technologies)
df


# In[42]:


df.where(df["Fee"]>25000)


# In[43]:


df.where(df["Fee"]>24000,"Hi")


# In[47]:


cond1 = df["Fee"]>24000
cond2 = df["Courses"]=="Python"
df.where(cond1 & cond2,"Hi")


# Concatination in Dataframe 
# concat([df1,df2])
# Use to concat two different datframe together

# In[60]:


import pandas as pd
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']},index=["a","b","c","d"])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7']},index=["m","n","o","p"])


# In[58]:


df1


# In[61]:


df2


# In[62]:


pd.concat([df1,df2])


# In[63]:


pd.concat([df1,df2],ignore_index=True)


# In[67]:


pd.concat([df1,df2],axis=1)


# Groupby function 
# Pandas groupby is used for grouping the data according to the categories and applying a function to the categories. 

# In[68]:


import pandas as pd
myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\nba.csv")
df = pd.DataFrame(myfile)


# In[69]:


df


# In[70]:


df["Team"].value_counts()


# In[74]:


df1 = df.groupby("Team")


# In[77]:


for i in df1:
    print(i)


# In[83]:


df2=df1.get_group("Atlanta Hawks")
df1.get_group("Atlanta Hawks")


# In[81]:


df2.dropna()


# Aggregate Function in Pandas Dataframe mean , mode , max,  min 

# In[84]:


import pandas as pd
myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\nba.csv")
df = pd.DataFrame(myfile)
df


# In[89]:


df1 = df.groupby("Team")


# In[90]:


df1.get_group("Boston Celtics")


# In[91]:


df1.get_group("Boston Celtics").agg(max)


# In[93]:


df1.get_group("Boston Celtics").agg(min)


# In[94]:


df1.get_group("Boston Celtics").agg([min,max])


# In[96]:


df.groupby("Team").agg([min,max])


# In[99]:


df.groupby("Team").agg([min,max])


# In[100]:


df.describe()


# In[101]:


df.info()


# In[104]:


df["Team"].unique()


# In[109]:


df.loc[df["Team"]=="Boston Celtics"].describe()


# Use of isin() and not isin() help in return the data of exact value given

# In[110]:


import pandas as pd
myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\nba.csv")
df = pd.DataFrame(myfile)
df


# In[112]:


df[df.Age.isin([25.0,27.0])]


# In[113]:


df[df.Team.isin(["Boston Celtics","Portland Trail Blazers"])]


# In[ ]:





# In[114]:


df[~ df.Team.isin(["Boston Celtics"])]   # we use negotion so , we will get all teams data except Boston Celtics


# How to use nlargest in Pandas dataframe use to find largest among the columns 

# In[116]:


df.nlargest(4,columns="Age")


# In[119]:


df.nlargest(10,columns="Weight").tail(5)


# Sql equivalent statement in pandas datframe
# 

# In[120]:


import pandas as pd
myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\employees.csv")
df = pd.DataFrame(myfile)
df


# Q - Find all the employee details whose salary is above 60,000 

# In[121]:


df[df.Salary>60000]


# Q - Find all the person name whose salary is above 75000

# In[130]:


df[df.Salary>75000]["First Name"]


# Q - Find the salary and emolyee nam eof a employee whose team is Marketing

# In[131]:


df[df.Team=="Marketing"][["First Name","Salary"]]


# Q - Find the employee deatails who is male and working in Finance department

# In[139]:


df[(df.Team=="Finance") & (df.Gender=="Male")]


# Q - Find the deatails of emoloyee working in finance as well as Marketing

# In[140]:


df[(df.Team=="Finance") | (df.Team=="Marketing")]


# Q - Find the deatils of employee whose name is rose , anthony and gloria

# In[141]:


df.rename(columns={"First Name":"FirstName"},inplace=True)


# In[142]:


df.head(3)


# In[143]:


df[df.FirstName.isin(["Gloria","Rose","Anthony"])]


# How to update , delete  data from dataframe 

# In[145]:


df.head()


# In[146]:


df.drop(df[df.FirstName=="Rose"].index)


# In[156]:


df.loc[df["Salary"]==97308,"Salary"]=100000
df


# In[171]:


myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\nba.csv",index_col="Name")
df = pd.DataFrame(myfile)
df


# In[172]:


df.drop(["R.J. Hunter"])


# In[175]:


myfile = pd.read_csv(r"E:\Python 100 Days\Pandas\nba.csv")
df = pd.DataFrame(myfile)
df.set_index("Name",inplace=True)


# In[176]:


df


# In[ ]:


Remember by using set index method you cannot drop rows it will show aixs error.....


# Thanks For Reading till here'
