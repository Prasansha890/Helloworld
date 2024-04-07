#CRUD operation Create Read Update Delete on MYSQL
import mysql.connector
#Setup connection
myconnection = mysql.connector.connect(host='localhost',username='root',password='',database='Prasansha')
#Verify the connection
if myconnection.is_connected():
    print("DB connect")
else:
    print("DB not connect")
#DB operations on the database passed in the connection
# the cursor will execute all mysql commands and cursor will provided by the connection
mycursor = myconnection.cursor()
#to create query  table    
# createQuery="Create table if not exists SecA(stuname text,stuemail text);"
# mycursor.execute(createQuery) 
# myconnection.commit()
#insert query string so '{}' if int then only {}
#satic way for data insert
# insertQuery="insert into SecA values('{}','{}');".format("pawan","p@gmail.com")
#insertQuery="insert into SecA values('{}','{}');".format(input("enter name"),input("enter email"))
#mycursor.execute(insertQuery)
# myconnection.commit()
#for dynamic data insert user input
#format(input("enter name"),input("enter email"))
#continue data input until for condition N and Y
# to fetch data
#selectQuery="(Select * from SecA)"
# mycursor.execute(selectQuery)
#myconnection.commit()
# myrecord=mycursor.fetchall()
# for i in myrecord:
#            print(i)
# connection.commit()    
#where(from table name where column name)
#whereQuery="select * from SecA where stuname='ram';"
#mycursor.execute(whereQuery)
#how to update the data
updateQuery="delete from seca where stuemail = 'selectQuery=""'"
mycursor.execute(updateQuery)
# myrecord=mycursor.fetchall()
# for i in myrecord:
#            print(i)
myconnection.commit()  


