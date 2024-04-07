import pandas as pd
import numpy as np
dataframe=pd.DataFrame(data=np.arange(0,4).reshape(2,2),index=["r1","r2"],columns=["c1","c2"])
print(dataframe[["c1","c2"]])