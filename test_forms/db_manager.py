#!/usr/bin/python
import pymysql.cursors
from object_file import Flight_Obj

connection = pymysql.connect(   host = 'cse305group.cqjihdluaq5a.us-east-2.rds.amazonaws.com', 
                                user='jhoffman1204', 
                                password='cse305group', 
                                database='tagency')
cursor = connection.cursor()

class dbm:
    def print_test():
        print("testing")

#    def add_new_user(email, password):
#        cursor.execute("INSERT INTO Users(email,password) VALUES ('" + email + "','" + password + "')")
#        connection.commit()

    def create_group(purpose, src_loc, dest_loc, group_size):
        cursor.execute("INSERT INTO Groups(purpose, source_location, destination_location, group_size) VALUES ('" + str(purpose) + "','" + str(src_loc) + "','" + str(dest_loc) + "','" + str(group_size) + "')")
        connection.commit()

    def create_group_passenger(groupID, age, Name, gender):
        cursor.execute("INSERT INTO Groups(groupID, age, Name, gender) VALUES ('" + str(groupID) + "','" + str(age) + "','" + str(Name) + "','" + str(gender) + "')")
        connection.commit()

    def create_Payment(card_number, card_expiration_date, payment_type):
        cursor.execute("INSERT INTO Payment(card_number, card_expiration_date, payment_type) VALUES ('" + str(card_number) + "','" + str(card_expiration_date) + "','" + str(payment_type) + "')")
        connection.commit()

    def create_Accomodation(address , discount, rate_per_night):
        cursor.execute("INSERT INTO Accomodation(address, discount, rate_per_night) VALUES ('" + str(address) + "','" + str(discount)+ "','" + str(rate_per_night) + "')")
        connection.commit()

    def create_Accomodation_facilities(address, facilities):
        cursor.execute("INSERT INTO Accomodation_facilities(address, facilities) VALUES ('" + str(address) + "','" + str(facilities) + "')")
        connection.commit()
    
    def create_Cruise(source_location, arrival_date, depart_date, fare):
        cursor.execute("INSERT INTO Cruise(source_location, arrival_date, depart_date, fair) VALUES ('" + str(source_location) + "','" + str(arrival_date)+ "','" + str(depart_date)+ "','" + str(fare) + "')")
        connection.commit()

    def create_Cruise_destinations(cruise_number, destination):
        cursor.execute("INSERT INTO Cruise_destinations(cruise_number, destination) VALUES ('" + str(cruise_number) + "','" + str(destination_location) + "')")
        connection.commit()
    
    def create_Car_rental(confirmation_ID, car_type, rent):
        cursor.execute("INSERT INTO Car_rental(confirmation_ID, car_type, rent) VALUES ('" + str(confirmation_ID) + "','" + str(car_type)+ "','" + str(rent) + "')")
        connection.commit()
    
    def create_Flight(flight_number, carrier, classt, depart_date, arrival_date, fare, destination):
        cursor.execute("INSERT INTO Flight(flight_number, carrier, classt, depart_date, arrival_date, fare, destination) VALUES ('" + str(flight_number) + "','"+ str(carrier) + "','"+ str(classt) + "','"+ str(depart_date) + "','"+ str(arrival_date) + "','"+ str(fare) + "','" + str(destination) + "')")
        connection.commit()
    
    def create_Review(userId, rating, reiew_target, detailed_view):
        cursor.execute("INSERT INTO Review(userId, rating, review_target, detailed_review) VALUES ('" + str(userId) + "','"+ str(rating) + "','"+ str(review_target) + "','"+ str(detailed_review) + "')")
        connection.commit()
    
    def create_Group_transportation(mode_of_transport, groupID, travel_date):
        cursor.execute("INSERT INTO Group_Transportation(mode_of_transport, groupID, travel_date) VALUES ('" + str(mode_of_transport) + "','"+ str(groupID) + "','"+ str(travel_date) + "')")
        connection.commit()

    def create_Group_Payment(card_number, groupID, price):
        cursor.execute("INSERT INTO Group_Payment(card_number, groupID, price) VALUES ('" + str(card_number) + "','"+ str(groupID) + "','"+ str(price) + "')")
        connection.commit()

    def create_Group_Accomodation(address, groupID, cost, reservation_date):
        cursor.execute("INSERT INTO Group_Accomodation(address, groupID, cost, reservation_date) VALUES ('" + str(address) + "','"+ str(groupID) + "','"+ str(cost)+ "','"+ str(reservation_date) + "')")
        connection.commit()

        
    def print_all_users():
        cursor.execute("SELECT * FROM Users")
        row = cursor.fetchall()
        while row:
            print(row)
            row = cursor.fetchone()
            first_table = row

    def add_new_user(email, password):
        # Checks to make sure username is valid
        x = cursor.execute("SELECT email FROM Users WHERE email = '" + email + "';") 
        if len(cursor.fetchall()) > 0:
            return False
        else:
            cursor.execute("INSERT INTO Users(email,password) VALUES ('" + email + "','" + password + "')")
            connection.commit()
            dbm.print_all_users()
            return True

    def does_user_exist(email, password):
        x = cursor.execute("SELECT email, password FROM Users WHERE email = '" + email + "';") 
        profiles = cursor.fetchone()
        if len(profiles) > 0:
            if password == profiles[1]:
                return 1
            return -1
        else:
            return 0

    
    def retrieve_flights():
        cursor.execute("SELECT * FROM Flight")
        row = cursor.fetchall()
        
        flights = []
        first_table = row

        #print(row[2][6])

        for i in range(0, len(row)):
                flights.append(Flight_Obj(row[i][0],row[i][1],row[i][2],row[i][3],row[i][4],row[i][5],row[i][6]))
                
        return flights

dbm.retrieve_flights()