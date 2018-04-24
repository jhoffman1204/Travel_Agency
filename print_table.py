# This python file prints all tables in our database

#!/usr/bin/python
import pymysql.cursors
import sys

connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')
cursor = connection.cursor()

print("total: " , cursor.execute("SELECT * FROM Users"))
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()