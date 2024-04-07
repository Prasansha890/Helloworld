import matplotlib.pyplot as plt
import numpy as np
#from scipy import stats for linear  regression only
#polynomail regression
#myline=np.linspace(10,25,100) for x
x=[20,10,15,25]
y=[1000,500,800,1500]
plt.grid()
modelY=np.poly1d(np.polyfit(x,y,3))
myline=np.linspace(10,25,100)
plt.scatter(x,y)
plt.plot(myline,modelY(myline))
plt.show()
newvalue=modelY(25)
print(newvalue)

