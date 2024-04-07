import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# matplot for graph  numpy for dataset   pandas for dataframe
#create dataset for graph(x,y) using numpy
x=np.arange(20,100)
y=np.arange(0,80)
# create a dataframe using numpy dataset by (pandas)
df1=pd.DataFrame(x)
df2=pd.DataFrame(y)
#for graph using matplotlib
plt.plot(df1,df2)
plt.show()


