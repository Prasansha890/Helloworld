#CRUD operation Create Read Update Delete on MYSQL
import mysql.connector
#Setup connection
myconnection = mysql.connector.connect(host='localhost',username='root',password='prasansha@89',database='mydb')
#Verify the connection
if myconnection.is_connected():
    print("DB connect")
else:
    print("DB not connect")

mycursor = myconnection.cursor()
#to create query  table    
createQuery="Create table if not exists VAM(stuname text,stuemail text,department text,mobile text);"
mycursor.execute(createQuery) 
myconnection.commit()
#to insert query
# i=0
# while (i<5):
#     insertQuery="insert into VAM values('{}','{}','{}','{}');".format(input("enter name"),input("enter email"),input("enter department"),input("enter mobile"))
#     i=i+1
#     mycursor.execute(insertQuery)
#     myconnection.commit()
#to update
updateQuery="update VAM set stuname='raj' , mobile='912345' where stuemail = 'pawan@gmail.com';"
mycursor.execute(updateQuery)    
myconnection.commit()