import pandas as pd
import numpy as np
#data frame allows parameter in it
#dataframe=pd.DataFrame(data=np.arange(0,100).reshape(50,2))
dataframe=pd.DataFrame(data=np.arange(0,9).reshape(3,3),index=["r1","r2","r3"],columns=["c1","c2","c3"])
print(dataframe)
#top 10 record
'''print(dataframe.head(10))
#bottom 8 record
print(dataframe.tail(8))
#how to provide name for column and row index name'''
#dataframe combination of row and column.......series single row or single column(subset of dataframe)
#how to access data from dataframe as series
#print(dataframe[0])
