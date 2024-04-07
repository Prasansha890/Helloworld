import pandas as pd
import numpy as np
#data frame allows parameter in it
mydata=np.arange(0,50).reshape(5,10)
mydataframe=pd.DataFrame(mydata)
print(mydataframe>20)
#airthmetic operation
print("original daraframe")
print(mydataframe)
print("\nafter operation")
print(mydataframe+10)