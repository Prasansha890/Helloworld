import numpy as np

myArr = np.array([1,2,3,4,5])
print(myArr)
for i in range(5):
   print(myArr[i])
   
print(type(myArr))
print("value of 2nd element ",myArr[1])

myArr[1] = 5
print("Updated Array : ",(myArr))

zeroArr = np.array(24)
print(zeroArr)
print(type(zeroArr))

twoArr = np.array([[1,2],[2,3],[3,4],[4,5]])
print(twoArr)
print("\nElement twoArr[1][1] : ",twoArr[1][1])

print("\n2D ARRAY BY ITERATOR : SINGLE FOR LOOP ")
for i in np.nditer(twoArr) :
    print(i)

print("\n\nprinting 2D Array : ")
for i in range(4):
    for j in range(2):
        print("twoArr[",i,"][",j,"] = ",twoArr[i][j]) 


"""
threeArr = np.array([[[1,2,3],[2,3,4],[4,5,6]]])
print(threeArr)

for i in range(3):
   for j in range(3):
       for k in range(3):
           print(threeArr[i][j][k])

threeArr[2,2,2] = 10
print(threeArr[2,2,2])

"""
#Numpy IS THE PYTHON LIBRARY WHICH WORK ON ARRAY AND IT IS 50 TIMES FASTER THAN PYTHON DEFAULT DATA SET (SET, LISTS, TUPLE, ARRAY)
#IT IS ALSO HAVING THE HIGH ORDER FUNCTION
#BASICALLY NUMPY CAN SAVE THE COMPLEX MATRIX PROBLEM.

# ZERO DIMENSIONAL ARRAY :- zeroArr = np.array(24)
# ONE DIMENSIONAL ARRAY  :- oneArr  = np.array([1,2,3,4,5])
# TWO DIMENSIONAL ARRAY  :- twoArr  = np.array([[1,2],[2,3],[3,4],[4,5]])
# THREE DIMENSIONAL ARRAY :- threeArr = np.array([[[1,2,3],[2,3,4],[3,4,5]]])


#RESHAPE FUNCTION
x = np.array([1,2,3,4])
print("\nArray of order 1X4\n",x)

y=x.reshape(2,2)
print("\nArray of order 2X2\n",y)
z=x.reshape(4,1)
print("\nArray of order 4X1\n",z)

print("\nARRAY X[2:4]",x[2:4])

#COPY AN ARRAY FROM AN ANOTHER ARRAY
y = x.copy()
print("\nY AS A COPY OF X ",y)


#VIEW FUNCTION :- VIEW ALWAYS SHOW THE CURRENT DATA BUT COPY WILL SHOW THE ORIGINAL DATA.

z=x.view()
print("\nZ as view of x: ",z)
x[1] = 10
print("\nZ as view of x after change: ",z)


#ARRAY JOINS :- IT CAN COMBINE TWO ARRAY
a = np.array([1,2,3]) 
b = np.array([2,3,4]) 
c = np.array([10,20,30])
d = np.concatenate((a,b,c))
print("a : ",a)
print("b : ",b)
print("c : ",c)
print("\nConcatenate a,b and c : ",d)

#ARRAY SPLIT : IT CAN BREAK AN ARRAY INTO MULTIPLE PARTS(ARRAY)
x = np.array ([1,2,3,4,5,6])
y = np.array_split(x,4)
print("\nSplitting array :",y)


#SEARCHING :- IT WILL CHECK THE PARTICULAR ELEMENT IS AVAILABLE IN GIVEN ARRAY OR NOT USING where() function
x = np.array ([1,2,3,4,5,6])
y = np.where(x==4)
print("\nSearching 4 in x : ",y) 

a = np.array(["Hi", "Bye", "Why"])
b = np.where(a=='Why')
print("\na: ",a)
print("Searching Why in a: ",b)

#ARRAY SORTING : IT CAN ARRANGE THE DATA THE UNORDERED DATA IN TO THE ORDER 
x = np.array([5,3,7,10,8])
y = np.sort(x)
print("\n Sorted data ",y)

#RANDOM FUNCTION
from numpy import random
x =  random.randint(9999)
print("\nRandom : ",x)