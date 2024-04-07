import matplotlib.pyplot as plt
from scipy import stats
#linear regression the best fit line near to all the points but linear y=mx+c(train amd test)
#slope,intercept,r(coefficient of error),p,std_err=stats.linregress?(x,y)
#if r is zero then linear regression cannot be best fit(bad fit)
# if r =-1 and r=1 best fit
x=[20,10,15,25]
y=[1000,500,800,1500]
plt.scatter(x,y)
plt.grid()
#plt.show()
slope,intercept,r,p,sta_err=stats.linregress(x,y)
print("coefficient of corelation:",r)
print("slope:",slope)
print("intercept:",intercept)
#print("polynomial error".p)
#To predict the future value
def futurevalue(x):
    return slope*x+intercept
y=futurevalue(50)
print("Future value",y)
# new y points for every x value
#To draw best fit line
modelY=list(map(futurevalue,x))
plt.plot(x,modelY)
plt.show()


