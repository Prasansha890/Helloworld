import os
# How to create a file
myfile=open("Prasansha.txt","w")
#How to wrie in file
myfile.write("My name is \nPrasansha")
#How to append a file
myfile=open("Prasansha.txt","a")
myfile.write(" \nSaubhari \nSharma")
#How to read a file
myfile=open("Prasansha.txt","r")
print(myfile.read())
# How to read the line
print(myfile.readline())
myfile.close()
#how to delete= os.remove("Prasansha.txt")