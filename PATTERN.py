a=int(input("enter rows"))
print("--------Right Angle Triangle--------")
for i in range(0,a):
    for j in range(0,i+1):
        print("*",end=" ")
    print()    
print("-------- Mirror Right Angle Triangle--------")
for i in range(1,a+1):
    for j in range(i,a):
        print(" ",end=" ")
    for k in range(1,i+1):   
        print("*",end=" ")
    print()
print("--------Equilateral Triangle--------")   
for i in range(1,a+1):
    for j in range(i,a):
        print(end=" ")
    for k in range(1,i+1):   
        print("*",end=" ")
    print()        
    

    
