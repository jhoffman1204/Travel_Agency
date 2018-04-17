#!/usr/bin/python
import pymysql.cursors

connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')

first_table = ""

cursor = connection.cursor()
print("Number of tables: " + str(cursor.execute("show tables")))
row = cursor.fetchone()
while row:
    first_table = row[0]
    print(row[0])
    row = cursor.fetchone()
print ("Removing table " + str(first_table))
cursor.execute("DROP TABLE `" + str(first_table) + "`")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
    first_table = row