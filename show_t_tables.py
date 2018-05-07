# This python file prints all tables in our database

#!/usr/bin/python
import pymysql.cursors
import sys

connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')
cursor = connection.cursor()

cursor.execute("SELECT * FROM Groups")
print("Groups: ")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print("Group_Payment: ")
cursor.execute("SELECT * FROM Group_Payment")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print("Payment: ")
cursor.execute("SELECT * FROM Payment")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print("Group_Accomodation: ")
cursor.execute("SELECT * FROM Group_Accomodation")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
print("Group_Transportation: ")
cursor.execute("SELECT * FROM Group_Transportation")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()