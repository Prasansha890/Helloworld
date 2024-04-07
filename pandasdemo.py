import pandas as pd
df=pd.read_csv("C:\\Users\\Admin\\Downloads\\CarMakers.csv")
#for printing data
'''print(df)
#print last 5 rows
df.tail()
#print first 5 rows
df.head()
#give the shape i.e, rows * col
df.shape
df.info()
df.describe()
df.dtypes'''
print(df.index)
#print(df.sample(3))
#to give null value we added
print(df.isnull().sum())
#to get where there is any duplicate
print(df.duplicated().sum())