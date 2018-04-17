# This python file adds all the tables from data.sql into our database

#!/usr/bin/python
import pymysql.cursors

connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')
cursor = connection.cursor()
print("Number of tables: " + str(cursor.execute("show tables")))
row = cursor.fetchall()

# Go thorugh entire list
count = 1
for x in row:
    print(str(count) + ": " + str(x[0]))
    count += 1

# Reading sql file and parsing
sqlFile = open ('data.sql', 'r')
sqlCommands = sqlFile.read()
sqlCommands = sqlCommands.split(';')
for command in sqlCommands:
    try:
        cursor.execute(command)
        print("Added table: " + str(command.split()[2]))
    except pymysql.err.InternalError as e:
        code, msg = e.args
        if code == 1050:
            print(msg)