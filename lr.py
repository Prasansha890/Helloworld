import matplotlib.pyplot as plt
from scipy import stats
x=[89,43,36,95]
y=[21,46,3,35]
plt.scatter(x,y)
plt.grid()
plt.show()
slope,intercept,r,p,sta_err=stats.linregress(x,y)
print("coefficient of corelation:",r)
#no future prediction is there