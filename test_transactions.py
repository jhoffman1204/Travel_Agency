from test_forms.db_manager import dbm
import sys
import pymysql.cursors

def print_new_table(table_name):
    connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')
    cursor = connection.cursor()

    print(cursor.execute("SELECT * FROM " + table_name))
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
        first_table = row

cmd = sys.argv[1]
if(cmd == 'Users'):
    dbm.add_new_user(email, password)
elif(cmd == 'Groups'):
    purpose = "test purpose"
    source_location = "source location"
    destination_location = "dest location"
    group_size = 10
    dbm.create_group(purpose , source_location,
        destination_location, group_size)
    print_new_table(cmd)
