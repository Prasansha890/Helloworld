#from scipy import stats
import statistics as stats
days={"rahul":0,"ivan":1,"kunal":2,"anshu":3,"rahul":4,"anjali":5,"aman":6}
x=stats.mode(days)
print(x)