import os

myfile=open("test.txt","w")
myfile.write("Name is Prasansha \t\tEmailid=prasansha89.sharma@gmail.com")
email=(input("enter email to check"))
a=myfile.read()
for i in a:
    if(a=="prasansha89.sharma@gmail.com"):
        print("exist")
    else:
        print("not exist")    