import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random

x=[]
y=[]
a=count()
def mylivegraph(i):
    x.append(next(a))
    y.append(random.randint(0,20))
    plt.cla
    plt.plot(x,y)
#gcf to draw figure of graph......funcanimation get 3 parameter
    #gcf get the current figure    
mygraph=FuncAnimation(plt.gcf(),mylivegraph,interval=700)
plt.show()    
