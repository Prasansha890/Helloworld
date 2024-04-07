#from scipy import stats
import numpy as np
import statistics as stats
#mean using numpy
data=[1,2,3,3,4,7,9,11,15]
x=np.mean(data)
print(x)
#median using numpy
y=np.median(data)
print(y)
#mode using numpy
z=stats.mode(data)
print(z)

