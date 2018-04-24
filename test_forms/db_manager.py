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
        
    def print_all_users():
        cursor.execute("SELECT * FROM Users")
        row = cursor.fetchall()
        while row:
            print(row)
            row = cursor.fetchone()
            first_table = row

    def add_new_user(email, password):
        dbm.print_all_users()
        # Checks to make sure username is valid
        x = cursor.execute("SELECT email FROM Users WHERE email = '" + email + "';") 
        if len(cursor.fetchall()) > 0:
            return False
        else:
            cursor.execute("INSERT INTO Users(email,password) VALUES ('" + email + "','" + password + "')")
            return True

    def does_user_exist(email, password):
        x = cursor.execute("SELECT email FROM Users WHERE email = '" + email + "';") 
        if len(cursor.fetchall()) > 0:
            user = cursor.fetchone()
            return True
        else:
            cursor.execute("INSERT INTO Users(email,password) VALUES ('" + email + "','" + password + "')")
            return False