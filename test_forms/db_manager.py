#!/usr/bin/python
import pymysql.cursors

connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')
cursor = connection.cursor()

class dbm:
    def print_test():
        print("testing")
    def add_new_user(email, password):
        # Checks to make sure username is valid
        x = cursor.execute("SELECT COUNT(*) FROM Users WHERE email = '" + email + "';")
        if x > 0:
            print("Username in use")
            return False
        
        # If username is valid create a new user
        print("new user created with username " , email 
             , "and email " , password)
        cursor.execute("INSERT INTO Users(email,password) VALUES ('" + email + "','" + password + "')")
        
        print(cursor.execute("SELECT * FROM Users"))
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
            first_table = row
        return True