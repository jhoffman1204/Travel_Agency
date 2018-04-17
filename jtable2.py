#!/usr/bin/python
import pymysql.cursors

connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')

# first_table = "Users"

cursor = connection.cursor()
# print("Number of tables: " + str(cursor.execute("show tables")))
# row = cursor.fetchone()
# while row:
    # row = cursor.fetchone()
# print ("Adding " + str(first_table))
print(cursor.execute("SELECT * FROM Users"))
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
    first_table = row