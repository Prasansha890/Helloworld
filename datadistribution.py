#for normal distribution
import random
import numpy as np
import matplotlib.pyplot as plt
#0=initial value 10=max value 1000 count values
#x=(np.random.normal(0,10,1000))
'''#print(x)
#plt.plot(x)
plt.grid()
plt.hist(x)
plt.show'''
#for uniform distribution
x=np.random.uniform(0,100,100000)
#plt.pie(x)
plt.grid()
plt.plot(x)
plt.show()
#we use distribution to work on huge data