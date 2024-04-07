import numpy as np
#how to find the standard devaition of the data set
#square root of variance is standard deviation
#(sigma)^2=Submission(x-u)/n
#x=values u=mean n=count
x=[5,10,20,25,40]
'''sum=0
su=0
c=0
u=np.mean(x)
n=5
for i in x:
    a=x-u
    b=(a*a)
for j in x:
    sum=sum+b  
for k in x:
    c=c+k;    
sigma=c/n
print(sigma)'''
m=np.var(x)
n=np.std(x)
print("Vatiance is:",m)
print("Standard deviation",n)