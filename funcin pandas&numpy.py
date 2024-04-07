import numpy as np
import pandas as pd
#how to check null value in dataframe
mydata=pd.DataFrame([[0,np.nan,1],[1,2,3]])
print(mydata.isnull())
#how to convert dataframe into array
for i in mydata.values:
       for j in i:
            print(j)
#how to compare dataframe values and operations  
print(mydata>1)     
print(mydata+1)
print()
#how to check duplicate data exist or not
print(mydata.duplicated())
print()
#how to remove null value row(cleaning of dataset)
print(mydata.dropna())
#how to remove duplicate data
print(mydata.drop_duplicates(inplace=True))
