#!/usr/bin/python
import pymysql.cursors

connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')

first_table = "Transportation"

cursor = connection.cursor()
print("Number of tables: " + str(cursor.execute("show tables")))
row = list(cursor.fetchall())
while(len(row) > 0):
    for x in row:
        first_table = x[0]
        print ("Removing table " + str(first_table))
        try:
            cursor.execute("DROP TABLE `" + str(first_table) + "`")
            row.remove(x)
        except:
            pass