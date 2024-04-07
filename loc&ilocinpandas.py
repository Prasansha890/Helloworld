#loc for row and iloc for column are used to retrieve/find data from dataframe
#row also known as index
import pandas as pd
import numpy as np
#data frame allows parameter in it
mydata=np.arange(0,50).reshape(5,10)
mydataframe=pd.DataFrame(mydata)
print(mydataframe.loc[4])
print(mydataframe.iloc[1])
#to retrieve dataframe in row and column
print(mydataframe.iloc[0:2,0:2])

print(mydataframe.iloc[3:5,7:10]) 
a=print(mydataframe.iloc[1:3,0:2])
b=print(mydataframe.iloc[2:4,2:5])
